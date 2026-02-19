<span id="class_VisualShaderNodeColorFunc"></span>

## VisualShaderNodeColorFunc

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Color](class_color.md#class_Color) function to be used within the visual shader graph.

### Description

Accept a [Color](class_color.md#class_Color) to the input port and transform it according to [function](class_visualshadernodecolorfunc.md#class_VisualShaderNodeColorFunc_property_function).

### Properties


| [Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) | [function](class_visualshadernodecolorfunc.md#class_VisualShaderNodeColorFunc_property_function) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeColorFunc_Function"></span>

enum **Function**: [🔗](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function)

<span id="class_VisualShaderNodeColorFunc_constant_FUNC_GRAYSCALE"></span>

[Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) **FUNC_GRAYSCALE** = `0`

Converts the color to grayscale using the following formula:

::

    vec3 c = input;
    float max1 = max(c.r, c.g);
    float max2 = max(max1, c.b);
    float max3 = max(max1, max2);
    return vec3(max3, max3, max3);

<span id="class_VisualShaderNodeColorFunc_constant_FUNC_HSV2RGB"></span>

[Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) **FUNC_HSV2RGB** = `1`

Converts HSV vector to RGB equivalent.

<span id="class_VisualShaderNodeColorFunc_constant_FUNC_RGB2HSV"></span>

[Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) **FUNC_RGB2HSV** = `2`

Converts RGB vector to HSV equivalent.

<span id="class_VisualShaderNodeColorFunc_constant_FUNC_SEPIA"></span>

[Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) **FUNC_SEPIA** = `3`

Applies sepia tone effect using the following formula:

::

    vec3 c = input;
    float r = (c.r * 0.393) + (c.g * 0.769) + (c.b * 0.189);
    float g = (c.r * 0.349) + (c.g * 0.686) + (c.b * 0.168);
    float b = (c.r * 0.272) + (c.g * 0.534) + (c.b * 0.131);
    return vec3(r, g, b);

<span id="class_VisualShaderNodeColorFunc_constant_FUNC_LINEAR_TO_SRGB"></span>

[Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) **FUNC_LINEAR_TO_SRGB** = `4`

Converts color from linear encoding to nonlinear sRGB encoding using the following formula:

::

    vec3 c = clamp(c, vec3(0.0), vec3(1.0));
    const vec3 a = vec3(0.055f);
    return mix((vec3(1.0f) + a) * pow(c.rgb, vec3(1.0f / 2.4f)) - a, 12.92f * c.rgb, lessThan(c.rgb, vec3(0.0031308f)));

The Compatibility renderer uses a simpler formula:

::

    vec3 c = input;
    return max(vec3(1.055) * pow(c, vec3(0.416666667)) - vec3(0.055), vec3(0.0));

<span id="class_VisualShaderNodeColorFunc_constant_FUNC_SRGB_TO_LINEAR"></span>

[Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) **FUNC_SRGB_TO_LINEAR** = `5`

Converts color from nonlinear sRGB encoding to linear encoding using the following formula:

::

    vec3 c = input;
    return mix(pow((c.rgb + vec3(0.055)) * (1.0 / (1.0 + 0.055)), vec3(2.4)), c.rgb * (1.0 / 12.92), lessThan(c.rgb, vec3(0.04045)));

The Compatibility renderer uses a simpler formula:

::

    vec3 c = input;
    return c * (c * (c * 0.305306011 + 0.682171111) + 0.012522878);

<span id="class_VisualShaderNodeColorFunc_constant_FUNC_MAX"></span>

[Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) **FUNC_MAX** = `6`

Represents the size of the [Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeColorFunc_property_function"></span>

[Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) **function** = `0` [🔗](class_visualshadernodecolorfunc.md#class_VisualShaderNodeColorFunc_property_function)

- void **set_function** ( value: [Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) )
- [Function](class_visualshadernodecolorfunc.md#enum_VisualShaderNodeColorFunc_Function) **get_function** ( )

A function to be applied to the input color.
