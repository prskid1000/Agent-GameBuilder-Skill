<span id="class_PlaceholderCubemap"></span>

## PlaceholderCubemap

**Inherits:** [PlaceholderTextureLayered](class_placeholdertexturelayered.md#class_PlaceholderTextureLayered) **<** [TextureLayered](class_texturelayered.md#class_TextureLayered) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A [Cubemap](class_cubemap.md#class_Cubemap) without image data.

### Description

This class replaces a [Cubemap](class_cubemap.md#class_Cubemap) or a [Cubemap](class_cubemap.md#class_Cubemap)-derived class in 2 conditions:

- In dedicated server mode, where the image data shouldn't affect game logic. This allows reducing the exported PCK's size significantly.

- When the [Cubemap](class_cubemap.md#class_Cubemap)-derived class is missing, for example when using a different engine version.

 **Note:** This class is not intended for rendering or for use in shaders. Operations like calculating UV are not guaranteed to work.
