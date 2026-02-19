<span id="class_Texture2D"></span>

## Texture2D

**Inherits:** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AnimatedTexture](class_animatedtexture.md#class_AnimatedTexture), [AtlasTexture](class_atlastexture.md#class_AtlasTexture), [CameraTexture](class_cameratexture.md#class_CameraTexture), [CanvasTexture](class_canvastexture.md#class_CanvasTexture), [CompressedTexture2D](class_compressedtexture2d.md#class_CompressedTexture2D), [CurveTexture](class_curvetexture.md#class_CurveTexture), [CurveXYZTexture](class_curvexyztexture.md#class_CurveXYZTexture), [DPITexture](class_dpitexture.md#class_DPITexture), [DrawableTexture2D](class_drawabletexture2d.md#class_DrawableTexture2D), [ExternalTexture](class_externaltexture.md#class_ExternalTexture), [GradientTexture1D](class_gradienttexture1d.md#class_GradientTexture1D), [GradientTexture2D](class_gradienttexture2d.md#class_GradientTexture2D), [ImageTexture](class_imagetexture.md#class_ImageTexture), [MeshTexture](class_meshtexture.md#class_MeshTexture), [NoiseTexture2D](class_noisetexture2d.md#class_NoiseTexture2D), [PlaceholderTexture2D](class_placeholdertexture2d.md#class_PlaceholderTexture2D), [PortableCompressedTexture2D](class_portablecompressedtexture2d.md#class_PortableCompressedTexture2D), [Texture2DRD](class_texture2drd.md#class_Texture2DRD), [ViewportTexture](class_viewporttexture.md#class_ViewportTexture)

Texture for 2D and 3D.

### Description

A texture works by registering an image in the video hardware, which then can be used in 3D models or 2D [Sprite2D](class_sprite2d.md#class_Sprite2D) or GUI [Control](class_control.md#class_Control).

Textures are often created by loading them from a file. See @GDScript.load().

 **Texture2D** is a base for other resources. It cannot be used directly.

 **Note:** The maximum texture size is 16384×16384 pixels due to graphics hardware limitations. Larger textures may fail to import.

### Methods


| void | [_draw](class_texture2d.md#class_Texture2D_private_method__draw) ( to_canvas_item: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), modulate: [Color](class_color.md#class_Color), transpose: [bool](class_bool.md#class_bool) ) | virtual | const |
| --- | --- | --- | --- |
| void | [_draw_rect](class_texture2d.md#class_Texture2D_private_method__draw_rect) ( to_canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), tile: [bool](class_bool.md#class_bool), modulate: [Color](class_color.md#class_Color), transpose: [bool](class_bool.md#class_bool) ) | virtual | const |
| void | [_draw_rect_region](class_texture2d.md#class_Texture2D_private_method__draw_rect_region) ( to_canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color), transpose: [bool](class_bool.md#class_bool), clip_uv: [bool](class_bool.md#class_bool) ) | virtual | const |
| [int](class_int.md#class_int) | [_get_height](class_texture2d.md#class_Texture2D_private_method__get_height) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_width](class_texture2d.md#class_Texture2D_private_method__get_width) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_has_alpha](class_texture2d.md#class_Texture2D_private_method__has_alpha) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_pixel_opaque](class_texture2d.md#class_Texture2D_private_method__is_pixel_opaque) ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) | virtual | const |
| [Resource](class_resource.md#class_Resource) | [create_placeholder](class_texture2d.md#class_Texture2D_method_create_placeholder) ( ) const |
| void | [draw](class_texture2d.md#class_Texture2D_method_draw) ( canvas_item: [RID](class_rid.md#class_RID), position: [Vector2](class_vector2.md#class_Vector2), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false ) const |
| void | [draw_rect](class_texture2d.md#class_Texture2D_method_draw_rect) ( canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), tile: [bool](class_bool.md#class_bool), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false ) const |
| void | [draw_rect_region](class_texture2d.md#class_Texture2D_method_draw_rect_region) ( canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false, clip_uv: [bool](class_bool.md#class_bool) = true ) const |
| [int](class_int.md#class_int) | [get_height](class_texture2d.md#class_Texture2D_method_get_height) ( ) const |
| [Image](class_image.md#class_Image) | [get_image](class_texture2d.md#class_Texture2D_method_get_image) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_size](class_texture2d.md#class_Texture2D_method_get_size) ( ) const |
| [int](class_int.md#class_int) | [get_width](class_texture2d.md#class_Texture2D_method_get_width) ( ) const |
| [bool](class_bool.md#class_bool) | [has_alpha](class_texture2d.md#class_Texture2D_method_has_alpha) ( ) const |

---

### Method Descriptions

<span id="class_Texture2D_private_method__draw"></span>

void **_draw** ( to_canvas_item: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), modulate: [Color](class_color.md#class_Color), transpose: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_texture2d.md#class_Texture2D_private_method__draw)

Called when the entire **Texture2D** is requested to be drawn over a [CanvasItem](class_canvasitem.md#class_CanvasItem), with the top-left offset specified in `pos`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

 **Note:** This is only used in 2D rendering, not 3D.

---

<span id="class_Texture2D_private_method__draw_rect"></span>

void **_draw_rect** ( to_canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), tile: [bool](class_bool.md#class_bool), modulate: [Color](class_color.md#class_Color), transpose: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_texture2d.md#class_Texture2D_private_method__draw_rect)

Called when the **Texture2D** is requested to be drawn onto [CanvasItem](class_canvasitem.md#class_CanvasItem)'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

 **Note:** This is only used in 2D rendering, not 3D.

---

<span id="class_Texture2D_private_method__draw_rect_region"></span>

void **_draw_rect_region** ( to_canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color), transpose: [bool](class_bool.md#class_bool), clip_uv: [bool](class_bool.md#class_bool) ) *virtual* *const* [🔗](class_texture2d.md#class_Texture2D_private_method__draw_rect_region)

Called when a part of the **Texture2D** specified by `src_rect`'s coordinates is requested to be drawn onto [CanvasItem](class_canvasitem.md#class_CanvasItem)'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

 **Note:** This is only used in 2D rendering, not 3D.

---

<span id="class_Texture2D_private_method__get_height"></span>

[int](class_int.md#class_int) **_get_height** ( ) *virtual* |required| *const* [🔗](class_texture2d.md#class_Texture2D_private_method__get_height)

Called when the **Texture2D**'s height is queried.

---

<span id="class_Texture2D_private_method__get_width"></span>

[int](class_int.md#class_int) **_get_width** ( ) *virtual* |required| *const* [🔗](class_texture2d.md#class_Texture2D_private_method__get_width)

Called when the **Texture2D**'s width is queried.

---

<span id="class_Texture2D_private_method__has_alpha"></span>

[bool](class_bool.md#class_bool) **_has_alpha** ( ) *virtual* *const* [🔗](class_texture2d.md#class_Texture2D_private_method__has_alpha)

Called when the presence of an alpha channel in the **Texture2D** is queried.

---

<span id="class_Texture2D_private_method__is_pixel_opaque"></span>

[bool](class_bool.md#class_bool) **_is_pixel_opaque** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_texture2d.md#class_Texture2D_private_method__is_pixel_opaque)

Called when a pixel's opaque state in the **Texture2D** is queried at the specified `(x, y)` position.

---

<span id="class_Texture2D_method_create_placeholder"></span>

[Resource](class_resource.md#class_Resource) **create_placeholder** ( ) *const* [🔗](class_texture2d.md#class_Texture2D_method_create_placeholder)

Creates a placeholder version of this resource ([PlaceholderTexture2D](class_placeholdertexture2d.md#class_PlaceholderTexture2D)).

---

<span id="class_Texture2D_method_draw"></span>

void **draw** ( canvas_item: [RID](class_rid.md#class_RID), position: [Vector2](class_vector2.md#class_Vector2), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_texture2d.md#class_Texture2D_method_draw)

Draws the texture using a [CanvasItem](class_canvasitem.md#class_CanvasItem) with the [RenderingServer](class_renderingserver.md#class_RenderingServer) API at the specified `position`.

---

<span id="class_Texture2D_method_draw_rect"></span>

void **draw_rect** ( canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), tile: [bool](class_bool.md#class_bool), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_texture2d.md#class_Texture2D_method_draw_rect)

Draws the texture using a [CanvasItem](class_canvasitem.md#class_CanvasItem) with the [RenderingServer](class_renderingserver.md#class_RenderingServer) API.

---

<span id="class_Texture2D_method_draw_rect_region"></span>

void **draw_rect_region** ( canvas_item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false, clip_uv: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_texture2d.md#class_Texture2D_method_draw_rect_region)

Draws a part of the texture using a [CanvasItem](class_canvasitem.md#class_CanvasItem) with the [RenderingServer](class_renderingserver.md#class_RenderingServer) API.

---

<span id="class_Texture2D_method_get_height"></span>

[int](class_int.md#class_int) **get_height** ( ) *const* [🔗](class_texture2d.md#class_Texture2D_method_get_height)

Returns the texture height in pixels.

---

<span id="class_Texture2D_method_get_image"></span>

[Image](class_image.md#class_Image) **get_image** ( ) *const* [🔗](class_texture2d.md#class_Texture2D_method_get_image)

Returns an [Image](class_image.md#class_Image) that is a copy of data from this **Texture2D** (a new [Image](class_image.md#class_Image) is created each time). [Image](class_image.md#class_Image) s can be accessed and manipulated directly.

 **Note:** This will return `null` if this **Texture2D** is invalid.

 **Note:** This will fetch the texture data from the GPU, which might cause performance problems when overused. Avoid calling [get_image()](class_texture2d.md#class_Texture2D_method_get_image) every frame, especially on large textures.

---

<span id="class_Texture2D_method_get_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_size** ( ) *const* [🔗](class_texture2d.md#class_Texture2D_method_get_size)

Returns the texture size in pixels.

---

<span id="class_Texture2D_method_get_width"></span>

[int](class_int.md#class_int) **get_width** ( ) *const* [🔗](class_texture2d.md#class_Texture2D_method_get_width)

Returns the texture width in pixels.

---

<span id="class_Texture2D_method_has_alpha"></span>

[bool](class_bool.md#class_bool) **has_alpha** ( ) *const* [🔗](class_texture2d.md#class_Texture2D_method_has_alpha)

Returns `true` if this **Texture2D** has an alpha channel.
