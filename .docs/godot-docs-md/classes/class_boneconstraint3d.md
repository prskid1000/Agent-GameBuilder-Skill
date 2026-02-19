<span id="class_BoneConstraint3D"></span>

## BoneConstraint3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AimModifier3D](class_aimmodifier3d.md#class_AimModifier3D), [ConvertTransformModifier3D](class_converttransformmodifier3d.md#class_ConvertTransformModifier3D), [CopyTransformModifier3D](class_copytransformmodifier3d.md#class_CopyTransformModifier3D)

A node that may modify Skeleton3D's bone with associating the two bones.

### Description

Base class of [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) that modifies the bone set in [set_apply_bone()](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_apply_bone) based on the transform of the bone retrieved by [get_reference_bone()](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_bone).

### Methods


| void | [clear_setting](class_boneconstraint3d.md#class_BoneConstraint3D_method_clear_setting) ( ) |
| --- | --- |
| [float](class_float.md#class_float) | [get_amount](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_amount) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_apply_bone](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_apply_bone) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_apply_bone_name](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_apply_bone_name) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_reference_bone](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_bone) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_reference_bone_name](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_bone_name) ( index: [int](class_int.md#class_int) ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_reference_node](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_node) ( index: [int](class_int.md#class_int) ) const |
| [ReferenceType](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType) | [get_reference_type](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_type) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_setting_count](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_setting_count) ( ) const |
| void | [set_amount](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_amount) ( index: [int](class_int.md#class_int), amount: [float](class_float.md#class_float) ) |
| void | [set_apply_bone](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_apply_bone) ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) |
| void | [set_apply_bone_name](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_apply_bone_name) ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) |
| void | [set_reference_bone](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_reference_bone) ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) |
| void | [set_reference_bone_name](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_reference_bone_name) ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) |
| void | [set_reference_node](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_reference_node) ( index: [int](class_int.md#class_int), node: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_reference_type](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_reference_type) ( index: [int](class_int.md#class_int), type: [ReferenceType](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType) ) |
| void | [set_setting_count](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_setting_count) ( count: [int](class_int.md#class_int) ) |

---

### Enumerations

<span id="enum_BoneConstraint3D_ReferenceType"></span>

enum **ReferenceType**: [🔗](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType)

<span id="class_BoneConstraint3D_constant_REFERENCE_TYPE_BONE"></span>

[ReferenceType](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType) **REFERENCE_TYPE_BONE** = `0`

The reference target is a bone. In this case, the reference target spaces is local space.

<span id="class_BoneConstraint3D_constant_REFERENCE_TYPE_NODE"></span>

[ReferenceType](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType) **REFERENCE_TYPE_NODE** = `1`

The reference target is a [Node3D](class_node3d.md#class_Node3D). In this case, the reference target spaces is model space.

In other words, the reference target's coordinates are treated as if it were placed directly under [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) which parent of the **BoneConstraint3D**.

---

### Method Descriptions

<span id="class_BoneConstraint3D_method_clear_setting"></span>

void **clear_setting** ( ) [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_clear_setting)

Clear all settings.

---

<span id="class_BoneConstraint3D_method_get_amount"></span>

[float](class_float.md#class_float) **get_amount** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_amount)

Returns the apply amount of the setting at `index`.

---

<span id="class_BoneConstraint3D_method_get_apply_bone"></span>

[int](class_int.md#class_int) **get_apply_bone** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_apply_bone)

Returns the apply bone of the setting at `index`. This bone will be modified.

---

<span id="class_BoneConstraint3D_method_get_apply_bone_name"></span>

[String](class_string.md#class_String) **get_apply_bone_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_apply_bone_name)

Returns the apply bone name of the setting at `index`. This bone will be modified.

---

<span id="class_BoneConstraint3D_method_get_reference_bone"></span>

[int](class_int.md#class_int) **get_reference_bone** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_bone)

Returns the reference bone of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

---

<span id="class_BoneConstraint3D_method_get_reference_bone_name"></span>

[String](class_string.md#class_String) **get_reference_bone_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_bone_name)

Returns the reference bone name of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

---

<span id="class_BoneConstraint3D_method_get_reference_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_reference_node** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_node)

Returns the reference node path of the setting at `index`.

This node will be only referenced and not modified by this modifier.

---

<span id="class_BoneConstraint3D_method_get_reference_type"></span>

[ReferenceType](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType) **get_reference_type** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_reference_type)

Returns the reference target type of the setting at `index`. See also [ReferenceType](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType).

---

<span id="class_BoneConstraint3D_method_get_setting_count"></span>

[int](class_int.md#class_int) **get_setting_count** ( ) *const* [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_get_setting_count)

Returns the number of settings in the modifier.

---

<span id="class_BoneConstraint3D_method_set_amount"></span>

void **set_amount** ( index: [int](class_int.md#class_int), amount: [float](class_float.md#class_float) ) [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_amount)

Sets the apply amount of the setting at `index` to `amount`.

---

<span id="class_BoneConstraint3D_method_set_apply_bone"></span>

void **set_apply_bone** ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_apply_bone)

Sets the apply bone of the setting at `index` to `bone`. This bone will be modified.

---

<span id="class_BoneConstraint3D_method_set_apply_bone_name"></span>

void **set_apply_bone_name** ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_apply_bone_name)

Sets the apply bone of the setting at `index` to `bone_name`. This bone will be modified.

---

<span id="class_BoneConstraint3D_method_set_reference_bone"></span>

void **set_reference_bone** ( index: [int](class_int.md#class_int), bone: [int](class_int.md#class_int) ) [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_reference_bone)

Sets the reference bone of the setting at `index` to `bone`.

This bone will be only referenced and not modified by this modifier.

---

<span id="class_BoneConstraint3D_method_set_reference_bone_name"></span>

void **set_reference_bone_name** ( index: [int](class_int.md#class_int), bone_name: [String](class_string.md#class_String) ) [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_reference_bone_name)

Sets the reference bone of the setting at `index` to `bone_name`.

This bone will be only referenced and not modified by this modifier.

---

<span id="class_BoneConstraint3D_method_set_reference_node"></span>

void **set_reference_node** ( index: [int](class_int.md#class_int), node: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_reference_node)

Sets the reference node path of the setting at `index` to `node`.

This node will be only referenced and not modified by this modifier.

---

<span id="class_BoneConstraint3D_method_set_reference_type"></span>

void **set_reference_type** ( index: [int](class_int.md#class_int), type: [ReferenceType](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType) ) [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_reference_type)

Sets the reference target type of the setting at `index` to `type`. See also [ReferenceType](class_boneconstraint3d.md#enum_BoneConstraint3D_ReferenceType).

---

<span id="class_BoneConstraint3D_method_set_setting_count"></span>

void **set_setting_count** ( count: [int](class_int.md#class_int) ) [🔗](class_boneconstraint3d.md#class_BoneConstraint3D_method_set_setting_count)

Sets the number of settings in the modifier.
