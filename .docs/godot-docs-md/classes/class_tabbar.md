<span id="class_TabBar"></span>

## TabBar

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A control that provides a horizontal bar with tabs.

### Description

A control that provides a horizontal bar with tabs. Similar to [TabContainer](class_tabcontainer.md#class_TabContainer) but is only in charge of drawing tabs, not interacting with children.

### Properties


| [bool](class_bool.md#class_bool) | [clip_tabs](class_tabbar.md#class_TabBar_property_clip_tabs) | `true` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [close_with_middle_mouse](class_tabbar.md#class_TabBar_property_close_with_middle_mouse) | `true` |
| [int](class_int.md#class_int) | [current_tab](class_tabbar.md#class_TabBar_property_current_tab) | `-1` |
| [bool](class_bool.md#class_bool) | [deselect_enabled](class_tabbar.md#class_TabBar_property_deselect_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [drag_to_rearrange_enabled](class_tabbar.md#class_TabBar_property_drag_to_rearrange_enabled) | `false` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `2` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [int](class_int.md#class_int) | [max_tab_width](class_tabbar.md#class_TabBar_property_max_tab_width) | `0` |
| [bool](class_bool.md#class_bool) | [scroll_to_selected](class_tabbar.md#class_TabBar_property_scroll_to_selected) | `true` |
| [bool](class_bool.md#class_bool) | [scrolling_enabled](class_tabbar.md#class_TabBar_property_scrolling_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [select_with_rmb](class_tabbar.md#class_TabBar_property_select_with_rmb) | `false` |
| [bool](class_bool.md#class_bool) | [switch_on_drag_hover](class_tabbar.md#class_TabBar_property_switch_on_drag_hover) | `true` |
| [AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) | [tab_alignment](class_tabbar.md#class_TabBar_property_tab_alignment) | `0` |
| [CloseButtonDisplayPolicy](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy) | [tab_close_display_policy](class_tabbar.md#class_TabBar_property_tab_close_display_policy) | `0` |
| [int](class_int.md#class_int) | [tab_count](class_tabbar.md#class_TabBar_property_tab_count) | `0` |
| [int](class_int.md#class_int) | [tabs_rearrange_group](class_tabbar.md#class_TabBar_property_tabs_rearrange_group) | `-1` |

### Methods


| void | [add_tab](class_tabbar.md#class_TabBar_method_add_tab) ( title: [String](class_string.md#class_String) = "", icon: [Texture2D](class_texture2d.md#class_Texture2D) = null ) |
| --- | --- |
| void | [clear_tabs](class_tabbar.md#class_TabBar_method_clear_tabs) ( ) |
| void | [ensure_tab_visible](class_tabbar.md#class_TabBar_method_ensure_tab_visible) ( idx: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [get_offset_buttons_visible](class_tabbar.md#class_TabBar_method_get_offset_buttons_visible) ( ) const |
| [int](class_int.md#class_int) | [get_previous_tab](class_tabbar.md#class_TabBar_method_get_previous_tab) ( ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_tab_button_icon](class_tabbar.md#class_TabBar_method_get_tab_button_icon) ( tab_idx: [int](class_int.md#class_int) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_tab_icon](class_tabbar.md#class_TabBar_method_get_tab_icon) ( tab_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_tab_icon_max_width](class_tabbar.md#class_TabBar_method_get_tab_icon_max_width) ( tab_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_tab_idx_at_point](class_tabbar.md#class_TabBar_method_get_tab_idx_at_point) ( point: [Vector2](class_vector2.md#class_Vector2) ) const |
| [String](class_string.md#class_String) | [get_tab_language](class_tabbar.md#class_TabBar_method_get_tab_language) ( tab_idx: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_tab_metadata](class_tabbar.md#class_TabBar_method_get_tab_metadata) ( tab_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_tab_offset](class_tabbar.md#class_TabBar_method_get_tab_offset) ( ) const |
| [Rect2](class_rect2.md#class_Rect2) | [get_tab_rect](class_tabbar.md#class_TabBar_method_get_tab_rect) ( tab_idx: [int](class_int.md#class_int) ) const |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [get_tab_text_direction](class_tabbar.md#class_TabBar_method_get_tab_text_direction) ( tab_idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_tab_title](class_tabbar.md#class_TabBar_method_get_tab_title) ( tab_idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_tab_tooltip](class_tabbar.md#class_TabBar_method_get_tab_tooltip) ( tab_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_tab_disabled](class_tabbar.md#class_TabBar_method_is_tab_disabled) ( tab_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_tab_hidden](class_tabbar.md#class_TabBar_method_is_tab_hidden) ( tab_idx: [int](class_int.md#class_int) ) const |
| void | [move_tab](class_tabbar.md#class_TabBar_method_move_tab) ( from: [int](class_int.md#class_int), to: [int](class_int.md#class_int) ) |
| void | [remove_tab](class_tabbar.md#class_TabBar_method_remove_tab) ( tab_idx: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [select_next_available](class_tabbar.md#class_TabBar_method_select_next_available) ( ) |
| [bool](class_bool.md#class_bool) | [select_previous_available](class_tabbar.md#class_TabBar_method_select_previous_available) ( ) |
| void | [set_tab_button_icon](class_tabbar.md#class_TabBar_method_set_tab_button_icon) ( tab_idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_tab_disabled](class_tabbar.md#class_TabBar_method_set_tab_disabled) ( tab_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) |
| void | [set_tab_hidden](class_tabbar.md#class_TabBar_method_set_tab_hidden) ( tab_idx: [int](class_int.md#class_int), hidden: [bool](class_bool.md#class_bool) ) |
| void | [set_tab_icon](class_tabbar.md#class_TabBar_method_set_tab_icon) ( tab_idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_tab_icon_max_width](class_tabbar.md#class_TabBar_method_set_tab_icon_max_width) ( tab_idx: [int](class_int.md#class_int), width: [int](class_int.md#class_int) ) |
| void | [set_tab_language](class_tabbar.md#class_TabBar_method_set_tab_language) ( tab_idx: [int](class_int.md#class_int), language: [String](class_string.md#class_String) ) |
| void | [set_tab_metadata](class_tabbar.md#class_TabBar_method_set_tab_metadata) ( tab_idx: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) |
| void | [set_tab_text_direction](class_tabbar.md#class_TabBar_method_set_tab_text_direction) ( tab_idx: [int](class_int.md#class_int), direction: [TextDirection](class_control.md#enum_Control_TextDirection) ) |
| void | [set_tab_title](class_tabbar.md#class_TabBar_method_set_tab_title) ( tab_idx: [int](class_int.md#class_int), title: [String](class_string.md#class_String) ) |
| void | [set_tab_tooltip](class_tabbar.md#class_TabBar_method_set_tab_tooltip) ( tab_idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [drop_mark_color](class_tabbar.md#class_TabBar_theme_color_drop_mark_color) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_disabled_color](class_tabbar.md#class_TabBar_theme_color_font_disabled_color) | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class_Color) | [font_hovered_color](class_tabbar.md#class_TabBar_theme_color_font_hovered_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_outline_color](class_tabbar.md#class_TabBar_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_selected_color](class_tabbar.md#class_TabBar_theme_color_font_selected_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_unselected_color](class_tabbar.md#class_TabBar_theme_color_font_unselected_color) | `Color(0.7, 0.7, 0.7, 1)` |
| [Color](class_color.md#class_Color) | [icon_disabled_color](class_tabbar.md#class_TabBar_theme_color_icon_disabled_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_hovered_color](class_tabbar.md#class_TabBar_theme_color_icon_hovered_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_selected_color](class_tabbar.md#class_TabBar_theme_color_icon_selected_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_unselected_color](class_tabbar.md#class_TabBar_theme_color_icon_unselected_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [h_separation](class_tabbar.md#class_TabBar_theme_constant_h_separation) | `4` |
| [int](class_int.md#class_int) | [hover_switch_wait_msec](class_tabbar.md#class_TabBar_theme_constant_hover_switch_wait_msec) | `500` |
| [int](class_int.md#class_int) | [icon_max_width](class_tabbar.md#class_TabBar_theme_constant_icon_max_width) | `0` |
| [int](class_int.md#class_int) | [outline_size](class_tabbar.md#class_TabBar_theme_constant_outline_size) | `0` |
| [int](class_int.md#class_int) | [tab_separation](class_tabbar.md#class_TabBar_theme_constant_tab_separation) | `0` |
| [Font](class_font.md#class_Font) | [font](class_tabbar.md#class_TabBar_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_tabbar.md#class_TabBar_theme_font_size_font_size) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [close](class_tabbar.md#class_TabBar_theme_icon_close) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [decrement](class_tabbar.md#class_TabBar_theme_icon_decrement) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [decrement_highlight](class_tabbar.md#class_TabBar_theme_icon_decrement_highlight) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [drop_mark](class_tabbar.md#class_TabBar_theme_icon_drop_mark) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [increment](class_tabbar.md#class_TabBar_theme_icon_increment) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [increment_highlight](class_tabbar.md#class_TabBar_theme_icon_increment_highlight) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [button_highlight](class_tabbar.md#class_TabBar_theme_style_button_highlight) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [button_pressed](class_tabbar.md#class_TabBar_theme_style_button_pressed) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_disabled](class_tabbar.md#class_TabBar_theme_style_tab_disabled) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_focus](class_tabbar.md#class_TabBar_theme_style_tab_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_hovered](class_tabbar.md#class_TabBar_theme_style_tab_hovered) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_selected](class_tabbar.md#class_TabBar_theme_style_tab_selected) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_unselected](class_tabbar.md#class_TabBar_theme_style_tab_unselected) |

---

### Signals

<span id="class_TabBar_signal_active_tab_rearranged"></span>

**active_tab_rearranged** ( idx_to: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_signal_active_tab_rearranged)

Emitted when the active tab is rearranged via mouse drag. See [drag_to_rearrange_enabled](class_tabbar.md#class_TabBar_property_drag_to_rearrange_enabled).

---

<span id="class_TabBar_signal_tab_button_pressed"></span>

**tab_button_pressed** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_signal_tab_button_pressed)

Emitted when a tab's right button is pressed. See [set_tab_button_icon()](class_tabbar.md#class_TabBar_method_set_tab_button_icon).

---

<span id="class_TabBar_signal_tab_changed"></span>

**tab_changed** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_signal_tab_changed)

Emitted when switching to another tab.

---

<span id="class_TabBar_signal_tab_clicked"></span>

**tab_clicked** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_signal_tab_clicked)

Emitted when a tab is clicked, even if it is the current tab.

---

<span id="class_TabBar_signal_tab_close_pressed"></span>

**tab_close_pressed** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_signal_tab_close_pressed)

Emitted when a tab's close button is pressed or, if [close_with_middle_mouse](class_tabbar.md#class_TabBar_property_close_with_middle_mouse) is `true`, when middle-clicking on a tab.

 **Note:** Tabs are not removed automatically; this behavior needs to be coded manually. For example:

.. tabs::

```
```

    $TabBar.tab_close_pressed.connect($TabBar.remove_tab)

```
```

    GetNode<TabBar>("TabBar").TabClosePressed += GetNode<TabBar>("TabBar").RemoveTab;

---

<span id="class_TabBar_signal_tab_hovered"></span>

**tab_hovered** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_signal_tab_hovered)

Emitted when a tab is hovered by the mouse.

---

<span id="class_TabBar_signal_tab_rmb_clicked"></span>

**tab_rmb_clicked** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_signal_tab_rmb_clicked)

Emitted when a tab is right-clicked.

---

<span id="class_TabBar_signal_tab_selected"></span>

**tab_selected** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_signal_tab_selected)

Emitted when a tab is selected via click, directional input, or script, even if it is the current tab.

---

### Enumerations

<span id="enum_TabBar_AlignmentMode"></span>

enum **AlignmentMode**: [🔗](class_tabbar.md#enum_TabBar_AlignmentMode)

<span id="class_TabBar_constant_ALIGNMENT_LEFT"></span>

[AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) **ALIGNMENT_LEFT** = `0`

Aligns tabs to the left.

<span id="class_TabBar_constant_ALIGNMENT_CENTER"></span>

[AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) **ALIGNMENT_CENTER** = `1`

Aligns tabs in the middle.

<span id="class_TabBar_constant_ALIGNMENT_RIGHT"></span>

[AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) **ALIGNMENT_RIGHT** = `2`

Aligns tabs to the right.

<span id="class_TabBar_constant_ALIGNMENT_MAX"></span>

[AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) **ALIGNMENT_MAX** = `3`

Represents the size of the [AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) enum.

---

<span id="enum_TabBar_CloseButtonDisplayPolicy"></span>

enum **CloseButtonDisplayPolicy**: [🔗](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy)

<span id="class_TabBar_constant_CLOSE_BUTTON_SHOW_NEVER"></span>

[CloseButtonDisplayPolicy](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy) **CLOSE_BUTTON_SHOW_NEVER** = `0`

Never show the close buttons.

<span id="class_TabBar_constant_CLOSE_BUTTON_SHOW_ACTIVE_ONLY"></span>

[CloseButtonDisplayPolicy](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy) **CLOSE_BUTTON_SHOW_ACTIVE_ONLY** = `1`

Only show the close button on the currently active tab.

<span id="class_TabBar_constant_CLOSE_BUTTON_SHOW_ALWAYS"></span>

[CloseButtonDisplayPolicy](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy) **CLOSE_BUTTON_SHOW_ALWAYS** = `2`

Show the close button on all tabs.

<span id="class_TabBar_constant_CLOSE_BUTTON_MAX"></span>

[CloseButtonDisplayPolicy](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy) **CLOSE_BUTTON_MAX** = `3`

Represents the size of the [CloseButtonDisplayPolicy](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy) enum.

---

### Property Descriptions

<span id="class_TabBar_property_clip_tabs"></span>

[bool](class_bool.md#class_bool) **clip_tabs** = `true` [🔗](class_tabbar.md#class_TabBar_property_clip_tabs)

- void **set_clip_tabs** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_clip_tabs** ( )

If `true`, tabs overflowing this node's width will be hidden, displaying two navigation buttons instead. Otherwise, this node's minimum size is updated so that all tabs are visible.

---

<span id="class_TabBar_property_close_with_middle_mouse"></span>

[bool](class_bool.md#class_bool) **close_with_middle_mouse** = `true` [🔗](class_tabbar.md#class_TabBar_property_close_with_middle_mouse)

- void **set_close_with_middle_mouse** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_close_with_middle_mouse** ( )

If `true`, middle-clicking on a tab will emit the [tab_close_pressed](class_tabbar.md#class_TabBar_signal_tab_close_pressed) signal.

---

<span id="class_TabBar_property_current_tab"></span>

[int](class_int.md#class_int) **current_tab** = `-1` [🔗](class_tabbar.md#class_TabBar_property_current_tab)

- void **set_current_tab** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_current_tab** ( )

The index of the current selected tab. A value of `-1` means that no tab is selected and can only be set when [deselect_enabled](class_tabbar.md#class_TabBar_property_deselect_enabled) is `true` or if all tabs are hidden or disabled.

---

<span id="class_TabBar_property_deselect_enabled"></span>

[bool](class_bool.md#class_bool) **deselect_enabled** = `false` [🔗](class_tabbar.md#class_TabBar_property_deselect_enabled)

- void **set_deselect_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_deselect_enabled** ( )

If `true`, all tabs can be deselected so that no tab is selected. Click on the current tab to deselect it.

---

<span id="class_TabBar_property_drag_to_rearrange_enabled"></span>

[bool](class_bool.md#class_bool) **drag_to_rearrange_enabled** = `false` [🔗](class_tabbar.md#class_TabBar_property_drag_to_rearrange_enabled)

- void **set_drag_to_rearrange_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_drag_to_rearrange_enabled** ( )

If `true`, tabs can be rearranged with mouse drag.

---

<span id="class_TabBar_property_max_tab_width"></span>

[int](class_int.md#class_int) **max_tab_width** = `0` [🔗](class_tabbar.md#class_TabBar_property_max_tab_width)

- void **set_max_tab_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_tab_width** ( )

Sets the maximum width which all tabs should be limited to. Unlimited if set to `0`.

---

<span id="class_TabBar_property_scroll_to_selected"></span>

[bool](class_bool.md#class_bool) **scroll_to_selected** = `true` [🔗](class_tabbar.md#class_TabBar_property_scroll_to_selected)

- void **set_scroll_to_selected** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_scroll_to_selected** ( )

If `true`, the tab offset will be changed to keep the currently selected tab visible.

---

<span id="class_TabBar_property_scrolling_enabled"></span>

[bool](class_bool.md#class_bool) **scrolling_enabled** = `true` [🔗](class_tabbar.md#class_TabBar_property_scrolling_enabled)

- void **set_scrolling_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_scrolling_enabled** ( )

if `true`, the mouse's scroll wheel can be used to navigate the scroll view.

---

<span id="class_TabBar_property_select_with_rmb"></span>

[bool](class_bool.md#class_bool) **select_with_rmb** = `false` [🔗](class_tabbar.md#class_TabBar_property_select_with_rmb)

- void **set_select_with_rmb** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_select_with_rmb** ( )

If `true`, enables selecting a tab with the right mouse button.

---

<span id="class_TabBar_property_switch_on_drag_hover"></span>

[bool](class_bool.md#class_bool) **switch_on_drag_hover** = `true` [🔗](class_tabbar.md#class_TabBar_property_switch_on_drag_hover)

- void **set_switch_on_drag_hover** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_switch_on_drag_hover** ( )

If `true`, hovering over a tab while dragging something will switch to that tab. Does not have effect when hovering another tab to rearrange. The delay for when this happens is dictated by [hover_switch_wait_msec](class_tabbar.md#class_TabBar_theme_constant_hover_switch_wait_msec).

---

<span id="class_TabBar_property_tab_alignment"></span>

[AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) **tab_alignment** = `0` [🔗](class_tabbar.md#class_TabBar_property_tab_alignment)

- void **set_tab_alignment** ( value: [AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) )
- [AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) **get_tab_alignment** ( )

The horizontal alignment of the tabs.

---

<span id="class_TabBar_property_tab_close_display_policy"></span>

[CloseButtonDisplayPolicy](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy) **tab_close_display_policy** = `0` [🔗](class_tabbar.md#class_TabBar_property_tab_close_display_policy)

- void **set_tab_close_display_policy** ( value: [CloseButtonDisplayPolicy](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy) )
- [CloseButtonDisplayPolicy](class_tabbar.md#enum_TabBar_CloseButtonDisplayPolicy) **get_tab_close_display_policy** ( )

When the close button will appear on the tabs.

---

<span id="class_TabBar_property_tab_count"></span>

[int](class_int.md#class_int) **tab_count** = `0` [🔗](class_tabbar.md#class_TabBar_property_tab_count)

- void **set_tab_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_tab_count** ( )

The number of tabs currently in the bar.

---

<span id="class_TabBar_property_tabs_rearrange_group"></span>

[int](class_int.md#class_int) **tabs_rearrange_group** = `-1` [🔗](class_tabbar.md#class_TabBar_property_tabs_rearrange_group)

- void **set_tabs_rearrange_group** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_tabs_rearrange_group** ( )

**TabBar** s with the same rearrange group ID will allow dragging the tabs between them. Enable drag with [drag_to_rearrange_enabled](class_tabbar.md#class_TabBar_property_drag_to_rearrange_enabled).

Setting this to `-1` will disable rearranging between **TabBar** s.

---

### Method Descriptions

<span id="class_TabBar_method_add_tab"></span>

void **add_tab** ( title: [String](class_string.md#class_String) = "", icon: [Texture2D](class_texture2d.md#class_Texture2D) = null ) [🔗](class_tabbar.md#class_TabBar_method_add_tab)

Adds a new tab.

---

<span id="class_TabBar_method_clear_tabs"></span>

void **clear_tabs** ( ) [🔗](class_tabbar.md#class_TabBar_method_clear_tabs)

Clears all tabs.

---

<span id="class_TabBar_method_ensure_tab_visible"></span>

void **ensure_tab_visible** ( idx: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_method_ensure_tab_visible)

Moves the scroll view to make the tab visible.

---

<span id="class_TabBar_method_get_offset_buttons_visible"></span>

[bool](class_bool.md#class_bool) **get_offset_buttons_visible** ( ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_offset_buttons_visible)

Returns `true` if the offset buttons (the ones that appear when there's not enough space for all tabs) are visible.

---

<span id="class_TabBar_method_get_previous_tab"></span>

[int](class_int.md#class_int) **get_previous_tab** ( ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_previous_tab)

Returns the previously active tab index.

---

<span id="class_TabBar_method_get_tab_button_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_tab_button_icon** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_button_icon)

Returns the icon for the right button of the tab at index `tab_idx` or `null` if the right button has no icon.

---

<span id="class_TabBar_method_get_tab_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_tab_icon** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_icon)

Returns the icon for the tab at index `tab_idx` or `null` if the tab has no icon.

---

<span id="class_TabBar_method_get_tab_icon_max_width"></span>

[int](class_int.md#class_int) **get_tab_icon_max_width** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_icon_max_width)

Returns the maximum allowed width of the icon for the tab at index `tab_idx`.

---

<span id="class_TabBar_method_get_tab_idx_at_point"></span>

[int](class_int.md#class_int) **get_tab_idx_at_point** ( point: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_idx_at_point)

Returns the index of the tab at local coordinates `point`. Returns `-1` if the point is outside the control boundaries or if there's no tab at the queried position.

---

<span id="class_TabBar_method_get_tab_language"></span>

[String](class_string.md#class_String) **get_tab_language** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_language)

Returns tab title language code.

---

<span id="class_TabBar_method_get_tab_metadata"></span>

[Variant](class_variant.md#class_Variant) **get_tab_metadata** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_metadata)

Returns the metadata value set to the tab at index `tab_idx` using [set_tab_metadata()](class_tabbar.md#class_TabBar_method_set_tab_metadata). If no metadata was previously set, returns `null` by default.

---

<span id="class_TabBar_method_get_tab_offset"></span>

[int](class_int.md#class_int) **get_tab_offset** ( ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_offset)

Returns the number of hidden tabs offsetted to the left.

---

<span id="class_TabBar_method_get_tab_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **get_tab_rect** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_rect)

Returns tab [Rect2](class_rect2.md#class_Rect2) with local position and size.

---

<span id="class_TabBar_method_get_tab_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **get_tab_text_direction** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_text_direction)

Returns tab title text base writing direction.

---

<span id="class_TabBar_method_get_tab_title"></span>

[String](class_string.md#class_String) **get_tab_title** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_title)

Returns the title of the tab at index `tab_idx`.

---

<span id="class_TabBar_method_get_tab_tooltip"></span>

[String](class_string.md#class_String) **get_tab_tooltip** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_get_tab_tooltip)

Returns the tooltip text of the tab at index `tab_idx`.

---

<span id="class_TabBar_method_is_tab_disabled"></span>

[bool](class_bool.md#class_bool) **is_tab_disabled** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_is_tab_disabled)

Returns `true` if the tab at index `tab_idx` is disabled.

---

<span id="class_TabBar_method_is_tab_hidden"></span>

[bool](class_bool.md#class_bool) **is_tab_hidden** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabbar.md#class_TabBar_method_is_tab_hidden)

Returns `true` if the tab at index `tab_idx` is hidden.

---

<span id="class_TabBar_method_move_tab"></span>

void **move_tab** ( from: [int](class_int.md#class_int), to: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_method_move_tab)

Moves a tab from `from` to `to`.

---

<span id="class_TabBar_method_remove_tab"></span>

void **remove_tab** ( tab_idx: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_method_remove_tab)

Removes the tab at index `tab_idx`.

---

<span id="class_TabBar_method_select_next_available"></span>

[bool](class_bool.md#class_bool) **select_next_available** ( ) [🔗](class_tabbar.md#class_TabBar_method_select_next_available)

Selects the first available tab with greater index than the currently selected. Returns `true` if tab selection changed.

---

<span id="class_TabBar_method_select_previous_available"></span>

[bool](class_bool.md#class_bool) **select_previous_available** ( ) [🔗](class_tabbar.md#class_TabBar_method_select_previous_available)

Selects the first available tab with lower index than the currently selected. Returns `true` if tab selection changed.

---

<span id="class_TabBar_method_set_tab_button_icon"></span>

void **set_tab_button_icon** ( tab_idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_button_icon)

Sets an `icon` for the button of the tab at index `tab_idx` (located to the right, before the close button), making it visible and clickable (See [tab_button_pressed](class_tabbar.md#class_TabBar_signal_tab_button_pressed)). Giving it a `null` value will hide the button.

---

<span id="class_TabBar_method_set_tab_disabled"></span>

void **set_tab_disabled** ( tab_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_disabled)

If `disabled` is `true`, disables the tab at index `tab_idx`, making it non-interactable.

---

<span id="class_TabBar_method_set_tab_hidden"></span>

void **set_tab_hidden** ( tab_idx: [int](class_int.md#class_int), hidden: [bool](class_bool.md#class_bool) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_hidden)

If `hidden` is `true`, hides the tab at index `tab_idx`, making it disappear from the tab area.

---

<span id="class_TabBar_method_set_tab_icon"></span>

void **set_tab_icon** ( tab_idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_icon)

Sets an `icon` for the tab at index `tab_idx`.

---

<span id="class_TabBar_method_set_tab_icon_max_width"></span>

void **set_tab_icon_max_width** ( tab_idx: [int](class_int.md#class_int), width: [int](class_int.md#class_int) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_icon_max_width)

Sets the maximum allowed width of the icon for the tab at index `tab_idx`. This limit is applied on top of the default size of the icon and on top of [icon_max_width](class_tabbar.md#class_TabBar_theme_constant_icon_max_width). The height is adjusted according to the icon's ratio.

---

<span id="class_TabBar_method_set_tab_language"></span>

void **set_tab_language** ( tab_idx: [int](class_int.md#class_int), language: [String](class_string.md#class_String) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_language)

Sets the language code of the title for the tab at index `tab_idx` to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---

<span id="class_TabBar_method_set_tab_metadata"></span>

void **set_tab_metadata** ( tab_idx: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_metadata)

Sets the metadata value for the tab at index `tab_idx`, which can be retrieved later using [get_tab_metadata()](class_tabbar.md#class_TabBar_method_get_tab_metadata).

---

<span id="class_TabBar_method_set_tab_text_direction"></span>

void **set_tab_text_direction** ( tab_idx: [int](class_int.md#class_int), direction: [TextDirection](class_control.md#enum_Control_TextDirection) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_text_direction)

Sets tab title base writing direction.

---

<span id="class_TabBar_method_set_tab_title"></span>

void **set_tab_title** ( tab_idx: [int](class_int.md#class_int), title: [String](class_string.md#class_String) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_title)

Sets a `title` for the tab at index `tab_idx`.

---

<span id="class_TabBar_method_set_tab_tooltip"></span>

void **set_tab_tooltip** ( tab_idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) [🔗](class_tabbar.md#class_TabBar_method_set_tab_tooltip)

Sets a `tooltip` for tab at index `tab_idx`.

 **Note:** By default, if the `tooltip` is empty and the tab text is truncated (not all characters fit into the tab), the title will be displayed as a tooltip. To hide the tooltip, assign `" "` as the `tooltip` text.

---

### Theme Property Descriptions

<span id="class_TabBar_theme_color_drop_mark_color"></span>

[Color](class_color.md#class_Color) **drop_mark_color** = `Color(1, 1, 1, 1)` [🔗](class_tabbar.md#class_TabBar_theme_color_drop_mark_color)

Modulation color for the [drop_mark](class_tabbar.md#class_TabBar_theme_icon_drop_mark) icon.

---

<span id="class_TabBar_theme_color_font_disabled_color"></span>

[Color](class_color.md#class_Color) **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗](class_tabbar.md#class_TabBar_theme_color_font_disabled_color)

Font color of disabled tabs.

---

<span id="class_TabBar_theme_color_font_hovered_color"></span>

[Color](class_color.md#class_Color) **font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_tabbar.md#class_TabBar_theme_color_font_hovered_color)

Font color of the currently hovered tab. Does not apply to the selected tab.

---

<span id="class_TabBar_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_tabbar.md#class_TabBar_theme_color_font_outline_color)

The tint of text outline of the tab name.

---

<span id="class_TabBar_theme_color_font_selected_color"></span>

[Color](class_color.md#class_Color) **font_selected_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_tabbar.md#class_TabBar_theme_color_font_selected_color)

Font color of the currently selected tab.

---

<span id="class_TabBar_theme_color_font_unselected_color"></span>

[Color](class_color.md#class_Color) **font_unselected_color** = `Color(0.7, 0.7, 0.7, 1)` [🔗](class_tabbar.md#class_TabBar_theme_color_font_unselected_color)

Font color of the other, unselected tabs.

---

<span id="class_TabBar_theme_color_icon_disabled_color"></span>

[Color](class_color.md#class_Color) **icon_disabled_color** = `Color(1, 1, 1, 1)` [🔗](class_tabbar.md#class_TabBar_theme_color_icon_disabled_color)

Icon color of disabled tabs.

---

<span id="class_TabBar_theme_color_icon_hovered_color"></span>

[Color](class_color.md#class_Color) **icon_hovered_color** = `Color(1, 1, 1, 1)` [🔗](class_tabbar.md#class_TabBar_theme_color_icon_hovered_color)

Icon color of the currently hovered tab. Does not apply to the selected tab.

---

<span id="class_TabBar_theme_color_icon_selected_color"></span>

[Color](class_color.md#class_Color) **icon_selected_color** = `Color(1, 1, 1, 1)` [🔗](class_tabbar.md#class_TabBar_theme_color_icon_selected_color)

Icon color of the currently selected tab.

---

<span id="class_TabBar_theme_color_icon_unselected_color"></span>

[Color](class_color.md#class_Color) **icon_unselected_color** = `Color(1, 1, 1, 1)` [🔗](class_tabbar.md#class_TabBar_theme_color_icon_unselected_color)

Icon color of the other, unselected tabs.

---

<span id="class_TabBar_theme_constant_h_separation"></span>

[int](class_int.md#class_int) **h_separation** = `4` [🔗](class_tabbar.md#class_TabBar_theme_constant_h_separation)

The horizontal separation between the elements inside tabs.

---

<span id="class_TabBar_theme_constant_hover_switch_wait_msec"></span>

[int](class_int.md#class_int) **hover_switch_wait_msec** = `500` [🔗](class_tabbar.md#class_TabBar_theme_constant_hover_switch_wait_msec)

During a drag-and-drop, this is how many milliseconds to wait before switching the tab.

---

<span id="class_TabBar_theme_constant_icon_max_width"></span>

[int](class_int.md#class_int) **icon_max_width** = `0` [🔗](class_tabbar.md#class_TabBar_theme_constant_icon_max_width)

The maximum allowed width of the tab's icon. This limit is applied on top of the default size of the icon, but before the value set with [set_tab_icon_max_width()](class_tabbar.md#class_TabBar_method_set_tab_icon_max_width). The height is adjusted according to the icon's ratio.

---

<span id="class_TabBar_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_tabbar.md#class_TabBar_theme_constant_outline_size)

The size of the tab text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_tabbar.md#class_TabBar_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_TabBar_theme_constant_tab_separation"></span>

[int](class_int.md#class_int) **tab_separation** = `0` [🔗](class_tabbar.md#class_TabBar_theme_constant_tab_separation)

The space between tabs in the tab bar.

---

<span id="class_TabBar_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_tabbar.md#class_TabBar_theme_font_font)

The font used to draw tab names.

---

<span id="class_TabBar_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_tabbar.md#class_TabBar_theme_font_size_font_size)

Font size of the tab names.

---

<span id="class_TabBar_theme_icon_close"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **close** [🔗](class_tabbar.md#class_TabBar_theme_icon_close)

The icon for the close button (see [tab_close_display_policy](class_tabbar.md#class_TabBar_property_tab_close_display_policy)).

---

<span id="class_TabBar_theme_icon_decrement"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **decrement** [🔗](class_tabbar.md#class_TabBar_theme_icon_decrement)

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the first tab is visible), it appears semi-transparent.

---

<span id="class_TabBar_theme_icon_decrement_highlight"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **decrement_highlight** [🔗](class_tabbar.md#class_TabBar_theme_icon_decrement_highlight)

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

---

<span id="class_TabBar_theme_icon_drop_mark"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **drop_mark** [🔗](class_tabbar.md#class_TabBar_theme_icon_drop_mark)

Icon shown to indicate where a dragged tab is gonna be dropped (see [drag_to_rearrange_enabled](class_tabbar.md#class_TabBar_property_drag_to_rearrange_enabled)).

---

<span id="class_TabBar_theme_icon_increment"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **increment** [🔗](class_tabbar.md#class_TabBar_theme_icon_increment)

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the last tab is visible) it appears semi-transparent.

---

<span id="class_TabBar_theme_icon_increment_highlight"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **increment_highlight** [🔗](class_tabbar.md#class_TabBar_theme_icon_increment_highlight)

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

---

<span id="class_TabBar_theme_style_button_highlight"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **button_highlight** [🔗](class_tabbar.md#class_TabBar_theme_style_button_highlight)

Background of the tab and close buttons when they're being hovered with the cursor.

---

<span id="class_TabBar_theme_style_button_pressed"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **button_pressed** [🔗](class_tabbar.md#class_TabBar_theme_style_button_pressed)

Background of the tab and close buttons when it's being pressed.

---

<span id="class_TabBar_theme_style_tab_disabled"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_disabled** [🔗](class_tabbar.md#class_TabBar_theme_style_tab_disabled)

The style of disabled tabs.

---

<span id="class_TabBar_theme_style_tab_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_focus** [🔗](class_tabbar.md#class_TabBar_theme_style_tab_focus)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **TabBar** is focused. The [tab_focus](class_tabbar.md#class_TabBar_theme_style_tab_focus) [StyleBox](class_stylebox.md#class_StyleBox) is displayed *over* the base [StyleBox](class_stylebox.md#class_StyleBox) of the selected tab, so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the base [StyleBox](class_stylebox.md#class_StyleBox) remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_TabBar_theme_style_tab_hovered"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_hovered** [🔗](class_tabbar.md#class_TabBar_theme_style_tab_hovered)

The style of the currently hovered tab. Does not apply to the selected tab.

 **Note:** This style will be drawn with the same width as [tab_unselected](class_tabbar.md#class_TabBar_theme_style_tab_unselected) at minimum.

---

<span id="class_TabBar_theme_style_tab_selected"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_selected** [🔗](class_tabbar.md#class_TabBar_theme_style_tab_selected)

The style of the currently selected tab.

---

<span id="class_TabBar_theme_style_tab_unselected"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_unselected** [🔗](class_tabbar.md#class_TabBar_theme_style_tab_unselected)

The style of the other, unselected tabs.
