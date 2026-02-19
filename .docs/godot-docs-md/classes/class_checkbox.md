<span id="class_CheckBox"></span>

## CheckBox

**Inherits:** [Button](class_button.md#class_Button) **<** [BaseButton](class_basebutton.md#class_BaseButton) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A button that represents a binary choice.

### Description

**CheckBox** allows the user to choose one of only two possible options. It's similar to [CheckButton](class_checkbutton.md#class_CheckButton) in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use **CheckBox** when toggling it has **no** immediate effect on something. For example, it could be used when toggling it will only do something once a confirmation button is pressed.

See also [BaseButton](class_basebutton.md#class_BaseButton) which contains common properties and methods associated with this node.

When [BaseButton.button_group](class_basebutton.md#class_BaseButton_property_button_group) specifies a [ButtonGroup](class_buttongroup.md#class_ButtonGroup), **CheckBox** changes its appearance to that of a radio button and uses the various `radio_*` theme properties.

### Properties


| HorizontalAlignment | alignment | `0` (overrides [Button](class_button.md#class_Button_property_alignment)) |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class_BaseButton_property_toggle_mode)) |

### Theme Properties


| [Color](class_color.md#class_Color) | [checkbox_checked_color](class_checkbox.md#class_CheckBox_theme_color_checkbox_checked_color) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [checkbox_unchecked_color](class_checkbox.md#class_CheckBox_theme_color_checkbox_unchecked_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [check_v_offset](class_checkbox.md#class_CheckBox_theme_constant_check_v_offset) | `0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [checked](class_checkbox.md#class_CheckBox_theme_icon_checked) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [checked_disabled](class_checkbox.md#class_CheckBox_theme_icon_checked_disabled) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [radio_checked](class_checkbox.md#class_CheckBox_theme_icon_radio_checked) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [radio_checked_disabled](class_checkbox.md#class_CheckBox_theme_icon_radio_checked_disabled) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [radio_unchecked](class_checkbox.md#class_CheckBox_theme_icon_radio_unchecked) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [radio_unchecked_disabled](class_checkbox.md#class_CheckBox_theme_icon_radio_unchecked_disabled) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [unchecked](class_checkbox.md#class_CheckBox_theme_icon_unchecked) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [unchecked_disabled](class_checkbox.md#class_CheckBox_theme_icon_unchecked_disabled) |

---

### Theme Property Descriptions

<span id="class_CheckBox_theme_color_checkbox_checked_color"></span>

[Color](class_color.md#class_Color) **checkbox_checked_color** = `Color(1, 1, 1, 1)` [🔗](class_checkbox.md#class_CheckBox_theme_color_checkbox_checked_color)

The color of the checked icon when the checkbox is pressed.

---

<span id="class_CheckBox_theme_color_checkbox_unchecked_color"></span>

[Color](class_color.md#class_Color) **checkbox_unchecked_color** = `Color(1, 1, 1, 1)` [🔗](class_checkbox.md#class_CheckBox_theme_color_checkbox_unchecked_color)

The color of the unchecked icon when the checkbox is not pressed.

---

<span id="class_CheckBox_theme_constant_check_v_offset"></span>

[int](class_int.md#class_int) **check_v_offset** = `0` [🔗](class_checkbox.md#class_CheckBox_theme_constant_check_v_offset)

The vertical offset used when rendering the check icons (in pixels).

---

<span id="class_CheckBox_theme_icon_checked"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **checked** [🔗](class_checkbox.md#class_CheckBox_theme_icon_checked)

The check icon to display when the **CheckBox** is checked.

---

<span id="class_CheckBox_theme_icon_checked_disabled"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **checked_disabled** [🔗](class_checkbox.md#class_CheckBox_theme_icon_checked_disabled)

The check icon to display when the **CheckBox** is checked and is disabled.

---

<span id="class_CheckBox_theme_icon_radio_checked"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **radio_checked** [🔗](class_checkbox.md#class_CheckBox_theme_icon_radio_checked)

The check icon to display when the **CheckBox** is configured as a radio button and is checked.

---

<span id="class_CheckBox_theme_icon_radio_checked_disabled"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **radio_checked_disabled** [🔗](class_checkbox.md#class_CheckBox_theme_icon_radio_checked_disabled)

The check icon to display when the **CheckBox** is configured as a radio button, is disabled, and is unchecked.

---

<span id="class_CheckBox_theme_icon_radio_unchecked"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **radio_unchecked** [🔗](class_checkbox.md#class_CheckBox_theme_icon_radio_unchecked)

The check icon to display when the **CheckBox** is configured as a radio button and is unchecked.

---

<span id="class_CheckBox_theme_icon_radio_unchecked_disabled"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **radio_unchecked_disabled** [🔗](class_checkbox.md#class_CheckBox_theme_icon_radio_unchecked_disabled)

The check icon to display when the **CheckBox** is configured as a radio button, is disabled, and is unchecked.

---

<span id="class_CheckBox_theme_icon_unchecked"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **unchecked** [🔗](class_checkbox.md#class_CheckBox_theme_icon_unchecked)

The check icon to display when the **CheckBox** is unchecked.

---

<span id="class_CheckBox_theme_icon_unchecked_disabled"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **unchecked_disabled** [🔗](class_checkbox.md#class_CheckBox_theme_icon_unchecked_disabled)

The check icon to display when the **CheckBox** is unchecked and is disabled.
