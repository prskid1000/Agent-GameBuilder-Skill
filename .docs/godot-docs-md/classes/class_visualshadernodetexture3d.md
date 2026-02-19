<span id="class_VisualShaderNodeTexture3D"></span>

## VisualShaderNodeTexture3D

**Inherits:** [VisualShaderNodeSample3D](class_visualshadernodesample3d.md#class_VisualShaderNodeSample3D) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Performs a 3D texture lookup within the visual shader graph.

### Description

Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.

### Properties


| [Texture3D](class_texture3d.md#class_Texture3D) | [texture](class_visualshadernodetexture3d.md#class_VisualShaderNodeTexture3D_property_texture) |
| --- | --- |

---

### Property Descriptions

<span id="class_VisualShaderNodeTexture3D_property_texture"></span>

[Texture3D](class_texture3d.md#class_Texture3D) **texture** [🔗](class_visualshadernodetexture3d.md#class_VisualShaderNodeTexture3D_property_texture)

- void **set_texture** ( value: [Texture3D](class_texture3d.md#class_Texture3D) )
- [Texture3D](class_texture3d.md#class_Texture3D) **get_texture** ( )

A source texture. Used if [VisualShaderNodeSample3D.source](class_visualshadernodesample3d.md#class_VisualShaderNodeSample3D_property_source) is set to [VisualShaderNodeSample3D.SOURCE_TEXTURE](class_visualshadernodesample3d.md#class_VisualShaderNodeSample3D_constant_SOURCE_TEXTURE).
