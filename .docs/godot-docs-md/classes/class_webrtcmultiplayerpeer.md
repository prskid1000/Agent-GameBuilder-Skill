<span id="class_WebRTCMultiplayerPeer"></span>

## WebRTCMultiplayerPeer

**Inherits:** [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) **<** [PacketPeer](class_packetpeer.md#class_PacketPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A simple interface to create a peer-to-peer mesh network composed of [WebRTCPeerConnection](class_webrtcpeerconnection.md#class_WebRTCPeerConnection) that is compatible with the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI).

### Description

This class constructs a full mesh of [WebRTCPeerConnection](class_webrtcpeerconnection.md#class_WebRTCPeerConnection) (one connection for each peer) that can be used as a [MultiplayerAPI.multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer).

You can add each [WebRTCPeerConnection](class_webrtcpeerconnection.md#class_WebRTCPeerConnection) via [add_peer()](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_add_peer) or remove them via [remove_peer()](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_remove_peer). Peers must be added in [WebRTCPeerConnection.STATE_NEW](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_constant_STATE_NEW) state to allow it to create the appropriate channels. This class will not create offers nor set descriptions, it will only poll them, and notify connections and disconnections.

When creating the peer via [create_client()](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_create_client) or [create_server()](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_create_server) the [MultiplayerPeer.is_server_relay_supported()](class_multiplayerpeer.md#class_MultiplayerPeer_method_is_server_relay_supported) method will return `true` enabling peer exchange and packet relaying when supported by the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) implementation.

 **Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

### Methods


| Error | [add_peer](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_add_peer) ( peer: [WebRTCPeerConnection](class_webrtcpeerconnection.md#class_WebRTCPeerConnection), peer_id: [int](class_int.md#class_int), unreliable_lifetime: [int](class_int.md#class_int) = 1 ) |
| --- | --- |
| Error | [create_client](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_create_client) ( peer_id: [int](class_int.md#class_int), channels_config: [Array](class_array.md#class_Array) = [] ) |
| Error | [create_mesh](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_create_mesh) ( peer_id: [int](class_int.md#class_int), channels_config: [Array](class_array.md#class_Array) = [] ) |
| Error | [create_server](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_create_server) ( channels_config: [Array](class_array.md#class_Array) = [] ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_peer](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_get_peer) ( peer_id: [int](class_int.md#class_int) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_peers](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_get_peers) ( ) |
| [bool](class_bool.md#class_bool) | [has_peer](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_has_peer) ( peer_id: [int](class_int.md#class_int) ) |
| void | [remove_peer](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_remove_peer) ( peer_id: [int](class_int.md#class_int) ) |

---

### Method Descriptions

<span id="class_WebRTCMultiplayerPeer_method_add_peer"></span>

Error **add_peer** ( peer: [WebRTCPeerConnection](class_webrtcpeerconnection.md#class_WebRTCPeerConnection), peer_id: [int](class_int.md#class_int), unreliable_lifetime: [int](class_int.md#class_int) = 1 ) [🔗](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_add_peer)

Add a new peer to the mesh with the given `peer_id`. The [WebRTCPeerConnection](class_webrtcpeerconnection.md#class_WebRTCPeerConnection) must be in state [WebRTCPeerConnection.STATE_NEW](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_constant_STATE_NEW).

Three channels will be created for reliable, unreliable, and ordered transport. The value of `unreliable_lifetime` will be passed to the `"maxPacketLifetime"` option when creating unreliable and ordered channels (see [WebRTCPeerConnection.create_data_channel()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_data_channel)).

---

<span id="class_WebRTCMultiplayerPeer_method_create_client"></span>

Error **create_client** ( peer_id: [int](class_int.md#class_int), channels_config: [Array](class_array.md#class_Array) = [] ) [🔗](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_create_client)

Initialize the multiplayer peer as a client with the given `peer_id` (must be between 2 and 2147483647). In this mode, you should only call [add_peer()](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_add_peer) once and with `peer_id` of `1`. This mode enables [MultiplayerPeer.is_server_relay_supported()](class_multiplayerpeer.md#class_MultiplayerPeer_method_is_server_relay_supported), allowing the upper [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) layer to perform peer exchange and packet relaying.

You can optionally specify a `channels_config` array of [TransferMode](class_multiplayerpeer.md#enum_MultiplayerPeer_TransferMode) which will be used to create extra channels (WebRTC only supports one transfer mode per channel).

---

<span id="class_WebRTCMultiplayerPeer_method_create_mesh"></span>

Error **create_mesh** ( peer_id: [int](class_int.md#class_int), channels_config: [Array](class_array.md#class_Array) = [] ) [🔗](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_create_mesh)

Initialize the multiplayer peer as a mesh (i.e. all peers connect to each other) with the given `peer_id` (must be between 1 and 2147483647).

---

<span id="class_WebRTCMultiplayerPeer_method_create_server"></span>

Error **create_server** ( channels_config: [Array](class_array.md#class_Array) = [] ) [🔗](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_create_server)

Initialize the multiplayer peer as a server (with unique ID of `1`). This mode enables [MultiplayerPeer.is_server_relay_supported()](class_multiplayerpeer.md#class_MultiplayerPeer_method_is_server_relay_supported), allowing the upper [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) layer to perform peer exchange and packet relaying.

You can optionally specify a `channels_config` array of [TransferMode](class_multiplayerpeer.md#enum_MultiplayerPeer_TransferMode) which will be used to create extra channels (WebRTC only supports one transfer mode per channel).

---

<span id="class_WebRTCMultiplayerPeer_method_get_peer"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_peer** ( peer_id: [int](class_int.md#class_int) ) [🔗](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_get_peer)

Returns a dictionary representation of the peer with given `peer_id` with three keys. `"connection"` containing the [WebRTCPeerConnection](class_webrtcpeerconnection.md#class_WebRTCPeerConnection) to this peer, `"channels"` an array of three [WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel), and `"connected"` a boolean representing if the peer connection is currently connected (all three channels are open).

---

<span id="class_WebRTCMultiplayerPeer_method_get_peers"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_peers** ( ) [🔗](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_get_peers)

Returns a dictionary which keys are the peer ids and values the peer representation as in [get_peer()](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_get_peer).

---

<span id="class_WebRTCMultiplayerPeer_method_has_peer"></span>

[bool](class_bool.md#class_bool) **has_peer** ( peer_id: [int](class_int.md#class_int) ) [🔗](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_has_peer)

Returns `true` if the given `peer_id` is in the peers map (it might not be connected though).

---

<span id="class_WebRTCMultiplayerPeer_method_remove_peer"></span>

void **remove_peer** ( peer_id: [int](class_int.md#class_int) ) [🔗](class_webrtcmultiplayerpeer.md#class_WebRTCMultiplayerPeer_method_remove_peer)

Remove the peer with given `peer_id` from the mesh. If the peer was connected, and [MultiplayerPeer.peer_connected](class_multiplayerpeer.md#class_MultiplayerPeer_signal_peer_connected) was emitted for it, then [MultiplayerPeer.peer_disconnected](class_multiplayerpeer.md#class_MultiplayerPeer_signal_peer_disconnected) will be emitted.
