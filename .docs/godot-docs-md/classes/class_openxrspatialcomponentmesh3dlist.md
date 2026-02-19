<span id="class_OpenXRSpatialComponentMesh3DList"></span>

## OpenXRSpatialComponentMesh3DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData](class_openxrspatialcomponentdata.md#class_OpenXRSpatialComponentData) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Object for storing the queries mesh3d result data.

### Description

Object for storing the queries 3d mesh result data when calling [OpenXRSpatialEntityExtension.query_snapshot()](class_openxrspatialentityextension.md#class_OpenXRSpatialEntityExtension_method_query_snapshot).

### Methods


| [Mesh](class_mesh.md#class_Mesh) | [get_mesh](class_openxrspatialcomponentmesh3dlist.md#class_OpenXRSpatialComponentMesh3DList_method_get_mesh) ( index: [int](class_int.md#class_int) ) const |
| --- | --- |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_transform](class_openxrspatialcomponentmesh3dlist.md#class_OpenXRSpatialComponentMesh3DList_method_get_transform) ( index: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_OpenXRSpatialComponentMesh3DList_method_get_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **get_mesh** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentmesh3dlist.md#class_OpenXRSpatialComponentMesh3DList_method_get_mesh)

Returns the mesh for the entity at this `index`.

---

<span id="class_OpenXRSpatialComponentMesh3DList_method_get_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_transform** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_openxrspatialcomponentmesh3dlist.md#class_OpenXRSpatialComponentMesh3DList_method_get_transform)

Returns the transform for positioning our mesh for the entity at this `index`.
