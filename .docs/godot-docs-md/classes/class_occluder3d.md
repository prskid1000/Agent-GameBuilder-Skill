<span id="class_Occluder3D"></span>

## Occluder3D

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [ArrayOccluder3D](class_arrayoccluder3d.md#class_ArrayOccluder3D), [BoxOccluder3D](class_boxoccluder3d.md#class_BoxOccluder3D), [PolygonOccluder3D](class_polygonoccluder3d.md#class_PolygonOccluder3D), [QuadOccluder3D](class_quadoccluder3d.md#class_QuadOccluder3D), [SphereOccluder3D](class_sphereoccluder3d.md#class_SphereOccluder3D)

Occluder shape resource for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D).

### Description

**Occluder3D** stores an occluder shape that can be used by the engine's occlusion culling system.

See [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D)'s documentation for instructions on setting up occlusion culling.

### Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

### Methods


| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_indices](class_occluder3d.md#class_Occluder3D_method_get_indices) ( ) const |
| --- | --- |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [get_vertices](class_occluder3d.md#class_Occluder3D_method_get_vertices) ( ) const |

---

### Method Descriptions

<span id="class_Occluder3D_method_get_indices"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_indices** ( ) *const* [🔗](class_occluder3d.md#class_Occluder3D_method_get_indices)

Returns the occluder shape's vertex indices.

---

<span id="class_Occluder3D_method_get_vertices"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_vertices** ( ) *const* [🔗](class_occluder3d.md#class_Occluder3D_method_get_vertices)

Returns the occluder shape's vertex positions.
