<span id="class_InputEventMouse"></span>

## InputEventMouse

**Inherits:** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow) **<** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton), [InputEventMouseMotion](class_inputeventmousemotion.md#class_InputEventMouseMotion)

Base input event type for mouse events.

### Description

Stores general information about mouse events.

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| bitfield | \[MouseButtonMask\] | [button_mask](class_inputeventmouse.md#class_InputEventMouse_property_button_mask) | `0` |
| --- | --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [global_position](class_inputeventmouse.md#class_InputEventMouse_property_global_position) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [position](class_inputeventmouse.md#class_InputEventMouse_property_position) | `Vector2(0, 0)` |

---

### Property Descriptions

<span id="class_InputEventMouse_property_button_mask"></span>

*BitField*\[MouseButtonMask\] **button_mask** = `0` [🔗](class_inputeventmouse.md#class_InputEventMouse_property_button_mask)

- void **set_button_mask** ( value: *BitField*\[MouseButtonMask\] )
- *BitField*\[MouseButtonMask\] **get_button_mask** ( )

The mouse button mask identifier, one of or a bitwise combination of the MouseButton button masks.

---

<span id="class_InputEventMouse_property_global_position"></span>

[Vector2](class_vector2.md#class_Vector2) **global_position** = `Vector2(0, 0)` [🔗](class_inputeventmouse.md#class_InputEventMouse_property_global_position)

- void **set_global_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_global_position** ( )

When received in [Node._input()](class_node.md#class_Node_private_method__input) or [Node._unhandled_input()](class_node.md#class_Node_private_method__unhandled_input), returns the mouse's position in the root [Viewport](class_viewport.md#class_Viewport) using the coordinate system of the root [Viewport](class_viewport.md#class_Viewport).

When received in [Control._gui_input()](class_control.md#class_Control_private_method__gui_input), returns the mouse's position in the [CanvasLayer](class_canvaslayer.md#class_CanvasLayer) that the [Control](class_control.md#class_Control) is in using the coordinate system of the [CanvasLayer](class_canvaslayer.md#class_CanvasLayer).

---

<span id="class_InputEventMouse_property_position"></span>

[Vector2](class_vector2.md#class_Vector2) **position** = `Vector2(0, 0)` [🔗](class_inputeventmouse.md#class_InputEventMouse_property_position)

- void **set_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_position** ( )

When received in [Node._input()](class_node.md#class_Node_private_method__input) or [Node._unhandled_input()](class_node.md#class_Node_private_method__unhandled_input), returns the mouse's position in the [Viewport](class_viewport.md#class_Viewport) this [Node](class_node.md#class_Node) is in using the coordinate system of this [Viewport](class_viewport.md#class_Viewport).

When received in [Control._gui_input()](class_control.md#class_Control_private_method__gui_input), returns the mouse's position in the [Control](class_control.md#class_Control) using the local coordinate system of the [Control](class_control.md#class_Control).
