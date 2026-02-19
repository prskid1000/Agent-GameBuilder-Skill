<span id="class_AudioEffectSpectrumAnalyzer"></span>

## AudioEffectSpectrumAnalyzer

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Audio effect that can be used for real-time audio visualizations.

### Description

This audio effect does not affect sound output, but can be used for real-time audio visualizations.

This resource configures an [AudioEffectSpectrumAnalyzerInstance](class_audioeffectspectrumanalyzerinstance.md#class_AudioEffectSpectrumAnalyzerInstance), which performs the actual analysis at runtime. An instance can be obtained with [AudioServer.get_bus_effect_instance()](class_audioserver.md#class_AudioServer_method_get_bus_effect_instance).

See also [AudioStreamGenerator](class_audiostreamgenerator.md#class_AudioStreamGenerator) for procedurally generating sounds.

### Tutorials

- Audio Spectrum Visualizer Demo

### Properties


| [float](class_float.md#class_float) | [buffer_length](class_audioeffectspectrumanalyzer.md#class_AudioEffectSpectrumAnalyzer_property_buffer_length) | `2.0` |
| --- | --- | --- |
| [FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) | [fft_size](class_audioeffectspectrumanalyzer.md#class_AudioEffectSpectrumAnalyzer_property_fft_size) | `2` |

---

### Enumerations

<span id="enum_AudioEffectSpectrumAnalyzer_FFTSize"></span>

enum **FFTSize**: [🔗](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize)

<span id="class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_256"></span>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) **FFT_SIZE_256** = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest latency, but least stable over time.

<span id="class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_512"></span>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) **FFT_SIZE_512** = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency, but less stable over time.

<span id="class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_1024"></span>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) **FFT_SIZE_1024** = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a compromise between latency and stability over time.

<span id="class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_2048"></span>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) **FFT_SIZE_2048** = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High latency, but stable over time.

<span id="class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_4096"></span>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) **FFT_SIZE_4096** = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest latency, but most stable over time.

<span id="class_AudioEffectSpectrumAnalyzer_constant_FFT_SIZE_MAX"></span>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) **FFT_SIZE_MAX** = `5`

Represents the size of the [FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) enum.

---

### Property Descriptions

<span id="class_AudioEffectSpectrumAnalyzer_property_buffer_length"></span>

[float](class_float.md#class_float) **buffer_length** = `2.0` [🔗](class_audioeffectspectrumanalyzer.md#class_AudioEffectSpectrumAnalyzer_property_buffer_length)

- void **set_buffer_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_buffer_length** ( )

The length of the buffer to keep (in seconds). Higher values keep data around for longer, but require more memory.

---

<span id="class_AudioEffectSpectrumAnalyzer_property_fft_size"></span>

[FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) **fft_size** = `2` [🔗](class_audioeffectspectrumanalyzer.md#class_AudioEffectSpectrumAnalyzer_property_fft_size)

- void **set_fft_size** ( value: [FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) )
- [FFTSize](class_audioeffectspectrumanalyzer.md#enum_AudioEffectSpectrumAnalyzer_FFTSize) **get_fft_size** ( )

The size of the Fast Fourier transform buffer. Higher values smooth out the spectrum analysis over time, but have greater latency. The effects of this higher latency are especially noticeable with sudden amplitude changes.
