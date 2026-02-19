<span id="class_OpenXRSpatialComponentData"></span>

## OpenXRSpatialComponentData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [OpenXRSpatialComponentAnchorList](class_openxrspatialcomponentanchorlist.md#class_OpenXRSpatialComponentAnchorList), [OpenXRSpatialComponentBounded2DList](class_openxrspatialcomponentbounded2dlist.md#class_OpenXRSpatialComponentBounded2DList), [OpenXRSpatialComponentBounded3DList](class_openxrspatialcomponentbounded3dlist.md#class_OpenXRSpatialComponentBounded3DList), [OpenXRSpatialComponentMarkerList](class_openxrspatialcomponentmarkerlist.md#class_OpenXRSpatialComponentMarkerList), [OpenXRSpatialComponentMesh2DList](class_openxrspatialcomponentmesh2dlist.md#class_OpenXRSpatialComponentMesh2DList), [OpenXRSpatialComponentMesh3DList](class_openxrspatialcomponentmesh3dlist.md#class_OpenXRSpatialComponentMesh3DList), [OpenXRSpatialComponentParentList](class_openxrspatialcomponentparentlist.md#class_OpenXRSpatialComponentParentList), [OpenXRSpatialComponentPersistenceList](class_openxrspatialcomponentpersistencelist.md#class_OpenXRSpatialComponentPersistenceList), [OpenXRSpatialComponentPlaneAlignmentList](class_openxrspatialcomponentplanealignmentlist.md#class_OpenXRSpatialComponentPlaneAlignmentList), [OpenXRSpatialComponentPlaneSemanticLabelList](class_openxrspatialcomponentplanesemanticlabellist.md#class_OpenXRSpatialComponentPlaneSemanticLabelList), [OpenXRSpatialComponentPolygon2DList](class_openxrspatialcomponentpolygon2dlist.md#class_OpenXRSpatialComponentPolygon2DList), [OpenXRSpatialQueryResultData](class_openxrspatialqueryresultdata.md#class_OpenXRSpatialQueryResultData)

Object for storing OpenXR spatial entity component data.

### Description

Object for storing OpenXR spatial entity component data.

### Methods


| [int](class_int.md#class_int) | [_get_component_type](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData_private_method__get_component_type) ( ) | virtual | const |
| --- | --- | --- | --- |
| [int](class_int.md#class_int) | [_get_structure_data](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData_private_method__get_structure_data) ( next: [int](class_int.md#class_int) ) | virtual | const |
| void | [_set_capacity](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData_private_method__set_capacity) ( capacity: [int](class_int.md#class_int) ) virtual |
| void | [set_capacity](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData_method_set_capacity) ( capacity: [int](class_int.md#class_int) ) |

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentData_private_method__get_component_type"></span>

[int](class_int.md#class_int) **_get_component_type** ( ) *virtual* *const* [🔗](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData_private_method__get_component_type)

Return the component type for the component we store data for.

---

<span id="class_OpenXRSpatialComponentData_private_method__get_structure_data"></span>

[int](class_int.md#class_int) **_get_structure_data** ( next: [int](class_int.md#class_int) ) *virtual* *const* [🔗](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData_private_method__get_structure_data)

Return a pointer to the structure data that will be submitted along with the snapshot query. This pointer must remain valid as long as this object is instantiated.

---

<span id="class_OpenXRSpatialComponentData_private_method__set_capacity"></span>

void **_set_capacity** ( capacity: [int](class_int.md#class_int) ) *virtual* [🔗](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData_private_method__set_capacity)

Set the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.

---

<span id="class_OpenXRSpatialComponentData_method_set_capacity"></span>

void **set_capacity** ( capacity: [int](class_int.md#class_int) ) [🔗](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData_method_set_capacity)

Set the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.
