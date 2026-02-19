<span id="class_MethodTweener"></span>

## MethodTweener

**Inherits:** [Tweener](class_tweener.md#class_Tweener) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Interpolates an abstract value and supplies it to a method called over time.

### Description

**MethodTweener** is similar to a combination of [CallbackTweener](class_callbacktweener.md#class_CallbackTweener) and [PropertyTweener](class_propertytweener.md#class_PropertyTweener). It calls a method providing an interpolated value as a parameter. See [Tween.tween_method()](class_tween.md#class_Tween_method_tween_method) for more usage information.

The tweener will finish automatically if the callback's target object is freed.

 **Note:** [Tween.tween_method()](class_tween.md#class_Tween_method_tween_method) is the only correct way to create **MethodTweener**. Any **MethodTweener** created manually will not function correctly.

### Methods


| [MethodTweener](class_methodtweener.md#class_MethodTweener) | [set_delay](class_methodtweener.md#class_MethodTweener_method_set_delay) ( delay: [float](class_float.md#class_float) ) |
| --- | --- |
| [MethodTweener](class_methodtweener.md#class_MethodTweener) | [set_ease](class_methodtweener.md#class_MethodTweener_method_set_ease) ( ease: [EaseType](class_tween.md#enum_Tween_EaseType) ) |
| [MethodTweener](class_methodtweener.md#class_MethodTweener) | [set_trans](class_methodtweener.md#class_MethodTweener_method_set_trans) ( trans: [TransitionType](class_tween.md#enum_Tween_TransitionType) ) |

---

### Method Descriptions

<span id="class_MethodTweener_method_set_delay"></span>

[MethodTweener](class_methodtweener.md#class_MethodTweener) **set_delay** ( delay: [float](class_float.md#class_float) ) [🔗](class_methodtweener.md#class_MethodTweener_method_set_delay)

Sets the time in seconds after which the **MethodTweener** will start interpolating. By default there's no delay.

---

<span id="class_MethodTweener_method_set_ease"></span>

[MethodTweener](class_methodtweener.md#class_MethodTweener) **set_ease** ( ease: [EaseType](class_tween.md#enum_Tween_EaseType) ) [🔗](class_methodtweener.md#class_MethodTweener_method_set_ease)

Sets the type of used easing from [EaseType](class_tween.md#enum_Tween_EaseType). If not set, the default easing is used from the [Tween](class_tween.md#class_Tween) that contains this Tweener.

---

<span id="class_MethodTweener_method_set_trans"></span>

[MethodTweener](class_methodtweener.md#class_MethodTweener) **set_trans** ( trans: [TransitionType](class_tween.md#enum_Tween_TransitionType) ) [🔗](class_methodtweener.md#class_MethodTweener_method_set_trans)

Sets the type of used transition from [TransitionType](class_tween.md#enum_Tween_TransitionType). If not set, the default transition is used from the [Tween](class_tween.md#class_Tween) that contains this Tweener.
