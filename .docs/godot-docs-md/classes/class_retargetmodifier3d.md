<span id="class_RetargetModifier3D"></span>

## RetargetModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A modifier to transfer parent skeleton poses (or global poses) to child skeletons in model space with different rests.

### Description

Retrieves the pose (or global pose) relative to the parent Skeleton's rest in model space and transfers it to the child Skeleton.

This modifier rewrites the pose of the child skeleton directly in the parent skeleton's update process. This means that it overwrites the mapped bone pose set in the normal process on the target skeleton. If you want to set the target skeleton bone pose after retargeting, you will need to add a [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) child to the target skeleton and thereby modify the pose.

 **Note:** When the [use_global_pose](class_retargetmodifier3d.md#class_RetargetModifier3D_property_use_global_pose) is enabled, even if it is an unmapped bone, it can cause visual problems because the global pose is applied ignoring the parent bone's pose **if it has mapped bone children**. See also [use_global_pose](class_retargetmodifier3d.md#class_RetargetModifier3D_property_use_global_pose).

### Properties


| bitfield | \[[TransformFlag](class_retargetmodifier3d.md#enum_RetargetModifier3D_TransformFlag)\] | [enable](class_retargetmodifier3d.md#class_RetargetModifier3D_property_enable) | `7` |
| --- | --- | --- | --- |
| [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) | [profile](class_retargetmodifier3d.md#class_RetargetModifier3D_property_profile) |
| [bool](class_bool.md#class_bool) | [use_global_pose](class_retargetmodifier3d.md#class_RetargetModifier3D_property_use_global_pose) | `false` |

### Methods


| [bool](class_bool.md#class_bool) | [is_position_enabled](class_retargetmodifier3d.md#class_RetargetModifier3D_method_is_position_enabled) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [is_rotation_enabled](class_retargetmodifier3d.md#class_RetargetModifier3D_method_is_rotation_enabled) ( ) const |
| [bool](class_bool.md#class_bool) | [is_scale_enabled](class_retargetmodifier3d.md#class_RetargetModifier3D_method_is_scale_enabled) ( ) const |
| void | [set_position_enabled](class_retargetmodifier3d.md#class_RetargetModifier3D_method_set_position_enabled) ( enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_rotation_enabled](class_retargetmodifier3d.md#class_RetargetModifier3D_method_set_rotation_enabled) ( enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_scale_enabled](class_retargetmodifier3d.md#class_RetargetModifier3D_method_set_scale_enabled) ( enabled: [bool](class_bool.md#class_bool) ) |

---

### Enumerations

<span id="enum_RetargetModifier3D_TransformFlag"></span>

flags **TransformFlag**: [🔗](class_retargetmodifier3d.md#enum_RetargetModifier3D_TransformFlag)

<span id="class_RetargetModifier3D_constant_TRANSFORM_FLAG_POSITION"></span>

[TransformFlag](class_retargetmodifier3d.md#enum_RetargetModifier3D_TransformFlag) **TRANSFORM_FLAG_POSITION** = `1`

If set, allows to retarget the position.

<span id="class_RetargetModifier3D_constant_TRANSFORM_FLAG_ROTATION"></span>

[TransformFlag](class_retargetmodifier3d.md#enum_RetargetModifier3D_TransformFlag) **TRANSFORM_FLAG_ROTATION** = `2`

If set, allows to retarget the rotation.

<span id="class_RetargetModifier3D_constant_TRANSFORM_FLAG_SCALE"></span>

[TransformFlag](class_retargetmodifier3d.md#enum_RetargetModifier3D_TransformFlag) **TRANSFORM_FLAG_SCALE** = `4`

If set, allows to retarget the scale.

<span id="class_RetargetModifier3D_constant_TRANSFORM_FLAG_ALL"></span>

[TransformFlag](class_retargetmodifier3d.md#enum_RetargetModifier3D_TransformFlag) **TRANSFORM_FLAG_ALL** = `7`

If set, allows to retarget the position/rotation/scale.

---

### Property Descriptions

<span id="class_RetargetModifier3D_property_enable"></span>

*BitField*\[[TransformFlag](class_retargetmodifier3d.md#enum_RetargetModifier3D_TransformFlag)\] **enable** = `7` [🔗](class_retargetmodifier3d.md#class_RetargetModifier3D_property_enable)

- void **set_enable_flags** ( value: *BitField*\[[TransformFlag](class_retargetmodifier3d.md#enum_RetargetModifier3D_TransformFlag)\] )
- *BitField*\[[TransformFlag](class_retargetmodifier3d.md#enum_RetargetModifier3D_TransformFlag)\] **get_enable_flags** ( )

Flags to control the process of the transform elements individually when [use_global_pose](class_retargetmodifier3d.md#class_RetargetModifier3D_property_use_global_pose) is disabled.

---

<span id="class_RetargetModifier3D_property_profile"></span>

[SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) **profile** [🔗](class_retargetmodifier3d.md#class_RetargetModifier3D_property_profile)

- void **set_profile** ( value: [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) )
- [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) **get_profile** ( )

[SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) for retargeting bones with names matching the bone list.

---

<span id="class_RetargetModifier3D_property_use_global_pose"></span>

[bool](class_bool.md#class_bool) **use_global_pose** = `false` [🔗](class_retargetmodifier3d.md#class_RetargetModifier3D_property_use_global_pose)

- void **set_use_global_pose** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_global_pose** ( )

If `false`, in case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform will be ignored.

Instead, it is possible to retarget between models with different body shapes, and position, rotation, and scale can be retargeted separately.

If `true`, retargeting is performed taking into account global pose.

In case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform is taken into account. However, bone length between skeletons must match exactly, if not, the bones will be forced to expand or shrink.

This is useful for using dummy bone with length `0` to match postures when retargeting between models with different number of bones.

---

### Method Descriptions

<span id="class_RetargetModifier3D_method_is_position_enabled"></span>

[bool](class_bool.md#class_bool) **is_position_enabled** ( ) *const* [🔗](class_retargetmodifier3d.md#class_RetargetModifier3D_method_is_position_enabled)

Returns `true` if [enable](class_retargetmodifier3d.md#class_RetargetModifier3D_property_enable) has [TRANSFORM_FLAG_POSITION](class_retargetmodifier3d.md#class_RetargetModifier3D_constant_TRANSFORM_FLAG_POSITION).

---

<span id="class_RetargetModifier3D_method_is_rotation_enabled"></span>

[bool](class_bool.md#class_bool) **is_rotation_enabled** ( ) *const* [🔗](class_retargetmodifier3d.md#class_RetargetModifier3D_method_is_rotation_enabled)

Returns `true` if [enable](class_retargetmodifier3d.md#class_RetargetModifier3D_property_enable) has [TRANSFORM_FLAG_ROTATION](class_retargetmodifier3d.md#class_RetargetModifier3D_constant_TRANSFORM_FLAG_ROTATION).

---

<span id="class_RetargetModifier3D_method_is_scale_enabled"></span>

[bool](class_bool.md#class_bool) **is_scale_enabled** ( ) *const* [🔗](class_retargetmodifier3d.md#class_RetargetModifier3D_method_is_scale_enabled)

Returns `true` if [enable](class_retargetmodifier3d.md#class_RetargetModifier3D_property_enable) has [TRANSFORM_FLAG_SCALE](class_retargetmodifier3d.md#class_RetargetModifier3D_constant_TRANSFORM_FLAG_SCALE).

---

<span id="class_RetargetModifier3D_method_set_position_enabled"></span>

void **set_position_enabled** ( enabled: [bool](class_bool.md#class_bool) ) [🔗](class_retargetmodifier3d.md#class_RetargetModifier3D_method_set_position_enabled)

Sets [TRANSFORM_FLAG_POSITION](class_retargetmodifier3d.md#class_RetargetModifier3D_constant_TRANSFORM_FLAG_POSITION) into [enable](class_retargetmodifier3d.md#class_RetargetModifier3D_property_enable).

---

<span id="class_RetargetModifier3D_method_set_rotation_enabled"></span>

void **set_rotation_enabled** ( enabled: [bool](class_bool.md#class_bool) ) [🔗](class_retargetmodifier3d.md#class_RetargetModifier3D_method_set_rotation_enabled)

Sets [TRANSFORM_FLAG_ROTATION](class_retargetmodifier3d.md#class_RetargetModifier3D_constant_TRANSFORM_FLAG_ROTATION) into [enable](class_retargetmodifier3d.md#class_RetargetModifier3D_property_enable).

---

<span id="class_RetargetModifier3D_method_set_scale_enabled"></span>

void **set_scale_enabled** ( enabled: [bool](class_bool.md#class_bool) ) [🔗](class_retargetmodifier3d.md#class_RetargetModifier3D_method_set_scale_enabled)

Sets [TRANSFORM_FLAG_SCALE](class_retargetmodifier3d.md#class_RetargetModifier3D_constant_TRANSFORM_FLAG_SCALE) into [enable](class_retargetmodifier3d.md#class_RetargetModifier3D_property_enable).
