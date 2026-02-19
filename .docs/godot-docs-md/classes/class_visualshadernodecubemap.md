<span id="class_VisualShaderNodeCubemap"></span>

## VisualShaderNodeCubemap

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Cubemap](class_cubemap.md#class_Cubemap) sampling node to be used within the visual shader graph.

### Description

Translated to `texture(cubemap, vec3)` in the shader language. Returns a color vector and alpha channel as scalar.

### Properties


| [TextureLayered](class_texturelayered.md#class_TextureLayered) | [cube_map](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_cube_map) |
| --- | --- |
| [Source](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_Source) | [source](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_source) | `0` |
| [TextureType](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType) | [texture_type](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_texture_type) | `0` |

---

### Enumerations

<span id="enum_VisualShaderNodeCubemap_Source"></span>

enum **Source**: [🔗](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_Source)

<span id="class_VisualShaderNodeCubemap_constant_SOURCE_TEXTURE"></span>

[Source](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_Source) **SOURCE_TEXTURE** = `0`

Use the [Cubemap](class_cubemap.md#class_Cubemap) set via [cube_map](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_cube_map). If this is set to [source](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_source), the `samplerCube` port is ignored.

<span id="class_VisualShaderNodeCubemap_constant_SOURCE_PORT"></span>

[Source](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_Source) **SOURCE_PORT** = `1`

Use the [Cubemap](class_cubemap.md#class_Cubemap) sampler reference passed via the `samplerCube` port. If this is set to [source](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_source), the [cube_map](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_cube_map) texture is ignored.

<span id="class_VisualShaderNodeCubemap_constant_SOURCE_MAX"></span>

[Source](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_Source) **SOURCE_MAX** = `2`

Represents the size of the [Source](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_Source) enum.

---

<span id="enum_VisualShaderNodeCubemap_TextureType"></span>

enum **TextureType**: [🔗](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType)

<span id="class_VisualShaderNodeCubemap_constant_TYPE_DATA"></span>

[TextureType](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType) **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

<span id="class_VisualShaderNodeCubemap_constant_TYPE_COLOR"></span>

[TextureType](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType) **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper conversion from nonlinear sRGB encoding to linear encoding.

<span id="class_VisualShaderNodeCubemap_constant_TYPE_NORMAL_MAP"></span>

[TextureType](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType) **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally converts the texture for proper usage as normal map.

<span id="class_VisualShaderNodeCubemap_constant_TYPE_MAX"></span>

[TextureType](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType) **TYPE_MAX** = `3`

Represents the size of the [TextureType](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeCubemap_property_cube_map"></span>

[TextureLayered](class_texturelayered.md#class_TextureLayered) **cube_map** [🔗](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_cube_map)

- void **set_cube_map** ( value: [TextureLayered](class_texturelayered.md#class_TextureLayered) )
- [TextureLayered](class_texturelayered.md#class_TextureLayered) **get_cube_map** ( )

The [Cubemap](class_cubemap.md#class_Cubemap) texture to sample when using [SOURCE_TEXTURE](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_constant_SOURCE_TEXTURE) as [source](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_source).

---

<span id="class_VisualShaderNodeCubemap_property_source"></span>

[Source](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_Source) **source** = `0` [🔗](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_source)

- void **set_source** ( value: [Source](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_Source) )
- [Source](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_Source) **get_source** ( )

Defines which source should be used for the sampling.

---

<span id="class_VisualShaderNodeCubemap_property_texture_type"></span>

[TextureType](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType) **texture_type** = `0` [🔗](class_visualshadernodecubemap.md#class_VisualShaderNodeCubemap_property_texture_type)

- void **set_texture_type** ( value: [TextureType](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType) )
- [TextureType](class_visualshadernodecubemap.md#enum_VisualShaderNodeCubemap_TextureType) **get_texture_type** ( )

Defines the type of data provided by the source texture.
