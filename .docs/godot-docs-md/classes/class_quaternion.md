<span id="class_Quaternion"></span>

## Quaternion

A unit quaternion used for representing 3D rotations.

### Description

The **Quaternion** built-in [Variant](class_variant.md#class_Variant) type is a 4D data structure that represents rotation in the form of a Hamilton convention quaternion. Compared to the [Basis](class_basis.md#class_Basis) type which can store both rotation and scale, quaternions can *only* store rotation.

A **Quaternion** is composed by 4 floating-point components: [w](class_quaternion.md#class_Quaternion_property_w), [x](class_quaternion.md#class_Quaternion_property_x), [y](class_quaternion.md#class_Quaternion_property_y), and [z](class_quaternion.md#class_Quaternion_property_z). These components are very compact in memory, and because of this some operations are more efficient and less likely to cause floating-point errors. Methods such as [get_angle()](class_quaternion.md#class_Quaternion_method_get_angle), [get_axis()](class_quaternion.md#class_Quaternion_method_get_axis), and [slerp()](class_quaternion.md#class_Quaternion_method_slerp) are faster than their [Basis](class_basis.md#class_Basis) counterparts.

For a great introduction to quaternions, see this video by 3Blue1Brown. You do not need to know the math behind quaternions, as Godot provides several helper methods that handle it for you. These include [slerp()](class_quaternion.md#class_Quaternion_method_slerp) and [spherical_cubic_interpolate()](class_quaternion.md#class_Quaternion_method_spherical_cubic_interpolate), as well as the `*` operator.

 **Note:** Quaternions must be normalized before being used for rotation (see [normalized()](class_quaternion.md#class_Quaternion_method_normalized)).

 **Note:** Similarly to [Vector2](class_vector2.md#class_Vector2) and [Vector3](class_vector3.md#class_Vector3), the components of a quaternion use 32-bit precision by default, unlike [float](class_float.md#class_float) which is always 64-bit. If double precision is needed, compile the engine with the option `precision=double`.

 **Note:** In a boolean context, a quaternion will evaluate to `false` if it's equal to [IDENTITY](class_quaternion.md#class_Quaternion_constant_IDENTITY). Otherwise, a quaternion will always evaluate to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Tutorials

- 3Blue1Brown's video on Quaternions

- Online Quaternion Visualization

- `Using 3D transforms <../tutorials/3d/using_transforms.html#interpolating-with-quaternions>`__

- Third Person Shooter (TPS) Demo

- Advanced Quaternion Visualization

### Properties


| [float](class_float.md#class_float) | [w](class_quaternion.md#class_Quaternion_property_w) | `1.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [x](class_quaternion.md#class_Quaternion_property_x) | `0.0` |
| [float](class_float.md#class_float) | [y](class_quaternion.md#class_Quaternion_property_y) | `0.0` |
| [float](class_float.md#class_float) | [z](class_quaternion.md#class_Quaternion_property_z) | `0.0` |

### Constructors


| [Quaternion](class_quaternion.md#class_Quaternion) | [Quaternion](class_quaternion.md#class_Quaternion_constructor_Quaternion) ( ) |
| --- | --- |
| [Quaternion](class_quaternion.md#class_Quaternion) | [Quaternion](class_quaternion.md#class_Quaternion_constructor_Quaternion) ( from: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [Quaternion](class_quaternion.md#class_Quaternion_constructor_Quaternion) ( arc_from: [Vector3](class_vector3.md#class_Vector3), arc_to: [Vector3](class_vector3.md#class_Vector3) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [Quaternion](class_quaternion.md#class_Quaternion_constructor_Quaternion) ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [Quaternion](class_quaternion.md#class_Quaternion_constructor_Quaternion) ( from: [Basis](class_basis.md#class_Basis) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [Quaternion](class_quaternion.md#class_Quaternion_constructor_Quaternion) ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), z: [float](class_float.md#class_float), w: [float](class_float.md#class_float) ) |

### Methods


| [float](class_float.md#class_float) | [angle_to](class_quaternion.md#class_Quaternion_method_angle_to) ( to: [Quaternion](class_quaternion.md#class_Quaternion) ) const |
| --- | --- |
| [float](class_float.md#class_float) | [dot](class_quaternion.md#class_Quaternion_method_dot) ( with: [Quaternion](class_quaternion.md#class_Quaternion) ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [exp](class_quaternion.md#class_Quaternion_method_exp) ( ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [from_euler](class_quaternion.md#class_Quaternion_method_from_euler) ( euler: [Vector3](class_vector3.md#class_Vector3) ) static |
| [float](class_float.md#class_float) | [get_angle](class_quaternion.md#class_Quaternion_method_get_angle) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_axis](class_quaternion.md#class_Quaternion_method_get_axis) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_euler](class_quaternion.md#class_Quaternion_method_get_euler) ( order: [int](class_int.md#class_int) = 2 ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [inverse](class_quaternion.md#class_Quaternion_method_inverse) ( ) const |
| [bool](class_bool.md#class_bool) | [is_equal_approx](class_quaternion.md#class_Quaternion_method_is_equal_approx) ( to: [Quaternion](class_quaternion.md#class_Quaternion) ) const |
| [bool](class_bool.md#class_bool) | [is_finite](class_quaternion.md#class_Quaternion_method_is_finite) ( ) const |
| [bool](class_bool.md#class_bool) | [is_normalized](class_quaternion.md#class_Quaternion_method_is_normalized) ( ) const |
| [float](class_float.md#class_float) | [length](class_quaternion.md#class_Quaternion_method_length) ( ) const |
| [float](class_float.md#class_float) | [length_squared](class_quaternion.md#class_Quaternion_method_length_squared) ( ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [log](class_quaternion.md#class_Quaternion_method_log) ( ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [normalized](class_quaternion.md#class_Quaternion_method_normalized) ( ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [slerp](class_quaternion.md#class_Quaternion_method_slerp) ( to: [Quaternion](class_quaternion.md#class_Quaternion), weight: [float](class_float.md#class_float) ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [slerpni](class_quaternion.md#class_Quaternion_method_slerpni) ( to: [Quaternion](class_quaternion.md#class_Quaternion), weight: [float](class_float.md#class_float) ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [spherical_cubic_interpolate](class_quaternion.md#class_Quaternion_method_spherical_cubic_interpolate) ( b: [Quaternion](class_quaternion.md#class_Quaternion), pre_a: [Quaternion](class_quaternion.md#class_Quaternion), post_b: [Quaternion](class_quaternion.md#class_Quaternion), weight: [float](class_float.md#class_float) ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [spherical_cubic_interpolate_in_time](class_quaternion.md#class_Quaternion_method_spherical_cubic_interpolate_in_time) ( b: [Quaternion](class_quaternion.md#class_Quaternion), pre_a: [Quaternion](class_quaternion.md#class_Quaternion), post_b: [Quaternion](class_quaternion.md#class_Quaternion), weight: [float](class_float.md#class_float), b_t: [float](class_float.md#class_float), pre_a_t: [float](class_float.md#class_float), post_b_t: [float](class_float.md#class_float) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_quaternion.md#class_Quaternion_operator_neq_Quaternion) ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| --- | --- |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator *](class_quaternion.md#class_Quaternion_operator_mul_Quaternion) ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_quaternion.md#class_Quaternion_operator_mul_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator *](class_quaternion.md#class_Quaternion_operator_mul_float) ( right: [float](class_float.md#class_float) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator *](class_quaternion.md#class_Quaternion_operator_mul_int) ( right: [int](class_int.md#class_int) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator +](class_quaternion.md#class_Quaternion_operator_sum_Quaternion) ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator -](class_quaternion.md#class_Quaternion_operator_dif_Quaternion) ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator /](class_quaternion.md#class_Quaternion_operator_div_float) ( right: [float](class_float.md#class_float) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator /](class_quaternion.md#class_Quaternion_operator_div_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_quaternion.md#class_Quaternion_operator_eq_Quaternion) ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| [float](class_float.md#class_float) | [operator []](class_quaternion.md#class_Quaternion_operator_idx_int) ( index: [int](class_int.md#class_int) ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator unary+](class_quaternion.md#class_Quaternion_operator_unplus) ( ) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [operator unary-](class_quaternion.md#class_Quaternion_operator_unminus) ( ) |

---

### Constants

<span id="class_Quaternion_constant_IDENTITY"></span>

**IDENTITY** = `Quaternion(0, 0, 0, 1)` [🔗](class_quaternion.md#class_Quaternion_constant_IDENTITY)

The identity quaternion, representing no rotation. This has the same rotation as [Basis.IDENTITY](class_basis.md#class_Basis_constant_IDENTITY).

If a [Vector3](class_vector3.md#class_Vector3) is rotated (multiplied) by this quaternion, it does not change.

 **Note:** In GDScript, this constant is equivalent to creating a [Quaternion](class_quaternion.md#class_Quaternion_constructor_Quaternion) without any arguments. It can be used to make your code clearer, and for consistency with C#.

---

### Property Descriptions

<span id="class_Quaternion_property_w"></span>

[float](class_float.md#class_float) **w** = `1.0` [🔗](class_quaternion.md#class_Quaternion_property_w)

W component of the quaternion. This is the "real" part.

 **Note:** Quaternion components should usually not be manipulated directly.

---

<span id="class_Quaternion_property_x"></span>

[float](class_float.md#class_float) **x** = `0.0` [🔗](class_quaternion.md#class_Quaternion_property_x)

X component of the quaternion. This is the value along the "imaginary" `i` axis.

 **Note:** Quaternion components should usually not be manipulated directly.

---

<span id="class_Quaternion_property_y"></span>

[float](class_float.md#class_float) **y** = `0.0` [🔗](class_quaternion.md#class_Quaternion_property_y)

Y component of the quaternion. This is the value along the "imaginary" `j` axis.

 **Note:** Quaternion components should usually not be manipulated directly.

---

<span id="class_Quaternion_property_z"></span>

[float](class_float.md#class_float) **z** = `0.0` [🔗](class_quaternion.md#class_Quaternion_property_z)

Z component of the quaternion. This is the value along the "imaginary" `k` axis.

 **Note:** Quaternion components should usually not be manipulated directly.

---

### Constructor Descriptions

<span id="class_Quaternion_constructor_Quaternion"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **Quaternion** ( ) [🔗](class_quaternion.md#class_Quaternion_constructor_Quaternion)

Constructs a **Quaternion** identical to [IDENTITY](class_quaternion.md#class_Quaternion_constant_IDENTITY).

 **Note:** In C#, this constructs a **Quaternion** with all of its components set to `0.0`.

---

[Quaternion](class_quaternion.md#class_Quaternion) **Quaternion** ( from: [Quaternion](class_quaternion.md#class_Quaternion) )

Constructs a **Quaternion** as a copy of the given **Quaternion**.

---

[Quaternion](class_quaternion.md#class_Quaternion) **Quaternion** ( arc_from: [Vector3](class_vector3.md#class_Vector3), arc_to: [Vector3](class_vector3.md#class_Vector3) )

Constructs a **Quaternion** representing the shortest arc between `arc_from` and `arc_to`. These can be imagined as two points intersecting a sphere's surface, with a radius of `1.0`.

---

[Quaternion](class_quaternion.md#class_Quaternion) **Quaternion** ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) )

Constructs a **Quaternion** representing rotation around the `axis` by the given `angle`, in radians. The axis must be a normalized vector.

---

[Quaternion](class_quaternion.md#class_Quaternion) **Quaternion** ( from: [Basis](class_basis.md#class_Basis) )

Constructs a **Quaternion** from the given rotation [Basis](class_basis.md#class_Basis).

This constructor is faster than [Basis.get_rotation_quaternion()](class_basis.md#class_Basis_method_get_rotation_quaternion), but the given basis must be *orthonormalized* (see [Basis.orthonormalized()](class_basis.md#class_Basis_method_orthonormalized)). Otherwise, the constructor fails and returns [IDENTITY](class_quaternion.md#class_Quaternion_constant_IDENTITY).

---

[Quaternion](class_quaternion.md#class_Quaternion) **Quaternion** ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), z: [float](class_float.md#class_float), w: [float](class_float.md#class_float) )

Constructs a **Quaternion** defined by the given values.

 **Note:** Only normalized quaternions represent rotation; if these values are not normalized, the new **Quaternion** will not be a valid rotation.

---

### Method Descriptions

<span id="class_Quaternion_method_angle_to"></span>

[float](class_float.md#class_float) **angle_to** ( to: [Quaternion](class_quaternion.md#class_Quaternion) ) *const* [🔗](class_quaternion.md#class_Quaternion_method_angle_to)

Returns the angle between this quaternion and `to`. This is the magnitude of the angle you would need to rotate by to get from one to the other.

 **Note:** The magnitude of the floating-point error for this method is abnormally high, so methods such as `is_zero_approx` will not work reliably.

---

<span id="class_Quaternion_method_dot"></span>

[float](class_float.md#class_float) **dot** ( with: [Quaternion](class_quaternion.md#class_Quaternion) ) *const* [🔗](class_quaternion.md#class_Quaternion_method_dot)

Returns the dot product between this quaternion and `with`.

This is equivalent to `(quat.x * with.x) + (quat.y * with.y) + (quat.z * with.z) + (quat.w * with.w)`.

---

<span id="class_Quaternion_method_exp"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **exp** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_exp)

Returns the exponential of this quaternion. The rotation axis of the result is the normalized rotation axis of this quaternion, the angle of the result is the length of the vector part of this quaternion.

---

<span id="class_Quaternion_method_from_euler"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **from_euler** ( euler: [Vector3](class_vector3.md#class_Vector3) ) *static* [🔗](class_quaternion.md#class_Quaternion_method_from_euler)

Constructs a new **Quaternion** from the given [Vector3](class_vector3.md#class_Vector3) of Euler angles, in radians. This method always uses the YXZ convention (@GlobalScope.EULER_ORDER_YXZ).

---

<span id="class_Quaternion_method_get_angle"></span>

[float](class_float.md#class_float) **get_angle** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_get_angle)

Returns the angle of the rotation represented by this quaternion.

 **Note:** The quaternion must be normalized.

---

<span id="class_Quaternion_method_get_axis"></span>

[Vector3](class_vector3.md#class_Vector3) **get_axis** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_get_axis)

Returns the rotation axis of the rotation represented by this quaternion.

---

<span id="class_Quaternion_method_get_euler"></span>

[Vector3](class_vector3.md#class_Vector3) **get_euler** ( order: [int](class_int.md#class_int) = 2 ) *const* [🔗](class_quaternion.md#class_Quaternion_method_get_euler)

Returns this quaternion's rotation as a [Vector3](class_vector3.md#class_Vector3) of Euler angles, in radians.

The order of each consecutive rotation can be changed with `order` (see EulerOrder constants). By default, the YXZ convention is used (@GlobalScope.EULER_ORDER_YXZ): Z (roll) is calculated first, then X (pitch), and lastly Y (yaw). When using the opposite method [from_euler()](class_quaternion.md#class_Quaternion_method_from_euler), this order is reversed.

---

<span id="class_Quaternion_method_inverse"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **inverse** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_inverse)

Returns the inverse version of this quaternion, inverting the sign of every component except [w](class_quaternion.md#class_Quaternion_property_w).

---

<span id="class_Quaternion_method_is_equal_approx"></span>

[bool](class_bool.md#class_bool) **is_equal_approx** ( to: [Quaternion](class_quaternion.md#class_Quaternion) ) *const* [🔗](class_quaternion.md#class_Quaternion_method_is_equal_approx)

Returns `true` if this quaternion and `to` are approximately equal, by calling @GlobalScope.is_equal_approx() on each component.

---

<span id="class_Quaternion_method_is_finite"></span>

[bool](class_bool.md#class_bool) **is_finite** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_is_finite)

Returns `true` if this quaternion is finite, by calling @GlobalScope.is_finite() on each component.

---

<span id="class_Quaternion_method_is_normalized"></span>

[bool](class_bool.md#class_bool) **is_normalized** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_is_normalized)

Returns `true` if this quaternion is normalized. See also [normalized()](class_quaternion.md#class_Quaternion_method_normalized).

---

<span id="class_Quaternion_method_length"></span>

[float](class_float.md#class_float) **length** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_length)

Returns this quaternion's length, also called magnitude.

---

<span id="class_Quaternion_method_length_squared"></span>

[float](class_float.md#class_float) **length_squared** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_length_squared)

Returns this quaternion's length, squared.

 **Note:** This method is faster than [length()](class_quaternion.md#class_Quaternion_method_length), so prefer it if you only need to compare quaternion lengths.

---

<span id="class_Quaternion_method_log"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **log** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_log)

Returns the logarithm of this quaternion. Multiplies this quaternion's rotation axis by its rotation angle, and stores the result in the returned quaternion's vector part ([x](class_quaternion.md#class_Quaternion_property_x), [y](class_quaternion.md#class_Quaternion_property_y), and [z](class_quaternion.md#class_Quaternion_property_z)). The returned quaternion's real part ([w](class_quaternion.md#class_Quaternion_property_w)) is always `0.0`.

---

<span id="class_Quaternion_method_normalized"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **normalized** ( ) *const* [🔗](class_quaternion.md#class_Quaternion_method_normalized)

Returns a copy of this quaternion, normalized so that its length is `1.0`. See also [is_normalized()](class_quaternion.md#class_Quaternion_method_is_normalized).

---

<span id="class_Quaternion_method_slerp"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **slerp** ( to: [Quaternion](class_quaternion.md#class_Quaternion), weight: [float](class_float.md#class_float) ) *const* [🔗](class_quaternion.md#class_Quaternion_method_slerp)

Performs a spherical-linear interpolation with the `to` quaternion, given a `weight` and returns the result. Both this quaternion and `to` must be normalized.

---

<span id="class_Quaternion_method_slerpni"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **slerpni** ( to: [Quaternion](class_quaternion.md#class_Quaternion), weight: [float](class_float.md#class_float) ) *const* [🔗](class_quaternion.md#class_Quaternion_method_slerpni)

Performs a spherical-linear interpolation with the `to` quaternion, given a `weight` and returns the result. Unlike [slerp()](class_quaternion.md#class_Quaternion_method_slerp), this method does not check if the rotation path is smaller than 90 degrees. Both this quaternion and `to` must be normalized.

---

<span id="class_Quaternion_method_spherical_cubic_interpolate"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **spherical_cubic_interpolate** ( b: [Quaternion](class_quaternion.md#class_Quaternion), pre_a: [Quaternion](class_quaternion.md#class_Quaternion), post_b: [Quaternion](class_quaternion.md#class_Quaternion), weight: [float](class_float.md#class_float) ) *const* [🔗](class_quaternion.md#class_Quaternion_method_spherical_cubic_interpolate)

Performs a spherical cubic interpolation between quaternions `pre_a`, this vector, `b`, and `post_b`, by the given amount `weight`.

---

<span id="class_Quaternion_method_spherical_cubic_interpolate_in_time"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **spherical_cubic_interpolate_in_time** ( b: [Quaternion](class_quaternion.md#class_Quaternion), pre_a: [Quaternion](class_quaternion.md#class_Quaternion), post_b: [Quaternion](class_quaternion.md#class_Quaternion), weight: [float](class_float.md#class_float), b_t: [float](class_float.md#class_float), pre_a_t: [float](class_float.md#class_float), post_b_t: [float](class_float.md#class_float) ) *const* [🔗](class_quaternion.md#class_Quaternion_method_spherical_cubic_interpolate_in_time)

Performs a spherical cubic interpolation between quaternions `pre_a`, this vector, `b`, and `post_b`, by the given amount `weight`.

It can perform smoother interpolation than [spherical_cubic_interpolate()](class_quaternion.md#class_Quaternion_method_spherical_cubic_interpolate) by the time values.

---

### Operator Descriptions

<span id="class_Quaternion_operator_neq_Quaternion"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) [🔗](class_quaternion.md#class_Quaternion_operator_neq_Quaternion)

Returns `true` if the components of both quaternions are not exactly equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_quaternion.md#class_Quaternion_method_is_equal_approx) instead, which is more reliable.

---

<span id="class_Quaternion_operator_mul_Quaternion"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator *** ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) [🔗](class_quaternion.md#class_Quaternion_operator_mul_Quaternion)

Composes (multiplies) two quaternions. This rotates the `right` quaternion (the child) by this quaternion (the parent).

---

<span id="class_Quaternion_operator_mul_Vector3"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_quaternion.md#class_Quaternion_operator_mul_Vector3)

Rotates (multiplies) the `right` vector by this quaternion, returning a [Vector3](class_vector3.md#class_Vector3).

---

<span id="class_Quaternion_operator_mul_float"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator *** ( right: [float](class_float.md#class_float) ) [🔗](class_quaternion.md#class_Quaternion_operator_mul_float)

Multiplies each component of the **Quaternion** by the right [float](class_float.md#class_float) value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---

<span id="class_Quaternion_operator_mul_int"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator *** ( right: [int](class_int.md#class_int) ) [🔗](class_quaternion.md#class_Quaternion_operator_mul_int)

Multiplies each component of the **Quaternion** by the right [int](class_int.md#class_int) value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---

<span id="class_Quaternion_operator_sum_Quaternion"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator +** ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) [🔗](class_quaternion.md#class_Quaternion_operator_sum_Quaternion)

Adds each component of the left **Quaternion** to the right **Quaternion**.

This operation is not meaningful on its own, but it can be used as a part of a larger expression, such as approximating an intermediate rotation between two nearby rotations.

---

<span id="class_Quaternion_operator_dif_Quaternion"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator -** ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) [🔗](class_quaternion.md#class_Quaternion_operator_dif_Quaternion)

Subtracts each component of the left **Quaternion** by the right **Quaternion**.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---

<span id="class_Quaternion_operator_div_float"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator /** ( right: [float](class_float.md#class_float) ) [🔗](class_quaternion.md#class_Quaternion_operator_div_float)

Divides each component of the **Quaternion** by the right [float](class_float.md#class_float) value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---

<span id="class_Quaternion_operator_div_int"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator /** ( right: [int](class_int.md#class_int) ) [🔗](class_quaternion.md#class_Quaternion_operator_div_int)

Divides each component of the **Quaternion** by the right [int](class_int.md#class_int) value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

---

<span id="class_Quaternion_operator_eq_Quaternion"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) [🔗](class_quaternion.md#class_Quaternion_operator_eq_Quaternion)

Returns `true` if the components of both quaternions are exactly equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_quaternion.md#class_Quaternion_method_is_equal_approx) instead, which is more reliable.

---

<span id="class_Quaternion_operator_idx_int"></span>

[float](class_float.md#class_float) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_quaternion.md#class_Quaternion_operator_idx_int)

Accesses each component of this quaternion by their index.

Index `0` is the same as [x](class_quaternion.md#class_Quaternion_property_x), index `1` is the same as [y](class_quaternion.md#class_Quaternion_property_y), index `2` is the same as [z](class_quaternion.md#class_Quaternion_property_z), and index `3` is the same as [w](class_quaternion.md#class_Quaternion_property_w).

---

<span id="class_Quaternion_operator_unplus"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator unary+** ( ) [🔗](class_quaternion.md#class_Quaternion_operator_unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

<span id="class_Quaternion_operator_unminus"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **operator unary-** ( ) [🔗](class_quaternion.md#class_Quaternion_operator_unminus)

Returns the negative value of the **Quaternion**. This is the same as multiplying all components by `-1`. This operation results in a quaternion that represents the same rotation.
