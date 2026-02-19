<span id="class_Basis"></span>

## Basis

A 3×3 matrix for representing 3D rotation and scale.

### Description

The **Basis** built-in [Variant](class_variant.md#class_Variant) type is a 3×3 matrix used to represent 3D rotation, scale, and shear. It is frequently used within a [Transform3D](class_transform3d.md#class_Transform3D).

A **Basis** is composed by 3 axis vectors, each representing a column of the matrix: [x](class_basis.md#class_Basis_property_x), [y](class_basis.md#class_Basis_property_y), and [z](class_basis.md#class_Basis_property_z). The length of each axis ([Vector3.length()](class_vector3.md#class_Vector3_method_length)) influences the basis's scale, while the direction of all axes influence the rotation. Usually, these axes are perpendicular to one another. However, when you rotate any axis individually, the basis becomes sheared. Applying a sheared basis to a 3D model will make the model appear distorted.

A **Basis** is:

- **Orthogonal** if its axes are perpendicular to each other.

- **Normalized** if the length of every axis is `1.0`.

- **Uniform** if all axes share the same length (see [get_scale()](class_basis.md#class_Basis_method_get_scale)).

- **Orthonormal** if it is both orthogonal and normalized, which allows it to only represent rotations (see [orthonormalized()](class_basis.md#class_Basis_method_orthonormalized)).

- **Conformal** if it is both orthogonal and uniform, which ensures it is not distorted.

For a general introduction, see the [Matrices and transforms](../tutorials/math/matrices_and_transforms.md) tutorial.

 **Note:** Godot uses a right-handed coordinate system, which is a common standard. For directions, the convention for built-in types like [Camera3D](class_camera3d.md#class_Camera3D) is for -Z to point forward (+X is right, +Y is up, and +Z is back). Other objects may use different direction conventions. For more information, see the `3D asset direction conventions <../tutorials/assets_pipeline/importing_3d_scenes/model_export_considerations.html#d-asset-direction-conventions>`__ tutorial.

 **Note:** The basis matrices are exposed as column-major order, which is the same as OpenGL. However, they are stored internally in row-major order, which is the same as DirectX.

 **Note:** In a boolean context, a basis will evaluate to `false` if it's equal to [IDENTITY](class_basis.md#class_Basis_constant_IDENTITY). Otherwise, a basis will always evaluate to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Tutorials

- [Math documentation index](../tutorials/math/index.md)

- [Matrices and transforms](../tutorials/math/matrices_and_transforms.md)

- [Using 3D transforms](../tutorials/3d/using_transforms.md)

- Matrix Transform Demo

- 3D Platformer Demo

- 3D Voxel Demo

- 2.5D Game Demo

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [x](class_basis.md#class_Basis_property_x) | `Vector3(1, 0, 0)` |
| --- | --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [y](class_basis.md#class_Basis_property_y) | `Vector3(0, 1, 0)` |
| [Vector3](class_vector3.md#class_Vector3) | [z](class_basis.md#class_Basis_property_z) | `Vector3(0, 0, 1)` |

### Constructors


| [Basis](class_basis.md#class_Basis) | [Basis](class_basis.md#class_Basis_constructor_Basis) ( ) |
| --- | --- |
| [Basis](class_basis.md#class_Basis) | [Basis](class_basis.md#class_Basis_constructor_Basis) ( from: [Basis](class_basis.md#class_Basis) ) |
| [Basis](class_basis.md#class_Basis) | [Basis](class_basis.md#class_Basis_constructor_Basis) ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) |
| [Basis](class_basis.md#class_Basis) | [Basis](class_basis.md#class_Basis_constructor_Basis) ( from: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| [Basis](class_basis.md#class_Basis) | [Basis](class_basis.md#class_Basis_constructor_Basis) ( x_axis: [Vector3](class_vector3.md#class_Vector3), y_axis: [Vector3](class_vector3.md#class_Vector3), z_axis: [Vector3](class_vector3.md#class_Vector3) ) |

### Methods


| [float](class_float.md#class_float) | [determinant](class_basis.md#class_Basis_method_determinant) ( ) const |
| --- | --- |
| [Basis](class_basis.md#class_Basis) | [from_euler](class_basis.md#class_Basis_method_from_euler) ( euler: [Vector3](class_vector3.md#class_Vector3), order: [int](class_int.md#class_int) = 2 ) static |
| [Basis](class_basis.md#class_Basis) | [from_scale](class_basis.md#class_Basis_method_from_scale) ( scale: [Vector3](class_vector3.md#class_Vector3) ) static |
| [Vector3](class_vector3.md#class_Vector3) | [get_euler](class_basis.md#class_Basis_method_get_euler) ( order: [int](class_int.md#class_int) = 2 ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [get_rotation_quaternion](class_basis.md#class_Basis_method_get_rotation_quaternion) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_scale](class_basis.md#class_Basis_method_get_scale) ( ) const |
| [Basis](class_basis.md#class_Basis) | [inverse](class_basis.md#class_Basis_method_inverse) ( ) const |
| [bool](class_bool.md#class_bool) | [is_conformal](class_basis.md#class_Basis_method_is_conformal) ( ) const |
| [bool](class_bool.md#class_bool) | [is_equal_approx](class_basis.md#class_Basis_method_is_equal_approx) ( b: [Basis](class_basis.md#class_Basis) ) const |
| [bool](class_bool.md#class_bool) | [is_finite](class_basis.md#class_Basis_method_is_finite) ( ) const |
| [Basis](class_basis.md#class_Basis) | [looking_at](class_basis.md#class_Basis_method_looking_at) ( target: [Vector3](class_vector3.md#class_Vector3), up: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class_bool) = false ) static |
| [Basis](class_basis.md#class_Basis) | [orthonormalized](class_basis.md#class_Basis_method_orthonormalized) ( ) const |
| [Basis](class_basis.md#class_Basis) | [rotated](class_basis.md#class_Basis_method_rotated) ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) const |
| [Basis](class_basis.md#class_Basis) | [scaled](class_basis.md#class_Basis_method_scaled) ( scale: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Basis](class_basis.md#class_Basis) | [scaled_local](class_basis.md#class_Basis_method_scaled_local) ( scale: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Basis](class_basis.md#class_Basis) | [slerp](class_basis.md#class_Basis_method_slerp) ( to: [Basis](class_basis.md#class_Basis), weight: [float](class_float.md#class_float) ) const |
| [float](class_float.md#class_float) | [tdotx](class_basis.md#class_Basis_method_tdotx) ( with: [Vector3](class_vector3.md#class_Vector3) ) const |
| [float](class_float.md#class_float) | [tdoty](class_basis.md#class_Basis_method_tdoty) ( with: [Vector3](class_vector3.md#class_Vector3) ) const |
| [float](class_float.md#class_float) | [tdotz](class_basis.md#class_Basis_method_tdotz) ( with: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Basis](class_basis.md#class_Basis) | [transposed](class_basis.md#class_Basis_method_transposed) ( ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_basis.md#class_Basis_operator_neq_Basis) ( right: [Basis](class_basis.md#class_Basis) ) |
| --- | --- |
| [Basis](class_basis.md#class_Basis) | [operator *](class_basis.md#class_Basis_operator_mul_Basis) ( right: [Basis](class_basis.md#class_Basis) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_basis.md#class_Basis_operator_mul_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [Basis](class_basis.md#class_Basis) | [operator *](class_basis.md#class_Basis_operator_mul_float) ( right: [float](class_float.md#class_float) ) |
| [Basis](class_basis.md#class_Basis) | [operator *](class_basis.md#class_Basis_operator_mul_int) ( right: [int](class_int.md#class_int) ) |
| [Basis](class_basis.md#class_Basis) | [operator /](class_basis.md#class_Basis_operator_div_float) ( right: [float](class_float.md#class_float) ) |
| [Basis](class_basis.md#class_Basis) | [operator /](class_basis.md#class_Basis_operator_div_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_basis.md#class_Basis_operator_eq_Basis) ( right: [Basis](class_basis.md#class_Basis) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator []](class_basis.md#class_Basis_operator_idx_int) ( index: [int](class_int.md#class_int) ) |

---

### Constants

<span id="class_Basis_constant_IDENTITY"></span>

**IDENTITY** = `Basis(1, 0, 0, 0, 1, 0, 0, 0, 1)` [🔗](class_basis.md#class_Basis_constant_IDENTITY)

The identity **Basis**. This is an orthonormal basis with no rotation, no shear, and a scale of [Vector3.ONE](class_vector3.md#class_Vector3_constant_ONE). This also means that:

- The [x](class_basis.md#class_Basis_property_x) points right ([Vector3.RIGHT](class_vector3.md#class_Vector3_constant_RIGHT));

- The [y](class_basis.md#class_Basis_property_y) points up ([Vector3.UP](class_vector3.md#class_Vector3_constant_UP));

- The [z](class_basis.md#class_Basis_property_z) points back ([Vector3.BACK](class_vector3.md#class_Vector3_constant_BACK)).

::

    var basis = Basis.IDENTITY
    print("| X | Y | Z")
    print("| %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x])
    print("| %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y])
    print("| %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z])
    # Prints:
    # | X | Y | Z
    # | 1 | 0 | 0
    # | 0 | 1 | 0
    # | 0 | 0 | 1

If a [Vector3](class_vector3.md#class_Vector3) or another **Basis** is transformed (multiplied) by this constant, no transformation occurs.

 **Note:** In GDScript, this constant is equivalent to creating a [Basis](class_basis.md#class_Basis_constructor_Basis) without any arguments. It can be used to make your code clearer, and for consistency with C#.

<span id="class_Basis_constant_FLIP_X"></span>

**FLIP_X** = `Basis(-1, 0, 0, 0, 1, 0, 0, 0, 1)` [🔗](class_basis.md#class_Basis_constant_FLIP_X)

When any basis is multiplied by [FLIP_X](class_basis.md#class_Basis_constant_FLIP_X), it negates all components of the [x](class_basis.md#class_Basis_property_x) axis (the X column).

When [FLIP_X](class_basis.md#class_Basis_constant_FLIP_X) is multiplied by any basis, it negates the [Vector3.x](class_vector3.md#class_Vector3_property_x) component of all axes (the X row).

<span id="class_Basis_constant_FLIP_Y"></span>

**FLIP_Y** = `Basis(1, 0, 0, 0, -1, 0, 0, 0, 1)` [🔗](class_basis.md#class_Basis_constant_FLIP_Y)

When any basis is multiplied by [FLIP_Y](class_basis.md#class_Basis_constant_FLIP_Y), it negates all components of the [y](class_basis.md#class_Basis_property_y) axis (the Y column).

When [FLIP_Y](class_basis.md#class_Basis_constant_FLIP_Y) is multiplied by any basis, it negates the [Vector3.y](class_vector3.md#class_Vector3_property_y) component of all axes (the Y row).

<span id="class_Basis_constant_FLIP_Z"></span>

**FLIP_Z** = `Basis(1, 0, 0, 0, 1, 0, 0, 0, -1)` [🔗](class_basis.md#class_Basis_constant_FLIP_Z)

When any basis is multiplied by [FLIP_Z](class_basis.md#class_Basis_constant_FLIP_Z), it negates all components of the [z](class_basis.md#class_Basis_property_z) axis (the Z column).

When [FLIP_Z](class_basis.md#class_Basis_constant_FLIP_Z) is multiplied by any basis, it negates the [Vector3.z](class_vector3.md#class_Vector3_property_z) component of all axes (the Z row).

---

### Property Descriptions

<span id="class_Basis_property_x"></span>

[Vector3](class_vector3.md#class_Vector3) **x** = `Vector3(1, 0, 0)` [🔗](class_basis.md#class_Basis_property_x)

The basis's X axis, and the column `0` of the matrix.

On the identity basis, this vector points right ([Vector3.RIGHT](class_vector3.md#class_Vector3_constant_RIGHT)).

---

<span id="class_Basis_property_y"></span>

[Vector3](class_vector3.md#class_Vector3) **y** = `Vector3(0, 1, 0)` [🔗](class_basis.md#class_Basis_property_y)

The basis's Y axis, and the column `1` of the matrix.

On the identity basis, this vector points up ([Vector3.UP](class_vector3.md#class_Vector3_constant_UP)).

---

<span id="class_Basis_property_z"></span>

[Vector3](class_vector3.md#class_Vector3) **z** = `Vector3(0, 0, 1)` [🔗](class_basis.md#class_Basis_property_z)

The basis's Z axis, and the column `2` of the matrix.

On the identity basis, this vector points back ([Vector3.BACK](class_vector3.md#class_Vector3_constant_BACK)).

---

### Constructor Descriptions

<span id="class_Basis_constructor_Basis"></span>

[Basis](class_basis.md#class_Basis) **Basis** ( ) [🔗](class_basis.md#class_Basis_constructor_Basis)

Constructs a **Basis** identical to [IDENTITY](class_basis.md#class_Basis_constant_IDENTITY).

 **Note:** In C#, this constructs a **Basis** with all of its components set to [Vector3.ZERO](class_vector3.md#class_Vector3_constant_ZERO).

---

[Basis](class_basis.md#class_Basis) **Basis** ( from: [Basis](class_basis.md#class_Basis) )

Constructs a **Basis** as a copy of the given **Basis**.

---

[Basis](class_basis.md#class_Basis) **Basis** ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) )

Constructs a **Basis** that only represents rotation, rotated around the `axis` by the given `angle`, in radians. The axis must be a normalized vector.

 **Note:** This is the same as using [rotated()](class_basis.md#class_Basis_method_rotated) on the [IDENTITY](class_basis.md#class_Basis_constant_IDENTITY) basis. With more than one angle consider using [from_euler()](class_basis.md#class_Basis_method_from_euler), instead.

---

[Basis](class_basis.md#class_Basis) **Basis** ( from: [Quaternion](class_quaternion.md#class_Quaternion) )

Constructs a **Basis** that only represents rotation from the given [Quaternion](class_quaternion.md#class_Quaternion).

 **Note:** Quaternions *only* store rotation, not scale. Because of this, conversions from **Basis** to [Quaternion](class_quaternion.md#class_Quaternion) cannot always be reversed.

---

[Basis](class_basis.md#class_Basis) **Basis** ( x_axis: [Vector3](class_vector3.md#class_Vector3), y_axis: [Vector3](class_vector3.md#class_Vector3), z_axis: [Vector3](class_vector3.md#class_Vector3) )

Constructs a **Basis** from 3 axis vectors. These are the columns of the basis matrix.

---

### Method Descriptions

<span id="class_Basis_method_determinant"></span>

[float](class_float.md#class_float) **determinant** ( ) *const* [🔗](class_basis.md#class_Basis_method_determinant)

Returns the determinant of this basis's matrix. For advanced math, this number can be used to determine a few attributes:

- If the determinant is exactly `0.0`, the basis is not invertible (see [inverse()](class_basis.md#class_Basis_method_inverse)).

- If the determinant is a negative number, the basis represents a negative scale.

 **Note:** If the basis's scale is the same for every axis, its determinant is always that scale by the power of 3.

---

<span id="class_Basis_method_from_euler"></span>

[Basis](class_basis.md#class_Basis) **from_euler** ( euler: [Vector3](class_vector3.md#class_Vector3), order: [int](class_int.md#class_int) = 2 ) *static* [🔗](class_basis.md#class_Basis_method_from_euler)

Constructs a new **Basis** that only represents rotation from the given [Vector3](class_vector3.md#class_Vector3) of Euler angles, in radians.

- The [Vector3.x](class_vector3.md#class_Vector3_property_x) should contain the angle around the [x](class_basis.md#class_Basis_property_x) axis (pitch);

- The [Vector3.y](class_vector3.md#class_Vector3_property_y) should contain the angle around the [y](class_basis.md#class_Basis_property_y) axis (yaw);

- The [Vector3.z](class_vector3.md#class_Vector3_property_z) should contain the angle around the [z](class_basis.md#class_Basis_property_z) axis (roll).

.. tabs::

```
```

    # Creates a Basis whose z axis points down.
    var my_basis = Basis.from_euler(Vector3(TAU / 4, 0, 0))

    print(my_basis.z) # Prints (0.0, -1.0, 0.0)

```
```

    // Creates a Basis whose z axis points down.
    var myBasis = Basis.FromEuler(new Vector3(Mathf.Tau / 4.0f, 0.0f, 0.0f));

    GD.Print(myBasis.Z); // Prints (0, -1, 0)

The order of each consecutive rotation can be changed with `order` (see EulerOrder constants). By default, the YXZ convention is used (@GlobalScope.EULER_ORDER_YXZ): the basis rotates first around the Y axis (yaw), then X (pitch), and lastly Z (roll). When using the opposite method [get_euler()](class_basis.md#class_Basis_method_get_euler), this order is reversed.

---

<span id="class_Basis_method_from_scale"></span>

[Basis](class_basis.md#class_Basis) **from_scale** ( scale: [Vector3](class_vector3.md#class_Vector3) ) *static* [🔗](class_basis.md#class_Basis_method_from_scale)

Constructs a new **Basis** that only represents scale, with no rotation or shear, from the given `scale` vector.

.. tabs::

```
```

    var my_basis = Basis.from_scale(Vector3(2, 4, 8))

    print(my_basis.x) # Prints (2.0, 0.0, 0.0)
    print(my_basis.y) # Prints (0.0, 4.0, 0.0)
    print(my_basis.z) # Prints (0.0, 0.0, 8.0)

```
```

    var myBasis = Basis.FromScale(new Vector3(2.0f, 4.0f, 8.0f));

    GD.Print(myBasis.X); // Prints (2, 0, 0)
    GD.Print(myBasis.Y); // Prints (0, 4, 0)
    GD.Print(myBasis.Z); // Prints (0, 0, 8)

 **Note:** In linear algebra, the matrix of this basis is also known as a diagonal matrix.

---

<span id="class_Basis_method_get_euler"></span>

[Vector3](class_vector3.md#class_Vector3) **get_euler** ( order: [int](class_int.md#class_int) = 2 ) *const* [🔗](class_basis.md#class_Basis_method_get_euler)

Returns this basis's rotation as a [Vector3](class_vector3.md#class_Vector3) of Euler angles, in radians. For the returned value:

- The [Vector3.x](class_vector3.md#class_Vector3_property_x) contains the angle around the [x](class_basis.md#class_Basis_property_x) axis (pitch);

- The [Vector3.y](class_vector3.md#class_Vector3_property_y) contains the angle around the [y](class_basis.md#class_Basis_property_y) axis (yaw);

- The [Vector3.z](class_vector3.md#class_Vector3_property_z) contains the angle around the [z](class_basis.md#class_Basis_property_z) axis (roll).

The order of each consecutive rotation can be changed with `order` (see EulerOrder constants). By default, the YXZ convention is used (@GlobalScope.EULER_ORDER_YXZ): Z (roll) is calculated first, then X (pitch), and lastly Y (yaw). When using the opposite method [from_euler()](class_basis.md#class_Basis_method_from_euler), this order is reversed.

 **Note:** For this method to return correctly, the basis needs to be *orthonormal* (see [orthonormalized()](class_basis.md#class_Basis_method_orthonormalized)).

 **Note:** Euler angles are much more intuitive but are not suitable for 3D math. Because of this, consider using the [get_rotation_quaternion()](class_basis.md#class_Basis_method_get_rotation_quaternion) method instead, which returns a [Quaternion](class_quaternion.md#class_Quaternion).

 **Note:** In the Inspector dock, a basis's rotation is often displayed in Euler angles (in degrees), as is the case with the [Node3D.rotation](class_node3d.md#class_Node3D_property_rotation) property.

---

<span id="class_Basis_method_get_rotation_quaternion"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **get_rotation_quaternion** ( ) *const* [🔗](class_basis.md#class_Basis_method_get_rotation_quaternion)

Returns this basis's rotation as a [Quaternion](class_quaternion.md#class_Quaternion).

 **Note:** Quaternions are much more suitable for 3D math but are less intuitive. For user interfaces, consider using the [get_euler()](class_basis.md#class_Basis_method_get_euler) method, which returns Euler angles.

---

<span id="class_Basis_method_get_scale"></span>

[Vector3](class_vector3.md#class_Vector3) **get_scale** ( ) *const* [🔗](class_basis.md#class_Basis_method_get_scale)

Returns the length of each axis of this basis, as a [Vector3](class_vector3.md#class_Vector3). If the basis is not sheared, this value is the scaling factor. It is not affected by rotation.

.. tabs::

```
```

    var my_basis = Basis(
        Vector3(2, 0, 0),
        Vector3(0, 4, 0),
        Vector3(0, 0, 8)
    )
    # Rotating the Basis in any way preserves its scale.
    my_basis = my_basis.rotated(Vector3.UP, TAU / 2)
    my_basis = my_basis.rotated(Vector3.RIGHT, TAU / 4)

    print(my_basis.get_scale()) # Prints (2.0, 4.0, 8.0)

```
```

    var myBasis = new Basis(
        Vector3(2.0f, 0.0f, 0.0f),
        Vector3(0.0f, 4.0f, 0.0f),
        Vector3(0.0f, 0.0f, 8.0f)
    );
    // Rotating the Basis in any way preserves its scale.
    myBasis = myBasis.Rotated(Vector3.Up, Mathf.Tau / 2.0f);
    myBasis = myBasis.Rotated(Vector3.Right, Mathf.Tau / 4.0f);

    GD.Print(myBasis.Scale); // Prints (2, 4, 8)

 **Note:** If the value returned by [determinant()](class_basis.md#class_Basis_method_determinant) is negative, the scale is also negative.

---

<span id="class_Basis_method_inverse"></span>

[Basis](class_basis.md#class_Basis) **inverse** ( ) *const* [🔗](class_basis.md#class_Basis_method_inverse)

Returns the inverse of this basis's matrix.

---

<span id="class_Basis_method_is_conformal"></span>

[bool](class_bool.md#class_bool) **is_conformal** ( ) *const* [🔗](class_basis.md#class_Basis_method_is_conformal)

Returns `true` if this basis is conformal. A conformal basis is both *orthogonal* (the axes are perpendicular to each other) and *uniform* (the axes share the same length). This method can be especially useful during physics calculations.

---

<span id="class_Basis_method_is_equal_approx"></span>

[bool](class_bool.md#class_bool) **is_equal_approx** ( b: [Basis](class_basis.md#class_Basis) ) *const* [🔗](class_basis.md#class_Basis_method_is_equal_approx)

Returns `true` if this basis and `b` are approximately equal, by calling @GlobalScope.is_equal_approx() on all vector components.

---

<span id="class_Basis_method_is_finite"></span>

[bool](class_bool.md#class_bool) **is_finite** ( ) *const* [🔗](class_basis.md#class_Basis_method_is_finite)

Returns `true` if this basis is finite, by calling @GlobalScope.is_finite() on all vector components.

---

<span id="class_Basis_method_looking_at"></span>

[Basis](class_basis.md#class_Basis) **looking_at** ( target: [Vector3](class_vector3.md#class_Vector3), up: [Vector3](class_vector3.md#class_Vector3) = Vector3(0, 1, 0), use_model_front: [bool](class_bool.md#class_bool) = false ) *static* [🔗](class_basis.md#class_Basis_method_looking_at)

Creates a new **Basis** with a rotation such that the forward axis (-Z) points towards the `target` position.

By default, the -Z axis (camera forward) is treated as forward (implies +X is right). If `use_model_front` is `true`, the +Z axis (asset front) is treated as forward (implies +X is left) and points toward the `target` position.

The up axis (+Y) points as close to the `up` vector as possible while staying perpendicular to the forward axis. The returned basis is orthonormalized (see [orthonormalized()](class_basis.md#class_Basis_method_orthonormalized)).

The `target` and the `up` cannot be [Vector3.ZERO](class_vector3.md#class_Vector3_constant_ZERO), and shouldn't be colinear to avoid unintended rotation around local Z axis.

---

<span id="class_Basis_method_orthonormalized"></span>

[Basis](class_basis.md#class_Basis) **orthonormalized** ( ) *const* [🔗](class_basis.md#class_Basis_method_orthonormalized)

Returns the orthonormalized version of this basis. An orthonormal basis is both *orthogonal* (the axes are perpendicular to each other) and *normalized* (the axes have a length of `1.0`), which also means it can only represent a rotation.

It is often useful to call this method to avoid rounding errors on a rotating basis:

.. tabs::

```
```

    # Rotate this Node3D every frame.
    func _process(delta):
        basis = basis.rotated(Vector3.UP, TAU * delta)
        basis = basis.rotated(Vector3.RIGHT, TAU * delta)
        basis = basis.orthonormalized()

```
```

    // Rotate this Node3D every frame.
    public override void _Process(double delta)
    {
        Basis = Basis.Rotated(Vector3.Up, Mathf.Tau * (float)delta)
                .Rotated(Vector3.Right, Mathf.Tau * (float)delta)
                .Orthonormalized();
    }

---

<span id="class_Basis_method_rotated"></span>

[Basis](class_basis.md#class_Basis) **rotated** ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) *const* [🔗](class_basis.md#class_Basis_method_rotated)

Returns a copy of this basis rotated around the given `axis` by the given `angle` (in radians).

The `axis` must be a normalized vector (see [Vector3.normalized()](class_vector3.md#class_Vector3_method_normalized)). If `angle` is positive, the basis is rotated counter-clockwise around the axis.

.. tabs::

```
```

    var my_basis = Basis.IDENTITY
    var angle = TAU / 2

    my_basis = my_basis.rotated(Vector3.UP, angle)    # Rotate around the up axis (yaw).
    my_basis = my_basis.rotated(Vector3.RIGHT, angle) # Rotate around the right axis (pitch).
    my_basis = my_basis.rotated(Vector3.BACK, angle)  # Rotate around the back axis (roll).

```
```

    var myBasis = Basis.Identity;
    var angle = Mathf.Tau / 2.0f;

    myBasis = myBasis.Rotated(Vector3.Up, angle);    // Rotate around the up axis (yaw).
    myBasis = myBasis.Rotated(Vector3.Right, angle); // Rotate around the right axis (pitch).
    myBasis = myBasis.Rotated(Vector3.Back, angle);  // Rotate around the back axis (roll).

---

<span id="class_Basis_method_scaled"></span>

[Basis](class_basis.md#class_Basis) **scaled** ( scale: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_basis.md#class_Basis_method_scaled)

Returns this basis with each axis's components scaled by the given `scale`'s components.

The basis matrix's rows are multiplied by `scale`'s components. This operation is a global scale (relative to the parent).

.. tabs::

```
```

    var my_basis = Basis(
        Vector3(1, 1, 1),
        Vector3(2, 2, 2),
        Vector3(3, 3, 3)
    )
    my_basis = my_basis.scaled(Vector3(0, 2, -2))

    print(my_basis.x) # Prints (0.0, 2.0, -2.0)
    print(my_basis.y) # Prints (0.0, 4.0, -4.0)
    print(my_basis.z) # Prints (0.0, 6.0, -6.0)

```
```

    var myBasis = new Basis(
        new Vector3(1.0f, 1.0f, 1.0f),
        new Vector3(2.0f, 2.0f, 2.0f),
        new Vector3(3.0f, 3.0f, 3.0f)
    );
    myBasis = myBasis.Scaled(new Vector3(0.0f, 2.0f, -2.0f));

    GD.Print(myBasis.X); // Prints (0, 2, -2)
    GD.Print(myBasis.Y); // Prints (0, 4, -4)
    GD.Print(myBasis.Z); // Prints (0, 6, -6)

---

<span id="class_Basis_method_scaled_local"></span>

[Basis](class_basis.md#class_Basis) **scaled_local** ( scale: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_basis.md#class_Basis_method_scaled_local)

Returns this basis with each axis scaled by the corresponding component in the given `scale`.

The basis matrix's columns are multiplied by `scale`'s components. This operation is a local scale (relative to self).

.. tabs::

```
```

    var my_basis = Basis(
        Vector3(1, 1, 1),
        Vector3(2, 2, 2),
        Vector3(3, 3, 3)
    )
    my_basis = my_basis.scaled_local(Vector3(0, 2, -2))

    print(my_basis.x) # Prints (0.0, 0.0, 0.0)
    print(my_basis.y) # Prints (4.0, 4.0, 4.0)
    print(my_basis.z) # Prints (-6.0, -6.0, -6.0)

```
```

    var myBasis = new Basis(
        new Vector3(1.0f, 1.0f, 1.0f),
        new Vector3(2.0f, 2.0f, 2.0f),
        new Vector3(3.0f, 3.0f, 3.0f)
    );
    myBasis = myBasis.ScaledLocal(new Vector3(0.0f, 2.0f, -2.0f));

    GD.Print(myBasis.X); // Prints (0, 0, 0)
    GD.Print(myBasis.Y); // Prints (4, 4, 4)
    GD.Print(myBasis.Z); // Prints (-6, -6, -6)

---

<span id="class_Basis_method_slerp"></span>

[Basis](class_basis.md#class_Basis) **slerp** ( to: [Basis](class_basis.md#class_Basis), weight: [float](class_float.md#class_float) ) *const* [🔗](class_basis.md#class_Basis_method_slerp)

Performs a spherical-linear interpolation with the `to` basis, given a `weight`. Both this basis and `to` should represent a rotation.

 **Example:** Smoothly rotate a [Node3D](class_node3d.md#class_Node3D) to the target basis over time, with a [Tween](class_tween.md#class_Tween):

::

    var start_basis = Basis.IDENTITY
    var target_basis = Basis.IDENTITY.rotated(Vector3.UP, TAU / 2)

    func _ready():
        create_tween().tween_method(interpolate, 0.0, 1.0, 5.0).set_trans(Tween.TRANS_EXPO)

    func interpolate(weight):
        basis = start_basis.slerp(target_basis, weight)

---

<span id="class_Basis_method_tdotx"></span>

[float](class_float.md#class_float) **tdotx** ( with: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_basis.md#class_Basis_method_tdotx)

Returns the transposed dot product between `with` and the [x](class_basis.md#class_Basis_property_x) axis (see [transposed()](class_basis.md#class_Basis_method_transposed)).

This is equivalent to `basis.x.dot(vector)`.

---

<span id="class_Basis_method_tdoty"></span>

[float](class_float.md#class_float) **tdoty** ( with: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_basis.md#class_Basis_method_tdoty)

Returns the transposed dot product between `with` and the [y](class_basis.md#class_Basis_property_y) axis (see [transposed()](class_basis.md#class_Basis_method_transposed)).

This is equivalent to `basis.y.dot(vector)`.

---

<span id="class_Basis_method_tdotz"></span>

[float](class_float.md#class_float) **tdotz** ( with: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_basis.md#class_Basis_method_tdotz)

Returns the transposed dot product between `with` and the [z](class_basis.md#class_Basis_property_z) axis (see [transposed()](class_basis.md#class_Basis_method_transposed)).

This is equivalent to `basis.z.dot(vector)`.

---

<span id="class_Basis_method_transposed"></span>

[Basis](class_basis.md#class_Basis) **transposed** ( ) *const* [🔗](class_basis.md#class_Basis_method_transposed)

Returns the transposed version of this basis. This turns the basis matrix's columns into rows, and its rows into columns.

.. tabs::

```
```

    var my_basis = Basis(
        Vector3(1, 2, 3),
        Vector3(4, 5, 6),
        Vector3(7, 8, 9)
    )
    my_basis = my_basis.transposed()

    print(my_basis.x) # Prints (1.0, 4.0, 7.0)
    print(my_basis.y) # Prints (2.0, 5.0, 8.0)
    print(my_basis.z) # Prints (3.0, 6.0, 9.0)

```
```

    var myBasis = new Basis(
        new Vector3(1.0f, 2.0f, 3.0f),
        new Vector3(4.0f, 5.0f, 6.0f),
        new Vector3(7.0f, 8.0f, 9.0f)
    );
    myBasis = myBasis.Transposed();

    GD.Print(myBasis.X); // Prints (1, 4, 7)
    GD.Print(myBasis.Y); // Prints (2, 5, 8)
    GD.Print(myBasis.Z); // Prints (3, 6, 9)

---

### Operator Descriptions

<span id="class_Basis_operator_neq_Basis"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Basis](class_basis.md#class_Basis) ) [🔗](class_basis.md#class_Basis_operator_neq_Basis)

Returns `true` if the components of both **Basis** matrices are not equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_basis.md#class_Basis_method_is_equal_approx) instead, which is more reliable.

---

<span id="class_Basis_operator_mul_Basis"></span>

[Basis](class_basis.md#class_Basis) **operator *** ( right: [Basis](class_basis.md#class_Basis) ) [🔗](class_basis.md#class_Basis_operator_mul_Basis)

Transforms (multiplies) the `right` basis by this basis.

This is the operation performed between parent and child [Node3D](class_node3d.md#class_Node3D) s.

---

<span id="class_Basis_operator_mul_Vector3"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_basis.md#class_Basis_operator_mul_Vector3)

Transforms (multiplies) the `right` vector by this basis, returning a [Vector3](class_vector3.md#class_Vector3).

.. tabs::

```
```

    # Basis that swaps the X/Z axes and doubles the scale.
    var my_basis = Basis(Vector3(0, 2, 0), Vector3(2, 0, 0), Vector3(0, 0, 2))
    print(my_basis * Vector3(1, 2, 3)) # Prints (4.0, 2.0, 6.0)

```
```

    // Basis that swaps the X/Z axes and doubles the scale.
    var myBasis = new Basis(new Vector3(0, 2, 0), new Vector3(2, 0, 0), new Vector3(0, 0, 2));
    GD.Print(myBasis * new Vector3(1, 2, 3)); // Prints (4, 2, 6)

---

<span id="class_Basis_operator_mul_float"></span>

[Basis](class_basis.md#class_Basis) **operator *** ( right: [float](class_float.md#class_float) ) [🔗](class_basis.md#class_Basis_operator_mul_float)

Multiplies all components of the **Basis** by the given [float](class_float.md#class_float). This affects the basis's scale uniformly, resizing all 3 axes by the `right` value.

---

<span id="class_Basis_operator_mul_int"></span>

[Basis](class_basis.md#class_Basis) **operator *** ( right: [int](class_int.md#class_int) ) [🔗](class_basis.md#class_Basis_operator_mul_int)

Multiplies all components of the **Basis** by the given [int](class_int.md#class_int). This affects the basis's scale uniformly, resizing all 3 axes by the `right` value.

---

<span id="class_Basis_operator_div_float"></span>

[Basis](class_basis.md#class_Basis) **operator /** ( right: [float](class_float.md#class_float) ) [🔗](class_basis.md#class_Basis_operator_div_float)

Divides all components of the **Basis** by the given [float](class_float.md#class_float). This affects the basis's scale uniformly, resizing all 3 axes by the `right` value.

---

<span id="class_Basis_operator_div_int"></span>

[Basis](class_basis.md#class_Basis) **operator /** ( right: [int](class_int.md#class_int) ) [🔗](class_basis.md#class_Basis_operator_div_int)

Divides all components of the **Basis** by the given [int](class_int.md#class_int). This affects the basis's scale uniformly, resizing all 3 axes by the `right` value.

---

<span id="class_Basis_operator_eq_Basis"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Basis](class_basis.md#class_Basis) ) [🔗](class_basis.md#class_Basis_operator_eq_Basis)

Returns `true` if the components of both **Basis** matrices are exactly equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_basis.md#class_Basis_method_is_equal_approx) instead, which is more reliable.

---

<span id="class_Basis_operator_idx_int"></span>

[Vector3](class_vector3.md#class_Vector3) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_basis.md#class_Basis_operator_idx_int)

Accesses each axis (column) of this basis by their index. Index `0` is the same as [x](class_basis.md#class_Basis_property_x), index `1` is the same as [y](class_basis.md#class_Basis_property_y), and index `2` is the same as [z](class_basis.md#class_Basis_property_z).

 **Note:** In C++, this operator accesses the rows of the basis matrix, *not* the columns. For the same behavior as scripting languages, use the `set_column` and `get_column` methods.
