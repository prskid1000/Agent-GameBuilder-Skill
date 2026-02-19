.. meta::
	:keywords: radio

<span id="class_ButtonGroup"></span>

## ButtonGroup

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A group of buttons that doesn't allow more than one button to be pressed at a time.

### Description

A group of [BaseButton](class_basebutton.md#class_BaseButton)-derived buttons. The buttons in a **ButtonGroup** are treated like radio buttons: No more than one button can be pressed at a time. Some types of buttons (such as [CheckBox](class_checkbox.md#class_CheckBox)) may have a special appearance in this state.

Every member of a **ButtonGroup** should have [BaseButton.toggle_mode](class_basebutton.md#class_BaseButton_property_toggle_mode) set to `true`.

### Properties


| [bool](class_bool.md#class_bool) | [allow_unpress](class_buttongroup.md#class_ButtonGroup_property_allow_unpress) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `true` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |

### Methods


| [Array](class_array.md#class_Array)\[[BaseButton](class_basebutton.md#class_BaseButton)\] | [get_buttons](class_buttongroup.md#class_ButtonGroup_method_get_buttons) ( ) |
| --- | --- |
| [BaseButton](class_basebutton.md#class_BaseButton) | [get_pressed_button](class_buttongroup.md#class_ButtonGroup_method_get_pressed_button) ( ) |

---

### Signals

<span id="class_ButtonGroup_signal_pressed"></span>

**pressed** ( button: [BaseButton](class_basebutton.md#class_BaseButton) ) [🔗](class_buttongroup.md#class_ButtonGroup_signal_pressed)

Emitted when one of the buttons of the group is pressed.

---

### Property Descriptions

<span id="class_ButtonGroup_property_allow_unpress"></span>

[bool](class_bool.md#class_bool) **allow_unpress** = `false` [🔗](class_buttongroup.md#class_ButtonGroup_property_allow_unpress)

- void **set_allow_unpress** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_allow_unpress** ( )

If `true`, it is possible to unpress all buttons in this **ButtonGroup**.

---

### Method Descriptions

<span id="class_ButtonGroup_method_get_buttons"></span>

[Array](class_array.md#class_Array)\[[BaseButton](class_basebutton.md#class_BaseButton)\] **get_buttons** ( ) [🔗](class_buttongroup.md#class_ButtonGroup_method_get_buttons)

Returns an [Array](class_array.md#class_Array) of [Button](class_button.md#class_Button) s who have this as their **ButtonGroup** (see [BaseButton.button_group](class_basebutton.md#class_BaseButton_property_button_group)).

---

<span id="class_ButtonGroup_method_get_pressed_button"></span>

[BaseButton](class_basebutton.md#class_BaseButton) **get_pressed_button** ( ) [🔗](class_buttongroup.md#class_ButtonGroup_method_get_pressed_button)

Returns the current pressed button.
