<span id="class_OpenXRDpadBindingModifier"></span>

## OpenXRDpadBindingModifier

**Inherits:** [OpenXRIPBindingModifier](class_openxripbindingmodifier.md#class_OpenXRIPBindingModifier) **<** [OpenXRBindingModifier](class_openxrbindingmodifier.md#class_OpenXRBindingModifier) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

The DPad binding modifier converts an axis input to a dpad output.

### Description

The DPad binding modifier converts an axis input to a dpad output, emulating a DPad. New input paths for each dpad direction will be added to the interaction profile. When bound to actions the DPad emulation will be activated. You should **not** combine dpad inputs with normal inputs in the same action set for the same control, this will result in an error being returned when suggested bindings are submitted to OpenXR.

See XR_EXT_dpad_binding for in-depth details.

 **Note:** If the DPad binding modifier extension is enabled, all dpad binding paths will be available in the action map. Adding the modifier to an interaction profile allows you to further customize the behavior.

### Properties


| [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) | [action_set](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_action_set) |
| --- | --- |
| [float](class_float.md#class_float) | [center_region](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_center_region) | `0.1` |
| [String](class_string.md#class_String) | [input_path](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_input_path) | `""` |
| [bool](class_bool.md#class_bool) | [is_sticky](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_is_sticky) | `false` |
| [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) | [off_haptic](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_off_haptic) |
| [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) | [on_haptic](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_on_haptic) |
| [float](class_float.md#class_float) | [threshold](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_threshold) | `0.6` |
| [float](class_float.md#class_float) | [threshold_released](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_threshold_released) | `0.4` |
| [float](class_float.md#class_float) | [wedge_angle](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_wedge_angle) | `1.5707964` |

---

### Property Descriptions

<span id="class_OpenXRDpadBindingModifier_property_action_set"></span>

[OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) **action_set** [🔗](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_action_set)

- void **set_action_set** ( value: [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) )
- [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) **get_action_set** ( )

Action set for which this dpad binding modifier is active.

---

<span id="class_OpenXRDpadBindingModifier_property_center_region"></span>

[float](class_float.md#class_float) **center_region** = `0.1` [🔗](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_center_region)

- void **set_center_region** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_center_region** ( )

Center region in which our center position of our dpad return `true`.

---

<span id="class_OpenXRDpadBindingModifier_property_input_path"></span>

[String](class_string.md#class_String) **input_path** = `""` [🔗](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_input_path)

- void **set_input_path** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_input_path** ( )

Input path for this dpad binding modifier.

---

<span id="class_OpenXRDpadBindingModifier_property_is_sticky"></span>

[bool](class_bool.md#class_bool) **is_sticky** = `false` [🔗](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_is_sticky)

- void **set_is_sticky** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_is_sticky** ( )

If `false`, when the joystick enters a new dpad zone this becomes `true`.

If `true`, when the joystick remains in active dpad zone, this remains `true` even if we overlap with another zone.

---

<span id="class_OpenXRDpadBindingModifier_property_off_haptic"></span>

[OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) **off_haptic** [🔗](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_off_haptic)

- void **set_off_haptic** ( value: [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) )
- [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) **get_off_haptic** ( )

Haptic pulse to emit when the user releases the input.

---

<span id="class_OpenXRDpadBindingModifier_property_on_haptic"></span>

[OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) **on_haptic** [🔗](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_on_haptic)

- void **set_on_haptic** ( value: [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) )
- [OpenXRHapticBase](class_openxrhapticbase.md#class_OpenXRHapticBase) **get_on_haptic** ( )

Haptic pulse to emit when the user presses the input.

---

<span id="class_OpenXRDpadBindingModifier_property_threshold"></span>

[float](class_float.md#class_float) **threshold** = `0.6` [🔗](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_threshold)

- void **set_threshold** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_threshold** ( )

When our input value is equal or larger than this value, our dpad in that direction becomes `true`. It stays `true` until it falls under the [threshold_released](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_threshold_released) value.

---

<span id="class_OpenXRDpadBindingModifier_property_threshold_released"></span>

[float](class_float.md#class_float) **threshold_released** = `0.4` [🔗](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_threshold_released)

- void **set_threshold_released** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_threshold_released** ( )

When our input value falls below this, our output becomes `false`.

---

<span id="class_OpenXRDpadBindingModifier_property_wedge_angle"></span>

[float](class_float.md#class_float) **wedge_angle** = `1.5707964` [🔗](class_openxrdpadbindingmodifier.md#class_OpenXRDpadBindingModifier_property_wedge_angle)

- void **set_wedge_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_wedge_angle** ( )

The angle of each wedge that identifies the 4 directions of the emulated dpad.
