<span id="class_InputEventFromWindow"></span>

## InputEventFromWindow

**Inherits:** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [InputEventScreenDrag](class_inputeventscreendrag.md#class_InputEventScreenDrag), [InputEventScreenTouch](class_inputeventscreentouch.md#class_InputEventScreenTouch), [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers)

Abstract base class for [Viewport](class_viewport.md#class_Viewport)-based input events.

### Description

InputEventFromWindow represents events specifically received by windows. This includes mouse events, keyboard events in focused windows or touch screen actions.

### Properties


| [int](class_int.md#class_int) | [window_id](class_inputeventfromwindow.md#class_InputEventFromWindow_property_window_id) | `0` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_InputEventFromWindow_property_window_id"></span>

[int](class_int.md#class_int) **window_id** = `0` [🔗](class_inputeventfromwindow.md#class_InputEventFromWindow_property_window_id)

- void **set_window_id** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_window_id** ( )

The ID of a [Window](class_window.md#class_Window) that received this event.
