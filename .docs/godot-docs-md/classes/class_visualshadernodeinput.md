<span id="class_VisualShaderNodeInput"></span>

## VisualShaderNodeInput

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents the input shader parameter within the visual shader graph.

### Description

Gives access to input variables (built-ins) available for the shader. See the shading reference for the list of available built-ins for each shader type (check `Tutorials` section for link).

### Tutorials

- [Shading reference index](../tutorials/shaders/shader_reference/index.md)

### Properties


| [String](class_string.md#class_String) | [input_name](class_visualshadernodeinput.md#class_VisualShaderNodeInput_property_input_name) | `"[None]"` |
| --- | --- | --- |

### Methods


| [String](class_string.md#class_String) | [get_input_real_name](class_visualshadernodeinput.md#class_VisualShaderNodeInput_method_get_input_real_name) ( ) const |
| --- | --- |

---

### Signals

<span id="class_VisualShaderNodeInput_signal_input_type_changed"></span>

**input_type_changed** ( ) [🔗](class_visualshadernodeinput.md#class_VisualShaderNodeInput_signal_input_type_changed)

Emitted when input is changed via [input_name](class_visualshadernodeinput.md#class_VisualShaderNodeInput_property_input_name).

---

### Property Descriptions

<span id="class_VisualShaderNodeInput_property_input_name"></span>

[String](class_string.md#class_String) **input_name** = `"[None]"` [🔗](class_visualshadernodeinput.md#class_VisualShaderNodeInput_property_input_name)

- void **set_input_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_input_name** ( )

One of the several input constants in lower-case style like: "vertex" (`VERTEX`) or "point_size" (`POINT_SIZE`).

---

### Method Descriptions

<span id="class_VisualShaderNodeInput_method_get_input_real_name"></span>

[String](class_string.md#class_String) **get_input_real_name** ( ) *const* [🔗](class_visualshadernodeinput.md#class_VisualShaderNodeInput_method_get_input_real_name)

Returns a translated name of the current constant in the Godot Shader Language. E.g. `"ALBEDO"` if the [input_name](class_visualshadernodeinput.md#class_VisualShaderNodeInput_property_input_name) equal to `"albedo"`.
