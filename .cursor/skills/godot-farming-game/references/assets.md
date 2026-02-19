# Asset Paths Reference

All paths are relative to `res://` (project root).

## Characters

| Path | Description | Frames |
|------|-------------|--------|
| `graphics/characters/main/main_basic.png` | Player default skin | 33H × 4V |
| `graphics/characters/main/main_blue.png` | Baseball hat skin | 33H × 4V |
| `graphics/characters/main/main_cowboy.png` | Cowboy hat skin | 33H × 4V |
| `graphics/characters/main/main_grey.png` | English hat skin | 33H × 4V |
| `graphics/characters/main/main_straw.png` | Straw hat skin | 33H × 4V |
| `graphics/characters/main/main_red.png` | Beanie hat skin | 33H × 4V |
| `graphics/characters/blob.png` | Blob enemy | 14H × 4V |
| `graphics/characters/cat.png` | Cat NPC |  |
| `graphics/characters/woman.png` | Woman NPC |  |
| `graphics/characters/mouse.png` | Mouse NPC |  |

**Player sprite sheet layout (33H × 4V):**
- Row 0: Idle frames (down, left, right, up) + tool animations down
- Row 1: Tool animations left
- Row 2: Tool animations right
- Row 3: Tool animations up
- Frames 0-1: Idle (down)
- Frames 2-5: Walk (down)
- Per-tool: 4 frames each direction

---

## Tilesets

| Path | Description | Usage |
|------|-------------|-------|
| `graphics/tilesets/grass.png` | Main ground tiles | GrassLayer terrain |
| `graphics/tilesets/soil.png` | Farm soil tiles | SoilLayer terrain |
| `graphics/tilesets/soil_water.png` | Watered soil (3 variants) | SoilWaterLayer |
| `graphics/tilesets/water.png` | Animated water (4 frames) | WaterLayer |
| `graphics/tilesets/walls_floor_tile.png` | House floor tiles | house.tscn FloorLayer |
| `graphics/tilesets/walls_nofloor.png` | House walls without floor | House walls |
| `graphics/tilesets/roof.png` | House roof tiles | house.tscn RoofLayer |
| `graphics/tilesets/fence.png` | Fence tiles | Decorative |
| `graphics/tilesets/path.png` | Path tiles | Decorative |
| `graphics/tilesets/hills.png` | Hill tiles | Decorative |
| `graphics/tilesets/decoration.png` | Bushes & rocks | simple_object (4H × 2V) |

**Tile size:** All tiles are 16×16 pixels.

**decoration.png layout:**
- H frames 0-3 = sizes (small to large)
- V frame 0 = bush, V frame 1 = rock

---

## Plants

| Path | Description | Frames |
|------|-------------|--------|
| `graphics/plants/tomato.png` | Tomato growth stages | 3H |
| `graphics/plants/corn.png` | Corn growth stages | 3H |
| `graphics/plants/pumpkin.png` | Pumpkin growth stages | 3H |
| `graphics/plants/wheat.png` | Wheat growth stages | 3H |
| `graphics/plants/tree.png` | Tree (2 variants) | 2H |
| `graphics/plants/stump.png` | Tree stump | 1H |
| `graphics/plants/apple.png` | Apple sprite (on tree) | 1H |

**Plant frame meaning:** 0=seedling, 1=growing, 2=mature (harvestable)

---

## Icons (UI / Tool indicators)

| Path | Represents |
|------|-----------|
| `graphics/icons/axe.png` | Axe tool |
| `graphics/icons/hoe.png` | Hoe tool |
| `graphics/icons/water.png` | Watering can |
| `graphics/icons/sword.png` | Sword tool |
| `graphics/icons/fish.png` | Fishing rod |
| `graphics/icons/wheat.png` | Seed tool |
| `graphics/icons/corn.png` | Corn seed |
| `graphics/icons/pumpkin.png` | Pumpkin seed |
| `graphics/icons/tomato.png` | Tomato seed |
| `graphics/icons/sprinkler.png` | Sprinkler machine |
| `graphics/icons/fisher.png` | Fisher machine |
| `graphics/icons/scarecrow.png` | Scarecrow machine |
| `graphics/icons/delete.png` | Delete machine mode |
| `graphics/icons/apple.png` | Apple item |
| `graphics/icons/wood.png` | Wood item |
| `graphics/icons/goldfish.png` | Gold fish |
| `graphics/icons/silverfish.png` | Silver fish |
| `graphics/icons/grayfish.png` | Gray fish |
| `graphics/icons/cowboy.png` | Cowboy hat (shop) |
| `graphics/icons/english.png` | English hat (shop) |
| `graphics/icons/blue.png` | Baseball hat (shop) |
| `graphics/icons/beanie.png` | Beanie hat (shop) |
| `graphics/icons/straw.png` | Straw hat (shop) |

---

## Hats

| Path | Style |
|------|-------|
| `graphics/hats/cowboy.png` | Cowboy |
| `graphics/hats/grey.png` | English |
| `graphics/hats/blue.png` | Baseball |
| `graphics/hats/red.png` | Beanie |
| `graphics/hats/straw.png` | Straw |

---

## Machines

| Path | Machine |
|------|---------|
| `graphics/machines/sprinkler.png` | Sprinkler |
| `graphics/machines/fisher.png` | Fisher |
| `graphics/machines/scarecrow.png` | Scarecrow |
| `graphics/machines/tv.png` | TV (house) |
| `graphics/machines/projectile.png` | Scarecrow projectile |
| `graphics/machines/food.png` | Food (shop/future) |

---

## UI

| Path | Used in |
|------|---------|
| `graphics/ui/frame.png` | PanelContainer background (9-patch, margins=6) |
| `graphics/ui/bar.png` | Fishing game bar |
| `graphics/ui/v_bar.png` | Plant info progress bars |
| `graphics/ui/fish_frame.png` | Fishing game frame |
| `graphics/ui/fish_bar.png` | Fishing progress bar |
| `graphics/ui/fish_progress.png` | Fishing progress fill |
| `graphics/ui/fish_progress_bg.png` | Fishing progress background |
| `graphics/ui/fisher_bar.png` | Fisher machine progress bar |

---

## Objects (House furniture)

| Path | Item |
|------|------|
| `graphics/objects/bed.png` | Bed |
| `graphics/objects/carpet.png` | Carpet |
| `graphics/objects/bookshelf.png` | Bookshelf |
| `graphics/objects/table.png` | Table |
| `graphics/objects/plant.png` | Indoor plant |
| `graphics/objects/night stand.png` | Night stand (note: space in filename) |
| `graphics/objects/chair.png` | Chair |

---

## Weather

| Path | Usage |
|------|-------|
| `graphics/weather/floor.png` | Rain floor particles texture |
| `graphics/weather/drops.png` | Rain drop particles texture |

---

## Fonts

| Path | Usage |
|------|-------|
| `graphics/fonts/HomeVideo-Regular.ttf` | Main game font (game_theme.tres) |
| `graphics/fonts/PixeloidSans.ttf` | Alternative pixel font |
| `graphics/fonts/dogicapixel.otf` | Alternative pixel font |
| `graphics/fonts/Better VCR 9.0.1.ttf` | VCR-style font |

---

## Premade Assets (do not recreate)

| Path | What it is |
|------|-----------|
| `premade/HouseTileSet.tres` | Complete TileSet for house walls/floor |
| `premade/HouseTileSet.tscn` | House TileSet scene |
| `premade/fisher.tres` | Fisher AnimatedSprite SpriteFrames resource |

---

## Audio

All audio files live in `audio/`. Each has a matching `.import` file (auto-generated by Godot).

| Path | Format | Used in | Trigger |
|------|--------|---------|---------|
| `audio/axe.wav` | WAV | player.gd | `AudioStreamPlayer.play()` when axe swing animation hits method track |
| `audio/hoe.wav` | WAV | player.gd | Same — hoe strike method track |
| `audio/fish.wav` | WAV | player.gd / fisher.gd | When fish is caught |
| `audio/water.ogg` | OGG | player.gd | When watering can is used |
| `audio/slime.ogg` | OGG | blob.gd | When blob is hit or spawned |
| `audio/step.mp3` | MP3 | player.gd | Footstep — plays on walk animation method track |
| `audio/music.mp3` | MP3 | level.gd | Background music — plays in loop at game start |
| `audio/rain.mp3` | MP3 | level.gd | Rain ambient — plays when rain day starts, stops when it ends |

**How to wire audio in Godot:**
```gdscript
# In the scene that needs audio, add an AudioStreamPlayer node.
# In the script:
@onready var sfx = $AudioStreamPlayer

func play_axe():
    sfx.stream = preload("res://audio/axe.wav")
    sfx.play()

# For looping music:
@onready var music = $AudioStreamPlayer
func _ready():
    music.stream = preload("res://audio/music.mp3")
    music.autoplay = true   # Or set in Inspector
```

---

## Shaders

| Path | Type | Used in |
|------|------|---------|
| `shaders/flash.tres` | VisualShader resource | FlashSprite2D material |
| `shaders/circle_transition.gdshader` | Code shader | DayTransitionLayer material |

---

## Premade files — do not recreate from scratch

| Path | What it is | How to use |
|------|-----------|------------|
| `premade/HouseTileSet.tres` | Full house wall/floor/door TileSet | Set as `tile_set` on WallsLayer and FloorLayer in house.tscn |
| `premade/HouseTileSet.tscn` | Editor viewer for HouseTileSet.tres | Open in editor to browse available tiles |
| `premade/fisher.tres` | SpriteFrames with 8 directional fisher animations | Set as `sprite_frames` on AnimatedSprite2D in fisher.tscn |
| `premade/code_snippets.txt` | Paste-ready GDScript constants (MACHINE_PREVIEW_TEXTURES, seed_amount, TOOL_TEXTURES, SOIL_DIRECTIONS) | See references/scene-files.md for full annotated content |
