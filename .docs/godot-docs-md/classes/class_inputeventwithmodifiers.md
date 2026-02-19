<span id="class_InputEventWithModifiers"></span>

## InputEventWithModifiers

**Inherits:** [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow) **<** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [InputEventGesture](class_inputeventgesture.md#class_InputEventGesture), [InputEventKey](class_inputeventkey.md#class_InputEventKey), [InputEventMouse](class_inputeventmouse.md#class_InputEventMouse)

Abstract base class for input events affected by modifier keys like :kbd:`Shift` and :kbd:`Alt`.

### Description

Stores information about mouse, keyboard, and touch gesture input events. This includes information about which modifier keys are pressed, such as :kbd:`Shift` or :kbd:`Alt`. See [Node._input()](class_node.md#class_Node_private_method__input).

 **Note:** Modifier keys are considered modifiers only when used in combination with another key. As a result, their corresponding member variables, such as [ctrl_pressed](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_ctrl_pressed), will return `false` if the key is pressed on its own.

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| [bool](class_bool.md#class_bool) | [alt_pressed](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_alt_pressed) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [command_or_control_autoremap](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_command_or_control_autoremap) | `false` |
| [bool](class_bool.md#class_bool) | [ctrl_pressed](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_ctrl_pressed) | `false` |
| [bool](class_bool.md#class_bool) | [meta_pressed](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_meta_pressed) | `false` |
| [bool](class_bool.md#class_bool) | [shift_pressed](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_shift_pressed) | `false` |

### Methods


| bitfield | \[KeyModifierMask\] | [get_modifiers_mask](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_method_get_modifiers_mask) ( ) | const |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [is_command_or_control_pressed](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_method_is_command_or_control_pressed) ( ) const |

---

### Property Descriptions

<span id="class_InputEventWithModifiers_property_alt_pressed"></span>

[bool](class_bool.md#class_bool) **alt_pressed** = `false` [🔗](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_alt_pressed)

- void **set_alt_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_alt_pressed** ( )

State of the :kbd:`Alt` modifier.

---

<span id="class_InputEventWithModifiers_property_command_or_control_autoremap"></span>

[bool](class_bool.md#class_bool) **command_or_control_autoremap** = `false` [🔗](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_command_or_control_autoremap)

- void **set_command_or_control_autoremap** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_command_or_control_autoremap** ( )

Automatically use :kbd:`Meta` (:kbd:`Cmd`) on macOS and :kbd:`Ctrl` on other platforms. If `true`, [ctrl_pressed](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_ctrl_pressed) and [meta_pressed](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_meta_pressed) cannot be set.

---

<span id="class_InputEventWithModifiers_property_ctrl_pressed"></span>

[bool](class_bool.md#class_bool) **ctrl_pressed** = `false` [🔗](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_ctrl_pressed)

- void **set_ctrl_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_ctrl_pressed** ( )

State of the :kbd:`Ctrl` modifier.

---

<span id="class_InputEventWithModifiers_property_meta_pressed"></span>

[bool](class_bool.md#class_bool) **meta_pressed** = `false` [🔗](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_meta_pressed)

- void **set_meta_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_meta_pressed** ( )

State of the :kbd:`Meta` modifier. On Windows and Linux, this represents the Windows key (sometimes called "meta" or "super" on Linux). On macOS, this represents the Command key.

---

<span id="class_InputEventWithModifiers_property_shift_pressed"></span>

[bool](class_bool.md#class_bool) **shift_pressed** = `false` [🔗](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_property_shift_pressed)

- void **set_shift_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_shift_pressed** ( )

State of the :kbd:`Shift` modifier.

---

### Method Descriptions

<span id="class_InputEventWithModifiers_method_get_modifiers_mask"></span>

*BitField*\[KeyModifierMask\] **get_modifiers_mask** ( ) *const* [🔗](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_method_get_modifiers_mask)

Returns the keycode combination of modifier keys.

---

<span id="class_InputEventWithModifiers_method_is_command_or_control_pressed"></span>

[bool](class_bool.md#class_bool) **is_command_or_control_pressed** ( ) *const* [🔗](class_inputeventwithmodifiers.md#class_InputEventWithModifiers_method_is_command_or_control_pressed)

On macOS, returns `true` if :kbd:`Meta` (:kbd:`Cmd`) is pressed.

On other platforms, returns `true` if :kbd:`Ctrl` is pressed.
