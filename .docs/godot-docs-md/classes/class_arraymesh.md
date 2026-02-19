<span id="class_ArrayMesh"></span>

## ArrayMesh

**Inherits:** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

[Mesh](class_mesh.md#class_Mesh) type that provides utility for constructing a surface from arrays.

### Description

The **ArrayMesh** is used to construct a [Mesh](class_mesh.md#class_Mesh) by specifying the attributes as arrays.

The most basic example is the creation of a single triangle:

.. tabs::

```
```

    var vertices = PackedVector3Array()
    vertices.push_back(Vector3(0, 1, 0))
    vertices.push_back(Vector3(1, 0, 0))
    vertices.push_back(Vector3(0, 0, 1))

    # Initialize the ArrayMesh.
    var arr_mesh = ArrayMesh.new()
    var arrays = []
    arrays.resize(Mesh.ARRAY_MAX)
    arrays[Mesh.ARRAY_VERTEX] = vertices

    # Create the Mesh.
    arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
    var m = MeshInstance3D.new()
    m.mesh = arr_mesh

```
```

    Vector3[] vertices =
    [
        new Vector3(0, 1, 0),
        new Vector3(1, 0, 0),
        new Vector3(0, 0, 1),
    ];

    // Initialize the ArrayMesh.
    var arrMesh = new ArrayMesh();
    Godot.Collections.Array arrays = [];
    arrays.Resize((int)Mesh.ArrayType.Max);
    arrays[(int)Mesh.ArrayType.Vertex] = vertices;

    // Create the Mesh.
    arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, arrays);
    var m = new MeshInstance3D();
    m.Mesh = arrMesh;

The [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) is ready to be added to the [SceneTree](class_scenetree.md#class_SceneTree) to be shown.

See also [ImmediateMesh](class_immediatemesh.md#class_ImmediateMesh), [MeshDataTool](class_meshdatatool.md#class_MeshDataTool) and [SurfaceTool](class_surfacetool.md#class_SurfaceTool) for procedural geometry generation.

 **Note:** Godot uses clockwise winding order for front faces of triangle primitive modes.

### Tutorials

- [Procedural geometry using the ArrayMesh](../tutorials/3d/procedural_geometry/arraymesh.md)

### Properties


| [BlendShapeMode](class_mesh.md#enum_Mesh_BlendShapeMode) | [blend_shape_mode](class_arraymesh.md#class_ArrayMesh_property_blend_shape_mode) | `1` |
| --- | --- | --- |
| [AABB](class_aabb.md#class_AABB) | [custom_aabb](class_arraymesh.md#class_ArrayMesh_property_custom_aabb) | `AABB(0, 0, 0, 0, 0, 0)` |
| [ArrayMesh](class_arraymesh.md#class_ArrayMesh) | [shadow_mesh](class_arraymesh.md#class_ArrayMesh_property_shadow_mesh) |

### Methods


| void | [add_blend_shape](class_arraymesh.md#class_ArrayMesh_method_add_blend_shape) ( name: [StringName](class_stringname.md#class_StringName) ) |
| --- | --- |
| void | [add_surface_from_arrays](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays) ( primitive: [PrimitiveType](class_mesh.md#enum_Mesh_PrimitiveType), arrays: [Array](class_array.md#class_Array), blend_shapes: [Array](class_array.md#class_Array)\[[Array](class_array.md#class_Array)\] = [], lods: [Dictionary](class_dictionary.md#class_Dictionary) = {}, flags: | bitfield | \[[ArrayFormat](class_mesh.md#enum_Mesh_ArrayFormat)\] = 0 ) |
| void | [clear_blend_shapes](class_arraymesh.md#class_ArrayMesh_method_clear_blend_shapes) ( ) |
| void | [clear_surfaces](class_arraymesh.md#class_ArrayMesh_method_clear_surfaces) ( ) |
| [int](class_int.md#class_int) | [get_blend_shape_count](class_arraymesh.md#class_ArrayMesh_method_get_blend_shape_count) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_blend_shape_name](class_arraymesh.md#class_ArrayMesh_method_get_blend_shape_name) ( index: [int](class_int.md#class_int) ) const |
| Error | [lightmap_unwrap](class_arraymesh.md#class_ArrayMesh_method_lightmap_unwrap) ( transform: [Transform3D](class_transform3d.md#class_Transform3D), texel_size: [float](class_float.md#class_float) ) |
| void | [regen_normal_maps](class_arraymesh.md#class_ArrayMesh_method_regen_normal_maps) ( ) |
| void | [set_blend_shape_name](class_arraymesh.md#class_ArrayMesh_method_set_blend_shape_name) ( index: [int](class_int.md#class_int), name: [StringName](class_stringname.md#class_StringName) ) |
| [int](class_int.md#class_int) | [surface_find_by_name](class_arraymesh.md#class_ArrayMesh_method_surface_find_by_name) ( name: [String](class_string.md#class_String) ) const |
| [int](class_int.md#class_int) | [surface_get_array_index_len](class_arraymesh.md#class_ArrayMesh_method_surface_get_array_index_len) ( surf_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [surface_get_array_len](class_arraymesh.md#class_ArrayMesh_method_surface_get_array_len) ( surf_idx: [int](class_int.md#class_int) ) const |
| bitfield | \[[ArrayFormat](class_mesh.md#enum_Mesh_ArrayFormat)\] | [surface_get_format](class_arraymesh.md#class_ArrayMesh_method_surface_get_format) ( surf_idx: [int](class_int.md#class_int) ) | const |
| [String](class_string.md#class_String) | [surface_get_name](class_arraymesh.md#class_ArrayMesh_method_surface_get_name) ( surf_idx: [int](class_int.md#class_int) ) const |
| [PrimitiveType](class_mesh.md#enum_Mesh_PrimitiveType) | [surface_get_primitive_type](class_arraymesh.md#class_ArrayMesh_method_surface_get_primitive_type) ( surf_idx: [int](class_int.md#class_int) ) const |
| void | [surface_remove](class_arraymesh.md#class_ArrayMesh_method_surface_remove) ( surf_idx: [int](class_int.md#class_int) ) |
| void | [surface_set_name](class_arraymesh.md#class_ArrayMesh_method_surface_set_name) ( surf_idx: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [surface_update_attribute_region](class_arraymesh.md#class_ArrayMesh_method_surface_update_attribute_region) ( surf_idx: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [surface_update_skin_region](class_arraymesh.md#class_ArrayMesh_method_surface_update_skin_region) ( surf_idx: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [surface_update_vertex_region](class_arraymesh.md#class_ArrayMesh_method_surface_update_vertex_region) ( surf_idx: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |

---

### Property Descriptions

<span id="class_ArrayMesh_property_blend_shape_mode"></span>

[BlendShapeMode](class_mesh.md#enum_Mesh_BlendShapeMode) **blend_shape_mode** = `1` [🔗](class_arraymesh.md#class_ArrayMesh_property_blend_shape_mode)

- void **set_blend_shape_mode** ( value: [BlendShapeMode](class_mesh.md#enum_Mesh_BlendShapeMode) )
- [BlendShapeMode](class_mesh.md#enum_Mesh_BlendShapeMode) **get_blend_shape_mode** ( )

The blend shape mode.

---

<span id="class_ArrayMesh_property_custom_aabb"></span>

[AABB](class_aabb.md#class_AABB) **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_arraymesh.md#class_ArrayMesh_property_custom_aabb)

- void **set_custom_aabb** ( value: [AABB](class_aabb.md#class_AABB) )
- [AABB](class_aabb.md#class_AABB) **get_custom_aabb** ( )

Overrides the [AABB](class_aabb.md#class_AABB) with one defined by user for use with frustum culling. Especially useful to avoid unexpected culling when using a shader to offset vertices.

---

<span id="class_ArrayMesh_property_shadow_mesh"></span>

[ArrayMesh](class_arraymesh.md#class_ArrayMesh) **shadow_mesh** [🔗](class_arraymesh.md#class_ArrayMesh_property_shadow_mesh)

- void **set_shadow_mesh** ( value: [ArrayMesh](class_arraymesh.md#class_ArrayMesh) )
- [ArrayMesh](class_arraymesh.md#class_ArrayMesh) **get_shadow_mesh** ( )

An optional mesh which can be used for rendering shadows and the depth prepass. Can be used to increase performance by supplying a mesh with fused vertices and only vertex position data (without normals, UVs, colors, etc.).

 **Note:** This mesh must have exactly the same vertex positions as the source mesh (including the source mesh's LODs, if present). If vertex positions differ, then the mesh will not draw correctly.

---

### Method Descriptions

<span id="class_ArrayMesh_method_add_blend_shape"></span>

void **add_blend_shape** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_arraymesh.md#class_ArrayMesh_method_add_blend_shape)

Adds name for a blend shape that will be added with [add_surface_from_arrays()](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays). Must be called before surface is added.

---

<span id="class_ArrayMesh_method_add_surface_from_arrays"></span>

void **add_surface_from_arrays** ( primitive: [PrimitiveType](class_mesh.md#enum_Mesh_PrimitiveType), arrays: [Array](class_array.md#class_Array), blend_shapes: [Array](class_array.md#class_Array)\[[Array](class_array.md#class_Array)\] = [], lods: [Dictionary](class_dictionary.md#class_Dictionary) = {}, flags: *BitField*\[[ArrayFormat](class_mesh.md#enum_Mesh_ArrayFormat)\] = 0 ) [🔗](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays)

Creates a new surface. [Mesh.get_surface_count()](class_mesh.md#class_Mesh_method_get_surface_count) will become the `surf_idx` for this new surface.

Surfaces are created to be rendered using a `primitive`, which may be any of the values defined in [PrimitiveType](class_mesh.md#enum_Mesh_PrimitiveType).

The `arrays` argument is an array of arrays. Each of the [Mesh.ARRAY_MAX](class_mesh.md#class_Mesh_constant_ARRAY_MAX) elements contains an array with some of the mesh data for this surface as described by the corresponding member of [ArrayType](class_mesh.md#enum_Mesh_ArrayType) or `null` if it is not used by the surface. For example, `arrays[0]` is the array of vertices. That first vertex sub-array is always required; the others are optional. Adding an index array puts this surface into "index mode" where the vertex and other arrays become the sources of data and the index array defines the vertex order. All sub-arrays must have the same length as the vertex array (or be an exact multiple of the vertex array's length, when multiple elements of a sub-array correspond to a single vertex) or be empty, except for [Mesh.ARRAY_INDEX](class_mesh.md#class_Mesh_constant_ARRAY_INDEX) if it is used.

The `blend_shapes` argument is an array of vertex data for each blend shape. Each element is an array of the same structure as `arrays`, but [Mesh.ARRAY_VERTEX](class_mesh.md#class_Mesh_constant_ARRAY_VERTEX), [Mesh.ARRAY_NORMAL](class_mesh.md#class_Mesh_constant_ARRAY_NORMAL), and [Mesh.ARRAY_TANGENT](class_mesh.md#class_Mesh_constant_ARRAY_TANGENT) are set if and only if they are set in `arrays` and all other entries are `null`.

The `lods` argument is a dictionary with [float](class_float.md#class_float) keys and [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) values. Each entry in the dictionary represents an LOD level of the surface, where the value is the [Mesh.ARRAY_INDEX](class_mesh.md#class_Mesh_constant_ARRAY_INDEX) array to use for the LOD level and the key is roughly proportional to the distance at which the LOD stats being used. I.e., increasing the key of an LOD also increases the distance that the objects has to be from the camera before the LOD is used.

The `flags` argument is the bitwise OR of, as required: One value of [ArrayCustomFormat](class_mesh.md#enum_Mesh_ArrayCustomFormat) left shifted by `ARRAY_FORMAT_CUSTOMn_SHIFT` for each custom channel in use, [Mesh.ARRAY_FLAG_USE_DYNAMIC_UPDATE](class_mesh.md#class_Mesh_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE), [Mesh.ARRAY_FLAG_USE_8_BONE_WEIGHTS](class_mesh.md#class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS), or [Mesh.ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY](class_mesh.md#class_Mesh_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY).

 **Note:** When using indices, it is recommended to only use points, lines, or triangles.

---

<span id="class_ArrayMesh_method_clear_blend_shapes"></span>

void **clear_blend_shapes** ( ) [🔗](class_arraymesh.md#class_ArrayMesh_method_clear_blend_shapes)

Removes all blend shapes from this **ArrayMesh**.

---

<span id="class_ArrayMesh_method_clear_surfaces"></span>

void **clear_surfaces** ( ) [🔗](class_arraymesh.md#class_ArrayMesh_method_clear_surfaces)

Removes all surfaces from this **ArrayMesh**.

---

<span id="class_ArrayMesh_method_get_blend_shape_count"></span>

[int](class_int.md#class_int) **get_blend_shape_count** ( ) *const* [🔗](class_arraymesh.md#class_ArrayMesh_method_get_blend_shape_count)

Returns the number of blend shapes that the **ArrayMesh** holds.

---

<span id="class_ArrayMesh_method_get_blend_shape_name"></span>

[StringName](class_stringname.md#class_StringName) **get_blend_shape_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_arraymesh.md#class_ArrayMesh_method_get_blend_shape_name)

Returns the name of the blend shape at this index.

---

<span id="class_ArrayMesh_method_lightmap_unwrap"></span>

Error **lightmap_unwrap** ( transform: [Transform3D](class_transform3d.md#class_Transform3D), texel_size: [float](class_float.md#class_float) ) [🔗](class_arraymesh.md#class_ArrayMesh_method_lightmap_unwrap)

Performs a UV unwrap on the **ArrayMesh** to prepare the mesh for lightmapping.

---

<span id="class_ArrayMesh_method_regen_normal_maps"></span>

void **regen_normal_maps** ( ) [🔗](class_arraymesh.md#class_ArrayMesh_method_regen_normal_maps)

Regenerates tangents for each of the **ArrayMesh**'s surfaces.

---

<span id="class_ArrayMesh_method_set_blend_shape_name"></span>

void **set_blend_shape_name** ( index: [int](class_int.md#class_int), name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_arraymesh.md#class_ArrayMesh_method_set_blend_shape_name)

Sets the name of the blend shape at this index.

---

<span id="class_ArrayMesh_method_surface_find_by_name"></span>

[int](class_int.md#class_int) **surface_find_by_name** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_find_by_name)

Returns the index of the first surface with this name held within this **ArrayMesh**. If none are found, -1 is returned.

---

<span id="class_ArrayMesh_method_surface_get_array_index_len"></span>

[int](class_int.md#class_int) **surface_get_array_index_len** ( surf_idx: [int](class_int.md#class_int) ) *const* [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_get_array_index_len)

Returns the length in indices of the index array in the requested surface (see [add_surface_from_arrays()](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays)).

---

<span id="class_ArrayMesh_method_surface_get_array_len"></span>

[int](class_int.md#class_int) **surface_get_array_len** ( surf_idx: [int](class_int.md#class_int) ) *const* [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_get_array_len)

Returns the length in vertices of the vertex array in the requested surface (see [add_surface_from_arrays()](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays)).

---

<span id="class_ArrayMesh_method_surface_get_format"></span>

*BitField*\[[ArrayFormat](class_mesh.md#enum_Mesh_ArrayFormat)\] **surface_get_format** ( surf_idx: [int](class_int.md#class_int) ) *const* [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_get_format)

Returns the format mask of the requested surface (see [add_surface_from_arrays()](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays)).

---

<span id="class_ArrayMesh_method_surface_get_name"></span>

[String](class_string.md#class_String) **surface_get_name** ( surf_idx: [int](class_int.md#class_int) ) *const* [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_get_name)

Gets the name assigned to this surface.

---

<span id="class_ArrayMesh_method_surface_get_primitive_type"></span>

[PrimitiveType](class_mesh.md#enum_Mesh_PrimitiveType) **surface_get_primitive_type** ( surf_idx: [int](class_int.md#class_int) ) *const* [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_get_primitive_type)

Returns the primitive type of the requested surface (see [add_surface_from_arrays()](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays)).

---

<span id="class_ArrayMesh_method_surface_remove"></span>

void **surface_remove** ( surf_idx: [int](class_int.md#class_int) ) [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_remove)

Removes the surface at the given index from the Mesh, shifting surfaces with higher index down by one.

---

<span id="class_ArrayMesh_method_surface_set_name"></span>

void **surface_set_name** ( surf_idx: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_set_name)

Sets a name for a given surface.

---

<span id="class_ArrayMesh_method_surface_update_attribute_region"></span>

void **surface_update_attribute_region** ( surf_idx: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_update_attribute_region)

Updates the attribute buffer of this mesh's surface with the given `data`. The expected data per attribute is 12 or 8 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class_Vector2), and 3 floats per [Vector3](class_vector3.md#class_Vector3)) depending on if the mesh is using [Vector3](class_vector3.md#class_Vector3) or [Vector2](class_vector2.md#class_Vector2) vertices. This value can be determined with [RenderingServer.mesh_surface_get_format_attribute_stride()](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_attribute_stride).

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each attribute.

A [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) of attribute locations can be converted into a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class_PackedVector3Array_method_to_byte_array) for use in `data`.

---

<span id="class_ArrayMesh_method_surface_update_skin_region"></span>

void **surface_update_skin_region** ( surf_idx: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_update_skin_region)

Updates the skin buffer of this mesh's surface with the given `data`. The expected data per skin is 12 or 8 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class_Vector2), and 3 floats per [Vector3](class_vector3.md#class_Vector3)) depending on if the mesh is using [Vector3](class_vector3.md#class_Vector3) or [Vector2](class_vector2.md#class_Vector2) vertices. This value can be determined with [RenderingServer.mesh_surface_get_format_skin_stride()](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_skin_stride).

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each skin.

A [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) of skin locations can be converted into a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class_PackedVector3Array_method_to_byte_array) for use in `data`.

---

<span id="class_ArrayMesh_method_surface_update_vertex_region"></span>

void **surface_update_vertex_region** ( surf_idx: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_arraymesh.md#class_ArrayMesh_method_surface_update_vertex_region)

Updates the vertex buffer of this mesh's surface with the given `data`. The expected data per vertex is 12 or 8 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class_Vector2), and 3 floats per [Vector3](class_vector3.md#class_Vector3)) depending on if the mesh is using [Vector3](class_vector3.md#class_Vector3) or [Vector2](class_vector2.md#class_Vector2) vertices. This value can be determined with [RenderingServer.mesh_surface_get_format_vertex_stride()](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_vertex_stride).

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each vertex.

A [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) of vertex locations can be converted into a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class_PackedVector3Array_method_to_byte_array) for use in `data`.
