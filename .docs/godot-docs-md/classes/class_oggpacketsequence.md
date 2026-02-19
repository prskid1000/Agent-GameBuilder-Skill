<span id="class_OggPacketSequence"></span>

## OggPacketSequence

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A sequence of Ogg packets.

### Description

A sequence of Ogg packets.

### Properties


| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [granule_positions](class_oggpacketsequence.md#class_OggPacketSequence_property_granule_positions) | `PackedInt64Array()` |
| --- | --- | --- |
| [Array](class_array.md#class_Array)\[[Array](class_array.md#class_Array)\] | [packet_data](class_oggpacketsequence.md#class_OggPacketSequence_property_packet_data) | `[]` |
| [float](class_float.md#class_float) | [sampling_rate](class_oggpacketsequence.md#class_OggPacketSequence_property_sampling_rate) | `0.0` |

### Methods


| [float](class_float.md#class_float) | [get_length](class_oggpacketsequence.md#class_OggPacketSequence_method_get_length) ( ) const |
| --- | --- |

---

### Property Descriptions

<span id="class_OggPacketSequence_property_granule_positions"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **granule_positions** = `PackedInt64Array()` [🔗](class_oggpacketsequence.md#class_OggPacketSequence_property_granule_positions)

- void **set_packet_granule_positions** ( value: [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) )
- [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **get_packet_granule_positions** ( )

Contains the granule positions for each page in this packet sequence.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) for more details.

---

<span id="class_OggPacketSequence_property_packet_data"></span>

[Array](class_array.md#class_Array)\[[Array](class_array.md#class_Array)\] **packet_data** = `[]` [🔗](class_oggpacketsequence.md#class_OggPacketSequence_property_packet_data)

- void **set_packet_data** ( value: [Array](class_array.md#class_Array)\[[Array](class_array.md#class_Array)\] )
- [Array](class_array.md#class_Array)\[[Array](class_array.md#class_Array)\] **get_packet_data** ( )

Contains the raw packets that make up this OggPacketSequence.

---

<span id="class_OggPacketSequence_property_sampling_rate"></span>

[float](class_float.md#class_float) **sampling_rate** = `0.0` [🔗](class_oggpacketsequence.md#class_OggPacketSequence_property_sampling_rate)

- void **set_sampling_rate** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_sampling_rate** ( )

Holds sample rate information about this sequence. Must be set by another class that actually understands the codec.

---

### Method Descriptions

<span id="class_OggPacketSequence_method_get_length"></span>

[float](class_float.md#class_float) **get_length** ( ) *const* [🔗](class_oggpacketsequence.md#class_OggPacketSequence_method_get_length)

The length of this stream, in seconds.
