<span id="class_AudioStreamPlayback"></span>

## AudioStreamPlayback

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AudioStreamPlaybackInteractive](class_audiostreamplaybackinteractive.md#class_AudioStreamPlaybackInteractive), [AudioStreamPlaybackPlaylist](class_audiostreamplaybackplaylist.md#class_AudioStreamPlaybackPlaylist), [AudioStreamPlaybackPolyphonic](class_audiostreamplaybackpolyphonic.md#class_AudioStreamPlaybackPolyphonic), [AudioStreamPlaybackResampled](class_audiostreamplaybackresampled.md#class_AudioStreamPlaybackResampled), [AudioStreamPlaybackSynchronized](class_audiostreamplaybacksynchronized.md#class_AudioStreamPlaybackSynchronized)

Meta class for playing back audio.

### Description

Can play, loop, pause a scroll through audio. See [AudioStream](class_audiostream.md#class_AudioStream) and [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis) for usage.

### Tutorials

- Audio Generator Demo

### Methods


| [int](class_int.md#class_int) | [_get_loop_count](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__get_loop_count) ( ) | virtual | const |
| --- | --- | --- | --- |
| [Variant](class_variant.md#class_Variant) | [_get_parameter](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__get_parameter) ( name: [StringName](class_stringname.md#class_StringName) ) | virtual | const |
| [float](class_float.md#class_float) | [_get_playback_position](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__get_playback_position) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_playing](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__is_playing) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_mix](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__mix) ( buffer: `AudioFrame*`, rate_scale: [float](class_float.md#class_float), frames: [int](class_int.md#class_int) ) | virtual | required |
| void | [_seek](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__seek) ( position: [float](class_float.md#class_float) ) virtual |
| void | [_set_parameter](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__set_parameter) ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) virtual |
| void | [_start](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__start) ( from_pos: [float](class_float.md#class_float) ) | virtual | required |
| void | [_stop](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__stop) ( ) | virtual | required |
| void | [_tag_used_streams](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__tag_used_streams) ( ) virtual |
| [int](class_int.md#class_int) | [get_loop_count](class_audiostreamplayback.md#class_AudioStreamPlayback_method_get_loop_count) ( ) const |
| [float](class_float.md#class_float) | [get_playback_position](class_audiostreamplayback.md#class_AudioStreamPlayback_method_get_playback_position) ( ) const |
| [AudioSamplePlayback](class_audiosampleplayback.md#class_AudioSamplePlayback) | [get_sample_playback](class_audiostreamplayback.md#class_AudioStreamPlayback_method_get_sample_playback) ( ) const |
| [bool](class_bool.md#class_bool) | [is_playing](class_audiostreamplayback.md#class_AudioStreamPlayback_method_is_playing) ( ) const |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [mix_audio](class_audiostreamplayback.md#class_AudioStreamPlayback_method_mix_audio) ( rate_scale: [float](class_float.md#class_float), frames: [int](class_int.md#class_int) ) |
| void | [seek](class_audiostreamplayback.md#class_AudioStreamPlayback_method_seek) ( time: [float](class_float.md#class_float) = 0.0 ) |
| void | [set_sample_playback](class_audiostreamplayback.md#class_AudioStreamPlayback_method_set_sample_playback) ( playback_sample: [AudioSamplePlayback](class_audiosampleplayback.md#class_AudioSamplePlayback) ) |
| void | [start](class_audiostreamplayback.md#class_AudioStreamPlayback_method_start) ( from_pos: [float](class_float.md#class_float) = 0.0 ) |
| void | [stop](class_audiostreamplayback.md#class_AudioStreamPlayback_method_stop) ( ) |

---

### Method Descriptions

<span id="class_AudioStreamPlayback_private_method__get_loop_count"></span>

[int](class_int.md#class_int) **_get_loop_count** ( ) *virtual* *const* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__get_loop_count)

Overridable method. Should return how many times this audio stream has looped. Most built-in playbacks always return `0`.

---

<span id="class_AudioStreamPlayback_private_method__get_parameter"></span>

[Variant](class_variant.md#class_Variant) **_get_parameter** ( name: [StringName](class_stringname.md#class_StringName) ) *virtual* *const* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__get_parameter)

Return the current value of a playback parameter by name (see [AudioStream._get_parameter_list()](class_audiostream.md#class_AudioStream_private_method__get_parameter_list)).

---

<span id="class_AudioStreamPlayback_private_method__get_playback_position"></span>

[float](class_float.md#class_float) **_get_playback_position** ( ) *virtual* |required| *const* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__get_playback_position)

Overridable method. Should return the current progress along the audio stream, in seconds.

---

<span id="class_AudioStreamPlayback_private_method__is_playing"></span>

[bool](class_bool.md#class_bool) **_is_playing** ( ) *virtual* |required| *const* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__is_playing)

Overridable method. Should return `true` if this playback is active and playing its audio stream.

---

<span id="class_AudioStreamPlayback_private_method__mix"></span>

[int](class_int.md#class_int) **_mix** ( buffer: `AudioFrame*`, rate_scale: [float](class_float.md#class_float), frames: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__mix)

Override this method to customize how the audio stream is mixed. This method is called even if the playback is not active.

 **Note:** It is not useful to override this method in GDScript or C#. Only GDExtension can take advantage of it.

---

<span id="class_AudioStreamPlayback_private_method__seek"></span>

void **_seek** ( position: [float](class_float.md#class_float) ) *virtual* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__seek)

Override this method to customize what happens when seeking this audio stream at the given `position`, such as by calling [AudioStreamPlayer.seek()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_seek).

---

<span id="class_AudioStreamPlayback_private_method__set_parameter"></span>

void **_set_parameter** ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) *virtual* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__set_parameter)

Set the current value of a playback parameter by name (see [AudioStream._get_parameter_list()](class_audiostream.md#class_AudioStream_private_method__get_parameter_list)).

---

<span id="class_AudioStreamPlayback_private_method__start"></span>

void **_start** ( from_pos: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__start)

Override this method to customize what happens when the playback starts at the given position, such as by calling [AudioStreamPlayer.play()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_play).

---

<span id="class_AudioStreamPlayback_private_method__stop"></span>

void **_stop** ( ) *virtual* |required| [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__stop)

Override this method to customize what happens when the playback is stopped, such as by calling [AudioStreamPlayer.stop()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_stop).

---

<span id="class_AudioStreamPlayback_private_method__tag_used_streams"></span>

void **_tag_used_streams** ( ) *virtual* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__tag_used_streams)

Overridable method. Called whenever the audio stream is mixed if the playback is active and [AudioServer.set_enable_tagging_used_audio_streams()](class_audioserver.md#class_AudioServer_method_set_enable_tagging_used_audio_streams) has been set to `true`. Editor plugins may use this method to "tag" the current position along the audio stream and display it in a preview.

---

<span id="class_AudioStreamPlayback_method_get_loop_count"></span>

[int](class_int.md#class_int) **get_loop_count** ( ) *const* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_method_get_loop_count)

Returns the number of times the stream has looped.

---

<span id="class_AudioStreamPlayback_method_get_playback_position"></span>

[float](class_float.md#class_float) **get_playback_position** ( ) *const* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_method_get_playback_position)

Returns the current position in the stream, in seconds.

---

<span id="class_AudioStreamPlayback_method_get_sample_playback"></span>

[AudioSamplePlayback](class_audiosampleplayback.md#class_AudioSamplePlayback) **get_sample_playback** ( ) *const* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_method_get_sample_playback)

**Experimental:** This method may be changed or removed in future versions.

Returns the [AudioSamplePlayback](class_audiosampleplayback.md#class_AudioSamplePlayback) associated with this **AudioStreamPlayback** for playing back the audio sample of this stream.

---

<span id="class_AudioStreamPlayback_method_is_playing"></span>

[bool](class_bool.md#class_bool) **is_playing** ( ) *const* [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_method_is_playing)

Returns `true` if the stream is playing.

---

<span id="class_AudioStreamPlayback_method_mix_audio"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **mix_audio** ( rate_scale: [float](class_float.md#class_float), frames: [int](class_int.md#class_int) ) [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_method_mix_audio)

Mixes up to `frames` of audio from the stream from the current position, at a rate of `rate_scale`, advancing the stream.

Returns a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) where each element holds the left and right channel volume levels of each frame.

 **Note:** Can return fewer frames than requested, make sure to use the size of the return value.

---

<span id="class_AudioStreamPlayback_method_seek"></span>

void **seek** ( time: [float](class_float.md#class_float) = 0.0 ) [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_method_seek)

Seeks the stream at the given `time`, in seconds.

---

<span id="class_AudioStreamPlayback_method_set_sample_playback"></span>

void **set_sample_playback** ( playback_sample: [AudioSamplePlayback](class_audiosampleplayback.md#class_AudioSamplePlayback) ) [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_method_set_sample_playback)

**Experimental:** This method may be changed or removed in future versions.

Associates [AudioSamplePlayback](class_audiosampleplayback.md#class_AudioSamplePlayback) to this **AudioStreamPlayback** for playing back the audio sample of this stream.

---

<span id="class_AudioStreamPlayback_method_start"></span>

void **start** ( from_pos: [float](class_float.md#class_float) = 0.0 ) [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_method_start)

Starts the stream from the given `from_pos`, in seconds.

---

<span id="class_AudioStreamPlayback_method_stop"></span>

void **stop** ( ) [🔗](class_audiostreamplayback.md#class_AudioStreamPlayback_method_stop)

Stops the stream.
