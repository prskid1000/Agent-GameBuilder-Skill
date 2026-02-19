<span id="class_EngineDebugger"></span>

## EngineDebugger

**Inherits:** [Object](class_object.md#class_Object)

Exposes the internal debugger.

### Description

**EngineDebugger** handles the communication between the editor and the running game. It is active in the running game. Messages can be sent/received through it. It also manages the profilers.

### Methods


| void | [clear_breakpoints](class_enginedebugger.md#class_EngineDebugger_method_clear_breakpoints) ( ) |
| --- | --- |
| void | [debug](class_enginedebugger.md#class_EngineDebugger_method_debug) ( can_continue: [bool](class_bool.md#class_bool) = true, is_error_breakpoint: [bool](class_bool.md#class_bool) = false ) |
| [int](class_int.md#class_int) | [get_depth](class_enginedebugger.md#class_EngineDebugger_method_get_depth) ( ) const |
| [int](class_int.md#class_int) | [get_lines_left](class_enginedebugger.md#class_EngineDebugger_method_get_lines_left) ( ) const |
| [bool](class_bool.md#class_bool) | [has_capture](class_enginedebugger.md#class_EngineDebugger_method_has_capture) ( name: [StringName](class_stringname.md#class_StringName) ) |
| [bool](class_bool.md#class_bool) | [has_profiler](class_enginedebugger.md#class_EngineDebugger_method_has_profiler) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [insert_breakpoint](class_enginedebugger.md#class_EngineDebugger_method_insert_breakpoint) ( line: [int](class_int.md#class_int), source: [StringName](class_stringname.md#class_StringName) ) |
| [bool](class_bool.md#class_bool) | [is_active](class_enginedebugger.md#class_EngineDebugger_method_is_active) ( ) |
| [bool](class_bool.md#class_bool) | [is_breakpoint](class_enginedebugger.md#class_EngineDebugger_method_is_breakpoint) ( line: [int](class_int.md#class_int), source: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [is_profiling](class_enginedebugger.md#class_EngineDebugger_method_is_profiling) ( name: [StringName](class_stringname.md#class_StringName) ) |
| [bool](class_bool.md#class_bool) | [is_skipping_breakpoints](class_enginedebugger.md#class_EngineDebugger_method_is_skipping_breakpoints) ( ) const |
| void | [line_poll](class_enginedebugger.md#class_EngineDebugger_method_line_poll) ( ) |
| void | [profiler_add_frame_data](class_enginedebugger.md#class_EngineDebugger_method_profiler_add_frame_data) ( name: [StringName](class_stringname.md#class_StringName), data: [Array](class_array.md#class_Array) ) |
| void | [profiler_enable](class_enginedebugger.md#class_EngineDebugger_method_profiler_enable) ( name: [StringName](class_stringname.md#class_StringName), enable: [bool](class_bool.md#class_bool), arguments: [Array](class_array.md#class_Array) = [] ) |
| void | [register_message_capture](class_enginedebugger.md#class_EngineDebugger_method_register_message_capture) ( name: [StringName](class_stringname.md#class_StringName), callable: [Callable](class_callable.md#class_Callable) ) |
| void | [register_profiler](class_enginedebugger.md#class_EngineDebugger_method_register_profiler) ( name: [StringName](class_stringname.md#class_StringName), profiler: [EngineProfiler](class_engineprofiler.md#class_EngineProfiler) ) |
| void | [remove_breakpoint](class_enginedebugger.md#class_EngineDebugger_method_remove_breakpoint) ( line: [int](class_int.md#class_int), source: [StringName](class_stringname.md#class_StringName) ) |
| void | [script_debug](class_enginedebugger.md#class_EngineDebugger_method_script_debug) ( language: [ScriptLanguage](class_scriptlanguage.md#class_ScriptLanguage), can_continue: [bool](class_bool.md#class_bool) = true, is_error_breakpoint: [bool](class_bool.md#class_bool) = false ) |
| void | [send_message](class_enginedebugger.md#class_EngineDebugger_method_send_message) ( message: [String](class_string.md#class_String), data: [Array](class_array.md#class_Array) ) |
| void | [set_depth](class_enginedebugger.md#class_EngineDebugger_method_set_depth) ( depth: [int](class_int.md#class_int) ) |
| void | [set_lines_left](class_enginedebugger.md#class_EngineDebugger_method_set_lines_left) ( lines: [int](class_int.md#class_int) ) |
| void | [unregister_message_capture](class_enginedebugger.md#class_EngineDebugger_method_unregister_message_capture) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [unregister_profiler](class_enginedebugger.md#class_EngineDebugger_method_unregister_profiler) ( name: [StringName](class_stringname.md#class_StringName) ) |

---

### Method Descriptions

<span id="class_EngineDebugger_method_clear_breakpoints"></span>

void **clear_breakpoints** ( ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_clear_breakpoints)

Clears all breakpoints.

---

<span id="class_EngineDebugger_method_debug"></span>

void **debug** ( can_continue: [bool](class_bool.md#class_bool) = true, is_error_breakpoint: [bool](class_bool.md#class_bool) = false ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_debug)

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.

---

<span id="class_EngineDebugger_method_get_depth"></span>

[int](class_int.md#class_int) **get_depth** ( ) *const* [🔗](class_enginedebugger.md#class_EngineDebugger_method_get_depth)

**Experimental:** This method may be changed or removed in future versions.

Returns the current debug depth.

---

<span id="class_EngineDebugger_method_get_lines_left"></span>

[int](class_int.md#class_int) **get_lines_left** ( ) *const* [🔗](class_enginedebugger.md#class_EngineDebugger_method_get_lines_left)

**Experimental:** This method may be changed or removed in future versions.

Returns the number of lines that remain.

---

<span id="class_EngineDebugger_method_has_capture"></span>

[bool](class_bool.md#class_bool) **has_capture** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_has_capture)

Returns `true` if a capture with the given name is present otherwise `false`.

---

<span id="class_EngineDebugger_method_has_profiler"></span>

[bool](class_bool.md#class_bool) **has_profiler** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_has_profiler)

Returns `true` if a profiler with the given name is present otherwise `false`.

---

<span id="class_EngineDebugger_method_insert_breakpoint"></span>

void **insert_breakpoint** ( line: [int](class_int.md#class_int), source: [StringName](class_stringname.md#class_StringName) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_insert_breakpoint)

Inserts a new breakpoint with the given `source` and `line`.

---

<span id="class_EngineDebugger_method_is_active"></span>

[bool](class_bool.md#class_bool) **is_active** ( ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_is_active)

Returns `true` if the debugger is active otherwise `false`.

---

<span id="class_EngineDebugger_method_is_breakpoint"></span>

[bool](class_bool.md#class_bool) **is_breakpoint** ( line: [int](class_int.md#class_int), source: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_enginedebugger.md#class_EngineDebugger_method_is_breakpoint)

Returns `true` if the given `source` and `line` represent an existing breakpoint.

---

<span id="class_EngineDebugger_method_is_profiling"></span>

[bool](class_bool.md#class_bool) **is_profiling** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_is_profiling)

Returns `true` if a profiler with the given name is present and active otherwise `false`.

---

<span id="class_EngineDebugger_method_is_skipping_breakpoints"></span>

[bool](class_bool.md#class_bool) **is_skipping_breakpoints** ( ) *const* [🔗](class_enginedebugger.md#class_EngineDebugger_method_is_skipping_breakpoints)

Returns `true` if the debugger is skipping breakpoints otherwise `false`.

---

<span id="class_EngineDebugger_method_line_poll"></span>

void **line_poll** ( ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_line_poll)

Forces a processing loop of debugger events. The purpose of this method is just processing events every now and then when the script might get too busy, so that bugs like infinite loops can be caught.

---

<span id="class_EngineDebugger_method_profiler_add_frame_data"></span>

void **profiler_add_frame_data** ( name: [StringName](class_stringname.md#class_StringName), data: [Array](class_array.md#class_Array) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_profiler_add_frame_data)

Calls the `add` callable of the profiler with given `name` and `data`.

---

<span id="class_EngineDebugger_method_profiler_enable"></span>

void **profiler_enable** ( name: [StringName](class_stringname.md#class_StringName), enable: [bool](class_bool.md#class_bool), arguments: [Array](class_array.md#class_Array) = [] ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_profiler_enable)

Calls the `toggle` callable of the profiler with given `name` and `arguments`. Enables/Disables the same profiler depending on `enable` argument.

---

<span id="class_EngineDebugger_method_register_message_capture"></span>

void **register_message_capture** ( name: [StringName](class_stringname.md#class_StringName), callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_register_message_capture)

Registers a message capture with given `name`. If `name` is "my_message" then messages starting with "my_message:" will be called with the given callable.

The callable must accept a message string and a data array as argument. The callable should return `true` if the message is recognized.

 **Note:** The callable will receive the message with the prefix stripped, unlike [EditorDebuggerPlugin._capture()](class_editordebuggerplugin.md#class_EditorDebuggerPlugin_private_method__capture). See the [EditorDebuggerPlugin](class_editordebuggerplugin.md#class_EditorDebuggerPlugin) description for an example.

---

<span id="class_EngineDebugger_method_register_profiler"></span>

void **register_profiler** ( name: [StringName](class_stringname.md#class_StringName), profiler: [EngineProfiler](class_engineprofiler.md#class_EngineProfiler) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_register_profiler)

Registers a profiler with the given `name`. See [EngineProfiler](class_engineprofiler.md#class_EngineProfiler) for more information.

---

<span id="class_EngineDebugger_method_remove_breakpoint"></span>

void **remove_breakpoint** ( line: [int](class_int.md#class_int), source: [StringName](class_stringname.md#class_StringName) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_remove_breakpoint)

Removes a breakpoint with the given `source` and `line`.

---

<span id="class_EngineDebugger_method_script_debug"></span>

void **script_debug** ( language: [ScriptLanguage](class_scriptlanguage.md#class_ScriptLanguage), can_continue: [bool](class_bool.md#class_bool) = true, is_error_breakpoint: [bool](class_bool.md#class_bool) = false ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_script_debug)

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.

---

<span id="class_EngineDebugger_method_send_message"></span>

void **send_message** ( message: [String](class_string.md#class_String), data: [Array](class_array.md#class_Array) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_send_message)

Sends a message with given `message` and `data` array.

---

<span id="class_EngineDebugger_method_set_depth"></span>

void **set_depth** ( depth: [int](class_int.md#class_int) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_set_depth)

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging depth.

---

<span id="class_EngineDebugger_method_set_lines_left"></span>

void **set_lines_left** ( lines: [int](class_int.md#class_int) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_set_lines_left)

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging lines that remain.

---

<span id="class_EngineDebugger_method_unregister_message_capture"></span>

void **unregister_message_capture** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_unregister_message_capture)

Unregisters the message capture with given `name`.

---

<span id="class_EngineDebugger_method_unregister_profiler"></span>

void **unregister_profiler** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_enginedebugger.md#class_EngineDebugger_method_unregister_profiler)

Unregisters a profiler with given `name`.
