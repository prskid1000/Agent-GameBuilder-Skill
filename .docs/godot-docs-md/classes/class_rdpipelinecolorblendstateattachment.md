<span id="class_RDPipelineColorBlendStateAttachment"></span>

## RDPipelineColorBlendStateAttachment

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Pipeline color blend state attachment (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

Controls how blending between source and destination fragments is performed when using [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

For reference, this is how common user-facing blend modes are implemented in Godot's 2D renderer:

 **Mix:**

::

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA

 **Add:**

::

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE

 **Subtract:**

::

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_REVERSE_SUBTRACT
    attachment.color_blend_op = RenderingDevice.BLEND_OP_REVERSE_SUBTRACT
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE

 **Multiply:**

::

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_DST_COLOR
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ZERO
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_DST_ALPHA
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ZERO

 **Pre-multiplied alpha:**

::

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA

### Properties


| [BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) | [alpha_blend_op](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_alpha_blend_op) | `0` |
| --- | --- | --- |
| [BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) | [color_blend_op](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_color_blend_op) | `0` |
| [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) | [dst_alpha_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor) | `0` |
| [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) | [dst_color_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor) | `0` |
| [bool](class_bool.md#class_bool) | [enable_blend](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_enable_blend) | `false` |
| [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) | [src_alpha_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor) | `0` |
| [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) | [src_color_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor) | `0` |
| [bool](class_bool.md#class_bool) | [write_a](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_a) | `true` |
| [bool](class_bool.md#class_bool) | [write_b](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_b) | `true` |
| [bool](class_bool.md#class_bool) | [write_g](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_g) | `true` |
| [bool](class_bool.md#class_bool) | [write_r](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_r) | `true` |

### Methods


| void | [set_as_mix](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_method_set_as_mix) ( ) |
| --- | --- |

---

### Property Descriptions

<span id="class_RDPipelineColorBlendStateAttachment_property_alpha_blend_op"></span>

[BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **alpha_blend_op** = `0` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_alpha_blend_op)

- void **set_alpha_blend_op** ( value: [BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) )
- [BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **get_alpha_blend_op** ( )

The blend mode to use for the alpha channel.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_color_blend_op"></span>

[BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **color_blend_op** = `0` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_color_blend_op)

- void **set_color_blend_op** ( value: [BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) )
- [BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **get_color_blend_op** ( )

The blend mode to use for the red/green/blue color channels.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **dst_alpha_blend_factor** = `0` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor)

- void **set_dst_alpha_blend_factor** ( value: [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) )
- [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **get_dst_alpha_blend_factor** ( )

Controls how the blend factor for the alpha channel is determined based on the destination's fragments.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **dst_color_blend_factor** = `0` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor)

- void **set_dst_color_blend_factor** ( value: [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) )
- [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **get_dst_color_blend_factor** ( )

Controls how the blend factor for the color channels is determined based on the destination's fragments.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_enable_blend"></span>

[bool](class_bool.md#class_bool) **enable_blend** = `false` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_enable_blend)

- void **set_enable_blend** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_blend** ( )

If `true`, performs blending between the source and destination according to the factors defined in [src_color_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor), [dst_color_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor), [src_alpha_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor) and [dst_alpha_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor). The blend modes [color_blend_op](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_color_blend_op) and [alpha_blend_op](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_alpha_blend_op) are also taken into account, with [write_r](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_r), [write_g](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_g), [write_b](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_b) and [write_a](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_a) controlling the output.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **src_alpha_blend_factor** = `0` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor)

- void **set_src_alpha_blend_factor** ( value: [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) )
- [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **get_src_alpha_blend_factor** ( )

Controls how the blend factor for the alpha channel is determined based on the source's fragments.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **src_color_blend_factor** = `0` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor)

- void **set_src_color_blend_factor** ( value: [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) )
- [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **get_src_color_blend_factor** ( )

Controls how the blend factor for the color channels is determined based on the source's fragments.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_write_a"></span>

[bool](class_bool.md#class_bool) **write_a** = `true` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_a)

- void **set_write_a** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_write_a** ( )

If `true`, writes the new alpha channel to the final result.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_write_b"></span>

[bool](class_bool.md#class_bool) **write_b** = `true` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_b)

- void **set_write_b** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_write_b** ( )

If `true`, writes the new blue color channel to the final result.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_write_g"></span>

[bool](class_bool.md#class_bool) **write_g** = `true` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_g)

- void **set_write_g** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_write_g** ( )

If `true`, writes the new green color channel to the final result.

---

<span id="class_RDPipelineColorBlendStateAttachment_property_write_r"></span>

[bool](class_bool.md#class_bool) **write_r** = `true` [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_write_r)

- void **set_write_r** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_write_r** ( )

If `true`, writes the new red color channel to the final result.

---

### Method Descriptions

<span id="class_RDPipelineColorBlendStateAttachment_method_set_as_mix"></span>

void **set_as_mix** ( ) [🔗](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_method_set_as_mix)

Convenience method to perform standard mix blending with straight (non-premultiplied) alpha. This sets [enable_blend](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_enable_blend) to `true`, [src_color_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor) to [RenderingDevice.BLEND_FACTOR_SRC_ALPHA](class_renderingdevice.md#class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA), [dst_color_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor) to [RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA](class_renderingdevice.md#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA), [src_alpha_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor) to [RenderingDevice.BLEND_FACTOR_SRC_ALPHA](class_renderingdevice.md#class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA) and [dst_alpha_blend_factor](class_rdpipelinecolorblendstateattachment.md#class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor) to [RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA](class_renderingdevice.md#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA).
