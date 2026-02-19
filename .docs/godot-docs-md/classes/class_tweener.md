<span id="class_Tweener"></span>

## Tweener

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CallbackTweener](class_callbacktweener.md#class_CallbackTweener), [IntervalTweener](class_intervaltweener.md#class_IntervalTweener), [MethodTweener](class_methodtweener.md#class_MethodTweener), [PropertyTweener](class_propertytweener.md#class_PropertyTweener), [SubtweenTweener](class_subtweentweener.md#class_SubtweenTweener)

Abstract class for all Tweeners used by [Tween](class_tween.md#class_Tween).

### Description

Tweeners are objects that perform a specific animating task, e.g. interpolating a property or calling a method at a given time. A **Tweener** can't be created manually, you need to use a dedicated method from [Tween](class_tween.md#class_Tween).

---

### Signals

<span id="class_Tweener_signal_finished"></span>

**finished** ( ) [🔗](class_tweener.md#class_Tweener_signal_finished)

Emitted when the **Tweener** has just finished its job or became invalid (e.g. due to a freed object).
