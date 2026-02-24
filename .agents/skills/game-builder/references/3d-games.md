# 3D Games — All Genres

Every architecture pattern references .docs/ for API verification.

---

## 3D First-Person (FPS, Horror, Exploration)

**Examples:** Doom, Half-Life, Minecraft, Amnesia, Portal

### Scene Tree
```
Player (CharacterBody3D)            player.gd
  CollisionShape3D                  CapsuleShape3D r=0.4 h=1.8, pos.y=0.9
  Head (Node3D)                     position.y=1.6 (eye height)
    Camera3D                        fov=75, current=true
    RayCast3D                       target=(0,0,-5), enabled=true
    GunModel (Node3D)               weapon meshes (children of camera)
  HurtBox (Area3D)                  damage detection
```
- `.docs/godot-docs-md/classes/class_characterbody3d.md`
- `.docs/godot-docs-md/classes/class_camera3d.md`
- `.docs/godot-docs-md/classes/class_raycast3d.md`

### Mouse Look

```gdscript
# .docs/godot-docs-md/classes/class_input.md — mouse modes
func _ready():
    Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _input(event):
    if event is InputEventMouseMotion and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
        rotate_y(-event.relative.x * SENSITIVITY)         # yaw on body
        _head.rotate_x(-event.relative.y * SENSITIVITY)   # pitch on head
        _head.rotation.x = clamp(_head.rotation.x, -PI/2, PI/2)  # prevent over-rotation

func _notification(what):
    if what == NOTIFICATION_WM_WINDOW_FOCUS_OUT:
        Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
```
- `.docs/godot-docs-md/classes/class_inputeventmousemotion.md`

### Movement (Gravity + Walk)

```gdscript
# .docs/godot-docs-md/classes/class_characterbody3d.md — velocity, move_and_slide
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

func _physics_process(delta):
    if not is_on_floor():
        velocity.y -= gravity * delta

    if Input.is_action_just_pressed("jump") and is_on_floor():
        velocity.y = JUMP_VELOCITY

    var input_dir = Input.get_vector("move_left", "move_right", "move_forward", "move_back")
    # Camera-relative movement:
    var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
    velocity.x = direction.x * speed
    velocity.z = direction.z * speed

    move_and_slide()
```

### Fly Mode (No Gravity, Voxel-style)

```gdscript
var dir = Vector3.ZERO
if Input.is_action_pressed("move_forward"): dir.z -= 1
if Input.is_action_pressed("move_back"):    dir.z += 1
if Input.is_action_pressed("move_left"):    dir.x -= 1
if Input.is_action_pressed("move_right"):   dir.x += 1
dir = dir.normalized()
dir = (_head.global_transform.basis * dir).normalized()  # camera-relative
# .docs/godot-docs-md/tutorials/3d/using_transforms.md

var up = Vector3.ZERO
if Input.is_action_pressed("jump"):   up.y += 1
if Input.is_action_pressed("crouch"): up.y -= 1
velocity = (dir + up).normalized() * speed
move_and_slide()
```

### Block Interaction (Voxel)

```gdscript
# .docs/godot-docs-md/classes/class_raycast3d.md
var hit_pos = _raycast.get_collision_point()
var normal = _raycast.get_collision_normal()
var break_block = Vector3i((hit_pos - normal / 2).floor())   # inside hit block
var place_block = Vector3i((hit_pos + normal / 2).floor())   # adjacent empty
```

### Weapon/Shooting

```gdscript
# Hitscan: use RayCast3D from camera
# .docs/godot-docs-md/classes/class_raycast3d.md
if _raycast.is_colliding():
    var target = _raycast.get_collider()
    if target.has_method("take_damage"):
        target.take_damage(weapon_damage)

# Projectile: spawn RigidBody3D or Area3D at gun barrel
# .docs/godot-docs-md/classes/class_rigidbody3d.md — apply_impulse
var bullet = bullet_scene.instantiate()
bullet.position = _gun_barrel.global_position
bullet.linear_velocity = -_camera.global_transform.basis.z * BULLET_SPEED
get_parent().add_child(bullet)
```

---

## 3D Third-Person (Action-Adventure, Souls-like, 3D Platformer)

**Examples:** Dark Souls, God of War, Mario 64, Tomb Raider

### Scene Tree
```
Player (CharacterBody3D)            player.gd
  CollisionShape3D                  CapsuleShape3D
  PlayerModel (Node3D)              character mesh + AnimationPlayer
  CameraPivot (Node3D)              rotates with mouse
    SpringArm3D                     spring_length=4, collision_mask=terrain
      Camera3D                      fov=60
  HitBox (Area3D)                   melee attack range
  HurtBox (Area3D)                  damage detection
  LockOnTarget (RayCast3D)          for target locking
```
- `.docs/godot-docs-md/classes/class_springarm3d.md` — prevents camera clipping through walls
- `.docs/godot-docs-md/tutorials/3d/spring_arm.md`

### Camera-Relative Movement

```gdscript
func _physics_process(delta):
    var input = Input.get_vector("move_left", "move_right", "move_forward", "move_back")

    # Get camera's forward/right on XZ plane (ignore pitch)
    var cam_forward = -_camera.global_transform.basis.z
    cam_forward.y = 0; cam_forward = cam_forward.normalized()
    var cam_right = _camera.global_transform.basis.x
    cam_right.y = 0; cam_right = cam_right.normalized()

    var direction = (cam_right * input.x + cam_forward * input.y).normalized()

    if direction:
        # Smooth rotation toward movement direction
        var target_angle = atan2(direction.x, direction.z)
        rotation.y = lerp_angle(rotation.y, target_angle, ROTATION_SPEED * delta)

    velocity.x = direction.x * speed
    velocity.z = direction.z * speed
    if not is_on_floor(): velocity.y -= gravity * delta

    move_and_slide()
```

### SpringArm3D Camera

```gdscript
# Mouse orbits CameraPivot, SpringArm3D auto-shortens on wall collision
func _input(event):
    if event is InputEventMouseMotion:
        _camera_pivot.rotate_y(-event.relative.x * SENSITIVITY)
        _camera_pivot.rotate_x(-event.relative.y * SENSITIVITY)
        _camera_pivot.rotation.x = clamp(_camera_pivot.rotation.x, -0.8, 0.6)
```

### Lock-On System

```gdscript
func _find_lock_target() -> Node3D:
    var enemies = get_tree().get_nodes_in_group("Enemies")
    var closest: Node3D = null
    var closest_dist = LOCK_ON_RANGE
    for e in enemies:
        var dist = global_position.distance_to(e.global_position)
        if dist < closest_dist:
            closest = e; closest_dist = dist
    return closest
```

---

## 3D Voxel (Minecraft-like)

**Examples:** Minecraft, Terraria 3D, survival crafting

### Architecture Overview

```
World (Node, world.gd)           chunk manager
  +-- Player (CharacterBody3D)   first-person, fly mode
  +-- Sky (sky.gd)               day/night, DirectionalLight3D
  +-- Generator (generator.gd)   FastNoiseLite terrain
  +-- Database (database.gd)     SQLite persistence
  +-- HUD (hud.gd)               stats + block display
  +-- [Chunk nodes at runtime]   StaticBody3D + ArrayMesh
```

### Key Systems

**Chunk:** W×H×W blocks (tune per game). Block storage = 1D array. Index = `x + z*W + y*W*W`.
- Flag-based state machine (GENERATING, MESHING, DONE)
- WorkerThreadPool for async generation + meshing
- `.docs/godot-docs-md/classes/class_workerthreadpool.md`

**Face Culling:** For each block, check 6 neighbors. Only add face if neighbor is transparent/air. THE critical optimization.
- `.docs/godot-docs-md/classes/class_arraymesh.md` for custom mesh building

**Generator:** FastNoiseLite for height. `height = BASE_HEIGHT + int(noise.get_noise_2d(wx, wz) * AMPLITUDE)`.
- `.docs/godot-docs-md/classes/class_fastnoiselite.md`
- Layer block types by height (e.g., stone below surface, dirt near surface, grass on top, water below sea level)

**Shaders:** Separate materials for opaque, transparent, and sprite blocks, all sampling same Texture2DArray.
- `.docs/godot-docs-md/classes/class_texture2darray.md`
- `.docs/godot-docs-md/classes/class_shadermaterial.md`

**Persistence:** godot-sqlite addon or JSON. Store only player edits (not generated terrain), player position, world state.
- All DB access mutex-locked — `.docs/godot-docs-md/classes/class_mutex.md`

**Gotchas:**
- All scene tree ops via call_deferred (worker threads can't touch nodes)
- Spawn player above generated terrain height
- RayCast3D target (0,0,-N) = N units forward (Godot -Z forward)

---

## 3D Racing

**Examples:** Need for Speed, Mario Kart, Trackmania

### VehicleBody3D Approach (Simulation)

```
Vehicle (VehicleBody3D)             vehicle.gd
  CollisionShape3D                  BoxShape3D (car body)
  MeshInstance3D                    car model
  FrontLeft (VehicleWheel3D)        use_as_steering=true
  FrontRight (VehicleWheel3D)       use_as_steering=true
  RearLeft (VehicleWheel3D)         use_as_traction=true
  RearRight (VehicleWheel3D)        use_as_traction=true
  Camera3D / SpringArm3D            chase camera
```
- `.docs/godot-docs-md/classes/class_vehiclebody3d.md` — engine_force, steering, brake
- `.docs/godot-docs-md/classes/class_vehiclewheel3d.md` — suspension, friction

```gdscript
func _physics_process(delta):
    engine_force = Input.get_axis("brake", "accelerate") * MAX_ENGINE_FORCE
    steering = Input.get_axis("steer_right", "steer_left") * MAX_STEERING
    brake = Input.get_action_strength("handbrake") * MAX_BRAKE
```

### Arcade Approach (Sphere Car)

Use RigidBody3D sphere for physics + MeshInstance3D car body that follows:
```gdscript
# .docs/godot-docs-md/classes/class_rigidbody3d.md — apply_force
# Force applied in car_mesh facing direction
_sphere.apply_force(-_car_mesh.global_transform.basis.z * accel_force)
# Car mesh smoothly follows sphere
_car_mesh.global_position = _car_mesh.global_position.lerp(_sphere.global_position, 10 * delta)
```

### Track Design

- Path3D for road centerline — `.docs/godot-docs-md/classes/class_path3d.md`
- CSGPolygon3D along path for road mesh — `.docs/godot-docs-md/classes/class_csgpolygon3d.md`
- Checkpoints: Area3D triggers along track
- Lap counting: track checkpoint order, lap on start/finish

---

## 3D Open-World

### Chunk Loading Pattern

```gdscript
var loaded_chunks: Dictionary = {}  # Vector2i -> chunk_node

func _process(delta):
    var player_chunk = Vector2i(
        int(player.position.x / CHUNK_SIZE),
        int(player.position.z / CHUNK_SIZE)
    )
    # Load nearby
    for x in range(-RENDER_DIST, RENDER_DIST + 1):
        for z in range(-RENDER_DIST, RENDER_DIST + 1):
            var coord = player_chunk + Vector2i(x, z)
            if coord not in loaded_chunks:
                _load_chunk(coord)
    # Unload far
    for coord in loaded_chunks.keys():
        if coord.distance_to(player_chunk) > RENDER_DIST + 1:
            _unload_chunk(coord)
```

### Day/Night Sky (3D)

```gdscript
# .docs/godot-docs-md/classes/class_directionallight3d.md
# .docs/godot-docs-md/classes/class_proceduralskymaterial.md
var time_of_day: float = 0.0  # 0.0 to 1.0

func _process(delta):
    time_of_day = fmod(time_of_day + speed * delta, 1.0)
    _sun.rotation_degrees.x = -time_of_day * 360
    _sun.light_energy = clamp(sin(time_of_day * TAU), 0, 1)
```

---

## Universal 3D Patterns

### 3D Lighting

- DirectionalLight3D (sun) — `.docs/godot-docs-md/classes/class_directionallight3d.md`
- OmniLight3D (point lights, torches) — `.docs/godot-docs-md/classes/class_omnilight3d.md`
- SpotLight3D (flashlights, lamps) — `.docs/godot-docs-md/classes/class_spotlight3d.md`
- WorldEnvironment for ambient — `.docs/godot-docs-md/classes/class_worldenvironment.md`

### 3D Audio

- AudioStreamPlayer3D for spatial SFX — `.docs/godot-docs-md/classes/class_audiostreamplayer3d.md`
- AudioListener3D on camera — `.docs/godot-docs-md/classes/class_audiolistener3d.md`

### 3D Navigation

- NavigationRegion3D with baked navmesh — `.docs/godot-docs-md/classes/class_navigationregion3d.md`
- NavigationAgent3D on enemies — `.docs/godot-docs-md/classes/class_navigationagent3d.md`
- Same API pattern as 2D: set target_position, get_next_path_position, move toward it

### Stealth / Horror Mechanics

**Vision cone detection:**
```gdscript
func _can_see_player() -> bool:
    var to_player = player.global_position - global_position
    var forward = -global_transform.basis.z
    var angle = forward.angle_to(to_player)
    if angle > FOV_RADIANS / 2: return false
    if to_player.length() > DETECT_RANGE: return false
    # Raycast to check line of sight
    # .docs/godot-docs-md/classes/class_raycast3d.md
    _sight_ray.target_position = to_player
    _sight_ray.force_raycast_update()
    return _sight_ray.get_collider() == player
```

**Noise detection:**
```gdscript
# Player emits noise_made(position, radius) signal
# Enemies in range switch to INVESTIGATE state
func _on_noise(pos: Vector3, radius: float):
    if global_position.distance_to(pos) < radius:
        investigate_position = pos
        state = State.INVESTIGATE
```

**Light-level detection:**
```gdscript
# Track how lit the player is (sum of nearby light energies)
# Enemies check player.light_level against threshold
```
