<span id="class_InputEventShortcut"></span>

## InputEventShortcut

**Inherits:** [InputEvent](class_inputevent.md#class_InputEvent) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a triggered keyboard [Shortcut](class_shortcut.md#class_Shortcut).

### Description

InputEventShortcut is a special event that can be received in [Node._input()](class_node.md#class_Node_private_method__input), [Node._shortcut_input()](class_node.md#class_Node_private_method__shortcut_input), and [Node._unhandled_input()](class_node.md#class_Node_private_method__unhandled_input). It is typically sent by the editor's Command Palette to trigger actions, but can also be sent manually using [Viewport.push_input()](class_viewport.md#class_Viewport_method_push_input).

### Properties


| [Shortcut](class_shortcut.md#class_Shortcut) | [shortcut](class_inputeventshortcut.md#class_InputEventShortcut_property_shortcut) |
| --- | --- |

---

### Property Descriptions

<span id="class_InputEventShortcut_property_shortcut"></span>

[Shortcut](class_shortcut.md#class_Shortcut) **shortcut** [🔗](class_inputeventshortcut.md#class_InputEventShortcut_property_shortcut)

- void **set_shortcut** ( value: [Shortcut](class_shortcut.md#class_Shortcut) )
- [Shortcut](class_shortcut.md#class_Shortcut) **get_shortcut** ( )

The [Shortcut](class_shortcut.md#class_Shortcut) represented by this event. Its [Shortcut.matches_event()](class_shortcut.md#class_Shortcut_method_matches_event) method will always return `true` for this event.
