<span id="class_ScriptCreateDialog"></span>

## ScriptCreateDialog

**Inherits:** [ConfirmationDialog](class_confirmationdialog.md#class_ConfirmationDialog) **<** [AcceptDialog](class_acceptdialog.md#class_AcceptDialog) **<** [Window](class_window.md#class_Window) **<** [Viewport](class_viewport.md#class_Viewport) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Godot editor's popup dialog for creating new [Script](class_script.md#class_Script) files.

### Description

The **ScriptCreateDialog** creates script files according to a given template for a given scripting language. The standard use is to configure its fields prior to calling one of the [Window.popup()](class_window.md#class_Window_method_popup) methods.

.. tabs::

```
```

    func _ready():
        var dialog = ScriptCreateDialog.new();
        dialog.config("Node", "res://new_node.gd") # For in-engine types.
        dialog.config("\"res://base_node.gd\"", "res://derived_node.gd") # For script types.
        dialog.popup_centered()

```
```

    public override void _Ready()
    {
        var dialog = new ScriptCreateDialog();
        dialog.Config("Node", "res://NewNode.cs"); // For in-engine types.
        dialog.Config("\"res://BaseNode.cs\"", "res://DerivedNode.cs"); // For script types.
        dialog.PopupCentered();
    }

### Properties


| [bool](class_bool.md#class_bool) | dialog_hide_on_ok | `false` (overrides [AcceptDialog](class_acceptdialog.md#class_AcceptDialog_property_dialog_hide_on_ok)) |
| --- | --- | --- |
| [String](class_string.md#class_String) | ok_button_text | `"Create"` (overrides [AcceptDialog](class_acceptdialog.md#class_AcceptDialog_property_ok_button_text)) |
| [String](class_string.md#class_String) | title | `"Attach Node Script"` (overrides [Window](class_window.md#class_Window_property_title)) |

### Methods


| void | [config](class_scriptcreatedialog.md#class_ScriptCreateDialog_method_config) ( inherits: [String](class_string.md#class_String), path: [String](class_string.md#class_String), built_in_enabled: [bool](class_bool.md#class_bool) = true, load_enabled: [bool](class_bool.md#class_bool) = true ) |
| --- | --- |

---

### Signals

<span id="class_ScriptCreateDialog_signal_script_created"></span>

**script_created** ( script: [Script](class_script.md#class_Script) ) [🔗](class_scriptcreatedialog.md#class_ScriptCreateDialog_signal_script_created)

Emitted when the user clicks the OK button.

---

### Method Descriptions

<span id="class_ScriptCreateDialog_method_config"></span>

void **config** ( inherits: [String](class_string.md#class_String), path: [String](class_string.md#class_String), built_in_enabled: [bool](class_bool.md#class_bool) = true, load_enabled: [bool](class_bool.md#class_bool) = true ) [🔗](class_scriptcreatedialog.md#class_ScriptCreateDialog_method_config)

Prefills required fields to configure the ScriptCreateDialog for use.
