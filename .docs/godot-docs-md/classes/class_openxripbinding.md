<span id="class_OpenXRIPBinding"></span>

## OpenXRIPBinding

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Defines a binding between an [OpenXRAction](class_openxraction.md#class_OpenXRAction) and an XR input or output.

### Description

This binding resource binds an [OpenXRAction](class_openxraction.md#class_OpenXRAction) to an input or output. As most controllers have left hand and right versions that are handled by the same interaction profile we can specify multiple bindings. For instance an action "Fire" could be bound to both "/user/hand/left/input/trigger" and "/user/hand/right/input/trigger". This would require two binding entries.

### Properties


| [OpenXRAction](class_openxraction.md#class_OpenXRAction) | [action](class_openxripbinding.md#class_OpenXRIPBinding_property_action) |
| --- | --- |
| [Array](class_array.md#class_Array) | [binding_modifiers](class_openxripbinding.md#class_OpenXRIPBinding_property_binding_modifiers) | `[]` |
| [String](class_string.md#class_String) | [binding_path](class_openxripbinding.md#class_OpenXRIPBinding_property_binding_path) | `""` |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [paths](class_openxripbinding.md#class_OpenXRIPBinding_property_paths) |

### Methods


| void | [add_path](class_openxripbinding.md#class_OpenXRIPBinding_method_add_path) ( path: [String](class_string.md#class_String) ) |
| --- | --- |
| [OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class_OpenXRActionBindingModifier) | [get_binding_modifier](class_openxripbinding.md#class_OpenXRIPBinding_method_get_binding_modifier) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_binding_modifier_count](class_openxripbinding.md#class_OpenXRIPBinding_method_get_binding_modifier_count) ( ) const |
| [int](class_int.md#class_int) | [get_path_count](class_openxripbinding.md#class_OpenXRIPBinding_method_get_path_count) ( ) const |
| [bool](class_bool.md#class_bool) | [has_path](class_openxripbinding.md#class_OpenXRIPBinding_method_has_path) ( path: [String](class_string.md#class_String) ) const |
| void | [remove_path](class_openxripbinding.md#class_OpenXRIPBinding_method_remove_path) ( path: [String](class_string.md#class_String) ) |

---

### Property Descriptions

<span id="class_OpenXRIPBinding_property_action"></span>

[OpenXRAction](class_openxraction.md#class_OpenXRAction) **action** [🔗](class_openxripbinding.md#class_OpenXRIPBinding_property_action)

- void **set_action** ( value: [OpenXRAction](class_openxraction.md#class_OpenXRAction) )
- [OpenXRAction](class_openxraction.md#class_OpenXRAction) **get_action** ( )

[OpenXRAction](class_openxraction.md#class_OpenXRAction) that is bound to [binding_path](class_openxripbinding.md#class_OpenXRIPBinding_property_binding_path).

---

<span id="class_OpenXRIPBinding_property_binding_modifiers"></span>

[Array](class_array.md#class_Array) **binding_modifiers** = `[]` [🔗](class_openxripbinding.md#class_OpenXRIPBinding_property_binding_modifiers)

- void **set_binding_modifiers** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_binding_modifiers** ( )

Binding modifiers for this binding.

---

<span id="class_OpenXRIPBinding_property_binding_path"></span>

[String](class_string.md#class_String) **binding_path** = `""` [🔗](class_openxripbinding.md#class_OpenXRIPBinding_property_binding_path)

- void **set_binding_path** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_binding_path** ( )

Binding path that defines the input or output bound to [action](class_openxripbinding.md#class_OpenXRIPBinding_property_action).

 **Note:** Binding paths are suggestions, an XR runtime may choose to bind the action to a different input or output emulating this input or output.

---

<span id="class_OpenXRIPBinding_property_paths"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **paths** [🔗](class_openxripbinding.md#class_OpenXRIPBinding_property_paths)

- void **set_paths** ( value: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )
- [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_paths** ( )

**Deprecated:** Use [binding_path](class_openxripbinding.md#class_OpenXRIPBinding_property_binding_path) instead.

Paths that define the inputs or outputs bound on the device.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

### Method Descriptions

<span id="class_OpenXRIPBinding_method_add_path"></span>

void **add_path** ( path: [String](class_string.md#class_String) ) [🔗](class_openxripbinding.md#class_OpenXRIPBinding_method_add_path)

**Deprecated:** Binding is for a single path.

Add an input/output path to this binding.

---

<span id="class_OpenXRIPBinding_method_get_binding_modifier"></span>

[OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class_OpenXRActionBindingModifier) **get_binding_modifier** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxripbinding.md#class_OpenXRIPBinding_method_get_binding_modifier)

Get the [OpenXRBindingModifier](class_openxrbindingmodifier.md#class_OpenXRBindingModifier) at this index.

---

<span id="class_OpenXRIPBinding_method_get_binding_modifier_count"></span>

[int](class_int.md#class_int) **get_binding_modifier_count** ( ) *const* [🔗](class_openxripbinding.md#class_OpenXRIPBinding_method_get_binding_modifier_count)

Get the number of binding modifiers for this binding.

---

<span id="class_OpenXRIPBinding_method_get_path_count"></span>

[int](class_int.md#class_int) **get_path_count** ( ) *const* [🔗](class_openxripbinding.md#class_OpenXRIPBinding_method_get_path_count)

**Deprecated:** Binding is for a single path.

Get the number of input/output paths in this binding.

---

<span id="class_OpenXRIPBinding_method_has_path"></span>

[bool](class_bool.md#class_bool) **has_path** ( path: [String](class_string.md#class_String) ) *const* [🔗](class_openxripbinding.md#class_OpenXRIPBinding_method_has_path)

**Deprecated:** Binding is for a single path.

Returns `true` if this input/output path is part of this binding.

---

<span id="class_OpenXRIPBinding_method_remove_path"></span>

void **remove_path** ( path: [String](class_string.md#class_String) ) [🔗](class_openxripbinding.md#class_OpenXRIPBinding_method_remove_path)

**Deprecated:** Binding is for a single path.

Removes this input/output path from this binding.
