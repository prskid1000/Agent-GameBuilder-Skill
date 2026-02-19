<span id="class_Rect2"></span>

## Rect2

A 2D axis-aligned bounding box using floating-point coordinates.

### Description

The **Rect2** built-in [Variant](class_variant.md#class_Variant) type represents an axis-aligned rectangle in a 2D space. It is defined by its [position](class_rect2.md#class_Rect2_property_position) and [size](class_rect2.md#class_Rect2_property_size), which are [Vector2](class_vector2.md#class_Vector2). It is frequently used for fast overlap tests (see [intersects()](class_rect2.md#class_Rect2_method_intersects)). Although **Rect2** itself is axis-aligned, it can be combined with [Transform2D](class_transform2d.md#class_Transform2D) to represent a rotated or skewed rectangle.

For integer coordinates, use [Rect2i](class_rect2i.md#class_Rect2i). The 3D equivalent to **Rect2** is [AABB](class_aabb.md#class_AABB).

 **Note:** Negative values for [size](class_rect2.md#class_Rect2_property_size) are not supported. With negative size, most **Rect2** methods do not work correctly. Use [abs()](class_rect2.md#class_Rect2_method_abs) to get an equivalent **Rect2** with a non-negative size.

 **Note:** In a boolean context, a **Rect2** evaluates to `false` if both [position](class_rect2.md#class_Rect2_property_position) and [size](class_rect2.md#class_Rect2_property_size) are zero (equal to [Vector2.ZERO](class_vector2.md#class_Vector2_constant_ZERO)). Otherwise, it always evaluates to `true`.

> **Note:** There are notable differences when using this API with C#. See :ref:`doc_c_sharp_differences` for more information.

### Tutorials

- [Math documentation index](../tutorials/math/index.md)

- [Vector math](../tutorials/math/vector_math.md)

- [Advanced vector math](../tutorials/math/vectors_advanced.md)

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [end](class_rect2.md#class_Rect2_property_end) | `Vector2(0, 0)` |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [position](class_rect2.md#class_Rect2_property_position) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [size](class_rect2.md#class_Rect2_property_size) | `Vector2(0, 0)` |

### Constructors


| [Rect2](class_rect2.md#class_Rect2) | [Rect2](class_rect2.md#class_Rect2_constructor_Rect2) ( ) |
| --- | --- |
| [Rect2](class_rect2.md#class_Rect2) | [Rect2](class_rect2.md#class_Rect2_constructor_Rect2) ( from: [Rect2](class_rect2.md#class_Rect2) ) |
| [Rect2](class_rect2.md#class_Rect2) | [Rect2](class_rect2.md#class_Rect2_constructor_Rect2) ( from: [Rect2i](class_rect2i.md#class_Rect2i) ) |
| [Rect2](class_rect2.md#class_Rect2) | [Rect2](class_rect2.md#class_Rect2_constructor_Rect2) ( position: [Vector2](class_vector2.md#class_Vector2), size: [Vector2](class_vector2.md#class_Vector2) ) |
| [Rect2](class_rect2.md#class_Rect2) | [Rect2](class_rect2.md#class_Rect2_constructor_Rect2) ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), width: [float](class_float.md#class_float), height: [float](class_float.md#class_float) ) |

### Methods


| [Rect2](class_rect2.md#class_Rect2) | [abs](class_rect2.md#class_Rect2_method_abs) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [encloses](class_rect2.md#class_Rect2_method_encloses) ( b: [Rect2](class_rect2.md#class_Rect2) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [expand](class_rect2.md#class_Rect2_method_expand) ( to: [Vector2](class_vector2.md#class_Vector2) ) const |
| [float](class_float.md#class_float) | [get_area](class_rect2.md#class_Rect2_method_get_area) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_center](class_rect2.md#class_Rect2_method_get_center) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_support](class_rect2.md#class_Rect2_method_get_support) ( direction: [Vector2](class_vector2.md#class_Vector2) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [grow](class_rect2.md#class_Rect2_method_grow) ( amount: [float](class_float.md#class_float) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [grow_individual](class_rect2.md#class_Rect2_method_grow_individual) ( left: [float](class_float.md#class_float), top: [float](class_float.md#class_float), right: [float](class_float.md#class_float), bottom: [float](class_float.md#class_float) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [grow_side](class_rect2.md#class_Rect2_method_grow_side) ( side: [int](class_int.md#class_int), amount: [float](class_float.md#class_float) ) const |
| [bool](class_bool.md#class_bool) | [has_area](class_rect2.md#class_Rect2_method_has_area) ( ) const |
| [bool](class_bool.md#class_bool) | [has_point](class_rect2.md#class_Rect2_method_has_point) ( point: [Vector2](class_vector2.md#class_Vector2) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [intersection](class_rect2.md#class_Rect2_method_intersection) ( b: [Rect2](class_rect2.md#class_Rect2) ) const |
| [bool](class_bool.md#class_bool) | [intersects](class_rect2.md#class_Rect2_method_intersects) ( b: [Rect2](class_rect2.md#class_Rect2), include_borders: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [is_equal_approx](class_rect2.md#class_Rect2_method_is_equal_approx) ( rect: [Rect2](class_rect2.md#class_Rect2) ) const |
| [bool](class_bool.md#class_bool) | [is_finite](class_rect2.md#class_Rect2_method_is_finite) ( ) const |
| [Rect2](class_rect2.md#class_Rect2) | [merge](class_rect2.md#class_Rect2_method_merge) ( b: [Rect2](class_rect2.md#class_Rect2) ) const |

### Operators


| [bool](class_bool.md#class_bool) | [operator !=](class_rect2.md#class_Rect2_operator_neq_Rect2) ( right: [Rect2](class_rect2.md#class_Rect2) ) |
| --- | --- |
| [Rect2](class_rect2.md#class_Rect2) | [operator *](class_rect2.md#class_Rect2_operator_mul_Transform2D) ( right: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| [bool](class_bool.md#class_bool) | [operator ==](class_rect2.md#class_Rect2_operator_eq_Rect2) ( right: [Rect2](class_rect2.md#class_Rect2) ) |

---

### Property Descriptions

<span id="class_Rect2_property_end"></span>

[Vector2](class_vector2.md#class_Vector2) **end** = `Vector2(0, 0)` [🔗](class_rect2.md#class_Rect2_property_end)

The ending point. This is usually the bottom-right corner of the rectangle, and is equivalent to `position + size`. Setting this point affects the [size](class_rect2.md#class_Rect2_property_size).

---

<span id="class_Rect2_property_position"></span>

[Vector2](class_vector2.md#class_Vector2) **position** = `Vector2(0, 0)` [🔗](class_rect2.md#class_Rect2_property_position)

The origin point. This is usually the top-left corner of the rectangle.

---

<span id="class_Rect2_property_size"></span>

[Vector2](class_vector2.md#class_Vector2) **size** = `Vector2(0, 0)` [🔗](class_rect2.md#class_Rect2_property_size)

The rectangle's width and height, starting from [position](class_rect2.md#class_Rect2_property_position). Setting this value also affects the [end](class_rect2.md#class_Rect2_property_end) point.

 **Note:** It's recommended setting the width and height to non-negative values, as most methods in Godot assume that the [position](class_rect2.md#class_Rect2_property_position) is the top-left corner, and the [end](class_rect2.md#class_Rect2_property_end) is the bottom-right corner. To get an equivalent rectangle with non-negative size, use [abs()](class_rect2.md#class_Rect2_method_abs).

---

### Constructor Descriptions

<span id="class_Rect2_constructor_Rect2"></span>

[Rect2](class_rect2.md#class_Rect2) **Rect2** ( ) [🔗](class_rect2.md#class_Rect2_constructor_Rect2)

Constructs a **Rect2** with its [position](class_rect2.md#class_Rect2_property_position) and [size](class_rect2.md#class_Rect2_property_size) set to [Vector2.ZERO](class_vector2.md#class_Vector2_constant_ZERO).

---

[Rect2](class_rect2.md#class_Rect2) **Rect2** ( from: [Rect2](class_rect2.md#class_Rect2) )

Constructs a **Rect2** as a copy of the given **Rect2**.

---

[Rect2](class_rect2.md#class_Rect2) **Rect2** ( from: [Rect2i](class_rect2i.md#class_Rect2i) )

Constructs a **Rect2** from a [Rect2i](class_rect2i.md#class_Rect2i).

---

[Rect2](class_rect2.md#class_Rect2) **Rect2** ( position: [Vector2](class_vector2.md#class_Vector2), size: [Vector2](class_vector2.md#class_Vector2) )

Constructs a **Rect2** by `position` and `size`.

---

[Rect2](class_rect2.md#class_Rect2) **Rect2** ( x: [float](class_float.md#class_float), y: [float](class_float.md#class_float), width: [float](class_float.md#class_float), height: [float](class_float.md#class_float) )

Constructs a **Rect2** by setting its [position](class_rect2.md#class_Rect2_property_position) to (`x`, `y`), and its [size](class_rect2.md#class_Rect2_property_size) to (`width`, `height`).

---

### Method Descriptions

<span id="class_Rect2_method_abs"></span>

[Rect2](class_rect2.md#class_Rect2) **abs** ( ) *const* [🔗](class_rect2.md#class_Rect2_method_abs)

Returns a **Rect2** equivalent to this rectangle, with its width and height modified to be non-negative values, and with its [position](class_rect2.md#class_Rect2_property_position) being the top-left corner of the rectangle.

.. tabs::

```
```

    var rect = Rect2(25, 25, -100, -50)
    var absolute = rect.abs() # absolute is Rect2(-75, -25, 100, 50)

```
```

    var rect = new Rect2(25, 25, -100, -50);
    var absolute = rect.Abs(); // absolute is Rect2(-75, -25, 100, 50)

 **Note:** It's recommended to use this method when [size](class_rect2.md#class_Rect2_property_size) is negative, as most other methods in Godot assume that the [position](class_rect2.md#class_Rect2_property_position) is the top-left corner, and the [end](class_rect2.md#class_Rect2_property_end) is the bottom-right corner.

---

<span id="class_Rect2_method_encloses"></span>

[bool](class_bool.md#class_bool) **encloses** ( b: [Rect2](class_rect2.md#class_Rect2) ) *const* [🔗](class_rect2.md#class_Rect2_method_encloses)

Returns `true` if this rectangle *completely* encloses the `b` rectangle.

---

<span id="class_Rect2_method_expand"></span>

[Rect2](class_rect2.md#class_Rect2) **expand** ( to: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_rect2.md#class_Rect2_method_expand)

Returns a copy of this rectangle expanded to align the edges with the given `to` point, if necessary.

.. tabs::

```
```

    var rect = Rect2(0, 0, 5, 2)

    rect = rect.expand(Vector2(10, 0)) # rect is Rect2(0, 0, 10, 2)
    rect = rect.expand(Vector2(-5, 5)) # rect is Rect2(-5, 0, 15, 5)

```
```

    var rect = new Rect2(0, 0, 5, 2);

    rect = rect.Expand(new Vector2(10, 0)); // rect is Rect2(0, 0, 10, 2)
    rect = rect.Expand(new Vector2(-5, 5)); // rect is Rect2(-5, 0, 15, 5)

---

<span id="class_Rect2_method_get_area"></span>

[float](class_float.md#class_float) **get_area** ( ) *const* [🔗](class_rect2.md#class_Rect2_method_get_area)

Returns the rectangle's area. This is equivalent to `size.x * size.y`. See also [has_area()](class_rect2.md#class_Rect2_method_has_area).

---

<span id="class_Rect2_method_get_center"></span>

[Vector2](class_vector2.md#class_Vector2) **get_center** ( ) *const* [🔗](class_rect2.md#class_Rect2_method_get_center)

Returns the center point of the rectangle. This is the same as `position + (size / 2.0)`.

---

<span id="class_Rect2_method_get_support"></span>

[Vector2](class_vector2.md#class_Vector2) **get_support** ( direction: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_rect2.md#class_Rect2_method_get_support)

Returns the vertex's position of this rect that's the farthest in the given direction. This point is commonly known as the support point in collision detection algorithms.

---

<span id="class_Rect2_method_grow"></span>

[Rect2](class_rect2.md#class_Rect2) **grow** ( amount: [float](class_float.md#class_float) ) *const* [🔗](class_rect2.md#class_Rect2_method_grow)

Returns a copy of this rectangle extended on all sides by the given `amount`. A negative `amount` shrinks the rectangle instead. See also [grow_individual()](class_rect2.md#class_Rect2_method_grow_individual) and [grow_side()](class_rect2.md#class_Rect2_method_grow_side).

.. tabs::

```
```

    var a = Rect2(4, 4, 8, 8).grow(4) # a is Rect2(0, 0, 16, 16)
    var b = Rect2(0, 0, 8, 4).grow(2) # b is Rect2(-2, -2, 12, 8)

```
```

    var a = new Rect2(4, 4, 8, 8).Grow(4); // a is Rect2(0, 0, 16, 16)
    var b = new Rect2(0, 0, 8, 4).Grow(2); // b is Rect2(-2, -2, 12, 8)

---

<span id="class_Rect2_method_grow_individual"></span>

[Rect2](class_rect2.md#class_Rect2) **grow_individual** ( left: [float](class_float.md#class_float), top: [float](class_float.md#class_float), right: [float](class_float.md#class_float), bottom: [float](class_float.md#class_float) ) *const* [🔗](class_rect2.md#class_Rect2_method_grow_individual)

Returns a copy of this rectangle with its `left`, `top`, `right`, and `bottom` sides extended by the given amounts. Negative values shrink the sides, instead. See also [grow()](class_rect2.md#class_Rect2_method_grow) and [grow_side()](class_rect2.md#class_Rect2_method_grow_side).

---

<span id="class_Rect2_method_grow_side"></span>

[Rect2](class_rect2.md#class_Rect2) **grow_side** ( side: [int](class_int.md#class_int), amount: [float](class_float.md#class_float) ) *const* [🔗](class_rect2.md#class_Rect2_method_grow_side)

Returns a copy of this rectangle with its `side` extended by the given `amount` (see Side constants). A negative `amount` shrinks the rectangle, instead. See also [grow()](class_rect2.md#class_Rect2_method_grow) and [grow_individual()](class_rect2.md#class_Rect2_method_grow_individual).

---

<span id="class_Rect2_method_has_area"></span>

[bool](class_bool.md#class_bool) **has_area** ( ) *const* [🔗](class_rect2.md#class_Rect2_method_has_area)

Returns `true` if this rectangle has positive width and height. See also [get_area()](class_rect2.md#class_Rect2_method_get_area).

---

<span id="class_Rect2_method_has_point"></span>

[bool](class_bool.md#class_bool) **has_point** ( point: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_rect2.md#class_Rect2_method_has_point)

Returns `true` if the rectangle contains the given `point`. By convention, points on the right and bottom edges are **not** included.

 **Note:** This method is not reliable for **Rect2** with a *negative* [size](class_rect2.md#class_Rect2_property_size). Use [abs()](class_rect2.md#class_Rect2_method_abs) first to get a valid rectangle.

---

<span id="class_Rect2_method_intersection"></span>

[Rect2](class_rect2.md#class_Rect2) **intersection** ( b: [Rect2](class_rect2.md#class_Rect2) ) *const* [🔗](class_rect2.md#class_Rect2_method_intersection)

Returns the intersection between this rectangle and `b`. If the rectangles do not intersect, returns an empty **Rect2**.

.. tabs::

```
```

    var rect1 = Rect2(0, 0, 5, 10)
    var rect2 = Rect2(2, 0, 8, 4)

    var a = rect1.intersection(rect2) # a is Rect2(2, 0, 3, 4)

```
```

    var rect1 = new Rect2(0, 0, 5, 10);
    var rect2 = new Rect2(2, 0, 8, 4);

    var a = rect1.Intersection(rect2); // a is Rect2(2, 0, 3, 4)

 **Note:** If you only need to know whether two rectangles are overlapping, use [intersects()](class_rect2.md#class_Rect2_method_intersects), instead.

---

<span id="class_Rect2_method_intersects"></span>

[bool](class_bool.md#class_bool) **intersects** ( b: [Rect2](class_rect2.md#class_Rect2), include_borders: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_rect2.md#class_Rect2_method_intersects)

Returns `true` if this rectangle overlaps with the `b` rectangle. The edges of both rectangles are excluded, unless `include_borders` is `true`.

---

<span id="class_Rect2_method_is_equal_approx"></span>

[bool](class_bool.md#class_bool) **is_equal_approx** ( rect: [Rect2](class_rect2.md#class_Rect2) ) *const* [🔗](class_rect2.md#class_Rect2_method_is_equal_approx)

Returns `true` if this rectangle and `rect` are approximately equal, by calling [Vector2.is_equal_approx()](class_vector2.md#class_Vector2_method_is_equal_approx) on the [position](class_rect2.md#class_Rect2_property_position) and the [size](class_rect2.md#class_Rect2_property_size).

---

<span id="class_Rect2_method_is_finite"></span>

[bool](class_bool.md#class_bool) **is_finite** ( ) *const* [🔗](class_rect2.md#class_Rect2_method_is_finite)

Returns `true` if this rectangle's values are finite, by calling [Vector2.is_finite()](class_vector2.md#class_Vector2_method_is_finite) on the [position](class_rect2.md#class_Rect2_property_position) and the [size](class_rect2.md#class_Rect2_property_size).

---

<span id="class_Rect2_method_merge"></span>

[Rect2](class_rect2.md#class_Rect2) **merge** ( b: [Rect2](class_rect2.md#class_Rect2) ) *const* [🔗](class_rect2.md#class_Rect2_method_merge)

Returns a **Rect2** that encloses both this rectangle and `b` around the edges. See also [encloses()](class_rect2.md#class_Rect2_method_encloses).

---

### Operator Descriptions

<span id="class_Rect2_operator_neq_Rect2"></span>

[bool](class_bool.md#class_bool) **operator !=** ( right: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_rect2.md#class_Rect2_operator_neq_Rect2)

Returns `true` if the [position](class_rect2.md#class_Rect2_property_position) or [size](class_rect2.md#class_Rect2_property_size) of both rectangles are not equal.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_rect2.md#class_Rect2_method_is_equal_approx) instead, which is more reliable.

---

<span id="class_Rect2_operator_mul_Transform2D"></span>

[Rect2](class_rect2.md#class_Rect2) **operator *** ( right: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_rect2.md#class_Rect2_operator_mul_Transform2D)

Inversely transforms (multiplies) the **Rect2** by the given [Transform2D](class_transform2d.md#class_Transform2D) transformation matrix, under the assumption that the transformation basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).

 `rect * transform` is equivalent to `transform.inverse() * rect`. See [Transform2D.inverse()](class_transform2d.md#class_Transform2D_method_inverse).

For transforming by inverse of an affine transformation (e.g. with scaling) `transform.affine_inverse() * rect` can be used instead. See [Transform2D.affine_inverse()](class_transform2d.md#class_Transform2D_method_affine_inverse).

---

<span id="class_Rect2_operator_eq_Rect2"></span>

[bool](class_bool.md#class_bool) **operator ==** ( right: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_rect2.md#class_Rect2_operator_eq_Rect2)

Returns `true` if both [position](class_rect2.md#class_Rect2_property_position) and [size](class_rect2.md#class_Rect2_property_size) of the rectangles are exactly equal, respectively.

 **Note:** Due to floating-point precision errors, consider using [is_equal_approx()](class_rect2.md#class_Rect2_method_is_equal_approx) instead, which is more reliable.
