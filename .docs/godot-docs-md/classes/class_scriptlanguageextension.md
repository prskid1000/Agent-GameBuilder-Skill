<span id="class_ScriptLanguageExtension"></span>

## ScriptLanguageExtension

**Inherits:** [ScriptLanguage](class_scriptlanguage.md#class_ScriptLanguage) **<** [Object](class_object.md#class_Object)

.. container:: contribute

	There is currently no description for this class. Please help us by contributing one!

### Methods


| void | [_add_global_constant](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__add_global_constant) ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| --- | --- | --- | --- |
| void | [_add_named_global_constant](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__add_named_global_constant) ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| [String](class_string.md#class_String) | [_auto_indent_code](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__auto_indent_code) ( code: [String](class_string.md#class_String), from_line: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_can_inherit_from_file](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__can_inherit_from_file) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_can_make_function](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__can_make_function) ( ) | virtual | required | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_complete_code](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__complete_code) ( code: [String](class_string.md#class_String), path: [String](class_string.md#class_String), owner: [Object](class_object.md#class_Object) ) | virtual | required | const |
| [Object](class_object.md#class_Object) | [_create_script](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__create_script) ( ) | virtual | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_debug_get_current_stack_info](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_current_stack_info) ( ) | virtual | required |
| [String](class_string.md#class_String) | [_debug_get_error](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_error) ( ) | virtual | required | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_debug_get_globals](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_globals) ( max_subitems: [int](class_int.md#class_int), max_depth: [int](class_int.md#class_int) ) | virtual | required |
| [int](class_int.md#class_int) | [_debug_get_stack_level_count](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_count) ( ) | virtual | required | const |
| [String](class_string.md#class_String) | [_debug_get_stack_level_function](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_function) ( level: [int](class_int.md#class_int) ) | virtual | required | const |
| `void*` | [_debug_get_stack_level_instance](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_instance) ( level: [int](class_int.md#class_int) ) | virtual | required |
| [int](class_int.md#class_int) | [_debug_get_stack_level_line](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_line) ( level: [int](class_int.md#class_int) ) | virtual | required | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_debug_get_stack_level_locals](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_locals) ( level: [int](class_int.md#class_int), max_subitems: [int](class_int.md#class_int), max_depth: [int](class_int.md#class_int) ) | virtual | required |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_debug_get_stack_level_members](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_members) ( level: [int](class_int.md#class_int), max_subitems: [int](class_int.md#class_int), max_depth: [int](class_int.md#class_int) ) | virtual | required |
| [String](class_string.md#class_String) | [_debug_get_stack_level_source](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_source) ( level: [int](class_int.md#class_int) ) | virtual | required | const |
| [String](class_string.md#class_String) | [_debug_parse_stack_level_expression](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_parse_stack_level_expression) ( level: [int](class_int.md#class_int), expression: [String](class_string.md#class_String), max_subitems: [int](class_int.md#class_int), max_depth: [int](class_int.md#class_int) ) | virtual | required |
| [int](class_int.md#class_int) | [_find_function](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__find_function) ( function: [String](class_string.md#class_String), code: [String](class_string.md#class_String) ) | virtual | required | const |
| void | [_finish](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__finish) ( ) | virtual | required |
| void | [_frame](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__frame) ( ) | virtual | required |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_built_in_templates](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_built_in_templates) ( object: [StringName](class_stringname.md#class_StringName) ) | virtual | required | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_comment_delimiters](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_comment_delimiters) ( ) | virtual | required | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_doc_comment_delimiters](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_doc_comment_delimiters) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_extension](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_extension) ( ) | virtual | required | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_global_class_name](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_global_class_name) ( path: [String](class_string.md#class_String) ) | virtual | required | const |
| [String](class_string.md#class_String) | [_get_name](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_name) ( ) | virtual | required | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_public_annotations](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_public_annotations) ( ) | virtual | required | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_public_constants](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_public_constants) ( ) | virtual | required | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_public_functions](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_public_functions) ( ) | virtual | required | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_recognized_extensions](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_recognized_extensions) ( ) | virtual | required | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_reserved_words](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_reserved_words) ( ) | virtual | required | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_string_delimiters](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_string_delimiters) ( ) | virtual | required | const |
| [String](class_string.md#class_String) | [_get_type](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_type) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_handles_global_class_type](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__handles_global_class_type) ( type: [String](class_string.md#class_String) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_named_classes](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__has_named_classes) ( ) | virtual | const |
| void | [_init](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__init) ( ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_is_control_flow_keyword](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__is_control_flow_keyword) ( keyword: [String](class_string.md#class_String) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_using_templates](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__is_using_templates) ( ) | virtual | required |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_lookup_code](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__lookup_code) ( code: [String](class_string.md#class_String), symbol: [String](class_string.md#class_String), path: [String](class_string.md#class_String), owner: [Object](class_object.md#class_Object) ) | virtual | required | const |
| [String](class_string.md#class_String) | [_make_function](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__make_function) ( class_name: [String](class_string.md#class_String), function_name: [String](class_string.md#class_String), function_args: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) | virtual | required | const |
| [Script](class_script.md#class_Script) | [_make_template](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__make_template) ( template: [String](class_string.md#class_String), class_name: [String](class_string.md#class_String), base_class_name: [String](class_string.md#class_String) ) | virtual | required | const |
| Error | [_open_in_external_editor](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__open_in_external_editor) ( script: [Script](class_script.md#class_Script), line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_overrides_external_editor](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__overrides_external_editor) ( ) | virtual | required |
| [ScriptNameCasing](class_scriptlanguage.md#enum_ScriptLanguage_ScriptNameCasing) | [_preferred_file_name_casing](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__preferred_file_name_casing) ( ) | virtual | const |
| [int](class_int.md#class_int) | [_profiling_get_accumulated_data](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_get_accumulated_data) ( info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class_int) ) | virtual | required |
| [int](class_int.md#class_int) | [_profiling_get_frame_data](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_get_frame_data) ( info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class_int) ) | virtual | required |
| void | [_profiling_set_save_native_calls](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_set_save_native_calls) ( enable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_profiling_start](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_start) ( ) | virtual | required |
| void | [_profiling_stop](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_stop) ( ) | virtual | required |
| void | [_reload_all_scripts](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__reload_all_scripts) ( ) | virtual | required |
| void | [_reload_scripts](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__reload_scripts) ( scripts: [Array](class_array.md#class_Array), soft_reload: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_reload_tool_script](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__reload_tool_script) ( script: [Script](class_script.md#class_Script), soft_reload: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_remove_named_global_constant](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__remove_named_global_constant) ( name: [StringName](class_stringname.md#class_StringName) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_supports_builtin_mode](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__supports_builtin_mode) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_supports_documentation](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__supports_documentation) ( ) | virtual | required | const |
| void | [_thread_enter](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__thread_enter) ( ) | virtual | required |
| void | [_thread_exit](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__thread_exit) ( ) | virtual | required |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_validate](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__validate) ( script: [String](class_string.md#class_String), path: [String](class_string.md#class_String), validate_functions: [bool](class_bool.md#class_bool), validate_errors: [bool](class_bool.md#class_bool), validate_warnings: [bool](class_bool.md#class_bool), validate_safe_lines: [bool](class_bool.md#class_bool) ) | virtual | required | const |
| [String](class_string.md#class_String) | [_validate_path](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__validate_path) ( path: [String](class_string.md#class_String) ) | virtual | required | const |

---

### Enumerations

<span id="enum_ScriptLanguageExtension_LookupResultType"></span>

enum **LookupResultType**: [🔗](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType)

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_SCRIPT_LOCATION"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_SCRIPT_LOCATION** = `0`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_CLASS"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_CLASS** = `1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_CLASS_CONSTANT"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_CLASS_CONSTANT** = `2`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_CLASS_PROPERTY"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_CLASS_PROPERTY** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_CLASS_METHOD"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_CLASS_METHOD** = `4`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_CLASS_SIGNAL"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_CLASS_SIGNAL** = `5`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_CLASS_ENUM"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_CLASS_ENUM** = `6`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_CLASS_TBD_GLOBALSCOPE"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_CLASS_TBD_GLOBALSCOPE** = `7`

**Deprecated:** This constant may be changed or removed in future versions.

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_CLASS_ANNOTATION"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_CLASS_ANNOTATION** = `8`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_LOCAL_CONSTANT"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_LOCAL_CONSTANT** = `9`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_LOCAL_VARIABLE"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_LOCAL_VARIABLE** = `10`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_LOOKUP_RESULT_MAX"></span>

[LookupResultType](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_LookupResultType) **LOOKUP_RESULT_MAX** = `11`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

<span id="enum_ScriptLanguageExtension_CodeCompletionLocation"></span>

enum **CodeCompletionLocation**: [🔗](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionLocation)

<span id="class_ScriptLanguageExtension_constant_LOCATION_LOCAL"></span>

[CodeCompletionLocation](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionLocation) **LOCATION_LOCAL** = `0`

The option is local to the location of the code completion query - e.g. a local variable. Subsequent value of location represent options from the outer class, the exact value represent how far they are (in terms of inner classes).

<span id="class_ScriptLanguageExtension_constant_LOCATION_PARENT_MASK"></span>

[CodeCompletionLocation](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionLocation) **LOCATION_PARENT_MASK** = `256`

The option is from the containing class or a parent class, relative to the location of the code completion query. Perform a bitwise OR with the class depth (e.g. `0` for the local class, `1` for the parent, `2` for the grandparent, etc.) to store the depth of an option in the class or a parent class.

<span id="class_ScriptLanguageExtension_constant_LOCATION_OTHER_USER_CODE"></span>

[CodeCompletionLocation](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionLocation) **LOCATION_OTHER_USER_CODE** = `512`

The option is from user code which is not local and not in a derived class (e.g. Autoload Singletons).

<span id="class_ScriptLanguageExtension_constant_LOCATION_OTHER"></span>

[CodeCompletionLocation](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionLocation) **LOCATION_OTHER** = `1024`

The option is from other engine code, not covered by the other enum constants - e.g. built-in classes.

---

<span id="enum_ScriptLanguageExtension_CodeCompletionKind"></span>

enum **CodeCompletionKind**: [🔗](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind)

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_CLASS"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_CLASS** = `0`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_FUNCTION"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_FUNCTION** = `1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_SIGNAL"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_SIGNAL** = `2`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_VARIABLE"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_VARIABLE** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_MEMBER"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_MEMBER** = `4`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_ENUM"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_ENUM** = `5`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_CONSTANT"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_CONSTANT** = `6`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_NODE_PATH"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_NODE_PATH** = `7`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_FILE_PATH"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_FILE_PATH** = `8`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_PLAIN_TEXT"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_PLAIN_TEXT** = `9`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ScriptLanguageExtension_constant_CODE_COMPLETION_KIND_MAX"></span>

[CodeCompletionKind](class_scriptlanguageextension.md#enum_ScriptLanguageExtension_CodeCompletionKind) **CODE_COMPLETION_KIND_MAX** = `10`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

### Method Descriptions

<span id="class_ScriptLanguageExtension_private_method__add_global_constant"></span>

void **_add_global_constant** ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__add_global_constant)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__add_named_global_constant"></span>

void **_add_named_global_constant** ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__add_named_global_constant)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__auto_indent_code"></span>

[String](class_string.md#class_String) **_auto_indent_code** ( code: [String](class_string.md#class_String), from_line: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__auto_indent_code)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__can_inherit_from_file"></span>

[bool](class_bool.md#class_bool) **_can_inherit_from_file** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__can_inherit_from_file)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__can_make_function"></span>

[bool](class_bool.md#class_bool) **_can_make_function** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__can_make_function)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__complete_code"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_complete_code** ( code: [String](class_string.md#class_String), path: [String](class_string.md#class_String), owner: [Object](class_object.md#class_Object) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__complete_code)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__create_script"></span>

[Object](class_object.md#class_Object) **_create_script** ( ) *virtual* *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__create_script)

**Deprecated:** This method is not called by the engine.

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_current_stack_info"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_debug_get_current_stack_info** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_current_stack_info)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_error"></span>

[String](class_string.md#class_String) **_debug_get_error** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_error)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_globals"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_debug_get_globals** ( max_subitems: [int](class_int.md#class_int), max_depth: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_globals)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_stack_level_count"></span>

[int](class_int.md#class_int) **_debug_get_stack_level_count** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_count)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_stack_level_function"></span>

[String](class_string.md#class_String) **_debug_get_stack_level_function** ( level: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_function)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_stack_level_instance"></span>

`void*` **_debug_get_stack_level_instance** ( level: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_instance)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_stack_level_line"></span>

[int](class_int.md#class_int) **_debug_get_stack_level_line** ( level: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_line)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_stack_level_locals"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_debug_get_stack_level_locals** ( level: [int](class_int.md#class_int), max_subitems: [int](class_int.md#class_int), max_depth: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_locals)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_stack_level_members"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_debug_get_stack_level_members** ( level: [int](class_int.md#class_int), max_subitems: [int](class_int.md#class_int), max_depth: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_members)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__debug_get_stack_level_source"></span>

[String](class_string.md#class_String) **_debug_get_stack_level_source** ( level: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_get_stack_level_source)

Returns the source associated with a given debug stack position.

---

<span id="class_ScriptLanguageExtension_private_method__debug_parse_stack_level_expression"></span>

[String](class_string.md#class_String) **_debug_parse_stack_level_expression** ( level: [int](class_int.md#class_int), expression: [String](class_string.md#class_String), max_subitems: [int](class_int.md#class_int), max_depth: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__debug_parse_stack_level_expression)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__find_function"></span>

[int](class_int.md#class_int) **_find_function** ( function: [String](class_string.md#class_String), code: [String](class_string.md#class_String) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__find_function)

Returns the line where the function is defined in the code, or `-1` if the function is not present.

---

<span id="class_ScriptLanguageExtension_private_method__finish"></span>

void **_finish** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__finish)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__frame"></span>

void **_frame** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__frame)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_built_in_templates"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_built_in_templates** ( object: [StringName](class_stringname.md#class_StringName) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_built_in_templates)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_comment_delimiters"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_comment_delimiters** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_comment_delimiters)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_doc_comment_delimiters"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_doc_comment_delimiters** ( ) *virtual* *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_doc_comment_delimiters)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_extension"></span>

[String](class_string.md#class_String) **_get_extension** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_extension)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_global_class_name"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_global_class_name** ( path: [String](class_string.md#class_String) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_global_class_name)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_name"></span>

[String](class_string.md#class_String) **_get_name** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_name)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_public_annotations"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_public_annotations** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_public_annotations)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_public_constants"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_public_constants** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_public_constants)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_public_functions"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_public_functions** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_public_functions)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_recognized_extensions"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_recognized_extensions** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_recognized_extensions)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_reserved_words"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_reserved_words** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_reserved_words)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_string_delimiters"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_string_delimiters** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_string_delimiters)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__get_type"></span>

[String](class_string.md#class_String) **_get_type** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__get_type)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__handles_global_class_type"></span>

[bool](class_bool.md#class_bool) **_handles_global_class_type** ( type: [String](class_string.md#class_String) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__handles_global_class_type)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__has_named_classes"></span>

[bool](class_bool.md#class_bool) **_has_named_classes** ( ) *virtual* *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__has_named_classes)

**Deprecated:** This method is not called by the engine.

---

<span id="class_ScriptLanguageExtension_private_method__init"></span>

void **_init** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__init)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__is_control_flow_keyword"></span>

[bool](class_bool.md#class_bool) **_is_control_flow_keyword** ( keyword: [String](class_string.md#class_String) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__is_control_flow_keyword)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__is_using_templates"></span>

[bool](class_bool.md#class_bool) **_is_using_templates** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__is_using_templates)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__lookup_code"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_lookup_code** ( code: [String](class_string.md#class_String), symbol: [String](class_string.md#class_String), path: [String](class_string.md#class_String), owner: [Object](class_object.md#class_Object) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__lookup_code)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__make_function"></span>

[String](class_string.md#class_String) **_make_function** ( class_name: [String](class_string.md#class_String), function_name: [String](class_string.md#class_String), function_args: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__make_function)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__make_template"></span>

[Script](class_script.md#class_Script) **_make_template** ( template: [String](class_string.md#class_String), class_name: [String](class_string.md#class_String), base_class_name: [String](class_string.md#class_String) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__make_template)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__open_in_external_editor"></span>

Error **_open_in_external_editor** ( script: [Script](class_script.md#class_Script), line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__open_in_external_editor)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__overrides_external_editor"></span>

[bool](class_bool.md#class_bool) **_overrides_external_editor** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__overrides_external_editor)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__preferred_file_name_casing"></span>

[ScriptNameCasing](class_scriptlanguage.md#enum_ScriptLanguage_ScriptNameCasing) **_preferred_file_name_casing** ( ) *virtual* *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__preferred_file_name_casing)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__profiling_get_accumulated_data"></span>

[int](class_int.md#class_int) **_profiling_get_accumulated_data** ( info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_get_accumulated_data)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__profiling_get_frame_data"></span>

[int](class_int.md#class_int) **_profiling_get_frame_data** ( info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_get_frame_data)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__profiling_set_save_native_calls"></span>

void **_profiling_set_save_native_calls** ( enable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_set_save_native_calls)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__profiling_start"></span>

void **_profiling_start** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_start)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__profiling_stop"></span>

void **_profiling_stop** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__profiling_stop)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__reload_all_scripts"></span>

void **_reload_all_scripts** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__reload_all_scripts)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__reload_scripts"></span>

void **_reload_scripts** ( scripts: [Array](class_array.md#class_Array), soft_reload: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__reload_scripts)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__reload_tool_script"></span>

void **_reload_tool_script** ( script: [Script](class_script.md#class_Script), soft_reload: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__reload_tool_script)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__remove_named_global_constant"></span>

void **_remove_named_global_constant** ( name: [StringName](class_stringname.md#class_StringName) ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__remove_named_global_constant)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__supports_builtin_mode"></span>

[bool](class_bool.md#class_bool) **_supports_builtin_mode** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__supports_builtin_mode)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__supports_documentation"></span>

[bool](class_bool.md#class_bool) **_supports_documentation** ( ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__supports_documentation)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__thread_enter"></span>

void **_thread_enter** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__thread_enter)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__thread_exit"></span>

void **_thread_exit** ( ) *virtual* |required| [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__thread_exit)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__validate"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_validate** ( script: [String](class_string.md#class_String), path: [String](class_string.md#class_String), validate_functions: [bool](class_bool.md#class_bool), validate_errors: [bool](class_bool.md#class_bool), validate_warnings: [bool](class_bool.md#class_bool), validate_safe_lines: [bool](class_bool.md#class_bool) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__validate)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_ScriptLanguageExtension_private_method__validate_path"></span>

[String](class_string.md#class_String) **_validate_path** ( path: [String](class_string.md#class_String) ) *virtual* |required| *const* [🔗](class_scriptlanguageextension.md#class_ScriptLanguageExtension_private_method__validate_path)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
