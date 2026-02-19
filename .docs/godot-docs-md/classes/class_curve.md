<span id="class_Curve"></span>

## Curve

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A mathematical curve.

### Description

This resource describes a mathematical curve by defining a set of points and tangents at each point. By default, it ranges between `0` and `1` on the X and Y axes, but these ranges can be changed.

Please note that many resources and nodes assume they are given *unit curves*. A unit curve is a curve whose domain (the X axis) is between `0` and `1`. Some examples of unit curve usage are [CPUParticles2D.angle_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_angle_curve) and [Line2D.width_curve](class_line2d.md#class_Line2D_property_width_curve).

### Properties


| [int](class_int.md#class_int) | [bake_resolution](class_curve.md#class_Curve_property_bake_resolution) | `100` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [max_domain](class_curve.md#class_Curve_property_max_domain) | `1.0` |
| [float](class_float.md#class_float) | [max_value](class_curve.md#class_Curve_property_max_value) | `1.0` |
| [float](class_float.md#class_float) | [min_domain](class_curve.md#class_Curve_property_min_domain) | `0.0` |
| [float](class_float.md#class_float) | [min_value](class_curve.md#class_Curve_property_min_value) | `0.0` |
| [int](class_int.md#class_int) | [point_count](class_curve.md#class_Curve_property_point_count) | `0` |

### Methods


| [int](class_int.md#class_int) | [add_point](class_curve.md#class_Curve_method_add_point) ( position: [Vector2](class_vector2.md#class_Vector2), left_tangent: [float](class_float.md#class_float) = 0, right_tangent: [float](class_float.md#class_float) = 0, left_mode: [TangentMode](class_curve.md#enum_Curve_TangentMode) = 0, right_mode: [TangentMode](class_curve.md#enum_Curve_TangentMode) = 0 ) |
| --- | --- |
| void | [bake](class_curve.md#class_Curve_method_bake) ( ) |
| void | [clean_dupes](class_curve.md#class_Curve_method_clean_dupes) ( ) |
| void | [clear_points](class_curve.md#class_Curve_method_clear_points) ( ) |
| [float](class_float.md#class_float) | [get_domain_range](class_curve.md#class_Curve_method_get_domain_range) ( ) const |
| [TangentMode](class_curve.md#enum_Curve_TangentMode) | [get_point_left_mode](class_curve.md#class_Curve_method_get_point_left_mode) ( index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_point_left_tangent](class_curve.md#class_Curve_method_get_point_left_tangent) ( index: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_point_position](class_curve.md#class_Curve_method_get_point_position) ( index: [int](class_int.md#class_int) ) const |
| [TangentMode](class_curve.md#enum_Curve_TangentMode) | [get_point_right_mode](class_curve.md#class_Curve_method_get_point_right_mode) ( index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_point_right_tangent](class_curve.md#class_Curve_method_get_point_right_tangent) ( index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_value_range](class_curve.md#class_Curve_method_get_value_range) ( ) const |
| void | [remove_point](class_curve.md#class_Curve_method_remove_point) ( index: [int](class_int.md#class_int) ) |
| [float](class_float.md#class_float) | [sample](class_curve.md#class_Curve_method_sample) ( offset: [float](class_float.md#class_float) ) const |
| [float](class_float.md#class_float) | [sample_baked](class_curve.md#class_Curve_method_sample_baked) ( offset: [float](class_float.md#class_float) ) const |
| void | [set_point_left_mode](class_curve.md#class_Curve_method_set_point_left_mode) ( index: [int](class_int.md#class_int), mode: [TangentMode](class_curve.md#enum_Curve_TangentMode) ) |
| void | [set_point_left_tangent](class_curve.md#class_Curve_method_set_point_left_tangent) ( index: [int](class_int.md#class_int), tangent: [float](class_float.md#class_float) ) |
| [int](class_int.md#class_int) | [set_point_offset](class_curve.md#class_Curve_method_set_point_offset) ( index: [int](class_int.md#class_int), offset: [float](class_float.md#class_float) ) |
| void | [set_point_right_mode](class_curve.md#class_Curve_method_set_point_right_mode) ( index: [int](class_int.md#class_int), mode: [TangentMode](class_curve.md#enum_Curve_TangentMode) ) |
| void | [set_point_right_tangent](class_curve.md#class_Curve_method_set_point_right_tangent) ( index: [int](class_int.md#class_int), tangent: [float](class_float.md#class_float) ) |
| void | [set_point_value](class_curve.md#class_Curve_method_set_point_value) ( index: [int](class_int.md#class_int), y: [float](class_float.md#class_float) ) |

---

### Signals

<span id="class_Curve_signal_domain_changed"></span>

**domain_changed** ( ) [🔗](class_curve.md#class_Curve_signal_domain_changed)

Emitted when [max_domain](class_curve.md#class_Curve_property_max_domain) or [min_domain](class_curve.md#class_Curve_property_min_domain) is changed.

---

<span id="class_Curve_signal_range_changed"></span>

**range_changed** ( ) [🔗](class_curve.md#class_Curve_signal_range_changed)

Emitted when [max_value](class_curve.md#class_Curve_property_max_value) or [min_value](class_curve.md#class_Curve_property_min_value) is changed.

---

### Enumerations

<span id="enum_Curve_TangentMode"></span>

enum **TangentMode**: [🔗](class_curve.md#enum_Curve_TangentMode)

<span id="class_Curve_constant_TANGENT_FREE"></span>

[TangentMode](class_curve.md#enum_Curve_TangentMode) **TANGENT_FREE** = `0`

The tangent on this side of the point is user-defined.

<span id="class_Curve_constant_TANGENT_LINEAR"></span>

[TangentMode](class_curve.md#enum_Curve_TangentMode) **TANGENT_LINEAR** = `1`

The curve calculates the tangent on this side of the point as the slope halfway towards the adjacent point.

<span id="class_Curve_constant_TANGENT_MODE_COUNT"></span>

[TangentMode](class_curve.md#enum_Curve_TangentMode) **TANGENT_MODE_COUNT** = `2`

The total number of available tangent modes.

---

### Property Descriptions

<span id="class_Curve_property_bake_resolution"></span>

[int](class_int.md#class_int) **bake_resolution** = `100` [🔗](class_curve.md#class_Curve_property_bake_resolution)

- void **set_bake_resolution** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bake_resolution** ( )

The number of points to include in the baked (i.e. cached) curve data.

---

<span id="class_Curve_property_max_domain"></span>

[float](class_float.md#class_float) **max_domain** = `1.0` [🔗](class_curve.md#class_Curve_property_max_domain)

- void **set_max_domain** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max_domain** ( )

The maximum domain (x-coordinate) that points can have.

---

<span id="class_Curve_property_max_value"></span>

[float](class_float.md#class_float) **max_value** = `1.0` [🔗](class_curve.md#class_Curve_property_max_value)

- void **set_max_value** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max_value** ( )

The maximum value (y-coordinate) that points can have. Tangents can cause higher values between points.

---

<span id="class_Curve_property_min_domain"></span>

[float](class_float.md#class_float) **min_domain** = `0.0` [🔗](class_curve.md#class_Curve_property_min_domain)

- void **set_min_domain** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_min_domain** ( )

The minimum domain (x-coordinate) that points can have.

---

<span id="class_Curve_property_min_value"></span>

[float](class_float.md#class_float) **min_value** = `0.0` [🔗](class_curve.md#class_Curve_property_min_value)

- void **set_min_value** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_min_value** ( )

The minimum value (y-coordinate) that points can have. Tangents can cause lower values between points.

---

<span id="class_Curve_property_point_count"></span>

[int](class_int.md#class_int) **point_count** = `0` [🔗](class_curve.md#class_Curve_property_point_count)

- void **set_point_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_point_count** ( )

The number of points describing the curve.

---

### Method Descriptions

<span id="class_Curve_method_add_point"></span>

[int](class_int.md#class_int) **add_point** ( position: [Vector2](class_vector2.md#class_Vector2), left_tangent: [float](class_float.md#class_float) = 0, right_tangent: [float](class_float.md#class_float) = 0, left_mode: [TangentMode](class_curve.md#enum_Curve_TangentMode) = 0, right_mode: [TangentMode](class_curve.md#enum_Curve_TangentMode) = 0 ) [🔗](class_curve.md#class_Curve_method_add_point)

Adds a point to the curve. For each side, if the `*_mode` is [TANGENT_LINEAR](class_curve.md#class_Curve_constant_TANGENT_LINEAR), the `*_tangent` angle (in degrees) uses the slope of the curve halfway to the adjacent point. Allows custom assignments to the `*_tangent` angle if `*_mode` is set to [TANGENT_FREE](class_curve.md#class_Curve_constant_TANGENT_FREE).

---

<span id="class_Curve_method_bake"></span>

void **bake** ( ) [🔗](class_curve.md#class_Curve_method_bake)

Recomputes the baked cache of points for the curve.

---

<span id="class_Curve_method_clean_dupes"></span>

void **clean_dupes** ( ) [🔗](class_curve.md#class_Curve_method_clean_dupes)

Removes duplicate points, i.e. points that are less than 0.00001 units (engine epsilon value) away from their neighbor on the curve.

---

<span id="class_Curve_method_clear_points"></span>

void **clear_points** ( ) [🔗](class_curve.md#class_Curve_method_clear_points)

Removes all points from the curve.

---

<span id="class_Curve_method_get_domain_range"></span>

[float](class_float.md#class_float) **get_domain_range** ( ) *const* [🔗](class_curve.md#class_Curve_method_get_domain_range)

Returns the difference between [min_domain](class_curve.md#class_Curve_property_min_domain) and [max_domain](class_curve.md#class_Curve_property_max_domain).

---

<span id="class_Curve_method_get_point_left_mode"></span>

[TangentMode](class_curve.md#enum_Curve_TangentMode) **get_point_left_mode** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_curve.md#class_Curve_method_get_point_left_mode)

Returns the left [TangentMode](class_curve.md#enum_Curve_TangentMode) for the point at `index`.

---

<span id="class_Curve_method_get_point_left_tangent"></span>

[float](class_float.md#class_float) **get_point_left_tangent** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_curve.md#class_Curve_method_get_point_left_tangent)

Returns the left tangent angle (in degrees) for the point at `index`.

---

<span id="class_Curve_method_get_point_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_point_position** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_curve.md#class_Curve_method_get_point_position)

Returns the curve coordinates for the point at `index`.

---

<span id="class_Curve_method_get_point_right_mode"></span>

[TangentMode](class_curve.md#enum_Curve_TangentMode) **get_point_right_mode** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_curve.md#class_Curve_method_get_point_right_mode)

Returns the right [TangentMode](class_curve.md#enum_Curve_TangentMode) for the point at `index`.

---

<span id="class_Curve_method_get_point_right_tangent"></span>

[float](class_float.md#class_float) **get_point_right_tangent** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_curve.md#class_Curve_method_get_point_right_tangent)

Returns the right tangent angle (in degrees) for the point at `index`.

---

<span id="class_Curve_method_get_value_range"></span>

[float](class_float.md#class_float) **get_value_range** ( ) *const* [🔗](class_curve.md#class_Curve_method_get_value_range)

Returns the difference between [min_value](class_curve.md#class_Curve_property_min_value) and [max_value](class_curve.md#class_Curve_property_max_value).

---

<span id="class_Curve_method_remove_point"></span>

void **remove_point** ( index: [int](class_int.md#class_int) ) [🔗](class_curve.md#class_Curve_method_remove_point)

Removes the point at `index` from the curve.

---

<span id="class_Curve_method_sample"></span>

[float](class_float.md#class_float) **sample** ( offset: [float](class_float.md#class_float) ) *const* [🔗](class_curve.md#class_Curve_method_sample)

Returns the Y value for the point that would exist at the X position `offset` along the curve.

---

<span id="class_Curve_method_sample_baked"></span>

[float](class_float.md#class_float) **sample_baked** ( offset: [float](class_float.md#class_float) ) *const* [🔗](class_curve.md#class_Curve_method_sample_baked)

Returns the Y value for the point that would exist at the X position `offset` along the curve using the baked cache. Bakes the curve's points if not already baked.

---

<span id="class_Curve_method_set_point_left_mode"></span>

void **set_point_left_mode** ( index: [int](class_int.md#class_int), mode: [TangentMode](class_curve.md#enum_Curve_TangentMode) ) [🔗](class_curve.md#class_Curve_method_set_point_left_mode)

Sets the left [TangentMode](class_curve.md#enum_Curve_TangentMode) for the point at `index` to `mode`.

---

<span id="class_Curve_method_set_point_left_tangent"></span>

void **set_point_left_tangent** ( index: [int](class_int.md#class_int), tangent: [float](class_float.md#class_float) ) [🔗](class_curve.md#class_Curve_method_set_point_left_tangent)

Sets the left tangent angle for the point at `index` to `tangent`.

---

<span id="class_Curve_method_set_point_offset"></span>

[int](class_int.md#class_int) **set_point_offset** ( index: [int](class_int.md#class_int), offset: [float](class_float.md#class_float) ) [🔗](class_curve.md#class_Curve_method_set_point_offset)

Sets the offset from `0.5`.

---

<span id="class_Curve_method_set_point_right_mode"></span>

void **set_point_right_mode** ( index: [int](class_int.md#class_int), mode: [TangentMode](class_curve.md#enum_Curve_TangentMode) ) [🔗](class_curve.md#class_Curve_method_set_point_right_mode)

Sets the right [TangentMode](class_curve.md#enum_Curve_TangentMode) for the point at `index` to `mode`.

---

<span id="class_Curve_method_set_point_right_tangent"></span>

void **set_point_right_tangent** ( index: [int](class_int.md#class_int), tangent: [float](class_float.md#class_float) ) [🔗](class_curve.md#class_Curve_method_set_point_right_tangent)

Sets the right tangent angle for the point at `index` to `tangent`.

---

<span id="class_Curve_method_set_point_value"></span>

void **set_point_value** ( index: [int](class_int.md#class_int), y: [float](class_float.md#class_float) ) [🔗](class_curve.md#class_Curve_method_set_point_value)

Assigns the vertical position `y` to the point at `index`.
