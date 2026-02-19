<span id="class_Geometry3D"></span>

## Geometry3D

**Inherits:** [Object](class_object.md#class_Object)

Provides methods for some common 3D geometric operations.

### Description

Provides a set of helper functions to create geometric shapes, compute intersections between shapes, and process various other geometric operations in 3D.

### Methods


| [Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] | [build_box_planes](class_geometry3d.md#class_Geometry3D_method_build_box_planes) ( extents: [Vector3](class_vector3.md#class_Vector3) ) |
| --- | --- |
| [Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] | [build_capsule_planes](class_geometry3d.md#class_Geometry3D_method_build_capsule_planes) ( radius: [float](class_float.md#class_float), height: [float](class_float.md#class_float), sides: [int](class_int.md#class_int), lats: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) = 2 ) |
| [Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] | [build_cylinder_planes](class_geometry3d.md#class_Geometry3D_method_build_cylinder_planes) ( radius: [float](class_float.md#class_float), height: [float](class_float.md#class_float), sides: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) = 2 ) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [clip_polygon](class_geometry3d.md#class_Geometry3D_method_clip_polygon) ( points: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), plane: [Plane](class_plane.md#class_Plane) ) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [compute_convex_mesh_points](class_geometry3d.md#class_Geometry3D_method_compute_convex_mesh_points) ( planes: [Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] ) |
| [Vector3](class_vector3.md#class_Vector3) | [get_closest_point_to_segment](class_geometry3d.md#class_Geometry3D_method_get_closest_point_to_segment) ( point: [Vector3](class_vector3.md#class_Vector3), s1: [Vector3](class_vector3.md#class_Vector3), s2: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3](class_vector3.md#class_Vector3) | [get_closest_point_to_segment_uncapped](class_geometry3d.md#class_Geometry3D_method_get_closest_point_to_segment_uncapped) ( point: [Vector3](class_vector3.md#class_Vector3), s1: [Vector3](class_vector3.md#class_Vector3), s2: [Vector3](class_vector3.md#class_Vector3) ) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [get_closest_points_between_segments](class_geometry3d.md#class_Geometry3D_method_get_closest_points_between_segments) ( p1: [Vector3](class_vector3.md#class_Vector3), p2: [Vector3](class_vector3.md#class_Vector3), q1: [Vector3](class_vector3.md#class_Vector3), q2: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3](class_vector3.md#class_Vector3) | [get_triangle_barycentric_coords](class_geometry3d.md#class_Geometry3D_method_get_triangle_barycentric_coords) ( point: [Vector3](class_vector3.md#class_Vector3), a: [Vector3](class_vector3.md#class_Vector3), b: [Vector3](class_vector3.md#class_Vector3), c: [Vector3](class_vector3.md#class_Vector3) ) |
| [Variant](class_variant.md#class_Variant) | [ray_intersects_triangle](class_geometry3d.md#class_Geometry3D_method_ray_intersects_triangle) ( from: [Vector3](class_vector3.md#class_Vector3), dir: [Vector3](class_vector3.md#class_Vector3), a: [Vector3](class_vector3.md#class_Vector3), b: [Vector3](class_vector3.md#class_Vector3), c: [Vector3](class_vector3.md#class_Vector3) ) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [segment_intersects_convex](class_geometry3d.md#class_Geometry3D_method_segment_intersects_convex) ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), planes: [Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] ) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [segment_intersects_cylinder](class_geometry3d.md#class_Geometry3D_method_segment_intersects_cylinder) ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), height: [float](class_float.md#class_float), radius: [float](class_float.md#class_float) ) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [segment_intersects_sphere](class_geometry3d.md#class_Geometry3D_method_segment_intersects_sphere) ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), sphere_position: [Vector3](class_vector3.md#class_Vector3), sphere_radius: [float](class_float.md#class_float) ) |
| [Variant](class_variant.md#class_Variant) | [segment_intersects_triangle](class_geometry3d.md#class_Geometry3D_method_segment_intersects_triangle) ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), a: [Vector3](class_vector3.md#class_Vector3), b: [Vector3](class_vector3.md#class_Vector3), c: [Vector3](class_vector3.md#class_Vector3) ) |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [tetrahedralize_delaunay](class_geometry3d.md#class_Geometry3D_method_tetrahedralize_delaunay) ( points: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) |

---

### Method Descriptions

<span id="class_Geometry3D_method_build_box_planes"></span>

[Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] **build_box_planes** ( extents: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_geometry3d.md#class_Geometry3D_method_build_box_planes)

Returns an array with 6 [Plane](class_plane.md#class_Plane) s that describe the sides of a box centered at the origin. The box size is defined by `extents`, which represents one (positive) corner of the box (i.e. half its actual size).

---

<span id="class_Geometry3D_method_build_capsule_planes"></span>

[Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] **build_capsule_planes** ( radius: [float](class_float.md#class_float), height: [float](class_float.md#class_float), sides: [int](class_int.md#class_int), lats: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) = 2 ) [🔗](class_geometry3d.md#class_Geometry3D_method_build_capsule_planes)

Returns an array of [Plane](class_plane.md#class_Plane) s closely bounding a faceted capsule centered at the origin with radius `radius` and height `height`. The parameter `sides` defines how many planes will be generated for the side part of the capsule, whereas `lats` gives the number of latitudinal steps at the bottom and top of the capsule. The parameter `axis` describes the axis along which the capsule is oriented (0 for X, 1 for Y, 2 for Z).

---

<span id="class_Geometry3D_method_build_cylinder_planes"></span>

[Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] **build_cylinder_planes** ( radius: [float](class_float.md#class_float), height: [float](class_float.md#class_float), sides: [int](class_int.md#class_int), axis: [Axis](class_vector3.md#enum_Vector3_Axis) = 2 ) [🔗](class_geometry3d.md#class_Geometry3D_method_build_cylinder_planes)

Returns an array of [Plane](class_plane.md#class_Plane) s closely bounding a faceted cylinder centered at the origin with radius `radius` and height `height`. The parameter `sides` defines how many planes will be generated for the round part of the cylinder. The parameter `axis` describes the axis along which the cylinder is oriented (0 for X, 1 for Y, 2 for Z).

---

<span id="class_Geometry3D_method_clip_polygon"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **clip_polygon** ( points: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), plane: [Plane](class_plane.md#class_Plane) ) [🔗](class_geometry3d.md#class_Geometry3D_method_clip_polygon)

Clips the polygon defined by the points in `points` against the `plane` and returns the points of the clipped polygon.

---

<span id="class_Geometry3D_method_compute_convex_mesh_points"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **compute_convex_mesh_points** ( planes: [Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] ) [🔗](class_geometry3d.md#class_Geometry3D_method_compute_convex_mesh_points)

Calculates and returns all the vertex points of a convex shape defined by an array of `planes`.

---

<span id="class_Geometry3D_method_get_closest_point_to_segment"></span>

[Vector3](class_vector3.md#class_Vector3) **get_closest_point_to_segment** ( point: [Vector3](class_vector3.md#class_Vector3), s1: [Vector3](class_vector3.md#class_Vector3), s2: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_geometry3d.md#class_Geometry3D_method_get_closest_point_to_segment)

Returns the 3D point on the 3D segment (`s1`, `s2`) that is closest to `point`. The returned point will always be inside the specified segment.

---

<span id="class_Geometry3D_method_get_closest_point_to_segment_uncapped"></span>

[Vector3](class_vector3.md#class_Vector3) **get_closest_point_to_segment_uncapped** ( point: [Vector3](class_vector3.md#class_Vector3), s1: [Vector3](class_vector3.md#class_Vector3), s2: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_geometry3d.md#class_Geometry3D_method_get_closest_point_to_segment_uncapped)

Returns the 3D point on the 3D line defined by (`s1`, `s2`) that is closest to `point`. The returned point can be inside the segment (`s1`, `s2`) or outside of it, i.e. somewhere on the line extending from the segment.

---

<span id="class_Geometry3D_method_get_closest_points_between_segments"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_closest_points_between_segments** ( p1: [Vector3](class_vector3.md#class_Vector3), p2: [Vector3](class_vector3.md#class_Vector3), q1: [Vector3](class_vector3.md#class_Vector3), q2: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_geometry3d.md#class_Geometry3D_method_get_closest_points_between_segments)

Given the two 3D segments (`p1`, `p2`) and (`q1`, `q2`), finds those two points on the two segments that are closest to each other. Returns a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) that contains this point on (`p1`, `p2`) as well the accompanying point on (`q1`, `q2`).

---

<span id="class_Geometry3D_method_get_triangle_barycentric_coords"></span>

[Vector3](class_vector3.md#class_Vector3) **get_triangle_barycentric_coords** ( point: [Vector3](class_vector3.md#class_Vector3), a: [Vector3](class_vector3.md#class_Vector3), b: [Vector3](class_vector3.md#class_Vector3), c: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_geometry3d.md#class_Geometry3D_method_get_triangle_barycentric_coords)

Returns a [Vector3](class_vector3.md#class_Vector3) containing weights based on how close a 3D position (`point`) is to a triangle's different vertices (`a`, `b` and `c`). This is useful for interpolating between the data of different vertices in a triangle. One example use case is using this to smoothly rotate over a mesh instead of relying solely on face normals.

 Here is a more detailed explanation of barycentric coordinates.

---

<span id="class_Geometry3D_method_ray_intersects_triangle"></span>

[Variant](class_variant.md#class_Variant) **ray_intersects_triangle** ( from: [Vector3](class_vector3.md#class_Vector3), dir: [Vector3](class_vector3.md#class_Vector3), a: [Vector3](class_vector3.md#class_Vector3), b: [Vector3](class_vector3.md#class_Vector3), c: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_geometry3d.md#class_Geometry3D_method_ray_intersects_triangle)

Tests if the 3D ray starting at `from` with the direction of `dir` intersects the triangle specified by `a`, `b` and `c`. If yes, returns the point of intersection as [Vector3](class_vector3.md#class_Vector3). If no intersection takes place, returns `null`.

---

<span id="class_Geometry3D_method_segment_intersects_convex"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **segment_intersects_convex** ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), planes: [Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\] ) [🔗](class_geometry3d.md#class_Geometry3D_method_segment_intersects_convex)

Given a convex hull defined though the [Plane](class_plane.md#class_Plane) s in the array `planes`, tests if the segment (`from`, `to`) intersects with that hull. If an intersection is found, returns a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) containing the point the intersection and the hull's normal. Otherwise, returns an empty array.

---

<span id="class_Geometry3D_method_segment_intersects_cylinder"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **segment_intersects_cylinder** ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), height: [float](class_float.md#class_float), radius: [float](class_float.md#class_float) ) [🔗](class_geometry3d.md#class_Geometry3D_method_segment_intersects_cylinder)

Checks if the segment (`from`, `to`) intersects the cylinder with height `height` that is centered at the origin and has radius `radius`. If no, returns an empty [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array). If an intersection takes place, the returned array contains the point of intersection and the cylinder's normal at the point of intersection.

---

<span id="class_Geometry3D_method_segment_intersects_sphere"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **segment_intersects_sphere** ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), sphere_position: [Vector3](class_vector3.md#class_Vector3), sphere_radius: [float](class_float.md#class_float) ) [🔗](class_geometry3d.md#class_Geometry3D_method_segment_intersects_sphere)

Checks if the segment (`from`, `to`) intersects the sphere that is located at `sphere_position` and has radius `sphere_radius`. If no, returns an empty [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array). If yes, returns a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) containing the point of intersection and the sphere's normal at the point of intersection.

---

<span id="class_Geometry3D_method_segment_intersects_triangle"></span>

[Variant](class_variant.md#class_Variant) **segment_intersects_triangle** ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), a: [Vector3](class_vector3.md#class_Vector3), b: [Vector3](class_vector3.md#class_Vector3), c: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_geometry3d.md#class_Geometry3D_method_segment_intersects_triangle)

Tests if the segment (`from`, `to`) intersects the triangle `a`, `b`, `c`. If yes, returns the point of intersection as [Vector3](class_vector3.md#class_Vector3). If no intersection takes place, returns `null`.

---

<span id="class_Geometry3D_method_tetrahedralize_delaunay"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **tetrahedralize_delaunay** ( points: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) [🔗](class_geometry3d.md#class_Geometry3D_method_tetrahedralize_delaunay)

Tetrahedralizes the volume specified by a discrete set of `points` in 3D space, ensuring that no point lies within the circumsphere of any resulting tetrahedron. The method returns a [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) where each tetrahedron consists of four consecutive point indices into the `points` array (resulting in an array with `n * 4` elements, where `n` is the number of tetrahedra found). If the tetrahedralization is unsuccessful, an empty [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) is returned.
