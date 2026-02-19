<span id="class_EditorExportPreset"></span>

## EditorExportPreset

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Export preset configuration.

### Description

Represents the configuration of an export preset, as created by the editor's export dialog. An **EditorExportPreset** instance is intended to be used a read-only configuration passed to the [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) methods when exporting the project.

### Methods


| [bool](class_bool.md#class_bool) | [are_advanced_options_enabled](class_editorexportpreset.md#class_EditorExportPreset_method_are_advanced_options_enabled) ( ) const |
| --- | --- |
| [String](class_string.md#class_String) | [get_custom_features](class_editorexportpreset.md#class_EditorExportPreset_method_get_custom_features) ( ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_customized_files](class_editorexportpreset.md#class_EditorExportPreset_method_get_customized_files) ( ) const |
| [int](class_int.md#class_int) | [get_customized_files_count](class_editorexportpreset.md#class_EditorExportPreset_method_get_customized_files_count) ( ) const |
| [bool](class_bool.md#class_bool) | [get_encrypt_directory](class_editorexportpreset.md#class_EditorExportPreset_method_get_encrypt_directory) ( ) const |
| [bool](class_bool.md#class_bool) | [get_encrypt_pck](class_editorexportpreset.md#class_EditorExportPreset_method_get_encrypt_pck) ( ) const |
| [String](class_string.md#class_String) | [get_encryption_ex_filter](class_editorexportpreset.md#class_EditorExportPreset_method_get_encryption_ex_filter) ( ) const |
| [String](class_string.md#class_String) | [get_encryption_in_filter](class_editorexportpreset.md#class_EditorExportPreset_method_get_encryption_in_filter) ( ) const |
| [String](class_string.md#class_String) | [get_encryption_key](class_editorexportpreset.md#class_EditorExportPreset_method_get_encryption_key) ( ) const |
| [String](class_string.md#class_String) | [get_exclude_filter](class_editorexportpreset.md#class_EditorExportPreset_method_get_exclude_filter) ( ) const |
| [ExportFilter](class_editorexportpreset.md#enum_EditorExportPreset_ExportFilter) | [get_export_filter](class_editorexportpreset.md#class_EditorExportPreset_method_get_export_filter) ( ) const |
| [String](class_string.md#class_String) | [get_export_path](class_editorexportpreset.md#class_EditorExportPreset_method_get_export_path) ( ) const |
| [FileExportMode](class_editorexportpreset.md#enum_EditorExportPreset_FileExportMode) | [get_file_export_mode](class_editorexportpreset.md#class_EditorExportPreset_method_get_file_export_mode) ( path: [String](class_string.md#class_String), default: [FileExportMode](class_editorexportpreset.md#enum_EditorExportPreset_FileExportMode) = 0 ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_files_to_export](class_editorexportpreset.md#class_EditorExportPreset_method_get_files_to_export) ( ) const |
| [String](class_string.md#class_String) | [get_include_filter](class_editorexportpreset.md#class_EditorExportPreset_method_get_include_filter) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_or_env](class_editorexportpreset.md#class_EditorExportPreset_method_get_or_env) ( name: [StringName](class_stringname.md#class_StringName), env_var: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_patches](class_editorexportpreset.md#class_EditorExportPreset_method_get_patches) ( ) const |
| [String](class_string.md#class_String) | [get_preset_name](class_editorexportpreset.md#class_EditorExportPreset_method_get_preset_name) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_project_setting](class_editorexportpreset.md#class_EditorExportPreset_method_get_project_setting) ( name: [StringName](class_stringname.md#class_StringName) ) |
| [ScriptExportMode](class_editorexportpreset.md#enum_EditorExportPreset_ScriptExportMode) | [get_script_export_mode](class_editorexportpreset.md#class_EditorExportPreset_method_get_script_export_mode) ( ) const |
| [String](class_string.md#class_String) | [get_version](class_editorexportpreset.md#class_EditorExportPreset_method_get_version) ( name: [StringName](class_stringname.md#class_StringName), windows_version: [bool](class_bool.md#class_bool) ) const |
| [bool](class_bool.md#class_bool) | [has](class_editorexportpreset.md#class_EditorExportPreset_method_has) ( property: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_export_file](class_editorexportpreset.md#class_EditorExportPreset_method_has_export_file) ( path: [String](class_string.md#class_String) ) |
| [bool](class_bool.md#class_bool) | [is_dedicated_server](class_editorexportpreset.md#class_EditorExportPreset_method_is_dedicated_server) ( ) const |
| [bool](class_bool.md#class_bool) | [is_runnable](class_editorexportpreset.md#class_EditorExportPreset_method_is_runnable) ( ) const |

---

### Enumerations

<span id="enum_EditorExportPreset_ExportFilter"></span>

enum **ExportFilter**: [🔗](class_editorexportpreset.md#enum_EditorExportPreset_ExportFilter)

<span id="class_EditorExportPreset_constant_EXPORT_ALL_RESOURCES"></span>

[ExportFilter](class_editorexportpreset.md#enum_EditorExportPreset_ExportFilter) **EXPORT_ALL_RESOURCES** = `0`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorExportPreset_constant_EXPORT_SELECTED_SCENES"></span>

[ExportFilter](class_editorexportpreset.md#enum_EditorExportPreset_ExportFilter) **EXPORT_SELECTED_SCENES** = `1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorExportPreset_constant_EXPORT_SELECTED_RESOURCES"></span>

[ExportFilter](class_editorexportpreset.md#enum_EditorExportPreset_ExportFilter) **EXPORT_SELECTED_RESOURCES** = `2`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorExportPreset_constant_EXCLUDE_SELECTED_RESOURCES"></span>

[ExportFilter](class_editorexportpreset.md#enum_EditorExportPreset_ExportFilter) **EXCLUDE_SELECTED_RESOURCES** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorExportPreset_constant_EXPORT_CUSTOMIZED"></span>

[ExportFilter](class_editorexportpreset.md#enum_EditorExportPreset_ExportFilter) **EXPORT_CUSTOMIZED** = `4`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

<span id="enum_EditorExportPreset_FileExportMode"></span>

enum **FileExportMode**: [🔗](class_editorexportpreset.md#enum_EditorExportPreset_FileExportMode)

<span id="class_EditorExportPreset_constant_MODE_FILE_NOT_CUSTOMIZED"></span>

[FileExportMode](class_editorexportpreset.md#enum_EditorExportPreset_FileExportMode) **MODE_FILE_NOT_CUSTOMIZED** = `0`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorExportPreset_constant_MODE_FILE_STRIP"></span>

[FileExportMode](class_editorexportpreset.md#enum_EditorExportPreset_FileExportMode) **MODE_FILE_STRIP** = `1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorExportPreset_constant_MODE_FILE_KEEP"></span>

[FileExportMode](class_editorexportpreset.md#enum_EditorExportPreset_FileExportMode) **MODE_FILE_KEEP** = `2`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorExportPreset_constant_MODE_FILE_REMOVE"></span>

[FileExportMode](class_editorexportpreset.md#enum_EditorExportPreset_FileExportMode) **MODE_FILE_REMOVE** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

<span id="enum_EditorExportPreset_ScriptExportMode"></span>

enum **ScriptExportMode**: [🔗](class_editorexportpreset.md#enum_EditorExportPreset_ScriptExportMode)

<span id="class_EditorExportPreset_constant_MODE_SCRIPT_TEXT"></span>

[ScriptExportMode](class_editorexportpreset.md#enum_EditorExportPreset_ScriptExportMode) **MODE_SCRIPT_TEXT** = `0`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorExportPreset_constant_MODE_SCRIPT_BINARY_TOKENS"></span>

[ScriptExportMode](class_editorexportpreset.md#enum_EditorExportPreset_ScriptExportMode) **MODE_SCRIPT_BINARY_TOKENS** = `1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorExportPreset_constant_MODE_SCRIPT_BINARY_TOKENS_COMPRESSED"></span>

[ScriptExportMode](class_editorexportpreset.md#enum_EditorExportPreset_ScriptExportMode) **MODE_SCRIPT_BINARY_TOKENS_COMPRESSED** = `2`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

### Method Descriptions

<span id="class_EditorExportPreset_method_are_advanced_options_enabled"></span>

[bool](class_bool.md#class_bool) **are_advanced_options_enabled** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_are_advanced_options_enabled)

Returns `true` if the "Advanced" toggle is enabled in the export dialog.

---

<span id="class_EditorExportPreset_method_get_custom_features"></span>

[String](class_string.md#class_String) **get_custom_features** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_custom_features)

Returns a comma-separated list of custom features added to this preset, as a string. See [Feature tags](../tutorials/export/feature_tags.md) in the documentation for more information.

---

<span id="class_EditorExportPreset_method_get_customized_files"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_customized_files** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_customized_files)

Returns a dictionary of files selected in the "Resources" tab of the export dialog. The dictionary's keys are file paths, and its values are the corresponding export modes: `"strip"`, `"keep"`, or `"remove"`. See also [get_file_export_mode()](class_editorexportpreset.md#class_EditorExportPreset_method_get_file_export_mode).

---

<span id="class_EditorExportPreset_method_get_customized_files_count"></span>

[int](class_int.md#class_int) **get_customized_files_count** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_customized_files_count)

Returns the number of files selected in the "Resources" tab of the export dialog.

---

<span id="class_EditorExportPreset_method_get_encrypt_directory"></span>

[bool](class_bool.md#class_bool) **get_encrypt_directory** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_encrypt_directory)

Returns `true` if PCK directory encryption is enabled in the export dialog.

---

<span id="class_EditorExportPreset_method_get_encrypt_pck"></span>

[bool](class_bool.md#class_bool) **get_encrypt_pck** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_encrypt_pck)

Returns `true` if PCK encryption is enabled in the export dialog.

---

<span id="class_EditorExportPreset_method_get_encryption_ex_filter"></span>

[String](class_string.md#class_String) **get_encryption_ex_filter** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_encryption_ex_filter)

Returns file filters to exclude during PCK encryption.

---

<span id="class_EditorExportPreset_method_get_encryption_in_filter"></span>

[String](class_string.md#class_String) **get_encryption_in_filter** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_encryption_in_filter)

Returns file filters to include during PCK encryption.

---

<span id="class_EditorExportPreset_method_get_encryption_key"></span>

[String](class_string.md#class_String) **get_encryption_key** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_encryption_key)

Returns PCK encryption key.

---

<span id="class_EditorExportPreset_method_get_exclude_filter"></span>

[String](class_string.md#class_String) **get_exclude_filter** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_exclude_filter)

Returns file filters to exclude during export.

---

<span id="class_EditorExportPreset_method_get_export_filter"></span>

[ExportFilter](class_editorexportpreset.md#enum_EditorExportPreset_ExportFilter) **get_export_filter** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_export_filter)

Returns export file filter mode selected in the "Resources" tab of the export dialog.

---

<span id="class_EditorExportPreset_method_get_export_path"></span>

[String](class_string.md#class_String) **get_export_path** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_export_path)

Returns export target path.

---

<span id="class_EditorExportPreset_method_get_file_export_mode"></span>

[FileExportMode](class_editorexportpreset.md#enum_EditorExportPreset_FileExportMode) **get_file_export_mode** ( path: [String](class_string.md#class_String), default: [FileExportMode](class_editorexportpreset.md#enum_EditorExportPreset_FileExportMode) = 0 ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_file_export_mode)

Returns file export mode for the specified file.

---

<span id="class_EditorExportPreset_method_get_files_to_export"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_files_to_export** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_files_to_export)

Returns array of files to export.

---

<span id="class_EditorExportPreset_method_get_include_filter"></span>

[String](class_string.md#class_String) **get_include_filter** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_include_filter)

Returns file filters to include during export.

---

<span id="class_EditorExportPreset_method_get_or_env"></span>

[Variant](class_variant.md#class_Variant) **get_or_env** ( name: [StringName](class_stringname.md#class_StringName), env_var: [String](class_string.md#class_String) ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_or_env)

Returns export option value or value of environment variable if it is set.

---

<span id="class_EditorExportPreset_method_get_patches"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_patches** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_patches)

Returns the list of packs on which to base a patch export on.

---

<span id="class_EditorExportPreset_method_get_preset_name"></span>

[String](class_string.md#class_String) **get_preset_name** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_preset_name)

Returns this export preset's name.

---

<span id="class_EditorExportPreset_method_get_project_setting"></span>

[Variant](class_variant.md#class_Variant) **get_project_setting** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_project_setting)

Returns the value of the setting identified by `name` using export preset feature tag overrides instead of current OS features.

---

<span id="class_EditorExportPreset_method_get_script_export_mode"></span>

[ScriptExportMode](class_editorexportpreset.md#enum_EditorExportPreset_ScriptExportMode) **get_script_export_mode** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_script_export_mode)

Returns the export mode used by GDScript files. `0` for "Text", `1` for "Binary tokens", and `2` for "Compressed binary tokens (smaller files)".

---

<span id="class_EditorExportPreset_method_get_version"></span>

[String](class_string.md#class_String) **get_version** ( name: [StringName](class_stringname.md#class_StringName), windows_version: [bool](class_bool.md#class_bool) ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_get_version)

Returns the preset's version number, or fall back to the ProjectSettings.application/config/version project setting if set to an empty string.

If `windows_version` is `true`, formats the returned version number to be compatible with Windows executable metadata.

---

<span id="class_EditorExportPreset_method_has"></span>

[bool](class_bool.md#class_bool) **has** ( property: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_has)

Returns `true` if the preset has the property named `property`.

---

<span id="class_EditorExportPreset_method_has_export_file"></span>

[bool](class_bool.md#class_bool) **has_export_file** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_has_export_file)

Returns `true` if the file at the specified `path` will be exported.

---

<span id="class_EditorExportPreset_method_is_dedicated_server"></span>

[bool](class_bool.md#class_bool) **is_dedicated_server** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_is_dedicated_server)

Returns `true` if the dedicated server export mode is selected in the export dialog.

---

<span id="class_EditorExportPreset_method_is_runnable"></span>

[bool](class_bool.md#class_bool) **is_runnable** ( ) *const* [🔗](class_editorexportpreset.md#class_EditorExportPreset_method_is_runnable)

Returns `true` if the "Runnable" toggle is enabled in the export dialog.
