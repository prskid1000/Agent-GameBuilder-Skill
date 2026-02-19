<span id="class_AudioEffectAmplify"></span>

## AudioEffectAmplify

**Inherits:** [AudioEffect](class_audioeffect.md#class_AudioEffect) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Adds an amplifying audio effect to an audio bus.

### Description

Increases or decreases the volume being routed through the audio bus.

### Tutorials

- [Audio buses](../tutorials/audio/audio_buses.md)

### Properties


| [float](class_float.md#class_float) | [volume_db](class_audioeffectamplify.md#class_AudioEffectAmplify_property_volume_db) | `0.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [volume_linear](class_audioeffectamplify.md#class_AudioEffectAmplify_property_volume_linear) |

---

### Property Descriptions

<span id="class_AudioEffectAmplify_property_volume_db"></span>

[float](class_float.md#class_float) **volume_db** = `0.0` [🔗](class_audioeffectamplify.md#class_AudioEffectAmplify_property_volume_db)

- void **set_volume_db** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume_db** ( )

Amount of amplification in decibels. Positive values make the sound louder, negative values make it quieter. Value can range from -80 to 24.

---

<span id="class_AudioEffectAmplify_property_volume_linear"></span>

[float](class_float.md#class_float) **volume_linear** [🔗](class_audioeffectamplify.md#class_AudioEffectAmplify_property_volume_linear)

- void **set_volume_linear** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_volume_linear** ( )

Amount of amplification as a linear value.

 **Note:** This member modifies [volume_db](class_audioeffectamplify.md#class_AudioEffectAmplify_property_volume_db) for convenience. The returned value is equivalent to the result of @GlobalScope.db_to_linear() on [volume_db](class_audioeffectamplify.md#class_AudioEffectAmplify_property_volume_db). Setting this member is equivalent to setting [volume_db](class_audioeffectamplify.md#class_AudioEffectAmplify_property_volume_db) to the result of @GlobalScope.linear_to_db() on a value.
