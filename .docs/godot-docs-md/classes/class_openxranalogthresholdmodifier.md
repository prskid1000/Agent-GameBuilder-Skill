<span id="class_OpenXRAnalogThresholdModifier"></span>

## OpenXRAnalogThresholdModifier

**Inherits:** [OpenXRActionBindingModifier](class_openxractionbindingmodifier.md#class_OpenXRActionBindingModifier) **<** [OpenXRBindingModifier](class_openxrbindingmodifier.md#class_OpenXRBindingModifier) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

### Description

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

See XR_VALVE_analog_threshold for in-depth details.

### Properties


| [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) | [off_haptic](class_openxranalogthresholdmodifier.md#class_OpenXRAnalogThresholdModifier_property_off_haptic) |
| --- | --- |
| [float](class_float.md#class_float) | [off_threshold](class_openxranalogthresholdmodifier.md#class_OpenXRAnalogThresholdModifier_property_off_threshold) | `0.4` |
| [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) | [on_haptic](class_openxranalogthresholdmodifier.md#class_OpenXRAnalogThresholdModifier_property_on_haptic) |
| [float](class_float.md#class_float) | [on_threshold](class_openxranalogthresholdmodifier.md#class_OpenXRAnalogThresholdModifier_property_on_threshold) | `0.6` |

---

### Property Descriptions

<span id="class_OpenXRAnalogThresholdModifier_property_off_haptic"></span>

[OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) **off_haptic** [🔗](class_openxranalogthresholdmodifier.md#class_OpenXRAnalogThresholdModifier_property_off_haptic)

- void **set_off_haptic** ( value: [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) )
- [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) **get_off_haptic** ( )

Haptic pulse to emit when the user releases the input.

---

<span id="class_OpenXRAnalogThresholdModifier_property_off_threshold"></span>

[float](class_float.md#class_float) **off_threshold** = `0.4` [🔗](class_openxranalogthresholdmodifier.md#class_OpenXRAnalogThresholdModifier_property_off_threshold)

- void **set_off_threshold** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_off_threshold** ( )

When our input value falls below this, our output becomes `false`.

---

<span id="class_OpenXRAnalogThresholdModifier_property_on_haptic"></span>

[OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) **on_haptic** [🔗](class_openxranalogthresholdmodifier.md#class_OpenXRAnalogThresholdModifier_property_on_haptic)

- void **set_on_haptic** ( value: [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) )
- [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) **get_on_haptic** ( )

Haptic pulse to emit when the user presses the input.

---

<span id="class_OpenXRAnalogThresholdModifier_property_on_threshold"></span>

[float](class_float.md#class_float) **on_threshold** = `0.6` [🔗](class_openxranalogthresholdmodifier.md#class_OpenXRAnalogThresholdModifier_property_on_threshold)

- void **set_on_threshold** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_on_threshold** ( )

When our input value is equal or larger than this value, our output becomes `true`. It stays `true` until it falls under the [off_threshold](class_openxranalogthresholdmodifier.md#class_OpenXRAnalogThresholdModifier_property_off_threshold) value.
