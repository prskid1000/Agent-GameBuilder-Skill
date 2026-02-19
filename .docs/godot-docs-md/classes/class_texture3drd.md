<span id="class_Texture3DRD"></span>

## Texture3DRD

**Inherits:** [Texture3D](class_texture3d.md#class_Texture3D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture for 3D that is bound to a texture created on the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Description

This texture class allows you to use a 3D texture created directly on the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) as a texture for materials, meshes, etc.

 **Note:** **Texture3DRD** is intended for low-level usage with [RenderingDevice](class_renderingdevice.md#class_RenderingDevice). For most use cases, use [Texture3D](class_texture3d.md#class_Texture3D) instead.

### Tutorials

- Compute Texture demo

### Properties


| [RID](class_rid.md#class_RID) | [texture_rd_rid](class_texture3drd.md#class_Texture3DRD_property_texture_rd_rid) |
| --- | --- |

---

### Property Descriptions

<span id="class_Texture3DRD_property_texture_rd_rid"></span>

[RID](class_rid.md#class_RID) **texture_rd_rid** [🔗](class_texture3drd.md#class_Texture3DRD_property_texture_rd_rid)

- void **set_texture_rd_rid** ( value: [RID](class_rid.md#class_RID) )
- [RID](class_rid.md#class_RID) **get_texture_rd_rid** ( )

The RID of the texture object created on the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).
