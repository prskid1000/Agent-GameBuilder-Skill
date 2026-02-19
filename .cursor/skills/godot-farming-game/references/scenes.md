# Scene Trees Reference

## scenes/characters/player.tscn

```
CharacterBody2D "Player"           player.gd | group: "Player"
  Sprite2D                         texture: main_basic.png | hframes=33 vframes=4
  CollisionShape2D                 CapsuleShape2D r=4 h=8
  Camera2D                         zoom=(4,4)
  RayCast2D                        target_position=(0,20) | enabled=true
  Animation/
    AnimationPlayer                autoplay="idle_down"
    AnimationTree                  active=true | tree_root=BlendTree | anim_player=AnimationPlayer
  ToolUI                           instance: scenes/ui/tool_ui.tscn
  FishingGame                      instance: scenes/ui/fishing_game.tscn
```

**Collision:** layer=2 (Player), mask=1 (Terrain)

**AnimationPlayer animations list:**
```
idle_down, idle_left, idle_right, idle_up
walk_down, walk_left, walk_right, walk_up
axe_down, axe_left, axe_right, axe_up
hoe_down, hoe_left, hoe_right, hoe_up
water_down, water_left, water_right, water_up
sword_down, sword_left, sword_right, sword_up
fish_down, fish_left, fish_right, fish_up
seed_down, seed_left, seed_right, seed_up
```
Each animation: Sprite2D frame property track + Method track calling `tool_use_emit()` at hit frame.

---

## scenes/levels/level.tscn

```
Node2D "Level"                     level.gd
  Layers/
    WaterLayer      TileMapLayer   z_index=-2 | tileset: water.png (animated, 4 frames @0.4s each)
    GrassLayer      TileMapLayer   z_index=-2 | tileset: grass.png | physics layer 1=Terrain
    SoilLayer       TileMapLayer   z_index=-2 | tileset: soil.png
    SoilWaterLayer  TileMapLayer   z_index=-2 | tileset: soil_water.png | modulate.a=~200/255
    RainFloorParticles GPUParticles2D  emitting=false | texture: weather/floor.png
  Objects/           Node2D        y_sort_enabled=true
    Player           instance player.tscn          pos=(~200,300)
    ScareCrow        instance scare_crow.tscn       pos=(173,389) | max_range=150
    House            instance house.tscn            pos=(232,224)
    Tree ... Tree31  instance tree.tscn ×31         (distributed across map)
    SimpleObject ... SimpleObject37  instance simple_object.tscn ×37
  Overlay/           Node2D
    DayTimeColor     CanvasModulate                 color=white (driven by script)
    CanvasLayer      CanvasLayer
      DayTransitionLayer  ColorRect               anchors=full rect | color=dark gray
                                                  material: ShaderMaterial(circle_transition.gdshader)
      PlantInfoContainer  instance plant_info_container.tscn
    RainDropsParticles GPUParticles2D              emitting=false | texture: weather/drops.png
    MachinePreviewSprite Sprite2D                  texture: icons/sprinkler.png (default)
  Timers/            Node
    DayTimer         Timer          wait_time=120 | one_shot=true | autostart=true
    BlobTimer        Timer          wait_time=20  | autostart=true
  BlobSpawnPositions Node2D
    Marker2D  pos=(455,194)
    Marker2D2 pos=(575,212)
    Marker2D3 pos=(656,311)
    Marker2D4 pos=(687,409)
    Marker2D5 pos=(633,488)
    Marker2D6 pos=(595,570)
    Marker2D7 pos=(342,643)
    Marker2D8 pos=(33,641)
    Marker2D9 pos=(-43,482)
    Marker2D10 pos=(7,203)
    Marker2D11 pos=(292,185)
```

**Signal connections in level.tscn:**
```
Objects/Player.tool_use       → Level._on_player_tool_use
Objects/Player.day_change     → Level._on_player_day_change
Objects/Player.diagnose       → Level._on_player_diagnose
Objects/Player.machine_change → Level._on_player_machine_change
Objects/Player.build          → Level._on_player_build
Timers/BlobTimer.timeout      → Level._on_blob_timer_timeout
```

---

## scenes/objects/plant.tscn

```
StaticBody2D "Plant"               plant.gd | group: "Plants"
  FlashSprite2D                    instance: vfx/flash_sprite_2d.tscn
                                   transform.y = -9
  CollisionShape2D                 CapsuleShape2D r=4 h=6
  CollisionArea       Area2D       no layer | mask=2 (Player)
    CollisionShape2D               CircleShape2D r=8
```

**Collision:** layer=3 (Objects), no mask

---

## scenes/objects/tree.tscn

```
StaticBody2D "Tree"                tree.gd | group: "Objects"
  FlashSprite2D                    instance: vfx/flash_sprite_2d.tscn
                                   texture: plants/tree.png | hframes=2
  Stump            Sprite2D        texture: plants/stump.png | visible=false | transform.y=10.5
  CollisionShape2D                 CapsuleShape2D r=8 h=22 | transform.y=4
  Apples           Node2D
  AppleSpawnPositions Node2D
    Marker2D pos=(various)
    Marker2D pos=(various)
    Marker2D pos=(various)
```

**Collision:** layer=3 (Objects), no mask

---

## scenes/objects/simple_object.tscn

```
StaticBody2D "SimpleObject"        simple_object.gd (@tool) | group: "Objects"
  Sprite2D                         texture: tilesets/decoration.png | hframes=4 vframes=2
  CollisionShape2D                 RectangleShape2D size=(10,4)
```

**Collision:** layer=1 (Terrain), no mask
**Note:** `z_index` and `collision.disabled` are set dynamically from `size` export var.

---

## scenes/objects/blob.tscn

```
CharacterBody2D "Blob"             blob.gd | group: "Objects" + "Blobs"
  FlashSprite2D                    instance: vfx/flash_sprite_2d.tscn
                                   texture: characters/blob.png | hframes=14 vframes=4
  CollisionShape2D                 CircleShape2D r=6
  AnimationPlayer
    move   (frames 3-6, loop, autoplay)
    explode (frames 7-13, no loop, calls queue_free at end via Method track)
```

**Collision:** layer=3 (Objects), mask=1 (Terrain)

---

## scenes/vfx/flash_sprite_2d.tscn

```
Sprite2D "FlashSprite2D"           flash_sprite_2d.gd
  material: ShaderMaterial
    shader: shaders/flash.tres
    shader_parameter/Progress = 0.0
    resource_local_to_scene = true    ← CRITICAL
```

---

## scenes/machines/machine.tscn (base — not instantiated directly)

```
StaticBody2D "Machine"             machine.gd | group: "Machines"
  CollisionShape2D
```

---

## scenes/machines/sprinkler.tscn

```
Machine "Sprinkler"                sprinkler.gd
  AnimatedSprite2D                 texture: machines/sprinkler.png
    animations: "default", "action"
  GPUParticles2D                   water particle effect | emitting=false
  Timer                            wait_time=~30s
```

---

## scenes/machines/scare_crow.tscn

```
Machine "ScareCrow"                scare_crow.gd
  Sprite2D                         texture: machines/scarecrow.png
  Timer                            wait_time=~5s | autostart=true
```

**Note:** ScareCrow is pre-placed in level scene (not built by player in base version).
Signal `shoot_projectile` connected to `level.create_projectile` in `level._ready()`.

---

## scenes/machines/fisher.tscn

```
Machine "Fisher"                   fisher.gd
  AnimatedSprite2D                 texture: machines/fisher.png
    animations: "down","left","right","up","down_idle","left_idle","right_idle","up_idle"
  Timer                            wait_time=~10s
  Control/
    TextureProgressBar             texture: ui/fisher_bar.png
```

---

## scenes/machines/projectile.tscn

```
Area2D "Projectile"                projectile.gd
  Sprite2D                         texture: machines/projectile.png
  CollisionShape2D                 CircleShape2D r=3
```

**Collision:** no layer, mask=3 (Objects — detects blobs)

---

## scenes/ui/tool_ui.tscn

```
Control "ToolUI"                   tool_ui.gd
  ToolContainer    HBoxContainer   custom_min_size=(100,30) | anchor=center | offset.bottom=-30
  SeedContainer    HBoxContainer   (same layout as ToolContainer)
  HideTimer        Timer           wait_time=1 | one_shot=true
```

---

## scenes/ui/tool_ui_texture.tscn

```
Control "ToolUITexture"            tool_ui_texture.gd
  TextureRect                      custom_min_size=(16,16) | expand_mode=FitWidth
                                   stretch_mode=KeepAspectCentered
```

---

## scenes/ui/fishing_game.tscn

```
Node2D "FishingGame"               fishing_game.gd
  Control/
    NinePatchRect                  texture: ui/fish_frame.png | custom_min_size=(?,100)
    TextureProgressBar             under: ui/fish_progress_bg.png | progress: ui/fish_progress.png
  BarSprite   Sprite2D             texture: ui/bar.png
  FishSprite  Sprite2D             texture: icons/goldfish.png
  FishUpdateTimer Timer            wait_time=randf(1,3) | autostart=true
```

---

## scenes/ui/plant_info.tscn

```
PanelContainer "PlantInfo"         plant_info.gd
  theme: game_theme.tres
  HBoxContainer
    IconTexture  TextureRect       custom_min_size=(40,40) | stretch_mode=KeepAspectCentered
    VBoxContainer
      NameLabel  Label
      GrowthBar  TextureProgressBar  under/progress: ui/v_bar.png | nine_patch_stretch=true
                                     custom_min_size.y=6 | tint_progress=8F62F (green)
      DeathBar   TextureProgressBar  under/progress: ui/v_bar.png | nine_patch_stretch=true
                                     custom_min_size.y=6 | tint_progress=C6441D (red)
```

---

## scenes/ui/plant_info_container.tscn

```
Control "PlantInfoContainer"       plant_info_container.gd
  MarginContainer                  anchor=left strip | custom_min_size.x=200
                                   theme_override_constants/margin_left=10
                                   theme_override_constants/margin_top=10
    ScrollContainer
      VBoxContainer                size_flags_horizontal=EXPAND
```

---

## scenes/ui/game_theme.tres

Theme resource applied to UI nodes. Key overrides:
- Label font: `HomeVideo-Regular.ttf` (FontVariation, size=30, extra_spacing_glyph=1)
- Label font_color: `#060606`
- PanelContainer style/panel: StyleBoxTexture → texture=`ui/frame.png`, margins=6 all sides

---

## scenes/levels/house.tscn

```
Node2D "House"                     house.gd
  WallsLayer  TileMapLayer         tileset: HouseTileSet.tres (premade)
  FloorLayer  TileMapLayer         tileset: walls_floor_tile.png
  RoofLayer   TileMapLayer         tileset: roof.png
  TV           instance tv.tscn    pos=(inside house)
  Bed          instance bed.tscn   pos=(inside house)
  Sprites (carpet, bookshelf, table, nightstand, plant decorations)
  HouseArea  Area2D + CollisionShape2D  (triggers in_house setter)
```

---

## scenes/levels/bed.tscn

```
StaticBody2D "Bed"                 bed.gd
  Sprite2D                         texture: objects/bed.png
  CollisionShape2D                 RectangleShape2D
```

---

## scenes/levels/tv.tscn

```
StaticBody2D "TV"                  tv.gd
  AnimatedSprite2D                 texture: machines/tv.png
    animations: "default", "rain", "sun"
  CollisionShape2D                 RectangleShape2D
  Timer                            wait_time=3 | one_shot=true
```
