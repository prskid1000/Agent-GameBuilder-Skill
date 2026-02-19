<span id="class_AudioEffectChorus"></span>

## AudioEffectChorus

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Adds a chorus audio effect.

### Description

Adds a chorus audio effect. The effect applies a filter with voices to duplicate the audio source and manipulate it through the filter.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [dry](class_audioeffectchorus.md#class_AudioEffectChorus_property_dry) | `1.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | voice/1/cutoff_hz | `8000.0` |
| [float](class_float.md#class_float) | voice/1/delay_ms | `15.0` |
| [float](class_float.md#class_float) | voice/1/depth_ms | `2.0` |
| [float](class_float.md#class_float) | voice/1/level_db | `0.0` |
| [float](class_float.md#class_float) | voice/1/pan | `-0.5` |
| [float](class_float.md#class_float) | voice/1/rate_hz | `0.8` |
| [float](class_float.md#class_float) | voice/2/cutoff_hz | `8000.0` |
| [float](class_float.md#class_float) | voice/2/delay_ms | `20.0` |
| [float](class_float.md#class_float) | voice/2/depth_ms | `3.0` |
| [float](class_float.md#class_float) | voice/2/level_db | `0.0` |
| [float](class_float.md#class_float) | voice/2/pan | `0.5` |
| [float](class_float.md#class_float) | voice/2/rate_hz | `1.2` |
| [float](class_float.md#class_float) | voice/3/cutoff_hz |
| [float](class_float.md#class_float) | voice/3/delay_ms |
| [float](class_float.md#class_float) | voice/3/depth_ms |
| [float](class_float.md#class_float) | voice/3/level_db |
| [float](class_float.md#class_float) | voice/3/pan |
| [float](class_float.md#class_float) | voice/3/rate_hz |
| [float](class_float.md#class_float) | voice/4/cutoff_hz |
| [float](class_float.md#class_float) | voice/4/delay_ms |
| [float](class_float.md#class_float) | voice/4/depth_ms |
| [float](class_float.md#class_float) | voice/4/level_db |
| [float](class_float.md#class_float) | voice/4/pan |
| [float](class_float.md#class_float) | voice/4/rate_hz |
| [int](class_int.md#class_int) | [voice_count](class_audioeffectchorus.md#class_AudioEffectChorus_property_voice_count) | `2` |
| [float](class_float.md#class_float) | [wet](class_audioeffectchorus.md#class_AudioEffectChorus_property_wet) | `0.5` |

### Methods


| [float](class_float.md#class_float) | [get_voice_cutoff_hz](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_cutoff_hz) ( voice_idx: [int](class_int.md#class_int) ) const |
| --- | --- |
| [float](class_float.md#class_float) | [get_voice_delay_ms](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_delay_ms) ( voice_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_voice_depth_ms](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_depth_ms) ( voice_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_voice_level_db](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_level_db) ( voice_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_voice_pan](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_pan) ( voice_idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_voice_rate_hz](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_rate_hz) ( voice_idx: [int](class_int.md#class_int) ) const |
| void | [set_voice_cutoff_hz](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_cutoff_hz) ( voice_idx: [int](class_int.md#class_int), cutoff_hz: [float](class_float.md#class_float) ) |
| void | [set_voice_delay_ms](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_delay_ms) ( voice_idx: [int](class_int.md#class_int), delay_ms: [float](class_float.md#class_float) ) |
| void | [set_voice_depth_ms](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_depth_ms) ( voice_idx: [int](class_int.md#class_int), depth_ms: [float](class_float.md#class_float) ) |
| void | [set_voice_level_db](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_level_db) ( voice_idx: [int](class_int.md#class_int), level_db: [float](class_float.md#class_float) ) |
| void | [set_voice_pan](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_pan) ( voice_idx: [int](class_int.md#class_int), pan: [float](class_float.md#class_float) ) |
| void | [set_voice_rate_hz](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_rate_hz) ( voice_idx: [int](class_int.md#class_int), rate_hz: [float](class_float.md#class_float) ) |

---

### Property Descriptions

<span id="class_AudioEffectChorus_property_dry"></span>

[float](class_float.md#class_float) **dry** = `1.0` [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_property_dry)

- void **set_dry** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_dry** ( )

The effect's raw signal.

---

.. _class_AudioEffectChorus_property_voice/1/cutoff_hz:

[float](class_float.md#class_float) **voice/1/cutoff_hz** = `8000.0` 🔗

- void **set_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int), cutoff_hz: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's cutoff frequency.

---

.. _class_AudioEffectChorus_property_voice/1/delay_ms:

[float](class_float.md#class_float) **voice/1/delay_ms** = `15.0` 🔗

- void **set_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int), delay_ms: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's signal delay.

---

.. _class_AudioEffectChorus_property_voice/1/depth_ms:

[float](class_float.md#class_float) **voice/1/depth_ms** = `2.0` 🔗

- void **set_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int), depth_ms: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice filter's depth.

---

.. _class_AudioEffectChorus_property_voice/1/level_db:

[float](class_float.md#class_float) **voice/1/level_db** = `0.0` 🔗

- void **set_voice_level_db** ( voice_idx: [int](class_int.md#class_int), level_db: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_level_db** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's volume.

---

.. _class_AudioEffectChorus_property_voice/1/pan:

[float](class_float.md#class_float) **voice/1/pan** = `-0.5` 🔗

- void **set_voice_pan** ( voice_idx: [int](class_int.md#class_int), pan: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_pan** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's pan level.

---

.. _class_AudioEffectChorus_property_voice/1/rate_hz:

[float](class_float.md#class_float) **voice/1/rate_hz** = `0.8` 🔗

- void **set_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int), rate_hz: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's filter rate.

---

.. _class_AudioEffectChorus_property_voice/2/cutoff_hz:

[float](class_float.md#class_float) **voice/2/cutoff_hz** = `8000.0` 🔗

- void **set_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int), cutoff_hz: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's cutoff frequency.

---

.. _class_AudioEffectChorus_property_voice/2/delay_ms:

[float](class_float.md#class_float) **voice/2/delay_ms** = `20.0` 🔗

- void **set_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int), delay_ms: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's signal delay.

---

.. _class_AudioEffectChorus_property_voice/2/depth_ms:

[float](class_float.md#class_float) **voice/2/depth_ms** = `3.0` 🔗

- void **set_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int), depth_ms: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice filter's depth.

---

.. _class_AudioEffectChorus_property_voice/2/level_db:

[float](class_float.md#class_float) **voice/2/level_db** = `0.0` 🔗

- void **set_voice_level_db** ( voice_idx: [int](class_int.md#class_int), level_db: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_level_db** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's volume.

---

.. _class_AudioEffectChorus_property_voice/2/pan:

[float](class_float.md#class_float) **voice/2/pan** = `0.5` 🔗

- void **set_voice_pan** ( voice_idx: [int](class_int.md#class_int), pan: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_pan** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's pan level.

---

.. _class_AudioEffectChorus_property_voice/2/rate_hz:

[float](class_float.md#class_float) **voice/2/rate_hz** = `1.2` 🔗

- void **set_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int), rate_hz: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's filter rate.

---

.. _class_AudioEffectChorus_property_voice/3/cutoff_hz:

[float](class_float.md#class_float) **voice/3/cutoff_hz** 🔗

- void **set_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int), cutoff_hz: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's cutoff frequency.

---

.. _class_AudioEffectChorus_property_voice/3/delay_ms:

[float](class_float.md#class_float) **voice/3/delay_ms** 🔗

- void **set_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int), delay_ms: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's signal delay.

---

.. _class_AudioEffectChorus_property_voice/3/depth_ms:

[float](class_float.md#class_float) **voice/3/depth_ms** 🔗

- void **set_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int), depth_ms: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice filter's depth.

---

.. _class_AudioEffectChorus_property_voice/3/level_db:

[float](class_float.md#class_float) **voice/3/level_db** 🔗

- void **set_voice_level_db** ( voice_idx: [int](class_int.md#class_int), level_db: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_level_db** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's volume.

---

.. _class_AudioEffectChorus_property_voice/3/pan:

[float](class_float.md#class_float) **voice/3/pan** 🔗

- void **set_voice_pan** ( voice_idx: [int](class_int.md#class_int), pan: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_pan** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's pan level.

---

.. _class_AudioEffectChorus_property_voice/3/rate_hz:

[float](class_float.md#class_float) **voice/3/rate_hz** 🔗

- void **set_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int), rate_hz: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's filter rate.

---

.. _class_AudioEffectChorus_property_voice/4/cutoff_hz:

[float](class_float.md#class_float) **voice/4/cutoff_hz** 🔗

- void **set_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int), cutoff_hz: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's cutoff frequency.

---

.. _class_AudioEffectChorus_property_voice/4/delay_ms:

[float](class_float.md#class_float) **voice/4/delay_ms** 🔗

- void **set_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int), delay_ms: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's signal delay.

---

.. _class_AudioEffectChorus_property_voice/4/depth_ms:

[float](class_float.md#class_float) **voice/4/depth_ms** 🔗

- void **set_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int), depth_ms: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice filter's depth.

---

.. _class_AudioEffectChorus_property_voice/4/level_db:

[float](class_float.md#class_float) **voice/4/level_db** 🔗

- void **set_voice_level_db** ( voice_idx: [int](class_int.md#class_int), level_db: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_level_db** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's volume.

---

.. _class_AudioEffectChorus_property_voice/4/pan:

[float](class_float.md#class_float) **voice/4/pan** 🔗

- void **set_voice_pan** ( voice_idx: [int](class_int.md#class_int), pan: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_pan** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's pan level.

---

.. _class_AudioEffectChorus_property_voice/4/rate_hz:

[float](class_float.md#class_float) **voice/4/rate_hz** 🔗

- void **set_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int), rate_hz: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int) ) *const*

The voice's filter rate.

---

<span id="class_AudioEffectChorus_property_voice_count"></span>

[int](class_int.md#class_int) **voice_count** = `2` [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_property_voice_count)

- void **set_voice_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_voice_count** ( )

The number of voices in the effect.

---

<span id="class_AudioEffectChorus_property_wet"></span>

[float](class_float.md#class_float) **wet** = `0.5` [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_property_wet)

- void **set_wet** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_wet** ( )

The effect's processed signal.

---

### Method Descriptions

<span id="class_AudioEffectChorus_method_get_voice_cutoff_hz"></span>

[float](class_float.md#class_float) **get_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_cutoff_hz)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_get_voice_delay_ms"></span>

[float](class_float.md#class_float) **get_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_delay_ms)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_get_voice_depth_ms"></span>

[float](class_float.md#class_float) **get_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_depth_ms)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_get_voice_level_db"></span>

[float](class_float.md#class_float) **get_voice_level_db** ( voice_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_level_db)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_get_voice_pan"></span>

[float](class_float.md#class_float) **get_voice_pan** ( voice_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_pan)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_get_voice_rate_hz"></span>

[float](class_float.md#class_float) **get_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int) ) *const* [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_get_voice_rate_hz)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_set_voice_cutoff_hz"></span>

void **set_voice_cutoff_hz** ( voice_idx: [int](class_int.md#class_int), cutoff_hz: [float](class_float.md#class_float) ) [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_cutoff_hz)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_set_voice_delay_ms"></span>

void **set_voice_delay_ms** ( voice_idx: [int](class_int.md#class_int), delay_ms: [float](class_float.md#class_float) ) [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_delay_ms)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_set_voice_depth_ms"></span>

void **set_voice_depth_ms** ( voice_idx: [int](class_int.md#class_int), depth_ms: [float](class_float.md#class_float) ) [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_depth_ms)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_set_voice_level_db"></span>

void **set_voice_level_db** ( voice_idx: [int](class_int.md#class_int), level_db: [float](class_float.md#class_float) ) [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_level_db)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_set_voice_pan"></span>

void **set_voice_pan** ( voice_idx: [int](class_int.md#class_int), pan: [float](class_float.md#class_float) ) [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_pan)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_AudioEffectChorus_method_set_voice_rate_hz"></span>

void **set_voice_rate_hz** ( voice_idx: [int](class_int.md#class_int), rate_hz: [float](class_float.md#class_float) ) [🔗](class_audioeffectchorus.md#class_AudioEffectChorus_method_set_voice_rate_hz)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
