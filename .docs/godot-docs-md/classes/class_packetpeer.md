<span id="class_PacketPeer"></span>

## PacketPeer

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [ENetPacketPeer](class_enetpacketpeer.md#class_ENetPacketPeer), [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer), [PacketPeerDTLS](class_packetpeerdtls.md#class_PacketPeerDTLS), [PacketPeerExtension](class_packetpeerextension.md#class_PacketPeerExtension), [PacketPeerStream](class_packetpeerstream.md#class_PacketPeerStream), [PacketPeerUDP](class_packetpeerudp.md#class_PacketPeerUDP), [WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel), [WebSocketPeer](class_websocketpeer.md#class_WebSocketPeer)

Abstraction and base class for packet-based protocols.

### Description

PacketPeer is an abstraction and base class for packet-based protocols (such as UDP). It provides an API for sending and receiving packets both as raw data or variables. This makes it easy to transfer data over a protocol, without having to encode data as low-level bytes or having to worry about network ordering.

 **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

### Properties


| [int](class_int.md#class_int) | [encode_buffer_max_size](class_packetpeer.md#class_PacketPeer_property_encode_buffer_max_size) | `8388608` |
| --- | --- | --- |

### Methods


| [int](class_int.md#class_int) | [get_available_packet_count](class_packetpeer.md#class_PacketPeer_method_get_available_packet_count) ( ) const |
| --- | --- |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [get_packet](class_packetpeer.md#class_PacketPeer_method_get_packet) ( ) |
| Error | [get_packet_error](class_packetpeer.md#class_PacketPeer_method_get_packet_error) ( ) const |
| [Variant](class_variant.md#class_Variant) | [get_var](class_packetpeer.md#class_PacketPeer_method_get_var) ( allow_objects: [bool](class_bool.md#class_bool) = false ) |
| Error | [put_packet](class_packetpeer.md#class_PacketPeer_method_put_packet) ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| Error | [put_var](class_packetpeer.md#class_PacketPeer_method_put_var) ( var: [Variant](class_variant.md#class_Variant), full_objects: [bool](class_bool.md#class_bool) = false ) |

---

### Property Descriptions

<span id="class_PacketPeer_property_encode_buffer_max_size"></span>

[int](class_int.md#class_int) **encode_buffer_max_size** = `8388608` [🔗](class_packetpeer.md#class_PacketPeer_property_encode_buffer_max_size)

- void **set_encode_buffer_max_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_encode_buffer_max_size** ( )

Maximum buffer size allowed when encoding [Variant](class_variant.md#class_Variant) s. Raise this value to support heavier memory allocations.

The [put_var()](class_packetpeer.md#class_PacketPeer_method_put_var) method allocates memory on the stack, and the buffer used will grow automatically to the closest power of two to match the size of the [Variant](class_variant.md#class_Variant). If the [Variant](class_variant.md#class_Variant) is bigger than [encode_buffer_max_size](class_packetpeer.md#class_PacketPeer_property_encode_buffer_max_size), the method will error out with @GlobalScope.ERR_OUT_OF_MEMORY.

---

### Method Descriptions

<span id="class_PacketPeer_method_get_available_packet_count"></span>

[int](class_int.md#class_int) **get_available_packet_count** ( ) *const* [🔗](class_packetpeer.md#class_PacketPeer_method_get_available_packet_count)

Returns the number of packets currently available in the ring-buffer.

---

<span id="class_PacketPeer_method_get_packet"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_packet** ( ) [🔗](class_packetpeer.md#class_PacketPeer_method_get_packet)

Gets a raw packet.

---

<span id="class_PacketPeer_method_get_packet_error"></span>

Error **get_packet_error** ( ) *const* [🔗](class_packetpeer.md#class_PacketPeer_method_get_packet_error)

Returns the error state of the last packet received (via [get_packet()](class_packetpeer.md#class_PacketPeer_method_get_packet) and [get_var()](class_packetpeer.md#class_PacketPeer_method_get_var)).

---

<span id="class_PacketPeer_method_get_var"></span>

[Variant](class_variant.md#class_Variant) **get_var** ( allow_objects: [bool](class_bool.md#class_bool) = false ) [🔗](class_packetpeer.md#class_PacketPeer_method_get_var)

Gets a Variant. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the @GlobalScope.bytes_to_var() method.

 **Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.

---

<span id="class_PacketPeer_method_put_packet"></span>

Error **put_packet** ( buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_packetpeer.md#class_PacketPeer_method_put_packet)

Sends a raw packet.

---

<span id="class_PacketPeer_method_put_var"></span>

Error **put_var** ( var: [Variant](class_variant.md#class_Variant), full_objects: [bool](class_bool.md#class_bool) = false ) [🔗](class_packetpeer.md#class_PacketPeer_method_put_var)

Sends a [Variant](class_variant.md#class_Variant) as a packet. If `full_objects` is `true`, encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the @GlobalScope.var_to_bytes() method.
