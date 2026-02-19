<span id="class_VisualShaderNodeDerivativeFunc"></span>

## VisualShaderNodeDerivativeFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Calculates a derivative within the visual shader graph.

### Description

This node is only available in `Fragment` and `Light` visual shaders.

### Properties


| [Function](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function) | [function](class_visualshadernodederivativefunc.md#class_VisualShaderNodeDerivativeFunc_property_function) | `0` |
| --- | --- | --- |
| [OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) | [op_type](class_visualshadernodederivativefunc.md#class_VisualShaderNodeDerivativeFunc_property_op_type) | `0` |
| [Precision](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision) | [precision](class_visualshadernodederivativefunc.md#class_VisualShaderNodeDerivativeFunc_property_precision) | `0` |

---

### Enumerations

<span id="enum_VisualShaderNodeDerivativeFunc_OpType"></span>

enum **OpType**: [🔗](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType)

<span id="class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_SCALAR"></span>

[OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

<span id="class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<span id="class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

<span id="class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

<span id="class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) **OP_TYPE_MAX** = `4`

Represents the size of the [OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) enum.

---

<span id="enum_VisualShaderNodeDerivativeFunc_Function"></span>

enum **Function**: [🔗](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function)

<span id="class_VisualShaderNodeDerivativeFunc_constant_FUNC_SUM"></span>

[Function](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function) **FUNC_SUM** = `0`

Sum of absolute derivative in `x` and `y`.

<span id="class_VisualShaderNodeDerivativeFunc_constant_FUNC_X"></span>

[Function](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function) **FUNC_X** = `1`

Derivative in `x` using local differencing.

<span id="class_VisualShaderNodeDerivativeFunc_constant_FUNC_Y"></span>

[Function](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function) **FUNC_Y** = `2`

Derivative in `y` using local differencing.

<span id="class_VisualShaderNodeDerivativeFunc_constant_FUNC_MAX"></span>

[Function](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function) **FUNC_MAX** = `3`

Represents the size of the [Function](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function) enum.

---

<span id="enum_VisualShaderNodeDerivativeFunc_Precision"></span>

enum **Precision**: [🔗](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision)

<span id="class_VisualShaderNodeDerivativeFunc_constant_PRECISION_NONE"></span>

[Precision](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision) **PRECISION_NONE** = `0`

No precision is specified, the GPU driver is allowed to use whatever level of precision it chooses. This is the default option and is equivalent to using `dFdx()` or `dFdy()` in text shaders.

<span id="class_VisualShaderNodeDerivativeFunc_constant_PRECISION_COARSE"></span>

[Precision](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision) **PRECISION_COARSE** = `1`

The derivative will be calculated using the current fragment's neighbors (which may not include the current fragment). This tends to be faster than using [PRECISION_FINE](class_visualshadernodederivativefunc.md#class_VisualShaderNodeDerivativeFunc_constant_PRECISION_FINE), but may not be suitable when more precision is needed. This is equivalent to using `dFdxCoarse()` or `dFdyCoarse()` in text shaders.

<span id="class_VisualShaderNodeDerivativeFunc_constant_PRECISION_FINE"></span>

[Precision](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision) **PRECISION_FINE** = `2`

The derivative will be calculated using the current fragment and its immediate neighbors. This tends to be slower than using [PRECISION_COARSE](class_visualshadernodederivativefunc.md#class_VisualShaderNodeDerivativeFunc_constant_PRECISION_COARSE), but may be necessary when more precision is needed. This is equivalent to using `dFdxFine()` or `dFdyFine()` in text shaders.

<span id="class_VisualShaderNodeDerivativeFunc_constant_PRECISION_MAX"></span>

[Precision](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision) **PRECISION_MAX** = `3`

Represents the size of the [Precision](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeDerivativeFunc_property_function"></span>

[Function](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function) **function** = `0` [🔗](class_visualshadernodederivativefunc.md#class_VisualShaderNodeDerivativeFunc_property_function)

- void **set_function** ( value: [Function](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function) )
- [Function](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Function) **get_function** ( )

A derivative function type.

---

<span id="class_VisualShaderNodeDerivativeFunc_property_op_type"></span>

[OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) **op_type** = `0` [🔗](class_visualshadernodederivativefunc.md#class_VisualShaderNodeDerivativeFunc_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) )
- [OpType](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_OpType) **get_op_type** ( )

A type of operands and returned value.

---

<span id="class_VisualShaderNodeDerivativeFunc_property_precision"></span>

[Precision](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision) **precision** = `0` [🔗](class_visualshadernodederivativefunc.md#class_VisualShaderNodeDerivativeFunc_property_precision)

- void **set_precision** ( value: [Precision](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision) )
- [Precision](class_visualshadernodederivativefunc.md#enum_VisualShaderNodeDerivativeFunc_Precision) **get_precision** ( )

Sets the level of precision to use for the derivative function. When using the Compatibility renderer, this setting has no effect.
