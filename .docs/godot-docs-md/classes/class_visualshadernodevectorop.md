<span id="class_VisualShaderNodeVectorOp"></span>

## VisualShaderNodeVectorOp

**Inherits:** [VisualShaderNodeVectorBase](class_visualshadernodevectorbase.md#class_VisualShaderNodeVectorBase) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A vector operator to be used within the visual shader graph.

### Description

A visual shader node for use of vector operators. Operates on vector `a` and vector `b`.

### Properties


| [Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) | [operator](class_visualshadernodevectorop.md#class_VisualShaderNodeVectorOp_property_operator) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeVectorOp_Operator"></span>

enum **Operator**: [🔗](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator)

<span id="class_VisualShaderNodeVectorOp_constant_OP_ADD"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_ADD** = `0`

Adds two vectors.

<span id="class_VisualShaderNodeVectorOp_constant_OP_SUB"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_SUB** = `1`

Subtracts a vector from a vector.

<span id="class_VisualShaderNodeVectorOp_constant_OP_MUL"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_MUL** = `2`

Multiplies two vectors.

<span id="class_VisualShaderNodeVectorOp_constant_OP_DIV"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_DIV** = `3`

Divides vector by vector.

<span id="class_VisualShaderNodeVectorOp_constant_OP_MOD"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_MOD** = `4`

Returns the remainder of the two vectors.

<span id="class_VisualShaderNodeVectorOp_constant_OP_POW"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_POW** = `5`

Returns the value of the first parameter raised to the power of the second, for each component of the vectors.

<span id="class_VisualShaderNodeVectorOp_constant_OP_MAX"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_MAX** = `6`

Returns the greater of two values, for each component of the vectors.

<span id="class_VisualShaderNodeVectorOp_constant_OP_MIN"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_MIN** = `7`

Returns the lesser of two values, for each component of the vectors.

<span id="class_VisualShaderNodeVectorOp_constant_OP_CROSS"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_CROSS** = `8`

Calculates the cross product of two vectors.

<span id="class_VisualShaderNodeVectorOp_constant_OP_ATAN2"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_ATAN2** = `9`

Returns the arc-tangent of the parameters.

<span id="class_VisualShaderNodeVectorOp_constant_OP_REFLECT"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_REFLECT** = `10`

Returns the vector that points in the direction of reflection. `a` is incident vector and `b` is the normal vector.

<span id="class_VisualShaderNodeVectorOp_constant_OP_STEP"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_STEP** = `11`

Vector step operator. Returns `0.0` if `a` is smaller than `b` and `1.0` otherwise.

<span id="class_VisualShaderNodeVectorOp_constant_OP_ENUM_SIZE"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **OP_ENUM_SIZE** = `12`

Represents the size of the [Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeVectorOp_property_operator"></span>

[Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **operator** = `0` [🔗](class_visualshadernodevectorop.md#class_VisualShaderNodeVectorOp_property_operator)

- void **set_operator** ( value: [Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) )
- [Operator](class_visualshadernodevectorop.md#enum_VisualShaderNodeVectorOp_Operator) **get_operator** ( )

The operator to be used.
