<span id="class_InputEventMagnifyGesture"></span>

## InputEventMagnifyGesture

**Inherits:** [InputEventGesture](class_inputeventgesture.md#class_InputEventGesture) **<** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow) **<** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a magnifying touch gesture.

### Description

Stores the factor of a magnifying touch gesture. This is usually performed when the user pinches the touch screen and used for zooming in/out.

 **Note:** On Android, this requires the ProjectSettings.input_devices/pointing/android/enable_pan_and_scale_gestures project setting to be enabled.

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| [float](class_float.md#class_float) | [factor](class_inputeventmagnifygesture.md#class_InputEventMagnifyGesture_property_factor) | `1.0` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_InputEventMagnifyGesture_property_factor"></span>

[float](class_float.md#class_float) **factor** = `1.0` [🔗](class_inputeventmagnifygesture.md#class_InputEventMagnifyGesture_property_factor)

- void **set_factor** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_factor** ( )

The amount (or delta) of the event. This value is closer to `1.0` the slower the gesture is performed.
