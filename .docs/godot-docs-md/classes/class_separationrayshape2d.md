<span id="class_SeparationRayShape2D"></span>

## SeparationRayShape2D

**Inherits:** [Shape2D](class_shape2d.md#class_Shape2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 2D ray shape used for physics collision that tries to separate itself from any collider.

### Description

A 2D ray shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D). When a **SeparationRayShape2D** collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a **SeparationRayShape2D** next to a character can allow it to instantly move up when touching stairs.

### Properties


| [float](class_float.md#class_float) | [length](class_separationrayshape2d.md#class_SeparationRayShape2D_property_length) | `20.0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [slide_on_slope](class_separationrayshape2d.md#class_SeparationRayShape2D_property_slide_on_slope) | `false` |

---

### Property Descriptions

<span id="class_SeparationRayShape2D_property_length"></span>

[float](class_float.md#class_float) **length** = `20.0` [🔗](class_separationrayshape2d.md#class_SeparationRayShape2D_property_length)

- void **set_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_length** ( )

The ray's length.

---

<span id="class_SeparationRayShape2D_property_slide_on_slope"></span>

[bool](class_bool.md#class_bool) **slide_on_slope** = `false` [🔗](class_separationrayshape2d.md#class_SeparationRayShape2D_property_slide_on_slope)

- void **set_slide_on_slope** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_slide_on_slope** ( )

If `false` (default), the shape always separates and returns a normal along its own direction.

If `true`, the shape can return the correct normal and separate in any direction, allowing sliding motion on slopes.
