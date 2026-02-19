<span id="class_RDAttachmentFormat"></span>

## RDAttachmentFormat

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Attachment format (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) | [format](class_rdattachmentformat.md#class_RDAttachmentFormat_property_format) | `36` |
| --- | --- | --- |
| [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) | [samples](class_rdattachmentformat.md#class_RDAttachmentFormat_property_samples) | `0` |
| [int](class_int.md#class_int) | [usage_flags](class_rdattachmentformat.md#class_RDAttachmentFormat_property_usage_flags) | `0` |

---

### Property Descriptions

<span id="class_RDAttachmentFormat_property_format"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **format** = `36` [🔗](class_rdattachmentformat.md#class_RDAttachmentFormat_property_format)

- void **set_format** ( value: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) )
- [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **get_format** ( )

The attachment's data format.

---

<span id="class_RDAttachmentFormat_property_samples"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **samples** = `0` [🔗](class_rdattachmentformat.md#class_RDAttachmentFormat_property_samples)

- void **set_samples** ( value: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) )
- [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **get_samples** ( )

The number of samples used when sampling the attachment.

---

<span id="class_RDAttachmentFormat_property_usage_flags"></span>

[int](class_int.md#class_int) **usage_flags** = `0` [🔗](class_rdattachmentformat.md#class_RDAttachmentFormat_property_usage_flags)

- void **set_usage_flags** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_usage_flags** ( )

The attachment's usage flags, which determine what can be done with it.
