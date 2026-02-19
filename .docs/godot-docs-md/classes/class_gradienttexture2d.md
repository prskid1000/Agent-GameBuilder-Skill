<span id="class_GradientTexture2D"></span>

## GradientTexture2D

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 2D texture that creates a pattern with colors obtained from a [Gradient](class_gradient.md#class_Gradient).

### Description

A 2D texture that obtains colors from a [Gradient](class_gradient.md#class_Gradient) to fill the texture data. This texture is able to transform a color transition into different patterns such as a linear or a radial gradient. The texture is filled by interpolating colors starting from [fill_from](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_from) to [fill_to](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_to) offsets by default, but the gradient fill can be repeated to cover the entire texture.

The gradient is sampled individually for each pixel so it does not necessarily represent an exact copy of the gradient (see [width](class_gradienttexture2d.md#class_GradientTexture2D_property_width) and [height](class_gradienttexture2d.md#class_GradientTexture2D_property_height)). See also [GradientTexture1D](class_gradienttexture1d.md#class_GradientTexture1D), [CurveTexture](class_curvetexture.md#class_CurveTexture) and [CurveXYZTexture](class_curvexyztexture.md#class_CurveXYZTexture).

### Properties


| [Fill](class_gradienttexture2d.md#enum_GradientTexture2D_Fill) | [fill](class_gradienttexture2d.md#class_GradientTexture2D_property_fill) | `0` |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [fill_from](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_from) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [fill_to](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_to) | `Vector2(1, 0)` |
| [Gradient](class_gradient.md#class_Gradient) | [gradient](class_gradienttexture2d.md#class_GradientTexture2D_property_gradient) |
| [int](class_int.md#class_int) | [height](class_gradienttexture2d.md#class_GradientTexture2D_property_height) | `64` |
| [Repeat](class_gradienttexture2d.md#enum_GradientTexture2D_Repeat) | [repeat](class_gradienttexture2d.md#class_GradientTexture2D_property_repeat) | `0` |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| [bool](class_bool.md#class_bool) | [use_hdr](class_gradienttexture2d.md#class_GradientTexture2D_property_use_hdr) | `false` |
| [int](class_int.md#class_int) | [width](class_gradienttexture2d.md#class_GradientTexture2D_property_width) | `64` |

---

### Enumerations

<span id="enum_GradientTexture2D_Fill"></span>

enum **Fill**: [🔗](class_gradienttexture2d.md#enum_GradientTexture2D_Fill)

<span id="class_GradientTexture2D_constant_FILL_LINEAR"></span>

[Fill](class_gradienttexture2d.md#enum_GradientTexture2D_Fill) **FILL_LINEAR** = `0`

The colors are linearly interpolated in a straight line.

<span id="class_GradientTexture2D_constant_FILL_RADIAL"></span>

[Fill](class_gradienttexture2d.md#enum_GradientTexture2D_Fill) **FILL_RADIAL** = `1`

The colors are linearly interpolated in a circular pattern.

<span id="class_GradientTexture2D_constant_FILL_SQUARE"></span>

[Fill](class_gradienttexture2d.md#enum_GradientTexture2D_Fill) **FILL_SQUARE** = `2`

The colors are linearly interpolated in a square pattern.

<span id="class_GradientTexture2D_constant_FILL_CONIC"></span>

[Fill](class_gradienttexture2d.md#enum_GradientTexture2D_Fill) **FILL_CONIC** = `3`

The colors are linearly interpolated in a cone pattern.

---

<span id="enum_GradientTexture2D_Repeat"></span>

enum **Repeat**: [🔗](class_gradienttexture2d.md#enum_GradientTexture2D_Repeat)

<span id="class_GradientTexture2D_constant_REPEAT_NONE"></span>

[Repeat](class_gradienttexture2d.md#enum_GradientTexture2D_Repeat) **REPEAT_NONE** = `0`

The gradient fill is restricted to the range defined by [fill_from](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_from) to [fill_to](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_to) offsets.

<span id="class_GradientTexture2D_constant_REPEAT"></span>

[Repeat](class_gradienttexture2d.md#enum_GradientTexture2D_Repeat) **REPEAT** = `1`

The texture is filled starting from [fill_from](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_from) to [fill_to](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_to) offsets, repeating the same pattern in both directions.

<span id="class_GradientTexture2D_constant_REPEAT_MIRROR"></span>

[Repeat](class_gradienttexture2d.md#enum_GradientTexture2D_Repeat) **REPEAT_MIRROR** = `2`

The texture is filled starting from [fill_from](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_from) to [fill_to](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_to) offsets, mirroring the pattern in both directions.

---

### Property Descriptions

<span id="class_GradientTexture2D_property_fill"></span>

[Fill](class_gradienttexture2d.md#enum_GradientTexture2D_Fill) **fill** = `0` [🔗](class_gradienttexture2d.md#class_GradientTexture2D_property_fill)

- void **set_fill** ( value: [Fill](class_gradienttexture2d.md#enum_GradientTexture2D_Fill) )
- [Fill](class_gradienttexture2d.md#enum_GradientTexture2D_Fill) **get_fill** ( )

The gradient's fill type.

---

<span id="class_GradientTexture2D_property_fill_from"></span>

[Vector2](class_vector2.md#class_Vector2) **fill_from** = `Vector2(0, 0)` [🔗](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_from)

- void **set_fill_from** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_fill_from** ( )

The initial offset used to fill the texture specified in UV coordinates.

---

<span id="class_GradientTexture2D_property_fill_to"></span>

[Vector2](class_vector2.md#class_Vector2) **fill_to** = `Vector2(1, 0)` [🔗](class_gradienttexture2d.md#class_GradientTexture2D_property_fill_to)

- void **set_fill_to** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_fill_to** ( )

The final offset used to fill the texture specified in UV coordinates.

---

<span id="class_GradientTexture2D_property_gradient"></span>

[Gradient](class_gradient.md#class_Gradient) **gradient** [🔗](class_gradienttexture2d.md#class_GradientTexture2D_property_gradient)

- void **set_gradient** ( value: [Gradient](class_gradient.md#class_Gradient) )
- [Gradient](class_gradient.md#class_Gradient) **get_gradient** ( )

The [Gradient](class_gradient.md#class_Gradient) used to fill the texture.

---

<span id="class_GradientTexture2D_property_height"></span>

[int](class_int.md#class_int) **height** = `64` [🔗](class_gradienttexture2d.md#class_GradientTexture2D_property_height)

- void **set_height** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_height** ( )

The number of vertical color samples that will be obtained from the [Gradient](class_gradient.md#class_Gradient), which also represents the texture's height.

---

<span id="class_GradientTexture2D_property_repeat"></span>

[Repeat](class_gradienttexture2d.md#enum_GradientTexture2D_Repeat) **repeat** = `0` [🔗](class_gradienttexture2d.md#class_GradientTexture2D_property_repeat)

- void **set_repeat** ( value: [Repeat](class_gradienttexture2d.md#enum_GradientTexture2D_Repeat) )
- [Repeat](class_gradienttexture2d.md#enum_GradientTexture2D_Repeat) **get_repeat** ( )

The gradient's repeat type.

---

<span id="class_GradientTexture2D_property_use_hdr"></span>

[bool](class_bool.md#class_bool) **use_hdr** = `false` [🔗](class_gradienttexture2d.md#class_GradientTexture2D_property_use_hdr)

- void **set_use_hdr** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_hdr** ( )

If `true`, the generated texture will support high dynamic range ([Image.FORMAT_RGBAF](class_image.md#class_Image_constant_FORMAT_RGBAF) format). This allows for glow effects to work if [Environment.glow_enabled](class_environment.md#class_Environment_property_glow_enabled) is `true`. If `false`, the generated texture will use low dynamic range; overbright colors will be clamped ([Image.FORMAT_RGBA8](class_image.md#class_Image_constant_FORMAT_RGBA8) format).

---

<span id="class_GradientTexture2D_property_width"></span>

[int](class_int.md#class_int) **width** = `64` [🔗](class_gradienttexture2d.md#class_GradientTexture2D_property_width)

- void **set_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_width** ( )

The number of horizontal color samples that will be obtained from the [Gradient](class_gradient.md#class_Gradient), which also represents the texture's width.
