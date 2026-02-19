<span id="class_VisualShaderNodeMultiplyAdd"></span>

## VisualShaderNodeMultiplyAdd

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Performs a fused multiply-add operation within the visual shader graph.

### Description

Uses three operands to compute `(a * b + c)` expression.

### Properties


| [OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) | [op_type](class_visualshadernodemultiplyadd.md#class_VisualShaderNodeMultiplyAdd_property_op_type) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeMultiplyAdd_OpType"></span>

enum **OpType**: [🔗](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType)

<span id="class_VisualShaderNodeMultiplyAdd_constant_OP_TYPE_SCALAR"></span>

[OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

<span id="class_VisualShaderNodeMultiplyAdd_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<span id="class_VisualShaderNodeMultiplyAdd_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

<span id="class_VisualShaderNodeMultiplyAdd_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

<span id="class_VisualShaderNodeMultiplyAdd_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) **OP_TYPE_MAX** = `4`

Represents the size of the [OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeMultiplyAdd_property_op_type"></span>

[OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) **op_type** = `0` [🔗](class_visualshadernodemultiplyadd.md#class_VisualShaderNodeMultiplyAdd_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) )
- [OpType](class_visualshadernodemultiplyadd.md#enum_VisualShaderNodeMultiplyAdd_OpType) **get_op_type** ( )

A type of operands and returned value.
