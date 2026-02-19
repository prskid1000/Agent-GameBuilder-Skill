<span id="class_XRServer"></span>

## XRServer

**Inherits:** [Object](class_object.md#class_Object)

Server for AR and VR features.

### Description

The AR/VR server is the heart of our Advanced and Virtual Reality solution and handles all the processing.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [bool](class_bool.md#class_bool) | [camera_locked_to_origin](class_xrserver.md#class_XRServer_property_camera_locked_to_origin) | `false` |
| --- | --- | --- |
| [XRInterface](class_xrinterface.md#class_XRInterface) | [primary_interface](class_xrserver.md#class_XRServer_property_primary_interface) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [world_origin](class_xrserver.md#class_XRServer_property_world_origin) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |
| [float](class_float.md#class_float) | [world_scale](class_xrserver.md#class_XRServer_property_world_scale) | `1.0` |

### Methods


| void | [add_interface](class_xrserver.md#class_XRServer_method_add_interface) ( interface: [XRInterface](class_xrinterface.md#class_XRInterface) ) |
| --- | --- |
| void | [add_tracker](class_xrserver.md#class_XRServer_method_add_tracker) ( tracker: [XRTracker](class_xrtracker.md#class_XRTracker) ) |
| void | [center_on_hmd](class_xrserver.md#class_XRServer_method_center_on_hmd) ( rotation_mode: [RotationMode](class_xrserver.md#enum_XRServer_RotationMode), keep_height: [bool](class_bool.md#class_bool) ) |
| void | [clear_reference_frame](class_xrserver.md#class_XRServer_method_clear_reference_frame) ( ) |
| [XRInterface](class_xrinterface.md#class_XRInterface) | [find_interface](class_xrserver.md#class_XRServer_method_find_interface) ( name: [String](class_string.md#class_String) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_hmd_transform](class_xrserver.md#class_XRServer_method_get_hmd_transform) ( ) |
| [XRInterface](class_xrinterface.md#class_XRInterface) | [get_interface](class_xrserver.md#class_XRServer_method_get_interface) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_interface_count](class_xrserver.md#class_XRServer_method_get_interface_count) ( ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_interfaces](class_xrserver.md#class_XRServer_method_get_interfaces) ( ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_reference_frame](class_xrserver.md#class_XRServer_method_get_reference_frame) ( ) const |
| [XRTracker](class_xrtracker.md#class_XRTracker) | [get_tracker](class_xrserver.md#class_XRServer_method_get_tracker) ( tracker_name: [StringName](class_stringname.md#class_StringName) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_trackers](class_xrserver.md#class_XRServer_method_get_trackers) ( tracker_types: [int](class_int.md#class_int) ) |
| void | [remove_interface](class_xrserver.md#class_XRServer_method_remove_interface) ( interface: [XRInterface](class_xrinterface.md#class_XRInterface) ) |
| void | [remove_tracker](class_xrserver.md#class_XRServer_method_remove_tracker) ( tracker: [XRTracker](class_xrtracker.md#class_XRTracker) ) |

---

### Signals

<span id="class_XRServer_signal_interface_added"></span>

**interface_added** ( interface_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_xrserver.md#class_XRServer_signal_interface_added)

Emitted when a new interface has been added.

---

<span id="class_XRServer_signal_interface_removed"></span>

**interface_removed** ( interface_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_xrserver.md#class_XRServer_signal_interface_removed)

Emitted when an interface is removed.

---

<span id="class_XRServer_signal_reference_frame_changed"></span>

**reference_frame_changed** ( ) [🔗](class_xrserver.md#class_XRServer_signal_reference_frame_changed)

Emitted when the reference frame transform changes.

---

<span id="class_XRServer_signal_tracker_added"></span>

**tracker_added** ( tracker_name: [StringName](class_stringname.md#class_StringName), type: [int](class_int.md#class_int) ) [🔗](class_xrserver.md#class_XRServer_signal_tracker_added)

Emitted when a new tracker has been added. If you don't use a fixed number of controllers or if you're using [XRAnchor3D](class_xranchor3d.md#class_XRAnchor3D) s for an AR solution, it is important to react to this signal to add the appropriate [XRController3D](class_xrcontroller3d.md#class_XRController3D) or [XRAnchor3D](class_xranchor3d.md#class_XRAnchor3D) nodes related to this new tracker.

---

<span id="class_XRServer_signal_tracker_removed"></span>

**tracker_removed** ( tracker_name: [StringName](class_stringname.md#class_StringName), type: [int](class_int.md#class_int) ) [🔗](class_xrserver.md#class_XRServer_signal_tracker_removed)

Emitted when a tracker is removed. You should remove any [XRController3D](class_xrcontroller3d.md#class_XRController3D) or [XRAnchor3D](class_xranchor3d.md#class_XRAnchor3D) points if applicable. This is not mandatory, the nodes simply become inactive and will be made active again when a new tracker becomes available (i.e. a new controller is switched on that takes the place of the previous one).

---

<span id="class_XRServer_signal_tracker_updated"></span>

**tracker_updated** ( tracker_name: [StringName](class_stringname.md#class_StringName), type: [int](class_int.md#class_int) ) [🔗](class_xrserver.md#class_XRServer_signal_tracker_updated)

Emitted when an existing tracker has been updated. This can happen if the user switches controllers.

---

### Enumerations

<span id="enum_XRServer_TrackerType"></span>

enum **TrackerType**: [🔗](class_xrserver.md#enum_XRServer_TrackerType)

<span id="class_XRServer_constant_TRACKER_HEAD"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_HEAD** = `1`

The tracker tracks the location of the player's head. This is usually a location centered between the player's eyes. Note that for handheld AR devices this can be the current location of the device.

<span id="class_XRServer_constant_TRACKER_CONTROLLER"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_CONTROLLER** = `2`

The tracker tracks the location of a controller.

<span id="class_XRServer_constant_TRACKER_BASESTATION"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_BASESTATION** = `4`

The tracker tracks the location of a base station.

<span id="class_XRServer_constant_TRACKER_ANCHOR"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_ANCHOR** = `8`

The tracker tracks the location and size of an AR anchor.

<span id="class_XRServer_constant_TRACKER_HAND"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_HAND** = `16`

The tracker tracks the location and joints of a hand.

<span id="class_XRServer_constant_TRACKER_BODY"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_BODY** = `32`

The tracker tracks the location and joints of a body.

<span id="class_XRServer_constant_TRACKER_FACE"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_FACE** = `64`

The tracker tracks the expressions of a face.

<span id="class_XRServer_constant_TRACKER_ANY_KNOWN"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_ANY_KNOWN** = `127`

Used internally to filter trackers of any known type.

<span id="class_XRServer_constant_TRACKER_UNKNOWN"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_UNKNOWN** = `128`

Used internally if we haven't set the tracker type yet.

<span id="class_XRServer_constant_TRACKER_ANY"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **TRACKER_ANY** = `255`

Used internally to select all trackers.

---

<span id="enum_XRServer_RotationMode"></span>

enum **RotationMode**: [🔗](class_xrserver.md#enum_XRServer_RotationMode)

<span id="class_XRServer_constant_RESET_FULL_ROTATION"></span>

[RotationMode](class_xrserver.md#enum_XRServer_RotationMode) **RESET_FULL_ROTATION** = `0`

Fully reset the orientation of the HMD. Regardless of what direction the user is looking to in the real world. The user will look dead ahead in the virtual world.

<span id="class_XRServer_constant_RESET_BUT_KEEP_TILT"></span>

[RotationMode](class_xrserver.md#enum_XRServer_RotationMode) **RESET_BUT_KEEP_TILT** = `1`

Resets the orientation but keeps the tilt of the device. So if we're looking down, we keep looking down but heading will be reset.

<span id="class_XRServer_constant_DONT_RESET_ROTATION"></span>

[RotationMode](class_xrserver.md#enum_XRServer_RotationMode) **DONT_RESET_ROTATION** = `2`

Does not reset the orientation of the HMD, only the position of the player gets centered.

---

### Property Descriptions

<span id="class_XRServer_property_camera_locked_to_origin"></span>

[bool](class_bool.md#class_bool) **camera_locked_to_origin** = `false` [🔗](class_xrserver.md#class_XRServer_property_camera_locked_to_origin)

- void **set_camera_locked_to_origin** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_camera_locked_to_origin** ( )

If set to `true`, the scene will be rendered as if the camera is locked to the [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D).

 **Note:** This doesn't provide a very comfortable experience for users. This setting exists for doing benchmarking or automated testing, where you want to control what is rendered via code.

---

<span id="class_XRServer_property_primary_interface"></span>

[XRInterface](class_xrinterface.md#class_XRInterface) **primary_interface** [🔗](class_xrserver.md#class_XRServer_property_primary_interface)

- void **set_primary_interface** ( value: [XRInterface](class_xrinterface.md#class_XRInterface) )
- [XRInterface](class_xrinterface.md#class_XRInterface) **get_primary_interface** ( )

The primary [XRInterface](class_xrinterface.md#class_XRInterface) currently bound to the **XRServer**.

---

<span id="class_XRServer_property_world_origin"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **world_origin** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_xrserver.md#class_XRServer_property_world_origin)

- void **set_world_origin** ( value: [Transform3D](class_transform3d.md#class_Transform3D) )
- [Transform3D](class_transform3d.md#class_Transform3D) **get_world_origin** ( )

The current origin of our tracking space in the virtual world. This is used by the renderer to properly position the camera with new tracking data.

 **Note:** This property is managed by the current [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D) node. It is exposed for access from GDExtensions.

---

<span id="class_XRServer_property_world_scale"></span>

[float](class_float.md#class_float) **world_scale** = `1.0` [🔗](class_xrserver.md#class_XRServer_property_world_scale)

- void **set_world_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_world_scale** ( )

The scale of the game world compared to the real world. By default, most AR/VR platforms assume that 1 game unit corresponds to 1 real world meter.

---

### Method Descriptions

<span id="class_XRServer_method_add_interface"></span>

void **add_interface** ( interface: [XRInterface](class_xrinterface.md#class_XRInterface) ) [🔗](class_xrserver.md#class_XRServer_method_add_interface)

Registers an [XRInterface](class_xrinterface.md#class_XRInterface) object.

---

<span id="class_XRServer_method_add_tracker"></span>

void **add_tracker** ( tracker: [XRTracker](class_xrtracker.md#class_XRTracker) ) [🔗](class_xrserver.md#class_XRServer_method_add_tracker)

Registers a new [XRTracker](class_xrtracker.md#class_XRTracker) that tracks a physical object.

---

<span id="class_XRServer_method_center_on_hmd"></span>

void **center_on_hmd** ( rotation_mode: [RotationMode](class_xrserver.md#enum_XRServer_RotationMode), keep_height: [bool](class_bool.md#class_bool) ) [🔗](class_xrserver.md#class_XRServer_method_center_on_hmd)

This is an important function to understand correctly. AR and VR platforms all handle positioning slightly differently.

For platforms that do not offer spatial tracking, our origin point `(0, 0, 0)` is the location of our HMD, but you have little control over the direction the player is facing in the real world.

For platforms that do offer spatial tracking, our origin point depends very much on the system. For OpenVR, our origin point is usually the center of the tracking space, on the ground. For other platforms, it's often the location of the tracking camera.

This method allows you to center your tracker on the location of the HMD. It will take the current location of the HMD and use that to adjust all your tracking data; in essence, realigning the real world to your player's current position in the game world.

For this method to produce usable results, tracking information must be available. This often takes a few frames after starting your game.

You should call this method after a few seconds have passed. For example, when the user requests a realignment of the display holding a designated button on a controller for a short period of time, or when implementing a teleport mechanism.

---

<span id="class_XRServer_method_clear_reference_frame"></span>

void **clear_reference_frame** ( ) [🔗](class_xrserver.md#class_XRServer_method_clear_reference_frame)

Clears the reference frame that was set by previous calls to [center_on_hmd()](class_xrserver.md#class_XRServer_method_center_on_hmd).

---

<span id="class_XRServer_method_find_interface"></span>

[XRInterface](class_xrinterface.md#class_XRInterface) **find_interface** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_xrserver.md#class_XRServer_method_find_interface)

Finds an interface by its `name`. For example, if your project uses capabilities of an AR/VR platform, you can find the interface for that platform by name and initialize it.

---

<span id="class_XRServer_method_get_hmd_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_hmd_transform** ( ) [🔗](class_xrserver.md#class_XRServer_method_get_hmd_transform)

Returns the primary interface's transformation.

---

<span id="class_XRServer_method_get_interface"></span>

[XRInterface](class_xrinterface.md#class_XRInterface) **get_interface** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_xrserver.md#class_XRServer_method_get_interface)

Returns the interface registered at the given `idx` index in the list of interfaces.

---

<span id="class_XRServer_method_get_interface_count"></span>

[int](class_int.md#class_int) **get_interface_count** ( ) *const* [🔗](class_xrserver.md#class_XRServer_method_get_interface_count)

Returns the number of interfaces currently registered with the AR/VR server. If your project supports multiple AR/VR platforms, you can look through the available interface, and either present the user with a selection or simply try to initialize each interface and use the first one that returns `true`.

---

<span id="class_XRServer_method_get_interfaces"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_interfaces** ( ) *const* [🔗](class_xrserver.md#class_XRServer_method_get_interfaces)

Returns a list of available interfaces the ID and name of each interface.

---

<span id="class_XRServer_method_get_reference_frame"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_reference_frame** ( ) *const* [🔗](class_xrserver.md#class_XRServer_method_get_reference_frame)

Returns the reference frame transform. Mostly used internally and exposed for GDExtension build interfaces.

---

<span id="class_XRServer_method_get_tracker"></span>

[XRTracker](class_xrtracker.md#class_XRTracker) **get_tracker** ( tracker_name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_xrserver.md#class_XRServer_method_get_tracker)

Returns the positional tracker with the given `tracker_name`.

---

<span id="class_XRServer_method_get_trackers"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_trackers** ( tracker_types: [int](class_int.md#class_int) ) [🔗](class_xrserver.md#class_XRServer_method_get_trackers)

Returns a dictionary of trackers for `tracker_types`.

---

<span id="class_XRServer_method_remove_interface"></span>

void **remove_interface** ( interface: [XRInterface](class_xrinterface.md#class_XRInterface) ) [🔗](class_xrserver.md#class_XRServer_method_remove_interface)

Removes this `interface`.

---

<span id="class_XRServer_method_remove_tracker"></span>

void **remove_tracker** ( tracker: [XRTracker](class_xrtracker.md#class_XRTracker) ) [🔗](class_xrserver.md#class_XRServer_method_remove_tracker)

Removes this `tracker`.
