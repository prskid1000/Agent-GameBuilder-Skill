<span id="class_VisualShaderNodeIs"></span>

## VisualShaderNodeIs

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A boolean comparison operator to be used within the visual shader graph.

### Description

Returns the boolean result of the comparison between `INF` or `NaN` and a scalar parameter.

### Properties


| [Function](class_visualshadernodeis.md#enum_VisualShaderNodeIs_Function) | [function](class_visualshadernodeis.md#class_VisualShaderNodeIs_property_function) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeIs_Function"></span>

enum **Function**: [🔗](class_visualshadernodeis.md#enum_VisualShaderNodeIs_Function)

<span id="class_VisualShaderNodeIs_constant_FUNC_IS_INF"></span>

[Function](class_visualshadernodeis.md#enum_VisualShaderNodeIs_Function) **FUNC_IS_INF** = `0`

Comparison with `INF` (Infinity).

<span id="class_VisualShaderNodeIs_constant_FUNC_IS_NAN"></span>

[Function](class_visualshadernodeis.md#enum_VisualShaderNodeIs_Function) **FUNC_IS_NAN** = `1`

Comparison with `NaN` (Not a Number; indicates invalid numeric results, such as division by zero).

<span id="class_VisualShaderNodeIs_constant_FUNC_MAX"></span>

[Function](class_visualshadernodeis.md#enum_VisualShaderNodeIs_Function) **FUNC_MAX** = `2`

Represents the size of the [Function](class_visualshadernodeis.md#enum_VisualShaderNodeIs_Function) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeIs_property_function"></span>

[Function](class_visualshadernodeis.md#enum_VisualShaderNodeIs_Function) **function** = `0` [🔗](class_visualshadernodeis.md#class_VisualShaderNodeIs_property_function)

- void **set_function** ( value: [Function](class_visualshadernodeis.md#enum_VisualShaderNodeIs_Function) )
- [Function](class_visualshadernodeis.md#enum_VisualShaderNodeIs_Function) **get_function** ( )

The comparison function.
