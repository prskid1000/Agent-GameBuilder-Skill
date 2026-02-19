<span id="class_OpenXRMarkerTracker"></span>

## OpenXRMarkerTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class_OpenXRSpatialEntityTracker) **<** [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) **<** [XRTracker](class_xrtracker.md#class_XRTracker) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Spatial entity tracker for our spatial entity marker tracking extension.

### Description

Spatial entity tracker for our OpenXR spatial entity marker tracking extension. These trackers identify entities in our real space detected by a visual marker such as a QRCode or Aruco code, and map their location to our virtual space.

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [bounds_size](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_property_bounds_size) | `Vector2(0, 0)` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [marker_id](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_property_marker_id) | `0` |
| [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) | [marker_type](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_property_marker_type) | `0` |

### Methods


| [Variant](class_variant.md#class_Variant) | [get_marker_data](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_method_get_marker_data) ( ) const |
| --- | --- |
| void | [set_marker_data](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_method_set_marker_data) ( marker_data: [Variant](class_variant.md#class_Variant) ) |

---

### Property Descriptions

<span id="class_OpenXRMarkerTracker_property_bounds_size"></span>

[Vector2](class_vector2.md#class_Vector2) **bounds_size** = `Vector2(0, 0)` [🔗](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_property_bounds_size)

- void **set_bounds_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_bounds_size** ( )

The bounds size for this marker.

---

<span id="class_OpenXRMarkerTracker_property_marker_id"></span>

[int](class_int.md#class_int) **marker_id** = `0` [🔗](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_property_marker_id)

- void **set_marker_id** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_marker_id** ( )

The marker ID for this marker, this is only returned for Aruco and April Tag markers. Call [get_marker_data()](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_method_get_marker_data) for QRCode markers.

---

<span id="class_OpenXRMarkerTracker_property_marker_type"></span>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) **marker_type** = `0` [🔗](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_property_marker_type)

- void **set_marker_type** ( value: [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) )
- [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) **get_marker_type** ( )

The type of marker.

---

### Method Descriptions

<span id="class_OpenXRMarkerTracker_method_get_marker_data"></span>

[Variant](class_variant.md#class_Variant) **get_marker_data** ( ) *const* [🔗](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_method_get_marker_data)

Returns the marker data for this marker. This can return a [String](class_string.md#class_String) or [PackedByteArray](class_packedbytearray.md#class_PackedByteArray). Only applicable to QR Code based markers.

---

<span id="class_OpenXRMarkerTracker_method_set_marker_data"></span>

void **set_marker_data** ( marker_data: [Variant](class_variant.md#class_Variant) ) [🔗](class_openxrmarkertracker.md#class_OpenXRMarkerTracker_method_set_marker_data)

Sets the marker data for this marker.

 **Note:** This should only be set by marker discovery logic.
