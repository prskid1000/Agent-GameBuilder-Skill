<span id="class_OpenXRSpatialComponentBounded2DList"></span>

## OpenXRSpatialComponentBounded2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the queries bounded2d result data.

### Description

Object for storing the queries 2D bounding rectangle result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [Transform3D](class_transform3d.md#class_Transform3D) | [get_center_pose](class_openxrspatialcomponentbounded2dlist.md#class_OpenXRSpatialComponentBounded2DList_method_get_center_pose) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [get_size](class_openxrspatialcomponentbounded2dlist.md#class_OpenXRSpatialComponentBounded2DList_method_get_size) ( index: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentBounded2DList_method_get_center_pose"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_center_pose** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentbounded2dlist.md#class_OpenXRSpatialComponentBounded2DList_method_get_center_pose)

Returns the center of our bounding rectangle for the entity at this `index`.

---

<span id="class_OpenXRSpatialComponentBounded2DList_method_get_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_size** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentbounded2dlist.md#class_OpenXRSpatialComponentBounded2DList_method_get_size)

Returns the size of our bounding rectangle for the entity at this `index`.
