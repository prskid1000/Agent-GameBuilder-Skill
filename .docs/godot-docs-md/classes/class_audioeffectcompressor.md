<span id="class_AudioEffectCompressor"></span>

## AudioEffectCompressor

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Adds a compressor audio effect to an audio bus.

Reduces sounds that exceed a certain threshold level, smooths out the dynamics and increases the overall volume.

### Description

Dynamic range compressor reduces the level of the sound when the amplitude goes over a certain threshold in Decibels. One of the main uses of a compressor is to increase the dynamic range by clipping as little as possible (when sound goes over 0dB).

Compressor has many uses in the mix:

- In the Master bus to compress the whole output (although an [AudioEffectHardLimiter](class_audioeffecthardlimiter.md#class_AudioEffectHardLimiter) is probably better).

- In voice channels to ensure they sound as balanced as possible.

- Sidechained. This can reduce the sound level sidechained with another audio bus for threshold detection. This technique is common in video game mixing to the level of music and SFX while voices are being heard.

- Accentuates transients by using a wider attack, making effects sound more punchy.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [attack_us](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_attack_us) | `20.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [gain](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_gain) | `0.0` |
| [float](class_float.md#class_float) | [mix](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_mix) | `1.0` |
| [float](class_float.md#class_float) | [ratio](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_ratio) | `4.0` |
| [float](class_float.md#class_float) | [release_ms](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_release_ms) | `250.0` |
| [StringName](class_stringname.md#class_StringName) | [sidechain](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_sidechain) | `&""` |
| [float](class_float.md#class_float) | [threshold](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_threshold) | `0.0` |

---

### Property Descriptions

<span id="class_AudioEffectCompressor_property_attack_us"></span>

[float](class_float.md#class_float) **attack_us** = `20.0` [🔗](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_attack_us)

- void **set_attack_us** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_attack_us** ( )

Compressor's reaction time when the signal exceeds the threshold, in microseconds. Value can range from 20 to 2000.

---

<span id="class_AudioEffectCompressor_property_gain"></span>

[float](class_float.md#class_float) **gain** = `0.0` [🔗](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_gain)

- void **set_gain** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_gain** ( )

Gain applied to the output signal.

---

<span id="class_AudioEffectCompressor_property_mix"></span>

[float](class_float.md#class_float) **mix** = `1.0` [🔗](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_mix)

- void **set_mix** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_mix** ( )

Balance between original signal and effect signal. Value can range from 0 (totally dry) to 1 (totally wet).

---

<span id="class_AudioEffectCompressor_property_ratio"></span>

[float](class_float.md#class_float) **ratio** = `4.0` [🔗](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_ratio)

- void **set_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_ratio** ( )

Amount of compression applied to the audio once it passes the threshold level. The higher the ratio, the more the loud parts of the audio will be compressed. Value can range from 1 to 48.

---

<span id="class_AudioEffectCompressor_property_release_ms"></span>

[float](class_float.md#class_float) **release_ms** = `250.0` [🔗](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_release_ms)

- void **set_release_ms** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_release_ms** ( )

Compressor's delay time to stop reducing the signal after the signal level falls below the threshold, in milliseconds. Value can range from 20 to 2000.

---

<span id="class_AudioEffectCompressor_property_sidechain"></span>

[StringName](class_stringname.md#class_StringName) **sidechain** = `&""` [🔗](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_sidechain)

- void **set_sidechain** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_sidechain** ( )

Reduce the sound level using another audio bus for threshold detection.

---

<span id="class_AudioEffectCompressor_property_threshold"></span>

[float](class_float.md#class_float) **threshold** = `0.0` [🔗](class_audioeffectcompressor.md#class_AudioEffectCompressor_property_threshold)

- void **set_threshold** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_threshold** ( )

The level above which compression is applied to the audio. Value can range from -60 to 0.
