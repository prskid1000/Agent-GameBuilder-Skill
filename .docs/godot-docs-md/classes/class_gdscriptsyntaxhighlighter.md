<span id="class_GDScriptSyntaxHighlighter"></span>

## GDScriptSyntaxHighlighter

**Inherits:** [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter) **<** [SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A GDScript syntax highlighter that can be used with [TextEdit](class_textedit.md#class_TextEdit) and [CodeEdit](class_codeedit.md#class_CodeEdit) nodes.

### Description

**Note:** This class can only be used for editor plugins because it relies on editor settings.

.. tabs::

```
```

    var code_preview = TextEdit.new()
    var highlighter = GDScriptSyntaxHighlighter.new()
    code_preview.syntax_highlighter = highlighter

```
```

    var codePreview = new TextEdit();
    var highlighter = new GDScriptSyntaxHighlighter();
    codePreview.SyntaxHighlighter = highlighter;
