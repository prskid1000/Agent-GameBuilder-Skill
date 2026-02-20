# Agent-GameBuilder-Skill

A Godot 4 game workspace with Cursor agent skills for building 2D and 3D games.

## Skills

| Skill | Focus | Features |
| ----- | ----- | -------- |
| **godot-adventure-rpg** | 2D top-down adventure/RPG | Combat, enemies, NavMesh2D, levels, inventory, HUD, dialogue, save/load, bosses |
| **godot-farming-game** | Stardew-style 2D farming | Crops, fishing, machines, day/night, plants, resources, UI (based on godot-valley) |
| **godot-open-world** | 3D voxel open-world (Minecraft-style) | Procedural terrain, chunk loading, ArrayMesh, SQLite persistence, day/night sky, torches (based on godot-craft) |

- Skills live in `.cursor/skills/`.
- In Cursor, use **@.docs** to pull in Godot engine documentation when working with the agent.

## Project layout

| Path | Description |
| ---- | ----------- |
| `.cursor/skills/` | Agent skills (godot-adventure-rpg, godot-farming-game, godot-open-world) |
| `.examples/godot-valley/` | Godot 4.6 example: **GodewValley** — 2D top-down farming/life-sim |
| `.examples/godot-craft/` | Godot 4.5 example: **GDCraft** — 3D voxel open-world (Minecraft clone) |
| `.docs/godot-docs-md/` | Godot engine docs (Markdown) |

## Example: godot-valley (GodewValley)

- **Engine:** Godot 4.6 — **Run:** Open `.examples/godot-valley/project.godot`
- **Type:** 2D top-down farming / life-sim (single persistent world)
- **Code:** Player with tool/seed/machine cycling, farming TileMaps (hoe/water/seed), fishing minigame, sprinkler/scarecrow/fisher machines, blob enemies, house/bed day-restart, day/night gradient, rain system, plant info UI. Autoloads: `Enum`, `Data`.

## Example: godot-craft (GDCraft)

- **Engine:** Godot 4.5 — **Run:** Open `.examples/godot-craft/project.godot`
- **Type:** 3D voxel open-world (tiny Minecraft clone)
- **Code:** 10 scripts — `World` (chunk manager), `Chunk` (async generate+mesh with WorkerThreadPool, ArrayMesh, face culling), `Generator` (FastNoiseLite terrain + trees + foliage), `Database` (godot-sqlite: blocks/player/sky persistence), `Player` (CharacterBody3D, first-person, place/break), `Sky` (4-phase day/night with DirectionalLight3D), `Block` + `Face` (static data classes), `HUD` (stats + block display), `GDCraftResources` (Texture2DArray spritesheet + 3 ShaderMaterials). Addon: **godot-sqlite**.

## Codebase notes

- **godot-valley:** Single level scene drives everything (day timer, rain, plant growth, blob spawns). Player emits signals; level reacts. Autoloads `Enum` + `Data` for typed state.
- **godot-craft:** Chunked infinite world. Async generation/meshing with flag-based state machine (GENERATING → GENERATED → MESHING → MESHED). Only player-edited blocks saved to SQLite (procedural terrain regenerated from noise). Three mesh types: OPAQUE, TRANSPARENT, SPRITE.
- **Fix applied (godot-valley):** `global/data.gd` — `MACHINE_UPGRADE_COST` had `'name': 'Sprinkler'` for FISHER and SCARECROW; corrected to `'Fisher'` and `'Scarecrow'`.
