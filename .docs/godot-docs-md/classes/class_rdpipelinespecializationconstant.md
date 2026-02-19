<span id="class_RDPipelineSpecializationConstant"></span>

## RDPipelineSpecializationConstant

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Pipeline specialization constant (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

A *specialization constant* is a way to create additional variants of shaders without actually increasing the number of shader versions that are compiled. This allows improving performance by reducing the number of shader versions and reducing `if` branching, while still allowing shaders to be flexible for different use cases.

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [int](class_int.md#class_int) | [constant_id](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant_property_constant_id) | `0` |
| --- | --- | --- |
| [Variant](class_variant.md#class_Variant) | [value](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant_property_value) |

---

### Property Descriptions

<span id="class_RDPipelineSpecializationConstant_property_constant_id"></span>

[int](class_int.md#class_int) **constant_id** = `0` [🔗](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant_property_constant_id)

- void **set_constant_id** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_constant_id** ( )

The identifier of the specialization constant. This is a value starting from `0` and that increments for every different specialization constant for a given shader.

---

<span id="class_RDPipelineSpecializationConstant_property_value"></span>

[Variant](class_variant.md#class_Variant) **value** [🔗](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant_property_value)

- void **set_value** ( value: [Variant](class_variant.md#class_Variant) )
- [Variant](class_variant.md#class_Variant) **get_value** ( )

The specialization constant's value. Only [bool](class_bool.md#class_bool), [int](class_int.md#class_int) and [float](class_float.md#class_float) types are valid for specialization constants.
