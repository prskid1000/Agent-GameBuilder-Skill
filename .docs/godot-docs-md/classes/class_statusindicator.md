.. meta::
	:keywords: tray

<span id="class_StatusIndicator"></span>

## StatusIndicator

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Application status indicator (aka notification area icon).

 **Note:** Status indicator is implemented on macOS and Windows.

### Properties


| [Texture2D](class_texture2d.md#class_Texture2D) | [icon](class_statusindicator.md#class_StatusIndicator_property_icon) |
| --- | --- |
| [NodePath](class_nodepath.md#class_NodePath) | [menu](class_statusindicator.md#class_StatusIndicator_property_menu) | `NodePath("")` |
| [String](class_string.md#class_String) | [tooltip](class_statusindicator.md#class_StatusIndicator_property_tooltip) | `""` |
| [bool](class_bool.md#class_bool) | [visible](class_statusindicator.md#class_StatusIndicator_property_visible) | `true` |

### Methods


| [Rect2](class_rect2.md#class_Rect2) | [get_rect](class_statusindicator.md#class_StatusIndicator_method_get_rect) ( ) const |
| --- | --- |

---

### Signals

<span id="class_StatusIndicator_signal_pressed"></span>

**pressed** ( mouse_button: [int](class_int.md#class_int), mouse_position: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_statusindicator.md#class_StatusIndicator_signal_pressed)

Emitted when the status indicator is pressed.

---

### Property Descriptions

<span id="class_StatusIndicator_property_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **icon** [🔗](class_statusindicator.md#class_StatusIndicator_property_icon)

- void **set_icon** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_icon** ( )

Status indicator icon.

---

<span id="class_StatusIndicator_property_menu"></span>

[NodePath](class_nodepath.md#class_NodePath) **menu** = `NodePath("")` [🔗](class_statusindicator.md#class_StatusIndicator_property_menu)

- void **set_menu** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_menu** ( )

Status indicator native popup menu. If this is set, the [pressed](class_statusindicator.md#class_StatusIndicator_signal_pressed) signal is not emitted.

 **Note:** Native popup is only supported if [NativeMenu](class_nativemenu.md#class_NativeMenu) supports [NativeMenu.FEATURE_POPUP_MENU](class_nativemenu.md#class_NativeMenu_constant_FEATURE_POPUP_MENU) feature.

---

<span id="class_StatusIndicator_property_tooltip"></span>

[String](class_string.md#class_String) **tooltip** = `""` [🔗](class_statusindicator.md#class_StatusIndicator_property_tooltip)

- void **set_tooltip** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_tooltip** ( )

Status indicator tooltip.

---

<span id="class_StatusIndicator_property_visible"></span>

[bool](class_bool.md#class_bool) **visible** = `true` [🔗](class_statusindicator.md#class_StatusIndicator_property_visible)

- void **set_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_visible** ( )

If `true`, the status indicator is visible.

---

### Method Descriptions

<span id="class_StatusIndicator_method_get_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **get_rect** ( ) *const* [🔗](class_statusindicator.md#class_StatusIndicator_method_get_rect)

Returns the status indicator rectangle in screen coordinates. If this status indicator is not visible, returns an empty [Rect2](class_rect2.md#class_Rect2).
