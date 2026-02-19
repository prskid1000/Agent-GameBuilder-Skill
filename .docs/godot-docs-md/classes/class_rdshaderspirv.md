<span id="class_RDShaderSPIRV"></span>

## RDShaderSPIRV

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

SPIR-V intermediate representation as part of an [RDShaderFile](class_rdshaderfile.md#class_RDShaderFile) (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

**RDShaderSPIRV** represents an [RDShaderFile](class_rdshaderfile.md#class_RDShaderFile)'s SPIR-V code for various shader stages, as well as possible compilation error messages. SPIR-V is a low-level intermediate shader representation. This intermediate representation is not used directly by GPUs for rendering, but it can be compiled into binary shaders that GPUs can understand. Unlike compiled shaders, SPIR-V is portable across GPU models and driver versions.

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_any_hit](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_any_hit) | `PackedByteArray()` |
| --- | --- | --- |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_closest_hit](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_closest_hit) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_compute](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_compute) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_fragment](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_fragment) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_intersection](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_intersection) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_miss](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_miss) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_raygen](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_raygen) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_tesselation_control](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_tesselation_control) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_tesselation_evaluation](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_tesselation_evaluation) | `PackedByteArray()` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [bytecode_vertex](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_vertex) | `PackedByteArray()` |
| [String](class_string.md#class_String) | [compile_error_any_hit](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_any_hit) | `""` |
| [String](class_string.md#class_String) | [compile_error_closest_hit](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_closest_hit) | `""` |
| [String](class_string.md#class_String) | [compile_error_compute](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_compute) | `""` |
| [String](class_string.md#class_String) | [compile_error_fragment](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_fragment) | `""` |
| [String](class_string.md#class_String) | [compile_error_intersection](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_intersection) | `""` |
| [String](class_string.md#class_String) | [compile_error_miss](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_miss) | `""` |
| [String](class_string.md#class_String) | [compile_error_raygen](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_raygen) | `""` |
| [String](class_string.md#class_String) | [compile_error_tesselation_control](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_tesselation_control) | `""` |
| [String](class_string.md#class_String) | [compile_error_tesselation_evaluation](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_tesselation_evaluation) | `""` |
| [String](class_string.md#class_String) | [compile_error_vertex](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_vertex) | `""` |

### Methods


| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [get_stage_bytecode](class_rdshaderspirv.md#class_RDShaderSPIRV_method_get_stage_bytecode) ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) const |
| --- | --- |
| [String](class_string.md#class_String) | [get_stage_compile_error](class_rdshaderspirv.md#class_RDShaderSPIRV_method_get_stage_compile_error) ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) const |
| void | [set_stage_bytecode](class_rdshaderspirv.md#class_RDShaderSPIRV_method_set_stage_bytecode) ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [set_stage_compile_error](class_rdshaderspirv.md#class_RDShaderSPIRV_method_set_stage_compile_error) ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) ) |

---

### Property Descriptions

<span id="class_RDShaderSPIRV_property_bytecode_any_hit"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_any_hit** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_any_hit)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the any hit shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_bytecode_closest_hit"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_closest_hit** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_closest_hit)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the closest hit shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_bytecode_compute"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_compute** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_compute)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the compute shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_bytecode_fragment"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_fragment** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_fragment)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the fragment shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_bytecode_intersection"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_intersection** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_intersection)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the intersection shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_bytecode_miss"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_miss** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_miss)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the miss shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_bytecode_raygen"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_raygen** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_raygen)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the ray generation shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_bytecode_tesselation_control"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_tesselation_control** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_tesselation_control)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the tessellation control shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_bytecode_tesselation_evaluation"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_tesselation_evaluation** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_tesselation_evaluation)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the tessellation evaluation shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_bytecode_vertex"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **bytecode_vertex** = `PackedByteArray()` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_vertex)

- void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The SPIR-V bytecode for the vertex shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_RDShaderSPIRV_property_compile_error_any_hit"></span>

[String](class_string.md#class_String) **compile_error_any_hit** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_any_hit)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the any hit shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

<span id="class_RDShaderSPIRV_property_compile_error_closest_hit"></span>

[String](class_string.md#class_String) **compile_error_closest_hit** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_closest_hit)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the closest hit shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

<span id="class_RDShaderSPIRV_property_compile_error_compute"></span>

[String](class_string.md#class_String) **compile_error_compute** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_compute)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the compute shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

<span id="class_RDShaderSPIRV_property_compile_error_fragment"></span>

[String](class_string.md#class_String) **compile_error_fragment** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_fragment)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the fragment shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

<span id="class_RDShaderSPIRV_property_compile_error_intersection"></span>

[String](class_string.md#class_String) **compile_error_intersection** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_intersection)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the intersection shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

<span id="class_RDShaderSPIRV_property_compile_error_miss"></span>

[String](class_string.md#class_String) **compile_error_miss** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_miss)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the miss shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

<span id="class_RDShaderSPIRV_property_compile_error_raygen"></span>

[String](class_string.md#class_String) **compile_error_raygen** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_raygen)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the ray generation shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

<span id="class_RDShaderSPIRV_property_compile_error_tesselation_control"></span>

[String](class_string.md#class_String) **compile_error_tesselation_control** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_tesselation_control)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the tessellation control shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

<span id="class_RDShaderSPIRV_property_compile_error_tesselation_evaluation"></span>

[String](class_string.md#class_String) **compile_error_tesselation_evaluation** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_tesselation_evaluation)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the tessellation evaluation shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

<span id="class_RDShaderSPIRV_property_compile_error_vertex"></span>

[String](class_string.md#class_String) **compile_error_vertex** = `""` [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_vertex)

- void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const*

The compilation error message for the vertex shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.

---

### Method Descriptions

<span id="class_RDShaderSPIRV_method_get_stage_bytecode"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const* [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_method_get_stage_bytecode)

Equivalent to getting one of [bytecode_compute](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_compute), [bytecode_fragment](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_fragment), [bytecode_tesselation_control](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_tesselation_control), [bytecode_tesselation_evaluation](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_tesselation_evaluation), [bytecode_vertex](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_vertex).

---

<span id="class_RDShaderSPIRV_method_get_stage_compile_error"></span>

[String](class_string.md#class_String) **get_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) ) *const* [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_method_get_stage_compile_error)

Returns the compilation error message for the given shader `stage`. Equivalent to getting one of [compile_error_compute](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_compute), [compile_error_fragment](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_fragment), [compile_error_tesselation_control](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_tesselation_control), [compile_error_tesselation_evaluation](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_tesselation_evaluation), [compile_error_vertex](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_vertex).

---

<span id="class_RDShaderSPIRV_method_set_stage_bytecode"></span>

void **set_stage_bytecode** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), bytecode: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_method_set_stage_bytecode)

Sets the SPIR-V `bytecode` for the given shader `stage`. Equivalent to setting one of [bytecode_compute](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_compute), [bytecode_fragment](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_fragment), [bytecode_tesselation_control](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_tesselation_control), [bytecode_tesselation_evaluation](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_tesselation_evaluation), [bytecode_vertex](class_rdshaderspirv.md#class_RDShaderSPIRV_property_bytecode_vertex).

---

<span id="class_RDShaderSPIRV_method_set_stage_compile_error"></span>

void **set_stage_compile_error** ( stage: [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage), compile_error: [String](class_string.md#class_String) ) [🔗](class_rdshaderspirv.md#class_RDShaderSPIRV_method_set_stage_compile_error)

Sets the compilation error message for the given shader `stage` to `compile_error`. Equivalent to setting one of [compile_error_compute](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_compute), [compile_error_fragment](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_fragment), [compile_error_tesselation_control](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_tesselation_control), [compile_error_tesselation_evaluation](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_tesselation_evaluation), [compile_error_vertex](class_rdshaderspirv.md#class_RDShaderSPIRV_property_compile_error_vertex).
