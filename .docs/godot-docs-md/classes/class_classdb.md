<span id="class_ClassDB"></span>

## ClassDB

**Inherits:** [Object](class_object.md#class_Object)

A class information repository.

### Description

Provides access to metadata stored for every available engine class.

 **Note:** Script-defined classes with `class_name` are not part of **ClassDB**, so they will not return reflection data such as a method or property list. However, [GDExtension](class_gdextension.md#class_GDExtension)-defined classes *are* part of **ClassDB**, so they will return reflection data.

### Methods


| [bool](class_bool.md#class_bool) | [can_instantiate](class_classdb.md#class_ClassDB_method_can_instantiate) ( class: [StringName](class_stringname.md#class_StringName) ) const |
| --- | --- |
| [Variant](class_variant.md#class_Variant) | [class_call_static](class_classdb.md#class_ClassDB_method_class_call_static) ( class: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), ... ) vararg |
| [bool](class_bool.md#class_bool) | [class_exists](class_classdb.md#class_ClassDB_method_class_exists) ( class: [StringName](class_stringname.md#class_StringName) ) const |
| [APIType](class_classdb.md#enum_ClassDB_APIType) | [class_get_api_type](class_classdb.md#class_ClassDB_method_class_get_api_type) ( class: [StringName](class_stringname.md#class_StringName) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [class_get_enum_constants](class_classdb.md#class_ClassDB_method_class_get_enum_constants) ( class: [StringName](class_stringname.md#class_StringName), enum: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [class_get_enum_list](class_classdb.md#class_ClassDB_method_class_get_enum_list) ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [int](class_int.md#class_int) | [class_get_integer_constant](class_classdb.md#class_ClassDB_method_class_get_integer_constant) ( class: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) const |
| [StringName](class_stringname.md#class_StringName) | [class_get_integer_constant_enum](class_classdb.md#class_ClassDB_method_class_get_integer_constant_enum) ( class: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [class_get_integer_constant_list](class_classdb.md#class_ClassDB_method_class_get_integer_constant_list) ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [int](class_int.md#class_int) | [class_get_method_argument_count](class_classdb.md#class_ClassDB_method_class_get_method_argument_count) ( class: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [class_get_method_list](class_classdb.md#class_ClassDB_method_class_get_method_list) ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [Variant](class_variant.md#class_Variant) | [class_get_property](class_classdb.md#class_ClassDB_method_class_get_property) ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName) ) const |
| [Variant](class_variant.md#class_Variant) | [class_get_property_default_value](class_classdb.md#class_ClassDB_method_class_get_property_default_value) ( class: [StringName](class_stringname.md#class_StringName), property: [StringName](class_stringname.md#class_StringName) ) const |
| [StringName](class_stringname.md#class_StringName) | [class_get_property_getter](class_classdb.md#class_ClassDB_method_class_get_property_getter) ( class: [StringName](class_stringname.md#class_StringName), property: [StringName](class_stringname.md#class_StringName) ) |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [class_get_property_list](class_classdb.md#class_ClassDB_method_class_get_property_list) ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [StringName](class_stringname.md#class_StringName) | [class_get_property_setter](class_classdb.md#class_ClassDB_method_class_get_property_setter) ( class: [StringName](class_stringname.md#class_StringName), property: [StringName](class_stringname.md#class_StringName) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [class_get_signal](class_classdb.md#class_ClassDB_method_class_get_signal) ( class: [StringName](class_stringname.md#class_StringName), signal: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [class_get_signal_list](class_classdb.md#class_ClassDB_method_class_get_signal_list) ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [class_has_enum](class_classdb.md#class_ClassDB_method_class_has_enum) ( class: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [class_has_integer_constant](class_classdb.md#class_ClassDB_method_class_has_integer_constant) ( class: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [class_has_method](class_classdb.md#class_ClassDB_method_class_has_method) ( class: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [class_has_signal](class_classdb.md#class_ClassDB_method_class_has_signal) ( class: [StringName](class_stringname.md#class_StringName), signal: [StringName](class_stringname.md#class_StringName) ) const |
| Error | [class_set_property](class_classdb.md#class_ClassDB_method_class_set_property) ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_class_list](class_classdb.md#class_ClassDB_method_get_class_list) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_inheriters_from_class](class_classdb.md#class_ClassDB_method_get_inheriters_from_class) ( class: [StringName](class_stringname.md#class_StringName) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_parent_class](class_classdb.md#class_ClassDB_method_get_parent_class) ( class: [StringName](class_stringname.md#class_StringName) ) const |
| [Variant](class_variant.md#class_Variant) | [instantiate](class_classdb.md#class_ClassDB_method_instantiate) ( class: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [is_class_enabled](class_classdb.md#class_ClassDB_method_is_class_enabled) ( class: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [is_class_enum_bitfield](class_classdb.md#class_ClassDB_method_is_class_enum_bitfield) ( class: [StringName](class_stringname.md#class_StringName), enum: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [is_parent_class](class_classdb.md#class_ClassDB_method_is_parent_class) ( class: [StringName](class_stringname.md#class_StringName), inherits: [StringName](class_stringname.md#class_StringName) ) const |

---

### Enumerations

<span id="enum_ClassDB_APIType"></span>

enum **APIType**: [🔗](class_classdb.md#enum_ClassDB_APIType)

<span id="class_ClassDB_constant_API_CORE"></span>

[APIType](class_classdb.md#enum_ClassDB_APIType) **API_CORE** = `0`

Native Core class type.

<span id="class_ClassDB_constant_API_EDITOR"></span>

[APIType](class_classdb.md#enum_ClassDB_APIType) **API_EDITOR** = `1`

Native Editor class type.

<span id="class_ClassDB_constant_API_EXTENSION"></span>

[APIType](class_classdb.md#enum_ClassDB_APIType) **API_EXTENSION** = `2`

GDExtension class type.

<span id="class_ClassDB_constant_API_EDITOR_EXTENSION"></span>

[APIType](class_classdb.md#enum_ClassDB_APIType) **API_EDITOR_EXTENSION** = `3`

GDExtension Editor class type.

<span id="class_ClassDB_constant_API_NONE"></span>

[APIType](class_classdb.md#enum_ClassDB_APIType) **API_NONE** = `4`

Unknown class type.

---

### Method Descriptions

<span id="class_ClassDB_method_can_instantiate"></span>

[bool](class_bool.md#class_bool) **can_instantiate** ( class: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_can_instantiate)

Returns `true` if objects can be instantiated from the specified `class`, otherwise returns `false`.

---

<span id="class_ClassDB_method_class_call_static"></span>

[Variant](class_variant.md#class_Variant) **class_call_static** ( class: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), ... ) *vararg* [🔗](class_classdb.md#class_ClassDB_method_class_call_static)

Calls a static method on a class.

---

<span id="class_ClassDB_method_class_exists"></span>

[bool](class_bool.md#class_bool) **class_exists** ( class: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_exists)

Returns whether the specified `class` is available or not.

---

<span id="class_ClassDB_method_class_get_api_type"></span>

[APIType](class_classdb.md#enum_ClassDB_APIType) **class_get_api_type** ( class: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_api_type)

Returns the API type of the specified `class`.

---

<span id="class_ClassDB_method_class_get_enum_constants"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **class_get_enum_constants** ( class: [StringName](class_stringname.md#class_StringName), enum: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_enum_constants)

Returns an array with all the keys in `enum` of `class` or its ancestry.

---

<span id="class_ClassDB_method_class_get_enum_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **class_get_enum_list** ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_enum_list)

Returns an array with all the enums of `class` or its ancestry.

---

<span id="class_ClassDB_method_class_get_integer_constant"></span>

[int](class_int.md#class_int) **class_get_integer_constant** ( class: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_integer_constant)

Returns the value of the integer constant `name` of `class` or its ancestry. Always returns 0 when the constant could not be found.

---

<span id="class_ClassDB_method_class_get_integer_constant_enum"></span>

[StringName](class_stringname.md#class_StringName) **class_get_integer_constant_enum** ( class: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_integer_constant_enum)

Returns which enum the integer constant `name` of `class` or its ancestry belongs to.

---

<span id="class_ClassDB_method_class_get_integer_constant_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **class_get_integer_constant_list** ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_integer_constant_list)

Returns an array with the names all the integer constants of `class` or its ancestry.

---

<span id="class_ClassDB_method_class_get_method_argument_count"></span>

[int](class_int.md#class_int) **class_get_method_argument_count** ( class: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_method_argument_count)

Returns the number of arguments of the method `method` of `class` or its ancestry if `no_inheritance` is `false`.

---

<span id="class_ClassDB_method_class_get_method_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **class_get_method_list** ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_method_list)

Returns an array with all the methods of `class` or its ancestry if `no_inheritance` is `false`. Every element of the array is a [Dictionary](class_dictionary.md#class_Dictionary) with the following keys: `args`, `default_args`, `flags`, `id`, `name`, `return: (class_name, hint, hint_string, name, type, usage)`.

 **Note:** In exported release builds the debug info is not available, so the returned dictionaries will contain only method names.

---

<span id="class_ClassDB_method_class_get_property"></span>

[Variant](class_variant.md#class_Variant) **class_get_property** ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_property)

Returns the value of `property` of `object` or its ancestry.

---

<span id="class_ClassDB_method_class_get_property_default_value"></span>

[Variant](class_variant.md#class_Variant) **class_get_property_default_value** ( class: [StringName](class_stringname.md#class_StringName), property: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_property_default_value)

Returns the default value of `property` of `class` or its ancestor classes.

---

<span id="class_ClassDB_method_class_get_property_getter"></span>

[StringName](class_stringname.md#class_StringName) **class_get_property_getter** ( class: [StringName](class_stringname.md#class_StringName), property: [StringName](class_stringname.md#class_StringName) ) [🔗](class_classdb.md#class_ClassDB_method_class_get_property_getter)

Returns the getter method name of `property` of `class`.

---

<span id="class_ClassDB_method_class_get_property_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **class_get_property_list** ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_property_list)

Returns an array with all the properties of `class` or its ancestry if `no_inheritance` is `false`.

---

<span id="class_ClassDB_method_class_get_property_setter"></span>

[StringName](class_stringname.md#class_StringName) **class_get_property_setter** ( class: [StringName](class_stringname.md#class_StringName), property: [StringName](class_stringname.md#class_StringName) ) [🔗](class_classdb.md#class_ClassDB_method_class_get_property_setter)

Returns the setter method name of `property` of `class`.

---

<span id="class_ClassDB_method_class_get_signal"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **class_get_signal** ( class: [StringName](class_stringname.md#class_StringName), signal: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_signal)

Returns the `signal` data of `class` or its ancestry. The returned value is a [Dictionary](class_dictionary.md#class_Dictionary) with the following keys: `args`, `default_args`, `flags`, `id`, `name`, `return: (class_name, hint, hint_string, name, type, usage)`.

---

<span id="class_ClassDB_method_class_get_signal_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **class_get_signal_list** ( class: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_get_signal_list)

Returns an array with all the signals of `class` or its ancestry if `no_inheritance` is `false`. Every element of the array is a [Dictionary](class_dictionary.md#class_Dictionary) as described in [class_get_signal()](class_classdb.md#class_ClassDB_method_class_get_signal).

---

<span id="class_ClassDB_method_class_has_enum"></span>

[bool](class_bool.md#class_bool) **class_has_enum** ( class: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_has_enum)

Returns whether `class` or its ancestry has an enum called `name` or not.

---

<span id="class_ClassDB_method_class_has_integer_constant"></span>

[bool](class_bool.md#class_bool) **class_has_integer_constant** ( class: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_has_integer_constant)

Returns whether `class` or its ancestry has an integer constant called `name` or not.

---

<span id="class_ClassDB_method_class_has_method"></span>

[bool](class_bool.md#class_bool) **class_has_method** ( class: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_has_method)

Returns whether `class` (or its ancestry if `no_inheritance` is `false`) has a method called `method` or not.

---

<span id="class_ClassDB_method_class_has_signal"></span>

[bool](class_bool.md#class_bool) **class_has_signal** ( class: [StringName](class_stringname.md#class_StringName), signal: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_has_signal)

Returns whether `class` or its ancestry has a signal called `signal` or not.

---

<span id="class_ClassDB_method_class_set_property"></span>

Error **class_set_property** ( object: [Object](class_object.md#class_Object), property: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_classdb.md#class_ClassDB_method_class_set_property)

Sets `property` value of `object` to `value`.

---

<span id="class_ClassDB_method_get_class_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_class_list** ( ) *const* [🔗](class_classdb.md#class_ClassDB_method_get_class_list)

Returns the names of all engine classes available.

 **Note:** Script-defined classes with `class_name` are not included in this list. Use [ProjectSettings.get_global_class_list()](class_projectsettings.md#class_ProjectSettings_method_get_global_class_list) to get a list of script-defined classes instead.

---

<span id="class_ClassDB_method_get_inheriters_from_class"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_inheriters_from_class** ( class: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_get_inheriters_from_class)

Returns the names of all engine classes that directly or indirectly inherit from `class`.

---

<span id="class_ClassDB_method_get_parent_class"></span>

[StringName](class_stringname.md#class_StringName) **get_parent_class** ( class: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_get_parent_class)

Returns the parent class of `class`.

---

<span id="class_ClassDB_method_instantiate"></span>

[Variant](class_variant.md#class_Variant) **instantiate** ( class: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_instantiate)

Creates an instance of `class`.

---

<span id="class_ClassDB_method_is_class_enabled"></span>

[bool](class_bool.md#class_bool) **is_class_enabled** ( class: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_is_class_enabled)

Returns whether this `class` is enabled or not.

---

<span id="class_ClassDB_method_is_class_enum_bitfield"></span>

[bool](class_bool.md#class_bool) **is_class_enum_bitfield** ( class: [StringName](class_stringname.md#class_StringName), enum: [StringName](class_stringname.md#class_StringName), no_inheritance: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_classdb.md#class_ClassDB_method_is_class_enum_bitfield)

Returns whether `class` (or its ancestor classes if `no_inheritance` is `false`) has an enum called `enum` that is a bitfield.

---

<span id="class_ClassDB_method_is_parent_class"></span>

[bool](class_bool.md#class_bool) **is_parent_class** ( class: [StringName](class_stringname.md#class_StringName), inherits: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_classdb.md#class_ClassDB_method_is_parent_class)

Returns whether `inherits` is an ancestor of `class` or not.
