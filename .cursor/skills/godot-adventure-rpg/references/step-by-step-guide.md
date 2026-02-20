# Step-by-Step Build Guide — 2D Adventure / RPG
# All 16 phases with exact code, matched to the architecture in SKILL.md

**Rule: After each phase, run the game (F5) and fix any errors before continuing. The project must never be left broken at the end of a step.**

---

## Phase 1 — Project Setup

```
Project Settings → Display → Window: 1920×1080
Project Settings → Rendering → Textures → Default Texture Filter → Nearest
Project Settings → 2D Physics → Layer Names: (set all 8 from SKILL.md table)
Project Settings → Input Map: (add all actions from SKILL.md table)
Project Settings → Globals (Autoloads):
    global/enums.gd         → Enum
    global/data.gd          → Data
    global/event_bus.gd     → EventBus
    global/game_manager.gd  → GameManager
    global/audio_manager.gd → AudioManager
```

**Folder structure to create in FileSystem:**
```
res://
├── audio/          music_outdoor.ogg, music_dungeon.ogg, music_boss.ogg, sfx/...
├── global/         enums.gd, data.gd, event_bus.gd, game_manager.gd, audio_manager.gd
├── graphics/       characters/, enemies/, tilesets/, icons/, vfx/, projectiles/, ui/
├── resources/      player_stats.gd + .tres, item_res.gd, weapon_res.gd
├── scenes/
│   ├── characters/ player.tscn
│   ├── enemies/    enemy_base.tscn, grunt.tscn, archer.tscn, mage.tscn, boss.tscn
│   ├── levels/     level_01.tscn, dungeon_01_f1.tscn, boss_01.tscn
│   ├── objects/    chest.tscn, door.tscn, pickup_item.tscn, save_point.tscn
│   ├── projectiles/ projectile.tscn
│   ├── ui/         hud.tscn, inventory.tscn, dialogue.tscn, pause_menu.tscn
│   └── vfx/        hit_spark.tscn, damage_number.tscn, explosion.tscn, flash_sprite_2d.tscn
└── shaders/        flash.tres, circle_transition.gdshader, vignette.gdshader
```

**Verify:** Set a minimal main scene (e.g. empty Node2D) and run (F5). Project opens and runs with no errors.

---

## Phase 2 — Global Scripts

See `references/enums-data.md` for the full code for:
- `enums.gd` — all enums
- `data.gd` — all data tables
- `event_bus.gd` — all shared signals
- `resources/player_stats.gd` — PlayerStats resource class

### game_manager.gd
```gdscript
# global/game_manager.gd
extends Node

const SAVE_PATH = "user://save_%d.json"
var current_level_id : String = "level_01_outdoor"
var player_ref       : Node   = null     # set by player._ready()

# ─── Scene transitions ────────────────────────────────────────────────────────
func change_level(level_id: String, entry_point: String = "default") -> void:
    current_level_id = level_id
    var data = Data.LEVEL_DATA[level_id]
    AudioManager.crossfade_music(data["music"])
    # Circle wipe transition → load → reveal
    var tween = create_tween()
    tween.tween_property($TransitionOverlay.material, "shader_parameter/progress", 1.0, 0.8)
    tween.tween_callback(func():
        get_tree().change_scene_to_file(data["scene"])
    )
    tween.tween_property($TransitionOverlay.material, "shader_parameter/progress", 0.0, 0.8)

# ─── Save / Load ──────────────────────────────────────────────────────────────
func save_game(slot: int = 1) -> void:
    if player_ref == null: return
    var save_data = {
        "level":      current_level_id,
        "stats":      _stats_to_dict(player_ref.stats),
        "inventory":  player_ref.inventory.serialize(),
        "flags":      _collect_flags(),
    }
    var file = FileAccess.open(SAVE_PATH % slot, FileAccess.WRITE)
    file.store_string(JSON.stringify(save_data))

func load_game(slot: int = 1) -> void:
    if not FileAccess.file_exists(SAVE_PATH % slot): return
    var file = FileAccess.open(SAVE_PATH % slot, FileAccess.READ)
    var data = JSON.parse_string(file.get_as_text())
    _apply_stats(data["stats"])
    player_ref.inventory.deserialize(data["inventory"])
    _apply_flags(data["flags"])
    change_level(data["level"])

func save_exists(slot: int) -> bool:
    return FileAccess.file_exists(SAVE_PATH % slot)

func _stats_to_dict(stats: PlayerStats) -> Dictionary:
    return {
        "hp": stats.hp, "mp": stats.mp, "max_hp": stats.max_hp,
        "max_mp": stats.max_mp, "level": stats.level, "xp": stats.xp,
        "base_atk": stats.base_atk, "base_def": stats.base_def,
    }

func _collect_flags() -> Dictionary:
    # Collect all flags from rooms, doors, chests — group-based approach
    var flags = {}
    for node in get_tree().get_nodes_in_group("Flagged"):
        flags[node.flag_id] = node.flag_value
    return flags

func _apply_flags(flags: Dictionary) -> void:
    for flag_id in flags:
        get_tree().call_group("Flagged_" + flag_id, "apply_flag", flags[flag_id])

func _apply_stats(dict: Dictionary) -> void:
    if player_ref == null: return
    for key in dict:
        player_ref.stats.set(key, dict[key])
```

**Verify:** Run project. No script parse errors; all autoloads load. Fix any missing references (e.g. Data.LEVEL_DATA) with stubs if needed so the game runs.

---

## Phase 3 — Player Scene + Movement

### Scene nodes
```
Player (CharacterBody2D)   layer=2, mask=1|3|7|8
  ├── CollisionShape2D      CapsuleShape2D radius=6 height=10
  ├── FlashSprite2D         hframes=<weapon_row_count> vframes=<direction_count>
  ├── AnimationPlayer       (all animations)
  ├── AnimationTree         tree_root=BlendTree, anim_player=AnimationPlayer, active=true
  ├── Camera2D              zoom=(3,3), position_smoothing=true, smoothing_speed=8.0
  ├── MeleeHitbox (Area2D)  layer=4, mask=3   [disabled by default]
  │    └── CollisionShape2D  RectangleShape2D
  ├── ProjectileSpawnPoint (Marker2D)
  ├── RayCast2D             collision_mask=7   (detect interactables)
  ├── HurtArea (Area2D)     layer=0, mask=5    (detects enemy hitboxes)
  │    └── CollisionShape2D  CapsuleShape2D
  └── StaminaRegen Timer    wait_time=0.1, autostart=true
```

### player.gd
```gdscript
# scenes/characters/player.gd
extends CharacterBody2D

# ─── References ───────────────────────────────────────────────────────────────
@onready var flash_sprite     = $FlashSprite2D
@onready var anim_tree        = $AnimationTree
@onready var camera           = $Camera2D
@onready var melee_hitbox     = $MeleeHitbox
@onready var projectile_spawn = $ProjectileSpawnPoint
@onready var hurt_area        = $HurtArea
@onready var ray_cast         = $RayCast2D
@onready var move_sm          = anim_tree.get("parameters/MoveStateMachine/playback")
@onready var attack_sm        = anim_tree.get("parameters/AttackStateMachine/playback")

# ─── State ────────────────────────────────────────────────────────────────────
var stats          : PlayerStats = PlayerStats.new()
var inventory      : InventorySystem
var direction      : Vector2 = Vector2.DOWN
var last_direction : Vector2 = Vector2.DOWN
var state          : Enum.PlayerState = Enum.PlayerState.IDLE
var combo_count    : int   = 0
var is_dodging     : bool  = false
var iframe_active  : bool  = false   # true during dodge → ignores damage
var locked_target  : Node  = null    # for aim-lock

const PROJECTILE_SCENE = preload("res://scenes/projectiles/projectile.tscn")

# ─── _ready ───────────────────────────────────────────────────────────────────
func _ready() -> void:
    GameManager.player_ref = self
    stats.hp      = stats.max_hp
    stats.mp      = stats.max_mp
    stats.stamina = stats.max_stamina
    inventory     = InventorySystem.new()
    anim_tree.active = true
    anim_tree.animation_started.connect(_on_anim_started)
    anim_tree.animation_finished.connect(_on_anim_finished)
    hurt_area.area_entered.connect(_on_hurt_area_entered)
    melee_hitbox.body_entered.connect(_on_melee_hit)
    melee_hitbox.monitoring = false   # only active during attack frames

# ─── _physics_process ────────────────────────────────────────────────────────
func _physics_process(delta: float) -> void:
    _handle_stamina_regen(delta)

    match state:
        Enum.PlayerState.IDLE, Enum.PlayerState.MOVE:
            _move()
            _handle_combat_input()
        Enum.PlayerState.DODGE:
            _do_dodge()
        Enum.PlayerState.HURT:
            pass   # knockback velocity applied by take_damage(), fade out naturally

# ─── Movement ─────────────────────────────────────────────────────────────────
func _move() -> void:
    var raw = Input.get_vector("move_left", "move_right", "move_up", "move_down")
    var sprinting = Input.is_action_pressed("sprint") and stats.stamina > 0
    var speed_mult = Data.PLAYER_BASE_STATS["sprint_mult"] if sprinting else 1.0

    if raw != Vector2.ZERO:
        direction = raw
        last_direction = Vector2(round(raw.x), round(raw.y))  # snap for blend space
        state = Enum.PlayerState.MOVE
        if sprinting: stats.stamina -= 25.0 * get_physics_process_delta_time()
    else:
        state = Enum.PlayerState.IDLE

    velocity = direction * stats.total_spd() * speed_mult if raw != Vector2.ZERO else Vector2.ZERO
    move_and_slide()
    _animate()

func _animate() -> void:
    var dir = last_direction
    anim_tree.set("parameters/MoveStateMachine/Idle/blend_position", dir)
    anim_tree.set("parameters/MoveStateMachine/Walk/blend_position", dir)
    # Update all attack blend positions via TOOL_STATE_ANIMATIONS equivalent:
    for anim_name in ["Sword", "Bow", "Staff", "Punch"]:
        anim_tree.set("parameters/AttackStateMachine/%s/blend_position" % anim_name, dir)
    if state == Enum.PlayerState.MOVE:
        move_sm.travel("Walk")
    else:
        move_sm.travel("Idle")

# ─── Combat Input ─────────────────────────────────────────────────────────────
func _handle_combat_input() -> void:
    # Dodge
    if Input.is_action_just_pressed("dodge") and stats.stamina >= 20:
        _start_dodge()
        return

    # Light attack (left click / J)
    if Input.is_action_just_pressed("attack"):
        _do_melee_attack()

    # Ranged attack (right click / K)
    if Input.is_action_just_pressed("shoot"):
        _do_ranged_attack()

    # Abilities
    if Input.is_action_just_pressed("ability_1"):
        _use_ability(Enum.AbilitySlot.ABILITY_1)
    if Input.is_action_just_pressed("ability_2"):
        _use_ability(Enum.AbilitySlot.ABILITY_2)

    # Interact
    if Input.is_action_just_pressed("interact"):
        _interact()

# ─── Melee Attack ─────────────────────────────────────────────────────────────
func _do_melee_attack() -> void:
    combo_count = (combo_count + 1) % 3   # 0→1→2→0 (3-hit combo)
    var anim = "attack_%d" % combo_count   # attack_0, attack_1, attack_2
    attack_sm.travel("Sword")
    anim_tree.set("parameters/AttackOneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)
    # The AnimationPlayer method track enables melee_hitbox during the hit frame.

# Called by AnimationPlayer method track at the hit frame:
func enable_hitbox() -> void:  melee_hitbox.monitoring = true
func disable_hitbox() -> void: melee_hitbox.monitoring = false

func _on_melee_hit(body: Node2D) -> void:
    if not body.is_in_group("Enemies"): return
    var dmg = stats.calculate_damage(Data.WEAPON_DATA["iron_sword"])  # use equipped weapon
    body.take_damage(dmg, Enum.DamageType.PHYSICAL, last_direction * 60.0)
    EventBus.damage_dealt.emit(dmg, body.global_position, false)
    EventBus.screen_shake_requested.emit(2.0, 0.12)

# ─── Ranged Attack ────────────────────────────────────────────────────────────
func _do_ranged_attack() -> void:
    if stats.mp < 5: return   # mp cost (adjust per weapon)
    stats.mp -= 5
    EventBus.player_mp_changed.emit(stats.mp, stats.max_mp)

    var proj = PROJECTILE_SCENE.instantiate()
    get_parent().get_node("Projectiles").add_child(proj)
    proj.global_position = projectile_spawn.global_position

    # Aim toward mouse OR locked target OR last direction
    var aim : Vector2
    if locked_target:
        aim = (locked_target.global_position - global_position).normalized()
    else:
        aim = (get_global_mouse_position() - global_position).normalized()

    proj.setup(Enum.ProjectileType.ARROW, aim, true)   # true = player-owned

# ─── Dodge ────────────────────────────────────────────────────────────────────
func _start_dodge() -> void:
    state = Enum.PlayerState.DODGE
    iframe_active = true
    stats.stamina -= 20.0
    EventBus.player_stamina_changed.emit(stats.stamina, stats.max_stamina)
    anim_tree.set("parameters/DodgeOneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)
    velocity = last_direction * Data.PLAYER_BASE_STATS["dodge_speed"]
    var tween = create_tween()
    tween.tween_interval(Data.PLAYER_BASE_STATS["dodge_duration"])
    tween.tween_callback(func():
        state = Enum.PlayerState.IDLE
        iframe_active = false
    )

func _do_dodge() -> void:
    velocity = velocity.lerp(Vector2.ZERO, 0.2)
    move_and_slide()

# ─── Take Damage ──────────────────────────────────────────────────────────────
func take_damage(amount: int, type: Enum.DamageType, knockback: Vector2 = Vector2.ZERO) -> void:
    if iframe_active: return   # dodge iframe protection
    var actual = stats.take_damage(amount, type)
    EventBus.player_hp_changed.emit(stats.hp, stats.max_hp)
    EventBus.damage_dealt.emit(actual, global_position, false)
    flash_sprite.flash(0.15, 0.3)
    # Apply knockback
    if knockback != Vector2.ZERO:
        velocity = knockback
        state = Enum.PlayerState.HURT
        var tween = create_tween()
        tween.tween_interval(0.25)
        tween.tween_callback(func(): state = Enum.PlayerState.IDLE)

# ─── Abilities ────────────────────────────────────────────────────────────────
func _use_ability(slot: Enum.AbilitySlot) -> void:
    var ability_id = "dash_strike"   # fetched from equipped ability — placeholder
    var ability    = Data.ABILITY_DATA[ability_id]
    if stats.mp < ability["mp_cost"]: return
    stats.mp -= ability["mp_cost"]
    EventBus.player_mp_changed.emit(stats.mp, stats.max_mp)
    anim_tree.set("parameters/AbilityOneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)

# ─── Interact ─────────────────────────────────────────────────────────────────
func _interact() -> void:
    if ray_cast.is_colliding():
        var target = ray_cast.get_collider()
        if target.has_method("interact"):
            target.interact(self)

# ─── Stamina Regen ────────────────────────────────────────────────────────────
func _handle_stamina_regen(delta: float) -> void:
    if state != Enum.PlayerState.DODGE and not Input.is_action_pressed("sprint"):
        stats.stamina = min(stats.max_stamina, stats.stamina + Data.PLAYER_BASE_STATS["stamina_regen"] * delta)
        EventBus.player_stamina_changed.emit(stats.stamina, stats.max_stamina)

# ─── Animation signals ────────────────────────────────────────────────────────
func _on_anim_started(_name: StringName) -> void:
    pass

func _on_anim_finished(_name: StringName) -> void:
    if state == Enum.PlayerState.HURT:
        state = Enum.PlayerState.IDLE

# ─── Hurt Area (enemy hitboxes touching player) ───────────────────────────────
func _on_hurt_area_entered(area: Area2D) -> void:
    if area.is_in_group("EnemyHitbox"):
        var dmg      = area.get_parent().get_attack_damage()
        var knockdir = (global_position - area.global_position).normalized() * 80.0
        take_damage(dmg, Enum.DamageType.PHYSICAL, knockdir)
```

**Verify:** Main scene contains Player instance. Run game: player moves with WASD, direction and animations update, dodge/sprint work. Resolve any missing AnimationTree parameters or node paths before Phase 4.

---

## Phase 4 — Projectile System

```gdscript
# scenes/projectiles/projectile.gd
extends Area2D

var speed       : float
var gravity     : float = 0.0
var pierce      : bool  = false
var bounce      : bool  = false
var homing      : bool  = false
var aoe_radius  : float = 0.0
var damage      : int
var damage_type : Enum.DamageType
var is_player   : bool  = true   # false = enemy projectile

var _direction  : Vector2
var _velocity   : Vector2
var _lifetime   : float

@onready var sprite = $Sprite2D

const HIT_EFFECT = preload("res://scenes/vfx/hit_spark.tscn")

func setup(type: Enum.ProjectileType, direction: Vector2, player_owned: bool) -> void:
    is_player   = player_owned
    _direction  = direction.normalized()
    var pdata   = Data.PROJECTILE_DATA[type]
    speed       = pdata["speed"]
    gravity     = pdata["gravity"]
    pierce      = pdata["pierce"]
    bounce      = pdata["bounce"]
    homing      = pdata["homing"]
    aoe_radius  = pdata["aoe_radius"]
    _lifetime   = pdata["lifetime"]
    sprite.texture = load(pdata["texture"])
    rotation    = _direction.angle()
    # Collision: player projectiles hit enemies (layer 3), enemy projectiles hit player (layer 2)
    collision_mask = 3 if is_player else 2
    body_entered.connect(_on_body_entered)
    area_entered.connect(_on_area_entered)
    get_tree().create_timer(_lifetime).timeout.connect(queue_free)

func _physics_process(delta: float) -> void:
    if homing and GameManager.player_ref:
        var target = GameManager.player_ref if not is_player else null
        if target:
            var to_target = (target.global_position - global_position).normalized()
            _direction = _direction.lerp(to_target, 0.05).normalized()

    _velocity = _direction * speed
    _velocity.y += gravity * get_physics_process_delta_time()   # arrow arc
    global_position += _velocity * delta
    rotation = _velocity.angle()

func _on_body_entered(body: Node2D) -> void:
    _hit(body.global_position)
    if not pierce: queue_free()

func _on_area_entered(area: Area2D) -> void:
    if area.is_in_group("Shield"):
        # Shield blocks projectile
        queue_free()
        return
    _hit(area.global_position)
    if not pierce: queue_free()

func _hit(hit_pos: Vector2) -> void:
    # Spawn VFX
    var vfx = HIT_EFFECT.instantiate()
    get_parent().add_child(vfx)
    vfx.global_position = hit_pos

    if aoe_radius > 0.0:
        # AOE splash damage — hit everything in radius
        for body in get_tree().get_nodes_in_group("Enemies" if is_player else "Player"):
            if body.global_position.distance_to(hit_pos) <= aoe_radius:
                body.take_damage(damage, damage_type)
                EventBus.damage_dealt.emit(damage, body.global_position, false)
    # Normal single-target damage is handled by _on_body_entered via the body itself
```

**Verify:** Run game. Fire ranged attack; projectile spawns, moves, and hits or expires. No errors. Ensure projectile scene and HIT_EFFECT path exist.

---

## Phase 5 — Combo Counter + Damage Numbers + Screen Shake

### Screen shake (on Camera2D)
```gdscript
# In camera.gd or player.gd where Camera2D is accessible:
func _ready() -> void:
    EventBus.screen_shake_requested.connect(apply_shake)

func apply_shake(magnitude: float, duration: float) -> void:
    var tween = create_tween()
    tween.set_loops(int(duration / 0.05))
    tween.tween_method(func(v): camera.offset = v,
        Vector2(magnitude, 0), Vector2(-magnitude, 0), 0.05)
    tween.tween_callback(func(): camera.offset = Vector2.ZERO)
```

### Hit-stop
```gdscript
# In game_manager.gd:
func _ready() -> void:
    EventBus.hit_stop_requested.connect(_do_hit_stop)

func _do_hit_stop(duration: float) -> void:
    Engine.time_scale = 0.05
    await get_tree().create_timer(duration, true, false, true).timeout
    Engine.time_scale = 1.0
    # create_timer(duration, process_always=true) so it runs even at 0.05 time scale
```

### Floating damage numbers
```gdscript
# scenes/vfx/damage_number.gd
extends Label

func setup(amount: int, is_crit: bool, position: Vector2) -> void:
    text        = str(amount)
    global_position = position + Vector2(randf_range(-10, 10), 0)
    modulate    = Color.YELLOW if is_crit else Color.WHITE
    if is_crit:
        add_theme_font_size_override("font_size", 20)

    var tween = create_tween()
    tween.tween_property(self, "position:y", position.y - 30, 0.6)
    tween.parallel().tween_property(self, "modulate:a", 0.0, 0.6)
    tween.tween_callback(queue_free)

# In HUD or level:
func _ready() -> void:
    EventBus.damage_dealt.connect(_spawn_damage_number)

func _spawn_damage_number(amount: int, pos: Vector2, is_crit: bool) -> void:
    var label = preload("res://scenes/vfx/damage_number.tscn").instantiate()
    $VFX.add_child(label)
    label.setup(amount, is_crit, pos)
```

### Combo counter
```gdscript
# In HUD:
var combo     : int   = 0
var combo_timer : float = 0.0
const COMBO_RESET_TIME = 2.0

func _process(delta: float) -> void:
    if combo > 0:
        combo_timer -= delta
        if combo_timer <= 0:
            combo = 0
            _update_combo_label()

func _on_enemy_damaged() -> void:
    combo += 1
    combo_timer = COMBO_RESET_TIME
    _update_combo_label()

func _update_combo_label() -> void:
    if combo < 3:
        combo_label.visible = false
        return
    combo_label.visible = true
    combo_label.text    = "%d HIT COMBO!" % combo
    # Pop animation
    combo_label.scale = Vector2(1.4, 1.4)
    var tween = create_tween()
    tween.tween_property(combo_label, "scale", Vector2.ONE, 0.15)
```

**Verify:** Run game. Deal damage: numbers appear and float; combo label shows after 3+ hits; screen shake and hit-stop trigger. No errors.

---

## Phase 6 — AAA Polish Systems

### Hit-stop + Camera-shake wired together on heavy hits
```gdscript
# Trigger both together from any hit:
func _on_heavy_hit(damage: int, target_pos: Vector2) -> void:
    EventBus.hit_stop_requested.emit(0.06)
    EventBus.screen_shake_requested.emit(4.0, 0.2)
    EventBus.damage_dealt.emit(damage, target_pos, false)
```

### Vignette + color correction shader
```glsl
// shaders/vignette.gdshader
shader_type canvas_item;
uniform float strength : hint_range(0.0, 1.0) = 0.4;
uniform vec4  tint : source_color = vec4(1.0);

void fragment() {
    vec2  uv     = UV - 0.5;
    float vign   = 1.0 - dot(uv, uv) * strength * 3.0;
    COLOR         = texture(TEXTURE, UV) * tint;
    COLOR.rgb    *= clamp(vign, 0.0, 1.0);
}
// Attach to a full-screen ColorRect in a CanvasLayer.
// Tint a CanvasModulate above it for level-theme color grading.
```

### Slow-motion on last kill
```gdscript
# When last enemy in room dies:
func _on_room_cleared() -> void:
    Engine.time_scale = 0.15
    await get_tree().create_timer(0.5, true, false, true).timeout
    Engine.time_scale = 1.0
    EventBus.room_cleared.emit(room_id)
    _unlock_doors()
```

---

## Phase 16 Summary — All Polish Checklist

| Feature | Where | Trigger |
|---------|-------|---------|
| Screen shake | Camera2D.apply_shake() | EventBus.screen_shake_requested |
| Hit-stop | GameManager._do_hit_stop() | EventBus.hit_stop_requested |
| Damage numbers | VFX label, tween upward | EventBus.damage_dealt |
| Crit flash | yellow damage number + bigger font | stats.calculate_damage() |
| Combo counter | HUD label | every enemy hit resets timer |
| Slow-mo last kill | Engine.time_scale | room cleared |
| Vignette | CanvasLayer shader | always on |
| Color tint per level | CanvasModulate | level_ready() |
| Boss death cinematic | AnimationPlayer in boss scene | boss HP = 0 |
| Particle VFX | GPUParticles2D one-shot | hit, death, pickup |

**Verify:** Run full playthrough. All polish features trigger as expected; no runtime errors. Fix any missing EventBus connections or scene references.
