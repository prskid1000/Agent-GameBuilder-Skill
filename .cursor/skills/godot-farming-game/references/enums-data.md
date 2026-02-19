# Enums & Data Globals Reference

## global/enums.gd — Full Source

```gdscript
extends Node

enum Style  { BASIC, COWBOY, ENGLISH, BASEBALL, BEANIE, STRAW }
enum State  { DEFAULT, FISHING, BUILDING, SHOP }
enum Tool   { AXE, HOE, SWORD, WATER, FISH, SEED }
enum Machine{ SPRINKLER, FISHER, SCARECROW, DELETE }
enum Seed   { TOMATO, CORN, PUMPKIN, WHEAT }
enum Item   { WOOD, APPLE, TOMATO, CORN, WHEAT, PUMPKIN, FISH }
enum Shop   { MAIN, HAT }
```

**Integer values (for reference — use names, not integers in code):**
- Tool: AXE=0, HOE=1, SWORD=2, WATER=3, FISH=4, SEED=5
- Machine: SPRINKLER=0, FISHER=1, SCARECROW=2, DELETE=3
- Seed: TOMATO=0, CORN=1, PUMPKIN=2, WHEAT=3

---

## global/data.gd — Full Source

```gdscript
extends Node

const PLAYER_SKINS = {
    Enum.Style.BASIC:    preload("res://graphics/characters/main/main_basic.png"),
    Enum.Style.BASEBALL: preload("res://graphics/characters/main/main_blue.png"),
    Enum.Style.COWBOY:   preload("res://graphics/characters/main/main_cowboy.png"),
    Enum.Style.ENGLISH:  preload("res://graphics/characters/main/main_grey.png"),
    Enum.Style.STRAW:    preload("res://graphics/characters/main/main_straw.png"),
    Enum.Style.BEANIE:   preload("res://graphics/characters/main/main_red.png"),
}

const TILE_SIZE = 16

const PLANT_DATA = {
    Enum.Seed.TOMATO: {
        'texture':      "res://graphics/plants/tomato.png",
        'icon_texture': "res://graphics/icons/tomato.png",
        'name':         'Tomato',
        'h_frames':     3,
        'grow_speed':   0.6,
        'death_max':    3,
        'reward':       Enum.Item.TOMATO,
    },
    Enum.Seed.CORN: {
        'texture':      "res://graphics/plants/corn.png",
        'icon_texture': "res://graphics/icons/corn.png",
        'name':         'Corn',
        'h_frames':     3,
        'grow_speed':   1.0,
        'death_max':    2,
        'reward':       Enum.Item.CORN,
    },
    Enum.Seed.PUMPKIN: {
        'texture':      "res://graphics/plants/pumpkin.png",
        'icon_texture': "res://graphics/icons/pumpkin.png",
        'name':         'Pumpkin',
        'h_frames':     3,
        'grow_speed':   0.3,
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

const HOUSE_COST = {
    1: { Enum.Item.WOOD: 30, Enum.Item.APPLE: 20 },
    2: { Enum.Item.WOOD: 40, Enum.Item.APPLE: 30 },
}

const STYLE_UPGRADES = {
    Enum.Style.COWBOY:   { 'name': 'Cowboy',   'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/cowboy.png") },
    Enum.Style.ENGLISH:  { 'name': 'Oldie',    'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/english.png") },
    Enum.Style.BASEBALL: { 'name': 'Baseball', 'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/blue.png") },
    Enum.Style.BEANIE:   { 'name': 'Beanie',   'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/beanie.png") },
    Enum.Style.STRAW:    { 'name': 'Straw',    'cost': { Enum.Item.WOOD: 8, Enum.Item.WHEAT: 6 }, 'icon': preload("res://graphics/icons/straw.png") },
}

# Keys = Enum.Tool values, Values = AnimationTree BlendSpace2D node names
const TOOL_STATE_ANIMATIONS = {
    Enum.Tool.HOE:   'Hoe',
    Enum.Tool.AXE:   'Axe',
    Enum.Tool.WATER: 'Water',
    Enum.Tool.SWORD: 'Sword',
    Enum.Tool.FISH:  'Fish',
    Enum.Tool.SEED:  'Seed',
}

var forecast_rain: bool
```

---

## How Enums Work in GDScript

```gdscript
# Correct — use enum name
var current_tool: Enum.Tool = Enum.Tool.AXE

# Cycle forward/back safely (never goes out of bounds)
current_tool = posmod(current_tool + int(dir), Enum.Tool.size()) as Enum.Tool

# Match statement with enum
match current_tool:
    Enum.Tool.HOE:   create_soil()
    Enum.Tool.WATER: water_soil()
    Enum.Tool.FISH:  start_fishing()
```

**Why enums:** Prevent typos (GDScript autocompletes), safer than strings, IDE warns on invalid values.

---

## TOOL_STATE_ANIMATIONS — How It's Used

```gdscript
# In player.gd — travel to correct tool blend space
tool_state_machine.travel(Data.TOOL_STATE_ANIMATIONS[current_tool])

# In animate() — update blend position for every tool animation
for animation in Data.TOOL_STATE_ANIMATIONS.values():
    var animation_name = "parameters/ToolStateMachine/" + animation + "/blend_position"
    $Animation/AnimationTree.set(animation_name, direction_animation)
```

The dictionary string values (e.g. `"Axe"`, `"Hoe"`) must exactly match the
BlendSpace2D node names inside the `ToolStateMachine` in the AnimationTree editor.
