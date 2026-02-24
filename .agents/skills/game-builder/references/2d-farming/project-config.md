# Project Configuration Reference

## project.godot — Full Settings

```ini
config_version=5

[application]
config/name="GodewValley"
run/main_scene="uid://dkaf0otbgtrp5"   # res://scenes/levels/level.tscn
config/features=PackedStringArray("4.6", "Forward Plus")
config/icon="res://icon.svg"

[animation]
compatibility/default_parent_skeleton_in_mesh_instance_3d=true

[autoload]
Enum="*res://global/enums.gd"
Data="*res://global/data.gd"

[display]
window/size/viewport_width=1920
window/size/viewport_height=1080

[rendering]
textures/canvas_textures/default_texture_filter=0   # 0=Nearest (pixel art crisp), 1=Linear (blurry)

[layer_names]
2d_physics/layer_1="Terrain"
2d_physics/layer_2="Player"
2d_physics/layer_3="Objects"
2d_physics/layer_4="Characters"
```

> **Note:** Pixel art REQUIRES `default_texture_filter=0` (Nearest). Without it every sprite blurs.

---

## Input Map

| Action | Keyboard | Controller |
|--------|----------|------------|
| `left` | A | Joypad Axis 0 -1 |
| `right` | D | Joypad Axis 0 +1 |
| `up` | W | Joypad Axis 1 -1 |
| `down` | S | Joypad Axis 1 +1 |
| `action` | Space | Joypad Button 0 (A) |
| `tool_backward` | Q | Joypad Button 9 (LB) |
| `tool_forward` | E | Joypad Button 10 (RB) |
| `style_toggle` | T | Joypad Button 3 (Y) |
| `seed_forward` | C | Joypad Button 1 (B) |
| `day_change` | Tab | Joypad Button 11 |
| `build` | M | Joypad Button 13 |
| `diagnose` | N | Joypad Button 14 |

**Deadzone** for `left/right/up/down`: 0.2
**Deadzone** for `action/tool_*/style_toggle/seed_forward/day_change/build/diagnose`: 0.2 (buttons) or 0.5 (ui_*)

---

## Physics Layers Reference

| Layer # | Name | Used by |
|---------|------|---------|
| 1 | Terrain | GrassLayer collision, TileMap walls |
| 2 | Player | Player CharacterBody2D |
| 3 | Objects | Plants, Trees, Blobs, Machines |
| 4 | Characters | NPCs (future) |

**Collision rules:**
- Player: layer=2, mask=1 (sees terrain only)
- Trees/SimpleObjects: layer=3, no mask
- Plants: layer=3, no mask; CollisionArea inside plant: no layer, mask=2 (detects player)
- Blob: layer=3, mask=1 (moves through terrain)
- Projectile (Area2D): no layer, mask=3 (detects objects/blobs)
- GrassLayer TileSet physics: layer=1

---

## Window Size Options

| Resolution | Config value |
|------------|-------------|
| 1920×1080 (default) | `viewport_width=1920` `viewport_height=1080` |
| 1280×720 | `viewport_width=1280` `viewport_height=720` |
| 960×540 | `viewport_width=960` `viewport_height=540` |

Camera2D zoom=4 is designed for 1920×1080 with 16px tile size. Adjust zoom if you change resolution.

---

## Tile Size

`Data.TILE_SIZE = 16` — all TileMapLayers use 16×16 pixel tiles.

Grid coordinate conversion:
```gdscript
# pixel pos → grid coord (handles negative coords correctly)
var grid_coord = Vector2i(int(pos.x / Data.TILE_SIZE), int(pos.y / Data.TILE_SIZE))
grid_coord.x += -1 if pos.x < 0 else 0
grid_coord.y += -1 if pos.y < 0 else 0
```

---

## Autoloads

Both scripts are singletons accessible globally by name:

- `Enum` → `res://global/enums.gd` — all game enums
- `Data` → `res://global/data.gd` — all game data dictionaries and constants

Usage in any script:
```gdscript
var tool = Enum.Tool.AXE
var texture = Data.PLAYER_SKINS[Enum.Style.BASIC]
var plant_info = Data.PLANT_DATA[Enum.Seed.TOMATO]
```
