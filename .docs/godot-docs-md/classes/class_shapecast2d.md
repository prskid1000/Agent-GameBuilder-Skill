<span id="class_ShapeCast2D"></span>

## ShapeCast2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A 2D shape that sweeps a region of space to detect [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) s.

### Description

Shape casting allows to detect collision objects by sweeping its [shape](class_shapecast2d.md#class_ShapeCast2D_property_shape) along the cast direction determined by [target_position](class_shapecast2d.md#class_ShapeCast2D_property_target_position). This is similar to [RayCast2D](class_raycast2d.md#class_RayCast2D), but it allows for sweeping a region of space, rather than just a straight line. **ShapeCast2D** can detect multiple collision objects. It is useful for things like wide laser beams or snapping a simple shape to a floor.

Immediate collision overlaps can be done with the [target_position](class_shapecast2d.md#class_ShapeCast2D_property_target_position) set to `Vector2(0, 0)` and by calling [force_shapecast_update()](class_shapecast2d.md#class_ShapeCast2D_method_force_shapecast_update) within the same physics frame. This helps to overcome some limitations of [Area2D](class_area2d.md#class_Area2D) when used as an instantaneous detection area, as collision information isn't immediately available to it.

 **Note:** Shape casting is more computationally expensive than ray casting.

### Properties


| [bool](class_bool.md#class_bool) | [collide_with_areas](class_shapecast2d.md#class_ShapeCast2D_property_collide_with_areas) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [collide_with_bodies](class_shapecast2d.md#class_ShapeCast2D_property_collide_with_bodies) | `true` |
| [int](class_int.md#class_int) | [collision_mask](class_shapecast2d.md#class_ShapeCast2D_property_collision_mask) | `1` |
| [Array](class_array.md#class_Array) | [collision_result](class_shapecast2d.md#class_ShapeCast2D_property_collision_result) | `[]` |
| [bool](class_bool.md#class_bool) | [enabled](class_shapecast2d.md#class_ShapeCast2D_property_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [exclude_parent](class_shapecast2d.md#class_ShapeCast2D_property_exclude_parent) | `true` |
| [float](class_float.md#class_float) | [margin](class_shapecast2d.md#class_ShapeCast2D_property_margin) | `0.0` |
| [int](class_int.md#class_int) | [max_results](class_shapecast2d.md#class_ShapeCast2D_property_max_results) | `32` |
| [Shape2D](class_shape2d.md#class_Shape2D) | [shape](class_shapecast2d.md#class_ShapeCast2D_property_shape) |
| [Vector2](class_vector2.md#class_Vector2) | [target_position](class_shapecast2d.md#class_ShapeCast2D_property_target_position) | `Vector2(0, 50)` |

### Methods


| void | [add_exception](class_shapecast2d.md#class_ShapeCast2D_method_add_exception) ( node: [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) ) |
| --- | --- |
| void | [add_exception_rid](class_shapecast2d.md#class_ShapeCast2D_method_add_exception_rid) ( rid: [RID](class_rid.md#class_RID) ) |
| void | [clear_exceptions](class_shapecast2d.md#class_ShapeCast2D_method_clear_exceptions) ( ) |
| void | [force_shapecast_update](class_shapecast2d.md#class_ShapeCast2D_method_force_shapecast_update) ( ) |
| [float](class_float.md#class_float) | [get_closest_collision_safe_fraction](class_shapecast2d.md#class_ShapeCast2D_method_get_closest_collision_safe_fraction) ( ) const |
| [float](class_float.md#class_float) | [get_closest_collision_unsafe_fraction](class_shapecast2d.md#class_ShapeCast2D_method_get_closest_collision_unsafe_fraction) ( ) const |
| [Object](class_object.md#class_Object) | [get_collider](class_shapecast2d.md#class_ShapeCast2D_method_get_collider) ( index: [int](class_int.md#class_int) ) const |
| [RID](class_rid.md#class_RID) | [get_collider_rid](class_shapecast2d.md#class_ShapeCast2D_method_get_collider_rid) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_collider_shape](class_shapecast2d.md#class_ShapeCast2D_method_get_collider_shape) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_collision_count](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_count) ( ) const |
| [bool](class_bool.md#class_bool) | [get_collision_mask_value](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_mask_value) ( layer_number: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_collision_normal](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_normal) ( index: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_collision_point](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_point) ( index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_colliding](class_shapecast2d.md#class_ShapeCast2D_method_is_colliding) ( ) const |
| void | [remove_exception](class_shapecast2d.md#class_ShapeCast2D_method_remove_exception) ( node: [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) ) |
| void | [remove_exception_rid](class_shapecast2d.md#class_ShapeCast2D_method_remove_exception_rid) ( rid: [RID](class_rid.md#class_RID) ) |
| void | [set_collision_mask_value](class_shapecast2d.md#class_ShapeCast2D_method_set_collision_mask_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_ShapeCast2D_property_collide_with_areas"></span>

[bool](class_bool.md#class_bool) **collide_with_areas** = `false` [🔗](class_shapecast2d.md#class_ShapeCast2D_property_collide_with_areas)

- void **set_collide_with_areas** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_areas_enabled** ( )

If `true`, collisions with [Area2D](class_area2d.md#class_Area2D) s will be reported.

---

<span id="class_ShapeCast2D_property_collide_with_bodies"></span>

[bool](class_bool.md#class_bool) **collide_with_bodies** = `true` [🔗](class_shapecast2d.md#class_ShapeCast2D_property_collide_with_bodies)

- void **set_collide_with_bodies** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_bodies_enabled** ( )

If `true`, collisions with [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) s will be reported.

---

<span id="class_ShapeCast2D_property_collision_mask"></span>

[int](class_int.md#class_int) **collision_mask** = `1` [🔗](class_shapecast2d.md#class_ShapeCast2D_property_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The shape's collision mask. Only objects in at least one collision layer enabled in the mask will be detected. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_ShapeCast2D_property_collision_result"></span>

[Array](class_array.md#class_Array) **collision_result** = `[]` [🔗](class_shapecast2d.md#class_ShapeCast2D_property_collision_result)

- [Array](class_array.md#class_Array) **get_collision_result** ( )

Returns the complete collision information from the collision sweep. The data returned is the same as in the [PhysicsDirectSpaceState2D.get_rest_info()](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D_method_get_rest_info) method.

---

<span id="class_ShapeCast2D_property_enabled"></span>

[bool](class_bool.md#class_bool) **enabled** = `true` [🔗](class_shapecast2d.md#class_ShapeCast2D_property_enabled)

- void **set_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_enabled** ( )

If `true`, collisions will be reported.

---

<span id="class_ShapeCast2D_property_exclude_parent"></span>

[bool](class_bool.md#class_bool) **exclude_parent** = `true` [🔗](class_shapecast2d.md#class_ShapeCast2D_property_exclude_parent)

- void **set_exclude_parent_body** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_exclude_parent_body** ( )

If `true`, the parent node will be excluded from collision detection.

---

<span id="class_ShapeCast2D_property_margin"></span>

[float](class_float.md#class_float) **margin** = `0.0` [🔗](class_shapecast2d.md#class_ShapeCast2D_property_margin)

- void **set_margin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_margin** ( )

The collision margin for the shape. A larger margin helps detecting collisions more consistently, at the cost of precision.

---

<span id="class_ShapeCast2D_property_max_results"></span>

[int](class_int.md#class_int) **max_results** = `32` [🔗](class_shapecast2d.md#class_ShapeCast2D_property_max_results)

- void **set_max_results** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_results** ( )

The number of intersections can be limited with this parameter, to reduce the processing time.

---

<span id="class_ShapeCast2D_property_shape"></span>

[Shape2D](class_shape2d.md#class_Shape2D) **shape** [🔗](class_shapecast2d.md#class_ShapeCast2D_property_shape)

- void **set_shape** ( value: [Shape2D](class_shape2d.md#class_Shape2D) )
- [Shape2D](class_shape2d.md#class_Shape2D) **get_shape** ( )

The shape to be used for collision queries.

---

<span id="class_ShapeCast2D_property_target_position"></span>

[Vector2](class_vector2.md#class_Vector2) **target_position** = `Vector2(0, 50)` [🔗](class_shapecast2d.md#class_ShapeCast2D_property_target_position)

- void **set_target_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_target_position** ( )

The shape's destination point, relative to this node's [Node2D.position](class_node2d.md#class_Node2D_property_position).

---

### Method Descriptions

<span id="class_ShapeCast2D_method_add_exception"></span>

void **add_exception** ( node: [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) ) [🔗](class_shapecast2d.md#class_ShapeCast2D_method_add_exception)

Adds a collision exception so the shape does not report collisions with the specified node.

---

<span id="class_ShapeCast2D_method_add_exception_rid"></span>

void **add_exception_rid** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_shapecast2d.md#class_ShapeCast2D_method_add_exception_rid)

Adds a collision exception so the shape does not report collisions with the specified [RID](class_rid.md#class_RID).

---

<span id="class_ShapeCast2D_method_clear_exceptions"></span>

void **clear_exceptions** ( ) [🔗](class_shapecast2d.md#class_ShapeCast2D_method_clear_exceptions)

Removes all collision exceptions for this shape.

---

<span id="class_ShapeCast2D_method_force_shapecast_update"></span>

void **force_shapecast_update** ( ) [🔗](class_shapecast2d.md#class_ShapeCast2D_method_force_shapecast_update)

Updates the collision information for the shape immediately, without waiting for the next `_physics_process` call. Use this method, for example, when the shape or its parent has changed state.

 **Note:** Setting [enabled](class_shapecast2d.md#class_ShapeCast2D_property_enabled) to `true` is not required for this to work.

---

<span id="class_ShapeCast2D_method_get_closest_collision_safe_fraction"></span>

[float](class_float.md#class_float) **get_closest_collision_safe_fraction** ( ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_get_closest_collision_safe_fraction)

Returns the fraction from this cast's origin to its [target_position](class_shapecast2d.md#class_ShapeCast2D_property_target_position) of how far the shape can move without triggering a collision, as a value between `0.0` and `1.0`.

---

<span id="class_ShapeCast2D_method_get_closest_collision_unsafe_fraction"></span>

[float](class_float.md#class_float) **get_closest_collision_unsafe_fraction** ( ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_get_closest_collision_unsafe_fraction)

Returns the fraction from this cast's origin to its [target_position](class_shapecast2d.md#class_ShapeCast2D_property_target_position) of how far the shape must move to trigger a collision, as a value between `0.0` and `1.0`.

In ideal conditions this would be the same as [get_closest_collision_safe_fraction()](class_shapecast2d.md#class_ShapeCast2D_method_get_closest_collision_safe_fraction), however shape casting is calculated in discrete steps, so the precise point of collision can occur between two calculated positions.

---

<span id="class_ShapeCast2D_method_get_collider"></span>

[Object](class_object.md#class_Object) **get_collider** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_get_collider)

Returns the collided [Object](class_object.md#class_Object) of one of the multiple collisions at `index`, or `null` if no object is intersecting the shape (i.e. [is_colliding()](class_shapecast2d.md#class_ShapeCast2D_method_is_colliding) returns `false`).

---

<span id="class_ShapeCast2D_method_get_collider_rid"></span>

[RID](class_rid.md#class_RID) **get_collider_rid** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_get_collider_rid)

Returns the [RID](class_rid.md#class_RID) of the collided object of one of the multiple collisions at `index`.

---

<span id="class_ShapeCast2D_method_get_collider_shape"></span>

[int](class_int.md#class_int) **get_collider_shape** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_get_collider_shape)

Returns the shape ID of the colliding shape of one of the multiple collisions at `index`, or `0` if no object is intersecting the shape (i.e. [is_colliding()](class_shapecast2d.md#class_ShapeCast2D_method_is_colliding) returns `false`).

---

<span id="class_ShapeCast2D_method_get_collision_count"></span>

[int](class_int.md#class_int) **get_collision_count** ( ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_count)

The number of collisions detected at the point of impact. Use this to iterate over multiple collisions as provided by [get_collider()](class_shapecast2d.md#class_ShapeCast2D_method_get_collider), [get_collider_shape()](class_shapecast2d.md#class_ShapeCast2D_method_get_collider_shape), [get_collision_point()](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_point), and [get_collision_normal()](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_normal) methods.

---

<span id="class_ShapeCast2D_method_get_collision_mask_value"></span>

[bool](class_bool.md#class_bool) **get_collision_mask_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_mask_value)

Returns whether or not the specified layer of the [collision_mask](class_shapecast2d.md#class_ShapeCast2D_property_collision_mask) is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_ShapeCast2D_method_get_collision_normal"></span>

[Vector2](class_vector2.md#class_Vector2) **get_collision_normal** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_normal)

Returns the normal of one of the multiple collisions at `index` of the intersecting object.

---

<span id="class_ShapeCast2D_method_get_collision_point"></span>

[Vector2](class_vector2.md#class_Vector2) **get_collision_point** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_get_collision_point)

Returns the collision point of one of the multiple collisions at `index` where the shape intersects the colliding object.

 **Note:** This point is in the **global** coordinate system.

---

<span id="class_ShapeCast2D_method_is_colliding"></span>

[bool](class_bool.md#class_bool) **is_colliding** ( ) *const* [🔗](class_shapecast2d.md#class_ShapeCast2D_method_is_colliding)

Returns whether any object is intersecting with the shape's vector (considering the vector length).

---

<span id="class_ShapeCast2D_method_remove_exception"></span>

void **remove_exception** ( node: [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) ) [🔗](class_shapecast2d.md#class_ShapeCast2D_method_remove_exception)

Removes a collision exception so the shape does report collisions with the specified node.

---

<span id="class_ShapeCast2D_method_remove_exception_rid"></span>

void **remove_exception_rid** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_shapecast2d.md#class_ShapeCast2D_method_remove_exception_rid)

Removes a collision exception so the shape does report collisions with the specified [RID](class_rid.md#class_RID).

---

<span id="class_ShapeCast2D_method_set_collision_mask_value"></span>

void **set_collision_mask_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_shapecast2d.md#class_ShapeCast2D_method_set_collision_mask_value)

Based on `value`, enables or disables the specified layer in the [collision_mask](class_shapecast2d.md#class_ShapeCast2D_property_collision_mask), given a `layer_number` between 1 and 32.
