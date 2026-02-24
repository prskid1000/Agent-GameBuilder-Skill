# Godot Foundations — Core Concepts, Engine Guide, Project Setup

Every concept includes the .docs path for API verification. The coding agent MUST
check these paths before writing any Godot API calls.

---

## Engine Guide

### Editor Layout

```
+---------------------------------------------------------------+
| Menu bar (Scene / Project / Debug / Editor / Help)            |
+----------+-----------------------------+----------------------+
| Scene    |                             | Inspector            |
| panel    |     2D/3D Viewport          | (properties)         |
| (node    |                             |                      |
| tree)    |                             | Node panel           |
|          |                             | (signals/groups)     |
+----------+-----------------------------+----------------------+
| FileSystem  | Output / Debugger / Audio / Animation           |
+---------------------------------------------------------------+
```

### Key Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+S | Save scene |
| Ctrl+A | Add node |
| Ctrl+D | Duplicate node |
| F | Focus on selected |
| Q/W/E/S | Select/Move/Rotate/Scale tools |
| R/H/V | Flip/rotate tile in TileMap |
| F5 | Run main scene |
| F8 | Stop running |

### Creating Scenes

Root node types and when to use them:

| Root Node | Use Case | .docs |
|-----------|----------|-------|
| CharacterBody2D | 2D player, enemies | `.docs/godot-docs-md/classes/class_characterbody2d.md` |
| CharacterBody3D | 3D player, enemies | `.docs/godot-docs-md/classes/class_characterbody3d.md` |
| RigidBody2D | Physics-driven 2D objects | `.docs/godot-docs-md/classes/class_rigidbody2d.md` |
| RigidBody3D | Physics-driven 3D objects | `.docs/godot-docs-md/classes/class_rigidbody3d.md` |
| StaticBody2D | Non-moving colliders, walls | `.docs/godot-docs-md/classes/class_staticbody2d.md` |
| StaticBody3D | Non-moving 3D geometry | `.docs/godot-docs-md/classes/class_staticbody3d.md` |
| Area2D | Triggers, hitboxes, pickups | `.docs/godot-docs-md/classes/class_area2d.md` |
| Area3D | 3D triggers, detection zones | `.docs/godot-docs-md/classes/class_area3d.md` |
| Node2D | Generic 2D container | `.docs/godot-docs-md/classes/class_node2d.md` |
| Node3D | Generic 3D container | `.docs/godot-docs-md/classes/class_node3d.md` |
| Control | UI elements | `.docs/godot-docs-md/classes/class_control.md` |
| CanvasLayer | UI that ignores camera | `.docs/godot-docs-md/classes/class_canvaslayer.md` |

### Importing Art

**Pixel art:** `Project > Project Settings > Rendering > Textures > Default Texture Filter > Nearest`
- `.docs/godot-docs-md/classes/class_projectsettings.md` for all settings

**Spritesheet on Sprite2D:**
- Set `hframes` (columns) and `vframes` (rows). `frame` property selects cell (0 = top-left)
- `.docs/godot-docs-md/classes/class_sprite2d.md` — check `hframes`, `vframes`, `frame`, `frame_coords`

**Audio formats:**
| Format | Use | Loop |
|--------|-----|------|
| .ogg | Music | Enable in Import tab |
| .wav | Short SFX | Leave off |
| .mp3 | Long SFX/music | Optional |
- `.docs/godot-docs-md/classes/class_audiostreamplayer.md`
- `.docs/godot-docs-md/classes/class_audiostreamplayer2d.md` (spatial 2D)
- `.docs/godot-docs-md/classes/class_audiostreamplayer3d.md` (spatial 3D)

---

## Core Godot Concepts

### 1. Input System

**Reading input** — `.docs/godot-docs-md/classes/class_input.md`:
```gdscript
# 2D 8-directional (top-down): returns normalized Vector2
var dir = Input.get_vector("move_left", "move_right", "move_up", "move_down")

# Single axis (tool cycling, zoom): returns float -1..1
var axis = Input.get_axis("tool_backward", "tool_forward")

# One-shot (attack, jump, interact):
if Input.is_action_just_pressed("jump"): ...

# Held (sprint, crouch):
if Input.is_action_pressed("sprint"): ...
```

**Where to read input:**
- Movement -> `_physics_process(delta)` — tied to physics tick, no jitter
- Mouse/UI -> `_input(event)` — immediate response
- NEVER read movement in `_process()` — frame rate dependent
- `.docs/godot-docs-md/tutorials/inputs/input_examples.md`

### 2. Physics Bodies

**CharacterBody2D** — `.docs/godot-docs-md/classes/class_characterbody2d.md`:
- `velocity` property + `move_and_slide()` handles collisions
- `motion_mode`: **Grounded** (platformer, gravity, `is_on_floor()`) vs **Floating** (top-down, no gravity)
- `.docs/godot-docs-md/tutorials/physics/using_character_body_2d.md`

**CharacterBody3D** — `.docs/godot-docs-md/classes/class_characterbody3d.md`:
- Same `velocity` + `move_and_slide()` pattern
- Used for FPS, TPS, 3D platformer players

**RigidBody2D/3D** — `.docs/godot-docs-md/classes/class_rigidbody2d.md`:
- Physics-driven (forces, torques, gravity). Less control but realistic.
- Use `apply_force()`, `apply_impulse()`, `apply_torque()`
- Good for: projectiles, debris, ragdoll, vehicles (arcade style)

**Collision layers** — `.docs/godot-docs-md/tutorials/physics/physics_introduction.md`:
- `collision_layer` = what this node IS
- `collision_mask` = what this node SEES/detects
- Name layers in Project Settings > Layer Names

### 3. AnimationTree

`.docs/godot-docs-md/classes/class_animationtree.md`

**Node types:**
- **BlendTree** (root): connects sub-nodes -> Output
- **AnimationNodeStateMachine**: named states, travel between them
  ```gdscript
  var sm = anim_tree.get("parameters/MoveStateMachine/playback")
  sm.travel("Walk")  # .docs/godot-docs-md/classes/class_animationnodestatemachinetransition.md
  ```
- **BlendSpace2D**: picks animation from 2D position (direction)
  - 9-point grid: (-1,-1) to (1,1). Y+ = DOWN in game, UP in blend space
  - ALWAYS round direction: `Vector2(round(dir.x), round(dir.y))` before setting
- **AnimationNodeOneShot**: play once then return to base
  ```gdscript
  anim_tree.set("parameters/AttackOneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)
  ```

**Method tracks** — AnimationPlayer calls functions at specific keyframes:
- Enable hitbox at swing apex, emit tool_use at impact frame
- `.docs/godot-docs-md/classes/class_animationplayer.md`

**Signals:** Connect `AnimationTree.animation_started` / `animation_finished`, NOT AnimationPlayer signals (unreliable when controlled by AnimationTree).

### 4. TileMapLayer

`.docs/godot-docs-md/classes/class_tilemaplayer.md`

**Terrain autotiling setup:**
1. TileSet > Terrain Sets > Add Element > Mode: Match Corners and Sides
2. Add terrain, paint tiles + connectivity in TileSet Paint tab
3. Paint in level: select terrain, left-drag

**Code API:**
```gdscript
# Place terrain tile(s)
tile_map.set_cells_terrain_connect([grid_coord], terrain_set, terrain_index)

# Place specific atlas tile
tile_map.set_cell(coord, source_id, atlas_coords)

# Query
var data = tile_map.get_cell_tile_data(coord)  # TileData or null
var custom = data.get_custom_data("farmable")   # custom data layer
var used = tile_map.get_used_cells()             # all occupied cells
```

**Custom Data Layers:** TileSet > Custom Data Layers > Add (name, type). Paint per-tile. Used for game logic (farmable, surface_type, etc.)

**Coordinate conversion (pixel <-> grid):**
```gdscript
var grid = Vector2i(int(pos.x / TILE_SIZE), int(pos.y / TILE_SIZE))
grid.x += -1 if pos.x < 0 else 0  # fix negative truncation
grid.y += -1 if pos.y < 0 else 0
```

### 5. Navigation (Pathfinding)

**2D** — `.docs/godot-docs-md/classes/class_navigationregion2d.md` + `.docs/godot-docs-md/classes/class_navigationagent2d.md`:
```gdscript
# On enemy with NavigationAgent2D child:
nav_agent.target_position = target.global_position
var next = nav_agent.get_next_path_position()
velocity = (next - global_position).normalized() * speed
move_and_slide()
```

**3D** — `.docs/godot-docs-md/classes/class_navigationregion3d.md` + `.docs/godot-docs-md/classes/class_navigationagent3d.md`:
Same API pattern, 3D vectors.

### 6. Cameras

**Camera2D** — `.docs/godot-docs-md/classes/class_camera2d.md`:
- `position_smoothing_enabled = true`, `position_smoothing_speed = 8.0`
- `limit_left/right/top/bottom` for level boundaries
- `zoom` for pixel art (e.g., zoom=(4,4) for 16px tiles at 1080p)

**Camera3D** — `.docs/godot-docs-md/classes/class_camera3d.md`:
- Child of player for FPS (at head height)
- Use with SpringArm3D for TPS — `.docs/godot-docs-md/classes/class_springarm3d.md`
- `.docs/godot-docs-md/tutorials/3d/spring_arm.md` — prevents camera clipping through walls

### 7. Signals and Callables

`.docs/godot-docs-md/tutorials/scripting/gdscript/gdscript_signals.md`

```gdscript
signal damage_dealt(amount: int, position: Vector2)  # declare
damage_dealt.emit(10, global_position)                # emit
player.damage_dealt.connect(_on_damage_dealt)         # connect
```

Pass functions: `Callable(self, "_my_method")` or just pass the method reference directly.

### 8. Custom Resources

`.docs/godot-docs-md/classes/class_resource.md`

```gdscript
class_name ItemData extends Resource
@export var name: String
@export var icon: Texture2D
@export var value: int
var count: int  # runtime only
```

- `emit_changed()` in setters notifies connected nodes
- Pass same Resource instance to multiple nodes -> shared state
- Save with `ResourceSaver.save(res, path)`, load with `ResourceLoader.load(path)`

### 9. Tweens

`.docs/godot-docs-md/classes/class_tween.md`

```gdscript
var tween = create_tween()
tween.tween_property(node, "modulate:a", 0.0, 0.5)   # fade out
tween.tween_interval(0.3)                               # pause
tween.tween_callback(queue_free)                         # then free
tween.tween_property(node, "position", target, 0.2)     # move
```

### 10. Groups

`.docs/godot-docs-md/classes/class_node.md` (see `add_to_group`, `get_tree().get_nodes_in_group`)

Tag nodes for bulk operations:
```gdscript
get_tree().get_nodes_in_group("Enemies")  # all enemies
get_tree().get_first_node_in_group("Player")  # the player
```

### 11. Enums Pattern

```gdscript
enum PlayerState { IDLE, MOVE, ATTACK, DODGE, HURT, DEAD }
enum Tool { AXE, HOE, SWORD, WATER }
# Cycle safely: posmod(current + dir, Enum.Tool.size()) as Enum.Tool
```

### 12. @tool Scripts

Make scripts run in editor for live preview:
```gdscript
@tool
extends StaticBody2D
@export var size: int:
    set(v): size = v; $Sprite2D.frame = size  # updates in editor
```

### 13. Y-Sort (2D)

`Node2D > Ordering > Y Sort Enabled = true`. Children auto-sorted by Y position. No code needed.

### 14. Property Setters

```gdscript
var health := 100:
    set(v):
        health = v
        if health <= 0: die()
        health_changed.emit(health)  # auto-notify
```

### 15. WorkerThreadPool

`.docs/godot-docs-md/classes/class_workerthreadpool.md`

```gdscript
var task_id = WorkerThreadPool.add_task(_heavy_work)
# In _heavy_work: _finish.call_deferred()  # scene tree ops on main thread only
```

### 16. Shaders

**VisualShader** — node graph editor, good for: flash effect, color grading
**Code shaders** (.gdshader) — GLSL-like, good for: circle wipe, water, custom rendering

Flash shader pattern (mix original with white):
```
Progress=0 -> original, Progress=1 -> white
Animate via tween: shader_parameter/Progress 0->1->0
```
**`local_to_scene = true`** on ShaderMaterial is MANDATORY — otherwise all instances share state.

Circle wipe transition:
```glsl
uniform float progress : hint_range(0.0, 1.0);
void fragment() {
    float ratio = SCREEN_PIXEL_SIZE.y / SCREEN_PIXEL_SIZE.x;
    vec2 adj = vec2(mix(0.5, UV.x, ratio), UV.y);
    COLOR.a = step(distance(vec2(0.5), adj), 1.5 - progress * 1.5);
}
```

---

## Project Setup Patterns

### Autoload Singletons

`.docs/godot-docs-md/tutorials/scripting/singletons_autoload.md`

```gdscript
# In project.godot: Enum="*res://global/enums.gd"
extends Node  # must extend Node, not RefCounted
# Access from anywhere: Enum.PlayerState.IDLE, Data.TILE_SIZE
```

Order matters — later autoloads can reference earlier ones.

### Recommended Autoloads by Complexity

| Game Complexity | Autoloads |
|----------------|-----------|
| Simple (puzzle, jam game) | Enum, Data |
| Medium (farming sim, platformer) | Enum, Data, GameManager |
| Complex (RPG, open-world) | Enum, Data, EventBus, GameManager, AudioManager |

### EventBus Pattern

Single autoload holding only signal declarations:
```gdscript
# event_bus.gd
signal player_hp_changed(hp: int, max_hp: int)
signal enemy_died(type, position, xp)
signal screen_shake_requested(magnitude: float, duration: float)
```

Any script emits/connects without direct node references. Decouples UI from gameplay.

### Enum/Data Separation

- **Enums:** vocabulary only (what types exist). No numbers, no paths.
- **Data:** values keyed by enum. All balance numbers, textures, costs.
- Change balance without touching gameplay scripts.

### Physics Layer Convention

| Layer | Name | Typical Use |
|-------|------|-------------|
| 1 | Terrain | Walls, floors, TileMap collision |
| 2 | Player | Player body |
| 3 | Enemies | Enemy bodies |
| 4 | PlayerHitbox | Melee attack areas |
| 5 | EnemyHitbox | Enemy attack areas |
| 6 | Projectiles | Bullets, arrows |
| 7 | Interactable | NPCs, doors, chests |
| 8 | Items | Pickups, drops |

Simpler games use fewer layers. The key: name them in Project Settings > Layer Names.

---

## Asset Prompt Generation (ComfyUI)

### OpenDUI / OpenDiT (Text-to-Image)

For sprites, tiles, icons, VFX. Rules:
- Plain text + quality tags: `masterpiece, best quality, 4k` or `pixel art, 16x16`
- Emphasis: `(keyword:1.2)`
- One prompt per image. Include style, perspective, size.

### Flux Kontext (Image Edit / Style Transfer)

For recoloring, character consistency, pose variants:
- Describe what to change AND what to preserve
- `"same character, same style, [specific change]"`

### Chatterbox TTS (Text-to-Speech)

For dialogue, barks, narration:
- One script per file. Tags: `[laugh]`, `[sigh]`, `[gasp]`
- Emotion: 0.1-0.3 monotone, 1.0 neutral, 1.7+ expressive

### Organization

| Approach | When | Format |
|----------|------|--------|
| Per-asset | Specific/long prompts | `graphics/hero/prompt.txt` |
| Per-folder PROMPTS.md | Many related assets | Single file per folder |

Every prompt standalone — no "same as above".
