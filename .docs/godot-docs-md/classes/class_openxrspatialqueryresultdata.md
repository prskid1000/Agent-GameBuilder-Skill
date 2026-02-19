<span id="class_OpenXRSpatialQueryResultData"></span>

## OpenXRSpatialQueryResultData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the main query result data.

### Description

Object for storing the main query result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot). This must always be the first component requested.

### Methods


| [int](class_int.md#class_int) | [get_capacity](class_openxrspatialqueryresultdata.md#class_OpenXRSpatialQueryResultData_method_get_capacity) ( ) const |
| --- | --- |
| [int](class_int.md#class_int) | [get_entity_id](class_openxrspatialqueryresultdata.md#class_OpenXRSpatialQueryResultData_method_get_entity_id) ( index: [int](class_int.md#class_int) ) const |
| [EntityTrackingState](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState) | [get_entity_state](class_openxrspatialqueryresultdata.md#class_OpenXRSpatialQueryResultData_method_get_entity_state) ( index: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_OpenXRSpatialQueryResultData_method_get_capacity"></span>

[int](class_int.md#class_int) **get_capacity** ( ) *const* [🔗](class_openxrspatialqueryresultdata.md#class_OpenXRSpatialQueryResultData_method_get_capacity)

Returns the number of entities that were retrieved.

---

<span id="class_OpenXRSpatialQueryResultData_method_get_entity_id"></span>

[int](class_int.md#class_int) **get_entity_id** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialqueryresultdata.md#class_OpenXRSpatialQueryResultData_method_get_entity_id)

Returns the entity id (`XrSpatialEntityIdEXT`) for the entity at this `index`.

---

<span id="class_OpenXRSpatialQueryResultData_method_get_entity_state"></span>

[EntityTrackingState](class_openxrspatialentitytracker.md#enum_OpenXRSpatialEntityTracker_EntityTrackingState) **get_entity_state** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialqueryresultdata.md#class_OpenXRSpatialQueryResultData_method_get_entity_state)

Returns the entity state for the entity at this `index`.
