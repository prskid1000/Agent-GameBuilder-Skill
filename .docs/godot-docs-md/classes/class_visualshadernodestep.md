<span id="class_VisualShaderNodeStep"></span>

## VisualShaderNodeStep

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Calculates a Step function within the visual shader graph.

### Description

Translates to `step(edge, x)` in the shader language.

Returns `0.0` if `x` is smaller than `edge` and `1.0` otherwise.

### Properties


| [OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) | [op_type](class_visualshadernodestep.md#class_VisualShaderNodeStep_property_op_type) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeStep_OpType"></span>

enum **OpType**: [🔗](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType)

<span id="class_VisualShaderNodeStep_constant_OP_TYPE_SCALAR"></span>

[OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

<span id="class_VisualShaderNodeStep_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<span id="class_VisualShaderNodeStep_constant_OP_TYPE_VECTOR_2D_SCALAR"></span>

[OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `x` port uses a 2D vector type, while the `edge` port uses a floating-point scalar type.

<span id="class_VisualShaderNodeStep_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

<span id="class_VisualShaderNodeStep_constant_OP_TYPE_VECTOR_3D_SCALAR"></span>

[OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `x` port uses a 3D vector type, while the `edge` port uses a floating-point scalar type.

<span id="class_VisualShaderNodeStep_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<span id="class_VisualShaderNodeStep_constant_OP_TYPE_VECTOR_4D_SCALAR"></span>

[OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `a` and `b` ports use a 4D vector type. The `weight` port uses a scalar type.

<span id="class_VisualShaderNodeStep_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **OP_TYPE_MAX** = `7`

Represents the size of the [OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeStep_property_op_type"></span>

[OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **op_type** = `0` [🔗](class_visualshadernodestep.md#class_VisualShaderNodeStep_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) )
- [OpType](class_visualshadernodestep.md#enum_VisualShaderNodeStep_OpType) **get_op_type** ( )

A type of operands and returned value.
