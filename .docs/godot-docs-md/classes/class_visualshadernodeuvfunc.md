<span id="class_VisualShaderNodeUVFunc"></span>

## VisualShaderNodeUVFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Contains functions to modify texture coordinates (`uv`) to be used within the visual shader graph.

### Description

UV functions are similar to [Vector2](class_vector2.md#class_Vector2) functions, but the input port of this node uses the shader's UV value by default.

### Properties


| [Function](class_visualshadernodeuvfunc.md#enum_VisualShaderNodeUVFunc_Function) | [function](class_visualshadernodeuvfunc.md#class_VisualShaderNodeUVFunc_property_function) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeUVFunc_Function"></span>

enum **Function**: [🔗](class_visualshadernodeuvfunc.md#enum_VisualShaderNodeUVFunc_Function)

<span id="class_VisualShaderNodeUVFunc_constant_FUNC_PANNING"></span>

[Function](class_visualshadernodeuvfunc.md#enum_VisualShaderNodeUVFunc_Function) **FUNC_PANNING** = `0`

Translates `uv` by using `scale` and `offset` values using the following formula: `uv = uv + offset * scale`. `uv` port is connected to `UV` built-in by default.

<span id="class_VisualShaderNodeUVFunc_constant_FUNC_SCALING"></span>

[Function](class_visualshadernodeuvfunc.md#enum_VisualShaderNodeUVFunc_Function) **FUNC_SCALING** = `1`

Scales `uv` by using `scale` and `pivot` values using the following formula: `uv = (uv - pivot) * scale + pivot`. `uv` port is connected to `UV` built-in by default.

<span id="class_VisualShaderNodeUVFunc_constant_FUNC_MAX"></span>

[Function](class_visualshadernodeuvfunc.md#enum_VisualShaderNodeUVFunc_Function) **FUNC_MAX** = `2`

Represents the size of the [Function](class_visualshadernodeuvfunc.md#enum_VisualShaderNodeUVFunc_Function) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeUVFunc_property_function"></span>

[Function](class_visualshadernodeuvfunc.md#enum_VisualShaderNodeUVFunc_Function) **function** = `0` [🔗](class_visualshadernodeuvfunc.md#class_VisualShaderNodeUVFunc_property_function)

- void **set_function** ( value: [Function](class_visualshadernodeuvfunc.md#enum_VisualShaderNodeUVFunc_Function) )
- [Function](class_visualshadernodeuvfunc.md#enum_VisualShaderNodeUVFunc_Function) **get_function** ( )

A function to be applied to the texture coordinates.
