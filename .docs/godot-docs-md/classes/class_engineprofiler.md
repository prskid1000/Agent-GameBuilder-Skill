<span id="class_EngineProfiler"></span>

## EngineProfiler

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Base class for creating custom profilers.

### Description

This class can be used to implement custom profilers that are able to interact with the engine and editor debugger.

See [EngineDebugger](class_enginedebugger.md#class_EngineDebugger) and [EditorDebuggerPlugin](class_editordebuggerplugin.md#class_EditorDebuggerPlugin) for more information.

### Methods


| void | [_add_frame](class_engineprofiler.md#class_EngineProfiler_private_method__add_frame) ( data: [Array](class_array.md#class_Array) ) virtual |
| --- | --- |
| void | [_tick](class_engineprofiler.md#class_EngineProfiler_private_method__tick) ( frame_time: [float](class_float.md#class_float), process_time: [float](class_float.md#class_float), physics_time: [float](class_float.md#class_float), physics_frame_time: [float](class_float.md#class_float) ) virtual |
| void | [_toggle](class_engineprofiler.md#class_EngineProfiler_private_method__toggle) ( enable: [bool](class_bool.md#class_bool), options: [Array](class_array.md#class_Array) ) virtual |

---

### Method Descriptions

<span id="class_EngineProfiler_private_method__add_frame"></span>

void **_add_frame** ( data: [Array](class_array.md#class_Array) ) *virtual* [🔗](class_engineprofiler.md#class_EngineProfiler_private_method__add_frame)

Called when data is added to profiler using [EngineDebugger.profiler_add_frame_data()](class_enginedebugger.md#class_EngineDebugger_method_profiler_add_frame_data).

---

<span id="class_EngineProfiler_private_method__tick"></span>

void **_tick** ( frame_time: [float](class_float.md#class_float), process_time: [float](class_float.md#class_float), physics_time: [float](class_float.md#class_float), physics_frame_time: [float](class_float.md#class_float) ) *virtual* [🔗](class_engineprofiler.md#class_EngineProfiler_private_method__tick)

Called once every engine iteration when the profiler is active with information about the current frame. All time values are in seconds. Lower values represent faster processing times and are therefore considered better.

---

<span id="class_EngineProfiler_private_method__toggle"></span>

void **_toggle** ( enable: [bool](class_bool.md#class_bool), options: [Array](class_array.md#class_Array) ) *virtual* [🔗](class_engineprofiler.md#class_EngineProfiler_private_method__toggle)

Called when the profiler is enabled/disabled, along with a set of `options`.
