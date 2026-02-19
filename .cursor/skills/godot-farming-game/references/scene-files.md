# Scene Files — Line-by-Line Reference
# Every .tscn node, property, and connection explained

## How to read .tscn files

A `.tscn` file has three sections:
```
[ext_resource]   → external files this scene depends on (scripts, textures, other scenes)
[sub_resource]   → data defined INSIDE this file (shapes, materials, animations)
[node]           → the actual scene tree — one block per node
[connection]     → signal→method wiring
```

`collision_layer` uses a bitmask: layer 1 = bit 1 = value 1, layer 2 = bit 2 = value 2,
layer 3 = bit 4 = value 4, layer 4 = bit 8 = value 8.
Multiple layers: layer 1+2 = value 3, layers 1+4 (Terrain+Objects) = value 5, etc.

---

## scenes/vfx/flash_sprite_2d.tscn
> The reusable white-flash sprite. Shared by plant, tree, and blob as a child scene.

```
[gd_scene load_steps=4]
# load_steps=4 → 2 ext_resources + 1 sub_resource + 1 node = 4 things to load

[ext_resource path="shaders/flash.tres"]
# The VisualShader that mixes original color with white based on "Progress" float parameter

[ext_resource path="scenes/vfx/flash_sprite_2d.gd"]
# The script that exposes the flash(start, end, callback) method

[sub_resource type="ShaderMaterial"]
resource_local_to_scene = true
# CRITICAL: true = this material instance is unique per scene instance.
# If false, hitting one tree would flash ALL trees simultaneously.
shader = flash.tres
shader_parameter/Color = Color(1, 1, 1, 1)   # White is the flash target color
shader_parameter/Progress = 0.0               # 0 = invisible effect (shows original texture)

[node name="FlashSprite2D" type="Sprite2D"]
# Root node is a Sprite2D so the texture property works normally
# Whoever instances this scene sets .texture, .hframes etc. after instantiating
material = ShaderMaterial   # Attach the local shader material
script = flash_sprite_2d.gd # Adds the flash() method
```

---

## scenes/objects/plant.tscn
> One growing crop. StaticBody2D so it blocks the player slightly. Has two collision shapes.

```
[gd_scene load_steps=7]

[ext_resource path="scenes/objects/plant.gd"]
[ext_resource path="scenes/vfx/flash_sprite_2d.tscn"]   # Reuse flash sprite
[ext_resource path="shaders/flash.tres"]                  # Needed to create local ShaderMaterial

[sub_resource type="CapsuleShape2D"]
radius = 3.0
height = 6.0
# Small capsule — just large enough to show a plant is here, small enough to walk between

[sub_resource type="CircleShape2D"]
# Default size (radius=10) — used by CollisionArea to detect player overlap for harvest
# Larger than the body collision so harvest triggers when player WALKS NEAR, not exactly on top

[sub_resource type="ShaderMaterial"]
resource_local_to_scene = true    # Each plant flashes independently
shader = flash.tres
shader_parameter/Progress = 0.0  # Start with no flash

[node name="Plant" type="StaticBody2D" groups=["Plants"]]
collision_layer = 4               # Bit 3 = layer 3 "Objects" — trees/machines/plants share this layer
collision_mask = 0                # Plant doesn't need to DETECT anything itself
script = plant.gd                 # Provides setup(), grow(), damage()

  [node name="CollisionShape2D" parent="."]
  shape = CapsuleShape2D          # Small body blocker — stops player walking INTO the plant center

  [node name="CollisionArea" type="Area2D" parent="."]
  collision_layer = 0             # Area2D doesn't need its own physics layer
  collision_mask = 2              # Bit 2 = layer 2 "Player" — only detects the player CharacterBody2D
  # This is what triggers harvest when the player walks close

    [node name="CollisionShape2D" parent="CollisionArea"]
    shape = CircleShape2D         # Larger circle — generous harvest detection radius

  [node name="FlashSprite2D" parent="." instance=flash_sprite_2d.tscn]
  material = ShaderMaterial       # Override with local material (required for independent flash)
  position = Vector2(0, -9)       # Shift UP 9px so sprite sits centered in tile, not at ground level
  hframes = 4                     # 4 growth stages (0=seed, 1=sprout, 2=growing, 3=mature)
  # NOTE: hframes is set here as default; plant.gd overrides it with res.h_frames in setup()

[connection signal="body_entered" from="CollisionArea" to="." method="_on_collision_area_body_entered"]
# When player enters CollisionArea → call plant._on_collision_area_body_entered() → harvest check
```

---

## scenes/objects/tree.tscn
> Choppable tree with health, apple spawn positions, and a hidden stump fallback sprite.

```
[gd_scene load_steps=8]

[ext_resource path="scenes/objects/tree.gd"]
[ext_resource path="graphics/plants/tree.png"]     # 2-frame tree spritesheet (2 visual variants)
[ext_resource path="scenes/vfx/flash_sprite_2d.tscn"]
[ext_resource path="graphics/plants/stump.png"]    # Stump shown after tree is chopped down
[ext_resource path="shaders/flash.tres"]

[sub_resource type="CapsuleShape2D"]
radius = 8.0
height = 22.0
# Taller than a plant collision — represents tree trunk, not just the base

[sub_resource type="ShaderMaterial"]
resource_local_to_scene = true    # Each tree flashes independently
shader = flash.tres
shader_parameter/Progress = 0.0  # No flash at start

[node name="Tree" type="StaticBody2D" groups=["Objects"]]
collision_layer = 4               # Layer 3 = "Objects" — hit by axe/sword checks
collision_mask = 0                # Tree doesn't need to detect anything
script = tree.gd                  # Provides hit(), reset(), create_apples()

  [node name="CollisionShape2D" parent="."]
  position = Vector2(0, 4)        # Offset 4px DOWN — collision sits at base of trunk, not at center
  shape = CapsuleShape2D          # Tall capsule matching the trunk visual

  [node name="Stump" type="Sprite2D" parent="."]
  visible = false                 # Hidden by default — tree.gd shows it when health reaches 0
  position = Vector2(0, 10.5)     # Lower than tree center — sits on the ground
  texture = stump.png             # The stump image

  [node name="FlashSprite2D" parent="." instance=flash_sprite_2d.tscn]
  material = ShaderMaterial       # Local material for independent flash
  texture = tree.png              # Set the tree texture on the flash sprite
  hframes = 2                     # 2 tree variants — tree.gd picks one randomly in _ready()

  [node name="AppleSpawnPositions" type="Node2D" parent="."]
  # Container for apple spawn marker points — tree.gd reads .get_children() to place apples

    [node name="Marker2D" parent="AppleSpawnPositions"] position = Vector2(7, 5)
    [node name="Marker2D2" parent="AppleSpawnPositions"] position = Vector2(8, -4)
    [node name="Marker2D3" parent="AppleSpawnPositions"] position = Vector2(-10, -4)
    [node name="Marker2D4" parent="AppleSpawnPositions"] position = Vector2(-9, 4)
    [node name="Marker2D5" parent="AppleSpawnPositions"] position = Vector2(-4, -1)
    [node name="Marker2D6" parent="AppleSpawnPositions"] position = Vector2(-4, -8)
    [node name="Marker2D7" parent="AppleSpawnPositions"] position = Vector2(4, -11)
    # 7 possible apple positions spread around the tree crown — tree.gd picks 0-3 randomly

  [node name="Apples" type="Node2D" parent="."]
  # Empty container — tree.gd dynamically adds Sprite2D children here for each apple
  # On reset(): all children are queue_free()d, then new ones are created
```

---

## scenes/objects/simple_object.tscn
> Bush or rock decoration. @tool script makes size/style live-editable in the Godot editor.

```
[gd_scene load_steps=4]

[ext_resource path="graphics/tilesets/decoration.png"]
# 4×2 sprite sheet: 4 sizes (cols) × 2 styles (rows: bush=row0, rock=row1)
[ext_resource path="scenes/objects/simple_object.gd"]   # @tool script

[sub_resource type="RectangleShape2D"]
size = Vector2(10, 4)
# Flat rectangle — matches the visual footprint of a small bush/rock on the ground

[node name="SimpleObject" type="StaticBody2D"]
collision_mask = 0              # Doesn't need to detect anything
script = simple_object.gd       # @tool script runs in editor AND at runtime
random = true                   # Export var — at _ready() will pick random size/style
# collision_layer not set = uses default (layer 1 = Terrain)

  [node name="Sprite2D" parent="."]
  texture = decoration.png
  hframes = 4                   # 4 horizontal frames = 4 size variants (tiny to large)
  vframes = 2                   # 2 vertical frames = 2 style variants (bush/rock)
  # frame_coords = Vector2i(size, style) set in script

  [node name="CollisionShape2D" parent="."]
  shape = RectangleShape2D      # simple_object.gd sets .disabled = true if size < 2
```

---

## scenes/objects/blob.tscn
> Enemy blob with move animation, explode animation, and flash-on-hit.

```
[gd_scene load_steps=11]

[ext_resource path="scenes/objects/blob.gd"]
[ext_resource path="scenes/vfx/flash_sprite_2d.tscn"]
[ext_resource path="shaders/flash.tres"]
[ext_resource path="graphics/characters/blob.png"]   # 14×4 spritesheet

[sub_resource type="ShaderMaterial"]
resource_local_to_scene = true    # Each blob flashes independently
shader = flash.tres
shader_parameter/Progress = 0.0

[sub_resource type="CircleShape2D"]
radius = 5.0                      # Small circle — blobs squeeze through tight gaps

# --- ANIMATIONS ---
[sub_resource type="Animation" resource_name="RESET" length=0.001]
# RESET animation: one-frame (length 0.001s), sets frame=0 (first blob frame)
# Godot generates RESET automatically; used to restore default state
tracks/0 path=NodePath("FlashSprite2D:frame")
keys = { values: [0] }            # Just sets frame to 0

[sub_resource type="Animation" resource_name="explode" length=1.4]
# Explode animation: plays frames 7-13 of the blob sprite (the explosion sequence)
# length=1.4s, 7 keyframes × 0.2s apart = uses bottom rows of the 14×4 sheet
tracks/0 path=NodePath("FlashSprite2D:frame")
keys = { times: [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2], values: [7, 8, 9, 10, 11, 12, 13] }
# Second track: method call at the END of the animation (t=1.4)
tracks/1 type="method" path=NodePath(".")
keys = { times: [1.4], values: [{ method: "queue_free", args: [] }] }
# queue_free() called at 1.4s → blob disappears exactly when explosion finishes

[sub_resource type="Animation" resource_name="move" length=0.8 loop_mode=1]
# Move animation: loops frames 3-6 of the blob sprite (the walking/moving sequence)
# loop_mode=1 → loops forever while blob is alive
tracks/0 path=NodePath("FlashSprite2D:frame")
keys = { times: [0, 0.2, 0.4, 0.6], values: [3, 4, 5, 6] }

[sub_resource type="AnimationLibrary"]
_data = { "RESET": RESET_anim, "explode": explode_anim, "move": move_anim }

[node name="Blob" type="CharacterBody2D" groups=["Blobs", "Objects"]]
# In TWO groups: "Blobs" (targeted by scarecrow projectiles) and "Objects" (hit by axe/sword)
collision_layer = 4               # Layer 3 "Objects" (same as trees/plants)
# No collision_mask listed = defaults 0 — blob's body doesn't block against layers
# But it DOES move through terrain because CharacterBody2D with mask=1 would add that
script = blob.gd

  [node name="FlashSprite2D" parent="." instance=flash_sprite_2d.tscn]
  material = ShaderMaterial        # Local material
  texture = blob.png               # 14×4 frame spritesheet
  hframes = 14                     # 14 horizontal frames (all animation stages side by side)
  vframes = 4                      # 4 vertical frames (different blob states)

  [node name="CollisionShape2D" parent="."]
  shape = CircleShape2D            # r=5 circle for physics body

  [node name="AnimationPlayer" parent="."]
  libraries = { "": AnimationLibrary }   # Default library (empty string key = default)
  autoplay = "move"                # Start playing move animation immediately on spawn
```

---

## scenes/machines/machine.tscn
> The base machine scene. Never used directly — sprinkler/fisher/scarecrow all `instance` this.

```
[gd_scene load_steps=2]

[ext_resource path="scenes/machines/machine.gd"]
# Provides setup(pos, level, parent) and delete(delete_coord)

[node name="Machine" type="StaticBody2D" groups=["Machines"]]
# All machines share the "Machines" group — used by DELETE mode to find and remove them
script = machine.gd
# collision_layer/mask not set here — child scenes override these

  [node name="CollisionShape2D" parent="."]
  # Shape not set here — each child scene sets the appropriate shape
```

---

## scenes/machines/sprinkler.tscn
> Instances machine.tscn and adds watering animation, particle burst, and a firing timer.

```
[gd_scene load_steps=12]

# Instances machine.tscn as the root — inherits Machine group + CollisionShape2D
[ext_resource path="scenes/machines/machine.tscn"]
[ext_resource path="scenes/machines/sprinkler.gd"]
[ext_resource path="graphics/machines/sprinkler.png"]   # 4-frame horizontal spritesheet

# AtlasTexture sub-resources: each slices a 16×16 region from sprinkler.png
# Frame 0: region Rect2(0,0,16,16)    — idle frame
# Frame 1: region Rect2(16,0,16,16)   — water arc frame 1
# Frame 2: region Rect2(32,0,16,16)   — water arc frame 2
# Frame 3: region Rect2(48,0,16,16)   — water arc frame 3

[sub_resource type="SpriteFrames"]
animations:
  "action":  frames=[0,1,2,3], loop=false, speed=5.0
  # Non-looping — plays once when watering, then stops
  "default": frames=[0], loop=true, speed=5.0
  # Single-frame idle animation (just stays on frame 0)

[sub_resource type="RectangleShape2D"]
size = Vector2(6, 8)              # Narrow collision — sprinkler is a small machine

[sub_resource type="ParticleProcessMaterial"]
# Water particle burst configuration
particle_flag_disable_z = true    # 2D game — no Z axis movement
emission_shape = 6                # Ring emission shape
emission_ring_inner_radius = 8.0  # Particles emit from ~8px radius ring around center
spread = 180.0                    # Wide spread — particles go in all directions
initial_velocity_min/max = 10,15  # Slow moving particles (water droplets)
gravity = Vector3(0,0,0)          # No gravity — water floats (stylized)
color = Color(0.027, 0.814, 0.88) # Cyan-blue water color

[node name="Sprinkler" instance=machine.tscn]   # Root inherits from machine.tscn
script = sprinkler.gd

  [node name="CollisionShape2D" parent="." index=0]
  # index=0 means this OVERRIDES the CollisionShape2D inherited from machine.tscn
  shape = RectangleShape2D (6×8)

  [node name="AnimatedSprite2D" parent="." index=1]
  position = Vector2(0, -2)       # Offset 2px up — sprite sits slightly above ground
  sprite_frames = SpriteFrames    # The action/default animations defined above
  autoplay = "default"            # Start in idle state

  [node name="Timer" parent="." index=2]
  wait_time = 5.0                 # Water every 5 seconds (in .example — production might be 30s)
  autostart = true                # Start counting immediately when placed

  [node name="GPUParticles2D" parent="." index=3]
  position = Vector2(0, -3)       # Slightly above ground for visual alignment
  emitting = false                # Off by default — turned on by sprinkler.gd in _on_timer_timeout
  amount = 50                     # 50 water particles per burst
  one_shot = true                 # One burst per activation (not continuous)
  process_material = ParticleProcessMaterial

[connection signal="timeout" from="Timer" to="." method="_on_timer_timeout"]
# Timer fires → _on_timer_timeout() in sprinkler.gd → animation + particles + signal
```

---

## scenes/machines/scare_crow.tscn
> Instances machine.tscn. Adds a static sprite and a fast-firing timer.

```
[gd_scene load_steps=5]

[ext_resource path="scenes/machines/machine.tscn"]
[ext_resource path="scenes/machines/scare_crow.gd"]
[ext_resource path="graphics/machines/scarecrow.png"]   # 4-frame sprite (4 variants)

[sub_resource type="RectangleShape2D"]
size = Vector2(10, 12)            # Slightly larger than sprinkler — scarecrow is taller

[node name="ScareCrow" instance=machine.tscn]
script = scare_crow.gd

  [node name="CollisionShape2D" parent="." index=0]
  position = Vector2(0, -2)       # Collision sits at foot, not center
  shape = RectangleShape2D (10×12)

  [node name="Sprite2D" parent="." index=1]
  position = Vector2(0, -8)       # Visual sits 8px above center (scarecrow is tall)
  texture = scarecrow.png
  hframes = 4                     # 4 scarecrow variants (different hat styles etc.)
  # frame is set randomly or left at 0 — currently not randomized in .example

  [node name="Timer" parent="." index=2]
  # wait_time not set = default 1.0s — fires every second to check for nearby blobs
  autostart = true                # Immediately start checking for blobs after being placed

[connection signal="timeout" from="Timer" to="." method="_on_timer_timeout"]
# Fast timer (1s) → check for blobs → fire projectile if one is in range
```

---

## scenes/machines/fisher.tscn
> Instances machine.tscn. Uses a premade SpriteFrames resource with 8 directional animations.

```
[gd_scene load_steps=6]

[ext_resource path="scenes/machines/machine.tscn"]
[ext_resource path="scenes/machines/fisher.gd"]
[ext_resource path="premade/fisher.tres"]   # Pre-made SpriteFrames with 8 animations:
# "down", "left", "right", "up" (cast animations)
# "down_idle", "left_idle", "right_idle", "up_idle" (holding-line animations)
[ext_resource path="graphics/ui/v_bar.png"] # Reuses the same bar texture from plant_info

[sub_resource type="RectangleShape2D"]
size = Vector2(6, 10)             # Narrow vertical shape — fisher is upright

[node name="Fisher" instance=machine.tscn]
script = fisher.gd

  [node name="CollisionShape2D" parent="." index=0]
  shape = RectangleShape2D (6×10)

  [node name="AnimatedSprite2D" parent="." index=1]
  sprite_frames = fisher.tres    # Use premade animations (saves defining them in this file)
  animation = "left_idle"        # Default — fisher.gd overrides in setup() based on coast direction

  [node name="Timer" parent="." index=2]
  wait_time = 5.0                # Wait 5 seconds between catches
  one_shot = true                # Does NOT autostart — started by start_fishing() in fisher.gd

  [node name="Control" parent="." index=3]
  anchors_preset = 8 (center)   # Control node centered on machine position
  # Container for the progress bar UI

    [node name="TextureProgressBar" parent="Control" index=0]
    custom_minimum_size = Vector2(20, 1)  # Very thin bar (1px tall = horizontal-style)
    anchor_right/bottom = 1.0             # Stretch to fill Control width
    offset_bottom = -22.0                 # Offset above the fisher sprite
    nine_patch_stretch = true
    texture_under/progress = v_bar.png    # Same bar texture as plant info panels
    tint_under = Color(0.18, 0.18, 0.18)  # Dark gray background
    tint_progress = Color(0.25, 1.0, 0.39) # Bright green fill

[connection signal="timeout" from="Timer" to="." method="_on_timer_timeout"]
# Timer fires → _on_timer_timeout() → restart the fishing cycle
```

---

## scenes/machines/projectile.tscn
> A flying Area2D that detects blobs. Has a safety timer that deletes it if it misses.

```
[gd_scene load_steps=4]

[ext_resource path="scenes/machines/projectile.gd"]
[ext_resource path="graphics/machines/projectile.png"]   # Small projectile sprite

[sub_resource type="CircleShape2D"]
radius = 3.0                      # Very small — only hits things it's very close to

[node name="Projectile" type="Area2D"]
collision_layer = 0               # No layer — projectile doesn't occupy physics space
collision_mask = 4                # Bit 3 = layer 3 "Objects" — detects blobs (and trees!)
# NOTE: mask=4 means it technically detects trees too, but projectile.gd
# only acts on bodies in the "Blobs" group, so trees are ignored
script = projectile.gd

  [node name="Sprite2D" parent="."]
  texture = projectile.png        # The visual bullet/seed sprite

  [node name="CollisionShape2D" parent="."]
  shape = CircleShape2D (r=3)     # Tiny circle hitbox

  [node name="Timer" parent="."]
  wait_time = 10.0                # Safety timeout — if projectile doesn't hit anything in 10s
  one_shot = true
  autostart = true                # Starts counting immediately on spawn

[connection signal="body_entered" from="." to="." method="_on_body_entered"]
# Area2D overlaps a physics body → check if it's a blob → hit it + queue_free
[connection signal="timeout" from="Timer" to="." method="queue_free"]
# Safety: projectile auto-deletes after 10 seconds if it never hit anything
```

---

## scenes/ui/tool_ui.tscn
> Two HBoxContainers (tools + seeds) floating centered above the player. Hidden until Q/E/C pressed.

```
[gd_scene load_steps=2]

[ext_resource path="scenes/ui/tool_ui.gd"]

[node name="ToolUI" type="Control"]
layout_mode = 3                   # Follows parent's layout (anchors mode)
anchors_preset = 8                # Preset 8 = CENTER — origin is at parent center
anchor_left/top/right/bottom = 0.5  # All anchors at center point
grow_horizontal/vertical = 2      # Grow in BOTH directions from center
script = tool_ui.gd               # Dynamically builds icon rows on _ready()

  [node name="ToolContainer" type="HBoxContainer" parent="."]
  custom_minimum_size = Vector2(100, 30)  # 100px wide, 30px tall container
  anchors_preset = -1             # Custom anchor (not a preset)
  anchor_left/top/right/bottom = 0.5     # Centered on parent
  offset_left = -50.0             # -50 from center = starts 50px left of center
  offset_top = -30.0              # -30 from center = sits 30px ABOVE player center
  offset_right = 50.0             # +50 = ends 50px right of center
  offset_bottom = -10.0           # -10 = bottom edge 10px above center
  # Net result: 100×20px bar centered horizontally, 10-30px above player
  grow_horizontal/vertical = 2    # Grow in both directions

  [node name="SeedContainer" type="HBoxContainer" parent="."]
  # Exact same layout as ToolContainer — they overlap and only one is shown at a time
  # tool_ui.gd hides one and shows the other based on reveal(bool)
  custom_minimum_size = Vector2(100, 30)
  [... same anchor/offset values as ToolContainer ...]

  [node name="HideTimer" type="Timer" parent="."]
  one_shot = true                 # Fires once then stops (must be restarted each key press)
  # wait_time not set = default 1.0s — hides containers after 1 second of no input

[connection signal="timeout" from="HideTimer" to="." method="_on_hide_timer_timeout"]
# 1 second after last key press → _on_hide_timer_timeout() → hide both containers
```

---

## scenes/ui/tool_ui_texture.tscn
> A single icon within the tool/seed row. 20×20px container with a centered 16×16 TextureRect.

```
[gd_scene load_steps=3]

[ext_resource path="graphics/icons/axe.png"]
# Default texture (axe). tool_ui.gd replaces this with the correct icon via setup()
[ext_resource path="scenes/ui/tool_ui_texture.gd"]

[node name="ToolUITexture" type="Control"]
custom_minimum_size = Vector2(20, 20)   # Reserve 20×20px in the HBoxContainer
anchors_preset = 0 (top-left)
offset_right/bottom = 20.0             # Total size: 20×20px
script = tool_ui_texture.gd            # Exposes setup(enum, texture) and highlight(bool)

  [node name="TextureRect" parent="."]
  custom_minimum_size = Vector2(16, 16) # Icon is 16×16 inside the 20×20 container (4px padding)
  anchors_preset = 8 (CENTER)           # Center the 16×16 rect within the 20×20 space
  anchor_left/top/right/bottom = 0.5
  offset_left/top = -8.0               # -8 from center = start 8px left/up
  offset_right/bottom = 8.0            # +8 from center = end 8px right/down
  grow_horizontal/vertical = 2         # Grow from center when highlight() tweens size up to 20×20
  texture = axe.png                    # Default — overridden by setup()
  expand_mode = 2 (FitWidth)           # Scale icon to fit width while keeping aspect ratio
  # When highlight() tweens custom_minimum_size to 20×20,
  # the TextureRect expands to fill, making the selected icon visually larger
```

---

## scenes/ui/fishing_game.tscn
> The fishing minigame overlay. Centered on the player. Z-index=2 so it draws above everything.

```
[gd_scene]

[ext_resource path="scenes/ui/fishing_game.gd"]
[ext_resource path="graphics/ui/fish_frame.png"]     # Frame/border around the minigame area
[ext_resource path="graphics/ui/fish_progress_bg.png"]  # Progress bar background
[ext_resource path="graphics/ui/fish_progress.png"]     # Progress bar fill
[ext_resource path="graphics/ui/bar.png"]            # The catchable bar (player moves this up/down)
[ext_resource path="graphics/icons/goldfish.png"]    # The fish the player is trying to catch

[node name="FishingGame" type="Node2D"]
z_index = 2                       # Draws on top of player (z=0) and most UI elements
script = fishing_game.gd          # All minigame logic

  [node name="Control" parent="."]
  anchors_preset = 8 (CENTER)     # Centered on player position (FishingGame is child of Player)

    [node name="NinePatchRect" parent="Control"]
    custom_minimum_size = Vector2(20, 150)
    # 20px wide, 150px tall — defines the play area height
    # fishing_game.gd uses this to calculate y_range = 150 - 10 = 140px play area
    anchors_preset = 15 (FULL RECT)  # Fills the Control container
    texture = fish_frame.png         # The decorative border around the minigame
    patch_margin_left/top/right = 5  # 5px patch margins preserve border corners
    patch_margin_bottom = 20         # Extra bottom margin for visual tail

    [node name="TextureProgressBar" parent="Control"]
    custom_minimum_size = Vector2(10, 130)
    fill_mode = 3                    # Fill from BOTTOM up (progress fills upward)
    nine_patch_stretch = true
    offset_left = 40.0               # Offset right of the frame
    texture_under = fish_progress_bg.png  # Gray background
    texture_progress = fish_progress.png  # Colored fill
    # fishing_game.gd drives .value every frame (0-100)

  [node name="BarSprite" type="Sprite2D" parent="."]
  texture = bar.png
  # The movable bar. Player presses Space to push it up.
  # Position driven every frame by fishing_game.gd velocity physics

  [node name="FishSprite" type="Sprite2D" parent="."]
  texture = goldfish.png
  # The fish icon. Bounces up/down randomly.
  # Position driven every frame by fish_velocity in fishing_game.gd

  [node name="FishUpdateTimer" parent="."]
  autostart = true                   # Immediately start randomizing fish direction

[connection signal="value_changed" from="Control/TextureProgressBar" to="." method="_on_texture_progress_bar_value_changed"]
# Progress bar hits 0 or 100 → minigame ends → stop_fishing() called on player

[connection signal="timeout" from="FishUpdateTimer" to="." method="_on_fish_update_timer_timeout"]
# Random interval → change fish velocity direction
```

---

## scenes/ui/plant_info.tscn
> One plant panel: icon + name label + green growth bar + red death bar.

```
[gd_scene load_steps=5]

[ext_resource path="graphics/icons/tomato.png"]  # Default icon (overridden by plant_info.gd setup)
[ext_resource path="scenes/ui/game_theme.tres"]  # Theme with HomeVideo font + frame StyleBox
[ext_resource path="scenes/ui/plant_info.gd"]
[ext_resource path="graphics/ui/v_bar.png"]      # Reused for both bars (tint colors differentiate them)

[node name="PlantInfo" type="PanelContainer"]
# PanelContainer: applies a background panel behind all children automatically
theme = game_theme.tres           # All children inherit font + panel styling from this theme
script = plant_info.gd            # setup(resource) wires up all UI to the resource

  [node name="HBoxContainer" parent="."]
  # Lays out icon (left) and text+bars (right) horizontally

    [node name="IconTexture" parent="HBoxContainer" type="TextureRect"]
    custom_minimum_size = Vector2(40, 0)  # 40px wide icon area
    texture = tomato.png          # Default — overridden by setup()
    stretch_mode = 5              # KeepAspectCentered — icon scales to fit while centered

    [node name="VBoxContainer" parent="HBoxContainer"]
    size_flags_horizontal = 3     # EXPAND — takes all remaining horizontal space after icon
    # Stacks NameLabel + GrowthBar + DeathBar vertically

      [node name="NameLabel" parent="HBoxContainer/VBoxContainer" type="Label"]
      text = "Tomato"             # Default text — overridden by setup()

      [node name="GrowthBar" parent="HBoxContainer/VBoxContainer" type="TextureProgressBar"]
      custom_minimum_size = Vector2(0, 6)   # 6px tall bar, width stretches to fill container
      nine_patch_stretch = true             # Bar texture stretches cleanly at any width
      texture_under = v_bar.png             # Same texture for background
      texture_progress = v_bar.png          # Same texture for fill (differentiated by tint)
      tint_under = Color(0.09, 0.09, 0.09)  # Dark gray background (almost black)
      tint_progress = Color(0.56, 0.84, 0.18) # Lime green — represents healthy growth

      [node name="DeathBar" parent="HBoxContainer/VBoxContainer" type="TextureProgressBar"]
      custom_minimum_size = Vector2(0, 6)
      nine_patch_stretch = true
      texture_under = v_bar.png
      texture_progress = v_bar.png
      tint_under = Color(0.09, 0.09, 0.09)      # Same dark gray background
      tint_progress = Color(0.78, 0.27, 0.11)   # Deep orange-red — represents neglect/danger
      # max_value set by setup() from res.death_max
      # value driven by setup() + update() from res.death_count via emit_changed signal
```

---

## scenes/ui/plant_info_container.tscn
> The scrollable sidebar that holds all plant panels. Covers the full left edge of the screen.

```
[gd_scene load_steps=2]

[ext_resource path="scenes/ui/plant_info_container.gd"]

[node name="PlantInfoContainer" type="Control"]
anchors_preset = 15 (FULL RECT)   # Stretches to cover the ENTIRE screen
# This seems large, but the children are constrained to the left edge
anchor_right = 1.0
anchor_bottom = 1.0
script = plant_info_container.gd  # Provides add() and update_all()

  [node name="MarginContainer" parent="."]
  custom_minimum_size = Vector2(200, 0)  # Panel is 200px wide
  anchors_preset = 9               # Preset 9 = LEFT SIDE (anchor_bottom=1.0 = full height)
  anchor_bottom = 1.0              # Stretches full height of screen
  grow_vertical = 2                # Grows upward and downward from anchor
  theme_override_constants/margin_left = 10  # 10px breathing room on left
  theme_override_constants/margin_top = 10   # 10px breathing room on top
  # Result: 200px wide strip on the left edge with inner padding

    [node name="ScrollContainer" parent="."]
    layout_mode = 2 (CONTAINER)    # Fills the MarginContainer
    # Enables scrolling when plant list exceeds screen height

      [node name="VBoxContainer" parent="ScrollContainer"]
      layout_mode = 2
      size_flags_horizontal = 3    # EXPAND — fills full 200px width
      size_flags_vertical = 3      # EXPAND — fills as much height as content needs
      # plant_info_container.gd.add() appends PlantInfo PanelContainers here
      # They stack vertically; ScrollContainer handles overflow
```

---

## scenes/levels/bed.tscn
> A simple StaticBody2D that the player can face and press Action to sleep.

```
[gd_scene]

[ext_resource path="scenes/levels/bed.gd"]
[ext_resource path="graphics/objects/bed.png"]

[sub_resource type="RectangleShape2D"]
size = Vector2(16, 16)            # One full tile — matches the bed sprite footprint

[node name="Bed" type="StaticBody2D"]
collision_layer = 12              # Binary 1100 = layers 3+4 (Objects + Characters)
# Layer 3 (Objects, value=4) + Layer 4 (Characters, value=8) = 12
# The player's RayCast2D detects layer 3 → can interact with this bed
collision_mask = 0                # Bed doesn't need to detect anything
script = bed.gd                   # Provides interact(player) → player.day_change_emit()

  [node name="Sprite2D" parent="."]
  texture = bed.png               # The bed graphic

  [node name="CollisionShape2D" parent="."]
  shape = RectangleShape2D (16×16)
```

---

## scenes/levels/tv.tscn
> A StaticBody2D with AnimatedSprite2D. Three animations: default (off), rain (clouds), sun.

```
[gd_scene]

[ext_resource path="scenes/levels/tv.gd"]
[ext_resource path="graphics/machines/tv.png"]  # TV sprite sheet with 5 frames horizontally

# AtlasTexture sub-resources slice tv.png horizontally into 16×32px regions
# Each AtlasTexture is one frame of one animation:
# Region (0,0,16,32)   = default (TV off)
# Region (16,0,16,32)  = sun frame 1
# Region (32,0,16,32)  = sun frame 2
# Region (48,0,16,32)  = rain frame 1
# Region (64,0,16,32)  = rain frame 2

[sub_resource type="SpriteFrames"]
animations:
  "default": [frame0], loop=true    # TV off — static single frame
  "rain":    [frame3, frame4], loop=true, speed=5.0  # Two-frame rain cloud animation
  "sun":     [frame1, frame2], loop=true, speed=5.0  # Two-frame sun animation

[sub_resource type="RectangleShape2D"]
size = Vector2(14, 12)            # Slightly narrower than one tile to feel accurate

[node name="TV" type="StaticBody2D"]
collision_layer = 12              # Layers 3+4 (same as Bed — interactable by RayCast)
collision_mask = 0
script = tv.gd                    # interact() plays the rain/sun animation for 3s

  [node name="AnimatedSprite2D" parent="."]
  sprite_frames = SpriteFrames    # Uses the three animations defined above
  autoplay = "default"            # Start with TV off

  [node name="CollisionShape2D" parent="."]
  position = Vector2(0, -4)       # Offset UP — collision sits around screen, not base
  shape = RectangleShape2D (14×12)

  [node name="Timer" parent="."]
  wait_time = 3.0                 # Show forecast for 3 seconds then return to "default"
  one_shot = true

[connection signal="timeout" from="Timer" to="." method="_on_timer_timeout"]
# After 3s → _on_timer_timeout() in tv.gd → play "default" animation again
```

---

## scenes/levels/house.tscn
> A Node2D containing 3 TileMapLayers (floor, walls, roof) plus TV and Bed inside.

```
[gd_scene format=4]

[ext_resource path="scenes/levels/house.gd"]
[ext_resource path="premade/HouseTileSet.tres"]        # Pre-made TileSet for the wall tiles
[ext_resource path="graphics/tilesets/walls_floor_tile.png"]  # Floor tile texture
[ext_resource path="graphics/tilesets/roof.png"]       # 6×6 grid of roof tiles
[ext_resource path="scenes/levels/tv.tscn"]
[ext_resource path="scenes/levels/bed.tscn"]
# Also: carpet, bookshelf, nightstand, table textures for decoration sprites

# Sub-resources: TileSetAtlasSource + TileSet for FloorLayer, separate TileSet for RoofLayer

[node name="House" type="Node2D"]
y_sort_enabled = true             # Objects inside house are Y-sorted (player walks behind furniture)
script = house.gd                 # Controls roof fade + door tile swap

  [node name="FloorLayer" type="TileMapLayer" parent="."]
  z_index = -2                    # Always behind everything
  tile_set = TileSet(walls_floor_tile.png)
  # tile_map_data NOT set here — house.gd._ready() fills it by copying WallsLayer cells

  [node name="WallsLayer" type="TileMapLayer" parent="."]
  y_sort_enabled = true           # Walls participate in Y-sort (player goes behind them)
  tile_map_data = PackedByteArray(...)  # Pre-painted wall layout (not editable in text)
  tile_set = HouseTileSet.tres    # Premade TileSet with full wall/corner/door tiles

  [node name="RoofLayer" type="TileMapLayer" parent="."]
  z_index = 2                     # Draws ON TOP of player and walls
  tile_map_data = PackedByteArray(...)  # Pre-painted roof layout
  tile_set = TileSet(roof.png)
  # house.gd tweens this layer's modulate.a (0=transparent when inside, 1=opaque when outside)

  [node name="HouseArea" type="Area2D" parent="."]
  collision_layer = 0             # Detector only — no physics body
  collision_mask = 2              # Bit 2 = layer 2 "Player" — detects only the player
    [CollisionPolygon2D]          # Custom polygon outlining the inside of the house

  [node name="TV" parent="." instance=tv.tscn]
  position = (inside house coords)

  [node name="Bed" parent="." instance=bed.tscn]
  position = (inside house coords)

  # Decoration sprites (StaticBody2D or Sprite2D):
  # Carpet, Bookshelf, Table, NightStand — visual only, some have collision shapes

[connection signal="body_entered" from="HouseArea" to="." method="_on_house_area_body_entered"]
[connection signal="body_exited"  from="HouseArea" to="." method="_on_house_area_body_exited"]
# Player enters/exits house area → in_house setter → roof fade + door tile change
```

---

## scenes/characters/player.tscn — AnimationTree detail

The AnimationTree in player.tscn is the most complex part. Here's what the sub-resources define:

```
BlendTree (root)
  ├── MoveStateMachine (AnimationNodeStateMachine)
  │     ├── Idle  → AnimationNodeBlendSpace2D with 9 points:
  │     │           (0,0)=idle_down  (1,0)=idle_right  (-1,0)=idle_left
  │     │           (0,-1)=idle_up   (0,1)=idle_down   diagonals=nearest cardinal
  │     └── Walk  → AnimationNodeBlendSpace2D with 9 points:
  │                 (0,0)=walk_down  (1,0)=walk_right  (-1,0)=walk_left
  │                 (0,-1)=walk_up   (0,1)=walk_down   diagonals=nearest cardinal
  │
  │    Transitions:
  │      Start → Idle   (auto=advance_mode=2, runs immediately at start)
  │      Idle  → Walk   (non-auto=advance_mode=0, must call travel("Walk"))
  │      Walk  → Idle   (non-auto=advance_mode=0, must call travel("Idle"))
  │
  ├── ToolOneShot (AnimationNodeOneShot)
  │     in  = MoveStateMachine output
  │     shot = ToolStateMachine
  │     Fires via: set("parameters/ToolOneShot/request", ONE_SHOT_REQUEST_FIRE)
  │
  └── ToolStateMachine (AnimationNodeStateMachine) — already set up in premade file
        Contains one BlendSpace2D per tool:
        Axe, Hoe, Water, Sword, Fish, Seed
        Each BlendSpace2D has 9 directional animation points (same layout as Walk/Idle)
```

**AnimationLibrary in player.tscn** — complete animation list:
```
Idle animations (loop_mode=1, 2-frame):
  idle_down, idle_left, idle_right, idle_up

Walk animations (loop_mode=1, 4-frame):
  walk_down, walk_left, walk_right, walk_up

Tool animations (loop_mode=0, 4-frame + method track at hit frame):
  axe_down,   axe_left,   axe_right,   axe_up
  hoe_down,   hoe_left,   hoe_right,   hoe_up
  water_down, water_left, water_right, water_up
  sword_down, sword_left, sword_right, sword_up
  seed_down,  seed_left,  seed_right,  seed_up

Fish animations (loop_mode=0, used for cast):
  fish_down, fish_left, fish_right, fish_up

Fish idle animations (loop_mode=1, holding the line):
  fish_idle_down, fish_idle_left, fish_idle_right, fish_idle_up
```

**Method track in every tool animation:**
```
At the exact "hit" keyframe time → calls tool_use_emit() on the root node (player)
This is why player.gd has func tool_use_emit() — it's called by the AnimationPlayer,
not by any GDScript code.
```

---

## Collision Layer Quick Reference

| Scene | collision_layer | collision_mask | Meaning |
|-------|----------------|----------------|---------|
| GrassLayer (TileMap) | 1 (Terrain) | — | Blocks player movement |
| Player CharacterBody2D | 2 (Player) | 1 (Terrain) | Player sees terrain |
| Plant StaticBody2D | 4 (Objects) | 0 | Other things can hit plant |
| Plant CollisionArea | 0 | 2 (Player) | Detects player for harvest |
| Tree StaticBody2D | 4 (Objects) | 0 | Hit by axe/sword range check |
| Blob CharacterBody2D | 4 (Objects) | 1 (Terrain) | Blob sees terrain for movement |
| SimpleObject StaticBody2D | 1 (Terrain) | 0 | Acts as terrain obstacle |
| Bed StaticBody2D | 12 (Obj+Char) | 0 | RayCast detects it |
| TV StaticBody2D | 12 (Obj+Char) | 0 | RayCast detects it |
| Machine StaticBody2D | 4 (Objects) | 0 | Hit by delete check |
| Projectile Area2D | 0 | 4 (Objects) | Detects blobs |
| HouseArea Area2D | 0 | 2 (Player) | Detects player entering house |

---

## scenes/levels/level.tscn
> The main game scene — root of everything that runs. 1310 lines; most are TileSet definitions.

### File structure overview
```
[gd_scene load_steps=30 format=4]
# format=4 = Godot 4.3+ binary-optimised text format
# load_steps=30 = 17 ext_resources + 12 sub_resources + 1 root node

--- External Resources ---
grass.png           → GrassLayer TileSet texture
level.gd            → Root script
water.png           → WaterLayer TileSet (4-frame animated)
player.tscn         → Player instance
soil.png            → SoilLayer TileSet
soil_water.png      → SoilWaterLayer TileSet (3 watered variants)
weather/floor.png   → RainFloorParticles texture
tree.tscn           → 31 tree instances
simple_object.tscn  → 37 bush/rock instances
circle_transition.gdshader → DayTransitionLayer shader
house.tscn          → 1 house instance
plant_info_container.tscn → UI sidebar
weather/drops.png   → RainDropsParticles texture
scare_crow.tscn     → 1 pre-placed scarecrow
icons/sprinkler.png → MachinePreviewSprite default texture
```

### Sub-resources defined inside level.tscn
```
[sub_resource type="Gradient"]
# The day/night colour gradient (4 stops):
# t=0.000 → Color(0.93, 0.86, 0.82) — dawn pinkish tint
# t=0.295 → Color(1,1,1)            — full daylight, no tint
# t=0.478 → Color(1,1,1)            — still daylight
# t=1.000 → Color(0.37, 0.47, 1.0)  — deep blue midnight tint
# level.gd samples this gradient at day_percent to drive DayTimeColor.color

[sub_resource type="TileSetAtlasSource" + TileSet for WaterLayer]
# water.png has animation_columns=4 (4 horizontal frames)
# Each frame duration = 0.4s → full cycle = 1.6s
# Only tile (0,0) is registered → the single animated water tile

[sub_resource type="TileSetAtlasSource" for GrassLayer — VERY LONG]
# ~750 lines defining every terrain tile in grass.png
# Each entry: column:row/0 = 0
# terrain_set=0, terrain=0 → all are the single "Grass" terrain
# physics_layer_0/polygon_0/points → custom collision polygon per tile
#   These are NOT full-square colliders — edge tiles have L-shaped or half-square polys
#   (this is how the player walks on the edge of the map)
# custom_data_0 = bool → marks which tiles are WALKABLE (true = full walk-through center tile)
# custom_data_1 = Vector2i → coast direction
#   Vector2i(0,0) = interior tile (no coast)
#   Vector2i(-1,0) = left coast (coast on left side, push player right)
#   Vector2i(1,0)  = right coast
#   Vector2i(0,-1) = top coast
#   Vector2i(0,1)  = bottom coast
# This is how level.gd knows which direction to push the player when swimming

[sub_resource type="ShaderMaterial" for DayTransitionLayer]
# Applies circle_transition.gdshader to the full-screen ColorRect
# shader_parameter/progress = 0.0  → circle is fully contracted (day is visible)
# This material is driven by level.gd's tween during day change

[sub_resource type="CanvasItemMaterial" for RainDropsParticles]
# light_mode = 0 (unshaded), blend_mode = 0 (mix) — standard particles

[sub_resource type="ParticleProcessMaterial" for RainDropsParticles]
# Rain particle configuration:
# particle_flag_disable_z = true     — 2D only
# emission_shape = 3 (Box)           — particles emit from a rectangular area
# emission_box_extents = (300,10,0)  — wide 600px box, 20px tall at top of screen
# direction = Vector3(0,1,0)         — falls straight down
# spread = 5.0                       — slight spread for natural look
# initial_velocity_min/max = 200,250 — fast downward rain
# gravity = Vector3(0,0,0)           — no extra gravity (velocity handles it)
# scale_min/max = 1.0,1.5            — slight size variation per drop
```

### Node tree
```
[node name="Level" type="Node2D"]
y_sort_enabled = true    # ALL children Y-sorted: player walks behind trees/house
script = level.gd

  [node name="Layers" type="Node2D" parent="."]
  # Organises all TileMapLayer nodes — no script, just a container

    [node name="WaterLayer" type="TileMapLayer" parent="Layers"]
    z_index = -3          # Deepest layer — always below everything
    y_sort_enabled = false
    tile_set = TileSet(water.png, 4-frame animation)
    tile_map_data = ...   # Painted lake/pond cells

    [node name="GrassLayer" type="TileMapLayer" parent="Layers"]
    z_index = -2          # Above water, below objects
    collision_layer = 1   # Layer 1 "Terrain" — player and blobs collide with this
    tile_set = TileSet(grass.png, full terrain)
    tile_map_data = ...   # The full map — grass + edge tiles

    [node name="SoilLayer" type="TileMapLayer" parent="Layers"]
    z_index = -1          # Above grass — soil patches are on top of grass
    tile_set = TileSet(soil.png, terrain)
    tile_map_data = ...   # Currently empty — filled at runtime by player hoeing

    [node name="SoilWaterLayer" type="TileMapLayer" parent="Layers"]
    z_index = -1          # Same level as SoilLayer — overwrites soil tile visually
    tile_set = TileSet(soil_water.png, 3 variants)
    tile_map_data = ...   # Empty — filled at runtime when player waters soil

    [node name="RainFloorParticles" type="GPUParticles2D" parent="Layers"]
    amount = 40           # 40 splash particles on ground
    emitting = false      # Off — enabled by level.gd when rain day starts
    texture = floor.png   # Splash/puddle texture
    process_material = ...  # Separate from drops — slower, falls at angle

  [node name="Objects" type="Node2D" parent="."]
  y_sort_enabled = true   # Objects within this group are Y-sorted against each other

    [node name="Player" parent="Objects" instance=player.tscn]
    position = Vector2(232, 340)  # Starting position near the farm area

    # 31 Tree instances (Tree through Tree31)
    # Each has a unique position spread around the map perimeter
    # Example:
    [node name="Tree" parent="Objects" instance=tree.tscn]
    position = Vector2(450, 200)  # Top-right forest area

    # 37 SimpleObject instances (SimpleObject through SimpleObject37)
    # Mix of bushes (style=0) and rocks (style=1), various sizes (0-3)
    # z_index=-1 on some = these objects are behind others despite Y-sort
    # Example:
    [node name="SimpleObject" parent="Objects" instance=simple_object.tscn]
    position = Vector2(67, 534)
    size = 2
    style = 1    # rock

    [node name="House" parent="Objects" instance=house.tscn]
    position = Vector2(232, 224)  # Upper-center of the map

    [node name="ScareCrow" parent="Objects" instance=scare_crow.tscn]
    position = Vector2(173, 389)  # Pre-placed in the field
    max_range = 150               # Override max_range export var to 150px

  [node name="Overlay" type="Node2D" parent="."]
  # Non-Y-sorted visual overlays — drawn in fixed order after all gameplay nodes

    [node name="DayTimeColor" type="CanvasModulate" parent="Overlay"]
    color = Color(0.994, 0.993, 1.0)  # Near-white = no tint at startup (morning)
    # level.gd updates this every frame by sampling the Gradient sub-resource
    # CanvasModulate multiplies this color with EVERY pixel on the canvas

    [node name="CanvasLayer" type="CanvasLayer" parent="Overlay"]
    # CanvasLayer = UI layer — ignores camera transform, always screen-space

      [node name="DayTransitionLayer" type="ColorRect" parent="Overlay/CanvasLayer"]
      anchors_preset = 15 (FULL RECT)  # Covers entire screen
      color = Color(0.024, 0.024, 0.024)  # Very dark grey/black
      material = ShaderMaterial(circle_transition.gdshader)
      # The shader cuts a circle hole in this black rect
      # At progress=0: circle is tiny → almost full black screen (transition start)
      # At progress=1: circle is huge → hole covers screen → transparent (day visible)
      # level.gd tweens progress 0→1 on new day

      [node name="PlantInfoContainer" parent="Overlay/CanvasLayer" instance=plant_info_container.tscn]
      # Left-side scrollable sidebar showing all active plants

    [node name="RainDropsParticles" type="GPUParticles2D" parent="Overlay"]
    position = Vector2(332, 412)  # Centered on typical player area
    emitting = false              # Off — enabled on rain days
    amount = 100                  # 100 rain drop particles
    texture = drops.png           # The raindrop sprite

    [node name="MachinePreviewSprite" type="Sprite2D" parent="Overlay"]
    texture = sprinkler.png       # Default preview icon (changes per machine type)
    # level.gd moves this sprite to follow the player when in machine-placement mode
    # offset is set per machine type (from MACHINE_PREVIEW_TEXTURES dict)

  [node name="Timers" type="Node" parent="."]
  # Pure container for timers — no script

    [node name="DayTimer" type="Timer" parent="Timers"]
    wait_time = 120.0  # One day = 2 minutes real time
    one_shot = true    # Fires once, then level.gd manually restarts it next day
    autostart = true   # Day starts counting immediately at game launch

    [node name="BlobTimer" type="Timer" parent="Timers"]
    wait_time = 20.0   # New blob spawns every 20 seconds
    autostart = true   # Loops — not one_shot — blobs keep spawning

  [node name="BlobSpawnPositions" type="Node2D" parent="."]
  # 11 Marker2D nodes around the map perimeter
  # All are off-screen or at the map edge so blobs appear to "arrive" from outside
  # level.gd picks a random one each time BlobTimer fires
  # Positions: (455,194), (575,212), (656,311), (687,409), (633,488),
  #            (595,570), (342,643), (33,641), (-43,482), (7,203), (292,185)

--- CONNECTIONS ---
[connection signal="build"          from="Objects/Player" to="." method="_on_player_build"]
# Player placed machine → level creates the scene at the tile position

[connection signal="day_change"     from="Objects/Player" to="." method="_on_player_day_change"]
# Player slept in bed → level triggers day transition tween + grows plants

[connection signal="diagnose"       from="Objects/Player" to="." method="_on_player_diagnose"]
# Debug key → level prints FPS/memory stats to output

[connection signal="machine_change" from="Objects/Player" to="." method="_on_player_machine_change"]
# Player pressed machine hotkey → level switches MachinePreviewSprite texture

[connection signal="tool_use"       from="Objects/Player" to="." method="_on_player_tool_use"]
# Player used tool (axe/hoe/water/etc.) → level handles the world-side effect

[connection signal="timeout"        from="Timers/BlobTimer" to="." method="_on_blob_timer_timeout"]
# 20s elapsed → spawn a new blob at a random BlobSpawnPosition
```

### TileSet custom data layers (grass.png TileSet)
```
custom_data_0  (bool)      = "walkable"
  true  → tile center is fully passable (interior grass)
  false → tile has collision polygon (edge tile)

custom_data_1  (Vector2i)  = "coast_direction"
  Vector2i( 0,  0) → no coast (interior tile)
  Vector2i(-1,  0) → coast faces LEFT  (player pushed right when swimming)
  Vector2i( 1,  0) → coast faces RIGHT
  Vector2i( 0, -1) → coast faces UP
  Vector2i( 0,  1) → coast faces DOWN
```

---

## resources/tomato_res.tres
> The only plant resource file included in the project. Shows the expected .tres format.
> The other 3 plants (corn, pumpkin, wheat) use the same format — only texture differs.

```
[gd_resource type="Resource" script_class="PlantResource" load_steps=3 format=3]
# type="Resource" because PlantResource extends Resource (not Node)
# script_class="PlantResource" — lets Godot show it in the "Create New Resource" dialog

[ext_resource path="res://resources/plant_res.gd"]   # The PlantResource script
[ext_resource path="res://graphics/plants/tomato.png"] # The plant's growth stage sprite

[resource]
script = plant_res.gd             # Attach the PlantResource class to this resource
texture = tomato.png              # The sprite used for all 4 growth frames (hframes=4)
metadata/_custom_type_script = uid://...  # Editor metadata — Godot auto-adds this
# All other PlantResource fields (grow_speed, death_max, sell_amount, seed_enum,
# h_frames, name, icon) are left at their script defaults.
# They must be filled in the Godot Inspector after creating each .tres file.
```

**How to create the other 3 plant resources:**
```
File Inspector settings per plant:
┌──────────┬────────────────────────────────┬───────────┬───────────────┬─────────────────────────────┬─────────┬──────────────┬──────────┐
│  File    │ texture                        │grow_speed │  death_max    │       sell_amount           │  seed   │   h_frames   │  name    │
├──────────┼────────────────────────────────┼───────────┼───────────────┼─────────────────────────────┼─────────┼──────────────┼──────────┤
│tomato    │ graphics/plants/tomato.png     │   1.5     │      50       │            3                │ TOMATO  │      4       │ Tomato   │
│corn      │ graphics/plants/corn.png       │   1.0     │      40       │            4                │ CORN    │      4       │ Corn     │
│pumpkin   │ graphics/plants/pumpkin.png    │   0.5     │      70       │            6                │ PUMPKIN │      4       │ Pumpkin  │
│wheat     │ graphics/plants/wheat.png      │   2.0     │      30       │            2                │ WHEAT   │      4       │ Wheat    │
└──────────┴────────────────────────────────┴───────────┴───────────────┴─────────────────────────────┴─────────┴──────────────┴──────────┘
```

---

## scenes/ui/game_theme.tres
> The single Theme resource that controls all UI fonts and panel backgrounds.

```
[gd_resource type="Theme" format=3]

[ext_resource path="graphics/fonts/HomeVideo-Regular.ttf"]
# The chunky pixel-style font used for all Labels in the game

[ext_resource path="graphics/ui/frame.png"]
# The 9-patch background for PanelContainer nodes (plant info panels)

[sub_resource type="FontVariation"]
base_font = HomeVideo-Regular.ttf
spacing_glyph = 1    # Add 1px extra space between characters — improves readability at small sizes

[sub_resource type="StyleBoxTexture"]
texture = frame.png
texture_margin_left   = 6.0  # 9-patch margins: 6px on all sides
texture_margin_top    = 6.0  # This means the 6px border corners never stretch
texture_margin_right  = 6.0  # Only the inner area of frame.png stretches
texture_margin_bottom = 6.0

[resource]
# These are theme overrides applied globally to all nodes using this theme:
Label/colors/font_color  = Color(0.023, 0.023, 0.023)  # Very dark (near-black) text
Label/font_sizes/font_size = 30                         # Large font — readable at pixel scale
Label/fonts/font          = FontVariation               # Use the HomeVideo font
PanelContainer/styles/panel = StyleBoxTexture           # Panels use the frame.png 9-patch
```

---

## premade/code_snippets.txt
> Paste-ready constant/variable declarations. Copy into the matching scripts during setup.

```
# ---- PASTE INTO: scenes/levels/level.gd ----

# Machine preview icons — shown when player is in machine-placement mode
# Key = Enum.Machine value, Value = { texture, offset }
const MACHINE_PREVIEW_TEXTURES = {
    Enum.Machine.SPRINKLER: {'texture': preload("res://graphics/icons/sprinkler.png"), 'offset': Vector2i(0,  0)},
    Enum.Machine.FISHER:    {'texture': preload("res://graphics/icons/fisher.png"),    'offset': Vector2i(0, -4)},
    Enum.Machine.SCARECROW: {'texture': preload("res://graphics/icons/scarecrow.png"), 'offset': Vector2i(0, -4)},
    Enum.Machine.DELETE:    {'texture': preload("res://graphics/icons/delete.png"),    'offset': Vector2i(0,  0)}
}
# offset = pixel offset so the preview icon is centered over the tile center

# Machine scene preloads — used when player confirms placement
var machine_scenes = {
    Enum.Machine.SPRINKLER: preload("res://scenes/machines/sprinkler.tscn"),
    Enum.Machine.FISHER:    preload("res://scenes/machines/fisher.tscn"),
    Enum.Machine.SCARECROW: preload("res://scenes/machines/scare_crow.tscn")
}
# NOTE: DELETE is not here — DELETE mode removes existing machines, doesn't place new ones

# ---- PASTE INTO: global/data.gd (or level.gd player-init section) ----

# Starting seed inventory — adjust amounts to balance difficulty
var seed_amount = {
    Enum.Seed.CORN:    10,
    Enum.Seed.TOMATO:  20,
    Enum.Seed.PUMPKIN: 14,
    Enum.Seed.WHEAT:    4
}

# Starting item inventory
var items = {
    Enum.Item.WOOD:    1,
    Enum.Item.APPLE:   3,
    Enum.Item.FISH:    4,
    Enum.Item.CORN:    0,
    Enum.Item.WHEAT:   0,
    Enum.Item.PUMPKIN: 0,
    Enum.Item.TOMATO:  0
}

# ---- PASTE INTO: scenes/ui/tool_ui.gd ----

# Tool icon textures — used by tool_ui.gd.setup() to populate the tool bar
const TOOL_TEXTURES = {
    Enum.Tool.AXE:   preload("res://graphics/icons/axe.png"),
    Enum.Tool.HOE:   preload("res://graphics/icons/hoe.png"),
    Enum.Tool.WATER: preload("res://graphics/icons/water.png"),
    Enum.Tool.SWORD: preload("res://graphics/icons/sword.png"),
    Enum.Tool.FISH:  preload("res://graphics/icons/fish.png"),
    Enum.Tool.SEED:  preload("res://graphics/icons/wheat.png")
}

# Seed icon textures — used by tool_ui.gd.setup() to populate the seed bar
const SEED_TEXTURES = {
    Enum.Seed.CORN:    preload("res://graphics/icons/corn.png"),
    Enum.Seed.PUMPKIN: preload("res://graphics/icons/pumpkin.png"),
    Enum.Seed.TOMATO:  preload("res://graphics/icons/tomato.png"),
    Enum.Seed.WHEAT:   preload("res://graphics/icons/wheat.png")
}

# ---- PASTE INTO: scenes/levels/level.gd (watering logic) ----

# The 8 tile directions around a soil tile
# Used by the sprinkler to find all neighbouring soil tiles to water
const SOIL_DIRECTIONS = [
    Vector2i(-1, -1), Vector2i( 0, -1), Vector2i(1, -1),
    Vector2i(-1,  0),                   Vector2i(1,  0),
    Vector2i(-1,  1), Vector2i( 0,  1), Vector2i(1,  1)
]
# Note: center (0,0) is NOT included — only the 8 surrounding tiles
```

---

## premade/HouseTileSet.tscn
> A simple viewer scene for HouseTileSet.tres. Not used at runtime — editor reference only.

```
[gd_scene load_steps=2]

[ext_resource path="premade/HouseTileSet.tres"]   # The full house TileSet resource

[node name="HouseTileSet" type="Node2D"]
# Empty Node2D root — this scene has no logic

  [node name="TileMapLayer" parent="."]
  tile_set = HouseTileSet.tres
  # Empty TileMapLayer — just mounts the tileset so you can view it in the editor
  # To browse tiles: open this scene → select TileMapLayer → open TileMap panel
```
