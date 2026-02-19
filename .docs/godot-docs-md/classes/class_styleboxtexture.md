<span id="class_StyleBoxTexture"></span>

## StyleBoxTexture

**Inherits:** [StyleBox](class_stylebox.md#class_StyleBox) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A texture-based nine-patch [StyleBox](class_stylebox.md#class_StyleBox).

### Description

A texture-based nine-patch [StyleBox](class_stylebox.md#class_StyleBox), in a way similar to [NinePatchRect](class_ninepatchrect.md#class_NinePatchRect). This stylebox performs a 3×3 scaling of a texture, where only the center cell is fully stretched. This makes it possible to design bordered styles regardless of the stylebox's size.

### Properties


| [AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) | [axis_stretch_horizontal](class_styleboxtexture.md#class_StyleBoxTexture_property_axis_stretch_horizontal) | `0` |
| --- | --- | --- |
| [AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) | [axis_stretch_vertical](class_styleboxtexture.md#class_StyleBoxTexture_property_axis_stretch_vertical) | `0` |
| [bool](class_bool.md#class_bool) | [draw_center](class_styleboxtexture.md#class_StyleBoxTexture_property_draw_center) | `true` |
| [float](class_float.md#class_float) | [expand_margin_bottom](class_styleboxtexture.md#class_StyleBoxTexture_property_expand_margin_bottom) | `0.0` |
| [float](class_float.md#class_float) | [expand_margin_left](class_styleboxtexture.md#class_StyleBoxTexture_property_expand_margin_left) | `0.0` |
| [float](class_float.md#class_float) | [expand_margin_right](class_styleboxtexture.md#class_StyleBoxTexture_property_expand_margin_right) | `0.0` |
| [float](class_float.md#class_float) | [expand_margin_top](class_styleboxtexture.md#class_StyleBoxTexture_property_expand_margin_top) | `0.0` |
| [Color](class_color.md#class_Color) | [modulate_color](class_styleboxtexture.md#class_StyleBoxTexture_property_modulate_color) | `Color(1, 1, 1, 1)` |
| [Rect2](class_rect2.md#class_Rect2) | [region_rect](class_styleboxtexture.md#class_StyleBoxTexture_property_region_rect) | `Rect2(0, 0, 0, 0)` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_styleboxtexture.md#class_StyleBoxTexture_property_texture) |
| [float](class_float.md#class_float) | [texture_margin_bottom](class_styleboxtexture.md#class_StyleBoxTexture_property_texture_margin_bottom) | `0.0` |
| [float](class_float.md#class_float) | [texture_margin_left](class_styleboxtexture.md#class_StyleBoxTexture_property_texture_margin_left) | `0.0` |
| [float](class_float.md#class_float) | [texture_margin_right](class_styleboxtexture.md#class_StyleBoxTexture_property_texture_margin_right) | `0.0` |
| [float](class_float.md#class_float) | [texture_margin_top](class_styleboxtexture.md#class_StyleBoxTexture_property_texture_margin_top) | `0.0` |

### Methods


| [float](class_float.md#class_float) | [get_expand_margin](class_styleboxtexture.md#class_StyleBoxTexture_method_get_expand_margin) ( margin: Side ) const |
| --- | --- |
| [float](class_float.md#class_float) | [get_texture_margin](class_styleboxtexture.md#class_StyleBoxTexture_method_get_texture_margin) ( margin: Side ) const |
| void | [set_expand_margin](class_styleboxtexture.md#class_StyleBoxTexture_method_set_expand_margin) ( margin: Side, size: [float](class_float.md#class_float) ) |
| void | [set_expand_margin_all](class_styleboxtexture.md#class_StyleBoxTexture_method_set_expand_margin_all) ( size: [float](class_float.md#class_float) ) |
| void | [set_texture_margin](class_styleboxtexture.md#class_StyleBoxTexture_method_set_texture_margin) ( margin: Side, size: [float](class_float.md#class_float) ) |
| void | [set_texture_margin_all](class_styleboxtexture.md#class_StyleBoxTexture_method_set_texture_margin_all) ( size: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_StyleBoxTexture_AxisStretchMode"></span>

enum **AxisStretchMode**: [🔗](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode)

<span id="class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_STRETCH"></span>

[AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) **AXIS_STRETCH_MODE_STRETCH** = `0`

Stretch the stylebox's texture. This results in visible distortion unless the texture size matches the stylebox's size perfectly.

<span id="class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_TILE"></span>

[AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) **AXIS_STRETCH_MODE_TILE** = `1`

Repeats the stylebox's texture to match the stylebox's size according to the nine-patch system.

<span id="class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_TILE_FIT"></span>

[AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) **AXIS_STRETCH_MODE_TILE_FIT** = `2`

Repeats the stylebox's texture to match the stylebox's size according to the nine-patch system. Unlike [AXIS_STRETCH_MODE_TILE](class_styleboxtexture.md#class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_TILE), the texture may be slightly stretched to make the nine-patch texture tile seamlessly.

---

### Property Descriptions

<span id="class_StyleBoxTexture_property_axis_stretch_horizontal"></span>

[AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) **axis_stretch_horizontal** = `0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_axis_stretch_horizontal)

- void **set_h_axis_stretch_mode** ( value: [AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) )
- [AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) **get_h_axis_stretch_mode** ( )

Controls how the stylebox's texture will be stretched or tiled horizontally.

---

<span id="class_StyleBoxTexture_property_axis_stretch_vertical"></span>

[AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) **axis_stretch_vertical** = `0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_axis_stretch_vertical)

- void **set_v_axis_stretch_mode** ( value: [AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) )
- [AxisStretchMode](class_styleboxtexture.md#enum_StyleBoxTexture_AxisStretchMode) **get_v_axis_stretch_mode** ( )

Controls how the stylebox's texture will be stretched or tiled vertically.

---

<span id="class_StyleBoxTexture_property_draw_center"></span>

[bool](class_bool.md#class_bool) **draw_center** = `true` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_draw_center)

- void **set_draw_center** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_draw_center_enabled** ( )

If `true`, the nine-patch texture's center tile will be drawn.

---

<span id="class_StyleBoxTexture_property_expand_margin_bottom"></span>

[float](class_float.md#class_float) **expand_margin_bottom** = `0.0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_expand_margin_bottom)

- void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const*

Expands the bottom margin of this style box when drawing, causing it to be drawn larger than requested.

---

<span id="class_StyleBoxTexture_property_expand_margin_left"></span>

[float](class_float.md#class_float) **expand_margin_left** = `0.0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_expand_margin_left)

- void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const*

Expands the left margin of this style box when drawing, causing it to be drawn larger than requested.

---

<span id="class_StyleBoxTexture_property_expand_margin_right"></span>

[float](class_float.md#class_float) **expand_margin_right** = `0.0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_expand_margin_right)

- void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const*

Expands the right margin of this style box when drawing, causing it to be drawn larger than requested.

---

<span id="class_StyleBoxTexture_property_expand_margin_top"></span>

[float](class_float.md#class_float) **expand_margin_top** = `0.0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_expand_margin_top)

- void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const*

Expands the top margin of this style box when drawing, causing it to be drawn larger than requested.

---

<span id="class_StyleBoxTexture_property_modulate_color"></span>

[Color](class_color.md#class_Color) **modulate_color** = `Color(1, 1, 1, 1)` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_modulate_color)

- void **set_modulate** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_modulate** ( )

Modulates the color of the texture when this style box is drawn.

---

<span id="class_StyleBoxTexture_property_region_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **region_rect** = `Rect2(0, 0, 0, 0)` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_region_rect)

- void **set_region_rect** ( value: [Rect2](class_rect2.md#class_Rect2) )
- [Rect2](class_rect2.md#class_Rect2) **get_region_rect** ( )

The region to use from the [texture](class_styleboxtexture.md#class_StyleBoxTexture_property_texture).

This is equivalent to first wrapping the [texture](class_styleboxtexture.md#class_StyleBoxTexture_property_texture) in an [AtlasTexture](class_atlastexture.md#class_AtlasTexture) with the same region.

If empty (`Rect2(0, 0, 0, 0)`), the whole [texture](class_styleboxtexture.md#class_StyleBoxTexture_property_texture) is used.

---

<span id="class_StyleBoxTexture_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

The texture to use when drawing this style box.

---

<span id="class_StyleBoxTexture_property_texture_margin_bottom"></span>

[float](class_float.md#class_float) **texture_margin_bottom** = `0.0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_texture_margin_bottom)

- void **set_texture_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_texture_margin** ( margin: Side ) *const*

Increases the bottom margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the bottom border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_bottom](class_stylebox.md#class_StyleBox_property_content_margin_bottom) if it is negative.

---

<span id="class_StyleBoxTexture_property_texture_margin_left"></span>

[float](class_float.md#class_float) **texture_margin_left** = `0.0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_texture_margin_left)

- void **set_texture_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_texture_margin** ( margin: Side ) *const*

Increases the left margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the left border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_left](class_stylebox.md#class_StyleBox_property_content_margin_left) if it is negative.

---

<span id="class_StyleBoxTexture_property_texture_margin_right"></span>

[float](class_float.md#class_float) **texture_margin_right** = `0.0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_texture_margin_right)

- void **set_texture_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_texture_margin** ( margin: Side ) *const*

Increases the right margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the right border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_right](class_stylebox.md#class_StyleBox_property_content_margin_right) if it is negative.

---

<span id="class_StyleBoxTexture_property_texture_margin_top"></span>

[float](class_float.md#class_float) **texture_margin_top** = `0.0` [🔗](class_styleboxtexture.md#class_StyleBoxTexture_property_texture_margin_top)

- void **set_texture_margin** ( margin: Side, size: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_texture_margin** ( margin: Side ) *const*

Increases the top margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the top border of the 3×3 box.

This is also the value used as fallback for [StyleBox.content_margin_top](class_stylebox.md#class_StyleBox_property_content_margin_top) if it is negative.

---

### Method Descriptions

<span id="class_StyleBoxTexture_method_get_expand_margin"></span>

[float](class_float.md#class_float) **get_expand_margin** ( margin: Side ) *const* [🔗](class_styleboxtexture.md#class_StyleBoxTexture_method_get_expand_margin)

Returns the expand margin size of the specified Side.

---

<span id="class_StyleBoxTexture_method_get_texture_margin"></span>

[float](class_float.md#class_float) **get_texture_margin** ( margin: Side ) *const* [🔗](class_styleboxtexture.md#class_StyleBoxTexture_method_get_texture_margin)

Returns the margin size of the specified Side.

---

<span id="class_StyleBoxTexture_method_set_expand_margin"></span>

void **set_expand_margin** ( margin: Side, size: [float](class_float.md#class_float) ) [🔗](class_styleboxtexture.md#class_StyleBoxTexture_method_set_expand_margin)

Sets the expand margin to `size` pixels for the specified Side.

---

<span id="class_StyleBoxTexture_method_set_expand_margin_all"></span>

void **set_expand_margin_all** ( size: [float](class_float.md#class_float) ) [🔗](class_styleboxtexture.md#class_StyleBoxTexture_method_set_expand_margin_all)

Sets the expand margin to `size` pixels for all sides.

---

<span id="class_StyleBoxTexture_method_set_texture_margin"></span>

void **set_texture_margin** ( margin: Side, size: [float](class_float.md#class_float) ) [🔗](class_styleboxtexture.md#class_StyleBoxTexture_method_set_texture_margin)

Sets the margin to `size` pixels for the specified Side.

---

<span id="class_StyleBoxTexture_method_set_texture_margin_all"></span>

void **set_texture_margin_all** ( size: [float](class_float.md#class_float) ) [🔗](class_styleboxtexture.md#class_StyleBoxTexture_method_set_texture_margin_all)

Sets the margin to `size` pixels for all sides.
