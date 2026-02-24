# 2D Games — All Genres

Every architecture pattern references .docs/ for API verification.

---

## 2D Platformer (Side-View with Gravity)

**Examples:** Mario, Celeste, Hollow Knight, Mega Man, Metroidvania

### Scene Tree
```
Player (CharacterBody2D)         motion_mode=Grounded
  CollisionShape2D               CapsuleShape2D
  Sprite2D / AnimatedSprite2D
  AnimationPlayer
  Camera2D                       position_smoothing=true, limits per level
  CoyoteTimer (Timer)            wait_time=0.1, one_shot=true
  JumpBufferTimer (Timer)        wait_time=0.1, one_shot=true
  HurtBox (Area2D)               detects enemy hitboxes
```
- `.docs/godot-docs-md/classes/class_characterbody2d.md` — motion_mode, is_on_floor(), is_on_wall()
- `.docs/godot-docs-md/tutorials/physics/using_character_body_2d.md`

### Movement Architecture

```gdscript
# Gravity from project settings:
# .docs/godot-docs-md/classes/class_projectsettings.md
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

func _physics_process(delta):
    # Gravity — .docs/godot-docs-md/classes/class_characterbody2d.md
    if not is_on_floor():
        velocity.y += gravity * delta

    # Jump with coyote time + jump buffer
    if Input.is_action_just_pressed("jump"):
        if is_on_floor() or not $CoyoteTimer.is_stopped():
            velocity.y = JUMP_SPEED  # negative value (up)
        else:
            $JumpBufferTimer.start()  # buffer the jump

    # Variable jump height (release early = lower jump)
    if Input.is_action_just_released("jump") and velocity.y < 0:
        velocity.y *= 0.5

    # Horizontal with acceleration/friction for game feel
    var input_dir = Input.get_axis("move_left", "move_right")
    if input_dir:
        velocity.x = lerp(velocity.x, input_dir * MAX_SPEED, ACCELERATION * delta)
    else:
        velocity.x = lerp(velocity.x, 0.0, FRICTION * delta)

    move_and_slide()

    # Coyote time: start timer when leaving floor
    if was_on_floor and not is_on_floor():
        $CoyoteTimer.start()
    was_on_floor = is_on_floor()
```

### Advanced Mechanics

**Wall jump** — `.docs/godot-docs-md/classes/class_characterbody2d.md` (is_on_wall, get_wall_normal):
```gdscript
if is_on_wall() and Input.is_action_just_pressed("jump"):
    velocity = get_wall_normal() * WALL_JUMP_H_SPEED + Vector2(0, WALL_JUMP_V_SPEED)
```

**Dash** — burst movement with cooldown:
```gdscript
velocity = facing_direction * DASH_SPEED
# Use tween or timer to restore normal state after dash_duration
```

**Double jump** — track `jumps_remaining`, reset on floor.

**One-way platforms** — `.docs/godot-docs-md/classes/class_staticbody2d.md`:
Set `collision_layer` on thin StaticBody2D platforms, use `set_collision_mask_value()` on player to drop through.

### Level Design

- TileMapLayer for terrain — `.docs/godot-docs-md/classes/class_tilemaplayer.md`
- Parallax scrolling — `.docs/godot-docs-md/classes/class_parallax2d.md`
- Camera limits per level — `.docs/godot-docs-md/classes/class_camera2d.md` (limit_left/right/top/bottom)
- Checkpoints: Area2D triggers that save player position

---

## 2D Top-Down (RPG, Adventure, Farming, Twin-Stick)

**Examples:** Zelda, Stardew Valley, Hades, Vampire Survivors, Enter the Gungeon

### Scene Tree
```
Player (CharacterBody2D)         motion_mode=Floating
  CollisionShape2D               CapsuleShape2D
  Sprite2D / FlashSprite2D       for hit feedback
  AnimationPlayer
  AnimationTree                  BlendTree root, active=true
  Camera2D                       zoom=(3,3) or (4,4), smoothing=true
  MeleeHitbox (Area2D)           monitoring=false, enabled by anim method tracks
  RayCast2D                      for interaction detection
  ProjectileSpawn (Marker2D)     projectile origin point
```
- `.docs/godot-docs-md/classes/class_characterbody2d.md` — Floating mode (no gravity, no is_on_floor)

### Movement Architecture

```gdscript
func _physics_process(delta):
    var raw = Input.get_vector("move_left", "move_right", "move_up", "move_down")
    # .docs/godot-docs-md/classes/class_input.md — get_vector()
    velocity = raw * speed
    move_and_slide()

    if raw != Vector2.ZERO:
        last_direction = raw  # persist for tools/attacks when standing still
        _update_animation("Walk", raw)
    else:
        _update_animation("Idle", last_direction)
```

### AnimationTree for 8-Direction

```
BlendTree root:
  MoveStateMachine (Idle <-> Walk, BlendSpace2D 9 points each)
  -> AttackOneShot (or ToolOneShot)
  -> Output
```
- 9 points per BlendSpace2D: (-1,-1) to (1,1)
- ALWAYS round direction: `Vector2(round(dir.x), round(dir.y))`
- Update BOTH idle and walk blend positions every frame
- `.docs/godot-docs-md/classes/class_animationtree.md`
- `.docs/godot-docs-md/classes/class_animationnodeblendspace2d.md`

### State Machine Pattern

```gdscript
enum State { IDLE, MOVE, ATTACK, DODGE, HURT, INTERACT, DEAD }
var state: State = State.IDLE

func _physics_process(delta):
    match state:
        State.IDLE, State.MOVE:
            _handle_movement(delta)
            _handle_input()
        State.ATTACK:
            pass  # animation drives, method track re-enables input
        State.DODGE:
            _do_dodge(delta)
        State.HURT:
            _apply_knockback(delta)
```

### Tool/Farming System

For farming games (Stardew-like):
```
ToolStateMachine: one BlendSpace2D per tool (Axe, Hoe, Water, Sword, etc.)
ToolOneShot fires tool animation, method track calls tool_use_emit()
```
- Tool cycling: `posmod(current + dir, Enum.Tool.size()) as Enum.Tool`
- Movement locked during tool animation: `can_move` flag via animation_started/finished signals
- RayCast2D for interaction (bed, NPC, shop) — `.docs/godot-docs-md/classes/class_raycast2d.md`

### Top-Down Level Architecture

```
Level (Node2D)
  +-- World/         TileMapLayers (terrain, water, decorations)
  +-- Entities/      Y-Sort enabled (player, NPCs, enemies)
  +-- Projectiles/
  +-- VFX/
  +-- Overlay/       CanvasLayer (HUD, transitions)
  +-- Timers/
```
- Y-sort: Node2D > Y Sort Enabled = true — auto depth sorting
- NavigationRegion2D for enemy pathfinding — `.docs/godot-docs-md/classes/class_navigationregion2d.md`

---

## 2D Side-Scroller (Beat-em-up, Run-and-Gun)

**Examples:** Streets of Rage, Contra, Metal Slug

### Scene Tree
```
Player (CharacterBody2D)         motion_mode=Grounded (with gravity)
  CollisionShape2D               CapsuleShape2D
  AnimatedSprite2D
  Camera2D                       drag_horizontal_enabled for auto-scroll feel
  HitBox (Area2D)                melee range
  HurtBox (Area2D)               damage detection
```

### Key Differences from Platformer

- Limited vertical movement (may have small jumps but focus is horizontal)
- Multi-lane system: Y position determines depth (fake 2.5D)
- Enemy waves spawn from screen edges
- Auto-scroll or player-pushed scroll

### Multi-Lane Movement (Beat-em-up)

```gdscript
# Horizontal movement (main axis)
velocity.x = Input.get_axis("move_left", "move_right") * speed

# Vertical movement (lane switching, limited range)
velocity.y = Input.get_axis("move_up", "move_down") * speed * 0.6

# Clamp Y to lane range
position.y = clamp(position.y, LANE_MIN_Y, LANE_MAX_Y)
```

---

## 2D Puzzle / Grid-Based / Strategy

**Examples:** Tetris, Match-3, Sokoban, Chess, Tower Defense path

### Architecture Pattern

**Separate data from visuals:**
```gdscript
# Data layer: pure arrays/dicts — fast logic
var grid: Array[Array] = []  # grid[x][y] = cell_type

# Visual layer: TileMapLayer or Sprite2D nodes — rendering only
func _sync_visuals():
    for x in WIDTH:
        for y in HEIGHT:
            tile_map.set_cell(Vector2i(x, y), 0, _type_to_atlas(grid[x][y]))
```

**Grid state management:**
- All game logic operates on arrays/dictionaries (fast)
- TileMapLayer is updated as a rendering step (slow, batch updates)
- `.docs/godot-docs-md/classes/class_tilemaplayer.md`

**Input for grid games:**
- Click: `_input(event)` with `event is InputEventMouseButton`
- Grid coord from mouse: `tile_map.local_to_map(tile_map.get_local_mouse_position())`
- `.docs/godot-docs-md/classes/class_inputeventmousebutton.md`

### Match-3 / Falling Pieces

```gdscript
# Check matches after every move:
func _find_matches() -> Array:
    var matches = []
    # Horizontal check
    for y in HEIGHT:
        for x in range(WIDTH - 2):
            if grid[x][y] == grid[x+1][y] and grid[x][y] == grid[x+2][y]:
                matches.append_array([Vector2i(x,y), Vector2i(x+1,y), Vector2i(x+2,y)])
    # Vertical check (similar)
    return matches

# Gravity: shift pieces down to fill gaps
func _apply_gravity():
    for x in WIDTH:
        var write_y = HEIGHT - 1
        for y in range(HEIGHT - 1, -1, -1):
            if grid[x][y] != EMPTY:
                grid[x][write_y] = grid[x][y]
                write_y -= 1
        while write_y >= 0:
            grid[x][write_y] = _random_piece()
            write_y -= 1
```

### Tower Defense Path

- Use Path2D + PathFollow2D for enemy movement along pre-defined paths
- `.docs/godot-docs-md/classes/class_path2d.md`
- `.docs/godot-docs-md/classes/class_pathfollow2d.md`
- Tower placement on grid: snap to grid coords, check occupancy

---

## Universal 2D Patterns

### Screen Shake (Camera2D)

```gdscript
# .docs/godot-docs-md/classes/class_camera2d.md — offset property
var trauma: float = 0.0

func add_trauma(amount: float):
    trauma = min(trauma + amount, 1.0)

func _process(delta):
    trauma = max(trauma - DECAY * delta, 0.0)
    var shake = trauma * trauma  # quadratic falloff
    $Camera2D.offset = Vector2(
        randf_range(-1, 1) * MAX_OFFSET * shake,
        randf_range(-1, 1) * MAX_OFFSET * shake
    )
```

### Hit-Stop (Freeze Frame)

```gdscript
func hit_stop(duration: float = 0.06):
    Engine.time_scale = 0.05
    await get_tree().create_timer(duration, true, false, true).timeout  # process_always=true
    Engine.time_scale = 1.0
```

### Flash Hit Feedback

VisualShader mixing original color with white via Progress parameter:
- `local_to_scene = true` MANDATORY on ShaderMaterial
- `.docs/godot-docs-md/classes/class_shadermaterial.md`

### Damage Numbers (Floating Text)

```gdscript
var label = Label.new()
label.text = str(damage)
label.position = world_pos
add_child(label)
var tween = create_tween()
tween.tween_property(label, "position:y", label.position.y - 30, 0.5)
tween.parallel().tween_property(label, "modulate:a", 0.0, 0.5)
tween.tween_callback(label.queue_free)
```

### Projectile Pattern

```gdscript
# projectile.gd — extends Area2D
# .docs/godot-docs-md/classes/class_area2d.md
var direction: Vector2
var speed: float
var damage: int

func _physics_process(delta):
    position += direction * speed * delta

func _on_body_entered(body):
    if body.has_method("take_damage"):
        body.take_damage(damage)
    queue_free()
```

### Day/Night Cycle (2D)

```gdscript
# .docs/godot-docs-md/classes/class_canvasmodulate.md
@export var daytime_gradient: Gradient  # 4 stops: dawn -> day -> day -> night

func _process(_delta):
    var t = 1.0 - ($DayTimer.time_left / $DayTimer.wait_time)
    $CanvasModulate.color = daytime_gradient.sample(t)
```

### Circle Wipe Transition

Apply code shader to full-screen ColorRect. Tween `shader_parameter/progress` 0->1 (close) -> do transition -> 1->0 (open).
