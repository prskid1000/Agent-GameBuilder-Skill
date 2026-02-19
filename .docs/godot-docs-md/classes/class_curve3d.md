<span id="class_Curve3D"></span>

## Curve3D

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Describes a Bézier curve in 3D space.

### Description

This class describes a Bézier curve in 3D space. It is mainly used to give a shape to a [Path3D](class_path3d.md#class_Path3D), but can be manually sampled for other purposes.

It keeps a cache of precalculated points along the curve, to speed up further calculations.

### Properties


| [float](class_float.md#class_float) | [bake_interval](class_curve3d.md#class_Curve3D_property_bake_interval) | `0.2` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [closed](class_curve3d.md#class_Curve3D_property_closed) | `false` |
| [int](class_int.md#class_int) | [point_count](class_curve3d.md#class_Curve3D_property_point_count) | `0` |
| [bool](class_bool.md#class_bool) | [up_vector_enabled](class_curve3d.md#class_Curve3D_property_up_vector_enabled) | `true` |

### Methods


| void | [add_point](class_curve3d.md#class_Curve3D_method_add_point) ( position: [Vector3](class_vector3.md#class_Vector3), in: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 0, 0), out: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 0, 0), index: [int](class_int.md#class_int) = -1 ) |
| --- | --- |
| void | [clear_points](class_curve3d.md#class_Curve3D_method_clear_points) ( ) |
| [float](class_float.md#class_float) | [get_baked_length](class_curve3d.md#class_Curve3D_method_get_baked_length) ( ) const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [get_baked_points](class_curve3d.md#class_Curve3D_method_get_baked_points) ( ) const |
| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [get_baked_tilts](class_curve3d.md#class_Curve3D_method_get_baked_tilts) ( ) const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [get_baked_up_vectors](class_curve3d.md#class_Curve3D_method_get_baked_up_vectors) ( ) const |
| [float](class_float.md#class_float) | [get_closest_offset](class_curve3d.md#class_Curve3D_method_get_closest_offset) ( to_point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_closest_point](class_curve3d.md#class_Curve3D_method_get_closest_point) ( to_point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_point_in](class_curve3d.md#class_Curve3D_method_get_point_in) ( idx: [int](class_int.md#class_int) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_point_out](class_curve3d.md#class_Curve3D_method_get_point_out) ( idx: [int](class_int.md#class_int) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_point_position](class_curve3d.md#class_Curve3D_method_get_point_position) ( idx: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_point_tilt](class_curve3d.md#class_Curve3D_method_get_point_tilt) ( idx: [int](class_int.md#class_int) ) const |
| void | [remove_point](class_curve3d.md#class_Curve3D_method_remove_point) ( idx: [int](class_int.md#class_int) ) |
| [Vector3](class_vector3.md#class_Vector3) | [sample](class_curve3d.md#class_Curve3D_method_sample) ( idx: [int](class_int.md#class_int), t: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [sample_baked](class_curve3d.md#class_Curve3D_method_sample_baked) ( offset: [float](class_float.md#class_float) = 0.0, cubic: [bool](class_bool.md#class_bool) = false ) const |
| [Vector3](class_vector3.md#class_Vector3) | [sample_baked_up_vector](class_curve3d.md#class_Curve3D_method_sample_baked_up_vector) ( offset: [float](class_float.md#class_float), apply_tilt: [bool](class_bool.md#class_bool) = false ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [sample_baked_with_rotation](class_curve3d.md#class_Curve3D_method_sample_baked_with_rotation) ( offset: [float](class_float.md#class_float) = 0.0, cubic: [bool](class_bool.md#class_bool) = false, apply_tilt: [bool](class_bool.md#class_bool) = false ) const |
| [Vector3](class_vector3.md#class_Vector3) | [samplef](class_curve3d.md#class_Curve3D_method_samplef) ( fofs: [float](class_float.md#class_float) ) const |
| void | [set_point_in](class_curve3d.md#class_Curve3D_method_set_point_in) ( idx: [int](class_int.md#class_int), position: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [set_point_out](class_curve3d.md#class_Curve3D_method_set_point_out) ( idx: [int](class_int.md#class_int), position: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [set_point_position](class_curve3d.md#class_Curve3D_method_set_point_position) ( idx: [int](class_int.md#class_int), position: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [set_point_tilt](class_curve3d.md#class_Curve3D_method_set_point_tilt) ( idx: [int](class_int.md#class_int), tilt: [float](class_float.md#class_float) ) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [tessellate](class_curve3d.md#class_Curve3D_method_tessellate) ( max_stages: [int](class_int.md#class_int) = 5, tolerance_degrees: [float](class_float.md#class_float) = 4 ) const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [tessellate_even_length](class_curve3d.md#class_Curve3D_method_tessellate_even_length) ( max_stages: [int](class_int.md#class_int) = 5, tolerance_length: [float](class_float.md#class_float) = 0.2 ) const |

---

### Property Descriptions

<span id="class_Curve3D_property_bake_interval"></span>

[float](class_float.md#class_float) **bake_interval** = `0.2` [🔗](class_curve3d.md#class_Curve3D_property_bake_interval)

- void **set_bake_interval** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_bake_interval** ( )

The distance in meters between two adjacent cached points. Changing it forces the cache to be recomputed the next time the [get_baked_points()](class_curve3d.md#class_Curve3D_method_get_baked_points) or [get_baked_length()](class_curve3d.md#class_Curve3D_method_get_baked_length) function is called. The smaller the distance, the more points in the cache and the more memory it will consume, so use with care.

---

<span id="class_Curve3D_property_closed"></span>

[bool](class_bool.md#class_bool) **closed** = `false` [🔗](class_curve3d.md#class_Curve3D_property_closed)

- void **set_closed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_closed** ( )

If `true`, and the curve has more than 2 control points, the last point and the first one will be connected in a loop.

---

<span id="class_Curve3D_property_point_count"></span>

[int](class_int.md#class_int) **point_count** = `0` [🔗](class_curve3d.md#class_Curve3D_property_point_count)

- void **set_point_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_point_count** ( )

The number of points describing the curve.

---

<span id="class_Curve3D_property_up_vector_enabled"></span>

[bool](class_bool.md#class_bool) **up_vector_enabled** = `true` [🔗](class_curve3d.md#class_Curve3D_property_up_vector_enabled)

- void **set_up_vector_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_up_vector_enabled** ( )

If `true`, the curve will bake up vectors used for orientation. This is used when [PathFollow3D.rotation_mode](class_pathfollow3d.md#class_PathFollow3D_property_rotation_mode) is set to [PathFollow3D.ROTATION_ORIENTED](class_pathfollow3d.md#class_PathFollow3D_constant_ROTATION_ORIENTED). Changing it forces the cache to be recomputed.

---

### Method Descriptions

<span id="class_Curve3D_method_add_point"></span>

void **add_point** ( position: [Vector3](class_vector3.md#class_Vector3), in: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 0, 0), out: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 0, 0), index: [int](class_int.md#class_int) = -1 ) [🔗](class_curve3d.md#class_Curve3D_method_add_point)

Adds a point with the specified `position` relative to the curve's own position, with control points `in` and `out`. Appends the new point at the end of the point list.

If `index` is given, the new point is inserted before the existing point identified by index `index`. Every existing point starting from `index` is shifted further down the list of points. The index must be greater than or equal to `0` and must not exceed the number of existing points in the line. See [point_count](class_curve3d.md#class_Curve3D_property_point_count).

---

<span id="class_Curve3D_method_clear_points"></span>

void **clear_points** ( ) [🔗](class_curve3d.md#class_Curve3D_method_clear_points)

Removes all points from the curve.

---

<span id="class_Curve3D_method_get_baked_length"></span>

[float](class_float.md#class_float) **get_baked_length** ( ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_baked_length)

Returns the total length of the curve, based on the cached points. Given enough density (see [bake_interval](class_curve3d.md#class_Curve3D_property_bake_interval)), it should be approximate enough.

---

<span id="class_Curve3D_method_get_baked_points"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_baked_points** ( ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_baked_points)

Returns the cache of points as a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array).

---

<span id="class_Curve3D_method_get_baked_tilts"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **get_baked_tilts** ( ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_baked_tilts)

Returns the cache of tilts as a [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array).

---

<span id="class_Curve3D_method_get_baked_up_vectors"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_baked_up_vectors** ( ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_baked_up_vectors)

Returns the cache of up vectors as a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array).

If [up_vector_enabled](class_curve3d.md#class_Curve3D_property_up_vector_enabled) is `false`, the cache will be empty.

---

<span id="class_Curve3D_method_get_closest_offset"></span>

[float](class_float.md#class_float) **get_closest_offset** ( to_point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_closest_offset)

Returns the closest offset to `to_point`. This offset is meant to be used in [sample_baked()](class_curve3d.md#class_Curve3D_method_sample_baked) or [sample_baked_up_vector()](class_curve3d.md#class_Curve3D_method_sample_baked_up_vector).

 `to_point` must be in this curve's local space.

---

<span id="class_Curve3D_method_get_closest_point"></span>

[Vector3](class_vector3.md#class_Vector3) **get_closest_point** ( to_point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_closest_point)

Returns the closest point on baked segments (in curve's local space) to `to_point`.

 `to_point` must be in this curve's local space.

---

<span id="class_Curve3D_method_get_point_in"></span>

[Vector3](class_vector3.md#class_Vector3) **get_point_in** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_point_in)

Returns the position of the control point leading to the vertex `idx`. The returned position is relative to the vertex `idx`. If the index is out of bounds, the function sends an error to the console, and returns `(0, 0, 0)`.

---

<span id="class_Curve3D_method_get_point_out"></span>

[Vector3](class_vector3.md#class_Vector3) **get_point_out** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_point_out)

Returns the position of the control point leading out of the vertex `idx`. The returned position is relative to the vertex `idx`. If the index is out of bounds, the function sends an error to the console, and returns `(0, 0, 0)`.

---

<span id="class_Curve3D_method_get_point_position"></span>

[Vector3](class_vector3.md#class_Vector3) **get_point_position** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_point_position)

Returns the position of the vertex `idx`. If the index is out of bounds, the function sends an error to the console, and returns `(0, 0, 0)`.

---

<span id="class_Curve3D_method_get_point_tilt"></span>

[float](class_float.md#class_float) **get_point_tilt** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_curve3d.md#class_Curve3D_method_get_point_tilt)

Returns the tilt angle in radians for the point `idx`. If the index is out of bounds, the function sends an error to the console, and returns `0`.

---

<span id="class_Curve3D_method_remove_point"></span>

void **remove_point** ( idx: [int](class_int.md#class_int) ) [🔗](class_curve3d.md#class_Curve3D_method_remove_point)

Deletes the point `idx` from the curve. Sends an error to the console if `idx` is out of bounds.

---

<span id="class_Curve3D_method_sample"></span>

[Vector3](class_vector3.md#class_Vector3) **sample** ( idx: [int](class_int.md#class_int), t: [float](class_float.md#class_float) ) *const* [🔗](class_curve3d.md#class_Curve3D_method_sample)

Returns the position between the vertex `idx` and the vertex `idx + 1`, where `t` controls if the point is the first vertex (`t = 0.0`), the last vertex (`t = 1.0`), or in between. Values of `t` outside the range (`0.0 >= t <=1`) give strange, but predictable results.

If `idx` is out of bounds it is truncated to the first or last vertex, and `t` is ignored. If the curve has no points, the function sends an error to the console, and returns `(0, 0, 0)`.

---

<span id="class_Curve3D_method_sample_baked"></span>

[Vector3](class_vector3.md#class_Vector3) **sample_baked** ( offset: [float](class_float.md#class_float) = 0.0, cubic: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_curve3d.md#class_Curve3D_method_sample_baked)

Returns a point within the curve at position `offset`, where `offset` is measured as a distance in 3D units along the curve. To do that, it finds the two cached points where the `offset` lies between, then interpolates the values. This interpolation is cubic if `cubic` is set to `true`, or linear if set to `false`.

Cubic interpolation tends to follow the curves better, but linear is faster (and often, precise enough).

---

<span id="class_Curve3D_method_sample_baked_up_vector"></span>

[Vector3](class_vector3.md#class_Vector3) **sample_baked_up_vector** ( offset: [float](class_float.md#class_float), apply_tilt: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_curve3d.md#class_Curve3D_method_sample_baked_up_vector)

Returns an up vector within the curve at position `offset`, where `offset` is measured as a distance in 3D units along the curve. To do that, it finds the two cached up vectors where the `offset` lies between, then interpolates the values. If `apply_tilt` is `true`, an interpolated tilt is applied to the interpolated up vector.

If the curve has no up vectors, the function sends an error to the console, and returns `(0, 1, 0)`.

---

<span id="class_Curve3D_method_sample_baked_with_rotation"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **sample_baked_with_rotation** ( offset: [float](class_float.md#class_float) = 0.0, cubic: [bool](class_bool.md#class_bool) = false, apply_tilt: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_curve3d.md#class_Curve3D_method_sample_baked_with_rotation)

Returns a [Transform3D](class_transform3d.md#class_Transform3D) with `origin` as point position, `basis.x` as sideway vector, `basis.y` as up vector, `basis.z` as forward vector. When the curve length is 0, there is no reasonable way to calculate the rotation, all vectors aligned with global space axes. See also [sample_baked()](class_curve3d.md#class_Curve3D_method_sample_baked).

---

<span id="class_Curve3D_method_samplef"></span>

[Vector3](class_vector3.md#class_Vector3) **samplef** ( fofs: [float](class_float.md#class_float) ) *const* [🔗](class_curve3d.md#class_Curve3D_method_samplef)

Returns the position at the vertex `fofs`. It calls [sample()](class_curve3d.md#class_Curve3D_method_sample) using the integer part of `fofs` as `idx`, and its fractional part as `t`.

---

<span id="class_Curve3D_method_set_point_in"></span>

void **set_point_in** ( idx: [int](class_int.md#class_int), position: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_curve3d.md#class_Curve3D_method_set_point_in)

Sets the position of the control point leading to the vertex `idx`. If the index is out of bounds, the function sends an error to the console. The position is relative to the vertex.

---

<span id="class_Curve3D_method_set_point_out"></span>

void **set_point_out** ( idx: [int](class_int.md#class_int), position: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_curve3d.md#class_Curve3D_method_set_point_out)

Sets the position of the control point leading out of the vertex `idx`. If the index is out of bounds, the function sends an error to the console. The position is relative to the vertex.

---

<span id="class_Curve3D_method_set_point_position"></span>

void **set_point_position** ( idx: [int](class_int.md#class_int), position: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_curve3d.md#class_Curve3D_method_set_point_position)

Sets the position for the vertex `idx`. If the index is out of bounds, the function sends an error to the console.

---

<span id="class_Curve3D_method_set_point_tilt"></span>

void **set_point_tilt** ( idx: [int](class_int.md#class_int), tilt: [float](class_float.md#class_float) ) [🔗](class_curve3d.md#class_Curve3D_method_set_point_tilt)

Sets the tilt angle in radians for the point `idx`. If the index is out of bounds, the function sends an error to the console.

The tilt controls the rotation along the look-at axis an object traveling the path would have. In the case of a curve controlling a [PathFollow3D](class_pathfollow3d.md#class_PathFollow3D), this tilt is an offset over the natural tilt the [PathFollow3D](class_pathfollow3d.md#class_PathFollow3D) calculates.

---

<span id="class_Curve3D_method_tessellate"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **tessellate** ( max_stages: [int](class_int.md#class_int) = 5, tolerance_degrees: [float](class_float.md#class_float) = 4 ) *const* [🔗](class_curve3d.md#class_Curve3D_method_tessellate)

Returns a list of points along the curve, with a curvature controlled point density. That is, the curvier parts will have more points than the straighter parts.

This approximation makes straight segments between each point, then subdivides those segments until the resulting shape is similar enough.

 `max_stages` controls how many subdivisions a curve segment may face before it is considered approximate enough. Each subdivision splits the segment in half, so the default 5 stages may mean up to 32 subdivisions per curve segment. Increase with care!

 `tolerance_degrees` controls how many degrees the midpoint of a segment may deviate from the real curve, before the segment has to be subdivided.

---

<span id="class_Curve3D_method_tessellate_even_length"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **tessellate_even_length** ( max_stages: [int](class_int.md#class_int) = 5, tolerance_length: [float](class_float.md#class_float) = 0.2 ) *const* [🔗](class_curve3d.md#class_Curve3D_method_tessellate_even_length)

Returns a list of points along the curve, with almost uniform density. `max_stages` controls how many subdivisions a curve segment may face before it is considered approximate enough. Each subdivision splits the segment in half, so the default 5 stages may mean up to 32 subdivisions per curve segment. Increase with care!

 `tolerance_length` controls the maximal distance between two neighboring points, before the segment has to be subdivided.
