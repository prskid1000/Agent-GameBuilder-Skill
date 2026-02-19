<span id="class_AnimationNodeBlendTree"></span>

## AnimationNodeBlendTree

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A sub-tree of many type [AnimationNode](class_animationnode.md#class_AnimationNode) s used for complex animations. Used by [AnimationTree](class_animationtree.md#class_AnimationTree).

### Description

This animation node may contain a sub-tree of any other type animation nodes, such as [AnimationNodeTransition](class_animationnodetransition.md#class_AnimationNodeTransition), [AnimationNodeBlend2](class_animationnodeblend2.md#class_AnimationNodeBlend2), [AnimationNodeBlend3](class_animationnodeblend3.md#class_AnimationNodeBlend3), [AnimationNodeOneShot](class_animationnodeoneshot.md#class_AnimationNodeOneShot), etc. This is one of the most commonly used animation node roots.

An [AnimationNodeOutput](class_animationnodeoutput.md#class_AnimationNodeOutput) node named `output` is created by default.

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [graph_offset](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_property_graph_offset) | `Vector2(0, 0)` |
| --- | --- | --- |

### Methods


| void | [add_node](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_add_node) ( name: [StringName](class_stringname.md#class_StringName), node: [AnimationNode](class_animationnode.md#class_AnimationNode), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| --- | --- |
| void | [connect_node](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_connect_node) ( input_node: [StringName](class_stringname.md#class_StringName), input_index: [int](class_int.md#class_int), output_node: [StringName](class_stringname.md#class_StringName) ) |
| void | [disconnect_node](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_disconnect_node) ( input_node: [StringName](class_stringname.md#class_StringName), input_index: [int](class_int.md#class_int) ) |
| [AnimationNode](class_animationnode.md#class_AnimationNode) | [get_node](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_get_node) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] | [get_node_list](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_get_node_list) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_node_position](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_get_node_position) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_node](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_has_node) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| void | [remove_node](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_remove_node) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_node](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_rename_node) ( name: [StringName](class_stringname.md#class_StringName), new_name: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_node_position](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_set_node_position) ( name: [StringName](class_stringname.md#class_StringName), position: [Vector2](class_vector2.md#class_Vector2) ) |

---

### Signals

<span id="class_AnimationNodeBlendTree_signal_node_changed"></span>

**node_changed** ( node_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_signal_node_changed)

Emitted when the input port information is changed.

---

### Constants

<span id="class_AnimationNodeBlendTree_constant_CONNECTION_OK"></span>

**CONNECTION_OK** = `0` [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_constant_CONNECTION_OK)

The connection was successful.

<span id="class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT"></span>

**CONNECTION_ERROR_NO_INPUT** = `1` [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT)

The input node is `null`.

<span id="class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT_INDEX"></span>

**CONNECTION_ERROR_NO_INPUT_INDEX** = `2` [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT_INDEX)

The specified input port is out of range.

<span id="class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_OUTPUT"></span>

**CONNECTION_ERROR_NO_OUTPUT** = `3` [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_OUTPUT)

The output node is `null`.

<span id="class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_SAME_NODE"></span>

**CONNECTION_ERROR_SAME_NODE** = `4` [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_SAME_NODE)

Input and output nodes are the same.

<span id="class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_CONNECTION_EXISTS"></span>

**CONNECTION_ERROR_CONNECTION_EXISTS** = `5` [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_CONNECTION_EXISTS)

The specified connection already exists.

---

### Property Descriptions

<span id="class_AnimationNodeBlendTree_property_graph_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **graph_offset** = `Vector2(0, 0)` [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_property_graph_offset)

- void **set_graph_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_graph_offset** ( )

The global offset of all sub animation nodes.

---

### Method Descriptions

<span id="class_AnimationNodeBlendTree_method_add_node"></span>

void **add_node** ( name: [StringName](class_stringname.md#class_StringName), node: [AnimationNode](class_animationnode.md#class_AnimationNode), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_add_node)

Adds an [AnimationNode](class_animationnode.md#class_AnimationNode) at the given `position`. The `name` is used to identify the created sub animation node later.

---

<span id="class_AnimationNodeBlendTree_method_connect_node"></span>

void **connect_node** ( input_node: [StringName](class_stringname.md#class_StringName), input_index: [int](class_int.md#class_int), output_node: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_connect_node)

Connects the output of an [AnimationNode](class_animationnode.md#class_AnimationNode) as input for another [AnimationNode](class_animationnode.md#class_AnimationNode), at the input port specified by `input_index`.

---

<span id="class_AnimationNodeBlendTree_method_disconnect_node"></span>

void **disconnect_node** ( input_node: [StringName](class_stringname.md#class_StringName), input_index: [int](class_int.md#class_int) ) [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_disconnect_node)

Disconnects the animation node connected to the specified input.

---

<span id="class_AnimationNodeBlendTree_method_get_node"></span>

[AnimationNode](class_animationnode.md#class_AnimationNode) **get_node** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_get_node)

Returns the sub animation node with the specified `name`.

---

<span id="class_AnimationNodeBlendTree_method_get_node_list"></span>

[Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] **get_node_list** ( ) *const* [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_get_node_list)

Returns a list containing the names of all sub animation nodes in this blend tree.

---

<span id="class_AnimationNodeBlendTree_method_get_node_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_node_position** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_get_node_position)

Returns the position of the sub animation node with the specified `name`.

---

<span id="class_AnimationNodeBlendTree_method_has_node"></span>

[bool](class_bool.md#class_bool) **has_node** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_has_node)

Returns `true` if a sub animation node with specified `name` exists.

---

<span id="class_AnimationNodeBlendTree_method_remove_node"></span>

void **remove_node** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_remove_node)

Removes a sub animation node.

---

<span id="class_AnimationNodeBlendTree_method_rename_node"></span>

void **rename_node** ( name: [StringName](class_stringname.md#class_StringName), new_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_rename_node)

Changes the name of a sub animation node.

---

<span id="class_AnimationNodeBlendTree_method_set_node_position"></span>

void **set_node_position** ( name: [StringName](class_stringname.md#class_StringName), position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_animationnodeblendtree.md#class_AnimationNodeBlendTree_method_set_node_position)

Modifies the position of a sub animation node.
