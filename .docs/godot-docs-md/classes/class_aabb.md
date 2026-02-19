<span id="class_AABB"></span>

## AABB

A 3D axis-aligned bounding box.

### Description

The **AABB** built-in [Variant](class_variant.md#class_Variant) type represents an axis-aligned bounding box in a 3D space. It is defined by its [position](class_aabb.md#class_AABB_property_position) and [size](class_aabb.md#class_AABB_property_size), which are [Vector3](class_vector3.md#class_Vector3). It is frequently used for fast overlap tests (see [intersects()](class_aabb.md#class_AABB_method_intersects)). Although **AABB** itself is axis-aligned, it can be combined with [Transform3D](class_transform3d.md#class_Transform3D) to represent a rotated or skewed bounding box.

It uses floating-point coordinates. The 2D counterpart to **AABB** is [Rect2](class_rect2.md#class_Rect2). There is no version of **AABB** that uses integer coordinates.

 **Note:** Negative values for [size](class_aabb.md#class_AABB_property_size) are not supported. With negative size, most **AABB** methods do not work correctly. Use [abs()](class_aabb.md#class_AABB_method_abs) to get an equivalent **AABB** with a non-negative size.

 **Note:** In a boolean context, an **AABB** evaluates to `false` if both [position](class_aabb.md#class_AABB_property_position) and [size](class_aabb.md#class_AABB_property_size) are zero (equal to [Vector3.ZERO](class_vector3.md#class_Vector3_constant_ZERO)). Otherwise, it always evaluates to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Tutorials

- [Math documentation index](../tutorials/math/index.md)

- [Vector math](../tutorials/math/vector_math.md)

- [Advanced vector math](../tutorials/math/vectors_advanced.md)

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [end](class_aabb.md#class_AABB_property_end) | `Vector3(0, 0, 0)` |
| --- | --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [position](class_aabb.md#class_AABB_property_position) | `Vector3(0, 0, 0)` |
| [Vector3](class_vector3.md#class_Vector3) | [size](class_aabb.md#class_AABB_property_size) | `Vector3(0, 0, 0)` |

### Constructors


| [AABB](class_aabb.md#class_AABB) | [AABB](class_aabb.md#class_AABB_constructor_AABB) ( ) |
| --- | --- |
| [AABB](class_aabb.md#class_AABB) | [AABB](class_aabb.md#class_AABB_constructor_AABB) ( from: [AABB](class_aabb.md#class_AABB) ) |
| [AABB](class_aabb.md#class_AABB) | [AABB](class_aabb.md#class_AABB_constructor_AABB) ( position: [Vector3](class_vector3.md#class_Vector3), size: [Vector3](class_vector3.md#class_Vector3) ) |

### Methods


| [AABB](class_aabb.md#class_AABB) | [abs](class_aabb.md#class_AABB_method_abs) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [encloses](class_aabb.md#class_AABB_method_encloses) ( with: [AABB](class_aabb.md#class_AABB) ) const |
| [AABB](class_aabb.md#class_AABB) | [expand](class_aabb.md#class_AABB_method_expand) ( to_point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_center](class_aabb.md#class_AABB_method_get_center) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_endpoint](class_aabb.md#class_AABB_method_get_endpoint) ( idx: [int](class_int.md#class_int) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_longest_axis](class_aabb.md#class_AABB_method_get_longest_axis) ( ) const |
| [int](class_int.md#class_int) | [get_longest_axis_index](class_aabb.md#class_AABB_method_get_longest_axis_index) ( ) const |
| [float](class_float.md#class_float) | [get_longest_axis_size](class_aabb.md#class_AABB_method_get_longest_axis_size) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_shortest_axis](class_aabb.md#class_AABB_method_get_shortest_axis) ( ) const |
| [int](class_int.md#class_int) | [get_shortest_axis_index](class_aabb.md#class_AABB_method_get_shortest_axis_index) ( ) const |
| [float](class_float.md#class_float) | [get_shortest_axis_size](class_aabb.md#class_AABB_method_get_shortest_axis_size) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_support](class_aabb.md#class_AABB_method_get_support) ( direction: [Vector3](class_vector3.md#class_Vector3) ) const |
| [float](class_float.md#class_float) | [get_volume](class_aabb.md#class_AABB_method_get_volume) ( ) const |
| [AABB](class_aabb.md#class_AABB) | [grow](class_aabb.md#class_AABB_method_grow) ( by: [float](class_float.md#class_float) ) const |
| [bool](class_bool.md#class_bool) | [has_point](class_aabb.md#class_AABB_method_has_point) ( point: [Vector3](class_vector3.md#class_Vector3) ) const |
| [bool](class_bool.md#class_bool) | [has_surface](class_aabb.md#class_AABB_method_has_surface) ( ) const |
| [bool](class_bool.md#class_bool) | [has_volume](class_aabb.md#class_AABB_method_has_volume) ( ) const |
| [AABB](class_aabb.md#class_AABB) | [intersection](class_aabb.md#class_AABB_method_intersection) ( with: [AABB](class_aabb.md#class_AABB) ) const |
| [bool](class_bool.md#class_bool) | [intersects](class_aabb.md#class_AABB_method_intersects) ( with: [AABB](class_aabb.md#class_AABB) ) const |
| [bool](class_bool.md#class_bool) | [intersects_plane](class_aabb.md#class_AABB_method_intersects_plane) ( plane: [Plane](class_plane.md#class_Plane) ) const |
| [Variant](class_variant.md#class_Variant) | [intersects_ray](class_aabb.md#class_AABB_method_intersects_ray) ( from: [Vector3](class_vector3.md#class_Vector3), dir: [Vector3](class_vector3.md#class_Vector3) ) const |
| [Variant](class_variant.md#class_Variant) | [intersects_segment](class_aabb.md#class_AABB_method_intersects_segment) ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3) ) const |
| [bool](class_bool.md#class_bool) | [is_equal_approx](class_aabb.md#class_AABB_method_is_equal_approx) ( aabb: [AABB](class_aabb.md#class_AABB) ) const |
| [bool](class_bool.md#class_bool) | [is_finite](class_aabb.md#class_AABB_method_is_finite) ( ) const |
| [AABB](class_aabb.md#class_AABB) | [merge](class_aabb.md#class_AABB_method_merge) ( with: [AABB](class_aabb.md#class_AABB) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_aabb.md#class_AABB_operator_neq_AABB) ( right: [AABB](class_aabb.md#class_AABB) ) |
| --- | --- |
| [AABB](class_aabb.md#class_AABB) | [operator *](class_aabb.md#class_AABB_operator_mul_Transform3D) ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_aabb.md#class_AABB_operator_eq_AABB) ( right: [AABB](class_aabb.md#class_AABB) ) |

---

### Property Descriptions

<span id="class_AABB_property_end"></span>

[Vector3](class_vector3.md#class_Vector3) **end** = `Vector3(0, 0, 0)` [🔗](class_aabb.md#class_AABB_property_end)

The ending point. This is usually the corner on the top-right and back of the bounding box, and is equivalent to `position + size`. Setting this point affects the [size](class_aabb.md#class_AABB_property_size).

---

<span id="class_AABB_property_position"></span>

[Vector3](class_vector3.md#class_Vector3) **position** = `Vector3(0, 0, 0)` [🔗](class_aabb.md#class_AABB_property_position)

The origin point. This is usually the corner on the bottom-left and forward of the bounding box.

---

<span id="class_AABB_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(0, 0, 0)` [🔗](class_aabb.md#class_AABB_property_size)

The bounding box's width, height, and depth starting from [position](class_aabb.md#class_AABB_property_position). Setting this value also affects the [end](class_aabb.md#class_AABB_property_end) point.

 **Note:** It's recommended setting the width, height, and depth to non-negative values. This is because most methods in Godot assume that the [position](class_aabb.md#class_AABB_property_position) is the bottom-left-forward corner, and the [end](class_aabb.md#class_AABB_property_end) is the top-right-back corner. To get an equivalent bounding box with non-negative size, use [abs()](class_aabb.md#class_AABB_method_abs).

---

### Constructor Descriptions

<span id="class_AABB_constructor_AABB"></span>

[AABB](class_aabb.md#class_AABB) **AABB** ( ) [🔗](class_aabb.md#class_AABB_constructor_AABB)

Constructs an **AABB** with its [position](class_aabb.md#class_AABB_property_position) and [size](class_aabb.md#class_AABB_property_size) set to [Vector3.ZERO](class_vector3.md#class_Vector3_constant_ZERO).

---

[AABB](class_aabb.md#class_AABB) **AABB** ( from: [AABB](class_aabb.md#class_AABB) )

Constructs an **AABB** as a copy of the given **AABB**.

---

[AABB](class_aabb.md#class_AABB) **AABB** ( position: [Vector3](class_vector3.md#class_Vector3), size: [Vector3](class_vector3.md#class_Vector3) )

Constructs an **AABB** by `position` and `size`.

---

### Method Descriptions

<span id="class_AABB_method_abs"></span>

[AABB](class_aabb.md#class_AABB) **abs** ( ) *const* [🔗](class_aabb.md#class_AABB_method_abs)

Returns an **AABB** equivalent to this bounding box, with its width, height, and depth modified to be non-negative values.

.. tabs::

```
```

    var box = AABB(Vector3(5, 0, 5), Vector3(-20, -10, -5))
    var absolute = box.abs()
    print(absolute.position) # Prints (-15.0, -10.0, 0.0)
    print(absolute.size)     # Prints (20.0, 10.0, 5.0)

```
```

    var box = new Aabb(new Vector3(5, 0, 5), new Vector3(-20, -10, -5));
    var absolute = box.Abs();
    GD.Print(absolute.Position); // Prints (-15, -10, 0)
    GD.Print(absolute.Size);     // Prints (20, 10, 5)

 **Note:** It's recommended to use this method when [size](class_aabb.md#class_AABB_property_size) is negative, as most other methods in Godot assume that the [size](class_aabb.md#class_AABB_property_size)'s components are greater than `0`.

---

<span id="class_AABB_method_encloses"></span>

[bool](class_bool.md#class_bool) **encloses** ( with: [AABB](class_aabb.md#class_AABB) ) *const* [🔗](class_aabb.md#class_AABB_method_encloses)

Returns `true` if this bounding box *completely* encloses the `with` box. The edges of both boxes are included.

.. tabs::

```
```

    var a = AABB(Vector3(0, 0, 0), Vector3(4, 4, 4))
    var b = AABB(Vector3(1, 1, 1), Vector3(3, 3, 3))
    var c = AABB(Vector3(2, 2, 2), Vector3(8, 8, 8))

    print(a.encloses(a)) # Prints true
    print(a.encloses(b)) # Prints true
    print(a.encloses(c)) # Prints false

```
```

    var a = new Aabb(new Vector3(0, 0, 0), new Vector3(4, 4, 4));
    var b = new Aabb(new Vector3(1, 1, 1), new Vector3(3, 3, 3));
    var c = new Aabb(new Vector3(2, 2, 2), new Vector3(8, 8, 8));

    GD.Print(a.Encloses(a)); // Prints True
    GD.Print(a.Encloses(b)); // Prints True
    GD.Print(a.Encloses(c)); // Prints False

---

<span id="class_AABB_method_expand"></span>

[AABB](class_aabb.md#class_AABB) **expand** ( to_point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_aabb.md#class_AABB_method_expand)

Returns a copy of this bounding box expanded to align the edges with the given `to_point`, if necessary.

.. tabs::

```
```

    var box = AABB(Vector3(0, 0, 0), Vector3(5, 2, 5))

    box = box.expand(Vector3(10, 0, 0))
    print(box.position) # Prints (0.0, 0.0, 0.0)
    print(box.size)     # Prints (10.0, 2.0, 5.0)

    box = box.expand(Vector3(-5, 0, 5))
    print(box.position) # Prints (-5.0, 0.0, 0.0)
    print(box.size)     # Prints (15.0, 2.0, 5.0)

```
```

    var box = new Aabb(new Vector3(0, 0, 0), new Vector3(5, 2, 5));

    box = box.Expand(new Vector3(10, 0, 0));
    GD.Print(box.Position); // Prints (0, 0, 0)
    GD.Print(box.Size);     // Prints (10, 2, 5)

    box = box.Expand(new Vector3(-5, 0, 5));
    GD.Print(box.Position); // Prints (-5, 0, 0)
    GD.Print(box.Size);     // Prints (15, 2, 5)

---

<span id="class_AABB_method_get_center"></span>

[Vector3](class_vector3.md#class_Vector3) **get_center** ( ) *const* [🔗](class_aabb.md#class_AABB_method_get_center)

Returns the center point of the bounding box. This is the same as `position + (size / 2.0)`.

---

<span id="class_AABB_method_get_endpoint"></span>

[Vector3](class_vector3.md#class_Vector3) **get_endpoint** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_aabb.md#class_AABB_method_get_endpoint)

Returns the position of one of the 8 vertices that compose this bounding box. With an `idx` of `0` this is the same as [position](class_aabb.md#class_AABB_property_position), and an `idx` of `7` is the same as [end](class_aabb.md#class_AABB_property_end).

---

<span id="class_AABB_method_get_longest_axis"></span>

[Vector3](class_vector3.md#class_Vector3) **get_longest_axis** ( ) *const* [🔗](class_aabb.md#class_AABB_method_get_longest_axis)

Returns the longest normalized axis of this bounding box's [size](class_aabb.md#class_AABB_property_size), as a [Vector3](class_vector3.md#class_Vector3) ([Vector3.RIGHT](class_vector3.md#class_Vector3_constant_RIGHT), [Vector3.UP](class_vector3.md#class_Vector3_constant_UP), or [Vector3.BACK](class_vector3.md#class_Vector3_constant_BACK)).

.. tabs::

```
```

    var box = AABB(Vector3(0, 0, 0), Vector3(2, 4, 8))

    print(box.get_longest_axis())       # Prints (0.0, 0.0, 1.0)
    print(box.get_longest_axis_index()) # Prints 2
    print(box.get_longest_axis_size())  # Prints 8.0

```
```

    var box = new Aabb(new Vector3(0, 0, 0), new Vector3(2, 4, 8));

    GD.Print(box.GetLongestAxis());      // Prints (0, 0, 1)
    GD.Print(box.GetLongestAxisIndex()); // Prints Z
    GD.Print(box.GetLongestAxisSize());  // Prints 8

See also [get_longest_axis_index()](class_aabb.md#class_AABB_method_get_longest_axis_index) and [get_longest_axis_size()](class_aabb.md#class_AABB_method_get_longest_axis_size).

---

<span id="class_AABB_method_get_longest_axis_index"></span>

[int](class_int.md#class_int) **get_longest_axis_index** ( ) *const* [🔗](class_aabb.md#class_AABB_method_get_longest_axis_index)

Returns the index to the longest axis of this bounding box's [size](class_aabb.md#class_AABB_property_size) (see [Vector3.AXIS_X](class_vector3.md#class_Vector3_constant_AXIS_X), [Vector3.AXIS_Y](class_vector3.md#class_Vector3_constant_AXIS_Y), and [Vector3.AXIS_Z](class_vector3.md#class_Vector3_constant_AXIS_Z)).

For an example, see [get_longest_axis()](class_aabb.md#class_AABB_method_get_longest_axis).

---

<span id="class_AABB_method_get_longest_axis_size"></span>

[float](class_float.md#class_float) **get_longest_axis_size** ( ) *const* [🔗](class_aabb.md#class_AABB_method_get_longest_axis_size)

Returns the longest dimension of this bounding box's [size](class_aabb.md#class_AABB_property_size).

For an example, see [get_longest_axis()](class_aabb.md#class_AABB_method_get_longest_axis).

---

<span id="class_AABB_method_get_shortest_axis"></span>

[Vector3](class_vector3.md#class_Vector3) **get_shortest_axis** ( ) *const* [🔗](class_aabb.md#class_AABB_method_get_shortest_axis)

Returns the shortest normalized axis of this bounding box's [size](class_aabb.md#class_AABB_property_size), as a [Vector3](class_vector3.md#class_Vector3) ([Vector3.RIGHT](class_vector3.md#class_Vector3_constant_RIGHT), [Vector3.UP](class_vector3.md#class_Vector3_constant_UP), or [Vector3.BACK](class_vector3.md#class_Vector3_constant_BACK)).

.. tabs::

```
```

    var box = AABB(Vector3(0, 0, 0), Vector3(2, 4, 8))

    print(box.get_shortest_axis())       # Prints (1.0, 0.0, 0.0)
    print(box.get_shortest_axis_index()) # Prints 0
    print(box.get_shortest_axis_size())  # Prints 2.0

```
```

    var box = new Aabb(new Vector3(0, 0, 0), new Vector3(2, 4, 8));

    GD.Print(box.GetShortestAxis());      // Prints (1, 0, 0)
    GD.Print(box.GetShortestAxisIndex()); // Prints X
    GD.Print(box.GetShortestAxisSize());  // Prints 2

See also [get_shortest_axis_index()](class_aabb.md#class_AABB_method_get_shortest_axis_index) and [get_shortest_axis_size()](class_aabb.md#class_AABB_method_get_shortest_axis_size).

---

<span id="class_AABB_method_get_shortest_axis_index"></span>

[int](class_int.md#class_int) **get_shortest_axis_index** ( ) *const* [🔗](class_aabb.md#class_AABB_method_get_shortest_axis_index)

Returns the index to the shortest axis of this bounding box's [size](class_aabb.md#class_AABB_property_size) (see [Vector3.AXIS_X](class_vector3.md#class_Vector3_constant_AXIS_X), [Vector3.AXIS_Y](class_vector3.md#class_Vector3_constant_AXIS_Y), and [Vector3.AXIS_Z](class_vector3.md#class_Vector3_constant_AXIS_Z)).

For an example, see [get_shortest_axis()](class_aabb.md#class_AABB_method_get_shortest_axis).

---

<span id="class_AABB_method_get_shortest_axis_size"></span>

[float](class_float.md#class_float) **get_shortest_axis_size** ( ) *const* [🔗](class_aabb.md#class_AABB_method_get_shortest_axis_size)

Returns the shortest dimension of this bounding box's [size](class_aabb.md#class_AABB_property_size).

For an example, see [get_shortest_axis()](class_aabb.md#class_AABB_method_get_shortest_axis).

---

<span id="class_AABB_method_get_support"></span>

[Vector3](class_vector3.md#class_Vector3) **get_support** ( direction: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_aabb.md#class_AABB_method_get_support)

Returns the vertex's position of this bounding box that's the farthest in the given direction. This point is commonly known as the support point in collision detection algorithms.

---

<span id="class_AABB_method_get_volume"></span>

[float](class_float.md#class_float) **get_volume** ( ) *const* [🔗](class_aabb.md#class_AABB_method_get_volume)

Returns the bounding box's volume. This is equivalent to `size.x * size.y * size.z`. See also [has_volume()](class_aabb.md#class_AABB_method_has_volume).

---

<span id="class_AABB_method_grow"></span>

[AABB](class_aabb.md#class_AABB) **grow** ( by: [float](class_float.md#class_float) ) *const* [🔗](class_aabb.md#class_AABB_method_grow)

Returns a copy of this bounding box extended on all sides by the given amount `by`. A negative amount shrinks the box instead.

.. tabs::

```
```

    var a = AABB(Vector3(4, 4, 4), Vector3(8, 8, 8)).grow(4)
    print(a.position) # Prints (0.0, 0.0, 0.0)
    print(a.size)     # Prints (16.0, 16.0, 16.0)

    var b = AABB(Vector3(0, 0, 0), Vector3(8, 4, 2)).grow(2)
    print(b.position) # Prints (-2.0, -2.0, -2.0)
    print(b.size)     # Prints (12.0, 8.0, 6.0)

```
```

    var a = new Aabb(new Vector3(4, 4, 4), new Vector3(8, 8, 8)).Grow(4);
    GD.Print(a.Position); // Prints (0, 0, 0)
    GD.Print(a.Size);     // Prints (16, 16, 16)

    var b = new Aabb(new Vector3(0, 0, 0), new Vector3(8, 4, 2)).Grow(2);
    GD.Print(b.Position); // Prints (-2, -2, -2)
    GD.Print(b.Size);     // Prints (12, 8, 6)

---

<span id="class_AABB_method_has_point"></span>

[bool](class_bool.md#class_bool) **has_point** ( point: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_aabb.md#class_AABB_method_has_point)

Returns `true` if the bounding box contains the given `point`. By convention, points exactly on the right, top, and front sides are **not** included.

 **Note:** This method is not reliable for **AABB** with a *negative* [size](class_aabb.md#class_AABB_property_size). Use [abs()](class_aabb.md#class_AABB_method_abs) first to get a valid bounding box.

---

<span id="class_AABB_method_has_surface"></span>

[bool](class_bool.md#class_bool) **has_surface** ( ) *const* [🔗](class_aabb.md#class_AABB_method_has_surface)

Returns `true` if this bounding box has a surface or a length, that is, at least one component of [size](class_aabb.md#class_AABB_property_size) is greater than `0`. Otherwise, returns `false`.

---

<span id="class_AABB_method_has_volume"></span>

[bool](class_bool.md#class_bool) **has_volume** ( ) *const* [🔗](class_aabb.md#class_AABB_method_has_volume)

Returns `true` if this bounding box's width, height, and depth are all positive. See also [get_volume()](class_aabb.md#class_AABB_method_get_volume).

---

<span id="class_AABB_method_intersection"></span>

[AABB](class_aabb.md#class_AABB) **intersection** ( with: [AABB](class_aabb.md#class_AABB) ) *const* [🔗](class_aabb.md#class_AABB_method_intersection)

Returns the intersection between this bounding box and `with`. If the boxes do not intersect, returns an empty **AABB**. If the boxes intersect at the edge, returns a flat **AABB** with no volume (see [has_surface()](class_aabb.md#class_AABB_method_has_surface) and [has_volume()](class_aabb.md#class_AABB_method_has_volume)).

.. tabs::

```
```

    var box1 = AABB(Vector3(0, 0, 0), Vector3(5, 2, 8))
    var box2 = AABB(Vector3(2, 0, 2), Vector3(8, 4, 4))

    var intersection = box1.intersection(box2)
    print(intersection.position) # Prints (2.0, 0.0, 2.0)
    print(intersection.size)     # Prints (3.0, 2.0, 4.0)

```
```

    var box1 = new Aabb(new Vector3(0, 0, 0), new Vector3(5, 2, 8));
    var box2 = new Aabb(new Vector3(2, 0, 2), new Vector3(8, 4, 4));

    var intersection = box1.Intersection(box2);
    GD.Print(intersection.Position); // Prints (2, 0, 2)
    GD.Print(intersection.Size);     // Prints (3, 2, 4)

 **Note:** If you only need to know whether two bounding boxes are intersecting, use [intersects()](class_aabb.md#class_AABB_method_intersects), instead.

---

<span id="class_AABB_method_intersects"></span>

[bool](class_bool.md#class_bool) **intersects** ( with: [AABB](class_aabb.md#class_AABB) ) *const* [🔗](class_aabb.md#class_AABB_method_intersects)

Returns `true` if this bounding box overlaps with the box `with`. The edges of both boxes are *always* excluded.

---

<span id="class_AABB_method_intersects_plane"></span>

[bool](class_bool.md#class_bool) **intersects_plane** ( plane: [Plane](class_plane.md#class_Plane) ) *const* [🔗](class_aabb.md#class_AABB_method_intersects_plane)

Returns `true` if this bounding box is on both sides of the given `plane`.

---

<span id="class_AABB_method_intersects_ray"></span>

[Variant](class_variant.md#class_Variant) **intersects_ray** ( from: [Vector3](class_vector3.md#class_Vector3), dir: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_aabb.md#class_AABB_method_intersects_ray)

Returns the first point where this bounding box and the given ray intersect, as a [Vector3](class_vector3.md#class_Vector3). If no intersection occurs, returns `null`.

The ray begin at `from`, faces `dir` and extends towards infinity.

---

<span id="class_AABB_method_intersects_segment"></span>

[Variant](class_variant.md#class_Variant) **intersects_segment** ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3) ) *const* [🔗](class_aabb.md#class_AABB_method_intersects_segment)

Returns the first point where this bounding box and the given segment intersect, as a [Vector3](class_vector3.md#class_Vector3). If no intersection occurs, returns `null`.

The segment begins at `from` and ends at `to`.

---

<span id="class_AABB_method_is_equal_approx"></span>

[bool](class_bool.md#class_bool) **is_equal_approx** ( aabb: [AABB](class_aabb.md#class_AABB) ) *const* [🔗](class_aabb.md#class_AABB_method_is_equal_approx)

Returns `true` if this bounding box and `aabb` are approximately equal, by calling [Vector3.is_equal_approx()](class_vector3.md#class_Vector3_method_is_equal_approx) on the [position](class_aabb.md#class_AABB_property_position) and the [size](class_aabb.md#class_AABB_property_size).

---

<span id="class_AABB_method_is_finite"></span>

[bool](class_bool.md#class_bool) **is_finite** ( ) *const* [🔗](class_aabb.md#class_AABB_method_is_finite)

Returns `true` if this bounding box's values are finite, by calling [Vector3.is_finite()](class_vector3.md#class_Vector3_method_is_finite) on the [position](class_aabb.md#class_AABB_property_position) and the [size](class_aabb.md#class_AABB_property_size).

---

<span id="class_AABB_method_merge"></span>

[AABB](class_aabb.md#class_AABB) **merge** ( with: [AABB](class_aabb.md#class_AABB) ) *const* [🔗](class_aabb.md#class_AABB_method_merge)

Returns an **AABB** that encloses both this bounding box and `with` around the edges. See also [encloses()](class_aabb.md#class_AABB_method_encloses).

---

### Operator Descriptions

<span id="class_AABB_operator_neq_AABB"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [AABB](class_aabb.md#class_AABB) ) [🔗](class_aabb.md#class_AABB_operator_neq_AABB)

Returns `true` if the [position](class_aabb.md#class_AABB_property_position) or [size](class_aabb.md#class_AABB_property_size) of both bounding boxes are not equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_aabb.md#class_AABB_method_is_equal_approx) instead, which is more reliable.

---

<span id="class_AABB_operator_mul_Transform3D"></span>

[AABB](class_aabb.md#class_AABB) **operator *** ( right: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_aabb.md#class_AABB_operator_mul_Transform3D)

Inversely transforms (multiplies) the **AABB** by the given [Transform3D](class_transform3d.md#class_Transform3D) transformation matrix, under the assumption that the transformation basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).

 `aabb * transform` is equivalent to `transform.inverse() * aabb`. See [Transform3D.inverse()](class_transform3d.md#class_Transform3D_method_inverse).

For transforming by inverse of an affine transformation (e.g. with scaling) `transform.affine_inverse() * aabb` can be used instead. See [Transform3D.affine_inverse()](class_transform3d.md#class_Transform3D_method_affine_inverse).

---

<span id="class_AABB_operator_eq_AABB"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [AABB](class_aabb.md#class_AABB) ) [🔗](class_aabb.md#class_AABB_operator_eq_AABB)

Returns `true` if both [position](class_aabb.md#class_AABB_property_position) and [size](class_aabb.md#class_AABB_property_size) of the bounding boxes are exactly equal, respectively.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_aabb.md#class_AABB_method_is_equal_approx) instead, which is more reliable.
