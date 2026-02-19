<span id="class_XRHandModifier3D"></span>

## XRHandModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node for driving hand meshes from [XRHandTracker](class_xrhandtracker.md#class_XRHandTracker) data.

### Description

This node uses hand tracking data from an [XRHandTracker](class_xrhandtracker.md#class_XRHandTracker) to pose the skeleton of a hand mesh.

Positioning of hands is performed by creating an [XRNode3D](class_xrnode3d.md#class_XRNode3D) ancestor of the hand mesh driven by the same [XRHandTracker](class_xrhandtracker.md#class_XRHandTracker).

The hand tracking position-data is scaled by [Skeleton3D.motion_scale](class_skeleton3d.md#class_Skeleton3D_property_motion_scale) when applied to the skeleton, which can be used to adjust the tracked hand to match the scale of the hand model.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [BoneUpdate](class_xrhandmodifier3d.md#enum_XRHandModifier3D_BoneUpdate) | [bone_update](class_xrhandmodifier3d.md#class_XRHandModifier3D_property_bone_update) | `0` |
| --- | --- | --- |
| [StringName](class_stringname.md#class_StringName) | [hand_tracker](class_xrhandmodifier3d.md#class_XRHandModifier3D_property_hand_tracker) | `&"/user/hand_tracker/left"` |

---

### Enumerations

<span id="enum_XRHandModifier3D_BoneUpdate"></span>

enum **BoneUpdate**: [🔗](class_xrhandmodifier3d.md#enum_XRHandModifier3D_BoneUpdate)

<span id="class_XRHandModifier3D_constant_BONE_UPDATE_FULL"></span>

[BoneUpdate](class_xrhandmodifier3d.md#enum_XRHandModifier3D_BoneUpdate) **BONE_UPDATE_FULL** = `0`

The skeleton's bones are fully updated (both position and rotation) to match the tracked bones.

<span id="class_XRHandModifier3D_constant_BONE_UPDATE_ROTATION_ONLY"></span>

[BoneUpdate](class_xrhandmodifier3d.md#enum_XRHandModifier3D_BoneUpdate) **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton's bones are only rotated to align with the tracked bones, preserving bone length.

<span id="class_XRHandModifier3D_constant_BONE_UPDATE_MAX"></span>

[BoneUpdate](class_xrhandmodifier3d.md#enum_XRHandModifier3D_BoneUpdate) **BONE_UPDATE_MAX** = `2`

Represents the size of the [BoneUpdate](class_xrhandmodifier3d.md#enum_XRHandModifier3D_BoneUpdate) enum.

---

### Property Descriptions

<span id="class_XRHandModifier3D_property_bone_update"></span>

[BoneUpdate](class_xrhandmodifier3d.md#enum_XRHandModifier3D_BoneUpdate) **bone_update** = `0` [🔗](class_xrhandmodifier3d.md#class_XRHandModifier3D_property_bone_update)

- void **set_bone_update** ( value: [BoneUpdate](class_xrhandmodifier3d.md#enum_XRHandModifier3D_BoneUpdate) )
- [BoneUpdate](class_xrhandmodifier3d.md#enum_XRHandModifier3D_BoneUpdate) **get_bone_update** ( )

Specifies the type of updates to perform on the bones.

---

<span id="class_XRHandModifier3D_property_hand_tracker"></span>

[StringName](class_stringname.md#class_StringName) **hand_tracker** = `&"/user/hand_tracker/left"` [🔗](class_xrhandmodifier3d.md#class_XRHandModifier3D_property_hand_tracker)

- void **set_hand_tracker** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_hand_tracker** ( )

The name of the [XRHandTracker](class_xrhandtracker.md#class_XRHandTracker) registered with [XRServer](class_xrserver.md#class_XRServer) to obtain the hand tracking data from.
