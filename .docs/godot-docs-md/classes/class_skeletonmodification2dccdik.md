<span id="class_SkeletonModification2DCCDIK"></span>

## SkeletonModification2DCCDIK

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A modification that uses CCDIK to manipulate a series of bones to reach a target in 2D.

### Description

This [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) uses an algorithm called Cyclic Coordinate Descent Inverse Kinematics, or CCDIK, to manipulate a chain of bones in a [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) so it reaches a defined target.

CCDIK works by rotating a set of bones, typically called a "bone chain", on a single axis. Each bone is rotated to face the target from the tip (by default), which over a chain of bones allow it to rotate properly to reach the target. Because the bones only rotate on a single axis, CCDIK *can* look more robotic than other IK solvers.

 **Note:** The CCDIK modifier has `ccdik_joints`, which are the data objects that hold the data for each joint in the CCDIK chain. This is different from a bone! CCDIK joints hold the data needed for each bone in the bone chain used by CCDIK.

CCDIK also fully supports angle constraints, allowing for more control over how a solution is met.

### Properties


| [int](class_int.md#class_int) | [ccdik_data_chain_length](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_property_ccdik_data_chain_length) | `0` |
| --- | --- | --- |
| [NodePath](class_nodepath.md#class_NodePath) | [target_nodepath](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_property_target_nodepath) | `NodePath("")` |
| [NodePath](class_nodepath.md#class_NodePath) | [tip_nodepath](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_property_tip_nodepath) | `NodePath("")` |

### Methods


| [NodePath](class_nodepath.md#class_NodePath) | [get_ccdik_joint_bone2d_node](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone2d_node) ( joint_idx: [int](class_int.md#class_int) ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_ccdik_joint_bone_index](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone_index) ( joint_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_ccdik_joint_constraint_angle_invert](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_invert) ( joint_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_ccdik_joint_constraint_angle_max](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_max) ( joint_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_ccdik_joint_constraint_angle_min](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_min) ( joint_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_ccdik_joint_enable_constraint](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_enable_constraint) ( joint_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_ccdik_joint_rotate_from_joint](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_rotate_from_joint) ( joint_idx: [int](class_int.md#class_int) ) const |
| void | [set_ccdik_joint_bone2d_node](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone2d_node) ( joint_idx: [int](class_int.md#class_int), bone2d_nodepath: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_ccdik_joint_bone_index](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone_index) ( joint_idx: [int](class_int.md#class_int), bone_idx: [int](class_int.md#class_int) ) |
| void | [set_ccdik_joint_constraint_angle_invert](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_invert) ( joint_idx: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) ) |
| void | [set_ccdik_joint_constraint_angle_max](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_max) ( joint_idx: [int](class_int.md#class_int), angle_max: [float](class_float.md#class_float) ) |
| void | [set_ccdik_joint_constraint_angle_min](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_min) ( joint_idx: [int](class_int.md#class_int), angle_min: [float](class_float.md#class_float) ) |
| void | [set_ccdik_joint_enable_constraint](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_enable_constraint) ( joint_idx: [int](class_int.md#class_int), enable_constraint: [bool](class_bool.md#class_bool) ) |
| void | [set_ccdik_joint_rotate_from_joint](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_rotate_from_joint) ( joint_idx: [int](class_int.md#class_int), rotate_from_joint: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_SkeletonModification2DCCDIK_property_ccdik_data_chain_length"></span>

[int](class_int.md#class_int) **ccdik_data_chain_length** = `0` [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_property_ccdik_data_chain_length)

- void **set_ccdik_data_chain_length** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_ccdik_data_chain_length** ( )

The number of CCDIK joints in the CCDIK modification.

---

<span id="class_SkeletonModification2DCCDIK_property_target_nodepath"></span>

[NodePath](class_nodepath.md#class_NodePath) **target_nodepath** = `NodePath("")` [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_property_target_nodepath)

- void **set_target_node** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_target_node** ( )

The NodePath to the node that is the target for the CCDIK modification. This node is what the CCDIK chain will attempt to rotate the bone chain to.

---

<span id="class_SkeletonModification2DCCDIK_property_tip_nodepath"></span>

[NodePath](class_nodepath.md#class_NodePath) **tip_nodepath** = `NodePath("")` [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_property_tip_nodepath)

- void **set_tip_node** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_tip_node** ( )

The end position of the CCDIK chain. Typically, this should be a child of a [Bone2D](class_bone2d.md#class_Bone2D) node attached to the final [Bone2D](class_bone2d.md#class_Bone2D) in the CCDIK chain.

---

### Method Descriptions

<span id="class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone2d_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_ccdik_joint_bone2d_node** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone2d_node)

Returns the [Bone2D](class_bone2d.md#class_Bone2D) node assigned to the CCDIK joint at `joint_idx`.

---

<span id="class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone_index"></span>

[int](class_int.md#class_int) **get_ccdik_joint_bone_index** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone_index)

Returns the index of the [Bone2D](class_bone2d.md#class_Bone2D) node assigned to the CCDIK joint at `joint_idx`.

---

<span id="class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_invert"></span>

[bool](class_bool.md#class_bool) **get_ccdik_joint_constraint_angle_invert** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_invert)

Returns whether the CCDIK joint at `joint_idx` uses an inverted joint constraint. See [set_ccdik_joint_constraint_angle_invert()](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_invert) for details.

---

<span id="class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_max"></span>

[float](class_float.md#class_float) **get_ccdik_joint_constraint_angle_max** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_max)

Returns the maximum angle constraint for the joint at `joint_idx`.

---

<span id="class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_min"></span>

[float](class_float.md#class_float) **get_ccdik_joint_constraint_angle_min** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_min)

Returns the minimum angle constraint for the joint at `joint_idx`.

---

<span id="class_SkeletonModification2DCCDIK_method_get_ccdik_joint_enable_constraint"></span>

[bool](class_bool.md#class_bool) **get_ccdik_joint_enable_constraint** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_enable_constraint)

Returns whether angle constraints on the CCDIK joint at `joint_idx` are enabled.

---

<span id="class_SkeletonModification2DCCDIK_method_get_ccdik_joint_rotate_from_joint"></span>

[bool](class_bool.md#class_bool) **get_ccdik_joint_rotate_from_joint** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_rotate_from_joint)

Returns whether the joint at `joint_idx` is set to rotate from the joint, `true`, or to rotate from the tip, `false`. The default is to rotate from the tip.

---

<span id="class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone2d_node"></span>

void **set_ccdik_joint_bone2d_node** ( joint_idx: [int](class_int.md#class_int), bone2d_nodepath: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone2d_node)

Sets the [Bone2D](class_bone2d.md#class_Bone2D) node assigned to the CCDIK joint at `joint_idx`.

---

<span id="class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone_index"></span>

void **set_ccdik_joint_bone_index** ( joint_idx: [int](class_int.md#class_int), bone_idx: [int](class_int.md#class_int) ) [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone_index)

Sets the bone index, `bone_idx`, of the CCDIK joint at `joint_idx`. When possible, this will also update the `bone2d_node` of the CCDIK joint based on data provided by the linked skeleton.

---

<span id="class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_invert"></span>

void **set_ccdik_joint_constraint_angle_invert** ( joint_idx: [int](class_int.md#class_int), invert: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_invert)

Sets whether the CCDIK joint at `joint_idx` uses an inverted joint constraint.

An inverted joint constraint only constraints the CCDIK joint to the angles *outside of* the inputted minimum and maximum angles. For this reason, it is referred to as an inverted joint constraint, as it constraints the joint to the outside of the inputted values.

---

<span id="class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_max"></span>

void **set_ccdik_joint_constraint_angle_max** ( joint_idx: [int](class_int.md#class_int), angle_max: [float](class_float.md#class_float) ) [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_max)

Sets the maximum angle constraint for the joint at `joint_idx`.

---

<span id="class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_min"></span>

void **set_ccdik_joint_constraint_angle_min** ( joint_idx: [int](class_int.md#class_int), angle_min: [float](class_float.md#class_float) ) [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_min)

Sets the minimum angle constraint for the joint at `joint_idx`.

---

<span id="class_SkeletonModification2DCCDIK_method_set_ccdik_joint_enable_constraint"></span>

void **set_ccdik_joint_enable_constraint** ( joint_idx: [int](class_int.md#class_int), enable_constraint: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_enable_constraint)

Determines whether angle constraints on the CCDIK joint at `joint_idx` are enabled. When `true`, constraints will be enabled and taken into account when solving.

---

<span id="class_SkeletonModification2DCCDIK_method_set_ccdik_joint_rotate_from_joint"></span>

void **set_ccdik_joint_rotate_from_joint** ( joint_idx: [int](class_int.md#class_int), rotate_from_joint: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_rotate_from_joint)

Sets whether the joint at `joint_idx` is set to rotate from the joint, `true`, or to rotate from the tip, `false`.
