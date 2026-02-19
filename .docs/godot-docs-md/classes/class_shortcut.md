<span id="class_Shortcut"></span>

## Shortcut

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A shortcut for binding input.

### Description

Shortcuts (also known as hotkeys) are containers of [InputEvent](class_inputevent.md#class_InputEvent) resources. They are commonly used to interact with a [Control](class_control.md#class_Control) element from an [InputEvent](class_inputevent.md#class_InputEvent).

One shortcut can contain multiple [InputEvent](class_inputevent.md#class_InputEvent) resources, making it possible to trigger one action with multiple different inputs.

 **Example:** Capture the :kbd:`Ctrl + S` shortcut using a **Shortcut** resource:

.. tabs::

```
```

    extends Node

    var save_shortcut = Shortcut.new()
    func _ready():
        var key_event = InputEventKey.new()
        key_event.keycode = KEY_S
        key_event.ctrl_pressed = true
        key_event.command_or_control_autoremap = true # Swaps Ctrl for Command on Mac.
        save_shortcut.events = [key_event]

    func _input(event):
        if save_shortcut.matches_event(event) and event.is_pressed() and not event.is_echo():
            print("Save shortcut pressed!")
            get_viewport().set_input_as_handled()

```
```

    using Godot;

    public partial class MyNode : Node
    {
        private readonly Shortcut _saveShortcut = new Shortcut();

        public override void _Ready()
        {
            InputEventKey keyEvent = new InputEventKey
            {
                Keycode = Key.S,
                CtrlPressed = true,
                CommandOrControlAutoremap = true, // Swaps Ctrl for Command on Mac.
            };

            _saveShortcut.Events = [keyEvent];
        }

        public override void _Input(InputEvent @event)
        {
            if (@event is InputEventKey keyEvent &&
                _saveShortcut.MatchesEvent(@event) &&
                keyEvent.Pressed && !keyEvent.Echo)
            {
                GD.Print("Save shortcut pressed!");
                GetViewport().SetInputAsHandled();
            }
        }
    }

### Properties


| [Array](class_array.md#class_Array) | [events](class_shortcut.md#class_Shortcut_property_events) | `[]` |
| --- | --- | --- |

### Methods


| [String](class_string.md#class_String) | [get_as_text](class_shortcut.md#class_Shortcut_method_get_as_text) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [has_valid_event](class_shortcut.md#class_Shortcut_method_has_valid_event) ( ) const |
| [bool](class_bool.md#class_bool) | [matches_event](class_shortcut.md#class_Shortcut_method_matches_event) ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) const |

---

### Property Descriptions

<span id="class_Shortcut_property_events"></span>

[Array](class_array.md#class_Array) **events** = `[]` [🔗](class_shortcut.md#class_Shortcut_property_events)

- void **set_events** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_events** ( )

The shortcut's [InputEvent](class_inputevent.md#class_InputEvent) array.

Generally the [InputEvent](class_inputevent.md#class_InputEvent) used is an [InputEventKey](class_inputeventkey.md#class_InputEventKey), though it can be any [InputEvent](class_inputevent.md#class_InputEvent), including an [InputEventAction](class_inputeventaction.md#class_InputEventAction).

---

### Method Descriptions

<span id="class_Shortcut_method_get_as_text"></span>

[String](class_string.md#class_String) **get_as_text** ( ) *const* [🔗](class_shortcut.md#class_Shortcut_method_get_as_text)

Returns the shortcut's first valid [InputEvent](class_inputevent.md#class_InputEvent) as a [String](class_string.md#class_String).

---

<span id="class_Shortcut_method_has_valid_event"></span>

[bool](class_bool.md#class_bool) **has_valid_event** ( ) *const* [🔗](class_shortcut.md#class_Shortcut_method_has_valid_event)

Returns whether [events](class_shortcut.md#class_Shortcut_property_events) contains an [InputEvent](class_inputevent.md#class_InputEvent) which is valid.

---

<span id="class_Shortcut_method_matches_event"></span>

[bool](class_bool.md#class_bool) **matches_event** ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) *const* [🔗](class_shortcut.md#class_Shortcut_method_matches_event)

Returns whether any [InputEvent](class_inputevent.md#class_InputEvent) in [events](class_shortcut.md#class_Shortcut_property_events) equals `event`. This uses [InputEvent.is_match()](class_inputevent.md#class_InputEvent_method_is_match) to compare events.
