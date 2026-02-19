# Agent-GameBuilder-Skill

A Godot 4 game workspace with Cursor agent skills for building 2D games—adventure/RPG or Stardew-style farming.

## Skills

| Skill | Focus | Features |
| ----- | ----- | -------- |
| **godot-adventure-rpg** | 2D top-down adventure/RPG | Combat, enemies, NavMesh2D, levels, inventory, HUD, dialogue, save/load, bosses |
| **godot-farming-game** | Stardew-style farming | Crops, fishing, machines, day/night, plants, resources, UI (based on GodewValley) |

- Skills live in `.cursor/skills/`.
- In Cursor, use **@.docs** to pull in Godot engine documentation when working with the agent.

## Project layout

| Path | Description |
| ---- | ----------- |
| `.cursor/skills/` | Agent skills (godot-adventure-rpg, godot-farming-game) |
| `.examples/` | Godot 4.5 example: **GodewValley** (farming game) |
| `.docs/godot-docs-md/` | Godot engine docs (Markdown) |

## Example: GodewValley

- **Engine:** Godot 4.5
- **Run:** Open `.examples/project.godot` in Godot, then run the project (or set `run/main_scene` and press Play).
- **Code:** 24 GDScript files—player, tools, plants, machines (sprinkler, fisher, scarecrow), levels, UI, fishing minigame, and global `Enum` + `Data` autoloads.

## Codebase notes

- **Structure:** Clear separation: global enums/data, scenes for characters, objects, machines, levels, UI, and VFX. Autoloads `Enum` and `Data` are used consistently.
- **Scripts:** Typed variables, signals, and state are handled in a readable way (e.g. `player.gd` with `Enum.State` and tool/machine cycles).
- **Fix applied:** In `global/data.gd`, `MACHINE_UPGRADE_COST` had `'name': 'Sprinkler'` for FISHER and SCARECROW; corrected to `'Fisher'` and `'Scarecrow'`.
