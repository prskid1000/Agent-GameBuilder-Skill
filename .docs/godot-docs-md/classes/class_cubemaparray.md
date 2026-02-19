<span id="class_CubemapArray"></span>

## CubemapArray

**Inherits:** [ImageTextureLayered](class_imagetexturelayered.md#class_ImageTextureLayered) **<** [TextureLayered](class_texturelayered.md#class_TextureLayered) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An array of [Cubemap](class_cubemap.md#class_Cubemap) s, stored together and with a single reference.

### Description

**CubemapArray** s are made of an array of [Cubemap](class_cubemap.md#class_Cubemap) s. Like [Cubemap](class_cubemap.md#class_Cubemap) s, they are made of multiple textures, the amount of which must be divisible by 6 (one for each face of the cube).

The primary benefit of **CubemapArray** s is that they can be accessed in shader code using a single texture reference. In other words, you can pass multiple [Cubemap](class_cubemap.md#class_Cubemap) s into a shader using a single **CubemapArray**. [Cubemap](class_cubemap.md#class_Cubemap) s are allocated in adjacent cache regions on the GPU, which makes **CubemapArray** s the most efficient way to store multiple [Cubemap](class_cubemap.md#class_Cubemap) s.

Godot uses **CubemapArray** s internally for many effects, including the [Sky](class_sky.md#class_Sky) if you set ProjectSettings.rendering/reflections/sky_reflections/texture_array_reflections to `true`.

To create such a texture file yourself, reimport your image files using the Godot Editor import presets. To create a CubemapArray from code, use [ImageTextureLayered.create_from_images()](class_imagetexturelayered.md#class_ImageTextureLayered_method_create_from_images) on an instance of the CubemapArray class.

The expected image order is X+, X-, Y+, Y-, Z+, Z- (in Godot's coordinate system, so Y+ is "up" and Z- is "forward"). You can use one of the following templates as a base:

- 2×3 cubemap template (default layout option)

- 3×2 cubemap template

- 1×6 cubemap template

- 6×1 cubemap template

Multiple layers are stacked on top of each other when using the default vertical import option (with the first layer at the top). Alternatively, you can choose a horizontal layout in the import options (with the first layer at the left).

 **Note:** **CubemapArray** is not supported in the Compatibility renderer due to graphics API limitations.

### Methods


| [Resource](class_resource.md#class_Resource) | [create_placeholder](class_cubemaparray.md#class_CubemapArray_method_create_placeholder) ( ) const |
| --- | --- |

---

### Method Descriptions

<span id="class_CubemapArray_method_create_placeholder"></span>

[Resource](class_resource.md#class_Resource) **create_placeholder** ( ) *const* [🔗](class_cubemaparray.md#class_CubemapArray_method_create_placeholder)

Creates a placeholder version of this resource ([PlaceholderCubemapArray](class_placeholdercubemaparray.md#class_PlaceholderCubemapArray)).
