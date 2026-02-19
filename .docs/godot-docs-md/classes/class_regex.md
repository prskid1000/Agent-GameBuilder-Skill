<span id="class_RegEx"></span>

## RegEx

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Class for searching text for patterns using regular expressions.

### Description

A regular expression (or regex) is a compact language that can be used to recognize strings that follow a specific pattern, such as URLs, email addresses, complete sentences, etc. For example, a regex of `ab[0-9]` would find any string that is `ab` followed by any number from `0` to `9`. For a more in-depth look, you can easily find various tutorials and detailed explanations on the Internet.

To begin, the RegEx object needs to be compiled with the search pattern using [compile()](class_regex.md#class_RegEx_method_compile) before it can be used. Alternatively, the static method [create_from_string()](class_regex.md#class_RegEx_method_create_from_string) can be used to create and compile a RegEx object in a single method call.

::

    var regex = RegEx.new()
    regex.compile("\\w-(\\d+)")
    # Shorthand to create and compile a regex (used in the examples below):
    var regex2 = RegEx.create_from_string("\\w-(\\d+)")

The search pattern must be escaped first for GDScript before it is escaped for the expression. For example, `compile("\\d+")` would be read by RegEx as `\d+`. Similarly, `compile("\"(?:\\\\.|[^\"])*\"")` would be read as `"(?:\\.|[^"])*"`. In GDScript, you can also use raw string literals (r-strings). For example, `compile(r'"(?:\\.|[^"])*"')` would be read the same.

Using [search()](class_regex.md#class_RegEx_method_search), you can find the pattern within the given text. If a pattern is found, [RegExMatch](class_regexmatch.md#class_RegExMatch) is returned and you can retrieve details of the results using methods such as [RegExMatch.get_string()](class_regexmatch.md#class_RegExMatch_method_get_string) and [RegExMatch.get_start()](class_regexmatch.md#class_RegExMatch_method_get_start).

::

    var regex = RegEx.create_from_string("\\w-(\\d+)")
    var result = regex.search("abc n-0123")
    if result:
        print(result.get_string()) # Prints "n-0123"

The results of capturing groups `()` can be retrieved by passing the group number to the various methods in [RegExMatch](class_regexmatch.md#class_RegExMatch). Group 0 is the default and will always refer to the entire pattern. In the above example, calling `result.get_string(1)` would give you `0123`.

This version of RegEx also supports named capturing groups, and the names can be used to retrieve the results. If two or more groups have the same name, the name would only refer to the first one with a match.

::

    var regex = RegEx.create_from_string("d(?<digit>[0-9]+)|x(?<digit>[0-9a-f]+)")
    var result = regex.search("the number is x2f")
    if result:
        print(result.get_string("digit")) # Prints "2f"

If you need to process multiple results, [search_all()](class_regex.md#class_RegEx_method_search_all) generates a list of all non-overlapping results. This can be combined with a `for` loop for convenience.

::

    # Prints "01 03 0 3f 42"
    for result in regex.search_all("d01, d03, d0c, x3f and x42"):
        print(result.get_string("digit"))

 **Example:** Split a string using a RegEx:

::

    var regex = RegEx.create_from_string("\\S+") # Negated whitespace character class.
    var results = []
    for result in regex.search_all("One  Two \n\tThree"):
        results.push_back(result.get_string())
    print(results) # Prints ["One", "Two", "Three"]

 **Note:** Godot's regex implementation is based on the PCRE2 library. You can view the full pattern reference here.

 **Tip:** You can use Regexr to test regular expressions online.

### Methods


| void | [clear](class_regex.md#class_RegEx_method_clear) ( ) |
| --- | --- |
| Error | [compile](class_regex.md#class_RegEx_method_compile) ( pattern: [String](class_string.md#class_String), show_error: [bool](class_bool.md#class_bool) = true ) |
| [RegEx](class_regex.md#class_RegEx) | [create_from_string](class_regex.md#class_RegEx_method_create_from_string) ( pattern: [String](class_string.md#class_String), show_error: [bool](class_bool.md#class_bool) = true ) static |
| [int](class_int.md#class_int) | [get_group_count](class_regex.md#class_RegEx_method_get_group_count) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_names](class_regex.md#class_RegEx_method_get_names) ( ) const |
| [String](class_string.md#class_String) | [get_pattern](class_regex.md#class_RegEx_method_get_pattern) ( ) const |
| [bool](class_bool.md#class_bool) | [is_valid](class_regex.md#class_RegEx_method_is_valid) ( ) const |
| [RegExMatch](class_regexmatch.md#class_RegExMatch) | [search](class_regex.md#class_RegEx_method_search) ( subject: [String](class_string.md#class_String), offset: [int](class_int.md#class_int) = 0, end: [int](class_int.md#class_int) = -1 ) const |
| [Array](class_array.md#class_Array)\[[RegExMatch](class_regexmatch.md#class_RegExMatch)\] | [search_all](class_regex.md#class_RegEx_method_search_all) ( subject: [String](class_string.md#class_String), offset: [int](class_int.md#class_int) = 0, end: [int](class_int.md#class_int) = -1 ) const |
| [String](class_string.md#class_String) | [sub](class_regex.md#class_RegEx_method_sub) ( subject: [String](class_string.md#class_String), replacement: [String](class_string.md#class_String), all: [bool](class_bool.md#class_bool) = false, offset: [int](class_int.md#class_int) = 0, end: [int](class_int.md#class_int) = -1 ) const |

---

### Method Descriptions

<span id="class_RegEx_method_clear"></span>

void **clear** ( ) [🔗](class_regex.md#class_RegEx_method_clear)

This method resets the state of the object, as if it was freshly created. Namely, it unassigns the regular expression of this object.

---

<span id="class_RegEx_method_compile"></span>

Error **compile** ( pattern: [String](class_string.md#class_String), show_error: [bool](class_bool.md#class_bool) = true ) [🔗](class_regex.md#class_RegEx_method_compile)

Compiles and assign the search pattern to use. Returns @GlobalScope.OK if the compilation is successful. If compilation fails, returns @GlobalScope.FAILED and when `show_error` is `true`, details are printed to standard output.

---

<span id="class_RegEx_method_create_from_string"></span>

[RegEx](class_regex.md#class_RegEx) **create_from_string** ( pattern: [String](class_string.md#class_String), show_error: [bool](class_bool.md#class_bool) = true ) *static* [🔗](class_regex.md#class_RegEx_method_create_from_string)

Creates and compiles a new **RegEx** object. See also [compile()](class_regex.md#class_RegEx_method_compile).

---

<span id="class_RegEx_method_get_group_count"></span>

[int](class_int.md#class_int) **get_group_count** ( ) *const* [🔗](class_regex.md#class_RegEx_method_get_group_count)

Returns the number of capturing groups in compiled pattern.

---

<span id="class_RegEx_method_get_names"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_names** ( ) *const* [🔗](class_regex.md#class_RegEx_method_get_names)

Returns an array of names of named capturing groups in the compiled pattern. They are ordered by appearance.

---

<span id="class_RegEx_method_get_pattern"></span>

[String](class_string.md#class_String) **get_pattern** ( ) *const* [🔗](class_regex.md#class_RegEx_method_get_pattern)

Returns the original search pattern that was compiled.

---

<span id="class_RegEx_method_is_valid"></span>

[bool](class_bool.md#class_bool) **is_valid** ( ) *const* [🔗](class_regex.md#class_RegEx_method_is_valid)

Returns whether this object has a valid search pattern assigned.

---

<span id="class_RegEx_method_search"></span>

[RegExMatch](class_regexmatch.md#class_RegExMatch) **search** ( subject: [String](class_string.md#class_String), offset: [int](class_int.md#class_int) = 0, end: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_regex.md#class_RegEx_method_search)

Searches the text for the compiled pattern. Returns a [RegExMatch](class_regexmatch.md#class_RegExMatch) container of the first matching result if found, otherwise `null`.

The region to search within can be specified with `offset` and `end`. This is useful when searching for another match in the same `subject` by calling this method again after a previous success. Note that setting these parameters differs from passing over a shortened string. For example, the start anchor `^` is not affected by `offset`, and the character before `offset` will be checked for the word boundary `\b`.

---

<span id="class_RegEx_method_search_all"></span>

[Array](class_array.md#class_Array)\[[RegExMatch](class_regexmatch.md#class_RegExMatch)\] **search_all** ( subject: [String](class_string.md#class_String), offset: [int](class_int.md#class_int) = 0, end: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_regex.md#class_RegEx_method_search_all)

Searches the text for the compiled pattern. Returns an array of [RegExMatch](class_regexmatch.md#class_RegExMatch) containers for each non-overlapping result. If no results were found, an empty array is returned instead.

The region to search within can be specified with `offset` and `end`. This is useful when searching for another match in the same `subject` by calling this method again after a previous success. Note that setting these parameters differs from passing over a shortened string. For example, the start anchor `^` is not affected by `offset`, and the character before `offset` will be checked for the word boundary `\b`.

---

<span id="class_RegEx_method_sub"></span>

[String](class_string.md#class_String) **sub** ( subject: [String](class_string.md#class_String), replacement: [String](class_string.md#class_String), all: [bool](class_bool.md#class_bool) = false, offset: [int](class_int.md#class_int) = 0, end: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_regex.md#class_RegEx_method_sub)

Searches the text for the compiled pattern and replaces it with the specified string. Escapes and backreferences such as `$1` and `$name` are expanded and resolved. By default, only the first instance is replaced, but it can be changed for all instances (global replacement).

The region to search within can be specified with `offset` and `end`. This is useful when searching for another match in the same `subject` by calling this method again after a previous success. Note that setting these parameters differs from passing over a shortened string. For example, the start anchor `^` is not affected by `offset`, and the character before `offset` will be checked for the word boundary `\b`.
