<span id="class_Timer"></span>

## Timer

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A countdown timer.

### Description

The **Timer** node is a countdown timer and is the simplest way to handle time-based logic in the engine. When a timer reaches the end of its [wait_time](class_timer.md#class_Timer_property_wait_time), it will emit the [timeout](class_timer.md#class_Timer_signal_timeout) signal.

After a timer enters the scene tree, it can be manually started with [start()](class_timer.md#class_Timer_method_start). A timer node is also started automatically if [autostart](class_timer.md#class_Timer_property_autostart) is `true`.

Without requiring much code, a timer node can be added and configured in the editor. The [timeout](class_timer.md#class_Timer_signal_timeout) signal it emits can also be connected through the Signals dock in the editor:

::

    func _on_timer_timeout():
        print("Time to attack!")

 **Note:** To create a one-shot timer without instantiating a node, use [SceneTree.create_timer()](class_scenetree.md#class_SceneTree_method_create_timer).

 **Note:** Timers are affected by [Engine.time_scale](class_engine.md#class_Engine_property_time_scale) unless [ignore_time_scale](class_timer.md#class_Timer_property_ignore_time_scale) is `true`. The higher the time scale, the sooner timers will end. How often a timer processes may depend on the framerate or [Engine.physics_ticks_per_second](class_engine.md#class_Engine_property_physics_ticks_per_second).

### Tutorials

- 2D Dodge The Creeps Demo

### Properties


| [bool](class_bool.md#class_bool) | [autostart](class_timer.md#class_Timer_property_autostart) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [ignore_time_scale](class_timer.md#class_Timer_property_ignore_time_scale) | `false` |
| [bool](class_bool.md#class_bool) | [one_shot](class_timer.md#class_Timer_property_one_shot) | `false` |
| [bool](class_bool.md#class_bool) | [paused](class_timer.md#class_Timer_property_paused) |
| [TimerProcessCallback](class_timer.md#enum_Timer_TimerProcessCallback) | [process_callback](class_timer.md#class_Timer_property_process_callback) | `1` |
| [float](class_float.md#class_float) | [time_left](class_timer.md#class_Timer_property_time_left) |
| [float](class_float.md#class_float) | [wait_time](class_timer.md#class_Timer_property_wait_time) | `1.0` |

### Methods


| [bool](class_bool.md#class_bool) | [is_stopped](class_timer.md#class_Timer_method_is_stopped) ( ) const |
| --- | --- |
| void | [start](class_timer.md#class_Timer_method_start) ( time_sec: [float](class_float.md#class_float) = -1 ) |
| void | [stop](class_timer.md#class_Timer_method_stop) ( ) |

---

### Signals

<span id="class_Timer_signal_timeout"></span>

**timeout** ( ) [🔗](class_timer.md#class_Timer_signal_timeout)

Emitted when the timer reaches the end.

---

### Enumerations

<span id="enum_Timer_TimerProcessCallback"></span>

enum **TimerProcessCallback**: [🔗](class_timer.md#enum_Timer_TimerProcessCallback)

<span id="class_Timer_constant_TIMER_PROCESS_PHYSICS"></span>

[TimerProcessCallback](class_timer.md#enum_Timer_TimerProcessCallback) **TIMER_PROCESS_PHYSICS** = `0`

Update the timer every physics process frame (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS)).

<span id="class_Timer_constant_TIMER_PROCESS_IDLE"></span>

[TimerProcessCallback](class_timer.md#enum_Timer_TimerProcessCallback) **TIMER_PROCESS_IDLE** = `1`

Update the timer every process (rendered) frame (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class_Node_constant_NOTIFICATION_INTERNAL_PROCESS)).

---

### Property Descriptions

<span id="class_Timer_property_autostart"></span>

[bool](class_bool.md#class_bool) **autostart** = `false` [🔗](class_timer.md#class_Timer_property_autostart)

- void **set_autostart** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_autostart** ( )

If `true`, the timer will start immediately when it enters the scene tree.

 **Note:** After the timer enters the tree, this property is automatically set to `false`.

 **Note:** This property does nothing when the timer is running in the editor.

---

<span id="class_Timer_property_ignore_time_scale"></span>

[bool](class_bool.md#class_bool) **ignore_time_scale** = `false` [🔗](class_timer.md#class_Timer_property_ignore_time_scale)

- void **set_ignore_time_scale** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_ignoring_time_scale** ( )

If `true`, the timer will ignore [Engine.time_scale](class_engine.md#class_Engine_property_time_scale) and update with the real, elapsed time.

---

<span id="class_Timer_property_one_shot"></span>

[bool](class_bool.md#class_bool) **one_shot** = `false` [🔗](class_timer.md#class_Timer_property_one_shot)

- void **set_one_shot** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_one_shot** ( )

If `true`, the timer will stop after reaching the end. Otherwise, as by default, the timer will automatically restart.

---

<span id="class_Timer_property_paused"></span>

[bool](class_bool.md#class_bool) **paused** [🔗](class_timer.md#class_Timer_property_paused)

- void **set_paused** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_paused** ( )

If `true`, the timer is paused. A paused timer does not process until this property is set back to `false`, even when [start()](class_timer.md#class_Timer_method_start) is called. See also [stop()](class_timer.md#class_Timer_method_stop).

---

<span id="class_Timer_property_process_callback"></span>

[TimerProcessCallback](class_timer.md#enum_Timer_TimerProcessCallback) **process_callback** = `1` [🔗](class_timer.md#class_Timer_property_process_callback)

- void **set_timer_process_callback** ( value: [TimerProcessCallback](class_timer.md#enum_Timer_TimerProcessCallback) )
- [TimerProcessCallback](class_timer.md#enum_Timer_TimerProcessCallback) **get_timer_process_callback** ( )

Specifies when the timer is updated during the main loop.

---

<span id="class_Timer_property_time_left"></span>

[float](class_float.md#class_float) **time_left** [🔗](class_timer.md#class_Timer_property_time_left)

- [float](class_float.md#class_float) **get_time_left** ( )

The timer's remaining time in seconds. This is always `0` if the timer is stopped.

 **Note:** This property is read-only and cannot be modified. It is based on [wait_time](class_timer.md#class_Timer_property_wait_time).

---

<span id="class_Timer_property_wait_time"></span>

[float](class_float.md#class_float) **wait_time** = `1.0` [🔗](class_timer.md#class_Timer_property_wait_time)

- void **set_wait_time** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_wait_time** ( )

The time required for the timer to end, in seconds. This property can also be set every time [start()](class_timer.md#class_Timer_method_start) is called.

 **Note:** Timers can only process once per physics or process frame (depending on the [process_callback](class_timer.md#class_Timer_property_process_callback)). An unstable framerate may cause the timer to end inconsistently, which is especially noticeable if the wait time is lower than roughly `0.05` seconds. For very short timers, it is recommended to write your own code instead of using a **Timer** node. Timers are also affected by [Engine.time_scale](class_engine.md#class_Engine_property_time_scale).

---

### Method Descriptions

<span id="class_Timer_method_is_stopped"></span>

[bool](class_bool.md#class_bool) **is_stopped** ( ) *const* [🔗](class_timer.md#class_Timer_method_is_stopped)

Returns `true` if the timer is stopped or has not started.

---

<span id="class_Timer_method_start"></span>

void **start** ( time_sec: [float](class_float.md#class_float) = -1 ) [🔗](class_timer.md#class_Timer_method_start)

Starts the timer, or resets the timer if it was started already. Fails if the timer is not inside the scene tree. If `time_sec` is greater than `0`, this value is used for the [wait_time](class_timer.md#class_Timer_property_wait_time).

 **Note:** This method does not resume a paused timer. See [paused](class_timer.md#class_Timer_property_paused).

---

<span id="class_Timer_method_stop"></span>

void **stop** ( ) [🔗](class_timer.md#class_Timer_method_stop)

Stops the timer. See also [paused](class_timer.md#class_Timer_property_paused). Unlike [start()](class_timer.md#class_Timer_method_start), this can safely be called if the timer is not inside the scene tree.

 **Note:** Calling [stop()](class_timer.md#class_Timer_method_stop) does not emit the [timeout](class_timer.md#class_Timer_signal_timeout) signal, as the timer is not considered to have timed out. If this is desired, use `$Timer.timeout.emit()` after calling [stop()](class_timer.md#class_Timer_method_stop) to manually emit the signal.
