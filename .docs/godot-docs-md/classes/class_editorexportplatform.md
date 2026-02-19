<span id="class_EditorExportPlatform"></span>

## EditorExportPlatform

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [EditorExportPlatformAndroid](class_editorexportplatformandroid.md#class_EditorExportPlatformAndroid), [EditorExportPlatformAppleEmbedded](class_editorexportplatformappleembedded.md#class_EditorExportPlatformAppleEmbedded), [EditorExportPlatformExtension](class_editorexportplatformextension.md#class_EditorExportPlatformExtension), [EditorExportPlatformMacOS](class_editorexportplatformmacos.md#class_EditorExportPlatformMacOS), [EditorExportPlatformPC](class_editorexportplatformpc.md#class_EditorExportPlatformPC), [EditorExportPlatformWeb](class_editorexportplatformweb.md#class_EditorExportPlatformWeb)

Identifies a supported export platform, and internally provides the functionality of exporting to that platform.

### Description

Base resource that provides the functionality of exporting a release build of a project to a platform, from the editor. Stores platform-specific metadata such as the name and supported features of the platform, and performs the exporting of projects, PCK files, and ZIP files. Uses an export template for the platform provided at the time of project exporting.

Used in scripting by [EditorExportPlugin](class_editorexportplugin.md#class_EditorExportPlugin) to configure platform-specific customization of scenes and resources. See [EditorExportPlugin._begin_customize_scenes()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__begin_customize_scenes) and [EditorExportPlugin._begin_customize_resources()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__begin_customize_resources) for more details.

### Methods


| void | [add_message](class_editorexportplatform.md#class_EditorExportPlatform_method_add_message) ( type: [ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType), category: [String](class_string.md#class_String), message: [String](class_string.md#class_String) ) |
| --- | --- |
| void | [clear_messages](class_editorexportplatform.md#class_EditorExportPlatform_method_clear_messages) ( ) |
| [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) | [create_preset](class_editorexportplatform.md#class_EditorExportPlatform_method_create_preset) ( ) |
| Error | [export_pack](class_editorexportplatform.md#class_EditorExportPlatform_method_export_pack) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) |
| Error | [export_pack_patch](class_editorexportplatform.md#class_EditorExportPlatform_method_export_pack_patch) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), patches: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) = PackedStringArray(), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) |
| Error | [export_project](class_editorexportplatform.md#class_EditorExportPlatform_method_export_project) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) |
| Error | [export_project_files](class_editorexportplatform.md#class_EditorExportPlatform_method_export_project_files) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), save_cb: [Callable](class_callable.md#class_Callable), shared_cb: [Callable](class_callable.md#class_Callable) = Callable() ) |
| Error | [export_zip](class_editorexportplatform.md#class_EditorExportPlatform_method_export_zip) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) |
| Error | [export_zip_patch](class_editorexportplatform.md#class_EditorExportPlatform_method_export_zip_patch) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), patches: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) = PackedStringArray(), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [find_export_template](class_editorexportplatform.md#class_EditorExportPlatform_method_find_export_template) ( template_file_name: [String](class_string.md#class_String) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [gen_export_flags](class_editorexportplatform.md#class_EditorExportPlatform_method_gen_export_flags) ( flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) |
| [Array](class_array.md#class_Array) | [get_current_presets](class_editorexportplatform.md#class_EditorExportPlatform_method_get_current_presets) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_forced_export_files](class_editorexportplatform.md#class_EditorExportPlatform_method_get_forced_export_files) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) = null ) static |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_internal_export_files](class_editorexportplatform.md#class_EditorExportPlatform_method_get_internal_export_files) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool) ) |
| [String](class_string.md#class_String) | [get_message_category](class_editorexportplatform.md#class_EditorExportPlatform_method_get_message_category) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_message_count](class_editorexportplatform.md#class_EditorExportPlatform_method_get_message_count) ( ) const |
| [String](class_string.md#class_String) | [get_message_text](class_editorexportplatform.md#class_EditorExportPlatform_method_get_message_text) ( index: [int](class_int.md#class_int) ) const |
| [ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType) | [get_message_type](class_editorexportplatform.md#class_EditorExportPlatform_method_get_message_type) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_os_name](class_editorexportplatform.md#class_EditorExportPlatform_method_get_os_name) ( ) const |
| [ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType) | [get_worst_message_type](class_editorexportplatform.md#class_EditorExportPlatform_method_get_worst_message_type) ( ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [save_pack](class_editorexportplatform.md#class_EditorExportPlatform_method_save_pack) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), embed: [bool](class_bool.md#class_bool) = false ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [save_pack_patch](class_editorexportplatform.md#class_EditorExportPlatform_method_save_pack_patch) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [save_zip](class_editorexportplatform.md#class_EditorExportPlatform_method_save_zip) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [save_zip_patch](class_editorexportplatform.md#class_EditorExportPlatform_method_save_zip_patch) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String) ) |
| Error | [ssh_push_to_remote](class_editorexportplatform.md#class_EditorExportPlatform_method_ssh_push_to_remote) ( host: [String](class_string.md#class_String), port: [String](class_string.md#class_String), scp_args: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), src_file: [String](class_string.md#class_String), dst_file: [String](class_string.md#class_String) ) const |
| Error | [ssh_run_on_remote](class_editorexportplatform.md#class_EditorExportPlatform_method_ssh_run_on_remote) ( host: [String](class_string.md#class_String), port: [String](class_string.md#class_String), ssh_arg: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), cmd_args: [String](class_string.md#class_String), output: [Array](class_array.md#class_Array) = [], port_fwd: [int](class_int.md#class_int) = -1 ) const |
| [int](class_int.md#class_int) | [ssh_run_on_remote_no_wait](class_editorexportplatform.md#class_EditorExportPlatform_method_ssh_run_on_remote_no_wait) ( host: [String](class_string.md#class_String), port: [String](class_string.md#class_String), ssh_args: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), cmd_args: [String](class_string.md#class_String), port_fwd: [int](class_int.md#class_int) = -1 ) const |

---

### Enumerations

<span id="enum_EditorExportPlatform_ExportMessageType"></span>

enum **ExportMessageType**: [🔗](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType)

<span id="class_EditorExportPlatform_constant_EXPORT_MESSAGE_NONE"></span>

[ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType) **EXPORT_MESSAGE_NONE** = `0`

Invalid message type used as the default value when no type is specified.

<span id="class_EditorExportPlatform_constant_EXPORT_MESSAGE_INFO"></span>

[ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType) **EXPORT_MESSAGE_INFO** = `1`

Message type for informational messages that have no effect on the export.

<span id="class_EditorExportPlatform_constant_EXPORT_MESSAGE_WARNING"></span>

[ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType) **EXPORT_MESSAGE_WARNING** = `2`

Message type for warning messages that should be addressed but still allow to complete the export.

<span id="class_EditorExportPlatform_constant_EXPORT_MESSAGE_ERROR"></span>

[ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType) **EXPORT_MESSAGE_ERROR** = `3`

Message type for error messages that must be addressed and fail the export.

---

<span id="enum_EditorExportPlatform_DebugFlags"></span>

flags **DebugFlags**: [🔗](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)

<span id="class_EditorExportPlatform_constant_DEBUG_FLAG_DUMB_CLIENT"></span>

[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags) **DEBUG_FLAG_DUMB_CLIENT** = `1`

Flag is set if the remotely debugged project is expected to use the remote file system. If set, [gen_export_flags()](class_editorexportplatform.md#class_EditorExportPlatform_method_gen_export_flags) will append `--remote-fs` and `--remote-fs-password` (if EditorSettings.filesystem/file_server/password is defined) command line arguments to the returned list.

<span id="class_EditorExportPlatform_constant_DEBUG_FLAG_REMOTE_DEBUG"></span>

[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags) **DEBUG_FLAG_REMOTE_DEBUG** = `2`

Flag is set if remote debug is enabled. If set, [gen_export_flags()](class_editorexportplatform.md#class_EditorExportPlatform_method_gen_export_flags) will append `--remote-debug` and `--breakpoints` (if breakpoints are selected in the script editor or added by the plugin) command line arguments to the returned list.

<span id="class_EditorExportPlatform_constant_DEBUG_FLAG_REMOTE_DEBUG_LOCALHOST"></span>

[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags) **DEBUG_FLAG_REMOTE_DEBUG_LOCALHOST** = `4`

Flag is set if remotely debugged project is running on the localhost. If set, [gen_export_flags()](class_editorexportplatform.md#class_EditorExportPlatform_method_gen_export_flags) will use `localhost` instead of EditorSettings.network/debug/remote_host as remote debugger host.

<span id="class_EditorExportPlatform_constant_DEBUG_FLAG_VIEW_COLLISIONS"></span>

[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags) **DEBUG_FLAG_VIEW_COLLISIONS** = `8`

Flag is set if the "Visible Collision Shapes" remote debug option is enabled. If set, [gen_export_flags()](class_editorexportplatform.md#class_EditorExportPlatform_method_gen_export_flags) will append the `--debug-collisions` command line argument to the returned list.

<span id="class_EditorExportPlatform_constant_DEBUG_FLAG_VIEW_NAVIGATION"></span>

[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags) **DEBUG_FLAG_VIEW_NAVIGATION** = `16`

Flag is set if the "Visible Navigation" remote debug option is enabled. If set, [gen_export_flags()](class_editorexportplatform.md#class_EditorExportPlatform_method_gen_export_flags) will append the `--debug-navigation` command line argument to the returned list.

---

### Method Descriptions

<span id="class_EditorExportPlatform_method_add_message"></span>

void **add_message** ( type: [ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType), category: [String](class_string.md#class_String), message: [String](class_string.md#class_String) ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_add_message)

Adds a message to the export log that will be displayed when exporting ends.

---

<span id="class_EditorExportPlatform_method_clear_messages"></span>

void **clear_messages** ( ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_clear_messages)

Clears the export log.

---

<span id="class_EditorExportPlatform_method_create_preset"></span>

[EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) **create_preset** ( ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_create_preset)

Create a new preset for this platform.

---

<span id="class_EditorExportPlatform_method_export_pack"></span>

Error **export_pack** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_export_pack)

Creates a PCK archive at `path` for the specified `preset`.

---

<span id="class_EditorExportPlatform_method_export_pack_patch"></span>

Error **export_pack_patch** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), patches: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) = PackedStringArray(), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_export_pack_patch)

Creates a patch PCK archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

 **Note:** `patches` is an optional override of the set of patches defined in the export preset. When empty the patches defined in the export preset will be used instead.

---

<span id="class_EditorExportPlatform_method_export_project"></span>

Error **export_project** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_export_project)

Creates a full project at `path` for the specified `preset`.

---

<span id="class_EditorExportPlatform_method_export_project_files"></span>

Error **export_project_files** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), save_cb: [Callable](class_callable.md#class_Callable), shared_cb: [Callable](class_callable.md#class_Callable) = Callable() ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_export_project_files)

Exports project files for the specified preset. This method can be used to implement custom export format, other than PCK and ZIP. One of the callbacks is called for each exported file.

 `save_cb` is called for all exported files and have the following arguments: `file_path: String`, `file_data: PackedByteArray`, `file_index: int`, `file_count: int`, `encryption_include_filters: PackedStringArray`, `encryption_exclude_filters: PackedStringArray`, `encryption_key: PackedByteArray`.

 `shared_cb` is called for exported native shared/static libraries and have the following arguments: `file_path: String`, `tags: PackedStringArray`, `target_folder: String`.

 **Note:** `file_index` and `file_count` are intended for progress tracking only and aren't necessarily unique and precise.

---

<span id="class_EditorExportPlatform_method_export_zip"></span>

Error **export_zip** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_export_zip)

Create a ZIP archive at `path` for the specified `preset`.

---

<span id="class_EditorExportPlatform_method_export_zip_patch"></span>

Error **export_zip_patch** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), patches: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) = PackedStringArray(), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] = 0 ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_export_zip_patch)

Create a patch ZIP archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

 **Note:** `patches` is an optional override of the set of patches defined in the export preset. When empty the patches defined in the export preset will be used instead.

---

<span id="class_EditorExportPlatform_method_find_export_template"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **find_export_template** ( template_file_name: [String](class_string.md#class_String) ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_find_export_template)

Locates export template for the platform, and returns [Dictionary](class_dictionary.md#class_Dictionary) with the following keys: `path: String` and `error: String`. This method is provided for convenience and custom export platforms aren't required to use it or keep export templates stored in the same way official templates are.

---

<span id="class_EditorExportPlatform_method_gen_export_flags"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **gen_export_flags** ( flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_gen_export_flags)

Generates array of command line arguments for the default export templates for the debug flags and editor settings.

---

<span id="class_EditorExportPlatform_method_get_current_presets"></span>

[Array](class_array.md#class_Array) **get_current_presets** ( ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_get_current_presets)

Returns array of [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) s for this platform.

---

<span id="class_EditorExportPlatform_method_get_forced_export_files"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_forced_export_files** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) = null ) *static* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_get_forced_export_files)

Returns array of core file names that always should be exported regardless of preset config.

---

<span id="class_EditorExportPlatform_method_get_internal_export_files"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_internal_export_files** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool) ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_get_internal_export_files)

Returns additional files that should always be exported regardless of preset configuration, and are not part of the project source. The returned [Dictionary](class_dictionary.md#class_Dictionary) contains filename keys ([String](class_string.md#class_String)) and their corresponding raw data ([PackedByteArray](class_packedbytearray.md#class_PackedByteArray)).

---

<span id="class_EditorExportPlatform_method_get_message_category"></span>

[String](class_string.md#class_String) **get_message_category** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_get_message_category)

Returns the message category for the message with the given `index`.

---

<span id="class_EditorExportPlatform_method_get_message_count"></span>

[int](class_int.md#class_int) **get_message_count** ( ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_get_message_count)

Returns the number of messages in the export log.

---

<span id="class_EditorExportPlatform_method_get_message_text"></span>

[String](class_string.md#class_String) **get_message_text** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_get_message_text)

Returns the text for the message with the given `index`.

---

<span id="class_EditorExportPlatform_method_get_message_type"></span>

[ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType) **get_message_type** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_get_message_type)

Returns the type for the message with the given `index`.

---

<span id="class_EditorExportPlatform_method_get_os_name"></span>

[String](class_string.md#class_String) **get_os_name** ( ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_get_os_name)

Returns the name of the export operating system handled by this **EditorExportPlatform** class, as a friendly string. Possible return values are `Windows`, `Linux`, `macOS`, `Android`, `iOS`, and `Web`.

---

<span id="class_EditorExportPlatform_method_get_worst_message_type"></span>

[ExportMessageType](class_editorexportplatform.md#enum_EditorExportPlatform_ExportMessageType) **get_worst_message_type** ( ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_get_worst_message_type)

Returns most severe message type currently present in the export log.

---

<span id="class_EditorExportPlatform_method_save_pack"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **save_pack** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), embed: [bool](class_bool.md#class_bool) = false ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_save_pack)

Saves PCK archive and returns [Dictionary](class_dictionary.md#class_Dictionary) with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).

If `embed` is `true`, PCK content is appended to the end of `path` file and return [Dictionary](class_dictionary.md#class_Dictionary) additionally include following keys: `embedded_start: int` (embedded PCK offset) and `embedded_size: int` (embedded PCK size).

---

<span id="class_EditorExportPlatform_method_save_pack_patch"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **save_pack_patch** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String) ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_save_pack_patch)

Saves patch PCK archive and returns [Dictionary](class_dictionary.md#class_Dictionary) with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).

---

<span id="class_EditorExportPlatform_method_save_zip"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **save_zip** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String) ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_save_zip)

Saves ZIP archive and returns [Dictionary](class_dictionary.md#class_Dictionary) with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).

---

<span id="class_EditorExportPlatform_method_save_zip_patch"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **save_zip_patch** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String) ) [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_save_zip_patch)

Saves patch ZIP archive and returns [Dictionary](class_dictionary.md#class_Dictionary) with the following keys: `result: Error`, `so_files: Array` (array of the shared/static objects which contains dictionaries with the following keys: `path: String`, `tags: PackedStringArray`, and `target_folder: String`).

---

<span id="class_EditorExportPlatform_method_ssh_push_to_remote"></span>

Error **ssh_push_to_remote** ( host: [String](class_string.md#class_String), port: [String](class_string.md#class_String), scp_args: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), src_file: [String](class_string.md#class_String), dst_file: [String](class_string.md#class_String) ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_ssh_push_to_remote)

Uploads specified file over SCP protocol to the remote host.

---

<span id="class_EditorExportPlatform_method_ssh_run_on_remote"></span>

Error **ssh_run_on_remote** ( host: [String](class_string.md#class_String), port: [String](class_string.md#class_String), ssh_arg: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), cmd_args: [String](class_string.md#class_String), output: [Array](class_array.md#class_Array) = [], port_fwd: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_ssh_run_on_remote)

Executes specified command on the remote host via SSH protocol and returns command output in the `output`.

---

<span id="class_EditorExportPlatform_method_ssh_run_on_remote_no_wait"></span>

[int](class_int.md#class_int) **ssh_run_on_remote_no_wait** ( host: [String](class_string.md#class_String), port: [String](class_string.md#class_String), ssh_args: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), cmd_args: [String](class_string.md#class_String), port_fwd: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_editorexportplatform.md#class_EditorExportPlatform_method_ssh_run_on_remote_no_wait)

Executes specified command on the remote host via SSH protocol and returns process ID (on the remote host) without waiting for command to finish.
