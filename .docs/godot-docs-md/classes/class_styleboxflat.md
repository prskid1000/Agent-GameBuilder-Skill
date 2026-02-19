<span id="class_StyleBoxFlat"></span>

## StyleBoxFlat

**Inherits:** [StyleBox](class_stylebox.md#class_StyleBox) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A customizable [StyleBox](class_stylebox.md#class_StyleBox) that doesn't use a texture.

### Description

By configuring various properties of this style box, you can achieve many common looks without the need of a texture. This includes optionally rounded borders, antialiasing, shadows, and skew.

Setting corner radius to high values is allowed. As soon as corners overlap, the stylebox will switch to a relative system:

.. code:: text

    height = 30
    corner_radius_top_left = 50
    corner_radius_bottom_left = 100

The relative system now would take the 1:2 ratio of the two left corners to calculate the actual corner width. Both corners added will **never** be more than the height. Result:

.. code:: text

    corner_radius_top_left: 10
    corner_radius_bottom_left: 20

### Properties


| [bool](class_bool.md#class_bool) | [anti_aliasing](class_styleboxflat.md#class_StyleBoxFlat_property_anti_aliasing) | `true` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [anti_aliasing_size](class_styleboxflat.md#class_StyleBoxFlat_property_anti_aliasing_size) | `1.0` |
| [Color](class_color.md#class_Color) | [bg_color](class_styleboxflat.md#class_StyleBoxFlat_property_bg_color) | `Color(0.6, 0.6, 0.6, 1)` |
| [bool](class_bool.md#class_bool) | [border_blend](class_styleboxflat.md#class_StyleBoxFlat_property_border_blend) | `false` |
| [Color](class_color.md#class_Color) | [border_color](class_styleboxflat.md#class_StyleBoxFlat_property_border_color) | `Color(0.8, 0.8, 0.8, 1)` |
| [int](class_int.md#class_int) | [border_width_bottom](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_bottom) | `0` |
| [int](class_int.md#class_int) | [border_width_left](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_left) | `0` |
| [int](class_int.md#class_int) | [border_width_right](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_right) | `0` |
| [int](class_int.md#class_int) | [border_width_top](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_top) | `0` |
| [int](class_int.md#class_int) | [corner_detail](class_styleboxflat.md#class_StyleBoxFlat_property_corner_detail) | `8` |
| [int](class_int.md#class_int) | [corner_radius_bottom_left](class_styleboxflat.md#class_StyleBoxFlat_property_corner_radius_bottom_left) | `0` |
| [int](class_int.md#class_int) | [corner_radius_bottom_right](class_styleboxflat.md#class_StyleBoxFlat_property_corner_radius_bottom_right) | `0` |
| [int](class_int.md#class_int) | [corner_radius_top_left](class_styleboxflat.md#class_StyleBoxFlat_property_corner_radius_top_left) | `0` |
| [int](class_int.md#class_int) | [corner_radius_top_right](class_styleboxflat.md#class_StyleBoxFlat_property_corner_radius_top_right) | `0` |
| [bool](class_bool.md#class_bool) | [draw_center](class_styleboxflat.md#class_StyleBoxFlat_property_draw_center) | `true` |
| [float](class_float.md#class_float) | [expand_margin_bottom](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_bottom) | `0.0` |
| [float](class_float.md#class_float) | [expand_margin_left](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_left) | `0.0` |
| [float](class_float.md#class_float) | [expand_margin_right](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_right) | `0.0` |
| [float](class_float.md#class_float) | [expand_margin_top](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_top) | `0.0` |
| [Color](class_color.md#class_Color) | [shadow_color](class_styleboxflat.md#class_StyleBoxFlat_property_shadow_color) | `Color(0, 0, 0, 0.6)` |
| [Vector2](class_vector2.md#class_Vector2) | [shadow_offset](class_styleboxflat.md#class_StyleBoxFlat_property_shadow_offset) | `Vector2(0, 0)` |
| [int](class_int.md#class_int) | [shadow_size](class_styleboxflat.md#class_StyleBoxFlat_property_shadow_size) | `0` |
| [Vector2](class_vector2.md#class_Vector2) | [skew](class_styleboxflat.md#class_StyleBoxFlat_property_skew) | `Vector2(0, 0)` |

### Methods


| [int](class_int.md#class_int) | [get_border_width](class_styleboxflat.md#class_StyleBoxFlat_method_get_border_width) ( margin: Side ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_border_width_min](class_styleboxflat.md#class_StyleBoxFlat_method_get_border_width_min) ( ) const |
| [int](class_int.md#class_int) | [get_corner_radius](class_styleboxflat.md#class_StyleBoxFlat_method_get_corner_radius) ( corner: Corner ) const |
| [float](class_float.md#class_float) | [get_expand_margin](class_styleboxflat.md#class_StyleBoxFlat_method_get_expand_margin) ( margin: Side ) const |
| void | [set_border_width](class_styleboxflat.md#class_StyleBoxFlat_method_set_border_width) ( margin: Side, width: [int](class_int.md#class_int) ) |
| void | [set_border_width_all](class_styleboxflat.md#class_StyleBoxFlat_method_set_border_width_all) ( width: [int](class_int.md#class_int) ) |
| void | [set_corner_radius](class_styleboxflat.md#class_StyleBoxFlat_method_set_corner_radius) ( corner: Corner, radius: [int](class_int.md#class_int) ) |
| void | [set_corner_radius_all](class_styleboxflat.md#class_StyleBoxFlat_method_set_corner_radius_all) ( radius: [int](class_int.md#class_int) ) |
| void | [set_expand_margin](class_styleboxflat.md#class_StyleBoxFlat_method_set_expand_margin) ( margin: Side, size: [float](class_float.md#class_float) ) |
| void | [set_expand_margin_all](class_styleboxflat.md#class_StyleBoxFlat_method_set_expand_margin_all) ( size: [float](class_float.md#class_float) ) |

---

### Property Descriptions

<span id="class_StyleBoxFlat_property_anti_aliasing"></span>

[bool](class_bool.md#class_bool) **anti_aliasing** = `true` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_anti_aliasing)

- void **set_anti_aliased** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_anti_aliased** ( )

Antialiasing draws a small ring around the edges, which fades to transparency. As a result, edges look much smoother. This is only noticeable when using rounded corners or [skew](class_styleboxflat.md#class_StyleBoxFlat_property_skew).

 **Note:** When using beveled corners with 45-degree angles ([corner_detail](class_styleboxflat.md#class_StyleBoxFlat_property_corner_detail) = 1), it is recommended to set [anti_aliasing](class_styleboxflat.md#class_StyleBoxFlat_property_anti_aliasing) to `false` to ensure crisp visuals and avoid possible visual glitches.

---

<span id="class_StyleBoxFlat_property_anti_aliasing_size"></span>

[float](class_float.md#class_float) **anti_aliasing_size** = `1.0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_anti_aliasing_size)

- void **set_aa_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_aa_size** ( )

This changes the size of the antialiasing effect. `1.0` is recommended for an optimal result at 100% scale, identical to how rounded rectangles are rendered in web browsers and most vector drawing software.

 **Note:** Higher values may produce a blur effect but can also create undesired artifacts on small boxes with large-radius corners.

---

<span id="class_StyleBoxFlat_property_bg_color"></span>

[Color](class_color.md#class_Color) **bg_color** = `Color(0.6, 0.6, 0.6, 1)` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_bg_color)

- void **set_bg_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_bg_color** ( )

The background color of the stylebox.

---

<span id="class_StyleBoxFlat_property_border_blend"></span>

[bool](class_bool.md#class_bool) **border_blend** = `false` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_border_blend)

- void **set_border_blend** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_border_blend** ( )

If `true`, the border will fade into the background color.

---

<span id="class_StyleBoxFlat_property_border_color"></span>

[Color](class_color.md#class_Color) **border_color** = `Color(0.8, 0.8, 0.8, 1)` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_border_color)

- void **set_border_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_border_color** ( )

Sets the color of the border.

---

<span id="class_StyleBoxFlat_property_border_width_bottom"></span>

[int](class_int.md#class_int) **border_width_bottom** = `0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_bottom)

- void **set_border_width** ( margin: Side, width: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_border_width** ( margin: Side ) *const*

Border width for the bottom border.

---

<span id="class_StyleBoxFlat_property_border_width_left"></span>

[int](class_int.md#class_int) **border_width_left** = `0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_left)

- void **set_border_width** ( margin: Side, width: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_border_width** ( margin: Side ) *const*

Border width for the left border.

---

<span id="class_StyleBoxFlat_property_border_width_right"></span>

[int](class_int.md#class_int) **border_width_right** = `0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_right)

- void **set_border_width** ( margin: Side, width: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_border_width** ( margin: Side ) *const*

Border width for the right border.

---

<span id="class_StyleBoxFlat_property_border_width_top"></span>

[int](class_int.md#class_int) **border_width_top** = `0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_top)

- void **set_border_width** ( margin: Side, width: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_border_width** ( margin: Side ) *const*

Border width for the top border.

---

<span id="class_StyleBoxFlat_property_corner_detail"></span>

[int](class_int.md#class_int) **corner_detail** = `8` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_corner_detail)

- void **set_corner_detail** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_corner_detail** ( )

This sets the number of vertices used for each corner. Higher values result in rounder corners but take more processing power to compute. When choosing a value, you should take the corner radius ([set_corner_radius_all()](class_styleboxflat.md#class_StyleBoxFlat_method_set_corner_radius_all)) into account.

For corner radii less than 10, `4` or `5` should be enough. For corner radii less than 30, values between `8` and `12` should be enough.

A corner detail of `1` will result in chamfered corners instead of rounded corners, which is useful for some artistic effects.

---

<span id="class_StyleBoxFlat_property_corner_radius_bottom_left"></span>

[int](class_int.md#class_int) **corner_radius_bottom_left** = `0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_corner_radius_bottom_left)

- void **set_corner_radius** ( corner: Corner, radius: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_corner_radius** ( corner: Corner ) *const*

The bottom-left corner's radius. If `0`, the corner is not rounded.

---

<span id="class_StyleBoxFlat_property_corner_radius_bottom_right"></span>

[int](class_int.md#class_int) **corner_radius_bottom_right** = `0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_corner_radius_bottom_right)

- void **set_corner_radius** ( corner: Corner, radius: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_corner_radius** ( corner: Corner ) *const*

The bottom-right corner's radius. If `0`, the corner is not rounded.

---

<span id="class_StyleBoxFlat_property_corner_radius_top_left"></span>

[int](class_int.md#class_int) **corner_radius_top_left** = `0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_corner_radius_top_left)

- void **set_corner_radius** ( corner: Corner, radius: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_corner_radius** ( corner: Corner ) *const*

The top-left corner's radius. If `0`, the corner is not rounded.

---

<span id="class_StyleBoxFlat_property_corner_radius_top_right"></span>

[int](class_int.md#class_int) **corner_radius_top_right** = `0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_corner_radius_top_right)

- void **set_corner_radius** ( corner: Corner, radius: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_corner_radius** ( corner: Corner ) *const*

The top-right corner's radius. If `0`, the corner is not rounded.

---

<span id="class_StyleBoxFlat_property_draw_center"></span>

[bool](class_bool.md#class_bool) **draw_center** = `true` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_draw_center)

- void **set_draw_center** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_draw_center_enabled** ( )

Toggles drawing of the inner part of the stylebox.

---

<span id="class_StyleBoxFlat_property_expand_margin_bottom"></span>

[float](class_float.md#class_float) **expand_margin_bottom** = `0.0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_bottom)

- void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const*

Expands the stylebox outside of the control rect on the bottom edge. Useful in combination with [border_width_bottom](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_bottom) to draw a border outside the control rect.

 **Note:** Unlike [StyleBox.content_margin_bottom](class_stylebox.md#class_StyleBox_property_content_margin_bottom), [expand_margin_bottom](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_bottom) does *not* affect the size of the clickable area for [Control](class_control.md#class_Control) s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---

<span id="class_StyleBoxFlat_property_expand_margin_left"></span>

[float](class_float.md#class_float) **expand_margin_left** = `0.0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_left)

- void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const*

Expands the stylebox outside of the control rect on the left edge. Useful in combination with [border_width_left](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_left) to draw a border outside the control rect.

 **Note:** Unlike [StyleBox.content_margin_left](class_stylebox.md#class_StyleBox_property_content_margin_left), [expand_margin_left](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_left) does *not* affect the size of the clickable area for [Control](class_control.md#class_Control) s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---

<span id="class_StyleBoxFlat_property_expand_margin_right"></span>

[float](class_float.md#class_float) **expand_margin_right** = `0.0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_right)

- void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const*

Expands the stylebox outside of the control rect on the right edge. Useful in combination with [border_width_right](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_right) to draw a border outside the control rect.

 **Note:** Unlike [StyleBox.content_margin_right](class_stylebox.md#class_StyleBox_property_content_margin_right), [expand_margin_right](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_right) does *not* affect the size of the clickable area for [Control](class_control.md#class_Control) s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---

<span id="class_StyleBoxFlat_property_expand_margin_top"></span>

[float](class_float.md#class_float) **expand_margin_top** = `0.0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_top)

- void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const*

Expands the stylebox outside of the control rect on the top edge. Useful in combination with [border_width_top](class_styleboxflat.md#class_StyleBoxFlat_property_border_width_top) to draw a border outside the control rect.

 **Note:** Unlike [StyleBox.content_margin_top](class_stylebox.md#class_StyleBox_property_content_margin_top), [expand_margin_top](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_top) does *not* affect the size of the clickable area for [Control](class_control.md#class_Control) s. This can negatively impact usability if used wrong, as the user may try to click an area of the StyleBox that cannot actually receive clicks.

---

<span id="class_StyleBoxFlat_property_shadow_color"></span>

[Color](class_color.md#class_Color) **shadow_color** = `Color(0, 0, 0, 0.6)` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_shadow_color)

- void **set_shadow_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_shadow_color** ( )

The color of the shadow. This has no effect if [shadow_size](class_styleboxflat.md#class_StyleBoxFlat_property_shadow_size) is lower than 1.

---

<span id="class_StyleBoxFlat_property_shadow_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **shadow_offset** = `Vector2(0, 0)` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_shadow_offset)

- void **set_shadow_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_shadow_offset** ( )

The shadow offset in pixels. Adjusts the position of the shadow relatively to the stylebox.

---

<span id="class_StyleBoxFlat_property_shadow_size"></span>

[int](class_int.md#class_int) **shadow_size** = `0` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_shadow_size)

- void **set_shadow_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_shadow_size** ( )

The shadow size in pixels.

---

<span id="class_StyleBoxFlat_property_skew"></span>

[Vector2](class_vector2.md#class_Vector2) **skew** = `Vector2(0, 0)` [🔗](class_styleboxflat.md#class_StyleBoxFlat_property_skew)

- void **set_skew** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_skew** ( )

If set to a non-zero value on either axis, [skew](class_styleboxflat.md#class_StyleBoxFlat_property_skew) distorts the StyleBox horizontally and/or vertically. This can be used for "futuristic"-style UIs. Positive values skew the StyleBox towards the right (X axis) and upwards (Y axis), while negative values skew the StyleBox towards the left (X axis) and downwards (Y axis).

 **Note:** To ensure text does not touch the StyleBox's edges, consider increasing the [StyleBox](class_stylebox.md#class_StyleBox)'s content margin (see [StyleBox.content_margin_bottom](class_stylebox.md#class_StyleBox_property_content_margin_bottom)). It is preferable to increase the content margin instead of the expand margin (see [expand_margin_bottom](class_styleboxflat.md#class_StyleBoxFlat_property_expand_margin_bottom)), as increasing the expand margin does not increase the size of the clickable area for [Control](class_control.md#class_Control) s.

---

### Method Descriptions

<span id="class_StyleBoxFlat_method_get_border_width"></span>

[int](class_int.md#class_int) **get_border_width** ( margin: Side ) *const* [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_get_border_width)

Returns the specified Side's border width.

---

<span id="class_StyleBoxFlat_method_get_border_width_min"></span>

[int](class_int.md#class_int) **get_border_width_min** ( ) *const* [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_get_border_width_min)

Returns the smallest border width out of all four borders.

---

<span id="class_StyleBoxFlat_method_get_corner_radius"></span>

[int](class_int.md#class_int) **get_corner_radius** ( corner: Corner ) *const* [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_get_corner_radius)

Returns the given `corner`'s radius.

---

<span id="class_StyleBoxFlat_method_get_expand_margin"></span>

[float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const* [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_get_expand_margin)

Returns the size of the specified Side's expand margin.

---

<span id="class_StyleBoxFlat_method_set_border_width"></span>

void **set_border_width** ( margin: Side, width: [int](class_int.md#class_int) ) [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_set_border_width)

Sets the specified Side's border width to `width` pixels.

---

<span id="class_StyleBoxFlat_method_set_border_width_all"></span>

void **set_border_width_all** ( width: [int](class_int.md#class_int) ) [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_set_border_width_all)

Sets the border width to `width` pixels for all sides.

---

<span id="class_StyleBoxFlat_method_set_corner_radius"></span>

void **set_corner_radius** ( corner: Corner, radius: [int](class_int.md#class_int) ) [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_set_corner_radius)

Sets the corner radius to `radius` pixels for the given `corner`.

---

<span id="class_StyleBoxFlat_method_set_corner_radius_all"></span>

void **set_corner_radius_all** ( radius: [int](class_int.md#class_int) ) [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_set_corner_radius_all)

Sets the corner radius to `radius` pixels for all corners.

---

<span id="class_StyleBoxFlat_method_set_expand_margin"></span>

void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) ) [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_set_expand_margin)

Sets the expand margin to `size` pixels for the specified Side.

---

<span id="class_StyleBoxFlat_method_set_expand_margin_all"></span>

void **set_expand_margin_all** ( size: [float](class_float.md#class_float) ) [🔗](class_styleboxflat.md#class_StyleBoxFlat_method_set_expand_margin_all)

Sets the expand margin to `size` pixels for all sides.
