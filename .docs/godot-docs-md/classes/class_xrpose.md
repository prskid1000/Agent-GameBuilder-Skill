<span id="class_XRPose"></span>

## XRPose

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

This object contains all data related to a pose on a tracked object.

### Description

XR runtimes often identify multiple locations on devices such as controllers that are spatially tracked.

Orientation, location, linear velocity and angular velocity are all provided for each pose by the XR runtime. This object contains this state of a pose.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [angular_velocity](class_xrpose.md#class_XRPose_property_angular_velocity) | `Vector3(0, 0, 0)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [has_tracking_data](class_xrpose.md#class_XRPose_property_has_tracking_data) | `false` |
| [Vector3](class_vector3.md#class_Vector3) | [linear_velocity](class_xrpose.md#class_XRPose_property_linear_velocity) | `Vector3(0, 0, 0)` |
| [StringName](class_stringname.md#class_StringName) | [name](class_xrpose.md#class_XRPose_property_name) | `&""` |
| [TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) | [tracking_confidence](class_xrpose.md#class_XRPose_property_tracking_confidence) | `0` |
| [Transform3D](class_transform3d.md#class_Transform3D) | [transform](class_xrpose.md#class_XRPose_property_transform) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |

### Methods


| [Transform3D](class_transform3d.md#class_Transform3D) | [get_adjusted_transform](class_xrpose.md#class_XRPose_method_get_adjusted_transform) ( ) const |
| --- | --- |

---

### Enumerations

<span id="enum_XRPose_TrackingConfidence"></span>

enum **TrackingConfidence**: [🔗](class_xrpose.md#enum_XRPose_TrackingConfidence)

<span id="class_XRPose_constant_XR_TRACKING_CONFIDENCE_NONE"></span>

[TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) **XR_TRACKING_CONFIDENCE_NONE** = `0`

No tracking information is available for this pose.

<span id="class_XRPose_constant_XR_TRACKING_CONFIDENCE_LOW"></span>

[TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) **XR_TRACKING_CONFIDENCE_LOW** = `1`

Tracking information may be inaccurate or estimated. For example, with inside out tracking this would indicate a controller may be (partially) obscured.

<span id="class_XRPose_constant_XR_TRACKING_CONFIDENCE_HIGH"></span>

[TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) **XR_TRACKING_CONFIDENCE_HIGH** = `2`

Tracking information is considered accurate and up to date.

---

### Property Descriptions

<span id="class_XRPose_property_angular_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **angular_velocity** = `Vector3(0, 0, 0)` [🔗](class_xrpose.md#class_XRPose_property_angular_velocity)

- void **set_angular_velocity** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_angular_velocity** ( )

The angular velocity for this pose.

---

<span id="class_XRPose_property_has_tracking_data"></span>

[bool](class_bool.md#class_bool) **has_tracking_data** = `false` [🔗](class_xrpose.md#class_XRPose_property_has_tracking_data)

- void **set_has_tracking_data** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_has_tracking_data** ( )

If `true` our tracking data is up to date. If `false` we're no longer receiving new tracking data and our state is whatever that last valid state was.

---

<span id="class_XRPose_property_linear_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **linear_velocity** = `Vector3(0, 0, 0)` [🔗](class_xrpose.md#class_XRPose_property_linear_velocity)

- void **set_linear_velocity** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_linear_velocity** ( )

The linear velocity of this pose.

---

<span id="class_XRPose_property_name"></span>

[StringName](class_stringname.md#class_StringName) **name** = `&""` [🔗](class_xrpose.md#class_XRPose_property_name)

- void **set_name** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_name** ( )

The name of this pose. Usually, this name is derived from an action map set up by the user. Godot also suggests some pose names that [XRInterface](class_xrinterface.md#class_XRInterface) objects are expected to implement:

- `root` is the root location, often used for tracked objects that do not have further nodes.

- `aim` is the tip of a controller with its orientation pointing outwards, often used for raycasts.

- `grip` is the location where the user grips the controller.

- `skeleton` is the root location for a hand mesh, when using hand tracking and an animated skeleton is supplied by the XR runtime.

---

<span id="class_XRPose_property_tracking_confidence"></span>

[TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) **tracking_confidence** = `0` [🔗](class_xrpose.md#class_XRPose_property_tracking_confidence)

- void **set_tracking_confidence** ( value: [TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) )
- [TrackingConfidence](class_xrpose.md#enum_XRPose_TrackingConfidence) **get_tracking_confidence** ( )

The tracking confidence for this pose, provides insight on how accurate the spatial positioning of this record is.

---

<span id="class_XRPose_property_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_xrpose.md#class_XRPose_property_transform)

- void **set_transform** ( value: [Transform3D](class_transform3d.md#class_Transform3D) )
- [Transform3D](class_transform3d.md#class_Transform3D) **get_transform** ( )

The transform containing the original and transform as reported by the XR runtime.

---

### Method Descriptions

<span id="class_XRPose_method_get_adjusted_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_adjusted_transform** ( ) *const* [🔗](class_xrpose.md#class_XRPose_method_get_adjusted_transform)

Returns the [transform](class_xrpose.md#class_XRPose_property_transform) with world scale and our reference frame applied. This is the transform used to position [XRNode3D](class_xrnode3d.md#class_XRNode3D) objects.
