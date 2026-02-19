<span id="class_OpenXRHand"></span>

## OpenXRHand

**Deprecated:** Use [XRHandModifier3D](class_xrhandmodifier3d.md#class_XRHandModifier3D) instead.

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Node supporting hand and finger tracking in OpenXR.

### Description

This node enables OpenXR's hand tracking functionality. The node should be a child node of an [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D) node, tracking will update its position to the player's tracked hand Palm joint location (the center of the middle finger's metacarpal bone). This node also updates the skeleton of a properly skinned hand or avatar model.

If the skeleton is a hand (one of the hand bones is the root node of the skeleton), then the skeleton will be placed relative to the hand palm location and the hand mesh and skeleton should be children of the OpenXRHand node.

If the hand bones are part of a full skeleton, then the root of the hand will keep its location with the assumption that IK is used to position the hand and arm.

By default the skeleton hand bones are repositioned to match the size of the tracked hand. To preserve the modeled bone sizes change [bone_update](class_openxrhand.md#class_OpenXRHand_property_bone_update) to apply rotation only.

### Properties


| [BoneUpdate](class_openxrhand.md#enum_OpenXRHand_BoneUpdate) | [bone_update](class_openxrhand.md#class_OpenXRHand_property_bone_update) | `0` |
| --- | --- | --- |
| [Hands](class_openxrhand.md#enum_OpenXRHand_Hands) | [hand](class_openxrhand.md#class_OpenXRHand_property_hand) | `0` |
| [NodePath](class_nodepath.md#class_NodePath) | [hand_skeleton](class_openxrhand.md#class_OpenXRHand_property_hand_skeleton) | `NodePath("")` |
| [MotionRange](class_openxrhand.md#enum_OpenXRHand_MotionRange) | [motion_range](class_openxrhand.md#class_OpenXRHand_property_motion_range) | `0` |
| [SkeletonRig](class_openxrhand.md#enum_OpenXRHand_SkeletonRig) | [skeleton_rig](class_openxrhand.md#class_OpenXRHand_property_skeleton_rig) | `0` |

---

### Enumerations

<span id="enum_OpenXRHand_Hands"></span>

enum **Hands**: [🔗](class_openxrhand.md#enum_OpenXRHand_Hands)

<span id="class_OpenXRHand_constant_HAND_LEFT"></span>

[Hands](class_openxrhand.md#enum_OpenXRHand_Hands) **HAND_LEFT** = `0`

Tracking the player's left hand.

<span id="class_OpenXRHand_constant_HAND_RIGHT"></span>

[Hands](class_openxrhand.md#enum_OpenXRHand_Hands) **HAND_RIGHT** = `1`

Tracking the player's right hand.

<span id="class_OpenXRHand_constant_HAND_MAX"></span>

[Hands](class_openxrhand.md#enum_OpenXRHand_Hands) **HAND_MAX** = `2`

Maximum supported hands.

---

<span id="enum_OpenXRHand_MotionRange"></span>

enum **MotionRange**: [🔗](class_openxrhand.md#enum_OpenXRHand_MotionRange)

<span id="class_OpenXRHand_constant_MOTION_RANGE_UNOBSTRUCTED"></span>

[MotionRange](class_openxrhand.md#enum_OpenXRHand_MotionRange) **MOTION_RANGE_UNOBSTRUCTED** = `0`

When player grips, hand skeleton will form a full fist.

<span id="class_OpenXRHand_constant_MOTION_RANGE_CONFORM_TO_CONTROLLER"></span>

[MotionRange](class_openxrhand.md#enum_OpenXRHand_MotionRange) **MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

When player grips, hand skeleton conforms to the controller the player is holding.

<span id="class_OpenXRHand_constant_MOTION_RANGE_MAX"></span>

[MotionRange](class_openxrhand.md#enum_OpenXRHand_MotionRange) **MOTION_RANGE_MAX** = `2`

Maximum supported motion ranges.

---

<span id="enum_OpenXRHand_SkeletonRig"></span>

enum **SkeletonRig**: [🔗](class_openxrhand.md#enum_OpenXRHand_SkeletonRig)

<span id="class_OpenXRHand_constant_SKELETON_RIG_OPENXR"></span>

[SkeletonRig](class_openxrhand.md#enum_OpenXRHand_SkeletonRig) **SKELETON_RIG_OPENXR** = `0`

An OpenXR compliant skeleton.

<span id="class_OpenXRHand_constant_SKELETON_RIG_HUMANOID"></span>

[SkeletonRig](class_openxrhand.md#enum_OpenXRHand_SkeletonRig) **SKELETON_RIG_HUMANOID** = `1`

A [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class_SkeletonProfileHumanoid) compliant skeleton.

<span id="class_OpenXRHand_constant_SKELETON_RIG_MAX"></span>

[SkeletonRig](class_openxrhand.md#enum_OpenXRHand_SkeletonRig) **SKELETON_RIG_MAX** = `2`

Maximum supported hands.

---

<span id="enum_OpenXRHand_BoneUpdate"></span>

enum **BoneUpdate**: [🔗](class_openxrhand.md#enum_OpenXRHand_BoneUpdate)

<span id="class_OpenXRHand_constant_BONE_UPDATE_FULL"></span>

[BoneUpdate](class_openxrhand.md#enum_OpenXRHand_BoneUpdate) **BONE_UPDATE_FULL** = `0`

The skeletons bones are fully updated (both position and rotation) to match the tracked bones.

<span id="class_OpenXRHand_constant_BONE_UPDATE_ROTATION_ONLY"></span>

[BoneUpdate](class_openxrhand.md#enum_OpenXRHand_BoneUpdate) **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeletons bones are only rotated to align with the tracked bones, preserving bone length.

<span id="class_OpenXRHand_constant_BONE_UPDATE_MAX"></span>

[BoneUpdate](class_openxrhand.md#enum_OpenXRHand_BoneUpdate) **BONE_UPDATE_MAX** = `2`

Maximum supported bone update mode.

---

### Property Descriptions

<span id="class_OpenXRHand_property_bone_update"></span>

[BoneUpdate](class_openxrhand.md#enum_OpenXRHand_BoneUpdate) **bone_update** = `0` [🔗](class_openxrhand.md#class_OpenXRHand_property_bone_update)

- void **set_bone_update** ( value: [BoneUpdate](class_openxrhand.md#enum_OpenXRHand_BoneUpdate) )
- [BoneUpdate](class_openxrhand.md#enum_OpenXRHand_BoneUpdate) **get_bone_update** ( )

Specify the type of updates to perform on the bone.

---

<span id="class_OpenXRHand_property_hand"></span>

[Hands](class_openxrhand.md#enum_OpenXRHand_Hands) **hand** = `0` [🔗](class_openxrhand.md#class_OpenXRHand_property_hand)

- void **set_hand** ( value: [Hands](class_openxrhand.md#enum_OpenXRHand_Hands) )
- [Hands](class_openxrhand.md#enum_OpenXRHand_Hands) **get_hand** ( )

Specifies whether this node tracks the left or right hand of the player.

---

<span id="class_OpenXRHand_property_hand_skeleton"></span>

[NodePath](class_nodepath.md#class_NodePath) **hand_skeleton** = `NodePath("")` [🔗](class_openxrhand.md#class_OpenXRHand_property_hand_skeleton)

- void **set_hand_skeleton** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_hand_skeleton** ( )

Set a [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) node for which the pose positions will be updated.

---

<span id="class_OpenXRHand_property_motion_range"></span>

[MotionRange](class_openxrhand.md#enum_OpenXRHand_MotionRange) **motion_range** = `0` [🔗](class_openxrhand.md#class_OpenXRHand_property_motion_range)

- void **set_motion_range** ( value: [MotionRange](class_openxrhand.md#enum_OpenXRHand_MotionRange) )
- [MotionRange](class_openxrhand.md#enum_OpenXRHand_MotionRange) **get_motion_range** ( )

Set the motion range (if supported) limiting the hand motion.

---

<span id="class_OpenXRHand_property_skeleton_rig"></span>

[SkeletonRig](class_openxrhand.md#enum_OpenXRHand_SkeletonRig) **skeleton_rig** = `0` [🔗](class_openxrhand.md#class_OpenXRHand_property_skeleton_rig)

- void **set_skeleton_rig** ( value: [SkeletonRig](class_openxrhand.md#enum_OpenXRHand_SkeletonRig) )
- [SkeletonRig](class_openxrhand.md#enum_OpenXRHand_SkeletonRig) **get_skeleton_rig** ( )

Set the type of skeleton rig the [hand_skeleton](class_openxrhand.md#class_OpenXRHand_property_hand_skeleton) is compliant with.
