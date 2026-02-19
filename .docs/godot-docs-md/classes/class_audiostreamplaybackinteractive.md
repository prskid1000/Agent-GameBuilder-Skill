<span id="class_AudioStreamPlaybackInteractive"></span>

## AudioStreamPlaybackInteractive

**Inherits:** [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Playback component of [AudioStreamInteractive](class_audiostreaminteractive.md#class_AudioStreamInteractive).

### Description

Playback component of [AudioStreamInteractive](class_audiostreaminteractive.md#class_AudioStreamInteractive). Contains functions to change the currently played clip.

### Methods


| [int](class_int.md#class_int) | [get_current_clip_index](class_audiostreamplaybackinteractive.md#class_AudioStreamPlaybackInteractive_method_get_current_clip_index) ( ) const |
| --- | --- |
| void | [switch_to_clip](class_audiostreamplaybackinteractive.md#class_AudioStreamPlaybackInteractive_method_switch_to_clip) ( clip_index: [int](class_int.md#class_int) ) |
| void | [switch_to_clip_by_name](class_audiostreamplaybackinteractive.md#class_AudioStreamPlaybackInteractive_method_switch_to_clip_by_name) ( clip_name: [StringName](class_stringname.md#class_StringName) ) |

---

### Method Descriptions

<span id="class_AudioStreamPlaybackInteractive_method_get_current_clip_index"></span>

[int](class_int.md#class_int) **get_current_clip_index** ( ) *const* [🔗](class_audiostreamplaybackinteractive.md#class_AudioStreamPlaybackInteractive_method_get_current_clip_index)

Return the index of the currently playing clip. You can use this to get the name of the currently playing clip with [AudioStreamInteractive.get_clip_name()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_clip_name).

 **Example:** Get the currently playing clip name from inside an [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer) node.

.. tabs::

```
```

    var playing_clip_name = stream.get_clip_name(get_stream_playback().get_current_clip_index())

---

<span id="class_AudioStreamPlaybackInteractive_method_switch_to_clip"></span>

void **switch_to_clip** ( clip_index: [int](class_int.md#class_int) ) [🔗](class_audiostreamplaybackinteractive.md#class_AudioStreamPlaybackInteractive_method_switch_to_clip)

Switch to a clip (by index).

---

<span id="class_AudioStreamPlaybackInteractive_method_switch_to_clip_by_name"></span>

void **switch_to_clip_by_name** ( clip_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_audiostreamplaybackinteractive.md#class_AudioStreamPlaybackInteractive_method_switch_to_clip_by_name)

Switch to a clip (by name).
