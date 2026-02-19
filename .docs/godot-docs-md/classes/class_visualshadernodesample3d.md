<span id="class_VisualShaderNodeSample3D"></span>

## VisualShaderNodeSample3D

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeTexture2DArray](class_visualshadernodetexture2darray.md#class_VisualShaderNodeTexture2DArray), [VisualShaderNodeTexture3D](class_visualshadernodetexture3d.md#class_VisualShaderNodeTexture3D)

A base node for nodes which samples 3D textures in the visual shader graph.

### Description

A virtual class, use the descendants instead.

### Properties


| [Source](class_visualshadernodesample3d.md#enum_VisualShaderNodeSample3D_Source) | [source](class_visualshadernodesample3d.md#class_VisualShaderNodeSample3D_property_source) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeSample3D_Source"></span>

enum **Source**: [🔗](class_visualshadernodesample3d.md#enum_VisualShaderNodeSample3D_Source)

<span id="class_VisualShaderNodeSample3D_constant_SOURCE_TEXTURE"></span>

[Source](class_visualshadernodesample3d.md#enum_VisualShaderNodeSample3D_Source) **SOURCE_TEXTURE** = `0`

Creates internal uniform and provides a way to assign it within node.

<span id="class_VisualShaderNodeSample3D_constant_SOURCE_PORT"></span>

[Source](class_visualshadernodesample3d.md#enum_VisualShaderNodeSample3D_Source) **SOURCE_PORT** = `1`

Use the uniform texture from sampler port.

<span id="class_VisualShaderNodeSample3D_constant_SOURCE_MAX"></span>

[Source](class_visualshadernodesample3d.md#enum_VisualShaderNodeSample3D_Source) **SOURCE_MAX** = `2`

Represents the size of the [Source](class_visualshadernodesample3d.md#enum_VisualShaderNodeSample3D_Source) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeSample3D_property_source"></span>

[Source](class_visualshadernodesample3d.md#enum_VisualShaderNodeSample3D_Source) **source** = `0` [🔗](class_visualshadernodesample3d.md#class_VisualShaderNodeSample3D_property_source)

- void **set_source** ( value: [Source](class_visualshadernodesample3d.md#enum_VisualShaderNodeSample3D_Source) )
- [Source](class_visualshadernodesample3d.md#enum_VisualShaderNodeSample3D_Source) **get_source** ( )

An input source type.
