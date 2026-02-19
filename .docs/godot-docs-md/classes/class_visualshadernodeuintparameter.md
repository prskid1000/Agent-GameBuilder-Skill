<span id="class_VisualShaderNodeUIntParameter"></span>

## VisualShaderNodeUIntParameter

**Inherits:** [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A visual shader node for shader parameter (uniform) of type unsigned [int](class_int.md#class_int).

### Description

A [VisualShaderNodeParameter](class_visualshadernodeparameter.md#class_VisualShaderNodeParameter) of type unsigned [int](class_int.md#class_int). Offers additional customization for range of accepted values.

### Properties


| [int](class_int.md#class_int) | [default_value](class_visualshadernodeuintparameter.md#class_VisualShaderNodeUIntParameter_property_default_value) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [default_value_enabled](class_visualshadernodeuintparameter.md#class_VisualShaderNodeUIntParameter_property_default_value_enabled) | `false` |

---

### Property Descriptions

<span id="class_VisualShaderNodeUIntParameter_property_default_value"></span>

[int](class_int.md#class_int) **default_value** = `0` [🔗](class_visualshadernodeuintparameter.md#class_VisualShaderNodeUIntParameter_property_default_value)

- void **set_default_value** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_default_value** ( )

Default value of this parameter, which will be used if not set externally. [default_value_enabled](class_visualshadernodeuintparameter.md#class_VisualShaderNodeUIntParameter_property_default_value_enabled) must be enabled; defaults to `0` otherwise.

---

<span id="class_VisualShaderNodeUIntParameter_property_default_value_enabled"></span>

[bool](class_bool.md#class_bool) **default_value_enabled** = `false` [🔗](class_visualshadernodeuintparameter.md#class_VisualShaderNodeUIntParameter_property_default_value_enabled)

- void **set_default_value_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_default_value_enabled** ( )

If `true`, the node will have a custom default value.
