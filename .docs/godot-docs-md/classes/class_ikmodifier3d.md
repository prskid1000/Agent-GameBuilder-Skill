<span id="class_IKModifier3D"></span>

## IKModifier3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [ChainIK3D](class_chainik3d.md#class_ChainIK3D), [TwoBoneIK3D](class_twoboneik3d.md#class_TwoBoneIK3D)

A node for inverse kinematics which may modify more than one bone.

### Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) s that has some joint lists and applies inverse kinematics. This class has some structs, enums, and helper methods which are useful to solve inverse kinematics.

### Tutorials

- Inverse Kinematics Returns to Godot 4.6 - IKModifier3D

### Properties


| [bool](class_bool.md#class_bool) | [mutable_bone_axes](class_ikmodifier3d.md#class_IKModifier3D_property_mutable_bone_axes) | `true` |
| --- | --- | --- |

### Methods


| void | [clear_settings](class_ikmodifier3d.md#class_IKModifier3D_method_clear_settings) ( ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_setting_count](class_ikmodifier3d.md#class_IKModifier3D_method_get_setting_count) ( ) const |
| void | [reset](class_ikmodifier3d.md#class_IKModifier3D_method_reset) ( ) |
| void | [set_setting_count](class_ikmodifier3d.md#class_IKModifier3D_method_set_setting_count) ( count: [int](class_int.md#class_int) ) |

---

### Property Descriptions

<span id="class_IKModifier3D_property_mutable_bone_axes"></span>

[bool](class_bool.md#class_bool) **mutable_bone_axes** = `true` [🔗](class_ikmodifier3d.md#class_IKModifier3D_property_mutable_bone_axes)

- void **set_mutable_bone_axes** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **are_bone_axes_mutable** ( )

If `true`, the solver retrieves the bone axis from the bone pose every frame.

If `false`, the solver retrieves the bone axis from the bone rest and caches it, which increases performance slightly, but position changes in the bone pose made before processing this **IKModifier3D** are ignored.

---

### Method Descriptions

<span id="class_IKModifier3D_method_clear_settings"></span>

void **clear_settings** ( ) [🔗](class_ikmodifier3d.md#class_IKModifier3D_method_clear_settings)

Clears all settings.

---

<span id="class_IKModifier3D_method_get_setting_count"></span>

[int](class_int.md#class_int) **get_setting_count** ( ) *const* [🔗](class_ikmodifier3d.md#class_IKModifier3D_method_get_setting_count)

Returns the number of settings.

---

<span id="class_IKModifier3D_method_reset"></span>

void **reset** ( ) [🔗](class_ikmodifier3d.md#class_IKModifier3D_method_reset)

Resets a state with respect to the current bone pose.

---

<span id="class_IKModifier3D_method_set_setting_count"></span>

void **set_setting_count** ( count: [int](class_int.md#class_int) ) [🔗](class_ikmodifier3d.md#class_IKModifier3D_method_set_setting_count)

Sets the number of settings.
