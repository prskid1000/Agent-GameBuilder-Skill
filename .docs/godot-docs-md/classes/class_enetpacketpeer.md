<span id="class_ENetPacketPeer"></span>

## ENetPacketPeer

**Inherits:** [PacketPeer](class_packetpeer.md#class_PacketPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A wrapper class for an ENetPeer.

### Description

A PacketPeer implementation representing a peer of an [ENetConnection](class_enetconnection.md#class_ENetConnection).

This class cannot be instantiated directly but can be retrieved during [ENetConnection.service()](class_enetconnection.md#class_ENetConnection_method_service) or via [ENetConnection.get_peers()](class_enetconnection.md#class_ENetConnection_method_get_peers).

 **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

### Tutorials

- API documentation on the ENet website

### Methods


| [int](class_int.md#class_int) | [get_channels](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_channels) ( ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_packet_flags](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_packet_flags) ( ) const |
| [String](class_string.md#class_String) | [get_remote_address](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_remote_address) ( ) const |
| [int](class_int.md#class_int) | [get_remote_port](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_remote_port) ( ) const |
| [PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) | [get_state](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_state) ( ) const |
| [float](class_float.md#class_float) | [get_statistic](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_statistic) ( statistic: [PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) ) |
| [bool](class_bool.md#class_bool) | [is_active](class_enetpacketpeer.md#class_ENetPacketPeer_method_is_active) ( ) const |
| void | [peer_disconnect](class_enetpacketpeer.md#class_ENetPacketPeer_method_peer_disconnect) ( data: [int](class_int.md#class_int) = 0 ) |
| void | [peer_disconnect_later](class_enetpacketpeer.md#class_ENetPacketPeer_method_peer_disconnect_later) ( data: [int](class_int.md#class_int) = 0 ) |
| void | [peer_disconnect_now](class_enetpacketpeer.md#class_ENetPacketPeer_method_peer_disconnect_now) ( data: [int](class_int.md#class_int) = 0 ) |
| void | [ping](class_enetpacketpeer.md#class_ENetPacketPeer_method_ping) ( ) |
| void | [ping_interval](class_enetpacketpeer.md#class_ENetPacketPeer_method_ping_interval) ( ping_interval: [int](class_int.md#class_int) ) |
| void | [reset](class_enetpacketpeer.md#class_ENetPacketPeer_method_reset) ( ) |
| Error | [send](class_enetpacketpeer.md#class_ENetPacketPeer_method_send) ( channel: [int](class_int.md#class_int), packet: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), flags: [int](class_int.md#class_int) ) |
| void | [set_timeout](class_enetpacketpeer.md#class_ENetPacketPeer_method_set_timeout) ( timeout: [int](class_int.md#class_int), timeout_min: [int](class_int.md#class_int), timeout_max: [int](class_int.md#class_int) ) |
| void | [throttle_configure](class_enetpacketpeer.md#class_ENetPacketPeer_method_throttle_configure) ( interval: [int](class_int.md#class_int), acceleration: [int](class_int.md#class_int), deceleration: [int](class_int.md#class_int) ) |

---

### Enumerations

<span id="enum_ENetPacketPeer_PeerState"></span>

enum **PeerState**: [🔗](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState)

<span id="class_ENetPacketPeer_constant_STATE_DISCONNECTED"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_DISCONNECTED** = `0`

The peer is disconnected.

<span id="class_ENetPacketPeer_constant_STATE_CONNECTING"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_CONNECTING** = `1`

The peer is currently attempting to connect.

<span id="class_ENetPacketPeer_constant_STATE_ACKNOWLEDGING_CONNECT"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_ACKNOWLEDGING_CONNECT** = `2`

The peer has acknowledged the connection request.

<span id="class_ENetPacketPeer_constant_STATE_CONNECTION_PENDING"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_CONNECTION_PENDING** = `3`

The peer is currently connecting.

<span id="class_ENetPacketPeer_constant_STATE_CONNECTION_SUCCEEDED"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_CONNECTION_SUCCEEDED** = `4`

The peer has successfully connected, but is not ready to communicate with yet ([STATE_CONNECTED](class_enetpacketpeer.md#class_ENetPacketPeer_constant_STATE_CONNECTED)).

<span id="class_ENetPacketPeer_constant_STATE_CONNECTED"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_CONNECTED** = `5`

The peer is currently connected and ready to communicate with.

<span id="class_ENetPacketPeer_constant_STATE_DISCONNECT_LATER"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_DISCONNECT_LATER** = `6`

The peer is expected to disconnect after it has no more outgoing packets to send.

<span id="class_ENetPacketPeer_constant_STATE_DISCONNECTING"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_DISCONNECTING** = `7`

The peer is currently disconnecting.

<span id="class_ENetPacketPeer_constant_STATE_ACKNOWLEDGING_DISCONNECT"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_ACKNOWLEDGING_DISCONNECT** = `8`

The peer has acknowledged the disconnection request.

<span id="class_ENetPacketPeer_constant_STATE_ZOMBIE"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **STATE_ZOMBIE** = `9`

The peer has lost connection, but is not considered truly disconnected (as the peer didn't acknowledge the disconnection request).

---

<span id="enum_ENetPacketPeer_PeerStatistic"></span>

enum **PeerStatistic**: [🔗](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic)

<span id="class_ENetPacketPeer_constant_PEER_PACKET_LOSS"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_LOSS** = `0`

Mean packet loss of reliable packets as a ratio with respect to the [PACKET_LOSS_SCALE](class_enetpacketpeer.md#class_ENetPacketPeer_constant_PACKET_LOSS_SCALE).

<span id="class_ENetPacketPeer_constant_PEER_PACKET_LOSS_VARIANCE"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_LOSS_VARIANCE** = `1`

Packet loss variance.

<span id="class_ENetPacketPeer_constant_PEER_PACKET_LOSS_EPOCH"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_LOSS_EPOCH** = `2`

The time at which packet loss statistics were last updated (in milliseconds since the connection started). The interval for packet loss statistics updates is 10 seconds, and at least one packet must have been sent since the last statistics update.

<span id="class_ENetPacketPeer_constant_PEER_ROUND_TRIP_TIME"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_ROUND_TRIP_TIME** = `3`

Mean packet round trip time for reliable packets.

<span id="class_ENetPacketPeer_constant_PEER_ROUND_TRIP_TIME_VARIANCE"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_ROUND_TRIP_TIME_VARIANCE** = `4`

Variance of the mean round trip time.

<span id="class_ENetPacketPeer_constant_PEER_LAST_ROUND_TRIP_TIME"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_LAST_ROUND_TRIP_TIME** = `5`

Last recorded round trip time for a reliable packet.

<span id="class_ENetPacketPeer_constant_PEER_LAST_ROUND_TRIP_TIME_VARIANCE"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_LAST_ROUND_TRIP_TIME_VARIANCE** = `6`

Variance of the last trip time recorded.

<span id="class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_THROTTLE** = `7`

The peer's current throttle status.

<span id="class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_LIMIT"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_THROTTLE_LIMIT** = `8`

The maximum number of unreliable packets that should not be dropped. This value is always greater than or equal to `1`. The initial value is equal to [PACKET_THROTTLE_SCALE](class_enetpacketpeer.md#class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE).

<span id="class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_COUNTER"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_THROTTLE_COUNTER** = `9`

Internal value used to increment the packet throttle counter. The value is hardcoded to `7` and cannot be changed. You probably want to look at [PEER_PACKET_THROTTLE_ACCELERATION](class_enetpacketpeer.md#class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_ACCELERATION) instead.

<span id="class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_EPOCH"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_THROTTLE_EPOCH** = `10`

The time at which throttle statistics were last updated (in milliseconds since the connection started). The interval for throttle statistics updates is [PEER_PACKET_THROTTLE_INTERVAL](class_enetpacketpeer.md#class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_INTERVAL).

<span id="class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_ACCELERATION"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_THROTTLE_ACCELERATION** = `11`

The throttle's acceleration factor. Higher values will make ENet adapt to fluctuating network conditions faster, causing unrelaible packets to be sent *more* often. The default value is `2`.

<span id="class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_DECELERATION"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_THROTTLE_DECELERATION** = `12`

The throttle's deceleration factor. Higher values will make ENet adapt to fluctuating network conditions faster, causing unrelaible packets to be sent *less* often. The default value is `2`.

<span id="class_ENetPacketPeer_constant_PEER_PACKET_THROTTLE_INTERVAL"></span>

[PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) **PEER_PACKET_THROTTLE_INTERVAL** = `13`

The interval over which the lowest mean round trip time should be measured for use by the throttle mechanism (in milliseconds). The default value is `5000`.

---

### Constants

<span id="class_ENetPacketPeer_constant_PACKET_LOSS_SCALE"></span>

**PACKET_LOSS_SCALE** = `65536` [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_constant_PACKET_LOSS_SCALE)

The reference scale for packet loss. See [get_statistic()](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_statistic) and [PEER_PACKET_LOSS](class_enetpacketpeer.md#class_ENetPacketPeer_constant_PEER_PACKET_LOSS).

<span id="class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE"></span>

**PACKET_THROTTLE_SCALE** = `32` [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE)

The reference value for throttle configuration. The default value is `32`. See [throttle_configure()](class_enetpacketpeer.md#class_ENetPacketPeer_method_throttle_configure).

<span id="class_ENetPacketPeer_constant_FLAG_RELIABLE"></span>

**FLAG_RELIABLE** = `1` [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_constant_FLAG_RELIABLE)

Mark the packet to be sent as reliable.

<span id="class_ENetPacketPeer_constant_FLAG_UNSEQUENCED"></span>

**FLAG_UNSEQUENCED** = `2` [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_constant_FLAG_UNSEQUENCED)

Mark the packet to be sent unsequenced (unreliable).

<span id="class_ENetPacketPeer_constant_FLAG_UNRELIABLE_FRAGMENT"></span>

**FLAG_UNRELIABLE_FRAGMENT** = `8` [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_constant_FLAG_UNRELIABLE_FRAGMENT)

Mark the packet to be sent unreliable even if the packet is too big and needs fragmentation (increasing the chance of it being dropped).

---

### Method Descriptions

<span id="class_ENetPacketPeer_method_get_channels"></span>

[int](class_int.md#class_int) **get_channels** ( ) *const* [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_channels)

Returns the number of channels allocated for communication with peer.

---

<span id="class_ENetPacketPeer_method_get_packet_flags"></span>

[int](class_int.md#class_int) **get_packet_flags** ( ) *const* [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_packet_flags)

Returns the ENet flags of the next packet in the received queue. See `FLAG_*` constants for available packet flags. Note that not all flags are replicated from the sending peer to the receiving peer.

---

<span id="class_ENetPacketPeer_method_get_remote_address"></span>

[String](class_string.md#class_String) **get_remote_address** ( ) *const* [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_remote_address)

Returns the IP address of this peer.

---

<span id="class_ENetPacketPeer_method_get_remote_port"></span>

[int](class_int.md#class_int) **get_remote_port** ( ) *const* [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_remote_port)

Returns the remote port of this peer.

---

<span id="class_ENetPacketPeer_method_get_state"></span>

[PeerState](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerState) **get_state** ( ) *const* [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_state)

Returns the current peer state.

---

<span id="class_ENetPacketPeer_method_get_statistic"></span>

[float](class_float.md#class_float) **get_statistic** ( statistic: [PeerStatistic](class_enetpacketpeer.md#enum_ENetPacketPeer_PeerStatistic) ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_get_statistic)

Returns the requested `statistic` for this peer.

---

<span id="class_ENetPacketPeer_method_is_active"></span>

[bool](class_bool.md#class_bool) **is_active** ( ) *const* [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_is_active)

Returns `true` if the peer is currently active (i.e. the associated [ENetConnection](class_enetconnection.md#class_ENetConnection) is still valid).

---

<span id="class_ENetPacketPeer_method_peer_disconnect"></span>

void **peer_disconnect** ( data: [int](class_int.md#class_int) = 0 ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_peer_disconnect)

Request a disconnection from a peer. An [ENetConnection.EVENT_DISCONNECT](class_enetconnection.md#class_ENetConnection_constant_EVENT_DISCONNECT) will be generated during [ENetConnection.service()](class_enetconnection.md#class_ENetConnection_method_service) once the disconnection is complete.

---

<span id="class_ENetPacketPeer_method_peer_disconnect_later"></span>

void **peer_disconnect_later** ( data: [int](class_int.md#class_int) = 0 ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_peer_disconnect_later)

Request a disconnection from a peer, but only after all queued outgoing packets are sent. An [ENetConnection.EVENT_DISCONNECT](class_enetconnection.md#class_ENetConnection_constant_EVENT_DISCONNECT) will be generated during [ENetConnection.service()](class_enetconnection.md#class_ENetConnection_method_service) once the disconnection is complete.

---

<span id="class_ENetPacketPeer_method_peer_disconnect_now"></span>

void **peer_disconnect_now** ( data: [int](class_int.md#class_int) = 0 ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_peer_disconnect_now)

Force an immediate disconnection from a peer. No [ENetConnection.EVENT_DISCONNECT](class_enetconnection.md#class_ENetConnection_constant_EVENT_DISCONNECT) will be generated. The foreign peer is not guaranteed to receive the disconnect notification, and is reset immediately upon return from this function.

---

<span id="class_ENetPacketPeer_method_ping"></span>

void **ping** ( ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_ping)

Sends a ping request to a peer. ENet automatically pings all connected peers at regular intervals, however, this function may be called to ensure more frequent ping requests.

---

<span id="class_ENetPacketPeer_method_ping_interval"></span>

void **ping_interval** ( ping_interval: [int](class_int.md#class_int) ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_ping_interval)

Sets the `ping_interval` in milliseconds at which pings will be sent to a peer. Pings are used both to monitor the liveness of the connection and also to dynamically adjust the throttle during periods of low traffic so that the throttle has reasonable responsiveness during traffic spikes. The default ping interval is `500` milliseconds.

---

<span id="class_ENetPacketPeer_method_reset"></span>

void **reset** ( ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_reset)

Forcefully disconnects a peer. The foreign host represented by the peer is not notified of the disconnection and will timeout on its connection to the local host.

---

<span id="class_ENetPacketPeer_method_send"></span>

Error **send** ( channel: [int](class_int.md#class_int), packet: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), flags: [int](class_int.md#class_int) ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_send)

Queues a `packet` to be sent over the specified `channel`. See `FLAG_*` constants for available packet flags.

---

<span id="class_ENetPacketPeer_method_set_timeout"></span>

void **set_timeout** ( timeout: [int](class_int.md#class_int), timeout_min: [int](class_int.md#class_int), timeout_max: [int](class_int.md#class_int) ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_set_timeout)

Sets the timeout parameters for a peer. The timeout parameters control how and when a peer will timeout from a failure to acknowledge reliable traffic. Timeout values are expressed in milliseconds.

The `timeout` is a factor that, multiplied by a value based on the average round trip time, will determine the timeout limit for a reliable packet. When that limit is reached, the timeout will be doubled, and the peer will be disconnected if that limit has reached `timeout_min`. The `timeout_max` parameter, on the other hand, defines a fixed timeout for which any packet must be acknowledged or the peer will be dropped.

---

<span id="class_ENetPacketPeer_method_throttle_configure"></span>

void **throttle_configure** ( interval: [int](class_int.md#class_int), acceleration: [int](class_int.md#class_int), deceleration: [int](class_int.md#class_int) ) [🔗](class_enetpacketpeer.md#class_ENetPacketPeer_method_throttle_configure)

Configures throttle parameter for a peer.

Unreliable packets are dropped by ENet in response to the varying conditions of the Internet connection to the peer. The throttle represents a probability that an unreliable packet should not be dropped and thus sent by ENet to the peer. By measuring fluctuations in round trip times of reliable packets over the specified `interval`, ENet will either increase the probability by the amount specified in the `acceleration` parameter, or decrease it by the amount specified in the `deceleration` parameter (both are ratios to [PACKET_THROTTLE_SCALE](class_enetpacketpeer.md#class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE)).

When the throttle has a value of [PACKET_THROTTLE_SCALE](class_enetpacketpeer.md#class_ENetPacketPeer_constant_PACKET_THROTTLE_SCALE), no unreliable packets are dropped by ENet, and so 100% of all unreliable packets will be sent.

When the throttle has a value of `0`, all unreliable packets are dropped by ENet, and so 0% of all unreliable packets will be sent.

Intermediate values for the throttle represent intermediate probabilities between 0% and 100% of unreliable packets being sent. The bandwidth limits of the local and foreign hosts are taken into account to determine a sensible limit for the throttle probability above which it should not raise even in the best of conditions.
