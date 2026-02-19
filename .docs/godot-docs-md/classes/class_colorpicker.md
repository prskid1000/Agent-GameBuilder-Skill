<span id="class_ColorPicker"></span>

## ColorPicker

**Inherits:** [VBoxContainer](class_vboxcontainer.md#class_VBoxContainer) **<** [BoxContainer](class_boxcontainer.md#class_BoxContainer) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A widget that provides an interface for selecting or modifying a color.

### Description

A widget that provides an interface for selecting or modifying a color. It can optionally provide functionalities like a color sampler (eyedropper), color modes, and presets.

 **Note:** This control is the color picker widget itself. You can use a [ColorPickerButton](class_colorpickerbutton.md#class_ColorPickerButton) instead if you need a button that brings up a **ColorPicker** in a popup.

### Tutorials

- Tween Interpolation Demo

### Properties


| [bool](class_bool.md#class_bool) | [can_add_swatches](class_colorpicker.md#class_ColorPicker_property_can_add_swatches) | `true` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [color](class_colorpicker.md#class_ColorPicker_property_color) | `Color(1, 1, 1, 1)` |
| [ColorModeType](class_colorpicker.md#enum_ColorPicker_ColorModeType) | [color_mode](class_colorpicker.md#class_ColorPicker_property_color_mode) | `0` |
| [bool](class_bool.md#class_bool) | [color_modes_visible](class_colorpicker.md#class_ColorPicker_property_color_modes_visible) | `true` |
| [bool](class_bool.md#class_bool) | [deferred_mode](class_colorpicker.md#class_ColorPicker_property_deferred_mode) | `false` |
| [bool](class_bool.md#class_bool) | [edit_alpha](class_colorpicker.md#class_ColorPicker_property_edit_alpha) | `true` |
| [bool](class_bool.md#class_bool) | [edit_intensity](class_colorpicker.md#class_ColorPicker_property_edit_intensity) | `true` |
| [bool](class_bool.md#class_bool) | [hex_visible](class_colorpicker.md#class_ColorPicker_property_hex_visible) | `true` |
| [PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) | [picker_shape](class_colorpicker.md#class_ColorPicker_property_picker_shape) | `0` |
| [bool](class_bool.md#class_bool) | [presets_visible](class_colorpicker.md#class_ColorPicker_property_presets_visible) | `true` |
| [bool](class_bool.md#class_bool) | [sampler_visible](class_colorpicker.md#class_ColorPicker_property_sampler_visible) | `true` |
| [bool](class_bool.md#class_bool) | [sliders_visible](class_colorpicker.md#class_ColorPicker_property_sliders_visible) | `true` |

### Methods


| void | [add_preset](class_colorpicker.md#class_ColorPicker_method_add_preset) ( color: [Color](class_color.md#class_Color) ) |
| --- | --- |
| void | [add_recent_preset](class_colorpicker.md#class_ColorPicker_method_add_recent_preset) ( color: [Color](class_color.md#class_Color) ) |
| void | [erase_preset](class_colorpicker.md#class_ColorPicker_method_erase_preset) ( color: [Color](class_color.md#class_Color) ) |
| void | [erase_recent_preset](class_colorpicker.md#class_ColorPicker_method_erase_recent_preset) ( color: [Color](class_color.md#class_Color) ) |
| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [get_presets](class_colorpicker.md#class_ColorPicker_method_get_presets) ( ) const |
| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [get_recent_presets](class_colorpicker.md#class_ColorPicker_method_get_recent_presets) ( ) const |

### Theme Properties


| [Color](class_color.md#class_Color) | [focused_not_editing_cursor_color](class_colorpicker.md#class_ColorPicker_theme_color_focused_not_editing_cursor_color) | `Color(1, 1, 1, 0.275)` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [center_slider_grabbers](class_colorpicker.md#class_ColorPicker_theme_constant_center_slider_grabbers) | `1` |
| [int](class_int.md#class_int) | [h_width](class_colorpicker.md#class_ColorPicker_theme_constant_h_width) | `30` |
| [int](class_int.md#class_int) | [label_width](class_colorpicker.md#class_ColorPicker_theme_constant_label_width) | `10` |
| [int](class_int.md#class_int) | [margin](class_colorpicker.md#class_ColorPicker_theme_constant_margin) | `4` |
| [int](class_int.md#class_int) | [sv_height](class_colorpicker.md#class_ColorPicker_theme_constant_sv_height) | `256` |
| [int](class_int.md#class_int) | [sv_width](class_colorpicker.md#class_ColorPicker_theme_constant_sv_width) | `256` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [add_preset](class_colorpicker.md#class_ColorPicker_theme_icon_add_preset) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [bar_arrow](class_colorpicker.md#class_ColorPicker_theme_icon_bar_arrow) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [color_copy](class_colorpicker.md#class_ColorPicker_theme_icon_color_copy) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [color_hue](class_colorpicker.md#class_ColorPicker_theme_icon_color_hue) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [color_script](class_colorpicker.md#class_ColorPicker_theme_icon_color_script) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [expanded_arrow](class_colorpicker.md#class_ColorPicker_theme_icon_expanded_arrow) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [folded_arrow](class_colorpicker.md#class_ColorPicker_theme_icon_folded_arrow) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [menu_option](class_colorpicker.md#class_ColorPicker_theme_icon_menu_option) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [overbright_indicator](class_colorpicker.md#class_ColorPicker_theme_icon_overbright_indicator) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [picker_cursor](class_colorpicker.md#class_ColorPicker_theme_icon_picker_cursor) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [picker_cursor_bg](class_colorpicker.md#class_ColorPicker_theme_icon_picker_cursor_bg) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [sample_bg](class_colorpicker.md#class_ColorPicker_theme_icon_sample_bg) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [sample_revert](class_colorpicker.md#class_ColorPicker_theme_icon_sample_revert) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [screen_picker](class_colorpicker.md#class_ColorPicker_theme_icon_screen_picker) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [shape_circle](class_colorpicker.md#class_ColorPicker_theme_icon_shape_circle) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [shape_rect](class_colorpicker.md#class_ColorPicker_theme_icon_shape_rect) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [shape_rect_wheel](class_colorpicker.md#class_ColorPicker_theme_icon_shape_rect_wheel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [picker_focus_circle](class_colorpicker.md#class_ColorPicker_theme_style_picker_focus_circle) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [picker_focus_rectangle](class_colorpicker.md#class_ColorPicker_theme_style_picker_focus_rectangle) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [sample_focus](class_colorpicker.md#class_ColorPicker_theme_style_sample_focus) |

---

### Signals

<span id="class_ColorPicker_signal_color_changed"></span>

**color_changed** ( color: [Color](class_color.md#class_Color) ) [🔗](class_colorpicker.md#class_ColorPicker_signal_color_changed)

Emitted when the color is changed.

---

<span id="class_ColorPicker_signal_preset_added"></span>

**preset_added** ( color: [Color](class_color.md#class_Color) ) [🔗](class_colorpicker.md#class_ColorPicker_signal_preset_added)

Emitted when a preset is added.

---

<span id="class_ColorPicker_signal_preset_removed"></span>

**preset_removed** ( color: [Color](class_color.md#class_Color) ) [🔗](class_colorpicker.md#class_ColorPicker_signal_preset_removed)

Emitted when a preset is removed.

---

### Enumerations

<span id="enum_ColorPicker_ColorModeType"></span>

enum **ColorModeType**: [🔗](class_colorpicker.md#enum_ColorPicker_ColorModeType)

<span id="class_ColorPicker_constant_MODE_RGB"></span>

[ColorModeType](class_colorpicker.md#enum_ColorPicker_ColorModeType) **MODE_RGB** = `0`

Allows editing the color with Red/Green/Blue sliders in sRGB color space.

<span id="class_ColorPicker_constant_MODE_HSV"></span>

[ColorModeType](class_colorpicker.md#enum_ColorPicker_ColorModeType) **MODE_HSV** = `1`

Allows editing the color with Hue/Saturation/Value sliders.

<span id="class_ColorPicker_constant_MODE_RAW"></span>

[ColorModeType](class_colorpicker.md#enum_ColorPicker_ColorModeType) **MODE_RAW** = `2`

**Deprecated:** This is replaced by [MODE_LINEAR](class_colorpicker.md#class_ColorPicker_constant_MODE_LINEAR).

<span id="class_ColorPicker_constant_MODE_LINEAR"></span>

[ColorModeType](class_colorpicker.md#enum_ColorPicker_ColorModeType) **MODE_LINEAR** = `2`

Allows editing the color with Red/Green/Blue sliders in linear color space.

<span id="class_ColorPicker_constant_MODE_OKHSL"></span>

[ColorModeType](class_colorpicker.md#enum_ColorPicker_ColorModeType) **MODE_OKHSL** = `3`

Allows editing the color with Hue/Saturation/Lightness sliders.

OKHSL is a new color space similar to HSL but that better match perception by leveraging the Oklab color space which is designed to be simple to use, while doing a good job at predicting perceived lightness, chroma and hue.

 Okhsv and Okhsl color spaces

---

<span id="enum_ColorPicker_PickerShapeType"></span>

enum **PickerShapeType**: [🔗](class_colorpicker.md#enum_ColorPicker_PickerShapeType)

<span id="class_ColorPicker_constant_SHAPE_HSV_RECTANGLE"></span>

[PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) **SHAPE_HSV_RECTANGLE** = `0`

HSV Color Model rectangle color space.

<span id="class_ColorPicker_constant_SHAPE_HSV_WHEEL"></span>

[PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) **SHAPE_HSV_WHEEL** = `1`

HSV Color Model rectangle color space with a wheel.

<span id="class_ColorPicker_constant_SHAPE_VHS_CIRCLE"></span>

[PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) **SHAPE_VHS_CIRCLE** = `2`

HSV Color Model circle color space. Use Saturation as a radius.

<span id="class_ColorPicker_constant_SHAPE_OKHSL_CIRCLE"></span>

[PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) **SHAPE_OKHSL_CIRCLE** = `3`

HSL OK Color Model circle color space.

<span id="class_ColorPicker_constant_SHAPE_NONE"></span>

[PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) **SHAPE_NONE** = `4`

The color space shape and the shape select button are hidden. Can't be selected from the shapes popup.

<span id="class_ColorPicker_constant_SHAPE_OK_HS_RECTANGLE"></span>

[PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) **SHAPE_OK_HS_RECTANGLE** = `5`

OKHSL Color Model rectangle with constant lightness.

<span id="class_ColorPicker_constant_SHAPE_OK_HL_RECTANGLE"></span>

[PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) **SHAPE_OK_HL_RECTANGLE** = `6`

OKHSL Color Model rectangle with constant saturation.

---

### Property Descriptions

<span id="class_ColorPicker_property_can_add_swatches"></span>

[bool](class_bool.md#class_bool) **can_add_swatches** = `true` [🔗](class_colorpicker.md#class_ColorPicker_property_can_add_swatches)

- void **set_can_add_swatches** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **are_swatches_enabled** ( )

If `true`, it's possible to add presets under Swatches. If `false`, the button to add presets is disabled.

---

<span id="class_ColorPicker_property_color"></span>

[Color](class_color.md#class_Color) **color** = `Color(1, 1, 1, 1)` [🔗](class_colorpicker.md#class_ColorPicker_property_color)

- void **set_pick_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_pick_color** ( )

The currently selected color.

---

<span id="class_ColorPicker_property_color_mode"></span>

[ColorModeType](class_colorpicker.md#enum_ColorPicker_ColorModeType) **color_mode** = `0` [🔗](class_colorpicker.md#class_ColorPicker_property_color_mode)

- void **set_color_mode** ( value: [ColorModeType](class_colorpicker.md#enum_ColorPicker_ColorModeType) )
- [ColorModeType](class_colorpicker.md#enum_ColorPicker_ColorModeType) **get_color_mode** ( )

The currently selected color mode.

---

<span id="class_ColorPicker_property_color_modes_visible"></span>

[bool](class_bool.md#class_bool) **color_modes_visible** = `true` [🔗](class_colorpicker.md#class_ColorPicker_property_color_modes_visible)

- void **set_modes_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **are_modes_visible** ( )

If `true`, the color mode buttons are visible.

---

<span id="class_ColorPicker_property_deferred_mode"></span>

[bool](class_bool.md#class_bool) **deferred_mode** = `false` [🔗](class_colorpicker.md#class_ColorPicker_property_deferred_mode)

- void **set_deferred_mode** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_deferred_mode** ( )

If `true`, the color will apply only after the user releases the mouse button, otherwise it will apply immediately even in mouse motion event (which can cause performance issues).

---

<span id="class_ColorPicker_property_edit_alpha"></span>

[bool](class_bool.md#class_bool) **edit_alpha** = `true` [🔗](class_colorpicker.md#class_ColorPicker_property_edit_alpha)

- void **set_edit_alpha** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editing_alpha** ( )

If `true`, shows an alpha channel slider (opacity).

---

<span id="class_ColorPicker_property_edit_intensity"></span>

[bool](class_bool.md#class_bool) **edit_intensity** = `true` [🔗](class_colorpicker.md#class_ColorPicker_property_edit_intensity)

- void **set_edit_intensity** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editing_intensity** ( )

If `true`, shows an intensity slider. The intensity is applied as follows: convert the color to linear encoding, multiply it by `2 ** intensity`, and then convert it back to nonlinear sRGB encoding.

---

<span id="class_ColorPicker_property_hex_visible"></span>

[bool](class_bool.md#class_bool) **hex_visible** = `true` [🔗](class_colorpicker.md#class_ColorPicker_property_hex_visible)

- void **set_hex_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_hex_visible** ( )

If `true`, the hex color code input field is visible.

---

<span id="class_ColorPicker_property_picker_shape"></span>

[PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) **picker_shape** = `0` [🔗](class_colorpicker.md#class_ColorPicker_property_picker_shape)

- void **set_picker_shape** ( value: [PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) )
- [PickerShapeType](class_colorpicker.md#enum_ColorPicker_PickerShapeType) **get_picker_shape** ( )

The shape of the color space view.

---

<span id="class_ColorPicker_property_presets_visible"></span>

[bool](class_bool.md#class_bool) **presets_visible** = `true` [🔗](class_colorpicker.md#class_ColorPicker_property_presets_visible)

- void **set_presets_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **are_presets_visible** ( )

If `true`, the Swatches and Recent Colors presets are visible.

---

<span id="class_ColorPicker_property_sampler_visible"></span>

[bool](class_bool.md#class_bool) **sampler_visible** = `true` [🔗](class_colorpicker.md#class_ColorPicker_property_sampler_visible)

- void **set_sampler_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_sampler_visible** ( )

If `true`, the color sampler and color preview are visible.

---

<span id="class_ColorPicker_property_sliders_visible"></span>

[bool](class_bool.md#class_bool) **sliders_visible** = `true` [🔗](class_colorpicker.md#class_ColorPicker_property_sliders_visible)

- void **set_sliders_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **are_sliders_visible** ( )

If `true`, the color sliders are visible.

---

### Method Descriptions

<span id="class_ColorPicker_method_add_preset"></span>

void **add_preset** ( color: [Color](class_color.md#class_Color) ) [🔗](class_colorpicker.md#class_ColorPicker_method_add_preset)

Adds the given color to a list of color presets. The presets are displayed in the color picker and the user will be able to select them.

 **Note:** The presets list is only for *this* color picker.

---

<span id="class_ColorPicker_method_add_recent_preset"></span>

void **add_recent_preset** ( color: [Color](class_color.md#class_Color) ) [🔗](class_colorpicker.md#class_ColorPicker_method_add_recent_preset)

Adds the given color to a list of color recent presets so that it can be picked later. Recent presets are the colors that were picked recently, a new preset is automatically created and added to recent presets when you pick a new color.

 **Note:** The recent presets list is only for *this* color picker.

---

<span id="class_ColorPicker_method_erase_preset"></span>

void **erase_preset** ( color: [Color](class_color.md#class_Color) ) [🔗](class_colorpicker.md#class_ColorPicker_method_erase_preset)

Removes the given color from the list of color presets of this color picker.

---

<span id="class_ColorPicker_method_erase_recent_preset"></span>

void **erase_recent_preset** ( color: [Color](class_color.md#class_Color) ) [🔗](class_colorpicker.md#class_ColorPicker_method_erase_recent_preset)

Removes the given color from the list of color recent presets of this color picker.

---

<span id="class_ColorPicker_method_get_presets"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **get_presets** ( ) *const* [🔗](class_colorpicker.md#class_ColorPicker_method_get_presets)

Returns the list of colors in the presets of the color picker.

---

<span id="class_ColorPicker_method_get_recent_presets"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **get_recent_presets** ( ) *const* [🔗](class_colorpicker.md#class_ColorPicker_method_get_recent_presets)

Returns the list of colors in the recent presets of the color picker.

---

### Theme Property Descriptions

<span id="class_ColorPicker_theme_color_focused_not_editing_cursor_color"></span>

[Color](class_color.md#class_Color) **focused_not_editing_cursor_color** = `Color(1, 1, 1, 0.275)` [🔗](class_colorpicker.md#class_ColorPicker_theme_color_focused_not_editing_cursor_color)

Color of rectangle or circle drawn when a picker shape part is focused but not editable via keyboard or joypad. Displayed *over* the picker shape, so a partially transparent color should be used to ensure the picker shape remains visible.

---

<span id="class_ColorPicker_theme_constant_center_slider_grabbers"></span>

[int](class_int.md#class_int) **center_slider_grabbers** = `1` [🔗](class_colorpicker.md#class_ColorPicker_theme_constant_center_slider_grabbers)

Overrides the [Slider.center_grabber](class_slider.md#class_Slider_theme_constant_center_grabber) theme property of the sliders.

---

<span id="class_ColorPicker_theme_constant_h_width"></span>

[int](class_int.md#class_int) **h_width** = `30` [🔗](class_colorpicker.md#class_ColorPicker_theme_constant_h_width)

The width of the hue selection slider.

---

<span id="class_ColorPicker_theme_constant_label_width"></span>

[int](class_int.md#class_int) **label_width** = `10` [🔗](class_colorpicker.md#class_ColorPicker_theme_constant_label_width)

The minimum width of the color labels next to sliders.

---

<span id="class_ColorPicker_theme_constant_margin"></span>

[int](class_int.md#class_int) **margin** = `4` [🔗](class_colorpicker.md#class_ColorPicker_theme_constant_margin)

The margin around the **ColorPicker**.

---

<span id="class_ColorPicker_theme_constant_sv_height"></span>

[int](class_int.md#class_int) **sv_height** = `256` [🔗](class_colorpicker.md#class_ColorPicker_theme_constant_sv_height)

The height of the saturation-value selection box.

---

<span id="class_ColorPicker_theme_constant_sv_width"></span>

[int](class_int.md#class_int) **sv_width** = `256` [🔗](class_colorpicker.md#class_ColorPicker_theme_constant_sv_width)

The width of the saturation-value selection box.

---

<span id="class_ColorPicker_theme_icon_add_preset"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **add_preset** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_add_preset)

The icon for the "Add Preset" button.

---

<span id="class_ColorPicker_theme_icon_bar_arrow"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **bar_arrow** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_bar_arrow)

The texture for the arrow grabber.

---

<span id="class_ColorPicker_theme_icon_color_copy"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **color_copy** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_color_copy)

The icon for the button that copies the color in text format to the clipboard.

---

<span id="class_ColorPicker_theme_icon_color_hue"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **color_hue** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_color_hue)

Custom texture for the hue selection slider on the right.

---

<span id="class_ColorPicker_theme_icon_color_script"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **color_script** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_color_script)

The icon for the button that switches color text to hexadecimal.

---

<span id="class_ColorPicker_theme_icon_expanded_arrow"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **expanded_arrow** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_expanded_arrow)

The icon for color preset drop down menu when expanded.

---

<span id="class_ColorPicker_theme_icon_folded_arrow"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **folded_arrow** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_folded_arrow)

The icon for color preset drop down menu when folded.

---

<span id="class_ColorPicker_theme_icon_menu_option"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **menu_option** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_menu_option)

The icon for color preset option menu.

---

<span id="class_ColorPicker_theme_icon_overbright_indicator"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **overbright_indicator** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_overbright_indicator)

The indicator used to signalize that the color value is outside the 0-1 range.

---

<span id="class_ColorPicker_theme_icon_picker_cursor"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **picker_cursor** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_picker_cursor)

The image displayed over the color box/circle (depending on the [picker_shape](class_colorpicker.md#class_ColorPicker_property_picker_shape)), marking the currently selected color.

---

<span id="class_ColorPicker_theme_icon_picker_cursor_bg"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **picker_cursor_bg** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_picker_cursor_bg)

The fill image displayed behind the picker cursor.

---

<span id="class_ColorPicker_theme_icon_sample_bg"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **sample_bg** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_sample_bg)

Background panel for the color preview box (visible when the color is translucent).

---

<span id="class_ColorPicker_theme_icon_sample_revert"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **sample_revert** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_sample_revert)

The icon for the revert button (visible on the middle of the "old" color when it differs from the currently selected color). This icon is modulated with a dark color if the "old" color is bright enough, so the icon should be bright to ensure visibility in both scenarios.

---

<span id="class_ColorPicker_theme_icon_screen_picker"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **screen_picker** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_screen_picker)

The icon for the screen color picker button.

---

<span id="class_ColorPicker_theme_icon_shape_circle"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **shape_circle** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_shape_circle)

The icon for circular picker shapes.

---

<span id="class_ColorPicker_theme_icon_shape_rect"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **shape_rect** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_shape_rect)

The icon for rectangular picker shapes.

---

<span id="class_ColorPicker_theme_icon_shape_rect_wheel"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **shape_rect_wheel** [🔗](class_colorpicker.md#class_ColorPicker_theme_icon_shape_rect_wheel)

The icon for rectangular wheel picker shapes.

---

<span id="class_ColorPicker_theme_style_picker_focus_circle"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **picker_focus_circle** [🔗](class_colorpicker.md#class_ColorPicker_theme_style_picker_focus_circle)

The [StyleBox](class_stylebox.md#class_StyleBox) used when the circle-shaped part of the picker is focused. Displayed *over* the picker shape, so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the picker shape remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_ColorPicker_theme_style_picker_focus_rectangle"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **picker_focus_rectangle** [🔗](class_colorpicker.md#class_ColorPicker_theme_style_picker_focus_rectangle)

The [StyleBox](class_stylebox.md#class_StyleBox) used when the rectangle-shaped part of the picker is focused. Displayed *over* the picker shape, so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the picker shape remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_ColorPicker_theme_style_sample_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **sample_focus** [🔗](class_colorpicker.md#class_ColorPicker_theme_style_sample_focus)

The [StyleBox](class_stylebox.md#class_StyleBox) used for the old color sample part when it is focused. Displayed *over* the sample, so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the picker shape remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.
