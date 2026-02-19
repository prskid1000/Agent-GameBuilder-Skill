<span id="class_VisualShaderNodeColorOp"></span>

## VisualShaderNodeColorOp

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Color](class_color.md#class_Color) operator to be used within the visual shader graph.

### Description

Applies [operator](class_visualshadernodecolorop.md#class_VisualShaderNodeColorOp_property_operator) to two color inputs.

### Properties


| [Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) | [operator](class_visualshadernodecolorop.md#class_VisualShaderNodeColorOp_property_operator) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeColorOp_Operator"></span>

enum **Operator**: [🔗](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator)

<span id="class_VisualShaderNodeColorOp_constant_OP_SCREEN"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_SCREEN** = `0`

Produce a screen effect with the following formula:

::

    result = vec3(1.0) - (vec3(1.0) - a) * (vec3(1.0) - b);

<span id="class_VisualShaderNodeColorOp_constant_OP_DIFFERENCE"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_DIFFERENCE** = `1`

Produce a difference effect with the following formula:

::

    result = abs(a - b);

<span id="class_VisualShaderNodeColorOp_constant_OP_DARKEN"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_DARKEN** = `2`

Produce a darken effect with the following formula:

::

    result = min(a, b);

<span id="class_VisualShaderNodeColorOp_constant_OP_LIGHTEN"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_LIGHTEN** = `3`

Produce a lighten effect with the following formula:

::

    result = max(a, b);

<span id="class_VisualShaderNodeColorOp_constant_OP_OVERLAY"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_OVERLAY** = `4`

Produce an overlay effect with the following formula:

::

    for (int i = 0; i < 3; i++) {
        float base = a[i];
        float blend = b[i];
        if (base < 0.5) {
            result[i] = 2.0 * base * blend;
        } else {
            result[i] = 1.0 - 2.0 * (1.0 - blend) * (1.0 - base);
        }
    }

<span id="class_VisualShaderNodeColorOp_constant_OP_DODGE"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_DODGE** = `5`

Produce a dodge effect with the following formula:

::

    result = a / (vec3(1.0) - b);

<span id="class_VisualShaderNodeColorOp_constant_OP_BURN"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_BURN** = `6`

Produce a burn effect with the following formula:

::

    result = vec3(1.0) - (vec3(1.0) - a) / b;

<span id="class_VisualShaderNodeColorOp_constant_OP_SOFT_LIGHT"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_SOFT_LIGHT** = `7`

Produce a soft light effect with the following formula:

::

    for (int i = 0; i < 3; i++) {
        float base = a[i];
        float blend = b[i];
        if (base < 0.5) {
            result[i] = base * (blend + 0.5);
        } else {
            result[i] = 1.0 - (1.0 - base) * (1.0 - (blend - 0.5));
        }
    }

<span id="class_VisualShaderNodeColorOp_constant_OP_HARD_LIGHT"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_HARD_LIGHT** = `8`

Produce a hard light effect with the following formula:

::

    for (int i = 0; i < 3; i++) {
        float base = a[i];
        float blend = b[i];
        if (base < 0.5) {
            result[i] = base * (2.0 * blend);
        } else {
            result[i] = 1.0 - (1.0 - base) * (1.0 - 2.0 * (blend - 0.5));
        }
    }

<span id="class_VisualShaderNodeColorOp_constant_OP_MAX"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **OP_MAX** = `9`

Represents the size of the [Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeColorOp_property_operator"></span>

[Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **operator** = `0` [🔗](class_visualshadernodecolorop.md#class_VisualShaderNodeColorOp_property_operator)

- void **set_operator** ( value: [Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) )
- [Operator](class_visualshadernodecolorop.md#enum_VisualShaderNodeColorOp_Operator) **get_operator** ( )

An operator to be applied to the inputs.
