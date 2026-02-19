<span id="class_VideoStreamPlayer"></span>

## VideoStreamPlayer

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A control used for video playback.

### Description

A control used for playback of [VideoStream](class_videostream.md#class_VideoStream) resources.

Supported video formats are Ogg Theora (`.ogv`, [VideoStreamTheora](class_videostreamtheora.md#class_VideoStreamTheora)) and any format exposed via a GDExtension plugin.

 **Warning:** On Web, video playback *will* perform poorly due to missing architecture-specific assembly optimizations.

### Tutorials

- [Playing videos](../tutorials/animation/playing_videos.md)

### Properties


| [int](class_int.md#class_int) | [audio_track](class_videostreamplayer.md#class_VideoStreamPlayer_property_audio_track) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [autoplay](class_videostreamplayer.md#class_VideoStreamPlayer_property_autoplay) | `false` |
| [int](class_int.md#class_int) | [buffering_msec](class_videostreamplayer.md#class_VideoStreamPlayer_property_buffering_msec) | `500` |
| [StringName](class_stringname.md#class_StringName) | [bus](class_videostreamplayer.md#class_VideoStreamPlayer_property_bus) | `&"Master"` |
| [bool](class_bool.md#class_bool) | [expand](class_videostreamplayer.md#class_VideoStreamPlayer_property_expand) | `false` |
| [bool](class_bool.md#class_bool) | [loop](class_videostreamplayer.md#class_VideoStreamPlayer_property_loop) | `false` |
| [bool](class_bool.md#class_bool) | [paused](class_videostreamplayer.md#class_VideoStreamPlayer_property_paused) | `false` |
| [float](class_float.md#class_float) | [speed_scale](class_videostreamplayer.md#class_VideoStreamPlayer_property_speed_scale) | `1.0` |
| [VideoStream](class_videostream.md#class_VideoStream) | [stream](class_videostreamplayer.md#class_VideoStreamPlayer_property_stream) |
| [float](class_float.md#class_float) | [stream_position](class_videostreamplayer.md#class_VideoStreamPlayer_property_stream_position) |
| [float](class_float.md#class_float) | [volume](class_videostreamplayer.md#class_VideoStreamPlayer_property_volume) |
| [float](class_float.md#class_float) | [volume_db](class_videostreamplayer.md#class_VideoStreamPlayer_property_volume_db) | `0.0` |

### Methods


| [float](class_float.md#class_float) | [get_stream_length](class_videostreamplayer.md#class_VideoStreamPlayer_method_get_stream_length) ( ) const |
| --- | --- |
| [String](class_string.md#class_String) | [get_stream_name](class_videostreamplayer.md#class_VideoStreamPlayer_method_get_stream_name) ( ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_video_texture](class_videostreamplayer.md#class_VideoStreamPlayer_method_get_video_texture) ( ) const |
| [bool](class_bool.md#class_bool) | [is_playing](class_videostreamplayer.md#class_VideoStreamPlayer_method_is_playing) ( ) const |
| void | [play](class_videostreamplayer.md#class_VideoStreamPlayer_method_play) ( ) |
| void | [stop](class_videostreamplayer.md#class_VideoStreamPlayer_method_stop) ( ) |

---

### Signals

<span id="class_VideoStreamPlayer_signal_finished"></span>

**finished** ( ) [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_signal_finished)

Emitted when playback is finished.

---

### Property Descriptions

<span id="class_VideoStreamPlayer_property_audio_track"></span>

[int](class_int.md#class_int) **audio_track** = `0` [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_audio_track)

- void **set_audio_track** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_audio_track** ( )

The embedded audio track to play.

---

<span id="class_VideoStreamPlayer_property_autoplay"></span>

[bool](class_bool.md#class_bool) **autoplay** = `false` [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_autoplay)

- void **set_autoplay** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_autoplay** ( )

If `true`, playback starts when the scene loads.

---

<span id="class_VideoStreamPlayer_property_buffering_msec"></span>

[int](class_int.md#class_int) **buffering_msec** = `500` [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_buffering_msec)

- void **set_buffering_msec** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_buffering_msec** ( )

Amount of time in milliseconds to store in buffer while playing.

---

<span id="class_VideoStreamPlayer_property_bus"></span>

[StringName](class_stringname.md#class_StringName) **bus** = `&"Master"` [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_bus)

- void **set_bus** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_bus** ( )

Audio bus to use for sound playback.

---

<span id="class_VideoStreamPlayer_property_expand"></span>

[bool](class_bool.md#class_bool) **expand** = `false` [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_expand)

- void **set_expand** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_expand** ( )

If `true`, the video scales to the control size. Otherwise, the control minimum size will be automatically adjusted to match the video stream's dimensions.

---

<span id="class_VideoStreamPlayer_property_loop"></span>

[bool](class_bool.md#class_bool) **loop** = `false` [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_loop)

- void **set_loop** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_loop** ( )

If `true`, the video restarts when it reaches its end.

---

<span id="class_VideoStreamPlayer_property_paused"></span>

[bool](class_bool.md#class_bool) **paused** = `false` [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_paused)

- void **set_paused** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_paused** ( )

If `true`, the video is paused.

---

<span id="class_VideoStreamPlayer_property_speed_scale"></span>

[float](class_float.md#class_float) **speed_scale** = `1.0` [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_speed_scale)

- void **set_speed_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_speed_scale** ( )

The stream's current speed scale. `1.0` is the normal speed, while `2.0` is double speed and `0.5` is half speed. A speed scale of `0.0` pauses the video, similar to setting [paused](class_videostreamplayer.md#class_VideoStreamPlayer_property_paused) to `true`.

---

<span id="class_VideoStreamPlayer_property_stream"></span>

[VideoStream](class_videostream.md#class_VideoStream) **stream** [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_stream)

- void **set_stream** ( value: [VideoStream](class_videostream.md#class_VideoStream) )
- [VideoStream](class_videostream.md#class_VideoStream) **get_stream** ( )

The assigned video stream. See description for supported formats.

---

<span id="class_VideoStreamPlayer_property_stream_position"></span>

[float](class_float.md#class_float) **stream_position** [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_stream_position)

- void **set_stream_position** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_stream_position** ( )

The current position of the stream, in seconds.

---

<span id="class_VideoStreamPlayer_property_volume"></span>

[float](class_float.md#class_float) **volume** [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_volume)

- void **set_volume** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume** ( )

Audio volume as a linear value.

---

<span id="class_VideoStreamPlayer_property_volume_db"></span>

[float](class_float.md#class_float) **volume_db** = `0.0` [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_property_volume_db)

- void **set_volume_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume_db** ( )

Audio volume in dB.

---

### Method Descriptions

<span id="class_VideoStreamPlayer_method_get_stream_length"></span>

[float](class_float.md#class_float) **get_stream_length** ( ) *const* [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_method_get_stream_length)

The length of the current stream, in seconds.

---

<span id="class_VideoStreamPlayer_method_get_stream_name"></span>

[String](class_string.md#class_String) **get_stream_name** ( ) *const* [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_method_get_stream_name)

Returns the video stream's name, or `"<No Stream>"` if no video stream is assigned.

---

<span id="class_VideoStreamPlayer_method_get_video_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_video_texture** ( ) *const* [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_method_get_video_texture)

Returns the current frame as a [Texture2D](class_texture2d.md#class_Texture2D).

---

<span id="class_VideoStreamPlayer_method_is_playing"></span>

[bool](class_bool.md#class_bool) **is_playing** ( ) *const* [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_method_is_playing)

Returns `true` if the video is playing.

 **Note:** The video is still considered playing if paused during playback.

---

<span id="class_VideoStreamPlayer_method_play"></span>

void **play** ( ) [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_method_play)

Starts the video playback from the beginning. If the video is paused, this will not unpause the video.

---

<span id="class_VideoStreamPlayer_method_stop"></span>

void **stop** ( ) [🔗](class_videostreamplayer.md#class_VideoStreamPlayer_method_stop)

Stops the video playback and sets the stream position to 0.

 **Note:** Although the stream position will be set to 0, the first frame of the video stream won't become the current frame.
