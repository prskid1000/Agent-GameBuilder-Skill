<span id="class_StreamPeerTLS"></span>

## StreamPeerTLS

**Inherits:** [StreamPeer](class_streampeer.md#class_StreamPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A stream peer that handles TLS connections.

### Description

A stream peer that handles TLS connections. This object can be used to connect to a TLS server or accept a single TLS client connection.

 **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

### Tutorials

- [TLS certificates](../tutorials/networking/ssl_certificates.md)

### Methods


| Error | [accept_stream](class_streampeertls.md#class_StreamPeerTLS_method_accept_stream) ( stream: [StreamPeer](class_streampeer.md#class_StreamPeer), server_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) ) |
| --- | --- |
| Error | [connect_to_stream](class_streampeertls.md#class_StreamPeerTLS_method_connect_to_stream) ( stream: [StreamPeer](class_streampeer.md#class_StreamPeer), common_name: [String](class_string.md#class_String), client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) |
| void | [disconnect_from_stream](class_streampeertls.md#class_StreamPeerTLS_method_disconnect_from_stream) ( ) |
| [Status](class_streampeertls.md#enum_StreamPeerTLS_Status) | [get_status](class_streampeertls.md#class_StreamPeerTLS_method_get_status) ( ) const |
| [StreamPeer](class_streampeer.md#class_StreamPeer) | [get_stream](class_streampeertls.md#class_StreamPeerTLS_method_get_stream) ( ) const |
| void | [poll](class_streampeertls.md#class_StreamPeerTLS_method_poll) ( ) |

---

### Enumerations

<span id="enum_StreamPeerTLS_Status"></span>

enum **Status**: [🔗](class_streampeertls.md#enum_StreamPeerTLS_Status)

<span id="class_StreamPeerTLS_constant_STATUS_DISCONNECTED"></span>

[Status](class_streampeertls.md#enum_StreamPeerTLS_Status) **STATUS_DISCONNECTED** = `0`

A status representing a **StreamPeerTLS** that is disconnected.

<span id="class_StreamPeerTLS_constant_STATUS_HANDSHAKING"></span>

[Status](class_streampeertls.md#enum_StreamPeerTLS_Status) **STATUS_HANDSHAKING** = `1`

A status representing a **StreamPeerTLS** during handshaking.

<span id="class_StreamPeerTLS_constant_STATUS_CONNECTED"></span>

[Status](class_streampeertls.md#enum_StreamPeerTLS_Status) **STATUS_CONNECTED** = `2`

A status representing a **StreamPeerTLS** that is connected to a host.

<span id="class_StreamPeerTLS_constant_STATUS_ERROR"></span>

[Status](class_streampeertls.md#enum_StreamPeerTLS_Status) **STATUS_ERROR** = `3`

A status representing a **StreamPeerTLS** in error state.

<span id="class_StreamPeerTLS_constant_STATUS_ERROR_HOSTNAME_MISMATCH"></span>

[Status](class_streampeertls.md#enum_StreamPeerTLS_Status) **STATUS_ERROR_HOSTNAME_MISMATCH** = `4`

An error status that shows a mismatch in the TLS certificate domain presented by the host and the domain requested for validation.

---

### Method Descriptions

<span id="class_StreamPeerTLS_method_accept_stream"></span>

Error **accept_stream** ( stream: [StreamPeer](class_streampeer.md#class_StreamPeer), server_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) ) [🔗](class_streampeertls.md#class_StreamPeerTLS_method_accept_stream)

Accepts a peer connection as a server using the given `server_options`. See [TLSOptions.server()](class_tlsoptions.md#class_TLSOptions_method_server).

---

<span id="class_StreamPeerTLS_method_connect_to_stream"></span>

Error **connect_to_stream** ( stream: [StreamPeer](class_streampeer.md#class_StreamPeer), common_name: [String](class_string.md#class_String), client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) [🔗](class_streampeertls.md#class_StreamPeerTLS_method_connect_to_stream)

Connects to a peer using an underlying [StreamPeer](class_streampeer.md#class_StreamPeer) `stream` and verifying the remote certificate is correctly signed for the given `common_name`. You can pass the optional `client_options` parameter to customize the trusted certification authorities, or disable the common name verification. See [TLSOptions.client()](class_tlsoptions.md#class_TLSOptions_method_client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class_TLSOptions_method_client_unsafe).

---

<span id="class_StreamPeerTLS_method_disconnect_from_stream"></span>

void **disconnect_from_stream** ( ) [🔗](class_streampeertls.md#class_StreamPeerTLS_method_disconnect_from_stream)

Disconnects from host.

---

<span id="class_StreamPeerTLS_method_get_status"></span>

[Status](class_streampeertls.md#enum_StreamPeerTLS_Status) **get_status** ( ) *const* [🔗](class_streampeertls.md#class_StreamPeerTLS_method_get_status)

Returns the status of the connection.

---

<span id="class_StreamPeerTLS_method_get_stream"></span>

[StreamPeer](class_streampeer.md#class_StreamPeer) **get_stream** ( ) *const* [🔗](class_streampeertls.md#class_StreamPeerTLS_method_get_stream)

Returns the underlying [StreamPeer](class_streampeer.md#class_StreamPeer) connection, used in [accept_stream()](class_streampeertls.md#class_StreamPeerTLS_method_accept_stream) or [connect_to_stream()](class_streampeertls.md#class_StreamPeerTLS_method_connect_to_stream).

---

<span id="class_StreamPeerTLS_method_poll"></span>

void **poll** ( ) [🔗](class_streampeertls.md#class_StreamPeerTLS_method_poll)

Poll the connection to check for incoming bytes. Call this right before [StreamPeer.get_available_bytes()](class_streampeer.md#class_StreamPeer_method_get_available_bytes) for it to work properly.
