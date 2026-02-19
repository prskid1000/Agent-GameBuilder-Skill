<span id="class_AudioStreamPolyphonic"></span>

## AudioStreamPolyphonic

**Inherits:** [AudioStream](class_audiostream.md#class_AudioStream) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

### Description

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

Playback control is done via the [AudioStreamPlaybackPolyphonic](class_audiostreamplaybackpolyphonic.md#class_AudioStreamPlaybackPolyphonic) instance set inside the player, which can be obtained via [AudioStreamPlayer.get_stream_playback()](class_audiostreamplayer.md#class_AudioStreamPlayer_method_get_stream_playback), [AudioStreamPlayer2D.get_stream_playback()](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D_method_get_stream_playback) or [AudioStreamPlayer3D.get_stream_playback()](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_method_get_stream_playback) methods. Obtaining the playback instance is only valid after the `stream` property is set as an **AudioStreamPolyphonic** in those players.

### Properties


| [int](class_int.md#class_int) | [polyphony](class_audiostreampolyphonic.md#class_AudioStreamPolyphonic_property_polyphony) | `32` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_AudioStreamPolyphonic_property_polyphony"></span>

[int](class_int.md#class_int) **polyphony** = `32` [🔗](class_audiostreampolyphonic.md#class_AudioStreamPolyphonic_property_polyphony)

- void **set_polyphony** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_polyphony** ( )

Maximum amount of simultaneous streams that can be played.
