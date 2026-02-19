<span id="class_OpenXRSpatialComponentMarkerList"></span>

## OpenXRSpatialComponentMarkerList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the queries marker result data.

### Description

Object for storing the queries marker result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [Variant](class_variant.md#class_Variant) | [get_marker_data](class_openxrspatialcomponentmarkerlist.md#class_OpenXRSpatialComponentMarkerList_method_get_marker_data) ( snapshot: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_marker_id](class_openxrspatialcomponentmarkerlist.md#class_OpenXRSpatialComponentMarkerList_method_get_marker_id) ( index: [int](class_int.md#class_int) ) const |
| [MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) | [get_marker_type](class_openxrspatialcomponentmarkerlist.md#class_OpenXRSpatialComponentMarkerList_method_get_marker_type) ( index: [int](class_int.md#class_int) ) const |

---

### Enumerations

<span id="enum_OpenXRSpatialComponentMarkerList_MarkerType"></span>

enum **MarkerType**: [🔗](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType)

<span id="class_OpenXRSpatialComponentMarkerList_constant_MARKER_TYPE_UNKNOWN"></span>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) **MARKER_TYPE_UNKNOWN** = `0`

Unknown or unset marker type.

<span id="class_OpenXRSpatialComponentMarkerList_constant_MARKER_TYPE_QRCODE"></span>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) **MARKER_TYPE_QRCODE** = `1`

Marker based on a QR code.

<span id="class_OpenXRSpatialComponentMarkerList_constant_MARKER_TYPE_MICRO_QRCODE"></span>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) **MARKER_TYPE_MICRO_QRCODE** = `2`

Marker based on a micro QR code.

<span id="class_OpenXRSpatialComponentMarkerList_constant_MARKER_TYPE_ARUCO"></span>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) **MARKER_TYPE_ARUCO** = `3`

Marker based on an Aruco code.

<span id="class_OpenXRSpatialComponentMarkerList_constant_MARKER_TYPE_APRIL_TAG"></span>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) **MARKER_TYPE_APRIL_TAG** = `4`

Marker based on an April Tag.

<span id="class_OpenXRSpatialComponentMarkerList_constant_MARKER_TYPE_MAX"></span>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) **MARKER_TYPE_MAX** = `5`

Maximum value for this enum.

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentMarkerList_method_get_marker_data"></span>

[Variant](class_variant.md#class_Variant) **get_marker_data** ( snapshot: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentmarkerlist.md#class_OpenXRSpatialComponentMarkerList_method_get_marker_data)

Returns either a [String](class_string.md#class_String) or a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) buffer with data for the marker at this `index`. Only applicable for QR code markers.

---

<span id="class_OpenXRSpatialComponentMarkerList_method_get_marker_id"></span>

[int](class_int.md#class_int) **get_marker_id** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentmarkerlist.md#class_OpenXRSpatialComponentMarkerList_method_get_marker_id)

Returns the marker ID for the marker at this `index`. Only applicable for Aruco or April Tag markers.

---

<span id="class_OpenXRSpatialComponentMarkerList_method_get_marker_type"></span>

[MarkerType](class_openxrspatialcomponentmarkerlist.md#enum_OpenXRSpatialComponentMarkerList_MarkerType) **get_marker_type** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentmarkerlist.md#class_OpenXRSpatialComponentMarkerList_method_get_marker_type)

Returns the marker type for the marker at this `index`.
