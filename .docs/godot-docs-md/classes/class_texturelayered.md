<span id="class_TextureLayered"></span>

## TextureLayered

**Inherits:** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CompressedTextureLayered](class_compressedtexturelayered.md#class_CompressedTextureLayered), [ImageTextureLayered](class_imagetexturelayered.md#class_ImageTextureLayered), [PlaceholderTextureLayered](class_placeholdertexturelayered.md#class_PlaceholderTextureLayered), [TextureLayeredRD](class_texturelayeredrd.md#class_TextureLayeredRD)

Base class for texture types which contain the data of multiple [Image](class_image.md#class_Image) s. Each image is of the same size and format.

### Description

Base class for [ImageTextureLayered](class_imagetexturelayered.md#class_ImageTextureLayered) and [CompressedTextureLayered](class_compressedtexturelayered.md#class_CompressedTextureLayered). Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also [Texture3D](class_texture3d.md#class_Texture3D).

Data is set on a per-layer basis. For [Texture2DArray](class_texture2darray.md#class_Texture2DArray) s, the layer specifies the array layer.

All images need to have the same width, height and number of mipmap levels.

A **TextureLayered** can be loaded with [ResourceLoader.load()](class_resourceloader.md#class_ResourceLoader_method_load).

Internally, Godot maps these files to their respective counterparts in the target rendering driver (Vulkan, OpenGL3).

### Methods


| [Format](class_image.md#enum_Image_Format) | [_get_format](class_texturelayered.md#class_TextureLayered_private_method__get_format) ( ) | virtual | required | const |
| --- | --- | --- | --- | --- |
| [int](class_int.md#class_int) | [_get_height](class_texturelayered.md#class_TextureLayered_private_method__get_height) ( ) | virtual | required | const |
| [Image](class_image.md#class_Image) | [_get_layer_data](class_texturelayered.md#class_TextureLayered_private_method__get_layer_data) ( layer_index: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_layered_type](class_texturelayered.md#class_TextureLayered_private_method__get_layered_type) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_layers](class_texturelayered.md#class_TextureLayered_private_method__get_layers) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_width](class_texturelayered.md#class_TextureLayered_private_method__get_width) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_mipmaps](class_texturelayered.md#class_TextureLayered_private_method__has_mipmaps) ( ) | virtual | required | const |
| [Format](class_image.md#enum_Image_Format) | [get_format](class_texturelayered.md#class_TextureLayered_method_get_format) ( ) const |
| [int](class_int.md#class_int) | [get_height](class_texturelayered.md#class_TextureLayered_method_get_height) ( ) const |
| [Image](class_image.md#class_Image) | [get_layer_data](class_texturelayered.md#class_TextureLayered_method_get_layer_data) ( layer: [int](class_int.md#class_int) ) const |
| [LayeredType](class_texturelayered.md#enum_TextureLayered_LayeredType) | [get_layered_type](class_texturelayered.md#class_TextureLayered_method_get_layered_type) ( ) const |
| [int](class_int.md#class_int) | [get_layers](class_texturelayered.md#class_TextureLayered_method_get_layers) ( ) const |
| [int](class_int.md#class_int) | [get_width](class_texturelayered.md#class_TextureLayered_method_get_width) ( ) const |
| [bool](class_bool.md#class_bool) | [has_mipmaps](class_texturelayered.md#class_TextureLayered_method_has_mipmaps) ( ) const |

---

### Enumerations

<span id="enum_TextureLayered_LayeredType"></span>

enum **LayeredType**: [🔗](class_texturelayered.md#enum_TextureLayered_LayeredType)

<span id="class_TextureLayered_constant_LAYERED_TYPE_2D_ARRAY"></span>

[LayeredType](class_texturelayered.md#enum_TextureLayered_LayeredType) **LAYERED_TYPE_2D_ARRAY** = `0`

Texture is a generic [Texture2DArray](class_texture2darray.md#class_Texture2DArray).

<span id="class_TextureLayered_constant_LAYERED_TYPE_CUBEMAP"></span>

[LayeredType](class_texturelayered.md#enum_TextureLayered_LayeredType) **LAYERED_TYPE_CUBEMAP** = `1`

Texture is a [Cubemap](class_cubemap.md#class_Cubemap), with each side in its own layer (6 in total).

<span id="class_TextureLayered_constant_LAYERED_TYPE_CUBEMAP_ARRAY"></span>

[LayeredType](class_texturelayered.md#enum_TextureLayered_LayeredType) **LAYERED_TYPE_CUBEMAP_ARRAY** = `2`

Texture is a [CubemapArray](class_cubemaparray.md#class_CubemapArray), with each cubemap being made of 6 layers.

---

### Method Descriptions

<span id="class_TextureLayered_private_method__get_format"></span>

[Format](class_image.md#enum_Image_Format) **_get_format** ( ) *virtual* |required| *const* [🔗](class_texturelayered.md#class_TextureLayered_private_method__get_format)

Called when the **TextureLayered**'s format is queried.

---

<span id="class_TextureLayered_private_method__get_height"></span>

[int](class_int.md#class_int) **_get_height** ( ) *virtual* |required| *const* [🔗](class_texturelayered.md#class_TextureLayered_private_method__get_height)

Called when the **TextureLayered**'s height is queried.

---

<span id="class_TextureLayered_private_method__get_layer_data"></span>

[Image](class_image.md#class_Image) **_get_layer_data** ( layer_index: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_texturelayered.md#class_TextureLayered_private_method__get_layer_data)

Called when the data for a layer in the **TextureLayered** is queried.

---

<span id="class_TextureLayered_private_method__get_layered_type"></span>

[int](class_int.md#class_int) **_get_layered_type** ( ) *virtual* |required| *const* [🔗](class_texturelayered.md#class_TextureLayered_private_method__get_layered_type)

Called when the layers' type in the **TextureLayered** is queried.

---

<span id="class_TextureLayered_private_method__get_layers"></span>

[int](class_int.md#class_int) **_get_layers** ( ) *virtual* |required| *const* [🔗](class_texturelayered.md#class_TextureLayered_private_method__get_layers)

Called when the number of layers in the **TextureLayered** is queried.

---

<span id="class_TextureLayered_private_method__get_width"></span>

[int](class_int.md#class_int) **_get_width** ( ) *virtual* |required| *const* [🔗](class_texturelayered.md#class_TextureLayered_private_method__get_width)

Called when the **TextureLayered**'s width queried.

---

<span id="class_TextureLayered_private_method__has_mipmaps"></span>

[bool](class_bool.md#class_bool) **_has_mipmaps** ( ) *virtual* |required| *const* [🔗](class_texturelayered.md#class_TextureLayered_private_method__has_mipmaps)

Called when the presence of mipmaps in the **TextureLayered** is queried.

---

<span id="class_TextureLayered_method_get_format"></span>

[Format](class_image.md#enum_Image_Format) **get_format** ( ) *const* [🔗](class_texturelayered.md#class_TextureLayered_method_get_format)

Returns the current format being used by this texture.

---

<span id="class_TextureLayered_method_get_height"></span>

[int](class_int.md#class_int) **get_height** ( ) *const* [🔗](class_texturelayered.md#class_TextureLayered_method_get_height)

Returns the height of the texture in pixels. Height is typically represented by the Y axis.

---

<span id="class_TextureLayered_method_get_layer_data"></span>

[Image](class_image.md#class_Image) **get_layer_data** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_texturelayered.md#class_TextureLayered_method_get_layer_data)

Returns an [Image](class_image.md#class_Image) resource with the data from specified `layer`.

---

<span id="class_TextureLayered_method_get_layered_type"></span>

[LayeredType](class_texturelayered.md#enum_TextureLayered_LayeredType) **get_layered_type** ( ) *const* [🔗](class_texturelayered.md#class_TextureLayered_method_get_layered_type)

Returns the **TextureLayered**'s type. The type determines how the data is accessed, with cubemaps having special types.

---

<span id="class_TextureLayered_method_get_layers"></span>

[int](class_int.md#class_int) **get_layers** ( ) *const* [🔗](class_texturelayered.md#class_TextureLayered_method_get_layers)

Returns the number of referenced [Image](class_image.md#class_Image) s.

---

<span id="class_TextureLayered_method_get_width"></span>

[int](class_int.md#class_int) **get_width** ( ) *const* [🔗](class_texturelayered.md#class_TextureLayered_method_get_width)

Returns the width of the texture in pixels. Width is typically represented by the X axis.

---

<span id="class_TextureLayered_method_has_mipmaps"></span>

[bool](class_bool.md#class_bool) **has_mipmaps** ( ) *const* [🔗](class_texturelayered.md#class_TextureLayered_method_has_mipmaps)

Returns `true` if the layers have generated mipmaps.
