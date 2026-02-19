<span id="class_OpenXRSpatialComponentParentList"></span>

## OpenXRSpatialComponentParentList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the queries parent result data.

### Description

Object for storing the queries parent result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [RID](class_rid.md#class_RID) | [get_parent](class_openxrspatialcomponentparentlist.md#class_OpenXRSpatialComponentParentList_method_get_parent) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentParentList_method_get_parent"></span>

[RID](class_rid.md#class_RID) **get_parent** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentparentlist.md#class_OpenXRSpatialComponentParentList_method_get_parent)

Returns the RID for the parent entity at this `index`.
