<span id="class_SkeletonModification2DTwoBoneIK"></span>

## SkeletonModification2DTwoBoneIK

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A modification that rotates two bones using the law of cosines to reach the target.

### Description

This [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) uses an algorithm typically called TwoBoneIK. This algorithm works by leveraging the law of cosines and the lengths of the bones to figure out what rotation the bones currently have, and what rotation they need to make a complete triangle, where the first bone, the second bone, and the target form the three vertices of the triangle. Because the algorithm works by making a triangle, it can only operate on two bones.

TwoBoneIK is great for arms, legs, and really any joints that can be represented by just two bones that bend to reach a target. This solver is more lightweight than [SkeletonModification2DFABRIK](class_skeletonmodification2dfabrik.md#class_SkeletonModification2DFABRIK), but gives similar, natural looking results.

### Properties


| [bool](class_bool.md#class_bool) | [flip_bend_direction](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_property_flip_bend_direction) | `false` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [target_maximum_distance](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_property_target_maximum_distance) | `0.0` |
| [float](class_float.md#class_float) | [target_minimum_distance](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_property_target_minimum_distance) | `0.0` |
| [NodePath](class_nodepath.md#class_NodePath) | [target_nodepath](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_property_target_nodepath) | `NodePath("")` |

### Methods


| [NodePath](class_nodepath.md#class_NodePath) | [get_joint_one_bone2d_node](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone2d_node) ( ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_joint_one_bone_idx](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone_idx) ( ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_joint_two_bone2d_node](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone2d_node) ( ) const |
| [int](class_int.md#class_int) | [get_joint_two_bone_idx](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone_idx) ( ) const |
| void | [set_joint_one_bone2d_node](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone2d_node) ( bone2d_node: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_joint_one_bone_idx](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone_idx) ( bone_idx: [int](class_int.md#class_int) ) |
| void | [set_joint_two_bone2d_node](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone2d_node) ( bone2d_node: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_joint_two_bone_idx](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone_idx) ( bone_idx: [int](class_int.md#class_int) ) |

---

### Property Descriptions

<span id="class_SkeletonModification2DTwoBoneIK_property_flip_bend_direction"></span>

[bool](class_bool.md#class_bool) **flip_bend_direction** = `false` [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_property_flip_bend_direction)

- void **set_flip_bend_direction** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flip_bend_direction** ( )

If `true`, the bones in the modification will bend outward as opposed to inwards when contracting. If `false`, the bones will bend inwards when contracting.

---

<span id="class_SkeletonModification2DTwoBoneIK_property_target_maximum_distance"></span>

[float](class_float.md#class_float) **target_maximum_distance** = `0.0` [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_property_target_maximum_distance)

- void **set_target_maximum_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_target_maximum_distance** ( )

The maximum distance the target can be at. If the target is farther than this distance, the modification will solve as if it's at this maximum distance. When set to `0`, the modification will solve without distance constraints.

---

<span id="class_SkeletonModification2DTwoBoneIK_property_target_minimum_distance"></span>

[float](class_float.md#class_float) **target_minimum_distance** = `0.0` [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_property_target_minimum_distance)

- void **set_target_minimum_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_target_minimum_distance** ( )

The minimum distance the target can be at. If the target is closer than this distance, the modification will solve as if it's at this minimum distance. When set to `0`, the modification will solve without distance constraints.

---

<span id="class_SkeletonModification2DTwoBoneIK_property_target_nodepath"></span>

[NodePath](class_nodepath.md#class_NodePath) **target_nodepath** = `NodePath("")` [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_property_target_nodepath)

- void **set_target_node** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_target_node** ( )

The NodePath to the node that is the target for the TwoBoneIK modification. This node is what the modification will use when bending the [Bone2D](class_bone2d.md#class_Bone2D) nodes.

---

### Method Descriptions

<span id="class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone2d_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_joint_one_bone2d_node** ( ) *const* [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone2d_node)

Returns the [Bone2D](class_bone2d.md#class_Bone2D) node that is being used as the first bone in the TwoBoneIK modification.

---

<span id="class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone_idx"></span>

[int](class_int.md#class_int) **get_joint_one_bone_idx** ( ) *const* [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone_idx)

Returns the index of the [Bone2D](class_bone2d.md#class_Bone2D) node that is being used as the first bone in the TwoBoneIK modification.

---

<span id="class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone2d_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_joint_two_bone2d_node** ( ) *const* [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone2d_node)

Returns the [Bone2D](class_bone2d.md#class_Bone2D) node that is being used as the second bone in the TwoBoneIK modification.

---

<span id="class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone_idx"></span>

[int](class_int.md#class_int) **get_joint_two_bone_idx** ( ) *const* [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone_idx)

Returns the index of the [Bone2D](class_bone2d.md#class_Bone2D) node that is being used as the second bone in the TwoBoneIK modification.

---

<span id="class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone2d_node"></span>

void **set_joint_one_bone2d_node** ( bone2d_node: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone2d_node)

Sets the [Bone2D](class_bone2d.md#class_Bone2D) node that is being used as the first bone in the TwoBoneIK modification.

---

<span id="class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone_idx"></span>

void **set_joint_one_bone_idx** ( bone_idx: [int](class_int.md#class_int) ) [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone_idx)

Sets the index of the [Bone2D](class_bone2d.md#class_Bone2D) node that is being used as the first bone in the TwoBoneIK modification.

---

<span id="class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone2d_node"></span>

void **set_joint_two_bone2d_node** ( bone2d_node: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone2d_node)

Sets the [Bone2D](class_bone2d.md#class_Bone2D) node that is being used as the second bone in the TwoBoneIK modification.

---

<span id="class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone_idx"></span>

void **set_joint_two_bone_idx** ( bone_idx: [int](class_int.md#class_int) ) [🔗](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone_idx)

Sets the index of the [Bone2D](class_bone2d.md#class_Bone2D) node that is being used as the second bone in the TwoBoneIK modification.
