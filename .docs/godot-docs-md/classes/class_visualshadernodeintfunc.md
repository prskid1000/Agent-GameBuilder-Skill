<span id="class_VisualShaderNodeIntFunc"></span>

## VisualShaderNodeIntFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A scalar integer function to be used within the visual shader graph.

### Description

Accept an integer scalar (`x`) to the input port and transform it according to [function](class_visualshadernodeintfunc.md#class_VisualShaderNodeIntFunc_property_function).

### Properties


| [Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) | [function](class_visualshadernodeintfunc.md#class_VisualShaderNodeIntFunc_property_function) | `2` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeIntFunc_Function"></span>

enum **Function**: [🔗](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function)

<span id="class_VisualShaderNodeIntFunc_constant_FUNC_ABS"></span>

[Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) **FUNC_ABS** = `0`

Returns the absolute value of the parameter. Translates to `abs(x)` in the Godot Shader Language.

<span id="class_VisualShaderNodeIntFunc_constant_FUNC_NEGATE"></span>

[Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) **FUNC_NEGATE** = `1`

Negates the `x` using `-(x)`.

<span id="class_VisualShaderNodeIntFunc_constant_FUNC_SIGN"></span>

[Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) **FUNC_SIGN** = `2`

Extracts the sign of the parameter. Translates to `sign(x)` in the Godot Shader Language.

<span id="class_VisualShaderNodeIntFunc_constant_FUNC_BITWISE_NOT"></span>

[Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) **FUNC_BITWISE_NOT** = `3`

Returns the result of bitwise `NOT` operation on the integer. Translates to `~a` in the Godot Shader Language.

<span id="class_VisualShaderNodeIntFunc_constant_FUNC_MAX"></span>

[Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) **FUNC_MAX** = `4`

Represents the size of the [Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeIntFunc_property_function"></span>

[Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) **function** = `2` [🔗](class_visualshadernodeintfunc.md#class_VisualShaderNodeIntFunc_property_function)

- void **set_function** ( value: [Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) )
- [Function](class_visualshadernodeintfunc.md#enum_VisualShaderNodeIntFunc_Function) **get_function** ( )

A function to be applied to the scalar.
