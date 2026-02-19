<span id="class_VisualShaderNodeVectorBase"></span>

## VisualShaderNodeVectorBase

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeFaceForward](class_visualshadernodefaceforward.md#class_VisualShaderNodeFaceForward), [VisualShaderNodeVectorCompose](class_visualshadernodevectorcompose.md#class_VisualShaderNodeVectorCompose), [VisualShaderNodeVectorDecompose](class_visualshadernodevectordecompose.md#class_VisualShaderNodeVectorDecompose), [VisualShaderNodeVectorDistance](class_visualshadernodevectordistance.md#class_VisualShaderNodeVectorDistance), [VisualShaderNodeVectorFunc](class_visualshadernodevectorfunc.md#class_VisualShaderNodeVectorFunc), [VisualShaderNodeVectorLen](class_visualshadernodevectorlen.md#class_VisualShaderNodeVectorLen), [VisualShaderNodeVectorOp](class_visualshadernodevectorop.md#class_VisualShaderNodeVectorOp), [VisualShaderNodeVectorRefract](class_visualshadernodevectorrefract.md#class_VisualShaderNodeVectorRefract)

A base type for the nodes that perform vector operations within the visual shader graph.

### Description

This is an abstract class. See the derived types for descriptions of the possible operations.

### Properties


| [OpType](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType) | [op_type](class_visualshadernodevectorbase.md#class_VisualShaderNodeVectorBase_property_op_type) | `1` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeVectorBase_OpType"></span>

enum **OpType**: [🔗](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType)

<span id="class_VisualShaderNodeVectorBase_constant_OP_TYPE_VECTOR_2D"></span>

[OpType](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType) **OP_TYPE_VECTOR_2D** = `0`

A 2D vector type.

<span id="class_VisualShaderNodeVectorBase_constant_OP_TYPE_VECTOR_3D"></span>

[OpType](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType) **OP_TYPE_VECTOR_3D** = `1`

A 3D vector type.

<span id="class_VisualShaderNodeVectorBase_constant_OP_TYPE_VECTOR_4D"></span>

[OpType](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType) **OP_TYPE_VECTOR_4D** = `2`

A 4D vector type.

<span id="class_VisualShaderNodeVectorBase_constant_OP_TYPE_MAX"></span>

[OpType](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType) **OP_TYPE_MAX** = `3`

Represents the size of the [OpType](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeVectorBase_property_op_type"></span>

[OpType](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType) **op_type** = `1` [🔗](class_visualshadernodevectorbase.md#class_VisualShaderNodeVectorBase_property_op_type)

- void **set_op_type** ( value: [OpType](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType) )
- [OpType](class_visualshadernodevectorbase.md#enum_VisualShaderNodeVectorBase_OpType) **get_op_type** ( )

A vector type that this operation is performed on.
