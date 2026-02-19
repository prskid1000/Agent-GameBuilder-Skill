<span id="class_PacketPeerDTLS"></span>

## PacketPeerDTLS

**Inherits:** [PacketPeer](class_packetpeer.md#class_PacketPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

DTLS packet peer.

### Description

This class represents a DTLS peer connection. It can be used to connect to a DTLS server, and is returned by [DTLSServer.take_connection()](class_dtlsserver.md#class_DTLSServer_method_take_connection).

 **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

 **Warning:** TLS certificate revocation and certificate pinning are currently not supported. Revoked certificates are accepted as long as they are otherwise valid. If this is a concern, you may want to use automatically managed certificates with a short validity period.

### Methods


| Error | [connect_to_peer](class_packetpeerdtls.md#class_PacketPeerDTLS_method_connect_to_peer) ( packet_peer: [PacketPeerUDP](class_packetpeerudp.md#class_PacketPeerUDP), hostname: [String](class_string.md#class_String), client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) |
| --- | --- |
| void | [disconnect_from_peer](class_packetpeerdtls.md#class_PacketPeerDTLS_method_disconnect_from_peer) ( ) |
| [Status](class_packetpeerdtls.md#enum_PacketPeerDTLS_Status) | [get_status](class_packetpeerdtls.md#class_PacketPeerDTLS_method_get_status) ( ) const |
| void | [poll](class_packetpeerdtls.md#class_PacketPeerDTLS_method_poll) ( ) |

---

### Enumerations

<span id="enum_PacketPeerDTLS_Status"></span>

enum **Status**: [🔗](class_packetpeerdtls.md#enum_PacketPeerDTLS_Status)

<span id="class_PacketPeerDTLS_constant_STATUS_DISCONNECTED"></span>

[Status](class_packetpeerdtls.md#enum_PacketPeerDTLS_Status) **STATUS_DISCONNECTED** = `0`

A status representing a **PacketPeerDTLS** that is disconnected.

<span id="class_PacketPeerDTLS_constant_STATUS_HANDSHAKING"></span>

[Status](class_packetpeerdtls.md#enum_PacketPeerDTLS_Status) **STATUS_HANDSHAKING** = `1`

A status representing a **PacketPeerDTLS** that is currently performing the handshake with a remote peer.

<span id="class_PacketPeerDTLS_constant_STATUS_CONNECTED"></span>

[Status](class_packetpeerdtls.md#enum_PacketPeerDTLS_Status) **STATUS_CONNECTED** = `2`

A status representing a **PacketPeerDTLS** that is connected to a remote peer.

<span id="class_PacketPeerDTLS_constant_STATUS_ERROR"></span>

[Status](class_packetpeerdtls.md#enum_PacketPeerDTLS_Status) **STATUS_ERROR** = `3`

A status representing a **PacketPeerDTLS** in a generic error state.

<span id="class_PacketPeerDTLS_constant_STATUS_ERROR_HOSTNAME_MISMATCH"></span>

[Status](class_packetpeerdtls.md#enum_PacketPeerDTLS_Status) **STATUS_ERROR_HOSTNAME_MISMATCH** = `4`

An error status that shows a mismatch in the DTLS certificate domain presented by the host and the domain requested for validation.

---

### Method Descriptions

<span id="class_PacketPeerDTLS_method_connect_to_peer"></span>

Error **connect_to_peer** ( packet_peer: [PacketPeerUDP](class_packetpeerudp.md#class_PacketPeerUDP), hostname: [String](class_string.md#class_String), client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) [🔗](class_packetpeerdtls.md#class_PacketPeerDTLS_method_connect_to_peer)

Connects a `packet_peer` beginning the DTLS handshake using the underlying [PacketPeerUDP](class_packetpeerudp.md#class_PacketPeerUDP) which must be connected (see [PacketPeerUDP.connect_to_host()](class_packetpeerudp.md#class_PacketPeerUDP_method_connect_to_host)). You can optionally specify the `client_options` to be used while verifying the TLS connections. See [TLSOptions.client()](class_tlsoptions.md#class_TLSOptions_method_client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class_TLSOptions_method_client_unsafe).

---

<span id="class_PacketPeerDTLS_method_disconnect_from_peer"></span>

void **disconnect_from_peer** ( ) [🔗](class_packetpeerdtls.md#class_PacketPeerDTLS_method_disconnect_from_peer)

Disconnects this peer, terminating the DTLS session.

---

<span id="class_PacketPeerDTLS_method_get_status"></span>

[Status](class_packetpeerdtls.md#enum_PacketPeerDTLS_Status) **get_status** ( ) *const* [🔗](class_packetpeerdtls.md#class_PacketPeerDTLS_method_get_status)

Returns the status of the connection.

---

<span id="class_PacketPeerDTLS_method_poll"></span>

void **poll** ( ) [🔗](class_packetpeerdtls.md#class_PacketPeerDTLS_method_poll)

Poll the connection to check for incoming packets. Call this frequently to update the status and keep the connection working.
