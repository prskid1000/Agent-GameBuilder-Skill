<span id="class_CapsuleShape2D"></span>

## CapsuleShape2D

**Inherits:** [Shape2D](class_shape2d.md#class_Shape2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 2D capsule shape used for physics collision.

### Description

A 2D capsule shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D).

 **Performance:** **CapsuleShape2D** is fast to check collisions against, but it is slower than [RectangleShape2D](class_rectangleshape2d.md#class_RectangleShape2D) and [CircleShape2D](class_circleshape2d.md#class_CircleShape2D).

### Properties


| [float](class_float.md#class_float) | [height](class_capsuleshape2d.md#class_CapsuleShape2D_property_height) | `30.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [mid_height](class_capsuleshape2d.md#class_CapsuleShape2D_property_mid_height) |
| [float](class_float.md#class_float) | [radius](class_capsuleshape2d.md#class_CapsuleShape2D_property_radius) | `10.0` |

---

### Property Descriptions

<span id="class_CapsuleShape2D_property_height"></span>

[float](class_float.md#class_float) **height** = `30.0` [🔗](class_capsuleshape2d.md#class_CapsuleShape2D_property_height)

- void **set_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height** ( )

The capsule's full height, including the semicircles.

 **Note:** The [height](class_capsuleshape2d.md#class_CapsuleShape2D_property_height) of a capsule must be at least twice its [radius](class_capsuleshape2d.md#class_CapsuleShape2D_property_radius). Otherwise, the capsule becomes a circle. If the [height](class_capsuleshape2d.md#class_CapsuleShape2D_property_height) is less than twice the [radius](class_capsuleshape2d.md#class_CapsuleShape2D_property_radius), the properties adjust to a valid value.

---

<span id="class_CapsuleShape2D_property_mid_height"></span>

[float](class_float.md#class_float) **mid_height** [🔗](class_capsuleshape2d.md#class_CapsuleShape2D_property_mid_height)

- void **set_mid_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_mid_height** ( )

The capsule's height, excluding the semicircles. This is the height of the central rectangular part in the middle of the capsule, and is the distance between the centers of the two semicircles. This is a wrapper for [height](class_capsuleshape2d.md#class_CapsuleShape2D_property_height).

---

<span id="class_CapsuleShape2D_property_radius"></span>

[float](class_float.md#class_float) **radius** = `10.0` [🔗](class_capsuleshape2d.md#class_CapsuleShape2D_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The capsule's radius.

 **Note:** The [radius](class_capsuleshape2d.md#class_CapsuleShape2D_property_radius) of a capsule cannot be greater than half of its [height](class_capsuleshape2d.md#class_CapsuleShape2D_property_height). Otherwise, the capsule becomes a circle. If the [radius](class_capsuleshape2d.md#class_CapsuleShape2D_property_radius) is greater than half of the [height](class_capsuleshape2d.md#class_CapsuleShape2D_property_height), the properties adjust to a valid value.
