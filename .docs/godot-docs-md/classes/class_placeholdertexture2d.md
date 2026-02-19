<span id="class_PlaceholderTexture2D"></span>

## PlaceholderTexture2D

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Placeholder class for a 2-dimensional texture.

### Description

This class is used when loading a project that uses a [Texture2D](class_texture2d.md#class_Texture2D) subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.

- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

 **Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).

### Properties


| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [size](class_placeholdertexture2d.md#class_PlaceholderTexture2D_property_size) | `Vector2(1, 1)` |

---

### Property Descriptions

<span id="class_PlaceholderTexture2D_property_size"></span>

[Vector2](class_vector2.md#class_Vector2) **size** = `Vector2(1, 1)` [🔗](class_placeholdertexture2d.md#class_PlaceholderTexture2D_property_size)

- void **set_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_size** ( )

The texture's size (in pixels).
