# Cross-Skill Patterns — Mixing Features from Multiple Skills

Ready-to-use combination recipes. Each pattern specifies:
- Which skill provides the **base architecture**
- Which skill provides the **add-on features**
- The exact steps/references to follow from each
- Key integration points (where the two skills connect)

---

## Pattern 1: Farming + Combat (Rune Factory / Story of Seasons style)

**Base:** `godot-farming-game`
**Add-on:** `godot-adventure-rpg` combat system

### What you get
- Full farming loop: planting, watering, harvesting, machines, fishing, day/night
- Enemy blobs evolve into real combat enemies with AI, health, and drops
- Sword tool becomes a real weapon with hitboxes and combo
- Dungeon entrance in the overworld (transition to adventure-rpg levels)

### Build order
1. **Follow `godot-farming-game` Steps 1–11 completely first.** Get a working farm.
2. **Upgrade blob enemies to adventure-rpg enemies:**
   - Replace `blob.gd` with `EnemyBase` from `godot-adventure-rpg/references/combat-enemies.md` Phase 7.
   - Keep blob spawn positions; route through `NavigationAgent2D` pathfinding.
3. **Upgrade sword tool to real melee combat:**
   - Add `HitboxArea2D` to player, activate only during sword animation frames (method track).
   - Add `_on_area_body_entered` to deal damage — from `combat-enemies.md` Phase 5.
4. **Add dungeon entrance:**
   - Place an Area2D door in the overworld level.
   - Use `GameManager.change_level()` from `godot-adventure-rpg/references/level-building.md` Phase 11.
   - Run a dungeon scene built from `level-building.md` Phase 10.
5. **Add loot/drops from enemies:**
   - Use `Data.gd` drop tables from `godot-adventure-rpg/references/enums-data.md`.
   - Drops go into farming's item system (expand `Enum.Item` with weapon/armor types).

### Key integration points
```
level.gd              ← farming base; add dungeon door signal
player.gd             ← add HitboxArea2D + combo state; extend Enum.State with COMBAT
Enum (autoload)       ← add Item types from RPG (weapons, armor) + farming items
Data (autoload)       ← add ENEMY_STATS, DROP_TABLES alongside PLANT_DATA
EventBus (new)        ← add enemy_died, dungeon_cleared signals (from adventure-rpg)
```

---

## Pattern 2: RPG Overworld + Life-Sim Town (Harvest Moon / Rune Factory overworld)

**Base:** `godot-adventure-rpg`
**Add-on:** `godot-farming-game` life-sim activities

### What you get
- Full adventure-rpg: multiple levels, dungeons, enemies, bosses, equipment, save/load
- Town hub with NPCs; inside the town: farming, fishing, day timer, shops
- Day/night affects both town life-sim AND enemy spawning in overworld

### Build order
1. **Follow `godot-adventure-rpg` Phases 1–11 completely first.** Get working RPG with levels.
2. **Create a "Town" level using farming-game architecture:**
   - TileMapLayers matching farming-game: GrassLayer, SoilLayer, WaterLayer.
   - Farming tools in player: add HOE, WATER, SEED to `Enum.Tool` (keep SWORD, BOW).
   - Reuse `plant.gd`, `plant_res.gd`, `tree.gd`, `fisher.gd` from farming skill directly.
3. **Add farming day timer to Town level:**
   - Add `DayTimer` + `daytime_color` (CanvasModulate + Gradient) from `farming-game/step-by-step-guide.md` Step 11.
   - `level_reset()` resets crops + restocks shops.
4. **Connect day to RPG overworld:**
   - When DayTimer expires, enemies in overworld levels become stronger (scale stats by day count).
   - Track `GameManager.current_day` (add to RPG save data).
5. **Add farming shops to town NPCs:**
   - NPC `interact()` opens farming shop UI (`Enum.Shop.MAIN`/`HAT`).
   - Crops sold give currency added to RPG gold system.

### Key integration points
```
GameManager           ← add current_day, gold; save with existing JSON save
Enum.Tool             ← merge farming tools (HOE/WATER/SEED) + RPG weapons (SWORD/BOW)
player.gd             ← switch to farming mode when in Town; combat mode elsewhere
Town level            ← farming architecture (TileMapLayers, DayTimer, Objects)
Overworld levels      ← adventure-rpg architecture (NavigationRegion2D, enemy spawns)
```

---

## Pattern 3: Voxel World + RPG Combat (Minecraft + combat enemies)

**Base:** `godot-open-world`
**Add-on:** `godot-adventure-rpg` combat system (ported to 3D)

### What you get
- Full voxel world: chunk loading, procedural terrain, block placement, SQLite persistence
- Hostile mobs spawn at night (use sky.gd `time_of_day` for night detection)
- First-person player can attack + has HP
- Loot drops that can be picked up and placed as blocks

### Build order
1. **Follow `godot-open-world` Steps 1–11 completely.** Get a working voxel world.
2. **Add player health:**
   - Add `health` var + `damage(amount)` method to `player.gd`.
   - Show HP bar in `hud.gd` (reuse `ProgressBar` node; model from adventure-rpg HUD).
3. **Add enemy mob scene (`mob.gd`):**
   - `CharacterBody3D` extending from adventure-rpg's `EnemyBase` concept, but in 3D.
   - Use `NavigationAgent3D` (3D equivalent of `NavigationAgent2D` — same API, see @.docs).
   - States: Idle → Chase (if player in range) → Attack → Dead.
   - Spawn on solid ground blocks at night (`sky.time_of_day > _sunset_end`).
4. **Add melee attack:**
   - Player `_input`: LMB = block break, RMB = block place, **Middle click / F = swing**.
   - `Area3D` hitbox in front of player; enabled for 0.2s on attack input.
5. **Mob drops:**
   - On death: `queue_free()` + spawn `ItemPickup3D` (small `MeshInstance3D` with `Area3D`).
   - Player walks into `Area3D` → picked up, added to inventory or placed as block.
6. **Night mob spawning:**
   - In `World._process()`: when `_sky.time_of_day > _sky._sunset_end` → spawn mobs near player edges.
   - Despawn at sunrise.

### Key integration points
```
sky.gd                ← add is_night() helper: return time_of_day > _sunset_end or time_of_day < _sunrise_end
world.gd              ← add mob spawn/despawn logic in _process
player.gd             ← add health, attack hitbox, damage(), death()
hud.gd                ← add HP bar; extend existing stats overlay
mob.gd                ← new CharacterBody3D with 3D navigation and attack AI
```

---

## Pattern 4: Voxel World + Survival Crafting (Minecraft survival)

**Base:** `godot-open-world`
**Add-on:** `godot-farming-game` resource/crafting loop

### What you get
- Voxel world with all block types
- Resources from breaking blocks (wood from LOG, stone from STONE)
- Crafting table interaction: combine resources → new block types
- Hunger/thirst meters from farming-game's item system

### Build order
1. **Follow `godot-open-world` Steps 1–11.** Get working voxel world.
2. **Add resource drops when breaking blocks:**
   - In `World._on_player_set_block(index, Block.Type.EMPTY)`:
     - Get the block type that was removed.
     - Spawn a `ResourcePickup3D` scene at world position.
3. **Add inventory (simple slot bar):**
   - Reuse `tool_ui.gd` concept from farming-game but for resource items.
   - `Enum.Item` for resource types (WOOD, STONE, SAND, etc.).
4. **Add crafting:**
   - Crafting recipes in `Data.gd` (reuse farming-game's `MACHINE_UPGRADE_COST` pattern):
     ```gdscript
     const CRAFT_RECIPES = {
         Block.Type.PLANKS: {Enum.Item.WOOD: 2},
         Block.Type.GLASS: {Enum.Item.SAND: 1},
     }
     ```
   - Player presses craft key near workbench block → open crafting UI.
5. **Hunger/thirst (optional):**
   - Add `hunger`, `thirst` floats to player.gd; decrease over time.
   - Food items (from farming-game APPLE, TOMATO etc.) restore them.
   - Starvation damages health.

### Key integration points
```
world.gd              ← emit resource_drop signal when block breaks
Data (new)            ← CRAFT_RECIPES dict (matches farming-game pattern)
Enum (new)            ← add Item types: WOOD, STONE, SAND, etc.
player.gd             ← add simple slot inventory + crafting interaction
hud.gd                ← add resource slot bar (model from farming tool_ui)
```

---

## Pattern 5: Roguelite Dungeon (farming day-reset + RPG combat)

**Base:** `godot-adventure-rpg`
**Concept:** Each dungeon run = one "day"; death or completion resets the floor

### What you get
- Full RPG combat and enemies
- Procedurally chosen room layouts per run (random from pool)
- Day-timer from farming-game drives floor reset
- Circle-wipe transition (from farming-game) used as floor-transition shader

### Build order
1. **Follow `godot-adventure-rpg` Phases 1–12.** Get working dungeon RPG.
2. **Add run timer:**
   - Reuse `DayTimer` (Timer node) from farming-game.
   - Timer expiry = run ends → show "Escape!" → wipe back to hub.
3. **Circle wipe for floor transitions:**
   - Import `circle_transition.gdshader` from `godot-farming-game/references/scripts.md`.
   - Use same tween pattern: 0→1 → do transition → 1→0.
4. **Procedural floor layout (optional):**
   - On floor entry: randomly pick 5–8 pre-built room scenes (from `level-building.md`).
   - Place them in a grid using `Vector2i` room indices.
   - Connect doors based on grid adjacency.

---

## Shared Components (Use From Any Game)

These components can be copy-pasted into any project regardless of which skill you're using:

### Flash shader (hit feedback) — from farming-game
```
Source: godot-farming-game/references/scripts.md → flash_sprite_2d.gd + flash.tres
Works for: any Sprite2D/Sprite3D hit effect in any game type
```

### Circle wipe transition — from farming-game
```
Source: godot-farming-game/references/scripts.md → circle_transition.gdshader
Works for: any scene/level/day transition in any game type
```

### Autoload singleton pattern — from adventure-rpg
```
Source: godot-adventure-rpg/references/enums-data.md
Works for: any game needing global state, event bus, or data tables
```

### Async WorkerThreadPool task — from open-world
```
Source: godot-open-world/references/scripts.md → chunk.gd (generate/mesh pattern)
Works for: any heavy computation in any game (dungeon generation, pathfinding bake, asset loading)
```

### AnimationTree (2D) — shared between adventure-rpg and farming-game
```
Source: godot-adventure-rpg/references/step-by-step-guide.md Phase 3
        godot-farming-game/references/step-by-step-guide.md Step 4
Works for: any 2D player with directional movement + action animations
```

### ComfyUI asset prompts — all skills
```
adventure-rpg/references/asset-prompts-comfyui.md  ← 2D sprites, tiles, VFX, portraits
farming-game/references/asset-prompts-comfyui.md   ← farming icons, plants, UI art
open-world/references/asset-prompts-comfyui.md     ← 3D block spritesheet, voxel art
Works for: any game; pick the closest style and modify the prompt
```
