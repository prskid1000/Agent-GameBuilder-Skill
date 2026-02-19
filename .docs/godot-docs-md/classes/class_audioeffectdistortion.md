<span id="class_AudioEffectDistortion"></span>

## AudioEffectDistortion

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Adds a distortion audio effect to an Audio bus.

Modifies the sound to make it distorted.

### Description

Different types are available: clip, tan, lo-fi (bit crushing), overdrive, or waveshape.

By distorting the waveform the frequency content changes, which will often make the sound "crunchy" or "abrasive". For games, it can simulate sound coming from some saturated device or speaker very efficiently.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [drive](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_drive) | `0.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [keep_hf_hz](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_keep_hf_hz) | `16000.0` |
| [Mode](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode) | [mode](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_mode) | `0` |
| [float](class_float.md#class_float) | [post_gain](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_post_gain) | `0.0` |
| [float](class_float.md#class_float) | [pre_gain](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_pre_gain) | `0.0` |

---

### Enumerations

<span id="enum_AudioEffectDistortion_Mode"></span>

enum **Mode**: [🔗](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode)

<span id="class_AudioEffectDistortion_constant_MODE_CLIP"></span>

[Mode](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode) **MODE_CLIP** = `0`

Digital distortion effect which cuts off peaks at the top and bottom of the waveform.

<span id="class_AudioEffectDistortion_constant_MODE_ATAN"></span>

[Mode](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode) **MODE_ATAN** = `1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_AudioEffectDistortion_constant_MODE_LOFI"></span>

[Mode](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode) **MODE_LOFI** = `2`

Low-resolution digital distortion effect (bit depth reduction). You can use it to emulate the sound of early digital audio devices.

<span id="class_AudioEffectDistortion_constant_MODE_OVERDRIVE"></span>

[Mode](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode) **MODE_OVERDRIVE** = `3`

Emulates the warm distortion produced by a field effect transistor, which is commonly used in solid-state musical instrument amplifiers. The [drive](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_drive) property has no effect in this mode.

<span id="class_AudioEffectDistortion_constant_MODE_WAVESHAPE"></span>

[Mode](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode) **MODE_WAVESHAPE** = `4`

Waveshaper distortions are used mainly by electronic musicians to achieve an extra-abrasive sound.

---

### Property Descriptions

<span id="class_AudioEffectDistortion_property_drive"></span>

[float](class_float.md#class_float) **drive** = `0.0` [🔗](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_drive)

- void **set_drive** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_drive** ( )

Distortion power. Value can range from 0 to 1.

---

<span id="class_AudioEffectDistortion_property_keep_hf_hz"></span>

[float](class_float.md#class_float) **keep_hf_hz** = `16000.0` [🔗](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_keep_hf_hz)

- void **set_keep_hf_hz** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_keep_hf_hz** ( )

High-pass filter, in Hz. Frequencies higher than this value will not be affected by the distortion. Value can range from 1 to 20000.

---

<span id="class_AudioEffectDistortion_property_mode"></span>

[Mode](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode) **mode** = `0` [🔗](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_mode)

- void **set_mode** ( value: [Mode](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode) )
- [Mode](class_audioeffectdistortion.md#enum_AudioEffectDistortion_Mode) **get_mode** ( )

Distortion type.

---

<span id="class_AudioEffectDistortion_property_post_gain"></span>

[float](class_float.md#class_float) **post_gain** = `0.0` [🔗](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_post_gain)

- void **set_post_gain** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_post_gain** ( )

Increases or decreases the volume after the effect, in decibels. Value can range from -80 to 24.

---

<span id="class_AudioEffectDistortion_property_pre_gain"></span>

[float](class_float.md#class_float) **pre_gain** = `0.0` [🔗](class_audioeffectdistortion.md#class_AudioEffectDistortion_property_pre_gain)

- void **set_pre_gain** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pre_gain** ( )

Increases or decreases the volume before the effect, in decibels. Value can range from -60 to 60.
