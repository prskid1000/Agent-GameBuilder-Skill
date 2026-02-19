.. meta::
	:keywords: gamepad, controller

<span id="class_InputEventJoypadButton"></span>

## InputEventJoypadButton

**Inherits:** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a gamepad button being pressed or released.

### Description

Input event type for gamepad buttons. For gamepad analog sticks and joysticks, see [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion).

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| JoyButton | [button_index](class_inputeventjoypadbutton.md#class_InputEventJoypadButton_property_button_index) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [pressed](class_inputeventjoypadbutton.md#class_InputEventJoypadButton_property_pressed) | `false` |
| [float](class_float.md#class_float) | [pressure](class_inputeventjoypadbutton.md#class_InputEventJoypadButton_property_pressure) | `0.0` |

---

### Property Descriptions

<span id="class_InputEventJoypadButton_property_button_index"></span>

JoyButton **button_index** = `0` [🔗](class_inputeventjoypadbutton.md#class_InputEventJoypadButton_property_button_index)

- void **set_button_index** ( value: JoyButton )
- JoyButton **get_button_index** ( )

Button identifier. One of the JoyButton button constants.

---

<span id="class_InputEventJoypadButton_property_pressed"></span>

[bool](class_bool.md#class_bool) **pressed** = `false` [🔗](class_inputeventjoypadbutton.md#class_InputEventJoypadButton_property_pressed)

- void **set_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pressed** ( )

If `true`, the button's state is pressed. If `false`, the button's state is released.

---

<span id="class_InputEventJoypadButton_property_pressure"></span>

[float](class_float.md#class_float) **pressure** = `0.0` [🔗](class_inputeventjoypadbutton.md#class_InputEventJoypadButton_property_pressure)

- void **set_pressure** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pressure** ( )

**Deprecated:** This property is never set by the engine and is always `0`.
