<span id="class_ScriptExtension"></span>

## ScriptExtension

**Inherits:** [Script](class_script.md#class_Script) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

.. container:: contribute

	There is currently no description for this class. Please help us by contributing one!

### Methods


| [bool](class_bool.md#class_bool) | [_can_instantiate](class_scriptextension.md#class_ScriptExtension_private_method__can_instantiate) ( ) | virtual | required | const |
| --- | --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_editor_can_reload_from_file](class_scriptextension.md#class_ScriptExtension_private_method__editor_can_reload_from_file) ( ) | virtual | required |
| [Script](class_script.md#class_Script) | [_get_base_script](class_scriptextension.md#class_ScriptExtension_private_method__get_base_script) ( ) | virtual | required | const |
| [String](class_string.md#class_String) | [_get_class_icon_path](class_scriptextension.md#class_ScriptExtension_private_method__get_class_icon_path) ( ) | virtual | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_constants](class_scriptextension.md#class_ScriptExtension_private_method__get_constants) ( ) | virtual | required | const |
| [StringName](class_stringname.md#class_StringName) | [_get_doc_class_name](class_scriptextension.md#class_ScriptExtension_private_method__get_doc_class_name) ( ) | virtual | required | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_documentation](class_scriptextension.md#class_ScriptExtension_private_method__get_documentation) ( ) | virtual | required | const |
| [StringName](class_stringname.md#class_StringName) | [_get_global_name](class_scriptextension.md#class_ScriptExtension_private_method__get_global_name) ( ) | virtual | required | const |
| [StringName](class_stringname.md#class_StringName) | [_get_instance_base_type](class_scriptextension.md#class_ScriptExtension_private_method__get_instance_base_type) ( ) | virtual | required | const |
| [ScriptLanguage](class_scriptlanguage.md#class_ScriptLanguage) | [_get_language](class_scriptextension.md#class_ScriptExtension_private_method__get_language) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_member_line](class_scriptextension.md#class_ScriptExtension_private_method__get_member_line) ( member: [StringName](class_stringname.md#class_StringName) ) | virtual | required | const |
| [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] | [_get_members](class_scriptextension.md#class_ScriptExtension_private_method__get_members) ( ) | virtual | required | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_method_info](class_scriptextension.md#class_ScriptExtension_private_method__get_method_info) ( method: [StringName](class_stringname.md#class_StringName) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_get_property_default_value](class_scriptextension.md#class_ScriptExtension_private_method__get_property_default_value) ( property: [StringName](class_stringname.md#class_StringName) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_get_rpc_config](class_scriptextension.md#class_ScriptExtension_private_method__get_rpc_config) ( ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_get_script_method_argument_count](class_scriptextension.md#class_ScriptExtension_private_method__get_script_method_argument_count) ( method: [StringName](class_stringname.md#class_StringName) ) | virtual | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_script_method_list](class_scriptextension.md#class_ScriptExtension_private_method__get_script_method_list) ( ) | virtual | required | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_script_property_list](class_scriptextension.md#class_ScriptExtension_private_method__get_script_property_list) ( ) | virtual | required | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_script_signal_list](class_scriptextension.md#class_ScriptExtension_private_method__get_script_signal_list) ( ) | virtual | required | const |
| [String](class_string.md#class_String) | [_get_source_code](class_scriptextension.md#class_ScriptExtension_private_method__get_source_code) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_method](class_scriptextension.md#class_ScriptExtension_private_method__has_method) ( method: [StringName](class_stringname.md#class_StringName) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_property_default_value](class_scriptextension.md#class_ScriptExtension_private_method__has_property_default_value) ( property: [StringName](class_stringname.md#class_StringName) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_script_signal](class_scriptextension.md#class_ScriptExtension_private_method__has_script_signal) ( signal: [StringName](class_stringname.md#class_StringName) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_source_code](class_scriptextension.md#class_ScriptExtension_private_method__has_source_code) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_static_method](class_scriptextension.md#class_ScriptExtension_private_method__has_static_method) ( method: [StringName](class_stringname.md#class_StringName) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_inherits_script](class_scriptextension.md#class_ScriptExtension_private_method__inherits_script) ( script: [Script](class_script.md#class_Script) ) | virtual | required | const |
| `void*` | [_instance_create](class_scriptextension.md#class_ScriptExtension_private_method__instance_create) ( for_object: [Object](class_object.md#class_Object) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_instance_has](class_scriptextension.md#class_ScriptExtension_private_method__instance_has) ( object: [Object](class_object.md#class_Object) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_abstract](class_scriptextension.md#class_ScriptExtension_private_method__is_abstract) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_placeholder_fallback_enabled](class_scriptextension.md#class_ScriptExtension_private_method__is_placeholder_fallback_enabled) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_tool](class_scriptextension.md#class_ScriptExtension_private_method__is_tool) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_valid](class_scriptextension.md#class_ScriptExtension_private_method__is_valid) ( ) | virtual | required | const |
| void | [_placeholder_erased](class_scriptextension.md#class_ScriptExtension_private_method__placeholder_erased) ( placeholder: `void*` ) virtual |
| `void*` | [_placeholder_instance_create](class_scriptextension.md#class_ScriptExtension_private_method__placeholder_instance_create) ( for_object: [Object](class_object.md#class_Object) ) | virtual | required | const |
| Error | [_reload](class_scriptextension.md#class_ScriptExtension_private_method__reload) ( keep_state: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_set_source_code](class_scriptextension.md#class_ScriptExtension_private_method__set_source_code) ( code: [String](class_string.md#class_String) ) | virtual | required |
| void | [_update_exports](class_scriptextension.md#class_ScriptExtension_private_method__update_exports) ( ) | virtual | required |

---

### Method Descriptions

<span id="class_ScriptExtension_private_method__can_instantiate"></span>

[bool](class_bool.md#class_bool) **_can_instantiate** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__can_instantiate)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__editor_can_reload_from_file"></span>

[bool](class_bool.md#class_bool) **_editor_can_reload_from_file** ( ) *virtual* |required| [🔗](class_scriptextension.md#class_ScriptExtension_private_method__editor_can_reload_from_file)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_base_script"></span>

[Script](class_script.md#class_Script) **_get_base_script** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_base_script)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_class_icon_path"></span>

[String](class_string.md#class_String) **_get_class_icon_path** ( ) *virtual* *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_class_icon_path)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_constants"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_constants** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_constants)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_doc_class_name"></span>

[StringName](class_stringname.md#class_StringName) **_get_doc_class_name** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_doc_class_name)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_documentation"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_documentation** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_documentation)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_global_name"></span>

[StringName](class_stringname.md#class_StringName) **_get_global_name** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_global_name)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_instance_base_type"></span>

[StringName](class_stringname.md#class_StringName) **_get_instance_base_type** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_instance_base_type)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_language"></span>

[ScriptLanguage](class_scriptlanguage.md#class_ScriptLanguage) **_get_language** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_language)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_member_line"></span>

[int](class_int.md#class_int) **_get_member_line** ( member: [StringName](class_stringname.md#class_StringName) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_member_line)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_members"></span>

[Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] **_get_members** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_members)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_method_info"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_method_info** ( method: [StringName](class_stringname.md#class_StringName) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_method_info)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_property_default_value"></span>

[Variant](class_variant.md#class_Variant) **_get_property_default_value** ( property: [StringName](class_stringname.md#class_StringName) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_property_default_value)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_rpc_config"></span>

[Variant](class_variant.md#class_Variant) **_get_rpc_config** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_rpc_config)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_script_method_argument_count"></span>

[Variant](class_variant.md#class_Variant) **_get_script_method_argument_count** ( method: [StringName](class_stringname.md#class_StringName) ) *virtual* *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_script_method_argument_count)

Return the expected argument count for the given `method`, or `null` if it can't be determined (which will then fall back to the default behavior).

---

<span id="class_ScriptExtension_private_method__get_script_method_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_script_method_list** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_script_method_list)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_script_property_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_script_property_list** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_script_property_list)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_script_signal_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_script_signal_list** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_script_signal_list)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__get_source_code"></span>

[String](class_string.md#class_String) **_get_source_code** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__get_source_code)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__has_method"></span>

[bool](class_bool.md#class_bool) **_has_method** ( method: [StringName](class_stringname.md#class_StringName) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__has_method)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__has_property_default_value"></span>

[bool](class_bool.md#class_bool) **_has_property_default_value** ( property: [StringName](class_stringname.md#class_StringName) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__has_property_default_value)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__has_script_signal"></span>

[bool](class_bool.md#class_bool) **_has_script_signal** ( signal: [StringName](class_stringname.md#class_StringName) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__has_script_signal)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__has_source_code"></span>

[bool](class_bool.md#class_bool) **_has_source_code** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__has_source_code)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__has_static_method"></span>

[bool](class_bool.md#class_bool) **_has_static_method** ( method: [StringName](class_stringname.md#class_StringName) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__has_static_method)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__inherits_script"></span>

[bool](class_bool.md#class_bool) **_inherits_script** ( script: [Script](class_script.md#class_Script) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__inherits_script)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__instance_create"></span>

`void*` **_instance_create** ( for_object: [Object](class_object.md#class_Object) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__instance_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__instance_has"></span>

[bool](class_bool.md#class_bool) **_instance_has** ( object: [Object](class_object.md#class_Object) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__instance_has)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__is_abstract"></span>

[bool](class_bool.md#class_bool) **_is_abstract** ( ) *virtual* *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__is_abstract)

Returns `true` if the script is an abstract script. Abstract scripts cannot be instantiated directly, instead other scripts should inherit them. Abstract scripts will be either unselectable or hidden in the Create New Node dialog (unselectable if there are non-abstract classes inheriting it, otherwise hidden).

---

<span id="class_ScriptExtension_private_method__is_placeholder_fallback_enabled"></span>

[bool](class_bool.md#class_bool) **_is_placeholder_fallback_enabled** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__is_placeholder_fallback_enabled)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__is_tool"></span>

[bool](class_bool.md#class_bool) **_is_tool** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__is_tool)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__is_valid"></span>

[bool](class_bool.md#class_bool) **_is_valid** ( ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__is_valid)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__placeholder_erased"></span>

void **_placeholder_erased** ( placeholder: `void*` ) *virtual* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__placeholder_erased)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__placeholder_instance_create"></span>

`void*` **_placeholder_instance_create** ( for_object: [Object](class_object.md#class_Object) ) *virtual* |required| *const* [🔗](class_scriptextension.md#class_ScriptExtension_private_method__placeholder_instance_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__reload"></span>

Error **_reload** ( keep_state: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_scriptextension.md#class_ScriptExtension_private_method__reload)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__set_source_code"></span>

void **_set_source_code** ( code: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_scriptextension.md#class_ScriptExtension_private_method__set_source_code)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptExtension_private_method__update_exports"></span>

void **_update_exports** ( ) *virtual* |required| [🔗](class_scriptextension.md#class_ScriptExtension_private_method__update_exports)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
