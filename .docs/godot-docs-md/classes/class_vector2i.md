<span id="class_Vector2i"></span>

## Vector2i

A 2D vector using integer coordinates.

### Description

A 2-element structure that can be used to represent 2D grid coordinates or any other pair of integers.

It uses integer coordinates and is therefore preferable to [Vector2](class_vector2.md#class_Vector2) when exact precision is required. Note that the values are limited to 32 bits, and unlike [Vector2](class_vector2.md#class_Vector2) this cannot be configured with an engine build option. Use [int](class_int.md#class_int) or [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) if 64-bit values are needed.

 **Note:** In a boolean context, a Vector2i will evaluate to `false` if it's equal to `Vector2i(0, 0)`. Otherwise, a Vector2i will always evaluate to `true`.

### Tutorials

- [Math documentation index](../tutorials/math/index.md)

- [Vector math](../tutorials/math/vector_math.md)

- 3Blue1Brown Essence of Linear Algebra

### Properties


| [int](class_int.md#class_int) | [x](class_vector2i.md#class_Vector2i_property_x) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [y](class_vector2i.md#class_Vector2i_property_y) | `0` |

### Constructors


| [Vector2i](class_vector2i.md#class_Vector2i) | [Vector2i](class_vector2i.md#class_Vector2i_constructor_Vector2i) ( ) |
| --- | --- |
| [Vector2i](class_vector2i.md#class_Vector2i) | [Vector2i](class_vector2i.md#class_Vector2i_constructor_Vector2i) ( from: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [Vector2i](class_vector2i.md#class_Vector2i_constructor_Vector2i) ( from: [Vector2](class_vector2.md#class_Vector2) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [Vector2i](class_vector2i.md#class_Vector2i_constructor_Vector2i) ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) ) |

### Methods


| [Vector2i](class_vector2i.md#class_Vector2i) | [abs](class_vector2i.md#class_Vector2i_method_abs) ( ) const |
| --- | --- |
| [float](class_float.md#class_float) | [aspect](class_vector2i.md#class_Vector2i_method_aspect) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [clamp](class_vector2i.md#class_Vector2i_method_clamp) ( min: [Vector2i](class_vector2i.md#class_Vector2i), max: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [clampi](class_vector2i.md#class_Vector2i_method_clampi) ( min: [int](class_int.md#class_int), max: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [distance_squared_to](class_vector2i.md#class_Vector2i_method_distance_squared_to) ( to: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [float](class_float.md#class_float) | [distance_to](class_vector2i.md#class_Vector2i_method_distance_to) ( to: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [float](class_float.md#class_float) | [length](class_vector2i.md#class_Vector2i_method_length) ( ) const |
| [int](class_int.md#class_int) | [length_squared](class_vector2i.md#class_Vector2i_method_length_squared) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [max](class_vector2i.md#class_Vector2i_method_max) ( with: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [int](class_int.md#class_int) | [max_axis_index](class_vector2i.md#class_Vector2i_method_max_axis_index) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [maxi](class_vector2i.md#class_Vector2i_method_maxi) ( with: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [min](class_vector2i.md#class_Vector2i_method_min) ( with: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [int](class_int.md#class_int) | [min_axis_index](class_vector2i.md#class_Vector2i_method_min_axis_index) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [mini](class_vector2i.md#class_Vector2i_method_mini) ( with: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [sign](class_vector2i.md#class_Vector2i_method_sign) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [snapped](class_vector2i.md#class_Vector2i_method_snapped) ( step: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [snappedi](class_vector2i.md#class_Vector2i_method_snappedi) ( step: [int](class_int.md#class_int) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_vector2i.md#class_Vector2i_operator_neq_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| --- | --- |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator %](class_vector2i.md#class_Vector2i_operator_mod_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator %](class_vector2i.md#class_Vector2i_operator_mod_int) ( right: [int](class_int.md#class_int) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator *](class_vector2i.md#class_Vector2i_operator_mul_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [Vector2](class_vector2.md#class_Vector2) | [operator *](class_vector2i.md#class_Vector2i_operator_mul_float) ( right: [float](class_float.md#class_float) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator *](class_vector2i.md#class_Vector2i_operator_mul_int) ( right: [int](class_int.md#class_int) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator +](class_vector2i.md#class_Vector2i_operator_sum_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator -](class_vector2i.md#class_Vector2i_operator_dif_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator /](class_vector2i.md#class_Vector2i_operator_div_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [Vector2](class_vector2.md#class_Vector2) | [operator /](class_vector2i.md#class_Vector2i_operator_div_float) ( right: [float](class_float.md#class_float) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator /](class_vector2i.md#class_Vector2i_operator_div_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_vector2i.md#class_Vector2i_operator_eq_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [bool](class_bool.md#class_bool) | [operator >](class_vector2i.md#class_Vector2i_operator_gt_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [bool](class_bool.md#class_bool) | [operator >=](class_vector2i.md#class_Vector2i_operator_gte_Vector2i) ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [int](class_int.md#class_int) | [operator []](class_vector2i.md#class_Vector2i_operator_idx_int) ( index: [int](class_int.md#class_int) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator unary+](class_vector2i.md#class_Vector2i_operator_unplus) ( ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [operator unary-](class_vector2i.md#class_Vector2i_operator_unminus) ( ) |

---

### Enumerations

<span id="enum_Vector2i_Axis"></span>

enum **Axis**: [🔗](class_vector2i.md#enum_Vector2i_Axis)

<span id="class_Vector2i_constant_AXIS_X"></span>

[Axis](class_vector2i.md#enum_Vector2i_Axis) **AXIS_X** = `0`

Enumerated value for the X axis. Returned by [max_axis_index()](class_vector2i.md#class_Vector2i_method_max_axis_index) and [min_axis_index()](class_vector2i.md#class_Vector2i_method_min_axis_index).

<span id="class_Vector2i_constant_AXIS_Y"></span>

[Axis](class_vector2i.md#enum_Vector2i_Axis) **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by [max_axis_index()](class_vector2i.md#class_Vector2i_method_max_axis_index) and [min_axis_index()](class_vector2i.md#class_Vector2i_method_min_axis_index).

---

### Constants

<span id="class_Vector2i_constant_ZERO"></span>

**ZERO** = `Vector2i(0, 0)` [🔗](class_vector2i.md#class_Vector2i_constant_ZERO)

Zero vector, a vector with all components set to `0`.

<span id="class_Vector2i_constant_ONE"></span>

**ONE** = `Vector2i(1, 1)` [🔗](class_vector2i.md#class_Vector2i_constant_ONE)

One vector, a vector with all components set to `1`.

<span id="class_Vector2i_constant_MIN"></span>

**MIN** = `Vector2i(-2147483648, -2147483648)` [🔗](class_vector2i.md#class_Vector2i_constant_MIN)

Min vector, a vector with all components equal to `INT32_MIN`. Can be used as a negative integer equivalent of [Vector2.INF](class_vector2.md#class_Vector2_constant_INF).

<span id="class_Vector2i_constant_MAX"></span>

**MAX** = `Vector2i(2147483647, 2147483647)` [🔗](class_vector2i.md#class_Vector2i_constant_MAX)

Max vector, a vector with all components equal to `INT32_MAX`. Can be used as an integer equivalent of [Vector2.INF](class_vector2.md#class_Vector2_constant_INF).

<span id="class_Vector2i_constant_LEFT"></span>

**LEFT** = `Vector2i(-1, 0)` [🔗](class_vector2i.md#class_Vector2i_constant_LEFT)

Left unit vector. Represents the direction of left.

<span id="class_Vector2i_constant_RIGHT"></span>

**RIGHT** = `Vector2i(1, 0)` [🔗](class_vector2i.md#class_Vector2i_constant_RIGHT)

Right unit vector. Represents the direction of right.

<span id="class_Vector2i_constant_UP"></span>

**UP** = `Vector2i(0, -1)` [🔗](class_vector2i.md#class_Vector2i_constant_UP)

Up unit vector. Y is down in 2D, so this vector points -Y.

<span id="class_Vector2i_constant_DOWN"></span>

**DOWN** = `Vector2i(0, 1)` [🔗](class_vector2i.md#class_Vector2i_constant_DOWN)

Down unit vector. Y is down in 2D, so this vector points +Y.

---

### Property Descriptions

<span id="class_Vector2i_property_x"></span>

[int](class_int.md#class_int) **x** = `0` [🔗](class_vector2i.md#class_Vector2i_property_x)

The vector's X component. Also accessible by using the index position `[0]`.

---

<span id="class_Vector2i_property_y"></span>

[int](class_int.md#class_int) **y** = `0` [🔗](class_vector2i.md#class_Vector2i_property_y)

The vector's Y component. Also accessible by using the index position `[1]`.

---

### Constructor Descriptions

<span id="class_Vector2i_constructor_Vector2i"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **Vector2i** ( ) [🔗](class_vector2i.md#class_Vector2i_constructor_Vector2i)

Constructs a default-initialized **Vector2i** with all components set to `0`.

---

[Vector2i](class_vector2i.md#class_Vector2i) **Vector2i** ( from: [Vector2i](class_vector2i.md#class_Vector2i) )

Constructs a **Vector2i** as a copy of the given **Vector2i**.

---

[Vector2i](class_vector2i.md#class_Vector2i) **Vector2i** ( from: [Vector2](class_vector2.md#class_Vector2) )

Constructs a new **Vector2i** from the given [Vector2](class_vector2.md#class_Vector2) by truncating components' fractional parts (rounding towards zero). For a different behavior consider passing the result of [Vector2.ceil()](class_vector2.md#class_Vector2_method_ceil), [Vector2.floor()](class_vector2.md#class_Vector2_method_floor) or [Vector2.round()](class_vector2.md#class_Vector2_method_round) to this constructor instead.

---

[Vector2i](class_vector2i.md#class_Vector2i) **Vector2i** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int) )

Constructs a new **Vector2i** from the given `x` and `y`.

---

### Method Descriptions

<span id="class_Vector2i_method_abs"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **abs** ( ) *const* [🔗](class_vector2i.md#class_Vector2i_method_abs)

Returns a new vector with all components in absolute values (i.e. positive).

---

<span id="class_Vector2i_method_aspect"></span>

[float](class_float.md#class_float) **aspect** ( ) *const* [🔗](class_vector2i.md#class_Vector2i_method_aspect)

Returns the aspect ratio of this vector, the ratio of [x](class_vector2i.md#class_Vector2i_property_x) to [y](class_vector2i.md#class_Vector2i_property_y).

---

<span id="class_Vector2i_method_clamp"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **clamp** ( min: [Vector2i](class_vector2i.md#class_Vector2i), max: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_clamp)

Returns a new vector with all components clamped between the components of `min` and `max`, by running @GlobalScope.clamp() on each component.

---

<span id="class_Vector2i_method_clampi"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **clampi** ( min: [int](class_int.md#class_int), max: [int](class_int.md#class_int) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_clampi)

Returns a new vector with all components clamped between `min` and `max`, by running @GlobalScope.clamp() on each component.

---

<span id="class_Vector2i_method_distance_squared_to"></span>

[int](class_int.md#class_int) **distance_squared_to** ( to: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_distance_squared_to)

Returns the squared distance between this vector and `to`.

This method runs faster than [distance_to()](class_vector2i.md#class_Vector2i_method_distance_to), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

<span id="class_Vector2i_method_distance_to"></span>

[float](class_float.md#class_float) **distance_to** ( to: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_distance_to)

Returns the distance between this vector and `to`.

---

<span id="class_Vector2i_method_length"></span>

[float](class_float.md#class_float) **length** ( ) *const* [🔗](class_vector2i.md#class_Vector2i_method_length)

Returns the length (magnitude) of this vector.

---

<span id="class_Vector2i_method_length_squared"></span>

[int](class_int.md#class_int) **length_squared** ( ) *const* [🔗](class_vector2i.md#class_Vector2i_method_length_squared)

Returns the squared length (squared magnitude) of this vector.

This method runs faster than [length()](class_vector2i.md#class_Vector2i_method_length), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

<span id="class_Vector2i_method_max"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **max** ( with: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_max)

Returns the component-wise maximum of this and `with`, equivalent to `Vector2i(maxi(x, with.x), maxi(y, with.y))`.

---

<span id="class_Vector2i_method_max_axis_index"></span>

[int](class_int.md#class_int) **max_axis_index** ( ) *const* [🔗](class_vector2i.md#class_Vector2i_method_max_axis_index)

Returns the axis of the vector's highest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_X](class_vector2i.md#class_Vector2i_constant_AXIS_X).

---

<span id="class_Vector2i_method_maxi"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **maxi** ( with: [int](class_int.md#class_int) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_maxi)

Returns the component-wise maximum of this and `with`, equivalent to `Vector2i(maxi(x, with), maxi(y, with))`.

---

<span id="class_Vector2i_method_min"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **min** ( with: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_min)

Returns the component-wise minimum of this and `with`, equivalent to `Vector2i(mini(x, with.x), mini(y, with.y))`.

---

<span id="class_Vector2i_method_min_axis_index"></span>

[int](class_int.md#class_int) **min_axis_index** ( ) *const* [🔗](class_vector2i.md#class_Vector2i_method_min_axis_index)

Returns the axis of the vector's lowest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_Y](class_vector2i.md#class_Vector2i_constant_AXIS_Y).

---

<span id="class_Vector2i_method_mini"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **mini** ( with: [int](class_int.md#class_int) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_mini)

Returns the component-wise minimum of this and `with`, equivalent to `Vector2i(mini(x, with), mini(y, with))`.

---

<span id="class_Vector2i_method_sign"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **sign** ( ) *const* [🔗](class_vector2i.md#class_Vector2i_method_sign)

Returns a new vector with each component set to `1` if it's positive, `-1` if it's negative, and `0` if it's zero. The result is identical to calling @GlobalScope.sign() on each component.

---

<span id="class_Vector2i_method_snapped"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **snapped** ( step: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_snapped)

Returns a new vector with each component snapped to the closest multiple of the corresponding component in `step`.

---

<span id="class_Vector2i_method_snappedi"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **snappedi** ( step: [int](class_int.md#class_int) ) *const* [🔗](class_vector2i.md#class_Vector2i_method_snappedi)

Returns a new vector with each component snapped to the closest multiple of `step`.

---

### Operator Descriptions

<span id="class_Vector2i_operator_neq_Vector2i"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_neq_Vector2i)

Returns `true` if the vectors are not equal.

---

<span id="class_Vector2i_operator_mod_Vector2i"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator %** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_mod_Vector2i)

Gets the remainder of each component of the **Vector2i** with the components of the given **Vector2i**. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using @GlobalScope.posmod() instead if you want to handle negative numbers.

::

    print(Vector2i(10, -20) % Vector2i(7, 8)) # Prints (3, -4)

---

<span id="class_Vector2i_operator_mod_int"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator %** ( right: [int](class_int.md#class_int) ) [🔗](class_vector2i.md#class_Vector2i_operator_mod_int)

Gets the remainder of each component of the **Vector2i** with the given [int](class_int.md#class_int). This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using @GlobalScope.posmod() instead if you want to handle negative numbers.

::

    print(Vector2i(10, -20) % 7) # Prints (3, -6)

---

<span id="class_Vector2i_operator_mul_Vector2i"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator *** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_mul_Vector2i)

Multiplies each component of the **Vector2i** by the components of the given **Vector2i**.

::

    print(Vector2i(10, 20) * Vector2i(3, 4)) # Prints (30, 80)

---

<span id="class_Vector2i_operator_mul_float"></span>

[Vector2](class_vector2.md#class_Vector2) **operator *** ( right: [float](class_float.md#class_float) ) [🔗](class_vector2i.md#class_Vector2i_operator_mul_float)

Multiplies each component of the **Vector2i** by the given [float](class_float.md#class_float). Returns a [Vector2](class_vector2.md#class_Vector2).

::

    print(Vector2i(10, 15) * 0.9) # Prints (9.0, 13.5)

---

<span id="class_Vector2i_operator_mul_int"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator *** ( right: [int](class_int.md#class_int) ) [🔗](class_vector2i.md#class_Vector2i_operator_mul_int)

Multiplies each component of the **Vector2i** by the given [int](class_int.md#class_int).

---

<span id="class_Vector2i_operator_sum_Vector2i"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator +** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_sum_Vector2i)

Adds each component of the **Vector2i** by the components of the given **Vector2i**.

::

    print(Vector2i(10, 20) + Vector2i(3, 4)) # Prints (13, 24)

---

<span id="class_Vector2i_operator_dif_Vector2i"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator -** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_dif_Vector2i)

Subtracts each component of the **Vector2i** by the components of the given **Vector2i**.

::

    print(Vector2i(10, 20) - Vector2i(3, 4)) # Prints (7, 16)

---

<span id="class_Vector2i_operator_div_Vector2i"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator /** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_div_Vector2i)

Divides each component of the **Vector2i** by the components of the given **Vector2i**.

::

    print(Vector2i(10, 20) / Vector2i(2, 5)) # Prints (5, 4)

---

<span id="class_Vector2i_operator_div_float"></span>

[Vector2](class_vector2.md#class_Vector2) **operator /** ( right: [float](class_float.md#class_float) ) [🔗](class_vector2i.md#class_Vector2i_operator_div_float)

Divides each component of the **Vector2i** by the given [float](class_float.md#class_float). Returns a [Vector2](class_vector2.md#class_Vector2).

::

    print(Vector2i(1, 2) / 2.5) # Prints (0.4, 0.8)

---

<span id="class_Vector2i_operator_div_int"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator /** ( right: [int](class_int.md#class_int) ) [🔗](class_vector2i.md#class_Vector2i_operator_div_int)

Divides each component of the **Vector2i** by the given [int](class_int.md#class_int).

---

<span id="class_Vector2i_operator_lt_Vector2i"></span>

[bool](class_bool.md#class_bool) **operator <** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_lt_Vector2i)

Compares two **Vector2i** vectors by first checking if the X value of the left vector is less than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

---

<span id="class_Vector2i_operator_lte_Vector2i"></span>

[bool](class_bool.md#class_bool) **operator <=** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_lte_Vector2i)

Compares two **Vector2i** vectors by first checking if the X value of the left vector is less than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

---

<span id="class_Vector2i_operator_eq_Vector2i"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_eq_Vector2i)

Returns `true` if the vectors are equal.

---

<span id="class_Vector2i_operator_gt_Vector2i"></span>

[bool](class_bool.md#class_bool) **operator >** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_gt_Vector2i)

Compares two **Vector2i** vectors by first checking if the X value of the left vector is greater than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

---

<span id="class_Vector2i_operator_gte_Vector2i"></span>

[bool](class_bool.md#class_bool) **operator >=** ( right: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_vector2i.md#class_Vector2i_operator_gte_Vector2i)

Compares two **Vector2i** vectors by first checking if the X value of the left vector is greater than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

---

<span id="class_Vector2i_operator_idx_int"></span>

[int](class_int.md#class_int) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_vector2i.md#class_Vector2i_operator_idx_int)

Access vector components using their `index`. `v[0]` is equivalent to `v.x`, and `v[1]` is equivalent to `v.y`.

---

<span id="class_Vector2i_operator_unplus"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator unary+** ( ) [🔗](class_vector2i.md#class_Vector2i_operator_unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

<span id="class_Vector2i_operator_unminus"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **operator unary-** ( ) [🔗](class_vector2i.md#class_Vector2i_operator_unminus)

Returns the negative value of the **Vector2i**. This is the same as writing `Vector2i(-v.x, -v.y)`. This operation flips the direction of the vector while keeping the same magnitude.
