<span id="class_VirtualJoystick"></span>

## VirtualJoystick

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A virtual joystick control for touchscreen devices.

### Description

A customizable on-screen joystick control designed for touchscreen devices. It allows users to provide directional input by dragging a virtual tip within a defined circular area.

This control can simulate directional actions (see [action_up](class_virtualjoystick.md#class_VirtualJoystick_property_action_up), [action_down](class_virtualjoystick.md#class_VirtualJoystick_property_action_down), [action_left](class_virtualjoystick.md#class_VirtualJoystick_property_action_left), and [action_right](class_virtualjoystick.md#class_VirtualJoystick_property_action_right)), which are triggered when the joystick is moved in the corresponding directions.

### Properties


| [StringName](class_stringname.md#class_StringName) | [action_down](class_virtualjoystick.md#class_VirtualJoystick_property_action_down) | `&"ui_down"` |
| --- | --- | --- |
| [StringName](class_stringname.md#class_StringName) | [action_left](class_virtualjoystick.md#class_VirtualJoystick_property_action_left) | `&"ui_left"` |
| [StringName](class_stringname.md#class_StringName) | [action_right](class_virtualjoystick.md#class_VirtualJoystick_property_action_right) | `&"ui_right"` |
| [StringName](class_stringname.md#class_StringName) | [action_up](class_virtualjoystick.md#class_VirtualJoystick_property_action_up) | `&"ui_up"` |
| [float](class_float.md#class_float) | [clampzone_ratio](class_virtualjoystick.md#class_VirtualJoystick_property_clampzone_ratio) | `1.0` |
| [float](class_float.md#class_float) | [deadzone_ratio](class_virtualjoystick.md#class_VirtualJoystick_property_deadzone_ratio) | `0.0` |
| [Vector2](class_vector2.md#class_Vector2) | [initial_offset_ratio](class_virtualjoystick.md#class_VirtualJoystick_property_initial_offset_ratio) | `Vector2(0.5, 0.5)` |
| [JoystickMode](class_virtualjoystick.md#enum_VirtualJoystick_JoystickMode) | [joystick_mode](class_virtualjoystick.md#class_VirtualJoystick_property_joystick_mode) | `0` |
| [float](class_float.md#class_float) | [joystick_size](class_virtualjoystick.md#class_VirtualJoystick_property_joystick_size) | `100.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [joystick_texture](class_virtualjoystick.md#class_VirtualJoystick_property_joystick_texture) |
| [float](class_float.md#class_float) | [tip_size](class_virtualjoystick.md#class_VirtualJoystick_property_tip_size) | `50.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [tip_texture](class_virtualjoystick.md#class_VirtualJoystick_property_tip_texture) |
| [VisibilityMode](class_virtualjoystick.md#enum_VirtualJoystick_VisibilityMode) | [visibility_mode](class_virtualjoystick.md#class_VirtualJoystick_property_visibility_mode) | `0` |

### Theme Properties


| [Color](class_color.md#class_Color) | [ring_normal_color](class_virtualjoystick.md#class_VirtualJoystick_theme_color_ring_normal_color) | `Color(0, 0, 0, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [ring_pressed_color](class_virtualjoystick.md#class_VirtualJoystick_theme_color_ring_pressed_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [tip_normal_color](class_virtualjoystick.md#class_VirtualJoystick_theme_color_tip_normal_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [tip_pressed_color](class_virtualjoystick.md#class_VirtualJoystick_theme_color_tip_pressed_color) | `Color(0, 0, 0, 1)` |

---

### Signals

<span id="class_VirtualJoystick_signal_flick_canceled"></span>

**flick_canceled** ( ) [🔗](class_virtualjoystick.md#class_VirtualJoystick_signal_flick_canceled)

Emitted when the tip enters the deadzone after being outside of it.

---

<span id="class_VirtualJoystick_signal_flicked"></span>

**flicked** ( input_vector: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_virtualjoystick.md#class_VirtualJoystick_signal_flicked)

Emitted when the tip moved outside the deadzone and the joystick is released. The `input_vector` contains the last input direction and strength before release. Its length is between `0.0` and `1.0`.

---

<span id="class_VirtualJoystick_signal_pressed"></span>

**pressed** ( ) [🔗](class_virtualjoystick.md#class_VirtualJoystick_signal_pressed)

Emitted when the joystick is pressed.

---

<span id="class_VirtualJoystick_signal_released"></span>

**released** ( input_vector: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_virtualjoystick.md#class_VirtualJoystick_signal_released)

Emitted when the joystick is released. The `input_vector` is the final input direction and strength, with a length between `0.0` and `1.0`.

---

<span id="class_VirtualJoystick_signal_tapped"></span>

**tapped** ( ) [🔗](class_virtualjoystick.md#class_VirtualJoystick_signal_tapped)

Emitted when the joystick is released without moving the tip.

---

### Enumerations

<span id="enum_VirtualJoystick_JoystickMode"></span>

enum **JoystickMode**: [🔗](class_virtualjoystick.md#enum_VirtualJoystick_JoystickMode)

<span id="class_VirtualJoystick_constant_JOYSTICK_FIXED"></span>

[JoystickMode](class_virtualjoystick.md#enum_VirtualJoystick_JoystickMode) **JOYSTICK_FIXED** = `0`

The joystick doesn't move.

<span id="class_VirtualJoystick_constant_JOYSTICK_DYNAMIC"></span>

[JoystickMode](class_virtualjoystick.md#enum_VirtualJoystick_JoystickMode) **JOYSTICK_DYNAMIC** = `1`

The joystick is moved to the initial touch position as long as it's within the joystick's bounds. It moves back to its original position when released.

<span id="class_VirtualJoystick_constant_JOYSTICK_FOLLOWING"></span>

[JoystickMode](class_virtualjoystick.md#enum_VirtualJoystick_JoystickMode) **JOYSTICK_FOLLOWING** = `2`

The joystick is moved to the initial touch position as long as it's within the joystick's bounds. It will follow the touch input if it goes outside the joystick's range. It moves back to its original position when released.

---

<span id="enum_VirtualJoystick_VisibilityMode"></span>

enum **VisibilityMode**: [🔗](class_virtualjoystick.md#enum_VirtualJoystick_VisibilityMode)

<span id="class_VirtualJoystick_constant_VISIBILITY_ALWAYS"></span>

[VisibilityMode](class_virtualjoystick.md#enum_VirtualJoystick_VisibilityMode) **VISIBILITY_ALWAYS** = `0`

The joystick is always visible.

<span id="class_VirtualJoystick_constant_VISIBILITY_WHEN_TOUCHED"></span>

[VisibilityMode](class_virtualjoystick.md#enum_VirtualJoystick_VisibilityMode) **VISIBILITY_WHEN_TOUCHED** = `1`

The joystick is only visible when being touched.

---

### Property Descriptions

<span id="class_VirtualJoystick_property_action_down"></span>

[StringName](class_stringname.md#class_StringName) **action_down** = `&"ui_down"` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_action_down)

- void **set_action_down** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_action_down** ( )

The action to trigger when the joystick is moved down.

---

<span id="class_VirtualJoystick_property_action_left"></span>

[StringName](class_stringname.md#class_StringName) **action_left** = `&"ui_left"` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_action_left)

- void **set_action_left** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_action_left** ( )

The action to trigger when the joystick is moved left.

---

<span id="class_VirtualJoystick_property_action_right"></span>

[StringName](class_stringname.md#class_StringName) **action_right** = `&"ui_right"` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_action_right)

- void **set_action_right** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_action_right** ( )

The action to trigger when the joystick is moved right.

---

<span id="class_VirtualJoystick_property_action_up"></span>

[StringName](class_stringname.md#class_StringName) **action_up** = `&"ui_up"` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_action_up)

- void **set_action_up** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_action_up** ( )

The action to trigger when the joystick is moved up.

---

<span id="class_VirtualJoystick_property_clampzone_ratio"></span>

[float](class_float.md#class_float) **clampzone_ratio** = `1.0` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_clampzone_ratio)

- void **set_clampzone_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_clampzone_ratio** ( )

The multiplier applied to the joystick's radius that defines the clamp zone.

This zone limits how far the joystick tip can move from its center before being clamped.

A value of `1.0` means the tip can move up to the edge of the joystick's visual size.

In [JOYSTICK_FOLLOWING](class_virtualjoystick.md#class_VirtualJoystick_constant_JOYSTICK_FOLLOWING) mode, this radius also determines how far the finger can move before the joystick base starts following the touch input.

---

<span id="class_VirtualJoystick_property_deadzone_ratio"></span>

[float](class_float.md#class_float) **deadzone_ratio** = `0.0` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_deadzone_ratio)

- void **set_deadzone_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_deadzone_ratio** ( )

The ratio of the joystick size that defines the joystick deadzone. The joystick tip must move beyond this ratio before being considered active.

This deadzone is applied before triggering input actions and affects the joystick's input vector and all related signals.

Note that input actions may also define their own deadzones in the InputMap. If both are set, the joystick deadzone is applied first, followed by the action's deadzone.

By default, this value is `0.0`, meaning the joystick does not apply its own deadzone and relies entirely on the InputMap action deadzones.

---

<span id="class_VirtualJoystick_property_initial_offset_ratio"></span>

[Vector2](class_vector2.md#class_Vector2) **initial_offset_ratio** = `Vector2(0.5, 0.5)` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_initial_offset_ratio)

- void **set_initial_offset_ratio** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_initial_offset_ratio** ( )

The initial position of the joystick as a ratio of the control's size. `(0, 0)` is top-left and `(1, 1)` is bottom-right.

---

<span id="class_VirtualJoystick_property_joystick_mode"></span>

[JoystickMode](class_virtualjoystick.md#enum_VirtualJoystick_JoystickMode) **joystick_mode** = `0` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_joystick_mode)

- void **set_joystick_mode** ( value: [JoystickMode](class_virtualjoystick.md#enum_VirtualJoystick_JoystickMode) )
- [JoystickMode](class_virtualjoystick.md#enum_VirtualJoystick_JoystickMode) **get_joystick_mode** ( )

The joystick mode to use.

---

<span id="class_VirtualJoystick_property_joystick_size"></span>

[float](class_float.md#class_float) **joystick_size** = `100.0` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_joystick_size)

- void **set_joystick_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_joystick_size** ( )

The size of the joystick in pixels.

---

<span id="class_VirtualJoystick_property_joystick_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **joystick_texture** [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_joystick_texture)

- void **set_joystick_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_joystick_texture** ( )

The texture to use for the joystick base. When `null`, a ring is drawn using the [ring_normal_color](class_virtualjoystick.md#class_VirtualJoystick_theme_color_ring_normal_color) and [ring_pressed_color](class_virtualjoystick.md#class_VirtualJoystick_theme_color_ring_pressed_color).

---

<span id="class_VirtualJoystick_property_tip_size"></span>

[float](class_float.md#class_float) **tip_size** = `50.0` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_tip_size)

- void **set_tip_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_tip_size** ( )

The size of the joystick tip in pixels.

---

<span id="class_VirtualJoystick_property_tip_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **tip_texture** [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_tip_texture)

- void **set_tip_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_tip_texture** ( )

The texture to use for the joystick tip. When `null`, a circle is drawn using the [tip_normal_color](class_virtualjoystick.md#class_VirtualJoystick_theme_color_tip_normal_color) and [tip_pressed_color](class_virtualjoystick.md#class_VirtualJoystick_theme_color_tip_pressed_color).

---

<span id="class_VirtualJoystick_property_visibility_mode"></span>

[VisibilityMode](class_virtualjoystick.md#enum_VirtualJoystick_VisibilityMode) **visibility_mode** = `0` [🔗](class_virtualjoystick.md#class_VirtualJoystick_property_visibility_mode)

- void **set_visibility_mode** ( value: [VisibilityMode](class_virtualjoystick.md#enum_VirtualJoystick_VisibilityMode) )
- [VisibilityMode](class_virtualjoystick.md#enum_VirtualJoystick_VisibilityMode) **get_visibility_mode** ( )

The visibility mode to use.

---

### Theme Property Descriptions

<span id="class_VirtualJoystick_theme_color_ring_normal_color"></span>

[Color](class_color.md#class_Color) **ring_normal_color** = `Color(0, 0, 0, 1)` [🔗](class_virtualjoystick.md#class_VirtualJoystick_theme_color_ring_normal_color)

Default ring joystick [Color](class_color.md#class_Color).

---

<span id="class_VirtualJoystick_theme_color_ring_pressed_color"></span>

[Color](class_color.md#class_Color) **ring_pressed_color** = `Color(0, 0, 0, 1)` [🔗](class_virtualjoystick.md#class_VirtualJoystick_theme_color_ring_pressed_color)

Ring joystick [Color](class_color.md#class_Color) when pressed.

---

<span id="class_VirtualJoystick_theme_color_tip_normal_color"></span>

[Color](class_color.md#class_Color) **tip_normal_color** = `Color(0, 0, 0, 1)` [🔗](class_virtualjoystick.md#class_VirtualJoystick_theme_color_tip_normal_color)

Default Tip joystick [Color](class_color.md#class_Color).

---

<span id="class_VirtualJoystick_theme_color_tip_pressed_color"></span>

[Color](class_color.md#class_Color) **tip_pressed_color** = `Color(0, 0, 0, 1)` [🔗](class_virtualjoystick.md#class_VirtualJoystick_theme_color_tip_pressed_color)

Tip joystick [Color](class_color.md#class_Color) when pressed.
