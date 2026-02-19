<span id="class_Parallax2D"></span>

## Parallax2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node used to create a parallax scrolling background.

### Description

A **Parallax2D** is used to create a parallax effect. It can move at a different speed relative to the camera movement using [scroll_scale](class_parallax2d.md#class_Parallax2D_property_scroll_scale). This creates an illusion of depth in a 2D game. If manual scrolling is desired, the [Camera2D](class_camera2d.md#class_Camera2D) position can be ignored with [ignore_camera_scroll](class_parallax2d.md#class_Parallax2D_property_ignore_camera_scroll).

 **Note:** Any changes to this node's position made after it enters the scene tree will be overridden if [ignore_camera_scroll](class_parallax2d.md#class_Parallax2D_property_ignore_camera_scroll) is `false` or [screen_offset](class_parallax2d.md#class_Parallax2D_property_screen_offset) is modified.

### Tutorials

- [2D Parallax](../tutorials/2d/2d_parallax.md)

### Properties


| [Vector2](class_vector2.md#class_Vector2) | [autoscroll](class_parallax2d.md#class_Parallax2D_property_autoscroll) | `Vector2(0, 0)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [follow_viewport](class_parallax2d.md#class_Parallax2D_property_follow_viewport) | `true` |
| [bool](class_bool.md#class_bool) | [ignore_camera_scroll](class_parallax2d.md#class_Parallax2D_property_ignore_camera_scroll) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [limit_begin](class_parallax2d.md#class_Parallax2D_property_limit_begin) | `Vector2(-10000000, -10000000)` |
| [Vector2](class_vector2.md#class_Vector2) | [limit_end](class_parallax2d.md#class_Parallax2D_property_limit_end) | `Vector2(10000000, 10000000)` |
| [PhysicsInterpolationMode](class_node.md#enum_Node_PhysicsInterpolationMode) | physics_interpolation_mode | `2` (overrides [Node](class_node.md#class_Node_property_physics_interpolation_mode)) |
| [Vector2](class_vector2.md#class_Vector2) | [repeat_size](class_parallax2d.md#class_Parallax2D_property_repeat_size) | `Vector2(0, 0)` |
| [int](class_int.md#class_int) | [repeat_times](class_parallax2d.md#class_Parallax2D_property_repeat_times) | `1` |
| [Vector2](class_vector2.md#class_Vector2) | [screen_offset](class_parallax2d.md#class_Parallax2D_property_screen_offset) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [scroll_offset](class_parallax2d.md#class_Parallax2D_property_scroll_offset) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [scroll_scale](class_parallax2d.md#class_Parallax2D_property_scroll_scale) | `Vector2(1, 1)` |

---

### Property Descriptions

<span id="class_Parallax2D_property_autoscroll"></span>

[Vector2](class_vector2.md#class_Vector2) **autoscroll** = `Vector2(0, 0)` [🔗](class_parallax2d.md#class_Parallax2D_property_autoscroll)

- void **set_autoscroll** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_autoscroll** ( )

Velocity at which the offset scrolls automatically, in pixels per second.

---

<span id="class_Parallax2D_property_follow_viewport"></span>

[bool](class_bool.md#class_bool) **follow_viewport** = `true` [🔗](class_parallax2d.md#class_Parallax2D_property_follow_viewport)

- void **set_follow_viewport** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_follow_viewport** ( )

If `true`, this **Parallax2D** is offset by the current camera's position. If the **Parallax2D** is in a [CanvasLayer](class_canvaslayer.md#class_CanvasLayer) separate from the current camera, it may be desired to match the value with [CanvasLayer.follow_viewport_enabled](class_canvaslayer.md#class_CanvasLayer_property_follow_viewport_enabled).

---

<span id="class_Parallax2D_property_ignore_camera_scroll"></span>

[bool](class_bool.md#class_bool) **ignore_camera_scroll** = `false` [🔗](class_parallax2d.md#class_Parallax2D_property_ignore_camera_scroll)

- void **set_ignore_camera_scroll** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_ignore_camera_scroll** ( )

If `true`, **Parallax2D**'s position is not affected by the position of the camera.

---

<span id="class_Parallax2D_property_limit_begin"></span>

[Vector2](class_vector2.md#class_Vector2) **limit_begin** = `Vector2(-10000000, -10000000)` [🔗](class_parallax2d.md#class_Parallax2D_property_limit_begin)

- void **set_limit_begin** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_limit_begin** ( )

Top-left limits for scrolling to begin. If the camera is outside of this limit, the **Parallax2D** stops scrolling. Must be lower than [limit_end](class_parallax2d.md#class_Parallax2D_property_limit_end) minus the viewport size to work.

---

<span id="class_Parallax2D_property_limit_end"></span>

[Vector2](class_vector2.md#class_Vector2) **limit_end** = `Vector2(10000000, 10000000)` [🔗](class_parallax2d.md#class_Parallax2D_property_limit_end)

- void **set_limit_end** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_limit_end** ( )

Bottom-right limits for scrolling to end. If the camera is outside of this limit, the **Parallax2D** will stop scrolling. Must be higher than [limit_begin](class_parallax2d.md#class_Parallax2D_property_limit_begin) and the viewport size combined to work.

---

<span id="class_Parallax2D_property_repeat_size"></span>

[Vector2](class_vector2.md#class_Vector2) **repeat_size** = `Vector2(0, 0)` [🔗](class_parallax2d.md#class_Parallax2D_property_repeat_size)

- void **set_repeat_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_repeat_size** ( )

Repeats the [Texture2D](class_texture2d.md#class_Texture2D) of each of this node's children and offsets them by this value. When scrolling, the node's position loops, giving the illusion of an infinite scrolling background if the values are larger than the screen size. If an axis is set to `0`, the [Texture2D](class_texture2d.md#class_Texture2D) will not be repeated.

---

<span id="class_Parallax2D_property_repeat_times"></span>

[int](class_int.md#class_int) **repeat_times** = `1` [🔗](class_parallax2d.md#class_Parallax2D_property_repeat_times)

- void **set_repeat_times** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_repeat_times** ( )

Overrides the amount of times the texture repeats. Each texture copy spreads evenly from the original by [repeat_size](class_parallax2d.md#class_Parallax2D_property_repeat_size). Useful for when zooming out with a camera.

---

<span id="class_Parallax2D_property_screen_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **screen_offset** = `Vector2(0, 0)` [🔗](class_parallax2d.md#class_Parallax2D_property_screen_offset)

- void **set_screen_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_screen_offset** ( )

Offset used to scroll this **Parallax2D**. This value is updated automatically unless [ignore_camera_scroll](class_parallax2d.md#class_Parallax2D_property_ignore_camera_scroll) is `true`.

---

<span id="class_Parallax2D_property_scroll_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **scroll_offset** = `Vector2(0, 0)` [🔗](class_parallax2d.md#class_Parallax2D_property_scroll_offset)

- void **set_scroll_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_scroll_offset** ( )

The **Parallax2D**'s offset. Similar to [screen_offset](class_parallax2d.md#class_Parallax2D_property_screen_offset) and [Node2D.position](class_node2d.md#class_Node2D_property_position), but will not be overridden.

 **Note:** Values will loop if [repeat_size](class_parallax2d.md#class_Parallax2D_property_repeat_size) is set higher than `0`.

---

<span id="class_Parallax2D_property_scroll_scale"></span>

[Vector2](class_vector2.md#class_Vector2) **scroll_scale** = `Vector2(1, 1)` [🔗](class_parallax2d.md#class_Parallax2D_property_scroll_scale)

- void **set_scroll_scale** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_scroll_scale** ( )

Multiplier to the final **Parallax2D**'s offset. Can be used to simulate distance from the camera.

For example, a value of `1` scrolls at the same speed as the camera. A value greater than `1` scrolls faster, making objects appear closer. Less than `1` scrolls slower, making objects appear further, and a value of `0` stops the objects completely.
