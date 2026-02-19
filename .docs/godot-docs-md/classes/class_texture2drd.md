<span id="class_Texture2DRD"></span>

## Texture2DRD

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture for 2D that is bound to a texture created on the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Description

This texture class allows you to use a 2D texture created directly on the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) as a texture for materials, meshes, etc.

 **Note:** **Texture2DRD** is intended for low-level usage with [RenderingDevice](class_renderingdevice.md#class_RenderingDevice). For most use cases, use [Texture2D](class_texture2d.md#class_Texture2D) instead.

### Tutorials

- Compute Texture demo

### Properties


| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| --- | --- | --- |
| [RID](class_rid.md#class_RID) | [texture_rd_rid](class_texture2drd.md#class_Texture2DRD_property_texture_rd_rid) |

---

### Property Descriptions

<span id="class_Texture2DRD_property_texture_rd_rid"></span>

[RID](class_rid.md#class_RID) **texture_rd_rid** [🔗](class_texture2drd.md#class_Texture2DRD_property_texture_rd_rid)

- void **set_texture_rd_rid** ( value: [RID](class_rid.md#class_RID) )
- [RID](class_rid.md#class_RID) **get_texture_rd_rid** ( )

The RID of the texture object created on the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).
