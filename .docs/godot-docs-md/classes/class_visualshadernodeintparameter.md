<span id="class_VisualShaderNodeIntParameter"></span>

## VisualShaderNodeIntParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A visual shader node for shader parameter (uniform) of type [int](class_int.md#class_int).

### Description

A [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) of type [int](class_int.md#class_int). Offers additional customization for range of accepted values.

### Properties


| [int](class_int.md#class_int) | [default_value](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_default_value) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [default_value_enabled](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_default_value_enabled) | `false` |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [enum_names](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_enum_names) | `PackedStringArray()` |
| [Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) | [hint](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_hint) | `0` |
| [int](class_int.md#class_int) | [max](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_max) | `100` |
| [int](class_int.md#class_int) | [min](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_min) | `0` |
| [int](class_int.md#class_int) | [step](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_step) | `1` |

---

### Enumerations

<span id="enum_VisualShaderNodeIntParameter_Hint"></span>

enum **Hint**: [🔗](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint)

<span id="class_VisualShaderNodeIntParameter_constant_HINT_NONE"></span>

[Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) **HINT_NONE** = `0`

The parameter will not constrain its value.

<span id="class_VisualShaderNodeIntParameter_constant_HINT_RANGE"></span>

[Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) **HINT_RANGE** = `1`

The parameter's value must be within the specified [min](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_min)/[max](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_max) range.

<span id="class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP"></span>

[Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) **HINT_RANGE_STEP** = `2`

The parameter's value must be within the specified range, with the given [step](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_step) between values.

<span id="class_VisualShaderNodeIntParameter_constant_HINT_ENUM"></span>

[Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) **HINT_ENUM** = `3`

The parameter uses an enum to associate preset values to names in the editor.

<span id="class_VisualShaderNodeIntParameter_constant_HINT_MAX"></span>

[Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) **HINT_MAX** = `4`

Represents the size of the [Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeIntParameter_property_default_value"></span>

[int](class_int.md#class_int) **default_value** = `0` [🔗](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_default_value)

- void **set_default_value** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_default_value** ( )

Default value of this parameter, which will be used if not set externally. [default_value_enabled](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_default_value_enabled) must be enabled; defaults to `0` otherwise.

---

<span id="class_VisualShaderNodeIntParameter_property_default_value_enabled"></span>

[bool](class_bool.md#class_bool) **default_value_enabled** = `false` [🔗](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_default_value_enabled)

- void **set_default_value_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_default_value_enabled** ( )

If `true`, the node will have a custom default value.

---

<span id="class_VisualShaderNodeIntParameter_property_enum_names"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **enum_names** = `PackedStringArray()` [🔗](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_enum_names)

- void **set_enum_names** ( value: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )
- [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_enum_names** ( )

The names used for the enum select in the editor. [hint](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_hint) must be [HINT_ENUM](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_constant_HINT_ENUM) for this to take effect.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

<span id="class_VisualShaderNodeIntParameter_property_hint"></span>

[Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) **hint** = `0` [🔗](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_hint)

- void **set_hint** ( value: [Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) )
- [Hint](class_visualshadernodeintparameter.md#enum_VisualShaderNodeIntParameter_Hint) **get_hint** ( )

Range hint of this node. Use it to customize valid parameter range.

---

<span id="class_VisualShaderNodeIntParameter_property_max"></span>

[int](class_int.md#class_int) **max** = `100` [🔗](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_max)

- void **set_max** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max** ( )

The maximum value this parameter can take. [hint](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_hint) must be either [HINT_RANGE](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_constant_HINT_RANGE) or [HINT_RANGE_STEP](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP) for this to take effect.

---

<span id="class_VisualShaderNodeIntParameter_property_min"></span>

[int](class_int.md#class_int) **min** = `0` [🔗](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_min)

- void **set_min** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_min** ( )

The minimum value this parameter can take. [hint](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_hint) must be either [HINT_RANGE](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_constant_HINT_RANGE) or [HINT_RANGE_STEP](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP) for this to take effect.

---

<span id="class_VisualShaderNodeIntParameter_property_step"></span>

[int](class_int.md#class_int) **step** = `1` [🔗](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_step)

- void **set_step** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_step** ( )

The step between parameter's values. Forces the parameter to be a multiple of the given value. [hint](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_property_hint) must be [HINT_RANGE_STEP](class_visualshadernodeintparameter.md#class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP) for this to take effect.
