<span id="class_PortableCompressedTexture2D"></span>

## PortableCompressedTexture2D

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides a compressed texture for disk and/or VRAM in a way that is portable.

### Description

This class allows storing compressed textures as self contained (not imported) resources.

For 2D usage (compressed on disk, uncompressed on VRAM), the lossy and lossless modes are recommended. For 3D usage (compressed on VRAM) it depends on the target platform.

If you intend to only use desktop, S3TC or BPTC are recommended. For only mobile, ETC2 is recommended.

For portable, self contained 3D textures that work on both desktop and mobile, Basis Universal is recommended (although it has a small quality cost and longer compression time as a tradeoff).

This resource is intended to be created from code.

### Properties


| [bool](class_bool.md#class_bool) | [keep_compressed_buffer](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_property_keep_compressed_buffer) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| [Vector2](class_vector2.md#class_Vector2) | [size_override](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_property_size_override) | `Vector2(0, 0)` |

### Methods


| void | [create_from_image](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_create_from_image) ( image: [Image](class_image.md#class_Image), compression_mode: [CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode), normal_map: [bool](class_bool.md#class_bool) = false, lossy_quality: [float](class_float.md#class_float) = 0.8 ) |
| --- | --- |
| [CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode) | [get_compression_mode](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_get_compression_mode) ( ) const |
| [Format](class_image.md#enum_Image_Format) | [get_format](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_get_format) ( ) const |
| [bool](class_bool.md#class_bool) | [is_keeping_all_compressed_buffers](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_is_keeping_all_compressed_buffers) ( ) static |
| void | [set_basisu_compressor_params](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_set_basisu_compressor_params) ( uastc_level: [int](class_int.md#class_int), rdo_quality_loss: [float](class_float.md#class_float) ) |
| void | [set_keep_all_compressed_buffers](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_set_keep_all_compressed_buffers) ( keep: [bool](class_bool.md#class_bool) ) static |

---

### Enumerations

<span id="enum_PortableCompressedTexture2D_CompressionMode"></span>

enum **CompressionMode**: [🔗](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode)

<span id="class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_LOSSLESS"></span>

[CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode) **COMPRESSION_MODE_LOSSLESS** = `0`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_LOSSY"></span>

[CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode) **COMPRESSION_MODE_LOSSY** = `1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_BASIS_UNIVERSAL"></span>

[CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode) **COMPRESSION_MODE_BASIS_UNIVERSAL** = `2`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_S3TC"></span>

[CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode) **COMPRESSION_MODE_S3TC** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_ETC2"></span>

[CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode) **COMPRESSION_MODE_ETC2** = `4`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_BPTC"></span>

[CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode) **COMPRESSION_MODE_BPTC** = `5`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_PortableCompressedTexture2D_constant_COMPRESSION_MODE_ASTC"></span>

[CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode) **COMPRESSION_MODE_ASTC** = `6`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

### Property Descriptions

<span id="class_PortableCompressedTexture2D_property_keep_compressed_buffer"></span>

[bool](class_bool.md#class_bool) **keep_compressed_buffer** = `false` [🔗](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_property_keep_compressed_buffer)

- void **set_keep_compressed_buffer** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_keeping_compressed_buffer** ( )

If `true`, when running in the editor, this texture will keep the source-compressed data in memory, allowing the data to persist after loading. Otherwise, the source-compressed data is lost after loading and the texture can't be re-saved.

 **Note:** This property must be set before [create_from_image()](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_create_from_image) for this to work.

---

<span id="class_PortableCompressedTexture2D_property_size_override"></span>

[Vector2](class_vector2.md#class_Vector2) **size_override** = `Vector2(0, 0)` [🔗](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_property_size_override)

- void **set_size_override** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_size_override** ( )

Allows overriding the texture's size (for 2D only).

---

### Method Descriptions

<span id="class_PortableCompressedTexture2D_method_create_from_image"></span>

void **create_from_image** ( image: [Image](class_image.md#class_Image), compression_mode: [CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode), normal_map: [bool](class_bool.md#class_bool) = false, lossy_quality: [float](class_float.md#class_float) = 0.8 ) [🔗](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_create_from_image)

Initializes the compressed texture from a base image. The compression mode must be provided.

 `normal_map` is recommended to ensure optimum quality if this image will be used as a normal map.

If lossy compression is requested, the quality setting can optionally be provided. This maps to Lossy WebP compression quality.

---

<span id="class_PortableCompressedTexture2D_method_get_compression_mode"></span>

[CompressionMode](class_portablecompressedtexture2d.md#enum_PortableCompressedTexture2D_CompressionMode) **get_compression_mode** ( ) *const* [🔗](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_get_compression_mode)

Return the compression mode used (valid after initialized).

---

<span id="class_PortableCompressedTexture2D_method_get_format"></span>

[Format](class_image.md#enum_Image_Format) **get_format** ( ) *const* [🔗](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_get_format)

Return the image format used (valid after initialized).

---

<span id="class_PortableCompressedTexture2D_method_is_keeping_all_compressed_buffers"></span>

[bool](class_bool.md#class_bool) **is_keeping_all_compressed_buffers** ( ) *static* [🔗](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_is_keeping_all_compressed_buffers)

Returns `true` if the flag is overridden for all textures of this type.

---

<span id="class_PortableCompressedTexture2D_method_set_basisu_compressor_params"></span>

void **set_basisu_compressor_params** ( uastc_level: [int](class_int.md#class_int), rdo_quality_loss: [float](class_float.md#class_float) ) [🔗](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_set_basisu_compressor_params)

Sets the compressor parameters for Basis Universal compression. See also the settings in [ResourceImporterTexture](class_resourceimportertexture.md#class_ResourceImporterTexture).

 **Note:** This method must be called before [create_from_image()](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_create_from_image) for this to work.

---

<span id="class_PortableCompressedTexture2D_method_set_keep_all_compressed_buffers"></span>

void **set_keep_all_compressed_buffers** ( keep: [bool](class_bool.md#class_bool) ) *static* [🔗](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D_method_set_keep_all_compressed_buffers)

If `keep` is `true`, overrides the flag globally for all textures of this type. This is used primarily by the editor.
