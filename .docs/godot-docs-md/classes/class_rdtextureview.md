<span id="class_RDTextureView"></span>

## RDTextureView

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture view (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) | [format_override](class_rdtextureview.md#class_RDTextureView_property_format_override) | `232` |
| --- | --- | --- |
| [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) | [swizzle_a](class_rdtextureview.md#class_RDTextureView_property_swizzle_a) | `6` |
| [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) | [swizzle_b](class_rdtextureview.md#class_RDTextureView_property_swizzle_b) | `5` |
| [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) | [swizzle_g](class_rdtextureview.md#class_RDTextureView_property_swizzle_g) | `4` |
| [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) | [swizzle_r](class_rdtextureview.md#class_RDTextureView_property_swizzle_r) | `3` |

---

### Property Descriptions

<span id="class_RDTextureView_property_format_override"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **format_override** = `232` [🔗](class_rdtextureview.md#class_RDTextureView_property_format_override)

- void **set_format_override** ( value: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) )
- [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **get_format_override** ( )

Optional override for the data format to return sampled values in. The corresponding [RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat) must have had this added as a shareable format. The default value of [RenderingDevice.DATA_FORMAT_MAX](class_renderingdevice.md#class_RenderingDevice_constant_DATA_FORMAT_MAX) does not override the format.

---

<span id="class_RDTextureView_property_swizzle_a"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **swizzle_a** = `6` [🔗](class_rdtextureview.md#class_RDTextureView_property_swizzle_a)

- void **set_swizzle_a** ( value: [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) )
- [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **get_swizzle_a** ( )

The channel to sample when sampling the alpha channel.

---

<span id="class_RDTextureView_property_swizzle_b"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **swizzle_b** = `5` [🔗](class_rdtextureview.md#class_RDTextureView_property_swizzle_b)

- void **set_swizzle_b** ( value: [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) )
- [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **get_swizzle_b** ( )

The channel to sample when sampling the blue color channel.

---

<span id="class_RDTextureView_property_swizzle_g"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **swizzle_g** = `4` [🔗](class_rdtextureview.md#class_RDTextureView_property_swizzle_g)

- void **set_swizzle_g** ( value: [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) )
- [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **get_swizzle_g** ( )

The channel to sample when sampling the green color channel.

---

<span id="class_RDTextureView_property_swizzle_r"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **swizzle_r** = `3` [🔗](class_rdtextureview.md#class_RDTextureView_property_swizzle_r)

- void **set_swizzle_r** ( value: [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) )
- [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **get_swizzle_r** ( )

The channel to sample when sampling the red color channel.
