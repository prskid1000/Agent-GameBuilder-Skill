<span id="class_WebRTCDataChannel"></span>

## WebRTCDataChannel

**Inherits:** [PacketPeer](class_packetpeer.md#class_PacketPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [WebRTCDataChannelExtension](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension)

.. container:: contribute

	There is currently no description for this class. Please help us by contributing one!

### Properties


| [WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) | [write_mode](class_webrtcdatachannel.md#class_WebRTCDataChannel_property_write_mode) | `1` |
| --- | --- | --- |

### Methods


| void | [close](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_close) ( ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_buffered_amount](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_buffered_amount) ( ) const |
| [int](class_int.md#class_int) | [get_id](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_id) ( ) const |
| [String](class_string.md#class_String) | [get_label](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_label) ( ) const |
| [int](class_int.md#class_int) | [get_max_packet_life_time](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_max_packet_life_time) ( ) const |
| [int](class_int.md#class_int) | [get_max_retransmits](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_max_retransmits) ( ) const |
| [String](class_string.md#class_String) | [get_protocol](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_protocol) ( ) const |
| [ChannelState](class_webrtcdatachannel.md#enum_WebRTCDataChannel_ChannelState) | [get_ready_state](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_ready_state) ( ) const |
| [bool](class_bool.md#class_bool) | [is_negotiated](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_is_negotiated) ( ) const |
| [bool](class_bool.md#class_bool) | [is_ordered](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_is_ordered) ( ) const |
| Error | [poll](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_poll) ( ) |
| [bool](class_bool.md#class_bool) | [was_string_packet](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_was_string_packet) ( ) const |

---

### Enumerations

<span id="enum_WebRTCDataChannel_WriteMode"></span>

enum **WriteMode**: [🔗](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode)

<span id="class_WebRTCDataChannel_constant_WRITE_MODE_TEXT"></span>

[WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) **WRITE_MODE_TEXT** = `0`

Tells the channel to send data over this channel as text. An external peer (non-Godot) would receive this as a string.

<span id="class_WebRTCDataChannel_constant_WRITE_MODE_BINARY"></span>

[WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) **WRITE_MODE_BINARY** = `1`

Tells the channel to send data over this channel as binary. An external peer (non-Godot) would receive this as array buffer or blob.

---

<span id="enum_WebRTCDataChannel_ChannelState"></span>

enum **ChannelState**: [🔗](class_webrtcdatachannel.md#enum_WebRTCDataChannel_ChannelState)

<span id="class_WebRTCDataChannel_constant_STATE_CONNECTING"></span>

[ChannelState](class_webrtcdatachannel.md#enum_WebRTCDataChannel_ChannelState) **STATE_CONNECTING** = `0`

The channel was created, but it's still trying to connect.

<span id="class_WebRTCDataChannel_constant_STATE_OPEN"></span>

[ChannelState](class_webrtcdatachannel.md#enum_WebRTCDataChannel_ChannelState) **STATE_OPEN** = `1`

The channel is currently open, and data can flow over it.

<span id="class_WebRTCDataChannel_constant_STATE_CLOSING"></span>

[ChannelState](class_webrtcdatachannel.md#enum_WebRTCDataChannel_ChannelState) **STATE_CLOSING** = `2`

The channel is being closed, no new messages will be accepted, but those already in queue will be flushed.

<span id="class_WebRTCDataChannel_constant_STATE_CLOSED"></span>

[ChannelState](class_webrtcdatachannel.md#enum_WebRTCDataChannel_ChannelState) **STATE_CLOSED** = `3`

The channel was closed, or connection failed.

---

### Property Descriptions

<span id="class_WebRTCDataChannel_property_write_mode"></span>

[WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) **write_mode** = `1` [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_property_write_mode)

- void **set_write_mode** ( value: [WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) )
- [WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) **get_write_mode** ( )

The transfer mode to use when sending outgoing packet. Either text or binary.

---

### Method Descriptions

<span id="class_WebRTCDataChannel_method_close"></span>

void **close** ( ) [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_close)

Closes this data channel, notifying the other peer.

---

<span id="class_WebRTCDataChannel_method_get_buffered_amount"></span>

[int](class_int.md#class_int) **get_buffered_amount** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_buffered_amount)

Returns the number of bytes currently queued to be sent over this channel.

---

<span id="class_WebRTCDataChannel_method_get_id"></span>

[int](class_int.md#class_int) **get_id** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_id)

Returns the ID assigned to this channel during creation (or auto-assigned during negotiation).

If the channel is not negotiated out-of-band the ID will only be available after the connection is established (will return `65535` until then).

---

<span id="class_WebRTCDataChannel_method_get_label"></span>

[String](class_string.md#class_String) **get_label** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_label)

Returns the label assigned to this channel during creation.

---

<span id="class_WebRTCDataChannel_method_get_max_packet_life_time"></span>

[int](class_int.md#class_int) **get_max_packet_life_time** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_max_packet_life_time)

Returns the `maxPacketLifeTime` value assigned to this channel during creation.

Will be `65535` if not specified.

---

<span id="class_WebRTCDataChannel_method_get_max_retransmits"></span>

[int](class_int.md#class_int) **get_max_retransmits** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_max_retransmits)

Returns the `maxRetransmits` value assigned to this channel during creation.

Will be `65535` if not specified.

---

<span id="class_WebRTCDataChannel_method_get_protocol"></span>

[String](class_string.md#class_String) **get_protocol** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_protocol)

Returns the sub-protocol assigned to this channel during creation. An empty string if not specified.

---

<span id="class_WebRTCDataChannel_method_get_ready_state"></span>

[ChannelState](class_webrtcdatachannel.md#enum_WebRTCDataChannel_ChannelState) **get_ready_state** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_get_ready_state)

Returns the current state of this channel.

---

<span id="class_WebRTCDataChannel_method_is_negotiated"></span>

[bool](class_bool.md#class_bool) **is_negotiated** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_is_negotiated)

Returns `true` if this channel was created with out-of-band configuration.

---

<span id="class_WebRTCDataChannel_method_is_ordered"></span>

[bool](class_bool.md#class_bool) **is_ordered** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_is_ordered)

Returns `true` if this channel was created with ordering enabled (default).

---

<span id="class_WebRTCDataChannel_method_poll"></span>

Error **poll** ( ) [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_poll)

Reserved, but not used for now.

---

<span id="class_WebRTCDataChannel_method_was_string_packet"></span>

[bool](class_bool.md#class_bool) **was_string_packet** ( ) *const* [🔗](class_webrtcdatachannel.md#class_WebRTCDataChannel_method_was_string_packet)

Returns `true` if the last received packet was transferred as text. See [write_mode](class_webrtcdatachannel.md#class_WebRTCDataChannel_property_write_mode).
