<span id="class_SplineIK3D"></span>

## SplineIK3D

**Inherits:** [ChainIK3D](class_chainik3d.md#class_ChainIK3D) **<** [IKModifier3D](class_ikmodifier3d.md#class_IKModifier3D) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) for aligning bones along a [Path3D](class_path3d.md#class_Path3D).

### Description

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) for aligning bones along a [Path3D](class_path3d.md#class_Path3D). The smoothness of the fitting depends on the [Curve3D.bake_interval](class_curve3d.md#class_Curve3D_property_bake_interval).

If you want the [Path3D](class_path3d.md#class_Path3D) to attach to a specific bone, it is recommended to place a [ModifierBoneTarget3D](class_modifierbonetarget3d.md#class_ModifierBoneTarget3D) before the **SplineIK3D** in the [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) list (children of the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D)), and then place a [Path3D](class_path3d.md#class_Path3D) as the [ModifierBoneTarget3D](class_modifierbonetarget3d.md#class_ModifierBoneTarget3D)'s child.

Bone twist is determined based on the [Curve3D.get_point_tilt()](class_curve3d.md#class_Curve3D_method_get_point_tilt).

If the root bone joint and the start point of the [Curve3D](class_curve3d.md#class_Curve3D) are separated, it assumes that there is a linear line segment between them. This means that the vector pointing toward the start point of the [Curve3D](class_curve3d.md#class_Curve3D) takes precedence over the shortest intersection point along the [Curve3D](class_curve3d.md#class_Curve3D).

If the end bone joint exceeds the path length, it is bent as close as possible to the end point of the [Curve3D](class_curve3d.md#class_Curve3D).

### Properties


| [int](class_int.md#class_int) | [setting_count](class_splineik3d.md#class_SplineIK3D_property_setting_count) | `0` |
| --- | --- | --- |

### Methods


| [NodePath](class_nodepath.md#class_NodePath) | [get_path_3d](class_splineik3d.md#class_SplineIK3D_method_get_path_3d) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_tilt_fade_in](class_splineik3d.md#class_SplineIK3D_method_get_tilt_fade_in) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_tilt_fade_out](class_splineik3d.md#class_SplineIK3D_method_get_tilt_fade_out) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_tilt_enabled](class_splineik3d.md#class_SplineIK3D_method_is_tilt_enabled) ( index: [int](class_int.md#class_int) ) const |
| void | [set_path_3d](class_splineik3d.md#class_SplineIK3D_method_set_path_3d) ( index: [int](class_int.md#class_int), path_3d: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_tilt_enabled](class_splineik3d.md#class_SplineIK3D_method_set_tilt_enabled) ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_tilt_fade_in](class_splineik3d.md#class_SplineIK3D_method_set_tilt_fade_in) ( index: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) |
| void | [set_tilt_fade_out](class_splineik3d.md#class_SplineIK3D_method_set_tilt_fade_out) ( index: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) |

---

### Property Descriptions

<span id="class_SplineIK3D_property_setting_count"></span>

[int](class_int.md#class_int) **setting_count** = `0` [🔗](class_splineik3d.md#class_SplineIK3D_property_setting_count)

- void **set_setting_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_setting_count** ( )

The number of settings.

---

### Method Descriptions

<span id="class_SplineIK3D_method_get_path_3d"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_path_3d** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_splineik3d.md#class_SplineIK3D_method_get_path_3d)

Returns the node path of the [Path3D](class_path3d.md#class_Path3D) which is describing the path.

---

<span id="class_SplineIK3D_method_get_tilt_fade_in"></span>

[int](class_int.md#class_int) **get_tilt_fade_in** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_splineik3d.md#class_SplineIK3D_method_get_tilt_fade_in)

Returns the tilt interpolation method used between the root bone and the start point of the [Curve3D](class_curve3d.md#class_Curve3D) when they are apart. See also [set_tilt_fade_in()](class_splineik3d.md#class_SplineIK3D_method_set_tilt_fade_in).

---

<span id="class_SplineIK3D_method_get_tilt_fade_out"></span>

[int](class_int.md#class_int) **get_tilt_fade_out** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_splineik3d.md#class_SplineIK3D_method_get_tilt_fade_out)

Returns the tilt interpolation method used between the end bone and the end point of the [Curve3D](class_curve3d.md#class_Curve3D) when they are apart. See also [set_tilt_fade_out()](class_splineik3d.md#class_SplineIK3D_method_set_tilt_fade_out).

---

<span id="class_SplineIK3D_method_is_tilt_enabled"></span>

[bool](class_bool.md#class_bool) **is_tilt_enabled** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_splineik3d.md#class_SplineIK3D_method_is_tilt_enabled)

Returns if the tilt property of the [Curve3D](class_curve3d.md#class_Curve3D) affects the bone twist.

---

<span id="class_SplineIK3D_method_set_path_3d"></span>

void **set_path_3d** ( index: [int](class_int.md#class_int), path_3d: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_splineik3d.md#class_SplineIK3D_method_set_path_3d)

Sets the node path of the [Path3D](class_path3d.md#class_Path3D) which is describing the path.

---

<span id="class_SplineIK3D_method_set_tilt_enabled"></span>

void **set_tilt_enabled** ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_splineik3d.md#class_SplineIK3D_method_set_tilt_enabled)

Sets if the tilt property of the [Curve3D](class_curve3d.md#class_Curve3D) should affect the bone twist.

---

<span id="class_SplineIK3D_method_set_tilt_fade_in"></span>

void **set_tilt_fade_in** ( index: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) [🔗](class_splineik3d.md#class_SplineIK3D_method_set_tilt_fade_in)

If `size` is greater than `0`, the tilt is interpolated between `size` start bones from the start point of the [Curve3D](class_curve3d.md#class_Curve3D) when they are apart.

If `size` is equal `0`, the tilts between the root bone head and the start point of the [Curve3D](class_curve3d.md#class_Curve3D) are unified with a tilt of the start point of the [Curve3D](class_curve3d.md#class_Curve3D).

If `size` is less than `0`, the tilts between the root bone and the start point of the [Curve3D](class_curve3d.md#class_Curve3D) are `0.0`.

---

<span id="class_SplineIK3D_method_set_tilt_fade_out"></span>

void **set_tilt_fade_out** ( index: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) [🔗](class_splineik3d.md#class_SplineIK3D_method_set_tilt_fade_out)

If `size` is greater than `0`, the tilt is interpolated between `size` end bones from the end point of the [Curve3D](class_curve3d.md#class_Curve3D) when they are apart.

If `size` is equal `0`, the tilts between the end bone tail and the end point of the [Curve3D](class_curve3d.md#class_Curve3D) are unified with a tilt of the end point of the [Curve3D](class_curve3d.md#class_Curve3D).

If `size` is less than `0`, the tilts between the end bone and the end point of the [Curve3D](class_curve3d.md#class_Curve3D) are `0.0`.
