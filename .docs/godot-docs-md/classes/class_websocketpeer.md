<span id="class_WebSocketPeer"></span>

## WebSocketPeer

**Inherits:** [PacketPeer](class_packetpeer.md#class_PacketPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A WebSocket connection.

### Description

This class represents WebSocket connection, and can be used as a WebSocket client (RFC 6455-compliant) or as a remote peer of a WebSocket server.

You can send WebSocket binary frames using [PacketPeer.put_packet()](class_packetpeer.md#class_PacketPeer_method_put_packet), and WebSocket text frames using [send()](class_websocketpeer.md#class_WebSocketPeer_method_send) (prefer text frames when interacting with text-based API). You can check the frame type of the last packet via [was_string_packet()](class_websocketpeer.md#class_WebSocketPeer_method_was_string_packet).

To start a WebSocket client, first call [connect_to_url()](class_websocketpeer.md#class_WebSocketPeer_method_connect_to_url), then regularly call [poll()](class_websocketpeer.md#class_WebSocketPeer_method_poll) (e.g. during [Node](class_node.md#class_Node) process). You can query the socket state via [get_ready_state()](class_websocketpeer.md#class_WebSocketPeer_method_get_ready_state), get the number of pending packets using [PacketPeer.get_available_packet_count()](class_packetpeer.md#class_PacketPeer_method_get_available_packet_count), and retrieve them via [PacketPeer.get_packet()](class_packetpeer.md#class_PacketPeer_method_get_packet).

.. tabs::

```
```

    extends Node

    var socket = WebSocketPeer.new()

    func _ready():
        socket.connect_to_url("wss://example.com")

    func _process(delta):
        socket.poll()
        var state = socket.get_ready_state()
        if state == WebSocketPeer.STATE_OPEN:
            while socket.get_available_packet_count():
                print("Packet: ", socket.get_packet())
        elif state == WebSocketPeer.STATE_CLOSING:
            # Keep polling to achieve proper close.
            pass
        elif state == WebSocketPeer.STATE_CLOSED:
            var code = socket.get_close_code()
            var reason = socket.get_close_reason()
            print("WebSocket closed with code: %d, reason %s. Clean: %s" % [code, reason, code != -1])
            set_process(false) # Stop processing.

To use the peer as part of a WebSocket server refer to [accept_stream()](class_websocketpeer.md#class_WebSocketPeer_method_accept_stream) and the online tutorial.

### Properties


| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [handshake_headers](class_websocketpeer.md#class_WebSocketPeer_property_handshake_headers) | `PackedStringArray()` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [heartbeat_interval](class_websocketpeer.md#class_WebSocketPeer_property_heartbeat_interval) | `0.0` |
| [int](class_int.md#class_int) | [inbound_buffer_size](class_websocketpeer.md#class_WebSocketPeer_property_inbound_buffer_size) | `65535` |
| [int](class_int.md#class_int) | [max_queued_packets](class_websocketpeer.md#class_WebSocketPeer_property_max_queued_packets) | `4096` |
| [int](class_int.md#class_int) | [outbound_buffer_size](class_websocketpeer.md#class_WebSocketPeer_property_outbound_buffer_size) | `65535` |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [supported_protocols](class_websocketpeer.md#class_WebSocketPeer_property_supported_protocols) | `PackedStringArray()` |

### Methods


| Error | [accept_stream](class_websocketpeer.md#class_WebSocketPeer_method_accept_stream) ( stream: [StreamPeer](class_streampeer.md#class_StreamPeer) ) |
| --- | --- |
| void | [close](class_websocketpeer.md#class_WebSocketPeer_method_close) ( code: [int](class_int.md#class_int) = 1000, reason: [String](class_string.md#class_String) = "" ) |
| Error | [connect_to_url](class_websocketpeer.md#class_WebSocketPeer_method_connect_to_url) ( url: [String](class_string.md#class_String), tls_client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) |
| [int](class_int.md#class_int) | [get_close_code](class_websocketpeer.md#class_WebSocketPeer_method_get_close_code) ( ) const |
| [String](class_string.md#class_String) | [get_close_reason](class_websocketpeer.md#class_WebSocketPeer_method_get_close_reason) ( ) const |
| [String](class_string.md#class_String) | [get_connected_host](class_websocketpeer.md#class_WebSocketPeer_method_get_connected_host) ( ) const |
| [int](class_int.md#class_int) | [get_connected_port](class_websocketpeer.md#class_WebSocketPeer_method_get_connected_port) ( ) const |
| [int](class_int.md#class_int) | [get_current_outbound_buffered_amount](class_websocketpeer.md#class_WebSocketPeer_method_get_current_outbound_buffered_amount) ( ) const |
| [State](class_websocketpeer.md#enum_WebSocketPeer_State) | [get_ready_state](class_websocketpeer.md#class_WebSocketPeer_method_get_ready_state) ( ) const |
| [String](class_string.md#class_String) | [get_requested_url](class_websocketpeer.md#class_WebSocketPeer_method_get_requested_url) ( ) const |
| [String](class_string.md#class_String) | [get_selected_protocol](class_websocketpeer.md#class_WebSocketPeer_method_get_selected_protocol) ( ) const |
| void | [poll](class_websocketpeer.md#class_WebSocketPeer_method_poll) ( ) |
| Error | [send](class_websocketpeer.md#class_WebSocketPeer_method_send) ( message: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), write_mode: [WriteMode](class_websocketpeer.md#enum_WebSocketPeer_WriteMode) = 1 ) |
| Error | [send_text](class_websocketpeer.md#class_WebSocketPeer_method_send_text) ( message: [String](class_string.md#class_String) ) |
| void | [set_no_delay](class_websocketpeer.md#class_WebSocketPeer_method_set_no_delay) ( enabled: [bool](class_bool.md#class_bool) ) |
| [bool](class_bool.md#class_bool) | [was_string_packet](class_websocketpeer.md#class_WebSocketPeer_method_was_string_packet) ( ) const |

---

### Enumerations

<span id="enum_WebSocketPeer_WriteMode"></span>

enum **WriteMode**: [🔗](class_websocketpeer.md#enum_WebSocketPeer_WriteMode)

<span id="class_WebSocketPeer_constant_WRITE_MODE_TEXT"></span>

[WriteMode](class_websocketpeer.md#enum_WebSocketPeer_WriteMode) **WRITE_MODE_TEXT** = `0`

Specifies that WebSockets messages should be transferred as text payload (only valid UTF-8 is allowed).

<span id="class_WebSocketPeer_constant_WRITE_MODE_BINARY"></span>

[WriteMode](class_websocketpeer.md#enum_WebSocketPeer_WriteMode) **WRITE_MODE_BINARY** = `1`

Specifies that WebSockets messages should be transferred as binary payload (any byte combination is allowed).

---

<span id="enum_WebSocketPeer_State"></span>

enum **State**: [🔗](class_websocketpeer.md#enum_WebSocketPeer_State)

<span id="class_WebSocketPeer_constant_STATE_CONNECTING"></span>

[State](class_websocketpeer.md#enum_WebSocketPeer_State) **STATE_CONNECTING** = `0`

Socket has been created. The connection is not yet open.

<span id="class_WebSocketPeer_constant_STATE_OPEN"></span>

[State](class_websocketpeer.md#enum_WebSocketPeer_State) **STATE_OPEN** = `1`

The connection is open and ready to communicate.

<span id="class_WebSocketPeer_constant_STATE_CLOSING"></span>

[State](class_websocketpeer.md#enum_WebSocketPeer_State) **STATE_CLOSING** = `2`

The connection is in the process of closing. This means a close request has been sent to the remote peer but confirmation has not been received.

<span id="class_WebSocketPeer_constant_STATE_CLOSED"></span>

[State](class_websocketpeer.md#enum_WebSocketPeer_State) **STATE_CLOSED** = `3`

The connection is closed or couldn't be opened.

---

### Property Descriptions

<span id="class_WebSocketPeer_property_handshake_headers"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **handshake_headers** = `PackedStringArray()` [🔗](class_websocketpeer.md#class_WebSocketPeer_property_handshake_headers)

- void **set_handshake_headers** ( value: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )
- [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_handshake_headers** ( )

The extra HTTP headers to be sent during the WebSocket handshake.

 **Note:** Not supported in Web exports due to browsers' restrictions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

<span id="class_WebSocketPeer_property_heartbeat_interval"></span>

[float](class_float.md#class_float) **heartbeat_interval** = `0.0` [🔗](class_websocketpeer.md#class_WebSocketPeer_property_heartbeat_interval)

- void **set_heartbeat_interval** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_heartbeat_interval** ( )

The interval (in seconds) at which the peer will automatically send WebSocket "ping" control frames. When set to `0`, no "ping" control frames will be sent.

 **Note:** Has no effect in Web exports due to browser restrictions.

---

<span id="class_WebSocketPeer_property_inbound_buffer_size"></span>

[int](class_int.md#class_int) **inbound_buffer_size** = `65535` [🔗](class_websocketpeer.md#class_WebSocketPeer_property_inbound_buffer_size)

- void **set_inbound_buffer_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_inbound_buffer_size** ( )

The size of the input buffer in bytes (roughly the maximum amount of memory that will be allocated for the inbound packets).

---

<span id="class_WebSocketPeer_property_max_queued_packets"></span>

[int](class_int.md#class_int) **max_queued_packets** = `4096` [🔗](class_websocketpeer.md#class_WebSocketPeer_property_max_queued_packets)

- void **set_max_queued_packets** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_queued_packets** ( )

The maximum amount of packets that will be allowed in the queues (both inbound and outbound).

---

<span id="class_WebSocketPeer_property_outbound_buffer_size"></span>

[int](class_int.md#class_int) **outbound_buffer_size** = `65535` [🔗](class_websocketpeer.md#class_WebSocketPeer_property_outbound_buffer_size)

- void **set_outbound_buffer_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_outbound_buffer_size** ( )

The size of the input buffer in bytes (roughly the maximum amount of memory that will be allocated for the outbound packets).

---

<span id="class_WebSocketPeer_property_supported_protocols"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **supported_protocols** = `PackedStringArray()` [🔗](class_websocketpeer.md#class_WebSocketPeer_property_supported_protocols)

- void **set_supported_protocols** ( value: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )
- [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_supported_protocols** ( )

The WebSocket sub-protocols allowed during the WebSocket handshake.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.

---

### Method Descriptions

<span id="class_WebSocketPeer_method_accept_stream"></span>

Error **accept_stream** ( stream: [StreamPeer](class_streampeer.md#class_StreamPeer) ) [🔗](class_websocketpeer.md#class_WebSocketPeer_method_accept_stream)

Accepts a peer connection performing the HTTP handshake as a WebSocket server. The `stream` must be a valid TCP stream retrieved via [TCPServer.take_connection()](class_tcpserver.md#class_TCPServer_method_take_connection), or a TLS stream accepted via [StreamPeerTLS.accept_stream()](class_streampeertls.md#class_StreamPeerTLS_method_accept_stream).

 **Note:** Not supported in Web exports due to browsers' restrictions.

---

<span id="class_WebSocketPeer_method_close"></span>

void **close** ( code: [int](class_int.md#class_int) = 1000, reason: [String](class_string.md#class_String) = "" ) [🔗](class_websocketpeer.md#class_WebSocketPeer_method_close)

Closes this WebSocket connection.

 `code` is the status code for the closure (see RFC 6455 section 7.4 for a list of valid status codes). If `code` is negative, the connection will be closed immediately without notifying the remote peer.

 `reason` is the human-readable reason for closing the connection. It can be any UTF-8 string that's smaller than 123 bytes.

 **Note:** To achieve a clean closure, you will need to keep polling until [STATE_CLOSED](class_websocketpeer.md#class_WebSocketPeer_constant_STATE_CLOSED) is reached.

 **Note:** The Web export might not support all status codes. Please refer to browser-specific documentation for more details.

---

<span id="class_WebSocketPeer_method_connect_to_url"></span>

Error **connect_to_url** ( url: [String](class_string.md#class_String), tls_client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) [🔗](class_websocketpeer.md#class_WebSocketPeer_method_connect_to_url)

Connects to the given URL. TLS certificates will be verified against the hostname when connecting using the `wss://` protocol. You can pass the optional `tls_client_options` parameter to customize the trusted certification authorities, or disable the common name verification. See [TLSOptions.client()](class_tlsoptions.md#class_TLSOptions_method_client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class_TLSOptions_method_client_unsafe).

 **Note:** This method is non-blocking, and will return @GlobalScope.OK before the connection is established as long as the provided parameters are valid and the peer is not in an invalid state (e.g. already connected). Regularly call [poll()](class_websocketpeer.md#class_WebSocketPeer_method_poll) (e.g. during [Node](class_node.md#class_Node) process) and check the result of [get_ready_state()](class_websocketpeer.md#class_WebSocketPeer_method_get_ready_state) to know whether the connection succeeds or fails.

 **Note:** To avoid mixed content warnings or errors in Web, you may have to use a `url` that starts with `wss://` (secure) instead of `ws://`. When doing so, make sure to use the fully qualified domain name that matches the one defined in the server's TLS certificate. Do not connect directly via the IP address for `wss://` connections, as it won't match with the TLS certificate.

---

<span id="class_WebSocketPeer_method_get_close_code"></span>

[int](class_int.md#class_int) **get_close_code** ( ) *const* [🔗](class_websocketpeer.md#class_WebSocketPeer_method_get_close_code)

Returns the received WebSocket close frame status code, or `-1` when the connection was not cleanly closed. Only call this method when [get_ready_state()](class_websocketpeer.md#class_WebSocketPeer_method_get_ready_state) returns [STATE_CLOSED](class_websocketpeer.md#class_WebSocketPeer_constant_STATE_CLOSED).

---

<span id="class_WebSocketPeer_method_get_close_reason"></span>

[String](class_string.md#class_String) **get_close_reason** ( ) *const* [🔗](class_websocketpeer.md#class_WebSocketPeer_method_get_close_reason)

Returns the received WebSocket close frame status reason string. Only call this method when [get_ready_state()](class_websocketpeer.md#class_WebSocketPeer_method_get_ready_state) returns [STATE_CLOSED](class_websocketpeer.md#class_WebSocketPeer_constant_STATE_CLOSED).

---

<span id="class_WebSocketPeer_method_get_connected_host"></span>

[String](class_string.md#class_String) **get_connected_host** ( ) *const* [🔗](class_websocketpeer.md#class_WebSocketPeer_method_get_connected_host)

Returns the IP address of the connected peer.

 **Note:** Not available in the Web export.

---

<span id="class_WebSocketPeer_method_get_connected_port"></span>

[int](class_int.md#class_int) **get_connected_port** ( ) *const* [🔗](class_websocketpeer.md#class_WebSocketPeer_method_get_connected_port)

Returns the remote port of the connected peer.

 **Note:** Not available in the Web export.

---

<span id="class_WebSocketPeer_method_get_current_outbound_buffered_amount"></span>

[int](class_int.md#class_int) **get_current_outbound_buffered_amount** ( ) *const* [🔗](class_websocketpeer.md#class_WebSocketPeer_method_get_current_outbound_buffered_amount)

Returns the current amount of data in the outbound websocket buffer. **Note:** Web exports use WebSocket.bufferedAmount, while other platforms use an internal buffer.

---

<span id="class_WebSocketPeer_method_get_ready_state"></span>

[State](class_websocketpeer.md#enum_WebSocketPeer_State) **get_ready_state** ( ) *const* [🔗](class_websocketpeer.md#class_WebSocketPeer_method_get_ready_state)

Returns the ready state of the connection.

---

<span id="class_WebSocketPeer_method_get_requested_url"></span>

[String](class_string.md#class_String) **get_requested_url** ( ) *const* [🔗](class_websocketpeer.md#class_WebSocketPeer_method_get_requested_url)

Returns the URL requested by this peer. The URL is derived from the `url` passed to [connect_to_url()](class_websocketpeer.md#class_WebSocketPeer_method_connect_to_url) or from the HTTP headers when acting as server (i.e. when using [accept_stream()](class_websocketpeer.md#class_WebSocketPeer_method_accept_stream)).

---

<span id="class_WebSocketPeer_method_get_selected_protocol"></span>

[String](class_string.md#class_String) **get_selected_protocol** ( ) *const* [🔗](class_websocketpeer.md#class_WebSocketPeer_method_get_selected_protocol)

Returns the selected WebSocket sub-protocol for this connection or an empty string if the sub-protocol has not been selected yet.

---

<span id="class_WebSocketPeer_method_poll"></span>

void **poll** ( ) [🔗](class_websocketpeer.md#class_WebSocketPeer_method_poll)

Updates the connection state and receive incoming packets. Call this function regularly to keep it in a clean state.

---

<span id="class_WebSocketPeer_method_send"></span>

Error **send** ( message: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), write_mode: [WriteMode](class_websocketpeer.md#enum_WebSocketPeer_WriteMode) = 1 ) [🔗](class_websocketpeer.md#class_WebSocketPeer_method_send)

Sends the given `message` using the desired `write_mode`. When sending a [String](class_string.md#class_String), prefer using [send_text()](class_websocketpeer.md#class_WebSocketPeer_method_send_text).

---

<span id="class_WebSocketPeer_method_send_text"></span>

Error **send_text** ( message: [String](class_string.md#class_String) ) [🔗](class_websocketpeer.md#class_WebSocketPeer_method_send_text)

Sends the given `message` using WebSocket text mode. Prefer this method over [PacketPeer.put_packet()](class_packetpeer.md#class_PacketPeer_method_put_packet) when interacting with third-party text-based API (e.g. when using [JSON](class_json.md#class_JSON) formatted messages).

---

<span id="class_WebSocketPeer_method_set_no_delay"></span>

void **set_no_delay** ( enabled: [bool](class_bool.md#class_bool) ) [🔗](class_websocketpeer.md#class_WebSocketPeer_method_set_no_delay)

Disable Nagle's algorithm on the underlying TCP socket (default). See [StreamPeerTCP.set_no_delay()](class_streampeertcp.md#class_StreamPeerTCP_method_set_no_delay) for more information.

 **Note:** Not available in the Web export.

---

<span id="class_WebSocketPeer_method_was_string_packet"></span>

[bool](class_bool.md#class_bool) **was_string_packet** ( ) *const* [🔗](class_websocketpeer.md#class_WebSocketPeer_method_was_string_packet)

Returns `true` if the last received packet was sent as a text payload. See [WriteMode](class_websocketpeer.md#enum_WebSocketPeer_WriteMode).
