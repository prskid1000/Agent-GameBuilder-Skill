<span id="class_EditorSceneFormatImporter"></span>

## EditorSceneFormatImporter

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [EditorSceneFormatImporterBlend](class_editorsceneformatimporterblend.md#class_EditorSceneFormatImporterBlend), [EditorSceneFormatImporterFBX2GLTF](class_editorsceneformatimporterfbx2gltf.md#class_EditorSceneFormatImporterFBX2GLTF), [EditorSceneFormatImporterGLTF](class_editorsceneformatimportergltf.md#class_EditorSceneFormatImporterGLTF), [EditorSceneFormatImporterUFBX](class_editorsceneformatimporterufbx.md#class_EditorSceneFormatImporterUFBX)

Imports scenes from third-parties' 3D files.

### Description

**EditorSceneFormatImporter** allows to define an importer script for a third-party 3D format.

To use **EditorSceneFormatImporter**, register it using the [EditorPlugin.add_scene_format_importer_plugin()](class_editorplugin.md#class_EditorPlugin_method_add_scene_format_importer_plugin) method first.

### Methods


| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_extensions](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__get_extensions) ( ) | virtual | required | const |
| --- | --- | --- | --- | --- |
| void | [_get_import_options](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__get_import_options) ( path: [String](class_string.md#class_String) ) virtual |
| [Variant](class_variant.md#class_Variant) | [_get_option_visibility](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__get_option_visibility) ( path: [String](class_string.md#class_String), for_animation: [bool](class_bool.md#class_bool), option: [String](class_string.md#class_String) ) | virtual | const |
| [Object](class_object.md#class_Object) | [_import_scene](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__import_scene) ( path: [String](class_string.md#class_String), flags: [int](class_int.md#class_int), options: [Dictionary](class_dictionary.md#class_Dictionary) ) | virtual | required |
| void | [add_import_option](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_method_add_import_option) ( name: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) |
| void | [add_import_option_advanced](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_method_add_import_option_advanced) ( type: Variant.Type, name: [String](class_string.md#class_String), default_value: [Variant](class_variant.md#class_Variant), hint: PropertyHint = 0, hint_string: [String](class_string.md#class_String) = "", usage_flags: [int](class_int.md#class_int) = 6 ) |

---

### Constants

<span id="class_EditorSceneFormatImporter_constant_IMPORT_SCENE"></span>

**IMPORT_SCENE** = `1` [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_constant_IMPORT_SCENE)

.. container:: contribute

	There is currently no description for this constant. Please help us by contributing one!

<span id="class_EditorSceneFormatImporter_constant_IMPORT_ANIMATION"></span>

**IMPORT_ANIMATION** = `2` [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_constant_IMPORT_ANIMATION)

.. container:: contribute

	There is currently no description for this constant. Please help us by contributing one!

<span id="class_EditorSceneFormatImporter_constant_IMPORT_FAIL_ON_MISSING_DEPENDENCIES"></span>

**IMPORT_FAIL_ON_MISSING_DEPENDENCIES** = `4` [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_constant_IMPORT_FAIL_ON_MISSING_DEPENDENCIES)

.. container:: contribute

	There is currently no description for this constant. Please help us by contributing one!

<span id="class_EditorSceneFormatImporter_constant_IMPORT_GENERATE_TANGENT_ARRAYS"></span>

**IMPORT_GENERATE_TANGENT_ARRAYS** = `8` [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_constant_IMPORT_GENERATE_TANGENT_ARRAYS)

.. container:: contribute

	There is currently no description for this constant. Please help us by contributing one!

<span id="class_EditorSceneFormatImporter_constant_IMPORT_USE_NAMED_SKIN_BINDS"></span>

**IMPORT_USE_NAMED_SKIN_BINDS** = `16` [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_constant_IMPORT_USE_NAMED_SKIN_BINDS)

.. container:: contribute

	There is currently no description for this constant. Please help us by contributing one!

<span id="class_EditorSceneFormatImporter_constant_IMPORT_DISCARD_MESHES_AND_MATERIALS"></span>

**IMPORT_DISCARD_MESHES_AND_MATERIALS** = `32` [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_constant_IMPORT_DISCARD_MESHES_AND_MATERIALS)

.. container:: contribute

	There is currently no description for this constant. Please help us by contributing one!

<span id="class_EditorSceneFormatImporter_constant_IMPORT_FORCE_DISABLE_MESH_COMPRESSION"></span>

**IMPORT_FORCE_DISABLE_MESH_COMPRESSION** = `64` [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_constant_IMPORT_FORCE_DISABLE_MESH_COMPRESSION)

.. container:: contribute

	There is currently no description for this constant. Please help us by contributing one!

---

### Method Descriptions

<span id="class_EditorSceneFormatImporter_private_method__get_extensions"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_extensions** ( ) *virtual* |required| *const* [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__get_extensions)

Return supported file extensions for this scene importer.

---

<span id="class_EditorSceneFormatImporter_private_method__get_import_options"></span>

void **_get_import_options** ( path: [String](class_string.md#class_String) ) *virtual* [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__get_import_options)

Override to add general import options. These will appear in the main import dock on the editor. Add options via [add_import_option()](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_method_add_import_option) and [add_import_option_advanced()](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_method_add_import_option_advanced).

 **Note:** All **EditorSceneFormatImporter** and [EditorScenePostImportPlugin](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin) instances will add options for all files. It is good practice to check the file extension when `path` is non-empty.

When the user is editing project settings, `path` will be empty. It is recommended to add all options when `path` is empty to allow the user to customize Import Defaults.

---

<span id="class_EditorSceneFormatImporter_private_method__get_option_visibility"></span>

[Variant](class_variant.md#class_Variant) **_get_option_visibility** ( path: [String](class_string.md#class_String), for_animation: [bool](class_bool.md#class_bool), option: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__get_option_visibility)

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

---

<span id="class_EditorSceneFormatImporter_private_method__import_scene"></span>

[Object](class_object.md#class_Object) **_import_scene** ( path: [String](class_string.md#class_String), flags: [int](class_int.md#class_int), options: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* |required| [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__import_scene)

Perform the bulk of the scene import logic here, for example using [GLTFDocument](class_gltfdocument.md#class_GLTFDocument) or [FBXDocument](class_fbxdocument.md#class_FBXDocument).

---

<span id="class_EditorSceneFormatImporter_method_add_import_option"></span>

void **add_import_option** ( name: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_method_add_import_option)

Add a specific import option (name and default value only). This function can only be called from [_get_import_options()](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__get_import_options).

---

<span id="class_EditorSceneFormatImporter_method_add_import_option_advanced"></span>

void **add_import_option_advanced** ( type: Variant.Type, name: [String](class_string.md#class_String), default_value: [Variant](class_variant.md#class_Variant), hint: PropertyHint = 0, hint_string: [String](class_string.md#class_String) = "", usage_flags: [int](class_int.md#class_int) = 6 ) [🔗](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_method_add_import_option_advanced)

Add a specific import option. This function can only be called from [_get_import_options()](class_editorsceneformatimporter.md#class_EditorSceneFormatImporter_private_method__get_import_options).
