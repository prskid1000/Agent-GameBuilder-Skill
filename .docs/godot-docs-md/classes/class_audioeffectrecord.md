<span id="class_AudioEffectRecord"></span>

## AudioEffectRecord

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Audio effect used for recording the sound from an audio bus.

### Description

Allows the user to record the sound from an audio bus into an [AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV). When used on the "Master" audio bus, this includes all audio output by Godot.

Unlike [AudioEffectCapture](class_audioeffectcapture.md#class_AudioEffectCapture), this effect encodes the recording with the given format (8-bit, 16-bit, or compressed) instead of giving access to the raw audio samples.

Can be used (with an [AudioStreamMicrophone](class_audiostreammicrophone.md#class_AudioStreamMicrophone)) to record from a microphone.

 **Note:** ProjectSettings.audio/driver/enable_input must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

### Tutorials

- [Recording with microphone](../tutorials/audio/recording_with_microphone.md)

- Audio Microphone Record Demo

### Properties


| [Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) | [format](class_audioeffectrecord.md#class_AudioEffectRecord_property_format) | `1` |
| --- | --- | --- |

### Methods


| [AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV) | [get_recording](class_audioeffectrecord.md#class_AudioEffectRecord_method_get_recording) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [is_recording_active](class_audioeffectrecord.md#class_AudioEffectRecord_method_is_recording_active) ( ) const |
| void | [set_recording_active](class_audioeffectrecord.md#class_AudioEffectRecord_method_set_recording_active) ( record: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_AudioEffectRecord_property_format"></span>

[Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) **format** = `1` [🔗](class_audioeffectrecord.md#class_AudioEffectRecord_property_format)

- void **set_format** ( value: [Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) )
- [Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) **get_format** ( )

Specifies the format in which the sample will be recorded.

---

### Method Descriptions

<span id="class_AudioEffectRecord_method_get_recording"></span>

[AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV) **get_recording** ( ) *const* [🔗](class_audioeffectrecord.md#class_AudioEffectRecord_method_get_recording)

Returns the recorded sample.

---

<span id="class_AudioEffectRecord_method_is_recording_active"></span>

[bool](class_bool.md#class_bool) **is_recording_active** ( ) *const* [🔗](class_audioeffectrecord.md#class_AudioEffectRecord_method_is_recording_active)

Returns whether the recording is active or not.

---

<span id="class_AudioEffectRecord_method_set_recording_active"></span>

void **set_recording_active** ( record: [bool](class_bool.md#class_bool) ) [🔗](class_audioeffectrecord.md#class_AudioEffectRecord_method_set_recording_active)

If `true`, the sound will be recorded. Note that restarting the recording will remove the previously recorded sample.
