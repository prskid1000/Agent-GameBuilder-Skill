<span id="class_VisualShaderNodeParticleRandomness"></span>

## VisualShaderNodeParticleRandomness

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Visual shader node for randomizing particle values.

### Description

Randomness node will output pseudo-random values of the given type based on the specified minimum and maximum values.

### Properties


| [OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) | [op_type](class_visualshadernodeparticlerandomness.md#class_VisualShaderNodeParticleRandomness_property_op_type) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeParticleRandomness_OpType"></span>

enum **OpType**: [🔗](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType)

<span id="class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_SCALAR"></span>

[OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

<span id="class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

<span id="class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

<span id="class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

<span id="class_VisualShaderNodeParticleRandomness_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) **OP_TYPE_MAX** = `4`

Represents the size of the [OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeParticleRandomness_property_op_type"></span>

[OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) **op_type** = `0` [🔗](class_visualshadernodeparticlerandomness.md#class_VisualShaderNodeParticleRandomness_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) )
- [OpType](class_visualshadernodeparticlerandomness.md#enum_VisualShaderNodeParticleRandomness_OpType) **get_op_type** ( )

A type of operands and returned value.
