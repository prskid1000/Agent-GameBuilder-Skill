<span id="class_OpenXRSpatialComponentBounded3DList"></span>

## OpenXRSpatialComponentBounded3DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the queries bounded3d result data.

### Description

Object for storing the queries 3d bounding box result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [Transform3D](class_transform3d.md#class_Transform3D) | [get_center_pose](class_openxrspatialcomponentbounded3dlist.md#class_OpenXRSpatialComponentBounded3DList_method_get_center_pose) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [get_size](class_openxrspatialcomponentbounded3dlist.md#class_OpenXRSpatialComponentBounded3DList_method_get_size) ( index: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentBounded3DList_method_get_center_pose"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_center_pose** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentbounded3dlist.md#class_OpenXRSpatialComponentBounded3DList_method_get_center_pose)

Returns the center of our bounding box for the entity at this `index`.

---

<span id="class_OpenXRSpatialComponentBounded3DList_method_get_size"></span>

[Vector3](class_vector3.md#class_Vector3) **get_size** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentbounded3dlist.md#class_OpenXRSpatialComponentBounded3DList_method_get_size)

Returns the size of our bounding box for the entity at this `index`.
