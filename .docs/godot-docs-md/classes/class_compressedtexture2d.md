<span id="class_CompressedTexture2D"></span>

## CompressedTexture2D

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture with 2 dimensions, optionally compressed.

### Description

A texture that is loaded from a `.ctex` file. This file format is internal to Godot; it is created by importing other image formats with the import system. **CompressedTexture2D** can use one of 4 compression methods (including a lack of any compression):

- Lossless (WebP or PNG, uncompressed on the GPU)

- Lossy (WebP, uncompressed on the GPU)

- VRAM Compressed (compressed on the GPU)

- VRAM Uncompressed (uncompressed on the GPU)

- Basis Universal (compressed on the GPU. Lower file sizes than VRAM Compressed, but slower to compress and lower quality than VRAM Compressed)

Only **VRAM Compressed** actually reduces the memory usage on the GPU. The **Lossless** and **Lossy** compression methods will reduce the required storage on disk, but they will not reduce memory usage on the GPU as the texture is sent to the GPU uncompressed.

Using **VRAM Compressed** also improves loading times, as VRAM-compressed textures are faster to load compared to textures using lossless or lossy compression. VRAM compression can exhibit noticeable artifacts and is intended to be used for 3D rendering, not 2D.

### Properties


| [String](class_string.md#class_String) | [load_path](class_compressedtexture2d.md#class_CompressedTexture2D_property_load_path) | `""` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |

### Methods


| Error | [load](class_compressedtexture2d.md#class_CompressedTexture2D_method_load) ( path: [String](class_string.md#class_String) ) |
| --- | --- |

---

### Property Descriptions

<span id="class_CompressedTexture2D_property_load_path"></span>

[String](class_string.md#class_String) **load_path** = `""` [🔗](class_compressedtexture2d.md#class_CompressedTexture2D_property_load_path)

- Error **load** ( path: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_load_path** ( )

The **CompressedTexture2D**'s file path to a `.ctex` file.

---

### Method Descriptions

<span id="class_CompressedTexture2D_method_load"></span>

Error **load** ( path: [String](class_string.md#class_String) ) [🔗](class_compressedtexture2d.md#class_CompressedTexture2D_method_load)

Loads the texture from the specified `path`.
