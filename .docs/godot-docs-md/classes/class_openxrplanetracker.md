<span id="class_OpenXRPlaneTracker"></span>

## OpenXRPlaneTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker](class_openxrspatialentitytracker.md#class_OpenXRSpatialEntityTracker) **<** [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) **<** [XRTracker](class_xrtracker.md#class_XRTracker) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Spatial entity tracker for our spatial entity plane tracking extension.

### Description

Spatial entity tracker for our OpenXR spatial entity plane tracking extension. These trackers identify entities in our real space such as walls, floors, tables, etc. and map their location to our virtual space.

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [bounds_size](class_openxrplanetracker.md#class_OpenXRPlaneTracker_property_bounds_size) | `Vector2(0, 0)` |
| --- | --- | --- |
| [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) | [plane_alignment](class_openxrplanetracker.md#class_OpenXRPlaneTracker_property_plane_alignment) | `0` |
| [String](class_string.md#class_String) | [plane_label](class_openxrplanetracker.md#class_OpenXRPlaneTracker_property_plane_label) | `""` |

### Methods


| void | [clear_mesh_data](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_clear_mesh_data) ( ) |
| --- | --- |
| [Mesh](class_mesh.md#class_Mesh) | [get_mesh](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_get_mesh) ( ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_mesh_offset](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_get_mesh_offset) ( ) const |
| [Shape3D](class_shape3d.md#class_Shape3D) | [get_shape](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_get_shape) ( thickness: [float](class_float.md#class_float) = 0.01 ) |
| void | [set_mesh_data](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_set_mesh_data) ( origin: [Transform3D](class_transform3d.md#class_Transform3D), vertices: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) = PackedInt32Array() ) |

---

### Signals

<span id="class_OpenXRPlaneTracker_signal_mesh_changed"></span>

**mesh_changed** ( ) [🔗](class_openxrplanetracker.md#class_OpenXRPlaneTracker_signal_mesh_changed)

Emitted when our mesh data has changed the mesh instance and collision needs to be updated.

---

### Property Descriptions

<span id="class_OpenXRPlaneTracker_property_bounds_size"></span>

[Vector2](class_vector2.md#class_Vector2) **bounds_size** = `Vector2(0, 0)` [🔗](class_openxrplanetracker.md#class_OpenXRPlaneTracker_property_bounds_size)

- void **set_bounds_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_bounds_size** ( )

The bounding size of the plane. This is a 2D size.

---

<span id="class_OpenXRPlaneTracker_property_plane_alignment"></span>

[PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) **plane_alignment** = `0` [🔗](class_openxrplanetracker.md#class_OpenXRPlaneTracker_property_plane_alignment)

- void **set_plane_alignment** ( value: [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) )
- [PlaneAlignment](class_openxrspatialcomponentplanealignmentlist.md#enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment) **get_plane_alignment** ( )

The main alignment in space of this plane.

---

<span id="class_OpenXRPlaneTracker_property_plane_label"></span>

[String](class_string.md#class_String) **plane_label** = `""` [🔗](class_openxrplanetracker.md#class_OpenXRPlaneTracker_property_plane_label)

- void **set_plane_label** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_plane_label** ( )

The semantic label for this plane.

---

### Method Descriptions

<span id="class_OpenXRPlaneTracker_method_clear_mesh_data"></span>

void **clear_mesh_data** ( ) [🔗](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_clear_mesh_data)

Clears the mesh data for this tracker. You should only call this if you are handling your own discovery logic.

---

<span id="class_OpenXRPlaneTracker_method_get_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **get_mesh** ( ) [🔗](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_get_mesh)

Gets a mesh created from either the mesh data or from our bounding size for this plane.

---

<span id="class_OpenXRPlaneTracker_method_get_mesh_offset"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_mesh_offset** ( ) *const* [🔗](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_get_mesh_offset)

Gets the transform by which to offset the mesh and collision shape from our pose to display these correctly.

---

<span id="class_OpenXRPlaneTracker_method_get_shape"></span>

[Shape3D](class_shape3d.md#class_Shape3D) **get_shape** ( thickness: [float](class_float.md#class_float) = 0.01 ) [🔗](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_get_shape)

Gets a collision shape built either from the mesh data or from our bounding size for this plane.

---

<span id="class_OpenXRPlaneTracker_method_set_mesh_data"></span>

void **set_mesh_data** ( origin: [Transform3D](class_transform3d.md#class_Transform3D), vertices: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) = PackedInt32Array() ) [🔗](class_openxrplanetracker.md#class_OpenXRPlaneTracker_method_set_mesh_data)

Sets the mesh data for this plane. You should only call this if you are handling your own discovery logic.
