<span id="class_SphereShape3D"></span>

## SphereShape3D

**Inherits:** [Shape3D](class_shape3d.md#class_Shape3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 3D sphere shape used for physics collision.

### Description

A 3D sphere shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D).

 **Performance:** **SphereShape3D** is fast to check collisions against. It is faster than [BoxShape3D](class_boxshape3d.md#class_BoxShape3D), [CapsuleShape3D](class_capsuleshape3d.md#class_CapsuleShape3D), and [CylinderShape3D](class_cylindershape3d.md#class_CylinderShape3D).

### Tutorials

- 3D Physics Tests Demo

### Properties


| [float](class_float.md#class_float) | [radius](class_sphereshape3d.md#class_SphereShape3D_property_radius) | `0.5` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_SphereShape3D_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.5` [🔗](class_sphereshape3d.md#class_SphereShape3D_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The sphere's radius. The shape's diameter is double the radius.
