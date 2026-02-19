<span id="class_InputMap"></span>

## InputMap

**Inherits:** [Object](class_object.md#class_Object)

A singleton that manages all [InputEventAction](class_inputeventaction.md#class_InputEventAction) s.

### Description

Manages all [InputEventAction](class_inputeventaction.md#class_InputEventAction) which can be created/modified from the project settings menu **Project > Project Settings > Input Map** or in code with [add_action()](class_inputmap.md#class_InputMap_method_add_action) and [action_add_event()](class_inputmap.md#class_InputMap_method_action_add_event). See [Node._input()](class_node.md#class_Node_private_method__input).

### Tutorials

- `Using InputEvent: InputMap <../tutorials/inputs/inputevent.html#inputmap>`__

### Methods


| void | [action_add_event](class_inputmap.md#class_InputMap_method_action_add_event) ( action: [StringName](class_stringname.md#class_StringName), event: [InputEvent](class_inputevent.md#class_InputEvent) ) |
| --- | --- |
| void | [action_erase_event](class_inputmap.md#class_InputMap_method_action_erase_event) ( action: [StringName](class_stringname.md#class_StringName), event: [InputEvent](class_inputevent.md#class_InputEvent) ) |
| void | [action_erase_events](class_inputmap.md#class_InputMap_method_action_erase_events) ( action: [StringName](class_stringname.md#class_StringName) ) |
| [float](class_float.md#class_float) | [action_get_deadzone](class_inputmap.md#class_InputMap_method_action_get_deadzone) ( action: [StringName](class_stringname.md#class_StringName) ) |
| [Array](class_array.md#class_Array)\[[InputEvent](class_inputevent.md#class_InputEvent)\] | [action_get_events](class_inputmap.md#class_InputMap_method_action_get_events) ( action: [StringName](class_stringname.md#class_StringName) ) |
| [bool](class_bool.md#class_bool) | [action_has_event](class_inputmap.md#class_InputMap_method_action_has_event) ( action: [StringName](class_stringname.md#class_StringName), event: [InputEvent](class_inputevent.md#class_InputEvent) ) |
| void | [action_set_deadzone](class_inputmap.md#class_InputMap_method_action_set_deadzone) ( action: [StringName](class_stringname.md#class_StringName), deadzone: [float](class_float.md#class_float) ) |
| void | [add_action](class_inputmap.md#class_InputMap_method_add_action) ( action: [StringName](class_stringname.md#class_StringName), deadzone: [float](class_float.md#class_float) = 0.2 ) |
| void | [erase_action](class_inputmap.md#class_InputMap_method_erase_action) ( action: [StringName](class_stringname.md#class_StringName) ) |
| [bool](class_bool.md#class_bool) | [event_is_action](class_inputmap.md#class_InputMap_method_event_is_action) ( event: [InputEvent](class_inputevent.md#class_InputEvent), action: [StringName](class_stringname.md#class_StringName), exact_match: [bool](class_bool.md#class_bool) = false ) const |
| [String](class_string.md#class_String) | [get_action_description](class_inputmap.md#class_InputMap_method_get_action_description) ( action: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] | [get_actions](class_inputmap.md#class_InputMap_method_get_actions) ( ) |
| [bool](class_bool.md#class_bool) | [has_action](class_inputmap.md#class_InputMap_method_has_action) ( action: [StringName](class_stringname.md#class_StringName) ) const |
| void | [load_from_project_settings](class_inputmap.md#class_InputMap_method_load_from_project_settings) ( ) |

---

### Method Descriptions

<span id="class_InputMap_method_action_add_event"></span>

void **action_add_event** ( action: [StringName](class_stringname.md#class_StringName), event: [InputEvent](class_inputevent.md#class_InputEvent) ) [🔗](class_inputmap.md#class_InputMap_method_action_add_event)

Adds an [InputEvent](class_inputevent.md#class_InputEvent) to an action. This [InputEvent](class_inputevent.md#class_InputEvent) will trigger the action.

---

<span id="class_InputMap_method_action_erase_event"></span>

void **action_erase_event** ( action: [StringName](class_stringname.md#class_StringName), event: [InputEvent](class_inputevent.md#class_InputEvent) ) [🔗](class_inputmap.md#class_InputMap_method_action_erase_event)

Removes an [InputEvent](class_inputevent.md#class_InputEvent) from an action.

---

<span id="class_InputMap_method_action_erase_events"></span>

void **action_erase_events** ( action: [StringName](class_stringname.md#class_StringName) ) [🔗](class_inputmap.md#class_InputMap_method_action_erase_events)

Removes all events from an action.

---

<span id="class_InputMap_method_action_get_deadzone"></span>

[float](class_float.md#class_float) **action_get_deadzone** ( action: [StringName](class_stringname.md#class_StringName) ) [🔗](class_inputmap.md#class_InputMap_method_action_get_deadzone)

Returns a deadzone value for the action.

---

<span id="class_InputMap_method_action_get_events"></span>

[Array](class_array.md#class_Array)\[[InputEvent](class_inputevent.md#class_InputEvent)\] **action_get_events** ( action: [StringName](class_stringname.md#class_StringName) ) [🔗](class_inputmap.md#class_InputMap_method_action_get_events)

Returns an array of [InputEvent](class_inputevent.md#class_InputEvent) s associated with a given action.

 **Note:** When used in the editor (e.g. a tool script or [EditorPlugin](class_editorplugin.md#class_EditorPlugin)), this method will return events for the editor action. If you want to access your project's input binds from the editor, read the `input/*` settings from [ProjectSettings](class_projectsettings.md#class_ProjectSettings).

---

<span id="class_InputMap_method_action_has_event"></span>

[bool](class_bool.md#class_bool) **action_has_event** ( action: [StringName](class_stringname.md#class_StringName), event: [InputEvent](class_inputevent.md#class_InputEvent) ) [🔗](class_inputmap.md#class_InputMap_method_action_has_event)

Returns `true` if the action has the given [InputEvent](class_inputevent.md#class_InputEvent) associated with it.

---

<span id="class_InputMap_method_action_set_deadzone"></span>

void **action_set_deadzone** ( action: [StringName](class_stringname.md#class_StringName), deadzone: [float](class_float.md#class_float) ) [🔗](class_inputmap.md#class_InputMap_method_action_set_deadzone)

Sets a deadzone value for the action.

---

<span id="class_InputMap_method_add_action"></span>

void **add_action** ( action: [StringName](class_stringname.md#class_StringName), deadzone: [float](class_float.md#class_float) = 0.2 ) [🔗](class_inputmap.md#class_InputMap_method_add_action)

Adds an empty action to the **InputMap** with a configurable `deadzone`.

An [InputEvent](class_inputevent.md#class_InputEvent) can then be added to this action with [action_add_event()](class_inputmap.md#class_InputMap_method_action_add_event).

---

<span id="class_InputMap_method_erase_action"></span>

void **erase_action** ( action: [StringName](class_stringname.md#class_StringName) ) [🔗](class_inputmap.md#class_InputMap_method_erase_action)

Removes an action from the **InputMap**.

---

<span id="class_InputMap_method_event_is_action"></span>

[bool](class_bool.md#class_bool) **event_is_action** ( event: [InputEvent](class_inputevent.md#class_InputEvent), action: [StringName](class_stringname.md#class_StringName), exact_match: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_inputmap.md#class_InputMap_method_event_is_action)

Returns `true` if the given event is part of an existing action. This method ignores keyboard modifiers if the given [InputEvent](class_inputevent.md#class_InputEvent) is not pressed (for proper release detection). See [action_has_event()](class_inputmap.md#class_InputMap_method_action_has_event) if you don't want this behavior.

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey](class_inputeventkey.md#class_InputEventKey) and [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton) events, and the direction for [InputEventJoypadMotion](class_inputeventjoypadmotion.md#class_InputEventJoypadMotion) events.

---

<span id="class_InputMap_method_get_action_description"></span>

[String](class_string.md#class_String) **get_action_description** ( action: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_inputmap.md#class_InputMap_method_get_action_description)

Returns the human-readable description of the given action.

---

<span id="class_InputMap_method_get_actions"></span>

[Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] **get_actions** ( ) [🔗](class_inputmap.md#class_InputMap_method_get_actions)

Returns an array of all actions in the **InputMap**.

---

<span id="class_InputMap_method_has_action"></span>

[bool](class_bool.md#class_bool) **has_action** ( action: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_inputmap.md#class_InputMap_method_has_action)

Returns `true` if the **InputMap** has a registered action with the given name.

---

<span id="class_InputMap_method_load_from_project_settings"></span>

void **load_from_project_settings** ( ) [🔗](class_inputmap.md#class_InputMap_method_load_from_project_settings)

Clears all [InputEventAction](class_inputeventaction.md#class_InputEventAction) in the **InputMap** and load it anew from [ProjectSettings](class_projectsettings.md#class_ProjectSettings).
