# All Scene Trees

Based on `.examples/godot-craft/scenes/`. Every node, its type, and key properties.

---

## main.tscn

Entry point. Simply loads `world.tscn` as a child (or can just set `world.tscn` as the main scene directly).

```
Node                ← root (or just use world.tscn as main scene)
  World [world.tscn]
```

---

## world.tscn

Root scene for gameplay. All chunk nodes are added at runtime by `world.gd`.

```
World  [Node, world.gd]
  ├── Player  [player.tscn]
  ├── Sky     [sky.tscn]
  ├── Generator  [Node, generator.gd]
  ├── Database   [Node, database.gd]
  └── HUD     [hud.tscn, CanvasLayer]
```

**Signal connections (set up in editor or _ready):**
- `Player.set_block` → `World._on_player_set_block`
- `Player.switch_block` → `HUD._on_player_switch_block`

**World exports (Inspector):**
- `load_radius` = 10
- `unload_radius` = 12
- `player_id` = 0
- `max_workers` = 8

---

## player.tscn

```
Player  [CharacterBody3D, player.gd]
  ├── CollisionShape3D   ← CapsuleShape3D (radius=0.4, height=1.8)
  ├── Head  [Node3D]     ← rotates for vertical look (pitch)
  │     └── RayCast3D   ← target_position=(0,0,-5); detects block face hit
  └── RayCastBlock  [MeshInstance3D]
        ← BoxMesh (size=1,1,1)
        ← StandardMaterial3D: unshaded, alpha, wireframe=true
        ← visible controlled by player.gd (_raycast.is_colliding())
```

**Player exports (Inspector):**
- `walk_speed` = 10.0
- `sprint_speed` = 100.0
- `rotate_speed` = 0.001

**Physics:**
- Layer: 2 (Player)
- Mask: 1 (World / chunks)

---

## sky.tscn

```
GDCraftSky  [Node, sky.gd]
  ├── Sun  [DirectionalLight3D]
  │     ├── shadow_enabled: managed at runtime by sky.gd
  │     └── DirectionalShadowMode: PARALLEL_4_SPLITS (set in editor)
  └── WorldEnvironment
        └── Environment:
              ├── Sky → ProceduralSkyMaterial
              │     (top/horizon colors set at runtime by sky.gd)
              └── Ambient Light → Source=Color
                    (color and energy set at runtime by sky.gd)
```

**Sky exports (Inspector):**
- `sunrise_length` = 30.0, `day_length` = 60.0, `sunset_length` = 30.0, `night_length` = 60.0
- `speed` = 1.0
- Colors: night/sunrise/day/sunset top + horizon, night/day ambient (see sky.gd for defaults)

---

## hud.tscn

```
HUD  [CanvasLayer, hud.gd]
  ├── Stats  [VBoxContainer]   ← hidden by default; toggled with F3
  │     ├── FPS                [Label]
  │     ├── Process            [Label]
  │     ├── PhysicsProcess     [Label]
  │     ├── StaticMemoryUsed   [Label]
  │     ├── VideoMemoryUsed    [Label]
  │     ├── DrawCalls          [Label]
  │     └── Primitives         [Label]
  └── BlockH  [HBoxContainer]  ← current block display (bottom of screen)
        └── BlockV  [VBoxContainer]
              ├── Texture  [TextureRect]
              │     └── AtlasTexture (region updated at runtime from spritesheet)
              └── Label    ← block name (e.g. "Grass", "Red Torch")
```

**Layout tips:**
- `HUD` CanvasLayer: layer=1
- `Stats` VBoxContainer: anchored top-left, small font, visible=false by default
- `BlockH` HBoxContainer: anchored bottom-center; Texture size=48×48 or 64×64

---

## Chunk (runtime-only, no .tscn file)

Chunks are created entirely in code by `World._generate()`. No scene file exists.

```
Chunk  [StaticBody3D, chunk.gd]      ← position = Vector3(_index * Chunk.SIZE)
  ├── [MeshInstance3D]               ← opaque ArrayMesh (added by _mesh, deferred)
  ├── [MeshInstance3D]               ← transparent ArrayMesh (if any transparent blocks)
  ├── [MeshInstance3D]               ← sprite ArrayMesh (if any sprite blocks)
  ├── [CollisionShape3D]             ← ConcavePolygonShape3D from opaque mesh
  └── [OmniLight3D ×N]              ← one per light-emitting block (torches)
```

**Chunk position:** `Vector3(_index.x * Chunk.WIDTH, _index.y * Chunk.HEIGHT, _index.z * Chunk.WIDTH)` — BUT note that in the example `_index.y` is always 0 (the world is a single layer of 128-tall chunks vertically).

**Physics:**
- Layer: 1 (World / Terrain)
- Mask: 0 (chunks don't collide with each other)

---

## Scene connections summary

| Signal | From | To | Method |
|--------|------|----|--------|
| `set_block(index, type)` | Player | World | `_on_player_set_block` |
| `switch_block(type)` | Player | HUD | `_on_player_switch_block` |
| `shoot_projectile` (if added) | future extension | World | custom |

All connections are set up in `world.tscn` editor or in `World._ready()`.
