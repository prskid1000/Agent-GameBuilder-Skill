<span id="class_XRPositionalTracker"></span>

## XRPositionalTracker

**Inherits:** [XRTracker](class_xrtracker.md#class_XRTracker) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class_OpenXRSpatialEntityTracker), [XRBodyTracker](class_xrbodytracker.md#class_XRBodyTracker), [XRControllerTracker](class_xrcontrollertracker.md#class_XRControllerTracker), [XRHandTracker](class_xrhandtracker.md#class_XRHandTracker)

A tracked object.

### Description

An instance of this object represents a device that is tracked, such as a controller or anchor point. HMDs aren't represented here as they are handled internally.

As controllers are turned on and the [XRInterface](class_xrinterface.md#class_XRInterface) detects them, instances of this object are automatically added to this list of active tracking objects accessible through the [XRServer](class_xrserver.md#class_XRServer).

The [XRNode3D](class_xrnode3d.md#class_XRNode3D) and [XRAnchor3D](class_xranchor3d.md#class_XRAnchor3D) both consume objects of this type and should be used in your project. The positional trackers are just under-the-hood objects that make this all work. These are mostly exposed so that GDExtension-based interfaces can interact with them.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) | [hand](class_xrpositionaltracker.md#class_XRPositionalTracker_property_hand) | `0` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [profile](class_xrpositionaltracker.md#class_XRPositionalTracker_property_profile) | `""` |

### Methods


| [Variant](class_variant.md#class_Variant) | [get_input](class_xrpositionaltracker.md#class_XRPositionalTracker_method_get_input) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| --- | --- |
| [XRPose](class_xrpose.md#class_XRPose) | [get_pose](class_xrpositionaltracker.md#class_XRPositionalTracker_method_get_pose) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_pose](class_xrpositionaltracker.md#class_XRPositionalTracker_method_has_pose) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| void | [invalidate_pose](class_xrpositionaltracker.md#class_XRPositionalTracker_method_invalidate_pose) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_input](class_xrpositionaltracker.md#class_XRPositionalTracker_method_set_input) ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |
| void | [set_pose](class_xrpositionaltracker.md#class_XRPositionalTracker_method_set_pose) ( name: [StringName](class_stringname.md#class_StringName), transform: [Transform3D](class_transform3d.md#class_Transform3D), linear_velocity: [Vector3](class_vector3.md#class_Vector3), angular_velocity: [Vector3](class_vector3.md#class_Vector3), tracking_confidence: [TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) ) |

---

### Signals

<span id="class_XRPositionalTracker_signal_button_pressed"></span>

**button_pressed** ( name: [String](class_string.md#class_String) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_signal_button_pressed)

Emitted when a button on this tracker is pressed. Note that many XR runtimes allow other inputs to be mapped to buttons.

---

<span id="class_XRPositionalTracker_signal_button_released"></span>

**button_released** ( name: [String](class_string.md#class_String) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_signal_button_released)

Emitted when a button on this tracker is released.

---

<span id="class_XRPositionalTracker_signal_input_float_changed"></span>

**input_float_changed** ( name: [String](class_string.md#class_String), value: [float](class_float.md#class_float) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_signal_input_float_changed)

Emitted when a trigger or similar input on this tracker changes value.

---

<span id="class_XRPositionalTracker_signal_input_vector2_changed"></span>

**input_vector2_changed** ( name: [String](class_string.md#class_String), vector: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_signal_input_vector2_changed)

Emitted when a thumbstick or thumbpad on this tracker moves.

---

<span id="class_XRPositionalTracker_signal_pose_changed"></span>

**pose_changed** ( pose: [XRPose](class_xrpose.md#class_XRPose) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_signal_pose_changed)

Emitted when the state of a pose tracked by this tracker changes.

---

<span id="class_XRPositionalTracker_signal_pose_lost_tracking"></span>

**pose_lost_tracking** ( pose: [XRPose](class_xrpose.md#class_XRPose) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_signal_pose_lost_tracking)

Emitted when a pose tracked by this tracker stops getting updated tracking data.

---

<span id="class_XRPositionalTracker_signal_profile_changed"></span>

**profile_changed** ( role: [String](class_string.md#class_String) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_signal_profile_changed)

Emitted when the profile of our tracker changes.

---

### Enumerations

<span id="enum_XRPositionalTracker_TrackerHand"></span>

enum **TrackerHand**: [🔗](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand)

<span id="class_XRPositionalTracker_constant_TRACKER_HAND_UNKNOWN"></span>

[TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) **TRACKER_HAND_UNKNOWN** = `0`

The hand this tracker is held in is unknown or not applicable.

<span id="class_XRPositionalTracker_constant_TRACKER_HAND_LEFT"></span>

[TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) **TRACKER_HAND_LEFT** = `1`

This tracker is the left hand controller.

<span id="class_XRPositionalTracker_constant_TRACKER_HAND_RIGHT"></span>

[TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) **TRACKER_HAND_RIGHT** = `2`

This tracker is the right hand controller.

<span id="class_XRPositionalTracker_constant_TRACKER_HAND_MAX"></span>

[TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) **TRACKER_HAND_MAX** = `3`

Represents the size of the [TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) enum.

---

### Property Descriptions

<span id="class_XRPositionalTracker_property_hand"></span>

[TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) **hand** = `0` [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_property_hand)

- void **set_tracker_hand** ( value: [TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) )
- [TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) **get_tracker_hand** ( )

Defines which hand this tracker relates to.

---

<span id="class_XRPositionalTracker_property_profile"></span>

[String](class_string.md#class_String) **profile** = `""` [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_property_profile)

- void **set_tracker_profile** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_tracker_profile** ( )

The profile associated with this tracker, interface dependent but will indicate the type of controller being tracked.

---

### Method Descriptions

<span id="class_XRPositionalTracker_method_get_input"></span>

[Variant](class_variant.md#class_Variant) **get_input** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_method_get_input)

**Deprecated:** Use through [XRControllerTracker](class_xrcontrollertracker.md#class_XRControllerTracker).

Returns an input for this tracker. It can return a boolean, float or [Vector2](class_vector2.md#class_Vector2) value depending on whether the input is a button, trigger or thumbstick/thumbpad.

---

<span id="class_XRPositionalTracker_method_get_pose"></span>

[XRPose](class_xrpose.md#class_XRPose) **get_pose** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_method_get_pose)

Returns the current [XRPose](class_xrpose.md#class_XRPose) state object for the bound `name` pose.

---

<span id="class_XRPositionalTracker_method_has_pose"></span>

[bool](class_bool.md#class_bool) **has_pose** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_method_has_pose)

Returns `true` if the tracker is available and is currently tracking the bound `name` pose.

---

<span id="class_XRPositionalTracker_method_invalidate_pose"></span>

void **invalidate_pose** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_method_invalidate_pose)

Marks this pose as invalid, we don't clear the last reported state but it allows users to decide if trackers need to be hidden if we lose tracking or just remain at their last known position.

---

<span id="class_XRPositionalTracker_method_set_input"></span>

void **set_input** ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_method_set_input)

**Deprecated:** Use through [XRControllerTracker](class_xrcontrollertracker.md#class_XRControllerTracker).

Changes the value for the given input. This method is called by an [XRInterface](class_xrinterface.md#class_XRInterface) implementation and should not be used directly.

---

<span id="class_XRPositionalTracker_method_set_pose"></span>

void **set_pose** ( name: [StringName](class_stringname.md#class_StringName), transform: [Transform3D](class_transform3d.md#class_Transform3D), linear_velocity: [Vector3](class_vector3.md#class_Vector3), angular_velocity: [Vector3](class_vector3.md#class_Vector3), tracking_confidence: [TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) ) [🔗](class_xrpositionaltracker.md#class_XRPositionalTracker_method_set_pose)

Sets the transform, linear velocity, angular velocity and tracking confidence for the given pose. This method is called by an [XRInterface](class_xrinterface.md#class_XRInterface) implementation and should not be used directly.
