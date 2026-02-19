<span id="class_CurveTexture"></span>

## CurveTexture

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 1D texture where pixel brightness corresponds to points on a curve.

### Description

A 1D texture where pixel brightness corresponds to points on a unit [Curve](class_curve.md#class_Curve) resource, either in grayscale or in red. This visual representation simplifies the task of saving curves as image files.

If you need to store up to 3 curves within a single texture, use [CurveXYZTexture](class_curvexyztexture.md#class_CurveXYZTexture) instead. See also [GradientTexture1D](class_gradienttexture1d.md#class_GradientTexture1D) and [GradientTexture2D](class_gradienttexture2d.md#class_GradientTexture2D).

### Properties


| [Curve](class_curve.md#class_Curve) | [curve](class_curvetexture.md#class_CurveTexture_property_curve) |
| --- | --- |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| [TextureMode](class_curvetexture.md#enum_CurveTexture_TextureMode) | [texture_mode](class_curvetexture.md#class_CurveTexture_property_texture_mode) | `0` |
| [int](class_int.md#class_int) | [width](class_curvetexture.md#class_CurveTexture_property_width) | `256` |

---

### Enumerations

<span id="enum_CurveTexture_TextureMode"></span>

enum **TextureMode**: [🔗](class_curvetexture.md#enum_CurveTexture_TextureMode)

<span id="class_CurveTexture_constant_TEXTURE_MODE_RGB"></span>

[TextureMode](class_curvetexture.md#enum_CurveTexture_TextureMode) **TEXTURE_MODE_RGB** = `0`

Store the curve equally across the red, green and blue channels. This uses more video memory, but is more compatible with shaders that only read the green and blue values.

<span id="class_CurveTexture_constant_TEXTURE_MODE_RED"></span>

[TextureMode](class_curvetexture.md#enum_CurveTexture_TextureMode) **TEXTURE_MODE_RED** = `1`

Store the curve only in the red channel. This saves video memory, but some custom shaders may not be able to work with this.

---

### Property Descriptions

<span id="class_CurveTexture_property_curve"></span>

[Curve](class_curve.md#class_Curve) **curve** [🔗](class_curvetexture.md#class_CurveTexture_property_curve)

- void **set_curve** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_curve** ( )

The [Curve](class_curve.md#class_Curve) that is rendered onto the texture. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CurveTexture_property_texture_mode"></span>

[TextureMode](class_curvetexture.md#enum_CurveTexture_TextureMode) **texture_mode** = `0` [🔗](class_curvetexture.md#class_CurveTexture_property_texture_mode)

- void **set_texture_mode** ( value: [TextureMode](class_curvetexture.md#enum_CurveTexture_TextureMode) )
- [TextureMode](class_curvetexture.md#enum_CurveTexture_TextureMode) **get_texture_mode** ( )

The format the texture should be generated with. When passing a CurveTexture as an input to a [Shader](class_shader.md#class_Shader), this may need to be adjusted.

---

<span id="class_CurveTexture_property_width"></span>

[int](class_int.md#class_int) **width** = `256` [🔗](class_curvetexture.md#class_CurveTexture_property_width)

- void **set_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_width** ( )

The width of the texture (in pixels). Higher values make it possible to represent high-frequency data better (such as sudden direction changes), at the cost of increased generation time and memory usage.
