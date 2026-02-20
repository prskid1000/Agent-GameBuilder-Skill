# Block Types, Texture Coords, Light & Transparency Rules

Complete reference for all block data used in `block.gd` and the spritesheet.

---

## Block.Type Enum

| Value | Name | Category | Notes |
|-------|------|----------|-------|
| 0 | GRASS | Solid | Top=grass, sides=grass-side, bottom=dirt |
| 1 | DIRT | Solid | All sides: dirt texture |
| 2 | STONE | Solid | All sides: stone texture |
| 3 | WATER | Transparent | Rendered with `transparent.gdshader`; alpha blended |
| 4 | LOG | Solid | Top/bottom=log-end, sides=bark texture |
| 5 | LEAVES | Solid (cutout) | Alpha discard (opaque shader, but has holes) |
| 6 | SAND | Solid | Beach / underwater surface |
| 7 | BUSH | Sprite | Cross-shape, no collision |
| 8 | POPPY | Sprite | Cross-shape, no collision |
| 9 | DANDELION | Sprite | Cross-shape, no collision |
| 10 | DAISY | Sprite | Cross-shape, no collision |
| 11 | CORNFLOWER | Sprite | Cross-shape, no collision |
| 12 | MARIGOLD | Sprite | Cross-shape, no collision |
| 13 | LAVENDER | Sprite | Cross-shape, no collision |
| 14 | RED_TORCH | Sprite + Light | OmniLight3D color=(1,0,0) |
| 15 | YELLOW_TORCH | Sprite + Light | OmniLight3D color=(1,1,0) |
| 16 | GREEN_TORCH | Sprite + Light | OmniLight3D color=(0,1,0) |
| 17 | BLUE_TORCH | Sprite + Light | OmniLight3D color=(0,0,1) |
| 18 | CYAN_TORCH | Sprite + Light | OmniLight3D color=(0,1,1) |
| 19 | MAGENTA_TORCH | Sprite + Light | OmniLight3D color=(1,0,1) |
| 20 | WHITE_TORCH | Sprite + Light | OmniLight3D color=(1,1,1) |
| 21 | PLANKS | Solid | Wood planks, all sides same |
| 22 | GLASS | Transparent | Alpha blended, all sides same |
| 23 | COUNT | Sentinel | Used for cycling/iteration (not a real block) |
| 24 | EMPTY | Air | No geometry; erases block from dict |

---

## Texture Coordinate Map (Spritesheet)

`Block.get_texcoord(type, face)` returns `Vector2(column, row)` — tile index in spritesheet grid.
Shader converts this to a `Texture2DArray` layer index: `layer = row * columns_per_row + column`.

### Row 0 (y=0)

| Column (x) | Block | Face condition |
|------------|-------|---------------|
| 0 | GRASS top | Face.UP |
| 1 | DIRT | (all) / GRASS bottom |
| 2 | GRASS side | other faces |
| 3 | STONE | all |
| 4 | WATER | all |
| 5 | LOG top/bottom | Face.UP or DOWN |
| 6 | LOG side (bark) | other faces |
| 7 | LEAVES | all |
| 8 | SAND | all |
| 9 | BUSH | all |
| 10 | POPPY | all |
| 11 | DANDELION | all |
| 12 | DAISY | all |
| 13 | CORNFLOWER | all |
| 14 | MARIGOLD | all |
| 15 | LAVENDER | all |

### Row 1 (y=1)

| Column (x) | Block |
|------------|-------|
| 0 | YELLOW_TORCH |
| 1 | RED_TORCH |
| 2 | BLUE_TORCH |
| 3 | GREEN_TORCH |
| 4 | CYAN_TORCH |
| 5 | MAGENTA_TORCH |
| 6 | WHITE_TORCH |
| 7 | PLANKS |
| 8 | GLASS |

---

## Spritesheet Layout

```
spritesheet.png  — 16×N pixels per tile, minimum 2 rows:

Row 0 (y=0):  [GRASS-top][DIRT][GRASS-side][STONE][WATER][LOG-top][LOG-side][LEAVES][SAND][BUSH][POPPY][DANDELION][DAISY][CORNFLOWER][MARIGOLD][LAVENDER]
Row 1 (y=1):  [YELLOW_TORCH][RED_TORCH][BLUE_TORCH][GREEN_TORCH][CYAN_TORCH][MAGENTA_TORCH][WHITE_TORCH][PLANKS][GLASS]
```

- Each tile: exactly 16×16 pixels.
- Total minimum size: 256×32 pixels (16 columns × 16px = 256px wide; 2 rows × 16px = 32px tall).
- `GDCraftResources._create_spritesheet()` slices this into a `Texture2DArray` with `SIZE=16`.
- Alpha channel required for LEAVES, sprites (torches, flowers) and GLASS.

---

## Transparency Rules

`Block.is_transparent(type)`:

| Block | Transparent |
|-------|-------------|
| WATER | ✓ |
| GLASS | ✓ |
| (all others) | ✗ |

`Block.is_sprite(type)` — rendered as cross-shape, always treated as "exposed" for culling:

All flowers (BUSH, POPPY, DANDELION, DAISY, CORNFLOWER, MARIGOLD, LAVENDER) + all torches (7 colors).

### Face exposure rule (`Block.is_exposed(lhs, rhs)`):

| lhs \ rhs | EMPTY | Sprite | Transparent | Opaque |
|-----------|-------|--------|-------------|--------|
| Opaque | ✓ draw | ✓ draw | ✓ draw | ✗ cull |
| Transparent | ✓ draw | ✓ draw | ✗ cull | ✓ draw |
| Sprite | always drawn (handled separately, never calls is_exposed) | — | — | — |

---

## Light Emission

`Block.is_light(type)` → true for all 7 torch colors.

All torches use the same strength: `Vector3(omni_range=5, omni_attenuation=0.02, light_energy=1.0)`.

Light colors:

| Block | Color (RGB) |
|-------|-------------|
| YELLOW_TORCH | (1.0, 1.0, 0.0) |
| RED_TORCH | (1.0, 0.0, 0.0) |
| BLUE_TORCH | (0.0, 0.0, 1.0) |
| GREEN_TORCH | (0.0, 1.0, 0.0) |
| CYAN_TORCH | (0.0, 1.0, 1.0) |
| MAGENTA_TORCH | (1.0, 0.0, 1.0) |
| WHITE_TORCH | (1.0, 1.0, 1.0) |

OmniLight3D is created at world-space center of the block: `Vector3(_chunk._index * Chunk.SIZE + block_index) + Vector3.ONE / 2`.

---

## Vertex Layout (Cube Faces)

Each face has 4 vertices (a quad), rendered as 2 triangles using indices `[0,1,2, 0,2,3]`.

Face order matches `Face.Type` enum:

| Face | Direction | Vertices (local block coords, unit cube) |
|------|-----------|------------------------------------------|
| FORWARD (+Z) | `(0,1,1)` `(1,1,1)` `(1,0,1)` `(0,0,1)` |
| BACK (-Z) | `(1,1,0)` `(0,1,0)` `(0,0,0)` `(1,0,0)` |
| LEFT (-X) | `(0,1,0)` `(0,1,1)` `(0,0,1)` `(0,0,0)` |
| RIGHT (+X) | `(1,1,1)` `(1,1,0)` `(1,0,0)` `(1,0,1)` |
| UP (+Y) | `(0,1,0)` `(1,1,0)` `(1,1,1)` `(0,1,1)` |
| DOWN (-Y) | `(0,0,1)` `(1,0,1)` `(1,0,0)` `(0,0,0)` |

World position of vertex = `Vector3(chunk._index * Chunk.SIZE + block_index) + vertex`.

---

## Chunk Size Constants

```gdscript
Chunk.WIDTH  = 10          # blocks per side (X and Z)
Chunk.HEIGHT = 128         # blocks tall (Y)
Chunk.SIZE   = Vector3i(10, 128, 10)
```

A chunk covers world area: `[index.x * 10, (index.x+1) * 10)` in X and Z.
The world is a single row of chunks in Y (index.y == 0 always in the example).

---

## Generator Height Formula

```
base_noise = (FastNoiseLite(freq=0.01).get_noise_2d(x, z) + 1.0) * 0.5   # [0..1]
overlay_noise = (FastNoiseLite(freq=0.1).get_noise_2d(x, z) + 1.0) * 0.5  # [0..1]
noise = int(pow(base_noise * 5, 1.25) * 5 + overlay_noise * 2)             # terrain height Y
sea_level = 10
```

Surface block assignment:
- `y > noise`: WATER
- near sea level (sand condition): SAND
- `y > 20 + overlay*2` (high altitude): STONE at surface
- `y == noise-1`: GRASS (surface)
- `y > noise-4`: DIRT (shallow sub-surface)
- else: STONE (deep)
