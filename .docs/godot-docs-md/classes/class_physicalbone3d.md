.. meta::
	:keywords: ragdoll

<span id="class_PhysicalBone3D"></span>

## PhysicalBone3D

**Inherits:** [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) **<** [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A physics body used to make bones in a [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) react to physics.

### Description

The **PhysicalBone3D** node is a physics body that can be used to make bones in a [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) react to physics.

 **Note:** In order to detect physical bones with raycasts, the [SkeletonModifier3D.active](class_skeletonmodifier3d.md#class_SkeletonModifier3D_property_active) property of the parent [PhysicalBoneSimulator3D](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D) must be `true` and the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D)'s bone must be assigned to **PhysicalBone3D** correctly; it means that [get_bone_id()](class_physicalbone3d.md#class_PhysicalBone3D_method_get_bone_id) should return a valid id (`>= 0`).

### Tutorials

- [Ragdoll System](../tutorials/physics/ragdoll_system.md)

### Properties


| [float](class_float.md#class_float) | [angular_damp](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_damp) | `0.0` |
| --- | --- | --- |
| [DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) | [angular_damp_mode](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_damp_mode) | `0` |
| [Vector3](class_vector3.md#class_Vector3) | [angular_velocity](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_velocity) | `Vector3(0, 0, 0)` |
| [Transform3D](class_transform3d.md#class_Transform3D) | [body_offset](class_physicalbone3d.md#class_PhysicalBone3D_property_body_offset) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |
| [float](class_float.md#class_float) | [bounce](class_physicalbone3d.md#class_PhysicalBone3D_property_bounce) | `0.0` |
| [bool](class_bool.md#class_bool) | [can_sleep](class_physicalbone3d.md#class_PhysicalBone3D_property_can_sleep) | `true` |
| [bool](class_bool.md#class_bool) | [custom_integrator](class_physicalbone3d.md#class_PhysicalBone3D_property_custom_integrator) | `false` |
| [float](class_float.md#class_float) | [friction](class_physicalbone3d.md#class_PhysicalBone3D_property_friction) | `1.0` |
| [float](class_float.md#class_float) | [gravity_scale](class_physicalbone3d.md#class_PhysicalBone3D_property_gravity_scale) | `1.0` |
| [Transform3D](class_transform3d.md#class_Transform3D) | [joint_offset](class_physicalbone3d.md#class_PhysicalBone3D_property_joint_offset) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |
| [Vector3](class_vector3.md#class_Vector3) | [joint_rotation](class_physicalbone3d.md#class_PhysicalBone3D_property_joint_rotation) | `Vector3(0, 0, 0)` |
| [JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) | [joint_type](class_physicalbone3d.md#class_PhysicalBone3D_property_joint_type) | `0` |
| [float](class_float.md#class_float) | [linear_damp](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_damp) | `0.0` |
| [DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) | [linear_damp_mode](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_damp_mode) | `0` |
| [Vector3](class_vector3.md#class_Vector3) | [linear_velocity](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_velocity) | `Vector3(0, 0, 0)` |
| [float](class_float.md#class_float) | [mass](class_physicalbone3d.md#class_PhysicalBone3D_property_mass) | `1.0` |

### Methods


| void | [_integrate_forces](class_physicalbone3d.md#class_PhysicalBone3D_private_method__integrate_forces) ( state: [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class_PhysicsDirectBodyState3D) ) virtual |
| --- | --- |
| void | [apply_central_impulse](class_physicalbone3d.md#class_PhysicalBone3D_method_apply_central_impulse) ( impulse: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [apply_impulse](class_physicalbone3d.md#class_PhysicalBone3D_method_apply_impulse) ( impulse: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 0, 0) ) |
| [int](class_int.md#class_int) | [get_bone_id](class_physicalbone3d.md#class_PhysicalBone3D_method_get_bone_id) ( ) const |
| [bool](class_bool.md#class_bool) | [get_simulate_physics](class_physicalbone3d.md#class_PhysicalBone3D_method_get_simulate_physics) ( ) |
| [bool](class_bool.md#class_bool) | [is_simulating_physics](class_physicalbone3d.md#class_PhysicalBone3D_method_is_simulating_physics) ( ) |

---

### Enumerations

<span id="enum_PhysicalBone3D_DampMode"></span>

enum **DampMode**: [🔗](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode)

<span id="class_PhysicalBone3D_constant_DAMP_MODE_COMBINE"></span>

[DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) **DAMP_MODE_COMBINE** = `0`

In this mode, the body's damping value is added to any value set in areas or the default value.

<span id="class_PhysicalBone3D_constant_DAMP_MODE_REPLACE"></span>

[DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) **DAMP_MODE_REPLACE** = `1`

In this mode, the body's damping value replaces any value set in areas or the default value.

---

<span id="enum_PhysicalBone3D_JointType"></span>

enum **JointType**: [🔗](class_physicalbone3d.md#enum_PhysicalBone3D_JointType)

<span id="class_PhysicalBone3D_constant_JOINT_TYPE_NONE"></span>

[JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) **JOINT_TYPE_NONE** = `0`

No joint is applied to the PhysicsBone3D.

<span id="class_PhysicalBone3D_constant_JOINT_TYPE_PIN"></span>

[JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) **JOINT_TYPE_PIN** = `1`

A pin joint is applied to the PhysicsBone3D.

<span id="class_PhysicalBone3D_constant_JOINT_TYPE_CONE"></span>

[JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) **JOINT_TYPE_CONE** = `2`

A cone joint is applied to the PhysicsBone3D.

<span id="class_PhysicalBone3D_constant_JOINT_TYPE_HINGE"></span>

[JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) **JOINT_TYPE_HINGE** = `3`

A hinge joint is applied to the PhysicsBone3D.

<span id="class_PhysicalBone3D_constant_JOINT_TYPE_SLIDER"></span>

[JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) **JOINT_TYPE_SLIDER** = `4`

A slider joint is applied to the PhysicsBone3D.

<span id="class_PhysicalBone3D_constant_JOINT_TYPE_6DOF"></span>

[JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) **JOINT_TYPE_6DOF** = `5`

A 6 degrees of freedom joint is applied to the PhysicsBone3D.

---

### Property Descriptions

<span id="class_PhysicalBone3D_property_angular_damp"></span>

[float](class_float.md#class_float) **angular_damp** = `0.0` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_damp)

- void **set_angular_damp** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_angular_damp** ( )

Damps the body's rotation. By default, the body will use the ProjectSettings.physics/3d/default_angular_damp project setting or any value override set by an [Area3D](class_area3d.md#class_Area3D) the body is in. Depending on [angular_damp_mode](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_damp_mode), you can set [angular_damp](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_damp) to be added to or to replace the body's damping value.

See ProjectSettings.physics/3d/default_angular_damp for more details about damping.

---

<span id="class_PhysicalBone3D_property_angular_damp_mode"></span>

[DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) **angular_damp_mode** = `0` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_damp_mode)

- void **set_angular_damp_mode** ( value: [DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) )
- [DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) **get_angular_damp_mode** ( )

Defines how [angular_damp](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_damp) is applied.

---

<span id="class_PhysicalBone3D_property_angular_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **angular_velocity** = `Vector3(0, 0, 0)` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_velocity)

- void **set_angular_velocity** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_angular_velocity** ( )

The PhysicalBone3D's rotational velocity in *radians* per second.

---

<span id="class_PhysicalBone3D_property_body_offset"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **body_offset** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_body_offset)

- void **set_body_offset** ( value: [Transform3D](class_transform3d.md#class_Transform3D) )
- [Transform3D](class_transform3d.md#class_Transform3D) **get_body_offset** ( )

Sets the body's transform.

---

<span id="class_PhysicalBone3D_property_bounce"></span>

[float](class_float.md#class_float) **bounce** = `0.0` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_bounce)

- void **set_bounce** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_bounce** ( )

The body's bounciness. Values range from `0` (no bounce) to `1` (full bounciness).

 **Note:** Even with [bounce](class_physicalbone3d.md#class_PhysicalBone3D_property_bounce) set to `1.0`, some energy will be lost over time due to linear and angular damping. To have a **PhysicalBone3D** that preserves all its energy over time, set [bounce](class_physicalbone3d.md#class_PhysicalBone3D_property_bounce) to `1.0`, [linear_damp_mode](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_damp_mode) to [DAMP_MODE_REPLACE](class_physicalbone3d.md#class_PhysicalBone3D_constant_DAMP_MODE_REPLACE), [linear_damp](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_damp) to `0.0`, [angular_damp_mode](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_damp_mode) to [DAMP_MODE_REPLACE](class_physicalbone3d.md#class_PhysicalBone3D_constant_DAMP_MODE_REPLACE), and [angular_damp](class_physicalbone3d.md#class_PhysicalBone3D_property_angular_damp) to `0.0`.

---

<span id="class_PhysicalBone3D_property_can_sleep"></span>

[bool](class_bool.md#class_bool) **can_sleep** = `true` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_can_sleep)

- void **set_can_sleep** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_able_to_sleep** ( )

If `true`, the body is deactivated when there is no movement, so it will not take part in the simulation until it is awakened by an external force.

---

<span id="class_PhysicalBone3D_property_custom_integrator"></span>

[bool](class_bool.md#class_bool) **custom_integrator** = `false` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_custom_integrator)

- void **set_use_custom_integrator** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_custom_integrator** ( )

If `true`, the standard force integration (like gravity or damping) will be disabled for this body. Other than collision response, the body will only move as determined by the [_integrate_forces()](class_physicalbone3d.md#class_PhysicalBone3D_private_method__integrate_forces) method, if that virtual method is overridden.

Setting this property will call the method [PhysicsServer3D.body_set_omit_force_integration()](class_physicsserver3d.md#class_PhysicsServer3D_method_body_set_omit_force_integration) internally.

---

<span id="class_PhysicalBone3D_property_friction"></span>

[float](class_float.md#class_float) **friction** = `1.0` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_friction)

- void **set_friction** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_friction** ( )

The body's friction, from `0` (frictionless) to `1` (max friction).

---

<span id="class_PhysicalBone3D_property_gravity_scale"></span>

[float](class_float.md#class_float) **gravity_scale** = `1.0` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_gravity_scale)

- void **set_gravity_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_gravity_scale** ( )

This is multiplied by ProjectSettings.physics/3d/default_gravity to produce this body's gravity. For example, a value of `1.0` will apply normal gravity, `2.0` will apply double the gravity, and `0.5` will apply half the gravity to this body.

---

<span id="class_PhysicalBone3D_property_joint_offset"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **joint_offset** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_joint_offset)

- void **set_joint_offset** ( value: [Transform3D](class_transform3d.md#class_Transform3D) )
- [Transform3D](class_transform3d.md#class_Transform3D) **get_joint_offset** ( )

Sets the joint's transform.

---

<span id="class_PhysicalBone3D_property_joint_rotation"></span>

[Vector3](class_vector3.md#class_Vector3) **joint_rotation** = `Vector3(0, 0, 0)` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_joint_rotation)

- void **set_joint_rotation** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_joint_rotation** ( )

Sets the joint's rotation in radians.

---

<span id="class_PhysicalBone3D_property_joint_type"></span>

[JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) **joint_type** = `0` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_joint_type)

- void **set_joint_type** ( value: [JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) )
- [JointType](class_physicalbone3d.md#enum_PhysicalBone3D_JointType) **get_joint_type** ( )

Sets the joint type.

---

<span id="class_PhysicalBone3D_property_linear_damp"></span>

[float](class_float.md#class_float) **linear_damp** = `0.0` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_damp)

- void **set_linear_damp** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_linear_damp** ( )

Damps the body's movement. By default, the body will use ProjectSettings.physics/3d/default_linear_damp or any value override set by an [Area3D](class_area3d.md#class_Area3D) the body is in. Depending on [linear_damp_mode](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_damp_mode), [linear_damp](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_damp) may be added to or replace the body's damping value.

See ProjectSettings.physics/3d/default_linear_damp for more details about damping.

---

<span id="class_PhysicalBone3D_property_linear_damp_mode"></span>

[DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) **linear_damp_mode** = `0` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_damp_mode)

- void **set_linear_damp_mode** ( value: [DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) )
- [DampMode](class_physicalbone3d.md#enum_PhysicalBone3D_DampMode) **get_linear_damp_mode** ( )

Defines how [linear_damp](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_damp) is applied.

---

<span id="class_PhysicalBone3D_property_linear_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **linear_velocity** = `Vector3(0, 0, 0)` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_linear_velocity)

- void **set_linear_velocity** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_linear_velocity** ( )

The body's linear velocity in units per second. Can be used sporadically, but **don't set this every frame**, because physics may run in another thread and runs at a different granularity. Use [_integrate_forces()](class_physicalbone3d.md#class_PhysicalBone3D_private_method__integrate_forces) as your process loop for precise control of the body state.

---

<span id="class_PhysicalBone3D_property_mass"></span>

[float](class_float.md#class_float) **mass** = `1.0` [🔗](class_physicalbone3d.md#class_PhysicalBone3D_property_mass)

- void **set_mass** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_mass** ( )

The body's mass.

---

### Method Descriptions

<span id="class_PhysicalBone3D_private_method__integrate_forces"></span>

void **_integrate_forces** ( state: [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class_PhysicsDirectBodyState3D) ) *virtual* [🔗](class_physicalbone3d.md#class_PhysicalBone3D_private_method__integrate_forces)

Called during physics processing, allowing you to read and safely modify the simulation state for the object. By default, it is called before the standard force integration, but the [custom_integrator](class_physicalbone3d.md#class_PhysicalBone3D_property_custom_integrator) property allows you to disable the standard force integration and do fully custom force integration for a body.

---

<span id="class_PhysicalBone3D_method_apply_central_impulse"></span>

void **apply_central_impulse** ( impulse: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_physicalbone3d.md#class_PhysicalBone3D_method_apply_central_impulse)

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_integrate_forces" functions otherwise).

This is equivalent to using [apply_impulse()](class_physicalbone3d.md#class_PhysicalBone3D_method_apply_impulse) at the body's center of mass.

---

<span id="class_PhysicalBone3D_method_apply_impulse"></span>

void **apply_impulse** ( impulse: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 0, 0) ) [🔗](class_physicalbone3d.md#class_PhysicalBone3D_method_apply_impulse)

Applies a positioned impulse to the PhysicsBone3D.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_integrate_forces" functions otherwise).

 `position` is the offset from the PhysicsBone3D origin in global coordinates.

---

<span id="class_PhysicalBone3D_method_get_bone_id"></span>

[int](class_int.md#class_int) **get_bone_id** ( ) *const* [🔗](class_physicalbone3d.md#class_PhysicalBone3D_method_get_bone_id)

Returns the unique identifier of the PhysicsBone3D.

---

<span id="class_PhysicalBone3D_method_get_simulate_physics"></span>

[bool](class_bool.md#class_bool) **get_simulate_physics** ( ) [🔗](class_physicalbone3d.md#class_PhysicalBone3D_method_get_simulate_physics)

Returns `true` if the PhysicsBone3D is allowed to simulate physics.

---

<span id="class_PhysicalBone3D_method_is_simulating_physics"></span>

[bool](class_bool.md#class_bool) **is_simulating_physics** ( ) [🔗](class_physicalbone3d.md#class_PhysicalBone3D_method_is_simulating_physics)

Returns `true` if the PhysicsBone3D is currently simulating physics.
