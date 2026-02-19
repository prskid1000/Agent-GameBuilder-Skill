<span id="class_Plane"></span>

## Plane

A plane in Hessian normal form.

### Description

Represents a normalized plane equation. [normal](class_plane.md#class_Plane_property_normal) is the normal of the plane (a, b, c normalized), and [d](class_plane.md#class_Plane_property_d) is the distance from the origin to the plane (in the direction of "normal"). "Over" or "Above" the plane is considered the side of the plane towards where the normal is pointing.

 **Note:** In a boolean context, a plane will evaluate to `false` if all its components equal `0`. Otherwise, a plane will always evaluate to `true`.

### Tutorials

- [Math documentation index](../tutorials/math/index.md)

### Properties


| [float](class_float.md#class_float) | [d](class_plane.md#class_Plane_property_d) | `0.0` |
| --- | --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [normal](class_plane.md#class_Plane_property_normal) | `Vector3(0, 0, 0)` |
| [float](class_float.md#class_float) | [x](class_plane.md#class_Plane_property_x) | `0.0` |
| [float](class_float.md#class_float) | [y](class_plane.md#class_Plane_property_y) | `0.0` |
| [float](class_float.md#class_float) | [z](class_plane.md#class_Plane_property_z) | `0.0` |

### Constructors


| [Plane](class_plane.md#class_Plane) | [Plane](class_plane.md#class_Plane_constructor_Plane) ( ) |
| --- | --- |
| [Plane](class_plane.md#class_Plane) | [Plane](class_plane.md#class_Plane_constructor_Plane) ( from: [Plane](class_plane.md#class_Plane) ) |
| [Plane](class_plane.md#class_Plane) | [Plane](class_plane.md#class_Plane_constructor_Plane) ( a: [float](class_float.md#class_float), b: [float](class_float.md#class_float), c: [float](class_float.md#class_float), d: [float](class_float.md#class_float) ) |
| [Plane](class_plane.md#class_Plane) | [Plane](class_plane.md#class_Plane_constructor_Plane) ( normal: [Vector3](class_vector3.md#class_Vector3) ) |
| [Plane](class_plane.md#class_Plane) | [Plane](class_plane.md#class_Plane_constructor_Plane) ( normal: [Vector3](class_vector3.md#class_Vector3), d: [float](class_float.md#class_float) ) |
| [Plane](class_plane.md#class_Plane) | [Plane](class_plane.md#class_Plane_constructor_Plane) ( normal: [Vector3](class_vector3.md#class_Vector3), point: [Vector3](class_vector3.md#class_Vector3) ) |
| [Plane](class_plane.md#class_Plane) | [Plane](class_plane.md#class_Plane_constructor_Plane) ( point1: [Vector3](class_vector3.md#class_Vector3), point2: [Vector3](class_vector3.md#class_Vector3), point3: [Vector3](class_vector3.md#class_Vector3) ) |

### Methods


| [float](class_float.md#class_float) | [distance_to](class_plane.md#class_Plane_method_distance_to) ( point: [Vector3](class_vector3.md#class_Vector3) ) const |
| --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [get_center](class_plane.md#class_Plane_method_get_center) ( ) const |
| [bool](class_bool.md#class_bool) | [has_point](class_plane.md#class_Plane_method_has_point) ( point: [Vector3](class_vector3.md#class_Vector3), tolerance: [float](class_float.md#class_float) = 1e-05 ) const |
| [Variant](class_variant.md#class_Variant) | [intersect_3](class_plane.md#class_Plane_method_intersect_3) ( b: [Plane](class_plane.md#class_Plane), c: [Plane](class_plane.md#class_Plane) ) const |
| [Variant](class_variant.md#class_Variant) | [intersects_ray](class_plane.md#class_Plane_method_intersects_ray) ( from: [Vector3](class_vector3.md#class_Vector3), dir: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Variant](class_variant.md#class_Variant) | [intersects_segment](class_plane.md#class_Plane_method_intersects_segment) ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3) ) const |
| [bool](class_bool.md#class_bool) | [is_equal_approx](class_plane.md#class_Plane_method_is_equal_approx) ( to_plane: [Plane](class_plane.md#class_Plane) ) const |
| [bool](class_bool.md#class_bool) | [is_finite](class_plane.md#class_Plane_method_is_finite) ( ) const |
| [bool](class_bool.md#class_bool) | [is_point_over](class_plane.md#class_Plane_method_is_point_over) ( point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Plane](class_plane.md#class_Plane) | [normalized](class_plane.md#class_Plane_method_normalized) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [project](class_plane.md#class_Plane_method_project) ( point: [Vector3](class_vector3.md#class_Vector3) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_plane.md#class_Plane_operator_neq_Plane) ( right: [Plane](class_plane.md#class_Plane) ) |
| --- | --- |
| [Plane](class_plane.md#class_Plane) | [operator *](class_plane.md#class_Plane_operator_mul_Transform3D) ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_plane.md#class_Plane_operator_eq_Plane) ( right: [Plane](class_plane.md#class_Plane) ) |
| [Plane](class_plane.md#class_Plane) | [operator unary+](class_plane.md#class_Plane_operator_unplus) ( ) |
| [Plane](class_plane.md#class_Plane) | [operator unary-](class_plane.md#class_Plane_operator_unminus) ( ) |

---

### Constants

<span id="class_Plane_constant_PLANE_YZ"></span>

**PLANE_YZ** = `Plane(1, 0, 0, 0)` [🔗](class_plane.md#class_Plane_constant_PLANE_YZ)

A plane that extends in the Y and Z axes (normal vector points +X).

<span id="class_Plane_constant_PLANE_XZ"></span>

**PLANE_XZ** = `Plane(0, 1, 0, 0)` [🔗](class_plane.md#class_Plane_constant_PLANE_XZ)

A plane that extends in the X and Z axes (normal vector points +Y).

<span id="class_Plane_constant_PLANE_XY"></span>

**PLANE_XY** = `Plane(0, 0, 1, 0)` [🔗](class_plane.md#class_Plane_constant_PLANE_XY)

A plane that extends in the X and Y axes (normal vector points +Z).

---

### Property Descriptions

<span id="class_Plane_property_d"></span>

[float](class_float.md#class_float) **d** = `0.0` [🔗](class_plane.md#class_Plane_property_d)

The distance from the origin to the plane, expressed in terms of [normal](class_plane.md#class_Plane_property_normal) (according to its direction and magnitude). Actual absolute distance from the origin to the plane can be calculated as `abs(d) / normal.length()` (if [normal](class_plane.md#class_Plane_property_normal) has zero length then this **Plane** does not represent a valid plane).

In the scalar equation of the plane `ax + by + cz = d`, this is `d`, while the `(a, b, c)` coordinates are represented by the [normal](class_plane.md#class_Plane_property_normal) property.

---

<span id="class_Plane_property_normal"></span>

[Vector3](class_vector3.md#class_Vector3) **normal** = `Vector3(0, 0, 0)` [🔗](class_plane.md#class_Plane_property_normal)

The normal of the plane, typically a unit vector. Shouldn't be a zero vector as **Plane** with such [normal](class_plane.md#class_Plane_property_normal) does not represent a valid plane.

In the scalar equation of the plane `ax + by + cz = d`, this is the vector `(a, b, c)`, where `d` is the [d](class_plane.md#class_Plane_property_d) property.

---

<span id="class_Plane_property_x"></span>

[float](class_float.md#class_float) **x** = `0.0` [🔗](class_plane.md#class_Plane_property_x)

The X component of the plane's [normal](class_plane.md#class_Plane_property_normal) vector.

---

<span id="class_Plane_property_y"></span>

[float](class_float.md#class_float) **y** = `0.0` [🔗](class_plane.md#class_Plane_property_y)

The Y component of the plane's [normal](class_plane.md#class_Plane_property_normal) vector.

---

<span id="class_Plane_property_z"></span>

[float](class_float.md#class_float) **z** = `0.0` [🔗](class_plane.md#class_Plane_property_z)

The Z component of the plane's [normal](class_plane.md#class_Plane_property_normal) vector.

---

### Constructor Descriptions

<span id="class_Plane_constructor_Plane"></span>

[Plane](class_plane.md#class_Plane) **Plane** ( ) [🔗](class_plane.md#class_Plane_constructor_Plane)

Constructs a default-initialized **Plane** with all components set to `0`.

---

[Plane](class_plane.md#class_Plane) **Plane** ( from: [Plane](class_plane.md#class_Plane) )

Constructs a **Plane** as a copy of the given **Plane**.

---

[Plane](class_plane.md#class_Plane) **Plane** ( a: [float](class_float.md#class_float), b: [float](class_float.md#class_float), c: [float](class_float.md#class_float), d: [float](class_float.md#class_float) )

Creates a plane from the four parameters. The three components of the resulting plane's [normal](class_plane.md#class_Plane_property_normal) are `a`, `b` and `c`, and the plane has a distance of `d` from the origin.

---

[Plane](class_plane.md#class_Plane) **Plane** ( normal: [Vector3](class_vector3.md#class_Vector3) )

Creates a plane from the normal vector. The plane will intersect the origin.

The `normal` of the plane must be a unit vector.

---

[Plane](class_plane.md#class_Plane) **Plane** ( normal: [Vector3](class_vector3.md#class_Vector3), d: [float](class_float.md#class_float) )

Creates a plane from the normal vector and the plane's distance from the origin.

The `normal` of the plane must be a unit vector.

---

[Plane](class_plane.md#class_Plane) **Plane** ( normal: [Vector3](class_vector3.md#class_Vector3), point: [Vector3](class_vector3.md#class_Vector3) )

Creates a plane from the normal vector and a point on the plane.

The `normal` of the plane must be a unit vector.

---

[Plane](class_plane.md#class_Plane) **Plane** ( point1: [Vector3](class_vector3.md#class_Vector3), point2: [Vector3](class_vector3.md#class_Vector3), point3: [Vector3](class_vector3.md#class_Vector3) )

Creates a plane from the three points, given in clockwise order.

---

### Method Descriptions

<span id="class_Plane_method_distance_to"></span>

[float](class_float.md#class_float) **distance_to** ( point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_plane.md#class_Plane_method_distance_to)

Returns the shortest distance from the plane to the position `point`. If the point is above the plane, the distance will be positive. If below, the distance will be negative.

---

<span id="class_Plane_method_get_center"></span>

[Vector3](class_vector3.md#class_Vector3) **get_center** ( ) *const* [🔗](class_plane.md#class_Plane_method_get_center)

Returns the center of the plane.

---

<span id="class_Plane_method_has_point"></span>

[bool](class_bool.md#class_bool) **has_point** ( point: [Vector3](class_vector3.md#class_Vector3), tolerance: [float](class_float.md#class_float) = 1e-05 ) *const* [🔗](class_plane.md#class_Plane_method_has_point)

Returns `true` if `point` is inside the plane. Comparison uses a custom minimum `tolerance` threshold.

---

<span id="class_Plane_method_intersect_3"></span>

[Variant](class_variant.md#class_Variant) **intersect_3** ( b: [Plane](class_plane.md#class_Plane), c: [Plane](class_plane.md#class_Plane) ) *const* [🔗](class_plane.md#class_Plane_method_intersect_3)

Returns the intersection point of the three planes `b`, `c` and this plane. If no intersection is found, `null` is returned.

---

<span id="class_Plane_method_intersects_ray"></span>

[Variant](class_variant.md#class_Variant) **intersects_ray** ( from: [Vector3](class_vector3.md#class_Vector3), dir: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_plane.md#class_Plane_method_intersects_ray)

Returns the intersection point of a ray consisting of the position `from` and the direction normal `dir` with this plane. If no intersection is found, `null` is returned.

---

<span id="class_Plane_method_intersects_segment"></span>

[Variant](class_variant.md#class_Variant) **intersects_segment** ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_plane.md#class_Plane_method_intersects_segment)

Returns the intersection point of a segment from position `from` to position `to` with this plane. If no intersection is found, `null` is returned.

---

<span id="class_Plane_method_is_equal_approx"></span>

[bool](class_bool.md#class_bool) **is_equal_approx** ( to_plane: [Plane](class_plane.md#class_Plane) ) *const* [🔗](class_plane.md#class_Plane_method_is_equal_approx)

Returns `true` if this plane and `to_plane` are approximately equal, by running @GlobalScope.is_equal_approx() on each component.

---

<span id="class_Plane_method_is_finite"></span>

[bool](class_bool.md#class_bool) **is_finite** ( ) *const* [🔗](class_plane.md#class_Plane_method_is_finite)

Returns `true` if this plane is finite, by calling @GlobalScope.is_finite() on each component.

---

<span id="class_Plane_method_is_point_over"></span>

[bool](class_bool.md#class_bool) **is_point_over** ( point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_plane.md#class_Plane_method_is_point_over)

Returns `true` if `point` is located above the plane.

---

<span id="class_Plane_method_normalized"></span>

[Plane](class_plane.md#class_Plane) **normalized** ( ) *const* [🔗](class_plane.md#class_Plane_method_normalized)

Returns a copy of the plane, with normalized [normal](class_plane.md#class_Plane_property_normal) (so it's a unit vector). Returns `Plane(0, 0, 0, 0)` if [normal](class_plane.md#class_Plane_property_normal) can't be normalized (it has zero length).

---

<span id="class_Plane_method_project"></span>

[Vector3](class_vector3.md#class_Vector3) **project** ( point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_plane.md#class_Plane_method_project)

Returns the orthogonal projection of `point` into a point in the plane.

---

### Operator Descriptions

<span id="class_Plane_operator_neq_Plane"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Plane](class_plane.md#class_Plane) ) [🔗](class_plane.md#class_Plane_operator_neq_Plane)

Returns `true` if the planes are not equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_plane.md#class_Plane_method_is_equal_approx) instead, which is more reliable.

---

<span id="class_Plane_operator_mul_Transform3D"></span>

[Plane](class_plane.md#class_Plane) **operator *** ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_plane.md#class_Plane_operator_mul_Transform3D)

Inversely transforms (multiplies) the **Plane** by the given [Transform3D](class_transform3d.md#class_Transform3D) transformation matrix.

 `plane * transform` is equivalent to `transform.affine_inverse() * plane`. See [Transform3D.affine_inverse()](class_transform3d.md#class_Transform3D_method_affine_inverse).

---

<span id="class_Plane_operator_eq_Plane"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Plane](class_plane.md#class_Plane) ) [🔗](class_plane.md#class_Plane_operator_eq_Plane)

Returns `true` if the planes are exactly equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_plane.md#class_Plane_method_is_equal_approx) instead, which is more reliable.

---

<span id="class_Plane_operator_unplus"></span>

[Plane](class_plane.md#class_Plane) **operator unary+** ( ) [🔗](class_plane.md#class_Plane_operator_unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

<span id="class_Plane_operator_unminus"></span>

[Plane](class_plane.md#class_Plane) **operator unary-** ( ) [🔗](class_plane.md#class_Plane_operator_unminus)

Returns the negative value of the **Plane**. This is the same as writing `Plane(-p.normal, -p.d)`. This operation flips the direction of the normal vector and also flips the distance value, resulting in a Plane that is in the same place, but facing the opposite direction.
