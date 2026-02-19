<span id="class_VoxelGI"></span>

## VoxelGI

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Real-time global illumination (GI) probe.

### Description

**VoxelGI** s are used to provide high-quality real-time indirect light and reflections to scenes. They precompute the effect of objects that emit light and the effect of static geometry to simulate the behavior of complex light in real-time. **VoxelGI** s need to be baked before having a visible effect. However, once baked, dynamic objects will receive light from them. Furthermore, lights can be fully dynamic or baked.

 **Note:** **VoxelGI** is only supported in the Forward+ rendering method, not Mobile or Compatibility.

 **Procedural generation:** **VoxelGI** can be baked in an exported project, which makes it suitable for procedurally generated or user-built levels as long as all the geometry is generated in advance. For games where geometry is generated at any time during gameplay, SDFGI is more suitable (see [Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled)).

 **Performance:** **VoxelGI** is relatively demanding on the GPU and is not suited to low-end hardware such as integrated graphics (consider [LightmapGI](class_lightmapgi.md#class_LightmapGI) instead). To improve performance, adjust ProjectSettings.rendering/global_illumination/voxel_gi/quality and enable ProjectSettings.rendering/global_illumination/gi/use_half_resolution in the Project Settings. To provide a fallback for low-end hardware, consider adding an option to disable **VoxelGI** in your project's options menus. A **VoxelGI** node can be disabled by hiding it.

 **Note:** Meshes should have sufficiently thick walls to avoid light leaks (avoid one-sided walls). For interior levels, enclose your level geometry in a sufficiently large box and bridge the loops to close the mesh. To further prevent light leaks, you can also strategically place temporary [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) nodes with their [GeometryInstance3D.gi_mode](class_geometryinstance3d.md#class_GeometryInstance3D_property_gi_mode) set to [GeometryInstance3D.GI_MODE_STATIC](class_geometryinstance3d.md#class_GeometryInstance3D_constant_GI_MODE_STATIC). These temporary nodes can then be hidden after baking the **VoxelGI** node.

### Tutorials

- [Using Voxel global illumination](../tutorials/3d/global_illumination/using_voxel_gi.md)

- Third Person Shooter (TPS) Demo

### Properties


| [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) | [camera_attributes](class_voxelgi.md#class_VoxelGI_property_camera_attributes) |
| --- | --- |
| [VoxelGIData](class_voxelgidata.md#class_VoxelGIData) | [data](class_voxelgi.md#class_VoxelGI_property_data) |
| [Vector3](class_vector3.md#class_Vector3) | [size](class_voxelgi.md#class_VoxelGI_property_size) | `Vector3(20, 20, 20)` |
| [Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) | [subdiv](class_voxelgi.md#class_VoxelGI_property_subdiv) | `1` |

### Methods


| void | [bake](class_voxelgi.md#class_VoxelGI_method_bake) ( from_node: [Node](class_node.md#class_Node) = null, create_visual_debug: [bool](class_bool.md#class_bool) = false ) |
| --- | --- |
| void | [debug_bake](class_voxelgi.md#class_VoxelGI_method_debug_bake) ( ) |

---

### Enumerations

<span id="enum_VoxelGI_Subdiv"></span>

enum **Subdiv**: [🔗](class_voxelgi.md#enum_VoxelGI_Subdiv)

<span id="class_VoxelGI_constant_SUBDIV_64"></span>

[Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) **SUBDIV_64** = `0`

Use 64 subdivisions. This is the lowest quality setting, but the fastest. Use it if you can, but especially use it on lower-end hardware.

<span id="class_VoxelGI_constant_SUBDIV_128"></span>

[Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) **SUBDIV_128** = `1`

Use 128 subdivisions. This is the default quality setting.

<span id="class_VoxelGI_constant_SUBDIV_256"></span>

[Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) **SUBDIV_256** = `2`

Use 256 subdivisions.

<span id="class_VoxelGI_constant_SUBDIV_512"></span>

[Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) **SUBDIV_512** = `3`

Use 512 subdivisions. This is the highest quality setting, but the slowest. On lower-end hardware, this could cause the GPU to stall.

<span id="class_VoxelGI_constant_SUBDIV_MAX"></span>

[Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) **SUBDIV_MAX** = `4`

Represents the size of the [Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) enum.

---

### Property Descriptions

<span id="class_VoxelGI_property_camera_attributes"></span>

[CameraAttributes](class_cameraattributes.md#class_CameraAttributes) **camera_attributes** [🔗](class_voxelgi.md#class_VoxelGI_property_camera_attributes)

- void **set_camera_attributes** ( value: [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) )
- [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) **get_camera_attributes** ( )

The [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) resource that specifies exposure levels to bake at. Auto-exposure and non exposure properties will be ignored. Exposure settings should be used to reduce the dynamic range present when baking. If exposure is too high, the **VoxelGI** will have banding artifacts or may have over-exposure artifacts.

---

<span id="class_VoxelGI_property_data"></span>

[VoxelGIData](class_voxelgidata.md#class_VoxelGIData) **data** [🔗](class_voxelgi.md#class_VoxelGI_property_data)

- void **set_probe_data** ( value: [VoxelGIData](class_voxelgidata.md#class_VoxelGIData) )
- [VoxelGIData](class_voxelgidata.md#class_VoxelGIData) **get_probe_data** ( )

The [VoxelGIData](class_voxelgidata.md#class_VoxelGIData) resource that holds the data for this **VoxelGI**.

---

<span id="class_VoxelGI_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(20, 20, 20)` [🔗](class_voxelgi.md#class_VoxelGI_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The size of the area covered by the **VoxelGI**. This must be `1.0` or greater on each axis.

 **Note:** If you make the size larger without increasing the number of subdivisions with [subdiv](class_voxelgi.md#class_VoxelGI_property_subdiv), the size of each cell will increase and result in less detailed lighting.

---

<span id="class_VoxelGI_property_subdiv"></span>

[Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) **subdiv** = `1` [🔗](class_voxelgi.md#class_VoxelGI_property_subdiv)

- void **set_subdiv** ( value: [Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) )
- [Subdiv](class_voxelgi.md#enum_VoxelGI_Subdiv) **get_subdiv** ( )

Number of times to subdivide the grid that the **VoxelGI** operates on. A higher number results in finer detail and thus higher visual quality, while lower numbers result in better performance.

---

### Method Descriptions

<span id="class_VoxelGI_method_bake"></span>

void **bake** ( from_node: [Node](class_node.md#class_Node) = null, create_visual_debug: [bool](class_bool.md#class_bool) = false ) [🔗](class_voxelgi.md#class_VoxelGI_method_bake)

Bakes the effect from all [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) s marked with [GeometryInstance3D.GI_MODE_STATIC](class_geometryinstance3d.md#class_GeometryInstance3D_constant_GI_MODE_STATIC) and [Light3D](class_light3d.md#class_Light3D) s marked with either [Light3D.BAKE_STATIC](class_light3d.md#class_Light3D_constant_BAKE_STATIC) or [Light3D.BAKE_DYNAMIC](class_light3d.md#class_Light3D_constant_BAKE_DYNAMIC). If `create_visual_debug` is `true`, after baking the light, this will generate a [MultiMesh](class_multimesh.md#class_MultiMesh) that has a cube representing each solid cell with each cube colored to the cell's albedo color. This can be used to visualize the **VoxelGI**'s data and debug any issues that may be occurring.

 **Note:** [bake()](class_voxelgi.md#class_VoxelGI_method_bake) works from the editor and in exported projects. This makes it suitable for procedurally generated or user-built levels. Baking a **VoxelGI** node generally takes from 5 to 20 seconds in most scenes. Reducing [subdiv](class_voxelgi.md#class_VoxelGI_property_subdiv) can speed up baking.

 **Note:** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) s and [Light3D](class_light3d.md#class_Light3D) s must be fully ready before [bake()](class_voxelgi.md#class_VoxelGI_method_bake) is called. If you are procedurally creating those and some meshes or lights are missing from your baked **VoxelGI**, use `call_deferred("bake")` instead of calling [bake()](class_voxelgi.md#class_VoxelGI_method_bake) directly.

---

<span id="class_VoxelGI_method_debug_bake"></span>

void **debug_bake** ( ) [🔗](class_voxelgi.md#class_VoxelGI_method_debug_bake)

Calls [bake()](class_voxelgi.md#class_VoxelGI_method_bake) with `create_visual_debug` enabled.
