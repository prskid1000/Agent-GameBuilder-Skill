# GodewValley — Complete Step-by-Step Build Guide
# Rewritten from tutorial transcript · Matched to .example scripts

This guide walks you through building the complete GodewValley farming game from scratch,
phase by phase. Every section shows **what to do**, **why it works**, and **the exact code**
matching the `.example` project.

**Rule: After each phase, run the game (F5) and fix any errors before continuing. The project must never be left broken at the end of a step.**

---

## Phase 1 — Project Setup

### What you are building
A Godot 4 project with the correct window size, physics layers, input actions, autoloads, and
texture filter. Without these settings nothing else in the game will behave correctly.

### Step 1.1 — Window size
`Project → Project Settings → Display → Window`
- **Width:** 1920 — **Height:** 1080
- Alternatively 1280×720 if your monitor is smaller. Keep it 16:9.

### Step 1.2 — Default texture filter
`Project → Project Settings → Rendering → Textures → Default Texture Filter → Nearest`

Why: All art is pixel art. Nearest keeps edges crisp. Linear blurs them into mush.

### Step 1.3 — 2D Physics layers
`Project → Project Settings → 2D Physics → Layer Names`
```
Layer 1 = Terrain      (grass TileMap blocks movement)
Layer 2 = Player       (CharacterBody2D)
Layer 3 = Objects      (trees, plants, blobs, machines)
Layer 4 = Characters   (bed, TV — interactable by RayCast)
```

### Step 1.4 — Input Map
`Project → Project Settings → Input Map`

| Action | Keyboard | Controller |
|--------|----------|-----------|
| `left` | A / ← | D-Pad Left |
| `right` | D / → | D-Pad Right |
| `up` | W / ↑ | D-Pad Up |
| `down` | S / ↓ | D-Pad Down |
| `action` | Space | Button South (A/X) |
| `tool_forward` | E | Right Shoulder |
| `tool_backward` | Q | Left Shoulder |
| `seed_forward` | C | Button East (B) |
| `style_toggle` | (none) | Button West (Y/X) |
| `build` | M | Button North |
| `day_change` | Tab | (none — debug) |
| `diagnose` | N | (none) |

### Step 1.5 — Autoloads
`Project → Project Settings → Globals`
```
Enum  →  res://global/enums.gd   (autoload name: Enum)
Data  →  res://global/data.gd    (autoload name: Data)
```

### Step 1.6 — File structure to create
```
res://
├── audio/              (sound files)
├── global/
│   ├── enums.gd
│   └── data.gd
├── graphics/           (all art assets — do not create, copy from .example)
├── premade/            (copy from .example — HouseTileSet.tres, fisher.tres, code_snippets.txt)
├── resources/
│   └── plant_res.gd
├── scenes/
│   ├── characters/     player.tscn + player.gd
│   ├── levels/         level.tscn + level.gd, house.tscn, bed.tscn, tv.tscn
│   ├── machines/       machine.tscn, sprinkler, fisher, scare_crow, projectile
│   ├── objects/        plant, tree, simple_object, blob
│   ├── ui/             tool_ui, tool_ui_texture, fishing_game, plant_info, plant_info_container
│   └── vfx/            flash_sprite_2d
└── shaders/
    ├── flash.tres
    └── circle_transition.gdshader
```

**Verify:** Set a minimal main scene (e.g. empty Node2D or placeholder level) and run (F5). Project runs with no errors.

---

## Phase 2 — Global Scripts (enums.gd + data.gd)

### What you are building
Two autoload singletons. `enums.gd` gives the whole project named integer constants so states
can never be misspelled. `data.gd` is the game's data table — plant stats, animation names,
upgrade costs. All scripts read from these instead of hard-coding values.

### Step 2.1 — enums.gd
```gdscript
# global/enums.gd
# Autoloaded as "Enum". Access anywhere: Enum.Tool.AXE, Enum.Seed.CORN, etc.

enum Style  { BASIC, COWBOY, ENGLISH, BASEBALL, BEANIE, STRAW }
# Player hat skins. BASIC=0 (no hat), others unlock in shop.

enum State  { MOVE, FISH, BUILD, SHOP }
# Current player activity. Determines which input/collision logic runs.

enum Tool   { AXE, HOE, WATER, SWORD, FISH, SEED }
# AXE=0  HOE=1  WATER=2  SWORD=3  FISH=4  SEED=5
# posmod(current + direction, Enum.Tool.size()) cycles safely through all.

enum Machine { SPRINKLER, FISHER, SCARECROW, DELETE }
# Machines player can place. DELETE removes an existing machine.

enum Seed   { CORN, TOMATO, PUMPKIN, WHEAT }
# Seeds the player carries. Connected to PlantResource in data.gd.

enum Item   { WOOD, APPLE, FISH, CORN, WHEAT, PUMPKIN, TOMATO }
# Collectible items. Used in inventory dict and shop transactions.

enum Shop   { HAT, MACHINE }
# Which shop panel is open: hat shop or machine shop.
```

### Step 2.2 — data.gd (key sections)
```gdscript
# global/data.gd
# Autoloaded as "Data". Access anywhere: Data.PLANT_DATA[Enum.Seed.CORN]

const TILE_SIZE = 16
# Every TileMapLayer tile is 16×16 px. Used to convert pixel pos → grid coord.

const PLAYER_SKINS = {
    Enum.Style.BASIC:    preload("res://graphics/characters/main/main_basic.png"),
    Enum.Style.COWBOY:   preload("res://graphics/characters/main/main_cowboy.png"),
    Enum.Style.ENGLISH:  preload("res://graphics/characters/main/main_grey.png"),
    Enum.Style.BASEBALL: preload("res://graphics/characters/main/main_blue.png"),
    Enum.Style.BEANIE:   preload("res://graphics/characters/main/main_red.png"),
    Enum.Style.STRAW:    preload("res://graphics/characters/main/main_straw.png"),
}
# Player skin textures keyed by style enum.
# player.gd sets FlashSprite2D.texture = PLAYER_SKINS[current_style]

const PLANT_DATA = {
    Enum.Seed.CORN:    { "grow_speed": 1.0, "death_max": 40, "sell_amount": 4,  "texture": preload("res://graphics/plants/corn.png"),    "h_frames": 4, "name": "Corn",    "icon": preload("res://graphics/icons/corn.png")    },
    Enum.Seed.TOMATO:  { "grow_speed": 1.5, "death_max": 50, "sell_amount": 3,  "texture": preload("res://graphics/plants/tomato.png"),  "h_frames": 4, "name": "Tomato",  "icon": preload("res://graphics/icons/tomato.png")  },
    Enum.Seed.PUMPKIN: { "grow_speed": 0.5, "death_max": 70, "sell_amount": 6,  "texture": preload("res://graphics/plants/pumpkin.png"), "h_frames": 4, "name": "Pumpkin", "icon": preload("res://graphics/icons/pumpkin.png") },
    Enum.Seed.WHEAT:   { "grow_speed": 2.0, "death_max": 30, "sell_amount": 2,  "texture": preload("res://graphics/plants/wheat.png"),  "h_frames": 4, "name": "Wheat",   "icon": preload("res://graphics/icons/wheat.png")   },
}
# grow_speed MUST be float (1.0 not 1) — PlantResource.grow_speed is float.
# If you write 1 it becomes int=0 after assignment to a float property → plant never grows.

const TOOL_STATE_ANIMATIONS = {
    Enum.Tool.AXE:   "Axe",
    Enum.Tool.HOE:   "Hoe",
    Enum.Tool.WATER: "Water",
    Enum.Tool.SWORD: "Sword",
    Enum.Tool.FISH:  "Fish",
    Enum.Tool.SEED:  "Seed",
}
# Maps tool enum → name of the BlendSpace2D inside ToolStateMachine.
# Used in player.gd animate() to update all 6 blend positions in one loop.
# The key "Axe" matches the node name inside AnimationTree > ToolStateMachine.
```

**Verify:** Run project. No script parse errors; Enum and Data autoload. Fix any missing preload paths (use placeholder paths or create empty assets so the game runs).

---

## Phase 3 — Player Scene

### What you are building
A `CharacterBody2D` player that moves in 8 directions, plays the correct directional animation
via an AnimationTree, cycles through 6 tools, and emits signals when tools are used.

### Step 3.1 — Scene nodes
```
Player (CharacterBody2D)  [layer=2, mask=1]
  ├── CollisionShape2D     CapsuleShape2D  radius=6 height=12
  ├── FlashSprite2D        (instance of vfx/flash_sprite_2d.tscn)
  │     hframes=33  vframes=4
  ├── AnimationPlayer      (library of all animations)
  ├── AnimationTree        (tree_root=BlendTree, anim_player=AnimationPlayer)
  ├── Camera2D             zoom=(4,4)
  └── RayCast2D            target=(0,20), enabled=true, collision_mask=12
```

### Step 3.2 — AnimationTree wiring (editor steps)
This is the one part you must do in the Godot editor — it cannot be scripted.

**BlendTree root:**
```
MoveStateMachine ──→ ToolOneShot (in=MoveStateMachine, shot=ToolStateMachine) ──→ Output
```

**MoveStateMachine contains:**
- `Idle` BlendSpace2D with 9 points:
  ```
  (-1, 0)=idle_left   (0,-1)=idle_up    (1, 0)=idle_right
  (-1, 1)=idle_left   (0, 0)=idle_down  (1, 1)=idle_right
  (-1,-1)=idle_left   (0, 1)=idle_down  (1,-1)=idle_right
  ```
  Note: Y-axis is inverted in BlendSpace2D — down in GDO coords = positive Y = top of blend space.
- `Walk` BlendSpace2D — same 9-point layout but walk animations
- Transitions: Start→Idle (auto), Idle↔Walk (manual — gray arrows, not green)

**ToolStateMachine (premade in project, do not recreate):**  
Contains one BlendSpace2D per tool (Axe, Hoe, Water, Sword, Fish, Seed), each with 9 directional points.

**Starting blend positions (set in Inspector → AnimationTree → Parameters):**
- `MoveStateMachine/Idle/blend_position` = (0, 0)
- `MoveStateMachine/Walk/blend_position` = (0, 0)
- Every tool blend position inside ToolStateMachine = (0, 0)

### Step 3.3 — player.gd
```gdscript
# scenes/characters/player.gd

extends CharacterBody2D

# ─── Signals ──────────────────────────────────────────────────────────────────
signal tool_use(tool: Enum.Tool, position: Vector2)
# Emitted by the AnimationPlayer method track at the hit frame of each tool animation.
# level.gd connects this to handle world effects (hoe soil, water, spawn plant, hit tree...).

signal day_change
# Emitted when player interacts with the Bed. level.gd triggers day transition.

signal diagnose
# Emitted on N key. level.gd toggles plant_info_container visibility.

signal machine_change(machine: Enum.Machine)
# Emitted when player presses build hotkey. level.gd switches the preview sprite.

signal build(machine: Enum.Machine, position: Vector2)
# Emitted when player confirms machine placement. level.gd instantiates the scene.

# ─── State ────────────────────────────────────────────────────────────────────
const SPEED = 50.0

var direction      : Vector2      # current movement vector from input
var last_direction : Vector2      # last non-zero direction (for tool targeting)
var can_move       : bool = true  # false while a tool animation is playing

var current_tool   : Enum.Tool    # active tool — cycles with Q/E
var current_seed   : Enum.Seed    # active seed — cycles with C
var current_style  : Enum.Style   # current hat/skin
var current_state  : Enum.State = Enum.State.MOVE

# ─── Node refs ────────────────────────────────────────────────────────────────
@onready var animation_tree     = $AnimationTree
@onready var move_state_machine = animation_tree.get("parameters/MoveStateMachine/playback")
@onready var tool_state_machine = animation_tree.get("parameters/ToolStateMachine/playback")
@onready var flash_sprite       = $FlashSprite2D
@onready var ray_cast           = $RayCast2D

# ─── _ready ───────────────────────────────────────────────────────────────────
func _ready() -> void:
    animation_tree.active = true
    # Connect animation signals from AnimationTree (not AnimationPlayer).
    # AnimationPlayer signals are unreliable when an AnimationTree is controlling it.
    animation_tree.animation_started.connect(_on_animation_started)
    animation_tree.animation_finished.connect(_on_animation_finished)

# ─── _physics_process ────────────────────────────────────────────────────────
func _physics_process(_delta: float) -> void:
    if can_move:
        move()
    get_basic_input()

# ─── Movement ─────────────────────────────────────────────────────────────────
func move() -> void:
    direction = Input.get_vector("left", "right", "up", "down")
    # get_vector returns a Vector2 from -1 to 1 already normalised for diagonals.
    velocity = direction * SPEED
    move_and_slide()
    animate()

func animate() -> void:
    if direction:
        # Round direction so BlendSpace2D crosshair lands exactly on a defined point.
        # Without rounding, diagonal input gives a float like (0.7, 0.7) → no match.
        var dir_anim = Vector2(round(direction.x), round(direction.y))
        last_direction = dir_anim

        # Update both Idle and Walk blend positions so idle retains direction after stop.
        animation_tree.set("parameters/MoveStateMachine/Idle/blend_position", dir_anim)
        animation_tree.set("parameters/MoveStateMachine/Walk/blend_position", dir_anim)

        # Travel to walk state inside the state machine.
        move_state_machine.travel("Walk")

        # Update all 6 tool blend positions in one loop via TOOL_STATE_ANIMATIONS dict.
        for tool_anim in Data.TOOL_STATE_ANIMATIONS.values():
            var path = "parameters/ToolStateMachine/%s/blend_position" % tool_anim
            animation_tree.set(path, dir_anim)
    else:
        # No input → return to idle state (retains last direction from above).
        move_state_machine.travel("Idle")

# ─── Input ────────────────────────────────────────────────────────────────────
func get_basic_input() -> void:
    # ── Tool cycling (Q = backward, E = forward) ──
    if Input.is_action_just_pressed("tool_forward") or Input.is_action_just_pressed("tool_backward"):
        var dir = int(Input.get_axis("tool_backward", "tool_forward"))
        current_tool = posmod(current_tool + dir, Enum.Tool.size()) as Enum.Tool
        # posmod keeps the value in [0, size-1] even when subtracting past 0.

    # ── Seed cycling (C = forward only) ──
    if Input.is_action_just_pressed("seed_forward"):
        current_seed = posmod(current_seed + 1, Enum.Seed.size()) as Enum.Seed

    # ── Tool use (Space = use current tool) ──
    if Input.is_action_just_pressed("action"):
        # Travel to the right BlendSpace2D inside ToolStateMachine.
        tool_state_machine.travel(Data.TOOL_STATE_ANIMATIONS[current_tool])
        # Fire the OneShot: plays tool animation once, then returns to MoveStateMachine.
        animation_tree.set(
            "parameters/ToolOneShot/request",
            AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE
        )

    # ── Diagnose (N = toggle plant panel) ──
    if Input.is_action_just_pressed("diagnose"):
        diagnose.emit()

    # ── Build mode cycling ──
    if Input.is_action_just_pressed("build"):
        # machine_change signal handled by level.gd
        pass

# Called by AnimationPlayer method tracks at the exact hit frame of each tool animation.
# This is wired in the AnimationPlayer editor (not in GDScript).
func tool_use_emit() -> void:
    # Calculate the tile position the player is targeting, accounting for negative coordinates.
    var offset   = last_direction * Data.TILE_SIZE * 1.2
    var raw_pos  = global_position + offset
    var grid_x   = int(raw_pos.x / Data.TILE_SIZE)
    var grid_y   = int(raw_pos.y / Data.TILE_SIZE)
    # Fix: integer division truncates toward zero, not toward negative infinity.
    # -20 / 16 = -1 in GDScript (truncation), but the correct tile is at -2.
    if raw_pos.x < 0: grid_x -= 1
    if raw_pos.y < 0: grid_y -= 1
    tool_use.emit(current_tool, Vector2(grid_x, grid_y) * Data.TILE_SIZE + Vector2(8, 5))

# ─── Animation signals ────────────────────────────────────────────────────────
func _on_animation_started(_anim_name: StringName) -> void:
    can_move = false   # Freeze movement while tool swing plays.

func _on_animation_finished(_anim_name: StringName) -> void:
    can_move = true    # Restore movement after animation completes.
```

**Verify:** Run game with level containing Player. Player moves with WASD; tool cycling (Q/E) and action (Space) do not error. Fix missing node paths or AnimationTree parameter names before Phase 4.

---

## Phase 4 — Level Scene (TileMapLayers + level.gd)

### What you are building
The main game scene. Four `TileMapLayer` nodes for grass, water, soil, and watered soil.
A `level.gd` script that responds to player signals and modifies tiles at runtime.

### Step 4.1 — Grass layer (autotiling)
1. Add `TileMapLayer` → rename `GrassLayer`
2. Inspector → TileSet → New TileSet → drag `graphics/tilesets/grass.png` → Create Atlas
3. TileSet → Terrain Sets → Add Element → Mode: Match Corners and Sides → Terrains → Add: "Grass"
4. TileSet → Paint → Terrains → draw connections on all 47+ tile variants
5. Physics Layer → Add Element → Layer=1 (Terrain) → Mask=0
6. Paint collision polygons on edge tiles (L-shaped for corners, rectangles for straight edges)
7. In `TileMap → Terrains → Grass`, paint your island shape

**Key terrain tile rule:** Every tile must have ALL of its connecting sides defined.
If a corner tile is missing its connections, autotiling will break for complex shapes.

### Step 4.2 — Water layer (animated)
1. Add `TileMapLayer` → rename `WaterLayer` → z_index=-3
2. New TileSet → drag `water.png` → **Do NOT create Atlas** — click No
3. Select the leftmost tile → Animation tab → Columns=4 → Frames → Add 4 elements at 0.4s each
4. Paint water in the TileMap (only tile 0 is available — GDO auto-adds the animation frames)

### Step 4.3 — Soil layers
```
SoilLayer      z_index=-1   tile_set=soil.png (with terrain, NO physics layer)
SoilWaterLayer z_index=-1   tile_set=soil_water.png (3 variants of watered soil)
```
Terrain setup same as grass but simpler (no collision needed — plants sit on top of soil).

### Step 4.4 — level.gd

```gdscript
# scenes/levels/level.gd

extends Node2D

# ─── Preloads ─────────────────────────────────────────────────────────────────
const MACHINE_PREVIEW_TEXTURES = {
    Enum.Machine.SPRINKLER: {"texture": preload("res://graphics/icons/sprinkler.png"), "offset": Vector2i(0,  0)},
    Enum.Machine.FISHER:    {"texture": preload("res://graphics/icons/fisher.png"),    "offset": Vector2i(0, -4)},
    Enum.Machine.SCARECROW: {"texture": preload("res://graphics/icons/scarecrow.png"), "offset": Vector2i(0, -4)},
    Enum.Machine.DELETE:    {"texture": preload("res://graphics/icons/delete.png"),    "offset": Vector2i(0,  0)},
}

var machine_scenes = {
    Enum.Machine.SPRINKLER: preload("res://scenes/machines/sprinkler.tscn"),
    Enum.Machine.FISHER:    preload("res://scenes/machines/fisher.tscn"),
    Enum.Machine.SCARECROW: preload("res://scenes/machines/scare_crow.tscn"),
}

var plant_scene = preload("res://scenes/objects/plant.tscn")
var blob_scene  = preload("res://scenes/objects/blob.tscn")

# ─── State ────────────────────────────────────────────────────────────────────
var used_cells : Array[Vector2i] = []
# Tracks which soil tiles already have a plant. Prevents double-planting.

# ─── Node refs ────────────────────────────────────────────────────────────────
@onready var grass_layer        = $Layers/GrassLayer
@onready var soil_layer         = $Layers/SoilLayer
@onready var soil_water_layer   = $Layers/SoilWaterLayer
@onready var objects            = $Objects
@onready var player             = $Objects/Player
@onready var day_transition_mat = $Overlay/CanvasLayer/DayTransitionLayer.material
@onready var day_time_color     = $Overlay/DayTimeColor
@onready var plant_info_cont    = $Overlay/CanvasLayer/PlantInfoContainer
@onready var machine_preview    = $Overlay/MachinePreviewSprite
@onready var rain_particles     = $Overlay/RainDropsParticles
@onready var rain_floor         = $Layers/RainFloorParticles
@onready var day_timer          = $Timers/DayTimer
@onready var blob_timer         = $Timers/BlobTimer

# ─── Soil directions for sprinkler (8 neighbours) ─────────────────────────────
const SOIL_DIRECTIONS = [
    Vector2i(-1,-1), Vector2i(0,-1), Vector2i(1,-1),
    Vector2i(-1, 0),                 Vector2i(1, 0),
    Vector2i(-1, 1), Vector2i(0, 1), Vector2i(1, 1),
]

# ─── Day/Night gradient ───────────────────────────────────────────────────────
@onready var day_night_gradient = $Layers  # actually a Gradient sub-resource in level.tscn

# ─── _ready ───────────────────────────────────────────────────────────────────
func _ready() -> void:
    # Connect all player signals.
    player.tool_use.connect(_on_player_tool_use)
    player.day_change.connect(_on_player_day_change)
    player.diagnose.connect(_on_player_diagnose)
    player.machine_change.connect(_on_player_machine_change)
    player.build.connect(_on_player_build)

# ─── _process ─────────────────────────────────────────────────────────────────
func _process(_delta: float) -> void:
    # Sample day/night gradient → update CanvasModulate color every frame.
    var t    = 1.0 - (day_timer.time_left / day_timer.wait_time)
    var col  = $DayNightGradient.sample(t)   # Gradient sub-resource
    day_time_color.color = col

    # Move machine preview sprite to follow player when in BUILD state.
    if player.current_state == Enum.State.BUILD:
        var preview_data = MACHINE_PREVIEW_TEXTURES[player.current_machine]
        machine_preview.position = player.global_position + Vector2(preview_data["offset"])

# ─── Convert pixel position → grid coordinate ────────────────────────────────
func _pixel_to_grid(pixel_pos: Vector2) -> Vector2i:
    var gx = int(pixel_pos.x / Data.TILE_SIZE)
    var gy = int(pixel_pos.y / Data.TILE_SIZE)
    # GDScript int() truncates toward zero. Negative positions need -1 correction
    # because tile (-1,0) starts at pixel -16, not 0.
    if pixel_pos.x < 0: gx -= 1
    if pixel_pos.y < 0: gy -= 1
    return Vector2i(gx, gy)

# ─── Player signal handlers ───────────────────────────────────────────────────
func _on_player_tool_use(tool: Enum.Tool, pixel_pos: Vector2) -> void:
    var coord = _pixel_to_grid(pixel_pos)
    match tool:
        Enum.Tool.HOE:
            # Place a soil tile at the target coordinate using terrain autotiling.
            soil_layer.set_cells_terrain_connect(
                [coord],        # array of cells to add
                0,              # terrain_set index
                0,              # terrain index
                false           # do NOT ignore empty cells (keep existing terrain connections)
            )

        Enum.Tool.WATER:
            # Place one of 3 watered soil variants. Only if soil tile exists there.
            if soil_layer.get_cell_source_id(coord) != -1:
                soil_water_layer.set_cells_terrain_connect([coord], 0, 0, false)

        Enum.Tool.FISH:
            # Check if player is at the coast (grass tile has a coast_direction custom data).
            var coast = grass_layer.get_cell_tile_data(coord)
            if coast and coast.get_custom_data("coast_direction") != Vector2i(0, 0):
                player.start_fishing()

        Enum.Tool.SEED:
            # Plant only if soil exists and cell not already used.
            if soil_layer.get_cell_source_id(coord) != -1 and coord not in used_cells:
                _spawn_plant(coord)

        Enum.Tool.AXE, Enum.Tool.SWORD:
            # Check all objects in scene for proximity to the target position.
            for object in get_tree().get_nodes_in_group("Objects"):
                if object.position.distance_to(pixel_pos) < 20:
                    object.hit(tool)

func _on_player_day_change() -> void:
    _day_restart()

func _on_player_diagnose() -> void:
    plant_info_cont.visible = !plant_info_cont.visible

func _on_player_machine_change(machine: Enum.Machine) -> void:
    machine_preview.texture = MACHINE_PREVIEW_TEXTURES[machine]["texture"]
    machine_preview.visible = true

func _on_player_build(machine: Enum.Machine, pixel_pos: Vector2) -> void:
    if machine == Enum.Machine.DELETE:
        for m in get_tree().get_nodes_in_group("Machines"):
            if m.position.distance_to(pixel_pos) < 12:
                m.delete(_pixel_to_grid(pixel_pos))
        return
    var coord = _pixel_to_grid(pixel_pos)
    var new_machine = machine_scenes[machine].instantiate()
    new_machine.setup(coord, self, objects)
    objects.add_child(new_machine)

# ─── Plant spawning ───────────────────────────────────────────────────────────
func _spawn_plant(coord: Vector2i) -> void:
    var plant    = plant_scene.instantiate()
    var resource = PlantResource.new()
    var data     = Data.PLANT_DATA[player.current_seed]
    resource.texture     = data["texture"]
    resource.h_frames    = data["h_frames"]
    resource.grow_speed  = data["grow_speed"]   # float — must match grow_speed: float in plant_res.gd
    resource.death_max   = data["death_max"]
    resource.sell_amount = data["sell_amount"]
    resource.name        = data["name"]
    resource.icon        = data["icon"]
    resource.seed_enum   = player.current_seed

    used_cells.append(coord)
    plant.setup(coord, objects, plant_death)
    # plant_death (without parentheses) passes the function itself as a Callable.
    # Inside plant.gd, setup() connects the death signal to this Callable.
    plant_info_cont.add(resource)

func plant_death(coord: Vector2i) -> void:
    # Called from plant.gd via Callable when plant dies or is harvested.
    used_cells.erase(coord)

# ─── Day cycle ────────────────────────────────────────────────────────────────
func _day_restart() -> void:
    var tween = create_tween()
    # 1. Expand black circle to cover screen (progress 0 → 1)
    tween.tween_property(day_transition_mat, "shader_parameter/progress", 1.0, 1.0)
    # 2. Pause half a second while screen is black
    tween.tween_interval(0.5)
    # 3. Run level reset while screen is black
    tween.tween_callback(level_reset)
    # 4. Shrink circle to reveal new day (progress 1 → 0)
    tween.tween_property(day_transition_mat, "shader_parameter/progress", 0.0, 1.0)

func level_reset() -> void:
    day_timer.start()    # Restart the day timer.
    # Grow all plants (called day_change on each resource).
    for plant in get_tree().get_nodes_in_group("Plants"):
        plant.day_change()
    # Reset all trees (new apples if still alive).
    for obj in get_tree().get_nodes_in_group("Objects"):
        if "reset" in obj:  # duck-type check — only trees have reset()
            obj.reset()
    # If it's a rain day: show rain particles and rain floor splashes.
    # (rain logic not shown — toggle emitting on rain_particles / rain_floor)

func _on_blob_timer_timeout() -> void:
    # Spawn blob at random perimeter marker.
    var markers  = $BlobSpawnPositions.get_children()
    var marker   = markers[randi() % markers.size()]
    var blob     = blob_scene.instantiate()
    objects.add_child(blob)
    blob.global_position = marker.global_position
```

**Verify:** Run game. Level loads; player is present; tool_use (hoe/water/seed) and day cycle wiring don’t error. Add stub nodes (e.g. DayTransitionLayer, DayNightGradient) if referenced but not yet built so the scene runs.

---

## Phase 5 — Flash Shader + FlashSprite2D

### What you are building
A white-flash effect applied to any sprite. Used when trees, blobs, and plants are hit or collected.
The shader interpolates between the original pixel color and pure white based on a `Progress` uniform.

### Step 5.1 — flash.tres (VisualShader — editor only)
Create in Godot: `New Resource → VisualShader` → save as `shaders/flash.tres`

In the VisualShader editor, wire nodes:
```
Texture2D(UV) → Mix(a=texture_color, b=Color(1,1,1,1), weight=Progress_uniform) → Output
Alpha passthrough from Texture2D
```

Key properties:
- `Progress` uniform: hint_range(0.0, 1.0) — 0 = no flash, 1 = full white
- `Color` uniform: default=(1,1,1,1) — the flash target color (white)

**Critical:** In every scene that uses FlashSprite2D as a child instance, set  
`material → resource_local_to_scene = true`. Without this, ALL sprites share one material —
hitting one tree would flash every tree simultaneously.

### Step 5.2 — flash_sprite_2d.gd
```gdscript
# scenes/vfx/flash_sprite_2d.gd

extends Sprite2D

func flash(start: float, end: float, callback_func: Callable = Callable()) -> void:
    # start = initial Progress value when tween begins (e.g. 0.0)
    # end   = target Progress value (e.g. 1.0 = full white)
    # callback_func = optional function called after the flash — use to queue_free the parent

    var tween = create_tween()
    tween.tween_property(material, "shader_parameter/Progress", end, start)
    # Tween Progress from current → end over 'start' seconds.

    if callback_func.is_valid():
        # is_valid() returns false for the default Callable() — safe to skip if no callback.
        tween.tween_callback(callback_func)

    tween.tween_property(material, "shader_parameter/Progress", 0.0, end)
    # Return Progress to 0 (sprite returns to normal color) over 'end' seconds.
```

**Verify:** Run game. Hit a tree or blob; flash effect plays. No missing FlashSprite2D or shader parameter errors.

---

## Phase 6 — Plant System

### What you are building
A `StaticBody2D` plant that grows over multiple days, shows the correct stage sprite,
dies if not watered, and vanishes with a flash when collected. Data is stored in a
`PlantResource` so the plant info UI can observe changes.

### Step 6.1 — plant_res.gd
```gdscript
# resources/plant_res.gd

extends Resource
class_name PlantResource

# Export vars appear in Inspector when you open a .tres file.
@export var texture     : Texture2D         # growth stage spritesheet
@export var h_frames    : int       = 4     # number of horizontal frames (growth stages)
@export var grow_speed  : float     = 1.0   # stages grown per day (MUST be float)
@export var death_max   : int       = 50    # days without water before death
@export var sell_amount : int       = 3     # coins earned on harvest
@export var seed_enum   : Enum.Seed         # which seed type spawned this plant
@export var name        : String    = ""    # display name ("Tomato", "Corn"...)
@export var icon        : Texture2D         # small icon for UI panel

# Runtime state (not exported — not saved to .tres):
var age        : float = 0.0  # current growth progress (frame = floor(age))
var death_count: int   = 0    # days without water (resets on watering)
var watered    : bool  = false
var dead       : bool  = false :
    set(value):
        dead = value
        emit_changed()
        # emit_changed() fires the Resource.changed signal.
        # plant_info.gd connects .changed → queue_free to auto-remove the UI panel.

func grow() -> void:
    if watered:
        age += grow_speed
        watered = false
    else:
        death_count += 1
    if death_count >= death_max:
        dead = true
    emit_changed()   # Triggers plant_info.gd to update bars.

func water() -> void:
    watered = true
    death_count = 0
    emit_changed()

func get_frame() -> int:
    # Current visible growth stage (0 = seedling, h_frames-1 = mature).
    return mini(int(age), h_frames - 1)

func get_complete() -> bool:
    return age >= h_frames   # Plant is harvestable when age reaches total frames.
```

### Step 6.2 — plant.gd
```gdscript
# scenes/objects/plant.gd

extends StaticBody2D

var res          : PlantResource
var coordinate   : Vector2i

@onready var flash_sprite = $FlashSprite2D

signal death(coordinate: Vector2i)

func setup(grid_coord: Vector2i, parent: Node2D, death_callback: Callable) -> void:
    coordinate = grid_coord
    # Convert grid coordinate to pixel position (top-left of tile + centering offset).
    position = Vector2(grid_coord) * Data.TILE_SIZE + Vector2(8, 5)
    parent.add_child(self)
    death.connect(death_callback)
    # death_callback is plant_death() from level.gd, passed as a Callable.
    # When this plant dies, level.gd's used_cells array is updated.

func setup_resource(plant_resource: PlantResource) -> void:
    res = plant_resource
    flash_sprite.texture  = res.texture
    flash_sprite.hframes  = res.h_frames
    flash_sprite.position = Vector2(0, -9)   # Center sprite above the tile

func day_change() -> void:
    if res == null: return
    res.grow()
    flash_sprite.frame = res.get_frame()   # Update visible growth stage.
    if res.dead:
        _die()

func _die() -> void:
    death.emit(coordinate)
    queue_free()

func _on_collision_area_body_entered(_body: Node2D) -> void:
    # Player walked close enough to harvest.
    if res == null or not res.get_complete(): return
    flash_sprite.flash(0.2, 0.4, queue_free)
    # Pass queue_free as a Callable — plant disappears AFTER the flash finishes.
    # If you called queue_free() directly here the plant would vanish before the flash plays.
    death.emit(coordinate)
```

**Verify:** Run game. Hoe soil, plant seed, water; plant grows and shows in UI. Harvest when complete; plant flashes and is removed. No errors.

---

## Phase 7 — Tree + Simple Object

### Step 7.1 — tree.gd
```gdscript
# scenes/objects/tree.gd

extends StaticBody2D

const MAX_HEALTH = 3
var health : int = MAX_HEALTH :
    set(value):
        health = value
        if health <= 0:
            _die()

@onready var flash_sprite = $FlashSprite2D
@onready var stump        = $Stump
@onready var apples_node  = $Apples
@onready var spawn_points = $AppleSpawnPositions

func _ready() -> void:
    # Pick one of the 2 tree variants randomly.
    flash_sprite.frame = [0, 1].pick_random()
    create_apples()

func hit(tool: Enum.Tool) -> void:
    if tool != Enum.Tool.AXE: return
    flash_sprite.flash(0.1, 0.2)
    health -= 1

func _die() -> void:
    # Show stump, hide tree sprite, disable collision.
    stump.visible = true
    flash_sprite.visible = false
    $CollisionShape2D.set_deferred("disabled", true)

func reset() -> void:
    # Called by level.gd on new day. Regrow apples if tree is still alive.
    if health <= 0: return
    for apple in apples_node.get_children():
        apple.queue_free()
    create_apples()

func create_apples() -> void:
    var count = randi_range(0, 3)   # 0 to 3 apples per tree
    var positions = spawn_points.get_children().duplicate()
    positions.shuffle()
    for i in count:
        var apple = Sprite2D.new()
        apple.texture  = preload("res://graphics/plants/apple.png")
        apple.position = positions[i].position
        apples_node.add_child(apple)
        # duplicate(true) is used when you need a deep copy of an array with nodes.
        # Here shuffle() on positions gives random spawn points each time.
```

### Step 7.2 — simple_object.gd
```gdscript
# scenes/objects/simple_object.gd

@tool   # @tool runs this script in the EDITOR as well as at runtime.
# This gives us live preview: change 'size' in Inspector → sprite updates immediately.

extends StaticBody2D

@export var size  : int = 0 : set = _set_size   # 0-3: small to large
@export var style : int = 0 : set = _set_style  # 0=bush, 1=rock
@export var random: bool = true

@onready var sprite    = $Sprite2D
@onready var collision = $CollisionShape2D

func _ready() -> void:
    if random:
        size  = randi() % 4
        style = randi() % 2
    _update_sprite()

func _set_size(value: int) -> void:
    size = value
    _update_sprite()

func _set_style(value: int) -> void:
    style = value
    _update_sprite()

func _update_sprite() -> void:
    if not is_node_ready(): return
    sprite.frame_coords = Vector2i(size, style)
    collision.disabled  = size < 2   # Very small objects have no collision.
```

**Verify:** Run game. Axe hits tree (flash, health decreases); simple objects display. No errors.

---

## Phase 8 — Blob Enemy

### What you are building
A `CharacterBody2D` enemy that moves toward the player, flashes when hit, gets pushed back by
the sword, and explodes with a frame-by-frame animation before disappearing.

### Step 8.1 — blob.gd
```gdscript
# scenes/objects/blob.gd

extends CharacterBody2D

const SPEED         = 20.0
const PUSH_DISTANCE = 130.0
const MAX_HEALTH    = 3

var health : int = MAX_HEALTH :
    set(value):
        health = value
        if health <= 0: _die()

var push_direction : Vector2 = Vector2.ZERO
# Added to velocity every frame. The sword push tween modifies this over 0.3s.

@onready var flash_sprite    = $FlashSprite2D
@onready var animation_player = $AnimationPlayer

func _physics_process(_delta: float) -> void:
    if speed == 0: return
    var target = get_tree().get_nodes_in_group("Player")
    if target.is_empty(): return
    var direction = (target[0].global_position - global_position).normalized()
    velocity = direction * SPEED + push_direction
    move_and_slide()

func hit(tool: Enum.Tool) -> void:
    if tool == Enum.Tool.SWORD:
        flash_sprite.flash(0.1, 0.2)
        health -= 1
        push(flash_sprite.global_position - get_tree().get_nodes_in_group("Player")[0].global_position)

func push(from_pos: Vector2) -> void:
    # Tween push_direction from target→zero so the push fades naturally.
    var target = (global_position - from_pos).normalized() * PUSH_DISTANCE
    var tween  = create_tween()
    tween.tween_property(self, "push_direction", target, 0.1)
    tween.tween_property(self, "push_direction", Vector2.ZERO, 0.2)

func _die() -> void:
    SPEED = 0              # Stop movement immediately.
    velocity = Vector2.ZERO
    animation_player.play("explode")
    # "explode" animation plays frames 7–13 of blob.png, then calls queue_free
    # via a method track at t=1.4s (set up in the AnimationPlayer editor).
```

**Verify:** Run game. Blobs spawn and chase player; sword hits push and damage; death plays explode animation. Fix blob.gd: `speed` is const — use a variable if you need to set SPEED = 0 in _die(). No errors.

---

## Phase 9 — Circle Transition Shader

### What you are building
A full-screen `ColorRect` with a GLSL shader that cuts a circular hole in it.
Tweening the hole from tiny→large reveals the new day; large→tiny hides it.

### Step 9.1 — circle_transition.gdshader
```glsl
// shaders/circle_transition.gdshader

shader_type canvas_item;

uniform float progress : hint_range(0.0, 1.0) = 0.0;
// 0.0 = tiny hole (screen mostly black), 1.0 = huge hole (screen fully visible)

void fragment() {
    // Correct the UV for non-square viewports (16:9 makes an oval, not a circle).
    float ratio        = SCREEN_PIXEL_SIZE.y / SCREEN_PIXEL_SIZE.x;
    vec2  adjusted_uv  = vec2(mix(0.5, UV.x, ratio), UV.y);
    // mix(0.5, UV.x, ratio) squeezes X toward center proportionally to the aspect ratio.

    // Distance from this pixel to the center of the screen.
    float circle = distance(vec2(0.5), adjusted_uv);

    // step(edge, value): returns 0 if value < edge, else 1.
    // progress * 1.5: multiply so 1.0 progress fully clears the corners (1.5 reaches them).
    // 1.5 - (progress * 1.5): invert so progress=0 → full black, progress=1 → full clear.
    float alpha = step(circle, 1.5 - (progress * 1.5));

    COLOR.a = alpha;
    // The ColorRect is a very dark gray. Alpha=1 shows it (black). Alpha=0 hides it (day visible).
}
```

**Verify:** Run game. Trigger day change (e.g. bed); circle wipe plays and level resets. No shader compile errors.

---

## Phase 10 — Tool UI

### What you are building
A floating row of tool icons above the player. Selecting a tool highlights its icon.
The row auto-hides after 1 second of inactivity.

### Step 10.1 — tool_ui.gd
```gdscript
# scenes/ui/tool_ui.gd

extends Control

const TOOL_TEXTURES = {
    Enum.Tool.AXE:   preload("res://graphics/icons/axe.png"),
    Enum.Tool.HOE:   preload("res://graphics/icons/hoe.png"),
    Enum.Tool.WATER: preload("res://graphics/icons/water.png"),
    Enum.Tool.SWORD: preload("res://graphics/icons/sword.png"),
    Enum.Tool.FISH:  preload("res://graphics/icons/fish.png"),
    Enum.Tool.SEED:  preload("res://graphics/icons/wheat.png"),
}
const SEED_TEXTURES = {
    Enum.Seed.CORN:    preload("res://graphics/icons/corn.png"),
    Enum.Seed.PUMPKIN: preload("res://graphics/icons/pumpkin.png"),
    Enum.Seed.TOMATO:  preload("res://graphics/icons/tomato.png"),
    Enum.Seed.WHEAT:   preload("res://graphics/icons/wheat.png"),
}

var tool_texture_scene = preload("res://scenes/ui/tool_ui_texture.tscn")
var tool_textures_list : Array = []
var seed_textures_list : Array = []

@onready var tool_container = $ToolContainer
@onready var seed_container = $SeedContainer
@onready var hide_timer     = $HideTimer

func _ready() -> void:
    _build_row(Enum.Tool.values(), TOOL_TEXTURES, tool_container, tool_textures_list)
    _build_row(Enum.Seed.values(), SEED_TEXTURES, seed_container, seed_textures_list)
    tool_container.visible = false
    seed_container.visible = false

func _build_row(enum_list: Array, textures: Dictionary, container: HBoxContainer, list: Array) -> void:
    for enum_id in enum_list:
        var icon = tool_texture_scene.instantiate()
        container.add_child(icon)
        icon.setup(enum_id, textures[enum_id])
        list.append(icon)

func reveal(is_seed: bool) -> void:
    # Show the correct row and restart the auto-hide timer.
    tool_container.visible = !is_seed
    seed_container.visible = is_seed
    hide_timer.start()

func highlight(enum_value: int, is_seed: bool) -> void:
    var list = seed_textures_list if is_seed else tool_textures_list
    for icon in list:
        icon.highlight(icon.enum_id == enum_value)

func _on_hide_timer_timeout() -> void:
    tool_container.visible = false
    seed_container.visible = false
```

### Step 10.2 — tool_ui_texture.gd
```gdscript
# scenes/ui/tool_ui_texture.gd

extends Control

var enum_id : int   # Which tool/seed this icon represents.

@onready var texture_rect = $TextureRect

func setup(id: int, tex: Texture2D) -> void:
    enum_id           = id
    texture_rect.texture = tex

func highlight(is_selected: bool) -> void:
    # Tween icon size: selected = 20×20 (fills container), unselected = 16×16.
    var target = Vector2(20, 20) if is_selected else Vector2(16, 16)
    var tween  = create_tween()
    tween.tween_property(texture_rect, "custom_minimum_size", target, 0.1)
```

**Verify:** Run game. Tool/seed bar shows and highlights on change; auto-hide works. No missing texture or scene errors.

---

## Phase 11 — Plant Info UI

### What you are building
A scrollable left-sidebar panel. Each active plant gets a card showing its icon, name,
green growth bar, and red death bar. Cards auto-remove when the plant dies.

### Step 11.1 — plant_info.gd
```gdscript
# scenes/ui/plant_info.gd

extends PanelContainer

var res : PlantResource

@onready var icon_texture = $HBoxContainer/IconTexture
@onready var name_label   = $HBoxContainer/VBoxContainer/NameLabel
@onready var growth_bar   = $HBoxContainer/VBoxContainer/GrowthBar
@onready var death_bar    = $HBoxContainer/VBoxContainer/DeathBar

func setup(plant_resource: PlantResource) -> void:
    res = plant_resource
    icon_texture.texture = res.icon
    name_label.text      = res.name
    growth_bar.max_value = res.h_frames
    death_bar.max_value  = res.death_max
    # Connect the Resource.changed signal → update bars every time grow() or water() is called.
    res.changed.connect(update)
    # Also connect changed → queue_free so the card disappears when the plant dies.
    res.changed.connect(func():
        if res.dead: queue_free()
    )
    update()

func update() -> void:
    # Always set max_value BEFORE value — setting value first on a new bar can clip it.
    growth_bar.max_value  = res.h_frames
    growth_bar.value      = res.age
    death_bar.max_value   = res.death_max
    death_bar.value       = res.death_count
```

### Step 11.2 — plant_info_container.gd
```gdscript
# scenes/ui/plant_info_container.gd

extends Control

@onready var vbox = $MarginContainer/ScrollContainer/VBoxContainer

func add(plant_resource: PlantResource) -> void:
    var panel = preload("res://scenes/ui/plant_info.tscn").instantiate()
    vbox.add_child(panel)
    panel.setup(plant_resource)
```

**Verify:** Run game. Plant a crop; plant info panel appears and updates on grow/water; panel removes when plant dies. No errors.

---

## Phase 12 — Day/Night Cycle

### What you are building
A `CanvasModulate` node whose color is sampled from a `Gradient` resource every frame.
Dawn is pinkish, midday is white, night is dark blue.

### Step 12.1 — Gradient sub-resource in level.tscn
Create a `Gradient` resource on the `Level` node (or as a sub-resource).
Four colour stops:
```
t=0.00 → Color(0.93, 0.86, 0.82)  dawn pinkish
t=0.30 → Color(1.00, 1.00, 1.00)  full daylight
t=0.48 → Color(1.00, 1.00, 1.00)  midday
t=1.00 → Color(0.37, 0.47, 1.00)  blue midnight
```

### Step 12.2 — Sampling in level.gd _process()
```gdscript
func _process(_delta: float) -> void:
    # Normalise timer → 0..1 range going forward in time.
    # day_timer counts DOWN from wait_time to 0.
    # 1.0 - (time_left / wait_time) gives 0 at day start, 1 at midnight.
    var t = 1.0 - (day_timer.time_left / day_timer.wait_time)
    day_time_color.color = day_night_gradient.sample(t)
    # gradient.sample(float) gives fine interpolation between stops.
    # gradient.get_color(int) only returns the discrete stop colors.
```

**Verify:** Run game. Day/night color shifts over time; sleeping triggers full day transition and level_reset. No errors.

---

## Phase 13 — Performance Monitoring

### How to check game performance
Run the game → Godot Editor → Debugger tab (bottom panel) → Monitors

**Key metrics:**
| Metric | What it means | Healthy value |
|--------|---------------|---------------|
| FPS | Frames drawn per second | ≥ 60 (disable V-Sync to see true FPS) |
| Process time | ms per _process() call | < 5ms |
| Physics process | ms per _physics_process() call | < 5ms |
| Static memory | CPU RAM used by game | < 500 MB |
| Video memory | GPU VRAM | < 512 MB for mobile, 1 GB desktop |

**V-Sync note:**  
`Project Settings → Display → V-Sync` is enabled by default. This caps FPS to your monitor
refresh rate (60 or 30). Disable it during development to see the true frame budget.

**What to watch for:**
- FPS drops below 30 → something is doing too much work per frame
- Memory climbing steadily → objects or textures are being created but never freed
  (common cause: spawning nodes in `_process()` without `queue_free()`)
- Video memory stable → GPU textures are fine even if CPU memory leaks

**Common mistakes:**
```gdscript
# BAD — creates a new Sprite2D and loads a texture 2000 times per second
func _process(_delta):
    var s = Sprite2D.new()
    s.texture = load("res://graphics/tilesets/grass.png")
    add_child(s)

# GOOD — preload once, instantiate rarely
var grass_tex = preload("res://graphics/tilesets/grass.png")
```

---

## Quick Summary — Build Order

```
1.  Project setup (settings, layers, input map, autoloads)
2.  enums.gd + data.gd  (global singletons)
3.  flash_sprite_2d.tscn + flash.tres  (shader + script)
4.  player.tscn  (nodes + camera)
5.  AnimationTree  (EDITOR ONLY — BlendTree/StateMachine/BlendSpace2D)
6.  player.gd  (movement + tool cycling + signals)
7.  level.tscn  (TileMapLayers — grass terrain + water animation + soil)
8.  level.gd  (pixel→grid conversion, tool_use handler, day cycle)
9.  simple_object.tscn + simple_object.gd  (@tool, random size/style)
10. tree.tscn + tree.gd  (hit, flash, apples, reset on new day)
11. blob.tscn + blob.gd  (movement, push tween, explode animation)
12. plant_res.gd  (PlantResource class, emit_changed)
13. plant.tscn + plant.gd  (setup, day_change, harvest via Callable)
14. tool_ui.tscn + tool_ui_texture.tscn  (floating icon bar)
15. plant_info.tscn + plant_info_container.tscn  (sidebar panels)
16. circle_transition.gdshader  (day transition effect)
17. machine scenes (machine → sprinkler → fisher → scarecrow → projectile)
18. house.tscn + bed.tscn + tv.tscn  (interior, sleep, weather forecast)
19. Level layout  (place trees, objects, house, scarecrow, blob spawn points)
20. Performance check  (FPS monitor, memory monitor)
```

**Verify (final):** Full playthrough: move, farm, fish, fight blobs, sleep, use machines. All features work; no runtime or missing-asset errors. Fix any remaining issues before considering the build complete.
