<span id="class_AnimationNodeBlendSpace1D"></span>

## AnimationNodeBlendSpace1D

**Inherits:** [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A set of [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) s placed on a virtual axis, crossfading between the two adjacent ones. Used by [AnimationTree](class_animationtree.md#class_AnimationTree).

### Description

A resource used by [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

 **AnimationNodeBlendSpace1D** represents a virtual axis on which any type of [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) s can be added using [add_blend_point()](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_add_blend_point). Outputs the linear blend of the two [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) s adjacent to the current value.

You can set the extents of the axis with [min_space](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_min_space) and [max_space](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_max_space).

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

### Properties


| [BlendMode](class_animationnodeblendspace1d.md#enum_AnimationNodeBlendSpace1D_BlendMode) | [blend_mode](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_blend_mode) | `0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [max_space](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_max_space) | `1.0` |
| [float](class_float.md#class_float) | [min_space](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_min_space) | `-1.0` |
| [float](class_float.md#class_float) | [snap](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_snap) | `0.1` |
| [bool](class_bool.md#class_bool) | [sync](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_sync) | `false` |
| [String](class_string.md#class_String) | [value_label](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_value_label) | `"value"` |

### Methods


| void | [add_blend_point](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_add_blend_point) ( node: [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), pos: [float](class_float.md#class_float), at_index: [int](class_int.md#class_int) = -1 ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_blend_point_count](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_get_blend_point_count) ( ) const |
| [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) | [get_blend_point_node](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_get_blend_point_node) ( point: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_blend_point_position](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_get_blend_point_position) ( point: [int](class_int.md#class_int) ) const |
| void | [remove_blend_point](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_remove_blend_point) ( point: [int](class_int.md#class_int) ) |
| void | [set_blend_point_node](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_set_blend_point_node) ( point: [int](class_int.md#class_int), node: [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) ) |
| void | [set_blend_point_position](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_set_blend_point_position) ( point: [int](class_int.md#class_int), pos: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_AnimationNodeBlendSpace1D_BlendMode"></span>

enum **BlendMode**: [🔗](class_animationnodeblendspace1d.md#enum_AnimationNodeBlendSpace1D_BlendMode)

<span id="class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_INTERPOLATED"></span>

[BlendMode](class_animationnodeblendspace1d.md#enum_AnimationNodeBlendSpace1D_BlendMode) **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.

<span id="class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_DISCRETE"></span>

[BlendMode](class_animationnodeblendspace1d.md#enum_AnimationNodeBlendSpace1D_BlendMode) **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending position is closest to. Useful for frame-by-frame 2D animations.

<span id="class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_DISCRETE_CARRY"></span>

[BlendMode](class_animationnodeblendspace1d.md#enum_AnimationNodeBlendSpace1D_BlendMode) **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to [BLEND_MODE_DISCRETE](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_DISCRETE), but starts the new animation at the last animation's playback position.

---

### Property Descriptions

<span id="class_AnimationNodeBlendSpace1D_property_blend_mode"></span>

[BlendMode](class_animationnodeblendspace1d.md#enum_AnimationNodeBlendSpace1D_BlendMode) **blend_mode** = `0` [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_blend_mode)

- void **set_blend_mode** ( value: [BlendMode](class_animationnodeblendspace1d.md#enum_AnimationNodeBlendSpace1D_BlendMode) )
- [BlendMode](class_animationnodeblendspace1d.md#enum_AnimationNodeBlendSpace1D_BlendMode) **get_blend_mode** ( )

Controls the interpolation between animations.

---

<span id="class_AnimationNodeBlendSpace1D_property_max_space"></span>

[float](class_float.md#class_float) **max_space** = `1.0` [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_max_space)

- void **set_max_space** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_max_space** ( )

The blend space's axis's upper limit for the points' position. See [add_blend_point()](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_add_blend_point).

---

<span id="class_AnimationNodeBlendSpace1D_property_min_space"></span>

[float](class_float.md#class_float) **min_space** = `-1.0` [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_min_space)

- void **set_min_space** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_min_space** ( )

The blend space's axis's lower limit for the points' position. See [add_blend_point()](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_add_blend_point).

---

<span id="class_AnimationNodeBlendSpace1D_property_snap"></span>

[float](class_float.md#class_float) **snap** = `0.1` [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_snap)

- void **set_snap** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_snap** ( )

Position increment to snap to when moving a point on the axis.

---

<span id="class_AnimationNodeBlendSpace1D_property_sync"></span>

[bool](class_bool.md#class_bool) **sync** = `false` [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_sync)

- void **set_use_sync** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_sync** ( )

If `false`, the blended animations' frame are stopped when the blend value is `0`.

If `true`, forcing the blended animations to advance frame.

---

<span id="class_AnimationNodeBlendSpace1D_property_value_label"></span>

[String](class_string.md#class_String) **value_label** = `"value"` [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_property_value_label)

- void **set_value_label** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_value_label** ( )

Label of the virtual axis of the blend space.

---

### Method Descriptions

<span id="class_AnimationNodeBlendSpace1D_method_add_blend_point"></span>

void **add_blend_point** ( node: [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode), pos: [float](class_float.md#class_float), at_index: [int](class_int.md#class_int) = -1 ) [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_add_blend_point)

Adds a new point that represents a `node` on the virtual axis at a given position set by `pos`. You can insert it at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

---

<span id="class_AnimationNodeBlendSpace1D_method_get_blend_point_count"></span>

[int](class_int.md#class_int) **get_blend_point_count** ( ) *const* [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_get_blend_point_count)

Returns the number of points on the blend axis.

---

<span id="class_AnimationNodeBlendSpace1D_method_get_blend_point_node"></span>

[AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) **get_blend_point_node** ( point: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_get_blend_point_node)

Returns the [AnimationNode](class_animationnode.md#class_AnimationNode) referenced by the point at index `point`.

---

<span id="class_AnimationNodeBlendSpace1D_method_get_blend_point_position"></span>

[float](class_float.md#class_float) **get_blend_point_position** ( point: [int](class_int.md#class_int) ) *const* [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_get_blend_point_position)

Returns the position of the point at index `point`.

---

<span id="class_AnimationNodeBlendSpace1D_method_remove_blend_point"></span>

void **remove_blend_point** ( point: [int](class_int.md#class_int) ) [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_remove_blend_point)

Removes the point at index `point` from the blend axis.

---

<span id="class_AnimationNodeBlendSpace1D_method_set_blend_point_node"></span>

void **set_blend_point_node** ( point: [int](class_int.md#class_int), node: [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) ) [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_set_blend_point_node)

Changes the [AnimationNode](class_animationnode.md#class_AnimationNode) referenced by the point at index `point`.

---

<span id="class_AnimationNodeBlendSpace1D_method_set_blend_point_position"></span>

void **set_blend_point_position** ( point: [int](class_int.md#class_int), pos: [float](class_float.md#class_float) ) [🔗](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D_method_set_blend_point_position)

Updates the position of the point at index `point` on the blend axis.
