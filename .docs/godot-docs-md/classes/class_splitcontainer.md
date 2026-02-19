<span id="class_SplitContainer"></span>

## SplitContainer

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [HSplitContainer](class_hsplitcontainer.md#class_HSplitContainer), [VSplitContainer](class_vsplitcontainer.md#class_VSplitContainer)

A container that arranges child controls horizontally or vertically and provides grabbers for adjusting the split ratios between them.

### Description

A container that arranges child controls horizontally or vertically and creates grabbers between them. The grabbers can be dragged around to change the size relations between the child controls.

### Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

### Properties


| [bool](class_bool.md#class_bool) | [collapsed](class_splitcontainer.md#class_SplitContainer_property_collapsed) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [drag_area_highlight_in_editor](class_splitcontainer.md#class_SplitContainer_property_drag_area_highlight_in_editor) | `false` |
| [int](class_int.md#class_int) | [drag_area_margin_begin](class_splitcontainer.md#class_SplitContainer_property_drag_area_margin_begin) | `0` |
| [int](class_int.md#class_int) | [drag_area_margin_end](class_splitcontainer.md#class_SplitContainer_property_drag_area_margin_end) | `0` |
| [int](class_int.md#class_int) | [drag_area_offset](class_splitcontainer.md#class_SplitContainer_property_drag_area_offset) | `0` |
| [DraggerVisibility](class_splitcontainer.md#enum_SplitContainer_DraggerVisibility) | [dragger_visibility](class_splitcontainer.md#class_SplitContainer_property_dragger_visibility) | `0` |
| [bool](class_bool.md#class_bool) | [dragging_enabled](class_splitcontainer.md#class_SplitContainer_property_dragging_enabled) | `true` |
| [int](class_int.md#class_int) | [split_offset](class_splitcontainer.md#class_SplitContainer_property_split_offset) | `0` |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [split_offsets](class_splitcontainer.md#class_SplitContainer_property_split_offsets) | `PackedInt32Array(0)` |
| [bool](class_bool.md#class_bool) | [touch_dragger_enabled](class_splitcontainer.md#class_SplitContainer_property_touch_dragger_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [vertical](class_splitcontainer.md#class_SplitContainer_property_vertical) | `false` |

### Methods


| void | [clamp_split_offset](class_splitcontainer.md#class_SplitContainer_method_clamp_split_offset) ( priority_index: [int](class_int.md#class_int) = 0 ) |
| --- | --- |
| [Control](class_control.md#class_Control) | [get_drag_area_control](class_splitcontainer.md#class_SplitContainer_method_get_drag_area_control) ( ) |
| [Array](class_array.md#class_Array)\[[Control](class_control.md#class_Control)\] | [get_drag_area_controls](class_splitcontainer.md#class_SplitContainer_method_get_drag_area_controls) ( ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [touch_dragger_color](class_splitcontainer.md#class_SplitContainer_theme_color_touch_dragger_color) | `Color(1, 1, 1, 0.3)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [touch_dragger_hover_color](class_splitcontainer.md#class_SplitContainer_theme_color_touch_dragger_hover_color) | `Color(1, 1, 1, 0.6)` |
| [Color](class_color.md#class_Color) | [touch_dragger_pressed_color](class_splitcontainer.md#class_SplitContainer_theme_color_touch_dragger_pressed_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [autohide](class_splitcontainer.md#class_SplitContainer_theme_constant_autohide) | `1` |
| [int](class_int.md#class_int) | [minimum_grab_thickness](class_splitcontainer.md#class_SplitContainer_theme_constant_minimum_grab_thickness) | `6` |
| [int](class_int.md#class_int) | [separation](class_splitcontainer.md#class_SplitContainer_theme_constant_separation) | `12` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [grabber](class_splitcontainer.md#class_SplitContainer_theme_icon_grabber) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [h_grabber](class_splitcontainer.md#class_SplitContainer_theme_icon_h_grabber) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [h_touch_dragger](class_splitcontainer.md#class_SplitContainer_theme_icon_h_touch_dragger) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [touch_dragger](class_splitcontainer.md#class_SplitContainer_theme_icon_touch_dragger) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [v_grabber](class_splitcontainer.md#class_SplitContainer_theme_icon_v_grabber) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [v_touch_dragger](class_splitcontainer.md#class_SplitContainer_theme_icon_v_touch_dragger) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [split_bar_background](class_splitcontainer.md#class_SplitContainer_theme_style_split_bar_background) |

---

### Signals

<span id="class_SplitContainer_signal_drag_ended"></span>

**drag_ended** ( ) [🔗](class_splitcontainer.md#class_SplitContainer_signal_drag_ended)

Emitted when the user ends dragging.

---

<span id="class_SplitContainer_signal_drag_started"></span>

**drag_started** ( ) [🔗](class_splitcontainer.md#class_SplitContainer_signal_drag_started)

Emitted when the user starts dragging.

---

<span id="class_SplitContainer_signal_dragged"></span>

**dragged** ( offset: [int](class_int.md#class_int) ) [🔗](class_splitcontainer.md#class_SplitContainer_signal_dragged)

Emitted when any dragger is dragged by user.

---

### Enumerations

<span id="enum_SplitContainer_DraggerVisibility"></span>

enum **DraggerVisibility**: [🔗](class_splitcontainer.md#enum_SplitContainer_DraggerVisibility)

<span id="class_SplitContainer_constant_DRAGGER_VISIBLE"></span>

[DraggerVisibility](class_splitcontainer.md#enum_SplitContainer_DraggerVisibility) **DRAGGER_VISIBLE** = `0`

The split dragger icon is always visible when [autohide](class_splitcontainer.md#class_SplitContainer_theme_constant_autohide) is `false`, otherwise visible only when the cursor hovers it.

The size of the grabber icon determines the minimum [separation](class_splitcontainer.md#class_SplitContainer_theme_constant_separation).

The dragger icon is automatically hidden if the length of the grabber icon is longer than the split bar.

<span id="class_SplitContainer_constant_DRAGGER_HIDDEN"></span>

[DraggerVisibility](class_splitcontainer.md#enum_SplitContainer_DraggerVisibility) **DRAGGER_HIDDEN** = `1`

The split dragger icon is never visible regardless of the value of [autohide](class_splitcontainer.md#class_SplitContainer_theme_constant_autohide).

The size of the grabber icon determines the minimum [separation](class_splitcontainer.md#class_SplitContainer_theme_constant_separation).

<span id="class_SplitContainer_constant_DRAGGER_HIDDEN_COLLAPSED"></span>

[DraggerVisibility](class_splitcontainer.md#enum_SplitContainer_DraggerVisibility) **DRAGGER_HIDDEN_COLLAPSED** = `2`

The split dragger icon is not visible, and the split bar is collapsed to zero thickness.

---

### Property Descriptions

<span id="class_SplitContainer_property_collapsed"></span>

[bool](class_bool.md#class_bool) **collapsed** = `false` [🔗](class_splitcontainer.md#class_SplitContainer_property_collapsed)

- void **set_collapsed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collapsed** ( )

If `true`, the draggers will be disabled and the children will be sized as if all [split_offsets](class_splitcontainer.md#class_SplitContainer_property_split_offsets) were `0`.

---

<span id="class_SplitContainer_property_drag_area_highlight_in_editor"></span>

[bool](class_bool.md#class_bool) **drag_area_highlight_in_editor** = `false` [🔗](class_splitcontainer.md#class_SplitContainer_property_drag_area_highlight_in_editor)

- void **set_drag_area_highlight_in_editor** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drag_area_highlight_in_editor_enabled** ( )

Highlights the drag area [Rect2](class_rect2.md#class_Rect2) so you can see where it is during development. The drag area is gold if [dragging_enabled](class_splitcontainer.md#class_SplitContainer_property_dragging_enabled) is `true`, and red if `false`.

---

<span id="class_SplitContainer_property_drag_area_margin_begin"></span>

[int](class_int.md#class_int) **drag_area_margin_begin** = `0` [🔗](class_splitcontainer.md#class_SplitContainer_property_drag_area_margin_begin)

- void **set_drag_area_margin_begin** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_drag_area_margin_begin** ( )

Reduces the size of the drag area and split bar [split_bar_background](class_splitcontainer.md#class_SplitContainer_theme_style_split_bar_background) at the beginning of the container.

---

<span id="class_SplitContainer_property_drag_area_margin_end"></span>

[int](class_int.md#class_int) **drag_area_margin_end** = `0` [🔗](class_splitcontainer.md#class_SplitContainer_property_drag_area_margin_end)

- void **set_drag_area_margin_end** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_drag_area_margin_end** ( )

Reduces the size of the drag area and split bar [split_bar_background](class_splitcontainer.md#class_SplitContainer_theme_style_split_bar_background) at the end of the container.

---

<span id="class_SplitContainer_property_drag_area_offset"></span>

[int](class_int.md#class_int) **drag_area_offset** = `0` [🔗](class_splitcontainer.md#class_SplitContainer_property_drag_area_offset)

- void **set_drag_area_offset** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_drag_area_offset** ( )

Shifts the drag area in the axis of the container to prevent the drag area from overlapping the [ScrollBar](class_scrollbar.md#class_ScrollBar) or other selectable [Control](class_control.md#class_Control) of a child node.

---

<span id="class_SplitContainer_property_dragger_visibility"></span>

[DraggerVisibility](class_splitcontainer.md#enum_SplitContainer_DraggerVisibility) **dragger_visibility** = `0` [🔗](class_splitcontainer.md#class_SplitContainer_property_dragger_visibility)

- void **set_dragger_visibility** ( value: [DraggerVisibility](class_splitcontainer.md#enum_SplitContainer_DraggerVisibility) )
- [DraggerVisibility](class_splitcontainer.md#enum_SplitContainer_DraggerVisibility) **get_dragger_visibility** ( )

Determines the dragger's visibility. This property does not determine whether dragging is enabled or not. Use [dragging_enabled](class_splitcontainer.md#class_SplitContainer_property_dragging_enabled) for that.

---

<span id="class_SplitContainer_property_dragging_enabled"></span>

[bool](class_bool.md#class_bool) **dragging_enabled** = `true` [🔗](class_splitcontainer.md#class_SplitContainer_property_dragging_enabled)

- void **set_dragging_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_dragging_enabled** ( )

Enables or disables split dragging.

---

<span id="class_SplitContainer_property_split_offset"></span>

[int](class_int.md#class_int) **split_offset** = `0` [🔗](class_splitcontainer.md#class_SplitContainer_property_split_offset)

- void **set_split_offset** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_split_offset** ( )

**Deprecated:** Use [split_offsets](class_splitcontainer.md#class_SplitContainer_property_split_offsets) instead. The first element of the array is the split offset between the first two children.

The first element of [split_offsets](class_splitcontainer.md#class_SplitContainer_property_split_offsets).

---

<span id="class_SplitContainer_property_split_offsets"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **split_offsets** = `PackedInt32Array(0)` [🔗](class_splitcontainer.md#class_SplitContainer_property_split_offsets)

- void **set_split_offsets** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_split_offsets** ( )

Offsets for each dragger in pixels. Each one is the offset of the split between the [Control](class_control.md#class_Control) nodes before and after the dragger, with `0` being the default position. The default position is based on the [Control](class_control.md#class_Control) nodes expand flags and minimum sizes. See [Control.size_flags_horizontal](class_control.md#class_Control_property_size_flags_horizontal), [Control.size_flags_vertical](class_control.md#class_Control_property_size_flags_vertical), and [Control.size_flags_stretch_ratio](class_control.md#class_Control_property_size_flags_stretch_ratio).

If none of the [Control](class_control.md#class_Control) nodes before the dragger are expanded, the default position will be at the start of the **SplitContainer**. If none of the [Control](class_control.md#class_Control) nodes after the dragger are expanded, the default position will be at the end of the **SplitContainer**. If the dragger is in between expanded [Control](class_control.md#class_Control) nodes, the default position will be in the middle, based on the [Control.size_flags_stretch_ratio](class_control.md#class_Control_property_size_flags_stretch_ratio) s and minimum sizes.

 **Note:** If the split offsets cause [Control](class_control.md#class_Control) nodes to overlap, the first split will take priority when resolving the positions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_SplitContainer_property_touch_dragger_enabled"></span>

[bool](class_bool.md#class_bool) **touch_dragger_enabled** = `false` [🔗](class_splitcontainer.md#class_SplitContainer_property_touch_dragger_enabled)

- void **set_touch_dragger_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_touch_dragger_enabled** ( )

If `true`, a touch-friendly drag handle will be enabled for better usability on smaller screens. Unlike the standard grabber, this drag handle overlaps the **SplitContainer**'s children and does not affect their minimum separation. The standard grabber will no longer be drawn when this option is enabled.

---

<span id="class_SplitContainer_property_vertical"></span>

[bool](class_bool.md#class_bool) **vertical** = `false` [🔗](class_splitcontainer.md#class_SplitContainer_property_vertical)

- void **set_vertical** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_vertical** ( )

If `true`, the **SplitContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HSplitContainer](class_hsplitcontainer.md#class_HSplitContainer) and [VSplitContainer](class_vsplitcontainer.md#class_VSplitContainer).

---

### Method Descriptions

<span id="class_SplitContainer_method_clamp_split_offset"></span>

void **clamp_split_offset** ( priority_index: [int](class_int.md#class_int) = 0 ) [🔗](class_splitcontainer.md#class_SplitContainer_method_clamp_split_offset)

Clamps the [split_offsets](class_splitcontainer.md#class_SplitContainer_property_split_offsets) values to ensure they are within valid ranges and do not overlap with each other. When overlaps occur, this method prioritizes one split offset (at index `priority_index`) by clamping any overlapping split offsets to it.

---

<span id="class_SplitContainer_method_get_drag_area_control"></span>

[Control](class_control.md#class_Control) **get_drag_area_control** ( ) [🔗](class_splitcontainer.md#class_SplitContainer_method_get_drag_area_control)

**Deprecated:** Use the first element of [get_drag_area_controls()](class_splitcontainer.md#class_SplitContainer_method_get_drag_area_controls) instead.

Returns the drag area [Control](class_control.md#class_Control). For example, you can move a pre-configured button into the drag area [Control](class_control.md#class_Control) so that it rides along with the split bar. Try setting the [Button](class_button.md#class_Button) anchors to `center` prior to the `reparent()` call.

::

    $BarnacleButton.reparent($SplitContainer.get_drag_area_control())

 **Note:** The drag area [Control](class_control.md#class_Control) is drawn over the **SplitContainer**'s children, so [CanvasItem](class_canvasitem.md#class_CanvasItem) draw objects called from the [Control](class_control.md#class_Control) and children added to the [Control](class_control.md#class_Control) will also appear over the **SplitContainer**'s children. Try setting [Control.mouse_filter](class_control.md#class_Control_property_mouse_filter) of custom children to [Control.MOUSE_FILTER_IGNORE](class_control.md#class_Control_constant_MOUSE_FILTER_IGNORE) to prevent blocking the mouse from dragging if desired.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash.

---

<span id="class_SplitContainer_method_get_drag_area_controls"></span>

[Array](class_array.md#class_Array)\[[Control](class_control.md#class_Control)\] **get_drag_area_controls** ( ) [🔗](class_splitcontainer.md#class_SplitContainer_method_get_drag_area_controls)

Returns an [Array](class_array.md#class_Array) of the drag area [Control](class_control.md#class_Control) s. These are the interactable [Control](class_control.md#class_Control) nodes between each child. For example, this can be used to add a pre-configured button to a drag area [Control](class_control.md#class_Control) so that it rides along with the split bar. Try setting the [Button](class_button.md#class_Button) anchors to `center` prior to the [Node.reparent()](class_node.md#class_Node_method_reparent) call.

::

    $BarnacleButton.reparent($SplitContainer.get_drag_area_controls()[0])

 **Note:** The drag area [Control](class_control.md#class_Control) s are drawn over the **SplitContainer**'s children, so [CanvasItem](class_canvasitem.md#class_CanvasItem) draw objects called from a drag area and children added to it will also appear over the **SplitContainer**'s children. Try setting [Control.mouse_filter](class_control.md#class_Control_property_mouse_filter) of custom children to [Control.MOUSE_FILTER_IGNORE](class_control.md#class_Control_constant_MOUSE_FILTER_IGNORE) to prevent blocking the mouse from dragging if desired.

 **Warning:** These are required internal nodes, removing or freeing them may cause a crash.

---

### Theme Property Descriptions

<span id="class_SplitContainer_theme_color_touch_dragger_color"></span>

[Color](class_color.md#class_Color) **touch_dragger_color** = `Color(1, 1, 1, 0.3)` [🔗](class_splitcontainer.md#class_SplitContainer_theme_color_touch_dragger_color)

The color of the touch dragger.

---

<span id="class_SplitContainer_theme_color_touch_dragger_hover_color"></span>

[Color](class_color.md#class_Color) **touch_dragger_hover_color** = `Color(1, 1, 1, 0.6)` [🔗](class_splitcontainer.md#class_SplitContainer_theme_color_touch_dragger_hover_color)

The color of the touch dragger when hovered.

---

<span id="class_SplitContainer_theme_color_touch_dragger_pressed_color"></span>

[Color](class_color.md#class_Color) **touch_dragger_pressed_color** = `Color(1, 1, 1, 1)` [🔗](class_splitcontainer.md#class_SplitContainer_theme_color_touch_dragger_pressed_color)

The color of the touch dragger when pressed.

---

<span id="class_SplitContainer_theme_constant_autohide"></span>

[int](class_int.md#class_int) **autohide** = `1` [🔗](class_splitcontainer.md#class_SplitContainer_theme_constant_autohide)

Boolean value. If `1` (`true`), the grabbers will hide automatically when they aren't under the cursor. If `0` (`false`), the grabbers are always visible. The [dragger_visibility](class_splitcontainer.md#class_SplitContainer_property_dragger_visibility) must be [DRAGGER_VISIBLE](class_splitcontainer.md#class_SplitContainer_constant_DRAGGER_VISIBLE).

---

<span id="class_SplitContainer_theme_constant_minimum_grab_thickness"></span>

[int](class_int.md#class_int) **minimum_grab_thickness** = `6` [🔗](class_splitcontainer.md#class_SplitContainer_theme_constant_minimum_grab_thickness)

The minimum thickness of the area users can click on to grab a split bar. This ensures that the split bar can still be dragged if [separation](class_splitcontainer.md#class_SplitContainer_theme_constant_separation) or [h_grabber](class_splitcontainer.md#class_SplitContainer_theme_icon_h_grabber) / [v_grabber](class_splitcontainer.md#class_SplitContainer_theme_icon_v_grabber)'s size is too narrow to easily select.

---

<span id="class_SplitContainer_theme_constant_separation"></span>

[int](class_int.md#class_int) **separation** = `12` [🔗](class_splitcontainer.md#class_SplitContainer_theme_constant_separation)

The split bar thickness, i.e., the gap between each child of the container. This is overridden by the size of the grabber icon if [dragger_visibility](class_splitcontainer.md#class_SplitContainer_property_dragger_visibility) is set to [DRAGGER_VISIBLE](class_splitcontainer.md#class_SplitContainer_constant_DRAGGER_VISIBLE), or [DRAGGER_HIDDEN](class_splitcontainer.md#class_SplitContainer_constant_DRAGGER_HIDDEN), and [separation](class_splitcontainer.md#class_SplitContainer_theme_constant_separation) is smaller than the size of the grabber icon in the same axis.

 **Note:** To obtain [separation](class_splitcontainer.md#class_SplitContainer_theme_constant_separation) values less than the size of the grabber icon, for example a `1 px` hairline, set [h_grabber](class_splitcontainer.md#class_SplitContainer_theme_icon_h_grabber) or [v_grabber](class_splitcontainer.md#class_SplitContainer_theme_icon_v_grabber) to a new [ImageTexture](class_imagetexture.md#class_ImageTexture), which effectively sets the grabber icon size to `0 px`.

---

<span id="class_SplitContainer_theme_icon_grabber"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **grabber** [🔗](class_splitcontainer.md#class_SplitContainer_theme_icon_grabber)

The icon used for the grabbers drawn in the separations. This is only used in [HSplitContainer](class_hsplitcontainer.md#class_HSplitContainer) and [VSplitContainer](class_vsplitcontainer.md#class_VSplitContainer). For **SplitContainer**, see [h_grabber](class_splitcontainer.md#class_SplitContainer_theme_icon_h_grabber) and [v_grabber](class_splitcontainer.md#class_SplitContainer_theme_icon_v_grabber) instead.

---

<span id="class_SplitContainer_theme_icon_h_grabber"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **h_grabber** [🔗](class_splitcontainer.md#class_SplitContainer_theme_icon_h_grabber)

The icon used for the grabbers drawn in the separations when [vertical](class_splitcontainer.md#class_SplitContainer_property_vertical) is `false`.

---

<span id="class_SplitContainer_theme_icon_h_touch_dragger"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **h_touch_dragger** [🔗](class_splitcontainer.md#class_SplitContainer_theme_icon_h_touch_dragger)

The icon used for the drag handle when [touch_dragger_enabled](class_splitcontainer.md#class_SplitContainer_property_touch_dragger_enabled) is `true` and [vertical](class_splitcontainer.md#class_SplitContainer_property_vertical) is `false`.

---

<span id="class_SplitContainer_theme_icon_touch_dragger"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **touch_dragger** [🔗](class_splitcontainer.md#class_SplitContainer_theme_icon_touch_dragger)

The icon used for the drag handle when [touch_dragger_enabled](class_splitcontainer.md#class_SplitContainer_property_touch_dragger_enabled) is `true`. This is only used in [HSplitContainer](class_hsplitcontainer.md#class_HSplitContainer) and [VSplitContainer](class_vsplitcontainer.md#class_VSplitContainer). For **SplitContainer**, see [h_touch_dragger](class_splitcontainer.md#class_SplitContainer_theme_icon_h_touch_dragger) and [v_touch_dragger](class_splitcontainer.md#class_SplitContainer_theme_icon_v_touch_dragger) instead.

---

<span id="class_SplitContainer_theme_icon_v_grabber"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **v_grabber** [🔗](class_splitcontainer.md#class_SplitContainer_theme_icon_v_grabber)

The icon used for the grabbers drawn in the separations when [vertical](class_splitcontainer.md#class_SplitContainer_property_vertical) is `true`.

---

<span id="class_SplitContainer_theme_icon_v_touch_dragger"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **v_touch_dragger** [🔗](class_splitcontainer.md#class_SplitContainer_theme_icon_v_touch_dragger)

The icon used for the drag handle when [touch_dragger_enabled](class_splitcontainer.md#class_SplitContainer_property_touch_dragger_enabled) is `true` and [vertical](class_splitcontainer.md#class_SplitContainer_property_vertical) is `true`.

---

<span id="class_SplitContainer_theme_style_split_bar_background"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **split_bar_background** [🔗](class_splitcontainer.md#class_SplitContainer_theme_style_split_bar_background)

Determines the background of the split bar if its thickness is greater than zero.
