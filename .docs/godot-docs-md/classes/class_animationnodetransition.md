<span id="class_AnimationNodeTransition"></span>

## AnimationNodeTransition

**Inherits:** [AnimationNodeSync](class_animationnodesync.md#class_AnimationNodeSync) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A transition within an [AnimationTree](class_animationtree.md#class_AnimationTree) connecting two [AnimationNode](class_animationnode.md#class_AnimationNode) s.

### Description

Simple state machine for cases which don't require a more advanced [AnimationNodeStateMachine](class_animationnodestatemachine.md#class_AnimationNodeStateMachine). Animations can be connected to the inputs and transition times can be specified.

After setting the request and changing the animation playback, the transition node automatically clears the request on the next process frame by setting its `transition_request` value to empty.

 **Note:** When using a cross-fade, `current_state` and `current_index` change to the next state immediately after the cross-fade begins.

.. tabs::

```
```

    # Play child animation connected to "state_2" port.
    animation_tree.set("parameters/Transition/transition_request", "state_2")
    # Alternative syntax (same result as above).
    animation_tree["parameters/Transition/transition_request"] = "state_2"

    # Get current state name (read-only).
    animation_tree.get("parameters/Transition/current_state")
    # Alternative syntax (same result as above).
    animation_tree["parameters/Transition/current_state"]

    # Get current state index (read-only).
    animation_tree.get("parameters/Transition/current_index")
    # Alternative syntax (same result as above).
    animation_tree["parameters/Transition/current_index"]

```
```

    // Play child animation connected to "state_2" port.
    animationTree.Set("parameters/Transition/transition_request", "state_2");

    // Get current state name (read-only).
    animationTree.Get("parameters/Transition/current_state");

    // Get current state index (read-only).
    animationTree.Get("parameters/Transition/current_index");

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

- 3D Platformer Demo

- Third Person Shooter (TPS) Demo

### Properties


| [bool](class_bool.md#class_bool) | [allow_transition_to_self](class_animationnodetransition.md#class_AnimationNodeTransition_property_allow_transition_to_self) | `false` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [input_count](class_animationnodetransition.md#class_AnimationNodeTransition_property_input_count) | `0` |
| [Curve](class_curve.md#class_Curve) | [xfade_curve](class_animationnodetransition.md#class_AnimationNodeTransition_property_xfade_curve) |
| [float](class_float.md#class_float) | [xfade_time](class_animationnodetransition.md#class_AnimationNodeTransition_property_xfade_time) | `0.0` |

### Methods


| [bool](class_bool.md#class_bool) | [is_input_loop_broken_at_end](class_animationnodetransition.md#class_AnimationNodeTransition_method_is_input_loop_broken_at_end) ( input: [int](class_int.md#class_int) ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [is_input_reset](class_animationnodetransition.md#class_AnimationNodeTransition_method_is_input_reset) ( input: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_input_set_as_auto_advance](class_animationnodetransition.md#class_AnimationNodeTransition_method_is_input_set_as_auto_advance) ( input: [int](class_int.md#class_int) ) const |
| void | [set_input_as_auto_advance](class_animationnodetransition.md#class_AnimationNodeTransition_method_set_input_as_auto_advance) ( input: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_input_break_loop_at_end](class_animationnodetransition.md#class_AnimationNodeTransition_method_set_input_break_loop_at_end) ( input: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_input_reset](class_animationnodetransition.md#class_AnimationNodeTransition_method_set_input_reset) ( input: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_AnimationNodeTransition_property_allow_transition_to_self"></span>

[bool](class_bool.md#class_bool) **allow_transition_to_self** = `false` [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_property_allow_transition_to_self)

- void **set_allow_transition_to_self** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_allow_transition_to_self** ( )

If `true`, allows transition to the self state. When the reset option is enabled in input, the animation is restarted. If `false`, nothing happens on the transition to the self state.

---

<span id="class_AnimationNodeTransition_property_input_count"></span>

[int](class_int.md#class_int) **input_count** = `0` [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_property_input_count)

- void **set_input_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_input_count** ( )

The number of enabled input ports for this animation node.

---

<span id="class_AnimationNodeTransition_property_xfade_curve"></span>

[Curve](class_curve.md#class_Curve) **xfade_curve** [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_property_xfade_curve)

- void **set_xfade_curve** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_xfade_curve** ( )

Determines how cross-fading between animations is eased. If empty, the transition will be linear. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_AnimationNodeTransition_property_xfade_time"></span>

[float](class_float.md#class_float) **xfade_time** = `0.0` [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_property_xfade_time)

- void **set_xfade_time** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_xfade_time** ( )

Cross-fading time (in seconds) between each animation connected to the inputs.

 **Note:** **AnimationNodeTransition** transitions the current state immediately after the start of the fading. The precise remaining time can only be inferred from the main animation. When [AnimationNodeOutput](class_animationnodeoutput.md#class_AnimationNodeOutput) is considered as the most upstream, so the [xfade_time](class_animationnodetransition.md#class_AnimationNodeTransition_property_xfade_time) is not scaled depending on the downstream delta. See also [AnimationNodeOneShot.fadeout_time](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_fadeout_time).

---

### Method Descriptions

<span id="class_AnimationNodeTransition_method_is_input_loop_broken_at_end"></span>

[bool](class_bool.md#class_bool) **is_input_loop_broken_at_end** ( input: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_method_is_input_loop_broken_at_end)

Returns whether the animation breaks the loop at the end of the loop cycle for transition.

---

<span id="class_AnimationNodeTransition_method_is_input_reset"></span>

[bool](class_bool.md#class_bool) **is_input_reset** ( input: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_method_is_input_reset)

Returns whether the animation restarts when the animation transitions from the other animation.

---

<span id="class_AnimationNodeTransition_method_is_input_set_as_auto_advance"></span>

[bool](class_bool.md#class_bool) **is_input_set_as_auto_advance** ( input: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_method_is_input_set_as_auto_advance)

Returns `true` if auto-advance is enabled for the given `input` index.

---

<span id="class_AnimationNodeTransition_method_set_input_as_auto_advance"></span>

void **set_input_as_auto_advance** ( input: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_method_set_input_as_auto_advance)

Enables or disables auto-advance for the given `input` index. If enabled, state changes to the next input after playing the animation once. If enabled for the last input state, it loops to the first.

---

<span id="class_AnimationNodeTransition_method_set_input_break_loop_at_end"></span>

void **set_input_break_loop_at_end** ( input: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_method_set_input_break_loop_at_end)

If `true`, breaks the loop at the end of the loop cycle for transition, even if the animation is looping.

---

<span id="class_AnimationNodeTransition_method_set_input_reset"></span>

void **set_input_reset** ( input: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_animationnodetransition.md#class_AnimationNodeTransition_method_set_input_reset)

If `true`, the destination animation is restarted when the animation transitions.
