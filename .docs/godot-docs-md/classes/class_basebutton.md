<span id="class_BaseButton"></span>

## BaseButton

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [Button](class_button.md#class_Button), [LinkButton](class_linkbutton.md#class_LinkButton), [TextureButton](class_texturebutton.md#class_TextureButton)

Abstract base class for GUI buttons.

### Description

**BaseButton** is an abstract base class for GUI buttons. It doesn't display anything by itself.

### Properties


| [ActionMode](class_basebutton.md#enum_BaseButton_ActionMode) | [action_mode](class_basebutton.md#class_BaseButton_property_action_mode) | `1` |
| --- | --- | --- |
| [ButtonGroup](class_buttongroup.md#class_ButtonGroup) | [button_group](class_basebutton.md#class_BaseButton_property_button_group) |
| bitfield | \[MouseButtonMask\] | [button_mask](class_basebutton.md#class_BaseButton_property_button_mask) | `1` |
| [bool](class_bool.md#class_bool) | [button_pressed](class_basebutton.md#class_BaseButton_property_button_pressed) | `false` |
| [bool](class_bool.md#class_bool) | [disabled](class_basebutton.md#class_BaseButton_property_disabled) | `false` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `2` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [bool](class_bool.md#class_bool) | [keep_pressed_outside](class_basebutton.md#class_BaseButton_property_keep_pressed_outside) | `false` |
| [Shortcut](class_shortcut.md#class_Shortcut) | [shortcut](class_basebutton.md#class_BaseButton_property_shortcut) |
| [bool](class_bool.md#class_bool) | [shortcut_feedback](class_basebutton.md#class_BaseButton_property_shortcut_feedback) | `true` |
| [bool](class_bool.md#class_bool) | [shortcut_in_tooltip](class_basebutton.md#class_BaseButton_property_shortcut_in_tooltip) | `true` |
| [bool](class_bool.md#class_bool) | [toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) | `false` |

### Methods


| void | [_pressed](class_basebutton.md#class_BaseButton_private_method__pressed) ( ) virtual |
| --- | --- |
| void | [_toggled](class_basebutton.md#class_BaseButton_private_method__toggled) ( toggled_on: [bool](class_bool.md#class_bool) ) virtual |
| [DrawMode](class_basebutton.md#enum_BaseButton_DrawMode) | [get_draw_mode](class_basebutton.md#class_BaseButton_method_get_draw_mode) ( ) const |
| [bool](class_bool.md#class_bool) | [is_hovered](class_basebutton.md#class_BaseButton_method_is_hovered) ( ) const |
| void | [set_pressed_no_signal](class_basebutton.md#class_BaseButton_method_set_pressed_no_signal) ( pressed: [bool](class_bool.md#class_bool) ) |

---

### Signals

<span id="class_BaseButton_signal_button_down"></span>

**button_down** ( ) [🔗](class_basebutton.md#class_BaseButton_signal_button_down)

Emitted when the button starts being held down.

---

<span id="class_BaseButton_signal_button_up"></span>

**button_up** ( ) [🔗](class_basebutton.md#class_BaseButton_signal_button_up)

Emitted when the button stops being held down.

---

<span id="class_BaseButton_signal_pressed"></span>

**pressed** ( ) [🔗](class_basebutton.md#class_BaseButton_signal_pressed)

Emitted when the button is toggled or pressed. This is on [button_down](class_basebutton.md#class_BaseButton_signal_button_down) if [action_mode](class_basebutton.md#class_BaseButton_property_action_mode) is [ACTION_MODE_BUTTON_PRESS](class_basebutton.md#class_BaseButton_constant_ACTION_MODE_BUTTON_PRESS) and on [button_up](class_basebutton.md#class_BaseButton_signal_button_up) otherwise.

If you need to know the button's pressed state (and [toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) is active), use [toggled](class_basebutton.md#class_BaseButton_signal_toggled) instead.

---

<span id="class_BaseButton_signal_toggled"></span>

**toggled** ( toggled_on: [bool](class_bool.md#class_bool) ) [🔗](class_basebutton.md#class_BaseButton_signal_toggled)

Emitted when the button was just toggled between pressed and normal states (only if [toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) is active). The new state is contained in the `toggled_on` argument.

---

### Enumerations

<span id="enum_BaseButton_DrawMode"></span>

enum **DrawMode**: [🔗](class_basebutton.md#enum_BaseButton_DrawMode)

<span id="class_BaseButton_constant_DRAW_NORMAL"></span>

[DrawMode](class_basebutton.md#enum_BaseButton_DrawMode) **DRAW_NORMAL** = `0`

The normal state (i.e. not pressed, not hovered, not toggled and enabled) of buttons.

<span id="class_BaseButton_constant_DRAW_PRESSED"></span>

[DrawMode](class_basebutton.md#enum_BaseButton_DrawMode) **DRAW_PRESSED** = `1`

The state of buttons are pressed.

<span id="class_BaseButton_constant_DRAW_HOVER"></span>

[DrawMode](class_basebutton.md#enum_BaseButton_DrawMode) **DRAW_HOVER** = `2`

The state of buttons are hovered.

<span id="class_BaseButton_constant_DRAW_DISABLED"></span>

[DrawMode](class_basebutton.md#enum_BaseButton_DrawMode) **DRAW_DISABLED** = `3`

The state of buttons are disabled.

<span id="class_BaseButton_constant_DRAW_HOVER_PRESSED"></span>

[DrawMode](class_basebutton.md#enum_BaseButton_DrawMode) **DRAW_HOVER_PRESSED** = `4`

The state of buttons are both hovered and pressed.

---

<span id="enum_BaseButton_ActionMode"></span>

enum **ActionMode**: [🔗](class_basebutton.md#enum_BaseButton_ActionMode)

<span id="class_BaseButton_constant_ACTION_MODE_BUTTON_PRESS"></span>

[ActionMode](class_basebutton.md#enum_BaseButton_ActionMode) **ACTION_MODE_BUTTON_PRESS** = `0`

Require just a press to consider the button clicked.

<span id="class_BaseButton_constant_ACTION_MODE_BUTTON_RELEASE"></span>

[ActionMode](class_basebutton.md#enum_BaseButton_ActionMode) **ACTION_MODE_BUTTON_RELEASE** = `1`

Require a press and a subsequent release before considering the button clicked.

---

### Property Descriptions

<span id="class_BaseButton_property_action_mode"></span>

[ActionMode](class_basebutton.md#enum_BaseButton_ActionMode) **action_mode** = `1` [🔗](class_basebutton.md#class_BaseButton_property_action_mode)

- void **set_action_mode** ( value: [ActionMode](class_basebutton.md#enum_BaseButton_ActionMode) )
- [ActionMode](class_basebutton.md#enum_BaseButton_ActionMode) **get_action_mode** ( )

Determines when the button is considered clicked.

---

<span id="class_BaseButton_property_button_group"></span>

[ButtonGroup](class_buttongroup.md#class_ButtonGroup) **button_group** [🔗](class_basebutton.md#class_BaseButton_property_button_group)

- void **set_button_group** ( value: [ButtonGroup](class_buttongroup.md#class_ButtonGroup) )
- [ButtonGroup](class_buttongroup.md#class_ButtonGroup) **get_button_group** ( )

The [ButtonGroup](class_buttongroup.md#class_ButtonGroup) associated with the button. Not to be confused with node groups.

 **Note:** The button will be configured as a radio button if a [ButtonGroup](class_buttongroup.md#class_ButtonGroup) is assigned to it.

---

<span id="class_BaseButton_property_button_mask"></span>

*BitField*\[MouseButtonMask\] **button_mask** = `1` [🔗](class_basebutton.md#class_BaseButton_property_button_mask)

- void **set_button_mask** ( value: *BitField*\[MouseButtonMask\] )
- *BitField*\[MouseButtonMask\] **get_button_mask** ( )

Binary mask to choose which mouse buttons this button will respond to.

To allow both left-click and right-click, use `MOUSE_BUTTON_MASK_LEFT | MOUSE_BUTTON_MASK_RIGHT`.

---

<span id="class_BaseButton_property_button_pressed"></span>

[bool](class_bool.md#class_bool) **button_pressed** = `false` [🔗](class_basebutton.md#class_BaseButton_property_button_pressed)

- void **set_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pressed** ( )

If `true`, the button's state is pressed. Means the button is pressed down or toggled (if [toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) is active). Only works if [toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) is `true`.

 **Note:** Changing the value of [button_pressed](class_basebutton.md#class_BaseButton_property_button_pressed) will result in [toggled](class_basebutton.md#class_BaseButton_signal_toggled) to be emitted. If you want to change the pressed state without emitting that signal, use [set_pressed_no_signal()](class_basebutton.md#class_BaseButton_method_set_pressed_no_signal).

---

<span id="class_BaseButton_property_disabled"></span>

[bool](class_bool.md#class_bool) **disabled** = `false` [🔗](class_basebutton.md#class_BaseButton_property_disabled)

- void **set_disabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_disabled** ( )

If `true`, the button is in disabled state and can't be clicked or toggled.

 **Note:** If the button is disabled while held down, [button_up](class_basebutton.md#class_BaseButton_signal_button_up) will be emitted.

---

<span id="class_BaseButton_property_keep_pressed_outside"></span>

[bool](class_bool.md#class_bool) **keep_pressed_outside** = `false` [🔗](class_basebutton.md#class_BaseButton_property_keep_pressed_outside)

- void **set_keep_pressed_outside** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_keep_pressed_outside** ( )

If `true`, the button stays pressed when moving the cursor outside the button while pressing it.

 **Note:** This property only affects the button's visual appearance. Signals will be emitted at the same moment regardless of this property's value.

---

<span id="class_BaseButton_property_shortcut"></span>

[Shortcut](class_shortcut.md#class_Shortcut) **shortcut** [🔗](class_basebutton.md#class_BaseButton_property_shortcut)

- void **set_shortcut** ( value: [Shortcut](class_shortcut.md#class_Shortcut) )
- [Shortcut](class_shortcut.md#class_Shortcut) **get_shortcut** ( )

[Shortcut](class_shortcut.md#class_Shortcut) associated to the button.

---

<span id="class_BaseButton_property_shortcut_feedback"></span>

[bool](class_bool.md#class_bool) **shortcut_feedback** = `true` [🔗](class_basebutton.md#class_BaseButton_property_shortcut_feedback)

- void **set_shortcut_feedback** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_shortcut_feedback** ( )

If `true`, the button will highlight for a short amount of time when its shortcut is activated. If `false` and [toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) is `false`, the shortcut will activate without any visual feedback.

---

<span id="class_BaseButton_property_shortcut_in_tooltip"></span>

[bool](class_bool.md#class_bool) **shortcut_in_tooltip** = `true` [🔗](class_basebutton.md#class_BaseButton_property_shortcut_in_tooltip)

- void **set_shortcut_in_tooltip** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_shortcut_in_tooltip_enabled** ( )

If `true`, the button will add information about its shortcut in the tooltip.

 **Note:** This property does nothing when the tooltip control is customized using [Control._make_custom_tooltip()](class_control.md#class_Control_private_method__make_custom_tooltip).

---

<span id="class_BaseButton_property_toggle_mode"></span>

[bool](class_bool.md#class_bool) **toggle_mode** = `false` [🔗](class_basebutton.md#class_BaseButton_property_toggle_mode)

- void **set_toggle_mode** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_toggle_mode** ( )

If `true`, the button is in toggle mode. Makes the button flip state between pressed and unpressed each time its area is clicked.

---

### Method Descriptions

<span id="class_BaseButton_private_method__pressed"></span>

void **_pressed** ( ) *virtual* [🔗](class_basebutton.md#class_BaseButton_private_method__pressed)

Called when the button is pressed. If you need to know the button's pressed state (and [toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) is active), use [_toggled()](class_basebutton.md#class_BaseButton_private_method__toggled) instead.

---

<span id="class_BaseButton_private_method__toggled"></span>

void **_toggled** ( toggled_on: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_basebutton.md#class_BaseButton_private_method__toggled)

Called when the button is toggled (only if [toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) is active).

---

<span id="class_BaseButton_method_get_draw_mode"></span>

[DrawMode](class_basebutton.md#enum_BaseButton_DrawMode) **get_draw_mode** ( ) *const* [🔗](class_basebutton.md#class_BaseButton_method_get_draw_mode)

Returns the visual state used to draw the button. This is useful mainly when implementing your own draw code by either overriding _draw() or connecting to "draw" signal. The visual state of the button is defined by the [DrawMode](class_basebutton.md#enum_BaseButton_DrawMode) enum.

---

<span id="class_BaseButton_method_is_hovered"></span>

[bool](class_bool.md#class_bool) **is_hovered** ( ) *const* [🔗](class_basebutton.md#class_BaseButton_method_is_hovered)

Returns `true` if the mouse has entered the button and has not left it yet.

---

<span id="class_BaseButton_method_set_pressed_no_signal"></span>

void **set_pressed_no_signal** ( pressed: [bool](class_bool.md#class_bool) ) [🔗](class_basebutton.md#class_BaseButton_method_set_pressed_no_signal)

Changes the [button_pressed](class_basebutton.md#class_BaseButton_property_button_pressed) state of the button, without emitting [toggled](class_basebutton.md#class_BaseButton_signal_toggled). Use when you just want to change the state of the button without sending the pressed event (e.g. when initializing scene). Only works if [toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) is `true`.

 **Note:** This method doesn't unpress other buttons in [button_group](class_basebutton.md#class_BaseButton_property_button_group).
