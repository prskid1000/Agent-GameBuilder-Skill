<span id="class_AnimationNodeBlendSpace2D"></span>

## AnimationNodeBlendSpace2D

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A set of [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) s placed on 2D coordinates, crossfading between the three adjacent ones. Used by [AnimationTree](class_animationtree.md#class_AnimationTree).

### Description

A resource used by [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

 **AnimationNodeBlendSpace2D** represents a virtual 2D space on which [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) s are placed. Outputs the linear blend of the three adjacent animations using a [Vector2](class_vector2.md#class_Vector2) weight. Adjacent in this context means the three [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) s making up the triangle that contains the current value.

You can add vertices to the blend space with [add_blend_point()](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_add_blend_point) and automatically triangulate it by setting [auto_triangles](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_auto_triangles) to `true`. Otherwise, use [add_triangle()](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_add_triangle) and [remove_triangle()](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_remove_triangle) to triangulate the blend space by hand.

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

- Third Person Shooter (TPS) Demo

### Properties


| [bool](class_bool.md#class_bool) | [auto_triangles](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_auto_triangles) | `true` |
| --- | --- | --- |
| [BlendMode](class_animationnodeblendspace2d.md#enum_AnimationNodeBlendSpace2D_BlendMode) | [blend_mode](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_blend_mode) | `0` |
| [Vector2](class_vector2.md#class_Vector2) | [max_space](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_max_space) | `Vector2(1, 1)` |
| [Vector2](class_vector2.md#class_Vector2) | [min_space](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_min_space) | `Vector2(-1, -1)` |
| [Vector2](class_vector2.md#class_Vector2) | [snap](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_snap) | `Vector2(0.1, 0.1)` |
| [bool](class_bool.md#class_bool) | [sync](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_sync) | `false` |
| [String](class_string.md#class_String) | [x_label](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_x_label) | `"x"` |
| [String](class_string.md#class_String) | [y_label](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_y_label) | `"y"` |

### Methods


| void | [add_blend_point](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_add_blend_point) ( node: [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), pos: [Vector2](class_vector2.md#class_Vector2), at_index: [int](class_int.md#class_int) = -1 ) |
| --- | --- |
| void | [add_triangle](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_add_triangle) ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int), z: [int](class_int.md#class_int), at_index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [get_blend_point_count](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_blend_point_count) ( ) const |
| [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) | [get_blend_point_node](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_blend_point_node) ( point: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_blend_point_position](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_blend_point_position) ( point: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_triangle_count](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_triangle_count) ( ) const |
| [int](class_int.md#class_int) | [get_triangle_point](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_triangle_point) ( triangle: [int](class_int.md#class_int), point: [int](class_int.md#class_int) ) |
| void | [remove_blend_point](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_remove_blend_point) ( point: [int](class_int.md#class_int) ) |
| void | [remove_triangle](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_remove_triangle) ( triangle: [int](class_int.md#class_int) ) |
| void | [set_blend_point_node](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_set_blend_point_node) ( point: [int](class_int.md#class_int), node: [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) ) |
| void | [set_blend_point_position](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_set_blend_point_position) ( point: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2) ) |

---

### Signals

<span id="class_AnimationNodeBlendSpace2D_signal_triangles_updated"></span>

**triangles_updated** ( ) [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_signal_triangles_updated)

Emitted every time the blend space's triangles are created, removed, or when one of their vertices changes position.

---

### Enumerations

<span id="enum_AnimationNodeBlendSpace2D_BlendMode"></span>

enum **BlendMode**: [🔗](class_animationnodeblendspace2d.md#enum_AnimationNodeBlendSpace2D_BlendMode)

<span id="class_AnimationNodeBlendSpace2D_constant_BLEND_MODE_INTERPOLATED"></span>

[BlendMode](class_animationnodeblendspace2d.md#enum_AnimationNodeBlendSpace2D_BlendMode) **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.

<span id="class_AnimationNodeBlendSpace2D_constant_BLEND_MODE_DISCRETE"></span>

[BlendMode](class_animationnodeblendspace2d.md#enum_AnimationNodeBlendSpace2D_BlendMode) **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending position is closest to. Useful for frame-by-frame 2D animations.

<span id="class_AnimationNodeBlendSpace2D_constant_BLEND_MODE_DISCRETE_CARRY"></span>

[BlendMode](class_animationnodeblendspace2d.md#enum_AnimationNodeBlendSpace2D_BlendMode) **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to [BLEND_MODE_DISCRETE](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_constant_BLEND_MODE_DISCRETE), but starts the new animation at the last animation's playback position.

---

### Property Descriptions

<span id="class_AnimationNodeBlendSpace2D_property_auto_triangles"></span>

[bool](class_bool.md#class_bool) **auto_triangles** = `true` [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_auto_triangles)

- void **set_auto_triangles** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_auto_triangles** ( )

If `true`, the blend space is triangulated automatically. The mesh updates every time you add or remove points with [add_blend_point()](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_add_blend_point) and [remove_blend_point()](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_remove_blend_point).

---

<span id="class_AnimationNodeBlendSpace2D_property_blend_mode"></span>

[BlendMode](class_animationnodeblendspace2d.md#enum_AnimationNodeBlendSpace2D_BlendMode) **blend_mode** = `0` [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_blend_mode)

- void **set_blend_mode** ( value: [BlendMode](class_animationnodeblendspace2d.md#enum_AnimationNodeBlendSpace2D_BlendMode) )
- [BlendMode](class_animationnodeblendspace2d.md#enum_AnimationNodeBlendSpace2D_BlendMode) **get_blend_mode** ( )

Controls the interpolation between animations.

---

<span id="class_AnimationNodeBlendSpace2D_property_max_space"></span>

[Vector2](class_vector2.md#class_Vector2) **max_space** = `Vector2(1, 1)` [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_max_space)

- void **set_max_space** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_max_space** ( )

The blend space's X and Y axes' upper limit for the points' position. See [add_blend_point()](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_add_blend_point).

---

<span id="class_AnimationNodeBlendSpace2D_property_min_space"></span>

[Vector2](class_vector2.md#class_Vector2) **min_space** = `Vector2(-1, -1)` [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_min_space)

- void **set_min_space** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_min_space** ( )

The blend space's X and Y axes' lower limit for the points' position. See [add_blend_point()](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_add_blend_point).

---

<span id="class_AnimationNodeBlendSpace2D_property_snap"></span>

[Vector2](class_vector2.md#class_Vector2) **snap** = `Vector2(0.1, 0.1)` [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_snap)

- void **set_snap** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_snap** ( )

Position increment to snap to when moving a point.

---

<span id="class_AnimationNodeBlendSpace2D_property_sync"></span>

[bool](class_bool.md#class_bool) **sync** = `false` [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_sync)

- void **set_use_sync** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_sync** ( )

If `false`, the blended animations' frame are stopped when the blend value is `0`.

If `true`, forcing the blended animations to advance frame.

---

<span id="class_AnimationNodeBlendSpace2D_property_x_label"></span>

[String](class_string.md#class_String) **x_label** = `"x"` [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_x_label)

- void **set_x_label** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_x_label** ( )

Name of the blend space's X axis.

---

<span id="class_AnimationNodeBlendSpace2D_property_y_label"></span>

[String](class_string.md#class_String) **y_label** = `"y"` [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_property_y_label)

- void **set_y_label** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_y_label** ( )

Name of the blend space's Y axis.

---

### Method Descriptions

<span id="class_AnimationNodeBlendSpace2D_method_add_blend_point"></span>

void **add_blend_point** ( node: [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), pos: [Vector2](class_vector2.md#class_Vector2), at_index: [int](class_int.md#class_int) = -1 ) [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_add_blend_point)

Adds a new point that represents a `node` at the position set by `pos`. You can insert it at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

---

<span id="class_AnimationNodeBlendSpace2D_method_add_triangle"></span>

void **add_triangle** ( x: [int](class_int.md#class_int), y: [int](class_int.md#class_int), z: [int](class_int.md#class_int), at_index: [int](class_int.md#class_int) = -1 ) [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_add_triangle)

Creates a new triangle using three points `x`, `y`, and `z`. Triangles can overlap. You can insert the triangle at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

---

<span id="class_AnimationNodeBlendSpace2D_method_get_blend_point_count"></span>

[int](class_int.md#class_int) **get_blend_point_count** ( ) *const* [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_blend_point_count)

Returns the number of points in the blend space.

---

<span id="class_AnimationNodeBlendSpace2D_method_get_blend_point_node"></span>

[AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) **get_blend_point_node** ( point: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_blend_point_node)

Returns the [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) referenced by the point at index `point`.

---

<span id="class_AnimationNodeBlendSpace2D_method_get_blend_point_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_blend_point_position** ( point: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_blend_point_position)

Returns the position of the point at index `point`.

---

<span id="class_AnimationNodeBlendSpace2D_method_get_triangle_count"></span>

[int](class_int.md#class_int) **get_triangle_count** ( ) *const* [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_triangle_count)

Returns the number of triangles in the blend space.

---

<span id="class_AnimationNodeBlendSpace2D_method_get_triangle_point"></span>

[int](class_int.md#class_int) **get_triangle_point** ( triangle: [int](class_int.md#class_int), point: [int](class_int.md#class_int) ) [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_get_triangle_point)

Returns the position of the point at index `point` in the triangle of index `triangle`.

---

<span id="class_AnimationNodeBlendSpace2D_method_remove_blend_point"></span>

void **remove_blend_point** ( point: [int](class_int.md#class_int) ) [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_remove_blend_point)

Removes the point at index `point` from the blend space.

---

<span id="class_AnimationNodeBlendSpace2D_method_remove_triangle"></span>

void **remove_triangle** ( triangle: [int](class_int.md#class_int) ) [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_remove_triangle)

Removes the triangle at index `triangle` from the blend space.

---

<span id="class_AnimationNodeBlendSpace2D_method_set_blend_point_node"></span>

void **set_blend_point_node** ( point: [int](class_int.md#class_int), node: [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) ) [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_set_blend_point_node)

Changes the [AnimationNode](class_animationnode.md#class_AnimationNode) referenced by the point at index `point`.

---

<span id="class_AnimationNodeBlendSpace2D_method_set_blend_point_position"></span>

void **set_blend_point_position** ( point: [int](class_int.md#class_int), pos: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D_method_set_blend_point_position)

Updates the position of the point at index `point` in the blend space.
