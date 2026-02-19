<span id="class_TileMapLayer"></span>

## TileMapLayer

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Node for 2D tile-based maps.

### Description

Node for 2D tile-based maps. A **TileMapLayer** uses a [TileSet](class_tileset.md#class_TileSet) which contain a list of tiles which are used to create grid-based maps. Unlike the [TileMap](class_tilemap.md#class_TileMap) node, which is deprecated, **TileMapLayer** has only one layer of tiles. You can use several **TileMapLayer** to achieve the same result as a [TileMap](class_tilemap.md#class_TileMap) node.

For performance reasons, all TileMap updates are batched at the end of a frame. Notably, this means that scene tiles from a [TileSetScenesCollectionSource](class_tilesetscenescollectionsource.md#class_TileSetScenesCollectionSource) are initialized after their parent. This is only queued when inside the scene tree.

To force an update earlier on, call [update_internals()](class_tilemaplayer.md#class_TileMapLayer_method_update_internals).

 **Note:** For performance and compatibility reasons, the coordinates serialized by **TileMapLayer** are limited to 16-bit signed integers, i.e. the range for X and Y coordinates is from `-32768` to `32767`. When saving tile data, tiles outside this range are wrapped.

### Tutorials

- [Using Tilemaps](../tutorials/2d/using_tilemaps.md)

- 2D Platformer Demo

- 2D Isometric Demo

- 2D Hexagonal Demo

- 2D Grid-based Navigation with AStarGrid2D Demo

- 2D Role Playing Game (RPG) Demo

- 2D Kinematic Character Demo

- 2D Dynamic TileMap Layers Demo

### Properties


| [bool](class_bool.md#class_bool) | [collision_enabled](class_tilemaplayer.md#class_TileMapLayer_property_collision_enabled) | `true` |
| --- | --- | --- |
| [DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) | [collision_visibility_mode](class_tilemaplayer.md#class_TileMapLayer_property_collision_visibility_mode) | `0` |
| [bool](class_bool.md#class_bool) | [enabled](class_tilemaplayer.md#class_TileMapLayer_property_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [navigation_enabled](class_tilemaplayer.md#class_TileMapLayer_property_navigation_enabled) | `true` |
| [DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) | [navigation_visibility_mode](class_tilemaplayer.md#class_TileMapLayer_property_navigation_visibility_mode) | `0` |
| [bool](class_bool.md#class_bool) | [occlusion_enabled](class_tilemaplayer.md#class_TileMapLayer_property_occlusion_enabled) | `true` |
| [int](class_int.md#class_int) | [physics_quadrant_size](class_tilemaplayer.md#class_TileMapLayer_property_physics_quadrant_size) | `16` |
| [int](class_int.md#class_int) | [rendering_quadrant_size](class_tilemaplayer.md#class_TileMapLayer_property_rendering_quadrant_size) | `16` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [tile_map_data](class_tilemaplayer.md#class_TileMapLayer_property_tile_map_data) | `PackedByteArray()` |
| [TileSet](class_tileset.md#class_TileSet) | [tile_set](class_tilemaplayer.md#class_TileMapLayer_property_tile_set) |
| [bool](class_bool.md#class_bool) | [use_kinematic_bodies](class_tilemaplayer.md#class_TileMapLayer_property_use_kinematic_bodies) | `false` |
| [bool](class_bool.md#class_bool) | [x_draw_order_reversed](class_tilemaplayer.md#class_TileMapLayer_property_x_draw_order_reversed) | `false` |
| [int](class_int.md#class_int) | [y_sort_origin](class_tilemaplayer.md#class_TileMapLayer_property_y_sort_origin) | `0` |

### Methods


| void | [_tile_data_runtime_update](class_tilemaplayer.md#class_TileMapLayer_private_method__tile_data_runtime_update) ( coords: [Vector2i](class_vector2i.md#class_Vector2i), tile_data: [TileData](class_tiledata.md#class_TileData) ) virtual |
| --- | --- |
| void | [_update_cells](class_tilemaplayer.md#class_TileMapLayer_private_method__update_cells) ( coords: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], forced_cleanup: [bool](class_bool.md#class_bool) ) virtual |
| [bool](class_bool.md#class_bool) | [_use_tile_data_runtime_update](class_tilemaplayer.md#class_TileMapLayer_private_method__use_tile_data_runtime_update) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) virtual |
| void | [clear](class_tilemaplayer.md#class_TileMapLayer_method_clear) ( ) |
| void | [erase_cell](class_tilemaplayer.md#class_TileMapLayer_method_erase_cell) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [fix_invalid_tiles](class_tilemaplayer.md#class_TileMapLayer_method_fix_invalid_tiles) ( ) |
| [int](class_int.md#class_int) | [get_cell_alternative_tile](class_tilemaplayer.md#class_TileMapLayer_method_get_cell_alternative_tile) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_cell_atlas_coords](class_tilemaplayer.md#class_TileMapLayer_method_get_cell_atlas_coords) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [int](class_int.md#class_int) | [get_cell_source_id](class_tilemaplayer.md#class_TileMapLayer_method_get_cell_source_id) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [TileData](class_tiledata.md#class_TileData) | [get_cell_tile_data](class_tilemaplayer.md#class_TileMapLayer_method_get_cell_tile_data) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_coords_for_body_rid](class_tilemaplayer.md#class_TileMapLayer_method_get_coords_for_body_rid) ( body: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [get_navigation_map](class_tilemaplayer.md#class_TileMapLayer_method_get_navigation_map) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_neighbor_cell](class_tilemaplayer.md#class_TileMapLayer_method_get_neighbor_cell) ( coords: [Vector2i](class_vector2i.md#class_Vector2i), neighbor: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) ) const |
| [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) | [get_pattern](class_tilemaplayer.md#class_TileMapLayer_method_get_pattern) ( coords_array: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] ) |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [get_surrounding_cells](class_tilemaplayer.md#class_TileMapLayer_method_get_surrounding_cells) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [get_used_cells](class_tilemaplayer.md#class_TileMapLayer_method_get_used_cells) ( ) const |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [get_used_cells_by_id](class_tilemaplayer.md#class_TileMapLayer_method_get_used_cells_by_id) ( source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = -1 ) const |
| [Rect2i](class_rect2i.md#class_Rect2i) | [get_used_rect](class_tilemaplayer.md#class_TileMapLayer_method_get_used_rect) ( ) const |
| [bool](class_bool.md#class_bool) | [has_body_rid](class_tilemaplayer.md#class_TileMapLayer_method_has_body_rid) ( body: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [is_cell_flipped_h](class_tilemaplayer.md#class_TileMapLayer_method_is_cell_flipped_h) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [bool](class_bool.md#class_bool) | [is_cell_flipped_v](class_tilemaplayer.md#class_TileMapLayer_method_is_cell_flipped_v) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [bool](class_bool.md#class_bool) | [is_cell_transposed](class_tilemaplayer.md#class_TileMapLayer_method_is_cell_transposed) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [local_to_map](class_tilemaplayer.md#class_TileMapLayer_method_local_to_map) ( local_position: [Vector2](class_vector2.md#class_Vector2) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [map_pattern](class_tilemaplayer.md#class_TileMapLayer_method_map_pattern) ( position_in_tilemap: [Vector2i](class_vector2i.md#class_Vector2i), coords_in_pattern: [Vector2i](class_vector2i.md#class_Vector2i), pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) ) |
| [Vector2](class_vector2.md#class_Vector2) | [map_to_local](class_tilemaplayer.md#class_TileMapLayer_method_map_to_local) ( map_position: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| void | [notify_runtime_tile_data_update](class_tilemaplayer.md#class_TileMapLayer_method_notify_runtime_tile_data_update) ( ) |
| void | [set_cell](class_tilemaplayer.md#class_TileMapLayer_method_set_cell) ( coords: [Vector2i](class_vector2i.md#class_Vector2i), source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = 0 ) |
| void | [set_cells_terrain_connect](class_tilemaplayer.md#class_TileMapLayer_method_set_cells_terrain_connect) ( cells: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], terrain_set: [int](class_int.md#class_int), terrain: [int](class_int.md#class_int), ignore_empty_terrains: [bool](class_bool.md#class_bool) = true ) |
| void | [set_cells_terrain_path](class_tilemaplayer.md#class_TileMapLayer_method_set_cells_terrain_path) ( path: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], terrain_set: [int](class_int.md#class_int), terrain: [int](class_int.md#class_int), ignore_empty_terrains: [bool](class_bool.md#class_bool) = true ) |
| void | [set_navigation_map](class_tilemaplayer.md#class_TileMapLayer_method_set_navigation_map) ( map: [RID](class_rid.md#class_RID) ) |
| void | [set_pattern](class_tilemaplayer.md#class_TileMapLayer_method_set_pattern) ( position: [Vector2i](class_vector2i.md#class_Vector2i), pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) ) |
| void | [update_internals](class_tilemaplayer.md#class_TileMapLayer_method_update_internals) ( ) |

---

### Signals

<span id="class_TileMapLayer_signal_changed"></span>

**changed** ( ) [🔗](class_tilemaplayer.md#class_TileMapLayer_signal_changed)

Emitted when this **TileMapLayer**'s properties changes. This includes modified cells, properties, or changes made to its assigned [TileSet](class_tileset.md#class_TileSet).

 **Note:** This signal may be emitted very often when batch-modifying a **TileMapLayer**. Avoid executing complex processing in a connected function, and consider delaying it to the end of the frame instead (i.e. calling [Object.call_deferred()](class_object.md#class_Object_method_call_deferred)).

---

### Enumerations

<span id="enum_TileMapLayer_DebugVisibilityMode"></span>

enum **DebugVisibilityMode**: [🔗](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode)

<span id="class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_DEFAULT"></span>

[DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) **DEBUG_VISIBILITY_MODE_DEFAULT** = `0`

Hide the collisions or navigation debug shapes in the editor, and use the debug settings to determine their visibility in game (i.e. [SceneTree.debug_collisions_hint](class_scenetree.md#class_SceneTree_property_debug_collisions_hint) or [SceneTree.debug_navigation_hint](class_scenetree.md#class_SceneTree_property_debug_navigation_hint)).

<span id="class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_FORCE_HIDE"></span>

[DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) **DEBUG_VISIBILITY_MODE_FORCE_HIDE** = `2`

Always hide the collisions or navigation debug shapes.

<span id="class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_FORCE_SHOW"></span>

[DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) **DEBUG_VISIBILITY_MODE_FORCE_SHOW** = `1`

Always show the collisions or navigation debug shapes.

---

### Property Descriptions

<span id="class_TileMapLayer_property_collision_enabled"></span>

[bool](class_bool.md#class_bool) **collision_enabled** = `true` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_collision_enabled)

- void **set_collision_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collision_enabled** ( )

Enable or disable collisions.

---

<span id="class_TileMapLayer_property_collision_visibility_mode"></span>

[DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) **collision_visibility_mode** = `0` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_collision_visibility_mode)

- void **set_collision_visibility_mode** ( value: [DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) )
- [DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) **get_collision_visibility_mode** ( )

Show or hide the **TileMapLayer**'s collision shapes. If set to [DEBUG_VISIBILITY_MODE_DEFAULT](class_tilemaplayer.md#class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_DEFAULT), this depends on the show collision debug settings.

---

<span id="class_TileMapLayer_property_enabled"></span>

[bool](class_bool.md#class_bool) **enabled** = `true` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_enabled)

- void **set_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_enabled** ( )

If `false`, disables this **TileMapLayer** completely (rendering, collision, navigation, scene tiles, etc.)

---

<span id="class_TileMapLayer_property_navigation_enabled"></span>

[bool](class_bool.md#class_bool) **navigation_enabled** = `true` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_navigation_enabled)

- void **set_navigation_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_navigation_enabled** ( )

If `true`, navigation regions are enabled.

---

<span id="class_TileMapLayer_property_navigation_visibility_mode"></span>

[DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) **navigation_visibility_mode** = `0` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_navigation_visibility_mode)

- void **set_navigation_visibility_mode** ( value: [DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) )
- [DebugVisibilityMode](class_tilemaplayer.md#enum_TileMapLayer_DebugVisibilityMode) **get_navigation_visibility_mode** ( )

Show or hide the **TileMapLayer**'s navigation meshes. If set to [DEBUG_VISIBILITY_MODE_DEFAULT](class_tilemaplayer.md#class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_DEFAULT), this depends on the show navigation debug settings.

---

<span id="class_TileMapLayer_property_occlusion_enabled"></span>

[bool](class_bool.md#class_bool) **occlusion_enabled** = `true` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_occlusion_enabled)

- void **set_occlusion_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_occlusion_enabled** ( )

Enable or disable light occlusion.

---

<span id="class_TileMapLayer_property_physics_quadrant_size"></span>

[int](class_int.md#class_int) **physics_quadrant_size** = `16` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_physics_quadrant_size)

- void **set_physics_quadrant_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_physics_quadrant_size** ( )

The **TileMapLayer**'s physics quadrant size. Within a physics quadrant, cells with similar physics properties are grouped together and their collision shapes get merged. [physics_quadrant_size](class_tilemaplayer.md#class_TileMapLayer_property_physics_quadrant_size) defines the length of a square's side, in the map's coordinate system, that forms the quadrant. Thus, the default quadrant size groups together `16 * 16 = 256` tiles.

 **Note:** As quadrants are created according to the map's coordinate system, the quadrant's "square shape" might not look like square in the **TileMapLayer**'s local coordinate system.

 **Note:** This impacts the value returned by [get_coords_for_body_rid()](class_tilemaplayer.md#class_TileMapLayer_method_get_coords_for_body_rid). Higher values will make that function less precise. To get the exact cell coordinates, you need to set [physics_quadrant_size](class_tilemaplayer.md#class_TileMapLayer_property_physics_quadrant_size) to `1`, which disables physics chunking.

---

<span id="class_TileMapLayer_property_rendering_quadrant_size"></span>

[int](class_int.md#class_int) **rendering_quadrant_size** = `16` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_rendering_quadrant_size)

- void **set_rendering_quadrant_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_rendering_quadrant_size** ( )

The **TileMapLayer**'s rendering quadrant size. A quadrant is a group of tiles to be drawn together on a single canvas item, for optimization purposes. [rendering_quadrant_size](class_tilemaplayer.md#class_TileMapLayer_property_rendering_quadrant_size) defines the length of a square's side, in the map's coordinate system, that forms the quadrant. Thus, the default quadrant size groups together `16 * 16 = 256` tiles.

The quadrant size does not apply on a Y-sorted **TileMapLayer**, as tiles are grouped by Y position instead in that case.

 **Note:** As quadrants are created according to the map's coordinate system, the quadrant's "square shape" might not look like square in the **TileMapLayer**'s local coordinate system.

---

<span id="class_TileMapLayer_property_tile_map_data"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **tile_map_data** = `PackedByteArray()` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_tile_map_data)

- void **set_tile_map_data_from_array** ( value: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_tile_map_data_as_array** ( )

The raw tile map data as a byte array.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_TileMapLayer_property_tile_set"></span>

[TileSet](class_tileset.md#class_TileSet) **tile_set** [🔗](class_tilemaplayer.md#class_TileMapLayer_property_tile_set)

- void **set_tile_set** ( value: [TileSet](class_tileset.md#class_TileSet) )
- [TileSet](class_tileset.md#class_TileSet) **get_tile_set** ( )

The [TileSet](class_tileset.md#class_TileSet) used by this layer. The textures, collisions, and additional behavior of all available tiles are stored here.

---

<span id="class_TileMapLayer_property_use_kinematic_bodies"></span>

[bool](class_bool.md#class_bool) **use_kinematic_bodies** = `false` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_use_kinematic_bodies)

- void **set_use_kinematic_bodies** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_kinematic_bodies** ( )

If `true`, this **TileMapLayer** collision shapes will be instantiated as kinematic bodies. This can be needed for moving **TileMapLayer** nodes (i.e. moving platforms).

---

<span id="class_TileMapLayer_property_x_draw_order_reversed"></span>

[bool](class_bool.md#class_bool) **x_draw_order_reversed** = `false` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_x_draw_order_reversed)

- void **set_x_draw_order_reversed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_x_draw_order_reversed** ( )

If [CanvasItem.y_sort_enabled](class_canvasitem.md#class_CanvasItem_property_y_sort_enabled) is enabled, setting this to `true` will reverse the order the tiles are drawn on the X-axis.

---

<span id="class_TileMapLayer_property_y_sort_origin"></span>

[int](class_int.md#class_int) **y_sort_origin** = `0` [🔗](class_tilemaplayer.md#class_TileMapLayer_property_y_sort_origin)

- void **set_y_sort_origin** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_y_sort_origin** ( )

This Y-sort origin value is added to each tile's Y-sort origin value. This allows, for example, to fake a different height level. This can be useful for top-down view games.

---

### Method Descriptions

<span id="class_TileMapLayer_private_method__tile_data_runtime_update"></span>

void **_tile_data_runtime_update** ( coords: [Vector2i](class_vector2i.md#class_Vector2i), tile_data: [TileData](class_tiledata.md#class_TileData) ) *virtual* [🔗](class_tilemaplayer.md#class_TileMapLayer_private_method__tile_data_runtime_update)

Called with a [TileData](class_tiledata.md#class_TileData) object about to be used internally by the **TileMapLayer**, allowing its modification at runtime.

This method is only called if [_use_tile_data_runtime_update()](class_tilemaplayer.md#class_TileMapLayer_private_method__use_tile_data_runtime_update) is implemented and returns `true` for the given tile `coords`.

 **Warning:** The `tile_data` object's sub-resources are the same as the one in the TileSet. Modifying them might impact the whole TileSet. Instead, make sure to duplicate those resources.

 **Note:** If the properties of `tile_data` object should change over time, use [notify_runtime_tile_data_update()](class_tilemaplayer.md#class_TileMapLayer_method_notify_runtime_tile_data_update) to notify the **TileMapLayer** it needs an update.

---

<span id="class_TileMapLayer_private_method__update_cells"></span>

void **_update_cells** ( coords: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], forced_cleanup: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_tilemaplayer.md#class_TileMapLayer_private_method__update_cells)

Called when this **TileMapLayer**'s cells need an internal update. This update may be caused from individual cells being modified or by a change in the [tile_set](class_tilemaplayer.md#class_TileMapLayer_property_tile_set) (causing all cells to be queued for an update). The first call to this function is always for initializing all the **TileMapLayer**'s cells. `coords` contains the coordinates of all modified cells, roughly in the order they were modified. `forced_cleanup` is `true` when the **TileMapLayer**'s internals should be fully cleaned up. This is the case when:

- The layer is disabled;

- The layer is not visible;

- [tile_set](class_tilemaplayer.md#class_TileMapLayer_property_tile_set) is set to `null`;

- The node is removed from the tree;

- The node is freed.

Note that any internal update happening while one of these conditions is verified is considered to be a "cleanup". See also [update_internals()](class_tilemaplayer.md#class_TileMapLayer_method_update_internals).

 **Warning:** Implementing this method may degrade the **TileMapLayer**'s performance.

---

<span id="class_TileMapLayer_private_method__use_tile_data_runtime_update"></span>

[bool](class_bool.md#class_bool) **_use_tile_data_runtime_update** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* [🔗](class_tilemaplayer.md#class_TileMapLayer_private_method__use_tile_data_runtime_update)

Should return `true` if the tile at coordinates `coords` requires a runtime update.

 **Warning:** Make sure this function only returns `true` when needed. Any tile processed at runtime without a need for it will imply a significant performance penalty.

 **Note:** If the result of this function should change, use [notify_runtime_tile_data_update()](class_tilemaplayer.md#class_TileMapLayer_method_notify_runtime_tile_data_update) to notify the **TileMapLayer** it needs an update.

---

<span id="class_TileMapLayer_method_clear"></span>

void **clear** ( ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_clear)

Clears all cells.

---

<span id="class_TileMapLayer_method_erase_cell"></span>

void **erase_cell** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_erase_cell)

Erases the cell at coordinates `coords`.

---

<span id="class_TileMapLayer_method_fix_invalid_tiles"></span>

void **fix_invalid_tiles** ( ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_fix_invalid_tiles)

Clears cells containing tiles that do not exist in the [tile_set](class_tilemaplayer.md#class_TileMapLayer_property_tile_set).

---

<span id="class_TileMapLayer_method_get_cell_alternative_tile"></span>

[int](class_int.md#class_int) **get_cell_alternative_tile** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_cell_alternative_tile)

Returns the tile alternative ID of the cell at coordinates `coords`.

---

<span id="class_TileMapLayer_method_get_cell_atlas_coords"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_cell_atlas_coords** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_cell_atlas_coords)

Returns the tile atlas coordinates ID of the cell at coordinates `coords`. Returns `Vector2i(-1, -1)` if the cell does not exist.

---

<span id="class_TileMapLayer_method_get_cell_source_id"></span>

[int](class_int.md#class_int) **get_cell_source_id** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_cell_source_id)

Returns the tile source ID of the cell at coordinates `coords`. Returns `-1` if the cell does not exist.

---

<span id="class_TileMapLayer_method_get_cell_tile_data"></span>

[TileData](class_tiledata.md#class_TileData) **get_cell_tile_data** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_cell_tile_data)

Returns the [TileData](class_tiledata.md#class_TileData) object associated with the given cell, or `null` if the cell does not exist or is not a [TileSetAtlasSource](class_tilesetatlassource.md#class_TileSetAtlasSource).

::

    func get_clicked_tile_power():
        var clicked_cell = tile_map_layer.local_to_map(tile_map_layer.get_local_mouse_position())
        var data = tile_map_layer.get_cell_tile_data(clicked_cell)
        if data:
            return data.get_custom_data("power")
        else:
            return 0

---

<span id="class_TileMapLayer_method_get_coords_for_body_rid"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_coords_for_body_rid** ( body: [RID](class_rid.md#class_RID) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_coords_for_body_rid)

Returns the coordinates of the physics quadrant (see [physics_quadrant_size](class_tilemaplayer.md#class_TileMapLayer_property_physics_quadrant_size)) for given physics body [RID](class_rid.md#class_RID). Such an [RID](class_rid.md#class_RID) can be retrieved from [KinematicCollision2D.get_collider_rid()](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_rid), when colliding with a tile.

 **Note:** Higher values of [physics_quadrant_size](class_tilemaplayer.md#class_TileMapLayer_property_physics_quadrant_size) will make this function less precise. To get the exact cell coordinates, you need to set [physics_quadrant_size](class_tilemaplayer.md#class_TileMapLayer_property_physics_quadrant_size) to `1`, which disables physics chunking.

---

<span id="class_TileMapLayer_method_get_navigation_map"></span>

[RID](class_rid.md#class_RID) **get_navigation_map** ( ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_navigation_map)

Returns the [RID](class_rid.md#class_RID) of the [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) navigation used by this **TileMapLayer**.

By default this returns the default [World2D](class_world2d.md#class_World2D) navigation map, unless a custom map was provided using [set_navigation_map()](class_tilemaplayer.md#class_TileMapLayer_method_set_navigation_map).

---

<span id="class_TileMapLayer_method_get_neighbor_cell"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_neighbor_cell** ( coords: [Vector2i](class_vector2i.md#class_Vector2i), neighbor: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_neighbor_cell)

Returns the neighboring cell to the one at coordinates `coords`, identified by the `neighbor` direction. This method takes into account the different layouts a TileMap can take.

---

<span id="class_TileMapLayer_method_get_pattern"></span>

[TileMapPattern](class_tilemappattern.md#class_TileMapPattern) **get_pattern** ( coords_array: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_pattern)

Creates and returns a new [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) from the given array of cells. See also [set_pattern()](class_tilemaplayer.md#class_TileMapLayer_method_set_pattern).

---

<span id="class_TileMapLayer_method_get_surrounding_cells"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **get_surrounding_cells** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_surrounding_cells)

Returns the list of all neighboring cells to the one at `coords`. Any neighboring cell is one that is touching edges, so for a square cell 4 cells would be returned, for a hexagon 6 cells are returned.

---

<span id="class_TileMapLayer_method_get_used_cells"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **get_used_cells** ( ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_used_cells)

Returns a [Vector2i](class_vector2i.md#class_Vector2i) array with the positions of all cells containing a tile. A cell is considered empty if its source identifier equals `-1`, its atlas coordinate identifier is `Vector2(-1, -1)` and its alternative identifier is `-1`.

---

<span id="class_TileMapLayer_method_get_used_cells_by_id"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **get_used_cells_by_id** ( source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_used_cells_by_id)

Returns a [Vector2i](class_vector2i.md#class_Vector2i) array with the positions of all cells containing a tile. Tiles may be filtered according to their source (`source_id`), their atlas coordinates (`atlas_coords`), or alternative id (`alternative_tile`).

If a parameter has its value set to the default one, this parameter is not used to filter a cell. Thus, if all parameters have their respective default values, this method returns the same result as [get_used_cells()](class_tilemaplayer.md#class_TileMapLayer_method_get_used_cells).

A cell is considered empty if its source identifier equals `-1`, its atlas coordinate identifier is `Vector2(-1, -1)` and its alternative identifier is `-1`.

---

<span id="class_TileMapLayer_method_get_used_rect"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **get_used_rect** ( ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_get_used_rect)

Returns a rectangle enclosing the used (non-empty) tiles of the map.

---

<span id="class_TileMapLayer_method_has_body_rid"></span>

[bool](class_bool.md#class_bool) **has_body_rid** ( body: [RID](class_rid.md#class_RID) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_has_body_rid)

Returns whether the provided `body` [RID](class_rid.md#class_RID) belongs to one of this **TileMapLayer**'s cells.

---

<span id="class_TileMapLayer_method_is_cell_flipped_h"></span>

[bool](class_bool.md#class_bool) **is_cell_flipped_h** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_is_cell_flipped_h)

Returns `true` if the cell at coordinates `coords` is flipped horizontally. The result is valid only for atlas sources.

---

<span id="class_TileMapLayer_method_is_cell_flipped_v"></span>

[bool](class_bool.md#class_bool) **is_cell_flipped_v** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_is_cell_flipped_v)

Returns `true` if the cell at coordinates `coords` is flipped vertically. The result is valid only for atlas sources.

---

<span id="class_TileMapLayer_method_is_cell_transposed"></span>

[bool](class_bool.md#class_bool) **is_cell_transposed** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_is_cell_transposed)

Returns `true` if the cell at coordinates `coords` is transposed. The result is valid only for atlas sources.

---

<span id="class_TileMapLayer_method_local_to_map"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **local_to_map** ( local_position: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_local_to_map)

Returns the map coordinates of the cell containing the given `local_position`. If `local_position` is in global coordinates, consider using [Node2D.to_local()](class_node2d.md#class_Node2D_method_to_local) before passing it to this method. See also [map_to_local()](class_tilemaplayer.md#class_TileMapLayer_method_map_to_local).

---

<span id="class_TileMapLayer_method_map_pattern"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **map_pattern** ( position_in_tilemap: [Vector2i](class_vector2i.md#class_Vector2i), coords_in_pattern: [Vector2i](class_vector2i.md#class_Vector2i), pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_map_pattern)

Returns for the given coordinates `coords_in_pattern` in a [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) the corresponding cell coordinates if the pattern was pasted at the `position_in_tilemap` coordinates (see [set_pattern()](class_tilemaplayer.md#class_TileMapLayer_method_set_pattern)). This mapping is required as in half-offset tile shapes, the mapping might not work by calculating `position_in_tile_map + coords_in_pattern`.

---

<span id="class_TileMapLayer_method_map_to_local"></span>

[Vector2](class_vector2.md#class_Vector2) **map_to_local** ( map_position: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemaplayer.md#class_TileMapLayer_method_map_to_local)

Returns the centered position of a cell in the **TileMapLayer**'s local coordinate space. To convert the returned value into global coordinates, use [Node2D.to_global()](class_node2d.md#class_Node2D_method_to_global). See also [local_to_map()](class_tilemaplayer.md#class_TileMapLayer_method_local_to_map).

 **Note:** This may not correspond to the visual position of the tile, i.e. it ignores the [TileData.texture_origin](class_tiledata.md#class_TileData_property_texture_origin) property of individual tiles.

---

<span id="class_TileMapLayer_method_notify_runtime_tile_data_update"></span>

void **notify_runtime_tile_data_update** ( ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_notify_runtime_tile_data_update)

Notifies the **TileMapLayer** node that calls to [_use_tile_data_runtime_update()](class_tilemaplayer.md#class_TileMapLayer_private_method__use_tile_data_runtime_update) or [_tile_data_runtime_update()](class_tilemaplayer.md#class_TileMapLayer_private_method__tile_data_runtime_update) will lead to different results. This will thus trigger a **TileMapLayer** update.

 **Warning:** Updating the **TileMapLayer** is computationally expensive and may impact performance. Try to limit the number of calls to this function to avoid unnecessary update.

 **Note:** This does not trigger a direct update of the **TileMapLayer**, the update will be done at the end of the frame as usual (unless you call [update_internals()](class_tilemaplayer.md#class_TileMapLayer_method_update_internals)).

---

<span id="class_TileMapLayer_method_set_cell"></span>

void **set_cell** ( coords: [Vector2i](class_vector2i.md#class_Vector2i), source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = 0 ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_set_cell)

Sets the tile identifiers for the cell at coordinates `coords`. Each tile of the [TileSet](class_tileset.md#class_TileSet) is identified using three parts:

- The source identifier `source_id` identifies a [TileSetSource](class_tilesetsource.md#class_TileSetSource) identifier. See [TileSet.set_source_id()](class_tileset.md#class_TileSet_method_set_source_id),

- The atlas coordinate identifier `atlas_coords` identifies a tile coordinates in the atlas (if the source is a [TileSetAtlasSource](class_tilesetatlassource.md#class_TileSetAtlasSource)). For [TileSetScenesCollectionSource](class_tilesetscenescollectionsource.md#class_TileSetScenesCollectionSource) it should always be `Vector2i(0, 0)`,

- The alternative tile identifier `alternative_tile` identifies a tile alternative in the atlas (if the source is a [TileSetAtlasSource](class_tilesetatlassource.md#class_TileSetAtlasSource)), and the scene for a [TileSetScenesCollectionSource](class_tilesetscenescollectionsource.md#class_TileSetScenesCollectionSource).

If `source_id` is set to `-1`, `atlas_coords` to `Vector2i(-1, -1)`, or `alternative_tile` to `-1`, the cell will be erased. An erased cell gets **all** its identifiers automatically set to their respective invalid values, namely `-1`, `Vector2i(-1, -1)` and `-1`.

---

<span id="class_TileMapLayer_method_set_cells_terrain_connect"></span>

void **set_cells_terrain_connect** ( cells: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], terrain_set: [int](class_int.md#class_int), terrain: [int](class_int.md#class_int), ignore_empty_terrains: [bool](class_bool.md#class_bool) = true ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_set_cells_terrain_connect)

Update all the cells in the `cells` coordinates array so that they use the given `terrain` for the given `terrain_set`. If an updated cell has the same terrain as one of its neighboring cells, this function tries to join the two. This function might update neighboring tiles if needed to create correct terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.

 **Note:** To work correctly, this method requires the **TileMapLayer**'s TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.

---

<span id="class_TileMapLayer_method_set_cells_terrain_path"></span>

void **set_cells_terrain_path** ( path: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], terrain_set: [int](class_int.md#class_int), terrain: [int](class_int.md#class_int), ignore_empty_terrains: [bool](class_bool.md#class_bool) = true ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_set_cells_terrain_path)

Update all the cells in the `path` coordinates array so that they use the given `terrain` for the given `terrain_set`. The function will also connect two successive cell in the path with the same terrain. This function might update neighboring tiles if needed to create correct terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.

 **Note:** To work correctly, this method requires the **TileMapLayer**'s TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.

---

<span id="class_TileMapLayer_method_set_navigation_map"></span>

void **set_navigation_map** ( map: [RID](class_rid.md#class_RID) ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_set_navigation_map)

Sets a custom `map` as a [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) navigation map. If not set, uses the default [World2D](class_world2d.md#class_World2D) navigation map instead.

---

<span id="class_TileMapLayer_method_set_pattern"></span>

void **set_pattern** ( position: [Vector2i](class_vector2i.md#class_Vector2i), pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_set_pattern)

Pastes the [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) at the given `position` in the tile map. See also [get_pattern()](class_tilemaplayer.md#class_TileMapLayer_method_get_pattern).

---

<span id="class_TileMapLayer_method_update_internals"></span>

void **update_internals** ( ) [🔗](class_tilemaplayer.md#class_TileMapLayer_method_update_internals)

Triggers a direct update of the **TileMapLayer**. Usually, calling this function is not needed, as **TileMapLayer** node updates automatically when one of its properties or cells is modified.

However, for performance reasons, those updates are batched and delayed to the end of the frame. Calling this function will force the **TileMapLayer** to update right away instead.

 **Warning:** Updating the **TileMapLayer** is computationally expensive and may impact performance. Try to limit the number of updates and how many tiles they impact.
