<span id="class_AStarGrid2D"></span>

## AStarGrid2D

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An implementation of A\* for finding the shortest path between two points on a partial 2D grid.

### Description

**AStarGrid2D** is a variant of [AStar2D](class_astar2d.md#class_AStar2D) that is specialized for partial 2D grids. It is simpler to use because it doesn't require you to manually create points and connect them together. This class also supports multiple types of heuristics, modes for diagonal movement, and a jumping mode to speed up calculations.

To use **AStarGrid2D**, you only need to set the [region](class_astargrid2d.md#class_AStarGrid2D_property_region) of the grid, optionally set the [cell_size](class_astargrid2d.md#class_AStarGrid2D_property_cell_size), and then call the [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) method:

.. tabs::

```
```

    var astar_grid = AStarGrid2D.new()
    astar_grid.region = Rect2i(0, 0, 32, 32)
    astar_grid.cell_size = Vector2(16, 16)
    astar_grid.update()
    print(astar_grid.get_id_path(Vector2i(0, 0), Vector2i(3, 4))) # Prints [(0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]
    print(astar_grid.get_point_path(Vector2i(0, 0), Vector2i(3, 4))) # Prints [(0, 0), (16, 16), (32, 32), (48, 48), (48, 64)]

```
```

    AStarGrid2D astarGrid = new AStarGrid2D();
    astarGrid.Region = new Rect2I(0, 0, 32, 32);
    astarGrid.CellSize = new Vector2I(16, 16);
    astarGrid.Update();
    GD.Print(astarGrid.GetIdPath(Vector2I.Zero, new Vector2I(3, 4))); // Prints [(0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]
    GD.Print(astarGrid.GetPointPath(Vector2I.Zero, new Vector2I(3, 4))); // Prints [(0, 0), (16, 16), (32, 32), (48, 48), (48, 64)]

To remove a point from the pathfinding grid, it must be set as "solid" with [set_point_solid()](class_astargrid2d.md#class_AStarGrid2D_method_set_point_solid).

### Tutorials

- Grid-based Navigation with AStarGrid2D Demo

### Properties


| [CellShape](class_astargrid2d.md#enum_AStarGrid2D_CellShape) | [cell_shape](class_astargrid2d.md#class_AStarGrid2D_property_cell_shape) | `0` |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [cell_size](class_astargrid2d.md#class_AStarGrid2D_property_cell_size) | `Vector2(1, 1)` |
| [Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) | [default_compute_heuristic](class_astargrid2d.md#class_AStarGrid2D_property_default_compute_heuristic) | `0` |
| [Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) | [default_estimate_heuristic](class_astargrid2d.md#class_AStarGrid2D_property_default_estimate_heuristic) | `0` |
| [DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) | [diagonal_mode](class_astargrid2d.md#class_AStarGrid2D_property_diagonal_mode) | `0` |
| [bool](class_bool.md#class_bool) | [jumping_enabled](class_astargrid2d.md#class_AStarGrid2D_property_jumping_enabled) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [offset](class_astargrid2d.md#class_AStarGrid2D_property_offset) | `Vector2(0, 0)` |
| [Rect2i](class_rect2i.md#class_Rect2i) | [region](class_astargrid2d.md#class_AStarGrid2D_property_region) | `Rect2i(0, 0, 0, 0)` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [size](class_astargrid2d.md#class_AStarGrid2D_property_size) | `Vector2i(0, 0)` |

### Methods


| [float](class_float.md#class_float) | [_compute_cost](class_astargrid2d.md#class_AStarGrid2D_private_method__compute_cost) ( from_id: [Vector2i](class_vector2i.md#class_Vector2i), to_id: [Vector2i](class_vector2i.md#class_Vector2i) ) | virtual | const |
| --- | --- | --- | --- |
| [float](class_float.md#class_float) | [_estimate_cost](class_astargrid2d.md#class_AStarGrid2D_private_method__estimate_cost) ( from_id: [Vector2i](class_vector2i.md#class_Vector2i), end_id: [Vector2i](class_vector2i.md#class_Vector2i) ) | virtual | const |
| void | [clear](class_astargrid2d.md#class_AStarGrid2D_method_clear) ( ) |
| void | [fill_solid_region](class_astargrid2d.md#class_AStarGrid2D_method_fill_solid_region) ( region: [Rect2i](class_rect2i.md#class_Rect2i), solid: [bool](class_bool.md#class_bool) = true ) |
| void | [fill_weight_scale_region](class_astargrid2d.md#class_AStarGrid2D_method_fill_weight_scale_region) ( region: [Rect2i](class_rect2i.md#class_Rect2i), weight_scale: [float](class_float.md#class_float) ) |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [get_id_path](class_astargrid2d.md#class_AStarGrid2D_method_get_id_path) ( from_id: [Vector2i](class_vector2i.md#class_Vector2i), to_id: [Vector2i](class_vector2i.md#class_Vector2i), allow_partial_path: [bool](class_bool.md#class_bool) = false ) |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_point_data_in_region](class_astargrid2d.md#class_AStarGrid2D_method_get_point_data_in_region) ( region: [Rect2i](class_rect2i.md#class_Rect2i) ) const |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [get_point_path](class_astargrid2d.md#class_AStarGrid2D_method_get_point_path) ( from_id: [Vector2i](class_vector2i.md#class_Vector2i), to_id: [Vector2i](class_vector2i.md#class_Vector2i), allow_partial_path: [bool](class_bool.md#class_bool) = false ) |
| [Vector2](class_vector2.md#class_Vector2) | [get_point_position](class_astargrid2d.md#class_AStarGrid2D_method_get_point_position) ( id: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [float](class_float.md#class_float) | [get_point_weight_scale](class_astargrid2d.md#class_AStarGrid2D_method_get_point_weight_scale) ( id: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [bool](class_bool.md#class_bool) | [is_dirty](class_astargrid2d.md#class_AStarGrid2D_method_is_dirty) ( ) const |
| [bool](class_bool.md#class_bool) | [is_in_bounds](class_astargrid2d.md#class_AStarGrid2D_method_is_in_bounds) ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_in_boundsv](class_astargrid2d.md#class_AStarGrid2D_method_is_in_boundsv) ( id: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [bool](class_bool.md#class_bool) | [is_point_solid](class_astargrid2d.md#class_AStarGrid2D_method_is_point_solid) ( id: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| void | [set_point_solid](class_astargrid2d.md#class_AStarGrid2D_method_set_point_solid) ( id: [Vector2i](class_vector2i.md#class_Vector2i), solid: [bool](class_bool.md#class_bool) = true ) |
| void | [set_point_weight_scale](class_astargrid2d.md#class_AStarGrid2D_method_set_point_weight_scale) ( id: [Vector2i](class_vector2i.md#class_Vector2i), weight_scale: [float](class_float.md#class_float) ) |
| void | [update](class_astargrid2d.md#class_AStarGrid2D_method_update) ( ) |

---

### Enumerations

<span id="enum_AStarGrid2D_Heuristic"></span>

enum **Heuristic**: [🔗](class_astargrid2d.md#enum_AStarGrid2D_Heuristic)

<span id="class_AStarGrid2D_constant_HEURISTIC_EUCLIDEAN"></span>

[Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) **HEURISTIC_EUCLIDEAN** = `0`

The Euclidean heuristic to be used for the pathfinding using the following formula:

::

    dx = abs(to_id.x - from_id.x)
    dy = abs(to_id.y - from_id.y)
    result = sqrt(dx * dx + dy * dy)

 **Note:** This is also the internal heuristic used in [AStar3D](class_astar3d.md#class_AStar3D) and [AStar2D](class_astar2d.md#class_AStar2D) by default (with the inclusion of possible z-axis coordinate).

<span id="class_AStarGrid2D_constant_HEURISTIC_MANHATTAN"></span>

[Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) **HEURISTIC_MANHATTAN** = `1`

The Manhattan heuristic to be used for the pathfinding using the following formula:

::

    dx = abs(to_id.x - from_id.x)
    dy = abs(to_id.y - from_id.y)
    result = dx + dy

 **Note:** This heuristic is intended to be used with 4-side orthogonal movements, provided by setting the [diagonal_mode](class_astargrid2d.md#class_AStarGrid2D_property_diagonal_mode) to [DIAGONAL_MODE_NEVER](class_astargrid2d.md#class_AStarGrid2D_constant_DIAGONAL_MODE_NEVER).

<span id="class_AStarGrid2D_constant_HEURISTIC_OCTILE"></span>

[Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) **HEURISTIC_OCTILE** = `2`

The Octile heuristic to be used for the pathfinding using the following formula:

::

    dx = abs(to_id.x - from_id.x)
    dy = abs(to_id.y - from_id.y)
    f = sqrt(2) - 1
    result = (dx < dy) ? f * dx + dy : f * dy + dx;

<span id="class_AStarGrid2D_constant_HEURISTIC_CHEBYSHEV"></span>

[Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) **HEURISTIC_CHEBYSHEV** = `3`

The Chebyshev heuristic to be used for the pathfinding using the following formula:

::

    dx = abs(to_id.x - from_id.x)
    dy = abs(to_id.y - from_id.y)
    result = max(dx, dy)

<span id="class_AStarGrid2D_constant_HEURISTIC_MAX"></span>

[Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) **HEURISTIC_MAX** = `4`

Represents the size of the [Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) enum.

---

<span id="enum_AStarGrid2D_DiagonalMode"></span>

enum **DiagonalMode**: [🔗](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode)

<span id="class_AStarGrid2D_constant_DIAGONAL_MODE_ALWAYS"></span>

[DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) **DIAGONAL_MODE_ALWAYS** = `0`

The pathfinding algorithm will ignore solid neighbors around the target cell and allow passing using diagonals.

<span id="class_AStarGrid2D_constant_DIAGONAL_MODE_NEVER"></span>

[DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) **DIAGONAL_MODE_NEVER** = `1`

The pathfinding algorithm will ignore all diagonals and the way will be always orthogonal.

<span id="class_AStarGrid2D_constant_DIAGONAL_MODE_AT_LEAST_ONE_WALKABLE"></span>

[DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) **DIAGONAL_MODE_AT_LEAST_ONE_WALKABLE** = `2`

The pathfinding algorithm will avoid using diagonals if at least two obstacles have been placed around the neighboring cells of the specific path segment.

<span id="class_AStarGrid2D_constant_DIAGONAL_MODE_ONLY_IF_NO_OBSTACLES"></span>

[DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) **DIAGONAL_MODE_ONLY_IF_NO_OBSTACLES** = `3`

The pathfinding algorithm will avoid using diagonals if any obstacle has been placed around the neighboring cells of the specific path segment.

<span id="class_AStarGrid2D_constant_DIAGONAL_MODE_MAX"></span>

[DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) **DIAGONAL_MODE_MAX** = `4`

Represents the size of the [DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) enum.

---

<span id="enum_AStarGrid2D_CellShape"></span>

enum **CellShape**: [🔗](class_astargrid2d.md#enum_AStarGrid2D_CellShape)

<span id="class_AStarGrid2D_constant_CELL_SHAPE_SQUARE"></span>

[CellShape](class_astargrid2d.md#enum_AStarGrid2D_CellShape) **CELL_SHAPE_SQUARE** = `0`

Rectangular cell shape.

<span id="class_AStarGrid2D_constant_CELL_SHAPE_ISOMETRIC_RIGHT"></span>

[CellShape](class_astargrid2d.md#enum_AStarGrid2D_CellShape) **CELL_SHAPE_ISOMETRIC_RIGHT** = `1`

Diamond cell shape (for isometric look). Cell coordinates layout where the horizontal axis goes up-right, and the vertical one goes down-right.

<span id="class_AStarGrid2D_constant_CELL_SHAPE_ISOMETRIC_DOWN"></span>

[CellShape](class_astargrid2d.md#enum_AStarGrid2D_CellShape) **CELL_SHAPE_ISOMETRIC_DOWN** = `2`

Diamond cell shape (for isometric look). Cell coordinates layout where the horizontal axis goes down-right, and the vertical one goes down-left.

<span id="class_AStarGrid2D_constant_CELL_SHAPE_MAX"></span>

[CellShape](class_astargrid2d.md#enum_AStarGrid2D_CellShape) **CELL_SHAPE_MAX** = `3`

Represents the size of the [CellShape](class_astargrid2d.md#enum_AStarGrid2D_CellShape) enum.

---

### Property Descriptions

<span id="class_AStarGrid2D_property_cell_shape"></span>

[CellShape](class_astargrid2d.md#enum_AStarGrid2D_CellShape) **cell_shape** = `0` [🔗](class_astargrid2d.md#class_AStarGrid2D_property_cell_shape)

- void **set_cell_shape** ( value: [CellShape](class_astargrid2d.md#enum_AStarGrid2D_CellShape) )
- [CellShape](class_astargrid2d.md#enum_AStarGrid2D_CellShape) **get_cell_shape** ( )

The cell shape. Affects how the positions are placed in the grid. If changed, [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) needs to be called before finding the next path.

---

<span id="class_AStarGrid2D_property_cell_size"></span>

[Vector2](class_vector2.md#class_Vector2) **cell_size** = `Vector2(1, 1)` [🔗](class_astargrid2d.md#class_AStarGrid2D_property_cell_size)

- void **set_cell_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_cell_size** ( )

The size of the point cell which will be applied to calculate the resulting point position returned by [get_point_path()](class_astargrid2d.md#class_AStarGrid2D_method_get_point_path). If changed, [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) needs to be called before finding the next path.

---

<span id="class_AStarGrid2D_property_default_compute_heuristic"></span>

[Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) **default_compute_heuristic** = `0` [🔗](class_astargrid2d.md#class_AStarGrid2D_property_default_compute_heuristic)

- void **set_default_compute_heuristic** ( value: [Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) )
- [Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) **get_default_compute_heuristic** ( )

The default [Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) which will be used to calculate the cost between two points if [_compute_cost()](class_astargrid2d.md#class_AStarGrid2D_private_method__compute_cost) was not overridden.

---

<span id="class_AStarGrid2D_property_default_estimate_heuristic"></span>

[Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) **default_estimate_heuristic** = `0` [🔗](class_astargrid2d.md#class_AStarGrid2D_property_default_estimate_heuristic)

- void **set_default_estimate_heuristic** ( value: [Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) )
- [Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) **get_default_estimate_heuristic** ( )

The default [Heuristic](class_astargrid2d.md#enum_AStarGrid2D_Heuristic) which will be used to calculate the cost between the point and the end point if [_estimate_cost()](class_astargrid2d.md#class_AStarGrid2D_private_method__estimate_cost) was not overridden.

---

<span id="class_AStarGrid2D_property_diagonal_mode"></span>

[DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) **diagonal_mode** = `0` [🔗](class_astargrid2d.md#class_AStarGrid2D_property_diagonal_mode)

- void **set_diagonal_mode** ( value: [DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) )
- [DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) **get_diagonal_mode** ( )

A specific [DiagonalMode](class_astargrid2d.md#enum_AStarGrid2D_DiagonalMode) mode which will force the path to avoid or accept the specified diagonals.

---

<span id="class_AStarGrid2D_property_jumping_enabled"></span>

[bool](class_bool.md#class_bool) **jumping_enabled** = `false` [🔗](class_astargrid2d.md#class_AStarGrid2D_property_jumping_enabled)

- void **set_jumping_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_jumping_enabled** ( )

Enables or disables jumping to skip up the intermediate points and speeds up the searching algorithm.

 **Note:** Currently, toggling it on disables the consideration of weight scaling in pathfinding.

---

<span id="class_AStarGrid2D_property_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **offset** = `Vector2(0, 0)` [🔗](class_astargrid2d.md#class_AStarGrid2D_property_offset)

- void **set_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_offset** ( )

The offset of the grid which will be applied to calculate the resulting point position returned by [get_point_path()](class_astargrid2d.md#class_AStarGrid2D_method_get_point_path). If changed, [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) needs to be called before finding the next path.

---

<span id="class_AStarGrid2D_property_region"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **region** = `Rect2i(0, 0, 0, 0)` [🔗](class_astargrid2d.md#class_AStarGrid2D_property_region)

- void **set_region** ( value: [Rect2i](class_rect2i.md#class_Rect2i) )
- [Rect2i](class_rect2i.md#class_Rect2i) **get_region** ( )

The region of grid cells available for pathfinding. If changed, [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) needs to be called before finding the next path.

---

<span id="class_AStarGrid2D_property_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **size** = `Vector2i(0, 0)` [🔗](class_astargrid2d.md#class_AStarGrid2D_property_size)

- void **set_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_size** ( )

**Deprecated:** Use [region](class_astargrid2d.md#class_AStarGrid2D_property_region) instead.

The size of the grid (number of cells of size [cell_size](class_astargrid2d.md#class_AStarGrid2D_property_cell_size) on each axis). If changed, [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) needs to be called before finding the next path.

---

### Method Descriptions

<span id="class_AStarGrid2D_private_method__compute_cost"></span>

[float](class_float.md#class_float) **_compute_cost** ( from_id: [Vector2i](class_vector2i.md#class_Vector2i), to_id: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* *const* [🔗](class_astargrid2d.md#class_AStarGrid2D_private_method__compute_cost)

Called when computing the cost between two connected points.

Note that this function is hidden in the default **AStarGrid2D** class.

---

<span id="class_AStarGrid2D_private_method__estimate_cost"></span>

[float](class_float.md#class_float) **_estimate_cost** ( from_id: [Vector2i](class_vector2i.md#class_Vector2i), end_id: [Vector2i](class_vector2i.md#class_Vector2i) ) *virtual* *const* [🔗](class_astargrid2d.md#class_AStarGrid2D_private_method__estimate_cost)

Called when estimating the cost between a point and the path's ending point.

Note that this function is hidden in the default **AStarGrid2D** class.

---

<span id="class_AStarGrid2D_method_clear"></span>

void **clear** ( ) [🔗](class_astargrid2d.md#class_AStarGrid2D_method_clear)

Clears the grid and sets the [region](class_astargrid2d.md#class_AStarGrid2D_property_region) to `Rect2i(0, 0, 0, 0)`.

---

<span id="class_AStarGrid2D_method_fill_solid_region"></span>

void **fill_solid_region** ( region: [Rect2i](class_rect2i.md#class_Rect2i), solid: [bool](class_bool.md#class_bool) = true ) [🔗](class_astargrid2d.md#class_AStarGrid2D_method_fill_solid_region)

Fills the given `region` on the grid with the specified value for the solid flag.

 **Note:** Calling [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) is not needed after the call of this function.

---

<span id="class_AStarGrid2D_method_fill_weight_scale_region"></span>

void **fill_weight_scale_region** ( region: [Rect2i](class_rect2i.md#class_Rect2i), weight_scale: [float](class_float.md#class_float) ) [🔗](class_astargrid2d.md#class_AStarGrid2D_method_fill_weight_scale_region)

Fills the given `region` on the grid with the specified value for the weight scale.

 **Note:** Calling [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) is not needed after the call of this function.

---

<span id="class_AStarGrid2D_method_get_id_path"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **get_id_path** ( from_id: [Vector2i](class_vector2i.md#class_Vector2i), to_id: [Vector2i](class_vector2i.md#class_Vector2i), allow_partial_path: [bool](class_bool.md#class_bool) = false ) [🔗](class_astargrid2d.md#class_AStarGrid2D_method_get_id_path)

Returns an array with the IDs of the points that form the path found by AStar2D between the given points. The array is ordered from the starting point to the ending point of the path.

If `from_id` point is disabled, returns an empty array (even if `from_id == to_id`).

If `from_id` point is not disabled, there is no valid path to the target, and `allow_partial_path` is `true`, returns a path to the point closest to the target that can be reached.

 **Note:** When `allow_partial_path` is `true` and `to_id` is solid the search may take an unusually long time to finish.

---

<span id="class_AStarGrid2D_method_get_point_data_in_region"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_point_data_in_region** ( region: [Rect2i](class_rect2i.md#class_Rect2i) ) *const* [🔗](class_astargrid2d.md#class_AStarGrid2D_method_get_point_data_in_region)

Returns an array of dictionaries with point data (`id`: [Vector2i](class_vector2i.md#class_Vector2i), `position`: [Vector2](class_vector2.md#class_Vector2), `solid`: [bool](class_bool.md#class_bool), `weight_scale`: [float](class_float.md#class_float)) within a `region`.

---

<span id="class_AStarGrid2D_method_get_point_path"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_point_path** ( from_id: [Vector2i](class_vector2i.md#class_Vector2i), to_id: [Vector2i](class_vector2i.md#class_Vector2i), allow_partial_path: [bool](class_bool.md#class_bool) = false ) [🔗](class_astargrid2d.md#class_AStarGrid2D_method_get_point_path)

Returns an array with the points that are in the path found by **AStarGrid2D** between the given points. The array is ordered from the starting point to the ending point of the path.

If `from_id` point is disabled, returns an empty array (even if `from_id == to_id`).

If `from_id` point is not disabled, there is no valid path to the target, and `allow_partial_path` is `true`, returns a path to the point closest to the target that can be reached.

 **Note:** This method is not thread-safe; it can only be used from a single [Thread](class_thread.md#class_Thread) at a given time. Consider using [Mutex](class_mutex.md#class_Mutex) to ensure exclusive access to one thread to avoid race conditions.

Additionally, when `allow_partial_path` is `true` and `to_id` is solid the search may take an unusually long time to finish.

---

<span id="class_AStarGrid2D_method_get_point_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_point_position** ( id: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_astargrid2d.md#class_AStarGrid2D_method_get_point_position)

Returns the position of the point associated with the given `id`.

---

<span id="class_AStarGrid2D_method_get_point_weight_scale"></span>

[float](class_float.md#class_float) **get_point_weight_scale** ( id: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_astargrid2d.md#class_AStarGrid2D_method_get_point_weight_scale)

Returns the weight scale of the point associated with the given `id`.

---

<span id="class_AStarGrid2D_method_is_dirty"></span>

[bool](class_bool.md#class_bool) **is_dirty** ( ) *const* [🔗](class_astargrid2d.md#class_AStarGrid2D_method_is_dirty)

Indicates that the grid parameters were changed and [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) needs to be called.

---

<span id="class_AStarGrid2D_method_is_in_bounds"></span>

[bool](class_bool.md#class_bool) **is_in_bounds** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) *const* [🔗](class_astargrid2d.md#class_AStarGrid2D_method_is_in_bounds)

Returns `true` if the `x` and `y` is a valid grid coordinate (id), i.e. if it is inside [region](class_astargrid2d.md#class_AStarGrid2D_property_region). Equivalent to `region.has_point(Vector2i(x, y))`.

---

<span id="class_AStarGrid2D_method_is_in_boundsv"></span>

[bool](class_bool.md#class_bool) **is_in_boundsv** ( id: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_astargrid2d.md#class_AStarGrid2D_method_is_in_boundsv)

Returns `true` if the `id` vector is a valid grid coordinate, i.e. if it is inside [region](class_astargrid2d.md#class_AStarGrid2D_property_region). Equivalent to `region.has_point(id)`.

---

<span id="class_AStarGrid2D_method_is_point_solid"></span>

[bool](class_bool.md#class_bool) **is_point_solid** ( id: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_astargrid2d.md#class_AStarGrid2D_method_is_point_solid)

Returns `true` if a point is disabled for pathfinding. By default, all points are enabled.

---

<span id="class_AStarGrid2D_method_set_point_solid"></span>

void **set_point_solid** ( id: [Vector2i](class_vector2i.md#class_Vector2i), solid: [bool](class_bool.md#class_bool) = true ) [🔗](class_astargrid2d.md#class_AStarGrid2D_method_set_point_solid)

Disables or enables the specified point for pathfinding. Useful for making an obstacle. By default, all points are enabled.

 **Note:** Calling [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) is not needed after the call of this function.

---

<span id="class_AStarGrid2D_method_set_point_weight_scale"></span>

void **set_point_weight_scale** ( id: [Vector2i](class_vector2i.md#class_Vector2i), weight_scale: [float](class_float.md#class_float) ) [🔗](class_astargrid2d.md#class_AStarGrid2D_method_set_point_weight_scale)

Sets the `weight_scale` for the point with the given `id`. The `weight_scale` is multiplied by the result of [_compute_cost()](class_astargrid2d.md#class_AStarGrid2D_private_method__compute_cost) when determining the overall cost of traveling across a segment from a neighboring point to this point.

 **Note:** Calling [update()](class_astargrid2d.md#class_AStarGrid2D_method_update) is not needed after the call of this function.

---

<span id="class_AStarGrid2D_method_update"></span>

void **update** ( ) [🔗](class_astargrid2d.md#class_AStarGrid2D_method_update)

Updates the internal state of the grid according to the parameters to prepare it to search the path. Needs to be called if parameters like [region](class_astargrid2d.md#class_AStarGrid2D_property_region), [cell_size](class_astargrid2d.md#class_AStarGrid2D_property_cell_size) or [offset](class_astargrid2d.md#class_AStarGrid2D_property_offset) are changed. [is_dirty()](class_astargrid2d.md#class_AStarGrid2D_method_is_dirty) will return `true` if this is the case and this needs to be called.

 **Note:** All point data (solidity and weight scale) will be cleared.
