<span id="class_NavigationMeshSourceGeometryData2D"></span>

## NavigationMeshSourceGeometryData2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Container for parsed source geometry data used in navigation mesh baking.

### Description

Container for parsed source geometry data used in navigation mesh baking.

### Methods


| void | [add_obstruction_outline](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_add_obstruction_outline) ( shape_outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) |
| --- | --- |
| void | [add_projected_obstruction](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_add_projected_obstruction) ( vertices: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), carve: [bool](class_bool.md#class_bool) ) |
| void | [add_traversable_outline](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_add_traversable_outline) ( shape_outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) |
| void | [append_obstruction_outlines](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_append_obstruction_outlines) ( obstruction_outlines: [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] ) |
| void | [append_traversable_outlines](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_append_traversable_outlines) ( traversable_outlines: [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] ) |
| void | [clear](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_clear) ( ) |
| void | [clear_projected_obstructions](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_clear_projected_obstructions) ( ) |
| [Rect2](class_rect2.md#class_Rect2) | [get_bounds](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_get_bounds) ( ) |
| [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] | [get_obstruction_outlines](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_get_obstruction_outlines) ( ) const |
| [Array](class_array.md#class_Array) | [get_projected_obstructions](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_get_projected_obstructions) ( ) const |
| [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] | [get_traversable_outlines](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_get_traversable_outlines) ( ) const |
| [bool](class_bool.md#class_bool) | [has_data](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_has_data) ( ) |
| void | [merge](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_merge) ( other_geometry: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D) ) |
| void | [set_obstruction_outlines](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_set_obstruction_outlines) ( obstruction_outlines: [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] ) |
| void | [set_projected_obstructions](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_set_projected_obstructions) ( projected_obstructions: [Array](class_array.md#class_Array) ) |
| void | [set_traversable_outlines](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_set_traversable_outlines) ( traversable_outlines: [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] ) |

---

### Method Descriptions

<span id="class_NavigationMeshSourceGeometryData2D_method_add_obstruction_outline"></span>

void **add_obstruction_outline** ( shape_outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_add_obstruction_outline)

Adds the outline points of a shape as obstructed area.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_add_projected_obstruction"></span>

void **add_projected_obstruction** ( vertices: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), carve: [bool](class_bool.md#class_bool) ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_add_projected_obstruction)

Adds a projected obstruction shape to the source geometry. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_add_traversable_outline"></span>

void **add_traversable_outline** ( shape_outline: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_add_traversable_outline)

Adds the outline points of a shape as traversable area.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_append_obstruction_outlines"></span>

void **append_obstruction_outlines** ( obstruction_outlines: [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_append_obstruction_outlines)

Appends another array of `obstruction_outlines` at the end of the existing obstruction outlines array.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_append_traversable_outlines"></span>

void **append_traversable_outlines** ( traversable_outlines: [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_append_traversable_outlines)

Appends another array of `traversable_outlines` at the end of the existing traversable outlines array.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_clear"></span>

void **clear** ( ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_clear)

Clears the internal data.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_clear_projected_obstructions"></span>

void **clear_projected_obstructions** ( ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_clear_projected_obstructions)

Clears all projected obstructions.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_get_bounds"></span>

[Rect2](class_rect2.md#class_Rect2) **get_bounds** ( ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_get_bounds)

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_get_obstruction_outlines"></span>

[Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] **get_obstruction_outlines** ( ) *const* [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_get_obstruction_outlines)

Returns all the obstructed area outlines arrays.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_get_projected_obstructions"></span>

[Array](class_array.md#class_Array) **get_projected_obstructions** ( ) *const* [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_get_projected_obstructions)

Returns the projected obstructions as an [Array](class_array.md#class_Array) of dictionaries. Each [Dictionary](class_dictionary.md#class_Dictionary) contains the following entries:

- `vertices` - A [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) that defines the outline points of the projected shape.

- `carve` - A [bool](class_bool.md#class_bool) that defines how the projected shape affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_get_traversable_outlines"></span>

[Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] **get_traversable_outlines** ( ) *const* [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_get_traversable_outlines)

Returns all the traversable area outlines arrays.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_has_data"></span>

[bool](class_bool.md#class_bool) **has_data** ( ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_has_data)

Returns `true` when parsed source geometry data exists.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_merge"></span>

void **merge** ( other_geometry: [NavigationMeshSourceGeometryData2D](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D) ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_merge)

Adds the geometry data of another **NavigationMeshSourceGeometryData2D** to the navigation mesh baking data.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_set_obstruction_outlines"></span>

void **set_obstruction_outlines** ( obstruction_outlines: [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_set_obstruction_outlines)

Sets all the obstructed area outlines arrays.

---

<span id="class_NavigationMeshSourceGeometryData2D_method_set_projected_obstructions"></span>

void **set_projected_obstructions** ( projected_obstructions: [Array](class_array.md#class_Array) ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_set_projected_obstructions)

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:

.. tabs::

```
```

    "vertices" : PackedFloat32Array
    "carve" : bool

---

<span id="class_NavigationMeshSourceGeometryData2D_method_set_traversable_outlines"></span>

void **set_traversable_outlines** ( traversable_outlines: [Array](class_array.md#class_Array)\[[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array)\] ) [🔗](class_navigationmeshsourcegeometrydata2d.md#class_NavigationMeshSourceGeometryData2D_method_set_traversable_outlines)

Sets all the traversable area outlines arrays.
