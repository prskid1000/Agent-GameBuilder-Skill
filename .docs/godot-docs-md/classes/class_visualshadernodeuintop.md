<span id="class_VisualShaderNodeUIntOp"></span>

## VisualShaderNodeUIntOp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An unsigned integer scalar operator to be used within the visual shader graph.

### Description

Applies [operator](class_visualshadernodeuintop.md#class_VisualShaderNodeUIntOp_property_operator) to two unsigned integer inputs: `a` and `b`.

### Properties


| [Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) | [operator](class_visualshadernodeuintop.md#class_VisualShaderNodeUIntOp_property_operator) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeUIntOp_Operator"></span>

enum **Operator**: [🔗](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator)

<span id="class_VisualShaderNodeUIntOp_constant_OP_ADD"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_ADD** = `0`

Sums two numbers using `a + b`.

<span id="class_VisualShaderNodeUIntOp_constant_OP_SUB"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_SUB** = `1`

Subtracts two numbers using `a - b`.

<span id="class_VisualShaderNodeUIntOp_constant_OP_MUL"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_MUL** = `2`

Multiplies two numbers using `a * b`.

<span id="class_VisualShaderNodeUIntOp_constant_OP_DIV"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_DIV** = `3`

Divides two numbers using `a / b`.

<span id="class_VisualShaderNodeUIntOp_constant_OP_MOD"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_MOD** = `4`

Calculates the remainder of two numbers using `a % b`.

<span id="class_VisualShaderNodeUIntOp_constant_OP_MAX"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_MAX** = `5`

Returns the greater of two numbers. Translates to `max(a, b)` in the Godot Shader Language.

<span id="class_VisualShaderNodeUIntOp_constant_OP_MIN"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_MIN** = `6`

Returns the lesser of two numbers. Translates to `max(a, b)` in the Godot Shader Language.

<span id="class_VisualShaderNodeUIntOp_constant_OP_BITWISE_AND"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_BITWISE_AND** = `7`

Returns the result of bitwise `AND` operation on the integer. Translates to `a & b` in the Godot Shader Language.

<span id="class_VisualShaderNodeUIntOp_constant_OP_BITWISE_OR"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_BITWISE_OR** = `8`

Returns the result of bitwise `OR` operation for two integers. Translates to `a | b` in the Godot Shader Language.

<span id="class_VisualShaderNodeUIntOp_constant_OP_BITWISE_XOR"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_BITWISE_XOR** = `9`

Returns the result of bitwise `XOR` operation for two integers. Translates to `a ^ b` in the Godot Shader Language.

<span id="class_VisualShaderNodeUIntOp_constant_OP_BITWISE_LEFT_SHIFT"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_BITWISE_LEFT_SHIFT** = `10`

Returns the result of bitwise left shift operation on the integer. Translates to `a << b` in the Godot Shader Language.

<span id="class_VisualShaderNodeUIntOp_constant_OP_BITWISE_RIGHT_SHIFT"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_BITWISE_RIGHT_SHIFT** = `11`

Returns the result of bitwise right shift operation on the integer. Translates to `a >> b` in the Godot Shader Language.

<span id="class_VisualShaderNodeUIntOp_constant_OP_ENUM_SIZE"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **OP_ENUM_SIZE** = `12`

Represents the size of the [Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeUIntOp_property_operator"></span>

[Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **operator** = `0` [🔗](class_visualshadernodeuintop.md#class_VisualShaderNodeUIntOp_property_operator)

- void **set_operator** ( value: [Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) )
- [Operator](class_visualshadernodeuintop.md#enum_VisualShaderNodeUIntOp_Operator) **get_operator** ( )

An operator to be applied to the inputs.
