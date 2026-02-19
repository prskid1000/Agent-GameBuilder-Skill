<span id="class_Image"></span>

## Image

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Image datatype.

### Description

Native image datatype. Contains image data which can be converted to an [ImageTexture](class_imagetexture.md#class_ImageTexture) and provides commonly used *image processing* methods. The maximum width and height for an **Image** are [MAX_WIDTH](class_image.md#class_Image_constant_MAX_WIDTH) and [MAX_HEIGHT](class_image.md#class_Image_constant_MAX_HEIGHT).

An **Image** cannot be assigned to a texture property of an object directly (such as [Sprite2D.texture](class_sprite2d.md#class_Sprite2D_property_texture)), and has to be converted manually to an [ImageTexture](class_imagetexture.md#class_ImageTexture) first.

 **Note:** Methods that modify the image data cannot be used on VRAM-compressed images. Use [decompress()](class_image.md#class_Image_method_decompress) to convert the image to an uncompressed format first.

 **Note:** The maximum image size is 16384×16384 pixels due to graphics hardware limitations. Larger images may fail to import.

### Tutorials

- [Importing images](../tutorials/assets_pipeline/importing_images.md)

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [Dictionary](class_dictionary.md#class_Dictionary) | [data](class_image.md#class_Image_property_data) | `{ "data": PackedByteArray(), "format": "Lum8", "height": 0, "mipmaps": false, "width": 0 }` |
| --- | --- | --- |

### Methods


| void | [adjust_bcs](class_image.md#class_Image_method_adjust_bcs) ( brightness: [float](class_float.md#class_float), contrast: [float](class_float.md#class_float), saturation: [float](class_float.md#class_float) ) |
| --- | --- |
| void | [blend_rect](class_image.md#class_Image_method_blend_rect) ( src: [Image](class_image.md#class_Image), src_rect: [Rect2i](class_rect2i.md#class_Rect2i), dst: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [blend_rect_mask](class_image.md#class_Image_method_blend_rect_mask) ( src: [Image](class_image.md#class_Image), mask: [Image](class_image.md#class_Image), src_rect: [Rect2i](class_rect2i.md#class_Rect2i), dst: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [blit_rect](class_image.md#class_Image_method_blit_rect) ( src: [Image](class_image.md#class_Image), src_rect: [Rect2i](class_rect2i.md#class_Rect2i), dst: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [blit_rect_mask](class_image.md#class_Image_method_blit_rect_mask) ( src: [Image](class_image.md#class_Image), mask: [Image](class_image.md#class_Image), src_rect: [Rect2i](class_rect2i.md#class_Rect2i), dst: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [bump_map_to_normal_map](class_image.md#class_Image_method_bump_map_to_normal_map) ( bump_scale: [float](class_float.md#class_float) = 1.0 ) |
| void | [clear_mipmaps](class_image.md#class_Image_method_clear_mipmaps) ( ) |
| Error | [compress](class_image.md#class_Image_method_compress) ( mode: [CompressMode](class_image.md#enum_Image_CompressMode), source: [CompressSource](class_image.md#enum_Image_CompressSource) = 0, astc_format: [ASTCFormat](class_image.md#enum_Image_ASTCFormat) = 0 ) |
| Error | [compress_from_channels](class_image.md#class_Image_method_compress_from_channels) ( mode: [CompressMode](class_image.md#enum_Image_CompressMode), channels: [UsedChannels](class_image.md#enum_Image_UsedChannels), astc_format: [ASTCFormat](class_image.md#enum_Image_ASTCFormat) = 0 ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [compute_image_metrics](class_image.md#class_Image_method_compute_image_metrics) ( compared_image: [Image](class_image.md#class_Image), use_luma: [bool](class_bool.md#class_bool) ) |
| void | [convert](class_image.md#class_Image_method_convert) ( format: [Format](class_image.md#enum_Image_Format) ) |
| void | [copy_from](class_image.md#class_Image_method_copy_from) ( src: [Image](class_image.md#class_Image) ) |
| [Image](class_image.md#class_Image) | [create](class_image.md#class_Image_method_create) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), format: [Format](class_image.md#enum_Image_Format) ) static |
| [Image](class_image.md#class_Image) | [create_empty](class_image.md#class_Image_method_create_empty) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), format: [Format](class_image.md#enum_Image_Format) ) static |
| [Image](class_image.md#class_Image) | [create_from_data](class_image.md#class_Image_method_create_from_data) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), format: [Format](class_image.md#enum_Image_Format), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) static |
| void | [crop](class_image.md#class_Image_method_crop) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) |
| Error | [decompress](class_image.md#class_Image_method_decompress) ( ) |
| [AlphaMode](class_image.md#enum_Image_AlphaMode) | [detect_alpha](class_image.md#class_Image_method_detect_alpha) ( ) const |
| [UsedChannels](class_image.md#enum_Image_UsedChannels) | [detect_used_channels](class_image.md#class_Image_method_detect_used_channels) ( source: [CompressSource](class_image.md#enum_Image_CompressSource) = 0 ) const |
| void | [fill](class_image.md#class_Image_method_fill) ( color: [Color](class_color.md#class_Color) ) |
| void | [fill_rect](class_image.md#class_Image_method_fill_rect) ( rect: [Rect2i](class_rect2i.md#class_Rect2i), color: [Color](class_color.md#class_Color) ) |
| void | [fix_alpha_edges](class_image.md#class_Image_method_fix_alpha_edges) ( ) |
| void | [flip_x](class_image.md#class_Image_method_flip_x) ( ) |
| void | [flip_y](class_image.md#class_Image_method_flip_y) ( ) |
| Error | [generate_mipmaps](class_image.md#class_Image_method_generate_mipmaps) ( renormalize: [bool](class_bool.md#class_bool) = false ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [get_data](class_image.md#class_Image_method_get_data) ( ) const |
| [int](class_int.md#class_int) | [get_data_size](class_image.md#class_Image_method_get_data_size) ( ) const |
| [Format](class_image.md#enum_Image_Format) | [get_format](class_image.md#class_Image_method_get_format) ( ) const |
| [int](class_int.md#class_int) | [get_height](class_image.md#class_Image_method_get_height) ( ) const |
| [int](class_int.md#class_int) | [get_mipmap_count](class_image.md#class_Image_method_get_mipmap_count) ( ) const |
| [int](class_int.md#class_int) | [get_mipmap_offset](class_image.md#class_Image_method_get_mipmap_offset) ( mipmap: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_pixel](class_image.md#class_Image_method_get_pixel) ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_pixelv](class_image.md#class_Image_method_get_pixelv) ( point: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Image](class_image.md#class_Image) | [get_region](class_image.md#class_Image_method_get_region) ( region: [Rect2i](class_rect2i.md#class_Rect2i) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_size](class_image.md#class_Image_method_get_size) ( ) const |
| [Rect2i](class_rect2i.md#class_Rect2i) | [get_used_rect](class_image.md#class_Image_method_get_used_rect) ( ) const |
| [int](class_int.md#class_int) | [get_width](class_image.md#class_Image_method_get_width) ( ) const |
| [bool](class_bool.md#class_bool) | [has_mipmaps](class_image.md#class_Image_method_has_mipmaps) ( ) const |
| [bool](class_bool.md#class_bool) | [is_compressed](class_image.md#class_Image_method_is_compressed) ( ) const |
| [bool](class_bool.md#class_bool) | [is_empty](class_image.md#class_Image_method_is_empty) ( ) const |
| [bool](class_bool.md#class_bool) | [is_invisible](class_image.md#class_Image_method_is_invisible) ( ) const |
| void | [linear_to_srgb](class_image.md#class_Image_method_linear_to_srgb) ( ) |
| Error | [load](class_image.md#class_Image_method_load) ( path: [String](class_string.md#class_String) ) |
| Error | [load_bmp_from_buffer](class_image.md#class_Image_method_load_bmp_from_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| Error | [load_dds_from_buffer](class_image.md#class_Image_method_load_dds_from_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| Error | [load_exr_from_buffer](class_image.md#class_Image_method_load_exr_from_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [Image](class_image.md#class_Image) | [load_from_file](class_image.md#class_Image_method_load_from_file) ( path: [String](class_string.md#class_String) ) static |
| Error | [load_jpg_from_buffer](class_image.md#class_Image_method_load_jpg_from_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| Error | [load_ktx_from_buffer](class_image.md#class_Image_method_load_ktx_from_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| Error | [load_png_from_buffer](class_image.md#class_Image_method_load_png_from_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| Error | [load_svg_from_buffer](class_image.md#class_Image_method_load_svg_from_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), scale: [float](class_float.md#class_float) = 1.0 ) |
| Error | [load_svg_from_string](class_image.md#class_Image_method_load_svg_from_string) ( svg_str: [String](class_string.md#class_String), scale: [float](class_float.md#class_float) = 1.0 ) |
| Error | [load_tga_from_buffer](class_image.md#class_Image_method_load_tga_from_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| Error | [load_webp_from_buffer](class_image.md#class_Image_method_load_webp_from_buffer) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [normal_map_to_xy](class_image.md#class_Image_method_normal_map_to_xy) ( ) |
| void | [premultiply_alpha](class_image.md#class_Image_method_premultiply_alpha) ( ) |
| void | [resize](class_image.md#class_Image_method_resize) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), interpolation: [Interpolation](class_image.md#enum_Image_Interpolation) = 1 ) |
| void | [resize_to_po2](class_image.md#class_Image_method_resize_to_po2) ( square: [bool](class_bool.md#class_bool) = false, interpolation: [Interpolation](class_image.md#enum_Image_Interpolation) = 1 ) |
| [Image](class_image.md#class_Image) | [rgbe_to_srgb](class_image.md#class_Image_method_rgbe_to_srgb) ( ) |
| void | [rotate_90](class_image.md#class_Image_method_rotate_90) ( direction: ClockDirection ) |
| void | [rotate_180](class_image.md#class_Image_method_rotate_180) ( ) |
| Error | [save_dds](class_image.md#class_Image_method_save_dds) ( path: [String](class_string.md#class_String) ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [save_dds_to_buffer](class_image.md#class_Image_method_save_dds_to_buffer) ( ) const |
| Error | [save_exr](class_image.md#class_Image_method_save_exr) ( path: [String](class_string.md#class_String), grayscale: [bool](class_bool.md#class_bool) = false ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [save_exr_to_buffer](class_image.md#class_Image_method_save_exr_to_buffer) ( grayscale: [bool](class_bool.md#class_bool) = false ) const |
| Error | [save_jpg](class_image.md#class_Image_method_save_jpg) ( path: [String](class_string.md#class_String), quality: [float](class_float.md#class_float) = 0.75 ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [save_jpg_to_buffer](class_image.md#class_Image_method_save_jpg_to_buffer) ( quality: [float](class_float.md#class_float) = 0.75 ) const |
| Error | [save_png](class_image.md#class_Image_method_save_png) ( path: [String](class_string.md#class_String) ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [save_png_to_buffer](class_image.md#class_Image_method_save_png_to_buffer) ( ) const |
| Error | [save_webp](class_image.md#class_Image_method_save_webp) ( path: [String](class_string.md#class_String), lossy: [bool](class_bool.md#class_bool) = false, quality: [float](class_float.md#class_float) = 0.75 ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [save_webp_to_buffer](class_image.md#class_Image_method_save_webp_to_buffer) ( lossy: [bool](class_bool.md#class_bool) = false, quality: [float](class_float.md#class_float) = 0.75 ) const |
| void | [set_data](class_image.md#class_Image_method_set_data) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), format: [Format](class_image.md#enum_Image_Format), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [set_pixel](class_image.md#class_Image_method_set_pixel) ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_pixelv](class_image.md#class_Image_method_set_pixelv) ( point: [Vector2i](class_vector2i.md#class_Vector2i), color: [Color](class_color.md#class_Color) ) |
| void | [shrink_x2](class_image.md#class_Image_method_shrink_x2) ( ) |
| void | [srgb_to_linear](class_image.md#class_Image_method_srgb_to_linear) ( ) |

---

### Enumerations

<span id="enum_Image_Format"></span>

enum **Format**: [🔗](class_image.md#enum_Image_Format)

<span id="class_Image_constant_FORMAT_L8"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_L8** = `0`

Texture format with a single 8-bit depth representing luminance.

<span id="class_Image_constant_FORMAT_LA8"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_LA8** = `1`

OpenGL texture format with two values, luminance and alpha each stored with 8 bits.

<span id="class_Image_constant_FORMAT_R8"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_R8** = `2`

OpenGL texture format `RED` with a single component and a bitdepth of 8.

<span id="class_Image_constant_FORMAT_RG8"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RG8** = `3`

OpenGL texture format `RG` with two components and a bitdepth of 8 for each.

<span id="class_Image_constant_FORMAT_RGB8"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGB8** = `4`

OpenGL texture format `RGB` with three components, each with a bitdepth of 8.

 **Note:** When creating an [ImageTexture](class_imagetexture.md#class_ImageTexture), a nonlinear sRGB to linear encoding conversion is performed.

<span id="class_Image_constant_FORMAT_RGBA8"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGBA8** = `5`

OpenGL texture format `RGBA` with four components, each with a bitdepth of 8.

 **Note:** When creating an [ImageTexture](class_imagetexture.md#class_ImageTexture), a nonlinear sRGB to linear encoding conversion is performed.

<span id="class_Image_constant_FORMAT_RGBA4444"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGBA4444** = `6`

OpenGL texture format `RGBA` with four components, each with a bitdepth of 4.

<span id="class_Image_constant_FORMAT_RGB565"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGB565** = `7`

OpenGL texture format `RGB` with three components. Red and blue have a bitdepth of 5, and green has a bitdepth of 6.

<span id="class_Image_constant_FORMAT_RF"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RF** = `8`

OpenGL texture format `GL_R32F` where there's one component, a 32-bit floating-point value.

<span id="class_Image_constant_FORMAT_RGF"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGF** = `9`

OpenGL texture format `GL_RG32F` where there are two components, each a 32-bit floating-point values.

<span id="class_Image_constant_FORMAT_RGBF"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGBF** = `10`

OpenGL texture format `GL_RGB32F` where there are three components, each a 32-bit floating-point values.

<span id="class_Image_constant_FORMAT_RGBAF"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGBAF** = `11`

OpenGL texture format `GL_RGBA32F` where there are four components, each a 32-bit floating-point values.

<span id="class_Image_constant_FORMAT_RH"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RH** = `12`

OpenGL texture format `GL_R16F` where there's one component, a 16-bit "half-precision" floating-point value.

<span id="class_Image_constant_FORMAT_RGH"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGH** = `13`

OpenGL texture format `GL_RG16F` where there are two components, each a 16-bit "half-precision" floating-point value.

<span id="class_Image_constant_FORMAT_RGBH"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGBH** = `14`

OpenGL texture format `GL_RGB16F` where there are three components, each a 16-bit "half-precision" floating-point value.

<span id="class_Image_constant_FORMAT_RGBAH"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGBAH** = `15`

OpenGL texture format `GL_RGBA16F` where there are four components, each a 16-bit "half-precision" floating-point value.

<span id="class_Image_constant_FORMAT_RGBE9995"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGBE9995** = `16`

A special OpenGL texture format where the three color components have 9 bits of precision and all three share a single 5-bit exponent.

<span id="class_Image_constant_FORMAT_DXT1"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_DXT1** = `17`

The S3TC texture format that uses Block Compression 1, and is the smallest variation of S3TC, only providing 1 bit of alpha and color data being premultiplied with alpha.

 **Note:** When creating an [ImageTexture](class_imagetexture.md#class_ImageTexture), a nonlinear sRGB to linear encoding conversion is performed.

<span id="class_Image_constant_FORMAT_DXT3"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_DXT3** = `18`

The S3TC texture format that uses Block Compression 2, and color data is interpreted as not having been premultiplied by alpha. Well suited for images with sharp alpha transitions between translucent and opaque areas.

 **Note:** When creating an [ImageTexture](class_imagetexture.md#class_ImageTexture), a nonlinear sRGB to linear encoding conversion is performed.

<span id="class_Image_constant_FORMAT_DXT5"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_DXT5** = `19`

The S3TC texture format also known as Block Compression 3 or BC3 that contains 64 bits of alpha channel data followed by 64 bits of DXT1-encoded color data. Color data is not premultiplied by alpha, same as DXT3. DXT5 generally produces superior results for transparent gradients compared to DXT3.

 **Note:** When creating an [ImageTexture](class_imagetexture.md#class_ImageTexture), a nonlinear sRGB to linear encoding conversion is performed.

<span id="class_Image_constant_FORMAT_RGTC_R"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGTC_R** = `20`

Texture format that uses Red Green Texture Compression, normalizing the red channel data using the same compression algorithm that DXT5 uses for the alpha channel.

<span id="class_Image_constant_FORMAT_RGTC_RG"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGTC_RG** = `21`

Texture format that uses Red Green Texture Compression, normalizing the red and green channel data using the same compression algorithm that DXT5 uses for the alpha channel.

<span id="class_Image_constant_FORMAT_BPTC_RGBA"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_BPTC_RGBA** = `22`

Texture format that uses BPTC compression with unsigned normalized RGBA components.

 **Note:** When creating an [ImageTexture](class_imagetexture.md#class_ImageTexture), a nonlinear sRGB to linear encoding conversion is performed.

<span id="class_Image_constant_FORMAT_BPTC_RGBF"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_BPTC_RGBF** = `23`

Texture format that uses BPTC compression with signed floating-point RGB components.

<span id="class_Image_constant_FORMAT_BPTC_RGBFU"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_BPTC_RGBFU** = `24`

Texture format that uses BPTC compression with unsigned floating-point RGB components.

<span id="class_Image_constant_FORMAT_ETC"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ETC** = `25`

Ericsson Texture Compression format 1, also referred to as "ETC1", and is part of the OpenGL ES graphics standard. This format cannot store an alpha channel.

<span id="class_Image_constant_FORMAT_ETC2_R11"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ETC2_R11** = `26`

Ericsson Texture Compression format 2 (`R11_EAC` variant), which provides one channel of unsigned data.

<span id="class_Image_constant_FORMAT_ETC2_R11S"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ETC2_R11S** = `27`

Ericsson Texture Compression format 2 (`SIGNED_R11_EAC` variant), which provides one channel of signed data.

<span id="class_Image_constant_FORMAT_ETC2_RG11"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ETC2_RG11** = `28`

Ericsson Texture Compression format 2 (`RG11_EAC` variant), which provides two channels of unsigned data.

<span id="class_Image_constant_FORMAT_ETC2_RG11S"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ETC2_RG11S** = `29`

Ericsson Texture Compression format 2 (`SIGNED_RG11_EAC` variant), which provides two channels of signed data.

<span id="class_Image_constant_FORMAT_ETC2_RGB8"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ETC2_RGB8** = `30`

Ericsson Texture Compression format 2 (`RGB8` variant), which is a follow-up of ETC1 and compresses RGB888 data.

 **Note:** When creating an [ImageTexture](class_imagetexture.md#class_ImageTexture), a nonlinear sRGB to linear encoding conversion is performed.

<span id="class_Image_constant_FORMAT_ETC2_RGBA8"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ETC2_RGBA8** = `31`

Ericsson Texture Compression format 2 (`RGBA8` variant), which compresses RGBA8888 data with full alpha support.

 **Note:** When creating an [ImageTexture](class_imagetexture.md#class_ImageTexture), a nonlinear sRGB to linear encoding conversion is performed.

<span id="class_Image_constant_FORMAT_ETC2_RGB8A1"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ETC2_RGB8A1** = `32`

Ericsson Texture Compression format 2 (`RGB8_PUNCHTHROUGH_ALPHA1` variant), which compresses RGBA data to make alpha either fully transparent or fully opaque.

 **Note:** When creating an [ImageTexture](class_imagetexture.md#class_ImageTexture), a nonlinear sRGB to linear encoding conversion is performed.

<span id="class_Image_constant_FORMAT_ETC2_RA_AS_RG"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ETC2_RA_AS_RG** = `33`

Ericsson Texture Compression format 2 (`RGBA8` variant), which compresses RA data and interprets it as two channels (red and green). See also [FORMAT_ETC2_RGBA8](class_image.md#class_Image_constant_FORMAT_ETC2_RGBA8).

<span id="class_Image_constant_FORMAT_DXT5_RA_AS_RG"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_DXT5_RA_AS_RG** = `34`

The S3TC texture format also known as Block Compression 3 or BC3, which compresses RA data and interprets it as two channels (red and green). See also [FORMAT_DXT5](class_image.md#class_Image_constant_FORMAT_DXT5).

<span id="class_Image_constant_FORMAT_ASTC_4x4"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ASTC_4x4** = `35`

Adaptive Scalable Texture Compression. This implements the 4×4 (high quality) mode.

<span id="class_Image_constant_FORMAT_ASTC_4x4_HDR"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ASTC_4x4_HDR** = `36`

Same format as [FORMAT_ASTC_4x4](class_image.md#class_Image_constant_FORMAT_ASTC_4x4), but with the hint to let the GPU know it is used for HDR.

<span id="class_Image_constant_FORMAT_ASTC_8x8"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ASTC_8x8** = `37`

Adaptive Scalable Texture Compression. This implements the 8×8 (low quality) mode.

<span id="class_Image_constant_FORMAT_ASTC_8x8_HDR"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_ASTC_8x8_HDR** = `38`

Same format as [FORMAT_ASTC_8x8](class_image.md#class_Image_constant_FORMAT_ASTC_8x8), but with the hint to let the GPU know it is used for HDR.

<span id="class_Image_constant_FORMAT_R16"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_R16** = `39`

OpenGL texture format `GL_R16` where there's one component, a 16-bit unsigned normalized integer value. Since the value is normalized, each component is clamped between `0.0` and `1.0` (inclusive).

 **Note:** Due to limited hardware support, it is mainly recommended to be used on desktop or console devices. It may be unsupported on mobile or web, and will consequently be converted to [FORMAT_RF](class_image.md#class_Image_constant_FORMAT_RF).

<span id="class_Image_constant_FORMAT_RG16"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RG16** = `40`

OpenGL texture format `GL_RG16` where there are two components, each a 16-bit unsigned normalized integer value. Since the value is normalized, each component is clamped between `0.0` and `1.0` (inclusive).

 **Note:** Due to limited hardware support, it is mainly recommended to be used on desktop or console devices. It may be unsupported on mobile or web, and will consequently be converted to [FORMAT_RGF](class_image.md#class_Image_constant_FORMAT_RGF).

<span id="class_Image_constant_FORMAT_RGB16"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGB16** = `41`

OpenGL texture format `GL_RGB16` where there are three components, each a 16-bit unsigned normalized integer value. Since the value is normalized, each component is clamped between `0.0` and `1.0` (inclusive).

 **Note:** Due to limited hardware support, it is mainly recommended to be used on desktop or console devices. It may be unsupported on mobile or web, and will consequently be converted to [FORMAT_RGBF](class_image.md#class_Image_constant_FORMAT_RGBF).

<span id="class_Image_constant_FORMAT_RGBA16"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGBA16** = `42`

OpenGL texture format `GL_RGBA16` where there are four components, each a 16-bit unsigned normalized integer value. Since the value is normalized, each component is clamped between `0.0` and `1.0` (inclusive).

 **Note:** Due to limited hardware support, it is mainly recommended to be used on desktop or console devices. It may be unsupported on mobile or web, and will consequently be converted to [FORMAT_RGBAF](class_image.md#class_Image_constant_FORMAT_RGBAF).

<span id="class_Image_constant_FORMAT_R16I"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_R16I** = `43`

OpenGL texture format `GL_R16UI` where there's one component, a 16-bit unsigned integer value. Each component is clamped between `0` and `65535` (inclusive).

 **Note:** When used in a shader, the texture requires usage of `usampler` samplers. Additionally, it only supports nearest-neighbor filtering under the Compatibility renderer.

 **Note:** When sampling using [get_pixel()](class_image.md#class_Image_method_get_pixel), returned [Color](class_color.md#class_Color) s have to be divided by `65535` to get the correct color value.

<span id="class_Image_constant_FORMAT_RG16I"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RG16I** = `44`

OpenGL texture format `GL_RG16UI` where there are two components, each a 16-bit unsigned integer value. Each component is clamped between `0` and `65535` (inclusive).

 **Note:** When used in a shader, the texture requires usage of `usampler` samplers. Additionally, it only supports nearest-neighbor filtering under the Compatibility renderer.

 **Note:** When sampling using [get_pixel()](class_image.md#class_Image_method_get_pixel), returned [Color](class_color.md#class_Color) s have to be divided by `65535` to get the correct color value.

<span id="class_Image_constant_FORMAT_RGB16I"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGB16I** = `45`

OpenGL texture format `GL_RGB16UI` where there are three components, each a 16-bit unsigned integer value. Each component is clamped between `0` and `65535` (inclusive).

 **Note:** When used in a shader, the texture requires usage of `usampler` samplers. Additionally, it only supports nearest-neighbor filtering under the Compatibility renderer.

 **Note:** When sampling using [get_pixel()](class_image.md#class_Image_method_get_pixel), returned [Color](class_color.md#class_Color) s have to be divided by `65535` to get the correct color value.

<span id="class_Image_constant_FORMAT_RGBA16I"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_RGBA16I** = `46`

OpenGL texture format `GL_RGBA16UI` where there are four components, each a 16-bit unsigned integer value. Each component is clamped between `0` and `65535` (inclusive).

 **Note:** When used in a shader, the texture requires usage of `usampler` samplers. Additionally, it only supports nearest-neighbor filtering under the Compatibility renderer.

 **Note:** When sampling using [get_pixel()](class_image.md#class_Image_method_get_pixel), returned [Color](class_color.md#class_Color) s have to be divided by `65535` to get the correct color value.

<span id="class_Image_constant_FORMAT_MAX"></span>

[Format](class_image.md#enum_Image_Format) **FORMAT_MAX** = `47`

Represents the size of the [Format](class_image.md#enum_Image_Format) enum.

---

<span id="enum_Image_Interpolation"></span>

enum **Interpolation**: [🔗](class_image.md#enum_Image_Interpolation)

<span id="class_Image_constant_INTERPOLATE_NEAREST"></span>

[Interpolation](class_image.md#enum_Image_Interpolation) **INTERPOLATE_NEAREST** = `0`

Performs nearest-neighbor interpolation. If the image is resized, it will be pixelated.

<span id="class_Image_constant_INTERPOLATE_BILINEAR"></span>

[Interpolation](class_image.md#enum_Image_Interpolation) **INTERPOLATE_BILINEAR** = `1`

Performs bilinear interpolation. If the image is resized, it will be blurry. This mode is faster than [INTERPOLATE_CUBIC](class_image.md#class_Image_constant_INTERPOLATE_CUBIC), but it results in lower quality.

<span id="class_Image_constant_INTERPOLATE_CUBIC"></span>

[Interpolation](class_image.md#enum_Image_Interpolation) **INTERPOLATE_CUBIC** = `2`

Performs cubic interpolation. If the image is resized, it will be blurry. This mode often gives better results compared to [INTERPOLATE_BILINEAR](class_image.md#class_Image_constant_INTERPOLATE_BILINEAR), at the cost of being slower.

<span id="class_Image_constant_INTERPOLATE_TRILINEAR"></span>

[Interpolation](class_image.md#enum_Image_Interpolation) **INTERPOLATE_TRILINEAR** = `3`

Performs bilinear separately on the two most-suited mipmap levels, then linearly interpolates between them.

It's slower than [INTERPOLATE_BILINEAR](class_image.md#class_Image_constant_INTERPOLATE_BILINEAR), but produces higher-quality results with far fewer aliasing artifacts.

If the image does not have mipmaps, they will be generated and used internally, but no mipmaps will be generated on the resulting image.

 **Note:** If you intend to scale multiple copies of the original image, it's better to call [generate_mipmaps()](class_image.md#class_Image_method_generate_mipmaps)] on it in advance, to avoid wasting processing power in generating them again and again.

On the other hand, if the image already has mipmaps, they will be used, and a new set will be generated for the resulting image.

<span id="class_Image_constant_INTERPOLATE_LANCZOS"></span>

[Interpolation](class_image.md#enum_Image_Interpolation) **INTERPOLATE_LANCZOS** = `4`

Performs Lanczos interpolation. This is the slowest image resizing mode, but it typically gives the best results, especially when downscaling images.

---

<span id="enum_Image_AlphaMode"></span>

enum **AlphaMode**: [🔗](class_image.md#enum_Image_AlphaMode)

<span id="class_Image_constant_ALPHA_NONE"></span>

[AlphaMode](class_image.md#enum_Image_AlphaMode) **ALPHA_NONE** = `0`

Image is fully opaque. It does not store alpha data.

<span id="class_Image_constant_ALPHA_BIT"></span>

[AlphaMode](class_image.md#enum_Image_AlphaMode) **ALPHA_BIT** = `1`

Image stores either fully opaque or fully transparent pixels. Also known as punchthrough alpha.

<span id="class_Image_constant_ALPHA_BLEND"></span>

[AlphaMode](class_image.md#enum_Image_AlphaMode) **ALPHA_BLEND** = `2`

Image stores alpha data with values varying between `0.0` and `1.0`.

---

<span id="enum_Image_CompressMode"></span>

enum **CompressMode**: [🔗](class_image.md#enum_Image_CompressMode)

<span id="class_Image_constant_COMPRESS_S3TC"></span>

[CompressMode](class_image.md#enum_Image_CompressMode) **COMPRESS_S3TC** = `0`

Use S3TC compression.

<span id="class_Image_constant_COMPRESS_ETC"></span>

[CompressMode](class_image.md#enum_Image_CompressMode) **COMPRESS_ETC** = `1`

Use ETC compression.

<span id="class_Image_constant_COMPRESS_ETC2"></span>

[CompressMode](class_image.md#enum_Image_CompressMode) **COMPRESS_ETC2** = `2`

Use ETC2 compression.

<span id="class_Image_constant_COMPRESS_BPTC"></span>

[CompressMode](class_image.md#enum_Image_CompressMode) **COMPRESS_BPTC** = `3`

Use BPTC compression.

<span id="class_Image_constant_COMPRESS_ASTC"></span>

[CompressMode](class_image.md#enum_Image_CompressMode) **COMPRESS_ASTC** = `4`

Use ASTC compression.

<span id="class_Image_constant_COMPRESS_MAX"></span>

[CompressMode](class_image.md#enum_Image_CompressMode) **COMPRESS_MAX** = `5`

Represents the size of the [CompressMode](class_image.md#enum_Image_CompressMode) enum.

---

<span id="enum_Image_UsedChannels"></span>

enum **UsedChannels**: [🔗](class_image.md#enum_Image_UsedChannels)

<span id="class_Image_constant_USED_CHANNELS_L"></span>

[UsedChannels](class_image.md#enum_Image_UsedChannels) **USED_CHANNELS_L** = `0`

The image only uses one channel for luminance (grayscale).

<span id="class_Image_constant_USED_CHANNELS_LA"></span>

[UsedChannels](class_image.md#enum_Image_UsedChannels) **USED_CHANNELS_LA** = `1`

The image uses two channels for luminance and alpha, respectively.

<span id="class_Image_constant_USED_CHANNELS_R"></span>

[UsedChannels](class_image.md#enum_Image_UsedChannels) **USED_CHANNELS_R** = `2`

The image only uses the red channel.

<span id="class_Image_constant_USED_CHANNELS_RG"></span>

[UsedChannels](class_image.md#enum_Image_UsedChannels) **USED_CHANNELS_RG** = `3`

The image uses two channels for red and green.

<span id="class_Image_constant_USED_CHANNELS_RGB"></span>

[UsedChannels](class_image.md#enum_Image_UsedChannels) **USED_CHANNELS_RGB** = `4`

The image uses three channels for red, green, and blue.

<span id="class_Image_constant_USED_CHANNELS_RGBA"></span>

[UsedChannels](class_image.md#enum_Image_UsedChannels) **USED_CHANNELS_RGBA** = `5`

The image uses four channels for red, green, blue, and alpha.

---

<span id="enum_Image_CompressSource"></span>

enum **CompressSource**: [🔗](class_image.md#enum_Image_CompressSource)

<span id="class_Image_constant_COMPRESS_SOURCE_GENERIC"></span>

[CompressSource](class_image.md#enum_Image_CompressSource) **COMPRESS_SOURCE_GENERIC** = `0`

Source texture (before compression) is a regular texture. Default for all textures.

<span id="class_Image_constant_COMPRESS_SOURCE_SRGB"></span>

[CompressSource](class_image.md#enum_Image_CompressSource) **COMPRESS_SOURCE_SRGB** = `1`

Source texture (before compression) uses nonlinear sRGB encoding.

<span id="class_Image_constant_COMPRESS_SOURCE_NORMAL"></span>

[CompressSource](class_image.md#enum_Image_CompressSource) **COMPRESS_SOURCE_NORMAL** = `2`

Source texture (before compression) is a normal texture (e.g. it can be compressed into two channels).

---

<span id="enum_Image_ASTCFormat"></span>

enum **ASTCFormat**: [🔗](class_image.md#enum_Image_ASTCFormat)

<span id="class_Image_constant_ASTC_FORMAT_4x4"></span>

[ASTCFormat](class_image.md#enum_Image_ASTCFormat) **ASTC_FORMAT_4x4** = `0`

Hint to indicate that the high quality 4×4 ASTC compression format should be used.

<span id="class_Image_constant_ASTC_FORMAT_8x8"></span>

[ASTCFormat](class_image.md#enum_Image_ASTCFormat) **ASTC_FORMAT_8x8** = `1`

Hint to indicate that the low quality 8×8 ASTC compression format should be used.

---

### Constants

<span id="class_Image_constant_MAX_WIDTH"></span>

**MAX_WIDTH** = `16777216` [🔗](class_image.md#class_Image_constant_MAX_WIDTH)

The maximal width allowed for **Image** resources.

<span id="class_Image_constant_MAX_HEIGHT"></span>

**MAX_HEIGHT** = `16777216` [🔗](class_image.md#class_Image_constant_MAX_HEIGHT)

The maximal height allowed for **Image** resources.

---

### Property Descriptions

<span id="class_Image_property_data"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **data** = `{ "data": PackedByteArray(), "format": "Lum8", "height": 0, "mipmaps": false, "width": 0 }` [🔗](class_image.md#class_Image_property_data)

Holds all the image's color data in a given format. See [Format](class_image.md#enum_Image_Format) constants.

---

### Method Descriptions

<span id="class_Image_method_adjust_bcs"></span>

void **adjust_bcs** ( brightness: [float](class_float.md#class_float), contrast: [float](class_float.md#class_float), saturation: [float](class_float.md#class_float) ) [🔗](class_image.md#class_Image_method_adjust_bcs)

Adjusts this image's `brightness`, `contrast`, and `saturation` by the given values. Does not work if the image is compressed (see [is_compressed()](class_image.md#class_Image_method_is_compressed)).

---

<span id="class_Image_method_blend_rect"></span>

void **blend_rect** ( src: [Image](class_image.md#class_Image), src_rect: [Rect2i](class_rect2i.md#class_Rect2i), dst: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_image.md#class_Image_method_blend_rect)

Alpha-blends `src_rect` from `src` image to this image at coordinates `dst`, clipped accordingly to both image bounds. This image and `src` image **must** have the same format. `src_rect` with non-positive size is treated as empty.

---

<span id="class_Image_method_blend_rect_mask"></span>

void **blend_rect_mask** ( src: [Image](class_image.md#class_Image), mask: [Image](class_image.md#class_Image), src_rect: [Rect2i](class_rect2i.md#class_Rect2i), dst: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_image.md#class_Image_method_blend_rect_mask)

Alpha-blends `src_rect` from `src` image to this image using `mask` image at coordinates `dst`, clipped accordingly to both image bounds. Alpha channels are required for both `src` and `mask`. `dst` pixels and `src` pixels will blend if the corresponding mask pixel's alpha value is not 0. This image and `src` image **must** have the same format. `src` image and `mask` image **must** have the same size (width and height) but they can have different formats. `src_rect` with non-positive size is treated as empty.

---

<span id="class_Image_method_blit_rect"></span>

void **blit_rect** ( src: [Image](class_image.md#class_Image), src_rect: [Rect2i](class_rect2i.md#class_Rect2i), dst: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_image.md#class_Image_method_blit_rect)

Copies `src_rect` from `src` image to this image at coordinates `dst`, clipped accordingly to both image bounds. This image and `src` image **must** have the same format. `src_rect` with non-positive size is treated as empty.

 **Note:** The alpha channel data in `src` will overwrite the corresponding data in this image at the target position. To blend alpha channels, use [blend_rect()](class_image.md#class_Image_method_blend_rect) instead.

---

<span id="class_Image_method_blit_rect_mask"></span>

void **blit_rect_mask** ( src: [Image](class_image.md#class_Image), mask: [Image](class_image.md#class_Image), src_rect: [Rect2i](class_rect2i.md#class_Rect2i), dst: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_image.md#class_Image_method_blit_rect_mask)

Blits `src_rect` area from `src` image to this image at the coordinates given by `dst`, clipped accordingly to both image bounds. `src` pixel is copied onto `dst` if the corresponding `mask` pixel's alpha value is not 0. This image and `src` image **must** have the same format. `src` image and `mask` image **must** have the same size (width and height) but they can have different formats. `src_rect` with non-positive size is treated as empty.

---

<span id="class_Image_method_bump_map_to_normal_map"></span>

void **bump_map_to_normal_map** ( bump_scale: [float](class_float.md#class_float) = 1.0 ) [🔗](class_image.md#class_Image_method_bump_map_to_normal_map)

Converts a bump map to a normal map. A bump map provides a height offset per-pixel, while a normal map provides a normal direction per pixel.

---

<span id="class_Image_method_clear_mipmaps"></span>

void **clear_mipmaps** ( ) [🔗](class_image.md#class_Image_method_clear_mipmaps)

Removes the image's mipmaps.

---

<span id="class_Image_method_compress"></span>

Error **compress** ( mode: [CompressMode](class_image.md#enum_Image_CompressMode), source: [CompressSource](class_image.md#enum_Image_CompressSource) = 0, astc_format: [ASTCFormat](class_image.md#enum_Image_ASTCFormat) = 0 ) [🔗](class_image.md#class_Image_method_compress)

Compresses the image with a VRAM-compressed format to use less memory. Can not directly access pixel data while the image is compressed. Returns error if the chosen compression mode is not available.

The `source` parameter helps to pick the best compression method for DXT and ETC2 formats. It is ignored for ASTC compression.

The `astc_format` parameter is only taken into account when using ASTC compression; it is ignored for all other formats.

 **Note:** [compress()](class_image.md#class_Image_method_compress) is only supported in editor builds. When run in an exported project, this method always returns @GlobalScope.ERR_UNAVAILABLE.

---

<span id="class_Image_method_compress_from_channels"></span>

Error **compress_from_channels** ( mode: [CompressMode](class_image.md#enum_Image_CompressMode), channels: [UsedChannels](class_image.md#enum_Image_UsedChannels), astc_format: [ASTCFormat](class_image.md#enum_Image_ASTCFormat) = 0 ) [🔗](class_image.md#class_Image_method_compress_from_channels)

Compresses the image with a VRAM-compressed format to use less memory. Can not directly access pixel data while the image is compressed. Returns error if the chosen compression mode is not available.

This is an alternative to [compress()](class_image.md#class_Image_method_compress) that lets the user supply the channels used in order for the compressor to pick the best DXT and ETC2 formats. For other formats (non DXT or ETC2), this argument is ignored.

The `astc_format` parameter is only taken into account when using ASTC compression; it is ignored for all other formats.

 **Note:** [compress_from_channels()](class_image.md#class_Image_method_compress_from_channels) is only supported in editor builds. When run in an exported project, this method always returns @GlobalScope.ERR_UNAVAILABLE.

---

<span id="class_Image_method_compute_image_metrics"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **compute_image_metrics** ( compared_image: [Image](class_image.md#class_Image), use_luma: [bool](class_bool.md#class_bool) ) [🔗](class_image.md#class_Image_method_compute_image_metrics)

Compute image metrics on the current image and the compared image. This can be used to calculate the similarity between two images.

The dictionary contains `max`, `mean`, `mean_squared`, `root_mean_squared` and `peak_snr`.

---

<span id="class_Image_method_convert"></span>

void **convert** ( format: [Format](class_image.md#enum_Image_Format) ) [🔗](class_image.md#class_Image_method_convert)

Converts this image's format to the given `format`.

---

<span id="class_Image_method_copy_from"></span>

void **copy_from** ( src: [Image](class_image.md#class_Image) ) [🔗](class_image.md#class_Image_method_copy_from)

Copies `src` image to this image.

---

<span id="class_Image_method_create"></span>

[Image](class_image.md#class_Image) **create** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), format: [Format](class_image.md#enum_Image_Format) ) *static* [🔗](class_image.md#class_Image_method_create)

**Deprecated:** Use [create_empty()](class_image.md#class_Image_method_create_empty).

Creates an empty image of the given size and format. If `use_mipmaps` is `true`, generates mipmaps for this image (see [generate_mipmaps()](class_image.md#class_Image_method_generate_mipmaps)).

---

<span id="class_Image_method_create_empty"></span>

[Image](class_image.md#class_Image) **create_empty** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), format: [Format](class_image.md#enum_Image_Format) ) *static* [🔗](class_image.md#class_Image_method_create_empty)

Creates an empty image of the given size and format. If `use_mipmaps` is `true`, generates mipmaps for this image (see [generate_mipmaps()](class_image.md#class_Image_method_generate_mipmaps)).

---

<span id="class_Image_method_create_from_data"></span>

[Image](class_image.md#class_Image) **create_from_data** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), format: [Format](class_image.md#enum_Image_Format), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) *static* [🔗](class_image.md#class_Image_method_create_from_data)

Creates a new image of the given size and format. Fills the image with the given raw data. If `use_mipmaps` is `true`, loads the mipmaps for this image from `data`. See [generate_mipmaps()](class_image.md#class_Image_method_generate_mipmaps).

---

<span id="class_Image_method_crop"></span>

void **crop** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) [🔗](class_image.md#class_Image_method_crop)

Crops the image to the given `width` and `height`. If the specified size is larger than the current size, the extra area is filled with black pixels.

---

<span id="class_Image_method_decompress"></span>

Error **decompress** ( ) [🔗](class_image.md#class_Image_method_decompress)

Decompresses the image if it is VRAM-compressed in a supported format. This increases memory utilization, but allows modifying the image. Returns @GlobalScope.OK if the format is supported, otherwise @GlobalScope.ERR_UNAVAILABLE. All VRAM-compressed formats supported by Godot can be decompressed with this method, except [FORMAT_ETC2_R11S](class_image.md#class_Image_constant_FORMAT_ETC2_R11S), [FORMAT_ETC2_RG11S](class_image.md#class_Image_constant_FORMAT_ETC2_RG11S), and [FORMAT_ETC2_RGB8A1](class_image.md#class_Image_constant_FORMAT_ETC2_RGB8A1).

---

<span id="class_Image_method_detect_alpha"></span>

[AlphaMode](class_image.md#enum_Image_AlphaMode) **detect_alpha** ( ) *const* [🔗](class_image.md#class_Image_method_detect_alpha)

Returns [ALPHA_BLEND](class_image.md#class_Image_constant_ALPHA_BLEND) if the image has data for alpha values. Returns [ALPHA_BIT](class_image.md#class_Image_constant_ALPHA_BIT) if all the alpha values are stored in a single bit. Returns [ALPHA_NONE](class_image.md#class_Image_constant_ALPHA_NONE) if no data for alpha values is found.

---

<span id="class_Image_method_detect_used_channels"></span>

[UsedChannels](class_image.md#enum_Image_UsedChannels) **detect_used_channels** ( source: [CompressSource](class_image.md#enum_Image_CompressSource) = 0 ) *const* [🔗](class_image.md#class_Image_method_detect_used_channels)

Returns the color channels used by this image. If the image is compressed, the original `source` must be specified.

---

<span id="class_Image_method_fill"></span>

void **fill** ( color: [Color](class_color.md#class_Color) ) [🔗](class_image.md#class_Image_method_fill)

Fills the image with `color`.

---

<span id="class_Image_method_fill_rect"></span>

void **fill_rect** ( rect: [Rect2i](class_rect2i.md#class_Rect2i), color: [Color](class_color.md#class_Color) ) [🔗](class_image.md#class_Image_method_fill_rect)

Fills `rect` with `color`.

---

<span id="class_Image_method_fix_alpha_edges"></span>

void **fix_alpha_edges** ( ) [🔗](class_image.md#class_Image_method_fix_alpha_edges)

Blends low-alpha pixels with nearby pixels.

---

<span id="class_Image_method_flip_x"></span>

void **flip_x** ( ) [🔗](class_image.md#class_Image_method_flip_x)

Flips the image horizontally.

---

<span id="class_Image_method_flip_y"></span>

void **flip_y** ( ) [🔗](class_image.md#class_Image_method_flip_y)

Flips the image vertically.

---

<span id="class_Image_method_generate_mipmaps"></span>

Error **generate_mipmaps** ( renormalize: [bool](class_bool.md#class_bool) = false ) [🔗](class_image.md#class_Image_method_generate_mipmaps)

Generates mipmaps for the image. Mipmaps are precalculated lower-resolution copies of the image that are automatically used if the image needs to be scaled down when rendered. They help improve image quality and performance when rendering. This method returns an error if the image is compressed, in a custom format, or if the image's width/height is `0`. Enabling `renormalize` when generating mipmaps for normal map textures will make sure all resulting vector values are normalized.

It is possible to check if the image has mipmaps by calling [has_mipmaps()](class_image.md#class_Image_method_has_mipmaps) or [get_mipmap_count()](class_image.md#class_Image_method_get_mipmap_count). Calling [generate_mipmaps()](class_image.md#class_Image_method_generate_mipmaps) on an image that already has mipmaps will replace existing mipmaps in the image.

---

<span id="class_Image_method_get_data"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_data** ( ) *const* [🔗](class_image.md#class_Image_method_get_data)

Returns a copy of the image's raw data.

---

<span id="class_Image_method_get_data_size"></span>

[int](class_int.md#class_int) **get_data_size** ( ) *const* [🔗](class_image.md#class_Image_method_get_data_size)

Returns size (in bytes) of the image's raw data.

---

<span id="class_Image_method_get_format"></span>

[Format](class_image.md#enum_Image_Format) **get_format** ( ) *const* [🔗](class_image.md#class_Image_method_get_format)

Returns this image's format.

---

<span id="class_Image_method_get_height"></span>

[int](class_int.md#class_int) **get_height** ( ) *const* [🔗](class_image.md#class_Image_method_get_height)

Returns the image's height.

---

<span id="class_Image_method_get_mipmap_count"></span>

[int](class_int.md#class_int) **get_mipmap_count** ( ) *const* [🔗](class_image.md#class_Image_method_get_mipmap_count)

Returns the number of mipmap levels or 0 if the image has no mipmaps. The largest main level image is not counted as a mipmap level by this method, so if you want to include it you can add 1 to this count.

---

<span id="class_Image_method_get_mipmap_offset"></span>

[int](class_int.md#class_int) **get_mipmap_offset** ( mipmap: [int](class_int.md#class_int) ) *const* [🔗](class_image.md#class_Image_method_get_mipmap_offset)

Returns the offset where the image's mipmap with index `mipmap` is stored in the [data](class_image.md#class_Image_property_data) dictionary.

---

<span id="class_Image_method_get_pixel"></span>

[Color](class_color.md#class_Color) **get_pixel** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) *const* [🔗](class_image.md#class_Image_method_get_pixel)

Returns the color of the pixel at `(x, y)`.

This is the same as [get_pixelv()](class_image.md#class_Image_method_get_pixelv), but with two integer arguments instead of a [Vector2i](class_vector2i.md#class_Vector2i) argument.

---

<span id="class_Image_method_get_pixelv"></span>

[Color](class_color.md#class_Color) **get_pixelv** ( point: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_image.md#class_Image_method_get_pixelv)

Returns the color of the pixel at `point`.

This is the same as [get_pixel()](class_image.md#class_Image_method_get_pixel), but with a [Vector2i](class_vector2i.md#class_Vector2i) argument instead of two integer arguments.

---

<span id="class_Image_method_get_region"></span>

[Image](class_image.md#class_Image) **get_region** ( region: [Rect2i](class_rect2i.md#class_Rect2i) ) *const* [🔗](class_image.md#class_Image_method_get_region)

Returns a new **Image** that is a copy of this **Image**'s area specified with `region`.

---

<span id="class_Image_method_get_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_size** ( ) *const* [🔗](class_image.md#class_Image_method_get_size)

Returns the image's size (width and height).

---

<span id="class_Image_method_get_used_rect"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **get_used_rect** ( ) *const* [🔗](class_image.md#class_Image_method_get_used_rect)

Returns a [Rect2i](class_rect2i.md#class_Rect2i) enclosing the visible portion of the image, considering each pixel with a non-zero alpha channel as visible.

---

<span id="class_Image_method_get_width"></span>

[int](class_int.md#class_int) **get_width** ( ) *const* [🔗](class_image.md#class_Image_method_get_width)

Returns the image's width.

---

<span id="class_Image_method_has_mipmaps"></span>

[bool](class_bool.md#class_bool) **has_mipmaps** ( ) *const* [🔗](class_image.md#class_Image_method_has_mipmaps)

Returns `true` if the image has generated mipmaps.

---

<span id="class_Image_method_is_compressed"></span>

[bool](class_bool.md#class_bool) **is_compressed** ( ) *const* [🔗](class_image.md#class_Image_method_is_compressed)

Returns `true` if the image is compressed.

---

<span id="class_Image_method_is_empty"></span>

[bool](class_bool.md#class_bool) **is_empty** ( ) *const* [🔗](class_image.md#class_Image_method_is_empty)

Returns `true` if the image has no data.

---

<span id="class_Image_method_is_invisible"></span>

[bool](class_bool.md#class_bool) **is_invisible** ( ) *const* [🔗](class_image.md#class_Image_method_is_invisible)

Returns `true` if all the image's pixels have an alpha value of 0. Returns `false` if any pixel has an alpha value higher than 0.

---

<span id="class_Image_method_linear_to_srgb"></span>

void **linear_to_srgb** ( ) [🔗](class_image.md#class_Image_method_linear_to_srgb)

Converts the entire image from linear encoding to nonlinear sRGB encoding by using a lookup table. Only works on images with [FORMAT_RGB8](class_image.md#class_Image_constant_FORMAT_RGB8) or [FORMAT_RGBA8](class_image.md#class_Image_constant_FORMAT_RGBA8) formats.

---

<span id="class_Image_method_load"></span>

Error **load** ( path: [String](class_string.md#class_String) ) [🔗](class_image.md#class_Image_method_load)

Loads an image from file `path`. See `Supported image formats <../tutorials/assets_pipeline/importing_images.html#supported-image-formats>`__ for a list of supported image formats and limitations.

 **Warning:** This method should only be used in the editor or in cases when you need to load external images at run-time, such as images located at the `user://` directory, and may not work in exported projects.

See also [ImageTexture](class_imagetexture.md#class_ImageTexture) description for usage examples.

---

<span id="class_Image_method_load_bmp_from_buffer"></span>

Error **load_bmp_from_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_image.md#class_Image_method_load_bmp_from_buffer)

Loads an image from the binary contents of a BMP file.

 **Note:** Godot's BMP module doesn't support 16-bit per pixel images. Only 1-bit, 4-bit, 8-bit, 24-bit, and 32-bit per pixel images are supported.

 **Note:** This method is only available in engine builds with the BMP module enabled. By default, the BMP module is enabled, but it can be disabled at build-time using the `module_bmp_enabled=no` SCons option.

---

<span id="class_Image_method_load_dds_from_buffer"></span>

Error **load_dds_from_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_image.md#class_Image_method_load_dds_from_buffer)

Loads an image from the binary contents of a DDS file.

 **Note:** This method is only available in engine builds with the DDS module enabled. By default, the DDS module is enabled, but it can be disabled at build-time using the `module_dds_enabled=no` SCons option.

---

<span id="class_Image_method_load_exr_from_buffer"></span>

Error **load_exr_from_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_image.md#class_Image_method_load_exr_from_buffer)

Loads an image from the binary contents of an OpenEXR file.

---

<span id="class_Image_method_load_from_file"></span>

[Image](class_image.md#class_Image) **load_from_file** ( path: [String](class_string.md#class_String) ) *static* [🔗](class_image.md#class_Image_method_load_from_file)

Creates a new **Image** and loads data from the specified file.

---

<span id="class_Image_method_load_jpg_from_buffer"></span>

Error **load_jpg_from_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_image.md#class_Image_method_load_jpg_from_buffer)

Loads an image from the binary contents of a JPEG file.

---

<span id="class_Image_method_load_ktx_from_buffer"></span>

Error **load_ktx_from_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_image.md#class_Image_method_load_ktx_from_buffer)

Loads an image from the binary contents of a KTX file. Unlike most image formats, KTX can store VRAM-compressed data and embed mipmaps.

 **Note:** Godot's libktx implementation only supports 2D images. Cubemaps, texture arrays, and de-padding are not supported.

 **Note:** This method is only available in engine builds with the KTX module enabled. By default, the KTX module is enabled, but it can be disabled at build-time using the `module_ktx_enabled=no` SCons option.

---

<span id="class_Image_method_load_png_from_buffer"></span>

Error **load_png_from_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_image.md#class_Image_method_load_png_from_buffer)

Loads an image from the binary contents of a PNG file.

---

<span id="class_Image_method_load_svg_from_buffer"></span>

Error **load_svg_from_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), scale: [float](class_float.md#class_float) = 1.0 ) [🔗](class_image.md#class_Image_method_load_svg_from_buffer)

Loads an image from the UTF-8 binary contents of an **uncompressed** SVG file (**.svg**).

 **Note:** Beware when using compressed SVG files (like **.svgz**), they need to be `decompressed` before loading.

 **Note:** This method is only available in engine builds with the SVG module enabled. By default, the SVG module is enabled, but it can be disabled at build-time using the `module_svg_enabled=no` SCons option.

---

<span id="class_Image_method_load_svg_from_string"></span>

Error **load_svg_from_string** ( svg_str: [String](class_string.md#class_String), scale: [float](class_float.md#class_float) = 1.0 ) [🔗](class_image.md#class_Image_method_load_svg_from_string)

Loads an image from the string contents of an SVG file (**.svg**).

 **Note:** This method is only available in engine builds with the SVG module enabled. By default, the SVG module is enabled, but it can be disabled at build-time using the `module_svg_enabled=no` SCons option.

---

<span id="class_Image_method_load_tga_from_buffer"></span>

Error **load_tga_from_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_image.md#class_Image_method_load_tga_from_buffer)

Loads an image from the binary contents of a TGA file.

 **Note:** This method is only available in engine builds with the TGA module enabled. By default, the TGA module is enabled, but it can be disabled at build-time using the `module_tga_enabled=no` SCons option.

---

<span id="class_Image_method_load_webp_from_buffer"></span>

Error **load_webp_from_buffer** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_image.md#class_Image_method_load_webp_from_buffer)

Loads an image from the binary contents of a WebP file.

---

<span id="class_Image_method_normal_map_to_xy"></span>

void **normal_map_to_xy** ( ) [🔗](class_image.md#class_Image_method_normal_map_to_xy)

Converts the image's data to represent coordinates on a 3D plane. This is used when the image represents a normal map. A normal map can add lots of detail to a 3D surface without increasing the polygon count.

---

<span id="class_Image_method_premultiply_alpha"></span>

void **premultiply_alpha** ( ) [🔗](class_image.md#class_Image_method_premultiply_alpha)

Multiplies color values with alpha values. Resulting color values for a pixel are `(color * alpha)/256`. See also [CanvasItemMaterial.blend_mode](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_blend_mode).

---

<span id="class_Image_method_resize"></span>

void **resize** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), interpolation: [Interpolation](class_image.md#enum_Image_Interpolation) = 1 ) [🔗](class_image.md#class_Image_method_resize)

Resizes the image to the given `width` and `height`. New pixels are calculated using the `interpolation` mode defined via [Interpolation](class_image.md#enum_Image_Interpolation) constants.

 **Note:** If the image's format is [FORMAT_RGBA4444](class_image.md#class_Image_constant_FORMAT_RGBA4444), [FORMAT_RGB565](class_image.md#class_Image_constant_FORMAT_RGB565), or [FORMAT_RGBE9995](class_image.md#class_Image_constant_FORMAT_RGBE9995), it will be temporarily converted to either [FORMAT_RGBA8](class_image.md#class_Image_constant_FORMAT_RGBA8) or [FORMAT_RGBAH](class_image.md#class_Image_constant_FORMAT_RGBAH). This can affect the quality of the resized image.

---

<span id="class_Image_method_resize_to_po2"></span>

void **resize_to_po2** ( square: [bool](class_bool.md#class_bool) = false, interpolation: [Interpolation](class_image.md#enum_Image_Interpolation) = 1 ) [🔗](class_image.md#class_Image_method_resize_to_po2)

Resizes the image to the nearest power of 2 for the width and height. If `square` is `true`, sets width and height to be the same. New pixels are calculated using the `interpolation` mode defined via [Interpolation](class_image.md#enum_Image_Interpolation) constants.

---

<span id="class_Image_method_rgbe_to_srgb"></span>

[Image](class_image.md#class_Image) **rgbe_to_srgb** ( ) [🔗](class_image.md#class_Image_method_rgbe_to_srgb)

Converts a standard linear RGBE (Red Green Blue Exponent) image to an image that uses nonlinear sRGB encoding.

---

<span id="class_Image_method_rotate_90"></span>

void **rotate_90** ( direction: ClockDirection ) [🔗](class_image.md#class_Image_method_rotate_90)

Rotates the image in the specified `direction` by `90` degrees. The width and height of the image must be greater than `1`. If the width and height are not equal, the image will be resized.

---

<span id="class_Image_method_rotate_180"></span>

void **rotate_180** ( ) [🔗](class_image.md#class_Image_method_rotate_180)

Rotates the image by `180` degrees. The width and height of the image must be greater than `1`.

---

<span id="class_Image_method_save_dds"></span>

Error **save_dds** ( path: [String](class_string.md#class_String) ) *const* [🔗](class_image.md#class_Image_method_save_dds)

Saves the image as a DDS (DirectDraw Surface) file to `path`. DDS is a container format that can store textures in various compression formats, such as DXT1, DXT5, or BC7. This function will return @GlobalScope.ERR_UNAVAILABLE if Godot was compiled without the DDS module.

 **Note:** The DDS module may be disabled in certain builds, which means [save_dds()](class_image.md#class_Image_method_save_dds) will return @GlobalScope.ERR_UNAVAILABLE when it is called from an exported project.

---

<span id="class_Image_method_save_dds_to_buffer"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **save_dds_to_buffer** ( ) *const* [🔗](class_image.md#class_Image_method_save_dds_to_buffer)

Saves the image as a DDS (DirectDraw Surface) file to a byte array. DDS is a container format that can store textures in various compression formats, such as DXT1, DXT5, or BC7. This function will return an empty byte array if Godot was compiled without the DDS module.

 **Note:** The DDS module may be disabled in certain builds, which means [save_dds_to_buffer()](class_image.md#class_Image_method_save_dds_to_buffer) will return an empty byte array when it is called from an exported project.

---

<span id="class_Image_method_save_exr"></span>

Error **save_exr** ( path: [String](class_string.md#class_String), grayscale: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_image.md#class_Image_method_save_exr)

Saves the image as an EXR file to `path`. If `grayscale` is `true` and the image has only one channel, it will be saved explicitly as monochrome rather than one red channel. This function will return @GlobalScope.ERR_UNAVAILABLE if Godot was compiled without the TinyEXR module.

---

<span id="class_Image_method_save_exr_to_buffer"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **save_exr_to_buffer** ( grayscale: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_image.md#class_Image_method_save_exr_to_buffer)

Saves the image as an EXR file to a byte array. If `grayscale` is `true` and the image has only one channel, it will be saved explicitly as monochrome rather than one red channel. This function will return an empty byte array if Godot was compiled without the TinyEXR module.

---

<span id="class_Image_method_save_jpg"></span>

Error **save_jpg** ( path: [String](class_string.md#class_String), quality: [float](class_float.md#class_float) = 0.75 ) *const* [🔗](class_image.md#class_Image_method_save_jpg)

Saves the image as a JPEG file to `path` with the specified `quality` between `0.01` and `1.0` (inclusive). Higher `quality` values result in better-looking output at the cost of larger file sizes. Recommended `quality` values are between `0.75` and `0.90`. Even at quality `1.00`, JPEG compression remains lossy.

 **Note:** JPEG does not save an alpha channel. If the **Image** contains an alpha channel, the image will still be saved, but the resulting JPEG file won't contain the alpha channel.

---

<span id="class_Image_method_save_jpg_to_buffer"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **save_jpg_to_buffer** ( quality: [float](class_float.md#class_float) = 0.75 ) *const* [🔗](class_image.md#class_Image_method_save_jpg_to_buffer)

Saves the image as a JPEG file to a byte array with the specified `quality` between `0.01` and `1.0` (inclusive). Higher `quality` values result in better-looking output at the cost of larger byte array sizes (and therefore memory usage). Recommended `quality` values are between `0.75` and `0.90`. Even at quality `1.00`, JPEG compression remains lossy.

 **Note:** JPEG does not save an alpha channel. If the **Image** contains an alpha channel, the image will still be saved, but the resulting byte array won't contain the alpha channel.

---

<span id="class_Image_method_save_png"></span>

Error **save_png** ( path: [String](class_string.md#class_String) ) *const* [🔗](class_image.md#class_Image_method_save_png)

Saves the image as a PNG file to the file at `path`.

---

<span id="class_Image_method_save_png_to_buffer"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **save_png_to_buffer** ( ) *const* [🔗](class_image.md#class_Image_method_save_png_to_buffer)

Saves the image as a PNG file to a byte array.

---

<span id="class_Image_method_save_webp"></span>

Error **save_webp** ( path: [String](class_string.md#class_String), lossy: [bool](class_bool.md#class_bool) = false, quality: [float](class_float.md#class_float) = 0.75 ) *const* [🔗](class_image.md#class_Image_method_save_webp)

Saves the image as a WebP (Web Picture) file to the file at `path`. By default it will save lossless. If `lossy` is `true`, the image will be saved lossy, using the `quality` setting between `0.0` and `1.0` (inclusive). Lossless WebP offers more efficient compression than PNG.

 **Note:** The WebP format is limited to a size of 16383×16383 pixels, while PNG can save larger images.

---

<span id="class_Image_method_save_webp_to_buffer"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **save_webp_to_buffer** ( lossy: [bool](class_bool.md#class_bool) = false, quality: [float](class_float.md#class_float) = 0.75 ) *const* [🔗](class_image.md#class_Image_method_save_webp_to_buffer)

Saves the image as a WebP (Web Picture) file to a byte array. By default it will save lossless. If `lossy` is `true`, the image will be saved lossy, using the `quality` setting between `0.0` and `1.0` (inclusive). Lossless WebP offers more efficient compression than PNG.

 **Note:** The WebP format is limited to a size of 16383×16383 pixels, while PNG can save larger images.

---

<span id="class_Image_method_set_data"></span>

void **set_data** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), use_mipmaps: [bool](class_bool.md#class_bool), format: [Format](class_image.md#enum_Image_Format), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_image.md#class_Image_method_set_data)

Overwrites data of an existing **Image**. Non-static equivalent of [create_from_data()](class_image.md#class_Image_method_create_from_data).

---

<span id="class_Image_method_set_pixel"></span>

void **set_pixel** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_image.md#class_Image_method_set_pixel)

Sets the [Color](class_color.md#class_Color) of the pixel at `(x, y)` to `color`.

.. tabs::

```
```

    var img_width = 10
    var img_height = 5
    var img = Image.create(img_width, img_height, false, Image.FORMAT_RGBA8)

    img.set_pixel(1, 2, Color.RED) # Sets the color at (1, 2) to red.

```
```

    int imgWidth = 10;
    int imgHeight = 5;
    var img = Image.Create(imgWidth, imgHeight, false, Image.Format.Rgba8);

    img.SetPixel(1, 2, Colors.Red); // Sets the color at (1, 2) to red.

This is the same as [set_pixelv()](class_image.md#class_Image_method_set_pixelv), but with a two integer arguments instead of a [Vector2i](class_vector2i.md#class_Vector2i) argument.

 **Note:** Depending on the image's format, the color set here may be clamped or lose precision. Do not assume the color returned by [get_pixel()](class_image.md#class_Image_method_get_pixel) to be identical to the one set here; any comparisons will likely need to use an approximation like [Color.is_equal_approx()](class_color.md#class_Color_method_is_equal_approx).

 **Note:** On grayscale image formats, only the red channel of `color` is used (and alpha if relevant). The green and blue channels are ignored.

---

<span id="class_Image_method_set_pixelv"></span>

void **set_pixelv** ( point: [Vector2i](class_vector2i.md#class_Vector2i), color: [Color](class_color.md#class_Color) ) [🔗](class_image.md#class_Image_method_set_pixelv)

Sets the [Color](class_color.md#class_Color) of the pixel at `point` to `color`.

.. tabs::

```
```

    var img_width = 10
    var img_height = 5
    var img = Image.create(img_width, img_height, false, Image.FORMAT_RGBA8)

    img.set_pixelv(Vector2i(1, 2), Color.RED) # Sets the color at (1, 2) to red.

```
```

    int imgWidth = 10;
    int imgHeight = 5;
    var img = Image.Create(imgWidth, imgHeight, false, Image.Format.Rgba8);

    img.SetPixelv(new Vector2I(1, 2), Colors.Red); // Sets the color at (1, 2) to red.

This is the same as [set_pixel()](class_image.md#class_Image_method_set_pixel), but with a [Vector2i](class_vector2i.md#class_Vector2i) argument instead of two integer arguments.

 **Note:** Depending on the image's format, the color set here may be clamped or lose precision. Do not assume the color returned by [get_pixelv()](class_image.md#class_Image_method_get_pixelv) to be identical to the one set here; any comparisons will likely need to use an approximation like [Color.is_equal_approx()](class_color.md#class_Color_method_is_equal_approx).

 **Note:** On grayscale image formats, only the red channel of `color` is used (and alpha if relevant). The green and blue channels are ignored.

---

<span id="class_Image_method_shrink_x2"></span>

void **shrink_x2** ( ) [🔗](class_image.md#class_Image_method_shrink_x2)

Shrinks the image by a factor of 2 on each axis (this divides the pixel count by 4).

---

<span id="class_Image_method_srgb_to_linear"></span>

void **srgb_to_linear** ( ) [🔗](class_image.md#class_Image_method_srgb_to_linear)

Converts the raw data from nonlinear sRGB encoding to linear encoding using a lookup table. Only works on images with [FORMAT_RGB8](class_image.md#class_Image_constant_FORMAT_RGB8) or [FORMAT_RGBA8](class_image.md#class_Image_constant_FORMAT_RGBA8) formats.

 **Note:** The 8-bit formats required by this method are not suitable for storing linearly encoded values; a significant amount of color information will be lost in darker values. To maintain image quality, this method should not be used.
