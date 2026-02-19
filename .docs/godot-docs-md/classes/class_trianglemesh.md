<span id="class_TriangleMesh"></span>

## TriangleMesh

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Triangle geometry for efficient, physicsless intersection queries.

### Description

Creates a bounding volume hierarchy (BVH) tree structure around triangle geometry.

The triangle BVH tree can be used for efficient intersection queries without involving a physics engine.

For example, this can be used in editor tools to select objects with complex shapes based on the mouse cursor position.

 **Performance:** Creating the BVH tree for complex geometry is a slow process and best done in a background thread.

### Methods


| [bool](class_bool.md#class_bool) | [create_from_faces](class_trianglemesh.md#class_TriangleMesh_method_create_from_faces) ( faces: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) |
| --- | --- |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [get_faces](class_trianglemesh.md#class_TriangleMesh_method_get_faces) ( ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [intersect_ray](class_trianglemesh.md#class_TriangleMesh_method_intersect_ray) ( begin: [Vector3](class_vector3.md#class_Vector3), dir: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [intersect_segment](class_trianglemesh.md#class_TriangleMesh_method_intersect_segment) ( begin: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3) ) const |

---

### Method Descriptions

<span id="class_TriangleMesh_method_create_from_faces"></span>

[bool](class_bool.md#class_bool) **create_from_faces** ( faces: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) [🔗](class_trianglemesh.md#class_TriangleMesh_method_create_from_faces)

Creates the BVH tree from an array of faces. Each 3 vertices of the input `faces` array represent one triangle (face).

Returns `true` if the tree is successfully built, `false` otherwise.

---

<span id="class_TriangleMesh_method_get_faces"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_faces** ( ) *const* [🔗](class_trianglemesh.md#class_TriangleMesh_method_get_faces)

Returns a copy of the geometry faces. Each 3 vertices of the array represent one triangle (face).

---

<span id="class_TriangleMesh_method_intersect_ray"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **intersect_ray** ( begin: [Vector3](class_vector3.md#class_Vector3), dir: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_trianglemesh.md#class_TriangleMesh_method_intersect_ray)

Tests for intersection with a ray starting at `begin` and facing `dir` and extending toward infinity.

If an intersection with a triangle happens, returns a [Dictionary](class_dictionary.md#class_Dictionary) with the following fields:

 `position`: The position on the intersected triangle.

 `normal`: The normal of the intersected triangle.

 `face_index`: The index of the intersected triangle.

Returns an empty [Dictionary](class_dictionary.md#class_Dictionary) if no intersection happens.

See also [intersect_segment()](class_trianglemesh.md#class_TriangleMesh_method_intersect_segment), which is similar but uses a finite-length segment.

---

<span id="class_TriangleMesh_method_intersect_segment"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **intersect_segment** ( begin: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_trianglemesh.md#class_TriangleMesh_method_intersect_segment)

Tests for intersection with a segment going from `begin` to `end`.

If an intersection with a triangle happens returns a [Dictionary](class_dictionary.md#class_Dictionary) with the following fields:

 `position`: The position on the intersected triangle.

 `normal`: The normal of the intersected triangle.

 `face_index`: The index of the intersected triangle.

Returns an empty [Dictionary](class_dictionary.md#class_Dictionary) if no intersection happens.

See also [intersect_ray()](class_trianglemesh.md#class_TriangleMesh_method_intersect_ray), which is similar but uses an infinite-length ray.
