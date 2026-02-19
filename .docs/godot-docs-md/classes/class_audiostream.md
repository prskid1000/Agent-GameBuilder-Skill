<span id="class_AudioStream"></span>

## AudioStream

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AudioStreamGenerator](class_audiostreamgenerator.md#class_AudioStreamGenerator), [AudioStreamInteractive](class_audiostreaminteractive.md#class_AudioStreamInteractive), [AudioStreamMicrophone](class_audiostreammicrophone.md#class_AudioStreamMicrophone), [AudioStreamMP3](class_audiostreammp3.md#class_AudioStreamMP3), [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis), [AudioStreamPlaylist](class_audiostreamplaylist.md#class_AudioStreamPlaylist), [AudioStreamPolyphonic](class_audiostreampolyphonic.md#class_AudioStreamPolyphonic), [AudioStreamRandomizer](class_audiostreamrandomizer.md#class_AudioStreamRandomizer), [AudioStreamSynchronized](class_audiostreamsynchronized.md#class_AudioStreamSynchronized), [AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV)

Base class for audio streams.

### Description

Base class for audio streams. Audio streams are used for sound effects and music playback, and support WAV (via [AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV)) and Ogg (via [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis)) file formats.

### Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

- Audio Generator Demo

- Audio Microphone Record Demo

- Audio Spectrum Visualizer Demo

### Methods


| [int](class_int.md#class_int) | [_get_bar_beats](class_audiostream.md#class_AudioStream_private_method__get_bar_beats) ( ) | virtual | const |
| --- | --- | --- | --- |
| [int](class_int.md#class_int) | [_get_beat_count](class_audiostream.md#class_AudioStream_private_method__get_beat_count) ( ) | virtual | const |
| [float](class_float.md#class_float) | [_get_bpm](class_audiostream.md#class_AudioStream_private_method__get_bpm) ( ) | virtual | const |
| [float](class_float.md#class_float) | [_get_length](class_audiostream.md#class_AudioStream_private_method__get_length) ( ) | virtual | const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_get_parameter_list](class_audiostream.md#class_AudioStream_private_method__get_parameter_list) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_stream_name](class_audiostream.md#class_AudioStream_private_method__get_stream_name) ( ) | virtual | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_tags](class_audiostream.md#class_AudioStream_private_method__get_tags) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_has_loop](class_audiostream.md#class_AudioStream_private_method__has_loop) ( ) | virtual | const |
| [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) | [_instantiate_playback](class_audiostream.md#class_AudioStream_private_method__instantiate_playback) ( ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_is_monophonic](class_audiostream.md#class_AudioStream_private_method__is_monophonic) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [can_be_sampled](class_audiostream.md#class_AudioStream_method_can_be_sampled) ( ) const |
| [AudioSample](class_audiosample.md#class_AudioSample) | [generate_sample](class_audiostream.md#class_AudioStream_method_generate_sample) ( ) const |
| [float](class_float.md#class_float) | [get_length](class_audiostream.md#class_AudioStream_method_get_length) ( ) const |
| [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) | [instantiate_playback](class_audiostream.md#class_AudioStream_method_instantiate_playback) ( ) |
| [bool](class_bool.md#class_bool) | [is_meta_stream](class_audiostream.md#class_AudioStream_method_is_meta_stream) ( ) const |
| [bool](class_bool.md#class_bool) | [is_monophonic](class_audiostream.md#class_AudioStream_method_is_monophonic) ( ) const |

---

### Signals

<span id="class_AudioStream_signal_parameter_list_changed"></span>

**parameter_list_changed** ( ) [🔗](class_audiostream.md#class_AudioStream_signal_parameter_list_changed)

Signal to be emitted to notify when the parameter list changed.

---

### Method Descriptions

<span id="class_AudioStream_private_method__get_bar_beats"></span>

[int](class_int.md#class_int) **_get_bar_beats** ( ) *virtual* *const* [🔗](class_audiostream.md#class_AudioStream_private_method__get_bar_beats)

Override this method to return the bar beats of this stream.

---

<span id="class_AudioStream_private_method__get_beat_count"></span>

[int](class_int.md#class_int) **_get_beat_count** ( ) *virtual* *const* [🔗](class_audiostream.md#class_AudioStream_private_method__get_beat_count)

Overridable method. Should return the total number of beats of this audio stream. Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate ([AudioStreamWAV.mix_rate](class_audiostreamwav.md#class_AudioStreamWAV_property_mix_rate), for example).

---

<span id="class_AudioStream_private_method__get_bpm"></span>

[float](class_float.md#class_float) **_get_bpm** ( ) *virtual* *const* [🔗](class_audiostream.md#class_AudioStream_private_method__get_bpm)

Overridable method. Should return the tempo of this audio stream, in beats per minute (BPM). Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate ([AudioStreamWAV.mix_rate](class_audiostreamwav.md#class_AudioStreamWAV_property_mix_rate), for example).

---

<span id="class_AudioStream_private_method__get_length"></span>

[float](class_float.md#class_float) **_get_length** ( ) *virtual* *const* [🔗](class_audiostream.md#class_AudioStream_private_method__get_length)

Override this method to customize the returned value of [get_length()](class_audiostream.md#class_AudioStream_method_get_length). Should return the length of this audio stream, in seconds.

---

<span id="class_AudioStream_private_method__get_parameter_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_get_parameter_list** ( ) *virtual* *const* [🔗](class_audiostream.md#class_AudioStream_private_method__get_parameter_list)

Return the controllable parameters of this stream. This array contains dictionaries with a property info description format (see [Object.get_property_list()](class_object.md#class_Object_method_get_property_list)). Additionally, the default value for this parameter must be added tho each dictionary in "default_value" field.

---

<span id="class_AudioStream_private_method__get_stream_name"></span>

[String](class_string.md#class_String) **_get_stream_name** ( ) *virtual* *const* [🔗](class_audiostream.md#class_AudioStream_private_method__get_stream_name)

Override this method to customize the name assigned to this audio stream. Unused by the engine.

---

<span id="class_AudioStream_private_method__get_tags"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_tags** ( ) *virtual* *const* [🔗](class_audiostream.md#class_AudioStream_private_method__get_tags)

Override this method to customize the tags for this audio stream. Should return a [Dictionary](class_dictionary.md#class_Dictionary) of strings with the tag as the key and its content as the value.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date`.

---

<span id="class_AudioStream_private_method__has_loop"></span>

[bool](class_bool.md#class_bool) **_has_loop** ( ) *virtual* *const* [🔗](class_audiostream.md#class_AudioStream_private_method__has_loop)

Override this method to return `true` if this stream has a loop.

---

<span id="class_AudioStream_private_method__instantiate_playback"></span>

[AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) **_instantiate_playback** ( ) *virtual* |required| *const* [🔗](class_audiostream.md#class_AudioStream_private_method__instantiate_playback)

Override this method to customize the returned value of [instantiate_playback()](class_audiostream.md#class_AudioStream_method_instantiate_playback). Should return a new [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) created when the stream is played (such as by an [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer)).

---

<span id="class_AudioStream_private_method__is_monophonic"></span>

[bool](class_bool.md#class_bool) **_is_monophonic** ( ) *virtual* *const* [🔗](class_audiostream.md#class_AudioStream_private_method__is_monophonic)

Override this method to customize the returned value of [is_monophonic()](class_audiostream.md#class_AudioStream_method_is_monophonic). Should return `true` if this audio stream only supports one channel.

---

<span id="class_AudioStream_method_can_be_sampled"></span>

[bool](class_bool.md#class_bool) **can_be_sampled** ( ) *const* [🔗](class_audiostream.md#class_AudioStream_method_can_be_sampled)

**Experimental:** This method may be changed or removed in future versions.

Returns if the current **AudioStream** can be used as a sample. Only static streams can be sampled.

---

<span id="class_AudioStream_method_generate_sample"></span>

[AudioSample](class_audiosample.md#class_AudioSample) **generate_sample** ( ) *const* [🔗](class_audiostream.md#class_AudioStream_method_generate_sample)

**Experimental:** This method may be changed or removed in future versions.

Generates an [AudioSample](class_audiosample.md#class_AudioSample) based on the current stream.

---

<span id="class_AudioStream_method_get_length"></span>

[float](class_float.md#class_float) **get_length** ( ) *const* [🔗](class_audiostream.md#class_AudioStream_method_get_length)

Returns the length of the audio stream in seconds. If this stream is an [AudioStreamRandomizer](class_audiostreamrandomizer.md#class_AudioStreamRandomizer), returns the length of the last played stream. If this stream has an indefinite length (such as for [AudioStreamGenerator](class_audiostreamgenerator.md#class_AudioStreamGenerator) and [AudioStreamMicrophone](class_audiostreammicrophone.md#class_AudioStreamMicrophone)), returns `0.0`.

---

<span id="class_AudioStream_method_instantiate_playback"></span>

[AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) **instantiate_playback** ( ) [🔗](class_audiostream.md#class_AudioStream_method_instantiate_playback)

Returns a newly created [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) intended to play this audio stream. Useful for when you want to extend [_instantiate_playback()](class_audiostream.md#class_AudioStream_private_method__instantiate_playback) but call [instantiate_playback()](class_audiostream.md#class_AudioStream_method_instantiate_playback) from an internally held AudioStream subresource. An example of this can be found in the source code for `AudioStreamRandomPitch::instantiate_playback`.

---

<span id="class_AudioStream_method_is_meta_stream"></span>

[bool](class_bool.md#class_bool) **is_meta_stream** ( ) *const* [🔗](class_audiostream.md#class_AudioStream_method_is_meta_stream)

Returns `true` if the stream is a collection of other streams, `false` otherwise.

---

<span id="class_AudioStream_method_is_monophonic"></span>

[bool](class_bool.md#class_bool) **is_monophonic** ( ) *const* [🔗](class_audiostream.md#class_AudioStream_method_is_monophonic)

Returns `true` if this audio stream only supports one channel (*monophony*), or `false` if the audio stream supports two or more channels (*polyphony*).
