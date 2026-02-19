<span id="class_VisualShaderNodeCustom"></span>

## VisualShaderNodeCustom

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Virtual class to define custom [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) s for use in the Visual Shader Editor.

### Description

By inheriting this class you can create a custom [VisualShader](class_visualshader.md#class_VisualShader) script addon which will be automatically added to the Visual Shader Editor. The [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode)'s behavior is defined by overriding the provided virtual methods.

In order for the node to be registered as an editor addon, you must use the `@tool` annotation and provide a `class_name` for your custom script. For example:

::

    @tool
    extends VisualShaderNodeCustom
    class_name VisualShaderNodeNoise

### Tutorials

- [Visual Shader plugins](../tutorials/plugins/editor/visual_shader_plugins.md)

### Methods


| [String](class_string.md#class_String) | [_get_category](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_category) ( ) | virtual | const |
| --- | --- | --- | --- |
| [String](class_string.md#class_String) | [_get_code](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_code) ( input_vars: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\], output_vars: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\], mode: [Mode](class_shader.md#enum_Shader_Mode), type: [Type](class_visualshader.md#enum_VisualShader_Type) ) | virtual | const |
| [int](class_int.md#class_int) | [_get_default_input_port](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_default_input_port) ( type: [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_description](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_description) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_func_code](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_func_code) ( mode: [Mode](class_shader.md#enum_Shader_Mode), type: [Type](class_visualshader.md#enum_VisualShader_Type) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_global_code](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_global_code) ( mode: [Mode](class_shader.md#enum_Shader_Mode) ) | virtual | const |
| [int](class_int.md#class_int) | [_get_input_port_count](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_input_port_count) ( ) | virtual | const |
| [Variant](class_variant.md#class_Variant) | [_get_input_port_default_value](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_input_port_default_value) ( port: [int](class_int.md#class_int) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_input_port_name](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_input_port_name) ( port: [int](class_int.md#class_int) ) | virtual | const |
| [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) | [_get_input_port_type](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_input_port_type) ( port: [int](class_int.md#class_int) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_name](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_name) ( ) | virtual | const |
| [int](class_int.md#class_int) | [_get_output_port_count](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_output_port_count) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_output_port_name](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_output_port_name) ( port: [int](class_int.md#class_int) ) | virtual | const |
| [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) | [_get_output_port_type](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_output_port_type) ( port: [int](class_int.md#class_int) ) | virtual | const |
| [int](class_int.md#class_int) | [_get_property_count](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_property_count) ( ) | virtual | const |
| [int](class_int.md#class_int) | [_get_property_default_index](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_property_default_index) ( index: [int](class_int.md#class_int) ) | virtual | const |
| [String](class_string.md#class_String) | [_get_property_name](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_property_name) ( index: [int](class_int.md#class_int) ) | virtual | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_property_options](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_property_options) ( index: [int](class_int.md#class_int) ) | virtual | const |
| [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) | [_get_return_icon_type](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_return_icon_type) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_available](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__is_available) ( mode: [Mode](class_shader.md#enum_Shader_Mode), type: [Type](class_visualshader.md#enum_VisualShader_Type) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_highend](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__is_highend) ( ) | virtual | const |
| [int](class_int.md#class_int) | [get_option_index](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_method_get_option_index) ( option: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_VisualShaderNodeCustom_private_method__get_category"></span>

[String](class_string.md#class_String) **_get_category** ( ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_category)

Override this method to define the path to the associated custom node in the Visual Shader Editor's members dialog. The path may look like `"MyGame/MyFunctions/Noise"`.

Defining this method is **optional**. If not overridden, the node will be filed under the "Addons" category.

---

<span id="class_VisualShaderNodeCustom_private_method__get_code"></span>

[String](class_string.md#class_String) **_get_code** ( input_vars: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\], output_vars: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\], mode: [Mode](class_shader.md#enum_Shader_Mode), type: [Type](class_visualshader.md#enum_VisualShader_Type) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_code)

Override this method to define the actual shader code of the associated custom node. The shader code should be returned as a string, which can have multiple lines (the `"""` multiline string construct can be used for convenience).

The `input_vars` and `output_vars` arrays contain the string names of the various input and output variables, as defined by `_get_input_*` and `_get_output_*` virtual methods in this class.

The output ports can be assigned values in the shader code. For example, `return output_vars[0] + " = " + input_vars[0] + ";"`.

You can customize the generated code based on the shader `mode` and/or `type`.

Defining this method is **required**.

---

<span id="class_VisualShaderNodeCustom_private_method__get_default_input_port"></span>

[int](class_int.md#class_int) **_get_default_input_port** ( type: [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_default_input_port)

Override this method to define the input port which should be connected by default when this node is created as a result of dragging a connection from an existing node to the empty space on the graph.

Defining this method is **optional**. If not overridden, the connection will be created to the first valid port.

---

<span id="class_VisualShaderNodeCustom_private_method__get_description"></span>

[String](class_string.md#class_String) **_get_description** ( ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_description)

Override this method to define the description of the associated custom node in the Visual Shader Editor's members dialog.

Defining this method is **optional**.

---

<span id="class_VisualShaderNodeCustom_private_method__get_func_code"></span>

[String](class_string.md#class_String) **_get_func_code** ( mode: [Mode](class_shader.md#enum_Shader_Mode), type: [Type](class_visualshader.md#enum_VisualShader_Type) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_func_code)

Override this method to add a shader code to the beginning of each shader function (once). The shader code should be returned as a string, which can have multiple lines (the `"""` multiline string construct can be used for convenience).

If there are multiple custom nodes of different types which use this feature the order of each insertion is undefined.

You can customize the generated code based on the shader `mode` and/or `type`.

Defining this method is **optional**.

---

<span id="class_VisualShaderNodeCustom_private_method__get_global_code"></span>

[String](class_string.md#class_String) **_get_global_code** ( mode: [Mode](class_shader.md#enum_Shader_Mode) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_global_code)

Override this method to add shader code on top of the global shader, to define your own standard library of reusable methods, varyings, constants, uniforms, etc. The shader code should be returned as a string, which can have multiple lines (the `"""` multiline string construct can be used for convenience).

Be careful with this functionality as it can cause name conflicts with other custom nodes, so be sure to give the defined entities unique names.

You can customize the generated code based on the shader `mode`.

Defining this method is **optional**.

---

<span id="class_VisualShaderNodeCustom_private_method__get_input_port_count"></span>

[int](class_int.md#class_int) **_get_input_port_count** ( ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_input_port_count)

Override this method to define the number of input ports of the associated custom node.

Defining this method is **required**. If not overridden, the node has no input ports.

---

<span id="class_VisualShaderNodeCustom_private_method__get_input_port_default_value"></span>

[Variant](class_variant.md#class_Variant) **_get_input_port_default_value** ( port: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_input_port_default_value)

Override this method to define the default value for the specified input port. Prefer use this over [VisualShaderNode.set_input_port_default_value()](class_visualshadernode.md#class_VisualShaderNode_method_set_input_port_default_value).

Defining this method is **required**. If not overridden, the node has no default values for their input ports.

---

<span id="class_VisualShaderNodeCustom_private_method__get_input_port_name"></span>

[String](class_string.md#class_String) **_get_input_port_name** ( port: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_input_port_name)

Override this method to define the names of input ports of the associated custom node. The names are used both for the input slots in the editor and as identifiers in the shader code, and are passed in the `input_vars` array in [_get_code()](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_code).

Defining this method is **optional**, but recommended. If not overridden, input ports are named as `"in" + str(port)`.

---

<span id="class_VisualShaderNodeCustom_private_method__get_input_port_type"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **_get_input_port_type** ( port: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_input_port_type)

Override this method to define the returned type of each input port of the associated custom node.

Defining this method is **optional**, but recommended. If not overridden, input ports will return the [VisualShaderNode.PORT_TYPE_SCALAR](class_visualshadernode.md#class_VisualShaderNode_constant_PORT_TYPE_SCALAR) type.

---

<span id="class_VisualShaderNodeCustom_private_method__get_name"></span>

[String](class_string.md#class_String) **_get_name** ( ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_name)

Override this method to define the name of the associated custom node in the Visual Shader Editor's members dialog and graph.

Defining this method is **optional**, but recommended. If not overridden, the node will be named as "Unnamed".

---

<span id="class_VisualShaderNodeCustom_private_method__get_output_port_count"></span>

[int](class_int.md#class_int) **_get_output_port_count** ( ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_output_port_count)

Override this method to define the number of output ports of the associated custom node.

Defining this method is **required**. If not overridden, the node has no output ports.

---

<span id="class_VisualShaderNodeCustom_private_method__get_output_port_name"></span>

[String](class_string.md#class_String) **_get_output_port_name** ( port: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_output_port_name)

Override this method to define the names of output ports of the associated custom node. The names are used both for the output slots in the editor and as identifiers in the shader code, and are passed in the `output_vars` array in [_get_code()](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_code).

Defining this method is **optional**, but recommended. If not overridden, output ports are named as `"out" + str(port)`.

---

<span id="class_VisualShaderNodeCustom_private_method__get_output_port_type"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **_get_output_port_type** ( port: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_output_port_type)

Override this method to define the returned type of each output port of the associated custom node.

Defining this method is **optional**, but recommended. If not overridden, output ports will return the [VisualShaderNode.PORT_TYPE_SCALAR](class_visualshadernode.md#class_VisualShaderNode_constant_PORT_TYPE_SCALAR) type.

---

<span id="class_VisualShaderNodeCustom_private_method__get_property_count"></span>

[int](class_int.md#class_int) **_get_property_count** ( ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_property_count)

Override this method to define the number of the properties.

Defining this method is **optional**.

---

<span id="class_VisualShaderNodeCustom_private_method__get_property_default_index"></span>

[int](class_int.md#class_int) **_get_property_default_index** ( index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_property_default_index)

Override this method to define the default index of the property of the associated custom node.

Defining this method is **optional**.

---

<span id="class_VisualShaderNodeCustom_private_method__get_property_name"></span>

[String](class_string.md#class_String) **_get_property_name** ( index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_property_name)

Override this method to define the names of the property of the associated custom node.

Defining this method is **optional**.

---

<span id="class_VisualShaderNodeCustom_private_method__get_property_options"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_property_options** ( index: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_property_options)

Override this method to define the options inside the drop-down list property of the associated custom node.

Defining this method is **optional**.

---

<span id="class_VisualShaderNodeCustom_private_method__get_return_icon_type"></span>

[PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType) **_get_return_icon_type** ( ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_return_icon_type)

Override this method to define the return icon of the associated custom node in the Visual Shader Editor's members dialog.

Defining this method is **optional**. If not overridden, no return icon is shown.

---

<span id="class_VisualShaderNodeCustom_private_method__is_available"></span>

[bool](class_bool.md#class_bool) **_is_available** ( mode: [Mode](class_shader.md#enum_Shader_Mode), type: [Type](class_visualshader.md#enum_VisualShader_Type) ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__is_available)

Override this method to prevent the node to be visible in the member dialog for the certain `mode` and/or `type`.

Defining this method is **optional**. If not overridden, it's `true`.

---

<span id="class_VisualShaderNodeCustom_private_method__is_highend"></span>

[bool](class_bool.md#class_bool) **_is_highend** ( ) *virtual* *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__is_highend)

Override this method to enable the high-end mark in the Visual Shader Editor's members dialog. This should return `true` for nodes that only work when using the Forward+ and Mobile renderers.

Defining this method is **optional**. If not overridden, it's `false`, which indicates this node works with all renderers (including Compatibility).

---

<span id="class_VisualShaderNodeCustom_method_get_option_index"></span>

[int](class_int.md#class_int) **get_option_index** ( option: [int](class_int.md#class_int) ) *const* [🔗](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_method_get_option_index)

Returns the selected index of the drop-down list option within a graph. You may use this function to define the specific behavior in the [_get_code()](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_code) or [_get_global_code()](class_visualshadernodecustom.md#class_VisualShaderNodeCustom_private_method__get_global_code).
