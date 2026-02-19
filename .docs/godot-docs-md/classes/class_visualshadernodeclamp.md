<span id="class_VisualShaderNodeClamp"></span>

## VisualShaderNodeClamp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Clamps a value within the visual shader graph.

### Description

Constrains a value to lie between `min` and `max` values.

### Properties


| [OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) | [op_type](class_visualshadernodeclamp.md#class_VisualShaderNodeClamp_property_op_type) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeClamp_OpType"></span>

enum **OpType**: [🔗](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType)

<span id="class_VisualShaderNodeClamp_constant_OP_TYPE_FLOAT"></span>

[OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) **OP_TYPE_FLOAT** = `0`

A floating-point scalar.

<span id="class_VisualShaderNodeClamp_constant_OP_TYPE_INT"></span>

[OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) **OP_TYPE_INT** = `1`

An integer scalar.

<span id="class_VisualShaderNodeClamp_constant_OP_TYPE_UINT"></span>

[OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) **OP_TYPE_UINT** = `2`

An unsigned integer scalar.

<span id="class_VisualShaderNodeClamp_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) **OP_TYPE_VECTOR_2D** = `3`

A 2D vector type.

<span id="class_VisualShaderNodeClamp_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) **OP_TYPE_VECTOR_3D** = `4`

A 3D vector type.

<span id="class_VisualShaderNodeClamp_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<span id="class_VisualShaderNodeClamp_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) **OP_TYPE_MAX** = `6`

Represents the size of the [OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeClamp_property_op_type"></span>

[OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) **op_type** = `0` [🔗](class_visualshadernodeclamp.md#class_VisualShaderNodeClamp_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) )
- [OpType](class_visualshadernodeclamp.md#enum_VisualShaderNodeClamp_OpType) **get_op_type** ( )

A type of operands and returned value.
