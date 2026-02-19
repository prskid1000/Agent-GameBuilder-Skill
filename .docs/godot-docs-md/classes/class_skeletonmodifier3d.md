<span id="class_SkeletonModifier3D"></span>

## SkeletonModifier3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [BoneConstraint3D](class_boneconstraint3d.md#class_BoneConstraint3D), [BoneTwistDisperser3D](class_bonetwistdisperser3d.md#class_BoneTwistDisperser3D), [IKModifier3D](class_ikmodifier3d.md#class_IKModifier3D), [LimitAngularVelocityModifier3D](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D), [LookAtModifier3D](class_lookatmodifier3d.md#class_LookAtModifier3D), [ModifierBoneTarget3D](class_modifierbonetarget3d.md#class_ModifierBoneTarget3D), [PhysicalBoneSimulator3D](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D), [RetargetModifier3D](class_retargetmodifier3d.md#class_RetargetModifier3D), [SkeletonIK3D](class_skeletonik3d.md#class_SkeletonIK3D), [SpringBoneSimulator3D](class_springbonesimulator3d.md#class_SpringBoneSimulator3D), [XRBodyModifier3D](class_xrbodymodifier3d.md#class_XRBodyModifier3D), [XRHandModifier3D](class_xrhandmodifier3d.md#class_XRHandModifier3D)

A node that may modify a Skeleton3D's bones.

### Description

**SkeletonModifier3D** retrieves a target [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) by having a [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) parent.

If there is an [AnimationMixer](class_animationmixer.md#class_AnimationMixer), a modification always performs after playback process of the [AnimationMixer](class_animationmixer.md#class_AnimationMixer).

This node should be used to implement custom IK solvers, constraints, or skeleton physics.

### Tutorials

- Design of the Skeleton Modifier 3D

### Properties


| [bool](class_bool.md#class_bool) | [active](class_skeletonmodifier3d.md#class_SkeletonModifier3D_property_active) | `true` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [influence](class_skeletonmodifier3d.md#class_SkeletonModifier3D_property_influence) | `1.0` |

### Methods


| void | [_process_modification](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__process_modification) ( ) virtual |
| --- | --- |
| void | [_process_modification_with_delta](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__process_modification_with_delta) ( delta: [float](class_float.md#class_float) ) virtual |
| void | [_skeleton_changed](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__skeleton_changed) ( old_skeleton: [Skeleton3D](class_skeleton3d.md#class_Skeleton3D), new_skeleton: [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) ) virtual |
| void | [_validate_bone_names](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__validate_bone_names) ( ) virtual |
| [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) | [get_skeleton](class_skeletonmodifier3d.md#class_SkeletonModifier3D_method_get_skeleton) ( ) const |

---

### Signals

<span id="class_SkeletonModifier3D_signal_modification_processed"></span>

**modification_processed** ( ) [🔗](class_skeletonmodifier3d.md#class_SkeletonModifier3D_signal_modification_processed)

Notifies when the modification have been finished.

 **Note:** If you want to get the modified bone pose by the modifier, you must use [Skeleton3D.get_bone_pose()](class_skeleton3d.md#class_Skeleton3D_method_get_bone_pose) or [Skeleton3D.get_bone_global_pose()](class_skeleton3d.md#class_Skeleton3D_method_get_bone_global_pose) at the moment this signal is fired.

---

### Enumerations

<span id="enum_SkeletonModifier3D_BoneAxis"></span>

enum **BoneAxis**: [🔗](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis)

<span id="class_SkeletonModifier3D_constant_BONE_AXIS_PLUS_X"></span>

[BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) **BONE_AXIS_PLUS_X** = `0`

Enumerated value for the +X axis.

<span id="class_SkeletonModifier3D_constant_BONE_AXIS_MINUS_X"></span>

[BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) **BONE_AXIS_MINUS_X** = `1`

Enumerated value for the -X axis.

<span id="class_SkeletonModifier3D_constant_BONE_AXIS_PLUS_Y"></span>

[BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) **BONE_AXIS_PLUS_Y** = `2`

Enumerated value for the +Y axis.

<span id="class_SkeletonModifier3D_constant_BONE_AXIS_MINUS_Y"></span>

[BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) **BONE_AXIS_MINUS_Y** = `3`

Enumerated value for the -Y axis.

<span id="class_SkeletonModifier3D_constant_BONE_AXIS_PLUS_Z"></span>

[BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) **BONE_AXIS_PLUS_Z** = `4`

Enumerated value for the +Z axis.

<span id="class_SkeletonModifier3D_constant_BONE_AXIS_MINUS_Z"></span>

[BoneAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneAxis) **BONE_AXIS_MINUS_Z** = `5`

Enumerated value for the -Z axis.

---

<span id="enum_SkeletonModifier3D_BoneDirection"></span>

enum **BoneDirection**: [🔗](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection)

<span id="class_SkeletonModifier3D_constant_BONE_DIRECTION_PLUS_X"></span>

[BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) **BONE_DIRECTION_PLUS_X** = `0`

Enumerated value for the +X axis.

<span id="class_SkeletonModifier3D_constant_BONE_DIRECTION_MINUS_X"></span>

[BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) **BONE_DIRECTION_MINUS_X** = `1`

Enumerated value for the -X axis.

<span id="class_SkeletonModifier3D_constant_BONE_DIRECTION_PLUS_Y"></span>

[BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) **BONE_DIRECTION_PLUS_Y** = `2`

Enumerated value for the +Y axis.

<span id="class_SkeletonModifier3D_constant_BONE_DIRECTION_MINUS_Y"></span>

[BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) **BONE_DIRECTION_MINUS_Y** = `3`

Enumerated value for the -Y axis.

<span id="class_SkeletonModifier3D_constant_BONE_DIRECTION_PLUS_Z"></span>

[BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) **BONE_DIRECTION_PLUS_Z** = `4`

Enumerated value for the +Z axis.

<span id="class_SkeletonModifier3D_constant_BONE_DIRECTION_MINUS_Z"></span>

[BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) **BONE_DIRECTION_MINUS_Z** = `5`

Enumerated value for the -Z axis.

<span id="class_SkeletonModifier3D_constant_BONE_DIRECTION_FROM_PARENT"></span>

[BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) **BONE_DIRECTION_FROM_PARENT** = `6`

Enumerated value for the axis from a parent bone to the child bone.

---

<span id="enum_SkeletonModifier3D_SecondaryDirection"></span>

enum **SecondaryDirection**: [🔗](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection)

<span id="class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_NONE"></span>

[SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) **SECONDARY_DIRECTION_NONE** = `0`

Enumerated value for the case when the axis is undefined.

<span id="class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_PLUS_X"></span>

[SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) **SECONDARY_DIRECTION_PLUS_X** = `1`

Enumerated value for the +X axis.

<span id="class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_MINUS_X"></span>

[SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) **SECONDARY_DIRECTION_MINUS_X** = `2`

Enumerated value for the -X axis.

<span id="class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_PLUS_Y"></span>

[SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) **SECONDARY_DIRECTION_PLUS_Y** = `3`

Enumerated value for the +Y axis.

<span id="class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_MINUS_Y"></span>

[SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) **SECONDARY_DIRECTION_MINUS_Y** = `4`

Enumerated value for the -Y axis.

<span id="class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_PLUS_Z"></span>

[SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) **SECONDARY_DIRECTION_PLUS_Z** = `5`

Enumerated value for the +Z axis.

<span id="class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_MINUS_Z"></span>

[SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) **SECONDARY_DIRECTION_MINUS_Z** = `6`

Enumerated value for the -Z axis.

<span id="class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_CUSTOM"></span>

[SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) **SECONDARY_DIRECTION_CUSTOM** = `7`

Enumerated value for an optional axis.

---

<span id="enum_SkeletonModifier3D_RotationAxis"></span>

enum **RotationAxis**: [🔗](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_RotationAxis)

<span id="class_SkeletonModifier3D_constant_ROTATION_AXIS_X"></span>

[RotationAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_RotationAxis) **ROTATION_AXIS_X** = `0`

Enumerated value for the rotation of the X axis.

<span id="class_SkeletonModifier3D_constant_ROTATION_AXIS_Y"></span>

[RotationAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_RotationAxis) **ROTATION_AXIS_Y** = `1`

Enumerated value for the rotation of the Y axis.

<span id="class_SkeletonModifier3D_constant_ROTATION_AXIS_Z"></span>

[RotationAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_RotationAxis) **ROTATION_AXIS_Z** = `2`

Enumerated value for the rotation of the Z axis.

<span id="class_SkeletonModifier3D_constant_ROTATION_AXIS_ALL"></span>

[RotationAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_RotationAxis) **ROTATION_AXIS_ALL** = `3`

Enumerated value for the unconstrained rotation.

<span id="class_SkeletonModifier3D_constant_ROTATION_AXIS_CUSTOM"></span>

[RotationAxis](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_RotationAxis) **ROTATION_AXIS_CUSTOM** = `4`

Enumerated value for an optional rotation axis.

---

### Property Descriptions

<span id="class_SkeletonModifier3D_property_active"></span>

[bool](class_bool.md#class_bool) **active** = `true` [🔗](class_skeletonmodifier3d.md#class_SkeletonModifier3D_property_active)

- void **set_active** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_active** ( )

If `true`, the **SkeletonModifier3D** will be processing.

---

<span id="class_SkeletonModifier3D_property_influence"></span>

[float](class_float.md#class_float) **influence** = `1.0` [🔗](class_skeletonmodifier3d.md#class_SkeletonModifier3D_property_influence)

- void **set_influence** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_influence** ( )

Sets the influence of the modification.

 **Note:** This value is used by [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) to blend, so the **SkeletonModifier3D** should always apply only 100% of the result without interpolation.

---

### Method Descriptions

<span id="class_SkeletonModifier3D_private_method__process_modification"></span>

void **_process_modification** ( ) *virtual* [🔗](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__process_modification)

**Deprecated:** Use [_process_modification_with_delta()](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__process_modification_with_delta) instead.

Override this virtual method to implement a custom skeleton modifier. You should do things like get the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D)'s current pose and apply the pose here.

 [_process_modification()](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__process_modification) must not apply [influence](class_skeletonmodifier3d.md#class_SkeletonModifier3D_property_influence) to bone poses because the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) automatically applies influence to all bone poses set by the modifier.

---

<span id="class_SkeletonModifier3D_private_method__process_modification_with_delta"></span>

void **_process_modification_with_delta** ( delta: [float](class_float.md#class_float) ) *virtual* [🔗](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__process_modification_with_delta)

Override this virtual method to implement a custom skeleton modifier. You should do things like get the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D)'s current pose and apply the pose here.

 [_process_modification_with_delta()](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__process_modification_with_delta) must not apply [influence](class_skeletonmodifier3d.md#class_SkeletonModifier3D_property_influence) to bone poses because the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) automatically applies influence to all bone poses set by the modifier.

 `delta` is passed from parent [Skeleton3D](class_skeleton3d.md#class_Skeleton3D). See also [Skeleton3D.advance()](class_skeleton3d.md#class_Skeleton3D_method_advance).

 **Note:** This method may be called outside [Node._process()](class_node.md#class_Node_private_method__process) and [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) with `delta` is `0.0`, since the modification should be processed immediately after initialization of the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D).

---

<span id="class_SkeletonModifier3D_private_method__skeleton_changed"></span>

void **_skeleton_changed** ( old_skeleton: [Skeleton3D](class_skeleton3d.md#class_Skeleton3D), new_skeleton: [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) ) *virtual* [🔗](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__skeleton_changed)

Called when the skeleton is changed.

---

<span id="class_SkeletonModifier3D_private_method__validate_bone_names"></span>

void **_validate_bone_names** ( ) *virtual* [🔗](class_skeletonmodifier3d.md#class_SkeletonModifier3D_private_method__validate_bone_names)

Called when bone names and indices need to be validated, such as when entering the scene tree or changing skeleton.

---

<span id="class_SkeletonModifier3D_method_get_skeleton"></span>

[Skeleton3D](class_skeleton3d.md#class_Skeleton3D) **get_skeleton** ( ) *const* [🔗](class_skeletonmodifier3d.md#class_SkeletonModifier3D_method_get_skeleton)

Returns the parent [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) node if it exists. Otherwise, returns `null`.
