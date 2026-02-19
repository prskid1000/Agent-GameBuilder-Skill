<span id="class_CompressedTextureLayered"></span>

## CompressedTextureLayered

**Inherits:** [TextureLayered](class_texturelayered.md#class_TextureLayered) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CompressedCubemap](class_compressedcubemap.md#class_CompressedCubemap), [CompressedCubemapArray](class_compressedcubemaparray.md#class_CompressedCubemapArray), [CompressedTexture2DArray](class_compressedtexture2darray.md#class_CompressedTexture2DArray)

Base class for texture arrays that can optionally be compressed.

### Description

Base class for [CompressedTexture2DArray](class_compressedtexture2darray.md#class_CompressedTexture2DArray) and [CompressedTexture3D](class_compressedtexture3d.md#class_CompressedTexture3D). Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also [TextureLayered](class_texturelayered.md#class_TextureLayered).

### Properties


| [String](class_string.md#class_String) | [load_path](class_compressedtexturelayered.md#class_CompressedTextureLayered_property_load_path) | `""` |
| --- | --- | --- |

### Methods


| Error | [load](class_compressedtexturelayered.md#class_CompressedTextureLayered_method_load) ( path: [String](class_string.md#class_String) ) |
| --- | --- |

---

### Property Descriptions

<span id="class_CompressedTextureLayered_property_load_path"></span>

[String](class_string.md#class_String) **load_path** = `""` [🔗](class_compressedtexturelayered.md#class_CompressedTextureLayered_property_load_path)

- Error **load** ( path: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_load_path** ( )

The path the texture should be loaded from.

---

### Method Descriptions

<span id="class_CompressedTextureLayered_method_load"></span>

Error **load** ( path: [String](class_string.md#class_String) ) [🔗](class_compressedtexturelayered.md#class_CompressedTextureLayered_method_load)

Loads the texture at `path`.
