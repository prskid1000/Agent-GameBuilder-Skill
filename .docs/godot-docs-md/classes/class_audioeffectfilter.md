<span id="class_AudioEffectFilter"></span>

## AudioEffectFilter

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AudioEffectBandLimitFilter](class_audioeffectbandlimitfilter.md#class_AudioEffectBandLimitFilter), [AudioEffectBandPassFilter](class_audioeffectbandpassfilter.md#class_AudioEffectBandPassFilter), [AudioEffectHighPassFilter](class_audioeffecthighpassfilter.md#class_AudioEffectHighPassFilter), [AudioEffectHighShelfFilter](class_audioeffecthighshelffilter.md#class_AudioEffectHighShelfFilter), [AudioEffectLowPassFilter](class_audioeffectlowpassfilter.md#class_AudioEffectLowPassFilter), [AudioEffectLowShelfFilter](class_audioeffectlowshelffilter.md#class_AudioEffectLowShelfFilter), [AudioEffectNotchFilter](class_audioeffectnotchfilter.md#class_AudioEffectNotchFilter)

Adds a filter to the audio bus.

### Description

Allows frequencies other than the [cutoff_hz](class_audioeffectfilter.md#class_AudioEffectFilter_property_cutoff_hz) to pass.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [cutoff_hz](class_audioeffectfilter.md#class_AudioEffectFilter_property_cutoff_hz) | `2000.0` |
| --- | --- | --- |
| [FilterDB](class_audioeffectfilter.md#enum_AudioEffectFilter_FilterDB) | [db](class_audioeffectfilter.md#class_AudioEffectFilter_property_db) | `0` |
| [float](class_float.md#class_float) | [gain](class_audioeffectfilter.md#class_AudioEffectFilter_property_gain) | `1.0` |
| [float](class_float.md#class_float) | [resonance](class_audioeffectfilter.md#class_AudioEffectFilter_property_resonance) | `0.5` |

---

### Enumerations

<span id="enum_AudioEffectFilter_FilterDB"></span>

enum **FilterDB**: [🔗](class_audioeffectfilter.md#enum_AudioEffectFilter_FilterDB)

<span id="class_AudioEffectFilter_constant_FILTER_6DB"></span>

[FilterDB](class_audioeffectfilter.md#enum_AudioEffectFilter_FilterDB) **FILTER_6DB** = `0`

Cutting off at 6dB per octave.

<span id="class_AudioEffectFilter_constant_FILTER_12DB"></span>

[FilterDB](class_audioeffectfilter.md#enum_AudioEffectFilter_FilterDB) **FILTER_12DB** = `1`

Cutting off at 12dB per octave.

<span id="class_AudioEffectFilter_constant_FILTER_18DB"></span>

[FilterDB](class_audioeffectfilter.md#enum_AudioEffectFilter_FilterDB) **FILTER_18DB** = `2`

Cutting off at 18dB per octave.

<span id="class_AudioEffectFilter_constant_FILTER_24DB"></span>

[FilterDB](class_audioeffectfilter.md#enum_AudioEffectFilter_FilterDB) **FILTER_24DB** = `3`

Cutting off at 24dB per octave.

---

### Property Descriptions

<span id="class_AudioEffectFilter_property_cutoff_hz"></span>

[float](class_float.md#class_float) **cutoff_hz** = `2000.0` [🔗](class_audioeffectfilter.md#class_AudioEffectFilter_property_cutoff_hz)

- void **set_cutoff** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_cutoff** ( )

Threshold frequency for the filter, in Hz.

---

<span id="class_AudioEffectFilter_property_db"></span>

[FilterDB](class_audioeffectfilter.md#enum_AudioEffectFilter_FilterDB) **db** = `0` [🔗](class_audioeffectfilter.md#class_AudioEffectFilter_property_db)

- void **set_db** ( value: [FilterDB](class_audioeffectfilter.md#enum_AudioEffectFilter_FilterDB) )
- [FilterDB](class_audioeffectfilter.md#enum_AudioEffectFilter_FilterDB) **get_db** ( )

Steepness of the cutoff curve in dB per octave, also known as the order of the filter. Higher orders have a more aggressive cutoff.

---

<span id="class_AudioEffectFilter_property_gain"></span>

[float](class_float.md#class_float) **gain** = `1.0` [🔗](class_audioeffectfilter.md#class_AudioEffectFilter_property_gain)

- void **set_gain** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_gain** ( )

Gain amount of the frequencies after the filter.

---

<span id="class_AudioEffectFilter_property_resonance"></span>

[float](class_float.md#class_float) **resonance** = `0.5` [🔗](class_audioeffectfilter.md#class_AudioEffectFilter_property_resonance)

- void **set_resonance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_resonance** ( )

Amount of boost in the frequency range near the cutoff frequency.
