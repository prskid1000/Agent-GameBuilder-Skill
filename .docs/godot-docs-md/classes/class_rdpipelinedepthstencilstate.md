<span id="class_RDPipelineDepthStencilState"></span>

## RDPipelineDepthStencilState

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Pipeline depth/stencil state (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

**RDPipelineDepthStencilState** controls the way depth and stencil comparisons are performed when sampling those values using [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) | [back_op_compare](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_compare) | `7` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [back_op_compare_mask](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_compare_mask) | `0` |
| [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) | [back_op_depth_fail](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_depth_fail) | `1` |
| [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) | [back_op_fail](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_fail) | `1` |
| [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) | [back_op_pass](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_pass) | `1` |
| [int](class_int.md#class_int) | [back_op_reference](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_reference) | `0` |
| [int](class_int.md#class_int) | [back_op_write_mask](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_write_mask) | `0` |
| [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) | [depth_compare_operator](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_depth_compare_operator) | `7` |
| [float](class_float.md#class_float) | [depth_range_max](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_depth_range_max) | `0.0` |
| [float](class_float.md#class_float) | [depth_range_min](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_depth_range_min) | `0.0` |
| [bool](class_bool.md#class_bool) | [enable_depth_range](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_depth_range) | `false` |
| [bool](class_bool.md#class_bool) | [enable_depth_test](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_depth_test) | `false` |
| [bool](class_bool.md#class_bool) | [enable_depth_write](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_depth_write) | `false` |
| [bool](class_bool.md#class_bool) | [enable_stencil](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_stencil) | `false` |
| [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) | [front_op_compare](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_compare) | `7` |
| [int](class_int.md#class_int) | [front_op_compare_mask](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_compare_mask) | `0` |
| [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) | [front_op_depth_fail](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_depth_fail) | `1` |
| [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) | [front_op_fail](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_fail) | `1` |
| [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) | [front_op_pass](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_pass) | `1` |
| [int](class_int.md#class_int) | [front_op_reference](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_reference) | `0` |
| [int](class_int.md#class_int) | [front_op_write_mask](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_write_mask) | `0` |

---

### Property Descriptions

<span id="class_RDPipelineDepthStencilState_property_back_op_compare"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **back_op_compare** = `7` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_compare)

- void **set_back_op_compare** ( value: [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) )
- [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **get_back_op_compare** ( )

The method used for comparing the previous back stencil value and [back_op_reference](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_reference).

---

<span id="class_RDPipelineDepthStencilState_property_back_op_compare_mask"></span>

[int](class_int.md#class_int) **back_op_compare_mask** = `0` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_compare_mask)

- void **set_back_op_compare_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_back_op_compare_mask** ( )

Selects which bits from the back stencil value will be compared.

---

<span id="class_RDPipelineDepthStencilState_property_back_op_depth_fail"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **back_op_depth_fail** = `1` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_depth_fail)

- void **set_back_op_depth_fail** ( value: [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) )
- [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **get_back_op_depth_fail** ( )

The operation to perform on the stencil buffer for back pixels that pass the stencil test but fail the depth test.

---

<span id="class_RDPipelineDepthStencilState_property_back_op_fail"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **back_op_fail** = `1` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_fail)

- void **set_back_op_fail** ( value: [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) )
- [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **get_back_op_fail** ( )

The operation to perform on the stencil buffer for back pixels that fail the stencil test.

---

<span id="class_RDPipelineDepthStencilState_property_back_op_pass"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **back_op_pass** = `1` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_pass)

- void **set_back_op_pass** ( value: [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) )
- [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **get_back_op_pass** ( )

The operation to perform on the stencil buffer for back pixels that pass the stencil test.

---

<span id="class_RDPipelineDepthStencilState_property_back_op_reference"></span>

[int](class_int.md#class_int) **back_op_reference** = `0` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_reference)

- void **set_back_op_reference** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_back_op_reference** ( )

The value the previous back stencil value will be compared to.

---

<span id="class_RDPipelineDepthStencilState_property_back_op_write_mask"></span>

[int](class_int.md#class_int) **back_op_write_mask** = `0` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_back_op_write_mask)

- void **set_back_op_write_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_back_op_write_mask** ( )

Selects which bits from the back stencil value will be changed.

---

<span id="class_RDPipelineDepthStencilState_property_depth_compare_operator"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **depth_compare_operator** = `7` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_depth_compare_operator)

- void **set_depth_compare_operator** ( value: [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) )
- [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **get_depth_compare_operator** ( )

The method used for comparing the previous and current depth values.

---

<span id="class_RDPipelineDepthStencilState_property_depth_range_max"></span>

[float](class_float.md#class_float) **depth_range_max** = `0.0` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_depth_range_max)

- void **set_depth_range_max** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth_range_max** ( )

The maximum depth that returns `true` for [enable_depth_range](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_depth_range).

---

<span id="class_RDPipelineDepthStencilState_property_depth_range_min"></span>

[float](class_float.md#class_float) **depth_range_min** = `0.0` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_depth_range_min)

- void **set_depth_range_min** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth_range_min** ( )

The minimum depth that returns `true` for [enable_depth_range](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_depth_range).

---

<span id="class_RDPipelineDepthStencilState_property_enable_depth_range"></span>

[bool](class_bool.md#class_bool) **enable_depth_range** = `false` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_depth_range)

- void **set_enable_depth_range** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_depth_range** ( )

If `true`, each depth value will be tested to see if it is between [depth_range_min](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_depth_range_min) and [depth_range_max](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_depth_range_max). If it is outside of these values, it is discarded.

---

<span id="class_RDPipelineDepthStencilState_property_enable_depth_test"></span>

[bool](class_bool.md#class_bool) **enable_depth_test** = `false` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_depth_test)

- void **set_enable_depth_test** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_depth_test** ( )

If `true`, enables depth testing which allows objects to be automatically occluded by other objects based on their depth. This also allows objects to be partially occluded by other objects. If `false`, objects will appear in the order they were drawn (like in Godot's 2D renderer).

---

<span id="class_RDPipelineDepthStencilState_property_enable_depth_write"></span>

[bool](class_bool.md#class_bool) **enable_depth_write** = `false` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_depth_write)

- void **set_enable_depth_write** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_depth_write** ( )

If `true`, writes to the depth buffer whenever the depth test returns `true`. Only works when enable_depth_test is also `true`.

---

<span id="class_RDPipelineDepthStencilState_property_enable_stencil"></span>

[bool](class_bool.md#class_bool) **enable_stencil** = `false` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_enable_stencil)

- void **set_enable_stencil** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_stencil** ( )

If `true`, enables stencil testing. There are separate stencil buffers for front-facing triangles and back-facing triangles. See properties that begin with "front_op" and properties with "back_op" for each.

---

<span id="class_RDPipelineDepthStencilState_property_front_op_compare"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **front_op_compare** = `7` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_compare)

- void **set_front_op_compare** ( value: [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) )
- [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **get_front_op_compare** ( )

The method used for comparing the previous front stencil value and [front_op_reference](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_reference).

---

<span id="class_RDPipelineDepthStencilState_property_front_op_compare_mask"></span>

[int](class_int.md#class_int) **front_op_compare_mask** = `0` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_compare_mask)

- void **set_front_op_compare_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_front_op_compare_mask** ( )

Selects which bits from the front stencil value will be compared.

---

<span id="class_RDPipelineDepthStencilState_property_front_op_depth_fail"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **front_op_depth_fail** = `1` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_depth_fail)

- void **set_front_op_depth_fail** ( value: [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) )
- [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **get_front_op_depth_fail** ( )

The operation to perform on the stencil buffer for front pixels that pass the stencil test but fail the depth test.

---

<span id="class_RDPipelineDepthStencilState_property_front_op_fail"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **front_op_fail** = `1` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_fail)

- void **set_front_op_fail** ( value: [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) )
- [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **get_front_op_fail** ( )

The operation to perform on the stencil buffer for front pixels that fail the stencil test.

---

<span id="class_RDPipelineDepthStencilState_property_front_op_pass"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **front_op_pass** = `1` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_pass)

- void **set_front_op_pass** ( value: [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) )
- [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **get_front_op_pass** ( )

The operation to perform on the stencil buffer for front pixels that pass the stencil test.

---

<span id="class_RDPipelineDepthStencilState_property_front_op_reference"></span>

[int](class_int.md#class_int) **front_op_reference** = `0` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_reference)

- void **set_front_op_reference** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_front_op_reference** ( )

The value the previous front stencil value will be compared to.

---

<span id="class_RDPipelineDepthStencilState_property_front_op_write_mask"></span>

[int](class_int.md#class_int) **front_op_write_mask** = `0` [🔗](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState_property_front_op_write_mask)

- void **set_front_op_write_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_front_op_write_mask** ( )

Selects which bits from the front stencil value will be changed.
