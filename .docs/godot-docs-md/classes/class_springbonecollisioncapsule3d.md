<span id="class_SpringBoneCollisionCapsule3D"></span>

## SpringBoneCollisionCapsule3D

**Inherits:** [SpringBoneCollision3D](class_springbonecollision3d.md#class_SpringBoneCollision3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A capsule shape collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class_SpringBoneSimulator3D).

### Description

A capsule shape collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class_SpringBoneSimulator3D).

### Properties


| [float](class_float.md#class_float) | [height](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_height) | `0.5` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [inside](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_inside) | `false` |
| [float](class_float.md#class_float) | [mid_height](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_mid_height) |
| [float](class_float.md#class_float) | [radius](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_radius) | `0.1` |

---

### Property Descriptions

<span id="class_SpringBoneCollisionCapsule3D_property_height"></span>

[float](class_float.md#class_float) **height** = `0.5` [🔗](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_height)

- void **set_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height** ( )

The capsule's full height, including the hemispheres.

 **Note:** The [height](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_height) of a capsule must be at least twice its [radius](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_radius). Otherwise, the capsule becomes a sphere. If the [height](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_height) is less than twice the [radius](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_radius), the properties adjust to a valid value.

---

<span id="class_SpringBoneCollisionCapsule3D_property_inside"></span>

[bool](class_bool.md#class_bool) **inside** = `false` [🔗](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_inside)

- void **set_inside** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_inside** ( )

If `true`, the collision acts to trap the joint within the collision.

---

<span id="class_SpringBoneCollisionCapsule3D_property_mid_height"></span>

[float](class_float.md#class_float) **mid_height** [🔗](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_mid_height)

- void **set_mid_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_mid_height** ( )

The capsule's height, excluding the hemispheres. This is the height of the central cylindrical part in the middle of the capsule, and is the distance between the centers of the two hemispheres. This is a wrapper for [height](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_height).

---

<span id="class_SpringBoneCollisionCapsule3D_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.1` [🔗](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The capsule's radius.

 **Note:** The [radius](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_radius) of a capsule cannot be greater than half of its [height](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_height). Otherwise, the capsule becomes a sphere. If the [radius](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_radius) is greater than half of the [height](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D_property_height), the properties adjust to a valid value.
