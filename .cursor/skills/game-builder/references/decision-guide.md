# Decision Guide — Which Skill for Which Game

Answer the questions below to find the right skill(s) for your game.

---

## Question 1: Dimension

| Answer | Next |
|--------|------|
| **3D** | → Go to [3D Games](#3d-games) |
| **2D** | → Go to [2D Games](#2d-games) |
| **Not sure** | → Pick based on your reference game (Stardew = 2D, Minecraft = 3D, Zelda = 2D) |

---

## 3D Games

| What best describes your game? | Skill |
|--------------------------------|-------|
| Infinite terrain, place/break blocks, Minecraft-like | **godot-open-world** |
| Exploration, building, survival in a voxel world | **godot-open-world** |
| Voxel world + combat / enemies / RPG | **godot-open-world** + **godot-adventure-rpg** combat |
| 3D exploration but no voxels (e.g. 3D platformer) | Neither — extend **godot-open-world** player base |

**godot-open-world** gives you: chunked world, procedural terrain (FastNoiseLite), AsyncMesh, SQLite persistence, day/night sky, torch lighting, first-person player.

---

## 2D Games

### Primary activity:

| Primary activity | Skill |
|-----------------|-------|
| Combat, fighting enemies, killing bosses | **godot-adventure-rpg** |
| Farming, planting, harvesting crops | **godot-farming-game** |
| Fishing | **godot-farming-game** (has fishing minigame built-in) |
| Exploring dungeons, rooms, maps | **godot-adventure-rpg** |
| Talking to NPCs, quests, story | **godot-adventure-rpg** |
| Building / placing machines | **godot-farming-game** (machine placement system) |
| Day/night cycle, seasons | **godot-farming-game** |
| Collecting items, inventory management | **godot-adventure-rpg** (full grid inventory) |
| Simple item cycling (tool bar) | **godot-farming-game** (simpler tool UI) |

---

## Genre → Skill Map

| Genre | Primary skill | Add-on skill |
|-------|--------------|--------------|
| Action RPG (Zelda-like) | **adventure-rpg** | — |
| Dungeon crawler / roguelite | **adventure-rpg** | — |
| Metroidvania | **adventure-rpg** | — |
| Top-down shooter | **adventure-rpg** | — |
| Farming sim (Stardew-like) | **farming-game** | — |
| Life sim / town builder | **farming-game** | — |
| Farming + combat (Story of Seasons Trio of Towns-like) | **farming-game** | **adventure-rpg** combat |
| Action adventure with homestead | **adventure-rpg** | **farming-game** farming loop |
| Minecraft 3D | **open-world** | — |
| 3D survival crafting | **open-world** | **farming-game** crafting/resource loop |
| 3D RPG voxel world | **open-world** | **adventure-rpg** combat + enemies |
| Tower defense | **adventure-rpg** (enemy AI + spawning) | — |
| Visual novel / dialogue-heavy | **adventure-rpg** (dialogue system) | — |

---

## Key Feature Checklist

Check off what your game needs, then look at which column has the most checkmarks:

| Feature | adventure-rpg | farming-game | open-world |
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

**Tiebreaker:** If you have equal checkmarks in adventure-rpg and farming-game, pick **adventure-rpg** for combat-first games and **farming-game** for resource/activity-first games.

---

## Examples of Popular Games → Skill

| Game | Closest skill |
|------|--------------|
| The Legend of Zelda: Link's Awakening | **adventure-rpg** |
| Stardew Valley | **farming-game** |
| Minecraft | **open-world** |
| Hades | **adventure-rpg** |
| Terraria (2D) | **adventure-rpg** + **farming-game** (building/crafting) |
| My Time at Portia | **farming-game** + **adventure-rpg** (combat) |
| Vampire Survivors | **adventure-rpg** (enemy spawning + projectiles) |
| Animal Crossing | **farming-game** |
| Rune Factory | **farming-game** + **adventure-rpg** (dungeon combat) |
| Valheim (2D version) | **farming-game** + **adventure-rpg** + **open-world** (world size) |
