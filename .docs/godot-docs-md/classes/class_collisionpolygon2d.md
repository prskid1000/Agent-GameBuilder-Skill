<span id="class_CollisionPolygon2D"></span>

## CollisionPolygon2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node that provides a polygon shape to a [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) parent.

### Description

A node that provides a polygon shape to a [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an [Area2D](class_area2d.md#class_Area2D), turn a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) into a solid object, or give a hollow shape to a [StaticBody2D](class_staticbody2d.md#class_StaticBody2D).

 **Warning:** A non-uniformly scaled **CollisionPolygon2D** will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its polygon instead.

### Properties


| [BuildMode](class_collisionpolygon2d.md#enum_CollisionPolygon2D_BuildMode) | [build_mode](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_build_mode) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [disabled](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_disabled) | `false` |
| [bool](class_bool.md#class_bool) | [one_way_collision](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_one_way_collision) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [one_way_collision_direction](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_one_way_collision_direction) | `Vector2(0, 1)` |
| [float](class_float.md#class_float) | [one_way_collision_margin](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_one_way_collision_margin) | `1.0` |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [polygon](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_polygon) | `PackedVector2Array()` |

---

### Enumerations

<span id="enum_CollisionPolygon2D_BuildMode"></span>

enum **BuildMode**: [🔗](class_collisionpolygon2d.md#enum_CollisionPolygon2D_BuildMode)

<span id="class_CollisionPolygon2D_constant_BUILD_SOLIDS"></span>

[BuildMode](class_collisionpolygon2d.md#enum_CollisionPolygon2D_BuildMode) **BUILD_SOLIDS** = `0`

Collisions will include the polygon and its contained area. In this mode the node has the same effect as several [ConvexPolygonShape2D](class_convexpolygonshape2d.md#class_ConvexPolygonShape2D) nodes, one for each convex shape in the convex decomposition of the polygon (but without the overhead of multiple nodes).

<span id="class_CollisionPolygon2D_constant_BUILD_SEGMENTS"></span>

[BuildMode](class_collisionpolygon2d.md#enum_CollisionPolygon2D_BuildMode) **BUILD_SEGMENTS** = `1`

Collisions will only include the polygon edges. In this mode the node has the same effect as a single [ConcavePolygonShape2D](class_concavepolygonshape2d.md#class_ConcavePolygonShape2D) made of segments, with the restriction that each segment (after the first one) starts where the previous one ends, and the last one ends where the first one starts (forming a closed but hollow polygon).

---

### Property Descriptions

<span id="class_CollisionPolygon2D_property_build_mode"></span>

[BuildMode](class_collisionpolygon2d.md#enum_CollisionPolygon2D_BuildMode) **build_mode** = `0` [🔗](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_build_mode)

- void **set_build_mode** ( value: [BuildMode](class_collisionpolygon2d.md#enum_CollisionPolygon2D_BuildMode) )
- [BuildMode](class_collisionpolygon2d.md#enum_CollisionPolygon2D_BuildMode) **get_build_mode** ( )

Collision build mode.

---

<span id="class_CollisionPolygon2D_property_disabled"></span>

[bool](class_bool.md#class_bool) **disabled** = `false` [🔗](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_disabled)

- void **set_disabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_disabled** ( )

If `true`, no collisions will be detected. This property should be changed with [Object.set_deferred()](class_object.md#class_Object_method_set_deferred).

---

<span id="class_CollisionPolygon2D_property_one_way_collision"></span>

[bool](class_bool.md#class_bool) **one_way_collision** = `false` [🔗](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_one_way_collision)

- void **set_one_way_collision** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_one_way_collision_enabled** ( )

If `true`, only edges that face up, relative to **CollisionPolygon2D**'s rotation, will collide with other objects.

 **Note:** This property has no effect if this **CollisionPolygon2D** is a child of an [Area2D](class_area2d.md#class_Area2D) node.

 **Note:** The one way collision direction can be configured by setting [one_way_collision_direction](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_one_way_collision_direction).

---

<span id="class_CollisionPolygon2D_property_one_way_collision_direction"></span>

[Vector2](class_vector2.md#class_Vector2) **one_way_collision_direction** = `Vector2(0, 1)` [🔗](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_one_way_collision_direction)

- void **set_one_way_collision_direction** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_one_way_collision_direction** ( )

The direction used for one-way collision.

---

<span id="class_CollisionPolygon2D_property_one_way_collision_margin"></span>

[float](class_float.md#class_float) **one_way_collision_margin** = `1.0` [🔗](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_one_way_collision_margin)

- void **set_one_way_collision_margin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_one_way_collision_margin** ( )

The margin used for one-way collision (in pixels). Higher values will make the shape thicker, and work better for colliders that enter the polygon at a high velocity.

---

<span id="class_CollisionPolygon2D_property_polygon"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **polygon** = `PackedVector2Array()` [🔗](class_collisionpolygon2d.md#class_CollisionPolygon2D_property_polygon)

- void **set_polygon** ( value: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )
- [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_polygon** ( )

The polygon's list of vertices. Each point will be connected to the next, and the final point will be connected to the first.

 **Note:** The returned vertices are in the local coordinate space of the given **CollisionPolygon2D**.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.
