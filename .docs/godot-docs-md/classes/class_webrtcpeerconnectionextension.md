<span id="class_WebRTCPeerConnectionExtension"></span>

## WebRTCPeerConnectionExtension

**Inherits:** [WebRTCPeerConnection](class_webrtcpeerconnection.md#class_WebRTCPeerConnection) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

.. container:: contribute

	There is currently no description for this class. Please help us by contributing one!

### Methods


| Error | [_add_ice_candidate](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__add_ice_candidate) ( p_sdp_mid_name: [String](class_string.md#class_String), p_sdp_mline_index: [int](class_int.md#class_int), p_sdp_name: [String](class_string.md#class_String) ) | virtual | required |
| --- | --- | --- | --- |
| void | [_close](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__close) ( ) | virtual | required |
| [WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel) | [_create_data_channel](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__create_data_channel) ( p_label: [String](class_string.md#class_String), p_config: [Dictionary](class_dictionary.md#class_Dictionary) ) | virtual | required |
| Error | [_create_offer](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__create_offer) ( ) | virtual | required |
| [ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) | [_get_connection_state](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__get_connection_state) ( ) | virtual | required | const |
| [GatheringState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_GatheringState) | [_get_gathering_state](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__get_gathering_state) ( ) | virtual | required | const |
| [SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) | [_get_signaling_state](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__get_signaling_state) ( ) | virtual | required | const |
| Error | [_initialize](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__initialize) ( p_config: [Dictionary](class_dictionary.md#class_Dictionary) ) | virtual | required |
| Error | [_poll](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__poll) ( ) | virtual | required |
| Error | [_set_local_description](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__set_local_description) ( p_type: [String](class_string.md#class_String), p_sdp: [String](class_string.md#class_String) ) | virtual | required |
| Error | [_set_remote_description](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__set_remote_description) ( p_type: [String](class_string.md#class_String), p_sdp: [String](class_string.md#class_String) ) | virtual | required |

---

### Method Descriptions

<span id="class_WebRTCPeerConnectionExtension_private_method__add_ice_candidate"></span>

Error **_add_ice_candidate** ( p_sdp_mid_name: [String](class_string.md#class_String), p_sdp_mline_index: [int](class_int.md#class_int), p_sdp_name: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__add_ice_candidate)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__close"></span>

void **_close** ( ) *virtual* |required| [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__close)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__create_data_channel"></span>

[WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel) **_create_data_channel** ( p_label: [String](class_string.md#class_String), p_config: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* |required| [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__create_data_channel)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__create_offer"></span>

Error **_create_offer** ( ) *virtual* |required| [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__create_offer)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__get_connection_state"></span>

[ConnectionState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_ConnectionState) **_get_connection_state** ( ) *virtual* |required| *const* [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__get_connection_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__get_gathering_state"></span>

[GatheringState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_GatheringState) **_get_gathering_state** ( ) *virtual* |required| *const* [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__get_gathering_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__get_signaling_state"></span>

[SignalingState](class_webrtcpeerconnection.md#enum_WebRTCPeerConnection_SignalingState) **_get_signaling_state** ( ) *virtual* |required| *const* [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__get_signaling_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__initialize"></span>

Error **_initialize** ( p_config: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* |required| [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__initialize)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__poll"></span>

Error **_poll** ( ) *virtual* |required| [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__poll)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__set_local_description"></span>

Error **_set_local_description** ( p_type: [String](class_string.md#class_String), p_sdp: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__set_local_description)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCPeerConnectionExtension_private_method__set_remote_description"></span>

Error **_set_remote_description** ( p_type: [String](class_string.md#class_String), p_sdp: [String](class_string.md#class_String) ) *virtual* |required| [🔗](class_webrtcpeerconnectionextension.md#class_WebRTCPeerConnectionExtension_private_method__set_remote_description)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
