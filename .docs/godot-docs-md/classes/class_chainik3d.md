<span id="class_ChainIK3D"></span>

## ChainIK3D

**Inherits:** [IKModifier3D](class_ikmodifier3d.md#class_IKModifier3D) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [IterateIK3D](class_iterateik3d.md#class_IterateIK3D), [SplineIK3D](class_splineik3d.md#class_SplineIK3D)

A [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) to apply inverse kinematics to bone chains containing an arbitrary number of bones.

### Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) that automatically generates a joint list from the bones between the root bone and the end bone.

### Methods


| [int](class_int.md#class_int) | [get_end_bone](class_chainik3d.md#class_ChainIK3D_method_get_end_bone) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) | [get_end_bone_direction](class_chainik3d.md#class_ChainIK3D_method_get_end_bone_direction) ( index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_end_bone_length](class_chainik3d.md#class_ChainIK3D_method_get_end_bone_length) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_end_bone_name](class_chainik3d.md#class_ChainIK3D_method_get_end_bone_name) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_joint_bone](class_chainik3d.md#class_ChainIK3D_method_get_joint_bone) ( index: [int](class_int.md#class_int), joint: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_joint_bone_name](class_chainik3d.md#class_ChainIK3D_method_get_joint_bone_name) ( index: [int](class_int.md#class_int), joint: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_joint_count](class_chainik3d.md#class_ChainIK3D_method_get_joint_count) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_root_bone](class_chainik3d.md#class_ChainIK3D_method_get_root_bone) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_root_bone_name](class_chainik3d.md#class_ChainIK3D_method_get_root_bone_name) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_end_bone_extended](class_chainik3d.md#class_ChainIK3D_method_is_end_bone_extended) ( index: [int](class_int.md#class_int) ) const |
| void | [set_end_bone](class_chainik3d.md#class_ChainIK3D_method_set_end_bone) ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) |
| void | [set_end_bone_direction](class_chainik3d.md#class_ChainIK3D_method_set_end_bone_direction) ( index: [int](class_int.md#class_int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) ) |
| void | [set_end_bone_length](class_chainik3d.md#class_ChainIK3D_method_set_end_bone_length) ( index: [int](class_int.md#class_int), length: [float](class_float.md#class_float) ) |
| void | [set_end_bone_name](class_chainik3d.md#class_ChainIK3D_method_set_end_bone_name) ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) |
| void | [set_extend_end_bone](class_chainik3d.md#class_ChainIK3D_method_set_extend_end_bone) ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_root_bone](class_chainik3d.md#class_ChainIK3D_method_set_root_bone) ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) |
| void | [set_root_bone_name](class_chainik3d.md#class_ChainIK3D_method_set_root_bone_name) ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) |

---

### Method Descriptions

<span id="class_ChainIK3D_method_get_end_bone"></span>

[int](class_int.md#class_int) **get_end_bone** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_get_end_bone)

Returns the end bone index of the bone chain.

---

<span id="class_ChainIK3D_method_get_end_bone_direction"></span>

[BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) **get_end_bone_direction** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_get_end_bone_direction)

Returns the tail direction of the end bone of the bone chain when [is_end_bone_extended()](class_chainik3d.md#class_ChainIK3D_method_is_end_bone_extended) is `true`.

---

<span id="class_ChainIK3D_method_get_end_bone_length"></span>

[float](class_float.md#class_float) **get_end_bone_length** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_get_end_bone_length)

Returns the end bone tail length of the bone chain when [is_end_bone_extended()](class_chainik3d.md#class_ChainIK3D_method_is_end_bone_extended) is `true`.

---

<span id="class_ChainIK3D_method_get_end_bone_name"></span>

[String](class_string.md#class_String) **get_end_bone_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_get_end_bone_name)

Returns the end bone name of the bone chain.

---

<span id="class_ChainIK3D_method_get_joint_bone"></span>

[int](class_int.md#class_int) **get_joint_bone** ( index: [int](class_int.md#class_int), joint: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_get_joint_bone)

Returns the bone index at `joint` in the bone chain's joint list.

---

<span id="class_ChainIK3D_method_get_joint_bone_name"></span>

[String](class_string.md#class_String) **get_joint_bone_name** ( index: [int](class_int.md#class_int), joint: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_get_joint_bone_name)

Returns the bone name at `joint` in the bone chain's joint list.

---

<span id="class_ChainIK3D_method_get_joint_count"></span>

[int](class_int.md#class_int) **get_joint_count** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_get_joint_count)

Returns the joint count of the bone chain's joint list.

---

<span id="class_ChainIK3D_method_get_root_bone"></span>

[int](class_int.md#class_int) **get_root_bone** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_get_root_bone)

Returns the root bone index of the bone chain.

---

<span id="class_ChainIK3D_method_get_root_bone_name"></span>

[String](class_string.md#class_String) **get_root_bone_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_get_root_bone_name)

Returns the root bone name of the bone chain.

---

<span id="class_ChainIK3D_method_is_end_bone_extended"></span>

[bool](class_bool.md#class_bool) **is_end_bone_extended** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_chainik3d.md#class_ChainIK3D_method_is_end_bone_extended)

Returns `true` if the end bone is extended to have a tail.

---

<span id="class_ChainIK3D_method_set_end_bone"></span>

void **set_end_bone** ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) [🔗](class_chainik3d.md#class_ChainIK3D_method_set_end_bone)

Sets the end bone index of the bone chain.

---

<span id="class_ChainIK3D_method_set_end_bone_direction"></span>

void **set_end_bone_direction** ( index: [int](class_int.md#class_int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) ) [🔗](class_chainik3d.md#class_ChainIK3D_method_set_end_bone_direction)

Sets the end bone tail direction of the bone chain when [is_end_bone_extended()](class_chainik3d.md#class_ChainIK3D_method_is_end_bone_extended) is `true`.

---

<span id="class_ChainIK3D_method_set_end_bone_length"></span>

void **set_end_bone_length** ( index: [int](class_int.md#class_int), length: [float](class_float.md#class_float) ) [🔗](class_chainik3d.md#class_ChainIK3D_method_set_end_bone_length)

Sets the end bone tail length of the bone chain when [is_end_bone_extended()](class_chainik3d.md#class_ChainIK3D_method_is_end_bone_extended) is `true`.

---

<span id="class_ChainIK3D_method_set_end_bone_name"></span>

void **set_end_bone_name** ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) [🔗](class_chainik3d.md#class_ChainIK3D_method_set_end_bone_name)

Sets the end bone name of the bone chain.

 **Note:** The end bone must be the root bone or a child of the root bone. If they are the same, the tail must be extended by [set_extend_end_bone()](class_chainik3d.md#class_ChainIK3D_method_set_extend_end_bone) to modify the bone.

---

<span id="class_ChainIK3D_method_set_extend_end_bone"></span>

void **set_extend_end_bone** ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_chainik3d.md#class_ChainIK3D_method_set_extend_end_bone)

If `enabled` is `true`, the end bone is extended to have a tail.

The extended tail config is allocated to the last element in the joint list. In other words, if you set `enabled` to `false`, the config of the last element in the joint list has no effect in the simulated result.

---

<span id="class_ChainIK3D_method_set_root_bone"></span>

void **set_root_bone** ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) [🔗](class_chainik3d.md#class_ChainIK3D_method_set_root_bone)

Sets the root bone index of the bone chain.

---

<span id="class_ChainIK3D_method_set_root_bone_name"></span>

void **set_root_bone_name** ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) [🔗](class_chainik3d.md#class_ChainIK3D_method_set_root_bone_name)

Sets the root bone name of the bone chain.
