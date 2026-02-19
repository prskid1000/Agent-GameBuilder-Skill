<span id="class_TileSet"></span>

## TileSet

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Tile library for tilemaps.

### Description

A TileSet is a library of tiles for a [TileMapLayer](class_tilemaplayer.md#class_TileMapLayer). A TileSet handles a list of [TileSetSource](class_tilesetsource.md#class_TileSetSource), each of them storing a set of tiles.

Tiles can either be from a [TileSetAtlasSource](class_tilesetatlassource.md#class_TileSetAtlasSource), which renders tiles out of a texture with support for physics, navigation, etc., or from a [TileSetScenesCollectionSource](class_tilesetscenescollectionsource.md#class_TileSetScenesCollectionSource), which exposes scene-based tiles.

Tiles are referenced by using three IDs: their source ID, their atlas coordinates ID, and their alternative tile ID.

A TileSet can be configured so that its tiles expose more or fewer properties. To do so, the TileSet resources use property layers, which you can add or remove depending on your needs.

For example, adding a physics layer allows giving collision shapes to your tiles. Each layer has dedicated properties (physics layer and mask), so you may add several TileSet physics layers for each type of collision you need.

See the functions to add new layers for more information.

### Tutorials

- [Using Tilemaps](../tutorials/2d/using_tilemaps.md)

- 2D Platformer Demo

- 2D Isometric Demo

- 2D Hexagonal Demo

- 2D Grid-based Navigation with AStarGrid2D Demo

- 2D Role Playing Game (RPG) Demo

- 2D Kinematic Character Demo

### Properties


| [TileLayout](class_tileset.md#enum_TileSet_TileLayout) | [tile_layout](class_tileset.md#class_TileSet_property_tile_layout) | `0` |
| --- | --- | --- |
| [TileOffsetAxis](class_tileset.md#enum_TileSet_TileOffsetAxis) | [tile_offset_axis](class_tileset.md#class_TileSet_property_tile_offset_axis) | `0` |
| [TileShape](class_tileset.md#enum_TileSet_TileShape) | [tile_shape](class_tileset.md#class_TileSet_property_tile_shape) | `0` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [tile_size](class_tileset.md#class_TileSet_property_tile_size) | `Vector2i(16, 16)` |
| [bool](class_bool.md#class_bool) | [uv_clipping](class_tileset.md#class_TileSet_property_uv_clipping) | `false` |

### Methods


| void | [add_custom_data_layer](class_tileset.md#class_TileSet_method_add_custom_data_layer) ( to_position: [int](class_int.md#class_int) = -1 ) |
| --- | --- |
| void | [add_navigation_layer](class_tileset.md#class_TileSet_method_add_navigation_layer) ( to_position: [int](class_int.md#class_int) = -1 ) |
| void | [add_occlusion_layer](class_tileset.md#class_TileSet_method_add_occlusion_layer) ( to_position: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [add_pattern](class_tileset.md#class_TileSet_method_add_pattern) ( pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern), index: [int](class_int.md#class_int) = -1 ) |
| void | [add_physics_layer](class_tileset.md#class_TileSet_method_add_physics_layer) ( to_position: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [add_source](class_tileset.md#class_TileSet_method_add_source) ( source: [TileSetSource](class_tilesetsource.md#class_TileSetSource), atlas_source_id_override: [int](class_int.md#class_int) = -1 ) |
| void | [add_terrain](class_tileset.md#class_TileSet_method_add_terrain) ( terrain_set: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) = -1 ) |
| void | [add_terrain_set](class_tileset.md#class_TileSet_method_add_terrain_set) ( to_position: [int](class_int.md#class_int) = -1 ) |
| void | [cleanup_invalid_tile_proxies](class_tileset.md#class_TileSet_method_cleanup_invalid_tile_proxies) ( ) |
| void | [clear_tile_proxies](class_tileset.md#class_TileSet_method_clear_tile_proxies) ( ) |
| [Array](class_array.md#class_Array) | [get_alternative_level_tile_proxy](class_tileset.md#class_TileSet_method_get_alternative_level_tile_proxy) ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int) ) |
| [Array](class_array.md#class_Array) | [get_coords_level_tile_proxy](class_tileset.md#class_TileSet_method_get_coords_level_tile_proxy) ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [int](class_int.md#class_int) | [get_custom_data_layer_by_name](class_tileset.md#class_TileSet_method_get_custom_data_layer_by_name) ( layer_name: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [get_custom_data_layer_name](class_tileset.md#class_TileSet_method_get_custom_data_layer_name) ( layer_index: [int](class_int.md#class_int) ) const |
| Variant.Type | [get_custom_data_layer_type](class_tileset.md#class_TileSet_method_get_custom_data_layer_type) ( layer_index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_custom_data_layers_count](class_tileset.md#class_TileSet_method_get_custom_data_layers_count) ( ) const |
| [bool](class_bool.md#class_bool) | [get_navigation_layer_layer_value](class_tileset.md#class_TileSet_method_get_navigation_layer_layer_value) ( layer_index: [int](class_int.md#class_int), layer_number: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_navigation_layer_layers](class_tileset.md#class_TileSet_method_get_navigation_layer_layers) ( layer_index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_navigation_layers_count](class_tileset.md#class_TileSet_method_get_navigation_layers_count) ( ) const |
| [int](class_int.md#class_int) | [get_next_source_id](class_tileset.md#class_TileSet_method_get_next_source_id) ( ) const |
| [int](class_int.md#class_int) | [get_occlusion_layer_light_mask](class_tileset.md#class_TileSet_method_get_occlusion_layer_light_mask) ( layer_index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_occlusion_layer_sdf_collision](class_tileset.md#class_TileSet_method_get_occlusion_layer_sdf_collision) ( layer_index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_occlusion_layers_count](class_tileset.md#class_TileSet_method_get_occlusion_layers_count) ( ) const |
| [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) | [get_pattern](class_tileset.md#class_TileSet_method_get_pattern) ( index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [get_patterns_count](class_tileset.md#class_TileSet_method_get_patterns_count) ( ) |
| [int](class_int.md#class_int) | [get_physics_layer_collision_layer](class_tileset.md#class_TileSet_method_get_physics_layer_collision_layer) ( layer_index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_physics_layer_collision_mask](class_tileset.md#class_TileSet_method_get_physics_layer_collision_mask) ( layer_index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_physics_layer_collision_priority](class_tileset.md#class_TileSet_method_get_physics_layer_collision_priority) ( layer_index: [int](class_int.md#class_int) ) const |
| [PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) | [get_physics_layer_physics_material](class_tileset.md#class_TileSet_method_get_physics_layer_physics_material) ( layer_index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_physics_layers_count](class_tileset.md#class_TileSet_method_get_physics_layers_count) ( ) const |
| [TileSetSource](class_tilesetsource.md#class_TileSetSource) | [get_source](class_tileset.md#class_TileSet_method_get_source) ( source_id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_source_count](class_tileset.md#class_TileSet_method_get_source_count) ( ) const |
| [int](class_int.md#class_int) | [get_source_id](class_tileset.md#class_TileSet_method_get_source_id) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_source_level_tile_proxy](class_tileset.md#class_TileSet_method_get_source_level_tile_proxy) ( source_from: [int](class_int.md#class_int) ) |
| [Color](class_color.md#class_Color) | [get_terrain_color](class_tileset.md#class_TileSet_method_get_terrain_color) ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_terrain_name](class_tileset.md#class_TileSet_method_get_terrain_name) ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int) ) const |
| [TerrainMode](class_tileset.md#enum_TileSet_TerrainMode) | [get_terrain_set_mode](class_tileset.md#class_TileSet_method_get_terrain_set_mode) ( terrain_set: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_terrain_sets_count](class_tileset.md#class_TileSet_method_get_terrain_sets_count) ( ) const |
| [int](class_int.md#class_int) | [get_terrains_count](class_tileset.md#class_TileSet_method_get_terrains_count) ( terrain_set: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has_alternative_level_tile_proxy](class_tileset.md#class_TileSet_method_has_alternative_level_tile_proxy) ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [has_coords_level_tile_proxy](class_tileset.md#class_TileSet_method_has_coords_level_tile_proxy) ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [bool](class_bool.md#class_bool) | [has_custom_data_layer_by_name](class_tileset.md#class_TileSet_method_has_custom_data_layer_by_name) ( layer_name: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [has_source](class_tileset.md#class_TileSet_method_has_source) ( source_id: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has_source_level_tile_proxy](class_tileset.md#class_TileSet_method_has_source_level_tile_proxy) ( source_from: [int](class_int.md#class_int) ) |
| [Array](class_array.md#class_Array) | [map_tile_proxy](class_tileset.md#class_TileSet_method_map_tile_proxy) ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int) ) const |
| void | [move_custom_data_layer](class_tileset.md#class_TileSet_method_move_custom_data_layer) ( layer_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) |
| void | [move_navigation_layer](class_tileset.md#class_TileSet_method_move_navigation_layer) ( layer_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) |
| void | [move_occlusion_layer](class_tileset.md#class_TileSet_method_move_occlusion_layer) ( layer_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) |
| void | [move_physics_layer](class_tileset.md#class_TileSet_method_move_physics_layer) ( layer_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) |
| void | [move_terrain](class_tileset.md#class_TileSet_method_move_terrain) ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) |
| void | [move_terrain_set](class_tileset.md#class_TileSet_method_move_terrain_set) ( terrain_set: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) |
| void | [remove_alternative_level_tile_proxy](class_tileset.md#class_TileSet_method_remove_alternative_level_tile_proxy) ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int) ) |
| void | [remove_coords_level_tile_proxy](class_tileset.md#class_TileSet_method_remove_coords_level_tile_proxy) ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [remove_custom_data_layer](class_tileset.md#class_TileSet_method_remove_custom_data_layer) ( layer_index: [int](class_int.md#class_int) ) |
| void | [remove_navigation_layer](class_tileset.md#class_TileSet_method_remove_navigation_layer) ( layer_index: [int](class_int.md#class_int) ) |
| void | [remove_occlusion_layer](class_tileset.md#class_TileSet_method_remove_occlusion_layer) ( layer_index: [int](class_int.md#class_int) ) |
| void | [remove_pattern](class_tileset.md#class_TileSet_method_remove_pattern) ( index: [int](class_int.md#class_int) ) |
| void | [remove_physics_layer](class_tileset.md#class_TileSet_method_remove_physics_layer) ( layer_index: [int](class_int.md#class_int) ) |
| void | [remove_source](class_tileset.md#class_TileSet_method_remove_source) ( source_id: [int](class_int.md#class_int) ) |
| void | [remove_source_level_tile_proxy](class_tileset.md#class_TileSet_method_remove_source_level_tile_proxy) ( source_from: [int](class_int.md#class_int) ) |
| void | [remove_terrain](class_tileset.md#class_TileSet_method_remove_terrain) ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int) ) |
| void | [remove_terrain_set](class_tileset.md#class_TileSet_method_remove_terrain_set) ( terrain_set: [int](class_int.md#class_int) ) |
| void | [set_alternative_level_tile_proxy](class_tileset.md#class_TileSet_method_set_alternative_level_tile_proxy) ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int), source_to: [int](class_int.md#class_int), coords_to: [Vector2i](class_vector2i.md#class_Vector2i), alternative_to: [int](class_int.md#class_int) ) |
| void | [set_coords_level_tile_proxy](class_tileset.md#class_TileSet_method_set_coords_level_tile_proxy) ( p_source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), source_to: [int](class_int.md#class_int), coords_to: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [set_custom_data_layer_name](class_tileset.md#class_TileSet_method_set_custom_data_layer_name) ( layer_index: [int](class_int.md#class_int), layer_name: [String](class_string.md#class_String) ) |
| void | [set_custom_data_layer_type](class_tileset.md#class_TileSet_method_set_custom_data_layer_type) ( layer_index: [int](class_int.md#class_int), layer_type: Variant.Type ) |
| void | [set_navigation_layer_layer_value](class_tileset.md#class_TileSet_method_set_navigation_layer_layer_value) ( layer_index: [int](class_int.md#class_int), layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |
| void | [set_navigation_layer_layers](class_tileset.md#class_TileSet_method_set_navigation_layer_layers) ( layer_index: [int](class_int.md#class_int), layers: [int](class_int.md#class_int) ) |
| void | [set_occlusion_layer_light_mask](class_tileset.md#class_TileSet_method_set_occlusion_layer_light_mask) ( layer_index: [int](class_int.md#class_int), light_mask: [int](class_int.md#class_int) ) |
| void | [set_occlusion_layer_sdf_collision](class_tileset.md#class_TileSet_method_set_occlusion_layer_sdf_collision) ( layer_index: [int](class_int.md#class_int), sdf_collision: [bool](class_bool.md#class_bool) ) |
| void | [set_physics_layer_collision_layer](class_tileset.md#class_TileSet_method_set_physics_layer_collision_layer) ( layer_index: [int](class_int.md#class_int), layer: [int](class_int.md#class_int) ) |
| void | [set_physics_layer_collision_mask](class_tileset.md#class_TileSet_method_set_physics_layer_collision_mask) ( layer_index: [int](class_int.md#class_int), mask: [int](class_int.md#class_int) ) |
| void | [set_physics_layer_collision_priority](class_tileset.md#class_TileSet_method_set_physics_layer_collision_priority) ( layer_index: [int](class_int.md#class_int), priority: [float](class_float.md#class_float) ) |
| void | [set_physics_layer_physics_material](class_tileset.md#class_TileSet_method_set_physics_layer_physics_material) ( layer_index: [int](class_int.md#class_int), physics_material: [PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) ) |
| void | [set_source_id](class_tileset.md#class_TileSet_method_set_source_id) ( source_id: [int](class_int.md#class_int), new_source_id: [int](class_int.md#class_int) ) |
| void | [set_source_level_tile_proxy](class_tileset.md#class_TileSet_method_set_source_level_tile_proxy) ( source_from: [int](class_int.md#class_int), source_to: [int](class_int.md#class_int) ) |
| void | [set_terrain_color](class_tileset.md#class_TileSet_method_set_terrain_color) ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_terrain_name](class_tileset.md#class_TileSet_method_set_terrain_name) ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [set_terrain_set_mode](class_tileset.md#class_TileSet_method_set_terrain_set_mode) ( terrain_set: [int](class_int.md#class_int), mode: [TerrainMode](class_tileset.md#enum_TileSet_TerrainMode) ) |

---

### Enumerations

<span id="enum_TileSet_TileShape"></span>

enum **TileShape**: [🔗](class_tileset.md#enum_TileSet_TileShape)

<span id="class_TileSet_constant_TILE_SHAPE_SQUARE"></span>

[TileShape](class_tileset.md#enum_TileSet_TileShape) **TILE_SHAPE_SQUARE** = `0`

Rectangular tile shape.

<span id="class_TileSet_constant_TILE_SHAPE_ISOMETRIC"></span>

[TileShape](class_tileset.md#enum_TileSet_TileShape) **TILE_SHAPE_ISOMETRIC** = `1`

Diamond tile shape (for isometric look).

 **Note:** Isometric **TileSet** works best if all sibling [TileMapLayer](class_tilemaplayer.md#class_TileMapLayer) s and their parent inheriting from [Node2D](class_node2d.md#class_Node2D) have Y-sort enabled.

<span id="class_TileSet_constant_TILE_SHAPE_HALF_OFFSET_SQUARE"></span>

[TileShape](class_tileset.md#enum_TileSet_TileShape) **TILE_SHAPE_HALF_OFFSET_SQUARE** = `2`

Rectangular tile shape with one row/column out of two offset by half a tile.

<span id="class_TileSet_constant_TILE_SHAPE_HEXAGON"></span>

[TileShape](class_tileset.md#enum_TileSet_TileShape) **TILE_SHAPE_HEXAGON** = `3`

Hexagonal tile shape.

---

<span id="enum_TileSet_TileLayout"></span>

enum **TileLayout**: [🔗](class_tileset.md#enum_TileSet_TileLayout)

<span id="class_TileSet_constant_TILE_LAYOUT_STACKED"></span>

[TileLayout](class_tileset.md#enum_TileSet_TileLayout) **TILE_LAYOUT_STACKED** = `0`

Tile coordinates layout where both axis stay consistent with their respective local horizontal and vertical axis.

<span id="class_TileSet_constant_TILE_LAYOUT_STACKED_OFFSET"></span>

[TileLayout](class_tileset.md#enum_TileSet_TileLayout) **TILE_LAYOUT_STACKED_OFFSET** = `1`

Same as [TILE_LAYOUT_STACKED](class_tileset.md#class_TileSet_constant_TILE_LAYOUT_STACKED), but the first half-offset is negative instead of positive.

<span id="class_TileSet_constant_TILE_LAYOUT_STAIRS_RIGHT"></span>

[TileLayout](class_tileset.md#enum_TileSet_TileLayout) **TILE_LAYOUT_STAIRS_RIGHT** = `2`

Tile coordinates layout where the horizontal axis stay horizontal, and the vertical one goes down-right.

<span id="class_TileSet_constant_TILE_LAYOUT_STAIRS_DOWN"></span>

[TileLayout](class_tileset.md#enum_TileSet_TileLayout) **TILE_LAYOUT_STAIRS_DOWN** = `3`

Tile coordinates layout where the vertical axis stay vertical, and the horizontal one goes down-right.

<span id="class_TileSet_constant_TILE_LAYOUT_DIAMOND_RIGHT"></span>

[TileLayout](class_tileset.md#enum_TileSet_TileLayout) **TILE_LAYOUT_DIAMOND_RIGHT** = `4`

Tile coordinates layout where the horizontal axis goes up-right, and the vertical one goes down-right.

<span id="class_TileSet_constant_TILE_LAYOUT_DIAMOND_DOWN"></span>

[TileLayout](class_tileset.md#enum_TileSet_TileLayout) **TILE_LAYOUT_DIAMOND_DOWN** = `5`

Tile coordinates layout where the horizontal axis goes down-right, and the vertical one goes down-left.

---

<span id="enum_TileSet_TileOffsetAxis"></span>

enum **TileOffsetAxis**: [🔗](class_tileset.md#enum_TileSet_TileOffsetAxis)

<span id="class_TileSet_constant_TILE_OFFSET_AXIS_HORIZONTAL"></span>

[TileOffsetAxis](class_tileset.md#enum_TileSet_TileOffsetAxis) **TILE_OFFSET_AXIS_HORIZONTAL** = `0`

Horizontal half-offset.

<span id="class_TileSet_constant_TILE_OFFSET_AXIS_VERTICAL"></span>

[TileOffsetAxis](class_tileset.md#enum_TileSet_TileOffsetAxis) **TILE_OFFSET_AXIS_VERTICAL** = `1`

Vertical half-offset.

---

<span id="enum_TileSet_CellNeighbor"></span>

enum **CellNeighbor**: [🔗](class_tileset.md#enum_TileSet_CellNeighbor)

<span id="class_TileSet_constant_CELL_NEIGHBOR_RIGHT_SIDE"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_RIGHT_SIDE** = `0`

Neighbor on the right side.

<span id="class_TileSet_constant_CELL_NEIGHBOR_RIGHT_CORNER"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_RIGHT_CORNER** = `1`

Neighbor in the right corner.

<span id="class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_RIGHT_SIDE"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_BOTTOM_RIGHT_SIDE** = `2`

Neighbor on the bottom right side.

<span id="class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_RIGHT_CORNER"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_BOTTOM_RIGHT_CORNER** = `3`

Neighbor in the bottom right corner.

<span id="class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_SIDE"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_BOTTOM_SIDE** = `4`

Neighbor on the bottom side.

<span id="class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_CORNER"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_BOTTOM_CORNER** = `5`

Neighbor in the bottom corner.

<span id="class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_LEFT_SIDE"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_BOTTOM_LEFT_SIDE** = `6`

Neighbor on the bottom left side.

<span id="class_TileSet_constant_CELL_NEIGHBOR_BOTTOM_LEFT_CORNER"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_BOTTOM_LEFT_CORNER** = `7`

Neighbor in the bottom left corner.

<span id="class_TileSet_constant_CELL_NEIGHBOR_LEFT_SIDE"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_LEFT_SIDE** = `8`

Neighbor on the left side.

<span id="class_TileSet_constant_CELL_NEIGHBOR_LEFT_CORNER"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_LEFT_CORNER** = `9`

Neighbor in the left corner.

<span id="class_TileSet_constant_CELL_NEIGHBOR_TOP_LEFT_SIDE"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_TOP_LEFT_SIDE** = `10`

Neighbor on the top left side.

<span id="class_TileSet_constant_CELL_NEIGHBOR_TOP_LEFT_CORNER"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_TOP_LEFT_CORNER** = `11`

Neighbor in the top left corner.

<span id="class_TileSet_constant_CELL_NEIGHBOR_TOP_SIDE"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_TOP_SIDE** = `12`

Neighbor on the top side.

<span id="class_TileSet_constant_CELL_NEIGHBOR_TOP_CORNER"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_TOP_CORNER** = `13`

Neighbor in the top corner.

<span id="class_TileSet_constant_CELL_NEIGHBOR_TOP_RIGHT_SIDE"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_TOP_RIGHT_SIDE** = `14`

Neighbor on the top right side.

<span id="class_TileSet_constant_CELL_NEIGHBOR_TOP_RIGHT_CORNER"></span>

[CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) **CELL_NEIGHBOR_TOP_RIGHT_CORNER** = `15`

Neighbor in the top right corner.

---

<span id="enum_TileSet_TerrainMode"></span>

enum **TerrainMode**: [🔗](class_tileset.md#enum_TileSet_TerrainMode)

<span id="class_TileSet_constant_TERRAIN_MODE_MATCH_CORNERS_AND_SIDES"></span>

[TerrainMode](class_tileset.md#enum_TileSet_TerrainMode) **TERRAIN_MODE_MATCH_CORNERS_AND_SIDES** = `0`

Requires both corners and side to match with neighboring tiles' terrains.

<span id="class_TileSet_constant_TERRAIN_MODE_MATCH_CORNERS"></span>

[TerrainMode](class_tileset.md#enum_TileSet_TerrainMode) **TERRAIN_MODE_MATCH_CORNERS** = `1`

Requires corners to match with neighboring tiles' terrains.

<span id="class_TileSet_constant_TERRAIN_MODE_MATCH_SIDES"></span>

[TerrainMode](class_tileset.md#enum_TileSet_TerrainMode) **TERRAIN_MODE_MATCH_SIDES** = `2`

Requires sides to match with neighboring tiles' terrains.

---

### Property Descriptions

<span id="class_TileSet_property_tile_layout"></span>

[TileLayout](class_tileset.md#enum_TileSet_TileLayout) **tile_layout** = `0` [🔗](class_tileset.md#class_TileSet_property_tile_layout)

- void **set_tile_layout** ( value: [TileLayout](class_tileset.md#enum_TileSet_TileLayout) )
- [TileLayout](class_tileset.md#enum_TileSet_TileLayout) **get_tile_layout** ( )

For all half-offset shapes (Isometric, Hexagonal and Half-Offset square), changes the way tiles are indexed in the [TileMapLayer](class_tilemaplayer.md#class_TileMapLayer) grid.

---

<span id="class_TileSet_property_tile_offset_axis"></span>

[TileOffsetAxis](class_tileset.md#enum_TileSet_TileOffsetAxis) **tile_offset_axis** = `0` [🔗](class_tileset.md#class_TileSet_property_tile_offset_axis)

- void **set_tile_offset_axis** ( value: [TileOffsetAxis](class_tileset.md#enum_TileSet_TileOffsetAxis) )
- [TileOffsetAxis](class_tileset.md#enum_TileSet_TileOffsetAxis) **get_tile_offset_axis** ( )

For all half-offset shapes (Isometric, Hexagonal and Half-Offset square), determines the offset axis.

---

<span id="class_TileSet_property_tile_shape"></span>

[TileShape](class_tileset.md#enum_TileSet_TileShape) **tile_shape** = `0` [🔗](class_tileset.md#class_TileSet_property_tile_shape)

- void **set_tile_shape** ( value: [TileShape](class_tileset.md#enum_TileSet_TileShape) )
- [TileShape](class_tileset.md#enum_TileSet_TileShape) **get_tile_shape** ( )

The tile shape.

---

<span id="class_TileSet_property_tile_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **tile_size** = `Vector2i(16, 16)` [🔗](class_tileset.md#class_TileSet_property_tile_size)

- void **set_tile_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_tile_size** ( )

The tile size, in pixels. For all tile shapes, this size corresponds to the encompassing rectangle of the tile shape. This is thus the minimal cell size required in an atlas.

---

<span id="class_TileSet_property_uv_clipping"></span>

[bool](class_bool.md#class_bool) **uv_clipping** = `false` [🔗](class_tileset.md#class_TileSet_property_uv_clipping)

- void **set_uv_clipping** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_uv_clipping** ( )

Enables/Disable uv clipping when rendering the tiles.

---

### Method Descriptions

<span id="class_TileSet_method_add_custom_data_layer"></span>

void **add_custom_data_layer** ( to_position: [int](class_int.md#class_int) = -1 ) [🔗](class_tileset.md#class_TileSet_method_add_custom_data_layer)

Adds a custom data layer to the TileSet at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

Custom data layers allow assigning custom properties to atlas tiles.

---

<span id="class_TileSet_method_add_navigation_layer"></span>

void **add_navigation_layer** ( to_position: [int](class_int.md#class_int) = -1 ) [🔗](class_tileset.md#class_TileSet_method_add_navigation_layer)

Adds a navigation layer to the TileSet at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

Navigation layers allow assigning a navigable area to atlas tiles.

---

<span id="class_TileSet_method_add_occlusion_layer"></span>

void **add_occlusion_layer** ( to_position: [int](class_int.md#class_int) = -1 ) [🔗](class_tileset.md#class_TileSet_method_add_occlusion_layer)

Adds an occlusion layer to the TileSet at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

Occlusion layers allow assigning occlusion polygons to atlas tiles.

---

<span id="class_TileSet_method_add_pattern"></span>

[int](class_int.md#class_int) **add_pattern** ( pattern: [TileMapPattern](class_tilemappattern.md#class_TileMapPattern), index: [int](class_int.md#class_int) = -1 ) [🔗](class_tileset.md#class_TileSet_method_add_pattern)

Adds a [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) to be stored in the TileSet resource. If provided, insert it at the given `index`.

---

<span id="class_TileSet_method_add_physics_layer"></span>

void **add_physics_layer** ( to_position: [int](class_int.md#class_int) = -1 ) [🔗](class_tileset.md#class_TileSet_method_add_physics_layer)

Adds a physics layer to the TileSet at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

Physics layers allow assigning collision polygons to atlas tiles.

---

<span id="class_TileSet_method_add_source"></span>

[int](class_int.md#class_int) **add_source** ( source: [TileSetSource](class_tilesetsource.md#class_TileSetSource), atlas_source_id_override: [int](class_int.md#class_int) = -1 ) [🔗](class_tileset.md#class_TileSet_method_add_source)

Adds a [TileSetSource](class_tilesetsource.md#class_TileSetSource) to the TileSet. If `atlas_source_id_override` is not -1, also set its source ID. Otherwise, a unique identifier is automatically generated.

The function returns the added source ID or -1 if the source could not be added.

 **Warning:** A source cannot belong to two TileSets at the same time. If the added source was attached to another **TileSet**, it will be removed from that one.

---

<span id="class_TileSet_method_add_terrain"></span>

void **add_terrain** ( terrain_set: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) = -1 ) [🔗](class_tileset.md#class_TileSet_method_add_terrain)

Adds a new terrain to the given terrain set `terrain_set` at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

---

<span id="class_TileSet_method_add_terrain_set"></span>

void **add_terrain_set** ( to_position: [int](class_int.md#class_int) = -1 ) [🔗](class_tileset.md#class_TileSet_method_add_terrain_set)

Adds a new terrain set at the given position `to_position` in the array. If `to_position` is -1, adds it at the end of the array.

---

<span id="class_TileSet_method_cleanup_invalid_tile_proxies"></span>

void **cleanup_invalid_tile_proxies** ( ) [🔗](class_tileset.md#class_TileSet_method_cleanup_invalid_tile_proxies)

Clears tile proxies pointing to invalid tiles.

---

<span id="class_TileSet_method_clear_tile_proxies"></span>

void **clear_tile_proxies** ( ) [🔗](class_tileset.md#class_TileSet_method_clear_tile_proxies)

Clears all tile proxies.

---

<span id="class_TileSet_method_get_alternative_level_tile_proxy"></span>

[Array](class_array.md#class_Array) **get_alternative_level_tile_proxy** ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_get_alternative_level_tile_proxy)

Returns the alternative-level proxy for the given identifiers. The returned array contains the three proxie's target identifiers (source ID, atlas coords ID and alternative tile ID).

If the TileSet has no proxy for the given identifiers, returns an empty Array.

---

<span id="class_TileSet_method_get_coords_level_tile_proxy"></span>

[Array](class_array.md#class_Array) **get_coords_level_tile_proxy** ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_tileset.md#class_TileSet_method_get_coords_level_tile_proxy)

Returns the coordinate-level proxy for the given identifiers. The returned array contains the two target identifiers of the proxy (source ID and atlas coordinates ID).

If the TileSet has no proxy for the given identifiers, returns an empty Array.

---

<span id="class_TileSet_method_get_custom_data_layer_by_name"></span>

[int](class_int.md#class_int) **get_custom_data_layer_by_name** ( layer_name: [String](class_string.md#class_String) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_custom_data_layer_by_name)

Returns the index of the custom data layer identified by the given name.

---

<span id="class_TileSet_method_get_custom_data_layer_name"></span>

[String](class_string.md#class_String) **get_custom_data_layer_name** ( layer_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_custom_data_layer_name)

Returns the name of the custom data layer identified by the given index.

---

<span id="class_TileSet_method_get_custom_data_layer_type"></span>

Variant.Type **get_custom_data_layer_type** ( layer_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_custom_data_layer_type)

Returns the type of the custom data layer identified by the given index.

---

<span id="class_TileSet_method_get_custom_data_layers_count"></span>

[int](class_int.md#class_int) **get_custom_data_layers_count** ( ) *const* [🔗](class_tileset.md#class_TileSet_method_get_custom_data_layers_count)

Returns the custom data layers count.

---

<span id="class_TileSet_method_get_navigation_layer_layer_value"></span>

[bool](class_bool.md#class_bool) **get_navigation_layer_layer_value** ( layer_index: [int](class_int.md#class_int), layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_navigation_layer_layer_value)

Returns whether or not the specified navigation layer of the TileSet navigation data layer identified by the given `layer_index` is enabled, given a navigation_layers `layer_number` between 1 and 32.

---

<span id="class_TileSet_method_get_navigation_layer_layers"></span>

[int](class_int.md#class_int) **get_navigation_layer_layers** ( layer_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_navigation_layer_layers)

Returns the navigation layers (as in the Navigation server) of the given TileSet navigation layer.

---

<span id="class_TileSet_method_get_navigation_layers_count"></span>

[int](class_int.md#class_int) **get_navigation_layers_count** ( ) *const* [🔗](class_tileset.md#class_TileSet_method_get_navigation_layers_count)

Returns the navigation layers count.

---

<span id="class_TileSet_method_get_next_source_id"></span>

[int](class_int.md#class_int) **get_next_source_id** ( ) *const* [🔗](class_tileset.md#class_TileSet_method_get_next_source_id)

Returns a new unused source ID. This generated ID is the same that a call to [add_source()](class_tileset.md#class_TileSet_method_add_source) would return.

---

<span id="class_TileSet_method_get_occlusion_layer_light_mask"></span>

[int](class_int.md#class_int) **get_occlusion_layer_light_mask** ( layer_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_occlusion_layer_light_mask)

Returns the light mask of the occlusion layer.

---

<span id="class_TileSet_method_get_occlusion_layer_sdf_collision"></span>

[bool](class_bool.md#class_bool) **get_occlusion_layer_sdf_collision** ( layer_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_occlusion_layer_sdf_collision)

Returns if the occluders from this layer use `sdf_collision`.

---

<span id="class_TileSet_method_get_occlusion_layers_count"></span>

[int](class_int.md#class_int) **get_occlusion_layers_count** ( ) *const* [🔗](class_tileset.md#class_TileSet_method_get_occlusion_layers_count)

Returns the occlusion layers count.

---

<span id="class_TileSet_method_get_pattern"></span>

[TileMapPattern](class_tilemappattern.md#class_TileMapPattern) **get_pattern** ( index: [int](class_int.md#class_int) = -1 ) [🔗](class_tileset.md#class_TileSet_method_get_pattern)

Returns the [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) at the given `index`.

---

<span id="class_TileSet_method_get_patterns_count"></span>

[int](class_int.md#class_int) **get_patterns_count** ( ) [🔗](class_tileset.md#class_TileSet_method_get_patterns_count)

Returns the number of [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) this tile set handles.

---

<span id="class_TileSet_method_get_physics_layer_collision_layer"></span>

[int](class_int.md#class_int) **get_physics_layer_collision_layer** ( layer_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_physics_layer_collision_layer)

Returns the collision layer (as in the physics server) bodies on the given TileSet's physics layer are in.

---

<span id="class_TileSet_method_get_physics_layer_collision_mask"></span>

[int](class_int.md#class_int) **get_physics_layer_collision_mask** ( layer_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_physics_layer_collision_mask)

Returns the collision mask of bodies on the given TileSet's physics layer.

---

<span id="class_TileSet_method_get_physics_layer_collision_priority"></span>

[float](class_float.md#class_float) **get_physics_layer_collision_priority** ( layer_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_physics_layer_collision_priority)

Returns the collision priority of bodies on the given TileSet's physics layer.

---

<span id="class_TileSet_method_get_physics_layer_physics_material"></span>

[PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) **get_physics_layer_physics_material** ( layer_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_physics_layer_physics_material)

Returns the physics material of bodies on the given TileSet's physics layer.

---

<span id="class_TileSet_method_get_physics_layers_count"></span>

[int](class_int.md#class_int) **get_physics_layers_count** ( ) *const* [🔗](class_tileset.md#class_TileSet_method_get_physics_layers_count)

Returns the physics layers count.

---

<span id="class_TileSet_method_get_source"></span>

[TileSetSource](class_tilesetsource.md#class_TileSetSource) **get_source** ( source_id: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_source)

Returns the [TileSetSource](class_tilesetsource.md#class_TileSetSource) with ID `source_id`.

---

<span id="class_TileSet_method_get_source_count"></span>

[int](class_int.md#class_int) **get_source_count** ( ) *const* [🔗](class_tileset.md#class_TileSet_method_get_source_count)

Returns the number of [TileSetSource](class_tilesetsource.md#class_TileSetSource) in this TileSet.

---

<span id="class_TileSet_method_get_source_id"></span>

[int](class_int.md#class_int) **get_source_id** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_source_id)

Returns the source ID for source with index `index`.

---

<span id="class_TileSet_method_get_source_level_tile_proxy"></span>

[int](class_int.md#class_int) **get_source_level_tile_proxy** ( source_from: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_get_source_level_tile_proxy)

Returns the source-level proxy for the given source identifier.

If the TileSet has no proxy for the given identifier, returns -1.

---

<span id="class_TileSet_method_get_terrain_color"></span>

[Color](class_color.md#class_Color) **get_terrain_color** ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_terrain_color)

Returns a terrain's color.

---

<span id="class_TileSet_method_get_terrain_name"></span>

[String](class_string.md#class_String) **get_terrain_name** ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_terrain_name)

Returns a terrain's name.

---

<span id="class_TileSet_method_get_terrain_set_mode"></span>

[TerrainMode](class_tileset.md#enum_TileSet_TerrainMode) **get_terrain_set_mode** ( terrain_set: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_terrain_set_mode)

Returns a terrain set mode.

---

<span id="class_TileSet_method_get_terrain_sets_count"></span>

[int](class_int.md#class_int) **get_terrain_sets_count** ( ) *const* [🔗](class_tileset.md#class_TileSet_method_get_terrain_sets_count)

Returns the terrain sets count.

---

<span id="class_TileSet_method_get_terrains_count"></span>

[int](class_int.md#class_int) **get_terrains_count** ( terrain_set: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_get_terrains_count)

Returns the number of terrains in the given terrain set.

---

<span id="class_TileSet_method_has_alternative_level_tile_proxy"></span>

[bool](class_bool.md#class_bool) **has_alternative_level_tile_proxy** ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_has_alternative_level_tile_proxy)

Returns if there is an alternative-level proxy for the given identifiers.

---

<span id="class_TileSet_method_has_coords_level_tile_proxy"></span>

[bool](class_bool.md#class_bool) **has_coords_level_tile_proxy** ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_tileset.md#class_TileSet_method_has_coords_level_tile_proxy)

Returns if there is a coodinates-level proxy for the given identifiers.

---

<span id="class_TileSet_method_has_custom_data_layer_by_name"></span>

[bool](class_bool.md#class_bool) **has_custom_data_layer_by_name** ( layer_name: [String](class_string.md#class_String) ) *const* [🔗](class_tileset.md#class_TileSet_method_has_custom_data_layer_by_name)

Returns if there is a custom data layer named `layer_name`.

---

<span id="class_TileSet_method_has_source"></span>

[bool](class_bool.md#class_bool) **has_source** ( source_id: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_has_source)

Returns if this TileSet has a source for the given source ID.

---

<span id="class_TileSet_method_has_source_level_tile_proxy"></span>

[bool](class_bool.md#class_bool) **has_source_level_tile_proxy** ( source_from: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_has_source_level_tile_proxy)

Returns if there is a source-level proxy for the given source ID.

---

<span id="class_TileSet_method_map_tile_proxy"></span>

[Array](class_array.md#class_Array) **map_tile_proxy** ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int) ) *const* [🔗](class_tileset.md#class_TileSet_method_map_tile_proxy)

According to the configured proxies, maps the provided identifiers to a new set of identifiers. The source ID, atlas coordinates ID and alternative tile ID are returned as a 3 elements Array.

This function first look for matching alternative-level proxies, then coordinates-level proxies, then source-level proxies.

If no proxy corresponding to provided identifiers are found, returns the same values the ones used as arguments.

---

<span id="class_TileSet_method_move_custom_data_layer"></span>

void **move_custom_data_layer** ( layer_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_move_custom_data_layer)

Moves the custom data layer at index `layer_index` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_move_navigation_layer"></span>

void **move_navigation_layer** ( layer_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_move_navigation_layer)

Moves the navigation layer at index `layer_index` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_move_occlusion_layer"></span>

void **move_occlusion_layer** ( layer_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_move_occlusion_layer)

Moves the occlusion layer at index `layer_index` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_move_physics_layer"></span>

void **move_physics_layer** ( layer_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_move_physics_layer)

Moves the physics layer at index `layer_index` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_move_terrain"></span>

void **move_terrain** ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_move_terrain)

Moves the terrain at index `terrain_index` for terrain set `terrain_set` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_move_terrain_set"></span>

void **move_terrain_set** ( terrain_set: [int](class_int.md#class_int), to_position: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_move_terrain_set)

Moves the terrain set at index `terrain_set` to the given position `to_position` in the array. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_remove_alternative_level_tile_proxy"></span>

void **remove_alternative_level_tile_proxy** ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_alternative_level_tile_proxy)

Removes an alternative-level proxy for the given identifiers.

---

<span id="class_TileSet_method_remove_coords_level_tile_proxy"></span>

void **remove_coords_level_tile_proxy** ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_tileset.md#class_TileSet_method_remove_coords_level_tile_proxy)

Removes a coordinates-level proxy for the given identifiers.

---

<span id="class_TileSet_method_remove_custom_data_layer"></span>

void **remove_custom_data_layer** ( layer_index: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_custom_data_layer)

Removes the custom data layer at index `layer_index`. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_remove_navigation_layer"></span>

void **remove_navigation_layer** ( layer_index: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_navigation_layer)

Removes the navigation layer at index `layer_index`. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_remove_occlusion_layer"></span>

void **remove_occlusion_layer** ( layer_index: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_occlusion_layer)

Removes the occlusion layer at index `layer_index`. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_remove_pattern"></span>

void **remove_pattern** ( index: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_pattern)

Remove the [TileMapPattern](class_tilemappattern.md#class_TileMapPattern) at the given index.

---

<span id="class_TileSet_method_remove_physics_layer"></span>

void **remove_physics_layer** ( layer_index: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_physics_layer)

Removes the physics layer at index `layer_index`. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_remove_source"></span>

void **remove_source** ( source_id: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_source)

Removes the source with the given source ID.

---

<span id="class_TileSet_method_remove_source_level_tile_proxy"></span>

void **remove_source_level_tile_proxy** ( source_from: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_source_level_tile_proxy)

Removes a source-level tile proxy.

---

<span id="class_TileSet_method_remove_terrain"></span>

void **remove_terrain** ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_terrain)

Removes the terrain at index `terrain_index` in the given terrain set `terrain_set`. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_remove_terrain_set"></span>

void **remove_terrain_set** ( terrain_set: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_remove_terrain_set)

Removes the terrain set at index `terrain_set`. Also updates the atlas tiles accordingly.

---

<span id="class_TileSet_method_set_alternative_level_tile_proxy"></span>

void **set_alternative_level_tile_proxy** ( source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), alternative_from: [int](class_int.md#class_int), source_to: [int](class_int.md#class_int), coords_to: [Vector2i](class_vector2i.md#class_Vector2i), alternative_to: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_set_alternative_level_tile_proxy)

Create an alternative-level proxy for the given identifiers. A proxy will map set of tile identifiers to another set of identifiers.

Proxied tiles can be automatically replaced in TileMapLayer nodes using the editor.

---

<span id="class_TileSet_method_set_coords_level_tile_proxy"></span>

void **set_coords_level_tile_proxy** ( p_source_from: [int](class_int.md#class_int), coords_from: [Vector2i](class_vector2i.md#class_Vector2i), source_to: [int](class_int.md#class_int), coords_to: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_tileset.md#class_TileSet_method_set_coords_level_tile_proxy)

Creates a coordinates-level proxy for the given identifiers. A proxy will map set of tile identifiers to another set of identifiers. The alternative tile ID is kept the same when using coordinates-level proxies.

Proxied tiles can be automatically replaced in TileMapLayer nodes using the editor.

---

<span id="class_TileSet_method_set_custom_data_layer_name"></span>

void **set_custom_data_layer_name** ( layer_index: [int](class_int.md#class_int), layer_name: [String](class_string.md#class_String) ) [🔗](class_tileset.md#class_TileSet_method_set_custom_data_layer_name)

Sets the name of the custom data layer identified by the given index. Names are identifiers of the layer therefore if the name is already taken it will fail and raise an error.

---

<span id="class_TileSet_method_set_custom_data_layer_type"></span>

void **set_custom_data_layer_type** ( layer_index: [int](class_int.md#class_int), layer_type: Variant.Type ) [🔗](class_tileset.md#class_TileSet_method_set_custom_data_layer_type)

Sets the type of the custom data layer identified by the given index.

---

<span id="class_TileSet_method_set_navigation_layer_layer_value"></span>

void **set_navigation_layer_layer_value** ( layer_index: [int](class_int.md#class_int), layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_tileset.md#class_TileSet_method_set_navigation_layer_layer_value)

Based on `value`, enables or disables the specified navigation layer of the TileSet navigation data layer identified by the given `layer_index`, given a navigation_layers `layer_number` between 1 and 32.

---

<span id="class_TileSet_method_set_navigation_layer_layers"></span>

void **set_navigation_layer_layers** ( layer_index: [int](class_int.md#class_int), layers: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_set_navigation_layer_layers)

Sets the navigation layers (as in the navigation server) for navigation regions in the given TileSet navigation layer.

---

<span id="class_TileSet_method_set_occlusion_layer_light_mask"></span>

void **set_occlusion_layer_light_mask** ( layer_index: [int](class_int.md#class_int), light_mask: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_set_occlusion_layer_light_mask)

Sets the occlusion layer (as in the rendering server) for occluders in the given TileSet occlusion layer.

---

<span id="class_TileSet_method_set_occlusion_layer_sdf_collision"></span>

void **set_occlusion_layer_sdf_collision** ( layer_index: [int](class_int.md#class_int), sdf_collision: [bool](class_bool.md#class_bool) ) [🔗](class_tileset.md#class_TileSet_method_set_occlusion_layer_sdf_collision)

Enables or disables SDF collision for occluders in the given TileSet occlusion layer.

---

<span id="class_TileSet_method_set_physics_layer_collision_layer"></span>

void **set_physics_layer_collision_layer** ( layer_index: [int](class_int.md#class_int), layer: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_set_physics_layer_collision_layer)

Sets the collision layer (as in the physics server) for bodies in the given TileSet physics layer.

---

<span id="class_TileSet_method_set_physics_layer_collision_mask"></span>

void **set_physics_layer_collision_mask** ( layer_index: [int](class_int.md#class_int), mask: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_set_physics_layer_collision_mask)

Sets the collision mask for bodies in the given TileSet physics layer.

---

<span id="class_TileSet_method_set_physics_layer_collision_priority"></span>

void **set_physics_layer_collision_priority** ( layer_index: [int](class_int.md#class_int), priority: [float](class_float.md#class_float) ) [🔗](class_tileset.md#class_TileSet_method_set_physics_layer_collision_priority)

Sets the collision priority for bodies in the given TileSet physics layer.

---

<span id="class_TileSet_method_set_physics_layer_physics_material"></span>

void **set_physics_layer_physics_material** ( layer_index: [int](class_int.md#class_int), physics_material: [PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) ) [🔗](class_tileset.md#class_TileSet_method_set_physics_layer_physics_material)

Sets the physics material for bodies in the given TileSet physics layer.

---

<span id="class_TileSet_method_set_source_id"></span>

void **set_source_id** ( source_id: [int](class_int.md#class_int), new_source_id: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_set_source_id)

Changes a source's ID.

---

<span id="class_TileSet_method_set_source_level_tile_proxy"></span>

void **set_source_level_tile_proxy** ( source_from: [int](class_int.md#class_int), source_to: [int](class_int.md#class_int) ) [🔗](class_tileset.md#class_TileSet_method_set_source_level_tile_proxy)

Creates a source-level proxy for the given source ID. A proxy will map set of tile identifiers to another set of identifiers. Both the atlas coordinates ID and the alternative tile ID are kept the same when using source-level proxies.

Proxied tiles can be automatically replaced in TileMapLayer nodes using the editor.

---

<span id="class_TileSet_method_set_terrain_color"></span>

void **set_terrain_color** ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_tileset.md#class_TileSet_method_set_terrain_color)

Sets a terrain's color. This color is used for identifying the different terrains in the TileSet editor.

---

<span id="class_TileSet_method_set_terrain_name"></span>

void **set_terrain_name** ( terrain_set: [int](class_int.md#class_int), terrain_index: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_tileset.md#class_TileSet_method_set_terrain_name)

Sets a terrain's name.

---

<span id="class_TileSet_method_set_terrain_set_mode"></span>

void **set_terrain_set_mode** ( terrain_set: [int](class_int.md#class_int), mode: [TerrainMode](class_tileset.md#enum_TileSet_TerrainMode) ) [🔗](class_tileset.md#class_TileSet_method_set_terrain_set_mode)

Sets a terrain mode. Each mode determines which bits of a tile shape is used to match the neighboring tiles' terrains.
