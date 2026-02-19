<span id="class_VisualShaderNodeFloatParameter"></span>

## VisualShaderNodeFloatParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A scalar float parameter to be used within the visual shader graph.

### Description

Translated to `uniform float` in the shader language.

### Properties


| [float](class_float.md#class_float) | [default_value](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_default_value) | `0.0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [default_value_enabled](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_default_value_enabled) | `false` |
| [Hint](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint) | [hint](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_hint) | `0` |
| [float](class_float.md#class_float) | [max](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_max) | `1.0` |
| [float](class_float.md#class_float) | [min](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_min) | `0.0` |
| [float](class_float.md#class_float) | [step](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_step) | `0.1` |

---

### Enumerations

<span id="enum_VisualShaderNodeFloatParameter_Hint"></span>

enum **Hint**: [🔗](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint)

<span id="class_VisualShaderNodeFloatParameter_constant_HINT_NONE"></span>

[Hint](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint) **HINT_NONE** = `0`

No hint used.

<span id="class_VisualShaderNodeFloatParameter_constant_HINT_RANGE"></span>

[Hint](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint) **HINT_RANGE** = `1`

A range hint for scalar value, which limits possible input values between [min](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_min) and [max](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_max). Translated to `hint_range(min, max)` in shader code.

<span id="class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP"></span>

[Hint](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint) **HINT_RANGE_STEP** = `2`

A range hint for scalar value with step, which limits possible input values between [min](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_min) and [max](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_max), with a step (increment) of [step](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_step)). Translated to `hint_range(min, max, step)` in shader code.

<span id="class_VisualShaderNodeFloatParameter_constant_HINT_MAX"></span>

[Hint](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint) **HINT_MAX** = `3`

Represents the size of the [Hint](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeFloatParameter_property_default_value"></span>

[float](class_float.md#class_float) **default_value** = `0.0` [🔗](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_default_value)

- void **set_default_value** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_default_value** ( )

A default value to be assigned within the shader.

---

<span id="class_VisualShaderNodeFloatParameter_property_default_value_enabled"></span>

[bool](class_bool.md#class_bool) **default_value_enabled** = `false` [🔗](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_default_value_enabled)

- void **set_default_value_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_default_value_enabled** ( )

Enables usage of the [default_value](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_default_value).

---

<span id="class_VisualShaderNodeFloatParameter_property_hint"></span>

[Hint](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint) **hint** = `0` [🔗](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_hint)

- void **set_hint** ( value: [Hint](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint) )
- [Hint](class_visualshadernodefloatparameter.md#enum_VisualShaderNodeFloatParameter_Hint) **get_hint** ( )

A hint applied to the uniform, which controls the values it can take when set through the Inspector.

---

<span id="class_VisualShaderNodeFloatParameter_property_max"></span>

[float](class_float.md#class_float) **max** = `1.0` [🔗](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_max)

- void **set_max** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max** ( )

Minimum value for range hints. Used if [hint](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_hint) is set to [HINT_RANGE](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_constant_HINT_RANGE) or [HINT_RANGE_STEP](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP).

---

<span id="class_VisualShaderNodeFloatParameter_property_min"></span>

[float](class_float.md#class_float) **min** = `0.0` [🔗](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_min)

- void **set_min** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_min** ( )

Maximum value for range hints. Used if [hint](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_hint) is set to [HINT_RANGE](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_constant_HINT_RANGE) or [HINT_RANGE_STEP](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP).

---

<span id="class_VisualShaderNodeFloatParameter_property_step"></span>

[float](class_float.md#class_float) **step** = `0.1` [🔗](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_step)

- void **set_step** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_step** ( )

Step (increment) value for the range hint with step. Used if [hint](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_property_hint) is set to [HINT_RANGE_STEP](class_visualshadernodefloatparameter.md#class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP).
