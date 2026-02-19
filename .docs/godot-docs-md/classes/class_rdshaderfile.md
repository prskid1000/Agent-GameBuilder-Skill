<span id="class_RDShaderFile"></span>

## RDShaderFile

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Compiled shader file in SPIR-V form (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)). Not to be confused with Godot's own [Shader](class_shader.md#class_Shader).

### Description

Compiled shader file in SPIR-V form.

See also [RDShaderSource](class_rdshadersource.md#class_RDShaderSource). **RDShaderFile** is only meant to be used with the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) API. It should not be confused with Godot's own [Shader](class_shader.md#class_Shader) resource, which is what Godot's various nodes use for high-level shader programming.

### Properties


| [String](class_string.md#class_String) | [base_error](class_rdshaderfile.md#class_RDShaderFile_property_base_error) | `""` |
| --- | --- | --- |

### Methods


| [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV) | [get_spirv](class_rdshaderfile.md#class_RDShaderFile_method_get_spirv) ( version: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| --- | --- |
| [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] | [get_version_list](class_rdshaderfile.md#class_RDShaderFile_method_get_version_list) ( ) const |
| void | [set_bytecode](class_rdshaderfile.md#class_RDShaderFile_method_set_bytecode) ( bytecode: [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV), version: [StringName](class_stringname.md#class_StringName) = &"" ) |

---

### Property Descriptions

<span id="class_RDShaderFile_property_base_error"></span>

[String](class_string.md#class_String) **base_error** = `""` [🔗](class_rdshaderfile.md#class_RDShaderFile_property_base_error)

- void **set_base_error** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_base_error** ( )

The base compilation error message, which indicates errors not related to a specific shader stage if non-empty. If empty, shader compilation is not necessarily successful (check [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV)'s error message members).

---

### Method Descriptions

<span id="class_RDShaderFile_method_get_spirv"></span>

[RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV) **get_spirv** ( version: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_rdshaderfile.md#class_RDShaderFile_method_get_spirv)

Returns the SPIR-V intermediate representation for the specified shader `version`.

---

<span id="class_RDShaderFile_method_get_version_list"></span>

[Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] **get_version_list** ( ) *const* [🔗](class_rdshaderfile.md#class_RDShaderFile_method_get_version_list)

Returns the list of compiled versions for this shader.

---

<span id="class_RDShaderFile_method_set_bytecode"></span>

void **set_bytecode** ( bytecode: [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV), version: [StringName](class_stringname.md#class_StringName) = &"" ) [🔗](class_rdshaderfile.md#class_RDShaderFile_method_set_bytecode)

Sets the SPIR-V `bytecode` that will be compiled for the specified `version`.
