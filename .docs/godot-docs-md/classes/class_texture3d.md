<span id="class_Texture3D"></span>

## Texture3D

**Inherits:** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CompressedTexture3D](class_compressedtexture3d.md#class_CompressedTexture3D), [ImageTexture3D](class_imagetexture3d.md#class_ImageTexture3D), [NoiseTexture3D](class_noisetexture3d.md#class_NoiseTexture3D), [PlaceholderTexture3D](class_placeholdertexture3d.md#class_PlaceholderTexture3D), [Texture3DRD](class_texture3drd.md#class_Texture3DRD)

Base class for 3-dimensional textures.

### Description

Base class for [ImageTexture3D](class_imagetexture3d.md#class_ImageTexture3D) and [CompressedTexture3D](class_compressedtexture3d.md#class_CompressedTexture3D). Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. **Texture3D** is the base class for all 3-dimensional texture types. See also [TextureLayered](class_texturelayered.md#class_TextureLayered).

All images need to have the same width, height and number of mipmap levels.

To create such a texture file yourself, reimport your image files using the Godot Editor import presets.

### Methods


| [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] | [_get_data](class_texture3d.md#class_Texture3D_private_method__get_data) ( ) | virtual | required | const |
| --- | --- | --- | --- | --- |
| [int](class_int.md#class_int) | [_get_depth](class_texture3d.md#class_Texture3D_private_method__get_depth) ( ) | virtual | required | const |
| [Format](class_image.md#enum_Image_Format) | [_get_format](class_texture3d.md#class_Texture3D_private_method__get_format) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_height](class_texture3d.md#class_Texture3D_private_method__get_height) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_width](class_texture3d.md#class_Texture3D_private_method__get_width) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_mipmaps](class_texture3d.md#class_Texture3D_private_method__has_mipmaps) ( ) | virtual | required | const |
| [Resource](class_resource.md#class_Resource) | [create_placeholder](class_texture3d.md#class_Texture3D_method_create_placeholder) ( ) const |
| [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] | [get_data](class_texture3d.md#class_Texture3D_method_get_data) ( ) const |
| [int](class_int.md#class_int) | [get_depth](class_texture3d.md#class_Texture3D_method_get_depth) ( ) const |
| [Format](class_image.md#enum_Image_Format) | [get_format](class_texture3d.md#class_Texture3D_method_get_format) ( ) const |
| [int](class_int.md#class_int) | [get_height](class_texture3d.md#class_Texture3D_method_get_height) ( ) const |
| [int](class_int.md#class_int) | [get_width](class_texture3d.md#class_Texture3D_method_get_width) ( ) const |
| [bool](class_bool.md#class_bool) | [has_mipmaps](class_texture3d.md#class_Texture3D_method_has_mipmaps) ( ) const |

---

### Method Descriptions

<span id="class_Texture3D_private_method__get_data"></span>

[Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] **_get_data** ( ) *virtual* |required| *const* [🔗](class_texture3d.md#class_Texture3D_private_method__get_data)

Called when the **Texture3D**'s data is queried.

---

<span id="class_Texture3D_private_method__get_depth"></span>

[int](class_int.md#class_int) **_get_depth** ( ) *virtual* |required| *const* [🔗](class_texture3d.md#class_Texture3D_private_method__get_depth)

Called when the **Texture3D**'s depth is queried.

---

<span id="class_Texture3D_private_method__get_format"></span>

[Format](class_image.md#enum_Image_Format) **_get_format** ( ) *virtual* |required| *const* [🔗](class_texture3d.md#class_Texture3D_private_method__get_format)

Called when the **Texture3D**'s format is queried.

---

<span id="class_Texture3D_private_method__get_height"></span>

[int](class_int.md#class_int) **_get_height** ( ) *virtual* |required| *const* [🔗](class_texture3d.md#class_Texture3D_private_method__get_height)

Called when the **Texture3D**'s height is queried.

---

<span id="class_Texture3D_private_method__get_width"></span>

[int](class_int.md#class_int) **_get_width** ( ) *virtual* |required| *const* [🔗](class_texture3d.md#class_Texture3D_private_method__get_width)

Called when the **Texture3D**'s width is queried.

---

<span id="class_Texture3D_private_method__has_mipmaps"></span>

[bool](class_bool.md#class_bool) **_has_mipmaps** ( ) *virtual* |required| *const* [🔗](class_texture3d.md#class_Texture3D_private_method__has_mipmaps)

Called when the presence of mipmaps in the **Texture3D** is queried.

---

<span id="class_Texture3D_method_create_placeholder"></span>

[Resource](class_resource.md#class_Resource) **create_placeholder** ( ) *const* [🔗](class_texture3d.md#class_Texture3D_method_create_placeholder)

Creates a placeholder version of this resource ([PlaceholderTexture3D](class_placeholdertexture3d.md#class_PlaceholderTexture3D)).

---

<span id="class_Texture3D_method_get_data"></span>

[Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] **get_data** ( ) *const* [🔗](class_texture3d.md#class_Texture3D_method_get_data)

Returns the **Texture3D**'s data as an array of [Image](class_image.md#class_Image) s. Each [Image](class_image.md#class_Image) represents a *slice* of the **Texture3D**, with different slices mapping to different depth (Z axis) levels.

---

<span id="class_Texture3D_method_get_depth"></span>

[int](class_int.md#class_int) **get_depth** ( ) *const* [🔗](class_texture3d.md#class_Texture3D_method_get_depth)

Returns the **Texture3D**'s depth in pixels. Depth is typically represented by the Z axis (a dimension not present in [Texture2D](class_texture2d.md#class_Texture2D)).

---

<span id="class_Texture3D_method_get_format"></span>

[Format](class_image.md#enum_Image_Format) **get_format** ( ) *const* [🔗](class_texture3d.md#class_Texture3D_method_get_format)

Returns the current format being used by this texture.

---

<span id="class_Texture3D_method_get_height"></span>

[int](class_int.md#class_int) **get_height** ( ) *const* [🔗](class_texture3d.md#class_Texture3D_method_get_height)

Returns the **Texture3D**'s height in pixels. Width is typically represented by the Y axis.

---

<span id="class_Texture3D_method_get_width"></span>

[int](class_int.md#class_int) **get_width** ( ) *const* [🔗](class_texture3d.md#class_Texture3D_method_get_width)

Returns the **Texture3D**'s width in pixels. Width is typically represented by the X axis.

---

<span id="class_Texture3D_method_has_mipmaps"></span>

[bool](class_bool.md#class_bool) **has_mipmaps** ( ) *const* [🔗](class_texture3d.md#class_Texture3D_method_has_mipmaps)

Returns `true` if the **Texture3D** has generated mipmaps.
