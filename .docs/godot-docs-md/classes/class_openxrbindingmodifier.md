<span id="class_OpenXRBindingModifier"></span>

## OpenXRBindingModifier

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class_OpenXRActionBindingModifier), [OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class_OpenXRIPBindingModifier)

Binding modifier base class.

### Description

Binding modifier base class. Subclasses implement various modifiers that alter how an OpenXR runtime processes inputs.

### Methods


| [String](class_string.md#class_String) | [_get_description](class_openxrbindingmodifier.md#class_OpenXRBindingModifier_private_method__get_description) ( ) | virtual | required | const |
| --- | --- | --- | --- | --- |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [_get_ip_modification](class_openxrbindingmodifier.md#class_OpenXRBindingModifier_private_method__get_ip_modification) ( ) | virtual | required |

---

### Method Descriptions

<span id="class_OpenXRBindingModifier_private_method__get_description"></span>

[String](class_string.md#class_String) **_get_description** ( ) *virtual* |required| *const* [🔗](class_openxrbindingmodifier.md#class_OpenXRBindingModifier_private_method__get_description)

Return the description of this class that is used for the title bar of the binding modifier editor.

---

<span id="class_OpenXRBindingModifier_private_method__get_ip_modification"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **_get_ip_modification** ( ) *virtual* |required| [🔗](class_openxrbindingmodifier.md#class_OpenXRBindingModifier_private_method__get_ip_modification)

Returns the data that is sent to OpenXR when submitting the suggested interacting bindings this modifier is a part of.

 **Note:** This must be data compatible with an `XrBindingModificationBaseHeaderKHR` structure.
