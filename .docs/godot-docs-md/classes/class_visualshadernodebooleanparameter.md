<span id="class_VisualShaderNodeBooleanParameter"></span>

## VisualShaderNodeBooleanParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A boolean parameter to be used within the visual shader graph.

### Description

Translated to `uniform bool` in the shader language.

### Properties


| [bool](class_bool.md#class_bool) | [default_value](class_visualshadernodebooleanparameter.md#class_VisualShaderNodeBooleanParameter_property_default_value) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [default_value_enabled](class_visualshadernodebooleanparameter.md#class_VisualShaderNodeBooleanParameter_property_default_value_enabled) | `false` |

---

### Property Descriptions

<span id="class_VisualShaderNodeBooleanParameter_property_default_value"></span>

[bool](class_bool.md#class_bool) **default_value** = `false` [🔗](class_visualshadernodebooleanparameter.md#class_VisualShaderNodeBooleanParameter_property_default_value)

- void **set_default_value** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_default_value** ( )

A default value to be assigned within the shader.

---

<span id="class_VisualShaderNodeBooleanParameter_property_default_value_enabled"></span>

[bool](class_bool.md#class_bool) **default_value_enabled** = `false` [🔗](class_visualshadernodebooleanparameter.md#class_VisualShaderNodeBooleanParameter_property_default_value_enabled)

- void **set_default_value_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_default_value_enabled** ( )

Enables usage of the [default_value](class_visualshadernodebooleanparameter.md#class_VisualShaderNodeBooleanParameter_property_default_value).
