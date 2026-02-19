<span id="class_VisualShaderNodeVec3Parameter"></span>

## VisualShaderNodeVec3Parameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Vector3](class_vector3.md#class_Vector3) parameter to be used within the visual shader graph.

### Description

Translated to `uniform vec3` in the shader language.

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [default_value](class_visualshadernodevec3parameter.md#class_VisualShaderNodeVec3Parameter_property_default_value) | `Vector3(0, 0, 0)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [default_value_enabled](class_visualshadernodevec3parameter.md#class_VisualShaderNodeVec3Parameter_property_default_value_enabled) | `false` |

---

### Property Descriptions

<span id="class_VisualShaderNodeVec3Parameter_property_default_value"></span>

[Vector3](class_vector3.md#class_Vector3) **default_value** = `Vector3(0, 0, 0)` [🔗](class_visualshadernodevec3parameter.md#class_VisualShaderNodeVec3Parameter_property_default_value)

- void **set_default_value** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_default_value** ( )

A default value to be assigned within the shader.

---

<span id="class_VisualShaderNodeVec3Parameter_property_default_value_enabled"></span>

[bool](class_bool.md#class_bool) **default_value_enabled** = `false` [🔗](class_visualshadernodevec3parameter.md#class_VisualShaderNodeVec3Parameter_property_default_value_enabled)

- void **set_default_value_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_default_value_enabled** ( )

Enables usage of the [default_value](class_visualshadernodevec3parameter.md#class_VisualShaderNodeVec3Parameter_property_default_value).
