<span id="class_KinematicCollision2D"></span>

## KinematicCollision2D

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Holds collision data from the movement of a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D).

### Description

Holds collision data from the movement of a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D), usually from [PhysicsBody2D.move_and_collide()](class_physicsbody2d.md#class_PhysicsBody2D_method_move_and_collide). When a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) is moved, it stops if it detects a collision with another body. If a collision is detected, a **KinematicCollision2D** object is returned.

The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.

### Methods


| [float](class_float.md#class_float) | [get_angle](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_angle) ( up_direction: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, -1) ) const |
| --- | --- |
| [Object](class_object.md#class_Object) | [get_collider](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider) ( ) const |
| [int](class_int.md#class_int) | [get_collider_id](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_id) ( ) const |
| [RID](class_rid.md#class_RID) | [get_collider_rid](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_rid) ( ) const |
| [Object](class_object.md#class_Object) | [get_collider_shape](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_shape) ( ) const |
| [int](class_int.md#class_int) | [get_collider_shape_index](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_shape_index) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_collider_velocity](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_velocity) ( ) const |
| [float](class_float.md#class_float) | [get_depth](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_depth) ( ) const |
| [Object](class_object.md#class_Object) | [get_local_shape](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_local_shape) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_normal](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_normal) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_position](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_position) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_remainder](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_remainder) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_travel](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_travel) ( ) const |

---

### Method Descriptions

<span id="class_KinematicCollision2D_method_get_angle"></span>

[float](class_float.md#class_float) **get_angle** ( up_direction: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, -1) ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_angle)

Returns the collision angle according to `up_direction`, which is [Vector2.UP](class_vector2.md#class_Vector2_constant_UP) by default. This value is always positive.

---

<span id="class_KinematicCollision2D_method_get_collider"></span>

[Object](class_object.md#class_Object) **get_collider** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider)

Returns the colliding body's attached [Object](class_object.md#class_Object).

---

<span id="class_KinematicCollision2D_method_get_collider_id"></span>

[int](class_int.md#class_int) **get_collider_id** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_id)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class_Object). See [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id).

---

<span id="class_KinematicCollision2D_method_get_collider_rid"></span>

[RID](class_rid.md#class_RID) **get_collider_rid** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_rid)

Returns the colliding body's [RID](class_rid.md#class_RID) used by the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D).

---

<span id="class_KinematicCollision2D_method_get_collider_shape"></span>

[Object](class_object.md#class_Object) **get_collider_shape** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_shape)

Returns the colliding body's shape.

---

<span id="class_KinematicCollision2D_method_get_collider_shape_index"></span>

[int](class_int.md#class_int) **get_collider_shape_index** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_shape_index)

Returns the colliding body's shape index. See [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D).

---

<span id="class_KinematicCollision2D_method_get_collider_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **get_collider_velocity** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_velocity)

Returns the colliding body's velocity.

---

<span id="class_KinematicCollision2D_method_get_depth"></span>

[float](class_float.md#class_float) **get_depth** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_depth)

Returns the colliding body's length of overlap along the collision normal.

---

<span id="class_KinematicCollision2D_method_get_local_shape"></span>

[Object](class_object.md#class_Object) **get_local_shape** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_local_shape)

Returns the moving object's colliding shape.

---

<span id="class_KinematicCollision2D_method_get_normal"></span>

[Vector2](class_vector2.md#class_Vector2) **get_normal** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_normal)

Returns the colliding body's shape's normal at the point of collision.

---

<span id="class_KinematicCollision2D_method_get_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_position** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_position)

Returns the point of collision in global coordinates.

---

<span id="class_KinematicCollision2D_method_get_remainder"></span>

[Vector2](class_vector2.md#class_Vector2) **get_remainder** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_remainder)

Returns the moving object's remaining movement vector.

---

<span id="class_KinematicCollision2D_method_get_travel"></span>

[Vector2](class_vector2.md#class_Vector2) **get_travel** ( ) *const* [🔗](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_travel)

Returns the moving object's travel before collision.
