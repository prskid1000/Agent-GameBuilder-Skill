<span id="class_EditorDebuggerSession"></span>

## EditorDebuggerSession

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A class to interact with the editor debugger.

### Description

This class cannot be directly instantiated and must be retrieved via an [EditorDebuggerPlugin](class_editordebuggerplugin.md#class_EditorDebuggerPlugin).

You can add tabs to the session UI via [add_session_tab()](class_editordebuggersession.md#class_EditorDebuggerSession_method_add_session_tab), send messages via [send_message()](class_editordebuggersession.md#class_EditorDebuggerSession_method_send_message), and toggle [EngineProfiler](class_engineprofiler.md#class_EngineProfiler) s via [toggle_profiler()](class_editordebuggersession.md#class_EditorDebuggerSession_method_toggle_profiler).

### Methods


| void | [add_session_tab](class_editordebuggersession.md#class_EditorDebuggerSession_method_add_session_tab) ( control: [Control](class_control.md#class_Control) ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [is_active](class_editordebuggersession.md#class_EditorDebuggerSession_method_is_active) ( ) |
| [bool](class_bool.md#class_bool) | [is_breaked](class_editordebuggersession.md#class_EditorDebuggerSession_method_is_breaked) ( ) |
| [bool](class_bool.md#class_bool) | [is_debuggable](class_editordebuggersession.md#class_EditorDebuggerSession_method_is_debuggable) ( ) |
| void | [remove_session_tab](class_editordebuggersession.md#class_EditorDebuggerSession_method_remove_session_tab) ( control: [Control](class_control.md#class_Control) ) |
| void | [send_message](class_editordebuggersession.md#class_EditorDebuggerSession_method_send_message) ( message: [String](class_string.md#class_String), data: [Array](class_array.md#class_Array) = [] ) |
| void | [set_breakpoint](class_editordebuggersession.md#class_EditorDebuggerSession_method_set_breakpoint) ( path: [String](class_string.md#class_String), line: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [toggle_profiler](class_editordebuggersession.md#class_EditorDebuggerSession_method_toggle_profiler) ( profiler: [String](class_string.md#class_String), enable: [bool](class_bool.md#class_bool), data: [Array](class_array.md#class_Array) = [] ) |

---

### Signals

<span id="class_EditorDebuggerSession_signal_breaked"></span>

**breaked** ( can_debug: [bool](class_bool.md#class_bool) ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_signal_breaked)

Emitted when the attached remote instance enters a break state. If `can_debug` is `true`, the remote instance will enter the debug loop.

---

<span id="class_EditorDebuggerSession_signal_continued"></span>

**continued** ( ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_signal_continued)

Emitted when the attached remote instance exits a break state.

---

<span id="class_EditorDebuggerSession_signal_started"></span>

**started** ( ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_signal_started)

Emitted when a remote instance is attached to this session (i.e. the session becomes active).

---

<span id="class_EditorDebuggerSession_signal_stopped"></span>

**stopped** ( ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_signal_stopped)

Emitted when a remote instance is detached from this session (i.e. the session becomes inactive).

---

### Method Descriptions

<span id="class_EditorDebuggerSession_method_add_session_tab"></span>

void **add_session_tab** ( control: [Control](class_control.md#class_Control) ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_method_add_session_tab)

Adds the given `control` to the debug session UI in the debugger bottom panel. The `control`'s node name will be used as the tab title.

---

<span id="class_EditorDebuggerSession_method_is_active"></span>

[bool](class_bool.md#class_bool) **is_active** ( ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_method_is_active)

Returns `true` if the debug session is currently attached to a remote instance.

---

<span id="class_EditorDebuggerSession_method_is_breaked"></span>

[bool](class_bool.md#class_bool) **is_breaked** ( ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_method_is_breaked)

Returns `true` if the attached remote instance is currently in the debug loop.

---

<span id="class_EditorDebuggerSession_method_is_debuggable"></span>

[bool](class_bool.md#class_bool) **is_debuggable** ( ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_method_is_debuggable)

Returns `true` if the attached remote instance can be debugged.

---

<span id="class_EditorDebuggerSession_method_remove_session_tab"></span>

void **remove_session_tab** ( control: [Control](class_control.md#class_Control) ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_method_remove_session_tab)

Removes the given `control` from the debug session UI in the debugger bottom panel.

---

<span id="class_EditorDebuggerSession_method_send_message"></span>

void **send_message** ( message: [String](class_string.md#class_String), data: [Array](class_array.md#class_Array) = [] ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_method_send_message)

Sends the given `message` to the attached remote instance, optionally passing additionally `data`. See [EngineDebugger](class_enginedebugger.md#class_EngineDebugger) for how to retrieve those messages.

---

<span id="class_EditorDebuggerSession_method_set_breakpoint"></span>

void **set_breakpoint** ( path: [String](class_string.md#class_String), line: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_method_set_breakpoint)

Enables or disables a specific breakpoint based on `enabled`, updating the Editor Breakpoint Panel accordingly.

---

<span id="class_EditorDebuggerSession_method_toggle_profiler"></span>

void **toggle_profiler** ( profiler: [String](class_string.md#class_String), enable: [bool](class_bool.md#class_bool), data: [Array](class_array.md#class_Array) = [] ) [🔗](class_editordebuggersession.md#class_EditorDebuggerSession_method_toggle_profiler)

Toggle the given `profiler` on the attached remote instance, optionally passing additionally `data`. See [EngineProfiler](class_engineprofiler.md#class_EngineProfiler) for more details.
