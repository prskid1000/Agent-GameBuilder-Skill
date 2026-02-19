<span id="class_AnimationNodeStateMachinePlayback"></span>

## AnimationNodeStateMachinePlayback

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides playback control for an [AnimationNodeStateMachine](class_animationnodestatemachine.md#class_AnimationNodeStateMachine).

### Description

Allows control of [AnimationTree](class_animationtree.md#class_AnimationTree) state machines created with [AnimationNodeStateMachine](class_animationnodestatemachine.md#class_AnimationNodeStateMachine). Retrieve with `$AnimationTree.get("parameters/playback")`.

.. tabs::

```
```

    var state_machine = $AnimationTree.get("parameters/playback")
    state_machine.travel("some_state")

```
```

    var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback").As<AnimationNodeStateMachinePlayback>();
    stateMachine.Travel("some_state");

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

### Properties


| [bool](class_bool.md#class_bool) | resource_local_to_scene | `true` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| --- | --- | --- |

### Methods


| [float](class_float.md#class_float) | [get_current_length](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_current_length) ( ) const |
| --- | --- |
| [StringName](class_stringname.md#class_StringName) | [get_current_node](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_current_node) ( ) const |
| [float](class_float.md#class_float) | [get_current_play_position](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_current_play_position) ( ) const |
| [float](class_float.md#class_float) | [get_fading_from_length](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_from_length) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_fading_from_node](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_from_node) ( ) const |
| [float](class_float.md#class_float) | [get_fading_from_play_position](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_from_play_position) ( ) const |
| [float](class_float.md#class_float) | [get_fading_length](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_length) ( ) const |
| [float](class_float.md#class_float) | [get_fading_position](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_position) ( ) const |
| [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] | [get_travel_path](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_travel_path) ( ) const |
| [bool](class_bool.md#class_bool) | [is_playing](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_is_playing) ( ) const |
| void | [next](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_next) ( ) |
| void | [start](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_start) ( node: [StringName](class_stringname.md#class_StringName), reset: [bool](class_bool.md#class_bool) = true ) |
| void | [stop](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_stop) ( ) |
| void | [travel](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_travel) ( to_node: [StringName](class_stringname.md#class_StringName), reset_on_teleport: [bool](class_bool.md#class_bool) = true ) |

---

### Signals

<span id="class_AnimationNodeStateMachinePlayback_signal_state_finished"></span>

**state_finished** ( state: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_signal_state_finished)

Emitted when the `state` finishes playback. If `state` is a state machine set to grouped mode, its signals are passed through with its name prefixed.

If there is a crossfade, this will be fired when the influence of the [get_fading_from_node()](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_from_node) animation is no longer present.

---

<span id="class_AnimationNodeStateMachinePlayback_signal_state_started"></span>

**state_started** ( state: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_signal_state_started)

Emitted when the `state` starts playback. If `state` is a state machine set to grouped mode, its signals are passed through with its name prefixed.

---

### Method Descriptions

<span id="class_AnimationNodeStateMachinePlayback_method_get_current_length"></span>

[float](class_float.md#class_float) **get_current_length** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_current_length)

Returns the current state length.

 **Note:** It is possible that any [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) can be nodes as well as animations. This means that there can be multiple animations within a single state. Which animation length has priority depends on the nodes connected inside it. Also, if a transition does not reset, the remaining length at that point will be returned.

---

<span id="class_AnimationNodeStateMachinePlayback_method_get_current_node"></span>

[StringName](class_stringname.md#class_StringName) **get_current_node** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_current_node)

Returns the currently playing animation state.

 **Note:** When using a cross-fade, the current state changes to the next state immediately after the cross-fade begins.

---

<span id="class_AnimationNodeStateMachinePlayback_method_get_current_play_position"></span>

[float](class_float.md#class_float) **get_current_play_position** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_current_play_position)

Returns the playback position within the current animation state.

---

<span id="class_AnimationNodeStateMachinePlayback_method_get_fading_from_length"></span>

[float](class_float.md#class_float) **get_fading_from_length** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_from_length)

Returns the playback state length of the node from [get_fading_from_node()](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_from_node). Returns `0` if no animation fade is occurring.

---

<span id="class_AnimationNodeStateMachinePlayback_method_get_fading_from_node"></span>

[StringName](class_stringname.md#class_StringName) **get_fading_from_node** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_from_node)

Returns the starting state of currently fading animation.

---

<span id="class_AnimationNodeStateMachinePlayback_method_get_fading_from_play_position"></span>

[float](class_float.md#class_float) **get_fading_from_play_position** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_from_play_position)

Returns the playback position of the node from [get_fading_from_node()](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_from_node). Returns `0` if no animation fade is occurring.

---

<span id="class_AnimationNodeStateMachinePlayback_method_get_fading_length"></span>

[float](class_float.md#class_float) **get_fading_length** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_length)

Returns the length of the current fade animation. Returns `0` if no animation fade is occurring.

---

<span id="class_AnimationNodeStateMachinePlayback_method_get_fading_position"></span>

[float](class_float.md#class_float) **get_fading_position** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_fading_position)

Returns the playback position of the current fade animation. Returns `0` if no animation fade is occurring.

---

<span id="class_AnimationNodeStateMachinePlayback_method_get_travel_path"></span>

[Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] **get_travel_path** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_get_travel_path)

Returns the current travel path as computed internally by the A\* algorithm.

---

<span id="class_AnimationNodeStateMachinePlayback_method_is_playing"></span>

[bool](class_bool.md#class_bool) **is_playing** ( ) *const* [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_is_playing)

Returns `true` if an animation is playing.

---

<span id="class_AnimationNodeStateMachinePlayback_method_next"></span>

void **next** ( ) [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_next)

If there is a next path by travel or auto advance, immediately transitions from the current state to the next state.

---

<span id="class_AnimationNodeStateMachinePlayback_method_start"></span>

void **start** ( node: [StringName](class_stringname.md#class_StringName), reset: [bool](class_bool.md#class_bool) = true ) [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_start)

Starts playing the given animation.

If `reset` is `true`, the animation is played from the beginning.

---

<span id="class_AnimationNodeStateMachinePlayback_method_stop"></span>

void **stop** ( ) [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_stop)

Stops the currently playing animation.

---

<span id="class_AnimationNodeStateMachinePlayback_method_travel"></span>

void **travel** ( to_node: [StringName](class_stringname.md#class_StringName), reset_on_teleport: [bool](class_bool.md#class_bool) = true ) [🔗](class_animationnodestatemachineplayback.md#class_AnimationNodeStateMachinePlayback_method_travel)

Transitions from the current state to another one, following the shortest path.

If the path does not connect from the current state, the animation will play after the state teleports.

If `reset_on_teleport` is `true`, the animation is played from the beginning when the travel cause a teleportation.
