<span id="class_Cubemap"></span>

## Cubemap

**Inherits:** [ImageTextureLayered](class_imagetexturelayered.md#class_ImageTextureLayered) **<** [TextureLayered](class_texturelayered.md#class_TextureLayered) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Six square textures representing the faces of a cube. Commonly used as a skybox.

### Description

A cubemap is made of 6 textures organized in layers. They are typically used for faking reflections in 3D rendering (see [ReflectionProbe](class_reflectionprobe.md#class_ReflectionProbe)). It can be used to make an object look as if it's reflecting its surroundings. This usually delivers much better performance than other reflection methods.

This resource is typically used as a uniform in custom shaders. Few core Godot methods make use of **Cubemap** resources.

To create such a texture file yourself, reimport your image files using the Godot Editor import presets. To create a Cubemap from code, use [ImageTextureLayered.create_from_images()](class_imagetexturelayered.md#class_ImageTextureLayered_method_create_from_images) on an instance of the Cubemap class.

The expected image order is X+, X-, Y+, Y-, Z+, Z- (in Godot's coordinate system, so Y+ is "up" and Z- is "forward"). You can use one of the following templates as a base:

- 2×3 cubemap template (default layout option)

- 3×2 cubemap template

- 1×6 cubemap template

- 6×1 cubemap template

 **Note:** Godot doesn't support using cubemaps in a [PanoramaSkyMaterial](class_panoramaskymaterial.md#class_PanoramaSkyMaterial). To use a cubemap as a skybox, convert the default [PanoramaSkyMaterial](class_panoramaskymaterial.md#class_PanoramaSkyMaterial) to a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) using the **Convert to ShaderMaterial** resource dropdown option, then replace its code with the following:

.. code:: text

    shader_type sky;

    uniform samplerCube source_panorama : filter_linear, source_color, hint_default_black;
    uniform float exposure : hint_range(0, 128) = 1.0;

    void sky() {
        // If importing a cubemap from another engine, you may need to flip one of the `EYEDIR` components below
        // by replacing it with `-EYEDIR`.
        vec3 eyedir = vec3(EYEDIR.x, EYEDIR.y, EYEDIR.z);
        COLOR = texture(source_panorama, eyedir).rgb * exposure;
    }

After replacing the shader code and saving, specify the imported Cubemap resource in the Shader Parameters section of the ShaderMaterial in the inspector.

Alternatively, you can use this tool to convert a cubemap to an equirectangular sky map and use [PanoramaSkyMaterial](class_panoramaskymaterial.md#class_PanoramaSkyMaterial) as usual.

### Methods


| [Resource](class_resource.md#class_Resource) | [create_placeholder](class_cubemap.md#class_Cubemap_method_create_placeholder) ( ) const |
| --- | --- |

---

### Method Descriptions

<span id="class_Cubemap_method_create_placeholder"></span>

[Resource](class_resource.md#class_Resource) **create_placeholder** ( ) *const* [🔗](class_cubemap.md#class_Cubemap_method_create_placeholder)

Creates a placeholder version of this resource ([PlaceholderCubemap](class_placeholdercubemap.md#class_PlaceholderCubemap)).
