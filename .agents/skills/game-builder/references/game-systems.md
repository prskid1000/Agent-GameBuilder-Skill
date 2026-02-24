# Game Systems — Reusable Across Any Genre

Every system references .docs/ for API verification. These patterns work in any 2D or 3D game.

---

## Combat System

### Melee Combat (2D)

**Hitbox pattern:** Area2D on player, `monitoring=false` by default. Enable via AnimationPlayer method track at swing frame, disable after.
- `.docs/godot-docs-md/classes/class_area2d.md` — monitoring, body_entered signal
- `.docs/godot-docs-md/classes/class_animationplayer.md` — method tracks

```gdscript
# AnimationPlayer method track calls at hit frame:
func _enable_hitbox(): $MeleeHitbox.monitoring = true
func _disable_hitbox(): $MeleeHitbox.monitoring = false

func _on_melee_hitbox_body_entered(body):
    if body.has_method("take_damage"):
        var dmg = stats.calculate_damage(weapon_data)
        body.take_damage(dmg, global_position)
```

**Combo system:** Track combo_count (0->1->2), reset after combo_window (Timer). Each hit plays next animation in sequence.

### Melee Combat (3D)

Same pattern with Area3D — `.docs/godot-docs-md/classes/class_area3d.md`
- Hitbox as child of weapon bone or player model
- Enable during attack animation frames

### Ranged Combat / Projectiles

**Projectile scene:** Area2D (2D) or Area3D (3D) with CollisionShape + Sprite/Mesh.

```gdscript
# .docs/godot-docs-md/classes/class_area2d.md or class_area3d.md
var direction: Vector2  # or Vector3
var speed: float = 300.0
var damage: int = 10
var pierce: bool = false
var lifetime: float = 3.0

func _ready():
    $LifetimeTimer.start(lifetime)  # .docs/godot-docs-md/classes/class_timer.md

func _physics_process(delta):
    position += direction * speed * delta
    # Optional: gravity for arrows
    # direction.y += gravity * delta

func _on_body_entered(body):
    if body.has_method("take_damage"):
        body.take_damage(damage)
    if not pierce:
        queue_free()
```

**Hitscan (3D):** Use RayCast3D instead of projectile — `.docs/godot-docs-md/classes/class_raycast3d.md`

### Damage System

```gdscript
# Standardized damage interface — any damageable node implements:
func take_damage(amount: int, source_position: Vector2 = Vector2.ZERO):
    health -= amount
    # Knockback
    var kb_dir = (global_position - source_position).normalized()
    velocity = kb_dir * KNOCKBACK_FORCE
    # Visual feedback
    $FlashSprite.flash()
    # EventBus notification
    EventBus.damage_dealt.emit(amount, global_position, false)
    if health <= 0:
        die()
```

### Screen Shake + Hit-Stop

```gdscript
# Screen shake via Camera offset — .docs/godot-docs-md/classes/class_camera2d.md
func add_trauma(amount): trauma = min(trauma + amount, 1.0)
func _process(delta):
    trauma = max(trauma - 4.0 * delta, 0.0)
    var s = trauma * trauma
    camera.offset = Vector2(randf_range(-1,1), randf_range(-1,1)) * MAX_SHAKE * s

# Hit-stop
func hit_stop(duration: float = 0.06):
    Engine.time_scale = 0.05
    # .docs/godot-docs-md/classes/class_scenetree.md — create_timer
    await get_tree().create_timer(duration, true, false, true).timeout
    Engine.time_scale = 1.0
```

---

## Enemy AI

### Finite State Machine (Recommended for Most Games)

```gdscript
enum State { IDLE, PATROL, CHASE, ATTACK, HURT, DEAD, INVESTIGATE, FLEE }
var state: State = State.IDLE

func _physics_process(delta):
    match state:
        State.IDLE:
            _idle_timer -= delta
            if _idle_timer <= 0: state = State.PATROL
            if _player_in_range(detect_range): state = State.CHASE
        State.PATROL:
            _move_to_patrol_point(delta)
            if _player_in_range(detect_range): state = State.CHASE
        State.CHASE:
            # .docs/godot-docs-md/classes/class_navigationagent2d.md
            nav_agent.target_position = player.global_position
            var next = nav_agent.get_next_path_position()
            velocity = (next - global_position).normalized() * speed
            move_and_slide()
            if _player_in_range(attack_range): state = State.ATTACK
            if not _player_in_range(detect_range * 1.5): state = State.PATROL
        State.ATTACK:
            _do_attack()
        State.HURT:
            _knockback_timer -= delta
            if _knockback_timer <= 0: state = State.CHASE
        State.DEAD:
            _spawn_loot(); queue_free()
```

### Behavior Trees (For Complex AI)

Use **LimboAI** plugin (C++ with GDScript support) for behavior trees + state machines combined. Or implement manually:

```gdscript
# Selector: try children in order, return first success
# Sequence: run children in order, fail on first failure
# Leaf: actual action (move_to, attack, wait)
```

### Enemy Types Pattern

**Base class** with shared logic (health, damage, knockback, state machine, navigation).
**Variants override** specific behaviors:

| Type | Behavior | Key Mechanic |
|------|----------|-------------|
| Melee (Grunt) | Chase + attack in range | Simple slam |
| Ranged (Archer) | Maintain distance, fire projectiles | preferred_distance |
| Caster (Mage) | AOE spells, teleport when low HP | aoe_radius, teleport |
| Tank (Shield) | Block frontal damage | dot product check for facing |
| Exploder | Suicide rush, fuse, area damage | fuse_time, explosion_radius |
| Boss | Multi-phase, attack patterns | phase transitions at HP thresholds |

### Stealth AI

**Detection systems:**
1. **Vision cone:** angle check + distance + raycast line-of-sight
2. **Noise radius:** player actions emit noise signals, nearby enemies react
3. **Light level:** track how lit the player is

**States:** PATROL -> SUSPICIOUS (heard noise) -> INVESTIGATE (go to noise) -> ALERT (saw player) -> CHASE -> SEARCH (lost player) -> PATROL

---

## Inventory System

### Resource-Based Items

```gdscript
# .docs/godot-docs-md/classes/class_resource.md
class_name ItemData extends Resource
@export var id: String
@export var name: String
@export var icon: Texture2D
@export var type: int  # ItemType enum
@export var stackable: bool = true
@export var max_stack: int = 99
@export var value: int = 0
@export var description: String
```

### Inventory Manager

```gdscript
class_name Inventory extends RefCounted

var slots: Array[Dictionary] = []  # [{item: ItemData, count: int}]
var max_slots: int = 30

func add_item(item: ItemData, count: int = 1) -> bool:
    # Try stacking first
    if item.stackable:
        for slot in slots:
            if slot.item == item and slot.count < item.max_stack:
                slot.count = min(slot.count + count, item.max_stack)
                return true
    # Try empty slot
    if slots.size() < max_slots:
        slots.append({item = item, count = count})
        return true
    return false  # full

func remove_item(item: ItemData, count: int = 1) -> bool:
    for i in slots.size():
        if slots[i].item == item:
            slots[i].count -= count
            if slots[i].count <= 0:
                slots.remove_at(i)
            return true
    return false

func serialize() -> Array:
    var data = []
    for slot in slots:
        data.append({id = slot.item.id, count = slot.count})
    return data
```

### Grid UI

- GridContainer with TextureRect slots — `.docs/godot-docs-md/classes/class_gridcontainer.md`
- Drag-drop: `_gui_input()` with `InputEventMouseButton` — `.docs/godot-docs-md/classes/class_control.md`
- Tooltip on hover showing item description

---

## Dialogue System

### Architecture

```gdscript
# dialogue_box.gd — CanvasLayer
# .docs/godot-docs-md/classes/class_canvaslayer.md
var dialogue_data: Array  # [{speaker, text, choices: [{text, next}]}]
var current_line: int = 0

func start(data: Array):
    dialogue_data = data
    current_line = 0
    visible = true
    get_tree().paused = true  # .docs/godot-docs-md/classes/class_scenetree.md
    _show_line()

func _show_line():
    var line = dialogue_data[current_line]
    $SpeakerLabel.text = line.speaker
    # Typewriter effect — .docs/godot-docs-md/classes/class_richtextlabel.md
    $TextLabel.text = line.text
    $TextLabel.visible_characters = 0
    var tween = create_tween()
    tween.tween_property($TextLabel, "visible_characters", line.text.length(), line.text.length() * 0.03)

func _advance():
    if $TextLabel.visible_characters < dialogue_data[current_line].text.length():
        $TextLabel.visible_characters = dialogue_data[current_line].text.length()  # skip
    else:
        current_line += 1
        if current_line >= dialogue_data.size():
            _end()
        else:
            _show_line()

func _end():
    visible = false
    get_tree().paused = false
```

### Branching Choices

Add choice buttons dynamically. Each choice has a `next` index pointing to the next dialogue line. Use `match` or dict lookup for quest flag checks.

---

## Quest System

### Simple Flag-Based

```gdscript
# In GameManager autoload:
var flags: Dictionary = {}  # {"quest_started": true, "boss_defeated": false}

func set_flag(key: String, value = true): flags[key] = value
func get_flag(key: String, default = false): return flags.get(key, default)
```

### Objective Tracking

```gdscript
class_name Quest extends Resource
@export var id: String
@export var title: String
@export var description: String
@export var objectives: Array[Dictionary]  # [{type, target, count, current}]
var state: int = 0  # INACTIVE, ACTIVE, COMPLETE, FAILED

func check_complete() -> bool:
    for obj in objectives:
        if obj.current < obj.count: return false
    state = 2  # COMPLETE
    return true
```

---

## Save/Load System

### Method Comparison

| Method | Best For | Pros | Cons | .docs |
|--------|----------|------|------|-------|
| Custom Resources | Complex nested data | Type-safe, auto-serialize | Security risk from untrusted files | `.docs/godot-docs-md/classes/class_resource.md` |
| FileAccess.store_var() | Simple data | Binary, fast, safe | No human-readable output | `.docs/godot-docs-md/classes/class_fileaccess.md` |
| JSON | Web-compatible data | Human-readable, portable | No Vector2/Color support, floats only | `.docs/godot-docs-md/classes/class_json.md` |
| ConfigFile | Settings/preferences | INI-style, easy | Limited nesting | `.docs/godot-docs-md/classes/class_configfile.md` |
| SQLite (addon) | Large world data, voxels | Queries, thread-safe | Requires addon | `.docs/godot-docs-md/classes/class_mutex.md` |

### Resource-Based Save (Recommended)

```gdscript
# .docs/godot-docs-md/classes/class_resource.md
class_name SaveData extends Resource
@export var player_position: Vector3
@export var player_health: int
@export var inventory: Array
@export var flags: Dictionary
@export var playtime: float

# Save:
func save_game(slot: int):
    var data = SaveData.new()
    data.player_position = player.global_position
    data.player_health = player.health
    data.inventory = inventory.serialize()
    data.flags = GameManager.flags.duplicate()
    ResourceSaver.save(data, "user://save_%d.tres" % slot)

# Load:
func load_game(slot: int):
    var path = "user://save_%d.tres" % slot
    if ResourceLoader.exists(path):
        var data = ResourceLoader.load(path) as SaveData
        # Restore...
```

### JSON Save (Simpler)

```gdscript
# .docs/godot-docs-md/classes/class_fileaccess.md
# .docs/godot-docs-md/classes/class_json.md
func save_json(slot: int):
    var data = {version = 1, hp = player.health, pos = var_to_str(player.position)}
    var file = FileAccess.open("user://save_%d.json" % slot, FileAccess.WRITE)
    file.store_string(JSON.stringify(data))

func load_json(slot: int):
    var file = FileAccess.open("user://save_%d.json" % slot, FileAccess.READ)
    var data = JSON.parse_string(file.get_as_text())
    player.health = data.hp
    player.position = str_to_var(data.pos)
```

---

## Audio System

### Architecture

```gdscript
# audio_manager.gd (Autoload)
# .docs/godot-docs-md/classes/class_audiostreamplayer.md

var _sfx_pool: Array[AudioStreamPlayer] = []
var _music_a: AudioStreamPlayer
var _music_b: AudioStreamPlayer
var _current_music: AudioStreamPlayer

func _ready():
    for i in 12:  # SFX pool
        var p = AudioStreamPlayer.new()
        p.bus = "SFX"
        add_child(p)
        _sfx_pool.append(p)
    _music_a = AudioStreamPlayer.new(); _music_a.bus = "Music"; add_child(_music_a)
    _music_b = AudioStreamPlayer.new(); _music_b.bus = "Music"; add_child(_music_b)

func play_sfx(stream: AudioStream, pitch_variation: float = 0.1):
    for p in _sfx_pool:
        if not p.playing:
            p.stream = stream
            p.pitch_scale = randf_range(1.0 - pitch_variation, 1.0 + pitch_variation)
            p.play()
            return

func crossfade_music(stream: AudioStream, duration: float = 1.5):
    var next = _music_b if _current_music == _music_a else _music_a
    next.stream = stream
    next.volume_db = -80
    next.play()
    var tween = create_tween()
    tween.tween_property(_current_music, "volume_db", -80, duration)
    tween.parallel().tween_property(next, "volume_db", 0, duration)
    tween.tween_callback(func(): _current_music.stop())
    _current_music = next
```

### Spatial Audio

- 2D: `AudioStreamPlayer2D` — `.docs/godot-docs-md/classes/class_audiostreamplayer2d.md`
- 3D: `AudioStreamPlayer3D` — `.docs/godot-docs-md/classes/class_audiostreamplayer3d.md`
- Audio buses: Project > Audio tab, create "SFX" and "Music" buses

### Surface-Based Footsteps

Map tile/surface type to footstep SFX variant. Play on walk animation method track.

---

## UI / HUD

### Health Bar

```gdscript
# .docs/godot-docs-md/classes/class_textureprogressbar.md
# or .docs/godot-docs-md/classes/class_progressbar.md
func _on_health_changed(hp: int, max_hp: int):
    var tween = create_tween()
    tween.tween_property($HPBar, "value", float(hp) / max_hp * 100, 0.3)
```

### Pause Menu

```gdscript
# .docs/godot-docs-md/classes/class_canvaslayer.md
# process_mode = PROCESS_MODE_ALWAYS (runs when paused)
func toggle_pause():
    visible = !visible
    get_tree().paused = visible
```

### Theme

Create a Theme resource with custom fonts, colors, and StyleBox overrides. Apply to root Control node — all children inherit.
- `.docs/godot-docs-md/classes/class_theme.md`

---

## Day/Night Cycle

### 2D (CanvasModulate + Gradient)

```gdscript
# .docs/godot-docs-md/classes/class_canvasmodulate.md
@export var gradient: Gradient  # dawn -> day -> dusk -> night
func _process(_d):
    var t = 1.0 - ($DayTimer.time_left / $DayTimer.wait_time)
    $CanvasModulate.color = gradient.sample(t)
```

### 3D (ProceduralSky + DirectionalLight)

```gdscript
# .docs/godot-docs-md/classes/class_directionallight3d.md
# .docs/godot-docs-md/classes/class_proceduralskymaterial.md
func _process(delta):
    time = fmod(time + speed * delta, 1.0)
    _sun.rotation_degrees.x = -time * 360
    _sun.light_energy = clamp(sin(time * TAU), 0, 1)
    # Lerp sky colors between phases (sunrise/day/sunset/night)
```

---

## Multiplayer Networking

### Architecture Overview

`.docs/godot-docs-md/tutorials/networking/high_level_multiplayer.md`

Three protocols:
| Protocol | Use Case | .docs |
|----------|----------|-------|
| ENet | Fast UDP, most games | `.docs/godot-docs-md/classes/class_enetmultiplayerpeer.md` |
| WebSocket | Browser games | `.docs/godot-docs-md/classes/class_websocketmultiplayerpeer.md` |
| WebRTC | P2P without server | `.docs/godot-docs-md/classes/class_webrtcmultiplayerpeer.md` |

### Basic Server/Client

```gdscript
# .docs/godot-docs-md/classes/class_enetmultiplayerpeer.md
func host_game():
    var peer = ENetMultiplayerPeer.new()
    peer.create_server(PORT, MAX_CLIENTS)
    multiplayer.multiplayer_peer = peer

func join_game(address: String):
    var peer = ENetMultiplayerPeer.new()
    peer.create_client(address, PORT)
    multiplayer.multiplayer_peer = peer
```

### RPC Pattern

```gdscript
# .docs/godot-docs-md/tutorials/networking/high_level_multiplayer.md
@rpc("any_peer", "call_local", "reliable")
func take_damage(amount: int):
    health -= amount

# Call: take_damage.rpc(10)  # runs on all peers
# Or: take_damage.rpc_id(target_id, 10)  # specific peer
```

### Synchronization

```gdscript
# MultiplayerSynchronizer node auto-syncs properties
# .docs/godot-docs-md/classes/class_multiplayersynchronizer.md
# Add to player scene, configure which properties to sync (position, rotation, etc.)
```

### Mesh Networking

ENet supports mesh mode (all peers connected, no central server):
```gdscript
var peer = ENetMultiplayerPeer.new()
peer.create_mesh(unique_id)
peer.add_mesh_peer(other_peer_id, host, port)
```

---

## Procedural Generation

### Noise-Based Terrain

```gdscript
# .docs/godot-docs-md/classes/class_fastnoiselite.md
var noise = FastNoiseLite.new()
noise.noise_type = FastNoiseLite.TYPE_PERLIN
noise.seed = randi()
noise.frequency = 0.02

func get_height(x: float, z: float) -> float:
    return BASE_HEIGHT + noise.get_noise_2d(x, z) * AMPLITUDE
```

### Room-Based Dungeons

1. Generate room positions on grid (random or BSP)
2. Connect rooms with corridors (A* or minimum spanning tree)
3. Instantiate pre-built room scenes at positions
4. Place doors at connection points

### Wave Function Collapse (Advanced)

For tile-based levels with complex adjacency rules. Implement as:
1. Define tile types with allowed neighbors per edge
2. Start with all cells uncollapsed (all types possible)
3. Collapse cell with fewest options, propagate constraints
4. Repeat until all collapsed
