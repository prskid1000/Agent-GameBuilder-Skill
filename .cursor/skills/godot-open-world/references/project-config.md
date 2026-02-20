# Project Config, Input Map & Addon Setup

Based on `.examples/godot-craft/project.godot`.

---

## project.godot

```ini
config_version=5

[application]
config/name="gdcraft"
run/main_scene="res://scenes/main.tscn"
config/features=PackedStringArray("4.5", "Forward Plus")
config/icon="res://icon.svg"

[autoload]
GDCraftResources="*res://scripts/resources.gd"

[display]
window/size/viewport_width=1600
window/size/viewport_height=900
window/stretch/mode="canvas_items"
window/stretch/aspect="expand"
window/vsync/vsync_mode=3

[editor_plugins]
enabled=PackedStringArray("res://addons/godot-sqlite/plugin.cfg")

[physics]
3d/physics_engine="Jolt Physics"

[rendering]
lights_and_shadows/directional_shadow/soft_shadow_filter_quality=3
anti_aliasing/quality/msaa_3d=2
```

---

## Input Map

| Action | Key | Notes |
|--------|-----|-------|
| `forward` | W | Move forward |
| `back` | S | Move back |
| `left` | A | Move left |
| `right` | D | Move right |
| `jump` | Space, E | Move up (fly/jump) |
| `crouch` | Q, Ctrl | Move down |
| `sprint` | Shift, F | Sprint speed |
| `break` | Left Mouse Button | Break block (raycast) |
| `place` | Right Mouse Button | Place selected block |
| `debug` | F3 | Toggle stats HUD |
| `unfocus` | Escape | Release mouse capture |

---

## Project File Layout

```
res://
  scripts/
    block.gd          ← Block static class (types, vertices, texcoords, light)
    chunk.gd          ← Chunk (StaticBody3D, generate, mesh, expose)
    database.gd       ← SQLite persistence (blocks, player, sky)
    face.gd           ← Face static class (6 directions)
    generator.gd      ← Terrain noise generation
    hud.gd            ← Stats + block display
    player.gd         ← CharacterBody3D, first-person, place/break
    resources.gd      ← Autoload: shaders + Texture2DArray
    sky.gd            ← Day/night cycle
    world.gd          ← Chunk manager + orchestrator
  scenes/
    main.tscn         ← Entry point (just loads world.tscn)
    world.tscn        ← World root with all children
    player.tscn       ← Player CharacterBody3D
    sky.tscn          ← Sky node + DirectionalLight + WorldEnvironment
    hud.tscn          ← HUD CanvasLayer
  resources/
    spritesheet.png           ← 16×N grid of 16×16 block textures
    opaque.gdshader           ← Opaque block shader
    transparent.gdshader      ← Transparent block shader (water, glass)
    sprite.gdshader           ← Cross-sprite shader (plants, torches)
    spritesheet.gdshaderinc   ← Shared spritesheet sampling include
  addons/
    godot-sqlite/             ← GDExtension SQLite plugin
      plugin.cfg
      godot-sqlite.gd
      gdsqlite.gdextension
      bin/                    ← Platform binaries
```

---

## godot-sqlite Addon Setup

1. Download or copy `addons/godot-sqlite/` from `.examples/godot-craft/addons/godot-sqlite/`.
2. Place it at `res://addons/godot-sqlite/`.
3. In the Godot editor: **Project → Project Settings → Plugins** → enable **godot-sqlite**.
4. The `SQLite` class is now available globally in GDScript.
5. DB file is created at `user://gdcraft.sqlite` on first run (`OS.get_user_data_dir()`).

---

## Rendering Notes

- **Jolt Physics** is used for better performance with many chunk `StaticBody3D` nodes.
- **MSAA 3D = 2** (2× anti-aliasing).
- **Directional Shadow Soft Quality = 3** (Soft Low).
- **VSync mode = 3** = Adaptive (matches monitor refresh, avoids tearing).
- **Forward Plus** renderer required (deferred lighting for `OmniLight3D` per-chunk torches).
