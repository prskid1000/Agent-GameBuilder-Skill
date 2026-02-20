# Step-by-Step Build Guide

Builds the complete GDCraft (Minecraft-style 3D voxel open-world game) from scratch.
Each step must run cleanly before proceeding to the next.

---

## Step 1 — Project Setup + Addon

**Agent produces:** `project.godot`

```ini
[application]
config/name="gdcraft"
run/main_scene="res://scenes/main.tscn"
config/features=PackedStringArray("4.5", "Forward Plus")

[autoload]
GDCraftResources="*res://scripts/resources.gd"

[display]
window/size/viewport_width=1600
window/size/viewport_height=900
window/stretch/mode="canvas_items"
window/stretch/aspect="expand"
window/vsync/vsync_mode=3

[physics]
3d/physics_engine="Jolt Physics"

[rendering]
lights_and_shadows/directional_shadow/soft_shadow_filter_quality=3
anti_aliasing/quality/msaa_3d=2
```

**Input map** (add all in Project Settings → Input Map):

| Action | Events |
|--------|--------|
| `forward` | W |
| `back` | S |
| `left` | A |
| `right` | D |
| `jump` | Space, E |
| `crouch` | Q, Ctrl |
| `sprint` | Shift, F |
| `break` | Left Mouse Button |
| `place` | Right Mouse Button |
| `debug` | F3 |
| `unfocus` | Escape |

**Addon — godot-sqlite:**
1. Copy `addons/godot-sqlite/` from `.examples/godot-craft/` into your project root.
2. In the editor: Project → Project Settings → Plugins → enable `godot-sqlite`.
3. The `SQLite` class is now globally available.

**Create placeholder main.tscn** (just a Node with no script) so the project runs.

**Verify:** Project opens in Godot. No missing plugin errors. F5 runs without crash.

---

## Step 2 — Face + Block Classes

**Agent produces:** `scripts/face.gd`, `scripts/block.gd`

These are static utility classes (no `extends`). Write them exactly as in [scripts.md](scripts.md).

Key things to get right:
- `Face.Type` enum must have COUNT=6 members in exact order: FORWARD, BACK, LEFT, RIGHT, UP, DOWN.
- `Block.Type` enum: ends with COUNT=23, then EMPTY=24.
- `Block._VERTICES`: 6 faces × 4 verts, in face order matching `Face.Type`.
- `Block.get_texcoord(type, face)`: returns `Vector2(column, row)` in spritesheet tile grid.
- `Block.is_exposed(lhs, rhs)`: the face-culling rule that drives mesh efficiency.

**Verify:** No parse errors. Add a test in a temp script: `print(Block.get_texcoord(Block.Type.GRASS, Face.Type.UP))` — should print `(0, 0)`.

---

## Step 3 — GDCraftResources Autoload

**Agent produces:** `scripts/resources.gd`

- `extends Node`
- Preloads spritesheet + 3 shaders.
- `_ready()` → `_create_spritesheet()` → slices `spritesheet.png` into 16×16 tiles → `Texture2DArray` → assigned to 3 `ShaderMaterial`s.
- Materials are stored as `opaque_material`, `transparent_material`, `sprite_material`.

**Spritesheet requirements:**
- Pixel art style, 16×16 tiles arranged in a grid.
- Row 0: GRASS-top, DIRT, GRASS-side, STONE, WATER, LOG-top, LOG-side, LEAVES, SAND, BUSH, POPPY, DANDELION, DAISY, CORNFLOWER, MARIGOLD, LAVENDER.
- Row 1: YELLOW_TORCH, RED_TORCH, BLUE_TORCH, GREEN_TORCH, CYAN_TORCH, MAGENTA_TORCH, WHITE_TORCH, PLANKS, GLASS.

See [asset-prompts-comfyui.md](asset-prompts-comfyui.md) for spritesheet generation prompts.

**Verify:** Autoload appears in scene tree. No texture errors. `GDCraftResources.opaque_material` is not null.

---

## Step 4 — Shaders

**Agent produces:** `resources/spritesheet.gdshaderinc`, `resources/opaque.gdshader`, `resources/transparent.gdshader`, `resources/sprite.gdshader`

Full GLSL source is in [scripts.md → Shaders](scripts.md).

Key design:
- All shaders `#include "spritesheet.gdshaderinc"`.
- `UV` = tile coordinate (column, row) from `Block.get_texcoord()`.
- `UV2` = per-vertex in-tile UV (0..1) from `Block.get_texcoord2()`.
- `get_color(UV2, UV)` computes the correct `Texture2DArray` layer and samples it.
- `opaque`: `cull_back`, discard if `alpha < 0.5` (cutout for leaves/glass edges).
- `transparent`: `blend_mix`, no discard — water and glass are semi-transparent.
- `sprite`: `cull_disabled, unshaded` — cross-sprite plants rendered from both sides.

**Verify:** Shaders compile without errors (red X in script editor = compile error). `GDCraftResources._ready()` completes without errors.

---

## Step 5 — Chunk

**Agent produces:** `scripts/chunk.gd`

The most complex script. Key implementation notes:

**Flag system:**
```gdscript
GENERATING = 0b00000001  # set before add_task, cleared in _end_generate
GENERATED  = 0b00000010  # set in _end_generate
EXPOSED    = 0b00000100  # set in _expose (called inside _mesh)
MESHING    = 0b00001000  # set before add_task, cleared in _end_mesh
MESHED     = 0b00010000  # set in _end_mesh
WORKING    = GENERATING | MESHING  # bitmask: any async op active?
```

**Thread safety:**
- `_generate()` and `_mesh()` run on WorkerThreadPool.
- `add_child.call_deferred()` and `_end_generate.call_deferred()` ensure main-thread operations.
- Never read/write `_world._chunks` or scene tree from worker thread — only call deferred.

**Mesh building (`_emit_face`):**
- `ARRAY_VERTEX`: world-space position = `Vector3(_index * SIZE + block_index) + vertex_offset`.
- `ARRAY_TEX_UV`: tile coordinate (stays constant per face — the shader indexes into Texture2DArray).
- `ARRAY_TEX_UV2`: in-tile UV (varies per vertex within the tile).
- `ARRAY_INDEX`: always `[0,1,2, 0,2,3]` (two triangles per quad), offset by `start_index`.

**Light blocks (`set_light`):**
- Creates `OmniLight3D` at exact world-space position of the block center.
- Stored in `_lights` dict by block index for removal when block changes.
- Uses `add_child.call_deferred()` (runs on worker thread context).

**`_skip_face`:** skips DOWN face at `y==0` in the bottom chunk row — never visible (underground).

**Verify:** (Tested in Step 7 when World creates chunks.)

---

## Step 6 — Generator

**Agent produces:** `scripts/generator.gd`

Three generator modes selectable via `@export var type`:

**NOISE (default):**
- 4 `FastNoiseLite` instances with different seeds and frequencies.
- Per column (x,z): compute height = `int(pow(base*5, 1.25)*5 + overlay*2)`.
- sea_level = 10: above → water; at/near → sand; high → stone; mid → grass+dirt.
- Surface: `foliage_value = int(foliage_noise * 13793) % 100`. Low values → trees (if in bounds); medium → foliage sprites.
- Trees: LOG trunk 4–8 high, LEAVES sphere radius 3 (manhattan ≤ 3).

**SUPERFLAT:** 3 STONE + 1 DIRT + 1 GRASS for testing.

**DEBUG:** Single GRASS block at (0,0,0) for mesh testing.

The return value is `Dictionary[Vector3i, Block.Type]` — only non-EMPTY blocks stored.

**Verify:** Add a test: `generator.generate(Vector3i.ZERO)` → print result size. Should be > 0 for all three modes.

---

## Step 7 — Database

**Agent produces:** `scripts/database.gd`

**SQLite setup:**
- DB opens at `user://gdcraft.sqlite` (in `AppData/Roaming/Godot/app_userdata/gdcraft/` on Windows).
- Tables created with `CREATE TABLE IF NOT EXISTS` — safe to run on every startup.
- `blocks` table: only player-edited blocks, not all procedural terrain.

**Thread safety:**
- `get_blocks()` is called from `Chunk._generate()` on a worker thread — must be mutex-locked.
- All other methods called from main thread but still mutex-locked for safety.

**Persistence flow:**
- `World._ready()` → `database.load_player()` + `database.load_sky()`.
- `World._notification(PREDELETE)` (on quit) → `database.save_player()` + `database.save_sky()`.
- `World._on_player_set_block()` → `database.set_block()` (called on main thread after chunk edit).

**Verify:** Run project. Check `user://gdcraft.sqlite` exists (use Editor → Open User Data Folder). No DB error prints.

---

## Step 8 — Player

**Agent produces:** `scripts/player.gd`, `scenes/player.tscn`

**Scene tree:**
```
Player  [CharacterBody3D, player.gd]
  CollisionShape3D  ← CapsuleShape3D (radius=0.4, height=1.8)
  Head  [Node3D, position=(0, 0.8, 0)]
    RayCast3D  ← enabled=true, target_position=(0, 0, -5)
  RayCastBlock  [MeshInstance3D]
    ← BoxMesh size=(1,1,1)
    ← StandardMaterial3D: Shading=Unshaded, Transparency=Alpha,
      Albedo=(1,1,1,0.3), Wireframe=true
```

**Player physics (set in Inspector):**
- CollisionLayer: bit 2 (Player)
- CollisionMask: bit 1 (World)
- `position.y = 30` set in `_init()` (spawns above terrain).

**Mouse capture:**
- Click anywhere → `Input.set_mouse_mode(CAPTURED)` → enables look.
- Esc → `VISIBLE` (releases cursor).
- Window unfocus → `VISIBLE` (handles Alt-Tab).

**Block cycling:**
- Scroll wheel calls `_switch_block(±factor)`.
- `_block_type` wraps around 0..COUNT-1 (excludes EMPTY=COUNT).

**Verify:** Player spawns. WASD moves. Mouse rotates view. Block wireframe shows when looking at terrain. Scroll changes block selection.

---

## Step 9 — Sky

**Agent produces:** `scripts/sky.gd`, `scenes/sky.tscn`

**Scene tree:**
```
GDCraftSky  [Node, sky.gd]
  Sun  [DirectionalLight3D]
    ← DirectionalShadow: Enabled, Mode=Parallel 4 Splits
  WorldEnvironment
    ← Environment:
        Sky: ProceduralSkyMaterial
        Ambient Light: Source=Color
```

**Sky math:**
- `time_of_day` advances by `delta * speed / _total_length` each frame → wraps at 1.0.
- Sun angle: `time_of_day * TAU + PI/2` → `light_energy = clamp(sin(angle-PI), 0, 1)`.
- Colors lerped across 4 phase bands; all set on `_sky_material` + `_environment`.

**Persistence:**
- `time_of_day` is saved to DB on quit, loaded on start → day continues from where it left off.

**Verify:** Sky colors change over time. Sun moves across the sky. Shadow cast at daytime, disabled at night.

---

## Step 10 — HUD

**Agent produces:** `scripts/hud.gd`, `scenes/hud.tscn`

**Scene tree:**
```
HUD  [CanvasLayer, hud.gd]
  Stats  [VBoxContainer, visible=false]
    FPS, Process, PhysicsProcess, StaticMemoryUsed,
    VideoMemoryUsed, DrawCalls, Primitives  [Label ×7]
  BlockH  [HBoxContainer, anchor=bottom-center]
    BlockV  [VBoxContainer]
      Texture  [TextureRect]  ← AtlasTexture from spritesheet, region updated at runtime
      Label                   ← block name
```

**Block texture display:**
- Create an `AtlasTexture` resource on `Texture.texture`.
- Set `atlas = ImageTexture.create_from_image(SPRITESHEET.get_image())`.
- In `_on_player_switch_block`: set `region = Rect2(col*16, row*16, 16, 16)`.

**Verify:** Block icon and name update when scrolling. F3 toggles stats. FPS is displayed correctly.

---

## Step 11 — World + Final Assembly

**Agent produces:** `scripts/world.gd`, `scenes/world.tscn`, `scenes/main.tscn`

**world.tscn:**
```
World  [Node, world.gd]
  Player  [player.tscn]
  Sky     [sky.tscn]
  Generator  [Node, generator.gd]
  Database   [Node, database.gd]
  HUD     [hud.tscn, CanvasLayer]
```

**Signal wiring in world.tscn (editor):**
- `Player.set_block` → `World._on_player_set_block`
- `Player.switch_block` → `HUD._on_player_switch_block`

Or wire in `World._ready()`:
```gdscript
_player.set_block.connect(_on_player_set_block)
_player.switch_block.connect($HUD._on_player_switch_block)
```

**World._process loop order:**
1. Update `_player_chunk_index` from player position.
2. `_generate()` — create and start generating missing chunks (up to max_workers).
3. `_mesh()` — only if no new generate tasks started this frame.
4. `_unload()` — free chunks outside unload_radius.

**Block placement flow:**
1. Player emits `set_block(global_index, type)`.
2. World converts to `chunk_index` + `block_index`.
3. Checks all 4 horizontal neighbors are GENERATED (face culling needs them).
4. `chunk.set_block()` → updates `_all_blocks`, recalculates exposure, updates light.
5. `chunk.mesh(false)` → synchronous remesh of this chunk.
6. Remesh up to 4 adjacent chunks if block was on boundary.
7. `database.set_block()` → persist to SQLite.

**Verify (full playthrough):**
- Chunks generate around player on startup.
- Walking toward new areas generates more chunks; old ones unload.
- Left-click breaks blocks; right-click places selected block.
- Blocks persist after restarting the game.
- Day/night cycle continues from where it left off.
- F3 shows stats. Scroll changes block type. Block wireframe highlights targeted block.

---

## Common Pitfalls

| Problem | Cause | Fix |
|---------|-------|-----|
| Crash: `assert(task_id > 0)` | `_end_generate` called from non-task context | Ensure `generate()` always calls `add_task` |
| Black chunks | Shaders not compiled / spritesheet not loaded | Check `GDCraftResources._ready()` errors |
| No collision | Collision shape not added | Check `_create_collision_shape` and `add_child.call_deferred` |
| Blocks don't persist | DB not saving | Confirm `NOTIFICATION_PREDELETE` triggers on quit |
| Chunks never mesh | Neighbor not GENERATED | Check `_generate_chunks` vs `_mesh_chunks` radius |
| Torch no light | `add_child.call_deferred` missing | Lights must be deferred from worker thread |
| Player falls through | ConcavePolygonShape3D not built | Wait for chunk to be MESHED before allowing physics |
