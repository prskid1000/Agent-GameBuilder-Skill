<span id="class_AudioStreamRandomizer"></span>

## AudioStreamRandomizer

**Inherits:** [AudioStream](class_audiostream.md#class_AudioStream) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Wraps a pool of audio streams with pitch and volume shifting.

### Description

Picks a random AudioStream from the pool, depending on the playback mode, and applies random pitch shifting and volume shifting during playback.

### Properties


| [PlaybackMode](class_audiostreamrandomizer.md#enum_AudioStreamRandomizer_PlaybackMode) | [playback_mode](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_playback_mode) | `0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [random_pitch](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_random_pitch) | `1.0` |
| [float](class_float.md#class_float) | [random_pitch_semitones](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_random_pitch_semitones) | `0.0` |
| [float](class_float.md#class_float) | [random_volume_offset_db](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_random_volume_offset_db) | `0.0` |
| [int](class_int.md#class_int) | [streams_count](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_streams_count) | `0` |

### Methods


| void | [add_stream](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_add_stream) ( index: [int](class_int.md#class_int), stream: [AudioStream](class_audiostream.md#class_AudioStream), weight: [float](class_float.md#class_float) = 1.0 ) |
| --- | --- |
| [AudioStream](class_audiostream.md#class_AudioStream) | [get_stream](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_get_stream) ( index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_stream_probability_weight](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_get_stream_probability_weight) ( index: [int](class_int.md#class_int) ) const |
| void | [move_stream](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_move_stream) ( index_from: [int](class_int.md#class_int), index_to: [int](class_int.md#class_int) ) |
| void | [remove_stream](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_remove_stream) ( index: [int](class_int.md#class_int) ) |
| void | [set_stream](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_set_stream) ( index: [int](class_int.md#class_int), stream: [AudioStream](class_audiostream.md#class_AudioStream) ) |
| void | [set_stream_probability_weight](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_set_stream_probability_weight) ( index: [int](class_int.md#class_int), weight: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_AudioStreamRandomizer_PlaybackMode"></span>

enum **PlaybackMode**: [🔗](class_audiostreamrandomizer.md#enum_AudioStreamRandomizer_PlaybackMode)

<span id="class_AudioStreamRandomizer_constant_PLAYBACK_RANDOM_NO_REPEATS"></span>

[PlaybackMode](class_audiostreamrandomizer.md#enum_AudioStreamRandomizer_PlaybackMode) **PLAYBACK_RANDOM_NO_REPEATS** = `0`

Pick a stream at random according to the probability weights chosen for each stream, but avoid playing the same stream twice in a row whenever possible. If only 1 sound is present in the pool, the same sound will always play, effectively allowing repeats to occur.

<span id="class_AudioStreamRandomizer_constant_PLAYBACK_RANDOM"></span>

[PlaybackMode](class_audiostreamrandomizer.md#enum_AudioStreamRandomizer_PlaybackMode) **PLAYBACK_RANDOM** = `1`

Pick a stream at random according to the probability weights chosen for each stream. If only 1 sound is present in the pool, the same sound will always play.

<span id="class_AudioStreamRandomizer_constant_PLAYBACK_SEQUENTIAL"></span>

[PlaybackMode](class_audiostreamrandomizer.md#enum_AudioStreamRandomizer_PlaybackMode) **PLAYBACK_SEQUENTIAL** = `2`

Play streams in the order they appear in the stream pool. If only 1 sound is present in the pool, the same sound will always play.

---

### Property Descriptions

<span id="class_AudioStreamRandomizer_property_playback_mode"></span>

[PlaybackMode](class_audiostreamrandomizer.md#enum_AudioStreamRandomizer_PlaybackMode) **playback_mode** = `0` [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_playback_mode)

- void **set_playback_mode** ( value: [PlaybackMode](class_audiostreamrandomizer.md#enum_AudioStreamRandomizer_PlaybackMode) )
- [PlaybackMode](class_audiostreamrandomizer.md#enum_AudioStreamRandomizer_PlaybackMode) **get_playback_mode** ( )

Controls how this AudioStreamRandomizer picks which AudioStream to play next.

---

<span id="class_AudioStreamRandomizer_property_random_pitch"></span>

[float](class_float.md#class_float) **random_pitch** = `1.0` [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_random_pitch)

- void **set_random_pitch** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_random_pitch** ( )

The largest possible frequency multiplier of the random pitch variation. Pitch will be randomly chosen within a range of `1.0 / random_pitch` and `random_pitch`. A value of `1.0` means no variation. A value of `2.0` means pitch will be randomized between double and half.

 **Note:** Setting this property also sets [random_pitch_semitones](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_random_pitch_semitones).

---

<span id="class_AudioStreamRandomizer_property_random_pitch_semitones"></span>

[float](class_float.md#class_float) **random_pitch_semitones** = `0.0` [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_random_pitch_semitones)

- void **set_random_pitch_semitones** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_random_pitch_semitones** ( )

The largest possible distance, in semitones, of the random pitch variation. A value of `0.0` means no variation.

 **Note:** Setting this property also sets [random_pitch](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_random_pitch).

---

<span id="class_AudioStreamRandomizer_property_random_volume_offset_db"></span>

[float](class_float.md#class_float) **random_volume_offset_db** = `0.0` [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_random_volume_offset_db)

- void **set_random_volume_offset_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_random_volume_offset_db** ( )

The intensity of random volume variation. Volume will be increased or decreased by a random value up to `random_volume_offset_db`. A value of `0.0` means no variation. A value of `3.0` means volume will be randomized between `-3.0 dB` and `+3.0 dB`.

---

<span id="class_AudioStreamRandomizer_property_streams_count"></span>

[int](class_int.md#class_int) **streams_count** = `0` [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_property_streams_count)

- void **set_streams_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_streams_count** ( )

The number of streams in the stream pool.

---

### Method Descriptions

<span id="class_AudioStreamRandomizer_method_add_stream"></span>

void **add_stream** ( index: [int](class_int.md#class_int), stream: [AudioStream](class_audiostream.md#class_AudioStream), weight: [float](class_float.md#class_float) = 1.0 ) [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_add_stream)

Insert a stream at the specified index. If the index is less than zero, the insertion occurs at the end of the underlying pool.

---

<span id="class_AudioStreamRandomizer_method_get_stream"></span>

[AudioStream](class_audiostream.md#class_AudioStream) **get_stream** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_get_stream)

Returns the stream at the specified index.

---

<span id="class_AudioStreamRandomizer_method_get_stream_probability_weight"></span>

[float](class_float.md#class_float) **get_stream_probability_weight** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_get_stream_probability_weight)

Returns the probability weight associated with the stream at the given index.

---

<span id="class_AudioStreamRandomizer_method_move_stream"></span>

void **move_stream** ( index_from: [int](class_int.md#class_int), index_to: [int](class_int.md#class_int) ) [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_move_stream)

Move a stream from one index to another.

---

<span id="class_AudioStreamRandomizer_method_remove_stream"></span>

void **remove_stream** ( index: [int](class_int.md#class_int) ) [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_remove_stream)

Remove the stream at the specified index.

---

<span id="class_AudioStreamRandomizer_method_set_stream"></span>

void **set_stream** ( index: [int](class_int.md#class_int), stream: [AudioStream](class_audiostream.md#class_AudioStream) ) [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_set_stream)

Set the AudioStream at the specified index.

---

<span id="class_AudioStreamRandomizer_method_set_stream_probability_weight"></span>

void **set_stream_probability_weight** ( index: [int](class_int.md#class_int), weight: [float](class_float.md#class_float) ) [🔗](class_audiostreamrandomizer.md#class_AudioStreamRandomizer_method_set_stream_probability_weight)

Set the probability weight of the stream at the specified index. The higher this value, the more likely that the randomizer will choose this stream during random playback modes.
