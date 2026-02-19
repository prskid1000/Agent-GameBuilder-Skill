<span id="class_ArrayOccluder3D"></span>

## ArrayOccluder3D

**Inherits:** [Occluder3D](class_occluder3d.md#class_Occluder3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

3D polygon shape for use with occlusion culling in [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D).

### Description

**ArrayOccluder3D** stores an arbitrary 3D polygon shape that can be used by the engine's occlusion culling system. This is analogous to [ArrayMesh](class_arraymesh.md#class_ArrayMesh), but for occluders.

See [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D)'s documentation for instructions on setting up occlusion culling.

### Tutorials

- [Occlusion culling](../tutorials/3d/occlusion_culling.md)

### Properties


| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [indices](class_arrayoccluder3d.md#class_ArrayOccluder3D_property_indices) | `PackedInt32Array()` |
| --- | --- | --- |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [vertices](class_arrayoccluder3d.md#class_ArrayOccluder3D_property_vertices) | `PackedVector3Array()` |

### Methods


| void | [set_arrays](class_arrayoccluder3d.md#class_ArrayOccluder3D_method_set_arrays) ( vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| --- | --- |

---

### Property Descriptions

<span id="class_ArrayOccluder3D_property_indices"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **indices** = `PackedInt32Array()` [🔗](class_arrayoccluder3d.md#class_ArrayOccluder3D_property_indices)

- void **set_indices** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_indices** ( )

The occluder's index position. Indices determine which points from the [vertices](class_arrayoccluder3d.md#class_ArrayOccluder3D_property_vertices) array should be drawn, and in which order.

 **Note:** The occluder is always updated after setting this value. If creating occluders procedurally, consider using [set_arrays()](class_arrayoccluder3d.md#class_ArrayOccluder3D_method_set_arrays) instead to avoid updating the occluder twice when it's created.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_ArrayOccluder3D_property_vertices"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **vertices** = `PackedVector3Array()` [🔗](class_arrayoccluder3d.md#class_ArrayOccluder3D_property_vertices)

- void **set_vertices** ( value: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) )
- [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_vertices** ( )

The occluder's vertex positions in local 3D coordinates.

 **Note:** The occluder is always updated after setting this value. If creating occluders procedurally, consider using [set_arrays()](class_arrayoccluder3d.md#class_ArrayOccluder3D_method_set_arrays) instead to avoid updating the occluder twice when it's created.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) for more details.

---

### Method Descriptions

<span id="class_ArrayOccluder3D_method_set_arrays"></span>

void **set_arrays** ( vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_arrayoccluder3d.md#class_ArrayOccluder3D_method_set_arrays)

Sets [indices](class_arrayoccluder3d.md#class_ArrayOccluder3D_property_indices) and [vertices](class_arrayoccluder3d.md#class_ArrayOccluder3D_property_vertices), while updating the final occluder only once after both values are set.
