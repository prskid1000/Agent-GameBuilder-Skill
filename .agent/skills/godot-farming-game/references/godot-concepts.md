# Godot 4 Concepts Used in This Game

This reference explains every advanced Godot concept used in the project,
with the exact patterns from the `.example` codebase.

---

## 1. AnimationTree

**What:** Controls an AnimationPlayer using a node graph instead of direct script calls.
Handles complex animation logic (blending, state switching, one-shots) with minimal code.

**Three node types used:**

### BlendTree (root)
The root container. Connects sub-nodes together and feeds the final animation to Output.

### AnimationNodeStateMachine
Moves between named states (animations or BlendSpaces). Used for MoveStateMachine and ToolStateMachine.

```
Start → Idle (auto)
Idle ↔ Walk (non-auto, both directions — gray arrows)
```

Travel between states from GDScript:
```gdscript
@onready var move_state_machine = $Animation/AnimationTree.get("parameters/MoveStateMachine/playback")
move_state_machine.travel('Walk')   # switch to Walk
move_state_machine.travel('Idle')   # switch to Idle
```

### BlendSpace2D
Selects an animation based on a 2D position (the blend position). Used for directional animations.

**Points layout (all BlendSpaces in this game):**
```
(-1,-1)  (0,-1)  (1,-1)     ← top row (UP direction = y=-1)
(-1, 0)  (0, 0)  (1, 0)     ← middle row
(-1, 1)  (0, 1)  (1, 1)     ← bottom row (DOWN direction = y=+1)
```

Set blend position from script:
```gdscript
var direction_animation = Vector2(round(direction.x), round(direction.y))
$Animation/AnimationTree.set("parameters/MoveStateMachine/Walk/blend_position", direction_animation)
```

**Critical:** The crosshair must sit on an EXACT point, not between points. Always `round()` the direction vector.

### AnimationNodeOneShot (ToolOneShot)
Plays a "shot" animation once then returns to the continuous "in" animation.

```gdscript
# Fire the one-shot (plays tool animation once)
$Animation/AnimationTree.set("parameters/ToolOneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)
```

### How to get animation parameter paths
Hover over any parameter in the AnimationTree inspector tab — Godot shows the full path string.

---

## 2. TileMapLayer (Terrain Autotiling)

**What:** Places tiles automatically based on neighbor connections. Replaces manual tile placement.

### Setup steps:
1. TileSet → Terrain Sets → Add Element → set mode (Match Corners & Sides for most cases)
2. Inside terrain set → Add terrain element → give it a name/color
3. TileSet → Paint tab → select Terrains → paint which tiles belong to which terrain
4. Draw terrain connections (the 9-point grid showing where neighbors connect)

### Dynamic placement from script:
```gdscript
# Place terrain tile(s) at grid position
$Layers/SoilLayer.set_cells_terrain_connect([grid_coord], 0, 0)
# Args: array of Vector2i, terrain_set index, terrain index

# Place a single non-terrain tile (e.g. water patch)
$Layers/SoilWaterLayer.set_cell(grid_coord, 0, Vector2i(randi_range(0,2), 0))
# Args: coord, source_id, atlas_coords

# Query tiles
var used = $Layers/GrassLayer.get_used_cells()         # all occupied cells
var data = $Layers/GrassLayer.get_cell_tile_data(coord) # returns TileData or null
var custom = data.get_custom_data('farmable')           # read custom data layer value
```

### Custom Data Layers
Add under TileSet → Custom Data Layers. Then paint values per-tile in the Paint tab.
Used to mark tiles as `farmable` (bool) or `coast` (Vector2i direction) for game logic.

### Coordinate conversion (pixel ↔ grid)
```gdscript
# Pixel position to grid coord (handles negative coords correctly)
var grid_coord = Vector2i(int(pos.x / Data.TILE_SIZE), int(pos.y / Data.TILE_SIZE))
grid_coord.x += -1 if pos.x < 0 else 0   # IMPORTANT: fix negative side
grid_coord.y += -1 if pos.y < 0 else 0
```

---

## 3. Resources (Custom)

**What:** Data containers — scripts without nodes. Share data between multiple scenes.

### Create a custom resource:
```gdscript
# plant_res.gd
class_name PlantResource extends Resource

@export var texture: Texture2D
@export var grow_speed: float = 1.0
var age: float                       # runtime, not exported
```

### Instantiate and populate at runtime:
```gdscript
var plant_res = PlantResource.new()
plant_res.setup(current_seed)        # fills from Data.PLANT_DATA dict
```

### Pass to multiple nodes (key benefit):
```gdscript
# Same resource object used in both the plant scene AND the plant_info panel
plant.setup(grid_coord, $Objects, plant_res, plant_death)
plant_info.setup(plant_res)          # same object → shared state
```

### `emit_changed()` — broadcast updates
Called inside setters to notify all connected scenes:
```gdscript
var death_count: int:
    set(value):
        death_count = value
        emit_changed()   # triggers "changed" signal on resource
```

Connect from another node:
```gdscript
res.connect("changed", update)       # update() called whenever any setter fires emit_changed()
```

---

## 4. `@tool` — Editor Tools

**What:** Adding `@tool` at the top of a script makes it run in the Godot editor (not just at runtime).
Used for live preview of randomized objects.

```gdscript
@tool
extends StaticBody2D

@export_range(0, 3, 1) var size: int:
    set(value):
        size = value
        $Sprite2D.frame_coords = Vector2i(size, style)  # updates in editor live
```

**Export tool button** — adds a clickable button in the Inspector:
```gdscript
@export_tool_button('Randomize', "Callable") var randomizer = randomize_func

func randomize_func():
    size = randi_range(0, 3)
    style = [0, 1].pick_random()
```

**Caution:** After editing `@tool` scripts, use right-click → Soft Reload Tool Script, or close/reopen the scene.

---

## 5. Signals and Callables

### Defining signals:
```gdscript
signal tool_use(tool: Enum.Tool, pos: Vector2)
signal death(coord: Vector2i)
```

### Emitting:
```gdscript
tool_use.emit(current_tool, position + last_direction * 16 + Vector2(0, 4))
```

### Connecting in code:
```gdscript
player.tool_use.connect(_on_player_tool_use)
```

### Passing functions as Callables (advanced pattern):
```gdscript
# In level.gd: pass a function reference into plant setup
plant.setup(grid_coord, $Objects, plant_res, plant_death)

# In plant.gd setup:
func setup(grid_coord, parent, new_res, plant_death_func):
    death.connect(plant_death_func)   # signal target is a Callable from outside
```

### Default Callable (for optional callback):
```gdscript
func flash(start_duration = 0.2, end_duration = 0.2, callback_func: Callable = Callable()):
    var tween = create_tween()
    tween.tween_property(material, 'shader_parameter/Progress', 1.0, start_duration)
    if callback_func.is_valid():
        tween.tween_callback(callback_func)
    tween.tween_property(material, 'shader_parameter/Progress', 0.0, end_duration)
```

---

## 6. Enums

**What:** Named integer constants. Prevent typos, enable IDE autocomplete, work with `match`.

```gdscript
# In enums.gd (autoload "Enum")
enum Tool { AXE, HOE, SWORD, WATER, FISH, SEED }

# Usage
var current_tool: Enum.Tool = Enum.Tool.AXE

# Cycle with wrap (posmod prevents going out of bounds)
current_tool = posmod(current_tool + int(dir), Enum.Tool.size()) as Enum.Tool

# match statement
match current_tool:
    Enum.Tool.HOE:   create_soil()
    Enum.Tool.WATER: water_soil()
```

---

## 7. Tweens (Code-Based Animation)

**What:** Animate any property over time without AnimationPlayer. Used for flash, day transition, push effects.

```gdscript
# Simple property tween
var tween = create_tween()
tween.tween_property(material, "shader_parameter/Progress", 1.0, 0.2)  # target, property, value, duration
tween.tween_property(material, "shader_parameter/Progress", 0.0, 0.2)  # runs after first completes

# With pause between
tween.tween_interval(0.5)

# Callback in sequence
tween.tween_callback(level_reset)

# Animate on a child node
tween.tween_property(self, "push_direction", target_dir * -push_distance, 0.1)
tween.tween_property(self, "push_direction", Vector2.ZERO, 0.2)
```

---

## 8. Y-Sort

**What:** Nodes with Y-Sort enabled automatically draw children back-to-front based on their Y position.
Players/objects further down screen appear in front of objects further up.

```
Objects/ Node2D  → Ordering → Y Sort Enabled = true
```

All objects under this node are automatically sorted. No extra code needed.

---

## 9. VisualShader (Flash Effect)

**What:** Node-graph shader editor for visual effects. Used for the flash-white effect on hit.

**Flash shader logic:**
```
Original color ──┐
                  ├── Mix (weight=Progress) ── Fragment output color
White color ─────┘
```

`Progress=0` → original color, `Progress=1` → fully white.

Animate via tween:
```gdscript
tween.tween_property(material, 'shader_parameter/Progress', 1.0, 0.2)
tween.tween_property(material, 'shader_parameter/Progress', 0.0, 0.2)
```

**`local_to_scene = true` is MANDATORY** on the ShaderMaterial — otherwise all instances share the same shader state.

---

## 10. Code Shader (Circle Transition)

**What:** GLSL fragment shader that creates a circle wipe transition.

```glsl
uniform float progress : hint_range(0.0, 1.0);

void fragment() {
    float ratio = SCREEN_PIXEL_SIZE.y / SCREEN_PIXEL_SIZE.x;
    vec2 adjusted_uv = vec2(mix(0.5, UV.x, ratio), UV.y);
    float circle = distance(vec2(0.5), adjusted_uv);
    float alpha = step(circle, 1.5 - progress * 1.5);
    COLOR.a = alpha;
}
```

- `progress=0` → fully visible (no wipe)
- `progress=1` → fully black (circle covers screen)
- `ratio` correction fixes the oval-vs-circle distortion on non-square viewports

---

## 11. Gradients for Day/Night

```gdscript
@export var daytime_color: Gradient   # set in Inspector with 4 color stops

func _process(_delta):
    var point = 1 - ($Timers/DayTimer.time_left / $Timers/DayTimer.wait_time)
    var color = daytime_color.sample(point)   # sample() gives smooth interpolation
    $Overlay/DayTimeColor.color = color
```

`Gradient.sample(t)` where `t` is 0.0–1.0 → returns interpolated Color between stops.
`Gradient.get_color(i)` gets a specific stop by index (not used here).

---

## 12. Groups

**What:** Tag nodes for bulk operations. Get all nodes in a group from anywhere.

```gdscript
# Tag a node (in the Node panel or in script)
# In Node panel: Groups tab → add "Objects"

# Get all tagged nodes
for object in get_tree().get_nodes_in_group('Objects'):
    object.hit(tool)

for plant in get_tree().get_nodes_in_group('Plants'):
    plant.grow(watered)

# Get first node in group
@onready var player = get_tree().get_first_node_in_group('Player')
```

**Groups used in this project:**
- `"Player"` — the player CharacterBody2D
- `"Objects"` — trees, blobs, simple_objects (can be hit)
- `"Plants"` — plant StaticBody2Ds (grown each day)
- `"Machines"` — sprinkler, fisher, scarecrow, etc.
- `"Blobs"` — blob enemies (targeted by projectiles)

---

## 13. Property Setters (`set`)

**What:** Run code whenever a variable changes. Useful for health, visibility flags, raining state.

```gdscript
var health := 3:
    set(value):
        health = value           # MUST update self first
        if health <= 0:
            death()              # auto-called whenever health changes to ≤0

var raining: bool:
    set(value):
        raining = value
        $Layers/RainFloorParticles.emitting = value
        $Overlay/RainDropsParticles.emitting = value
```

---

## 14. RayCast2D for Interaction

**What:** Casts a ray from the player in their facing direction. Detects interactable objects.

```gdscript
# In _physics_process:
var ray_y = int(direction.y) if not direction.x else 0
$RayCast2D.target_position = Vector2(direction.x, ray_y).normalized() * 20

# In get_basic_input:
if Input.is_action_just_pressed("action"):
    if not $RayCast2D.get_collider():
        # use tool
    else:
        $RayCast2D.get_collider().interact(self)  # interact with object in front
```

Objects that can be interacted with implement `func interact(player)`.

---

## 15. Performance Monitoring

Open debugger → Monitors tab while game is running. Key metrics:

| Metric | What it means | Target |
|--------|--------------|--------|
| FPS | Frames per second | ≥60 (30 minimum) |
| Process time | _process duration in ms | Lower = better |
| Physics process | _physics_process duration | Lower = better |
| Video RAM | GPU memory used | Watch for spikes |
| Object count | Nodes in scene tree | Watch for leaks |

**V-Sync:** Project Settings → Display → Window → V-Sync. On = capped to monitor refresh. Off = uncapped (shows true FPS).
