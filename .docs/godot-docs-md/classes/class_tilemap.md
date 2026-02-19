.. meta::
	:keywords: gridmap

<span id="class_TileMap"></span>

## TileMap

**Deprecated:** Use multiple [TileMapLayer](class_tilemaplayer.md#class_TileMapLayer) nodes instead. To convert a TileMap to a set of TileMapLayer nodes, open the TileMap bottom panel with the node selected, click the toolbox icon in the top-right corner and choose 'Extract TileMap layers as individual TileMapLayer nodes'.

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Node for 2D tile-based maps.

### Description

Node for 2D tile-based maps. Tilemaps use a [TileSet](class_tileset.md#class_TileSet) which contain a list of tiles which are used to create grid-based maps. A TileMap may have several layers, layouting tiles on top of each other.

For performance reasons, all TileMap updates are batched at the end of a frame. Notably, this means that scene tiles from a [TileSetScenesCollectionSource](class_tilesetscenescollectionsource.md#class_TileSetScenesCollectionSource) may be initialized after their parent. This is only queued when inside the scene tree.

To force an update earlier on, call [update_internals()](class_tilemap.md#class_TileMap_method_update_internals).

 **Note:** For performance and compatibility reasons, the coordinates serialized by **TileMap** are limited to 16-bit signed integers, i.e. the range for X and Y coordinates is from `-32768` to `32767`. When saving tile data, tiles outside this range are wrapped.

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


| [bool](class_bool.md#class_bool) | [collision_animatable](class_tilemap.md#class_TileMap_property_collision_animatable) | `false` |
| --- | --- | --- |
| [VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) | [collision_visibility_mode](class_tilemap.md#class_TileMap_property_collision_visibility_mode) | `0` |
| [VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) | [navigation_visibility_mode](class_tilemap.md#class_TileMap_property_navigation_visibility_mode) | `0` |
| [int](class_int.md#class_int) | [rendering_quadrant_size](class_tilemap.md#class_TileMap_property_rendering_quadrant_size) | `16` |
| [TileSet](class_tileset.md#class_TileSet) | [tile_set](class_tilemap.md#class_TileMap_property_tile_set) |

### Methods


| void | [_tile_data_runtime_update](class_tilemap.md#class_TileMap_private_method__tile_data_runtime_update) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), tile_data: [TileData](class_tiledata.md#class_TileData) ) virtual |
| --- | --- |
| [bool](class_bool.md#class_bool) | [_use_tile_data_runtime_update](class_tilemap.md#class_TileMap_private_method__use_tile_data_runtime_update) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i) ) virtual |
| void | [add_layer](class_tilemap.md#class_TileMap_method_add_layer) ( to_position: [int](class_int.md#class_int) ) |
| void | [clear](class_tilemap.md#class_TileMap_method_clear) ( ) |
| void | [clear_layer](class_tilemap.md#class_TileMap_method_clear_layer) ( layer: [int](class_int.md#class_int) ) |
| void | [erase_cell](class_tilemap.md#class_TileMap_method_erase_cell) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [fix_invalid_tiles](class_tilemap.md#class_TileMap_method_fix_invalid_tiles) ( ) |
| void | [force_update](class_tilemap.md#class_TileMap_method_force_update) ( layer: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [get_cell_alternative_tile](class_tilemap.md#class_TileMap_method_get_cell_alternative_tile) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_cell_atlas_coords](class_tilemap.md#class_TileMap_method_get_cell_atlas_coords) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) const |
| [int](class_int.md#class_int) | [get_cell_source_id](class_tilemap.md#class_TileMap_method_get_cell_source_id) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) const |
| [TileData](class_tiledata.md#class_TileData) | [get_cell_tile_data](class_tilemap.md#class_TileMap_method_get_cell_tile_data) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_coords_for_body_rid](class_tilemap.md#class_TileMap_method_get_coords_for_body_rid) ( body: [RID](class_rid.md#class_RID) ) |
| [int](class_int.md#class_int) | [get_layer_for_body_rid](class_tilemap.md#class_TileMap_method_get_layer_for_body_rid) ( body: [RID](class_rid.md#class_RID) ) |
| [Color](class_color.md#class_Color) | [get_layer_modulate](class_tilemap.md#class_TileMap_method_get_layer_modulate) ( layer: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_layer_name](class_tilemap.md#class_TileMap_method_get_layer_name) ( layer: [int](class_int.md#class_int) ) const |
| [RID](class_rid.md#class_RID) | [get_layer_navigation_map](class_tilemap.md#class_TileMap_method_get_layer_navigation_map) ( layer: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_layer_y_sort_origin](class_tilemap.md#class_TileMap_method_get_layer_y_sort_origin) ( layer: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_layer_z_index](class_tilemap.md#class_TileMap_method_get_layer_z_index) ( layer: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_layers_count](class_tilemap.md#class_TileMap_method_get_layers_count) ( ) const |
| [RID](class_rid.md#class_RID) | [get_navigation_map](class_tilemap.md#class_TileMap_method_get_navigation_map) ( layer: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_neighbor_cell](class_tilemap.md#class_TileMap_method_get_neighbor_cell) ( coords: [Vector2i](class_vector2i.md#class_Vector2i), neighbor: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) ) const |
| [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) | [get_pattern](class_tilemap.md#class_TileMap_method_get_pattern) ( layer: [int](class_int.md#class_int), coords_array: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] ) |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [get_surrounding_cells](class_tilemap.md#class_TileMap_method_get_surrounding_cells) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [get_used_cells](class_tilemap.md#class_TileMap_method_get_used_cells) ( layer: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [get_used_cells_by_id](class_tilemap.md#class_TileMap_method_get_used_cells_by_id) ( layer: [int](class_int.md#class_int), source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = -1 ) const |
| [Rect2i](class_rect2i.md#class_Rect2i) | [get_used_rect](class_tilemap.md#class_TileMap_method_get_used_rect) ( ) const |
| [bool](class_bool.md#class_bool) | [is_cell_flipped_h](class_tilemap.md#class_TileMap_method_is_cell_flipped_h) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [is_cell_flipped_v](class_tilemap.md#class_TileMap_method_is_cell_flipped_v) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [is_cell_transposed](class_tilemap.md#class_TileMap_method_is_cell_transposed) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [is_layer_enabled](class_tilemap.md#class_TileMap_method_is_layer_enabled) ( layer: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_layer_navigation_enabled](class_tilemap.md#class_TileMap_method_is_layer_navigation_enabled) ( layer: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_layer_y_sort_enabled](class_tilemap.md#class_TileMap_method_is_layer_y_sort_enabled) ( layer: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [local_to_map](class_tilemap.md#class_TileMap_method_local_to_map) ( local_position: [Vector2](class_vector2.md#class_Vector2) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [map_pattern](class_tilemap.md#class_TileMap_method_map_pattern) ( position_in_tilemap: [Vector2i](class_vector2i.md#class_Vector2i), coords_in_pattern: [Vector2i](class_vector2i.md#class_Vector2i), pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) ) |
| [Vector2](class_vector2.md#class_Vector2) | [map_to_local](class_tilemap.md#class_TileMap_method_map_to_local) ( map_position: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| void | [move_layer](class_tilemap.md#class_TileMap_method_move_layer) ( layer: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) |
| void | [notify_runtime_tile_data_update](class_tilemap.md#class_TileMap_method_notify_runtime_tile_data_update) ( layer: [int](class_int.md#class_int) = -1 ) |
| void | [remove_layer](class_tilemap.md#class_TileMap_method_remove_layer) ( layer: [int](class_int.md#class_int) ) |
| void | [set_cell](class_tilemap.md#class_TileMap_method_set_cell) ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = 0 ) |
| void | [set_cells_terrain_connect](class_tilemap.md#class_TileMap_method_set_cells_terrain_connect) ( layer: [int](class_int.md#class_int), cells: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], terrain_set: [int](class_int.md#class_int), terrain: [int](class_int.md#class_int), ignore_empty_terrains: [bool](class_bool.md#class_bool) = true ) |
| void | [set_cells_terrain_path](class_tilemap.md#class_TileMap_method_set_cells_terrain_path) ( layer: [int](class_int.md#class_int), path: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], terrain_set: [int](class_int.md#class_int), terrain: [int](class_int.md#class_int), ignore_empty_terrains: [bool](class_bool.md#class_bool) = true ) |
| void | [set_layer_enabled](class_tilemap.md#class_TileMap_method_set_layer_enabled) ( layer: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_layer_modulate](class_tilemap.md#class_TileMap_method_set_layer_modulate) ( layer: [int](class_int.md#class_int), modulate: [Color](class_color.md#class_Color) ) |
| void | [set_layer_name](class_tilemap.md#class_TileMap_method_set_layer_name) ( layer: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [set_layer_navigation_enabled](class_tilemap.md#class_TileMap_method_set_layer_navigation_enabled) ( layer: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_layer_navigation_map](class_tilemap.md#class_TileMap_method_set_layer_navigation_map) ( layer: [int](class_int.md#class_int), map: [RID](class_rid.md#class_RID) ) |
| void | [set_layer_y_sort_enabled](class_tilemap.md#class_TileMap_method_set_layer_y_sort_enabled) ( layer: [int](class_int.md#class_int), y_sort_enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_layer_y_sort_origin](class_tilemap.md#class_TileMap_method_set_layer_y_sort_origin) ( layer: [int](class_int.md#class_int), y_sort_origin: [int](class_int.md#class_int) ) |
| void | [set_layer_z_index](class_tilemap.md#class_TileMap_method_set_layer_z_index) ( layer: [int](class_int.md#class_int), z_index: [int](class_int.md#class_int) ) |
| void | [set_navigation_map](class_tilemap.md#class_TileMap_method_set_navigation_map) ( layer: [int](class_int.md#class_int), map: [RID](class_rid.md#class_RID) ) |
| void | [set_pattern](class_tilemap.md#class_TileMap_method_set_pattern) ( layer: [int](class_int.md#class_int), position: [Vector2i](class_vector2i.md#class_Vector2i), pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) ) |
| void | [update_internals](class_tilemap.md#class_TileMap_method_update_internals) ( ) |

---

### Signals

<span id="class_TileMap_signal_changed"></span>

**changed** ( ) [🔗](class_tilemap.md#class_TileMap_signal_changed)

Emitted when the [TileSet](class_tileset.md#class_TileSet) of this TileMap changes.

---

### Enumerations

<span id="enum_TileMap_VisibilityMode"></span>

enum **VisibilityMode**: [🔗](class_tilemap.md#enum_TileMap_VisibilityMode)

<span id="class_TileMap_constant_VISIBILITY_MODE_DEFAULT"></span>

[VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) **VISIBILITY_MODE_DEFAULT** = `0`

Use the debug settings to determine visibility.

<span id="class_TileMap_constant_VISIBILITY_MODE_FORCE_HIDE"></span>

[VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) **VISIBILITY_MODE_FORCE_HIDE** = `2`

Always hide.

<span id="class_TileMap_constant_VISIBILITY_MODE_FORCE_SHOW"></span>

[VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) **VISIBILITY_MODE_FORCE_SHOW** = `1`

Always show.

---

### Property Descriptions

<span id="class_TileMap_property_collision_animatable"></span>

[bool](class_bool.md#class_bool) **collision_animatable** = `false` [🔗](class_tilemap.md#class_TileMap_property_collision_animatable)

- void **set_collision_animatable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collision_animatable** ( )

If enabled, the TileMap will see its collisions synced to the physics tick and change its collision type from static to kinematic. This is required to create TileMap-based moving platform.

 **Note:** Enabling [collision_animatable](class_tilemap.md#class_TileMap_property_collision_animatable) may have a small performance impact, only do it if the TileMap is moving and has colliding tiles.

---

<span id="class_TileMap_property_collision_visibility_mode"></span>

[VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) **collision_visibility_mode** = `0` [🔗](class_tilemap.md#class_TileMap_property_collision_visibility_mode)

- void **set_collision_visibility_mode** ( value: [VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) )
- [VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) **get_collision_visibility_mode** ( )

Show or hide the TileMap's collision shapes. If set to [VISIBILITY_MODE_DEFAULT](class_tilemap.md#class_TileMap_constant_VISIBILITY_MODE_DEFAULT), this depends on the show collision debug settings.

---

<span id="class_TileMap_property_navigation_visibility_mode"></span>

[VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) **navigation_visibility_mode** = `0` [🔗](class_tilemap.md#class_TileMap_property_navigation_visibility_mode)

- void **set_navigation_visibility_mode** ( value: [VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) )
- [VisibilityMode](class_tilemap.md#enum_TileMap_VisibilityMode) **get_navigation_visibility_mode** ( )

Show or hide the TileMap's navigation meshes. If set to [VISIBILITY_MODE_DEFAULT](class_tilemap.md#class_TileMap_constant_VISIBILITY_MODE_DEFAULT), this depends on the show navigation debug settings.

---

<span id="class_TileMap_property_rendering_quadrant_size"></span>

[int](class_int.md#class_int) **rendering_quadrant_size** = `16` [🔗](class_tilemap.md#class_TileMap_property_rendering_quadrant_size)

- void **set_rendering_quadrant_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_rendering_quadrant_size** ( )

The TileMap's quadrant size. A quadrant is a group of tiles to be drawn together on a single canvas item, for optimization purposes. [rendering_quadrant_size](class_tilemap.md#class_TileMap_property_rendering_quadrant_size) defines the length of a square's side, in the map's coordinate system, that forms the quadrant. Thus, the default quadrant size groups together `16 * 16 = 256` tiles.

The quadrant size does not apply on Y-sorted layers, as tiles are grouped by Y position instead in that case.

 **Note:** As quadrants are created according to the map's coordinate system, the quadrant's "square shape" might not look like square in the TileMap's local coordinate system.

---

<span id="class_TileMap_property_tile_set"></span>

[TileSet](class_tileset.md#class_TileSet) **tile_set** [🔗](class_tilemap.md#class_TileMap_property_tile_set)

- void **set_tileset** ( value: [TileSet](class_tileset.md#class_TileSet) )
- [TileSet](class_tileset.md#class_TileSet) **get_tileset** ( )

The [TileSet](class_tileset.md#class_TileSet) used by this **TileMap**. The textures, collisions, and additional behavior of all available tiles are stored here.

---

### Method Descriptions

<span id="class_TileMap_private_method__tile_data_runtime_update"></span>

void **_tile_data_runtime_update** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), tile_data: [TileData](class_tiledata.md#class_TileData) ) *virtual* [🔗](class_tilemap.md#class_TileMap_private_method__tile_data_runtime_update)

Called with a TileData object about to be used internally by the TileMap, allowing its modification at runtime.

This method is only called if [_use_tile_data_runtime_update()](class_tilemap.md#class_TileMap_private_method__use_tile_data_runtime_update) is implemented and returns `true` for the given tile `coords` and `layer`.

 **Warning:** The `tile_data` object's sub-resources are the same as the one in the TileSet. Modifying them might impact the whole TileSet. Instead, make sure to duplicate those resources.

 **Note:** If the properties of `tile_data` object should change over time, use [notify_runtime_tile_data_update()](class_tilemap.md#class_TileMap_method_notify_runtime_tile_data_update) to notify the TileMap it needs an update.

---

<span id="class_TileMap_private_method__use_tile_data_runtime_update"></span>

[bool](class_bool.md#class_bool) **_use_tile_data_runtime_update** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* [🔗](class_tilemap.md#class_TileMap_private_method__use_tile_data_runtime_update)

Should return `true` if the tile at coordinates `coords` on layer `layer` requires a runtime update.

 **Warning:** Make sure this function only return `true` when needed. Any tile processed at runtime without a need for it will imply a significant performance penalty.

 **Note:** If the result of this function should changed, use [notify_runtime_tile_data_update()](class_tilemap.md#class_TileMap_method_notify_runtime_tile_data_update) to notify the TileMap it needs an update.

---

<span id="class_TileMap_method_add_layer"></span>

void **add_layer** ( to_position: [int](class_int.md#class_int) ) [🔗](class_tilemap.md#class_TileMap_method_add_layer)

Adds a layer at the given position `to_position` in the array. If `to_position` is negative, the position is counted from the end, with `-1` adding the layer at the end of the array.

---

<span id="class_TileMap_method_clear"></span>

void **clear** ( ) [🔗](class_tilemap.md#class_TileMap_method_clear)

Clears all cells.

---

<span id="class_TileMap_method_clear_layer"></span>

void **clear_layer** ( layer: [int](class_int.md#class_int) ) [🔗](class_tilemap.md#class_TileMap_method_clear_layer)

Clears all cells on the given layer.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_erase_cell"></span>

void **erase_cell** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_tilemap.md#class_TileMap_method_erase_cell)

Erases the cell on layer `layer` at coordinates `coords`.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_fix_invalid_tiles"></span>

void **fix_invalid_tiles** ( ) [🔗](class_tilemap.md#class_TileMap_method_fix_invalid_tiles)

Clears cells that do not exist in the tileset.

---

<span id="class_TileMap_method_force_update"></span>

void **force_update** ( layer: [int](class_int.md#class_int) = -1 ) [🔗](class_tilemap.md#class_TileMap_method_force_update)

**Deprecated:** Use [notify_runtime_tile_data_update()](class_tilemap.md#class_TileMap_method_notify_runtime_tile_data_update) and/or [update_internals()](class_tilemap.md#class_TileMap_method_update_internals) instead.

Forces the TileMap and the layer `layer` to update.

---

<span id="class_TileMap_method_get_cell_alternative_tile"></span>

[int](class_int.md#class_int) **get_cell_alternative_tile** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_cell_alternative_tile)

Returns the tile alternative ID of the cell on layer `layer` at `coords`.

If `use_proxies` is `false`, ignores the [TileSet](class_tileset.md#class_TileSet)'s tile proxies, returning the raw alternative identifier. See [TileSet.map_tile_proxy()](class_tileset.md#class_TileSet_method_map_tile_proxy).

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_cell_atlas_coords"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_cell_atlas_coords** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_cell_atlas_coords)

Returns the tile atlas coordinates ID of the cell on layer `layer` at coordinates `coords`. Returns `Vector2i(-1, -1)` if the cell does not exist.

If `use_proxies` is `false`, ignores the [TileSet](class_tileset.md#class_TileSet)'s tile proxies, returning the raw atlas coordinate identifier. See [TileSet.map_tile_proxy()](class_tileset.md#class_TileSet_method_map_tile_proxy).

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_cell_source_id"></span>

[int](class_int.md#class_int) **get_cell_source_id** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_cell_source_id)

Returns the tile source ID of the cell on layer `layer` at coordinates `coords`. Returns `-1` if the cell does not exist.

If `use_proxies` is `false`, ignores the [TileSet](class_tileset.md#class_TileSet)'s tile proxies, returning the raw source identifier. See [TileSet.map_tile_proxy()](class_tileset.md#class_TileSet_method_map_tile_proxy).

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_cell_tile_data"></span>

[TileData](class_tiledata.md#class_TileData) **get_cell_tile_data** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_cell_tile_data)

Returns the [TileData](class_tiledata.md#class_TileData) object associated with the given cell, or `null` if the cell does not exist or is not a [TileSetAtlasSource](class_tilesetatlassource.md#class_TileSetAtlasSource).

If `layer` is negative, the layers are accessed from the last one.

::

    func get_clicked_tile_power():
        var clicked_cell = tile_map.local_to_map(tile_map.get_local_mouse_position())
        var data = tile_map.get_cell_tile_data(0, clicked_cell)
        if data:
            return data.get_custom_data("power")
        else:
            return 0

If `use_proxies` is `false`, ignores the [TileSet](class_tileset.md#class_TileSet)'s tile proxies. See [TileSet.map_tile_proxy()](class_tileset.md#class_TileSet_method_map_tile_proxy).

---

<span id="class_TileMap_method_get_coords_for_body_rid"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_coords_for_body_rid** ( body: [RID](class_rid.md#class_RID) ) [🔗](class_tilemap.md#class_TileMap_method_get_coords_for_body_rid)

Returns the coordinates of the tile for given physics body RID. Such RID can be retrieved from [KinematicCollision2D.get_collider_rid()](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_rid), when colliding with a tile.

---

<span id="class_TileMap_method_get_layer_for_body_rid"></span>

[int](class_int.md#class_int) **get_layer_for_body_rid** ( body: [RID](class_rid.md#class_RID) ) [🔗](class_tilemap.md#class_TileMap_method_get_layer_for_body_rid)

Returns the tilemap layer of the tile for given physics body RID. Such RID can be retrieved from [KinematicCollision2D.get_collider_rid()](class_kinematiccollision2d.md#class_KinematicCollision2D_method_get_collider_rid), when colliding with a tile.

---

<span id="class_TileMap_method_get_layer_modulate"></span>

[Color](class_color.md#class_Color) **get_layer_modulate** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_layer_modulate)

Returns a TileMap layer's modulate.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_layer_name"></span>

[String](class_string.md#class_String) **get_layer_name** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_layer_name)

Returns a TileMap layer's name.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_layer_navigation_map"></span>

[RID](class_rid.md#class_RID) **get_layer_navigation_map** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_layer_navigation_map)

Returns the [RID](class_rid.md#class_RID) of the [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) navigation map assigned to the specified TileMap layer `layer`.

By default the TileMap uses the default [World2D](class_world2d.md#class_World2D) navigation map for the first TileMap layer. For each additional TileMap layer a new navigation map is created for the additional layer.

In order to make [NavigationAgent2D](class_navigationagent2d.md#class_NavigationAgent2D) switch between TileMap layer navigation maps use [NavigationAgent2D.set_navigation_map()](class_navigationagent2d.md#class_NavigationAgent2D_method_set_navigation_map) with the navigation map received from [get_layer_navigation_map()](class_tilemap.md#class_TileMap_method_get_layer_navigation_map).

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_layer_y_sort_origin"></span>

[int](class_int.md#class_int) **get_layer_y_sort_origin** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_layer_y_sort_origin)

Returns a TileMap layer's Y sort origin.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_layer_z_index"></span>

[int](class_int.md#class_int) **get_layer_z_index** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_layer_z_index)

Returns a TileMap layer's Z-index value.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_layers_count"></span>

[int](class_int.md#class_int) **get_layers_count** ( ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_layers_count)

Returns the number of layers in the TileMap.

---

<span id="class_TileMap_method_get_navigation_map"></span>

[RID](class_rid.md#class_RID) **get_navigation_map** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_navigation_map)

**Deprecated:** Use [get_layer_navigation_map()](class_tilemap.md#class_TileMap_method_get_layer_navigation_map) instead.

Returns the [RID](class_rid.md#class_RID) of the [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) navigation map assigned to the specified TileMap layer `layer`.

---

<span id="class_TileMap_method_get_neighbor_cell"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_neighbor_cell** ( coords: [Vector2i](class_vector2i.md#class_Vector2i), neighbor: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_neighbor_cell)

Returns the neighboring cell to the one at coordinates `coords`, identified by the `neighbor` direction. This method takes into account the different layouts a TileMap can take.

---

<span id="class_TileMap_method_get_pattern"></span>

[TileMapPattern](class_tilemappattern.md#class_TileMapPattern) **get_pattern** ( layer: [int](class_int.md#class_int), coords_array: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] ) [🔗](class_tilemap.md#class_TileMap_method_get_pattern)

Creates a new [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) from the given layer and set of cells.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_surrounding_cells"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **get_surrounding_cells** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_tilemap.md#class_TileMap_method_get_surrounding_cells)

Returns the list of all neighbourings cells to the one at `coords`.

---

<span id="class_TileMap_method_get_used_cells"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **get_used_cells** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_used_cells)

Returns a [Vector2i](class_vector2i.md#class_Vector2i) array with the positions of all cells containing a tile in the given layer. A cell is considered empty if its source identifier equals -1, its atlas coordinates identifiers is `Vector2(-1, -1)` and its alternative identifier is -1.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_used_cells_by_id"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **get_used_cells_by_id** ( layer: [int](class_int.md#class_int), source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_used_cells_by_id)

Returns a [Vector2i](class_vector2i.md#class_Vector2i) array with the positions of all cells containing a tile in the given layer. Tiles may be filtered according to their source (`source_id`), their atlas coordinates (`atlas_coords`) or alternative id (`alternative_tile`).

If a parameter has its value set to the default one, this parameter is not used to filter a cell. Thus, if all parameters have their respective default value, this method returns the same result as [get_used_cells()](class_tilemap.md#class_TileMap_method_get_used_cells).

A cell is considered empty if its source identifier equals -1, its atlas coordinates identifiers is `Vector2(-1, -1)` and its alternative identifier is -1.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_get_used_rect"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **get_used_rect** ( ) *const* [🔗](class_tilemap.md#class_TileMap_method_get_used_rect)

Returns a rectangle enclosing the used (non-empty) tiles of the map, including all layers.

---

<span id="class_TileMap_method_is_cell_flipped_h"></span>

[bool](class_bool.md#class_bool) **is_cell_flipped_h** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tilemap.md#class_TileMap_method_is_cell_flipped_h)

Returns `true` if the cell on layer `layer` at coordinates `coords` is flipped horizontally. The result is valid only for atlas sources.

---

<span id="class_TileMap_method_is_cell_flipped_v"></span>

[bool](class_bool.md#class_bool) **is_cell_flipped_v** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tilemap.md#class_TileMap_method_is_cell_flipped_v)

Returns `true` if the cell on layer `layer` at coordinates `coords` is flipped vertically. The result is valid only for atlas sources.

---

<span id="class_TileMap_method_is_cell_transposed"></span>

[bool](class_bool.md#class_bool) **is_cell_transposed** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), use_proxies: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tilemap.md#class_TileMap_method_is_cell_transposed)

Returns `true` if the cell on layer `layer` at coordinates `coords` is transposed. The result is valid only for atlas sources.

---

<span id="class_TileMap_method_is_layer_enabled"></span>

[bool](class_bool.md#class_bool) **is_layer_enabled** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_is_layer_enabled)

Returns if a layer is enabled.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_is_layer_navigation_enabled"></span>

[bool](class_bool.md#class_bool) **is_layer_navigation_enabled** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_is_layer_navigation_enabled)

Returns if a layer's built-in navigation regions generation is enabled.

---

<span id="class_TileMap_method_is_layer_y_sort_enabled"></span>

[bool](class_bool.md#class_bool) **is_layer_y_sort_enabled** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_tilemap.md#class_TileMap_method_is_layer_y_sort_enabled)

Returns if a layer Y-sorts its tiles.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_local_to_map"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **local_to_map** ( local_position: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_tilemap.md#class_TileMap_method_local_to_map)

Returns the map coordinates of the cell containing the given `local_position`. If `local_position` is in global coordinates, consider using [Node2D.to_local()](class_node2d.md#class_Node2D_method_to_local) before passing it to this method. See also [map_to_local()](class_tilemap.md#class_TileMap_method_map_to_local).

---

<span id="class_TileMap_method_map_pattern"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **map_pattern** ( position_in_tilemap: [Vector2i](class_vector2i.md#class_Vector2i), coords_in_pattern: [Vector2i](class_vector2i.md#class_Vector2i), pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) ) [🔗](class_tilemap.md#class_TileMap_method_map_pattern)

Returns for the given coordinate `coords_in_pattern` in a [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) the corresponding cell coordinates if the pattern was pasted at the `position_in_tilemap` coordinates (see [set_pattern()](class_tilemap.md#class_TileMap_method_set_pattern)). This mapping is required as in half-offset tile shapes, the mapping might not work by calculating `position_in_tile_map + coords_in_pattern`.

---

<span id="class_TileMap_method_map_to_local"></span>

[Vector2](class_vector2.md#class_Vector2) **map_to_local** ( map_position: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemap.md#class_TileMap_method_map_to_local)

Returns the centered position of a cell in the TileMap's local coordinate space. To convert the returned value into global coordinates, use [Node2D.to_global()](class_node2d.md#class_Node2D_method_to_global). See also [local_to_map()](class_tilemap.md#class_TileMap_method_local_to_map).

 **Note:** This may not correspond to the visual position of the tile, i.e. it ignores the [TileData.texture_origin](class_tiledata.md#class_TileData_property_texture_origin) property of individual tiles.

---

<span id="class_TileMap_method_move_layer"></span>

void **move_layer** ( layer: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) [🔗](class_tilemap.md#class_TileMap_method_move_layer)

Moves the layer at index `layer` to the given position `to_position` in the array.

---

<span id="class_TileMap_method_notify_runtime_tile_data_update"></span>

void **notify_runtime_tile_data_update** ( layer: [int](class_int.md#class_int) = -1 ) [🔗](class_tilemap.md#class_TileMap_method_notify_runtime_tile_data_update)

Notifies the TileMap node that calls to [_use_tile_data_runtime_update()](class_tilemap.md#class_TileMap_private_method__use_tile_data_runtime_update) or [_tile_data_runtime_update()](class_tilemap.md#class_TileMap_private_method__tile_data_runtime_update) will lead to different results. This will thus trigger a TileMap update.

If `layer` is provided, only notifies changes for the given layer. Providing the `layer` argument (when applicable) is usually preferred for performance reasons.

 **Warning:** Updating the TileMap is computationally expensive and may impact performance. Try to limit the number of calls to this function to avoid unnecessary update.

 **Note:** This does not trigger a direct update of the TileMap, the update will be done at the end of the frame as usual (unless you call [update_internals()](class_tilemap.md#class_TileMap_method_update_internals)).

---

<span id="class_TileMap_method_remove_layer"></span>

void **remove_layer** ( layer: [int](class_int.md#class_int) ) [🔗](class_tilemap.md#class_TileMap_method_remove_layer)

Removes the layer at index `layer`.

---

<span id="class_TileMap_method_set_cell"></span>

void **set_cell** ( layer: [int](class_int.md#class_int), coords: [Vector2i](class_vector2i.md#class_Vector2i), source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = 0 ) [🔗](class_tilemap.md#class_TileMap_method_set_cell)

Sets the tile identifiers for the cell on layer `layer` at coordinates `coords`. Each tile of the [TileSet](class_tileset.md#class_TileSet) is identified using three parts:

- The source identifier `source_id` identifies a [TileSetSource](class_tilesetsource.md#class_TileSetSource) identifier. See [TileSet.set_source_id()](class_tileset.md#class_TileSet_method_set_source_id),

- The atlas coordinates identifier `atlas_coords` identifies a tile coordinates in the atlas (if the source is a [TileSetAtlasSource](class_tilesetatlassource.md#class_TileSetAtlasSource)). For [TileSetScenesCollectionSource](class_tilesetscenescollectionsource.md#class_TileSetScenesCollectionSource) it should always be `Vector2i(0, 0)`),

- The alternative tile identifier `alternative_tile` identifies a tile alternative in the atlas (if the source is a [TileSetAtlasSource](class_tilesetatlassource.md#class_TileSetAtlasSource)), and the scene for a [TileSetScenesCollectionSource](class_tilesetscenescollectionsource.md#class_TileSetScenesCollectionSource).

If `source_id` is set to `-1`, `atlas_coords` to `Vector2i(-1, -1)` or `alternative_tile` to `-1`, the cell will be erased. An erased cell gets **all** its identifiers automatically set to their respective invalid values, namely `-1`, `Vector2i(-1, -1)` and `-1`.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_set_cells_terrain_connect"></span>

void **set_cells_terrain_connect** ( layer: [int](class_int.md#class_int), cells: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], terrain_set: [int](class_int.md#class_int), terrain: [int](class_int.md#class_int), ignore_empty_terrains: [bool](class_bool.md#class_bool) = true ) [🔗](class_tilemap.md#class_TileMap_method_set_cells_terrain_connect)

Update all the cells in the `cells` coordinates array so that they use the given `terrain` for the given `terrain_set`. If an updated cell has the same terrain as one of its neighboring cells, this function tries to join the two. This function might update neighboring tiles if needed to create correct terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.

If `layer` is negative, the layers are accessed from the last one.

 **Note:** To work correctly, this method requires the TileMap's TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.

---

<span id="class_TileMap_method_set_cells_terrain_path"></span>

void **set_cells_terrain_path** ( layer: [int](class_int.md#class_int), path: [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\], terrain_set: [int](class_int.md#class_int), terrain: [int](class_int.md#class_int), ignore_empty_terrains: [bool](class_bool.md#class_bool) = true ) [🔗](class_tilemap.md#class_TileMap_method_set_cells_terrain_path)

Update all the cells in the `path` coordinates array so that they use the given `terrain` for the given `terrain_set`. The function will also connect two successive cell in the path with the same terrain. This function might update neighboring tiles if needed to create correct terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.

If `layer` is negative, the layers are accessed from the last one.

 **Note:** To work correctly, this method requires the TileMap's TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.

---

<span id="class_TileMap_method_set_layer_enabled"></span>

void **set_layer_enabled** ( layer: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_tilemap.md#class_TileMap_method_set_layer_enabled)

Enables or disables the layer `layer`. A disabled layer is not processed at all (no rendering, no physics, etc.).

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_set_layer_modulate"></span>

void **set_layer_modulate** ( layer: [int](class_int.md#class_int), modulate: [Color](class_color.md#class_Color) ) [🔗](class_tilemap.md#class_TileMap_method_set_layer_modulate)

Sets a layer's color. It will be multiplied by tile's color and TileMap's modulate.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_set_layer_name"></span>

void **set_layer_name** ( layer: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_tilemap.md#class_TileMap_method_set_layer_name)

Sets a layer's name. This is mostly useful in the editor.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_set_layer_navigation_enabled"></span>

void **set_layer_navigation_enabled** ( layer: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_tilemap.md#class_TileMap_method_set_layer_navigation_enabled)

Enables or disables a layer's built-in navigation regions generation. Disable this if you need to bake navigation regions from a TileMap using a [NavigationRegion2D](class_navigationregion2d.md#class_NavigationRegion2D) node.

---

<span id="class_TileMap_method_set_layer_navigation_map"></span>

void **set_layer_navigation_map** ( layer: [int](class_int.md#class_int), map: [RID](class_rid.md#class_RID) ) [🔗](class_tilemap.md#class_TileMap_method_set_layer_navigation_map)

Assigns `map` as a [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) navigation map for the specified TileMap layer `layer`.

By default the TileMap uses the default [World2D](class_world2d.md#class_World2D) navigation map for the first TileMap layer. For each additional TileMap layer a new navigation map is created for the additional layer.

In order to make [NavigationAgent2D](class_navigationagent2d.md#class_NavigationAgent2D) switch between TileMap layer navigation maps use [NavigationAgent2D.set_navigation_map()](class_navigationagent2d.md#class_NavigationAgent2D_method_set_navigation_map) with the navigation map received from [get_layer_navigation_map()](class_tilemap.md#class_TileMap_method_get_layer_navigation_map).

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_set_layer_y_sort_enabled"></span>

void **set_layer_y_sort_enabled** ( layer: [int](class_int.md#class_int), y_sort_enabled: [bool](class_bool.md#class_bool) ) [🔗](class_tilemap.md#class_TileMap_method_set_layer_y_sort_enabled)

Enables or disables a layer's Y-sorting. If a layer is Y-sorted, the layer will behave as a CanvasItem node where each of its tile gets Y-sorted.

Y-sorted layers should usually be on different Z-index values than not Y-sorted layers, otherwise, each of those layer will be Y-sorted as whole with the Y-sorted one. This is usually an undesired behavior.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_set_layer_y_sort_origin"></span>

void **set_layer_y_sort_origin** ( layer: [int](class_int.md#class_int), y_sort_origin: [int](class_int.md#class_int) ) [🔗](class_tilemap.md#class_TileMap_method_set_layer_y_sort_origin)

Sets a layer's Y-sort origin value. This Y-sort origin value is added to each tile's Y-sort origin value.

This allows, for example, to fake a different height level on each layer. This can be useful for top-down view games.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_set_layer_z_index"></span>

void **set_layer_z_index** ( layer: [int](class_int.md#class_int), z_index: [int](class_int.md#class_int) ) [🔗](class_tilemap.md#class_TileMap_method_set_layer_z_index)

Sets a layers Z-index value. This Z-index is added to each tile's Z-index value.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_set_navigation_map"></span>

void **set_navigation_map** ( layer: [int](class_int.md#class_int), map: [RID](class_rid.md#class_RID) ) [🔗](class_tilemap.md#class_TileMap_method_set_navigation_map)

**Deprecated:** Use [set_layer_navigation_map()](class_tilemap.md#class_TileMap_method_set_layer_navigation_map) instead.

Assigns `map` as a [NavigationServer2D](class_navigationserver2d.md#class_NavigationServer2D) navigation map for the specified TileMap layer `layer`.

---

<span id="class_TileMap_method_set_pattern"></span>

void **set_pattern** ( layer: [int](class_int.md#class_int), position: [Vector2i](class_vector2i.md#class_Vector2i), pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) ) [🔗](class_tilemap.md#class_TileMap_method_set_pattern)

Paste the given [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) at the given `position` and `layer` in the tile map.

If `layer` is negative, the layers are accessed from the last one.

---

<span id="class_TileMap_method_update_internals"></span>

void **update_internals** ( ) [🔗](class_tilemap.md#class_TileMap_method_update_internals)

Triggers a direct update of the TileMap. Usually, calling this function is not needed, as TileMap node updates automatically when one of its properties or cells is modified.

However, for performance reasons, those updates are batched and delayed to the end of the frame. Calling this function will force the TileMap to update right away instead.

 **Warning:** Updating the TileMap is computationally expensive and may impact performance. Try to limit the number of updates and how many tiles they impact.
