<span id="class_RDShaderSource"></span>

## RDShaderSource

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Shader source code (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

Shader source code in text form.

See also [RDShaderFile](class_rdshaderfile.md#class_RDShaderFile). **RDShaderSource** is only meant to be used with the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) API. It should not be confused with Godot's own [Shader](class_shader.md#class_Shader) resource, which is what Godot's various nodes use for high-level shader programming.

### Properties


| [ShaderLanguage](class_renderingdevice.md#enum_RenderingDevice_ShaderLanguage) | [language](class_rdshadersource.md#class_RDShaderSource_property_language) | `0` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [source_any_hit](class_rdshadersource.md#class_RDShaderSource_property_source_any_hit) | `""` |
| [String](class_string.md#class_String) | [source_closest_hit](class_rdshadersource.md#class_RDShaderSource_property_source_closest_hit) | `""` |
| [String](class_string.md#class_String) | [source_compute](class_rdshadersource.md#class_RDShaderSource_property_source_compute) | `""` |
| [String](class_string.md#class_String) | [source_fragment](class_rdshadersource.md#class_RDShaderSource_property_source_fragment) | `""` |
| [String](class_string.md#class_String) | [source_intersection](class_rdshadersource.md#class_RDShaderSource_property_source_intersection) | `""` |
| [String](class_string.md#class_String) | [source_miss](class_rdshadersource.md#class_RDShaderSource_property_source_miss) | `""` |
| [String](class_string.md#class_String) | [source_raygen](class_rdshadersource.md#class_RDShaderSource_property_source_raygen) | `""` |
| [String](class_string.md#class_String) | [source_tesselation_control](class_rdshadersource.md#class_RDShaderSource_property_source_tesselation_control) | `""` |
| [String](class_string.md#class_String) | [source_tesselation_evaluation](class_rdshadersource.md#class_RDShaderSource_property_source_tesselation_evaluation) | `""` |
| [String](class_string.md#class_String) | [source_vertex](class_rdshadersource.md#class_RDShaderSource_property_source_vertex) | `""` |

### Methods


| [String](class_string.md#class_String) | [get_stage_source](class_rdshadersource.md#class_RDShaderSource_method_get_stage_source) ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) const |
| --- | --- |
| void | [set_stage_source](class_rdshadersource.md#class_RDShaderSource_method_set_stage_source) ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) ) |

---

### Property Descriptions

<span id="class_RDShaderSource_property_language"></span>

[ShaderLanguage](class_renderingdevice.md#enum_RenderingDevice_ShaderLanguage) **language** = `0` [🔗](class_rdshadersource.md#class_RDShaderSource_property_language)

- void **set_language** ( value: [ShaderLanguage](class_renderingdevice.md#enum_RenderingDevice_ShaderLanguage) )
- [ShaderLanguage](class_renderingdevice.md#enum_RenderingDevice_ShaderLanguage) **get_language** ( )

The language the shader is written in.

---

<span id="class_RDShaderSource_property_source_any_hit"></span>

[String](class_string.md#class_String) **source_any_hit** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_any_hit)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's any hit stage.

---

<span id="class_RDShaderSource_property_source_closest_hit"></span>

[String](class_string.md#class_String) **source_closest_hit** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_closest_hit)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's closest hit stage.

---

<span id="class_RDShaderSource_property_source_compute"></span>

[String](class_string.md#class_String) **source_compute** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_compute)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's compute stage.

---

<span id="class_RDShaderSource_property_source_fragment"></span>

[String](class_string.md#class_String) **source_fragment** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_fragment)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's fragment stage.

---

<span id="class_RDShaderSource_property_source_intersection"></span>

[String](class_string.md#class_String) **source_intersection** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_intersection)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's intersection stage.

---

<span id="class_RDShaderSource_property_source_miss"></span>

[String](class_string.md#class_String) **source_miss** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_miss)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's miss stage.

---

<span id="class_RDShaderSource_property_source_raygen"></span>

[String](class_string.md#class_String) **source_raygen** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_raygen)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's ray generation stage.

---

<span id="class_RDShaderSource_property_source_tesselation_control"></span>

[String](class_string.md#class_String) **source_tesselation_control** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_tesselation_control)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's tessellation control stage.

---

<span id="class_RDShaderSource_property_source_tesselation_evaluation"></span>

[String](class_string.md#class_String) **source_tesselation_evaluation** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_tesselation_evaluation)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's tessellation evaluation stage.

---

<span id="class_RDShaderSource_property_source_vertex"></span>

[String](class_string.md#class_String) **source_vertex** = `""` [🔗](class_rdshadersource.md#class_RDShaderSource_property_source_vertex)

- void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

Source code for the shader's vertex stage.

---

### Method Descriptions

<span id="class_RDShaderSource_method_get_stage_source"></span>

[String](class_string.md#class_String) **get_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const* [🔗](class_rdshadersource.md#class_RDShaderSource_method_get_stage_source)

Returns source code for the specified shader `stage`. Equivalent to getting one of [source_compute](class_rdshadersource.md#class_RDShaderSource_property_source_compute), [source_fragment](class_rdshadersource.md#class_RDShaderSource_property_source_fragment), [source_tesselation_control](class_rdshadersource.md#class_RDShaderSource_property_source_tesselation_control), [source_tesselation_evaluation](class_rdshadersource.md#class_RDShaderSource_property_source_tesselation_evaluation) or [source_vertex](class_rdshadersource.md#class_RDShaderSource_property_source_vertex).

---

<span id="class_RDShaderSource_method_set_stage_source"></span>

void **set_stage_source** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), source: [String](class_string.md#class_String) ) [🔗](class_rdshadersource.md#class_RDShaderSource_method_set_stage_source)

Sets `source` code for the specified shader `stage`. Equivalent to setting one of [source_compute](class_rdshadersource.md#class_RDShaderSource_property_source_compute), [source_fragment](class_rdshadersource.md#class_RDShaderSource_property_source_fragment), [source_tesselation_control](class_rdshadersource.md#class_RDShaderSource_property_source_tesselation_control), [source_tesselation_evaluation](class_rdshadersource.md#class_RDShaderSource_property_source_tesselation_evaluation) or [source_vertex](class_rdshadersource.md#class_RDShaderSource_property_source_vertex).

 **Note:** If you set the compute shader source code using this method directly, remember to remove the Godot-specific hint `#[compute]`.
