<span id="class_Animation"></span>

## Animation

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Holds data that can be used to animate anything in the engine.

### Description

This resource holds data that can be used to animate anything in the engine. Animations are divided into tracks and each track must be linked to a node. The state of that node can be changed through time, by adding timed keys (events) to the track.

.. tabs::

```
```

    # This creates an animation that makes the node "Enemy" move to the right by
    # 100 pixels in 2.0 seconds.
    var animation = Animation.new()
    var track_index = animation.add_track(Animation.TYPE_VALUE)
    animation.track_set_path(track_index, "Enemy:position:x")
    animation.track_insert_key(track_index, 0.0, 0)
    animation.track_insert_key(track_index, 2.0, 100)
    animation.length = 2.0

```
```

    // This creates an animation that makes the node "Enemy" move to the right by
    // 100 pixels in 2.0 seconds.
    var animation = new Animation();
    int trackIndex = animation.AddTrack(Animation.TrackType.Value);
    animation.TrackSetPath(trackIndex, "Enemy:position:x");
    animation.TrackInsertKey(trackIndex, 0.0f, 0);
    animation.TrackInsertKey(trackIndex, 2.0f, 100);
    animation.Length = 2.0f;

Animations are just data containers, and must be added to nodes such as an [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer) to be played back. Animation tracks have different types, each with its own set of dedicated methods. Check [TrackType](class_animation.md#enum_Animation_TrackType) to see available types.

 **Note:** For 3D position/rotation/scale, using the dedicated [TYPE_POSITION_3D](class_animation.md#class_Animation_constant_TYPE_POSITION_3D), [TYPE_ROTATION_3D](class_animation.md#class_Animation_constant_TYPE_ROTATION_3D) and [TYPE_SCALE_3D](class_animation.md#class_Animation_constant_TYPE_SCALE_3D) track types instead of [TYPE_VALUE](class_animation.md#class_Animation_constant_TYPE_VALUE) is recommended for performance reasons.

### Tutorials

- [Animation documentation index](../tutorials/animation/index.md)

### Properties


| [bool](class_bool.md#class_bool) | [capture_included](class_animation.md#class_Animation_property_capture_included) | `false` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [length](class_animation.md#class_Animation_property_length) | `1.0` |
| [LoopMode](class_animation.md#enum_Animation_LoopMode) | [loop_mode](class_animation.md#class_Animation_property_loop_mode) | `0` |
| [float](class_float.md#class_float) | [step](class_animation.md#class_Animation_property_step) | `0.033333335` |

### Methods


| void | [add_marker](class_animation.md#class_Animation_method_add_marker) ( name: [StringName](class_stringname.md#class_StringName), time: [float](class_float.md#class_float) ) |
| --- | --- |
| [int](class_int.md#class_int) | [add_track](class_animation.md#class_Animation_method_add_track) ( type: [TrackType](class_animation.md#enum_Animation_TrackType), at_position: [int](class_int.md#class_int) = -1 ) |
| [StringName](class_stringname.md#class_StringName) | [animation_track_get_key_animation](class_animation.md#class_Animation_method_animation_track_get_key_animation) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [animation_track_insert_key](class_animation.md#class_Animation_method_animation_track_insert_key) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), animation: [StringName](class_stringname.md#class_StringName) ) |
| void | [animation_track_set_key_animation](class_animation.md#class_Animation_method_animation_track_set_key_animation) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), animation: [StringName](class_stringname.md#class_StringName) ) |
| [float](class_float.md#class_float) | [audio_track_get_key_end_offset](class_animation.md#class_Animation_method_audio_track_get_key_end_offset) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [audio_track_get_key_start_offset](class_animation.md#class_Animation_method_audio_track_get_key_start_offset) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [Resource](class_resource.md#class_Resource) | [audio_track_get_key_stream](class_animation.md#class_Animation_method_audio_track_get_key_stream) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [audio_track_insert_key](class_animation.md#class_Animation_method_audio_track_insert_key) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), stream: [Resource](class_resource.md#class_Resource), start_offset: [float](class_float.md#class_float) = 0, end_offset: [float](class_float.md#class_float) = 0 ) |
| [bool](class_bool.md#class_bool) | [audio_track_is_use_blend](class_animation.md#class_Animation_method_audio_track_is_use_blend) ( track_idx: [int](class_int.md#class_int) ) const |
| void | [audio_track_set_key_end_offset](class_animation.md#class_Animation_method_audio_track_set_key_end_offset) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), offset: [float](class_float.md#class_float) ) |
| void | [audio_track_set_key_start_offset](class_animation.md#class_Animation_method_audio_track_set_key_start_offset) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), offset: [float](class_float.md#class_float) ) |
| void | [audio_track_set_key_stream](class_animation.md#class_Animation_method_audio_track_set_key_stream) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), stream: [Resource](class_resource.md#class_Resource) ) |
| void | [audio_track_set_use_blend](class_animation.md#class_Animation_method_audio_track_set_use_blend) ( track_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| [Vector2](class_vector2.md#class_Vector2) | [bezier_track_get_key_in_handle](class_animation.md#class_Animation_method_bezier_track_get_key_in_handle) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [bezier_track_get_key_out_handle](class_animation.md#class_Animation_method_bezier_track_get_key_out_handle) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [bezier_track_get_key_value](class_animation.md#class_Animation_method_bezier_track_get_key_value) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [bezier_track_insert_key](class_animation.md#class_Animation_method_bezier_track_insert_key) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), value: [float](class_float.md#class_float), in_handle: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0), out_handle: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| [float](class_float.md#class_float) | [bezier_track_interpolate](class_animation.md#class_Animation_method_bezier_track_interpolate) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float) ) const |
| void | [bezier_track_set_key_in_handle](class_animation.md#class_Animation_method_bezier_track_set_key_in_handle) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), in_handle: [Vector2](class_vector2.md#class_Vector2), balanced_value_time_ratio: [float](class_float.md#class_float) = 1.0 ) |
| void | [bezier_track_set_key_out_handle](class_animation.md#class_Animation_method_bezier_track_set_key_out_handle) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), out_handle: [Vector2](class_vector2.md#class_Vector2), balanced_value_time_ratio: [float](class_float.md#class_float) = 1.0 ) |
| void | [bezier_track_set_key_value](class_animation.md#class_Animation_method_bezier_track_set_key_value) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | [blend_shape_track_insert_key](class_animation.md#class_Animation_method_blend_shape_track_insert_key) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), amount: [float](class_float.md#class_float) ) |
| [float](class_float.md#class_float) | [blend_shape_track_interpolate](class_animation.md#class_Animation_method_blend_shape_track_interpolate) ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) const |
| void | [clear](class_animation.md#class_Animation_method_clear) ( ) |
| void | [compress](class_animation.md#class_Animation_method_compress) ( page_size: [int](class_int.md#class_int) = 8192, fps: [int](class_int.md#class_int) = 120, split_tolerance: [float](class_float.md#class_float) = 4.0 ) |
| void | [copy_track](class_animation.md#class_Animation_method_copy_track) ( track_idx: [int](class_int.md#class_int), to_animation: [Animation](class_animation.md#class_Animation) ) |
| [int](class_int.md#class_int) | [find_track](class_animation.md#class_Animation_method_find_track) ( path: [NodePath](class_nodepath.md#class_NodePath), type: [TrackType](class_animation.md#enum_Animation_TrackType) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_marker_at_time](class_animation.md#class_Animation_method_get_marker_at_time) ( time: [float](class_float.md#class_float) ) const |
| [Color](class_color.md#class_Color) | [get_marker_color](class_animation.md#class_Animation_method_get_marker_color) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_marker_names](class_animation.md#class_Animation_method_get_marker_names) ( ) const |
| [float](class_float.md#class_float) | [get_marker_time](class_animation.md#class_Animation_method_get_marker_time) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_next_marker](class_animation.md#class_Animation_method_get_next_marker) ( time: [float](class_float.md#class_float) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_prev_marker](class_animation.md#class_Animation_method_get_prev_marker) ( time: [float](class_float.md#class_float) ) const |
| [int](class_int.md#class_int) | [get_track_count](class_animation.md#class_Animation_method_get_track_count) ( ) const |
| [bool](class_bool.md#class_bool) | [has_marker](class_animation.md#class_Animation_method_has_marker) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [StringName](class_stringname.md#class_StringName) | [method_track_get_name](class_animation.md#class_Animation_method_method_track_get_name) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array) | [method_track_get_params](class_animation.md#class_Animation_method_method_track_get_params) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| void | [optimize](class_animation.md#class_Animation_method_optimize) ( allowed_velocity_err: [float](class_float.md#class_float) = 0.01, allowed_angular_err: [float](class_float.md#class_float) = 0.01, precision: [int](class_int.md#class_int) = 3 ) |
| [int](class_int.md#class_int) | [position_track_insert_key](class_animation.md#class_Animation_method_position_track_insert_key) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), position: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3](class_vector3.md#class_Vector3) | [position_track_interpolate](class_animation.md#class_Animation_method_position_track_interpolate) ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) const |
| void | [remove_marker](class_animation.md#class_Animation_method_remove_marker) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_track](class_animation.md#class_Animation_method_remove_track) ( track_idx: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [rotation_track_insert_key](class_animation.md#class_Animation_method_rotation_track_insert_key) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), rotation: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [rotation_track_interpolate](class_animation.md#class_Animation_method_rotation_track_interpolate) ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) const |
| [int](class_int.md#class_int) | [scale_track_insert_key](class_animation.md#class_Animation_method_scale_track_insert_key) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), scale: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3](class_vector3.md#class_Vector3) | [scale_track_interpolate](class_animation.md#class_Animation_method_scale_track_interpolate) ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) const |
| void | [set_marker_color](class_animation.md#class_Animation_method_set_marker_color) ( name: [StringName](class_stringname.md#class_StringName), color: [Color](class_color.md#class_Color) ) |
| [int](class_int.md#class_int) | [track_find_key](class_animation.md#class_Animation_method_track_find_key) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), find_mode: [FindMode](class_animation.md#enum_Animation_FindMode) = 0, limit: [bool](class_bool.md#class_bool) = false, backward: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [track_get_interpolation_loop_wrap](class_animation.md#class_Animation_method_track_get_interpolation_loop_wrap) ( track_idx: [int](class_int.md#class_int) ) const |
| [InterpolationType](class_animation.md#enum_Animation_InterpolationType) | [track_get_interpolation_type](class_animation.md#class_Animation_method_track_get_interpolation_type) ( track_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [track_get_key_count](class_animation.md#class_Animation_method_track_get_key_count) ( track_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [track_get_key_time](class_animation.md#class_Animation_method_track_get_key_time) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [track_get_key_transition](class_animation.md#class_Animation_method_track_get_key_transition) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [track_get_key_value](class_animation.md#class_Animation_method_track_get_key_value) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [track_get_path](class_animation.md#class_Animation_method_track_get_path) ( track_idx: [int](class_int.md#class_int) ) const |
| [TrackType](class_animation.md#enum_Animation_TrackType) | [track_get_type](class_animation.md#class_Animation_method_track_get_type) ( track_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [track_insert_key](class_animation.md#class_Animation_method_track_insert_key) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), key: [Variant](class_variant.md#class_Variant), transition: [float](class_float.md#class_float) = 1 ) |
| [bool](class_bool.md#class_bool) | [track_is_compressed](class_animation.md#class_Animation_method_track_is_compressed) ( track_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [track_is_enabled](class_animation.md#class_Animation_method_track_is_enabled) ( track_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [track_is_imported](class_animation.md#class_Animation_method_track_is_imported) ( track_idx: [int](class_int.md#class_int) ) const |
| void | [track_move_down](class_animation.md#class_Animation_method_track_move_down) ( track_idx: [int](class_int.md#class_int) ) |
| void | [track_move_to](class_animation.md#class_Animation_method_track_move_to) ( track_idx: [int](class_int.md#class_int), to_idx: [int](class_int.md#class_int) ) |
| void | [track_move_up](class_animation.md#class_Animation_method_track_move_up) ( track_idx: [int](class_int.md#class_int) ) |
| void | [track_remove_key](class_animation.md#class_Animation_method_track_remove_key) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) |
| void | [track_remove_key_at_time](class_animation.md#class_Animation_method_track_remove_key_at_time) ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float) ) |
| void | [track_set_enabled](class_animation.md#class_Animation_method_track_set_enabled) ( track_idx: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [track_set_imported](class_animation.md#class_Animation_method_track_set_imported) ( track_idx: [int](class_int.md#class_int), imported: [bool](class_bool.md#class_bool) ) |
| void | [track_set_interpolation_loop_wrap](class_animation.md#class_Animation_method_track_set_interpolation_loop_wrap) ( track_idx: [int](class_int.md#class_int), interpolation: [bool](class_bool.md#class_bool) ) |
| void | [track_set_interpolation_type](class_animation.md#class_Animation_method_track_set_interpolation_type) ( track_idx: [int](class_int.md#class_int), interpolation: [InterpolationType](class_animation.md#enum_Animation_InterpolationType) ) |
| void | [track_set_key_time](class_animation.md#class_Animation_method_track_set_key_time) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float) ) |
| void | [track_set_key_transition](class_animation.md#class_Animation_method_track_set_key_transition) ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), transition: [float](class_float.md#class_float) ) |
| void | [track_set_key_value](class_animation.md#class_Animation_method_track_set_key_value) ( track_idx: [int](class_int.md#class_int), key: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant) ) |
| void | [track_set_path](class_animation.md#class_Animation_method_track_set_path) ( track_idx: [int](class_int.md#class_int), path: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [track_swap](class_animation.md#class_Animation_method_track_swap) ( track_idx: [int](class_int.md#class_int), with_idx: [int](class_int.md#class_int) ) |
| [UpdateMode](class_animation.md#enum_Animation_UpdateMode) | [value_track_get_update_mode](class_animation.md#class_Animation_method_value_track_get_update_mode) ( track_idx: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [value_track_interpolate](class_animation.md#class_Animation_method_value_track_interpolate) ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) const |
| void | [value_track_set_update_mode](class_animation.md#class_Animation_method_value_track_set_update_mode) ( track_idx: [int](class_int.md#class_int), mode: [UpdateMode](class_animation.md#enum_Animation_UpdateMode) ) |

---

### Enumerations

<span id="enum_Animation_TrackType"></span>

enum **TrackType**: [🔗](class_animation.md#enum_Animation_TrackType)

<span id="class_Animation_constant_TYPE_VALUE"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **TYPE_VALUE** = `0`

Value tracks set values in node properties, but only those which can be interpolated. For 3D position/rotation/scale, using the dedicated [TYPE_POSITION_3D](class_animation.md#class_Animation_constant_TYPE_POSITION_3D), [TYPE_ROTATION_3D](class_animation.md#class_Animation_constant_TYPE_ROTATION_3D) and [TYPE_SCALE_3D](class_animation.md#class_Animation_constant_TYPE_SCALE_3D) track types instead of [TYPE_VALUE](class_animation.md#class_Animation_constant_TYPE_VALUE) is recommended for performance reasons.

<span id="class_Animation_constant_TYPE_POSITION_3D"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **TYPE_POSITION_3D** = `1`

3D position track (values are stored in [Vector3](class_vector3.md#class_Vector3) s).

<span id="class_Animation_constant_TYPE_ROTATION_3D"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **TYPE_ROTATION_3D** = `2`

3D rotation track (values are stored in [Quaternion](class_quaternion.md#class_Quaternion) s).

<span id="class_Animation_constant_TYPE_SCALE_3D"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **TYPE_SCALE_3D** = `3`

3D scale track (values are stored in [Vector3](class_vector3.md#class_Vector3) s).

<span id="class_Animation_constant_TYPE_BLEND_SHAPE"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **TYPE_BLEND_SHAPE** = `4`

Blend shape track.

<span id="class_Animation_constant_TYPE_METHOD"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **TYPE_METHOD** = `5`

Method tracks call functions with given arguments per key.

<span id="class_Animation_constant_TYPE_BEZIER"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **TYPE_BEZIER** = `6`

Bezier tracks are used to interpolate a value using custom curves. They can also be used to animate sub-properties of vectors and colors (e.g. alpha value of a [Color](class_color.md#class_Color)).

<span id="class_Animation_constant_TYPE_AUDIO"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **TYPE_AUDIO** = `7`

Audio tracks are used to play an audio stream with either type of [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer). The stream can be trimmed and previewed in the animation.

<span id="class_Animation_constant_TYPE_ANIMATION"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **TYPE_ANIMATION** = `8`

Animation tracks play animations in other [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer) nodes.

---

<span id="enum_Animation_InterpolationType"></span>

enum **InterpolationType**: [🔗](class_animation.md#enum_Animation_InterpolationType)

<span id="class_Animation_constant_INTERPOLATION_NEAREST"></span>

[InterpolationType](class_animation.md#enum_Animation_InterpolationType) **INTERPOLATION_NEAREST** = `0`

No interpolation (nearest value).

<span id="class_Animation_constant_INTERPOLATION_LINEAR"></span>

[InterpolationType](class_animation.md#enum_Animation_InterpolationType) **INTERPOLATION_LINEAR** = `1`

Linear interpolation.

<span id="class_Animation_constant_INTERPOLATION_CUBIC"></span>

[InterpolationType](class_animation.md#enum_Animation_InterpolationType) **INTERPOLATION_CUBIC** = `2`

Cubic interpolation. This looks smoother than linear interpolation, but is more expensive to interpolate. Stick to [INTERPOLATION_LINEAR](class_animation.md#class_Animation_constant_INTERPOLATION_LINEAR) for complex 3D animations imported from external software, even if it requires using a higher animation framerate in return.

<span id="class_Animation_constant_INTERPOLATION_LINEAR_ANGLE"></span>

[InterpolationType](class_animation.md#enum_Animation_InterpolationType) **INTERPOLATION_LINEAR_ANGLE** = `3`

Linear interpolation with shortest path rotation.

 **Note:** The result value is always normalized and may not match the key value.

<span id="class_Animation_constant_INTERPOLATION_CUBIC_ANGLE"></span>

[InterpolationType](class_animation.md#enum_Animation_InterpolationType) **INTERPOLATION_CUBIC_ANGLE** = `4`

Cubic interpolation with shortest path rotation.

 **Note:** The result value is always normalized and may not match the key value.

---

<span id="enum_Animation_UpdateMode"></span>

enum **UpdateMode**: [🔗](class_animation.md#enum_Animation_UpdateMode)

<span id="class_Animation_constant_UPDATE_CONTINUOUS"></span>

[UpdateMode](class_animation.md#enum_Animation_UpdateMode) **UPDATE_CONTINUOUS** = `0`

Update between keyframes and hold the value.

<span id="class_Animation_constant_UPDATE_DISCRETE"></span>

[UpdateMode](class_animation.md#enum_Animation_UpdateMode) **UPDATE_DISCRETE** = `1`

Update at the keyframes.

<span id="class_Animation_constant_UPDATE_CAPTURE"></span>

[UpdateMode](class_animation.md#enum_Animation_UpdateMode) **UPDATE_CAPTURE** = `2`

Same as [UPDATE_CONTINUOUS](class_animation.md#class_Animation_constant_UPDATE_CONTINUOUS) but works as a flag to capture the value of the current object and perform interpolation in some methods. See also [AnimationMixer.capture()](class_animationmixer.md#class_AnimationMixer_method_capture), [AnimationPlayer.playback_auto_capture](class_animationplayer.md#class_AnimationPlayer_property_playback_auto_capture), and [AnimationPlayer.play_with_capture()](class_animationplayer.md#class_AnimationPlayer_method_play_with_capture).

---

<span id="enum_Animation_LoopMode"></span>

enum **LoopMode**: [🔗](class_animation.md#enum_Animation_LoopMode)

<span id="class_Animation_constant_LOOP_NONE"></span>

[LoopMode](class_animation.md#enum_Animation_LoopMode) **LOOP_NONE** = `0`

At both ends of the animation, the animation will stop playing.

<span id="class_Animation_constant_LOOP_LINEAR"></span>

[LoopMode](class_animation.md#enum_Animation_LoopMode) **LOOP_LINEAR** = `1`

At both ends of the animation, the animation will be repeated without changing the playback direction.

<span id="class_Animation_constant_LOOP_PINGPONG"></span>

[LoopMode](class_animation.md#enum_Animation_LoopMode) **LOOP_PINGPONG** = `2`

Repeats playback and reverse playback at both ends of the animation.

---

<span id="enum_Animation_LoopedFlag"></span>

enum **LoopedFlag**: [🔗](class_animation.md#enum_Animation_LoopedFlag)

<span id="class_Animation_constant_LOOPED_FLAG_NONE"></span>

[LoopedFlag](class_animation.md#enum_Animation_LoopedFlag) **LOOPED_FLAG_NONE** = `0`

This flag indicates that the animation proceeds without any looping.

<span id="class_Animation_constant_LOOPED_FLAG_END"></span>

[LoopedFlag](class_animation.md#enum_Animation_LoopedFlag) **LOOPED_FLAG_END** = `1`

This flag indicates that the animation has reached the end of the animation and just after loop processed.

<span id="class_Animation_constant_LOOPED_FLAG_START"></span>

[LoopedFlag](class_animation.md#enum_Animation_LoopedFlag) **LOOPED_FLAG_START** = `2`

This flag indicates that the animation has reached the start of the animation and just after loop processed.

---

<span id="enum_Animation_FindMode"></span>

enum **FindMode**: [🔗](class_animation.md#enum_Animation_FindMode)

<span id="class_Animation_constant_FIND_MODE_NEAREST"></span>

[FindMode](class_animation.md#enum_Animation_FindMode) **FIND_MODE_NEAREST** = `0`

Finds the nearest time key.

<span id="class_Animation_constant_FIND_MODE_APPROX"></span>

[FindMode](class_animation.md#enum_Animation_FindMode) **FIND_MODE_APPROX** = `1`

Finds only the key with approximating the time.

<span id="class_Animation_constant_FIND_MODE_EXACT"></span>

[FindMode](class_animation.md#enum_Animation_FindMode) **FIND_MODE_EXACT** = `2`

Finds only the key with matching the time.

---

### Property Descriptions

<span id="class_Animation_property_capture_included"></span>

[bool](class_bool.md#class_bool) **capture_included** = `false` [🔗](class_animation.md#class_Animation_property_capture_included)

- [bool](class_bool.md#class_bool) **is_capture_included** ( )

Returns `true` if the capture track is included. This is a cached readonly value for performance.

---

<span id="class_Animation_property_length"></span>

[float](class_float.md#class_float) **length** = `1.0` [🔗](class_animation.md#class_Animation_property_length)

- void **set_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_length** ( )

The total length of the animation (in seconds).

 **Note:** Length is not delimited by the last key, as this one may be before or after the end to ensure correct interpolation and looping.

---

<span id="class_Animation_property_loop_mode"></span>

[LoopMode](class_animation.md#enum_Animation_LoopMode) **loop_mode** = `0` [🔗](class_animation.md#class_Animation_property_loop_mode)

- void **set_loop_mode** ( value: [LoopMode](class_animation.md#enum_Animation_LoopMode) )
- [LoopMode](class_animation.md#enum_Animation_LoopMode) **get_loop_mode** ( )

Determines the behavior of both ends of the animation timeline during animation playback. This indicates whether and how the animation should be restarted, and is also used to correctly interpolate animation cycles.

---

<span id="class_Animation_property_step"></span>

[float](class_float.md#class_float) **step** = `0.033333335` [🔗](class_animation.md#class_Animation_property_step)

- void **set_step** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_step** ( )

The animation step value.

---

### Method Descriptions

<span id="class_Animation_method_add_marker"></span>

void **add_marker** ( name: [StringName](class_stringname.md#class_StringName), time: [float](class_float.md#class_float) ) [🔗](class_animation.md#class_Animation_method_add_marker)

Adds a marker to this Animation.

---

<span id="class_Animation_method_add_track"></span>

[int](class_int.md#class_int) **add_track** ( type: [TrackType](class_animation.md#enum_Animation_TrackType), at_position: [int](class_int.md#class_int) = -1 ) [🔗](class_animation.md#class_Animation_method_add_track)

Adds a track to the Animation.

---

<span id="class_Animation_method_animation_track_get_key_animation"></span>

[StringName](class_stringname.md#class_StringName) **animation_track_get_key_animation** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_animation_track_get_key_animation)

Returns the animation name at the key identified by `key_idx`. The `track_idx` must be the index of an Animation Track.

---

<span id="class_Animation_method_animation_track_insert_key"></span>

[int](class_int.md#class_int) **animation_track_insert_key** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), animation: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animation.md#class_Animation_method_animation_track_insert_key)

Inserts a key with value `animation` at the given `time` (in seconds). The `track_idx` must be the index of an Animation Track.

---

<span id="class_Animation_method_animation_track_set_key_animation"></span>

void **animation_track_set_key_animation** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), animation: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animation.md#class_Animation_method_animation_track_set_key_animation)

Sets the key identified by `key_idx` to value `animation`. The `track_idx` must be the index of an Animation Track.

---

<span id="class_Animation_method_audio_track_get_key_end_offset"></span>

[float](class_float.md#class_float) **audio_track_get_key_end_offset** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_audio_track_get_key_end_offset)

Returns the end offset of the key identified by `key_idx`. The `track_idx` must be the index of an Audio Track.

End offset is the number of seconds cut off at the ending of the audio stream.

---

<span id="class_Animation_method_audio_track_get_key_start_offset"></span>

[float](class_float.md#class_float) **audio_track_get_key_start_offset** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_audio_track_get_key_start_offset)

Returns the start offset of the key identified by `key_idx`. The `track_idx` must be the index of an Audio Track.

Start offset is the number of seconds cut off at the beginning of the audio stream.

---

<span id="class_Animation_method_audio_track_get_key_stream"></span>

[Resource](class_resource.md#class_Resource) **audio_track_get_key_stream** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_audio_track_get_key_stream)

Returns the audio stream of the key identified by `key_idx`. The `track_idx` must be the index of an Audio Track.

---

<span id="class_Animation_method_audio_track_insert_key"></span>

[int](class_int.md#class_int) **audio_track_insert_key** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), stream: [Resource](class_resource.md#class_Resource), start_offset: [float](class_float.md#class_float) = 0, end_offset: [float](class_float.md#class_float) = 0 ) [🔗](class_animation.md#class_Animation_method_audio_track_insert_key)

Inserts an Audio Track key at the given `time` in seconds. The `track_idx` must be the index of an Audio Track.

 `stream` is the [AudioStream](class_audiostream.md#class_AudioStream) resource to play. `start_offset` is the number of seconds cut off at the beginning of the audio stream, while `end_offset` is at the ending.

---

<span id="class_Animation_method_audio_track_is_use_blend"></span>

[bool](class_bool.md#class_bool) **audio_track_is_use_blend** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_audio_track_is_use_blend)

Returns `true` if the track at `track_idx` will be blended with other animations.

---

<span id="class_Animation_method_audio_track_set_key_end_offset"></span>

void **audio_track_set_key_end_offset** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), offset: [float](class_float.md#class_float) ) [🔗](class_animation.md#class_Animation_method_audio_track_set_key_end_offset)

Sets the end offset of the key identified by `key_idx` to value `offset`. The `track_idx` must be the index of an Audio Track.

---

<span id="class_Animation_method_audio_track_set_key_start_offset"></span>

void **audio_track_set_key_start_offset** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), offset: [float](class_float.md#class_float) ) [🔗](class_animation.md#class_Animation_method_audio_track_set_key_start_offset)

Sets the start offset of the key identified by `key_idx` to value `offset`. The `track_idx` must be the index of an Audio Track.

---

<span id="class_Animation_method_audio_track_set_key_stream"></span>

void **audio_track_set_key_stream** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), stream: [Resource](class_resource.md#class_Resource) ) [🔗](class_animation.md#class_Animation_method_audio_track_set_key_stream)

Sets the stream of the key identified by `key_idx` to value `stream`. The `track_idx` must be the index of an Audio Track.

---

<span id="class_Animation_method_audio_track_set_use_blend"></span>

void **audio_track_set_use_blend** ( track_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_animation.md#class_Animation_method_audio_track_set_use_blend)

Sets whether the track will be blended with other animations. If `true`, the audio playback volume changes depending on the blend value.

---

<span id="class_Animation_method_bezier_track_get_key_in_handle"></span>

[Vector2](class_vector2.md#class_Vector2) **bezier_track_get_key_in_handle** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_bezier_track_get_key_in_handle)

Returns the in handle of the key identified by `key_idx`. The `track_idx` must be the index of a Bezier Track.

---

<span id="class_Animation_method_bezier_track_get_key_out_handle"></span>

[Vector2](class_vector2.md#class_Vector2) **bezier_track_get_key_out_handle** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_bezier_track_get_key_out_handle)

Returns the out handle of the key identified by `key_idx`. The `track_idx` must be the index of a Bezier Track.

---

<span id="class_Animation_method_bezier_track_get_key_value"></span>

[float](class_float.md#class_float) **bezier_track_get_key_value** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_bezier_track_get_key_value)

Returns the value of the key identified by `key_idx`. The `track_idx` must be the index of a Bezier Track.

---

<span id="class_Animation_method_bezier_track_insert_key"></span>

[int](class_int.md#class_int) **bezier_track_insert_key** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), value: [float](class_float.md#class_float), in_handle: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0), out_handle: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_animation.md#class_Animation_method_bezier_track_insert_key)

Inserts a Bezier Track key at the given `time` in seconds. The `track_idx` must be the index of a Bezier Track.

 `in_handle` is the left-side weight of the added Bezier curve point, `out_handle` is the right-side one, while `value` is the actual value at this point.

---

<span id="class_Animation_method_bezier_track_interpolate"></span>

[float](class_float.md#class_float) **bezier_track_interpolate** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float) ) *const* [🔗](class_animation.md#class_Animation_method_bezier_track_interpolate)

Returns the interpolated value at the given `time` (in seconds). The `track_idx` must be the index of a Bezier Track.

---

<span id="class_Animation_method_bezier_track_set_key_in_handle"></span>

void **bezier_track_set_key_in_handle** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), in_handle: [Vector2](class_vector2.md#class_Vector2), balanced_value_time_ratio: [float](class_float.md#class_float) = 1.0 ) [🔗](class_animation.md#class_Animation_method_bezier_track_set_key_in_handle)

Sets the in handle of the key identified by `key_idx` to value `in_handle`. The `track_idx` must be the index of a Bezier Track.

---

<span id="class_Animation_method_bezier_track_set_key_out_handle"></span>

void **bezier_track_set_key_out_handle** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), out_handle: [Vector2](class_vector2.md#class_Vector2), balanced_value_time_ratio: [float](class_float.md#class_float) = 1.0 ) [🔗](class_animation.md#class_Animation_method_bezier_track_set_key_out_handle)

Sets the out handle of the key identified by `key_idx` to value `out_handle`. The `track_idx` must be the index of a Bezier Track.

---

<span id="class_Animation_method_bezier_track_set_key_value"></span>

void **bezier_track_set_key_value** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) [🔗](class_animation.md#class_Animation_method_bezier_track_set_key_value)

Sets the value of the key identified by `key_idx` to the given value. The `track_idx` must be the index of a Bezier Track.

---

<span id="class_Animation_method_blend_shape_track_insert_key"></span>

[int](class_int.md#class_int) **blend_shape_track_insert_key** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), amount: [float](class_float.md#class_float) ) [🔗](class_animation.md#class_Animation_method_blend_shape_track_insert_key)

Inserts a key in a given blend shape track. Returns the key index.

---

<span id="class_Animation_method_blend_shape_track_interpolate"></span>

[float](class_float.md#class_float) **blend_shape_track_interpolate** ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_animation.md#class_Animation_method_blend_shape_track_interpolate)

Returns the interpolated blend shape value at the given time (in seconds). The `track_idx` must be the index of a blend shape track.

---

<span id="class_Animation_method_clear"></span>

void **clear** ( ) [🔗](class_animation.md#class_Animation_method_clear)

Clear the animation (clear all tracks and reset all).

---

<span id="class_Animation_method_compress"></span>

void **compress** ( page_size: [int](class_int.md#class_int) = 8192, fps: [int](class_int.md#class_int) = 120, split_tolerance: [float](class_float.md#class_float) = 4.0 ) [🔗](class_animation.md#class_Animation_method_compress)

Compress the animation and all its tracks in-place. This will make [track_is_compressed()](class_animation.md#class_Animation_method_track_is_compressed) return `true` once called on this **Animation**. Compressed tracks require less memory to be played, and are designed to be used for complex 3D animations (such as cutscenes) imported from external 3D software. Compression is lossy, but the difference is usually not noticeable in real world conditions.

 **Note:** Compressed tracks have various limitations (such as not being editable from the editor), so only use compressed animations if you actually need them.

---

<span id="class_Animation_method_copy_track"></span>

void **copy_track** ( track_idx: [int](class_int.md#class_int), to_animation: [Animation](class_animation.md#class_Animation) ) [🔗](class_animation.md#class_Animation_method_copy_track)

Adds a new track to `to_animation` that is a copy of the given track from this animation.

---

<span id="class_Animation_method_find_track"></span>

[int](class_int.md#class_int) **find_track** ( path: [NodePath](class_nodepath.md#class_NodePath), type: [TrackType](class_animation.md#enum_Animation_TrackType) ) *const* [🔗](class_animation.md#class_Animation_method_find_track)

Returns the index of the specified track. If the track is not found, return -1.

---

<span id="class_Animation_method_get_marker_at_time"></span>

[StringName](class_stringname.md#class_StringName) **get_marker_at_time** ( time: [float](class_float.md#class_float) ) *const* [🔗](class_animation.md#class_Animation_method_get_marker_at_time)

Returns the name of the marker located at the given time.

---

<span id="class_Animation_method_get_marker_color"></span>

[Color](class_color.md#class_Color) **get_marker_color** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animation.md#class_Animation_method_get_marker_color)

Returns the given marker's color.

---

<span id="class_Animation_method_get_marker_names"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_marker_names** ( ) *const* [🔗](class_animation.md#class_Animation_method_get_marker_names)

Returns every marker in this Animation, sorted ascending by time.

---

<span id="class_Animation_method_get_marker_time"></span>

[float](class_float.md#class_float) **get_marker_time** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animation.md#class_Animation_method_get_marker_time)

Returns the given marker's time.

---

<span id="class_Animation_method_get_next_marker"></span>

[StringName](class_stringname.md#class_StringName) **get_next_marker** ( time: [float](class_float.md#class_float) ) *const* [🔗](class_animation.md#class_Animation_method_get_next_marker)

Returns the closest marker that comes after the given time. If no such marker exists, an empty string is returned.

---

<span id="class_Animation_method_get_prev_marker"></span>

[StringName](class_stringname.md#class_StringName) **get_prev_marker** ( time: [float](class_float.md#class_float) ) *const* [🔗](class_animation.md#class_Animation_method_get_prev_marker)

Returns the closest marker that comes before the given time. If no such marker exists, an empty string is returned.

---

<span id="class_Animation_method_get_track_count"></span>

[int](class_int.md#class_int) **get_track_count** ( ) *const* [🔗](class_animation.md#class_Animation_method_get_track_count)

Returns the amount of tracks in the animation.

---

<span id="class_Animation_method_has_marker"></span>

[bool](class_bool.md#class_bool) **has_marker** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animation.md#class_Animation_method_has_marker)

Returns `true` if this Animation contains a marker with the given name.

---

<span id="class_Animation_method_method_track_get_name"></span>

[StringName](class_stringname.md#class_StringName) **method_track_get_name** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_method_track_get_name)

Returns the method name of a method track.

---

<span id="class_Animation_method_method_track_get_params"></span>

[Array](class_array.md#class_Array) **method_track_get_params** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_method_track_get_params)

Returns the arguments values to be called on a method track for a given key in a given track.

---

<span id="class_Animation_method_optimize"></span>

void **optimize** ( allowed_velocity_err: [float](class_float.md#class_float) = 0.01, allowed_angular_err: [float](class_float.md#class_float) = 0.01, precision: [int](class_int.md#class_int) = 3 ) [🔗](class_animation.md#class_Animation_method_optimize)

Optimize the animation and all its tracks in-place. This will preserve only as many keys as are necessary to keep the animation within the specified bounds.

---

<span id="class_Animation_method_position_track_insert_key"></span>

[int](class_int.md#class_int) **position_track_insert_key** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), position: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_animation.md#class_Animation_method_position_track_insert_key)

Inserts a key in a given 3D position track. Returns the key index.

---

<span id="class_Animation_method_position_track_interpolate"></span>

[Vector3](class_vector3.md#class_Vector3) **position_track_interpolate** ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_animation.md#class_Animation_method_position_track_interpolate)

Returns the interpolated position value at the given time (in seconds). The `track_idx` must be the index of a 3D position track.

---

<span id="class_Animation_method_remove_marker"></span>

void **remove_marker** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animation.md#class_Animation_method_remove_marker)

Removes the marker with the given name from this Animation.

---

<span id="class_Animation_method_remove_track"></span>

void **remove_track** ( track_idx: [int](class_int.md#class_int) ) [🔗](class_animation.md#class_Animation_method_remove_track)

Removes a track by specifying the track index.

---

<span id="class_Animation_method_rotation_track_insert_key"></span>

[int](class_int.md#class_int) **rotation_track_insert_key** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), rotation: [Quaternion](class_quaternion.md#class_Quaternion) ) [🔗](class_animation.md#class_Animation_method_rotation_track_insert_key)

Inserts a key in a given 3D rotation track. Returns the key index.

---

<span id="class_Animation_method_rotation_track_interpolate"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **rotation_track_interpolate** ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_animation.md#class_Animation_method_rotation_track_interpolate)

Returns the interpolated rotation value at the given time (in seconds). The `track_idx` must be the index of a 3D rotation track.

---

<span id="class_Animation_method_scale_track_insert_key"></span>

[int](class_int.md#class_int) **scale_track_insert_key** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), scale: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_animation.md#class_Animation_method_scale_track_insert_key)

Inserts a key in a given 3D scale track. Returns the key index.

---

<span id="class_Animation_method_scale_track_interpolate"></span>

[Vector3](class_vector3.md#class_Vector3) **scale_track_interpolate** ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_animation.md#class_Animation_method_scale_track_interpolate)

Returns the interpolated scale value at the given time (in seconds). The `track_idx` must be the index of a 3D scale track.

---

<span id="class_Animation_method_set_marker_color"></span>

void **set_marker_color** ( name: [StringName](class_stringname.md#class_StringName), color: [Color](class_color.md#class_Color) ) [🔗](class_animation.md#class_Animation_method_set_marker_color)

Sets the given marker's color.

---

<span id="class_Animation_method_track_find_key"></span>

[int](class_int.md#class_int) **track_find_key** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), find_mode: [FindMode](class_animation.md#enum_Animation_FindMode) = 0, limit: [bool](class_bool.md#class_bool) = false, backward: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_animation.md#class_Animation_method_track_find_key)

Finds the key index by time in a given track. Optionally, only find it if the approx/exact time is given.

If `limit` is `true`, it does not return keys outside the animation range.

If `backward` is `true`, the direction is reversed in methods that rely on one directional processing.

For example, in case `find_mode` is [FIND_MODE_NEAREST](class_animation.md#class_Animation_constant_FIND_MODE_NEAREST), if there is no key in the current position just after seeked, the first key found is retrieved by searching before the position, but if `backward` is `true`, the first key found is retrieved after the position.

---

<span id="class_Animation_method_track_get_interpolation_loop_wrap"></span>

[bool](class_bool.md#class_bool) **track_get_interpolation_loop_wrap** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_get_interpolation_loop_wrap)

Returns `true` if the track at `track_idx` wraps the interpolation loop. New tracks wrap the interpolation loop by default.

---

<span id="class_Animation_method_track_get_interpolation_type"></span>

[InterpolationType](class_animation.md#enum_Animation_InterpolationType) **track_get_interpolation_type** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_get_interpolation_type)

Returns the interpolation type of a given track.

---

<span id="class_Animation_method_track_get_key_count"></span>

[int](class_int.md#class_int) **track_get_key_count** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_get_key_count)

Returns the number of keys in a given track.

---

<span id="class_Animation_method_track_get_key_time"></span>

[float](class_float.md#class_float) **track_get_key_time** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_get_key_time)

Returns the time at which the key is located.

---

<span id="class_Animation_method_track_get_key_transition"></span>

[float](class_float.md#class_float) **track_get_key_transition** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_get_key_transition)

Returns the transition curve (easing) for a specific key (see the built-in math function @GlobalScope.ease()).

---

<span id="class_Animation_method_track_get_key_value"></span>

[Variant](class_variant.md#class_Variant) **track_get_key_value** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_get_key_value)

Returns the value of a given key in a given track.

---

<span id="class_Animation_method_track_get_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **track_get_path** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_get_path)

Gets the path of a track. For more information on the path format, see [track_set_path()](class_animation.md#class_Animation_method_track_set_path).

---

<span id="class_Animation_method_track_get_type"></span>

[TrackType](class_animation.md#enum_Animation_TrackType) **track_get_type** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_get_type)

Gets the type of a track.

---

<span id="class_Animation_method_track_insert_key"></span>

[int](class_int.md#class_int) **track_insert_key** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float), key: [Variant](class_variant.md#class_Variant), transition: [float](class_float.md#class_float) = 1 ) [🔗](class_animation.md#class_Animation_method_track_insert_key)

Inserts a generic key in a given track. Returns the key index.

---

<span id="class_Animation_method_track_is_compressed"></span>

[bool](class_bool.md#class_bool) **track_is_compressed** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_is_compressed)

Returns `true` if the track is compressed, `false` otherwise. See also [compress()](class_animation.md#class_Animation_method_compress).

---

<span id="class_Animation_method_track_is_enabled"></span>

[bool](class_bool.md#class_bool) **track_is_enabled** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_is_enabled)

Returns `true` if the track at index `track_idx` is enabled.

---

<span id="class_Animation_method_track_is_imported"></span>

[bool](class_bool.md#class_bool) **track_is_imported** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_track_is_imported)

Returns `true` if the given track is imported. Else, return `false`.

---

<span id="class_Animation_method_track_move_down"></span>

void **track_move_down** ( track_idx: [int](class_int.md#class_int) ) [🔗](class_animation.md#class_Animation_method_track_move_down)

Moves a track down.

---

<span id="class_Animation_method_track_move_to"></span>

void **track_move_to** ( track_idx: [int](class_int.md#class_int), to_idx: [int](class_int.md#class_int) ) [🔗](class_animation.md#class_Animation_method_track_move_to)

Changes the index position of track `track_idx` to the one defined in `to_idx`.

---

<span id="class_Animation_method_track_move_up"></span>

void **track_move_up** ( track_idx: [int](class_int.md#class_int) ) [🔗](class_animation.md#class_Animation_method_track_move_up)

Moves a track up.

---

<span id="class_Animation_method_track_remove_key"></span>

void **track_remove_key** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int) ) [🔗](class_animation.md#class_Animation_method_track_remove_key)

Removes a key by index in a given track.

---

<span id="class_Animation_method_track_remove_key_at_time"></span>

void **track_remove_key_at_time** ( track_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float) ) [🔗](class_animation.md#class_Animation_method_track_remove_key_at_time)

Removes a key at `time` in a given track.

---

<span id="class_Animation_method_track_set_enabled"></span>

void **track_set_enabled** ( track_idx: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_animation.md#class_Animation_method_track_set_enabled)

Enables/disables the given track. Tracks are enabled by default.

---

<span id="class_Animation_method_track_set_imported"></span>

void **track_set_imported** ( track_idx: [int](class_int.md#class_int), imported: [bool](class_bool.md#class_bool) ) [🔗](class_animation.md#class_Animation_method_track_set_imported)

Sets the given track as imported or not.

---

<span id="class_Animation_method_track_set_interpolation_loop_wrap"></span>

void **track_set_interpolation_loop_wrap** ( track_idx: [int](class_int.md#class_int), interpolation: [bool](class_bool.md#class_bool) ) [🔗](class_animation.md#class_Animation_method_track_set_interpolation_loop_wrap)

If `true`, the track at `track_idx` wraps the interpolation loop.

---

<span id="class_Animation_method_track_set_interpolation_type"></span>

void **track_set_interpolation_type** ( track_idx: [int](class_int.md#class_int), interpolation: [InterpolationType](class_animation.md#enum_Animation_InterpolationType) ) [🔗](class_animation.md#class_Animation_method_track_set_interpolation_type)

Sets the interpolation type of a given track.

---

<span id="class_Animation_method_track_set_key_time"></span>

void **track_set_key_time** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), time: [float](class_float.md#class_float) ) [🔗](class_animation.md#class_Animation_method_track_set_key_time)

Sets the time of an existing key.

---

<span id="class_Animation_method_track_set_key_transition"></span>

void **track_set_key_transition** ( track_idx: [int](class_int.md#class_int), key_idx: [int](class_int.md#class_int), transition: [float](class_float.md#class_float) ) [🔗](class_animation.md#class_Animation_method_track_set_key_transition)

Sets the transition curve (easing) for a specific key (see the built-in math function @GlobalScope.ease()).

---

<span id="class_Animation_method_track_set_key_value"></span>

void **track_set_key_value** ( track_idx: [int](class_int.md#class_int), key: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_animation.md#class_Animation_method_track_set_key_value)

Sets the value of an existing key.

---

<span id="class_Animation_method_track_set_path"></span>

void **track_set_path** ( track_idx: [int](class_int.md#class_int), path: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_animation.md#class_Animation_method_track_set_path)

Sets the path of a track. Paths must be valid scene-tree paths to a node and must be specified starting from the [AnimationMixer.root_node](class_animationmixer.md#class_AnimationMixer_property_root_node) that will reproduce the animation. Tracks that control properties or bones must append their name after the path, separated by `":"`.

For example, `"character/skeleton:ankle"` or `"character/mesh:transform/local"`.

---

<span id="class_Animation_method_track_swap"></span>

void **track_swap** ( track_idx: [int](class_int.md#class_int), with_idx: [int](class_int.md#class_int) ) [🔗](class_animation.md#class_Animation_method_track_swap)

Swaps the track `track_idx`'s index position with the track `with_idx`.

---

<span id="class_Animation_method_value_track_get_update_mode"></span>

[UpdateMode](class_animation.md#enum_Animation_UpdateMode) **value_track_get_update_mode** ( track_idx: [int](class_int.md#class_int) ) *const* [🔗](class_animation.md#class_Animation_method_value_track_get_update_mode)

Returns the update mode of a value track.

---

<span id="class_Animation_method_value_track_interpolate"></span>

[Variant](class_variant.md#class_Variant) **value_track_interpolate** ( track_idx: [int](class_int.md#class_int), time_sec: [float](class_float.md#class_float), backward: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_animation.md#class_Animation_method_value_track_interpolate)

Returns the interpolated value at the given time (in seconds). The `track_idx` must be the index of a value track.

A `backward` mainly affects the direction of key retrieval of the track with [UPDATE_DISCRETE](class_animation.md#class_Animation_constant_UPDATE_DISCRETE) converted by [AnimationMixer.ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS](class_animationmixer.md#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS) to match the result with [track_find_key()](class_animation.md#class_Animation_method_track_find_key).

---

<span id="class_Animation_method_value_track_set_update_mode"></span>

void **value_track_set_update_mode** ( track_idx: [int](class_int.md#class_int), mode: [UpdateMode](class_animation.md#enum_Animation_UpdateMode) ) [🔗](class_animation.md#class_Animation_method_value_track_set_update_mode)

Sets the update mode of a value track.
