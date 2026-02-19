# Enums, Data Tables & Stats System

All enums live in `global/enums.gd` (autoloaded as `Enum`).
All data tables live in `global/data.gd` (autoloaded as `Data`).

---

## enums.gd — Full File

```gdscript
# global/enums.gd
# Autoloaded as "Enum". Never use raw strings for game state — always use these.

# ─── Player ───────────────────────────────────────────────────────────────────
enum PlayerState { IDLE, MOVE, ATTACK, ATTACK_ALT, DODGE, HURT, DEAD, INTERACT, CAST }
# Tracks what the player is currently doing.
# DODGE = iframe window (0.3s), HURT = knockback, CAST = ability channel

enum WeaponType { SWORD, DAGGER, BOW, STAFF, GUN, SPEAR, SHIELD, UNARMED }
# Physical weapon categories. Determines which attack animations play.

enum DamageType { PHYSICAL, FIRE, ICE, LIGHTNING, POISON, VOID, HOLY }
# Used for resistance checks. Enemy.resistances[DamageType.FIRE] = 0.5 = 50% resist

enum AbilitySlot { ABILITY_1, ABILITY_2 }
# Which ability slot was triggered (Q or R by default)

# ─── Enemies ──────────────────────────────────────────────────────────────────
enum EnemyType { GRUNT, ARCHER, MAGE, SHIELD_BEARER, EXPLODER, BOSS }
# Determines which enemy scene to spawn and which data row to look up.

enum EnemyState { IDLE, PATROL, ALERT, CHASE, ATTACK, HURT, DEAD, FLEE }
# AI state machine states. Transitions driven by distance to player + HP thresholds.

# ─── Items ────────────────────────────────────────────────────────────────────
enum ItemType { WEAPON, ARMOR, HELMET, BOOTS, RING, ACCESSORY, CONSUMABLE, KEY, MATERIAL }
# Determines which inventory grid slot / equip slot accepts this item.

enum ItemRarity { COMMON, UNCOMMON, RARE, EPIC, LEGENDARY }
# Visual color coding: gray / green / blue / purple / orange

enum EquipSlot { WEAPON, OFFHAND, HELMET, ARMOR, BOOTS, RING_L, RING_R, ACCESSORY_1, ACCESSORY_2 }
# Exact equipment slots on the character sheet.

# ─── Projectiles ──────────────────────────────────────────────────────────────
enum ProjectileType { BULLET, ARROW, FIREBALL, ICE_SHARD, LIGHTNING_BOLT, VOID_ORB, GRENADE }
# Controls sprite, speed, gravity, pierce, bounce, and AOE radius.

# ─── Level / World ────────────────────────────────────────────────────────────
enum LevelType { OUTDOOR, INDOOR_DUNGEON, INDOOR_BUILDING, BOSS_ARENA, HUB }
# Affects lighting setup, music selection, navigation bake settings.

enum RoomState { LOCKED, ACTIVE, CLEARED }
# LOCKED = sealed doors. ACTIVE = enemies alive. CLEARED = doors open + loot spawned.

enum SurfaceType { GRASS, STONE, WATER, SAND, WOOD, METAL }
# Custom tile data. Used by AudioManager to pick footstep SFX variant.

# ─── Quests / Progress ────────────────────────────────────────────────────────
enum QuestState { INACTIVE, ACTIVE, COMPLETE, FAILED }

enum BossPhase { NONE, PHASE_1, PHASE_2, ENRAGE }
# Boss transitions through these as HP drops. Each phase adds attacks.

# ─── UI ───────────────────────────────────────────────────────────────────────
enum MenuScreen { NONE, MAIN_MENU, PAUSE, INVENTORY, EQUIPMENT, MAP, DIALOGUE, GAME_OVER }

enum DialogueSpeaker { PLAYER, NPC_A, NPC_B, NARRATOR, ENEMY }
```

---

## data.gd — Full File

```gdscript
# global/data.gd
# Autoloaded as "Data". Centralizes all game balance numbers.
# Change values here without touching any gameplay scripts.

# ─── World ────────────────────────────────────────────────────────────────────
const TILE_SIZE = 16            # All TileMapLayers use 16×16 tiles
const ROOM_SIZE = Vector2i(20, 15)  # Standard room in tiles (320×240 px)

# ─── Player Stats ─────────────────────────────────────────────────────────────
const PLAYER_BASE_STATS = {
    "max_hp":       100,
    "max_mp":       50,
    "max_stamina":  100,
    "base_atk":     10,
    "base_def":     5,
    "base_spd":     80.0,       # pixels/second
    "sprint_mult":  1.6,        # speed multiplier while sprinting
    "dodge_speed":  200.0,      # pixels/second during dodge roll
    "dodge_duration": 0.3,      # seconds of iframe
    "stamina_regen": 20.0,      # per second when not acting
    "crit_chance":  0.05,       # 5% base crit chance
    "crit_mult":    2.0,        # crits deal 2× damage
}

# ─── Enemy Stats ──────────────────────────────────────────────────────────────
const ENEMY_DATA = {
    Enum.EnemyType.GRUNT: {
        "max_hp": 40,  "atk": 8,  "def": 2,  "speed": 55.0,
        "detect_range": 120.0,  "attack_range": 28.0,  "attack_cooldown": 1.2,
        "xp": 10,
        "resistances": {},
        "loot_table": [
            { "item": "gold_coin",   "weight": 60, "amount": [1, 3] },
            { "item": "health_herb", "weight": 30, "amount": [1, 1] },
            { "item": "grunt_fang",  "weight": 10, "amount": [1, 1] },
        ],
    },
    Enum.EnemyType.ARCHER: {
        "max_hp": 30,  "atk": 12, "def": 1,  "speed": 45.0,
        "detect_range": 200.0,  "attack_range": 160.0, "attack_cooldown": 2.0,
        "preferred_distance": 120.0,   # tries to stay this far from player
        "projectile": Enum.ProjectileType.ARROW,
        "xp": 15,
        "resistances": {},
        "loot_table": [
            { "item": "gold_coin",   "weight": 50, "amount": [1, 4] },
            { "item": "arrow_bundle","weight": 40, "amount": [2, 6] },
            { "item": "archer_eye",  "weight": 10, "amount": [1, 1] },
        ],
    },
    Enum.EnemyType.MAGE: {
        "max_hp": 50,  "atk": 18, "def": 0,  "speed": 40.0,
        "detect_range": 220.0,  "attack_range": 180.0, "attack_cooldown": 3.0,
        "projectile": Enum.ProjectileType.FIREBALL,
        "teleport_hp_threshold": 0.3,  # teleports when HP < 30%
        "aoe_radius": 48.0,
        "xp": 25,
        "resistances": { Enum.DamageType.FIRE: 0.75 },
        "loot_table": [
            { "item": "gold_coin",    "weight": 40, "amount": [2, 6] },
            { "item": "mana_crystal", "weight": 50, "amount": [1, 2] },
            { "item": "spellbook_pg", "weight": 10, "amount": [1, 1] },
        ],
    },
    Enum.EnemyType.EXPLODER: {
        "max_hp": 25,  "atk": 40, "def": 0,  "speed": 70.0,
        "detect_range": 160.0,  "attack_range": 24.0, "fuse_time": 1.5,
        "explosion_radius": 64.0,
        "xp": 20,
        "resistances": {},
        "loot_table": [
            { "item": "bomb_part",  "weight": 60, "amount": [1, 2] },
            { "item": "gold_coin",  "weight": 40, "amount": [0, 2] },
        ],
    },
    Enum.EnemyType.BOSS: {
        "max_hp": 800, "atk": 25, "def": 10, "speed": 60.0,
        "phase2_threshold": 0.5,   # enter phase 2 at 50% HP
        "enrage_threshold": 0.1,   # enrage at 10% HP
        "xp": 500,
        "resistances": { Enum.DamageType.POISON: 1.0 },
        "loot_table": [
            { "item": "boss_key",      "weight": 100, "amount": [1, 1] },
            { "item": "epic_weapon",   "weight": 50,  "amount": [1, 1] },
            { "item": "gold_coin",     "weight": 100, "amount": [20, 50] },
        ],
    },
}

# ─── Weapons ──────────────────────────────────────────────────────────────────
const WEAPON_DATA = {
    "iron_sword": {
        "type": Enum.WeaponType.SWORD,
        "damage": [12, 18],         # [min, max] before ATK modifier
        "damage_type": Enum.DamageType.PHYSICAL,
        "combo_hits": 3,            # 3-hit light combo
        "heavy_damage_mult": 2.5,   # heavy attack multiplier
        "attack_speed": 1.0,        # animation speed multiplier
        "range": 32.0,              # hitbox radius
        "knockback": 60.0,
        "texture": "res://graphics/icons/iron_sword.png",
    },
    "fire_staff": {
        "type": Enum.WeaponType.STAFF,
        "damage": [20, 30],
        "damage_type": Enum.DamageType.FIRE,
        "projectile": Enum.ProjectileType.FIREBALL,
        "projectile_speed": 180.0,
        "mp_cost": 8,
        "aoe_radius": 40.0,
        "texture": "res://graphics/icons/fire_staff.png",
    },
    "hunters_bow": {
        "type": Enum.WeaponType.BOW,
        "damage": [8, 14],
        "damage_type": Enum.DamageType.PHYSICAL,
        "projectile": Enum.ProjectileType.ARROW,
        "projectile_speed": 280.0,
        "charge_time": 0.8,         # hold attack to charge for bonus damage
        "charged_mult": 1.8,
        "texture": "res://graphics/icons/bow.png",
    },
}

# ─── Projectiles ──────────────────────────────────────────────────────────────
const PROJECTILE_DATA = {
    Enum.ProjectileType.BULLET: {
        "speed": 350.0, "gravity": 0.0, "pierce": false,
        "bounce": false, "homing": false, "aoe_radius": 0.0,
        "lifetime": 2.0, "texture": "res://graphics/projectiles/bullet.png",
    },
    Enum.ProjectileType.ARROW: {
        "speed": 280.0, "gravity": 80.0, "pierce": false,
        "bounce": false, "homing": false, "aoe_radius": 0.0,
        "lifetime": 3.0, "texture": "res://graphics/projectiles/arrow.png",
    },
    Enum.ProjectileType.FIREBALL: {
        "speed": 180.0, "gravity": 0.0, "pierce": false,
        "bounce": false, "homing": false, "aoe_radius": 48.0,
        "lifetime": 4.0, "texture": "res://graphics/projectiles/fireball.png",
    },
    Enum.ProjectileType.ICE_SHARD: {
        "speed": 220.0, "gravity": 0.0, "pierce": true,
        "bounce": false, "homing": false, "aoe_radius": 0.0,
        "lifetime": 2.5, "texture": "res://graphics/projectiles/ice_shard.png",
    },
    Enum.ProjectileType.VOID_ORB: {
        "speed": 120.0, "gravity": 0.0, "pierce": false,
        "bounce": true,  "homing": true, "aoe_radius": 0.0,
        "lifetime": 5.0, "texture": "res://graphics/projectiles/void_orb.png",
    },
}

# ─── Items ────────────────────────────────────────────────────────────────────
const ITEM_DATA = {
    "health_herb": {
        "type": Enum.ItemType.CONSUMABLE,
        "rarity": Enum.ItemRarity.COMMON,
        "effect": "heal", "amount": 25,
        "texture": "res://graphics/icons/herb.png",
        "sell_value": 5,
    },
    "mana_crystal": {
        "type": Enum.ItemType.CONSUMABLE,
        "rarity": Enum.ItemRarity.UNCOMMON,
        "effect": "restore_mp", "amount": 20,
        "texture": "res://graphics/icons/crystal.png",
        "sell_value": 10,
    },
    "gold_coin": {
        "type": Enum.ItemType.MATERIAL,
        "rarity": Enum.ItemRarity.COMMON,
        "texture": "res://graphics/icons/coin.png",
        "sell_value": 1,
    },
}

# ─── Levels ───────────────────────────────────────────────────────────────────
const LEVEL_DATA = {
    "level_01_outdoor": {
        "scene":   "res://scenes/levels/level_01.tscn",
        "type":    Enum.LevelType.OUTDOOR,
        "music":   "res://audio/music_outdoor.ogg",
        "ambient": "res://audio/ambient_wind.ogg",
        "enemy_spawn_table": [
            { "type": Enum.EnemyType.GRUNT,  "weight": 60 },
            { "type": Enum.EnemyType.ARCHER, "weight": 40 },
        ],
    },
    "dungeon_01_floor_1": {
        "scene":   "res://scenes/levels/dungeon_01_f1.tscn",
        "type":    Enum.LevelType.INDOOR_DUNGEON,
        "music":   "res://audio/music_dungeon.ogg",
        "ambient": "res://audio/ambient_dungeon.ogg",
        "floor":   1,
        "enemy_spawn_table": [
            { "type": Enum.EnemyType.GRUNT,    "weight": 40 },
            { "type": Enum.EnemyType.EXPLODER, "weight": 35 },
            { "type": Enum.EnemyType.MAGE,     "weight": 25 },
        ],
    },
    "boss_arena_01": {
        "scene":   "res://scenes/levels/boss_01.tscn",
        "type":    Enum.LevelType.BOSS_ARENA,
        "music":   "res://audio/music_boss.ogg",
        "ambient": "",
        "boss":    Enum.EnemyType.BOSS,
    },
}

# ─── Abilities ────────────────────────────────────────────────────────────────
const ABILITY_DATA = {
    "dash_strike": {
        "damage_mult": 1.5, "range": 80.0, "mp_cost": 10,
        "cooldown": 4.0,    "animation": "dash_strike",
        "damage_type": Enum.DamageType.PHYSICAL,
    },
    "fireball_blast": {
        "damage": [35, 55], "aoe_radius": 64.0, "mp_cost": 20,
        "cooldown": 6.0,    "animation": "cast_fire",
        "damage_type": Enum.DamageType.FIRE,
        "projectile": Enum.ProjectileType.FIREBALL,
    },
}

# ─── XP / Leveling ────────────────────────────────────────────────────────────
const XP_PER_LEVEL = [
    0, 100, 250, 450, 700, 1000, 1400, 1900, 2500, 3200
]   # XP thresholds for levels 1-10
# Level up: +10 max_hp, +5 max_mp, +2 base_atk, +1 base_def
const LEVEL_UP_BONUSES = { "max_hp": 10, "max_mp": 5, "base_atk": 2, "base_def": 1 }
```

---

## PlayerStats Resource

```gdscript
# resources/player_stats.gd
extends Resource
class_name PlayerStats

# Base stats (from class + level)
@export var max_hp      : int   = 100
@export var max_mp      : int   = 50
@export var max_stamina : int   = 100
@export var base_atk    : int   = 10
@export var base_def    : int   = 5
@export var base_spd    : float = 80.0
@export var crit_chance : float = 0.05
@export var crit_mult   : float = 2.0
@export var level       : int   = 1
@export var xp          : int   = 0

# Current values (runtime, not saved as properties)
var hp      : int
var mp      : int
var stamina : float

# Bonus stats from equipment (recalculated on equip change)
var bonus_atk : int   = 0
var bonus_def : int   = 0
var bonus_spd : float = 0.0

func total_atk() -> int:   return base_atk + bonus_atk
func total_def() -> int:   return base_def + bonus_def
func total_spd() -> float: return base_spd + bonus_spd

func calculate_damage(weapon_data: Dictionary) -> int:
    var raw   = randi_range(weapon_data["damage"][0], weapon_data["damage"][1])
    var total = int(raw * (1.0 + total_atk() / 100.0))
    if randf() < crit_chance:
        total = int(total * crit_mult)
        EventBus.crit_hit.emit()   # triggers yellow damage number
    return total

func take_damage(amount: int, type: Enum.DamageType) -> int:
    var reduced = max(1, amount - total_def())   # minimum 1 damage always
    hp = max(0, hp - reduced)
    if hp == 0: EventBus.player_died.emit()
    return reduced   # return actual damage dealt (for damage number display)

func add_xp(amount: int) -> void:
    xp += amount
    var needed = Data.XP_PER_LEVEL[min(level, Data.XP_PER_LEVEL.size() - 1)]
    if xp >= needed:
        xp -= needed
        level_up()

func level_up() -> void:
    level += 1
    for stat in Data.LEVEL_UP_BONUSES:
        set(stat, get(stat) + Data.LEVEL_UP_BONUSES[stat])
    hp = max_hp   # full heal on level up
    EventBus.player_leveled_up.emit(level)
```

---

## event_bus.gd — Shared Signals

```gdscript
# global/event_bus.gd
# Autoloaded as "EventBus". Scripts emit here instead of needing direct references.
# This decouples systems — the UI doesn't need to know the Player node path.

extends Node

# ── Player ────────────────────────────────────────────────────────────────────
signal player_died
signal player_leveled_up(new_level: int)
signal player_hp_changed(new_hp: int, max_hp: int)
signal player_mp_changed(new_mp: int, max_mp: int)
signal player_stamina_changed(new_stamina: float, max_stamina: float)

# ── Combat ────────────────────────────────────────────────────────────────────
signal damage_dealt(amount: int, position: Vector2, is_crit: bool)
# HUD listens → spawns floating damage number label at position

signal crit_hit
signal hit_stop_requested(duration: float)
# GameManager/Camera listens → pauses Engine.time_scale

signal screen_shake_requested(magnitude: float, duration: float)

# ── Enemy ─────────────────────────────────────────────────────────────────────
signal enemy_died(enemy_type: Enum.EnemyType, position: Vector2, xp: int)
# HUD listens → +XP popup. QuestManager listens → quest counter update.

signal boss_phase_changed(new_phase: Enum.BossPhase)
signal boss_died

# ── Level ─────────────────────────────────────────────────────────────────────
signal room_cleared(room_id: String)
signal level_transition_requested(target_level: String, entry_point: String)
signal all_rooms_cleared

# ── Items / Inventory ─────────────────────────────────────────────────────────
signal item_picked_up(item_id: String, amount: int)
signal inventory_changed

# ── UI ────────────────────────────────────────────────────────────────────────
signal dialogue_started(speaker: Enum.DialogueSpeaker, lines: Array)
signal dialogue_ended
signal menu_opened(screen: Enum.MenuScreen)
signal menu_closed
```
