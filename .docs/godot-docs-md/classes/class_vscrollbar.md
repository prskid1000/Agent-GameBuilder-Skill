<span id="class_VScrollBar"></span>

## VScrollBar

**Inherits:** [ScrollBar](class_scrollbar.md#class_ScrollBar) **<** [Range](class_range.md#class_Range) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A vertical scrollbar that goes from top (min) to bottom (max).

### Description

A vertical scrollbar, typically used to navigate through content that extends beyond the visible height of a control. It is a [Range](class_range.md#class_Range)-based control and goes from top (min) to bottom (max). Note that this direction is the opposite of [VSlider](class_vslider.md#class_VSlider)'s.

### Properties


| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | size_flags_horizontal | `0` (overrides [Control](class_control.md#class_Control_property_size_flags_horizontal)) |
| --- | --- | --- | --- |
| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | size_flags_vertical | `1` (overrides [Control](class_control.md#class_Control_property_size_flags_vertical)) |

### Theme Properties


| [int](class_int.md#class_int) | [padding_left](class_vscrollbar.md#class_VScrollBar_theme_constant_padding_left) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [padding_right](class_vscrollbar.md#class_VScrollBar_theme_constant_padding_right) | `0` |

---

### Theme Property Descriptions

<span id="class_VScrollBar_theme_constant_padding_left"></span>

[int](class_int.md#class_int) **padding_left** = `0` [🔗](class_vscrollbar.md#class_VScrollBar_theme_constant_padding_left)

Padding between the left of the [ScrollBar.scroll](class_scrollbar.md#class_ScrollBar_theme_style_scroll) element and the [ScrollBar.grabber](class_scrollbar.md#class_ScrollBar_theme_style_grabber).

 **Note:** To apply vertical padding, modify the top/bottom content margins of [ScrollBar.scroll](class_scrollbar.md#class_ScrollBar_theme_style_scroll) instead.

---

<span id="class_VScrollBar_theme_constant_padding_right"></span>

[int](class_int.md#class_int) **padding_right** = `0` [🔗](class_vscrollbar.md#class_VScrollBar_theme_constant_padding_right)

Padding between the right of the [ScrollBar.scroll](class_scrollbar.md#class_ScrollBar_theme_style_scroll) element and the [ScrollBar.grabber](class_scrollbar.md#class_ScrollBar_theme_style_grabber).

 **Note:** To apply vertical padding, modify the top/bottom content margins of [ScrollBar.scroll](class_scrollbar.md#class_ScrollBar_theme_style_scroll) instead.
