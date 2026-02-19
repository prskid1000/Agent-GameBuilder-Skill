<span id="class_MobileVRInterface"></span>

## MobileVRInterface

**Inherits:** [XRInterface](class_xrinterface.md#class_XRInterface) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Generic mobile VR implementation.

### Description

This is a generic mobile VR implementation where you need to provide details about the phone and HMD used. It does not rely on any existing framework. This is the most basic interface we have. For the best effect, you need a mobile phone with a gyroscope and accelerometer.

Note that even though there is no positional tracking, the camera will assume the headset is at a height of 1.85 meters. You can change this by setting [eye_height](class_mobilevrinterface.md#class_MobileVRInterface_property_eye_height).

You can initialize this interface as follows:

::

    var interface = XRServer.find_interface("Native mobile")
    if interface and interface.initialize():
        get_viewport().use_xr = true

 **Note:** For Android, ProjectSettings.input_devices/sensors/enable_accelerometer, ProjectSettings.input_devices/sensors/enable_gravity, ProjectSettings.input_devices/sensors/enable_gyroscope and ProjectSettings.input_devices/sensors/enable_magnetometer must be enabled.

### Properties


| [float](class_float.md#class_float) | [display_to_lens](class_mobilevrinterface.md#class_MobileVRInterface_property_display_to_lens) | `4.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [display_width](class_mobilevrinterface.md#class_MobileVRInterface_property_display_width) | `14.5` |
| [float](class_float.md#class_float) | [eye_height](class_mobilevrinterface.md#class_MobileVRInterface_property_eye_height) | `1.85` |
| [float](class_float.md#class_float) | [iod](class_mobilevrinterface.md#class_MobileVRInterface_property_iod) | `6.0` |
| [float](class_float.md#class_float) | [k1](class_mobilevrinterface.md#class_MobileVRInterface_property_k1) | `0.215` |
| [float](class_float.md#class_float) | [k2](class_mobilevrinterface.md#class_MobileVRInterface_property_k2) | `0.215` |
| [Rect2](class_rect2.md#class_Rect2) | [offset_rect](class_mobilevrinterface.md#class_MobileVRInterface_property_offset_rect) | `Rect2(0, 0, 1, 1)` |
| [float](class_float.md#class_float) | [oversample](class_mobilevrinterface.md#class_MobileVRInterface_property_oversample) | `1.5` |
| [float](class_float.md#class_float) | [vrs_min_radius](class_mobilevrinterface.md#class_MobileVRInterface_property_vrs_min_radius) | `20.0` |
| [float](class_float.md#class_float) | [vrs_strength](class_mobilevrinterface.md#class_MobileVRInterface_property_vrs_strength) | `1.0` |
| [PlayAreaMode](class_xrinterface.md#enum_XRInterface_PlayAreaMode) | xr_play_area_mode | `1` (overrides [XRInterface](class_xrinterface.md#class_XRInterface_property_xr_play_area_mode)) |

---

### Property Descriptions

<span id="class_MobileVRInterface_property_display_to_lens"></span>

[float](class_float.md#class_float) **display_to_lens** = `4.0` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_display_to_lens)

- void **set_display_to_lens** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_display_to_lens** ( )

The distance between the display and the lenses inside of the device in centimeters.

---

<span id="class_MobileVRInterface_property_display_width"></span>

[float](class_float.md#class_float) **display_width** = `14.5` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_display_width)

- void **set_display_width** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_display_width** ( )

The width of the display in centimeters.

---

<span id="class_MobileVRInterface_property_eye_height"></span>

[float](class_float.md#class_float) **eye_height** = `1.85` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_eye_height)

- void **set_eye_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_eye_height** ( )

The height at which the camera is placed in relation to the ground (i.e. [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D) node).

---

<span id="class_MobileVRInterface_property_iod"></span>

[float](class_float.md#class_float) **iod** = `6.0` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_iod)

- void **set_iod** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_iod** ( )

The interocular distance, also known as the interpupillary distance. The distance between the pupils of the left and right eye.

---

<span id="class_MobileVRInterface_property_k1"></span>

[float](class_float.md#class_float) **k1** = `0.215` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_k1)

- void **set_k1** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_k1** ( )

The k1 lens factor is one of the two constants that define the strength of the lens used and directly influences the lens distortion effect.

---

<span id="class_MobileVRInterface_property_k2"></span>

[float](class_float.md#class_float) **k2** = `0.215` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_k2)

- void **set_k2** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_k2** ( )

The k2 lens factor, see k1.

---

<span id="class_MobileVRInterface_property_offset_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **offset_rect** = `Rect2(0, 0, 1, 1)` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_offset_rect)

- void **set_offset_rect** ( value: [Rect2](class_rect2.md#class_Rect2) )
- [Rect2](class_rect2.md#class_Rect2) **get_offset_rect** ( )

Set the offset rect relative to the area being rendered. A length of 1 represents the whole rendering area on that axis.

---

<span id="class_MobileVRInterface_property_oversample"></span>

[float](class_float.md#class_float) **oversample** = `1.5` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_oversample)

- void **set_oversample** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_oversample** ( )

The oversample setting. Because of the lens distortion we have to render our buffers at a higher resolution then the screen can natively handle. A value between 1.5 and 2.0 often provides good results but at the cost of performance.

---

<span id="class_MobileVRInterface_property_vrs_min_radius"></span>

[float](class_float.md#class_float) **vrs_min_radius** = `20.0` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_vrs_min_radius)

- void **set_vrs_min_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_vrs_min_radius** ( )

The minimum radius around the focal point where full quality is guaranteed if VRS is used as a percentage of screen size.

 **Note:** Mobile and Forward+ renderers only. Requires [Viewport.vrs_mode](class_viewport.md#class_Viewport_property_vrs_mode) to be set to [Viewport.VRS_XR](class_viewport.md#class_Viewport_constant_VRS_XR).

---

<span id="class_MobileVRInterface_property_vrs_strength"></span>

[float](class_float.md#class_float) **vrs_strength** = `1.0` [🔗](class_mobilevrinterface.md#class_MobileVRInterface_property_vrs_strength)

- void **set_vrs_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_vrs_strength** ( )

The strength used to calculate the VRS density map. The greater this value, the more noticeable VRS is. This improves performance at the cost of quality.

 **Note:** Mobile and Forward+ renderers only. Requires [Viewport.vrs_mode](class_viewport.md#class_Viewport_property_vrs_mode) to be set to [Viewport.VRS_XR](class_viewport.md#class_Viewport_constant_VRS_XR).
