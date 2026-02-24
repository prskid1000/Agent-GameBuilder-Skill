# UI, Inventory, Dialogue, Audio, Save System

---

## HUD (Heads-Up Display)

### Scene structure
```
HUD (CanvasLayer)
  ├── HPBar (TextureProgressBar)         ← red fill, left side
  ├── MPBar (TextureProgressBar)         ← blue fill
  ├── StaminaBar (TextureProgressBar)    ← yellow fill
  ├── XPBar (TextureProgressBar)         ← thin bar at bottom
  ├── LevelLabel (Label)                 ← "Lv. 5"
  ├── WeaponIcon (TextureRect)           ← current weapon sprite
  ├── AbilityIcons (HBoxContainer)
  │     ├── Ability1 (TextureRect + CooldownOverlay)
  │     └── Ability2 (TextureRect + CooldownOverlay)
  ├── FloorLabel (Label)                 ← "Floor 2" (dungeon only)
  ├── BossHealthBar (VBoxContainer)      ← hidden until boss fight
  │     ├── BossNameLabel
  │     └── BossHPBar (TextureProgressBar)
  ├── DamageNumbers (Control)            ← floating number labels parented here
  ├── ComboLabel (Label)                 ← "7 HIT COMBO!"
  ├── NotificationBar (Control)          ← item pickup popups, level-up text
  └── MiniMap (SubViewportContainer)     ← small map top-right corner
```

### hud.gd
```gdscript
# scenes/ui/hud.gd
extends CanvasLayer

@onready var hp_bar        = $HPBar
@onready var mp_bar        = $MPBar
@onready var stamina_bar   = $StaminaBar
@onready var xp_bar        = $XPBar
@onready var level_label   = $LevelLabel
@onready var weapon_icon   = $WeaponIcon
@onready var boss_bar_root = $BossHealthBar
@onready var boss_hp       = $BossHealthBar/BossHPBar
@onready var boss_name     = $BossHealthBar/BossNameLabel
@onready var combo_label   = $ComboLabel
@onready var dmg_numbers   = $DamageNumbers
@onready var floor_label   = $FloorLabel

var combo_count : int   = 0
var combo_timer : float = 0.0
const COMBO_RESET = 2.0

func _ready() -> void:
    # Wire EventBus signals
    EventBus.player_hp_changed.connect(_on_hp)
    EventBus.player_mp_changed.connect(_on_mp)
    EventBus.player_stamina_changed.connect(_on_stamina)
    EventBus.player_leveled_up.connect(_on_level_up)
    EventBus.damage_dealt.connect(_spawn_damage_number)
    EventBus.boss_phase_changed.connect(_on_boss_phase)
    EventBus.boss_died.connect(func(): boss_bar_root.visible = false)
    EventBus.enemy_died.connect(func(_t, _p, xp): _add_xp_visual(xp))
    EventBus.item_picked_up.connect(_show_pickup_notification)
    boss_bar_root.visible = false
    combo_label.visible   = false

func _process(delta: float) -> void:
    if combo_count > 0:
        combo_timer -= delta
        if combo_timer <= 0:
            combo_count = 0
            combo_label.visible = false

func _on_hp(current: int, maximum: int) -> void:
    hp_bar.max_value = maximum
    hp_bar.value     = current
    _flash_bar(hp_bar, Color.RED)

func _on_mp(current: int, maximum: int) -> void:
    mp_bar.max_value = maximum
    mp_bar.value     = current

func _on_stamina(current: float, maximum: float) -> void:
    stamina_bar.max_value = maximum
    stamina_bar.value     = current

func _on_level_up(level: int) -> void:
    level_label.text = "Lv. %d" % level
    _show_notification("LEVEL UP!", Color.YELLOW)

func _on_boss_phase(phase: Enum.BossPhase) -> void:
    boss_bar_root.visible = true
    boss_name.text        = "Boss"   # set per boss scene
    match phase:
        Enum.BossPhase.PHASE_2: boss_hp.modulate = Color(1.0, 0.6, 0.2)
        Enum.BossPhase.ENRAGE:  boss_hp.modulate = Color(1.0, 0.1, 0.1)

func _add_xp_visual(xp: int) -> void:
    # Animate XP bar filling
    var tween = create_tween()
    tween.tween_property(xp_bar, "value", xp_bar.value + xp, 0.5)

func _spawn_damage_number(amount: int, pos: Vector2, is_crit: bool) -> void:
    combo_count += 1
    combo_timer  = COMBO_RESET
    _update_combo()
    var label = Label.new()
    dmg_numbers.add_child(label)
    label.text     = str(amount) + ("!" if is_crit else "")
    label.position = pos - global_position   # convert to CanvasLayer local
    label.add_theme_color_override("font_color", Color.YELLOW if is_crit else Color.WHITE)
    if is_crit:
        label.add_theme_font_size_override("font_size", 22)
    var tween = create_tween()
    tween.tween_property(label, "position:y", label.position.y - 32, 0.7)
    tween.parallel().tween_property(label, "modulate:a", 0.0, 0.7)
    tween.tween_callback(label.queue_free)

func _update_combo() -> void:
    if combo_count < 3:
        combo_label.visible = false
        return
    combo_label.visible = true
    combo_label.text    = "%d HIT COMBO!" % combo_count
    var tween = create_tween()
    tween.tween_property(combo_label, "scale", Vector2(1.3, 1.3), 0.0)
    tween.tween_property(combo_label, "scale", Vector2.ONE, 0.15)

func _show_pickup_notification(item_id: String, amount: int) -> void:
    _show_notification("+%d  %s" % [amount, item_id], Color.WHITE)

func _show_notification(text: String, color: Color) -> void:
    var label = Label.new()
    $NotificationBar.add_child(label)
    label.text = text
    label.add_theme_color_override("font_color", color)
    var tween = create_tween()
    tween.tween_property(label, "position:y", label.position.y - 24, 1.5)
    tween.parallel().tween_property(label, "modulate:a", 0.0, 1.5)
    tween.tween_callback(label.queue_free)

func _flash_bar(bar: TextureProgressBar, color: Color) -> void:
    var tween = create_tween()
    tween.tween_property(bar, "modulate", color * 1.5, 0.05)
    tween.tween_property(bar, "modulate", Color.WHITE, 0.15)
```

---

## Inventory System

```gdscript
# resources/inventory_system.gd
class_name InventorySystem

const MAX_SLOTS = 30

var slots : Array = []   # Array of { item_id: String, amount: int } or null

func _init() -> void:
    slots.resize(MAX_SLOTS)
    slots.fill(null)

func add(item_id: String, amount: int) -> bool:
    # Try stack onto existing slot first
    for i in MAX_SLOTS:
        if slots[i] and slots[i]["item_id"] == item_id:
            slots[i]["amount"] += amount
            EventBus.inventory_changed.emit()
            return true
    # Find empty slot
    for i in MAX_SLOTS:
        if slots[i] == null:
            slots[i] = { "item_id": item_id, "amount": amount }
            EventBus.inventory_changed.emit()
            return true
    return false   # inventory full

func remove(item_id: String, amount: int) -> bool:
    for i in MAX_SLOTS:
        if slots[i] and slots[i]["item_id"] == item_id:
            slots[i]["amount"] -= amount
            if slots[i]["amount"] <= 0:
                slots[i] = null
            EventBus.inventory_changed.emit()
            return true
    return false

func has(item_id: String, amount: int = 1) -> bool:
    for slot in slots:
        if slot and slot["item_id"] == item_id and slot["amount"] >= amount:
            return true
    return false

func use_consumable(item_id: String, player: Node) -> void:
    if not has(item_id): return
    var item = Data.ITEM_DATA[item_id]
    match item["effect"]:
        "heal":       player.stats.hp = min(player.stats.max_hp, player.stats.hp + item["amount"])
        "restore_mp": player.stats.mp = min(player.stats.max_mp, player.stats.mp + item["amount"])
    remove(item_id, 1)
    EventBus.player_hp_changed.emit(player.stats.hp, player.stats.max_hp)
    EventBus.player_mp_changed.emit(player.stats.mp, player.stats.max_mp)

func serialize() -> Array:
    return slots.map(func(s): return s)   # returns a copy

func deserialize(data: Array) -> void:
    slots = data
    EventBus.inventory_changed.emit()
```

### Inventory UI
```gdscript
# scenes/ui/inventory.gd
extends Control

@onready var grid = $MarginContainer/ScrollContainer/GridContainer
var slot_scene    = preload("res://scenes/ui/inventory_slot.tscn")

func _ready() -> void:
    EventBus.menu_opened.connect(func(screen):
        visible = screen == Enum.MenuScreen.INVENTORY
        if visible: _refresh()
    )
    EventBus.inventory_changed.connect(_refresh)

func _refresh() -> void:
    for child in grid.get_children(): child.queue_free()
    var inv = GameManager.player_ref.inventory
    for i in inv.MAX_SLOTS:
        var slot = slot_scene.instantiate()
        grid.add_child(slot)
        slot.setup(i, inv.slots[i])
        slot.slot_clicked.connect(_on_slot_clicked.bind(i))

func _on_slot_clicked(slot_index: int) -> void:
    var slot = GameManager.player_ref.inventory.slots[slot_index]
    if slot == null: return
    var item_data = Data.ITEM_DATA[slot["item_id"]]
    match item_data["type"]:
        Enum.ItemType.CONSUMABLE:
            GameManager.player_ref.inventory.use_consumable(slot["item_id"], GameManager.player_ref)
        Enum.ItemType.WEAPON, Enum.ItemType.ARMOR:
            _equip_item(slot["item_id"])
```

---

## Dialogue System

```gdscript
# scenes/ui/dialogue.gd
extends CanvasLayer

@onready var box         = $DialogueBox
@onready var speaker_lbl = $DialogueBox/SpeakerLabel
@onready var text_lbl    = $DialogueBox/TextLabel
@onready var portrait    = $DialogueBox/Portrait
@onready var choices     = $DialogueBox/ChoicesContainer

var current_lines   : Array  = []
var current_index   : int    = 0
var is_typing       : bool   = false
var full_text       : String = ""

func _ready() -> void:
    box.visible = false
    EventBus.dialogue_started.connect(start)

func start(speaker: Enum.DialogueSpeaker, lines: Array) -> void:
    current_lines = lines
    current_index = 0
    box.visible   = true
    get_tree().paused = true   # pause game during dialogue
    _show_line()

func _show_line() -> void:
    if current_index >= current_lines.size():
        _end()
        return
    var line = current_lines[current_index]
    speaker_lbl.text = line.get("speaker", "???")
    full_text        = line.get("text", "")
    # Typewriter effect
    text_lbl.text    = ""
    is_typing        = true
    var tween        = create_tween()
    tween.tween_method(func(t: float):
        text_lbl.text = full_text.substr(0, int(t * full_text.length()))
    , 0.0, 1.0, full_text.length() * 0.04)
    tween.tween_callback(func(): is_typing = false)
    # Show choices if this is a branching line
    if line.has("choices"):
        await tween.finished
        _show_choices(line["choices"])

func _show_choices(choices_data: Array) -> void:
    for child in choices.get_children(): child.queue_free()
    for choice in choices_data:
        var btn = Button.new()
        btn.text = choice["text"]
        choices.add_child(btn)
        btn.pressed.connect(func():
            if choice.has("next"):
                current_lines = choice["next"]
                current_index = 0
                _show_line()
            else:
                _end()
        )

func _input(event: InputEvent) -> void:
    if not box.visible: return
    if event.is_action_just_pressed("interact"):
        if is_typing:
            # Skip typewriter — show full text immediately
            text_lbl.text = full_text
            is_typing     = false
        else:
            current_index += 1
            _show_line()

func _end() -> void:
    box.visible       = false
    get_tree().paused = false
    EventBus.dialogue_ended.emit()
```

---

## Audio Manager

```gdscript
# global/audio_manager.gd
extends Node

const SFX_POOL_SIZE = 12

var sfx_pool         : Array[AudioStreamPlayer] = []
var sfx_pool_index   : int                      = 0
var music_player_a   : AudioStreamPlayer
var music_player_b   : AudioStreamPlayer
var active_music     : AudioStreamPlayer

# Surface → footstep SFX mapping
const FOOTSTEP_SFX = {
    Enum.SurfaceType.GRASS:  "res://audio/sfx/step_grass.wav",
    Enum.SurfaceType.STONE:  "res://audio/sfx/step_stone.wav",
    Enum.SurfaceType.WOOD:   "res://audio/sfx/step_wood.wav",
    Enum.SurfaceType.WATER:  "res://audio/sfx/step_water.wav",
    Enum.SurfaceType.SAND:   "res://audio/sfx/step_sand.wav",
    Enum.SurfaceType.METAL:  "res://audio/sfx/step_metal.wav",
}

func _ready() -> void:
    # Build SFX pool
    for i in SFX_POOL_SIZE:
        var p = AudioStreamPlayer.new()
        add_child(p)
        p.bus = "SFX"
        sfx_pool.append(p)
    # Build music crossfade players
    music_player_a        = AudioStreamPlayer.new()
    music_player_b        = AudioStreamPlayer.new()
    music_player_a.bus    = "Music"
    music_player_b.bus    = "Music"
    add_child(music_player_a)
    add_child(music_player_b)
    active_music          = music_player_a

func play_sfx(path: String, pitch_variation: float = 0.1) -> void:
    var player   = sfx_pool[sfx_pool_index]
    sfx_pool_index = (sfx_pool_index + 1) % SFX_POOL_SIZE
    player.stream          = load(path)
    player.pitch_scale     = 1.0 + randf_range(-pitch_variation, pitch_variation)
    player.play()

func play_footstep(surface: Enum.SurfaceType) -> void:
    if FOOTSTEP_SFX.has(surface):
        play_sfx(FOOTSTEP_SFX[surface], 0.15)

func play_music(path: String, loop: bool = true) -> void:
    if active_music.stream and active_music.stream.resource_path == path: return
    active_music.stream       = load(path)
    active_music.stream.loop  = loop
    active_music.play()

func crossfade_music(path: String, fade_time: float = 1.5) -> void:
    var from_player = active_music
    var to_player   = music_player_b if active_music == music_player_a else music_player_a
    to_player.stream       = load(path)
    to_player.volume_db    = -80
    to_player.play()
    active_music           = to_player
    var tween              = create_tween()
    tween.tween_property(from_player, "volume_db", -80, fade_time)
    tween.parallel().tween_property(to_player,   "volume_db",   0, fade_time)
    tween.tween_callback(from_player.stop)

func set_sfx_volume(db: float)   -> void: AudioServer.set_bus_volume_db(AudioServer.get_bus_index("SFX"),   db)
func set_music_volume(db: float) -> void: AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Music"), db)
```

---

## Save / Load System

```gdscript
# global/game_manager.gd  — save section (extends what was shown earlier)

# ── Flags (boolean game state: opened chests, defeated bosses, etc.) ─────────
var flags : Dictionary = {}

func set_flag(flag_id: String, value: bool) -> void:
    flags[flag_id] = value

func get_flag(flag_id: String) -> bool:
    return flags.get(flag_id, false)

# ── Full save ─────────────────────────────────────────────────────────────────
func save_game(slot: int = 1) -> void:
    if player_ref == null: return
    var data = {
        "version":    1,
        "level":      current_level_id,
        "entry":      requested_entry_point,
        "stats": {
            "hp":       player_ref.stats.hp,
            "mp":       player_ref.stats.mp,
            "max_hp":   player_ref.stats.max_hp,
            "max_mp":   player_ref.stats.max_mp,
            "base_atk": player_ref.stats.base_atk,
            "base_def": player_ref.stats.base_def,
            "level":    player_ref.stats.level,
            "xp":       player_ref.stats.xp,
        },
        "inventory": player_ref.inventory.serialize(),
        "flags":     flags,
        "playtime":  _get_playtime(),
    }
    var path = "user://save_%d.json" % slot
    var file = FileAccess.open(path, FileAccess.WRITE)
    file.store_string(JSON.stringify(data, "\t"))
    file.close()

func load_game(slot: int = 1) -> void:
    var path = "user://save_%d.json" % slot
    if not FileAccess.file_exists(path): return
    var file = FileAccess.open(path, FileAccess.READ)
    var text = file.get_as_text()
    file.close()
    var data = JSON.parse_string(text)
    if data == null: return
    # Restore flags first (before level loads, so doors/chests restore correctly)
    flags = data.get("flags", {})
    requested_entry_point = data.get("entry", "default")
    # Restore stats (player spawns with these)
    _pending_stats = data["stats"]
    _pending_inventory = data["inventory"]
    # Load the level (player spawns → _ready() calls restore_pending_data)
    change_level(data["level"])

func restore_pending_data() -> void:
    # Called by player._ready() after scene loads
    if _pending_stats.is_empty(): return
    for key in _pending_stats:
        player_ref.stats.set(key, _pending_stats[key])
    player_ref.inventory.deserialize(_pending_inventory)
    _pending_stats     = {}
    _pending_inventory = []

var _pending_stats     : Dictionary = {}
var _pending_inventory : Array      = []

func get_save_info(slot: int) -> Dictionary:
    var path = "user://save_%d.json" % slot
    if not FileAccess.file_exists(path): return {}
    var file = FileAccess.open(path, FileAccess.READ)
    var data = JSON.parse_string(file.get_as_text())
    file.close()
    if data == null: return {}
    return {
        "exists":   true,
        "level":    data.get("level", ""),
        "playtime": data.get("playtime", 0),
        "char_lvl": data.get("stats", {}).get("level", 1),
    }

var _playtime_start : int = 0
func _get_playtime() -> int:
    return Time.get_ticks_msec() - _playtime_start
```

---

## Pause Menu

```gdscript
# scenes/ui/pause_menu.gd
extends CanvasLayer

@onready var resume_btn  = $Panel/VBox/ResumeButton
@onready var save_btn    = $Panel/VBox/SaveButton
@onready var options_btn = $Panel/VBox/OptionsButton
@onready var quit_btn    = $Panel/VBox/QuitButton
@onready var sfx_slider  = $Panel/Options/SFXSlider
@onready var music_slider= $Panel/Options/MusicSlider

func _ready() -> void:
    visible         = false
    process_mode    = Node.PROCESS_MODE_ALWAYS   # runs even when tree is paused
    resume_btn.pressed.connect(_resume)
    save_btn.pressed.connect(func(): GameManager.save_game())
    quit_btn.pressed.connect(func(): get_tree().quit())
    sfx_slider.value_changed.connect(AudioManager.set_sfx_volume)
    music_slider.value_changed.connect(AudioManager.set_music_volume)

func _input(event: InputEvent) -> void:
    if event.is_action_just_pressed("menu"):
        if visible: _resume()
        else:       _open()

func _open() -> void:
    visible             = true
    get_tree().paused   = true
    EventBus.menu_opened.emit(Enum.MenuScreen.PAUSE)

func _resume() -> void:
    visible             = false
    get_tree().paused   = false
    EventBus.menu_closed.emit()
```

---

## Main Menu

```gdscript
# scenes/ui/main_menu.gd
extends Control

@onready var new_game_btn   = $VBox/NewGameButton
@onready var continue_btn   = $VBox/ContinueButton
@onready var slot_buttons   = $VBox/SaveSlots
@onready var quit_btn       = $VBox/QuitButton

func _ready() -> void:
    # Show "Continue" only if save exists
    continue_btn.visible = GameManager.save_exists(1)
    new_game_btn.pressed.connect(_new_game)
    continue_btn.pressed.connect(func(): GameManager.load_game(1))
    quit_btn.pressed.connect(func(): get_tree().quit())
    # Show save slot info
    for i in 3:
        var info = GameManager.get_save_info(i + 1)
        var btn  = slot_buttons.get_child(i)
        if info.get("exists"):
            btn.text = "Slot %d  —  Lv.%d  %s" % [i+1, info["char_lvl"], info["level"]]
        else:
            btn.text = "Slot %d  —  Empty" % (i + 1)
        btn.pressed.connect(_load_slot.bind(i + 1))
    AudioManager.play_music("res://audio/music_menu.ogg")

func _new_game() -> void:
    GameManager.flags                = {}
    GameManager.current_level_id     = "level_01_outdoor"
    GameManager.requested_entry_point = "default"
    GameManager.change_level("level_01_outdoor")

func _load_slot(slot: int) -> void:
    GameManager.load_game(slot)
```
