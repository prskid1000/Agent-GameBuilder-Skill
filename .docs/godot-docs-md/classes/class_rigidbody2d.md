<span id="class_RigidBody2D"></span>

## RigidBody2D

**Inherits:** [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) **<** [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D)

A 2D physics body that is moved by a physics simulation.

### Description

**RigidBody2D** implements full 2D physics. It cannot be controlled directly, instead, you must apply forces to it (gravity, impulses, etc.), and the physics simulation will calculate the resulting movement, rotation, react to collisions, and affect other physics bodies in its path.

The body's behavior can be adjusted via [lock_rotation](class_rigidbody2d.md#class_RigidBody2D_property_lock_rotation), [freeze](class_rigidbody2d.md#class_RigidBody2D_property_freeze), and [freeze_mode](class_rigidbody2d.md#class_RigidBody2D_property_freeze_mode). By changing various properties of the object, such as [mass](class_rigidbody2d.md#class_RigidBody2D_property_mass), you can control how the physics simulation acts on it.

A rigid body will always maintain its shape and size, even when forces are applied to it. It is useful for objects that can be interacted with in an environment, such as a tree that can be knocked over or a stack of crates that can be pushed around.

If you need to directly affect the body, prefer [_integrate_forces()](class_rigidbody2d.md#class_RigidBody2D_private_method__integrate_forces) as it allows you to directly access the physics state.

If you need to override the default physics behavior, you can write a custom force integration function. See [custom_integrator](class_rigidbody2d.md#class_RigidBody2D_property_custom_integrator).

 **Note:** Changing the 2D transform or [linear_velocity](class_rigidbody2d.md#class_RigidBody2D_property_linear_velocity) of a **RigidBody2D** very often may lead to some unpredictable behaviors. This also happens when a **RigidBody2D** is the descendant of a constantly moving node, like another **RigidBody2D**, as that will cause its global transform to be set whenever its ancestor moves.

### Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)

- 2D Physics Platformer Demo

- Instancing Demo

### Properties


| [float](class_float.md#class_float) | [angular_damp](class_rigidbody2d.md#class_RigidBody2D_property_angular_damp) | `0.0` |
| --- | --- | --- |
| [DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) | [angular_damp_mode](class_rigidbody2d.md#class_RigidBody2D_property_angular_damp_mode) | `0` |
| [float](class_float.md#class_float) | [angular_velocity](class_rigidbody2d.md#class_RigidBody2D_property_angular_velocity) | `0.0` |
| [bool](class_bool.md#class_bool) | [can_sleep](class_rigidbody2d.md#class_RigidBody2D_property_can_sleep) | `true` |
| [Vector2](class_vector2.md#class_Vector2) | [center_of_mass](class_rigidbody2d.md#class_RigidBody2D_property_center_of_mass) | `Vector2(0, 0)` |
| [CenterOfMassMode](class_rigidbody2d.md#enum_RigidBody2D_CenterOfMassMode) | [center_of_mass_mode](class_rigidbody2d.md#class_RigidBody2D_property_center_of_mass_mode) | `0` |
| [Vector2](class_vector2.md#class_Vector2) | [constant_force](class_rigidbody2d.md#class_RigidBody2D_property_constant_force) | `Vector2(0, 0)` |
| [float](class_float.md#class_float) | [constant_torque](class_rigidbody2d.md#class_RigidBody2D_property_constant_torque) | `0.0` |
| [bool](class_bool.md#class_bool) | [contact_monitor](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor) | `false` |
| [CCDMode](class_rigidbody2d.md#enum_RigidBody2D_CCDMode) | [continuous_cd](class_rigidbody2d.md#class_RigidBody2D_property_continuous_cd) | `0` |
| [bool](class_bool.md#class_bool) | [custom_integrator](class_rigidbody2d.md#class_RigidBody2D_property_custom_integrator) | `false` |
| [bool](class_bool.md#class_bool) | [freeze](class_rigidbody2d.md#class_RigidBody2D_property_freeze) | `false` |
| [FreezeMode](class_rigidbody2d.md#enum_RigidBody2D_FreezeMode) | [freeze_mode](class_rigidbody2d.md#class_RigidBody2D_property_freeze_mode) | `0` |
| [float](class_float.md#class_float) | [gravity_scale](class_rigidbody2d.md#class_RigidBody2D_property_gravity_scale) | `1.0` |
| [float](class_float.md#class_float) | [inertia](class_rigidbody2d.md#class_RigidBody2D_property_inertia) | `0.0` |
| [float](class_float.md#class_float) | [linear_damp](class_rigidbody2d.md#class_RigidBody2D_property_linear_damp) | `0.0` |
| [DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) | [linear_damp_mode](class_rigidbody2d.md#class_RigidBody2D_property_linear_damp_mode) | `0` |
| [Vector2](class_vector2.md#class_Vector2) | [linear_velocity](class_rigidbody2d.md#class_RigidBody2D_property_linear_velocity) | `Vector2(0, 0)` |
| [bool](class_bool.md#class_bool) | [lock_rotation](class_rigidbody2d.md#class_RigidBody2D_property_lock_rotation) | `false` |
| [float](class_float.md#class_float) | [mass](class_rigidbody2d.md#class_RigidBody2D_property_mass) | `1.0` |
| [int](class_int.md#class_int) | [max_contacts_reported](class_rigidbody2d.md#class_RigidBody2D_property_max_contacts_reported) | `0` |
| [PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) | [physics_material_override](class_rigidbody2d.md#class_RigidBody2D_property_physics_material_override) |
| [bool](class_bool.md#class_bool) | [sleeping](class_rigidbody2d.md#class_RigidBody2D_property_sleeping) | `false` |

### Methods


| void | [_integrate_forces](class_rigidbody2d.md#class_RigidBody2D_private_method__integrate_forces) ( state: [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D) ) virtual |
| --- | --- |
| void | [add_constant_central_force](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_central_force) ( force: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [add_constant_force](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_force) ( force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| void | [add_constant_torque](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_torque) ( torque: [float](class_float.md#class_float) ) |
| void | [apply_central_force](class_rigidbody2d.md#class_RigidBody2D_method_apply_central_force) ( force: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [apply_central_impulse](class_rigidbody2d.md#class_RigidBody2D_method_apply_central_impulse) ( impulse: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| void | [apply_force](class_rigidbody2d.md#class_RigidBody2D_method_apply_force) ( force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| void | [apply_impulse](class_rigidbody2d.md#class_RigidBody2D_method_apply_impulse) ( impulse: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| void | [apply_torque](class_rigidbody2d.md#class_RigidBody2D_method_apply_torque) ( torque: [float](class_float.md#class_float) ) |
| void | [apply_torque_impulse](class_rigidbody2d.md#class_RigidBody2D_method_apply_torque_impulse) ( torque: [float](class_float.md#class_float) ) |
| [Array](class_array.md#class_Array)\[[Node2D](class_node2d.md#class_Node2D)\] | [get_colliding_bodies](class_rigidbody2d.md#class_RigidBody2D_method_get_colliding_bodies) ( ) const |
| [int](class_int.md#class_int) | [get_contact_count](class_rigidbody2d.md#class_RigidBody2D_method_get_contact_count) ( ) const |
| void | [set_axis_velocity](class_rigidbody2d.md#class_RigidBody2D_method_set_axis_velocity) ( axis_velocity: [Vector2](class_vector2.md#class_Vector2) ) |

---

### Signals

<span id="class_RigidBody2D_signal_body_entered"></span>

**body_entered** ( body: [Node](class_node.md#class_Node) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_signal_body_entered)

Emitted when a collision with another [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap) occurs. Requires [contact_monitor](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor) to be set to `true` and [max_contacts_reported](class_rigidbody2d.md#class_RigidBody2D_property_max_contacts_reported) to be set high enough to detect all the collisions. [TileMap](class_tilemap.md#class_TileMap) s are detected if the [TileSet](class_tileset.md#class_TileSet) has Collision [Shape2D](class_shape2d.md#class_Shape2D) s.

 `body` the [Node](class_node.md#class_Node), if it exists in the tree, of the other [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap).

---

<span id="class_RigidBody2D_signal_body_exited"></span>

**body_exited** ( body: [Node](class_node.md#class_Node) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_signal_body_exited)

Emitted when the collision with another [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap) ends. Requires [contact_monitor](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor) to be set to `true` and [max_contacts_reported](class_rigidbody2d.md#class_RigidBody2D_property_max_contacts_reported) to be set high enough to detect all the collisions. [TileMap](class_tilemap.md#class_TileMap) s are detected if the [TileSet](class_tileset.md#class_TileSet) has Collision [Shape2D](class_shape2d.md#class_Shape2D) s.

 `body` the [Node](class_node.md#class_Node), if it exists in the tree, of the other [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap).

---

<span id="class_RigidBody2D_signal_body_shape_entered"></span>

**body_shape_entered** ( body_rid: [RID](class_rid.md#class_RID), body: [Node](class_node.md#class_Node), body_shape_index: [int](class_int.md#class_int), local_shape_index: [int](class_int.md#class_int) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_signal_body_shape_entered)

Emitted when one of this RigidBody2D's [Shape2D](class_shape2d.md#class_Shape2D) s collides with another [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap)'s [Shape2D](class_shape2d.md#class_Shape2D) s. Requires [contact_monitor](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor) to be set to `true` and [max_contacts_reported](class_rigidbody2d.md#class_RigidBody2D_property_max_contacts_reported) to be set high enough to detect all the collisions. [TileMap](class_tilemap.md#class_TileMap) s are detected if the [TileSet](class_tileset.md#class_TileSet) has Collision [Shape2D](class_shape2d.md#class_Shape2D) s.

 `body_rid` the [RID](class_rid.md#class_RID) of the other [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileSet](class_tileset.md#class_TileSet)'s [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) used by the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D).

 `body` the [Node](class_node.md#class_Node), if it exists in the tree, of the other [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap).

 `body_shape_index` the index of the [Shape2D](class_shape2d.md#class_Shape2D) of the other [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap) used by the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D). Get the [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) node with `body.shape_owner_get_owner(body.shape_find_owner(body_shape_index))`.

 `local_shape_index` the index of the [Shape2D](class_shape2d.md#class_Shape2D) of this RigidBody2D used by the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D). Get the [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) node with `self.shape_owner_get_owner(self.shape_find_owner(local_shape_index))`.

---

<span id="class_RigidBody2D_signal_body_shape_exited"></span>

**body_shape_exited** ( body_rid: [RID](class_rid.md#class_RID), body: [Node](class_node.md#class_Node), body_shape_index: [int](class_int.md#class_int), local_shape_index: [int](class_int.md#class_int) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_signal_body_shape_exited)

Emitted when the collision between one of this RigidBody2D's [Shape2D](class_shape2d.md#class_Shape2D) s and another [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap)'s [Shape2D](class_shape2d.md#class_Shape2D) s ends. Requires [contact_monitor](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor) to be set to `true` and [max_contacts_reported](class_rigidbody2d.md#class_RigidBody2D_property_max_contacts_reported) to be set high enough to detect all the collisions. [TileMap](class_tilemap.md#class_TileMap) s are detected if the [TileSet](class_tileset.md#class_TileSet) has Collision [Shape2D](class_shape2d.md#class_Shape2D) s.

 `body_rid` the [RID](class_rid.md#class_RID) of the other [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileSet](class_tileset.md#class_TileSet)'s [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) used by the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D).

 `body` the [Node](class_node.md#class_Node), if it exists in the tree, of the other [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap).

 `body_shape_index` the index of the [Shape2D](class_shape2d.md#class_Shape2D) of the other [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or [TileMap](class_tilemap.md#class_TileMap) used by the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D). Get the [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) node with `body.shape_owner_get_owner(body.shape_find_owner(body_shape_index))`.

 `local_shape_index` the index of the [Shape2D](class_shape2d.md#class_Shape2D) of this RigidBody2D used by the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D). Get the [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) node with `self.shape_owner_get_owner(self.shape_find_owner(local_shape_index))`.

---

<span id="class_RigidBody2D_signal_sleeping_state_changed"></span>

**sleeping_state_changed** ( ) [🔗](class_rigidbody2d.md#class_RigidBody2D_signal_sleeping_state_changed)

Emitted when the physics engine changes the body's sleeping state.

 **Note:** Changing the value [sleeping](class_rigidbody2d.md#class_RigidBody2D_property_sleeping) will not trigger this signal. It is only emitted if the sleeping state is changed by the physics engine or `emit_signal("sleeping_state_changed")` is used.

---

### Enumerations

<span id="enum_RigidBody2D_FreezeMode"></span>

enum **FreezeMode**: [🔗](class_rigidbody2d.md#enum_RigidBody2D_FreezeMode)

<span id="class_RigidBody2D_constant_FREEZE_MODE_STATIC"></span>

[FreezeMode](class_rigidbody2d.md#enum_RigidBody2D_FreezeMode) **FREEZE_MODE_STATIC** = `0`

Static body freeze mode (default). The body is not affected by gravity and forces. It can be only moved by user code and doesn't collide with other bodies along its path.

<span id="class_RigidBody2D_constant_FREEZE_MODE_KINEMATIC"></span>

[FreezeMode](class_rigidbody2d.md#enum_RigidBody2D_FreezeMode) **FREEZE_MODE_KINEMATIC** = `1`

Kinematic body freeze mode. Similar to [FREEZE_MODE_STATIC](class_rigidbody2d.md#class_RigidBody2D_constant_FREEZE_MODE_STATIC), but collides with other bodies along its path when moved. Useful for a frozen body that needs to be animated.

---

<span id="enum_RigidBody2D_CenterOfMassMode"></span>

enum **CenterOfMassMode**: [🔗](class_rigidbody2d.md#enum_RigidBody2D_CenterOfMassMode)

<span id="class_RigidBody2D_constant_CENTER_OF_MASS_MODE_AUTO"></span>

[CenterOfMassMode](class_rigidbody2d.md#enum_RigidBody2D_CenterOfMassMode) **CENTER_OF_MASS_MODE_AUTO** = `0`

In this mode, the body's center of mass is calculated automatically based on its shapes. This assumes that the shapes' origins are also their center of mass.

<span id="class_RigidBody2D_constant_CENTER_OF_MASS_MODE_CUSTOM"></span>

[CenterOfMassMode](class_rigidbody2d.md#enum_RigidBody2D_CenterOfMassMode) **CENTER_OF_MASS_MODE_CUSTOM** = `1`

In this mode, the body's center of mass is set through [center_of_mass](class_rigidbody2d.md#class_RigidBody2D_property_center_of_mass). Defaults to the body's origin position.

---

<span id="enum_RigidBody2D_DampMode"></span>

enum **DampMode**: [🔗](class_rigidbody2d.md#enum_RigidBody2D_DampMode)

<span id="class_RigidBody2D_constant_DAMP_MODE_COMBINE"></span>

[DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) **DAMP_MODE_COMBINE** = `0`

In this mode, the body's damping value is added to any value set in areas or the default value.

<span id="class_RigidBody2D_constant_DAMP_MODE_REPLACE"></span>

[DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) **DAMP_MODE_REPLACE** = `1`

In this mode, the body's damping value replaces any value set in areas or the default value.

---

<span id="enum_RigidBody2D_CCDMode"></span>

enum **CCDMode**: [🔗](class_rigidbody2d.md#enum_RigidBody2D_CCDMode)

<span id="class_RigidBody2D_constant_CCD_MODE_DISABLED"></span>

[CCDMode](class_rigidbody2d.md#enum_RigidBody2D_CCDMode) **CCD_MODE_DISABLED** = `0`

Continuous collision detection disabled. This is the fastest way to detect body collisions, but can miss small, fast-moving objects.

<span id="class_RigidBody2D_constant_CCD_MODE_CAST_RAY"></span>

[CCDMode](class_rigidbody2d.md#enum_RigidBody2D_CCDMode) **CCD_MODE_CAST_RAY** = `1`

Continuous collision detection enabled using raycasting. This is faster than shapecasting but less precise.

<span id="class_RigidBody2D_constant_CCD_MODE_CAST_SHAPE"></span>

[CCDMode](class_rigidbody2d.md#enum_RigidBody2D_CCDMode) **CCD_MODE_CAST_SHAPE** = `2`

Continuous collision detection enabled using shapecasting. This is the slowest CCD method and the most precise.

---

### Property Descriptions

<span id="class_RigidBody2D_property_angular_damp"></span>

[float](class_float.md#class_float) **angular_damp** = `0.0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_angular_damp)

- void **set_angular_damp** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_angular_damp** ( )

Damps the body's rotation. By default, the body will use the ProjectSettings.physics/2d/default_angular_damp setting or any value override set by an [Area2D](class_area2d.md#class_Area2D) the body is in. Depending on [angular_damp_mode](class_rigidbody2d.md#class_RigidBody2D_property_angular_damp_mode), you can set [angular_damp](class_rigidbody2d.md#class_RigidBody2D_property_angular_damp) to be added to or to replace the body's damping value.

See ProjectSettings.physics/2d/default_angular_damp for more details about damping.

---

<span id="class_RigidBody2D_property_angular_damp_mode"></span>

[DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) **angular_damp_mode** = `0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_angular_damp_mode)

- void **set_angular_damp_mode** ( value: [DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) )
- [DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) **get_angular_damp_mode** ( )

Defines how [angular_damp](class_rigidbody2d.md#class_RigidBody2D_property_angular_damp) is applied.

---

<span id="class_RigidBody2D_property_angular_velocity"></span>

[float](class_float.md#class_float) **angular_velocity** = `0.0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_angular_velocity)

- void **set_angular_velocity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_angular_velocity** ( )

The body's rotational velocity in *radians* per second.

---

<span id="class_RigidBody2D_property_can_sleep"></span>

[bool](class_bool.md#class_bool) **can_sleep** = `true` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_can_sleep)

- void **set_can_sleep** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_able_to_sleep** ( )

If `true`, the body can enter sleep mode when there is no movement. See [sleeping](class_rigidbody2d.md#class_RigidBody2D_property_sleeping).

---

<span id="class_RigidBody2D_property_center_of_mass"></span>

[Vector2](class_vector2.md#class_Vector2) **center_of_mass** = `Vector2(0, 0)` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_center_of_mass)

- void **set_center_of_mass** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_center_of_mass** ( )

The body's custom center of mass, relative to the body's origin position, when [center_of_mass_mode](class_rigidbody2d.md#class_RigidBody2D_property_center_of_mass_mode) is set to [CENTER_OF_MASS_MODE_CUSTOM](class_rigidbody2d.md#class_RigidBody2D_constant_CENTER_OF_MASS_MODE_CUSTOM). This is the balanced point of the body, where applied forces only cause linear acceleration. Applying forces outside of the center of mass causes angular acceleration.

When [center_of_mass_mode](class_rigidbody2d.md#class_RigidBody2D_property_center_of_mass_mode) is set to [CENTER_OF_MASS_MODE_AUTO](class_rigidbody2d.md#class_RigidBody2D_constant_CENTER_OF_MASS_MODE_AUTO) (default value), the center of mass is automatically determined, but this does not update the value of [center_of_mass](class_rigidbody2d.md#class_RigidBody2D_property_center_of_mass).

---

<span id="class_RigidBody2D_property_center_of_mass_mode"></span>

[CenterOfMassMode](class_rigidbody2d.md#enum_RigidBody2D_CenterOfMassMode) **center_of_mass_mode** = `0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_center_of_mass_mode)

- void **set_center_of_mass_mode** ( value: [CenterOfMassMode](class_rigidbody2d.md#enum_RigidBody2D_CenterOfMassMode) )
- [CenterOfMassMode](class_rigidbody2d.md#enum_RigidBody2D_CenterOfMassMode) **get_center_of_mass_mode** ( )

Defines the way the body's center of mass is set.

---

<span id="class_RigidBody2D_property_constant_force"></span>

[Vector2](class_vector2.md#class_Vector2) **constant_force** = `Vector2(0, 0)` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_constant_force)

- void **set_constant_force** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_constant_force** ( )

The body's total constant positional forces applied during each physics update.

See [add_constant_force()](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_force) and [add_constant_central_force()](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_central_force).

---

<span id="class_RigidBody2D_property_constant_torque"></span>

[float](class_float.md#class_float) **constant_torque** = `0.0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_constant_torque)

- void **set_constant_torque** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_constant_torque** ( )

The body's total constant rotational forces applied during each physics update.

See [add_constant_torque()](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_torque).

---

<span id="class_RigidBody2D_property_contact_monitor"></span>

[bool](class_bool.md#class_bool) **contact_monitor** = `false` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor)

- void **set_contact_monitor** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_contact_monitor_enabled** ( )

If `true`, the RigidBody2D will emit signals when it collides with another body.

 **Note:** By default the maximum contacts reported is set to 0, meaning nothing will be recorded, see [max_contacts_reported](class_rigidbody2d.md#class_RigidBody2D_property_max_contacts_reported).

---

<span id="class_RigidBody2D_property_continuous_cd"></span>

[CCDMode](class_rigidbody2d.md#enum_RigidBody2D_CCDMode) **continuous_cd** = `0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_continuous_cd)

- void **set_continuous_collision_detection_mode** ( value: [CCDMode](class_rigidbody2d.md#enum_RigidBody2D_CCDMode) )
- [CCDMode](class_rigidbody2d.md#enum_RigidBody2D_CCDMode) **get_continuous_collision_detection_mode** ( )

Continuous collision detection mode.

Continuous collision detection tries to predict where a moving body will collide instead of moving it and correcting its movement after collision. Continuous collision detection is slower, but more precise and misses fewer collisions with small, fast-moving objects. Raycasting and shapecasting methods are available.

---

<span id="class_RigidBody2D_property_custom_integrator"></span>

[bool](class_bool.md#class_bool) **custom_integrator** = `false` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_custom_integrator)

- void **set_use_custom_integrator** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_custom_integrator** ( )

If `true`, the standard force integration (like gravity or damping) will be disabled for this body. Other than collision response, the body will only move as determined by the [_integrate_forces()](class_rigidbody2d.md#class_RigidBody2D_private_method__integrate_forces) method, if that virtual method is overridden.

Setting this property will call the method [PhysicsServer2D.body_set_omit_force_integration()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_omit_force_integration) internally.

---

<span id="class_RigidBody2D_property_freeze"></span>

[bool](class_bool.md#class_bool) **freeze** = `false` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_freeze)

- void **set_freeze_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_freeze_enabled** ( )

If `true`, the body is frozen. Gravity and forces are not applied anymore.

See [freeze_mode](class_rigidbody2d.md#class_RigidBody2D_property_freeze_mode) to set the body's behavior when frozen.

 **Note:** For a body that is always frozen, use [StaticBody2D](class_staticbody2d.md#class_StaticBody2D) or [AnimatableBody2D](class_animatablebody2d.md#class_AnimatableBody2D) instead.

---

<span id="class_RigidBody2D_property_freeze_mode"></span>

[FreezeMode](class_rigidbody2d.md#enum_RigidBody2D_FreezeMode) **freeze_mode** = `0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_freeze_mode)

- void **set_freeze_mode** ( value: [FreezeMode](class_rigidbody2d.md#enum_RigidBody2D_FreezeMode) )
- [FreezeMode](class_rigidbody2d.md#enum_RigidBody2D_FreezeMode) **get_freeze_mode** ( )

The body's freeze mode. Determines the body's behavior when [freeze](class_rigidbody2d.md#class_RigidBody2D_property_freeze) is `true`.

 **Note:** For a body that is always frozen, use [StaticBody2D](class_staticbody2d.md#class_StaticBody2D) or [AnimatableBody2D](class_animatablebody2d.md#class_AnimatableBody2D) instead.

---

<span id="class_RigidBody2D_property_gravity_scale"></span>

[float](class_float.md#class_float) **gravity_scale** = `1.0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_gravity_scale)

- void **set_gravity_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_gravity_scale** ( )

Multiplies the gravity applied to the body. The body's gravity is calculated from the ProjectSettings.physics/2d/default_gravity project setting and/or any additional gravity vector applied by [Area2D](class_area2d.md#class_Area2D) s.

---

<span id="class_RigidBody2D_property_inertia"></span>

[float](class_float.md#class_float) **inertia** = `0.0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_inertia)

- void **set_inertia** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_inertia** ( )

The body's moment of inertia. This is like mass, but for rotation: it determines how much torque it takes to rotate the body. The moment of inertia is usually computed automatically from the mass and the shapes, but this property allows you to set a custom value.

If set to `0`, inertia is automatically computed (default value).

 **Note:** This value does not change when inertia is automatically computed. Use [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D) to get the computed inertia.

.. tabs::

```
```

    @onready var ball = $Ball

    func get_ball_inertia():
        return 1.0 / PhysicsServer2D.body_get_direct_state(ball.get_rid()).inverse_inertia

```
```

    private RigidBody2D _ball;

    public override void _Ready()
    {
        _ball = GetNode<RigidBody2D>("Ball");
    }

    private float GetBallInertia()
    {
        return 1.0f / PhysicsServer2D.BodyGetDirectState(_ball.GetRid()).InverseInertia;
    }

---

<span id="class_RigidBody2D_property_linear_damp"></span>

[float](class_float.md#class_float) **linear_damp** = `0.0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_linear_damp)

- void **set_linear_damp** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_linear_damp** ( )

Damps the body's movement. By default, the body will use the ProjectSettings.physics/2d/default_linear_damp setting or any value override set by an [Area2D](class_area2d.md#class_Area2D) the body is in. Depending on [linear_damp_mode](class_rigidbody2d.md#class_RigidBody2D_property_linear_damp_mode), you can set [linear_damp](class_rigidbody2d.md#class_RigidBody2D_property_linear_damp) to be added to or to replace the body's damping value.

See ProjectSettings.physics/2d/default_linear_damp for more details about damping.

---

<span id="class_RigidBody2D_property_linear_damp_mode"></span>

[DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) **linear_damp_mode** = `0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_linear_damp_mode)

- void **set_linear_damp_mode** ( value: [DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) )
- [DampMode](class_rigidbody2d.md#enum_RigidBody2D_DampMode) **get_linear_damp_mode** ( )

Defines how [linear_damp](class_rigidbody2d.md#class_RigidBody2D_property_linear_damp) is applied.

---

<span id="class_RigidBody2D_property_linear_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **linear_velocity** = `Vector2(0, 0)` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_linear_velocity)

- void **set_linear_velocity** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_linear_velocity** ( )

The body's linear velocity in pixels per second. Can be used sporadically, but **don't set this every frame**, because physics may run in another thread and runs at a different granularity. Use [_integrate_forces()](class_rigidbody2d.md#class_RigidBody2D_private_method__integrate_forces) as your process loop for precise control of the body state.

---

<span id="class_RigidBody2D_property_lock_rotation"></span>

[bool](class_bool.md#class_bool) **lock_rotation** = `false` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_lock_rotation)

- void **set_lock_rotation_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_lock_rotation_enabled** ( )

If `true`, the body cannot rotate. Gravity and forces only apply linear movement.

---

<span id="class_RigidBody2D_property_mass"></span>

[float](class_float.md#class_float) **mass** = `1.0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_mass)

- void **set_mass** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_mass** ( )

The body's mass.

---

<span id="class_RigidBody2D_property_max_contacts_reported"></span>

[int](class_int.md#class_int) **max_contacts_reported** = `0` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_max_contacts_reported)

- void **set_max_contacts_reported** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_contacts_reported** ( )

The maximum number of contacts that will be recorded. Requires a value greater than 0 and [contact_monitor](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor) to be set to `true` to start to register contacts. Use [get_contact_count()](class_rigidbody2d.md#class_RigidBody2D_method_get_contact_count) to retrieve the count or [get_colliding_bodies()](class_rigidbody2d.md#class_RigidBody2D_method_get_colliding_bodies) to retrieve bodies that have been collided with.

 **Note:** The number of contacts is different from the number of collisions. Collisions between parallel edges will result in two contacts (one at each end), and collisions between parallel faces will result in four contacts (one at each corner).

---

<span id="class_RigidBody2D_property_physics_material_override"></span>

[PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) **physics_material_override** [🔗](class_rigidbody2d.md#class_RigidBody2D_property_physics_material_override)

- void **set_physics_material_override** ( value: [PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) )
- [PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) **get_physics_material_override** ( )

The physics material override for the body.

If a material is assigned to this property, it will be used instead of any other physics material, such as an inherited one.

---

<span id="class_RigidBody2D_property_sleeping"></span>

[bool](class_bool.md#class_bool) **sleeping** = `false` [🔗](class_rigidbody2d.md#class_RigidBody2D_property_sleeping)

- void **set_sleeping** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_sleeping** ( )

If `true`, the body will not move and will not calculate forces until woken up by another body through, for example, a collision, or by using the [apply_impulse()](class_rigidbody2d.md#class_RigidBody2D_method_apply_impulse) or [apply_force()](class_rigidbody2d.md#class_RigidBody2D_method_apply_force) methods.

---

### Method Descriptions

<span id="class_RigidBody2D_private_method__integrate_forces"></span>

void **_integrate_forces** ( state: [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D) ) *virtual* [🔗](class_rigidbody2d.md#class_RigidBody2D_private_method__integrate_forces)

Called during physics processing, allowing you to read and safely modify the simulation state for the object. By default, it is called before the standard force integration, but the [custom_integrator](class_rigidbody2d.md#class_RigidBody2D_property_custom_integrator) property allows you to disable the standard force integration and do fully custom force integration for a body.

---

<span id="class_RigidBody2D_method_add_constant_central_force"></span>

void **add_constant_central_force** ( force: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_central_force)

Adds a constant directional force without affecting rotation that keeps being applied over time until cleared with `constant_force = Vector2(0, 0)`.

This is equivalent to using [add_constant_force()](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_force) at the body's center of mass.

---

<span id="class_RigidBody2D_method_add_constant_force"></span>

void **add_constant_force** ( force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_force)

Adds a constant positioned force to the body that keeps being applied over time until cleared with `constant_force = Vector2(0, 0)`.

 `position` is the offset from the body origin in global coordinates.

---

<span id="class_RigidBody2D_method_add_constant_torque"></span>

void **add_constant_torque** ( torque: [float](class_float.md#class_float) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_add_constant_torque)

Adds a constant rotational force without affecting position that keeps being applied over time until cleared with `constant_torque = 0`.

---

<span id="class_RigidBody2D_method_apply_central_force"></span>

void **apply_central_force** ( force: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_apply_central_force)

Applies a directional force without affecting rotation. A force is time dependent and meant to be applied every physics update.

This is equivalent to using [apply_force()](class_rigidbody2d.md#class_RigidBody2D_method_apply_force) at the body's center of mass.

---

<span id="class_RigidBody2D_method_apply_central_impulse"></span>

void **apply_central_impulse** ( impulse: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_apply_central_impulse)

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

This is equivalent to using [apply_impulse()](class_rigidbody2d.md#class_RigidBody2D_method_apply_impulse) at the body's center of mass.

---

<span id="class_RigidBody2D_method_apply_force"></span>

void **apply_force** ( force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_apply_force)

Applies a positioned force to the body. A force is time dependent and meant to be applied every physics update.

 `position` is the offset from the body origin in global coordinates.

---

<span id="class_RigidBody2D_method_apply_impulse"></span>

void **apply_impulse** ( impulse: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_apply_impulse)

Applies a positioned impulse to the body.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

 `position` is the offset from the body origin in global coordinates.

---

<span id="class_RigidBody2D_method_apply_torque"></span>

void **apply_torque** ( torque: [float](class_float.md#class_float) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_apply_torque)

Applies a rotational force without affecting position. A force is time dependent and meant to be applied every physics update.

 **Note:** [inertia](class_rigidbody2d.md#class_RigidBody2D_property_inertia) is required for this to work. To have [inertia](class_rigidbody2d.md#class_RigidBody2D_property_inertia), an active [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) must be a child of the node, or you can manually set [inertia](class_rigidbody2d.md#class_RigidBody2D_property_inertia).

---

<span id="class_RigidBody2D_method_apply_torque_impulse"></span>

void **apply_torque_impulse** ( torque: [float](class_float.md#class_float) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_apply_torque_impulse)

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).

 **Note:** [inertia](class_rigidbody2d.md#class_RigidBody2D_property_inertia) is required for this to work. To have [inertia](class_rigidbody2d.md#class_RigidBody2D_property_inertia), an active [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) must be a child of the node, or you can manually set [inertia](class_rigidbody2d.md#class_RigidBody2D_property_inertia).

---

<span id="class_RigidBody2D_method_get_colliding_bodies"></span>

[Array](class_array.md#class_Array)\[[Node2D](class_node2d.md#class_Node2D)\] **get_colliding_bodies** ( ) *const* [🔗](class_rigidbody2d.md#class_RigidBody2D_method_get_colliding_bodies)

Returns a list of the bodies colliding with this one. Requires [contact_monitor](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor) to be set to `true` and [max_contacts_reported](class_rigidbody2d.md#class_RigidBody2D_property_max_contacts_reported) to be set high enough to detect all the collisions.

 **Note:** The result of this test is not immediate after moving objects. For performance, list of collisions is updated once per frame and before the physics step. Consider using signals instead.

---

<span id="class_RigidBody2D_method_get_contact_count"></span>

[int](class_int.md#class_int) **get_contact_count** ( ) *const* [🔗](class_rigidbody2d.md#class_RigidBody2D_method_get_contact_count)

Returns the number of contacts this body has with other bodies. By default, this returns 0 unless bodies are configured to monitor contacts (see [contact_monitor](class_rigidbody2d.md#class_RigidBody2D_property_contact_monitor)).

 **Note:** To retrieve the colliding bodies, use [get_colliding_bodies()](class_rigidbody2d.md#class_RigidBody2D_method_get_colliding_bodies).

---

<span id="class_RigidBody2D_method_set_axis_velocity"></span>

void **set_axis_velocity** ( axis_velocity: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_rigidbody2d.md#class_RigidBody2D_method_set_axis_velocity)

Sets the body's velocity on the given axis. The velocity in the given vector axis will be set as the given vector length. This is useful for jumping behavior.
