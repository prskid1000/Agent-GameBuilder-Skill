<span id="class_RDTextureFormat"></span>

## RDTextureFormat

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture format (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [int](class_int.md#class_int) | [array_layers](class_rdtextureformat.md#class_RDTextureFormat_property_array_layers) | `1` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [depth](class_rdtextureformat.md#class_RDTextureFormat_property_depth) | `1` |
| [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) | [format](class_rdtextureformat.md#class_RDTextureFormat_property_format) | `8` |
| [int](class_int.md#class_int) | [height](class_rdtextureformat.md#class_RDTextureFormat_property_height) | `1` |
| [bool](class_bool.md#class_bool) | [is_discardable](class_rdtextureformat.md#class_RDTextureFormat_property_is_discardable) | `false` |
| [bool](class_bool.md#class_bool) | [is_resolve_buffer](class_rdtextureformat.md#class_RDTextureFormat_property_is_resolve_buffer) | `false` |
| [int](class_int.md#class_int) | [mipmaps](class_rdtextureformat.md#class_RDTextureFormat_property_mipmaps) | `1` |
| [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) | [samples](class_rdtextureformat.md#class_RDTextureFormat_property_samples) | `0` |
| [TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) | [texture_type](class_rdtextureformat.md#class_RDTextureFormat_property_texture_type) | `1` |
| bitfield | \[[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits)\] | [usage_bits](class_rdtextureformat.md#class_RDTextureFormat_property_usage_bits) | `0` |
| [int](class_int.md#class_int) | [width](class_rdtextureformat.md#class_RDTextureFormat_property_width) | `1` |

### Methods


| void | [add_shareable_format](class_rdtextureformat.md#class_RDTextureFormat_method_add_shareable_format) ( format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) ) |
| --- | --- |
| void | [remove_shareable_format](class_rdtextureformat.md#class_RDTextureFormat_method_remove_shareable_format) ( format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) ) |

---

### Property Descriptions

<span id="class_RDTextureFormat_property_array_layers"></span>

[int](class_int.md#class_int) **array_layers** = `1` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_array_layers)

- void **set_array_layers** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_array_layers** ( )

The number of layers in the texture. Only relevant for 2D texture arrays.

---

<span id="class_RDTextureFormat_property_depth"></span>

[int](class_int.md#class_int) **depth** = `1` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_depth)

- void **set_depth** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_depth** ( )

The texture's depth (in pixels). This is always `1` for 2D textures.

---

<span id="class_RDTextureFormat_property_format"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **format** = `8` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_format)

- void **set_format** ( value: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) )
- [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **get_format** ( )

The texture's pixel data format.

---

<span id="class_RDTextureFormat_property_height"></span>

[int](class_int.md#class_int) **height** = `1` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_height)

- void **set_height** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_height** ( )

The texture's height (in pixels).

---

<span id="class_RDTextureFormat_property_is_discardable"></span>

[bool](class_bool.md#class_bool) **is_discardable** = `false` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_is_discardable)

- void **set_is_discardable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_is_discardable** ( )

If a texture is discardable, its contents do not need to be preserved between frames. This flag is only relevant when the texture is used as target in a draw list.

This information is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) to figure out if a texture's contents can be discarded, eliminating unnecessary writes to memory and boosting performance.

---

<span id="class_RDTextureFormat_property_is_resolve_buffer"></span>

[bool](class_bool.md#class_bool) **is_resolve_buffer** = `false` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_is_resolve_buffer)

- void **set_is_resolve_buffer** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_is_resolve_buffer** ( )

The texture will be used as the destination of a resolve operation.

---

<span id="class_RDTextureFormat_property_mipmaps"></span>

[int](class_int.md#class_int) **mipmaps** = `1` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_mipmaps)

- void **set_mipmaps** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_mipmaps** ( )

The number of mipmaps available in the texture.

---

<span id="class_RDTextureFormat_property_samples"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **samples** = `0` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_samples)

- void **set_samples** ( value: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) )
- [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **get_samples** ( )

The number of samples used when sampling the texture.

---

<span id="class_RDTextureFormat_property_texture_type"></span>

[TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **texture_type** = `1` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_texture_type)

- void **set_texture_type** ( value: [TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) )
- [TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **get_texture_type** ( )

The texture type.

---

<span id="class_RDTextureFormat_property_usage_bits"></span>

*BitField*\[[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits)\] **usage_bits** = `0` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_usage_bits)

- void **set_usage_bits** ( value: *BitField*\[[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits)\] )
- *BitField*\[[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits)\] **get_usage_bits** ( )

The texture's usage bits, which determine what can be done using the texture.

---

<span id="class_RDTextureFormat_property_width"></span>

[int](class_int.md#class_int) **width** = `1` [🔗](class_rdtextureformat.md#class_RDTextureFormat_property_width)

- void **set_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_width** ( )

The texture's width (in pixels).

---

### Method Descriptions

<span id="class_RDTextureFormat_method_add_shareable_format"></span>

void **add_shareable_format** ( format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) ) [🔗](class_rdtextureformat.md#class_RDTextureFormat_method_add_shareable_format)

Adds `format` as a valid format for the corresponding [RDTextureView](class_rdtextureview.md#class_RDTextureView)'s [RDTextureView.format_override](class_rdtextureview.md#class_RDTextureView_property_format_override) property. If any format is added as shareable, then the main [format](class_rdtextureformat.md#class_RDTextureFormat_property_format) must also be added.

---

<span id="class_RDTextureFormat_method_remove_shareable_format"></span>

void **remove_shareable_format** ( format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) ) [🔗](class_rdtextureformat.md#class_RDTextureFormat_method_remove_shareable_format)

Removes `format` from the list of valid formats that the corresponding [RDTextureView](class_rdtextureview.md#class_RDTextureView)'s [RDTextureView.format_override](class_rdtextureview.md#class_RDTextureView_property_format_override) property can be set to.
