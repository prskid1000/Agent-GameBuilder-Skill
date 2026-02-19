<span id="class_AudioStreamPlaylist"></span>

## AudioStreamPlaylist

**Inherits:** [AudioStream](class_audiostream.md#class_AudioStream) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

[AudioStream](class_audiostream.md#class_AudioStream) that includes sub-streams and plays them back like a playlist.

### Properties


| [float](class_float.md#class_float) | [fade_time](class_audiostreamplaylist.md#class_AudioStreamPlaylist_property_fade_time) | `0.3` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [loop](class_audiostreamplaylist.md#class_AudioStreamPlaylist_property_loop) | `true` |
| [bool](class_bool.md#class_bool) | [shuffle](class_audiostreamplaylist.md#class_AudioStreamPlaylist_property_shuffle) | `false` |
| [int](class_int.md#class_int) | [stream_count](class_audiostreamplaylist.md#class_AudioStreamPlaylist_property_stream_count) | `0` |

### Methods


| [float](class_float.md#class_float) | [get_bpm](class_audiostreamplaylist.md#class_AudioStreamPlaylist_method_get_bpm) ( ) const |
| --- | --- |
| [AudioStream](class_audiostream.md#class_AudioStream) | [get_list_stream](class_audiostreamplaylist.md#class_AudioStreamPlaylist_method_get_list_stream) ( stream_index: [int](class_int.md#class_int) ) const |
| void | [set_list_stream](class_audiostreamplaylist.md#class_AudioStreamPlaylist_method_set_list_stream) ( stream_index: [int](class_int.md#class_int), audio_stream: [AudioStream](class_audiostream.md#class_AudioStream) ) |

---

### Constants

<span id="class_AudioStreamPlaylist_constant_MAX_STREAMS"></span>

**MAX_STREAMS** = `64` [🔗](class_audiostreamplaylist.md#class_AudioStreamPlaylist_constant_MAX_STREAMS)

Maximum amount of streams supported in the playlist.

---

### Property Descriptions

<span id="class_AudioStreamPlaylist_property_fade_time"></span>

[float](class_float.md#class_float) **fade_time** = `0.3` [🔗](class_audiostreamplaylist.md#class_AudioStreamPlaylist_property_fade_time)

- void **set_fade_time** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fade_time** ( )

Fade time used when a stream ends, when going to the next one. Streams are expected to have an extra bit of audio after the end to help with fading.

---

<span id="class_AudioStreamPlaylist_property_loop"></span>

[bool](class_bool.md#class_bool) **loop** = `true` [🔗](class_audiostreamplaylist.md#class_AudioStreamPlaylist_property_loop)

- void **set_loop** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_loop** ( )

If `true`, the playlist will loop, otherwise the playlist will end when the last stream is finished.

---

<span id="class_AudioStreamPlaylist_property_shuffle"></span>

[bool](class_bool.md#class_bool) **shuffle** = `false` [🔗](class_audiostreamplaylist.md#class_AudioStreamPlaylist_property_shuffle)

- void **set_shuffle** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_shuffle** ( )

If `true`, the playlist will shuffle each time playback starts and each time it loops.

---

<span id="class_AudioStreamPlaylist_property_stream_count"></span>

[int](class_int.md#class_int) **stream_count** = `0` [🔗](class_audiostreamplaylist.md#class_AudioStreamPlaylist_property_stream_count)

- void **set_stream_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_stream_count** ( )

Amount of streams in the playlist.

---

### Method Descriptions

<span id="class_AudioStreamPlaylist_method_get_bpm"></span>

[float](class_float.md#class_float) **get_bpm** ( ) *const* [🔗](class_audiostreamplaylist.md#class_AudioStreamPlaylist_method_get_bpm)

Returns the BPM of the playlist, which can vary depending on the clip being played.

---

<span id="class_AudioStreamPlaylist_method_get_list_stream"></span>

[AudioStream](class_audiostream.md#class_AudioStream) **get_list_stream** ( stream_index: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreamplaylist.md#class_AudioStreamPlaylist_method_get_list_stream)

Returns the stream at playback position index.

---

<span id="class_AudioStreamPlaylist_method_set_list_stream"></span>

void **set_list_stream** ( stream_index: [int](class_int.md#class_int), audio_stream: [AudioStream](class_audiostream.md#class_AudioStream) ) [🔗](class_audiostreamplaylist.md#class_AudioStreamPlaylist_method_set_list_stream)

Sets the stream at playback position index.
