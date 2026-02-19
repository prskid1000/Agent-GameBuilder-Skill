<span id="class_TileMapPattern"></span>

## TileMapPattern

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Holds a pattern to be copied from or pasted into [TileMap](class_tilemap.md#class_TileMap) s.

### Description

This resource holds a set of cells to help bulk manipulations of [TileMap](class_tilemap.md#class_TileMap).

A pattern always starts at the `(0, 0)` coordinates and cannot have cells with negative coordinates.

### Methods


| [int](class_int.md#class_int) | [get_cell_alternative_tile](class_tilemappattern.md#class_TileMapPattern_method_get_cell_alternative_tile) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| --- | --- |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_cell_atlas_coords](class_tilemappattern.md#class_TileMapPattern_method_get_cell_atlas_coords) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [int](class_int.md#class_int) | [get_cell_source_id](class_tilemappattern.md#class_TileMapPattern_method_get_cell_source_id) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_size](class_tilemappattern.md#class_TileMapPattern_method_get_size) ( ) const |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [get_used_cells](class_tilemappattern.md#class_TileMapPattern_method_get_used_cells) ( ) const |
| [bool](class_bool.md#class_bool) | [has_cell](class_tilemappattern.md#class_TileMapPattern_method_has_cell) ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [bool](class_bool.md#class_bool) | [is_empty](class_tilemappattern.md#class_TileMapPattern_method_is_empty) ( ) const |
| void | [remove_cell](class_tilemappattern.md#class_TileMapPattern_method_remove_cell) ( coords: [Vector2i](class_vector2i.md#class_Vector2i), update_size: [bool](class_bool.md#class_bool) ) |
| void | [set_cell](class_tilemappattern.md#class_TileMapPattern_method_set_cell) ( coords: [Vector2i](class_vector2i.md#class_Vector2i), source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = -1 ) |
| void | [set_size](class_tilemappattern.md#class_TileMapPattern_method_set_size) ( size: [Vector2i](class_vector2i.md#class_Vector2i) ) |

---

### Method Descriptions

<span id="class_TileMapPattern_method_get_cell_alternative_tile"></span>

[int](class_int.md#class_int) **get_cell_alternative_tile** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemappattern.md#class_TileMapPattern_method_get_cell_alternative_tile)

Returns the tile alternative ID of the cell at `coords`.

---

<span id="class_TileMapPattern_method_get_cell_atlas_coords"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_cell_atlas_coords** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemappattern.md#class_TileMapPattern_method_get_cell_atlas_coords)

Returns the tile atlas coordinates ID of the cell at `coords`.

---

<span id="class_TileMapPattern_method_get_cell_source_id"></span>

[int](class_int.md#class_int) **get_cell_source_id** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemappattern.md#class_TileMapPattern_method_get_cell_source_id)

Returns the tile source ID of the cell at `coords`.

---

<span id="class_TileMapPattern_method_get_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_size** ( ) *const* [🔗](class_tilemappattern.md#class_TileMapPattern_method_get_size)

Returns the size, in cells, of the pattern.

---

<span id="class_TileMapPattern_method_get_used_cells"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **get_used_cells** ( ) *const* [🔗](class_tilemappattern.md#class_TileMapPattern_method_get_used_cells)

Returns the list of used cell coordinates in the pattern.

---

<span id="class_TileMapPattern_method_has_cell"></span>

[bool](class_bool.md#class_bool) **has_cell** ( coords: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_tilemappattern.md#class_TileMapPattern_method_has_cell)

Returns whether the pattern has a tile at the given coordinates.

---

<span id="class_TileMapPattern_method_is_empty"></span>

[bool](class_bool.md#class_bool) **is_empty** ( ) *const* [🔗](class_tilemappattern.md#class_TileMapPattern_method_is_empty)

Returns whether the pattern is empty or not.

---

<span id="class_TileMapPattern_method_remove_cell"></span>

void **remove_cell** ( coords: [Vector2i](class_vector2i.md#class_Vector2i), update_size: [bool](class_bool.md#class_bool) ) [🔗](class_tilemappattern.md#class_TileMapPattern_method_remove_cell)

Remove the cell at the given coordinates.

---

<span id="class_TileMapPattern_method_set_cell"></span>

void **set_cell** ( coords: [Vector2i](class_vector2i.md#class_Vector2i), source_id: [int](class_int.md#class_int) = -1, atlas_coords: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(-1, -1), alternative_tile: [int](class_int.md#class_int) = -1 ) [🔗](class_tilemappattern.md#class_TileMapPattern_method_set_cell)

Sets the tile identifiers for the cell at coordinates `coords`. See [TileMap.set_cell()](class_tilemap.md#class_TileMap_method_set_cell).

---

<span id="class_TileMapPattern_method_set_size"></span>

void **set_size** ( size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_tilemappattern.md#class_TileMapPattern_method_set_size)

Sets the size of the pattern.
