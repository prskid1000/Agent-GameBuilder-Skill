<span id="class_TileData"></span>

## TileData

**Inherits:** [Object](class_object.md#class_Object)

Settings for a single tile in a [TileSet](class_tileset.md#class_TileSet).

### Description

**TileData** object represents a single tile in a [TileSet](class_tileset.md#class_TileSet). It is usually edited using the tileset editor, but it can be modified at runtime using [TileMapLayer._tile_data_runtime_update()](class_tilemaplayer.md#class_TileMapLayer_private_method__tile_data_runtime_update).

### Properties


| [bool](class_bool.md#class_bool) | [flip_h](class_tiledata.md#class_TileData_property_flip_h) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [flip_v](class_tiledata.md#class_TileData_property_flip_v) | `false` |
| [Material](class_material.md#class_Material) | [material](class_tiledata.md#class_TileData_property_material) |
| [Color](class_color.md#class_Color) | [modulate](class_tiledata.md#class_TileData_property_modulate) | `Color(1, 1, 1, 1)` |
| [float](class_float.md#class_float) | [probability](class_tiledata.md#class_TileData_property_probability) | `1.0` |
| [int](class_int.md#class_int) | [terrain](class_tiledata.md#class_TileData_property_terrain) | `-1` |
| [int](class_int.md#class_int) | [terrain_set](class_tiledata.md#class_TileData_property_terrain_set) | `-1` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [texture_origin](class_tiledata.md#class_TileData_property_texture_origin) | `Vector2i(0, 0)` |
| [bool](class_bool.md#class_bool) | [transpose](class_tiledata.md#class_TileData_property_transpose) | `false` |
| [int](class_int.md#class_int) | [y_sort_origin](class_tiledata.md#class_TileData_property_y_sort_origin) | `0` |
| [int](class_int.md#class_int) | [z_index](class_tiledata.md#class_TileData_property_z_index) | `0` |

### Methods


| void | [add_collision_polygon](class_tiledata.md#class_TileData_method_add_collision_polygon) ( layer_id: [int](class_int.md#class_int) ) |
| --- | --- |
| void | [add_occluder_polygon](class_tiledata.md#class_TileData_method_add_occluder_polygon) ( layer_id: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | [get_collision_polygon_one_way_margin](class_tiledata.md#class_TileData_method_get_collision_polygon_one_way_margin) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) const |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [get_collision_polygon_points](class_tiledata.md#class_TileData_method_get_collision_polygon_points) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_collision_polygons_count](class_tiledata.md#class_TileData_method_get_collision_polygons_count) ( layer_id: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_constant_angular_velocity](class_tiledata.md#class_TileData_method_get_constant_angular_velocity) ( layer_id: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_constant_linear_velocity](class_tiledata.md#class_TileData_method_get_constant_linear_velocity) ( layer_id: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_custom_data](class_tiledata.md#class_TileData_method_get_custom_data) ( layer_name: [String](class_string.md#class_String) ) const |
| [Variant](class_variant.md#class_Variant) | [get_custom_data_by_layer_id](class_tiledata.md#class_TileData_method_get_custom_data_by_layer_id) ( layer_id: [int](class_int.md#class_int) ) const |
| [NavigationPolygon](class_navigationpolygon.md#class_NavigationPolygon) | [get_navigation_polygon](class_tiledata.md#class_TileData_method_get_navigation_polygon) ( layer_id: [int](class_int.md#class_int), flip_h: [bool](class_bool.md#class_bool) = false, flip_v: [bool](class_bool.md#class_bool) = false, transpose: [bool](class_bool.md#class_bool) = false ) const |
| [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) | [get_occluder](class_tiledata.md#class_TileData_method_get_occluder) ( layer_id: [int](class_int.md#class_int), flip_h: [bool](class_bool.md#class_bool) = false, flip_v: [bool](class_bool.md#class_bool) = false, transpose: [bool](class_bool.md#class_bool) = false ) const |
| [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) | [get_occluder_polygon](class_tiledata.md#class_TileData_method_get_occluder_polygon) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), flip_h: [bool](class_bool.md#class_bool) = false, flip_v: [bool](class_bool.md#class_bool) = false, transpose: [bool](class_bool.md#class_bool) = false ) const |
| [int](class_int.md#class_int) | [get_occluder_polygons_count](class_tiledata.md#class_TileData_method_get_occluder_polygons_count) ( layer_id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_terrain_peering_bit](class_tiledata.md#class_TileData_method_get_terrain_peering_bit) ( peering_bit: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) ) const |
| [bool](class_bool.md#class_bool) | [has_custom_data](class_tiledata.md#class_TileData_method_has_custom_data) ( layer_name: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [is_collision_polygon_one_way](class_tiledata.md#class_TileData_method_is_collision_polygon_one_way) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_valid_terrain_peering_bit](class_tiledata.md#class_TileData_method_is_valid_terrain_peering_bit) ( peering_bit: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) ) const |
| void | [remove_collision_polygon](class_tiledata.md#class_TileData_method_remove_collision_polygon) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) |
| void | [remove_occluder_polygon](class_tiledata.md#class_TileData_method_remove_occluder_polygon) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) |
| void | [set_collision_polygon_one_way](class_tiledata.md#class_TileData_method_set_collision_polygon_one_way) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), one_way: [bool](class_bool.md#class_bool) ) |
| void | [set_collision_polygon_one_way_margin](class_tiledata.md#class_TileData_method_set_collision_polygon_one_way_margin) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), one_way_margin: [float](class_float.md#class_float) ) |
| void | [set_collision_polygon_points](class_tiledata.md#class_TileData_method_set_collision_polygon_points) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), polygon: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) |
| void | [set_collision_polygons_count](class_tiledata.md#class_TileData_method_set_collision_polygons_count) ( layer_id: [int](class_int.md#class_int), polygons_count: [int](class_int.md#class_int) ) |
| void | [set_constant_angular_velocity](class_tiledata.md#class_TileData_method_set_constant_angular_velocity) ( layer_id: [int](class_int.md#class_int), velocity: [float](class_float.md#class_float) ) |
| void | [set_constant_linear_velocity](class_tiledata.md#class_TileData_method_set_constant_linear_velocity) ( layer_id: [int](class_int.md#class_int), velocity: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_custom_data](class_tiledata.md#class_TileData_method_set_custom_data) ( layer_name: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) |
| void | [set_custom_data_by_layer_id](class_tiledata.md#class_TileData_method_set_custom_data_by_layer_id) ( layer_id: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant) ) |
| void | [set_navigation_polygon](class_tiledata.md#class_TileData_method_set_navigation_polygon) ( layer_id: [int](class_int.md#class_int), navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class_NavigationPolygon) ) |
| void | [set_occluder](class_tiledata.md#class_TileData_method_set_occluder) ( layer_id: [int](class_int.md#class_int), occluder_polygon: [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) ) |
| void | [set_occluder_polygon](class_tiledata.md#class_TileData_method_set_occluder_polygon) ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), polygon: [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) ) |
| void | [set_occluder_polygons_count](class_tiledata.md#class_TileData_method_set_occluder_polygons_count) ( layer_id: [int](class_int.md#class_int), polygons_count: [int](class_int.md#class_int) ) |
| void | [set_terrain_peering_bit](class_tiledata.md#class_TileData_method_set_terrain_peering_bit) ( peering_bit: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor), terrain: [int](class_int.md#class_int) ) |

---

### Signals

<span id="class_TileData_signal_changed"></span>

**changed** ( ) [🔗](class_tiledata.md#class_TileData_signal_changed)

Emitted when any of the properties are changed.

---

### Property Descriptions

<span id="class_TileData_property_flip_h"></span>

[bool](class_bool.md#class_bool) **flip_h** = `false` [🔗](class_tiledata.md#class_TileData_property_flip_h)

- void **set_flip_h** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flip_h** ( )

If `true`, the tile will have its texture flipped horizontally.

---

<span id="class_TileData_property_flip_v"></span>

[bool](class_bool.md#class_bool) **flip_v** = `false` [🔗](class_tiledata.md#class_TileData_property_flip_v)

- void **set_flip_v** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flip_v** ( )

If `true`, the tile will have its texture flipped vertically.

---

<span id="class_TileData_property_material"></span>

[Material](class_material.md#class_Material) **material** [🔗](class_tiledata.md#class_TileData_property_material)

- void **set_material** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_material** ( )

The [Material](class_material.md#class_Material) to use for this **TileData**. This can be a [CanvasItemMaterial](class_canvasitemmaterial.md#class_CanvasItemMaterial) to use the default shader, or a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) to use a custom shader.

---

<span id="class_TileData_property_modulate"></span>

[Color](class_color.md#class_Color) **modulate** = `Color(1, 1, 1, 1)` [🔗](class_tiledata.md#class_TileData_property_modulate)

- void **set_modulate** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_modulate** ( )

Color modulation of the tile.

---

<span id="class_TileData_property_probability"></span>

[float](class_float.md#class_float) **probability** = `1.0` [🔗](class_tiledata.md#class_TileData_property_probability)

- void **set_probability** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_probability** ( )

Relative probability of this tile being selected when drawing a pattern of random tiles.

---

<span id="class_TileData_property_terrain"></span>

[int](class_int.md#class_int) **terrain** = `-1` [🔗](class_tiledata.md#class_TileData_property_terrain)

- void **set_terrain** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_terrain** ( )

ID of the terrain from the terrain set that the tile uses.

---

<span id="class_TileData_property_terrain_set"></span>

[int](class_int.md#class_int) **terrain_set** = `-1` [🔗](class_tiledata.md#class_TileData_property_terrain_set)

- void **set_terrain_set** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_terrain_set** ( )

ID of the terrain set that the tile uses.

---

<span id="class_TileData_property_texture_origin"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **texture_origin** = `Vector2i(0, 0)` [🔗](class_tiledata.md#class_TileData_property_texture_origin)

- void **set_texture_origin** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_texture_origin** ( )

Offsets the position of where the tile is drawn.

---

<span id="class_TileData_property_transpose"></span>

[bool](class_bool.md#class_bool) **transpose** = `false` [🔗](class_tiledata.md#class_TileData_property_transpose)

- void **set_transpose** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_transpose** ( )

If `true`, the tile will display transposed, i.e. with horizontal and vertical texture UVs swapped.

---

<span id="class_TileData_property_y_sort_origin"></span>

[int](class_int.md#class_int) **y_sort_origin** = `0` [🔗](class_tiledata.md#class_TileData_property_y_sort_origin)

- void **set_y_sort_origin** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_y_sort_origin** ( )

Vertical point of the tile used for determining y-sorted order.

---

<span id="class_TileData_property_z_index"></span>

[int](class_int.md#class_int) **z_index** = `0` [🔗](class_tiledata.md#class_TileData_property_z_index)

- void **set_z_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_z_index** ( )

Ordering index of this tile, relative to [TileMapLayer](class_tilemaplayer.md#class_TileMapLayer).

---

### Method Descriptions

<span id="class_TileData_method_add_collision_polygon"></span>

void **add_collision_polygon** ( layer_id: [int](class_int.md#class_int) ) [🔗](class_tiledata.md#class_TileData_method_add_collision_polygon)

Adds a collision polygon to the tile on the given TileSet physics layer.

---

<span id="class_TileData_method_add_occluder_polygon"></span>

void **add_occluder_polygon** ( layer_id: [int](class_int.md#class_int) ) [🔗](class_tiledata.md#class_TileData_method_add_occluder_polygon)

Adds an occlusion polygon to the tile on the TileSet occlusion layer with index `layer_id`.

---

<span id="class_TileData_method_get_collision_polygon_one_way_margin"></span>

[float](class_float.md#class_float) **get_collision_polygon_one_way_margin** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) *const* [🔗](class_tiledata.md#class_TileData_method_get_collision_polygon_one_way_margin)

Returns the one-way margin (for one-way platforms) of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

<span id="class_TileData_method_get_collision_polygon_points"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_collision_polygon_points** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) *const* [🔗](class_tiledata.md#class_TileData_method_get_collision_polygon_points)

Returns the points of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

<span id="class_TileData_method_get_collision_polygons_count"></span>

[int](class_int.md#class_int) **get_collision_polygons_count** ( layer_id: [int](class_int.md#class_int) ) *const* [🔗](class_tiledata.md#class_TileData_method_get_collision_polygons_count)

Returns how many polygons the tile has for TileSet physics layer with index `layer_id`.

---

<span id="class_TileData_method_get_constant_angular_velocity"></span>

[float](class_float.md#class_float) **get_constant_angular_velocity** ( layer_id: [int](class_int.md#class_int) ) *const* [🔗](class_tiledata.md#class_TileData_method_get_constant_angular_velocity)

Returns the constant angular velocity applied to objects colliding with this tile.

---

<span id="class_TileData_method_get_constant_linear_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **get_constant_linear_velocity** ( layer_id: [int](class_int.md#class_int) ) *const* [🔗](class_tiledata.md#class_TileData_method_get_constant_linear_velocity)

Returns the constant linear velocity applied to objects colliding with this tile.

---

<span id="class_TileData_method_get_custom_data"></span>

[Variant](class_variant.md#class_Variant) **get_custom_data** ( layer_name: [String](class_string.md#class_String) ) *const* [🔗](class_tiledata.md#class_TileData_method_get_custom_data)

Returns the custom data value for custom data layer named `layer_name`. To check if a custom data layer exists, use [has_custom_data()](class_tiledata.md#class_TileData_method_has_custom_data).

---

<span id="class_TileData_method_get_custom_data_by_layer_id"></span>

[Variant](class_variant.md#class_Variant) **get_custom_data_by_layer_id** ( layer_id: [int](class_int.md#class_int) ) *const* [🔗](class_tiledata.md#class_TileData_method_get_custom_data_by_layer_id)

Returns the custom data value for custom data layer with index `layer_id`.

---

<span id="class_TileData_method_get_navigation_polygon"></span>

[NavigationPolygon](class_navigationpolygon.md#class_NavigationPolygon) **get_navigation_polygon** ( layer_id: [int](class_int.md#class_int), flip_h: [bool](class_bool.md#class_bool) = false, flip_v: [bool](class_bool.md#class_bool) = false, transpose: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tiledata.md#class_TileData_method_get_navigation_polygon)

Returns the navigation polygon of the tile for the TileSet navigation layer with index `layer_id`.

 `flip_h`, `flip_v`, and `transpose` allow transforming the returned polygon.

---

<span id="class_TileData_method_get_occluder"></span>

[OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) **get_occluder** ( layer_id: [int](class_int.md#class_int), flip_h: [bool](class_bool.md#class_bool) = false, flip_v: [bool](class_bool.md#class_bool) = false, transpose: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tiledata.md#class_TileData_method_get_occluder)

**Deprecated:** Use [get_occluder_polygon()](class_tiledata.md#class_TileData_method_get_occluder_polygon) instead.

Returns the occluder polygon of the tile for the TileSet occlusion layer with index `layer_id`.

 `flip_h`, `flip_v`, and `transpose` allow transforming the returned polygon.

---

<span id="class_TileData_method_get_occluder_polygon"></span>

[OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) **get_occluder_polygon** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), flip_h: [bool](class_bool.md#class_bool) = false, flip_v: [bool](class_bool.md#class_bool) = false, transpose: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_tiledata.md#class_TileData_method_get_occluder_polygon)

Returns the occluder polygon at index `polygon_index` from the TileSet occlusion layer with index `layer_id`.

The `flip_h`, `flip_v`, and `transpose` parameters can be `true` to transform the returned polygon.

---

<span id="class_TileData_method_get_occluder_polygons_count"></span>

[int](class_int.md#class_int) **get_occluder_polygons_count** ( layer_id: [int](class_int.md#class_int) ) *const* [🔗](class_tiledata.md#class_TileData_method_get_occluder_polygons_count)

Returns the number of occluder polygons of the tile in the TileSet occlusion layer with index `layer_id`.

---

<span id="class_TileData_method_get_terrain_peering_bit"></span>

[int](class_int.md#class_int) **get_terrain_peering_bit** ( peering_bit: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) ) *const* [🔗](class_tiledata.md#class_TileData_method_get_terrain_peering_bit)

Returns the tile's terrain bit for the given `peering_bit` direction. To check that a direction is valid, use [is_valid_terrain_peering_bit()](class_tiledata.md#class_TileData_method_is_valid_terrain_peering_bit).

---

<span id="class_TileData_method_has_custom_data"></span>

[bool](class_bool.md#class_bool) **has_custom_data** ( layer_name: [String](class_string.md#class_String) ) *const* [🔗](class_tiledata.md#class_TileData_method_has_custom_data)

Returns whether there exists a custom data layer named `layer_name`.

---

<span id="class_TileData_method_is_collision_polygon_one_way"></span>

[bool](class_bool.md#class_bool) **is_collision_polygon_one_way** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) *const* [🔗](class_tiledata.md#class_TileData_method_is_collision_polygon_one_way)

Returns whether one-way collisions are enabled for the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

<span id="class_TileData_method_is_valid_terrain_peering_bit"></span>

[bool](class_bool.md#class_bool) **is_valid_terrain_peering_bit** ( peering_bit: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor) ) *const* [🔗](class_tiledata.md#class_TileData_method_is_valid_terrain_peering_bit)

Returns whether the given `peering_bit` direction is valid for this tile.

---

<span id="class_TileData_method_remove_collision_polygon"></span>

void **remove_collision_polygon** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) [🔗](class_tiledata.md#class_TileData_method_remove_collision_polygon)

Removes the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

<span id="class_TileData_method_remove_occluder_polygon"></span>

void **remove_occluder_polygon** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int) ) [🔗](class_tiledata.md#class_TileData_method_remove_occluder_polygon)

Removes the polygon at index `polygon_index` for TileSet occlusion layer with index `layer_id`.

---

<span id="class_TileData_method_set_collision_polygon_one_way"></span>

void **set_collision_polygon_one_way** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), one_way: [bool](class_bool.md#class_bool) ) [🔗](class_tiledata.md#class_TileData_method_set_collision_polygon_one_way)

Enables/disables one-way collisions on the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

<span id="class_TileData_method_set_collision_polygon_one_way_margin"></span>

void **set_collision_polygon_one_way_margin** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), one_way_margin: [float](class_float.md#class_float) ) [🔗](class_tiledata.md#class_TileData_method_set_collision_polygon_one_way_margin)

Sets the one-way margin (for one-way platforms) of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

<span id="class_TileData_method_set_collision_polygon_points"></span>

void **set_collision_polygon_points** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), polygon: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) [🔗](class_tiledata.md#class_TileData_method_set_collision_polygon_points)

Sets the points of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.

---

<span id="class_TileData_method_set_collision_polygons_count"></span>

void **set_collision_polygons_count** ( layer_id: [int](class_int.md#class_int), polygons_count: [int](class_int.md#class_int) ) [🔗](class_tiledata.md#class_TileData_method_set_collision_polygons_count)

Sets the polygons count for TileSet physics layer with index `layer_id`.

---

<span id="class_TileData_method_set_constant_angular_velocity"></span>

void **set_constant_angular_velocity** ( layer_id: [int](class_int.md#class_int), velocity: [float](class_float.md#class_float) ) [🔗](class_tiledata.md#class_TileData_method_set_constant_angular_velocity)

Sets the constant angular velocity. This does not rotate the tile. This angular velocity is applied to objects colliding with this tile.

---

<span id="class_TileData_method_set_constant_linear_velocity"></span>

void **set_constant_linear_velocity** ( layer_id: [int](class_int.md#class_int), velocity: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_tiledata.md#class_TileData_method_set_constant_linear_velocity)

Sets the constant linear velocity. This does not move the tile. This linear velocity is applied to objects colliding with this tile. This is useful to create conveyor belts.

---

<span id="class_TileData_method_set_custom_data"></span>

void **set_custom_data** ( layer_name: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_tiledata.md#class_TileData_method_set_custom_data)

Sets the tile's custom data value for the TileSet custom data layer with name `layer_name`.

---

<span id="class_TileData_method_set_custom_data_by_layer_id"></span>

void **set_custom_data_by_layer_id** ( layer_id: [int](class_int.md#class_int), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_tiledata.md#class_TileData_method_set_custom_data_by_layer_id)

Sets the tile's custom data value for the TileSet custom data layer with index `layer_id`.

---

<span id="class_TileData_method_set_navigation_polygon"></span>

void **set_navigation_polygon** ( layer_id: [int](class_int.md#class_int), navigation_polygon: [NavigationPolygon](class_navigationpolygon.md#class_NavigationPolygon) ) [🔗](class_tiledata.md#class_TileData_method_set_navigation_polygon)

Sets the navigation polygon for the TileSet navigation layer with index `layer_id`.

---

<span id="class_TileData_method_set_occluder"></span>

void **set_occluder** ( layer_id: [int](class_int.md#class_int), occluder_polygon: [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) ) [🔗](class_tiledata.md#class_TileData_method_set_occluder)

**Deprecated:** Use [set_occluder_polygon()](class_tiledata.md#class_TileData_method_set_occluder_polygon) instead.

Sets the occluder for the TileSet occlusion layer with index `layer_id`.

---

<span id="class_TileData_method_set_occluder_polygon"></span>

void **set_occluder_polygon** ( layer_id: [int](class_int.md#class_int), polygon_index: [int](class_int.md#class_int), polygon: [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D) ) [🔗](class_tiledata.md#class_TileData_method_set_occluder_polygon)

Sets the occluder for polygon with index `polygon_index` in the TileSet occlusion layer with index `layer_id`.

---

<span id="class_TileData_method_set_occluder_polygons_count"></span>

void **set_occluder_polygons_count** ( layer_id: [int](class_int.md#class_int), polygons_count: [int](class_int.md#class_int) ) [🔗](class_tiledata.md#class_TileData_method_set_occluder_polygons_count)

Sets the occluder polygon count in the TileSet occlusion layer with index `layer_id`.

---

<span id="class_TileData_method_set_terrain_peering_bit"></span>

void **set_terrain_peering_bit** ( peering_bit: [CellNeighbor](class_tileset.md#enum_TileSet_CellNeighbor), terrain: [int](class_int.md#class_int) ) [🔗](class_tiledata.md#class_TileData_method_set_terrain_peering_bit)

Sets the tile's terrain bit for the given `peering_bit` direction. To check that a direction is valid, use [is_valid_terrain_peering_bit()](class_tiledata.md#class_TileData_method_is_valid_terrain_peering_bit).
