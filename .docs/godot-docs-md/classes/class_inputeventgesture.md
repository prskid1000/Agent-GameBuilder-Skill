<span id="class_InputEventGesture"></span>

## InputEventGesture

**Inherits:** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow) **<** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [InputEventMagnifyGesture](class_inputeventmagnifygesture.md#class_InputEventMagnifyGesture), [InputEventPanGesture](class_inputeventpangesture.md#class_InputEventPanGesture)

Abstract base class for touch gestures.

### Description

InputEventGestures are sent when a user performs a supported gesture on a touch screen. Gestures can't be emulated using mouse, because they typically require multi-touch.

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [position](class_inputeventgesture.md#class_InputEventGesture_property_position) | `Vector2(0, 0)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_InputEventGesture_property_position"></span>

[Vector2](class_vector2.md#class_Vector2) **position** = `Vector2(0, 0)` [🔗](class_inputeventgesture.md#class_InputEventGesture_property_position)

- void **set_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_position** ( )

The local gesture position relative to the [Viewport](class_viewport.md#class_Viewport). If used in [Control._gui_input()](class_control.md#class_Control_private_method__gui_input), the position is relative to the current [Control](class_control.md#class_Control) that received this gesture.
