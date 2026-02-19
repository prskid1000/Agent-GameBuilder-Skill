<span id="class_Script"></span>

## Script

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CSharpScript](class_csharpscript.md#class_CSharpScript), [GDScript](class_gdscript.md#class_GDScript), [ScriptExtension](class_scriptextension.md#class_ScriptExtension)

A class stored as a resource.

### Description

A class stored as a resource. A script extends the functionality of all objects that instantiate it.

This is the base class for all scripts and should not be used directly. Trying to create a new script with this class will result in an error.

The `new` method of a script subclass creates a new instance. [Object.set_script()](class_object.md#class_Object_method_set_script) extends an existing object, if that object's class matches one of the script's base classes.

### Tutorials

- [Scripting documentation index](../tutorials/scripting/index.md)

### Properties


| [String](class_string.md#class_String) | [source_code](class_script.md#class_Script_property_source_code) |
| --- | --- |

### Methods


| [bool](class_bool.md#class_bool) | [can_instantiate](class_script.md#class_Script_method_can_instantiate) ( ) const |
| --- | --- |
| [Script](class_script.md#class_Script) | [get_base_script](class_script.md#class_Script_method_get_base_script) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_global_name](class_script.md#class_Script_method_get_global_name) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_instance_base_type](class_script.md#class_Script_method_get_instance_base_type) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_property_default_value](class_script.md#class_Script_method_get_property_default_value) ( property: [StringName](class_stringname.md#class_StringName) ) |
| [Variant](class_variant.md#class_Variant) | [get_rpc_config](class_script.md#class_Script_method_get_rpc_config) ( ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_script_constant_map](class_script.md#class_Script_method_get_script_constant_map) ( ) |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_script_method_list](class_script.md#class_Script_method_get_script_method_list) ( ) |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_script_property_list](class_script.md#class_Script_method_get_script_property_list) ( ) |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_script_signal_list](class_script.md#class_Script_method_get_script_signal_list) ( ) |
| [bool](class_bool.md#class_bool) | [has_script_signal](class_script.md#class_Script_method_has_script_signal) ( signal_name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_source_code](class_script.md#class_Script_method_has_source_code) ( ) const |
| [bool](class_bool.md#class_bool) | [instance_has](class_script.md#class_Script_method_instance_has) ( base_object: [Object](class_object.md#class_Object) ) const |
| [bool](class_bool.md#class_bool) | [is_abstract](class_script.md#class_Script_method_is_abstract) ( ) const |
| [bool](class_bool.md#class_bool) | [is_tool](class_script.md#class_Script_method_is_tool) ( ) const |
| Error | [reload](class_script.md#class_Script_method_reload) ( keep_state: [bool](class_bool.md#class_bool) = false ) |

---

### Property Descriptions

<span id="class_Script_property_source_code"></span>

[String](class_string.md#class_String) **source_code** [🔗](class_script.md#class_Script_property_source_code)

- void **set_source_code** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_source_code** ( )

The script source code or an empty string if source code is not available. When set, does not reload the class implementation automatically.

---

### Method Descriptions

<span id="class_Script_method_can_instantiate"></span>

[bool](class_bool.md#class_bool) **can_instantiate** ( ) *const* [🔗](class_script.md#class_Script_method_can_instantiate)

Returns `true` if the script can be instantiated.

---

<span id="class_Script_method_get_base_script"></span>

[Script](class_script.md#class_Script) **get_base_script** ( ) *const* [🔗](class_script.md#class_Script_method_get_base_script)

Returns the script directly inherited by this script.

---

<span id="class_Script_method_get_global_name"></span>

[StringName](class_stringname.md#class_StringName) **get_global_name** ( ) *const* [🔗](class_script.md#class_Script_method_get_global_name)

Returns the class name associated with the script, if there is one. Returns an empty string otherwise.

To give the script a global name, you can use the `class_name` keyword in GDScript and the `[GlobalClass]` attribute in C#.

.. tabs::

```
```

    class_name MyNode
    extends Node

```
```

    using Godot;

    [GlobalClass]
    public partial class MyNode : Node
    {
    }

---

<span id="class_Script_method_get_instance_base_type"></span>

[StringName](class_stringname.md#class_StringName) **get_instance_base_type** ( ) *const* [🔗](class_script.md#class_Script_method_get_instance_base_type)

Returns the script's base type.

---

<span id="class_Script_method_get_property_default_value"></span>

[Variant](class_variant.md#class_Variant) **get_property_default_value** ( property: [StringName](class_stringname.md#class_StringName) ) [🔗](class_script.md#class_Script_method_get_property_default_value)

Returns the default value of the specified property.

---

<span id="class_Script_method_get_rpc_config"></span>

[Variant](class_variant.md#class_Variant) **get_rpc_config** ( ) *const* [🔗](class_script.md#class_Script_method_get_rpc_config)

Returns a [Dictionary](class_dictionary.md#class_Dictionary) mapping method names to their RPC configuration defined by this script.

---

<span id="class_Script_method_get_script_constant_map"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_script_constant_map** ( ) [🔗](class_script.md#class_Script_method_get_script_constant_map)

Returns a dictionary containing constant names and their values.

---

<span id="class_Script_method_get_script_method_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_script_method_list** ( ) [🔗](class_script.md#class_Script_method_get_script_method_list)

Returns the list of methods in this **Script**.

 **Note:** The dictionaries returned by this method are formatted identically to those returned by [Object.get_method_list()](class_object.md#class_Object_method_get_method_list).

---

<span id="class_Script_method_get_script_property_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_script_property_list** ( ) [🔗](class_script.md#class_Script_method_get_script_property_list)

Returns the list of properties in this **Script**.

 **Note:** The dictionaries returned by this method are formatted identically to those returned by [Object.get_property_list()](class_object.md#class_Object_method_get_property_list).

---

<span id="class_Script_method_get_script_signal_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_script_signal_list** ( ) [🔗](class_script.md#class_Script_method_get_script_signal_list)

Returns the list of signals defined in this **Script**.

 **Note:** The dictionaries returned by this method are formatted identically to those returned by [Object.get_signal_list()](class_object.md#class_Object_method_get_signal_list).

---

<span id="class_Script_method_has_script_signal"></span>

[bool](class_bool.md#class_bool) **has_script_signal** ( signal_name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_script.md#class_Script_method_has_script_signal)

Returns `true` if the script, or a base class, defines a signal with the given name.

---

<span id="class_Script_method_has_source_code"></span>

[bool](class_bool.md#class_bool) **has_source_code** ( ) *const* [🔗](class_script.md#class_Script_method_has_source_code)

Returns `true` if the script contains non-empty source code.

 **Note:** If a script does not have source code, this does not mean that it is invalid or unusable. For example, a [GDScript](class_gdscript.md#class_GDScript) that was exported with binary tokenization has no source code, but still behaves as expected and could be instantiated. This can be checked with [can_instantiate()](class_script.md#class_Script_method_can_instantiate).

---

<span id="class_Script_method_instance_has"></span>

[bool](class_bool.md#class_bool) **instance_has** ( base_object: [Object](class_object.md#class_Object) ) *const* [🔗](class_script.md#class_Script_method_instance_has)

Returns `true` if `base_object` is an instance of this script.

---

<span id="class_Script_method_is_abstract"></span>

[bool](class_bool.md#class_bool) **is_abstract** ( ) *const* [🔗](class_script.md#class_Script_method_is_abstract)

Returns `true` if the script is an abstract script. An abstract script does not have a constructor and cannot be instantiated.

---

<span id="class_Script_method_is_tool"></span>

[bool](class_bool.md#class_bool) **is_tool** ( ) *const* [🔗](class_script.md#class_Script_method_is_tool)

Returns `true` if the script is a tool script. A tool script can run in the editor.

---

<span id="class_Script_method_reload"></span>

Error **reload** ( keep_state: [bool](class_bool.md#class_bool) = false ) [🔗](class_script.md#class_Script_method_reload)

Reloads the script's class implementation. Returns an error code.
