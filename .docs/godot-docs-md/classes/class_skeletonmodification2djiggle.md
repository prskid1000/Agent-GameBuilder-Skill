<span id="class_SkeletonModification2DJiggle"></span>

## SkeletonModification2DJiggle

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A modification that jiggles [Bone2D](class_bone2d.md#class_Bone2D) nodes as they move towards a target.

### Description

This modification moves a series of bones, typically called a bone chain, towards a target. What makes this modification special is that it calculates the velocity and acceleration for each bone in the bone chain, and runs a very light physics-like calculation using the inputted values. This allows the bones to overshoot the target and "jiggle" around. It can be configured to act more like a spring, or sway around like cloth might.

This modification is useful for adding additional motion to things like hair, the edges of clothing, and more. It has several settings to that allow control over how the joint moves when the target moves.

 **Note:** The Jiggle modifier has `jiggle_joints`, which are the data objects that hold the data for each joint in the Jiggle chain. This is different from than [Bone2D](class_bone2d.md#class_Bone2D) nodes! Jiggle joints hold the data needed for each [Bone2D](class_bone2d.md#class_Bone2D) in the bone chain used by the Jiggle modification.

### Properties


| [float](class_float.md#class_float) | [damping](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_damping) | `0.75` |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [gravity](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_gravity) | `Vector2(0, 6)` |
| [int](class_int.md#class_int) | [jiggle_data_chain_length](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_jiggle_data_chain_length) | `0` |
| [float](class_float.md#class_float) | [mass](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_mass) | `0.75` |
| [float](class_float.md#class_float) | [stiffness](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_stiffness) | `3.0` |
| [NodePath](class_nodepath.md#class_NodePath) | [target_nodepath](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_target_nodepath) | `NodePath("")` |
| [bool](class_bool.md#class_bool) | [use_gravity](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_use_gravity) | `false` |

### Methods


| [int](class_int.md#class_int) | [get_collision_mask](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_collision_mask) ( ) const |
| --- | --- |
| [NodePath](class_nodepath.md#class_NodePath) | [get_jiggle_joint_bone2d_node](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone2d_node) ( joint_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_jiggle_joint_bone_index](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone_index) ( joint_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_jiggle_joint_damping](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_damping) ( joint_idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_jiggle_joint_gravity](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_gravity) ( joint_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_jiggle_joint_mass](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_mass) ( joint_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_jiggle_joint_override](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_override) ( joint_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_jiggle_joint_stiffness](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_stiffness) ( joint_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_jiggle_joint_use_gravity](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_use_gravity) ( joint_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_use_colliders](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_use_colliders) ( ) const |
| void | [set_collision_mask](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_collision_mask) ( collision_mask: [int](class_int.md#class_int) ) |
| void | [set_jiggle_joint_bone2d_node](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone2d_node) ( joint_idx: [int](class_int.md#class_int), bone2d_node: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_jiggle_joint_bone_index](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone_index) ( joint_idx: [int](class_int.md#class_int), bone_idx: [int](class_int.md#class_int) ) |
| void | [set_jiggle_joint_damping](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_damping) ( joint_idx: [int](class_int.md#class_int), damping: [float](class_float.md#class_float) ) |
| void | [set_jiggle_joint_gravity](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_gravity) ( joint_idx: [int](class_int.md#class_int), gravity: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_jiggle_joint_mass](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_mass) ( joint_idx: [int](class_int.md#class_int), mass: [float](class_float.md#class_float) ) |
| void | [set_jiggle_joint_override](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_override) ( joint_idx: [int](class_int.md#class_int), override: [bool](class_bool.md#class_bool) ) |
| void | [set_jiggle_joint_stiffness](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_stiffness) ( joint_idx: [int](class_int.md#class_int), stiffness: [float](class_float.md#class_float) ) |
| void | [set_jiggle_joint_use_gravity](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_use_gravity) ( joint_idx: [int](class_int.md#class_int), use_gravity: [bool](class_bool.md#class_bool) ) |
| void | [set_use_colliders](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_use_colliders) ( use_colliders: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_SkeletonModification2DJiggle_property_damping"></span>

[float](class_float.md#class_float) **damping** = `0.75` [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_damping)

- void **set_damping** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_damping** ( )

The default amount of damping applied to the Jiggle joints, if they are not overridden. Higher values lead to more of the calculated velocity being applied.

---

<span id="class_SkeletonModification2DJiggle_property_gravity"></span>

[Vector2](class_vector2.md#class_Vector2) **gravity** = `Vector2(0, 6)` [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_gravity)

- void **set_gravity** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_gravity** ( )

The default amount of gravity applied to the Jiggle joints, if they are not overridden.

---

<span id="class_SkeletonModification2DJiggle_property_jiggle_data_chain_length"></span>

[int](class_int.md#class_int) **jiggle_data_chain_length** = `0` [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_jiggle_data_chain_length)

- void **set_jiggle_data_chain_length** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_jiggle_data_chain_length** ( )

The amount of Jiggle joints in the Jiggle modification.

---

<span id="class_SkeletonModification2DJiggle_property_mass"></span>

[float](class_float.md#class_float) **mass** = `0.75` [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_mass)

- void **set_mass** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_mass** ( )

The default amount of mass assigned to the Jiggle joints, if they are not overridden. Higher values lead to faster movements and more overshooting.

---

<span id="class_SkeletonModification2DJiggle_property_stiffness"></span>

[float](class_float.md#class_float) **stiffness** = `3.0` [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_stiffness)

- void **set_stiffness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_stiffness** ( )

The default amount of stiffness assigned to the Jiggle joints, if they are not overridden. Higher values act more like springs, quickly moving into the correct position.

---

<span id="class_SkeletonModification2DJiggle_property_target_nodepath"></span>

[NodePath](class_nodepath.md#class_NodePath) **target_nodepath** = `NodePath("")` [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_target_nodepath)

- void **set_target_node** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_target_node** ( )

The NodePath to the node that is the target for the Jiggle modification. This node is what the Jiggle chain will attempt to rotate the bone chain to.

---

<span id="class_SkeletonModification2DJiggle_property_use_gravity"></span>

[bool](class_bool.md#class_bool) **use_gravity** = `false` [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_use_gravity)

- void **set_use_gravity** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_gravity** ( )

Whether the gravity vector, [gravity](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_property_gravity), should be applied to the Jiggle joints, assuming they are not overriding the default settings.

---

### Method Descriptions

<span id="class_SkeletonModification2DJiggle_method_get_collision_mask"></span>

[int](class_int.md#class_int) **get_collision_mask** ( ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_collision_mask)

Returns the collision mask used by the Jiggle modifier when collisions are enabled.

---

<span id="class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone2d_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_jiggle_joint_bone2d_node** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone2d_node)

Returns the [Bone2D](class_bone2d.md#class_Bone2D) node assigned to the Jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone_index"></span>

[int](class_int.md#class_int) **get_jiggle_joint_bone_index** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone_index)

Returns the index of the [Bone2D](class_bone2d.md#class_Bone2D) node assigned to the Jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_get_jiggle_joint_damping"></span>

[float](class_float.md#class_float) **get_jiggle_joint_damping** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_damping)

Returns the amount of damping of the Jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_get_jiggle_joint_gravity"></span>

[Vector2](class_vector2.md#class_Vector2) **get_jiggle_joint_gravity** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_gravity)

Returns a [Vector2](class_vector2.md#class_Vector2) representing the amount of gravity the Jiggle joint at `joint_idx` is influenced by.

---

<span id="class_SkeletonModification2DJiggle_method_get_jiggle_joint_mass"></span>

[float](class_float.md#class_float) **get_jiggle_joint_mass** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_mass)

Returns the amount of mass of the jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_get_jiggle_joint_override"></span>

[bool](class_bool.md#class_bool) **get_jiggle_joint_override** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_override)

Returns a boolean that indicates whether the joint at `joint_idx` is overriding the default Jiggle joint data defined in the modification.

---

<span id="class_SkeletonModification2DJiggle_method_get_jiggle_joint_stiffness"></span>

[float](class_float.md#class_float) **get_jiggle_joint_stiffness** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_stiffness)

Returns the stiffness of the Jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_get_jiggle_joint_use_gravity"></span>

[bool](class_bool.md#class_bool) **get_jiggle_joint_use_gravity** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_jiggle_joint_use_gravity)

Returns a boolean that indicates whether the joint at `joint_idx` is using gravity or not.

---

<span id="class_SkeletonModification2DJiggle_method_get_use_colliders"></span>

[bool](class_bool.md#class_bool) **get_use_colliders** ( ) *const* [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_get_use_colliders)

Returns whether the jiggle modifier is taking physics colliders into account when solving.

---

<span id="class_SkeletonModification2DJiggle_method_set_collision_mask"></span>

void **set_collision_mask** ( collision_mask: [int](class_int.md#class_int) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_collision_mask)

Sets the collision mask that the Jiggle modifier will use when reacting to colliders, if the Jiggle modifier is set to take colliders into account.

---

<span id="class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone2d_node"></span>

void **set_jiggle_joint_bone2d_node** ( joint_idx: [int](class_int.md#class_int), bone2d_node: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone2d_node)

Sets the [Bone2D](class_bone2d.md#class_Bone2D) node assigned to the Jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone_index"></span>

void **set_jiggle_joint_bone_index** ( joint_idx: [int](class_int.md#class_int), bone_idx: [int](class_int.md#class_int) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone_index)

Sets the bone index, `bone_idx`, of the Jiggle joint at `joint_idx`. When possible, this will also update the `bone2d_node` of the Jiggle joint based on data provided by the linked skeleton.

---

<span id="class_SkeletonModification2DJiggle_method_set_jiggle_joint_damping"></span>

void **set_jiggle_joint_damping** ( joint_idx: [int](class_int.md#class_int), damping: [float](class_float.md#class_float) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_damping)

Sets the amount of damping of the Jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_set_jiggle_joint_gravity"></span>

void **set_jiggle_joint_gravity** ( joint_idx: [int](class_int.md#class_int), gravity: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_gravity)

Sets the gravity vector of the Jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_set_jiggle_joint_mass"></span>

void **set_jiggle_joint_mass** ( joint_idx: [int](class_int.md#class_int), mass: [float](class_float.md#class_float) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_mass)

Sets the of mass of the Jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_set_jiggle_joint_override"></span>

void **set_jiggle_joint_override** ( joint_idx: [int](class_int.md#class_int), override: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_override)

Sets whether the Jiggle joint at `joint_idx` should override the default Jiggle joint settings. Setting this to `true` will make the joint use its own settings rather than the default ones attached to the modification.

---

<span id="class_SkeletonModification2DJiggle_method_set_jiggle_joint_stiffness"></span>

void **set_jiggle_joint_stiffness** ( joint_idx: [int](class_int.md#class_int), stiffness: [float](class_float.md#class_float) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_stiffness)

Sets the of stiffness of the Jiggle joint at `joint_idx`.

---

<span id="class_SkeletonModification2DJiggle_method_set_jiggle_joint_use_gravity"></span>

void **set_jiggle_joint_use_gravity** ( joint_idx: [int](class_int.md#class_int), use_gravity: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_jiggle_joint_use_gravity)

Sets whether the Jiggle joint at `joint_idx` should use gravity.

---

<span id="class_SkeletonModification2DJiggle_method_set_use_colliders"></span>

void **set_use_colliders** ( use_colliders: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle_method_set_use_colliders)

If `true`, the Jiggle modifier will take colliders into account, keeping them from entering into these collision objects.
