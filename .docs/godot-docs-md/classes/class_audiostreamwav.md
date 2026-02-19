<span id="class_AudioStreamWAV"></span>

## AudioStreamWAV

**Inherits:** [AudioStream](class_audiostream.md#class_AudioStream) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Stores audio data loaded from WAV files.

### Description

AudioStreamWAV stores sound samples loaded from WAV files. To play the stored sound, use an [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer) (for non-positional audio) or [AudioStreamPlayer2D](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D)/[AudioStreamPlayer3D](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D) (for positional audio). The sound can be looped.

This class can also be used to store dynamically-generated PCM audio data. See also [AudioStreamGenerator](class_audiostreamgenerator.md#class_AudioStreamGenerator) for procedural audio generation.

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [data](class_audiostreamwav.md#class_AudioStreamWAV_property_data) | `PackedByteArray()` |
| --- | --- | --- |
| [Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) | [format](class_audiostreamwav.md#class_AudioStreamWAV_property_format) | `0` |
| [int](class_int.md#class_int) | [loop_begin](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_begin) | `0` |
| [int](class_int.md#class_int) | [loop_end](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_end) | `0` |
| [LoopMode](class_audiostreamwav.md#enum_AudioStreamWAV_LoopMode) | [loop_mode](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_mode) | `0` |
| [int](class_int.md#class_int) | [mix_rate](class_audiostreamwav.md#class_AudioStreamWAV_property_mix_rate) | `44100` |
| [bool](class_bool.md#class_bool) | [stereo](class_audiostreamwav.md#class_AudioStreamWAV_property_stereo) | `false` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [tags](class_audiostreamwav.md#class_AudioStreamWAV_property_tags) | `{}` |

### Methods


| [AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV) | [load_from_buffer](class_audiostreamwav.md#class_AudioStreamWAV_method_load_from_buffer) ( stream_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), options: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) static |
| --- | --- |
| [AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV) | [load_from_file](class_audiostreamwav.md#class_AudioStreamWAV_method_load_from_file) ( path: [String](class_string.md#class_String), options: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) static |
| Error | [save_to_wav](class_audiostreamwav.md#class_AudioStreamWAV_method_save_to_wav) ( path: [String](class_string.md#class_String) ) |

---

### Enumerations

<span id="enum_AudioStreamWAV_Format"></span>

enum **Format**: [🔗](class_audiostreamwav.md#enum_AudioStreamWAV_Format)

<span id="class_AudioStreamWAV_constant_FORMAT_8_BITS"></span>

[Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) **FORMAT_8_BITS** = `0`

8-bit PCM audio codec.

<span id="class_AudioStreamWAV_constant_FORMAT_16_BITS"></span>

[Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) **FORMAT_16_BITS** = `1`

16-bit PCM audio codec.

<span id="class_AudioStreamWAV_constant_FORMAT_IMA_ADPCM"></span>

[Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) **FORMAT_IMA_ADPCM** = `2`

Audio is lossily compressed as IMA ADPCM.

<span id="class_AudioStreamWAV_constant_FORMAT_QOA"></span>

[Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) **FORMAT_QOA** = `3`

Audio is lossily compressed as Quite OK Audio.

---

<span id="enum_AudioStreamWAV_LoopMode"></span>

enum **LoopMode**: [🔗](class_audiostreamwav.md#enum_AudioStreamWAV_LoopMode)

<span id="class_AudioStreamWAV_constant_LOOP_DISABLED"></span>

[LoopMode](class_audiostreamwav.md#enum_AudioStreamWAV_LoopMode) **LOOP_DISABLED** = `0`

Audio does not loop.

<span id="class_AudioStreamWAV_constant_LOOP_FORWARD"></span>

[LoopMode](class_audiostreamwav.md#enum_AudioStreamWAV_LoopMode) **LOOP_FORWARD** = `1`

Audio loops the data between [loop_begin](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_begin) and [loop_end](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_end), playing forward only.

<span id="class_AudioStreamWAV_constant_LOOP_PINGPONG"></span>

[LoopMode](class_audiostreamwav.md#enum_AudioStreamWAV_LoopMode) **LOOP_PINGPONG** = `2`

Audio loops the data between [loop_begin](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_begin) and [loop_end](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_end), playing back and forth.

<span id="class_AudioStreamWAV_constant_LOOP_BACKWARD"></span>

[LoopMode](class_audiostreamwav.md#enum_AudioStreamWAV_LoopMode) **LOOP_BACKWARD** = `3`

Audio loops the data between [loop_begin](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_begin) and [loop_end](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_end), playing backward only.

---

### Property Descriptions

<span id="class_AudioStreamWAV_property_data"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **data** = `PackedByteArray()` [🔗](class_audiostreamwav.md#class_AudioStreamWAV_property_data)

- void **set_data** ( value: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) )
- [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **get_data** ( )

Contains the audio data in bytes.

 **Note:** If [format](class_audiostreamwav.md#class_AudioStreamWAV_property_format) is set to [FORMAT_8_BITS](class_audiostreamwav.md#class_AudioStreamWAV_constant_FORMAT_8_BITS), this property expects signed 8-bit PCM data. To convert from unsigned 8-bit PCM, subtract 128 from each byte.

 **Note:** If [format](class_audiostreamwav.md#class_AudioStreamWAV_property_format) is set to [FORMAT_QOA](class_audiostreamwav.md#class_AudioStreamWAV_constant_FORMAT_QOA), this property expects data from a full QOA file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) for more details.

---

<span id="class_AudioStreamWAV_property_format"></span>

[Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) **format** = `0` [🔗](class_audiostreamwav.md#class_AudioStreamWAV_property_format)

- void **set_format** ( value: [Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) )
- [Format](class_audiostreamwav.md#enum_AudioStreamWAV_Format) **get_format** ( )

Audio format.

---

<span id="class_AudioStreamWAV_property_loop_begin"></span>

[int](class_int.md#class_int) **loop_begin** = `0` [🔗](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_begin)

- void **set_loop_begin** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_loop_begin** ( )

The loop start point (in number of samples, relative to the beginning of the stream).

---

<span id="class_AudioStreamWAV_property_loop_end"></span>

[int](class_int.md#class_int) **loop_end** = `0` [🔗](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_end)

- void **set_loop_end** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_loop_end** ( )

The loop end point (in number of samples, relative to the beginning of the stream).

---

<span id="class_AudioStreamWAV_property_loop_mode"></span>

[LoopMode](class_audiostreamwav.md#enum_AudioStreamWAV_LoopMode) **loop_mode** = `0` [🔗](class_audiostreamwav.md#class_AudioStreamWAV_property_loop_mode)

- void **set_loop_mode** ( value: [LoopMode](class_audiostreamwav.md#enum_AudioStreamWAV_LoopMode) )
- [LoopMode](class_audiostreamwav.md#enum_AudioStreamWAV_LoopMode) **get_loop_mode** ( )

The loop mode.

---

<span id="class_AudioStreamWAV_property_mix_rate"></span>

[int](class_int.md#class_int) **mix_rate** = `44100` [🔗](class_audiostreamwav.md#class_AudioStreamWAV_property_mix_rate)

- void **set_mix_rate** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_mix_rate** ( )

The sample rate for mixing this audio. Higher values require more storage space, but result in better quality.

In games, common sample rates in use are `11025`, `16000`, `22050`, `32000`, `44100`, and `48000`.

According to the Nyquist-Shannon sampling theorem, there is no quality difference to human hearing when going past 40,000 Hz (since most humans can only hear up to ~20,000 Hz, often less). If you are using lower-pitched sounds such as voices, lower sample rates such as `32000` or `22050` may be usable with no loss in quality.

---

<span id="class_AudioStreamWAV_property_stereo"></span>

[bool](class_bool.md#class_bool) **stereo** = `false` [🔗](class_audiostreamwav.md#class_AudioStreamWAV_property_stereo)

- void **set_stereo** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_stereo** ( )

If `true`, audio is stereo.

---

<span id="class_AudioStreamWAV_property_tags"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **tags** = `{}` [🔗](class_audiostreamwav.md#class_AudioStreamWAV_property_tags)

- void **set_tags** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_tags** ( )

Contains user-defined tags if found in the WAV data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date` (`date` does not have a standard date format).

 **Note:** No tag is *guaranteed* to be present in every file, so make sure to account for the keys not always existing.

 **Note:** Only WAV files using a `LIST` chunk with an identifier of `INFO` to encode the tags are currently supported.

---

### Method Descriptions

<span id="class_AudioStreamWAV_method_load_from_buffer"></span>

[AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV) **load_from_buffer** ( stream_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), options: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) *static* [🔗](class_audiostreamwav.md#class_AudioStreamWAV_method_load_from_buffer)

Creates a new **AudioStreamWAV** instance from the given buffer. The buffer must contain WAV data.

The keys and values of `options` match the properties of [ResourceImporterWAV](class_resourceimporterwav.md#class_ResourceImporterWAV). The usage of `options` is identical to [load_from_file()](class_audiostreamwav.md#class_AudioStreamWAV_method_load_from_file).

---

<span id="class_AudioStreamWAV_method_load_from_file"></span>

[AudioStreamWAV](class_audiostreamwav.md#class_AudioStreamWAV) **load_from_file** ( path: [String](class_string.md#class_String), options: [Dictionary](class_dictionary.md#class_Dictionary) = {} ) *static* [🔗](class_audiostreamwav.md#class_AudioStreamWAV_method_load_from_file)

Creates a new **AudioStreamWAV** instance from the given file path. The file must be in WAV format.

The keys and values of `options` match the properties of [ResourceImporterWAV](class_resourceimporterwav.md#class_ResourceImporterWAV).

 **Example:** Load the first file dropped as a WAV and play it:

::

    @onready var audio_player = $AudioStreamPlayer

    func _ready():
        get_window().files_dropped.connect(_on_files_dropped)

    func _on_files_dropped(files):
        if files[0].get_extension() == "wav":
            audio_player.stream = AudioStreamWAV.load_from_file(files[0], {
                    "force/max_rate": true,
                    "force/max_rate_hz": 11025
                })
            audio_player.play()

---

<span id="class_AudioStreamWAV_method_save_to_wav"></span>

Error **save_to_wav** ( path: [String](class_string.md#class_String) ) [🔗](class_audiostreamwav.md#class_AudioStreamWAV_method_save_to_wav)

Saves the AudioStreamWAV as a WAV file to `path`. Samples with IMA ADPCM or Quite OK Audio formats can't be saved.

 **Note:** A `.wav` extension is automatically appended to `path` if it is missing.
