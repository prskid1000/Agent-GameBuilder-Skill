<span id="class_RegExMatch"></span>

## RegExMatch

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Contains the results of a [RegEx](class_regex.md#class_RegEx) search.

### Description

Contains the results of a single [RegEx](class_regex.md#class_RegEx) match returned by [RegEx.search()](class_regex.md#class_RegEx_method_search) and [RegEx.search_all()](class_regex.md#class_RegEx_method_search_all). It can be used to find the position and range of the match and its capturing groups, and it can extract its substring for you.

### Properties


| [Dictionary](class_dictionary.md#class_Dictionary) | [names](class_regexmatch.md#class_RegExMatch_property_names) | `{}` |
| --- | --- | --- |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [strings](class_regexmatch.md#class_RegExMatch_property_strings) | `PackedStringArray()` |
| [String](class_string.md#class_String) | [subject](class_regexmatch.md#class_RegExMatch_property_subject) | `""` |

### Methods


| [int](class_int.md#class_int) | [get_end](class_regexmatch.md#class_RegExMatch_method_get_end) ( name: [Variant](class_variant.md#class_Variant) = 0 ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_group_count](class_regexmatch.md#class_RegExMatch_method_get_group_count) ( ) const |
| [int](class_int.md#class_int) | [get_start](class_regexmatch.md#class_RegExMatch_method_get_start) ( name: [Variant](class_variant.md#class_Variant) = 0 ) const |
| [String](class_string.md#class_String) | [get_string](class_regexmatch.md#class_RegExMatch_method_get_string) ( name: [Variant](class_variant.md#class_Variant) = 0 ) const |

---

### Property Descriptions

<span id="class_RegExMatch_property_names"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **names** = `{}` [🔗](class_regexmatch.md#class_RegExMatch_property_names)

- [Dictionary](class_dictionary.md#class_Dictionary) **get_names** ( )

A dictionary of named groups and its corresponding group number. Only groups that were matched are included. If multiple groups have the same name, that name would refer to the first matching one.

---

<span id="class_RegExMatch_property_strings"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **strings** = `PackedStringArray()` [🔗](class_regexmatch.md#class_RegExMatch_property_strings)

- [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_strings** ( )

An [Array](class_array.md#class_Array) of the match and its capturing groups.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

<span id="class_RegExMatch_property_subject"></span>

[String](class_string.md#class_String) **subject** = `""` [🔗](class_regexmatch.md#class_RegExMatch_property_subject)

- [String](class_string.md#class_String) **get_subject** ( )

The source string used with the search pattern to find this matching result.

---

### Method Descriptions

<span id="class_RegExMatch_method_get_end"></span>

[int](class_int.md#class_int) **get_end** ( name: [Variant](class_variant.md#class_Variant) = 0 ) *const* [🔗](class_regexmatch.md#class_RegExMatch_method_get_end)

Returns the end position of the match within the source string. The end position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.

---

<span id="class_RegExMatch_method_get_group_count"></span>

[int](class_int.md#class_int) **get_group_count** ( ) *const* [🔗](class_regexmatch.md#class_RegExMatch_method_get_group_count)

Returns the number of capturing groups.

---

<span id="class_RegExMatch_method_get_start"></span>

[int](class_int.md#class_int) **get_start** ( name: [Variant](class_variant.md#class_Variant) = 0 ) *const* [🔗](class_regexmatch.md#class_RegExMatch_method_get_start)

Returns the starting position of the match within the source string. The starting position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.

---

<span id="class_RegExMatch_method_get_string"></span>

[String](class_string.md#class_String) **get_string** ( name: [Variant](class_variant.md#class_Variant) = 0 ) *const* [🔗](class_regexmatch.md#class_RegExMatch_method_get_string)

Returns the substring of the match from the source string. Capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns an empty string if the group did not match or doesn't exist.
