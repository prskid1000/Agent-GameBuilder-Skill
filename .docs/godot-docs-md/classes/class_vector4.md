<span id="class_Vector4"></span>

## Vector4

A 4D vector using floating-point coordinates.

### Description

A 4-element structure that can be used to represent 4D coordinates or any other quadruplet of numeric values.

It uses floating-point coordinates. By default, these floating-point values use 32-bit precision, unlike [float](class_float.md#class_float) which is always 64-bit. If double precision is needed, compile the engine with the option `precision=double`.

See [Vector4i](class_vector4i.md#class_Vector4i) for its integer counterpart.

 **Note:** In a boolean context, a Vector4 will evaluate to `false` if it's equal to `Vector4(0, 0, 0, 0)`. Otherwise, a Vector4 will always evaluate to `true`.

### Properties


| [float](class_float.md#class_float) | [w](class_vector4.md#class_Vector4_property_w) | `0.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [x](class_vector4.md#class_Vector4_property_x) | `0.0` |
| [float](class_float.md#class_float) | [y](class_vector4.md#class_Vector4_property_y) | `0.0` |
| [float](class_float.md#class_float) | [z](class_vector4.md#class_Vector4_property_z) | `0.0` |

### Constructors


| [Vector4](class_vector4.md#class_Vector4) | [Vector4](class_vector4.md#class_Vector4_constructor_Vector4) ( ) |
| --- | --- |
| [Vector4](class_vector4.md#class_Vector4) | [Vector4](class_vector4.md#class_Vector4_constructor_Vector4) ( from: [Vector4](class_vector4.md#class_Vector4) ) |
| [Vector4](class_vector4.md#class_Vector4) | [Vector4](class_vector4.md#class_Vector4_constructor_Vector4) ( from: [Vector4i](class_vector4i.md#class_Vector4i) ) |
| [Vector4](class_vector4.md#class_Vector4) | [Vector4](class_vector4.md#class_Vector4_constructor_Vector4) ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), z: [float](class_float.md#class_float), w: [float](class_float.md#class_float) ) |

### Methods


| [Vector4](class_vector4.md#class_Vector4) | [abs](class_vector4.md#class_Vector4_method_abs) ( ) const |
| --- | --- |
| [Vector4](class_vector4.md#class_Vector4) | [ceil](class_vector4.md#class_Vector4_method_ceil) ( ) const |
| [Vector4](class_vector4.md#class_Vector4) | [clamp](class_vector4.md#class_Vector4_method_clamp) ( min: [Vector4](class_vector4.md#class_Vector4), max: [Vector4](class_vector4.md#class_Vector4) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [clampf](class_vector4.md#class_Vector4_method_clampf) ( min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [cubic_interpolate](class_vector4.md#class_Vector4_method_cubic_interpolate) ( b: [Vector4](class_vector4.md#class_Vector4), pre_a: [Vector4](class_vector4.md#class_Vector4), post_b: [Vector4](class_vector4.md#class_Vector4), weight: [float](class_float.md#class_float) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [cubic_interpolate_in_time](class_vector4.md#class_Vector4_method_cubic_interpolate_in_time) ( b: [Vector4](class_vector4.md#class_Vector4), pre_a: [Vector4](class_vector4.md#class_Vector4), post_b: [Vector4](class_vector4.md#class_Vector4), weight: [float](class_float.md#class_float), b_t: [float](class_float.md#class_float), pre_a_t: [float](class_float.md#class_float), post_b_t: [float](class_float.md#class_float) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [direction_to](class_vector4.md#class_Vector4_method_direction_to) ( to: [Vector4](class_vector4.md#class_Vector4) ) const |
| [float](class_float.md#class_float) | [distance_squared_to](class_vector4.md#class_Vector4_method_distance_squared_to) ( to: [Vector4](class_vector4.md#class_Vector4) ) const |
| [float](class_float.md#class_float) | [distance_to](class_vector4.md#class_Vector4_method_distance_to) ( to: [Vector4](class_vector4.md#class_Vector4) ) const |
| [float](class_float.md#class_float) | [dot](class_vector4.md#class_Vector4_method_dot) ( with: [Vector4](class_vector4.md#class_Vector4) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [floor](class_vector4.md#class_Vector4_method_floor) ( ) const |
| [Vector4](class_vector4.md#class_Vector4) | [inverse](class_vector4.md#class_Vector4_method_inverse) ( ) const |
| [bool](class_bool.md#class_bool) | [is_equal_approx](class_vector4.md#class_Vector4_method_is_equal_approx) ( to: [Vector4](class_vector4.md#class_Vector4) ) const |
| [bool](class_bool.md#class_bool) | [is_finite](class_vector4.md#class_Vector4_method_is_finite) ( ) const |
| [bool](class_bool.md#class_bool) | [is_normalized](class_vector4.md#class_Vector4_method_is_normalized) ( ) const |
| [bool](class_bool.md#class_bool) | [is_zero_approx](class_vector4.md#class_Vector4_method_is_zero_approx) ( ) const |
| [float](class_float.md#class_float) | [length](class_vector4.md#class_Vector4_method_length) ( ) const |
| [float](class_float.md#class_float) | [length_squared](class_vector4.md#class_Vector4_method_length_squared) ( ) const |
| [Vector4](class_vector4.md#class_Vector4) | [lerp](class_vector4.md#class_Vector4_method_lerp) ( to: [Vector4](class_vector4.md#class_Vector4), weight: [float](class_float.md#class_float) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [max](class_vector4.md#class_Vector4_method_max) ( with: [Vector4](class_vector4.md#class_Vector4) ) const |
| [int](class_int.md#class_int) | [max_axis_index](class_vector4.md#class_Vector4_method_max_axis_index) ( ) const |
| [Vector4](class_vector4.md#class_Vector4) | [maxf](class_vector4.md#class_Vector4_method_maxf) ( with: [float](class_float.md#class_float) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [min](class_vector4.md#class_Vector4_method_min) ( with: [Vector4](class_vector4.md#class_Vector4) ) const |
| [int](class_int.md#class_int) | [min_axis_index](class_vector4.md#class_Vector4_method_min_axis_index) ( ) const |
| [Vector4](class_vector4.md#class_Vector4) | [minf](class_vector4.md#class_Vector4_method_minf) ( with: [float](class_float.md#class_float) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [normalized](class_vector4.md#class_Vector4_method_normalized) ( ) const |
| [Vector4](class_vector4.md#class_Vector4) | [posmod](class_vector4.md#class_Vector4_method_posmod) ( mod: [float](class_float.md#class_float) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [posmodv](class_vector4.md#class_Vector4_method_posmodv) ( modv: [Vector4](class_vector4.md#class_Vector4) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [round](class_vector4.md#class_Vector4_method_round) ( ) const |
| [Vector4](class_vector4.md#class_Vector4) | [sign](class_vector4.md#class_Vector4_method_sign) ( ) const |
| [Vector4](class_vector4.md#class_Vector4) | [snapped](class_vector4.md#class_Vector4_method_snapped) ( step: [Vector4](class_vector4.md#class_Vector4) ) const |
| [Vector4](class_vector4.md#class_Vector4) | [snappedf](class_vector4.md#class_Vector4_method_snappedf) ( step: [float](class_float.md#class_float) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_vector4.md#class_Vector4_operator_neq_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| --- | --- |
| [Vector4](class_vector4.md#class_Vector4) | [operator *](class_vector4.md#class_Vector4_operator_mul_Projection) ( right: [Projection](class_projection.md#class_Projection) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator *](class_vector4.md#class_Vector4_operator_mul_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator *](class_vector4.md#class_Vector4_operator_mul_float) ( right: [float](class_float.md#class_float) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator *](class_vector4.md#class_Vector4_operator_mul_int) ( right: [int](class_int.md#class_int) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator +](class_vector4.md#class_Vector4_operator_sum_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator -](class_vector4.md#class_Vector4_operator_dif_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator /](class_vector4.md#class_Vector4_operator_div_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator /](class_vector4.md#class_Vector4_operator_div_float) ( right: [float](class_float.md#class_float) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator /](class_vector4.md#class_Vector4_operator_div_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_vector4.md#class_Vector4_operator_eq_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [bool](class_bool.md#class_bool) | [operator >](class_vector4.md#class_Vector4_operator_gt_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [bool](class_bool.md#class_bool) | [operator >=](class_vector4.md#class_Vector4_operator_gte_Vector4) ( right: [Vector4](class_vector4.md#class_Vector4) ) |
| [float](class_float.md#class_float) | [operator []](class_vector4.md#class_Vector4_operator_idx_int) ( index: [int](class_int.md#class_int) ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator unary+](class_vector4.md#class_Vector4_operator_unplus) ( ) |
| [Vector4](class_vector4.md#class_Vector4) | [operator unary-](class_vector4.md#class_Vector4_operator_unminus) ( ) |

---

### Enumerations

<span id="enum_Vector4_Axis"></span>

enum **Axis**: [🔗](class_vector4.md#enum_Vector4_Axis)

<span id="class_Vector4_constant_AXIS_X"></span>

[Axis](class_vector4.md#enum_Vector4_Axis) **AXIS_X** = `0`

Enumerated value for the X axis. Returned by [max_axis_index()](class_vector4.md#class_Vector4_method_max_axis_index) and [min_axis_index()](class_vector4.md#class_Vector4_method_min_axis_index).

<span id="class_Vector4_constant_AXIS_Y"></span>

[Axis](class_vector4.md#enum_Vector4_Axis) **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by [max_axis_index()](class_vector4.md#class_Vector4_method_max_axis_index) and [min_axis_index()](class_vector4.md#class_Vector4_method_min_axis_index).

<span id="class_Vector4_constant_AXIS_Z"></span>

[Axis](class_vector4.md#enum_Vector4_Axis) **AXIS_Z** = `2`

Enumerated value for the Z axis. Returned by [max_axis_index()](class_vector4.md#class_Vector4_method_max_axis_index) and [min_axis_index()](class_vector4.md#class_Vector4_method_min_axis_index).

<span id="class_Vector4_constant_AXIS_W"></span>

[Axis](class_vector4.md#enum_Vector4_Axis) **AXIS_W** = `3`

Enumerated value for the W axis. Returned by [max_axis_index()](class_vector4.md#class_Vector4_method_max_axis_index) and [min_axis_index()](class_vector4.md#class_Vector4_method_min_axis_index).

---

### Constants

<span id="class_Vector4_constant_ZERO"></span>

**ZERO** = `Vector4(0, 0, 0, 0)` [🔗](class_vector4.md#class_Vector4_constant_ZERO)

Zero vector, a vector with all components set to `0`.

<span id="class_Vector4_constant_ONE"></span>

**ONE** = `Vector4(1, 1, 1, 1)` [🔗](class_vector4.md#class_Vector4_constant_ONE)

One vector, a vector with all components set to `1`.

<span id="class_Vector4_constant_INF"></span>

**INF** = `Vector4(inf, inf, inf, inf)` [🔗](class_vector4.md#class_Vector4_constant_INF)

Infinity vector, a vector with all components set to @GDScript.INF.

---

### Property Descriptions

<span id="class_Vector4_property_w"></span>

[float](class_float.md#class_float) **w** = `0.0` [🔗](class_vector4.md#class_Vector4_property_w)

The vector's W component. Also accessible by using the index position `[3]`.

---

<span id="class_Vector4_property_x"></span>

[float](class_float.md#class_float) **x** = `0.0` [🔗](class_vector4.md#class_Vector4_property_x)

The vector's X component. Also accessible by using the index position `[0]`.

---

<span id="class_Vector4_property_y"></span>

[float](class_float.md#class_float) **y** = `0.0` [🔗](class_vector4.md#class_Vector4_property_y)

The vector's Y component. Also accessible by using the index position `[1]`.

---

<span id="class_Vector4_property_z"></span>

[float](class_float.md#class_float) **z** = `0.0` [🔗](class_vector4.md#class_Vector4_property_z)

The vector's Z component. Also accessible by using the index position `[2]`.

---

### Constructor Descriptions

<span id="class_Vector4_constructor_Vector4"></span>

[Vector4](class_vector4.md#class_Vector4) **Vector4** ( ) [🔗](class_vector4.md#class_Vector4_constructor_Vector4)

Constructs a default-initialized **Vector4** with all components set to `0`.

---

[Vector4](class_vector4.md#class_Vector4) **Vector4** ( from: [Vector4](class_vector4.md#class_Vector4) )

Constructs a **Vector4** as a copy of the given **Vector4**.

---

[Vector4](class_vector4.md#class_Vector4) **Vector4** ( from: [Vector4i](class_vector4i.md#class_Vector4i) )

Constructs a new **Vector4** from the given [Vector4i](class_vector4i.md#class_Vector4i).

---

[Vector4](class_vector4.md#class_Vector4) **Vector4** ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), z: [float](class_float.md#class_float), w: [float](class_float.md#class_float) )

Returns a **Vector4** with the given components.

---

### Method Descriptions

<span id="class_Vector4_method_abs"></span>

[Vector4](class_vector4.md#class_Vector4) **abs** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_abs)

Returns a new vector with all components in absolute values (i.e. positive).

---

<span id="class_Vector4_method_ceil"></span>

[Vector4](class_vector4.md#class_Vector4) **ceil** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_ceil)

Returns a new vector with all components rounded up (towards positive infinity).

---

<span id="class_Vector4_method_clamp"></span>

[Vector4](class_vector4.md#class_Vector4) **clamp** ( min: [Vector4](class_vector4.md#class_Vector4), max: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_clamp)

Returns a new vector with all components clamped between the components of `min` and `max`, by running @GlobalScope.clamp() on each component.

---

<span id="class_Vector4_method_clampf"></span>

[Vector4](class_vector4.md#class_Vector4) **clampf** ( min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) *const* [🔗](class_vector4.md#class_Vector4_method_clampf)

Returns a new vector with all components clamped between `min` and `max`, by running @GlobalScope.clamp() on each component.

---

<span id="class_Vector4_method_cubic_interpolate"></span>

[Vector4](class_vector4.md#class_Vector4) **cubic_interpolate** ( b: [Vector4](class_vector4.md#class_Vector4), pre_a: [Vector4](class_vector4.md#class_Vector4), post_b: [Vector4](class_vector4.md#class_Vector4), weight: [float](class_float.md#class_float) ) *const* [🔗](class_vector4.md#class_Vector4_method_cubic_interpolate)

Performs a cubic interpolation between this vector and `b` using `pre_a` and `post_b` as handles, and returns the result at position `weight`. `weight` is on the range of 0.0 to 1.0, representing the amount of interpolation.

---

<span id="class_Vector4_method_cubic_interpolate_in_time"></span>

[Vector4](class_vector4.md#class_Vector4) **cubic_interpolate_in_time** ( b: [Vector4](class_vector4.md#class_Vector4), pre_a: [Vector4](class_vector4.md#class_Vector4), post_b: [Vector4](class_vector4.md#class_Vector4), weight: [float](class_float.md#class_float), b_t: [float](class_float.md#class_float), pre_a_t: [float](class_float.md#class_float), post_b_t: [float](class_float.md#class_float) ) *const* [🔗](class_vector4.md#class_Vector4_method_cubic_interpolate_in_time)

Performs a cubic interpolation between this vector and `b` using `pre_a` and `post_b` as handles, and returns the result at position `weight`. `weight` is on the range of 0.0 to 1.0, representing the amount of interpolation.

It can perform smoother interpolation than [cubic_interpolate()](class_vector4.md#class_Vector4_method_cubic_interpolate) by the time values.

---

<span id="class_Vector4_method_direction_to"></span>

[Vector4](class_vector4.md#class_Vector4) **direction_to** ( to: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_direction_to)

Returns the normalized vector pointing from this vector to `to`. This is equivalent to using `(b - a).normalized()`.

---

<span id="class_Vector4_method_distance_squared_to"></span>

[float](class_float.md#class_float) **distance_squared_to** ( to: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_distance_squared_to)

Returns the squared distance between this vector and `to`.

This method runs faster than [distance_to()](class_vector4.md#class_Vector4_method_distance_to), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

<span id="class_Vector4_method_distance_to"></span>

[float](class_float.md#class_float) **distance_to** ( to: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_distance_to)

Returns the distance between this vector and `to`.

---

<span id="class_Vector4_method_dot"></span>

[float](class_float.md#class_float) **dot** ( with: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_dot)

Returns the dot product of this vector and `with`.

---

<span id="class_Vector4_method_floor"></span>

[Vector4](class_vector4.md#class_Vector4) **floor** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_floor)

Returns a new vector with all components rounded down (towards negative infinity).

---

<span id="class_Vector4_method_inverse"></span>

[Vector4](class_vector4.md#class_Vector4) **inverse** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_inverse)

Returns the inverse of the vector. This is the same as `Vector4(1.0 / v.x, 1.0 / v.y, 1.0 / v.z, 1.0 / v.w)`.

---

<span id="class_Vector4_method_is_equal_approx"></span>

[bool](class_bool.md#class_bool) **is_equal_approx** ( to: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_is_equal_approx)

Returns `true` if this vector and `to` are approximately equal, by running @GlobalScope.is_equal_approx() on each component.

---

<span id="class_Vector4_method_is_finite"></span>

[bool](class_bool.md#class_bool) **is_finite** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_is_finite)

Returns `true` if this vector is finite, by calling @GlobalScope.is_finite() on each component.

---

<span id="class_Vector4_method_is_normalized"></span>

[bool](class_bool.md#class_bool) **is_normalized** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_is_normalized)

Returns `true` if the vector is normalized, i.e. its length is approximately equal to 1.

---

<span id="class_Vector4_method_is_zero_approx"></span>

[bool](class_bool.md#class_bool) **is_zero_approx** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_is_zero_approx)

Returns `true` if this vector's values are approximately zero, by running @GlobalScope.is_zero_approx() on each component.

This method is faster than using [is_equal_approx()](class_vector4.md#class_Vector4_method_is_equal_approx) with one value as a zero vector.

---

<span id="class_Vector4_method_length"></span>

[float](class_float.md#class_float) **length** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_length)

Returns the length (magnitude) of this vector.

---

<span id="class_Vector4_method_length_squared"></span>

[float](class_float.md#class_float) **length_squared** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_length_squared)

Returns the squared length (squared magnitude) of this vector.

This method runs faster than [length()](class_vector4.md#class_Vector4_method_length), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

<span id="class_Vector4_method_lerp"></span>

[Vector4](class_vector4.md#class_Vector4) **lerp** ( to: [Vector4](class_vector4.md#class_Vector4), weight: [float](class_float.md#class_float) ) *const* [🔗](class_vector4.md#class_Vector4_method_lerp)

Returns the result of the linear interpolation between this vector and `to` by amount `weight`. `weight` is on the range of `0.0` to `1.0`, representing the amount of interpolation.

---

<span id="class_Vector4_method_max"></span>

[Vector4](class_vector4.md#class_Vector4) **max** ( with: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_max)

Returns the component-wise maximum of this and `with`, equivalent to `Vector4(maxf(x, with.x), maxf(y, with.y), maxf(z, with.z), maxf(w, with.w))`.

---

<span id="class_Vector4_method_max_axis_index"></span>

[int](class_int.md#class_int) **max_axis_index** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_max_axis_index)

Returns the axis of the vector's highest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_X](class_vector4.md#class_Vector4_constant_AXIS_X).

---

<span id="class_Vector4_method_maxf"></span>

[Vector4](class_vector4.md#class_Vector4) **maxf** ( with: [float](class_float.md#class_float) ) *const* [🔗](class_vector4.md#class_Vector4_method_maxf)

Returns the component-wise maximum of this and `with`, equivalent to `Vector4(maxf(x, with), maxf(y, with), maxf(z, with), maxf(w, with))`.

---

<span id="class_Vector4_method_min"></span>

[Vector4](class_vector4.md#class_Vector4) **min** ( with: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_min)

Returns the component-wise minimum of this and `with`, equivalent to `Vector4(minf(x, with.x), minf(y, with.y), minf(z, with.z), minf(w, with.w))`.

---

<span id="class_Vector4_method_min_axis_index"></span>

[int](class_int.md#class_int) **min_axis_index** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_min_axis_index)

Returns the axis of the vector's lowest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_W](class_vector4.md#class_Vector4_constant_AXIS_W).

---

<span id="class_Vector4_method_minf"></span>

[Vector4](class_vector4.md#class_Vector4) **minf** ( with: [float](class_float.md#class_float) ) *const* [🔗](class_vector4.md#class_Vector4_method_minf)

Returns the component-wise minimum of this and `with`, equivalent to `Vector4(minf(x, with), minf(y, with), minf(z, with), minf(w, with))`.

---

<span id="class_Vector4_method_normalized"></span>

[Vector4](class_vector4.md#class_Vector4) **normalized** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_normalized)

Returns the result of scaling the vector to unit length. Equivalent to `v / v.length()`. Returns `(0, 0, 0, 0)` if `v.length() == 0`. See also [is_normalized()](class_vector4.md#class_Vector4_method_is_normalized).

 **Note:** This function may return incorrect values if the input vector length is near zero.

---

<span id="class_Vector4_method_posmod"></span>

[Vector4](class_vector4.md#class_Vector4) **posmod** ( mod: [float](class_float.md#class_float) ) *const* [🔗](class_vector4.md#class_Vector4_method_posmod)

Returns a vector composed of the @GlobalScope.fposmod() of this vector's components and `mod`.

---

<span id="class_Vector4_method_posmodv"></span>

[Vector4](class_vector4.md#class_Vector4) **posmodv** ( modv: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_posmodv)

Returns a vector composed of the @GlobalScope.fposmod() of this vector's components and `modv`'s components.

---

<span id="class_Vector4_method_round"></span>

[Vector4](class_vector4.md#class_Vector4) **round** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_round)

Returns a new vector with all components rounded to the nearest integer, with halfway cases rounded away from zero.

---

<span id="class_Vector4_method_sign"></span>

[Vector4](class_vector4.md#class_Vector4) **sign** ( ) *const* [🔗](class_vector4.md#class_Vector4_method_sign)

Returns a new vector with each component set to `1.0` if it's positive, `-1.0` if it's negative, and `0.0` if it's zero. The result is identical to calling @GlobalScope.sign() on each component.

---

<span id="class_Vector4_method_snapped"></span>

[Vector4](class_vector4.md#class_Vector4) **snapped** ( step: [Vector4](class_vector4.md#class_Vector4) ) *const* [🔗](class_vector4.md#class_Vector4_method_snapped)

Returns a new vector with each component snapped to the nearest multiple of the corresponding component in `step`. This can also be used to round the components to an arbitrary number of decimals.

---

<span id="class_Vector4_method_snappedf"></span>

[Vector4](class_vector4.md#class_Vector4) **snappedf** ( step: [float](class_float.md#class_float) ) *const* [🔗](class_vector4.md#class_Vector4_method_snappedf)

Returns a new vector with each component snapped to the nearest multiple of `step`. This can also be used to round the components to an arbitrary number of decimals.

---

### Operator Descriptions

<span id="class_Vector4_operator_neq_Vector4"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_neq_Vector4)

Returns `true` if the vectors are not equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_vector4.md#class_Vector4_method_is_equal_approx) instead, which is more reliable.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector4_operator_mul_Projection"></span>

[Vector4](class_vector4.md#class_Vector4) **operator *** ( right: [Projection](class_projection.md#class_Projection) ) [🔗](class_vector4.md#class_Vector4_operator_mul_Projection)

Transforms (multiplies) the **Vector4** by the transpose of the given [Projection](class_projection.md#class_Projection) matrix.

For transforming by inverse of a projection `projection.inverse() * vector` can be used instead. See [Projection.inverse()](class_projection.md#class_Projection_method_inverse).

---

<span id="class_Vector4_operator_mul_Vector4"></span>

[Vector4](class_vector4.md#class_Vector4) **operator *** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_mul_Vector4)

Multiplies each component of the **Vector4** by the components of the given **Vector4**.

::

    print(Vector4(10, 20, 30, 40) * Vector4(3, 4, 5, 6)) # Prints (30.0, 80.0, 150.0, 240.0)

---

<span id="class_Vector4_operator_mul_float"></span>

[Vector4](class_vector4.md#class_Vector4) **operator *** ( right: [float](class_float.md#class_float) ) [🔗](class_vector4.md#class_Vector4_operator_mul_float)

Multiplies each component of the **Vector4** by the given [float](class_float.md#class_float).

::

    print(Vector4(10, 20, 30, 40) * 2) # Prints (20.0, 40.0, 60.0, 80.0)

---

<span id="class_Vector4_operator_mul_int"></span>

[Vector4](class_vector4.md#class_Vector4) **operator *** ( right: [int](class_int.md#class_int) ) [🔗](class_vector4.md#class_Vector4_operator_mul_int)

Multiplies each component of the **Vector4** by the given [int](class_int.md#class_int).

---

<span id="class_Vector4_operator_sum_Vector4"></span>

[Vector4](class_vector4.md#class_Vector4) **operator +** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_sum_Vector4)

Adds each component of the **Vector4** by the components of the given **Vector4**.

::

    print(Vector4(10, 20, 30, 40) + Vector4(3, 4, 5, 6)) # Prints (13.0, 24.0, 35.0, 46.0)

---

<span id="class_Vector4_operator_dif_Vector4"></span>

[Vector4](class_vector4.md#class_Vector4) **operator -** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_dif_Vector4)

Subtracts each component of the **Vector4** by the components of the given **Vector4**.

::

    print(Vector4(10, 20, 30, 40) - Vector4(3, 4, 5, 6)) # Prints (7.0, 16.0, 25.0, 34.0)

---

<span id="class_Vector4_operator_div_Vector4"></span>

[Vector4](class_vector4.md#class_Vector4) **operator /** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_div_Vector4)

Divides each component of the **Vector4** by the components of the given **Vector4**.

::

    print(Vector4(10, 20, 30, 40) / Vector4(2, 5, 3, 4)) # Prints (5.0, 4.0, 10.0, 10.0)

---

<span id="class_Vector4_operator_div_float"></span>

[Vector4](class_vector4.md#class_Vector4) **operator /** ( right: [float](class_float.md#class_float) ) [🔗](class_vector4.md#class_Vector4_operator_div_float)

Divides each component of the **Vector4** by the given [float](class_float.md#class_float).

::

    print(Vector4(10, 20, 30, 40) / 2) # Prints (5.0, 10.0, 15.0, 20.0)

---

<span id="class_Vector4_operator_div_int"></span>

[Vector4](class_vector4.md#class_Vector4) **operator /** ( right: [int](class_int.md#class_int) ) [🔗](class_vector4.md#class_Vector4_operator_div_int)

Divides each component of the **Vector4** by the given [int](class_int.md#class_int).

---

<span id="class_Vector4_operator_lt_Vector4"></span>

[bool](class_bool.md#class_bool) **operator <** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_lt_Vector4)

Compares two **Vector4** vectors by first checking if the X value of the left vector is less than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector4_operator_lte_Vector4"></span>

[bool](class_bool.md#class_bool) **operator <=** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_lte_Vector4)

Compares two **Vector4** vectors by first checking if the X value of the left vector is less than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector4_operator_eq_Vector4"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_eq_Vector4)

Returns `true` if the vectors are exactly equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_vector4.md#class_Vector4_method_is_equal_approx) instead, which is more reliable.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector4_operator_gt_Vector4"></span>

[bool](class_bool.md#class_bool) **operator >** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_gt_Vector4)

Compares two **Vector4** vectors by first checking if the X value of the left vector is greater than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector4_operator_gte_Vector4"></span>

[bool](class_bool.md#class_bool) **operator >=** ( right: [Vector4](class_vector4.md#class_Vector4) ) [🔗](class_vector4.md#class_Vector4_operator_gte_Vector4)

Compares two **Vector4** vectors by first checking if the X value of the left vector is greater than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector4_operator_idx_int"></span>

[float](class_float.md#class_float) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_vector4.md#class_Vector4_operator_idx_int)

Access vector components using their `index`. `v[0]` is equivalent to `v.x`, `v[1]` is equivalent to `v.y`, `v[2]` is equivalent to `v.z`, and `v[3]` is equivalent to `v.w`.

---

<span id="class_Vector4_operator_unplus"></span>

[Vector4](class_vector4.md#class_Vector4) **operator unary+** ( ) [🔗](class_vector4.md#class_Vector4_operator_unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

<span id="class_Vector4_operator_unminus"></span>

[Vector4](class_vector4.md#class_Vector4) **operator unary-** ( ) [🔗](class_vector4.md#class_Vector4_operator_unminus)

Returns the negative value of the **Vector4**. This is the same as writing `Vector4(-v.x, -v.y, -v.z, -v.w)`. This operation flips the direction of the vector while keeping the same magnitude. With floats, the number zero can be either positive or negative.
