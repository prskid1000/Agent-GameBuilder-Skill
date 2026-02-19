<span id="class_NavigationMeshSourceGeometryData3D"></span>

## NavigationMeshSourceGeometryData3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Container for parsed source geometry data used in navigation mesh baking.

### Description

Container for parsed source geometry data used in navigation mesh baking.

### Methods


| void | [add_faces](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_add_faces) ( faces: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), xform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| --- | --- |
| void | [add_mesh](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_add_mesh) ( mesh: [Mesh](class_mesh.md#class_Mesh), xform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [add_mesh_array](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_add_mesh_array) ( mesh_array: [Array](class_array.md#class_Array), xform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [add_projected_obstruction](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_add_projected_obstruction) ( vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), elevation: [float](class_float.md#class_float), height: [float](class_float.md#class_float), carve: [bool](class_bool.md#class_bool) ) |
| void | [append_arrays](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_append_arrays) ( vertices: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| void | [clear](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_clear) ( ) |
| void | [clear_projected_obstructions](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_clear_projected_obstructions) ( ) |
| [AABB](class_aabb.md#class_AABB) | [get_bounds](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_get_bounds) ( ) |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_indices](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_get_indices) ( ) const |
| [Array](class_array.md#class_Array) | [get_projected_obstructions](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_get_projected_obstructions) ( ) const |
| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [get_vertices](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_get_vertices) ( ) const |
| [bool](class_bool.md#class_bool) | [has_data](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_has_data) ( ) |
| void | [merge](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_merge) ( other_geometry: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D) ) |
| void | [set_indices](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_set_indices) ( indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| void | [set_projected_obstructions](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_set_projected_obstructions) ( projected_obstructions: [Array](class_array.md#class_Array) ) |
| void | [set_vertices](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_set_vertices) ( vertices: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |

---

### Method Descriptions

<span id="class_NavigationMeshSourceGeometryData3D_method_add_faces"></span>

void **add_faces** ( faces: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), xform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_add_faces)

Adds an array of vertex positions to the geometry data for navigation mesh baking to form triangulated faces. For each face the array must have three vertex positions in clockwise winding order. Since [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_add_mesh"></span>

void **add_mesh** ( mesh: [Mesh](class_mesh.md#class_Mesh), xform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_add_mesh)

Adds the geometry data of a [Mesh](class_mesh.md#class_Mesh) resource to the navigation mesh baking data. The mesh must have valid triangulated mesh data to be considered. Since [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_add_mesh_array"></span>

void **add_mesh_array** ( mesh_array: [Array](class_array.md#class_Array), xform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_add_mesh_array)

Adds an [Array](class_array.md#class_Array) the size of [Mesh.ARRAY_MAX](class_mesh.md#class_Mesh_constant_ARRAY_MAX) and with vertices at index [Mesh.ARRAY_VERTEX](class_mesh.md#class_Mesh_constant_ARRAY_VERTEX) and indices at index [Mesh.ARRAY_INDEX](class_mesh.md#class_Mesh_constant_ARRAY_INDEX) to the navigation mesh baking data. The array must have valid triangulated mesh data to be considered. Since [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_add_projected_obstruction"></span>

void **add_projected_obstruction** ( vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), elevation: [float](class_float.md#class_float), height: [float](class_float.md#class_float), carve: [bool](class_bool.md#class_bool) ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_add_projected_obstruction)

Adds a projected obstruction shape to the source geometry. The `vertices` are considered projected on an xz-axes plane, placed at the global y-axis `elevation` and extruded by `height`. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_append_arrays"></span>

void **append_arrays** ( vertices: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_append_arrays)

Appends arrays of `vertices` and `indices` at the end of the existing arrays. Adds the existing index as an offset to the appended indices.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_clear"></span>

void **clear** ( ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_clear)

Clears the internal data.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_clear_projected_obstructions"></span>

void **clear_projected_obstructions** ( ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_clear_projected_obstructions)

Clears all projected obstructions.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_get_bounds"></span>

[AABB](class_aabb.md#class_AABB) **get_bounds** ( ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_get_bounds)

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_get_indices"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_indices** ( ) *const* [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_get_indices)

Returns the parsed source geometry data indices array.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_get_projected_obstructions"></span>

[Array](class_array.md#class_Array) **get_projected_obstructions** ( ) *const* [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_get_projected_obstructions)

Returns the projected obstructions as an [Array](class_array.md#class_Array) of dictionaries. Each [Dictionary](class_dictionary.md#class_Dictionary) contains the following entries:

- `vertices` - A [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) that defines the outline points of the projected shape.

- `elevation` - A [float](class_float.md#class_float) that defines the projected shape placement on the y-axis.

- `height` - A [float](class_float.md#class_float) that defines how much the projected shape is extruded along the y-axis.

- `carve` - A [bool](class_bool.md#class_bool) that defines how the obstacle affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_get_vertices"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **get_vertices** ( ) *const* [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_get_vertices)

Returns the parsed source geometry data vertices array.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_has_data"></span>

[bool](class_bool.md#class_bool) **has_data** ( ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_has_data)

Returns `true` when parsed source geometry data exists.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_merge"></span>

void **merge** ( other_geometry: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D) ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_merge)

Adds the geometry data of another **NavigationMeshSourceGeometryData3D** to the navigation mesh baking data.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_set_indices"></span>

void **set_indices** ( indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_set_indices)

Sets the parsed source geometry data indices. The indices need to be matched with appropriated vertices.

 **Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.

---

<span id="class_NavigationMeshSourceGeometryData3D_method_set_projected_obstructions"></span>

void **set_projected_obstructions** ( projected_obstructions: [Array](class_array.md#class_Array) ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_set_projected_obstructions)

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:

.. tabs::

```
```

    "vertices" : PackedFloat32Array
    "elevation" : float
    "height" : float
    "carve" : bool

---

<span id="class_NavigationMeshSourceGeometryData3D_method_set_vertices"></span>

void **set_vertices** ( vertices: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D_method_set_vertices)

Sets the parsed source geometry data vertices. The vertices need to be matched with appropriated indices.

 **Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.
