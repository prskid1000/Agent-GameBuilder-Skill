<span id="class_VisualShaderNodeColorParameter"></span>

## VisualShaderNodeColorParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Color](class_color.md#class_Color) parameter to be used within the visual shader graph.

### Description

Translated to `uniform vec4` in the shader language.

### Properties


| [Color](class_color.md#class_Color) | [default_value](class_visualshadernodecolorparameter.md#class_VisualShaderNodeColorParameter_property_default_value) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [default_value_enabled](class_visualshadernodecolorparameter.md#class_VisualShaderNodeColorParameter_property_default_value_enabled) | `false` |

---

### Property Descriptions

<span id="class_VisualShaderNodeColorParameter_property_default_value"></span>

[Color](class_color.md#class_Color) **default_value** = `Color(1, 1, 1, 1)` [🔗](class_visualshadernodecolorparameter.md#class_VisualShaderNodeColorParameter_property_default_value)

- void **set_default_value** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_default_value** ( )

A default value to be assigned within the shader.

---

<span id="class_VisualShaderNodeColorParameter_property_default_value_enabled"></span>

[bool](class_bool.md#class_bool) **default_value_enabled** = `false` [🔗](class_visualshadernodecolorparameter.md#class_VisualShaderNodeColorParameter_property_default_value_enabled)

- void **set_default_value_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_default_value_enabled** ( )

Enables usage of the [default_value](class_visualshadernodecolorparameter.md#class_VisualShaderNodeColorParameter_property_default_value).
