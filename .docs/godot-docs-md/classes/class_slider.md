<span id="class_Slider"></span>

## Slider

**Inherits:** [Range](class_range.md#class_Range) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [HSlider](class_hslider.md#class_HSlider), [VSlider](class_vslider.md#class_VSlider)

Abstract base class for sliders.

### Description

Abstract base class for sliders, used to adjust a value by moving a grabber along a horizontal or vertical axis. Sliders are [Range](class_range.md#class_Range)-based controls.

### Properties


| [bool](class_bool.md#class_bool) | [editable](class_slider.md#class_Slider_property_editable) | `true` |
| --- | --- | --- |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `2` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [bool](class_bool.md#class_bool) | [scrollable](class_slider.md#class_Slider_property_scrollable) | `true` |
| [float](class_float.md#class_float) | step | `1.0` (overrides [Range](class_range.md#class_Range_property_step)) |
| [int](class_int.md#class_int) | [tick_count](class_slider.md#class_Slider_property_tick_count) | `0` |
| [bool](class_bool.md#class_bool) | [ticks_on_borders](class_slider.md#class_Slider_property_ticks_on_borders) | `false` |
| [TickPosition](class_slider.md#enum_Slider_TickPosition) | [ticks_position](class_slider.md#class_Slider_property_ticks_position) | `0` |

### Theme Properties


| [int](class_int.md#class_int) | [center_grabber](class_slider.md#class_Slider_theme_constant_center_grabber) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [grabber_offset](class_slider.md#class_Slider_theme_constant_grabber_offset) | `0` |
| [int](class_int.md#class_int) | [tick_offset](class_slider.md#class_Slider_theme_constant_tick_offset) | `0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [grabber](class_slider.md#class_Slider_theme_icon_grabber) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [grabber_disabled](class_slider.md#class_Slider_theme_icon_grabber_disabled) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [grabber_highlight](class_slider.md#class_Slider_theme_icon_grabber_highlight) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [tick](class_slider.md#class_Slider_theme_icon_tick) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [grabber_area](class_slider.md#class_Slider_theme_style_grabber_area) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [grabber_area_highlight](class_slider.md#class_Slider_theme_style_grabber_area_highlight) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [slider](class_slider.md#class_Slider_theme_style_slider) |

---

### Signals

<span id="class_Slider_signal_drag_ended"></span>

**drag_ended** ( value_changed: [bool](class_bool.md#class_bool) ) [🔗](class_slider.md#class_Slider_signal_drag_ended)

Emitted when the grabber stops being dragged. If `value_changed` is `true`, [Range.value](class_range.md#class_Range_property_value) is different from the value when the dragging was started.

---

<span id="class_Slider_signal_drag_started"></span>

**drag_started** ( ) [🔗](class_slider.md#class_Slider_signal_drag_started)

Emitted when the grabber starts being dragged. This is emitted before the corresponding [Range.value_changed](class_range.md#class_Range_signal_value_changed) signal.

---

### Enumerations

<span id="enum_Slider_TickPosition"></span>

enum **TickPosition**: [🔗](class_slider.md#enum_Slider_TickPosition)

<span id="class_Slider_constant_TICK_POSITION_BOTTOM_RIGHT"></span>

[TickPosition](class_slider.md#enum_Slider_TickPosition) **TICK_POSITION_BOTTOM_RIGHT** = `0`

Places the ticks at the bottom of the [HSlider](class_hslider.md#class_HSlider), or right of the [VSlider](class_vslider.md#class_VSlider).

<span id="class_Slider_constant_TICK_POSITION_TOP_LEFT"></span>

[TickPosition](class_slider.md#enum_Slider_TickPosition) **TICK_POSITION_TOP_LEFT** = `1`

Places the ticks at the top of the [HSlider](class_hslider.md#class_HSlider), or left of the [VSlider](class_vslider.md#class_VSlider).

<span id="class_Slider_constant_TICK_POSITION_BOTH"></span>

[TickPosition](class_slider.md#enum_Slider_TickPosition) **TICK_POSITION_BOTH** = `2`

Places the ticks at the both sides of the slider.

<span id="class_Slider_constant_TICK_POSITION_CENTER"></span>

[TickPosition](class_slider.md#enum_Slider_TickPosition) **TICK_POSITION_CENTER** = `3`

Places the ticks at the center of the slider.

---

### Property Descriptions

<span id="class_Slider_property_editable"></span>

[bool](class_bool.md#class_bool) **editable** = `true` [🔗](class_slider.md#class_Slider_property_editable)

- void **set_editable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editable** ( )

If `true`, the slider can be interacted with. If `false`, the value can be changed only by code.

---

<span id="class_Slider_property_scrollable"></span>

[bool](class_bool.md#class_bool) **scrollable** = `true` [🔗](class_slider.md#class_Slider_property_scrollable)

- void **set_scrollable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_scrollable** ( )

If `true`, the value can be changed using the mouse wheel.

---

<span id="class_Slider_property_tick_count"></span>

[int](class_int.md#class_int) **tick_count** = `0` [🔗](class_slider.md#class_Slider_property_tick_count)

- void **set_ticks** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_ticks** ( )

Number of ticks displayed on the slider, including border ticks. Ticks are uniformly-distributed value markers.

---

<span id="class_Slider_property_ticks_on_borders"></span>

[bool](class_bool.md#class_bool) **ticks_on_borders** = `false` [🔗](class_slider.md#class_Slider_property_ticks_on_borders)

- void **set_ticks_on_borders** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_ticks_on_borders** ( )

If `true`, the slider will display ticks for minimum and maximum values.

---

<span id="class_Slider_property_ticks_position"></span>

[TickPosition](class_slider.md#enum_Slider_TickPosition) **ticks_position** = `0` [🔗](class_slider.md#class_Slider_property_ticks_position)

- void **set_ticks_position** ( value: [TickPosition](class_slider.md#enum_Slider_TickPosition) )
- [TickPosition](class_slider.md#enum_Slider_TickPosition) **get_ticks_position** ( )

Sets the position of the ticks. See [TickPosition](class_slider.md#enum_Slider_TickPosition) for details.

---

### Theme Property Descriptions

<span id="class_Slider_theme_constant_center_grabber"></span>

[int](class_int.md#class_int) **center_grabber** = `0` [🔗](class_slider.md#class_Slider_theme_constant_center_grabber)

Boolean constant. If `1`, the grabber texture size will be ignored and it will fit within slider's bounds based only on its center position.

---

<span id="class_Slider_theme_constant_grabber_offset"></span>

[int](class_int.md#class_int) **grabber_offset** = `0` [🔗](class_slider.md#class_Slider_theme_constant_grabber_offset)

Vertical or horizontal offset of the grabber.

---

<span id="class_Slider_theme_constant_tick_offset"></span>

[int](class_int.md#class_int) **tick_offset** = `0` [🔗](class_slider.md#class_Slider_theme_constant_tick_offset)

Vertical or horizontal offset of the ticks. The offset is reversed for top or left ticks.

---

<span id="class_Slider_theme_icon_grabber"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **grabber** [🔗](class_slider.md#class_Slider_theme_icon_grabber)

The texture for the grabber (the draggable element).

---

<span id="class_Slider_theme_icon_grabber_disabled"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **grabber_disabled** [🔗](class_slider.md#class_Slider_theme_icon_grabber_disabled)

The texture for the grabber when it's disabled.

---

<span id="class_Slider_theme_icon_grabber_highlight"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **grabber_highlight** [🔗](class_slider.md#class_Slider_theme_icon_grabber_highlight)

The texture for the grabber when it's focused.

---

<span id="class_Slider_theme_icon_tick"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **tick** [🔗](class_slider.md#class_Slider_theme_icon_tick)

The texture for the ticks, visible when [tick_count](class_slider.md#class_Slider_property_tick_count) is greater than 0.

---

<span id="class_Slider_theme_style_grabber_area"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **grabber_area** [🔗](class_slider.md#class_Slider_theme_style_grabber_area)

The background of the area to the left or bottom of the grabber.

---

<span id="class_Slider_theme_style_grabber_area_highlight"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **grabber_area_highlight** [🔗](class_slider.md#class_Slider_theme_style_grabber_area_highlight)

The background of the area to the left or bottom of the grabber that displays when it's being hovered or focused.

---

<span id="class_Slider_theme_style_slider"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **slider** [🔗](class_slider.md#class_Slider_theme_style_slider)

The background for the whole slider. Affects the height or width of the [grabber_area](class_slider.md#class_Slider_theme_style_grabber_area).
