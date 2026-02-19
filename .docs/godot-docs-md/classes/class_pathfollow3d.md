<span id="class_PathFollow3D"></span>

## PathFollow3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Point sampler for a [Path3D](class_path3d.md#class_Path3D).

### Description

This node takes its parent [Path3D](class_path3d.md#class_Path3D), and returns the coordinates of a point within it, given a distance from the first vertex.

It is useful for making other nodes follow a path, without coding the movement pattern. For that, the nodes must be children of this node. The descendant nodes will then move accordingly when setting the [progress](class_pathfollow3d.md#class_PathFollow3D_property_progress) in this node.

### Properties


| [bool](class_bool.md#class_bool) | [cubic_interp](class_pathfollow3d.md#class_PathFollow3D_property_cubic_interp) | `true` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [h_offset](class_pathfollow3d.md#class_PathFollow3D_property_h_offset) | `0.0` |
| [bool](class_bool.md#class_bool) | [loop](class_pathfollow3d.md#class_PathFollow3D_property_loop) | `true` |
| [float](class_float.md#class_float) | [progress](class_pathfollow3d.md#class_PathFollow3D_property_progress) | `0.0` |
| [float](class_float.md#class_float) | [progress_ratio](class_pathfollow3d.md#class_PathFollow3D_property_progress_ratio) | `0.0` |
| [RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) | [rotation_mode](class_pathfollow3d.md#class_PathFollow3D_property_rotation_mode) | `3` |
| [bool](class_bool.md#class_bool) | [tilt_enabled](class_pathfollow3d.md#class_PathFollow3D_property_tilt_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [use_model_front](class_pathfollow3d.md#class_PathFollow3D_property_use_model_front) | `false` |
| [float](class_float.md#class_float) | [v_offset](class_pathfollow3d.md#class_PathFollow3D_property_v_offset) | `0.0` |

### Methods


| [Transform3D](class_transform3d.md#class_Transform3D) | [correct_posture](class_pathfollow3d.md#class_PathFollow3D_method_correct_posture) ( transform: [Transform3D](class_transform3d.md#class_Transform3D), rotation_mode: [RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) ) static |
| --- | --- |

---

### Enumerations

<span id="enum_PathFollow3D_RotationMode"></span>

enum **RotationMode**: [🔗](class_pathfollow3d.md#enum_PathFollow3D_RotationMode)

<span id="class_PathFollow3D_constant_ROTATION_NONE"></span>

[RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) **ROTATION_NONE** = `0`

Forbids the PathFollow3D to rotate.

<span id="class_PathFollow3D_constant_ROTATION_Y"></span>

[RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) **ROTATION_Y** = `1`

Allows the PathFollow3D to rotate in the Y axis only.

<span id="class_PathFollow3D_constant_ROTATION_XY"></span>

[RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) **ROTATION_XY** = `2`

Allows the PathFollow3D to rotate in both the X, and Y axes.

<span id="class_PathFollow3D_constant_ROTATION_XYZ"></span>

[RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) **ROTATION_XYZ** = `3`

Allows the PathFollow3D to rotate in any axis.

<span id="class_PathFollow3D_constant_ROTATION_ORIENTED"></span>

[RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) **ROTATION_ORIENTED** = `4`

Uses the up vector information in a [Curve3D](class_curve3d.md#class_Curve3D) to enforce orientation. This rotation mode requires the [Path3D](class_path3d.md#class_Path3D)'s [Curve3D.up_vector_enabled](class_curve3d.md#class_Curve3D_property_up_vector_enabled) property to be set to `true`.

---

### Property Descriptions

<span id="class_PathFollow3D_property_cubic_interp"></span>

[bool](class_bool.md#class_bool) **cubic_interp** = `true` [🔗](class_pathfollow3d.md#class_PathFollow3D_property_cubic_interp)

- void **set_cubic_interpolation** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_cubic_interpolation** ( )

If `true`, the position between two cached points is interpolated cubically, and linearly otherwise.

The points along the [Curve3D](class_curve3d.md#class_Curve3D) of the [Path3D](class_path3d.md#class_Path3D) are precomputed before use, for faster calculations. The point at the requested offset is then calculated interpolating between two adjacent cached points. This may present a problem if the curve makes sharp turns, as the cached points may not follow the curve closely enough.

There are two answers to this problem: either increase the number of cached points and increase memory consumption, or make a cubic interpolation between two points at the cost of (slightly) slower calculations.

---

<span id="class_PathFollow3D_property_h_offset"></span>

[float](class_float.md#class_float) **h_offset** = `0.0` [🔗](class_pathfollow3d.md#class_PathFollow3D_property_h_offset)

- void **set_h_offset** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_h_offset** ( )

The node's offset along the curve.

---

<span id="class_PathFollow3D_property_loop"></span>

[bool](class_bool.md#class_bool) **loop** = `true` [🔗](class_pathfollow3d.md#class_PathFollow3D_property_loop)

- void **set_loop** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_loop** ( )

If `true`, any offset outside the path's length will wrap around, instead of stopping at the ends. Use it for cyclic paths.

---

<span id="class_PathFollow3D_property_progress"></span>

[float](class_float.md#class_float) **progress** = `0.0` [🔗](class_pathfollow3d.md#class_PathFollow3D_property_progress)

- void **set_progress** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_progress** ( )

The distance from the first vertex, measured in 3D units along the path. Changing this value sets this node's position to a point within the path.

---

<span id="class_PathFollow3D_property_progress_ratio"></span>

[float](class_float.md#class_float) **progress_ratio** = `0.0` [🔗](class_pathfollow3d.md#class_PathFollow3D_property_progress_ratio)

- void **set_progress_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_progress_ratio** ( )

The distance from the first vertex, considering 0.0 as the first vertex and 1.0 as the last. This is just another way of expressing the progress within the path, as the progress supplied is multiplied internally by the path's length.

It can be set or get only if the **PathFollow3D** is the child of a [Path3D](class_path3d.md#class_Path3D) which is part of the scene tree, and that this [Path3D](class_path3d.md#class_Path3D) has a [Curve3D](class_curve3d.md#class_Curve3D) with a non-zero length. Otherwise, trying to set this field will print an error, and getting this field will return `0.0`.

---

<span id="class_PathFollow3D_property_rotation_mode"></span>

[RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) **rotation_mode** = `3` [🔗](class_pathfollow3d.md#class_PathFollow3D_property_rotation_mode)

- void **set_rotation_mode** ( value: [RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) )
- [RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) **get_rotation_mode** ( )

Allows or forbids rotation on one or more axes, depending on the [RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) constants being used.

---

<span id="class_PathFollow3D_property_tilt_enabled"></span>

[bool](class_bool.md#class_bool) **tilt_enabled** = `true` [🔗](class_pathfollow3d.md#class_PathFollow3D_property_tilt_enabled)

- void **set_tilt_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_tilt_enabled** ( )

If `true`, the tilt property of [Curve3D](class_curve3d.md#class_Curve3D) takes effect.

---

<span id="class_PathFollow3D_property_use_model_front"></span>

[bool](class_bool.md#class_bool) **use_model_front** = `false` [🔗](class_pathfollow3d.md#class_PathFollow3D_property_use_model_front)

- void **set_use_model_front** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_model_front** ( )

If `true`, the node moves on the travel path with orienting the +Z axis as forward. See also [Vector3.FORWARD](class_vector3.md#class_Vector3_constant_FORWARD) and [Vector3.MODEL_FRONT](class_vector3.md#class_Vector3_constant_MODEL_FRONT).

---

<span id="class_PathFollow3D_property_v_offset"></span>

[float](class_float.md#class_float) **v_offset** = `0.0` [🔗](class_pathfollow3d.md#class_PathFollow3D_property_v_offset)

- void **set_v_offset** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_v_offset** ( )

The node's offset perpendicular to the curve.

---

### Method Descriptions

<span id="class_PathFollow3D_method_correct_posture"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **correct_posture** ( transform: [Transform3D](class_transform3d.md#class_Transform3D), rotation_mode: [RotationMode](class_pathfollow3d.md#enum_PathFollow3D_RotationMode) ) *static* [🔗](class_pathfollow3d.md#class_PathFollow3D_method_correct_posture)

Correct the `transform`. `rotation_mode` implicitly specifies how posture (forward, up and sideway direction) is calculated.
