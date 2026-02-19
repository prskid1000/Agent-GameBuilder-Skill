<span id="class_WebXRInterface"></span>

## WebXRInterface

**Inherits:** [XRInterface](class_xrinterface.md#class_XRInterface) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

XR interface using WebXR.

### Description

WebXR is an open standard that allows creating VR and AR applications that run in the web browser.

As such, this interface is only available when running in Web exports.

WebXR supports a wide range of devices, from the very capable (like Valve Index, HTC Vive, Oculus Rift and Quest) down to the much less capable (like Google Cardboard, Oculus Go, GearVR, or plain smartphones).

Since WebXR is based on JavaScript, it makes extensive use of callbacks, which means that **WebXRInterface** is forced to use signals, where other XR interfaces would instead use functions that return a result immediately. This makes **WebXRInterface** quite a bit more complicated to initialize than other XR interfaces.

Here's the minimum code required to start an immersive VR session:

::

    extends Node3D

    var webxr_interface
    var vr_supported = false

    func _ready():
        # We assume this node has a button as a child.
        # This button is for the user to consent to entering immersive VR mode.
        $Button.pressed.connect(self._on_button_pressed)

        webxr_interface = XRServer.find_interface("WebXR")
        if webxr_interface:
            # WebXR uses a lot of asynchronous callbacks, so we connect to various
            # signals in order to receive them.
            webxr_interface.session_supported.connect(self._webxr_session_supported)
            webxr_interface.session_started.connect(self._webxr_session_started)
            webxr_interface.session_ended.connect(self._webxr_session_ended)
            webxr_interface.session_failed.connect(self._webxr_session_failed)

            # This returns immediately - our _webxr_session_supported() method
            # (which we connected to the "session_supported" signal above) will
            # be called sometime later to let us know if it's supported or not.
            webxr_interface.is_session_supported("immersive-vr")

    func _webxr_session_supported(session_mode, supported):
        if session_mode == 'immersive-vr':
            vr_supported = supported

    func _on_button_pressed():
        if not vr_supported:
            OS.alert("Your browser doesn't support VR")
            return

        # We want an immersive VR session, as opposed to AR ('immersive-ar') or a
        # simple 3DoF viewer ('viewer').
        webxr_interface.session_mode = 'immersive-vr'
        # 'bounded-floor' is room scale, 'local-floor' is a standing or sitting
        # experience (it puts you 1.6m above the ground if you have 3DoF headset),
        # whereas as 'local' puts you down at the XROrigin.
        # This list means it'll first try to request 'bounded-floor', then
        # fallback on 'local-floor' and ultimately 'local', if nothing else is
        # supported.
        webxr_interface.requested_reference_space_types = 'bounded-floor, local-floor, local'
        # In order to use 'local-floor' or 'bounded-floor' we must also
        # mark the features as required or optional. By including 'hand-tracking'
        # as an optional feature, it will be enabled if supported.
        webxr_interface.required_features = 'local-floor'
        webxr_interface.optional_features = 'bounded-floor, hand-tracking'

        # This will return false if we're unable to even request the session,
        # however, it can still fail asynchronously later in the process, so we
        # only know if it's really succeeded or failed when our
        # _webxr_session_started() or _webxr_session_failed() methods are called.
        if not webxr_interface.initialize():
            OS.alert("Failed to initialize")
            return

    func _webxr_session_started():
        $Button.visible = false
        # This tells Godot to start rendering to the headset.
        get_viewport().use_xr = true
        # This will be the reference space type you ultimately got, out of the
        # types that you requested above. This is useful if you want the game to
        # work a little differently in 'bounded-floor' versus 'local-floor'.
        print("Reference space type: ", webxr_interface.reference_space_type)
        # This will be the list of features that were successfully enabled
        # (except on browsers that don't support this property).
        print("Enabled features: ", webxr_interface.enabled_features)

    func _webxr_session_ended():
        $Button.visible = true
        # If the user exits immersive mode, then we tell Godot to render to the web
        # page again.
        get_viewport().use_xr = false

    func _webxr_session_failed(message):
        OS.alert("Failed to initialize: " + message)

There are a couple ways to handle "controller" input:

- Using [XRController3D](class_xrcontroller3d.md#class_XRController3D) nodes and their [XRController3D.button_pressed](class_xrcontroller3d.md#class_XRController3D_signal_button_pressed) and [XRController3D.button_released](class_xrcontroller3d.md#class_XRController3D_signal_button_released) signals. This is how controllers are typically handled in XR apps in Godot, however, this will only work with advanced VR controllers like the Oculus Touch or Index controllers, for example.

- Using the [select](class_webxrinterface.md#class_WebXRInterface_signal_select), [squeeze](class_webxrinterface.md#class_WebXRInterface_signal_squeeze) and related signals. This method will work for both advanced VR controllers, and non-traditional input sources like a tap on the screen, a spoken voice command or a button press on the device itself.

You can use both methods to allow your game or app to support a wider or narrower set of devices and input methods, or to allow more advanced interactions with more advanced devices.

### Tutorials

- How to make a VR game for WebXR with Godot 4

### Properties


| [String](class_string.md#class_String) | [enabled_features](class_webxrinterface.md#class_WebXRInterface_property_enabled_features) |
| --- | --- |
| [String](class_string.md#class_String) | [optional_features](class_webxrinterface.md#class_WebXRInterface_property_optional_features) |
| [String](class_string.md#class_String) | [reference_space_type](class_webxrinterface.md#class_WebXRInterface_property_reference_space_type) |
| [String](class_string.md#class_String) | [requested_reference_space_types](class_webxrinterface.md#class_WebXRInterface_property_requested_reference_space_types) |
| [String](class_string.md#class_String) | [required_features](class_webxrinterface.md#class_WebXRInterface_property_required_features) |
| [String](class_string.md#class_String) | [session_mode](class_webxrinterface.md#class_WebXRInterface_property_session_mode) |
| [String](class_string.md#class_String) | [visibility_state](class_webxrinterface.md#class_WebXRInterface_property_visibility_state) |

### Methods


| [Array](class_array.md#class_Array) | [get_available_display_refresh_rates](class_webxrinterface.md#class_WebXRInterface_method_get_available_display_refresh_rates) ( ) const |
| --- | --- |
| [float](class_float.md#class_float) | [get_display_refresh_rate](class_webxrinterface.md#class_WebXRInterface_method_get_display_refresh_rate) ( ) const |
| [TargetRayMode](class_webxrinterface.md#enum_WebXRInterface_TargetRayMode) | [get_input_source_target_ray_mode](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_target_ray_mode) ( input_source_id: [int](class_int.md#class_int) ) const |
| [XRControllerTracker](class_xrcontrollertracker.md#class_XRControllerTracker) | [get_input_source_tracker](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_tracker) ( input_source_id: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_input_source_active](class_webxrinterface.md#class_WebXRInterface_method_is_input_source_active) ( input_source_id: [int](class_int.md#class_int) ) const |
| void | [is_session_supported](class_webxrinterface.md#class_WebXRInterface_method_is_session_supported) ( session_mode: [String](class_string.md#class_String) ) |
| void | [set_display_refresh_rate](class_webxrinterface.md#class_WebXRInterface_method_set_display_refresh_rate) ( refresh_rate: [float](class_float.md#class_float) ) |

---

### Signals

<span id="class_WebXRInterface_signal_display_refresh_rate_changed"></span>

**display_refresh_rate_changed** ( ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_display_refresh_rate_changed)

Emitted after the display's refresh rate has changed.

---

<span id="class_WebXRInterface_signal_reference_space_reset"></span>

**reference_space_reset** ( ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_reference_space_reset)

Emitted to indicate that the reference space has been reset or reconfigured.

When (or whether) this is emitted depends on the user's browser or device, but may include when the user has changed the dimensions of their play space (which you may be able to access via [XRInterface.get_play_area()](class_xrinterface.md#class_XRInterface_method_get_play_area)) or pressed/held a button to recenter their position.

See WebXR's XRReferenceSpace reset event for more information.

---

<span id="class_WebXRInterface_signal_select"></span>

**select** ( input_source_id: [int](class_int.md#class_int) ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_select)

Emitted after one of the input sources has finished its "primary action".

Use [get_input_source_tracker()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_tracker) and [get_input_source_target_ray_mode()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_target_ray_mode) to get more information about the input source.

---

<span id="class_WebXRInterface_signal_selectend"></span>

**selectend** ( input_source_id: [int](class_int.md#class_int) ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_selectend)

Emitted when one of the input sources has finished its "primary action".

Use [get_input_source_tracker()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_tracker) and [get_input_source_target_ray_mode()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_target_ray_mode) to get more information about the input source.

---

<span id="class_WebXRInterface_signal_selectstart"></span>

**selectstart** ( input_source_id: [int](class_int.md#class_int) ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_selectstart)

Emitted when one of the input source has started its "primary action".

Use [get_input_source_tracker()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_tracker) and [get_input_source_target_ray_mode()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_target_ray_mode) to get more information about the input source.

---

<span id="class_WebXRInterface_signal_session_ended"></span>

**session_ended** ( ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_session_ended)

Emitted when the user ends the WebXR session (which can be done using UI from the browser or device).

At this point, you should do `get_viewport().use_xr = false` to instruct Godot to resume rendering to the screen.

---

<span id="class_WebXRInterface_signal_session_failed"></span>

**session_failed** ( message: [String](class_string.md#class_String) ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_session_failed)

Emitted by [XRInterface.initialize()](class_xrinterface.md#class_XRInterface_method_initialize) if the session fails to start.

 `message` may optionally contain an error message from WebXR, or an empty string if no message is available.

---

<span id="class_WebXRInterface_signal_session_started"></span>

**session_started** ( ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_session_started)

Emitted by [XRInterface.initialize()](class_xrinterface.md#class_XRInterface_method_initialize) if the session is successfully started.

At this point, it's safe to do `get_viewport().use_xr = true` to instruct Godot to start rendering to the XR device.

---

<span id="class_WebXRInterface_signal_session_supported"></span>

**session_supported** ( session_mode: [String](class_string.md#class_String), supported: [bool](class_bool.md#class_bool) ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_session_supported)

Emitted by [is_session_supported()](class_webxrinterface.md#class_WebXRInterface_method_is_session_supported) to indicate if the given `session_mode` is supported or not.

---

<span id="class_WebXRInterface_signal_squeeze"></span>

**squeeze** ( input_source_id: [int](class_int.md#class_int) ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_squeeze)

Emitted after one of the input sources has finished its "primary squeeze action".

Use [get_input_source_tracker()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_tracker) and [get_input_source_target_ray_mode()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_target_ray_mode) to get more information about the input source.

---

<span id="class_WebXRInterface_signal_squeezeend"></span>

**squeezeend** ( input_source_id: [int](class_int.md#class_int) ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_squeezeend)

Emitted when one of the input sources has finished its "primary squeeze action".

Use [get_input_source_tracker()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_tracker) and [get_input_source_target_ray_mode()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_target_ray_mode) to get more information about the input source.

---

<span id="class_WebXRInterface_signal_squeezestart"></span>

**squeezestart** ( input_source_id: [int](class_int.md#class_int) ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_squeezestart)

Emitted when one of the input sources has started its "primary squeeze action".

Use [get_input_source_tracker()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_tracker) and [get_input_source_target_ray_mode()](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_target_ray_mode) to get more information about the input source.

---

<span id="class_WebXRInterface_signal_visibility_state_changed"></span>

**visibility_state_changed** ( ) [🔗](class_webxrinterface.md#class_WebXRInterface_signal_visibility_state_changed)

Emitted when [visibility_state](class_webxrinterface.md#class_WebXRInterface_property_visibility_state) has changed.

---

### Enumerations

<span id="enum_WebXRInterface_TargetRayMode"></span>

enum **TargetRayMode**: [🔗](class_webxrinterface.md#enum_WebXRInterface_TargetRayMode)

<span id="class_WebXRInterface_constant_TARGET_RAY_MODE_UNKNOWN"></span>

[TargetRayMode](class_webxrinterface.md#enum_WebXRInterface_TargetRayMode) **TARGET_RAY_MODE_UNKNOWN** = `0`

We don't know the target ray mode.

<span id="class_WebXRInterface_constant_TARGET_RAY_MODE_GAZE"></span>

[TargetRayMode](class_webxrinterface.md#enum_WebXRInterface_TargetRayMode) **TARGET_RAY_MODE_GAZE** = `1`

Target ray originates at the viewer's eyes and points in the direction they are looking.

<span id="class_WebXRInterface_constant_TARGET_RAY_MODE_TRACKED_POINTER"></span>

[TargetRayMode](class_webxrinterface.md#enum_WebXRInterface_TargetRayMode) **TARGET_RAY_MODE_TRACKED_POINTER** = `2`

Target ray from a handheld pointer, most likely a VR touch controller.

<span id="class_WebXRInterface_constant_TARGET_RAY_MODE_SCREEN"></span>

[TargetRayMode](class_webxrinterface.md#enum_WebXRInterface_TargetRayMode) **TARGET_RAY_MODE_SCREEN** = `3`

Target ray from touch screen, mouse or other tactile input device.

---

### Property Descriptions

<span id="class_WebXRInterface_property_enabled_features"></span>

[String](class_string.md#class_String) **enabled_features** [🔗](class_webxrinterface.md#class_WebXRInterface_property_enabled_features)

- [String](class_string.md#class_String) **get_enabled_features** ( )

A comma-separated list of features that were successfully enabled by [XRInterface.initialize()](class_xrinterface.md#class_XRInterface_method_initialize) when setting up the WebXR session.

This may include features requested by setting [required_features](class_webxrinterface.md#class_WebXRInterface_property_required_features) and [optional_features](class_webxrinterface.md#class_WebXRInterface_property_optional_features), and will only be available after [session_started](class_webxrinterface.md#class_WebXRInterface_signal_session_started) has been emitted.

 **Note:** This may not be support by all web browsers, in which case it will be an empty string.

---

<span id="class_WebXRInterface_property_optional_features"></span>

[String](class_string.md#class_String) **optional_features** [🔗](class_webxrinterface.md#class_WebXRInterface_property_optional_features)

- void **set_optional_features** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_optional_features** ( )

A comma-seperated list of optional features used by [XRInterface.initialize()](class_xrinterface.md#class_XRInterface_method_initialize) when setting up the WebXR session.

If a user's browser or device doesn't support one of the given features, initialization will continue, but you won't be able to use the requested feature.

This doesn't have any effect on the interface when already initialized.

See the MDN documentation on WebXR's session features for a list of possible values.

---

<span id="class_WebXRInterface_property_reference_space_type"></span>

[String](class_string.md#class_String) **reference_space_type** [🔗](class_webxrinterface.md#class_WebXRInterface_property_reference_space_type)

- [String](class_string.md#class_String) **get_reference_space_type** ( )

The reference space type (from the list of requested types set in the [requested_reference_space_types](class_webxrinterface.md#class_WebXRInterface_property_requested_reference_space_types) property), that was ultimately used by [XRInterface.initialize()](class_xrinterface.md#class_XRInterface_method_initialize) when setting up the WebXR session.

Possible values come from WebXR's XRReferenceSpaceType. If you want to use a particular reference space type, it must be listed in either [required_features](class_webxrinterface.md#class_WebXRInterface_property_required_features) or [optional_features](class_webxrinterface.md#class_WebXRInterface_property_optional_features).

---

<span id="class_WebXRInterface_property_requested_reference_space_types"></span>

[String](class_string.md#class_String) **requested_reference_space_types** [🔗](class_webxrinterface.md#class_WebXRInterface_property_requested_reference_space_types)

- void **set_requested_reference_space_types** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_requested_reference_space_types** ( )

A comma-seperated list of reference space types used by [XRInterface.initialize()](class_xrinterface.md#class_XRInterface_method_initialize) when setting up the WebXR session.

The reference space types are requested in order, and the first one supported by the user's device or browser will be used. The [reference_space_type](class_webxrinterface.md#class_WebXRInterface_property_reference_space_type) property contains the reference space type that was ultimately selected.

This doesn't have any effect on the interface when already initialized.

Possible values come from WebXR's XRReferenceSpaceType. If you want to use a particular reference space type, it must be listed in either [required_features](class_webxrinterface.md#class_WebXRInterface_property_required_features) or [optional_features](class_webxrinterface.md#class_WebXRInterface_property_optional_features).

---

<span id="class_WebXRInterface_property_required_features"></span>

[String](class_string.md#class_String) **required_features** [🔗](class_webxrinterface.md#class_WebXRInterface_property_required_features)

- void **set_required_features** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_required_features** ( )

A comma-seperated list of required features used by [XRInterface.initialize()](class_xrinterface.md#class_XRInterface_method_initialize) when setting up the WebXR session.

If a user's browser or device doesn't support one of the given features, initialization will fail and [session_failed](class_webxrinterface.md#class_WebXRInterface_signal_session_failed) will be emitted.

This doesn't have any effect on the interface when already initialized.

See the MDN documentation on WebXR's session features for a list of possible values.

---

<span id="class_WebXRInterface_property_session_mode"></span>

[String](class_string.md#class_String) **session_mode** [🔗](class_webxrinterface.md#class_WebXRInterface_property_session_mode)

- void **set_session_mode** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_session_mode** ( )

The session mode used by [XRInterface.initialize()](class_xrinterface.md#class_XRInterface_method_initialize) when setting up the WebXR session.

This doesn't have any effect on the interface when already initialized.

Possible values come from WebXR's XRSessionMode, including: `"immersive-vr"`, `"immersive-ar"`, and `"inline"`.

---

<span id="class_WebXRInterface_property_visibility_state"></span>

[String](class_string.md#class_String) **visibility_state** [🔗](class_webxrinterface.md#class_WebXRInterface_property_visibility_state)

- [String](class_string.md#class_String) **get_visibility_state** ( )

Indicates if the WebXR session's imagery is visible to the user.

Possible values come from WebXR's XRVisibilityState, including `"hidden"`, `"visible"`, and `"visible-blurred"`.

---

### Method Descriptions

<span id="class_WebXRInterface_method_get_available_display_refresh_rates"></span>

[Array](class_array.md#class_Array) **get_available_display_refresh_rates** ( ) *const* [🔗](class_webxrinterface.md#class_WebXRInterface_method_get_available_display_refresh_rates)

Returns display refresh rates supported by the current HMD. Only returned if this feature is supported by the web browser and after the interface has been initialized.

---

<span id="class_WebXRInterface_method_get_display_refresh_rate"></span>

[float](class_float.md#class_float) **get_display_refresh_rate** ( ) *const* [🔗](class_webxrinterface.md#class_WebXRInterface_method_get_display_refresh_rate)

Returns the display refresh rate for the current HMD. Not supported on all HMDs and browsers. It may not report an accurate value until after using [set_display_refresh_rate()](class_webxrinterface.md#class_WebXRInterface_method_set_display_refresh_rate).

---

<span id="class_WebXRInterface_method_get_input_source_target_ray_mode"></span>

[TargetRayMode](class_webxrinterface.md#enum_WebXRInterface_TargetRayMode) **get_input_source_target_ray_mode** ( input_source_id: [int](class_int.md#class_int) ) *const* [🔗](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_target_ray_mode)

Returns the target ray mode for the given `input_source_id`.

This can help interpret the input coming from that input source. See XRInputSource.targetRayMode for more information.

---

<span id="class_WebXRInterface_method_get_input_source_tracker"></span>

[XRControllerTracker](class_xrcontrollertracker.md#class_XRControllerTracker) **get_input_source_tracker** ( input_source_id: [int](class_int.md#class_int) ) *const* [🔗](class_webxrinterface.md#class_WebXRInterface_method_get_input_source_tracker)

Gets an [XRControllerTracker](class_xrcontrollertracker.md#class_XRControllerTracker) for the given `input_source_id`.

In the context of WebXR, an input source can be an advanced VR controller like the Oculus Touch or Index controllers, or even a tap on the screen, a spoken voice command or a button press on the device itself. When a non-traditional input source is used, interpret the position and orientation of the [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) as a ray pointing at the object the user wishes to interact with.

Use this method to get information about the input source that triggered one of these signals:

- [selectstart](class_webxrinterface.md#class_WebXRInterface_signal_selectstart)

- [select](class_webxrinterface.md#class_WebXRInterface_signal_select)

- [selectend](class_webxrinterface.md#class_WebXRInterface_signal_selectend)

- [squeezestart](class_webxrinterface.md#class_WebXRInterface_signal_squeezestart)

- [squeeze](class_webxrinterface.md#class_WebXRInterface_signal_squeeze)

- [squeezestart](class_webxrinterface.md#class_WebXRInterface_signal_squeezestart)

---

<span id="class_WebXRInterface_method_is_input_source_active"></span>

[bool](class_bool.md#class_bool) **is_input_source_active** ( input_source_id: [int](class_int.md#class_int) ) *const* [🔗](class_webxrinterface.md#class_WebXRInterface_method_is_input_source_active)

Returns `true` if there is an active input source with the given `input_source_id`.

---

<span id="class_WebXRInterface_method_is_session_supported"></span>

void **is_session_supported** ( session_mode: [String](class_string.md#class_String) ) [🔗](class_webxrinterface.md#class_WebXRInterface_method_is_session_supported)

Checks if the given `session_mode` is supported by the user's browser.

Possible values come from WebXR's XRSessionMode, including: `"immersive-vr"`, `"immersive-ar"`, and `"inline"`.

This method returns nothing, instead it emits the [session_supported](class_webxrinterface.md#class_WebXRInterface_signal_session_supported) signal with the result.

---

<span id="class_WebXRInterface_method_set_display_refresh_rate"></span>

void **set_display_refresh_rate** ( refresh_rate: [float](class_float.md#class_float) ) [🔗](class_webxrinterface.md#class_WebXRInterface_method_set_display_refresh_rate)

Sets the display refresh rate for the current HMD. Not supported on all HMDs and browsers. It won't take effect right away until after [display_refresh_rate_changed](class_webxrinterface.md#class_WebXRInterface_signal_display_refresh_rate_changed) is emitted.
