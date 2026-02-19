.. meta::
	:keywords: tag

<span id="class_BoneAttachment3D"></span>

## BoneAttachment3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

А node that dynamically copies or overrides the 3D transform of a bone in its parent [Skeleton3D](class_skeleton3d.md#class_Skeleton3D).

### Description

This node selects a bone in a [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) and attaches to it. This means that the **BoneAttachment3D** node will either dynamically copy or override the 3D transform of the selected bone.

### Properties


| [int](class_int.md#class_int) | [bone_idx](class_boneattachment3d.md#class_BoneAttachment3D_property_bone_idx) | `-1` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [bone_name](class_boneattachment3d.md#class_BoneAttachment3D_property_bone_name) | `""` |
| [NodePath](class_nodepath.md#class_NodePath) | [external_skeleton](class_boneattachment3d.md#class_BoneAttachment3D_property_external_skeleton) |
| [bool](class_bool.md#class_bool) | [override_pose](class_boneattachment3d.md#class_BoneAttachment3D_property_override_pose) | `false` |
| [PhysicsInterpolationMode](class_node.md#enum_Node_PhysicsInterpolationMode) | physics_interpolation_mode | `2` (overrides [Node](class_node.md#class_Node_property_physics_interpolation_mode)) |
| [bool](class_bool.md#class_bool) | [use_external_skeleton](class_boneattachment3d.md#class_BoneAttachment3D_property_use_external_skeleton) | `false` |

### Methods


| [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) | [get_skeleton](class_boneattachment3d.md#class_BoneAttachment3D_method_get_skeleton) ( ) |
| --- | --- |
| void | [on_skeleton_update](class_boneattachment3d.md#class_BoneAttachment3D_method_on_skeleton_update) ( ) |

---

### Property Descriptions

<span id="class_BoneAttachment3D_property_bone_idx"></span>

[int](class_int.md#class_int) **bone_idx** = `-1` [🔗](class_boneattachment3d.md#class_BoneAttachment3D_property_bone_idx)

- void **set_bone_idx** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bone_idx** ( )

The index of the attached bone.

---

<span id="class_BoneAttachment3D_property_bone_name"></span>

[String](class_string.md#class_String) **bone_name** = `""` [🔗](class_boneattachment3d.md#class_BoneAttachment3D_property_bone_name)

- void **set_bone_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_bone_name** ( )

The name of the attached bone.

---

<span id="class_BoneAttachment3D_property_external_skeleton"></span>

[NodePath](class_nodepath.md#class_NodePath) **external_skeleton** [🔗](class_boneattachment3d.md#class_BoneAttachment3D_property_external_skeleton)

- void **set_external_skeleton** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_external_skeleton** ( )

The [NodePath](class_nodepath.md#class_NodePath) to the external [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) node.

---

<span id="class_BoneAttachment3D_property_override_pose"></span>

[bool](class_bool.md#class_bool) **override_pose** = `false` [🔗](class_boneattachment3d.md#class_BoneAttachment3D_property_override_pose)

- void **set_override_pose** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_override_pose** ( )

Whether the **BoneAttachment3D** node will override the bone pose of the bone it is attached to. When set to `true`, the **BoneAttachment3D** node can change the pose of the bone. When set to `false`, the **BoneAttachment3D** will always be set to the bone's transform.

 **Note:** This override performs interruptively in the skeleton update process using signals due to the old design. It may cause unintended behavior when used at the same time with [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D).

---

<span id="class_BoneAttachment3D_property_use_external_skeleton"></span>

[bool](class_bool.md#class_bool) **use_external_skeleton** = `false` [🔗](class_boneattachment3d.md#class_BoneAttachment3D_property_use_external_skeleton)

- void **set_use_external_skeleton** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_external_skeleton** ( )

Whether the **BoneAttachment3D** node will use an external [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) node rather than attempting to use its parent node as the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D). When set to `true`, the **BoneAttachment3D** node will use the external [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) node set in [external_skeleton](class_boneattachment3d.md#class_BoneAttachment3D_property_external_skeleton).

---

### Method Descriptions

<span id="class_BoneAttachment3D_method_get_skeleton"></span>

[Skeleton3D](class_skeleton3d.md#class_Skeleton3D) **get_skeleton** ( ) [🔗](class_boneattachment3d.md#class_BoneAttachment3D_method_get_skeleton)

Returns the parent or external [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) node if it exists, otherwise returns `null`.

---

<span id="class_BoneAttachment3D_method_on_skeleton_update"></span>

void **on_skeleton_update** ( ) [🔗](class_boneattachment3d.md#class_BoneAttachment3D_method_on_skeleton_update)

A function that is called automatically when the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) is updated. This function is where the **BoneAttachment3D** node updates its position so it is correctly bound when it is *not* set to override the bone pose.
