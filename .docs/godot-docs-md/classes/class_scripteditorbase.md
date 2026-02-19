<span id="class_ScriptEditorBase"></span>

## ScriptEditorBase

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Base editor for editing scripts in the [ScriptEditor](class_scripteditor.md#class_ScriptEditor).

### Description

Base editor for editing scripts in the [ScriptEditor](class_scripteditor.md#class_ScriptEditor). This does not include documentation items.

### Methods


| void | [add_syntax_highlighter](class_scripteditorbase.md#class_ScriptEditorBase_method_add_syntax_highlighter) ( highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) ) |
| --- | --- |
| [Control](class_control.md#class_Control) | [get_base_editor](class_scripteditorbase.md#class_ScriptEditorBase_method_get_base_editor) ( ) const |

---

### Signals

<span id="class_ScriptEditorBase_signal_edited_script_changed"></span>

**edited_script_changed** ( ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_edited_script_changed)

Emitted after script validation.

---

<span id="class_ScriptEditorBase_signal_go_to_help"></span>

**go_to_help** ( what: [String](class_string.md#class_String) ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_go_to_help)

Emitted when the user requests a specific documentation page.

---

<span id="class_ScriptEditorBase_signal_go_to_method"></span>

**go_to_method** ( script: [Object](class_object.md#class_Object), method: [String](class_string.md#class_String) ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_go_to_method)

Emitted when the user requests to view a specific method of a script, similar to [request_open_script_at_line](class_scripteditorbase.md#class_ScriptEditorBase_signal_request_open_script_at_line).

---

<span id="class_ScriptEditorBase_signal_name_changed"></span>

**name_changed** ( ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_name_changed)

Emitted after script validation or when the edited resource has changed.

---

<span id="class_ScriptEditorBase_signal_replace_in_files_requested"></span>

**replace_in_files_requested** ( text: [String](class_string.md#class_String) ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_replace_in_files_requested)

Emitted when the user request to find and replace text in the file system.

---

<span id="class_ScriptEditorBase_signal_request_help"></span>

**request_help** ( topic: [String](class_string.md#class_String) ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_request_help)

Emitted when the user requests contextual help.

---

<span id="class_ScriptEditorBase_signal_request_open_script_at_line"></span>

**request_open_script_at_line** ( script: [Object](class_object.md#class_Object), line: [int](class_int.md#class_int) ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_request_open_script_at_line)

Emitted when the user requests to view a specific line of a script, similar to [go_to_method](class_scripteditorbase.md#class_ScriptEditorBase_signal_go_to_method).

---

<span id="class_ScriptEditorBase_signal_request_save_history"></span>

**request_save_history** ( ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_request_save_history)

Emitted when the user contextual goto and the item is in the same script.

---

<span id="class_ScriptEditorBase_signal_request_save_previous_state"></span>

**request_save_previous_state** ( state: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_request_save_previous_state)

Emitted when the user changes current script or moves caret by 10 or more columns within the same script.

---

<span id="class_ScriptEditorBase_signal_search_in_files_requested"></span>

**search_in_files_requested** ( text: [String](class_string.md#class_String) ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_signal_search_in_files_requested)

Emitted when the user request to search text in the file system.

---

### Method Descriptions

<span id="class_ScriptEditorBase_method_add_syntax_highlighter"></span>

void **add_syntax_highlighter** ( highlighter: [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) ) [🔗](class_scripteditorbase.md#class_ScriptEditorBase_method_add_syntax_highlighter)

Adds an [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) to the open script.

---

<span id="class_ScriptEditorBase_method_get_base_editor"></span>

[Control](class_control.md#class_Control) **get_base_editor** ( ) *const* [🔗](class_scripteditorbase.md#class_ScriptEditorBase_method_get_base_editor)

Returns the underlying [Control](class_control.md#class_Control) used for editing scripts. For text scripts, this is a [CodeEdit](class_codeedit.md#class_CodeEdit).
