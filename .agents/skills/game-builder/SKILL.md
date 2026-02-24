---
name: game-builder
description: >
  Complete, self-contained skill for building Godot 4 games of any type:
  2D adventure/RPG, 2D farming/life-sim, 3D voxel open-world, or any hybrid.
  Contains full architecture, code, scenes, enums, data tables, combat systems,
  farming mechanics, voxel chunk rendering, UI, audio, save/load, shaders,
  asset prompts (ComfyUI), and step-by-step build guides for all three game
  archetypes. Diagnoses what the user wants to build, routes to the correct
  references, and can combine mechanics across types (e.g. voxel + RPG combat,
  farming + dungeon, open-world + inventory).
---

# Game Builder — Complete Godot 4 Game Skill

This skill builds complete, production-quality games in Godot 4. It covers three
game archetypes and any hybrid combination. All code, scenes, data, and build
instructions are self-contained in this skill's references.

---

## Quick Start — What Are You Building?

```
Is it 3D?
├── YES → Does it involve placing/breaking blocks or a voxel world?
│         ├── YES → 3D Voxel Open-World  (→ references/3d-voxel/)
│         └── NO  → 3D Voxel base + 2D RPG combat (hybrid)
│
└── NO (2D) → Does it primarily involve:
              ├── Combat, dungeons, bosses, enemies, progression?
              │   → 2D Adventure RPG  (→ references/2d-rpg/)
              ├── Farming, fishing, seasons, crafting, life-sim?
              │   → 2D Farming Game  (→ references/2d-farming/)
              ├── BOTH (farming + combat / dungeon)?
              │   → 2D Farming base + 2D RPG combat (hybrid)
              └── Open overworld with towns / quests?
                  → 2D RPG (level system) + 2D Farming (life-sim)
```

Full genre routing: **[Decision Guide](references/decision-guide.md)**
Feature comparison: **[Feature Matrix](references/feature-matrix.md)**
Hybrid recipes: **[Cross-Skill Patterns](references/cross-skill-patterns.md)**

---

## Reference File Map

### Shared / Universal

| File | Description |
|------|-------------|
| [Decision Guide](references/decision-guide.md) | Genre → game type routing, feature checklist, popular games mapping |
| [Feature Matrix](references/feature-matrix.md) | Every feature compared across all 3 game types |
| [Cross-Skill Patterns](references/cross-skill-patterns.md) | 5 hybrid game recipes with build orders and integration points |
| [Godot Engine Guide](references/godot-engine-guide.md) | Godot editor tutorial: layout, scenes, importing, TileMap, AnimationTree, Camera2D |
| [Godot Concepts](references/godot-concepts.md) | 15 Godot concepts: AnimationTree, TileMapLayer, Resources, @tool, Signals, Tweens, Y-Sort, Shaders |
| [Asset Prompts (ComfyUI)](references/asset-prompts-comfyui.md) | OpenDUI/Flux Kontext/Chatterbox TTS prompts for all game types |

### 2D Adventure RPG (`references/2d-rpg/`)

| File | Description |
|------|-------------|
| [Step-by-Step Build Guide](references/2d-rpg/step-by-step-guide.md) | 16-phase build with exact code: setup → player → combat → enemies → levels → UI → polish |
| [Enums & Data Tables](references/2d-rpg/enums-data.md) | All enums, stat tables, drop tables, PlayerStats resource, EventBus signals |
| [Combat & Enemies](references/2d-rpg/combat-enemies.md) | Melee/ranged/AOE combat, 6 enemy types (Grunt/Archer/Mage/Shield/Exploder/Boss), NavMesh AI |
| [Level Building](references/2d-rpg/level-building.md) | TileMap terrain, rooms, indoor/outdoor, roof fade, transitions, multi-floor dungeons, lighting |
| [UI, Audio & Save](references/2d-rpg/ui-audio-save.md) | HUD, inventory (30-slot drag-drop), dialogue, audio manager, save/load (JSON, 3 slots) |

### 2D Farming / Life-Sim (`references/2d-farming/`)

| File | Description |
|------|-------------|
| [Step-by-Step Build Guide](references/2d-farming/step-by-step-guide.md) | 12-step build: setup → player → level → objects → shaders → UI → plants → house → day/night |
| [Project Config](references/2d-farming/project-config.md) | Full project.godot, input map, physics layers, tile size, autoloads |
| [Enums & Data](references/2d-farming/enums-data.md) | Farming enums (Style/State/Tool/Machine/Seed/Item/Shop), data constants |
| [All Scripts](references/2d-farming/scripts.md) | Full annotated source for ALL scripts: player, level, plant, tree, blob, machines, UI, shaders |
| [All Scene Trees](references/2d-farming/scenes.md) | Complete scene tree for every .tscn file |
| [Scene Files (.tscn)](references/2d-farming/scene-files.md) | Line-by-line .tscn annotations (~1300 lines) |
| [Screen-by-Screen Guide](references/2d-farming/screen-by-screen.md) | Every visual element mapped to its node/script/function |
| [Asset Paths](references/2d-farming/assets.md) | Complete asset path list: characters, tilesets, plants, icons, machines, UI, audio |

### 3D Voxel Open-World (`references/3d-voxel/`)

| File | Description |
|------|-------------|
| [Step-by-Step Build Guide](references/3d-voxel/step-by-step-guide.md) | 11-step build: setup → blocks → shaders → chunks → generator → DB → player → sky → HUD → world |
| [Project Config](references/3d-voxel/project-config.md) | Full project.godot, input map, Jolt Physics, godot-sqlite addon setup |
| [All Scripts](references/3d-voxel/scripts.md) | Full source: block, face, chunk, generator, database, player, sky, hud, world, shaders |
| [All Scene Trees](references/3d-voxel/scenes.md) | Scene tree for world, player, sky, hud, chunk (runtime) |
| [Block Data](references/3d-voxel/block-data.md) | Block types, texture coords, spritesheet layout, transparency/light rules, face culling |

---

## Feature Routing — Find Any Feature

| Feature | Game Type | Reference |
|---------|-----------|-----------|
| **Player movement (2D, 8-dir, AnimationTree)** | 2D RPG / Farming | `2d-rpg/step-by-step-guide.md` Phase 3 |
| **Player movement (3D, first-person)** | 3D Voxel | `3d-voxel/scripts.md` → player.gd |
| **Combat — melee, hitbox, combo** | 2D RPG | `2d-rpg/combat-enemies.md` |
| **Combat — ranged, projectiles** | 2D RPG | `2d-rpg/combat-enemies.md` Phase 6 |
| **Combat — AOE, magic** | 2D RPG | `2d-rpg/combat-enemies.md` Phase 6 |
| **Enemy AI — NavMesh2D pathfinding** | 2D RPG | `2d-rpg/combat-enemies.md` Phase 7 |
| **Enemy types (Grunt/Archer/Mage/Boss)** | 2D RPG | `2d-rpg/combat-enemies.md` Phase 8 |
| **Boss fights with phases** | 2D RPG | `2d-rpg/combat-enemies.md` Phase 12 |
| **Farming tools (hoe/water/seed)** | 2D Farming | `2d-farming/step-by-step-guide.md` Step 6 |
| **Farming machines (sprinkler/scarecrow/fisher)** | 2D Farming | `2d-farming/scripts.md` → machine scripts |
| **Fishing minigame** | 2D Farming | `2d-farming/scripts.md` → fishing_game.gd |
| **Day/night cycle (2D, gradient)** | 2D Farming | `2d-farming/step-by-step-guide.md` Step 11 |
| **Day/night cycle (3D, sky)** | 3D Voxel | `3d-voxel/scripts.md` → sky.gd |
| **Rain system + weather** | 2D Farming | `2d-farming/scripts.md` → level.gd |
| **TileMap terrain autotiling** | 2D RPG / Farming | `2d-rpg/level-building.md` |
| **Plant growth system + resources** | 2D Farming | `2d-farming/scripts.md` → plant_res.gd |
| **Inventory system (grid, drag-drop)** | 2D RPG | `2d-rpg/ui-audio-save.md` Phase 13 |
| **Equipment slots + stats** | 2D RPG | `2d-rpg/enums-data.md` |
| **Dialogue system (typewriter, branching)** | 2D RPG | `2d-rpg/ui-audio-save.md` Phase 13 |
| **Save / load system (JSON)** | 2D RPG | `2d-rpg/ui-audio-save.md` Phase 15 |
| **Audio system (pooled SFX, music crossfade)** | 2D RPG | `2d-rpg/ui-audio-save.md` Phase 14 |
| **Chunk loading (3D voxel)** | 3D Voxel | `3d-voxel/scripts.md` → world.gd + chunk.gd |
| **Procedural terrain (noise)** | 3D Voxel | `3d-voxel/scripts.md` → generator.gd |
| **ArrayMesh block rendering** | 3D Voxel | `3d-voxel/block-data.md` |
| **SQLite persistence** | 3D Voxel | `3d-voxel/scripts.md` → database.gd |
| **Dynamic lighting (torches)** | 3D Voxel | `3d-voxel/block-data.md` → Light Emission |
| **Flash shader (hit feedback)** | 2D Farming (reusable) | `2d-farming/scripts.md` → flash_sprite_2d.gd |
| **Circle wipe transition shader** | 2D Farming (reusable) | `2d-farming/scripts.md` → shaders |
| **Screen shake + hit-stop** | 2D RPG | `2d-rpg/step-by-step-guide.md` Phase 16 |
| **Damage numbers + combo counter** | 2D RPG | `2d-rpg/step-by-step-guide.md` Phase 16 |
| **HUD (HP bar, minimap, hotbar)** | 2D RPG | `2d-rpg/ui-audio-save.md` Phase 13 |
| **Simple HUD (tool/block selector)** | 2D Farm / 3D Voxel | farming: `2d-farming/step-by-step-guide.md` Step 8; voxel: `3d-voxel/scripts.md` → hud.gd |
| **Enums + Data autoloads** | 2D Farming | `2d-farming/enums-data.md` |
| **Event bus (decoupled signals)** | 2D RPG | `2d-rpg/enums-data.md` |

---

## Architecture Overview — All Game Types

### 2D Adventure RPG

```
GameManager (Autoload)          ← global state, scene switching, save/load
  │
  ├── Level_01.tscn             ← first outdoor level
  │     ├── World               Node2D  (tilemap layers, lights)
  │     ├── Entities            Node2D  (player + enemies, y-sorted)
  │     ├── Projectiles         Node2D  (bullets, arrows, spells)
  │     ├── VFX                 Node2D  (hit sparks, explosions)
  │     ├── Doors               Node2D  (level transition triggers)
  │     └── UI                  CanvasLayer
  │
  ├── Dungeon_01_Floor_1.tscn
  ├── Boss_01.tscn
  └── ...
```

**Autoloads:** GameManager, Enum, Data, AudioManager, EventBus
**Physics layers:** Terrain(1), Player(2), Enemy(3), PlayerHitbox(4), EnemyHitbox(5), Projectile(6), Interactable(7), Item(8)

### 2D Farming / Life-Sim

```
Level (Node2D, level.gd)
  ├── Layers/    WaterLayer, GrassLayer, SoilLayer, SoilWaterLayer, RainFloorParticles
  ├── Objects/   Player, ScareCrow, House, Trees×31, SimpleObjects×37
  ├── Overlay/   DayTimeColor, CanvasLayer(DayTransitionLayer, PlantInfoContainer),
  │              RainDropsParticles, MachinePreviewSprite
  ├── Timers/    DayTimer(120s), BlobTimer(20s)
  └── BlobSpawnPositions/  Marker2D×11
```

**Autoloads:** Enum, Data
**Physics layers:** Terrain(1), Player(2), Objects(3), Characters(4)

### 3D Voxel Open-World

```
World (Node, world.gd)          ← chunk manager + orchestrator
  ├── Player (CharacterBody3D)  ← first-person, place/break blocks
  ├── Sky (sky.gd)              ← day/night cycle, DirectionalLight3D
  ├── Generator (generator.gd)  ← terrain noise + tree/foliage
  ├── Database (database.gd)    ← godot-sqlite: blocks, player, sky
  ├── HUD (hud.gd)              ← stats overlay + current block
  └── [Chunk nodes at runtime]  ← StaticBody3D, ArrayMesh, OmniLight3D
```

**Autoloads:** GDCraftResources (shader materials + Texture2DArray)
**Key patterns:** Chunked world (10x128x10), WorkerThreadPool async, ArrayMesh face culling, SQLite persistence, 3 shader types (opaque/transparent/sprite)

---

## Shared Patterns (Reusable Across Any Game Type)

### Flash hit feedback
```gdscript
# Works for any Sprite2D — attach FlashSprite2D child with flash.tres material
func flash(start=0.2, end=0.2, callback=Callable()):
    var tween = create_tween()
    tween.tween_property(material, 'shader_parameter/Progress', 1.0, start)
    if callback.is_valid(): tween.tween_callback(callback)
    tween.tween_property(material, 'shader_parameter/Progress', 0.0, end)
```

### Circle wipe transition
```gdscript
# Reuse for scene transitions, day restarts, boss intros
tween.tween_property(material, "shader_parameter/progress", 1.0, 1.0)
tween.tween_interval(0.5)
tween.tween_callback(do_transition)
tween.tween_property(material, "shader_parameter/progress", 0.0, 1.0)
```

### Day/night color gradient (2D)
- Use `CanvasModulate` + `Gradient` + `DayTimer` sampled in `_process`.
- Gradient points: morning warm → white → white → night blue.

### Day/night sky cycle (3D)
- 4-phase lerp (sunrise/day/sunset/night) on `ProceduralSkyMaterial`.
- `DirectionalLight3D` energy = `clamp(sin(angle), 0, 1)`.

### AnimationTree (2D player)
- BlendTree → MoveStateMachine (Idle/Walk BlendSpace2D) → ToolOneShot → Output.
- Both 2D RPG and 2D Farming use this same structure.

### Async WorkerThreadPool (any heavy computation)
```gdscript
set_flag(Flag.WORKING)
var task_id = WorkerThreadPool.add_task(_heavy_function)
world.add_task_id(task_id)
# In _heavy_function:
_end_function.call_deferred(WorkerThreadPool.get_caller_task_id())
```

---

## Build Workflow by Game Type

### 2D Adventure RPG — 16 Phases
1. Project setup → 2. Global scripts → 3. Player + AnimationTree → 4. Stats + Inventory →
5. Melee combat → 6. Ranged + projectiles → 7. Enemy base → 8. Enemy types →
9. Outdoor level → 10. Indoor/dungeon → 11. Level transitions → 12. Boss fight →
13. UI system → 14. Audio → 15. Save/load → 16. Polish (shake, hit-stop, combo, VFX)

**Full guide:** [references/2d-rpg/step-by-step-guide.md](references/2d-rpg/step-by-step-guide.md)

### 2D Farming Game — 12 Steps
1. Project setup → 2. Enum + Data → 3. Player scene → 4. AnimationTree (editor) →
5. Level + TileMaps → 6. Objects (plant/tree/blob/machines) → 7. Flash + shaders →
8. UI scenes → 9. PlantResource → 10. House scene → 11. Day/night cycle → 12. Final layout

**Full guide:** [references/2d-farming/step-by-step-guide.md](references/2d-farming/step-by-step-guide.md)

### 3D Voxel Open-World — 11 Steps
1. Project + addon → 2. Face + Block classes → 3. Resources autoload → 4. Shaders →
5. Chunk → 6. Generator → 7. Database → 8. Player → 9. Sky → 10. HUD → 11. World + assembly

**Full guide:** [references/3d-voxel/step-by-step-guide.md](references/3d-voxel/step-by-step-guide.md)

### Hybrid Game — Use Cross-Skill Patterns
**[Cross-Skill Patterns](references/cross-skill-patterns.md)** has 5 ready-to-use recipes:
1. Farming + Combat (Rune Factory style)
2. RPG Overworld + Life-Sim Town
3. Voxel + RPG Combat
4. Voxel + Survival Crafting
5. Roguelite Dungeon

---

## Using Godot Engine Documentation (@.docs)

For any Godot API lookup, use the project's `.docs/godot-docs-md/`:

- `classes/class_characterbody2d.md` — 2D player physics
- `classes/class_characterbody3d.md` — 3D player physics
- `classes/class_navigationagent2d.md` — enemy pathfinding
- `classes/class_animationtree.md` — animation state machines
- `classes/class_tilemaplayer.md` — TileMap terrain + custom data
- `classes/class_workerthreadpool.md` — async tasks
- `classes/class_arraymesh.md` — custom 3D mesh building
- `classes/class_fastnoiselite.md` — procedural generation
- `tutorials/` — step-by-step Godot guides

Do not guess Godot API behavior; look it up and cite when relevant.

---

## Incremental Verification (Required)

After every phase/step, the game must run cleanly:
1. Run project (F5) — confirm main scene loads.
2. No runtime or parse errors in Output/Debugger.
3. New behavior is testable (player moves, tools work, chunks generate, etc.).

Fix errors before proceeding. Never leave the project in a broken state.

---

## Animation Standard (Required)

All 2D animations must use **side-by-side horizontal frame strips**:
- One row per action/direction (idle, walk, attack, tool use).
- Frames ordered left-to-right within each row.
- Set `h_frames` = frame count, `v_frames` = row count.
- Prefer `flip_h` for left-facing instead of unique left art.

For 3D voxel: keep block textures as static atlas tiles; this rule applies only to animated assets.

---

## Asset Prompt Generation (ComfyUI)

Generate **independent, complete** prompts for:
- **OpenDUI / OpenDiT** — text-to-image (sprites, tiles, block textures, VFX).
- **Flux Kontext** — image edit / style transfer / character consistency.
- **Chatterbox TTS** — text-to-speech (dialogue, barks, narration).

One prompt per asset; no "same as above". Full rules and examples for all game types:
**[Asset Prompts for ComfyUI](references/asset-prompts-comfyui.md)**

---

## Quick-Start by Game Type

### "I want to make an RPG / action game"
1. Read [references/2d-rpg/step-by-step-guide.md](references/2d-rpg/step-by-step-guide.md)
2. New to Godot? Read [references/godot-engine-guide.md](references/godot-engine-guide.md) first

### "I want to make a farming / life-sim game"
1. Read [references/2d-farming/step-by-step-guide.md](references/2d-farming/step-by-step-guide.md)
2. Reference example at `.examples/godot-valley/`

### "I want to make a Minecraft / voxel / open-world game"
1. Read [references/3d-voxel/step-by-step-guide.md](references/3d-voxel/step-by-step-guide.md)
2. Reference example at `.examples/godot-craft/`
3. Install `addons/godot-sqlite/` (copy from `.examples/godot-craft/addons/`)

### "I want to make a hybrid (e.g. farming + combat)"
1. Read [references/cross-skill-patterns.md](references/cross-skill-patterns.md)
2. Follow the recipe for your hybrid type

### "I don't know what I want yet"
1. Read [references/decision-guide.md](references/decision-guide.md)
2. Answer the genre questions to find the right game type
