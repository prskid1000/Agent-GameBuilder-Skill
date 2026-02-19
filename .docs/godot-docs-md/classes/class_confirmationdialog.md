<span id="class_ConfirmationDialog"></span>

## ConfirmationDialog

**Inherits:** [AcceptDialog](class_acceptdialog.md#class_AcceptDialog) **<** [Window](class_window.md#class_Window) **<** [Viewport](class_viewport.md#class_Viewport) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [EditorCommandPalette](class_editorcommandpalette.md#class_EditorCommandPalette), [FileDialog](class_filedialog.md#class_FileDialog), [ScriptCreateDialog](class_scriptcreatedialog.md#class_ScriptCreateDialog)

A dialog used for confirmation of actions.

### Description

A dialog used for confirmation of actions. This window is similar to [AcceptDialog](class_acceptdialog.md#class_AcceptDialog), but pressing its Cancel button can have a different outcome from pressing the OK button. The order of the two buttons varies depending on the host OS.

To get cancel action, you can use:

.. tabs::

```
```

    get_cancel_button().pressed.connect(_on_canceled)

```
```

    GetCancelButton().Pressed += OnCanceled;

 **Note:** [AcceptDialog](class_acceptdialog.md#class_AcceptDialog) is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class_Window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class_Window_method_popup_centered_clamped).

### Properties


| [String](class_string.md#class_String) | [cancel_button_text](class_confirmationdialog.md#class_ConfirmationDialog_property_cancel_button_text) | `"Cancel"` |
| --- | --- | --- |
| [Vector2i](class_vector2i.md#class_Vector2i) | min_size | `Vector2i(200, 70)` (overrides [Window](class_window.md#class_Window_property_min_size)) |
| [Vector2i](class_vector2i.md#class_Vector2i) | size | `Vector2i(200, 100)` (overrides [Window](class_window.md#class_Window_property_size)) |
| [String](class_string.md#class_String) | title | `"Please Confirm..."` (overrides [Window](class_window.md#class_Window_property_title)) |

### Methods


| [Button](class_button.md#class_Button) | [get_cancel_button](class_confirmationdialog.md#class_ConfirmationDialog_method_get_cancel_button) ( ) |
| --- | --- |

---

### Property Descriptions

<span id="class_ConfirmationDialog_property_cancel_button_text"></span>

[String](class_string.md#class_String) **cancel_button_text** = `"Cancel"` [🔗](class_confirmationdialog.md#class_ConfirmationDialog_property_cancel_button_text)

- void **set_cancel_button_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_cancel_button_text** ( )

The text displayed by the cancel button (see [get_cancel_button()](class_confirmationdialog.md#class_ConfirmationDialog_method_get_cancel_button)).

---

### Method Descriptions

<span id="class_ConfirmationDialog_method_get_cancel_button"></span>

[Button](class_button.md#class_Button) **get_cancel_button** ( ) [🔗](class_confirmationdialog.md#class_ConfirmationDialog_method_get_cancel_button)

Returns the cancel button.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.
