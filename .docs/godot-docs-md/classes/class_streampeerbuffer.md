<span id="class_StreamPeerBuffer"></span>

## StreamPeerBuffer

**Inherits:** [StreamPeer](class_streampeer.md#class_StreamPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A stream peer used to handle binary data streams.

### Description

A data buffer stream peer that uses a byte array as the stream. This object can be used to handle binary data from network sessions. To handle binary data stored in files, [FileAccess](class_fileaccess.md#class_FileAccess) can be used directly.

A **StreamPeerBuffer** object keeps an internal cursor which is the offset in bytes to the start of the buffer. Get and put operations are performed at the cursor position and will move the cursor accordingly.

### Properties


| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [data_array](class_streampeerbuffer.md#class_StreamPeerBuffer_property_data_array) | `PackedByteArray()` |
| --- | --- | --- |

### Methods


| void | [clear](class_streampeerbuffer.md#class_StreamPeerBuffer_method_clear) ( ) |
| --- | --- |
| [StreamPeerBuffer](class_streampeerbuffer.md#class_StreamPeerBuffer) | [duplicate](class_streampeerbuffer.md#class_StreamPeerBuffer_method_duplicate) ( ) const |
| [int](class_int.md#class_int) | [get_position](class_streampeerbuffer.md#class_StreamPeerBuffer_method_get_position) ( ) const |
| [int](class_int.md#class_int) | [get_size](class_streampeerbuffer.md#class_StreamPeerBuffer_method_get_size) ( ) const |
| void | [resize](class_streampeerbuffer.md#class_StreamPeerBuffer_method_resize) ( size: [int](class_int.md#class_int) ) |
| void | [seek](class_streampeerbuffer.md#class_StreamPeerBuffer_method_seek) ( position: [int](class_int.md#class_int) ) |

---

### Property Descriptions

<span id="class_StreamPeerBuffer_property_data_array"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **data_array** = `PackedByteArray()` [🔗](class_streampeerbuffer.md#class_StreamPeerBuffer_property_data_array)

- void **set_data_array** ( value: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_data_array** ( )

The underlying data buffer. Setting this value resets the cursor.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

### Method Descriptions

<span id="class_StreamPeerBuffer_method_clear"></span>

void **clear** ( ) [🔗](class_streampeerbuffer.md#class_StreamPeerBuffer_method_clear)

Clears the [data_array](class_streampeerbuffer.md#class_StreamPeerBuffer_property_data_array) and resets the cursor.

---

<span id="class_StreamPeerBuffer_method_duplicate"></span>

[StreamPeerBuffer](class_streampeerbuffer.md#class_StreamPeerBuffer) **duplicate** ( ) *const* [🔗](class_streampeerbuffer.md#class_StreamPeerBuffer_method_duplicate)

Returns a new **StreamPeerBuffer** with the same [data_array](class_streampeerbuffer.md#class_StreamPeerBuffer_property_data_array) content.

---

<span id="class_StreamPeerBuffer_method_get_position"></span>

[int](class_int.md#class_int) **get_position** ( ) *const* [🔗](class_streampeerbuffer.md#class_StreamPeerBuffer_method_get_position)

Returns the current cursor position.

---

<span id="class_StreamPeerBuffer_method_get_size"></span>

[int](class_int.md#class_int) **get_size** ( ) *const* [🔗](class_streampeerbuffer.md#class_StreamPeerBuffer_method_get_size)

Returns the size of [data_array](class_streampeerbuffer.md#class_StreamPeerBuffer_property_data_array).

---

<span id="class_StreamPeerBuffer_method_resize"></span>

void **resize** ( size: [int](class_int.md#class_int) ) [🔗](class_streampeerbuffer.md#class_StreamPeerBuffer_method_resize)

Resizes the [data_array](class_streampeerbuffer.md#class_StreamPeerBuffer_property_data_array). This *doesn't* update the cursor.

---

<span id="class_StreamPeerBuffer_method_seek"></span>

void **seek** ( position: [int](class_int.md#class_int) ) [🔗](class_streampeerbuffer.md#class_StreamPeerBuffer_method_seek)

Moves the cursor to the specified position. `position` must be a valid index of [data_array](class_streampeerbuffer.md#class_StreamPeerBuffer_property_data_array).
