<span id="class_TabContainer"></span>

## TabContainer

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A container that creates a tab for each child control, displaying only the active tab's control.

### Description

Arranges child controls into a tabbed view, creating a tab for each one. The active tab's corresponding control is made visible, while all other child controls are hidden. Ignores non-control children.

 **Note:** The drawing of the clickable tabs is handled by this node; [TabBar](class_tabbar.md#class_TabBar) is not needed.

### Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

### Properties


| [bool](class_bool.md#class_bool) | [all_tabs_in_front](class_tabcontainer.md#class_TabContainer_property_all_tabs_in_front) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [clip_tabs](class_tabcontainer.md#class_TabContainer_property_clip_tabs) | `true` |
| [int](class_int.md#class_int) | [current_tab](class_tabcontainer.md#class_TabContainer_property_current_tab) | `-1` |
| [bool](class_bool.md#class_bool) | [deselect_enabled](class_tabcontainer.md#class_TabContainer_property_deselect_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [drag_to_rearrange_enabled](class_tabcontainer.md#class_TabContainer_property_drag_to_rearrange_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [switch_on_drag_hover](class_tabcontainer.md#class_TabContainer_property_switch_on_drag_hover) | `true` |
| [AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) | [tab_alignment](class_tabcontainer.md#class_TabContainer_property_tab_alignment) | `0` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | [tab_focus_mode](class_tabcontainer.md#class_TabContainer_property_tab_focus_mode) | `2` |
| [TabPosition](class_tabcontainer.md#enum_TabContainer_TabPosition) | [tabs_position](class_tabcontainer.md#class_TabContainer_property_tabs_position) | `0` |
| [int](class_int.md#class_int) | [tabs_rearrange_group](class_tabcontainer.md#class_TabContainer_property_tabs_rearrange_group) | `-1` |
| [bool](class_bool.md#class_bool) | [tabs_visible](class_tabcontainer.md#class_TabContainer_property_tabs_visible) | `true` |
| [bool](class_bool.md#class_bool) | [use_hidden_tabs_for_min_size](class_tabcontainer.md#class_TabContainer_property_use_hidden_tabs_for_min_size) | `false` |

### Methods


| [Control](class_control.md#class_Control) | [get_current_tab_control](class_tabcontainer.md#class_TabContainer_method_get_current_tab_control) ( ) const |
| --- | --- |
| [Popup](class_popup.md#class_Popup) | [get_popup](class_tabcontainer.md#class_TabContainer_method_get_popup) ( ) const |
| [int](class_int.md#class_int) | [get_previous_tab](class_tabcontainer.md#class_TabContainer_method_get_previous_tab) ( ) const |
| [TabBar](class_tabbar.md#class_TabBar) | [get_tab_bar](class_tabcontainer.md#class_TabContainer_method_get_tab_bar) ( ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_tab_button_icon](class_tabcontainer.md#class_TabContainer_method_get_tab_button_icon) ( tab_idx: [int](class_int.md#class_int) ) const |
| [Control](class_control.md#class_Control) | [get_tab_control](class_tabcontainer.md#class_TabContainer_method_get_tab_control) ( tab_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_tab_count](class_tabcontainer.md#class_TabContainer_method_get_tab_count) ( ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_tab_icon](class_tabcontainer.md#class_TabContainer_method_get_tab_icon) ( tab_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_tab_icon_max_width](class_tabcontainer.md#class_TabContainer_method_get_tab_icon_max_width) ( tab_idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_tab_idx_at_point](class_tabcontainer.md#class_TabContainer_method_get_tab_idx_at_point) ( point: [Vector2](class_vector2.md#class_Vector2) ) const |
| [int](class_int.md#class_int) | [get_tab_idx_from_control](class_tabcontainer.md#class_TabContainer_method_get_tab_idx_from_control) ( control: [Control](class_control.md#class_Control) ) const |
| [Variant](class_variant.md#class_Variant) | [get_tab_metadata](class_tabcontainer.md#class_TabContainer_method_get_tab_metadata) ( tab_idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_tab_title](class_tabcontainer.md#class_TabContainer_method_get_tab_title) ( tab_idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_tab_tooltip](class_tabcontainer.md#class_TabContainer_method_get_tab_tooltip) ( tab_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_tab_disabled](class_tabcontainer.md#class_TabContainer_method_is_tab_disabled) ( tab_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_tab_hidden](class_tabcontainer.md#class_TabContainer_method_is_tab_hidden) ( tab_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [select_next_available](class_tabcontainer.md#class_TabContainer_method_select_next_available) ( ) |
| [bool](class_bool.md#class_bool) | [select_previous_available](class_tabcontainer.md#class_TabContainer_method_select_previous_available) ( ) |
| void | [set_popup](class_tabcontainer.md#class_TabContainer_method_set_popup) ( popup: [Node](class_node.md#class_Node) ) |
| void | [set_tab_button_icon](class_tabcontainer.md#class_TabContainer_method_set_tab_button_icon) ( tab_idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_tab_disabled](class_tabcontainer.md#class_TabContainer_method_set_tab_disabled) ( tab_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) |
| void | [set_tab_hidden](class_tabcontainer.md#class_TabContainer_method_set_tab_hidden) ( tab_idx: [int](class_int.md#class_int), hidden: [bool](class_bool.md#class_bool) ) |
| void | [set_tab_icon](class_tabcontainer.md#class_TabContainer_method_set_tab_icon) ( tab_idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_tab_icon_max_width](class_tabcontainer.md#class_TabContainer_method_set_tab_icon_max_width) ( tab_idx: [int](class_int.md#class_int), width: [int](class_int.md#class_int) ) |
| void | [set_tab_metadata](class_tabcontainer.md#class_TabContainer_method_set_tab_metadata) ( tab_idx: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) |
| void | [set_tab_title](class_tabcontainer.md#class_TabContainer_method_set_tab_title) ( tab_idx: [int](class_int.md#class_int), title: [String](class_string.md#class_String) ) |
| void | [set_tab_tooltip](class_tabcontainer.md#class_TabContainer_method_set_tab_tooltip) ( tab_idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [drop_mark_color](class_tabcontainer.md#class_TabContainer_theme_color_drop_mark_color) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_disabled_color](class_tabcontainer.md#class_TabContainer_theme_color_font_disabled_color) | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class_Color) | [font_hovered_color](class_tabcontainer.md#class_TabContainer_theme_color_font_hovered_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_outline_color](class_tabcontainer.md#class_TabContainer_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_selected_color](class_tabcontainer.md#class_TabContainer_theme_color_font_selected_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_unselected_color](class_tabcontainer.md#class_TabContainer_theme_color_font_unselected_color) | `Color(0.7, 0.7, 0.7, 1)` |
| [Color](class_color.md#class_Color) | [icon_disabled_color](class_tabcontainer.md#class_TabContainer_theme_color_icon_disabled_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_hovered_color](class_tabcontainer.md#class_TabContainer_theme_color_icon_hovered_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_selected_color](class_tabcontainer.md#class_TabContainer_theme_color_icon_selected_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [icon_unselected_color](class_tabcontainer.md#class_TabContainer_theme_color_icon_unselected_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [icon_max_width](class_tabcontainer.md#class_TabContainer_theme_constant_icon_max_width) | `0` |
| [int](class_int.md#class_int) | [icon_separation](class_tabcontainer.md#class_TabContainer_theme_constant_icon_separation) | `4` |
| [int](class_int.md#class_int) | [outline_size](class_tabcontainer.md#class_TabContainer_theme_constant_outline_size) | `0` |
| [int](class_int.md#class_int) | [side_margin](class_tabcontainer.md#class_TabContainer_theme_constant_side_margin) | `8` |
| [int](class_int.md#class_int) | [tab_separation](class_tabcontainer.md#class_TabContainer_theme_constant_tab_separation) | `0` |
| [Font](class_font.md#class_Font) | [font](class_tabcontainer.md#class_TabContainer_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_tabcontainer.md#class_TabContainer_theme_font_size_font_size) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [decrement](class_tabcontainer.md#class_TabContainer_theme_icon_decrement) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [decrement_highlight](class_tabcontainer.md#class_TabContainer_theme_icon_decrement_highlight) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [drop_mark](class_tabcontainer.md#class_TabContainer_theme_icon_drop_mark) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [increment](class_tabcontainer.md#class_TabContainer_theme_icon_increment) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [increment_highlight](class_tabcontainer.md#class_TabContainer_theme_icon_increment_highlight) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [menu](class_tabcontainer.md#class_TabContainer_theme_icon_menu) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [menu_highlight](class_tabcontainer.md#class_TabContainer_theme_icon_menu_highlight) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [panel](class_tabcontainer.md#class_TabContainer_theme_style_panel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_disabled](class_tabcontainer.md#class_TabContainer_theme_style_tab_disabled) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_focus](class_tabcontainer.md#class_TabContainer_theme_style_tab_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_hovered](class_tabcontainer.md#class_TabContainer_theme_style_tab_hovered) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_selected](class_tabcontainer.md#class_TabContainer_theme_style_tab_selected) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tab_unselected](class_tabcontainer.md#class_TabContainer_theme_style_tab_unselected) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [tabbar_background](class_tabcontainer.md#class_TabContainer_theme_style_tabbar_background) |

---

### Signals

<span id="class_TabContainer_signal_active_tab_rearranged"></span>

**active_tab_rearranged** ( idx_to: [int](class_int.md#class_int) ) [🔗](class_tabcontainer.md#class_TabContainer_signal_active_tab_rearranged)

Emitted when the active tab is rearranged via mouse drag. See [drag_to_rearrange_enabled](class_tabcontainer.md#class_TabContainer_property_drag_to_rearrange_enabled).

---

<span id="class_TabContainer_signal_pre_popup_pressed"></span>

**pre_popup_pressed** ( ) [🔗](class_tabcontainer.md#class_TabContainer_signal_pre_popup_pressed)

Emitted when the **TabContainer**'s [Popup](class_popup.md#class_Popup) button is clicked. See [set_popup()](class_tabcontainer.md#class_TabContainer_method_set_popup) for details.

---

<span id="class_TabContainer_signal_tab_button_pressed"></span>

**tab_button_pressed** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabcontainer.md#class_TabContainer_signal_tab_button_pressed)

Emitted when the user clicks on the button icon on this tab.

---

<span id="class_TabContainer_signal_tab_changed"></span>

**tab_changed** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabcontainer.md#class_TabContainer_signal_tab_changed)

Emitted when switching to another tab.

---

<span id="class_TabContainer_signal_tab_clicked"></span>

**tab_clicked** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabcontainer.md#class_TabContainer_signal_tab_clicked)

Emitted when a tab is clicked, even if it is the current tab.

---

<span id="class_TabContainer_signal_tab_hovered"></span>

**tab_hovered** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabcontainer.md#class_TabContainer_signal_tab_hovered)

Emitted when a tab is hovered by the mouse.

---

<span id="class_TabContainer_signal_tab_selected"></span>

**tab_selected** ( tab: [int](class_int.md#class_int) ) [🔗](class_tabcontainer.md#class_TabContainer_signal_tab_selected)

Emitted when a tab is selected via click, directional input, or script, even if it is the current tab.

---

### Enumerations

<span id="enum_TabContainer_TabPosition"></span>

enum **TabPosition**: [🔗](class_tabcontainer.md#enum_TabContainer_TabPosition)

<span id="class_TabContainer_constant_POSITION_TOP"></span>

[TabPosition](class_tabcontainer.md#enum_TabContainer_TabPosition) **POSITION_TOP** = `0`

Places the tab bar at the top.

<span id="class_TabContainer_constant_POSITION_BOTTOM"></span>

[TabPosition](class_tabcontainer.md#enum_TabContainer_TabPosition) **POSITION_BOTTOM** = `1`

Places the tab bar at the bottom. The tab bar's [StyleBox](class_stylebox.md#class_StyleBox) will be flipped vertically.

<span id="class_TabContainer_constant_POSITION_MAX"></span>

[TabPosition](class_tabcontainer.md#enum_TabContainer_TabPosition) **POSITION_MAX** = `2`

Represents the size of the [TabPosition](class_tabcontainer.md#enum_TabContainer_TabPosition) enum.

---

### Property Descriptions

<span id="class_TabContainer_property_all_tabs_in_front"></span>

[bool](class_bool.md#class_bool) **all_tabs_in_front** = `false` [🔗](class_tabcontainer.md#class_TabContainer_property_all_tabs_in_front)

- void **set_all_tabs_in_front** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_all_tabs_in_front** ( )

If `true`, all tabs are drawn in front of the panel. If `false`, inactive tabs are drawn behind the panel.

---

<span id="class_TabContainer_property_clip_tabs"></span>

[bool](class_bool.md#class_bool) **clip_tabs** = `true` [🔗](class_tabcontainer.md#class_TabContainer_property_clip_tabs)

- void **set_clip_tabs** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_clip_tabs** ( )

If `true`, tabs overflowing this node's width will be hidden, displaying two navigation buttons instead. Otherwise, this node's minimum size is updated so that all tabs are visible.

---

<span id="class_TabContainer_property_current_tab"></span>

[int](class_int.md#class_int) **current_tab** = `-1` [🔗](class_tabcontainer.md#class_TabContainer_property_current_tab)

- void **set_current_tab** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_current_tab** ( )

The current tab index. When set, this index's [Control](class_control.md#class_Control) node's `visible` property is set to `true` and all others are set to `false`.

A value of `-1` means that no tab is selected.

---

<span id="class_TabContainer_property_deselect_enabled"></span>

[bool](class_bool.md#class_bool) **deselect_enabled** = `false` [🔗](class_tabcontainer.md#class_TabContainer_property_deselect_enabled)

- void **set_deselect_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_deselect_enabled** ( )

If `true`, all tabs can be deselected so that no tab is selected. Click on the [current_tab](class_tabcontainer.md#class_TabContainer_property_current_tab) to deselect it.

Only the tab header will be shown if no tabs are selected.

---

<span id="class_TabContainer_property_drag_to_rearrange_enabled"></span>

[bool](class_bool.md#class_bool) **drag_to_rearrange_enabled** = `false` [🔗](class_tabcontainer.md#class_TabContainer_property_drag_to_rearrange_enabled)

- void **set_drag_to_rearrange_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_drag_to_rearrange_enabled** ( )

If `true`, tabs can be rearranged with mouse drag.

---

<span id="class_TabContainer_property_switch_on_drag_hover"></span>

[bool](class_bool.md#class_bool) **switch_on_drag_hover** = `true` [🔗](class_tabcontainer.md#class_TabContainer_property_switch_on_drag_hover)

- void **set_switch_on_drag_hover** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_switch_on_drag_hover** ( )

If `true`, hovering over a tab while dragging something will switch to that tab. Does not have effect when hovering another tab to rearrange.

---

<span id="class_TabContainer_property_tab_alignment"></span>

[AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) **tab_alignment** = `0` [🔗](class_tabcontainer.md#class_TabContainer_property_tab_alignment)

- void **set_tab_alignment** ( value: [AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) )
- [AlignmentMode](class_tabbar.md#enum_TabBar_AlignmentMode) **get_tab_alignment** ( )

The position at which tabs will be placed.

---

<span id="class_TabContainer_property_tab_focus_mode"></span>

[FocusMode](class_control.md#enum_Control_FocusMode) **tab_focus_mode** = `2` [🔗](class_tabcontainer.md#class_TabContainer_property_tab_focus_mode)

- void **set_tab_focus_mode** ( value: [FocusMode](class_control.md#enum_Control_FocusMode) )
- [FocusMode](class_control.md#enum_Control_FocusMode) **get_tab_focus_mode** ( )

The focus access mode for the internal [TabBar](class_tabbar.md#class_TabBar) node.

---

<span id="class_TabContainer_property_tabs_position"></span>

[TabPosition](class_tabcontainer.md#enum_TabContainer_TabPosition) **tabs_position** = `0` [🔗](class_tabcontainer.md#class_TabContainer_property_tabs_position)

- void **set_tabs_position** ( value: [TabPosition](class_tabcontainer.md#enum_TabContainer_TabPosition) )
- [TabPosition](class_tabcontainer.md#enum_TabContainer_TabPosition) **get_tabs_position** ( )

The horizontal alignment of the tabs.

---

<span id="class_TabContainer_property_tabs_rearrange_group"></span>

[int](class_int.md#class_int) **tabs_rearrange_group** = `-1` [🔗](class_tabcontainer.md#class_TabContainer_property_tabs_rearrange_group)

- void **set_tabs_rearrange_group** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_tabs_rearrange_group** ( )

**TabContainer** s with the same rearrange group ID will allow dragging the tabs between them. Enable drag with [drag_to_rearrange_enabled](class_tabcontainer.md#class_TabContainer_property_drag_to_rearrange_enabled).

Setting this to `-1` will disable rearranging between **TabContainer** s.

---

<span id="class_TabContainer_property_tabs_visible"></span>

[bool](class_bool.md#class_bool) **tabs_visible** = `true` [🔗](class_tabcontainer.md#class_TabContainer_property_tabs_visible)

- void **set_tabs_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **are_tabs_visible** ( )

If `true`, tabs are visible. If `false`, tabs' content and titles are hidden.

---

<span id="class_TabContainer_property_use_hidden_tabs_for_min_size"></span>

[bool](class_bool.md#class_bool) **use_hidden_tabs_for_min_size** = `false` [🔗](class_tabcontainer.md#class_TabContainer_property_use_hidden_tabs_for_min_size)

- void **set_use_hidden_tabs_for_min_size** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_hidden_tabs_for_min_size** ( )

If `true`, child [Control](class_control.md#class_Control) nodes that are hidden have their minimum size take into account in the total, instead of only the currently visible one.

---

### Method Descriptions

<span id="class_TabContainer_method_get_current_tab_control"></span>

[Control](class_control.md#class_Control) **get_current_tab_control** ( ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_current_tab_control)

Returns the child [Control](class_control.md#class_Control) node located at the active tab index.

---

<span id="class_TabContainer_method_get_popup"></span>

[Popup](class_popup.md#class_Popup) **get_popup** ( ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_popup)

Returns the [Popup](class_popup.md#class_Popup) node instance if one has been set already with [set_popup()](class_tabcontainer.md#class_TabContainer_method_set_popup).

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class_Window_property_visible) property.

---

<span id="class_TabContainer_method_get_previous_tab"></span>

[int](class_int.md#class_int) **get_previous_tab** ( ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_previous_tab)

Returns the previously active tab index.

---

<span id="class_TabContainer_method_get_tab_bar"></span>

[TabBar](class_tabbar.md#class_TabBar) **get_tab_bar** ( ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_bar)

Returns the [TabBar](class_tabbar.md#class_TabBar) contained in this container.

 **Warning:** This is a required internal node, removing and freeing it or editing its tabs may cause a crash. If you wish to edit the tabs, use the methods provided in **TabContainer**.

---

<span id="class_TabContainer_method_get_tab_button_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_tab_button_icon** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_button_icon)

Returns the button icon from the tab at index `tab_idx`.

---

<span id="class_TabContainer_method_get_tab_control"></span>

[Control](class_control.md#class_Control) **get_tab_control** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_control)

Returns the [Control](class_control.md#class_Control) node from the tab at index `tab_idx`.

---

<span id="class_TabContainer_method_get_tab_count"></span>

[int](class_int.md#class_int) **get_tab_count** ( ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_count)

Returns the number of tabs.

---

<span id="class_TabContainer_method_get_tab_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_tab_icon** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_icon)

Returns the [Texture2D](class_texture2d.md#class_Texture2D) for the tab at index `tab_idx` or `null` if the tab has no [Texture2D](class_texture2d.md#class_Texture2D).

---

<span id="class_TabContainer_method_get_tab_icon_max_width"></span>

[int](class_int.md#class_int) **get_tab_icon_max_width** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_icon_max_width)

Returns the maximum allowed width of the icon for the tab at index `tab_idx`.

---

<span id="class_TabContainer_method_get_tab_idx_at_point"></span>

[int](class_int.md#class_int) **get_tab_idx_at_point** ( point: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_idx_at_point)

Returns the index of the tab at local coordinates `point`. Returns `-1` if the point is outside the control boundaries or if there's no tab at the queried position.

---

<span id="class_TabContainer_method_get_tab_idx_from_control"></span>

[int](class_int.md#class_int) **get_tab_idx_from_control** ( control: [Control](class_control.md#class_Control) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_idx_from_control)

Returns the index of the tab tied to the given `control`. The control must be a child of the **TabContainer**.

---

<span id="class_TabContainer_method_get_tab_metadata"></span>

[Variant](class_variant.md#class_Variant) **get_tab_metadata** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_metadata)

Returns the metadata value set to the tab at index `tab_idx` using [set_tab_metadata()](class_tabcontainer.md#class_TabContainer_method_set_tab_metadata). If no metadata was previously set, returns `null` by default.

---

<span id="class_TabContainer_method_get_tab_title"></span>

[String](class_string.md#class_String) **get_tab_title** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_title)

Returns the title of the tab at index `tab_idx`. Tab titles default to the name of the indexed child node, but this can be overridden with [set_tab_title()](class_tabcontainer.md#class_TabContainer_method_set_tab_title).

---

<span id="class_TabContainer_method_get_tab_tooltip"></span>

[String](class_string.md#class_String) **get_tab_tooltip** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_get_tab_tooltip)

Returns the tooltip text of the tab at index `tab_idx`.

---

<span id="class_TabContainer_method_is_tab_disabled"></span>

[bool](class_bool.md#class_bool) **is_tab_disabled** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_is_tab_disabled)

Returns `true` if the tab at index `tab_idx` is disabled.

---

<span id="class_TabContainer_method_is_tab_hidden"></span>

[bool](class_bool.md#class_bool) **is_tab_hidden** ( tab_idx: [int](class_int.md#class_int) ) *const* [🔗](class_tabcontainer.md#class_TabContainer_method_is_tab_hidden)

Returns `true` if the tab at index `tab_idx` is hidden.

---

<span id="class_TabContainer_method_select_next_available"></span>

[bool](class_bool.md#class_bool) **select_next_available** ( ) [🔗](class_tabcontainer.md#class_TabContainer_method_select_next_available)

Selects the first available tab with greater index than the currently selected. Returns `true` if tab selection changed.

---

<span id="class_TabContainer_method_select_previous_available"></span>

[bool](class_bool.md#class_bool) **select_previous_available** ( ) [🔗](class_tabcontainer.md#class_TabContainer_method_select_previous_available)

Selects the first available tab with lower index than the currently selected. Returns `true` if tab selection changed.

---

<span id="class_TabContainer_method_set_popup"></span>

void **set_popup** ( popup: [Node](class_node.md#class_Node) ) [🔗](class_tabcontainer.md#class_TabContainer_method_set_popup)

If set on a [Popup](class_popup.md#class_Popup) node instance, a popup menu icon appears in the top-right corner of the **TabContainer** (setting it to `null` will make it go away). Clicking it will expand the [Popup](class_popup.md#class_Popup) node.

---

<span id="class_TabContainer_method_set_tab_button_icon"></span>

void **set_tab_button_icon** ( tab_idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_tabcontainer.md#class_TabContainer_method_set_tab_button_icon)

Sets the button icon from the tab at index `tab_idx`.

---

<span id="class_TabContainer_method_set_tab_disabled"></span>

void **set_tab_disabled** ( tab_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) [🔗](class_tabcontainer.md#class_TabContainer_method_set_tab_disabled)

If `disabled` is `true`, disables the tab at index `tab_idx`, making it non-interactable.

---

<span id="class_TabContainer_method_set_tab_hidden"></span>

void **set_tab_hidden** ( tab_idx: [int](class_int.md#class_int), hidden: [bool](class_bool.md#class_bool) ) [🔗](class_tabcontainer.md#class_TabContainer_method_set_tab_hidden)

If `hidden` is `true`, hides the tab at index `tab_idx`, making it disappear from the tab area.

---

<span id="class_TabContainer_method_set_tab_icon"></span>

void **set_tab_icon** ( tab_idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_tabcontainer.md#class_TabContainer_method_set_tab_icon)

Sets an icon for the tab at index `tab_idx`.

---

<span id="class_TabContainer_method_set_tab_icon_max_width"></span>

void **set_tab_icon_max_width** ( tab_idx: [int](class_int.md#class_int), width: [int](class_int.md#class_int) ) [🔗](class_tabcontainer.md#class_TabContainer_method_set_tab_icon_max_width)

Sets the maximum allowed width of the icon for the tab at index `tab_idx`. This limit is applied on top of the default size of the icon and on top of [icon_max_width](class_tabcontainer.md#class_TabContainer_theme_constant_icon_max_width). The height is adjusted according to the icon's ratio.

---

<span id="class_TabContainer_method_set_tab_metadata"></span>

void **set_tab_metadata** ( tab_idx: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) [🔗](class_tabcontainer.md#class_TabContainer_method_set_tab_metadata)

Sets the metadata value for the tab at index `tab_idx`, which can be retrieved later using [get_tab_metadata()](class_tabcontainer.md#class_TabContainer_method_get_tab_metadata).

---

<span id="class_TabContainer_method_set_tab_title"></span>

void **set_tab_title** ( tab_idx: [int](class_int.md#class_int), title: [String](class_string.md#class_String) ) [🔗](class_tabcontainer.md#class_TabContainer_method_set_tab_title)

Sets a custom title for the tab at index `tab_idx` (tab titles default to the name of the indexed child node). Set it back to the child's name to make the tab default to it again.

---

<span id="class_TabContainer_method_set_tab_tooltip"></span>

void **set_tab_tooltip** ( tab_idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) [🔗](class_tabcontainer.md#class_TabContainer_method_set_tab_tooltip)

Sets a custom tooltip text for tab at index `tab_idx`.

 **Note:** By default, if the `tooltip` is empty and the tab text is truncated (not all characters fit into the tab), the title will be displayed as a tooltip. To hide the tooltip, assign `" "` as the `tooltip` text.

---

### Theme Property Descriptions

<span id="class_TabContainer_theme_color_drop_mark_color"></span>

[Color](class_color.md#class_Color) **drop_mark_color** = `Color(1, 1, 1, 1)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_drop_mark_color)

Modulation color for the [drop_mark](class_tabcontainer.md#class_TabContainer_theme_icon_drop_mark) icon.

---

<span id="class_TabContainer_theme_color_font_disabled_color"></span>

[Color](class_color.md#class_Color) **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_font_disabled_color)

Font color of disabled tabs.

---

<span id="class_TabContainer_theme_color_font_hovered_color"></span>

[Color](class_color.md#class_Color) **font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_font_hovered_color)

Font color of the currently hovered tab. Does not apply to the selected tab.

---

<span id="class_TabContainer_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_font_outline_color)

The tint of text outline of the tab name.

---

<span id="class_TabContainer_theme_color_font_selected_color"></span>

[Color](class_color.md#class_Color) **font_selected_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_font_selected_color)

Font color of the currently selected tab.

---

<span id="class_TabContainer_theme_color_font_unselected_color"></span>

[Color](class_color.md#class_Color) **font_unselected_color** = `Color(0.7, 0.7, 0.7, 1)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_font_unselected_color)

Font color of the other, unselected tabs.

---

<span id="class_TabContainer_theme_color_icon_disabled_color"></span>

[Color](class_color.md#class_Color) **icon_disabled_color** = `Color(1, 1, 1, 1)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_icon_disabled_color)

Icon color of disabled tabs.

---

<span id="class_TabContainer_theme_color_icon_hovered_color"></span>

[Color](class_color.md#class_Color) **icon_hovered_color** = `Color(1, 1, 1, 1)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_icon_hovered_color)

Icon color of the currently hovered tab. Does not apply to the selected tab.

---

<span id="class_TabContainer_theme_color_icon_selected_color"></span>

[Color](class_color.md#class_Color) **icon_selected_color** = `Color(1, 1, 1, 1)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_icon_selected_color)

Icon color of the currently selected tab.

---

<span id="class_TabContainer_theme_color_icon_unselected_color"></span>

[Color](class_color.md#class_Color) **icon_unselected_color** = `Color(1, 1, 1, 1)` [🔗](class_tabcontainer.md#class_TabContainer_theme_color_icon_unselected_color)

Icon color of the other, unselected tabs.

---

<span id="class_TabContainer_theme_constant_icon_max_width"></span>

[int](class_int.md#class_int) **icon_max_width** = `0` [🔗](class_tabcontainer.md#class_TabContainer_theme_constant_icon_max_width)

The maximum allowed width of the tab's icon. This limit is applied on top of the default size of the icon, but before the value set with [TabBar.set_tab_icon_max_width()](class_tabbar.md#class_TabBar_method_set_tab_icon_max_width). The height is adjusted according to the icon's ratio.

---

<span id="class_TabContainer_theme_constant_icon_separation"></span>

[int](class_int.md#class_int) **icon_separation** = `4` [🔗](class_tabcontainer.md#class_TabContainer_theme_constant_icon_separation)

Space between tab's name and its icon.

---

<span id="class_TabContainer_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_tabcontainer.md#class_TabContainer_theme_constant_outline_size)

The size of the tab text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_tabcontainer.md#class_TabContainer_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_TabContainer_theme_constant_side_margin"></span>

[int](class_int.md#class_int) **side_margin** = `8` [🔗](class_tabcontainer.md#class_TabContainer_theme_constant_side_margin)

The space at the left or right edges of the tab bar, accordingly with the current [tab_alignment](class_tabcontainer.md#class_TabContainer_property_tab_alignment).

The margin is ignored with [TabBar.ALIGNMENT_RIGHT](class_tabbar.md#class_TabBar_constant_ALIGNMENT_RIGHT) if the tabs are clipped (see [clip_tabs](class_tabcontainer.md#class_TabContainer_property_clip_tabs)) or a popup has been set (see [set_popup()](class_tabcontainer.md#class_TabContainer_method_set_popup)). The margin is always ignored with [TabBar.ALIGNMENT_CENTER](class_tabbar.md#class_TabBar_constant_ALIGNMENT_CENTER).

---

<span id="class_TabContainer_theme_constant_tab_separation"></span>

[int](class_int.md#class_int) **tab_separation** = `0` [🔗](class_tabcontainer.md#class_TabContainer_theme_constant_tab_separation)

The space between tabs in the tab bar.

---

<span id="class_TabContainer_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_tabcontainer.md#class_TabContainer_theme_font_font)

The font used to draw tab names.

---

<span id="class_TabContainer_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_tabcontainer.md#class_TabContainer_theme_font_size_font_size)

Font size of the tab names.

---

<span id="class_TabContainer_theme_icon_decrement"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **decrement** [🔗](class_tabcontainer.md#class_TabContainer_theme_icon_decrement)

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the first tab is visible), it appears semi-transparent.

---

<span id="class_TabContainer_theme_icon_decrement_highlight"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **decrement_highlight** [🔗](class_tabcontainer.md#class_TabContainer_theme_icon_decrement_highlight)

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

---

<span id="class_TabContainer_theme_icon_drop_mark"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **drop_mark** [🔗](class_tabcontainer.md#class_TabContainer_theme_icon_drop_mark)

Icon shown to indicate where a dragged tab is gonna be dropped (see [drag_to_rearrange_enabled](class_tabcontainer.md#class_TabContainer_property_drag_to_rearrange_enabled)).

---

<span id="class_TabContainer_theme_icon_increment"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **increment** [🔗](class_tabcontainer.md#class_TabContainer_theme_icon_increment)

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the last tab is visible) it appears semi-transparent.

---

<span id="class_TabContainer_theme_icon_increment_highlight"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **increment_highlight** [🔗](class_tabcontainer.md#class_TabContainer_theme_icon_increment_highlight)

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

---

<span id="class_TabContainer_theme_icon_menu"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **menu** [🔗](class_tabcontainer.md#class_TabContainer_theme_icon_menu)

The icon for the menu button (see [set_popup()](class_tabcontainer.md#class_TabContainer_method_set_popup)).

---

<span id="class_TabContainer_theme_icon_menu_highlight"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **menu_highlight** [🔗](class_tabcontainer.md#class_TabContainer_theme_icon_menu_highlight)

The icon for the menu button (see [set_popup()](class_tabcontainer.md#class_TabContainer_method_set_popup)) when it's being hovered with the cursor.

---

<span id="class_TabContainer_theme_style_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **panel** [🔗](class_tabcontainer.md#class_TabContainer_theme_style_panel)

The style for the background fill.

---

<span id="class_TabContainer_theme_style_tab_disabled"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_disabled** [🔗](class_tabcontainer.md#class_TabContainer_theme_style_tab_disabled)

The style of disabled tabs.

---

<span id="class_TabContainer_theme_style_tab_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_focus** [🔗](class_tabcontainer.md#class_TabContainer_theme_style_tab_focus)

[StyleBox](class_stylebox.md#class_StyleBox) used when the [TabBar](class_tabbar.md#class_TabBar) is focused. The [tab_focus](class_tabcontainer.md#class_TabContainer_theme_style_tab_focus) [StyleBox](class_stylebox.md#class_StyleBox) is displayed *over* the base [StyleBox](class_stylebox.md#class_StyleBox) of the selected tab, so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the base [StyleBox](class_stylebox.md#class_StyleBox) remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_TabContainer_theme_style_tab_hovered"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_hovered** [🔗](class_tabcontainer.md#class_TabContainer_theme_style_tab_hovered)

The style of the currently hovered tab.

 **Note:** This style will be drawn with the same width as [tab_unselected](class_tabcontainer.md#class_TabContainer_theme_style_tab_unselected) at minimum.

---

<span id="class_TabContainer_theme_style_tab_selected"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_selected** [🔗](class_tabcontainer.md#class_TabContainer_theme_style_tab_selected)

The style of the currently selected tab.

---

<span id="class_TabContainer_theme_style_tab_unselected"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tab_unselected** [🔗](class_tabcontainer.md#class_TabContainer_theme_style_tab_unselected)

The style of the other, unselected tabs.

---

<span id="class_TabContainer_theme_style_tabbar_background"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **tabbar_background** [🔗](class_tabcontainer.md#class_TabContainer_theme_style_tabbar_background)

The style for the background fill of the [TabBar](class_tabbar.md#class_TabBar) area.
