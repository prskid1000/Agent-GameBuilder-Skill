# Screen-by-Screen Guide
# What you see → which script/node is driving it

This file maps every visual element you see on screen to the exact node, script, and
function responsible for it. Use it when something looks wrong or you want to modify a specific thing.

---

## The Main Level Screen

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ [Plant Info Sidebar]         [Day Color Tint - whole screen]                │
│                                                                             │
│  🌱 Tomato  [====   ]        [Trees scattered around]                       │
│  🌽 Corn    [=======]        [Rocks/Bushes scattered]                       │
│  🎃 Pumpkin [==     ]                                                       │
│                              [Grass terrain with coast]                     │
│                              [Soil patches where hoe used]                  │
│  (scroll)                    [Water patches (watered soil)]                 │
│                              [Animated water tiles at edges]                │
│                                                                             │
│                              [Player sprite]     ← facing direction         │
│                              [Tool UI above player]                         │
│                                                                             │
│                              [House with roof]                              │
│                              [Scarecrow machine]                            │
│                                                                             │
│                       [Machine placement preview icon]                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Element Map

### 🌅 Day Color Tint (whole screen color shift)
- **Node:** `Level → Overlay → DayTimeColor` (CanvasModulate)
- **Script:** `level.gd → _process()` — runs every frame
- **How:** `daytime_color.sample(daytime_point)` samples a Gradient over the 120s day timer
- **Modify:** Change the `daytime_color` Gradient export on the Level node in Inspector
- **Morning** → warm pinkish (`#EDD0CF`), **Midday** → white, **Evening** → blue (`#5E77FF`)

---

### 🌧️ Rain Effect
- **Particles:** `Level → Layers → RainFloorParticles` + `Level → Overlay → RainDropsParticles`
- **Script:** `level.gd → raining` setter — toggling `raining=true` starts both particle systems
- **When toggled:** At the start of `level_reset()` — `raining = Data.forecast_rain`
- **Forecast decided:** `_ready()` (first day) and at end of each `level_reset()`

---

### 🌱 Grass Terrain (ground)
- **Node:** `Level → Layers → GrassLayer` (TileMapLayer)
- **Script:** None — painted entirely in editor
- **Farmable tiles:** Custom data layer `farmable=true` — checked by `level.gd` when HOE is used
- **Coast tiles:** Custom data layer `coast=Vector2i` — read by `fisher.gd` to set facing direction
- **Collision:** Physics layer painted on coast tiles — stops player walking into water

---

### 🟫 Soil Patches (dark brown tiles after hoeing)
- **Node:** `Level → Layers → SoilLayer` (TileMapLayer)
- **Script:** `level.gd → _on_player_tool_use()` when `tool == Enum.Tool.HOE`
- **Code:** `$Layers/SoilLayer.set_cells_terrain_connect([grid_coord], 0, 0)`
- **Condition:** GrassLayer tile at that coord must have `farmable=true`

---

### 💧 Water Patches (blue patches on soil after watering)
- **Node:** `Level → Layers → SoilWaterLayer` (TileMapLayer)
- **Script:** `level.gd → _on_player_tool_use()` when `tool == Enum.Tool.WATER`
- **Code:** `$Layers/SoilWaterLayer.set_cell(grid_coord, 0, Vector2i(randi_range(0,2), 0))`
- **Cleared:** `level.gd → level_reset()` calls `$Layers/SoilWaterLayer.clear()` each day
- **Also added by:** Sprinkler machine (`sprinkler.gd`), rain during HOE or day reset

---

### 🌊 Animated Water Tiles
- **Node:** `Level → Layers → WaterLayer` (TileMapLayer)
- **Script:** None — animation is configured in TileSet editor (4 frames × 0.4s each)
- **Painted:** Fully in editor, covers all non-grass areas
- **Z-Index:** -2 (always behind everything)

---

### 🌳 Trees
- **Node:** `Level → Objects → Tree` ... `Tree31` (instances of `scenes/objects/tree.tscn`)
- **Script:** `tree.gd`
- **On screen:** Tree sprite with randomly placed apples. Stump when health=0.
- **Randomization:** `_ready()` picks frame 0 or 1 randomly (two tree variants)
- **Hit:** `tree.gd → hit(tool)` — only responds to AXE → flashes + apple falls + health-1
- **Stump transition:** `health` setter swaps sprite, resizes collision shape
- **Day reset:** `tree.gd → reset()` — respawn apples, restore health (if alive)

---

### 🪨 Rocks & Bushes (SimpleObjects)
- **Node:** `Level → Objects → SimpleObject` ... `SimpleObject37`
- **Script:** `simple_object.gd` (`@tool` script)
- **On screen:** Small/large bush or rock sprite scattered around the map
- **Randomization:** `random=true` export → picks random size/style in `_ready()`
- **Editor live preview:** Change `size` or `style` in Inspector → sprite updates immediately
- **Z-Index:** -1 if size<2 (small = behind player), 0 if size≥2 (large = in front)
- **Collision:** Disabled for small objects (size<2) — player walks through them

---

### 🏠 House
- **Node:** `Level → Objects → House` (instance of `scenes/levels/house.tscn`)
- **Script:** `house.gd`
- **On screen:** House with walls, floor, and a roof that fades out when player enters
- **Roof fade:** `house.gd → in_house` setter tweens `$RoofLayer.modulate.a` 1→0 (enter) or 0→1 (exit)
- **Door:** WallsLayer cell at `door_cell_coord` switches atlas tile when entering/exiting
- **Inside:** TV (forecast) and Bed (day change) — both are StaticBody2D with `interact()` function
- **TV:** `tv.gd → interact()` plays rain or sun animation based on `Data.forecast_rain`
- **Bed:** `bed.gd → interact()` calls `player.day_change_emit()` → triggers `level.day_restart()`

---

### 👤 Player Character
- **Node:** `Level → Objects → Player` (instance of `scenes/characters/player.tscn`)
- **Script:** `player.gd`
- **On screen:** The controllable character sprite + tool animation + hat style
- **Sprite:** `Sprite2D` with 33×4 frame spritesheet — frame changed by AnimationPlayer
- **Movement:** `player.gd → move()` reads WASD → `move_and_slide()`
- **Animation:** `player.gd → animate()` updates AnimationTree blend positions each frame
- **Skin swap:** T key → `current_style` cycles → `$Sprite2D.texture = Data.PLAYER_SKINS[style]`
- **Can't move while using tool:** `_on_animation_tree_animation_started` sets `can_move=false`

---

### 🔧 Tool UI (icon row above player)
- **Node:** Inside `player.tscn → ToolUI` (instance of `scenes/ui/tool_ui.tscn`)
- **Script:** `tool_ui.gd` + `tool_ui_texture.gd`
- **On screen:** Row of 6 tool icons OR 4 seed icons that slides in when Q/E/C pressed
- **Appear:** `player.gd` calls `$ToolUI.reveal(true/false)` when tool/seed changes
- **Highlight:** Selected icon tweens to 20×20px, others stay at 16×16px
- **Auto-hide:** `HideTimer` (1 second) hides all containers after no interaction

---

### 🎣 Fishing Minigame Overlay
- **Node:** Inside `player.tscn → FishingGame` (instance of `scenes/ui/fishing_game.tscn`)
- **Script:** `fishing_game.gd`
- **On screen:** Vertical bar (gravity pulls it down) + fish icon (bounces randomly) + progress bar
- **Appears:** `player.gd → start_fishing()` calls `$FishingGame.reveal()`
- **Controls:** Space key → `fishing_game.gd → action()` → applies -25 upward velocity to bar
- **Fish:** Changes direction every 1–3 seconds (FishUpdateTimer)
- **Win/Lose:** Progress bar reaches 100 or 0 → `stop_fishing()` called on player
- **Physics:** Pure math in `_process()` — no physics engine used

---

### 🌱 Plant Sprites (growing crops)
- **Node:** Dynamically added to `Level → Objects` when SEED tool is used
- **Script:** `plant.gd` (StaticBody2D) + `plant_res.gd` (Resource)
- **On screen:** 3-frame spritesheet (seedling → growing → mature), centered in soil tile
- **Growth:** `level_reset()` calls `plant.grow(watered)` → `res.grow(sprite)` → `sprite.frame = int(age)`
- **Harvest:** Player walks into CollisionArea → `res.get_complete()` → flash → `queue_free()`
- **Death:** Not watered `death_max` times → `res.decay(self)` → `queue_free()`
- **Flash on harvest:** `$FlashSprite2D.flash(0.2, 0.4, queue_free)` — white then disappears

---

### 📊 Plant Info Sidebar (left side)
- **Node:** `Level → Overlay → CanvasLayer → PlantInfoContainer`
- **Script:** `plant_info_container.gd` + `plant_info.gd`
- **On screen:** Scroll container with one panel per living plant. Each shows name, icon, two bars.
- **Green bar:** Growth progress (`res.age / res.h_frames`)
- **Red bar:** Death counter (`res.death_count / res.death_max`)
- **Created:** `level.gd` instantiates one panel when SEED plants a crop
- **Updated:** `level_reset()` calls `update_all()` → each panel reads from shared resource
- **Removed:** When `res.death_count >= res.death_max` OR when plant harvested (`res.dead=true`)
- **Toggle visible:** N key → `level._on_player_diagnose()` flips `.visible`

---

### 🔵 Blob Enemy
- **Node:** Dynamically added to `Level → Objects` every 20 seconds (BlobTimer)
- **Script:** `blob.gd`
- **On screen:** Blue blob character moving toward a random plant
- **Spawn:** `level.gd → _on_blob_timer_timeout()` → picks random spawn point + random plant target
- **Movement:** `_physics_process()` normalizes direction to plant → `move_and_slide()`
- **Hit:** Sword → `hit()` → flash + knockback tween + health-1
- **Death:** health=0 → `death()` → stop moving, play explode animation → `queue_free()` at animation end
- **Damages plant:** Reaches plant (distance<10) → `plant_target.damage()` → `res.damage()`

---

### ⚙️ Machine Placement Preview
- **Node:** `Level → Overlay → MachinePreviewSprite` (Sprite2D)
- **Script:** `level.gd → _process()` — updates every frame
- **On screen:** Icon floating one tile ahead of player while in BUILD mode (M key)
- **Shows:** Current machine icon from `MACHINE_PREVIEW_TEXTURES` dict
- **Position:** `player.get_machine_coord()` + machine's visual offset
- **Visibility:** Only when `player.current_state == Enum.State.BUILDING`

---

### 🚿 Sprinkler Machine
- **Node:** Dynamically added to `Level → Objects` when built in BUILD mode
- **Script:** `sprinkler.gd` (extends Machine)
- **On screen:** Animated sprinkler sprite, water particle burst, 3×3 area of soil gets watered
- **Timer:** Fires every ~30 seconds → `_on_timer_timeout()` → animation + emit `water_plants`
- **Effect:** `level.water_plants(coord)` → writes water tiles to SoilWaterLayer in 8 directions

---

### 🐟 Fisher Machine
- **Node:** Dynamically added to `Level → Objects` when built on a coast tile
- **Script:** `fisher.gd` (extends Machine)
- **On screen:** Directional animated fisher sprite, progress bar (fishing cooldown)
- **Direction:** Reads `coast` custom data from GrassLayer tile at placement position
- **Animation:** Cast → idle → wait → cast again cycle
- **Progress bar:** `_process()` updates `TextureProgressBar.value` based on timer

---

### 🔫 Scarecrow Machine
- **Node:** Pre-placed in `Level → Objects → ScareCrow` (not built by player in base version)
- **Script:** `scare_crow.gd` (extends Machine)
- **On screen:** Static scarecrow sprite, projectiles fly out when blobs are nearby
- **Logic:** Timer fires → get all blobs → find nearest within `max_range` → emit `shoot_projectile`
- **Projectile:** `level.create_projectile()` instantiates `projectile.tscn` at scarecrow position

---

### 🎯 Projectile
- **Node:** Dynamically instantiated by `level.create_projectile()`
- **Script:** `projectile.gd` (extends Area2D)
- **On screen:** Small sprite flying in a straight line from scarecrow toward blob
- **Movement:** `_process()` — `position += direction * speed * delta`
- **Hit:** `_on_body_entered()` — if blob: `blob.hit()`, then always `queue_free()`

---

### ⚫ Day Transition (black circle wipe)
- **Node:** `Level → Overlay → CanvasLayer → DayTransitionLayer` (ColorRect)
- **Script:** `level.gd → day_restart()` tweens the shader parameter
- **Shader:** `shaders/circle_transition.gdshader`
- **On screen:** Black circle that closes (shrinks inward) → holds for 0.5s → opens back out
- **When:** Player sleeps in bed OR presses Tab (day_change input action)
- **Progress param 0→1:** Circle shrinks → screen goes black
- **Progress param 1→0:** Circle grows → screen reveals

---

## Script Dependency Map

```
project.godot
  ↓ autoloads
Enum (enums.gd) ←── used by all scripts
Data (data.gd)  ←── used by all scripts

level.gd
  ├── receives signals from player.gd
  │   ├── tool_use    → modifies TileMapLayers, spawns plants/machines
  │   ├── day_change  → day_restart() → level_reset()
  │   ├── diagnose    → toggles PlantInfoContainer.visible
  │   ├── build       → instantiates machine scenes
  │   └── machine_change → updates preview sprite
  ├── manages plants via PlantResource (plant_res.gd)
  ├── manages plant UI via plant_info.gd / plant_info_container.gd
  ├── drives day color via DayTimer + daytime_color Gradient
  ├── drives rain via raining setter
  └── spawns blobs via BlobTimer

player.gd
  ├── drives AnimationTree (move_state_machine, tool_state_machine)
  ├── reads from Data.TOOL_STATE_ANIMATIONS for animation routing
  ├── calls tool_ui.gd → reveal() on Q/E/C
  └── calls fishing_game.gd → reveal()/action() on fish tool

plant.gd (shell)
  └── uses PlantResource (data + business logic)
      └── emit_changed() → plant_info.gd → update()

tree.gd
  └── uses flash_sprite_2d.gd → flash()
blob.gd
  └── uses flash_sprite_2d.gd → flash()
plant.gd
  └── uses flash_sprite_2d.gd → flash(0.2, 0.4, queue_free)
```
