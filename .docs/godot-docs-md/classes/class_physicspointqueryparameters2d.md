<span id="class_PhysicsPointQueryParameters2D"></span>

## PhysicsPointQueryParameters2D

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides parameters for [PhysicsDirectSpaceState2D.intersect_point()](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D_method_intersect_point).

### Description

By changing various properties of this object, such as the point position, you can configure the parameters for [PhysicsDirectSpaceState2D.intersect_point()](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D_method_intersect_point).

### Properties


| [int](class_int.md#class_int) | [canvas_instance_id](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_canvas_instance_id) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [collide_with_areas](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_collide_with_areas) | `false` |
| [bool](class_bool.md#class_bool) | [collide_with_bodies](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_collide_with_bodies) | `true` |
| [int](class_int.md#class_int) | [collision_mask](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_collision_mask) | `4294967295` |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [exclude](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_exclude) | `[]` |
| [Vector2](class_vector2.md#class_Vector2) | [position](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_position) | `Vector2(0, 0)` |

---

### Property Descriptions

<span id="class_PhysicsPointQueryParameters2D_property_canvas_instance_id"></span>

[int](class_int.md#class_int) **canvas_instance_id** = `0` [🔗](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_canvas_instance_id)

- void **set_canvas_instance_id** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_canvas_instance_id** ( )

If different from `0`, restricts the query to a specific canvas layer specified by its instance ID. See [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id).

If `0`, restricts the query to the Viewport's default canvas layer.

---

<span id="class_PhysicsPointQueryParameters2D_property_collide_with_areas"></span>

[bool](class_bool.md#class_bool) **collide_with_areas** = `false` [🔗](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_collide_with_areas)

- void **set_collide_with_areas** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_areas_enabled** ( )

If `true`, the query will take [Area2D](class_area2d.md#class_Area2D) s into account.

---

<span id="class_PhysicsPointQueryParameters2D_property_collide_with_bodies"></span>

[bool](class_bool.md#class_bool) **collide_with_bodies** = `true` [🔗](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_collide_with_bodies)

- void **set_collide_with_bodies** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_bodies_enabled** ( )

If `true`, the query will take [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) s into account.

---

<span id="class_PhysicsPointQueryParameters2D_property_collision_mask"></span>

[int](class_int.md#class_int) **collision_mask** = `4294967295` [🔗](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_PhysicsPointQueryParameters2D_property_exclude"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **exclude** = `[]` [🔗](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_exclude)

- void **set_exclude** ( value: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] )
- [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **get_exclude** ( )

The list of object [RID](class_rid.md#class_RID) s that will be excluded from collisions. Use [CollisionObject2D.get_rid()](class_collisionobject2d.md#class_CollisionObject2D_method_get_rid) to get the [RID](class_rid.md#class_RID) associated with a [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D)-derived node.

 **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.

---

<span id="class_PhysicsPointQueryParameters2D_property_position"></span>

[Vector2](class_vector2.md#class_Vector2) **position** = `Vector2(0, 0)` [🔗](class_physicspointqueryparameters2d.md#class_PhysicsPointQueryParameters2D_property_position)

- void **set_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_position** ( )

The position being queried for, in global coordinates.
