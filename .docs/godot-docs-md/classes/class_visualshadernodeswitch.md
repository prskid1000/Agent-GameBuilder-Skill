<span id="class_VisualShaderNodeSwitch"></span>

## VisualShaderNodeSwitch

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A selector function for use within the visual shader graph.

### Description

Returns an associated value of the [op_type](class_visualshadernodeswitch.md#class_VisualShaderNodeSwitch_property_op_type) type if the provided boolean value is `true` or `false`.

### Properties


| [OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) | [op_type](class_visualshadernodeswitch.md#class_VisualShaderNodeSwitch_property_op_type) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeSwitch_OpType"></span>

enum **OpType**: [🔗](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType)

<span id="class_VisualShaderNodeSwitch_constant_OP_TYPE_FLOAT"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **OP_TYPE_FLOAT** = `0`

A floating-point scalar.

<span id="class_VisualShaderNodeSwitch_constant_OP_TYPE_INT"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **OP_TYPE_INT** = `1`

An integer scalar.

<span id="class_VisualShaderNodeSwitch_constant_OP_TYPE_UINT"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **OP_TYPE_UINT** = `2`

An unsigned integer scalar.

<span id="class_VisualShaderNodeSwitch_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **OP_TYPE_VECTOR_2D** = `3`

A 2D vector type.

<span id="class_VisualShaderNodeSwitch_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **OP_TYPE_VECTOR_3D** = `4`

A 3D vector type.

<span id="class_VisualShaderNodeSwitch_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

<span id="class_VisualShaderNodeSwitch_constant_OP_TYPE_BOOLEAN"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **OP_TYPE_BOOLEAN** = `6`

A boolean type.

<span id="class_VisualShaderNodeSwitch_constant_OP_TYPE_TRANSFORM"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **OP_TYPE_TRANSFORM** = `7`

A transform type.

<span id="class_VisualShaderNodeSwitch_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **OP_TYPE_MAX** = `8`

Represents the size of the [OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeSwitch_property_op_type"></span>

[OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **op_type** = `0` [🔗](class_visualshadernodeswitch.md#class_VisualShaderNodeSwitch_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) )
- [OpType](class_visualshadernodeswitch.md#enum_VisualShaderNodeSwitch_OpType) **get_op_type** ( )

A type of operands and returned value.
