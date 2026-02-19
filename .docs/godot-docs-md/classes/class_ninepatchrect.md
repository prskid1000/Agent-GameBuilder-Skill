<span id="class_NinePatchRect"></span>

## NinePatchRect

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A control that displays a texture by keeping its corners intact, but tiling its edges and center.

### Description

Also known as 9-slice panels, **NinePatchRect** produces clean panels of any size based on a small texture. To do so, it splits the texture in a 3×3 grid. When you scale the node, it tiles the texture's edges horizontally or vertically, tiles the center on both axes, and leaves the corners unchanged.

### Properties


| [AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) | [axis_stretch_horizontal](class_ninepatchrect.md#class_NinePatchRect_property_axis_stretch_horizontal) | `0` |
| --- | --- | --- |
| [AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) | [axis_stretch_vertical](class_ninepatchrect.md#class_NinePatchRect_property_axis_stretch_vertical) | `0` |
| [bool](class_bool.md#class_bool) | [draw_center](class_ninepatchrect.md#class_NinePatchRect_property_draw_center) | `true` |
| [MouseFilter](class_control.md#enum_Control_MouseFilter) | mouse_filter | `2` (overrides [Control](class_control.md#class_Control_property_mouse_filter)) |
| [int](class_int.md#class_int) | [patch_margin_bottom](class_ninepatchrect.md#class_NinePatchRect_property_patch_margin_bottom) | `0` |
| [int](class_int.md#class_int) | [patch_margin_left](class_ninepatchrect.md#class_NinePatchRect_property_patch_margin_left) | `0` |
| [int](class_int.md#class_int) | [patch_margin_right](class_ninepatchrect.md#class_NinePatchRect_property_patch_margin_right) | `0` |
| [int](class_int.md#class_int) | [patch_margin_top](class_ninepatchrect.md#class_NinePatchRect_property_patch_margin_top) | `0` |
| [Rect2](class_rect2.md#class_Rect2) | [region_rect](class_ninepatchrect.md#class_NinePatchRect_property_region_rect) | `Rect2(0, 0, 0, 0)` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_ninepatchrect.md#class_NinePatchRect_property_texture) |

### Methods


| [int](class_int.md#class_int) | [get_patch_margin](class_ninepatchrect.md#class_NinePatchRect_method_get_patch_margin) ( margin: Side ) const |
| --- | --- |
| void | [set_patch_margin](class_ninepatchrect.md#class_NinePatchRect_method_set_patch_margin) ( margin: Side, value: [int](class_int.md#class_int) ) |

---

### Signals

<span id="class_NinePatchRect_signal_texture_changed"></span>

**texture_changed** ( ) [🔗](class_ninepatchrect.md#class_NinePatchRect_signal_texture_changed)

Emitted when the node's texture changes.

---

### Enumerations

<span id="enum_NinePatchRect_AxisStretchMode"></span>

enum **AxisStretchMode**: [🔗](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode)

<span id="class_NinePatchRect_constant_AXIS_STRETCH_MODE_STRETCH"></span>

[AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) **AXIS_STRETCH_MODE_STRETCH** = `0`

Stretches the center texture across the NinePatchRect. This may cause the texture to be distorted.

<span id="class_NinePatchRect_constant_AXIS_STRETCH_MODE_TILE"></span>

[AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) **AXIS_STRETCH_MODE_TILE** = `1`

Repeats the center texture across the NinePatchRect. This won't cause any visible distortion. The texture must be seamless for this to work without displaying artifacts between edges.

<span id="class_NinePatchRect_constant_AXIS_STRETCH_MODE_TILE_FIT"></span>

[AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) **AXIS_STRETCH_MODE_TILE_FIT** = `2`

Repeats the center texture across the NinePatchRect, but will also stretch the texture to make sure each tile is visible in full. This may cause the texture to be distorted, but less than [AXIS_STRETCH_MODE_STRETCH](class_ninepatchrect.md#class_NinePatchRect_constant_AXIS_STRETCH_MODE_STRETCH). The texture must be seamless for this to work without displaying artifacts between edges.

---

### Property Descriptions

<span id="class_NinePatchRect_property_axis_stretch_horizontal"></span>

[AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) **axis_stretch_horizontal** = `0` [🔗](class_ninepatchrect.md#class_NinePatchRect_property_axis_stretch_horizontal)

- void **set_h_axis_stretch_mode** ( value: [AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) )
- [AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) **get_h_axis_stretch_mode** ( )

The stretch mode to use for horizontal stretching/tiling.

---

<span id="class_NinePatchRect_property_axis_stretch_vertical"></span>

[AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) **axis_stretch_vertical** = `0` [🔗](class_ninepatchrect.md#class_NinePatchRect_property_axis_stretch_vertical)

- void **set_v_axis_stretch_mode** ( value: [AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) )
- [AxisStretchMode](class_ninepatchrect.md#enum_NinePatchRect_AxisStretchMode) **get_v_axis_stretch_mode** ( )

The stretch mode to use for vertical stretching/tiling.

---

<span id="class_NinePatchRect_property_draw_center"></span>

[bool](class_bool.md#class_bool) **draw_center** = `true` [🔗](class_ninepatchrect.md#class_NinePatchRect_property_draw_center)

- void **set_draw_center** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_draw_center_enabled** ( )

If `true`, draw the panel's center. Else, only draw the 9-slice's borders.

---

<span id="class_NinePatchRect_property_patch_margin_bottom"></span>

[int](class_int.md#class_int) **patch_margin_bottom** = `0` [🔗](class_ninepatchrect.md#class_NinePatchRect_property_patch_margin_bottom)

- void **set_patch_margin** ( margin: Side, value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_patch_margin** ( margin: Side ) *const*

The height of the 9-slice's bottom row. A margin of 16 means the 9-slice's bottom corners and side will have a height of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.

---

<span id="class_NinePatchRect_property_patch_margin_left"></span>

[int](class_int.md#class_int) **patch_margin_left** = `0` [🔗](class_ninepatchrect.md#class_NinePatchRect_property_patch_margin_left)

- void **set_patch_margin** ( margin: Side, value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_patch_margin** ( margin: Side ) *const*

The width of the 9-slice's left column. A margin of 16 means the 9-slice's left corners and side will have a width of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.

---

<span id="class_NinePatchRect_property_patch_margin_right"></span>

[int](class_int.md#class_int) **patch_margin_right** = `0` [🔗](class_ninepatchrect.md#class_NinePatchRect_property_patch_margin_right)

- void **set_patch_margin** ( margin: Side, value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_patch_margin** ( margin: Side ) *const*

The width of the 9-slice's right column. A margin of 16 means the 9-slice's right corners and side will have a width of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.

---

<span id="class_NinePatchRect_property_patch_margin_top"></span>

[int](class_int.md#class_int) **patch_margin_top** = `0` [🔗](class_ninepatchrect.md#class_NinePatchRect_property_patch_margin_top)

- void **set_patch_margin** ( margin: Side, value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_patch_margin** ( margin: Side ) *const*

The height of the 9-slice's top row. A margin of 16 means the 9-slice's top corners and side will have a height of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders.

---

<span id="class_NinePatchRect_property_region_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **region_rect** = `Rect2(0, 0, 0, 0)` [🔗](class_ninepatchrect.md#class_NinePatchRect_property_region_rect)

- void **set_region_rect** ( value: [Rect2](class_rect2.md#class_Rect2) )
- [Rect2](class_rect2.md#class_Rect2) **get_region_rect** ( )

Rectangular region of the texture to sample from. If you're working with an atlas, use this property to define the area the 9-slice should use. All other properties are relative to this one. If the rect is empty, NinePatchRect will use the whole texture.

---

<span id="class_NinePatchRect_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_ninepatchrect.md#class_NinePatchRect_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

The node's texture resource.

---

### Method Descriptions

<span id="class_NinePatchRect_method_get_patch_margin"></span>

[int](class_int.md#class_int) **get_patch_margin** ( margin: Side ) *const* [🔗](class_ninepatchrect.md#class_NinePatchRect_method_get_patch_margin)

Returns the size of the margin on the specified Side.

---

<span id="class_NinePatchRect_method_set_patch_margin"></span>

void **set_patch_margin** ( margin: Side, value: [int](class_int.md#class_int) ) [🔗](class_ninepatchrect.md#class_NinePatchRect_method_set_patch_margin)

Sets the size of the margin on the specified Side to `value` pixels.
