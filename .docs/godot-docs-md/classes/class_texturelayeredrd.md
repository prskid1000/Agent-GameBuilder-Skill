<span id="class_TextureLayeredRD"></span>

## TextureLayeredRD

**Inherits:** [TextureLayered](class_texturelayered.md#class_TextureLayered) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [Texture2DArrayRD](class_texture2darrayrd.md#class_Texture2DArrayRD), [TextureCubemapArrayRD](class_texturecubemaparrayrd.md#class_TextureCubemapArrayRD), [TextureCubemapRD](class_texturecubemaprd.md#class_TextureCubemapRD)

Abstract base class for layered texture RD types.

### Description

Base class for [Texture2DArrayRD](class_texture2darrayrd.md#class_Texture2DArrayRD), [TextureCubemapRD](class_texturecubemaprd.md#class_TextureCubemapRD) and [TextureCubemapArrayRD](class_texturecubemaparrayrd.md#class_TextureCubemapArrayRD). Cannot be used directly, but contains all the functions necessary for accessing the derived resource types.

 **Note:** **TextureLayeredRD** is intended for low-level usage with [RenderingDevice](class_renderingdevice.md#class_RenderingDevice). For most use cases, use [TextureLayered](class_texturelayered.md#class_TextureLayered) instead.

### Tutorials

- Compute Texture demo

### Properties


| [RID](class_rid.md#class_RID) | [texture_rd_rid](class_texturelayeredrd.md#class_TextureLayeredRD_property_texture_rd_rid) |
| --- | --- |

---

### Property Descriptions

<span id="class_TextureLayeredRD_property_texture_rd_rid"></span>

[RID](class_rid.md#class_RID) **texture_rd_rid** [🔗](class_texturelayeredrd.md#class_TextureLayeredRD_property_texture_rd_rid)

- void **set_texture_rd_rid** ( value: [RID](class_rid.md#class_RID) )
- [RID](class_rid.md#class_RID) **get_texture_rd_rid** ( )

The RID of the texture object created on the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).
