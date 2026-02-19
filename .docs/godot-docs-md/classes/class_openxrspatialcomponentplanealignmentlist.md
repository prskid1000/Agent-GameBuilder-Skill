<span id="class_OpenXRSpatialComponentPlaneAlignmentList"></span>

## OpenXRSpatialComponentPlaneAlignmentList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the queries plane alignment result data.

### Description

Object for storing the queries plane alignment result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) | [get_plane_alignment](class_openxrspatialcomponentplanealignmentlist.md#class_OpenXRSpatialComponentPlaneAlignmentList_method_get_plane_alignment) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |

---

### Enumerations

<span id="enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment"></span>

enum **PlaneAlignment**: [🔗](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment)

<span id="class_OpenXRSpatialComponentPlaneAlignmentList_constant_PLANE_ALIGNMENT_HORIZONTAL_UPWARD"></span>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) **PLANE_ALIGNMENT_HORIZONTAL_UPWARD** = `0`

Plane is facing upward.

<span id="class_OpenXRSpatialComponentPlaneAlignmentList_constant_PLANE_ALIGNMENT_HORIZONTAL_DOWNWARD"></span>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) **PLANE_ALIGNMENT_HORIZONTAL_DOWNWARD** = `1`

Plane is facing downwards.

<span id="class_OpenXRSpatialComponentPlaneAlignmentList_constant_PLANE_ALIGNMENT_VERTICAL"></span>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) **PLANE_ALIGNMENT_VERTICAL** = `2`

Plane is vertically aligned.

<span id="class_OpenXRSpatialComponentPlaneAlignmentList_constant_PLANE_ALIGNMENT_ARBITRARY"></span>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) **PLANE_ALIGNMENT_ARBITRARY** = `3`

Plane has an arbitrary alignment.

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentPlaneAlignmentList_method_get_plane_alignment"></span>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) **get_plane_alignment** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentplanealignmentlist.md#class_OpenXRSpatialComponentPlaneAlignmentList_method_get_plane_alignment)

Returns the plane alignment for the parent entity at this `index`.
