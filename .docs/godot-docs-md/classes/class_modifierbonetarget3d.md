<span id="class_ModifierBoneTarget3D"></span>

## ModifierBoneTarget3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

А node that dynamically copies the 3D transform of a bone in its parent [Skeleton3D](class_skeleton3d.md#class_Skeleton3D).

### Description

This node selects a bone in a [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) and attaches to it. This means that the **ModifierBoneTarget3D** node will dynamically copy the 3D transform of the selected bone.

The functionality is similar to [BoneAttachment3D](class_boneattachment3d.md#class_BoneAttachment3D), but this node adopts the [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) cycle and is intended to be used as another [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D)'s target.

### Properties


| [int](class_int.md#class_int) | [bone](class_modifierbonetarget3d.md#class_ModifierBoneTarget3D_property_bone) | `-1` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [bone_name](class_modifierbonetarget3d.md#class_ModifierBoneTarget3D_property_bone_name) | `""` |

---

### Property Descriptions

<span id="class_ModifierBoneTarget3D_property_bone"></span>

[int](class_int.md#class_int) **bone** = `-1` [🔗](class_modifierbonetarget3d.md#class_ModifierBoneTarget3D_property_bone)

- void **set_bone** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bone** ( )

The index of the attached bone.

---

<span id="class_ModifierBoneTarget3D_property_bone_name"></span>

[String](class_string.md#class_String) **bone_name** = `""` [🔗](class_modifierbonetarget3d.md#class_ModifierBoneTarget3D_property_bone_name)

- void **set_bone_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_bone_name** ( )

The name of the attached bone.
