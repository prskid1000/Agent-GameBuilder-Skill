# .games

Godot 4 game workspace with Cursor agent skills and example projects.

## Skills (Agent)

- **godot-adventure-rpg** — 2D top-down adventure/RPG: combat, enemies, NavMesh2D, levels, inventory, HUD, dialogue, save/load, bosses.
- **godot-farming-game** — Stardew-style farming: crops, fishing, machines, day/night, plants, resources, UI (based on GodewValley example).

Skills live in `.cursor/skills/` and use `@.docs` for Godot engine documentation.

## Project layout

| Path | Description |
|------|-------------|
| `.cursor/skills/` | Agent skills (godot-adventure-rpg, godot-farming-game) |
| `.examples/` | Godot 4.5 example: **GodewValley** (farming game) |
| `.docs/godot-docs-md/` | Godot engine docs (Markdown) |

## Example: GodewValley

- **Engine:** Godot 4.5  
- **Run:** Open `.examples/project.godot` in Godot and run, or set `run/main_scene` and press Play.  
- **Code:** 24 GDScript files — player, tools, plants, machines (sprinkler, fisher, scarecrow), levels, UI, fishing minigame, global `Enum` + `Data` autoloads.

## Code check (summary)

- **Structure:** Clear separation (global enums/data, scenes for characters/objects/machines/levels/UI/vfx). Autoloads `Enum` and `Data` used consistently.
- **Scripts:** Typed vars, signals, and state handled in a readable way (e.g. `player.gd` with `Enum.State` and tool/machine cycles).
- **Fix applied:** In `global/data.gd`, `MACHINE_UPGRADE_COST` had `'name': 'Sprinkler'` for FISHER and SCARECROW; corrected to `'Fisher'` and `'Scarecrow'`.
