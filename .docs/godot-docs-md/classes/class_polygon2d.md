<span id="class_Polygon2D"></span>

## Polygon2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A 2D polygon.

### Description

A Polygon2D is defined by a set of points. Each point is connected to the next, with the final point being connected to the first, resulting in a closed polygon. Polygon2Ds can be filled with color (solid or gradient) or filled with a given texture.

### Properties


| [bool](class_bool.md#class_bool) | [antialiased](class_polygon2d.md#class_Polygon2D_property_antialiased) | `false` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [color](class_polygon2d.md#class_Polygon2D_property_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [internal_vertex_count](class_polygon2d.md#class_Polygon2D_property_internal_vertex_count) | `0` |
| [float](class_float.md#class_float) | [invert_border](class_polygon2d.md#class_Polygon2D_property_invert_border) | `100.0` |
| [bool](class_bool.md#class_bool) | [invert_enabled](class_polygon2d.md#class_Polygon2D_property_invert_enabled) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [offset](class_polygon2d.md#class_Polygon2D_property_offset) | `Vector2(0, 0)` |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [polygon](class_polygon2d.md#class_Polygon2D_property_polygon) | `PackedVector2Array()` |
| [Array](class_array.md#class_Array) | [polygons](class_polygon2d.md#class_Polygon2D_property_polygons) | `[]` |
| [NodePath](class_nodepath.md#class_NodePath) | [skeleton](class_polygon2d.md#class_Polygon2D_property_skeleton) | `NodePath("")` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_polygon2d.md#class_Polygon2D_property_texture) |
| [Vector2](class_vector2.md#class_Vector2) | [texture_offset](class_polygon2d.md#class_Polygon2D_property_texture_offset) | `Vector2(0, 0)` |
| [float](class_float.md#class_float) | [texture_rotation](class_polygon2d.md#class_Polygon2D_property_texture_rotation) | `0.0` |
| [Vector2](class_vector2.md#class_Vector2) | [texture_scale](class_polygon2d.md#class_Polygon2D_property_texture_scale) | `Vector2(1, 1)` |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [uv](class_polygon2d.md#class_Polygon2D_property_uv) | `PackedVector2Array()` |
| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [vertex_colors](class_polygon2d.md#class_Polygon2D_property_vertex_colors) | `PackedColorArray()` |

### Methods


| void | [add_bone](class_polygon2d.md#class_Polygon2D_method_add_bone) ( path: [NodePath](class_nodepath.md#class_NodePath), weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |
| --- | --- |
| void | [clear_bones](class_polygon2d.md#class_Polygon2D_method_clear_bones) ( ) |
| void | [erase_bone](class_polygon2d.md#class_Polygon2D_method_erase_bone) ( index: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_bone_count](class_polygon2d.md#class_Polygon2D_method_get_bone_count) ( ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_bone_path](class_polygon2d.md#class_Polygon2D_method_get_bone_path) ( index: [int](class_int.md#class_int) ) const |
| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [get_bone_weights](class_polygon2d.md#class_Polygon2D_method_get_bone_weights) ( index: [int](class_int.md#class_int) ) const |
| void | [set_bone_path](class_polygon2d.md#class_Polygon2D_method_set_bone_path) ( index: [int](class_int.md#class_int), path: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_bone_weights](class_polygon2d.md#class_Polygon2D_method_set_bone_weights) ( index: [int](class_int.md#class_int), weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |

---

### Property Descriptions

<span id="class_Polygon2D_property_antialiased"></span>

[bool](class_bool.md#class_bool) **antialiased** = `false` [🔗](class_polygon2d.md#class_Polygon2D_property_antialiased)

- void **set_antialiased** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_antialiased** ( )

If `true`, polygon edges will be anti-aliased.

---

<span id="class_Polygon2D_property_color"></span>

[Color](class_color.md#class_Color) **color** = `Color(1, 1, 1, 1)` [🔗](class_polygon2d.md#class_Polygon2D_property_color)

- void **set_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_color** ( )

The polygon's fill color. If [texture](class_polygon2d.md#class_Polygon2D_property_texture) is set, it will be multiplied by this color. It will also be the default color for vertices not set in [vertex_colors](class_polygon2d.md#class_Polygon2D_property_vertex_colors).

---

<span id="class_Polygon2D_property_internal_vertex_count"></span>

[int](class_int.md#class_int) **internal_vertex_count** = `0` [🔗](class_polygon2d.md#class_Polygon2D_property_internal_vertex_count)

- void **set_internal_vertex_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_internal_vertex_count** ( )

Number of internal vertices, used for UV mapping.

---

<span id="class_Polygon2D_property_invert_border"></span>

[float](class_float.md#class_float) **invert_border** = `100.0` [🔗](class_polygon2d.md#class_Polygon2D_property_invert_border)

- void **set_invert_border** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_invert_border** ( )

Added padding applied to the bounding box when [invert_enabled](class_polygon2d.md#class_Polygon2D_property_invert_enabled) is set to `true`. Setting this value too small may result in a "Bad Polygon" error.

---

<span id="class_Polygon2D_property_invert_enabled"></span>

[bool](class_bool.md#class_bool) **invert_enabled** = `false` [🔗](class_polygon2d.md#class_Polygon2D_property_invert_enabled)

- void **set_invert_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_invert_enabled** ( )

If `true`, the polygon will be inverted, containing the area outside the defined points and extending to the [invert_border](class_polygon2d.md#class_Polygon2D_property_invert_border).

---

<span id="class_Polygon2D_property_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **offset** = `Vector2(0, 0)` [🔗](class_polygon2d.md#class_Polygon2D_property_offset)

- void **set_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_offset** ( )

The offset applied to each vertex.

---

<span id="class_Polygon2D_property_polygon"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **polygon** = `PackedVector2Array()` [🔗](class_polygon2d.md#class_Polygon2D_property_polygon)

- void **set_polygon** ( value: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )
- [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_polygon** ( )

The polygon's list of vertices. The final point will be connected to the first.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.

---

<span id="class_Polygon2D_property_polygons"></span>

[Array](class_array.md#class_Array) **polygons** = `[]` [🔗](class_polygon2d.md#class_Polygon2D_property_polygons)

- void **set_polygons** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_polygons** ( )

The list of polygons, in case more than one is being represented. Every individual polygon is stored as a [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) where each [int](class_int.md#class_int) is an index to a point in [polygon](class_polygon2d.md#class_Polygon2D_property_polygon). If empty, this property will be ignored, and the resulting single polygon will be composed of all points in [polygon](class_polygon2d.md#class_Polygon2D_property_polygon), using the order they are stored in.

---

<span id="class_Polygon2D_property_skeleton"></span>

[NodePath](class_nodepath.md#class_NodePath) **skeleton** = `NodePath("")` [🔗](class_polygon2d.md#class_Polygon2D_property_skeleton)

- void **set_skeleton** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_skeleton** ( )

Path to a [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) node used for skeleton-based deformations of this polygon. If empty or invalid, skeletal deformations will not be used.

---

<span id="class_Polygon2D_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_polygon2d.md#class_Polygon2D_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

The polygon's fill texture. Use [uv](class_polygon2d.md#class_Polygon2D_property_uv) to set texture coordinates.

---

<span id="class_Polygon2D_property_texture_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **texture_offset** = `Vector2(0, 0)` [🔗](class_polygon2d.md#class_Polygon2D_property_texture_offset)

- void **set_texture_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_texture_offset** ( )

Amount to offset the polygon's [texture](class_polygon2d.md#class_Polygon2D_property_texture). If set to `Vector2(0, 0)`, the texture's origin (its top-left corner) will be placed at the polygon's position.

---

<span id="class_Polygon2D_property_texture_rotation"></span>

[float](class_float.md#class_float) **texture_rotation** = `0.0` [🔗](class_polygon2d.md#class_Polygon2D_property_texture_rotation)

- void **set_texture_rotation** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_texture_rotation** ( )

The texture's rotation in radians.

---

<span id="class_Polygon2D_property_texture_scale"></span>

[Vector2](class_vector2.md#class_Vector2) **texture_scale** = `Vector2(1, 1)` [🔗](class_polygon2d.md#class_Polygon2D_property_texture_scale)

- void **set_texture_scale** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_texture_scale** ( )

Amount to multiply the [uv](class_polygon2d.md#class_Polygon2D_property_uv) coordinates when using [texture](class_polygon2d.md#class_Polygon2D_property_texture). Larger values make the texture smaller, and vice versa.

---

<span id="class_Polygon2D_property_uv"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **uv** = `PackedVector2Array()` [🔗](class_polygon2d.md#class_Polygon2D_property_uv)

- void **set_uv** ( value: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )
- [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_uv** ( )

Texture coordinates for each vertex of the polygon. There should be one UV value per polygon vertex. If there are fewer, undefined vertices will use `Vector2(0, 0)`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.

---

<span id="class_Polygon2D_property_vertex_colors"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **vertex_colors** = `PackedColorArray()` [🔗](class_polygon2d.md#class_Polygon2D_property_vertex_colors)

- void **set_vertex_colors** ( value: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) )
- [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **get_vertex_colors** ( )

Color for each vertex. Colors are interpolated between vertices, resulting in smooth gradients. There should be one per polygon vertex. If there are fewer, undefined vertices will use [color](class_polygon2d.md#class_Polygon2D_property_color).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) for more details.

---

### Method Descriptions

<span id="class_Polygon2D_method_add_bone"></span>

void **add_bone** ( path: [NodePath](class_nodepath.md#class_NodePath), weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_polygon2d.md#class_Polygon2D_method_add_bone)

Adds a bone with the specified `path` and `weights`.

---

<span id="class_Polygon2D_method_clear_bones"></span>

void **clear_bones** ( ) [🔗](class_polygon2d.md#class_Polygon2D_method_clear_bones)

Removes all bones from this **Polygon2D**.

---

<span id="class_Polygon2D_method_erase_bone"></span>

void **erase_bone** ( index: [int](class_int.md#class_int) ) [🔗](class_polygon2d.md#class_Polygon2D_method_erase_bone)

Removes the specified bone from this **Polygon2D**.

---

<span id="class_Polygon2D_method_get_bone_count"></span>

[int](class_int.md#class_int) **get_bone_count** ( ) *const* [🔗](class_polygon2d.md#class_Polygon2D_method_get_bone_count)

Returns the number of bones in this **Polygon2D**.

---

<span id="class_Polygon2D_method_get_bone_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_bone_path** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_polygon2d.md#class_Polygon2D_method_get_bone_path)

Returns the path to the node associated with the specified bone.

---

<span id="class_Polygon2D_method_get_bone_weights"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **get_bone_weights** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_polygon2d.md#class_Polygon2D_method_get_bone_weights)

Returns the weight values of the specified bone.

---

<span id="class_Polygon2D_method_set_bone_path"></span>

void **set_bone_path** ( index: [int](class_int.md#class_int), path: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_polygon2d.md#class_Polygon2D_method_set_bone_path)

Sets the path to the node associated with the specified bone.

---

<span id="class_Polygon2D_method_set_bone_weights"></span>

void **set_bone_weights** ( index: [int](class_int.md#class_int), weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_polygon2d.md#class_Polygon2D_method_set_bone_weights)

Sets the weight values for the specified bone.
