<span id="class_CameraFeed"></span>

## CameraFeed

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A camera feed gives you access to a single physical camera attached to your device.

### Description

A camera feed gives you access to a single physical camera attached to your device. When enabled, Godot will start capturing frames from the camera which can then be used. See also [CameraServer](class_cameraserver.md#class_CameraServer).

 **Note:** Many cameras will return YCbCr images which are split into two textures and need to be combined in a shader. Godot does this automatically for you if you set the environment to show the camera image in the background.

 **Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no **CameraFeed** s will be available. To get a **CameraFeed** on iOS, the camera plugin from godot-ios-plugins is required.

### Properties


| [bool](class_bool.md#class_bool) | [feed_is_active](class_camerafeed.md#class_CameraFeed_property_feed_is_active) | `false` |
| --- | --- | --- |
| [Transform2D](class_transform2d.md#class_Transform2D) | [feed_transform](class_camerafeed.md#class_CameraFeed_property_feed_transform) | `Transform2D(1, 0, 0, -1, 0, 1)` |
| [Array](class_array.md#class_Array) | [formats](class_camerafeed.md#class_CameraFeed_property_formats) | `[]` |

### Methods


| [bool](class_bool.md#class_bool) | [_activate_feed](class_camerafeed.md#class_CameraFeed_private_method__activate_feed) ( ) virtual |
| --- | --- |
| void | [_deactivate_feed](class_camerafeed.md#class_CameraFeed_private_method__deactivate_feed) ( ) virtual |
| [Array](class_array.md#class_Array) | [_get_formats](class_camerafeed.md#class_CameraFeed_private_method__get_formats) ( ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_set_format](class_camerafeed.md#class_CameraFeed_private_method__set_format) ( index: [int](class_int.md#class_int), parameters: [Dictionary](class_dictionary.md#class_Dictionary) ) virtual |
| [FeedDataType](class_camerafeed.md#enum_CameraFeed_FeedDataType) | [get_datatype](class_camerafeed.md#class_CameraFeed_method_get_datatype) ( ) const |
| [int](class_int.md#class_int) | [get_id](class_camerafeed.md#class_CameraFeed_method_get_id) ( ) const |
| [String](class_string.md#class_String) | [get_name](class_camerafeed.md#class_CameraFeed_method_get_name) ( ) const |
| [FeedPosition](class_camerafeed.md#enum_CameraFeed_FeedPosition) | [get_position](class_camerafeed.md#class_CameraFeed_method_get_position) ( ) const |
| [int](class_int.md#class_int) | [get_texture_tex_id](class_camerafeed.md#class_CameraFeed_method_get_texture_tex_id) ( feed_image_type: [FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) ) |
| void | [set_external](class_camerafeed.md#class_CameraFeed_method_set_external) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [set_format](class_camerafeed.md#class_CameraFeed_method_set_format) ( index: [int](class_int.md#class_int), parameters: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| void | [set_name](class_camerafeed.md#class_CameraFeed_method_set_name) ( name: [String](class_string.md#class_String) ) |
| void | [set_position](class_camerafeed.md#class_CameraFeed_method_set_position) ( position: [FeedPosition](class_camerafeed.md#enum_CameraFeed_FeedPosition) ) |
| void | [set_rgb_image](class_camerafeed.md#class_CameraFeed_method_set_rgb_image) ( rgb_image: [Image](class_image.md#class_Image) ) |
| void | [set_ycbcr_image](class_camerafeed.md#class_CameraFeed_method_set_ycbcr_image) ( ycbcr_image: [Image](class_image.md#class_Image) ) |
| void | [set_ycbcr_images](class_camerafeed.md#class_CameraFeed_method_set_ycbcr_images) ( y_image: [Image](class_image.md#class_Image), cbcr_image: [Image](class_image.md#class_Image) ) |

---

### Signals

<span id="class_CameraFeed_signal_format_changed"></span>

**format_changed** ( ) [🔗](class_camerafeed.md#class_CameraFeed_signal_format_changed)

Emitted when the format has changed.

---

<span id="class_CameraFeed_signal_frame_changed"></span>

**frame_changed** ( ) [🔗](class_camerafeed.md#class_CameraFeed_signal_frame_changed)

Emitted when a new frame is available.

---

### Enumerations

<span id="enum_CameraFeed_FeedDataType"></span>

enum **FeedDataType**: [🔗](class_camerafeed.md#enum_CameraFeed_FeedDataType)

<span id="class_CameraFeed_constant_FEED_NOIMAGE"></span>

[FeedDataType](class_camerafeed.md#enum_CameraFeed_FeedDataType) **FEED_NOIMAGE** = `0`

No image set for the feed.

<span id="class_CameraFeed_constant_FEED_RGB"></span>

[FeedDataType](class_camerafeed.md#enum_CameraFeed_FeedDataType) **FEED_RGB** = `1`

Feed supplies RGB images.

<span id="class_CameraFeed_constant_FEED_YCBCR"></span>

[FeedDataType](class_camerafeed.md#enum_CameraFeed_FeedDataType) **FEED_YCBCR** = `2`

Feed supplies YCbCr images that need to be converted to RGB.

<span id="class_CameraFeed_constant_FEED_YCBCR_SEP"></span>

[FeedDataType](class_camerafeed.md#enum_CameraFeed_FeedDataType) **FEED_YCBCR_SEP** = `3`

Feed supplies separate Y and CbCr images that need to be combined and converted to RGB.

<span id="class_CameraFeed_constant_FEED_EXTERNAL"></span>

[FeedDataType](class_camerafeed.md#enum_CameraFeed_FeedDataType) **FEED_EXTERNAL** = `4`

Feed supplies external image.

---

<span id="enum_CameraFeed_FeedPosition"></span>

enum **FeedPosition**: [🔗](class_camerafeed.md#enum_CameraFeed_FeedPosition)

<span id="class_CameraFeed_constant_FEED_UNSPECIFIED"></span>

[FeedPosition](class_camerafeed.md#enum_CameraFeed_FeedPosition) **FEED_UNSPECIFIED** = `0`

Unspecified position.

<span id="class_CameraFeed_constant_FEED_FRONT"></span>

[FeedPosition](class_camerafeed.md#enum_CameraFeed_FeedPosition) **FEED_FRONT** = `1`

Camera is mounted at the front of the device.

<span id="class_CameraFeed_constant_FEED_BACK"></span>

[FeedPosition](class_camerafeed.md#enum_CameraFeed_FeedPosition) **FEED_BACK** = `2`

Camera is mounted at the back of the device.

---

### Property Descriptions

<span id="class_CameraFeed_property_feed_is_active"></span>

[bool](class_bool.md#class_bool) **feed_is_active** = `false` [🔗](class_camerafeed.md#class_CameraFeed_property_feed_is_active)

- void **set_active** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_active** ( )

If `true`, the feed is active.

---

<span id="class_CameraFeed_property_feed_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **feed_transform** = `Transform2D(1, 0, 0, -1, 0, 1)` [🔗](class_camerafeed.md#class_CameraFeed_property_feed_transform)

- void **set_transform** ( value: [Transform2D](class_transform2d.md#class_Transform2D) )
- [Transform2D](class_transform2d.md#class_Transform2D) **get_transform** ( )

The transform applied to the camera's image.

---

<span id="class_CameraFeed_property_formats"></span>

[Array](class_array.md#class_Array) **formats** = `[]` [🔗](class_camerafeed.md#class_CameraFeed_property_formats)

- [Array](class_array.md#class_Array) **get_formats** ( )

Formats supported by the feed. Each entry is a [Dictionary](class_dictionary.md#class_Dictionary) describing format parameters.

---

### Method Descriptions

<span id="class_CameraFeed_private_method__activate_feed"></span>

[bool](class_bool.md#class_bool) **_activate_feed** ( ) *virtual* [🔗](class_camerafeed.md#class_CameraFeed_private_method__activate_feed)

Called when the camera feed is activated.

---

<span id="class_CameraFeed_private_method__deactivate_feed"></span>

void **_deactivate_feed** ( ) *virtual* [🔗](class_camerafeed.md#class_CameraFeed_private_method__deactivate_feed)

Called when the camera feed is deactivated.

---

<span id="class_CameraFeed_private_method__get_formats"></span>

[Array](class_array.md#class_Array) **_get_formats** ( ) *virtual* *const* [🔗](class_camerafeed.md#class_CameraFeed_private_method__get_formats)

Override this method to define supported formats of the camera feed.

---

<span id="class_CameraFeed_private_method__set_format"></span>

[bool](class_bool.md#class_bool) **_set_format** ( index: [int](class_int.md#class_int), parameters: [Dictionary](class_dictionary.md#class_Dictionary) ) *virtual* [🔗](class_camerafeed.md#class_CameraFeed_private_method__set_format)

Override this method to set the format of the camera feed.

---

<span id="class_CameraFeed_method_get_datatype"></span>

[FeedDataType](class_camerafeed.md#enum_CameraFeed_FeedDataType) **get_datatype** ( ) *const* [🔗](class_camerafeed.md#class_CameraFeed_method_get_datatype)

Returns feed image data type.

---

<span id="class_CameraFeed_method_get_id"></span>

[int](class_int.md#class_int) **get_id** ( ) *const* [🔗](class_camerafeed.md#class_CameraFeed_method_get_id)

Returns the unique ID for this feed.

---

<span id="class_CameraFeed_method_get_name"></span>

[String](class_string.md#class_String) **get_name** ( ) *const* [🔗](class_camerafeed.md#class_CameraFeed_method_get_name)

Returns the camera's name.

---

<span id="class_CameraFeed_method_get_position"></span>

[FeedPosition](class_camerafeed.md#enum_CameraFeed_FeedPosition) **get_position** ( ) *const* [🔗](class_camerafeed.md#class_CameraFeed_method_get_position)

Returns the position of camera on the device.

---

<span id="class_CameraFeed_method_get_texture_tex_id"></span>

[int](class_int.md#class_int) **get_texture_tex_id** ( feed_image_type: [FeedImage](class_cameraserver.md#enum_CameraServer_FeedImage) ) [🔗](class_camerafeed.md#class_CameraFeed_method_get_texture_tex_id)

Returns the texture backend ID (usable by some external libraries that need a handle to a texture to write data).

---

<span id="class_CameraFeed_method_set_external"></span>

void **set_external** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) [🔗](class_camerafeed.md#class_CameraFeed_method_set_external)

Sets the feed as external feed provided by another library.

---

<span id="class_CameraFeed_method_set_format"></span>

[bool](class_bool.md#class_bool) **set_format** ( index: [int](class_int.md#class_int), parameters: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_camerafeed.md#class_CameraFeed_method_set_format)

Sets the feed format parameters for the given `index` in the [formats](class_camerafeed.md#class_CameraFeed_property_formats) array. Returns `true` on success. By default, the YUYV encoded stream is transformed to [FEED_RGB](class_camerafeed.md#class_CameraFeed_constant_FEED_RGB). The YUYV encoded stream output format can be changed by setting `parameters`'s `output` entry to one of the following:

- `"separate"` will result in [FEED_YCBCR_SEP](class_camerafeed.md#class_CameraFeed_constant_FEED_YCBCR_SEP);

- `"grayscale"` will result in desaturated [FEED_RGB](class_camerafeed.md#class_CameraFeed_constant_FEED_RGB);

- `"copy"` will result in [FEED_YCBCR](class_camerafeed.md#class_CameraFeed_constant_FEED_YCBCR).

---

<span id="class_CameraFeed_method_set_name"></span>

void **set_name** ( name: [String](class_string.md#class_String) ) [🔗](class_camerafeed.md#class_CameraFeed_method_set_name)

Sets the camera's name.

---

<span id="class_CameraFeed_method_set_position"></span>

void **set_position** ( position: [FeedPosition](class_camerafeed.md#enum_CameraFeed_FeedPosition) ) [🔗](class_camerafeed.md#class_CameraFeed_method_set_position)

Sets the position of this camera.

---

<span id="class_CameraFeed_method_set_rgb_image"></span>

void **set_rgb_image** ( rgb_image: [Image](class_image.md#class_Image) ) [🔗](class_camerafeed.md#class_CameraFeed_method_set_rgb_image)

Sets RGB image for this feed.

---

<span id="class_CameraFeed_method_set_ycbcr_image"></span>

void **set_ycbcr_image** ( ycbcr_image: [Image](class_image.md#class_Image) ) [🔗](class_camerafeed.md#class_CameraFeed_method_set_ycbcr_image)

Sets YCbCr image for this feed.

---

<span id="class_CameraFeed_method_set_ycbcr_images"></span>

void **set_ycbcr_images** ( y_image: [Image](class_image.md#class_Image), cbcr_image: [Image](class_image.md#class_Image) ) [🔗](class_camerafeed.md#class_CameraFeed_method_set_ycbcr_images)

Sets Y and CbCr images for this feed.
