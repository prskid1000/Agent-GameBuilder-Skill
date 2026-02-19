<span id="class_WebRTCDataChannelExtension"></span>

## WebRTCDataChannelExtension

**Inherits:** [WebRTCDataChannel](class_webrtcdatachannel.md#class_WebRTCDataChannel) **<** [PacketPeer](class_packetpeer.md#class_PacketPeer) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

.. container:: contribute

	There is currently no description for this class. Please help us by contributing one!

### Methods


| void | [_close](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__close) ( ) | virtual | required |
| --- | --- | --- | --- |
| [int](class_int.md#class_int) | [_get_available_packet_count](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_available_packet_count) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_buffered_amount](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_buffered_amount) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_id](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_id) ( ) | virtual | required | const |
| [String](class_string.md#class_String) | [_get_label](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_label) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_max_packet_life_time](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_max_packet_life_time) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_max_packet_size](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_max_packet_size) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_max_retransmits](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_max_retransmits) ( ) | virtual | required | const |
| Error | [_get_packet](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_packet) ( r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*` ) virtual |
| [String](class_string.md#class_String) | [_get_protocol](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_protocol) ( ) | virtual | required | const |
| [ChannelState](class_webrtcdatachannel.md#enum_WebRTCDataChannel_ChannelState) | [_get_ready_state](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_ready_state) ( ) | virtual | required | const |
| [WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) | [_get_write_mode](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_write_mode) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_negotiated](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__is_negotiated) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_ordered](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__is_ordered) ( ) | virtual | required | const |
| Error | [_poll](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__poll) ( ) | virtual | required |
| Error | [_put_packet](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__put_packet) ( p_buffer: `const uint8_t*`, p_buffer_size: [int](class_int.md#class_int) ) virtual |
| void | [_set_write_mode](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__set_write_mode) ( p_write_mode: [WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_was_string_packet](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__was_string_packet) ( ) | virtual | required | const |

---

### Method Descriptions

<span id="class_WebRTCDataChannelExtension_private_method__close"></span>

void **_close** ( ) *virtual* |required| [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__close)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_available_packet_count"></span>

[int](class_int.md#class_int) **_get_available_packet_count** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_available_packet_count)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_buffered_amount"></span>

[int](class_int.md#class_int) **_get_buffered_amount** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_buffered_amount)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_id"></span>

[int](class_int.md#class_int) **_get_id** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_id)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_label"></span>

[String](class_string.md#class_String) **_get_label** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_label)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_max_packet_life_time"></span>

[int](class_int.md#class_int) **_get_max_packet_life_time** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_max_packet_life_time)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_max_packet_size"></span>

[int](class_int.md#class_int) **_get_max_packet_size** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_max_packet_size)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_max_retransmits"></span>

[int](class_int.md#class_int) **_get_max_retransmits** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_max_retransmits)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_packet"></span>

Error **_get_packet** ( r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*` ) *virtual* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_packet)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_protocol"></span>

[String](class_string.md#class_String) **_get_protocol** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_protocol)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_ready_state"></span>

[ChannelState](class_webrtcdatachannel.md#enum_WebRTCDataChannel_ChannelState) **_get_ready_state** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_ready_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__get_write_mode"></span>

[WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) **_get_write_mode** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__get_write_mode)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__is_negotiated"></span>

[bool](class_bool.md#class_bool) **_is_negotiated** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__is_negotiated)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__is_ordered"></span>

[bool](class_bool.md#class_bool) **_is_ordered** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__is_ordered)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__poll"></span>

Error **_poll** ( ) *virtual* |required| [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__poll)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__put_packet"></span>

Error **_put_packet** ( p_buffer: `const uint8_t*`, p_buffer_size: [int](class_int.md#class_int) ) *virtual* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__put_packet)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__set_write_mode"></span>

void **_set_write_mode** ( p_write_mode: [WriteMode](class_webrtcdatachannel.md#enum_WebRTCDataChannel_WriteMode) ) *virtual* |required| [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__set_write_mode)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_WebRTCDataChannelExtension_private_method__was_string_packet"></span>

[bool](class_bool.md#class_bool) **_was_string_packet** ( ) *virtual* |required| *const* [🔗](class_webrtcdatachannelextension.md#class_WebRTCDataChannelExtension_private_method__was_string_packet)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
