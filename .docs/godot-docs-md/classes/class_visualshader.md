<span id="class_VisualShader"></span>

## VisualShader

**Inherits:** [Shader](class_shader.md#class_Shader) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A custom shader program with a visual editor.

### Description

This class provides a graph-like visual editor for creating a [Shader](class_shader.md#class_Shader). Although **VisualShader** s do not require coding, they share the same logic with script shaders. They use [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) s that can be connected to each other to control the flow of the shader. The visual shader graph is converted to a script shader behind the scenes.

### Tutorials

- [Using VisualShaders](../tutorials/shaders/visual_shaders.md)

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [graph_offset](class_visualshader.md#class_VisualShader_property_graph_offset) |
| --- | --- |

### Methods


| void | [add_node](class_visualshader.md#class_VisualShader_method_add_node) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), node: [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode), position: [Vector2](class_vector2.md#class_Vector2), id: [int](class_int.md#class_int) ) |
| --- | --- |
| void | [add_varying](class_visualshader.md#class_VisualShader_method_add_varying) ( name: [String](class_string.md#class_String), mode: [VaryingMode](class_visualshader.md#enum_VisualShader_VaryingMode), type: [VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) ) |
| void | [attach_node_to_frame](class_visualshader.md#class_VisualShader_method_attach_node_to_frame) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int), frame: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [can_connect_nodes](class_visualshader.md#class_VisualShader_method_can_connect_nodes) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) const |
| Error | [connect_nodes](class_visualshader.md#class_VisualShader_method_connect_nodes) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) |
| void | [connect_nodes_forced](class_visualshader.md#class_VisualShader_method_connect_nodes_forced) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) |
| void | [detach_node_from_frame](class_visualshader.md#class_VisualShader_method_detach_node_from_frame) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int) ) |
| void | [disconnect_nodes](class_visualshader.md#class_VisualShader_method_disconnect_nodes) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) |
| [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) | [get_node](class_visualshader.md#class_VisualShader_method_get_node) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_node_connections](class_visualshader.md#class_VisualShader_method_get_node_connections) ( type: [Type](class_visualshader.md#enum_VisualShader_Type) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_node_list](class_visualshader.md#class_VisualShader_method_get_node_list) ( type: [Type](class_visualshader.md#enum_VisualShader_Type) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_node_position](class_visualshader.md#class_VisualShader_method_get_node_position) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_valid_node_id](class_visualshader.md#class_VisualShader_method_get_valid_node_id) ( type: [Type](class_visualshader.md#enum_VisualShader_Type) ) const |
| [bool](class_bool.md#class_bool) | [has_varying](class_visualshader.md#class_VisualShader_method_has_varying) ( name: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [is_node_connection](class_visualshader.md#class_VisualShader_method_is_node_connection) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) const |
| void | [remove_node](class_visualshader.md#class_VisualShader_method_remove_node) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int) ) |
| void | [remove_varying](class_visualshader.md#class_VisualShader_method_remove_varying) ( name: [String](class_string.md#class_String) ) |
| void | [replace_node](class_visualshader.md#class_VisualShader_method_replace_node) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int), new_class: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_mode](class_visualshader.md#class_VisualShader_method_set_mode) ( mode: [Mode](class_shader.md#enum_Shader_Mode) ) |
| void | [set_node_position](class_visualshader.md#class_VisualShader_method_set_node_position) ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int), position: [Vector2](class_vector2.md#class_Vector2) ) |

---

### Enumerations

<span id="enum_VisualShader_Type"></span>

enum **Type**: [🔗](class_visualshader.md#enum_VisualShader_Type)

<span id="class_VisualShader_constant_TYPE_VERTEX"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_VERTEX** = `0`

A vertex shader, operating on vertices.

<span id="class_VisualShader_constant_TYPE_FRAGMENT"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_FRAGMENT** = `1`

A fragment shader, operating on fragments (pixels).

<span id="class_VisualShader_constant_TYPE_LIGHT"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_LIGHT** = `2`

A shader for light calculations.

<span id="class_VisualShader_constant_TYPE_START"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_START** = `3`

A function for the "start" stage of particle shader.

<span id="class_VisualShader_constant_TYPE_PROCESS"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_PROCESS** = `4`

A function for the "process" stage of particle shader.

<span id="class_VisualShader_constant_TYPE_COLLIDE"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_COLLIDE** = `5`

A function for the "collide" stage (particle collision handler) of particle shader.

<span id="class_VisualShader_constant_TYPE_START_CUSTOM"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_START_CUSTOM** = `6`

A function for the "start" stage of particle shader, with customized output.

<span id="class_VisualShader_constant_TYPE_PROCESS_CUSTOM"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_PROCESS_CUSTOM** = `7`

A function for the "process" stage of particle shader, with customized output.

<span id="class_VisualShader_constant_TYPE_SKY"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_SKY** = `8`

A shader for 3D environment's sky.

<span id="class_VisualShader_constant_TYPE_FOG"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_FOG** = `9`

A compute shader that runs for each froxel of the volumetric fog map.

<span id="class_VisualShader_constant_TYPE_TEXTURE_BLIT"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_TEXTURE_BLIT** = `10`

A shader used to process blit calls to a DrawableTexture.

<span id="class_VisualShader_constant_TYPE_MAX"></span>

[Type](class_visualshader.md#enum_VisualShader_Type) **TYPE_MAX** = `11`

Represents the size of the [Type](class_visualshader.md#enum_VisualShader_Type) enum.

---

<span id="enum_VisualShader_VaryingMode"></span>

enum **VaryingMode**: [🔗](class_visualshader.md#enum_VisualShader_VaryingMode)

<span id="class_VisualShader_constant_VARYING_MODE_VERTEX_TO_FRAG_LIGHT"></span>

[VaryingMode](class_visualshader.md#enum_VisualShader_VaryingMode) **VARYING_MODE_VERTEX_TO_FRAG_LIGHT** = `0`

Varying is passed from `Vertex` function to `Fragment` and `Light` functions.

<span id="class_VisualShader_constant_VARYING_MODE_FRAG_TO_LIGHT"></span>

[VaryingMode](class_visualshader.md#enum_VisualShader_VaryingMode) **VARYING_MODE_FRAG_TO_LIGHT** = `1`

Varying is passed from `Fragment` function to `Light` function.

<span id="class_VisualShader_constant_VARYING_MODE_MAX"></span>

[VaryingMode](class_visualshader.md#enum_VisualShader_VaryingMode) **VARYING_MODE_MAX** = `2`

Represents the size of the [VaryingMode](class_visualshader.md#enum_VisualShader_VaryingMode) enum.

---

<span id="enum_VisualShader_VaryingType"></span>

enum **VaryingType**: [🔗](class_visualshader.md#enum_VisualShader_VaryingType)

<span id="class_VisualShader_constant_VARYING_TYPE_FLOAT"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **VARYING_TYPE_FLOAT** = `0`

Varying is of type [float](class_float.md#class_float).

<span id="class_VisualShader_constant_VARYING_TYPE_INT"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **VARYING_TYPE_INT** = `1`

Varying is of type [int](class_int.md#class_int).

<span id="class_VisualShader_constant_VARYING_TYPE_UINT"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **VARYING_TYPE_UINT** = `2`

Varying is of type unsigned [int](class_int.md#class_int).

<span id="class_VisualShader_constant_VARYING_TYPE_VECTOR_2D"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **VARYING_TYPE_VECTOR_2D** = `3`

Varying is of type [Vector2](class_vector2.md#class_Vector2).

<span id="class_VisualShader_constant_VARYING_TYPE_VECTOR_3D"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **VARYING_TYPE_VECTOR_3D** = `4`

Varying is of type [Vector3](class_vector3.md#class_Vector3).

<span id="class_VisualShader_constant_VARYING_TYPE_VECTOR_4D"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **VARYING_TYPE_VECTOR_4D** = `5`

Varying is of type [Vector4](class_vector4.md#class_Vector4).

<span id="class_VisualShader_constant_VARYING_TYPE_BOOLEAN"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **VARYING_TYPE_BOOLEAN** = `6`

Varying is of type [bool](class_bool.md#class_bool).

<span id="class_VisualShader_constant_VARYING_TYPE_TRANSFORM"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **VARYING_TYPE_TRANSFORM** = `7`

Varying is of type [Transform3D](class_transform3d.md#class_Transform3D).

<span id="class_VisualShader_constant_VARYING_TYPE_MAX"></span>

[VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) **VARYING_TYPE_MAX** = `8`

Represents the size of the [VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) enum.

---

### Constants

<span id="class_VisualShader_constant_NODE_ID_INVALID"></span>

**NODE_ID_INVALID** = `-1` [🔗](class_visualshader.md#class_VisualShader_constant_NODE_ID_INVALID)

Indicates an invalid **VisualShader** node.

<span id="class_VisualShader_constant_NODE_ID_OUTPUT"></span>

**NODE_ID_OUTPUT** = `0` [🔗](class_visualshader.md#class_VisualShader_constant_NODE_ID_OUTPUT)

Indicates an output node of **VisualShader**.

---

### Property Descriptions

<span id="class_VisualShader_property_graph_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **graph_offset** [🔗](class_visualshader.md#class_VisualShader_property_graph_offset)

- void **set_graph_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_graph_offset** ( )

**Deprecated:** This property does nothing and always equals to zero.

Deprecated.

---

### Method Descriptions

<span id="class_VisualShader_method_add_node"></span>

void **add_node** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), node: [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode), position: [Vector2](class_vector2.md#class_Vector2), id: [int](class_int.md#class_int) ) [🔗](class_visualshader.md#class_VisualShader_method_add_node)

Adds the specified `node` to the shader.

---

<span id="class_VisualShader_method_add_varying"></span>

void **add_varying** ( name: [String](class_string.md#class_String), mode: [VaryingMode](class_visualshader.md#enum_VisualShader_VaryingMode), type: [VaryingType](class_visualshader.md#enum_VisualShader_VaryingType) ) [🔗](class_visualshader.md#class_VisualShader_method_add_varying)

Adds a new varying value node to the shader.

---

<span id="class_VisualShader_method_attach_node_to_frame"></span>

void **attach_node_to_frame** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int), frame: [int](class_int.md#class_int) ) [🔗](class_visualshader.md#class_VisualShader_method_attach_node_to_frame)

Attaches the given node to the given frame.

---

<span id="class_VisualShader_method_can_connect_nodes"></span>

[bool](class_bool.md#class_bool) **can_connect_nodes** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) *const* [🔗](class_visualshader.md#class_VisualShader_method_can_connect_nodes)

Returns `true` if the specified nodes and ports can be connected together.

---

<span id="class_VisualShader_method_connect_nodes"></span>

Error **connect_nodes** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) [🔗](class_visualshader.md#class_VisualShader_method_connect_nodes)

Connects the specified nodes and ports.

---

<span id="class_VisualShader_method_connect_nodes_forced"></span>

void **connect_nodes_forced** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) [🔗](class_visualshader.md#class_VisualShader_method_connect_nodes_forced)

Connects the specified nodes and ports, even if they can't be connected. Such connection is invalid and will not function properly.

---

<span id="class_VisualShader_method_detach_node_from_frame"></span>

void **detach_node_from_frame** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int) ) [🔗](class_visualshader.md#class_VisualShader_method_detach_node_from_frame)

Detaches the given node from the frame it is attached to.

---

<span id="class_VisualShader_method_disconnect_nodes"></span>

void **disconnect_nodes** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) [🔗](class_visualshader.md#class_VisualShader_method_disconnect_nodes)

Connects the specified nodes and ports.

---

<span id="class_VisualShader_method_get_node"></span>

[VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **get_node** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int) ) *const* [🔗](class_visualshader.md#class_VisualShader_method_get_node)

Returns the shader node instance with specified `type` and `id`.

---

<span id="class_VisualShader_method_get_node_connections"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_node_connections** ( type: [Type](class_visualshader.md#enum_VisualShader_Type) ) *const* [🔗](class_visualshader.md#class_VisualShader_method_get_node_connections)

Returns the list of connected nodes with the specified type.

---

<span id="class_VisualShader_method_get_node_list"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_node_list** ( type: [Type](class_visualshader.md#enum_VisualShader_Type) ) *const* [🔗](class_visualshader.md#class_VisualShader_method_get_node_list)

Returns the list of all nodes in the shader with the specified type.

---

<span id="class_VisualShader_method_get_node_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_node_position** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int) ) *const* [🔗](class_visualshader.md#class_VisualShader_method_get_node_position)

Returns the position of the specified node within the shader graph.

---

<span id="class_VisualShader_method_get_valid_node_id"></span>

[int](class_int.md#class_int) **get_valid_node_id** ( type: [Type](class_visualshader.md#enum_VisualShader_Type) ) *const* [🔗](class_visualshader.md#class_VisualShader_method_get_valid_node_id)

Returns next valid node ID that can be added to the shader graph.

---

<span id="class_VisualShader_method_has_varying"></span>

[bool](class_bool.md#class_bool) **has_varying** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_visualshader.md#class_VisualShader_method_has_varying)

Returns `true` if the shader has a varying with the given `name`.

---

<span id="class_VisualShader_method_is_node_connection"></span>

[bool](class_bool.md#class_bool) **is_node_connection** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), from_node: [int](class_int.md#class_int), from_port: [int](class_int.md#class_int), to_node: [int](class_int.md#class_int), to_port: [int](class_int.md#class_int) ) *const* [🔗](class_visualshader.md#class_VisualShader_method_is_node_connection)

Returns `true` if the specified node and port connection exist.

---

<span id="class_VisualShader_method_remove_node"></span>

void **remove_node** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int) ) [🔗](class_visualshader.md#class_VisualShader_method_remove_node)

Removes the specified node from the shader.

---

<span id="class_VisualShader_method_remove_varying"></span>

void **remove_varying** ( name: [String](class_string.md#class_String) ) [🔗](class_visualshader.md#class_VisualShader_method_remove_varying)

Removes a varying value node with the given `name`. Prints an error if a node with this name is not found.

---

<span id="class_VisualShader_method_replace_node"></span>

void **replace_node** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int), new_class: [StringName](class_stringname.md#class_StringName) ) [🔗](class_visualshader.md#class_VisualShader_method_replace_node)

Replaces the specified node with a node of new class type.

---

<span id="class_VisualShader_method_set_mode"></span>

void **set_mode** ( mode: [Mode](class_shader.md#enum_Shader_Mode) ) [🔗](class_visualshader.md#class_VisualShader_method_set_mode)

Sets the mode of this shader.

---

<span id="class_VisualShader_method_set_node_position"></span>

void **set_node_position** ( type: [Type](class_visualshader.md#enum_VisualShader_Type), id: [int](class_int.md#class_int), position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_visualshader.md#class_VisualShader_method_set_node_position)

Sets the position of the specified node.
