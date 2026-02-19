.. meta::
	:keywords: sound, sfx

<span id="class_AudioStreamPlayer2D"></span>

## AudioStreamPlayer2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Plays positional sound in 2D space.

### Description

Plays audio that is attenuated with distance to the listener.

By default, audio is heard from the screen center. This can be changed by adding an [AudioListener2D](class_audiolistener2d.md#class_AudioListener2D) node to the scene and enabling it by calling [AudioListener2D.make_current()](class_audiolistener2d.md#class_AudioListener2D_method_make_current) on it.

See also [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer) to play a sound non-positionally.

 **Note:** Hiding an **AudioStreamPlayer2D** node does not disable its audio output. To temporarily disable an **AudioStreamPlayer2D**'s audio output, set [volume_db](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_volume_db) to a very low value like `-100` (which isn't audible to human hearing).

### Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

### Properties


| [int](class_int.md#class_int) | [area_mask](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_area_mask) | `1` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [attenuation](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_attenuation) | `1.0` |
| [bool](class_bool.md#class_bool) | [autoplay](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_autoplay) | `false` |
| [StringName](class_stringname.md#class_StringName) | [bus](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_bus) | `&"Master"` |
| [float](class_float.md#class_float) | [max_distance](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_max_distance) | `2000.0` |
| [int](class_int.md#class_int) | [max_polyphony](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_max_polyphony) | `1` |
| [float](class_float.md#class_float) | [panning_strength](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_panning_strength) | `1.0` |
| [float](class_float.md#class_float) | [pitch_scale](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_pitch_scale) | `1.0` |
| [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) | [playback_type](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_playback_type) | `0` |
| [bool](class_bool.md#class_bool) | [playing](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_playing) | `false` |
| [AudioStream](class_audiostream.md#class_AudioStream) | [stream](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_stream) |
| [bool](class_bool.md#class_bool) | [stream_paused](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_stream_paused) | `false` |
| [float](class_float.md#class_float) | [volume_db](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_volume_db) | `0.0` |
| [float](class_float.md#class_float) | [volume_linear](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_volume_linear) |

### Methods


| [float](class_float.md#class_float) | [get_playback_position](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_get_playback_position) ( ) |
| --- | --- |
| [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) | [get_stream_playback](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_get_stream_playback) ( ) |
| [bool](class_bool.md#class_bool) | [has_stream_playback](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_has_stream_playback) ( ) |
| void | [play](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_play) ( from_position: [float](class_float.md#class_float) = 0.0 ) |
| void | [seek](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_seek) ( to_position: [float](class_float.md#class_float) ) |
| void | [stop](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_stop) ( ) |

---

### Signals

<span id="class_AudioStreamPlayer2D_signal_finished"></span>

**finished** ( ) [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_signal_finished)

Emitted when the audio stops playing.

---

### Property Descriptions

<span id="class_AudioStreamPlayer2D_property_area_mask"></span>

[int](class_int.md#class_int) **area_mask** = `1` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_area_mask)

- void **set_area_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_area_mask** ( )

Determines which [Area2D](class_area2d.md#class_Area2D) layers affect the sound for reverb and audio bus effects. Areas can be used to redirect [AudioStream](class_audiostream.md#class_AudioStream) s so that they play in a certain audio bus. An example of how you might use this is making a "water" area so that sounds played in the water are redirected through an audio bus to make them sound like they are being played underwater.

---

<span id="class_AudioStreamPlayer2D_property_attenuation"></span>

[float](class_float.md#class_float) **attenuation** = `1.0` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_attenuation)

- void **set_attenuation** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_attenuation** ( )

The volume is attenuated over distance with this as an exponent.

---

<span id="class_AudioStreamPlayer2D_property_autoplay"></span>

[bool](class_bool.md#class_bool) **autoplay** = `false` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_autoplay)

- void **set_autoplay** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_autoplay_enabled** ( )

If `true`, audio plays when added to scene tree.

---

<span id="class_AudioStreamPlayer2D_property_bus"></span>

[StringName](class_stringname.md#class_StringName) **bus** = `&"Master"` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_bus)

- void **set_bus** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_bus** ( )

Bus on which this audio is playing.

 **Note:** When setting this property, keep in mind that no validation is performed to see if the given name matches an existing bus. This is because audio bus layouts might be loaded after this property is set. If this given name can't be resolved at runtime, it will fall back to `"Master"`.

---

<span id="class_AudioStreamPlayer2D_property_max_distance"></span>

[float](class_float.md#class_float) **max_distance** = `2000.0` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_max_distance)

- void **set_max_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max_distance** ( )

Maximum distance from which audio is still hearable.

---

<span id="class_AudioStreamPlayer2D_property_max_polyphony"></span>

[int](class_int.md#class_int) **max_polyphony** = `1` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_max_polyphony)

- void **set_max_polyphony** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_polyphony** ( )

The maximum number of sounds this node can play at the same time. Playing additional sounds after this value is reached will cut off the oldest sounds.

---

<span id="class_AudioStreamPlayer2D_property_panning_strength"></span>

[float](class_float.md#class_float) **panning_strength** = `1.0` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_panning_strength)

- void **set_panning_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_panning_strength** ( )

Scales the panning strength for this node by multiplying the base ProjectSettings.audio/general/2d_panning_strength with this factor. Higher values will pan audio from left to right more dramatically than lower values.

---

<span id="class_AudioStreamPlayer2D_property_pitch_scale"></span>

[float](class_float.md#class_float) **pitch_scale** = `1.0` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_pitch_scale)

- void **set_pitch_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pitch_scale** ( )

The pitch and the tempo of the audio, as a multiplier of the audio sample's sample rate.

---

<span id="class_AudioStreamPlayer2D_property_playback_type"></span>

[PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **playback_type** = `0` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_playback_type)

- void **set_playback_type** ( value: [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) )
- [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **get_playback_type** ( )

**Experimental:** This property may be changed or removed in future versions.

The playback type of the stream player. If set other than to the default value, it will force that playback type.

---

<span id="class_AudioStreamPlayer2D_property_playing"></span>

[bool](class_bool.md#class_bool) **playing** = `false` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_playing)

- void **set_playing** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_playing** ( )

If `true`, audio is playing or is queued to be played (see [play()](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_play)).

---

<span id="class_AudioStreamPlayer2D_property_stream"></span>

[AudioStream](class_audiostream.md#class_AudioStream) **stream** [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_stream)

- void **set_stream** ( value: [AudioStream](class_audiostream.md#class_AudioStream) )
- [AudioStream](class_audiostream.md#class_AudioStream) **get_stream** ( )

The [AudioStream](class_audiostream.md#class_AudioStream) object to be played.

---

<span id="class_AudioStreamPlayer2D_property_stream_paused"></span>

[bool](class_bool.md#class_bool) **stream_paused** = `false` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_stream_paused)

- void **set_stream_paused** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_stream_paused** ( )

If `true`, the playback is paused. You can resume it by setting [stream_paused](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_stream_paused) to `false`.

---

<span id="class_AudioStreamPlayer2D_property_volume_db"></span>

[float](class_float.md#class_float) **volume_db** = `0.0` [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_volume_db)

- void **set_volume_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume_db** ( )

Base volume before attenuation, in decibels.

---

<span id="class_AudioStreamPlayer2D_property_volume_linear"></span>

[float](class_float.md#class_float) **volume_linear** [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_volume_linear)

- void **set_volume_linear** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume_linear** ( )

Base volume before attenuation, as a linear value.

 **Note:** This member modifies [volume_db](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_volume_db) for convenience. The returned value is equivalent to the result of @GlobalScope.db_to_linear() on [volume_db](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_volume_db). Setting this member is equivalent to setting [volume_db](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_property_volume_db) to the result of @GlobalScope.linear_to_db() on a value.

---

### Method Descriptions

<span id="class_AudioStreamPlayer2D_method_get_playback_position"></span>

[float](class_float.md#class_float) **get_playback_position** ( ) [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_get_playback_position)

Returns the position in the [AudioStream](class_audiostream.md#class_AudioStream).

---

<span id="class_AudioStreamPlayer2D_method_get_stream_playback"></span>

[AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) **get_stream_playback** ( ) [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_get_stream_playback)

Returns the [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) object associated with this **AudioStreamPlayer2D**.

---

<span id="class_AudioStreamPlayer2D_method_has_stream_playback"></span>

[bool](class_bool.md#class_bool) **has_stream_playback** ( ) [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_has_stream_playback)

Returns whether the [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer) can return the [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) object or not.

---

<span id="class_AudioStreamPlayer2D_method_play"></span>

void **play** ( from_position: [float](class_float.md#class_float) = 0.0 ) [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_play)

Queues the audio to play on the next physics frame, from the given position `from_position`, in seconds.

---

<span id="class_AudioStreamPlayer2D_method_seek"></span>

void **seek** ( to_position: [float](class_float.md#class_float) ) [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_seek)

Sets the position from which audio will be played, in seconds.

---

<span id="class_AudioStreamPlayer2D_method_stop"></span>

void **stop** ( ) [🔗](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_stop)

Stops the audio.
