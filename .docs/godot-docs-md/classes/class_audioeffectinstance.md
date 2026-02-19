<span id="class_AudioEffectInstance"></span>

## AudioEffectInstance

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AudioEffectSpectrumAnalyzerInstance](class_audioeffectspectrumanalyzerinstance.md#class_AudioEffectSpectrumAnalyzerInstance)

Manipulates the audio it receives for a given effect.

### Description

An audio effect instance manipulates the audio it receives for a given effect. This instance is automatically created by an [AudioEffect](class_audioeffect.md#class_AudioEffect) when it is added to a bus, and should usually not be created directly. If necessary, it can be fetched at run-time with [AudioServer.get_bus_effect_instance()](class_audioserver.md#class_AudioServer_method_get_bus_effect_instance).

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Methods


| void | [_process](class_audioeffectinstance.md#class_AudioEffectInstance_private_method__process) ( src_buffer: `const void*`, dst_buffer: `AudioFrame*`, frame_count: [int](class_int.md#class_int) ) | virtual | required |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_process_silence](class_audioeffectinstance.md#class_AudioEffectInstance_private_method__process_silence) ( ) | virtual | const |

---

### Method Descriptions

<span id="class_AudioEffectInstance_private_method__process"></span>

void **_process** ( src_buffer: `const void*`, dst_buffer: `AudioFrame*`, frame_count: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_audioeffectinstance.md#class_AudioEffectInstance_private_method__process)

Called by the [AudioServer](class_audioserver.md#class_AudioServer) to process this effect. When [_process_silence()](class_audioeffectinstance.md#class_AudioEffectInstance_private_method__process_silence) is not overridden or it returns `false`, this method is called only when the bus is active.

 **Note:** It is not useful to override this method in GDScript or C#. Only GDExtension can take advantage of it.

---

<span id="class_AudioEffectInstance_private_method__process_silence"></span>

[bool](class_bool.md#class_bool) **_process_silence** ( ) *virtual* *const* [🔗](class_audioeffectinstance.md#class_AudioEffectInstance_private_method__process_silence)

Override this method to customize the processing behavior of this effect instance.

Should return `true` to force the [AudioServer](class_audioserver.md#class_AudioServer) to always call [_process()](class_audioeffectinstance.md#class_AudioEffectInstance_private_method__process), even if the bus has been muted or cannot otherwise be heard.
