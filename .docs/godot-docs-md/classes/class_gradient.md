<span id="class_Gradient"></span>

## Gradient

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A color transition.

### Description

This resource describes a color transition by defining a set of colored points and how to interpolate between them.

See also [Curve](class_curve.md#class_Curve) which supports more complex easing methods, but does not support colors.

### Properties


| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [colors](class_gradient.md#class_Gradient_property_colors) | `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)` |
| --- | --- | --- |
| [ColorSpace](class_gradient.md#enum_Gradient_ColorSpace) | [interpolation_color_space](class_gradient.md#class_Gradient_property_interpolation_color_space) | `0` |
| [InterpolationMode](class_gradient.md#enum_Gradient_InterpolationMode) | [interpolation_mode](class_gradient.md#class_Gradient_property_interpolation_mode) | `0` |
| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [offsets](class_gradient.md#class_Gradient_property_offsets) | `PackedFloat32Array(0, 1)` |

### Methods


| void | [add_point](class_gradient.md#class_Gradient_method_add_point) ( offset: [float](class_float.md#class_float), color: [Color](class_color.md#class_Color) ) |
| --- | --- |
| [Color](class_color.md#class_Color) | [get_color](class_gradient.md#class_Gradient_method_get_color) ( point: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | [get_offset](class_gradient.md#class_Gradient_method_get_offset) ( point: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_point_count](class_gradient.md#class_Gradient_method_get_point_count) ( ) const |
| void | [remove_point](class_gradient.md#class_Gradient_method_remove_point) ( point: [int](class_int.md#class_int) ) |
| void | [reverse](class_gradient.md#class_Gradient_method_reverse) ( ) |
| [Color](class_color.md#class_Color) | [sample](class_gradient.md#class_Gradient_method_sample) ( offset: [float](class_float.md#class_float) ) |
| void | [set_color](class_gradient.md#class_Gradient_method_set_color) ( point: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_offset](class_gradient.md#class_Gradient_method_set_offset) ( point: [int](class_int.md#class_int), offset: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_Gradient_InterpolationMode"></span>

enum **InterpolationMode**: [🔗](class_gradient.md#enum_Gradient_InterpolationMode)

<span id="class_Gradient_constant_GRADIENT_INTERPOLATE_LINEAR"></span>

[InterpolationMode](class_gradient.md#enum_Gradient_InterpolationMode) **GRADIENT_INTERPOLATE_LINEAR** = `0`

Linear interpolation.

<span id="class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT"></span>

[InterpolationMode](class_gradient.md#enum_Gradient_InterpolationMode) **GRADIENT_INTERPOLATE_CONSTANT** = `1`

Constant interpolation, color changes abruptly at each point and stays uniform between. This might cause visible aliasing when used for a gradient texture in some cases.

<span id="class_Gradient_constant_GRADIENT_INTERPOLATE_CUBIC"></span>

[InterpolationMode](class_gradient.md#enum_Gradient_InterpolationMode) **GRADIENT_INTERPOLATE_CUBIC** = `2`

Cubic interpolation.

---

<span id="enum_Gradient_ColorSpace"></span>

enum **ColorSpace**: [🔗](class_gradient.md#enum_Gradient_ColorSpace)

<span id="class_Gradient_constant_GRADIENT_COLOR_SPACE_SRGB"></span>

[ColorSpace](class_gradient.md#enum_Gradient_ColorSpace) **GRADIENT_COLOR_SPACE_SRGB** = `0`

sRGB color space.

<span id="class_Gradient_constant_GRADIENT_COLOR_SPACE_LINEAR_SRGB"></span>

[ColorSpace](class_gradient.md#enum_Gradient_ColorSpace) **GRADIENT_COLOR_SPACE_LINEAR_SRGB** = `1`

Linear sRGB color space.

<span id="class_Gradient_constant_GRADIENT_COLOR_SPACE_OKLAB"></span>

[ColorSpace](class_gradient.md#enum_Gradient_ColorSpace) **GRADIENT_COLOR_SPACE_OKLAB** = `2`

Oklab color space. This color space provides a smooth and uniform-looking transition between colors.

---

### Property Descriptions

<span id="class_Gradient_property_colors"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **colors** = `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)` [🔗](class_gradient.md#class_Gradient_property_colors)

- void **set_colors** ( value: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) )
- [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **get_colors** ( )

Gradient's colors as a [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray).

 **Note:** Setting this property updates all colors at once. To update any color individually use [set_color()](class_gradient.md#class_Gradient_method_set_color).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) for more details.

---

<span id="class_Gradient_property_interpolation_color_space"></span>

[ColorSpace](class_gradient.md#enum_Gradient_ColorSpace) **interpolation_color_space** = `0` [🔗](class_gradient.md#class_Gradient_property_interpolation_color_space)

- void **set_interpolation_color_space** ( value: [ColorSpace](class_gradient.md#enum_Gradient_ColorSpace) )
- [ColorSpace](class_gradient.md#enum_Gradient_ColorSpace) **get_interpolation_color_space** ( )

The color space used to interpolate between points of the gradient. It does not affect the returned colors, which will always use nonlinear sRGB encoding.

 **Note:** This setting has no effect when [interpolation_mode](class_gradient.md#class_Gradient_property_interpolation_mode) is set to [GRADIENT_INTERPOLATE_CONSTANT](class_gradient.md#class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT).

---

<span id="class_Gradient_property_interpolation_mode"></span>

[InterpolationMode](class_gradient.md#enum_Gradient_InterpolationMode) **interpolation_mode** = `0` [🔗](class_gradient.md#class_Gradient_property_interpolation_mode)

- void **set_interpolation_mode** ( value: [InterpolationMode](class_gradient.md#enum_Gradient_InterpolationMode) )
- [InterpolationMode](class_gradient.md#enum_Gradient_InterpolationMode) **get_interpolation_mode** ( )

The algorithm used to interpolate between points of the gradient.

---

<span id="class_Gradient_property_offsets"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **offsets** = `PackedFloat32Array(0, 1)` [🔗](class_gradient.md#class_Gradient_property_offsets)

- void **set_offsets** ( value: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) )
- [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **get_offsets** ( )

Gradient's offsets as a [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array).

 **Note:** Setting this property updates all offsets at once. To update any offset individually use [set_offset()](class_gradient.md#class_Gradient_method_set_offset).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) for more details.

---

### Method Descriptions

<span id="class_Gradient_method_add_point"></span>

void **add_point** ( offset: [float](class_float.md#class_float), color: [Color](class_color.md#class_Color) ) [🔗](class_gradient.md#class_Gradient_method_add_point)

Adds the specified color to the gradient, with the specified offset.

---

<span id="class_Gradient_method_get_color"></span>

[Color](class_color.md#class_Color) **get_color** ( point: [int](class_int.md#class_int) ) [🔗](class_gradient.md#class_Gradient_method_get_color)

Returns the color of the gradient color at index `point`.

---

<span id="class_Gradient_method_get_offset"></span>

[float](class_float.md#class_float) **get_offset** ( point: [int](class_int.md#class_int) ) [🔗](class_gradient.md#class_Gradient_method_get_offset)

Returns the offset of the gradient color at index `point`.

---

<span id="class_Gradient_method_get_point_count"></span>

[int](class_int.md#class_int) **get_point_count** ( ) *const* [🔗](class_gradient.md#class_Gradient_method_get_point_count)

Returns the number of colors in the gradient.

---

<span id="class_Gradient_method_remove_point"></span>

void **remove_point** ( point: [int](class_int.md#class_int) ) [🔗](class_gradient.md#class_Gradient_method_remove_point)

Removes the color at index `point`.

---

<span id="class_Gradient_method_reverse"></span>

void **reverse** ( ) [🔗](class_gradient.md#class_Gradient_method_reverse)

Reverses/mirrors the gradient.

 **Note:** This method mirrors all points around the middle of the gradient, which may produce unexpected results when [interpolation_mode](class_gradient.md#class_Gradient_property_interpolation_mode) is set to [GRADIENT_INTERPOLATE_CONSTANT](class_gradient.md#class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT).

---

<span id="class_Gradient_method_sample"></span>

[Color](class_color.md#class_Color) **sample** ( offset: [float](class_float.md#class_float) ) [🔗](class_gradient.md#class_Gradient_method_sample)

Returns the interpolated color specified by `offset`. `offset` should be between `0.0` and `1.0` (inclusive). Using a value lower than `0.0` will return the same color as `0.0`, and using a value higher than `1.0` will return the same color as `1.0`. If your input value is not within this range, consider using @GlobalScope.remap() on the input value with output values set to `0.0` and `1.0`.

---

<span id="class_Gradient_method_set_color"></span>

void **set_color** ( point: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_gradient.md#class_Gradient_method_set_color)

Sets the color of the gradient color at index `point`.

---

<span id="class_Gradient_method_set_offset"></span>

void **set_offset** ( point: [int](class_int.md#class_int), offset: [float](class_float.md#class_float) ) [🔗](class_gradient.md#class_Gradient_method_set_offset)

Sets the offset for the gradient color at index `point`.
