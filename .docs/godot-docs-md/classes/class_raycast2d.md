<span id="class_RayCast2D"></span>

## RayCast2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A ray in 2D space, used to find the first collision object it intersects.

### Description

A raycast represents a ray from its origin to its [target_position](class_raycast2d.md#class_RayCast2D_property_target_position) that finds the closest object along its path, if it intersects any.

 **RayCast2D** can ignore some objects by adding them to an exception list, by making its detection reporting ignore [Area2D](class_area2d.md#class_Area2D) s ([collide_with_areas](class_raycast2d.md#class_RayCast2D_property_collide_with_areas)) or [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) s ([collide_with_bodies](class_raycast2d.md#class_RayCast2D_property_collide_with_bodies)), or by configuring physics layers.

 **RayCast2D** calculates intersection every physics frame, and it holds the result until the next physics frame. For an immediate raycast, or if you want to configure a **RayCast2D** multiple times within the same physics frame, use [force_raycast_update()](class_raycast2d.md#class_RayCast2D_method_force_raycast_update).

To sweep over a region of 2D space, you can approximate the region with multiple **RayCast2D** s or use [ShapeCast2D](class_shapecast2d.md#class_ShapeCast2D).

### Tutorials

- [Ray-casting](../tutorials/physics/ray-casting.md)

### Properties


| [bool](class_bool.md#class_bool) | [collide_with_areas](class_raycast2d.md#class_RayCast2D_property_collide_with_areas) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [collide_with_bodies](class_raycast2d.md#class_RayCast2D_property_collide_with_bodies) | `true` |
| [int](class_int.md#class_int) | [collision_mask](class_raycast2d.md#class_RayCast2D_property_collision_mask) | `1` |
| [bool](class_bool.md#class_bool) | [enabled](class_raycast2d.md#class_RayCast2D_property_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [exclude_parent](class_raycast2d.md#class_RayCast2D_property_exclude_parent) | `true` |
| [bool](class_bool.md#class_bool) | [hit_from_inside](class_raycast2d.md#class_RayCast2D_property_hit_from_inside) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [target_position](class_raycast2d.md#class_RayCast2D_property_target_position) | `Vector2(0, 50)` |

### Methods


| void | [add_exception](class_raycast2d.md#class_RayCast2D_method_add_exception) ( node: [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) ) |
| --- | --- |
| void | [add_exception_rid](class_raycast2d.md#class_RayCast2D_method_add_exception_rid) ( rid: [RID](class_rid.md#class_RID) ) |
| void | [clear_exceptions](class_raycast2d.md#class_RayCast2D_method_clear_exceptions) ( ) |
| void | [force_raycast_update](class_raycast2d.md#class_RayCast2D_method_force_raycast_update) ( ) |
| [Object](class_object.md#class_Object) | [get_collider](class_raycast2d.md#class_RayCast2D_method_get_collider) ( ) const |
| [RID](class_rid.md#class_RID) | [get_collider_rid](class_raycast2d.md#class_RayCast2D_method_get_collider_rid) ( ) const |
| [int](class_int.md#class_int) | [get_collider_shape](class_raycast2d.md#class_RayCast2D_method_get_collider_shape) ( ) const |
| [bool](class_bool.md#class_bool) | [get_collision_mask_value](class_raycast2d.md#class_RayCast2D_method_get_collision_mask_value) ( layer_number: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_collision_normal](class_raycast2d.md#class_RayCast2D_method_get_collision_normal) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_collision_point](class_raycast2d.md#class_RayCast2D_method_get_collision_point) ( ) const |
| [bool](class_bool.md#class_bool) | [is_colliding](class_raycast2d.md#class_RayCast2D_method_is_colliding) ( ) const |
| void | [remove_exception](class_raycast2d.md#class_RayCast2D_method_remove_exception) ( node: [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) ) |
| void | [remove_exception_rid](class_raycast2d.md#class_RayCast2D_method_remove_exception_rid) ( rid: [RID](class_rid.md#class_RID) ) |
| void | [set_collision_mask_value](class_raycast2d.md#class_RayCast2D_method_set_collision_mask_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_RayCast2D_property_collide_with_areas"></span>

[bool](class_bool.md#class_bool) **collide_with_areas** = `false` [🔗](class_raycast2d.md#class_RayCast2D_property_collide_with_areas)

- void **set_collide_with_areas** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_areas_enabled** ( )

If `true`, collisions with [Area2D](class_area2d.md#class_Area2D) s will be reported.

---

<span id="class_RayCast2D_property_collide_with_bodies"></span>

[bool](class_bool.md#class_bool) **collide_with_bodies** = `true` [🔗](class_raycast2d.md#class_RayCast2D_property_collide_with_bodies)

- void **set_collide_with_bodies** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_bodies_enabled** ( )

If `true`, collisions with [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) s will be reported.

---

<span id="class_RayCast2D_property_collision_mask"></span>

[int](class_int.md#class_int) **collision_mask** = `1` [🔗](class_raycast2d.md#class_RayCast2D_property_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The ray's collision mask. Only objects in at least one collision layer enabled in the mask will be detected. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_RayCast2D_property_enabled"></span>

[bool](class_bool.md#class_bool) **enabled** = `true` [🔗](class_raycast2d.md#class_RayCast2D_property_enabled)

- void **set_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_enabled** ( )

If `true`, collisions will be reported.

---

<span id="class_RayCast2D_property_exclude_parent"></span>

[bool](class_bool.md#class_bool) **exclude_parent** = `true` [🔗](class_raycast2d.md#class_RayCast2D_property_exclude_parent)

- void **set_exclude_parent_body** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_exclude_parent_body** ( )

If `true`, this raycast will not report collisions with its parent node. This property only has an effect if the parent node is a [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D). See also [Node.get_parent()](class_node.md#class_Node_method_get_parent) and [add_exception()](class_raycast2d.md#class_RayCast2D_method_add_exception).

---

<span id="class_RayCast2D_property_hit_from_inside"></span>

[bool](class_bool.md#class_bool) **hit_from_inside** = `false` [🔗](class_raycast2d.md#class_RayCast2D_property_hit_from_inside)

- void **set_hit_from_inside** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_hit_from_inside_enabled** ( )

If `true`, the ray will detect a hit when starting inside shapes. In this case the collision normal will be `Vector2(0, 0)`. Does not affect concave polygon shapes.

---

<span id="class_RayCast2D_property_target_position"></span>

[Vector2](class_vector2.md#class_Vector2) **target_position** = `Vector2(0, 50)` [🔗](class_raycast2d.md#class_RayCast2D_property_target_position)

- void **set_target_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_target_position** ( )

The ray's destination point, relative to this raycast's [Node2D.position](class_node2d.md#class_Node2D_property_position).

---

### Method Descriptions

<span id="class_RayCast2D_method_add_exception"></span>

void **add_exception** ( node: [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) ) [🔗](class_raycast2d.md#class_RayCast2D_method_add_exception)

Adds a collision exception so the ray does not report collisions with the specified `node`.

---

<span id="class_RayCast2D_method_add_exception_rid"></span>

void **add_exception_rid** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_raycast2d.md#class_RayCast2D_method_add_exception_rid)

Adds a collision exception so the ray does not report collisions with the specified [RID](class_rid.md#class_RID).

---

<span id="class_RayCast2D_method_clear_exceptions"></span>

void **clear_exceptions** ( ) [🔗](class_raycast2d.md#class_RayCast2D_method_clear_exceptions)

Removes all collision exceptions for this ray.

---

<span id="class_RayCast2D_method_force_raycast_update"></span>

void **force_raycast_update** ( ) [🔗](class_raycast2d.md#class_RayCast2D_method_force_raycast_update)

Updates the collision information for the ray immediately, without waiting for the next `_physics_process` call. Use this method, for example, when the ray or its parent has changed state.

 **Note:** [enabled](class_raycast2d.md#class_RayCast2D_property_enabled) does not need to be `true` for this to work.

---

<span id="class_RayCast2D_method_get_collider"></span>

[Object](class_object.md#class_Object) **get_collider** ( ) *const* [🔗](class_raycast2d.md#class_RayCast2D_method_get_collider)

Returns the first object that the ray intersects, or `null` if no object is intersecting the ray (i.e. [is_colliding()](class_raycast2d.md#class_RayCast2D_method_is_colliding) returns `false`).

 **Note:** This object is not guaranteed to be a [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D). For example, if the ray intersects a [TileMapLayer](class_tilemaplayer.md#class_TileMapLayer), the method will return a [TileMapLayer](class_tilemaplayer.md#class_TileMapLayer) instance.

---

<span id="class_RayCast2D_method_get_collider_rid"></span>

[RID](class_rid.md#class_RID) **get_collider_rid** ( ) *const* [🔗](class_raycast2d.md#class_RayCast2D_method_get_collider_rid)

Returns the [RID](class_rid.md#class_RID) of the first object that the ray intersects, or an empty [RID](class_rid.md#class_RID) if no object is intersecting the ray (i.e. [is_colliding()](class_raycast2d.md#class_RayCast2D_method_is_colliding) returns `false`).

---

<span id="class_RayCast2D_method_get_collider_shape"></span>

[int](class_int.md#class_int) **get_collider_shape** ( ) *const* [🔗](class_raycast2d.md#class_RayCast2D_method_get_collider_shape)

Returns the shape ID of the first object that the ray intersects, or `0` if no object is intersecting the ray (i.e. [is_colliding()](class_raycast2d.md#class_RayCast2D_method_is_colliding) returns `false`).

To get the intersected shape node, for a [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) target, use:

.. tabs::

```
```

    var target = get_collider() # A CollisionObject2D.
    var shape_id = get_collider_shape() # The shape index in the collider.
    var owner_id = target.shape_find_owner(shape_id) # The owner ID in the collider.
    var shape = target.shape_owner_get_owner(owner_id)

```
```

    var target = (CollisionObject2D)GetCollider(); // A CollisionObject2D.
    var shapeId = GetColliderShape(); // The shape index in the collider.
    var ownerId = target.ShapeFindOwner(shapeId); // The owner ID in the collider.
    var shape = target.ShapeOwnerGetOwner(ownerId);

---

<span id="class_RayCast2D_method_get_collision_mask_value"></span>

[bool](class_bool.md#class_bool) **get_collision_mask_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_raycast2d.md#class_RayCast2D_method_get_collision_mask_value)

Returns whether or not the specified layer of the [collision_mask](class_raycast2d.md#class_RayCast2D_property_collision_mask) is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_RayCast2D_method_get_collision_normal"></span>

[Vector2](class_vector2.md#class_Vector2) **get_collision_normal** ( ) *const* [🔗](class_raycast2d.md#class_RayCast2D_method_get_collision_normal)

Returns the normal of the intersecting object's shape at the collision point, or `Vector2(0, 0)` if the ray starts inside the shape and [hit_from_inside](class_raycast2d.md#class_RayCast2D_property_hit_from_inside) is `true`.

 **Note:** Check that [is_colliding()](class_raycast2d.md#class_RayCast2D_method_is_colliding) returns `true` before calling this method to ensure the returned normal is valid and up-to-date.

---

<span id="class_RayCast2D_method_get_collision_point"></span>

[Vector2](class_vector2.md#class_Vector2) **get_collision_point** ( ) *const* [🔗](class_raycast2d.md#class_RayCast2D_method_get_collision_point)

Returns the collision point at which the ray intersects the closest object, in the global coordinate system. If [hit_from_inside](class_raycast2d.md#class_RayCast2D_property_hit_from_inside) is `true` and the ray starts inside of a collision shape, this function will return the origin point of the ray.

 **Note:** Check that [is_colliding()](class_raycast2d.md#class_RayCast2D_method_is_colliding) returns `true` before calling this method to ensure the returned point is valid and up-to-date.

---

<span id="class_RayCast2D_method_is_colliding"></span>

[bool](class_bool.md#class_bool) **is_colliding** ( ) *const* [🔗](class_raycast2d.md#class_RayCast2D_method_is_colliding)

Returns whether any object is intersecting with the ray's vector (considering the vector length).

---

<span id="class_RayCast2D_method_remove_exception"></span>

void **remove_exception** ( node: [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) ) [🔗](class_raycast2d.md#class_RayCast2D_method_remove_exception)

Removes a collision exception so the ray can report collisions with the specified `node`.

---

<span id="class_RayCast2D_method_remove_exception_rid"></span>

void **remove_exception_rid** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_raycast2d.md#class_RayCast2D_method_remove_exception_rid)

Removes a collision exception so the ray can report collisions with the specified [RID](class_rid.md#class_RID).

---

<span id="class_RayCast2D_method_set_collision_mask_value"></span>

void **set_collision_mask_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_raycast2d.md#class_RayCast2D_method_set_collision_mask_value)

Based on `value`, enables or disables the specified layer in the [collision_mask](class_raycast2d.md#class_RayCast2D_property_collision_mask), given a `layer_number` between 1 and 32.
