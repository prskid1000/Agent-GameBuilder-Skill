<span id="class_KinematicCollision3D"></span>

## KinematicCollision3D

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Holds collision data from the movement of a [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D).

### Description

Holds collision data from the movement of a [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D), usually from [PhysicsBody3D.move_and_collide()](class_physicsbody3d.md#class_PhysicsBody3D_method_move_and_collide). When a [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) is moved, it stops if it detects a collision with another body. If a collision is detected, a **KinematicCollision3D** object is returned.

The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.

### Methods


| [float](class_float.md#class_float) | [get_angle](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_angle) ( collision_index: [int](class_int.md#class_int) = 0, up_direction: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 1, 0) ) const |
| --- | --- |
| [Object](class_object.md#class_Object) | [get_collider](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_collider_id](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_id) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [RID](class_rid.md#class_RID) | [get_collider_rid](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_rid) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [Object](class_object.md#class_Object) | [get_collider_shape](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_shape) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_collider_shape_index](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_shape_index) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_collider_velocity](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_velocity) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_collision_count](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collision_count) ( ) const |
| [float](class_float.md#class_float) | [get_depth](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_depth) ( ) const |
| [Object](class_object.md#class_Object) | [get_local_shape](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_local_shape) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_normal](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_normal) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_position](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_position) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_remainder](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_remainder) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_travel](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_travel) ( ) const |

---

### Method Descriptions

<span id="class_KinematicCollision3D_method_get_angle"></span>

[float](class_float.md#class_float) **get_angle** ( collision_index: [int](class_int.md#class_int) = 0, up_direction: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 1, 0) ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_angle)

Returns the collision angle according to `up_direction`, which is [Vector3.UP](class_vector3.md#class_Vector3_constant_UP) by default. This value is always positive.

---

<span id="class_KinematicCollision3D_method_get_collider"></span>

[Object](class_object.md#class_Object) **get_collider** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider)

Returns the colliding body's attached [Object](class_object.md#class_Object) given a collision index (the deepest collision by default).

---

<span id="class_KinematicCollision3D_method_get_collider_id"></span>

[int](class_int.md#class_int) **get_collider_id** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_id)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class_Object) given a collision index (the deepest collision by default). See [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id).

---

<span id="class_KinematicCollision3D_method_get_collider_rid"></span>

[RID](class_rid.md#class_RID) **get_collider_rid** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_rid)

Returns the colliding body's [RID](class_rid.md#class_RID) used by the [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) given a collision index (the deepest collision by default).

---

<span id="class_KinematicCollision3D_method_get_collider_shape"></span>

[Object](class_object.md#class_Object) **get_collider_shape** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_shape)

Returns the colliding body's shape given a collision index (the deepest collision by default).

---

<span id="class_KinematicCollision3D_method_get_collider_shape_index"></span>

[int](class_int.md#class_int) **get_collider_shape_index** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_shape_index)

Returns the colliding body's shape index given a collision index (the deepest collision by default). See [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D).

---

<span id="class_KinematicCollision3D_method_get_collider_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **get_collider_velocity** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collider_velocity)

Returns the colliding body's velocity given a collision index (the deepest collision by default).

---

<span id="class_KinematicCollision3D_method_get_collision_count"></span>

[int](class_int.md#class_int) **get_collision_count** ( ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_collision_count)

Returns the number of detected collisions.

---

<span id="class_KinematicCollision3D_method_get_depth"></span>

[float](class_float.md#class_float) **get_depth** ( ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_depth)

Returns the colliding body's length of overlap along the collision normal.

---

<span id="class_KinematicCollision3D_method_get_local_shape"></span>

[Object](class_object.md#class_Object) **get_local_shape** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_local_shape)

Returns the moving object's colliding shape given a collision index (the deepest collision by default).

---

<span id="class_KinematicCollision3D_method_get_normal"></span>

[Vector3](class_vector3.md#class_Vector3) **get_normal** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_normal)

Returns the colliding body's shape's normal at the point of collision given a collision index (the deepest collision by default).

---

<span id="class_KinematicCollision3D_method_get_position"></span>

[Vector3](class_vector3.md#class_Vector3) **get_position** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_position)

Returns the point of collision in global coordinates given a collision index (the deepest collision by default).

---

<span id="class_KinematicCollision3D_method_get_remainder"></span>

[Vector3](class_vector3.md#class_Vector3) **get_remainder** ( ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_remainder)

Returns the moving object's remaining movement vector.

---

<span id="class_KinematicCollision3D_method_get_travel"></span>

[Vector3](class_vector3.md#class_Vector3) **get_travel** ( ) *const* [🔗](class_kinematiccollision3d.md#class_KinematicCollision3D_method_get_travel)

Returns the moving object's travel before collision.
