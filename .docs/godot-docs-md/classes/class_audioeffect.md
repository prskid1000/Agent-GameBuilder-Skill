<span id="class_AudioEffect"></span>

## AudioEffect

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AudioEffectAmplify](class_audioeffectamplify.md#class_AudioEffectAmplify), [AudioEffectCapture](class_audioeffectcapture.md#class_AudioEffectCapture), [AudioEffectChorus](class_audioeffectchorus.md#class_AudioEffectChorus), [AudioEffectCompressor](class_audioeffectcompressor.md#class_AudioEffectCompressor), [AudioEffectDelay](class_audioeffectdelay.md#class_AudioEffectDelay), [AudioEffectDistortion](class_audioeffectdistortion.md#class_AudioEffectDistortion), [AudioEffectEQ](class_audioeffecteq.md#class_AudioEffectEQ), [AudioEffectFilter](class_audioeffectfilter.md#class_AudioEffectFilter), [AudioEffectHardLimiter](class_audioeffecthardlimiter.md#class_AudioEffectHardLimiter), [AudioEffectLimiter](class_audioeffectlimiter.md#class_AudioEffectLimiter), [AudioEffectPanner](class_audioeffectpanner.md#class_AudioEffectPanner), [AudioEffectPhaser](class_audioeffectphaser.md#class_AudioEffectPhaser), [AudioEffectPitchShift](class_audioeffectpitchshift.md#class_AudioEffectPitchShift), [AudioEffectRecord](class_audioeffectrecord.md#class_AudioEffectRecord), [AudioEffectReverb](class_audioeffectreverb.md#class_AudioEffectReverb), [AudioEffectSpectrumAnalyzer](class_audioeffectspectrumanalyzer.md#class_AudioEffectSpectrumAnalyzer), [AudioEffectStereoEnhance](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance)

Base class for audio effect resources.

### Description

The base [Resource](class_resource.md#class_Resource) for every audio effect. In the editor, an audio effect can be added to the current bus layout through the Audio panel. At run-time, it is also possible to manipulate audio effects through [AudioServer.add_bus_effect()](class_audioserver.md#class_AudioServer_method_add_bus_effect), [AudioServer.remove_bus_effect()](class_audioserver.md#class_AudioServer_method_remove_bus_effect), and [AudioServer.get_bus_effect()](class_audioserver.md#class_AudioServer_method_get_bus_effect).

When applied on a bus, an audio effect creates a corresponding [AudioEffectInstance](class_audioeffectinstance.md#class_AudioEffectInstance). The instance is directly responsible for manipulating the sound, based on the original audio effect's properties.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

- Audio Microphone Record Demo

### Methods


| [AudioEffectInstance](class_audioeffectinstance.md#class_AudioEffectInstance) | [_instantiate](class_audioeffect.md#class_AudioEffect_private_method__instantiate) ( ) | virtual | required |
| --- | --- | --- | --- |

---

### Method Descriptions

<span id="class_AudioEffect_private_method__instantiate"></span>

[AudioEffectInstance](class_audioeffectinstance.md#class_AudioEffectInstance) **_instantiate** ( ) *virtual* |required| [🔗](class_audioeffect.md#class_AudioEffect_private_method__instantiate)

Override this method to customize the [AudioEffectInstance](class_audioeffectinstance.md#class_AudioEffectInstance) created when this effect is applied on a bus in the editor's Audio panel, or through [AudioServer.add_bus_effect()](class_audioserver.md#class_AudioServer_method_add_bus_effect).

::

    extends AudioEffect

    @export var strength = 4.0

    func _instantiate():
        var effect = CustomAudioEffectInstance.new()
        effect.base = self

        return effect

 **Note:** It is recommended to keep a reference to the original **AudioEffect** in the new instance. Depending on the implementation this allows the effect instance to listen for changes at run-time and be modified accordingly.
