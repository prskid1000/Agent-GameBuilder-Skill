<span id="class_SkeletonModification2DLookAt"></span>

## SkeletonModification2DLookAt

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A modification that rotates a [Bone2D](class_bone2d.md#class_Bone2D) node to look at a target.

### Description

This [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) rotates a bone to look a target. This is extremely helpful for moving character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

### Properties


| [NodePath](class_nodepath.md#class_NodePath) | [bone2d_node](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_property_bone2d_node) | `NodePath("")` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [bone_index](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_property_bone_index) | `-1` |
| [NodePath](class_nodepath.md#class_NodePath) | [target_nodepath](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_property_target_nodepath) | `NodePath("")` |

### Methods


| [float](class_float.md#class_float) | [get_additional_rotation](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_additional_rotation) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [get_constraint_angle_invert](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_constraint_angle_invert) ( ) const |
| [float](class_float.md#class_float) | [get_constraint_angle_max](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_constraint_angle_max) ( ) const |
| [float](class_float.md#class_float) | [get_constraint_angle_min](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_constraint_angle_min) ( ) const |
| [bool](class_bool.md#class_bool) | [get_enable_constraint](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_enable_constraint) ( ) const |
| void | [set_additional_rotation](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_additional_rotation) ( rotation: [float](class_float.md#class_float) ) |
| void | [set_constraint_angle_invert](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_constraint_angle_invert) ( invert: [bool](class_bool.md#class_bool) ) |
| void | [set_constraint_angle_max](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_constraint_angle_max) ( angle_max: [float](class_float.md#class_float) ) |
| void | [set_constraint_angle_min](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_constraint_angle_min) ( angle_min: [float](class_float.md#class_float) ) |
| void | [set_enable_constraint](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_enable_constraint) ( enable_constraint: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_SkeletonModification2DLookAt_property_bone2d_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **bone2d_node** = `NodePath("")` [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_property_bone2d_node)

- void **set_bone2d_node** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_bone2d_node** ( )

The [Bone2D](class_bone2d.md#class_Bone2D) node that the modification will operate on.

---

<span id="class_SkeletonModification2DLookAt_property_bone_index"></span>

[int](class_int.md#class_int) **bone_index** = `-1` [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_property_bone_index)

- void **set_bone_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bone_index** ( )

The index of the [Bone2D](class_bone2d.md#class_Bone2D) node that the modification will operate on.

---

<span id="class_SkeletonModification2DLookAt_property_target_nodepath"></span>

[NodePath](class_nodepath.md#class_NodePath) **target_nodepath** = `NodePath("")` [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_property_target_nodepath)

- void **set_target_node** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_target_node** ( )

The NodePath to the node that is the target for the LookAt modification. This node is what the modification will rotate the [Bone2D](class_bone2d.md#class_Bone2D) to.

---

### Method Descriptions

<span id="class_SkeletonModification2DLookAt_method_get_additional_rotation"></span>

[float](class_float.md#class_float) **get_additional_rotation** ( ) *const* [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_additional_rotation)

Returns the amount of additional rotation that is applied after the LookAt modification executes.

---

<span id="class_SkeletonModification2DLookAt_method_get_constraint_angle_invert"></span>

[bool](class_bool.md#class_bool) **get_constraint_angle_invert** ( ) *const* [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_constraint_angle_invert)

Returns whether the constraints to this modification are inverted or not.

---

<span id="class_SkeletonModification2DLookAt_method_get_constraint_angle_max"></span>

[float](class_float.md#class_float) **get_constraint_angle_max** ( ) *const* [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_constraint_angle_max)

Returns the constraint's maximum allowed angle.

---

<span id="class_SkeletonModification2DLookAt_method_get_constraint_angle_min"></span>

[float](class_float.md#class_float) **get_constraint_angle_min** ( ) *const* [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_constraint_angle_min)

Returns the constraint's minimum allowed angle.

---

<span id="class_SkeletonModification2DLookAt_method_get_enable_constraint"></span>

[bool](class_bool.md#class_bool) **get_enable_constraint** ( ) *const* [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_get_enable_constraint)

Returns `true` if the LookAt modification is using constraints.

---

<span id="class_SkeletonModification2DLookAt_method_set_additional_rotation"></span>

void **set_additional_rotation** ( rotation: [float](class_float.md#class_float) ) [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_additional_rotation)

Sets the amount of additional rotation that is to be applied after executing the modification. This allows for offsetting the results by the inputted rotation amount.

---

<span id="class_SkeletonModification2DLookAt_method_set_constraint_angle_invert"></span>

void **set_constraint_angle_invert** ( invert: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_constraint_angle_invert)

When `true`, the modification will use an inverted joint constraint.

An inverted joint constraint only constraints the [Bone2D](class_bone2d.md#class_Bone2D) to the angles *outside of* the inputted minimum and maximum angles. For this reason, it is referred to as an inverted joint constraint, as it constraints the joint to the outside of the inputted values.

---

<span id="class_SkeletonModification2DLookAt_method_set_constraint_angle_max"></span>

void **set_constraint_angle_max** ( angle_max: [float](class_float.md#class_float) ) [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_constraint_angle_max)

Sets the constraint's maximum allowed angle.

---

<span id="class_SkeletonModification2DLookAt_method_set_constraint_angle_min"></span>

void **set_constraint_angle_min** ( angle_min: [float](class_float.md#class_float) ) [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_constraint_angle_min)

Sets the constraint's minimum allowed angle.

---

<span id="class_SkeletonModification2DLookAt_method_set_enable_constraint"></span>

void **set_enable_constraint** ( enable_constraint: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt_method_set_enable_constraint)

Sets whether this modification will use constraints or not. When `true`, constraints will be applied when solving the LookAt modification.
