<span id="class_Line2D"></span>

## Line2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A 2D polyline that can optionally be textured.

### Description

This node draws a 2D polyline, i.e. a shape consisting of several points connected by segments. **Line2D** is not a mathematical polyline, i.e. the segments are not infinitely thin. It is intended for rendering and it can be colored and optionally textured.

 **Warning:** Certain configurations may be impossible to draw nicely, such as very sharp angles. In these situations, the node uses fallback drawing logic to look decent.

 **Note:** **Line2D** is drawn using a 2D mesh.

### Tutorials

- Matrix Transform Demo

- 2.5D Game Demo

### Properties


| [bool](class_bool.md#class_bool) | [antialiased](class_line2d.md#class_Line2D_property_antialiased) | `false` |
| --- | --- | --- |
| [LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) | [begin_cap_mode](class_line2d.md#class_Line2D_property_begin_cap_mode) | `0` |
| [bool](class_bool.md#class_bool) | [closed](class_line2d.md#class_Line2D_property_closed) | `false` |
| [Color](class_color.md#class_Color) | [default_color](class_line2d.md#class_Line2D_property_default_color) | `Color(1, 1, 1, 1)` |
| [LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) | [end_cap_mode](class_line2d.md#class_Line2D_property_end_cap_mode) | `0` |
| [Gradient](class_gradient.md#class_Gradient) | [gradient](class_line2d.md#class_Line2D_property_gradient) |
| [LineJointMode](class_line2d.md#enum_Line2D_LineJointMode) | [joint_mode](class_line2d.md#class_Line2D_property_joint_mode) | `0` |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [points](class_line2d.md#class_Line2D_property_points) | `PackedVector2Array()` |
| [int](class_int.md#class_int) | [round_precision](class_line2d.md#class_Line2D_property_round_precision) | `8` |
| [float](class_float.md#class_float) | [sharp_limit](class_line2d.md#class_Line2D_property_sharp_limit) | `2.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_line2d.md#class_Line2D_property_texture) |
| [LineTextureMode](class_line2d.md#enum_Line2D_LineTextureMode) | [texture_mode](class_line2d.md#class_Line2D_property_texture_mode) | `0` |
| [float](class_float.md#class_float) | [width](class_line2d.md#class_Line2D_property_width) | `10.0` |
| [Curve](class_curve.md#class_Curve) | [width_curve](class_line2d.md#class_Line2D_property_width_curve) |

### Methods


| void | [add_point](class_line2d.md#class_Line2D_method_add_point) ( position: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int) = -1 ) |
| --- | --- |
| void | [clear_points](class_line2d.md#class_Line2D_method_clear_points) ( ) |
| [int](class_int.md#class_int) | [get_point_count](class_line2d.md#class_Line2D_method_get_point_count) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_point_position](class_line2d.md#class_Line2D_method_get_point_position) ( index: [int](class_int.md#class_int) ) const |
| void | [remove_point](class_line2d.md#class_Line2D_method_remove_point) ( index: [int](class_int.md#class_int) ) |
| void | [set_point_position](class_line2d.md#class_Line2D_method_set_point_position) ( index: [int](class_int.md#class_int), position: [Vector2](class_vector2.md#class_Vector2) ) |

---

### Enumerations

<span id="enum_Line2D_LineJointMode"></span>

enum **LineJointMode**: [🔗](class_line2d.md#enum_Line2D_LineJointMode)

<span id="class_Line2D_constant_LINE_JOINT_SHARP"></span>

[LineJointMode](class_line2d.md#enum_Line2D_LineJointMode) **LINE_JOINT_SHARP** = `0`

Makes the polyline's joints pointy, connecting the sides of the two segments by extending them until they intersect. If the rotation of a joint is too big (based on [sharp_limit](class_line2d.md#class_Line2D_property_sharp_limit)), the joint falls back to [LINE_JOINT_BEVEL](class_line2d.md#class_Line2D_constant_LINE_JOINT_BEVEL) to prevent very long miters.

<span id="class_Line2D_constant_LINE_JOINT_BEVEL"></span>

[LineJointMode](class_line2d.md#enum_Line2D_LineJointMode) **LINE_JOINT_BEVEL** = `1`

Makes the polyline's joints bevelled/chamfered, connecting the sides of the two segments with a simple line.

<span id="class_Line2D_constant_LINE_JOINT_ROUND"></span>

[LineJointMode](class_line2d.md#enum_Line2D_LineJointMode) **LINE_JOINT_ROUND** = `2`

Makes the polyline's joints rounded, connecting the sides of the two segments with an arc. The detail of this arc depends on [round_precision](class_line2d.md#class_Line2D_property_round_precision).

---

<span id="enum_Line2D_LineCapMode"></span>

enum **LineCapMode**: [🔗](class_line2d.md#enum_Line2D_LineCapMode)

<span id="class_Line2D_constant_LINE_CAP_NONE"></span>

[LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) **LINE_CAP_NONE** = `0`

Draws no line cap.

<span id="class_Line2D_constant_LINE_CAP_BOX"></span>

[LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) **LINE_CAP_BOX** = `1`

Draws the line cap as a box, slightly extending the first/last segment.

<span id="class_Line2D_constant_LINE_CAP_ROUND"></span>

[LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) **LINE_CAP_ROUND** = `2`

Draws the line cap as a semicircle attached to the first/last segment.

---

<span id="enum_Line2D_LineTextureMode"></span>

enum **LineTextureMode**: [🔗](class_line2d.md#enum_Line2D_LineTextureMode)

<span id="class_Line2D_constant_LINE_TEXTURE_NONE"></span>

[LineTextureMode](class_line2d.md#enum_Line2D_LineTextureMode) **LINE_TEXTURE_NONE** = `0`

Takes the left pixels of the texture and renders them over the whole polyline.

<span id="class_Line2D_constant_LINE_TEXTURE_TILE"></span>

[LineTextureMode](class_line2d.md#enum_Line2D_LineTextureMode) **LINE_TEXTURE_TILE** = `1`

Tiles the texture over the polyline. [CanvasItem.texture_repeat](class_canvasitem.md#class_CanvasItem_property_texture_repeat) of the **Line2D** node must be [CanvasItem.TEXTURE_REPEAT_ENABLED](class_canvasitem.md#class_CanvasItem_constant_TEXTURE_REPEAT_ENABLED) or [CanvasItem.TEXTURE_REPEAT_MIRROR](class_canvasitem.md#class_CanvasItem_constant_TEXTURE_REPEAT_MIRROR) for it to work properly.

<span id="class_Line2D_constant_LINE_TEXTURE_STRETCH"></span>

[LineTextureMode](class_line2d.md#enum_Line2D_LineTextureMode) **LINE_TEXTURE_STRETCH** = `2`

Stretches the texture across the polyline. [CanvasItem.texture_repeat](class_canvasitem.md#class_CanvasItem_property_texture_repeat) of the **Line2D** node must be [CanvasItem.TEXTURE_REPEAT_DISABLED](class_canvasitem.md#class_CanvasItem_constant_TEXTURE_REPEAT_DISABLED) for best results.

---

### Property Descriptions

<span id="class_Line2D_property_antialiased"></span>

[bool](class_bool.md#class_bool) **antialiased** = `false` [🔗](class_line2d.md#class_Line2D_property_antialiased)

- void **set_antialiased** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_antialiased** ( )

If `true`, the polyline's border will be anti-aliased.

 **Note:** **Line2D** is not accelerated by batching when being anti-aliased.

---

<span id="class_Line2D_property_begin_cap_mode"></span>

[LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) **begin_cap_mode** = `0` [🔗](class_line2d.md#class_Line2D_property_begin_cap_mode)

- void **set_begin_cap_mode** ( value: [LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) )
- [LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) **get_begin_cap_mode** ( )

The style of the beginning of the polyline, if [closed](class_line2d.md#class_Line2D_property_closed) is `false`.

---

<span id="class_Line2D_property_closed"></span>

[bool](class_bool.md#class_bool) **closed** = `false` [🔗](class_line2d.md#class_Line2D_property_closed)

- void **set_closed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_closed** ( )

If `true` and the polyline has more than 2 points, the last point and the first one will be connected by a segment.

 **Note:** The shape of the closing segment is not guaranteed to be seamless if a [width_curve](class_line2d.md#class_Line2D_property_width_curve) is provided.

 **Note:** The joint between the closing segment and the first segment is drawn first and it samples the [gradient](class_line2d.md#class_Line2D_property_gradient) and the [width_curve](class_line2d.md#class_Line2D_property_width_curve) at the beginning. This is an implementation detail that might change in a future version.

---

<span id="class_Line2D_property_default_color"></span>

[Color](class_color.md#class_Color) **default_color** = `Color(1, 1, 1, 1)` [🔗](class_line2d.md#class_Line2D_property_default_color)

- void **set_default_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_default_color** ( )

The color of the polyline. Will not be used if a gradient is set.

---

<span id="class_Line2D_property_end_cap_mode"></span>

[LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) **end_cap_mode** = `0` [🔗](class_line2d.md#class_Line2D_property_end_cap_mode)

- void **set_end_cap_mode** ( value: [LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) )
- [LineCapMode](class_line2d.md#enum_Line2D_LineCapMode) **get_end_cap_mode** ( )

The style of the end of the polyline, if [closed](class_line2d.md#class_Line2D_property_closed) is `false`.

---

<span id="class_Line2D_property_gradient"></span>

[Gradient](class_gradient.md#class_Gradient) **gradient** [🔗](class_line2d.md#class_Line2D_property_gradient)

- void **set_gradient** ( value: [Gradient](class_gradient.md#class_Gradient) )
- [Gradient](class_gradient.md#class_Gradient) **get_gradient** ( )

The gradient is drawn through the whole line from start to finish. The [default_color](class_line2d.md#class_Line2D_property_default_color) will not be used if this property is set.

---

<span id="class_Line2D_property_joint_mode"></span>

[LineJointMode](class_line2d.md#enum_Line2D_LineJointMode) **joint_mode** = `0` [🔗](class_line2d.md#class_Line2D_property_joint_mode)

- void **set_joint_mode** ( value: [LineJointMode](class_line2d.md#enum_Line2D_LineJointMode) )
- [LineJointMode](class_line2d.md#enum_Line2D_LineJointMode) **get_joint_mode** ( )

The style of the connections between segments of the polyline.

---

<span id="class_Line2D_property_points"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **points** = `PackedVector2Array()` [🔗](class_line2d.md#class_Line2D_property_points)

- void **set_points** ( value: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )
- [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_points** ( )

The points of the polyline, interpreted in local 2D coordinates. Segments are drawn between the adjacent points in this array.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.

---

<span id="class_Line2D_property_round_precision"></span>

[int](class_int.md#class_int) **round_precision** = `8` [🔗](class_line2d.md#class_Line2D_property_round_precision)

- void **set_round_precision** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_round_precision** ( )

The smoothness used for rounded joints and caps. Higher values result in smoother corners, but are more demanding to render and update.

---

<span id="class_Line2D_property_sharp_limit"></span>

[float](class_float.md#class_float) **sharp_limit** = `2.0` [🔗](class_line2d.md#class_Line2D_property_sharp_limit)

- void **set_sharp_limit** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_sharp_limit** ( )

Determines the miter limit of the polyline. Normally, when [joint_mode](class_line2d.md#class_Line2D_property_joint_mode) is set to [LINE_JOINT_SHARP](class_line2d.md#class_Line2D_constant_LINE_JOINT_SHARP), sharp angles fall back to using the logic of [LINE_JOINT_BEVEL](class_line2d.md#class_Line2D_constant_LINE_JOINT_BEVEL) joints to prevent very long miters. Higher values of this property mean that the fallback to a bevel joint will happen at sharper angles.

---

<span id="class_Line2D_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_line2d.md#class_Line2D_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

The texture used for the polyline. Uses [texture_mode](class_line2d.md#class_Line2D_property_texture_mode) for drawing style.

---

<span id="class_Line2D_property_texture_mode"></span>

[LineTextureMode](class_line2d.md#enum_Line2D_LineTextureMode) **texture_mode** = `0` [🔗](class_line2d.md#class_Line2D_property_texture_mode)

- void **set_texture_mode** ( value: [LineTextureMode](class_line2d.md#enum_Line2D_LineTextureMode) )
- [LineTextureMode](class_line2d.md#enum_Line2D_LineTextureMode) **get_texture_mode** ( )

The style to render the [texture](class_line2d.md#class_Line2D_property_texture) of the polyline.

---

<span id="class_Line2D_property_width"></span>

[float](class_float.md#class_float) **width** = `10.0` [🔗](class_line2d.md#class_Line2D_property_width)

- void **set_width** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_width** ( )

The polyline's width.

---

<span id="class_Line2D_property_width_curve"></span>

[Curve](class_curve.md#class_Curve) **width_curve** [🔗](class_line2d.md#class_Line2D_property_width_curve)

- void **set_curve** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_curve** ( )

The polyline's width curve. The width of the polyline over its length will be equivalent to the value of the width curve over its domain. The width curve should be a unit [Curve](class_curve.md#class_Curve).

---

### Method Descriptions

<span id="class_Line2D_method_add_point"></span>

void **add_point** ( position: [Vector2](class_vector2.md#class_Vector2), index: [int](class_int.md#class_int) = -1 ) [🔗](class_line2d.md#class_Line2D_method_add_point)

Adds a point with the specified `position` relative to the polyline's own position. If no `index` is provided, the new point will be added to the end of the points array.

If `index` is given, the new point is inserted before the existing point identified by index `index`. The indices of the points after the new point get increased by 1. The provided `index` must not exceed the number of existing points in the polyline. See [get_point_count()](class_line2d.md#class_Line2D_method_get_point_count).

---

<span id="class_Line2D_method_clear_points"></span>

void **clear_points** ( ) [🔗](class_line2d.md#class_Line2D_method_clear_points)

Removes all points from the polyline, making it empty.

---

<span id="class_Line2D_method_get_point_count"></span>

[int](class_int.md#class_int) **get_point_count** ( ) *const* [🔗](class_line2d.md#class_Line2D_method_get_point_count)

Returns the number of points in the polyline.

---

<span id="class_Line2D_method_get_point_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_point_position** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_line2d.md#class_Line2D_method_get_point_position)

Returns the position of the point at index `index`.

---

<span id="class_Line2D_method_remove_point"></span>

void **remove_point** ( index: [int](class_int.md#class_int) ) [🔗](class_line2d.md#class_Line2D_method_remove_point)

Removes the point at index `index` from the polyline.

---

<span id="class_Line2D_method_set_point_position"></span>

void **set_point_position** ( index: [int](class_int.md#class_int), position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_line2d.md#class_Line2D_method_set_point_position)

Overwrites the position of the point at the given `index` with the supplied `position`.
