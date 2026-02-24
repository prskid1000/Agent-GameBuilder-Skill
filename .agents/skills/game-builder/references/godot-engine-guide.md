# Godot Engine Guide — Editor, Assets, Scenes, TileMap

This guide teaches you how to USE the Godot 4 editor. Read this first if you are new
to Godot or need a refresher on editor operations.

---

## 1 — Editor Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  Menu bar (Scene / Project / Debug / Editor / Help)             │
├──────────┬──────────────────────────────────┬───────────────────┤
│  Scene   │                                  │    Inspector      │
│  panel   │         3D/2D Viewport           │    (properties)   │
│  (node   │                                  │                   │
│  tree)   │                                  │  Node panel       │
│          │                                  │  (signals/groups) │
├──────────┴──────────────────────────────────┴───────────────────┤
│  FileSystem   │  Output / Debugger / Audio / Animation          │
└─────────────────────────────────────────────────────────────────┘
```

| Panel | Shortcut | Purpose |
|-------|----------|---------|
| Scene Tree | — | Hierarchy of all nodes in the open scene |
| Inspector | — | Properties of the selected node |
| FileSystem | — | All project files (res://) |
| Output | — | print() output + warnings |
| Debugger | — | Errors, profiler, monitors |
| Script editor | Ctrl+` | Write GDScript |
| 2D editor | Ctrl+F1 | Visual scene editing |

---

## 2 — Creating a Scene

**Method A — New scene from scratch:**
1. `Scene → New Scene`
2. In the Scene panel, click **+ Other Node** → type the root type (e.g. `CharacterBody2D`)
3. Press **Ctrl+S** → choose `res://scenes/` subfolder → give it a name

**Method B — Instantiate an existing scene:**
1. In FileSystem, drag a `.tscn` file into the Viewport **or** into the Scene panel
2. The scene appears as a single node (gray icon = inherited)

**Renaming a scene root node:**
- Click the root node in Scene panel → press F2 → type new name

**Scene types you'll use:**
| Root Node | Use case |
|-----------|----------|
| `CharacterBody2D` | Player, enemies |
| `StaticBody2D` | Non-moving objects (rocks, chests) |
| `Area2D` | Hitboxes, triggers, pickups |
| `Node2D` | Containers with no physics |
| `Control` | UI elements |
| `CanvasLayer` | UI that ignores camera (HUD) |

---

## 3 — Adding Nodes to a Scene

1. Select a parent node in the Scene panel
2. Click **+** (top of Scene panel) OR press **Ctrl+A**
3. Type the node name in the search box → double-click it

**Common nodes for RPG:**
```
CharacterBody2D
  CollisionShape2D        ← required for physics
  Sprite2D / AnimatedSprite2D
  AnimationPlayer
  AnimationTree
  Area2D                  ← hitbox / hurtbox
    CollisionShape2D
  NavigationAgent2D       ← enemy pathfinding
  AudioStreamPlayer2D     ← spatial SFX
  PointLight2D            ← dynamic lighting
  Camera2D                ← (player only)
```

---

## 4 — Importing Art Assets

### Pixel Art Setup (do this first)
`Project → Project Settings → Rendering → Textures → Default Texture Filter → Nearest`
This prevents pixel art from becoming blurry. You never have to set it per-sprite.

### Importing Images
1. Copy/paste your `.png` files into the project folder (res://graphics/...)
2. Godot auto-imports them — a `.import` file is created automatically
3. **Never manually edit `.import` files**

### Spritesheet (SpriteFrames / Sprite2D)
**For Sprite2D with frame animation:**
1. Select the `Sprite2D` node → Inspector → Texture → drag your spritesheet PNG
2. Set `HFrames` = number of horizontal animation frames
3. Set `VFrames` = number of rows (usually 4 for up/down/left/right)
4. The `Frame` property selects which cell to show (0 = top-left)

**For AnimatedSprite2D:**
1. Inspector → SpriteFrames → New SpriteFrames
2. Click the SpriteFrames resource → opens Animation panel at bottom
3. Create animations (idle, walk, attack...) → drag frames into the timeline
4. Set FPS per animation

### Importing Audio
| Format | Use for |
|--------|---------|
| `.ogg` | Music (compressed, loops well) |
| `.wav` | Short SFX (sword swing, footstep) |
| `.mp3` | Long SFX or music |

After importing: select the file in FileSystem → Import tab:
- Music: enable **Loop** → Reimport
- SFX: leave Loop off → Reimport

### Fonts
1. Copy `.ttf` or `.otf` into `res://fonts/`
2. In a Label's Inspector → Label Settings → New LabelSettings → Font → drag your font
3. Or create a Theme resource and set fonts globally

---

## 5 — Inspector: Setting Node Properties

| Property type | How to set it |
|--------------|--------------|
| Number | Click field, type value |
| Vector2 | Two number fields (X, Y) |
| Color | Click color swatch → color picker |
| Texture | Drag PNG from FileSystem into the slot |
| Resource | Click → New [ResourceType] → or drag existing .tres |
| Node path | Drag a node from Scene panel into the slot |
| Enum dropdown | Click dropdown → pick value |
| Bool checkbox | Click to toggle |

**Important for collisions:**
- `collision_layer` = which layer THIS node lives on
- `collision_mask` = which layers THIS node detects / collides with
- Use bit buttons in Inspector or set via script: `collision_layer = 0b00000100` = layer 3

---

## 6 — Signals (connecting events)

### In the Editor (recommended for fixed connections)
1. Select the source node → **Node panel** (tab next to Inspector) → **Signals** tab
2. Double-click the signal you want (e.g. `body_entered`)
3. Pick the target node → pick or create the function → Connect

### In GDScript (recommended for dynamic connections)
```gdscript
# Connect in _ready():
$Area2D.body_entered.connect(_on_hitbox_body_entered)

# Disconnect later:
$Area2D.body_entered.disconnect(_on_hitbox_body_entered)

# Connect with extra arguments (bind):
$Area2D.body_entered.connect(_on_hitbox_body_entered.bind(damage_value))
```

---

## 7 — TileMap: Building Levels

### Creating a TileMapLayer
1. Add node `TileMapLayer` to your level scene
2. Inspector → TileSet → **New TileSet**
3. Click the TileSet → opens TileSet editor at bottom
4. Drag your tileset PNG into the **Sources** panel → Create Atlas

### Setting up Terrain (autotiling)
1. TileSet Inspector → **Terrain Sets** → Add Element → Mode: `Match Corners and Sides`
2. Inside Terrain Sets → **Terrains** → Add Element → name it (e.g. "Grass") → pick a color
3. Bottom TileSet panel → **Paint** tab → dropdown: **Terrains**
4. Select Terrain Set 0, Terrain 0 ("Grass")
5. Left-click each tile to activate it for this terrain
6. Draw the connectivity arrows on each tile: click the 8 surrounding dots to tell Godot "this tile connects here"
7. Add ALL tile variants (corners, edges, fills, diagonals) for complete autotiling

### Painting Terrain in the Level
1. Select the TileMapLayer node
2. Bottom panel → **TileMap** tab → **Terrains** → pick your terrain
3. Left-drag to paint, right-drag to erase
4. Use the **rectangle** tool for fast fills

### Adding Collision to Tiles
1. TileSet Inspector → **Physics Layers** → Add Element
2. Set `collision_layer` = 1 (Terrain), mask = 0 (walls don't detect anything)
3. Bottom TileSet panel → **Paint** → **Physics Layer 0**
4. Click each tile to draw collision polygons
5. Adjust polygon points by dragging handles
6. Tip: use `R` to rotate, `H`/`V` to flip when painting collision shapes

### Custom Data on Tiles (e.g. walkable, surface_type)
1. TileSet Inspector → **Custom Data Layers** → Add Element
2. Name it (e.g. "surface_type") → Type: String
3. Paint tab → Custom Data → select your layer → paint values on individual tiles
4. In GDScript: `var data = tile_map.get_cell_tile_data(coord)` then `data.get_custom_data("surface_type")`

---

## 8 — NavigationRegion2D (Enemy Pathfinding)

### Setup
1. Add `NavigationRegion2D` to your level (must wrap your walkable area)
2. Inspector → NavigationPolygon → New NavigationPolygon
3. Draw the walkable polygon manually **or** use "Bake NavigationPolygon" button
4. For TileMap-based levels: enable **Geometry → Use TileMap** on the NavigationRegion2D
5. Click **Bake NavigationPolygon** → Godot generates the walkable mesh from your TileMap

### Enemy usage
```gdscript
@onready var nav_agent = $NavigationAgent2D

func _physics_process(_delta):
    nav_agent.target_position = target.global_position
    var next_pos = nav_agent.get_next_path_position()
    velocity = (next_pos - global_position).normalized() * speed
    move_and_slide()
```

---

## 9 — 2D Lights and Shadows

### PointLight2D (dynamic torches, lanterns, etc.)
1. Add `PointLight2D` to your scene
2. Inspector → Texture → drag a light texture (soft white circle gradient)
3. Set Energy (brightness), Color, and Range
4. Enable **Shadow → Enabled** for hard shadows

### LightOccluder2D (walls that block light)
1. Add `LightOccluder2D` as a child of each wall object or TileMapLayer
2. Inspector → Occluder → New OccluderPolygon2D
3. Draw the polygon outline around the wall shape

### CanvasModulate for global darkness
1. Add `CanvasModulate` node to the scene
2. Set Color → dark gray or black
3. Lights punch through this darkness

---

## 10 — AnimationTree Setup (step by step)

The AnimationTree is the hardest editor step. Follow carefully.

### Create the tree structure
1. Add `AnimationPlayer` to player (create all animations here)
2. Add `AnimationTree` to player
3. AnimationTree Inspector → **Tree Root** → New AnimationNodeBlendTree
4. AnimationTree Inspector → **Anim Player** → drag AnimationPlayer here
5. AnimationTree Inspector → **Active** → ON

### Inside the BlendTree
1. Click AnimationTree to open the graph editor
2. Right-click → **Add Node** → `AnimationNodeStateMachine` → name it `MoveStateMachine`
3. Right-click → **Add Node** → `AnimationNodeOneShot` → name it `AttackOneShot`
4. Wire: `MoveStateMachine → AttackOneShot (in)` → `AttackOneShot (out) → Output`
5. Also connect any `AbilityOneShot` nodes for special moves

### Inside MoveStateMachine
1. Double-click MoveStateMachine → opens state machine editor
2. Right-click → **Add Node** → `AnimationNodeBlendSpace2D` → name it `Idle`
3. Right-click → Add another `AnimationNodeBlendSpace2D` → name it `Walk`
4. Connect: `Start → Idle` (auto), `Idle ↔ Walk` (manual, gray arrows)

### Inside each BlendSpace2D
1. Double-click Idle or Walk to open it
2. Right-click at position (-1, 0) → Add Animation → `idle_left`
3. Repeat for all 8 or 9 points:
   ```
   (-1, 0) = idle_left      (0,-1) = idle_up      (1, 0) = idle_right
   (-1, 1) = idle_left      (0, 0) = idle_down     (1, 1) = idle_right
   (-1,-1) = idle_left      (0, 1) = idle_down     (1,-1) = idle_right
   ```
   Note: Y-axis is INVERTED in BlendSpace2D (positive Y = upward in blend space = downward in GDO)

### Set starting blend positions
AnimationTree Inspector → Parameters:
- `MoveStateMachine/Idle/blend_position` = (0, 0)
- `MoveStateMachine/Walk/blend_position` = (0, 0)
- All attack blend positions = (0, 0)

---

## 11 — Camera2D Setup

```gdscript
# On the Camera2D node:
# Inspector settings:
# Position Smoothing → Enabled = true, Speed = 10.0
# Drag → Horizontal/Vertical enabled (for slight lag behind player)
# Limit → Set Left/Top/Right/Bottom to level boundaries

# In script:
@onready var camera = $Camera2D

func apply_shake(magnitude: float, duration: float) -> void:
    var tween = create_tween()
    tween.tween_method(_set_camera_offset, Vector2.ZERO, Vector2(magnitude, 0), duration * 0.25)
    tween.tween_method(_set_camera_offset, Vector2(magnitude, 0), Vector2(-magnitude, 0), duration * 0.5)
    tween.tween_method(_set_camera_offset, Vector2(-magnitude, 0), Vector2.ZERO, duration * 0.25)

func _set_camera_offset(value: Vector2) -> void:
    camera.offset = value
```

---

## 12 — Useful Editor Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+S | Save scene |
| Ctrl+Shift+S | Save all |
| Ctrl+D | Duplicate node |
| Ctrl+Z | Undo |
| Ctrl+Shift+Z | Redo |
| F | Focus camera on selected node |
| Q | Select tool |
| W | Move tool |
| E | Rotate tool |
| S | Scale tool |
| R | Flip/rotate tile in TileMap |
| H | Flip tile horizontal |
| V | Flip tile vertical |
| Ctrl+G | Toggle grid snap |
| Ctrl+R | Run current scene |
| F5 | Run main scene |
| F8 | Stop running scene |
