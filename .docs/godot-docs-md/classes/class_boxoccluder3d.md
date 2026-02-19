<span id="class_BoxOccluder3D"></span>

## BoxOccluder3D

**Inherits:** [Occluder3D](class_occluder3d.md#class_Occluder3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Cuboid shape for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D).

### Description

**BoxOccluder3D** stores a cuboid shape that can be used by the engine's occlusion culling system.

See [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D)'s documentation for instructions on setting up occlusion culling.

### Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [size](class_boxoccluder3d.md#class_BoxOccluder3D_property_size) | `Vector3(1, 1, 1)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_BoxOccluder3D_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_boxoccluder3d.md#class_BoxOccluder3D_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The box's size in 3D units.
