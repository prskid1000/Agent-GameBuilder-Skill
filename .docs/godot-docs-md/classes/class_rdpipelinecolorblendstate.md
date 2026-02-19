<span id="class_RDPipelineColorBlendState"></span>

## RDPipelineColorBlendState

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Pipeline color blend state (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [Array](class_array.md#class_Array)\[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment)\] | [attachments](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_attachments) | `[]` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [blend_constant](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_blend_constant) | `Color(0, 0, 0, 1)` |
| [bool](class_bool.md#class_bool) | [enable_logic_op](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_enable_logic_op) | `false` |
| [LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) | [logic_op](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_logic_op) | `0` |

---

### Property Descriptions

<span id="class_RDPipelineColorBlendState_property_attachments"></span>

[Array](class_array.md#class_Array)\[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment)\] **attachments** = `[]` [🔗](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_attachments)

- void **set_attachments** ( value: [Array](class_array.md#class_Array)\[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment)\] )
- [Array](class_array.md#class_Array)\[[RDPipelineColorBlendStateAttachment](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment)\] **get_attachments** ( )

The attachments that are blended together.

---

<span id="class_RDPipelineColorBlendState_property_blend_constant"></span>

[Color](class_color.md#class_Color) **blend_constant** = `Color(0, 0, 0, 1)` [🔗](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_blend_constant)

- void **set_blend_constant** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_blend_constant** ( )

The constant color to blend with. See also [RenderingDevice.draw_list_set_blend_constants()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_set_blend_constants).

---

<span id="class_RDPipelineColorBlendState_property_enable_logic_op"></span>

[bool](class_bool.md#class_bool) **enable_logic_op** = `false` [🔗](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_enable_logic_op)

- void **set_enable_logic_op** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_logic_op** ( )

If `true`, performs the logic operation defined in [logic_op](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_logic_op).

---

<span id="class_RDPipelineColorBlendState_property_logic_op"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **logic_op** = `0` [🔗](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_logic_op)

- void **set_logic_op** ( value: [LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) )
- [LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **get_logic_op** ( )

The logic operation to perform for blending. Only effective if [enable_logic_op](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState_property_enable_logic_op) is `true`.
