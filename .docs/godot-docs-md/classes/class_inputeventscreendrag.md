<span id="class_InputEventScreenDrag"></span>

## InputEventScreenDrag

**Inherits:** [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow) **<** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a screen drag event.

### Description

Stores information about screen drag events. See [Node._input()](class_node.md#class_Node_private_method__input).

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| [int](class_int.md#class_int) | [index](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_index) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [pen_inverted](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_pen_inverted) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [position](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_position) | `Vector2(0, 0)` |
| [float](class_float.md#class_float) | [pressure](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_pressure) | `0.0` |
| [Vector2](class_vector2.md#class_Vector2) | [relative](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_relative) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [screen_relative](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_screen_relative) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [screen_velocity](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_screen_velocity) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [tilt](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_tilt) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [velocity](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_velocity) | `Vector2(0, 0)` |

---

### Property Descriptions

<span id="class_InputEventScreenDrag_property_index"></span>

[int](class_int.md#class_int) **index** = `0` [🔗](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_index)

- void **set_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_index** ( )

The drag event index in the case of a multi-drag event.

---

<span id="class_InputEventScreenDrag_property_pen_inverted"></span>

[bool](class_bool.md#class_bool) **pen_inverted** = `false` [🔗](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_pen_inverted)

- void **set_pen_inverted** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_pen_inverted** ( )

Returns `true` when using the eraser end of a stylus pen.

---

<span id="class_InputEventScreenDrag_property_position"></span>

[Vector2](class_vector2.md#class_Vector2) **position** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_position)

- void **set_position** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_position** ( )

The drag position in the viewport the node is in, using the coordinate system of this viewport.

---

<span id="class_InputEventScreenDrag_property_pressure"></span>

[float](class_float.md#class_float) **pressure** = `0.0` [🔗](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_pressure)

- void **set_pressure** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pressure** ( )

Represents the pressure the user puts on the pen. Ranges from `0.0` to `1.0`.

---

<span id="class_InputEventScreenDrag_property_relative"></span>

[Vector2](class_vector2.md#class_Vector2) **relative** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_relative)

- void **set_relative** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_relative** ( )

The drag position relative to the previous position (position at the last frame).

 **Note:** [relative](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_relative) is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means touch sensitivity will appear different depending on resolution when using [relative](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_relative) in a script that handles touch aiming. To avoid this, use [screen_relative](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_screen_relative) instead.

---

<span id="class_InputEventScreenDrag_property_screen_relative"></span>

[Vector2](class_vector2.md#class_Vector2) **screen_relative** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_screen_relative)

- void **set_screen_relative** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_screen_relative** ( )

The unscaled drag position relative to the previous position in screen coordinates (position at the last frame). This position is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()](class_inputevent.md#class_InputEvent_method_xformed_by). This should be preferred over [relative](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_relative) for touch aiming regardless of the project's stretch mode.

---

<span id="class_InputEventScreenDrag_property_screen_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **screen_velocity** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_screen_velocity)

- void **set_screen_velocity** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_screen_velocity** ( )

The unscaled drag velocity in pixels per second in screen coordinates. This velocity is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()](class_inputevent.md#class_InputEvent_method_xformed_by). This should be preferred over [velocity](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_velocity) for touch aiming regardless of the project's stretch mode.

---

<span id="class_InputEventScreenDrag_property_tilt"></span>

[Vector2](class_vector2.md#class_Vector2) **tilt** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_tilt)

- void **set_tilt** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_tilt** ( )

Represents the angles of tilt of the pen. Positive X-coordinate value indicates a tilt to the right. Positive Y-coordinate value indicates a tilt toward the user. Ranges from `-1.0` to `1.0` for both axes.

---

<span id="class_InputEventScreenDrag_property_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **velocity** = `Vector2(0, 0)` [🔗](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_velocity)

- void **set_velocity** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_velocity** ( )

The drag velocity.

 **Note:** [velocity](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_velocity) is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means touch sensitivity will appear different depending on resolution when using [velocity](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_velocity) in a script that handles touch aiming. To avoid this, use [screen_velocity](class_inputeventscreendrag.md#class_InputEventScreenDrag_property_screen_velocity) instead.
