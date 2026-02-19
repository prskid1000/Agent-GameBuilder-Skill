<span id="class_EditorSyntaxHighlighter"></span>

## EditorSyntaxHighlighter

**Inherits:** [SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [GDScriptSyntaxHighlighter](class_gdscriptsyntaxhighlighter.md#class_GDScriptSyntaxHighlighter)

Base class for [SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) used by the [ScriptEditor](class_scripteditor.md#class_ScriptEditor).

### Description

Base class that all [SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) s used by the [ScriptEditor](class_scripteditor.md#class_ScriptEditor) extend from.

Add a syntax highlighter to an individual script by calling [ScriptEditorBase.add_syntax_highlighter()](class_scripteditorbase.md#class_ScriptEditorBase_method_add_syntax_highlighter). To apply to all scripts on open, call [ScriptEditor.register_syntax_highlighter()](class_scripteditor.md#class_ScriptEditor_method_register_syntax_highlighter).

### Methods


| [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) | [_create](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter_private_method__create) ( ) | virtual | const |
| --- | --- | --- | --- |
| [String](class_string.md#class_String) | [_get_name](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter_private_method__get_name) ( ) | virtual | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_supported_languages](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter_private_method__get_supported_languages) ( ) | virtual | const |

---

### Method Descriptions

<span id="class_EditorSyntaxHighlighter_private_method__create"></span>

[EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) **_create** ( ) *virtual* *const* [🔗](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter_private_method__create)

Virtual method which creates a new instance of the syntax highlighter.

---

<span id="class_EditorSyntaxHighlighter_private_method__get_name"></span>

[String](class_string.md#class_String) **_get_name** ( ) *virtual* *const* [🔗](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter_private_method__get_name)

Virtual method which can be overridden to return the syntax highlighter name.

---

<span id="class_EditorSyntaxHighlighter_private_method__get_supported_languages"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_supported_languages** ( ) *virtual* *const* [🔗](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter_private_method__get_supported_languages)

Virtual method which can be overridden to return the supported language names.
