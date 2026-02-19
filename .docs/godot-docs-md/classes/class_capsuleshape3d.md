<span id="class_CapsuleShape3D"></span>

## CapsuleShape3D

**Inherits:** [Shape3D](class_shape3d.md#class_Shape3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 3D capsule shape used for physics collision.

### Description

A 3D capsule shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D).

 **Performance:** **CapsuleShape3D** is fast to check collisions against. It is faster than [CylinderShape3D](class_cylindershape3d.md#class_CylinderShape3D), but slower than [SphereShape3D](class_sphereshape3d.md#class_SphereShape3D) and [BoxShape3D](class_boxshape3d.md#class_BoxShape3D).

### Tutorials

- 3D Physics Tests Demo

### Properties


| [float](class_float.md#class_float) | [height](class_capsuleshape3d.md#class_CapsuleShape3D_property_height) | `2.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [mid_height](class_capsuleshape3d.md#class_CapsuleShape3D_property_mid_height) |
| [float](class_float.md#class_float) | [radius](class_capsuleshape3d.md#class_CapsuleShape3D_property_radius) | `0.5` |

---

### Property Descriptions

<span id="class_CapsuleShape3D_property_height"></span>

[float](class_float.md#class_float) **height** = `2.0` [🔗](class_capsuleshape3d.md#class_CapsuleShape3D_property_height)

- void **set_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height** ( )

The capsule's full height, including the hemispheres.

 **Note:** The [height](class_capsuleshape3d.md#class_CapsuleShape3D_property_height) of a capsule must be at least twice its [radius](class_capsuleshape3d.md#class_CapsuleShape3D_property_radius). Otherwise, the capsule becomes a sphere. If the [height](class_capsuleshape3d.md#class_CapsuleShape3D_property_height) is less than twice the [radius](class_capsuleshape3d.md#class_CapsuleShape3D_property_radius), the properties adjust to a valid value.

---

<span id="class_CapsuleShape3D_property_mid_height"></span>

[float](class_float.md#class_float) **mid_height** [🔗](class_capsuleshape3d.md#class_CapsuleShape3D_property_mid_height)

- void **set_mid_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_mid_height** ( )

The capsule's height, excluding the hemispheres. This is the height of the central cylindrical part in the middle of the capsule, and is the distance between the centers of the two hemispheres. This is a wrapper for [height](class_capsuleshape3d.md#class_CapsuleShape3D_property_height).

---

<span id="class_CapsuleShape3D_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.5` [🔗](class_capsuleshape3d.md#class_CapsuleShape3D_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The capsule's radius.

 **Note:** The [radius](class_capsuleshape3d.md#class_CapsuleShape3D_property_radius) of a capsule cannot be greater than half of its [height](class_capsuleshape3d.md#class_CapsuleShape3D_property_height). Otherwise, the capsule becomes a sphere. If the [radius](class_capsuleshape3d.md#class_CapsuleShape3D_property_radius) is greater than half of the [height](class_capsuleshape3d.md#class_CapsuleShape3D_property_height), the properties adjust to a valid value.
