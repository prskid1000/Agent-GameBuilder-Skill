.. meta::
	:keywords: sound, music, song

<span id="class_AudioStreamPlayer"></span>

## AudioStreamPlayer

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node for audio playback.

### Description

The **AudioStreamPlayer** node plays an audio stream non-positionally. It is ideal for user interfaces, menus, or background music.

To use this node, [stream](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream) needs to be set to a valid [AudioStream](class_audiostream.md#class_AudioStream) resource. Playing more than one sound at the same time is also supported, see [max_polyphony](class_audiostreamplayer.md#class_AudioStreamPlayer_property_max_polyphony).

If you need to play audio at a specific position, use [AudioStreamPlayer2D](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D) or [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D) instead.

### Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

- 2D Dodge The Creeps Demo

- Audio Device Changer Demo

- Audio Generator Demo

- Audio Microphone Record Demo

- Audio Spectrum Visualizer Demo

### Properties


| [bool](class_bool.md#class_bool) | [autoplay](class_audiostreamplayer.md#class_AudioStreamPlayer_property_autoplay) | `false` |
| --- | --- | --- |
| [StringName](class_stringname.md#class_StringName) | [bus](class_audiostreamplayer.md#class_AudioStreamPlayer_property_bus) | `&"Master"` |
| [int](class_int.md#class_int) | [max_polyphony](class_audiostreamplayer.md#class_AudioStreamPlayer_property_max_polyphony) | `1` |
| [MixTarget](class_audiostreamplayer.md#enum_AudioStreamPlayer_MixTarget) | [mix_target](class_audiostreamplayer.md#class_AudioStreamPlayer_property_mix_target) | `0` |
| [float](class_float.md#class_float) | [pitch_scale](class_audiostreamplayer.md#class_AudioStreamPlayer_property_pitch_scale) | `1.0` |
| [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) | [playback_type](class_audiostreamplayer.md#class_AudioStreamPlayer_property_playback_type) | `0` |
| [bool](class_bool.md#class_bool) | [playing](class_audiostreamplayer.md#class_AudioStreamPlayer_property_playing) | `false` |
| [AudioStream](class_audiostream.md#class_AudioStream) | [stream](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream) |
| [bool](class_bool.md#class_bool) | [stream_paused](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream_paused) | `false` |
| [float](class_float.md#class_float) | [volume_db](class_audiostreamplayer.md#class_AudioStreamPlayer_property_volume_db) | `0.0` |
| [float](class_float.md#class_float) | [volume_linear](class_audiostreamplayer.md#class_AudioStreamPlayer_property_volume_linear) |

### Methods


| [float](class_float.md#class_float) | [get_playback_position](class_audiostreamplayer.md#class_AudioStreamPlayer_method_get_playback_position) ( ) |
| --- | --- |
| [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) | [get_stream_playback](class_audiostreamplayer.md#class_AudioStreamPlayer_method_get_stream_playback) ( ) |
| [bool](class_bool.md#class_bool) | [has_stream_playback](class_audiostreamplayer.md#class_AudioStreamPlayer_method_has_stream_playback) ( ) |
| void | [play](class_audiostreamplayer.md#class_AudioStreamPlayer_method_play) ( from_position: [float](class_float.md#class_float) = 0.0 ) |
| void | [seek](class_audiostreamplayer.md#class_AudioStreamPlayer_method_seek) ( to_position: [float](class_float.md#class_float) ) |
| void | [stop](class_audiostreamplayer.md#class_AudioStreamPlayer_method_stop) ( ) |

---

### Signals

<span id="class_AudioStreamPlayer_signal_finished"></span>

**finished** ( ) [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_signal_finished)

Emitted when a sound finishes playing without interruptions. This signal is *not* emitted when calling [stop()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_stop), or when exiting the tree while sounds are playing.

---

### Enumerations

<span id="enum_AudioStreamPlayer_MixTarget"></span>

enum **MixTarget**: [🔗](class_audiostreamplayer.md#enum_AudioStreamPlayer_MixTarget)

<span id="class_AudioStreamPlayer_constant_MIX_TARGET_STEREO"></span>

[MixTarget](class_audiostreamplayer.md#enum_AudioStreamPlayer_MixTarget) **MIX_TARGET_STEREO** = `0`

The audio will be played only on the first channel. This is the default.

<span id="class_AudioStreamPlayer_constant_MIX_TARGET_SURROUND"></span>

[MixTarget](class_audiostreamplayer.md#enum_AudioStreamPlayer_MixTarget) **MIX_TARGET_SURROUND** = `1`

The audio will be played on all surround channels.

<span id="class_AudioStreamPlayer_constant_MIX_TARGET_CENTER"></span>

[MixTarget](class_audiostreamplayer.md#enum_AudioStreamPlayer_MixTarget) **MIX_TARGET_CENTER** = `2`

The audio will be played on the second channel, which is usually the center.

---

### Property Descriptions

<span id="class_AudioStreamPlayer_property_autoplay"></span>

[bool](class_bool.md#class_bool) **autoplay** = `false` [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_autoplay)

- void **set_autoplay** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_autoplay_enabled** ( )

If `true`, this node calls [play()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_play) when entering the tree.

---

<span id="class_AudioStreamPlayer_property_bus"></span>

[StringName](class_stringname.md#class_StringName) **bus** = `&"Master"` [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_bus)

- void **set_bus** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_bus** ( )

The target bus name. All sounds from this node will be playing on this bus.

 **Note:** At runtime, if no bus with the given name exists, all sounds will fall back on `"Master"`. See also [AudioServer.get_bus_name()](class_audioserver.md#class_AudioServer_method_get_bus_name).

---

<span id="class_AudioStreamPlayer_property_max_polyphony"></span>

[int](class_int.md#class_int) **max_polyphony** = `1` [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_max_polyphony)

- void **set_max_polyphony** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_polyphony** ( )

The maximum number of sounds this node can play at the same time. Calling [play()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_play) after this value is reached will cut off the oldest sounds.

---

<span id="class_AudioStreamPlayer_property_mix_target"></span>

[MixTarget](class_audiostreamplayer.md#enum_AudioStreamPlayer_MixTarget) **mix_target** = `0` [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_mix_target)

- void **set_mix_target** ( value: [MixTarget](class_audiostreamplayer.md#enum_AudioStreamPlayer_MixTarget) )
- [MixTarget](class_audiostreamplayer.md#enum_AudioStreamPlayer_MixTarget) **get_mix_target** ( )

The mix target channels. Has no effect when two speakers or less are detected (see [SpeakerMode](class_audioserver.md#enum_AudioServer_SpeakerMode)).

---

<span id="class_AudioStreamPlayer_property_pitch_scale"></span>

[float](class_float.md#class_float) **pitch_scale** = `1.0` [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_pitch_scale)

- void **set_pitch_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pitch_scale** ( )

The audio's pitch and tempo, as a multiplier of the [stream](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream)'s sample rate. A value of `2.0` doubles the audio's pitch, while a value of `0.5` halves the pitch.

---

<span id="class_AudioStreamPlayer_property_playback_type"></span>

[PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **playback_type** = `0` [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_playback_type)

- void **set_playback_type** ( value: [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) )
- [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **get_playback_type** ( )

**Experimental:** This property may be changed or removed in future versions.

The playback type of the stream player. If set other than to the default value, it will force that playback type.

---

<span id="class_AudioStreamPlayer_property_playing"></span>

[bool](class_bool.md#class_bool) **playing** = `false` [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_playing)

- void **set_playing** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_playing** ( )

If `true`, this node is playing sounds. Setting this property has the same effect as [play()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_play) and [stop()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_stop).

---

<span id="class_AudioStreamPlayer_property_stream"></span>

[AudioStream](class_audiostream.md#class_AudioStream) **stream** [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream)

- void **set_stream** ( value: [AudioStream](class_audiostream.md#class_AudioStream) )
- [AudioStream](class_audiostream.md#class_AudioStream) **get_stream** ( )

The [AudioStream](class_audiostream.md#class_AudioStream) resource to be played. Setting this property stops all currently playing sounds. If left empty, the **AudioStreamPlayer** does not work.

---

<span id="class_AudioStreamPlayer_property_stream_paused"></span>

[bool](class_bool.md#class_bool) **stream_paused** = `false` [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream_paused)

- void **set_stream_paused** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_stream_paused** ( )

If `true`, the sounds are paused. Setting [stream_paused](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream_paused) to `false` resumes all sounds.

 **Note:** This property is automatically changed when exiting or entering the tree, or this node is paused (see [Node.process_mode](class_node.md#class_Node_property_process_mode)).

---

<span id="class_AudioStreamPlayer_property_volume_db"></span>

[float](class_float.md#class_float) **volume_db** = `0.0` [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_volume_db)

- void **set_volume_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume_db** ( )

Volume of sound, in decibels. This is an offset of the [stream](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream)'s volume.

 **Note:** To convert between decibel and linear energy (like most volume sliders do), use [volume_linear](class_audiostreamplayer.md#class_AudioStreamPlayer_property_volume_linear), or @GlobalScope.db_to_linear() and @GlobalScope.linear_to_db().

---

<span id="class_AudioStreamPlayer_property_volume_linear"></span>

[float](class_float.md#class_float) **volume_linear** [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_property_volume_linear)

- void **set_volume_linear** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume_linear** ( )

Volume of sound, as a linear value.

 **Note:** This member modifies [volume_db](class_audiostreamplayer.md#class_AudioStreamPlayer_property_volume_db) for convenience. The returned value is equivalent to the result of @GlobalScope.db_to_linear() on [volume_db](class_audiostreamplayer.md#class_AudioStreamPlayer_property_volume_db). Setting this member is equivalent to setting [volume_db](class_audiostreamplayer.md#class_AudioStreamPlayer_property_volume_db) to the result of @GlobalScope.linear_to_db() on a value.

---

### Method Descriptions

<span id="class_AudioStreamPlayer_method_get_playback_position"></span>

[float](class_float.md#class_float) **get_playback_position** ( ) [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_method_get_playback_position)

Returns the position in the [AudioStream](class_audiostream.md#class_AudioStream) of the latest sound, in seconds. Returns `0.0` if no sounds are playing.

 **Note:** The position is not always accurate, as the [AudioServer](class_audioserver.md#class_AudioServer) does not mix audio every processed frame. To get more accurate results, add [AudioServer.get_time_since_last_mix()](class_audioserver.md#class_AudioServer_method_get_time_since_last_mix) to the returned position.

 **Note:** This method always returns `0.0` if the [stream](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream) is an [AudioStreamInteractive](class_audiostreaminteractive.md#class_AudioStreamInteractive), since it can have multiple clips playing at once.

---

<span id="class_AudioStreamPlayer_method_get_stream_playback"></span>

[AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) **get_stream_playback** ( ) [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_method_get_stream_playback)

Returns the latest [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) of this node, usually the most recently created by [play()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_play). If no sounds are playing, this method fails and returns an empty playback.

---

<span id="class_AudioStreamPlayer_method_has_stream_playback"></span>

[bool](class_bool.md#class_bool) **has_stream_playback** ( ) [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_method_has_stream_playback)

Returns `true` if any sound is active, even if [stream_paused](class_audiostreamplayer.md#class_AudioStreamPlayer_property_stream_paused) is set to `true`. See also [playing](class_audiostreamplayer.md#class_AudioStreamPlayer_property_playing) and [get_stream_playback()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_get_stream_playback).

---

<span id="class_AudioStreamPlayer_method_play"></span>

void **play** ( from_position: [float](class_float.md#class_float) = 0.0 ) [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_method_play)

Plays a sound from the beginning, or the given `from_position` in seconds.

---

<span id="class_AudioStreamPlayer_method_seek"></span>

void **seek** ( to_position: [float](class_float.md#class_float) ) [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_method_seek)

Restarts all sounds to be played from the given `to_position`, in seconds. Does nothing if no sounds are playing.

---

<span id="class_AudioStreamPlayer_method_stop"></span>

void **stop** ( ) [🔗](class_audiostreamplayer.md#class_AudioStreamPlayer_method_stop)

Stops all sounds from this node.
