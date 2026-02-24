# Decision Guide — Which Template for Which Game

Answer the questions below to find the right template(s) for your game.

---

## Question 1: Dimension

| Answer | Next |
|--------|------|
| **3D** | → Go to [3D Games](#3d-games) |
| **2D** | → Go to [2D Games](#2d-games) |
| **Not sure** | → Pick based on your reference game (Stardew = 2D, Minecraft = 3D, Zelda = 2D) |

---

## 3D Games

| What best describes your game? | Template |
|--------------------------------|----------|
| Infinite terrain, place/break blocks, Minecraft-like | **3D Voxel Open-World** |
| Exploration, building, survival in a voxel world | **3D Voxel Open-World** |
| Voxel world + combat / enemies / RPG | **3D Voxel Open-World** + **2D Adventure RPG** combat |
| 3D exploration but no voxels (e.g. 3D platformer) | Neither — extend **3D Voxel Open-World** player base |

**3D Voxel Open-World** gives you: chunked world, procedural terrain (FastNoiseLite), AsyncMesh, SQLite persistence, day/night sky, torch lighting, first-person player.

---

## 2D Games

### Primary activity:

| Primary activity | Template |
|-----------------|----------|
| Combat, fighting enemies, killing bosses | **2D Adventure RPG** |
| Farming, planting, harvesting crops | **2D Farming Game** |
| Fishing | **2D Farming Game** (has fishing minigame built-in) |
| Exploring dungeons, rooms, maps | **2D Adventure RPG** |
| Talking to NPCs, quests, story | **2D Adventure RPG** |
| Building / placing machines | **2D Farming Game** (machine placement system) |
| Day/night cycle, seasons | **2D Farming Game** |
| Collecting items, inventory management | **2D Adventure RPG** (full grid inventory) |
| Simple item cycling (tool bar) | **2D Farming Game** (simpler tool UI) |

---

## Genre → Template Map

| Genre | Primary template | Add-on template |
|-------|-----------------|-----------------|
| Action RPG (Zelda-like) | **2D RPG** | — |
| Dungeon crawler / roguelite | **2D RPG** | — |
| Metroidvania | **2D RPG** | — |
| Top-down shooter | **2D RPG** | — |
| Farming sim (Stardew-like) | **2D Farm** | — |
| Life sim / town builder | **2D Farm** | — |
| Farming + combat (Story of Seasons Trio of Towns-like) | **2D Farm** | **2D RPG** combat |
| Action adventure with homestead | **2D RPG** | **2D Farm** farming loop |
| Minecraft 3D | **3D Voxel** | — |
| 3D survival crafting | **3D Voxel** | **2D Farm** crafting/resource loop |
| 3D RPG voxel world | **3D Voxel** | **2D RPG** combat + enemies |
| Tower defense | **2D RPG** (enemy AI + spawning) | — |
| Visual novel / dialogue-heavy | **2D RPG** (dialogue system) | — |

---

## Key Feature Checklist

Check off what your game needs, then look at which column has the most checkmarks:

| Feature | 2D RPG | 2D Farm | 3D Voxel |
|---------|:---:|:---:|:---:|
| 2D top-down movement | ✓ | ✓ | |
| 3D first-person movement | | | ✓ |
| Melee combat | ✓ | (sword tool) | |
| Ranged combat / projectiles | ✓ | (scarecrow machine) | |
| Enemy AI (pathfinding) | ✓ | (blobs, basic) | |
| Boss fights | ✓ | | |
| Inventory grid (drag-drop) | ✓ | | |
| Tool bar (cycle left/right) | | ✓ | |
| Farming / planting | | ✓ | |
| Fishing minigame | | ✓ | |
| Machine placement | | ✓ | |
| Block placement / building | | | ✓ |
| Procedural terrain | | | ✓ |
| Infinite world / chunk loading | | | ✓ |
| Day/night (2D gradient) | | ✓ | |
| Day/night (3D sky) | | | ✓ |
| Rain / weather | | ✓ | |
| Save/load (JSON) | ✓ | | |
| Save/load (SQLite) | | | ✓ |
| Dialogue (branching, typewriter) | ✓ | | |
| Quest system | ✓ | | |
| Equipment slots + stat system | ✓ | | |
| Screen shake + hit-stop | ✓ | | |
| Flash hit feedback | | ✓ | |
| Circle wipe transition | | ✓ | |
| Multiple levels / level transitions | ✓ | | |
| Single persistent world | | ✓ | ✓ |
| Audio (pooled SFX, crossfade music) | ✓ | | |
| HUD (HP/MP bars, minimap) | ✓ | | |
| Simple HUD (tool icons, block name) | | ✓ | ✓ |
| Dynamic lighting (OmniLight3D) | | | ✓ |
| Ambient 2D lights | ✓ | | |
| Shaders (opaque/transparent/sprite) | | | ✓ |
| ComfyUI asset prompts | ✓ | ✓ | ✓ |

**Tiebreaker:** If you have equal checkmarks in 2D RPG and 2D Farm, pick **2D RPG** for combat-first games and **2D Farm** for resource/activity-first games.

---

## Examples of Popular Games → Template

| Game | Closest template |
|------|-----------------|
| The Legend of Zelda: Link's Awakening | **2D RPG** |
| Stardew Valley | **2D Farm** |
| Minecraft | **3D Voxel** |
| Hades | **2D RPG** |
| Terraria (2D) | **2D RPG** + **2D Farm** (building/crafting) |
| My Time at Portia | **2D Farm** + **2D RPG** (combat) |
| Vampire Survivors | **2D RPG** (enemy spawning + projectiles) |
| Animal Crossing | **2D Farm** |
| Rune Factory | **2D Farm** + **2D RPG** (dungeon combat) |
| Valheim (2D version) | **2D Farm** + **2D RPG** + **3D Voxel** (world size) |
