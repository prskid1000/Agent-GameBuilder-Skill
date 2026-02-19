<span id="class_OpenXRSpatialComponentPolygon2DList"></span>

## OpenXRSpatialComponentPolygon2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the queries polygon2d result data.

### Description

Object for storing the queries 2D polygon result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [Transform3D](class_transform3d.md#class_Transform3D) | [get_transform](class_openxrspatialcomponentpolygon2dlist.md#class_OpenXRSpatialComponentPolygon2DList_method_get_transform) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [get_vertices](class_openxrspatialcomponentpolygon2dlist.md#class_OpenXRSpatialComponentPolygon2DList_method_get_vertices) ( snapshot: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentPolygon2DList_method_get_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_transform** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentpolygon2dlist.md#class_OpenXRSpatialComponentPolygon2DList_method_get_transform)

Returns the transform for positioning our polygon for the entity at this `index`.

---

<span id="class_OpenXRSpatialComponentPolygon2DList_method_get_vertices"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_vertices** ( snapshot: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentpolygon2dlist.md#class_OpenXRSpatialComponentPolygon2DList_method_get_vertices)

Returns the polygon vertices for the entity at this `index`.
