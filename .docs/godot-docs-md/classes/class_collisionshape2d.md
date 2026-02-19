<span id="class_CollisionShape2D"></span>

## CollisionShape2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node that provides a [Shape2D](class_shape2d.md#class_Shape2D) to a [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) parent.

### Description

A node that provides a [Shape2D](class_shape2d.md#class_Shape2D) to a [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) parent and allows it to be edited. This can give a detection shape to an [Area2D](class_area2d.md#class_Area2D) or turn a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) into a solid object.

### Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

- 2D Dodge The Creeps Demo

- 2D Pong Demo

- 2D Kinematic Character Demo

### Properties


| [Color](class_color.md#class_Color) | [debug_color](class_collisionshape2d.md#class_CollisionShape2D_property_debug_color) | `Color(0, 0, 0, 0)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [disabled](class_collisionshape2d.md#class_CollisionShape2D_property_disabled) | `false` |
| [bool](class_bool.md#class_bool) | [one_way_collision](class_collisionshape2d.md#class_CollisionShape2D_property_one_way_collision) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [one_way_collision_direction](class_collisionshape2d.md#class_CollisionShape2D_property_one_way_collision_direction) | `Vector2(0, 1)` |
| [float](class_float.md#class_float) | [one_way_collision_margin](class_collisionshape2d.md#class_CollisionShape2D_property_one_way_collision_margin) | `1.0` |
| [Shape2D](class_shape2d.md#class_Shape2D) | [shape](class_collisionshape2d.md#class_CollisionShape2D_property_shape) |

---

### Property Descriptions

<span id="class_CollisionShape2D_property_debug_color"></span>

[Color](class_color.md#class_Color) **debug_color** = `Color(0, 0, 0, 0)` [🔗](class_collisionshape2d.md#class_CollisionShape2D_property_debug_color)

- void **set_debug_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_debug_color** ( )

The collision shape color that is displayed in the editor, or in the running project if **Debug > Visible Collision Shapes** is checked at the top of the editor.

 **Note:** The default value is ProjectSettings.debug/shapes/collision/shape_color. The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.

---

<span id="class_CollisionShape2D_property_disabled"></span>

[bool](class_bool.md#class_bool) **disabled** = `false` [🔗](class_collisionshape2d.md#class_CollisionShape2D_property_disabled)

- void **set_disabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_disabled** ( )

A disabled collision shape has no effect in the world. This property should be changed with [Object.set_deferred()](class_object.md#class_Object_method_set_deferred).

---

<span id="class_CollisionShape2D_property_one_way_collision"></span>

[bool](class_bool.md#class_bool) **one_way_collision** = `false` [🔗](class_collisionshape2d.md#class_CollisionShape2D_property_one_way_collision)

- void **set_one_way_collision** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_one_way_collision_enabled** ( )

Sets whether this collision shape should only detect collision on one side (top or bottom).

 **Note:** This property has no effect if this **CollisionShape2D** is a child of an [Area2D](class_area2d.md#class_Area2D) node.

 **Note:** The one way collision direction can be configured by setting [one_way_collision_direction](class_collisionshape2d.md#class_CollisionShape2D_property_one_way_collision_direction).

---

<span id="class_CollisionShape2D_property_one_way_collision_direction"></span>

[Vector2](class_vector2.md#class_Vector2) **one_way_collision_direction** = `Vector2(0, 1)` [🔗](class_collisionshape2d.md#class_CollisionShape2D_property_one_way_collision_direction)

- void **set_one_way_collision_direction** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_one_way_collision_direction** ( )

The direction used for one-way collision.

---

<span id="class_CollisionShape2D_property_one_way_collision_margin"></span>

[float](class_float.md#class_float) **one_way_collision_margin** = `1.0` [🔗](class_collisionshape2d.md#class_CollisionShape2D_property_one_way_collision_margin)

- void **set_one_way_collision_margin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_one_way_collision_margin** ( )

The margin used for one-way collision (in pixels). Higher values will make the shape thicker, and work better for colliders that enter the shape at a high velocity.

---

<span id="class_CollisionShape2D_property_shape"></span>

[Shape2D](class_shape2d.md#class_Shape2D) **shape** [🔗](class_collisionshape2d.md#class_CollisionShape2D_property_shape)

- void **set_shape** ( value: [Shape2D](class_shape2d.md#class_Shape2D) )
- [Shape2D](class_shape2d.md#class_Shape2D) **get_shape** ( )

The actual shape owned by this collision shape.
