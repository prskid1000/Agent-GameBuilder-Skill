<span id="class_GodotInstance"></span>

## GodotInstance

**Inherits:** [Object](class_object.md#class_Object)

Provides access to an embedded Godot instance.

### Description

GodotInstance represents a running Godot instance that is controlled from an outside codebase, without a perpetual main loop. It is created by the C API `libgodot_create_godot_instance`. Only one may be created per process.

### Methods


| void | [focus_in](class_godotinstance.md#class_GodotInstance_method_focus_in) ( ) |
| --- | --- |
| void | [focus_out](class_godotinstance.md#class_GodotInstance_method_focus_out) ( ) |
| [bool](class_bool.md#class_bool) | [is_started](class_godotinstance.md#class_GodotInstance_method_is_started) ( ) |
| [bool](class_bool.md#class_bool) | [iteration](class_godotinstance.md#class_GodotInstance_method_iteration) ( ) |
| void | [pause](class_godotinstance.md#class_GodotInstance_method_pause) ( ) |
| void | [resume](class_godotinstance.md#class_GodotInstance_method_resume) ( ) |
| [bool](class_bool.md#class_bool) | [start](class_godotinstance.md#class_GodotInstance_method_start) ( ) |

---

### Method Descriptions

<span id="class_GodotInstance_method_focus_in"></span>

void **focus_in** ( ) [🔗](class_godotinstance.md#class_GodotInstance_method_focus_in)

Notifies the instance that it is now in focus.

---

<span id="class_GodotInstance_method_focus_out"></span>

void **focus_out** ( ) [🔗](class_godotinstance.md#class_GodotInstance_method_focus_out)

Notifies the instance that it is now not in focus.

---

<span id="class_GodotInstance_method_is_started"></span>

[bool](class_bool.md#class_bool) **is_started** ( ) [🔗](class_godotinstance.md#class_GodotInstance_method_is_started)

Returns `true` if this instance has been fully started.

---

<span id="class_GodotInstance_method_iteration"></span>

[bool](class_bool.md#class_bool) **iteration** ( ) [🔗](class_godotinstance.md#class_GodotInstance_method_iteration)

Runs a single iteration of the main loop. Returns `true` if the engine is attempting to quit.

---

<span id="class_GodotInstance_method_pause"></span>

void **pause** ( ) [🔗](class_godotinstance.md#class_GodotInstance_method_pause)

Notifies the instance that it is going to be paused.

---

<span id="class_GodotInstance_method_resume"></span>

void **resume** ( ) [🔗](class_godotinstance.md#class_GodotInstance_method_resume)

Notifies the instance that it is being resumed.

---

<span id="class_GodotInstance_method_start"></span>

[bool](class_bool.md#class_bool) **start** ( ) [🔗](class_godotinstance.md#class_GodotInstance_method_start)

Finishes this instance's startup sequence. Returns `true` on success.
