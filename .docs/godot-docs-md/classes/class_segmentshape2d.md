<span id="class_SegmentShape2D"></span>

## SegmentShape2D

**Inherits:** [Shape2D](class_shape2d.md#class_Shape2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 2D line segment shape used for physics collision.

### Description

A 2D line segment shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D).

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [a](class_segmentshape2d.md#class_SegmentShape2D_property_a) | `Vector2(0, 0)` |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [b](class_segmentshape2d.md#class_SegmentShape2D_property_b) | `Vector2(0, 10)` |

---

### Property Descriptions

<span id="class_SegmentShape2D_property_a"></span>

[Vector2](class_vector2.md#class_Vector2) **a** = `Vector2(0, 0)` [🔗](class_segmentshape2d.md#class_SegmentShape2D_property_a)

- void **set_a** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_a** ( )

The segment's first point position.

---

<span id="class_SegmentShape2D_property_b"></span>

[Vector2](class_vector2.md#class_Vector2) **b** = `Vector2(0, 10)` [🔗](class_segmentshape2d.md#class_SegmentShape2D_property_b)

- void **set_b** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_b** ( )

The segment's second point position.
