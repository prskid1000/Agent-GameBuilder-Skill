<span id="class_OpenXRInteractionProfile"></span>

## OpenXRInteractionProfile

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Suggested bindings object for OpenXR.

### Description

This object stores suggested bindings for an interaction profile. Interaction profiles define the metadata for a tracked XR device such as an XR controller.

For more information see the interaction profiles info in the OpenXR specification.

### Properties


| [Array](class_array.md#class_Array) | [binding_modifiers](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_property_binding_modifiers) | `[]` |
| --- | --- | --- |
| [Array](class_array.md#class_Array) | [bindings](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_property_bindings) | `[]` |
| [String](class_string.md#class_String) | [interaction_profile_path](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_property_interaction_profile_path) | `""` |

### Methods


| [OpenXRIPBinding](class_openxripbinding.md#class_OpenXRIPBinding) | [get_binding](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_method_get_binding) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_binding_count](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_method_get_binding_count) ( ) const |
| [OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class_OpenXRIPBindingModifier) | [get_binding_modifier](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_method_get_binding_modifier) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_binding_modifier_count](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_method_get_binding_modifier_count) ( ) const |

---

### Property Descriptions

<span id="class_OpenXRInteractionProfile_property_binding_modifiers"></span>

[Array](class_array.md#class_Array) **binding_modifiers** = `[]` [🔗](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_property_binding_modifiers)

- void **set_binding_modifiers** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_binding_modifiers** ( )

Binding modifiers for this interaction profile.

---

<span id="class_OpenXRInteractionProfile_property_bindings"></span>

[Array](class_array.md#class_Array) **bindings** = `[]` [🔗](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_property_bindings)

- void **set_bindings** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_bindings** ( )

Action bindings for this interaction profile.

---

<span id="class_OpenXRInteractionProfile_property_interaction_profile_path"></span>

[String](class_string.md#class_String) **interaction_profile_path** = `""` [🔗](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_property_interaction_profile_path)

- void **set_interaction_profile_path** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_interaction_profile_path** ( )

The interaction profile path identifying the XR device.

---

### Method Descriptions

<span id="class_OpenXRInteractionProfile_method_get_binding"></span>

[OpenXRIPBinding](class_openxripbinding.md#class_OpenXRIPBinding) **get_binding** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_method_get_binding)

Retrieve the binding at this index.

---

<span id="class_OpenXRInteractionProfile_method_get_binding_count"></span>

[int](class_int.md#class_int) **get_binding_count** ( ) *const* [🔗](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_method_get_binding_count)

Get the number of bindings in this interaction profile.

---

<span id="class_OpenXRInteractionProfile_method_get_binding_modifier"></span>

[OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class_OpenXRIPBindingModifier) **get_binding_modifier** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_method_get_binding_modifier)

Get the [OpenXRBindingModifier](class_openxrbindingmodifier.md#class_OpenXRBindingModifier) at this index.

---

<span id="class_OpenXRInteractionProfile_method_get_binding_modifier_count"></span>

[int](class_int.md#class_int) **get_binding_modifier_count** ( ) *const* [🔗](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile_method_get_binding_modifier_count)

Get the number of binding modifiers in this interaction profile.
