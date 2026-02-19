.. meta::
	:keywords: sound, sfx

<span id="class_AudioStreamPlayer3D"></span>

## AudioStreamPlayer3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Plays positional sound in 3D space.

### Description

Plays audio with positional sound effects, based on the relative position of the audio listener. Positional effects include distance attenuation, directionality, and the Doppler effect. For greater realism, a low-pass filter is applied to distant sounds. This can be disabled by setting [attenuation_filter_cutoff_hz](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_attenuation_filter_cutoff_hz) to `20500`.

By default, audio is heard from the camera position. This can be changed by adding an [AudioListener3D](class_audiolistener3d.md#class_AudioListener3D) node to the scene and enabling it by calling [AudioListener3D.make_current()](class_audiolistener3d.md#class_AudioListener3D_method_make_current) on it.

See also [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer) to play a sound non-positionally.

 **Note:** Hiding an **AudioStreamPlayer3D** node does not disable its audio output. To temporarily disable an **AudioStreamPlayer3D**'s audio output, set [volume_db](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_volume_db) to a very low value like `-100` (which isn't audible to human hearing).

### Tutorials

- [Audio streams](../tutorials/audio/audio_streams.md)

### Properties


| [int](class_int.md#class_int) | [area_mask](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_area_mask) | `1` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [attenuation_filter_cutoff_hz](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_attenuation_filter_cutoff_hz) | `5000.0` |
| [float](class_float.md#class_float) | [attenuation_filter_db](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_attenuation_filter_db) | `-24.0` |
| [AttenuationModel](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_AttenuationModel) | [attenuation_model](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_attenuation_model) | `0` |
| [bool](class_bool.md#class_bool) | [autoplay](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_autoplay) | `false` |
| [StringName](class_stringname.md#class_StringName) | [bus](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_bus) | `&"Master"` |
| [DopplerTracking](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_DopplerTracking) | [doppler_tracking](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_doppler_tracking) | `0` |
| [float](class_float.md#class_float) | [emission_angle_degrees](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_emission_angle_degrees) | `45.0` |
| [bool](class_bool.md#class_bool) | [emission_angle_enabled](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_emission_angle_enabled) | `false` |
| [float](class_float.md#class_float) | [emission_angle_filter_attenuation_db](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_emission_angle_filter_attenuation_db) | `-12.0` |
| [float](class_float.md#class_float) | [max_db](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_max_db) | `3.0` |
| [float](class_float.md#class_float) | [max_distance](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_max_distance) | `0.0` |
| [int](class_int.md#class_int) | [max_polyphony](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_max_polyphony) | `1` |
| [float](class_float.md#class_float) | [panning_strength](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_panning_strength) | `1.0` |
| [float](class_float.md#class_float) | [pitch_scale](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_pitch_scale) | `1.0` |
| [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) | [playback_type](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_playback_type) | `0` |
| [bool](class_bool.md#class_bool) | [playing](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_playing) | `false` |
| [AudioStream](class_audiostream.md#class_AudioStream) | [stream](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_stream) |
| [bool](class_bool.md#class_bool) | [stream_paused](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_stream_paused) | `false` |
| [float](class_float.md#class_float) | [unit_size](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_unit_size) | `10.0` |
| [float](class_float.md#class_float) | [volume_db](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_volume_db) | `0.0` |
| [float](class_float.md#class_float) | [volume_linear](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_volume_linear) |

### Methods


| [float](class_float.md#class_float) | [get_playback_position](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_get_playback_position) ( ) |
| --- | --- |
| [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) | [get_stream_playback](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_get_stream_playback) ( ) |
| [bool](class_bool.md#class_bool) | [has_stream_playback](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_has_stream_playback) ( ) |
| void | [play](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_play) ( from_position: [float](class_float.md#class_float) = 0.0 ) |
| void | [seek](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_seek) ( to_position: [float](class_float.md#class_float) ) |
| void | [stop](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_stop) ( ) |

---

### Signals

<span id="class_AudioStreamPlayer3D_signal_finished"></span>

**finished** ( ) [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_signal_finished)

Emitted when the audio stops playing.

---

### Enumerations

<span id="enum_AudioStreamPlayer3D_AttenuationModel"></span>

enum **AttenuationModel**: [🔗](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_AttenuationModel)

<span id="class_AudioStreamPlayer3D_constant_ATTENUATION_INVERSE_DISTANCE"></span>

[AttenuationModel](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_AttenuationModel) **ATTENUATION_INVERSE_DISTANCE** = `0`

Attenuation of loudness according to linear distance.

<span id="class_AudioStreamPlayer3D_constant_ATTENUATION_INVERSE_SQUARE_DISTANCE"></span>

[AttenuationModel](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_AttenuationModel) **ATTENUATION_INVERSE_SQUARE_DISTANCE** = `1`

Attenuation of loudness according to squared distance.

<span id="class_AudioStreamPlayer3D_constant_ATTENUATION_LOGARITHMIC"></span>

[AttenuationModel](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_AttenuationModel) **ATTENUATION_LOGARITHMIC** = `2`

Attenuation of loudness according to logarithmic distance.

<span id="class_AudioStreamPlayer3D_constant_ATTENUATION_DISABLED"></span>

[AttenuationModel](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_AttenuationModel) **ATTENUATION_DISABLED** = `3`

No attenuation of loudness according to distance. The sound will still be heard positionally, unlike an [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer). [ATTENUATION_DISABLED](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_constant_ATTENUATION_DISABLED) can be combined with a [max_distance](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_max_distance) value greater than `0.0` to achieve linear attenuation clamped to a sphere of a defined size.

---

<span id="enum_AudioStreamPlayer3D_DopplerTracking"></span>

enum **DopplerTracking**: [🔗](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_DopplerTracking)

<span id="class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_DISABLED"></span>

[DopplerTracking](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_DopplerTracking) **DOPPLER_TRACKING_DISABLED** = `0`

Disables doppler tracking.

<span id="class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_IDLE_STEP"></span>

[DopplerTracking](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_DopplerTracking) **DOPPLER_TRACKING_IDLE_STEP** = `1`

Executes doppler tracking during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class_Node_constant_NOTIFICATION_INTERNAL_PROCESS)).

<span id="class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_PHYSICS_STEP"></span>

[DopplerTracking](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_DopplerTracking) **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Executes doppler tracking during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS)).

---

### Property Descriptions

<span id="class_AudioStreamPlayer3D_property_area_mask"></span>

[int](class_int.md#class_int) **area_mask** = `1` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_area_mask)

- void **set_area_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_area_mask** ( )

Determines which [Area3D](class_area3d.md#class_Area3D) layers affect the sound for reverb and audio bus effects. Areas can be used to redirect [AudioStream](class_audiostream.md#class_AudioStream) s so that they play in a certain audio bus. An example of how you might use this is making a "water" area so that sounds played in the water are redirected through an audio bus to make them sound like they are being played underwater.

---

<span id="class_AudioStreamPlayer3D_property_attenuation_filter_cutoff_hz"></span>

[float](class_float.md#class_float) **attenuation_filter_cutoff_hz** = `5000.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_attenuation_filter_cutoff_hz)

- void **set_attenuation_filter_cutoff_hz** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_attenuation_filter_cutoff_hz** ( )

The cutoff frequency of the attenuation low-pass filter, in Hz. A sound above this frequency is attenuated more than a sound below this frequency. To disable this effect, set this to `20500` as this frequency is above the human hearing limit.

---

<span id="class_AudioStreamPlayer3D_property_attenuation_filter_db"></span>

[float](class_float.md#class_float) **attenuation_filter_db** = `-24.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_attenuation_filter_db)

- void **set_attenuation_filter_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_attenuation_filter_db** ( )

Amount how much the filter affects the loudness, in decibels.

---

<span id="class_AudioStreamPlayer3D_property_attenuation_model"></span>

[AttenuationModel](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_AttenuationModel) **attenuation_model** = `0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_attenuation_model)

- void **set_attenuation_model** ( value: [AttenuationModel](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_AttenuationModel) )
- [AttenuationModel](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_AttenuationModel) **get_attenuation_model** ( )

Decides if audio should get quieter with distance linearly, quadratically, logarithmically, or not be affected by distance, effectively disabling attenuation.

---

<span id="class_AudioStreamPlayer3D_property_autoplay"></span>

[bool](class_bool.md#class_bool) **autoplay** = `false` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_autoplay)

- void **set_autoplay** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_autoplay_enabled** ( )

If `true`, audio plays when the AudioStreamPlayer3D node is added to scene tree.

---

<span id="class_AudioStreamPlayer3D_property_bus"></span>

[StringName](class_stringname.md#class_StringName) **bus** = `&"Master"` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_bus)

- void **set_bus** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_bus** ( )

The bus on which this audio is playing.

 **Note:** When setting this property, keep in mind that no validation is performed to see if the given name matches an existing bus. This is because audio bus layouts might be loaded after this property is set. If this given name can't be resolved at runtime, it will fall back to `"Master"`.

---

<span id="class_AudioStreamPlayer3D_property_doppler_tracking"></span>

[DopplerTracking](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_DopplerTracking) **doppler_tracking** = `0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_doppler_tracking)

- void **set_doppler_tracking** ( value: [DopplerTracking](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_DopplerTracking) )
- [DopplerTracking](class_audiostreamplayer3d.md#enum_AudioStreamPlayer3D_DopplerTracking) **get_doppler_tracking** ( )

Decides in which step the Doppler effect should be calculated.

 **Note:** If [doppler_tracking](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_doppler_tracking) is not [DOPPLER_TRACKING_DISABLED](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_DISABLED) but the current [Camera3D](class_camera3d.md#class_Camera3D)/[AudioListener3D](class_audiolistener3d.md#class_AudioListener3D) has doppler tracking disabled, the Doppler effect will be heard but will not take the movement of the current listener into account. If accurate Doppler effect is desired, doppler tracking should be enabled on both the **AudioStreamPlayer3D** and the current [Camera3D](class_camera3d.md#class_Camera3D)/[AudioListener3D](class_audiolistener3d.md#class_AudioListener3D).

---

<span id="class_AudioStreamPlayer3D_property_emission_angle_degrees"></span>

[float](class_float.md#class_float) **emission_angle_degrees** = `45.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_emission_angle_degrees)

- void **set_emission_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_angle** ( )

The angle in which the audio reaches a listener unattenuated.

---

<span id="class_AudioStreamPlayer3D_property_emission_angle_enabled"></span>

[bool](class_bool.md#class_bool) **emission_angle_enabled** = `false` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_emission_angle_enabled)

- void **set_emission_angle_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_emission_angle_enabled** ( )

If `true`, the audio should be attenuated according to the direction of the sound.

---

<span id="class_AudioStreamPlayer3D_property_emission_angle_filter_attenuation_db"></span>

[float](class_float.md#class_float) **emission_angle_filter_attenuation_db** = `-12.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_emission_angle_filter_attenuation_db)

- void **set_emission_angle_filter_attenuation_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_angle_filter_attenuation_db** ( )

Attenuation factor used if listener is outside of [emission_angle_degrees](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_emission_angle_degrees) and [emission_angle_enabled](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_emission_angle_enabled) is set, in decibels.

---

<span id="class_AudioStreamPlayer3D_property_max_db"></span>

[float](class_float.md#class_float) **max_db** = `3.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_max_db)

- void **set_max_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max_db** ( )

Sets the absolute maximum of the sound level, in decibels.

---

<span id="class_AudioStreamPlayer3D_property_max_distance"></span>

[float](class_float.md#class_float) **max_distance** = `0.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_max_distance)

- void **set_max_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max_distance** ( )

The distance past which the sound can no longer be heard at all. Only has an effect if set to a value greater than `0.0`. [max_distance](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_max_distance) works in tandem with [unit_size](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_unit_size). However, unlike [unit_size](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_unit_size) whose behavior depends on the [attenuation_model](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_attenuation_model), [max_distance](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_max_distance) always works in a linear fashion. This can be used to prevent the **AudioStreamPlayer3D** from requiring audio mixing when the listener is far away, which saves CPU resources.

---

<span id="class_AudioStreamPlayer3D_property_max_polyphony"></span>

[int](class_int.md#class_int) **max_polyphony** = `1` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_max_polyphony)

- void **set_max_polyphony** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_polyphony** ( )

The maximum number of sounds this node can play at the same time. Playing additional sounds after this value is reached will cut off the oldest sounds.

---

<span id="class_AudioStreamPlayer3D_property_panning_strength"></span>

[float](class_float.md#class_float) **panning_strength** = `1.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_panning_strength)

- void **set_panning_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_panning_strength** ( )

Scales the panning strength for this node by multiplying the base ProjectSettings.audio/general/3d_panning_strength by this factor. If the product is `0.0` then stereo panning is disabled and the volume is the same for all channels. If the product is `1.0` then one of the channels will be muted when the sound is located exactly to the left (or right) of the listener.

Two speaker stereo arrangements implement the WebAudio standard for StereoPannerNode Panning where the volume is cosine of half the azimuth angle to the ear.

For other speaker arrangements such as the 5.1 and 7.1 the SPCAP (Speaker-Placement Correction Amplitude) algorithm is implemented.

---

<span id="class_AudioStreamPlayer3D_property_pitch_scale"></span>

[float](class_float.md#class_float) **pitch_scale** = `1.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_pitch_scale)

- void **set_pitch_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pitch_scale** ( )

The pitch and the tempo of the audio, as a multiplier of the audio sample's sample rate.

---

<span id="class_AudioStreamPlayer3D_property_playback_type"></span>

[PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **playback_type** = `0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_playback_type)

- void **set_playback_type** ( value: [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) )
- [PlaybackType](class_audioserver.md#enum_AudioServer_PlaybackType) **get_playback_type** ( )

**Experimental:** This property may be changed or removed in future versions.

The playback type of the stream player. If set other than to the default value, it will force that playback type.

---

<span id="class_AudioStreamPlayer3D_property_playing"></span>

[bool](class_bool.md#class_bool) **playing** = `false` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_playing)

- void **set_playing** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_playing** ( )

If `true`, audio is playing or is queued to be played (see [play()](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_play)).

---

<span id="class_AudioStreamPlayer3D_property_stream"></span>

[AudioStream](class_audiostream.md#class_AudioStream) **stream** [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_stream)

- void **set_stream** ( value: [AudioStream](class_audiostream.md#class_AudioStream) )
- [AudioStream](class_audiostream.md#class_AudioStream) **get_stream** ( )

The [AudioStream](class_audiostream.md#class_AudioStream) resource to be played.

---

<span id="class_AudioStreamPlayer3D_property_stream_paused"></span>

[bool](class_bool.md#class_bool) **stream_paused** = `false` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_stream_paused)

- void **set_stream_paused** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_stream_paused** ( )

If `true`, the playback is paused. You can resume it by setting [stream_paused](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_stream_paused) to `false`.

---

<span id="class_AudioStreamPlayer3D_property_unit_size"></span>

[float](class_float.md#class_float) **unit_size** = `10.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_unit_size)

- void **set_unit_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_unit_size** ( )

The factor for the attenuation effect. Higher values make the sound audible over a larger distance.

---

<span id="class_AudioStreamPlayer3D_property_volume_db"></span>

[float](class_float.md#class_float) **volume_db** = `0.0` [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_volume_db)

- void **set_volume_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume_db** ( )

The base sound level before attenuation, in decibels.

---

<span id="class_AudioStreamPlayer3D_property_volume_linear"></span>

[float](class_float.md#class_float) **volume_linear** [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_volume_linear)

- void **set_volume_linear** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume_linear** ( )

The base sound level before attenuation, as a linear value.

 **Note:** This member modifies [volume_db](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_volume_db) for convenience. The returned value is equivalent to the result of @GlobalScope.db_to_linear() on [volume_db](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_volume_db). Setting this member is equivalent to setting [volume_db](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_volume_db) to the result of @GlobalScope.linear_to_db() on a value.

---

### Method Descriptions

<span id="class_AudioStreamPlayer3D_method_get_playback_position"></span>

[float](class_float.md#class_float) **get_playback_position** ( ) [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_get_playback_position)

Returns the position in the [AudioStream](class_audiostream.md#class_AudioStream).

---

<span id="class_AudioStreamPlayer3D_method_get_stream_playback"></span>

[AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) **get_stream_playback** ( ) [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_get_stream_playback)

Returns the [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) object associated with this **AudioStreamPlayer3D**.

---

<span id="class_AudioStreamPlayer3D_method_has_stream_playback"></span>

[bool](class_bool.md#class_bool) **has_stream_playback** ( ) [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_has_stream_playback)

Returns whether the [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer) can return the [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) object or not.

---

<span id="class_AudioStreamPlayer3D_method_play"></span>

void **play** ( from_position: [float](class_float.md#class_float) = 0.0 ) [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_play)

Queues the audio to play on the next physics frame, from the given position `from_position`, in seconds.

---

<span id="class_AudioStreamPlayer3D_method_seek"></span>

void **seek** ( to_position: [float](class_float.md#class_float) ) [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_seek)

Sets the position from which audio will be played, in seconds.

---

<span id="class_AudioStreamPlayer3D_method_stop"></span>

void **stop** ( ) [🔗](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_stop)

Stops the audio.
