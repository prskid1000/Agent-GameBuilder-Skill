<span id="class_XRTracker"></span>

## XRTracker

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [XRFaceTracker](class_xrfacetracker.md#class_XRFaceTracker), [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker)

A tracked object.

### Description

This object is the base of all XR trackers.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [String](class_string.md#class_String) | [description](class_xrtracker.md#class_XRTracker_property_description) | `""` |
| --- | --- | --- |
| [StringName](class_stringname.md#class_StringName) | [name](class_xrtracker.md#class_XRTracker_property_name) | `&"Unknown"` |
| [TrackerType](class_xrserver.md#enum_XRServer_TrackerType) | [type](class_xrtracker.md#class_XRTracker_property_type) | `128` |

---

### Property Descriptions

<span id="class_XRTracker_property_description"></span>

[String](class_string.md#class_String) **description** = `""` [🔗](class_xrtracker.md#class_XRTracker_property_description)

- void **set_tracker_desc** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_tracker_desc** ( )

The description of this tracker.

---

<span id="class_XRTracker_property_name"></span>

[StringName](class_stringname.md#class_StringName) **name** = `&"Unknown"` [🔗](class_xrtracker.md#class_XRTracker_property_name)

- void **set_tracker_name** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_tracker_name** ( )

The unique name of this tracker. The trackers that are available differ between various XR runtimes and can often be configured by the user. Godot maintains a number of reserved names that it expects the [XRInterface](class_xrinterface.md#class_XRInterface) to implement if applicable:

- `"head"` identifies the [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) of the player's head

- `"left_hand"` identifies the [XRControllerTracker](class_xrcontrollertracker.md#class_XRControllerTracker) in the player's left hand

- `"right_hand"` identifies the [XRControllerTracker](class_xrcontrollertracker.md#class_XRControllerTracker) in the player's right hand

- `"/user/hand_tracker/left"` identifies the [XRHandTracker](class_xrhandtracker.md#class_XRHandTracker) for the player's left hand

- `"/user/hand_tracker/right"` identifies the [XRHandTracker](class_xrhandtracker.md#class_XRHandTracker) for the player's right hand

- `"/user/body_tracker"` identifies the [XRBodyTracker](class_xrbodytracker.md#class_XRBodyTracker) for the player's body

- `"/user/face_tracker"` identifies the [XRFaceTracker](class_xrfacetracker.md#class_XRFaceTracker) for the player's face

---

<span id="class_XRTracker_property_type"></span>

[TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **type** = `128` [🔗](class_xrtracker.md#class_XRTracker_property_type)

- void **set_tracker_type** ( value: [TrackerType](class_xrserver.md#enum_XRServer_TrackerType) )
- [TrackerType](class_xrserver.md#enum_XRServer_TrackerType) **get_tracker_type** ( )

The type of tracker.
