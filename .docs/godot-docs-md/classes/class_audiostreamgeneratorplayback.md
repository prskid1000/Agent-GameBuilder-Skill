<span id="class_AudioStreamGeneratorPlayback"></span>

## AudioStreamGeneratorPlayback

**Inherits:** [AudioStreamPlaybackResampled](class_audiostreamplaybackresampled.md#class_AudioStreamPlaybackResampled) **<** [AudioStreamPlayback](class_audiostreamplayback.md#class_AudioStreamPlayback) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Plays back audio generated using [AudioStreamGenerator](class_audiostreamgenerator.md#class_AudioStreamGenerator).

### Description

This class is meant to be used with [AudioStreamGenerator](class_audiostreamgenerator.md#class_AudioStreamGenerator) to play back the generated audio in real-time.

### Tutorials

- Audio Generator Demo

- Godot 3.2 will get new audio features

### Methods


| [bool](class_bool.md#class_bool) | [can_push_buffer](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_can_push_buffer) ( amount: [int](class_int.md#class_int) ) const |
| --- | --- |
| void | [clear_buffer](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_clear_buffer) ( ) |
| [int](class_int.md#class_int) | [get_frames_available](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_get_frames_available) ( ) const |
| [int](class_int.md#class_int) | [get_skips](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_get_skips) ( ) const |
| [bool](class_bool.md#class_bool) | [push_buffer](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_push_buffer) ( frames: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) |
| [bool](class_bool.md#class_bool) | [push_frame](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_push_frame) ( frame: [Vector2](class_vector2.md#class_Vector2) ) |

---

### Method Descriptions

<span id="class_AudioStreamGeneratorPlayback_method_can_push_buffer"></span>

[bool](class_bool.md#class_bool) **can_push_buffer** ( amount: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_can_push_buffer)

Returns `true` if a buffer of the size `amount` can be pushed to the audio sample data buffer without overflowing it, `false` otherwise.

---

<span id="class_AudioStreamGeneratorPlayback_method_clear_buffer"></span>

void **clear_buffer** ( ) [🔗](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_clear_buffer)

Clears the audio sample data buffer.

---

<span id="class_AudioStreamGeneratorPlayback_method_get_frames_available"></span>

[int](class_int.md#class_int) **get_frames_available** ( ) *const* [🔗](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_get_frames_available)

Returns the number of frames that can be pushed to the audio sample data buffer without overflowing it. If the result is `0`, the buffer is full.

---

<span id="class_AudioStreamGeneratorPlayback_method_get_skips"></span>

[int](class_int.md#class_int) **get_skips** ( ) *const* [🔗](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_get_skips)

Returns the number of times the playback skipped due to a buffer underrun in the audio sample data. This value is reset at the start of the playback.

---

<span id="class_AudioStreamGeneratorPlayback_method_push_buffer"></span>

[bool](class_bool.md#class_bool) **push_buffer** ( frames: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) ) [🔗](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_push_buffer)

Pushes several audio data frames to the buffer. This is usually more efficient than [push_frame()](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_push_frame) in C# and compiled languages via GDExtension, but [push_buffer()](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_push_buffer) may be *less* efficient in GDScript.

---

<span id="class_AudioStreamGeneratorPlayback_method_push_frame"></span>

[bool](class_bool.md#class_bool) **push_frame** ( frame: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_push_frame)

Pushes a single audio data frame to the buffer. This is usually less efficient than [push_buffer()](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_push_buffer) in C# and compiled languages via GDExtension, but [push_frame()](class_audiostreamgeneratorplayback.md#class_AudioStreamGeneratorPlayback_method_push_frame) may be *more* efficient in GDScript.
