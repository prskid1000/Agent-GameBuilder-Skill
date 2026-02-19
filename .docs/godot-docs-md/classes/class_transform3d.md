<span id="class_Transform3D"></span>

## Transform3D

A 3×4 matrix representing a 3D transformation.

### Description

The **Transform3D** built-in [Variant](class_variant.md#class_Variant) type is a 3×4 matrix representing a transformation in 3D space. It contains a [Basis](class_basis.md#class_Basis), which on its own can represent rotation, scale, and shear. Additionally, combined with its own [origin](class_transform3d.md#class_Transform3D_property_origin), the transform can also represent a translation.

For a general introduction, see the [Matrices and transforms](../tutorials/math/matrices_and_transforms.md) tutorial.

 **Note:** Godot uses a right-handed coordinate system, which is a common standard. For directions, the convention for built-in types like [Camera3D](class_camera3d.md#class_Camera3D) is for -Z to point forward (+X is right, +Y is up, and +Z is back). Other objects may use different direction conventions. For more information, see the `3D asset direction conventions <../tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html#d-asset-direction-conventions>`__ tutorial.

 **Note:** In a boolean context, a Transform3D will evaluate to `false` if it's equal to [IDENTITY](class_transform3d.md#class_Transform3D_constant_IDENTITY). Otherwise, a Transform3D will always evaluate to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Tutorials

- [Math documentation index](../tutorials/math/index.md)

- [Matrices and transforms](../tutorials/math/matrices_and_transforms.md)

- [Using 3D transforms](../tutorials/3d/using_transforms.md)

- Matrix Transform Demo

- 3D Platformer Demo

- 2.5D Game Demo

### Properties


| [Basis](class_basis.md#class_Basis) | [basis](class_transform3d.md#class_Transform3D_property_basis) | `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)` |
| --- | --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [origin](class_transform3d.md#class_Transform3D_property_origin) | `Vector3(0, 0, 0)` |

### Constructors


| [Transform3D](class_transform3d.md#class_Transform3D) | [Transform3D](class_transform3d.md#class_Transform3D_constructor_Transform3D) ( ) |
| --- | --- |
| [Transform3D](class_transform3d.md#class_Transform3D) | [Transform3D](class_transform3d.md#class_Transform3D_constructor_Transform3D) ( from: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [Transform3D](class_transform3d.md#class_Transform3D_constructor_Transform3D) ( basis: [Basis](class_basis.md#class_Basis), origin: [Vector3](class_vector3.md#class_Vector3) ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [Transform3D](class_transform3d.md#class_Transform3D_constructor_Transform3D) ( from: [Projection](class_projection.md#class_Projection) ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [Transform3D](class_transform3d.md#class_Transform3D_constructor_Transform3D) ( x_axis: [Vector3](class_vector3.md#class_Vector3), y_axis: [Vector3](class_vector3.md#class_Vector3), z_axis: [Vector3](class_vector3.md#class_Vector3), origin: [Vector3](class_vector3.md#class_Vector3) ) |

### Methods


| [Transform3D](class_transform3d.md#class_Transform3D) | [affine_inverse](class_transform3d.md#class_Transform3D_method_affine_inverse) ( ) const |
| --- | --- |
| [Transform3D](class_transform3d.md#class_Transform3D) | [interpolate_with](class_transform3d.md#class_Transform3D_method_interpolate_with) ( xform: [Transform3D](class_transform3d.md#class_Transform3D), weight: [float](class_float.md#class_float) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [inverse](class_transform3d.md#class_Transform3D_method_inverse) ( ) const |
| [bool](class_bool.md#class_bool) | [is_equal_approx](class_transform3d.md#class_Transform3D_method_is_equal_approx) ( xform: [Transform3D](class_transform3d.md#class_Transform3D) ) const |
| [bool](class_bool.md#class_bool) | [is_finite](class_transform3d.md#class_Transform3D_method_is_finite) ( ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [looking_at](class_transform3d.md#class_Transform3D_method_looking_at) ( target: [Vector3](class_vector3.md#class_Vector3), up: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class_bool) = false ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [orthonormalized](class_transform3d.md#class_Transform3D_method_orthonormalized) ( ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [rotated](class_transform3d.md#class_Transform3D_method_rotated) ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [rotated_local](class_transform3d.md#class_Transform3D_method_rotated_local) ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [scaled](class_transform3d.md#class_Transform3D_method_scaled) ( scale: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [scaled_local](class_transform3d.md#class_Transform3D_method_scaled_local) ( scale: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [translated](class_transform3d.md#class_Transform3D_method_translated) ( offset: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [translated_local](class_transform3d.md#class_Transform3D_method_translated_local) ( offset: [Vector3](class_vector3.md#class_Vector3) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_transform3d.md#class_Transform3D_operator_neq_Transform3D) ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| --- | --- |
| [AABB](class_aabb.md#class_AABB) | [operator *](class_transform3d.md#class_Transform3D_operator_mul_AABB) ( right: [AABB](class_aabb.md#class_AABB) ) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [operator *](class_transform3d.md#class_Transform3D_operator_mul_PackedVector3Array) ( right: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) |
| [Plane](class_plane.md#class_Plane) | [operator *](class_transform3d.md#class_Transform3D_operator_mul_Plane) ( right: [Plane](class_plane.md#class_Plane) ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [operator *](class_transform3d.md#class_Transform3D_operator_mul_Transform3D) ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_transform3d.md#class_Transform3D_operator_mul_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [operator *](class_transform3d.md#class_Transform3D_operator_mul_float) ( right: [float](class_float.md#class_float) ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [operator *](class_transform3d.md#class_Transform3D_operator_mul_int) ( right: [int](class_int.md#class_int) ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [operator /](class_transform3d.md#class_Transform3D_operator_div_float) ( right: [float](class_float.md#class_float) ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [operator /](class_transform3d.md#class_Transform3D_operator_div_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_transform3d.md#class_Transform3D_operator_eq_Transform3D) ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) |

---

### Constants

<span id="class_Transform3D_constant_IDENTITY"></span>

**IDENTITY** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_transform3d.md#class_Transform3D_constant_IDENTITY)

The identity **Transform3D**. This is a transform with no translation, no rotation, and a scale of [Vector3.ONE](class_vector3.md#class_Vector3_constant_ONE). Its [basis](class_transform3d.md#class_Transform3D_property_basis) is equal to [Basis.IDENTITY](class_basis.md#class_Basis_constant_IDENTITY). This also means that:

- Its [Basis.x](class_basis.md#class_Basis_property_x) points right ([Vector3.RIGHT](class_vector3.md#class_Vector3_constant_RIGHT));

- Its [Basis.y](class_basis.md#class_Basis_property_y) points up ([Vector3.UP](class_vector3.md#class_Vector3_constant_UP));

- Its [Basis.z](class_basis.md#class_Basis_property_z) points back ([Vector3.BACK](class_vector3.md#class_Vector3_constant_BACK)).

::

    var transform = Transform3D.IDENTITY
    var basis = transform.basis
    print("| X | Y | Z | Origin")
    print("| %.f | %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x, transform.origin.x])
    print("| %.f | %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y, transform.origin.y])
    print("| %.f | %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z, transform.origin.z])
    # Prints:
    # | X | Y | Z | Origin
    # | 1 | 0 | 0 | 0
    # | 0 | 1 | 0 | 0
    # | 0 | 0 | 1 | 0

If a [Vector3](class_vector3.md#class_Vector3), an [AABB](class_aabb.md#class_AABB), a [Plane](class_plane.md#class_Plane), a [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), or another **Transform3D** is transformed (multiplied) by this constant, no transformation occurs.

 **Note:** In GDScript, this constant is equivalent to creating a [Transform3D](class_transform3d.md#class_Transform3D_constructor_Transform3D) without any arguments. It can be used to make your code clearer, and for consistency with C#.

<span id="class_Transform3D_constant_FLIP_X"></span>

**FLIP_X** = `Transform3D(-1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_transform3d.md#class_Transform3D_constant_FLIP_X)

**Transform3D** with mirroring applied perpendicular to the YZ plane. Its [basis](class_transform3d.md#class_Transform3D_property_basis) is equal to [Basis.FLIP_X](class_basis.md#class_Basis_constant_FLIP_X).

<span id="class_Transform3D_constant_FLIP_Y"></span>

**FLIP_Y** = `Transform3D(1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_transform3d.md#class_Transform3D_constant_FLIP_Y)

**Transform3D** with mirroring applied perpendicular to the XZ plane. Its [basis](class_transform3d.md#class_Transform3D_property_basis) is equal to [Basis.FLIP_Y](class_basis.md#class_Basis_constant_FLIP_Y).

<span id="class_Transform3D_constant_FLIP_Z"></span>

**FLIP_Z** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0)` [🔗](class_transform3d.md#class_Transform3D_constant_FLIP_Z)

**Transform3D** with mirroring applied perpendicular to the XY plane. Its [basis](class_transform3d.md#class_Transform3D_property_basis) is equal to [Basis.FLIP_Z](class_basis.md#class_Basis_constant_FLIP_Z).

---

### Property Descriptions

<span id="class_Transform3D_property_basis"></span>

[Basis](class_basis.md#class_Basis) **basis** = `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)` [🔗](class_transform3d.md#class_Transform3D_property_basis)

The [Basis](class_basis.md#class_Basis) of this transform. It is composed by 3 axes ([Basis.x](class_basis.md#class_Basis_property_x), [Basis.y](class_basis.md#class_Basis_property_y), and [Basis.z](class_basis.md#class_Basis_property_z)). Together, these represent the transform's rotation, scale, and shear.

---

<span id="class_Transform3D_property_origin"></span>

[Vector3](class_vector3.md#class_Vector3) **origin** = `Vector3(0, 0, 0)` [🔗](class_transform3d.md#class_Transform3D_property_origin)

The translation offset of this transform. In 3D space, this can be seen as the position.

---

### Constructor Descriptions

<span id="class_Transform3D_constructor_Transform3D"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **Transform3D** ( ) [🔗](class_transform3d.md#class_Transform3D_constructor_Transform3D)

Constructs a **Transform3D** identical to [IDENTITY](class_transform3d.md#class_Transform3D_constant_IDENTITY).

 **Note:** In C#, this constructs a **Transform3D** with its [origin](class_transform3d.md#class_Transform3D_property_origin) and the components of its [basis](class_transform3d.md#class_Transform3D_property_basis) set to [Vector3.ZERO](class_vector3.md#class_Vector3_constant_ZERO).

---

[Transform3D](class_transform3d.md#class_Transform3D) **Transform3D** ( from: [Transform3D](class_transform3d.md#class_Transform3D) )

Constructs a **Transform3D** as a copy of the given **Transform3D**.

---

[Transform3D](class_transform3d.md#class_Transform3D) **Transform3D** ( basis: [Basis](class_basis.md#class_Basis), origin: [Vector3](class_vector3.md#class_Vector3) )

Constructs a **Transform3D** from a [Basis](class_basis.md#class_Basis) and [Vector3](class_vector3.md#class_Vector3).

---

[Transform3D](class_transform3d.md#class_Transform3D) **Transform3D** ( from: [Projection](class_projection.md#class_Projection) )

Constructs a **Transform3D** from a [Projection](class_projection.md#class_Projection). Because **Transform3D** is a 3×4 matrix and [Projection](class_projection.md#class_Projection) is a 4×4 matrix, this operation trims the last row of the projection matrix (`from.x.w`, `from.y.w`, `from.z.w`, and `from.w.w` are not included in the new transform).

---

[Transform3D](class_transform3d.md#class_Transform3D) **Transform3D** ( x_axis: [Vector3](class_vector3.md#class_Vector3), y_axis: [Vector3](class_vector3.md#class_Vector3), z_axis: [Vector3](class_vector3.md#class_Vector3), origin: [Vector3](class_vector3.md#class_Vector3) )

Constructs a **Transform3D** from four [Vector3](class_vector3.md#class_Vector3) values (also called matrix columns).

The first three arguments are the [basis](class_transform3d.md#class_Transform3D_property_basis)'s axes ([Basis.x](class_basis.md#class_Basis_property_x), [Basis.y](class_basis.md#class_Basis_property_y), and [Basis.z](class_basis.md#class_Basis_property_z)).

---

### Method Descriptions

<span id="class_Transform3D_method_affine_inverse"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **affine_inverse** ( ) *const* [🔗](class_transform3d.md#class_Transform3D_method_affine_inverse)

Returns the inverted version of this transform. Unlike [inverse()](class_transform3d.md#class_Transform3D_method_inverse), this method works with almost any [basis](class_transform3d.md#class_Transform3D_property_basis), including non-uniform ones, but is slower. See also [Basis.inverse()](class_basis.md#class_Basis_method_inverse).

 **Note:** For this method to return correctly, the transform's [basis](class_transform3d.md#class_Transform3D_property_basis) needs to have a determinant that is not exactly `0.0` (see [Basis.determinant()](class_basis.md#class_Basis_method_determinant)).

---

<span id="class_Transform3D_method_interpolate_with"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **interpolate_with** ( xform: [Transform3D](class_transform3d.md#class_Transform3D), weight: [float](class_float.md#class_float) ) *const* [🔗](class_transform3d.md#class_Transform3D_method_interpolate_with)

Returns the result of the linear interpolation between this transform and `xform` by the given `weight`.

The `weight` should be between `0.0` and `1.0` (inclusive). Values outside this range are allowed and can be used to perform *extrapolation* instead.

---

<span id="class_Transform3D_method_inverse"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **inverse** ( ) *const* [🔗](class_transform3d.md#class_Transform3D_method_inverse)

Returns the inverted version of this transform. See also [Basis.inverse()](class_basis.md#class_Basis_method_inverse).

 **Note:** For this method to return correctly, the transform's [basis](class_transform3d.md#class_Transform3D_property_basis) needs to be *orthonormal* (see [orthonormalized()](class_transform3d.md#class_Transform3D_method_orthonormalized)). That means the basis should only represent a rotation. If it does not, use [affine_inverse()](class_transform3d.md#class_Transform3D_method_affine_inverse) instead.

---

<span id="class_Transform3D_method_is_equal_approx"></span>

[bool](class_bool.md#class_bool) **is_equal_approx** ( xform: [Transform3D](class_transform3d.md#class_Transform3D) ) *const* [🔗](class_transform3d.md#class_Transform3D_method_is_equal_approx)

Returns `true` if this transform and `xform` are approximately equal, by running @GlobalScope.is_equal_approx() on each component.

---

<span id="class_Transform3D_method_is_finite"></span>

[bool](class_bool.md#class_bool) **is_finite** ( ) *const* [🔗](class_transform3d.md#class_Transform3D_method_is_finite)

Returns `true` if this transform is finite, by calling @GlobalScope.is_finite() on each component.

---

<span id="class_Transform3D_method_looking_at"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **looking_at** ( target: [Vector3](class_vector3.md#class_Vector3), up: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_transform3d.md#class_Transform3D_method_looking_at)

Returns a copy of this transform rotated so that the forward axis (-Z) points towards the `target` position.

The up axis (+Y) points as close to the `up` vector as possible while staying perpendicular to the forward axis. The resulting transform is orthonormalized. The existing rotation, scale, and skew information from the original transform is discarded. The `target` and `up` vectors cannot be zero, cannot be parallel to each other, and are defined in global/parent space.

If `use_model_front` is `true`, the +Z axis (asset front) is treated as forward (implies +X is left) and points toward the `target` position. By default, the -Z axis (camera forward) is treated as forward (implies +X is right).

---

<span id="class_Transform3D_method_orthonormalized"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **orthonormalized** ( ) *const* [🔗](class_transform3d.md#class_Transform3D_method_orthonormalized)

Returns a copy of this transform with its [basis](class_transform3d.md#class_Transform3D_property_basis) orthonormalized. An orthonormal basis is both *orthogonal* (the axes are perpendicular to each other) and *normalized* (the axes have a length of `1.0`), which also means it can only represent a rotation. See also [Basis.orthonormalized()](class_basis.md#class_Basis_method_orthonormalized).

---

<span id="class_Transform3D_method_rotated"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **rotated** ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) *const* [🔗](class_transform3d.md#class_Transform3D_method_rotated)

Returns a copy of this transform rotated around the given `axis` by the given `angle` (in radians).

The `axis` must be a normalized vector (see [Vector3.normalized()](class_vector3.md#class_Vector3_method_normalized)). If `angle` is positive, the basis is rotated counter-clockwise around the axis.

This method is an optimized version of multiplying the given transform `X` with a corresponding rotation transform `R` from the left, i.e., `R * X`.

This can be seen as transforming with respect to the global/parent frame.

---

<span id="class_Transform3D_method_rotated_local"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **rotated_local** ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) *const* [🔗](class_transform3d.md#class_Transform3D_method_rotated_local)

Returns a copy of this transform rotated around the given `axis` by the given `angle` (in radians).

The `axis` must be a normalized vector in the transform's local coordinate system. For example, to rotate around the local X-axis, use [Vector3.RIGHT](class_vector3.md#class_Vector3_constant_RIGHT).

This method is an optimized version of multiplying the given transform `X` with a corresponding rotation transform `R` from the right, i.e., `X * R`.

This can be seen as transforming with respect to the local frame.

---

<span id="class_Transform3D_method_scaled"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **scaled** ( scale: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_transform3d.md#class_Transform3D_method_scaled)

Returns a copy of this transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform `X` with a corresponding scaling transform `S` from the left, i.e., `S * X`.

This can be seen as transforming with respect to the global/parent frame.

---

<span id="class_Transform3D_method_scaled_local"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **scaled_local** ( scale: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_transform3d.md#class_Transform3D_method_scaled_local)

Returns a copy of this transform scaled by the given `scale` factor.

This method is an optimized version of multiplying the given transform `X` with a corresponding scaling transform `S` from the right, i.e., `X * S`.

This can be seen as transforming with respect to the local frame.

---

<span id="class_Transform3D_method_translated"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **translated** ( offset: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_transform3d.md#class_Transform3D_method_translated)

Returns a copy of this transform translated by the given `offset`.

This method is an optimized version of multiplying the given transform `X` with a corresponding translation transform `T` from the left, i.e., `T * X`.

This can be seen as transforming with respect to the global/parent frame.

---

<span id="class_Transform3D_method_translated_local"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **translated_local** ( offset: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_transform3d.md#class_Transform3D_method_translated_local)

Returns a copy of this transform translated by the given `offset`.

This method is an optimized version of multiplying the given transform `X` with a corresponding translation transform `T` from the right, i.e., `X * T`.

This can be seen as transforming with respect to the local frame.

---

### Operator Descriptions

<span id="class_Transform3D_operator_neq_Transform3D"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_transform3d.md#class_Transform3D_operator_neq_Transform3D)

Returns `true` if the components of both transforms are not equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_transform3d.md#class_Transform3D_method_is_equal_approx) instead, which is more reliable.

---

<span id="class_Transform3D_operator_mul_AABB"></span>

[AABB](class_aabb.md#class_AABB) **operator *** ( right: [AABB](class_aabb.md#class_AABB) ) [🔗](class_transform3d.md#class_Transform3D_operator_mul_AABB)

Transforms (multiplies) the [AABB](class_aabb.md#class_AABB) by this transformation matrix.

---

<span id="class_Transform3D_operator_mul_PackedVector3Array"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **operator *** ( right: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) [🔗](class_transform3d.md#class_Transform3D_operator_mul_PackedVector3Array)

Transforms (multiplies) every [Vector3](class_vector3.md#class_Vector3) element of the given [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) by this transformation matrix.

On larger arrays, this operation is much faster than transforming each [Vector3](class_vector3.md#class_Vector3) individually.

---

<span id="class_Transform3D_operator_mul_Plane"></span>

[Plane](class_plane.md#class_Plane) **operator *** ( right: [Plane](class_plane.md#class_Plane) ) [🔗](class_transform3d.md#class_Transform3D_operator_mul_Plane)

Transforms (multiplies) the [Plane](class_plane.md#class_Plane) by this transformation matrix.

---

<span id="class_Transform3D_operator_mul_Transform3D"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **operator *** ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_transform3d.md#class_Transform3D_operator_mul_Transform3D)

Transforms (multiplies) this transform by the `right` transform.

This is the operation performed between parent and child [Node3D](class_node3d.md#class_Node3D) s.

 **Note:** If you need to only modify one attribute of this transform, consider using one of the following methods, instead:

- For translation, see [translated()](class_transform3d.md#class_Transform3D_method_translated) or [translated_local()](class_transform3d.md#class_Transform3D_method_translated_local).

- For rotation, see [rotated()](class_transform3d.md#class_Transform3D_method_rotated) or [rotated_local()](class_transform3d.md#class_Transform3D_method_rotated_local).

- For scale, see [scaled()](class_transform3d.md#class_Transform3D_method_scaled) or [scaled_local()](class_transform3d.md#class_Transform3D_method_scaled_local).

---

<span id="class_Transform3D_operator_mul_Vector3"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_transform3d.md#class_Transform3D_operator_mul_Vector3)

Transforms (multiplies) the [Vector3](class_vector3.md#class_Vector3) by this transformation matrix.

---

<span id="class_Transform3D_operator_mul_float"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **operator *** ( right: [float](class_float.md#class_float) ) [🔗](class_transform3d.md#class_Transform3D_operator_mul_float)

Multiplies all components of the **Transform3D** by the given [float](class_float.md#class_float), including the [origin](class_transform3d.md#class_Transform3D_property_origin). This affects the transform's scale uniformly, scaling the [basis](class_transform3d.md#class_Transform3D_property_basis).

---

<span id="class_Transform3D_operator_mul_int"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **operator *** ( right: [int](class_int.md#class_int) ) [🔗](class_transform3d.md#class_Transform3D_operator_mul_int)

Multiplies all components of the **Transform3D** by the given [int](class_int.md#class_int), including the [origin](class_transform3d.md#class_Transform3D_property_origin). This affects the transform's scale uniformly, scaling the [basis](class_transform3d.md#class_Transform3D_property_basis).

---

<span id="class_Transform3D_operator_div_float"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **operator /** ( right: [float](class_float.md#class_float) ) [🔗](class_transform3d.md#class_Transform3D_operator_div_float)

Divides all components of the **Transform3D** by the given [float](class_float.md#class_float), including the [origin](class_transform3d.md#class_Transform3D_property_origin). This affects the transform's scale uniformly, scaling the [basis](class_transform3d.md#class_Transform3D_property_basis).

---

<span id="class_Transform3D_operator_div_int"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **operator /** ( right: [int](class_int.md#class_int) ) [🔗](class_transform3d.md#class_Transform3D_operator_div_int)

Divides all components of the **Transform3D** by the given [int](class_int.md#class_int), including the [origin](class_transform3d.md#class_Transform3D_property_origin). This affects the transform's scale uniformly, scaling the [basis](class_transform3d.md#class_Transform3D_property_basis).

---

<span id="class_Transform3D_operator_eq_Transform3D"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_transform3d.md#class_Transform3D_operator_eq_Transform3D)

Returns `true` if the components of both transforms are exactly equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_transform3d.md#class_Transform3D_method_is_equal_approx) instead, which is more reliable.
