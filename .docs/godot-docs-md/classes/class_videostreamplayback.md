<span id="class_VideoStreamPlayback"></span>

## VideoStreamPlayback

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Internal class used by [VideoStream](class_videostream.md#class_VideoStream) to manage playback state when played from a [VideoStreamPlayer](class_videostreamplayer.md#class_VideoStreamPlayer).

### Description

This class is intended to be overridden by video decoder extensions with custom implementations of [VideoStream](class_videostream.md#class_VideoStream).

### Methods


| [int](class_int.md#class_int) | [_get_channels](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_channels) ( ) | virtual | const |
| --- | --- | --- | --- |
| [float](class_float.md#class_float) | [_get_length](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_length) ( ) | virtual | const |
| [int](class_int.md#class_int) | [_get_mix_rate](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_mix_rate) ( ) | virtual | const |
| [float](class_float.md#class_float) | [_get_playback_position](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_playback_position) ( ) | virtual | const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [_get_texture](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_texture) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_paused](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__is_paused) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_is_playing](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__is_playing) ( ) | virtual | const |
| void | [_play](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__play) ( ) virtual |
| void | [_seek](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__seek) ( time: [float](class_float.md#class_float) ) virtual |
| void | [_set_audio_track](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__set_audio_track) ( idx: [int](class_int.md#class_int) ) virtual |
| void | [_set_paused](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__set_paused) ( paused: [bool](class_bool.md#class_bool) ) virtual |
| void | [_stop](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__stop) ( ) virtual |
| void | [_update](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__update) ( delta: [float](class_float.md#class_float) ) | virtual | required |
| [int](class_int.md#class_int) | [mix_audio](class_videostreamplayback.md#class_VideoStreamPlayback_method_mix_audio) ( num_frames: [int](class_int.md#class_int), buffer: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) = PackedFloat32Array(), offset: [int](class_int.md#class_int) = 0 ) |

---

### Method Descriptions

<span id="class_VideoStreamPlayback_private_method__get_channels"></span>

[int](class_int.md#class_int) **_get_channels** ( ) *virtual* *const* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_channels)

Returns the number of audio channels.

---

<span id="class_VideoStreamPlayback_private_method__get_length"></span>

[float](class_float.md#class_float) **_get_length** ( ) *virtual* *const* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_length)

Returns the video duration in seconds, if known, or 0 if unknown.

---

<span id="class_VideoStreamPlayback_private_method__get_mix_rate"></span>

[int](class_int.md#class_int) **_get_mix_rate** ( ) *virtual* *const* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_mix_rate)

Returns the audio sample rate used for mixing.

---

<span id="class_VideoStreamPlayback_private_method__get_playback_position"></span>

[float](class_float.md#class_float) **_get_playback_position** ( ) *virtual* *const* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_playback_position)

Return the current playback timestamp. Called in response to the [VideoStreamPlayer.stream_position](class_videostreamplayer.md#class_VideoStreamPlayer_property_stream_position) getter.

---

<span id="class_VideoStreamPlayback_private_method__get_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **_get_texture** ( ) *virtual* *const* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_texture)

Allocates a [Texture2D](class_texture2d.md#class_Texture2D) in which decoded video frames will be drawn.

---

<span id="class_VideoStreamPlayback_private_method__is_paused"></span>

[bool](class_bool.md#class_bool) **_is_paused** ( ) *virtual* *const* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__is_paused)

Returns the paused status, as set by [_set_paused()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__set_paused).

---

<span id="class_VideoStreamPlayback_private_method__is_playing"></span>

[bool](class_bool.md#class_bool) **_is_playing** ( ) *virtual* *const* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__is_playing)

Returns the playback state, as determined by calls to [_play()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__play) and [_stop()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__stop).

---

<span id="class_VideoStreamPlayback_private_method__play"></span>

void **_play** ( ) *virtual* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__play)

Called in response to [VideoStreamPlayer.autoplay](class_videostreamplayer.md#class_VideoStreamPlayer_property_autoplay) or [VideoStreamPlayer.play()](class_videostreamplayer.md#class_VideoStreamPlayer_method_play). Note that manual playback may also invoke [_stop()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__stop) multiple times before this method is called. [_is_playing()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__is_playing) should return `true` once playing.

---

<span id="class_VideoStreamPlayback_private_method__seek"></span>

void **_seek** ( time: [float](class_float.md#class_float) ) *virtual* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__seek)

Seeks to `time` seconds. Called in response to the [VideoStreamPlayer.stream_position](class_videostreamplayer.md#class_VideoStreamPlayer_property_stream_position) setter.

---

<span id="class_VideoStreamPlayback_private_method__set_audio_track"></span>

void **_set_audio_track** ( idx: [int](class_int.md#class_int) ) *virtual* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__set_audio_track)

Select the audio track `idx`. Called when playback starts, and in response to the [VideoStreamPlayer.audio_track](class_videostreamplayer.md#class_VideoStreamPlayer_property_audio_track) setter.

---

<span id="class_VideoStreamPlayback_private_method__set_paused"></span>

void **_set_paused** ( paused: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__set_paused)

Set the paused status of video playback. [_is_paused()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__is_paused) must return `paused`. Called in response to the [VideoStreamPlayer.paused](class_videostreamplayer.md#class_VideoStreamPlayer_property_paused) setter.

---

<span id="class_VideoStreamPlayback_private_method__stop"></span>

void **_stop** ( ) *virtual* [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__stop)

Stops playback. May be called multiple times before [_play()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__play), or in response to [VideoStreamPlayer.stop()](class_videostreamplayer.md#class_VideoStreamPlayer_method_stop). [_is_playing()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__is_playing) should return `false` once stopped.

---

<span id="class_VideoStreamPlayback_private_method__update"></span>

void **_update** ( delta: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__update)

Ticks video playback for `delta` seconds. Called every frame as long as both [_is_paused()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__is_paused) and [_is_playing()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__is_playing) return `true`.

---

<span id="class_VideoStreamPlayback_method_mix_audio"></span>

[int](class_int.md#class_int) **mix_audio** ( num_frames: [int](class_int.md#class_int), buffer: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) = PackedFloat32Array(), offset: [int](class_int.md#class_int) = 0 ) [🔗](class_videostreamplayback.md#class_VideoStreamPlayback_method_mix_audio)

Render `num_frames` audio frames (of [_get_channels()](class_videostreamplayback.md#class_VideoStreamPlayback_private_method__get_channels) floats each) from `buffer`, starting from index `offset` in the array. Returns the number of audio frames rendered, or -1 on error.
