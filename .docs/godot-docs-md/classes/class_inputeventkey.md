<span id="class_InputEventKey"></span>

## InputEventKey

**Inherits:** [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers) **<** [InputEventFromWindow](class_inputeventfromwindow.md#class_InputEventFromWindow) **<** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a key on a keyboard being pressed or released.

### Description

An input event for keys on a keyboard. Supports key presses, key releases and [echo](class_inputeventkey.md#class_InputEventKey_property_echo) events. It can also be received in [Node._unhandled_key_input()](class_node.md#class_Node_private_method__unhandled_key_input).

 **Note:** Events received from the keyboard usually have all properties set. Event mappings should have only one of the [keycode](class_inputeventkey.md#class_InputEventKey_property_keycode), [physical_keycode](class_inputeventkey.md#class_InputEventKey_property_physical_keycode) or [unicode](class_inputeventkey.md#class_InputEventKey_property_unicode) set.

When events are compared, properties are checked in the following priority - [keycode](class_inputeventkey.md#class_InputEventKey_property_keycode), [physical_keycode](class_inputeventkey.md#class_InputEventKey_property_physical_keycode) and [unicode](class_inputeventkey.md#class_InputEventKey_property_unicode). Events with the first matching value will be considered equal.

### Tutorials

- [Using InputEvent](../tutorials/inputs/inputevent.md)

### Properties


| [bool](class_bool.md#class_bool) | [echo](class_inputeventkey.md#class_InputEventKey_property_echo) | `false` |
| --- | --- | --- |
| Key | [key_label](class_inputeventkey.md#class_InputEventKey_property_key_label) | `0` |
| Key | [keycode](class_inputeventkey.md#class_InputEventKey_property_keycode) | `0` |
| KeyLocation | [location](class_inputeventkey.md#class_InputEventKey_property_location) | `0` |
| Key | [physical_keycode](class_inputeventkey.md#class_InputEventKey_property_physical_keycode) | `0` |
| [bool](class_bool.md#class_bool) | [pressed](class_inputeventkey.md#class_InputEventKey_property_pressed) | `false` |
| [int](class_int.md#class_int) | [unicode](class_inputeventkey.md#class_InputEventKey_property_unicode) | `0` |

### Methods


| [String](class_string.md#class_String) | [as_text_key_label](class_inputeventkey.md#class_InputEventKey_method_as_text_key_label) ( ) const |
| --- | --- |
| [String](class_string.md#class_String) | [as_text_keycode](class_inputeventkey.md#class_InputEventKey_method_as_text_keycode) ( ) const |
| [String](class_string.md#class_String) | [as_text_location](class_inputeventkey.md#class_InputEventKey_method_as_text_location) ( ) const |
| [String](class_string.md#class_String) | [as_text_physical_keycode](class_inputeventkey.md#class_InputEventKey_method_as_text_physical_keycode) ( ) const |
| Key | [get_key_label_with_modifiers](class_inputeventkey.md#class_InputEventKey_method_get_key_label_with_modifiers) ( ) const |
| Key | [get_keycode_with_modifiers](class_inputeventkey.md#class_InputEventKey_method_get_keycode_with_modifiers) ( ) const |
| Key | [get_physical_keycode_with_modifiers](class_inputeventkey.md#class_InputEventKey_method_get_physical_keycode_with_modifiers) ( ) const |

---

### Property Descriptions

<span id="class_InputEventKey_property_echo"></span>

[bool](class_bool.md#class_bool) **echo** = `false` [🔗](class_inputeventkey.md#class_InputEventKey_property_echo)

- void **set_echo** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_echo** ( )

If `true`, the key was already pressed before this event. An echo event is a repeated key event sent when the user is holding down the key.

 **Note:** The rate at which echo events are sent is typically around 20 events per second (after holding down the key for roughly half a second). However, the key repeat delay/speed can be changed by the user or disabled entirely in the operating system settings. To ensure your project works correctly on all configurations, do not assume the user has a specific key repeat configuration in your project's behavior.

---

<span id="class_InputEventKey_property_key_label"></span>

Key **key_label** = `0` [🔗](class_inputeventkey.md#class_InputEventKey_property_key_label)

- void **set_key_label** ( value: Key )
- Key **get_key_label** ( )

Represents the localized label printed on the key in the current keyboard layout, which corresponds to one of the Key constants or any valid Unicode character. Key labels are meant for key prompts.

For keyboard layouts with a single label on the key, it is equivalent to [keycode](class_inputeventkey.md#class_InputEventKey_property_keycode).

To get a human-readable representation of the **InputEventKey**, use `OS.get_keycode_string(event.key_label)` where `event` is the **InputEventKey**.

.. code:: text

    +-----+ +-----+
    | Q   | | Q   | - "Q" - keycode
    |   Й | |  ض | - "Й" and "ض" - key_label
    +-----+ +-----+

---

<span id="class_InputEventKey_property_keycode"></span>

Key **keycode** = `0` [🔗](class_inputeventkey.md#class_InputEventKey_property_keycode)

- void **set_keycode** ( value: Key )
- Key **get_keycode** ( )

Latin label printed on the key in the current keyboard layout, which corresponds to one of the Key constants. Key codes are meant for shortcuts expressed with a standard Latin keyboard, such as :kbd:`Ctrl + S` for a "Save" shortcut.

To get a human-readable representation of the **InputEventKey**, use `OS.get_keycode_string(event.keycode)` where `event` is the **InputEventKey**.

.. code:: text

    +-----+ +-----+
    | Q   | | Q   | - "Q" - keycode
    |   Й | |  ض | - "Й" and "ض" - key_label
    +-----+ +-----+

---

<span id="class_InputEventKey_property_location"></span>

KeyLocation **location** = `0` [🔗](class_inputeventkey.md#class_InputEventKey_property_location)

- void **set_location** ( value: KeyLocation )
- KeyLocation **get_location** ( )

Represents the location of a key which has both left and right versions, such as :kbd:`Shift` or :kbd:`Alt`.

---

<span id="class_InputEventKey_property_physical_keycode"></span>

Key **physical_keycode** = `0` [🔗](class_inputeventkey.md#class_InputEventKey_property_physical_keycode)

- void **set_physical_keycode** ( value: Key )
- Key **get_physical_keycode** ( )

Represents the physical location of a key on the 101/102-key US QWERTY keyboard, which corresponds to one of the Key constants. Physical key codes meant for game input, such as WASD movement, where only the location of the keys is important.

To get a human-readable representation of the **InputEventKey**, use [OS.get_keycode_string()](class_os.md#class_OS_method_get_keycode_string) in combination with [DisplayServer.keyboard_get_keycode_from_physical()](class_displayserver.md#class_DisplayServer_method_keyboard_get_keycode_from_physical) or [DisplayServer.keyboard_get_label_from_physical()](class_displayserver.md#class_DisplayServer_method_keyboard_get_label_from_physical):

.. tabs::

```
```

    func _input(event):
        if event is InputEventKey:
            var keycode = DisplayServer.keyboard_get_keycode_from_physical(event.physical_keycode)
            var label = DisplayServer.keyboard_get_label_from_physical(event.physical_keycode)
            print(OS.get_keycode_string(keycode))
            print(OS.get_keycode_string(label))

```
```

    public override void _Input(InputEvent @event)
    {
        if (@event is InputEventKey inputEventKey)
        {
            var keycode = DisplayServer.KeyboardGetKeycodeFromPhysical(inputEventKey.PhysicalKeycode);
            var label = DisplayServer.KeyboardGetLabelFromPhysical(inputEventKey.PhysicalKeycode);
            GD.Print(OS.GetKeycodeString(keycode));
            GD.Print(OS.GetKeycodeString(label));
        }
    }

---

<span id="class_InputEventKey_property_pressed"></span>

[bool](class_bool.md#class_bool) **pressed** = `false` [🔗](class_inputeventkey.md#class_InputEventKey_property_pressed)

- void **set_pressed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_pressed** ( )

If `true`, the key's state is pressed. If `false`, the key's state is released.

---

<span id="class_InputEventKey_property_unicode"></span>

[int](class_int.md#class_int) **unicode** = `0` [🔗](class_inputeventkey.md#class_InputEventKey_property_unicode)

- void **set_unicode** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_unicode** ( )

The key Unicode character code (when relevant), shifted by modifier keys. Unicode character codes for composite characters and complex scripts may not be available unless IME input mode is active. See [Window.set_ime_active()](class_window.md#class_Window_method_set_ime_active) for more information. Unicode character codes are meant for text input.

 **Note:** This property is set by the engine only for a pressed event. If the event is sent by an IME or a virtual keyboard, no corresponding key released event is sent.

---

### Method Descriptions

<span id="class_InputEventKey_method_as_text_key_label"></span>

[String](class_string.md#class_String) **as_text_key_label** ( ) *const* [🔗](class_inputeventkey.md#class_InputEventKey_method_as_text_key_label)

Returns a [String](class_string.md#class_String) representation of the event's [key_label](class_inputeventkey.md#class_InputEventKey_property_key_label) and modifiers.

---

<span id="class_InputEventKey_method_as_text_keycode"></span>

[String](class_string.md#class_String) **as_text_keycode** ( ) *const* [🔗](class_inputeventkey.md#class_InputEventKey_method_as_text_keycode)

Returns a [String](class_string.md#class_String) representation of the event's [keycode](class_inputeventkey.md#class_InputEventKey_property_keycode) and modifiers.

---

<span id="class_InputEventKey_method_as_text_location"></span>

[String](class_string.md#class_String) **as_text_location** ( ) *const* [🔗](class_inputeventkey.md#class_InputEventKey_method_as_text_location)

Returns a [String](class_string.md#class_String) representation of the event's [location](class_inputeventkey.md#class_InputEventKey_property_location). This will be a blank string if the event is not specific to a location.

---

<span id="class_InputEventKey_method_as_text_physical_keycode"></span>

[String](class_string.md#class_String) **as_text_physical_keycode** ( ) *const* [🔗](class_inputeventkey.md#class_InputEventKey_method_as_text_physical_keycode)

Returns a [String](class_string.md#class_String) representation of the event's [physical_keycode](class_inputeventkey.md#class_InputEventKey_property_physical_keycode) and modifiers.

---

<span id="class_InputEventKey_method_get_key_label_with_modifiers"></span>

Key **get_key_label_with_modifiers** ( ) *const* [🔗](class_inputeventkey.md#class_InputEventKey_method_get_key_label_with_modifiers)

Returns the localized key label combined with modifier keys such as :kbd:`Shift` or :kbd:`Alt`. See also [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers).

To get a human-readable representation of the **InputEventKey** with modifiers, use `OS.get_keycode_string(event.get_key_label_with_modifiers())` where `event` is the **InputEventKey**.

---

<span id="class_InputEventKey_method_get_keycode_with_modifiers"></span>

Key **get_keycode_with_modifiers** ( ) *const* [🔗](class_inputeventkey.md#class_InputEventKey_method_get_keycode_with_modifiers)

Returns the Latin keycode combined with modifier keys such as :kbd:`Shift` or :kbd:`Alt`. See also [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers).

To get a human-readable representation of the **InputEventKey** with modifiers, use `OS.get_keycode_string(event.get_keycode_with_modifiers())` where `event` is the **InputEventKey**.

---

<span id="class_InputEventKey_method_get_physical_keycode_with_modifiers"></span>

Key **get_physical_keycode_with_modifiers** ( ) *const* [🔗](class_inputeventkey.md#class_InputEventKey_method_get_physical_keycode_with_modifiers)

Returns the physical keycode combined with modifier keys such as :kbd:`Shift` or :kbd:`Alt`. See also [InputEventWithModifiers](class_inputeventwithmodifiers.md#class_InputEventWithModifiers).

To get a human-readable representation of the **InputEventKey** with modifiers, use `OS.get_keycode_string(event.get_physical_keycode_with_modifiers())` where `event` is the **InputEventKey**.
