<span id="class_VisualShaderNodeVarying"></span>

## VisualShaderNodeVarying

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeVaryingGetter](class_visualshadernodevaryinggetter.md#class_VisualShaderNodeVaryingGetter), [VisualShaderNodeVaryingSetter](class_visualshadernodevaryingsetter.md#class_VisualShaderNodeVaryingSetter)

A visual shader node that represents a "varying" shader value.

### Description

Varying values are shader variables that can be passed between shader functions, e.g. from Vertex shader to Fragment shader.

### Properties


| [String](class_string.md#class_String) | [varying_name](class_visualshadernodevarying.md#class_VisualShaderNodeVarying_property_varying_name) | `"[None]"` |
| --- | --- | --- |
| [VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) | [varying_type](class_visualshadernodevarying.md#class_VisualShaderNodeVarying_property_varying_type) | `0` |

---

### Property Descriptions

<span id="class_VisualShaderNodeVarying_property_varying_name"></span>

[String](class_string.md#class_String) **varying_name** = `"[None]"` [🔗](class_visualshadernodevarying.md#class_VisualShaderNodeVarying_property_varying_name)

- void **set_varying_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_varying_name** ( )

Name of the variable. Must be unique.

---

<span id="class_VisualShaderNodeVarying_property_varying_type"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **varying_type** = `0` [🔗](class_visualshadernodevarying.md#class_VisualShaderNodeVarying_property_varying_type)

- void **set_varying_type** ( value: [VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) )
- [VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **get_varying_type** ( )

Type of the variable. Determines where the variable can be accessed.
