<span id="class_QuadOccluder3D"></span>

## QuadOccluder3D

**Inherits:** [Occluder3D](class_occluder3d.md#class_Occluder3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Flat plane shape for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D).

### Description

**QuadOccluder3D** stores a flat plane shape that can be used by the engine's occlusion culling system. See also [PolygonOccluder3D](class_polygonoccluder3d.md#class_PolygonOccluder3D) if you need to customize the quad's shape.

See [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D)'s documentation for instructions on setting up occlusion culling.

### Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [size](class_quadoccluder3d.md#class_QuadOccluder3D_property_size) | `Vector2(1, 1)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_QuadOccluder3D_property_size"></span>

[Vector2](class_vector2.md#class_Vector2) **size** = `Vector2(1, 1)` [🔗](class_quadoccluder3d.md#class_QuadOccluder3D_property_size)

- void **set_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_size** ( )

The quad's size in 3D units.
