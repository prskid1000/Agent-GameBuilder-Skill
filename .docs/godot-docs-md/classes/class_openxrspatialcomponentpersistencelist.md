<span id="class_OpenXRSpatialComponentPersistenceList"></span>

## OpenXRSpatialComponentPersistenceList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the query persistence result data.

### Description

Object for storing the query persistence result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [int](class_int.md#class_int) | [get_persistent_state](class_openxrspatialcomponentpersistencelist.md#class_OpenXRSpatialComponentPersistenceList_method_get_persistent_state) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [String](class_string.md#class_String) | [get_persistent_uuid](class_openxrspatialcomponentpersistencelist.md#class_OpenXRSpatialComponentPersistenceList_method_get_persistent_uuid) ( index: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentPersistenceList_method_get_persistent_state"></span>

[int](class_int.md#class_int) **get_persistent_state** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentpersistencelist.md#class_OpenXRSpatialComponentPersistenceList_method_get_persistent_state)

Returns the persistent state (`XrSpatialPersistenceStateEXT`) for the entity at this `index`.

---

<span id="class_OpenXRSpatialComponentPersistenceList_method_get_persistent_uuid"></span>

[String](class_string.md#class_String) **get_persistent_uuid** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentpersistencelist.md#class_OpenXRSpatialComponentPersistenceList_method_get_persistent_uuid)

Returns the persistent uuid for the entity at this `index`.
