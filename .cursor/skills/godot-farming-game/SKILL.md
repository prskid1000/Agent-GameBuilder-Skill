---
name: godot-farming-game
description: >
  Creates a Godot 4 top-down farming game (Stardew Valley style) step by step,
  including farming, fishing, combat, machines, day/night cycle, plants, resources,
  and UI. Based on the .examples/godot-valley project (GodewValley). Use when the
  user wants to create a Godot game similar to the sample project, build farming
  game mechanics, or recreate features from the tutorial. When Godot API or
  how-to details are needed, use the project's @.docs (Godot engine docs). Can
  generate independent, complete ComfyUI prompts for assets (OpenDUI, Flux Kontext,
  Chatterbox TTS).
---

# Godot Farming Game Skill

Builds a complete Godot 4 farming / life-sim game matching `.examples/godot-valley`
(GodewValley). The agent generates ~95% of all code and scene structure.

## Quick References

- **[Step-by-Step Build Guide — START HERE](references/step-by-step-guide.md)**
- [Project Config & Input Map](references/project-config.md)
- [Enums & Data Globals](references/enums-data.md)
- [All Scripts with Comments](references/scripts.md)
- [All Scene Trees](references/scenes.md)
- [All .tscn Files](references/scene-files.md)
- [Asset Paths + Audio](references/assets.md)
- [Asset Prompts for ComfyUI](references/asset-prompts-comfyui.md)
- [Godot Concepts Used](references/godot-concepts.md)
- [Screen-by-Screen Guide](references/screen-by-screen.md)

## Example project

Run `.examples/godot-valley/project.godot` in Godot 4.6 to see the finished game.

## Using @.docs

Look up Godot APIs in `.docs/godot-docs-md/`:
- `classes/class_*.md` — class reference (TileMapLayer, AnimationTree, GPUParticles2D…)
- `tutorials/` — step-by-step guides

Do not guess API behavior; look it up and cite when relevant.
---


## Incremental verification (required)

After every step the game must run cleanly:
1. Run project (F5) — confirm main scene loads.
2. No runtime or parse errors in Output/Debugger.
3. New behavior is testable (player moves, tools work, plants grow, etc.).
If something breaks, fix it in the current step before adding the next. Never leave the project in a broken state at the end of a step.

---


Fix errors before proceeding to the next step.

## Asset prompt generation (ComfyUI)

Generate **independent, complete** prompts for:
- **OpenDUI / OpenDiT** — sprites, tiles, plants, UI art.
- **Flux Kontext** — image edit / style transfer / character variants.
- **Chatterbox TTS** — NPC dialogue, barks, narration.

One prompt per asset; no "same as above". Full rules: [Asset Prompts](references/asset-prompts-comfyui.md).

## Build Steps (summary — full detail in step-by-step-guide.md)

| Step | What gets built | Verify |
|------|----------------|--------|
| 1 | Project setup, input map, physics layers | F5 runs, no errors |
| 2 | Enum + Data autoloads | No parse errors |
| 3 | Player scene + movement | Player moves with WASD |
| 4 | AnimationTree (editor-only) | Idle/walk/tool animations play |
| 5 | Level scene + TileMaps | Level loads, player on map |
| 6 | Objects (plant, tree, blob, machines, VFX) | Tools affect world, blobs spawn |
| 7 | Flash + circle-wipe shaders | Hit flash and day transition work |
| 8 | UI scenes (tool bar, fishing, plant info) | UI visible and responsive |
| 9 | PlantResource | Planting, growing, harvesting work |
| 10 | House scene (roof fade, bed, TV) | Enter house, use bed |
| 11 | Day/night cycle | Day timer, color, rain, level reset |
| 12 | Final level layout | Full playthrough without errors |

## User-Only Editor Steps

These must be done by hand in the Godot editor (cannot be scripted):
- **AnimationTree** — BlendTree, BlendSpace2D, OneShot nodes, transitions
- **TileMaps** — paint terrain, custom data (farmable, coast), Z-index
- **Daytime Gradient** — set on Level node export (4 color stops)
- **Theme** — font, StyleBoxTexture for PanelContainer
- **Collision shapes** — CapsuleShape2D per scene, tuned per character
- **Particle systems** — rain floor + drops, emitting=false by default

Full click-by-click instructions for every editor step: [step-by-step-guide.md → User-Only Editor Tweaks](references/step-by-step-guide.md).

**Agent produces:**
- `project.godot` with all settings below

**Settings to apply:**
```
[application]
config/name="YourGameName"
run/main_scene="res://scenes/levels/level.tscn"
config/features=PackedStringArray("4.6", "Forward Plus")

[display]
window/size/viewport_width=1920
window/size/viewport_height=1080

[rendering]
textures/canvas_textures/default_texture_filter=0   # Nearest (pixel art)

[autoload]
Enum="*res://global/enums.gd"
Data="*res://global/data.gd"

[layer_names]
2d_physics/layer_1="Terrain"
2d_physics/layer_2="Player"
2d_physics/layer_3="Objects"
2d_physics/layer_4="Characters"
```

**Input map** (full list in [project-config.md](references/project-config.md)):
`left/right/up/down`, `action` (Space/A), `tool_forward` (E), `tool_backward` (Q),
`seed_forward` (C), `style_toggle` (T), `day_change` (Tab), `build` (M), `diagnose` (N)

**User tweak:** Window size — change to `1280x720` if 1920x1080 is too large for your screen.

**Verify:** Run project (F5). Main scene loads (use a minimal placeholder scene if level not ready). No errors.

---

### Step 2 — Global Scripts (Autoloads)

**Agent produces:** `global/enums.gd` and `global/data.gd`

See full source in [enums-data.md](references/enums-data.md).

Key enums: `Style`, `State`, `Tool`, `Machine`, `Seed`, `Item`, `Shop`
Key data constants: `PLAYER_SKINS`, `TILE_SIZE=16`, `PLANT_DATA`, `MACHINE_UPGRADE_COST`, `TOOL_STATE_ANIMATIONS`

**Verify:** Run project. No script parse errors; Enum and Data autoload without error.

---

### Step 3 — Player Scene

**Agent produces:** `scenes/characters/player.tscn` + `player.gd`

Scene tree:
```
CharacterBody2D (player.gd, group: "Player")
  Sprite2D
  CollisionShape2D (CapsuleShape2D r=4 h=8)
  Camera2D (zoom=4)
  RayCast2D (target=(0,20))
  Animation/
    AnimationPlayer    ← all tool/move/idle animations
    AnimationTree      ← blend tree controlling AnimationPlayer
  ToolUI (instance: tool_ui.tscn)
  FishingGame (instance: fishing_game.tscn)
```

Key variables: `direction`, `last_direction`, `speed=50`, `can_move`, `current_tool`,
`current_seed`, `current_state`, `current_style`, `current_machine`

Signals emitted: `tool_use(tool, pos)`, `diagnose`, `day_change`, `build(machine)`, `machine_change(machine)`

Full script in [scripts.md → player.gd](references/scripts.md).

**User tweak (AnimationTree):** See Step 4 below for editor-only animation tree setup.

**Verify:** Run game with level containing Player. Player moves with WASD; tool cycling (Q/E) and action (Space) don’t error. Fix any missing node paths or AnimationTree refs.

---

### Step 4 — AnimationTree Setup

**This step is editor-only** — the AnimationTree cannot be fully scripted.

See **[User-Only Editor Tweaks → AnimationTree](#animationtree)** for exact click-by-click instructions.

Summary of what to build:
- Root: **BlendTree**
- Inside BlendTree: `MoveStateMachine` (BlendSpace2D states) → `ToolOneShot` (OneShot) → `Output`
- `ToolOneShot`: in=MoveStateMachine, shot=ToolStateMachine
- `MoveStateMachine`: states = `Idle` (BlendSpace2D) + `Walk` (BlendSpace2D), transitions both ways (non-auto)
- Each BlendSpace2D: 9 points (4 cardinals + 4 diagonals + center) with direction animations

`Data.TOOL_STATE_ANIMATIONS` keys match the BlendSpace2D node names in ToolStateMachine.

**Verify:** After editor setup, run game. Idle/walk and tool animations play correctly; no animation tree errors.

---

### Step 5 — Level Scene

**Agent produces:** `scenes/levels/level.tscn` + `level.gd`

Scene tree:
```
Node2D "Level" (level.gd)
  Layers/
    WaterLayer       (TileMapLayer)
    GrassLayer       (TileMapLayer, collision layer 1=Terrain)
    SoilLayer        (TileMapLayer)
    SoilWaterLayer   (TileMapLayer)
    RainFloorParticles (GPUParticles2D)
  Objects/
    Player           (instance player.tscn)
    ScareCrow        (instance scare_crow.tscn)
    House            (instance house.tscn)
    Tree, Tree2...   (instance tree.tscn ×N)
    SimpleObject...  (instance simple_object.tscn ×N)
  Overlay/
    DayTimeColor     (CanvasModulate)
    CanvasLayer/
      DayTransitionLayer (ColorRect + circle_transition shader)
      PlantInfoContainer (instance plant_info_container.tscn)
    RainDropsParticles (GPUParticles2D)
    MachinePreviewSprite (Sprite2D)
  Timers/
    DayTimer         (Timer, wait=120, one_shot=true, autostart=true)
    BlobTimer        (Timer, wait=20, autostart=true)
  BlobSpawnPositions/ (Marker2D nodes ×11)
```

**Exports on Level node:** `daytime_color: Gradient`, `rain_color: Color`

Full script in [scripts.md → level.gd](references/scripts.md).

**User tweak:** Paint TileMaps in editor — see [User-Only Editor Tweaks → TileMaps](#tilemaps).

**Verify:** Run game. Level loads; player is on the level; day timer and gradient work if wired. No missing node or script errors.

---

### Step 6 — Object Scenes

**Agent produces all scripts + scene files:**

| Scene | Root Node | Script |
|-------|-----------|--------|
| `scenes/objects/plant.tscn` | StaticBody2D | plant.gd |
| `scenes/objects/tree.tscn` | StaticBody2D | tree.gd |
| `scenes/objects/simple_object.tscn` | StaticBody2D | simple_object.gd |
| `scenes/objects/blob.tscn` | CharacterBody2D | blob.gd |
| `scenes/vfx/flash_sprite_2d.tscn` | Sprite2D | flash_sprite_2d.gd |
| `scenes/machines/machine.tscn` | StaticBody2D (base class) | machine.gd |
| `scenes/machines/sprinkler.tscn` | extends Machine | sprinkler.gd |
| `scenes/machines/scare_crow.tscn` | extends Machine | scare_crow.gd |
| `scenes/machines/fisher.tscn` | extends Machine | fisher.gd |
| `scenes/machines/projectile.tscn` | Area2D | projectile.gd |

Groups: `"Objects"` → tree, blob, simple_object; `"Plants"` → plant; `"Machines"` → all machines; `"Player"` → player; `"Blobs"` → blob

Full scripts in [scripts.md](references/scripts.md). Full scene trees in [scenes.md](references/scenes.md).

**Verify:** Run game. Hoe/water/seed on soil, axe/sword on objects; plants and objects respond. Blobs spawn and move. No errors.

---

### Step 7 — Flash Shader

**Agent produces:** `shaders/flash.tres` (VisualShader) + `shaders/circle_transition.gdshader`

Flash shader: mixes original color with white via `Progress` parameter (0→1).
Enable **Local to Scene** on the ShaderMaterial so each object flashes independently.

Circle transition shader: draws expanding circle wipe using UV distance + `progress` uniform.
See full GLSL in [scripts.md → shaders](references/scripts.md).

**Verify:** Run game. Hit a tree/blob or harvest plant; flash effect plays. Day transition circle works when triggered. No shader/material errors.

---

### Step 8 — UI Scenes

**Agent produces:**

| Scene | Purpose |
|-------|---------|
| `scenes/ui/tool_ui.tscn` + `tool_ui.gd` | HBoxContainer showing current tool/seed icons |
| `scenes/ui/tool_ui_texture.tscn` + `tool_ui_texture.gd` | Single icon that scales when selected |
| `scenes/ui/fishing_game.tscn` + `fishing_game.gd` | Bar+fish minigame overlay |
| `scenes/ui/plant_info.tscn` + `plant_info.gd` | Panel showing plant name, growth bar, death bar |
| `scenes/ui/plant_info_container.tscn` + `plant_info_container.gd` | ScrollContainer holding all plant_info panels |
| `scenes/ui/game_theme.tres` | Theme: HomeVideo-Regular font, frame.png StyleBoxTexture |

Full scripts in [scripts.md](references/scripts.md). Full scene trees in [scenes.md](references/scenes.md).

**Verify:** Run game. Tool/seed UI shows and highlights; plant info panels appear for planted crops; fishing minigame opens at coast. No UI or missing-scene errors.

---

### Step 9 — Plant Resource

**Agent produces:** `resources/plant_res.gd`

```gdscript
class_name PlantResource extends Resource
```

Key exported vars: `texture`, `icon_texture`, `grow_speed`, `h_frames`, `death_max`, `name`
Runtime vars: `age`, `death_count`, `dead`

Methods: `setup(seed_enum)`, `grow(sprite)`, `decay(plant)`, `get_complete()`, `damage()`

Emits `changed` signal on `death_count`, `dead` set — used by plant_info to update bars.

**Verify:** (Covered by Step 6/8.) Planting, growing, watering, and harvesting update plant state and UI; no resource errors.

---

### Step 10 — House Scene

**Agent produces:** `scenes/levels/house.tscn` + `house.gd`

Uses `HouseTileSet.tres` (premade). Roof fades out when player enters.
Contains `tv.tscn` (AnimatedSprite2D showing rain/sun forecast) and `bed.tscn` (triggers day change).

**Verify:** Run game. Enter house; roof fades. Use bed; day transition plays and level resets. No errors.

---

### Step 11 — Day/Night Cycle

Already wired in `level.gd`. Key logic:
- `DayTimer` (120s) drives `daytime_color.sample(1 - time_left/wait_time)`
- `day_restart()` tweens `circle_transition progress` 0→1, calls `level_reset()`, then 1→0
- `level_reset()`: grows plants, clears soil water, restarts timer, resets objects, applies rain

**Verify:** Run game. Day/night color and timer advance; sleeping triggers full day cycle and plant growth; no errors.

---

### Step 12 — Final Level Layout

Place in editor: Trees (×31), SimpleObjects (×37), House, ScareCrow, BlobSpawnPositions (×11 Marker2Ds).
Paint GrassLayer terrain, WaterLayer tiles, SoilLayer terrain (for testing).
See [scenes.md → level positions](references/scenes.md) for exact coordinates from `.example`.

**Verify:** Run full playthrough. Move, farm, fish, fight blobs, sleep; all systems work. No errors. Fix any remaining missing assets or node paths.

---

## User-Only Editor Tweaks

These ~5% steps must be done by hand in the Godot editor after code is generated.

### AnimationTree

**Where:** Player scene → Animation/AnimationTree node → open editor

**What to build:**
1. Inspector → Tree Root → BlendTree
2. Right-click canvas → Add State Machine → name `MoveStateMachine` → connect to Output
3. Right-click → Add OneShot → name `ToolOneShot` → In = MoveStateMachine, Shot = ToolStateMachine → connect to Output
4. Open MoveStateMachine → right-click → Add BlendSpace2D → name `Idle`; repeat for `Walk`
5. Connect Start → Idle (auto). Add non-auto arrows: Idle↔Walk (both directions, gray arrows)
6. Open each BlendSpace2D → right-click → Add Animation at positions:
   - Center (0,0), Right (1,0), Left (-1,0), Up (0,-1), Down (0,1) + 4 diagonals
   - Pick corresponding animation name (e.g. `idle_right`, `walk_down`, etc.)
7. Open ToolStateMachine (already in premade AnimationTree) → verify Start connects to each tool's BlendSpace2D with auto-transition
8. Inspector → AnimationTree → Anim Player = `Animation/AnimationPlayer`

**Key gotcha:** BlendSpace2D crosshair must be on EXACT point (not just close). Set blend_position to `Vector2(0,0)` in Inspector for each state initially.

### TileMaps

**Where:** Level scene → select each TileMapLayer

**GrassLayer:**
1. Inspector → TileSet → New TileSet → drag `graphics/tilesets/grass.png` → Create Atlas
2. TileSet tab → Terrain Sets → Add Element → Match Corners & Sides → Add terrain "grass" inside it
3. Select tab → Physics Layer → Add Element → Collision Layer 1 (Terrain), no mask
4. Paint tab → Terrains → paint terrain connections on all tiles (corners, sides, center variants)
5. Set low-probability tiles probability=0.1 for variation
6. Custom Data: Add layer `farmable` (bool) → paint `true` on interior/full tiles only

**SoilLayer:** Same process with `graphics/tilesets/soil.png`, terrain "soil"

**WaterLayer:**
1. Drag `graphics/tilesets/water.png` → No atlas
2. Select the single leftmost tile → Animation tab → Columns=4 → Add 4 frames each 0.4s duration

**SoilWaterLayer:** Drag `graphics/tilesets/soil_water.png` → Atlas (3 tiles, no terrain needed)

**GrassLayer coast custom data:**
- Tile custom data layer: name `coast`, type `Vector2i`
- Paint coast direction (e.g. `Vector2i.DOWN`, `Vector2i.LEFT`) on water-adjacent tiles
- Used by fisher.gd to know which way to face

### Z-Index & Y-Sort

- All TileMapLayer nodes: Ordering → Z Index = **-2**
- Objects/ Node2D: Ordering → **Y Sort Enabled = true**
- SimpleObject: Z Index = -1 if size < 2 (handled in script), else 0

### Theme (game_theme.tres)

1. Open `scenes/ui/game_theme.tres`
2. Label → Font → FontVariation → set `graphics/fonts/HomeVideo-Regular.ttf`, size=30, extra spacing glyph=1
3. Label → Font Color = `#060606`
4. PanelContainer → Styles → Panel → StyleBoxTexture → texture = `graphics/ui/frame.png` → margins=6 all sides

### AnimationPlayer (player.tscn)

- All tool animations call `tool_use_emit()` at the correct frame via a Method track
- `idle_down` is set to autoplay
- Each animation has `loop_mode=1` for idle/walk, `loop_mode=0` for tool animations
- Call `day_change_emit()` in bed.gd interact → already done in script

### Collision Shapes

- GrassLayer physics shapes: use the 3-dot menu to flip/rotate (R=rotate, H=flip horizontal, V=flip vertical)
- Player CollisionShape: CapsuleShape2D, radius=4, height=8 (keep short so player fits between plants)
- Plant CollisionShape: CapsuleShape2D (short, ~r=4 h=6)
- Blob CollisionShape: CircleShape2D r=6, on layer 3 (Objects), mask 1 (Terrain)
- Tree CollisionShape: CapsuleShape2D r=8 h=22, Y offset=4

### Daytime Gradient

Level node → Export `daytime_color` Gradient:
- 0.0 → `#EDD0CF` (warm morning)
- 0.29 → white `#FFFFFF`
- 0.48 → white `#FFFFFF`
- 1.0 → `#5E77FF` (night blue)

Export `rain_color`: a desaturated blue-gray (e.g. `#8899AA`)

### Particle Systems

**RainFloorParticles** (Layers/) and **RainDropsParticles** (Overlay/): set `emitting=false` by default. They are toggled in `level.gd` via the `raining` setter.

Configure particle materials with downward velocity + spread for rain effect.
Texture: `graphics/weather/floor.png` and `graphics/weather/drops.png`.
