<span id="class_PhysicsBody2D"></span>

## PhysicsBody2D

**Inherits:** [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CharacterBody2D](class_characterbody2d.md#class_CharacterBody2D), [RigidBody2D](class_rigidbody2d.md#class_RigidBody2D), [StaticBody2D](class_staticbody2d.md#class_StaticBody2D)

Abstract base class for 2D game objects affected by physics.

### Description

**PhysicsBody2D** is an abstract base class for 2D game objects affected by physics. All 2D physics bodies inherit from it.

### Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)

### Properties


| [bool](class_bool.md#class_bool) | input_pickable | `false` (overrides [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D_property_input_pickable)) |
| --- | --- | --- |

### Methods


| void | [add_collision_exception_with](class_physicsbody2d.md#class_PhysicsBody2D_method_add_collision_exception_with) ( body: [Node](class_node.md#class_Node) ) |
| --- | --- |
| [Array](class_array.md#class_Array)\[[PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D)\] | [get_collision_exceptions](class_physicsbody2d.md#class_PhysicsBody2D_method_get_collision_exceptions) ( ) |
| [Vector2](class_vector2.md#class_Vector2) | [get_gravity](class_physicsbody2d.md#class_PhysicsBody2D_method_get_gravity) ( ) const |
| [KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D) | [move_and_collide](class_physicsbody2d.md#class_PhysicsBody2D_method_move_and_collide) ( motion: [Vector2](class_vector2.md#class_Vector2), test_only: [bool](class_bool.md#class_bool) = false, safe_margin: [float](class_float.md#class_float) = 0.08, recovery_as_collision: [bool](class_bool.md#class_bool) = false ) |
| void | [remove_collision_exception_with](class_physicsbody2d.md#class_PhysicsBody2D_method_remove_collision_exception_with) ( body: [Node](class_node.md#class_Node) ) |
| [bool](class_bool.md#class_bool) | [test_move](class_physicsbody2d.md#class_PhysicsBody2D_method_test_move) ( from: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), collision: [KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D) = null, safe_margin: [float](class_float.md#class_float) = 0.08, recovery_as_collision: [bool](class_bool.md#class_bool) = false ) |

---

### Method Descriptions

<span id="class_PhysicsBody2D_method_add_collision_exception_with"></span>

void **add_collision_exception_with** ( body: [Node](class_node.md#class_Node) ) [🔗](class_physicsbody2d.md#class_PhysicsBody2D_method_add_collision_exception_with)

Adds a body to the list of bodies that this body can't collide with.

---

<span id="class_PhysicsBody2D_method_get_collision_exceptions"></span>

[Array](class_array.md#class_Array)\[[PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D)\] **get_collision_exceptions** ( ) [🔗](class_physicsbody2d.md#class_PhysicsBody2D_method_get_collision_exceptions)

Returns an array of nodes that were added as collision exceptions for this body.

---

<span id="class_PhysicsBody2D_method_get_gravity"></span>

[Vector2](class_vector2.md#class_Vector2) **get_gravity** ( ) *const* [🔗](class_physicsbody2d.md#class_PhysicsBody2D_method_get_gravity)

Returns the gravity vector computed from all sources that can affect the body, including all gravity overrides from [Area2D](class_area2d.md#class_Area2D) nodes and the global world gravity.

---

<span id="class_PhysicsBody2D_method_move_and_collide"></span>

[KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D) **move_and_collide** ( motion: [Vector2](class_vector2.md#class_Vector2), test_only: [bool](class_bool.md#class_bool) = false, safe_margin: [float](class_float.md#class_float) = 0.08, recovery_as_collision: [bool](class_bool.md#class_bool) = false ) [🔗](class_physicsbody2d.md#class_PhysicsBody2D_method_move_and_collide)

Moves the body along the vector `motion`. In order to be frame rate independent in [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) or [Node._process()](class_node.md#class_Node_private_method__process), `motion` should be computed using `delta`.

Returns a [KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D), which contains information about the collision when stopped, or when touching another body along the motion.

If `test_only` is `true`, the body does not move but the would-be collision information is given.

 `safe_margin` is the extra margin used for collision recovery (see [CharacterBody2D.safe_margin](class_characterbody2d.md#class_CharacterBody2D_property_safe_margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is used e.g. by [CharacterBody2D](class_characterbody2d.md#class_CharacterBody2D) for improving floor detection during floor snapping.

---

<span id="class_PhysicsBody2D_method_remove_collision_exception_with"></span>

void **remove_collision_exception_with** ( body: [Node](class_node.md#class_Node) ) [🔗](class_physicsbody2d.md#class_PhysicsBody2D_method_remove_collision_exception_with)

Removes a body from the list of bodies that this body can't collide with.

---

<span id="class_PhysicsBody2D_method_test_move"></span>

[bool](class_bool.md#class_bool) **test_move** ( from: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), collision: [KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D) = null, safe_margin: [float](class_float.md#class_float) = 0.08, recovery_as_collision: [bool](class_bool.md#class_bool) = false ) [🔗](class_physicsbody2d.md#class_PhysicsBody2D_method_test_move)

Checks for collisions without moving the body. In order to be frame rate independent in [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) or [Node._process()](class_node.md#class_Node_private_method__process), `motion` should be computed using `delta`.

Virtually sets the node's position, scale and rotation to that of the given [Transform2D](class_transform2d.md#class_Transform2D), then tries to move the body along the vector `motion`. Returns `true` if a collision would stop the body from moving along the whole path.

 `collision` is an optional object of type [KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D), which contains additional information about the collision when stopped, or when touching another body along the motion.

 `safe_margin` is the extra margin used for collision recovery (see [CharacterBody2D.safe_margin](class_characterbody2d.md#class_CharacterBody2D_property_safe_margin) for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is useful for checking whether the body would *touch* any other bodies.
