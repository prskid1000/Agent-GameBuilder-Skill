.. meta::
	:keywords: network

<span id="class_MultiplayerPeerExtension"></span>

## MultiplayerPeerExtension

**Inherits:** [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) **<** [PacketPeer](class_packetpeer.md#class_PacketPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Class that can be inherited to implement custom multiplayer API networking layers via GDExtension.

### Description

This class is designed to be inherited from a GDExtension plugin to implement custom networking layers for the multiplayer API (such as WebRTC). All the methods below **must** be implemented to have a working custom multiplayer implementation. See also [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI).

### Methods


| void | [_close](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__close) ( ) | virtual | required |
| --- | --- | --- | --- |
| void | [_disconnect_peer](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__disconnect_peer) ( p_peer: [int](class_int.md#class_int), p_force: [bool](class_bool.md#class_bool) ) | virtual | required |
| [int](class_int.md#class_int) | [_get_available_packet_count](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_available_packet_count) ( ) | virtual | required | const |
| [ConnectionStatus](class_multiplayerpeer.md#enum_MultiplayerPeer_ConnectionStatus) | [_get_connection_status](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_connection_status) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_max_packet_size](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_max_packet_size) ( ) | virtual | required | const |
| Error | [_get_packet](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet) ( r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*` ) virtual |
| [int](class_int.md#class_int) | [_get_packet_channel](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet_channel) ( ) | virtual | required | const |
| [TransferMode](class_multiplayerpeer.md#enum_MultiplayerPeer_TransferMode) | [_get_packet_mode](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet_mode) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_packet_peer](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet_peer) ( ) | virtual | required | const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [_get_packet_script](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet_script) ( ) virtual |
| [int](class_int.md#class_int) | [_get_transfer_channel](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_transfer_channel) ( ) | virtual | required | const |
| [TransferMode](class_multiplayerpeer.md#enum_MultiplayerPeer_TransferMode) | [_get_transfer_mode](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_transfer_mode) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_unique_id](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_unique_id) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_refusing_new_connections](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__is_refusing_new_connections) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_server](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__is_server) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_server_relay_supported](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__is_server_relay_supported) ( ) | virtual | const |
| void | [_poll](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__poll) ( ) | virtual | required |
| Error | [_put_packet](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__put_packet) ( p_buffer: `const uint8_t*`, p_buffer_size: [int](class_int.md#class_int) ) virtual |
| Error | [_put_packet_script](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__put_packet_script) ( p_buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) virtual |
| void | [_set_refuse_new_connections](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__set_refuse_new_connections) ( p_enable: [bool](class_bool.md#class_bool) ) virtual |
| void | [_set_target_peer](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__set_target_peer) ( p_peer: [int](class_int.md#class_int) ) | virtual | required |
| void | [_set_transfer_channel](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__set_transfer_channel) ( p_channel: [int](class_int.md#class_int) ) | virtual | required |
| void | [_set_transfer_mode](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__set_transfer_mode) ( p_mode: [TransferMode](class_multiplayerpeer.md#enum_MultiplayerPeer_TransferMode) ) | virtual | required |

---

### Method Descriptions

<span id="class_MultiplayerPeerExtension_private_method__close"></span>

void **_close** ( ) *virtual* |required| [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__close)

Called when the multiplayer peer should be immediately closed (see [MultiplayerPeer.close()](class_multiplayerpeer.md#class_MultiplayerPeer_method_close)).

---

<span id="class_MultiplayerPeerExtension_private_method__disconnect_peer"></span>

void **_disconnect_peer** ( p_peer: [int](class_int.md#class_int), p_force: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__disconnect_peer)

Called when the connected `p_peer` should be forcibly disconnected (see [MultiplayerPeer.disconnect_peer()](class_multiplayerpeer.md#class_MultiplayerPeer_method_disconnect_peer)).

---

<span id="class_MultiplayerPeerExtension_private_method__get_available_packet_count"></span>

[int](class_int.md#class_int) **_get_available_packet_count** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_available_packet_count)

Called when the available packet count is internally requested by the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI).

---

<span id="class_MultiplayerPeerExtension_private_method__get_connection_status"></span>

[ConnectionStatus](class_multiplayerpeer.md#enum_MultiplayerPeer_ConnectionStatus) **_get_connection_status** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_connection_status)

Called when the connection status is requested on the [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) (see [MultiplayerPeer.get_connection_status()](class_multiplayerpeer.md#class_MultiplayerPeer_method_get_connection_status)).

---

<span id="class_MultiplayerPeerExtension_private_method__get_max_packet_size"></span>

[int](class_int.md#class_int) **_get_max_packet_size** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_max_packet_size)

Called when the maximum allowed packet size (in bytes) is requested by the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI).

---

<span id="class_MultiplayerPeerExtension_private_method__get_packet"></span>

Error **_get_packet** ( r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*` ) *virtual* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet)

Called when a packet needs to be received by the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI), with `r_buffer_size` being the size of the binary `r_buffer` in bytes.

---

<span id="class_MultiplayerPeerExtension_private_method__get_packet_channel"></span>

[int](class_int.md#class_int) **_get_packet_channel** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet_channel)

Called to get the channel over which the next available packet was received. See [MultiplayerPeer.get_packet_channel()](class_multiplayerpeer.md#class_MultiplayerPeer_method_get_packet_channel).

---

<span id="class_MultiplayerPeerExtension_private_method__get_packet_mode"></span>

[TransferMode](class_multiplayerpeer.md#enum_MultiplayerPeer_TransferMode) **_get_packet_mode** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet_mode)

Called to get the transfer mode the remote peer used to send the next available packet. See [MultiplayerPeer.get_packet_mode()](class_multiplayerpeer.md#class_MultiplayerPeer_method_get_packet_mode).

---

<span id="class_MultiplayerPeerExtension_private_method__get_packet_peer"></span>

[int](class_int.md#class_int) **_get_packet_peer** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet_peer)

Called when the ID of the [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) who sent the most recent packet is requested (see [MultiplayerPeer.get_packet_peer()](class_multiplayerpeer.md#class_MultiplayerPeer_method_get_packet_peer)).

---

<span id="class_MultiplayerPeerExtension_private_method__get_packet_script"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **_get_packet_script** ( ) *virtual* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet_script)

Called when a packet needs to be received by the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI), if [_get_packet()](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_packet) isn't implemented. Use this when extending this class via GDScript.

---

<span id="class_MultiplayerPeerExtension_private_method__get_transfer_channel"></span>

[int](class_int.md#class_int) **_get_transfer_channel** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_transfer_channel)

Called when the transfer channel to use is read on this [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) (see [MultiplayerPeer.transfer_channel](class_multiplayerpeer.md#class_MultiplayerPeer_property_transfer_channel)).

---

<span id="class_MultiplayerPeerExtension_private_method__get_transfer_mode"></span>

[TransferMode](class_multiplayerpeer.md#enum_MultiplayerPeer_TransferMode) **_get_transfer_mode** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_transfer_mode)

Called when the transfer mode to use is read on this [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) (see [MultiplayerPeer.transfer_mode](class_multiplayerpeer.md#class_MultiplayerPeer_property_transfer_mode)).

---

<span id="class_MultiplayerPeerExtension_private_method__get_unique_id"></span>

[int](class_int.md#class_int) **_get_unique_id** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__get_unique_id)

Called when the unique ID of this [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) is requested (see [MultiplayerPeer.get_unique_id()](class_multiplayerpeer.md#class_MultiplayerPeer_method_get_unique_id)). The value must be between `1` and `2147483647`.

---

<span id="class_MultiplayerPeerExtension_private_method__is_refusing_new_connections"></span>

[bool](class_bool.md#class_bool) **_is_refusing_new_connections** ( ) *virtual* *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__is_refusing_new_connections)

Called when the "refuse new connections" status is requested on this [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) (see [MultiplayerPeer.refuse_new_connections](class_multiplayerpeer.md#class_MultiplayerPeer_property_refuse_new_connections)).

---

<span id="class_MultiplayerPeerExtension_private_method__is_server"></span>

[bool](class_bool.md#class_bool) **_is_server** ( ) *virtual* |required| *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__is_server)

Called when the "is server" status is requested on the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI). See [MultiplayerAPI.is_server()](class_multiplayerapi.md#class_MultiplayerAPI_method_is_server).

---

<span id="class_MultiplayerPeerExtension_private_method__is_server_relay_supported"></span>

[bool](class_bool.md#class_bool) **_is_server_relay_supported** ( ) *virtual* *const* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__is_server_relay_supported)

Called to check if the server can act as a relay in the current configuration. See [MultiplayerPeer.is_server_relay_supported()](class_multiplayerpeer.md#class_MultiplayerPeer_method_is_server_relay_supported).

---

<span id="class_MultiplayerPeerExtension_private_method__poll"></span>

void **_poll** ( ) *virtual* |required| [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__poll)

Called when the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) is polled. See [MultiplayerAPI.poll()](class_multiplayerapi.md#class_MultiplayerAPI_method_poll).

---

<span id="class_MultiplayerPeerExtension_private_method__put_packet"></span>

Error **_put_packet** ( p_buffer: `const uint8_t*`, p_buffer_size: [int](class_int.md#class_int) ) *virtual* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__put_packet)

Called when a packet needs to be sent by the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI), with `p_buffer_size` being the size of the binary `p_buffer` in bytes.

---

<span id="class_MultiplayerPeerExtension_private_method__put_packet_script"></span>

Error **_put_packet_script** ( p_buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) *virtual* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__put_packet_script)

Called when a packet needs to be sent by the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI), if [_put_packet()](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__put_packet) isn't implemented. Use this when extending this class via GDScript.

---

<span id="class_MultiplayerPeerExtension_private_method__set_refuse_new_connections"></span>

void **_set_refuse_new_connections** ( p_enable: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__set_refuse_new_connections)

Called when the "refuse new connections" status is set on this [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) (see [MultiplayerPeer.refuse_new_connections](class_multiplayerpeer.md#class_MultiplayerPeer_property_refuse_new_connections)).

---

<span id="class_MultiplayerPeerExtension_private_method__set_target_peer"></span>

void **_set_target_peer** ( p_peer: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__set_target_peer)

Called when the target peer to use is set for this [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) (see [MultiplayerPeer.set_target_peer()](class_multiplayerpeer.md#class_MultiplayerPeer_method_set_target_peer)).

---

<span id="class_MultiplayerPeerExtension_private_method__set_transfer_channel"></span>

void **_set_transfer_channel** ( p_channel: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__set_transfer_channel)

Called when the channel to use is set for this [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) (see [MultiplayerPeer.transfer_channel](class_multiplayerpeer.md#class_MultiplayerPeer_property_transfer_channel)).

---

<span id="class_MultiplayerPeerExtension_private_method__set_transfer_mode"></span>

void **_set_transfer_mode** ( p_mode: [TransferMode](class_multiplayerpeer.md#enum_MultiplayerPeer_TransferMode) ) *virtual* |required| [🔗](class_multiplayerpeerextension.md#class_MultiplayerPeerExtension_private_method__set_transfer_mode)

Called when the transfer mode is set on this [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) (see [MultiplayerPeer.transfer_mode](class_multiplayerpeer.md#class_MultiplayerPeer_property_transfer_mode)).
