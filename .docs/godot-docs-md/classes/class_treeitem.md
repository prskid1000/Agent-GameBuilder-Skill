<span id="class_TreeItem"></span>

## TreeItem

**Inherits:** [Object](class_object.md#class_Object)

An internal control for a single item inside [Tree](class_tree.md#class_Tree).

### Description

A single item of a [Tree](class_tree.md#class_Tree) control. It can contain other **TreeItem** s as children, which allows it to create a hierarchy. It can also contain text and buttons. **TreeItem** is not a [Node](class_node.md#class_Node), it is internal to the [Tree](class_tree.md#class_Tree).

To create a **TreeItem**, use [Tree.create_item()](class_tree.md#class_Tree_method_create_item) or [create_child()](class_treeitem.md#class_TreeItem_method_create_child). To remove a **TreeItem**, use [Object.free()](class_object.md#class_Object_method_free).

 **Note:** The ID values used for buttons are 32-bit, unlike [int](class_int.md#class_int) which is always 64-bit. They go from `-2147483648` to `2147483647`.

### Properties


| [bool](class_bool.md#class_bool) | [collapsed](class_treeitem.md#class_TreeItem_property_collapsed) |
| --- | --- |
| [int](class_int.md#class_int) | [custom_minimum_height](class_treeitem.md#class_TreeItem_property_custom_minimum_height) |
| [bool](class_bool.md#class_bool) | [disable_folding](class_treeitem.md#class_TreeItem_property_disable_folding) |
| [bool](class_bool.md#class_bool) | [visible](class_treeitem.md#class_TreeItem_property_visible) |

### Methods


| void | [add_button](class_treeitem.md#class_TreeItem_method_add_button) ( column: [int](class_int.md#class_int), button: [Texture2D](class_texture2d.md#class_Texture2D), id: [int](class_int.md#class_int) = -1, disabled: [bool](class_bool.md#class_bool) = false, tooltip_text: [String](class_string.md#class_String) = "", description: [String](class_string.md#class_String) = "" ) |
| --- | --- |
| void | [add_child](class_treeitem.md#class_TreeItem_method_add_child) ( child: [TreeItem](class_treeitem.md#class_TreeItem) ) |
| void | [call_recursive](class_treeitem.md#class_TreeItem_method_call_recursive) ( method: [StringName](class_stringname.md#class_StringName), ... ) vararg |
| void | [clear_buttons](class_treeitem.md#class_TreeItem_method_clear_buttons) ( ) |
| void | [clear_custom_bg_color](class_treeitem.md#class_TreeItem_method_clear_custom_bg_color) ( column: [int](class_int.md#class_int) ) |
| void | [clear_custom_color](class_treeitem.md#class_TreeItem_method_clear_custom_color) ( column: [int](class_int.md#class_int) ) |
| [TreeItem](class_treeitem.md#class_TreeItem) | [create_child](class_treeitem.md#class_TreeItem_method_create_child) ( index: [int](class_int.md#class_int) = -1 ) |
| void | [deselect](class_treeitem.md#class_TreeItem_method_deselect) ( column: [int](class_int.md#class_int) ) |
| void | [erase_button](class_treeitem.md#class_TreeItem_method_erase_button) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) |
| [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) | [get_auto_translate_mode](class_treeitem.md#class_TreeItem_method_get_auto_translate_mode) ( column: [int](class_int.md#class_int) ) const |
| [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) | [get_autowrap_mode](class_treeitem.md#class_TreeItem_method_get_autowrap_mode) ( column: [int](class_int.md#class_int) ) const |
| bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] | [get_autowrap_trim_flags](class_treeitem.md#class_TreeItem_method_get_autowrap_trim_flags) ( column: [int](class_int.md#class_int) ) | const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_button](class_treeitem.md#class_TreeItem_method_get_button) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_button_by_id](class_treeitem.md#class_TreeItem_method_get_button_by_id) ( column: [int](class_int.md#class_int), id: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_button_color](class_treeitem.md#class_TreeItem_method_get_button_color) ( column: [int](class_int.md#class_int), id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_button_count](class_treeitem.md#class_TreeItem_method_get_button_count) ( column: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_button_id](class_treeitem.md#class_TreeItem_method_get_button_id) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_button_tooltip_text](class_treeitem.md#class_TreeItem_method_get_button_tooltip_text) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) const |
| [TreeCellMode](class_treeitem.md#enum_TreeItem_TreeCellMode) | [get_cell_mode](class_treeitem.md#class_TreeItem_method_get_cell_mode) ( column: [int](class_int.md#class_int) ) const |
| [TreeItem](class_treeitem.md#class_TreeItem) | [get_child](class_treeitem.md#class_TreeItem_method_get_child) ( index: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_child_count](class_treeitem.md#class_TreeItem_method_get_child_count) ( ) |
| [Array](class_array.md#class_Array)\[[TreeItem](class_treeitem.md#class_TreeItem)\] | [get_children](class_treeitem.md#class_TreeItem_method_get_children) ( ) |
| [Color](class_color.md#class_Color) | [get_custom_bg_color](class_treeitem.md#class_TreeItem_method_get_custom_bg_color) ( column: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_custom_color](class_treeitem.md#class_TreeItem_method_get_custom_color) ( column: [int](class_int.md#class_int) ) const |
| [Callable](class_callable.md#class_Callable) | [get_custom_draw_callback](class_treeitem.md#class_TreeItem_method_get_custom_draw_callback) ( column: [int](class_int.md#class_int) ) const |
| [Font](class_font.md#class_Font) | [get_custom_font](class_treeitem.md#class_TreeItem_method_get_custom_font) ( column: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_custom_font_size](class_treeitem.md#class_TreeItem_method_get_custom_font_size) ( column: [int](class_int.md#class_int) ) const |
| [StyleBox](class_stylebox.md#class_StyleBox) | [get_custom_stylebox](class_treeitem.md#class_TreeItem_method_get_custom_stylebox) ( column: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_description](class_treeitem.md#class_TreeItem_method_get_description) ( column: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_expand_right](class_treeitem.md#class_TreeItem_method_get_expand_right) ( column: [int](class_int.md#class_int) ) const |
| [TreeItem](class_treeitem.md#class_TreeItem) | [get_first_child](class_treeitem.md#class_TreeItem_method_get_first_child) ( ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_icon](class_treeitem.md#class_TreeItem_method_get_icon) ( column: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_icon_max_width](class_treeitem.md#class_TreeItem_method_get_icon_max_width) ( column: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_icon_modulate](class_treeitem.md#class_TreeItem_method_get_icon_modulate) ( column: [int](class_int.md#class_int) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_icon_overlay](class_treeitem.md#class_TreeItem_method_get_icon_overlay) ( column: [int](class_int.md#class_int) ) const |
| [Rect2](class_rect2.md#class_Rect2) | [get_icon_region](class_treeitem.md#class_TreeItem_method_get_icon_region) ( column: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_index](class_treeitem.md#class_TreeItem_method_get_index) ( ) |
| [String](class_string.md#class_String) | [get_language](class_treeitem.md#class_TreeItem_method_get_language) ( column: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_metadata](class_treeitem.md#class_TreeItem_method_get_metadata) ( column: [int](class_int.md#class_int) ) const |
| [TreeItem](class_treeitem.md#class_TreeItem) | [get_next](class_treeitem.md#class_TreeItem_method_get_next) ( ) const |
| [TreeItem](class_treeitem.md#class_TreeItem) | [get_next_in_tree](class_treeitem.md#class_TreeItem_method_get_next_in_tree) ( wrap: [bool](class_bool.md#class_bool) = false ) |
| [TreeItem](class_treeitem.md#class_TreeItem) | [get_next_visible](class_treeitem.md#class_TreeItem_method_get_next_visible) ( wrap: [bool](class_bool.md#class_bool) = false ) |
| [TreeItem](class_treeitem.md#class_TreeItem) | [get_parent](class_treeitem.md#class_TreeItem_method_get_parent) ( ) const |
| [TreeItem](class_treeitem.md#class_TreeItem) | [get_prev](class_treeitem.md#class_TreeItem_method_get_prev) ( ) |
| [TreeItem](class_treeitem.md#class_TreeItem) | [get_prev_in_tree](class_treeitem.md#class_TreeItem_method_get_prev_in_tree) ( wrap: [bool](class_bool.md#class_bool) = false ) |
| [TreeItem](class_treeitem.md#class_TreeItem) | [get_prev_visible](class_treeitem.md#class_TreeItem_method_get_prev_visible) ( wrap: [bool](class_bool.md#class_bool) = false ) |
| [float](class_float.md#class_float) | [get_range](class_treeitem.md#class_TreeItem_method_get_range) ( column: [int](class_int.md#class_int) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_range_config](class_treeitem.md#class_TreeItem_method_get_range_config) ( column: [int](class_int.md#class_int) ) |
| [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) | [get_structured_text_bidi_override](class_treeitem.md#class_TreeItem_method_get_structured_text_bidi_override) ( column: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array) | [get_structured_text_bidi_override_options](class_treeitem.md#class_TreeItem_method_get_structured_text_bidi_override_options) ( column: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_suffix](class_treeitem.md#class_TreeItem_method_get_suffix) ( column: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_text](class_treeitem.md#class_TreeItem_method_get_text) ( column: [int](class_int.md#class_int) ) const |
| HorizontalAlignment | [get_text_alignment](class_treeitem.md#class_TreeItem_method_get_text_alignment) ( column: [int](class_int.md#class_int) ) const |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [get_text_direction](class_treeitem.md#class_TreeItem_method_get_text_direction) ( column: [int](class_int.md#class_int) ) const |
| [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) | [get_text_overrun_behavior](class_treeitem.md#class_TreeItem_method_get_text_overrun_behavior) ( column: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_tooltip_text](class_treeitem.md#class_TreeItem_method_get_tooltip_text) ( column: [int](class_int.md#class_int) ) const |
| [Tree](class_tree.md#class_Tree) | [get_tree](class_treeitem.md#class_TreeItem_method_get_tree) ( ) const |
| [bool](class_bool.md#class_bool) | [is_any_collapsed](class_treeitem.md#class_TreeItem_method_is_any_collapsed) ( only_visible: [bool](class_bool.md#class_bool) = false ) |
| [bool](class_bool.md#class_bool) | [is_button_disabled](class_treeitem.md#class_TreeItem_method_is_button_disabled) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_checked](class_treeitem.md#class_TreeItem_method_is_checked) ( column: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_custom_set_as_button](class_treeitem.md#class_TreeItem_method_is_custom_set_as_button) ( column: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_edit_multiline](class_treeitem.md#class_TreeItem_method_is_edit_multiline) ( column: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_editable](class_treeitem.md#class_TreeItem_method_is_editable) ( column: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [is_indeterminate](class_treeitem.md#class_TreeItem_method_is_indeterminate) ( column: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_selectable](class_treeitem.md#class_TreeItem_method_is_selectable) ( column: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_selected](class_treeitem.md#class_TreeItem_method_is_selected) ( column: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [is_visible_in_tree](class_treeitem.md#class_TreeItem_method_is_visible_in_tree) ( ) const |
| void | [move_after](class_treeitem.md#class_TreeItem_method_move_after) ( item: [TreeItem](class_treeitem.md#class_TreeItem) ) |
| void | [move_before](class_treeitem.md#class_TreeItem_method_move_before) ( item: [TreeItem](class_treeitem.md#class_TreeItem) ) |
| void | [propagate_check](class_treeitem.md#class_TreeItem_method_propagate_check) ( column: [int](class_int.md#class_int), emit_signal: [bool](class_bool.md#class_bool) = true ) |
| void | [remove_child](class_treeitem.md#class_TreeItem_method_remove_child) ( child: [TreeItem](class_treeitem.md#class_TreeItem) ) |
| void | [select](class_treeitem.md#class_TreeItem_method_select) ( column: [int](class_int.md#class_int) ) |
| void | [set_auto_translate_mode](class_treeitem.md#class_TreeItem_method_set_auto_translate_mode) ( column: [int](class_int.md#class_int), mode: [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) ) |
| void | [set_autowrap_mode](class_treeitem.md#class_TreeItem_method_set_autowrap_mode) ( column: [int](class_int.md#class_int), autowrap_mode: [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) ) |
| void | [set_autowrap_trim_flags](class_treeitem.md#class_TreeItem_method_set_autowrap_trim_flags) ( column: [int](class_int.md#class_int), flags: | bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] ) |
| void | [set_button](class_treeitem.md#class_TreeItem_method_set_button) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), button: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_button_color](class_treeitem.md#class_TreeItem_method_set_button_color) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_button_description](class_treeitem.md#class_TreeItem_method_set_button_description) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), description: [String](class_string.md#class_String) ) |
| void | [set_button_disabled](class_treeitem.md#class_TreeItem_method_set_button_disabled) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) |
| void | [set_button_tooltip_text](class_treeitem.md#class_TreeItem_method_set_button_tooltip_text) ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) |
| void | [set_cell_mode](class_treeitem.md#class_TreeItem_method_set_cell_mode) ( column: [int](class_int.md#class_int), mode: [TreeCellMode](class_treeitem.md#enum_TreeItem_TreeCellMode) ) |
| void | [set_checked](class_treeitem.md#class_TreeItem_method_set_checked) ( column: [int](class_int.md#class_int), checked: [bool](class_bool.md#class_bool) ) |
| void | [set_collapsed_recursive](class_treeitem.md#class_TreeItem_method_set_collapsed_recursive) ( enable: [bool](class_bool.md#class_bool) ) |
| void | [set_custom_as_button](class_treeitem.md#class_TreeItem_method_set_custom_as_button) ( column: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_custom_bg_color](class_treeitem.md#class_TreeItem_method_set_custom_bg_color) ( column: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color), just_outline: [bool](class_bool.md#class_bool) = false ) |
| void | [set_custom_color](class_treeitem.md#class_TreeItem_method_set_custom_color) ( column: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_custom_draw](class_treeitem.md#class_TreeItem_method_set_custom_draw) ( column: [int](class_int.md#class_int), object: [Object](class_object.md#class_Object), callback: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_custom_draw_callback](class_treeitem.md#class_TreeItem_method_set_custom_draw_callback) ( column: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) |
| void | [set_custom_font](class_treeitem.md#class_TreeItem_method_set_custom_font) ( column: [int](class_int.md#class_int), font: [Font](class_font.md#class_Font) ) |
| void | [set_custom_font_size](class_treeitem.md#class_TreeItem_method_set_custom_font_size) ( column: [int](class_int.md#class_int), font_size: [int](class_int.md#class_int) ) |
| void | [set_custom_stylebox](class_treeitem.md#class_TreeItem_method_set_custom_stylebox) ( column: [int](class_int.md#class_int), stylebox: [StyleBox](class_stylebox.md#class_StyleBox) ) |
| void | [set_description](class_treeitem.md#class_TreeItem_method_set_description) ( column: [int](class_int.md#class_int), description: [String](class_string.md#class_String) ) |
| void | [set_edit_multiline](class_treeitem.md#class_TreeItem_method_set_edit_multiline) ( column: [int](class_int.md#class_int), multiline: [bool](class_bool.md#class_bool) ) |
| void | [set_editable](class_treeitem.md#class_TreeItem_method_set_editable) ( column: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_expand_right](class_treeitem.md#class_TreeItem_method_set_expand_right) ( column: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_icon](class_treeitem.md#class_TreeItem_method_set_icon) ( column: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_icon_max_width](class_treeitem.md#class_TreeItem_method_set_icon_max_width) ( column: [int](class_int.md#class_int), width: [int](class_int.md#class_int) ) |
| void | [set_icon_modulate](class_treeitem.md#class_TreeItem_method_set_icon_modulate) ( column: [int](class_int.md#class_int), modulate: [Color](class_color.md#class_Color) ) |
| void | [set_icon_overlay](class_treeitem.md#class_TreeItem_method_set_icon_overlay) ( column: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_icon_region](class_treeitem.md#class_TreeItem_method_set_icon_region) ( column: [int](class_int.md#class_int), region: [Rect2](class_rect2.md#class_Rect2) ) |
| void | [set_indeterminate](class_treeitem.md#class_TreeItem_method_set_indeterminate) ( column: [int](class_int.md#class_int), indeterminate: [bool](class_bool.md#class_bool) ) |
| void | [set_language](class_treeitem.md#class_TreeItem_method_set_language) ( column: [int](class_int.md#class_int), language: [String](class_string.md#class_String) ) |
| void | [set_metadata](class_treeitem.md#class_TreeItem_method_set_metadata) ( column: [int](class_int.md#class_int), meta: [Variant](class_variant.md#class_Variant) ) |
| void | [set_range](class_treeitem.md#class_TreeItem_method_set_range) ( column: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) |
| void | [set_range_config](class_treeitem.md#class_TreeItem_method_set_range_config) ( column: [int](class_int.md#class_int), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float), step: [float](class_float.md#class_float), expr: [bool](class_bool.md#class_bool) = false ) |
| void | [set_selectable](class_treeitem.md#class_TreeItem_method_set_selectable) ( column: [int](class_int.md#class_int), selectable: [bool](class_bool.md#class_bool) ) |
| void | [set_structured_text_bidi_override](class_treeitem.md#class_TreeItem_method_set_structured_text_bidi_override) ( column: [int](class_int.md#class_int), parser: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) ) |
| void | [set_structured_text_bidi_override_options](class_treeitem.md#class_TreeItem_method_set_structured_text_bidi_override_options) ( column: [int](class_int.md#class_int), args: [Array](class_array.md#class_Array) ) |
| void | [set_suffix](class_treeitem.md#class_TreeItem_method_set_suffix) ( column: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) |
| void | [set_text](class_treeitem.md#class_TreeItem_method_set_text) ( column: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) |
| void | [set_text_alignment](class_treeitem.md#class_TreeItem_method_set_text_alignment) ( column: [int](class_int.md#class_int), text_alignment: HorizontalAlignment ) |
| void | [set_text_direction](class_treeitem.md#class_TreeItem_method_set_text_direction) ( column: [int](class_int.md#class_int), direction: [TextDirection](class_control.md#enum_Control_TextDirection) ) |
| void | [set_text_overrun_behavior](class_treeitem.md#class_TreeItem_method_set_text_overrun_behavior) ( column: [int](class_int.md#class_int), overrun_behavior: [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) ) |
| void | [set_tooltip_text](class_treeitem.md#class_TreeItem_method_set_tooltip_text) ( column: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) |
| void | [uncollapse_tree](class_treeitem.md#class_TreeItem_method_uncollapse_tree) ( ) |

---

### Enumerations

<span id="enum_TreeItem_TreeCellMode"></span>

enum **TreeCellMode**: [🔗](class_treeitem.md#enum_TreeItem_TreeCellMode)

<span id="class_TreeItem_constant_CELL_MODE_STRING"></span>

[TreeCellMode](class_treeitem.md#enum_TreeItem_TreeCellMode) **CELL_MODE_STRING** = `0`

Cell shows a string label, optionally with an icon. When editable, the text can be edited using a [LineEdit](class_lineedit.md#class_LineEdit), or a [TextEdit](class_textedit.md#class_TextEdit) popup if [set_edit_multiline()](class_treeitem.md#class_TreeItem_method_set_edit_multiline) is used.

<span id="class_TreeItem_constant_CELL_MODE_CHECK"></span>

[TreeCellMode](class_treeitem.md#enum_TreeItem_TreeCellMode) **CELL_MODE_CHECK** = `1`

Cell shows a checkbox, optionally with text and an icon. The checkbox can be pressed, released, or indeterminate (via [set_indeterminate()](class_treeitem.md#class_TreeItem_method_set_indeterminate)). The checkbox can't be clicked unless the cell is editable.

<span id="class_TreeItem_constant_CELL_MODE_RANGE"></span>

[TreeCellMode](class_treeitem.md#enum_TreeItem_TreeCellMode) **CELL_MODE_RANGE** = `2`

Cell shows a numeric range. When editable, it can be edited using a range slider. Use [set_range()](class_treeitem.md#class_TreeItem_method_set_range) to set the value and [set_range_config()](class_treeitem.md#class_TreeItem_method_set_range_config) to configure the range.

This cell can also be used in a text dropdown mode when you assign a text with [set_text()](class_treeitem.md#class_TreeItem_method_set_text). Separate options with a comma, e.g. `"Option1,Option2,Option3"`.

<span id="class_TreeItem_constant_CELL_MODE_ICON"></span>

[TreeCellMode](class_treeitem.md#enum_TreeItem_TreeCellMode) **CELL_MODE_ICON** = `3`

Cell shows an icon. It can't be edited nor display text. The icon is always centered within the cell.

<span id="class_TreeItem_constant_CELL_MODE_CUSTOM"></span>

[TreeCellMode](class_treeitem.md#enum_TreeItem_TreeCellMode) **CELL_MODE_CUSTOM** = `4`

Cell shows as a clickable button. It will display an arrow similar to [OptionButton](class_optionbutton.md#class_OptionButton), but doesn't feature a dropdown (for that you can use [CELL_MODE_RANGE](class_treeitem.md#class_TreeItem_constant_CELL_MODE_RANGE)). Clicking the button emits the [Tree.item_edited](class_tree.md#class_Tree_signal_item_edited) signal. The button is flat by default, you can use [set_custom_as_button()](class_treeitem.md#class_TreeItem_method_set_custom_as_button) to display it with a [StyleBox](class_stylebox.md#class_StyleBox).

This mode also supports custom drawing using [set_custom_draw_callback()](class_treeitem.md#class_TreeItem_method_set_custom_draw_callback).

---

### Property Descriptions

<span id="class_TreeItem_property_collapsed"></span>

[bool](class_bool.md#class_bool) **collapsed** [🔗](class_treeitem.md#class_TreeItem_property_collapsed)

- void **set_collapsed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collapsed** ( )

If `true`, the TreeItem is collapsed.

---

<span id="class_TreeItem_property_custom_minimum_height"></span>

[int](class_int.md#class_int) **custom_minimum_height** [🔗](class_treeitem.md#class_TreeItem_property_custom_minimum_height)

- void **set_custom_minimum_height** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_custom_minimum_height** ( )

The custom minimum height.

---

<span id="class_TreeItem_property_disable_folding"></span>

[bool](class_bool.md#class_bool) **disable_folding** [🔗](class_treeitem.md#class_TreeItem_property_disable_folding)

- void **set_disable_folding** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_folding_disabled** ( )

If `true`, folding is disabled for this TreeItem.

---

<span id="class_TreeItem_property_visible"></span>

[bool](class_bool.md#class_bool) **visible** [🔗](class_treeitem.md#class_TreeItem_property_visible)

- void **set_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_visible** ( )

If `true`, the **TreeItem** is visible (default).

Note that if a **TreeItem** is set to not be visible, none of its children will be visible either.

---

### Method Descriptions

<span id="class_TreeItem_method_add_button"></span>

void **add_button** ( column: [int](class_int.md#class_int), button: [Texture2D](class_texture2d.md#class_Texture2D), id: [int](class_int.md#class_int) = -1, disabled: [bool](class_bool.md#class_bool) = false, tooltip_text: [String](class_string.md#class_String) = "", description: [String](class_string.md#class_String) = "" ) [🔗](class_treeitem.md#class_TreeItem_method_add_button)

Adds a button with [Texture2D](class_texture2d.md#class_Texture2D) `button` to the end of the cell at column `column`. The `id` is used to identify the button in the according [Tree.button_clicked](class_tree.md#class_Tree_signal_button_clicked) signal and can be different from the buttons index. If not specified, the next available index is used, which may be retrieved by calling [get_button_count()](class_treeitem.md#class_TreeItem_method_get_button_count) immediately before this method. Optionally, the button can be `disabled` and have a `tooltip_text`. `description` is used as the button description for assistive apps.

---

<span id="class_TreeItem_method_add_child"></span>

void **add_child** ( child: [TreeItem](class_treeitem.md#class_TreeItem) ) [🔗](class_treeitem.md#class_TreeItem_method_add_child)

Adds a previously unparented **TreeItem** as a direct child of this one. The `child` item must not be a part of any [Tree](class_tree.md#class_Tree) or parented to any **TreeItem**. See also [remove_child()](class_treeitem.md#class_TreeItem_method_remove_child).

---

<span id="class_TreeItem_method_call_recursive"></span>

void **call_recursive** ( method: [StringName](class_stringname.md#class_StringName), ... ) *vararg* [🔗](class_treeitem.md#class_TreeItem_method_call_recursive)

Calls the `method` on the actual TreeItem and its children recursively. Pass parameters as a comma separated list.

---

<span id="class_TreeItem_method_clear_buttons"></span>

void **clear_buttons** ( ) [🔗](class_treeitem.md#class_TreeItem_method_clear_buttons)

Removes all buttons from all columns of this item.

---

<span id="class_TreeItem_method_clear_custom_bg_color"></span>

void **clear_custom_bg_color** ( column: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_clear_custom_bg_color)

Resets the background color for the given column to default.

---

<span id="class_TreeItem_method_clear_custom_color"></span>

void **clear_custom_color** ( column: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_clear_custom_color)

Resets the color for the given column to default.

---

<span id="class_TreeItem_method_create_child"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **create_child** ( index: [int](class_int.md#class_int) = -1 ) [🔗](class_treeitem.md#class_TreeItem_method_create_child)

Creates an item and adds it as a child.

The new item will be inserted as position `index` (the default value `-1` means the last position), or it will be the last child if `index` is higher than the child count.

---

<span id="class_TreeItem_method_deselect"></span>

void **deselect** ( column: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_deselect)

Deselects the given column.

---

<span id="class_TreeItem_method_erase_button"></span>

void **erase_button** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_erase_button)

Removes the button at index `button_index` in column `column`.

---

<span id="class_TreeItem_method_get_auto_translate_mode"></span>

[AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) **get_auto_translate_mode** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_auto_translate_mode)

Returns the column's auto translate mode.

---

<span id="class_TreeItem_method_get_autowrap_mode"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **get_autowrap_mode** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_autowrap_mode)

Returns the text autowrap mode in the given `column`. By default it is [TextServer.AUTOWRAP_OFF](class_textserver.md#class_TextServer_constant_AUTOWRAP_OFF).

---

<span id="class_TreeItem_method_get_autowrap_trim_flags"></span>

*BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **get_autowrap_trim_flags** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_autowrap_trim_flags)

Returns the autowrap trim flags for the given `column`. By default, both [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES) are enabled.

---

<span id="class_TreeItem_method_get_button"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_button** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_button)

Returns the [Texture2D](class_texture2d.md#class_Texture2D) of the button at index `button_index` in column `column`.

---

<span id="class_TreeItem_method_get_button_by_id"></span>

[int](class_int.md#class_int) **get_button_by_id** ( column: [int](class_int.md#class_int), id: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_button_by_id)

Returns the button index if there is a button with ID `id` in column `column`, otherwise returns -1.

---

<span id="class_TreeItem_method_get_button_color"></span>

[Color](class_color.md#class_Color) **get_button_color** ( column: [int](class_int.md#class_int), id: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_button_color)

Returns the color of the button with ID `id` in column `column`. If the specified button does not exist, returns [Color.BLACK](class_color.md#class_Color_constant_BLACK).

---

<span id="class_TreeItem_method_get_button_count"></span>

[int](class_int.md#class_int) **get_button_count** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_button_count)

Returns the number of buttons in column `column`.

---

<span id="class_TreeItem_method_get_button_id"></span>

[int](class_int.md#class_int) **get_button_id** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_button_id)

Returns the ID for the button at index `button_index` in column `column`.

---

<span id="class_TreeItem_method_get_button_tooltip_text"></span>

[String](class_string.md#class_String) **get_button_tooltip_text** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_button_tooltip_text)

Returns the tooltip text for the button at index `button_index` in column `column`.

---

<span id="class_TreeItem_method_get_cell_mode"></span>

[TreeCellMode](class_treeitem.md#enum_TreeItem_TreeCellMode) **get_cell_mode** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_cell_mode)

Returns the column's cell mode.

---

<span id="class_TreeItem_method_get_child"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **get_child** ( index: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_get_child)

Returns a child item by its `index` (see [get_child_count()](class_treeitem.md#class_TreeItem_method_get_child_count)). This method is often used for iterating all children of an item.

Negative indices access the children from the last one.

---

<span id="class_TreeItem_method_get_child_count"></span>

[int](class_int.md#class_int) **get_child_count** ( ) [🔗](class_treeitem.md#class_TreeItem_method_get_child_count)

Returns the number of child items.

---

<span id="class_TreeItem_method_get_children"></span>

[Array](class_array.md#class_Array)\[[TreeItem](class_treeitem.md#class_TreeItem)\] **get_children** ( ) [🔗](class_treeitem.md#class_TreeItem_method_get_children)

Returns an array of references to the item's children.

---

<span id="class_TreeItem_method_get_custom_bg_color"></span>

[Color](class_color.md#class_Color) **get_custom_bg_color** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_custom_bg_color)

Returns the custom background color of column `column`.

---

<span id="class_TreeItem_method_get_custom_color"></span>

[Color](class_color.md#class_Color) **get_custom_color** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_custom_color)

Returns the custom color of column `column`.

---

<span id="class_TreeItem_method_get_custom_draw_callback"></span>

[Callable](class_callable.md#class_Callable) **get_custom_draw_callback** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_custom_draw_callback)

Returns the custom callback of column `column`.

---

<span id="class_TreeItem_method_get_custom_font"></span>

[Font](class_font.md#class_Font) **get_custom_font** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_custom_font)

Returns custom font used to draw text in the column `column`.

---

<span id="class_TreeItem_method_get_custom_font_size"></span>

[int](class_int.md#class_int) **get_custom_font_size** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_custom_font_size)

Returns custom font size used to draw text in the column `column`.

---

<span id="class_TreeItem_method_get_custom_stylebox"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **get_custom_stylebox** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_custom_stylebox)

Returns the given column's custom [StyleBox](class_stylebox.md#class_StyleBox) used to draw the background.

---

<span id="class_TreeItem_method_get_description"></span>

[String](class_string.md#class_String) **get_description** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_description)

Returns the given column's description for assistive apps.

---

<span id="class_TreeItem_method_get_expand_right"></span>

[bool](class_bool.md#class_bool) **get_expand_right** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_expand_right)

Returns `true` if `expand_right` is set.

---

<span id="class_TreeItem_method_get_first_child"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **get_first_child** ( ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_first_child)

Returns the TreeItem's first child.

---

<span id="class_TreeItem_method_get_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_icon** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_icon)

Returns the given column's icon [Texture2D](class_texture2d.md#class_Texture2D). Error if no icon is set.

---

<span id="class_TreeItem_method_get_icon_max_width"></span>

[int](class_int.md#class_int) **get_icon_max_width** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_icon_max_width)

Returns the maximum allowed width of the icon in the given `column`.

---

<span id="class_TreeItem_method_get_icon_modulate"></span>

[Color](class_color.md#class_Color) **get_icon_modulate** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_icon_modulate)

Returns the [Color](class_color.md#class_Color) modulating the column's icon.

---

<span id="class_TreeItem_method_get_icon_overlay"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_icon_overlay** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_icon_overlay)

Returns the given column's icon overlay [Texture2D](class_texture2d.md#class_Texture2D).

---

<span id="class_TreeItem_method_get_icon_region"></span>

[Rect2](class_rect2.md#class_Rect2) **get_icon_region** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_icon_region)

Returns the icon [Texture2D](class_texture2d.md#class_Texture2D) region as [Rect2](class_rect2.md#class_Rect2).

---

<span id="class_TreeItem_method_get_index"></span>

[int](class_int.md#class_int) **get_index** ( ) [🔗](class_treeitem.md#class_TreeItem_method_get_index)

Returns the node's order in the tree. For example, if called on the first child item the position is `0`.

---

<span id="class_TreeItem_method_get_language"></span>

[String](class_string.md#class_String) **get_language** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_language)

Returns item's text language code.

---

<span id="class_TreeItem_method_get_metadata"></span>

[Variant](class_variant.md#class_Variant) **get_metadata** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_metadata)

Returns the metadata value that was set for the given column using [set_metadata()](class_treeitem.md#class_TreeItem_method_set_metadata).

---

<span id="class_TreeItem_method_get_next"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **get_next** ( ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_next)

Returns the next sibling TreeItem in the tree or a `null` object if there is none.

---

<span id="class_TreeItem_method_get_next_in_tree"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **get_next_in_tree** ( wrap: [bool](class_bool.md#class_bool) = false ) [🔗](class_treeitem.md#class_TreeItem_method_get_next_in_tree)

Returns the next TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the first element in the tree when called on the last element, otherwise it returns `null`.

---

<span id="class_TreeItem_method_get_next_visible"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **get_next_visible** ( wrap: [bool](class_bool.md#class_bool) = false ) [🔗](class_treeitem.md#class_TreeItem_method_get_next_visible)

Returns the next visible TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the first visible element in the tree when called on the last visible element, otherwise it returns `null`.

---

<span id="class_TreeItem_method_get_parent"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **get_parent** ( ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_parent)

Returns the parent TreeItem or a `null` object if there is none.

---

<span id="class_TreeItem_method_get_prev"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **get_prev** ( ) [🔗](class_treeitem.md#class_TreeItem_method_get_prev)

Returns the previous sibling TreeItem in the tree or a `null` object if there is none.

---

<span id="class_TreeItem_method_get_prev_in_tree"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **get_prev_in_tree** ( wrap: [bool](class_bool.md#class_bool) = false ) [🔗](class_treeitem.md#class_TreeItem_method_get_prev_in_tree)

Returns the previous TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the last element in the tree when called on the first visible element, otherwise it returns `null`.

---

<span id="class_TreeItem_method_get_prev_visible"></span>

[TreeItem](class_treeitem.md#class_TreeItem) **get_prev_visible** ( wrap: [bool](class_bool.md#class_bool) = false ) [🔗](class_treeitem.md#class_TreeItem_method_get_prev_visible)

Returns the previous visible sibling TreeItem in the tree (in the context of a depth-first search) or a `null` object if there is none.

If `wrap` is enabled, the method will wrap around to the last visible element in the tree when called on the first visible element, otherwise it returns `null`.

---

<span id="class_TreeItem_method_get_range"></span>

[float](class_float.md#class_float) **get_range** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_range)

Returns the value of a [CELL_MODE_RANGE](class_treeitem.md#class_TreeItem_constant_CELL_MODE_RANGE) column.

---

<span id="class_TreeItem_method_get_range_config"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_range_config** ( column: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_get_range_config)

Returns a dictionary containing the range parameters for a given column. The keys are "min", "max", "step", and "expr".

---

<span id="class_TreeItem_method_get_structured_text_bidi_override"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **get_structured_text_bidi_override** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_structured_text_bidi_override)

Returns the BiDi algorithm override set for this cell.

---

<span id="class_TreeItem_method_get_structured_text_bidi_override_options"></span>

[Array](class_array.md#class_Array) **get_structured_text_bidi_override_options** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_structured_text_bidi_override_options)

Returns the additional BiDi options set for this cell.

---

<span id="class_TreeItem_method_get_suffix"></span>

[String](class_string.md#class_String) **get_suffix** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_suffix)

Gets the suffix string shown after the column value.

---

<span id="class_TreeItem_method_get_text"></span>

[String](class_string.md#class_String) **get_text** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_text)

Returns the given column's text.

---

<span id="class_TreeItem_method_get_text_alignment"></span>

HorizontalAlignment **get_text_alignment** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_text_alignment)

Returns the given column's text alignment.

---

<span id="class_TreeItem_method_get_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **get_text_direction** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_text_direction)

Returns item's text base writing direction.

---

<span id="class_TreeItem_method_get_text_overrun_behavior"></span>

[OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) **get_text_overrun_behavior** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_text_overrun_behavior)

Returns the clipping behavior when the text exceeds the item's bounding rectangle in the given `column`. By default it is [TextServer.OVERRUN_TRIM_ELLIPSIS](class_textserver.md#class_TextServer_constant_OVERRUN_TRIM_ELLIPSIS).

---

<span id="class_TreeItem_method_get_tooltip_text"></span>

[String](class_string.md#class_String) **get_tooltip_text** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_tooltip_text)

Returns the given column's tooltip text.

---

<span id="class_TreeItem_method_get_tree"></span>

[Tree](class_tree.md#class_Tree) **get_tree** ( ) *const* [🔗](class_treeitem.md#class_TreeItem_method_get_tree)

Returns the [Tree](class_tree.md#class_Tree) that owns this TreeItem.

---

<span id="class_TreeItem_method_is_any_collapsed"></span>

[bool](class_bool.md#class_bool) **is_any_collapsed** ( only_visible: [bool](class_bool.md#class_bool) = false ) [🔗](class_treeitem.md#class_TreeItem_method_is_any_collapsed)

Returns `true` if this **TreeItem**, or any of its descendants, is collapsed.

If `only_visible` is `true` it ignores non-visible **TreeItem** s.

---

<span id="class_TreeItem_method_is_button_disabled"></span>

[bool](class_bool.md#class_bool) **is_button_disabled** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_is_button_disabled)

Returns `true` if the button at index `button_index` for the given `column` is disabled.

---

<span id="class_TreeItem_method_is_checked"></span>

[bool](class_bool.md#class_bool) **is_checked** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_is_checked)

Returns `true` if the given `column` is checked.

---

<span id="class_TreeItem_method_is_custom_set_as_button"></span>

[bool](class_bool.md#class_bool) **is_custom_set_as_button** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_is_custom_set_as_button)

Returns `true` if the cell was made into a button with [set_custom_as_button()](class_treeitem.md#class_TreeItem_method_set_custom_as_button).

---

<span id="class_TreeItem_method_is_edit_multiline"></span>

[bool](class_bool.md#class_bool) **is_edit_multiline** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_is_edit_multiline)

Returns `true` if the given `column` is multiline editable.

---

<span id="class_TreeItem_method_is_editable"></span>

[bool](class_bool.md#class_bool) **is_editable** ( column: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_is_editable)

Returns `true` if the given `column` is editable.

---

<span id="class_TreeItem_method_is_indeterminate"></span>

[bool](class_bool.md#class_bool) **is_indeterminate** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_is_indeterminate)

Returns `true` if the given `column` is indeterminate.

---

<span id="class_TreeItem_method_is_selectable"></span>

[bool](class_bool.md#class_bool) **is_selectable** ( column: [int](class_int.md#class_int) ) *const* [🔗](class_treeitem.md#class_TreeItem_method_is_selectable)

Returns `true` if the given `column` is selectable.

---

<span id="class_TreeItem_method_is_selected"></span>

[bool](class_bool.md#class_bool) **is_selected** ( column: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_is_selected)

Returns `true` if the given `column` is selected.

---

<span id="class_TreeItem_method_is_visible_in_tree"></span>

[bool](class_bool.md#class_bool) **is_visible_in_tree** ( ) *const* [🔗](class_treeitem.md#class_TreeItem_method_is_visible_in_tree)

Returns `true` if [visible](class_treeitem.md#class_TreeItem_property_visible) is `true` and all its ancestors are also visible.

---

<span id="class_TreeItem_method_move_after"></span>

void **move_after** ( item: [TreeItem](class_treeitem.md#class_TreeItem) ) [🔗](class_treeitem.md#class_TreeItem_method_move_after)

Moves this TreeItem right after the given `item`.

 **Note:** You can't move to the root or move the root.

---

<span id="class_TreeItem_method_move_before"></span>

void **move_before** ( item: [TreeItem](class_treeitem.md#class_TreeItem) ) [🔗](class_treeitem.md#class_TreeItem_method_move_before)

Moves this TreeItem right before the given `item`.

 **Note:** You can't move to the root or move the root.

---

<span id="class_TreeItem_method_propagate_check"></span>

void **propagate_check** ( column: [int](class_int.md#class_int), emit_signal: [bool](class_bool.md#class_bool) = true ) [🔗](class_treeitem.md#class_TreeItem_method_propagate_check)

Propagates this item's checked status to its children and parents for the given `column`. It is possible to process the items affected by this method call by connecting to [Tree.check_propagated_to_item](class_tree.md#class_Tree_signal_check_propagated_to_item). The order that the items affected will be processed is as follows: the item invoking this method, children of that item, and finally parents of that item. If `emit_signal` is `false`, then [Tree.check_propagated_to_item](class_tree.md#class_Tree_signal_check_propagated_to_item) will not be emitted.

---

<span id="class_TreeItem_method_remove_child"></span>

void **remove_child** ( child: [TreeItem](class_treeitem.md#class_TreeItem) ) [🔗](class_treeitem.md#class_TreeItem_method_remove_child)

Removes the given child **TreeItem** and all its children from the [Tree](class_tree.md#class_Tree). Note that it doesn't free the item from memory, so it can be reused later (see [add_child()](class_treeitem.md#class_TreeItem_method_add_child)). To completely remove a **TreeItem** use [Object.free()](class_object.md#class_Object_method_free).

 **Note:** If you want to move a child from one [Tree](class_tree.md#class_Tree) to another, then instead of removing and adding it manually you can use [move_before()](class_treeitem.md#class_TreeItem_method_move_before) or [move_after()](class_treeitem.md#class_TreeItem_method_move_after).

---

<span id="class_TreeItem_method_select"></span>

void **select** ( column: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_select)

Selects the given `column`.

---

<span id="class_TreeItem_method_set_auto_translate_mode"></span>

void **set_auto_translate_mode** ( column: [int](class_int.md#class_int), mode: [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) ) [🔗](class_treeitem.md#class_TreeItem_method_set_auto_translate_mode)

Sets the given column's auto translate mode to `mode`.

All columns use [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT) by default, which uses the same auto translate mode as the [Tree](class_tree.md#class_Tree) itself.

---

<span id="class_TreeItem_method_set_autowrap_mode"></span>

void **set_autowrap_mode** ( column: [int](class_int.md#class_int), autowrap_mode: [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) ) [🔗](class_treeitem.md#class_TreeItem_method_set_autowrap_mode)

Sets the autowrap mode in the given `column`. If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class_TextServer_constant_AUTOWRAP_OFF), the text gets wrapped inside the cell's bounding rectangle.

---

<span id="class_TreeItem_method_set_autowrap_trim_flags"></span>

void **set_autowrap_trim_flags** ( column: [int](class_int.md#class_int), flags: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] ) [🔗](class_treeitem.md#class_TreeItem_method_set_autowrap_trim_flags)

Sets the autowrap trim flags for the given `column`. These flags control whether leading and trailing spaces are trimmed on wrapped lines. Set to `0` to disable all trimming.

---

<span id="class_TreeItem_method_set_button"></span>

void **set_button** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), button: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_treeitem.md#class_TreeItem_method_set_button)

Sets the given column's button [Texture2D](class_texture2d.md#class_Texture2D) at index `button_index` to `button`.

---

<span id="class_TreeItem_method_set_button_color"></span>

void **set_button_color** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_treeitem.md#class_TreeItem_method_set_button_color)

Sets the given column's button color at index `button_index` to `color`.

---

<span id="class_TreeItem_method_set_button_description"></span>

void **set_button_description** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), description: [String](class_string.md#class_String) ) [🔗](class_treeitem.md#class_TreeItem_method_set_button_description)

Sets the given column's button description at index `button_index` for assistive apps.

---

<span id="class_TreeItem_method_set_button_disabled"></span>

void **set_button_disabled** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) [🔗](class_treeitem.md#class_TreeItem_method_set_button_disabled)

If `true`, disables the button at index `button_index` in the given `column`.

---

<span id="class_TreeItem_method_set_button_tooltip_text"></span>

void **set_button_tooltip_text** ( column: [int](class_int.md#class_int), button_index: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) [🔗](class_treeitem.md#class_TreeItem_method_set_button_tooltip_text)

Sets the tooltip text for the button at index `button_index` in the given `column`.

---

<span id="class_TreeItem_method_set_cell_mode"></span>

void **set_cell_mode** ( column: [int](class_int.md#class_int), mode: [TreeCellMode](class_treeitem.md#enum_TreeItem_TreeCellMode) ) [🔗](class_treeitem.md#class_TreeItem_method_set_cell_mode)

Sets the given column's cell mode to `mode`. This determines how the cell is displayed and edited.

---

<span id="class_TreeItem_method_set_checked"></span>

void **set_checked** ( column: [int](class_int.md#class_int), checked: [bool](class_bool.md#class_bool) ) [🔗](class_treeitem.md#class_TreeItem_method_set_checked)

If `checked` is `true`, the given `column` is checked. Clears column's indeterminate status.

---

<span id="class_TreeItem_method_set_collapsed_recursive"></span>

void **set_collapsed_recursive** ( enable: [bool](class_bool.md#class_bool) ) [🔗](class_treeitem.md#class_TreeItem_method_set_collapsed_recursive)

Collapses or uncollapses this **TreeItem** and all the descendants of this item.

---

<span id="class_TreeItem_method_set_custom_as_button"></span>

void **set_custom_as_button** ( column: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_treeitem.md#class_TreeItem_method_set_custom_as_button)

Makes a cell with [CELL_MODE_CUSTOM](class_treeitem.md#class_TreeItem_constant_CELL_MODE_CUSTOM) display as a non-flat button with a [StyleBox](class_stylebox.md#class_StyleBox).

---

<span id="class_TreeItem_method_set_custom_bg_color"></span>

void **set_custom_bg_color** ( column: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color), just_outline: [bool](class_bool.md#class_bool) = false ) [🔗](class_treeitem.md#class_TreeItem_method_set_custom_bg_color)

Sets the given column's custom background color and whether to just use it as an outline.

 **Note:** If a custom [StyleBox](class_stylebox.md#class_StyleBox) is set, the background color will be drawn behind it.

---

<span id="class_TreeItem_method_set_custom_color"></span>

void **set_custom_color** ( column: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_treeitem.md#class_TreeItem_method_set_custom_color)

Sets the given column's custom color.

---

<span id="class_TreeItem_method_set_custom_draw"></span>

void **set_custom_draw** ( column: [int](class_int.md#class_int), object: [Object](class_object.md#class_Object), callback: [StringName](class_stringname.md#class_StringName) ) [🔗](class_treeitem.md#class_TreeItem_method_set_custom_draw)

**Deprecated:** Use [set_custom_draw_callback()](class_treeitem.md#class_TreeItem_method_set_custom_draw_callback) instead.

Sets the given column's custom draw callback to the `callback` method on `object`.

The method named `callback` should accept two arguments: the **TreeItem** that is drawn and its position and size as a [Rect2](class_rect2.md#class_Rect2).

---

<span id="class_TreeItem_method_set_custom_draw_callback"></span>

void **set_custom_draw_callback** ( column: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_treeitem.md#class_TreeItem_method_set_custom_draw_callback)

Sets the given column's custom draw callback. Use an empty [Callable](class_callable.md#class_Callable) (`Callable()`) to clear the custom callback. The cell has to be in [CELL_MODE_CUSTOM](class_treeitem.md#class_TreeItem_constant_CELL_MODE_CUSTOM) to use this feature.

The `callback` should accept two arguments: the **TreeItem** that is drawn and its position and size as a [Rect2](class_rect2.md#class_Rect2).

---

<span id="class_TreeItem_method_set_custom_font"></span>

void **set_custom_font** ( column: [int](class_int.md#class_int), font: [Font](class_font.md#class_Font) ) [🔗](class_treeitem.md#class_TreeItem_method_set_custom_font)

Sets custom font used to draw text in the given `column`.

---

<span id="class_TreeItem_method_set_custom_font_size"></span>

void **set_custom_font_size** ( column: [int](class_int.md#class_int), font_size: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_set_custom_font_size)

Sets custom font size used to draw text in the given `column`.

---

<span id="class_TreeItem_method_set_custom_stylebox"></span>

void **set_custom_stylebox** ( column: [int](class_int.md#class_int), stylebox: [StyleBox](class_stylebox.md#class_StyleBox) ) [🔗](class_treeitem.md#class_TreeItem_method_set_custom_stylebox)

Sets the given column's custom [StyleBox](class_stylebox.md#class_StyleBox) used to draw the background.

 **Note:** If a custom background color is set, the [StyleBox](class_stylebox.md#class_StyleBox) will be drawn in front of it.

---

<span id="class_TreeItem_method_set_description"></span>

void **set_description** ( column: [int](class_int.md#class_int), description: [String](class_string.md#class_String) ) [🔗](class_treeitem.md#class_TreeItem_method_set_description)

Sets the given column's description for assistive apps.

---

<span id="class_TreeItem_method_set_edit_multiline"></span>

void **set_edit_multiline** ( column: [int](class_int.md#class_int), multiline: [bool](class_bool.md#class_bool) ) [🔗](class_treeitem.md#class_TreeItem_method_set_edit_multiline)

If `multiline` is `true`, the given `column` is multiline editable.

 **Note:** This option only affects the type of control ([LineEdit](class_lineedit.md#class_LineEdit) or [TextEdit](class_textedit.md#class_TextEdit)) that appears when editing the column. You can set multiline values with [set_text()](class_treeitem.md#class_TreeItem_method_set_text) even if the column is not multiline editable.

---

<span id="class_TreeItem_method_set_editable"></span>

void **set_editable** ( column: [int](class_int.md#class_int), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_treeitem.md#class_TreeItem_method_set_editable)

If `enabled` is `true`, the given `column` is editable.

---

<span id="class_TreeItem_method_set_expand_right"></span>

void **set_expand_right** ( column: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_treeitem.md#class_TreeItem_method_set_expand_right)

If `enable` is `true`, the given `column` is expanded to the right.

---

<span id="class_TreeItem_method_set_icon"></span>

void **set_icon** ( column: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_treeitem.md#class_TreeItem_method_set_icon)

Sets the given cell's icon [Texture2D](class_texture2d.md#class_Texture2D). If the cell is in [CELL_MODE_ICON](class_treeitem.md#class_TreeItem_constant_CELL_MODE_ICON) mode, the icon is displayed in the center of the cell. Otherwise, the icon is displayed before the cell's text. [CELL_MODE_RANGE](class_treeitem.md#class_TreeItem_constant_CELL_MODE_RANGE) does not display an icon.

---

<span id="class_TreeItem_method_set_icon_max_width"></span>

void **set_icon_max_width** ( column: [int](class_int.md#class_int), width: [int](class_int.md#class_int) ) [🔗](class_treeitem.md#class_TreeItem_method_set_icon_max_width)

Sets the maximum allowed width of the icon in the given `column`. This limit is applied on top of the default size of the icon and on top of [Tree.icon_max_width](class_tree.md#class_Tree_theme_constant_icon_max_width). The height is adjusted according to the icon's ratio.

---

<span id="class_TreeItem_method_set_icon_modulate"></span>

void **set_icon_modulate** ( column: [int](class_int.md#class_int), modulate: [Color](class_color.md#class_Color) ) [🔗](class_treeitem.md#class_TreeItem_method_set_icon_modulate)

Modulates the given column's icon with `modulate`.

---

<span id="class_TreeItem_method_set_icon_overlay"></span>

void **set_icon_overlay** ( column: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_treeitem.md#class_TreeItem_method_set_icon_overlay)

Sets the given cell's icon overlay [Texture2D](class_texture2d.md#class_Texture2D). The cell has to be in [CELL_MODE_ICON](class_treeitem.md#class_TreeItem_constant_CELL_MODE_ICON) mode, and icon has to be set. Overlay is drawn on top of icon, in the bottom left corner.

---

<span id="class_TreeItem_method_set_icon_region"></span>

void **set_icon_region** ( column: [int](class_int.md#class_int), region: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_treeitem.md#class_TreeItem_method_set_icon_region)

Sets the given column's icon's texture region.

---

<span id="class_TreeItem_method_set_indeterminate"></span>

void **set_indeterminate** ( column: [int](class_int.md#class_int), indeterminate: [bool](class_bool.md#class_bool) ) [🔗](class_treeitem.md#class_TreeItem_method_set_indeterminate)

If `indeterminate` is `true`, the given `column` is marked indeterminate.

 **Note:** If set `true` from `false`, then column is cleared of checked status.

---

<span id="class_TreeItem_method_set_language"></span>

void **set_language** ( column: [int](class_int.md#class_int), language: [String](class_string.md#class_String) ) [🔗](class_treeitem.md#class_TreeItem_method_set_language)

Sets the language code of the given `column`'s text to `language`. This is used for line-breaking and text shaping algorithms. If `language` is empty, the current locale is used.

---

<span id="class_TreeItem_method_set_metadata"></span>

void **set_metadata** ( column: [int](class_int.md#class_int), meta: [Variant](class_variant.md#class_Variant) ) [🔗](class_treeitem.md#class_TreeItem_method_set_metadata)

Sets the metadata value for the given column, which can be retrieved later using [get_metadata()](class_treeitem.md#class_TreeItem_method_get_metadata). This can be used, for example, to store a reference to the original data.

---

<span id="class_TreeItem_method_set_range"></span>

void **set_range** ( column: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) [🔗](class_treeitem.md#class_TreeItem_method_set_range)

Sets the value of a [CELL_MODE_RANGE](class_treeitem.md#class_TreeItem_constant_CELL_MODE_RANGE) column.

---

<span id="class_TreeItem_method_set_range_config"></span>

void **set_range_config** ( column: [int](class_int.md#class_int), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float), step: [float](class_float.md#class_float), expr: [bool](class_bool.md#class_bool) = false ) [🔗](class_treeitem.md#class_TreeItem_method_set_range_config)

Sets the range of accepted values for a column. The column must be in the [CELL_MODE_RANGE](class_treeitem.md#class_TreeItem_constant_CELL_MODE_RANGE) mode.

If `expr` is `true`, the edit mode slider will use an exponential scale as with [Range.exp_edit](class_range.md#class_Range_property_exp_edit).

---

<span id="class_TreeItem_method_set_selectable"></span>

void **set_selectable** ( column: [int](class_int.md#class_int), selectable: [bool](class_bool.md#class_bool) ) [🔗](class_treeitem.md#class_TreeItem_method_set_selectable)

If `selectable` is `true`, the given `column` is selectable.

---

<span id="class_TreeItem_method_set_structured_text_bidi_override"></span>

void **set_structured_text_bidi_override** ( column: [int](class_int.md#class_int), parser: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) ) [🔗](class_treeitem.md#class_TreeItem_method_set_structured_text_bidi_override)

Set BiDi algorithm override for the structured text. Has effect for cells that display text.

---

<span id="class_TreeItem_method_set_structured_text_bidi_override_options"></span>

void **set_structured_text_bidi_override_options** ( column: [int](class_int.md#class_int), args: [Array](class_array.md#class_Array) ) [🔗](class_treeitem.md#class_TreeItem_method_set_structured_text_bidi_override_options)

Set additional options for BiDi override. Has effect for cells that display text.

---

<span id="class_TreeItem_method_set_suffix"></span>

void **set_suffix** ( column: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) [🔗](class_treeitem.md#class_TreeItem_method_set_suffix)

Sets a string to be shown after a column's value (for example, a unit abbreviation).

---

<span id="class_TreeItem_method_set_text"></span>

void **set_text** ( column: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) [🔗](class_treeitem.md#class_TreeItem_method_set_text)

Sets the given column's text value.

---

<span id="class_TreeItem_method_set_text_alignment"></span>

void **set_text_alignment** ( column: [int](class_int.md#class_int), text_alignment: HorizontalAlignment ) [🔗](class_treeitem.md#class_TreeItem_method_set_text_alignment)

Sets the given column's text alignment to `text_alignment`.

---

<span id="class_TreeItem_method_set_text_direction"></span>

void **set_text_direction** ( column: [int](class_int.md#class_int), direction: [TextDirection](class_control.md#enum_Control_TextDirection) ) [🔗](class_treeitem.md#class_TreeItem_method_set_text_direction)

Sets item's text base writing direction.

---

<span id="class_TreeItem_method_set_text_overrun_behavior"></span>

void **set_text_overrun_behavior** ( column: [int](class_int.md#class_int), overrun_behavior: [OverrunBehavior](class_textserver.md#enum_TextServer_OverrunBehavior) ) [🔗](class_treeitem.md#class_TreeItem_method_set_text_overrun_behavior)

Sets the clipping behavior when the text exceeds the item's bounding rectangle in the given `column`.

---

<span id="class_TreeItem_method_set_tooltip_text"></span>

void **set_tooltip_text** ( column: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) [🔗](class_treeitem.md#class_TreeItem_method_set_tooltip_text)

Sets the given column's tooltip text.

---

<span id="class_TreeItem_method_uncollapse_tree"></span>

void **uncollapse_tree** ( ) [🔗](class_treeitem.md#class_TreeItem_method_uncollapse_tree)

Uncollapses all **TreeItem** s necessary to reveal this **TreeItem**, i.e. all ancestor **TreeItem** s.
