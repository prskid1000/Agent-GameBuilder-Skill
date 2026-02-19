<span id="class_OpenXRAndroidThreadSettingsExtension"></span>

## OpenXRAndroidThreadSettingsExtension

**Inherits:** [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) **<** [Object](class_object.md#class_Object)

Wraps the XR_KHR_android_thread_settings extension.

### Description

For XR to be comfortable, it is important for applications to deliver frames quickly and consistently. In order to make sure the important application threads get their full share of time, these threads must be identified to the system, which will adjust their scheduling priority accordingly.

### Methods


| [bool](class_bool.md#class_bool) | [set_application_thread_type](class_openxrandroidthreadsettingsextension.md#class_OpenXRAndroidThreadSettingsExtension_method_set_application_thread_type) ( thread_type: [ThreadType](class_openxrandroidthreadsettingsextension.md#enum_OpenXRAndroidThreadSettingsExtension_ThreadType), thread_id: [int](class_int.md#class_int) = 0 ) |
| --- | --- |

---

### Enumerations

<span id="enum_OpenXRAndroidThreadSettingsExtension_ThreadType"></span>

enum **ThreadType**: [🔗](class_openxrandroidthreadsettingsextension.md#enum_OpenXRAndroidThreadSettingsExtension_ThreadType)

<span id="class_OpenXRAndroidThreadSettingsExtension_constant_THREAD_TYPE_APPLICATION_MAIN"></span>

[ThreadType](class_openxrandroidthreadsettingsextension.md#enum_OpenXRAndroidThreadSettingsExtension_ThreadType) **THREAD_TYPE_APPLICATION_MAIN** = `0`

Hints to the XR runtime that the thread is doing time critical CPU tasks.

<span id="class_OpenXRAndroidThreadSettingsExtension_constant_THREAD_TYPE_APPLICATION_WORKER"></span>

[ThreadType](class_openxrandroidthreadsettingsextension.md#enum_OpenXRAndroidThreadSettingsExtension_ThreadType) **THREAD_TYPE_APPLICATION_WORKER** = `1`

Hints to the XR runtime that the thread is doing background CPU tasks.

<span id="class_OpenXRAndroidThreadSettingsExtension_constant_THREAD_TYPE_RENDERER_MAIN"></span>

[ThreadType](class_openxrandroidthreadsettingsextension.md#enum_OpenXRAndroidThreadSettingsExtension_ThreadType) **THREAD_TYPE_RENDERER_MAIN** = `2`

Hints to the XR runtime that the thread is doing time critical graphics device tasks.

<span id="class_OpenXRAndroidThreadSettingsExtension_constant_THREAD_TYPE_RENDERER_WORKER"></span>

[ThreadType](class_openxrandroidthreadsettingsextension.md#enum_OpenXRAndroidThreadSettingsExtension_ThreadType) **THREAD_TYPE_RENDERER_WORKER** = `3`

Hints to the XR runtime that the thread is doing background graphics device tasks.

---

### Method Descriptions

<span id="class_OpenXRAndroidThreadSettingsExtension_method_set_application_thread_type"></span>

[bool](class_bool.md#class_bool) **set_application_thread_type** ( thread_type: [ThreadType](class_openxrandroidthreadsettingsextension.md#enum_OpenXRAndroidThreadSettingsExtension_ThreadType), thread_id: [int](class_int.md#class_int) = 0 ) [🔗](class_openxrandroidthreadsettingsextension.md#class_OpenXRAndroidThreadSettingsExtension_method_set_application_thread_type)

Sets the thread type of the given thread, so that the XR runtime can adjust its scheduling priority accordingly.

 `thread_id` refers to the OS thread id (ie from `gettid()`). When `thread_id` is `0`, it will set the thread type of the current thread.

 **NOTE:** The id returned by [Thread.get_id()](class_thread.md#class_Thread_method_get_id) is incompatible with `thread_id`.
