<span id="class_XRInterface"></span>

## XRInterface

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [MobileVRInterface](class_mobilevrinterface.md#class_MobileVRInterface), [OpenXRInterface](class_openxrinterface.md#class_OpenXRInterface), [WebXRInterface](class_webxrinterface.md#class_WebXRInterface), [XRInterfaceExtension](class_xrinterfaceextension.md#class_XRInterfaceExtension)

Base class for an XR interface implementation.

### Description

This class needs to be implemented to make an AR or VR platform available to Godot and these should be implemented as C++ modules or GDExtension modules. Part of the interface is exposed to GDScript so you can detect, enable and configure an AR or VR platform.

Interfaces should be written in such a way that simply enabling them will give us a working setup. You can query the available interfaces through [XRServer](class_xrserver.md#class_XRServer).

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [bool](class_bool.md#class_bool) | [ar_is_anchor_detection_enabled](class_xrinterface.md#class_XRInterface_property_ar_is_anchor_detection_enabled) | `false` |
| --- | --- | --- |
| [EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode) | [environment_blend_mode](class_xrinterface.md#class_XRInterface_property_environment_blend_mode) | `0` |
| [bool](class_bool.md#class_bool) | [interface_is_primary](class_xrinterface.md#class_XRInterface_property_interface_is_primary) | `false` |
| [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) | [xr_play_area_mode](class_xrinterface.md#class_XRInterface_property_xr_play_area_mode) | `0` |

### Methods


| [int](class_int.md#class_int) | [get_camera_feed_id](class_xrinterface.md#class_XRInterface_method_get_camera_feed_id) ( ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_capabilities](class_xrinterface.md#class_XRInterface_method_get_capabilities) ( ) const |
| [StringName](class_stringname.md#class_StringName) | [get_name](class_xrinterface.md#class_XRInterface_method_get_name) ( ) const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [get_play_area](class_xrinterface.md#class_XRInterface_method_get_play_area) ( ) const |
| [Projection](class_projection.md#class_Projection) | [get_projection_for_view](class_xrinterface.md#class_XRInterface_method_get_projection_for_view) ( view: [int](class_int.md#class_int), aspect: [float](class_float.md#class_float), near: [float](class_float.md#class_float), far: [float](class_float.md#class_float) ) |
| [Vector2](class_vector2.md#class_Vector2) | [get_render_target_size](class_xrinterface.md#class_XRInterface_method_get_render_target_size) ( ) |
| [Array](class_array.md#class_Array) | [get_supported_environment_blend_modes](class_xrinterface.md#class_XRInterface_method_get_supported_environment_blend_modes) ( ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_system_info](class_xrinterface.md#class_XRInterface_method_get_system_info) ( ) |
| [TrackingStatus](class_xrinterface.md#enum_XRInterface_TrackingStatus) | [get_tracking_status](class_xrinterface.md#class_XRInterface_method_get_tracking_status) ( ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_transform_for_view](class_xrinterface.md#class_XRInterface_method_get_transform_for_view) ( view: [int](class_int.md#class_int), cam_transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| [int](class_int.md#class_int) | [get_view_count](class_xrinterface.md#class_XRInterface_method_get_view_count) ( ) |
| [bool](class_bool.md#class_bool) | [initialize](class_xrinterface.md#class_XRInterface_method_initialize) ( ) |
| [bool](class_bool.md#class_bool) | [is_initialized](class_xrinterface.md#class_XRInterface_method_is_initialized) ( ) const |
| [bool](class_bool.md#class_bool) | [is_passthrough_enabled](class_xrinterface.md#class_XRInterface_method_is_passthrough_enabled) ( ) |
| [bool](class_bool.md#class_bool) | [is_passthrough_supported](class_xrinterface.md#class_XRInterface_method_is_passthrough_supported) ( ) |
| [bool](class_bool.md#class_bool) | [set_environment_blend_mode](class_xrinterface.md#class_XRInterface_method_set_environment_blend_mode) ( mode: [EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode) ) |
| [bool](class_bool.md#class_bool) | [set_play_area_mode](class_xrinterface.md#class_XRInterface_method_set_play_area_mode) ( mode: [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) ) |
| [bool](class_bool.md#class_bool) | [start_passthrough](class_xrinterface.md#class_XRInterface_method_start_passthrough) ( ) |
| void | [stop_passthrough](class_xrinterface.md#class_XRInterface_method_stop_passthrough) ( ) |
| [bool](class_bool.md#class_bool) | [supports_play_area_mode](class_xrinterface.md#class_XRInterface_method_supports_play_area_mode) ( mode: [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) ) |
| void | [trigger_haptic_pulse](class_xrinterface.md#class_XRInterface_method_trigger_haptic_pulse) ( action_name: [String](class_string.md#class_String), tracker_name: [StringName](class_stringname.md#class_StringName), frequency: [float](class_float.md#class_float), amplitude: [float](class_float.md#class_float), duration_sec: [float](class_float.md#class_float), delay_sec: [float](class_float.md#class_float) ) |
| void | [uninitialize](class_xrinterface.md#class_XRInterface_method_uninitialize) ( ) |

---

### Signals

<span id="class_XRInterface_signal_play_area_changed"></span>

**play_area_changed** ( mode: [int](class_int.md#class_int) ) [🔗](class_xrinterface.md#class_XRInterface_signal_play_area_changed)

Emitted when the play area is changed. This can be a result of the player resetting the boundary or entering a new play area, the player changing the play area mode, the world scale changing or the player resetting their headset orientation.

---

### Enumerations

<span id="enum_XRInterface_Capabilities"></span>

enum **Capabilities**: [🔗](class_xrinterface.md#enum_XRInterface_Capabilities)

<span id="class_XRInterface_constant_XR_NONE"></span>

[Capabilities](class_xrinterface.md#enum_XRInterface_Capabilities) **XR_NONE** = `0`

No XR capabilities.

<span id="class_XRInterface_constant_XR_MONO"></span>

[Capabilities](class_xrinterface.md#enum_XRInterface_Capabilities) **XR_MONO** = `1`

This interface can work with normal rendering output (non-HMD based AR).

<span id="class_XRInterface_constant_XR_STEREO"></span>

[Capabilities](class_xrinterface.md#enum_XRInterface_Capabilities) **XR_STEREO** = `2`

This interface supports stereoscopic rendering.

<span id="class_XRInterface_constant_XR_QUAD"></span>

[Capabilities](class_xrinterface.md#enum_XRInterface_Capabilities) **XR_QUAD** = `4`

This interface supports quad rendering (not yet supported by Godot).

<span id="class_XRInterface_constant_XR_VR"></span>

[Capabilities](class_xrinterface.md#enum_XRInterface_Capabilities) **XR_VR** = `8`

This interface supports VR.

<span id="class_XRInterface_constant_XR_AR"></span>

[Capabilities](class_xrinterface.md#enum_XRInterface_Capabilities) **XR_AR** = `16`

This interface supports AR (video background and real world tracking).

<span id="class_XRInterface_constant_XR_EXTERNAL"></span>

[Capabilities](class_xrinterface.md#enum_XRInterface_Capabilities) **XR_EXTERNAL** = `32`

This interface outputs to an external device. If the main viewport is used, the on screen output is an unmodified buffer of either the left or right eye (stretched if the viewport size is not changed to the same aspect ratio of [get_render_target_size()](class_xrinterface.md#class_XRInterface_method_get_render_target_size)). Using a separate viewport node frees up the main viewport for other purposes.

---

<span id="enum_XRInterface_TrackingStatus"></span>

enum **TrackingStatus**: [🔗](class_xrinterface.md#enum_XRInterface_TrackingStatus)

<span id="class_XRInterface_constant_XR_NORMAL_TRACKING"></span>

[TrackingStatus](class_xrinterface.md#enum_XRInterface_TrackingStatus) **XR_NORMAL_TRACKING** = `0`

Tracking is behaving as expected.

<span id="class_XRInterface_constant_XR_EXCESSIVE_MOTION"></span>

[TrackingStatus](class_xrinterface.md#enum_XRInterface_TrackingStatus) **XR_EXCESSIVE_MOTION** = `1`

Tracking is hindered by excessive motion (the player is moving faster than tracking can keep up).

<span id="class_XRInterface_constant_XR_INSUFFICIENT_FEATURES"></span>

[TrackingStatus](class_xrinterface.md#enum_XRInterface_TrackingStatus) **XR_INSUFFICIENT_FEATURES** = `2`

Tracking is hindered by insufficient features, it's too dark (for camera-based tracking), player is blocked, etc.

<span id="class_XRInterface_constant_XR_UNKNOWN_TRACKING"></span>

[TrackingStatus](class_xrinterface.md#enum_XRInterface_TrackingStatus) **XR_UNKNOWN_TRACKING** = `3`

We don't know the status of the tracking or this interface does not provide feedback.

<span id="class_XRInterface_constant_XR_NOT_TRACKING"></span>

[TrackingStatus](class_xrinterface.md#enum_XRInterface_TrackingStatus) **XR_NOT_TRACKING** = `4`

Tracking is not functional (camera not plugged in or obscured, lighthouses turned off, etc.).

---

<span id="enum_XRInterface_PlayAreaMode"></span>

enum **PlayAreaMode**: [🔗](class_xrinterface.md#enum_XRInterface_PlayAreaMode)

<span id="class_XRInterface_constant_XR_PLAY_AREA_UNKNOWN"></span>

[PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) **XR_PLAY_AREA_UNKNOWN** = `0`

Play area mode not set or not available.

<span id="class_XRInterface_constant_XR_PLAY_AREA_3DOF"></span>

[PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) **XR_PLAY_AREA_3DOF** = `1`

Play area only supports orientation tracking, no positional tracking, area will center around player.

<span id="class_XRInterface_constant_XR_PLAY_AREA_SITTING"></span>

[PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) **XR_PLAY_AREA_SITTING** = `2`

Player is in seated position, limited positional tracking, fixed guardian around player.

<span id="class_XRInterface_constant_XR_PLAY_AREA_ROOMSCALE"></span>

[PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) **XR_PLAY_AREA_ROOMSCALE** = `3`

Player is free to move around, full positional tracking.

<span id="class_XRInterface_constant_XR_PLAY_AREA_STAGE"></span>

[PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) **XR_PLAY_AREA_STAGE** = `4`

Same as [XR_PLAY_AREA_ROOMSCALE](class_xrinterface.md#class_XRInterface_constant_XR_PLAY_AREA_ROOMSCALE) but origin point is fixed to the center of the physical space. In this mode, system-level recentering may be disabled, requiring the use of [XRServer.center_on_hmd()](class_xrserver.md#class_XRServer_method_center_on_hmd).

<span id="class_XRInterface_constant_XR_PLAY_AREA_CUSTOM"></span>

[PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) **XR_PLAY_AREA_CUSTOM** = `2147483647`

Custom play area set by a GDExtension.

---

<span id="enum_XRInterface_EnvironmentBlendMode"></span>

enum **EnvironmentBlendMode**: [🔗](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode)

<span id="class_XRInterface_constant_XR_ENV_BLEND_MODE_OPAQUE"></span>

[EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode) **XR_ENV_BLEND_MODE_OPAQUE** = `0`

Opaque blend mode. This is typically used for VR devices.

<span id="class_XRInterface_constant_XR_ENV_BLEND_MODE_ADDITIVE"></span>

[EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode) **XR_ENV_BLEND_MODE_ADDITIVE** = `1`

Additive blend mode. This is typically used for AR devices or VR devices with passthrough.

<span id="class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND"></span>

[EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode) **XR_ENV_BLEND_MODE_ALPHA_BLEND** = `2`

Alpha blend mode. This is typically used for AR or VR devices with passthrough capabilities. The alpha channel controls how much of the passthrough is visible. Alpha of 0.0 means the passthrough is visible and this pixel works in ADDITIVE mode. Alpha of 1.0 means that the passthrough is not visible and this pixel works in OPAQUE mode.

---

<span id="enum_XRInterface_VRSTextureFormat"></span>

enum **VRSTextureFormat**: [🔗](class_xrinterface.md#enum_XRInterface_VRSTextureFormat)

<span id="class_XRInterface_constant_XR_VRS_TEXTURE_FORMAT_UNIFIED"></span>

[VRSTextureFormat](class_xrinterface.md#enum_XRInterface_VRSTextureFormat) **XR_VRS_TEXTURE_FORMAT_UNIFIED** = `0`

The texture format is the same as returned by [XRVRS.make_vrs_texture()](class_xrvrs.md#class_XRVRS_method_make_vrs_texture).

<span id="class_XRInterface_constant_XR_VRS_TEXTURE_FORMAT_FRAGMENT_SHADING_RATE"></span>

[VRSTextureFormat](class_xrinterface.md#enum_XRInterface_VRSTextureFormat) **XR_VRS_TEXTURE_FORMAT_FRAGMENT_SHADING_RATE** = `1`

The texture format is the same as expected by the Vulkan `VK_KHR_fragment_shading_rate` extension.

<span id="class_XRInterface_constant_XR_VRS_TEXTURE_FORMAT_FRAGMENT_DENSITY_MAP"></span>

[VRSTextureFormat](class_xrinterface.md#enum_XRInterface_VRSTextureFormat) **XR_VRS_TEXTURE_FORMAT_FRAGMENT_DENSITY_MAP** = `2`

The texture format is the same as expected by the Vulkan `VK_EXT_fragment_density_map` extension.

---

### Property Descriptions

<span id="class_XRInterface_property_ar_is_anchor_detection_enabled"></span>

[bool](class_bool.md#class_bool) **ar_is_anchor_detection_enabled** = `false` [🔗](class_xrinterface.md#class_XRInterface_property_ar_is_anchor_detection_enabled)

- void **set_anchor_detection_is_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_anchor_detection_is_enabled** ( )

On an AR interface, `true` if anchor detection is enabled.

---

<span id="class_XRInterface_property_environment_blend_mode"></span>

[EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode) **environment_blend_mode** = `0` [🔗](class_xrinterface.md#class_XRInterface_property_environment_blend_mode)

- [bool](class_bool.md#class_bool) **set_environment_blend_mode** ( mode: [EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode) )
- [EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode) **get_environment_blend_mode** ( )

Specify how XR should blend in the environment. This is specific to certain AR and passthrough devices where camera images are blended in by the XR compositor.

---

<span id="class_XRInterface_property_interface_is_primary"></span>

[bool](class_bool.md#class_bool) **interface_is_primary** = `false` [🔗](class_xrinterface.md#class_XRInterface_property_interface_is_primary)

- void **set_primary** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_primary** ( )

`true` if this is the primary interface.

---

<span id="class_XRInterface_property_xr_play_area_mode"></span>

[PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) **xr_play_area_mode** = `0` [🔗](class_xrinterface.md#class_XRInterface_property_xr_play_area_mode)

- [bool](class_bool.md#class_bool) **set_play_area_mode** ( mode: [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) )
- [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) **get_play_area_mode** ( )

The play area mode for this interface.

---

### Method Descriptions

<span id="class_XRInterface_method_get_camera_feed_id"></span>

[int](class_int.md#class_int) **get_camera_feed_id** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_get_camera_feed_id)

If this is an AR interface that requires displaying a camera feed as the background, this method returns the feed ID in the [CameraServer](class_cameraserver.md#class_CameraServer) for this interface.

---

<span id="class_XRInterface_method_get_capabilities"></span>

[int](class_int.md#class_int) **get_capabilities** ( ) *const* [🔗](class_xrinterface.md#class_XRInterface_method_get_capabilities)

Returns a combination of [Capabilities](class_xrinterface.md#enum_XRInterface_Capabilities) flags providing information about the capabilities of this interface.

---

<span id="class_XRInterface_method_get_name"></span>

[StringName](class_stringname.md#class_StringName) **get_name** ( ) *const* [🔗](class_xrinterface.md#class_XRInterface_method_get_name)

Returns the name of this interface (`"OpenXR"`, `"OpenVR"`, `"OpenHMD"`, `"ARKit"`, etc.).

---

<span id="class_XRInterface_method_get_play_area"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_play_area** ( ) *const* [🔗](class_xrinterface.md#class_XRInterface_method_get_play_area)

Returns an array of vectors that represent the physical play area mapped to the virtual space around the [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D) point. The points form a convex polygon that can be used to react to or visualize the play area. This returns an empty array if this feature is not supported or if the information is not yet available.

---

<span id="class_XRInterface_method_get_projection_for_view"></span>

[Projection](class_projection.md#class_Projection) **get_projection_for_view** ( view: [int](class_int.md#class_int), aspect: [float](class_float.md#class_float), near: [float](class_float.md#class_float), far: [float](class_float.md#class_float) ) [🔗](class_xrinterface.md#class_XRInterface_method_get_projection_for_view)

Returns the projection matrix for a view/eye.

---

<span id="class_XRInterface_method_get_render_target_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_render_target_size** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_get_render_target_size)

Returns the resolution at which we should render our intermediate results before things like lens distortion are applied by the VR platform.

---

<span id="class_XRInterface_method_get_supported_environment_blend_modes"></span>

[Array](class_array.md#class_Array) **get_supported_environment_blend_modes** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_get_supported_environment_blend_modes)

Returns the an array of supported environment blend modes, see [EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode).

---

<span id="class_XRInterface_method_get_system_info"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_system_info** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_get_system_info)

Returns a [Dictionary](class_dictionary.md#class_Dictionary) with extra system info. Interfaces are expected to return `XRRuntimeName` and `XRRuntimeVersion` providing info about the used XR runtime. Additional entries may be provided specific to an interface.

 **Note:** This information may only be available after [initialize()](class_xrinterface.md#class_XRInterface_method_initialize) was successfully called.

---

<span id="class_XRInterface_method_get_tracking_status"></span>

[TrackingStatus](class_xrinterface.md#enum_XRInterface_TrackingStatus) **get_tracking_status** ( ) *const* [🔗](class_xrinterface.md#class_XRInterface_method_get_tracking_status)

If supported, returns the status of our tracking. This will allow you to provide feedback to the user whether there are issues with positional tracking.

---

<span id="class_XRInterface_method_get_transform_for_view"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_transform_for_view** ( view: [int](class_int.md#class_int), cam_transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_xrinterface.md#class_XRInterface_method_get_transform_for_view)

Returns the transform for a view/eye.

 `view` is the view/eye index.

 `cam_transform` is the transform that maps device coordinates to scene coordinates, typically the [Node3D.global_transform](class_node3d.md#class_Node3D_property_global_transform) of the current XROrigin3D.

---

<span id="class_XRInterface_method_get_view_count"></span>

[int](class_int.md#class_int) **get_view_count** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_get_view_count)

Returns the number of views that need to be rendered for this device. 1 for Monoscopic, 2 for Stereoscopic.

---

<span id="class_XRInterface_method_initialize"></span>

[bool](class_bool.md#class_bool) **initialize** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_initialize)

Call this to initialize this interface. The first interface that is initialized is identified as the primary interface and it will be used for rendering output.

After initializing the interface you want to use you then need to enable the AR/VR mode of a viewport and rendering should commence.

 **Note:** You must enable the XR mode on the main viewport for any device that uses the main output of Godot, such as for mobile VR.

If you do this for a platform that handles its own output (such as OpenVR) Godot will show just one eye without distortion on screen. Alternatively, you can add a separate viewport node to your scene and enable AR/VR on that viewport. It will be used to output to the HMD, leaving you free to do anything you like in the main window, such as using a separate camera as a spectator camera or rendering something completely different.

While currently not used, you can activate additional interfaces. You may wish to do this if you want to track controllers from other platforms. However, at this point in time only one interface can render to an HMD.

---

<span id="class_XRInterface_method_is_initialized"></span>

[bool](class_bool.md#class_bool) **is_initialized** ( ) *const* [🔗](class_xrinterface.md#class_XRInterface_method_is_initialized)

Returns `true` if this interface has been initialized.

---

<span id="class_XRInterface_method_is_passthrough_enabled"></span>

[bool](class_bool.md#class_bool) **is_passthrough_enabled** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_is_passthrough_enabled)

**Deprecated:** Check if [environment_blend_mode](class_xrinterface.md#class_XRInterface_property_environment_blend_mode) is [XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND), instead.

Returns `true` if passthrough is enabled.

---

<span id="class_XRInterface_method_is_passthrough_supported"></span>

[bool](class_bool.md#class_bool) **is_passthrough_supported** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_is_passthrough_supported)

**Deprecated:** Check that [XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND) is supported using [get_supported_environment_blend_modes()](class_xrinterface.md#class_XRInterface_method_get_supported_environment_blend_modes), instead.

Returns `true` if this interface supports passthrough.

---

<span id="class_XRInterface_method_set_environment_blend_mode"></span>

[bool](class_bool.md#class_bool) **set_environment_blend_mode** ( mode: [EnvironmentBlendMode](class_xrinterface.md#enum_XRInterface_EnvironmentBlendMode) ) [🔗](class_xrinterface.md#class_XRInterface_method_set_environment_blend_mode)

Sets the active environment blend mode.

 `mode` is the environment blend mode starting with the next frame.

 **Note:** Not all runtimes support all environment blend modes, so it is important to check this at startup. For example:

::

    func _ready():
        var xr_interface = XRServer.find_interface("OpenXR")
        if xr_interface and xr_interface.is_initialized():
            var vp = get_viewport()
            vp.use_xr = true
            var acceptable_modes = [XRInterface.XR_ENV_BLEND_MODE_OPAQUE, XRInterface.XR_ENV_BLEND_MODE_ADDITIVE]
            var modes = xr_interface.get_supported_environment_blend_modes()
            for mode in acceptable_modes:
                if mode in modes:
                    xr_interface.set_environment_blend_mode(mode)
                    break

---

<span id="class_XRInterface_method_set_play_area_mode"></span>

[bool](class_bool.md#class_bool) **set_play_area_mode** ( mode: [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) ) [🔗](class_xrinterface.md#class_XRInterface_method_set_play_area_mode)

Sets the active play area mode, will return `false` if the mode can't be used with this interface.

 **Note:** Changing this after the interface has already been initialized can be jarring for the player, so it's recommended to recenter on the HMD with [XRServer.center_on_hmd()](class_xrserver.md#class_XRServer_method_center_on_hmd) (if switching to [XR_PLAY_AREA_STAGE](class_xrinterface.md#class_XRInterface_constant_XR_PLAY_AREA_STAGE)) or make the switch during a scene change.

---

<span id="class_XRInterface_method_start_passthrough"></span>

[bool](class_bool.md#class_bool) **start_passthrough** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_start_passthrough)

**Deprecated:** Set the [environment_blend_mode](class_xrinterface.md#class_XRInterface_property_environment_blend_mode) to [XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND), instead.

Starts passthrough, will return `false` if passthrough couldn't be started.

 **Note:** The viewport used for XR must have a transparent background, otherwise passthrough may not properly render.

---

<span id="class_XRInterface_method_stop_passthrough"></span>

void **stop_passthrough** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_stop_passthrough)

**Deprecated:** Set the [environment_blend_mode](class_xrinterface.md#class_XRInterface_property_environment_blend_mode) to [XR_ENV_BLEND_MODE_OPAQUE](class_xrinterface.md#class_XRInterface_constant_XR_ENV_BLEND_MODE_OPAQUE), instead.

Stops passthrough.

---

<span id="class_XRInterface_method_supports_play_area_mode"></span>

[bool](class_bool.md#class_bool) **supports_play_area_mode** ( mode: [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) ) [🔗](class_xrinterface.md#class_XRInterface_method_supports_play_area_mode)

Call this to find out if a given play area mode is supported by this interface.

---

<span id="class_XRInterface_method_trigger_haptic_pulse"></span>

void **trigger_haptic_pulse** ( action_name: [String](class_string.md#class_String), tracker_name: [StringName](class_stringname.md#class_StringName), frequency: [float](class_float.md#class_float), amplitude: [float](class_float.md#class_float), duration_sec: [float](class_float.md#class_float), delay_sec: [float](class_float.md#class_float) ) [🔗](class_xrinterface.md#class_XRInterface_method_trigger_haptic_pulse)

Triggers a haptic pulse on a device associated with this interface.

 `action_name` is the name of the action for this pulse.

 `tracker_name` is optional and can be used to direct the pulse to a specific device provided that device is bound to this haptic.

 `frequency` is the frequency of the pulse, set to `0.0` to have the system use a default frequency.

 `amplitude` is the amplitude of the pulse between `0.0` and `1.0`.

 `duration_sec` is the duration of the pulse in seconds.

 `delay_sec` is a delay in seconds before the pulse is given.

---

<span id="class_XRInterface_method_uninitialize"></span>

void **uninitialize** ( ) [🔗](class_xrinterface.md#class_XRInterface_method_uninitialize)

Turns the interface off.
