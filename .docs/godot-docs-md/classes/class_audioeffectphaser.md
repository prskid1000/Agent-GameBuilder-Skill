<span id="class_AudioEffectPhaser"></span>

## AudioEffectPhaser

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Adds a phaser audio effect to an audio bus.

Combines the original signal with a copy that is slightly out of phase with the original.

### Description

Combines phase-shifted signals with the original signal. The movement of the phase-shifted signals is controlled using a low-frequency oscillator.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [depth](class_audioeffectphaser.md#class_AudioEffectPhaser_property_depth) | `1.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [feedback](class_audioeffectphaser.md#class_AudioEffectPhaser_property_feedback) | `0.7` |
| [float](class_float.md#class_float) | [range_max_hz](class_audioeffectphaser.md#class_AudioEffectPhaser_property_range_max_hz) | `1600.0` |
| [float](class_float.md#class_float) | [range_min_hz](class_audioeffectphaser.md#class_AudioEffectPhaser_property_range_min_hz) | `440.0` |
| [float](class_float.md#class_float) | [rate_hz](class_audioeffectphaser.md#class_AudioEffectPhaser_property_rate_hz) | `0.5` |

---

### Property Descriptions

<span id="class_AudioEffectPhaser_property_depth"></span>

[float](class_float.md#class_float) **depth** = `1.0` [🔗](class_audioeffectphaser.md#class_AudioEffectPhaser_property_depth)

- void **set_depth** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth** ( )

Determines how high the filter frequencies sweep. Low value will primarily affect bass frequencies. High value can sweep high into the treble. Value can range from `0.1` to `4.0`.

---

<span id="class_AudioEffectPhaser_property_feedback"></span>

[float](class_float.md#class_float) **feedback** = `0.7` [🔗](class_audioeffectphaser.md#class_AudioEffectPhaser_property_feedback)

- void **set_feedback** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_feedback** ( )

Output percent of modified sound. Value can range from 0.1 to 0.9.

---

<span id="class_AudioEffectPhaser_property_range_max_hz"></span>

[float](class_float.md#class_float) **range_max_hz** = `1600.0` [🔗](class_audioeffectphaser.md#class_AudioEffectPhaser_property_range_max_hz)

- void **set_range_max_hz** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_range_max_hz** ( )

Determines the maximum frequency affected by the LFO modulations, in Hz. Value can range from 10 to 10000.

---

<span id="class_AudioEffectPhaser_property_range_min_hz"></span>

[float](class_float.md#class_float) **range_min_hz** = `440.0` [🔗](class_audioeffectphaser.md#class_AudioEffectPhaser_property_range_min_hz)

- void **set_range_min_hz** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_range_min_hz** ( )

Determines the minimum frequency affected by the LFO modulations, in Hz. Value can range from 10 to 10000.

---

<span id="class_AudioEffectPhaser_property_rate_hz"></span>

[float](class_float.md#class_float) **rate_hz** = `0.5` [🔗](class_audioeffectphaser.md#class_AudioEffectPhaser_property_rate_hz)

- void **set_rate_hz** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_rate_hz** ( )

Adjusts the rate in Hz at which the effect sweeps up and down across the frequency range.
