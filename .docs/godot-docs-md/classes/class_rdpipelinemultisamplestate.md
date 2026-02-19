<span id="class_RDPipelineMultisampleState"></span>

## RDPipelineMultisampleState

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Pipeline multisample state (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

**RDPipelineMultisampleState** is used to control how multisample or supersample antialiasing is being performed when rendering using [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [bool](class_bool.md#class_bool) | [enable_alpha_to_coverage](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_alpha_to_coverage) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [enable_alpha_to_one](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_alpha_to_one) | `false` |
| [bool](class_bool.md#class_bool) | [enable_sample_shading](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_sample_shading) | `false` |
| [float](class_float.md#class_float) | [min_sample_shading](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_min_sample_shading) | `0.0` |
| [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) | [sample_count](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_sample_count) | `0` |
| [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] | [sample_masks](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_sample_masks) | `[]` |

---

### Property Descriptions

<span id="class_RDPipelineMultisampleState_property_enable_alpha_to_coverage"></span>

[bool](class_bool.md#class_bool) **enable_alpha_to_coverage** = `false` [🔗](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_alpha_to_coverage)

- void **set_enable_alpha_to_coverage** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_alpha_to_coverage** ( )

If `true`, alpha to coverage is enabled. This generates a temporary coverage value based on the alpha component of the fragment's first color output. This allows alpha transparency to make use of multisample antialiasing.

---

<span id="class_RDPipelineMultisampleState_property_enable_alpha_to_one"></span>

[bool](class_bool.md#class_bool) **enable_alpha_to_one** = `false` [🔗](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_alpha_to_one)

- void **set_enable_alpha_to_one** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_alpha_to_one** ( )

If `true`, alpha is forced to either `0.0` or `1.0`. This allows hardening the edges of antialiased alpha transparencies. Only relevant if [enable_alpha_to_coverage](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_alpha_to_coverage) is `true`.

---

<span id="class_RDPipelineMultisampleState_property_enable_sample_shading"></span>

[bool](class_bool.md#class_bool) **enable_sample_shading** = `false` [🔗](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_sample_shading)

- void **set_enable_sample_shading** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_sample_shading** ( )

If `true`, enables per-sample shading which replaces MSAA by SSAA. This provides higher quality antialiasing that works with transparent (alpha scissor) edges. This has a very high performance cost. See also [min_sample_shading](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_min_sample_shading). See the per-sample shading Vulkan documentation for more details.

---

<span id="class_RDPipelineMultisampleState_property_min_sample_shading"></span>

[float](class_float.md#class_float) **min_sample_shading** = `0.0` [🔗](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_min_sample_shading)

- void **set_min_sample_shading** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_min_sample_shading** ( )

The multiplier of [sample_count](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_sample_count) that determines how many samples are performed for each fragment. Must be between `0.0` and `1.0` (inclusive). Only effective if [enable_sample_shading](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_sample_shading) is `true`. If [min_sample_shading](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_min_sample_shading) is `1.0`, fragment invocation must only read from the coverage index sample. Tile image access must not be used if [enable_sample_shading](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_sample_shading) is *not* `1.0`.

---

<span id="class_RDPipelineMultisampleState_property_sample_count"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **sample_count** = `0` [🔗](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_sample_count)

- void **set_sample_count** ( value: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) )
- [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **get_sample_count** ( )

The number of MSAA samples (or SSAA samples if [enable_sample_shading](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_enable_sample_shading) is `true`) to perform. Higher values result in better antialiasing, at the cost of performance.

---

<span id="class_RDPipelineMultisampleState_property_sample_masks"></span>

[Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] **sample_masks** = `[]` [🔗](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState_property_sample_masks)

- void **set_sample_masks** ( value: [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] )
- [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] **get_sample_masks** ( )

The sample mask array. See the sample mask Vulkan documentation for more details.
