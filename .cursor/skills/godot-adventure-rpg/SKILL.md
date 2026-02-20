---
name: godot-adventure-rpg
description: >
  Complete skill for building a 2D top-down adventure/RPG game in Godot 4.
  Covers player movement and animation trees, full combat (melee, ranged shooting,
  magic projectiles, AOE), multi-type enemy AI with NavMesh2D pathfinding, multiple
  levels with indoor/outdoor environments and complex room layouts, inventory and
  equipment system, HUD, dialogue, save/load, audio, screen shake, damage numbers,
  combo counter, boss fights with phases — all AAA concepts adapted for 2D.
  Also includes a Godot Engine guide for users who need help with the editor,
  asset importing, scene manipulation, and TileMap building. When Godot API or
  how-to details are needed, use the project's @.docs (Godot engine docs). Can
  generate independent, complete ComfyUI prompts for assets (OpenDUI, Flux Kontext,
  Chatterbox TTS).
---

# Godot 4 — 2D Adventure / RPG Game Skill

This skill generates a complete, production-quality 2D adventure/RPG. It is designed to
produce ~95% of all code and scene setup, leaving only art-asset painting and fine-tuning
to the user.

---

## Quick References

- **[Godot Engine Guide — Editor, Assets, Scenes](references/godot-engine-guide.md)** ← start here if new to Godot
- **[Step-by-Step Build Guide (all phases + code)](references/step-by-step-guide.md)** ← main build document
- [Enums, Data Tables & Stats](references/enums-data.md)
- [Combat System — Melee, Ranged, Projectiles, AOE, Bosses](references/combat-enemies.md)
- [Level Building — TileMap, Rooms, Indoor/Outdoor, Transitions](references/level-building.md)
- [UI, Inventory, Dialogue, Audio, Save System](references/ui-audio-save.md)
- [Asset prompts for ComfyUI (OpenDUI, Flux Kontext, Chatterbox TTS)](references/asset-prompts-comfyui.md)

---

## Using Godot engine documentation (@.docs)

When you need to **look up Godot APIs, classes, tutorials, or how to implement something**, use the project’s **@.docs** (or path `.docs/godot-docs-md/`). It contains the full Godot engine documentation in Markdown.

- **When to use:** Figuring out class methods/signals, node usage, TileMap/NavigationRegion2D/AnimationTree setup, shaders, input, saving, etc.
- **How:** Reference or read from `.docs/godot-docs-md/` — e.g. `classes/class_*.md` for class reference, `tutorials/` for step-by-step guides.
- **Search:** Use semantic or grep search under `.docs/godot-docs-md/` for topics (e.g. CharacterBody2D, NavigationAgent2D, AnimatedTexture).

Do not guess Godot API or node behavior when the answer is in @.docs; look it up and cite the doc when relevant.

---

## Asset prompt generation (ComfyUI)

When the user wants **prompts to create or edit assets** (sprites, tiles, icons, dialogue audio), generate **independent, complete prompts** for:

- **OpenDUI / OpenDiT** — text-to-image (sprites, tiles, portraits, VFX).
- **Flux Kontext** — image edit / style transfer / character consistency.
- **Chatterbox TTS** — text-to-speech (dialogue lines, barks, narration).

Use **one prompt per asset** (or one `PROMPTS.md` per folder listing each asset and its full prompt). Each prompt must be standalone — no “same as above” or implicit context.

Full rules, examples, and per-folder vs per-asset layout: **[Asset prompts for ComfyUI](references/asset-prompts-comfyui.md)**.

---

## Animation standard (required)

All 2D animations must use **side-by-side horizontal frame strips**.

- Layout each animation as one row, with frames ordered left-to-right.
- Use one strip per action/direction (idle, walk, attack, hurt, etc.); do not stack time-frames vertically for one animation.
- In Godot, set `h_frames` to frame count in the strip and `v_frames` to total row count in the sheet.
- Prefer reusing right-facing strips with `flip_h` for left-facing motion unless unique left art is required.

Apply this rule to player, enemies, VFX spritesheets, and any generated asset prompts.

---

## Game Architecture Overview

```
GameManager (Autoload)          ← global state, scene switching, save/load
  │
  ├── Level_01.tscn             ← first outdoor level
  │     ├── World               Node2D  (tilemap layers, lights)
  │     ├── Entities            Node2D  (player + all enemies, y-sorted)
  │     ├── Projectiles         Node2D  (bullets, arrows, spells — NOT y-sorted)
  │     ├── VFX                 Node2D  (hit sparks, blood, explosions)
  │     ├── Doors               Node2D  (level transition triggers)
  │     └── UI                  CanvasLayer
  │
  ├── Dungeon_01_Floor_1.tscn   ← indoor dungeon, floor 1
  ├── Dungeon_01_Floor_2.tscn   ← indoor dungeon, floor 2 (harder)
  ├── Boss_01.tscn              ← boss arena
  └── ...                       more levels follow same pattern
```

---

## Project Physics Layers

| Layer | Name | Used by |
|-------|------|---------|
| 1 | Terrain | TileMap collision, walls |
| 2 | Player | CharacterBody2D player |
| 3 | Enemy | CharacterBody2D enemies |
| 4 | PlayerHitbox | Area2D that hurts enemies |
| 5 | EnemyHitbox | Area2D that hurts player |
| 6 | Projectile | Bullets, arrows, spells |
| 7 | Interactable | Doors, chests, NPCs |
| 8 | Item | Dropped pickups |

---

## Input Map (full game)

| Action | Key | Controller |
|--------|-----|-----------|
| `move_left/right/up/down` | WASD / Arrows | Left stick |
| `attack` | Left click / J | Button South |
| `attack_alt` | Right click / K | Left Trigger |
| `dodge` | Shift / L | Button East |
| `interact` | E / F | Button North |
| `inventory` | I / Tab | Select |
| `map` | M | D-Pad Right |
| `menu` | Escape | Start |
| `shoot` | Right click / K | Right Trigger |
| `ability_1` | Q | L Bumper |
| `ability_2` | R | R Bumper |
| `hotbar_1-6` | 1–6 | D-Pad variations |
| `sprint` | Shift (hold) | Left Stick click |
| `lock_target` | Middle click / T | Right Stick click |

---

## Autoloads

| Script | Autoload Name | Purpose |
|--------|--------------|---------|
| `global/game_manager.gd` | GameManager | Scene transitions, save/load, global events |
| `global/enums.gd` | Enum | All named constants |
| `global/data.gd` | Data | Stat tables, drop tables, dialogue DB |
| `global/audio_manager.gd` | AudioManager | Pooled SFX + music crossfade |
| `global/event_bus.gd` | EventBus | Decoupled signal hub (enemy died, quest updated) |

---

## Incremental verification (required)

**After every phase (or sub-step), the game must run and complete without errors.** Do not proceed to the next phase until:

1. **Run the project** (F5 or Play) and confirm the main scene loads.
2. **No runtime errors** in the Output/Debugger — fix any missing nodes, typos, or null refs before continuing.
3. **New behavior is testable** — e.g. after Phase 3 you can move the player; after Phase 5 you can attack and see damage.

If something breaks, fix it in the current phase before adding the next. Never leave the project in a broken state at the end of a step.

---

## Build Workflow — 16 Phases

Work through these phases in order. Each phase produces testable output.

### Phase 1 — Project Setup
→ See `references/godot-engine-guide.md` (if new to Godot)
→ See `references/step-by-step-guide.md` Phase 1

- Create project in Godot 4
- Set physics layer names (8 layers above)
- Set input map (full action list above)
- Set window size 1920×1080, texture filter = Nearest
- Create all autoload scripts (empty shells first)
- Set up folder structure

**Verify:** Project runs (F5). A minimal test scene or placeholder main scene loads with no errors.

### Phase 2 — Global Scripts
→ See `references/enums-data.md`

- `enums.gd` — all enums (EnemyType, ItemType, WeaponType, DamageType, QuestState…)
- `data.gd` — stat tables (enemy HP/speed/damage, item values, weapon damage ranges)
- `event_bus.gd` — shared signals (enemy_died, item_picked_up, quest_updated, player_died)

**Verify:** Project still runs. No script parse errors; autoloads load without error.

### Phase 3 — Player Scene + AnimationTree
→ See `references/step-by-step-guide.md` Phase 3

- CharacterBody2D + 8-directional movement
- Full AnimationTree (BlendTree → MoveStateMachine → BlendSpace2D for walk/idle)
- ToolOneShot for all attack animations
- Can dodge-roll (iframe window = 0.3s)
- Can sprint (speed multiplier while sprint held)

**Verify:** Main scene has Player. Run game: player moves with WASD, animations play, no errors.

### Phase 4 — Stats + Inventory (data layer)
→ See `references/enums-data.md`

- `PlayerStats` Resource (HP, MP, ATK, DEF, SPD, crit_chance, crit_mult)
- `InventorySystem` (array of ItemResource, max_slots=30)
- `EquipmentSlots` (weapon, shield, helmet, armor, boots, ring x2, accessory x2)
- Stats automatically recalculated when equipment changes

**Verify:** Game runs. Player has stats; no errors when opening inventory or changing equipment (if UI exists).

### Phase 5 — Combat: Melee
→ See `references/combat-enemies.md` Phase 5

- Weapon hitbox as Area2D child of player
- Hitbox only active during attack animation frames (method track)
- Combo system: 3-hit light, 1-hit heavy, 2-hit finisher
- Damage = ATK × weapon_multiplier + rand_range(±10%)
- Screen shake on heavy hits
- Floating damage numbers (red=normal, yellow=crit, white=miss)

**Verify:** Run game. Attack key triggers attack animation; hitting an enemy applies damage and shows numbers (once enemies exist); no errors.

### Phase 6 — Combat: Ranged + Projectiles
→ See `references/combat-enemies.md` Phase 6

- Generic `Projectile` scene (bullet, arrow, spell — same base, different data)
- Fires from player's weapon position toward mouse / right stick
- Gravity optional (arrows arc, bullets don't)
- Piercing, bouncing, and homing variants via flags
- On hit: impact VFX + SFX, apply damage, queue_free

**Verify:** Run game. Ranged attack spawns projectile; projectile moves and hits (or times out); no errors.

### Phase 7 — Enemy Base System
→ See `references/combat-enemies.md` Phase 7

- `EnemyBase` CharacterBody2D with NavigationAgent2D (pathfinding)
- State machine: Idle → Patrol → Alert → Chase → Attack → Hurt → Dead
- Shared signals via EventBus (enemy_died broadcasts drops + quest progress)
- Hit flash using same FlashSprite2D shader as farming game
- Drop loot on death (weighted random table in data.gd)

**Verify:** Run game. At least one enemy type in level: moves, chases player, takes damage, dies and drops; no errors.

### Phase 8 — Enemy Types
→ See `references/combat-enemies.md` Phase 8

Each type extends EnemyBase and overrides `_attack()`:
- **Grunt** — melee charge, simple AI
- **Archer** — keeps distance, fires projectiles at player
- **Mage** — casts AOE spells, teleports when cornered
- **Shield** — blocks frontal damage, must be flanked
- **Exploder** — rushes player and detonates (AOE)
- **Boss** — multi-phase, scripted attack patterns, health bar UI

**Verify:** Run game. Each new enemy type behaves as intended (melee, ranged, etc.); no errors.

### Phase 9 — Level Building: Outdoor
→ See `references/level-building.md` Phase 9

- Grass / dirt / water TileMapLayers with terrain autotiling
- Navigation bake (NavigationRegion2D) for enemy pathfinding
- Ambient 2D lights (PointLight2D + LightOccluder2D for shadows)
- Weather layer (rain particles — reuse farming game system)
- Outdoor camera: smooth follow with level boundaries (Camera2D limits)

**Verify:** Run game. Outdoor level loads; player and enemies move on terrain; camera stays in bounds; no errors.

### Phase 10 — Level Building: Indoor / Dungeon
→ See `references/level-building.md` Phase 10

- Room-based dungeon: each room is a Node2D child loaded/activated on entry
- Wall, floor, ceiling TileMapLayers with different z_indices
- Y-sort for entities (player always behind walls they walk behind)
- Roof tiles fade when player enters (same as farming game house)
- Door triggers: Area2D → animate door open → load next room/floor

**Verify:** Run game. Enter dungeon; rooms/doors work; Y-sort and roof fade correct; no errors.

### Phase 11 — Level Transitions + Game Manager
→ See `references/level-building.md` Phase 11

- `GameManager.change_level(scene_path, entry_point)` — loads next scene
- Circle wipe transition shader (reuse from farming game)
- Persistent data between levels (player HP, inventory) via GameManager singleton
- Floor counter for dungeon (Floor 1 / 2 / 3…) shown in HUD

**Verify:** Run game. Trigger level/room transition; scene changes with wipe; player state persists; no errors.

### Phase 12 — Boss Fight
→ See `references/combat-enemies.md` Phase 12

- Boss arena: sealed room (doors lock on entry, unlock on death)
- Boss state machine with phases: Phase1 (50% HP) → Phase2 (<50%) → Enrage (<10%)
- Phase 2: gains new attack pattern + speed increase
- Enrage: all attacks faster, new visual (red modulate, particle trail)
- Boss health bar: full-width UI at top of screen (fades between phases)
- Death sequence: slow-mo flash → explosion VFX → cinematic message

**Verify:** Run game. Enter boss room; doors lock; phases and health bar update; boss dies and doors unlock; no errors.

### Phase 13 — UI System
→ See `references/ui-audio-save.md` Phase 13

- HUD: HP bar, MP bar, stamina bar, ammo counter, active weapon, minimap
- Inventory grid (drag-and-drop items, right-click context menu)
- Equipment screen (character silhouette with slot overlays)
- Stats panel (base + bonus from equipment)
- Pause menu (resume / options / quit)
- Dialogue box (typewriter effect, branching choices, portrait)

**Verify:** Run game. HUD updates with HP/MP; inventory and equipment open/close; pause works; no errors.

### Phase 14 — Audio System
→ See `references/ui-audio-save.md` Phase 14

- Pooled SFX players (10 AudioStreamPlayer nodes, cycled FIFO)
- Music: crossfade between exploration, combat, boss tracks
- Footstep variety: different SFX per tile surface (grass, stone, water)
- Spatial SFX for distant enemies (AudioStreamPlayer2D)
- Master/SFX/Music bus volumes saved to user settings

**Verify:** Run game. SFX and music play; crossfade on scene change; no missing files or errors.

### Phase 15 — Save / Load System
→ See `references/ui-audio-save.md` Phase 15

- Save to `user://save_01.json` (up to 3 slots)
- Saved data: player stats, inventory, equipment, current level, flags (doors opened, bosses defeated, quests)
- Auto-save on room transition + manual save at save points
- New game / continue detection on main menu

**Verify:** Run game. Save and load; quit and continue; state matches (level, HP, inventory); no errors.

### Phase 16 — Polish + AAA Feel
→ See `references/step-by-step-guide.md` Phase 16

- Screen shake: `Camera2D.offset` tweened on impact (configurable magnitude + duration)
- Hit-stop: `Engine.time_scale = 0.1` for 0.05s on heavy hits → snap back to 1.0
- Combo counter: UI label fades in/out, resets on 2s idle
- Damage numbers: spawned label nodes, tween upward + fade
- Particle VFX: hit sparks, blood splatter, magic dust, explosion
- Procedural screenshake via sine noise
- Post-processing: subtle vignette + color correction shader per level theme

**Verify:** Run game. Shake, hit-stop, combo, damage numbers, and VFX trigger correctly; no errors.

---

## User-Only Editor Steps (cannot be scripted)

The following MUST be done manually in the Godot editor:

1. **AnimationTree setup** — Create BlendSpaces, StateMachines, OneShot nodes and wire them
2. **TileMap terrain painting** — Paint terrain connections and draw level layouts
3. **NavigationRegion2D bake** — Click "Bake NavigationPolygon" after placing tiles
4. **2D Light setup** — Place PointLight2D nodes and draw LightOccluder2D polygons
5. **Boss scripted positions** — Place Marker2D nodes for boss movement waypoints
6. **Room layout** — Design each room by hand using TileMap tools
7. **Collision shape tuning** — Fine-tune hitbox/hurtbox shapes for each enemy type
8. **Audio import settings** — Set Loop=true on music, Loop=false on SFX in the Import panel

For each of these steps, the reference files provide step-by-step editor instructions.
