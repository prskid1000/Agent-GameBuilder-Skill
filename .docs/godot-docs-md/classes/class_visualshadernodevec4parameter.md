<span id="class_VisualShaderNodeVec4Parameter"></span>

## VisualShaderNodeVec4Parameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 4D vector parameter to be used within the visual shader graph.

### Description

Translated to `uniform vec4` in the shader language.

### Properties


| [Vector4](class_vector4.md#class_Vector4) | [default_value](class_visualshadernodevec4parameter.md#class_VisualShaderNodeVec4Parameter_property_default_value) | `Vector4(0, 0, 0, 0)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [default_value_enabled](class_visualshadernodevec4parameter.md#class_VisualShaderNodeVec4Parameter_property_default_value_enabled) | `false` |

---

### Property Descriptions

<span id="class_VisualShaderNodeVec4Parameter_property_default_value"></span>

[Vector4](class_vector4.md#class_Vector4) **default_value** = `Vector4(0, 0, 0, 0)` [🔗](class_visualshadernodevec4parameter.md#class_VisualShaderNodeVec4Parameter_property_default_value)

- void **set_default_value** ( value: [Vector4](class_vector4.md#class_Vector4) )
- [Vector4](class_vector4.md#class_Vector4) **get_default_value** ( )

A default value to be assigned within the shader.

---

<span id="class_VisualShaderNodeVec4Parameter_property_default_value_enabled"></span>

[bool](class_bool.md#class_bool) **default_value_enabled** = `false` [🔗](class_visualshadernodevec4parameter.md#class_VisualShaderNodeVec4Parameter_property_default_value_enabled)

- void **set_default_value_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_default_value_enabled** ( )

Enables usage of the [default_value](class_visualshadernodevec4parameter.md#class_VisualShaderNodeVec4Parameter_property_default_value).
