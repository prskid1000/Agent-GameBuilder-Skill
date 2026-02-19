.. meta::
	:keywords: gamepad, controller

<span id="class_InputEventJoypadMotion"></span>

## InputEventJoypadMotion

**Inherits:** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents axis motions (such as joystick or analog triggers) from a gamepad.

### Description

Stores information about joystick motions. One **InputEventJoypadMotion** represents one axis at a time. For gamepad buttons, see [InputEventJoypadButton](class_inputeventjoypadbutton.md#class_InputEventJoypadButton).

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| JoyAxis | [axis](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion_property_axis) | `0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [axis_value](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion_property_axis_value) | `0.0` |

---

### Property Descriptions

<span id="class_InputEventJoypadMotion_property_axis"></span>

JoyAxis **axis** = `0` [🔗](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion_property_axis)

- void **set_axis** ( value: JoyAxis )
- JoyAxis **get_axis** ( )

Axis identifier.

---

<span id="class_InputEventJoypadMotion_property_axis_value"></span>

[float](class_float.md#class_float) **axis_value** = `0.0` [🔗](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion_property_axis_value)

- void **set_axis_value** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_axis_value** ( )

Current position of the joystick on the given axis. The value ranges from `-1.0` to `1.0`. A value of `0` means the axis is in its resting position.
