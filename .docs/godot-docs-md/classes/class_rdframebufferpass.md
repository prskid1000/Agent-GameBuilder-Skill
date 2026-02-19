<span id="class_RDFramebufferPass"></span>

## RDFramebufferPass

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Framebuffer pass attachment description (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

This class contains the list of attachment descriptions for a framebuffer pass. Each points with an index to a previously supplied list of texture attachments.

Multipass framebuffers can optimize some configurations in mobile. On desktop, they provide little to no advantage.

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [color_attachments](class_rdframebufferpass.md#class_RDFramebufferPass_property_color_attachments) | `PackedInt32Array()` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [depth_attachment](class_rdframebufferpass.md#class_RDFramebufferPass_property_depth_attachment) | `-1` |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [input_attachments](class_rdframebufferpass.md#class_RDFramebufferPass_property_input_attachments) | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [preserve_attachments](class_rdframebufferpass.md#class_RDFramebufferPass_property_preserve_attachments) | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [resolve_attachments](class_rdframebufferpass.md#class_RDFramebufferPass_property_resolve_attachments) | `PackedInt32Array()` |

---

### Constants

<span id="class_RDFramebufferPass_constant_ATTACHMENT_UNUSED"></span>

**ATTACHMENT_UNUSED** = `-1` [🔗](class_rdframebufferpass.md#class_RDFramebufferPass_constant_ATTACHMENT_UNUSED)

Attachment is unused.

---

### Property Descriptions

<span id="class_RDFramebufferPass_property_color_attachments"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **color_attachments** = `PackedInt32Array()` [🔗](class_rdframebufferpass.md#class_RDFramebufferPass_property_color_attachments)

- void **set_color_attachments** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_color_attachments** ( )

Color attachments in order starting from 0. If this attachment is not used by the shader, pass ATTACHMENT_UNUSED to skip.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_RDFramebufferPass_property_depth_attachment"></span>

[int](class_int.md#class_int) **depth_attachment** = `-1` [🔗](class_rdframebufferpass.md#class_RDFramebufferPass_property_depth_attachment)

- void **set_depth_attachment** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_depth_attachment** ( )

Depth attachment. ATTACHMENT_UNUSED should be used if no depth buffer is required for this pass.

---

<span id="class_RDFramebufferPass_property_input_attachments"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **input_attachments** = `PackedInt32Array()` [🔗](class_rdframebufferpass.md#class_RDFramebufferPass_property_input_attachments)

- void **set_input_attachments** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_input_attachments** ( )

Used for multipass framebuffers (more than one render pass). Converts an attachment to an input. Make sure to also supply it properly in the [RDUniform](class_rduniform.md#class_RDUniform) for the uniform set.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_RDFramebufferPass_property_preserve_attachments"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **preserve_attachments** = `PackedInt32Array()` [🔗](class_rdframebufferpass.md#class_RDFramebufferPass_property_preserve_attachments)

- void **set_preserve_attachments** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_preserve_attachments** ( )

Attachments to preserve in this pass (otherwise they are erased).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_RDFramebufferPass_property_resolve_attachments"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **resolve_attachments** = `PackedInt32Array()` [🔗](class_rdframebufferpass.md#class_RDFramebufferPass_property_resolve_attachments)

- void **set_resolve_attachments** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_resolve_attachments** ( )

If the color attachments are multisampled, non-multisampled resolve attachments can be provided.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.
