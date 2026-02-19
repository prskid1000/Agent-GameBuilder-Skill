<span id="class_CallbackTweener"></span>

## CallbackTweener

**Inherits:** [Tweener](class_tweener.md#class_Tweener) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Calls the specified method after optional delay.

### Description

**CallbackTweener** is used to call a method in a tweening sequence. See [Tween.tween_callback()](class_tween.md#class_Tween_method_tween_callback) for more usage information.

The tweener will finish automatically if the callback's target object is freed.

 **Note:** [Tween.tween_callback()](class_tween.md#class_Tween_method_tween_callback) is the only correct way to create **CallbackTweener**. Any **CallbackTweener** created manually will not function correctly.

### Methods


| [CallbackTweener](class_callbacktweener.md#class_CallbackTweener) | [set_delay](class_callbacktweener.md#class_CallbackTweener_method_set_delay) ( delay: [float](class_float.md#class_float) ) |
| --- | --- |

---

### Method Descriptions

<span id="class_CallbackTweener_method_set_delay"></span>

[CallbackTweener](class_callbacktweener.md#class_CallbackTweener) **set_delay** ( delay: [float](class_float.md#class_float) ) [🔗](class_callbacktweener.md#class_CallbackTweener_method_set_delay)

Makes the callback call delayed by given time in seconds.

 **Example:** Call [Node.queue_free()](class_node.md#class_Node_method_queue_free) after 2 seconds:

::

    var tween = get_tree().create_tween()
    tween.tween_callback(queue_free).set_delay(2)
