<span id="class_NavigationServer3D"></span>

## NavigationServer3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Object](class_object.md#class_Object)

A server interface for low-level 3D navigation access.

### Description

NavigationServer3D is the server that handles navigation maps, regions and agents. It does not handle A\* navigation from [AStar3D](class_astar3d.md#class_AStar3D).

Maps are divided into regions, which are composed of navigation meshes. Together, they define the navigable areas in the 3D world.

 **Note:** Most **NavigationServer3D** changes take effect after the next physics frame and not immediately. This includes all changes made to maps, regions or agents by navigation-related nodes in the scene tree or made through scripts.

For two regions to be connected to each other, they must share a similar edge. An edge is considered connected to another if both of its two vertices are at a distance less than `edge_connection_margin` to the respective other edge's vertex.

You may assign navigation layers to regions with [region_set_navigation_layers()](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_navigation_layers), which then can be checked upon when requesting a path with [map_get_path()](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_path). This can be used to allow or deny certain areas for some objects.

To use the collision avoidance system, you may use agents. You can set an agent's target velocity, then the servers will emit a callback with a modified velocity.

 **Note:** The collision avoidance system ignores regions. Using the modified velocity directly may move an agent outside of the traversable area. This is a limitation of the collision avoidance system, any more complex situation may require the use of the physics engine.

This server keeps tracks of any call and executes them during the sync phase. This means that you can request any change to the map, using any thread, without worrying.

### Tutorials

- [Using NavigationServer](../tutorials/navigation/navigation_using_navigationservers.md)

- 3D Navigation Demo

### Methods


| [RID](class_rid.md#class_RID) | [agent_create](class_navigationserver3d.md#class_NavigationServer3D_method_agent_create) ( ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [agent_get_avoidance_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_avoidance_enabled) ( agent: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [agent_get_avoidance_layers](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_avoidance_layers) ( agent: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [agent_get_avoidance_mask](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_avoidance_mask) ( agent: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [agent_get_avoidance_priority](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_avoidance_priority) ( agent: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [agent_get_height](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_height) ( agent: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [agent_get_map](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_map) ( agent: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [agent_get_max_neighbors](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_max_neighbors) ( agent: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [agent_get_max_speed](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_max_speed) ( agent: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [agent_get_neighbor_distance](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_neighbor_distance) ( agent: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [agent_get_paused](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_paused) ( agent: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [agent_get_position](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_position) ( agent: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [agent_get_radius](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_radius) ( agent: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [agent_get_time_horizon_agents](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_time_horizon_agents) ( agent: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [agent_get_time_horizon_obstacles](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_time_horizon_obstacles) ( agent: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [agent_get_use_3d_avoidance](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_use_3d_avoidance) ( agent: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [agent_get_velocity](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_velocity) ( agent: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [agent_has_avoidance_callback](class_navigationserver3d.md#class_NavigationServer3D_method_agent_has_avoidance_callback) ( agent: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [agent_is_map_changed](class_navigationserver3d.md#class_NavigationServer3D_method_agent_is_map_changed) ( agent: [RID](class_rid.md#class_RID) ) const |
| void | [agent_set_avoidance_callback](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_callback) ( agent: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) |
| void | [agent_set_avoidance_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_enabled) ( agent: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [agent_set_avoidance_layers](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_layers) ( agent: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) |
| void | [agent_set_avoidance_mask](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_mask) ( agent: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [agent_set_avoidance_priority](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_priority) ( agent: [RID](class_rid.md#class_RID), priority: [float](class_float.md#class_float) ) |
| void | [agent_set_height](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_height) ( agent: [RID](class_rid.md#class_RID), height: [float](class_float.md#class_float) ) |
| void | [agent_set_map](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_map) ( agent: [RID](class_rid.md#class_RID), map: [RID](class_rid.md#class_RID) ) |
| void | [agent_set_max_neighbors](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_max_neighbors) ( agent: [RID](class_rid.md#class_RID), count: [int](class_int.md#class_int) ) |
| void | [agent_set_max_speed](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_max_speed) ( agent: [RID](class_rid.md#class_RID), max_speed: [float](class_float.md#class_float) ) |
| void | [agent_set_neighbor_distance](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_neighbor_distance) ( agent: [RID](class_rid.md#class_RID), distance: [float](class_float.md#class_float) ) |
| void | [agent_set_paused](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_paused) ( agent: [RID](class_rid.md#class_RID), paused: [bool](class_bool.md#class_bool) ) |
| void | [agent_set_position](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_position) ( agent: [RID](class_rid.md#class_RID), position: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [agent_set_radius](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_radius) ( agent: [RID](class_rid.md#class_RID), radius: [float](class_float.md#class_float) ) |
| void | [agent_set_time_horizon_agents](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_time_horizon_agents) ( agent: [RID](class_rid.md#class_RID), time_horizon: [float](class_float.md#class_float) ) |
| void | [agent_set_time_horizon_obstacles](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_time_horizon_obstacles) ( agent: [RID](class_rid.md#class_RID), time_horizon: [float](class_float.md#class_float) ) |
| void | [agent_set_use_3d_avoidance](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_use_3d_avoidance) ( agent: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [agent_set_velocity](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_velocity) ( agent: [RID](class_rid.md#class_RID), velocity: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [agent_set_velocity_forced](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_velocity_forced) ( agent: [RID](class_rid.md#class_RID), velocity: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [bake_from_source_geometry_data](class_navigationserver3d.md#class_NavigationServer3D_method_bake_from_source_geometry_data) ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D), callback: [Callable](class_callable.md#class_Callable) = Callable() ) |
| void | [bake_from_source_geometry_data_async](class_navigationserver3d.md#class_NavigationServer3D_method_bake_from_source_geometry_data_async) ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D), callback: [Callable](class_callable.md#class_Callable) = Callable() ) |
| void | [free_rid](class_navigationserver3d.md#class_NavigationServer3D_method_free_rid) ( rid: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [get_debug_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_get_debug_enabled) ( ) const |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [get_maps](class_navigationserver3d.md#class_NavigationServer3D_method_get_maps) ( ) const |
| [int](class_int.md#class_int) | [get_process_info](class_navigationserver3d.md#class_NavigationServer3D_method_get_process_info) ( process_info: [ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) ) const |
| [bool](class_bool.md#class_bool) | [is_baking_navigation_mesh](class_navigationserver3d.md#class_NavigationServer3D_method_is_baking_navigation_mesh) ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) ) const |
| [RID](class_rid.md#class_RID) | [link_create](class_navigationserver3d.md#class_NavigationServer3D_method_link_create) ( ) |
| [bool](class_bool.md#class_bool) | [link_get_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_enabled) ( link: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [link_get_end_position](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_end_position) ( link: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [link_get_enter_cost](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_enter_cost) ( link: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [link_get_iteration_id](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_iteration_id) ( link: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [link_get_map](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_map) ( link: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [link_get_navigation_layers](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_navigation_layers) ( link: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [link_get_owner_id](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_owner_id) ( link: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [link_get_start_position](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_start_position) ( link: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [link_get_travel_cost](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_travel_cost) ( link: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [link_is_bidirectional](class_navigationserver3d.md#class_NavigationServer3D_method_link_is_bidirectional) ( link: [RID](class_rid.md#class_RID) ) const |
| void | [link_set_bidirectional](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_bidirectional) ( link: [RID](class_rid.md#class_RID), bidirectional: [bool](class_bool.md#class_bool) ) |
| void | [link_set_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_enabled) ( link: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [link_set_end_position](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_end_position) ( link: [RID](class_rid.md#class_RID), position: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [link_set_enter_cost](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_enter_cost) ( link: [RID](class_rid.md#class_RID), enter_cost: [float](class_float.md#class_float) ) |
| void | [link_set_map](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_map) ( link: [RID](class_rid.md#class_RID), map: [RID](class_rid.md#class_RID) ) |
| void | [link_set_navigation_layers](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_navigation_layers) ( link: [RID](class_rid.md#class_RID), navigation_layers: [int](class_int.md#class_int) ) |
| void | [link_set_owner_id](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_owner_id) ( link: [RID](class_rid.md#class_RID), owner_id: [int](class_int.md#class_int) ) |
| void | [link_set_start_position](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_start_position) ( link: [RID](class_rid.md#class_RID), position: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [link_set_travel_cost](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_travel_cost) ( link: [RID](class_rid.md#class_RID), travel_cost: [float](class_float.md#class_float) ) |
| [RID](class_rid.md#class_RID) | [map_create](class_navigationserver3d.md#class_NavigationServer3D_method_map_create) ( ) |
| void | [map_force_update](class_navigationserver3d.md#class_NavigationServer3D_method_map_force_update) ( map: [RID](class_rid.md#class_RID) ) |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [map_get_agents](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_agents) ( map: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [map_get_cell_height](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_cell_height) ( map: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [map_get_cell_size](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_cell_size) ( map: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [map_get_closest_point](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_closest_point) ( map: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [map_get_closest_point_normal](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_closest_point_normal) ( map: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [RID](class_rid.md#class_RID) | [map_get_closest_point_owner](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_closest_point_owner) ( map: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [map_get_closest_point_to_segment](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_closest_point_to_segment) ( map: [RID](class_rid.md#class_RID), start: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3), use_collision: [bool](class_bool.md#class_bool) = false ) const |
| [float](class_float.md#class_float) | [map_get_edge_connection_margin](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_edge_connection_margin) ( map: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [map_get_iteration_id](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_iteration_id) ( map: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [map_get_link_connection_radius](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_link_connection_radius) ( map: [RID](class_rid.md#class_RID) ) const |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [map_get_links](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_links) ( map: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [map_get_merge_rasterizer_cell_scale](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_merge_rasterizer_cell_scale) ( map: [RID](class_rid.md#class_RID) ) const |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [map_get_obstacles](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_obstacles) ( map: [RID](class_rid.md#class_RID) ) const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [map_get_path](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_path) ( map: [RID](class_rid.md#class_RID), origin: [Vector3](class_vector3.md#class_Vector3), destination: [Vector3](class_vector3.md#class_Vector3), optimize: [bool](class_bool.md#class_bool), navigation_layers: [int](class_int.md#class_int) = 1 ) |
| [Vector3](class_vector3.md#class_Vector3) | [map_get_random_point](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_random_point) ( map: [RID](class_rid.md#class_RID), navigation_layers: [int](class_int.md#class_int), uniformly: [bool](class_bool.md#class_bool) ) const |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [map_get_regions](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_regions) ( map: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [map_get_up](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_up) ( map: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [map_get_use_async_iterations](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_use_async_iterations) ( map: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [map_get_use_edge_connections](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_use_edge_connections) ( map: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [map_is_active](class_navigationserver3d.md#class_NavigationServer3D_method_map_is_active) ( map: [RID](class_rid.md#class_RID) ) const |
| void | [map_set_active](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_active) ( map: [RID](class_rid.md#class_RID), active: [bool](class_bool.md#class_bool) ) |
| void | [map_set_cell_height](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_cell_height) ( map: [RID](class_rid.md#class_RID), cell_height: [float](class_float.md#class_float) ) |
| void | [map_set_cell_size](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_cell_size) ( map: [RID](class_rid.md#class_RID), cell_size: [float](class_float.md#class_float) ) |
| void | [map_set_edge_connection_margin](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_edge_connection_margin) ( map: [RID](class_rid.md#class_RID), margin: [float](class_float.md#class_float) ) |
| void | [map_set_link_connection_radius](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_link_connection_radius) ( map: [RID](class_rid.md#class_RID), radius: [float](class_float.md#class_float) ) |
| void | [map_set_merge_rasterizer_cell_scale](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_merge_rasterizer_cell_scale) ( map: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) |
| void | [map_set_up](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_up) ( map: [RID](class_rid.md#class_RID), up: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [map_set_use_async_iterations](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_use_async_iterations) ( map: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [map_set_use_edge_connections](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_use_edge_connections) ( map: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| [RID](class_rid.md#class_RID) | [obstacle_create](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_create) ( ) |
| [bool](class_bool.md#class_bool) | [obstacle_get_avoidance_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_avoidance_enabled) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [obstacle_get_avoidance_layers](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_avoidance_layers) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [obstacle_get_height](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_height) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [obstacle_get_map](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_map) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [obstacle_get_paused](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_paused) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [obstacle_get_position](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_position) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [obstacle_get_radius](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_radius) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [obstacle_get_use_3d_avoidance](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_use_3d_avoidance) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [obstacle_get_velocity](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_velocity) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [obstacle_get_vertices](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_vertices) ( obstacle: [RID](class_rid.md#class_RID) ) const |
| void | [obstacle_set_avoidance_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_avoidance_enabled) ( obstacle: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [obstacle_set_avoidance_layers](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_avoidance_layers) ( obstacle: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) |
| void | [obstacle_set_height](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_height) ( obstacle: [RID](class_rid.md#class_RID), height: [float](class_float.md#class_float) ) |
| void | [obstacle_set_map](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_map) ( obstacle: [RID](class_rid.md#class_RID), map: [RID](class_rid.md#class_RID) ) |
| void | [obstacle_set_paused](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_paused) ( obstacle: [RID](class_rid.md#class_RID), paused: [bool](class_bool.md#class_bool) ) |
| void | [obstacle_set_position](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_position) ( obstacle: [RID](class_rid.md#class_RID), position: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [obstacle_set_radius](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_radius) ( obstacle: [RID](class_rid.md#class_RID), radius: [float](class_float.md#class_float) ) |
| void | [obstacle_set_use_3d_avoidance](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_use_3d_avoidance) ( obstacle: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [obstacle_set_velocity](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_velocity) ( obstacle: [RID](class_rid.md#class_RID), velocity: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [obstacle_set_vertices](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_vertices) ( obstacle: [RID](class_rid.md#class_RID), vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) |
| void | [parse_source_geometry_data](class_navigationserver3d.md#class_NavigationServer3D_method_parse_source_geometry_data) ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D), root_node: [Node](class_node.md#class_Node), callback: [Callable](class_callable.md#class_Callable) = Callable() ) |
| void | [query_path](class_navigationserver3d.md#class_NavigationServer3D_method_query_path) ( parameters: [NavigationPathQueryParameters3D](class_navigationpathqueryparameters3d.md#class_NavigationPathQueryParameters3D), result: [NavigationPathQueryResult3D](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D), callback: [Callable](class_callable.md#class_Callable) = Callable() ) |
| void | [region_bake_navigation_mesh](class_navigationserver3d.md#class_NavigationServer3D_method_region_bake_navigation_mesh) ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh), root_node: [Node](class_node.md#class_Node) ) |
| [RID](class_rid.md#class_RID) | [region_create](class_navigationserver3d.md#class_NavigationServer3D_method_region_create) ( ) |
| [AABB](class_aabb.md#class_AABB) | [region_get_bounds](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_bounds) ( region: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [region_get_closest_point](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_closest_point) ( region: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [region_get_closest_point_normal](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_closest_point_normal) ( region: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [region_get_closest_point_to_segment](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_closest_point_to_segment) ( region: [RID](class_rid.md#class_RID), start: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3), use_collision: [bool](class_bool.md#class_bool) = false ) const |
| [Vector3](class_vector3.md#class_Vector3) | [region_get_connection_pathway_end](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_connection_pathway_end) ( region: [RID](class_rid.md#class_RID), connection: [int](class_int.md#class_int) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [region_get_connection_pathway_start](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_connection_pathway_start) ( region: [RID](class_rid.md#class_RID), connection: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [region_get_connections_count](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_connections_count) ( region: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [region_get_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_enabled) ( region: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [region_get_enter_cost](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_enter_cost) ( region: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [region_get_iteration_id](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_iteration_id) ( region: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [region_get_map](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_map) ( region: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [region_get_navigation_layers](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_navigation_layers) ( region: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [region_get_owner_id](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_owner_id) ( region: [RID](class_rid.md#class_RID) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [region_get_random_point](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_random_point) ( region: [RID](class_rid.md#class_RID), navigation_layers: [int](class_int.md#class_int), uniformly: [bool](class_bool.md#class_bool) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [region_get_transform](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_transform) ( region: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [region_get_travel_cost](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_travel_cost) ( region: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [region_get_use_async_iterations](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_use_async_iterations) ( region: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [region_get_use_edge_connections](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_use_edge_connections) ( region: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [region_owns_point](class_navigationserver3d.md#class_NavigationServer3D_method_region_owns_point) ( region: [RID](class_rid.md#class_RID), point: [Vector3](class_vector3.md#class_Vector3) ) const |
| void | [region_set_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_enabled) ( region: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [region_set_enter_cost](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_enter_cost) ( region: [RID](class_rid.md#class_RID), enter_cost: [float](class_float.md#class_float) ) |
| void | [region_set_map](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_map) ( region: [RID](class_rid.md#class_RID), map: [RID](class_rid.md#class_RID) ) |
| void | [region_set_navigation_layers](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_navigation_layers) ( region: [RID](class_rid.md#class_RID), navigation_layers: [int](class_int.md#class_int) ) |
| void | [region_set_navigation_mesh](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_navigation_mesh) ( region: [RID](class_rid.md#class_RID), navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) ) |
| void | [region_set_owner_id](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_owner_id) ( region: [RID](class_rid.md#class_RID), owner_id: [int](class_int.md#class_int) ) |
| void | [region_set_transform](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_transform) ( region: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [region_set_travel_cost](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_travel_cost) ( region: [RID](class_rid.md#class_RID), travel_cost: [float](class_float.md#class_float) ) |
| void | [region_set_use_async_iterations](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_use_async_iterations) ( region: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [region_set_use_edge_connections](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_use_edge_connections) ( region: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_active](class_navigationserver3d.md#class_NavigationServer3D_method_set_active) ( active: [bool](class_bool.md#class_bool) ) |
| void | [set_debug_enabled](class_navigationserver3d.md#class_NavigationServer3D_method_set_debug_enabled) ( enabled: [bool](class_bool.md#class_bool) ) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [simplify_path](class_navigationserver3d.md#class_NavigationServer3D_method_simplify_path) ( path: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), epsilon: [float](class_float.md#class_float) ) |
| [RID](class_rid.md#class_RID) | [source_geometry_parser_create](class_navigationserver3d.md#class_NavigationServer3D_method_source_geometry_parser_create) ( ) |
| void | [source_geometry_parser_set_callback](class_navigationserver3d.md#class_NavigationServer3D_method_source_geometry_parser_set_callback) ( parser: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) |

---

### Signals

<span id="class_NavigationServer3D_signal_avoidance_debug_changed"></span>

**avoidance_debug_changed** ( ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_signal_avoidance_debug_changed)

Emitted when avoidance debug settings are changed. Only available in debug builds.

---

<span id="class_NavigationServer3D_signal_map_changed"></span>

**map_changed** ( map: [RID](class_rid.md#class_RID) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_signal_map_changed)

Emitted when a navigation map is updated, when a region moves or is modified.

---

<span id="class_NavigationServer3D_signal_navigation_debug_changed"></span>

**navigation_debug_changed** ( ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_signal_navigation_debug_changed)

Emitted when navigation debug settings are changed. Only available in debug builds.

---

### Enumerations

<span id="enum_NavigationServer3D_ProcessInfo"></span>

enum **ProcessInfo**: [🔗](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo)

<span id="class_NavigationServer3D_constant_INFO_ACTIVE_MAPS"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_ACTIVE_MAPS** = `0`

Constant to get the number of active navigation maps.

<span id="class_NavigationServer3D_constant_INFO_REGION_COUNT"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_REGION_COUNT** = `1`

Constant to get the number of active navigation regions.

<span id="class_NavigationServer3D_constant_INFO_AGENT_COUNT"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_AGENT_COUNT** = `2`

Constant to get the number of active navigation agents processing avoidance.

<span id="class_NavigationServer3D_constant_INFO_LINK_COUNT"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_LINK_COUNT** = `3`

Constant to get the number of active navigation links.

<span id="class_NavigationServer3D_constant_INFO_POLYGON_COUNT"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_POLYGON_COUNT** = `4`

Constant to get the number of navigation mesh polygons.

<span id="class_NavigationServer3D_constant_INFO_EDGE_COUNT"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_EDGE_COUNT** = `5`

Constant to get the number of navigation mesh polygon edges.

<span id="class_NavigationServer3D_constant_INFO_EDGE_MERGE_COUNT"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_EDGE_MERGE_COUNT** = `6`

Constant to get the number of navigation mesh polygon edges that were merged due to edge key overlap.

<span id="class_NavigationServer3D_constant_INFO_EDGE_CONNECTION_COUNT"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_EDGE_CONNECTION_COUNT** = `7`

Constant to get the number of navigation mesh polygon edges that are considered connected by edge proximity.

<span id="class_NavigationServer3D_constant_INFO_EDGE_FREE_COUNT"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_EDGE_FREE_COUNT** = `8`

Constant to get the number of navigation mesh polygon edges that could not be merged but may be still connected by edge proximity or with links.

<span id="class_NavigationServer3D_constant_INFO_OBSTACLE_COUNT"></span>

[ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) **INFO_OBSTACLE_COUNT** = `9`

Constant to get the number of active navigation obstacles.

---

### Method Descriptions

<span id="class_NavigationServer3D_method_agent_create"></span>

[RID](class_rid.md#class_RID) **agent_create** ( ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_create)

Creates the agent.

---

<span id="class_NavigationServer3D_method_agent_get_avoidance_enabled"></span>

[bool](class_bool.md#class_bool) **agent_get_avoidance_enabled** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_avoidance_enabled)

Returns `true` if the provided `agent` has avoidance enabled.

---

<span id="class_NavigationServer3D_method_agent_get_avoidance_layers"></span>

[int](class_int.md#class_int) **agent_get_avoidance_layers** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_avoidance_layers)

Returns the `avoidance_layers` bitmask of the specified `agent`.

---

<span id="class_NavigationServer3D_method_agent_get_avoidance_mask"></span>

[int](class_int.md#class_int) **agent_get_avoidance_mask** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_avoidance_mask)

Returns the `avoidance_mask` bitmask of the specified `agent`.

---

<span id="class_NavigationServer3D_method_agent_get_avoidance_priority"></span>

[float](class_float.md#class_float) **agent_get_avoidance_priority** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_avoidance_priority)

Returns the `avoidance_priority` of the specified `agent`.

---

<span id="class_NavigationServer3D_method_agent_get_height"></span>

[float](class_float.md#class_float) **agent_get_height** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_height)

Returns the `height` of the specified `agent`.

---

<span id="class_NavigationServer3D_method_agent_get_map"></span>

[RID](class_rid.md#class_RID) **agent_get_map** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_map)

Returns the navigation map [RID](class_rid.md#class_RID) the requested `agent` is currently assigned to.

---

<span id="class_NavigationServer3D_method_agent_get_max_neighbors"></span>

[int](class_int.md#class_int) **agent_get_max_neighbors** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_max_neighbors)

Returns the maximum number of other agents the specified `agent` takes into account in the navigation.

---

<span id="class_NavigationServer3D_method_agent_get_max_speed"></span>

[float](class_float.md#class_float) **agent_get_max_speed** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_max_speed)

Returns the maximum speed of the specified `agent`.

---

<span id="class_NavigationServer3D_method_agent_get_neighbor_distance"></span>

[float](class_float.md#class_float) **agent_get_neighbor_distance** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_neighbor_distance)

Returns the maximum distance to other agents the specified `agent` takes into account in the navigation.

---

<span id="class_NavigationServer3D_method_agent_get_paused"></span>

[bool](class_bool.md#class_bool) **agent_get_paused** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_paused)

Returns `true` if the specified `agent` is paused.

---

<span id="class_NavigationServer3D_method_agent_get_position"></span>

[Vector3](class_vector3.md#class_Vector3) **agent_get_position** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_position)

Returns the position of the specified `agent` in world space.

---

<span id="class_NavigationServer3D_method_agent_get_radius"></span>

[float](class_float.md#class_float) **agent_get_radius** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_radius)

Returns the radius of the specified `agent`.

---

<span id="class_NavigationServer3D_method_agent_get_time_horizon_agents"></span>

[float](class_float.md#class_float) **agent_get_time_horizon_agents** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_time_horizon_agents)

Returns the minimal amount of time for which the specified `agent`'s velocities that are computed by the simulation are safe with respect to other agents.

---

<span id="class_NavigationServer3D_method_agent_get_time_horizon_obstacles"></span>

[float](class_float.md#class_float) **agent_get_time_horizon_obstacles** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_time_horizon_obstacles)

Returns the minimal amount of time for which the specified `agent`'s velocities that are computed by the simulation are safe with respect to static avoidance obstacles.

---

<span id="class_NavigationServer3D_method_agent_get_use_3d_avoidance"></span>

[bool](class_bool.md#class_bool) **agent_get_use_3d_avoidance** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_use_3d_avoidance)

Returns `true` if the provided `agent` uses avoidance in 3D space Vector3(x,y,z) instead of horizontal 2D Vector2(x,y) / Vector3(x,0.0,z).

---

<span id="class_NavigationServer3D_method_agent_get_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **agent_get_velocity** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_get_velocity)

Returns the velocity of the specified `agent`.

---

<span id="class_NavigationServer3D_method_agent_has_avoidance_callback"></span>

[bool](class_bool.md#class_bool) **agent_has_avoidance_callback** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_has_avoidance_callback)

Return `true` if the specified `agent` has an avoidance callback.

---

<span id="class_NavigationServer3D_method_agent_is_map_changed"></span>

[bool](class_bool.md#class_bool) **agent_is_map_changed** ( agent: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_is_map_changed)

Returns `true` if the map got changed the previous frame.

---

<span id="class_NavigationServer3D_method_agent_set_avoidance_callback"></span>

void **agent_set_avoidance_callback** ( agent: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_callback)

Sets the callback [Callable](class_callable.md#class_Callable) that gets called after each avoidance processing step for the `agent`. The calculated `safe_velocity` will be dispatched with a signal to the object just before the physics calculations.

 **Note:** Created callbacks are always processed independently of the SceneTree state as long as the agent is on a navigation map and not freed. To disable the dispatch of a callback from an agent use [agent_set_avoidance_callback()](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_callback) again with an empty [Callable](class_callable.md#class_Callable).

---

<span id="class_NavigationServer3D_method_agent_set_avoidance_enabled"></span>

void **agent_set_avoidance_enabled** ( agent: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_enabled)

If `enabled` is `true`, the provided `agent` calculates avoidance.

---

<span id="class_NavigationServer3D_method_agent_set_avoidance_layers"></span>

void **agent_set_avoidance_layers** ( agent: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_layers)

Set the agent's `avoidance_layers` bitmask.

---

<span id="class_NavigationServer3D_method_agent_set_avoidance_mask"></span>

void **agent_set_avoidance_mask** ( agent: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_mask)

Set the agent's `avoidance_mask` bitmask.

---

<span id="class_NavigationServer3D_method_agent_set_avoidance_priority"></span>

void **agent_set_avoidance_priority** ( agent: [RID](class_rid.md#class_RID), priority: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_avoidance_priority)

Set the agent's `avoidance_priority` with a `priority` between 0.0 (lowest priority) to 1.0 (highest priority).

The specified `agent` does not adjust the velocity for other agents that would match the `avoidance_mask` but have a lower `avoidance_priority`. This in turn makes the other agents with lower priority adjust their velocities even more to avoid collision with this agent.

---

<span id="class_NavigationServer3D_method_agent_set_height"></span>

void **agent_set_height** ( agent: [RID](class_rid.md#class_RID), height: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_height)

Updates the provided `agent` `height`.

---

<span id="class_NavigationServer3D_method_agent_set_map"></span>

void **agent_set_map** ( agent: [RID](class_rid.md#class_RID), map: [RID](class_rid.md#class_RID) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_map)

Puts the agent in the map.

---

<span id="class_NavigationServer3D_method_agent_set_max_neighbors"></span>

void **agent_set_max_neighbors** ( agent: [RID](class_rid.md#class_RID), count: [int](class_int.md#class_int) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_max_neighbors)

Sets the maximum number of other agents the agent takes into account in the navigation. The larger this number, the longer the running time of the simulation. If the number is too low, the simulation will not be safe.

---

<span id="class_NavigationServer3D_method_agent_set_max_speed"></span>

void **agent_set_max_speed** ( agent: [RID](class_rid.md#class_RID), max_speed: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_max_speed)

Sets the maximum speed of the agent. Must be positive.

---

<span id="class_NavigationServer3D_method_agent_set_neighbor_distance"></span>

void **agent_set_neighbor_distance** ( agent: [RID](class_rid.md#class_RID), distance: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_neighbor_distance)

Sets the maximum distance to other agents this agent takes into account in the navigation. The larger this number, the longer the running time of the simulation. If the number is too low, the simulation will not be safe.

---

<span id="class_NavigationServer3D_method_agent_set_paused"></span>

void **agent_set_paused** ( agent: [RID](class_rid.md#class_RID), paused: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_paused)

If `paused` is `true` the specified `agent` will not be processed. For example, it will not calculate avoidance velocities or receive avoidance callbacks.

---

<span id="class_NavigationServer3D_method_agent_set_position"></span>

void **agent_set_position** ( agent: [RID](class_rid.md#class_RID), position: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_position)

Sets the position of the agent in world space.

---

<span id="class_NavigationServer3D_method_agent_set_radius"></span>

void **agent_set_radius** ( agent: [RID](class_rid.md#class_RID), radius: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_radius)

Sets the radius of the agent.

---

<span id="class_NavigationServer3D_method_agent_set_time_horizon_agents"></span>

void **agent_set_time_horizon_agents** ( agent: [RID](class_rid.md#class_RID), time_horizon: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_time_horizon_agents)

The minimal amount of time for which the agent's velocities that are computed by the simulation are safe with respect to other agents. The larger this number, the sooner this agent will respond to the presence of other agents, but the less freedom this agent has in choosing its velocities. A too high value will slow down agents movement considerably. Must be positive.

---

<span id="class_NavigationServer3D_method_agent_set_time_horizon_obstacles"></span>

void **agent_set_time_horizon_obstacles** ( agent: [RID](class_rid.md#class_RID), time_horizon: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_time_horizon_obstacles)

The minimal amount of time for which the agent's velocities that are computed by the simulation are safe with respect to static avoidance obstacles. The larger this number, the sooner this agent will respond to the presence of static avoidance obstacles, but the less freedom this agent has in choosing its velocities. A too high value will slow down agents movement considerably. Must be positive.

---

<span id="class_NavigationServer3D_method_agent_set_use_3d_avoidance"></span>

void **agent_set_use_3d_avoidance** ( agent: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_use_3d_avoidance)

Sets if the agent uses the 2D avoidance or the 3D avoidance while avoidance is enabled.

If `true` the agent calculates avoidance velocities in 3D for the xyz-axis, e.g. for games that take place in air, underwater or space. The 3D using agent only avoids other 3D avoidance using agent's. The 3D using agent only reacts to radius based avoidance obstacles. The 3D using agent ignores any vertices based obstacles. The 3D using agent only avoids other 3D using agent's.

If `false` the agent calculates avoidance velocities in 2D along the xz-axis ignoring the y-axis. The 2D using agent only avoids other 2D avoidance using agent's. The 2D using agent reacts to radius avoidance obstacles. The 2D using agent reacts to vertices based avoidance obstacles. The 2D using agent only avoids other 2D using agent's. 2D using agents will ignore other 2D using agents or obstacles that are below their current position or above their current position including the agents height in 2D avoidance.

---

<span id="class_NavigationServer3D_method_agent_set_velocity"></span>

void **agent_set_velocity** ( agent: [RID](class_rid.md#class_RID), velocity: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_velocity)

Sets `velocity` as the new wanted velocity for the specified `agent`. The avoidance simulation will try to fulfill this velocity if possible but will modify it to avoid collision with other agent's and obstacles. When an agent is teleported to a new position use [agent_set_velocity_forced()](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_velocity_forced) as well to reset the internal simulation velocity.

---

<span id="class_NavigationServer3D_method_agent_set_velocity_forced"></span>

void **agent_set_velocity_forced** ( agent: [RID](class_rid.md#class_RID), velocity: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_agent_set_velocity_forced)

Replaces the internal velocity in the collision avoidance simulation with `velocity` for the specified `agent`. When an agent is teleported to a new position this function should be used in the same frame. If called frequently this function can get agents stuck.

---

<span id="class_NavigationServer3D_method_bake_from_source_geometry_data"></span>

void **bake_from_source_geometry_data** ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D), callback: [Callable](class_callable.md#class_Callable) = Callable() ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_bake_from_source_geometry_data)

Bakes the provided `navigation_mesh` with the data from the provided `source_geometry_data`. After the process is finished the optional `callback` will be called.

---

<span id="class_NavigationServer3D_method_bake_from_source_geometry_data_async"></span>

void **bake_from_source_geometry_data_async** ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D), callback: [Callable](class_callable.md#class_Callable) = Callable() ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_bake_from_source_geometry_data_async)

Bakes the provided `navigation_mesh` with the data from the provided `source_geometry_data` as an async task running on a background thread. After the process is finished the optional `callback` will be called.

---

<span id="class_NavigationServer3D_method_free_rid"></span>

void **free_rid** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_free_rid)

Destroys the given RID.

---

<span id="class_NavigationServer3D_method_get_debug_enabled"></span>

[bool](class_bool.md#class_bool) **get_debug_enabled** ( ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_get_debug_enabled)

Returns `true` when the NavigationServer has debug enabled.

---

<span id="class_NavigationServer3D_method_get_maps"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **get_maps** ( ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_get_maps)

Returns all created navigation map [RID](class_rid.md#class_RID) s on the NavigationServer. This returns both 2D and 3D created navigation maps as there is technically no distinction between them.

---

<span id="class_NavigationServer3D_method_get_process_info"></span>

[int](class_int.md#class_int) **get_process_info** ( process_info: [ProcessInfo](class_navigationserver3d.md#enum_NavigationServer3D_ProcessInfo) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_get_process_info)

Returns information about the current state of the NavigationServer.

---

<span id="class_NavigationServer3D_method_is_baking_navigation_mesh"></span>

[bool](class_bool.md#class_bool) **is_baking_navigation_mesh** ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_is_baking_navigation_mesh)

Returns `true` when the provided navigation mesh is being baked on a background thread.

---

<span id="class_NavigationServer3D_method_link_create"></span>

[RID](class_rid.md#class_RID) **link_create** ( ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_create)

Create a new link between two positions on a map.

---

<span id="class_NavigationServer3D_method_link_get_enabled"></span>

[bool](class_bool.md#class_bool) **link_get_enabled** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_enabled)

Returns `true` if the specified `link` is enabled.

---

<span id="class_NavigationServer3D_method_link_get_end_position"></span>

[Vector3](class_vector3.md#class_Vector3) **link_get_end_position** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_end_position)

Returns the ending position of this `link`.

---

<span id="class_NavigationServer3D_method_link_get_enter_cost"></span>

[float](class_float.md#class_float) **link_get_enter_cost** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_enter_cost)

Returns the enter cost of this `link`.

---

<span id="class_NavigationServer3D_method_link_get_iteration_id"></span>

[int](class_int.md#class_int) **link_get_iteration_id** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_iteration_id)

Returns the current iteration ID of the navigation link. Every time the navigation link changes and synchronizes, the iteration ID increases. An iteration ID of `0` means the navigation link has never synchronized.

 **Note:** The iteration ID will wrap around to `1` after reaching its range limit.

---

<span id="class_NavigationServer3D_method_link_get_map"></span>

[RID](class_rid.md#class_RID) **link_get_map** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_map)

Returns the navigation map [RID](class_rid.md#class_RID) the requested `link` is currently assigned to.

---

<span id="class_NavigationServer3D_method_link_get_navigation_layers"></span>

[int](class_int.md#class_int) **link_get_navigation_layers** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_navigation_layers)

Returns the navigation layers for this `link`.

---

<span id="class_NavigationServer3D_method_link_get_owner_id"></span>

[int](class_int.md#class_int) **link_get_owner_id** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_owner_id)

Returns the `ObjectID` of the object which manages this link.

---

<span id="class_NavigationServer3D_method_link_get_start_position"></span>

[Vector3](class_vector3.md#class_Vector3) **link_get_start_position** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_start_position)

Returns the starting position of this `link`.

---

<span id="class_NavigationServer3D_method_link_get_travel_cost"></span>

[float](class_float.md#class_float) **link_get_travel_cost** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_get_travel_cost)

Returns the travel cost of this `link`.

---

<span id="class_NavigationServer3D_method_link_is_bidirectional"></span>

[bool](class_bool.md#class_bool) **link_is_bidirectional** ( link: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_is_bidirectional)

Returns whether this `link` can be travelled in both directions.

---

<span id="class_NavigationServer3D_method_link_set_bidirectional"></span>

void **link_set_bidirectional** ( link: [RID](class_rid.md#class_RID), bidirectional: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_bidirectional)

Sets whether this `link` can be travelled in both directions.

---

<span id="class_NavigationServer3D_method_link_set_enabled"></span>

void **link_set_enabled** ( link: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_enabled)

If `enabled` is `true`, the specified `link` will contribute to its current navigation map.

---

<span id="class_NavigationServer3D_method_link_set_end_position"></span>

void **link_set_end_position** ( link: [RID](class_rid.md#class_RID), position: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_end_position)

Sets the exit position for the `link`.

---

<span id="class_NavigationServer3D_method_link_set_enter_cost"></span>

void **link_set_enter_cost** ( link: [RID](class_rid.md#class_RID), enter_cost: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_enter_cost)

Sets the `enter_cost` for this `link`.

---

<span id="class_NavigationServer3D_method_link_set_map"></span>

void **link_set_map** ( link: [RID](class_rid.md#class_RID), map: [RID](class_rid.md#class_RID) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_map)

Sets the navigation map [RID](class_rid.md#class_RID) for the link.

---

<span id="class_NavigationServer3D_method_link_set_navigation_layers"></span>

void **link_set_navigation_layers** ( link: [RID](class_rid.md#class_RID), navigation_layers: [int](class_int.md#class_int) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_navigation_layers)

Set the links's navigation layers. This allows selecting links from a path request (when using [map_get_path()](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_path)).

---

<span id="class_NavigationServer3D_method_link_set_owner_id"></span>

void **link_set_owner_id** ( link: [RID](class_rid.md#class_RID), owner_id: [int](class_int.md#class_int) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_owner_id)

Set the `ObjectID` of the object which manages this link.

---

<span id="class_NavigationServer3D_method_link_set_start_position"></span>

void **link_set_start_position** ( link: [RID](class_rid.md#class_RID), position: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_start_position)

Sets the entry position for this `link`.

---

<span id="class_NavigationServer3D_method_link_set_travel_cost"></span>

void **link_set_travel_cost** ( link: [RID](class_rid.md#class_RID), travel_cost: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_link_set_travel_cost)

Sets the `travel_cost` for this `link`.

---

<span id="class_NavigationServer3D_method_map_create"></span>

[RID](class_rid.md#class_RID) **map_create** ( ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_create)

Create a new map.

---

<span id="class_NavigationServer3D_method_map_force_update"></span>

void **map_force_update** ( map: [RID](class_rid.md#class_RID) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_force_update)

**Deprecated:** This method is no longer supported, as it is incompatible with asynchronous updates. It can only be used in a single-threaded context, at your own risk.

This function immediately forces synchronization of the specified navigation `map` [RID](class_rid.md#class_RID). By default navigation maps are only synchronized at the end of each physics frame. This function can be used to immediately (re)calculate all the navigation meshes and region connections of the navigation map. This makes it possible to query a navigation path for a changed map immediately and in the same frame (multiple times if needed).

Due to technical restrictions the current NavigationServer command queue will be flushed. This means all already queued update commands for this physics frame will be executed, even those intended for other maps, regions and agents not part of the specified map. The expensive computation of the navigation meshes and region connections of a map will only be done for the specified map. Other maps will receive the normal synchronization at the end of the physics frame. Should the specified map receive changes after the forced update it will update again as well when the other maps receive their update.

Avoidance processing and dispatch of the `safe_velocity` signals is unaffected by this function and continues to happen for all maps and agents at the end of the physics frame.

 **Note:** With great power comes great responsibility. This function should only be used by users that really know what they are doing and have a good reason for it. Forcing an immediate update of a navigation map requires locking the NavigationServer and flushing the entire NavigationServer command queue. Not only can this severely impact the performance of a game but it can also introduce bugs if used inappropriately without much foresight.

---

<span id="class_NavigationServer3D_method_map_get_agents"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **map_get_agents** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_agents)

Returns all navigation agents [RID](class_rid.md#class_RID) s that are currently assigned to the requested navigation `map`.

---

<span id="class_NavigationServer3D_method_map_get_cell_height"></span>

[float](class_float.md#class_float) **map_get_cell_height** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_cell_height)

Returns the map cell height used to rasterize the navigation mesh vertices on the Y axis.

---

<span id="class_NavigationServer3D_method_map_get_cell_size"></span>

[float](class_float.md#class_float) **map_get_cell_size** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_cell_size)

Returns the map cell size used to rasterize the navigation mesh vertices on the XZ plane.

---

<span id="class_NavigationServer3D_method_map_get_closest_point"></span>

[Vector3](class_vector3.md#class_Vector3) **map_get_closest_point** ( map: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_closest_point)

Returns the navigation mesh surface point closest to the provided `to_point` on the navigation `map`.

---

<span id="class_NavigationServer3D_method_map_get_closest_point_normal"></span>

[Vector3](class_vector3.md#class_Vector3) **map_get_closest_point_normal** ( map: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_closest_point_normal)

Returns the navigation mesh surface normal closest to the provided `to_point` on the navigation `map`.

---

<span id="class_NavigationServer3D_method_map_get_closest_point_owner"></span>

[RID](class_rid.md#class_RID) **map_get_closest_point_owner** ( map: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_closest_point_owner)

Returns the owner region RID for the navigation mesh surface point closest to the provided `to_point` on the navigation `map`.

---

<span id="class_NavigationServer3D_method_map_get_closest_point_to_segment"></span>

[Vector3](class_vector3.md#class_Vector3) **map_get_closest_point_to_segment** ( map: [RID](class_rid.md#class_RID), start: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3), use_collision: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_closest_point_to_segment)

Returns the navigation mesh surface point closest to the provided `start` and `end` segment on the navigation `map`.

If `use_collision` is `true`, a closest point test is only done when the segment intersects with the navigation mesh surface.

---

<span id="class_NavigationServer3D_method_map_get_edge_connection_margin"></span>

[float](class_float.md#class_float) **map_get_edge_connection_margin** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_edge_connection_margin)

Returns the edge connection margin of the map. This distance is the minimum vertex distance needed to connect two edges from different regions.

---

<span id="class_NavigationServer3D_method_map_get_iteration_id"></span>

[int](class_int.md#class_int) **map_get_iteration_id** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_iteration_id)

Returns the current iteration id of the navigation map. Every time the navigation map changes and synchronizes the iteration id increases. An iteration id of 0 means the navigation map has never synchronized.

 **Note:** The iteration id will wrap back to 1 after reaching its range limit.

---

<span id="class_NavigationServer3D_method_map_get_link_connection_radius"></span>

[float](class_float.md#class_float) **map_get_link_connection_radius** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_link_connection_radius)

Returns the link connection radius of the map. This distance is the maximum range any link will search for navigation mesh polygons to connect to.

---

<span id="class_NavigationServer3D_method_map_get_links"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **map_get_links** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_links)

Returns all navigation link [RID](class_rid.md#class_RID) s that are currently assigned to the requested navigation `map`.

---

<span id="class_NavigationServer3D_method_map_get_merge_rasterizer_cell_scale"></span>

[float](class_float.md#class_float) **map_get_merge_rasterizer_cell_scale** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_merge_rasterizer_cell_scale)

Returns map's internal merge rasterizer cell scale.

---

<span id="class_NavigationServer3D_method_map_get_obstacles"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **map_get_obstacles** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_obstacles)

Returns all navigation obstacle [RID](class_rid.md#class_RID) s that are currently assigned to the requested navigation `map`.

---

<span id="class_NavigationServer3D_method_map_get_path"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **map_get_path** ( map: [RID](class_rid.md#class_RID), origin: [Vector3](class_vector3.md#class_Vector3), destination: [Vector3](class_vector3.md#class_Vector3), optimize: [bool](class_bool.md#class_bool), navigation_layers: [int](class_int.md#class_int) = 1 ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_path)

Returns the navigation path to reach the destination from the origin. `navigation_layers` is a bitmask of all region navigation layers that are allowed to be in the path.

---

<span id="class_NavigationServer3D_method_map_get_random_point"></span>

[Vector3](class_vector3.md#class_Vector3) **map_get_random_point** ( map: [RID](class_rid.md#class_RID), navigation_layers: [int](class_int.md#class_int), uniformly: [bool](class_bool.md#class_bool) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_random_point)

Returns a random position picked from all map region polygons with matching `navigation_layers`.

If `uniformly` is `true`, all map regions, polygons, and faces are weighted by their surface area (slower).

If `uniformly` is `false`, just a random region and a random polygon are picked (faster).

---

<span id="class_NavigationServer3D_method_map_get_regions"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **map_get_regions** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_regions)

Returns all navigation regions [RID](class_rid.md#class_RID) s that are currently assigned to the requested navigation `map`.

---

<span id="class_NavigationServer3D_method_map_get_up"></span>

[Vector3](class_vector3.md#class_Vector3) **map_get_up** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_up)

Returns the map's up direction.

---

<span id="class_NavigationServer3D_method_map_get_use_async_iterations"></span>

[bool](class_bool.md#class_bool) **map_get_use_async_iterations** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_use_async_iterations)

Returns `true` if the `map` synchronization uses an async process that runs on a background thread.

---

<span id="class_NavigationServer3D_method_map_get_use_edge_connections"></span>

[bool](class_bool.md#class_bool) **map_get_use_edge_connections** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_use_edge_connections)

Returns `true` if the navigation `map` allows navigation regions to use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

<span id="class_NavigationServer3D_method_map_is_active"></span>

[bool](class_bool.md#class_bool) **map_is_active** ( map: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_is_active)

Returns `true` if the map is active.

---

<span id="class_NavigationServer3D_method_map_set_active"></span>

void **map_set_active** ( map: [RID](class_rid.md#class_RID), active: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_active)

Sets the map active.

---

<span id="class_NavigationServer3D_method_map_set_cell_height"></span>

void **map_set_cell_height** ( map: [RID](class_rid.md#class_RID), cell_height: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_cell_height)

Sets the map cell height used to rasterize the navigation mesh vertices on the Y axis. Must match with the cell height of the used navigation meshes.

---

<span id="class_NavigationServer3D_method_map_set_cell_size"></span>

void **map_set_cell_size** ( map: [RID](class_rid.md#class_RID), cell_size: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_cell_size)

Sets the map cell size used to rasterize the navigation mesh vertices on the XZ plane. Must match with the cell size of the used navigation meshes.

---

<span id="class_NavigationServer3D_method_map_set_edge_connection_margin"></span>

void **map_set_edge_connection_margin** ( map: [RID](class_rid.md#class_RID), margin: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_edge_connection_margin)

Set the map edge connection margin used to weld the compatible region edges.

---

<span id="class_NavigationServer3D_method_map_set_link_connection_radius"></span>

void **map_set_link_connection_radius** ( map: [RID](class_rid.md#class_RID), radius: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_link_connection_radius)

Set the map's link connection radius used to connect links to navigation polygons.

---

<span id="class_NavigationServer3D_method_map_set_merge_rasterizer_cell_scale"></span>

void **map_set_merge_rasterizer_cell_scale** ( map: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_merge_rasterizer_cell_scale)

Set the map's internal merge rasterizer cell scale used to control merging sensitivity.

---

<span id="class_NavigationServer3D_method_map_set_up"></span>

void **map_set_up** ( map: [RID](class_rid.md#class_RID), up: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_up)

Sets the map up direction.

---

<span id="class_NavigationServer3D_method_map_set_use_async_iterations"></span>

void **map_set_use_async_iterations** ( map: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_use_async_iterations)

If `enabled` is `true` the `map` synchronization uses an async process that runs on a background thread.

---

<span id="class_NavigationServer3D_method_map_set_use_edge_connections"></span>

void **map_set_use_edge_connections** ( map: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_use_edge_connections)

Set the navigation `map` edge connection use. If `enabled` is `true`, the navigation map allows navigation regions to use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

<span id="class_NavigationServer3D_method_obstacle_create"></span>

[RID](class_rid.md#class_RID) **obstacle_create** ( ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_create)

Creates a new obstacle.

---

<span id="class_NavigationServer3D_method_obstacle_get_avoidance_enabled"></span>

[bool](class_bool.md#class_bool) **obstacle_get_avoidance_enabled** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_avoidance_enabled)

Returns `true` if the provided `obstacle` has avoidance enabled.

---

<span id="class_NavigationServer3D_method_obstacle_get_avoidance_layers"></span>

[int](class_int.md#class_int) **obstacle_get_avoidance_layers** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_avoidance_layers)

Returns the `avoidance_layers` bitmask of the specified `obstacle`.

---

<span id="class_NavigationServer3D_method_obstacle_get_height"></span>

[float](class_float.md#class_float) **obstacle_get_height** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_height)

Returns the `height` of the specified `obstacle`.

---

<span id="class_NavigationServer3D_method_obstacle_get_map"></span>

[RID](class_rid.md#class_RID) **obstacle_get_map** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_map)

Returns the navigation map [RID](class_rid.md#class_RID) the requested `obstacle` is currently assigned to.

---

<span id="class_NavigationServer3D_method_obstacle_get_paused"></span>

[bool](class_bool.md#class_bool) **obstacle_get_paused** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_paused)

Returns `true` if the specified `obstacle` is paused.

---

<span id="class_NavigationServer3D_method_obstacle_get_position"></span>

[Vector3](class_vector3.md#class_Vector3) **obstacle_get_position** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_position)

Returns the position of the specified `obstacle` in world space.

---

<span id="class_NavigationServer3D_method_obstacle_get_radius"></span>

[float](class_float.md#class_float) **obstacle_get_radius** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_radius)

Returns the radius of the specified dynamic `obstacle`.

---

<span id="class_NavigationServer3D_method_obstacle_get_use_3d_avoidance"></span>

[bool](class_bool.md#class_bool) **obstacle_get_use_3d_avoidance** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_use_3d_avoidance)

Returns `true` if the provided `obstacle` uses avoidance in 3D space Vector3(x,y,z) instead of horizontal 2D Vector2(x,y) / Vector3(x,0.0,z).

---

<span id="class_NavigationServer3D_method_obstacle_get_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **obstacle_get_velocity** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_velocity)

Returns the velocity of the specified dynamic `obstacle`.

---

<span id="class_NavigationServer3D_method_obstacle_get_vertices"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **obstacle_get_vertices** ( obstacle: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_get_vertices)

Returns the outline vertices for the specified `obstacle`.

---

<span id="class_NavigationServer3D_method_obstacle_set_avoidance_enabled"></span>

void **obstacle_set_avoidance_enabled** ( obstacle: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_avoidance_enabled)

If `enabled` is `true`, the provided `obstacle` affects avoidance using agents.

---

<span id="class_NavigationServer3D_method_obstacle_set_avoidance_layers"></span>

void **obstacle_set_avoidance_layers** ( obstacle: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_avoidance_layers)

Set the obstacles's `avoidance_layers` bitmask.

---

<span id="class_NavigationServer3D_method_obstacle_set_height"></span>

void **obstacle_set_height** ( obstacle: [RID](class_rid.md#class_RID), height: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_height)

Sets the `height` for the `obstacle`. In 3D agents will ignore obstacles that are above or below them while using 2D avoidance.

---

<span id="class_NavigationServer3D_method_obstacle_set_map"></span>

void **obstacle_set_map** ( obstacle: [RID](class_rid.md#class_RID), map: [RID](class_rid.md#class_RID) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_map)

Assigns the `obstacle` to a navigation map.

---

<span id="class_NavigationServer3D_method_obstacle_set_paused"></span>

void **obstacle_set_paused** ( obstacle: [RID](class_rid.md#class_RID), paused: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_paused)

If `paused` is `true` the specified `obstacle` will not be processed. For example, it will no longer affect avoidance velocities.

---

<span id="class_NavigationServer3D_method_obstacle_set_position"></span>

void **obstacle_set_position** ( obstacle: [RID](class_rid.md#class_RID), position: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_position)

Updates the `position` in world space for the `obstacle`.

---

<span id="class_NavigationServer3D_method_obstacle_set_radius"></span>

void **obstacle_set_radius** ( obstacle: [RID](class_rid.md#class_RID), radius: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_radius)

Sets the radius of the dynamic obstacle.

---

<span id="class_NavigationServer3D_method_obstacle_set_use_3d_avoidance"></span>

void **obstacle_set_use_3d_avoidance** ( obstacle: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_use_3d_avoidance)

Sets if the `obstacle` uses the 2D avoidance or the 3D avoidance while avoidance is enabled.

---

<span id="class_NavigationServer3D_method_obstacle_set_velocity"></span>

void **obstacle_set_velocity** ( obstacle: [RID](class_rid.md#class_RID), velocity: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_velocity)

Sets `velocity` of the dynamic `obstacle`. Allows other agents to better predict the movement of the dynamic obstacle. Only works in combination with the radius of the obstacle.

---

<span id="class_NavigationServer3D_method_obstacle_set_vertices"></span>

void **obstacle_set_vertices** ( obstacle: [RID](class_rid.md#class_RID), vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_obstacle_set_vertices)

Sets the outline vertices for the obstacle. If the vertices are winded in clockwise order agents will be pushed in by the obstacle, else they will be pushed out.

---

<span id="class_NavigationServer3D_method_parse_source_geometry_data"></span>

void **parse_source_geometry_data** ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh), source_geometry_data: [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D), root_node: [Node](class_node.md#class_Node), callback: [Callable](class_callable.md#class_Callable) = Callable() ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_parse_source_geometry_data)

Parses the [SceneTree](class_scenetree.md#class_SceneTree) for source geometry according to the properties of `navigation_mesh`. Updates the provided `source_geometry_data` resource with the resulting data. The resource can then be used to bake a navigation mesh with [bake_from_source_geometry_data()](class_navigationserver3d.md#class_NavigationServer3D_method_bake_from_source_geometry_data). After the process is finished the optional `callback` will be called.

 **Note:** This function needs to run on the main thread or with a deferred call as the SceneTree is not thread-safe.

 **Performance:** While convenient, reading data arrays from [Mesh](class_mesh.md#class_Mesh) resources can affect the frame rate negatively. The data needs to be received from the GPU, stalling the [RenderingServer](class_renderingserver.md#class_RenderingServer) in the process. For performance prefer the use of e.g. collision shapes or creating the data arrays entirely in code.

---

<span id="class_NavigationServer3D_method_query_path"></span>

void **query_path** ( parameters: [NavigationPathQueryParameters3D](class_navigationpathqueryparameters3d.md#class_NavigationPathQueryParameters3D), result: [NavigationPathQueryResult3D](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D), callback: [Callable](class_callable.md#class_Callable) = Callable() ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_query_path)

Queries a path in a given navigation map. Start and target position and other parameters are defined through [NavigationPathQueryParameters3D](class_navigationpathqueryparameters3d.md#class_NavigationPathQueryParameters3D). Updates the provided [NavigationPathQueryResult3D](class_navigationpathqueryresult3d.md#class_NavigationPathQueryResult3D) result object with the path among other results requested by the query. After the process is finished the optional `callback` will be called.

---

<span id="class_NavigationServer3D_method_region_bake_navigation_mesh"></span>

void **region_bake_navigation_mesh** ( navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh), root_node: [Node](class_node.md#class_Node) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_bake_navigation_mesh)

**Deprecated:** This method is deprecated due to core threading changes. To upgrade existing code, first create a [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D) resource. Use this resource with [parse_source_geometry_data()](class_navigationserver3d.md#class_NavigationServer3D_method_parse_source_geometry_data) to parse the [SceneTree](class_scenetree.md#class_SceneTree) for nodes that should contribute to the navigation mesh baking. The [SceneTree](class_scenetree.md#class_SceneTree) parsing needs to happen on the main thread. After the parsing is finished use the resource with [bake_from_source_geometry_data()](class_navigationserver3d.md#class_NavigationServer3D_method_bake_from_source_geometry_data) to bake a navigation mesh.

Bakes the `navigation_mesh` with bake source geometry collected starting from the `root_node`.

---

<span id="class_NavigationServer3D_method_region_create"></span>

[RID](class_rid.md#class_RID) **region_create** ( ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_create)

Creates a new region.

---

<span id="class_NavigationServer3D_method_region_get_bounds"></span>

[AABB](class_aabb.md#class_AABB) **region_get_bounds** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_bounds)

Returns the axis-aligned bounding box for the `region`'s transformed navigation mesh.

---

<span id="class_NavigationServer3D_method_region_get_closest_point"></span>

[Vector3](class_vector3.md#class_Vector3) **region_get_closest_point** ( region: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_closest_point)

Returns the navigation mesh surface point closest to the provided `to_point` on the navigation `region`.

---

<span id="class_NavigationServer3D_method_region_get_closest_point_normal"></span>

[Vector3](class_vector3.md#class_Vector3) **region_get_closest_point_normal** ( region: [RID](class_rid.md#class_RID), to_point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_closest_point_normal)

Returns the navigation mesh surface normal closest to the provided `to_point` on the navigation `region`.

---

<span id="class_NavigationServer3D_method_region_get_closest_point_to_segment"></span>

[Vector3](class_vector3.md#class_Vector3) **region_get_closest_point_to_segment** ( region: [RID](class_rid.md#class_RID), start: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3), use_collision: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_closest_point_to_segment)

Returns the navigation mesh surface point closest to the provided `start` and `end` segment on the navigation `region`.

If `use_collision` is `true`, a closest point test is only done when the segment intersects with the navigation mesh surface.

---

<span id="class_NavigationServer3D_method_region_get_connection_pathway_end"></span>

[Vector3](class_vector3.md#class_Vector3) **region_get_connection_pathway_end** ( region: [RID](class_rid.md#class_RID), connection: [int](class_int.md#class_int) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_connection_pathway_end)

Returns the ending point of a connection door. `connection` is an index between 0 and the return value of [region_get_connections_count()](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_connections_count).

---

<span id="class_NavigationServer3D_method_region_get_connection_pathway_start"></span>

[Vector3](class_vector3.md#class_Vector3) **region_get_connection_pathway_start** ( region: [RID](class_rid.md#class_RID), connection: [int](class_int.md#class_int) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_connection_pathway_start)

Returns the starting point of a connection door. `connection` is an index between 0 and the return value of [region_get_connections_count()](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_connections_count).

---

<span id="class_NavigationServer3D_method_region_get_connections_count"></span>

[int](class_int.md#class_int) **region_get_connections_count** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_connections_count)

Returns how many connections this `region` has with other regions in the map.

---

<span id="class_NavigationServer3D_method_region_get_enabled"></span>

[bool](class_bool.md#class_bool) **region_get_enabled** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_enabled)

Returns `true` if the specified `region` is enabled.

---

<span id="class_NavigationServer3D_method_region_get_enter_cost"></span>

[float](class_float.md#class_float) **region_get_enter_cost** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_enter_cost)

Returns the enter cost of this `region`.

---

<span id="class_NavigationServer3D_method_region_get_iteration_id"></span>

[int](class_int.md#class_int) **region_get_iteration_id** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_iteration_id)

Returns the current iteration ID of the navigation region. Every time the navigation region changes and synchronizes, the iteration ID increases. An iteration ID of `0` means the navigation region has never synchronized.

 **Note:** The iteration ID will wrap around to `1` after reaching its range limit.

---

<span id="class_NavigationServer3D_method_region_get_map"></span>

[RID](class_rid.md#class_RID) **region_get_map** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_map)

Returns the navigation map [RID](class_rid.md#class_RID) the requested `region` is currently assigned to.

---

<span id="class_NavigationServer3D_method_region_get_navigation_layers"></span>

[int](class_int.md#class_int) **region_get_navigation_layers** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_navigation_layers)

Returns the region's navigation layers.

---

<span id="class_NavigationServer3D_method_region_get_owner_id"></span>

[int](class_int.md#class_int) **region_get_owner_id** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_owner_id)

Returns the `ObjectID` of the object which manages this region.

---

<span id="class_NavigationServer3D_method_region_get_random_point"></span>

[Vector3](class_vector3.md#class_Vector3) **region_get_random_point** ( region: [RID](class_rid.md#class_RID), navigation_layers: [int](class_int.md#class_int), uniformly: [bool](class_bool.md#class_bool) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_random_point)

Returns a random position picked from all region polygons with matching `navigation_layers`.

If `uniformly` is `true`, all region polygons and faces are weighted by their surface area (slower).

If `uniformly` is `false`, just a random polygon and face is picked (faster).

---

<span id="class_NavigationServer3D_method_region_get_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **region_get_transform** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_transform)

Returns the global transformation of this `region`.

---

<span id="class_NavigationServer3D_method_region_get_travel_cost"></span>

[float](class_float.md#class_float) **region_get_travel_cost** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_travel_cost)

Returns the travel cost of this `region`.

---

<span id="class_NavigationServer3D_method_region_get_use_async_iterations"></span>

[bool](class_bool.md#class_bool) **region_get_use_async_iterations** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_use_async_iterations)

Returns `true` if the `region` uses an async synchronization process that runs on a background thread.

---

<span id="class_NavigationServer3D_method_region_get_use_edge_connections"></span>

[bool](class_bool.md#class_bool) **region_get_use_edge_connections** ( region: [RID](class_rid.md#class_RID) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_get_use_edge_connections)

Returns `true` if the navigation `region` is set to use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

<span id="class_NavigationServer3D_method_region_owns_point"></span>

[bool](class_bool.md#class_bool) **region_owns_point** ( region: [RID](class_rid.md#class_RID), point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_owns_point)

Returns `true` if the provided `point` in world space is currently owned by the provided navigation `region`. Owned in this context means that one of the region's navigation mesh polygon faces has a possible position at the closest distance to this point compared to all other navigation meshes from other navigation regions that are also registered on the navigation map of the provided region.

If multiple navigation meshes have positions at equal distance the navigation region whose polygons are processed first wins the ownership. Polygons are processed in the same order that navigation regions were registered on the NavigationServer.

 **Note:** If navigation meshes from different navigation regions overlap (which should be avoided in general) the result might not be what is expected.

---

<span id="class_NavigationServer3D_method_region_set_enabled"></span>

void **region_set_enabled** ( region: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_enabled)

If `enabled` is `true`, the specified `region` will contribute to its current navigation map.

---

<span id="class_NavigationServer3D_method_region_set_enter_cost"></span>

void **region_set_enter_cost** ( region: [RID](class_rid.md#class_RID), enter_cost: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_enter_cost)

Sets the `enter_cost` for this `region`.

---

<span id="class_NavigationServer3D_method_region_set_map"></span>

void **region_set_map** ( region: [RID](class_rid.md#class_RID), map: [RID](class_rid.md#class_RID) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_map)

Sets the map for the region.

---

<span id="class_NavigationServer3D_method_region_set_navigation_layers"></span>

void **region_set_navigation_layers** ( region: [RID](class_rid.md#class_RID), navigation_layers: [int](class_int.md#class_int) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_navigation_layers)

Set the region's navigation layers. This allows selecting regions from a path request (when using [map_get_path()](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_path)).

---

<span id="class_NavigationServer3D_method_region_set_navigation_mesh"></span>

void **region_set_navigation_mesh** ( region: [RID](class_rid.md#class_RID), navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_navigation_mesh)

Sets the navigation mesh for the region.

---

<span id="class_NavigationServer3D_method_region_set_owner_id"></span>

void **region_set_owner_id** ( region: [RID](class_rid.md#class_RID), owner_id: [int](class_int.md#class_int) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_owner_id)

Set the `ObjectID` of the object which manages this region.

---

<span id="class_NavigationServer3D_method_region_set_transform"></span>

void **region_set_transform** ( region: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_transform)

Sets the global transformation for the region.

---

<span id="class_NavigationServer3D_method_region_set_travel_cost"></span>

void **region_set_travel_cost** ( region: [RID](class_rid.md#class_RID), travel_cost: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_travel_cost)

Sets the `travel_cost` for this `region`.

---

<span id="class_NavigationServer3D_method_region_set_use_async_iterations"></span>

void **region_set_use_async_iterations** ( region: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_use_async_iterations)

If `enabled` is `true` the `region` uses an async synchronization process that runs on a background thread.

---

<span id="class_NavigationServer3D_method_region_set_use_edge_connections"></span>

void **region_set_use_edge_connections** ( region: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_region_set_use_edge_connections)

If `enabled` is `true`, the navigation `region` will use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

<span id="class_NavigationServer3D_method_set_active"></span>

void **set_active** ( active: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_set_active)

Control activation of this server.

---

<span id="class_NavigationServer3D_method_set_debug_enabled"></span>

void **set_debug_enabled** ( enabled: [bool](class_bool.md#class_bool) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_set_debug_enabled)

If `true` enables debug mode on the NavigationServer.

---

<span id="class_NavigationServer3D_method_simplify_path"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **simplify_path** ( path: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), epsilon: [float](class_float.md#class_float) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_simplify_path)

Returns a simplified version of `path` with less critical path points removed. The simplification amount is in worlds units and controlled by `epsilon`. The simplification uses a variant of Ramer-Douglas-Peucker algorithm for curve point decimation.

Path simplification can be helpful to mitigate various path following issues that can arise with certain agent types and script behaviors. E.g. "steering" agents or avoidance in "open fields".

---

<span id="class_NavigationServer3D_method_source_geometry_parser_create"></span>

[RID](class_rid.md#class_RID) **source_geometry_parser_create** ( ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_source_geometry_parser_create)

Creates a new source geometry parser. If a [Callable](class_callable.md#class_Callable) is set for the parser with [source_geometry_parser_set_callback()](class_navigationserver3d.md#class_NavigationServer3D_method_source_geometry_parser_set_callback) the callback will be called for every single node that gets parsed whenever [parse_source_geometry_data()](class_navigationserver3d.md#class_NavigationServer3D_method_parse_source_geometry_data) is used.

---

<span id="class_NavigationServer3D_method_source_geometry_parser_set_callback"></span>

void **source_geometry_parser_set_callback** ( parser: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_navigationserver3d.md#class_NavigationServer3D_method_source_geometry_parser_set_callback)

Sets the `callback` [Callable](class_callable.md#class_Callable) for the specific source geometry `parser`. The [Callable](class_callable.md#class_Callable) will receive a call with the following parameters:

- `navigation_mesh` - The [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) reference used to define the parse settings. Do NOT edit or add directly to the navigation mesh.

- `source_geometry_data` - The [NavigationMeshSourceGeometryData3D](class_navigationmeshsourcegeometrydata3d.md#class_NavigationMeshSourceGeometryData3D) reference. Add custom source geometry for navigation mesh baking to this object.

- `node` - The [Node](class_node.md#class_Node) that is parsed.
