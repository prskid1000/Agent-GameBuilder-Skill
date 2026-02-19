<span id="class_AudioStreamOggVorbis"></span>

## AudioStreamOggVorbis

**Inherits:** [AudioStream](class_audiostream.md#class_AudioStream) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A class representing an Ogg Vorbis audio stream.

### Description

The AudioStreamOggVorbis class is a specialized [AudioStream](class_audiostream.md#class_AudioStream) for handling Ogg Vorbis file formats. It offers functionality for loading and playing back Ogg Vorbis files, as well as managing looping and other playback properties. This class is part of the audio stream system, which also supports WAV files through the [AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV) class.

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [int](class_int.md#class_int) | [bar_beats](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_bar_beats) | `4` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [beat_count](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_beat_count) | `0` |
| [float](class_float.md#class_float) | [bpm](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_bpm) | `0.0` |
| [bool](class_bool.md#class_bool) | [loop](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_loop) | `false` |
| [float](class_float.md#class_float) | [loop_offset](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_loop_offset) | `0.0` |
| [OggPacketSequence](class_oggpacketsequence.md#class_OggPacketSequence) | [packet_sequence](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_packet_sequence) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [tags](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_tags) | `{}` |

### Methods


| [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis) | [load_from_buffer](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_method_load_from_buffer) ( stream_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) static |
| --- | --- |
| [AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis) | [load_from_file](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_method_load_from_file) ( path: [String](class_string.md#class_String) ) static |

---

### Property Descriptions

<span id="class_AudioStreamOggVorbis_property_bar_beats"></span>

[int](class_int.md#class_int) **bar_beats** = `4` [🔗](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_bar_beats)

- void **set_bar_beats** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bar_beats** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_AudioStreamOggVorbis_property_beat_count"></span>

[int](class_int.md#class_int) **beat_count** = `0` [🔗](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_beat_count)

- void **set_beat_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_beat_count** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_AudioStreamOggVorbis_property_bpm"></span>

[float](class_float.md#class_float) **bpm** = `0.0` [🔗](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_bpm)

- void **set_bpm** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_bpm** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_AudioStreamOggVorbis_property_loop"></span>

[bool](class_bool.md#class_bool) **loop** = `false` [🔗](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_loop)

- void **set_loop** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_loop** ( )

If `true`, the audio will play again from the specified [loop_offset](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_loop_offset) once it is done playing. Useful for ambient sounds and background music.

---

<span id="class_AudioStreamOggVorbis_property_loop_offset"></span>

[float](class_float.md#class_float) **loop_offset** = `0.0` [🔗](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_loop_offset)

- void **set_loop_offset** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_loop_offset** ( )

Time in seconds at which the stream starts after being looped.

---

<span id="class_AudioStreamOggVorbis_property_packet_sequence"></span>

[OggPacketSequence](class_oggpacketsequence.md#class_OggPacketSequence) **packet_sequence** [🔗](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_packet_sequence)

- void **set_packet_sequence** ( value: [OggPacketSequence](class_oggpacketsequence.md#class_OggPacketSequence) )
- [OggPacketSequence](class_oggpacketsequence.md#class_OggPacketSequence) **get_packet_sequence** ( )

Contains the raw Ogg data for this stream.

---

<span id="class_AudioStreamOggVorbis_property_tags"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **tags** = `{}` [🔗](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_property_tags)

- void **set_tags** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_tags** ( )

Contains user-defined tags if found in the Ogg Vorbis data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date` (`date` does not have a standard date format).

 **Note:** No tag is *guaranteed* to be present in every file, so make sure to account for the keys not always existing.

---

### Method Descriptions

<span id="class_AudioStreamOggVorbis_method_load_from_buffer"></span>

[AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis) **load_from_buffer** ( stream_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) *static* [🔗](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_method_load_from_buffer)

Creates a new **AudioStreamOggVorbis** instance from the given buffer. The buffer must contain Ogg Vorbis data.

---

<span id="class_AudioStreamOggVorbis_method_load_from_file"></span>

[AudioStreamOggVorbis](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis) **load_from_file** ( path: [String](class_string.md#class_String) ) *static* [🔗](class_audiostreamoggvorbis.md#class_AudioStreamOggVorbis_method_load_from_file)

Creates a new **AudioStreamOggVorbis** instance from the given file path. The file must be in Ogg Vorbis format.
