<span id="class_NavigationPathQueryParameters2D"></span>

## NavigationPathQueryParameters2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides parameters for 2D navigation path queries.

### Description

By changing various properties of this object, such as the start and target position, you can configure path queries to the [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D).

### Tutorials

- [Using NavigationPathQueryObjects](../tutorials/navigation/navigation_using_navigationpathqueryobjects.md)

### Properties


| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [excluded_regions](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_excluded_regions) | `[]` |
| --- | --- | --- |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [included_regions](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_included_regions) | `[]` |
| [RID](class_rid.md#class_RID) | [map](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_map) | `RID()` |
| bitfield | \[[PathMetadataFlags](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags)\] | [metadata_flags](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_metadata_flags) | `7` |
| [int](class_int.md#class_int) | [navigation_layers](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_navigation_layers) | `1` |
| [PathPostProcessing](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathPostProcessing) | [path_postprocessing](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_postprocessing) | `0` |
| [float](class_float.md#class_float) | [path_return_max_length](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_return_max_length) | `0.0` |
| [float](class_float.md#class_float) | [path_return_max_radius](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_return_max_radius) | `0.0` |
| [float](class_float.md#class_float) | [path_search_max_distance](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_search_max_distance) | `0.0` |
| [int](class_int.md#class_int) | [path_search_max_polygons](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_search_max_polygons) | `4096` |
| [PathfindingAlgorithm](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathfindingAlgorithm) | [pathfinding_algorithm](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_pathfinding_algorithm) | `0` |
| [float](class_float.md#class_float) | [simplify_epsilon](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_simplify_epsilon) | `0.0` |
| [bool](class_bool.md#class_bool) | [simplify_path](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_simplify_path) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [start_position](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_start_position) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [target_position](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_target_position) | `Vector2(0, 0)` |

---

### Enumerations

<span id="enum_NavigationPathQueryParameters2D_PathfindingAlgorithm"></span>

enum **PathfindingAlgorithm**: [🔗](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathfindingAlgorithm)

<span id="class_NavigationPathQueryParameters2D_constant_PATHFINDING_ALGORITHM_ASTAR"></span>

[PathfindingAlgorithm](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathfindingAlgorithm) **PATHFINDING_ALGORITHM_ASTAR** = `0`

The path query uses the default A\* pathfinding algorithm.

---

<span id="enum_NavigationPathQueryParameters2D_PathPostProcessing"></span>

enum **PathPostProcessing**: [🔗](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathPostProcessing)

<span id="class_NavigationPathQueryParameters2D_constant_PATH_POSTPROCESSING_CORRIDORFUNNEL"></span>

[PathPostProcessing](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathPostProcessing) **PATH_POSTPROCESSING_CORRIDORFUNNEL** = `0`

Applies a funnel algorithm to the raw path corridor found by the pathfinding algorithm. This will result in the shortest path possible inside the path corridor. This postprocessing very much depends on the navigation mesh polygon layout and the created corridor. Especially tile- or gridbased layouts can face artificial corners with diagonal movement due to a jagged path corridor imposed by the cell shapes.

<span id="class_NavigationPathQueryParameters2D_constant_PATH_POSTPROCESSING_EDGECENTERED"></span>

[PathPostProcessing](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathPostProcessing) **PATH_POSTPROCESSING_EDGECENTERED** = `1`

Centers every path position in the middle of the traveled navigation mesh polygon edge. This creates better paths for tile- or gridbased layouts that restrict the movement to the cells center.

<span id="class_NavigationPathQueryParameters2D_constant_PATH_POSTPROCESSING_NONE"></span>

[PathPostProcessing](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathPostProcessing) **PATH_POSTPROCESSING_NONE** = `2`

Applies no postprocessing and returns the raw path corridor as found by the pathfinding algorithm.

---

<span id="enum_NavigationPathQueryParameters2D_PathMetadataFlags"></span>

flags **PathMetadataFlags**: [🔗](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags)

<span id="class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_NONE"></span>

[PathMetadataFlags](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags) **PATH_METADATA_INCLUDE_NONE** = `0`

Don't include any additional metadata about the returned path.

<span id="class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_TYPES"></span>

[PathMetadataFlags](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags) **PATH_METADATA_INCLUDE_TYPES** = `1`

Include the type of navigation primitive (region or link) that each point of the path goes through.

<span id="class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_RIDS"></span>

[PathMetadataFlags](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags) **PATH_METADATA_INCLUDE_RIDS** = `2`

Include the [RID](class_rid.md#class_RID) s of the regions and links that each point of the path goes through.

<span id="class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_OWNERS"></span>

[PathMetadataFlags](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags) **PATH_METADATA_INCLUDE_OWNERS** = `4`

Include the `ObjectID` s of the [Object](class_object.md#class_Object) s which manage the regions and links each point of the path goes through.

<span id="class_NavigationPathQueryParameters2D_constant_PATH_METADATA_INCLUDE_ALL"></span>

[PathMetadataFlags](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags) **PATH_METADATA_INCLUDE_ALL** = `7`

Include all available metadata about the returned path.

---

### Property Descriptions

<span id="class_NavigationPathQueryParameters2D_property_excluded_regions"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **excluded_regions** = `[]` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_excluded_regions)

- void **set_excluded_regions** ( value: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] )
- [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **get_excluded_regions** ( )

The list of region [RID](class_rid.md#class_RID) s that will be excluded from the path query. Use [NavigationRegion2D.get_rid()](class_navigationregion2d.md#class_NavigationRegion2D_method_get_rid) to get the [RID](class_rid.md#class_RID) associated with a [NavigationRegion2D](class_navigationregion2d.md#class_NavigationRegion2D) node.

 **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then set it to the property again.

---

<span id="class_NavigationPathQueryParameters2D_property_included_regions"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **included_regions** = `[]` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_included_regions)

- void **set_included_regions** ( value: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] )
- [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **get_included_regions** ( )

The list of region [RID](class_rid.md#class_RID) s that will be included by the path query. Use [NavigationRegion2D.get_rid()](class_navigationregion2d.md#class_NavigationRegion2D_method_get_rid) to get the [RID](class_rid.md#class_RID) associated with a [NavigationRegion2D](class_navigationregion2d.md#class_NavigationRegion2D) node. If left empty all regions are included. If a region ends up being both included and excluded at the same time it will be excluded.

 **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then set it to the property again.

---

<span id="class_NavigationPathQueryParameters2D_property_map"></span>

[RID](class_rid.md#class_RID) **map** = `RID()` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_map)

- void **set_map** ( value: [RID](class_rid.md#class_RID) )
- [RID](class_rid.md#class_RID) **get_map** ( )

The navigation map [RID](class_rid.md#class_RID) used in the path query.

---

<span id="class_NavigationPathQueryParameters2D_property_metadata_flags"></span>

*BitField*\[[PathMetadataFlags](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags)\] **metadata_flags** = `7` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_metadata_flags)

- void **set_metadata_flags** ( value: *BitField*\[[PathMetadataFlags](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags)\] )
- *BitField*\[[PathMetadataFlags](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathMetadataFlags)\] **get_metadata_flags** ( )

Additional information to include with the navigation path.

---

<span id="class_NavigationPathQueryParameters2D_property_navigation_layers"></span>

[int](class_int.md#class_int) **navigation_layers** = `1` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_navigation_layers)

- void **set_navigation_layers** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_navigation_layers** ( )

The navigation layers the query will use (as a bitmask).

---

<span id="class_NavigationPathQueryParameters2D_property_path_postprocessing"></span>

[PathPostProcessing](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathPostProcessing) **path_postprocessing** = `0` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_postprocessing)

- void **set_path_postprocessing** ( value: [PathPostProcessing](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathPostProcessing) )
- [PathPostProcessing](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathPostProcessing) **get_path_postprocessing** ( )

The path postprocessing applied to the raw path corridor found by the [pathfinding_algorithm](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_pathfinding_algorithm).

---

<span id="class_NavigationPathQueryParameters2D_property_path_return_max_length"></span>

[float](class_float.md#class_float) **path_return_max_length** = `0.0` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_return_max_length)

- void **set_path_return_max_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_path_return_max_length** ( )

The maximum allowed length of the returned path in world units. A path will be clipped when going over this length. A value of `0` or below counts as disabled.

---

<span id="class_NavigationPathQueryParameters2D_property_path_return_max_radius"></span>

[float](class_float.md#class_float) **path_return_max_radius** = `0.0` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_return_max_radius)

- void **set_path_return_max_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_path_return_max_radius** ( )

The maximum allowed radius in world units that the returned path can be from the path start. The path will be clipped when going over this radius. A value of `0` or below counts as disabled.

 **Note:** This will perform a circle shaped clip operation on the path with the first path position being the circle's center position.

---

<span id="class_NavigationPathQueryParameters2D_property_path_search_max_distance"></span>

[float](class_float.md#class_float) **path_search_max_distance** = `0.0` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_search_max_distance)

- void **set_path_search_max_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_path_search_max_distance** ( )

The maximum distance a searched polygon can be away from the start polygon before the pathfinding cancels the search for a path to the (possibly unreachable or very far away) target position polygon. In this case the pathfinding resets and builds a path from the start polygon to the polygon that was found closest to the target position so far. A value of `0` or below counts as unlimited. In case of unlimited the pathfinding will search all polygons connected with the start polygon until either the target position polygon is found or all available polygon search options are exhausted.

---

<span id="class_NavigationPathQueryParameters2D_property_path_search_max_polygons"></span>

[int](class_int.md#class_int) **path_search_max_polygons** = `4096` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_path_search_max_polygons)

- void **set_path_search_max_polygons** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_path_search_max_polygons** ( )

The maximum number of polygons that are searched before the pathfinding cancels the search for a path to the (possibly unreachable or very far away) target position polygon. In this case the pathfinding resets and builds a path from the start polygon to the polygon that was found closest to the target position so far. A value of `0` or below counts as unlimited. In case of unlimited the pathfinding will search all polygons connected with the start polygon until either the target position polygon is found or all available polygon search options are exhausted.

---

<span id="class_NavigationPathQueryParameters2D_property_pathfinding_algorithm"></span>

[PathfindingAlgorithm](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathfindingAlgorithm) **pathfinding_algorithm** = `0` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_pathfinding_algorithm)

- void **set_pathfinding_algorithm** ( value: [PathfindingAlgorithm](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathfindingAlgorithm) )
- [PathfindingAlgorithm](class_navigationpathqueryparameters2d.md#enum_NavigationPathQueryParameters2D_PathfindingAlgorithm) **get_pathfinding_algorithm** ( )

The pathfinding algorithm used in the path query.

---

<span id="class_NavigationPathQueryParameters2D_property_simplify_epsilon"></span>

[float](class_float.md#class_float) **simplify_epsilon** = `0.0` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_simplify_epsilon)

- void **set_simplify_epsilon** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_simplify_epsilon** ( )

The path simplification amount in worlds units.

---

<span id="class_NavigationPathQueryParameters2D_property_simplify_path"></span>

[bool](class_bool.md#class_bool) **simplify_path** = `false` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_simplify_path)

- void **set_simplify_path** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_simplify_path** ( )

If `true` a simplified version of the path will be returned with less critical path points removed. The simplification amount is controlled by [simplify_epsilon](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_simplify_epsilon). The simplification uses a variant of Ramer-Douglas-Peucker algorithm for curve point decimation.

Path simplification can be helpful to mitigate various path following issues that can arise with certain agent types and script behaviors. E.g. "steering" agents or avoidance in "open fields".

---

<span id="class_NavigationPathQueryParameters2D_property_start_position"></span>

[Vector2](class_vector2.md#class_Vector2) **start_position** = `Vector2(0, 0)` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_start_position)

- void **set_start_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_start_position** ( )

The pathfinding start position in global coordinates.

---

<span id="class_NavigationPathQueryParameters2D_property_target_position"></span>

[Vector2](class_vector2.md#class_Vector2) **target_position** = `Vector2(0, 0)` [🔗](class_navigationpathqueryparameters2d.md#class_NavigationPathQueryParameters2D_property_target_position)

- void **set_target_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_target_position** ( )

The pathfinding target position in global coordinates.
