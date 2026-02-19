<span id="class_BoxShape3D"></span>

## BoxShape3D

**Inherits:** [Shape3D](class_shape3d.md#class_Shape3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 3D box shape used for physics collision.

### Description

A 3D box shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D).

 **Performance:** **BoxShape3D** is fast to check collisions against. It is faster than [CapsuleShape3D](class_capsuleshape3d.md#class_CapsuleShape3D) and [CylinderShape3D](class_cylindershape3d.md#class_CylinderShape3D), but slower than [SphereShape3D](class_sphereshape3d.md#class_SphereShape3D).

### Tutorials

- 3D Physics Tests Demo

- 3D Kinematic Character Demo

- 3D Platformer Demo

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [size](class_boxshape3d.md#class_BoxShape3D_property_size) | `Vector3(1, 1, 1)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_BoxShape3D_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_boxshape3d.md#class_BoxShape3D_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The box's width, height and depth.
