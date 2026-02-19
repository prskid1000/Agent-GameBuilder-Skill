<span id="class_DrawableTexture2D"></span>

## DrawableTexture2D

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 2D texture that supports drawing to itself via Blit calls.

### Description

A 2D texture that can be modified via blit calls, copying from a target texture to itself. Primarily intended to be managed in code, a user must call [setup()](class_drawabletexture2d.md#class_DrawableTexture2D_method_setup) to initialize the state before drawing. Each [blit_rect()](class_drawabletexture2d.md#class_DrawableTexture2D_method_blit_rect) call takes at least a rectangle, the area to draw to, and another texture, what to be drawn. The draw calls use a Texture_Blit Shader to process and calculate the result, pixel by pixel. Users can supply their own ShaderMaterial with custom Texture_Blit shaders for more complex behaviors.

### Properties


| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| --- | --- | --- |

### Methods


| void | [blit_rect](class_drawabletexture2d.md#class_DrawableTexture2D_method_blit_rect) ( rect: [Rect2i](class_rect2i.md#class_Rect2i), source: [Texture2D](class_texture2d.md#class_Texture2D), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), mipmap: [int](class_int.md#class_int) = 0, material: [Material](class_material.md#class_Material) = null ) |
| --- | --- |
| void | [blit_rect_multi](class_drawabletexture2d.md#class_DrawableTexture2D_method_blit_rect_multi) ( rect: [Rect2i](class_rect2i.md#class_Rect2i), sources: [Array](class_array.md#class_Array)\[[Texture2D](class_texture2d.md#class_Texture2D)\], extra_targets: [Array](class_array.md#class_Array)\[[DrawableTexture2D](class_drawabletexture2d.md#class_DrawableTexture2D)\], modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), mipmap: [int](class_int.md#class_int) = 0, material: [Material](class_material.md#class_Material) = null ) |
| void | [generate_mipmaps](class_drawabletexture2d.md#class_DrawableTexture2D_method_generate_mipmaps) ( ) |
| void | [setup](class_drawabletexture2d.md#class_DrawableTexture2D_method_setup) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), format: [DrawableFormat](class_drawabletexture2d.md#enum_DrawableTexture2D_DrawableFormat), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), use_mipmaps: [bool](class_bool.md#class_bool) = false ) |

---

### Enumerations

<span id="enum_DrawableTexture2D_DrawableFormat"></span>

enum **DrawableFormat**: [🔗](class_drawabletexture2d.md#enum_DrawableTexture2D_DrawableFormat)

<span id="class_DrawableTexture2D_constant_DRAWABLE_FORMAT_RGBA8"></span>

[DrawableFormat](class_drawabletexture2d.md#enum_DrawableTexture2D_DrawableFormat) **DRAWABLE_FORMAT_RGBA8** = `0`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

<span id="class_DrawableTexture2D_constant_DRAWABLE_FORMAT_RGBA8_SRGB"></span>

[DrawableFormat](class_drawabletexture2d.md#enum_DrawableTexture2D_DrawableFormat) **DRAWABLE_FORMAT_RGBA8_SRGB** = `1`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

When drawn to, an sRGB to linear color space conversion is performed.

<span id="class_DrawableTexture2D_constant_DRAWABLE_FORMAT_RGBAH"></span>

[DrawableFormat](class_drawabletexture2d.md#enum_DrawableTexture2D_DrawableFormat) **DRAWABLE_FORMAT_RGBAH** = `2`

OpenGL texture format GL_RGBA16F where there are four components, each a 16-bit "half-precision" floating-point value.

<span id="class_DrawableTexture2D_constant_DRAWABLE_FORMAT_RGBAF"></span>

[DrawableFormat](class_drawabletexture2d.md#enum_DrawableTexture2D_DrawableFormat) **DRAWABLE_FORMAT_RGBAF** = `3`

OpenGL texture format GL_RGBA32F where there are four components, each a 32-bit floating-point value.

---

### Method Descriptions

<span id="class_DrawableTexture2D_method_blit_rect"></span>

void **blit_rect** ( rect: [Rect2i](class_rect2i.md#class_Rect2i), source: [Texture2D](class_texture2d.md#class_Texture2D), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), mipmap: [int](class_int.md#class_int) = 0, material: [Material](class_material.md#class_Material) = null ) [🔗](class_drawabletexture2d.md#class_DrawableTexture2D_method_blit_rect)

**Experimental:** This function and its parameters are likely to change in the 4.7 Dev Cycle

Draws to given `rect` on this texture by copying from the given `source`. A `modulate` color can be passed in for the shader to use, but defaults to White. The `mipmap` value can specify a draw to a lower mipmap level. The `material` parameter can take a ShaderMaterial with a TextureBlit Shader for custom drawing behavior.

---

<span id="class_DrawableTexture2D_method_blit_rect_multi"></span>

void **blit_rect_multi** ( rect: [Rect2i](class_rect2i.md#class_Rect2i), sources: [Array](class_array.md#class_Array)\[[Texture2D](class_texture2d.md#class_Texture2D)\], extra_targets: [Array](class_array.md#class_Array)\[[DrawableTexture2D](class_drawabletexture2d.md#class_DrawableTexture2D)\], modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), mipmap: [int](class_int.md#class_int) = 0, material: [Material](class_material.md#class_Material) = null ) [🔗](class_drawabletexture2d.md#class_DrawableTexture2D_method_blit_rect_multi)

**Experimental:** This function and its parameters are likely to change in the 4.7 Dev Cycle

Draws to the given `rect` on this texture, as well as on up to 3 DrawableTexture `extra_targets`. All `extra_targets` must be the same size and DrawableFormat as the original target, otherwise the Shader may fail. Expects up to 4 Texture `sources`, but will replace missing `sources` with default Black Textures.

---

<span id="class_DrawableTexture2D_method_generate_mipmaps"></span>

void **generate_mipmaps** ( ) [🔗](class_drawabletexture2d.md#class_DrawableTexture2D_method_generate_mipmaps)

Re-calculates the mipmaps for this texture on demand.

---

<span id="class_DrawableTexture2D_method_setup"></span>

void **setup** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), format: [DrawableFormat](class_drawabletexture2d.md#enum_DrawableTexture2D_DrawableFormat), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), use_mipmaps: [bool](class_bool.md#class_bool) = false ) [🔗](class_drawabletexture2d.md#class_DrawableTexture2D_method_setup)

**Experimental:** This function and its parameters are likely to change in the 4.7 Dev Cycle

Initializes the DrawableTexture to a White texture of the given `width`, `height`, and `format`.
