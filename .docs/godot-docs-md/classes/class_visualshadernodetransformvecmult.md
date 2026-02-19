<span id="class_VisualShaderNodeTransformVecMult"></span>

## VisualShaderNodeTransformVecMult

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Multiplies a [Transform3D](class_transform3d.md#class_Transform3D) and a [Vector3](class_vector3.md#class_Vector3) within the visual shader graph.

### Description

A multiplication operation on a transform (4×4 matrix) and a vector, with support for different multiplication operators.

### Properties


| [Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) | [operator](class_visualshadernodetransformvecmult.md#class_VisualShaderNodeTransformVecMult_property_operator) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeTransformVecMult_Operator"></span>

enum **Operator**: [🔗](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator)

<span id="class_VisualShaderNodeTransformVecMult_constant_OP_AxB"></span>

[Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) **OP_AxB** = `0`

Multiplies transform `a` by the vector `b`.

<span id="class_VisualShaderNodeTransformVecMult_constant_OP_BxA"></span>

[Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) **OP_BxA** = `1`

Multiplies vector `b` by the transform `a`.

<span id="class_VisualShaderNodeTransformVecMult_constant_OP_3x3_AxB"></span>

[Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) **OP_3x3_AxB** = `2`

Multiplies transform `a` by the vector `b`, skipping the last row and column of the transform.

<span id="class_VisualShaderNodeTransformVecMult_constant_OP_3x3_BxA"></span>

[Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) **OP_3x3_BxA** = `3`

Multiplies vector `b` by the transform `a`, skipping the last row and column of the transform.

<span id="class_VisualShaderNodeTransformVecMult_constant_OP_MAX"></span>

[Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) **OP_MAX** = `4`

Represents the size of the [Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeTransformVecMult_property_operator"></span>

[Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) **operator** = `0` [🔗](class_visualshadernodetransformvecmult.md#class_VisualShaderNodeTransformVecMult_property_operator)

- void **set_operator** ( value: [Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) )
- [Operator](class_visualshadernodetransformvecmult.md#enum_VisualShaderNodeTransformVecMult_Operator) **get_operator** ( )

The multiplication type to be performed.
