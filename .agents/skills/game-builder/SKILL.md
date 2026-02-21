---
name: game-builder
description: >
  Master skill that orchestrates all other Godot 4 game skills in this workspace.
  Use this skill FIRST for any new game project. It diagnoses what the user wants
  to build, selects the right skill(s), extracts the best features across all skills,
  and can combine mechanics from multiple skills (e.g. voxel world + RPG combat,
  farming + dungeon, open-world + inventory). Covers all Godot 4 game genres:
  2D adventure/RPG, 2D farming/life-sim, 3D voxel open-world, and any hybrid.
  Routes to the correct skill references automatically.
---

# Game Builder — Master Skill

**Read this skill first for any new game project.** This skill diagnoses the user's
game concept, picks the right skill(s) from this workspace, and routes to the exact
references needed. It also knows how to combine features across skills for hybrid games.

---

## Available Skills in This Workspace

| Skill | Path | Type | Example Project |
|-------|------|------|----------------|
| **godot-adventure-rpg** | `.cursor/skills/godot-adventure-rpg/` | 2D top-down action RPG | — |
| **godot-farming-game** | `.cursor/skills/godot-farming-game/` | 2D farming / life-sim | `.examples/godot-valley/` |
| **godot-open-world** | `.cursor/skills/godot-open-world/` | 3D voxel / Minecraft-style | `.examples/godot-craft/` |

---

## Step 1 — Diagnose the Game

When the user describes a game, answer these questions to route to the right skill(s):

### Quick decision tree

```
Is it 3D?
├── YES → Does it involve placing/breaking blocks or a voxel world?
│         ├── YES → godot-open-world
│         └── NO  → godot-open-world as base + RPG combat from godot-adventure-rpg
│
└── NO (2D) → Does it primarily involve:
              ├── Combat, dungeons, bosses, enemies, progression?
              │   → godot-adventure-rpg
              ├── Farming, fishing, seasons, crafting, life-sim activities?
              │   → godot-farming-game
              ├── BOTH (farming + combat / dungeon)?
              │   → godot-farming-game (base) + godot-adventure-rpg (combat phases)
              └── Open overworld with multiple biomes / towns / quests?
                  → godot-adventure-rpg (level system) + godot-farming-game (life-sim)
```

See **[Decision Guide](references/decision-guide.md)** for the full genre matrix and hybrid patterns.

---

## Step 2 — Load the Right Skill(s)

Once the game type is identified, **read the chosen skill's SKILL.md immediately**:

| Game type | Read first |
|-----------|-----------|
| Pure RPG / action / dungeon | `.cursor/skills/godot-adventure-rpg/SKILL.md` |
| Pure farming / life-sim | `.cursor/skills/godot-farming-game/SKILL.md` |
| Pure 3D voxel / open-world | `.cursor/skills/godot-open-world/SKILL.md` |
| Hybrid (any combination) | Read both relevant SKILL.mds; see [Cross-Skill Patterns](references/cross-skill-patterns.md) |

---

## Step 3 — Feature Routing

Use the table below to find the **exact reference file** for any feature, regardless of which skill it comes from.

| Feature | Skill | Reference file |
|---------|-------|---------------|
| **Player movement (2D, 8-dir, AnimationTree)** | adventure-rpg / farming | `godot-adventure-rpg/references/step-by-step-guide.md` Phase 3 |
| **Player movement (3D, first-person)** | open-world | `godot-open-world/references/scripts.md` → player.gd |
| **Combat — melee, hitbox, combo** | adventure-rpg | `godot-adventure-rpg/references/combat-enemies.md` |
| **Combat — ranged, projectiles** | adventure-rpg | `godot-adventure-rpg/references/combat-enemies.md` Phase 6 |
| **Combat — AOE, magic** | adventure-rpg | `godot-adventure-rpg/references/combat-enemies.md` Phase 6 |
| **Enemy AI — NavMesh2D pathfinding** | adventure-rpg | `godot-adventure-rpg/references/combat-enemies.md` Phase 7 |
| **Enemy types (Grunt/Archer/Mage/Boss)** | adventure-rpg | `godot-adventure-rpg/references/combat-enemies.md` Phase 8 |
| **Boss fights with phases** | adventure-rpg | `godot-adventure-rpg/references/combat-enemies.md` Phase 12 |
| **Farming tools (hoe/water/seed)** | farming | `godot-farming-game/references/step-by-step-guide.md` Step 6 |
| **Farming machines (sprinkler/scarecrow/fisher)** | farming | `godot-farming-game/references/scripts.md` → machine scripts |
| **Fishing minigame** | farming | `godot-farming-game/references/scripts.md` → fishing_game.gd |
| **Day/night cycle (2D, gradient)** | farming | `godot-farming-game/references/step-by-step-guide.md` Step 11 |
| **Day/night cycle (3D, sky)** | open-world | `godot-open-world/references/scripts.md` → sky.gd |
| **Rain system + weather** | farming | `godot-farming-game/references/scripts.md` → level.gd |
| **TileMap terrain autotiling** | farming / adventure-rpg | `godot-adventure-rpg/references/level-building.md` |
| **Plant growth system + resources** | farming | `godot-farming-game/references/scripts.md` → plant_res.gd |
| **Inventory system (grid, drag-drop)** | adventure-rpg | `godot-adventure-rpg/references/ui-audio-save.md` Phase 13 |
| **Equipment slots + stats** | adventure-rpg | `godot-adventure-rpg/references/enums-data.md` |
| **Dialogue system (typewriter, branching)** | adventure-rpg | `godot-adventure-rpg/references/ui-audio-save.md` Phase 13 |
| **Save / load system** | adventure-rpg | `godot-adventure-rpg/references/ui-audio-save.md` Phase 15 |
| **Audio system (pooled SFX, music crossfade)** | adventure-rpg | `godot-adventure-rpg/references/ui-audio-save.md` Phase 14 |
| **Chunk loading (3D voxel)** | open-world | `godot-open-world/references/scripts.md` → world.gd + chunk.gd |
| **Procedural terrain (noise)** | open-world | `godot-open-world/references/scripts.md` → generator.gd |
| **ArrayMesh block rendering** | open-world | `godot-open-world/references/block-data.md` |
| **SQLite persistence** | open-world | `godot-open-world/references/scripts.md` → database.gd |
| **Dynamic lighting (torches)** | open-world | `godot-open-world/references/block-data.md` → Light Emission |
| **Flash shader (hit feedback)** | farming | `godot-farming-game/references/scripts.md` → flash_sprite_2d.gd |
| **Circle wipe transition shader** | farming / adventure-rpg | `godot-farming-game/references/scripts.md` → shaders |
| **Screen shake + hit-stop** | adventure-rpg | `godot-adventure-rpg/references/step-by-step-guide.md` Phase 16 |
| **Damage numbers + combo counter** | adventure-rpg | `godot-adventure-rpg/references/step-by-step-guide.md` Phase 16 |
| **HUD (HP bar, minimap, hotbar)** | adventure-rpg | `godot-adventure-rpg/references/ui-audio-save.md` Phase 13 |
| **Simple HUD (tool/block selector)** | farming / open-world | farming: `step-by-step-guide.md` Step 8; open-world: `scripts.md` → hud.gd |
| **Enums + Data autoloads** | farming | `godot-farming-game/references/enums-data.md` |
| **Event bus (decoupled signals)** | adventure-rpg | `godot-adventure-rpg/references/enums-data.md` |
| **Godot engine guide (editor, TileMap, etc.)** | adventure-rpg | `godot-adventure-rpg/references/godot-engine-guide.md` |
| **Asset prompts (ComfyUI / OpenDUI / TTS)** | all | each skill's `references/asset-prompts-comfyui.md` |

Full cross-skill comparison: **[Feature Matrix](references/feature-matrix.md)**

---

## Step 4 — Hybrid Game Patterns

If the user's game is a hybrid (e.g. farming + combat, voxel + RPG), use the pre-built combination patterns:

| Hybrid | Pattern |
|--------|---------|
| Farming + combat/enemies | Use **farming-game** as base; graft **adventure-rpg** combat phases (5–8) |
| RPG overworld + towns | Use **adventure-rpg** level system; add **farming-game** NPC/life-sim loop |
| Voxel + RPG | Use **open-world** as base; add **adventure-rpg** combat (melee/ranged) and enemy AI |
| Voxel + survival crafting | Use **open-world** as base; add **farming-game** resource/crafting loop |
| Roguelite dungeon | Use **adventure-rpg**; use procedural room generation (level-building.md) + farming's day-reset pattern |

Detailed combination recipes: **[Cross-Skill Patterns](references/cross-skill-patterns.md)**

---

## Step 5 — Shared Patterns (Apply to Any Skill)

These patterns appear in multiple skills and can be reused anywhere:

### Flash hit feedback
Source: `godot-farming-game/references/scripts.md` → `flash_sprite_2d.gd`
```gdscript
# Works for any Sprite2D — attach as child, give it the flash.tres material
func flash(start=0.2, end=0.2, callback=Callable()):
    var tween = create_tween()
    tween.tween_property(material, 'shader_parameter/Progress', 1.0, start)
    if callback.is_valid(): tween.tween_callback(callback)
    tween.tween_property(material, 'shader_parameter/Progress', 0.0, end)
```

### Circle wipe transition
Source: `godot-farming-game/references/scripts.md` → `circle_transition.gdshader`
```gdscript
# Reuse in any game for scene transitions, day restarts, boss intros
tween.tween_property(material, "shader_parameter/progress", 1.0, 1.0)
tween.tween_interval(0.5)
tween.tween_callback(do_transition)
tween.tween_property(material, "shader_parameter/progress", 0.0, 1.0)
```

### Day/night color gradient (2D)
Source: `godot-farming-game/references/step-by-step-guide.md` Step 11
- Use `CanvasModulate` + `Gradient` + `DayTimer` sampled in `_process`.
- Gradient points: morning warm → white → white → night blue.

### Day/night sky cycle (3D)
Source: `godot-open-world/references/scripts.md` → `sky.gd`
- 4-phase lerp (sunrise/day/sunset/night) on `ProceduralSkyMaterial`.
- `DirectionalLight3D` energy = `clamp(sin(angle), 0, 1)`.

### AnimationTree (2D player)
Source: `godot-adventure-rpg/references/step-by-step-guide.md` Phase 3 + `godot-farming-game/references/step-by-step-guide.md` Step 4
- BlendTree → MoveStateMachine (Idle/Walk BlendSpace2D) → ToolOneShot → Output.
- Both skills use the same structure; farming adds FishBlend layer.

### Async WorkerThreadPool pattern (any heavy computation)
Source: `godot-open-world/references/scripts.md` → `chunk.gd`
```gdscript
# Use for any slow generation: dungeon rooms, pathfinding, asset loading
set_flag(Flag.WORKING)
var task_id = WorkerThreadPool.add_task(_heavy_function)
world.add_task_id(task_id)
# In _heavy_function:
_end_function.call_deferred(WorkerThreadPool.get_caller_task_id())
```

---

## Step 6 — Godot Engine Guide

If the user is new to Godot or needs help with the editor, importing assets, TileMaps, or scene manipulation, read:

**`.cursor/skills/godot-adventure-rpg/references/godot-engine-guide.md`**

This guide covers: Godot project setup, scene tree, node types, import pipeline, TileSet/TileMap setup, AnimationPlayer/AnimationTree, NavigationRegion2D, PhysicsLayers, and common gotchas.

---

## Step 7 — Using @.docs

For any Godot API lookup, use the project's **@.docs** (`.docs/godot-docs-md/`):

- `classes/class_characterbody2d.md` — 2D player physics
- `classes/class_characterbody3d.md` — 3D player physics
- `classes/class_navigationagent2d.md` — enemy pathfinding
- `classes/class_animationtree.md` — animation state machines
- `classes/class_tilemaplayer.md` — TileMap terrain + custom data
- `classes/class_workerthreadpool.md` — async tasks
- `classes/class_arraymesh.md` — custom 3D mesh building
- `classes/class_fastnoiselite.md` — procedural generation
- `tutorials/` — step-by-step Godot guides

---

## Step 8 — Asset Prompt Generation

When generating art or audio assets, use the skill-specific prompt files:

| Asset type | Prompt file |
|------------|------------|
| 2D sprites, tiles, characters, VFX | `godot-adventure-rpg/references/asset-prompts-comfyui.md` |
| Farming tiles, plant sprites, icons | `godot-farming-game/references/assets.md` |
| 3D voxel spritesheet (block textures) | `godot-open-world/references/asset-prompts-comfyui.md` |

All prompts use: **OpenDUI / OpenDiT** (text-to-image), **Flux Kontext** (edit/restyle), **Chatterbox TTS** (dialogue/audio).

---

## Quick-Start by Game Type

### "I want to make an RPG / action game"
1. Read `.cursor/skills/godot-adventure-rpg/SKILL.md`
2. Start with Phase 1 in `godot-adventure-rpg/references/step-by-step-guide.md`
3. New to Godot? Read `godot-adventure-rpg/references/godot-engine-guide.md` first

### "I want to make a farming / life-sim game"
1. Read `.cursor/skills/godot-farming-game/SKILL.md`
2. Start with Step 1 in `godot-farming-game/references/step-by-step-guide.md`
3. Reference example at `.examples/godot-valley/` — run `project.godot` to see the finished game

### "I want to make a Minecraft / voxel / open-world game"
1. Read `.cursor/skills/godot-open-world/SKILL.md`
2. Start with Step 1 in `godot-open-world/references/step-by-step-guide.md`
3. Reference example at `.examples/godot-craft/` — run `project.godot` to see the finished game
4. Install `addons/godot-sqlite/` (copy from `.examples/godot-craft/addons/`)

### "I want to make a hybrid (e.g. farming + combat)"
1. Read `.cursor/skills/game-builder/references/cross-skill-patterns.md`
2. Follow the recipe for your hybrid type
3. Load both parent skill SKILL.mds for their full references

### "I don't know what I want yet"
1. Read `.cursor/skills/game-builder/references/decision-guide.md`
2. Answer the genre questions → get routed to the right skill(s)
