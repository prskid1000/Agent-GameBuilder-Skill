<span id="class_VideoStream"></span>

## VideoStream

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VideoStreamTheora](class_videostreamtheora.md#class_VideoStreamTheora)

Base resource for video streams.

### Description

Base resource type for all video streams. Classes that derive from **VideoStream** can all be used as resource types to play back videos in [VideoStreamPlayer](class_videostreamplayer.md#class_VideoStreamPlayer).

### Tutorials

- [Playing videos](../tutorials/animation/playing_videos.md)

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [String](class_string.md#class_String) | [file](class_videostream.md#class_VideoStream_property_file) | `""` |
| --- | --- | --- |

### Methods


| [VideoStreamPlayback](class_videostreamplayback.md#class_VideoStreamPlayback) | [_instantiate_playback](class_videostream.md#class_VideoStream_private_method__instantiate_playback) ( ) | virtual | required |
| --- | --- | --- | --- |

---

### Property Descriptions

<span id="class_VideoStream_property_file"></span>

[String](class_string.md#class_String) **file** = `""` [🔗](class_videostream.md#class_VideoStream_property_file)

- void **set_file** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_file** ( )

The video file path or URI that this **VideoStream** resource handles.

For [VideoStreamTheora](class_videostreamtheora.md#class_VideoStreamTheora), this filename should be an Ogg Theora video file with the `.ogv` extension.

---

### Method Descriptions

<span id="class_VideoStream_private_method__instantiate_playback"></span>

[VideoStreamPlayback](class_videostreamplayback.md#class_VideoStreamPlayback) **_instantiate_playback** ( ) *virtual* |required| [🔗](class_videostream.md#class_VideoStream_private_method__instantiate_playback)

Called when the video starts playing, to initialize and return a subclass of [VideoStreamPlayback](class_videostreamplayback.md#class_VideoStreamPlayback).
