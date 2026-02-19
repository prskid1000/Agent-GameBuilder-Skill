<span id="class_VisualShaderNodeFloatOp"></span>

## VisualShaderNodeFloatOp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A floating-point scalar operator to be used within the visual shader graph.

### Description

Applies [operator](class_visualshadernodefloatop.md#class_VisualShaderNodeFloatOp_property_operator) to two floating-point inputs: `a` and `b`.

### Properties


| [Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) | [operator](class_visualshadernodefloatop.md#class_VisualShaderNodeFloatOp_property_operator) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeFloatOp_Operator"></span>

enum **Operator**: [🔗](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator)

<span id="class_VisualShaderNodeFloatOp_constant_OP_ADD"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_ADD** = `0`

Sums two numbers using `a + b`.

<span id="class_VisualShaderNodeFloatOp_constant_OP_SUB"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_SUB** = `1`

Subtracts two numbers using `a - b`.

<span id="class_VisualShaderNodeFloatOp_constant_OP_MUL"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_MUL** = `2`

Multiplies two numbers using `a * b`.

<span id="class_VisualShaderNodeFloatOp_constant_OP_DIV"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_DIV** = `3`

Divides two numbers using `a / b`.

<span id="class_VisualShaderNodeFloatOp_constant_OP_MOD"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_MOD** = `4`

Calculates the remainder of two numbers. Translates to `mod(a, b)` in the Godot Shader Language.

<span id="class_VisualShaderNodeFloatOp_constant_OP_POW"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_POW** = `5`

Raises the `a` to the power of `b`. Translates to `pow(a, b)` in the Godot Shader Language.

<span id="class_VisualShaderNodeFloatOp_constant_OP_MAX"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_MAX** = `6`

Returns the greater of two numbers. Translates to `max(a, b)` in the Godot Shader Language.

<span id="class_VisualShaderNodeFloatOp_constant_OP_MIN"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_MIN** = `7`

Returns the lesser of two numbers. Translates to `min(a, b)` in the Godot Shader Language.

<span id="class_VisualShaderNodeFloatOp_constant_OP_ATAN2"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_ATAN2** = `8`

Returns the arc-tangent of the parameters. Translates to `atan(a, b)` in the Godot Shader Language.

<span id="class_VisualShaderNodeFloatOp_constant_OP_STEP"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_STEP** = `9`

Generates a step function by comparing `b` (x) to `a` (edge). Returns 0.0 if `x` is smaller than `edge` and otherwise 1.0. Translates to `step(a, b)` in the Godot Shader Language.

<span id="class_VisualShaderNodeFloatOp_constant_OP_ENUM_SIZE"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **OP_ENUM_SIZE** = `10`

Represents the size of the [Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeFloatOp_property_operator"></span>

[Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **operator** = `0` [🔗](class_visualshadernodefloatop.md#class_VisualShaderNodeFloatOp_property_operator)

- void **set_operator** ( value: [Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) )
- [Operator](class_visualshadernodefloatop.md#enum_VisualShaderNodeFloatOp_Operator) **get_operator** ( )

An operator to be applied to the inputs.
