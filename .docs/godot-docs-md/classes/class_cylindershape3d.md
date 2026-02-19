<span id="class_CylinderShape3D"></span>

## CylinderShape3D

**Inherits:** [Shape3D](class_shape3d.md#class_Shape3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 3D cylinder shape used for physics collision.

### Description

A 3D cylinder shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D).

 **Note:** There are several known bugs with cylinder collision shapes. Using [CapsuleShape3D](class_capsuleshape3d.md#class_CapsuleShape3D) or [BoxShape3D](class_boxshape3d.md#class_BoxShape3D) instead is recommended.

 **Performance:** **CylinderShape3D** is fast to check collisions against, but it is slower than [CapsuleShape3D](class_capsuleshape3d.md#class_CapsuleShape3D), [BoxShape3D](class_boxshape3d.md#class_BoxShape3D), and [SphereShape3D](class_sphereshape3d.md#class_SphereShape3D).

### Tutorials

- Third Person Shooter (TPS) Demo

- 3D Physics Tests Demo

- 3D Voxel Demo

### Properties


| [float](class_float.md#class_float) | [height](class_cylindershape3d.md#class_CylinderShape3D_property_height) | `2.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [radius](class_cylindershape3d.md#class_CylinderShape3D_property_radius) | `0.5` |

---

### Property Descriptions

<span id="class_CylinderShape3D_property_height"></span>

[float](class_float.md#class_float) **height** = `2.0` [🔗](class_cylindershape3d.md#class_CylinderShape3D_property_height)

- void **set_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height** ( )

The cylinder's height.

---

<span id="class_CylinderShape3D_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.5` [🔗](class_cylindershape3d.md#class_CylinderShape3D_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The cylinder's radius.
