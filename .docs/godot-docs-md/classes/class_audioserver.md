<span id="class_AudioServer"></span>

## AudioServer

**Inherits:** [Object](class_object.md#class_Object)

Server interface for low-level audio access.

### Description

**AudioServer** is a low-level server interface for audio access. It is in charge of creating sample data (playable audio) as well as its playback via a voice interface.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

- Audio Device Changer Demo

- Audio Microphone Record Demo

- Audio Spectrum Visualizer Demo

### Properties


| [int](class_int.md#class_int) | [bus_count](class_audioserver.md#class_AudioServer_property_bus_count) | `1` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [input_device](class_audioserver.md#class_AudioServer_property_input_device) | `"Default"` |
| [String](class_string.md#class_String) | [output_device](class_audioserver.md#class_AudioServer_property_output_device) | `"Default"` |
| [float](class_float.md#class_float) | [playback_speed_scale](class_audioserver.md#class_AudioServer_property_playback_speed_scale) | `1.0` |

### Methods


| void | [add_bus](class_audioserver.md#class_AudioServer_method_add_bus) ( at_position: [int](class_int.md#class_int) = -1 ) |
| --- | --- |
| void | [add_bus_effect](class_audioserver.md#class_AudioServer_method_add_bus_effect) ( bus_idx: [int](class_int.md#class_int), effect: [AudioEffect](class_audioeffect.md#class_AudioEffect), at_position: [int](class_int.md#class_int) = -1 ) |
| [AudioBusLayout](class_audiobuslayout.md#class_AudioBusLayout) | [generate_bus_layout](class_audioserver.md#class_AudioServer_method_generate_bus_layout) ( ) const |
| [int](class_int.md#class_int) | [get_bus_channels](class_audioserver.md#class_AudioServer_method_get_bus_channels) ( bus_idx: [int](class_int.md#class_int) ) const |
| [AudioEffect](class_audioeffect.md#class_AudioEffect) | [get_bus_effect](class_audioserver.md#class_AudioServer_method_get_bus_effect) ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_bus_effect_count](class_audioserver.md#class_AudioServer_method_get_bus_effect_count) ( bus_idx: [int](class_int.md#class_int) ) |
| [AudioEffectInstance](class_audioeffectinstance.md#class_AudioEffectInstance) | [get_bus_effect_instance](class_audioserver.md#class_AudioServer_method_get_bus_effect_instance) ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int), channel: [int](class_int.md#class_int) = 0 ) |
| [int](class_int.md#class_int) | [get_bus_index](class_audioserver.md#class_AudioServer_method_get_bus_index) ( bus_name: [StringName](class_stringname.md#class_StringName) ) const |
| [String](class_string.md#class_String) | [get_bus_name](class_audioserver.md#class_AudioServer_method_get_bus_name) ( bus_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_bus_peak_volume_left_db](class_audioserver.md#class_AudioServer_method_get_bus_peak_volume_left_db) ( bus_idx: [int](class_int.md#class_int), channel: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_bus_peak_volume_right_db](class_audioserver.md#class_AudioServer_method_get_bus_peak_volume_right_db) ( bus_idx: [int](class_int.md#class_int), channel: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_bus_send](class_audioserver.md#class_AudioServer_method_get_bus_send) ( bus_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_bus_volume_db](class_audioserver.md#class_AudioServer_method_get_bus_volume_db) ( bus_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_bus_volume_linear](class_audioserver.md#class_AudioServer_method_get_bus_volume_linear) ( bus_idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_driver_name](class_audioserver.md#class_AudioServer_method_get_driver_name) ( ) const |
| [int](class_int.md#class_int) | [get_input_buffer_length_frames](class_audioserver.md#class_AudioServer_method_get_input_buffer_length_frames) ( ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_input_device_list](class_audioserver.md#class_AudioServer_method_get_input_device_list) ( ) |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [get_input_frames](class_audioserver.md#class_AudioServer_method_get_input_frames) ( frames: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_input_frames_available](class_audioserver.md#class_AudioServer_method_get_input_frames_available) ( ) |
| [float](class_float.md#class_float) | [get_input_mix_rate](class_audioserver.md#class_AudioServer_method_get_input_mix_rate) ( ) const |
| [float](class_float.md#class_float) | [get_mix_rate](class_audioserver.md#class_AudioServer_method_get_mix_rate) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_output_device_list](class_audioserver.md#class_AudioServer_method_get_output_device_list) ( ) |
| [float](class_float.md#class_float) | [get_output_latency](class_audioserver.md#class_AudioServer_method_get_output_latency) ( ) const |
| [SpeakerMode](class_audioserver.md#enum_AudioServer_SpeakerMode) | [get_speaker_mode](class_audioserver.md#class_AudioServer_method_get_speaker_mode) ( ) const |
| [float](class_float.md#class_float) | [get_time_since_last_mix](class_audioserver.md#class_AudioServer_method_get_time_since_last_mix) ( ) const |
| [float](class_float.md#class_float) | [get_time_to_next_mix](class_audioserver.md#class_AudioServer_method_get_time_to_next_mix) ( ) const |
| [bool](class_bool.md#class_bool) | [is_bus_bypassing_effects](class_audioserver.md#class_AudioServer_method_is_bus_bypassing_effects) ( bus_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_bus_effect_enabled](class_audioserver.md#class_AudioServer_method_is_bus_effect_enabled) ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_bus_mute](class_audioserver.md#class_AudioServer_method_is_bus_mute) ( bus_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_bus_solo](class_audioserver.md#class_AudioServer_method_is_bus_solo) ( bus_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_stream_registered_as_sample](class_audioserver.md#class_AudioServer_method_is_stream_registered_as_sample) ( stream: [AudioStream](class_audiostream.md#class_AudioStream) ) |
| void | [lock](class_audioserver.md#class_AudioServer_method_lock) ( ) |
| void | [move_bus](class_audioserver.md#class_AudioServer_method_move_bus) ( index: [int](class_int.md#class_int), to_index: [int](class_int.md#class_int) ) |
| void | [register_stream_as_sample](class_audioserver.md#class_AudioServer_method_register_stream_as_sample) ( stream: [AudioStream](class_audiostream.md#class_AudioStream) ) |
| void | [remove_bus](class_audioserver.md#class_AudioServer_method_remove_bus) ( index: [int](class_int.md#class_int) ) |
| void | [remove_bus_effect](class_audioserver.md#class_AudioServer_method_remove_bus_effect) ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int) ) |
| void | [set_bus_bypass_effects](class_audioserver.md#class_AudioServer_method_set_bus_bypass_effects) ( bus_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_bus_effect_enabled](class_audioserver.md#class_AudioServer_method_set_bus_effect_enabled) ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_bus_layout](class_audioserver.md#class_AudioServer_method_set_bus_layout) ( bus_layout: [AudioBusLayout](class_audiobuslayout.md#class_AudioBusLayout) ) |
| void | [set_bus_mute](class_audioserver.md#class_AudioServer_method_set_bus_mute) ( bus_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_bus_name](class_audioserver.md#class_AudioServer_method_set_bus_name) ( bus_idx: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [set_bus_send](class_audioserver.md#class_AudioServer_method_set_bus_send) ( bus_idx: [int](class_int.md#class_int), send: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_bus_solo](class_audioserver.md#class_AudioServer_method_set_bus_solo) ( bus_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_bus_volume_db](class_audioserver.md#class_AudioServer_method_set_bus_volume_db) ( bus_idx: [int](class_int.md#class_int), volume_db: [float](class_float.md#class_float) ) |
| void | [set_bus_volume_linear](class_audioserver.md#class_AudioServer_method_set_bus_volume_linear) ( bus_idx: [int](class_int.md#class_int), volume_linear: [float](class_float.md#class_float) ) |
| void | [set_enable_tagging_used_audio_streams](class_audioserver.md#class_AudioServer_method_set_enable_tagging_used_audio_streams) ( enable: [bool](class_bool.md#class_bool) ) |
| Error | [set_input_device_active](class_audioserver.md#class_AudioServer_method_set_input_device_active) ( active: [bool](class_bool.md#class_bool) ) |
| void | [swap_bus_effects](class_audioserver.md#class_AudioServer_method_swap_bus_effects) ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int), by_effect_idx: [int](class_int.md#class_int) ) |
| void | [unlock](class_audioserver.md#class_AudioServer_method_unlock) ( ) |

---

### Signals

<span id="class_AudioServer_signal_bus_layout_changed"></span>

**bus_layout_changed** ( ) [🔗](class_audioserver.md#class_AudioServer_signal_bus_layout_changed)

Emitted when an audio bus is added, deleted, or moved.

---

<span id="class_AudioServer_signal_bus_renamed"></span>

**bus_renamed** ( bus_index: [int](class_int.md#class_int), old_name: [StringName](class_stringname.md#class_StringName), new_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_audioserver.md#class_AudioServer_signal_bus_renamed)

Emitted when the audio bus at `bus_index` is renamed from `old_name` to `new_name`.

---

### Enumerations

<span id="enum_AudioServer_SpeakerMode"></span>

enum **SpeakerMode**: [🔗](class_audioserver.md#enum_AudioServer_SpeakerMode)

<span id="class_AudioServer_constant_SPEAKER_MODE_STEREO"></span>

[SpeakerMode](class_audioserver.md#enum_AudioServer_SpeakerMode) **SPEAKER_MODE_STEREO** = `0`

Two or fewer speakers were detected.

<span id="class_AudioServer_constant_SPEAKER_SURROUND_31"></span>

[SpeakerMode](class_audioserver.md#enum_AudioServer_SpeakerMode) **SPEAKER_SURROUND_31** = `1`

A 3.1 channel surround setup was detected.

<span id="class_AudioServer_constant_SPEAKER_SURROUND_51"></span>

[SpeakerMode](class_audioserver.md#enum_AudioServer_SpeakerMode) **SPEAKER_SURROUND_51** = `2`

A 5.1 channel surround setup was detected.

<span id="class_AudioServer_constant_SPEAKER_SURROUND_71"></span>

[SpeakerMode](class_audioserver.md#enum_AudioServer_SpeakerMode) **SPEAKER_SURROUND_71** = `3`

A 7.1 channel surround setup was detected.

---

<span id="enum_AudioServer_PlaybackType"></span>

enum **PlaybackType**: [🔗](class_audioserver.md#enum_AudioServer_PlaybackType)

<span id="class_AudioServer_constant_PLAYBACK_TYPE_DEFAULT"></span>

[PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **PLAYBACK_TYPE_DEFAULT** = `0`

**Experimental:** This constant may be changed or removed in future versions.

The playback will be considered of the type declared at ProjectSettings.audio/general/default_playback_type.

<span id="class_AudioServer_constant_PLAYBACK_TYPE_STREAM"></span>

[PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **PLAYBACK_TYPE_STREAM** = `1`

**Experimental:** This constant may be changed or removed in future versions.

Force the playback to be considered as a stream.

<span id="class_AudioServer_constant_PLAYBACK_TYPE_SAMPLE"></span>

[PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **PLAYBACK_TYPE_SAMPLE** = `2`

**Experimental:** This constant may be changed or removed in future versions.

Force the playback to be considered as a sample. This can provide lower latency and more stable playback (with less risk of audio crackling), at the cost of having less flexibility.

 **Note:** Only currently supported on the web platform.

 **Note:** [AudioEffect](class_audioeffect.md#class_AudioEffect) s are not supported when playback is considered as a sample.

<span id="class_AudioServer_constant_PLAYBACK_TYPE_MAX"></span>

[PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **PLAYBACK_TYPE_MAX** = `3`

**Experimental:** This constant may be changed or removed in future versions.

Represents the size of the [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) enum.

---

### Property Descriptions

<span id="class_AudioServer_property_bus_count"></span>

[int](class_int.md#class_int) **bus_count** = `1` [🔗](class_audioserver.md#class_AudioServer_property_bus_count)

- void **set_bus_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bus_count** ( )

Number of available audio buses.

---

<span id="class_AudioServer_property_input_device"></span>

[String](class_string.md#class_String) **input_device** = `"Default"` [🔗](class_audioserver.md#class_AudioServer_property_input_device)

- void **set_input_device** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_input_device** ( )

Name of the current device for audio input (see [get_input_device_list()](class_audioserver.md#class_AudioServer_method_get_input_device_list)). On systems with multiple audio inputs (such as analog, USB and HDMI audio), this can be used to select the audio input device. The value `"Default"` will record audio on the system-wide default audio input. If an invalid device name is set, the value will be reverted back to `"Default"`.

 **Note:** ProjectSettings.audio/driver/enable_input must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

---

<span id="class_AudioServer_property_output_device"></span>

[String](class_string.md#class_String) **output_device** = `"Default"` [🔗](class_audioserver.md#class_AudioServer_property_output_device)

- void **set_output_device** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_output_device** ( )

Name of the current device for audio output (see [get_output_device_list()](class_audioserver.md#class_AudioServer_method_get_output_device_list)). On systems with multiple audio outputs (such as analog, USB and HDMI audio), this can be used to select the audio output device. The value `"Default"` will play audio on the system-wide default audio output. If an invalid device name is set, the value will be reverted back to `"Default"`.

---

<span id="class_AudioServer_property_playback_speed_scale"></span>

[float](class_float.md#class_float) **playback_speed_scale** = `1.0` [🔗](class_audioserver.md#class_AudioServer_property_playback_speed_scale)

- void **set_playback_speed_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_playback_speed_scale** ( )

Scales the rate at which audio is played (i.e. setting it to `0.5` will make the audio be played at half its speed). See also [Engine.time_scale](class_engine.md#class_Engine_property_time_scale) to affect the general simulation speed, which is independent from [playback_speed_scale](class_audioserver.md#class_AudioServer_property_playback_speed_scale).

---

### Method Descriptions

<span id="class_AudioServer_method_add_bus"></span>

void **add_bus** ( at_position: [int](class_int.md#class_int) = -1 ) [🔗](class_audioserver.md#class_AudioServer_method_add_bus)

Adds a bus at `at_position`.

---

<span id="class_AudioServer_method_add_bus_effect"></span>

void **add_bus_effect** ( bus_idx: [int](class_int.md#class_int), effect: [AudioEffect](class_audioeffect.md#class_AudioEffect), at_position: [int](class_int.md#class_int) = -1 ) [🔗](class_audioserver.md#class_AudioServer_method_add_bus_effect)

Adds an [AudioEffect](class_audioeffect.md#class_AudioEffect) effect to the bus `bus_idx` at `at_position`.

---

<span id="class_AudioServer_method_generate_bus_layout"></span>

[AudioBusLayout](class_audiobuslayout.md#class_AudioBusLayout) **generate_bus_layout** ( ) *const* [🔗](class_audioserver.md#class_AudioServer_method_generate_bus_layout)

Generates an [AudioBusLayout](class_audiobuslayout.md#class_AudioBusLayout) using the available buses and effects.

---

<span id="class_AudioServer_method_get_bus_channels"></span>

[int](class_int.md#class_int) **get_bus_channels** ( bus_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_bus_channels)

Returns the number of channels of the bus at index `bus_idx`.

---

<span id="class_AudioServer_method_get_bus_effect"></span>

[AudioEffect](class_audioeffect.md#class_AudioEffect) **get_bus_effect** ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int) ) [🔗](class_audioserver.md#class_AudioServer_method_get_bus_effect)

Returns the [AudioEffect](class_audioeffect.md#class_AudioEffect) at position `effect_idx` in bus `bus_idx`.

---

<span id="class_AudioServer_method_get_bus_effect_count"></span>

[int](class_int.md#class_int) **get_bus_effect_count** ( bus_idx: [int](class_int.md#class_int) ) [🔗](class_audioserver.md#class_AudioServer_method_get_bus_effect_count)

Returns the number of effects on the bus at `bus_idx`.

---

<span id="class_AudioServer_method_get_bus_effect_instance"></span>

[AudioEffectInstance](class_audioeffectinstance.md#class_AudioEffectInstance) **get_bus_effect_instance** ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int), channel: [int](class_int.md#class_int) = 0 ) [🔗](class_audioserver.md#class_AudioServer_method_get_bus_effect_instance)

Returns the [AudioEffectInstance](class_audioeffectinstance.md#class_AudioEffectInstance) assigned to the given bus and effect indices (and optionally channel).

---

<span id="class_AudioServer_method_get_bus_index"></span>

[int](class_int.md#class_int) **get_bus_index** ( bus_name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_bus_index)

Returns the index of the bus with the name `bus_name`. Returns `-1` if no bus with the specified name exist.

---

<span id="class_AudioServer_method_get_bus_name"></span>

[String](class_string.md#class_String) **get_bus_name** ( bus_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_bus_name)

Returns the name of the bus with the index `bus_idx`.

---

<span id="class_AudioServer_method_get_bus_peak_volume_left_db"></span>

[float](class_float.md#class_float) **get_bus_peak_volume_left_db** ( bus_idx: [int](class_int.md#class_int), channel: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_bus_peak_volume_left_db)

Returns the peak volume of the left speaker at bus index `bus_idx` and channel index `channel`.

---

<span id="class_AudioServer_method_get_bus_peak_volume_right_db"></span>

[float](class_float.md#class_float) **get_bus_peak_volume_right_db** ( bus_idx: [int](class_int.md#class_int), channel: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_bus_peak_volume_right_db)

Returns the peak volume of the right speaker at bus index `bus_idx` and channel index `channel`.

---

<span id="class_AudioServer_method_get_bus_send"></span>

[StringName](class_stringname.md#class_StringName) **get_bus_send** ( bus_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_bus_send)

Returns the name of the bus that the bus at index `bus_idx` sends to.

---

<span id="class_AudioServer_method_get_bus_volume_db"></span>

[float](class_float.md#class_float) **get_bus_volume_db** ( bus_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_bus_volume_db)

Returns the volume of the bus at index `bus_idx` in dB.

---

<span id="class_AudioServer_method_get_bus_volume_linear"></span>

[float](class_float.md#class_float) **get_bus_volume_linear** ( bus_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_bus_volume_linear)

Returns the volume of the bus at index `bus_idx` as a linear value.

 **Note:** The returned value is equivalent to the result of @GlobalScope.db_to_linear() on the result of [get_bus_volume_db()](class_audioserver.md#class_AudioServer_method_get_bus_volume_db).

---

<span id="class_AudioServer_method_get_driver_name"></span>

[String](class_string.md#class_String) **get_driver_name** ( ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_driver_name)

Returns the name of the current audio driver. The default usually depends on the operating system, but may be overridden via the `--audio-driver` [command line argument](../tutorials/editor/command_line_tutorial.md). `--headless` also automatically sets the audio driver to `Dummy`. See also ProjectSettings.audio/driver/driver.

---

<span id="class_AudioServer_method_get_input_buffer_length_frames"></span>

[int](class_int.md#class_int) **get_input_buffer_length_frames** ( ) [🔗](class_audioserver.md#class_AudioServer_method_get_input_buffer_length_frames)

**Experimental:** This method may be changed or removed in future versions.

Returns the absolute size of the microphone input buffer. This is set to a multiple of the audio latency and can be used to estimate the minimum rate at which the frames need to be fetched.

---

<span id="class_AudioServer_method_get_input_device_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_input_device_list** ( ) [🔗](class_audioserver.md#class_AudioServer_method_get_input_device_list)

Returns the names of all audio input devices detected on the system.

 **Note:** ProjectSettings.audio/driver/enable_input must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

---

<span id="class_AudioServer_method_get_input_frames"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_input_frames** ( frames: [int](class_int.md#class_int) ) [🔗](class_audioserver.md#class_AudioServer_method_get_input_frames)

**Experimental:** This method may be changed or removed in future versions.

Returns a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) containing exactly `frames` audio samples from the internal microphone buffer if available, otherwise returns an empty [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array).

The buffer is filled at the rate of [get_input_mix_rate()](class_audioserver.md#class_AudioServer_method_get_input_mix_rate) frames per second when [set_input_device_active()](class_audioserver.md#class_AudioServer_method_set_input_device_active) has successfully been set to `true`.

The samples are signed floating-point PCM values between `-1` and `1`.

---

<span id="class_AudioServer_method_get_input_frames_available"></span>

[int](class_int.md#class_int) **get_input_frames_available** ( ) [🔗](class_audioserver.md#class_AudioServer_method_get_input_frames_available)

**Experimental:** This method may be changed or removed in future versions.

Returns the number of frames available to read using [get_input_frames()](class_audioserver.md#class_AudioServer_method_get_input_frames).

---

<span id="class_AudioServer_method_get_input_mix_rate"></span>

[float](class_float.md#class_float) **get_input_mix_rate** ( ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_input_mix_rate)

Returns the sample rate at the input of the **AudioServer**.

---

<span id="class_AudioServer_method_get_mix_rate"></span>

[float](class_float.md#class_float) **get_mix_rate** ( ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_mix_rate)

Returns the sample rate at the output of the **AudioServer**.

---

<span id="class_AudioServer_method_get_output_device_list"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_output_device_list** ( ) [🔗](class_audioserver.md#class_AudioServer_method_get_output_device_list)

Returns the names of all audio output devices detected on the system.

---

<span id="class_AudioServer_method_get_output_latency"></span>

[float](class_float.md#class_float) **get_output_latency** ( ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_output_latency)

Returns the audio driver's effective output latency. This is based on ProjectSettings.audio/driver/output_latency, but the exact returned value will differ depending on the operating system and audio driver.

 **Note:** This can be expensive; it is not recommended to call [get_output_latency()](class_audioserver.md#class_AudioServer_method_get_output_latency) every frame.

---

<span id="class_AudioServer_method_get_speaker_mode"></span>

[SpeakerMode](class_audioserver.md#enum_AudioServer_SpeakerMode) **get_speaker_mode** ( ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_speaker_mode)

Returns the speaker configuration.

---

<span id="class_AudioServer_method_get_time_since_last_mix"></span>

[float](class_float.md#class_float) **get_time_since_last_mix** ( ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_time_since_last_mix)

Returns the relative time since the last mix occurred.

---

<span id="class_AudioServer_method_get_time_to_next_mix"></span>

[float](class_float.md#class_float) **get_time_to_next_mix** ( ) *const* [🔗](class_audioserver.md#class_AudioServer_method_get_time_to_next_mix)

Returns the relative time until the next mix occurs.

---

<span id="class_AudioServer_method_is_bus_bypassing_effects"></span>

[bool](class_bool.md#class_bool) **is_bus_bypassing_effects** ( bus_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_is_bus_bypassing_effects)

If `true`, the bus at index `bus_idx` is bypassing effects.

---

<span id="class_AudioServer_method_is_bus_effect_enabled"></span>

[bool](class_bool.md#class_bool) **is_bus_effect_enabled** ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_is_bus_effect_enabled)

If `true`, the effect at index `effect_idx` on the bus at index `bus_idx` is enabled.

---

<span id="class_AudioServer_method_is_bus_mute"></span>

[bool](class_bool.md#class_bool) **is_bus_mute** ( bus_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_is_bus_mute)

If `true`, the bus at index `bus_idx` is muted.

---

<span id="class_AudioServer_method_is_bus_solo"></span>

[bool](class_bool.md#class_bool) **is_bus_solo** ( bus_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioserver.md#class_AudioServer_method_is_bus_solo)

If `true`, the bus at index `bus_idx` is in solo mode.

---

<span id="class_AudioServer_method_is_stream_registered_as_sample"></span>

[bool](class_bool.md#class_bool) **is_stream_registered_as_sample** ( stream: [AudioStream](class_audiostream.md#class_AudioStream) ) [🔗](class_audioserver.md#class_AudioServer_method_is_stream_registered_as_sample)

**Experimental:** This method may be changed or removed in future versions.

If `true`, the stream is registered as a sample. The engine will not have to register it before playing the sample.

If `false`, the stream will have to be registered before playing it. To prevent lag spikes, register the stream as sample with [register_stream_as_sample()](class_audioserver.md#class_AudioServer_method_register_stream_as_sample).

---

<span id="class_AudioServer_method_lock"></span>

void **lock** ( ) [🔗](class_audioserver.md#class_AudioServer_method_lock)

Locks the audio driver's main loop.

 **Note:** Remember to unlock it afterwards.

---

<span id="class_AudioServer_method_move_bus"></span>

void **move_bus** ( index: [int](class_int.md#class_int), to_index: [int](class_int.md#class_int) ) [🔗](class_audioserver.md#class_AudioServer_method_move_bus)

Moves the bus from index `index` to index `to_index`.

---

<span id="class_AudioServer_method_register_stream_as_sample"></span>

void **register_stream_as_sample** ( stream: [AudioStream](class_audiostream.md#class_AudioStream) ) [🔗](class_audioserver.md#class_AudioServer_method_register_stream_as_sample)

**Experimental:** This method may be changed or removed in future versions.

Forces the registration of a stream as a sample.

 **Note:** Lag spikes may occur when calling this method, especially on single-threaded builds. It is suggested to call this method while loading assets, where the lag spike could be masked, instead of registering the sample right before it needs to be played.

---

<span id="class_AudioServer_method_remove_bus"></span>

void **remove_bus** ( index: [int](class_int.md#class_int) ) [🔗](class_audioserver.md#class_AudioServer_method_remove_bus)

Removes the bus at index `index`.

---

<span id="class_AudioServer_method_remove_bus_effect"></span>

void **remove_bus_effect** ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int) ) [🔗](class_audioserver.md#class_AudioServer_method_remove_bus_effect)

Removes the effect at index `effect_idx` from the bus at index `bus_idx`.

---

<span id="class_AudioServer_method_set_bus_bypass_effects"></span>

void **set_bus_bypass_effects** ( bus_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_audioserver.md#class_AudioServer_method_set_bus_bypass_effects)

If `true`, the bus at index `bus_idx` is bypassing effects.

---

<span id="class_AudioServer_method_set_bus_effect_enabled"></span>

void **set_bus_effect_enabled** ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_audioserver.md#class_AudioServer_method_set_bus_effect_enabled)

If `true`, the effect at index `effect_idx` on the bus at index `bus_idx` is enabled.

---

<span id="class_AudioServer_method_set_bus_layout"></span>

void **set_bus_layout** ( bus_layout: [AudioBusLayout](class_audiobuslayout.md#class_AudioBusLayout) ) [🔗](class_audioserver.md#class_AudioServer_method_set_bus_layout)

Overwrites the currently used [AudioBusLayout](class_audiobuslayout.md#class_AudioBusLayout).

---

<span id="class_AudioServer_method_set_bus_mute"></span>

void **set_bus_mute** ( bus_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_audioserver.md#class_AudioServer_method_set_bus_mute)

If `true`, the bus at index `bus_idx` is muted.

---

<span id="class_AudioServer_method_set_bus_name"></span>

void **set_bus_name** ( bus_idx: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_audioserver.md#class_AudioServer_method_set_bus_name)

Sets the name of the bus at index `bus_idx` to `name`.

---

<span id="class_AudioServer_method_set_bus_send"></span>

void **set_bus_send** ( bus_idx: [int](class_int.md#class_int), send: [StringName](class_stringname.md#class_StringName) ) [🔗](class_audioserver.md#class_AudioServer_method_set_bus_send)

Connects the output of the bus at `bus_idx` to the bus named `send`.

---

<span id="class_AudioServer_method_set_bus_solo"></span>

void **set_bus_solo** ( bus_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_audioserver.md#class_AudioServer_method_set_bus_solo)

If `true`, the bus at index `bus_idx` is in solo mode.

---

<span id="class_AudioServer_method_set_bus_volume_db"></span>

void **set_bus_volume_db** ( bus_idx: [int](class_int.md#class_int), volume_db: [float](class_float.md#class_float) ) [🔗](class_audioserver.md#class_AudioServer_method_set_bus_volume_db)

Sets the volume in decibels of the bus at index `bus_idx` to `volume_db`.

---

<span id="class_AudioServer_method_set_bus_volume_linear"></span>

void **set_bus_volume_linear** ( bus_idx: [int](class_int.md#class_int), volume_linear: [float](class_float.md#class_float) ) [🔗](class_audioserver.md#class_AudioServer_method_set_bus_volume_linear)

Sets the volume as a linear value of the bus at index `bus_idx` to `volume_linear`.

 **Note:** Using this method is equivalent to calling [set_bus_volume_db()](class_audioserver.md#class_AudioServer_method_set_bus_volume_db) with the result of @GlobalScope.linear_to_db() on a value.

---

<span id="class_AudioServer_method_set_enable_tagging_used_audio_streams"></span>

void **set_enable_tagging_used_audio_streams** ( enable: [bool](class_bool.md#class_bool) ) [🔗](class_audioserver.md#class_AudioServer_method_set_enable_tagging_used_audio_streams)

If set to `true`, all instances of [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) will call [AudioStreamPlayback._tag_used_streams()](class_audiostreamplayback.md#class_AudioStreamPlayback_private_method__tag_used_streams) every mix step.

 **Note:** This is enabled by default in the editor, as it is used by editor plugins for the audio stream previews.

---

<span id="class_AudioServer_method_set_input_device_active"></span>

Error **set_input_device_active** ( active: [bool](class_bool.md#class_bool) ) [🔗](class_audioserver.md#class_AudioServer_method_set_input_device_active)

**Experimental:** This method may be changed or removed in future versions.

If `active` is `true`, starts the microphone input stream specified by [input_device](class_audioserver.md#class_AudioServer_property_input_device) or returns an error if it failed.

If `active` is `false`, stops the input stream if it is running.

---

<span id="class_AudioServer_method_swap_bus_effects"></span>

void **swap_bus_effects** ( bus_idx: [int](class_int.md#class_int), effect_idx: [int](class_int.md#class_int), by_effect_idx: [int](class_int.md#class_int) ) [🔗](class_audioserver.md#class_AudioServer_method_swap_bus_effects)

Swaps the position of two effects in bus `bus_idx`.

---

<span id="class_AudioServer_method_unlock"></span>

void **unlock** ( ) [🔗](class_audioserver.md#class_AudioServer_method_unlock)

Unlocks the audio driver's main loop. (After locking it, you should always unlock it.)
