<span id="class_OpenXRHapticVibration"></span>

## OpenXRHapticVibration

**Inherits:** [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Vibration haptic feedback.

### Description

This haptic feedback resource makes it possible to define a vibration based haptic feedback pulse that can be triggered through actions in the OpenXR action map.

### Properties


| [float](class_float.md#class_float) | [amplitude](class_openxrhapticvibration.md#class_OpenXRHapticVibration_property_amplitude) | `1.0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [duration](class_openxrhapticvibration.md#class_OpenXRHapticVibration_property_duration) | `-1` |
| [float](class_float.md#class_float) | [frequency](class_openxrhapticvibration.md#class_OpenXRHapticVibration_property_frequency) | `0.0` |

---

### Property Descriptions

<span id="class_OpenXRHapticVibration_property_amplitude"></span>

[float](class_float.md#class_float) **amplitude** = `1.0` [🔗](class_openxrhapticvibration.md#class_OpenXRHapticVibration_property_amplitude)

- void **set_amplitude** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_amplitude** ( )

The amplitude of the pulse between `0.0` and `1.0`.

---

<span id="class_OpenXRHapticVibration_property_duration"></span>

[int](class_int.md#class_int) **duration** = `-1` [🔗](class_openxrhapticvibration.md#class_OpenXRHapticVibration_property_duration)

- void **set_duration** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_duration** ( )

The duration of the pulse in nanoseconds. Use `-1` for a minimum duration pulse for the current XR runtime.

---

<span id="class_OpenXRHapticVibration_property_frequency"></span>

[float](class_float.md#class_float) **frequency** = `0.0` [🔗](class_openxrhapticvibration.md#class_OpenXRHapticVibration_property_frequency)

- void **set_frequency** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_frequency** ( )

The frequency of the pulse in Hz. `0.0` will let the XR runtime chose an optimal frequency for the device used.
