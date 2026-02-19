<span id="class_XRBodyModifier3D"></span>

## XRBodyModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node for driving body meshes from [XRBodyTracker](class_xrbodytracker.md#class_XRBodyTracker) data.

### Description

This node uses body tracking data from an [XRBodyTracker](class_xrbodytracker.md#class_XRBodyTracker) to pose the skeleton of a body mesh.

Positioning of the body is performed by creating an [XRNode3D](class_xrnode3d.md#class_XRNode3D) ancestor of the body mesh driven by the same [XRBodyTracker](class_xrbodytracker.md#class_XRBodyTracker).

The body tracking position-data is scaled by [Skeleton3D.motion_scale](class_skeleton3d.md#class_Skeleton3D_property_motion_scale) when applied to the skeleton, which can be used to adjust the tracked body to match the scale of the body model.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [StringName](class_stringname.md#class_StringName) | [body_tracker](class_xrbodymodifier3d.md#class_XRBodyModifier3D_property_body_tracker) | `&"/user/body_tracker"` |
| --- | --- | --- |
| bitfield | \[[BodyUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BodyUpdate)\] | [body_update](class_xrbodymodifier3d.md#class_XRBodyModifier3D_property_body_update) | `7` |
| [BoneUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BoneUpdate) | [bone_update](class_xrbodymodifier3d.md#class_XRBodyModifier3D_property_bone_update) | `0` |

---

### Enumerations

<span id="enum_XRBodyModifier3D_BodyUpdate"></span>

flags **BodyUpdate**: [🔗](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BodyUpdate)

<span id="class_XRBodyModifier3D_constant_BODY_UPDATE_UPPER_BODY"></span>

[BodyUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BodyUpdate) **BODY_UPDATE_UPPER_BODY** = `1`

The skeleton's upper body joints are updated.

<span id="class_XRBodyModifier3D_constant_BODY_UPDATE_LOWER_BODY"></span>

[BodyUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BodyUpdate) **BODY_UPDATE_LOWER_BODY** = `2`

The skeleton's lower body joints are updated.

<span id="class_XRBodyModifier3D_constant_BODY_UPDATE_HANDS"></span>

[BodyUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BodyUpdate) **BODY_UPDATE_HANDS** = `4`

The skeleton's hand joints are updated.

---

<span id="enum_XRBodyModifier3D_BoneUpdate"></span>

enum **BoneUpdate**: [🔗](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BoneUpdate)

<span id="class_XRBodyModifier3D_constant_BONE_UPDATE_FULL"></span>

[BoneUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BoneUpdate) **BONE_UPDATE_FULL** = `0`

The skeleton's bones are fully updated (both position and rotation) to match the tracked bones.

<span id="class_XRBodyModifier3D_constant_BONE_UPDATE_ROTATION_ONLY"></span>

[BoneUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BoneUpdate) **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton's bones are only rotated to align with the tracked bones, preserving bone length.

<span id="class_XRBodyModifier3D_constant_BONE_UPDATE_MAX"></span>

[BoneUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BoneUpdate) **BONE_UPDATE_MAX** = `2`

Represents the size of the [BoneUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BoneUpdate) enum.

---

### Property Descriptions

<span id="class_XRBodyModifier3D_property_body_tracker"></span>

[StringName](class_stringname.md#class_StringName) **body_tracker** = `&"/user/body_tracker"` [🔗](class_xrbodymodifier3d.md#class_XRBodyModifier3D_property_body_tracker)

- void **set_body_tracker** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_body_tracker** ( )

The name of the [XRBodyTracker](class_xrbodytracker.md#class_XRBodyTracker) registered with [XRServer](class_xrserver.md#class_XRServer) to obtain the body tracking data from.

---

<span id="class_XRBodyModifier3D_property_body_update"></span>

*BitField*\[[BodyUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BodyUpdate)\] **body_update** = `7` [🔗](class_xrbodymodifier3d.md#class_XRBodyModifier3D_property_body_update)

- void **set_body_update** ( value: *BitField*\[[BodyUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BodyUpdate)\] )
- *BitField*\[[BodyUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BodyUpdate)\] **get_body_update** ( )

Specifies the body parts to update.

---

<span id="class_XRBodyModifier3D_property_bone_update"></span>

[BoneUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BoneUpdate) **bone_update** = `0` [🔗](class_xrbodymodifier3d.md#class_XRBodyModifier3D_property_bone_update)

- void **set_bone_update** ( value: [BoneUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BoneUpdate) )
- [BoneUpdate](class_xrbodymodifier3d.md#enum_XRBodyModifier3D_BoneUpdate) **get_bone_update** ( )

Specifies the type of updates to perform on the bones.
