<span id="class_OpenXRSpatialComponentAnchorList"></span>

## OpenXRSpatialComponentAnchorList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the queries anchor result data.

### Description

Object for storing the queries anchor result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [Transform3D](class_transform3d.md#class_Transform3D) | [get_entity_pose](class_openxrspatialcomponentanchorlist.md#class_OpenXRSpatialComponentAnchorList_method_get_entity_pose) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentAnchorList_method_get_entity_pose"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_entity_pose** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentanchorlist.md#class_OpenXRSpatialComponentAnchorList_method_get_entity_pose)

Returns the transform for the entity at this `index`.
