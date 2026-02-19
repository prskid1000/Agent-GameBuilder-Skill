<span id="class_EditorFileDialog"></span>

## EditorFileDialog

**Inherits:** [FileDialog](class_filedialog.md#class_FileDialog) **<** [ConfirmationDialog](class_confirmationdialog.md#class_ConfirmationDialog) **<** [AcceptDialog](class_acceptdialog.md#class_AcceptDialog) **<** [Window](class_window.md#class_Window) **<** [Viewport](class_viewport.md#class_Viewport) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A modified version of [FileDialog](class_filedialog.md#class_FileDialog) used by the editor.

### Description

**EditorFileDialog** is a [FileDialog](class_filedialog.md#class_FileDialog) tweaked to work in the editor. It automatically handles favorite and recent directory lists, and synchronizes some properties with their corresponding editor settings.

 **EditorFileDialog** will automatically show a native dialog based on the EditorSettings.interface/editor/use_native_file_dialogs editor setting and ignores [FileDialog.use_native_dialog](class_filedialog.md#class_FileDialog_property_use_native_dialog).

 **Note:** **EditorFileDialog** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window](class_window.md#class_Window) on the node, such as [Window.popup_centered_clamped()](class_window.md#class_Window_method_popup_centered_clamped).

### Properties


| [bool](class_bool.md#class_bool) | [disable_overwrite_warning](class_editorfiledialog.md#class_EditorFileDialog_property_disable_overwrite_warning) | `false` |
| --- | --- | --- |

### Methods


| void | [add_side_menu](class_editorfiledialog.md#class_EditorFileDialog_method_add_side_menu) ( menu: [Control](class_control.md#class_Control), title: [String](class_string.md#class_String) = "" ) |
| --- | --- |

---

### Property Descriptions

<span id="class_EditorFileDialog_property_disable_overwrite_warning"></span>

[bool](class_bool.md#class_bool) **disable_overwrite_warning** = `false` [🔗](class_editorfiledialog.md#class_EditorFileDialog_property_disable_overwrite_warning)

- void **set_disable_overwrite_warning** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_overwrite_warning_disabled** ( )

**Deprecated:** Use [FileDialog.overwrite_warning_enabled](class_filedialog.md#class_FileDialog_property_overwrite_warning_enabled) instead.

If `true`, the **EditorFileDialog** will not warn the user before overwriting files.

---

### Method Descriptions

<span id="class_EditorFileDialog_method_add_side_menu"></span>

void **add_side_menu** ( menu: [Control](class_control.md#class_Control), title: [String](class_string.md#class_String) = "" ) [🔗](class_editorfiledialog.md#class_EditorFileDialog_method_add_side_menu)

**Deprecated:** This feature is no longer supported.

This method is kept for compatibility and does nothing. As an alternative, you can display another dialog after showing the file dialog.
