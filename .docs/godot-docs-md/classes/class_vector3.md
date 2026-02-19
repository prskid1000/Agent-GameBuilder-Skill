<span id="class_Vector3"></span>

## Vector3

A 3D vector using floating-point coordinates.

### Description

A 3-element structure that can be used to represent 3D coordinates or any other triplet of numeric values.

It uses floating-point coordinates. By default, these floating-point values use 32-bit precision, unlike [float](class_float.md#class_float) which is always 64-bit. If double precision is needed, compile the engine with the option `precision=double`.

See [Vector3i](class_vector3i.md#class_Vector3i) for its integer counterpart.

 **Note:** In a boolean context, a Vector3 will evaluate to `false` if it's equal to `Vector3(0, 0, 0)`. Otherwise, a Vector3 will always evaluate to `true`.

### Tutorials

- [Math documentation index](../tutorials/math/index.md)

- [Vector math](../tutorials/math/vector_math.md)

- [Advanced vector math](../tutorials/math/vectors_advanced.md)

- 3Blue1Brown Essence of Linear Algebra

- Matrix Transform Demo

- All 3D Demos

### Properties


| [float](class_float.md#class_float) | [x](class_vector3.md#class_Vector3_property_x) | `0.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [y](class_vector3.md#class_Vector3_property_y) | `0.0` |
| [float](class_float.md#class_float) | [z](class_vector3.md#class_Vector3_property_z) | `0.0` |

### Constructors


| [Vector3](class_vector3.md#class_Vector3) | [Vector3](class_vector3.md#class_Vector3_constructor_Vector3) ( ) |
| --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [Vector3](class_vector3.md#class_Vector3_constructor_Vector3) ( from: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3](class_vector3.md#class_Vector3) | [Vector3](class_vector3.md#class_Vector3_constructor_Vector3) ( from: [Vector3i](class_vector3i.md#class_Vector3i) ) |
| [Vector3](class_vector3.md#class_Vector3) | [Vector3](class_vector3.md#class_Vector3_constructor_Vector3) ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), z: [float](class_float.md#class_float) ) |

### Methods


| [Vector3](class_vector3.md#class_Vector3) | [abs](class_vector3.md#class_Vector3_method_abs) ( ) const |
| --- | --- |
| [float](class_float.md#class_float) | [angle_to](class_vector3.md#class_Vector3_method_angle_to) ( to: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [bezier_derivative](class_vector3.md#class_Vector3_method_bezier_derivative) ( control_1: [Vector3](class_vector3.md#class_Vector3), control_2: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3), t: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [bezier_interpolate](class_vector3.md#class_Vector3_method_bezier_interpolate) ( control_1: [Vector3](class_vector3.md#class_Vector3), control_2: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3), t: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [bounce](class_vector3.md#class_Vector3_method_bounce) ( n: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [ceil](class_vector3.md#class_Vector3_method_ceil) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [clamp](class_vector3.md#class_Vector3_method_clamp) ( min: [Vector3](class_vector3.md#class_Vector3), max: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [clampf](class_vector3.md#class_Vector3_method_clampf) ( min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [cross](class_vector3.md#class_Vector3_method_cross) ( with: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [cubic_interpolate](class_vector3.md#class_Vector3_method_cubic_interpolate) ( b: [Vector3](class_vector3.md#class_Vector3), pre_a: [Vector3](class_vector3.md#class_Vector3), post_b: [Vector3](class_vector3.md#class_Vector3), weight: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [cubic_interpolate_in_time](class_vector3.md#class_Vector3_method_cubic_interpolate_in_time) ( b: [Vector3](class_vector3.md#class_Vector3), pre_a: [Vector3](class_vector3.md#class_Vector3), post_b: [Vector3](class_vector3.md#class_Vector3), weight: [float](class_float.md#class_float), b_t: [float](class_float.md#class_float), pre_a_t: [float](class_float.md#class_float), post_b_t: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [direction_to](class_vector3.md#class_Vector3_method_direction_to) ( to: [Vector3](class_vector3.md#class_Vector3) ) const |
| [float](class_float.md#class_float) | [distance_squared_to](class_vector3.md#class_Vector3_method_distance_squared_to) ( to: [Vector3](class_vector3.md#class_Vector3) ) const |
| [float](class_float.md#class_float) | [distance_to](class_vector3.md#class_Vector3_method_distance_to) ( to: [Vector3](class_vector3.md#class_Vector3) ) const |
| [float](class_float.md#class_float) | [dot](class_vector3.md#class_Vector3_method_dot) ( with: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [floor](class_vector3.md#class_Vector3_method_floor) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [inverse](class_vector3.md#class_Vector3_method_inverse) ( ) const |
| [bool](class_bool.md#class_bool) | [is_equal_approx](class_vector3.md#class_Vector3_method_is_equal_approx) ( to: [Vector3](class_vector3.md#class_Vector3) ) const |
| [bool](class_bool.md#class_bool) | [is_finite](class_vector3.md#class_Vector3_method_is_finite) ( ) const |
| [bool](class_bool.md#class_bool) | [is_normalized](class_vector3.md#class_Vector3_method_is_normalized) ( ) const |
| [bool](class_bool.md#class_bool) | [is_zero_approx](class_vector3.md#class_Vector3_method_is_zero_approx) ( ) const |
| [float](class_float.md#class_float) | [length](class_vector3.md#class_Vector3_method_length) ( ) const |
| [float](class_float.md#class_float) | [length_squared](class_vector3.md#class_Vector3_method_length_squared) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [lerp](class_vector3.md#class_Vector3_method_lerp) ( to: [Vector3](class_vector3.md#class_Vector3), weight: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [limit_length](class_vector3.md#class_Vector3_method_limit_length) ( length: [float](class_float.md#class_float) = 1.0 ) const |
| [Vector3](class_vector3.md#class_Vector3) | [max](class_vector3.md#class_Vector3_method_max) ( with: [Vector3](class_vector3.md#class_Vector3) ) const |
| [int](class_int.md#class_int) | [max_axis_index](class_vector3.md#class_Vector3_method_max_axis_index) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [maxf](class_vector3.md#class_Vector3_method_maxf) ( with: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [min](class_vector3.md#class_Vector3_method_min) ( with: [Vector3](class_vector3.md#class_Vector3) ) const |
| [int](class_int.md#class_int) | [min_axis_index](class_vector3.md#class_Vector3_method_min_axis_index) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [minf](class_vector3.md#class_Vector3_method_minf) ( with: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [move_toward](class_vector3.md#class_Vector3_method_move_toward) ( to: [Vector3](class_vector3.md#class_Vector3), delta: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [normalized](class_vector3.md#class_Vector3_method_normalized) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [octahedron_decode](class_vector3.md#class_Vector3_method_octahedron_decode) ( uv: [Vector2](class_vector2.md#class_Vector2) ) static |
| [Vector2](class_vector2.md#class_Vector2) | [octahedron_encode](class_vector3.md#class_Vector3_method_octahedron_encode) ( ) const |
| [Basis](class_basis.md#class_Basis) | [outer](class_vector3.md#class_Vector3_method_outer) ( with: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [posmod](class_vector3.md#class_Vector3_method_posmod) ( mod: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [posmodv](class_vector3.md#class_Vector3_method_posmodv) ( modv: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [project](class_vector3.md#class_Vector3_method_project) ( b: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [reflect](class_vector3.md#class_Vector3_method_reflect) ( n: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [rotated](class_vector3.md#class_Vector3_method_rotated) ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [round](class_vector3.md#class_Vector3_method_round) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [sign](class_vector3.md#class_Vector3_method_sign) ( ) const |
| [float](class_float.md#class_float) | [signed_angle_to](class_vector3.md#class_Vector3_method_signed_angle_to) ( to: [Vector3](class_vector3.md#class_Vector3), axis: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [slerp](class_vector3.md#class_Vector3_method_slerp) ( to: [Vector3](class_vector3.md#class_Vector3), weight: [float](class_float.md#class_float) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [slide](class_vector3.md#class_Vector3_method_slide) ( n: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [snapped](class_vector3.md#class_Vector3_method_snapped) ( step: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [snappedf](class_vector3.md#class_Vector3_method_snappedf) ( step: [float](class_float.md#class_float) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_vector3.md#class_Vector3_operator_neq_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_vector3.md#class_Vector3_operator_mul_Basis) ( right: [Basis](class_basis.md#class_Basis) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_vector3.md#class_Vector3_operator_mul_Quaternion) ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_vector3.md#class_Vector3_operator_mul_Transform3D) ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_vector3.md#class_Vector3_operator_mul_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_vector3.md#class_Vector3_operator_mul_float) ( right: [float](class_float.md#class_float) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator *](class_vector3.md#class_Vector3_operator_mul_int) ( right: [int](class_int.md#class_int) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator +](class_vector3.md#class_Vector3_operator_sum_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator -](class_vector3.md#class_Vector3_operator_dif_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator /](class_vector3.md#class_Vector3_operator_div_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator /](class_vector3.md#class_Vector3_operator_div_float) ( right: [float](class_float.md#class_float) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator /](class_vector3.md#class_Vector3_operator_div_int) ( right: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [bool](class_bool.md#class_bool) | operator \ ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_vector3.md#class_Vector3_operator_eq_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [bool](class_bool.md#class_bool) | [operator >](class_vector3.md#class_Vector3_operator_gt_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [bool](class_bool.md#class_bool) | [operator >=](class_vector3.md#class_Vector3_operator_gte_Vector3) ( right: [Vector3](class_vector3.md#class_Vector3) ) |
| [float](class_float.md#class_float) | [operator []](class_vector3.md#class_Vector3_operator_idx_int) ( index: [int](class_int.md#class_int) ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator unary+](class_vector3.md#class_Vector3_operator_unplus) ( ) |
| [Vector3](class_vector3.md#class_Vector3) | [operator unary-](class_vector3.md#class_Vector3_operator_unminus) ( ) |

---

### Enumerations

<span id="enum_Vector3_Axis"></span>

enum **Axis**: [🔗](class_vector3.md#enum_Vector3_Axis)

<span id="class_Vector3_constant_AXIS_X"></span>

[Axis](class_vector3.md#enum_Vector3_Axis) **AXIS_X** = `0`

Enumerated value for the X axis. Returned by [max_axis_index()](class_vector3.md#class_Vector3_method_max_axis_index) and [min_axis_index()](class_vector3.md#class_Vector3_method_min_axis_index).

<span id="class_Vector3_constant_AXIS_Y"></span>

[Axis](class_vector3.md#enum_Vector3_Axis) **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by [max_axis_index()](class_vector3.md#class_Vector3_method_max_axis_index) and [min_axis_index()](class_vector3.md#class_Vector3_method_min_axis_index).

<span id="class_Vector3_constant_AXIS_Z"></span>

[Axis](class_vector3.md#enum_Vector3_Axis) **AXIS_Z** = `2`

Enumerated value for the Z axis. Returned by [max_axis_index()](class_vector3.md#class_Vector3_method_max_axis_index) and [min_axis_index()](class_vector3.md#class_Vector3_method_min_axis_index).

---

### Constants

<span id="class_Vector3_constant_ZERO"></span>

**ZERO** = `Vector3(0, 0, 0)` [🔗](class_vector3.md#class_Vector3_constant_ZERO)

Zero vector, a vector with all components set to `0`.

<span id="class_Vector3_constant_ONE"></span>

**ONE** = `Vector3(1, 1, 1)` [🔗](class_vector3.md#class_Vector3_constant_ONE)

One vector, a vector with all components set to `1`.

<span id="class_Vector3_constant_INF"></span>

**INF** = `Vector3(inf, inf, inf)` [🔗](class_vector3.md#class_Vector3_constant_INF)

Infinity vector, a vector with all components set to @GDScript.INF.

<span id="class_Vector3_constant_LEFT"></span>

**LEFT** = `Vector3(-1, 0, 0)` [🔗](class_vector3.md#class_Vector3_constant_LEFT)

Left unit vector. Represents the local direction of left, and the global direction of west.

<span id="class_Vector3_constant_RIGHT"></span>

**RIGHT** = `Vector3(1, 0, 0)` [🔗](class_vector3.md#class_Vector3_constant_RIGHT)

Right unit vector. Represents the local direction of right, and the global direction of east.

<span id="class_Vector3_constant_UP"></span>

**UP** = `Vector3(0, 1, 0)` [🔗](class_vector3.md#class_Vector3_constant_UP)

Up unit vector.

<span id="class_Vector3_constant_DOWN"></span>

**DOWN** = `Vector3(0, -1, 0)` [🔗](class_vector3.md#class_Vector3_constant_DOWN)

Down unit vector.

<span id="class_Vector3_constant_FORWARD"></span>

**FORWARD** = `Vector3(0, 0, -1)` [🔗](class_vector3.md#class_Vector3_constant_FORWARD)

Forward unit vector. Represents the local direction of forward, and the global direction of north. Keep in mind that the forward direction for lights, cameras, etc is different from 3D assets like characters, which face towards the camera by convention. Use [MODEL_FRONT](class_vector3.md#class_Vector3_constant_MODEL_FRONT) and similar constants when working in 3D asset space.

<span id="class_Vector3_constant_BACK"></span>

**BACK** = `Vector3(0, 0, 1)` [🔗](class_vector3.md#class_Vector3_constant_BACK)

Back unit vector. Represents the local direction of back, and the global direction of south.

<span id="class_Vector3_constant_MODEL_LEFT"></span>

**MODEL_LEFT** = `Vector3(1, 0, 0)` [🔗](class_vector3.md#class_Vector3_constant_MODEL_LEFT)

Unit vector pointing towards the left side of imported 3D assets.

<span id="class_Vector3_constant_MODEL_RIGHT"></span>

**MODEL_RIGHT** = `Vector3(-1, 0, 0)` [🔗](class_vector3.md#class_Vector3_constant_MODEL_RIGHT)

Unit vector pointing towards the right side of imported 3D assets.

<span id="class_Vector3_constant_MODEL_TOP"></span>

**MODEL_TOP** = `Vector3(0, 1, 0)` [🔗](class_vector3.md#class_Vector3_constant_MODEL_TOP)

Unit vector pointing towards the top side (up) of imported 3D assets.

<span id="class_Vector3_constant_MODEL_BOTTOM"></span>

**MODEL_BOTTOM** = `Vector3(0, -1, 0)` [🔗](class_vector3.md#class_Vector3_constant_MODEL_BOTTOM)

Unit vector pointing towards the bottom side (down) of imported 3D assets.

<span id="class_Vector3_constant_MODEL_FRONT"></span>

**MODEL_FRONT** = `Vector3(0, 0, 1)` [🔗](class_vector3.md#class_Vector3_constant_MODEL_FRONT)

Unit vector pointing towards the front side (facing forward) of imported 3D assets.

<span id="class_Vector3_constant_MODEL_REAR"></span>

**MODEL_REAR** = `Vector3(0, 0, -1)` [🔗](class_vector3.md#class_Vector3_constant_MODEL_REAR)

Unit vector pointing towards the rear side (back) of imported 3D assets.

---

### Property Descriptions

<span id="class_Vector3_property_x"></span>

[float](class_float.md#class_float) **x** = `0.0` [🔗](class_vector3.md#class_Vector3_property_x)

The vector's X component. Also accessible by using the index position `[0]`.

---

<span id="class_Vector3_property_y"></span>

[float](class_float.md#class_float) **y** = `0.0` [🔗](class_vector3.md#class_Vector3_property_y)

The vector's Y component. Also accessible by using the index position `[1]`.

---

<span id="class_Vector3_property_z"></span>

[float](class_float.md#class_float) **z** = `0.0` [🔗](class_vector3.md#class_Vector3_property_z)

The vector's Z component. Also accessible by using the index position `[2]`.

---

### Constructor Descriptions

<span id="class_Vector3_constructor_Vector3"></span>

[Vector3](class_vector3.md#class_Vector3) **Vector3** ( ) [🔗](class_vector3.md#class_Vector3_constructor_Vector3)

Constructs a default-initialized **Vector3** with all components set to `0`.

---

[Vector3](class_vector3.md#class_Vector3) **Vector3** ( from: [Vector3](class_vector3.md#class_Vector3) )

Constructs a **Vector3** as a copy of the given **Vector3**.

---

[Vector3](class_vector3.md#class_Vector3) **Vector3** ( from: [Vector3i](class_vector3i.md#class_Vector3i) )

Constructs a new **Vector3** from [Vector3i](class_vector3i.md#class_Vector3i).

---

[Vector3](class_vector3.md#class_Vector3) **Vector3** ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), z: [float](class_float.md#class_float) )

Returns a **Vector3** with the given components.

---

### Method Descriptions

<span id="class_Vector3_method_abs"></span>

[Vector3](class_vector3.md#class_Vector3) **abs** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_abs)

Returns a new vector with all components in absolute values (i.e. positive).

---

<span id="class_Vector3_method_angle_to"></span>

[float](class_float.md#class_float) **angle_to** ( to: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_angle_to)

Returns the unsigned minimum angle to the given vector, in radians.

---

<span id="class_Vector3_method_bezier_derivative"></span>

[Vector3](class_vector3.md#class_Vector3) **bezier_derivative** ( control_1: [Vector3](class_vector3.md#class_Vector3), control_2: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3), t: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_bezier_derivative)

Returns the derivative at the given `t` on the Bézier curve defined by this vector and the given `control_1`, `control_2`, and `end` points.

---

<span id="class_Vector3_method_bezier_interpolate"></span>

[Vector3](class_vector3.md#class_Vector3) **bezier_interpolate** ( control_1: [Vector3](class_vector3.md#class_Vector3), control_2: [Vector3](class_vector3.md#class_Vector3), end: [Vector3](class_vector3.md#class_Vector3), t: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_bezier_interpolate)

Returns the point at the given `t` on the Bézier curve defined by this vector and the given `control_1`, `control_2`, and `end` points.

---

<span id="class_Vector3_method_bounce"></span>

[Vector3](class_vector3.md#class_Vector3) **bounce** ( n: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_bounce)

Returns the vector "bounced off" from a plane defined by the given normal `n`.

 **Note:** [bounce()](class_vector3.md#class_Vector3_method_bounce) performs the operation that most engines and frameworks call `reflect()`.

---

<span id="class_Vector3_method_ceil"></span>

[Vector3](class_vector3.md#class_Vector3) **ceil** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_ceil)

Returns a new vector with all components rounded up (towards positive infinity).

---

<span id="class_Vector3_method_clamp"></span>

[Vector3](class_vector3.md#class_Vector3) **clamp** ( min: [Vector3](class_vector3.md#class_Vector3), max: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_clamp)

Returns a new vector with all components clamped between the components of `min` and `max`, by running @GlobalScope.clamp() on each component.

---

<span id="class_Vector3_method_clampf"></span>

[Vector3](class_vector3.md#class_Vector3) **clampf** ( min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_clampf)

Returns a new vector with all components clamped between `min` and `max`, by running @GlobalScope.clamp() on each component.

---

<span id="class_Vector3_method_cross"></span>

[Vector3](class_vector3.md#class_Vector3) **cross** ( with: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_cross)

Returns the cross product of this vector and `with`.

This returns a vector perpendicular to both this and `with`, which would be the normal vector of the plane defined by the two vectors. As there are two such vectors, in opposite directions, this method returns the vector defined by a right-handed coordinate system. If the two vectors are parallel this returns an empty vector, making it useful for testing if two vectors are parallel.

---

<span id="class_Vector3_method_cubic_interpolate"></span>

[Vector3](class_vector3.md#class_Vector3) **cubic_interpolate** ( b: [Vector3](class_vector3.md#class_Vector3), pre_a: [Vector3](class_vector3.md#class_Vector3), post_b: [Vector3](class_vector3.md#class_Vector3), weight: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_cubic_interpolate)

Performs a cubic interpolation between this vector and `b` using `pre_a` and `post_b` as handles, and returns the result at position `weight`. `weight` is on the range of 0.0 to 1.0, representing the amount of interpolation.

---

<span id="class_Vector3_method_cubic_interpolate_in_time"></span>

[Vector3](class_vector3.md#class_Vector3) **cubic_interpolate_in_time** ( b: [Vector3](class_vector3.md#class_Vector3), pre_a: [Vector3](class_vector3.md#class_Vector3), post_b: [Vector3](class_vector3.md#class_Vector3), weight: [float](class_float.md#class_float), b_t: [float](class_float.md#class_float), pre_a_t: [float](class_float.md#class_float), post_b_t: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_cubic_interpolate_in_time)

Performs a cubic interpolation between this vector and `b` using `pre_a` and `post_b` as handles, and returns the result at position `weight`. `weight` is on the range of 0.0 to 1.0, representing the amount of interpolation.

It can perform smoother interpolation than [cubic_interpolate()](class_vector3.md#class_Vector3_method_cubic_interpolate) by the time values.

---

<span id="class_Vector3_method_direction_to"></span>

[Vector3](class_vector3.md#class_Vector3) **direction_to** ( to: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_direction_to)

Returns the normalized vector pointing from this vector to `to`. This is equivalent to using `(b - a).normalized()`.

---

<span id="class_Vector3_method_distance_squared_to"></span>

[float](class_float.md#class_float) **distance_squared_to** ( to: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_distance_squared_to)

Returns the squared distance between this vector and `to`.

This method runs faster than [distance_to()](class_vector3.md#class_Vector3_method_distance_to), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

<span id="class_Vector3_method_distance_to"></span>

[float](class_float.md#class_float) **distance_to** ( to: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_distance_to)

Returns the distance between this vector and `to`.

---

<span id="class_Vector3_method_dot"></span>

[float](class_float.md#class_float) **dot** ( with: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_dot)

Returns the dot product of this vector and `with`. This can be used to compare the angle between two vectors. For example, this can be used to determine whether an enemy is facing the player.

The dot product will be `0` for a right angle (90 degrees), greater than 0 for angles narrower than 90 degrees and lower than 0 for angles wider than 90 degrees.

When using unit (normalized) vectors, the result will always be between `-1.0` (180 degree angle) when the vectors are facing opposite directions, and `1.0` (0 degree angle) when the vectors are aligned.

 **Note:** `a.dot(b)` is equivalent to `b.dot(a)`.

---

<span id="class_Vector3_method_floor"></span>

[Vector3](class_vector3.md#class_Vector3) **floor** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_floor)

Returns a new vector with all components rounded down (towards negative infinity).

---

<span id="class_Vector3_method_inverse"></span>

[Vector3](class_vector3.md#class_Vector3) **inverse** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_inverse)

Returns the inverse of the vector. This is the same as `Vector3(1.0 / v.x, 1.0 / v.y, 1.0 / v.z)`.

---

<span id="class_Vector3_method_is_equal_approx"></span>

[bool](class_bool.md#class_bool) **is_equal_approx** ( to: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_is_equal_approx)

Returns `true` if this vector and `to` are approximately equal, by running @GlobalScope.is_equal_approx() on each component.

---

<span id="class_Vector3_method_is_finite"></span>

[bool](class_bool.md#class_bool) **is_finite** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_is_finite)

Returns `true` if this vector is finite, by calling @GlobalScope.is_finite() on each component.

---

<span id="class_Vector3_method_is_normalized"></span>

[bool](class_bool.md#class_bool) **is_normalized** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_is_normalized)

Returns `true` if the vector is normalized, i.e. its length is approximately equal to 1.

---

<span id="class_Vector3_method_is_zero_approx"></span>

[bool](class_bool.md#class_bool) **is_zero_approx** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_is_zero_approx)

Returns `true` if this vector's values are approximately zero, by running @GlobalScope.is_zero_approx() on each component.

This method is faster than using [is_equal_approx()](class_vector3.md#class_Vector3_method_is_equal_approx) with one value as a zero vector.

---

<span id="class_Vector3_method_length"></span>

[float](class_float.md#class_float) **length** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_length)

Returns the length (magnitude) of this vector.

---

<span id="class_Vector3_method_length_squared"></span>

[float](class_float.md#class_float) **length_squared** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_length_squared)

Returns the squared length (squared magnitude) of this vector.

This method runs faster than [length()](class_vector3.md#class_Vector3_method_length), so prefer it if you need to compare vectors or need the squared distance for some formula.

---

<span id="class_Vector3_method_lerp"></span>

[Vector3](class_vector3.md#class_Vector3) **lerp** ( to: [Vector3](class_vector3.md#class_Vector3), weight: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_lerp)

Returns the result of the linear interpolation between this vector and `to` by amount `weight`. `weight` is on the range of `0.0` to `1.0`, representing the amount of interpolation.

---

<span id="class_Vector3_method_limit_length"></span>

[Vector3](class_vector3.md#class_Vector3) **limit_length** ( length: [float](class_float.md#class_float) = 1.0 ) *const* [🔗](class_vector3.md#class_Vector3_method_limit_length)

Returns the vector with a maximum length by limiting its length to `length`. If the vector is non-finite, the result is undefined.

---

<span id="class_Vector3_method_max"></span>

[Vector3](class_vector3.md#class_Vector3) **max** ( with: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_max)

Returns the component-wise maximum of this and `with`, equivalent to `Vector3(maxf(x, with.x), maxf(y, with.y), maxf(z, with.z))`.

---

<span id="class_Vector3_method_max_axis_index"></span>

[int](class_int.md#class_int) **max_axis_index** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_max_axis_index)

Returns the axis of the vector's highest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_X](class_vector3.md#class_Vector3_constant_AXIS_X).

---

<span id="class_Vector3_method_maxf"></span>

[Vector3](class_vector3.md#class_Vector3) **maxf** ( with: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_maxf)

Returns the component-wise maximum of this and `with`, equivalent to `Vector3(maxf(x, with), maxf(y, with), maxf(z, with))`.

---

<span id="class_Vector3_method_min"></span>

[Vector3](class_vector3.md#class_Vector3) **min** ( with: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_min)

Returns the component-wise minimum of this and `with`, equivalent to `Vector3(minf(x, with.x), minf(y, with.y), minf(z, with.z))`.

---

<span id="class_Vector3_method_min_axis_index"></span>

[int](class_int.md#class_int) **min_axis_index** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_min_axis_index)

Returns the axis of the vector's lowest value. See `AXIS_*` constants. If all components are equal, this method returns [AXIS_Z](class_vector3.md#class_Vector3_constant_AXIS_Z).

---

<span id="class_Vector3_method_minf"></span>

[Vector3](class_vector3.md#class_Vector3) **minf** ( with: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_minf)

Returns the component-wise minimum of this and `with`, equivalent to `Vector3(minf(x, with), minf(y, with), minf(z, with))`.

---

<span id="class_Vector3_method_move_toward"></span>

[Vector3](class_vector3.md#class_Vector3) **move_toward** ( to: [Vector3](class_vector3.md#class_Vector3), delta: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_move_toward)

Returns a new vector moved toward `to` by the fixed `delta` amount. Will not go past the final value.

---

<span id="class_Vector3_method_normalized"></span>

[Vector3](class_vector3.md#class_Vector3) **normalized** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_normalized)

Returns the result of scaling the vector to unit length. Equivalent to `v / v.length()`. Returns `(0, 0, 0)` if `v.length() == 0`. See also [is_normalized()](class_vector3.md#class_Vector3_method_is_normalized).

 **Note:** This function may return incorrect values if the input vector length is near zero.

---

<span id="class_Vector3_method_octahedron_decode"></span>

[Vector3](class_vector3.md#class_Vector3) **octahedron_decode** ( uv: [Vector2](class_vector2.md#class_Vector2) ) *static* [🔗](class_vector3.md#class_Vector3_method_octahedron_decode)

Returns the **Vector3** from an octahedral-compressed form created using [octahedron_encode()](class_vector3.md#class_Vector3_method_octahedron_encode) (stored as a [Vector2](class_vector2.md#class_Vector2)).

---

<span id="class_Vector3_method_octahedron_encode"></span>

[Vector2](class_vector2.md#class_Vector2) **octahedron_encode** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_octahedron_encode)

Returns the octahedral-encoded (oct32) form of this **Vector3** as a [Vector2](class_vector2.md#class_Vector2). Since a [Vector2](class_vector2.md#class_Vector2) occupies 1/3 less memory compared to **Vector3**, this form of compression can be used to pass greater amounts of [normalized()](class_vector3.md#class_Vector3_method_normalized) **Vector3** s without increasing storage or memory requirements. See also [octahedron_decode()](class_vector3.md#class_Vector3_method_octahedron_decode).

 **Note:** [octahedron_encode()](class_vector3.md#class_Vector3_method_octahedron_encode) can only be used for [normalized()](class_vector3.md#class_Vector3_method_normalized) vectors. [octahedron_encode()](class_vector3.md#class_Vector3_method_octahedron_encode) does *not* check whether this **Vector3** is normalized, and will return a value that does not decompress to the original value if the **Vector3** is not normalized.

 **Note:** Octahedral compression is *lossy*, although visual differences are rarely perceptible in real world scenarios.

---

<span id="class_Vector3_method_outer"></span>

[Basis](class_basis.md#class_Basis) **outer** ( with: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_outer)

Returns the outer product with `with`.

---

<span id="class_Vector3_method_posmod"></span>

[Vector3](class_vector3.md#class_Vector3) **posmod** ( mod: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_posmod)

Returns a vector composed of the @GlobalScope.fposmod() of this vector's components and `mod`.

---

<span id="class_Vector3_method_posmodv"></span>

[Vector3](class_vector3.md#class_Vector3) **posmodv** ( modv: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_posmodv)

Returns a vector composed of the @GlobalScope.fposmod() of this vector's components and `modv`'s components.

---

<span id="class_Vector3_method_project"></span>

[Vector3](class_vector3.md#class_Vector3) **project** ( b: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_project)

Returns a new vector resulting from projecting this vector onto the given vector `b`. The resulting new vector is parallel to `b`. See also [slide()](class_vector3.md#class_Vector3_method_slide).

 **Note:** If the vector `b` is a zero vector, the components of the resulting new vector will be @GDScript.NAN.

---

<span id="class_Vector3_method_reflect"></span>

[Vector3](class_vector3.md#class_Vector3) **reflect** ( n: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_reflect)

Returns the result of reflecting the vector through a plane defined by the given normal vector `n`.

 **Note:** [reflect()](class_vector3.md#class_Vector3_method_reflect) differs from what other engines and frameworks call `reflect()`. In other engines, `reflect()` returns the result of the vector reflected by the given plane. The reflection thus passes through the given normal. While in Godot the reflection passes through the plane and can be thought of as bouncing off the normal. See also [bounce()](class_vector3.md#class_Vector3_method_bounce) which does what most engines call `reflect()`.

---

<span id="class_Vector3_method_rotated"></span>

[Vector3](class_vector3.md#class_Vector3) **rotated** ( axis: [Vector3](class_vector3.md#class_Vector3), angle: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_rotated)

Returns the result of rotating this vector around a given axis by `angle` (in radians). The axis must be a normalized vector. See also @GlobalScope.deg_to_rad().

---

<span id="class_Vector3_method_round"></span>

[Vector3](class_vector3.md#class_Vector3) **round** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_round)

Returns a new vector with all components rounded to the nearest integer, with halfway cases rounded away from zero.

---

<span id="class_Vector3_method_sign"></span>

[Vector3](class_vector3.md#class_Vector3) **sign** ( ) *const* [🔗](class_vector3.md#class_Vector3_method_sign)

Returns a new vector with each component set to `1.0` if it's positive, `-1.0` if it's negative, and `0.0` if it's zero. The result is identical to calling @GlobalScope.sign() on each component.

---

<span id="class_Vector3_method_signed_angle_to"></span>

[float](class_float.md#class_float) **signed_angle_to** ( to: [Vector3](class_vector3.md#class_Vector3), axis: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_signed_angle_to)

Returns the signed angle to the given vector, in radians. The sign of the angle is positive in a counter-clockwise direction and negative in a clockwise direction when viewed from the side specified by the `axis`.

---

<span id="class_Vector3_method_slerp"></span>

[Vector3](class_vector3.md#class_Vector3) **slerp** ( to: [Vector3](class_vector3.md#class_Vector3), weight: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_slerp)

Returns the result of spherical linear interpolation between this vector and `to`, by amount `weight`. `weight` is on the range of 0.0 to 1.0, representing the amount of interpolation.

This method also handles interpolating the lengths if the input vectors have different lengths. For the special case of one or both input vectors having zero length, this method behaves like [lerp()](class_vector3.md#class_Vector3_method_lerp).

---

<span id="class_Vector3_method_slide"></span>

[Vector3](class_vector3.md#class_Vector3) **slide** ( n: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_slide)

Returns a new vector resulting from sliding this vector along a plane with normal `n`. The resulting new vector is perpendicular to `n`, and is equivalent to this vector minus its projection on `n`. See also [project()](class_vector3.md#class_Vector3_method_project).

 **Note:** The vector `n` must be normalized. See also [normalized()](class_vector3.md#class_Vector3_method_normalized).

---

<span id="class_Vector3_method_snapped"></span>

[Vector3](class_vector3.md#class_Vector3) **snapped** ( step: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_vector3.md#class_Vector3_method_snapped)

Returns a new vector with each component snapped to the nearest multiple of the corresponding component in `step`. This can also be used to round the components to an arbitrary number of decimals.

---

<span id="class_Vector3_method_snappedf"></span>

[Vector3](class_vector3.md#class_Vector3) **snappedf** ( step: [float](class_float.md#class_float) ) *const* [🔗](class_vector3.md#class_Vector3_method_snappedf)

Returns a new vector with each component snapped to the nearest multiple of `step`. This can also be used to round the components to an arbitrary number of decimals.

---

### Operator Descriptions

<span id="class_Vector3_operator_neq_Vector3"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_neq_Vector3)

Returns `true` if the vectors are not equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_vector3.md#class_Vector3_method_is_equal_approx) instead, which is more reliable.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector3_operator_mul_Basis"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [Basis](class_basis.md#class_Basis) ) [🔗](class_vector3.md#class_Vector3_operator_mul_Basis)

Inversely transforms (multiplies) the **Vector3** by the given [Basis](class_basis.md#class_Basis) matrix, under the assumption that the basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).

 `vector * basis` is equivalent to `basis.transposed() * vector`. See [Basis.transposed()](class_basis.md#class_Basis_method_transposed).

For transforming by inverse of a non-orthonormal basis (e.g. with scaling) `basis.inverse() * vector` can be used instead. See [Basis.inverse()](class_basis.md#class_Basis_method_inverse).

---

<span id="class_Vector3_operator_mul_Quaternion"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [Quaternion](class_quaternion.md#class_Quaternion) ) [🔗](class_vector3.md#class_Vector3_operator_mul_Quaternion)

Inversely transforms (multiplies) the **Vector3** by the given [Quaternion](class_quaternion.md#class_Quaternion).

 `vector * quaternion` is equivalent to `quaternion.inverse() * vector`. See [Quaternion.inverse()](class_quaternion.md#class_Quaternion_method_inverse).

---

<span id="class_Vector3_operator_mul_Transform3D"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_vector3.md#class_Vector3_operator_mul_Transform3D)

Inversely transforms (multiplies) the **Vector3** by the given [Transform3D](class_transform3d.md#class_Transform3D) transformation matrix, under the assumption that the transformation basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).

 `vector * transform` is equivalent to `transform.inverse() * vector`. See [Transform3D.inverse()](class_transform3d.md#class_Transform3D_method_inverse).

For transforming by inverse of an affine transformation (e.g. with scaling) `transform.affine_inverse() * vector` can be used instead. See [Transform3D.affine_inverse()](class_transform3d.md#class_Transform3D_method_affine_inverse).

---

<span id="class_Vector3_operator_mul_Vector3"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_mul_Vector3)

Multiplies each component of the **Vector3** by the components of the given **Vector3**.

::

    print(Vector3(10, 20, 30) * Vector3(3, 4, 5)) # Prints (30.0, 80.0, 150.0)

---

<span id="class_Vector3_operator_mul_float"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [float](class_float.md#class_float) ) [🔗](class_vector3.md#class_Vector3_operator_mul_float)

Multiplies each component of the **Vector3** by the given [float](class_float.md#class_float).

---

<span id="class_Vector3_operator_mul_int"></span>

[Vector3](class_vector3.md#class_Vector3) **operator *** ( right: [int](class_int.md#class_int) ) [🔗](class_vector3.md#class_Vector3_operator_mul_int)

Multiplies each component of the **Vector3** by the given [int](class_int.md#class_int).

---

<span id="class_Vector3_operator_sum_Vector3"></span>

[Vector3](class_vector3.md#class_Vector3) **operator +** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_sum_Vector3)

Adds each component of the **Vector3** by the components of the given **Vector3**.

::

    print(Vector3(10, 20, 30) + Vector3(3, 4, 5)) # Prints (13.0, 24.0, 35.0)

---

<span id="class_Vector3_operator_dif_Vector3"></span>

[Vector3](class_vector3.md#class_Vector3) **operator -** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_dif_Vector3)

Subtracts each component of the **Vector3** by the components of the given **Vector3**.

::

    print(Vector3(10, 20, 30) - Vector3(3, 4, 5)) # Prints (7.0, 16.0, 25.0)

---

<span id="class_Vector3_operator_div_Vector3"></span>

[Vector3](class_vector3.md#class_Vector3) **operator /** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_div_Vector3)

Divides each component of the **Vector3** by the components of the given **Vector3**.

::

    print(Vector3(10, 20, 30) / Vector3(2, 5, 3)) # Prints (5.0, 4.0, 10.0)

---

<span id="class_Vector3_operator_div_float"></span>

[Vector3](class_vector3.md#class_Vector3) **operator /** ( right: [float](class_float.md#class_float) ) [🔗](class_vector3.md#class_Vector3_operator_div_float)

Divides each component of the **Vector3** by the given [float](class_float.md#class_float).

---

<span id="class_Vector3_operator_div_int"></span>

[Vector3](class_vector3.md#class_Vector3) **operator /** ( right: [int](class_int.md#class_int) ) [🔗](class_vector3.md#class_Vector3_operator_div_int)

Divides each component of the **Vector3** by the given [int](class_int.md#class_int).

---

<span id="class_Vector3_operator_lt_Vector3"></span>

[bool](class_bool.md#class_bool) **operator <** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_lt_Vector3)

Compares two **Vector3** vectors by first checking if the X value of the left vector is less than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector3_operator_lte_Vector3"></span>

[bool](class_bool.md#class_bool) **operator <=** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_lte_Vector3)

Compares two **Vector3** vectors by first checking if the X value of the left vector is less than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector3_operator_eq_Vector3"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_eq_Vector3)

Returns `true` if the vectors are exactly equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_vector3.md#class_Vector3_method_is_equal_approx) instead, which is more reliable.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector3_operator_gt_Vector3"></span>

[bool](class_bool.md#class_bool) **operator >** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_gt_Vector3)

Compares two **Vector3** vectors by first checking if the X value of the left vector is greater than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector3_operator_gte_Vector3"></span>

[bool](class_bool.md#class_bool) **operator >=** ( right: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_vector3.md#class_Vector3_operator_gte_Vector3)

Compares two **Vector3** vectors by first checking if the X value of the left vector is greater than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.

 **Note:** Vectors with @GDScript.NAN elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

---

<span id="class_Vector3_operator_idx_int"></span>

[float](class_float.md#class_float) **operator []** ( index: [int](class_int.md#class_int) ) [🔗](class_vector3.md#class_Vector3_operator_idx_int)

Access vector components using their `index`. `v[0]` is equivalent to `v.x`, `v[1]` is equivalent to `v.y`, and `v[2]` is equivalent to `v.z`.

---

<span id="class_Vector3_operator_unplus"></span>

[Vector3](class_vector3.md#class_Vector3) **operator unary+** ( ) [🔗](class_vector3.md#class_Vector3_operator_unplus)

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

---

<span id="class_Vector3_operator_unminus"></span>

[Vector3](class_vector3.md#class_Vector3) **operator unary-** ( ) [🔗](class_vector3.md#class_Vector3_operator_unminus)

Returns the negative value of the **Vector3**. This is the same as writing `Vector3(-v.x, -v.y, -v.z)`. This operation flips the direction of the vector while keeping the same magnitude. With floats, the number zero can be either positive or negative.
