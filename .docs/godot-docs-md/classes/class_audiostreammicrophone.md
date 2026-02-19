<span id="class_AudioStreamMicrophone"></span>

## AudioStreamMicrophone

**Inherits:** [AudioStream](class_audiostream.md#class_AudioStream) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Plays real-time audio input data.

### Description

When used directly in an [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer) node, **AudioStreamMicrophone** plays back microphone input in real-time. This can be used in conjunction with [AudioEffectCapture](class_audioeffectcapture.md#class_AudioEffectCapture) to process the data or save it.

 **Note:** ProjectSettings.audio/driver/enable_input must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

### Tutorials

- [Recording with microphone](../tutorials/audio/recording_with_microphone.md)

- Audio Mic Record Demo
