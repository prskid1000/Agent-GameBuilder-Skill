<span id="class_AnimationNodeExtension"></span>

## AnimationNodeExtension

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Base class for extending [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) s from GDScript, C#, or C++.

### Description

**AnimationNodeExtension** exposes the APIs of [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) to allow users to extend it from GDScript, C#, or C++. This class is not meant to be used directly, but to be extended by other classes. It is used to create custom nodes for the [AnimationTree](class_animationtree.md#class_AnimationTree) system.

### Methods


| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [_process_animation_node](class_animationnodeextension.md#class_AnimationNodeExtension_private_method__process_animation_node) ( playback_info: [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array), test_only: [bool](class_bool.md#class_bool) ) | virtual | required |
| --- | --- | --- | --- |
| [float](class_float.md#class_float) | [get_remaining_time](class_animationnodeextension.md#class_AnimationNodeExtension_method_get_remaining_time) ( node_info: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), break_loop: [bool](class_bool.md#class_bool) ) static |
| [bool](class_bool.md#class_bool) | [is_looping](class_animationnodeextension.md#class_AnimationNodeExtension_method_is_looping) ( node_info: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) static |

---

### Method Descriptions

<span id="class_AnimationNodeExtension_private_method__process_animation_node"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **_process_animation_node** ( playback_info: [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array), test_only: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_animationnodeextension.md#class_AnimationNodeExtension_private_method__process_animation_node)

A version of the [AnimationNode._process()](class_animationnode.md#class_AnimationNode_private_method__process) method that is meant to be overridden by custom nodes. It returns a [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) with the processed animation data.

The [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) parameter contains the playback information, containing the following values encoded as floating point numbers (in order): playback time and delta, start and end times, whether a seek was requested (encoded as a float greater than `0`), whether the seek request was externally requested (encoded as a float greater than `0`), the current [LoopedFlag](class_animation.md#enum_Animation_LoopedFlag) (encoded as a float), and the current blend weight.

The function must return a [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) of the node's time info, containing the following values (in order): animation length, time position, delta, [LoopMode](class_animation.md#enum_Animation_LoopMode) (encoded as a float), whether the animation is about to end (encoded as a float greater than `0`) and whether the animation is infinite (encoded as a float greater than `0`). All values must be included in the returned array.

---

<span id="class_AnimationNodeExtension_method_get_remaining_time"></span>

[float](class_float.md#class_float) **get_remaining_time** ( node_info: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), break_loop: [bool](class_bool.md#class_bool) ) *static* [🔗](class_animationnodeextension.md#class_AnimationNodeExtension_method_get_remaining_time)

Returns the animation's remaining time for the given node info. For looping animations, it will only return the remaining time if `break_loop` is `true`, a large integer value will be returned otherwise.

---

<span id="class_AnimationNodeExtension_method_is_looping"></span>

[bool](class_bool.md#class_bool) **is_looping** ( node_info: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) *static* [🔗](class_animationnodeextension.md#class_AnimationNodeExtension_method_is_looping)

Returns `true` if the animation for the given `node_info` is looping.
