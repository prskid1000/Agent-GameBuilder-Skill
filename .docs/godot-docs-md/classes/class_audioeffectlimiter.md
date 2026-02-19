<span id="class_AudioEffectLimiter"></span>

## AudioEffectLimiter

**Deprecated:** Use [AudioEffectHardLimiter](class_audioeffecthardlimiter.md#class_AudioEffectHardLimiter) instead.

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Adds a soft-clip limiter audio effect to an Audio bus.

### Description

A limiter is similar to a compressor, but it's less flexible and designed to disallow sound going over a given dB threshold. Adding one in the Master bus is always recommended to reduce the effects of clipping.

Soft clipping starts to reduce the peaks a little below the threshold level and progressively increases its effect as the input level increases such that the threshold is never exceeded.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [ceiling_db](class_audioeffectlimiter.md#class_AudioEffectLimiter_property_ceiling_db) | `-0.1` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [soft_clip_db](class_audioeffectlimiter.md#class_AudioEffectLimiter_property_soft_clip_db) | `2.0` |
| [float](class_float.md#class_float) | [soft_clip_ratio](class_audioeffectlimiter.md#class_AudioEffectLimiter_property_soft_clip_ratio) | `10.0` |
| [float](class_float.md#class_float) | [threshold_db](class_audioeffectlimiter.md#class_AudioEffectLimiter_property_threshold_db) | `0.0` |

---

### Property Descriptions

<span id="class_AudioEffectLimiter_property_ceiling_db"></span>

[float](class_float.md#class_float) **ceiling_db** = `-0.1` [🔗](class_audioeffectlimiter.md#class_AudioEffectLimiter_property_ceiling_db)

- void **set_ceiling_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_ceiling_db** ( )

The waveform's maximum allowed value, in decibels. Value can range from -20 to -0.1.

---

<span id="class_AudioEffectLimiter_property_soft_clip_db"></span>

[float](class_float.md#class_float) **soft_clip_db** = `2.0` [🔗](class_audioeffectlimiter.md#class_AudioEffectLimiter_property_soft_clip_db)

- void **set_soft_clip_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_soft_clip_db** ( )

Applies a gain to the limited waves, in decibels. Value can range from 0 to 6.

---

<span id="class_AudioEffectLimiter_property_soft_clip_ratio"></span>

[float](class_float.md#class_float) **soft_clip_ratio** = `10.0` [🔗](class_audioeffectlimiter.md#class_AudioEffectLimiter_property_soft_clip_ratio)

- void **set_soft_clip_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_soft_clip_ratio** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_AudioEffectLimiter_property_threshold_db"></span>

[float](class_float.md#class_float) **threshold_db** = `0.0` [🔗](class_audioeffectlimiter.md#class_AudioEffectLimiter_property_threshold_db)

- void **set_threshold_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_threshold_db** ( )

Threshold from which the limiter begins to be active, in decibels. Value can range from -30 to 0.
