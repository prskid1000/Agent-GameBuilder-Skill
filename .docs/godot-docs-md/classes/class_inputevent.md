<span id="class_InputEvent"></span>

## InputEvent

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [InputEventAction](class_inputeventaction.md#class_InputEventAction), [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow), [InputEventJoypadButton](class_inputeventjoypadbutton.md#class_InputEventJoypadButton), [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion), [InputEventMIDI](class_inputeventmidi.md#class_InputEventMIDI), [InputEventShortcut](class_inputeventshortcut.md#class_InputEventShortcut)

Abstract base class for input events.

### Description

Abstract base class of all types of input events. See [Node._input()](class_node.md#class_Node_private_method__input).

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

- [Viewport and canvas transforms](../tutorials/2d/2d_transforms.md)

- 2D Dodge The Creeps Demo

- 3D Voxel Demo

### Properties


| [int](class_int.md#class_int) | [device](class_inputevent.md#class_InputEvent_property_device) | `0` |
| --- | --- | --- |

### Methods


| [bool](class_bool.md#class_bool) | [accumulate](class_inputevent.md#class_InputEvent_method_accumulate) ( with_event: [InputEvent](class_inputevent.md#class_InputEvent) ) |
| --- | --- |
| [String](class_string.md#class_String) | [as_text](class_inputevent.md#class_InputEvent_method_as_text) ( ) const |
| [float](class_float.md#class_float) | [get_action_strength](class_inputevent.md#class_InputEvent_method_get_action_strength) ( action: [StringName](class_stringname.md#class_StringName), exact_match: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [is_action](class_inputevent.md#class_InputEvent_method_is_action) ( action: [StringName](class_stringname.md#class_StringName), exact_match: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [is_action_pressed](class_inputevent.md#class_InputEvent_method_is_action_pressed) ( action: [StringName](class_stringname.md#class_StringName), allow_echo: [bool](class_bool.md#class_bool) = false, exact_match: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [is_action_released](class_inputevent.md#class_InputEvent_method_is_action_released) ( action: [StringName](class_stringname.md#class_StringName), exact_match: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [is_action_type](class_inputevent.md#class_InputEvent_method_is_action_type) ( ) const |
| [bool](class_bool.md#class_bool) | [is_canceled](class_inputevent.md#class_InputEvent_method_is_canceled) ( ) const |
| [bool](class_bool.md#class_bool) | [is_echo](class_inputevent.md#class_InputEvent_method_is_echo) ( ) const |
| [bool](class_bool.md#class_bool) | [is_match](class_inputevent.md#class_InputEvent_method_is_match) ( event: [InputEvent](class_inputevent.md#class_InputEvent), exact_match: [bool](class_bool.md#class_bool) = true ) const |
| [bool](class_bool.md#class_bool) | [is_pressed](class_inputevent.md#class_InputEvent_method_is_pressed) ( ) const |
| [bool](class_bool.md#class_bool) | [is_released](class_inputevent.md#class_InputEvent_method_is_released) ( ) const |
| [InputEvent](class_inputevent.md#class_InputEvent) | [xformed_by](class_inputevent.md#class_InputEvent_method_xformed_by) ( xform: [Transform2D](class_transform2d.md#class_Transform2D), local_ofs: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) const |

---

### Constants

<span id="class_InputEvent_constant_DEVICE_ID_EMULATION"></span>

**DEVICE_ID_EMULATION** = `-1` [🔗](class_inputevent.md#class_InputEvent_constant_DEVICE_ID_EMULATION)

Device ID used for emulated mouse input from a touchscreen, or for emulated touch input from a mouse. This can be used to distinguish emulated mouse input from physical mouse input, or emulated touch input from physical touch input.

---

### Property Descriptions

<span id="class_InputEvent_property_device"></span>

[int](class_int.md#class_int) **device** = `0` [🔗](class_inputevent.md#class_InputEvent_property_device)

- void **set_device** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_device** ( )

The event's device ID.

 **Note:** [device](class_inputevent.md#class_InputEvent_property_device) can be negative for special use cases that don't refer to devices physically present on the system. See [DEVICE_ID_EMULATION](class_inputevent.md#class_InputEvent_constant_DEVICE_ID_EMULATION).

---

### Method Descriptions

<span id="class_InputEvent_method_accumulate"></span>

[bool](class_bool.md#class_bool) **accumulate** ( with_event: [InputEvent](class_inputevent.md#class_InputEvent) ) [🔗](class_inputevent.md#class_InputEvent_method_accumulate)

Returns `true` if the given input event and this input event can be added together (only for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class_InputEventMouseMotion)).

The given input event's position, global position and speed will be copied. The resulting `relative` is a sum of both events. Both events' modifiers have to be identical.

---

<span id="class_InputEvent_method_as_text"></span>

[String](class_string.md#class_String) **as_text** ( ) *const* [🔗](class_inputevent.md#class_InputEvent_method_as_text)

Returns a [String](class_string.md#class_String) representation of the event.

---

<span id="class_InputEvent_method_get_action_strength"></span>

[float](class_float.md#class_float) **get_action_strength** ( action: [StringName](class_stringname.md#class_StringName), exact_match: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_inputevent.md#class_InputEvent_method_get_action_strength)

Returns a value between 0.0 and 1.0 depending on the given actions' state. Useful for getting the value of events of type [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion).

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class_InputEventKey) and [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion) events.

---

<span id="class_InputEvent_method_is_action"></span>

[bool](class_bool.md#class_bool) **is_action** ( action: [StringName](class_stringname.md#class_StringName), exact_match: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_inputevent.md#class_InputEvent_method_is_action)

Returns `true` if this input event matches a pre-defined action of any type.

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class_InputEventKey) and [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion) events.

---

<span id="class_InputEvent_method_is_action_pressed"></span>

[bool](class_bool.md#class_bool) **is_action_pressed** ( action: [StringName](class_stringname.md#class_StringName), allow_echo: [bool](class_bool.md#class_bool) = false, exact_match: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_inputevent.md#class_InputEvent_method_is_action_pressed)

Returns `true` if the given action matches this event and is being pressed (and is not an echo event for [InputEventKey](class_inputeventkey.md#class_InputEventKey) events, unless `allow_echo` is `true`). Not relevant for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class_InputEventMouseMotion) or [InputEventScreenDrag](class_inputeventscreendrag.md#class_InputEventScreenDrag).

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class_InputEventKey) and [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion) events.

 **Note:** Due to keyboard ghosting, [is_action_pressed()](class_inputevent.md#class_InputEvent_method_is_action_pressed) may return `false` even if one of the action's keys is pressed. See `Input examples <../tutorials/inputs/input_examples.html#keyboard-events>`__ in the documentation for more information.

---

<span id="class_InputEvent_method_is_action_released"></span>

[bool](class_bool.md#class_bool) **is_action_released** ( action: [StringName](class_stringname.md#class_StringName), exact_match: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_inputevent.md#class_InputEvent_method_is_action_released)

Returns `true` if the given action matches this event and is released (i.e. not pressed). Not relevant for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class_InputEventMouseMotion) or [InputEventScreenDrag](class_inputeventscreendrag.md#class_InputEventScreenDrag).

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class_InputEventKey) and [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion) events.

---

<span id="class_InputEvent_method_is_action_type"></span>

[bool](class_bool.md#class_bool) **is_action_type** ( ) *const* [🔗](class_inputevent.md#class_InputEvent_method_is_action_type)

Returns `true` if this input event's type is one that can be assigned to an input action: [InputEventKey](class_inputeventkey.md#class_InputEventKey), [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton), [InputEventJoypadButton](class_inputeventjoypadbutton.md#class_InputEventJoypadButton), [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion), [InputEventAction](class_inputeventaction.md#class_InputEventAction). Returns `false` for all other input event types.

---

<span id="class_InputEvent_method_is_canceled"></span>

[bool](class_bool.md#class_bool) **is_canceled** ( ) *const* [🔗](class_inputevent.md#class_InputEvent_method_is_canceled)

Returns `true` if this input event has been canceled.

---

<span id="class_InputEvent_method_is_echo"></span>

[bool](class_bool.md#class_bool) **is_echo** ( ) *const* [🔗](class_inputevent.md#class_InputEvent_method_is_echo)

Returns `true` if this input event is an echo event (only for events of type [InputEventKey](class_inputeventkey.md#class_InputEventKey)). An echo event is a repeated key event sent when the user is holding down the key. Any other event type returns `false`.

 **Note:** The rate at which echo events are sent is typically around 20 events per second (after holding down the key for roughly half a second). However, the key repeat delay/speed can be changed by the user or disabled entirely in the operating system settings. To ensure your project works correctly on all configurations, do not assume the user has a specific key repeat configuration in your project's behavior.

---

<span id="class_InputEvent_method_is_match"></span>

[bool](class_bool.md#class_bool) **is_match** ( event: [InputEvent](class_inputevent.md#class_InputEvent), exact_match: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_inputevent.md#class_InputEvent_method_is_match)

Returns `true` if the specified `event` matches this event. Only valid for action events, which include key ([InputEventKey](class_inputeventkey.md#class_InputEventKey)), button ([InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton) or [InputEventJoypadButton](class_inputeventjoypadbutton.md#class_InputEventJoypadButton)), axis [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion), and action ([InputEventAction](class_inputeventaction.md#class_InputEventAction)) events.

If `exact_match` is `false`, the check ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class_InputEventKey) and [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion) events.

 **Note:** This method only considers the event configuration (such as the keyboard key or the joypad axis), not state information like [is_pressed()](class_inputevent.md#class_InputEvent_method_is_pressed), [is_released()](class_inputevent.md#class_InputEvent_method_is_released), [is_echo()](class_inputevent.md#class_InputEvent_method_is_echo), or [is_canceled()](class_inputevent.md#class_InputEvent_method_is_canceled).

---

<span id="class_InputEvent_method_is_pressed"></span>

[bool](class_bool.md#class_bool) **is_pressed** ( ) *const* [🔗](class_inputevent.md#class_InputEvent_method_is_pressed)

Returns `true` if this input event is pressed. Not relevant for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class_InputEventMouseMotion) or [InputEventScreenDrag](class_inputeventscreendrag.md#class_InputEventScreenDrag).

 **Note:** Due to keyboard ghosting, [is_pressed()](class_inputevent.md#class_InputEvent_method_is_pressed) may return `false` even if one of the action's keys is pressed. See `Input examples <../tutorials/inputs/input_examples.html#keyboard-events>`__ in the documentation for more information.

---

<span id="class_InputEvent_method_is_released"></span>

[bool](class_bool.md#class_bool) **is_released** ( ) *const* [🔗](class_inputevent.md#class_InputEvent_method_is_released)

Returns `true` if this input event is released. Not relevant for events of type [InputEventMouseMotion](class_inputeventmousemotion.md#class_InputEventMouseMotion) or [InputEventScreenDrag](class_inputeventscreendrag.md#class_InputEventScreenDrag).

---

<span id="class_InputEvent_method_xformed_by"></span>

[InputEvent](class_inputevent.md#class_InputEvent) **xformed_by** ( xform: [Transform2D](class_transform2d.md#class_Transform2D), local_ofs: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) *const* [🔗](class_inputevent.md#class_InputEvent_method_xformed_by)

Returns a copy of the given input event which has been offset by `local_ofs` and transformed by `xform`. Relevant for events of type [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton), [InputEventMouseMotion](class_inputeventmousemotion.md#class_InputEventMouseMotion), [InputEventScreenTouch](class_inputeventscreentouch.md#class_InputEventScreenTouch), [InputEventScreenDrag](class_inputeventscreendrag.md#class_InputEventScreenDrag), [InputEventMagnifyGesture](class_inputeventmagnifygesture.md#class_InputEventMagnifyGesture) and [InputEventPanGesture](class_inputeventpangesture.md#class_InputEventPanGesture).
