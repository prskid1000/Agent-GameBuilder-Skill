<span id="class_PhysicsBody3D"></span>

## PhysicsBody3D

**Inherits:** [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CharacterBody3D](class_characterbody3d.md#class_CharacterBody3D), [PhysicalBone3D](class_physicalbone3d.md#class_PhysicalBone3D), [RigidBody3D](class_rigidbody3d.md#class_RigidBody3D), [StaticBody3D](class_staticbody3d.md#class_StaticBody3D)

Abstract base class for 3D game objects affected by physics.

### Description

**PhysicsBody3D** is an abstract base class for 3D game objects affected by physics. All 3D physics bodies inherit from it.

 **Warning:** With a non-uniform scale, this node will likely not behave as expected. It is advised to keep its scale the same on all axes and adjust its collision shape(s) instead.

### Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)

### Properties


| [bool](class_bool.md#class_bool) | [axis_lock_angular_x](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_angular_x) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [axis_lock_angular_y](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_angular_y) | `false` |
| [bool](class_bool.md#class_bool) | [axis_lock_angular_z](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_angular_z) | `false` |
| [bool](class_bool.md#class_bool) | [axis_lock_linear_x](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_linear_x) | `false` |
| [bool](class_bool.md#class_bool) | [axis_lock_linear_y](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_linear_y) | `false` |
| [bool](class_bool.md#class_bool) | [axis_lock_linear_z](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_linear_z) | `false` |

### Methods


| void | [add_collision_exception_with](class_physicsbody3d.md#class_PhysicsBody3D_method_add_collision_exception_with) ( body: [Node](class_node.md#class_Node) ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [get_axis_lock](class_physicsbody3d.md#class_PhysicsBody3D_method_get_axis_lock) ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) const |
| [Array](class_array.md#class_Array)\[[PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D)\] | [get_collision_exceptions](class_physicsbody3d.md#class_PhysicsBody3D_method_get_collision_exceptions) ( ) |
| [Vector3](class_vector3.md#class_Vector3) | [get_gravity](class_physicsbody3d.md#class_PhysicsBody3D_method_get_gravity) ( ) const |
| [KinematicCollision3D](class_kinematiccollision3d.md#class_KinematicCollision3D) | [move_and_collide](class_physicsbody3d.md#class_PhysicsBody3D_method_move_and_collide) ( motion: [Vector3](class_vector3.md#class_Vector3), test_only: [bool](class_bool.md#class_bool) = false, safe_margin: [float](class_float.md#class_float) = 0.001, recovery_as_collision: [bool](class_bool.md#class_bool) = false, max_collisions: [int](class_int.md#class_int) = 1 ) |
| void | [remove_collision_exception_with](class_physicsbody3d.md#class_PhysicsBody3D_method_remove_collision_exception_with) ( body: [Node](class_node.md#class_Node) ) |
| void | [set_axis_lock](class_physicsbody3d.md#class_PhysicsBody3D_method_set_axis_lock) ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) ) |
| [bool](class_bool.md#class_bool) | [test_move](class_physicsbody3d.md#class_PhysicsBody3D_method_test_move) ( from: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), collision: [KinematicCollision3D](class_kinematiccollision3d.md#class_KinematicCollision3D) = null, safe_margin: [float](class_float.md#class_float) = 0.001, recovery_as_collision: [bool](class_bool.md#class_bool) = false, max_collisions: [int](class_int.md#class_int) = 1 ) |

---

### Property Descriptions

<span id="class_PhysicsBody3D_property_axis_lock_angular_x"></span>

[bool](class_bool.md#class_bool) **axis_lock_angular_x** = `false` [🔗](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_angular_x)

- void **set_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) *const*

Lock the body's rotation in the X axis.

---

<span id="class_PhysicsBody3D_property_axis_lock_angular_y"></span>

[bool](class_bool.md#class_bool) **axis_lock_angular_y** = `false` [🔗](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_angular_y)

- void **set_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) *const*

Lock the body's rotation in the Y axis.

---

<span id="class_PhysicsBody3D_property_axis_lock_angular_z"></span>

[bool](class_bool.md#class_bool) **axis_lock_angular_z** = `false` [🔗](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_angular_z)

- void **set_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) *const*

Lock the body's rotation in the Z axis.

---

<span id="class_PhysicsBody3D_property_axis_lock_linear_x"></span>

[bool](class_bool.md#class_bool) **axis_lock_linear_x** = `false` [🔗](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_linear_x)

- void **set_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) *const*

Lock the body's linear movement in the X axis.

---

<span id="class_PhysicsBody3D_property_axis_lock_linear_y"></span>

[bool](class_bool.md#class_bool) **axis_lock_linear_y** = `false` [🔗](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_linear_y)

- void **set_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) *const*

Lock the body's linear movement in the Y axis.

---

<span id="class_PhysicsBody3D_property_axis_lock_linear_z"></span>

[bool](class_bool.md#class_bool) **axis_lock_linear_z** = `false` [🔗](class_physicsbody3d.md#class_PhysicsBody3D_property_axis_lock_linear_z)

- void **set_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) *const*

Lock the body's linear movement in the Z axis.

---

### Method Descriptions

<span id="class_PhysicsBody3D_method_add_collision_exception_with"></span>

void **add_collision_exception_with** ( body: [Node](class_node.md#class_Node) ) [🔗](class_physicsbody3d.md#class_PhysicsBody3D_method_add_collision_exception_with)

Adds a body to the list of bodies that this body can't collide with.

---

<span id="class_PhysicsBody3D_method_get_axis_lock"></span>

[bool](class_bool.md#class_bool) **get_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) *const* [🔗](class_physicsbody3d.md#class_PhysicsBody3D_method_get_axis_lock)

Returns `true` if the specified linear or rotational `axis` is locked.

---

<span id="class_PhysicsBody3D_method_get_collision_exceptions"></span>

[Array](class_array.md#class_Array)\[[PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D)\] **get_collision_exceptions** ( ) [🔗](class_physicsbody3d.md#class_PhysicsBody3D_method_get_collision_exceptions)

Returns an array of nodes that were added as collision exceptions for this body.

---

<span id="class_PhysicsBody3D_method_get_gravity"></span>

[Vector3](class_vector3.md#class_Vector3) **get_gravity** ( ) *const* [🔗](class_physicsbody3d.md#class_PhysicsBody3D_method_get_gravity)

Returns the gravity vector computed from all sources that can affect the body, including all gravity overrides from [Area3D](class_area3d.md#class_Area3D) nodes and the global world gravity.

---

<span id="class_PhysicsBody3D_method_move_and_collide"></span>

[KinematicCollision3D](class_kinematiccollision3d.md#class_KinematicCollision3D) **move_and_collide** ( motion: [Vector3](class_vector3.md#class_Vector3), test_only: [bool](class_bool.md#class_bool) = false, safe_margin: [float](class_float.md#class_float) = 0.001, recovery_as_collision: [bool](class_bool.md#class_bool) = false, max_collisions: [int](class_int.md#class_int) = 1 ) [🔗](class_physicsbody3d.md#class_PhysicsBody3D_method_move_and_collide)

Moves the body along the vector `motion`. In order to be frame rate independent in [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) or [Node._process()](class_node.md#class_Node_private_method__process), `motion` should be computed using `delta`.

The body will stop if it collides. Returns a [KinematicCollision3D](class_kinematiccollision3d.md#class_KinematicCollision3D), which contains information about the collision when stopped, or when touching another body along the motion.

If `test_only` is `true`, the body does not move but the would-be collision information is given.

 `safe_margin` is the extra margin used for collision recovery (see [CharacterBody3D.safe_margin](class_characterbody3d.md#class_CharacterBody3D_property_safe_margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is used e.g. by [CharacterBody3D](class_characterbody3d.md#class_CharacterBody3D) for improving floor detection during floor snapping.

 `max_collisions` allows to retrieve more than one collision result.

---

<span id="class_PhysicsBody3D_method_remove_collision_exception_with"></span>

void **remove_collision_exception_with** ( body: [Node](class_node.md#class_Node) ) [🔗](class_physicsbody3d.md#class_PhysicsBody3D_method_remove_collision_exception_with)

Removes a body from the list of bodies that this body can't collide with.

---

<span id="class_PhysicsBody3D_method_set_axis_lock"></span>

void **set_axis_lock** ( axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) ) [🔗](class_physicsbody3d.md#class_PhysicsBody3D_method_set_axis_lock)

Locks or unlocks the specified linear or rotational `axis` depending on the value of `lock`.

---

<span id="class_PhysicsBody3D_method_test_move"></span>

[bool](class_bool.md#class_bool) **test_move** ( from: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), collision: [KinematicCollision3D](class_kinematiccollision3d.md#class_KinematicCollision3D) = null, safe_margin: [float](class_float.md#class_float) = 0.001, recovery_as_collision: [bool](class_bool.md#class_bool) = false, max_collisions: [int](class_int.md#class_int) = 1 ) [🔗](class_physicsbody3d.md#class_PhysicsBody3D_method_test_move)

Checks for collisions without moving the body. In order to be frame rate independent in [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) or [Node._process()](class_node.md#class_Node_private_method__process), `motion` should be computed using `delta`.

Virtually sets the node's position, scale and rotation to that of the given [Transform3D](class_transform3d.md#class_Transform3D), then tries to move the body along the vector `motion`. Returns `true` if a collision would stop the body from moving along the whole path.

 `collision` is an optional object of type [KinematicCollision3D](class_kinematiccollision3d.md#class_KinematicCollision3D), which contains additional information about the collision when stopped, or when touching another body along the motion.

 `safe_margin` is the extra margin used for collision recovery (see [CharacterBody3D.safe_margin](class_characterbody3d.md#class_CharacterBody3D_property_safe_margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is useful for checking whether the body would *touch* any other bodies.

 `max_collisions` allows to retrieve more than one collision result.
