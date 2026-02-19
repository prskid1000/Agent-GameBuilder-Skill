<span id="class_AnimationNodeAnimation"></span>

## AnimationNodeAnimation

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An input animation for an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

### Description

A resource to add to an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree). Only has one output port using the [animation](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_animation) property. Used as an input for [AnimationNode](class_animationnode.md#class_AnimationNode) s that blend animations together.

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

- 3D Platformer Demo

- Third Person Shooter (TPS) Demo

### Properties


| [bool](class_bool.md#class_bool) | [advance_on_start](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_advance_on_start) | `false` |
| --- | --- | --- |
| [StringName](class_stringname.md#class_StringName) | [animation](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_animation) | `&""` |
| [LoopMode](class_animation.md#enum_Animation_LoopMode) | [loop_mode](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_loop_mode) |
| [PlayMode](class_animationnodeanimation.md#enum_AnimationNodeAnimation_PlayMode) | [play_mode](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_play_mode) | `0` |
| [float](class_float.md#class_float) | [start_offset](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_start_offset) |
| [bool](class_bool.md#class_bool) | [stretch_time_scale](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_stretch_time_scale) |
| [float](class_float.md#class_float) | [timeline_length](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_timeline_length) |
| [bool](class_bool.md#class_bool) | [use_custom_timeline](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_use_custom_timeline) | `false` |

---

### Enumerations

<span id="enum_AnimationNodeAnimation_PlayMode"></span>

enum **PlayMode**: [🔗](class_animationnodeanimation.md#enum_AnimationNodeAnimation_PlayMode)

<span id="class_AnimationNodeAnimation_constant_PLAY_MODE_FORWARD"></span>

[PlayMode](class_animationnodeanimation.md#enum_AnimationNodeAnimation_PlayMode) **PLAY_MODE_FORWARD** = `0`

Plays animation in forward direction.

<span id="class_AnimationNodeAnimation_constant_PLAY_MODE_BACKWARD"></span>

[PlayMode](class_animationnodeanimation.md#enum_AnimationNodeAnimation_PlayMode) **PLAY_MODE_BACKWARD** = `1`

Plays animation in backward direction.

---

### Property Descriptions

<span id="class_AnimationNodeAnimation_property_advance_on_start"></span>

[bool](class_bool.md#class_bool) **advance_on_start** = `false` [🔗](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_advance_on_start)

- void **set_advance_on_start** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_advance_on_start** ( )

If `true`, on receiving a request to play an animation from the start, the first frame is not drawn, but only processed, and playback starts from the next frame.

See also the notes of [AnimationPlayer.play()](class_animationplayer.md#class_AnimationPlayer_method_play).

---

<span id="class_AnimationNodeAnimation_property_animation"></span>

[StringName](class_stringname.md#class_StringName) **animation** = `&""` [🔗](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_animation)

- void **set_animation** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_animation** ( )

Animation to use as an output. It is one of the animations provided by [AnimationTree.anim_player](class_animationtree.md#class_AnimationTree_property_anim_player).

---

<span id="class_AnimationNodeAnimation_property_loop_mode"></span>

[LoopMode](class_animation.md#enum_Animation_LoopMode) **loop_mode** [🔗](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_loop_mode)

- void **set_loop_mode** ( value: [LoopMode](class_animation.md#enum_Animation_LoopMode) )
- [LoopMode](class_animation.md#enum_Animation_LoopMode) **get_loop_mode** ( )

If [use_custom_timeline](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_use_custom_timeline) is `true`, override the loop settings of the original [Animation](class_animation.md#class_Animation) resource with the value.

 **Note:** If the [Animation.loop_mode](class_animation.md#class_Animation_property_loop_mode) isn't set to looping, the [Animation.track_set_interpolation_loop_wrap()](class_animation.md#class_Animation_method_track_set_interpolation_loop_wrap) option will not be respected. If you cannot get the expected behavior, consider duplicating the [Animation](class_animation.md#class_Animation) resource and changing the loop settings.

---

<span id="class_AnimationNodeAnimation_property_play_mode"></span>

[PlayMode](class_animationnodeanimation.md#enum_AnimationNodeAnimation_PlayMode) **play_mode** = `0` [🔗](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_play_mode)

- void **set_play_mode** ( value: [PlayMode](class_animationnodeanimation.md#enum_AnimationNodeAnimation_PlayMode) )
- [PlayMode](class_animationnodeanimation.md#enum_AnimationNodeAnimation_PlayMode) **get_play_mode** ( )

Determines the playback direction of the animation.

---

<span id="class_AnimationNodeAnimation_property_start_offset"></span>

[float](class_float.md#class_float) **start_offset** [🔗](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_start_offset)

- void **set_start_offset** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_start_offset** ( )

If [use_custom_timeline](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_use_custom_timeline) is `true`, offset the start position of the animation.

This is useful for adjusting which foot steps first in 3D walking animations.

---

<span id="class_AnimationNodeAnimation_property_stretch_time_scale"></span>

[bool](class_bool.md#class_bool) **stretch_time_scale** [🔗](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_stretch_time_scale)

- void **set_stretch_time_scale** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_stretching_time_scale** ( )

If `true`, scales the time so that the length specified in [timeline_length](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_timeline_length) is one cycle.

This is useful for matching the periods of walking and running animations.

If `false`, the original animation length is respected. If you set the loop to [loop_mode](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_loop_mode), the animation will loop in [timeline_length](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_timeline_length).

---

<span id="class_AnimationNodeAnimation_property_timeline_length"></span>

[float](class_float.md#class_float) **timeline_length** [🔗](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_timeline_length)

- void **set_timeline_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_timeline_length** ( )

The length of the custom timeline.

If [stretch_time_scale](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_stretch_time_scale) is `true`, scales the animation to this length.

---

<span id="class_AnimationNodeAnimation_property_use_custom_timeline"></span>

[bool](class_bool.md#class_bool) **use_custom_timeline** = `false` [🔗](class_animationnodeanimation.md#class_AnimationNodeAnimation_property_use_custom_timeline)

- void **set_use_custom_timeline** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_custom_timeline** ( )

If `true`, [AnimationNode](class_animationnode.md#class_AnimationNode) provides an animation based on the [Animation](class_animation.md#class_Animation) resource with some parameters adjusted.
