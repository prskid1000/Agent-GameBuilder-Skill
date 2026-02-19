<span id="class_VisualShaderNodeTexture2DArray"></span>

## VisualShaderNodeTexture2DArray

**Inherits:** [VisualShaderNodeSample3D](class_visualshadernodesample3d.md#class_VisualShaderNodeSample3D) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 2D texture uniform array to be used within the visual shader graph.

### Description

Translated to `uniform sampler2DArray` in the shader language.

### Properties


| [TextureLayered](class_texturelayered.md#class_TextureLayered) | [texture_array](class_visualshadernodetexture2darray.md#class_VisualShaderNodeTexture2DArray_property_texture_array) |
| --- | --- |

---

### Property Descriptions

<span id="class_VisualShaderNodeTexture2DArray_property_texture_array"></span>

[TextureLayered](class_texturelayered.md#class_TextureLayered) **texture_array** [🔗](class_visualshadernodetexture2darray.md#class_VisualShaderNodeTexture2DArray_property_texture_array)

- void **set_texture_array** ( value: [TextureLayered](class_texturelayered.md#class_TextureLayered) )
- [TextureLayered](class_texturelayered.md#class_TextureLayered) **get_texture_array** ( )

A source texture array. Used if [VisualShaderNodeSample3D.source](class_visualshadernodesample3d.md#class_VisualShaderNodeSample3D_property_source) is set to [VisualShaderNodeSample3D.SOURCE_TEXTURE](class_visualshadernodesample3d.md#class_VisualShaderNodeSample3D_constant_SOURCE_TEXTURE).
