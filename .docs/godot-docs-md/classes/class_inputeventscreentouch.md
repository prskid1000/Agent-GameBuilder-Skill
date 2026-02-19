<span id="class_InputEventScreenTouch"></span>

## InputEventScreenTouch

**Inherits:** [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow) **<** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a screen touch event.

### Description

Stores information about multi-touch press/release input events. Supports touch press, touch release and [index](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_index) for multi-touch count and order.

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| [bool](class_bool.md#class_bool) | [canceled](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_canceled) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [double_tap](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_double_tap) | `false` |
| [int](class_int.md#class_int) | [index](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_index) | `0` |
| [Vector2](class_vector2.md#class_Vector2) | [position](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_position) | `Vector2(0, 0)` |
| [bool](class_bool.md#class_bool) | [pressed](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_pressed) | `false` |

---

### Property Descriptions

<span id="class_InputEventScreenTouch_property_canceled"></span>

[bool](class_bool.md#class_bool) **canceled** = `false` [🔗](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_canceled)

- void **set_canceled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_canceled** ( )

If `true`, the touch event has been canceled.

---

<span id="class_InputEventScreenTouch_property_double_tap"></span>

[bool](class_bool.md#class_bool) **double_tap** = `false` [🔗](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_double_tap)

- void **set_double_tap** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_double_tap** ( )

If `true`, the touch's state is a double tap.

---

<span id="class_InputEventScreenTouch_property_index"></span>

[int](class_int.md#class_int) **index** = `0` [🔗](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_index)

- void **set_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_index** ( )

The touch index in the case of a multi-touch event. One index = one finger.

---

<span id="class_InputEventScreenTouch_property_position"></span>

[Vector2](class_vector2.md#class_Vector2) **position** = `Vector2(0, 0)` [🔗](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_position)

- void **set_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_position** ( )

The touch position in the viewport the node is in, using the coordinate system of this viewport.

---

<span id="class_InputEventScreenTouch_property_pressed"></span>

[bool](class_bool.md#class_bool) **pressed** = `false` [🔗](class_inputeventscreentouch.md#class_InputEventScreenTouch_property_pressed)

- void **set_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pressed** ( )

If `true`, the touch's state is pressed. If `false`, the touch's state is released.
