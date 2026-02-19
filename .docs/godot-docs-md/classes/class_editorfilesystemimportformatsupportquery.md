<span id="class_EditorFileSystemImportFormatSupportQuery"></span>

## EditorFileSystemImportFormatSupportQuery

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Used to query and configure import format support.

### Description

This class is used to query and configure a certain import format. It is used in conjunction with asset format import plugins.

### Methods


| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_file_extensions](class_editorfilesystemimportformatsupportquery.md#class_EditorFileSystemImportFormatSupportQuery_private_method__get_file_extensions) ( ) | virtual | required | const |
| --- | --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_is_active](class_editorfilesystemimportformatsupportquery.md#class_EditorFileSystemImportFormatSupportQuery_private_method__is_active) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_query](class_editorfilesystemimportformatsupportquery.md#class_EditorFileSystemImportFormatSupportQuery_private_method__query) ( ) | virtual | required | const |

---

### Method Descriptions

<span id="class_EditorFileSystemImportFormatSupportQuery_private_method__get_file_extensions"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_file_extensions** ( ) *virtual* |required| *const* [🔗](class_editorfilesystemimportformatsupportquery.md#class_EditorFileSystemImportFormatSupportQuery_private_method__get_file_extensions)

Return the file extensions supported.

---

<span id="class_EditorFileSystemImportFormatSupportQuery_private_method__is_active"></span>

[bool](class_bool.md#class_bool) **_is_active** ( ) *virtual* |required| *const* [🔗](class_editorfilesystemimportformatsupportquery.md#class_EditorFileSystemImportFormatSupportQuery_private_method__is_active)

Return whether this importer is active.

---

<span id="class_EditorFileSystemImportFormatSupportQuery_private_method__query"></span>

[bool](class_bool.md#class_bool) **_query** ( ) *virtual* |required| *const* [🔗](class_editorfilesystemimportformatsupportquery.md#class_EditorFileSystemImportFormatSupportQuery_private_method__query)

Query support. Return `false` if import must not continue.
