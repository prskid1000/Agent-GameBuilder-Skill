<span id="class_CodeHighlighter"></span>

## CodeHighlighter

**Inherits:** [SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A syntax highlighter intended for code.

### Description

By adjusting various properties of this resource, you can change the colors of strings, comments, numbers, and other text patterns inside a [TextEdit](class_textedit.md#class_TextEdit) control.

### Properties


| [Dictionary](class_dictionary.md#class_Dictionary) | [color_regions](class_codehighlighter.md#class_CodeHighlighter_property_color_regions) | `{}` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [function_color](class_codehighlighter.md#class_CodeHighlighter_property_function_color) | `Color(0, 0, 0, 1)` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [keyword_colors](class_codehighlighter.md#class_CodeHighlighter_property_keyword_colors) | `{}` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [member_keyword_colors](class_codehighlighter.md#class_CodeHighlighter_property_member_keyword_colors) | `{}` |
| [Color](class_color.md#class_Color) | [member_variable_color](class_codehighlighter.md#class_CodeHighlighter_property_member_variable_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [number_color](class_codehighlighter.md#class_CodeHighlighter_property_number_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [symbol_color](class_codehighlighter.md#class_CodeHighlighter_property_symbol_color) | `Color(0, 0, 0, 1)` |

### Methods


| void | [add_color_region](class_codehighlighter.md#class_CodeHighlighter_method_add_color_region) ( start_key: [String](class_string.md#class_String), end_key: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color), line_only: [bool](class_bool.md#class_bool) = false ) |
| --- | --- |
| void | [add_keyword_color](class_codehighlighter.md#class_CodeHighlighter_method_add_keyword_color) ( keyword: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color) ) |
| void | [add_member_keyword_color](class_codehighlighter.md#class_CodeHighlighter_method_add_member_keyword_color) ( member_keyword: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color) ) |
| void | [clear_color_regions](class_codehighlighter.md#class_CodeHighlighter_method_clear_color_regions) ( ) |
| void | [clear_keyword_colors](class_codehighlighter.md#class_CodeHighlighter_method_clear_keyword_colors) ( ) |
| void | [clear_member_keyword_colors](class_codehighlighter.md#class_CodeHighlighter_method_clear_member_keyword_colors) ( ) |
| [Color](class_color.md#class_Color) | [get_keyword_color](class_codehighlighter.md#class_CodeHighlighter_method_get_keyword_color) ( keyword: [String](class_string.md#class_String) ) const |
| [Color](class_color.md#class_Color) | [get_member_keyword_color](class_codehighlighter.md#class_CodeHighlighter_method_get_member_keyword_color) ( member_keyword: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [has_color_region](class_codehighlighter.md#class_CodeHighlighter_method_has_color_region) ( start_key: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [has_keyword_color](class_codehighlighter.md#class_CodeHighlighter_method_has_keyword_color) ( keyword: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [has_member_keyword_color](class_codehighlighter.md#class_CodeHighlighter_method_has_member_keyword_color) ( member_keyword: [String](class_string.md#class_String) ) const |
| void | [remove_color_region](class_codehighlighter.md#class_CodeHighlighter_method_remove_color_region) ( start_key: [String](class_string.md#class_String) ) |
| void | [remove_keyword_color](class_codehighlighter.md#class_CodeHighlighter_method_remove_keyword_color) ( keyword: [String](class_string.md#class_String) ) |
| void | [remove_member_keyword_color](class_codehighlighter.md#class_CodeHighlighter_method_remove_member_keyword_color) ( member_keyword: [String](class_string.md#class_String) ) |

---

### Property Descriptions

<span id="class_CodeHighlighter_property_color_regions"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **color_regions** = `{}` [🔗](class_codehighlighter.md#class_CodeHighlighter_property_color_regions)

- void **set_color_regions** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_color_regions** ( )

Sets the color regions. All existing regions will be removed. The [Dictionary](class_dictionary.md#class_Dictionary) key is the region start and end key, separated by a space. The value is the region color.

---

<span id="class_CodeHighlighter_property_function_color"></span>

[Color](class_color.md#class_Color) **function_color** = `Color(0, 0, 0, 1)` [🔗](class_codehighlighter.md#class_CodeHighlighter_property_function_color)

- void **set_function_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_function_color** ( )

Sets color for functions. A function is a non-keyword string followed by a '('.

---

<span id="class_CodeHighlighter_property_keyword_colors"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **keyword_colors** = `{}` [🔗](class_codehighlighter.md#class_CodeHighlighter_property_keyword_colors)

- void **set_keyword_colors** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_keyword_colors** ( )

Sets the keyword colors. All existing keywords will be removed. The [Dictionary](class_dictionary.md#class_Dictionary) key is the keyword. The value is the keyword color.

---

<span id="class_CodeHighlighter_property_member_keyword_colors"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **member_keyword_colors** = `{}` [🔗](class_codehighlighter.md#class_CodeHighlighter_property_member_keyword_colors)

- void **set_member_keyword_colors** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_member_keyword_colors** ( )

Sets the member keyword colors. All existing member keyword will be removed. The [Dictionary](class_dictionary.md#class_Dictionary) key is the member keyword. The value is the member keyword color.

---

<span id="class_CodeHighlighter_property_member_variable_color"></span>

[Color](class_color.md#class_Color) **member_variable_color** = `Color(0, 0, 0, 1)` [🔗](class_codehighlighter.md#class_CodeHighlighter_property_member_variable_color)

- void **set_member_variable_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_member_variable_color** ( )

Sets color for member variables. A member variable is non-keyword, non-function string proceeded with a '.'.

---

<span id="class_CodeHighlighter_property_number_color"></span>

[Color](class_color.md#class_Color) **number_color** = `Color(0, 0, 0, 1)` [🔗](class_codehighlighter.md#class_CodeHighlighter_property_number_color)

- void **set_number_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_number_color** ( )

Sets the color for numbers.

---

<span id="class_CodeHighlighter_property_symbol_color"></span>

[Color](class_color.md#class_Color) **symbol_color** = `Color(0, 0, 0, 1)` [🔗](class_codehighlighter.md#class_CodeHighlighter_property_symbol_color)

- void **set_symbol_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_symbol_color** ( )

Sets the color for symbols.

---

### Method Descriptions

<span id="class_CodeHighlighter_method_add_color_region"></span>

void **add_color_region** ( start_key: [String](class_string.md#class_String), end_key: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color), line_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_codehighlighter.md#class_CodeHighlighter_method_add_color_region)

Adds a color region (such as for comments or strings) from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty [String](class_string.md#class_String), the region does not carry over to the next line.

---

<span id="class_CodeHighlighter_method_add_keyword_color"></span>

void **add_keyword_color** ( keyword: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color) ) [🔗](class_codehighlighter.md#class_CodeHighlighter_method_add_keyword_color)

Sets the color for a keyword.

The keyword cannot contain any symbols except '\_'.

---

<span id="class_CodeHighlighter_method_add_member_keyword_color"></span>

void **add_member_keyword_color** ( member_keyword: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color) ) [🔗](class_codehighlighter.md#class_CodeHighlighter_method_add_member_keyword_color)

Sets the color for a member keyword.

The member keyword cannot contain any symbols except '\_'.

It will not be highlighted if preceded by a '.'.

---

<span id="class_CodeHighlighter_method_clear_color_regions"></span>

void **clear_color_regions** ( ) [🔗](class_codehighlighter.md#class_CodeHighlighter_method_clear_color_regions)

Removes all color regions.

---

<span id="class_CodeHighlighter_method_clear_keyword_colors"></span>

void **clear_keyword_colors** ( ) [🔗](class_codehighlighter.md#class_CodeHighlighter_method_clear_keyword_colors)

Removes all keywords.

---

<span id="class_CodeHighlighter_method_clear_member_keyword_colors"></span>

void **clear_member_keyword_colors** ( ) [🔗](class_codehighlighter.md#class_CodeHighlighter_method_clear_member_keyword_colors)

Removes all member keywords.

---

<span id="class_CodeHighlighter_method_get_keyword_color"></span>

[Color](class_color.md#class_Color) **get_keyword_color** ( keyword: [String](class_string.md#class_String) ) *const* [🔗](class_codehighlighter.md#class_CodeHighlighter_method_get_keyword_color)

Returns the color for a keyword.

---

<span id="class_CodeHighlighter_method_get_member_keyword_color"></span>

[Color](class_color.md#class_Color) **get_member_keyword_color** ( member_keyword: [String](class_string.md#class_String) ) *const* [🔗](class_codehighlighter.md#class_CodeHighlighter_method_get_member_keyword_color)

Returns the color for a member keyword.

---

<span id="class_CodeHighlighter_method_has_color_region"></span>

[bool](class_bool.md#class_bool) **has_color_region** ( start_key: [String](class_string.md#class_String) ) *const* [🔗](class_codehighlighter.md#class_CodeHighlighter_method_has_color_region)

Returns `true` if the start key exists, else `false`.

---

<span id="class_CodeHighlighter_method_has_keyword_color"></span>

[bool](class_bool.md#class_bool) **has_keyword_color** ( keyword: [String](class_string.md#class_String) ) *const* [🔗](class_codehighlighter.md#class_CodeHighlighter_method_has_keyword_color)

Returns `true` if the keyword exists, else `false`.

---

<span id="class_CodeHighlighter_method_has_member_keyword_color"></span>

[bool](class_bool.md#class_bool) **has_member_keyword_color** ( member_keyword: [String](class_string.md#class_String) ) *const* [🔗](class_codehighlighter.md#class_CodeHighlighter_method_has_member_keyword_color)

Returns `true` if the member keyword exists, else `false`.

---

<span id="class_CodeHighlighter_method_remove_color_region"></span>

void **remove_color_region** ( start_key: [String](class_string.md#class_String) ) [🔗](class_codehighlighter.md#class_CodeHighlighter_method_remove_color_region)

Removes the color region that uses that start key.

---

<span id="class_CodeHighlighter_method_remove_keyword_color"></span>

void **remove_keyword_color** ( keyword: [String](class_string.md#class_String) ) [🔗](class_codehighlighter.md#class_CodeHighlighter_method_remove_keyword_color)

Removes the keyword.

---

<span id="class_CodeHighlighter_method_remove_member_keyword_color"></span>

void **remove_member_keyword_color** ( member_keyword: [String](class_string.md#class_String) ) [🔗](class_codehighlighter.md#class_CodeHighlighter_method_remove_member_keyword_color)

Removes the member keyword.
