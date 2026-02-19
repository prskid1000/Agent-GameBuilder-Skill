<span id="class_VisualShaderNodeTextureParameter"></span>

## VisualShaderNodeTextureParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeCubemapParameter](class_visualshadernodecubemapparameter.md#class_VisualShaderNodeCubemapParameter), [VisualShaderNodeTexture2DArrayParameter](class_visualshadernodetexture2darrayparameter.md#class_VisualShaderNodeTexture2DArrayParameter), [VisualShaderNodeTexture2DParameter](class_visualshadernodetexture2dparameter.md#class_VisualShaderNodeTexture2DParameter), [VisualShaderNodeTexture3DParameter](class_visualshadernodetexture3dparameter.md#class_VisualShaderNodeTexture3DParameter), [VisualShaderNodeTextureParameterTriplanar](class_visualshadernodetextureparametertriplanar.md#class_VisualShaderNodeTextureParameterTriplanar)

Performs a uniform texture lookup within the visual shader graph.

### Description

Performs a lookup operation on the texture provided as a uniform for the shader.

### Properties


| [ColorDefault](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault) | [color_default](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_color_default) | `0` |
| --- | --- | --- |
| [TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) | [texture_filter](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_texture_filter) | `0` |
| [TextureRepeat](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat) | [texture_repeat](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_texture_repeat) | `0` |
| [TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) | [texture_source](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_texture_source) | `0` |
| [TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) | [texture_type](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_texture_type) | `0` |

---

### Enumerations

<span id="enum_VisualShaderNodeTextureParameter_TextureType"></span>

enum **TextureType**: [🔗](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType)

<span id="class_VisualShaderNodeTextureParameter_constant_TYPE_DATA"></span>

[TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

<span id="class_VisualShaderNodeTextureParameter_constant_TYPE_COLOR"></span>

[TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper conversion from nonlinear sRGB encoding to linear encoding.

<span id="class_VisualShaderNodeTextureParameter_constant_TYPE_NORMAL_MAP"></span>

[TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally converts the texture for proper usage as normal map.

<span id="class_VisualShaderNodeTextureParameter_constant_TYPE_ANISOTROPY"></span>

[TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) **TYPE_ANISOTROPY** = `3`

Adds `hint_anisotropy` as hint to the uniform declaration to use for a flowmap.

<span id="class_VisualShaderNodeTextureParameter_constant_TYPE_MAX"></span>

[TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) **TYPE_MAX** = `4`

Represents the size of the [TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) enum.

---

<span id="enum_VisualShaderNodeTextureParameter_ColorDefault"></span>

enum **ColorDefault**: [🔗](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault)

<span id="class_VisualShaderNodeTextureParameter_constant_COLOR_DEFAULT_WHITE"></span>

[ColorDefault](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault) **COLOR_DEFAULT_WHITE** = `0`

Defaults to fully opaque white color.

<span id="class_VisualShaderNodeTextureParameter_constant_COLOR_DEFAULT_BLACK"></span>

[ColorDefault](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault) **COLOR_DEFAULT_BLACK** = `1`

Defaults to fully opaque black color.

<span id="class_VisualShaderNodeTextureParameter_constant_COLOR_DEFAULT_TRANSPARENT"></span>

[ColorDefault](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault) **COLOR_DEFAULT_TRANSPARENT** = `2`

Defaults to fully transparent black color.

<span id="class_VisualShaderNodeTextureParameter_constant_COLOR_DEFAULT_MAX"></span>

[ColorDefault](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault) **COLOR_DEFAULT_MAX** = `3`

Represents the size of the [ColorDefault](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault) enum.

---

<span id="enum_VisualShaderNodeTextureParameter_TextureFilter"></span>

enum **TextureFilter**: [🔗](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter)

<span id="class_VisualShaderNodeTextureParameter_constant_FILTER_DEFAULT"></span>

[TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **FILTER_DEFAULT** = `0`

Sample the texture using the filter determined by the node this shader is attached to.

<span id="class_VisualShaderNodeTextureParameter_constant_FILTER_NEAREST"></span>

[TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **FILTER_NEAREST** = `1`

The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).

<span id="class_VisualShaderNodeTextureParameter_constant_FILTER_LINEAR"></span>

[TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **FILTER_LINEAR** = `2`

The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).

<span id="class_VisualShaderNodeTextureParameter_constant_FILTER_NEAREST_MIPMAP"></span>

[TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **FILTER_NEAREST_MIPMAP** = `3`

The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`). This makes the texture look pixelated from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class_Camera2D) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<span id="class_VisualShaderNodeTextureParameter_constant_FILTER_LINEAR_MIPMAP"></span>

[TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **FILTER_LINEAR_MIPMAP** = `4`

The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`). This makes the texture look smooth from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class_Camera2D) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<span id="class_VisualShaderNodeTextureParameter_constant_FILTER_NEAREST_MIPMAP_ANISOTROPIC"></span>

[TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **FILTER_NEAREST_MIPMAP_ANISOTROPIC** = `5`

The texture filter reads from the nearest pixel and blends between 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`) based on the angle between the surface and the camera view. This makes the texture look pixelated from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

 **Note:** This texture filter is rarely useful in 2D projects. [FILTER_NEAREST_MIPMAP](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_constant_FILTER_NEAREST_MIPMAP) is usually more appropriate in this case.

<span id="class_VisualShaderNodeTextureParameter_constant_FILTER_LINEAR_MIPMAP_ANISOTROPIC"></span>

[TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **FILTER_LINEAR_MIPMAP_ANISOTROPIC** = `6`

The texture filter blends between the nearest 4 pixels and blends between 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`) based on the angle between the surface and the camera view. This makes the texture look smooth from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

 **Note:** This texture filter is rarely useful in 2D projects. [FILTER_LINEAR_MIPMAP](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_constant_FILTER_LINEAR_MIPMAP) is usually more appropriate in this case.

<span id="class_VisualShaderNodeTextureParameter_constant_FILTER_MAX"></span>

[TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **FILTER_MAX** = `7`

Represents the size of the [TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) enum.

---

<span id="enum_VisualShaderNodeTextureParameter_TextureRepeat"></span>

enum **TextureRepeat**: [🔗](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat)

<span id="class_VisualShaderNodeTextureParameter_constant_REPEAT_DEFAULT"></span>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat) **REPEAT_DEFAULT** = `0`

Sample the texture using the repeat mode determined by the node this shader is attached to.

<span id="class_VisualShaderNodeTextureParameter_constant_REPEAT_ENABLED"></span>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat) **REPEAT_ENABLED** = `1`

Texture will repeat normally.

<span id="class_VisualShaderNodeTextureParameter_constant_REPEAT_DISABLED"></span>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat) **REPEAT_DISABLED** = `2`

Texture will not repeat.

<span id="class_VisualShaderNodeTextureParameter_constant_REPEAT_MAX"></span>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat) **REPEAT_MAX** = `3`

Represents the size of the [TextureRepeat](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat) enum.

---

<span id="enum_VisualShaderNodeTextureParameter_TextureSource"></span>

enum **TextureSource**: [🔗](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource)

<span id="class_VisualShaderNodeTextureParameter_constant_SOURCE_NONE"></span>

[TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) **SOURCE_NONE** = `0`

The texture source is not specified in the shader.

<span id="class_VisualShaderNodeTextureParameter_constant_SOURCE_SCREEN"></span>

[TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) **SOURCE_SCREEN** = `1`

The texture source is the screen texture which captures all opaque objects drawn this frame.

<span id="class_VisualShaderNodeTextureParameter_constant_SOURCE_DEPTH"></span>

[TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) **SOURCE_DEPTH** = `2`

The texture source is the depth texture from the depth prepass.

<span id="class_VisualShaderNodeTextureParameter_constant_SOURCE_NORMAL_ROUGHNESS"></span>

[TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) **SOURCE_NORMAL_ROUGHNESS** = `3`

The texture source is the normal-roughness buffer from the depth prepass.

<span id="class_VisualShaderNodeTextureParameter_constant_SOURCE_MAX"></span>

[TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) **SOURCE_MAX** = `4`

Represents the size of the [TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeTextureParameter_property_color_default"></span>

[ColorDefault](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault) **color_default** = `0` [🔗](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_color_default)

- void **set_color_default** ( value: [ColorDefault](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault) )
- [ColorDefault](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_ColorDefault) **get_color_default** ( )

Sets the default color if no texture is assigned to the uniform.

---

<span id="class_VisualShaderNodeTextureParameter_property_texture_filter"></span>

[TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **texture_filter** = `0` [🔗](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_texture_filter)

- void **set_texture_filter** ( value: [TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) )
- [TextureFilter](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureFilter) **get_texture_filter** ( )

Sets the texture filtering mode.

---

<span id="class_VisualShaderNodeTextureParameter_property_texture_repeat"></span>

[TextureRepeat](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat) **texture_repeat** = `0` [🔗](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_texture_repeat)

- void **set_texture_repeat** ( value: [TextureRepeat](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat) )
- [TextureRepeat](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureRepeat) **get_texture_repeat** ( )

Sets the texture repeating mode.

---

<span id="class_VisualShaderNodeTextureParameter_property_texture_source"></span>

[TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) **texture_source** = `0` [🔗](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_texture_source)

- void **set_texture_source** ( value: [TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) )
- [TextureSource](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureSource) **get_texture_source** ( )

Sets the texture source mode. Used for reading from the screen, depth, or normal_roughness texture.

---

<span id="class_VisualShaderNodeTextureParameter_property_texture_type"></span>

[TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) **texture_type** = `0` [🔗](class_visualshadernodetextureparameter.md#class_VisualShaderNodeTextureParameter_property_texture_type)

- void **set_texture_type** ( value: [TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) )
- [TextureType](class_visualshadernodetextureparameter.md#enum_VisualShaderNodeTextureParameter_TextureType) **get_texture_type** ( )

Defines the type of data provided by the source texture.
