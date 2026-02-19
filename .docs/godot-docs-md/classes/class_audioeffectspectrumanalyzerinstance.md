<span id="class_AudioEffectSpectrumAnalyzerInstance"></span>

## AudioEffectSpectrumAnalyzerInstance

**Inherits:** [AudioEffectInstance](class_audioeffectinstance.md#class_AudioEffectInstance) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Queryable instance of an [AudioEffectSpectrumAnalyzer](class_audioeffectspectrumanalyzer.md#class_AudioEffectSpectrumAnalyzer).

### Description

The runtime part of an [AudioEffectSpectrumAnalyzer](class_audioeffectspectrumanalyzer.md#class_AudioEffectSpectrumAnalyzer), which can be used to query the magnitude of a frequency range on its host bus.

An instance of this class can be obtained with [AudioServer.get_bus_effect_instance()](class_audioserver.md#class_AudioServer_method_get_bus_effect_instance).

### Tutorials

- Audio Spectrum Visualizer Demo

### Methods


| [Vector2](class_vector2.md#class_Vector2) | [get_magnitude_for_frequency_range](class_audioeffectspectrumanalyzerinstance.md#class_AudioEffectSpectrumAnalyzerInstance_method_get_magnitude_for_frequency_range) ( from_hz: [float](class_float.md#class_float), to_hz: [float](class_float.md#class_float), mode: [MagnitudeMode](class_audioeffectspectrumanalyzerinstance.md#enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode) = 1 ) const |
| --- | --- |

---

### Enumerations

<span id="enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode"></span>

enum **MagnitudeMode**: [🔗](class_audioeffectspectrumanalyzerinstance.md#enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode)

<span id="class_AudioEffectSpectrumAnalyzerInstance_constant_MAGNITUDE_AVERAGE"></span>

[MagnitudeMode](class_audioeffectspectrumanalyzerinstance.md#enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode) **MAGNITUDE_AVERAGE** = `0`

Use the average value across the frequency range as magnitude.

<span id="class_AudioEffectSpectrumAnalyzerInstance_constant_MAGNITUDE_MAX"></span>

[MagnitudeMode](class_audioeffectspectrumanalyzerinstance.md#enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode) **MAGNITUDE_MAX** = `1`

Use the maximum value of the frequency range as magnitude.

---

### Method Descriptions

<span id="class_AudioEffectSpectrumAnalyzerInstance_method_get_magnitude_for_frequency_range"></span>

[Vector2](class_vector2.md#class_Vector2) **get_magnitude_for_frequency_range** ( from_hz: [float](class_float.md#class_float), to_hz: [float](class_float.md#class_float), mode: [MagnitudeMode](class_audioeffectspectrumanalyzerinstance.md#enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode) = 1 ) *const* [🔗](class_audioeffectspectrumanalyzerinstance.md#class_AudioEffectSpectrumAnalyzerInstance_method_get_magnitude_for_frequency_range)

Returns the magnitude of the frequencies from `from_hz` to `to_hz` in linear energy as a Vector2. The `x` component of the return value represents the left stereo channel, and `y` represents the right channel.

 `mode` determines how the frequency range will be processed.
