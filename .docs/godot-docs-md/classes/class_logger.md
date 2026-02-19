<span id="class_Logger"></span>

## Logger

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Custom logger to receive messages from the internal error/warning stream.

### Description

Custom logger to receive messages from the internal error/warning stream. Loggers are registered via [OS.add_logger()](class_os.md#class_OS_method_add_logger).

### Methods


| void | [_log_error](class_logger.md#class_Logger_private_method__log_error) ( function: [String](class_string.md#class_String), file: [String](class_string.md#class_String), line: [int](class_int.md#class_int), code: [String](class_string.md#class_String), rationale: [String](class_string.md#class_String), editor_notify: [bool](class_bool.md#class_bool), error_type: [int](class_int.md#class_int), script_backtraces: [Array](class_array.md#class_Array)\[[ScriptBacktrace](class_scriptbacktrace.md#class_ScriptBacktrace)\] ) virtual |
| --- | --- |
| void | [_log_message](class_logger.md#class_Logger_private_method__log_message) ( message: [String](class_string.md#class_String), error: [bool](class_bool.md#class_bool) ) virtual |

---

### Enumerations

<span id="enum_Logger_ErrorType"></span>

enum **ErrorType**: [🔗](class_logger.md#enum_Logger_ErrorType)

<span id="class_Logger_constant_ERROR_TYPE_ERROR"></span>

[ErrorType](class_logger.md#enum_Logger_ErrorType) **ERROR_TYPE_ERROR** = `0`

The message received is an error.

<span id="class_Logger_constant_ERROR_TYPE_WARNING"></span>

[ErrorType](class_logger.md#enum_Logger_ErrorType) **ERROR_TYPE_WARNING** = `1`

The message received is a warning.

<span id="class_Logger_constant_ERROR_TYPE_SCRIPT"></span>

[ErrorType](class_logger.md#enum_Logger_ErrorType) **ERROR_TYPE_SCRIPT** = `2`

The message received is a script error.

<span id="class_Logger_constant_ERROR_TYPE_SHADER"></span>

[ErrorType](class_logger.md#enum_Logger_ErrorType) **ERROR_TYPE_SHADER** = `3`

The message received is a shader error.

---

### Method Descriptions

<span id="class_Logger_private_method__log_error"></span>

void **_log_error** ( function: [String](class_string.md#class_String), file: [String](class_string.md#class_String), line: [int](class_int.md#class_int), code: [String](class_string.md#class_String), rationale: [String](class_string.md#class_String), editor_notify: [bool](class_bool.md#class_bool), error_type: [int](class_int.md#class_int), script_backtraces: [Array](class_array.md#class_Array)\[[ScriptBacktrace](class_scriptbacktrace.md#class_ScriptBacktrace)\] ) *virtual* [🔗](class_logger.md#class_Logger_private_method__log_error)

Called when an error is logged. The error provides the `function`, `file`, and `line` that it originated from, as well as either the `code` that generated the error or a `rationale`.

The type of error provided by `error_type` is described in the [ErrorType](class_logger.md#enum_Logger_ErrorType) enumeration.

Additionally, `script_backtraces` provides backtraces for each of the script languages. These will only contain stack frames in editor builds and debug builds by default. To enable them for release builds as well, you need to enable ProjectSettings.debug/settings/gdscript/always_track_call_stacks.

 **Warning:** This method will be called from threads other than the main thread, possibly at the same time, so you will need to have some kind of thread-safety in your implementation of it, like a [Mutex](class_mutex.md#class_Mutex).

 **Note:** `script_backtraces` will not contain any captured variables, due to its prohibitively high cost. To get those you will need to capture the backtraces yourself, from within the **Logger** virtual methods, using [Engine.capture_script_backtraces()](class_engine.md#class_Engine_method_capture_script_backtraces).

 **Note:** Logging errors from this method using functions like @GlobalScope.push_error() or @GlobalScope.push_warning() is not supported, as it could cause infinite recursion. These errors will only show up in the console output.

---

<span id="class_Logger_private_method__log_message"></span>

void **_log_message** ( message: [String](class_string.md#class_String), error: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_logger.md#class_Logger_private_method__log_message)

Called when a message is logged. If `error` is `true`, then this message was meant to be sent to `stderr`.

 **Warning:** This method will be called from threads other than the main thread, possibly at the same time, so you will need to have some kind of thread-safety in your implementation of it, like a [Mutex](class_mutex.md#class_Mutex).

 **Note:** Logging another message from this method using functions like @GlobalScope.print() is not supported, as it could cause infinite recursion. These messages will only show up in the console output.
