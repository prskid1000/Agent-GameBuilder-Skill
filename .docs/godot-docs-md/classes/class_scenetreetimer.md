<span id="class_SceneTreeTimer"></span>

## SceneTreeTimer

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

One-shot timer.

### Description

A one-shot timer managed by the scene tree, which emits [timeout](class_scenetreetimer.md#class_SceneTreeTimer_signal_timeout) on completion. See also [SceneTree.create_timer()](class_scenetree.md#class_SceneTree_method_create_timer).

As opposed to [Timer](class_timer.md#class_Timer), it does not require the instantiation of a node. Commonly used to create a one-shot delay timer as in the following example:

.. tabs::

```
```

    func some_function():
        print("Timer started.")
        await get_tree().create_timer(1.0).timeout
        print("Timer ended.")

```
```

    public async Task SomeFunction()
    {
        GD.Print("Timer started.");
        await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
        GD.Print("Timer ended.");
    }

The timer will be dereferenced after its time elapses. To preserve the timer, you can keep a reference to it. See [RefCounted](class_refcounted.md#class_RefCounted).

 **Note:** The timer is processed after all of the nodes in the current frame, i.e. node's [Node._process()](class_node.md#class_Node_private_method__process) method would be called before the timer (or [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) if `process_in_physics` in [SceneTree.create_timer()](class_scenetree.md#class_SceneTree_method_create_timer) has been set to `true`).

### Properties


| [float](class_float.md#class_float) | [time_left](class_scenetreetimer.md#class_SceneTreeTimer_property_time_left) |
| --- | --- |

---

### Signals

<span id="class_SceneTreeTimer_signal_timeout"></span>

**timeout** ( ) [🔗](class_scenetreetimer.md#class_SceneTreeTimer_signal_timeout)

Emitted when the timer reaches 0.

---

### Property Descriptions

<span id="class_SceneTreeTimer_property_time_left"></span>

[float](class_float.md#class_float) **time_left** [🔗](class_scenetreetimer.md#class_SceneTreeTimer_property_time_left)

- void **set_time_left** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_time_left** ( )

The time remaining (in seconds).
