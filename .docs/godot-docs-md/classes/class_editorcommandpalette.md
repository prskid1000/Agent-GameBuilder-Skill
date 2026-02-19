<span id="class_EditorCommandPalette"></span>

## EditorCommandPalette

**Inherits:** [ConfirmationDialog](class_confirmationdialog.md#class_ConfirmationDialog) **<** [AcceptDialog](class_acceptdialog.md#class_AcceptDialog) **<** [Window](class_window.md#class_Window) **<** [Viewport](class_viewport.md#class_Viewport) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Godot editor's command palette.

### Description

Object that holds all the available Commands and their shortcuts text. These Commands can be accessed through **Editor > Command Palette** menu.

Command key names use slash delimiters to distinguish sections, for example: `"example/command1"` then `example` will be the section name.

.. tabs::

```
```

    var command_palette = EditorInterface.get_command_palette()
    # external_command is a function that will be called with the command is executed.
    var command_callable = Callable(self, "external_command").bind(arguments)
    command_palette.add_command("command", "test/command",command_callable)

```
```

    EditorCommandPalette commandPalette = EditorInterface.Singleton.GetCommandPalette();
    // ExternalCommand is a function that will be called with the command is executed.
    Callable commandCallable = new Callable(this, MethodName.ExternalCommand);
    commandPalette.AddCommand("command", "test/command", commandCallable)

 **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_command_palette()](class_editorinterface.md#class_EditorInterface_method_get_command_palette).

### Properties


| [bool](class_bool.md#class_bool) | dialog_hide_on_ok | `false` (overrides [AcceptDialog](class_acceptdialog.md#class_AcceptDialog_property_dialog_hide_on_ok)) |
| --- | --- | --- |

### Methods


| void | [add_command](class_editorcommandpalette.md#class_EditorCommandPalette_method_add_command) ( command_name: [String](class_string.md#class_String), key_name: [String](class_string.md#class_String), binded_callable: [Callable](class_callable.md#class_Callable), shortcut_text: [String](class_string.md#class_String) = "None" ) |
| --- | --- |
| void | [remove_command](class_editorcommandpalette.md#class_EditorCommandPalette_method_remove_command) ( key_name: [String](class_string.md#class_String) ) |

---

### Method Descriptions

<span id="class_EditorCommandPalette_method_add_command"></span>

void **add_command** ( command_name: [String](class_string.md#class_String), key_name: [String](class_string.md#class_String), binded_callable: [Callable](class_callable.md#class_Callable), shortcut_text: [String](class_string.md#class_String) = "None" ) [🔗](class_editorcommandpalette.md#class_EditorCommandPalette_method_add_command)

Adds a custom command to EditorCommandPalette.

- `command_name`: [String](class_string.md#class_String) (Name of the **Command**. This is displayed to the user.)

- `key_name`: [String](class_string.md#class_String) (Name of the key for a particular **Command**. This is used to uniquely identify the **Command**.)

- `binded_callable`: [Callable](class_callable.md#class_Callable) (Callable of the **Command**. This will be executed when the **Command** is selected.)

- `shortcut_text`: [String](class_string.md#class_String) (Shortcut text of the **Command** if available.)

---

<span id="class_EditorCommandPalette_method_remove_command"></span>

void **remove_command** ( key_name: [String](class_string.md#class_String) ) [🔗](class_editorcommandpalette.md#class_EditorCommandPalette_method_remove_command)

Removes the custom command from EditorCommandPalette.

- `key_name`: [String](class_string.md#class_String) (Name of the key for a particular **Command**.)
