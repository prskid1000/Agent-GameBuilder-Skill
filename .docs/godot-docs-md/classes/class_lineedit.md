.. meta::
	:keywords: text, input

<span id="class_LineEdit"></span>

## LineEdit

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

An input field for single-line text.

### Description

**LineEdit** provides an input field for editing a single line of text.

- When the **LineEdit** control is focused using the keyboard arrow keys, it will only gain focus and not enter edit mode.

- To enter edit mode, click on the control with the mouse, see also [keep_editing_on_text_submit](class_lineedit.md#class_LineEdit_property_keep_editing_on_text_submit).

- To exit edit mode, press `ui_text_submit` or `ui_cancel` (by default :kbd:`Escape`) actions.

- Check [edit()](class_lineedit.md#class_LineEdit_method_edit), [unedit()](class_lineedit.md#class_LineEdit_method_unedit), [is_editing()](class_lineedit.md#class_LineEdit_method_is_editing), and [editing_toggled](class_lineedit.md#class_LineEdit_signal_editing_toggled) for more information.

While entering text, it is possible to insert special characters using Unicode, OEM or Windows alt codes:

- To enter Unicode codepoints, hold :kbd:`Alt` and type the codepoint on the numpad. For example, to enter the character `á` (U+00E1), hold :kbd:`Alt` and type :kbd:`+E1` on the numpad (the leading zeroes can be omitted).

- To enter OEM codepoints, hold :kbd:`Alt` and type the code on the numpad. For example, to enter the character `á` (OEM 160), hold :kbd:`Alt` and type `160` on the numpad.

- To enter Windows codepoints, hold :kbd:`Alt` and type the code on the numpad. For example, to enter the character `á` (Windows 0225), hold :kbd:`Alt` and type :kbd:`0`, :kbd:`2`, :kbd:`2`, :kbd:`5` on the numpad. The leading zero here must **not** be omitted, as this is how Windows codepoints are distinguished from OEM codepoints.

 **Important:**

- Focusing the **LineEdit** with `ui_focus_next` (by default :kbd:`Tab`) or `ui_focus_prev` (by default :kbd:`Shift + Tab`) or [Control.grab_focus()](class_control.md#class_Control_method_grab_focus) still enters edit mode (for compatibility).

 **LineEdit** features many built-in shortcuts that are always available (:kbd:`Ctrl` here maps to :kbd:`Cmd` on macOS):

- :kbd:`Ctrl + C`: Copy

- :kbd:`Ctrl + X`: Cut

- :kbd:`Ctrl + V` or :kbd:`Ctrl + Y`: Paste/"yank"

- :kbd:`Ctrl + Z`: Undo

- :kbd:`Ctrl + ~`: Swap input direction.

- :kbd:`Ctrl + Shift + Z`: Redo

- :kbd:`Ctrl + U`: Delete text from the caret position to the beginning of the line

- :kbd:`Ctrl + K`: Delete text from the caret position to the end of the line

- :kbd:`Ctrl + A`: Select all text

- :kbd:`Up Arrow`/:kbd:`Down Arrow`: Move the caret to the beginning/end of the line

On macOS, some extra keyboard shortcuts are available:

- :kbd:`Cmd + F`: Same as :kbd:`Right Arrow`, move the caret one character right

- :kbd:`Cmd + B`: Same as :kbd:`Left Arrow`, move the caret one character left

- :kbd:`Cmd + P`: Same as :kbd:`Up Arrow`, move the caret to the previous line

- :kbd:`Cmd + N`: Same as :kbd:`Down Arrow`, move the caret to the next line

- :kbd:`Cmd + D`: Same as :kbd:`Delete`, delete the character on the right side of caret

- :kbd:`Cmd + H`: Same as :kbd:`Backspace`, delete the character on the left side of the caret

- :kbd:`Cmd + A`: Same as :kbd:`Home`, move the caret to the beginning of the line

- :kbd:`Cmd + E`: Same as :kbd:`End`, move the caret to the end of the line

- :kbd:`Cmd + Left Arrow`: Same as :kbd:`Home`, move the caret to the beginning of the line

- :kbd:`Cmd + Right Arrow`: Same as :kbd:`End`, move the caret to the end of the line

 **Note:** Caret movement shortcuts listed above are not affected by [shortcut_keys_enabled](class_lineedit.md#class_LineEdit_property_shortcut_keys_enabled).

### Properties


| HorizontalAlignment | [alignment](class_lineedit.md#class_LineEdit_property_alignment) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [backspace_deletes_composite_character_enabled](class_lineedit.md#class_LineEdit_property_backspace_deletes_composite_character_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [caret_blink](class_lineedit.md#class_LineEdit_property_caret_blink) | `false` |
| [float](class_float.md#class_float) | [caret_blink_interval](class_lineedit.md#class_LineEdit_property_caret_blink_interval) | `0.65` |
| [int](class_int.md#class_int) | [caret_column](class_lineedit.md#class_LineEdit_property_caret_column) | `0` |
| [bool](class_bool.md#class_bool) | [caret_force_displayed](class_lineedit.md#class_LineEdit_property_caret_force_displayed) | `false` |
| [bool](class_bool.md#class_bool) | [caret_mid_grapheme](class_lineedit.md#class_LineEdit_property_caret_mid_grapheme) | `false` |
| [bool](class_bool.md#class_bool) | [clear_button_enabled](class_lineedit.md#class_LineEdit_property_clear_button_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [context_menu_enabled](class_lineedit.md#class_LineEdit_property_context_menu_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [deselect_on_focus_loss_enabled](class_lineedit.md#class_LineEdit_property_deselect_on_focus_loss_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [drag_and_drop_selection_enabled](class_lineedit.md#class_LineEdit_property_drag_and_drop_selection_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [draw_control_chars](class_lineedit.md#class_LineEdit_property_draw_control_chars) | `false` |
| [bool](class_bool.md#class_bool) | [editable](class_lineedit.md#class_LineEdit_property_editable) | `true` |
| [bool](class_bool.md#class_bool) | [emoji_menu_enabled](class_lineedit.md#class_LineEdit_property_emoji_menu_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [expand_to_text_length](class_lineedit.md#class_LineEdit_property_expand_to_text_length) | `false` |
| [bool](class_bool.md#class_bool) | [flat](class_lineedit.md#class_LineEdit_property_flat) | `false` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `2` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [ExpandMode](class_lineedit.md#enum_LineEdit_ExpandMode) | [icon_expand_mode](class_lineedit.md#class_LineEdit_property_icon_expand_mode) | `0` |
| [bool](class_bool.md#class_bool) | [keep_editing_on_text_submit](class_lineedit.md#class_LineEdit_property_keep_editing_on_text_submit) | `false` |
| [String](class_string.md#class_String) | [language](class_lineedit.md#class_LineEdit_property_language) | `""` |
| [int](class_int.md#class_int) | [max_length](class_lineedit.md#class_LineEdit_property_max_length) | `0` |
| [bool](class_bool.md#class_bool) | [middle_mouse_paste_enabled](class_lineedit.md#class_LineEdit_property_middle_mouse_paste_enabled) | `true` |
| [CursorShape](class_control.md#enum_Control_CursorShape) | mouse_default_cursor_shape | `1` (overrides [Control](class_control.md#class_Control_property_mouse_default_cursor_shape)) |
| [String](class_string.md#class_String) | [placeholder_text](class_lineedit.md#class_LineEdit_property_placeholder_text) | `""` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [right_icon](class_lineedit.md#class_LineEdit_property_right_icon) |
| [float](class_float.md#class_float) | [right_icon_scale](class_lineedit.md#class_LineEdit_property_right_icon_scale) | `1.0` |
| [bool](class_bool.md#class_bool) | [secret](class_lineedit.md#class_LineEdit_property_secret) | `false` |
| [String](class_string.md#class_String) | [secret_character](class_lineedit.md#class_LineEdit_property_secret_character) | `"•"` |
| [bool](class_bool.md#class_bool) | [select_all_on_focus](class_lineedit.md#class_LineEdit_property_select_all_on_focus) | `false` |
| [bool](class_bool.md#class_bool) | [selecting_enabled](class_lineedit.md#class_LineEdit_property_selecting_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [shortcut_keys_enabled](class_lineedit.md#class_LineEdit_property_shortcut_keys_enabled) | `true` |
| [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) | [structured_text_bidi_override](class_lineedit.md#class_LineEdit_property_structured_text_bidi_override) | `0` |
| [Array](class_array.md#class_Array) | [structured_text_bidi_override_options](class_lineedit.md#class_LineEdit_property_structured_text_bidi_override_options) | `[]` |
| [String](class_string.md#class_String) | [text](class_lineedit.md#class_LineEdit_property_text) | `""` |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [text_direction](class_lineedit.md#class_LineEdit_property_text_direction) | `0` |
| [bool](class_bool.md#class_bool) | [virtual_keyboard_enabled](class_lineedit.md#class_LineEdit_property_virtual_keyboard_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [virtual_keyboard_show_on_focus](class_lineedit.md#class_LineEdit_property_virtual_keyboard_show_on_focus) | `true` |
| [VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) | [virtual_keyboard_type](class_lineedit.md#class_LineEdit_property_virtual_keyboard_type) | `0` |

### Methods


| void | [apply_ime](class_lineedit.md#class_LineEdit_method_apply_ime) ( ) |
| --- | --- |
| void | [cancel_ime](class_lineedit.md#class_LineEdit_method_cancel_ime) ( ) |
| void | [clear](class_lineedit.md#class_LineEdit_method_clear) ( ) |
| void | [delete_char_at_caret](class_lineedit.md#class_LineEdit_method_delete_char_at_caret) ( ) |
| void | [delete_text](class_lineedit.md#class_LineEdit_method_delete_text) ( from_column: [int](class_int.md#class_int), to_column: [int](class_int.md#class_int) ) |
| void | [deselect](class_lineedit.md#class_LineEdit_method_deselect) ( ) |
| void | [edit](class_lineedit.md#class_LineEdit_method_edit) ( hide_focus: [bool](class_bool.md#class_bool) = false ) |
| [PopupMenu](class_popupmenu.md#class_PopupMenu) | [get_menu](class_lineedit.md#class_LineEdit_method_get_menu) ( ) const |
| [int](class_int.md#class_int) | [get_next_composite_character_column](class_lineedit.md#class_LineEdit_method_get_next_composite_character_column) ( column: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_previous_composite_character_column](class_lineedit.md#class_LineEdit_method_get_previous_composite_character_column) ( column: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_scroll_offset](class_lineedit.md#class_LineEdit_method_get_scroll_offset) ( ) const |
| [String](class_string.md#class_String) | [get_selected_text](class_lineedit.md#class_LineEdit_method_get_selected_text) ( ) |
| [int](class_int.md#class_int) | [get_selection_from_column](class_lineedit.md#class_LineEdit_method_get_selection_from_column) ( ) const |
| [int](class_int.md#class_int) | [get_selection_to_column](class_lineedit.md#class_LineEdit_method_get_selection_to_column) ( ) const |
| [bool](class_bool.md#class_bool) | [has_ime_text](class_lineedit.md#class_LineEdit_method_has_ime_text) ( ) const |
| [bool](class_bool.md#class_bool) | [has_redo](class_lineedit.md#class_LineEdit_method_has_redo) ( ) const |
| [bool](class_bool.md#class_bool) | [has_selection](class_lineedit.md#class_LineEdit_method_has_selection) ( ) const |
| [bool](class_bool.md#class_bool) | [has_undo](class_lineedit.md#class_LineEdit_method_has_undo) ( ) const |
| void | [insert_text_at_caret](class_lineedit.md#class_LineEdit_method_insert_text_at_caret) ( text: [String](class_string.md#class_String) ) |
| [bool](class_bool.md#class_bool) | [is_editing](class_lineedit.md#class_LineEdit_method_is_editing) ( ) const |
| [bool](class_bool.md#class_bool) | [is_menu_visible](class_lineedit.md#class_LineEdit_method_is_menu_visible) ( ) const |
| void | [menu_option](class_lineedit.md#class_LineEdit_method_menu_option) ( option: [int](class_int.md#class_int) ) |
| void | [select](class_lineedit.md#class_LineEdit_method_select) ( from: [int](class_int.md#class_int) = 0, to: [int](class_int.md#class_int) = -1 ) |
| void | [select_all](class_lineedit.md#class_LineEdit_method_select_all) ( ) |
| void | [unedit](class_lineedit.md#class_LineEdit_method_unedit) ( ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [caret_color](class_lineedit.md#class_LineEdit_theme_color_caret_color) | `Color(0.95, 0.95, 0.95, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [clear_button_color](class_lineedit.md#class_LineEdit_theme_color_clear_button_color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class_Color) | [clear_button_color_pressed](class_lineedit.md#class_LineEdit_theme_color_clear_button_color_pressed) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [font_color](class_lineedit.md#class_LineEdit_theme_color_font_color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class_Color) | [font_outline_color](class_lineedit.md#class_LineEdit_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_placeholder_color](class_lineedit.md#class_LineEdit_theme_color_font_placeholder_color) | `Color(0.875, 0.875, 0.875, 0.6)` |
| [Color](class_color.md#class_Color) | [font_selected_color](class_lineedit.md#class_LineEdit_theme_color_font_selected_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [font_uneditable_color](class_lineedit.md#class_LineEdit_theme_color_font_uneditable_color) | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class_Color) | [selection_color](class_lineedit.md#class_LineEdit_theme_color_selection_color) | `Color(0.5, 0.5, 0.5, 1)` |
| [int](class_int.md#class_int) | [caret_width](class_lineedit.md#class_LineEdit_theme_constant_caret_width) | `1` |
| [int](class_int.md#class_int) | [minimum_character_width](class_lineedit.md#class_LineEdit_theme_constant_minimum_character_width) | `4` |
| [int](class_int.md#class_int) | [outline_size](class_lineedit.md#class_LineEdit_theme_constant_outline_size) | `0` |
| [Font](class_font.md#class_Font) | [font](class_lineedit.md#class_LineEdit_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_lineedit.md#class_LineEdit_theme_font_size_font_size) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [clear](class_lineedit.md#class_LineEdit_theme_icon_clear) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [focus](class_lineedit.md#class_LineEdit_theme_style_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [normal](class_lineedit.md#class_LineEdit_theme_style_normal) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [read_only](class_lineedit.md#class_LineEdit_theme_style_read_only) |

---

### Signals

<span id="class_LineEdit_signal_editing_toggled"></span>

**editing_toggled** ( toggled_on: [bool](class_bool.md#class_bool) ) [🔗](class_lineedit.md#class_LineEdit_signal_editing_toggled)

Emitted when the **LineEdit** switches in or out of edit mode.

---

<span id="class_LineEdit_signal_text_change_rejected"></span>

**text_change_rejected** ( rejected_substring: [String](class_string.md#class_String) ) [🔗](class_lineedit.md#class_LineEdit_signal_text_change_rejected)

Emitted when appending text that overflows the [max_length](class_lineedit.md#class_LineEdit_property_max_length). The appended text is truncated to fit [max_length](class_lineedit.md#class_LineEdit_property_max_length), and the part that couldn't fit is passed as the `rejected_substring` argument.

---

<span id="class_LineEdit_signal_text_changed"></span>

**text_changed** ( new_text: [String](class_string.md#class_String) ) [🔗](class_lineedit.md#class_LineEdit_signal_text_changed)

Emitted when the text changes.

---

<span id="class_LineEdit_signal_text_submitted"></span>

**text_submitted** ( new_text: [String](class_string.md#class_String) ) [🔗](class_lineedit.md#class_LineEdit_signal_text_submitted)

Emitted when the user presses the `ui_text_submit` action (by default: :kbd:`Enter` or :kbd:`Kp Enter`) while the **LineEdit** has focus.

---

### Enumerations

<span id="enum_LineEdit_MenuItems"></span>

enum **MenuItems**: [🔗](class_lineedit.md#enum_LineEdit_MenuItems)

<span id="class_LineEdit_constant_MENU_CUT"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_CUT** = `0`

Cuts (copies and clears) the selected text.

<span id="class_LineEdit_constant_MENU_COPY"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_COPY** = `1`

Copies the selected text.

<span id="class_LineEdit_constant_MENU_PASTE"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_PASTE** = `2`

Pastes the clipboard text over the selected text (or at the caret's position).

Non-printable escape characters are automatically stripped from the OS clipboard via [String.strip_escapes()](class_string.md#class_String_method_strip_escapes).

<span id="class_LineEdit_constant_MENU_CLEAR"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_CLEAR** = `3`

Erases the whole **LineEdit** text.

<span id="class_LineEdit_constant_MENU_SELECT_ALL"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_SELECT_ALL** = `4`

Selects the whole **LineEdit** text.

<span id="class_LineEdit_constant_MENU_UNDO"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_UNDO** = `5`

Undoes the previous action.

<span id="class_LineEdit_constant_MENU_REDO"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_REDO** = `6`

Reverse the last undo action.

<span id="class_LineEdit_constant_MENU_SUBMENU_TEXT_DIR"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_SUBMENU_TEXT_DIR** = `7`

ID of "Text Writing Direction" submenu.

<span id="class_LineEdit_constant_MENU_DIR_INHERITED"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_DIR_INHERITED** = `8`

Sets text direction to inherited.

<span id="class_LineEdit_constant_MENU_DIR_AUTO"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_DIR_AUTO** = `9`

Sets text direction to automatic.

<span id="class_LineEdit_constant_MENU_DIR_LTR"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_DIR_LTR** = `10`

Sets text direction to left-to-right.

<span id="class_LineEdit_constant_MENU_DIR_RTL"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_DIR_RTL** = `11`

Sets text direction to right-to-left.

<span id="class_LineEdit_constant_MENU_DISPLAY_UCC"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_DISPLAY_UCC** = `12`

Toggles control character display.

<span id="class_LineEdit_constant_MENU_SUBMENU_INSERT_UCC"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_SUBMENU_INSERT_UCC** = `13`

ID of "Insert Control Character" submenu.

<span id="class_LineEdit_constant_MENU_INSERT_LRM"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_LRM** = `14`

Inserts left-to-right mark (LRM) character.

<span id="class_LineEdit_constant_MENU_INSERT_RLM"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_RLM** = `15`

Inserts right-to-left mark (RLM) character.

<span id="class_LineEdit_constant_MENU_INSERT_LRE"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_LRE** = `16`

Inserts start of left-to-right embedding (LRE) character.

<span id="class_LineEdit_constant_MENU_INSERT_RLE"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_RLE** = `17`

Inserts start of right-to-left embedding (RLE) character.

<span id="class_LineEdit_constant_MENU_INSERT_LRO"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_LRO** = `18`

Inserts start of left-to-right override (LRO) character.

<span id="class_LineEdit_constant_MENU_INSERT_RLO"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_RLO** = `19`

Inserts start of right-to-left override (RLO) character.

<span id="class_LineEdit_constant_MENU_INSERT_PDF"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_PDF** = `20`

Inserts pop direction formatting (PDF) character.

<span id="class_LineEdit_constant_MENU_INSERT_ALM"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_ALM** = `21`

Inserts Arabic letter mark (ALM) character.

<span id="class_LineEdit_constant_MENU_INSERT_LRI"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_LRI** = `22`

Inserts left-to-right isolate (LRI) character.

<span id="class_LineEdit_constant_MENU_INSERT_RLI"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_RLI** = `23`

Inserts right-to-left isolate (RLI) character.

<span id="class_LineEdit_constant_MENU_INSERT_FSI"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_FSI** = `24`

Inserts first strong isolate (FSI) character.

<span id="class_LineEdit_constant_MENU_INSERT_PDI"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_PDI** = `25`

Inserts pop direction isolate (PDI) character.

<span id="class_LineEdit_constant_MENU_INSERT_ZWJ"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_ZWJ** = `26`

Inserts zero width joiner (ZWJ) character.

<span id="class_LineEdit_constant_MENU_INSERT_ZWNJ"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_ZWNJ** = `27`

Inserts zero width non-joiner (ZWNJ) character.

<span id="class_LineEdit_constant_MENU_INSERT_WJ"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_WJ** = `28`

Inserts word joiner (WJ) character.

<span id="class_LineEdit_constant_MENU_INSERT_SHY"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_INSERT_SHY** = `29`

Inserts soft hyphen (SHY) character.

<span id="class_LineEdit_constant_MENU_EMOJI_AND_SYMBOL"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_EMOJI_AND_SYMBOL** = `30`

Opens system emoji and symbol picker.

<span id="class_LineEdit_constant_MENU_MAX"></span>

[MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) **MENU_MAX** = `31`

Represents the size of the [MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) enum.

---

<span id="enum_LineEdit_VirtualKeyboardType"></span>

enum **VirtualKeyboardType**: [🔗](class_lineedit.md#enum_LineEdit_VirtualKeyboardType)

<span id="class_LineEdit_constant_KEYBOARD_TYPE_DEFAULT"></span>

[VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **KEYBOARD_TYPE_DEFAULT** = `0`

Default text virtual keyboard.

<span id="class_LineEdit_constant_KEYBOARD_TYPE_MULTILINE"></span>

[VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **KEYBOARD_TYPE_MULTILINE** = `1`

Multiline virtual keyboard.

<span id="class_LineEdit_constant_KEYBOARD_TYPE_NUMBER"></span>

[VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **KEYBOARD_TYPE_NUMBER** = `2`

Virtual number keypad, useful for PIN entry.

<span id="class_LineEdit_constant_KEYBOARD_TYPE_NUMBER_DECIMAL"></span>

[VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **KEYBOARD_TYPE_NUMBER_DECIMAL** = `3`

Virtual number keypad, useful for entering fractional numbers.

<span id="class_LineEdit_constant_KEYBOARD_TYPE_PHONE"></span>

[VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **KEYBOARD_TYPE_PHONE** = `4`

Virtual phone number keypad.

<span id="class_LineEdit_constant_KEYBOARD_TYPE_EMAIL_ADDRESS"></span>

[VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **KEYBOARD_TYPE_EMAIL_ADDRESS** = `5`

Virtual keyboard with additional keys to assist with typing email addresses.

<span id="class_LineEdit_constant_KEYBOARD_TYPE_PASSWORD"></span>

[VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **KEYBOARD_TYPE_PASSWORD** = `6`

Virtual keyboard for entering a password. On most platforms, this should disable autocomplete and autocapitalization.

 **Note:** This is not supported on Web. Instead, this behaves identically to [KEYBOARD_TYPE_DEFAULT](class_lineedit.md#class_LineEdit_constant_KEYBOARD_TYPE_DEFAULT).

<span id="class_LineEdit_constant_KEYBOARD_TYPE_URL"></span>

[VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **KEYBOARD_TYPE_URL** = `7`

Virtual keyboard with additional keys to assist with typing URLs.

---

<span id="enum_LineEdit_ExpandMode"></span>

enum **ExpandMode**: [🔗](class_lineedit.md#enum_LineEdit_ExpandMode)

<span id="class_LineEdit_constant_EXPAND_MODE_ORIGINAL_SIZE"></span>

[ExpandMode](class_lineedit.md#enum_LineEdit_ExpandMode) **EXPAND_MODE_ORIGINAL_SIZE** = `0`

Use the original size for the right icon.

<span id="class_LineEdit_constant_EXPAND_MODE_FIT_TO_TEXT"></span>

[ExpandMode](class_lineedit.md#enum_LineEdit_ExpandMode) **EXPAND_MODE_FIT_TO_TEXT** = `1`

Scale the right icon's size to match the size of the text.

<span id="class_LineEdit_constant_EXPAND_MODE_FIT_TO_LINE_EDIT"></span>

[ExpandMode](class_lineedit.md#enum_LineEdit_ExpandMode) **EXPAND_MODE_FIT_TO_LINE_EDIT** = `2`

Scale the right icon to fit the LineEdit.

---

### Property Descriptions

<span id="class_LineEdit_property_alignment"></span>

HorizontalAlignment **alignment** = `0` [🔗](class_lineedit.md#class_LineEdit_property_alignment)

- void **set_horizontal_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_horizontal_alignment** ( )

The text's horizontal alignment.

---

<span id="class_LineEdit_property_backspace_deletes_composite_character_enabled"></span>

[bool](class_bool.md#class_bool) **backspace_deletes_composite_character_enabled** = `false` [🔗](class_lineedit.md#class_LineEdit_property_backspace_deletes_composite_character_enabled)

- void **set_backspace_deletes_composite_character_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_backspace_deletes_composite_character_enabled** ( )

If `true` and [caret_mid_grapheme](class_lineedit.md#class_LineEdit_property_caret_mid_grapheme) is `false`, backspace deletes an entire composite character such as ❤️‍🩹, instead of deleting part of the composite character.

---

<span id="class_LineEdit_property_caret_blink"></span>

[bool](class_bool.md#class_bool) **caret_blink** = `false` [🔗](class_lineedit.md#class_LineEdit_property_caret_blink)

- void **set_caret_blink_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_caret_blink_enabled** ( )

If `true`, makes the caret blink.

---

<span id="class_LineEdit_property_caret_blink_interval"></span>

[float](class_float.md#class_float) **caret_blink_interval** = `0.65` [🔗](class_lineedit.md#class_LineEdit_property_caret_blink_interval)

- void **set_caret_blink_interval** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_caret_blink_interval** ( )

The interval at which the caret blinks (in seconds).

---

<span id="class_LineEdit_property_caret_column"></span>

[int](class_int.md#class_int) **caret_column** = `0` [🔗](class_lineedit.md#class_LineEdit_property_caret_column)

- void **set_caret_column** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_caret_column** ( )

The caret's column position inside the **LineEdit**. When set, the text may scroll to accommodate it.

---

<span id="class_LineEdit_property_caret_force_displayed"></span>

[bool](class_bool.md#class_bool) **caret_force_displayed** = `false` [🔗](class_lineedit.md#class_LineEdit_property_caret_force_displayed)

- void **set_caret_force_displayed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_caret_force_displayed** ( )

If `true`, the **LineEdit** will always show the caret, even if not editing or focus is lost.

---

<span id="class_LineEdit_property_caret_mid_grapheme"></span>

[bool](class_bool.md#class_bool) **caret_mid_grapheme** = `false` [🔗](class_lineedit.md#class_LineEdit_property_caret_mid_grapheme)

- void **set_caret_mid_grapheme_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_caret_mid_grapheme_enabled** ( )

Allow moving caret, selecting and removing the individual composite character components.

 **Note:** :kbd:`Backspace` is always removing individual composite character components.

---

<span id="class_LineEdit_property_clear_button_enabled"></span>

[bool](class_bool.md#class_bool) **clear_button_enabled** = `false` [🔗](class_lineedit.md#class_LineEdit_property_clear_button_enabled)

- void **set_clear_button_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_clear_button_enabled** ( )

If `true`, the **LineEdit** will show a clear button if [text](class_lineedit.md#class_LineEdit_property_text) is not empty, which can be used to clear the text quickly.

---

<span id="class_LineEdit_property_context_menu_enabled"></span>

[bool](class_bool.md#class_bool) **context_menu_enabled** = `true` [🔗](class_lineedit.md#class_LineEdit_property_context_menu_enabled)

- void **set_context_menu_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_context_menu_enabled** ( )

If `true`, the context menu will appear when right-clicked.

---

<span id="class_LineEdit_property_deselect_on_focus_loss_enabled"></span>

[bool](class_bool.md#class_bool) **deselect_on_focus_loss_enabled** = `true` [🔗](class_lineedit.md#class_LineEdit_property_deselect_on_focus_loss_enabled)

- void **set_deselect_on_focus_loss_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_deselect_on_focus_loss_enabled** ( )

If `true`, the selected text will be deselected when focus is lost.

---

<span id="class_LineEdit_property_drag_and_drop_selection_enabled"></span>

[bool](class_bool.md#class_bool) **drag_and_drop_selection_enabled** = `true` [🔗](class_lineedit.md#class_LineEdit_property_drag_and_drop_selection_enabled)

- void **set_drag_and_drop_selection_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drag_and_drop_selection_enabled** ( )

If `true`, allow drag and drop of selected text.

---

<span id="class_LineEdit_property_draw_control_chars"></span>

[bool](class_bool.md#class_bool) **draw_control_chars** = `false` [🔗](class_lineedit.md#class_LineEdit_property_draw_control_chars)

- void **set_draw_control_chars** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_draw_control_chars** ( )

If `true`, control characters are displayed.

---

<span id="class_LineEdit_property_editable"></span>

[bool](class_bool.md#class_bool) **editable** = `true` [🔗](class_lineedit.md#class_LineEdit_property_editable)

- void **set_editable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editable** ( )

If `false`, existing text cannot be modified and new text cannot be added.

---

<span id="class_LineEdit_property_emoji_menu_enabled"></span>

[bool](class_bool.md#class_bool) **emoji_menu_enabled** = `true` [🔗](class_lineedit.md#class_LineEdit_property_emoji_menu_enabled)

- void **set_emoji_menu_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_emoji_menu_enabled** ( )

If `true`, "Emoji and Symbols" menu is enabled.

---

<span id="class_LineEdit_property_expand_to_text_length"></span>

[bool](class_bool.md#class_bool) **expand_to_text_length** = `false` [🔗](class_lineedit.md#class_LineEdit_property_expand_to_text_length)

- void **set_expand_to_text_length_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_expand_to_text_length_enabled** ( )

If `true`, the **LineEdit** width will increase to stay longer than the [text](class_lineedit.md#class_LineEdit_property_text). It will **not** compress if the [text](class_lineedit.md#class_LineEdit_property_text) is shortened.

---

<span id="class_LineEdit_property_flat"></span>

[bool](class_bool.md#class_bool) **flat** = `false` [🔗](class_lineedit.md#class_LineEdit_property_flat)

- void **set_flat** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_flat** ( )

If `true`, the **LineEdit** doesn't display decoration.

---

<span id="class_LineEdit_property_icon_expand_mode"></span>

[ExpandMode](class_lineedit.md#enum_LineEdit_ExpandMode) **icon_expand_mode** = `0` [🔗](class_lineedit.md#class_LineEdit_property_icon_expand_mode)

- void **set_icon_expand_mode** ( value: [ExpandMode](class_lineedit.md#enum_LineEdit_ExpandMode) )
- [ExpandMode](class_lineedit.md#enum_LineEdit_ExpandMode) **get_icon_expand_mode** ( )

Define the scaling behavior of the [right_icon](class_lineedit.md#class_LineEdit_property_right_icon).

---

<span id="class_LineEdit_property_keep_editing_on_text_submit"></span>

[bool](class_bool.md#class_bool) **keep_editing_on_text_submit** = `false` [🔗](class_lineedit.md#class_LineEdit_property_keep_editing_on_text_submit)

- void **set_keep_editing_on_text_submit** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editing_kept_on_text_submit** ( )

If `true`, the **LineEdit** will not exit edit mode when text is submitted by pressing `ui_text_submit` action (by default: :kbd:`Enter` or :kbd:`Kp Enter`).

---

<span id="class_LineEdit_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_lineedit.md#class_LineEdit_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_LineEdit_property_max_length"></span>

[int](class_int.md#class_int) **max_length** = `0` [🔗](class_lineedit.md#class_LineEdit_property_max_length)

- void **set_max_length** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_length** ( )

Maximum number of characters that can be entered inside the **LineEdit**. If `0`, there is no limit.

When a limit is defined, characters that would exceed [max_length](class_lineedit.md#class_LineEdit_property_max_length) are truncated. This happens both for existing [text](class_lineedit.md#class_LineEdit_property_text) contents when setting the max length, or for new text inserted in the **LineEdit**, including pasting.

If any input text is truncated, the [text_change_rejected](class_lineedit.md#class_LineEdit_signal_text_change_rejected) signal is emitted with the truncated substring as a parameter:

.. tabs::

```
```

    text = "Hello world"
    max_length = 5
    # `text` becomes "Hello".
    max_length = 10
    text += " goodbye"
    # `text` becomes "Hello good".
    # `text_change_rejected` is emitted with "bye" as a parameter.

```
```

    Text = "Hello world";
    MaxLength = 5;
    // `Text` becomes "Hello".
    MaxLength = 10;
    Text += " goodbye";
    // `Text` becomes "Hello good".
    // `text_change_rejected` is emitted with "bye" as a parameter.

---

<span id="class_LineEdit_property_middle_mouse_paste_enabled"></span>

[bool](class_bool.md#class_bool) **middle_mouse_paste_enabled** = `true` [🔗](class_lineedit.md#class_LineEdit_property_middle_mouse_paste_enabled)

- void **set_middle_mouse_paste_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_middle_mouse_paste_enabled** ( )

If `false`, using middle mouse button to paste clipboard will be disabled.

 **Note:** This method is only implemented on Linux.

---

<span id="class_LineEdit_property_placeholder_text"></span>

[String](class_string.md#class_String) **placeholder_text** = `""` [🔗](class_lineedit.md#class_LineEdit_property_placeholder_text)

- void **set_placeholder** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_placeholder** ( )

Text shown when the **LineEdit** is empty. It is **not** the **LineEdit**'s default value (see [text](class_lineedit.md#class_LineEdit_property_text)).

---

<span id="class_LineEdit_property_right_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **right_icon** [🔗](class_lineedit.md#class_LineEdit_property_right_icon)

- void **set_right_icon** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_right_icon** ( )

Sets the icon that will appear in the right end of the **LineEdit** if there's no [text](class_lineedit.md#class_LineEdit_property_text), or always, if [clear_button_enabled](class_lineedit.md#class_LineEdit_property_clear_button_enabled) is set to `false`.

---

<span id="class_LineEdit_property_right_icon_scale"></span>

[float](class_float.md#class_float) **right_icon_scale** = `1.0` [🔗](class_lineedit.md#class_LineEdit_property_right_icon_scale)

- void **set_right_icon_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_right_icon_scale** ( )

Scale ratio of the icon when [icon_expand_mode](class_lineedit.md#class_LineEdit_property_icon_expand_mode) is set to [EXPAND_MODE_FIT_TO_LINE_EDIT](class_lineedit.md#class_LineEdit_constant_EXPAND_MODE_FIT_TO_LINE_EDIT).

---

<span id="class_LineEdit_property_secret"></span>

[bool](class_bool.md#class_bool) **secret** = `false` [🔗](class_lineedit.md#class_LineEdit_property_secret)

- void **set_secret** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_secret** ( )

If `true`, every character is replaced with the secret character (see [secret_character](class_lineedit.md#class_LineEdit_property_secret_character)).

---

<span id="class_LineEdit_property_secret_character"></span>

[String](class_string.md#class_String) **secret_character** = `"•"` [🔗](class_lineedit.md#class_LineEdit_property_secret_character)

- void **set_secret_character** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_secret_character** ( )

The character to use to mask secret input. Only a single character can be used as the secret character. If it is longer than one character, only the first one will be used. If it is empty, a space will be used instead.

---

<span id="class_LineEdit_property_select_all_on_focus"></span>

[bool](class_bool.md#class_bool) **select_all_on_focus** = `false` [🔗](class_lineedit.md#class_LineEdit_property_select_all_on_focus)

- void **set_select_all_on_focus** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_select_all_on_focus** ( )

If `true`, the **LineEdit** will select the whole text when it gains focus.

---

<span id="class_LineEdit_property_selecting_enabled"></span>

[bool](class_bool.md#class_bool) **selecting_enabled** = `true` [🔗](class_lineedit.md#class_LineEdit_property_selecting_enabled)

- void **set_selecting_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_selecting_enabled** ( )

If `false`, it's impossible to select the text using mouse nor keyboard.

---

<span id="class_LineEdit_property_shortcut_keys_enabled"></span>

[bool](class_bool.md#class_bool) **shortcut_keys_enabled** = `true` [🔗](class_lineedit.md#class_LineEdit_property_shortcut_keys_enabled)

- void **set_shortcut_keys_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_shortcut_keys_enabled** ( )

If `true`, shortcut keys for context menu items are enabled, even if the context menu is disabled.

---

<span id="class_LineEdit_property_structured_text_bidi_override"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **structured_text_bidi_override** = `0` [🔗](class_lineedit.md#class_LineEdit_property_structured_text_bidi_override)

- void **set_structured_text_bidi_override** ( value: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) )
- [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **get_structured_text_bidi_override** ( )

Set BiDi algorithm override for the structured text.

---

<span id="class_LineEdit_property_structured_text_bidi_override_options"></span>

[Array](class_array.md#class_Array) **structured_text_bidi_override_options** = `[]` [🔗](class_lineedit.md#class_LineEdit_property_structured_text_bidi_override_options)

- void **set_structured_text_bidi_override_options** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_structured_text_bidi_override_options** ( )

Set additional options for BiDi override.

---

<span id="class_LineEdit_property_text"></span>

[String](class_string.md#class_String) **text** = `""` [🔗](class_lineedit.md#class_LineEdit_property_text)

- void **set_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_text** ( )

String value of the **LineEdit**.

 **Note:** Changing text using this property won't emit the [text_changed](class_lineedit.md#class_LineEdit_signal_text_changed) signal.

---

<span id="class_LineEdit_property_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **text_direction** = `0` [🔗](class_lineedit.md#class_LineEdit_property_text_direction)

- void **set_text_direction** ( value: [TextDirection](class_control.md#enum_Control_TextDirection) )
- [TextDirection](class_control.md#enum_Control_TextDirection) **get_text_direction** ( )

Base text writing direction.

---

<span id="class_LineEdit_property_virtual_keyboard_enabled"></span>

[bool](class_bool.md#class_bool) **virtual_keyboard_enabled** = `true` [🔗](class_lineedit.md#class_LineEdit_property_virtual_keyboard_enabled)

- void **set_virtual_keyboard_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_virtual_keyboard_enabled** ( )

If `true`, the native virtual keyboard is enabled on platforms that support it.

---

<span id="class_LineEdit_property_virtual_keyboard_show_on_focus"></span>

[bool](class_bool.md#class_bool) **virtual_keyboard_show_on_focus** = `true` [🔗](class_lineedit.md#class_LineEdit_property_virtual_keyboard_show_on_focus)

- void **set_virtual_keyboard_show_on_focus** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_virtual_keyboard_show_on_focus** ( )

If `true`, the native virtual keyboard is shown on focus events on platforms that support it.

---

<span id="class_LineEdit_property_virtual_keyboard_type"></span>

[VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **virtual_keyboard_type** = `0` [🔗](class_lineedit.md#class_LineEdit_property_virtual_keyboard_type)

- void **set_virtual_keyboard_type** ( value: [VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) )
- [VirtualKeyboardType](class_lineedit.md#enum_LineEdit_VirtualKeyboardType) **get_virtual_keyboard_type** ( )

Specifies the type of virtual keyboard to show.

---

### Method Descriptions

<span id="class_LineEdit_method_apply_ime"></span>

void **apply_ime** ( ) [🔗](class_lineedit.md#class_LineEdit_method_apply_ime)

Applies text from the Input Method Editor (IME) and closes the IME if it is open.

---

<span id="class_LineEdit_method_cancel_ime"></span>

void **cancel_ime** ( ) [🔗](class_lineedit.md#class_LineEdit_method_cancel_ime)

Closes the Input Method Editor (IME) if it is open. Any text in the IME will be lost.

---

<span id="class_LineEdit_method_clear"></span>

void **clear** ( ) [🔗](class_lineedit.md#class_LineEdit_method_clear)

Erases the **LineEdit**'s [text](class_lineedit.md#class_LineEdit_property_text).

---

<span id="class_LineEdit_method_delete_char_at_caret"></span>

void **delete_char_at_caret** ( ) [🔗](class_lineedit.md#class_LineEdit_method_delete_char_at_caret)

Deletes one character at the caret's current position (equivalent to pressing :kbd:`Delete`).

---

<span id="class_LineEdit_method_delete_text"></span>

void **delete_text** ( from_column: [int](class_int.md#class_int), to_column: [int](class_int.md#class_int) ) [🔗](class_lineedit.md#class_LineEdit_method_delete_text)

Deletes a section of the [text](class_lineedit.md#class_LineEdit_property_text) going from position `from_column` to `to_column`. Both parameters should be within the text's length.

---

<span id="class_LineEdit_method_deselect"></span>

void **deselect** ( ) [🔗](class_lineedit.md#class_LineEdit_method_deselect)

Clears the current selection.

---

<span id="class_LineEdit_method_edit"></span>

void **edit** ( hide_focus: [bool](class_bool.md#class_bool) = false ) [🔗](class_lineedit.md#class_LineEdit_method_edit)

Allows entering edit mode whether the **LineEdit** is focused or not. If `hide_focus` is `true`, the focused state will not be shown (see [Control.grab_focus()](class_control.md#class_Control_method_grab_focus)).

See also [keep_editing_on_text_submit](class_lineedit.md#class_LineEdit_property_keep_editing_on_text_submit).

---

<span id="class_LineEdit_method_get_menu"></span>

[PopupMenu](class_popupmenu.md#class_PopupMenu) **get_menu** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_get_menu)

Returns the [PopupMenu](class_popupmenu.md#class_PopupMenu) of this **LineEdit**. By default, this menu is displayed when right-clicking on the **LineEdit**.

You can add custom menu items or remove standard ones. Make sure your IDs don't conflict with the standard ones (see [MenuItems](class_lineedit.md#enum_LineEdit_MenuItems)). For example:

.. tabs::

```
```

    func _ready():
        var menu = get_menu()
        # Remove all items after "Redo".
        menu.item_count = menu.get_item_index(MENU_REDO) + 1
        # Add custom items.
        menu.add_separator()
        menu.add_item("Insert Date", MENU_MAX + 1)
        # Connect callback.
        menu.id_pressed.connect(_on_item_pressed)

    func _on_item_pressed(id):
        if id == MENU_MAX + 1:
            insert_text_at_caret(Time.get_date_string_from_system())

```
```

    public override void _Ready()
    {
        var menu = GetMenu();
        // Remove all items after "Redo".
        menu.ItemCount = menu.GetItemIndex(LineEdit.MenuItems.Redo) + 1;
        // Add custom items.
        menu.AddSeparator();
        menu.AddItem("Insert Date", LineEdit.MenuItems.Max + 1);
        // Add event handler.
        menu.IdPressed += OnItemPressed;
    }

    public void OnItemPressed(int id)
    {
        if (id == LineEdit.MenuItems.Max + 1)
        {
            InsertTextAtCaret(Time.GetDateStringFromSystem());
        }
    }

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class_Window_property_visible) property.

---

<span id="class_LineEdit_method_get_next_composite_character_column"></span>

[int](class_int.md#class_int) **get_next_composite_character_column** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_lineedit.md#class_LineEdit_method_get_next_composite_character_column)

Returns the correct column at the end of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the start of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

 **Note:** To check at caret location use `get_next_composite_character_column(get_caret_column())`

---

<span id="class_LineEdit_method_get_previous_composite_character_column"></span>

[int](class_int.md#class_int) **get_previous_composite_character_column** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_lineedit.md#class_LineEdit_method_get_previous_composite_character_column)

Returns the correct column at the start of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the end of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

 **Note:** To check at caret location use `get_previous_composite_character_column(get_caret_column())`

---

<span id="class_LineEdit_method_get_scroll_offset"></span>

[float](class_float.md#class_float) **get_scroll_offset** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_get_scroll_offset)

Returns the scroll offset due to [caret_column](class_lineedit.md#class_LineEdit_property_caret_column), as a number of characters.

---

<span id="class_LineEdit_method_get_selected_text"></span>

[String](class_string.md#class_String) **get_selected_text** ( ) [🔗](class_lineedit.md#class_LineEdit_method_get_selected_text)

Returns the text inside the selection.

---

<span id="class_LineEdit_method_get_selection_from_column"></span>

[int](class_int.md#class_int) **get_selection_from_column** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_get_selection_from_column)

Returns the selection begin column.

---

<span id="class_LineEdit_method_get_selection_to_column"></span>

[int](class_int.md#class_int) **get_selection_to_column** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_get_selection_to_column)

Returns the selection end column.

---

<span id="class_LineEdit_method_has_ime_text"></span>

[bool](class_bool.md#class_bool) **has_ime_text** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_has_ime_text)

Returns `true` if the user has text in the Input Method Editor (IME).

---

<span id="class_LineEdit_method_has_redo"></span>

[bool](class_bool.md#class_bool) **has_redo** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_has_redo)

Returns `true` if a "redo" action is available.

---

<span id="class_LineEdit_method_has_selection"></span>

[bool](class_bool.md#class_bool) **has_selection** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_has_selection)

Returns `true` if the user has selected text.

---

<span id="class_LineEdit_method_has_undo"></span>

[bool](class_bool.md#class_bool) **has_undo** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_has_undo)

Returns `true` if an "undo" action is available.

---

<span id="class_LineEdit_method_insert_text_at_caret"></span>

void **insert_text_at_caret** ( text: [String](class_string.md#class_String) ) [🔗](class_lineedit.md#class_LineEdit_method_insert_text_at_caret)

Inserts `text` at the caret. If the resulting value is longer than [max_length](class_lineedit.md#class_LineEdit_property_max_length), nothing happens.

---

<span id="class_LineEdit_method_is_editing"></span>

[bool](class_bool.md#class_bool) **is_editing** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_is_editing)

Returns whether the **LineEdit** is being edited.

---

<span id="class_LineEdit_method_is_menu_visible"></span>

[bool](class_bool.md#class_bool) **is_menu_visible** ( ) *const* [🔗](class_lineedit.md#class_LineEdit_method_is_menu_visible)

Returns whether the menu is visible. Use this instead of `get_menu().visible` to improve performance (so the creation of the menu is avoided).

---

<span id="class_LineEdit_method_menu_option"></span>

void **menu_option** ( option: [int](class_int.md#class_int) ) [🔗](class_lineedit.md#class_LineEdit_method_menu_option)

Executes a given action as defined in the [MenuItems](class_lineedit.md#enum_LineEdit_MenuItems) enum.

---

<span id="class_LineEdit_method_select"></span>

void **select** ( from: [int](class_int.md#class_int) = 0, to: [int](class_int.md#class_int) = -1 ) [🔗](class_lineedit.md#class_LineEdit_method_select)

Selects characters inside **LineEdit** between `from` and `to`. By default, `from` is at the beginning and `to` at the end.

.. tabs::

```
```

    text = "Welcome"
    select() # Will select "Welcome".
    select(4) # Will select "ome".
    select(2, 5) # Will select "lco".

```
```

    Text = "Welcome";
    Select(); // Will select "Welcome".
    Select(4); // Will select "ome".
    Select(2, 5); // Will select "lco".

---

<span id="class_LineEdit_method_select_all"></span>

void **select_all** ( ) [🔗](class_lineedit.md#class_LineEdit_method_select_all)

Selects the whole [String](class_string.md#class_String).

---

<span id="class_LineEdit_method_unedit"></span>

void **unedit** ( ) [🔗](class_lineedit.md#class_LineEdit_method_unedit)

Allows exiting edit mode while preserving focus.

---

### Theme Property Descriptions

<span id="class_LineEdit_theme_color_caret_color"></span>

[Color](class_color.md#class_Color) **caret_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_lineedit.md#class_LineEdit_theme_color_caret_color)

Color of the **LineEdit**'s caret (text cursor). This can be set to a fully transparent color to hide the caret entirely.

---

<span id="class_LineEdit_theme_color_clear_button_color"></span>

[Color](class_color.md#class_Color) **clear_button_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_lineedit.md#class_LineEdit_theme_color_clear_button_color)

Color used as default tint for the clear button.

---

<span id="class_LineEdit_theme_color_clear_button_color_pressed"></span>

[Color](class_color.md#class_Color) **clear_button_color_pressed** = `Color(1, 1, 1, 1)` [🔗](class_lineedit.md#class_LineEdit_theme_color_clear_button_color_pressed)

Color used for the clear button when it's pressed.

---

<span id="class_LineEdit_theme_color_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_lineedit.md#class_LineEdit_theme_color_font_color)

Default font color.

---

<span id="class_LineEdit_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_lineedit.md#class_LineEdit_theme_color_font_outline_color)

The tint of text outline of the **LineEdit**.

---

<span id="class_LineEdit_theme_color_font_placeholder_color"></span>

[Color](class_color.md#class_Color) **font_placeholder_color** = `Color(0.875, 0.875, 0.875, 0.6)` [🔗](class_lineedit.md#class_LineEdit_theme_color_font_placeholder_color)

Font color for [placeholder_text](class_lineedit.md#class_LineEdit_property_placeholder_text).

---

<span id="class_LineEdit_theme_color_font_selected_color"></span>

[Color](class_color.md#class_Color) **font_selected_color** = `Color(1, 1, 1, 1)` [🔗](class_lineedit.md#class_LineEdit_theme_color_font_selected_color)

Font color for selected text (inside the selection rectangle).

---

<span id="class_LineEdit_theme_color_font_uneditable_color"></span>

[Color](class_color.md#class_Color) **font_uneditable_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗](class_lineedit.md#class_LineEdit_theme_color_font_uneditable_color)

Font color when editing is disabled.

---

<span id="class_LineEdit_theme_color_selection_color"></span>

[Color](class_color.md#class_Color) **selection_color** = `Color(0.5, 0.5, 0.5, 1)` [🔗](class_lineedit.md#class_LineEdit_theme_color_selection_color)

Color of the selection rectangle.

---

<span id="class_LineEdit_theme_constant_caret_width"></span>

[int](class_int.md#class_int) **caret_width** = `1` [🔗](class_lineedit.md#class_LineEdit_theme_constant_caret_width)

The caret's width in pixels. Greater values can be used to improve accessibility by ensuring the caret is easily visible, or to ensure consistency with a large font size.

---

<span id="class_LineEdit_theme_constant_minimum_character_width"></span>

[int](class_int.md#class_int) **minimum_character_width** = `4` [🔗](class_lineedit.md#class_LineEdit_theme_constant_minimum_character_width)

Minimum horizontal space for the text (not counting the clear button and content margins). This value is measured in count of 'M' characters (i.e. this number of 'M' characters can be displayed without scrolling).

---

<span id="class_LineEdit_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_lineedit.md#class_LineEdit_theme_constant_outline_size)

The size of the text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_lineedit.md#class_LineEdit_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_LineEdit_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_lineedit.md#class_LineEdit_theme_font_font)

Font used for the text.

---

<span id="class_LineEdit_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_lineedit.md#class_LineEdit_theme_font_size_font_size)

Font size of the **LineEdit**'s text.

---

<span id="class_LineEdit_theme_icon_clear"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **clear** [🔗](class_lineedit.md#class_LineEdit_theme_icon_clear)

Texture for the clear button. See [clear_button_enabled](class_lineedit.md#class_LineEdit_property_clear_button_enabled).

---

<span id="class_LineEdit_theme_style_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **focus** [🔗](class_lineedit.md#class_LineEdit_theme_style_focus)

Background used when **LineEdit** has GUI focus. The [focus](class_lineedit.md#class_LineEdit_theme_style_focus) [StyleBox](class_stylebox.md#class_StyleBox) is displayed *over* the base [StyleBox](class_stylebox.md#class_StyleBox), so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the base [StyleBox](class_stylebox.md#class_StyleBox) remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_LineEdit_theme_style_normal"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **normal** [🔗](class_lineedit.md#class_LineEdit_theme_style_normal)

Default background for the **LineEdit**.

---

<span id="class_LineEdit_theme_style_read_only"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **read_only** [🔗](class_lineedit.md#class_LineEdit_theme_style_read_only)

Background used when **LineEdit** is in read-only mode ([editable](class_lineedit.md#class_LineEdit_property_editable) is set to `false`).
