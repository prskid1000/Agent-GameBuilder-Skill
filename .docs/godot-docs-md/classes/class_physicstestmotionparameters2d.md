<span id="class_PhysicsTestMotionParameters2D"></span>

## PhysicsTestMotionParameters2D

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides parameters for [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_test_motion).

### Description

By changing various properties of this object, such as the motion, you can configure the parameters for [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_test_motion).

### Properties


| [bool](class_bool.md#class_bool) | [collide_separation_ray](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_collide_separation_ray) | `false` |
| --- | --- | --- |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [exclude_bodies](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_exclude_bodies) | `[]` |
| [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] | [exclude_objects](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_exclude_objects) | `[]` |
| [Transform2D](class_transform2d.md#class_Transform2D) | [from](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_from) | `Transform2D(1, 0, 0, 1, 0, 0)` |
| [float](class_float.md#class_float) | [margin](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_margin) | `0.08` |
| [Vector2](class_vector2.md#class_Vector2) | [motion](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_motion) | `Vector2(0, 0)` |
| [bool](class_bool.md#class_bool) | [recovery_as_collision](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_recovery_as_collision) | `false` |

---

### Property Descriptions

<span id="class_PhysicsTestMotionParameters2D_property_collide_separation_ray"></span>

[bool](class_bool.md#class_bool) **collide_separation_ray** = `false` [🔗](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_collide_separation_ray)

- void **set_collide_separation_ray_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_separation_ray_enabled** ( )

If set to `true`, shapes of type [PhysicsServer2D.SHAPE_SEPARATION_RAY](class_physicsserver2d.md#class_PhysicsServer2D_constant_SHAPE_SEPARATION_RAY) are used to detect collisions and can stop the motion. Can be useful when snapping to the ground.

If set to `false`, shapes of type [PhysicsServer2D.SHAPE_SEPARATION_RAY](class_physicsserver2d.md#class_PhysicsServer2D_constant_SHAPE_SEPARATION_RAY) are only used for separation when overlapping with other bodies. That's the main use for separation ray shapes.

---

<span id="class_PhysicsTestMotionParameters2D_property_exclude_bodies"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **exclude_bodies** = `[]` [🔗](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_exclude_bodies)

- void **set_exclude_bodies** ( value: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] )
- [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **get_exclude_bodies** ( )

Optional array of body [RID](class_rid.md#class_RID) to exclude from collision. Use [CollisionObject2D.get_rid()](class_collisionobject2d.md#class_CollisionObject2D_method_get_rid) to get the [RID](class_rid.md#class_RID) associated with a [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D)-derived node.

---

<span id="class_PhysicsTestMotionParameters2D_property_exclude_objects"></span>

[Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] **exclude_objects** = `[]` [🔗](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_exclude_objects)

- void **set_exclude_objects** ( value: [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] )
- [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] **get_exclude_objects** ( )

Optional array of object unique instance ID to exclude from collision. See [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id).

---

<span id="class_PhysicsTestMotionParameters2D_property_from"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **from** = `Transform2D(1, 0, 0, 1, 0, 0)` [🔗](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_from)

- void **set_from** ( value: [Transform2D](class_transform2d.md#class_Transform2D) )
- [Transform2D](class_transform2d.md#class_Transform2D) **get_from** ( )

Transform in global space where the motion should start. Usually set to [Node2D.global_transform](class_node2d.md#class_Node2D_property_global_transform) for the current body's transform.

---

<span id="class_PhysicsTestMotionParameters2D_property_margin"></span>

[float](class_float.md#class_float) **margin** = `0.08` [🔗](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_margin)

- void **set_margin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_margin** ( )

Increases the size of the shapes involved in the collision detection.

---

<span id="class_PhysicsTestMotionParameters2D_property_motion"></span>

[Vector2](class_vector2.md#class_Vector2) **motion** = `Vector2(0, 0)` [🔗](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_motion)

- void **set_motion** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_motion** ( )

Motion vector to define the length and direction of the motion to test.

---

<span id="class_PhysicsTestMotionParameters2D_property_recovery_as_collision"></span>

[bool](class_bool.md#class_bool) **recovery_as_collision** = `false` [🔗](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D_property_recovery_as_collision)

- void **set_recovery_as_collision_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_recovery_as_collision_enabled** ( )

If set to `true`, any depenetration from the recovery phase is reported as a collision; this is used e.g. by [CharacterBody2D](class_characterbody2d.md#class_CharacterBody2D) for improving floor detection during floor snapping.

If set to `false`, only collisions resulting from the motion are reported, which is generally the desired behavior.
