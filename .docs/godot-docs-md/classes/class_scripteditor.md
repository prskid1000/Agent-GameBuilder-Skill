<span id="class_ScriptEditor"></span>

## ScriptEditor

**Inherits:** [PanelContainer](class_panelcontainer.md#class_PanelContainer) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Godot editor's script editor.

### Description

Godot editor's script editor.

 **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_script_editor()](class_editorinterface.md#class_EditorInterface_method_get_script_editor).

### Methods


| void | [clear_docs_from_script](class_scripteditor.md#class_ScriptEditor_method_clear_docs_from_script) ( script: [Script](class_script.md#class_Script) ) |
| --- | --- |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_breakpoints](class_scripteditor.md#class_ScriptEditor_method_get_breakpoints) ( ) |
| [ScriptEditorBase](class_scripteditorbase.md#class_ScriptEditorBase) | [get_current_editor](class_scripteditor.md#class_ScriptEditor_method_get_current_editor) ( ) const |
| [Script](class_script.md#class_Script) | [get_current_script](class_scripteditor.md#class_ScriptEditor_method_get_current_script) ( ) |
| [Array](class_array.md#class_Array)\[[ScriptEditorBase](class_scripteditorbase.md#class_ScriptEditorBase)\] | [get_open_script_editors](class_scripteditor.md#class_ScriptEditor_method_get_open_script_editors) ( ) const |
| [Array](class_array.md#class_Array)\[[Script](class_script.md#class_Script)\] | [get_open_scripts](class_scripteditor.md#class_ScriptEditor_method_get_open_scripts) ( ) const |
| void | [goto_help](class_scripteditor.md#class_ScriptEditor_method_goto_help) ( topic: [String](class_string.md#class_String) ) |
| void | [goto_line](class_scripteditor.md#class_ScriptEditor_method_goto_line) ( line_number: [int](class_int.md#class_int) ) |
| void | [open_script_create_dialog](class_scripteditor.md#class_ScriptEditor_method_open_script_create_dialog) ( base_name: [String](class_string.md#class_String), base_path: [String](class_string.md#class_String) ) |
| void | [register_syntax_highlighter](class_scripteditor.md#class_ScriptEditor_method_register_syntax_highlighter) ( syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) ) |
| void | [save_all_scripts](class_scripteditor.md#class_ScriptEditor_method_save_all_scripts) ( ) |
| void | [unregister_syntax_highlighter](class_scripteditor.md#class_ScriptEditor_method_unregister_syntax_highlighter) ( syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) ) |
| void | [update_docs_from_script](class_scripteditor.md#class_ScriptEditor_method_update_docs_from_script) ( script: [Script](class_script.md#class_Script) ) |

---

### Signals

<span id="class_ScriptEditor_signal_editor_script_changed"></span>

**editor_script_changed** ( script: [Script](class_script.md#class_Script) ) [🔗](class_scripteditor.md#class_ScriptEditor_signal_editor_script_changed)

Emitted when user changed active script. Argument is a freshly activated [Script](class_script.md#class_Script).

---

<span id="class_ScriptEditor_signal_script_close"></span>

**script_close** ( script: [Script](class_script.md#class_Script) ) [🔗](class_scripteditor.md#class_ScriptEditor_signal_script_close)

Emitted when editor is about to close the active script. Argument is a [Script](class_script.md#class_Script) that is going to be closed.

---

### Method Descriptions

<span id="class_ScriptEditor_method_clear_docs_from_script"></span>

void **clear_docs_from_script** ( script: [Script](class_script.md#class_Script) ) [🔗](class_scripteditor.md#class_ScriptEditor_method_clear_docs_from_script)

Removes the documentation for the given `script`.

 **Note:** This should be called whenever the script is changed to keep the open documentation state up to date.

---

<span id="class_ScriptEditor_method_get_breakpoints"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_breakpoints** ( ) [🔗](class_scripteditor.md#class_ScriptEditor_method_get_breakpoints)

Returns array of breakpoints.

---

<span id="class_ScriptEditor_method_get_current_editor"></span>

[ScriptEditorBase](class_scripteditorbase.md#class_ScriptEditorBase) **get_current_editor** ( ) *const* [🔗](class_scripteditor.md#class_ScriptEditor_method_get_current_editor)

Returns the [ScriptEditorBase](class_scripteditorbase.md#class_ScriptEditorBase) object that the user is currently editing.

---

<span id="class_ScriptEditor_method_get_current_script"></span>

[Script](class_script.md#class_Script) **get_current_script** ( ) [🔗](class_scripteditor.md#class_ScriptEditor_method_get_current_script)

Returns a [Script](class_script.md#class_Script) that is currently active in editor.

---

<span id="class_ScriptEditor_method_get_open_script_editors"></span>

[Array](class_array.md#class_Array)\[[ScriptEditorBase](class_scripteditorbase.md#class_ScriptEditorBase)\] **get_open_script_editors** ( ) *const* [🔗](class_scripteditor.md#class_ScriptEditor_method_get_open_script_editors)

Returns an array with all [ScriptEditorBase](class_scripteditorbase.md#class_ScriptEditorBase) objects which are currently open in editor.

---

<span id="class_ScriptEditor_method_get_open_scripts"></span>

[Array](class_array.md#class_Array)\[[Script](class_script.md#class_Script)\] **get_open_scripts** ( ) *const* [🔗](class_scripteditor.md#class_ScriptEditor_method_get_open_scripts)

Returns an array with all [Script](class_script.md#class_Script) objects which are currently open in editor.

---

<span id="class_ScriptEditor_method_goto_help"></span>

void **goto_help** ( topic: [String](class_string.md#class_String) ) [🔗](class_scripteditor.md#class_ScriptEditor_method_goto_help)

Opens help for the given topic. The `topic` is an encoded string that controls which class, method, constant, signal, annotation, property, or theme item should be focused.

The supported `topic` formats include `class_name:class`, `class_method:class:method`, `class_constant:class:constant`, `class_signal:class:signal`, `class_annotation:class:@annotation`, `class_property:class:property`, and `class_theme_item:class:item`, where `class` is the class name, `method` is the method name, `constant` is the constant name, `signal` is the signal name, `annotation` is the annotation name, `property` is the property name, and `item` is the theme item.

::

    # Shows help for the Node class.
    class_name:Node
    # Shows help for the global min function.
    # Global objects are accessible in the `@GlobalScope` namespace, shown here.
    class_method:@GlobalScope:min
    # Shows help for get_viewport in the Node class.
    class_method:Node:get_viewport
    # Shows help for the Input constant MOUSE_BUTTON_MIDDLE.
    class_constant:Input:MOUSE_BUTTON_MIDDLE
    # Shows help for the BaseButton signal pressed.
    class_signal:BaseButton:pressed
    # Shows help for the CanvasItem property visible.
    class_property:CanvasItem:visible
    # Shows help for the GDScript annotation export.
    # Annotations should be prefixed with the `@` symbol in the descriptor, as shown here.
    class_annotation:@GDScript:@export
    # Shows help for the GraphNode theme item named panel_selected.
    class_theme_item:GraphNode:panel_selected

---

<span id="class_ScriptEditor_method_goto_line"></span>

void **goto_line** ( line_number: [int](class_int.md#class_int) ) [🔗](class_scripteditor.md#class_ScriptEditor_method_goto_line)

Goes to the specified line in the current script.

---

<span id="class_ScriptEditor_method_open_script_create_dialog"></span>

void **open_script_create_dialog** ( base_name: [String](class_string.md#class_String), base_path: [String](class_string.md#class_String) ) [🔗](class_scripteditor.md#class_ScriptEditor_method_open_script_create_dialog)

Opens the script create dialog. The script will extend `base_name`. The file extension can be omitted from `base_path`. It will be added based on the selected scripting language.

---

<span id="class_ScriptEditor_method_register_syntax_highlighter"></span>

void **register_syntax_highlighter** ( syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) ) [🔗](class_scripteditor.md#class_ScriptEditor_method_register_syntax_highlighter)

Registers the [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) to the editor, the [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) will be available on all open scripts.

 **Note:** Does not apply to scripts that are already opened.

---

<span id="class_ScriptEditor_method_save_all_scripts"></span>

void **save_all_scripts** ( ) [🔗](class_scripteditor.md#class_ScriptEditor_method_save_all_scripts)

Saves all open scripts.

---

<span id="class_ScriptEditor_method_unregister_syntax_highlighter"></span>

void **unregister_syntax_highlighter** ( syntax_highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) ) [🔗](class_scripteditor.md#class_ScriptEditor_method_unregister_syntax_highlighter)

Unregisters the [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) from the editor.

 **Note:** The [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) will still be applied to scripts that are already opened.

---

<span id="class_ScriptEditor_method_update_docs_from_script"></span>

void **update_docs_from_script** ( script: [Script](class_script.md#class_Script) ) [🔗](class_scripteditor.md#class_ScriptEditor_method_update_docs_from_script)

Updates the documentation for the given `script`.

 **Note:** This should be called whenever the script is changed to keep the open documentation state up to date.
