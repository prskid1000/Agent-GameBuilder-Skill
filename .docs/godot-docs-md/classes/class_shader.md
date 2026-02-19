<span id="class_Shader"></span>

## Shader

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShader](class_visualshader.md#class_VisualShader)

A shader implemented in the Godot shading language.

### Description

A custom shader program implemented in the Godot shading language, saved with the `.gdshader` extension.

This class is used by a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) and allows you to write your own custom behavior for rendering visual items or updating particle information. For a detailed explanation and usage, please see the tutorials linked below.

### Tutorials

- [Shaders documentation index](../tutorials/shaders/index.md)

### Properties


| [String](class_string.md#class_String) | [code](class_shader.md#class_Shader_property_code) | `""` |
| --- | --- | --- |

### Methods


| [Texture](class_texture.md#class_Texture) | [get_default_texture_parameter](class_shader.md#class_Shader_method_get_default_texture_parameter) ( name: [StringName](class_stringname.md#class_StringName), index: [int](class_int.md#class_int) = 0 ) const |
| --- | --- |
| [Mode](class_shader.md#enum_Shader_Mode) | [get_mode](class_shader.md#class_Shader_method_get_mode) ( ) const |
| [Array](class_array.md#class_Array) | [get_shader_uniform_list](class_shader.md#class_Shader_method_get_shader_uniform_list) ( get_groups: [bool](class_bool.md#class_bool) = false ) |
| void | [inspect_native_shader_code](class_shader.md#class_Shader_method_inspect_native_shader_code) ( ) |
| void | [set_default_texture_parameter](class_shader.md#class_Shader_method_set_default_texture_parameter) ( name: [StringName](class_stringname.md#class_StringName), texture: [Texture](class_texture.md#class_Texture), index: [int](class_int.md#class_int) = 0 ) |

---

### Enumerations

<span id="enum_Shader_Mode"></span>

enum **Mode**: [🔗](class_shader.md#enum_Shader_Mode)

<span id="class_Shader_constant_MODE_SPATIAL"></span>

[Mode](class_shader.md#enum_Shader_Mode) **MODE_SPATIAL** = `0`

Mode used to draw all 3D objects.

<span id="class_Shader_constant_MODE_CANVAS_ITEM"></span>

[Mode](class_shader.md#enum_Shader_Mode) **MODE_CANVAS_ITEM** = `1`

Mode used to draw all 2D objects.

<span id="class_Shader_constant_MODE_PARTICLES"></span>

[Mode](class_shader.md#enum_Shader_Mode) **MODE_PARTICLES** = `2`

Mode used to calculate particle information on a per-particle basis. Not used for drawing.

<span id="class_Shader_constant_MODE_SKY"></span>

[Mode](class_shader.md#enum_Shader_Mode) **MODE_SKY** = `3`

Mode used for drawing skies. Only works with shaders attached to [Sky](class_sky.md#class_Sky) objects.

<span id="class_Shader_constant_MODE_FOG"></span>

[Mode](class_shader.md#enum_Shader_Mode) **MODE_FOG** = `4`

Mode used for setting the color and density of volumetric fog effect.

<span id="class_Shader_constant_MODE_TEXTURE_BLIT"></span>

[Mode](class_shader.md#enum_Shader_Mode) **MODE_TEXTURE_BLIT** = `5`

Mode used for drawing to DrawableTexture resources via blit calls.

---

### Property Descriptions

<span id="class_Shader_property_code"></span>

[String](class_string.md#class_String) **code** = `""` [🔗](class_shader.md#class_Shader_property_code)

- void **set_code** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_code** ( )

Returns the shader's code as the user has written it, not the full generated code used internally.

---

### Method Descriptions

<span id="class_Shader_method_get_default_texture_parameter"></span>

[Texture](class_texture.md#class_Texture) **get_default_texture_parameter** ( name: [StringName](class_stringname.md#class_StringName), index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_shader.md#class_Shader_method_get_default_texture_parameter)

Returns the texture that is set as default for the specified parameter.

 **Note:** `name` must match the name of the uniform in the code exactly.

 **Note:** If the sampler array is used use `index` to access the specified texture.

---

<span id="class_Shader_method_get_mode"></span>

[Mode](class_shader.md#enum_Shader_Mode) **get_mode** ( ) *const* [🔗](class_shader.md#class_Shader_method_get_mode)

Returns the shader mode for the shader.

---

<span id="class_Shader_method_get_shader_uniform_list"></span>

[Array](class_array.md#class_Array) **get_shader_uniform_list** ( get_groups: [bool](class_bool.md#class_bool) = false ) [🔗](class_shader.md#class_Shader_method_get_shader_uniform_list)

Returns the list of shader uniforms that can be assigned to a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), for use with [ShaderMaterial.set_shader_parameter()](class_shadermaterial.md#class_ShaderMaterial_method_set_shader_parameter) and [ShaderMaterial.get_shader_parameter()](class_shadermaterial.md#class_ShaderMaterial_method_get_shader_parameter). The parameters returned are contained in dictionaries in a similar format to the ones returned by [Object.get_property_list()](class_object.md#class_Object_method_get_property_list).

If argument `get_groups` is `true`, parameter grouping hints are also included in the list.

---

<span id="class_Shader_method_inspect_native_shader_code"></span>

void **inspect_native_shader_code** ( ) [🔗](class_shader.md#class_Shader_method_inspect_native_shader_code)

Only available when running in the editor. Opens a popup that visualizes the generated shader code, including all variants and internal shader code. See also [Material.inspect_native_shader_code()](class_material.md#class_Material_method_inspect_native_shader_code).

---

<span id="class_Shader_method_set_default_texture_parameter"></span>

void **set_default_texture_parameter** ( name: [StringName](class_stringname.md#class_StringName), texture: [Texture](class_texture.md#class_Texture), index: [int](class_int.md#class_int) = 0 ) [🔗](class_shader.md#class_Shader_method_set_default_texture_parameter)

Sets the default texture to be used with a texture uniform. The default is used if a texture is not set in the [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial).

 **Note:** `name` must match the name of the uniform in the code exactly.

 **Note:** If the sampler array is used use `index` to access the specified texture.
