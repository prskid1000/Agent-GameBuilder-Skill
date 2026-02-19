<span id="class_VisualShaderNodeMix"></span>

## VisualShaderNodeMix

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Linearly interpolates between two values within the visual shader graph.

### Description

Translates to `mix(a, b, weight)` in the shader language.

### Properties


| [OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) | [op_type](class_visualshadernodemix.md#class_VisualShaderNodeMix_property_op_type) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeMix_OpType"></span>

enum **OpType**: [🔗](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType)

<span id="class_VisualShaderNodeMix_constant_OP_TYPE_SCALAR"></span>

[OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

<span id="class_VisualShaderNodeMix_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<span id="class_VisualShaderNodeMix_constant_OP_TYPE_VECTOR_2D_SCALAR"></span>

[OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `a` and `b` ports use a 2D vector type. The `weight` port uses a scalar type.

<span id="class_VisualShaderNodeMix_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

<span id="class_VisualShaderNodeMix_constant_OP_TYPE_VECTOR_3D_SCALAR"></span>

[OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `a` and `b` ports use a 3D vector type. The `weight` port uses a scalar type.

<span id="class_VisualShaderNodeMix_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<span id="class_VisualShaderNodeMix_constant_OP_TYPE_VECTOR_4D_SCALAR"></span>

[OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `a` and `b` ports use a 4D vector type. The `weight` port uses a scalar type.

<span id="class_VisualShaderNodeMix_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **OP_TYPE_MAX** = `7`

Represents the size of the [OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeMix_property_op_type"></span>

[OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **op_type** = `0` [🔗](class_visualshadernodemix.md#class_VisualShaderNodeMix_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) )
- [OpType](class_visualshadernodemix.md#enum_VisualShaderNodeMix_OpType) **get_op_type** ( )

A type of operands and returned value.
