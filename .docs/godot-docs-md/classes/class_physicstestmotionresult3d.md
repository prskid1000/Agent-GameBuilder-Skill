<span id="class_PhysicsTestMotionResult3D"></span>

## PhysicsTestMotionResult3D

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Describes the motion and collision result from [PhysicsServer3D.body_test_motion()](class_physicsserver3d.md#class_PhysicsServer3D_method_body_test_motion).

### Description

Describes the motion and collision result from [PhysicsServer3D.body_test_motion()](class_physicsserver3d.md#class_PhysicsServer3D_method_body_test_motion).

### Methods


| [Object](class_object.md#class_Object) | [get_collider](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_collider_id](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider_id) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [RID](class_rid.md#class_RID) | [get_collider_rid](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider_rid) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_collider_shape](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider_shape) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_collider_velocity](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider_velocity) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_collision_count](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_count) ( ) const |
| [float](class_float.md#class_float) | [get_collision_depth](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_depth) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_collision_local_shape](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_local_shape) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_collision_normal](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_normal) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_collision_point](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_point) ( collision_index: [int](class_int.md#class_int) = 0 ) const |
| [float](class_float.md#class_float) | [get_collision_safe_fraction](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_safe_fraction) ( ) const |
| [float](class_float.md#class_float) | [get_collision_unsafe_fraction](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_unsafe_fraction) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_remainder](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_remainder) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_travel](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_travel) ( ) const |

---

### Method Descriptions

<span id="class_PhysicsTestMotionResult3D_method_get_collider"></span>

[Object](class_object.md#class_Object) **get_collider** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider)

Returns the colliding body's attached [Object](class_object.md#class_Object) given a collision index (the deepest collision by default), if a collision occurred.

---

<span id="class_PhysicsTestMotionResult3D_method_get_collider_id"></span>

[int](class_int.md#class_int) **get_collider_id** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider_id)

Returns the unique instance ID of the colliding body's attached [Object](class_object.md#class_Object) given a collision index (the deepest collision by default), if a collision occurred. See [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id).

---

<span id="class_PhysicsTestMotionResult3D_method_get_collider_rid"></span>

[RID](class_rid.md#class_RID) **get_collider_rid** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider_rid)

Returns the colliding body's [RID](class_rid.md#class_RID) used by the [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) given a collision index (the deepest collision by default), if a collision occurred.

---

<span id="class_PhysicsTestMotionResult3D_method_get_collider_shape"></span>

[int](class_int.md#class_int) **get_collider_shape** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider_shape)

Returns the colliding body's shape index given a collision index (the deepest collision by default), if a collision occurred. See [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D).

---

<span id="class_PhysicsTestMotionResult3D_method_get_collider_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **get_collider_velocity** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collider_velocity)

Returns the colliding body's velocity given a collision index (the deepest collision by default), if a collision occurred.

---

<span id="class_PhysicsTestMotionResult3D_method_get_collision_count"></span>

[int](class_int.md#class_int) **get_collision_count** ( ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_count)

Returns the number of detected collisions.

---

<span id="class_PhysicsTestMotionResult3D_method_get_collision_depth"></span>

[float](class_float.md#class_float) **get_collision_depth** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_depth)

Returns the length of overlap along the collision normal given a collision index (the deepest collision by default), if a collision occurred.

---

<span id="class_PhysicsTestMotionResult3D_method_get_collision_local_shape"></span>

[int](class_int.md#class_int) **get_collision_local_shape** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_local_shape)

Returns the moving object's colliding shape given a collision index (the deepest collision by default), if a collision occurred.

---

<span id="class_PhysicsTestMotionResult3D_method_get_collision_normal"></span>

[Vector3](class_vector3.md#class_Vector3) **get_collision_normal** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_normal)

Returns the colliding body's shape's normal at the point of collision given a collision index (the deepest collision by default), if a collision occurred.

---

<span id="class_PhysicsTestMotionResult3D_method_get_collision_point"></span>

[Vector3](class_vector3.md#class_Vector3) **get_collision_point** ( collision_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_point)

Returns the point of collision in global coordinates given a collision index (the deepest collision by default), if a collision occurred.

---

<span id="class_PhysicsTestMotionResult3D_method_get_collision_safe_fraction"></span>

[float](class_float.md#class_float) **get_collision_safe_fraction** ( ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_safe_fraction)

Returns the maximum fraction of the motion that can occur without a collision, between `0` and `1`.

---

<span id="class_PhysicsTestMotionResult3D_method_get_collision_unsafe_fraction"></span>

[float](class_float.md#class_float) **get_collision_unsafe_fraction** ( ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_collision_unsafe_fraction)

Returns the minimum fraction of the motion needed to collide, if a collision occurred, between `0` and `1`.

---

<span id="class_PhysicsTestMotionResult3D_method_get_remainder"></span>

[Vector3](class_vector3.md#class_Vector3) **get_remainder** ( ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_remainder)

Returns the moving object's remaining movement vector.

---

<span id="class_PhysicsTestMotionResult3D_method_get_travel"></span>

[Vector3](class_vector3.md#class_Vector3) **get_travel** ( ) *const* [🔗](class_physicstestmotionresult3d.md#class_PhysicsTestMotionResult3D_method_get_travel)

Returns the moving object's travel before collision.
