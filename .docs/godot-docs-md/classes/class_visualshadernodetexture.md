<span id="class_VisualShaderNodeTexture"></span>

## VisualShaderNodeTexture

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Performs a 2D texture lookup within the visual shader graph.

### Description

Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.

### Properties


| [Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) | [source](class_visualshadernodetexture.md#class_VisualShaderNodeTexture_property_source) | `0` |
| --- | --- | --- |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_visualshadernodetexture.md#class_VisualShaderNodeTexture_property_texture) |
| [TextureType](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType) | [texture_type](class_visualshadernodetexture.md#class_VisualShaderNodeTexture_property_texture_type) | `0` |

---

### Enumerations

<span id="enum_VisualShaderNodeTexture_Source"></span>

enum **Source**: [🔗](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source)

<span id="class_VisualShaderNodeTexture_constant_SOURCE_TEXTURE"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **SOURCE_TEXTURE** = `0`

Use the texture given as an argument for this function.

<span id="class_VisualShaderNodeTexture_constant_SOURCE_SCREEN"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **SOURCE_SCREEN** = `1`

Use the current viewport's texture as the source.

<span id="class_VisualShaderNodeTexture_constant_SOURCE_2D_TEXTURE"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **SOURCE_2D_TEXTURE** = `2`

Use the texture from this shader's texture built-in (e.g. a texture of a [Sprite2D](class_sprite2d.md#class_Sprite2D)).

<span id="class_VisualShaderNodeTexture_constant_SOURCE_2D_NORMAL"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **SOURCE_2D_NORMAL** = `3`

Use the texture from this shader's normal map built-in.

<span id="class_VisualShaderNodeTexture_constant_SOURCE_DEPTH"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **SOURCE_DEPTH** = `4`

Use the depth texture captured during the depth prepass. Only available when the depth prepass is used (i.e. in spatial shaders and in the forward_plus or gl_compatibility renderers).

<span id="class_VisualShaderNodeTexture_constant_SOURCE_PORT"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **SOURCE_PORT** = `5`

Use the texture provided in the input port for this function.

<span id="class_VisualShaderNodeTexture_constant_SOURCE_3D_NORMAL"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **SOURCE_3D_NORMAL** = `6`

Use the normal buffer captured during the depth prepass. Only available when the normal-roughness buffer is available (i.e. in spatial shaders and in the forward_plus renderer).

<span id="class_VisualShaderNodeTexture_constant_SOURCE_ROUGHNESS"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **SOURCE_ROUGHNESS** = `7`

Use the roughness buffer captured during the depth prepass. Only available when the normal-roughness buffer is available (i.e. in spatial shaders and in the forward_plus renderer).

<span id="class_VisualShaderNodeTexture_constant_SOURCE_MAX"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **SOURCE_MAX** = `8`

Represents the size of the [Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) enum.

---

<span id="enum_VisualShaderNodeTexture_TextureType"></span>

enum **TextureType**: [🔗](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType)

<span id="class_VisualShaderNodeTexture_constant_TYPE_DATA"></span>

[TextureType](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType) **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

<span id="class_VisualShaderNodeTexture_constant_TYPE_COLOR"></span>

[TextureType](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType) **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper conversion from nonlinear sRGB encoding to linear encoding.

<span id="class_VisualShaderNodeTexture_constant_TYPE_NORMAL_MAP"></span>

[TextureType](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType) **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally converts the texture for proper usage as normal map.

<span id="class_VisualShaderNodeTexture_constant_TYPE_MAX"></span>

[TextureType](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType) **TYPE_MAX** = `3`

Represents the size of the [TextureType](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeTexture_property_source"></span>

[Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **source** = `0` [🔗](class_visualshadernodetexture.md#class_VisualShaderNodeTexture_property_source)

- void **set_source** ( value: [Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) )
- [Source](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_Source) **get_source** ( )

Determines the source for the lookup.

---

<span id="class_VisualShaderNodeTexture_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_visualshadernodetexture.md#class_VisualShaderNodeTexture_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

The source texture, if needed for the selected [source](class_visualshadernodetexture.md#class_VisualShaderNodeTexture_property_source).

---

<span id="class_VisualShaderNodeTexture_property_texture_type"></span>

[TextureType](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType) **texture_type** = `0` [🔗](class_visualshadernodetexture.md#class_VisualShaderNodeTexture_property_texture_type)

- void **set_texture_type** ( value: [TextureType](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType) )
- [TextureType](class_visualshadernodetexture.md#enum_VisualShaderNodeTexture_TextureType) **get_texture_type** ( )

Specifies the type of the texture if [source](class_visualshadernodetexture.md#class_VisualShaderNodeTexture_property_source) is set to [SOURCE_TEXTURE](class_visualshadernodetexture.md#class_VisualShaderNodeTexture_constant_SOURCE_TEXTURE).
