<span id="class_CircleShape2D"></span>

## CircleShape2D

**Inherits:** [Shape2D](class_shape2d.md#class_Shape2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 2D circle shape used for physics collision.

### Description

A 2D circle shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D).

 **Performance:** **CircleShape2D** is fast to check collisions against. It is faster than [RectangleShape2D](class_rectangleshape2d.md#class_RectangleShape2D) and [CapsuleShape2D](class_capsuleshape2d.md#class_CapsuleShape2D).

### Properties


| [float](class_float.md#class_float) | [radius](class_circleshape2d.md#class_CircleShape2D_property_radius) | `10.0` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_CircleShape2D_property_radius"></span>

[float](class_float.md#class_float) **radius** = `10.0` [🔗](class_circleshape2d.md#class_CircleShape2D_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The circle's radius.
