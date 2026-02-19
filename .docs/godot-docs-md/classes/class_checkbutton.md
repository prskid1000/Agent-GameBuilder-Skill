.. meta::
	:keywords: switch, toggle

<span id="class_CheckButton"></span>

## CheckButton

**Inherits:** [Button](class_button.md#class_Button) **<** [BaseButton](class_basebutton.md#class_BaseButton) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A button that represents a binary choice.

### Description

**CheckButton** is a toggle button displayed as a check field. It's similar to [CheckBox](class_checkbox.md#class_CheckBox) in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use **CheckButton** when toggling it has an **immediate** effect on something. For example, it can be used when pressing it shows or hides advanced settings, without asking the user to confirm this action.

See also [BaseButton](class_basebutton.md#class_BaseButton) which contains common properties and methods associated with this node.

### Properties


| HorizontalAlignment | alignment | `0` (overrides [Button](class_button.md#class_Button_property_alignment)) |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | toggle_mode | `true` (overrides [BaseButton](class_basebutton.md#class_BaseButton_property_toggle_mode)) |

### Theme Properties


| [Color](class_color.md#class_Color) | [button_checked_color](class_checkbutton.md#class_CheckButton_theme_color_button_checked_color) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [button_unchecked_color](class_checkbutton.md#class_CheckButton_theme_color_button_unchecked_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [check_v_offset](class_checkbutton.md#class_CheckButton_theme_constant_check_v_offset) | `0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [checked](class_checkbutton.md#class_CheckButton_theme_icon_checked) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [checked_disabled](class_checkbutton.md#class_CheckButton_theme_icon_checked_disabled) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [checked_disabled_mirrored](class_checkbutton.md#class_CheckButton_theme_icon_checked_disabled_mirrored) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [checked_mirrored](class_checkbutton.md#class_CheckButton_theme_icon_checked_mirrored) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [unchecked](class_checkbutton.md#class_CheckButton_theme_icon_unchecked) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [unchecked_disabled](class_checkbutton.md#class_CheckButton_theme_icon_unchecked_disabled) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [unchecked_disabled_mirrored](class_checkbutton.md#class_CheckButton_theme_icon_unchecked_disabled_mirrored) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [unchecked_mirrored](class_checkbutton.md#class_CheckButton_theme_icon_unchecked_mirrored) |

---

### Theme Property Descriptions

<span id="class_CheckButton_theme_color_button_checked_color"></span>

[Color](class_color.md#class_Color) **button_checked_color** = `Color(1, 1, 1, 1)` [🔗](class_checkbutton.md#class_CheckButton_theme_color_button_checked_color)

The color of the checked icon when the checkbox is pressed.

---

<span id="class_CheckButton_theme_color_button_unchecked_color"></span>

[Color](class_color.md#class_Color) **button_unchecked_color** = `Color(1, 1, 1, 1)` [🔗](class_checkbutton.md#class_CheckButton_theme_color_button_unchecked_color)

The color of the unchecked icon when the checkbox is not pressed.

---

<span id="class_CheckButton_theme_constant_check_v_offset"></span>

[int](class_int.md#class_int) **check_v_offset** = `0` [🔗](class_checkbutton.md#class_CheckButton_theme_constant_check_v_offset)

The vertical offset used when rendering the toggle icons (in pixels).

---

<span id="class_CheckButton_theme_icon_checked"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **checked** [🔗](class_checkbutton.md#class_CheckButton_theme_icon_checked)

The icon to display when the **CheckButton** is checked (for left-to-right layouts).

---

<span id="class_CheckButton_theme_icon_checked_disabled"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **checked_disabled** [🔗](class_checkbutton.md#class_CheckButton_theme_icon_checked_disabled)

The icon to display when the **CheckButton** is checked and disabled (for left-to-right layouts).

---

<span id="class_CheckButton_theme_icon_checked_disabled_mirrored"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **checked_disabled_mirrored** [🔗](class_checkbutton.md#class_CheckButton_theme_icon_checked_disabled_mirrored)

The icon to display when the **CheckButton** is checked and disabled (for right-to-left layouts).

---

<span id="class_CheckButton_theme_icon_checked_mirrored"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **checked_mirrored** [🔗](class_checkbutton.md#class_CheckButton_theme_icon_checked_mirrored)

The icon to display when the **CheckButton** is checked (for right-to-left layouts).

---

<span id="class_CheckButton_theme_icon_unchecked"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **unchecked** [🔗](class_checkbutton.md#class_CheckButton_theme_icon_unchecked)

The icon to display when the **CheckButton** is unchecked (for left-to-right layouts).

---

<span id="class_CheckButton_theme_icon_unchecked_disabled"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **unchecked_disabled** [🔗](class_checkbutton.md#class_CheckButton_theme_icon_unchecked_disabled)

The icon to display when the **CheckButton** is unchecked and disabled (for left-to-right layouts).

---

<span id="class_CheckButton_theme_icon_unchecked_disabled_mirrored"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **unchecked_disabled_mirrored** [🔗](class_checkbutton.md#class_CheckButton_theme_icon_unchecked_disabled_mirrored)

The icon to display when the **CheckButton** is unchecked and disabled (for right-to-left layouts).

---

<span id="class_CheckButton_theme_icon_unchecked_mirrored"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **unchecked_mirrored** [🔗](class_checkbutton.md#class_CheckButton_theme_icon_unchecked_mirrored)

The icon to display when the **CheckButton** is unchecked (for right-to-left layouts).
