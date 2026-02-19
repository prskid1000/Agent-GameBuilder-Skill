<span id="class_ConvertTransformModifier3D"></span>

## ConvertTransformModifier3D

**Inherits:** [BoneConstraint3D](class_boneconstraint3d.md#class_BoneConstraint3D) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) that apply transform to the bone which converted from reference.

### Description

Apply the copied transform of the bone set by [BoneConstraint3D.set_reference_bone()](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_reference_bone) to the bone set by [BoneConstraint3D.set_apply_bone()](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_apply_bone) about the specific axis with remapping it with some options.

There are 4 ways to apply the transform, depending on the combination of [set_relative()](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_relative) and [set_additive()](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_additive).

 **Relative + Additive:**

- Extract reference pose relative to the rest and add it to the apply bone's pose.

 **Relative + Not Additive:**

- Extract reference pose relative to the rest and add it to the apply bone's rest.

 **Not Relative + Additive:**

- Extract reference pose absolutely and add it to the apply bone's pose.

 **Not Relative + Not Additive:**

- Extract reference pose absolutely and the apply bone's pose is replaced with it.

 **Note:** Relative option is available only in the case [BoneConstraint3D.get_reference_type()](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_type) is [BoneConstraint3D.REFERENCE_TYPE_BONE](class_boneconstraint3d.md#class_BoneConstraint3D_constant_REFERENCE_TYPE_BONE). See also [ReferenceType](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType).

 **Note:** If there is a rotation greater than `180` degrees with constrained axes, flipping may occur.

### Properties


| [int](class_int.md#class_int) | [setting_count](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_property_setting_count) | `0` |
| --- | --- | --- |

### Methods


| [Axis](class_vector3.md#enum_Vector3_Axis) | [get_apply_axis](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_apply_axis) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [float](class_float.md#class_float) | [get_apply_range_max](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_apply_range_max) ( index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_apply_range_min](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_apply_range_min) ( index: [int](class_int.md#class_int) ) const |
| [TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) | [get_apply_transform_mode](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_apply_transform_mode) ( index: [int](class_int.md#class_int) ) const |
| [Axis](class_vector3.md#enum_Vector3_Axis) | [get_reference_axis](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_reference_axis) ( index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_reference_range_max](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_reference_range_max) ( index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_reference_range_min](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_reference_range_min) ( index: [int](class_int.md#class_int) ) const |
| [TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) | [get_reference_transform_mode](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_reference_transform_mode) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_additive](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_is_additive) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_relative](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_is_relative) ( index: [int](class_int.md#class_int) ) const |
| void | [set_additive](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_additive) ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_apply_axis](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_apply_axis) ( index: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) ) |
| void | [set_apply_range_max](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_apply_range_max) ( index: [int](class_int.md#class_int), range_max: [float](class_float.md#class_float) ) |
| void | [set_apply_range_min](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_apply_range_min) ( index: [int](class_int.md#class_int), range_min: [float](class_float.md#class_float) ) |
| void | [set_apply_transform_mode](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_apply_transform_mode) ( index: [int](class_int.md#class_int), transform_mode: [TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) ) |
| void | [set_reference_axis](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_reference_axis) ( index: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) ) |
| void | [set_reference_range_max](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_reference_range_max) ( index: [int](class_int.md#class_int), range_max: [float](class_float.md#class_float) ) |
| void | [set_reference_range_min](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_reference_range_min) ( index: [int](class_int.md#class_int), range_min: [float](class_float.md#class_float) ) |
| void | [set_reference_transform_mode](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_reference_transform_mode) ( index: [int](class_int.md#class_int), transform_mode: [TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) ) |
| void | [set_relative](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_relative) ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |

---

### Enumerations

<span id="enum_ConvertTransformModifier3D_TransformMode"></span>

enum **TransformMode**: [🔗](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode)

<span id="class_ConvertTransformModifier3D_constant_TRANSFORM_MODE_POSITION"></span>

[TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) **TRANSFORM_MODE_POSITION** = `0`

Convert with position. Transfer the difference.

<span id="class_ConvertTransformModifier3D_constant_TRANSFORM_MODE_ROTATION"></span>

[TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) **TRANSFORM_MODE_ROTATION** = `1`

Convert with rotation. The angle is the roll for the specified axis.

<span id="class_ConvertTransformModifier3D_constant_TRANSFORM_MODE_SCALE"></span>

[TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) **TRANSFORM_MODE_SCALE** = `2`

Convert with scale. Transfers the ratio, not the difference.

---

### Property Descriptions

<span id="class_ConvertTransformModifier3D_property_setting_count"></span>

[int](class_int.md#class_int) **setting_count** = `0` [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_property_setting_count)

- void **set_setting_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_setting_count** ( )

The number of settings in the modifier.

---

### Method Descriptions

<span id="class_ConvertTransformModifier3D_method_get_apply_axis"></span>

[Axis](class_vector3.md#enum_Vector3_Axis) **get_apply_axis** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_apply_axis)

Returns the axis of the remapping destination transform.

---

<span id="class_ConvertTransformModifier3D_method_get_apply_range_max"></span>

[float](class_float.md#class_float) **get_apply_range_max** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_apply_range_max)

Returns the maximum value of the remapping destination range.

---

<span id="class_ConvertTransformModifier3D_method_get_apply_range_min"></span>

[float](class_float.md#class_float) **get_apply_range_min** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_apply_range_min)

Returns the minimum value of the remapping destination range.

---

<span id="class_ConvertTransformModifier3D_method_get_apply_transform_mode"></span>

[TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) **get_apply_transform_mode** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_apply_transform_mode)

Returns the operation of the remapping destination transform.

---

<span id="class_ConvertTransformModifier3D_method_get_reference_axis"></span>

[Axis](class_vector3.md#enum_Vector3_Axis) **get_reference_axis** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_reference_axis)

Returns the axis of the remapping source transform.

---

<span id="class_ConvertTransformModifier3D_method_get_reference_range_max"></span>

[float](class_float.md#class_float) **get_reference_range_max** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_reference_range_max)

Returns the maximum value of the remapping source range.

---

<span id="class_ConvertTransformModifier3D_method_get_reference_range_min"></span>

[float](class_float.md#class_float) **get_reference_range_min** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_reference_range_min)

Returns the minimum value of the remapping source range.

---

<span id="class_ConvertTransformModifier3D_method_get_reference_transform_mode"></span>

[TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) **get_reference_transform_mode** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_get_reference_transform_mode)

Returns the operation of the remapping source transform.

---

<span id="class_ConvertTransformModifier3D_method_is_additive"></span>

[bool](class_bool.md#class_bool) **is_additive** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_is_additive)

Returns `true` if the additive option is enabled in the setting at `index`.

---

<span id="class_ConvertTransformModifier3D_method_is_relative"></span>

[bool](class_bool.md#class_bool) **is_relative** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_is_relative)

Returns `true` if the relative option is enabled in the setting at `index`.

---

<span id="class_ConvertTransformModifier3D_method_set_additive"></span>

void **set_additive** ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_additive)

Sets additive option in the setting at `index` to `enabled`. This mainly affects the process of applying transform to the [BoneConstraint3D.set_apply_bone()](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_apply_bone).

If sets `enabled` to `true`, the processed transform is added to the pose of the current apply bone.

If sets `enabled` to `false`, the pose of the current apply bone is replaced with the processed transform. However, if set [set_relative()](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_relative) to `true`, the transform is relative to rest.

---

<span id="class_ConvertTransformModifier3D_method_set_apply_axis"></span>

void **set_apply_axis** ( index: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_apply_axis)

Sets the axis of the remapping destination transform.

---

<span id="class_ConvertTransformModifier3D_method_set_apply_range_max"></span>

void **set_apply_range_max** ( index: [int](class_int.md#class_int), range_max: [float](class_float.md#class_float) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_apply_range_max)

Sets the maximum value of the remapping destination range.

---

<span id="class_ConvertTransformModifier3D_method_set_apply_range_min"></span>

void **set_apply_range_min** ( index: [int](class_int.md#class_int), range_min: [float](class_float.md#class_float) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_apply_range_min)

Sets the minimum value of the remapping destination range.

---

<span id="class_ConvertTransformModifier3D_method_set_apply_transform_mode"></span>

void **set_apply_transform_mode** ( index: [int](class_int.md#class_int), transform_mode: [TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_apply_transform_mode)

Sets the operation of the remapping destination transform.

---

<span id="class_ConvertTransformModifier3D_method_set_reference_axis"></span>

void **set_reference_axis** ( index: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_reference_axis)

Sets the axis of the remapping source transform.

---

<span id="class_ConvertTransformModifier3D_method_set_reference_range_max"></span>

void **set_reference_range_max** ( index: [int](class_int.md#class_int), range_max: [float](class_float.md#class_float) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_reference_range_max)

Sets the maximum value of the remapping source range.

---

<span id="class_ConvertTransformModifier3D_method_set_reference_range_min"></span>

void **set_reference_range_min** ( index: [int](class_int.md#class_int), range_min: [float](class_float.md#class_float) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_reference_range_min)

Sets the minimum value of the remapping source range.

---

<span id="class_ConvertTransformModifier3D_method_set_reference_transform_mode"></span>

void **set_reference_transform_mode** ( index: [int](class_int.md#class_int), transform_mode: [TransformMode](class_converttransformmodifier3d.md#enum_ConvertTransformModifier3D_TransformMode) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_reference_transform_mode)

Sets the operation of the remapping source transform.

---

<span id="class_ConvertTransformModifier3D_method_set_relative"></span>

void **set_relative** ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D_method_set_relative)

Sets relative option in the setting at `index` to `enabled`.

If sets `enabled` to `true`, the extracted and applying transform is relative to the rest.

If sets `enabled` to `false`, the extracted transform is absolute.
