<span id="class_AudioEffectEQ"></span>

## AudioEffectEQ

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AudioEffectEQ10](class_audioeffecteq10.md#class_AudioEffectEQ10), [AudioEffectEQ21](class_audioeffecteq21.md#class_AudioEffectEQ21), [AudioEffectEQ6](class_audioeffecteq6.md#class_AudioEffectEQ6)

Base class for audio equalizers. Gives you control over frequencies.

Use it to create a custom equalizer if [AudioEffectEQ6](class_audioeffecteq6.md#class_AudioEffectEQ6), [AudioEffectEQ10](class_audioeffecteq10.md#class_AudioEffectEQ10) or [AudioEffectEQ21](class_audioeffecteq21.md#class_AudioEffectEQ21) don't fit your needs.

### Description

AudioEffectEQ gives you control over frequencies. Use it to compensate for existing deficiencies in audio. AudioEffectEQs are useful on the Master bus to completely master a mix and give it more character. They are also useful when a game is run on a mobile device, to adjust the mix to that kind of speakers (it can be added but disabled when headphones are plugged).

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Methods


| [int](class_int.md#class_int) | [get_band_count](class_audioeffecteq.md#class_AudioEffectEQ_method_get_band_count) ( ) const |
| --- | --- |
| [float](class_float.md#class_float) | [get_band_gain_db](class_audioeffecteq.md#class_AudioEffectEQ_method_get_band_gain_db) ( band_idx: [int](class_int.md#class_int) ) const |
| void | [set_band_gain_db](class_audioeffecteq.md#class_AudioEffectEQ_method_set_band_gain_db) ( band_idx: [int](class_int.md#class_int), volume_db: [float](class_float.md#class_float) ) |

---

### Method Descriptions

<span id="class_AudioEffectEQ_method_get_band_count"></span>

[int](class_int.md#class_int) **get_band_count** ( ) *const* [🔗](class_audioeffecteq.md#class_AudioEffectEQ_method_get_band_count)

Returns the number of bands of the equalizer.

---

<span id="class_AudioEffectEQ_method_get_band_gain_db"></span>

[float](class_float.md#class_float) **get_band_gain_db** ( band_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioeffecteq.md#class_AudioEffectEQ_method_get_band_gain_db)

Returns the band's gain at the specified index, in dB.

---

<span id="class_AudioEffectEQ_method_set_band_gain_db"></span>

void **set_band_gain_db** ( band_idx: [int](class_int.md#class_int), volume_db: [float](class_float.md#class_float) ) [🔗](class_audioeffecteq.md#class_AudioEffectEQ_method_set_band_gain_db)

Sets band's gain at the specified index, in dB.
