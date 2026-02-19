<span id="class_NavigationRegion3D"></span>

## NavigationRegion3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A traversable 3D region that [NavigationAgent3D](class_navigationagent3d.md#class_NavigationAgent3D) s can use for pathfinding.

### Description

A traversable 3D region based on a [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) that [NavigationAgent3D](class_navigationagent3d.md#class_NavigationAgent3D) s can use for pathfinding.

Two regions can be connected to each other if they share a similar edge. You can set the minimum distance between two vertices required to connect two edges by using [NavigationServer3D.map_set_edge_connection_margin()](class_navigationserver3d.md#class_NavigationServer3D_method_map_set_edge_connection_margin).

 **Note:** Overlapping two regions' navigation meshes is not enough for connecting two regions. They must share a similar edge.

The cost of entering this region from another region can be controlled with the [enter_cost](class_navigationregion3d.md#class_NavigationRegion3D_property_enter_cost) value.

 **Note:** This value is not added to the path cost when the start position is already inside this region.

The cost of traveling distances inside this region can be controlled with the [travel_cost](class_navigationregion3d.md#class_NavigationRegion3D_property_travel_cost) multiplier.

 **Note:** This node caches changes to its properties, so if you make changes to the underlying region [RID](class_rid.md#class_RID) in [NavigationServer3D](class_navigationserver3d.md#class_NavigationServer3D), they will not be reflected in this node's properties.

### Tutorials

- [Using NavigationRegions](../tutorials/navigation/navigation_using_navigationregions.md)

### Properties


| [bool](class_bool.md#class_bool) | [enabled](class_navigationregion3d.md#class_NavigationRegion3D_property_enabled) | `true` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [enter_cost](class_navigationregion3d.md#class_NavigationRegion3D_property_enter_cost) | `0.0` |
| [int](class_int.md#class_int) | [navigation_layers](class_navigationregion3d.md#class_NavigationRegion3D_property_navigation_layers) | `1` |
| [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) | [navigation_mesh](class_navigationregion3d.md#class_NavigationRegion3D_property_navigation_mesh) |
| [float](class_float.md#class_float) | [travel_cost](class_navigationregion3d.md#class_NavigationRegion3D_property_travel_cost) | `1.0` |
| [bool](class_bool.md#class_bool) | [use_edge_connections](class_navigationregion3d.md#class_NavigationRegion3D_property_use_edge_connections) | `true` |

### Methods


| void | [bake_navigation_mesh](class_navigationregion3d.md#class_NavigationRegion3D_method_bake_navigation_mesh) ( on_thread: [bool](class_bool.md#class_bool) = true ) |
| --- | --- |
| [AABB](class_aabb.md#class_AABB) | [get_bounds](class_navigationregion3d.md#class_NavigationRegion3D_method_get_bounds) ( ) const |
| [bool](class_bool.md#class_bool) | [get_navigation_layer_value](class_navigationregion3d.md#class_NavigationRegion3D_method_get_navigation_layer_value) ( layer_number: [int](class_int.md#class_int) ) const |
| [RID](class_rid.md#class_RID) | [get_navigation_map](class_navigationregion3d.md#class_NavigationRegion3D_method_get_navigation_map) ( ) const |
| [RID](class_rid.md#class_RID) | [get_region_rid](class_navigationregion3d.md#class_NavigationRegion3D_method_get_region_rid) ( ) const |
| [RID](class_rid.md#class_RID) | [get_rid](class_navigationregion3d.md#class_NavigationRegion3D_method_get_rid) ( ) const |
| [bool](class_bool.md#class_bool) | [is_baking](class_navigationregion3d.md#class_NavigationRegion3D_method_is_baking) ( ) const |
| void | [set_navigation_layer_value](class_navigationregion3d.md#class_NavigationRegion3D_method_set_navigation_layer_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |
| void | [set_navigation_map](class_navigationregion3d.md#class_NavigationRegion3D_method_set_navigation_map) ( navigation_map: [RID](class_rid.md#class_RID) ) |

---

### Signals

<span id="class_NavigationRegion3D_signal_bake_finished"></span>

**bake_finished** ( ) [🔗](class_navigationregion3d.md#class_NavigationRegion3D_signal_bake_finished)

Notifies when the navigation mesh bake operation is completed.

---

<span id="class_NavigationRegion3D_signal_navigation_mesh_changed"></span>

**navigation_mesh_changed** ( ) [🔗](class_navigationregion3d.md#class_NavigationRegion3D_signal_navigation_mesh_changed)

Notifies when the [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) has changed.

---

### Property Descriptions

<span id="class_NavigationRegion3D_property_enabled"></span>

[bool](class_bool.md#class_bool) **enabled** = `true` [🔗](class_navigationregion3d.md#class_NavigationRegion3D_property_enabled)

- void **set_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_enabled** ( )

Determines if the **NavigationRegion3D** is enabled or disabled.

---

<span id="class_NavigationRegion3D_property_enter_cost"></span>

[float](class_float.md#class_float) **enter_cost** = `0.0` [🔗](class_navigationregion3d.md#class_NavigationRegion3D_property_enter_cost)

- void **set_enter_cost** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_enter_cost** ( )

When pathfinding enters this region's navigation mesh from another regions navigation mesh the [enter_cost](class_navigationregion3d.md#class_NavigationRegion3D_property_enter_cost) value is added to the path distance for determining the shortest path.

---

<span id="class_NavigationRegion3D_property_navigation_layers"></span>

[int](class_int.md#class_int) **navigation_layers** = `1` [🔗](class_navigationregion3d.md#class_NavigationRegion3D_property_navigation_layers)

- void **set_navigation_layers** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_navigation_layers** ( )

A bitfield determining all navigation layers the region belongs to. These navigation layers can be checked upon when requesting a path with [NavigationServer3D.map_get_path()](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_path).

---

<span id="class_NavigationRegion3D_property_navigation_mesh"></span>

[NavigationMesh](class_navigationmesh.md#class_NavigationMesh) **navigation_mesh** [🔗](class_navigationregion3d.md#class_NavigationRegion3D_property_navigation_mesh)

- void **set_navigation_mesh** ( value: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) )
- [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) **get_navigation_mesh** ( )

The [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) resource to use.

---

<span id="class_NavigationRegion3D_property_travel_cost"></span>

[float](class_float.md#class_float) **travel_cost** = `1.0` [🔗](class_navigationregion3d.md#class_NavigationRegion3D_property_travel_cost)

- void **set_travel_cost** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_travel_cost** ( )

When pathfinding moves inside this region's navigation mesh the traveled distances are multiplied with [travel_cost](class_navigationregion3d.md#class_NavigationRegion3D_property_travel_cost) for determining the shortest path.

---

<span id="class_NavigationRegion3D_property_use_edge_connections"></span>

[bool](class_bool.md#class_bool) **use_edge_connections** = `true` [🔗](class_navigationregion3d.md#class_NavigationRegion3D_property_use_edge_connections)

- void **set_use_edge_connections** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_edge_connections** ( )

If enabled the navigation region will use edge connections to connect with other navigation regions within proximity of the navigation map edge connection margin.

---

### Method Descriptions

<span id="class_NavigationRegion3D_method_bake_navigation_mesh"></span>

void **bake_navigation_mesh** ( on_thread: [bool](class_bool.md#class_bool) = true ) [🔗](class_navigationregion3d.md#class_NavigationRegion3D_method_bake_navigation_mesh)

Bakes the [NavigationMesh](class_navigationmesh.md#class_NavigationMesh). If `on_thread` is set to `true` (default), the baking is done on a separate thread. Baking on separate thread is useful because navigation baking is not a cheap operation. When it is completed, it automatically sets the new [NavigationMesh](class_navigationmesh.md#class_NavigationMesh). Please note that baking on separate thread may be very slow if geometry is parsed from meshes as async access to each mesh involves heavy synchronization. Also, please note that baking on a separate thread is automatically disabled on operating systems that cannot use threads (such as Web with threads disabled).

---

<span id="class_NavigationRegion3D_method_get_bounds"></span>

[AABB](class_aabb.md#class_AABB) **get_bounds** ( ) *const* [🔗](class_navigationregion3d.md#class_NavigationRegion3D_method_get_bounds)

Returns the axis-aligned bounding box for the region's transformed navigation mesh.

---

<span id="class_NavigationRegion3D_method_get_navigation_layer_value"></span>

[bool](class_bool.md#class_bool) **get_navigation_layer_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_navigationregion3d.md#class_NavigationRegion3D_method_get_navigation_layer_value)

Returns whether or not the specified layer of the [navigation_layers](class_navigationregion3d.md#class_NavigationRegion3D_property_navigation_layers) bitmask is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_NavigationRegion3D_method_get_navigation_map"></span>

[RID](class_rid.md#class_RID) **get_navigation_map** ( ) *const* [🔗](class_navigationregion3d.md#class_NavigationRegion3D_method_get_navigation_map)

Returns the current navigation map [RID](class_rid.md#class_RID) used by this region.

---

<span id="class_NavigationRegion3D_method_get_region_rid"></span>

[RID](class_rid.md#class_RID) **get_region_rid** ( ) *const* [🔗](class_navigationregion3d.md#class_NavigationRegion3D_method_get_region_rid)

**Deprecated:** Use [get_rid()](class_navigationregion3d.md#class_NavigationRegion3D_method_get_rid) instead.

Returns the [RID](class_rid.md#class_RID) of this region on the [NavigationServer3D](class_navigationserver3d.md#class_NavigationServer3D).

---

<span id="class_NavigationRegion3D_method_get_rid"></span>

[RID](class_rid.md#class_RID) **get_rid** ( ) *const* [🔗](class_navigationregion3d.md#class_NavigationRegion3D_method_get_rid)

Returns the [RID](class_rid.md#class_RID) of this region on the [NavigationServer3D](class_navigationserver3d.md#class_NavigationServer3D). Combined with [NavigationServer3D.map_get_closest_point_owner()](class_navigationserver3d.md#class_NavigationServer3D_method_map_get_closest_point_owner) can be used to identify the **NavigationRegion3D** closest to a point on the merged navigation map.

---

<span id="class_NavigationRegion3D_method_is_baking"></span>

[bool](class_bool.md#class_bool) **is_baking** ( ) *const* [🔗](class_navigationregion3d.md#class_NavigationRegion3D_method_is_baking)

Returns `true` when the [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) is being baked on a background thread.

---

<span id="class_NavigationRegion3D_method_set_navigation_layer_value"></span>

void **set_navigation_layer_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_navigationregion3d.md#class_NavigationRegion3D_method_set_navigation_layer_value)

Based on `value`, enables or disables the specified layer in the [navigation_layers](class_navigationregion3d.md#class_NavigationRegion3D_property_navigation_layers) bitmask, given a `layer_number` between 1 and 32.

---

<span id="class_NavigationRegion3D_method_set_navigation_map"></span>

void **set_navigation_map** ( navigation_map: [RID](class_rid.md#class_RID) ) [🔗](class_navigationregion3d.md#class_NavigationRegion3D_method_set_navigation_map)

Sets the [RID](class_rid.md#class_RID) of the navigation map this region should use. By default the region will automatically join the [World3D](class_world3d.md#class_World3D) default navigation map so this function is only required to override the default map.
