<span id="class_MeshConvexDecompositionSettings"></span>

## MeshConvexDecompositionSettings

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Parameters to be used with a [Mesh](class_mesh.md#class_Mesh) convex decomposition operation.

### Description

Parameters to be used with a [Mesh](class_mesh.md#class_Mesh) convex decomposition operation.

### Properties


| [bool](class_bool.md#class_bool) | [convex_hull_approximation](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_convex_hull_approximation) | `true` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [convex_hull_downsampling](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_convex_hull_downsampling) | `4` |
| [float](class_float.md#class_float) | [max_concavity](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_max_concavity) | `1.0` |
| [int](class_int.md#class_int) | [max_convex_hulls](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_max_convex_hulls) | `1` |
| [int](class_int.md#class_int) | [max_num_vertices_per_convex_hull](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_max_num_vertices_per_convex_hull) | `32` |
| [float](class_float.md#class_float) | [min_volume_per_convex_hull](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_min_volume_per_convex_hull) | `0.0001` |
| [Mode](class_meshconvexdecompositionsettings.md#enum_MeshConvexDecompositionSettings_Mode) | [mode](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_mode) | `0` |
| [bool](class_bool.md#class_bool) | [normalize_mesh](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_normalize_mesh) | `false` |
| [int](class_int.md#class_int) | [plane_downsampling](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_plane_downsampling) | `4` |
| [bool](class_bool.md#class_bool) | [project_hull_vertices](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_project_hull_vertices) | `true` |
| [int](class_int.md#class_int) | [resolution](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_resolution) | `10000` |
| [float](class_float.md#class_float) | [revolution_axes_clipping_bias](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_revolution_axes_clipping_bias) | `0.05` |
| [float](class_float.md#class_float) | [symmetry_planes_clipping_bias](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_symmetry_planes_clipping_bias) | `0.05` |

---

### Enumerations

<span id="enum_MeshConvexDecompositionSettings_Mode"></span>

enum **Mode**: [🔗](class_meshconvexdecompositionsettings.md#enum_MeshConvexDecompositionSettings_Mode)

<span id="class_MeshConvexDecompositionSettings_constant_CONVEX_DECOMPOSITION_MODE_VOXEL"></span>

[Mode](class_meshconvexdecompositionsettings.md#enum_MeshConvexDecompositionSettings_Mode) **CONVEX_DECOMPOSITION_MODE_VOXEL** = `0`

Constant for voxel-based approximate convex decomposition.

<span id="class_MeshConvexDecompositionSettings_constant_CONVEX_DECOMPOSITION_MODE_TETRAHEDRON"></span>

[Mode](class_meshconvexdecompositionsettings.md#enum_MeshConvexDecompositionSettings_Mode) **CONVEX_DECOMPOSITION_MODE_TETRAHEDRON** = `1`

Constant for tetrahedron-based approximate convex decomposition.

---

### Property Descriptions

<span id="class_MeshConvexDecompositionSettings_property_convex_hull_approximation"></span>

[bool](class_bool.md#class_bool) **convex_hull_approximation** = `true` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_convex_hull_approximation)

- void **set_convex_hull_approximation** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_convex_hull_approximation** ( )

If `true`, uses approximation for computing convex hulls.

---

<span id="class_MeshConvexDecompositionSettings_property_convex_hull_downsampling"></span>

[int](class_int.md#class_int) **convex_hull_downsampling** = `4` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_convex_hull_downsampling)

- void **set_convex_hull_downsampling** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_convex_hull_downsampling** ( )

Controls the precision of the convex-hull generation process during the clipping plane selection stage. Ranges from `1` to `16`.

---

<span id="class_MeshConvexDecompositionSettings_property_max_concavity"></span>

[float](class_float.md#class_float) **max_concavity** = `1.0` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_max_concavity)

- void **set_max_concavity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max_concavity** ( )

Maximum concavity. Ranges from `0.0` to `1.0`.

---

<span id="class_MeshConvexDecompositionSettings_property_max_convex_hulls"></span>

[int](class_int.md#class_int) **max_convex_hulls** = `1` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_max_convex_hulls)

- void **set_max_convex_hulls** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_convex_hulls** ( )

The maximum number of convex hulls to produce from the merge operation.

---

<span id="class_MeshConvexDecompositionSettings_property_max_num_vertices_per_convex_hull"></span>

[int](class_int.md#class_int) **max_num_vertices_per_convex_hull** = `32` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_max_num_vertices_per_convex_hull)

- void **set_max_num_vertices_per_convex_hull** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_num_vertices_per_convex_hull** ( )

Controls the maximum number of triangles per convex-hull. Ranges from `4` to `1024`.

---

<span id="class_MeshConvexDecompositionSettings_property_min_volume_per_convex_hull"></span>

[float](class_float.md#class_float) **min_volume_per_convex_hull** = `0.0001` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_min_volume_per_convex_hull)

- void **set_min_volume_per_convex_hull** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_min_volume_per_convex_hull** ( )

Controls the adaptive sampling of the generated convex-hulls. Ranges from `0.0` to `0.01`.

---

<span id="class_MeshConvexDecompositionSettings_property_mode"></span>

[Mode](class_meshconvexdecompositionsettings.md#enum_MeshConvexDecompositionSettings_Mode) **mode** = `0` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_mode)

- void **set_mode** ( value: [Mode](class_meshconvexdecompositionsettings.md#enum_MeshConvexDecompositionSettings_Mode) )
- [Mode](class_meshconvexdecompositionsettings.md#enum_MeshConvexDecompositionSettings_Mode) **get_mode** ( )

Mode for the approximate convex decomposition.

---

<span id="class_MeshConvexDecompositionSettings_property_normalize_mesh"></span>

[bool](class_bool.md#class_bool) **normalize_mesh** = `false` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_normalize_mesh)

- void **set_normalize_mesh** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_normalize_mesh** ( )

If `true`, normalizes the mesh before applying the convex decomposition.

---

<span id="class_MeshConvexDecompositionSettings_property_plane_downsampling"></span>

[int](class_int.md#class_int) **plane_downsampling** = `4` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_plane_downsampling)

- void **set_plane_downsampling** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_plane_downsampling** ( )

Controls the granularity of the search for the "best" clipping plane. Ranges from `1` to `16`.

---

<span id="class_MeshConvexDecompositionSettings_property_project_hull_vertices"></span>

[bool](class_bool.md#class_bool) **project_hull_vertices** = `true` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_project_hull_vertices)

- void **set_project_hull_vertices** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_project_hull_vertices** ( )

If `true`, projects output convex hull vertices onto the original source mesh to increase floating-point accuracy of the results.

---

<span id="class_MeshConvexDecompositionSettings_property_resolution"></span>

[int](class_int.md#class_int) **resolution** = `10000` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_resolution)

- void **set_resolution** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_resolution** ( )

Maximum number of voxels generated during the voxelization stage.

---

<span id="class_MeshConvexDecompositionSettings_property_revolution_axes_clipping_bias"></span>

[float](class_float.md#class_float) **revolution_axes_clipping_bias** = `0.05` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_revolution_axes_clipping_bias)

- void **set_revolution_axes_clipping_bias** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_revolution_axes_clipping_bias** ( )

Controls the bias toward clipping along revolution axes. Ranges from `0.0` to `1.0`.

---

<span id="class_MeshConvexDecompositionSettings_property_symmetry_planes_clipping_bias"></span>

[float](class_float.md#class_float) **symmetry_planes_clipping_bias** = `0.05` [🔗](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings_property_symmetry_planes_clipping_bias)

- void **set_symmetry_planes_clipping_bias** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_symmetry_planes_clipping_bias** ( )

Controls the bias toward clipping along symmetry planes. Ranges from `0.0` to `1.0`.
