<span id="class_NavigationMesh"></span>

## NavigationMesh

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A navigation mesh that defines traversable areas and obstacles.

### Description

A navigation mesh is a collection of polygons that define which areas of an environment are traversable to aid agents in pathfinding through complicated spaces.

### Tutorials

- [Using NavigationMeshes](../tutorials/navigation/navigation_using_navigationmeshes.md)

- 3D Navigation Demo

### Properties


| [float](class_float.md#class_float) | [agent_height](class_navigationmesh.md#class_NavigationMesh_property_agent_height) | `1.5` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [agent_max_climb](class_navigationmesh.md#class_NavigationMesh_property_agent_max_climb) | `0.25` |
| [float](class_float.md#class_float) | [agent_max_slope](class_navigationmesh.md#class_NavigationMesh_property_agent_max_slope) | `45.0` |
| [float](class_float.md#class_float) | [agent_radius](class_navigationmesh.md#class_NavigationMesh_property_agent_radius) | `0.5` |
| [float](class_float.md#class_float) | [border_size](class_navigationmesh.md#class_NavigationMesh_property_border_size) | `0.0` |
| [float](class_float.md#class_float) | [cell_height](class_navigationmesh.md#class_NavigationMesh_property_cell_height) | `0.25` |
| [float](class_float.md#class_float) | [cell_size](class_navigationmesh.md#class_NavigationMesh_property_cell_size) | `0.25` |
| [float](class_float.md#class_float) | [detail_sample_distance](class_navigationmesh.md#class_NavigationMesh_property_detail_sample_distance) | `6.0` |
| [float](class_float.md#class_float) | [detail_sample_max_error](class_navigationmesh.md#class_NavigationMesh_property_detail_sample_max_error) | `1.0` |
| [float](class_float.md#class_float) | [edge_max_error](class_navigationmesh.md#class_NavigationMesh_property_edge_max_error) | `1.3` |
| [float](class_float.md#class_float) | [edge_max_length](class_navigationmesh.md#class_NavigationMesh_property_edge_max_length) | `0.0` |
| [AABB](class_aabb.md#class_AABB) | [filter_baking_aabb](class_navigationmesh.md#class_NavigationMesh_property_filter_baking_aabb) | `AABB(0, 0, 0, 0, 0, 0)` |
| [Vector3](class_vector3.md#class_Vector3) | [filter_baking_aabb_offset](class_navigationmesh.md#class_NavigationMesh_property_filter_baking_aabb_offset) | `Vector3(0, 0, 0)` |
| [bool](class_bool.md#class_bool) | [filter_ledge_spans](class_navigationmesh.md#class_NavigationMesh_property_filter_ledge_spans) | `false` |
| [bool](class_bool.md#class_bool) | [filter_low_hanging_obstacles](class_navigationmesh.md#class_NavigationMesh_property_filter_low_hanging_obstacles) | `false` |
| [bool](class_bool.md#class_bool) | [filter_walkable_low_height_spans](class_navigationmesh.md#class_NavigationMesh_property_filter_walkable_low_height_spans) | `false` |
| [int](class_int.md#class_int) | [geometry_collision_mask](class_navigationmesh.md#class_NavigationMesh_property_geometry_collision_mask) | `4294967295` |
| [ParsedGeometryType](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType) | [geometry_parsed_geometry_type](class_navigationmesh.md#class_NavigationMesh_property_geometry_parsed_geometry_type) | `2` |
| [SourceGeometryMode](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode) | [geometry_source_geometry_mode](class_navigationmesh.md#class_NavigationMesh_property_geometry_source_geometry_mode) | `0` |
| [StringName](class_stringname.md#class_StringName) | [geometry_source_group_name](class_navigationmesh.md#class_NavigationMesh_property_geometry_source_group_name) | `&"navigation_mesh_source_group"` |
| [float](class_float.md#class_float) | [region_merge_size](class_navigationmesh.md#class_NavigationMesh_property_region_merge_size) | `20.0` |
| [float](class_float.md#class_float) | [region_min_size](class_navigationmesh.md#class_NavigationMesh_property_region_min_size) | `2.0` |
| [SamplePartitionType](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType) | [sample_partition_type](class_navigationmesh.md#class_NavigationMesh_property_sample_partition_type) | `0` |
| [float](class_float.md#class_float) | [vertices_per_polygon](class_navigationmesh.md#class_NavigationMesh_property_vertices_per_polygon) | `6.0` |

### Methods


| void | [add_polygon](class_navigationmesh.md#class_NavigationMesh_method_add_polygon) ( polygon: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| --- | --- |
| void | [clear](class_navigationmesh.md#class_NavigationMesh_method_clear) ( ) |
| void | [clear_polygons](class_navigationmesh.md#class_NavigationMesh_method_clear_polygons) ( ) |
| void | [create_from_mesh](class_navigationmesh.md#class_NavigationMesh_method_create_from_mesh) ( mesh: [Mesh](class_mesh.md#class_Mesh) ) |
| [bool](class_bool.md#class_bool) | [get_collision_mask_value](class_navigationmesh.md#class_NavigationMesh_method_get_collision_mask_value) ( layer_number: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_polygon](class_navigationmesh.md#class_NavigationMesh_method_get_polygon) ( idx: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_polygon_count](class_navigationmesh.md#class_NavigationMesh_method_get_polygon_count) ( ) const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [get_vertices](class_navigationmesh.md#class_NavigationMesh_method_get_vertices) ( ) const |
| void | [set_collision_mask_value](class_navigationmesh.md#class_NavigationMesh_method_set_collision_mask_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |
| void | [set_vertices](class_navigationmesh.md#class_NavigationMesh_method_set_vertices) ( vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) |

---

### Enumerations

<span id="enum_NavigationMesh_SamplePartitionType"></span>

enum **SamplePartitionType**: [🔗](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType)

<span id="class_NavigationMesh_constant_SAMPLE_PARTITION_WATERSHED"></span>

[SamplePartitionType](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType) **SAMPLE_PARTITION_WATERSHED** = `0`

Watershed partitioning. Generally the best choice if you precompute the navigation mesh, use this if you have large open areas.

<span id="class_NavigationMesh_constant_SAMPLE_PARTITION_MONOTONE"></span>

[SamplePartitionType](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType) **SAMPLE_PARTITION_MONOTONE** = `1`

Monotone partitioning. Use this if you want fast navigation mesh generation.

<span id="class_NavigationMesh_constant_SAMPLE_PARTITION_LAYERS"></span>

[SamplePartitionType](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType) **SAMPLE_PARTITION_LAYERS** = `2`

Layer partitioning. Good choice to use for tiled navigation mesh with medium and small sized tiles.

<span id="class_NavigationMesh_constant_SAMPLE_PARTITION_MAX"></span>

[SamplePartitionType](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType) **SAMPLE_PARTITION_MAX** = `3`

Represents the size of the [SamplePartitionType](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType) enum.

---

<span id="enum_NavigationMesh_ParsedGeometryType"></span>

enum **ParsedGeometryType**: [🔗](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType)

<span id="class_NavigationMesh_constant_PARSED_GEOMETRY_MESH_INSTANCES"></span>

[ParsedGeometryType](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType) **PARSED_GEOMETRY_MESH_INSTANCES** = `0`

Parses mesh instances as geometry. This includes [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D), [CSGShape3D](class_csgshape3d.md#class_CSGShape3D), and [GridMap](class_gridmap.md#class_GridMap) nodes.

<span id="class_NavigationMesh_constant_PARSED_GEOMETRY_STATIC_COLLIDERS"></span>

[ParsedGeometryType](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType) **PARSED_GEOMETRY_STATIC_COLLIDERS** = `1`

Parses [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) colliders as geometry. The collider should be in any of the layers specified by [geometry_collision_mask](class_navigationmesh.md#class_NavigationMesh_property_geometry_collision_mask).

<span id="class_NavigationMesh_constant_PARSED_GEOMETRY_BOTH"></span>

[ParsedGeometryType](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType) **PARSED_GEOMETRY_BOTH** = `2`

Both [PARSED_GEOMETRY_MESH_INSTANCES](class_navigationmesh.md#class_NavigationMesh_constant_PARSED_GEOMETRY_MESH_INSTANCES) and [PARSED_GEOMETRY_STATIC_COLLIDERS](class_navigationmesh.md#class_NavigationMesh_constant_PARSED_GEOMETRY_STATIC_COLLIDERS).

<span id="class_NavigationMesh_constant_PARSED_GEOMETRY_MAX"></span>

[ParsedGeometryType](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType) **PARSED_GEOMETRY_MAX** = `3`

Represents the size of the [ParsedGeometryType](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType) enum.

---

<span id="enum_NavigationMesh_SourceGeometryMode"></span>

enum **SourceGeometryMode**: [🔗](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode)

<span id="class_NavigationMesh_constant_SOURCE_GEOMETRY_ROOT_NODE_CHILDREN"></span>

[SourceGeometryMode](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode) **SOURCE_GEOMETRY_ROOT_NODE_CHILDREN** = `0`

Scans the child nodes of the root node recursively for geometry.

<span id="class_NavigationMesh_constant_SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN"></span>

[SourceGeometryMode](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode) **SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN** = `1`

Scans nodes in a group and their child nodes recursively for geometry. The group is specified by [geometry_source_group_name](class_navigationmesh.md#class_NavigationMesh_property_geometry_source_group_name).

<span id="class_NavigationMesh_constant_SOURCE_GEOMETRY_GROUPS_EXPLICIT"></span>

[SourceGeometryMode](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode) **SOURCE_GEOMETRY_GROUPS_EXPLICIT** = `2`

Uses nodes in a group for geometry. The group is specified by [geometry_source_group_name](class_navigationmesh.md#class_NavigationMesh_property_geometry_source_group_name).

<span id="class_NavigationMesh_constant_SOURCE_GEOMETRY_MAX"></span>

[SourceGeometryMode](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode) **SOURCE_GEOMETRY_MAX** = `3`

Represents the size of the [SourceGeometryMode](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode) enum.

---

### Property Descriptions

<span id="class_NavigationMesh_property_agent_height"></span>

[float](class_float.md#class_float) **agent_height** = `1.5` [🔗](class_navigationmesh.md#class_NavigationMesh_property_agent_height)

- void **set_agent_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_agent_height** ( )

The minimum floor to ceiling height that will still allow the floor area to be considered walkable.

 **Note:** While baking, this value will be rounded up to the nearest multiple of [cell_height](class_navigationmesh.md#class_NavigationMesh_property_cell_height).

---

<span id="class_NavigationMesh_property_agent_max_climb"></span>

[float](class_float.md#class_float) **agent_max_climb** = `0.25` [🔗](class_navigationmesh.md#class_NavigationMesh_property_agent_max_climb)

- void **set_agent_max_climb** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_agent_max_climb** ( )

The minimum ledge height that is considered to still be traversable.

 **Note:** While baking, this value will be rounded down to the nearest multiple of [cell_height](class_navigationmesh.md#class_NavigationMesh_property_cell_height).

---

<span id="class_NavigationMesh_property_agent_max_slope"></span>

[float](class_float.md#class_float) **agent_max_slope** = `45.0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_agent_max_slope)

- void **set_agent_max_slope** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_agent_max_slope** ( )

The maximum slope that is considered walkable, in degrees.

---

<span id="class_NavigationMesh_property_agent_radius"></span>

[float](class_float.md#class_float) **agent_radius** = `0.5` [🔗](class_navigationmesh.md#class_NavigationMesh_property_agent_radius)

- void **set_agent_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_agent_radius** ( )

The distance to erode/shrink the walkable area of the heightfield away from obstructions.

 **Note:** While baking, this value will be rounded up to the nearest multiple of [cell_size](class_navigationmesh.md#class_NavigationMesh_property_cell_size).

 **Note:** The radius must be equal or higher than `0.0`. If the radius is `0.0`, it won't be possible to fix invalid outline overlaps and other precision errors during the baking process. As a result, some obstacles may be excluded incorrectly from the final navigation mesh, or may delete the navigation mesh's polygons.

---

<span id="class_NavigationMesh_property_border_size"></span>

[float](class_float.md#class_float) **border_size** = `0.0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_border_size)

- void **set_border_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_border_size** ( )

The size of the non-navigable border around the bake bounding area.

In conjunction with the [filter_baking_aabb](class_navigationmesh.md#class_NavigationMesh_property_filter_baking_aabb) and a [edge_max_error](class_navigationmesh.md#class_NavigationMesh_property_edge_max_error) value at `1.0` or below the border size can be used to bake tile aligned navigation meshes without the tile edges being shrunk by [agent_radius](class_navigationmesh.md#class_NavigationMesh_property_agent_radius).

 **Note:** If this value is not `0.0`, it will be rounded up to the nearest multiple of [cell_size](class_navigationmesh.md#class_NavigationMesh_property_cell_size) during baking.

---

<span id="class_NavigationMesh_property_cell_height"></span>

[float](class_float.md#class_float) **cell_height** = `0.25` [🔗](class_navigationmesh.md#class_NavigationMesh_property_cell_height)

- void **set_cell_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_cell_height** ( )

The cell height used to rasterize the navigation mesh vertices on the Y axis. Must match with the cell height on the navigation map.

---

<span id="class_NavigationMesh_property_cell_size"></span>

[float](class_float.md#class_float) **cell_size** = `0.25` [🔗](class_navigationmesh.md#class_NavigationMesh_property_cell_size)

- void **set_cell_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_cell_size** ( )

The cell size used to rasterize the navigation mesh vertices on the XZ plane. Must match with the cell size on the navigation map.

---

<span id="class_NavigationMesh_property_detail_sample_distance"></span>

[float](class_float.md#class_float) **detail_sample_distance** = `6.0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_detail_sample_distance)

- void **set_detail_sample_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_detail_sample_distance** ( )

The sampling distance to use when generating the detail mesh, in cell unit.

---

<span id="class_NavigationMesh_property_detail_sample_max_error"></span>

[float](class_float.md#class_float) **detail_sample_max_error** = `1.0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_detail_sample_max_error)

- void **set_detail_sample_max_error** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_detail_sample_max_error** ( )

The maximum distance the detail mesh surface should deviate from heightfield, in cell unit.

---

<span id="class_NavigationMesh_property_edge_max_error"></span>

[float](class_float.md#class_float) **edge_max_error** = `1.3` [🔗](class_navigationmesh.md#class_NavigationMesh_property_edge_max_error)

- void **set_edge_max_error** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_edge_max_error** ( )

The maximum distance a simplified contour's border edges should deviate the original raw contour.

---

<span id="class_NavigationMesh_property_edge_max_length"></span>

[float](class_float.md#class_float) **edge_max_length** = `0.0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_edge_max_length)

- void **set_edge_max_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_edge_max_length** ( )

The maximum allowed length for contour edges along the border of the mesh. A value of `0.0` disables this feature.

 **Note:** While baking, this value will be rounded up to the nearest multiple of [cell_size](class_navigationmesh.md#class_NavigationMesh_property_cell_size).

---

<span id="class_NavigationMesh_property_filter_baking_aabb"></span>

[AABB](class_aabb.md#class_AABB) **filter_baking_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_navigationmesh.md#class_NavigationMesh_property_filter_baking_aabb)

- void **set_filter_baking_aabb** ( value: [AABB](class_aabb.md#class_AABB) )
- [AABB](class_aabb.md#class_AABB) **get_filter_baking_aabb** ( )

If the baking [AABB](class_aabb.md#class_AABB) has a volume the navigation mesh baking will be restricted to its enclosing area.

---

<span id="class_NavigationMesh_property_filter_baking_aabb_offset"></span>

[Vector3](class_vector3.md#class_Vector3) **filter_baking_aabb_offset** = `Vector3(0, 0, 0)` [🔗](class_navigationmesh.md#class_NavigationMesh_property_filter_baking_aabb_offset)

- void **set_filter_baking_aabb_offset** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_filter_baking_aabb_offset** ( )

The position offset applied to the [filter_baking_aabb](class_navigationmesh.md#class_NavigationMesh_property_filter_baking_aabb) [AABB](class_aabb.md#class_AABB).

---

<span id="class_NavigationMesh_property_filter_ledge_spans"></span>

[bool](class_bool.md#class_bool) **filter_ledge_spans** = `false` [🔗](class_navigationmesh.md#class_NavigationMesh_property_filter_ledge_spans)

- void **set_filter_ledge_spans** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_filter_ledge_spans** ( )

If `true`, marks spans that are ledges as non-walkable.

---

<span id="class_NavigationMesh_property_filter_low_hanging_obstacles"></span>

[bool](class_bool.md#class_bool) **filter_low_hanging_obstacles** = `false` [🔗](class_navigationmesh.md#class_NavigationMesh_property_filter_low_hanging_obstacles)

- void **set_filter_low_hanging_obstacles** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_filter_low_hanging_obstacles** ( )

If `true`, marks non-walkable spans as walkable if their maximum is within [agent_max_climb](class_navigationmesh.md#class_NavigationMesh_property_agent_max_climb) of a walkable neighbor.

---

<span id="class_NavigationMesh_property_filter_walkable_low_height_spans"></span>

[bool](class_bool.md#class_bool) **filter_walkable_low_height_spans** = `false` [🔗](class_navigationmesh.md#class_NavigationMesh_property_filter_walkable_low_height_spans)

- void **set_filter_walkable_low_height_spans** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_filter_walkable_low_height_spans** ( )

If `true`, marks walkable spans as not walkable if the clearance above the span is less than [agent_height](class_navigationmesh.md#class_NavigationMesh_property_agent_height).

---

<span id="class_NavigationMesh_property_geometry_collision_mask"></span>

[int](class_int.md#class_int) **geometry_collision_mask** = `4294967295` [🔗](class_navigationmesh.md#class_NavigationMesh_property_geometry_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The physics layers to scan for static colliders.

Only used when [geometry_parsed_geometry_type](class_navigationmesh.md#class_NavigationMesh_property_geometry_parsed_geometry_type) is [PARSED_GEOMETRY_STATIC_COLLIDERS](class_navigationmesh.md#class_NavigationMesh_constant_PARSED_GEOMETRY_STATIC_COLLIDERS) or [PARSED_GEOMETRY_BOTH](class_navigationmesh.md#class_NavigationMesh_constant_PARSED_GEOMETRY_BOTH).

---

<span id="class_NavigationMesh_property_geometry_parsed_geometry_type"></span>

[ParsedGeometryType](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType) **geometry_parsed_geometry_type** = `2` [🔗](class_navigationmesh.md#class_NavigationMesh_property_geometry_parsed_geometry_type)

- void **set_parsed_geometry_type** ( value: [ParsedGeometryType](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType) )
- [ParsedGeometryType](class_navigationmesh.md#enum_NavigationMesh_ParsedGeometryType) **get_parsed_geometry_type** ( )

Determines which type of nodes will be parsed as geometry.

---

<span id="class_NavigationMesh_property_geometry_source_geometry_mode"></span>

[SourceGeometryMode](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode) **geometry_source_geometry_mode** = `0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_geometry_source_geometry_mode)

- void **set_source_geometry_mode** ( value: [SourceGeometryMode](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode) )
- [SourceGeometryMode](class_navigationmesh.md#enum_NavigationMesh_SourceGeometryMode) **get_source_geometry_mode** ( )

The source of the geometry used when baking.

---

<span id="class_NavigationMesh_property_geometry_source_group_name"></span>

[StringName](class_stringname.md#class_StringName) **geometry_source_group_name** = `&"navigation_mesh_source_group"` [🔗](class_navigationmesh.md#class_NavigationMesh_property_geometry_source_group_name)

- void **set_source_group_name** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_source_group_name** ( )

The name of the group to scan for geometry.

Only used when [geometry_source_geometry_mode](class_navigationmesh.md#class_NavigationMesh_property_geometry_source_geometry_mode) is [SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN](class_navigationmesh.md#class_NavigationMesh_constant_SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN) or [SOURCE_GEOMETRY_GROUPS_EXPLICIT](class_navigationmesh.md#class_NavigationMesh_constant_SOURCE_GEOMETRY_GROUPS_EXPLICIT).

---

<span id="class_NavigationMesh_property_region_merge_size"></span>

[float](class_float.md#class_float) **region_merge_size** = `20.0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_region_merge_size)

- void **set_region_merge_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_region_merge_size** ( )

Any regions with a size smaller than this will be merged with larger regions if possible.

 **Note:** This value will be squared to calculate the number of cells. For example, a value of 20 will set the number of cells to 400.

---

<span id="class_NavigationMesh_property_region_min_size"></span>

[float](class_float.md#class_float) **region_min_size** = `2.0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_region_min_size)

- void **set_region_min_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_region_min_size** ( )

The minimum size of a region for it to be created.

 **Note:** This value will be squared to calculate the minimum number of cells allowed to form isolated island areas. For example, a value of 8 will set the number of cells to 64.

---

<span id="class_NavigationMesh_property_sample_partition_type"></span>

[SamplePartitionType](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType) **sample_partition_type** = `0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_sample_partition_type)

- void **set_sample_partition_type** ( value: [SamplePartitionType](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType) )
- [SamplePartitionType](class_navigationmesh.md#enum_NavigationMesh_SamplePartitionType) **get_sample_partition_type** ( )

Partitioning algorithm for creating the navigation mesh polys.

---

<span id="class_NavigationMesh_property_vertices_per_polygon"></span>

[float](class_float.md#class_float) **vertices_per_polygon** = `6.0` [🔗](class_navigationmesh.md#class_NavigationMesh_property_vertices_per_polygon)

- void **set_vertices_per_polygon** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_vertices_per_polygon** ( )

The maximum number of vertices allowed for polygons generated during the contour to polygon conversion process.

---

### Method Descriptions

<span id="class_NavigationMesh_method_add_polygon"></span>

void **add_polygon** ( polygon: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_navigationmesh.md#class_NavigationMesh_method_add_polygon)

Adds a polygon using the indices of the vertices you get when calling [get_vertices()](class_navigationmesh.md#class_NavigationMesh_method_get_vertices).

---

<span id="class_NavigationMesh_method_clear"></span>

void **clear** ( ) [🔗](class_navigationmesh.md#class_NavigationMesh_method_clear)

Clears the internal arrays for vertices and polygon indices.

---

<span id="class_NavigationMesh_method_clear_polygons"></span>

void **clear_polygons** ( ) [🔗](class_navigationmesh.md#class_NavigationMesh_method_clear_polygons)

Clears the array of polygons, but it doesn't clear the array of vertices.

---

<span id="class_NavigationMesh_method_create_from_mesh"></span>

void **create_from_mesh** ( mesh: [Mesh](class_mesh.md#class_Mesh) ) [🔗](class_navigationmesh.md#class_NavigationMesh_method_create_from_mesh)

Initializes the navigation mesh by setting the vertices and indices according to a [Mesh](class_mesh.md#class_Mesh).

 **Note:** The given `mesh` must be of type [Mesh.PRIMITIVE_TRIANGLES](class_mesh.md#class_Mesh_constant_PRIMITIVE_TRIANGLES) and have an index array.

---

<span id="class_NavigationMesh_method_get_collision_mask_value"></span>

[bool](class_bool.md#class_bool) **get_collision_mask_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_navigationmesh.md#class_NavigationMesh_method_get_collision_mask_value)

Returns whether or not the specified layer of the [geometry_collision_mask](class_navigationmesh.md#class_NavigationMesh_property_geometry_collision_mask) is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_NavigationMesh_method_get_polygon"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_polygon** ( idx: [int](class_int.md#class_int) ) [🔗](class_navigationmesh.md#class_NavigationMesh_method_get_polygon)

Returns a [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) containing the indices of the vertices of a created polygon.

---

<span id="class_NavigationMesh_method_get_polygon_count"></span>

[int](class_int.md#class_int) **get_polygon_count** ( ) *const* [🔗](class_navigationmesh.md#class_NavigationMesh_method_get_polygon_count)

Returns the number of polygons in the navigation mesh.

---

<span id="class_NavigationMesh_method_get_vertices"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_vertices** ( ) *const* [🔗](class_navigationmesh.md#class_NavigationMesh_method_get_vertices)

Returns a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) containing all the vertices being used to create the polygons.

---

<span id="class_NavigationMesh_method_set_collision_mask_value"></span>

void **set_collision_mask_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_navigationmesh.md#class_NavigationMesh_method_set_collision_mask_value)

Based on `value`, enables or disables the specified layer in the [geometry_collision_mask](class_navigationmesh.md#class_NavigationMesh_property_geometry_collision_mask), given a `layer_number` between 1 and 32.

---

<span id="class_NavigationMesh_method_set_vertices"></span>

void **set_vertices** ( vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) [🔗](class_navigationmesh.md#class_NavigationMesh_method_set_vertices)

Sets the vertices that can be then indexed to create polygons with the [add_polygon()](class_navigationmesh.md#class_NavigationMesh_method_add_polygon) method.
