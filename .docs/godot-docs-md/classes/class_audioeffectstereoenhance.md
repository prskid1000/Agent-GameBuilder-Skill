<span id="class_AudioEffectStereoEnhance"></span>

## AudioEffectStereoEnhance

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An audio effect that can be used to adjust the intensity of stereo panning.

### Description

An audio effect that can be used to adjust the intensity of stereo panning.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [pan_pullout](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_pan_pullout) | `1.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [surround](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_surround) | `0.0` |
| [float](class_float.md#class_float) | [time_pullout_ms](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_time_pullout_ms) | `0.0` |

---

### Property Descriptions

<span id="class_AudioEffectStereoEnhance_property_pan_pullout"></span>

[float](class_float.md#class_float) **pan_pullout** = `1.0` [🔗](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_pan_pullout)

- void **set_pan_pullout** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pan_pullout** ( )

Amplifies the difference between stereo channels, increasing or decreasing existing panning. A value of 0.0 will downmix stereo to mono. Does not affect a mono signal.

---

<span id="class_AudioEffectStereoEnhance_property_surround"></span>

[float](class_float.md#class_float) **surround** = `0.0` [🔗](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_surround)

- void **set_surround** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_surround** ( )

Widens sound stage through phase shifting in conjunction with [time_pullout_ms](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_time_pullout_ms). Just pans sound to the left channel if [time_pullout_ms](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_time_pullout_ms) is 0.

---

<span id="class_AudioEffectStereoEnhance_property_time_pullout_ms"></span>

[float](class_float.md#class_float) **time_pullout_ms** = `0.0` [🔗](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_time_pullout_ms)

- void **set_time_pullout** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_time_pullout** ( )

Widens sound stage through phase shifting in conjunction with [surround](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_surround). Just delays the right channel if [surround](class_audioeffectstereoenhance.md#class_AudioEffectStereoEnhance_property_surround) is 0.
