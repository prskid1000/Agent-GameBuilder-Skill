<span id="class_SubtweenTweener"></span>

## SubtweenTweener

**Inherits:** [Tweener](class_tweener.md#class_Tweener) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Runs a [Tween](class_tween.md#class_Tween) nested within another [Tween](class_tween.md#class_Tween).

### Description

**SubtweenTweener** is used to execute a [Tween](class_tween.md#class_Tween) as one step in a sequence defined by another [Tween](class_tween.md#class_Tween). See [Tween.tween_subtween()](class_tween.md#class_Tween_method_tween_subtween) for more usage information.

 **Note:** [Tween.tween_subtween()](class_tween.md#class_Tween_method_tween_subtween) is the only correct way to create **SubtweenTweener**. Any **SubtweenTweener** created manually will not function correctly.

### Methods


| [SubtweenTweener](class_subtweentweener.md#class_SubtweenTweener) | [set_delay](class_subtweentweener.md#class_SubtweenTweener_method_set_delay) ( delay: [float](class_float.md#class_float) ) |
| --- | --- |

---

### Method Descriptions

<span id="class_SubtweenTweener_method_set_delay"></span>

[SubtweenTweener](class_subtweentweener.md#class_SubtweenTweener) **set_delay** ( delay: [float](class_float.md#class_float) ) [🔗](class_subtweentweener.md#class_SubtweenTweener_method_set_delay)

Sets the time in seconds after which the **SubtweenTweener** will start running the subtween. By default there's no delay.
