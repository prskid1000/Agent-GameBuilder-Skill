<span id="class_WebSocketMultiplayerPeer"></span>

## WebSocketMultiplayerPeer

**Inherits:** [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) **<** [PacketPeer](class_packetpeer.md#class_PacketPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Base class for WebSocket server and client.

### Description

Base class for WebSocket server and client, allowing them to be used as multiplayer peer for the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI).

 **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

### Properties


| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [handshake_headers](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_handshake_headers) | `PackedStringArray()` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [handshake_timeout](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_handshake_timeout) | `3.0` |
| [int](class_int.md#class_int) | [inbound_buffer_size](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_inbound_buffer_size) | `65535` |
| [int](class_int.md#class_int) | [max_queued_packets](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_max_queued_packets) | `4096` |
| [int](class_int.md#class_int) | [outbound_buffer_size](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_outbound_buffer_size) | `65535` |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [supported_protocols](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_supported_protocols) | `PackedStringArray()` |

### Methods


| Error | [create_client](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_create_client) ( url: [String](class_string.md#class_String), tls_client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) |
| --- | --- |
| Error | [create_server](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_create_server) ( port: [int](class_int.md#class_int), bind_address: [String](class_string.md#class_String) = "*", tls_server_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) |
| [WebSocketPeer](class_websocketpeer.md#class_WebSocketPeer) | [get_peer](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_get_peer) ( peer_id: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_peer_address](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_get_peer_address) ( id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_peer_port](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_get_peer_port) ( id: [int](class_int.md#class_int) ) const |

---

### Property Descriptions

<span id="class_WebSocketMultiplayerPeer_property_handshake_headers"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **handshake_headers** = `PackedStringArray()` [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_handshake_headers)

- void **set_handshake_headers** ( value: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )
- [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_handshake_headers** ( )

The extra headers to use during handshake. See [WebSocketPeer.handshake_headers](class_websocketpeer.md#class_WebSocketPeer_property_handshake_headers) for more details.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

<span id="class_WebSocketMultiplayerPeer_property_handshake_timeout"></span>

[float](class_float.md#class_float) **handshake_timeout** = `3.0` [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_handshake_timeout)

- void **set_handshake_timeout** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_handshake_timeout** ( )

The maximum time each peer can stay in a connecting state before being dropped.

---

<span id="class_WebSocketMultiplayerPeer_property_inbound_buffer_size"></span>

[int](class_int.md#class_int) **inbound_buffer_size** = `65535` [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_inbound_buffer_size)

- void **set_inbound_buffer_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_inbound_buffer_size** ( )

The inbound buffer size for connected peers. See [WebSocketPeer.inbound_buffer_size](class_websocketpeer.md#class_WebSocketPeer_property_inbound_buffer_size) for more details.

---

<span id="class_WebSocketMultiplayerPeer_property_max_queued_packets"></span>

[int](class_int.md#class_int) **max_queued_packets** = `4096` [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_max_queued_packets)

- void **set_max_queued_packets** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_queued_packets** ( )

The maximum number of queued packets for connected peers. See [WebSocketPeer.max_queued_packets](class_websocketpeer.md#class_WebSocketPeer_property_max_queued_packets) for more details.

---

<span id="class_WebSocketMultiplayerPeer_property_outbound_buffer_size"></span>

[int](class_int.md#class_int) **outbound_buffer_size** = `65535` [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_outbound_buffer_size)

- void **set_outbound_buffer_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_outbound_buffer_size** ( )

The outbound buffer size for connected peers. See [WebSocketPeer.outbound_buffer_size](class_websocketpeer.md#class_WebSocketPeer_property_outbound_buffer_size) for more details.

---

<span id="class_WebSocketMultiplayerPeer_property_supported_protocols"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **supported_protocols** = `PackedStringArray()` [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_property_supported_protocols)

- void **set_supported_protocols** ( value: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )
- [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_supported_protocols** ( )

The supported WebSocket sub-protocols. See [WebSocketPeer.supported_protocols](class_websocketpeer.md#class_WebSocketPeer_property_supported_protocols) for more details.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

### Method Descriptions

<span id="class_WebSocketMultiplayerPeer_method_create_client"></span>

Error **create_client** ( url: [String](class_string.md#class_String), tls_client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_create_client)

Starts a new multiplayer client connecting to the given `url`. TLS certificates will be verified against the hostname when connecting using the `wss://` protocol. You can pass the optional `tls_client_options` parameter to customize the trusted certification authorities, or disable the common name verification. See [TLSOptions.client()](class_tlsoptions.md#class_TLSOptions_method_client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class_TLSOptions_method_client_unsafe).

 **Note:** It is recommended to specify the scheme part of the URL, i.e. the `url` should start with either `ws://` or `wss://`.

---

<span id="class_WebSocketMultiplayerPeer_method_create_server"></span>

Error **create_server** ( port: [int](class_int.md#class_int), bind_address: [String](class_string.md#class_String) = "*", tls_server_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_create_server)

Starts a new multiplayer server listening on the given `port`. You can optionally specify a `bind_address`, and provide valid `tls_server_options` to use TLS. See [TLSOptions.server()](class_tlsoptions.md#class_TLSOptions_method_server).

---

<span id="class_WebSocketMultiplayerPeer_method_get_peer"></span>

[WebSocketPeer](class_websocketpeer.md#class_WebSocketPeer) **get_peer** ( peer_id: [int](class_int.md#class_int) ) *const* [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_get_peer)

Returns the [WebSocketPeer](class_websocketpeer.md#class_WebSocketPeer) associated to the given `peer_id`.

---

<span id="class_WebSocketMultiplayerPeer_method_get_peer_address"></span>

[String](class_string.md#class_String) **get_peer_address** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_get_peer_address)

Returns the IP address of the given peer.

---

<span id="class_WebSocketMultiplayerPeer_method_get_peer_port"></span>

[int](class_int.md#class_int) **get_peer_port** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_websocketmultiplayerpeer.md#class_WebSocketMultiplayerPeer_method_get_peer_port)

Returns the remote port of the given peer.
