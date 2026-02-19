<span id="class_PacketPeerStream"></span>

## PacketPeerStream

**Inherits:** [PacketPeer](class_packetpeer.md#class_PacketPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Wrapper to use a PacketPeer over a StreamPeer.

### Description

PacketStreamPeer provides a wrapper for working using packets over a stream. This allows for using packet based code with StreamPeers. PacketPeerStream implements a custom protocol over the StreamPeer, so the user should not read or write to the wrapped StreamPeer directly.

 **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

### Properties


| [int](class_int.md#class_int) | [input_buffer_max_size](class_packetpeerstream.md#class_PacketPeerStream_property_input_buffer_max_size) | `65532` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [output_buffer_max_size](class_packetpeerstream.md#class_PacketPeerStream_property_output_buffer_max_size) | `65532` |
| [StreamPeer](class_streampeer.md#class_StreamPeer) | [stream_peer](class_packetpeerstream.md#class_PacketPeerStream_property_stream_peer) |

---

### Property Descriptions

<span id="class_PacketPeerStream_property_input_buffer_max_size"></span>

[int](class_int.md#class_int) **input_buffer_max_size** = `65532` [🔗](class_packetpeerstream.md#class_PacketPeerStream_property_input_buffer_max_size)

- void **set_input_buffer_max_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_input_buffer_max_size** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_PacketPeerStream_property_output_buffer_max_size"></span>

[int](class_int.md#class_int) **output_buffer_max_size** = `65532` [🔗](class_packetpeerstream.md#class_PacketPeerStream_property_output_buffer_max_size)

- void **set_output_buffer_max_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_output_buffer_max_size** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_PacketPeerStream_property_stream_peer"></span>

[StreamPeer](class_streampeer.md#class_StreamPeer) **stream_peer** [🔗](class_packetpeerstream.md#class_PacketPeerStream_property_stream_peer)

- void **set_stream_peer** ( value: [StreamPeer](class_streampeer.md#class_StreamPeer) )
- [StreamPeer](class_streampeer.md#class_StreamPeer) **get_stream_peer** ( )

The wrapped [StreamPeer](class_streampeer.md#class_StreamPeer) object.
