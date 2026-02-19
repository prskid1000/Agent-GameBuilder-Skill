<span id="class_RDSamplerState"></span>

## RDSamplerState

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Sampler state (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [float](class_float.md#class_float) | [anisotropy_max](class_rdsamplerstate.md#class_RDSamplerState_property_anisotropy_max) | `1.0` |
| --- | --- | --- |
| [SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) | [border_color](class_rdsamplerstate.md#class_RDSamplerState_property_border_color) | `2` |
| [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) | [compare_op](class_rdsamplerstate.md#class_RDSamplerState_property_compare_op) | `7` |
| [bool](class_bool.md#class_bool) | [enable_compare](class_rdsamplerstate.md#class_RDSamplerState_property_enable_compare) | `false` |
| [float](class_float.md#class_float) | [lod_bias](class_rdsamplerstate.md#class_RDSamplerState_property_lod_bias) | `0.0` |
| [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) | [mag_filter](class_rdsamplerstate.md#class_RDSamplerState_property_mag_filter) | `0` |
| [float](class_float.md#class_float) | [max_lod](class_rdsamplerstate.md#class_RDSamplerState_property_max_lod) | `1e+20` |
| [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) | [min_filter](class_rdsamplerstate.md#class_RDSamplerState_property_min_filter) | `0` |
| [float](class_float.md#class_float) | [min_lod](class_rdsamplerstate.md#class_RDSamplerState_property_min_lod) | `0.0` |
| [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) | [mip_filter](class_rdsamplerstate.md#class_RDSamplerState_property_mip_filter) | `0` |
| [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) | [repeat_u](class_rdsamplerstate.md#class_RDSamplerState_property_repeat_u) | `2` |
| [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) | [repeat_v](class_rdsamplerstate.md#class_RDSamplerState_property_repeat_v) | `2` |
| [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) | [repeat_w](class_rdsamplerstate.md#class_RDSamplerState_property_repeat_w) | `2` |
| [bool](class_bool.md#class_bool) | [unnormalized_uvw](class_rdsamplerstate.md#class_RDSamplerState_property_unnormalized_uvw) | `false` |
| [bool](class_bool.md#class_bool) | [use_anisotropy](class_rdsamplerstate.md#class_RDSamplerState_property_use_anisotropy) | `false` |

---

### Property Descriptions

<span id="class_RDSamplerState_property_anisotropy_max"></span>

[float](class_float.md#class_float) **anisotropy_max** = `1.0` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_anisotropy_max)

- void **set_anisotropy_max** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_anisotropy_max** ( )

Maximum anisotropy that can be used when sampling. Only effective if [use_anisotropy](class_rdsamplerstate.md#class_RDSamplerState_property_use_anisotropy) is `true`. Higher values result in a sharper sampler at oblique angles, at the cost of performance (due to memory bandwidth). This value may be limited by the graphics hardware in use. Most graphics hardware only supports values up to `16.0`.

If [anisotropy_max](class_rdsamplerstate.md#class_RDSamplerState_property_anisotropy_max) is `1.0`, forcibly disables anisotropy even if [use_anisotropy](class_rdsamplerstate.md#class_RDSamplerState_property_use_anisotropy) is `true`.

---

<span id="class_RDSamplerState_property_border_color"></span>

[SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) **border_color** = `2` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_border_color)

- void **set_border_color** ( value: [SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) )
- [SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) **get_border_color** ( )

The border color that will be returned when sampling outside the sampler's bounds and the [repeat_u](class_rdsamplerstate.md#class_RDSamplerState_property_repeat_u), [repeat_v](class_rdsamplerstate.md#class_RDSamplerState_property_repeat_v) or [repeat_w](class_rdsamplerstate.md#class_RDSamplerState_property_repeat_w) modes have repeating disabled.

---

<span id="class_RDSamplerState_property_compare_op"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **compare_op** = `7` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_compare_op)

- void **set_compare_op** ( value: [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) )
- [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **get_compare_op** ( )

The compare operation to use. Only effective if [enable_compare](class_rdsamplerstate.md#class_RDSamplerState_property_enable_compare) is `true`.

---

<span id="class_RDSamplerState_property_enable_compare"></span>

[bool](class_bool.md#class_bool) **enable_compare** = `false` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_enable_compare)

- void **set_enable_compare** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_compare** ( )

If `true`, returned values will be based on the comparison operation defined in [compare_op](class_rdsamplerstate.md#class_RDSamplerState_property_compare_op). This is a hardware-based approach and is therefore faster than performing this manually in a shader. For example, compare operations are used for shadow map rendering by comparing depth values from a shadow sampler.

---

<span id="class_RDSamplerState_property_lod_bias"></span>

[float](class_float.md#class_float) **lod_bias** = `0.0` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_lod_bias)

- void **set_lod_bias** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_lod_bias** ( )

The mipmap LOD bias to use. Positive values will make the sampler blurrier at a given distance, while negative values will make the sampler sharper at a given distance (at the risk of looking grainy). Recommended values are between `-0.5` and `0.0`. Only effective if the sampler has mipmaps available.

---

<span id="class_RDSamplerState_property_mag_filter"></span>

[SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) **mag_filter** = `0` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_mag_filter)

- void **set_mag_filter** ( value: [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) )
- [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) **get_mag_filter** ( )

The sampler's magnification filter. It is the filtering method used when sampling texels that appear bigger than on-screen pixels.

---

<span id="class_RDSamplerState_property_max_lod"></span>

[float](class_float.md#class_float) **max_lod** = `1e+20` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_max_lod)

- void **set_max_lod** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max_lod** ( )

The maximum mipmap LOD bias to display (lowest resolution). Only effective if the sampler has mipmaps available.

---

<span id="class_RDSamplerState_property_min_filter"></span>

[SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) **min_filter** = `0` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_min_filter)

- void **set_min_filter** ( value: [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) )
- [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) **get_min_filter** ( )

The sampler's minification filter. It is the filtering method used when sampling texels that appear smaller than on-screen pixels.

---

<span id="class_RDSamplerState_property_min_lod"></span>

[float](class_float.md#class_float) **min_lod** = `0.0` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_min_lod)

- void **set_min_lod** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_min_lod** ( )

The minimum mipmap LOD bias to display (highest resolution). Only effective if the sampler has mipmaps available.

---

<span id="class_RDSamplerState_property_mip_filter"></span>

[SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) **mip_filter** = `0` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_mip_filter)

- void **set_mip_filter** ( value: [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) )
- [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) **get_mip_filter** ( )

The filtering method to use for mipmaps.

---

<span id="class_RDSamplerState_property_repeat_u"></span>

[SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **repeat_u** = `2` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_repeat_u)

- void **set_repeat_u** ( value: [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) )
- [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **get_repeat_u** ( )

The repeat mode to use along the U axis of UV coordinates. This affects the returned values if sampling outside the UV bounds.

---

<span id="class_RDSamplerState_property_repeat_v"></span>

[SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **repeat_v** = `2` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_repeat_v)

- void **set_repeat_v** ( value: [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) )
- [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **get_repeat_v** ( )

The repeat mode to use along the V axis of UV coordinates. This affects the returned values if sampling outside the UV bounds.

---

<span id="class_RDSamplerState_property_repeat_w"></span>

[SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **repeat_w** = `2` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_repeat_w)

- void **set_repeat_w** ( value: [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) )
- [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **get_repeat_w** ( )

The repeat mode to use along the W axis of UV coordinates. This affects the returned values if sampling outside the UV bounds. Only effective for 3D samplers.

---

<span id="class_RDSamplerState_property_unnormalized_uvw"></span>

[bool](class_bool.md#class_bool) **unnormalized_uvw** = `false` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_unnormalized_uvw)

- void **set_unnormalized_uvw** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_unnormalized_uvw** ( )

If `true`, the texture will be sampled with coordinates ranging from 0 to the texture's resolution. Otherwise, the coordinates will be normalized and range from 0 to 1.

---

<span id="class_RDSamplerState_property_use_anisotropy"></span>

[bool](class_bool.md#class_bool) **use_anisotropy** = `false` [🔗](class_rdsamplerstate.md#class_RDSamplerState_property_use_anisotropy)

- void **set_use_anisotropy** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_anisotropy** ( )

If `true`, perform anisotropic sampling. See [anisotropy_max](class_rdsamplerstate.md#class_RDSamplerState_property_anisotropy_max).
