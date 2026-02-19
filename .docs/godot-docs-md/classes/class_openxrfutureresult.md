<span id="class_OpenXRFutureResult"></span>

## OpenXRFutureResult

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Result object tracking the asynchronous result of an OpenXR Future object.

### Description

Result object tracking the asynchronous result of an OpenXR Future object, you can use this object to track the result status.

### Methods


| void | [cancel_future](class_openxrfutureresult.md#class_OpenXRFutureResult_method_cancel_future) ( ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_future](class_openxrfutureresult.md#class_OpenXRFutureResult_method_get_future) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_result_value](class_openxrfutureresult.md#class_OpenXRFutureResult_method_get_result_value) ( ) const |
| [ResultStatus](class_openxrfutureresult.md#enum_OpenXRFutureResult_ResultStatus) | [get_status](class_openxrfutureresult.md#class_OpenXRFutureResult_method_get_status) ( ) const |
| void | [set_result_value](class_openxrfutureresult.md#class_OpenXRFutureResult_method_set_result_value) ( result_value: [Variant](class_variant.md#class_Variant) ) |

---

### Signals

<span id="class_OpenXRFutureResult_signal_completed"></span>

**completed** ( result: [OpenXRFutureResult](class_openxrfutureresult.md#class_OpenXRFutureResult) ) [🔗](class_openxrfutureresult.md#class_OpenXRFutureResult_signal_completed)

Emitted when the asynchronous function is finished or has been cancelled.

---

### Enumerations

<span id="enum_OpenXRFutureResult_ResultStatus"></span>

enum **ResultStatus**: [🔗](class_openxrfutureresult.md#enum_OpenXRFutureResult_ResultStatus)

<span id="class_OpenXRFutureResult_constant_RESULT_RUNNING"></span>

[ResultStatus](class_openxrfutureresult.md#enum_OpenXRFutureResult_ResultStatus) **RESULT_RUNNING** = `0`

The asynchronous function is running.

<span id="class_OpenXRFutureResult_constant_RESULT_FINISHED"></span>

[ResultStatus](class_openxrfutureresult.md#enum_OpenXRFutureResult_ResultStatus) **RESULT_FINISHED** = `1`

The asynchronous function has finished.

<span id="class_OpenXRFutureResult_constant_RESULT_CANCELLED"></span>

[ResultStatus](class_openxrfutureresult.md#enum_OpenXRFutureResult_ResultStatus) **RESULT_CANCELLED** = `2`

The asynchronous function has been cancelled.

---

### Method Descriptions

<span id="class_OpenXRFutureResult_method_cancel_future"></span>

void **cancel_future** ( ) [🔗](class_openxrfutureresult.md#class_OpenXRFutureResult_method_cancel_future)

Cancel this future, this will interrupt and stop the asynchronous function.

---

<span id="class_OpenXRFutureResult_method_get_future"></span>

[int](class_int.md#class_int) **get_future** ( ) *const* [🔗](class_openxrfutureresult.md#class_OpenXRFutureResult_method_get_future)

Return the `XrFutureEXT` value this result relates to.

---

<span id="class_OpenXRFutureResult_method_get_result_value"></span>

[Variant](class_variant.md#class_Variant) **get_result_value** ( ) *const* [🔗](class_openxrfutureresult.md#class_OpenXRFutureResult_method_get_result_value)

Returns the result value of our asynchronous function (if set by the extension). The type of this result value depends on the function being called. Consult the documentation of the relevant function.

---

<span id="class_OpenXRFutureResult_method_get_status"></span>

[ResultStatus](class_openxrfutureresult.md#enum_OpenXRFutureResult_ResultStatus) **get_status** ( ) *const* [🔗](class_openxrfutureresult.md#class_OpenXRFutureResult_method_get_status)

Returns the status of this result.

---

<span id="class_OpenXRFutureResult_method_set_result_value"></span>

void **set_result_value** ( result_value: [Variant](class_variant.md#class_Variant) ) [🔗](class_openxrfutureresult.md#class_OpenXRFutureResult_method_set_result_value)

Stores the result value we expose to the user.

 **Note:** This method should only be called by an OpenXR extension that implements an asynchronous function.
