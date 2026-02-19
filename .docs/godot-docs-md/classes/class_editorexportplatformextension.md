<span id="class_EditorExportPlatformExtension"></span>

## EditorExportPlatformExtension

**Inherits:** [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Base class for custom [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) implementations (plugins).

### Description

External [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) implementations should inherit from this class.

To use [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), register it using the [EditorPlugin.add_export_platform()](class_editorplugin.md#class_EditorPlugin_method_add_export_platform) method first.

### Methods


| [bool](class_bool.md#class_bool) | [_can_export](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__can_export) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool) ) | virtual | const |
| --- | --- | --- | --- |
| void | [_cleanup](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__cleanup) ( ) virtual |
| Error | [_export_pack](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_pack) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) | virtual |
| Error | [_export_pack_patch](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_pack_patch) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), patches: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) | virtual |
| Error | [_export_project](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_project) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) | virtual | required |
| Error | [_export_zip](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_zip) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) | virtual |
| Error | [_export_zip_patch](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_zip_patch) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), patches: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) | virtual |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_binary_extensions](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_binary_extensions) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) ) | virtual | required | const |
| [String](class_string.md#class_String) | [_get_debug_protocol](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_debug_protocol) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_device_architecture](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_device_architecture) ( device: [int](class_int.md#class_int) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_get_export_option_visibility](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_export_option_visibility) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), option: [String](class_string.md#class_String) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_export_option_warning](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_export_option_warning) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), option: [StringName](class_stringname.md#class_StringName) ) | virtual | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_export_options](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_export_options) ( ) | virtual | const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [_get_logo](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_logo) ( ) | virtual | required | const |
| [String](class_string.md#class_String) | [_get_name](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_name) ( ) | virtual | required | const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [_get_option_icon](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_option_icon) ( device: [int](class_int.md#class_int) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_option_label](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_option_label) ( device: [int](class_int.md#class_int) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_option_tooltip](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_option_tooltip) ( device: [int](class_int.md#class_int) ) | virtual | const |
| [int](class_int.md#class_int) | [_get_options_count](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_options_count) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_options_tooltip](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_options_tooltip) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_os_name](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_os_name) ( ) | virtual | required | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_platform_features](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_platform_features) ( ) | virtual | required | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_preset_features](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_preset_features) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) ) | virtual | required | const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [_get_run_icon](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_run_icon) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_has_valid_export_configuration](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_export_configuration) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_valid_project_configuration](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_project_configuration) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) ) | virtual | required | const |
| void | [_initialize](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__initialize) ( ) virtual |
| [bool](class_bool.md#class_bool) | [_is_executable](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__is_executable) ( path: [String](class_string.md#class_String) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_poll_export](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__poll_export) ( ) virtual |
| Error | [_run](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__run) ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), device: [int](class_int.md#class_int), debug_flags: | bitfield | \[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) | virtual |
| [bool](class_bool.md#class_bool) | [_should_update_export_options](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__should_update_export_options) ( ) virtual |
| [String](class_string.md#class_String) | [get_config_error](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_get_config_error) ( ) const |
| [bool](class_bool.md#class_bool) | [get_config_missing_templates](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_get_config_missing_templates) ( ) const |
| void | [set_config_error](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_set_config_error) ( error_text: [String](class_string.md#class_String) ) const |
| void | [set_config_missing_templates](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_set_config_missing_templates) ( missing_templates: [bool](class_bool.md#class_bool) ) const |

---

### Method Descriptions

<span id="class_EditorExportPlatformExtension_private_method__can_export"></span>

[bool](class_bool.md#class_bool) **_can_export** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__can_export)

Returns `true` if the specified `preset` is valid and can be exported. Use [set_config_error()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_set_config_error) and [set_config_missing_templates()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_set_config_missing_templates) to set error details.

Usual implementations call [_has_valid_export_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_export_configuration) and [_has_valid_project_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_project_configuration) to determine if exporting is possible.

---

<span id="class_EditorExportPlatformExtension_private_method__cleanup"></span>

void **_cleanup** ( ) *virtual* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__cleanup)

Called by the editor before platform is unregistered.

---

<span id="class_EditorExportPlatformExtension_private_method__export_pack"></span>

Error **_export_pack** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) *virtual* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_pack)

Creates a PCK archive at `path` for the specified `preset`.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" disabled, and PCK is selected as a file type.

---

<span id="class_EditorExportPlatformExtension_private_method__export_pack_patch"></span>

Error **_export_pack_patch** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), patches: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) *virtual* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_pack_patch)

Creates a patch PCK archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" enabled, and PCK is selected as a file type.

 **Note:** The patches provided in `patches` have already been loaded when this method is called and are merely provided as context. When empty the patches defined in the export preset have been loaded instead.

---

<span id="class_EditorExportPlatformExtension_private_method__export_project"></span>

Error **_export_project** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) *virtual* |required| [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_project)

Creates a full project at `path` for the specified `preset`.

This method is called when "Export" button is pressed in the export dialog.

This method implementation can call [EditorExportPlatform.save_pack()](class_editorexportplatform.md#class_EditorExportPlatform_method_save_pack) or [EditorExportPlatform.save_zip()](class_editorexportplatform.md#class_EditorExportPlatform_method_save_zip) to use default PCK/ZIP export process, or calls [EditorExportPlatform.export_project_files()](class_editorexportplatform.md#class_EditorExportPlatform_method_export_project_files) and implement custom callback for processing each exported file.

---

<span id="class_EditorExportPlatformExtension_private_method__export_zip"></span>

Error **_export_zip** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) *virtual* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_zip)

Create a ZIP archive at `path` for the specified `preset`.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" disabled, and ZIP is selected as a file type.

---

<span id="class_EditorExportPlatformExtension_private_method__export_zip_patch"></span>

Error **_export_zip_patch** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), patches: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) *virtual* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__export_zip_patch)

Create a ZIP archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" enabled, and ZIP is selected as a file type.

 **Note:** The patches provided in `patches` have already been loaded when this method is called and are merely provided as context. When empty the patches defined in the export preset have been loaded instead.

---

<span id="class_EditorExportPlatformExtension_private_method__get_binary_extensions"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_binary_extensions** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) ) *virtual* |required| *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_binary_extensions)

Returns array of supported binary extensions for the full project export.

---

<span id="class_EditorExportPlatformExtension_private_method__get_debug_protocol"></span>

[String](class_string.md#class_String) **_get_debug_protocol** ( ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_debug_protocol)

Returns protocol used for remote debugging. Default implementation return `tcp://`.

---

<span id="class_EditorExportPlatformExtension_private_method__get_device_architecture"></span>

[String](class_string.md#class_String) **_get_device_architecture** ( device: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_device_architecture)

Returns device architecture for one-click deploy.

---

<span id="class_EditorExportPlatformExtension_private_method__get_export_option_visibility"></span>

[bool](class_bool.md#class_bool) **_get_export_option_visibility** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), option: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_export_option_visibility)

Validates `option` and returns visibility for the specified `preset`. Default implementation return `true` for all options.

---

<span id="class_EditorExportPlatformExtension_private_method__get_export_option_warning"></span>

[String](class_string.md#class_String) **_get_export_option_warning** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), option: [StringName](class_stringname.md#class_StringName) ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_export_option_warning)

Validates `option` and returns warning message for the specified `preset`. Default implementation return empty string for all options.

---

<span id="class_EditorExportPlatformExtension_private_method__get_export_options"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_export_options** ( ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_export_options)

Returns a property list, as an [Array](class_array.md#class_Array) of dictionaries. Each [Dictionary](class_dictionary.md#class_Dictionary) must at least contain the `name: StringName` and `type: Variant.Type` entries.

Additionally, the following keys are supported:

- `hint: PropertyHint`

- `hint_string: String`

- `usage: PropertyUsageFlags`

- `class_name: StringName`

- `default_value: Variant`, default value of the property.

- `update_visibility: bool`, if set to `true`, [_get_export_option_visibility()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_export_option_visibility) is called for each property when this property is changed.

- `required: bool`, if set to `true`, this property warnings are critical, and should be resolved to make export possible. This value is a hint for the [_has_valid_export_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_export_configuration) implementation, and not used by the engine directly.

See also [Object._get_property_list()](class_object.md#class_Object_private_method__get_property_list).

---

<span id="class_EditorExportPlatformExtension_private_method__get_logo"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **_get_logo** ( ) *virtual* |required| *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_logo)

Returns the platform logo displayed in the export dialog. The logo should be 32×32 pixels, adjusted for the current editor scale (see [EditorInterface.get_editor_scale()](class_editorinterface.md#class_EditorInterface_method_get_editor_scale)).

---

<span id="class_EditorExportPlatformExtension_private_method__get_name"></span>

[String](class_string.md#class_String) **_get_name** ( ) *virtual* |required| *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_name)

Returns export platform name.

---

<span id="class_EditorExportPlatformExtension_private_method__get_option_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **_get_option_icon** ( device: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_option_icon)

Returns the item icon for the specified `device` in the one-click deploy menu. The icon should be 16×16 pixels, adjusted for the current editor scale (see [EditorInterface.get_editor_scale()](class_editorinterface.md#class_EditorInterface_method_get_editor_scale)).

---

<span id="class_EditorExportPlatformExtension_private_method__get_option_label"></span>

[String](class_string.md#class_String) **_get_option_label** ( device: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_option_label)

Returns one-click deploy menu item label for the specified `device`.

---

<span id="class_EditorExportPlatformExtension_private_method__get_option_tooltip"></span>

[String](class_string.md#class_String) **_get_option_tooltip** ( device: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_option_tooltip)

Returns one-click deploy menu item tooltip for the specified `device`.

---

<span id="class_EditorExportPlatformExtension_private_method__get_options_count"></span>

[int](class_int.md#class_int) **_get_options_count** ( ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_options_count)

Returns the number of devices (or other options) available in the one-click deploy menu.

---

<span id="class_EditorExportPlatformExtension_private_method__get_options_tooltip"></span>

[String](class_string.md#class_String) **_get_options_tooltip** ( ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_options_tooltip)

Returns tooltip of the one-click deploy menu button.

---

<span id="class_EditorExportPlatformExtension_private_method__get_os_name"></span>

[String](class_string.md#class_String) **_get_os_name** ( ) *virtual* |required| *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_os_name)

Returns target OS name.

---

<span id="class_EditorExportPlatformExtension_private_method__get_platform_features"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_platform_features** ( ) *virtual* |required| *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_platform_features)

Returns array of platform specific features.

---

<span id="class_EditorExportPlatformExtension_private_method__get_preset_features"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_preset_features** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) ) *virtual* |required| *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_preset_features)

Returns array of platform specific features for the specified `preset`.

---

<span id="class_EditorExportPlatformExtension_private_method__get_run_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **_get_run_icon** ( ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__get_run_icon)

Returns the icon of the one-click deploy menu button. The icon should be 16×16 pixels, adjusted for the current editor scale (see [EditorInterface.get_editor_scale()](class_editorinterface.md#class_EditorInterface_method_get_editor_scale)).

---

<span id="class_EditorExportPlatformExtension_private_method__has_valid_export_configuration"></span>

[bool](class_bool.md#class_bool) **_has_valid_export_configuration** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), debug: [bool](class_bool.md#class_bool) ) *virtual* |required| *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_export_configuration)

Returns `true` if export configuration is valid.

---

<span id="class_EditorExportPlatformExtension_private_method__has_valid_project_configuration"></span>

[bool](class_bool.md#class_bool) **_has_valid_project_configuration** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) ) *virtual* |required| *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_project_configuration)

Returns `true` if project configuration is valid.

---

<span id="class_EditorExportPlatformExtension_private_method__initialize"></span>

void **_initialize** ( ) *virtual* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__initialize)

Initializes the plugin. Called by the editor when platform is registered.

---

<span id="class_EditorExportPlatformExtension_private_method__is_executable"></span>

[bool](class_bool.md#class_bool) **_is_executable** ( path: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__is_executable)

Returns `true` if specified file is a valid executable (native executable or script) for the target platform.

---

<span id="class_EditorExportPlatformExtension_private_method__poll_export"></span>

[bool](class_bool.md#class_bool) **_poll_export** ( ) *virtual* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__poll_export)

Returns `true` if one-click deploy options are changed and editor interface should be updated.

---

<span id="class_EditorExportPlatformExtension_private_method__run"></span>

Error **_run** ( preset: [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset), device: [int](class_int.md#class_int), debug_flags: *BitField*\[[DebugFlags](class_editorexportplatform.md#enum_EditorExportPlatform_DebugFlags)\] ) *virtual* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__run)

This method is called when `device` one-click deploy menu option is selected.

Implementation should export project to a temporary location, upload and run it on the specific `device`, or perform another action associated with the menu item.

---

<span id="class_EditorExportPlatformExtension_private_method__should_update_export_options"></span>

[bool](class_bool.md#class_bool) **_should_update_export_options** ( ) *virtual* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__should_update_export_options)

Returns `true` if export options list is changed and presets should be updated.

---

<span id="class_EditorExportPlatformExtension_method_get_config_error"></span>

[String](class_string.md#class_String) **get_config_error** ( ) *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_get_config_error)

Returns current configuration error message text. This method should be called only from the [_can_export()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__can_export), [_has_valid_export_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_export_configuration), or [_has_valid_project_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_project_configuration) implementations.

---

<span id="class_EditorExportPlatformExtension_method_get_config_missing_templates"></span>

[bool](class_bool.md#class_bool) **get_config_missing_templates** ( ) *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_get_config_missing_templates)

Returns `true` is export templates are missing from the current configuration. This method should be called only from the [_can_export()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__can_export), [_has_valid_export_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_export_configuration), or [_has_valid_project_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_project_configuration) implementations.

---

<span id="class_EditorExportPlatformExtension_method_set_config_error"></span>

void **set_config_error** ( error_text: [String](class_string.md#class_String) ) *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_set_config_error)

Sets current configuration error message text. This method should be called only from the [_can_export()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__can_export), [_has_valid_export_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_export_configuration), or [_has_valid_project_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_project_configuration) implementations.

---

<span id="class_EditorExportPlatformExtension_method_set_config_missing_templates"></span>

void **set_config_missing_templates** ( missing_templates: [bool](class_bool.md#class_bool) ) *const* [🔗](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_method_set_config_missing_templates)

Set to `true` is export templates are missing from the current configuration. This method should be called only from the [_can_export()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__can_export), [_has_valid_export_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_export_configuration), or [_has_valid_project_configuration()](class_editorexportplatformextension.md#class_EditorExportPlatformExtension_private_method__has_valid_project_configuration) implementations.
