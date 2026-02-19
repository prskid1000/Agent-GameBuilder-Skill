<span id="class_AudioEffectCapture"></span>

## AudioEffectCapture

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Captures audio from an audio bus in real-time.

### Description

AudioEffectCapture is an AudioEffect which copies all audio frames from the attached audio effect bus into its internal ring buffer.

Application code should consume these audio frames from this ring buffer using [get_buffer()](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_buffer) and process it as needed, for example to capture data from an [AudioStreamMicrophone](class_audiostreammicrophone.md#class_AudioStreamMicrophone), implement application-defined effects, or to transmit audio over the network. When capturing audio data from a microphone, the format of the samples will be stereo 32-bit floating-point PCM.

Unlike [AudioEffectRecord](class_audioeffectrecord.md#class_AudioEffectRecord), this effect only returns the raw audio samples instead of encoding them into an [AudioStream](class_audiostream.md#class_AudioStream).

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [buffer_length](class_audioeffectcapture.md#class_AudioEffectCapture_property_buffer_length) | `0.1` |
| --- | --- | --- |

### Methods


| [bool](class_bool.md#class_bool) | [can_get_buffer](class_audioeffectcapture.md#class_AudioEffectCapture_method_can_get_buffer) ( frames: [int](class_int.md#class_int) ) const |
| --- | --- |
| void | [clear_buffer](class_audioeffectcapture.md#class_AudioEffectCapture_method_clear_buffer) ( ) |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [get_buffer](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_buffer) ( frames: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_buffer_length_frames](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_buffer_length_frames) ( ) const |
| [int](class_int.md#class_int) | [get_discarded_frames](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_discarded_frames) ( ) const |
| [int](class_int.md#class_int) | [get_frames_available](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_frames_available) ( ) const |
| [int](class_int.md#class_int) | [get_pushed_frames](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_pushed_frames) ( ) const |

---

### Property Descriptions

<span id="class_AudioEffectCapture_property_buffer_length"></span>

[float](class_float.md#class_float) **buffer_length** = `0.1` [🔗](class_audioeffectcapture.md#class_AudioEffectCapture_property_buffer_length)

- void **set_buffer_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_buffer_length** ( )

Length of the internal ring buffer, in seconds. Setting the buffer length will have no effect if already initialized.

---

### Method Descriptions

<span id="class_AudioEffectCapture_method_can_get_buffer"></span>

[bool](class_bool.md#class_bool) **can_get_buffer** ( frames: [int](class_int.md#class_int) ) *const* [🔗](class_audioeffectcapture.md#class_AudioEffectCapture_method_can_get_buffer)

Returns `true` if at least `frames` audio frames are available to read in the internal ring buffer.

---

<span id="class_AudioEffectCapture_method_clear_buffer"></span>

void **clear_buffer** ( ) [🔗](class_audioeffectcapture.md#class_AudioEffectCapture_method_clear_buffer)

Clears the internal ring buffer.

 **Note:** Calling this during a capture can cause the loss of samples which causes popping in the playback.

---

<span id="class_AudioEffectCapture_method_get_buffer"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_buffer** ( frames: [int](class_int.md#class_int) ) [🔗](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_buffer)

Gets the next `frames` audio samples from the internal ring buffer.

Returns a [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) containing exactly `frames` audio samples if available, or an empty [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) if insufficient data was available.

The samples are signed floating-point PCM between `-1` and `1`. You will have to scale them if you want to use them as 8 or 16-bit integer samples. (`v = 0x7fff * samples[0].x`)

---

<span id="class_AudioEffectCapture_method_get_buffer_length_frames"></span>

[int](class_int.md#class_int) **get_buffer_length_frames** ( ) *const* [🔗](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_buffer_length_frames)

Returns the total size of the internal ring buffer in frames.

---

<span id="class_AudioEffectCapture_method_get_discarded_frames"></span>

[int](class_int.md#class_int) **get_discarded_frames** ( ) *const* [🔗](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_discarded_frames)

Returns the number of audio frames discarded from the audio bus due to full buffer.

---

<span id="class_AudioEffectCapture_method_get_frames_available"></span>

[int](class_int.md#class_int) **get_frames_available** ( ) *const* [🔗](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_frames_available)

Returns the number of frames available to read using [get_buffer()](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_buffer).

---

<span id="class_AudioEffectCapture_method_get_pushed_frames"></span>

[int](class_int.md#class_int) **get_pushed_frames** ( ) *const* [🔗](class_audioeffectcapture.md#class_AudioEffectCapture_method_get_pushed_frames)

Returns the number of audio frames inserted from the audio bus.
