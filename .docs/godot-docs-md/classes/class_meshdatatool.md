<span id="class_MeshDataTool"></span>

## MeshDataTool

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Helper tool to access and edit [Mesh](class_mesh.md#class_Mesh) data.

### Description

MeshDataTool provides access to individual vertices in a [Mesh](class_mesh.md#class_Mesh). It allows users to read and edit vertex data of meshes. It also creates an array of faces and edges.

To use MeshDataTool, load a mesh with [create_from_surface()](class_meshdatatool.md#class_MeshDataTool_method_create_from_surface). When you are finished editing the data commit the data to a mesh with [commit_to_surface()](class_meshdatatool.md#class_MeshDataTool_method_commit_to_surface).

Below is an example of how MeshDataTool may be used.

.. tabs::

```
```

    var mesh = ArrayMesh.new()
    mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, BoxMesh.new().get_mesh_arrays())
    var mdt = MeshDataTool.new()
    mdt.create_from_surface(mesh, 0)
    for i in range(mdt.get_vertex_count()):
        var vertex = mdt.get_vertex(i)
        # In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded.
        vertex += mdt.get_vertex_normal(i)
        # Save your change.
        mdt.set_vertex(i, vertex)
    mesh.clear_surfaces()
    mdt.commit_to_surface(mesh)
    var mi = MeshInstance.new()
    mi.mesh = mesh
    add_child(mi)

```
```

    var mesh = new ArrayMesh();
    mesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, new BoxMesh().GetMeshArrays());
    var mdt = new MeshDataTool();
    mdt.CreateFromSurface(mesh, 0);
    for (var i = 0; i < mdt.GetVertexCount(); i++)
    {
        Vector3 vertex = mdt.GetVertex(i);
        // In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded.
        vertex += mdt.GetVertexNormal(i);
        // Save your change.
        mdt.SetVertex(i, vertex);
    }
    mesh.ClearSurfaces();
    mdt.CommitToSurface(mesh);
    var mi = new MeshInstance();
    mi.Mesh = mesh;
    AddChild(mi);

See also [ArrayMesh](class_arraymesh.md#class_ArrayMesh), [ImmediateMesh](class_immediatemesh.md#class_ImmediateMesh) and [SurfaceTool](class_surfacetool.md#class_SurfaceTool) for procedural geometry generation.

 **Note:** Godot uses clockwise winding order for front faces of triangle primitive modes.

### Tutorials

- [Using the MeshDataTool](../tutorials/3d/procedural_geometry/meshdatatool.md)

### Methods


| void | [clear](class_meshdatatool.md#class_MeshDataTool_method_clear) ( ) |
| --- | --- |
| Error | [commit_to_surface](class_meshdatatool.md#class_MeshDataTool_method_commit_to_surface) ( mesh: [ArrayMesh](class_arraymesh.md#class_ArrayMesh), compression_flags: [int](class_int.md#class_int) = 0 ) |
| Error | [create_from_surface](class_meshdatatool.md#class_MeshDataTool_method_create_from_surface) ( mesh: [ArrayMesh](class_arraymesh.md#class_ArrayMesh), surface: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_edge_count](class_meshdatatool.md#class_MeshDataTool_method_get_edge_count) ( ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_edge_faces](class_meshdatatool.md#class_MeshDataTool_method_get_edge_faces) ( idx: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_edge_meta](class_meshdatatool.md#class_MeshDataTool_method_get_edge_meta) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_edge_vertex](class_meshdatatool.md#class_MeshDataTool_method_get_edge_vertex) ( idx: [int](class_int.md#class_int), vertex: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_face_count](class_meshdatatool.md#class_MeshDataTool_method_get_face_count) ( ) const |
| [int](class_int.md#class_int) | [get_face_edge](class_meshdatatool.md#class_MeshDataTool_method_get_face_edge) ( idx: [int](class_int.md#class_int), edge: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_face_meta](class_meshdatatool.md#class_MeshDataTool_method_get_face_meta) ( idx: [int](class_int.md#class_int) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_face_normal](class_meshdatatool.md#class_MeshDataTool_method_get_face_normal) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_face_vertex](class_meshdatatool.md#class_MeshDataTool_method_get_face_vertex) ( idx: [int](class_int.md#class_int), vertex: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_format](class_meshdatatool.md#class_MeshDataTool_method_get_format) ( ) const |
| [Material](class_material.md#class_Material) | [get_material](class_meshdatatool.md#class_MeshDataTool_method_get_material) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_vertex](class_meshdatatool.md#class_MeshDataTool_method_get_vertex) ( idx: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_vertex_bones](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_bones) ( idx: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_vertex_color](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_color) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_vertex_count](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_count) ( ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_vertex_edges](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_edges) ( idx: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_vertex_faces](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_faces) ( idx: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_vertex_meta](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_meta) ( idx: [int](class_int.md#class_int) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_vertex_normal](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_normal) ( idx: [int](class_int.md#class_int) ) const |
| [Plane](class_plane.md#class_Plane) | [get_vertex_tangent](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_tangent) ( idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_vertex_uv](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_uv) ( idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_vertex_uv2](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_uv2) ( idx: [int](class_int.md#class_int) ) const |
| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [get_vertex_weights](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_weights) ( idx: [int](class_int.md#class_int) ) const |
| void | [set_edge_meta](class_meshdatatool.md#class_MeshDataTool_method_set_edge_meta) ( idx: [int](class_int.md#class_int), meta: [Variant](class_variant.md#class_Variant) ) |
| void | [set_face_meta](class_meshdatatool.md#class_MeshDataTool_method_set_face_meta) ( idx: [int](class_int.md#class_int), meta: [Variant](class_variant.md#class_Variant) ) |
| void | [set_material](class_meshdatatool.md#class_MeshDataTool_method_set_material) ( material: [Material](class_material.md#class_Material) ) |
| void | [set_vertex](class_meshdatatool.md#class_MeshDataTool_method_set_vertex) ( idx: [int](class_int.md#class_int), vertex: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [set_vertex_bones](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_bones) ( idx: [int](class_int.md#class_int), bones: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| void | [set_vertex_color](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_color) ( idx: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_vertex_meta](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_meta) ( idx: [int](class_int.md#class_int), meta: [Variant](class_variant.md#class_Variant) ) |
| void | [set_vertex_normal](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_normal) ( idx: [int](class_int.md#class_int), normal: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [set_vertex_tangent](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_tangent) ( idx: [int](class_int.md#class_int), tangent: [Plane](class_plane.md#class_Plane) ) |
| void | [set_vertex_uv](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_uv) ( idx: [int](class_int.md#class_int), uv: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_vertex_uv2](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_uv2) ( idx: [int](class_int.md#class_int), uv2: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_vertex_weights](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_weights) ( idx: [int](class_int.md#class_int), weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |

---

### Method Descriptions

<span id="class_MeshDataTool_method_clear"></span>

void **clear** ( ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_clear)

Clears all data currently in MeshDataTool.

---

<span id="class_MeshDataTool_method_commit_to_surface"></span>

Error **commit_to_surface** ( mesh: [ArrayMesh](class_arraymesh.md#class_ArrayMesh), compression_flags: [int](class_int.md#class_int) = 0 ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_commit_to_surface)

Adds a new surface to specified [Mesh](class_mesh.md#class_Mesh) with edited data.

---

<span id="class_MeshDataTool_method_create_from_surface"></span>

Error **create_from_surface** ( mesh: [ArrayMesh](class_arraymesh.md#class_ArrayMesh), surface: [int](class_int.md#class_int) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_create_from_surface)

Uses specified surface of given [Mesh](class_mesh.md#class_Mesh) to populate data for MeshDataTool.

Requires [Mesh](class_mesh.md#class_Mesh) with primitive type [Mesh.PRIMITIVE_TRIANGLES](class_mesh.md#class_Mesh_constant_PRIMITIVE_TRIANGLES).

---

<span id="class_MeshDataTool_method_get_edge_count"></span>

[int](class_int.md#class_int) **get_edge_count** ( ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_edge_count)

Returns the number of edges in this [Mesh](class_mesh.md#class_Mesh).

---

<span id="class_MeshDataTool_method_get_edge_faces"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_edge_faces** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_edge_faces)

Returns array of faces that touch given edge.

---

<span id="class_MeshDataTool_method_get_edge_meta"></span>

[Variant](class_variant.md#class_Variant) **get_edge_meta** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_edge_meta)

Returns meta information assigned to given edge.

---

<span id="class_MeshDataTool_method_get_edge_vertex"></span>

[int](class_int.md#class_int) **get_edge_vertex** ( idx: [int](class_int.md#class_int), vertex: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_edge_vertex)

Returns the index of the specified `vertex` connected to the edge at index `idx`.

 `vertex` can only be `0` or `1`, as edges are composed of two vertices.

---

<span id="class_MeshDataTool_method_get_face_count"></span>

[int](class_int.md#class_int) **get_face_count** ( ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_face_count)

Returns the number of faces in this [Mesh](class_mesh.md#class_Mesh).

---

<span id="class_MeshDataTool_method_get_face_edge"></span>

[int](class_int.md#class_int) **get_face_edge** ( idx: [int](class_int.md#class_int), edge: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_face_edge)

Returns the edge associated with the face at index `idx`.

 `edge` argument must be either `0`, `1`, or `2` because a face only has three edges.

---

<span id="class_MeshDataTool_method_get_face_meta"></span>

[Variant](class_variant.md#class_Variant) **get_face_meta** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_face_meta)

Returns the metadata associated with the given face.

---

<span id="class_MeshDataTool_method_get_face_normal"></span>

[Vector3](class_vector3.md#class_Vector3) **get_face_normal** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_face_normal)

Calculates and returns the face normal of the given face.

---

<span id="class_MeshDataTool_method_get_face_vertex"></span>

[int](class_int.md#class_int) **get_face_vertex** ( idx: [int](class_int.md#class_int), vertex: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_face_vertex)

Returns the specified vertex index of the given face.

 `vertex` must be either `0`, `1`, or `2` because faces contain three vertices.

.. tabs::

```
```

    var index = mesh_data_tool.get_face_vertex(0, 1) # Gets the index of the second vertex of the first face.
    var position = mesh_data_tool.get_vertex(index)
    var normal = mesh_data_tool.get_vertex_normal(index)

```
```

    int index = meshDataTool.GetFaceVertex(0, 1); // Gets the index of the second vertex of the first face.
    Vector3 position = meshDataTool.GetVertex(index);
    Vector3 normal = meshDataTool.GetVertexNormal(index);

---

<span id="class_MeshDataTool_method_get_format"></span>

[int](class_int.md#class_int) **get_format** ( ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_format)

Returns the [Mesh](class_mesh.md#class_Mesh)'s format as a combination of the [ArrayFormat](class_mesh.md#enum_Mesh_ArrayFormat) flags. For example, a mesh containing both vertices and normals would return a format of `3` because [Mesh.ARRAY_FORMAT_VERTEX](class_mesh.md#class_Mesh_constant_ARRAY_FORMAT_VERTEX) is `1` and [Mesh.ARRAY_FORMAT_NORMAL](class_mesh.md#class_Mesh_constant_ARRAY_FORMAT_NORMAL) is `2`.

---

<span id="class_MeshDataTool_method_get_material"></span>

[Material](class_material.md#class_Material) **get_material** ( ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_material)

Returns the material assigned to the [Mesh](class_mesh.md#class_Mesh).

---

<span id="class_MeshDataTool_method_get_vertex"></span>

[Vector3](class_vector3.md#class_Vector3) **get_vertex** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex)

Returns the position of the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_bones"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_vertex_bones** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_bones)

Returns the bones of the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_color"></span>

[Color](class_color.md#class_Color) **get_vertex_color** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_color)

Returns the color of the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_count"></span>

[int](class_int.md#class_int) **get_vertex_count** ( ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_count)

Returns the total number of vertices in [Mesh](class_mesh.md#class_Mesh).

---

<span id="class_MeshDataTool_method_get_vertex_edges"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_vertex_edges** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_edges)

Returns an array of edges that share the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_faces"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_vertex_faces** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_faces)

Returns an array of faces that share the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_meta"></span>

[Variant](class_variant.md#class_Variant) **get_vertex_meta** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_meta)

Returns the metadata associated with the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_normal"></span>

[Vector3](class_vector3.md#class_Vector3) **get_vertex_normal** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_normal)

Returns the normal of the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_tangent"></span>

[Plane](class_plane.md#class_Plane) **get_vertex_tangent** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_tangent)

Returns the tangent of the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_uv"></span>

[Vector2](class_vector2.md#class_Vector2) **get_vertex_uv** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_uv)

Returns the UV of the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_uv2"></span>

[Vector2](class_vector2.md#class_Vector2) **get_vertex_uv2** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_uv2)

Returns the UV2 of the given vertex.

---

<span id="class_MeshDataTool_method_get_vertex_weights"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **get_vertex_weights** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshdatatool.md#class_MeshDataTool_method_get_vertex_weights)

Returns bone weights of the given vertex.

---

<span id="class_MeshDataTool_method_set_edge_meta"></span>

void **set_edge_meta** ( idx: [int](class_int.md#class_int), meta: [Variant](class_variant.md#class_Variant) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_edge_meta)

Sets the metadata of the given edge.

---

<span id="class_MeshDataTool_method_set_face_meta"></span>

void **set_face_meta** ( idx: [int](class_int.md#class_int), meta: [Variant](class_variant.md#class_Variant) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_face_meta)

Sets the metadata of the given face.

---

<span id="class_MeshDataTool_method_set_material"></span>

void **set_material** ( material: [Material](class_material.md#class_Material) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_material)

Sets the material to be used by newly-constructed [Mesh](class_mesh.md#class_Mesh).

---

<span id="class_MeshDataTool_method_set_vertex"></span>

void **set_vertex** ( idx: [int](class_int.md#class_int), vertex: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_vertex)

Sets the position of the given vertex.

---

<span id="class_MeshDataTool_method_set_vertex_bones"></span>

void **set_vertex_bones** ( idx: [int](class_int.md#class_int), bones: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_bones)

Sets the bones of the given vertex.

---

<span id="class_MeshDataTool_method_set_vertex_color"></span>

void **set_vertex_color** ( idx: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_color)

Sets the color of the given vertex.

---

<span id="class_MeshDataTool_method_set_vertex_meta"></span>

void **set_vertex_meta** ( idx: [int](class_int.md#class_int), meta: [Variant](class_variant.md#class_Variant) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_meta)

Sets the metadata associated with the given vertex.

---

<span id="class_MeshDataTool_method_set_vertex_normal"></span>

void **set_vertex_normal** ( idx: [int](class_int.md#class_int), normal: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_normal)

Sets the normal of the given vertex.

---

<span id="class_MeshDataTool_method_set_vertex_tangent"></span>

void **set_vertex_tangent** ( idx: [int](class_int.md#class_int), tangent: [Plane](class_plane.md#class_Plane) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_tangent)

Sets the tangent of the given vertex.

 **Note:** Even though `tangent` is a [Plane](class_plane.md#class_Plane), it does not directly represent the tangent plane. Its [Plane.x](class_plane.md#class_Plane_property_x), [Plane.y](class_plane.md#class_Plane_property_y), and [Plane.z](class_plane.md#class_Plane_property_z) represent the tangent vector and [Plane.d](class_plane.md#class_Plane_property_d) should be either `-1` or `1`. See also [Mesh.ARRAY_TANGENT](class_mesh.md#class_Mesh_constant_ARRAY_TANGENT).

---

<span id="class_MeshDataTool_method_set_vertex_uv"></span>

void **set_vertex_uv** ( idx: [int](class_int.md#class_int), uv: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_uv)

Sets the UV of the given vertex.

---

<span id="class_MeshDataTool_method_set_vertex_uv2"></span>

void **set_vertex_uv2** ( idx: [int](class_int.md#class_int), uv2: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_uv2)

Sets the UV2 of the given vertex.

---

<span id="class_MeshDataTool_method_set_vertex_weights"></span>

void **set_vertex_weights** ( idx: [int](class_int.md#class_int), weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_meshdatatool.md#class_MeshDataTool_method_set_vertex_weights)

Sets the bone weights of the given vertex.
