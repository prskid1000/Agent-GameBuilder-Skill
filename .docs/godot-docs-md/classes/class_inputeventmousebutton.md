.. meta::
	:keywords: click, press

<span id="class_InputEventMouseButton"></span>

## InputEventMouseButton

**Inherits:** [InputEventMouse](class_inputeventmouse.md#class_InputEventMouse) **<** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow) **<** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a mouse button being pressed or released.

### Description

Stores information about mouse click events. See [Node._input()](class_node.md#class_Node_private_method__input).

 **Note:** On Wear OS devices, rotary input is mapped to @GlobalScope.MOUSE_BUTTON_WHEEL_UP and @GlobalScope.MOUSE_BUTTON_WHEEL_DOWN. This can be changed to @GlobalScope.MOUSE_BUTTON_WHEEL_LEFT and @GlobalScope.MOUSE_BUTTON_WHEEL_RIGHT with the ProjectSettings.input_devices/pointing/android/rotary_input_scroll_axis setting.

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

- [Mouse and input coordinates](../tutorials/inputs/mouse_and_input_coordinates.md)

### Properties


| MouseButton | [button_index](class_inputeventmousebutton.md#class_InputEventMouseButton_property_button_index) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [canceled](class_inputeventmousebutton.md#class_InputEventMouseButton_property_canceled) | `false` |
| [bool](class_bool.md#class_bool) | [double_click](class_inputeventmousebutton.md#class_InputEventMouseButton_property_double_click) | `false` |
| [float](class_float.md#class_float) | [factor](class_inputeventmousebutton.md#class_InputEventMouseButton_property_factor) | `1.0` |
| [bool](class_bool.md#class_bool) | [pressed](class_inputeventmousebutton.md#class_InputEventMouseButton_property_pressed) | `false` |

---

### Property Descriptions

<span id="class_InputEventMouseButton_property_button_index"></span>

MouseButton **button_index** = `0` [🔗](class_inputeventmousebutton.md#class_InputEventMouseButton_property_button_index)

- void **set_button_index** ( value: MouseButton )
- MouseButton **get_button_index** ( )

The mouse button identifier, one of the MouseButton button or button wheel constants.

---

<span id="class_InputEventMouseButton_property_canceled"></span>

[bool](class_bool.md#class_bool) **canceled** = `false` [🔗](class_inputeventmousebutton.md#class_InputEventMouseButton_property_canceled)

- void **set_canceled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_canceled** ( )

If `true`, the mouse button event has been canceled.

---

<span id="class_InputEventMouseButton_property_double_click"></span>

[bool](class_bool.md#class_bool) **double_click** = `false` [🔗](class_inputeventmousebutton.md#class_InputEventMouseButton_property_double_click)

- void **set_double_click** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_double_click** ( )

If `true`, the mouse button's state is a double-click.

---

<span id="class_InputEventMouseButton_property_factor"></span>

[float](class_float.md#class_float) **factor** = `1.0` [🔗](class_inputeventmousebutton.md#class_InputEventMouseButton_property_factor)

- void **set_factor** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_factor** ( )

The amount (or delta) of the event. When used for high-precision scroll events, this indicates the scroll amount (vertical or horizontal). This is only supported on some platforms; the reported sensitivity varies depending on the platform. May be `0` if not supported.

---

<span id="class_InputEventMouseButton_property_pressed"></span>

[bool](class_bool.md#class_bool) **pressed** = `false` [🔗](class_inputeventmousebutton.md#class_InputEventMouseButton_property_pressed)

- void **set_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pressed** ( )

If `true`, the mouse button's state is pressed. If `false`, the mouse button's state is released.
