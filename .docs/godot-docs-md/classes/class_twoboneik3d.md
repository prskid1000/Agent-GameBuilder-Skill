<span id="class_TwoBoneIK3D"></span>

## TwoBoneIK3D

**Inherits:** [IKModifier3D](class_ikmodifier3d.md#class_IKModifier3D) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Rotation based intersection of two circles inverse kinematics solver.

### Description

This [IKModifier3D](class_ikmodifier3d.md#class_IKModifier3D) requires a pole target. It provides deterministic results by constructing a plane from each joint and pole target and finding the intersection of two circles (disks in 3D).

This IK can handle twist by setting the pole direction. If there are more than one bone between each set bone, their rotations are ignored, and the straight line connecting the root-middle and middle-end joints are treated as virtual bones.

### Properties


| [int](class_int.md#class_int) | [setting_count](class_twoboneik3d.md#class_TwoBoneIK3D_property_setting_count) | `0` |
| --- | --- | --- |

### Methods


| [int](class_int.md#class_int) | [get_end_bone](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_end_bone) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) | [get_end_bone_direction](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_end_bone_direction) ( index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_end_bone_length](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_end_bone_length) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_end_bone_name](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_end_bone_name) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_middle_bone](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_middle_bone) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_middle_bone_name](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_middle_bone_name) ( index: [int](class_int.md#class_int) ) const |
| [SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) | [get_pole_direction](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_pole_direction) ( index: [int](class_int.md#class_int) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_pole_direction_vector](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_pole_direction_vector) ( index: [int](class_int.md#class_int) ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_pole_node](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_pole_node) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_root_bone](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_root_bone) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_root_bone_name](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_root_bone_name) ( index: [int](class_int.md#class_int) ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_target_node](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_target_node) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_end_bone_extended](class_twoboneik3d.md#class_TwoBoneIK3D_method_is_end_bone_extended) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_using_virtual_end](class_twoboneik3d.md#class_TwoBoneIK3D_method_is_using_virtual_end) ( index: [int](class_int.md#class_int) ) const |
| void | [set_end_bone](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_end_bone) ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) |
| void | [set_end_bone_direction](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_end_bone_direction) ( index: [int](class_int.md#class_int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) ) |
| void | [set_end_bone_length](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_end_bone_length) ( index: [int](class_int.md#class_int), length: [float](class_float.md#class_float) ) |
| void | [set_end_bone_name](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_end_bone_name) ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) |
| void | [set_extend_end_bone](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_extend_end_bone) ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_middle_bone](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_middle_bone) ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) |
| void | [set_middle_bone_name](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_middle_bone_name) ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) |
| void | [set_pole_direction](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_pole_direction) ( index: [int](class_int.md#class_int), direction: [SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) ) |
| void | [set_pole_direction_vector](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_pole_direction_vector) ( index: [int](class_int.md#class_int), vector: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [set_pole_node](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_pole_node) ( index: [int](class_int.md#class_int), pole_node: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_root_bone](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_root_bone) ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) |
| void | [set_root_bone_name](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_root_bone_name) ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) |
| void | [set_target_node](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_target_node) ( index: [int](class_int.md#class_int), target_node: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_use_virtual_end](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_use_virtual_end) ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_TwoBoneIK3D_property_setting_count"></span>

[int](class_int.md#class_int) **setting_count** = `0` [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_property_setting_count)

- void **set_setting_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_setting_count** ( )

The number of settings.

---

### Method Descriptions

<span id="class_TwoBoneIK3D_method_get_end_bone"></span>

[int](class_int.md#class_int) **get_end_bone** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_end_bone)

Returns the end bone index.

---

<span id="class_TwoBoneIK3D_method_get_end_bone_direction"></span>

[BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) **get_end_bone_direction** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_end_bone_direction)

Returns the end bone's tail direction when [is_end_bone_extended()](class_twoboneik3d.md#class_TwoBoneIK3D_method_is_end_bone_extended) is `true`.

---

<span id="class_TwoBoneIK3D_method_get_end_bone_length"></span>

[float](class_float.md#class_float) **get_end_bone_length** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_end_bone_length)

Returns the end bone tail length of the bone chain when [is_end_bone_extended()](class_twoboneik3d.md#class_TwoBoneIK3D_method_is_end_bone_extended) is `true`.

---

<span id="class_TwoBoneIK3D_method_get_end_bone_name"></span>

[String](class_string.md#class_String) **get_end_bone_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_end_bone_name)

Returns the end bone name.

---

<span id="class_TwoBoneIK3D_method_get_middle_bone"></span>

[int](class_int.md#class_int) **get_middle_bone** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_middle_bone)

Returns the middle bone index.

---

<span id="class_TwoBoneIK3D_method_get_middle_bone_name"></span>

[String](class_string.md#class_String) **get_middle_bone_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_middle_bone_name)

Returns the middle bone name.

---

<span id="class_TwoBoneIK3D_method_get_pole_direction"></span>

[SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) **get_pole_direction** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_pole_direction)

Returns the pole direction.

---

<span id="class_TwoBoneIK3D_method_get_pole_direction_vector"></span>

[Vector3](class_vector3.md#class_Vector3) **get_pole_direction_vector** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_pole_direction_vector)

Returns the pole direction vector.

If [get_pole_direction()](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_pole_direction) is [SkeletonModifier3D.SECONDARY_DIRECTION_NONE](class_skeletonmodifier3d.md#class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_NONE), this method returns `Vector3(0, 0, 0)`.

---

<span id="class_TwoBoneIK3D_method_get_pole_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_pole_node** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_pole_node)

Returns the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.

---

<span id="class_TwoBoneIK3D_method_get_root_bone"></span>

[int](class_int.md#class_int) **get_root_bone** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_root_bone)

Returns the root bone index.

---

<span id="class_TwoBoneIK3D_method_get_root_bone_name"></span>

[String](class_string.md#class_String) **get_root_bone_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_root_bone_name)

Returns the root bone name.

---

<span id="class_TwoBoneIK3D_method_get_target_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_target_node** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_get_target_node)

Returns the target node that the end bone is trying to reach.

---

<span id="class_TwoBoneIK3D_method_is_end_bone_extended"></span>

[bool](class_bool.md#class_bool) **is_end_bone_extended** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_is_end_bone_extended)

Returns `true` if the end bone is extended to have a tail.

---

<span id="class_TwoBoneIK3D_method_is_using_virtual_end"></span>

[bool](class_bool.md#class_bool) **is_using_virtual_end** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_is_using_virtual_end)

Returns `true` if the end bone is extended from the middle bone as a virtual bone.

---

<span id="class_TwoBoneIK3D_method_set_end_bone"></span>

void **set_end_bone** ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_end_bone)

Sets the end bone index.

---

<span id="class_TwoBoneIK3D_method_set_end_bone_direction"></span>

void **set_end_bone_direction** ( index: [int](class_int.md#class_int), bone_direction: [BoneDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_BoneDirection) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_end_bone_direction)

Sets the end bone tail direction when [is_end_bone_extended()](class_twoboneik3d.md#class_TwoBoneIK3D_method_is_end_bone_extended) is `true`.

---

<span id="class_TwoBoneIK3D_method_set_end_bone_length"></span>

void **set_end_bone_length** ( index: [int](class_int.md#class_int), length: [float](class_float.md#class_float) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_end_bone_length)

Sets the end bone tail length when [is_end_bone_extended()](class_twoboneik3d.md#class_TwoBoneIK3D_method_is_end_bone_extended) is `true`.

---

<span id="class_TwoBoneIK3D_method_set_end_bone_name"></span>

void **set_end_bone_name** ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_end_bone_name)

Sets the end bone name.

 **Note:** The end bone must be a child of the middle bone.

---

<span id="class_TwoBoneIK3D_method_set_extend_end_bone"></span>

void **set_extend_end_bone** ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_extend_end_bone)

If `enabled` is `true`, the end bone is extended to have a tail.

---

<span id="class_TwoBoneIK3D_method_set_middle_bone"></span>

void **set_middle_bone** ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_middle_bone)

Sets the middle bone index.

---

<span id="class_TwoBoneIK3D_method_set_middle_bone_name"></span>

void **set_middle_bone_name** ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_middle_bone_name)

Sets the middle bone name.

 **Note:** The middle bone must be a child of the root bone.

---

<span id="class_TwoBoneIK3D_method_set_pole_direction"></span>

void **set_pole_direction** ( index: [int](class_int.md#class_int), direction: [SecondaryDirection](class_skeletonmodifier3d.md#enum_SkeletonModifier3D_SecondaryDirection) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_pole_direction)

Sets the pole direction.

The pole is on the middle bone and will direct to the pole target.

The rotation axis is a vector that is orthogonal to this and the forward vector.

 **Note:** The pole direction and the forward vector shouldn't be colinear to avoid unintended rotation.

---

<span id="class_TwoBoneIK3D_method_set_pole_direction_vector"></span>

void **set_pole_direction_vector** ( index: [int](class_int.md#class_int), vector: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_pole_direction_vector)

Sets the pole direction vector.

This vector is normalized by an internal process.

If the vector length is `0`, it is considered synonymous with [SkeletonModifier3D.SECONDARY_DIRECTION_NONE](class_skeletonmodifier3d.md#class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_NONE).

---

<span id="class_TwoBoneIK3D_method_set_pole_node"></span>

void **set_pole_node** ( index: [int](class_int.md#class_int), pole_node: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_pole_node)

Sets the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.

---

<span id="class_TwoBoneIK3D_method_set_root_bone"></span>

void **set_root_bone** ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_root_bone)

Sets the root bone index.

---

<span id="class_TwoBoneIK3D_method_set_root_bone_name"></span>

void **set_root_bone_name** ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_root_bone_name)

Sets the root bone name.

---

<span id="class_TwoBoneIK3D_method_set_target_node"></span>

void **set_target_node** ( index: [int](class_int.md#class_int), target_node: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_target_node)

Sets the target node that the end bone is trying to reach.

---

<span id="class_TwoBoneIK3D_method_set_use_virtual_end"></span>

void **set_use_virtual_end** ( index: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_twoboneik3d.md#class_TwoBoneIK3D_method_set_use_virtual_end)

If `enabled` is `true`, the end bone is extended from the middle bone as a virtual bone.
