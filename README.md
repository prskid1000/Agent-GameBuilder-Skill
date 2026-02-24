# Game Builder Skill for Claude Code

A generic Godot 4 game-building skill for Claude Code. Covers all game genres (2D and 3D), with every code pattern referencing `.docs/` for correct API syntax.

## Repo Structure

| Path | Description |
|------|-------------|
| `.agents/skills/game-builder/SKILL.md` | Main skill — genre routing, .docs API table, build workflow |
| `.agents/skills/game-builder/references/godot-foundations.md` | Core engine concepts (input, physics, animation, tilemaps, nav, cameras, signals, resources, shaders) |
| `.agents/skills/game-builder/references/2d-games.md` | All 2D genres (platformer, top-down, side-scroller, puzzle/grid) |
| `.agents/skills/game-builder/references/3d-games.md` | All 3D genres (FPS, TPS, voxel, racing, open-world) |
| `.agents/skills/game-builder/references/game-systems.md` | Reusable systems (combat, AI, inventory, dialogue, quests, save/load, audio, UI, multiplayer, procgen) |
| `.docs/godot-docs-md/` | Godot engine docs (Markdown) — skill references these for every API call |

**Branches:** `main` (current), `backup` (original .examples projects preserved)

## How This Skill Was Built

This documents the full process of going from example projects to a polished generic skill. Useful as a guide for creating your own Claude Code skills.

| Step | What | Why | Result |
|------|------|-----|--------|
| **1. Start with examples + docs** | Gathered working Godot projects (`.examples/godot-valley/` 2D farming sim, `.examples/godot-craft/` 3D voxel world) and engine docs (`.docs/godot-docs-md/`) | Real tested code gives concrete patterns to learn from; docs give API reference to verify every call | Working examples + full Godot docs in repo |
| **2. Create skill per project + master** | Built separate skills by studying each project: `godot-adventure-rpg`, `godot-farming-game`, `godot-open-world` — each with architecture plans, scene trees, code patterns, data tables, enums. Plus a master `game-builder` skill routing to the right sub-skill | Each project type needs its own detailed reference; master skill decides which to use based on user description | 3 detailed skills + 1 master router |
| **3. Backup examples, remove them** | Created `backup` branch preserving everything, deleted `.examples/` from `main` | Example projects were large and no longer needed once skills captured their patterns | Skills stand alone without source projects |
| **4. Consolidate into single skill** | Merged all sub-skills into one `game-builder` skill with references as subfolders, removed individual skill folders | Multiple skills had too much duplication (shared Godot concepts, overlapping patterns) | 1 skill with 3 subfolders |
| **5. Consolidate subfolders into files** | Combined each subfolder (5-8 files each: architecture.md, code.md, enums.md, data.md...) into a single file per game type + shared.md for common concepts | Too many granular files; kept hints/architecture/guidelines, removed verbose full code | ~4 files instead of ~20+ |
| **6. Make it generic** | Researched all genres (platformer, FPS, TPS, racing, puzzle, horror...), replaced game-specific files with genre-based ones, added `.docs/` path refs to every code pattern, removed all hardcoded values | Skill was still tied to specific games (farming crops, enemy stats, tile sizes); needed to work for ANY game | 1 universal skill with 5 generic reference files |

## Key Design Principles

| Principle | Description |
|-----------|-------------|
| **Reference .docs for every API call** | Skill points to `.docs/godot-docs-md/classes/class_*.md` paths so the agent verifies correct Godot syntax before writing code |
| **Patterns over code** | Reference files contain architecture hints, scene trees, and short snippets showing the pattern — not full implementations. Agent fills in details per project |
| **Genre routing** | SKILL.md has a decision tree: describe your game, get routed to the right architecture (CharacterBody2D Grounded for platformers, Floating for top-down, CharacterBody3D + SpringArm3D for TPS, etc.) |
| **Separate concerns** | Foundations (engine concepts) separate from genre patterns (2D/3D) separate from reusable systems (combat, inventory, AI). Mix and match per project |
