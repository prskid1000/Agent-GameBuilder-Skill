<span id="class_VisualShaderNodeParameterRef"></span>

## VisualShaderNodeParameterRef

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A reference to an existing [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter).

### Description

Creating a reference to a [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) allows you to reuse this parameter in different shaders or shader stages easily.

### Properties


| [String](class_string.md#class_String) | [parameter_name](class_visualshadernodeparameterref.md#class_VisualShaderNodeParameterRef_property_parameter_name) | `"[None]"` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_VisualShaderNodeParameterRef_property_parameter_name"></span>

[String](class_string.md#class_String) **parameter_name** = `"[None]"` [🔗](class_visualshadernodeparameterref.md#class_VisualShaderNodeParameterRef_property_parameter_name)

- void **set_parameter_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_parameter_name** ( )

The name of the parameter which this reference points to.
