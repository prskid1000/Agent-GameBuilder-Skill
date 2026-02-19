<span id="class_AudioEffectPanner"></span>

## AudioEffectPanner

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Adds a panner audio effect to an audio bus. Pans sound left or right.

### Description

Determines how much of an audio signal is sent to the left and right buses.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [pan](class_audioeffectpanner.md#class_AudioEffectPanner_property_pan) | `0.0` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_AudioEffectPanner_property_pan"></span>

[float](class_float.md#class_float) **pan** = `0.0` [🔗](class_audioeffectpanner.md#class_AudioEffectPanner_property_pan)

- void **set_pan** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pan** ( )

Pan position. Value can range from -1 (fully left) to 1 (fully right).
