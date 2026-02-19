<span id="class_LimitAngularVelocityModifier3D"></span>

## LimitAngularVelocityModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Limit bone rotation angular velocity.

### Description

This modifier limits bone rotation angular velocity by comparing poses between previous and current frame.

You can add bone chains by specifying their root and end bones, then add the bones between them to a list. Modifier processes either that list or the bones excluding those in the list depending on the option [exclude](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_property_exclude).

### Properties


| [int](class_int.md#class_int) | [chain_count](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_property_chain_count) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [exclude](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_property_exclude) | `false` |
| [int](class_int.md#class_int) | [joint_count](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_property_joint_count) | `0` |
| [float](class_float.md#class_float) | [max_angular_velocity](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_property_max_angular_velocity) | `6.2831855` |

### Methods


| void | [clear_chains](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_clear_chains) ( ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_end_bone](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_get_end_bone) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_end_bone_name](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_get_end_bone_name) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_root_bone](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_get_root_bone) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_root_bone_name](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_get_root_bone_name) ( index: [int](class_int.md#class_int) ) const |
| void | [reset](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_reset) ( ) |
| void | [set_end_bone](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_set_end_bone) ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) |
| void | [set_end_bone_name](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_set_end_bone_name) ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) |
| void | [set_root_bone](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_set_root_bone) ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) |
| void | [set_root_bone_name](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_set_root_bone_name) ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) |

---

### Property Descriptions

<span id="class_LimitAngularVelocityModifier3D_property_chain_count"></span>

[int](class_int.md#class_int) **chain_count** = `0` [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_property_chain_count)

- void **set_chain_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_chain_count** ( )

The number of chains.

---

<span id="class_LimitAngularVelocityModifier3D_property_exclude"></span>

[bool](class_bool.md#class_bool) **exclude** = `false` [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_property_exclude)

- void **set_exclude** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_exclude** ( )

If `true`, the modifier processes bones not included in the bone list.

If `false`, the bones processed by the modifier are equal to the bone list.

---

<span id="class_LimitAngularVelocityModifier3D_property_joint_count"></span>

[int](class_int.md#class_int) **joint_count** = `0` [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_property_joint_count)

The number of joints in the list which created by chains dynamically.

---

<span id="class_LimitAngularVelocityModifier3D_property_max_angular_velocity"></span>

[float](class_float.md#class_float) **max_angular_velocity** = `6.2831855` [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_property_max_angular_velocity)

- void **set_max_angular_velocity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max_angular_velocity** ( )

The maximum angular velocity per second.

---

### Method Descriptions

<span id="class_LimitAngularVelocityModifier3D_method_clear_chains"></span>

void **clear_chains** ( ) [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_clear_chains)

Clear all chains.

---

<span id="class_LimitAngularVelocityModifier3D_method_get_end_bone"></span>

[int](class_int.md#class_int) **get_end_bone** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_get_end_bone)

Returns the end bone index of the bone chain.

---

<span id="class_LimitAngularVelocityModifier3D_method_get_end_bone_name"></span>

[String](class_string.md#class_String) **get_end_bone_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_get_end_bone_name)

Returns the end bone name of the bone chain.

---

<span id="class_LimitAngularVelocityModifier3D_method_get_root_bone"></span>

[int](class_int.md#class_int) **get_root_bone** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_get_root_bone)

Returns the root bone index of the bone chain.

---

<span id="class_LimitAngularVelocityModifier3D_method_get_root_bone_name"></span>

[String](class_string.md#class_String) **get_root_bone_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_get_root_bone_name)

Returns the root bone name of the bone chain.

---

<span id="class_LimitAngularVelocityModifier3D_method_reset"></span>

void **reset** ( ) [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_reset)

Sets the reference pose for angle comparison to the current pose with the influence of constraints removed. This function is automatically triggered when joints change or upon activation.

---

<span id="class_LimitAngularVelocityModifier3D_method_set_end_bone"></span>

void **set_end_bone** ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_set_end_bone)

Sets the end bone index of the bone chain.

---

<span id="class_LimitAngularVelocityModifier3D_method_set_end_bone_name"></span>

void **set_end_bone_name** ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_set_end_bone_name)

Sets the end bone name of the bone chain.

 **Note:** End bone must be the root bone or a child of the root bone.

---

<span id="class_LimitAngularVelocityModifier3D_method_set_root_bone"></span>

void **set_root_bone** ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_set_root_bone)

Sets the root bone index of the bone chain.

---

<span id="class_LimitAngularVelocityModifier3D_method_set_root_bone_name"></span>

void **set_root_bone_name** ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) [🔗](class_limitangularvelocitymodifier3d.md#class_LimitAngularVelocityModifier3D_method_set_root_bone_name)

Sets the root bone name of the bone chain.
