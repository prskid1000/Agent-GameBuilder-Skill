<span id="class_AcceptDialog"></span>

## AcceptDialog

**Inherits:** [Window](class_window.md#class_Window) **<** [Viewport](class_viewport.md#class_Viewport) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [ConfirmationDialog](class_confirmationdialog.md#class_ConfirmationDialog)

A base dialog used for user notification.

### Description

The default use of **AcceptDialog** is to allow it to only be accepted or closed, with the same result. However, the [confirmed](class_acceptdialog.md#class_AcceptDialog_signal_confirmed) and [canceled](class_acceptdialog.md#class_AcceptDialog_signal_canceled) signals allow to make the two actions different, and the [add_button()](class_acceptdialog.md#class_AcceptDialog_method_add_button) method allows to add custom buttons and actions.

 **Note:** **AcceptDialog** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class_Window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class_Window_method_popup_centered_clamped).

### Properties


| [bool](class_bool.md#class_bool) | [dialog_autowrap](class_acceptdialog.md#class_AcceptDialog_property_dialog_autowrap) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [dialog_close_on_escape](class_acceptdialog.md#class_AcceptDialog_property_dialog_close_on_escape) | `true` |
| [bool](class_bool.md#class_bool) | [dialog_hide_on_ok](class_acceptdialog.md#class_AcceptDialog_property_dialog_hide_on_ok) | `true` |
| [String](class_string.md#class_String) | [dialog_text](class_acceptdialog.md#class_AcceptDialog_property_dialog_text) | `""` |
| [bool](class_bool.md#class_bool) | exclusive | `true` (overrides [Window](class_window.md#class_Window_property_exclusive)) |
| [bool](class_bool.md#class_bool) | keep_title_visible | `true` (overrides [Window](class_window.md#class_Window_property_keep_title_visible)) |
| [bool](class_bool.md#class_bool) | maximize_disabled | `true` (overrides [Window](class_window.md#class_Window_property_maximize_disabled)) |
| [bool](class_bool.md#class_bool) | minimize_disabled | `true` (overrides [Window](class_window.md#class_Window_property_minimize_disabled)) |
| [String](class_string.md#class_String) | [ok_button_text](class_acceptdialog.md#class_AcceptDialog_property_ok_button_text) | `""` |
| [String](class_string.md#class_String) | title | `"Alert!"` (overrides [Window](class_window.md#class_Window_property_title)) |
| [bool](class_bool.md#class_bool) | transient | `true` (overrides [Window](class_window.md#class_Window_property_transient)) |
| [bool](class_bool.md#class_bool) | visible | `false` (overrides [Window](class_window.md#class_Window_property_visible)) |
| [bool](class_bool.md#class_bool) | wrap_controls | `true` (overrides [Window](class_window.md#class_Window_property_wrap_controls)) |

### Methods


| [Button](class_button.md#class_Button) | [add_button](class_acceptdialog.md#class_AcceptDialog_method_add_button) ( text: [String](class_string.md#class_String), right: [bool](class_bool.md#class_bool) = false, action: [String](class_string.md#class_String) = "" ) |
| --- | --- |
| [Button](class_button.md#class_Button) | [add_cancel_button](class_acceptdialog.md#class_AcceptDialog_method_add_cancel_button) ( name: [String](class_string.md#class_String) ) |
| [Label](class_label.md#class_Label) | [get_label](class_acceptdialog.md#class_AcceptDialog_method_get_label) ( ) |
| [Button](class_button.md#class_Button) | [get_ok_button](class_acceptdialog.md#class_AcceptDialog_method_get_ok_button) ( ) |
| void | [register_text_enter](class_acceptdialog.md#class_AcceptDialog_method_register_text_enter) ( line_edit: [LineEdit](class_lineedit.md#class_LineEdit) ) |
| void | [remove_button](class_acceptdialog.md#class_AcceptDialog_method_remove_button) ( button: [Button](class_button.md#class_Button) ) |

### Theme Properties


| [int](class_int.md#class_int) | [buttons_min_height](class_acceptdialog.md#class_AcceptDialog_theme_constant_buttons_min_height) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [buttons_min_width](class_acceptdialog.md#class_AcceptDialog_theme_constant_buttons_min_width) | `0` |
| [int](class_int.md#class_int) | [buttons_separation](class_acceptdialog.md#class_AcceptDialog_theme_constant_buttons_separation) | `10` |
| [StyleBox](class_stylebox.md#class_StyleBox) | [panel](class_acceptdialog.md#class_AcceptDialog_theme_style_panel) |

---

### Signals

<span id="class_AcceptDialog_signal_canceled"></span>

**canceled** ( ) [🔗](class_acceptdialog.md#class_AcceptDialog_signal_canceled)

Emitted when the dialog is closed or the button created with [add_cancel_button()](class_acceptdialog.md#class_AcceptDialog_method_add_cancel_button) is pressed.

---

<span id="class_AcceptDialog_signal_confirmed"></span>

**confirmed** ( ) [🔗](class_acceptdialog.md#class_AcceptDialog_signal_confirmed)

Emitted when the dialog is accepted, i.e. the OK button is pressed.

---

<span id="class_AcceptDialog_signal_custom_action"></span>

**custom_action** ( action: [StringName](class_stringname.md#class_StringName) ) [🔗](class_acceptdialog.md#class_AcceptDialog_signal_custom_action)

Emitted when a custom button with an action is pressed. See [add_button()](class_acceptdialog.md#class_AcceptDialog_method_add_button).

---

### Property Descriptions

<span id="class_AcceptDialog_property_dialog_autowrap"></span>

[bool](class_bool.md#class_bool) **dialog_autowrap** = `false` [🔗](class_acceptdialog.md#class_AcceptDialog_property_dialog_autowrap)

- void **set_autowrap** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_autowrap** ( )

Sets autowrapping for the text in the dialog.

---

<span id="class_AcceptDialog_property_dialog_close_on_escape"></span>

[bool](class_bool.md#class_bool) **dialog_close_on_escape** = `true` [🔗](class_acceptdialog.md#class_AcceptDialog_property_dialog_close_on_escape)

- void **set_close_on_escape** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_close_on_escape** ( )

If `true`, the dialog will be hidden when the `ui_close_dialog` action is pressed (by default, this action is bound to :kbd:`Escape`, or :kbd:`Cmd + W` on macOS).

---

<span id="class_AcceptDialog_property_dialog_hide_on_ok"></span>

[bool](class_bool.md#class_bool) **dialog_hide_on_ok** = `true` [🔗](class_acceptdialog.md#class_AcceptDialog_property_dialog_hide_on_ok)

- void **set_hide_on_ok** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_hide_on_ok** ( )

If `true`, the dialog is hidden when the OK button is pressed. You can set it to `false` if you want to do e.g. input validation when receiving the [confirmed](class_acceptdialog.md#class_AcceptDialog_signal_confirmed) signal, and handle hiding the dialog in your own logic.

 **Note:** Some nodes derived from this class can have a different default value, and potentially their own built-in logic overriding this setting. For example [FileDialog](class_filedialog.md#class_FileDialog) defaults to `false`, and has its own input validation code that is called when you press OK, which eventually hides the dialog if the input is valid. As such, this property can't be used in [FileDialog](class_filedialog.md#class_FileDialog) to disable hiding the dialog when pressing OK.

---

<span id="class_AcceptDialog_property_dialog_text"></span>

[String](class_string.md#class_String) **dialog_text** = `""` [🔗](class_acceptdialog.md#class_AcceptDialog_property_dialog_text)

- void **set_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_text** ( )

The text displayed by the dialog.

---

<span id="class_AcceptDialog_property_ok_button_text"></span>

[String](class_string.md#class_String) **ok_button_text** = `""` [🔗](class_acceptdialog.md#class_AcceptDialog_property_ok_button_text)

- void **set_ok_button_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_ok_button_text** ( )

The text displayed by the OK button (see [get_ok_button()](class_acceptdialog.md#class_AcceptDialog_method_get_ok_button)). If empty, a default text will be used.

---

### Method Descriptions

<span id="class_AcceptDialog_method_add_button"></span>

[Button](class_button.md#class_Button) **add_button** ( text: [String](class_string.md#class_String), right: [bool](class_bool.md#class_bool) = false, action: [String](class_string.md#class_String) = "" ) [🔗](class_acceptdialog.md#class_AcceptDialog_method_add_button)

Adds a button with label `text` and a custom `action` to the dialog and returns the created button.

If `action` is not empty, pressing the button will emit the [custom_action](class_acceptdialog.md#class_AcceptDialog_signal_custom_action) signal with the specified action string.

If `true`, `right` will place the button to the right of any sibling buttons.

You can use [remove_button()](class_acceptdialog.md#class_AcceptDialog_method_remove_button) method to remove a button created with this method from the dialog.

---

<span id="class_AcceptDialog_method_add_cancel_button"></span>

[Button](class_button.md#class_Button) **add_cancel_button** ( name: [String](class_string.md#class_String) ) [🔗](class_acceptdialog.md#class_AcceptDialog_method_add_cancel_button)

Adds a button with label `name` and a cancel action to the dialog and returns the created button.

You can use [remove_button()](class_acceptdialog.md#class_AcceptDialog_method_remove_button) method to remove a button created with this method from the dialog.

---

<span id="class_AcceptDialog_method_get_label"></span>

[Label](class_label.md#class_Label) **get_label** ( ) [🔗](class_acceptdialog.md#class_AcceptDialog_method_get_label)

Returns the label used for built-in text.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.

---

<span id="class_AcceptDialog_method_get_ok_button"></span>

[Button](class_button.md#class_Button) **get_ok_button** ( ) [🔗](class_acceptdialog.md#class_AcceptDialog_method_get_ok_button)

Returns the OK [Button](class_button.md#class_Button) instance.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.

---

<span id="class_AcceptDialog_method_register_text_enter"></span>

void **register_text_enter** ( line_edit: [LineEdit](class_lineedit.md#class_LineEdit) ) [🔗](class_acceptdialog.md#class_AcceptDialog_method_register_text_enter)

Registers a [LineEdit](class_lineedit.md#class_LineEdit) in the dialog. When the enter key is pressed, the dialog will be accepted.

---

<span id="class_AcceptDialog_method_remove_button"></span>

void **remove_button** ( button: [Button](class_button.md#class_Button) ) [🔗](class_acceptdialog.md#class_AcceptDialog_method_remove_button)

Removes the `button` from the dialog. Does NOT free the `button`. The `button` must be a [Button](class_button.md#class_Button) added with [add_button()](class_acceptdialog.md#class_AcceptDialog_method_add_button) or [add_cancel_button()](class_acceptdialog.md#class_AcceptDialog_method_add_cancel_button) method. After removal, pressing the `button` will no longer emit this dialog's [custom_action](class_acceptdialog.md#class_AcceptDialog_signal_custom_action) or [canceled](class_acceptdialog.md#class_AcceptDialog_signal_canceled) signals.

---

### Theme Property Descriptions

<span id="class_AcceptDialog_theme_constant_buttons_min_height"></span>

[int](class_int.md#class_int) **buttons_min_height** = `0` [🔗](class_acceptdialog.md#class_AcceptDialog_theme_constant_buttons_min_height)

The minimum height of each button in the bottom row (such as OK/Cancel) in pixels. This can be increased to make buttons with short texts easier to click/tap.

---

<span id="class_AcceptDialog_theme_constant_buttons_min_width"></span>

[int](class_int.md#class_int) **buttons_min_width** = `0` [🔗](class_acceptdialog.md#class_AcceptDialog_theme_constant_buttons_min_width)

The minimum width of each button in the bottom row (such as OK/Cancel) in pixels. This can be increased to make buttons with short texts easier to click/tap.

---

<span id="class_AcceptDialog_theme_constant_buttons_separation"></span>

[int](class_int.md#class_int) **buttons_separation** = `10` [🔗](class_acceptdialog.md#class_AcceptDialog_theme_constant_buttons_separation)

The size of the vertical space between the dialog's content and the button row.

---

<span id="class_AcceptDialog_theme_style_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **panel** [🔗](class_acceptdialog.md#class_AcceptDialog_theme_style_panel)

The panel that fills the background of the window.
