<span id="class_XRHandTracker"></span>

## XRHandTracker

**Inherits:** [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) **<** [XRTracker](class_xrtracker.md#class_XRTracker) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A tracked hand in XR.

### Description

A hand tracking system will create an instance of this object and add it to the [XRServer](class_xrserver.md#class_XRServer). This tracking system will then obtain skeleton data, convert it to the Godot Humanoid hand skeleton and store this data on the **XRHandTracker** object.

Use [XRHandModifier3D](class_xrhandmodifier3d.md#class_XRHandModifier3D) to animate a hand mesh using hand tracking data.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [TrackerHand](class_xrpositionaltracker.md#enum_XRPositionalTracker_TrackerHand) | hand | `1` (overrides [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker_property_hand)) |
| --- | --- | --- |
| [HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) | [hand_tracking_source](class_xrhandtracker.md#class_XRHandTracker_property_hand_tracking_source) | `0` |
| [bool](class_bool.md#class_bool) | [has_tracking_data](class_xrhandtracker.md#class_XRHandTracker_property_has_tracking_data) | `false` |
| [TrackerType](class_xrserver.md#enum_XRServer_TrackerType) | type | `16` (overrides [XRTracker](class_xrtracker.md#class_XRTracker_property_type)) |

### Methods


| [Vector3](class_vector3.md#class_Vector3) | [get_hand_joint_angular_velocity](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_angular_velocity) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) const |
| --- | --- |
| bitfield | \[[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags)\] | [get_hand_joint_flags](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_flags) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) | const |
| [Vector3](class_vector3.md#class_Vector3) | [get_hand_joint_linear_velocity](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_linear_velocity) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) const |
| [float](class_float.md#class_float) | [get_hand_joint_radius](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_radius) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_hand_joint_transform](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_transform) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) const |
| void | [set_hand_joint_angular_velocity](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_angular_velocity) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), angular_velocity: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [set_hand_joint_flags](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_flags) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), flags: | bitfield | \[[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags)\] ) |
| void | [set_hand_joint_linear_velocity](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_linear_velocity) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), linear_velocity: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [set_hand_joint_radius](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_radius) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), radius: [float](class_float.md#class_float) ) |
| void | [set_hand_joint_transform](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_transform) ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |

---

### Enumerations

<span id="enum_XRHandTracker_HandTrackingSource"></span>

enum **HandTrackingSource**: [🔗](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource)

<span id="class_XRHandTracker_constant_HAND_TRACKING_SOURCE_UNKNOWN"></span>

[HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) **HAND_TRACKING_SOURCE_UNKNOWN** = `0`

The source of hand tracking data is unknown.

<span id="class_XRHandTracker_constant_HAND_TRACKING_SOURCE_UNOBSTRUCTED"></span>

[HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) **HAND_TRACKING_SOURCE_UNOBSTRUCTED** = `1`

The source of hand tracking data is unobstructed, meaning that an accurate method of hand tracking is used. These include optical hand tracking, data gloves, etc.

<span id="class_XRHandTracker_constant_HAND_TRACKING_SOURCE_CONTROLLER"></span>

[HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) **HAND_TRACKING_SOURCE_CONTROLLER** = `2`

The source of hand tracking data is a controller, meaning that joint positions are inferred from controller inputs.

<span id="class_XRHandTracker_constant_HAND_TRACKING_SOURCE_NOT_TRACKED"></span>

[HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) **HAND_TRACKING_SOURCE_NOT_TRACKED** = `3`

No hand tracking data is tracked, this either means the hand is obscured, the controller is turned off, or tracking is not supported for the current input type.

<span id="class_XRHandTracker_constant_HAND_TRACKING_SOURCE_MAX"></span>

[HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) **HAND_TRACKING_SOURCE_MAX** = `4`

Represents the size of the [HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) enum.

---

<span id="enum_XRHandTracker_HandJoint"></span>

enum **HandJoint**: [🔗](class_xrhandtracker.md#enum_XRHandTracker_HandJoint)

<span id="class_XRHandTracker_constant_HAND_JOINT_PALM"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_PALM** = `0`

Palm joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_WRIST"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_WRIST** = `1`

Wrist joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_THUMB_METACARPAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_THUMB_METACARPAL** = `2`

Thumb metacarpal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_THUMB_PHALANX_PROXIMAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_THUMB_PHALANX_PROXIMAL** = `3`

Thumb phalanx proximal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_THUMB_PHALANX_DISTAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_THUMB_PHALANX_DISTAL** = `4`

Thumb phalanx distal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_THUMB_TIP"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_THUMB_TIP** = `5`

Thumb tip joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_METACARPAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_INDEX_FINGER_METACARPAL** = `6`

Index finger metacarpal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_PHALANX_PROXIMAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_INDEX_FINGER_PHALANX_PROXIMAL** = `7`

Index finger phalanx proximal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_PHALANX_INTERMEDIATE"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_INDEX_FINGER_PHALANX_INTERMEDIATE** = `8`

Index finger phalanx intermediate joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_PHALANX_DISTAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_INDEX_FINGER_PHALANX_DISTAL** = `9`

Index finger phalanx distal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_TIP"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_INDEX_FINGER_TIP** = `10`

Index finger tip joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_METACARPAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_MIDDLE_FINGER_METACARPAL** = `11`

Middle finger metacarpal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_PHALANX_PROXIMAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_MIDDLE_FINGER_PHALANX_PROXIMAL** = `12`

Middle finger phalanx proximal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_PHALANX_INTERMEDIATE"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_MIDDLE_FINGER_PHALANX_INTERMEDIATE** = `13`

Middle finger phalanx intermediate joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_PHALANX_DISTAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_MIDDLE_FINGER_PHALANX_DISTAL** = `14`

Middle finger phalanx distal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_TIP"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_MIDDLE_FINGER_TIP** = `15`

Middle finger tip joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_METACARPAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_RING_FINGER_METACARPAL** = `16`

Ring finger metacarpal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_PHALANX_PROXIMAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_RING_FINGER_PHALANX_PROXIMAL** = `17`

Ring finger phalanx proximal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_PHALANX_INTERMEDIATE"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_RING_FINGER_PHALANX_INTERMEDIATE** = `18`

Ring finger phalanx intermediate joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_PHALANX_DISTAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_RING_FINGER_PHALANX_DISTAL** = `19`

Ring finger phalanx distal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_TIP"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_RING_FINGER_TIP** = `20`

Ring finger tip joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_METACARPAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_PINKY_FINGER_METACARPAL** = `21`

Pinky finger metacarpal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_PHALANX_PROXIMAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_PINKY_FINGER_PHALANX_PROXIMAL** = `22`

Pinky finger phalanx proximal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_PHALANX_INTERMEDIATE"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_PINKY_FINGER_PHALANX_INTERMEDIATE** = `23`

Pinky finger phalanx intermediate joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_PHALANX_DISTAL"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_PINKY_FINGER_PHALANX_DISTAL** = `24`

Pinky finger phalanx distal joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_TIP"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_PINKY_FINGER_TIP** = `25`

Pinky finger tip joint.

<span id="class_XRHandTracker_constant_HAND_JOINT_MAX"></span>

[HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) **HAND_JOINT_MAX** = `26`

Represents the size of the [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) enum.

---

<span id="enum_XRHandTracker_HandJointFlags"></span>

flags **HandJointFlags**: [🔗](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags)

<span id="class_XRHandTracker_constant_HAND_JOINT_FLAG_ORIENTATION_VALID"></span>

[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags) **HAND_JOINT_FLAG_ORIENTATION_VALID** = `1`

The hand joint's orientation data is valid.

<span id="class_XRHandTracker_constant_HAND_JOINT_FLAG_ORIENTATION_TRACKED"></span>

[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags) **HAND_JOINT_FLAG_ORIENTATION_TRACKED** = `2`

The hand joint's orientation is actively tracked. May not be set if tracking has been temporarily lost.

<span id="class_XRHandTracker_constant_HAND_JOINT_FLAG_POSITION_VALID"></span>

[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags) **HAND_JOINT_FLAG_POSITION_VALID** = `4`

The hand joint's position data is valid.

<span id="class_XRHandTracker_constant_HAND_JOINT_FLAG_POSITION_TRACKED"></span>

[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags) **HAND_JOINT_FLAG_POSITION_TRACKED** = `8`

The hand joint's position is actively tracked. May not be set if tracking has been temporarily lost.

<span id="class_XRHandTracker_constant_HAND_JOINT_FLAG_LINEAR_VELOCITY_VALID"></span>

[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags) **HAND_JOINT_FLAG_LINEAR_VELOCITY_VALID** = `16`

The hand joint's linear velocity data is valid.

<span id="class_XRHandTracker_constant_HAND_JOINT_FLAG_ANGULAR_VELOCITY_VALID"></span>

[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags) **HAND_JOINT_FLAG_ANGULAR_VELOCITY_VALID** = `32`

The hand joint's angular velocity data is valid.

---

### Property Descriptions

<span id="class_XRHandTracker_property_hand_tracking_source"></span>

[HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) **hand_tracking_source** = `0` [🔗](class_xrhandtracker.md#class_XRHandTracker_property_hand_tracking_source)

- void **set_hand_tracking_source** ( value: [HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) )
- [HandTrackingSource](class_xrhandtracker.md#enum_XRHandTracker_HandTrackingSource) **get_hand_tracking_source** ( )

The source of the hand tracking data.

---

<span id="class_XRHandTracker_property_has_tracking_data"></span>

[bool](class_bool.md#class_bool) **has_tracking_data** = `false` [🔗](class_xrhandtracker.md#class_XRHandTracker_property_has_tracking_data)

- void **set_has_tracking_data** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_has_tracking_data** ( )

If `true`, the hand tracking data is valid.

---

### Method Descriptions

<span id="class_XRHandTracker_method_get_hand_joint_angular_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **get_hand_joint_angular_velocity** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) *const* [🔗](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_angular_velocity)

Returns the angular velocity for the given hand joint.

---

<span id="class_XRHandTracker_method_get_hand_joint_flags"></span>

*BitField*\[[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags)\] **get_hand_joint_flags** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) *const* [🔗](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_flags)

Returns flags about the validity of the tracking data for the given hand joint.

---

<span id="class_XRHandTracker_method_get_hand_joint_linear_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **get_hand_joint_linear_velocity** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) *const* [🔗](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_linear_velocity)

Returns the linear velocity for the given hand joint.

---

<span id="class_XRHandTracker_method_get_hand_joint_radius"></span>

[float](class_float.md#class_float) **get_hand_joint_radius** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) *const* [🔗](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_radius)

Returns the radius of the given hand joint.

---

<span id="class_XRHandTracker_method_get_hand_joint_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_hand_joint_transform** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint) ) *const* [🔗](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_transform)

Returns the transform for the given hand joint.

---

<span id="class_XRHandTracker_method_set_hand_joint_angular_velocity"></span>

void **set_hand_joint_angular_velocity** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), angular_velocity: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_angular_velocity)

Sets the angular velocity for the given hand joint.

---

<span id="class_XRHandTracker_method_set_hand_joint_flags"></span>

void **set_hand_joint_flags** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), flags: *BitField*\[[HandJointFlags](class_xrhandtracker.md#enum_XRHandTracker_HandJointFlags)\] ) [🔗](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_flags)

Sets flags about the validity of the tracking data for the given hand joint.

---

<span id="class_XRHandTracker_method_set_hand_joint_linear_velocity"></span>

void **set_hand_joint_linear_velocity** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), linear_velocity: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_linear_velocity)

Sets the linear velocity for the given hand joint.

---

<span id="class_XRHandTracker_method_set_hand_joint_radius"></span>

void **set_hand_joint_radius** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), radius: [float](class_float.md#class_float) ) [🔗](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_radius)

Sets the radius of the given hand joint.

---

<span id="class_XRHandTracker_method_set_hand_joint_transform"></span>

void **set_hand_joint_transform** ( joint: [HandJoint](class_xrhandtracker.md#enum_XRHandTracker_HandJoint), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_xrhandtracker.md#class_XRHandTracker_method_set_hand_joint_transform)

Sets the transform for the given hand joint.
