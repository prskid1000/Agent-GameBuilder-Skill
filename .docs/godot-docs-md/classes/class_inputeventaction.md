<span id="class_InputEventAction"></span>

## InputEventAction

**Inherits:** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An input event type for actions.

### Description

Contains a generic action which can be targeted from several types of inputs. Actions and their events can be set in the **Input Map** tab in **Project > Project Settings**, or with the [InputMap](class_inputmap.md#class_InputMap) class.

 **Note:** Unlike the other [InputEvent](class_inputevent.md#class_InputEvent) subclasses which map to unique physical events, this virtual one is not emitted by the engine. This class is useful to emit actions manually with [Input.parse_input_event()](class_input.md#class_Input_method_parse_input_event), which are then received in [Node._input()](class_node.md#class_Node_private_method__input). To check if a physical event matches an action from the Input Map, use [InputEvent.is_action()](class_inputevent.md#class_InputEvent_method_is_action) and [InputEvent.is_action_pressed()](class_inputevent.md#class_InputEvent_method_is_action_pressed).

### Tutorials

- `Using InputEvent: Actions <../tutorials/inputs/inputevent.html#actions>`__

- 2D Dodge The Creeps Demo

- 3D Voxel Demo

### Properties


| [StringName](class_stringname.md#class_StringName) | [action](class_inputeventaction.md#class_InputEventAction_property_action) | `&""` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [event_index](class_inputeventaction.md#class_InputEventAction_property_event_index) | `-1` |
| [bool](class_bool.md#class_bool) | [pressed](class_inputeventaction.md#class_InputEventAction_property_pressed) | `false` |
| [float](class_float.md#class_float) | [strength](class_inputeventaction.md#class_InputEventAction_property_strength) | `1.0` |

---

### Property Descriptions

<span id="class_InputEventAction_property_action"></span>

[StringName](class_stringname.md#class_StringName) **action** = `&""` [🔗](class_inputeventaction.md#class_InputEventAction_property_action)

- void **set_action** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_action** ( )

The action's name. This is usually the name of an existing action in the [InputMap](class_inputmap.md#class_InputMap) which you want this custom event to match.

---

<span id="class_InputEventAction_property_event_index"></span>

[int](class_int.md#class_int) **event_index** = `-1` [🔗](class_inputeventaction.md#class_InputEventAction_property_event_index)

- void **set_event_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_event_index** ( )

The real event index in action this event corresponds to (from events defined for this action in the [InputMap](class_inputmap.md#class_InputMap)). If `-1`, a unique ID will be used and actions pressed with this ID will need to be released with another **InputEventAction**.

---

<span id="class_InputEventAction_property_pressed"></span>

[bool](class_bool.md#class_bool) **pressed** = `false` [🔗](class_inputeventaction.md#class_InputEventAction_property_pressed)

- void **set_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pressed** ( )

If `true`, the action's state is pressed. If `false`, the action's state is released.

---

<span id="class_InputEventAction_property_strength"></span>

[float](class_float.md#class_float) **strength** = `1.0` [🔗](class_inputeventaction.md#class_InputEventAction_property_strength)

- void **set_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_strength** ( )

The action's strength between 0 and 1. This value is considered as equal to 0 if pressed is `false`. The event strength allows faking analog joypad motion events, by specifying how strongly the joypad axis is bent or pressed.
