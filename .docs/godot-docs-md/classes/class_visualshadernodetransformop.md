<span id="class_VisualShaderNodeTransformOp"></span>

## VisualShaderNodeTransformOp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Transform3D](class_transform3d.md#class_Transform3D) operator to be used within the visual shader graph.

### Description

Applies [operator](class_visualshadernodetransformop.md#class_VisualShaderNodeTransformOp_property_operator) to two transform (4×4 matrices) inputs.

### Properties


| [Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) | [operator](class_visualshadernodetransformop.md#class_VisualShaderNodeTransformOp_property_operator) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeTransformOp_Operator"></span>

enum **Operator**: [🔗](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator)

<span id="class_VisualShaderNodeTransformOp_constant_OP_AxB"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_AxB** = `0`

Multiplies transform `a` by the transform `b`.

<span id="class_VisualShaderNodeTransformOp_constant_OP_BxA"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_BxA** = `1`

Multiplies transform `b` by the transform `a`.

<span id="class_VisualShaderNodeTransformOp_constant_OP_AxB_COMP"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_AxB_COMP** = `2`

Performs a component-wise multiplication of transform `a` by the transform `b`.

<span id="class_VisualShaderNodeTransformOp_constant_OP_BxA_COMP"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_BxA_COMP** = `3`

Performs a component-wise multiplication of transform `b` by the transform `a`.

<span id="class_VisualShaderNodeTransformOp_constant_OP_ADD"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_ADD** = `4`

Adds two transforms.

<span id="class_VisualShaderNodeTransformOp_constant_OP_A_MINUS_B"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_A_MINUS_B** = `5`

Subtracts the transform `a` from the transform `b`.

<span id="class_VisualShaderNodeTransformOp_constant_OP_B_MINUS_A"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_B_MINUS_A** = `6`

Subtracts the transform `b` from the transform `a`.

<span id="class_VisualShaderNodeTransformOp_constant_OP_A_DIV_B"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_A_DIV_B** = `7`

Divides the transform `a` by the transform `b`.

<span id="class_VisualShaderNodeTransformOp_constant_OP_B_DIV_A"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_B_DIV_A** = `8`

Divides the transform `b` by the transform `a`.

<span id="class_VisualShaderNodeTransformOp_constant_OP_MAX"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **OP_MAX** = `9`

Represents the size of the [Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeTransformOp_property_operator"></span>

[Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **operator** = `0` [🔗](class_visualshadernodetransformop.md#class_VisualShaderNodeTransformOp_property_operator)

- void **set_operator** ( value: [Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) )
- [Operator](class_visualshadernodetransformop.md#enum_VisualShaderNodeTransformOp_Operator) **get_operator** ( )

The type of the operation to be performed on the transforms.
