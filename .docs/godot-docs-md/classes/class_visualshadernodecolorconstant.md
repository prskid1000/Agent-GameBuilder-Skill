<span id="class_VisualShaderNodeColorConstant"></span>

## VisualShaderNodeColorConstant

**Inherits:** [VisualShaderNodeConstant](class_visualshadernodeconstant.md#class_VisualShaderNodeConstant) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Color](class_color.md#class_Color) constant to be used within the visual shader graph.

### Description

Has two output ports representing RGB and alpha channels of [Color](class_color.md#class_Color).

Translated to `vec3 rgb` and `float alpha` in the shader language.

### Properties


| [Color](class_color.md#class_Color) | [constant](class_visualshadernodecolorconstant.md#class_VisualShaderNodeColorConstant_property_constant) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_VisualShaderNodeColorConstant_property_constant"></span>

[Color](class_color.md#class_Color) **constant** = `Color(1, 1, 1, 1)` [🔗](class_visualshadernodecolorconstant.md#class_VisualShaderNodeColorConstant_property_constant)

- void **set_constant** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_constant** ( )

A [Color](class_color.md#class_Color) constant which represents a state of this node.
