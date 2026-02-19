<span id="class_Vector4i"></span>

## Vector4i

A 4D vector using integer coordinates.

### Description

A 4-element structure that can be used to represent 4D grid coordinates or any other quadruplet of integers.

It uses integer coordinates and is therefore preferable to [Vector4](class_vector4.md#class_Vector4) when exact precision is required. Note that the values are limited to 32 bits, and unlike [Vector4](class_vector4.md#class_Vector4) this cannot be configured with an engine build option. Use [int](class_int.md#class_int) or [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) if 64-bit values are needed.

 **Note:** In a boolean context, a Vector4i will evaluate to `false` if it's equal to `Vector4i(0, 0, 0, 0)`. Otherwise, a Vector4i will always evaluate to `true`.

### Properties


| [int](class_int.md#class_int) | [w](class_vector4i.md#class_Vector4i_property_w) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [x](class_vector4i.md#class_Vector4i_property_x) | `0` |
| [int](class_int.md#class_int) | [y](class_vector4i.md#class_Vector4i_property_y) | `0` |
| [int](class_int.md#class_int) | [z](class_vector4i.md#class_Vector4i_property_z) | `0` |

### Constructors


| [Vector4i](class_vector4i.md#class_Vector4i) | [Vector4i](class_vector4i.md#class_Vector4i_constructor_Vector4i) ( ) |
| --- | --- |
| [Vector4i](class_vector4i.md#class_Vector4i) | [Vector4i](class_vector4i.md#class_Vector4i_constructor_Vector4i) ( from: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [Vector4i](class_vector4i.md#class_Vector4i_constructor_Vector4i) ( from: [Vector4](class_vector4.md#class_Vector4) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [Vector4i](class_vector4i.md#class_Vector4i_constructor_Vector4i) ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int), z: [int](class_int.md#class_int), w: [int](class_int.md#class_int) ) |

### Methods


| [Vector4i](class_vector4i.md#class_Vector4i) | [abs](class_vector4i.md#class_Vector4i_method_abs) ( ) const |
| --- | --- |
| [Vector4i](class_vector4i.md#class_Vector4i) | [clamp](class_vector4i.md#class_Vector4i_method_clamp) ( min: [Vector4i](class_vector4i.md#class_Vector4i), max: [Vector4i](class_vector4i.md#class_Vector4i) ) const |
| [Vector4i](class_vector4i.md#class_Vector4i) | [clampi](class_vector4i.md#class_Vector4i_method_clampi) ( min: [int](class_int.md#class_int), max: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [distance_squared_to](class_vector4i.md#class_Vector4i_method_distance_squared_to) ( to: [Vector4i](class_vector4i.md#class_Vector4i) ) const |
| [float](class_float.md#class_float) | [distance_to](class_vector4i.md#class_Vector4i_method_distance_to) ( to: [Vector4i](class_vector4i.md#class_Vector4i) ) const |
| [float](class_float.md#class_float) | [length](class_vector4i.md#class_Vector4i_method_length) ( ) const |
| [int](class_int.md#class_int) | [length_squared](class_vector4i.md#class_Vector4i_method_length_squared) ( ) const |
| [Vector4i](class_vector4i.md#class_Vector4i) | [max](class_vector4i.md#class_Vector4i_method_max) ( with: [Vector4i](class_vector4i.md#class_Vector4i) ) const |
| [int](class_int.md#class_int) | [max_axis_index](class_vector4i.md#class_Vector4i_method_max_axis_index) ( ) const |
| [Vector4i](class_vector4i.md#class_Vector4i) | [maxi](class_vector4i.md#class_Vector4i_method_maxi) ( with: [int](class_int.md#class_int) ) const |
| [Vector4i](class_vector4i.md#class_Vector4i) | [min](class_vector4i.md#class_Vector4i_method_min) ( with: [Vector4i](class_vector4i.md#class_Vector4i) ) const |
| [int](class_int.md#class_int) | [min_axis_index](class_vector4i.md#class_Vector4i_method_min_axis_index) ( ) const |
| [Vector4i](class_vector4i.md#class_Vector4i) | [mini](class_vector4i.md#class_Vector4i_method_mini) ( with: [int](class_int.md#class_int) ) const |
| [Vector4i](class_vector4i.md#class_Vector4i) | [sign](class_vector4i.md#class_Vector4i_method_sign) ( ) const |
| [Vector4i](class_vector4i.md#class_Vector4i) | [snapped](class_vector4i.md#class_Vector4i_method_snapped) ( step: [Vector4i](class_vector4i.md#class_Vector4i) ) const |
| [Vector4i](class_vector4i.md#class_Vector4i) | [snappedi](class_vector4i.md#class_Vector4i_method_snappedi) ( step: [int](class_int.md#class_int) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_vector4i.md#class_Vector4i_operator_neq_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| --- | --- |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator %](class_vector4i.md#class_Vector4i_operator_mod_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator %](class_vector4i.md#class_Vector4i_operator_mod_int) ( right: [int](class_int.md#class_int) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator *](class_vector4i.md#class_Vector4i_operator_mul_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator *](class_vector4i.md#class_Vector4i_operator_mul_float) ( right: [float](class_float.md#class_float) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator *](class_vector4i.md#class_Vector4i_operator_mul_int) ( right: [int](class_int.md#class_int) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator +](class_vector4i.md#class_Vector4i_operator_sum_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator -](class_vector4i.md#class_Vector4i_operator_dif_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator /](class_vector4i.md#class_Vector4i_operator_div_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator /](class_vector4i.md#class_Vector4i_operator_div_float) ( right: [float](class_float.md#class_float) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator /](class_vector4i.md#class_Vector4i_operator_div_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_vector4i.md#class_Vector4i_operator_eq_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [bool](class_bool.md#class_bool) | [operator >](class_vector4i.md#class_Vector4i_operator_gt_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [bool](class_bool.md#class_bool) | [operator >=](class_vector4i.md#class_Vector4i_operator_gte_Vector4i) ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [int](class_int.md#class_int) | [operator []](class_vector4i.md#class_Vector4i_operator_idx_int) ( index: [int](class_int.md#class_int) ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator unary+](class_vector4i.md#class_Vector4i_operator_unplus) ( ) |
| [Vector4i](class_vector4i.md#class_Vector4i) | [operator unary-](class_vector4i.md#class_Vector4i_operator_unminus) ( ) |

---

### Enumerations

<span id="enum_Vector4i_Axis"></span>

enum **Axis**: [🔗](class_vector4i.md#enum_Vector4i_Axis)

<span id="class_Vector4i_constant_AXIS_X"></span>

[Axis](class_vector4i.md#enum_Vector4i_Axis) **AXIS_X** = `0`

Enumerated value for the X axis. Returned by [max_axis_index()](class_vector4i.md#class_Vector4i_method_max_axis_index) and [min_axis_index()](class_vector4i.md#class_Vector4i_method_min_axis_index).

<span id="class_Vector4i_constant_AXIS_Y"></span>

[Axis](class_vector4i.md#enum_Vector4i_Axis) **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by [max_axis_index()](class_vector4i.md#class_Vector4i_method_max_axis_index) and [min_axis_index()](class_vector4i.md#class_Vector4i_method_min_axis_index).

<span id="class_Vector4i_constant_AXIS_Z"></span>

[Axis](class_vector4i.md#enum_Vector4i_Axis) **AXIS_Z** = `2`

Enumerated value for the Z axis. Returned by [max_axis_index()](class_vector4i.md#class_Vector4i_method_max_axis_index) and [min_axis_index()](class_vector4i.md#class_Vector4i_method_min_axis_index).

<span id="class_Vector4i_constant_AXIS_W"></span>

[Axis](class_vector4i.md#enum_Vector4i_Axis) **AXIS_W** = `3`

Enumerated value for the W axis. Returned by [max_axis_index()](class_vector4i.md#class_Vector4i_method_max_axis_index) and [min_axis_index()](class_vector4i.md#class_Vector4i_method_min_axis_index).

---

### Constants

<span id="class_Vector4i_constant_ZERO"></span>

**ZERO** = `Vector4i(0, 0, 0, 0)` [🔗](class_vector4i.md#class_Vector4i_constant_ZERO)

Zero vector, a vector with all components set to `0`.

<span id="class_Vector4i_constant_ONE"></span>

**ONE** = `Vector4i(1, 1, 1, 1)` [🔗](class_vector4i.md#class_Vector4i_constant_ONE)

One vector, a vector with all components set to `1`.

<span id="class_Vector4i_constant_MIN"></span>

**MIN** = `Vector4i(-2147483648, -2147483648, -2147483648, -2147483648)` [🔗](class_vector4i.md#class_Vector4i_constant_MIN)

Min vector, a vector with all components equal to `INT32_MIN`. Can be used as a negative integer equivalent of [Vector4.INF](class_vector4.md#class_Vector4_constant_INF).

<span id="class_Vector4i_constant_MAX"></span>

**MAX** = `Vector4i(2147483647, 2147483647, 2147483647, 2147483647)` [🔗](class_vector4i.md#class_Vector4i_constant_MAX)

Max vector, a vector with all components equal to `INT32_MAX`. Can be used as an integer equivalent of [Vector4.INF](class_vector4.md#class_Vector4_constant_INF).

---

### Property Descriptions

<span id="class_Vector4i_property_w"></span>

[int](class_int.md#class_int) **w** = `0` [🔗](class_vector4i.md#class_Vector4i_property_w)

The vector's W component. Also accessible by using the index position `[3]`.

---

<span id="class_Vector4i_property_x"></span>

[int](class_int.md#class_int) **x** = `0` [🔗](class_vector4i.md#class_Vector4i_property_x)

The vector's X component. Also accessible by using the index position `[0]`.

---

<span id="class_Vector4i_property_y"></span>

[int](class_int.md#class_int) **y** = `0` [🔗](class_vector4i.md#class_Vector4i_property_y)

The vector's Y component. Also accessible by using the index position `[1]`.

---

<span id="class_Vector4i_property_z"></span>

[int](class_int.md#class_int) **z** = `0` [🔗](class_vector4i.md#class_Vector4i_property_z)

The vector's Z component. Also accessible by using the index position `[2]`.

---

### Constructor Descriptions

<span id="class_Vector4i_constructor_Vector4i"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **Vector4i** ( ) [🔗](class_vector4i.md#class_Vector4i_constructor_Vector4i)

Constructs a default-initialized **Vector4i** with all components set to `0`.

---

[Vector4i](class_vector4i.md#class_Vector4i) **Vector4i** ( from: [Vector4i](class_vector4i.md#class_Vector4i) )

Constructs a **Vector4i** as a copy of the given **Vector4i**.

---

[Vector4i](class_vector4i.md#class_Vector4i) **Vector4i** ( from: [Vector4](class_vector4.md#class_Vector4) )

Constructs a new **Vector4i** from the given [Vector4](class_vector4.md#class_Vector4) by truncating components' fractional parts (rounding towards zero). For a different behavior consider passing the result of [Vector4.ceil()](class_vector4.md#class_Vector4_method_ceil), [Vector4.floor()](class_vector4.md#class_Vector4_method_floor) or [Vector4.round()](class_vector4.md#class_Vector4_method_round) to this constructor instead.

---

[Vector4i](class_vector4i.md#class_Vector4i) **Vector4i** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int), z: [int](class_int.md#class_int), w: [int](class_int.md#class_int) )

Returns a **Vector4i** with the given components.

---

### Method Descriptions

<span id="class_Vector4i_method_abs"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **abs** ( ) *const* [🔗](class_vector4i.md#class_Vector4i_method_abs)

Returns a new vector with all components in absolute values (i.e. positive).

---

<span id="class_Vector4i_method_clamp"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **clamp** ( min: [Vector4i](class_vector4i.md#class_Vector4i), max: [Vector4i](class_vector4i.md#class_Vector4i) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_clamp)

Returns a new vector with all components clamped between the components of `min` and `max`, by running @GlobalScope.clamp() on each component.

---

<span id="class_Vector4i_method_clampi"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **clampi** ( min: [int](class_int.md#class_int), max: [int](class_int.md#class_int) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_clampi)

Returns a new vector with all components clamped between `min` and `max`, by running @GlobalScope.clamp() on each component.

---

<span id="class_Vector4i_method_distance_squared_to"></span>

[int](class_int.md#class_int) **distance_squared_to** ( to: [Vector4i](class_vector4i.md#class_Vector4i) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_distance_squared_to)

Returns the squared distance between this vector and `to`.

This method runs faster than [distance_to()](class_vector4i.md#class_Vector4i_method_distance_to), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

<span id="class_Vector4i_method_distance_to"></span>

[float](class_float.md#class_float) **distance_to** ( to: [Vector4i](class_vector4i.md#class_Vector4i) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_distance_to)

Returns the distance between this vector and `to`.

---

<span id="class_Vector4i_method_length"></span>

[float](class_float.md#class_float) **length** ( ) *const* [🔗](class_vector4i.md#class_Vector4i_method_length)

Returns the length (magnitude) of this vector.

---

<span id="class_Vector4i_method_length_squared"></span>

[int](class_int.md#class_int) **length_squared** ( ) *const* [🔗](class_vector4i.md#class_Vector4i_method_length_squared)

Returns the squared length (squared magnitude) of this vector.

This method runs faster than [length()](class_vector4i.md#class_Vector4i_method_length), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

<span id="class_Vector4i_method_max"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **max** ( with: [Vector4i](class_vector4i.md#class_Vector4i) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_max)

Returns the component-wise maximum of this and `with`, equivalent to `Vector4i(maxi(x, with.x), maxi(y, with.y), maxi(z, with.z), maxi(w, with.w))`.

---

<span id="class_Vector4i_method_max_axis_index"></span>

[int](class_int.md#class_int) **max_axis_index** ( ) *const* [🔗](class_vector4i.md#class_Vector4i_method_max_axis_index)

Returns the axis of the vector's highest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_X](class_vector4i.md#class_Vector4i_constant_AXIS_X).

---

<span id="class_Vector4i_method_maxi"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **maxi** ( with: [int](class_int.md#class_int) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_maxi)

Returns the component-wise maximum of this and `with`, equivalent to `Vector4i(maxi(x, with), maxi(y, with), maxi(z, with), maxi(w, with))`.

---

<span id="class_Vector4i_method_min"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **min** ( with: [Vector4i](class_vector4i.md#class_Vector4i) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_min)

Returns the component-wise minimum of this and `with`, equivalent to `Vector4i(mini(x, with.x), mini(y, with.y), mini(z, with.z), mini(w, with.w))`.

---

<span id="class_Vector4i_method_min_axis_index"></span>

[int](class_int.md#class_int) **min_axis_index** ( ) *const* [🔗](class_vector4i.md#class_Vector4i_method_min_axis_index)

Returns the axis of the vector's lowest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_W](class_vector4i.md#class_Vector4i_constant_AXIS_W).

---

<span id="class_Vector4i_method_mini"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **mini** ( with: [int](class_int.md#class_int) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_mini)

Returns the component-wise minimum of this and `with`, equivalent to `Vector4i(mini(x, with), mini(y, with), mini(z, with), mini(w, with))`.

---

<span id="class_Vector4i_method_sign"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **sign** ( ) *const* [🔗](class_vector4i.md#class_Vector4i_method_sign)

Returns a new vector with each component set to `1` if it's positive, `-1` if it's negative, and `0` if it's zero. The result is identical to calling @GlobalScope.sign() on each component.

---

<span id="class_Vector4i_method_snapped"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **snapped** ( step: [Vector4i](class_vector4i.md#class_Vector4i) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_snapped)

Returns a new vector with each component snapped to the closest multiple of the corresponding component in `step`.

---

<span id="class_Vector4i_method_snappedi"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **snappedi** ( step: [int](class_int.md#class_int) ) *const* [🔗](class_vector4i.md#class_Vector4i_method_snappedi)

Returns a new vector with each component snapped to the closest multiple of `step`.

---

### Operator Descriptions

<span id="class_Vector4i_operator_neq_Vector4i"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_neq_Vector4i)

Returns `true` if the vectors are not equal.

---

<span id="class_Vector4i_operator_mod_Vector4i"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator %** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_mod_Vector4i)

Gets the remainder of each component of the **Vector4i** with the components of the given **Vector4i**. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using @GlobalScope.posmod() instead if you want to handle negative numbers.

::

    print(Vector4i(10, -20, 30, -40) % Vector4i(7, 8, 9, 10)) # Prints (3, -4, 3, 0)

---

<span id="class_Vector4i_operator_mod_int"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator %** ( right: [int](class_int.md#class_int) ) [🔗](class_vector4i.md#class_Vector4i_operator_mod_int)

Gets the remainder of each component of the **Vector4i** with the given [int](class_int.md#class_int). This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using @GlobalScope.posmod() instead if you want to handle negative numbers.

::

    print(Vector4i(10, -20, 30, -40) % 7) # Prints (3, -6, 2, -5)

---

<span id="class_Vector4i_operator_mul_Vector4i"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator *** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_mul_Vector4i)

Multiplies each component of the **Vector4i** by the components of the given **Vector4i**.

::

    print(Vector4i(10, 20, 30, 40) * Vector4i(3, 4, 5, 6)) # Prints (30, 80, 150, 240)

---

<span id="class_Vector4i_operator_mul_float"></span>

[Vector4](class_vector4.md#class_Vector4) **operator *** ( right: [float](class_float.md#class_float) ) [🔗](class_vector4i.md#class_Vector4i_operator_mul_float)

Multiplies each component of the **Vector4i** by the given [float](class_float.md#class_float).

Returns a Vector4 value due to floating-point operations.

::

    print(Vector4i(10, 20, 30, 40) * 2) # Prints (20.0, 40.0, 60.0, 80.0)

---

<span id="class_Vector4i_operator_mul_int"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator *** ( right: [int](class_int.md#class_int) ) [🔗](class_vector4i.md#class_Vector4i_operator_mul_int)

Multiplies each component of the **Vector4i** by the given [int](class_int.md#class_int).

---

<span id="class_Vector4i_operator_sum_Vector4i"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator +** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_sum_Vector4i)

Adds each component of the **Vector4i** by the components of the given **Vector4i**.

::

    print(Vector4i(10, 20, 30, 40) + Vector4i(3, 4, 5, 6)) # Prints (13, 24, 35, 46)

---

<span id="class_Vector4i_operator_dif_Vector4i"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator -** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_dif_Vector4i)

Subtracts each component of the **Vector4i** by the components of the given **Vector4i**.

::

    print(Vector4i(10, 20, 30, 40) - Vector4i(3, 4, 5, 6)) # Prints (7, 16, 25, 34)

---

<span id="class_Vector4i_operator_div_Vector4i"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator /** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_div_Vector4i)

Divides each component of the **Vector4i** by the components of the given **Vector4i**.

::

    print(Vector4i(10, 20, 30, 40) / Vector4i(2, 5, 3, 4)) # Prints (5, 4, 10, 10)

---

<span id="class_Vector4i_operator_div_float"></span>

[Vector4](class_vector4.md#class_Vector4) **operator /** ( right: [float](class_float.md#class_float) ) [🔗](class_vector4i.md#class_Vector4i_operator_div_float)

Divides each component of the **Vector4i** by the given [float](class_float.md#class_float).

Returns a Vector4 value due to floating-point operations.

::

    print(Vector4i(1, 2, 3, 4) / 2.5) # Prints (0.4, 0.8, 1.2, 1.6)

---

<span id="class_Vector4i_operator_div_int"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator /** ( right: [int](class_int.md#class_int) ) [🔗](class_vector4i.md#class_Vector4i_operator_div_int)

Divides each component of the **Vector4i** by the given [int](class_int.md#class_int).

---

<span id="class_Vector4i_operator_lt_Vector4i"></span>

[bool](class_bool.md#class_bool) **operator <** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_lt_Vector4i)

Compares two **Vector4i** vectors by first checking if the X value of the left vector is less than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

---

<span id="class_Vector4i_operator_lte_Vector4i"></span>

[bool](class_bool.md#class_bool) **operator <=** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_lte_Vector4i)

Compares two **Vector4i** vectors by first checking if the X value of the left vector is less than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

---

<span id="class_Vector4i_operator_eq_Vector4i"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_eq_Vector4i)

Returns `true` if the vectors are exactly equal.

---

<span id="class_Vector4i_operator_gt_Vector4i"></span>

[bool](class_bool.md#class_bool) **operator >** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_gt_Vector4i)

Compares two **Vector4i** vectors by first checking if the X value of the left vector is greater than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

---

<span id="class_Vector4i_operator_gte_Vector4i"></span>

[bool](class_bool.md#class_bool) **operator >=** ( right: [Vector4i](class_vector4i.md#class_Vector4i) ) [🔗](class_vector4i.md#class_Vector4i_operator_gte_Vector4i)

Compares two **Vector4i** vectors by first checking if the X value of the left vector is greater than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

---

<span id="class_Vector4i_operator_idx_int"></span>

[int](class_int.md#class_int) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_vector4i.md#class_Vector4i_operator_idx_int)

Access vector components using their `index`. `v[0]` is equivalent to `v.x`, `v[1]` is equivalent to `v.y`, `v[2]` is equivalent to `v.z`, and `v[3]` is equivalent to `v.w`.

---

<span id="class_Vector4i_operator_unplus"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator unary+** ( ) [🔗](class_vector4i.md#class_Vector4i_operator_unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

<span id="class_Vector4i_operator_unminus"></span>

[Vector4i](class_vector4i.md#class_Vector4i) **operator unary-** ( ) [🔗](class_vector4i.md#class_Vector4i_operator_unminus)

Returns the negative value of the **Vector4i**. This is the same as writing `Vector4i(-v.x, -v.y, -v.z, -v.w)`. This operation flips the direction of the vector while keeping the same magnitude.
