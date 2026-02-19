<span id="class_SpriteFrames"></span>

## SpriteFrames

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Sprite frame library for AnimatedSprite2D and AnimatedSprite3D.

### Description

Sprite frame library for an [AnimatedSprite2D](class_animatedsprite2d.md#class_AnimatedSprite2D) or [AnimatedSprite3D](class_animatedsprite3d.md#class_AnimatedSprite3D) node. Contains frames and animation data for playback.

### Methods


| void | [add_animation](class_spriteframes.md#class_SpriteFrames_method_add_animation) ( anim: [StringName](class_stringname.md#class_StringName) ) |
| --- | --- |
| void | [add_frame](class_spriteframes.md#class_SpriteFrames_method_add_frame) ( anim: [StringName](class_stringname.md#class_StringName), texture: [Texture2D](class_texture2d.md#class_Texture2D), duration: [float](class_float.md#class_float) = 1.0, at_position: [int](class_int.md#class_int) = -1 ) |
| void | [clear](class_spriteframes.md#class_SpriteFrames_method_clear) ( anim: [StringName](class_stringname.md#class_StringName) ) |
| void | [clear_all](class_spriteframes.md#class_SpriteFrames_method_clear_all) ( ) |
| void | [duplicate_animation](class_spriteframes.md#class_SpriteFrames_method_duplicate_animation) ( anim_from: [StringName](class_stringname.md#class_StringName), anim_to: [StringName](class_stringname.md#class_StringName) ) |
| [bool](class_bool.md#class_bool) | [get_animation_loop](class_spriteframes.md#class_SpriteFrames_method_get_animation_loop) ( anim: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_animation_names](class_spriteframes.md#class_SpriteFrames_method_get_animation_names) ( ) const |
| [float](class_float.md#class_float) | [get_animation_speed](class_spriteframes.md#class_SpriteFrames_method_get_animation_speed) ( anim: [StringName](class_stringname.md#class_StringName) ) const |
| [int](class_int.md#class_int) | [get_frame_count](class_spriteframes.md#class_SpriteFrames_method_get_frame_count) ( anim: [StringName](class_stringname.md#class_StringName) ) const |
| [float](class_float.md#class_float) | [get_frame_duration](class_spriteframes.md#class_SpriteFrames_method_get_frame_duration) ( anim: [StringName](class_stringname.md#class_StringName), idx: [int](class_int.md#class_int) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_frame_texture](class_spriteframes.md#class_SpriteFrames_method_get_frame_texture) ( anim: [StringName](class_stringname.md#class_StringName), idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has_animation](class_spriteframes.md#class_SpriteFrames_method_has_animation) ( anim: [StringName](class_stringname.md#class_StringName) ) const |
| void | [remove_animation](class_spriteframes.md#class_SpriteFrames_method_remove_animation) ( anim: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_frame](class_spriteframes.md#class_SpriteFrames_method_remove_frame) ( anim: [StringName](class_stringname.md#class_StringName), idx: [int](class_int.md#class_int) ) |
| void | [rename_animation](class_spriteframes.md#class_SpriteFrames_method_rename_animation) ( anim: [StringName](class_stringname.md#class_StringName), newname: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_animation_loop](class_spriteframes.md#class_SpriteFrames_method_set_animation_loop) ( anim: [StringName](class_stringname.md#class_StringName), loop: [bool](class_bool.md#class_bool) ) |
| void | [set_animation_speed](class_spriteframes.md#class_SpriteFrames_method_set_animation_speed) ( anim: [StringName](class_stringname.md#class_StringName), fps: [float](class_float.md#class_float) ) |
| void | [set_frame](class_spriteframes.md#class_SpriteFrames_method_set_frame) ( anim: [StringName](class_stringname.md#class_StringName), idx: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D), duration: [float](class_float.md#class_float) = 1.0 ) |

---

### Method Descriptions

<span id="class_SpriteFrames_method_add_animation"></span>

void **add_animation** ( anim: [StringName](class_stringname.md#class_StringName) ) [🔗](class_spriteframes.md#class_SpriteFrames_method_add_animation)

Adds a new `anim` animation to the library.

---

<span id="class_SpriteFrames_method_add_frame"></span>

void **add_frame** ( anim: [StringName](class_stringname.md#class_StringName), texture: [Texture2D](class_texture2d.md#class_Texture2D), duration: [float](class_float.md#class_float) = 1.0, at_position: [int](class_int.md#class_int) = -1 ) [🔗](class_spriteframes.md#class_SpriteFrames_method_add_frame)

Adds a frame to the `anim` animation. If `at_position` is `-1`, the frame will be added to the end of the animation. `duration` specifies the relative duration, see [get_frame_duration()](class_spriteframes.md#class_SpriteFrames_method_get_frame_duration) for details.

---

<span id="class_SpriteFrames_method_clear"></span>

void **clear** ( anim: [StringName](class_stringname.md#class_StringName) ) [🔗](class_spriteframes.md#class_SpriteFrames_method_clear)

Removes all frames from the `anim` animation.

---

<span id="class_SpriteFrames_method_clear_all"></span>

void **clear_all** ( ) [🔗](class_spriteframes.md#class_SpriteFrames_method_clear_all)

Removes all animations. An empty `default` animation will be created.

---

<span id="class_SpriteFrames_method_duplicate_animation"></span>

void **duplicate_animation** ( anim_from: [StringName](class_stringname.md#class_StringName), anim_to: [StringName](class_stringname.md#class_StringName) ) [🔗](class_spriteframes.md#class_SpriteFrames_method_duplicate_animation)

Duplicates the animation `anim_from` to a new animation named `anim_to`. Fails if `anim_to` already exists, or if `anim_from` does not exist.

---

<span id="class_SpriteFrames_method_get_animation_loop"></span>

[bool](class_bool.md#class_bool) **get_animation_loop** ( anim: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_spriteframes.md#class_SpriteFrames_method_get_animation_loop)

Returns `true` if the given animation is configured to loop when it finishes playing. Otherwise, returns `false`.

---

<span id="class_SpriteFrames_method_get_animation_names"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_animation_names** ( ) *const* [🔗](class_spriteframes.md#class_SpriteFrames_method_get_animation_names)

Returns an array containing the names associated to each animation. Values are placed in alphabetical order.

---

<span id="class_SpriteFrames_method_get_animation_speed"></span>

[float](class_float.md#class_float) **get_animation_speed** ( anim: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_spriteframes.md#class_SpriteFrames_method_get_animation_speed)

Returns the speed in frames per second for the `anim` animation.

---

<span id="class_SpriteFrames_method_get_frame_count"></span>

[int](class_int.md#class_int) **get_frame_count** ( anim: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_spriteframes.md#class_SpriteFrames_method_get_frame_count)

Returns the number of frames for the `anim` animation.

---

<span id="class_SpriteFrames_method_get_frame_duration"></span>

[float](class_float.md#class_float) **get_frame_duration** ( anim: [StringName](class_stringname.md#class_StringName), idx: [int](class_int.md#class_int) ) *const* [🔗](class_spriteframes.md#class_SpriteFrames_method_get_frame_duration)

Returns a relative duration of the frame `idx` in the `anim` animation (defaults to `1.0`). For example, a frame with a duration of `2.0` is displayed twice as long as a frame with a duration of `1.0`. You can calculate the absolute duration (in seconds) of a frame using the following formula:

::

    absolute_duration = relative_duration / (animation_fps * abs(playing_speed))

In this example, `playing_speed` refers to either [AnimatedSprite2D.get_playing_speed()](class_animatedsprite2d.md#class_AnimatedSprite2D_method_get_playing_speed) or [AnimatedSprite3D.get_playing_speed()](class_animatedsprite3d.md#class_AnimatedSprite3D_method_get_playing_speed).

---

<span id="class_SpriteFrames_method_get_frame_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_frame_texture** ( anim: [StringName](class_stringname.md#class_StringName), idx: [int](class_int.md#class_int) ) *const* [🔗](class_spriteframes.md#class_SpriteFrames_method_get_frame_texture)

Returns the texture of the frame `idx` in the `anim` animation.

---

<span id="class_SpriteFrames_method_has_animation"></span>

[bool](class_bool.md#class_bool) **has_animation** ( anim: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_spriteframes.md#class_SpriteFrames_method_has_animation)

Returns `true` if the `anim` animation exists.

---

<span id="class_SpriteFrames_method_remove_animation"></span>

void **remove_animation** ( anim: [StringName](class_stringname.md#class_StringName) ) [🔗](class_spriteframes.md#class_SpriteFrames_method_remove_animation)

Removes the `anim` animation.

---

<span id="class_SpriteFrames_method_remove_frame"></span>

void **remove_frame** ( anim: [StringName](class_stringname.md#class_StringName), idx: [int](class_int.md#class_int) ) [🔗](class_spriteframes.md#class_SpriteFrames_method_remove_frame)

Removes the `anim` animation's frame `idx`.

---

<span id="class_SpriteFrames_method_rename_animation"></span>

void **rename_animation** ( anim: [StringName](class_stringname.md#class_StringName), newname: [StringName](class_stringname.md#class_StringName) ) [🔗](class_spriteframes.md#class_SpriteFrames_method_rename_animation)

Changes the `anim` animation's name to `newname`.

---

<span id="class_SpriteFrames_method_set_animation_loop"></span>

void **set_animation_loop** ( anim: [StringName](class_stringname.md#class_StringName), loop: [bool](class_bool.md#class_bool) ) [🔗](class_spriteframes.md#class_SpriteFrames_method_set_animation_loop)

If `loop` is `true`, the `anim` animation will loop when it reaches the end, or the start if it is played in reverse.

---

<span id="class_SpriteFrames_method_set_animation_speed"></span>

void **set_animation_speed** ( anim: [StringName](class_stringname.md#class_StringName), fps: [float](class_float.md#class_float) ) [🔗](class_spriteframes.md#class_SpriteFrames_method_set_animation_speed)

Sets the speed for the `anim` animation in frames per second.

---

<span id="class_SpriteFrames_method_set_frame"></span>

void **set_frame** ( anim: [StringName](class_stringname.md#class_StringName), idx: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D), duration: [float](class_float.md#class_float) = 1.0 ) [🔗](class_spriteframes.md#class_SpriteFrames_method_set_frame)

Sets the `texture` and the `duration` of the frame `idx` in the `anim` animation. `duration` specifies the relative duration, see [get_frame_duration()](class_spriteframes.md#class_SpriteFrames_method_get_frame_duration) for details.
