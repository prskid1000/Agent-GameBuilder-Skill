<span id="class_GLTFTextureSampler"></span>

## GLTFTextureSampler

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a glTF texture sampler

### Description

Represents a texture sampler as defined by the base glTF spec. Texture samplers in glTF specify how to sample data from the texture's base image, when rendering the texture on an object.

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [int](class_int.md#class_int) | [mag_filter](class_gltftexturesampler.md#class_GLTFTextureSampler_property_mag_filter) | `9729` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [min_filter](class_gltftexturesampler.md#class_GLTFTextureSampler_property_min_filter) | `9987` |
| [int](class_int.md#class_int) | [wrap_s](class_gltftexturesampler.md#class_GLTFTextureSampler_property_wrap_s) | `10497` |
| [int](class_int.md#class_int) | [wrap_t](class_gltftexturesampler.md#class_GLTFTextureSampler_property_wrap_t) | `10497` |

---

### Property Descriptions

<span id="class_GLTFTextureSampler_property_mag_filter"></span>

[int](class_int.md#class_int) **mag_filter** = `9729` [🔗](class_gltftexturesampler.md#class_GLTFTextureSampler_property_mag_filter)

- void **set_mag_filter** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_mag_filter** ( )

Texture's magnification filter, used when texture appears larger on screen than the source image.

---

<span id="class_GLTFTextureSampler_property_min_filter"></span>

[int](class_int.md#class_int) **min_filter** = `9987` [🔗](class_gltftexturesampler.md#class_GLTFTextureSampler_property_min_filter)

- void **set_min_filter** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_min_filter** ( )

Texture's minification filter, used when the texture appears smaller on screen than the source image.

---

<span id="class_GLTFTextureSampler_property_wrap_s"></span>

[int](class_int.md#class_int) **wrap_s** = `10497` [🔗](class_gltftexturesampler.md#class_GLTFTextureSampler_property_wrap_s)

- void **set_wrap_s** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_wrap_s** ( )

Wrapping mode to use for S-axis (horizontal) texture coordinates.

---

<span id="class_GLTFTextureSampler_property_wrap_t"></span>

[int](class_int.md#class_int) **wrap_t** = `10497` [🔗](class_gltftexturesampler.md#class_GLTFTextureSampler_property_wrap_t)

- void **set_wrap_t** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_wrap_t** ( )

Wrapping mode to use for T-axis (vertical) texture coordinates.
