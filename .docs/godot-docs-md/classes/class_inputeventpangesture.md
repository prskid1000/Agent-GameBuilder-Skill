<span id="class_InputEventPanGesture"></span>

## InputEventPanGesture

**Inherits:** [InputEventGesture](class_inputeventgesture.md#class_InputEventGesture) **<** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow) **<** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a panning touch gesture.

### Description

Stores information about pan gestures. A pan gesture is performed when the user swipes the touch screen with two fingers. It's typically used for panning/scrolling.

 **Note:** On Android, this requires the ProjectSettings.input_devices/pointing/android/enable_pan_and_scale_gestures project setting to be enabled.

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [delta](class_inputeventpangesture.md#class_InputEventPanGesture_property_delta) | `Vector2(0, 0)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_InputEventPanGesture_property_delta"></span>

[Vector2](class_vector2.md#class_Vector2) **delta** = `Vector2(0, 0)` [🔗](class_inputeventpangesture.md#class_InputEventPanGesture_property_delta)

- void **set_delta** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_delta** ( )

Panning amount since last pan event.
