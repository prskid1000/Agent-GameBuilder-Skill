---
name: godot-open-world
description: >
  Creates a Godot 4 3D open-world voxel game (Minecraft-style) step by step:
  procedural chunk-based terrain generation (FastNoiseLite), async WorkerThreadPool
  chunk loading/meshing, custom ArrayMesh block rendering with face culling, SQLite
  persistence (player/sky/blocks), 3D first-person player (place/break blocks),
  day/night sky cycle, dynamic torch lighting, HUD, and three shader types
  (opaque, transparent, sprite). Based on the .examples/godot-craft project (GDCraft).
  Use when the user wants an infinite procedural 3D voxel world. When Godot API or
  how-to details are needed, use the project's @.docs (Godot engine docs). Can
  generate independent, complete ComfyUI prompts for assets (OpenDUI, Flux Kontext,
  Chatterbox TTS).
---

# Godot 4 — 3D Open-World Voxel Game Skill

This skill guides building a complete **3D voxel/open-world** game in Godot 4,
matching the `.examples/godot-craft` project (GDCraft — a tiny Minecraft clone).
The agent generates ~95% of all code and scene structure; editor-only wiring is
called out explicitly.

---

## Quick References

- **[Step-by-Step Build Guide — START HERE](references/step-by-step-guide.md)**
- [Project Config, Input Map & Addon Setup](references/project-config.md)
- [All Scripts — Full Source + Line-by-Line Comments](references/scripts.md)
- [All Scene Trees](references/scenes.md)
- [Block Types, Texture Coords, Light & Transparency Rules](references/block-data.md)
- [Asset Prompts for ComfyUI (Spritesheet, OpenDUI, Flux Kontext, Chatterbox TTS)](references/asset-prompts-comfyui.md)

---

## Using Godot engine documentation (@.docs)

When you need to look up Godot APIs, use **@.docs** (`.docs/godot-docs-md/`).

- **When to use:** `WorkerThreadPool`, `ArrayMesh`, `ConcavePolygonShape3D`, `FastNoiseLite`, `CharacterBody3D`, `OmniLight3D`, `ShaderMaterial`, `SQLite` (GDExtension), `Texture2DArray`.
- **How:** Read from `.docs/godot-docs-md/classes/class_*.md` or `tutorials/`.
- Do not guess API when the answer is in @.docs; cite when relevant.

---

## Incremental verification (required)

After every step, the project must run without errors:

1. Run project (F5) — confirm scene loads.
2. No parse or runtime errors in Output/Debugger.
3. New feature is visible/testable (chunk appears, player moves, block places, etc.).

Fix errors before starting the next step.

---

## Asset prompt generation (ComfyUI)

When the user wants **prompts to create or edit assets** (spritesheet, block textures, UI), generate **independent, complete prompts** for:

- **OpenDUI / OpenDiT** — text-to-image (spritesheet rows, torch icons, block textures).
- **Flux Kontext** — image edit / style transfer (texture packs, palette changes).
- **Chatterbox TTS** — text-to-speech (narration, ambient audio scripts).

Each prompt must be standalone. Full rules: **[Asset Prompts for ComfyUI](references/asset-prompts-comfyui.md)**.

---

## Animation standard (required)

For any animated 2D assets used by this skill (UI icons, sprite effects, animated billboards, texture-strip effects), use **side-by-side horizontal frame strips**.

- Layout each animation as one row, with frames ordered left-to-right.
- Use one strip per animation/state; do not stack time-frames vertically for one animation.
- In Godot, set `h_frames` to frame count in the strip and `v_frames` to total row count in the sheet.
- Keep tile textures for voxel blocks as static atlas tiles; this rule applies only to animated assets.

Apply this rule to generated asset prompts and any imported animated sprite sheets.

---

## Architecture Overview

```
main.tscn
  └── World (world.gd)          ← chunk manager + orchestrator
        ├── Player (player.gd)  ← CharacterBody3D, first-person, place/break
        ├── Sky (sky.gd)        ← day/night cycle, DirectionalLight3D, WorldEnvironment
        ├── Generator (generator.gd) ← terrain noise + tree/foliage generation
        ├── Database (database.gd)   ← godot-sqlite: blocks, player, sky persistence
        ├── HUD (hud.gd)             ← stats overlay + current block display
        └── [Chunk nodes added at runtime] (chunk.gd, StaticBody3D)
```

### Key design patterns (godot-craft)

- **Chunked world:** `Chunk.WIDTH=10, HEIGHT=128, SIZE=Vector3i(10,128,10)`. Chunks are `StaticBody3D` nodes added/removed at runtime by `World`.
- **Async generation:** `WorkerThreadPool.add_task()` runs `_generate()` and `_mesh()` off main thread. Flags (`GENERATING`, `GENERATED`, `MESHING`, `MESHED`) prevent race conditions.
- **ArrayMesh:** `Chunk._mesh()` builds `PackedVector3Array` / `PackedVector2Array` / `PackedInt32Array` manually (one face at a time); uploads via `ArrayMesh.add_surface_from_arrays()`.
- **Face culling:** Only exposed faces are emitted. `Block.is_exposed(lhs, rhs)` — face shown if neighbor is EMPTY, a sprite, or a transparent block.
- **Three mesh types:** OPAQUE, TRANSPARENT (water, glass), SPRITE (crosses: bushes, flowers, torches). Each gets its own `MeshInstance3D` + `ShaderMaterial`.
- **Dynamic lights:** Light-emitting blocks (torches) create `OmniLight3D` children on the chunk at exact block positions.
- **SQLite persistence:** `godot-sqlite` GDExtension. Tables: `blocks` (player edits only — not procedural), `players`, `sky`. Loaded in `World._ready()`, saved in `World._notification(PREDELETE)`.
- **GDCraftResources autoload:** Creates `Texture2DArray` from a `spritesheet.png` (16×16 tiles in a grid); shared across all chunk `ShaderMaterial`s.

---

## Build Workflow (follow in order)

### Step 1 — Project Setup + Addon

See **[Project Config](references/project-config.md)** for complete `project.godot`.

- App name `gdcraft`, main scene `res://scenes/main.tscn`.
- Physics engine: `Jolt Physics` (`[physics] 3d/physics_engine="Jolt Physics"`).
- Autoload: `GDCraftResources="*res://scripts/resources.gd"` (no `*` prefix in editor; add `*` in file directly).
- Addon: **godot-sqlite** — copy `addons/godot-sqlite/` from example into project; enable in Editor → Project → Plugins.
- Input map: `forward` (W), `back` (S), `left` (A), `right` (D), `jump` (Space/E), `crouch` (Q/Ctrl), `sprint` (Shift/F), `break` (LMB), `place` (RMB), `debug` (F3), `unfocus` (Esc).

**Verify:** Project opens. No missing addon errors.

---

### Step 2 — Face + Block Classes

**Agent produces:** `scripts/face.gd`, `scripts/block.gd`

`Face` — static class, no `extends`. Enum `Type {FORWARD, BACK, LEFT, RIGHT, UP, DOWN, COUNT}`. Static `_VECTORS` array. `get_vector(face)` returns corresponding `Vector3i`.

`Block` — static class, no `extends`. Enum `Type` (GRASS, DIRT, STONE, WATER, LOG, LEAVES, SAND, BUSH, POPPY, DANDELION, DAISY, CORNFLOWER, MARIGOLD, LAVENDER, RED/YELLOW/GREEN/BLUE/CYAN/MAGENTA/WHITE_TORCH, PLANKS, GLASS, COUNT, EMPTY). Static packed arrays for cube vertices (6 faces × 4 verts), cross-sprite vertices (4 faces × 4 verts), texcoords, normals. Static methods: `get_texcoord(type, face) → Vector2` (spritesheet tile coord), `is_transparent`, `is_sprite`, `is_light`, `get_light_color`, `get_light_strength`, `is_exposed`.

Full source: **[scripts.md → block.gd + face.gd](references/scripts.md)**.

**Verify:** No parse errors. Can reference `Block.Type.GRASS`, `Face.get_vector(Face.Type.UP)` from any script.

---

### Step 3 — GDCraftResources Autoload

**Agent produces:** `scripts/resources.gd`

`extends Node`. Constants: `SPRITESHEET`, `OPAQUE_SHADER`, `TRANSPARENT_SHADER`, `SPRITE_SHADER`, `SIZE = 16`. Vars: `opaque_material`, `transparent_material`, `sprite_material`. `_ready()` calls `_create_spritesheet()` → slices `spritesheet.png` into 16×16 tiles → `Texture2DArray` → assigns to each `ShaderMaterial` as `"spritesheet"` shader parameter.

**Verify:** Autoload node appears in scene tree. No texture load errors.

---

### Step 4 — Shaders

**Agent produces:** `resources/opaque.gdshader`, `resources/transparent.gdshader`, `resources/sprite.gdshader`, `resources/spritesheet.gdshaderinc`

- `spritesheet.gdshaderinc` — shared include: `uniform sampler2DArray spritesheet`. `vec4 get_color(vec2 uv, vec2 tile)` → samples correct layer from array.
- `opaque.gdshader` — `canvas_item` → actually `spatial`, render_mode `cull_back`. Samples spritesheet by `UV` (tile index) + `UV2` (in-tile UV). Discards if `alpha < 0.5`.
- `transparent.gdshader` — same but `render_mode blend_mix` (no discard).
- `sprite.gdshader` — `render_mode cull_disabled, unshaded` (for cross-sprites).

Full GLSL: **[scripts.md → shaders](references/scripts.md)**.

**Verify:** Shaders compile. `GDCraftResources` assigns them to materials without errors.

---

### Step 5 — Chunk

**Agent produces:** `scripts/chunk.gd` (`class_name Chunk extends StaticBody3D`)

Constants: `WIDTH=10`, `HEIGHT=128`, `SIZE=Vector3i(WIDTH,HEIGHT,WIDTH)`.
Flags enum: `NONE, GENERATING, GENERATED, EXPOSED, MESHING, MESHED, WORKING=GENERATING|MESHING`.
MeshType enum: `OPAQUE, TRANSPARENT, SPRITE, COUNT`.
Key vars: `_world`, `_index: Vector3i`, `_flags`, `_all_blocks: Dictionary[Vector3i, Block.Type]`, `_exposed_blocks: Dictionary[Vector3i, bool]`, `_lights: Dictionary[Vector3i, OmniLight3D]`.

Methods: `generate()` (async), `mesh(async, force)` (async or sync), `set_block(index, type)`, `set_light(index, type)`, `get_block(index)`, `_generate()`, `_mesh()`, `_expose()`, `_emit_face()`, `_create_mesh_arrays/instance/collision`, `_end_generate/mesh` (deferred callbacks), flag helpers.

Full source: **[scripts.md → chunk.gd](references/scripts.md)**.

**Verify:** (covered in step 7 when World instantiates chunks).

---

### Step 6 — Generator

**Agent produces:** `scripts/generator.gd` (`class_name Generator extends Node`)

Enum `Type {NOISE, SUPERFLAT, DEBUG}`. Export: `type`, `generator_seed=1337`. Four `FastNoiseLite` instances: `_base_generator` (frequency=0.01), `_overlay_generator` (0.1), `_foliage_generator` (0.05), `_tree_generator` (0.05). Seeds are `generator_seed * 13/79/53/139`.

`generate(index: Vector3i) → Dictionary[Vector3i, Block.Type]` — dispatches to `_noise`, `_superflat`, or `_debug`.

`_noise`: sea_level=10; per (x,z) column: compute height from noise formula, fill stone/dirt/grass/sand/water; place tree or foliage at surface with probability.
`_tree`: LOG trunk (random height 4–8), LEAVES sphere (radius 3, manhattan distance ≤ 3).
`_foliage`: BUSH/POPPY/DANDELION/DAISY/CORNFLOWER/MARIGOLD/LAVENDER by value ranges.

Full source: **[scripts.md → generator.gd](references/scripts.md)**.

**Verify:** Call `generator.generate(Vector3i.ZERO)` from a test script and print keys count. Should be non-empty.

---

### Step 7 — Database

**Agent produces:** `scripts/database.gd` (`class_name Database extends Node`)

Uses `godot-sqlite` (`SQLite` class from addon). Mutex-protected. Opens `user://gdcraft.sqlite` on init. Creates tables: `blocks` (chunk_x/y/z + block_x/y/z + type, PK on all six coords), `players` (id + position xyz + rotation xyz), `sky` (id + time_of_day). Indexes on chunk coords, player id, sky id.

Methods: `set_block(chunk, block, type)` — INSERT OR UPDATE (or DELETE if EMPTY); `get_blocks(chunk) → Array`; `save_player(player, id)`, `load_player(player, id)`, `save_sky(sky)`, `load_sky(sky)`. Mutex locked around every query. `_notification(PREDELETE)` closes DB.

Full source: **[scripts.md → database.gd](references/scripts.md)**.

**Verify:** Run project; `user://gdcraft.sqlite` file is created. No DB errors.

---

### Step 8 — Player

**Agent produces:** `scripts/player.gd` (`class_name Player extends CharacterBody3D`)

Signals: `switch_block(type: Block.Type)`, `set_block(index: Vector3i, type: Block.Type)`.
Exports: `walk_speed=10.0`, `sprint_speed=100.0`, `rotate_speed=0.001`.
Children: `$Head` (Node3D), `$Head/RayCast3D` (ray from head), `$RayCastBlock` (MeshInstance3D wireframe preview).
Vars: `_raycast_break_position`, `_raycast_place_position`, `_block_type`.

`_init()`: sets `position.y=30` (spawn above terrain). `_ready()`: calls `_switch_block(0)`.
`_switch_block(delta)`: cycles `_block_type` by delta, emits `switch_block`.
`_input`: captures mouse on click; on mouse motion → `rotate_y` + `_head.rotate_x`; LMB → `set_block` break; RMB → `set_block` place; scroll → `_switch_block`; Esc → uncapture.
`_physics_process`: WASD direction + up/down; apply sprint_speed; `direction = (_head.global_transform.basis * direction).normalized()`; `velocity = direction * speed`; `move_and_slide()`. Update `_raycast_block` visibility + position from raycast hit.

Full source: **[scripts.md → player.gd](references/scripts.md)**.

**Verify:** Player moves in 3D; mouse look works; scroll cycles block type.

---

### Step 9 — Sky

**Agent produces:** `scripts/sky.gd` (`class_name GDCraftSky extends Node`)

Exports: `sunrise_length=30`, `day_length=60`, `sunset_length=30`, `night_length=60`, `speed=1.0`, plus 8 Color exports for sky top/horizon at each phase + ambient colors.
Children: `$Sun` (DirectionalLight3D), `$WorldEnvironment`.
Var: `time_of_day: float` (0.0–1.0, persisted to DB).

`_init()`: computes phase boundaries (`_sunrise_end`, `_day_end`, etc.).
`_process(delta)`: advances `time_of_day`; sets `_sun.rotation.x = time_of_day * TAU + PI/2`; `_sun.light_energy = clamp(sin(angle), 0, 1)`; `_sun.shadow_enabled = sin_angle > 0`; lerps `top_color`, `horizon_color`, `ambient_color` across 4 phases; sets them on `_sky_material` and `_environment`.

Full source: **[scripts.md → sky.gd](references/scripts.md)**.

**Verify:** Sky color transitions dawn → day → dusk → night. Sun rotates overhead.

---

### Step 10 — HUD

**Agent produces:** `scripts/hud.gd` (`extends Node`)

Children: `$Stats` (VBoxContainer, hidden by default), `$Stats/FPS`, `$Stats/Process`, etc. (Labels), `$BlockH/BlockV/Texture` (TextureRect showing current block), `$BlockH/BlockV/Label` (block name).

`_input`: F3 toggles `$Stats.visible`.
`_process`: reads `Performance` monitors (FPS, process time, physics time, static memory, video memory, draw calls, primitives) → updates labels.
`_on_player_switch_block(type)`: crops `GDCraftResources.SIZE`-px region from spritesheet image, sets on `_block_texture`, capitalizes block name → `_block_label`.

Full source: **[scripts.md → hud.gd](references/scripts.md)**.

**Verify:** HUD shows current block; F3 shows stats overlay.

---

### Step 11 — World

**Agent produces:** `scripts/world.gd` (`class_name World extends Node`)

Exports: `load_radius=10`, `unload_radius=12`, `player_id=0`, `max_workers=8`.
Children (at design time): `$Player`, `$Sky`, `$Generator`, `$Database`, `$HUD`.
Vars: `_chunks: Dictionary[Vector3i, Chunk]`, `_generate_chunks: Array[Vector3i]`, `_mesh_chunks: Array[Vector3i]`, `_player_chunk_index: Vector3i`, `_task_ids: Dictionary[int, bool]`.

`_ready()`: builds `_generate_chunks` list (square `load_radius`), `_mesh_chunks` (one smaller, sorted by distance); loads player + sky from DB.
`_notification(PREDELETE)`: waits for all tasks, saves player + sky.
`_process`: recalculates `_player_chunk_index` from player position; calls `_generate()`, then `_mesh()` (if no new generate tasks), then `_unload()`.
`_generate()`: iterates list; if chunk missing → create + add_child; if not GENERATED and not GENERATING → `chunk.generate()`.
`_mesh()`: iterates list; if GENERATED and not MESHED → `chunk.mesh(true)`.
`_unload()`: erases out-of-bounds chunks not working (waits for meshing neighbors to finish first); frees chunk on worker thread.
`_on_player_set_block(index, type)`: converts global block index → chunk + local block index; calls `chunk.set_block`; remeshes chunk + up to 4 neighbors; calls `database.set_block`.
`_remesh(index)`: forces mesh rebuild on a fully meshed chunk.

Full source: **[scripts.md → world.gd](references/scripts.md)**.

**Verify:** Chunks appear around player on startup; moving generates new chunks; old chunks unload.

---

### Step 12 — Scene Assembly

**Agent produces:** `scenes/main.tscn`, `scenes/world.tscn`, `scenes/player.tscn`, `scenes/sky.tscn`, `scenes/hud.tscn`

See **[scenes.md](references/scenes.md)** for full node hierarchies.

Key wiring:
- `World` connects `Player.set_block → World._on_player_set_block`.
- `World` connects `Player.switch_block → HUD._on_player_switch_block`.
- `World._ready()` calls `database.load_player(_player, player_id)` and `database.load_sky(_sky)`.

**Verify:** Full playthrough — walk around, see terrain generate, place/break blocks, blocks persist after restart. F3 shows stats. Day/night cycle runs.

---

## User-Only Editor Tweaks

### DirectionalLight3D (Sun)

In `Sky` scene → `$Sun` node:
- Shadow: enabled (managed by script at runtime)
- `DirectionalShadowMode`: set to `PARALLEL_4_SPLITS` for quality
- Inspector → Rendering → `Soft Shadow Filter Quality` should match `project.godot` setting (3 = Soft Low)

### WorldEnvironment

In `Sky` scene → `$WorldEnvironment`:
- `Environment` → `Sky` → `PhysicalSkyMaterial` OR `ProceduralSkyMaterial`
- For `ProceduralSkyMaterial`: `sky_top_color`, `sky_horizon_color`, `ground_bottom_color`, `ground_horizon_color` are set at runtime by `sky.gd`
- `Ambient Light` → `Source = Color` (managed by script)

### RayCastBlock (wireframe block preview)

In Player scene → `$RayCastBlock`:
- `MeshInstance3D` with a `BoxMesh` (size=1,1,1)
- Material → `StandardMaterial3D` → `Shading Mode = Unshaded`, `Transparency = Alpha`, `Albedo Color = (1,1,1,0.3)`, `Wireframe = true`

### Collision Layer Setup

- Player: Layer 2 (Player), Mask 1 (World)
- Chunk (StaticBody3D): Layer 1 (World), Mask 0

### SQLite Plugin

1. Copy `addons/godot-sqlite/` into your project.
2. Editor → Project → Plugins → enable `godot-sqlite`.
3. The `SQLite` class becomes available globally.
