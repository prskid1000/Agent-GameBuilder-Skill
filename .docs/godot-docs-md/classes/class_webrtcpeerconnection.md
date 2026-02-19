<span id="class_WebRTCPeerConnection"></span>

## WebRTCPeerConnection

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [WebRTCPeerConnectionExtension](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension)

Interface to a WebRTC peer connection.

### Description

A WebRTC connection between the local computer and a remote peer. Provides an interface to connect, maintain, and monitor the connection.

Setting up a WebRTC connection between two peers may not seem a trivial task, but it can be broken down into 3 main steps:

- The peer that wants to initiate the connection (`A` from now on) creates an offer and sends it to the other peer (`B` from now on).

- `B` receives the offer, generates an answer, and sends it to `A`.

- `A` and `B` then generate and exchange ICE candidates with each other.

After these steps, the connection should be established. Refer to the linked tutorials for details.

### Tutorials

- [WebRTC documentation](../tutorials/networking/webrtc.md)

- [High-level multiplayer](../tutorials/networking/high_level_multiplayer.md)

### Methods


| Error | [add_ice_candidate](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_add_ice_candidate) ( media: [String](class_string.md#class_String), index: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| --- | --- |
| void | [close](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_close) ( ) |
| [WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel) | [create_data_channel](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_data_channel) ( label: [String](class_string.md#class_String), options: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) |
| Error | [create_offer](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_offer) ( ) |
| [ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) | [get_connection_state](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_get_connection_state) ( ) const |
| [GatheringState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_GatheringState) | [get_gathering_state](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_get_gathering_state) ( ) const |
| [SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) | [get_signaling_state](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_get_signaling_state) ( ) const |
| Error | [initialize](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_initialize) ( configuration: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) |
| Error | [poll](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_poll) ( ) |
| void | [set_default_extension](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_default_extension) ( extension_class: [StringName](class_stringname.md#class_StringName) ) static |
| Error | [set_local_description](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_local_description) ( type: [String](class_string.md#class_String), sdp: [String](class_string.md#class_String) ) |
| Error | [set_remote_description](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_remote_description) ( type: [String](class_string.md#class_String), sdp: [String](class_string.md#class_String) ) |

---

### Signals

<span id="class_WebRTCPeerConnection_signal_data_channel_received"></span>

**data_channel_received** ( channel: [WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel) ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_data_channel_received)

Emitted when a new in-band channel is received, i.e. when the channel was created with `negotiated: false` (default).

The object will be an instance of [WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel). You must keep a reference of it or it will be closed automatically. See [create_data_channel()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_data_channel).

---

<span id="class_WebRTCPeerConnection_signal_ice_candidate_created"></span>

**ice_candidate_created** ( media: [String](class_string.md#class_String), index: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_ice_candidate_created)

Emitted when a new ICE candidate has been created. The three parameters are meant to be passed to the remote peer over the signaling server.

---

<span id="class_WebRTCPeerConnection_signal_session_description_created"></span>

**session_description_created** ( type: [String](class_string.md#class_String), sdp: [String](class_string.md#class_String) ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_session_description_created)

Emitted after a successful call to [create_offer()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_offer) or [set_remote_description()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_remote_description) (when it generates an answer). The parameters are meant to be passed to [set_local_description()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_local_description) on this object, and sent to the remote peer over the signaling server.

---

### Enumerations

<span id="enum_WebRTCPeerConnection_ConnectionState"></span>

enum **ConnectionState**: [🔗](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState)

<span id="class_WebRTCPeerConnection_constant_STATE_NEW"></span>

[ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) **STATE_NEW** = `0`

The connection is new, data channels and an offer can be created in this state.

<span id="class_WebRTCPeerConnection_constant_STATE_CONNECTING"></span>

[ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) **STATE_CONNECTING** = `1`

The peer is connecting, ICE is in progress, none of the transports has failed.

<span id="class_WebRTCPeerConnection_constant_STATE_CONNECTED"></span>

[ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) **STATE_CONNECTED** = `2`

The peer is connected, all ICE transports are connected.

<span id="class_WebRTCPeerConnection_constant_STATE_DISCONNECTED"></span>

[ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) **STATE_DISCONNECTED** = `3`

At least one ICE transport is disconnected.

<span id="class_WebRTCPeerConnection_constant_STATE_FAILED"></span>

[ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) **STATE_FAILED** = `4`

One or more of the ICE transports failed.

<span id="class_WebRTCPeerConnection_constant_STATE_CLOSED"></span>

[ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) **STATE_CLOSED** = `5`

The peer connection is closed (after calling [close()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_close) for example).

---

<span id="enum_WebRTCPeerConnection_GatheringState"></span>

enum **GatheringState**: [🔗](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_GatheringState)

<span id="class_WebRTCPeerConnection_constant_GATHERING_STATE_NEW"></span>

[GatheringState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_GatheringState) **GATHERING_STATE_NEW** = `0`

The peer connection was just created and hasn't done any networking yet.

<span id="class_WebRTCPeerConnection_constant_GATHERING_STATE_GATHERING"></span>

[GatheringState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_GatheringState) **GATHERING_STATE_GATHERING** = `1`

The ICE agent is in the process of gathering candidates for the connection.

<span id="class_WebRTCPeerConnection_constant_GATHERING_STATE_COMPLETE"></span>

[GatheringState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_GatheringState) **GATHERING_STATE_COMPLETE** = `2`

The ICE agent has finished gathering candidates. If something happens that requires collecting new candidates, such as a new interface being added or the addition of a new ICE server, the state will revert to gathering to gather those candidates.

---

<span id="enum_WebRTCPeerConnection_SignalingState"></span>

enum **SignalingState**: [🔗](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState)

<span id="class_WebRTCPeerConnection_constant_SIGNALING_STATE_STABLE"></span>

[SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) **SIGNALING_STATE_STABLE** = `0`

There is no ongoing exchange of offer and answer underway. This may mean that the **WebRTCPeerConnection** is new ([STATE_NEW](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_constant_STATE_NEW)) or that negotiation is complete and a connection has been established ([STATE_CONNECTED](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_constant_STATE_CONNECTED)).

<span id="class_WebRTCPeerConnection_constant_SIGNALING_STATE_HAVE_LOCAL_OFFER"></span>

[SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) **SIGNALING_STATE_HAVE_LOCAL_OFFER** = `1`

The local peer has called [set_local_description()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_local_description), passing in SDP representing an offer (usually created by calling [create_offer()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_offer)), and the offer has been applied successfully.

<span id="class_WebRTCPeerConnection_constant_SIGNALING_STATE_HAVE_REMOTE_OFFER"></span>

[SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) **SIGNALING_STATE_HAVE_REMOTE_OFFER** = `2`

The remote peer has created an offer and used the signaling server to deliver it to the local peer, which has set the offer as the remote description by calling [set_remote_description()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_remote_description).

<span id="class_WebRTCPeerConnection_constant_SIGNALING_STATE_HAVE_LOCAL_PRANSWER"></span>

[SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) **SIGNALING_STATE_HAVE_LOCAL_PRANSWER** = `3`

The offer sent by the remote peer has been applied and an answer has been created and applied by calling [set_local_description()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_local_description). This provisional answer describes the supported media formats and so forth, but may not have a complete set of ICE candidates included. Further candidates will be delivered separately later.

<span id="class_WebRTCPeerConnection_constant_SIGNALING_STATE_HAVE_REMOTE_PRANSWER"></span>

[SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) **SIGNALING_STATE_HAVE_REMOTE_PRANSWER** = `4`

A provisional answer has been received and successfully applied in response to an offer previously sent and established by calling [set_local_description()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_local_description).

<span id="class_WebRTCPeerConnection_constant_SIGNALING_STATE_CLOSED"></span>

[SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) **SIGNALING_STATE_CLOSED** = `5`

The **WebRTCPeerConnection** has been closed.

---

### Method Descriptions

<span id="class_WebRTCPeerConnection_method_add_ice_candidate"></span>

Error **add_ice_candidate** ( media: [String](class_string.md#class_String), index: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_add_ice_candidate)

Add an ice candidate generated by a remote peer (and received over the signaling server). See [ice_candidate_created](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_ice_candidate_created).

---

<span id="class_WebRTCPeerConnection_method_close"></span>

void **close** ( ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_close)

Close the peer connection and all data channels associated with it.

 **Note:** You cannot reuse this object for a new connection unless you call [initialize()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_initialize).

---

<span id="class_WebRTCPeerConnection_method_create_data_channel"></span>

[WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel) **create_data_channel** ( label: [String](class_string.md#class_String), options: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_data_channel)

Returns a new [WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel) (or `null` on failure) with given `label` and optionally configured via the `options` dictionary. This method can only be called when the connection is in state [STATE_NEW](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_constant_STATE_NEW).

There are two ways to create a working data channel: either call [create_data_channel()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_data_channel) on only one of the peer and listen to [data_channel_received](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_data_channel_received) on the other, or call [create_data_channel()](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_data_channel) on both peers, with the same values, and the `"negotiated"` option set to `true`.

Valid `options` are:

::

    {
        "negotiated": true, # When set to true (default off), means the channel is negotiated out of band. "id" must be set too. "data_channel_received" will not be called.
        "id": 1, # When "negotiated" is true this value must also be set to the same value on both peer.

        # Only one of maxRetransmits and maxPacketLifeTime can be specified, not both. They make the channel unreliable (but also better at real time).
        "maxRetransmits": 1, # Specify the maximum number of attempt the peer will make to retransmits packets if they are not acknowledged.
        "maxPacketLifeTime": 100, # Specify the maximum amount of time before giving up retransmitions of unacknowledged packets (in milliseconds).
        "ordered": true, # When in unreliable mode (i.e. either "maxRetransmits" or "maxPacketLifetime" is set), "ordered" (true by default) specify if packet ordering is to be enforced.

        "protocol": "my-custom-protocol", # A custom sub-protocol string for this channel.
    }

 **Note:** You must keep a reference to channels created this way, or it will be closed.

---

<span id="class_WebRTCPeerConnection_method_create_offer"></span>

Error **create_offer** ( ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_create_offer)

Creates a new SDP offer to start a WebRTC connection with a remote peer. At least one [WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel) must have been created before calling this method.

If this functions returns @GlobalScope.OK, [session_description_created](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_session_description_created) will be called when the session is ready to be sent.

---

<span id="class_WebRTCPeerConnection_method_get_connection_state"></span>

[ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) **get_connection_state** ( ) *const* [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_get_connection_state)

Returns the connection state.

---

<span id="class_WebRTCPeerConnection_method_get_gathering_state"></span>

[GatheringState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_GatheringState) **get_gathering_state** ( ) *const* [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_get_gathering_state)

Returns the ICE [GatheringState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_GatheringState) of the connection. This lets you detect, for example, when collection of ICE candidates has finished.

---

<span id="class_WebRTCPeerConnection_method_get_signaling_state"></span>

[SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) **get_signaling_state** ( ) *const* [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_get_signaling_state)

Returns the signaling state on the local end of the connection while connecting or reconnecting to another peer.

---

<span id="class_WebRTCPeerConnection_method_initialize"></span>

Error **initialize** ( configuration: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_initialize)

Re-initialize this peer connection, closing any previously active connection, and going back to state [STATE_NEW](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_constant_STATE_NEW). A dictionary of `configuration` options can be passed to configure the peer connection.

Valid `configuration` options are:

::

    {
        "iceServers": [
            {
                "urls": [ "stun:stun.example.com:3478" ], # One or more STUN servers.
            },
            {
                "urls": [ "turn:turn.example.com:3478" ], # One or more TURN servers.
                "username": "a_username", # Optional username for the TURN server.
                "credential": "a_password", # Optional password for the TURN server.
            }
        ]
    }

---

<span id="class_WebRTCPeerConnection_method_poll"></span>

Error **poll** ( ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_poll)

Call this method frequently (e.g. in [Node._process()](class_node.md#class_Node_private_method__process) or [Node._physics_process()](class_node.md#class_Node_private_method__physics_process)) to properly receive signals.

---

<span id="class_WebRTCPeerConnection_method_set_default_extension"></span>

void **set_default_extension** ( extension_class: [StringName](class_stringname.md#class_StringName) ) *static* [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_default_extension)

Sets the `extension_class` as the default [WebRTCPeerConnectionExtension](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension) returned when creating a new **WebRTCPeerConnection**.

---

<span id="class_WebRTCPeerConnection_method_set_local_description"></span>

Error **set_local_description** ( type: [String](class_string.md#class_String), sdp: [String](class_string.md#class_String) ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_local_description)

Sets the SDP description of the local peer. This should be called in response to [session_description_created](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_session_description_created).

After calling this function the peer will start emitting [ice_candidate_created](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_ice_candidate_created) (unless an Error different from @GlobalScope.OK is returned).

---

<span id="class_WebRTCPeerConnection_method_set_remote_description"></span>

Error **set_remote_description** ( type: [String](class_string.md#class_String), sdp: [String](class_string.md#class_String) ) [🔗](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_method_set_remote_description)

Sets the SDP description of the remote peer. This should be called with the values generated by a remote peer and received over the signaling server.

If `type` is `"offer"` the peer will emit [session_description_created](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_session_description_created) with the appropriate answer.

If `type` is `"answer"` the peer will start emitting [ice_candidate_created](class_webrtcpeerconnection.md#class_WebRTCPeerConnection_signal_ice_candidate_created).
