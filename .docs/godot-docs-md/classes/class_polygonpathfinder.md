<span id="class_PolygonPathFinder"></span>

## PolygonPathFinder

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

.. container:: contribute

	There is currently no description for this class. Please help us by contributing one!

### Methods


| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [find_path](class_polygonpathfinder.md#class_PolygonPathFinder_method_find_path) ( from: [Vector2](class_vector2.md#class_Vector2), to: [Vector2](class_vector2.md#class_Vector2) ) |
| --- | --- |
| [Rect2](class_rect2.md#class_Rect2) | [get_bounds](class_polygonpathfinder.md#class_PolygonPathFinder_method_get_bounds) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_closest_point](class_polygonpathfinder.md#class_PolygonPathFinder_method_get_closest_point) ( point: [Vector2](class_vector2.md#class_Vector2) ) const |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [get_intersections](class_polygonpathfinder.md#class_PolygonPathFinder_method_get_intersections) ( from: [Vector2](class_vector2.md#class_Vector2), to: [Vector2](class_vector2.md#class_Vector2) ) const |
| [float](class_float.md#class_float) | [get_point_penalty](class_polygonpathfinder.md#class_PolygonPathFinder_method_get_point_penalty) ( idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_point_inside](class_polygonpathfinder.md#class_PolygonPathFinder_method_is_point_inside) ( point: [Vector2](class_vector2.md#class_Vector2) ) const |
| void | [set_point_penalty](class_polygonpathfinder.md#class_PolygonPathFinder_method_set_point_penalty) ( idx: [int](class_int.md#class_int), penalty: [float](class_float.md#class_float) ) |
| void | [setup](class_polygonpathfinder.md#class_PolygonPathFinder_method_setup) ( points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), connections: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |

---

### Method Descriptions

<span id="class_PolygonPathFinder_method_find_path"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **find_path** ( from: [Vector2](class_vector2.md#class_Vector2), to: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_polygonpathfinder.md#class_PolygonPathFinder_method_find_path)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PolygonPathFinder_method_get_bounds"></span>

[Rect2](class_rect2.md#class_Rect2) **get_bounds** ( ) *const* [🔗](class_polygonpathfinder.md#class_PolygonPathFinder_method_get_bounds)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PolygonPathFinder_method_get_closest_point"></span>

[Vector2](class_vector2.md#class_Vector2) **get_closest_point** ( point: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_polygonpathfinder.md#class_PolygonPathFinder_method_get_closest_point)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PolygonPathFinder_method_get_intersections"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_intersections** ( from: [Vector2](class_vector2.md#class_Vector2), to: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_polygonpathfinder.md#class_PolygonPathFinder_method_get_intersections)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PolygonPathFinder_method_get_point_penalty"></span>

[float](class_float.md#class_float) **get_point_penalty** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_polygonpathfinder.md#class_PolygonPathFinder_method_get_point_penalty)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PolygonPathFinder_method_is_point_inside"></span>

[bool](class_bool.md#class_bool) **is_point_inside** ( point: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_polygonpathfinder.md#class_PolygonPathFinder_method_is_point_inside)

Returns `true` if `point` falls inside the polygon area.

.. tabs::

```
```

    var polygon_path_finder = PolygonPathFinder.new()
    var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
    var connections = [0, 1, 1, 2, 2, 0]
    polygon_path_finder.setup(points, connections)
    print(polygon_path_finder.is_point_inside(Vector2(0.2, 0.2))) # Prints true
    print(polygon_path_finder.is_point_inside(Vector2(1.0, 1.0))) # Prints false

```
```

    var polygonPathFinder = new PolygonPathFinder();
    Vector2[] points =
    [
        new Vector2(0.0f, 0.0f),
        new Vector2(1.0f, 0.0f),
        new Vector2(0.0f, 1.0f)
    ];
    int[] connections = [0, 1, 1, 2, 2, 0];
    polygonPathFinder.Setup(points, connections);
    GD.Print(polygonPathFinder.IsPointInside(new Vector2(0.2f, 0.2f))); // Prints True
    GD.Print(polygonPathFinder.IsPointInside(new Vector2(1.0f, 1.0f))); // Prints False

---

<span id="class_PolygonPathFinder_method_set_point_penalty"></span>

void **set_point_penalty** ( idx: [int](class_int.md#class_int), penalty: [float](class_float.md#class_float) ) [🔗](class_polygonpathfinder.md#class_PolygonPathFinder_method_set_point_penalty)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PolygonPathFinder_method_setup"></span>

void **setup** ( points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), connections: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_polygonpathfinder.md#class_PolygonPathFinder_method_setup)

Sets up **PolygonPathFinder** with an array of points that define the vertices of the polygon, and an array of indices that determine the edges of the polygon.

The length of `connections` must be even, returns an error if odd.

.. tabs::

```
```

    var polygon_path_finder = PolygonPathFinder.new()
    var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
    var connections = [0, 1, 1, 2, 2, 0]
    polygon_path_finder.setup(points, connections)

```
```

    var polygonPathFinder = new PolygonPathFinder();
    Vector2[] points =
    [
        new Vector2(0.0f, 0.0f),
        new Vector2(1.0f, 0.0f),
        new Vector2(0.0f, 1.0f)
    ];
    int[] connections = [0, 1, 1, 2, 2, 0];
    polygonPathFinder.Setup(points, connections);
