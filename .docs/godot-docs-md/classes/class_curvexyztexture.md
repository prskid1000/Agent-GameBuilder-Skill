<span id="class_CurveXYZTexture"></span>

## CurveXYZTexture

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 1D texture where the red, green, and blue color channels correspond to points on 3 curves.

### Description

A 1D texture where the red, green, and blue color channels correspond to points on 3 unit [Curve](class_curve.md#class_Curve) resources. Compared to using separate [CurveTexture](class_curvetexture.md#class_CurveTexture) s, this further simplifies the task of saving curves as image files.

If you only need to store one curve within a single texture, use [CurveTexture](class_curvetexture.md#class_CurveTexture) instead. See also [GradientTexture1D](class_gradienttexture1d.md#class_GradientTexture1D) and [GradientTexture2D](class_gradienttexture2d.md#class_GradientTexture2D).

### Properties


| [Curve](class_curve.md#class_Curve) | [curve_x](class_curvexyztexture.md#class_CurveXYZTexture_property_curve_x) |
| --- | --- |
| [Curve](class_curve.md#class_Curve) | [curve_y](class_curvexyztexture.md#class_CurveXYZTexture_property_curve_y) |
| [Curve](class_curve.md#class_Curve) | [curve_z](class_curvexyztexture.md#class_CurveXYZTexture_property_curve_z) |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| [int](class_int.md#class_int) | [width](class_curvexyztexture.md#class_CurveXYZTexture_property_width) | `256` |

---

### Property Descriptions

<span id="class_CurveXYZTexture_property_curve_x"></span>

[Curve](class_curve.md#class_Curve) **curve_x** [🔗](class_curvexyztexture.md#class_CurveXYZTexture_property_curve_x)

- void **set_curve_x** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_curve_x** ( )

The [Curve](class_curve.md#class_Curve) that is rendered onto the texture's red channel. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CurveXYZTexture_property_curve_y"></span>

[Curve](class_curve.md#class_Curve) **curve_y** [🔗](class_curvexyztexture.md#class_CurveXYZTexture_property_curve_y)

- void **set_curve_y** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_curve_y** ( )

The [Curve](class_curve.md#class_Curve) that is rendered onto the texture's green channel. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CurveXYZTexture_property_curve_z"></span>

[Curve](class_curve.md#class_Curve) **curve_z** [🔗](class_curvexyztexture.md#class_CurveXYZTexture_property_curve_z)

- void **set_curve_z** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_curve_z** ( )

The [Curve](class_curve.md#class_Curve) that is rendered onto the texture's blue channel. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CurveXYZTexture_property_width"></span>

[int](class_int.md#class_int) **width** = `256` [🔗](class_curvexyztexture.md#class_CurveXYZTexture_property_width)

- void **set_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_width** ( )

The width of the texture (in pixels). Higher values make it possible to represent high-frequency data better (such as sudden direction changes), at the cost of increased generation time and memory usage.
