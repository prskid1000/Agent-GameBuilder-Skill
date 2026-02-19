<span id="class_EditorExportPlugin"></span>

## EditorExportPlugin

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A script that is executed when exporting the project.

### Description

**EditorExportPlugin** s are automatically invoked whenever the user exports the project. Their most common use is to determine what files are being included in the exported project. For each plugin, [_export_begin()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_begin) is called at the beginning of the export process and then [_export_file()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_file) is called for each exported file.

To use **EditorExportPlugin**, register it using the [EditorPlugin.add_export_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_export_plugin) method first.

### Tutorials

- [Export Android plugins](../tutorials/platform/android/android_plugin.md)

### Methods


| [bool](class_bool.md#class_bool) | [_begin_customize_resources](class_editorexportplugin.md#class_EditorExportPlugin_private_method__begin_customize_resources) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), features: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) | virtual | const |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_begin_customize_scenes](class_editorexportplugin.md#class_EditorExportPlugin_private_method__begin_customize_scenes) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), features: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) | virtual | const |
| [Resource](class_resource.md#class_Resource) | [_customize_resource](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_resource) ( resource: [Resource](class_resource.md#class_Resource), path: [String](class_string.md#class_String) ) | virtual | required |
| [Node](class_node.md#class_Node) | [_customize_scene](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_scene) ( scene: [Node](class_node.md#class_Node), path: [String](class_string.md#class_String) ) | virtual | required |
| void | [_end_customize_resources](class_editorexportplugin.md#class_EditorExportPlugin_private_method__end_customize_resources) ( ) virtual |
| void | [_end_customize_scenes](class_editorexportplugin.md#class_EditorExportPlugin_private_method__end_customize_scenes) ( ) virtual |
| void | [_export_begin](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_begin) ( features: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), is_debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: [int](class_int.md#class_int) ) virtual |
| void | [_export_end](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_end) ( ) virtual |
| void | [_export_file](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_file) ( path: [String](class_string.md#class_String), type: [String](class_string.md#class_String), features: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) virtual |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_android_dependencies](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_dependencies) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) | virtual | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_android_dependencies_maven_repos](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_dependencies_maven_repos) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) | virtual | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_android_libraries](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_libraries) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_android_manifest_activity_element_contents](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_manifest_activity_element_contents) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_android_manifest_application_element_contents](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_manifest_application_element_contents) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_android_manifest_element_contents](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_manifest_element_contents) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) | virtual | const |
| [int](class_int.md#class_int) | [_get_customization_configuration_hash](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_customization_configuration_hash) ( ) | virtual | required | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_export_features](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_features) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_get_export_option_visibility](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_option_visibility) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), option: [String](class_string.md#class_String) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_export_option_warning](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_option_warning) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), option: [String](class_string.md#class_String) ) | virtual | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_export_options](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_options) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) | virtual | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_export_options_overrides](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_options_overrides) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_name](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_name) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_should_update_export_options](class_editorexportplugin.md#class_EditorExportPlugin_private_method__should_update_export_options) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_supports_platform](class_editorexportplugin.md#class_EditorExportPlugin_private_method__supports_platform) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) | virtual | const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [_update_android_prebuilt_manifest](class_editorexportplugin.md#class_EditorExportPlugin_private_method__update_android_prebuilt_manifest) ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), manifest_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) | virtual | const |
| void | [add_apple_embedded_platform_bundle_file](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_bundle_file) ( path: [String](class_string.md#class_String) ) |
| void | [add_apple_embedded_platform_cpp_code](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_cpp_code) ( code: [String](class_string.md#class_String) ) |
| void | [add_apple_embedded_platform_embedded_framework](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_embedded_framework) ( path: [String](class_string.md#class_String) ) |
| void | [add_apple_embedded_platform_framework](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_framework) ( path: [String](class_string.md#class_String) ) |
| void | [add_apple_embedded_platform_linker_flags](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_linker_flags) ( flags: [String](class_string.md#class_String) ) |
| void | [add_apple_embedded_platform_plist_content](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_plist_content) ( plist_content: [String](class_string.md#class_String) ) |
| void | [add_apple_embedded_platform_project_static_lib](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_project_static_lib) ( path: [String](class_string.md#class_String) ) |
| void | [add_file](class_editorexportplugin.md#class_EditorExportPlugin_method_add_file) ( path: [String](class_string.md#class_String), file: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), remap: [bool](class_bool.md#class_bool) ) |
| void | [add_ios_bundle_file](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_bundle_file) ( path: [String](class_string.md#class_String) ) |
| void | [add_ios_cpp_code](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_cpp_code) ( code: [String](class_string.md#class_String) ) |
| void | [add_ios_embedded_framework](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_embedded_framework) ( path: [String](class_string.md#class_String) ) |
| void | [add_ios_framework](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_framework) ( path: [String](class_string.md#class_String) ) |
| void | [add_ios_linker_flags](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_linker_flags) ( flags: [String](class_string.md#class_String) ) |
| void | [add_ios_plist_content](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_plist_content) ( plist_content: [String](class_string.md#class_String) ) |
| void | [add_ios_project_static_lib](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_project_static_lib) ( path: [String](class_string.md#class_String) ) |
| void | [add_macos_plugin_file](class_editorexportplugin.md#class_EditorExportPlugin_method_add_macos_plugin_file) ( path: [String](class_string.md#class_String) ) |
| void | [add_shared_object](class_editorexportplugin.md#class_EditorExportPlugin_method_add_shared_object) ( path: [String](class_string.md#class_String), tags: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), target: [String](class_string.md#class_String) ) |
| [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) | [get_export_platform](class_editorexportplugin.md#class_EditorExportPlugin_method_get_export_platform) ( ) const |
| [EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) | [get_export_preset](class_editorexportplugin.md#class_EditorExportPlugin_method_get_export_preset) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_option](class_editorexportplugin.md#class_EditorExportPlugin_method_get_option) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| void | [skip](class_editorexportplugin.md#class_EditorExportPlugin_method_skip) ( ) |

---

### Method Descriptions

<span id="class_EditorExportPlugin_private_method__begin_customize_resources"></span>

[bool](class_bool.md#class_bool) **_begin_customize_resources** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), features: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__begin_customize_resources)

Return `true` if this plugin will customize resources based on the platform and features used.

When enabled, [_get_customization_configuration_hash()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_customization_configuration_hash) and [_customize_resource()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_resource) will be called and must be implemented.

---

<span id="class_EditorExportPlugin_private_method__begin_customize_scenes"></span>

[bool](class_bool.md#class_bool) **_begin_customize_scenes** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), features: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__begin_customize_scenes)

Return `true` if this plugin will customize scenes based on the platform and features used.

When enabled, [_get_customization_configuration_hash()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_customization_configuration_hash) and [_customize_scene()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_scene) will be called and must be implemented.

 **Note:** [_customize_scene()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_scene) will only be called for scenes that have been modified since the last export.

---

<span id="class_EditorExportPlugin_private_method__customize_resource"></span>

[Resource](class_resource.md#class_Resource) **_customize_resource** ( resource: [Resource](class_resource.md#class_Resource), path: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_resource)

Customize a resource. If changes are made to it, return the same or a new resource. Otherwise, return `null`. When a new resource is returned, `resource` will be replaced by a copy of the new resource.

The `path` argument is only used when customizing an actual file, otherwise this means that this resource is part of another one and it will be empty.

Implementing this method is required if [_begin_customize_resources()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__begin_customize_resources) returns `true`.

 **Note:** When customizing any of the following types and returning another resource, the other resource should not be skipped using [skip()](class_editorexportplugin.md#class_EditorExportPlugin_method_skip) in [_export_file()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_file):

- [AtlasTexture](class_atlastexture.md#class_AtlasTexture)

- [CompressedCubemap](class_compressedcubemap.md#class_CompressedCubemap)

- [CompressedCubemapArray](class_compressedcubemaparray.md#class_CompressedCubemapArray)

- [CompressedTexture2D](class_compressedtexture2d.md#class_CompressedTexture2D)

- [CompressedTexture2DArray](class_compressedtexture2darray.md#class_CompressedTexture2DArray)

- [CompressedTexture3D](class_compressedtexture3d.md#class_CompressedTexture3D)

---

<span id="class_EditorExportPlugin_private_method__customize_scene"></span>

[Node](class_node.md#class_Node) **_customize_scene** ( scene: [Node](class_node.md#class_Node), path: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_scene)

Customize a scene. If changes are made to it, return the same or a new scene. Otherwise, return `null`. If a new scene is returned, it is up to you to dispose of the old one.

Implementing this method is required if [_begin_customize_scenes()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__begin_customize_scenes) returns `true`.

---

<span id="class_EditorExportPlugin_private_method__end_customize_resources"></span>

void **_end_customize_resources** ( ) *virtual* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__end_customize_resources)

This is called when the customization process for resources ends.

---

<span id="class_EditorExportPlugin_private_method__end_customize_scenes"></span>

void **_end_customize_scenes** ( ) *virtual* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__end_customize_scenes)

This is called when the customization process for scenes ends.

---

<span id="class_EditorExportPlugin_private_method__export_begin"></span>

void **_export_begin** ( features: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), is_debug: [bool](class_bool.md#class_bool), path: [String](class_string.md#class_String), flags: [int](class_int.md#class_int) ) *virtual* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_begin)

Virtual method to be overridden by the user. It is called when the export starts and provides all information about the export. `features` is the list of features for the export, `is_debug` is `true` for debug builds, `path` is the target path for the exported project. `flags` is only used when running a runnable profile, e.g. when using native run on Android.

---

<span id="class_EditorExportPlugin_private_method__export_end"></span>

void **_export_end** ( ) *virtual* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_end)

Virtual method to be overridden by the user. Called when the export is finished.

---

<span id="class_EditorExportPlugin_private_method__export_file"></span>

void **_export_file** ( path: [String](class_string.md#class_String), type: [String](class_string.md#class_String), features: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *virtual* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_file)

Virtual method to be overridden by the user. Called for each exported file before [_customize_resource()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_resource) and [_customize_scene()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_scene). The arguments can be used to identify the file. `path` is the path of the file, `type` is the [Resource](class_resource.md#class_Resource) represented by the file (e.g. [PackedScene](class_packedscene.md#class_PackedScene)), and `features` is the list of features for the export.

Calling [skip()](class_editorexportplugin.md#class_EditorExportPlugin_method_skip) inside this callback will make the file not included in the export.

---

<span id="class_EditorExportPlugin_private_method__get_android_dependencies"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_android_dependencies** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_dependencies)

Virtual method to be overridden by the user. This is called to retrieve the set of Android dependencies provided by this plugin. Each returned Android dependency should have the format of an Android remote binary dependency: `org.godot.example:my-plugin:0.0.0`

For more information see Android documentation on dependencies.

 **Note:** Only supported on Android and requires EditorExportPlatformAndroid.gradle_build/use_gradle_build to be enabled.

---

<span id="class_EditorExportPlugin_private_method__get_android_dependencies_maven_repos"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_android_dependencies_maven_repos** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_dependencies_maven_repos)

Virtual method to be overridden by the user. This is called to retrieve the URLs of Maven repositories for the set of Android dependencies provided by this plugin.

For more information see Gradle documentation on dependency management.

 **Note:** Google's Maven repo and the Maven Central repo are already included by default.

 **Note:** Only supported on Android and requires EditorExportPlatformAndroid.gradle_build/use_gradle_build to be enabled.

---

<span id="class_EditorExportPlugin_private_method__get_android_libraries"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_android_libraries** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_libraries)

Virtual method to be overridden by the user. This is called to retrieve the local paths of the Android libraries archive (AAR) files provided by this plugin.

 **Note:** Relative paths **must** be relative to Godot's `res://addons/` directory. For example, an AAR file located under `res://addons/hello_world_plugin/HelloWorld.release.aar` can be returned as an absolute path using `res://addons/hello_world_plugin/HelloWorld.release.aar` or a relative path using `hello_world_plugin/HelloWorld.release.aar`.

 **Note:** Only supported on Android and requires EditorExportPlatformAndroid.gradle_build/use_gradle_build to be enabled.

---

<span id="class_EditorExportPlugin_private_method__get_android_manifest_activity_element_contents"></span>

[String](class_string.md#class_String) **_get_android_manifest_activity_element_contents** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_manifest_activity_element_contents)

Virtual method to be overridden by the user. This is used at export time to update the contents of the `activity` element in the generated Android manifest.

 **Note:** Only supported on Android and requires EditorExportPlatformAndroid.gradle_build/use_gradle_build to be enabled.

---

<span id="class_EditorExportPlugin_private_method__get_android_manifest_application_element_contents"></span>

[String](class_string.md#class_String) **_get_android_manifest_application_element_contents** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_manifest_application_element_contents)

Virtual method to be overridden by the user. This is used at export time to update the contents of the `application` element in the generated Android manifest.

 **Note:** Only supported on Android and requires EditorExportPlatformAndroid.gradle_build/use_gradle_build to be enabled.

---

<span id="class_EditorExportPlugin_private_method__get_android_manifest_element_contents"></span>

[String](class_string.md#class_String) **_get_android_manifest_element_contents** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_android_manifest_element_contents)

Virtual method to be overridden by the user. This is used at export time to update the contents of the `manifest` element in the generated Android manifest.

 **Note:** Only supported on Android and requires EditorExportPlatformAndroid.gradle_build/use_gradle_build to be enabled.

---

<span id="class_EditorExportPlugin_private_method__get_customization_configuration_hash"></span>

[int](class_int.md#class_int) **_get_customization_configuration_hash** ( ) *virtual* |required| *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_customization_configuration_hash)

Return a hash based on the configuration passed (for both scenes and resources). This helps keep separate caches for separate export configurations.

Implementing this method is required if [_begin_customize_resources()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__begin_customize_resources) returns `true`.

---

<span id="class_EditorExportPlugin_private_method__get_export_features"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_export_features** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), debug: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_features)

Return a [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) of additional features this preset, for the given `platform`, should have.

---

<span id="class_EditorExportPlugin_private_method__get_export_option_visibility"></span>

[bool](class_bool.md#class_bool) **_get_export_option_visibility** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), option: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_option_visibility)

Validates `option` and returns the visibility for the specified `platform`. The default implementation returns `true` for all options.

---

<span id="class_EditorExportPlugin_private_method__get_export_option_warning"></span>

[String](class_string.md#class_String) **_get_export_option_warning** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), option: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_option_warning)

Check the requirements for the given `option` and return a non-empty warning string if they are not met.

 **Note:** Use [get_option()](class_editorexportplugin.md#class_EditorExportPlugin_method_get_option) to check the value of the export options.

---

<span id="class_EditorExportPlugin_private_method__get_export_options"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_export_options** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_options)

Return a list of export options that can be configured for this export plugin.

Each element in the return value is a [Dictionary](class_dictionary.md#class_Dictionary) with the following keys:

- `option`: A dictionary with the structure documented by [Object.get_property_list()](class_object.md#class_Object_method_get_property_list), but all keys are optional.

- `default_value`: The default value for this option.

- `update_visibility`: An optional boolean value. If set to `true`, the preset will emit [Object.property_list_changed](class_object.md#class_Object_signal_property_list_changed) when the option is changed.

---

<span id="class_EditorExportPlugin_private_method__get_export_options_overrides"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_export_options_overrides** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_options_overrides)

Return a [Dictionary](class_dictionary.md#class_Dictionary) of override values for export options, that will be used instead of user-provided values. Overridden options will be hidden from the user interface.

::

    class MyExportPlugin extends EditorExportPlugin:
        func _get_name() -> String:
            return "MyExportPlugin"

        func _supports_platform(platform) -> bool:
            if platform is EditorExportPlatformPC:
                # Run on all desktop platforms including Windows, MacOS and Linux.
                return true
            return false

        func _get_export_options_overrides(platform) -> Dictionary:
            # Override "Embed PCK" to always be enabled.
            return {
                "binary_format/embed_pck": true,
            }

---

<span id="class_EditorExportPlugin_private_method__get_name"></span>

[String](class_string.md#class_String) **_get_name** ( ) *virtual* |required| *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_name)

Return the name identifier of this plugin (for future identification by the exporter). The plugins are sorted by name before exporting.

Implementing this method is required.

---

<span id="class_EditorExportPlugin_private_method__should_update_export_options"></span>

[bool](class_bool.md#class_bool) **_should_update_export_options** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__should_update_export_options)

Return `true` if the result of [_get_export_options()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_options) has changed and the export options of the preset corresponding to `platform` should be updated.

---

<span id="class_EditorExportPlugin_private_method__supports_platform"></span>

[bool](class_bool.md#class_bool) **_supports_platform** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__supports_platform)

Return `true` if the plugin supports the given `platform`.

---

<span id="class_EditorExportPlugin_private_method__update_android_prebuilt_manifest"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **_update_android_prebuilt_manifest** ( platform: [EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform), manifest_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) *virtual* *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_private_method__update_android_prebuilt_manifest)

Provide access to the Android prebuilt manifest and allows the plugin to modify it if needed.

Implementers of this virtual method should take the binary manifest data from `manifest_data`, copy it, modify it, and then return it with the modifications.

If no modifications are needed, then an empty [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) should be returned.

---

<span id="class_EditorExportPlugin_method_add_apple_embedded_platform_bundle_file"></span>

void **add_apple_embedded_platform_bundle_file** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_bundle_file)

Adds an Apple embedded platform bundle file from the given `path` to the exported project.

---

<span id="class_EditorExportPlugin_method_add_apple_embedded_platform_cpp_code"></span>

void **add_apple_embedded_platform_cpp_code** ( code: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_cpp_code)

Adds C++ code to the Apple embedded platform export. The final code is created from the code appended by each active export plugin.

---

<span id="class_EditorExportPlugin_method_add_apple_embedded_platform_embedded_framework"></span>

void **add_apple_embedded_platform_embedded_framework** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_embedded_framework)

Adds a dynamic library (\*.dylib, \*.framework) to the Linking Phase in the Apple embedded platform's Xcode project and embeds it into the resulting binary.

 **Note:** For static libraries (\*.a), this works in the same way as [add_apple_embedded_platform_framework()](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_framework).

 **Note:** This method should not be used for System libraries as they are already present on the device.

---

<span id="class_EditorExportPlugin_method_add_apple_embedded_platform_framework"></span>

void **add_apple_embedded_platform_framework** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_framework)

Adds a static library (\*.a) or a dynamic library (\*.dylib, \*.framework) to the Linking Phase to the Apple embedded platform's Xcode project.

---

<span id="class_EditorExportPlugin_method_add_apple_embedded_platform_linker_flags"></span>

void **add_apple_embedded_platform_linker_flags** ( flags: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_linker_flags)

Adds linker flags for the Apple embedded platform export.

---

<span id="class_EditorExportPlugin_method_add_apple_embedded_platform_plist_content"></span>

void **add_apple_embedded_platform_plist_content** ( plist_content: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_plist_content)

Adds additional fields to the Apple embedded platform's project Info.plist file.

---

<span id="class_EditorExportPlugin_method_add_apple_embedded_platform_project_static_lib"></span>

void **add_apple_embedded_platform_project_static_lib** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_project_static_lib)

Adds a static library from the given `path` to the Apple embedded platform project.

---

<span id="class_EditorExportPlugin_method_add_file"></span>

void **add_file** ( path: [String](class_string.md#class_String), file: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), remap: [bool](class_bool.md#class_bool) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_file)

Adds a custom file to be exported. `path` is the virtual path that can be used to load the file, `file` is the binary data of the file.

When called inside [_export_file()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_file) and `remap` is `true`, the current file will not be exported, but instead remapped to this custom file. `remap` is ignored when called in other places.

 `file` will not be imported, so consider using [_customize_resource()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__customize_resource) to remap imported resources.

---

<span id="class_EditorExportPlugin_method_add_ios_bundle_file"></span>

void **add_ios_bundle_file** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_bundle_file)

**Deprecated:** Use [add_apple_embedded_platform_bundle_file()](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_bundle_file) instead.

Adds an iOS bundle file from the given `path` to the exported project.

---

<span id="class_EditorExportPlugin_method_add_ios_cpp_code"></span>

void **add_ios_cpp_code** ( code: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_cpp_code)

**Deprecated:** Use [add_apple_embedded_platform_cpp_code()](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_cpp_code) instead.

Adds C++ code to the iOS export. The final code is created from the code appended by each active export plugin.

---

<span id="class_EditorExportPlugin_method_add_ios_embedded_framework"></span>

void **add_ios_embedded_framework** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_embedded_framework)

**Deprecated:** Use [add_apple_embedded_platform_embedded_framework()](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_embedded_framework) instead.

Adds a dynamic library (\*.dylib, \*.framework) to Linking Phase in iOS's Xcode project and embeds it into resulting binary.

 **Note:** For static libraries (\*.a), this works the in same way as [add_apple_embedded_platform_framework()](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_framework).

 **Note:** This method should not be used for System libraries as they are already present on the device.

---

<span id="class_EditorExportPlugin_method_add_ios_framework"></span>

void **add_ios_framework** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_framework)

**Deprecated:** Use [add_apple_embedded_platform_framework()](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_framework) instead.

Adds a static library (\*.a) or a dynamic library (\*.dylib, \*.framework) to the Linking Phase to the iOS Xcode project.

---

<span id="class_EditorExportPlugin_method_add_ios_linker_flags"></span>

void **add_ios_linker_flags** ( flags: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_linker_flags)

**Deprecated:** Use [add_apple_embedded_platform_linker_flags()](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_linker_flags) instead.

Adds linker flags for the iOS export.

---

<span id="class_EditorExportPlugin_method_add_ios_plist_content"></span>

void **add_ios_plist_content** ( plist_content: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_plist_content)

**Deprecated:** Use [add_apple_embedded_platform_plist_content()](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_plist_content) instead.

Adds additional fields to the iOS project Info.plist file.

---

<span id="class_EditorExportPlugin_method_add_ios_project_static_lib"></span>

void **add_ios_project_static_lib** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_ios_project_static_lib)

**Deprecated:** Use [add_apple_embedded_platform_project_static_lib()](class_editorexportplugin.md#class_EditorExportPlugin_method_add_apple_embedded_platform_project_static_lib) instead.

Adds a static library from the given `path` to the iOS project.

---

<span id="class_EditorExportPlugin_method_add_macos_plugin_file"></span>

void **add_macos_plugin_file** ( path: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_macos_plugin_file)

Adds file or directory matching `path` to `PlugIns` directory of macOS app bundle.

 **Note:** This is useful only for macOS exports.

---

<span id="class_EditorExportPlugin_method_add_shared_object"></span>

void **add_shared_object** ( path: [String](class_string.md#class_String), tags: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), target: [String](class_string.md#class_String) ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_add_shared_object)

Adds a shared object or a directory containing only shared objects with the given `tags` and destination `path`.

 **Note:** In case of macOS exports, those shared objects will be added to `Frameworks` directory of app bundle.

In case of a directory code-sign will error if you place non code object in directory.

---

<span id="class_EditorExportPlugin_method_get_export_platform"></span>

[EditorExportPlatform](class_editorexportplatform.md#class_EditorExportPlatform) **get_export_platform** ( ) *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_get_export_platform)

Returns currently used export platform.

---

<span id="class_EditorExportPlugin_method_get_export_preset"></span>

[EditorExportPreset](class_editorexportpreset.md#class_EditorExportPreset) **get_export_preset** ( ) *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_get_export_preset)

Returns currently used export preset.

---

<span id="class_EditorExportPlugin_method_get_option"></span>

[Variant](class_variant.md#class_Variant) **get_option** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_get_option)

Returns the current value of an export option supplied by [_get_export_options()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__get_export_options).

---

<span id="class_EditorExportPlugin_method_skip"></span>

void **skip** ( ) [🔗](class_editorexportplugin.md#class_EditorExportPlugin_method_skip)

To be called inside [_export_file()](class_editorexportplugin.md#class_EditorExportPlugin_private_method__export_file). Skips the current file, so it's not included in the export.
