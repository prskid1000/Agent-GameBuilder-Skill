<span id="class_GradientTexture1D"></span>

## GradientTexture1D

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 1D texture that uses colors obtained from a [Gradient](class_gradient.md#class_Gradient).

### Description

A 1D texture that obtains colors from a [Gradient](class_gradient.md#class_Gradient) to fill the texture data. The texture is filled by sampling the gradient for each pixel. Therefore, the texture does not necessarily represent an exact copy of the gradient, as it may miss some colors if there are not enough pixels. See also [GradientTexture2D](class_gradienttexture2d.md#class_GradientTexture2D), [CurveTexture](class_curvetexture.md#class_CurveTexture) and [CurveXYZTexture](class_curvexyztexture.md#class_CurveXYZTexture).

### Properties


| [Gradient](class_gradient.md#class_Gradient) | [gradient](class_gradienttexture1d.md#class_GradientTexture1D_property_gradient) |
| --- | --- |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| [bool](class_bool.md#class_bool) | [use_hdr](class_gradienttexture1d.md#class_GradientTexture1D_property_use_hdr) | `false` |
| [int](class_int.md#class_int) | [width](class_gradienttexture1d.md#class_GradientTexture1D_property_width) | `256` |

---

### Property Descriptions

<span id="class_GradientTexture1D_property_gradient"></span>

[Gradient](class_gradient.md#class_Gradient) **gradient** [🔗](class_gradienttexture1d.md#class_GradientTexture1D_property_gradient)

- void **set_gradient** ( value: [Gradient](class_gradient.md#class_Gradient) )
- [Gradient](class_gradient.md#class_Gradient) **get_gradient** ( )

The [Gradient](class_gradient.md#class_Gradient) used to fill the texture.

---

<span id="class_GradientTexture1D_property_use_hdr"></span>

[bool](class_bool.md#class_bool) **use_hdr** = `false` [🔗](class_gradienttexture1d.md#class_GradientTexture1D_property_use_hdr)

- void **set_use_hdr** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_hdr** ( )

If `true`, the generated texture will support high dynamic range ([Image.FORMAT_RGBAF](class_image.md#class_Image_constant_FORMAT_RGBAF) format). This allows for glow effects to work if [Environment.glow_enabled](class_environment.md#class_Environment_property_glow_enabled) is `true`. If `false`, the generated texture will use low dynamic range; overbright colors will be clamped ([Image.FORMAT_RGBA8](class_image.md#class_Image_constant_FORMAT_RGBA8) format).

---

<span id="class_GradientTexture1D_property_width"></span>

[int](class_int.md#class_int) **width** = `256` [🔗](class_gradienttexture1d.md#class_GradientTexture1D_property_width)

- void **set_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_width** ( )

The number of color samples that will be obtained from the [Gradient](class_gradient.md#class_Gradient).
