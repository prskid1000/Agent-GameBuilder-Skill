<span id="class_RDVertexAttribute"></span>

## RDVertexAttribute

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Vertex attribute (used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice)).

### Description

This object is used by [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

### Properties


| [int](class_int.md#class_int) | [binding](class_rdvertexattribute.md#class_RDVertexAttribute_property_binding) | `4294967295` |
| --- | --- | --- |
| [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) | [format](class_rdvertexattribute.md#class_RDVertexAttribute_property_format) | `232` |
| [VertexFrequency](class_renderingdevice.md#enum_RenderingDevice_VertexFrequency) | [frequency](class_rdvertexattribute.md#class_RDVertexAttribute_property_frequency) | `0` |
| [int](class_int.md#class_int) | [location](class_rdvertexattribute.md#class_RDVertexAttribute_property_location) | `0` |
| [int](class_int.md#class_int) | [offset](class_rdvertexattribute.md#class_RDVertexAttribute_property_offset) | `0` |
| [int](class_int.md#class_int) | [stride](class_rdvertexattribute.md#class_RDVertexAttribute_property_stride) | `0` |

---

### Property Descriptions

<span id="class_RDVertexAttribute_property_binding"></span>

[int](class_int.md#class_int) **binding** = `4294967295` [🔗](class_rdvertexattribute.md#class_RDVertexAttribute_property_binding)

- void **set_binding** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_binding** ( )

The index of the buffer in the vertex buffer array to bind this vertex attribute. When set to `-1`, it defaults to the index of the attribute.

 **Note:** You cannot mix binding explicitly assigned attributes with implicitly assigned ones (i.e. `-1`). Either all attributes must have their binding set to `-1`, or all must have explicit bindings.

---

<span id="class_RDVertexAttribute_property_format"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **format** = `232` [🔗](class_rdvertexattribute.md#class_RDVertexAttribute_property_format)

- void **set_format** ( value: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) )
- [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **get_format** ( )

The way that this attribute's data is interpreted when sent to a shader.

---

<span id="class_RDVertexAttribute_property_frequency"></span>

[VertexFrequency](class_renderingdevice.md#enum_RenderingDevice_VertexFrequency) **frequency** = `0` [🔗](class_rdvertexattribute.md#class_RDVertexAttribute_property_frequency)

- void **set_frequency** ( value: [VertexFrequency](class_renderingdevice.md#enum_RenderingDevice_VertexFrequency) )
- [VertexFrequency](class_renderingdevice.md#enum_RenderingDevice_VertexFrequency) **get_frequency** ( )

The rate at which this attribute is pulled from its vertex buffer.

---

<span id="class_RDVertexAttribute_property_location"></span>

[int](class_int.md#class_int) **location** = `0` [🔗](class_rdvertexattribute.md#class_RDVertexAttribute_property_location)

- void **set_location** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_location** ( )

The location in the shader that this attribute is bound to.

---

<span id="class_RDVertexAttribute_property_offset"></span>

[int](class_int.md#class_int) **offset** = `0` [🔗](class_rdvertexattribute.md#class_RDVertexAttribute_property_offset)

- void **set_offset** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_offset** ( )

The number of bytes between the start of the vertex buffer and the first instance of this attribute.

---

<span id="class_RDVertexAttribute_property_stride"></span>

[int](class_int.md#class_int) **stride** = `0` [🔗](class_rdvertexattribute.md#class_RDVertexAttribute_property_stride)

- void **set_stride** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_stride** ( )

The number of bytes between the starts of consecutive instances of this attribute.
