<span id="class_TouchScreenButton"></span>

## TouchScreenButton

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Button for touch screen devices for gameplay use.

### Description

TouchScreenButton allows you to create on-screen buttons for touch devices. It's intended for gameplay use, such as a unit you have to touch to move. Unlike [Button](class_button.md#class_Button), TouchScreenButton supports multitouch out of the box. Several TouchScreenButtons can be pressed at the same time with touch input.

This node inherits from [Node2D](class_node2d.md#class_Node2D). Unlike with [Control](class_control.md#class_Control) nodes, you cannot set anchors on it. If you want to create menus or user interfaces, you may want to use [Button](class_button.md#class_Button) nodes instead. To make button nodes react to touch events, you can enable ProjectSettings.input_devices/pointing/emulate_mouse_from_touch in the Project Settings.

You can configure TouchScreenButton to be visible only on touch devices, helping you develop your game both for desktop and mobile devices.

### Properties


| [String](class_string.md#class_String) | [action](class_touchscreenbutton.md#class_TouchScreenButton_property_action) | `""` |
| --- | --- | --- |
| [BitMap](class_bitmap.md#class_BitMap) | [bitmask](class_touchscreenbutton.md#class_TouchScreenButton_property_bitmask) |
| [bool](class_bool.md#class_bool) | [passby_press](class_touchscreenbutton.md#class_TouchScreenButton_property_passby_press) | `false` |
| [Shape2D](class_shape2d.md#class_Shape2D) | [shape](class_touchscreenbutton.md#class_TouchScreenButton_property_shape) |
| [bool](class_bool.md#class_bool) | [shape_centered](class_touchscreenbutton.md#class_TouchScreenButton_property_shape_centered) | `true` |
| [bool](class_bool.md#class_bool) | [shape_visible](class_touchscreenbutton.md#class_TouchScreenButton_property_shape_visible) | `true` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_normal](class_touchscreenbutton.md#class_TouchScreenButton_property_texture_normal) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture_pressed](class_touchscreenbutton.md#class_TouchScreenButton_property_texture_pressed) |
| [VisibilityMode](class_touchscreenbutton.md#enum_TouchScreenButton_VisibilityMode) | [visibility_mode](class_touchscreenbutton.md#class_TouchScreenButton_property_visibility_mode) | `0` |

### Methods


| [bool](class_bool.md#class_bool) | [is_pressed](class_touchscreenbutton.md#class_TouchScreenButton_method_is_pressed) ( ) const |
| --- | --- |

---

### Signals

<span id="class_TouchScreenButton_signal_pressed"></span>

**pressed** ( ) [🔗](class_touchscreenbutton.md#class_TouchScreenButton_signal_pressed)

Emitted when the button is pressed (down).

---

<span id="class_TouchScreenButton_signal_released"></span>

**released** ( ) [🔗](class_touchscreenbutton.md#class_TouchScreenButton_signal_released)

Emitted when the button is released (up).

---

### Enumerations

<span id="enum_TouchScreenButton_VisibilityMode"></span>

enum **VisibilityMode**: [🔗](class_touchscreenbutton.md#enum_TouchScreenButton_VisibilityMode)

<span id="class_TouchScreenButton_constant_VISIBILITY_ALWAYS"></span>

[VisibilityMode](class_touchscreenbutton.md#enum_TouchScreenButton_VisibilityMode) **VISIBILITY_ALWAYS** = `0`

Always visible.

<span id="class_TouchScreenButton_constant_VISIBILITY_TOUCHSCREEN_ONLY"></span>

[VisibilityMode](class_touchscreenbutton.md#enum_TouchScreenButton_VisibilityMode) **VISIBILITY_TOUCHSCREEN_ONLY** = `1`

Visible on touch screens only.

---

### Property Descriptions

<span id="class_TouchScreenButton_property_action"></span>

[String](class_string.md#class_String) **action** = `""` [🔗](class_touchscreenbutton.md#class_TouchScreenButton_property_action)

- void **set_action** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_action** ( )

The button's action. Actions can be handled with [InputEventAction](class_inputeventaction.md#class_InputEventAction).

---

<span id="class_TouchScreenButton_property_bitmask"></span>

[BitMap](class_bitmap.md#class_BitMap) **bitmask** [🔗](class_touchscreenbutton.md#class_TouchScreenButton_property_bitmask)

- void **set_bitmask** ( value: [BitMap](class_bitmap.md#class_BitMap) )
- [BitMap](class_bitmap.md#class_BitMap) **get_bitmask** ( )

The button's bitmask.

---

<span id="class_TouchScreenButton_property_passby_press"></span>

[bool](class_bool.md#class_bool) **passby_press** = `false` [🔗](class_touchscreenbutton.md#class_TouchScreenButton_property_passby_press)

- void **set_passby_press** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_passby_press_enabled** ( )

If `true`, the [pressed](class_touchscreenbutton.md#class_TouchScreenButton_signal_pressed) and [released](class_touchscreenbutton.md#class_TouchScreenButton_signal_released) signals are emitted whenever a pressed finger goes in and out of the button, even if the pressure started outside the active area of the button.

 **Note:** This is a "pass-by" (not "bypass") press mode.

---

<span id="class_TouchScreenButton_property_shape"></span>

[Shape2D](class_shape2d.md#class_Shape2D) **shape** [🔗](class_touchscreenbutton.md#class_TouchScreenButton_property_shape)

- void **set_shape** ( value: [Shape2D](class_shape2d.md#class_Shape2D) )
- [Shape2D](class_shape2d.md#class_Shape2D) **get_shape** ( )

The button's shape.

---

<span id="class_TouchScreenButton_property_shape_centered"></span>

[bool](class_bool.md#class_bool) **shape_centered** = `true` [🔗](class_touchscreenbutton.md#class_TouchScreenButton_property_shape_centered)

- void **set_shape_centered** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_shape_centered** ( )

If `true`, the button's shape is centered in the provided texture. If no texture is used, this property has no effect.

---

<span id="class_TouchScreenButton_property_shape_visible"></span>

[bool](class_bool.md#class_bool) **shape_visible** = `true` [🔗](class_touchscreenbutton.md#class_TouchScreenButton_property_shape_visible)

- void **set_shape_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_shape_visible** ( )

If `true`, the button's shape is visible in the editor.

---

<span id="class_TouchScreenButton_property_texture_normal"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_normal** [🔗](class_touchscreenbutton.md#class_TouchScreenButton_property_texture_normal)

- void **set_texture_normal** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture_normal** ( )

The button's texture for the normal state.

---

<span id="class_TouchScreenButton_property_texture_pressed"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture_pressed** [🔗](class_touchscreenbutton.md#class_TouchScreenButton_property_texture_pressed)

- void **set_texture_pressed** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture_pressed** ( )

The button's texture for the pressed state.

---

<span id="class_TouchScreenButton_property_visibility_mode"></span>

[VisibilityMode](class_touchscreenbutton.md#enum_TouchScreenButton_VisibilityMode) **visibility_mode** = `0` [🔗](class_touchscreenbutton.md#class_TouchScreenButton_property_visibility_mode)

- void **set_visibility_mode** ( value: [VisibilityMode](class_touchscreenbutton.md#enum_TouchScreenButton_VisibilityMode) )
- [VisibilityMode](class_touchscreenbutton.md#enum_TouchScreenButton_VisibilityMode) **get_visibility_mode** ( )

The button's visibility mode.

---

### Method Descriptions

<span id="class_TouchScreenButton_method_is_pressed"></span>

[bool](class_bool.md#class_bool) **is_pressed** ( ) *const* [🔗](class_touchscreenbutton.md#class_TouchScreenButton_method_is_pressed)

Returns `true` if this button is currently pressed.
