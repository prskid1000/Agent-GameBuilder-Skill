<span id="class_VisualShaderNodeGroupBase"></span>

## VisualShaderNodeGroupBase

**Inherits:** [VisualShaderNodeResizableBase](class_visualshadernoderesizablebase.md#class_VisualShaderNodeResizableBase) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeExpression](class_visualshadernodeexpression.md#class_VisualShaderNodeExpression)

Base class for a family of nodes with variable number of input and output ports within the visual shader graph.

### Description

Currently, has no direct usage, use the derived classes instead.

### Methods


| void | [add_input_port](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_input_port) ( id: [int](class_int.md#class_int), type: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| --- | --- |
| void | [add_output_port](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_output_port) ( id: [int](class_int.md#class_int), type: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [clear_input_ports](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_clear_input_ports) ( ) |
| void | [clear_output_ports](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_clear_output_ports) ( ) |
| [int](class_int.md#class_int) | [get_free_input_port_id](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_free_input_port_id) ( ) const |
| [int](class_int.md#class_int) | [get_free_output_port_id](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_free_output_port_id) ( ) const |
| [int](class_int.md#class_int) | [get_input_port_count](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_input_port_count) ( ) const |
| [String](class_string.md#class_String) | [get_inputs](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_inputs) ( ) const |
| [int](class_int.md#class_int) | [get_output_port_count](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_output_port_count) ( ) const |
| [String](class_string.md#class_String) | [get_outputs](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_outputs) ( ) const |
| [bool](class_bool.md#class_bool) | [has_input_port](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_has_input_port) ( id: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has_output_port](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_has_output_port) ( id: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_valid_port_name](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_is_valid_port_name) ( name: [String](class_string.md#class_String) ) const |
| void | [remove_input_port](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_remove_input_port) ( id: [int](class_int.md#class_int) ) |
| void | [remove_output_port](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_remove_output_port) ( id: [int](class_int.md#class_int) ) |
| void | [set_input_port_name](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_input_port_name) ( id: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [set_input_port_type](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_input_port_type) ( id: [int](class_int.md#class_int), type: [int](class_int.md#class_int) ) |
| void | [set_inputs](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_inputs) ( inputs: [String](class_string.md#class_String) ) |
| void | [set_output_port_name](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_output_port_name) ( id: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [set_output_port_type](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_output_port_type) ( id: [int](class_int.md#class_int), type: [int](class_int.md#class_int) ) |
| void | [set_outputs](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_outputs) ( outputs: [String](class_string.md#class_String) ) |

---

### Method Descriptions

<span id="class_VisualShaderNodeGroupBase_method_add_input_port"></span>

void **add_input_port** ( id: [int](class_int.md#class_int), type: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_input_port)

Adds an input port with the specified `type` (see [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType)) and `name`.

---

<span id="class_VisualShaderNodeGroupBase_method_add_output_port"></span>

void **add_output_port** ( id: [int](class_int.md#class_int), type: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_output_port)

Adds an output port with the specified `type` (see [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType)) and `name`.

---

<span id="class_VisualShaderNodeGroupBase_method_clear_input_ports"></span>

void **clear_input_ports** ( ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_clear_input_ports)

Removes all previously specified input ports.

---

<span id="class_VisualShaderNodeGroupBase_method_clear_output_ports"></span>

void **clear_output_ports** ( ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_clear_output_ports)

Removes all previously specified output ports.

---

<span id="class_VisualShaderNodeGroupBase_method_get_free_input_port_id"></span>

[int](class_int.md#class_int) **get_free_input_port_id** ( ) *const* [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_free_input_port_id)

Returns a free input port ID which can be used in [add_input_port()](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_input_port).

---

<span id="class_VisualShaderNodeGroupBase_method_get_free_output_port_id"></span>

[int](class_int.md#class_int) **get_free_output_port_id** ( ) *const* [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_free_output_port_id)

Returns a free output port ID which can be used in [add_output_port()](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_output_port).

---

<span id="class_VisualShaderNodeGroupBase_method_get_input_port_count"></span>

[int](class_int.md#class_int) **get_input_port_count** ( ) *const* [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_input_port_count)

Returns the number of input ports in use. Alternative for [get_free_input_port_id()](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_free_input_port_id).

---

<span id="class_VisualShaderNodeGroupBase_method_get_inputs"></span>

[String](class_string.md#class_String) **get_inputs** ( ) *const* [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_inputs)

Returns a [String](class_string.md#class_String) description of the input ports as a colon-separated list using the format `id,type,name;` (see [add_input_port()](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_input_port)).

---

<span id="class_VisualShaderNodeGroupBase_method_get_output_port_count"></span>

[int](class_int.md#class_int) **get_output_port_count** ( ) *const* [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_output_port_count)

Returns the number of output ports in use. Alternative for [get_free_output_port_id()](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_free_output_port_id).

---

<span id="class_VisualShaderNodeGroupBase_method_get_outputs"></span>

[String](class_string.md#class_String) **get_outputs** ( ) *const* [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_get_outputs)

Returns a [String](class_string.md#class_String) description of the output ports as a colon-separated list using the format `id,type,name;` (see [add_output_port()](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_output_port)).

---

<span id="class_VisualShaderNodeGroupBase_method_has_input_port"></span>

[bool](class_bool.md#class_bool) **has_input_port** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_has_input_port)

Returns `true` if the specified input port exists.

---

<span id="class_VisualShaderNodeGroupBase_method_has_output_port"></span>

[bool](class_bool.md#class_bool) **has_output_port** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_has_output_port)

Returns `true` if the specified output port exists.

---

<span id="class_VisualShaderNodeGroupBase_method_is_valid_port_name"></span>

[bool](class_bool.md#class_bool) **is_valid_port_name** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_is_valid_port_name)

Returns `true` if the specified port name does not override an existed port name and is valid within the shader.

---

<span id="class_VisualShaderNodeGroupBase_method_remove_input_port"></span>

void **remove_input_port** ( id: [int](class_int.md#class_int) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_remove_input_port)

Removes the specified input port.

---

<span id="class_VisualShaderNodeGroupBase_method_remove_output_port"></span>

void **remove_output_port** ( id: [int](class_int.md#class_int) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_remove_output_port)

Removes the specified output port.

---

<span id="class_VisualShaderNodeGroupBase_method_set_input_port_name"></span>

void **set_input_port_name** ( id: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_input_port_name)

Renames the specified input port.

---

<span id="class_VisualShaderNodeGroupBase_method_set_input_port_type"></span>

void **set_input_port_type** ( id: [int](class_int.md#class_int), type: [int](class_int.md#class_int) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_input_port_type)

Sets the specified input port's type (see [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType)).

---

<span id="class_VisualShaderNodeGroupBase_method_set_inputs"></span>

void **set_inputs** ( inputs: [String](class_string.md#class_String) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_inputs)

Defines all input ports using a [String](class_string.md#class_String) formatted as a colon-separated list: `id,type,name;` (see [add_input_port()](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_input_port)).

---

<span id="class_VisualShaderNodeGroupBase_method_set_output_port_name"></span>

void **set_output_port_name** ( id: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_output_port_name)

Renames the specified output port.

---

<span id="class_VisualShaderNodeGroupBase_method_set_output_port_type"></span>

void **set_output_port_type** ( id: [int](class_int.md#class_int), type: [int](class_int.md#class_int) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_output_port_type)

Sets the specified output port's type (see [PortType](class_visualshadernode.md#enum_VisualShaderNode_PortType)).

---

<span id="class_VisualShaderNodeGroupBase_method_set_outputs"></span>

void **set_outputs** ( outputs: [String](class_string.md#class_String) ) [🔗](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_set_outputs)

Defines all output ports using a [String](class_string.md#class_String) formatted as a colon-separated list: `id,type,name;` (see [add_output_port()](class_visualshadernodegroupbase.md#class_VisualShaderNodeGroupBase_method_add_output_port)).
