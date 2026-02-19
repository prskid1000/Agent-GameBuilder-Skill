<span id="class_AudioStreamSynchronized"></span>

## AudioStreamSynchronized

**Inherits:** [AudioStream](class_audiostream.md#class_AudioStream) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Stream that can be fitted with sub-streams, which will be played in-sync.

### Description

This is a stream that can be fitted with sub-streams, which will be played in-sync. The streams begin at exactly the same time when play is pressed, and will end when the last of them ends. If one of the sub-streams loops, then playback will continue.

### Properties


| [int](class_int.md#class_int) | [stream_count](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_property_stream_count) | `0` |
| --- | --- | --- |

### Methods


| [AudioStream](class_audiostream.md#class_AudioStream) | [get_sync_stream](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_method_get_sync_stream) ( stream_index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [float](class_float.md#class_float) | [get_sync_stream_volume](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_method_get_sync_stream_volume) ( stream_index: [int](class_int.md#class_int) ) const |
| void | [set_sync_stream](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_method_set_sync_stream) ( stream_index: [int](class_int.md#class_int), audio_stream: [AudioStream](class_audiostream.md#class_AudioStream) ) |
| void | [set_sync_stream_volume](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_method_set_sync_stream_volume) ( stream_index: [int](class_int.md#class_int), volume_db: [float](class_float.md#class_float) ) |

---

### Constants

<span id="class_AudioStreamSynchronized_constant_MAX_STREAMS"></span>

**MAX_STREAMS** = `32` [🔗](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_constant_MAX_STREAMS)

Maximum amount of streams that can be synchronized.

---

### Property Descriptions

<span id="class_AudioStreamSynchronized_property_stream_count"></span>

[int](class_int.md#class_int) **stream_count** = `0` [🔗](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_property_stream_count)

- void **set_stream_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_stream_count** ( )

Set the total amount of streams that will be played back synchronized.

---

### Method Descriptions

<span id="class_AudioStreamSynchronized_method_get_sync_stream"></span>

[AudioStream](class_audiostream.md#class_AudioStream) **get_sync_stream** ( stream_index: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_method_get_sync_stream)

Get one of the synchronized streams, by index.

---

<span id="class_AudioStreamSynchronized_method_get_sync_stream_volume"></span>

[float](class_float.md#class_float) **get_sync_stream_volume** ( stream_index: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_method_get_sync_stream_volume)

Get the volume of one of the synchronized streams, by index.

---

<span id="class_AudioStreamSynchronized_method_set_sync_stream"></span>

void **set_sync_stream** ( stream_index: [int](class_int.md#class_int), audio_stream: [AudioStream](class_audiostream.md#class_AudioStream) ) [🔗](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_method_set_sync_stream)

Set one of the synchronized streams, by index.

---

<span id="class_AudioStreamSynchronized_method_set_sync_stream_volume"></span>

void **set_sync_stream_volume** ( stream_index: [int](class_int.md#class_int), volume_db: [float](class_float.md#class_float) ) [🔗](class_audiostreamsynchronized.md#class_AudioStreamSynchronized_method_set_sync_stream_volume)

Set the volume of one of the synchronized streams, by index.
