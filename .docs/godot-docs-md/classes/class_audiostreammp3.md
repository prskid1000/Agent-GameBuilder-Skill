<span id="class_AudioStreamMP3"></span>

## AudioStreamMP3

**Inherits:** [AudioStream](class_audiostream.md#class_AudioStream) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

MP3 audio stream driver.

### Description

MP3 audio stream driver. See [data](class_audiostreammp3.md#class_AudioStreamMP3_property_data) if you want to load an MP3 file at run-time.

 **Note:** This class can optionally support legacy MP1 and MP2 formats, provided that the engine is compiled with the `minimp3_extra_formats=yes` SCons option. These extra formats are not enabled by default.

### Properties


| [int](class_int.md#class_int) | [bar_beats](class_audiostreammp3.md#class_AudioStreamMP3_property_bar_beats) | `4` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [beat_count](class_audiostreammp3.md#class_AudioStreamMP3_property_beat_count) | `0` |
| [float](class_float.md#class_float) | [bpm](class_audiostreammp3.md#class_AudioStreamMP3_property_bpm) | `0.0` |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [data](class_audiostreammp3.md#class_AudioStreamMP3_property_data) | `PackedByteArray()` |
| [bool](class_bool.md#class_bool) | [loop](class_audiostreammp3.md#class_AudioStreamMP3_property_loop) | `false` |
| [float](class_float.md#class_float) | [loop_offset](class_audiostreammp3.md#class_AudioStreamMP3_property_loop_offset) | `0.0` |

### Methods


| [AudioStreamMP3](class_audiostreammp3.md#class_AudioStreamMP3) | [load_from_buffer](class_audiostreammp3.md#class_AudioStreamMP3_method_load_from_buffer) ( stream_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) static |
| --- | --- |
| [AudioStreamMP3](class_audiostreammp3.md#class_AudioStreamMP3) | [load_from_file](class_audiostreammp3.md#class_AudioStreamMP3_method_load_from_file) ( path: [String](class_string.md#class_String) ) static |

---

### Property Descriptions

<span id="class_AudioStreamMP3_property_bar_beats"></span>

[int](class_int.md#class_int) **bar_beats** = `4` [🔗](class_audiostreammp3.md#class_AudioStreamMP3_property_bar_beats)

- void **set_bar_beats** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bar_beats** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_AudioStreamMP3_property_beat_count"></span>

[int](class_int.md#class_int) **beat_count** = `0` [🔗](class_audiostreammp3.md#class_AudioStreamMP3_property_beat_count)

- void **set_beat_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_beat_count** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_AudioStreamMP3_property_bpm"></span>

[float](class_float.md#class_float) **bpm** = `0.0` [🔗](class_audiostreammp3.md#class_AudioStreamMP3_property_bpm)

- void **set_bpm** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_bpm** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_AudioStreamMP3_property_data"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **data** = `PackedByteArray()` [🔗](class_audiostreammp3.md#class_AudioStreamMP3_property_data)

- void **set_data** ( value: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_data** ( )

Contains the audio data in bytes.

You can load a file without having to import it beforehand using the code snippet below. Keep in mind that this snippet loads the whole file into memory and may not be ideal for huge files (hundreds of megabytes or more).

.. tabs::

```
```

    func load_mp3(path):
        var file = FileAccess.open(path, FileAccess.READ)
        var sound = AudioStreamMP3.new()
        sound.data = file.get_buffer(file.get_length())
        return sound

```
```

    public AudioStreamMP3 LoadMP3(string path)
    {
        using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read);
        var sound = new AudioStreamMP3();
        sound.Data = file.GetBuffer(file.GetLength());
        return sound;
    }

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_AudioStreamMP3_property_loop"></span>

[bool](class_bool.md#class_bool) **loop** = `false` [🔗](class_audiostreammp3.md#class_AudioStreamMP3_property_loop)

- void **set_loop** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_loop** ( )

If `true`, the stream will automatically loop when it reaches the end.

---

<span id="class_AudioStreamMP3_property_loop_offset"></span>

[float](class_float.md#class_float) **loop_offset** = `0.0` [🔗](class_audiostreammp3.md#class_AudioStreamMP3_property_loop_offset)

- void **set_loop_offset** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_loop_offset** ( )

Time in seconds at which the stream starts after being looped.

---

### Method Descriptions

<span id="class_AudioStreamMP3_method_load_from_buffer"></span>

[AudioStreamMP3](class_audiostreammp3.md#class_AudioStreamMP3) **load_from_buffer** ( stream_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) *static* [🔗](class_audiostreammp3.md#class_AudioStreamMP3_method_load_from_buffer)

Creates a new **AudioStreamMP3** instance from the given buffer. The buffer must contain MP3 data.

---

<span id="class_AudioStreamMP3_method_load_from_file"></span>

[AudioStreamMP3](class_audiostreammp3.md#class_AudioStreamMP3) **load_from_file** ( path: [String](class_string.md#class_String) ) *static* [🔗](class_audiostreammp3.md#class_AudioStreamMP3_method_load_from_file)

Creates a new **AudioStreamMP3** instance from the given file path. The file must be in MP3 format.
