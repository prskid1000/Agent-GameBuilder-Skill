<span id="class_ColorPickerButton"></span>

## ColorPickerButton

**Inherits:** [Button](class_button.md#class_Button) **<** [BaseButton](class_basebutton.md#class_BaseButton) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A button that brings up a [ColorPicker](class_colorpicker.md#class_ColorPicker) when pressed.

### Description

Encapsulates a [ColorPicker](class_colorpicker.md#class_ColorPicker), making it accessible by pressing a button. Pressing the button will toggle the [ColorPicker](class_colorpicker.md#class_ColorPicker)'s visibility.

See also [BaseButton](class_basebutton.md#class_BaseButton) which contains common properties and methods associated with this node.

 **Note:** By default, the button may not be wide enough for the color preview swatch to be visible. Make sure to set [Control.custom_minimum_size](class_control.md#class_Control_property_custom_minimum_size) to a big enough value to give the button enough space.

### Tutorials

- 2D GD Paint Demo

- GUI Drag And Drop Demo

### Properties


| [Color](class_color.md#class_Color) | [color](class_colorpickerbutton.md#class_ColorPickerButton_property_color) | `Color(0, 0, 0, 1)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [edit_alpha](class_colorpickerbutton.md#class_ColorPickerButton_property_edit_alpha) | `true` |
| [bool](class_bool.md#class_bool) | [edit_intensity](class_colorpickerbutton.md#class_ColorPickerButton_property_edit_intensity) | `true` |
| [bool](class_bool.md#class_bool) | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class_BaseButton_property_toggle_mode)) |

### Methods


| [ColorPicker](class_colorpicker.md#class_ColorPicker) | [get_picker](class_colorpickerbutton.md#class_ColorPickerButton_method_get_picker) ( ) |
| --- | --- |
| [PopupPanel](class_popuppanel.md#class_PopupPanel) | [get_popup](class_colorpickerbutton.md#class_ColorPickerButton_method_get_popup) ( ) |

### Theme Properties


| [Texture2D](class_texture2d.md#class_Texture2D) | [bg](class_colorpickerbutton.md#class_ColorPickerButton_theme_icon_bg) |
| --- | --- |

---

### Signals

<span id="class_ColorPickerButton_signal_color_changed"></span>

**color_changed** ( color: [Color](class_color.md#class_Color) ) [🔗](class_colorpickerbutton.md#class_ColorPickerButton_signal_color_changed)

Emitted when the color changes.

---

<span id="class_ColorPickerButton_signal_picker_created"></span>

**picker_created** ( ) [🔗](class_colorpickerbutton.md#class_ColorPickerButton_signal_picker_created)

Emitted when the [ColorPicker](class_colorpicker.md#class_ColorPicker) is created (the button is pressed for the first time).

---

<span id="class_ColorPickerButton_signal_popup_closed"></span>

**popup_closed** ( ) [🔗](class_colorpickerbutton.md#class_ColorPickerButton_signal_popup_closed)

Emitted when the [ColorPicker](class_colorpicker.md#class_ColorPicker) is closed.

---

### Property Descriptions

<span id="class_ColorPickerButton_property_color"></span>

[Color](class_color.md#class_Color) **color** = `Color(0, 0, 0, 1)` [🔗](class_colorpickerbutton.md#class_ColorPickerButton_property_color)

- void **set_pick_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_pick_color** ( )

The currently selected color.

---

<span id="class_ColorPickerButton_property_edit_alpha"></span>

[bool](class_bool.md#class_bool) **edit_alpha** = `true` [🔗](class_colorpickerbutton.md#class_ColorPickerButton_property_edit_alpha)

- void **set_edit_alpha** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editing_alpha** ( )

If `true`, the alpha channel in the displayed [ColorPicker](class_colorpicker.md#class_ColorPicker) will be visible.

---

<span id="class_ColorPickerButton_property_edit_intensity"></span>

[bool](class_bool.md#class_bool) **edit_intensity** = `true` [🔗](class_colorpickerbutton.md#class_ColorPickerButton_property_edit_intensity)

- void **set_edit_intensity** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editing_intensity** ( )

If `true`, the intensity slider in the displayed [ColorPicker](class_colorpicker.md#class_ColorPicker) will be visible.

---

### Method Descriptions

<span id="class_ColorPickerButton_method_get_picker"></span>

[ColorPicker](class_colorpicker.md#class_ColorPicker) **get_picker** ( ) [🔗](class_colorpickerbutton.md#class_ColorPickerButton_method_get_picker)

Returns the [ColorPicker](class_colorpicker.md#class_ColorPicker) that this node toggles.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.

---

<span id="class_ColorPickerButton_method_get_popup"></span>

[PopupPanel](class_popuppanel.md#class_PopupPanel) **get_popup** ( ) [🔗](class_colorpickerbutton.md#class_ColorPickerButton_method_get_popup)

Returns the control's [PopupPanel](class_popuppanel.md#class_PopupPanel) which allows you to connect to popup signals. This allows you to handle events when the ColorPicker is shown or hidden.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class_Window_property_visible) property.

---

### Theme Property Descriptions

<span id="class_ColorPickerButton_theme_icon_bg"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **bg** [🔗](class_colorpickerbutton.md#class_ColorPickerButton_theme_icon_bg)

The background of the color preview rect on the button.
