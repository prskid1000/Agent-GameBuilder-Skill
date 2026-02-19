<span id="class_SyntaxHighlighter"></span>

## SyntaxHighlighter

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CodeHighlighter](class_codehighlighter.md#class_CodeHighlighter), [EditorSyntaxHighlighter](class_editorsyntaxhighlighter.md#class_EditorSyntaxHighlighter)

Base class for syntax highlighters. Provides syntax highlighting data to a [TextEdit](class_textedit.md#class_TextEdit).

### Description

Base class for syntax highlighters. Provides syntax highlighting data to a [TextEdit](class_textedit.md#class_TextEdit). The associated [TextEdit](class_textedit.md#class_TextEdit) will call into the **SyntaxHighlighter** on an as-needed basis.

 **Note:** A **SyntaxHighlighter** instance should not be used across multiple [TextEdit](class_textedit.md#class_TextEdit) nodes.

### Methods


| void | [_clear_highlighting_cache](class_syntaxhighlighter.md#class_SyntaxHighlighter_private_method__clear_highlighting_cache) ( ) virtual |
| --- | --- |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_line_syntax_highlighting](class_syntaxhighlighter.md#class_SyntaxHighlighter_private_method__get_line_syntax_highlighting) ( line: [int](class_int.md#class_int) ) | virtual | const |
| void | [_update_cache](class_syntaxhighlighter.md#class_SyntaxHighlighter_private_method__update_cache) ( ) virtual |
| void | [clear_highlighting_cache](class_syntaxhighlighter.md#class_SyntaxHighlighter_method_clear_highlighting_cache) ( ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_line_syntax_highlighting](class_syntaxhighlighter.md#class_SyntaxHighlighter_method_get_line_syntax_highlighting) ( line: [int](class_int.md#class_int) ) |
| [TextEdit](class_textedit.md#class_TextEdit) | [get_text_edit](class_syntaxhighlighter.md#class_SyntaxHighlighter_method_get_text_edit) ( ) const |
| void | [update_cache](class_syntaxhighlighter.md#class_SyntaxHighlighter_method_update_cache) ( ) |

---

### Method Descriptions

<span id="class_SyntaxHighlighter_private_method__clear_highlighting_cache"></span>

void **_clear_highlighting_cache** ( ) *virtual* [🔗](class_syntaxhighlighter.md#class_SyntaxHighlighter_private_method__clear_highlighting_cache)

Virtual method which can be overridden to clear any local caches.

---

<span id="class_SyntaxHighlighter_private_method__get_line_syntax_highlighting"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_line_syntax_highlighting** ( line: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_syntaxhighlighter.md#class_SyntaxHighlighter_private_method__get_line_syntax_highlighting)

Virtual method which can be overridden to return syntax highlighting data.

See [get_line_syntax_highlighting()](class_syntaxhighlighter.md#class_SyntaxHighlighter_method_get_line_syntax_highlighting) for more details.

---

<span id="class_SyntaxHighlighter_private_method__update_cache"></span>

void **_update_cache** ( ) *virtual* [🔗](class_syntaxhighlighter.md#class_SyntaxHighlighter_private_method__update_cache)

Virtual method which can be overridden to update any local caches.

---

<span id="class_SyntaxHighlighter_method_clear_highlighting_cache"></span>

void **clear_highlighting_cache** ( ) [🔗](class_syntaxhighlighter.md#class_SyntaxHighlighter_method_clear_highlighting_cache)

Clears all cached syntax highlighting data.

Then calls overridable method [_clear_highlighting_cache()](class_syntaxhighlighter.md#class_SyntaxHighlighter_private_method__clear_highlighting_cache).

---

<span id="class_SyntaxHighlighter_method_get_line_syntax_highlighting"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_line_syntax_highlighting** ( line: [int](class_int.md#class_int) ) [🔗](class_syntaxhighlighter.md#class_SyntaxHighlighter_method_get_line_syntax_highlighting)

Returns the syntax highlighting data for the line at index `line`. If the line is not cached, calls [_get_line_syntax_highlighting()](class_syntaxhighlighter.md#class_SyntaxHighlighter_private_method__get_line_syntax_highlighting) first to calculate the data.

Each entry is a column number containing a nested [Dictionary](class_dictionary.md#class_Dictionary). The column number denotes the start of a region, the region will end if another region is found, or at the end of the line. The nested [Dictionary](class_dictionary.md#class_Dictionary) contains the data for that region. Currently only the key `"color"` is supported.

 **Example:** Possible return value. This means columns `0` to `4` should be red, and columns `5` to the end of the line should be green:

::

    {
        0: {
            "color": Color(1, 0, 0)
        },
        5: {
            "color": Color(0, 1, 0)
        }
    }

---

<span id="class_SyntaxHighlighter_method_get_text_edit"></span>

[TextEdit](class_textedit.md#class_TextEdit) **get_text_edit** ( ) *const* [🔗](class_syntaxhighlighter.md#class_SyntaxHighlighter_method_get_text_edit)

Returns the associated [TextEdit](class_textedit.md#class_TextEdit) node.

---

<span id="class_SyntaxHighlighter_method_update_cache"></span>

void **update_cache** ( ) [🔗](class_syntaxhighlighter.md#class_SyntaxHighlighter_method_update_cache)

Clears then updates the **SyntaxHighlighter** caches. Override [_update_cache()](class_syntaxhighlighter.md#class_SyntaxHighlighter_private_method__update_cache) for a callback.

 **Note:** This is called automatically when the associated [TextEdit](class_textedit.md#class_TextEdit) node, updates its own cache.
