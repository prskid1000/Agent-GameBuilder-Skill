<span id="class_VisualShaderNodeRemap"></span>

## VisualShaderNodeRemap

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A visual shader node for remap function.

### Description

Remap will transform the input range into output range, e.g. you can change a `0..1` value to `-2..2` etc. See @GlobalScope.remap() for more details.

### Properties


| [OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) | [op_type](class_visualshadernoderemap.md#class_VisualShaderNodeRemap_property_op_type) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeRemap_OpType"></span>

enum **OpType**: [🔗](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType)

<span id="class_VisualShaderNodeRemap_constant_OP_TYPE_SCALAR"></span>

[OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

<span id="class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<span id="class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_2D_SCALAR"></span>

[OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `value` port uses a 2D vector type, while the `input min`, `input max`, `output min`, and `output max` ports use a floating-point scalar type.

<span id="class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

<span id="class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_3D_SCALAR"></span>

[OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `value` port uses a 3D vector type, while the `input min`, `input max`, `output min`, and `output max` ports use a floating-point scalar type.

<span id="class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<span id="class_VisualShaderNodeRemap_constant_OP_TYPE_VECTOR_4D_SCALAR"></span>

[OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `value` port uses a 4D vector type, while the `input min`, `input max`, `output min`, and `output max` ports use a floating-point scalar type.

<span id="class_VisualShaderNodeRemap_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **OP_TYPE_MAX** = `7`

Represents the size of the [OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeRemap_property_op_type"></span>

[OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **op_type** = `0` [🔗](class_visualshadernoderemap.md#class_VisualShaderNodeRemap_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) )
- [OpType](class_visualshadernoderemap.md#enum_VisualShaderNodeRemap_OpType) **get_op_type** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!
