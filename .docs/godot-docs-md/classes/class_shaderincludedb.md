<span id="class_ShaderIncludeDB"></span>

## ShaderIncludeDB

**Inherits:** [Object](class_object.md#class_Object)

Internal database of built in shader include files.

### Description

This object contains shader fragments from Godot's internal shaders. These can be used when access to internal uniform buffers and/or internal functions is required for instance when composing compositor effects or compute shaders. Only fragments for the current rendering device are loaded.

### Methods


| [String](class_string.md#class_String) | [get_built_in_include_file](class_shaderincludedb.md#class_ShaderIncludeDB_method_get_built_in_include_file) ( filename: [String](class_string.md#class_String) ) static |
| --- | --- |
| [bool](class_bool.md#class_bool) | [has_built_in_include_file](class_shaderincludedb.md#class_ShaderIncludeDB_method_has_built_in_include_file) ( filename: [String](class_string.md#class_String) ) static |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [list_built_in_include_files](class_shaderincludedb.md#class_ShaderIncludeDB_method_list_built_in_include_files) ( ) static |

---

### Method Descriptions

<span id="class_ShaderIncludeDB_method_get_built_in_include_file"></span>

[String](class_string.md#class_String) **get_built_in_include_file** ( filename: [String](class_string.md#class_String) ) *static* [🔗](class_shaderincludedb.md#class_ShaderIncludeDB_method_get_built_in_include_file)

Returns the code for the built-in shader fragment. You can also access this in your shader code through `#include "filename"`.

---

<span id="class_ShaderIncludeDB_method_has_built_in_include_file"></span>

[bool](class_bool.md#class_bool) **has_built_in_include_file** ( filename: [String](class_string.md#class_String) ) *static* [🔗](class_shaderincludedb.md#class_ShaderIncludeDB_method_has_built_in_include_file)

Returns `true` if an include file with this name exists.

---

<span id="class_ShaderIncludeDB_method_list_built_in_include_files"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **list_built_in_include_files** ( ) *static* [🔗](class_shaderincludedb.md#class_ShaderIncludeDB_method_list_built_in_include_files)

Returns a list of built-in include files that are currently registered.
