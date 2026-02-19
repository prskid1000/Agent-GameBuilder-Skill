<span id="class_EditorFileSystemDirectory"></span>

## EditorFileSystemDirectory

**Inherits:** [Object](class_object.md#class_Object)

A directory for the resource filesystem.

### Description

A more generalized, low-level variation of the directory concept.

### Methods


| [int](class_int.md#class_int) | [find_dir_index](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_find_dir_index) ( name: [String](class_string.md#class_String) ) const |
| --- | --- |
| [int](class_int.md#class_int) | [find_file_index](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_find_file_index) ( name: [String](class_string.md#class_String) ) const |
| [String](class_string.md#class_String) | [get_file](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_file_count](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_count) ( ) const |
| [bool](class_bool.md#class_bool) | [get_file_import_is_valid](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_import_is_valid) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_file_path](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_path) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_file_script_class_extends](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_script_class_extends) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_file_script_class_name](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_script_class_name) ( idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_file_type](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_type) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_name](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_name) ( ) |
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory) | [get_parent](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_parent) ( ) |
| [String](class_string.md#class_String) | [get_path](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_path) ( ) const |
| [EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory) | [get_subdir](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_subdir) ( idx: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_subdir_count](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_subdir_count) ( ) const |

---

### Method Descriptions

<span id="class_EditorFileSystemDirectory_method_find_dir_index"></span>

[int](class_int.md#class_int) **find_dir_index** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_find_dir_index)

Returns the index of the directory with name `name` or `-1` if not found.

---

<span id="class_EditorFileSystemDirectory_method_find_file_index"></span>

[int](class_int.md#class_int) **find_file_index** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_find_file_index)

Returns the index of the file with name `name` or `-1` if not found.

---

<span id="class_EditorFileSystemDirectory_method_get_file"></span>

[String](class_string.md#class_String) **get_file** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file)

Returns the name of the file at index `idx`.

---

<span id="class_EditorFileSystemDirectory_method_get_file_count"></span>

[int](class_int.md#class_int) **get_file_count** ( ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_count)

Returns the number of files in this directory.

---

<span id="class_EditorFileSystemDirectory_method_get_file_import_is_valid"></span>

[bool](class_bool.md#class_bool) **get_file_import_is_valid** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_import_is_valid)

Returns `true` if the file at index `idx` imported properly.

---

<span id="class_EditorFileSystemDirectory_method_get_file_path"></span>

[String](class_string.md#class_String) **get_file_path** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_path)

Returns the path to the file at index `idx`.

---

<span id="class_EditorFileSystemDirectory_method_get_file_script_class_extends"></span>

[String](class_string.md#class_String) **get_file_script_class_extends** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_script_class_extends)

Returns the base class of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.

---

<span id="class_EditorFileSystemDirectory_method_get_file_script_class_name"></span>

[String](class_string.md#class_String) **get_file_script_class_name** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_script_class_name)

Returns the name of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.

---

<span id="class_EditorFileSystemDirectory_method_get_file_type"></span>

[StringName](class_stringname.md#class_StringName) **get_file_type** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_file_type)

Returns the resource type of the file at index `idx`. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.

---

<span id="class_EditorFileSystemDirectory_method_get_name"></span>

[String](class_string.md#class_String) **get_name** ( ) [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_name)

Returns the name of this directory.

---

<span id="class_EditorFileSystemDirectory_method_get_parent"></span>

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory) **get_parent** ( ) [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_parent)

Returns the parent directory for this directory or `null` if called on a directory at `res://` or `user://`.

---

<span id="class_EditorFileSystemDirectory_method_get_path"></span>

[String](class_string.md#class_String) **get_path** ( ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_path)

Returns the path to this directory.

---

<span id="class_EditorFileSystemDirectory_method_get_subdir"></span>

[EditorFileSystemDirectory](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory) **get_subdir** ( idx: [int](class_int.md#class_int) ) [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_subdir)

Returns the subdirectory at index `idx`.

---

<span id="class_EditorFileSystemDirectory_method_get_subdir_count"></span>

[int](class_int.md#class_int) **get_subdir_count** ( ) *const* [🔗](class_editorfilesystemdirectory.md#class_EditorFileSystemDirectory_method_get_subdir_count)

Returns the number of subdirectories in this directory.
