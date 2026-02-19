<span id="class_CanvasTexture"></span>

## CanvasTexture

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture with optional normal and specular maps for use in 2D rendering.

### Description

**CanvasTexture** is an alternative to [ImageTexture](class_imagetexture.md#class_ImageTexture) for 2D rendering. It allows using normal maps and specular maps in any node that inherits from [CanvasItem](class_canvasitem.md#class_CanvasItem). **CanvasTexture** also allows overriding the texture's filter and repeat mode independently of the node's properties (or the project settings).

 **Note:** **CanvasTexture** cannot be used in 3D. It will not display correctly when applied to any [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D), such as [Sprite3D](class_sprite3d.md#class_Sprite3D) or [Decal](class_decal.md#class_Decal). For physically-based materials in 3D, use [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D) instead.

### Tutorials

- [2D Lights and Shadows](../tutorials/2d/2d_lights_and_shadows.md)

### Properties


| [Texture2D](class_texture2d.md#class_Texture2D) | [diffuse_texture](class_canvastexture.md#class_CanvasTexture_property_diffuse_texture) |
| --- | --- |
| [Texture2D](class_texture2d.md#class_Texture2D) | [normal_texture](class_canvastexture.md#class_CanvasTexture_property_normal_texture) |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| [Color](class_color.md#class_Color) | [specular_color](class_canvastexture.md#class_CanvasTexture_property_specular_color) | `Color(1, 1, 1, 1)` |
| [float](class_float.md#class_float) | [specular_shininess](class_canvastexture.md#class_CanvasTexture_property_specular_shininess) | `1.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [specular_texture](class_canvastexture.md#class_CanvasTexture_property_specular_texture) |
| [TextureFilter](class_canvasitem.md#enum_CanvasItem_TextureFilter) | [texture_filter](class_canvastexture.md#class_CanvasTexture_property_texture_filter) | `0` |
| [TextureRepeat](class_canvasitem.md#enum_CanvasItem_TextureRepeat) | [texture_repeat](class_canvastexture.md#class_CanvasTexture_property_texture_repeat) | `0` |

---

### Property Descriptions

<span id="class_CanvasTexture_property_diffuse_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **diffuse_texture** [🔗](class_canvastexture.md#class_CanvasTexture_property_diffuse_texture)

- void **set_diffuse_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_diffuse_texture** ( )

The diffuse (color) texture to use. This is the main texture you want to set in most cases.

---

<span id="class_CanvasTexture_property_normal_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **normal_texture** [🔗](class_canvastexture.md#class_CanvasTexture_property_normal_texture)

- void **set_normal_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_normal_texture** ( )

The normal map texture to use. Only has a visible effect if [Light2D](class_light2d.md#class_Light2D) s are affecting this **CanvasTexture**.

 **Note:** Godot expects the normal map to use X+, Y+, and Z+ coordinates. See this page for a comparison of normal map coordinates expected by popular engines.

---

<span id="class_CanvasTexture_property_specular_color"></span>

[Color](class_color.md#class_Color) **specular_color** = `Color(1, 1, 1, 1)` [🔗](class_canvastexture.md#class_CanvasTexture_property_specular_color)

- void **set_specular_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_specular_color** ( )

The multiplier for specular reflection colors. The [Light2D](class_light2d.md#class_Light2D)'s color is also taken into account when determining the reflection color. Only has a visible effect if [Light2D](class_light2d.md#class_Light2D) s are affecting this **CanvasTexture**.

---

<span id="class_CanvasTexture_property_specular_shininess"></span>

[float](class_float.md#class_float) **specular_shininess** = `1.0` [🔗](class_canvastexture.md#class_CanvasTexture_property_specular_shininess)

- void **set_specular_shininess** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_specular_shininess** ( )

The specular exponent for [Light2D](class_light2d.md#class_Light2D) specular reflections. Higher values result in a more glossy/"wet" look, with reflections becoming more localized and less visible overall. The default value of `1.0` disables specular reflections entirely. Only has a visible effect if [Light2D](class_light2d.md#class_Light2D) s are affecting this **CanvasTexture**.

---

<span id="class_CanvasTexture_property_specular_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **specular_texture** [🔗](class_canvastexture.md#class_CanvasTexture_property_specular_texture)

- void **set_specular_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_specular_texture** ( )

The specular map to use for [Light2D](class_light2d.md#class_Light2D) specular reflections. This should be a grayscale or colored texture, with brighter areas resulting in a higher [specular_shininess](class_canvastexture.md#class_CanvasTexture_property_specular_shininess) value. Using a colored [specular_texture](class_canvastexture.md#class_CanvasTexture_property_specular_texture) allows controlling specular shininess on a per-channel basis. Only has a visible effect if [Light2D](class_light2d.md#class_Light2D) s are affecting this **CanvasTexture**.

---

<span id="class_CanvasTexture_property_texture_filter"></span>

[TextureFilter](class_canvasitem.md#enum_CanvasItem_TextureFilter) **texture_filter** = `0` [🔗](class_canvastexture.md#class_CanvasTexture_property_texture_filter)

- void **set_texture_filter** ( value: [TextureFilter](class_canvasitem.md#enum_CanvasItem_TextureFilter) )
- [TextureFilter](class_canvasitem.md#enum_CanvasItem_TextureFilter) **get_texture_filter** ( )

The texture filtering mode to use when drawing this **CanvasTexture**.

---

<span id="class_CanvasTexture_property_texture_repeat"></span>

[TextureRepeat](class_canvasitem.md#enum_CanvasItem_TextureRepeat) **texture_repeat** = `0` [🔗](class_canvastexture.md#class_CanvasTexture_property_texture_repeat)

- void **set_texture_repeat** ( value: [TextureRepeat](class_canvasitem.md#enum_CanvasItem_TextureRepeat) )
- [TextureRepeat](class_canvasitem.md#enum_CanvasItem_TextureRepeat) **get_texture_repeat** ( )

The texture repeat mode to use when drawing this **CanvasTexture**.
