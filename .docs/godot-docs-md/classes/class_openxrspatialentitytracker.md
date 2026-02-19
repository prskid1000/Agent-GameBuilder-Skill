<span id="class_OpenXRSpatialEntityTracker"></span>

## OpenXRSpatialEntityTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) **<** [XRTracker](class_xrtracker.md#class_XRTracker) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [OpenXRAnchorTracker](class_openxranchortracker.md#class_OpenXRAnchorTracker), [OpenXRMarkerTracker](class_openxrmarkertracker.md#class_OpenXRMarkerTracker), [OpenXRPlaneTracker](class_openxrplanetracker.md#class_OpenXRPlaneTracker)

Base class for Positional trackers managed by OpenXR's spatial entity extensions.

### Description

These are trackers created and managed by OpenXR's spatial entity extensions that give access to specific data related to OpenXR's spatial entities. They will always be of type `TRACKER_ANCHOR`.

### Properties


| [RID](class_rid.md#class_RID) | [entity](class_openxrspatialentitytracker.md#class_OpenXRSpatialEntityTracker_property_entity) | `RID()` |
| --- | --- | --- |
| [EntityTrackingState](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState) | [spatial_tracking_state](class_openxrspatialentitytracker.md#class_OpenXRSpatialEntityTracker_property_spatial_tracking_state) | `2` |
| [TrackerType](class_xrserver.md#enum_XRServer_TrackerType) | type | `8` (overrides [XRTracker](class_xrtracker.md#class_XRTracker_property_type)) |

---

### Signals

<span id="class_OpenXRSpatialEntityTracker_signal_spatial_tracking_state_changed"></span>

**spatial_tracking_state_changed** ( spatial_tracking_state: [int](class_int.md#class_int) ) [🔗](class_openxrspatialentitytracker.md#class_OpenXRSpatialEntityTracker_signal_spatial_tracking_state_changed)

.. container:: contribute

	There is currently no description for this signal. Please help us by contributing one!

---

### Enumerations

<span id="enum_OpenXRSpatialEntityTracker_EntityTrackingState"></span>

enum **EntityTrackingState**: [🔗](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState)

<span id="class_OpenXRSpatialEntityTracker_constant_ENTITY_TRACKING_STATE_STOPPED"></span>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState) **ENTITY_TRACKING_STATE_STOPPED** = `1`

This anchor has stopped tracking.

<span id="class_OpenXRSpatialEntityTracker_constant_ENTITY_TRACKING_STATE_PAUSED"></span>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState) **ENTITY_TRACKING_STATE_PAUSED** = `2`

Tracking is currently paused.

<span id="class_OpenXRSpatialEntityTracker_constant_ENTITY_TRACKING_STATE_TRACKING"></span>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState) **ENTITY_TRACKING_STATE_TRACKING** = `3`

This anchor is currently being tracked.

---

### Property Descriptions

<span id="class_OpenXRSpatialEntityTracker_property_entity"></span>

[RID](class_rid.md#class_RID) **entity** = `RID()` [🔗](class_openxrspatialentitytracker.md#class_OpenXRSpatialEntityTracker_property_entity)

- void **set_entity** ( value: [RID](class_rid.md#class_RID) )
- [RID](class_rid.md#class_RID) **get_entity** ( )

The spatial entity associated with this tracker.

---

<span id="class_OpenXRSpatialEntityTracker_property_spatial_tracking_state"></span>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState) **spatial_tracking_state** = `2` [🔗](class_openxrspatialentitytracker.md#class_OpenXRSpatialEntityTracker_property_spatial_tracking_state)

- void **set_spatial_tracking_state** ( value: [EntityTrackingState](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState) )
- [EntityTrackingState](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState) **get_spatial_tracking_state** ( )

The spatial tracking state for this tracker.
