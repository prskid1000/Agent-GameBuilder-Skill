# Combat System — Enemies, AI, Pathfinding, Bosses

---

## EnemyBase — Shared Base Class

All enemies extend this. Specific types override `_attack()` and optionally `_on_phase_change()`.

```gdscript
# scenes/enemies/enemy_base.gd
extends CharacterBody2D
class_name EnemyBase

# ─── Nodes ────────────────────────────────────────────────────────────────────
@onready var nav_agent    = $NavigationAgent2D
@onready var flash_sprite = $FlashSprite2D
@onready var anim_player  = $AnimationPlayer
@onready var hitbox       = $Hitbox          # Area2D, layer=5 (EnemyHitbox)
@onready var detect_area  = $DetectArea      # Area2D, mask=2  (detects player layer)
@onready var attack_timer = $AttackTimer

# ─── State ────────────────────────────────────────────────────────────────────
var enemy_type   : Enum.EnemyType
var state        : Enum.EnemyState = Enum.EnemyState.IDLE
var stats        : Dictionary      # filled from Data.ENEMY_DATA in _setup()
var player_ref   : Node2D          = null
var health       : int
var last_direction : Vector2       = Vector2.DOWN
var patrol_points  : Array[Vector2] = []
var patrol_index   : int           = 0

signal died(enemy_type: Enum.EnemyType, position: Vector2)

# ─── Setup ────────────────────────────────────────────────────────────────────
func _setup(type: Enum.EnemyType) -> void:
    enemy_type = type
    stats      = Data.ENEMY_DATA[type]
    health     = stats["max_hp"]
    attack_timer.wait_time = stats["attack_cooldown"]
    attack_timer.timeout.connect(_on_attack_timer)
    detect_area.body_entered.connect(_on_player_detected)
    detect_area.body_exited.connect(_on_player_lost)
    add_to_group("Enemies")
    add_to_group("Objects")

# ─── _physics_process ────────────────────────────────────────────────────────
func _physics_process(_delta: float) -> void:
    match state:
        Enum.EnemyState.PATROL: _do_patrol()
        Enum.EnemyState.CHASE:  _do_chase()
        Enum.EnemyState.ATTACK: pass   # handled by timer
        Enum.EnemyState.HURT:   _apply_knockback_decay()
        Enum.EnemyState.DEAD:   pass

func _do_patrol() -> void:
    if patrol_points.is_empty(): return
    var target = patrol_points[patrol_index]
    nav_agent.target_position = target
    var next   = nav_agent.get_next_path_position()
    var dir    = (next - global_position).normalized()
    velocity   = dir * stats["speed"] * 0.5   # slower while patrolling
    move_and_slide()
    last_direction = dir
    _update_anim_direction(dir)
    anim_player.play("walk")
    if global_position.distance_to(target) < 8.0:
        patrol_index = (patrol_index + 1) % patrol_points.size()

func _do_chase() -> void:
    if player_ref == null: return
    var dist = global_position.distance_to(player_ref.global_position)
    if dist <= stats["attack_range"]:
        state = Enum.EnemyState.ATTACK
        if attack_timer.is_stopped():
            attack_timer.start()
        anim_player.play("idle")
        return
    nav_agent.target_position = player_ref.global_position
    var next = nav_agent.get_next_path_position()
    var dir  = (next - global_position).normalized()
    velocity = dir * stats["speed"]
    move_and_slide()
    last_direction = dir
    _update_anim_direction(dir)
    anim_player.play("walk")

func _apply_knockback_decay() -> void:
    velocity = velocity.lerp(Vector2.ZERO, 0.2)
    move_and_slide()
    if velocity.length() < 5.0:
        state = Enum.EnemyState.CHASE if player_ref else Enum.EnemyState.PATROL

# ─── Detection ────────────────────────────────────────────────────────────────
func _on_player_detected(body: Node2D) -> void:
    if not body.is_in_group("Player"): return
    player_ref = body
    state      = Enum.EnemyState.ALERT
    anim_player.play("alert")   # brief "!" reaction
    await get_tree().create_timer(0.4).timeout
    state = Enum.EnemyState.CHASE

func _on_player_lost(body: Node2D) -> void:
    if body != player_ref: return
    # Wait 2s before returning to patrol (give player chance to re-enter)
    await get_tree().create_timer(2.0).timeout
    if player_ref and global_position.distance_to(player_ref.global_position) > stats["detect_range"] * 1.5:
        player_ref = null
        state      = Enum.EnemyState.PATROL

# ─── Damage ───────────────────────────────────────────────────────────────────
func take_damage(amount: int, type: Enum.DamageType, knockback: Vector2 = Vector2.ZERO) -> void:
    if state == Enum.EnemyState.DEAD: return
    # Apply resistance
    var resist  = stats["resistances"].get(type, 0.0)
    var actual  = max(1, int(amount * (1.0 - resist)) - stats["def"])
    health     -= actual
    EventBus.damage_dealt.emit(actual, global_position, false)
    flash_sprite.flash(0.1, 0.15)
    if knockback != Vector2.ZERO:
        velocity  = knockback
        state     = Enum.EnemyState.HURT
    if health <= 0:
        _die()

func get_attack_damage() -> int:
    return stats["atk"]

# ─── Attack ───────────────────────────────────────────────────────────────────
func _on_attack_timer() -> void:
    if state != Enum.EnemyState.ATTACK: return
    if player_ref == null: return
    var dist = global_position.distance_to(player_ref.global_position)
    if dist > stats["attack_range"] * 1.3:
        state = Enum.EnemyState.CHASE
        attack_timer.stop()
        return
    _attack()

func _attack() -> void:
    # Override in each enemy type.
    pass

# ─── Death ────────────────────────────────────────────────────────────────────
func _die() -> void:
    state = Enum.EnemyState.DEAD
    attack_timer.stop()
    set_physics_process(false)
    $CollisionShape2D.set_deferred("disabled", true)
    hitbox.monitoring = false
    anim_player.play("death")
    await anim_player.animation_finished
    _spawn_drops()
    EventBus.enemy_died.emit(enemy_type, global_position, stats["xp"])
    died.emit(enemy_type, global_position)
    queue_free()

func _spawn_drops() -> void:
    var table = stats["loot_table"]
    for entry in table:
        if randf() * 100.0 < entry["weight"]:
            var amount = randi_range(entry["amount"][0], entry["amount"][1])
            if amount <= 0: continue
            var pickup = preload("res://scenes/objects/pickup_item.tscn").instantiate()
            get_parent().add_child(pickup)
            pickup.global_position = global_position + Vector2(randf_range(-12, 12), randf_range(-12, 12))
            pickup.setup(entry["item"], amount)

# ─── Utilities ────────────────────────────────────────────────────────────────
func _update_anim_direction(dir: Vector2) -> void:
    # Update blend positions for the walk/idle blend spaces.
    var snapped = Vector2(round(dir.x), round(dir.y))
    anim_player.set_blend(snapped)   # or use AnimationTree if present
```

---

## Enemy Types

### Grunt (melee charger)
```gdscript
# scenes/enemies/grunt.gd
extends EnemyBase

func _ready() -> void:
    _setup(Enum.EnemyType.GRUNT)

func _attack() -> void:
    anim_player.play("attack")
    # Hitbox method track enables/disables hitbox during swing frame.
    # No projectile — just the melee swing.
```

### Archer (keeps distance, fires arrows)
```gdscript
# scenes/enemies/archer.gd
extends EnemyBase

const PROJ_SCENE = preload("res://scenes/projectiles/projectile.tscn")

func _ready() -> void:
    _setup(Enum.EnemyType.ARCHER)

func _do_chase() -> void:
    if player_ref == null: return
    var dist = global_position.distance_to(player_ref.global_position)
    # Keep preferred distance — back away if too close
    if dist < stats["preferred_distance"] * 0.7:
        var away = (global_position - player_ref.global_position).normalized()
        velocity = away * stats["speed"]
        move_and_slide()
        return
    if dist <= stats["attack_range"]:
        state = Enum.EnemyState.ATTACK
        if attack_timer.is_stopped(): attack_timer.start()
        velocity = Vector2.ZERO
        return
    super._do_chase()

func _attack() -> void:
    anim_player.play("shoot")
    # Spawn arrow at attack frame via method track:

func spawn_projectile() -> void:   # called by method track
    var proj = PROJ_SCENE.instantiate()
    get_parent().add_child(proj)
    proj.global_position = global_position
    var dir  = (player_ref.global_position - global_position).normalized()
    proj.setup(Enum.ProjectileType.ARROW, dir, false)  # false = enemy-owned
    proj.damage      = stats["atk"]
    proj.damage_type = Enum.DamageType.PHYSICAL
```

### Mage (AOE spells + teleport when low HP)
```gdscript
# scenes/enemies/mage.gd
extends EnemyBase

const PROJ_SCENE = preload("res://scenes/projectiles/projectile.tscn")
var   teleport_used : bool = false

func _ready() -> void:
    _setup(Enum.EnemyType.MAGE)

func take_damage(amount: int, type: Enum.DamageType, knockback: Vector2 = Vector2.ZERO) -> void:
    super.take_damage(amount, type, knockback)
    if not teleport_used and health < stats["max_hp"] * stats["teleport_hp_threshold"]:
        teleport_used = true
        _teleport()

func _teleport() -> void:
    # Jump to a random walkable position far from player
    var angle  = randf() * TAU
    var offset = Vector2(cos(angle), sin(angle)) * 150.0
    var target = global_position + offset
    var tween  = create_tween()
    flash_sprite.flash(0.3, 0.0)
    tween.tween_interval(0.3)
    tween.tween_callback(func(): global_position = target)
    tween.tween_callback(func(): flash_sprite.flash(0.0, 0.3))

func _attack() -> void:
    anim_player.play("cast")

func spawn_fireball() -> void:   # method track
    var proj = PROJ_SCENE.instantiate()
    get_parent().add_child(proj)
    proj.global_position = global_position
    var dir  = (player_ref.global_position - global_position).normalized()
    proj.setup(Enum.ProjectileType.FIREBALL, dir, false)
    proj.damage      = stats["atk"]
    proj.damage_type = Enum.DamageType.FIRE
    proj.aoe_radius  = stats["aoe_radius"]
```

### Exploder (suicide bomber)
```gdscript
# scenes/enemies/exploder.gd
extends EnemyBase

var fuse_active : bool = false

func _ready() -> void:
    _setup(Enum.EnemyType.EXPLODER)

func _attack() -> void:
    if fuse_active: return
    fuse_active = true
    anim_player.play("fuse")   # flashing animation while counting down
    # Flash faster as fuse burns
    var tween = create_tween()
    tween.tween_interval(stats["fuse_time"])
    tween.tween_callback(_explode)

func _explode() -> void:
    var explosion = preload("res://scenes/vfx/explosion.tscn").instantiate()
    get_parent().add_child(explosion)
    explosion.global_position = global_position
    explosion.radius           = stats["explosion_radius"]
    # Damage all entities in radius
    for body in get_tree().get_nodes_in_group("Player"):
        if body.global_position.distance_to(global_position) <= stats["explosion_radius"]:
            body.take_damage(stats["atk"], Enum.DamageType.PHYSICAL,
                (body.global_position - global_position).normalized() * 120.0)
    EventBus.screen_shake_requested.emit(8.0, 0.4)
    health = 0
    _die()
```

---

## Boss Fight System

```gdscript
# scenes/enemies/boss.gd
extends EnemyBase

var phase       : Enum.BossPhase = Enum.BossPhase.PHASE_1
var phase_changed : bool         = false
var attack_patterns : Array      = []
var current_pattern_idx : int    = 0

# Boss has a dedicated health bar in HUD. EventBus drives it.
signal health_changed(current: int, maximum: int)

func _ready() -> void:
    _setup(Enum.EnemyType.BOSS)
    # Seal the arena doors:
    get_tree().call_group("ArenaDoor", "lock")
    # Start music:
    AudioManager.play_music("music_boss")

func take_damage(amount: int, type: Enum.DamageType, knockback: Vector2 = Vector2.ZERO) -> void:
    super.take_damage(amount, type, knockback)
    health_changed.emit(health, stats["max_hp"])
    _check_phase()

func _check_phase() -> void:
    var pct = float(health) / float(stats["max_hp"])
    if pct < stats["enrage_threshold"] and phase != Enum.BossPhase.ENRAGE:
        _enter_phase(Enum.BossPhase.ENRAGE)
    elif pct < stats["phase2_threshold"] and phase == Enum.BossPhase.PHASE_1:
        _enter_phase(Enum.BossPhase.PHASE_2)

func _enter_phase(new_phase: Enum.BossPhase) -> void:
    phase = new_phase
    EventBus.boss_phase_changed.emit(phase)
    match phase:
        Enum.BossPhase.PHASE_2:
            stats["attack_cooldown"] *= 0.7   # 30% faster attacks
            attack_timer.wait_time = stats["attack_cooldown"]
            flash_sprite.modulate = Color(1.4, 0.8, 0.8)   # slight red tint
            anim_player.play("phase_transition")
            await anim_player.animation_finished
        Enum.BossPhase.ENRAGE:
            stats["speed"] *= 1.4
            flash_sprite.modulate = Color(2.0, 0.5, 0.5)   # strong red
            # Spawn particles trail:
            $EnrageParticles.emitting = true
            anim_player.play("enrage_roar")
            EventBus.screen_shake_requested.emit(10.0, 0.8)
            await anim_player.animation_finished

func _attack() -> void:
    # Rotate through attack patterns depending on phase
    match phase:
        Enum.BossPhase.PHASE_1: _pattern_basic_slam()
        Enum.BossPhase.PHASE_2: _pattern_multishot() if (current_pattern_idx % 2 == 0) else _pattern_charge()
        Enum.BossPhase.ENRAGE:  _pattern_enrage_barrage()
    current_pattern_idx += 1

func _pattern_basic_slam() -> void:
    anim_player.play("slam")
    # Hitbox activates at slam frame via method track

func _pattern_multishot() -> void:
    anim_player.play("shoot_burst")
    # Spawns 5 projectiles in arc via method track → spawn_burst()

func spawn_burst() -> void:
    for i in 5:
        var angle = deg_to_rad(-60 + i * 30)
        var base  = (player_ref.global_position - global_position).normalized()
        var dir   = base.rotated(angle)
        var proj  = preload("res://scenes/projectiles/projectile.tscn").instantiate()
        get_parent().add_child(proj)
        proj.global_position = global_position
        proj.setup(Enum.ProjectileType.FIREBALL, dir, false)
        proj.damage = stats["atk"]

func _pattern_charge() -> void:
    # Rush toward player at high speed
    var dir   = (player_ref.global_position - global_position).normalized()
    velocity  = dir * stats["speed"] * 3.0
    anim_player.play("charge")
    var tween = create_tween()
    tween.tween_interval(0.4)
    tween.tween_callback(func(): velocity = Vector2.ZERO)

func _pattern_enrage_barrage() -> void:
    # Continuous projectile spiral
    for i in 8:
        var angle = deg_to_rad(i * 45)
        var dir   = Vector2.RIGHT.rotated(angle)
        var proj  = preload("res://scenes/projectiles/projectile.tscn").instantiate()
        get_parent().add_child(proj)
        proj.global_position = global_position
        proj.setup(Enum.ProjectileType.VOID_ORB, dir, false)
        proj.damage = int(stats["atk"] * 0.6)

func _die() -> void:
    # Boss death sequence
    state = Enum.EnemyState.DEAD
    set_physics_process(false)
    $CollisionShape2D.set_deferred("disabled", true)
    # Cinematic death:
    var tween = create_tween()
    tween.tween_property(self, "modulate", Color.WHITE * 3.0, 0.1)
    tween.tween_interval(0.3)
    tween.tween_callback(_play_death_explosion)
    tween.tween_interval(1.5)
    tween.tween_callback(func():
        _spawn_drops()
        EventBus.boss_died.emit()
        get_tree().call_group("ArenaDoor", "unlock")
        AudioManager.crossfade_music(Data.LEVEL_DATA[GameManager.current_level_id]["music"])
        queue_free()
    )

func _play_death_explosion() -> void:
    for i in 8:
        var exp = preload("res://scenes/vfx/explosion.tscn").instantiate()
        get_parent().add_child(exp)
        exp.global_position = global_position + Vector2(randf_range(-40,40), randf_range(-40,40))
        await get_tree().create_timer(0.15).timeout
    EventBus.screen_shake_requested.emit(12.0, 1.0)
```

---

## Shield Bearer (blocks frontal damage)

```gdscript
# scenes/enemies/shield_bearer.gd
extends EnemyBase

var shield_active : bool = true

func _ready() -> void:
    _setup(Enum.EnemyType.SHIELD_BEARER)
    add_to_group("Shield")   # projectile.gd checks for this group

func take_damage(amount: int, type: Enum.DamageType, knockback: Vector2 = Vector2.ZERO) -> void:
    if shield_active:
        # Check if hit came from the front (within 90° shield arc)
        if player_ref:
            var to_player = (player_ref.global_position - global_position).normalized()
            var shield_dir = last_direction
            var dot = to_player.dot(shield_dir)
            if dot > 0.3:   # player is roughly in front → shield blocks
                # Spawn block VFX, no damage
                flash_sprite.flash(0.05, 0.1)
                return
    super.take_damage(amount, type, knockback)
```

---

## Room Locking on Enemy Entry

```gdscript
# scenes/objects/arena_door.gd
extends Node2D

@onready var sprite    = $Sprite2D
@onready var collision = $StaticBody2D/CollisionShape2D

func lock() -> void:
    sprite.frame    = 1   # closed door frame
    collision.disabled = false

func unlock() -> void:
    sprite.frame    = 0   # open door frame
    collision.disabled = true
    var tween = create_tween()
    tween.tween_property(self, "modulate:a", 0.0, 0.5)
    tween.tween_callback(queue_free)
```
