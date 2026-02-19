<span id="class_XRInterfaceExtension"></span>

## XRInterfaceExtension

**Inherits:** [XRInterface](class_xrinterface.md#class_XRInterface) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Base class for XR interface extensions (plugins).

### Description

External XR interface plugins should inherit from this class.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Methods


| void | [_end_frame](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__end_frame) ( ) virtual |
| --- | --- |
| [bool](class_bool.md#class_bool) | [_get_anchor_detection_is_enabled](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_anchor_detection_is_enabled) ( ) | virtual | const |
| [int](class_int.md#class_int) | [_get_camera_feed_id](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_camera_feed_id) ( ) | virtual | const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [_get_camera_transform](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_camera_transform) ( ) virtual |
| [int](class_int.md#class_int) | [_get_capabilities](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_capabilities) ( ) | virtual | const |
| [RID](class_rid.md#class_RID) | [_get_color_texture](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_color_texture) ( ) virtual |
| [RID](class_rid.md#class_RID) | [_get_depth_texture](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_depth_texture) ( ) virtual |
| [StringName](class_stringname.md#class_StringName) | [_get_name](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_name) ( ) | virtual | const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [_get_play_area](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_play_area) ( ) | virtual | const |
| [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) | [_get_play_area_mode](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_play_area_mode) ( ) | virtual | const |
| [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) | [_get_projection_for_view](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_projection_for_view) ( view: [int](class_int.md#class_int), aspect: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) virtual |
| [Vector2](class_vector2.md#class_Vector2) | [_get_render_target_size](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_render_target_size) ( ) virtual |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_suggested_pose_names](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_suggested_pose_names) ( tracker_name: [StringName](class_stringname.md#class_StringName) ) | virtual | const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [_get_suggested_tracker_names](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_suggested_tracker_names) ( ) | virtual | const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [_get_system_info](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_system_info) ( ) | virtual | const |
| [TrackingStatus](class_xrinterface.md#enum_XRInterface_TrackingStatus) | [_get_tracking_status](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_tracking_status) ( ) | virtual | const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [_get_transform_for_view](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_transform_for_view) ( view: [int](class_int.md#class_int), cam_transform: [Transform3D](class_transform3d.md#class_Transform3D) ) virtual |
| [RID](class_rid.md#class_RID) | [_get_velocity_texture](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_velocity_texture) ( ) virtual |
| [int](class_int.md#class_int) | [_get_view_count](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_view_count) ( ) virtual |
| [RID](class_rid.md#class_RID) | [_get_vrs_texture](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_vrs_texture) ( ) virtual |
| [VRSTextureFormat](class_xrinterface.md#enum_XRInterface_VRSTextureFormat) | [_get_vrs_texture_format](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_vrs_texture_format) ( ) virtual |
| [bool](class_bool.md#class_bool) | [_initialize](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__initialize) ( ) virtual |
| [bool](class_bool.md#class_bool) | [_is_initialized](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__is_initialized) ( ) | virtual | const |
| void | [_post_draw_viewport](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__post_draw_viewport) ( render_target: [RID](class_rid.md#class_RID), screen_rect: [Rect2](class_rect2.md#class_Rect2) ) virtual |
| [bool](class_bool.md#class_bool) | [_pre_draw_viewport](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__pre_draw_viewport) ( render_target: [RID](class_rid.md#class_RID) ) virtual |
| void | [_pre_render](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__pre_render) ( ) virtual |
| void | [_process](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__process) ( ) virtual |
| void | [_set_anchor_detection_is_enabled](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__set_anchor_detection_is_enabled) ( enabled: [bool](class_bool.md#class_bool) ) virtual |
| [bool](class_bool.md#class_bool) | [_set_play_area_mode](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__set_play_area_mode) ( mode: [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) ) | virtual | const |
| [bool](class_bool.md#class_bool) | [_supports_play_area_mode](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__supports_play_area_mode) ( mode: [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) ) | virtual | const |
| void | [_trigger_haptic_pulse](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__trigger_haptic_pulse) ( action_name: [String](class_string.md#class_String), tracker_name: [StringName](class_stringname.md#class_StringName), frequency: [float](class_float.md#class_float), amplitude: [float](class_float.md#class_float), duration_sec: [float](class_float.md#class_float), delay_sec: [float](class_float.md#class_float) ) virtual |
| void | [_uninitialize](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__uninitialize) ( ) virtual |
| void | [add_blit](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_add_blit) ( render_target: [RID](class_rid.md#class_RID), src_rect: [Rect2](class_rect2.md#class_Rect2), dst_rect: [Rect2i](class_rect2i.md#class_Rect2i), use_layer: [bool](class_bool.md#class_bool), layer: [int](class_int.md#class_int), apply_lens_distortion: [bool](class_bool.md#class_bool), eye_center: [Vector2](class_vector2.md#class_Vector2), k1: [float](class_float.md#class_float), k2: [float](class_float.md#class_float), upscale: [float](class_float.md#class_float), aspect_ratio: [float](class_float.md#class_float) ) |
| [RID](class_rid.md#class_RID) | [get_color_texture](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_get_color_texture) ( ) |
| [RID](class_rid.md#class_RID) | [get_depth_texture](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_get_depth_texture) ( ) |
| [RID](class_rid.md#class_RID) | [get_render_target_texture](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_get_render_target_texture) ( render_target: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [get_velocity_texture](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_get_velocity_texture) ( ) |

---

### Method Descriptions

<span id="class_XRInterfaceExtension_private_method__end_frame"></span>

void **_end_frame** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__end_frame)

Called if interface is active and queues have been submitted.

---

<span id="class_XRInterfaceExtension_private_method__get_anchor_detection_is_enabled"></span>

[bool](class_bool.md#class_bool) **_get_anchor_detection_is_enabled** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_anchor_detection_is_enabled)

Return `true` if anchor detection is enabled for this interface.

---

<span id="class_XRInterfaceExtension_private_method__get_camera_feed_id"></span>

[int](class_int.md#class_int) **_get_camera_feed_id** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_camera_feed_id)

Returns the camera feed ID for the [CameraFeed](class_camerafeed.md#class_CameraFeed) registered with the [CameraServer](class_cameraserver.md#class_CameraServer) that should be presented as the background on an AR capable device (if applicable).

---

<span id="class_XRInterfaceExtension_private_method__get_camera_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **_get_camera_transform** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_camera_transform)

Returns the [Transform3D](class_transform3d.md#class_Transform3D) that positions the [XRCamera3D](class_xrcamera3d.md#class_XRCamera3D) in the world.

---

<span id="class_XRInterfaceExtension_private_method__get_capabilities"></span>

[int](class_int.md#class_int) **_get_capabilities** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_capabilities)

Returns the capabilities of this interface.

---

<span id="class_XRInterfaceExtension_private_method__get_color_texture"></span>

[RID](class_rid.md#class_RID) **_get_color_texture** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_color_texture)

Return color texture into which to render (if applicable).

---

<span id="class_XRInterfaceExtension_private_method__get_depth_texture"></span>

[RID](class_rid.md#class_RID) **_get_depth_texture** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_depth_texture)

Return depth texture into which to render (if applicable).

---

<span id="class_XRInterfaceExtension_private_method__get_name"></span>

[StringName](class_stringname.md#class_StringName) **_get_name** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_name)

Returns the name of this interface.

---

<span id="class_XRInterfaceExtension_private_method__get_play_area"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **_get_play_area** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_play_area)

Returns a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) that represents the play areas boundaries (if applicable).

---

<span id="class_XRInterfaceExtension_private_method__get_play_area_mode"></span>

[PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) **_get_play_area_mode** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_play_area_mode)

Returns the play area mode that sets up our play area.

---

<span id="class_XRInterfaceExtension_private_method__get_projection_for_view"></span>

[PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array) **_get_projection_for_view** ( view: [int](class_int.md#class_int), aspect: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_projection_for_view)

Returns the projection matrix for the given view as a [PackedFloat64Array](class_packedfloat64array.md#class_PackedFloat64Array).

---

<span id="class_XRInterfaceExtension_private_method__get_render_target_size"></span>

[Vector2](class_vector2.md#class_Vector2) **_get_render_target_size** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_render_target_size)

Returns the size of our render target for this interface, this overrides the size of the [Viewport](class_viewport.md#class_Viewport) marked as the xr viewport.

---

<span id="class_XRInterfaceExtension_private_method__get_suggested_pose_names"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_suggested_pose_names** ( tracker_name: [StringName](class_stringname.md#class_StringName) ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_suggested_pose_names)

Returns a [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) with pose names configured by this interface. Note that user configuration can override this list.

---

<span id="class_XRInterfaceExtension_private_method__get_suggested_tracker_names"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **_get_suggested_tracker_names** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_suggested_tracker_names)

Returns a [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) with tracker names configured by this interface. Note that user configuration can override this list.

---

<span id="class_XRInterfaceExtension_private_method__get_system_info"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **_get_system_info** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_system_info)

Returns a [Dictionary](class_dictionary.md#class_Dictionary) with system information related to this interface.

---

<span id="class_XRInterfaceExtension_private_method__get_tracking_status"></span>

[TrackingStatus](class_xrinterface.md#enum_XRInterface_TrackingStatus) **_get_tracking_status** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_tracking_status)

Returns the current status of our tracking.

---

<span id="class_XRInterfaceExtension_private_method__get_transform_for_view"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **_get_transform_for_view** ( view: [int](class_int.md#class_int), cam_transform: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_transform_for_view)

Returns a [Transform3D](class_transform3d.md#class_Transform3D) for a given view.

---

<span id="class_XRInterfaceExtension_private_method__get_velocity_texture"></span>

[RID](class_rid.md#class_RID) **_get_velocity_texture** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_velocity_texture)

Return velocity texture into which to render (if applicable).

---

<span id="class_XRInterfaceExtension_private_method__get_view_count"></span>

[int](class_int.md#class_int) **_get_view_count** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_view_count)

Returns the number of views this interface requires, 1 for mono, 2 for stereoscopic.

---

<span id="class_XRInterfaceExtension_private_method__get_vrs_texture"></span>

[RID](class_rid.md#class_RID) **_get_vrs_texture** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_vrs_texture)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_XRInterfaceExtension_private_method__get_vrs_texture_format"></span>

[VRSTextureFormat](class_xrinterface.md#enum_XRInterface_VRSTextureFormat) **_get_vrs_texture_format** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_vrs_texture_format)

Returns the format of the texture returned by [_get_vrs_texture()](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__get_vrs_texture).

---

<span id="class_XRInterfaceExtension_private_method__initialize"></span>

[bool](class_bool.md#class_bool) **_initialize** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__initialize)

Initializes the interface, returns `true` on success.

---

<span id="class_XRInterfaceExtension_private_method__is_initialized"></span>

[bool](class_bool.md#class_bool) **_is_initialized** ( ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__is_initialized)

Returns `true` if this interface has been initialized.

---

<span id="class_XRInterfaceExtension_private_method__post_draw_viewport"></span>

void **_post_draw_viewport** ( render_target: [RID](class_rid.md#class_RID), screen_rect: [Rect2](class_rect2.md#class_Rect2) ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__post_draw_viewport)

Called after the XR [Viewport](class_viewport.md#class_Viewport) draw logic has completed.

---

<span id="class_XRInterfaceExtension_private_method__pre_draw_viewport"></span>

[bool](class_bool.md#class_bool) **_pre_draw_viewport** ( render_target: [RID](class_rid.md#class_RID) ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__pre_draw_viewport)

Called if this is our primary **XRInterfaceExtension** before we start processing a [Viewport](class_viewport.md#class_Viewport) for every active XR [Viewport](class_viewport.md#class_Viewport), returns `true` if that viewport should be rendered. An XR interface may return `false` if the user has taken off their headset and we can pause rendering.

---

<span id="class_XRInterfaceExtension_private_method__pre_render"></span>

void **_pre_render** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__pre_render)

Called if this **XRInterfaceExtension** is active before rendering starts. Most XR interfaces will sync tracking at this point in time.

---

<span id="class_XRInterfaceExtension_private_method__process"></span>

void **_process** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__process)

Called if this **XRInterfaceExtension** is active before our physics and game process is called. Most XR interfaces will update its [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) s at this point in time.

---

<span id="class_XRInterfaceExtension_private_method__set_anchor_detection_is_enabled"></span>

void **_set_anchor_detection_is_enabled** ( enabled: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__set_anchor_detection_is_enabled)

Enables anchor detection on this interface if supported.

---

<span id="class_XRInterfaceExtension_private_method__set_play_area_mode"></span>

[bool](class_bool.md#class_bool) **_set_play_area_mode** ( mode: [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__set_play_area_mode)

Set the play area mode for this interface.

---

<span id="class_XRInterfaceExtension_private_method__supports_play_area_mode"></span>

[bool](class_bool.md#class_bool) **_supports_play_area_mode** ( mode: [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) ) *virtual* *const* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__supports_play_area_mode)

Returns `true` if this interface supports this play area mode.

---

<span id="class_XRInterfaceExtension_private_method__trigger_haptic_pulse"></span>

void **_trigger_haptic_pulse** ( action_name: [String](class_string.md#class_String), tracker_name: [StringName](class_stringname.md#class_StringName), frequency: [float](class_float.md#class_float), amplitude: [float](class_float.md#class_float), duration_sec: [float](class_float.md#class_float), delay_sec: [float](class_float.md#class_float) ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__trigger_haptic_pulse)

Triggers a haptic pulse to be emitted on the specified tracker.

---

<span id="class_XRInterfaceExtension_private_method__uninitialize"></span>

void **_uninitialize** ( ) *virtual* [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_private_method__uninitialize)

Uninitialize the interface.

---

<span id="class_XRInterfaceExtension_method_add_blit"></span>

void **add_blit** ( render_target: [RID](class_rid.md#class_RID), src_rect: [Rect2](class_rect2.md#class_Rect2), dst_rect: [Rect2i](class_rect2i.md#class_Rect2i), use_layer: [bool](class_bool.md#class_bool), layer: [int](class_int.md#class_int), apply_lens_distortion: [bool](class_bool.md#class_bool), eye_center: [Vector2](class_vector2.md#class_Vector2), k1: [float](class_float.md#class_float), k2: [float](class_float.md#class_float), upscale: [float](class_float.md#class_float), aspect_ratio: [float](class_float.md#class_float) ) [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_add_blit)

Blits our render results to screen optionally applying lens distortion. This can only be called while processing `_commit_views`.

---

<span id="class_XRInterfaceExtension_method_get_color_texture"></span>

[RID](class_rid.md#class_RID) **get_color_texture** ( ) [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_get_color_texture)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_XRInterfaceExtension_method_get_depth_texture"></span>

[RID](class_rid.md#class_RID) **get_depth_texture** ( ) [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_get_depth_texture)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_XRInterfaceExtension_method_get_render_target_texture"></span>

[RID](class_rid.md#class_RID) **get_render_target_texture** ( render_target: [RID](class_rid.md#class_RID) ) [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_get_render_target_texture)

Returns a valid [RID](class_rid.md#class_RID) for a texture to which we should render the current frame if supported by the interface.

---

<span id="class_XRInterfaceExtension_method_get_velocity_texture"></span>

[RID](class_rid.md#class_RID) **get_velocity_texture** ( ) [🔗](class_xrinterfaceextension.md#class_XRInterfaceExtension_method_get_velocity_texture)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
