<span id="class_RectangleShape2D"></span>

## RectangleShape2D

**Inherits:** [Shape2D](class_shape2d.md#class_Shape2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 2D rectangle shape used for physics collision.

### Description

A 2D rectangle shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D).

 **Performance:** **RectangleShape2D** is fast to check collisions against. It is faster than [CapsuleShape2D](class_capsuleshape2d.md#class_CapsuleShape2D), but slower than [CircleShape2D](class_circleshape2d.md#class_CircleShape2D).

### Tutorials

- 2D Pong Demo

- 2D Kinematic Character Demo

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [size](class_rectangleshape2d.md#class_RectangleShape2D_property_size) | `Vector2(20, 20)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_RectangleShape2D_property_size"></span>

[Vector2](class_vector2.md#class_Vector2) **size** = `Vector2(20, 20)` [🔗](class_rectangleshape2d.md#class_RectangleShape2D_property_size)

- void **set_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_size** ( )

The rectangle's width and height.
