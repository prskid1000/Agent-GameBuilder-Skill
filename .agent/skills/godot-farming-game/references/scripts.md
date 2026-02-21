# All Scripts — Line-by-Line Commented Reference

Every script from the `.example` project, with a comment on every meaningful line.
Read together with `screen-by-screen.md` to understand what drives what visually.

---

## global/enums.gd
> **Purpose:** Defines every named state in the game. Autoloaded as `Enum` so any script can use `Enum.Tool.AXE` etc.
> **Screen:** Not visible — purely a data definition file.

```gdscript
extends Node   # Makes this a singleton node (autoloaded in project.godot)

# Player costume / hat styles the user can switch between with T key
enum Style { BASIC, COWBOY, ENGLISH, BASEBALL, BEANIE, STRAW }

# What the player is currently doing — controls which input branch runs in _physics_process
enum State { DEFAULT, FISHING, BUILDING, SHOP }

# The 6 holdable tools cycled with Q/E keys
# Order matters: AXE=0, HOE=1, SWORD=2, WATER=3, FISH=4, SEED=5
enum Tool { AXE, HOE, SWORD, WATER, FISH, SEED }

# The 4 placeable machines cycled in BUILD mode; DELETE removes an existing machine
enum Machine { SPRINKLER, FISHER, SCARECROW, DELETE }

# The 4 seed types cycled with C key; each grows a different plant
enum Seed { TOMATO, CORN, PUMPKIN, WHEAT }

# Collectible items that go into the player's inventory
enum Item { WOOD, APPLE, TOMATO, CORN, WHEAT, PUMPKIN, FISH }

# Which shop panel is open (for future shop scenes)
enum Shop { MAIN, HAT }
```

---

## global/data.gd
> **Purpose:** Central data store — all textures, costs, and lookup tables in one place.
> **Screen:** Not visible — but every texture you SEE on screen is referenced here.

```gdscript
extends Node   # Autoloaded as "Data" — accessible everywhere as Data.TILE_SIZE etc.

# --- PLAYER SKINS ---
# Dictionary: Enum.Style → Texture2D
# preload() loads the PNG at startup so there is no runtime delay when swapping skins
const PLAYER_SKINS = {
    Enum.Style.BASIC:    preload("res://graphics/characters/main/main_basic.png"),
    Enum.Style.BASEBALL: preload("res://graphics/characters/main/main_blue.png"),
    Enum.Style.COWBOY:   preload("res://graphics/characters/main/main_cowboy.png"),
    Enum.Style.ENGLISH:  preload("res://graphics/characters/main/main_grey.png"),
    Enum.Style.STRAW:    preload("res://graphics/characters/main/main_straw.png"),
    Enum.Style.BEANIE:   preload("res://graphics/characters/main/main_red.png"),
}

# Every TileMap in the game uses 16×16 pixel tiles — one constant prevents magic numbers everywhere
const TILE_SIZE = 16

# --- PLANT DATA ---
# Dictionary: Enum.Seed → dict of properties for that plant type
# 'texture'      = the growth-stage sprite sheet (3 frames: seedling → growing → mature)
# 'icon_texture' = small icon shown in tool UI and plant info panel
# 'name'         = display name shown in plant info panel
# 'h_frames'     = how many horizontal frames the sprite sheet has (always 3 here)
# 'grow_speed'   = how much "age" is added per watered day (float! 0.3 = slow, 1.0 = fast)
# 'death_max'    = how many consecutive un-watered days before the plant dies
# 'reward'       = the Enum.Item the player receives when they harvest it
const PLANT_DATA = {
    Enum.Seed.TOMATO: {
        'texture':      "res://graphics/plants/tomato.png",
        'icon_texture': "res://graphics/icons/tomato.png",
        'name':         'Tomato',
        'h_frames':     3,
        'grow_speed':   0.6,   # medium speed
        'death_max':    3,     # tolerates 3 dry days
        'reward':       Enum.Item.TOMATO,
    },
    Enum.Seed.CORN: {
        'texture':      "res://graphics/plants/corn.png",
        'icon_texture': "res://graphics/icons/corn.png",
        'name':         'Corn',
        'h_frames':     3,
        'grow_speed':   1.0,   # fastest growth
        'death_max':    2,     # dies after only 2 dry days — high maintenance
        'reward':       Enum.Item.CORN,
    },
    Enum.Seed.PUMPKIN: {
        'texture':      "res://graphics/plants/pumpkin.png",
        'icon_texture': "res://graphics/icons/pumpkin.png",
        'name':         'Pumpkin',
        'h_frames':     3,
        'grow_speed':   0.3,   # slowest growth — takes many days
        'death_max':    3,
        'reward':       Enum.Item.PUMPKIN,
    },
    Enum.Seed.WHEAT: {
        'texture':      "res://graphics/plants/wheat.png",
        'icon_texture': "res://graphics/icons/wheat.png",
        'name':         'Wheat',
        'h_frames':     3,
        'grow_speed':   1.0,
        'death_max':    3,
        'reward':       Enum.Item.WHEAT,
    },
}

# --- MACHINE UPGRADE COSTS ---
# Dictionary: Enum.Machine → dict with display name, item costs, and HUD icon
# 'cost' is itself a dict: Enum.Item → quantity required
const MACHINE_UPGRADE_COST = {
    Enum.Machine.SPRINKLER: {
        'name': 'Sprinkler',
        'cost': { Enum.Item.TOMATO: 30, Enum.Item.WHEAT: 20 },
        'icon': preload("res://graphics/icons/sprinkler.png"),
    },
    Enum.Machine.FISHER: {
        'name': 'Fisher',
        'cost': { Enum.Item.WOOD: 25, Enum.Item.FISH: 15 },
        'icon': preload("res://graphics/icons/fisher.png"),
    },
    Enum.Machine.SCARECROW: {
        'name': 'Scarecrow',
        'cost': { Enum.Item.PUMPKIN: 15, Enum.Item.CORN: 15 },
        'icon': preload("res://graphics/icons/scarecrow.png"),
    },
}

# --- HOUSE UPGRADE COSTS ---
# Dictionary: upgrade_level (int) → item costs for that level
const HOUSE_COST = {
    1: { Enum.Item.WOOD: 30, Enum.Item.APPLE: 20 },
    2: { Enum.Item.WOOD: 40, Enum.Item.APPLE: 30 },
}

# --- STYLE UPGRADE COSTS (hat shop) ---
const STYLE_UPGRADES = {
    Enum.Style.COWBOY:   { 'name': 'Cowboy',   'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/cowboy.png") },
    Enum.Style.ENGLISH:  { 'name': 'Oldie',    'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/english.png") },
    Enum.Style.BASEBALL: { 'name': 'Baseball', 'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/blue.png") },
    Enum.Style.BEANIE:   { 'name': 'Beanie',   'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/beanie.png") },
    Enum.Style.STRAW:    { 'name': 'Straw',    'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/straw.png") },
}

# --- ANIMATION NAME LOOKUP ---
# Maps Enum.Tool values to the BlendSpace2D node name inside ToolStateMachine in the AnimationTree.
# The STRING values here must EXACTLY match the node names in the AnimationTree editor.
# Used in two places:
#   1. tool_state_machine.travel(Data.TOOL_STATE_ANIMATIONS[current_tool])  → switch tool animation
#   2. Loop over .values() to update every tool's blend_position each frame
const TOOL_STATE_ANIMATIONS = {
    Enum.Tool.HOE:   'Hoe',    # BlendSpace2D named "Hoe" in AnimationTree ToolStateMachine
    Enum.Tool.AXE:   'Axe',
    Enum.Tool.WATER: 'Water',
    Enum.Tool.SWORD: 'Sword',
    Enum.Tool.FISH:  'Fish',
    Enum.Tool.SEED:  'Seed',
}

# Runtime variable (not const) — changes each day reset
# true = it will rain tomorrow, false = sunny tomorrow
# Set randomly in level._ready() and re-randomized each level_reset()
var forecast_rain: bool
```

---

## scenes/characters/player.gd
> **Purpose:** All player movement, input, animation, and state switching.
> **Screen:** The character you see and control. The sprite, tool UI above it, fishing minigame overlay.

```gdscript
extends CharacterBody2D   # Built-in Godot type: a body that moves with move_and_slide()

# --- MOVEMENT VARIABLES ---
var direction: Vector2        # Current input direction this frame (zero when no key pressed)
var last_direction: Vector2   # Direction from the LAST frame that had movement
                              # Needed so tool-use offset still works when player is standing still
var speed := 50               # Pixels per second movement speed

# Prevents movement while a tool animation plays (axe swing etc.)
var can_move: bool = true

# --- ANIMATION TREE REFERENCES ---
# get() on AnimationTree returns the playback controller for a state machine
# This is the only way to call .travel() to switch states from GDScript
@onready var move_state_machine = $Animation/AnimationTree.get("parameters/MoveStateMachine/playback")
@onready var tool_state_machine = $Animation/AnimationTree.get("parameters/ToolStateMachine/playback")

# --- GAME STATE VARIABLES ---
# These track what the player is currently doing/holding
var current_tool: Enum.Tool = Enum.Tool.AXE      # Which tool is equipped (cycled with Q/E)
var current_seed: Enum.Seed                       # Which seed is selected (cycled with C)
var current_state: Enum.State                     # DEFAULT / FISHING / BUILDING / SHOP
var current_style: Enum.Style                     # Current hat/skin (cycled with T)
var current_machine: Enum.Machine                 # Which machine to place in BUILD mode

# --- SIGNALS ---
# These are emitted BY the player and RECEIVED by the level script
# Decouples player from level — player doesn't need a reference to level
signal tool_use(tool: Enum.Tool, pos: Vector2)    # Emitted at the hit frame of each animation
signal diagnose                                    # Toggle plant info overlay (N key)
signal day_change                                  # Sleeping in bed triggers day reset
signal build(current_machine: Enum.Machine)        # Place a machine at player's feet
signal machine_change(current_machine: Enum.Machine) # Switched which machine to place

# ─────────────────────────────────────────────────────────────────────────────
func _physics_process(_delta: float) -> void:
    # Called 60 times per second by Godot's physics engine
    # Uses match instead of if/elif so each State has a completely separate input path

    match current_state:
        Enum.State.DEFAULT:
            if can_move:           # Only accept input when no tool animation is playing
                get_basic_input()  # Check Q/E/C/T/Space/M/N keys
                move()             # Read WASD/arrow keys, apply velocity
                animate()          # Update AnimationTree blend positions

        Enum.State.FISHING:
            get_fishing_input()    # Only Space (action) matters while fishing

        Enum.State.BUILDING:
            get_building_input()   # Q/E cycle machines, Space places, M exits
            move()                 # Player can still walk while in build mode
            animate()

    # Update the RayCast so it always points in the player's facing direction
    # This ray is used to detect interactable objects (bed, TV) in front of player
    if direction:
        # ray_y: if moving diagonally, only use vertical component for ray direction
        var ray_y = int(direction.y) if not direction.x else 0
        $RayCast2D.target_position = Vector2(direction.x, ray_y).normalized() * 20

# ─────────────────────────────────────────────────────────────────────────────
func get_basic_input():
    # Called every physics frame when state=DEFAULT and can_move=true

    # --- TOOL CYCLING (Q/E keys) ---
    if Input.is_action_just_pressed("tool_forward") or Input.is_action_just_pressed("tool_backward"):
        # get_axis returns -1.0 (backward) or +1.0 (forward)
        var dir = Input.get_axis("tool_backward", "tool_forward")

        # posmod (positive modulo) wraps the index so it never goes negative or out of bounds
        # e.g. posmod(-1, 6) = 5, posmod(6, 6) = 0
        current_tool = posmod(current_tool + int(dir), Enum.Tool.size()) as Enum.Tool

        # Tell ToolUI to show the tool container (true=tools, false=seeds)
        $ToolUI.reveal(true)

    # --- SEED CYCLING (C key — forward only) ---
    if Input.is_action_just_pressed("seed_forward"):
        current_seed = posmod(current_seed + 1, Enum.Seed.size()) as Enum.Seed
        $ToolUI.reveal(false)   # Show seed container

    # --- ACTION (Space / A button) ---
    if Input.is_action_just_pressed("action"):
        if not $RayCast2D.get_collider():
            # Nothing in front of player → use equipped tool
            # 1. Tell AnimationTree which tool BlendSpace2D to play
            tool_state_machine.travel(Data.TOOL_STATE_ANIMATIONS[current_tool])
            # 2. Fire the OneShot node so the tool animation plays once then returns to walk/idle
            $Animation/AnimationTree.set(
                "parameters/ToolOneShot/request",
                AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE
            )
        else:
            # Something is in front → call its interact() function
            # e.g. Bed.interact(player) triggers day_change_emit()
            $RayCast2D.get_collider().interact(self)

    # --- PLANT INFO OVERLAY (N key) ---
    if Input.is_action_just_pressed("diagnose"):
        diagnose.emit()   # Level receives this and toggles plant_info_container.visible

    # --- STYLE / SKIN TOGGLE (T key) ---
    if Input.is_action_just_pressed("style_toggle"):
        current_style = posmod(current_style + 1, Enum.Style.size()) as Enum.Style
        # Directly swap the Sprite2D texture — Data.PLAYER_SKINS has preloaded all textures
        $Sprite2D.texture = Data.PLAYER_SKINS[current_style]

    # --- ENTER BUILD MODE (M key) ---
    if Input.is_action_just_pressed("build"):
        current_state = Enum.State.BUILDING

# ─────────────────────────────────────────────────────────────────────────────
func get_fishing_input():
    # Only one input matters during fishing: Space raises the bar
    if Input.is_action_just_pressed("action"):
        $FishingGame.action()   # fishing_game.gd: apply upward velocity to the bar sprite

# ─────────────────────────────────────────────────────────────────────────────
func get_building_input():
    # M key again → exit build mode
    if Input.is_action_just_pressed("build"):
        current_state = Enum.State.DEFAULT

    # Q/E cycle through machines (same pattern as tools)
    if Input.is_action_just_pressed("tool_forward") or Input.is_action_just_pressed("tool_backward"):
        var dir = Input.get_axis("tool_backward", "tool_forward")
        current_machine = posmod(current_machine + int(dir), Enum.Machine.size()) as Enum.Machine
        machine_change.emit(current_machine)   # Level updates the preview sprite

    # Space places the selected machine at the player's tile position
    if Input.is_action_just_pressed("action"):
        build.emit(current_machine)   # Level.gd instantiates the correct machine scene

# ─────────────────────────────────────────────────────────────────────────────
func move():
    # Read the 4 movement keys as a normalized Vector2 (-1 to 1 on each axis)
    direction = Input.get_vector("left", "right", "up", "down")
    velocity = direction * speed   # velocity is CharacterBody2D's built-in property
    move_and_slide()               # Godot handles collision response and sliding

# ─────────────────────────────────────────────────────────────────────────────
func animate():
    if direction:
        # Player is moving → switch to Walk state in the state machine
        move_state_machine.travel('Walk')

        # Round the direction so we land on an EXACT point in the BlendSpace2D
        # Without round(): diagonal movement = (0.7, 0.7) which is between points → wrong animation
        # With round():    diagonal movement = (1.0, 1.0) which IS a defined point → correct
        var direction_animation = Vector2(round(direction.x), round(direction.y))

        # Update blend position for IDLE state too, so when player stops,
        # idle animation faces the correct direction
        $Animation/AnimationTree.set("parameters/MoveStateMachine/Idle/blend_position", direction_animation)
        $Animation/AnimationTree.set("parameters/MoveStateMachine/Walk/blend_position", direction_animation)

        # Update fish blend space (used when fishing animation blends with movement)
        $Animation/AnimationTree.set("parameters/FishBlendSpace2D/blend_position", direction_animation)

        # Update ALL tool blend spaces so every tool faces the right direction
        # Data.TOOL_STATE_ANIMATIONS.values() = ["Hoe", "Axe", "Water", "Sword", "Fish", "Seed"]
        for animation in Data.TOOL_STATE_ANIMATIONS.values():
            # Build the parameter path dynamically: "parameters/ToolStateMachine/Axe/blend_position"
            var animation_name: String = "parameters/ToolStateMachine/" + animation + "/blend_position"
            $Animation/AnimationTree.set(animation_name, direction_animation)
    else:
        # No input → switch to Idle state; last blend position is retained from when we were moving
        move_state_machine.travel('Idle')

# ─────────────────────────────────────────────────────────────────────────────
func start_fishing():
    # Called by level.gd when player uses FISH tool while standing next to water
    $FishingGame.reveal()                  # Show the fishing minigame overlay
    current_state = Enum.State.FISHING     # Block normal movement input
    # blend_amount=1 transitions to the fishing animation blend
    $Animation/AnimationTree.set("parameters/FishBlend/blend_amount", 1)

func stop_fishing():
    # Called by fishing_game.gd when the progress bar fills or empties
    can_move = true
    current_state = Enum.State.DEFAULT
    $Animation/AnimationTree.set("parameters/FishBlend/blend_amount", 0)

# ─────────────────────────────────────────────────────────────────────────────
func tool_use_emit():
    # Called by a METHOD TRACK in AnimationPlayer at the exact hit frame of each tool animation
    # Emits the signal with the tool type and the world position of the hit point
    # Position formula: player center + (facing direction × 16px) + 4px downward offset
    tool_use.emit(current_tool, position + last_direction * 16 + Vector2(0, 4))

# ─────────────────────────────────────────────────────────────────────────────
# AnimationTree signals — lock/unlock movement around tool animations
func _on_animation_tree_animation_started(_anim_name: StringName) -> void:
    can_move = false   # Freeze player movement when any animation starts

func _on_animation_tree_animation_finished(_anim_name: StringName) -> void:
    can_move = true    # Unfreeze when animation ends

# ─────────────────────────────────────────────────────────────────────────────
func day_change_emit():
    # Called by Bed.interact() → triggers the day-reset sequence in level.gd
    day_change.emit()

# ─────────────────────────────────────────────────────────────────────────────
func get_machine_coord() -> Vector2i:
    # Returns the world pixel position (snapped to tile center) where a machine should be placed
    # Starts from the player's position, looks 20px in facing direction, offsets down 8px
    var pos = position + last_direction * 20 + Vector2(0, 8)

    # Convert pixel position to tile-grid coordinate
    var coord = Vector2i(pos.x / Data.TILE_SIZE, pos.y / Data.TILE_SIZE)

    # Fix rounding for negative coordinates (integer division truncates toward zero, not floor)
    # e.g. -5 / 16 = 0 in GDScript, but the correct tile is -1
    coord.x += -1 if pos.x < 0 else 0
    coord.y += -1 if pos.y < 0 else 0

    # Snap to tile CENTER (add half-tile offset = 8px) and return as pixel position again
    return coord * Data.TILE_SIZE + Vector2i(8, 8)
```

---

## scenes/levels/level.gd
> **Purpose:** The main game controller — handles all tool effects on the world, day cycle, machine placement, blob spawning.
> **Screen:** Everything you see in the outdoor level. Day color changing, rain particles, machine preview sprite.

```gdscript
extends Node2D

# --- PRELOADED SCENES ---
# All scenes that get dynamically instantiated at runtime
# preload() at the top means they are ready instantly — no delay when spawning
var plant_scene      = preload("res://scenes/objects/plant.tscn")
var plant_info_scene = preload("res://scenes/ui/plant_info.tscn")
var projectile_scene = preload("res://scenes/machines/projectile.tscn")
var blob_scene       = preload("res://scenes/objects/blob.tscn")

# Machine scenes in a dict so we can instantiate the right one by enum key
var machine_scenes = {
    Enum.Machine.SPRINKLER: preload("res://scenes/machines/sprinkler.tscn"),
    Enum.Machine.SCARECROW: preload("res://scenes/machines/scare_crow.tscn"),
    Enum.Machine.FISHER:    preload("res://scenes/machines/fisher.tscn"),
}

# Tracks which grid cells already have a plant (prevents planting on top of existing plant)
var used_cells: Array[Vector2i]

# --- RAINING SETTER ---
# The 'set(value)' block runs automatically whenever raining is assigned
# This keeps particle systems in sync without needing manual calls
var raining: bool:
    set(value):
        raining = value
        $Layers/RainFloorParticles.emitting = value    # Floor splashes start/stop
        $Overlay/RainDropsParticles.emitting = value   # Drop particles start/stop

# --- ONREADY REFERENCES ---
@onready var player = $Objects/Player   # Cached so we don't call $Objects/Player every frame

# The ShaderMaterial on DayTransitionLayer — we animate its 'progress' parameter for day wipe
@onready var day_transition_material = $Overlay/CanvasLayer/DayTransitionLayer.material

# --- EXPORTS ---
# Set in Inspector on the Level node — allows designer to tune colors without touching code
@export var daytime_color: Gradient   # 4-stop gradient: warm morning → white midday → blue night
@export var rain_color: Color         # Tint applied when raining (gray-blue)

# Machine preview sprite textures and their visual offsets
# Shown above player cursor while in BUILD mode so player can see what they're placing
const MACHINE_PREVIEW_TEXTURES = {
    Enum.Machine.SPRINKLER: { 'texture': preload("res://graphics/icons/sprinkler.png"), 'offset': Vector2i(0,  0) },
    Enum.Machine.FISHER:    { 'texture': preload("res://graphics/icons/fisher.png"),    'offset': Vector2i(0, -4) },
    Enum.Machine.SCARECROW: { 'texture': preload("res://graphics/icons/scarecrow.png"), 'offset': Vector2i(0, -4) },
    Enum.Machine.DELETE:    { 'texture': preload("res://graphics/icons/delete.png"),    'offset': Vector2i(0,  0) },
}

# ─────────────────────────────────────────────────────────────────────────────
func _ready() -> void:
    # Randomly decide whether it will rain on the FIRST day
    Data.forecast_rain = [true, false].pick_random()

    # Connect ScareCrow's shoot_projectile signal here (ScareCrow is pre-placed in the scene)
    # We do this in code rather than the editor because the function lives here in level.gd
    $Objects/ScareCrow.connect("shoot_projectile", create_projectile)

# ─────────────────────────────────────────────────────────────────────────────
func _process(_delta: float) -> void:
    # Runs every frame. Handles two visual effects that need continuous updates.

    # --- DAY/NIGHT COLOR ---
    # daytime_point goes from 0.0 (start of day) → 1.0 (end of day)
    var daytime_point = 1 - ($Timers/DayTimer.time_left / $Timers/DayTimer.wait_time)
    # Sample the gradient at this point: morning=warm, midday=white, evening=blue
    # If raining: lerp 50% toward the rain_color for an overcast look
    var color = daytime_color.sample(daytime_point).lerp(rain_color, 0.5 if raining else 0.0)
    $Overlay/DayTimeColor.color = color   # Apply to CanvasModulate — tints the whole scene

    # --- MACHINE BUILD PREVIEW ---
    # Show/hide the preview sprite based on whether player is in BUILD mode
    $Overlay/MachinePreviewSprite.visible = player.current_state == Enum.State.BUILDING
    # Move the preview icon to where the machine would be placed (one tile ahead of player)
    $Overlay/MachinePreviewSprite.position = (
        player.get_machine_coord() +
        MACHINE_PREVIEW_TEXTURES[player.current_machine]['offset']
    )

# ─────────────────────────────────────────────────────────────────────────────
func _on_player_tool_use(tool: Enum.Tool, pos: Vector2) -> void:
    # Receives the tool_use signal from the player (emitted at animation hit frame)
    # pos = world pixel position of the hit point (already offset from player center)

    # Convert pixel position to tile-grid coordinate
    var grid_coord := Vector2i(int(pos.x / Data.TILE_SIZE), int(pos.y / Data.TILE_SIZE))
    # Fix negative-side rounding (see player.gd get_machine_coord() for explanation)
    grid_coord.x += -1 if pos.x < 0 else 0
    grid_coord.y += -1 if pos.y < 0 else 0

    # Reusable check: is there a soil tile at this grid position?
    var has_soil = grid_coord in $Layers/SoilLayer.get_used_cells()

    match tool:
        Enum.Tool.HOE:
            # Only allow hoeing on tiles marked 'farmable' in GrassLayer custom data
            var cell = $Layers/GrassLayer.get_cell_tile_data(grid_coord) as TileData
            if cell and cell.get_custom_data('farmable'):
                # set_cells_terrain_connect: place a terrain tile that auto-connects to neighbors
                # Args: [cells array], terrain_set index, terrain index
                $Layers/SoilLayer.set_cells_terrain_connect([grid_coord], 0, 0)
            # If it's raining, also add a water tile immediately (free watering from rain)
            if raining:
                $Layers/SoilWaterLayer.set_cell(grid_coord, 0, Vector2i(randi_range(0,2), 0))

        Enum.Tool.WATER:
            # Only water tiles that have soil beneath them
            if has_soil:
                # Pick one of 3 water patch variants randomly (atlas x coord 0,1, or 2)
                $Layers/SoilWaterLayer.set_cell(grid_coord, 0, Vector2i(randi_range(0,2), 0))

        Enum.Tool.FISH:
            # Can only fish where there is NO grass tile (i.e. in water / at coast)
            if not grid_coord in $Layers/GrassLayer.get_used_cells():
                $Objects/Player.start_fishing()

        Enum.Tool.SEED:
            # Can only plant on soil that doesn't already have a plant
            if has_soil and grid_coord not in used_cells:
                # Create a new PlantResource and fill it from the data dict
                var plant_res = PlantResource.new()
                plant_res.setup($Objects/Player.current_seed)

                # Instantiate the plant scene and set it up at the correct tile position
                var plant = plant_scene.instantiate()
                # Pass plant_death as a callable so the plant can call it when it dies
                plant.setup(grid_coord, $Objects, plant_res, plant_death)
                used_cells.append(grid_coord)   # Mark this cell as occupied

                # Create the companion UI panel for this plant
                var plant_info = plant_info_scene.instantiate()
                plant_info.setup(plant_res)   # Both plant AND panel share the SAME resource object
                $Overlay/CanvasLayer/PlantInfoContainer.add(plant_info)

        Enum.Tool.AXE, Enum.Tool.SWORD:
            # Both tools hit nearby objects in the "Objects" group
            for object in get_tree().get_nodes_in_group('Objects'):
                # distance_to < 20px means the object is close enough to be hit
                if object.position.distance_to(pos) < 20:
                    object.hit(tool)   # tree.gd / blob.gd both implement hit()

# ─────────────────────────────────────────────────────────────────────────────
func _on_player_diagnose() -> void:
    # N key pressed → toggle plant info overlay visibility
    $Overlay/CanvasLayer/PlantInfoContainer.visible = not $Overlay/CanvasLayer/PlantInfoContainer.visible

func _on_player_day_change() -> void:
    # Player slept in bed → start the day-reset sequence
    day_restart()

# ─────────────────────────────────────────────────────────────────────────────
func _on_player_build(current_machine: int) -> void:
    if current_machine != Enum.Machine.DELETE:
        # Instantiate and place the selected machine at the player's target tile
        var machine = machine_scenes[current_machine].instantiate()
        machine.setup(player.get_machine_coord(), self, $Objects)
    else:
        # DELETE mode: remove the machine at the player's target tile
        # coord is in tile units, get_machine_coord() returns pixel units → divide by 16
        for machine in get_tree().get_nodes_in_group('Machines'):
            machine.delete(player.get_machine_coord() / 16)

func _on_player_machine_change(current_machine: int) -> void:
    # Player cycled to a different machine → update the preview icon
    $Overlay/MachinePreviewSprite.texture = MACHINE_PREVIEW_TEXTURES[current_machine]['texture']

# ─────────────────────────────────────────────────────────────────────────────
func day_restart():
    # Sequence: fade to black → reset world → fade back in
    var tween = create_tween()
    # Animate the circle shader's progress from 0→1 (screen goes black, circle shrinks)
    tween.tween_property(day_transition_material, "shader_parameter/progress", 1.0, 1.0)
    tween.tween_interval(0.5)       # Hold black screen for half a second
    tween.tween_callback(level_reset)  # Run all world-reset logic while screen is black
    # Animate progress 1→0 (circle expands, reveals new day)
    tween.tween_property(day_transition_material, "shader_parameter/progress", 0.0, 1.0)

# ─────────────────────────────────────────────────────────────────────────────
func level_reset():
    # Called while screen is black — safe to update all world state here

    # Grow or decay every plant based on whether its tile was watered
    for plant in get_tree().get_nodes_in_group('Plants'):
        # coord in SoilWaterLayer.get_used_cells() = true means this tile has a water patch
        plant.grow(plant.coord in $Layers/SoilWaterLayer.get_used_cells())

    # Remove all water patches — player must water again each day
    $Layers/SoilWaterLayer.clear()

    # Refresh all plant info panels (growth bars, death bars)
    $Overlay/CanvasLayer/PlantInfoContainer.update_all()

    # Restart the 2-minute day timer
    $Timers/DayTimer.start()

    # Call reset() on any object that has one (trees respawn apples, etc.)
    for object in get_tree().get_nodes_in_group('Objects'):
        if 'reset' in object:   # 'reset' in object checks if object has a 'reset' property/method
            object.reset()

    # Apply the rain forecast that was decided on the PREVIOUS day
    raining = Data.forecast_rain
    # Decide randomly whether TOMORROW will rain
    Data.forecast_rain = [true, false].pick_random()

    # If raining: automatically water all existing soil tiles
    if raining:
        for cell in $Layers/SoilLayer.get_used_cells():
            $Layers/SoilWaterLayer.set_cell(cell, 0, Vector2i(randi_range(0,2), 0))

# ─────────────────────────────────────────────────────────────────────────────
func plant_death(coord: Vector2i):
    # Called via signal when a plant is harvested or dies from neglect
    # Removes the grid cell from the occupied list so a new plant can be placed there
    used_cells.erase(coord)

func create_projectile(start_pos: Vector2, dir: Vector2):
    # Called when ScareCrow fires at a blob
    var projectile = projectile_scene.instantiate()
    projectile.setup(start_pos, dir)
    $Objects.add_child(projectile)   # Add to Objects node so it's Y-sorted with everything else

func water_plants(coord: Vector2i):
    # Called by Sprinkler machine — waters the 8 tiles surrounding the machine's position
    const SOIL_DIRECTIONS = [
        Vector2i(-1,-1), Vector2i(0,-1), Vector2i(1,-1),
        Vector2i(-1, 0),                 Vector2i(1, 0),
        Vector2i(-1, 1), Vector2i(0, 1), Vector2i(1, 1),
    ]
    for dir in SOIL_DIRECTIONS:
        var cell = coord + dir
        # Only place water where soil actually exists (don't draw water on grass/water tiles)
        if cell in $Layers/SoilLayer.get_used_cells():
            $Layers/SoilWaterLayer.set_cell(cell, 0, Vector2i(randi_range(0,2), 0))

func _on_blob_timer_timeout() -> void:
    # Every 20 seconds: spawn a blob at a random spawn point, targeting a random plant
    var plants = get_tree().get_nodes_in_group('Plants')
    if plants:   # Only spawn if there are plants to attack (no point otherwise)
        var blob = blob_scene.instantiate()
        var pos = $BlobSpawnPositions.get_children().pick_random().position
        # Give the blob a random plant as its target
        blob.setup(pos, plants.pick_random(), $Objects)
```

---

## resources/plant_res.gd
> **Purpose:** Data container for one plant instance. Shared between the plant sprite and the plant info panel.
> **Screen:** The plant's growth frame, the green growth bar, the red death bar — all driven by this resource.

```gdscript
class_name PlantResource extends Resource
# class_name: makes "PlantResource.new()" available everywhere
# extends Resource: no node needed, just data + signals

# --- EXPORTED DATA ---
# These are set by setup() from Data.PLANT_DATA — designer-tunable per plant type
@export var texture: Texture2D       # The growth-stage spritesheet
@export var icon_texture: Texture2D  # Small icon for the UI panel header
@export var grow_speed: float = 1.0  # How much age increases per watered day (MUST be float!)
@export var h_frames: int = 3        # Number of growth stages (frames) in the spritesheet
@export var death_max: int = 3       # Un-watered days before death
@export var name: String             # Display name e.g. "Tomato"

# --- RUNTIME STATE ---
# Not exported — changes every day as the plant grows
var age: float          # Accumulated growth (0.0 → h_frames = fully grown)

# Property setter: call emit_changed() whenever death_count changes
# This triggers the "changed" signal → plant_info.gd updates its progress bar
var death_count: int:
    set(value):
        death_count = value
        emit_changed()   # Broadcast to all connected scenes (plant_info panels)

# Property setter: same pattern — tells plant_info to remove itself when plant dies
var dead: bool:
    set(value):
        dead = value
        emit_changed()

# ─────────────────────────────────────────────────────────────────────────────
func setup(seed_enum: Enum.Seed):
    # Populate all exported vars from the central data dictionary
    # load() (not preload) because we create resources at runtime, not at startup
    texture      = load(Data.PLANT_DATA[seed_enum]['texture'])
    icon_texture = load(Data.PLANT_DATA[seed_enum]['icon_texture'])
    grow_speed   = Data.PLANT_DATA[seed_enum]['grow_speed']   # float value from dict
    h_frames     = Data.PLANT_DATA[seed_enum]['h_frames']
    death_max    = Data.PLANT_DATA[seed_enum]['death_max']
    name         = Data.PLANT_DATA[seed_enum]['name']

func grow(sprite: Sprite2D):
    # Called on day reset if the plant's tile had water on it
    # Clamp so age never exceeds the maximum frame (h_frames)
    age = min(age + grow_speed, h_frames)
    # Update the visible sprite frame (int() truncates the float → frame index 0,1,2,3)
    sprite.frame = int(age)
    # Reset death counter — being watered once forgives all previous dry days
    death_count = 0

func decay(plant: StaticBody2D):
    # Called on day reset if the plant's tile had NO water
    death_count += 1   # Triggers setter → emit_changed() → panel updates red bar
    if death_count >= death_max:
        emit_changed()
        plant.queue_free()   # Remove the plant node from the scene

func get_complete() -> bool:
    # Returns true when the plant has reached max growth and is ready to harvest
    return age >= h_frames

func damage():
    # Called by blob.gd when a blob reaches the plant — same as one dry day
    death_count += 1
```

---

## scenes/objects/plant.gd
> **Purpose:** The visual plant node. A thin "shell" that displays the PlantResource data.
> **Screen:** The growing sprite in the soil. Flashes white on harvest, then disappears.

```gdscript
extends StaticBody2D   # Static = doesn't move, but has physics collision

var coord: Vector2i      # Grid coordinate (tile position, not pixel) — used to check if watered
@export var res: PlantResource   # The data resource; set via setup()
signal death(coord: Vector2i)    # Emitted when plant is harvested → level removes used_cell

func setup(grid_coord: Vector2i, parent: Node2D, new_res: PlantResource, plant_death_func):
    # Convert tile coordinate to pixel position and center it in the tile
    # +Vector2i(8,5) = half tile width, slightly above center for visual alignment
    position = grid_coord * Data.TILE_SIZE + Vector2i(8, 5)
    parent.add_child(self)   # Add to $Objects in level.tscn (must be done after setup)
    coord = grid_coord
    res = new_res

    # Set FlashSprite2D texture and frame count from the resource
    $FlashSprite2D.texture = res.texture
    $FlashSprite2D.hframes = res.h_frames

    # Connect the death signal to the function passed in from level.gd
    # This pattern avoids the plant needing a reference to level
    death.connect(plant_death_func)

    # React to resource changes (emit_changed) → update visual or remove if dead
    res.connect("changed", update)

func update():
    # Called automatically whenever the resource emits emit_changed()
    if res.death_count >= res.death_max:
        queue_free()   # Remove the plant sprite when it's fully dead

func grow(watered: bool):
    # Called by level_reset() each day for every plant
    if watered:
        res.grow($FlashSprite2D)   # Pass the sprite so resource can update frame
    else:
        res.decay(self)            # Pass self so resource can queue_free() this node

func _on_collision_area_body_entered(_body: Node2D) -> void:
    # Triggered when the player walks into the plant's Area2D collision
    if res.get_complete():   # Only harvest if fully grown
        # Flash white first (0.2s fade in, 0.4s fade out), THEN call queue_free
        $FlashSprite2D.flash(0.2, 0.4, queue_free)
        death.emit(coord)    # Tell level to free up this grid cell
        res.dead = true      # Triggers setter → emit_changed → plant_info panel removes itself

func damage():
    # Called by level.gd when axe/sword hits nearby, or by blob when it reaches the plant
    res.damage()
```

---

## scenes/objects/tree.gd
> **Purpose:** Choppable tree with health, apple drops, and stump fallback.
> **Screen:** Tree sprite → flashes on axe hit → apples fall off → becomes stump at health=0.

```gdscript
extends StaticBody2D

# Preload apple texture once at class level (shared across all tree instances)
const apple_texture = preload("res://graphics/plants/apple.png")

# Health with setter — automatically triggers visual change when reaching 0
var health := 3:
    set(value):
        health = value
        if health <= 0:
            # Hide tree, show stump
            $FlashSprite2D.hide()
            $Stump.show()
            # Shrink collision shape to match the smaller stump sprite
            var shape = RectangleShape2D.new()
            shape.size = Vector2(12, 6)
            $CollisionShape2D.shape = shape
            $CollisionShape2D.position.y = 8   # Move collision down to ground level

func _ready() -> void:
    # Randomly pick one of the two tree variants (frame 0 or 1)
    $FlashSprite2D.frame = [0, 1].pick_random()
    # Spawn 0-3 apples randomly on the tree at startup
    create_apples(randi_range(0, 3))

func hit(tool: Enum.Tool):
    # Called by level.gd when axe/sword hits this tree
    if tool == Enum.Tool.AXE:          # Only axe damages trees (sword is for enemies)
        $FlashSprite2D.flash()          # White flash visual feedback
        get_apple()                     # Knock one apple off
        health -= 1                     # Triggers setter above

func create_apples(num: int):
    # Spawn 'num' apple sprites at random positions from the AppleSpawnPositions markers
    var apple_markers = $AppleSpawnPositions.get_children().duplicate(true)  # deep copy so we can pop
    for i in num:
        # Pick a random position marker and remove it from the list (no duplicate positions)
        var pos_marker = apple_markers.pop_at(randi_range(0, apple_markers.size() - 1))
        var sprite = Sprite2D.new()    # Create apple sprite dynamically
        sprite.texture = apple_texture
        $Apples.add_child(sprite)
        sprite.position = pos_marker.position

func get_apple():
    # Remove one random apple sprite from the tree (called when axe hits)
    if $Apples.get_children():
        $Apples.get_children().pick_random().queue_free()

func reset():
    # Called by level_reset() at start of each day
    if health > 0:   # Don't reset a dead (stumped) tree
        for apple in $Apples.get_children():
            apple.queue_free()                    # Clear old apples
        create_apples(randi_range(0, 3))          # Spawn fresh apples
        health = 3                                # Restore health for new day
```

---

## scenes/objects/simple_object.gd
> **Purpose:** Decorative bush or rock. Uses @tool so you can randomize it live in the editor.
> **Screen:** The scattered bushes and rocks visible across the level.

```gdscript
@tool           # Makes this script run in the Godot EDITOR as well as at runtime
                # Without @tool: code only runs when game is playing
                # With @tool: set() functions update the sprite live as you change Inspector values
extends StaticBody2D

# @export_range(min, max, step) — creates an Inspector slider
# 'set(value)' runs immediately when you change the value in Inspector (because @tool)
@export_range(0, 3, 1) var size: int:
    set(value):
        size = value
        $Sprite2D.frame_coords = Vector2i(size, style)  # Update sprite immediately in editor

# @export_enum shows a dropdown in Inspector with string labels (but stores 0 or 1 as int)
@export_enum('Bush', 'Rock') var style: int:
    set(value):
        style = value
        $Sprite2D.frame_coords = Vector2i(size, style)

@export var random: bool   # If true: randomize size and style at _ready()

func _ready() -> void:
    if random:
        # Pick random size (0–hframes-1) and random style (0=bush or 1=rock)
        size  = randi_range(0, $Sprite2D.hframes - 1)
        style = [0, 1].pick_random()

    # Apply the current size/style to the sprite
    $Sprite2D.frame_coords = Vector2i(size, style)

    # Small objects (size 0 or 1) = player can walk through (no collision)
    $CollisionShape2D.disabled = size < 2

    # Small objects draw BEHIND the player (z=-1), large objects draw in front (z=0)
    z_index = -1 if size < 2 else 0
```

---

## scenes/objects/blob.gd
> **Purpose:** Enemy that seeks the nearest plant and attacks it. Pushed by sword hits, dies to 3 hits.
> **Screen:** The blob character moving toward plants. Flashes on hit. Explodes when killed.

```gdscript
extends CharacterBody2D   # Needs physics-based movement like the player

var direction: Vector2    # Direction toward current plant target
var speed := 20           # Slower than player (player speed=50) so player can outrun it
var push_distance := 130  # How far a sword hit pushes the blob back

# Added to velocity so the push effect gradually fades (set by tween, decays to zero)
var push_direction: Vector2

var health := 3:
    set(value):
        health = value
        if health <= 0:
            death()       # Triggered automatically when health reaches zero

var plant_target: StaticBody2D   # The plant this blob is moving toward
var active: bool = true          # False after damaging plant — prevents double-hit

# Get player reference once (used to calculate push direction away from player)
@onready var player = get_tree().get_first_node_in_group('Player')

func setup(start_pos, target, parent):
    # Called by level.gd when spawning the blob
    position = start_pos
    parent.add_child(self)    # Add to $Objects in level scene
    plant_target = target     # Assign the plant this blob will chase

func _physics_process(_delta: float) -> void:
    if plant_target:
        # Move toward the plant target — normalized gives direction only (speed=1 unit)
        direction = (plant_target.position - position).normalized()
        # Add push_direction on top of normal movement (push_direction tweens back to zero)
        velocity = direction * speed + push_direction
        move_and_slide()

        # When blob reaches the plant:
        if position.distance_to(plant_target.position) < 10 and active:
            plant_target.damage()  # Reduce plant's death_count via plant_res.gd
            active = false         # Prevent hitting again
            death()                # Self-destruct after hitting
    else:
        death()   # Plant was deleted before blob arrived → just die

func push(dir = Vector2.ZERO):
    # Apply knockback when hit by sword
    var tween = get_tree().create_tween()
    # If no direction passed, push AWAY from player
    var target_dir = dir if dir else (player.position - position).normalized()
    # Push backward at full distance, then smoothly return to zero (simulate deceleration)
    var target = target_dir * -1 * push_distance
    tween.tween_property(self, "push_direction", target, 0.1)   # Fast knockback
    tween.tween_property(self, "push_direction", Vector2.ZERO, 0.2)  # Slow recovery

func death():
    speed = 0   # Stop moving
    $AnimationPlayer.current_animation = 'explode'   # Play explosion frames, then queue_free at end

func hit(tool: Enum.Tool, dir = Vector2.ZERO):
    if tool == Enum.Tool.SWORD:
        $FlashSprite2D.flash()   # White flash feedback
        push(dir)                # Push away from hit direction
        health -= 1              # Triggers health setter above
```

---

## scenes/vfx/flash_sprite_2d.gd
> **Purpose:** A reusable Sprite2D that can flash white on command. Used by trees, blobs, plants.
> **Screen:** The white flash on hit/harvest — the satisfying visual feedback for every interaction.

```gdscript
extends Sprite2D   # This IS a Sprite2D (the texture is set by whoever uses it)

func flash(start_duration: float = 0.2, end_duration: float = 0.2, callback_func: Callable = Callable()):
    # start_duration: how long to fade TO white (quick hit = 0.2s)
    # end_duration:   how long to fade back FROM white
    # callback_func:  optional function to call between the two tweens
    #                 Used by plant.gd to call queue_free() AFTER the flash (not before)

    var tween = create_tween()   # Create a new animation sequence

    # Tween the shader's 'Progress' parameter: 0=original color, 1=pure white
    tween.tween_property(material, 'shader_parameter/Progress', 1.0, start_duration)

    # If a callback was provided (e.g. queue_free), insert it between the two tweens
    if callback_func.is_valid():
        tween.tween_callback(callback_func)

    # Fade back to original color
    tween.tween_property(material, 'shader_parameter/Progress', 0.0, end_duration)
    # NOTE: if callback was queue_free(), this line never runs (node is already freed)
    # That's fine — Godot cancels tweens on freed nodes automatically
```

---

## scenes/machines/machine.gd
> **Purpose:** Base class for all placeable machines. Handles grid snapping and deletion.
> **Screen:** The machine sprite placed on the ground. Deletes when DELETE mode targets its tile.

```gdscript
class_name Machine extends StaticBody2D
# class_name: child scripts use 'extends Machine' to inherit setup() and delete()

var coord: Vector2i   # The machine's position in TILE GRID units (not pixels)
                      # Stored as tile coord so delete() can compare with integer math

func setup(pos: Vector2i, _level: Node2D, parent: Node2D):
    # pos is already a pixel position snapped to tile center from get_machine_coord()
    coord = pos / Data.TILE_SIZE   # Convert pixel → tile grid for delete comparison
    position = pos                  # Set visual position in the world
    parent.add_child(self)          # Add to $Objects in level.tscn

func delete(delete_coord):
    # Called on ALL machines when DELETE mode is used
    # Each machine checks if it's the one being targeted
    if coord == delete_coord:
        queue_free()   # Only this machine removes itself
```

---

## scenes/machines/sprinkler.gd
> **Purpose:** Waters a 3×3 area around itself every timer interval.
> **Screen:** Animated sprinkler, water particles, watered soil patches appear around it.

```gdscript
extends Machine   # Inherits setup() and delete() from machine.gd

signal water_plants(coord: Vector2i)   # Received by level.gd which actually modifies the tilemap

func setup(pos: Vector2i, level: Node2D, parent: Node2D):
    super.setup(pos, level, parent)   # Call Machine.setup() first (sets coord, position, adds child)
    # Connect this signal to level.water_plants() so the sprinkler can trigger tile updates
    connect("water_plants", level.water_plants)

func _on_timer_timeout() -> void:
    # Timer fires every ~30 seconds
    $AnimatedSprite2D.play("action")    # Play watering animation
    $GPUParticles2D.emitting = true     # Burst of water particles
    await $AnimatedSprite2D.animation_finished   # Wait for animation to complete
    $AnimatedSprite2D.play("default")  # Return to idle animation
    water_plants.emit(coord)           # Signal level.gd to water surrounding tiles
```

---

## scenes/machines/scare_crow.gd
> **Purpose:** Automatic turret — fires projectiles at the nearest blob within range.
> **Screen:** The scarecrow statue. When a blob is near, a projectile shoots toward it.

```gdscript
extends Machine

signal shoot_projectile(start_pos: Vector2, dir: Vector2)   # Received by level.gd → spawns projectile scene
@export var max_range := 150   # Inspector-tweakable detection radius in pixels

func _on_timer_timeout() -> void:
    var blobs = get_tree().get_nodes_in_group("Blobs")
    if blobs:   # Only fire if there are blobs to target
        var nearest_blob = get_nearest_blob(blobs)
        # Only fire if the nearest blob is within range
        if nearest_blob.position.distance_to(position) < max_range:
            # Emit direction vector from scarecrow to blob
            shoot_projectile.emit(position, (nearest_blob.position - position).normalized())

func get_nearest_blob(blobs: Array) -> CharacterBody2D:
    var nearest = blobs[0]   # Start with the first blob as candidate
    for blob in blobs:
        # Replace candidate if this blob is closer
        if blob.position.distance_to(position) <= nearest.position.distance_to(position):
            nearest = blob
    return nearest
```

---

## scenes/machines/fisher.gd
> **Purpose:** Automated fisher machine placed at the water's edge. Plays directional cast animation.
> **Screen:** Fisher sprite facing toward the water, with a progress bar showing fishing cooldown.

```gdscript
extends Machine

# Maps coast direction (from GrassLayer custom data) to animation name
const ANIMATIONS = {
    Vector2i.DOWN:  'down',
    Vector2i.LEFT:  'left',
    Vector2i.RIGHT: 'right',
    Vector2i.UP:    'up',
}
var direction := Vector2i.DOWN   # Default direction (overridden by coast tile data)

func setup(pos: Vector2i, level: Node2D, parent: Node2D):
    # Read the GrassLayer tile at this position to find the coast direction
    var grass_layer = level.get_node("Layers/GrassLayer") as TileMapLayer
    var adjusted_coord = pos / Data.TILE_SIZE
    # Negative coordinate fix (same pattern as player.gd and level.gd)
    adjusted_coord.x += -1 if pos.x < 0 else 0
    adjusted_coord.y += -1 if pos.y < 0 else 0
    var tile_data = grass_layer.get_cell_tile_data(adjusted_coord) as TileData
    # 'coast' is a custom data layer on GrassLayer tiles — Vector2i indicating water direction
    if tile_data.get_custom_data('coast'):
        direction = tile_data.get_custom_data('coast')
        super.setup(pos, level, parent)   # Only place the fisher if this IS a coast tile

func _ready() -> void:
    start_fishing()   # Begin the animation cycle immediately

func _process(_delta: float) -> void:
    # Update progress bar: 0% at start of wait, 100% when timer is about to fire
    var progress = (1 - ($Timer.time_left / $Timer.wait_time)) * 100
    $Control/TextureProgressBar.value = progress

func _on_timer_timeout() -> void:
    start_fishing()   # Restart the fishing cycle after each catch

func start_fishing():
    $AnimatedSprite2D.play(ANIMATIONS[direction])             # Cast animation (based on coast direction)
    await $AnimatedSprite2D.animation_finished                # Wait for cast to finish
    $AnimatedSprite2D.play(ANIMATIONS[direction] + "_idle")   # Hold idle (line in water)
    $Timer.start()                                            # Start wait timer for next catch
```

---

## scenes/machines/projectile.gd
> **Purpose:** A single projectile fired by the scarecrow. Moves in a straight line and hits blobs.
> **Screen:** A small moving sprite flying from the scarecrow toward a blob.

```gdscript
extends Area2D   # Area2D: detects overlaps but has no physics body of its own

var direction: Vector2   # Set by setup() — normalized direction toward target
var speed := 150         # Pixels per second (much faster than blob speed=20)

func setup(start_pos: Vector2, new_direction: Vector2):
    position = start_pos
    direction = new_direction

func _process(delta: float) -> void:
    # Move in a straight line every frame (no physics engine needed for simple linear motion)
    position += direction * speed * delta

func _on_body_entered(body: Node2D) -> void:
    # Fires when the Area2D overlaps a physics body
    if body.is_in_group("Blobs"):
        # Hit the blob — pass the reverse direction as the knockback direction
        body.hit(Enum.Tool.SWORD, direction * -1)
    queue_free()   # Projectile always disappears on contact (whether it hit a blob or a wall)
```

---

## scenes/ui/fishing_game.gd
> **Purpose:** The minigame overlay when fishing. Player presses Space to raise a bar, keeping it over a moving fish.
> **Screen:** A vertical bar indicator. Green progress meter. Fish icon bouncing randomly.

```gdscript
extends Node2D

# y_range: the total vertical space the bar and fish can move in
# Calculated from the NinePatchRect container size minus margins
@onready var y_range = $Control/NinePatchRect.custom_minimum_size.y - 10

var velocity: float       # Downward velocity of the bar — increases over time (gravity effect)
var fish_velocity: float  # Current velocity of the fish (random direction, changes on timer)
var progress := 30.0      # Progress bar value (0=fail, 100=success, starts at 30 = middle)
var sprite_size: Vector2  # Cached size of the bar sprite for boundary calculations

func _ready() -> void:
    hide()   # Fishing UI is hidden until player uses the FISH tool at water
    sprite_size = $BarSprite.get_rect().size

func _process(delta: float) -> void:
    if visible:   # Only run game logic when the overlay is shown
        # --- BAR MOVEMENT (gravity) ---
        velocity += 20 * delta         # Accelerate downward each frame
        $BarSprite.position.y += velocity * delta   # Apply velocity to bar position

        # Clamp bar within the play area (half-bar padding on each side)
        var half_bar_height = sprite_size.y / 2 - 2
        $BarSprite.position.y = clamp(
            $BarSprite.position.y,
            -y_range / 2.0 + half_bar_height,
            y_range / 2.0 - half_bar_height
        )

        # --- FISH MOVEMENT ---
        $FishSprite.position.y += fish_velocity * delta
        $FishSprite.position.y = clamp($FishSprite.position.y, -y_range / 2.0, y_range / 2.0)

        # --- PROGRESS CALCULATION ---
        var top_point    = $BarSprite.position.y - sprite_size.y / 2
        var bottom_point = $BarSprite.position.y + sprite_size.y / 2
        # If fish is inside the bar boundaries → gain progress, otherwise lose it
        if $FishSprite.position.y >= top_point and $FishSprite.position.y <= bottom_point:
            progress += 10 * delta   # Increase when catching
        else:
            progress -= 10 * delta   # Decrease when missing
        $Control/TextureProgressBar.value = progress

func reveal():
    show()   # Display the UI
    # Start fish at a random vertical position
    $FishSprite.position.y = randf_range(-y_range / 2.0, y_range / 2.0)
    fish_velocity = randf_range(-20, 20)   # Random initial direction

func action():
    # Called every time player presses Space while fishing
    velocity = -25   # Apply upward impulse to the bar (fight against gravity)

func _on_fish_update_timer_timeout() -> void:
    # Periodically change fish direction to make it unpredictable
    fish_velocity = randf_range(-20, 20)
    $FishUpdateTimer.wait_time = randf_range(1, 3)   # Random interval for next change

func _on_texture_progress_bar_value_changed(value: float) -> void:
    # Called automatically by Godot when TextureProgressBar.value changes
    if value <= 0 or value >= 100:
        hide()                          # Hide the minigame UI
        get_parent().stop_fishing()     # Tell player.gd to exit FISHING state
```

---

## scenes/ui/tool_ui.gd
> **Purpose:** Builds and shows the tool/seed icon row above the player's head.
> **Screen:** The row of 6 tool icons or 4 seed icons that slides in when you press Q/E/C, hides after 1 second.

```gdscript
extends Control

# Texture lookup: Enum.Tool → icon texture
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

func _ready() -> void:
    # Hide both containers on startup (only show when player cycles tools)
    for container in [$ToolContainer, $SeedContainer]:
        container.hide()
    # Build the icon rows dynamically from enum values + texture dicts
    texture_setup(Enum.Tool.values(), TOOL_TEXTURES, $ToolContainer)
    texture_setup(Enum.Seed.values(), SEED_TEXTURES, $SeedContainer)

func texture_setup(enum_list: Array, textures: Dictionary, container: HBoxContainer):
    # Instantiate one ToolUITexture scene per enum value and add to the container
    for enum_id in enum_list:
        var tool_texture = tool_texture_scene.instantiate()
        tool_texture.setup(enum_id, textures[enum_id])  # Pass enum id and icon texture
        container.add_child(tool_texture)

func reveal(tool: bool):
    # tool=true: show tool row; tool=false: show seed row
    $HideTimer.start()   # Reset the 1-second auto-hide timer

    # Determine which container and which currently selected item to highlight
    var current_container = $ToolContainer if tool else $SeedContainer
    var target = get_parent().current_tool if tool else get_parent().current_seed

    # Hide both, then show only the relevant one
    for container in [$ToolContainer, $SeedContainer]:
        container.hide()
    current_container.show()

    # Scale up the selected icon, scale down all others
    for texture in current_container.get_children():
        texture.highlight(target == texture.tool_enum)

func _on_hide_timer_timeout() -> void:
    for container in [$ToolContainer, $SeedContainer]:
        container.hide()
```

---

## scenes/ui/tool_ui_texture.gd
> **Purpose:** A single icon in the tool/seed row. Scales up when it's the currently selected item.
> **Screen:** Each individual icon in the tool row. Selected one is 20×20px, others are 16×16px.

```gdscript
extends Control

var tool_enum: Enum.Tool   # Which tool/seed this icon represents (set by setup)

func setup(new_tool_enum: Enum.Tool, main_texture: Texture2D):
    tool_enum = new_tool_enum      # Remember which enum value this icon is
    $TextureRect.texture = main_texture   # Apply the icon image

func highlight(selected: bool):
    # Smoothly resize the icon: selected=20×20, not selected=16×16
    var tween = create_tween()
    var target_size = Vector2(20, 20) if selected else Vector2(16, 16)
    # Tween the TextureRect's custom_minimum_size to smoothly scale
    tween.tween_property($TextureRect, "custom_minimum_size", target_size, 0.1)
```

---

## scenes/ui/plant_info.gd
> **Purpose:** One panel showing a single plant's name, icon, growth bar, and death bar.
> **Screen:** The sidebar panels on the left showing each plant's status.

```gdscript
extends PanelContainer

var res: PlantResource   # Reference to the plant's shared resource

func setup(new_res: PlantResource):
    res = new_res
    # Set static data (doesn't change after setup)
    $HBoxContainer/VBoxContainer/NameLabel.text = res.name
    $HBoxContainer/IconTexture.texture = res.icon_texture
    # Set progress bar max values based on plant type
    $HBoxContainer/VBoxContainer/GrowthBar.max_value = res.h_frames
    $HBoxContainer/VBoxContainer/DeathBar.max_value = res.death_max
    update()                    # Set initial bar values
    res.connect("changed", update)   # Auto-update whenever resource emits emit_changed()

func update():
    # Update both bars to reflect current resource state
    $HBoxContainer/VBoxContainer/GrowthBar.value = res.age         # Green bar: growth
    $HBoxContainer/VBoxContainer/DeathBar.value = res.death_count  # Red bar: neglect
    # Remove this panel if the plant has died (death_count reached max)
    if res.death_count >= res.death_max:
        queue_free()
```

---

## scenes/ui/plant_info_container.gd
> **Purpose:** The scroll container that holds ALL plant info panels.
> **Screen:** The scrollable sidebar on the left of the screen showing all active plants.

```gdscript
extends Control

func add(child: PanelContainer):
    # Add a new plant_info panel to the VBoxContainer (stacks them vertically)
    $MarginContainer/ScrollContainer/VBoxContainer.add_child(child)

func update_all():
    # Called by level_reset() each day — refresh every panel's bars
    for plant_info in $MarginContainer/ScrollContainer/VBoxContainer.get_children():
        plant_info.update()
```

---

## scenes/levels/house.gd
> **Purpose:** Controls roof transparency when player enters, and syncs floor tiles with wall tiles.
> **Screen:** House roof fades out when you walk inside. Door opens/closes.

```gdscript
extends Node2D

# Setter: changing in_house automatically updates the door tile and roof opacity
var in_house: bool:
    set(value):
        in_house = value
        # Door tile: Vector2i.ONE = open door frame, Vector2i(0,4) = closed door tile
        $WallsLayer.set_cell(door_cell_coord, 0, Vector2i.ONE if value else Vector2i(0,4))
        # Tween roof alpha: 0=transparent (inside), 1=opaque (outside)
        var tween = create_tween()
        tween.tween_property($RoofLayer, "modulate:a", 0.0 if in_house else 1.0, 0.5)

var door_cell_coord: Vector2i   # Grid coordinate of the door tile (found in _ready)

func _ready() -> void:
    # Scan wall tiles to find the door and auto-generate the floor
    for cell in $WallsLayer.get_used_cells():
        # Copy each wall tile position to floor layer (floor fills the same footprint as walls)
        $FloorLayer.set_cell(cell, 0, Vector2i.ZERO)
        # The door tile has atlas coords (0,4) — record its position for the setter above
        if $WallsLayer.get_cell_atlas_coords(cell) == Vector2i(0, 4):
            door_cell_coord = cell

func _on_house_area_body_entered(_body: Node2D) -> void:
    in_house = true    # Triggers setter → roof fades out, door opens

func _on_house_area_body_exited(_body: Node2D) -> void:
    in_house = false   # Triggers setter → roof fades in, door closes
```

---

## scenes/levels/bed.gd & tv.gd
> **bed.gd Screen:** Interacting with bed → day changes (Tab key OR RayCast)
> **tv.gd Screen:** Interacting with TV → shows rain/sun forecast animation

```gdscript
# bed.gd
extends StaticBody2D

func interact(player: CharacterBody2D):
    # Player presses action while facing bed → emit day_change to trigger level_reset sequence
    player.day_change_emit()
```

```gdscript
# tv.gd
extends StaticBody2D

func interact(_player):
    # Play the forecast animation (rain clouds or sun) then return to default idle
    $AnimatedSprite2D.play("rain" if Data.forecast_rain else 'sun')
    $Timer.start()   # Timer duration determines how long forecast shows

func _on_timer_timeout() -> void:
    $AnimatedSprite2D.play("default")   # Return to off/idle state
```

---

## Shaders

### shaders/circle_transition.gdshader
> **Screen:** The black circle that closes/opens between days. Covers the whole screen.

```glsl
shader_type canvas_item;

// progress: 0.0=fully open (no black), 1.0=fully closed (all black)
// Animated by tween in level.gd: 0→1 to close, 1→0 to open
uniform float progress : hint_range(0.0, 1.0);

void fragment() {
    // Fix for non-square viewports: the UV space is rectangular but we want a circle
    // ratio = how much taller than wide the viewport is (e.g. 0.5625 for 16:9)
    float ratio = SCREEN_PIXEL_SIZE.y / SCREEN_PIXEL_SIZE.x;

    // Squish the UV horizontally by the ratio so the distance calculation produces a circle
    vec2 adjusted_uv = vec2(mix(0.5, UV.x, ratio), UV.y);

    // Distance from this pixel to the center (0.5, 0.5)
    float circle = distance(vec2(0.5), adjusted_uv);

    // step(edge, x): returns 0 if x < edge, 1 if x >= edge
    // 1.5 - progress*1.5: shrinks the cutoff radius as progress increases
    // At progress=0: cutoff=1.5 (all pixels pass → fully transparent)
    // At progress=1: cutoff=0.0 (all pixels fail → fully opaque black)
    float alpha = step(circle, 1.5 - progress * 1.5);
    COLOR.a = alpha;
}
```

### shaders/flash.tres (Visual Shader — equivalent GLSL)
> **Screen:** The white flash on any FlashSprite2D — trees, blobs, plants.

```glsl
// Fragment shader equivalent of the VisualShader nodes in flash.tres:
void fragment() {
    vec4 original = COLOR;        // Input node: original texture color
    vec4 white = vec4(1.0);       // ColorParameter "Color" (default=white)
    float t = Progress;           // FloatParameter "Progress" range(0,1)
    // Mix: original color at t=0, pure white at t=1
    COLOR.rgb = mix(original.rgb, white.rgb, t);
    // Keep original alpha unchanged
}
```
