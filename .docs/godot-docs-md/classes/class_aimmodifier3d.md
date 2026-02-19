<span id="class_AimModifier3D"></span>

## AimModifier3D

**Inherits:** [BoneConstraint3D](class_boneconstraint3d.md#class_BoneConstraint3D) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

The **AimModifier3D** rotates a bone to look at a reference bone.

### Description

This is a simple version of [LookAtModifier3D](class_lookatmodifier3d.md#class_LookAtModifier3D) that only allows bone to the reference without advanced options such as angle limitation or time-based interpolation.

The feature is simplified, but instead it is implemented with smooth tracking without euler, see [set_use_euler()](class_aimmodifier3d.md#class_AimModifier3D_method_set_use_euler).

### Properties


| [int](class_int.md#class_int) | [setting_count](class_aimmodifier3d.md#class_AimModifier3D_property_setting_count) | `0` |
| --- | --- | --- |

### Methods


| [BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) | [get_forward_axis](class_aimmodifier3d.md#class_AimModifier3D_method_get_forward_axis) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [Axis](class_vector3.md#enum_Vector3_Axis) | [get_primary_rotation_axis](class_aimmodifier3d.md#class_AimModifier3D_method_get_primary_rotation_axis) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_relative](class_aimmodifier3d.md#class_AimModifier3D_method_is_relative) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_using_euler](class_aimmodifier3d.md#class_AimModifier3D_method_is_using_euler) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_using_secondary_rotation](class_aimmodifier3d.md#class_AimModifier3D_method_is_using_secondary_rotation) ( index: [int](class_int.md#class_int) ) const |
| void | [set_forward_axis](class_aimmodifier3d.md#class_AimModifier3D_method_set_forward_axis) ( index: [int](class_int.md#class_int), axis: [BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) ) |
| void | [set_primary_rotation_axis](class_aimmodifier3d.md#class_AimModifier3D_method_set_primary_rotation_axis) ( index: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) ) |
| void | [set_relative](class_aimmodifier3d.md#class_AimModifier3D_method_set_relative) ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_use_euler](class_aimmodifier3d.md#class_AimModifier3D_method_set_use_euler) ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_use_secondary_rotation](class_aimmodifier3d.md#class_AimModifier3D_method_set_use_secondary_rotation) ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_AimModifier3D_property_setting_count"></span>

[int](class_int.md#class_int) **setting_count** = `0` [🔗](class_aimmodifier3d.md#class_AimModifier3D_property_setting_count)

- void **set_setting_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_setting_count** ( )

The number of settings in the modifier.

---

### Method Descriptions

<span id="class_AimModifier3D_method_get_forward_axis"></span>

[BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) **get_forward_axis** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_get_forward_axis)

Returns the forward axis of the bone.

---

<span id="class_AimModifier3D_method_get_primary_rotation_axis"></span>

[Axis](class_vector3.md#enum_Vector3_Axis) **get_primary_rotation_axis** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_get_primary_rotation_axis)

Returns the axis of the first rotation. It is enabled only if [is_using_euler()](class_aimmodifier3d.md#class_AimModifier3D_method_is_using_euler) is `true`.

---

<span id="class_AimModifier3D_method_is_relative"></span>

[bool](class_bool.md#class_bool) **is_relative** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_is_relative)

Returns `true` if the relative option is enabled in the setting at `index`.

---

<span id="class_AimModifier3D_method_is_using_euler"></span>

[bool](class_bool.md#class_bool) **is_using_euler** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_is_using_euler)

Returns `true` if it provides rotation with using euler.

---

<span id="class_AimModifier3D_method_is_using_secondary_rotation"></span>

[bool](class_bool.md#class_bool) **is_using_secondary_rotation** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_is_using_secondary_rotation)

Returns `true` if it provides rotation by two axes. It is enabled only if [is_using_euler()](class_aimmodifier3d.md#class_AimModifier3D_method_is_using_euler) is `true`.

---

<span id="class_AimModifier3D_method_set_forward_axis"></span>

void **set_forward_axis** ( index: [int](class_int.md#class_int), axis: [BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) ) [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_set_forward_axis)

Sets the forward axis of the bone.

---

<span id="class_AimModifier3D_method_set_primary_rotation_axis"></span>

void **set_primary_rotation_axis** ( index: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) ) [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_set_primary_rotation_axis)

Sets the axis of the first rotation. It is enabled only if [is_using_euler()](class_aimmodifier3d.md#class_AimModifier3D_method_is_using_euler) is `true`.

---

<span id="class_AimModifier3D_method_set_relative"></span>

void **set_relative** ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_set_relative)

Sets relative option in the setting at `index` to `enabled`.

If sets `enabled` to `true`, the rotation is applied relative to the pose.

If sets `enabled` to `false`, the rotation is applied relative to the rest. It means to replace the current pose with the **AimModifier3D**'s result.

---

<span id="class_AimModifier3D_method_set_use_euler"></span>

void **set_use_euler** ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_set_use_euler)

If sets `enabled` to `true`, it provides rotation with using euler.

If sets `enabled` to `false`, it provides rotation with using rotation by arc generated from the forward axis vector and the vector toward the reference.

---

<span id="class_AimModifier3D_method_set_use_secondary_rotation"></span>

void **set_use_secondary_rotation** ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_aimmodifier3d.md#class_AimModifier3D_method_set_use_secondary_rotation)

If sets `enabled` to `true`, it provides rotation by two axes. It is enabled only if [is_using_euler()](class_aimmodifier3d.md#class_AimModifier3D_method_is_using_euler) is `true`.
