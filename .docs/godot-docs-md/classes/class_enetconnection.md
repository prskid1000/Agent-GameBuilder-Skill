<span id="class_ENetConnection"></span>

## ENetConnection

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A wrapper class for an ENetHost.

### Description

ENet's purpose is to provide a relatively thin, simple and robust network communication layer on top of UDP (User Datagram Protocol).

### Tutorials

- API documentation on the ENet website

### Methods


| void | [bandwidth_limit](class_enetconnection.md#class_ENetConnection_method_bandwidth_limit) ( in_bandwidth: [int](class_int.md#class_int) = 0, out_bandwidth: [int](class_int.md#class_int) = 0 ) |
| --- | --- |
| void | [broadcast](class_enetconnection.md#class_ENetConnection_method_broadcast) ( channel: [int](class_int.md#class_int), packet: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), flags: [int](class_int.md#class_int) ) |
| void | [channel_limit](class_enetconnection.md#class_ENetConnection_method_channel_limit) ( limit: [int](class_int.md#class_int) ) |
| void | [compress](class_enetconnection.md#class_ENetConnection_method_compress) ( mode: [CompressionMode](class_enetconnection.md#enum_ENetConnection_CompressionMode) ) |
| [ENetPacketPeer](class_enetpacketpeer.md#class_ENetPacketPeer) | [connect_to_host](class_enetconnection.md#class_ENetConnection_method_connect_to_host) ( address: [String](class_string.md#class_String), port: [int](class_int.md#class_int), channels: [int](class_int.md#class_int) = 0, data: [int](class_int.md#class_int) = 0 ) |
| Error | [create_host](class_enetconnection.md#class_ENetConnection_method_create_host) ( max_peers: [int](class_int.md#class_int) = 32, max_channels: [int](class_int.md#class_int) = 0, in_bandwidth: [int](class_int.md#class_int) = 0, out_bandwidth: [int](class_int.md#class_int) = 0 ) |
| Error | [create_host_bound](class_enetconnection.md#class_ENetConnection_method_create_host_bound) ( bind_address: [String](class_string.md#class_String), bind_port: [int](class_int.md#class_int), max_peers: [int](class_int.md#class_int) = 32, max_channels: [int](class_int.md#class_int) = 0, in_bandwidth: [int](class_int.md#class_int) = 0, out_bandwidth: [int](class_int.md#class_int) = 0 ) |
| void | [destroy](class_enetconnection.md#class_ENetConnection_method_destroy) ( ) |
| Error | [dtls_client_setup](class_enetconnection.md#class_ENetConnection_method_dtls_client_setup) ( hostname: [String](class_string.md#class_String), client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) |
| Error | [dtls_server_setup](class_enetconnection.md#class_ENetConnection_method_dtls_server_setup) ( server_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) ) |
| void | [flush](class_enetconnection.md#class_ENetConnection_method_flush) ( ) |
| [int](class_int.md#class_int) | [get_local_port](class_enetconnection.md#class_ENetConnection_method_get_local_port) ( ) const |
| [int](class_int.md#class_int) | [get_max_channels](class_enetconnection.md#class_ENetConnection_method_get_max_channels) ( ) const |
| [Array](class_array.md#class_Array)\[[ENetPacketPeer](class_enetpacketpeer.md#class_ENetPacketPeer)\] | [get_peers](class_enetconnection.md#class_ENetConnection_method_get_peers) ( ) |
| [float](class_float.md#class_float) | [pop_statistic](class_enetconnection.md#class_ENetConnection_method_pop_statistic) ( statistic: [HostStatistic](class_enetconnection.md#enum_ENetConnection_HostStatistic) ) |
| void | [refuse_new_connections](class_enetconnection.md#class_ENetConnection_method_refuse_new_connections) ( refuse: [bool](class_bool.md#class_bool) ) |
| [Array](class_array.md#class_Array) | [service](class_enetconnection.md#class_ENetConnection_method_service) ( timeout: [int](class_int.md#class_int) = 0 ) |
| void | [socket_send](class_enetconnection.md#class_ENetConnection_method_socket_send) ( destination_address: [String](class_string.md#class_String), destination_port: [int](class_int.md#class_int), packet: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |

---

### Enumerations

<span id="enum_ENetConnection_CompressionMode"></span>

enum **CompressionMode**: [🔗](class_enetconnection.md#enum_ENetConnection_CompressionMode)

<span id="class_ENetConnection_constant_COMPRESS_NONE"></span>

[CompressionMode](class_enetconnection.md#enum_ENetConnection_CompressionMode) **COMPRESS_NONE** = `0`

No compression. This uses the most bandwidth, but has the upside of requiring the fewest CPU resources. This option may also be used to make network debugging using tools like Wireshark easier.

<span id="class_ENetConnection_constant_COMPRESS_RANGE_CODER"></span>

[CompressionMode](class_enetconnection.md#enum_ENetConnection_CompressionMode) **COMPRESS_RANGE_CODER** = `1`

ENet's built-in range encoding. Works well on small packets, but is not the most efficient algorithm on packets larger than 4 KB.

<span id="class_ENetConnection_constant_COMPRESS_FASTLZ"></span>

[CompressionMode](class_enetconnection.md#enum_ENetConnection_CompressionMode) **COMPRESS_FASTLZ** = `2`

FastLZ compression. This option uses less CPU resources compared to [COMPRESS_ZLIB](class_enetconnection.md#class_ENetConnection_constant_COMPRESS_ZLIB), at the expense of using more bandwidth.

<span id="class_ENetConnection_constant_COMPRESS_ZLIB"></span>

[CompressionMode](class_enetconnection.md#enum_ENetConnection_CompressionMode) **COMPRESS_ZLIB** = `3`

Zlib compression. This option uses less bandwidth compared to [COMPRESS_FASTLZ](class_enetconnection.md#class_ENetConnection_constant_COMPRESS_FASTLZ), at the expense of using more CPU resources.

<span id="class_ENetConnection_constant_COMPRESS_ZSTD"></span>

[CompressionMode](class_enetconnection.md#enum_ENetConnection_CompressionMode) **COMPRESS_ZSTD** = `4`

Zstandard compression. Note that this algorithm is not very efficient on packets smaller than 4 KB. Therefore, it's recommended to use other compression algorithms in most cases.

---

<span id="enum_ENetConnection_EventType"></span>

enum **EventType**: [🔗](class_enetconnection.md#enum_ENetConnection_EventType)

<span id="class_ENetConnection_constant_EVENT_ERROR"></span>

[EventType](class_enetconnection.md#enum_ENetConnection_EventType) **EVENT_ERROR** = `-1`

An error occurred during [service()](class_enetconnection.md#class_ENetConnection_method_service). You will likely need to [destroy()](class_enetconnection.md#class_ENetConnection_method_destroy) the host and recreate it.

<span id="class_ENetConnection_constant_EVENT_NONE"></span>

[EventType](class_enetconnection.md#enum_ENetConnection_EventType) **EVENT_NONE** = `0`

No event occurred within the specified time limit.

<span id="class_ENetConnection_constant_EVENT_CONNECT"></span>

[EventType](class_enetconnection.md#enum_ENetConnection_EventType) **EVENT_CONNECT** = `1`

A connection request initiated by enet_host_connect has completed. The array will contain the peer which successfully connected.

<span id="class_ENetConnection_constant_EVENT_DISCONNECT"></span>

[EventType](class_enetconnection.md#enum_ENetConnection_EventType) **EVENT_DISCONNECT** = `2`

A peer has disconnected. This event is generated on a successful completion of a disconnect initiated by [ENetPacketPeer.peer_disconnect()](class_enetpacketpeer.md#class_ENetPacketPeer_method_peer_disconnect), if a peer has timed out, or if a connection request initialized by [connect_to_host()](class_enetconnection.md#class_ENetConnection_method_connect_to_host) has timed out. The array will contain the peer which disconnected. The data field contains user supplied data describing the disconnection, or 0, if none is available.

<span id="class_ENetConnection_constant_EVENT_RECEIVE"></span>

[EventType](class_enetconnection.md#enum_ENetConnection_EventType) **EVENT_RECEIVE** = `3`

A packet has been received from a peer. The array will contain the peer which sent the packet and the channel number upon which the packet was received. The received packet will be queued to the associated [ENetPacketPeer](class_enetpacketpeer.md#class_ENetPacketPeer).

---

<span id="enum_ENetConnection_HostStatistic"></span>

enum **HostStatistic**: [🔗](class_enetconnection.md#enum_ENetConnection_HostStatistic)

<span id="class_ENetConnection_constant_HOST_TOTAL_SENT_DATA"></span>

[HostStatistic](class_enetconnection.md#enum_ENetConnection_HostStatistic) **HOST_TOTAL_SENT_DATA** = `0`

Total data sent.

<span id="class_ENetConnection_constant_HOST_TOTAL_SENT_PACKETS"></span>

[HostStatistic](class_enetconnection.md#enum_ENetConnection_HostStatistic) **HOST_TOTAL_SENT_PACKETS** = `1`

Total UDP packets sent.

<span id="class_ENetConnection_constant_HOST_TOTAL_RECEIVED_DATA"></span>

[HostStatistic](class_enetconnection.md#enum_ENetConnection_HostStatistic) **HOST_TOTAL_RECEIVED_DATA** = `2`

Total data received.

<span id="class_ENetConnection_constant_HOST_TOTAL_RECEIVED_PACKETS"></span>

[HostStatistic](class_enetconnection.md#enum_ENetConnection_HostStatistic) **HOST_TOTAL_RECEIVED_PACKETS** = `3`

Total UDP packets received.

---

### Method Descriptions

<span id="class_ENetConnection_method_bandwidth_limit"></span>

void **bandwidth_limit** ( in_bandwidth: [int](class_int.md#class_int) = 0, out_bandwidth: [int](class_int.md#class_int) = 0 ) [🔗](class_enetconnection.md#class_ENetConnection_method_bandwidth_limit)

Adjusts the bandwidth limits of a host.

---

<span id="class_ENetConnection_method_broadcast"></span>

void **broadcast** ( channel: [int](class_int.md#class_int), packet: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), flags: [int](class_int.md#class_int) ) [🔗](class_enetconnection.md#class_ENetConnection_method_broadcast)

Queues a `packet` to be sent to all peers associated with the host over the specified `channel`. See [ENetPacketPeer](class_enetpacketpeer.md#class_ENetPacketPeer) `FLAG_*` constants for available packet flags.

---

<span id="class_ENetConnection_method_channel_limit"></span>

void **channel_limit** ( limit: [int](class_int.md#class_int) ) [🔗](class_enetconnection.md#class_ENetConnection_method_channel_limit)

Limits the maximum allowed channels of future incoming connections.

---

<span id="class_ENetConnection_method_compress"></span>

void **compress** ( mode: [CompressionMode](class_enetconnection.md#enum_ENetConnection_CompressionMode) ) [🔗](class_enetconnection.md#class_ENetConnection_method_compress)

Sets the compression method used for network packets. These have different tradeoffs of compression speed versus bandwidth, you may need to test which one works best for your use case if you use compression at all.

 **Note:** Most games' network design involve sending many small packets frequently (smaller than 4 KB each). If in doubt, it is recommended to keep the default compression algorithm as it works best on these small packets.

 **Note:** The compression mode must be set to the same value on both the server and all its clients. Clients will fail to connect if the compression mode set on the client differs from the one set on the server.

---

<span id="class_ENetConnection_method_connect_to_host"></span>

[ENetPacketPeer](class_enetpacketpeer.md#class_ENetPacketPeer) **connect_to_host** ( address: [String](class_string.md#class_String), port: [int](class_int.md#class_int), channels: [int](class_int.md#class_int) = 0, data: [int](class_int.md#class_int) = 0 ) [🔗](class_enetconnection.md#class_ENetConnection_method_connect_to_host)

Initiates a connection to a foreign `address` using the specified `port` and allocating the requested `channels`. Optional `data` can be passed during connection in the form of a 32 bit integer.

 **Note:** You must call either [create_host()](class_enetconnection.md#class_ENetConnection_method_create_host) or [create_host_bound()](class_enetconnection.md#class_ENetConnection_method_create_host_bound) on both ends before calling this method.

---

<span id="class_ENetConnection_method_create_host"></span>

Error **create_host** ( max_peers: [int](class_int.md#class_int) = 32, max_channels: [int](class_int.md#class_int) = 0, in_bandwidth: [int](class_int.md#class_int) = 0, out_bandwidth: [int](class_int.md#class_int) = 0 ) [🔗](class_enetconnection.md#class_ENetConnection_method_create_host)

Creates an ENetHost that allows up to `max_peers` connected peers, each allocating up to `max_channels` channels, optionally limiting bandwidth to `in_bandwidth` and `out_bandwidth` (if greater than zero).

This method binds a random available dynamic UDP port on the host machine at the *unspecified* address. Use [create_host_bound()](class_enetconnection.md#class_ENetConnection_method_create_host_bound) to specify the address and port.

 **Note:** It is necessary to create a host in both client and server in order to establish a connection.

---

<span id="class_ENetConnection_method_create_host_bound"></span>

Error **create_host_bound** ( bind_address: [String](class_string.md#class_String), bind_port: [int](class_int.md#class_int), max_peers: [int](class_int.md#class_int) = 32, max_channels: [int](class_int.md#class_int) = 0, in_bandwidth: [int](class_int.md#class_int) = 0, out_bandwidth: [int](class_int.md#class_int) = 0 ) [🔗](class_enetconnection.md#class_ENetConnection_method_create_host_bound)

Creates an ENetHost bound to the given `bind_address` and `bind_port` that allows up to `max_peers` connected peers, each allocating up to `max_channels` channels, optionally limiting bandwidth to `in_bandwidth` and `out_bandwidth` (if greater than zero).

 **Note:** It is necessary to create a host in both client and server in order to establish a connection.

---

<span id="class_ENetConnection_method_destroy"></span>

void **destroy** ( ) [🔗](class_enetconnection.md#class_ENetConnection_method_destroy)

Destroys the host and all resources associated with it.

---

<span id="class_ENetConnection_method_dtls_client_setup"></span>

Error **dtls_client_setup** ( hostname: [String](class_string.md#class_String), client_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) = null ) [🔗](class_enetconnection.md#class_ENetConnection_method_dtls_client_setup)

Configure this ENetHost to use the custom Godot extension allowing DTLS encryption for ENet clients. Call this before [connect_to_host()](class_enetconnection.md#class_ENetConnection_method_connect_to_host) to have ENet connect using DTLS validating the server certificate against `hostname`. You can pass the optional `client_options` parameter to customize the trusted certification authorities, or disable the common name verification. See [TLSOptions.client()](class_tlsoptions.md#class_TLSOptions_method_client) and [TLSOptions.client_unsafe()](class_tlsoptions.md#class_TLSOptions_method_client_unsafe).

---

<span id="class_ENetConnection_method_dtls_server_setup"></span>

Error **dtls_server_setup** ( server_options: [TLSOptions](class_tlsoptions.md#class_TLSOptions) ) [🔗](class_enetconnection.md#class_ENetConnection_method_dtls_server_setup)

Configure this ENetHost to use the custom Godot extension allowing DTLS encryption for ENet servers. Call this right after [create_host_bound()](class_enetconnection.md#class_ENetConnection_method_create_host_bound) to have ENet expect peers to connect using DTLS. See [TLSOptions.server()](class_tlsoptions.md#class_TLSOptions_method_server).

---

<span id="class_ENetConnection_method_flush"></span>

void **flush** ( ) [🔗](class_enetconnection.md#class_ENetConnection_method_flush)

Sends any queued packets on the host specified to its designated peers.

---

<span id="class_ENetConnection_method_get_local_port"></span>

[int](class_int.md#class_int) **get_local_port** ( ) *const* [🔗](class_enetconnection.md#class_ENetConnection_method_get_local_port)

Returns the local port to which this peer is bound.

---

<span id="class_ENetConnection_method_get_max_channels"></span>

[int](class_int.md#class_int) **get_max_channels** ( ) *const* [🔗](class_enetconnection.md#class_ENetConnection_method_get_max_channels)

Returns the maximum number of channels allowed for connected peers.

---

<span id="class_ENetConnection_method_get_peers"></span>

[Array](class_array.md#class_Array)\[[ENetPacketPeer](class_enetpacketpeer.md#class_ENetPacketPeer)\] **get_peers** ( ) [🔗](class_enetconnection.md#class_ENetConnection_method_get_peers)

Returns the list of peers associated with this host.

 **Note:** This list might include some peers that are not fully connected or are still being disconnected.

---

<span id="class_ENetConnection_method_pop_statistic"></span>

[float](class_float.md#class_float) **pop_statistic** ( statistic: [HostStatistic](class_enetconnection.md#enum_ENetConnection_HostStatistic) ) [🔗](class_enetconnection.md#class_ENetConnection_method_pop_statistic)

Returns and resets host statistics.

---

<span id="class_ENetConnection_method_refuse_new_connections"></span>

void **refuse_new_connections** ( refuse: [bool](class_bool.md#class_bool) ) [🔗](class_enetconnection.md#class_ENetConnection_method_refuse_new_connections)

Configures the DTLS server to automatically drop new connections.

 **Note:** This method is only relevant after calling [dtls_server_setup()](class_enetconnection.md#class_ENetConnection_method_dtls_server_setup).

---

<span id="class_ENetConnection_method_service"></span>

[Array](class_array.md#class_Array) **service** ( timeout: [int](class_int.md#class_int) = 0 ) [🔗](class_enetconnection.md#class_ENetConnection_method_service)

Waits for events on this connection and shuttles packets between the host and its peers, with the given `timeout` (in milliseconds). The returned [Array](class_array.md#class_Array) will have 4 elements. An [EventType](class_enetconnection.md#enum_ENetConnection_EventType), the [ENetPacketPeer](class_enetpacketpeer.md#class_ENetPacketPeer) which generated the event, the event associated data (if any), the event associated channel (if any). If the generated event is [EVENT_RECEIVE](class_enetconnection.md#class_ENetConnection_constant_EVENT_RECEIVE), the received packet will be queued to the associated [ENetPacketPeer](class_enetpacketpeer.md#class_ENetPacketPeer).

Call this function regularly to handle connections, disconnections, and to receive new packets.

 **Note:** This method must be called on both ends involved in the event (sending and receiving hosts).

---

<span id="class_ENetConnection_method_socket_send"></span>

void **socket_send** ( destination_address: [String](class_string.md#class_String), destination_port: [int](class_int.md#class_int), packet: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_enetconnection.md#class_ENetConnection_method_socket_send)

Sends a `packet` toward a destination from the address and port currently bound by this ENetConnection instance.

This is useful as it serves to establish entries in NAT routing tables on all devices between this bound instance and the public facing internet, allowing a prospective client's connection packets to be routed backward through the NAT device(s) between the public internet and this host.

This requires forward knowledge of a prospective client's address and communication port as seen by the public internet - after any NAT devices have handled their connection request. This information can be obtained by a STUN service, and must be handed off to your host by an entity that is not the prospective client. This will never work for a client behind a Symmetric NAT due to the nature of the Symmetric NAT routing algorithm, as their IP and Port cannot be known beforehand.
