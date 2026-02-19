<span id="class_AudioEffectHardLimiter"></span>

## AudioEffectHardLimiter

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Adds a hard limiter audio effect to an Audio bus.

### Description

A limiter is an effect designed to disallow sound from going over a given dB threshold. Hard limiters predict volume peaks, and will smoothly apply gain reduction when a peak crosses the ceiling threshold to prevent clipping and distortion. It preserves the waveform and prevents it from crossing the ceiling threshold. Adding one in the Master bus is recommended as a safety measure to prevent sudden volume peaks from occurring, and to prevent distortion caused by clipping.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [ceiling_db](class_audioeffecthardlimiter.md#class_AudioEffectHardLimiter_property_ceiling_db) | `-0.3` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [pre_gain_db](class_audioeffecthardlimiter.md#class_AudioEffectHardLimiter_property_pre_gain_db) | `0.0` |
| [float](class_float.md#class_float) | [release](class_audioeffecthardlimiter.md#class_AudioEffectHardLimiter_property_release) | `0.1` |

---

### Property Descriptions

<span id="class_AudioEffectHardLimiter_property_ceiling_db"></span>

[float](class_float.md#class_float) **ceiling_db** = `-0.3` [🔗](class_audioeffecthardlimiter.md#class_AudioEffectHardLimiter_property_ceiling_db)

- void **set_ceiling_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_ceiling_db** ( )

The waveform's maximum allowed value, in decibels. This value can range from `-24.0` to `0.0`.

The default value of `-0.3` prevents potential inter-sample peaks (ISP) from crossing over 0 dB, which can cause slight distortion on some older hardware.

---

<span id="class_AudioEffectHardLimiter_property_pre_gain_db"></span>

[float](class_float.md#class_float) **pre_gain_db** = `0.0` [🔗](class_audioeffecthardlimiter.md#class_AudioEffectHardLimiter_property_pre_gain_db)

- void **set_pre_gain_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pre_gain_db** ( )

Gain to apply before limiting, in decibels.

---

<span id="class_AudioEffectHardLimiter_property_release"></span>

[float](class_float.md#class_float) **release** = `0.1` [🔗](class_audioeffecthardlimiter.md#class_AudioEffectHardLimiter_property_release)

- void **set_release** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_release** ( )

Time it takes in seconds for the gain reduction to fully release.
