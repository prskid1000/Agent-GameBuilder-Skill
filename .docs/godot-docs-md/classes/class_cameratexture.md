<span id="class_CameraTexture"></span>

## CameraTexture

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture provided by a [CameraFeed](class_camerafeed.md#class_CameraFeed).

### Description

This texture gives access to the camera texture provided by a [CameraFeed](class_camerafeed.md#class_CameraFeed).

 **Note:** Many cameras supply YCbCr images which need to be converted in a shader.

### Properties


| [int](class_int.md#class_int) | [camera_feed_id](class_cameratexture.md#class_CameraTexture_property_camera_feed_id) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [camera_is_active](class_cameratexture.md#class_CameraTexture_property_camera_is_active) | `false` |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| [FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) | [which_feed](class_cameratexture.md#class_CameraTexture_property_which_feed) | `0` |

---

### Property Descriptions

<span id="class_CameraTexture_property_camera_feed_id"></span>

[int](class_int.md#class_int) **camera_feed_id** = `0` [🔗](class_cameratexture.md#class_CameraTexture_property_camera_feed_id)

- void **set_camera_feed_id** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_camera_feed_id** ( )

The ID of the [CameraFeed](class_camerafeed.md#class_CameraFeed) for which we want to display the image.

---

<span id="class_CameraTexture_property_camera_is_active"></span>

[bool](class_bool.md#class_bool) **camera_is_active** = `false` [🔗](class_cameratexture.md#class_CameraTexture_property_camera_is_active)

- void **set_camera_active** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_camera_active** ( )

Convenience property that gives access to the active property of the [CameraFeed](class_camerafeed.md#class_CameraFeed).

---

<span id="class_CameraTexture_property_which_feed"></span>

[FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) **which_feed** = `0` [🔗](class_cameratexture.md#class_CameraTexture_property_which_feed)

- void **set_which_feed** ( value: [FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) )
- [FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) **get_which_feed** ( )

Which image within the [CameraFeed](class_camerafeed.md#class_CameraFeed) we want access to, important if the camera image is split in a Y and CbCr component.
