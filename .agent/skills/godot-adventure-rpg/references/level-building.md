# Level Building — TileMap, Rooms, Indoor/Outdoor, Transitions

---

## Level Scene Structure (every level uses this)

```
Level (Node2D)
  ├── World (Node2D)
  │     ├── WaterLayer      (TileMapLayer  z_index=-3)
  │     ├── GroundLayer     (TileMapLayer  z_index=-2)   ← grass/stone/sand terrain
  │     ├── DecalLayer      (TileMapLayer  z_index=-1)   ← scattered flowers, cracks
  │     ├── WallLayer       (TileMapLayer  z_index=0 )   ← dungeon walls (indoor only)
  │     ├── RoofLayer       (TileMapLayer  z_index=5 )   ← fades when player under it
  │     ├── NavigationRegion2D                           ← baked walkable mesh
  │     └── PointLight2D nodes (torches, windows…)
  │
  ├── Entities (Node2D — Y-Sort enabled)
  │     ├── Player  (instance)
  │     ├── Enemy spawns (populated at runtime)
  │     ├── NPCs
  │     └── Interactables (chests, save points, doors)
  │
  ├── Projectiles (Node2D — Y-Sort OFF)
  │     └── (bullets, arrows, spells spawned here)
  │
  ├── VFX (Node2D)
  │     └── (damage numbers, explosions, particles)
  │
  ├── Rooms (Node2D)         ← indoor only: each child is a Room node
  │     ├── Room_A (Node2D)
  │     ├── Room_B (Node2D)
  │     └── ...
  │
  ├── Doors (Node2D)
  │     └── (Door instances — level transition triggers)
  │
  ├── BlobSpawnMarkers (Node2D)
  │     └── (Marker2D positions where enemies spawn)
  │
  ├── Overlay (CanvasLayer)
  │     ├── DayTimeColor (CanvasModulate)
  │     ├── DayTransitionLayer (ColorRect + circle_transition shader)
  │     ├── RainParticles (GPUParticles2D)
  │     └── VignetteLayer (ColorRect + vignette shader)
  │
  └── Timers (Node)
        ├── EnemySpawnTimer
        └── AmbientTimer
```

---

## Outdoor Level Setup

### Step 1 — Terrain Layers

**GroundLayer (grass, dirt, stone):**
1. `Add TileMapLayer` → Inspector → TileSet → New TileSet
2. Drag `graphics/tilesets/grass.png` into Sources → Create Atlas
3. TileSet → Terrain Sets → Add → Mode: `Match Corners and Sides` → name "Grass"
4. Paint connections on all tile variants (see `godot-engine-guide.md` section 7)
5. Physics Layer → Add → layer=1 (Terrain), mask=0
6. Paint collision polygons on all edge tiles

**WaterLayer (animated):**
1. `TileMapLayer` → z_index=-3
2. New TileSet → drag `water.png` → No Atlas
3. Select tile → Animation tab → Columns=4 → Frames: add 4 at 0.4s each
4. Paint water tiles around the island perimeter

**DecalLayer (details, no collision):**
- Scatter tile variants: pebbles, flowers, grass tufts
- Use probability < 0.1 for rare variants (set in TileSet terrain tile probability)

### Step 2 — Navigation Bake
1. Add `NavigationRegion2D` wrapping the walkable area
2. Inspector → NavigationPolygon → New NavigationPolygon
3. Enable: `Geometry → Parsed Geometry Type → Static Colliders`
4. Click **Bake NavigationPolygon** — Godot traces from your TileMap collision
5. Re-bake after every tile edit

### Step 3 — Enemy Spawn System
```gdscript
# scenes/levels/level_base.gd  (all levels extend this)
extends Node2D

@onready var spawn_markers  = $BlobSpawnMarkers.get_children()
@onready var entities       = $Entities
@onready var spawn_timer    = $Timers/EnemySpawnTimer

var level_id    : String
var max_enemies : int   = 8
var enemy_count : int   = 0

func _ready() -> void:
    level_id = _get_level_id()
    EventBus.enemy_died.connect(_on_enemy_died)
    spawn_timer.timeout.connect(_spawn_enemy)
    spawn_timer.start()
    # Auto-save on level entry
    GameManager.save_game()

func _get_level_id() -> String:
    return "level_01_outdoor"   # override per level

func _spawn_enemy() -> void:
    if enemy_count >= max_enemies: return
    var level_data  = Data.LEVEL_DATA[level_id]
    var spawn_table = level_data["enemy_spawn_table"]
    var enemy_type  = _weighted_pick(spawn_table)
    var marker      = spawn_markers[randi() % spawn_markers.size()]
    var scene_path  = _get_enemy_scene(enemy_type)
    var enemy       = load(scene_path).instantiate()
    entities.add_child(enemy)
    enemy.global_position = marker.global_position
    enemy.died.connect(_on_enemy_died_pos)
    enemy_count += 1

func _on_enemy_died(_type, _pos: Vector2) -> void:
    enemy_count = max(0, enemy_count - 1)

func _weighted_pick(table: Array) -> Enum.EnemyType:
    var total  = table.reduce(func(a, b): return a + b["weight"], 0)
    var roll   = randi() % total
    var cumul  = 0
    for entry in table:
        cumul += entry["weight"]
        if roll < cumul:
            return entry["type"]
    return table[0]["type"]

func _get_enemy_scene(type: Enum.EnemyType) -> String:
    match type:
        Enum.EnemyType.GRUNT:   return "res://scenes/enemies/grunt.tscn"
        Enum.EnemyType.ARCHER:  return "res://scenes/enemies/archer.tscn"
        Enum.EnemyType.MAGE:    return "res://scenes/enemies/mage.tscn"
        _:                      return "res://scenes/enemies/grunt.tscn"
```

---

## Indoor / Dungeon Level Setup

### Room System

Each dungeon is a collection of rooms. Rooms activate when the player enters,
lock doors while enemies are alive, and unlock when cleared.

**Room node structure:**
```
Room_A (Node2D)
  ├── FloorLayer   (TileMapLayer  z_index=-2)
  ├── WallLayer    (TileMapLayer  z_index=0 , physics layer 1)
  ├── RoofLayer    (TileMapLayer  z_index=5 )
  ├── EnemySlots   (Node2D)   ← enemies instantiated here on room activation
  ├── Doors        (Node2D)   ← 1-4 doors (N/S/E/W)
  ├── TriggerArea  (Area2D)   ← activates room when player enters
  └── Decorations  (Node2D)   ← chests, torches, barrels
```

```gdscript
# scenes/levels/room.gd
extends Node2D

@export var room_id         : String
@export var enemy_types     : Array[Enum.EnemyType] = []
@export var door_directions : Array[String]          = ["north", "south"]

var room_state      : Enum.RoomState = Enum.RoomState.LOCKED
var enemies_alive   : int            = 0

@onready var trigger    = $TriggerArea
@onready var enemy_node = $EnemySlots
@onready var doors_node = $Doors

func _ready() -> void:
    trigger.body_entered.connect(_on_player_entered)
    # Mark all doors as locked initially
    for door in doors_node.get_children():
        door.lock()

func _on_player_entered(body: Node2D) -> void:
    if not body.is_in_group("Player"): return
    if room_state != Enum.RoomState.LOCKED: return
    room_state = Enum.RoomState.ACTIVE
    _spawn_enemies()
    _lock_doors()

func _spawn_enemies() -> void:
    var spawn_positions = $EnemySlots.get_children()
    var positions = spawn_positions.duplicate()
    positions.shuffle()
    for i in min(enemy_types.size(), positions.size()):
        var enemy = _load_enemy(enemy_types[i]).instantiate()
        enemy_node.add_child(enemy)
        enemy.global_position = positions[i].global_position
        enemy.died.connect(_on_enemy_died)
        enemies_alive += 1

func _on_enemy_died(_type, _pos) -> void:
    enemies_alive = max(0, enemies_alive - 1)
    if enemies_alive == 0:
        room_state = Enum.RoomState.CLEARED
        _unlock_doors()
        _spawn_cleared_rewards()
        EventBus.room_cleared.emit(room_id)

func _lock_doors() -> void:
    for door in doors_node.get_children():
        door.lock()

func _unlock_doors() -> void:
    for door in doors_node.get_children():
        door.unlock()
    # Slow-mo + screen flash on room clear:
    EventBus.screen_shake_requested.emit(3.0, 0.2)
    Engine.time_scale = 0.15
    await get_tree().create_timer(0.4, true, false, true).timeout
    Engine.time_scale = 1.0

func _spawn_cleared_rewards() -> void:
    # Optionally open a chest, spawn a save point, etc.
    if $Decorations.get_node_or_null("Chest"):
        $Decorations/Chest.open()

func _load_enemy(type: Enum.EnemyType) -> PackedScene:
    match type:
        Enum.EnemyType.GRUNT:    return preload("res://scenes/enemies/grunt.tscn")
        Enum.EnemyType.ARCHER:   return preload("res://scenes/enemies/archer.tscn")
        Enum.EnemyType.MAGE:     return preload("res://scenes/enemies/mage.tscn")
        Enum.EnemyType.EXPLODER: return preload("res://scenes/enemies/exploder.tscn")
        _:                       return preload("res://scenes/enemies/grunt.tscn")
```

---

## Roof Fade (player under overhangs)

```gdscript
# Add to each RoofLayer TileMapLayer, or as a monitor Area2D per overhang:

# scenes/levels/roof_fade.gd
extends Area2D

@export var roof_tiles : TileMapLayer   # drag RoofLayer here

func _ready() -> void:
    body_entered.connect(func(body):
        if body.is_in_group("Player"):
            var tween = create_tween()
            tween.tween_property(roof_tiles, "modulate:a", 0.0, 0.3)
    )
    body_exited.connect(func(body):
        if body.is_in_group("Player"):
            var tween = create_tween()
            tween.tween_property(roof_tiles, "modulate:a", 1.0, 0.3)
    )
```

---

## Level Transitions (Doors)

```gdscript
# scenes/objects/door.gd
extends Area2D

@export var target_level_id  : String = ""    # e.g. "dungeon_01_floor_2"
@export var target_entry     : String = "default"
@export var door_direction   : String = "south"   # north/south/east/west
@export var is_locked        : bool   = false

var _can_transition : bool = true

@onready var sprite     = $Sprite2D
@onready var label      = $Label      # "Press E to enter" prompt
@onready var collision  = $CollisionShape2D

func _ready() -> void:
    body_entered.connect(_on_body_entered)
    body_exited.connect(_on_body_exited)
    if is_locked:
        lock()
    label.visible = false

func _on_body_entered(body: Node2D) -> void:
    if not body.is_in_group("Player"): return
    if is_locked:
        label.text    = "[Locked]"
        label.visible = true
        return
    label.text    = "Press E to enter"
    label.visible = true
    # Connect player interact signal
    if body.has_signal("interacted"):
        body.interacted.connect(_do_transition, CONNECT_ONE_SHOT)

func _on_body_exited(body: Node2D) -> void:
    label.visible = false
    if body.has_signal("interacted"):
        if body.interacted.is_connected(_do_transition):
            body.interacted.disconnect(_do_transition)

func _do_transition() -> void:
    if not _can_transition: return
    _can_transition = false
    if target_level_id != "":
        EventBus.level_transition_requested.emit(target_level_id, target_entry)
    else:
        # Same scene, different entry (e.g. house interior)
        EventBus.level_transition_requested.emit(GameManager.current_level_id, target_entry)

func lock() -> void:
    is_locked       = true
    sprite.frame    = 1   # closed frame
    collision.disabled = false   # impassable

func unlock() -> void:
    is_locked          = false
    sprite.frame       = 0
    collision.disabled = true
    var tween = create_tween()
    tween.tween_property(sprite, "modulate:a", 0.0, 0.4)
    tween.tween_callback(func(): sprite.modulate.a = 1.0; sprite.frame = 0)
```

---

## Multi-Floor Dungeon

### Floor tracking
```gdscript
# In each dungeon floor scene:
# scenes/levels/dungeon_01_f1.gd
extends Node2D   # or your level_base.gd

const FLOOR_NUMBER = 1
const NEXT_FLOOR   = "dungeon_01_floor_2"

func _ready() -> void:
    super._ready()
    $Overlay/HUD/FloorLabel.text = "Floor %d" % FLOOR_NUMBER
    # Stairs (down) door in the cleared final room leads to NEXT_FLOOR

# Door in final room is set to:
# target_level_id = "dungeon_01_floor_2"
# target_entry    = "stairs_up"     ← the Marker2D name in floor 2 where player spawns
```

### Player spawn on entry
```gdscript
# In level_base.gd _ready():
func _ready() -> void:
    super._ready()
    # Find the entry Marker2D that matches the requested entry point
    var entry = get_node_or_null("EntryPoints/" + GameManager.requested_entry_point)
    if entry:
        $Entities/Player.global_position = entry.global_position
    else:
        $Entities/Player.global_position = $EntryPoints/default.global_position
```

---

## 2D Lighting Setup (per dungeon floor)

```
World (Node2D)
  ├── CanvasModulate      Color=(0.15, 0.10, 0.20)  ← near-dark ambient
  ├── Torch_01 (PointLight2D)
  │     texture=light_soft_circle.png
  │     energy=1.2, color=(1.0, 0.8, 0.5)   ← warm torch color
  │     shadow_enabled=true
  ├── Torch_02...
  ├── WallLayer
  │     └── LightOccluder2D (one per wall segment — draw polygon)
  └── Player
        └── PlayerLight (PointLight2D)
              texture=light_soft_small.png
              energy=0.6   ← faint ambient glow around player
```

```gdscript
# Flicker torches (optional atmosphere):
# scenes/objects/torch.gd
extends PointLight2D

func _ready() -> void:
    _flicker()

func _flicker() -> void:
    var tween = create_tween().set_loops()
    tween.tween_property(self, "energy", randf_range(1.0, 1.4), randf_range(0.08, 0.15))
    tween.tween_property(self, "energy", randf_range(0.9, 1.2), randf_range(0.08, 0.15))
```

---

## Camera System

```gdscript
# scenes/characters/player_camera.gd   (or add to Camera2D in player scene)
extends Camera2D

@export var look_ahead_strength : float = 20.0   # camera leads player movement direction
@export var trauma_decay        : float = 4.0    # how fast shake fades

var trauma : float = 0.0   # 0–1 shake intensity

func _ready() -> void:
    EventBus.screen_shake_requested.connect(_add_trauma)
    position_smoothing_enabled = true
    position_smoothing_speed   = 8.0

func _process(delta: float) -> void:
    # Look-ahead: offset camera slightly in movement direction
    var player = get_parent()
    if player.has_method("get_movement_direction"):
        offset = player.get_movement_direction() * look_ahead_strength

    # Trauma-based shake
    if trauma > 0:
        trauma = max(0, trauma - trauma_decay * delta)
        var shake_amount = pow(trauma, 2) * 8.0
        offset += Vector2(randf_range(-shake_amount, shake_amount),
                          randf_range(-shake_amount, shake_amount))

func _add_trauma(magnitude: float, _duration: float) -> void:
    trauma = min(1.0, trauma + magnitude * 0.1)

# Camera limits (set per level in _ready or via exported vars):
func set_limits(rect: Rect2) -> void:
    limit_left   = int(rect.position.x)
    limit_top    = int(rect.position.y)
    limit_right  = int(rect.end.x)
    limit_bottom = int(rect.end.y)
```

---

## Chest + Pickup Items

```gdscript
# scenes/objects/chest.gd
extends StaticBody2D

@export var loot_table : Array[Dictionary] = [
    { "item": "health_herb", "weight": 50, "amount": [1, 2] },
    { "item": "gold_coin",   "weight": 50, "amount": [5, 15] },
]
var opened : bool = false

@onready var anim = $AnimationPlayer
@onready var flag_id = "chest_" + name   # unique save flag

func _ready() -> void:
    # Restore state from save (if chest was already opened)
    if GameManager.get_flag(flag_id):
        anim.play("open_instant")
        opened = true

func interact(_player: Node2D) -> void:
    if opened: return
    opened = true
    anim.play("open")
    GameManager.set_flag(flag_id, true)
    await anim.animation_finished
    _spawn_loot()

func _spawn_loot() -> void:
    var pickup_scene = preload("res://scenes/objects/pickup_item.tscn")
    for entry in loot_table:
        if randf() * 100.0 < entry["weight"]:
            var amount = randi_range(entry["amount"][0], entry["amount"][1])
            var pickup = pickup_scene.instantiate()
            get_parent().add_child(pickup)
            pickup.global_position = global_position + Vector2(randf_range(-16,16), -8)
            pickup.setup(entry["item"], amount)
```

```gdscript
# scenes/objects/pickup_item.gd
extends Area2D

var item_id : String
var amount  : int

@onready var sprite = $Sprite2D

func setup(id: String, qty: int) -> void:
    item_id           = id
    amount            = qty
    sprite.texture    = load(Data.ITEM_DATA[id]["texture"])
    body_entered.connect(_on_player_touch)
    # Bounce animation when spawned:
    var tween = create_tween()
    tween.tween_property(self, "position:y", position.y - 12, 0.2)
    tween.tween_property(self, "position:y", position.y,      0.15)

func _on_player_touch(body: Node2D) -> void:
    if not body.is_in_group("Player"): return
    body.inventory.add(item_id, amount)
    EventBus.item_picked_up.emit(item_id, amount)
    # Pop label:
    var label = Label.new()
    get_parent().add_child(label)
    label.text            = "+%d %s" % [amount, item_id]
    label.global_position = global_position
    var t = label.create_tween()
    t.tween_property(label, "position:y", position.y - 24, 0.6)
    t.parallel().tween_property(label, "modulate:a", 0.0, 0.6)
    t.tween_callback(label.queue_free)
    queue_free()
```

---

## Save Point

```gdscript
# scenes/objects/save_point.gd
extends Area2D

@onready var anim   = $AnimationPlayer
@onready var label  = $Label
var player_inside   : bool = false

func _ready() -> void:
    body_entered.connect(func(b):
        if b.is_in_group("Player"):
            player_inside = true
            label.text    = "Press E to save"
            label.visible = true
            anim.play("active")
    )
    body_exited.connect(func(b):
        if b.is_in_group("Player"):
            player_inside = false
            label.visible = false
            anim.play("idle")
    )

func _input(event: InputEvent) -> void:
    if player_inside and event.is_action_pressed("interact"):
        GameManager.save_game()
        _show_saved_message()

func _show_saved_message() -> void:
    label.text = "Game Saved!"
    anim.play("save_flash")
    await get_tree().create_timer(1.5).timeout
    label.visible = false
```
