<span id="class_ItemList"></span>

## ItemList

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A vertical list of selectable items with one or multiple columns.

### Description

This control provides a vertical list of selectable items that may be in a single or in multiple columns, with each item having options for text and an icon. Tooltips are supported and may be different for every item in the list.

Selectable items in the list may be selected or deselected and multiple selection may be enabled. Selection with right mouse button may also be enabled to allow use of popup context menus. Items may also be "activated" by double-clicking them or by pressing :kbd:`Enter`.

Item text only supports single-line strings. Newline characters (e.g. `\n`) in the string won't produce a newline. Text wrapping is enabled in [ICON_MODE_TOP](class_itemlist.md#class_ItemList_constant_ICON_MODE_TOP) mode, but the column's width is adjusted to fully fit its content by default. You need to set [fixed_column_width](class_itemlist.md#class_ItemList_property_fixed_column_width) greater than zero to wrap the text.

All `set_*` methods allow negative item indices, i.e. `-1` to access the last item, `-2` to select the second-to-last item, and so on.

 **Incremental search:** Like [PopupMenu](class_popupmenu.md#class_PopupMenu) and [Tree](class_tree.md#class_Tree), **ItemList** supports searching within the list while the control is focused. Press a key that matches the first letter of an item's name to select the first item starting with the given letter. After that point, there are two ways to perform incremental search: 1) Press the same key again before the timeout duration to select the next item starting with the same letter. 2) Press letter keys that match the rest of the word before the timeout duration to match to select the item in question directly. Both of these actions will be reset to the beginning of the list if the timeout duration has passed since the last keystroke was registered. You can adjust the timeout duration by changing ProjectSettings.gui/timers/incremental_search_max_interval_msec.

### Properties


| [bool](class_bool.md#class_bool) | [allow_reselect](class_itemlist.md#class_ItemList_property_allow_reselect) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [allow_rmb_select](class_itemlist.md#class_ItemList_property_allow_rmb_select) | `false` |
| [bool](class_bool.md#class_bool) | [allow_search](class_itemlist.md#class_ItemList_property_allow_search) | `true` |
| [bool](class_bool.md#class_bool) | [auto_height](class_itemlist.md#class_ItemList_property_auto_height) | `false` |
| [bool](class_bool.md#class_bool) | [auto_width](class_itemlist.md#class_ItemList_property_auto_width) | `false` |
| [bool](class_bool.md#class_bool) | clip_contents | `true` (overrides [Control](class_control.md#class_Control_property_clip_contents)) |
| [int](class_int.md#class_int) | [fixed_column_width](class_itemlist.md#class_ItemList_property_fixed_column_width) | `0` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [fixed_icon_size](class_itemlist.md#class_ItemList_property_fixed_icon_size) | `Vector2i(0, 0)` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `2` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [IconMode](class_itemlist.md#enum_ItemList_IconMode) | [icon_mode](class_itemlist.md#class_ItemList_property_icon_mode) | `1` |
| [float](class_float.md#class_float) | [icon_scale](class_itemlist.md#class_ItemList_property_icon_scale) | `1.0` |
| [int](class_int.md#class_int) | [item_count](class_itemlist.md#class_ItemList_property_item_count) | `0` |
| [int](class_int.md#class_int) | [max_columns](class_itemlist.md#class_ItemList_property_max_columns) | `1` |
| [int](class_int.md#class_int) | [max_text_lines](class_itemlist.md#class_ItemList_property_max_text_lines) | `1` |
| [bool](class_bool.md#class_bool) | [same_column_width](class_itemlist.md#class_ItemList_property_same_column_width) | `false` |
| [ScrollHintMode](class_itemlist.md#enum_ItemList_ScrollHintMode) | [scroll_hint_mode](class_itemlist.md#class_ItemList_property_scroll_hint_mode) | `0` |
| [SelectMode](class_itemlist.md#enum_ItemList_SelectMode) | [select_mode](class_itemlist.md#class_ItemList_property_select_mode) | `0` |
| [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) | [text_overrun_behavior](class_itemlist.md#class_ItemList_property_text_overrun_behavior) | `3` |
| [bool](class_bool.md#class_bool) | [tile_scroll_hint](class_itemlist.md#class_ItemList_property_tile_scroll_hint) | `false` |
| [bool](class_bool.md#class_bool) | [wraparound_items](class_itemlist.md#class_ItemList_property_wraparound_items) | `true` |

### Methods


| [int](class_int.md#class_int) | [add_icon_item](class_itemlist.md#class_ItemList_method_add_icon_item) ( icon: [Texture2D](class_texture2d.md#class_Texture2D), selectable: [bool](class_bool.md#class_bool) = true ) |
| --- | --- |
| [int](class_int.md#class_int) | [add_item](class_itemlist.md#class_ItemList_method_add_item) ( text: [String](class_string.md#class_String), icon: [Texture2D](class_texture2d.md#class_Texture2D) = null, selectable: [bool](class_bool.md#class_bool) = true ) |
| void | [center_on_current](class_itemlist.md#class_ItemList_method_center_on_current) ( center_verically: [bool](class_bool.md#class_bool) = true, center_horizontally: [bool](class_bool.md#class_bool) = true ) |
| void | [clear](class_itemlist.md#class_ItemList_method_clear) ( ) |
| void | [deselect](class_itemlist.md#class_ItemList_method_deselect) ( idx: [int](class_int.md#class_int) ) |
| void | [deselect_all](class_itemlist.md#class_ItemList_method_deselect_all) ( ) |
| void | [ensure_current_is_visible](class_itemlist.md#class_ItemList_method_ensure_current_is_visible) ( ) |
| void | [force_update_list_size](class_itemlist.md#class_ItemList_method_force_update_list_size) ( ) |
| [HScrollBar](class_hscrollbar.md#class_HScrollBar) | [get_h_scroll_bar](class_itemlist.md#class_ItemList_method_get_h_scroll_bar) ( ) |
| [int](class_int.md#class_int) | [get_item_at_position](class_itemlist.md#class_ItemList_method_get_item_at_position) ( position: [Vector2](class_vector2.md#class_Vector2), exact: [bool](class_bool.md#class_bool) = false ) const |
| [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) | [get_item_auto_translate_mode](class_itemlist.md#class_ItemList_method_get_item_auto_translate_mode) ( idx: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_item_custom_bg_color](class_itemlist.md#class_ItemList_method_get_item_custom_bg_color) ( idx: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_item_custom_fg_color](class_itemlist.md#class_ItemList_method_get_item_custom_fg_color) ( idx: [int](class_int.md#class_int) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_item_icon](class_itemlist.md#class_ItemList_method_get_item_icon) ( idx: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_item_icon_modulate](class_itemlist.md#class_ItemList_method_get_item_icon_modulate) ( idx: [int](class_int.md#class_int) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [get_item_icon_region](class_itemlist.md#class_ItemList_method_get_item_icon_region) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_item_language](class_itemlist.md#class_ItemList_method_get_item_language) ( idx: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_item_metadata](class_itemlist.md#class_ItemList_method_get_item_metadata) ( idx: [int](class_int.md#class_int) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [get_item_rect](class_itemlist.md#class_ItemList_method_get_item_rect) ( idx: [int](class_int.md#class_int), expand: [bool](class_bool.md#class_bool) = true ) const |
| [String](class_string.md#class_String) | [get_item_text](class_itemlist.md#class_ItemList_method_get_item_text) ( idx: [int](class_int.md#class_int) ) const |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [get_item_text_direction](class_itemlist.md#class_ItemList_method_get_item_text_direction) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_item_tooltip](class_itemlist.md#class_ItemList_method_get_item_tooltip) ( idx: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_selected_items](class_itemlist.md#class_ItemList_method_get_selected_items) ( ) |
| [VScrollBar](class_vscrollbar.md#class_VScrollBar) | [get_v_scroll_bar](class_itemlist.md#class_ItemList_method_get_v_scroll_bar) ( ) |
| [bool](class_bool.md#class_bool) | [is_anything_selected](class_itemlist.md#class_ItemList_method_is_anything_selected) ( ) |
| [bool](class_bool.md#class_bool) | [is_item_disabled](class_itemlist.md#class_ItemList_method_is_item_disabled) ( idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_item_icon_transposed](class_itemlist.md#class_ItemList_method_is_item_icon_transposed) ( idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_item_selectable](class_itemlist.md#class_ItemList_method_is_item_selectable) ( idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_item_tooltip_enabled](class_itemlist.md#class_ItemList_method_is_item_tooltip_enabled) ( idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_selected](class_itemlist.md#class_ItemList_method_is_selected) ( idx: [int](class_int.md#class_int) ) const |
| void | [move_item](class_itemlist.md#class_ItemList_method_move_item) ( from_idx: [int](class_int.md#class_int), to_idx: [int](class_int.md#class_int) ) |
| void | [remove_item](class_itemlist.md#class_ItemList_method_remove_item) ( idx: [int](class_int.md#class_int) ) |
| void | [select](class_itemlist.md#class_ItemList_method_select) ( idx: [int](class_int.md#class_int), single: [bool](class_bool.md#class_bool) = true ) |
| void | [set_item_auto_translate_mode](class_itemlist.md#class_ItemList_method_set_item_auto_translate_mode) ( idx: [int](class_int.md#class_int), mode: [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) ) |
| void | [set_item_custom_bg_color](class_itemlist.md#class_ItemList_method_set_item_custom_bg_color) ( idx: [int](class_int.md#class_int), custom_bg_color: [Color](class_color.md#class_Color) ) |
| void | [set_item_custom_fg_color](class_itemlist.md#class_ItemList_method_set_item_custom_fg_color) ( idx: [int](class_int.md#class_int), custom_fg_color: [Color](class_color.md#class_Color) ) |
| void | [set_item_disabled](class_itemlist.md#class_ItemList_method_set_item_disabled) ( idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) |
| void | [set_item_icon](class_itemlist.md#class_ItemList_method_set_item_icon) ( idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_item_icon_modulate](class_itemlist.md#class_ItemList_method_set_item_icon_modulate) ( idx: [int](class_int.md#class_int), modulate: [Color](class_color.md#class_Color) ) |
| void | [set_item_icon_region](class_itemlist.md#class_ItemList_method_set_item_icon_region) ( idx: [int](class_int.md#class_int), rect: [Rect2](class_rect2.md#class_Rect2) ) |
| void | [set_item_icon_transposed](class_itemlist.md#class_ItemList_method_set_item_icon_transposed) ( idx: [int](class_int.md#class_int), transposed: [bool](class_bool.md#class_bool) ) |
| void | [set_item_language](class_itemlist.md#class_ItemList_method_set_item_language) ( idx: [int](class_int.md#class_int), language: [String](class_string.md#class_String) ) |
| void | [set_item_metadata](class_itemlist.md#class_ItemList_method_set_item_metadata) ( idx: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) |
| void | [set_item_selectable](class_itemlist.md#class_ItemList_method_set_item_selectable) ( idx: [int](class_int.md#class_int), selectable: [bool](class_bool.md#class_bool) ) |
| void | [set_item_text](class_itemlist.md#class_ItemList_method_set_item_text) ( idx: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) |
| void | [set_item_text_direction](class_itemlist.md#class_ItemList_method_set_item_text_direction) ( idx: [int](class_int.md#class_int), direction: [TextDirection](class_control.md#enum_Control_TextDirection) ) |
| void | [set_item_tooltip](class_itemlist.md#class_ItemList_method_set_item_tooltip) ( idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) |
| void | [set_item_tooltip_enabled](class_itemlist.md#class_ItemList_method_set_item_tooltip_enabled) ( idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| void | [sort_items_by_text](class_itemlist.md#class_ItemList_method_sort_items_by_text) ( ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [font_color](class_itemlist.md#class_ItemList_theme_color_font_color) | `Color(0.65, 0.65, 0.65, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_hovered_color](class_itemlist.md#class_ItemList_theme_color_font_hovered_color) | `Color(0.95, 0.95, 0.95, 1)` |
| [Color](class_color.md#class_Color) | [font_hovered_selected_color](class_itemlist.md#class_ItemList_theme_color_font_hovered_selected_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [font_outline_color](class_itemlist.md#class_ItemList_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_selected_color](class_itemlist.md#class_ItemList_theme_color_font_selected_color) | `Color(1, 1, 1, 1)` |
| [Color](class_color.md#class_Color) | [guide_color](class_itemlist.md#class_ItemList_theme_color_guide_color) | `Color(0.7, 0.7, 0.7, 0.25)` |
| [Color](class_color.md#class_Color) | [scroll_hint_color](class_itemlist.md#class_ItemList_theme_color_scroll_hint_color) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class_int) | [h_separation](class_itemlist.md#class_ItemList_theme_constant_h_separation) | `4` |
| [int](class_int.md#class_int) | [icon_margin](class_itemlist.md#class_ItemList_theme_constant_icon_margin) | `4` |
| [int](class_int.md#class_int) | [line_separation](class_itemlist.md#class_ItemList_theme_constant_line_separation) | `2` |
| [int](class_int.md#class_int) | [outline_size](class_itemlist.md#class_ItemList_theme_constant_outline_size) | `0` |
| [int](class_int.md#class_int) | [v_separation](class_itemlist.md#class_ItemList_theme_constant_v_separation) | `4` |
| [Font](class_font.md#class_Font) | [font](class_itemlist.md#class_ItemList_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_itemlist.md#class_ItemList_theme_font_size_font_size) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [scroll_hint](class_itemlist.md#class_ItemList_theme_icon_scroll_hint) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [cursor](class_itemlist.md#class_ItemList_theme_style_cursor) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [cursor_unfocused](class_itemlist.md#class_ItemList_theme_style_cursor_unfocused) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [focus](class_itemlist.md#class_ItemList_theme_style_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hovered](class_itemlist.md#class_ItemList_theme_style_hovered) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hovered_selected](class_itemlist.md#class_ItemList_theme_style_hovered_selected) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [hovered_selected_focus](class_itemlist.md#class_ItemList_theme_style_hovered_selected_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [panel](class_itemlist.md#class_ItemList_theme_style_panel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [selected](class_itemlist.md#class_ItemList_theme_style_selected) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [selected_focus](class_itemlist.md#class_ItemList_theme_style_selected_focus) |

---

### Signals

<span id="class_ItemList_signal_empty_clicked"></span>

**empty_clicked** ( at_position: [Vector2](class_vector2.md#class_Vector2), mouse_button_index: [int](class_int.md#class_int) ) [🔗](class_itemlist.md#class_ItemList_signal_empty_clicked)

Emitted when any mouse click is issued within the rect of the list but on empty space.

 `at_position` is the click position in this control's local coordinate system.

---

<span id="class_ItemList_signal_item_activated"></span>

**item_activated** ( index: [int](class_int.md#class_int) ) [🔗](class_itemlist.md#class_ItemList_signal_item_activated)

Emitted when specified list item is activated via double-clicking or by pressing :kbd:`Enter`.

---

<span id="class_ItemList_signal_item_clicked"></span>

**item_clicked** ( index: [int](class_int.md#class_int), at_position: [Vector2](class_vector2.md#class_Vector2), mouse_button_index: [int](class_int.md#class_int) ) [🔗](class_itemlist.md#class_ItemList_signal_item_clicked)

Emitted when specified list item has been clicked with any mouse button.

 `at_position` is the click position in this control's local coordinate system.

---

<span id="class_ItemList_signal_item_selected"></span>

**item_selected** ( index: [int](class_int.md#class_int) ) [🔗](class_itemlist.md#class_ItemList_signal_item_selected)

Emitted when specified item has been selected. Only applicable in single selection mode.

 [allow_reselect](class_itemlist.md#class_ItemList_property_allow_reselect) must be enabled to reselect an item.

---

<span id="class_ItemList_signal_multi_selected"></span>

**multi_selected** ( index: [int](class_int.md#class_int), selected: [bool](class_bool.md#class_bool) ) [🔗](class_itemlist.md#class_ItemList_signal_multi_selected)

Emitted when a multiple selection is altered on a list allowing multiple selection.

---

### Enumerations

<span id="enum_ItemList_IconMode"></span>

enum **IconMode**: [🔗](class_itemlist.md#enum_ItemList_IconMode)

<span id="class_ItemList_constant_ICON_MODE_TOP"></span>

[IconMode](class_itemlist.md#enum_ItemList_IconMode) **ICON_MODE_TOP** = `0`

Icon is drawn above the text.

<span id="class_ItemList_constant_ICON_MODE_LEFT"></span>

[IconMode](class_itemlist.md#enum_ItemList_IconMode) **ICON_MODE_LEFT** = `1`

Icon is drawn to the left of the text.

---

<span id="enum_ItemList_SelectMode"></span>

enum **SelectMode**: [🔗](class_itemlist.md#enum_ItemList_SelectMode)

<span id="class_ItemList_constant_SELECT_SINGLE"></span>

[SelectMode](class_itemlist.md#enum_ItemList_SelectMode) **SELECT_SINGLE** = `0`

Only allow selecting a single item.

<span id="class_ItemList_constant_SELECT_MULTI"></span>

[SelectMode](class_itemlist.md#enum_ItemList_SelectMode) **SELECT_MULTI** = `1`

Allows selecting multiple items by holding :kbd:`Ctrl` or :kbd:`Shift`.

<span id="class_ItemList_constant_SELECT_TOGGLE"></span>

[SelectMode](class_itemlist.md#enum_ItemList_SelectMode) **SELECT_TOGGLE** = `2`

Allows selecting multiple items by toggling them on and off.

---

<span id="enum_ItemList_ScrollHintMode"></span>

enum **ScrollHintMode**: [🔗](class_itemlist.md#enum_ItemList_ScrollHintMode)

<span id="class_ItemList_constant_SCROLL_HINT_MODE_DISABLED"></span>

[ScrollHintMode](class_itemlist.md#enum_ItemList_ScrollHintMode) **SCROLL_HINT_MODE_DISABLED** = `0`

Scroll hints will never be shown.

<span id="class_ItemList_constant_SCROLL_HINT_MODE_BOTH"></span>

[ScrollHintMode](class_itemlist.md#enum_ItemList_ScrollHintMode) **SCROLL_HINT_MODE_BOTH** = `1`

Scroll hints will be shown at the top and bottom.

<span id="class_ItemList_constant_SCROLL_HINT_MODE_TOP"></span>

[ScrollHintMode](class_itemlist.md#enum_ItemList_ScrollHintMode) **SCROLL_HINT_MODE_TOP** = `2`

Only the top scroll hint will be shown.

<span id="class_ItemList_constant_SCROLL_HINT_MODE_BOTTOM"></span>

[ScrollHintMode](class_itemlist.md#enum_ItemList_ScrollHintMode) **SCROLL_HINT_MODE_BOTTOM** = `3`

Only the bottom scroll hint will be shown.

---

### Property Descriptions

<span id="class_ItemList_property_allow_reselect"></span>

[bool](class_bool.md#class_bool) **allow_reselect** = `false` [🔗](class_itemlist.md#class_ItemList_property_allow_reselect)

- void **set_allow_reselect** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_allow_reselect** ( )

If `true`, the currently selected item can be selected again.

---

<span id="class_ItemList_property_allow_rmb_select"></span>

[bool](class_bool.md#class_bool) **allow_rmb_select** = `false` [🔗](class_itemlist.md#class_ItemList_property_allow_rmb_select)

- void **set_allow_rmb_select** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_allow_rmb_select** ( )

If `true`, right mouse button click can select items.

---

<span id="class_ItemList_property_allow_search"></span>

[bool](class_bool.md#class_bool) **allow_search** = `true` [🔗](class_itemlist.md#class_ItemList_property_allow_search)

- void **set_allow_search** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_allow_search** ( )

If `true`, allows navigating the **ItemList** with letter keys through incremental search.

---

<span id="class_ItemList_property_auto_height"></span>

[bool](class_bool.md#class_bool) **auto_height** = `false` [🔗](class_itemlist.md#class_ItemList_property_auto_height)

- void **set_auto_height** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_auto_height** ( )

If `true`, the control will automatically resize the height to fit its content.

---

<span id="class_ItemList_property_auto_width"></span>

[bool](class_bool.md#class_bool) **auto_width** = `false` [🔗](class_itemlist.md#class_ItemList_property_auto_width)

- void **set_auto_width** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_auto_width** ( )

If `true`, the control will automatically resize the width to fit its content.

---

<span id="class_ItemList_property_fixed_column_width"></span>

[int](class_int.md#class_int) **fixed_column_width** = `0` [🔗](class_itemlist.md#class_ItemList_property_fixed_column_width)

- void **set_fixed_column_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_fixed_column_width** ( )

The width all columns will be adjusted to.

A value of zero disables the adjustment, each item will have a width equal to the width of its content and the columns will have an uneven width.

---

<span id="class_ItemList_property_fixed_icon_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **fixed_icon_size** = `Vector2i(0, 0)` [🔗](class_itemlist.md#class_ItemList_property_fixed_icon_size)

- void **set_fixed_icon_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_fixed_icon_size** ( )

The size all icons will be adjusted to.

If either X or Y component is not greater than zero, icon size won't be affected.

---

<span id="class_ItemList_property_icon_mode"></span>

[IconMode](class_itemlist.md#enum_ItemList_IconMode) **icon_mode** = `1` [🔗](class_itemlist.md#class_ItemList_property_icon_mode)

- void **set_icon_mode** ( value: [IconMode](class_itemlist.md#enum_ItemList_IconMode) )
- [IconMode](class_itemlist.md#enum_ItemList_IconMode) **get_icon_mode** ( )

The icon position, whether above or to the left of the text. See the [IconMode](class_itemlist.md#enum_ItemList_IconMode) constants.

---

<span id="class_ItemList_property_icon_scale"></span>

[float](class_float.md#class_float) **icon_scale** = `1.0` [🔗](class_itemlist.md#class_ItemList_property_icon_scale)

- void **set_icon_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_icon_scale** ( )

The scale of icon applied after [fixed_icon_size](class_itemlist.md#class_ItemList_property_fixed_icon_size) and transposing takes effect.

---

<span id="class_ItemList_property_item_count"></span>

[int](class_int.md#class_int) **item_count** = `0` [🔗](class_itemlist.md#class_ItemList_property_item_count)

- void **set_item_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_item_count** ( )

The number of items currently in the list.

---

<span id="class_ItemList_property_max_columns"></span>

[int](class_int.md#class_int) **max_columns** = `1` [🔗](class_itemlist.md#class_ItemList_property_max_columns)

- void **set_max_columns** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_columns** ( )

Maximum columns the list will have.

If greater than zero, the content will be split among the specified columns.

A value of zero means unlimited columns, i.e. all items will be put in the same row.

---

<span id="class_ItemList_property_max_text_lines"></span>

[int](class_int.md#class_int) **max_text_lines** = `1` [🔗](class_itemlist.md#class_ItemList_property_max_text_lines)

- void **set_max_text_lines** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_text_lines** ( )

Maximum lines of text allowed in each item. Space will be reserved even when there is not enough lines of text to display.

 **Note:** This property takes effect only when [icon_mode](class_itemlist.md#class_ItemList_property_icon_mode) is [ICON_MODE_TOP](class_itemlist.md#class_ItemList_constant_ICON_MODE_TOP). To make the text wrap, [fixed_column_width](class_itemlist.md#class_ItemList_property_fixed_column_width) should be greater than zero.

---

<span id="class_ItemList_property_same_column_width"></span>

[bool](class_bool.md#class_bool) **same_column_width** = `false` [🔗](class_itemlist.md#class_ItemList_property_same_column_width)

- void **set_same_column_width** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_same_column_width** ( )

Whether all columns will have the same width.

If `true`, the width is equal to the largest column width of all columns.

---

<span id="class_ItemList_property_scroll_hint_mode"></span>

[ScrollHintMode](class_itemlist.md#enum_ItemList_ScrollHintMode) **scroll_hint_mode** = `0` [🔗](class_itemlist.md#class_ItemList_property_scroll_hint_mode)

- void **set_scroll_hint_mode** ( value: [ScrollHintMode](class_itemlist.md#enum_ItemList_ScrollHintMode) )
- [ScrollHintMode](class_itemlist.md#enum_ItemList_ScrollHintMode) **get_scroll_hint_mode** ( )

The way which scroll hints (indicators that show that the content can still be scrolled in a certain direction) will be shown.

---

<span id="class_ItemList_property_select_mode"></span>

[SelectMode](class_itemlist.md#enum_ItemList_SelectMode) **select_mode** = `0` [🔗](class_itemlist.md#class_ItemList_property_select_mode)

- void **set_select_mode** ( value: [SelectMode](class_itemlist.md#enum_ItemList_SelectMode) )
- [SelectMode](class_itemlist.md#enum_ItemList_SelectMode) **get_select_mode** ( )

Allows single or multiple item selection. See the [SelectMode](class_itemlist.md#enum_ItemList_SelectMode) constants.

---

<span id="class_ItemList_property_text_overrun_behavior"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **text_overrun_behavior** = `3` [🔗](class_itemlist.md#class_ItemList_property_text_overrun_behavior)

- void **set_text_overrun_behavior** ( value: [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) )
- [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **get_text_overrun_behavior** ( )

The clipping behavior when the text exceeds an item's bounding rectangle.

---

<span id="class_ItemList_property_tile_scroll_hint"></span>

[bool](class_bool.md#class_bool) **tile_scroll_hint** = `false` [🔗](class_itemlist.md#class_ItemList_property_tile_scroll_hint)

- void **set_tile_scroll_hint** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_scroll_hint_tiled** ( )

If `true`, the scroll hint texture will be tiled instead of stretched. See [scroll_hint_mode](class_itemlist.md#class_ItemList_property_scroll_hint_mode).

---

<span id="class_ItemList_property_wraparound_items"></span>

[bool](class_bool.md#class_bool) **wraparound_items** = `true` [🔗](class_itemlist.md#class_ItemList_property_wraparound_items)

- void **set_wraparound_items** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_wraparound_items** ( )

If `true`, the control will automatically move items into a new row to fit its content. See also [HFlowContainer](class_hflowcontainer.md#class_HFlowContainer) for this behavior.

If `false`, the control will add a horizontal scrollbar to make all items visible.

---

### Method Descriptions

<span id="class_ItemList_method_add_icon_item"></span>

[int](class_int.md#class_int) **add_icon_item** ( icon: [Texture2D](class_texture2d.md#class_Texture2D), selectable: [bool](class_bool.md#class_bool) = true ) [🔗](class_itemlist.md#class_ItemList_method_add_icon_item)

Adds an item to the item list with no text, only an icon. Returns the index of an added item.

---

<span id="class_ItemList_method_add_item"></span>

[int](class_int.md#class_int) **add_item** ( text: [String](class_string.md#class_String), icon: [Texture2D](class_texture2d.md#class_Texture2D) = null, selectable: [bool](class_bool.md#class_bool) = true ) [🔗](class_itemlist.md#class_ItemList_method_add_item)

Adds an item to the item list with specified text. Returns the index of an added item.

Specify an `icon`, or use `null` as the `icon` for a list item with no icon.

If `selectable` is `true`, the list item will be selectable.

---

<span id="class_ItemList_method_center_on_current"></span>

void **center_on_current** ( center_verically: [bool](class_bool.md#class_bool) = true, center_horizontally: [bool](class_bool.md#class_bool) = true ) [🔗](class_itemlist.md#class_ItemList_method_center_on_current)

Ensures the currently selected item (the first selected item if multiple selection is enabled) is visible, adjusting the scroll position as necessary to place the item at the center of the list if possible. See also [ensure_current_is_visible()](class_itemlist.md#class_ItemList_method_ensure_current_is_visible).

Fails and prints an error if both arguments are `false`.

---

<span id="class_ItemList_method_clear"></span>

void **clear** ( ) [🔗](class_itemlist.md#class_ItemList_method_clear)

Removes all items from the list.

---

<span id="class_ItemList_method_deselect"></span>

void **deselect** ( idx: [int](class_int.md#class_int) ) [🔗](class_itemlist.md#class_ItemList_method_deselect)

Ensures the item associated with the specified index is not selected.

---

<span id="class_ItemList_method_deselect_all"></span>

void **deselect_all** ( ) [🔗](class_itemlist.md#class_ItemList_method_deselect_all)

Ensures there are no items selected.

---

<span id="class_ItemList_method_ensure_current_is_visible"></span>

void **ensure_current_is_visible** ( ) [🔗](class_itemlist.md#class_ItemList_method_ensure_current_is_visible)

Ensures the currently selected item (the first selected item if multiple selection is enabled) is visible, adjusting the scroll position as necessary. See also [center_on_current()](class_itemlist.md#class_ItemList_method_center_on_current).

---

<span id="class_ItemList_method_force_update_list_size"></span>

void **force_update_list_size** ( ) [🔗](class_itemlist.md#class_ItemList_method_force_update_list_size)

Forces an update to the list size based on its items. This happens automatically whenever size of the items, or other relevant settings like [auto_height](class_itemlist.md#class_ItemList_property_auto_height), change. The method can be used to trigger the update ahead of next drawing pass.

---

<span id="class_ItemList_method_get_h_scroll_bar"></span>

[HScrollBar](class_hscrollbar.md#class_HScrollBar) **get_h_scroll_bar** ( ) [🔗](class_itemlist.md#class_ItemList_method_get_h_scroll_bar)

Returns the horizontal scrollbar.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.

---

<span id="class_ItemList_method_get_item_at_position"></span>

[int](class_int.md#class_int) **get_item_at_position** ( position: [Vector2](class_vector2.md#class_Vector2), exact: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_at_position)

Returns the item index at the given `position`.

When there is no item at that point, -1 will be returned if `exact` is `true`, and the closest item index will be returned otherwise.

 **Note:** The returned value is unreliable if called right after modifying the **ItemList**, before it redraws in the next frame.

---

<span id="class_ItemList_method_get_item_auto_translate_mode"></span>

[AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) **get_item_auto_translate_mode** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_auto_translate_mode)

Returns item's auto translate mode.

---

<span id="class_ItemList_method_get_item_custom_bg_color"></span>

[Color](class_color.md#class_Color) **get_item_custom_bg_color** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_custom_bg_color)

Returns the custom background color of the item specified by `idx` index.

---

<span id="class_ItemList_method_get_item_custom_fg_color"></span>

[Color](class_color.md#class_Color) **get_item_custom_fg_color** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_custom_fg_color)

Returns the custom foreground color of the item specified by `idx` index.

---

<span id="class_ItemList_method_get_item_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_item_icon** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_icon)

Returns the icon associated with the specified index.

---

<span id="class_ItemList_method_get_item_icon_modulate"></span>

[Color](class_color.md#class_Color) **get_item_icon_modulate** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_icon_modulate)

Returns a [Color](class_color.md#class_Color) modulating item's icon at the specified index.

---

<span id="class_ItemList_method_get_item_icon_region"></span>

[Rect2](class_rect2.md#class_Rect2) **get_item_icon_region** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_icon_region)

Returns the region of item's icon used. The whole icon will be used if the region has no area.

---

<span id="class_ItemList_method_get_item_language"></span>

[String](class_string.md#class_String) **get_item_language** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_language)

Returns item's text language code.

---

<span id="class_ItemList_method_get_item_metadata"></span>

[Variant](class_variant.md#class_Variant) **get_item_metadata** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_metadata)

Returns the metadata value of the specified index.

---

<span id="class_ItemList_method_get_item_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **get_item_rect** ( idx: [int](class_int.md#class_int), expand: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_rect)

Returns the position and size of the item with the specified index, in the coordinate system of the **ItemList** node. If `expand` is `true` the last column expands to fill the rest of the row.

 **Note:** The returned value is unreliable if called right after modifying the **ItemList**, before it redraws in the next frame.

---

<span id="class_ItemList_method_get_item_text"></span>

[String](class_string.md#class_String) **get_item_text** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_text)

Returns the text associated with the specified index.

---

<span id="class_ItemList_method_get_item_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **get_item_text_direction** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_text_direction)

Returns item's text base writing direction.

---

<span id="class_ItemList_method_get_item_tooltip"></span>

[String](class_string.md#class_String) **get_item_tooltip** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_get_item_tooltip)

Returns the tooltip hint associated with the specified index.

---

<span id="class_ItemList_method_get_selected_items"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_selected_items** ( ) [🔗](class_itemlist.md#class_ItemList_method_get_selected_items)

Returns an array with the indexes of the selected items.

---

<span id="class_ItemList_method_get_v_scroll_bar"></span>

[VScrollBar](class_vscrollbar.md#class_VScrollBar) **get_v_scroll_bar** ( ) [🔗](class_itemlist.md#class_ItemList_method_get_v_scroll_bar)

Returns the vertical scrollbar.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.

---

<span id="class_ItemList_method_is_anything_selected"></span>

[bool](class_bool.md#class_bool) **is_anything_selected** ( ) [🔗](class_itemlist.md#class_ItemList_method_is_anything_selected)

Returns `true` if one or more items are selected.

---

<span id="class_ItemList_method_is_item_disabled"></span>

[bool](class_bool.md#class_bool) **is_item_disabled** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_is_item_disabled)

Returns `true` if the item at the specified index is disabled.

---

<span id="class_ItemList_method_is_item_icon_transposed"></span>

[bool](class_bool.md#class_bool) **is_item_icon_transposed** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_is_item_icon_transposed)

Returns `true` if the item icon will be drawn transposed, i.e. the X and Y axes are swapped.

---

<span id="class_ItemList_method_is_item_selectable"></span>

[bool](class_bool.md#class_bool) **is_item_selectable** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_is_item_selectable)

Returns `true` if the item at the specified index is selectable.

---

<span id="class_ItemList_method_is_item_tooltip_enabled"></span>

[bool](class_bool.md#class_bool) **is_item_tooltip_enabled** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_is_item_tooltip_enabled)

Returns `true` if the tooltip is enabled for specified item index.

---

<span id="class_ItemList_method_is_selected"></span>

[bool](class_bool.md#class_bool) **is_selected** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_itemlist.md#class_ItemList_method_is_selected)

Returns `true` if the item at the specified index is currently selected.

---

<span id="class_ItemList_method_move_item"></span>

void **move_item** ( from_idx: [int](class_int.md#class_int), to_idx: [int](class_int.md#class_int) ) [🔗](class_itemlist.md#class_ItemList_method_move_item)

Moves item from index `from_idx` to `to_idx`.

---

<span id="class_ItemList_method_remove_item"></span>

void **remove_item** ( idx: [int](class_int.md#class_int) ) [🔗](class_itemlist.md#class_ItemList_method_remove_item)

Removes the item specified by `idx` index from the list.

---

<span id="class_ItemList_method_select"></span>

void **select** ( idx: [int](class_int.md#class_int), single: [bool](class_bool.md#class_bool) = true ) [🔗](class_itemlist.md#class_ItemList_method_select)

Selects the item at the specified index.

 **Note:** This method does not trigger the item selection signal.

---

<span id="class_ItemList_method_set_item_auto_translate_mode"></span>

void **set_item_auto_translate_mode** ( idx: [int](class_int.md#class_int), mode: [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_auto_translate_mode)

Sets the auto translate mode of the item associated with the specified index.

Items use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT) by default, which uses the same auto translate mode as the **ItemList** itself.

---

<span id="class_ItemList_method_set_item_custom_bg_color"></span>

void **set_item_custom_bg_color** ( idx: [int](class_int.md#class_int), custom_bg_color: [Color](class_color.md#class_Color) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_custom_bg_color)

Sets the background color of the item specified by `idx` index to the specified [Color](class_color.md#class_Color).

---

<span id="class_ItemList_method_set_item_custom_fg_color"></span>

void **set_item_custom_fg_color** ( idx: [int](class_int.md#class_int), custom_fg_color: [Color](class_color.md#class_Color) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_custom_fg_color)

Sets the foreground color of the item specified by `idx` index to the specified [Color](class_color.md#class_Color).

---

<span id="class_ItemList_method_set_item_disabled"></span>

void **set_item_disabled** ( idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_disabled)

Disables (or enables) the item at the specified index.

Disabled items cannot be selected and do not trigger activation signals (when double-clicking or pressing :kbd:`Enter`).

---

<span id="class_ItemList_method_set_item_icon"></span>

void **set_item_icon** ( idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_icon)

Sets (or replaces) the icon's [Texture2D](class_texture2d.md#class_Texture2D) associated with the specified index.

---

<span id="class_ItemList_method_set_item_icon_modulate"></span>

void **set_item_icon_modulate** ( idx: [int](class_int.md#class_int), modulate: [Color](class_color.md#class_Color) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_icon_modulate)

Sets a modulating [Color](class_color.md#class_Color) of the item associated with the specified index.

---

<span id="class_ItemList_method_set_item_icon_region"></span>

void **set_item_icon_region** ( idx: [int](class_int.md#class_int), rect: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_icon_region)

Sets the region of item's icon used. The whole icon will be used if the region has no area.

---

<span id="class_ItemList_method_set_item_icon_transposed"></span>

void **set_item_icon_transposed** ( idx: [int](class_int.md#class_int), transposed: [bool](class_bool.md#class_bool) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_icon_transposed)

Sets whether the item icon will be drawn transposed.

---

<span id="class_ItemList_method_set_item_language"></span>

void **set_item_language** ( idx: [int](class_int.md#class_int), language: [String](class_string.md#class_String) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_language)

Sets the language code of the text for the item at the given index to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---

<span id="class_ItemList_method_set_item_metadata"></span>

void **set_item_metadata** ( idx: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_metadata)

Sets a value (of any type) to be stored with the item associated with the specified index.

---

<span id="class_ItemList_method_set_item_selectable"></span>

void **set_item_selectable** ( idx: [int](class_int.md#class_int), selectable: [bool](class_bool.md#class_bool) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_selectable)

Allows or disallows selection of the item associated with the specified index.

---

<span id="class_ItemList_method_set_item_text"></span>

void **set_item_text** ( idx: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_text)

Sets text of the item associated with the specified index.

---

<span id="class_ItemList_method_set_item_text_direction"></span>

void **set_item_text_direction** ( idx: [int](class_int.md#class_int), direction: [TextDirection](class_control.md#enum_Control_TextDirection) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_text_direction)

Sets item's text base writing direction.

---

<span id="class_ItemList_method_set_item_tooltip"></span>

void **set_item_tooltip** ( idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_tooltip)

Sets the tooltip hint for the item associated with the specified index.

---

<span id="class_ItemList_method_set_item_tooltip_enabled"></span>

void **set_item_tooltip_enabled** ( idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_itemlist.md#class_ItemList_method_set_item_tooltip_enabled)

Sets whether the tooltip hint is enabled for specified item index.

---

<span id="class_ItemList_method_sort_items_by_text"></span>

void **sort_items_by_text** ( ) [🔗](class_itemlist.md#class_ItemList_method_sort_items_by_text)

Sorts items in the list by their text.

---

### Theme Property Descriptions

<span id="class_ItemList_theme_color_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(0.65, 0.65, 0.65, 1)` [🔗](class_itemlist.md#class_ItemList_theme_color_font_color)

Default text [Color](class_color.md#class_Color) of the item.

---

<span id="class_ItemList_theme_color_font_hovered_color"></span>

[Color](class_color.md#class_Color) **font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)` [🔗](class_itemlist.md#class_ItemList_theme_color_font_hovered_color)

Text [Color](class_color.md#class_Color) used when the item is hovered and not selected yet.

---

<span id="class_ItemList_theme_color_font_hovered_selected_color"></span>

[Color](class_color.md#class_Color) **font_hovered_selected_color** = `Color(1, 1, 1, 1)` [🔗](class_itemlist.md#class_ItemList_theme_color_font_hovered_selected_color)

Text [Color](class_color.md#class_Color) used when the item is hovered and selected.

---

<span id="class_ItemList_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_itemlist.md#class_ItemList_theme_color_font_outline_color)

The tint of text outline of the item.

---

<span id="class_ItemList_theme_color_font_selected_color"></span>

[Color](class_color.md#class_Color) **font_selected_color** = `Color(1, 1, 1, 1)` [🔗](class_itemlist.md#class_ItemList_theme_color_font_selected_color)

Text [Color](class_color.md#class_Color) used when the item is selected, but not hovered.

---

<span id="class_ItemList_theme_color_guide_color"></span>

[Color](class_color.md#class_Color) **guide_color** = `Color(0.7, 0.7, 0.7, 0.25)` [🔗](class_itemlist.md#class_ItemList_theme_color_guide_color)

[Color](class_color.md#class_Color) of the guideline. The guideline is a line drawn between each row of items.

---

<span id="class_ItemList_theme_color_scroll_hint_color"></span>

[Color](class_color.md#class_Color) **scroll_hint_color** = `Color(0, 0, 0, 1)` [🔗](class_itemlist.md#class_ItemList_theme_color_scroll_hint_color)

[Color](class_color.md#class_Color) used to modulate the [scroll_hint](class_itemlist.md#class_ItemList_theme_icon_scroll_hint) texture.

---

<span id="class_ItemList_theme_constant_h_separation"></span>

[int](class_int.md#class_int) **h_separation** = `4` [🔗](class_itemlist.md#class_ItemList_theme_constant_h_separation)

The horizontal spacing between items.

---

<span id="class_ItemList_theme_constant_icon_margin"></span>

[int](class_int.md#class_int) **icon_margin** = `4` [🔗](class_itemlist.md#class_ItemList_theme_constant_icon_margin)

The spacing between item's icon and text.

---

<span id="class_ItemList_theme_constant_line_separation"></span>

[int](class_int.md#class_int) **line_separation** = `2` [🔗](class_itemlist.md#class_ItemList_theme_constant_line_separation)

The vertical spacing between each line of text.

---

<span id="class_ItemList_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_itemlist.md#class_ItemList_theme_constant_outline_size)

The size of the item text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_itemlist.md#class_ItemList_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_ItemList_theme_constant_v_separation"></span>

[int](class_int.md#class_int) **v_separation** = `4` [🔗](class_itemlist.md#class_ItemList_theme_constant_v_separation)

The vertical spacing between items.

---

<span id="class_ItemList_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_itemlist.md#class_ItemList_theme_font_font)

[Font](class_font.md#class_Font) of the item's text.

---

<span id="class_ItemList_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_itemlist.md#class_ItemList_theme_font_size_font_size)

Font size of the item's text.

---

<span id="class_ItemList_theme_icon_scroll_hint"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **scroll_hint** [🔗](class_itemlist.md#class_ItemList_theme_icon_scroll_hint)

The indicator that will be shown when the content can still be scrolled. See [scroll_hint_mode](class_itemlist.md#class_ItemList_property_scroll_hint_mode).

---

<span id="class_ItemList_theme_style_cursor"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **cursor** [🔗](class_itemlist.md#class_ItemList_theme_style_cursor)

[StyleBox](class_stylebox.md#class_StyleBox) used for the cursor, when the **ItemList** is being focused.

---

<span id="class_ItemList_theme_style_cursor_unfocused"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **cursor_unfocused** [🔗](class_itemlist.md#class_ItemList_theme_style_cursor_unfocused)

[StyleBox](class_stylebox.md#class_StyleBox) used for the cursor, when the **ItemList** is not being focused.

---

<span id="class_ItemList_theme_style_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **focus** [🔗](class_itemlist.md#class_ItemList_theme_style_focus)

The focused style for the **ItemList**, drawn on top of everything.

---

<span id="class_ItemList_theme_style_hovered"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hovered** [🔗](class_itemlist.md#class_ItemList_theme_style_hovered)

[StyleBox](class_stylebox.md#class_StyleBox) for the hovered, but not selected items.

---

<span id="class_ItemList_theme_style_hovered_selected"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hovered_selected** [🔗](class_itemlist.md#class_ItemList_theme_style_hovered_selected)

[StyleBox](class_stylebox.md#class_StyleBox) for the hovered and selected items, used when the **ItemList** is not being focused.

---

<span id="class_ItemList_theme_style_hovered_selected_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **hovered_selected_focus** [🔗](class_itemlist.md#class_ItemList_theme_style_hovered_selected_focus)

[StyleBox](class_stylebox.md#class_StyleBox) for the hovered and selected items, used when the **ItemList** is being focused.

---

<span id="class_ItemList_theme_style_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **panel** [🔗](class_itemlist.md#class_ItemList_theme_style_panel)

The background style for the **ItemList**.

---

<span id="class_ItemList_theme_style_selected"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **selected** [🔗](class_itemlist.md#class_ItemList_theme_style_selected)

[StyleBox](class_stylebox.md#class_StyleBox) for the selected items, used when the **ItemList** is not being focused.

---

<span id="class_ItemList_theme_style_selected_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **selected_focus** [🔗](class_itemlist.md#class_ItemList_theme_style_selected_focus)

[StyleBox](class_stylebox.md#class_StyleBox) for the selected items, used when the **ItemList** is being focused.
