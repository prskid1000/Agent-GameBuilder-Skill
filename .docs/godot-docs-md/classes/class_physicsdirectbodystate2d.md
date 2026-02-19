<span id="class_PhysicsDirectBodyState2D"></span>

## PhysicsDirectBodyState2D

**Inherits:** [Object](class_object.md#class_Object)

**Inherited By:** [PhysicsDirectBodyState2DExtension](class_physicsdirectbodystate2dextension.md#class_PhysicsDirectBodyState2DExtension)

Provides direct access to a physics body in the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D).

### Description

Provides direct access to a physics body in the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D), allowing safe changes to physics properties. This object is passed via the direct state callback of [RigidBody2D](class_rigidbody2d.md#class_RigidBody2D), and is intended for changing the direct state of that body. See [RigidBody2D._integrate_forces()](class_rigidbody2d.md#class_RigidBody2D_private_method__integrate_forces).

### Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

- [Ray-casting](../tutorials/physics/ray-casting.md)

### Properties


| [float](class_float.md#class_float) | [angular_velocity](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_angular_velocity) |
| --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [center_of_mass](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_center_of_mass) |
| [Vector2](class_vector2.md#class_Vector2) | [center_of_mass_local](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_center_of_mass_local) |
| [int](class_int.md#class_int) | [collision_layer](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_collision_layer) |
| [int](class_int.md#class_int) | [collision_mask](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_collision_mask) |
| [float](class_float.md#class_float) | [inverse_inertia](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_inertia) |
| [float](class_float.md#class_float) | [inverse_mass](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_mass) |
| [Vector2](class_vector2.md#class_Vector2) | [linear_velocity](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_linear_velocity) |
| [bool](class_bool.md#class_bool) | [sleeping](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_sleeping) |
| [float](class_float.md#class_float) | [step](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_step) |
| [float](class_float.md#class_float) | [total_angular_damp](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_total_angular_damp) |
| [Vector2](class_vector2.md#class_Vector2) | [total_gravity](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_total_gravity) |
| [float](class_float.md#class_float) | [total_linear_damp](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_total_linear_damp) |
| [Transform2D](class_transform2d.md#class_Transform2D) | [transform](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_transform) |

### Methods


| void | [add_constant_central_force](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_central_force) ( force: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| --- | --- |
| void | [add_constant_force](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_force) ( force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| void | [add_constant_torque](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_torque) ( torque: [float](class_float.md#class_float) ) |
| void | [apply_central_force](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_central_force) ( force: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| void | [apply_central_impulse](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_central_impulse) ( impulse: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [apply_force](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_force) ( force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| void | [apply_impulse](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_impulse) ( impulse: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| void | [apply_torque](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_torque) ( torque: [float](class_float.md#class_float) ) |
| void | [apply_torque_impulse](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_torque_impulse) ( impulse: [float](class_float.md#class_float) ) |
| [Vector2](class_vector2.md#class_Vector2) | [get_constant_force](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_constant_force) ( ) const |
| [float](class_float.md#class_float) | [get_constant_torque](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_constant_torque) ( ) const |
| [RID](class_rid.md#class_RID) | [get_contact_collider](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider) ( contact_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_contact_collider_id](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_id) ( contact_idx: [int](class_int.md#class_int) ) const |
| [Object](class_object.md#class_Object) | [get_contact_collider_object](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_object) ( contact_idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_contact_collider_position](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_position) ( contact_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_contact_collider_shape](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_shape) ( contact_idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_contact_collider_velocity_at_position](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_velocity_at_position) ( contact_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_contact_count](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_count) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_contact_impulse](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_impulse) ( contact_idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_contact_local_normal](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_local_normal) ( contact_idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_contact_local_position](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_local_position) ( contact_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_contact_local_shape](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_local_shape) ( contact_idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_contact_local_velocity_at_position](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_local_velocity_at_position) ( contact_idx: [int](class_int.md#class_int) ) const |
| [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) | [get_space_state](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_space_state) ( ) |
| [Vector2](class_vector2.md#class_Vector2) | [get_velocity_at_local_position](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_velocity_at_local_position) ( local_position: [Vector2](class_vector2.md#class_Vector2) ) const |
| void | [integrate_forces](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_integrate_forces) ( ) |
| void | [set_constant_force](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_set_constant_force) ( force: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_constant_torque](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_set_constant_torque) ( torque: [float](class_float.md#class_float) ) |

---

### Property Descriptions

<span id="class_PhysicsDirectBodyState2D_property_angular_velocity"></span>

[float](class_float.md#class_float) **angular_velocity** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_angular_velocity)

- void **set_angular_velocity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_angular_velocity** ( )

The body's rotational velocity in *radians* per second.

---

<span id="class_PhysicsDirectBodyState2D_property_center_of_mass"></span>

[Vector2](class_vector2.md#class_Vector2) **center_of_mass** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_center_of_mass)

- [Vector2](class_vector2.md#class_Vector2) **get_center_of_mass** ( )

The body's center of mass position relative to the body's center in the global coordinate system.

---

<span id="class_PhysicsDirectBodyState2D_property_center_of_mass_local"></span>

[Vector2](class_vector2.md#class_Vector2) **center_of_mass_local** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_center_of_mass_local)

- [Vector2](class_vector2.md#class_Vector2) **get_center_of_mass_local** ( )

The body's center of mass position in the body's local coordinate system.

---

<span id="class_PhysicsDirectBodyState2D_property_collision_layer"></span>

[int](class_int.md#class_int) **collision_layer** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_collision_layer)

- void **set_collision_layer** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_layer** ( )

The body's collision layer.

---

<span id="class_PhysicsDirectBodyState2D_property_collision_mask"></span>

[int](class_int.md#class_int) **collision_mask** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The body's collision mask.

---

<span id="class_PhysicsDirectBodyState2D_property_inverse_inertia"></span>

[float](class_float.md#class_float) **inverse_inertia** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_inertia)

- [float](class_float.md#class_float) **get_inverse_inertia** ( )

The inverse of the inertia of the body.

---

<span id="class_PhysicsDirectBodyState2D_property_inverse_mass"></span>

[float](class_float.md#class_float) **inverse_mass** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_mass)

- [float](class_float.md#class_float) **get_inverse_mass** ( )

The inverse of the mass of the body.

---

<span id="class_PhysicsDirectBodyState2D_property_linear_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **linear_velocity** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_linear_velocity)

- void **set_linear_velocity** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_linear_velocity** ( )

The body's linear velocity in pixels per second.

---

<span id="class_PhysicsDirectBodyState2D_property_sleeping"></span>

[bool](class_bool.md#class_bool) **sleeping** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_sleeping)

- void **set_sleep_state** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_sleeping** ( )

If `true`, this body is currently sleeping (not active).

---

<span id="class_PhysicsDirectBodyState2D_property_step"></span>

[float](class_float.md#class_float) **step** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_step)

- [float](class_float.md#class_float) **get_step** ( )

The timestep (delta) used for the simulation.

---

<span id="class_PhysicsDirectBodyState2D_property_total_angular_damp"></span>

[float](class_float.md#class_float) **total_angular_damp** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_total_angular_damp)

- [float](class_float.md#class_float) **get_total_angular_damp** ( )

The rate at which the body stops rotating, if there are not any other forces moving it.

---

<span id="class_PhysicsDirectBodyState2D_property_total_gravity"></span>

[Vector2](class_vector2.md#class_Vector2) **total_gravity** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_total_gravity)

- [Vector2](class_vector2.md#class_Vector2) **get_total_gravity** ( )

The total gravity vector being currently applied to this body.

---

<span id="class_PhysicsDirectBodyState2D_property_total_linear_damp"></span>

[float](class_float.md#class_float) **total_linear_damp** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_total_linear_damp)

- [float](class_float.md#class_float) **get_total_linear_damp** ( )

The rate at which the body stops moving, if there are not any other forces moving it.

---

<span id="class_PhysicsDirectBodyState2D_property_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **transform** [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_transform)

- void **set_transform** ( value: [Transform2D](class_transform2d.md#class_Transform2D) )
- [Transform2D](class_transform2d.md#class_Transform2D) **get_transform** ( )

The body's transformation matrix.

---

### Method Descriptions

<span id="class_PhysicsDirectBodyState2D_method_add_constant_central_force"></span>

void **add_constant_central_force** ( force: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_central_force)

Adds a constant directional force without affecting rotation that keeps being applied over time until cleared with `constant_force = Vector2(0, 0)`.

This is equivalent to using [add_constant_force()](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_force) at the body's center of mass.

---

<span id="class_PhysicsDirectBodyState2D_method_add_constant_force"></span>

void **add_constant_force** ( force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_force)

Adds a constant positioned force to the body that keeps being applied over time until cleared with `constant_force = Vector2(0, 0)`.

 `position` is the offset from the body origin in global coordinates.

---

<span id="class_PhysicsDirectBodyState2D_method_add_constant_torque"></span>

void **add_constant_torque** ( torque: [float](class_float.md#class_float) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_torque)

Adds a constant rotational force without affecting position that keeps being applied over time until cleared with `constant_torque = 0`.

---

<span id="class_PhysicsDirectBodyState2D_method_apply_central_force"></span>

void **apply_central_force** ( force: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_central_force)

Applies a directional force without affecting rotation. A force is time dependent and meant to be applied every physics update.

This is equivalent to using [apply_force()](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_force) at the body's center of mass.

---

<span id="class_PhysicsDirectBodyState2D_method_apply_central_impulse"></span>

void **apply_central_impulse** ( impulse: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_central_impulse)

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

This is equivalent to using [apply_impulse()](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_impulse) at the body's center of mass.

---

<span id="class_PhysicsDirectBodyState2D_method_apply_force"></span>

void **apply_force** ( force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_force)

Applies a positioned force to the body. A force is time dependent and meant to be applied every physics update.

 `position` is the offset from the body origin in global coordinates.

---

<span id="class_PhysicsDirectBodyState2D_method_apply_impulse"></span>

void **apply_impulse** ( impulse: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_impulse)

Applies a positioned impulse to the body.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

 `position` is the offset from the body origin in global coordinates.

---

<span id="class_PhysicsDirectBodyState2D_method_apply_torque"></span>

void **apply_torque** ( torque: [float](class_float.md#class_float) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_torque)

Applies a rotational force without affecting position. A force is time dependent and meant to be applied every physics update.

 **Note:** [inverse_inertia](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_inertia) is required for this to work. To have [inverse_inertia](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_inertia), an active [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) must be a child of the node, or you can manually set [inverse_inertia](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_inertia).

---

<span id="class_PhysicsDirectBodyState2D_method_apply_torque_impulse"></span>

void **apply_torque_impulse** ( impulse: [float](class_float.md#class_float) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_apply_torque_impulse)

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

 **Note:** [inverse_inertia](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_inertia) is required for this to work. To have [inverse_inertia](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_inertia), an active [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) must be a child of the node, or you can manually set [inverse_inertia](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_property_inverse_inertia).

---

<span id="class_PhysicsDirectBodyState2D_method_get_constant_force"></span>

[Vector2](class_vector2.md#class_Vector2) **get_constant_force** ( ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_constant_force)

Returns the body's total constant positional forces applied during each physics update.

See [add_constant_force()](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_force) and [add_constant_central_force()](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_central_force).

---

<span id="class_PhysicsDirectBodyState2D_method_get_constant_torque"></span>

[float](class_float.md#class_float) **get_constant_torque** ( ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_constant_torque)

Returns the body's total constant rotational forces applied during each physics update.

See [add_constant_torque()](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_torque).

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_collider"></span>

[RID](class_rid.md#class_RID) **get_contact_collider** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider)

Returns the collider's [RID](class_rid.md#class_RID).

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_collider_id"></span>

[int](class_int.md#class_int) **get_contact_collider_id** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_id)

Returns the collider's object id.

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_collider_object"></span>

[Object](class_object.md#class_Object) **get_contact_collider_object** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_object)

Returns the collider object. This depends on how it was created (will return a scene node if such was used to create it).

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_collider_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_contact_collider_position** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_position)

Returns the position of the contact point on the collider in the global coordinate system.

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_collider_shape"></span>

[int](class_int.md#class_int) **get_contact_collider_shape** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_shape)

Returns the collider's shape index.

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_collider_velocity_at_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_contact_collider_velocity_at_position** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_collider_velocity_at_position)

Returns the velocity vector at the collider's contact point.

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_count"></span>

[int](class_int.md#class_int) **get_contact_count** ( ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_count)

Returns the number of contacts this body has with other bodies.

 **Note:** By default, this returns 0 unless bodies are configured to monitor contacts. See [RigidBody2D.contact_monitor](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor).

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_impulse"></span>

[Vector2](class_vector2.md#class_Vector2) **get_contact_impulse** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_impulse)

Returns the impulse created by the contact.

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_local_normal"></span>

[Vector2](class_vector2.md#class_Vector2) **get_contact_local_normal** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_local_normal)

Returns the local normal at the contact point.

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_local_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_contact_local_position** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_local_position)

Returns the position of the contact point on the body in the global coordinate system.

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_local_shape"></span>

[int](class_int.md#class_int) **get_contact_local_shape** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_local_shape)

Returns the local shape index of the collision.

---

<span id="class_PhysicsDirectBodyState2D_method_get_contact_local_velocity_at_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_contact_local_velocity_at_position** ( contact_idx: [int](class_int.md#class_int) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_contact_local_velocity_at_position)

Returns the velocity vector at the body's contact point.

---

<span id="class_PhysicsDirectBodyState2D_method_get_space_state"></span>

[PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) **get_space_state** ( ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_space_state)

Returns the current state of the space, useful for queries.

---

<span id="class_PhysicsDirectBodyState2D_method_get_velocity_at_local_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_velocity_at_local_position** ( local_position: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_get_velocity_at_local_position)

Returns the body's velocity at the given relative position.

 `local_position` is the offset from the body origin in global coordinates.

---

<span id="class_PhysicsDirectBodyState2D_method_integrate_forces"></span>

void **integrate_forces** ( ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_integrate_forces)

Updates the body's linear and angular velocity by applying gravity and damping for the equivalent of one physics tick.

---

<span id="class_PhysicsDirectBodyState2D_method_set_constant_force"></span>

void **set_constant_force** ( force: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_set_constant_force)

Sets the body's total constant positional forces applied during each physics update.

See [add_constant_force()](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_force) and [add_constant_central_force()](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_central_force).

---

<span id="class_PhysicsDirectBodyState2D_method_set_constant_torque"></span>

void **set_constant_torque** ( torque: [float](class_float.md#class_float) ) [🔗](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_set_constant_torque)

Sets the body's total constant rotational forces applied during each physics update.

See [add_constant_torque()](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D_method_add_constant_torque).
