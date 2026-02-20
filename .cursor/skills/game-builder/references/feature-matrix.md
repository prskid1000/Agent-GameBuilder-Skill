# Feature Matrix — All Skills Compared

Every feature available across all skills, with the exact source reference for each.

---

## Player

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| 2D CharacterBody2D | ✓ | ✓ | |
| 3D CharacterBody3D | | | ✓ |
| 8-directional movement | ✓ | ✓ | |
| Free 3D movement (fly) | | | ✓ |
| AnimationTree (BlendSpace2D) | ✓ | ✓ | |
| AnimationTree (OneShot tools) | ✓ | ✓ | |
| Camera2D (smooth follow) | ✓ | ✓ | |
| Camera3D (head-mounted) | | | ✓ |
| Sprint | ✓ | | ✓ |
| Dodge roll (i-frames) | ✓ | | |
| Mouse-aim (3D raycast) | | | ✓ |
| RayCast2D (facing direction) | | ✓ | |
| Skin/style cycling | | ✓ | |
| Block type cycling (scroll) | | | ✓ |
| Tool cycling (Q/E) | | ✓ | |

**Best player reference:**
- 2D with animation: `godot-adventure-rpg/references/step-by-step-guide.md` Phase 3
- 2D with tools: `godot-farming-game/references/step-by-step-guide.md` Step 3
- 3D first-person: `godot-open-world/references/scripts.md` → player.gd

---

## Combat

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| Melee attack (hitbox Area2D) | ✓ | (sword tool) | |
| 3-hit light combo | ✓ | | |
| Heavy attack | ✓ | | |
| Combo counter UI | ✓ | | |
| Ranged projectile (bullet/arrow/spell) | ✓ | (scarecrow shoots) | |
| Projectile piercing / bouncing / homing | ✓ | | |
| AOE damage | ✓ | | |
| Knockback / push | ✓ | ✓ (blob push) | |
| Damage numbers (floating text) | ✓ | | |
| Screen shake | ✓ | | |
| Hit-stop (time_scale) | ✓ | | |
| Flash hit feedback | (uses same) | ✓ | |
| Block / place blocks | | | ✓ |
| Break blocks (raycast hit) | | | ✓ |

**Best combat reference:** `godot-adventure-rpg/references/combat-enemies.md`

---

## Enemies / AI

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| NavigationAgent2D pathfinding | ✓ | | |
| State machine (Idle/Patrol/Chase/Attack/Dead) | ✓ | | |
| Basic seek AI (no navmesh) | | ✓ (blob) | |
| Grunt (melee) | ✓ | | |
| Archer (ranged) | ✓ | | |
| Mage (AOE, teleport) | ✓ | | |
| Shield (directional block) | ✓ | | |
| Exploder (suicide rush) | ✓ | | |
| Boss (multi-phase, health bar) | ✓ | | |
| Enemy spawning (timer-based) | ✓ | ✓ (blobs) | |
| Drop loot on death | ✓ | | |
| EventBus death signal | ✓ | | |

**Best enemy reference:** `godot-adventure-rpg/references/combat-enemies.md` Phases 7–12

---

## World / Level

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| TileMapLayer (terrain autotiling) | ✓ | ✓ | |
| Multiple TileMap layers (water/grass/soil) | | ✓ | |
| Custom tile data (farmable, coast) | | ✓ | |
| Room-based dungeon | ✓ | | |
| Outdoor level + camera limits | ✓ | ✓ | |
| House / indoor with roof fade | | ✓ | |
| Level transition (door → scene change) | ✓ | | |
| Chunked infinite world (3D) | | | ✓ |
| Procedural terrain (FastNoiseLite) | | | ✓ |
| Trees, foliage generation | | | ✓ |
| Y-sort (entities behind walls) | ✓ | ✓ | |
| NavigationRegion2D bake | ✓ | | |
| 2D ambient lights + shadows | ✓ | | |
| 3D DirectionalLight (sun) | | | ✓ |
| 3D OmniLight (torches) | | | ✓ |

**Best level reference:**
- 2D: `godot-adventure-rpg/references/level-building.md`
- 3D chunked: `godot-open-world/references/step-by-step-guide.md`

---

## Time / Environment

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| Day timer (countdown) | | ✓ | |
| Day/night (2D CanvasModulate + Gradient) | | ✓ | |
| Day/night (3D ProceduralSkyMaterial) | | | ✓ |
| Day restart (tween + level_reset) | | ✓ | |
| Rain particles (2D) | ✓ (weather) | ✓ | |
| Rain probability (forecast) | | ✓ | |
| Soil auto-water when raining | | ✓ | |
| Sunrise/sunset sky lerp (4 phases) | | | ✓ |
| Time persistence (DB) | | | ✓ |
| Time persistence (JSON save) | ✓ | | |

**Best time/cycle reference:**
- 2D: `godot-farming-game/references/step-by-step-guide.md` Step 11
- 3D: `godot-open-world/references/scripts.md` → sky.gd

---

## Farming / Resource Activities

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| Hoe tool (till soil) | | ✓ | |
| Watering can tool | | ✓ | |
| Seed planting | | ✓ | |
| Plant growth (stages, age, death) | | ✓ | |
| PlantResource (custom Resource class) | | ✓ | |
| Harvest on walk-over | | ✓ | |
| Plant info UI (growth/death bars) | | ✓ | |
| Axe tool (chop trees, get wood) | | ✓ | |
| Tree reset on day | | ✓ | |
| Fishing minigame (bar catch) | | ✓ | |
| Machines (sprinkler / scarecrow / fisher) | | ✓ | |
| Machine placement mode | | ✓ | |
| Machine delete | | ✓ | |
| Block placement | | | ✓ |
| Block break | | | ✓ |
| Block persistence (SQLite) | | | ✓ |

**Best farming reference:** `godot-farming-game/references/step-by-step-guide.md` Steps 6–10

---

## Inventory / Items / Equipment

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| Full grid inventory (30 slots, drag-drop) | ✓ | | |
| Equipment slots (weapon/armor/rings) | ✓ | | |
| Stats from equipment | ✓ | | |
| Item resource (value, icon, type) | ✓ | | |
| Item drops from enemies | ✓ | | |
| Item pickup (Area2D) | ✓ | | |
| Shop / purchase upgrades | | ✓ | |
| Tool bar (cycle, no grid) | | ✓ | |
| Block selector (scroll wheel) | | | ✓ |
| Skin/hat upgrades | | ✓ | |

**Best inventory reference:**
- Full grid: `godot-adventure-rpg/references/ui-audio-save.md` Phase 13
- Tool bar: `godot-farming-game/references/step-by-step-guide.md` Step 8

---

## UI / HUD

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| HP / MP / stamina bars | ✓ | | |
| Minimap | ✓ | | |
| Dialogue box (typewriter, branching) | ✓ | | |
| Inventory panel | ✓ | | |
| Equipment screen | ✓ | | |
| Pause menu | ✓ | | |
| Tool icon bar | | ✓ | |
| Seed icon bar | | ✓ | |
| Plant info container (scroll) | | ✓ | |
| Fishing progress bar | | ✓ | |
| Block name + sprite display | | | ✓ |
| Debug stats (FPS, draw calls, memory) | | | ✓ |
| Boss health bar (full-width) | ✓ | | |
| Floor counter (dungeon) | ✓ | | |
| Theme (custom fonts, StyleBoxTexture) | | ✓ | |

---

## Persistence / Save

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| Save to JSON (`user://save.json`) | ✓ | | |
| 3 save slots | ✓ | | |
| Save: HP, inventory, equipment, flags | ✓ | | |
| Auto-save on room transition | ✓ | | |
| Manual save at save points | ✓ | | |
| SQLite DB (`user://game.sqlite`) | | | ✓ |
| Save: block edits (player-placed only) | | | ✓ |
| Save: player position + rotation | | | ✓ |
| Save: time of day | | | ✓ |
| Thread-safe DB access (Mutex) | | | ✓ |

---

## Audio

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| Pooled SFX (10 players, FIFO) | ✓ | | |
| Music crossfade (exploration/combat/boss) | ✓ | | |
| Footstep variety (tile-based) | ✓ | | |
| Spatial SFX (AudioStreamPlayer2D) | ✓ | | |
| Volume buses saved to settings | ✓ | | |
| Basic SFX on interactions | | ✓ | |

**Best audio reference:** `godot-adventure-rpg/references/ui-audio-save.md` Phase 14

---

## VFX / Shaders

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| Flash shader (hit feedback) | ✓ (same) | ✓ | |
| Circle wipe transition shader | ✓ (same) | ✓ | |
| Hit sparks / blood particles | ✓ | | |
| Explosion VFX | ✓ | | |
| Rain particles | ✓ | ✓ | |
| Vignette + color correction | ✓ | | |
| Opaque block shader (Texture2DArray) | | | ✓ |
| Transparent block shader | | | ✓ |
| Cross-sprite shader (plants, torches) | | | ✓ |
| Spritesheet include (gdshaderinc) | | | ✓ |

---

## Performance / Architecture

| Feature | adventure-rpg | farming-game | open-world |
|---------|:---:|:---:|:---:|
| Autoloads (GameManager, Enum, Data, Audio, EventBus) | ✓ | | |
| Autoloads (Enum, Data) | | ✓ | |
| Autoload (GDCraftResources) | | | ✓ |
| EventBus (decoupled signals) | ✓ | | |
| WorkerThreadPool (async generation) | | | ✓ |
| Flag-based state machine | | | ✓ |
| Object pooling (enemy drops, particles) | ✓ | | |
| Godot-sqlite GDExtension | | | ✓ |
| Jolt Physics (3D) | | | ✓ |
| NavigationRegion2D (2D navmesh) | ✓ | | |
