<span id="class_PlaceholderTextureLayered"></span>

## PlaceholderTextureLayered

**Inherits:** [TextureLayered](class_texturelayered.md#class_TextureLayered) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [PlaceholderCubemap](class_placeholdercubemap.md#class_PlaceholderCubemap), [PlaceholderCubemapArray](class_placeholdercubemaparray.md#class_PlaceholderCubemapArray), [PlaceholderTexture2DArray](class_placeholdertexture2darray.md#class_PlaceholderTexture2DArray)

Placeholder class for a 2-dimensional texture array.

### Description

This class is used when loading a project that uses a [TextureLayered](class_texturelayered.md#class_TextureLayered) subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.

- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

 **Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).

### Properties


| [int](class_int.md#class_int) | [layers](class_placeholdertexturelayered.md#class_PlaceholderTextureLayered_property_layers) | `1` |
| --- | --- | --- |
| [Vector2i](class_vector2i.md#class_Vector2i) | [size](class_placeholdertexturelayered.md#class_PlaceholderTextureLayered_property_size) | `Vector2i(1, 1)` |

---

### Property Descriptions

<span id="class_PlaceholderTextureLayered_property_layers"></span>

[int](class_int.md#class_int) **layers** = `1` [🔗](class_placeholdertexturelayered.md#class_PlaceholderTextureLayered_property_layers)

- void **set_layers** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_layers** ( )

The number of layers in the texture array.

---

<span id="class_PlaceholderTextureLayered_property_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **size** = `Vector2i(1, 1)` [🔗](class_placeholdertexturelayered.md#class_PlaceholderTextureLayered_property_size)

- void **set_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_size** ( )

The size of each texture layer (in pixels).
