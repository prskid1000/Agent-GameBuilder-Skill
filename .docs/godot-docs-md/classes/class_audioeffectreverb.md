<span id="class_AudioEffectReverb"></span>

## AudioEffectReverb

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Adds a reverberation audio effect to an Audio bus.

### Description

Simulates the sound of acoustic environments such as rooms, concert halls, caverns, or an open spaces.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

- Third Person Shooter (TPS) Demo

### Properties


| [float](class_float.md#class_float) | [damping](class_audioeffectreverb.md#class_AudioEffectReverb_property_damping) | `0.5` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [dry](class_audioeffectreverb.md#class_AudioEffectReverb_property_dry) | `1.0` |
| [float](class_float.md#class_float) | [hipass](class_audioeffectreverb.md#class_AudioEffectReverb_property_hipass) | `0.0` |
| [float](class_float.md#class_float) | [predelay_feedback](class_audioeffectreverb.md#class_AudioEffectReverb_property_predelay_feedback) | `0.4` |
| [float](class_float.md#class_float) | [predelay_msec](class_audioeffectreverb.md#class_AudioEffectReverb_property_predelay_msec) | `150.0` |
| [float](class_float.md#class_float) | [room_size](class_audioeffectreverb.md#class_AudioEffectReverb_property_room_size) | `0.8` |
| [float](class_float.md#class_float) | [spread](class_audioeffectreverb.md#class_AudioEffectReverb_property_spread) | `1.0` |
| [float](class_float.md#class_float) | [wet](class_audioeffectreverb.md#class_AudioEffectReverb_property_wet) | `0.5` |

---

### Property Descriptions

<span id="class_AudioEffectReverb_property_damping"></span>

[float](class_float.md#class_float) **damping** = `0.5` [🔗](class_audioeffectreverb.md#class_AudioEffectReverb_property_damping)

- void **set_damping** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_damping** ( )

Defines how reflective the imaginary room's walls are. Value can range from 0 to 1.

---

<span id="class_AudioEffectReverb_property_dry"></span>

[float](class_float.md#class_float) **dry** = `1.0` [🔗](class_audioeffectreverb.md#class_AudioEffectReverb_property_dry)

- void **set_dry** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_dry** ( )

Output percent of original sound. At 0, only modified sound is outputted. Value can range from 0 to 1.

---

<span id="class_AudioEffectReverb_property_hipass"></span>

[float](class_float.md#class_float) **hipass** = `0.0` [🔗](class_audioeffectreverb.md#class_AudioEffectReverb_property_hipass)

- void **set_hpf** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_hpf** ( )

High-pass filter passes signals with a frequency higher than a certain cutoff frequency and attenuates signals with frequencies lower than the cutoff frequency. Value can range from 0 to 1.

---

<span id="class_AudioEffectReverb_property_predelay_feedback"></span>

[float](class_float.md#class_float) **predelay_feedback** = `0.4` [🔗](class_audioeffectreverb.md#class_AudioEffectReverb_property_predelay_feedback)

- void **set_predelay_feedback** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_predelay_feedback** ( )

Output percent of predelay. Value can range from 0 to 1.

---

<span id="class_AudioEffectReverb_property_predelay_msec"></span>

[float](class_float.md#class_float) **predelay_msec** = `150.0` [🔗](class_audioeffectreverb.md#class_AudioEffectReverb_property_predelay_msec)

- void **set_predelay_msec** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_predelay_msec** ( )

Time between the original signal and the early reflections of the reverb signal, in milliseconds.

---

<span id="class_AudioEffectReverb_property_room_size"></span>

[float](class_float.md#class_float) **room_size** = `0.8` [🔗](class_audioeffectreverb.md#class_AudioEffectReverb_property_room_size)

- void **set_room_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_room_size** ( )

Dimensions of simulated room. Bigger means more echoes. Value can range from 0 to 1.

---

<span id="class_AudioEffectReverb_property_spread"></span>

[float](class_float.md#class_float) **spread** = `1.0` [🔗](class_audioeffectreverb.md#class_AudioEffectReverb_property_spread)

- void **set_spread** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_spread** ( )

Widens or narrows the stereo image of the reverb tail. 1 means fully widens. Value can range from 0 to 1.

---

<span id="class_AudioEffectReverb_property_wet"></span>

[float](class_float.md#class_float) **wet** = `0.5` [🔗](class_audioeffectreverb.md#class_AudioEffectReverb_property_wet)

- void **set_wet** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_wet** ( )

Output percent of modified sound. At 0, only original sound is outputted. Value can range from 0 to 1.
