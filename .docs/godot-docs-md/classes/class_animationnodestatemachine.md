<span id="class_AnimationNodeStateMachine"></span>

## AnimationNodeStateMachine

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A state machine with multiple [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) s, used by [AnimationTree](class_animationtree.md#class_AnimationTree).

### Description

Contains multiple [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) s representing animation states, connected in a graph. State transitions can be configured to happen automatically or via code, using a shortest-path algorithm. Retrieve the [AnimationNodeStateMachinePlayback](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback) object from the [AnimationTree](class_animationtree.md#class_AnimationTree) node to control it programmatically.

.. tabs::

```
```

    var state_machine = $AnimationTree.get("parameters/playback")
    state_machine.travel("some_state")

```
```

    var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback") as AnimationNodeStateMachinePlayback;
    stateMachine.Travel("some_state");

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

### Properties


| [bool](class_bool.md#class_bool) | [allow_transition_to_self](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_property_allow_transition_to_self) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [reset_ends](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_property_reset_ends) | `false` |
| [StateMachineType](class_animationnodestatemachine.md#enum_AnimationNodeStateMachine_StateMachineType) | [state_machine_type](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_property_state_machine_type) | `0` |

### Methods


| void | [add_node](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_add_node) ( name: [StringName](class_stringname.md#class_StringName), node: [AnimationNode](class_animationnode.md#class_AnimationNode), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| --- | --- |
| void | [add_transition](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_add_transition) ( from: [StringName](class_stringname.md#class_StringName), to: [StringName](class_stringname.md#class_StringName), transition: [AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class_AnimationNodeStateMachineTransition) ) |
| [Vector2](class_vector2.md#class_Vector2) | [get_graph_offset](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_graph_offset) ( ) const |
| [AnimationNode](class_animationnode.md#class_AnimationNode) | [get_node](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_node) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] | [get_node_list](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_node_list) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_node_name](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_node_name) ( node: [AnimationNode](class_animationnode.md#class_AnimationNode) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_node_position](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_node_position) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class_AnimationNodeStateMachineTransition) | [get_transition](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_transition) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_transition_count](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_transition_count) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_transition_from](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_transition_from) ( idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_transition_to](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_transition_to) ( idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has_node](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_has_node) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_transition](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_has_transition) ( from: [StringName](class_stringname.md#class_StringName), to: [StringName](class_stringname.md#class_StringName) ) const |
| void | [remove_node](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_remove_node) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_transition](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_remove_transition) ( from: [StringName](class_stringname.md#class_StringName), to: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_transition_by_index](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_remove_transition_by_index) ( idx: [int](class_int.md#class_int) ) |
| void | [rename_node](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_rename_node) ( name: [StringName](class_stringname.md#class_StringName), new_name: [StringName](class_stringname.md#class_StringName) ) |
| void | [replace_node](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_replace_node) ( name: [StringName](class_stringname.md#class_StringName), node: [AnimationNode](class_animationnode.md#class_AnimationNode) ) |
| void | [set_graph_offset](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_set_graph_offset) ( offset: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_node_position](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_set_node_position) ( name: [StringName](class_stringname.md#class_StringName), position: [Vector2](class_vector2.md#class_Vector2) ) |

---

### Enumerations

<span id="enum_AnimationNodeStateMachine_StateMachineType"></span>

enum **StateMachineType**: [🔗](class_animationnodestatemachine.md#enum_AnimationNodeStateMachine_StateMachineType)

<span id="class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_ROOT"></span>

[StateMachineType](class_animationnodestatemachine.md#enum_AnimationNodeStateMachine_StateMachineType) **STATE_MACHINE_TYPE_ROOT** = `0`

Seeking to the beginning is treated as playing from the start state. Transition to the end state is treated as exiting the state machine.

<span id="class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_NESTED"></span>

[StateMachineType](class_animationnodestatemachine.md#enum_AnimationNodeStateMachine_StateMachineType) **STATE_MACHINE_TYPE_NESTED** = `1`

Seeking to the beginning is treated as seeking to the beginning of the animation in the current state. Transition to the end state, or the absence of transitions in each state, is treated as exiting the state machine.

<span id="class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_GROUPED"></span>

[StateMachineType](class_animationnodestatemachine.md#enum_AnimationNodeStateMachine_StateMachineType) **STATE_MACHINE_TYPE_GROUPED** = `2`

This is a grouped state machine that can be controlled from a parent state machine. It does not work independently. There must be a state machine with [state_machine_type](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_property_state_machine_type) of [STATE_MACHINE_TYPE_ROOT](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_ROOT) or [STATE_MACHINE_TYPE_NESTED](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_NESTED) in the parent or ancestor.

---

### Property Descriptions

<span id="class_AnimationNodeStateMachine_property_allow_transition_to_self"></span>

[bool](class_bool.md#class_bool) **allow_transition_to_self** = `false` [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_property_allow_transition_to_self)

- void **set_allow_transition_to_self** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_allow_transition_to_self** ( )

If `true`, allows teleport to the self state with [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_travel). When the reset option is enabled in [AnimationNodeStateMachinePlayback.travel()](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_travel), the animation is restarted. If `false`, nothing happens on the teleportation to the self state.

---

<span id="class_AnimationNodeStateMachine_property_reset_ends"></span>

[bool](class_bool.md#class_bool) **reset_ends** = `false` [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_property_reset_ends)

- void **set_reset_ends** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **are_ends_reset** ( )

If `true`, treat the cross-fade to the start and end nodes as a blend with the RESET animation.

In most cases, when additional cross-fades are performed in the parent [AnimationNode](class_animationnode.md#class_AnimationNode) of the state machine, setting this property to `false` and matching the cross-fade time of the parent [AnimationNode](class_animationnode.md#class_AnimationNode) and the state machine's start node and end node gives good results.

---

<span id="class_AnimationNodeStateMachine_property_state_machine_type"></span>

[StateMachineType](class_animationnodestatemachine.md#enum_AnimationNodeStateMachine_StateMachineType) **state_machine_type** = `0` [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_property_state_machine_type)

- void **set_state_machine_type** ( value: [StateMachineType](class_animationnodestatemachine.md#enum_AnimationNodeStateMachine_StateMachineType) )
- [StateMachineType](class_animationnodestatemachine.md#enum_AnimationNodeStateMachine_StateMachineType) **get_state_machine_type** ( )

This property can define the process of transitions for different use cases. See also [StateMachineType](class_animationnodestatemachine.md#enum_AnimationNodeStateMachine_StateMachineType).

---

### Method Descriptions

<span id="class_AnimationNodeStateMachine_method_add_node"></span>

void **add_node** ( name: [StringName](class_stringname.md#class_StringName), node: [AnimationNode](class_animationnode.md#class_AnimationNode), position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_add_node)

Adds a new animation node to the graph. The `position` is used for display in the editor.

---

<span id="class_AnimationNodeStateMachine_method_add_transition"></span>

void **add_transition** ( from: [StringName](class_stringname.md#class_StringName), to: [StringName](class_stringname.md#class_StringName), transition: [AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class_AnimationNodeStateMachineTransition) ) [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_add_transition)

Adds a transition between the given animation nodes.

---

<span id="class_AnimationNodeStateMachine_method_get_graph_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **get_graph_offset** ( ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_graph_offset)

Returns the draw offset of the graph. Used for display in the editor.

---

<span id="class_AnimationNodeStateMachine_method_get_node"></span>

[AnimationNode](class_animationnode.md#class_AnimationNode) **get_node** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_node)

Returns the animation node with the given name.

---

<span id="class_AnimationNodeStateMachine_method_get_node_list"></span>

[Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] **get_node_list** ( ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_node_list)

Returns a list containing the names of all animation nodes in this state machine.

---

<span id="class_AnimationNodeStateMachine_method_get_node_name"></span>

[StringName](class_stringname.md#class_StringName) **get_node_name** ( node: [AnimationNode](class_animationnode.md#class_AnimationNode) ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_node_name)

Returns the given animation node's name.

---

<span id="class_AnimationNodeStateMachine_method_get_node_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_node_position** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_node_position)

Returns the given animation node's coordinates. Used for display in the editor.

---

<span id="class_AnimationNodeStateMachine_method_get_transition"></span>

[AnimationNodeStateMachineTransition](class_animationnodestatemachinetransition.md#class_AnimationNodeStateMachineTransition) **get_transition** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_transition)

Returns the given transition.

---

<span id="class_AnimationNodeStateMachine_method_get_transition_count"></span>

[int](class_int.md#class_int) **get_transition_count** ( ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_transition_count)

Returns the number of connections in the graph.

---

<span id="class_AnimationNodeStateMachine_method_get_transition_from"></span>

[StringName](class_stringname.md#class_StringName) **get_transition_from** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_transition_from)

Returns the given transition's start node.

---

<span id="class_AnimationNodeStateMachine_method_get_transition_to"></span>

[StringName](class_stringname.md#class_StringName) **get_transition_to** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_get_transition_to)

Returns the given transition's end node.

---

<span id="class_AnimationNodeStateMachine_method_has_node"></span>

[bool](class_bool.md#class_bool) **has_node** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_has_node)

Returns `true` if the graph contains the given animation node.

---

<span id="class_AnimationNodeStateMachine_method_has_transition"></span>

[bool](class_bool.md#class_bool) **has_transition** ( from: [StringName](class_stringname.md#class_StringName), to: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_has_transition)

Returns `true` if there is a transition between the given animation nodes.

---

<span id="class_AnimationNodeStateMachine_method_remove_node"></span>

void **remove_node** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_remove_node)

Deletes the given animation node from the graph.

---

<span id="class_AnimationNodeStateMachine_method_remove_transition"></span>

void **remove_transition** ( from: [StringName](class_stringname.md#class_StringName), to: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_remove_transition)

Deletes the transition between the two specified animation nodes.

---

<span id="class_AnimationNodeStateMachine_method_remove_transition_by_index"></span>

void **remove_transition_by_index** ( idx: [int](class_int.md#class_int) ) [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_remove_transition_by_index)

Deletes the given transition by index.

---

<span id="class_AnimationNodeStateMachine_method_rename_node"></span>

void **rename_node** ( name: [StringName](class_stringname.md#class_StringName), new_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_rename_node)

Renames the given animation node.

---

<span id="class_AnimationNodeStateMachine_method_replace_node"></span>

void **replace_node** ( name: [StringName](class_stringname.md#class_StringName), node: [AnimationNode](class_animationnode.md#class_AnimationNode) ) [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_replace_node)

Replaces the given animation node with a new animation node.

---

<span id="class_AnimationNodeStateMachine_method_set_graph_offset"></span>

void **set_graph_offset** ( offset: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_set_graph_offset)

Sets the draw offset of the graph. Used for display in the editor.

---

<span id="class_AnimationNodeStateMachine_method_set_node_position"></span>

void **set_node_position** ( name: [StringName](class_stringname.md#class_StringName), position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_animationnodestatemachine.md#class_AnimationNodeStateMachine_method_set_node_position)

Sets the animation node's coordinates. Used for display in the editor.
