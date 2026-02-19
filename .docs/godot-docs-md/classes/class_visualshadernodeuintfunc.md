<span id="class_VisualShaderNodeUIntFunc"></span>

## VisualShaderNodeUIntFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An unsigned scalar integer function to be used within the visual shader graph.

### Description

Accept an unsigned integer scalar (`x`) to the input port and transform it according to [function](class_visualshadernodeuintfunc.md#class_VisualShaderNodeUIntFunc_property_function).

### Properties


| [Function](class_visualshadernodeuintfunc.md#enum_VisualShaderNodeUIntFunc_Function) | [function](class_visualshadernodeuintfunc.md#class_VisualShaderNodeUIntFunc_property_function) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeUIntFunc_Function"></span>

enum **Function**: [🔗](class_visualshadernodeuintfunc.md#enum_VisualShaderNodeUIntFunc_Function)

<span id="class_VisualShaderNodeUIntFunc_constant_FUNC_NEGATE"></span>

[Function](class_visualshadernodeuintfunc.md#enum_VisualShaderNodeUIntFunc_Function) **FUNC_NEGATE** = `0`

Negates the `x` using `-(x)`.

<span id="class_VisualShaderNodeUIntFunc_constant_FUNC_BITWISE_NOT"></span>

[Function](class_visualshadernodeuintfunc.md#enum_VisualShaderNodeUIntFunc_Function) **FUNC_BITWISE_NOT** = `1`

Returns the result of bitwise `NOT` operation on the integer. Translates to `~a` in the Godot Shader Language.

<span id="class_VisualShaderNodeUIntFunc_constant_FUNC_MAX"></span>

[Function](class_visualshadernodeuintfunc.md#enum_VisualShaderNodeUIntFunc_Function) **FUNC_MAX** = `2`

Represents the size of the [Function](class_visualshadernodeuintfunc.md#enum_VisualShaderNodeUIntFunc_Function) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeUIntFunc_property_function"></span>

[Function](class_visualshadernodeuintfunc.md#enum_VisualShaderNodeUIntFunc_Function) **function** = `0` [🔗](class_visualshadernodeuintfunc.md#class_VisualShaderNodeUIntFunc_property_function)

- void **set_function** ( value: [Function](class_visualshadernodeuintfunc.md#enum_VisualShaderNodeUIntFunc_Function) )
- [Function](class_visualshadernodeuintfunc.md#enum_VisualShaderNodeUIntFunc_Function) **get_function** ( )

A function to be applied to the scalar.
