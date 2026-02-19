<span id="class_PhysicsTestMotionResult2D"></span>

## PhysicsTestMotionResult2D

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Describes the motion and collision result from [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_test_motion).

### Description

Describes the motion and collision result from [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_test_motion).

### Methods


| [Object](class_object.md#class_Object) | [get_collider](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider) ( ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_collider_id](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider_id) ( ) const |
| [RID](class_rid.md#class_RID) | [get_collider_rid](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider_rid) ( ) const |
| [int](class_int.md#class_int) | [get_collider_shape](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider_shape) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_collider_velocity](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider_velocity) ( ) const |
| [float](class_float.md#class_float) | [get_collision_depth](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_depth) ( ) const |
| [int](class_int.md#class_int) | [get_collision_local_shape](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_local_shape) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_collision_normal](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_normal) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_collision_point](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_point) ( ) const |
| [float](class_float.md#class_float) | [get_collision_safe_fraction](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_safe_fraction) ( ) const |
| [float](class_float.md#class_float) | [get_collision_unsafe_fraction](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_unsafe_fraction) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_remainder](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_remainder) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_travel](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_travel) ( ) const |

---

### Method Descriptions

<span id="class_PhysicsTestMotionResult2D_method_get_collider"></span>

[Object](class_object.md#class_Object) **get_collider** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider)

Returns the colliding body's attached [Object](class_object.md#class_Object), if a collision occurred.

---

<span id="class_PhysicsTestMotionResult2D_method_get_collider_id"></span>

[int](class_int.md#class_int) **get_collider_id** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider_id)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class_Object), if a collision occurred. See [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id).

---

<span id="class_PhysicsTestMotionResult2D_method_get_collider_rid"></span>

[RID](class_rid.md#class_RID) **get_collider_rid** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider_rid)

Returns the colliding body's [RID](class_rid.md#class_RID) used by the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D), if a collision occurred.

---

<span id="class_PhysicsTestMotionResult2D_method_get_collider_shape"></span>

[int](class_int.md#class_int) **get_collider_shape** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider_shape)

Returns the colliding body's shape index, if a collision occurred. See [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D).

---

<span id="class_PhysicsTestMotionResult2D_method_get_collider_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **get_collider_velocity** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collider_velocity)

Returns the colliding body's velocity, if a collision occurred.

---

<span id="class_PhysicsTestMotionResult2D_method_get_collision_depth"></span>

[float](class_float.md#class_float) **get_collision_depth** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_depth)

Returns the length of overlap along the collision normal, if a collision occurred.

---

<span id="class_PhysicsTestMotionResult2D_method_get_collision_local_shape"></span>

[int](class_int.md#class_int) **get_collision_local_shape** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_local_shape)

Returns the moving object's colliding shape, if a collision occurred.

---

<span id="class_PhysicsTestMotionResult2D_method_get_collision_normal"></span>

[Vector2](class_vector2.md#class_Vector2) **get_collision_normal** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_normal)

Returns the colliding body's shape's normal at the point of collision, if a collision occurred.

---

<span id="class_PhysicsTestMotionResult2D_method_get_collision_point"></span>

[Vector2](class_vector2.md#class_Vector2) **get_collision_point** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_point)

Returns the point of collision in global coordinates, if a collision occurred.

---

<span id="class_PhysicsTestMotionResult2D_method_get_collision_safe_fraction"></span>

[float](class_float.md#class_float) **get_collision_safe_fraction** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_safe_fraction)

Returns the maximum fraction of the motion that can occur without a collision, between `0` and `1`.

---

<span id="class_PhysicsTestMotionResult2D_method_get_collision_unsafe_fraction"></span>

[float](class_float.md#class_float) **get_collision_unsafe_fraction** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_collision_unsafe_fraction)

Returns the minimum fraction of the motion needed to collide, if a collision occurred, between `0` and `1`.

---

<span id="class_PhysicsTestMotionResult2D_method_get_remainder"></span>

[Vector2](class_vector2.md#class_Vector2) **get_remainder** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_remainder)

Returns the moving object's remaining movement vector.

---

<span id="class_PhysicsTestMotionResult2D_method_get_travel"></span>

[Vector2](class_vector2.md#class_Vector2) **get_travel** ( ) *const* [🔗](class_physicstestmotionresult2d.md#class_PhysicsTestMotionResult2D_method_get_travel)

Returns the moving object's travel before collision.
