<span id="class_Path3D"></span>

## Path3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Contains a [Curve3D](class_curve3d.md#class_Curve3D) path for [PathFollow3D](class_pathfollow3d.md#class_PathFollow3D) nodes to follow.

### Description

Can have [PathFollow3D](class_pathfollow3d.md#class_PathFollow3D) child nodes moving along the [Curve3D](class_curve3d.md#class_Curve3D). See [PathFollow3D](class_pathfollow3d.md#class_PathFollow3D) for more information on the usage.

Note that the path is considered as relative to the moved nodes (children of [PathFollow3D](class_pathfollow3d.md#class_PathFollow3D)). As such, the curve should usually start with a zero vector `(0, 0, 0)`.

### Properties


| [Curve3D](class_curve3d.md#class_Curve3D) | [curve](class_path3d.md#class_Path3D_property_curve) |
| --- | --- |
| [Color](class_color.md#class_Color) | [debug_custom_color](class_path3d.md#class_Path3D_property_debug_custom_color) | `Color(0, 0, 0, 1)` |

---

### Signals

<span id="class_Path3D_signal_curve_changed"></span>

**curve_changed** ( ) [🔗](class_path3d.md#class_Path3D_signal_curve_changed)

Emitted when the [curve](class_path3d.md#class_Path3D_property_curve) changes.

---

<span id="class_Path3D_signal_debug_color_changed"></span>

**debug_color_changed** ( ) [🔗](class_path3d.md#class_Path3D_signal_debug_color_changed)

Emitted when the [debug_custom_color](class_path3d.md#class_Path3D_property_debug_custom_color) changes.

---

### Property Descriptions

<span id="class_Path3D_property_curve"></span>

[Curve3D](class_curve3d.md#class_Curve3D) **curve** [🔗](class_path3d.md#class_Path3D_property_curve)

- void **set_curve** ( value: [Curve3D](class_curve3d.md#class_Curve3D) )
- [Curve3D](class_curve3d.md#class_Curve3D) **get_curve** ( )

A [Curve3D](class_curve3d.md#class_Curve3D) describing the path.

---

<span id="class_Path3D_property_debug_custom_color"></span>

[Color](class_color.md#class_Color) **debug_custom_color** = `Color(0, 0, 0, 1)` [🔗](class_path3d.md#class_Path3D_property_debug_custom_color)

- void **set_debug_custom_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_debug_custom_color** ( )

The custom color used to draw the path in the editor. If set to [Color.BLACK](class_color.md#class_Color_constant_BLACK) (as by default), the color set in ProjectSettings.debug/shapes/paths/geometry_color is used.
