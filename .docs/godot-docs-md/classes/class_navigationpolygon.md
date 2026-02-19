<span id="class_NavigationPolygon"></span>

## NavigationPolygon

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 2D navigation mesh that describes a traversable surface for pathfinding.

### Description

A navigation mesh can be created either by baking it with the help of the [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D), or by adding vertices and convex polygon indices arrays manually.

To bake a navigation mesh at least one outline needs to be added that defines the outer bounds of the baked area.

.. tabs::

```
```

    var new_navigation_mesh = NavigationPolygon.new()
    var bounding_outline = PackedVector2Array([Vector2(0, 0), Vector2(0, 50), Vector2(50, 50), Vector2(50, 0)])
    new_navigation_mesh.add_outline(bounding_outline)
    NavigationServer2D.bake_from_source_geometry_data(new_navigation_mesh, NavigationMeshSourceGeometryData2D.new());
    $NavigationRegion2D.navigation_polygon = new_navigation_mesh

```
```

    var newNavigationMesh = new NavigationPolygon();
    Vector2[] boundingOutline = [new Vector2(0, 0), new Vector2(0, 50), new Vector2(50, 50), new Vector2(50, 0)];
    newNavigationMesh.AddOutline(boundingOutline);
    NavigationServer2D.BakeFromSourceGeometryData(newNavigationMesh, new NavigationMeshSourceGeometryData2D());
    GetNode<NavigationRegion2D>("NavigationRegion2D").NavigationPolygon = newNavigationMesh;

Adding vertices and polygon indices manually.

.. tabs::

```
```

    var new_navigation_mesh = NavigationPolygon.new()
    var new_vertices = PackedVector2Array([Vector2(0, 0), Vector2(0, 50), Vector2(50, 50), Vector2(50, 0)])
    new_navigation_mesh.vertices = new_vertices
    var new_polygon_indices = PackedInt32Array([0, 1, 2, 3])
    new_navigation_mesh.add_polygon(new_polygon_indices)
    $NavigationRegion2D.navigation_polygon = new_navigation_mesh

```
```

    var newNavigationMesh = new NavigationPolygon();
    Vector2[] newVertices = [new Vector2(0, 0), new Vector2(0, 50), new Vector2(50, 50), new Vector2(50, 0)];
    newNavigationMesh.Vertices = newVertices;
    int[] newPolygonIndices = [0, 1, 2, 3];
    newNavigationMesh.AddPolygon(newPolygonIndices);
    GetNode<NavigationRegion2D>("NavigationRegion2D").NavigationPolygon = newNavigationMesh;

### Tutorials

- [Using NavigationMeshes](../tutorials/navigation/navigation_using_navigationmeshes.md)

- Navigation Polygon 2D Demo

### Properties


| [float](class_float.md#class_float) | [agent_radius](class_navigationpolygon.md#class_NavigationPolygon_property_agent_radius) | `10.0` |
| --- | --- | --- |
| [Rect2](class_rect2.md#class_Rect2) | [baking_rect](class_navigationpolygon.md#class_NavigationPolygon_property_baking_rect) | `Rect2(0, 0, 0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [baking_rect_offset](class_navigationpolygon.md#class_NavigationPolygon_property_baking_rect_offset) | `Vector2(0, 0)` |
| [float](class_float.md#class_float) | [border_size](class_navigationpolygon.md#class_NavigationPolygon_property_border_size) | `0.0` |
| [float](class_float.md#class_float) | [cell_size](class_navigationpolygon.md#class_NavigationPolygon_property_cell_size) | `1.0` |
| [int](class_int.md#class_int) | [parsed_collision_mask](class_navigationpolygon.md#class_NavigationPolygon_property_parsed_collision_mask) | `4294967295` |
| [ParsedGeometryType](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType) | [parsed_geometry_type](class_navigationpolygon.md#class_NavigationPolygon_property_parsed_geometry_type) | `2` |
| [SamplePartitionType](class_navigationpolygon.md#enum_NavigationPolygon_SamplePartitionType) | [sample_partition_type](class_navigationpolygon.md#class_NavigationPolygon_property_sample_partition_type) | `0` |
| [StringName](class_stringname.md#class_StringName) | [source_geometry_group_name](class_navigationpolygon.md#class_NavigationPolygon_property_source_geometry_group_name) | `&"navigation_polygon_source_geometry_group"` |
| [SourceGeometryMode](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode) | [source_geometry_mode](class_navigationpolygon.md#class_NavigationPolygon_property_source_geometry_mode) | `0` |

### Methods


| void | [add_outline](class_navigationpolygon.md#class_NavigationPolygon_method_add_outline) ( outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) |
| --- | --- |
| void | [add_outline_at_index](class_navigationpolygon.md#class_NavigationPolygon_method_add_outline_at_index) ( outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), index: [int](class_int.md#class_int) ) |
| void | [add_polygon](class_navigationpolygon.md#class_NavigationPolygon_method_add_polygon) ( polygon: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| void | [clear](class_navigationpolygon.md#class_NavigationPolygon_method_clear) ( ) |
| void | [clear_outlines](class_navigationpolygon.md#class_NavigationPolygon_method_clear_outlines) ( ) |
| void | [clear_polygons](class_navigationpolygon.md#class_NavigationPolygon_method_clear_polygons) ( ) |
| [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) | [get_navigation_mesh](class_navigationpolygon.md#class_NavigationPolygon_method_get_navigation_mesh) ( ) |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [get_outline](class_navigationpolygon.md#class_NavigationPolygon_method_get_outline) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_outline_count](class_navigationpolygon.md#class_NavigationPolygon_method_get_outline_count) ( ) const |
| [bool](class_bool.md#class_bool) | [get_parsed_collision_mask_value](class_navigationpolygon.md#class_NavigationPolygon_method_get_parsed_collision_mask_value) ( layer_number: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_polygon](class_navigationpolygon.md#class_NavigationPolygon_method_get_polygon) ( idx: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_polygon_count](class_navigationpolygon.md#class_NavigationPolygon_method_get_polygon_count) ( ) const |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [get_vertices](class_navigationpolygon.md#class_NavigationPolygon_method_get_vertices) ( ) const |
| void | [make_polygons_from_outlines](class_navigationpolygon.md#class_NavigationPolygon_method_make_polygons_from_outlines) ( ) |
| void | [remove_outline](class_navigationpolygon.md#class_NavigationPolygon_method_remove_outline) ( idx: [int](class_int.md#class_int) ) |
| void | [set_outline](class_navigationpolygon.md#class_NavigationPolygon_method_set_outline) ( idx: [int](class_int.md#class_int), outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) |
| void | [set_parsed_collision_mask_value](class_navigationpolygon.md#class_NavigationPolygon_method_set_parsed_collision_mask_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |
| void | [set_vertices](class_navigationpolygon.md#class_NavigationPolygon_method_set_vertices) ( vertices: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) |

---

### Enumerations

<span id="enum_NavigationPolygon_SamplePartitionType"></span>

enum **SamplePartitionType**: [🔗](class_navigationpolygon.md#enum_NavigationPolygon_SamplePartitionType)

<span id="class_NavigationPolygon_constant_SAMPLE_PARTITION_CONVEX_PARTITION"></span>

[SamplePartitionType](class_navigationpolygon.md#enum_NavigationPolygon_SamplePartitionType) **SAMPLE_PARTITION_CONVEX_PARTITION** = `0`

Convex partitioning that results in a navigation mesh with convex polygons.

<span id="class_NavigationPolygon_constant_SAMPLE_PARTITION_TRIANGULATE"></span>

[SamplePartitionType](class_navigationpolygon.md#enum_NavigationPolygon_SamplePartitionType) **SAMPLE_PARTITION_TRIANGULATE** = `1`

Triangulation partitioning that results in a navigation mesh with triangle polygons.

<span id="class_NavigationPolygon_constant_SAMPLE_PARTITION_MAX"></span>

[SamplePartitionType](class_navigationpolygon.md#enum_NavigationPolygon_SamplePartitionType) **SAMPLE_PARTITION_MAX** = `2`

Represents the size of the [SamplePartitionType](class_navigationpolygon.md#enum_NavigationPolygon_SamplePartitionType) enum.

---

<span id="enum_NavigationPolygon_ParsedGeometryType"></span>

enum **ParsedGeometryType**: [🔗](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType)

<span id="class_NavigationPolygon_constant_PARSED_GEOMETRY_MESH_INSTANCES"></span>

[ParsedGeometryType](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType) **PARSED_GEOMETRY_MESH_INSTANCES** = `0`

Parses mesh instances as obstruction geometry. This includes [Polygon2D](class_polygon2d.md#class_Polygon2D), [MeshInstance2D](class_meshinstance2d.md#class_MeshInstance2D), [MultiMeshInstance2D](class_multimeshinstance2d.md#class_MultiMeshInstance2D), and [TileMap](class_tilemap.md#class_TileMap) nodes.

Meshes are only parsed when they use a 2D vertices surface format.

<span id="class_NavigationPolygon_constant_PARSED_GEOMETRY_STATIC_COLLIDERS"></span>

[ParsedGeometryType](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType) **PARSED_GEOMETRY_STATIC_COLLIDERS** = `1`

Parses [StaticBody2D](class_staticbody2d.md#class_StaticBody2D) and [TileMap](class_tilemap.md#class_TileMap) colliders as obstruction geometry. The collider should be in any of the layers specified by [parsed_collision_mask](class_navigationpolygon.md#class_NavigationPolygon_property_parsed_collision_mask).

<span id="class_NavigationPolygon_constant_PARSED_GEOMETRY_BOTH"></span>

[ParsedGeometryType](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType) **PARSED_GEOMETRY_BOTH** = `2`

Both [PARSED_GEOMETRY_MESH_INSTANCES](class_navigationpolygon.md#class_NavigationPolygon_constant_PARSED_GEOMETRY_MESH_INSTANCES) and [PARSED_GEOMETRY_STATIC_COLLIDERS](class_navigationpolygon.md#class_NavigationPolygon_constant_PARSED_GEOMETRY_STATIC_COLLIDERS).

<span id="class_NavigationPolygon_constant_PARSED_GEOMETRY_MAX"></span>

[ParsedGeometryType](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType) **PARSED_GEOMETRY_MAX** = `3`

Represents the size of the [ParsedGeometryType](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType) enum.

---

<span id="enum_NavigationPolygon_SourceGeometryMode"></span>

enum **SourceGeometryMode**: [🔗](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode)

<span id="class_NavigationPolygon_constant_SOURCE_GEOMETRY_ROOT_NODE_CHILDREN"></span>

[SourceGeometryMode](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode) **SOURCE_GEOMETRY_ROOT_NODE_CHILDREN** = `0`

Scans the child nodes of the root node recursively for geometry.

<span id="class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN"></span>

[SourceGeometryMode](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode) **SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN** = `1`

Scans nodes in a group and their child nodes recursively for geometry. The group is specified by [source_geometry_group_name](class_navigationpolygon.md#class_NavigationPolygon_property_source_geometry_group_name).

<span id="class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_EXPLICIT"></span>

[SourceGeometryMode](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode) **SOURCE_GEOMETRY_GROUPS_EXPLICIT** = `2`

Uses nodes in a group for geometry. The group is specified by [source_geometry_group_name](class_navigationpolygon.md#class_NavigationPolygon_property_source_geometry_group_name).

<span id="class_NavigationPolygon_constant_SOURCE_GEOMETRY_MAX"></span>

[SourceGeometryMode](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode) **SOURCE_GEOMETRY_MAX** = `3`

Represents the size of the [SourceGeometryMode](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode) enum.

---

### Property Descriptions

<span id="class_NavigationPolygon_property_agent_radius"></span>

[float](class_float.md#class_float) **agent_radius** = `10.0` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_agent_radius)

- void **set_agent_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_agent_radius** ( )

The distance to erode/shrink the walkable surface when baking the navigation mesh.

 **Note:** The radius must be equal or higher than `0.0`. If the radius is `0.0`, it won't be possible to fix invalid outline overlaps and other precision errors during the baking process. As a result, some obstacles may be excluded incorrectly from the final navigation mesh, or may delete the navigation mesh's polygons.

---

<span id="class_NavigationPolygon_property_baking_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **baking_rect** = `Rect2(0, 0, 0, 0)` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_baking_rect)

- void **set_baking_rect** ( value: [Rect2](class_rect2.md#class_Rect2) )
- [Rect2](class_rect2.md#class_Rect2) **get_baking_rect** ( )

If the baking [Rect2](class_rect2.md#class_Rect2) has an area the navigation mesh baking will be restricted to its enclosing area.

---

<span id="class_NavigationPolygon_property_baking_rect_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **baking_rect_offset** = `Vector2(0, 0)` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_baking_rect_offset)

- void **set_baking_rect_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_baking_rect_offset** ( )

The position offset applied to the [baking_rect](class_navigationpolygon.md#class_NavigationPolygon_property_baking_rect) [Rect2](class_rect2.md#class_Rect2).

---

<span id="class_NavigationPolygon_property_border_size"></span>

[float](class_float.md#class_float) **border_size** = `0.0` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_border_size)

- void **set_border_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_border_size** ( )

The size of the non-navigable border around the bake bounding area defined by the [baking_rect](class_navigationpolygon.md#class_NavigationPolygon_property_baking_rect) [Rect2](class_rect2.md#class_Rect2).

In conjunction with the [baking_rect](class_navigationpolygon.md#class_NavigationPolygon_property_baking_rect) the border size can be used to bake tile aligned navigation meshes without the tile edges being shrunk by [agent_radius](class_navigationpolygon.md#class_NavigationPolygon_property_agent_radius).

---

<span id="class_NavigationPolygon_property_cell_size"></span>

[float](class_float.md#class_float) **cell_size** = `1.0` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_cell_size)

- void **set_cell_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_cell_size** ( )

The cell size used to rasterize the navigation mesh vertices. Must match with the cell size on the navigation map.

---

<span id="class_NavigationPolygon_property_parsed_collision_mask"></span>

[int](class_int.md#class_int) **parsed_collision_mask** = `4294967295` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_parsed_collision_mask)

- void **set_parsed_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_parsed_collision_mask** ( )

The physics layers to scan for static colliders.

Only used when [parsed_geometry_type](class_navigationpolygon.md#class_NavigationPolygon_property_parsed_geometry_type) is [PARSED_GEOMETRY_STATIC_COLLIDERS](class_navigationpolygon.md#class_NavigationPolygon_constant_PARSED_GEOMETRY_STATIC_COLLIDERS) or [PARSED_GEOMETRY_BOTH](class_navigationpolygon.md#class_NavigationPolygon_constant_PARSED_GEOMETRY_BOTH).

---

<span id="class_NavigationPolygon_property_parsed_geometry_type"></span>

[ParsedGeometryType](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType) **parsed_geometry_type** = `2` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_parsed_geometry_type)

- void **set_parsed_geometry_type** ( value: [ParsedGeometryType](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType) )
- [ParsedGeometryType](class_navigationpolygon.md#enum_NavigationPolygon_ParsedGeometryType) **get_parsed_geometry_type** ( )

Determines which type of nodes will be parsed as geometry.

---

<span id="class_NavigationPolygon_property_sample_partition_type"></span>

[SamplePartitionType](class_navigationpolygon.md#enum_NavigationPolygon_SamplePartitionType) **sample_partition_type** = `0` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_sample_partition_type)

- void **set_sample_partition_type** ( value: [SamplePartitionType](class_navigationpolygon.md#enum_NavigationPolygon_SamplePartitionType) )
- [SamplePartitionType](class_navigationpolygon.md#enum_NavigationPolygon_SamplePartitionType) **get_sample_partition_type** ( )

Partitioning algorithm for creating the navigation mesh polys.

---

<span id="class_NavigationPolygon_property_source_geometry_group_name"></span>

[StringName](class_stringname.md#class_StringName) **source_geometry_group_name** = `&"navigation_polygon_source_geometry_group"` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_source_geometry_group_name)

- void **set_source_geometry_group_name** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_source_geometry_group_name** ( )

The group name of nodes that should be parsed for baking source geometry.

Only used when [source_geometry_mode](class_navigationpolygon.md#class_NavigationPolygon_property_source_geometry_mode) is [SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN](class_navigationpolygon.md#class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN) or [SOURCE_GEOMETRY_GROUPS_EXPLICIT](class_navigationpolygon.md#class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_EXPLICIT).

---

<span id="class_NavigationPolygon_property_source_geometry_mode"></span>

[SourceGeometryMode](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode) **source_geometry_mode** = `0` [🔗](class_navigationpolygon.md#class_NavigationPolygon_property_source_geometry_mode)

- void **set_source_geometry_mode** ( value: [SourceGeometryMode](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode) )
- [SourceGeometryMode](class_navigationpolygon.md#enum_NavigationPolygon_SourceGeometryMode) **get_source_geometry_mode** ( )

The source of the geometry used when baking.

---

### Method Descriptions

<span id="class_NavigationPolygon_method_add_outline"></span>

void **add_outline** ( outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_add_outline)

Appends a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) that contains the vertices of an outline to the internal array that contains all the outlines.

---

<span id="class_NavigationPolygon_method_add_outline_at_index"></span>

void **add_outline_at_index** ( outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), index: [int](class_int.md#class_int) ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_add_outline_at_index)

Adds a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) that contains the vertices of an outline to the internal array that contains all the outlines at a fixed position.

---

<span id="class_NavigationPolygon_method_add_polygon"></span>

void **add_polygon** ( polygon: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_add_polygon)

Adds a polygon using the indices of the vertices you get when calling [get_vertices()](class_navigationpolygon.md#class_NavigationPolygon_method_get_vertices).

---

<span id="class_NavigationPolygon_method_clear"></span>

void **clear** ( ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_clear)

Clears the internal arrays for vertices and polygon indices.

---

<span id="class_NavigationPolygon_method_clear_outlines"></span>

void **clear_outlines** ( ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_clear_outlines)

Clears the array of the outlines, but it doesn't clear the vertices and the polygons that were created by them.

---

<span id="class_NavigationPolygon_method_clear_polygons"></span>

void **clear_polygons** ( ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_clear_polygons)

Clears the array of polygons, but it doesn't clear the array of outlines and vertices.

---

<span id="class_NavigationPolygon_method_get_navigation_mesh"></span>

[NavigationMesh](class_navigationmesh.md#class_NavigationMesh) **get_navigation_mesh** ( ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_get_navigation_mesh)

Returns the [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) resulting from this navigation polygon. This navigation mesh can be used to update the navigation mesh of a region with the [NavigationServer3D.region_set_navigation_mesh()](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_navigation_mesh) API directly.

---

<span id="class_NavigationPolygon_method_get_outline"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_outline** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_get_outline)

Returns a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) containing the vertices of an outline that was created in the editor or by script.

---

<span id="class_NavigationPolygon_method_get_outline_count"></span>

[int](class_int.md#class_int) **get_outline_count** ( ) *const* [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_get_outline_count)

Returns the number of outlines that were created in the editor or by script.

---

<span id="class_NavigationPolygon_method_get_parsed_collision_mask_value"></span>

[bool](class_bool.md#class_bool) **get_parsed_collision_mask_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_get_parsed_collision_mask_value)

Returns whether or not the specified layer of the [parsed_collision_mask](class_navigationpolygon.md#class_NavigationPolygon_property_parsed_collision_mask) is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_NavigationPolygon_method_get_polygon"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_polygon** ( idx: [int](class_int.md#class_int) ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_get_polygon)

Returns a [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) containing the indices of the vertices of a created polygon.

---

<span id="class_NavigationPolygon_method_get_polygon_count"></span>

[int](class_int.md#class_int) **get_polygon_count** ( ) *const* [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_get_polygon_count)

Returns the count of all polygons.

---

<span id="class_NavigationPolygon_method_get_vertices"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_vertices** ( ) *const* [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_get_vertices)

Returns a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) containing all the vertices being used to create the polygons.

---

<span id="class_NavigationPolygon_method_make_polygons_from_outlines"></span>

void **make_polygons_from_outlines** ( ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_make_polygons_from_outlines)

**Deprecated:** Use [NavigationServer2D.parse_source_geometry_data()](class_navigationserver2d.md#class_NavigationServer2D_method_parse_source_geometry_data) and [NavigationServer2D.bake_from_source_geometry_data()](class_navigationserver2d.md#class_NavigationServer2D_method_bake_from_source_geometry_data) instead.

Creates polygons from the outlines added in the editor or by script.

---

<span id="class_NavigationPolygon_method_remove_outline"></span>

void **remove_outline** ( idx: [int](class_int.md#class_int) ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_remove_outline)

Removes an outline created in the editor or by script. You have to call [make_polygons_from_outlines()](class_navigationpolygon.md#class_NavigationPolygon_method_make_polygons_from_outlines) for the polygons to update.

---

<span id="class_NavigationPolygon_method_set_outline"></span>

void **set_outline** ( idx: [int](class_int.md#class_int), outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_set_outline)

Changes an outline created in the editor or by script. You have to call [make_polygons_from_outlines()](class_navigationpolygon.md#class_NavigationPolygon_method_make_polygons_from_outlines) for the polygons to update.

---

<span id="class_NavigationPolygon_method_set_parsed_collision_mask_value"></span>

void **set_parsed_collision_mask_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_set_parsed_collision_mask_value)

Based on `value`, enables or disables the specified layer in the [parsed_collision_mask](class_navigationpolygon.md#class_NavigationPolygon_property_parsed_collision_mask), given a `layer_number` between 1 and 32.

---

<span id="class_NavigationPolygon_method_set_vertices"></span>

void **set_vertices** ( vertices: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) [🔗](class_navigationpolygon.md#class_NavigationPolygon_method_set_vertices)

Sets the vertices that can be then indexed to create polygons with the [add_polygon()](class_navigationpolygon.md#class_NavigationPolygon_method_add_polygon) method.
