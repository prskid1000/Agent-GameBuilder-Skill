<span id="class_VisualShaderNodeSmoothStep"></span>

## VisualShaderNodeSmoothStep

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Calculates a SmoothStep function within the visual shader graph.

### Description

Translates to `smoothstep(edge0, edge1, x)` in the shader language.

Returns `0.0` if `x` is smaller than `edge0` and `1.0` if `x` is larger than `edge1`. Otherwise, the return value is interpolated between `0.0` and `1.0` using Hermite polynomials.

### Properties


| [OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) | [op_type](class_visualshadernodesmoothstep.md#class_VisualShaderNodeSmoothStep_property_op_type) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeSmoothStep_OpType"></span>

enum **OpType**: [🔗](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType)

<span id="class_VisualShaderNodeSmoothStep_constant_OP_TYPE_SCALAR"></span>

[OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

<span id="class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<span id="class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_2D_SCALAR"></span>

[OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `x` port uses a 2D vector type. The first two ports use a floating-point scalar type.

<span id="class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

<span id="class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_3D_SCALAR"></span>

[OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `x` port uses a 3D vector type. The first two ports use a floating-point scalar type.

<span id="class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<span id="class_VisualShaderNodeSmoothStep_constant_OP_TYPE_VECTOR_4D_SCALAR"></span>

[OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `a` and `b` ports use a 4D vector type. The `weight` port uses a scalar type.

<span id="class_VisualShaderNodeSmoothStep_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **OP_TYPE_MAX** = `7`

Represents the size of the [OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeSmoothStep_property_op_type"></span>

[OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **op_type** = `0` [🔗](class_visualshadernodesmoothstep.md#class_VisualShaderNodeSmoothStep_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) )
- [OpType](class_visualshadernodesmoothstep.md#enum_VisualShaderNodeSmoothStep_OpType) **get_op_type** ( )

A type of operands and returned value.
