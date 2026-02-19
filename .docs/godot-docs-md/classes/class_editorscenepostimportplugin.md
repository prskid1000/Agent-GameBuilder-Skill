<span id="class_EditorScenePostImportPlugin"></span>

## EditorScenePostImportPlugin

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Plugin to control and modifying the process of importing a scene.

### Description

This plugin type exists to modify the process of importing scenes, allowing to change the content as well as add importer options at every stage of the process.

### Methods


| void | [_get_import_options](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_import_options) ( path: [String](class_string.md#class_String) ) virtual |
| --- | --- |
| void | [_get_internal_import_options](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_internal_import_options) ( category: [int](class_int.md#class_int) ) virtual |
| [Variant](class_variant.md#class_Variant) | [_get_internal_option_update_view_required](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_internal_option_update_view_required) ( category: [int](class_int.md#class_int), option: [String](class_string.md#class_String) ) | virtual | const |
| [Variant](class_variant.md#class_Variant) | [_get_internal_option_visibility](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_internal_option_visibility) ( category: [int](class_int.md#class_int), for_animation: [bool](class_bool.md#class_bool), option: [String](class_string.md#class_String) ) | virtual | const |
| [Variant](class_variant.md#class_Variant) | [_get_option_visibility](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_option_visibility) ( path: [String](class_string.md#class_String), for_animation: [bool](class_bool.md#class_bool), option: [String](class_string.md#class_String) ) | virtual | const |
| void | [_internal_process](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__internal_process) ( category: [int](class_int.md#class_int), base_node: [Node](class_node.md#class_Node), node: [Node](class_node.md#class_Node), resource: [Resource](class_resource.md#class_Resource) ) virtual |
| void | [_post_process](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__post_process) ( scene: [Node](class_node.md#class_Node) ) virtual |
| void | [_pre_process](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__pre_process) ( scene: [Node](class_node.md#class_Node) ) virtual |
| void | [add_import_option](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_add_import_option) ( name: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) |
| void | [add_import_option_advanced](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_add_import_option_advanced) ( type: Variant.Type, name: [String](class_string.md#class_String), default_value: [Variant](class_variant.md#class_Variant), hint: PropertyHint = 0, hint_string: [String](class_string.md#class_String) = "", usage_flags: [int](class_int.md#class_int) = 6 ) |
| [Variant](class_variant.md#class_Variant) | [get_option_value](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_get_option_value) ( name: [StringName](class_stringname.md#class_StringName) ) const |

---

### Enumerations

<span id="enum_EditorScenePostImportPlugin_InternalImportCategory"></span>

enum **InternalImportCategory**: [🔗](class_editorscenepostimportplugin.md#enum_EditorScenePostImportPlugin_InternalImportCategory)

<span id="class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_NODE"></span>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum_EditorScenePostImportPlugin_InternalImportCategory) **INTERNAL_IMPORT_CATEGORY_NODE** = `0`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_MESH_3D_NODE"></span>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum_EditorScenePostImportPlugin_InternalImportCategory) **INTERNAL_IMPORT_CATEGORY_MESH_3D_NODE** = `1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_MESH"></span>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum_EditorScenePostImportPlugin_InternalImportCategory) **INTERNAL_IMPORT_CATEGORY_MESH** = `2`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_MATERIAL"></span>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum_EditorScenePostImportPlugin_InternalImportCategory) **INTERNAL_IMPORT_CATEGORY_MATERIAL** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_ANIMATION"></span>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum_EditorScenePostImportPlugin_InternalImportCategory) **INTERNAL_IMPORT_CATEGORY_ANIMATION** = `4`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_ANIMATION_NODE"></span>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum_EditorScenePostImportPlugin_InternalImportCategory) **INTERNAL_IMPORT_CATEGORY_ANIMATION_NODE** = `5`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_SKELETON_3D_NODE"></span>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum_EditorScenePostImportPlugin_InternalImportCategory) **INTERNAL_IMPORT_CATEGORY_SKELETON_3D_NODE** = `6`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_MAX"></span>

[InternalImportCategory](class_editorscenepostimportplugin.md#enum_EditorScenePostImportPlugin_InternalImportCategory) **INTERNAL_IMPORT_CATEGORY_MAX** = `7`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

### Method Descriptions

<span id="class_EditorScenePostImportPlugin_private_method__get_import_options"></span>

void **_get_import_options** ( path: [String](class_string.md#class_String) ) *virtual* [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_import_options)

Override to add general import options. These will appear in the main import dock on the editor. Add options via [add_import_option()](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_add_import_option) and [add_import_option_advanced()](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_add_import_option_advanced).

---

<span id="class_EditorScenePostImportPlugin_private_method__get_internal_import_options"></span>

void **_get_internal_import_options** ( category: [int](class_int.md#class_int) ) *virtual* [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_internal_import_options)

Override to add internal import options. These will appear in the 3D scene import dialog. Add options via [add_import_option()](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_add_import_option) and [add_import_option_advanced()](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_add_import_option_advanced).

---

<span id="class_EditorScenePostImportPlugin_private_method__get_internal_option_update_view_required"></span>

[Variant](class_variant.md#class_Variant) **_get_internal_option_update_view_required** ( category: [int](class_int.md#class_int), option: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_internal_option_update_view_required)

Should return `true` if the 3D view of the import dialog needs to update when changing the given option.

---

<span id="class_EditorScenePostImportPlugin_private_method__get_internal_option_visibility"></span>

[Variant](class_variant.md#class_Variant) **_get_internal_option_visibility** ( category: [int](class_int.md#class_int), for_animation: [bool](class_bool.md#class_bool), option: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_internal_option_visibility)

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

---

<span id="class_EditorScenePostImportPlugin_private_method__get_option_visibility"></span>

[Variant](class_variant.md#class_Variant) **_get_option_visibility** ( path: [String](class_string.md#class_String), for_animation: [bool](class_bool.md#class_bool), option: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_option_visibility)

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

---

<span id="class_EditorScenePostImportPlugin_private_method__internal_process"></span>

void **_internal_process** ( category: [int](class_int.md#class_int), base_node: [Node](class_node.md#class_Node), node: [Node](class_node.md#class_Node), resource: [Resource](class_resource.md#class_Resource) ) *virtual* [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__internal_process)

Process a specific node or resource for a given category.

---

<span id="class_EditorScenePostImportPlugin_private_method__post_process"></span>

void **_post_process** ( scene: [Node](class_node.md#class_Node) ) *virtual* [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__post_process)

Post-process the scene. This function is called after the final scene has been configured.

---

<span id="class_EditorScenePostImportPlugin_private_method__pre_process"></span>

void **_pre_process** ( scene: [Node](class_node.md#class_Node) ) *virtual* [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__pre_process)

Pre-process the scene. This function is called right after the scene format loader loaded the scene and no changes have been made.

Pre-process may be used to adjust internal import options in the `"nodes"`, `"meshes"`, `"animations"` or `"materials"` keys inside `get_option_value("_subresources")`.

---

<span id="class_EditorScenePostImportPlugin_method_add_import_option"></span>

void **add_import_option** ( name: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_add_import_option)

Add a specific import option (name and default value only). This function can only be called from [_get_import_options()](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_import_options) and [_get_internal_import_options()](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_internal_import_options).

---

<span id="class_EditorScenePostImportPlugin_method_add_import_option_advanced"></span>

void **add_import_option_advanced** ( type: Variant.Type, name: [String](class_string.md#class_String), default_value: [Variant](class_variant.md#class_Variant), hint: PropertyHint = 0, hint_string: [String](class_string.md#class_String) = "", usage_flags: [int](class_int.md#class_int) = 6 ) [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_add_import_option_advanced)

Add a specific import option. This function can only be called from [_get_import_options()](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_import_options) and [_get_internal_import_options()](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_private_method__get_internal_import_options).

---

<span id="class_EditorScenePostImportPlugin_method_get_option_value"></span>

[Variant](class_variant.md#class_Variant) **get_option_value** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_editorscenepostimportplugin.md#class_EditorScenePostImportPlugin_method_get_option_value)

Query the value of an option. This function can only be called from those querying visibility, or processing.
