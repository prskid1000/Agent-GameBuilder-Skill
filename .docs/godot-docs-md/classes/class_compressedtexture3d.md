<span id="class_CompressedTexture3D"></span>

## CompressedTexture3D

**Inherits:** [Texture3D](class_texture3d.md#class_Texture3D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture with 3 dimensions, optionally compressed.

### Description

**CompressedTexture3D** is the VRAM-compressed counterpart of [ImageTexture3D](class_imagetexture3d.md#class_ImageTexture3D). The file extension for **CompressedTexture3D** files is `.ctex3d`. This file format is internal to Godot; it is created by importing other image formats with the import system.

 **CompressedTexture3D** uses VRAM compression, which allows to reduce memory usage on the GPU when rendering the texture. This also improves loading times, as VRAM-compressed textures are faster to load compared to textures using lossless compression. VRAM compression can exhibit noticeable artifacts and is intended to be used for 3D rendering, not 2D.

See [Texture3D](class_texture3d.md#class_Texture3D) for a general description of 3D textures.

### Properties


| [String](class_string.md#class_String) | [load_path](class_compressedtexture3d.md#class_CompressedTexture3D_property_load_path) | `""` |
| --- | --- | --- |

### Methods


| Error | [load](class_compressedtexture3d.md#class_CompressedTexture3D_method_load) ( path: [String](class_string.md#class_String) ) |
| --- | --- |

---

### Property Descriptions

<span id="class_CompressedTexture3D_property_load_path"></span>

[String](class_string.md#class_String) **load_path** = `""` [🔗](class_compressedtexture3d.md#class_CompressedTexture3D_property_load_path)

- Error **load** ( path: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_load_path** ( )

The **CompressedTexture3D**'s file path to a `.ctex3d` file.

---

### Method Descriptions

<span id="class_CompressedTexture3D_method_load"></span>

Error **load** ( path: [String](class_string.md#class_String) ) [🔗](class_compressedtexture3d.md#class_CompressedTexture3D_method_load)

Loads the texture from the specified `path`.
