.. meta::
	:keywords: textarea

<span id="class_TextEdit"></span>

## TextEdit

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CodeEdit](class_codeedit.md#class_CodeEdit)

A multiline text editor.

### Description

A multiline text editor. It also has limited facilities for editing code, such as syntax highlighting support. For more advanced facilities for editing code, see [CodeEdit](class_codeedit.md#class_CodeEdit).

While entering text, it is possible to insert special characters using Unicode, OEM or Windows alt codes:

- To enter Unicode codepoints, hold :kbd:`Alt` and type the codepoint on the numpad. For example, to enter the character `á` (U+00E1), hold :kbd:`Alt` and type :kbd:`+E1` on the numpad (the leading zeroes can be omitted).

- To enter OEM codepoints, hold :kbd:`Alt` and type the code on the numpad. For example, to enter the character `á` (OEM 160), hold :kbd:`Alt` and type `160` on the numpad.

- To enter Windows codepoints, hold :kbd:`Alt` and type the code on the numpad. For example, to enter the character `á` (Windows 0225), hold :kbd:`Alt` and type :kbd:`0`, :kbd:`2`, :kbd:`2`, :kbd:`5` on the numpad. The leading zero here must **not** be omitted, as this is how Windows codepoints are distinguished from OEM codepoints.

 **Note:** Most viewport, caret, and edit methods contain a `caret_index` argument for [caret_multiple](class_textedit.md#class_TextEdit_property_caret_multiple) support. The argument should be one of the following: `-1` for all carets, `0` for the main caret, or greater than `0` for secondary carets in the order they were created.

 **Note:** When holding down :kbd:`Alt`, the vertical scroll wheel will scroll 5 times as fast as it would normally do. This also works in the Godot script editor.

### Properties


| [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) | [autowrap_mode](class_textedit.md#class_TextEdit_property_autowrap_mode) | `3` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [backspace_deletes_composite_character_enabled](class_textedit.md#class_TextEdit_property_backspace_deletes_composite_character_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [caret_blink](class_textedit.md#class_TextEdit_property_caret_blink) | `false` |
| [float](class_float.md#class_float) | [caret_blink_interval](class_textedit.md#class_TextEdit_property_caret_blink_interval) | `0.65` |
| [bool](class_bool.md#class_bool) | [caret_draw_when_editable_disabled](class_textedit.md#class_TextEdit_property_caret_draw_when_editable_disabled) | `false` |
| [bool](class_bool.md#class_bool) | [caret_mid_grapheme](class_textedit.md#class_TextEdit_property_caret_mid_grapheme) | `false` |
| [bool](class_bool.md#class_bool) | [caret_move_on_right_click](class_textedit.md#class_TextEdit_property_caret_move_on_right_click) | `true` |
| [bool](class_bool.md#class_bool) | [caret_multiple](class_textedit.md#class_TextEdit_property_caret_multiple) | `true` |
| [CaretType](class_textedit.md#enum_TextEdit_CaretType) | [caret_type](class_textedit.md#class_TextEdit_property_caret_type) | `0` |
| [bool](class_bool.md#class_bool) | [context_menu_enabled](class_textedit.md#class_TextEdit_property_context_menu_enabled) | `true` |
| [String](class_string.md#class_String) | [custom_word_separators](class_textedit.md#class_TextEdit_property_custom_word_separators) | `""` |
| [bool](class_bool.md#class_bool) | [deselect_on_focus_loss_enabled](class_textedit.md#class_TextEdit_property_deselect_on_focus_loss_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [drag_and_drop_selection_enabled](class_textedit.md#class_TextEdit_property_drag_and_drop_selection_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [draw_control_chars](class_textedit.md#class_TextEdit_property_draw_control_chars) | `false` |
| [bool](class_bool.md#class_bool) | [draw_spaces](class_textedit.md#class_TextEdit_property_draw_spaces) | `false` |
| [bool](class_bool.md#class_bool) | [draw_tabs](class_textedit.md#class_TextEdit_property_draw_tabs) | `false` |
| [bool](class_bool.md#class_bool) | [editable](class_textedit.md#class_TextEdit_property_editable) | `true` |
| [bool](class_bool.md#class_bool) | [emoji_menu_enabled](class_textedit.md#class_TextEdit_property_emoji_menu_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [empty_selection_clipboard_enabled](class_textedit.md#class_TextEdit_property_empty_selection_clipboard_enabled) | `true` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `2` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [bool](class_bool.md#class_bool) | [highlight_all_occurrences](class_textedit.md#class_TextEdit_property_highlight_all_occurrences) | `false` |
| [bool](class_bool.md#class_bool) | [highlight_current_line](class_textedit.md#class_TextEdit_property_highlight_current_line) | `false` |
| [bool](class_bool.md#class_bool) | [indent_wrapped_lines](class_textedit.md#class_TextEdit_property_indent_wrapped_lines) | `false` |
| [String](class_string.md#class_String) | [language](class_textedit.md#class_TextEdit_property_language) | `""` |
| [bool](class_bool.md#class_bool) | [middle_mouse_paste_enabled](class_textedit.md#class_TextEdit_property_middle_mouse_paste_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [minimap_draw](class_textedit.md#class_TextEdit_property_minimap_draw) | `false` |
| [int](class_int.md#class_int) | [minimap_width](class_textedit.md#class_TextEdit_property_minimap_width) | `80` |
| [CursorShape](class_control.md#enum_Control_CursorShape) | mouse_default_cursor_shape | `1` (overrides [Control](class_control.md#class_Control_property_mouse_default_cursor_shape)) |
| [String](class_string.md#class_String) | [placeholder_text](class_textedit.md#class_TextEdit_property_placeholder_text) | `""` |
| [bool](class_bool.md#class_bool) | [scroll_fit_content_height](class_textedit.md#class_TextEdit_property_scroll_fit_content_height) | `false` |
| [bool](class_bool.md#class_bool) | [scroll_fit_content_width](class_textedit.md#class_TextEdit_property_scroll_fit_content_width) | `false` |
| [int](class_int.md#class_int) | [scroll_horizontal](class_textedit.md#class_TextEdit_property_scroll_horizontal) | `0` |
| [bool](class_bool.md#class_bool) | [scroll_past_end_of_file](class_textedit.md#class_TextEdit_property_scroll_past_end_of_file) | `false` |
| [bool](class_bool.md#class_bool) | [scroll_smooth](class_textedit.md#class_TextEdit_property_scroll_smooth) | `false` |
| [float](class_float.md#class_float) | [scroll_v_scroll_speed](class_textedit.md#class_TextEdit_property_scroll_v_scroll_speed) | `80.0` |
| [float](class_float.md#class_float) | [scroll_vertical](class_textedit.md#class_TextEdit_property_scroll_vertical) | `0.0` |
| [bool](class_bool.md#class_bool) | [selecting_enabled](class_textedit.md#class_TextEdit_property_selecting_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [shortcut_keys_enabled](class_textedit.md#class_TextEdit_property_shortcut_keys_enabled) | `true` |
| [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) | [structured_text_bidi_override](class_textedit.md#class_TextEdit_property_structured_text_bidi_override) | `0` |
| [Array](class_array.md#class_Array) | [structured_text_bidi_override_options](class_textedit.md#class_TextEdit_property_structured_text_bidi_override_options) | `[]` |
| [SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) | [syntax_highlighter](class_textedit.md#class_TextEdit_property_syntax_highlighter) |
| [bool](class_bool.md#class_bool) | [tab_input_mode](class_textedit.md#class_TextEdit_property_tab_input_mode) | `true` |
| [String](class_string.md#class_String) | [text](class_textedit.md#class_TextEdit_property_text) | `""` |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [text_direction](class_textedit.md#class_TextEdit_property_text_direction) | `0` |
| [bool](class_bool.md#class_bool) | [use_custom_word_separators](class_textedit.md#class_TextEdit_property_use_custom_word_separators) | `false` |
| [bool](class_bool.md#class_bool) | [use_default_word_separators](class_textedit.md#class_TextEdit_property_use_default_word_separators) | `true` |
| [bool](class_bool.md#class_bool) | [virtual_keyboard_enabled](class_textedit.md#class_TextEdit_property_virtual_keyboard_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [virtual_keyboard_show_on_focus](class_textedit.md#class_TextEdit_property_virtual_keyboard_show_on_focus) | `true` |
| [LineWrappingMode](class_textedit.md#enum_TextEdit_LineWrappingMode) | [wrap_mode](class_textedit.md#class_TextEdit_property_wrap_mode) | `0` |

### Methods


| void | [_backspace](class_textedit.md#class_TextEdit_private_method__backspace) ( caret_index: [int](class_int.md#class_int) ) virtual |
| --- | --- |
| void | [_copy](class_textedit.md#class_TextEdit_private_method__copy) ( caret_index: [int](class_int.md#class_int) ) virtual |
| void | [_cut](class_textedit.md#class_TextEdit_private_method__cut) ( caret_index: [int](class_int.md#class_int) ) virtual |
| void | [_handle_unicode_input](class_textedit.md#class_TextEdit_private_method__handle_unicode_input) ( unicode_char: [int](class_int.md#class_int), caret_index: [int](class_int.md#class_int) ) virtual |
| void | [_paste](class_textedit.md#class_TextEdit_private_method__paste) ( caret_index: [int](class_int.md#class_int) ) virtual |
| void | [_paste_primary_clipboard](class_textedit.md#class_TextEdit_private_method__paste_primary_clipboard) ( caret_index: [int](class_int.md#class_int) ) virtual |
| [int](class_int.md#class_int) | [add_caret](class_textedit.md#class_TextEdit_method_add_caret) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) |
| void | [add_caret_at_carets](class_textedit.md#class_TextEdit_method_add_caret_at_carets) ( below: [bool](class_bool.md#class_bool) ) |
| void | [add_gutter](class_textedit.md#class_TextEdit_method_add_gutter) ( at: [int](class_int.md#class_int) = -1 ) |
| void | [add_selection_for_next_occurrence](class_textedit.md#class_TextEdit_method_add_selection_for_next_occurrence) ( ) |
| void | [adjust_carets_after_edit](class_textedit.md#class_TextEdit_method_adjust_carets_after_edit) ( caret: [int](class_int.md#class_int), from_line: [int](class_int.md#class_int), from_col: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int), to_col: [int](class_int.md#class_int) ) |
| void | [adjust_viewport_to_caret](class_textedit.md#class_TextEdit_method_adjust_viewport_to_caret) ( caret_index: [int](class_int.md#class_int) = 0 ) |
| void | [apply_ime](class_textedit.md#class_TextEdit_method_apply_ime) ( ) |
| void | [backspace](class_textedit.md#class_TextEdit_method_backspace) ( caret_index: [int](class_int.md#class_int) = -1 ) |
| void | [begin_complex_operation](class_textedit.md#class_TextEdit_method_begin_complex_operation) ( ) |
| void | [begin_multicaret_edit](class_textedit.md#class_TextEdit_method_begin_multicaret_edit) ( ) |
| void | [cancel_ime](class_textedit.md#class_TextEdit_method_cancel_ime) ( ) |
| void | [center_viewport_to_caret](class_textedit.md#class_TextEdit_method_center_viewport_to_caret) ( caret_index: [int](class_int.md#class_int) = 0 ) |
| void | [clear](class_textedit.md#class_TextEdit_method_clear) ( ) |
| void | [clear_undo_history](class_textedit.md#class_TextEdit_method_clear_undo_history) ( ) |
| void | [collapse_carets](class_textedit.md#class_TextEdit_method_collapse_carets) ( from_line: [int](class_int.md#class_int), from_column: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int), to_column: [int](class_int.md#class_int), inclusive: [bool](class_bool.md#class_bool) = false ) |
| void | [copy](class_textedit.md#class_TextEdit_method_copy) ( caret_index: [int](class_int.md#class_int) = -1 ) |
| void | [cut](class_textedit.md#class_TextEdit_method_cut) ( caret_index: [int](class_int.md#class_int) = -1 ) |
| void | [delete_selection](class_textedit.md#class_TextEdit_method_delete_selection) ( caret_index: [int](class_int.md#class_int) = -1 ) |
| void | [deselect](class_textedit.md#class_TextEdit_method_deselect) ( caret_index: [int](class_int.md#class_int) = -1 ) |
| void | [end_action](class_textedit.md#class_TextEdit_method_end_action) ( ) |
| void | [end_complex_operation](class_textedit.md#class_TextEdit_method_end_complex_operation) ( ) |
| void | [end_multicaret_edit](class_textedit.md#class_TextEdit_method_end_multicaret_edit) ( ) |
| [int](class_int.md#class_int) | [get_caret_column](class_textedit.md#class_TextEdit_method_get_caret_column) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_caret_count](class_textedit.md#class_TextEdit_method_get_caret_count) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_caret_draw_pos](class_textedit.md#class_TextEdit_method_get_caret_draw_pos) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_caret_index_edit_order](class_textedit.md#class_TextEdit_method_get_caret_index_edit_order) ( ) |
| [int](class_int.md#class_int) | [get_caret_line](class_textedit.md#class_TextEdit_method_get_caret_line) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_caret_wrap_index](class_textedit.md#class_TextEdit_method_get_caret_wrap_index) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_first_non_whitespace_column](class_textedit.md#class_TextEdit_method_get_first_non_whitespace_column) ( line: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_first_visible_line](class_textedit.md#class_TextEdit_method_get_first_visible_line) ( ) const |
| [int](class_int.md#class_int) | [get_gutter_count](class_textedit.md#class_TextEdit_method_get_gutter_count) ( ) const |
| [String](class_string.md#class_String) | [get_gutter_name](class_textedit.md#class_TextEdit_method_get_gutter_name) ( gutter: [int](class_int.md#class_int) ) const |
| [GutterType](class_textedit.md#enum_TextEdit_GutterType) | [get_gutter_type](class_textedit.md#class_TextEdit_method_get_gutter_type) ( gutter: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_gutter_width](class_textedit.md#class_TextEdit_method_get_gutter_width) ( gutter: [int](class_int.md#class_int) ) const |
| [HScrollBar](class_hscrollbar.md#class_HScrollBar) | [get_h_scroll_bar](class_textedit.md#class_TextEdit_method_get_h_scroll_bar) ( ) const |
| [int](class_int.md#class_int) | [get_indent_level](class_textedit.md#class_TextEdit_method_get_indent_level) ( line: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_last_full_visible_line](class_textedit.md#class_TextEdit_method_get_last_full_visible_line) ( ) const |
| [int](class_int.md#class_int) | [get_last_full_visible_line_wrap_index](class_textedit.md#class_TextEdit_method_get_last_full_visible_line_wrap_index) ( ) const |
| [int](class_int.md#class_int) | [get_last_unhidden_line](class_textedit.md#class_TextEdit_method_get_last_unhidden_line) ( ) const |
| [String](class_string.md#class_String) | [get_line](class_textedit.md#class_TextEdit_method_get_line) ( line: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_line_background_color](class_textedit.md#class_TextEdit_method_get_line_background_color) ( line: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_line_column_at_pos](class_textedit.md#class_TextEdit_method_get_line_column_at_pos) ( position: [Vector2i](class_vector2i.md#class_Vector2i), clamp_line: [bool](class_bool.md#class_bool) = true, clamp_column: [bool](class_bool.md#class_bool) = true ) const |
| [int](class_int.md#class_int) | [get_line_count](class_textedit.md#class_TextEdit_method_get_line_count) ( ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_line_gutter_icon](class_textedit.md#class_TextEdit_method_get_line_gutter_icon) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [get_line_gutter_item_color](class_textedit.md#class_TextEdit_method_get_line_gutter_item_color) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_line_gutter_metadata](class_textedit.md#class_TextEdit_method_get_line_gutter_metadata) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_line_gutter_text](class_textedit.md#class_TextEdit_method_get_line_gutter_text) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_line_height](class_textedit.md#class_TextEdit_method_get_line_height) ( ) const |
| [Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] | [get_line_ranges_from_carets](class_textedit.md#class_TextEdit_method_get_line_ranges_from_carets) ( only_selections: [bool](class_bool.md#class_bool) = false, merge_adjacent: [bool](class_bool.md#class_bool) = true ) const |
| [int](class_int.md#class_int) | [get_line_width](class_textedit.md#class_TextEdit_method_get_line_width) ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = -1 ) const |
| [String](class_string.md#class_String) | [get_line_with_ime](class_textedit.md#class_TextEdit_method_get_line_with_ime) ( line: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_line_wrap_count](class_textedit.md#class_TextEdit_method_get_line_wrap_count) ( line: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_line_wrap_index_at_column](class_textedit.md#class_TextEdit_method_get_line_wrap_index_at_column) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_line_wrapped_text](class_textedit.md#class_TextEdit_method_get_line_wrapped_text) ( line: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_local_mouse_pos](class_textedit.md#class_TextEdit_method_get_local_mouse_pos) ( ) const |
| [PopupMenu](class_popupmenu.md#class_PopupMenu) | [get_menu](class_textedit.md#class_TextEdit_method_get_menu) ( ) const |
| [int](class_int.md#class_int) | [get_minimap_line_at_pos](class_textedit.md#class_TextEdit_method_get_minimap_line_at_pos) ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [int](class_int.md#class_int) | [get_minimap_visible_lines](class_textedit.md#class_TextEdit_method_get_minimap_visible_lines) ( ) const |
| [int](class_int.md#class_int) | [get_next_composite_character_column](class_textedit.md#class_TextEdit_method_get_next_composite_character_column) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_next_visible_line_index_offset_from](class_textedit.md#class_TextEdit_method_get_next_visible_line_index_offset_from) ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int), visible_amount: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_next_visible_line_offset_from](class_textedit.md#class_TextEdit_method_get_next_visible_line_offset_from) ( line: [int](class_int.md#class_int), visible_amount: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_pos_at_line_column](class_textedit.md#class_TextEdit_method_get_pos_at_line_column) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_previous_composite_character_column](class_textedit.md#class_TextEdit_method_get_previous_composite_character_column) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) const |
| [Rect2i](class_rect2i.md#class_Rect2i) | [get_rect_at_line_column](class_textedit.md#class_TextEdit_method_get_rect_at_line_column) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_saved_version](class_textedit.md#class_TextEdit_method_get_saved_version) ( ) const |
| [float](class_float.md#class_float) | [get_scroll_pos_for_line](class_textedit.md#class_TextEdit_method_get_scroll_pos_for_line) ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = 0 ) const |
| [String](class_string.md#class_String) | [get_selected_text](class_textedit.md#class_TextEdit_method_get_selected_text) ( caret_index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [get_selection_at_line_column](class_textedit.md#class_TextEdit_method_get_selection_at_line_column) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int), include_edges: [bool](class_bool.md#class_bool) = true, only_selections: [bool](class_bool.md#class_bool) = true ) const |
| [int](class_int.md#class_int) | [get_selection_column](class_textedit.md#class_TextEdit_method_get_selection_column) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_selection_from_column](class_textedit.md#class_TextEdit_method_get_selection_from_column) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_selection_from_line](class_textedit.md#class_TextEdit_method_get_selection_from_line) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_selection_line](class_textedit.md#class_TextEdit_method_get_selection_line) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [SelectionMode](class_textedit.md#enum_TextEdit_SelectionMode) | [get_selection_mode](class_textedit.md#class_TextEdit_method_get_selection_mode) ( ) const |
| [int](class_int.md#class_int) | [get_selection_origin_column](class_textedit.md#class_TextEdit_method_get_selection_origin_column) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_selection_origin_line](class_textedit.md#class_TextEdit_method_get_selection_origin_line) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_selection_to_column](class_textedit.md#class_TextEdit_method_get_selection_to_column) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [get_selection_to_line](class_textedit.md#class_TextEdit_method_get_selection_to_line) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_sorted_carets](class_textedit.md#class_TextEdit_method_get_sorted_carets) ( include_ignored_carets: [bool](class_bool.md#class_bool) = false ) const |
| [int](class_int.md#class_int) | [get_tab_size](class_textedit.md#class_TextEdit_method_get_tab_size) ( ) const |
| [int](class_int.md#class_int) | [get_total_gutter_width](class_textedit.md#class_TextEdit_method_get_total_gutter_width) ( ) const |
| [int](class_int.md#class_int) | [get_total_visible_line_count](class_textedit.md#class_TextEdit_method_get_total_visible_line_count) ( ) const |
| [VScrollBar](class_vscrollbar.md#class_VScrollBar) | [get_v_scroll_bar](class_textedit.md#class_TextEdit_method_get_v_scroll_bar) ( ) const |
| [int](class_int.md#class_int) | [get_version](class_textedit.md#class_TextEdit_method_get_version) ( ) const |
| [int](class_int.md#class_int) | [get_visible_line_count](class_textedit.md#class_TextEdit_method_get_visible_line_count) ( ) const |
| [int](class_int.md#class_int) | [get_visible_line_count_in_range](class_textedit.md#class_TextEdit_method_get_visible_line_count_in_range) ( from_line: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_word_at_pos](class_textedit.md#class_TextEdit_method_get_word_at_pos) ( position: [Vector2](class_vector2.md#class_Vector2) ) const |
| [String](class_string.md#class_String) | [get_word_under_caret](class_textedit.md#class_TextEdit_method_get_word_under_caret) ( caret_index: [int](class_int.md#class_int) = -1 ) const |
| [bool](class_bool.md#class_bool) | [has_ime_text](class_textedit.md#class_TextEdit_method_has_ime_text) ( ) const |
| [bool](class_bool.md#class_bool) | [has_redo](class_textedit.md#class_TextEdit_method_has_redo) ( ) const |
| [bool](class_bool.md#class_bool) | [has_selection](class_textedit.md#class_TextEdit_method_has_selection) ( caret_index: [int](class_int.md#class_int) = -1 ) const |
| [bool](class_bool.md#class_bool) | [has_undo](class_textedit.md#class_TextEdit_method_has_undo) ( ) const |
| void | [insert_line_at](class_textedit.md#class_TextEdit_method_insert_line_at) ( line: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) |
| void | [insert_text](class_textedit.md#class_TextEdit_method_insert_text) ( text: [String](class_string.md#class_String), line: [int](class_int.md#class_int), column: [int](class_int.md#class_int), before_selection_begin: [bool](class_bool.md#class_bool) = true, before_selection_end: [bool](class_bool.md#class_bool) = false ) |
| void | [insert_text_at_caret](class_textedit.md#class_TextEdit_method_insert_text_at_caret) ( text: [String](class_string.md#class_String), caret_index: [int](class_int.md#class_int) = -1 ) |
| [bool](class_bool.md#class_bool) | [is_caret_after_selection_origin](class_textedit.md#class_TextEdit_method_is_caret_after_selection_origin) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [bool](class_bool.md#class_bool) | [is_caret_visible](class_textedit.md#class_TextEdit_method_is_caret_visible) ( caret_index: [int](class_int.md#class_int) = 0 ) const |
| [bool](class_bool.md#class_bool) | [is_dragging_cursor](class_textedit.md#class_TextEdit_method_is_dragging_cursor) ( ) const |
| [bool](class_bool.md#class_bool) | [is_gutter_clickable](class_textedit.md#class_TextEdit_method_is_gutter_clickable) ( gutter: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_gutter_drawn](class_textedit.md#class_TextEdit_method_is_gutter_drawn) ( gutter: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_gutter_overwritable](class_textedit.md#class_TextEdit_method_is_gutter_overwritable) ( gutter: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_in_mulitcaret_edit](class_textedit.md#class_TextEdit_method_is_in_mulitcaret_edit) ( ) const |
| [bool](class_bool.md#class_bool) | [is_line_gutter_clickable](class_textedit.md#class_TextEdit_method_is_line_gutter_clickable) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_line_wrapped](class_textedit.md#class_TextEdit_method_is_line_wrapped) ( line: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_menu_visible](class_textedit.md#class_TextEdit_method_is_menu_visible) ( ) const |
| [bool](class_bool.md#class_bool) | [is_mouse_over_selection](class_textedit.md#class_TextEdit_method_is_mouse_over_selection) ( edges: [bool](class_bool.md#class_bool), caret_index: [int](class_int.md#class_int) = -1 ) const |
| [bool](class_bool.md#class_bool) | [is_overtype_mode_enabled](class_textedit.md#class_TextEdit_method_is_overtype_mode_enabled) ( ) const |
| void | [menu_option](class_textedit.md#class_TextEdit_method_menu_option) ( option: [int](class_int.md#class_int) ) |
| void | [merge_gutters](class_textedit.md#class_TextEdit_method_merge_gutters) ( from_line: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int) ) |
| void | [merge_overlapping_carets](class_textedit.md#class_TextEdit_method_merge_overlapping_carets) ( ) |
| [bool](class_bool.md#class_bool) | [multicaret_edit_ignore_caret](class_textedit.md#class_TextEdit_method_multicaret_edit_ignore_caret) ( caret_index: [int](class_int.md#class_int) ) const |
| void | [paste](class_textedit.md#class_TextEdit_method_paste) ( caret_index: [int](class_int.md#class_int) = -1 ) |
| void | [paste_primary_clipboard](class_textedit.md#class_TextEdit_method_paste_primary_clipboard) ( caret_index: [int](class_int.md#class_int) = -1 ) |
| void | [redo](class_textedit.md#class_TextEdit_method_redo) ( ) |
| void | [remove_caret](class_textedit.md#class_TextEdit_method_remove_caret) ( caret: [int](class_int.md#class_int) ) |
| void | [remove_gutter](class_textedit.md#class_TextEdit_method_remove_gutter) ( gutter: [int](class_int.md#class_int) ) |
| void | [remove_line_at](class_textedit.md#class_TextEdit_method_remove_line_at) ( line: [int](class_int.md#class_int), move_carets_down: [bool](class_bool.md#class_bool) = true ) |
| void | [remove_secondary_carets](class_textedit.md#class_TextEdit_method_remove_secondary_carets) ( ) |
| void | [remove_text](class_textedit.md#class_TextEdit_method_remove_text) ( from_line: [int](class_int.md#class_int), from_column: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int), to_column: [int](class_int.md#class_int) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [search](class_textedit.md#class_TextEdit_method_search) ( text: [String](class_string.md#class_String), flags: [int](class_int.md#class_int), from_line: [int](class_int.md#class_int), from_column: [int](class_int.md#class_int) ) const |
| void | [select](class_textedit.md#class_TextEdit_method_select) ( origin_line: [int](class_int.md#class_int), origin_column: [int](class_int.md#class_int), caret_line: [int](class_int.md#class_int), caret_column: [int](class_int.md#class_int), caret_index: [int](class_int.md#class_int) = 0 ) |
| void | [select_all](class_textedit.md#class_TextEdit_method_select_all) ( ) |
| void | [select_word_under_caret](class_textedit.md#class_TextEdit_method_select_word_under_caret) ( caret_index: [int](class_int.md#class_int) = -1 ) |
| void | [set_caret_column](class_textedit.md#class_TextEdit_method_set_caret_column) ( column: [int](class_int.md#class_int), adjust_viewport: [bool](class_bool.md#class_bool) = true, caret_index: [int](class_int.md#class_int) = 0 ) |
| void | [set_caret_line](class_textedit.md#class_TextEdit_method_set_caret_line) ( line: [int](class_int.md#class_int), adjust_viewport: [bool](class_bool.md#class_bool) = true, can_be_hidden: [bool](class_bool.md#class_bool) = true, wrap_index: [int](class_int.md#class_int) = 0, caret_index: [int](class_int.md#class_int) = 0 ) |
| void | [set_gutter_clickable](class_textedit.md#class_TextEdit_method_set_gutter_clickable) ( gutter: [int](class_int.md#class_int), clickable: [bool](class_bool.md#class_bool) ) |
| void | [set_gutter_custom_draw](class_textedit.md#class_TextEdit_method_set_gutter_custom_draw) ( column: [int](class_int.md#class_int), draw_callback: [Callable](class_callable.md#class_Callable) ) |
| void | [set_gutter_draw](class_textedit.md#class_TextEdit_method_set_gutter_draw) ( gutter: [int](class_int.md#class_int), draw: [bool](class_bool.md#class_bool) ) |
| void | [set_gutter_name](class_textedit.md#class_TextEdit_method_set_gutter_name) ( gutter: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [set_gutter_overwritable](class_textedit.md#class_TextEdit_method_set_gutter_overwritable) ( gutter: [int](class_int.md#class_int), overwritable: [bool](class_bool.md#class_bool) ) |
| void | [set_gutter_type](class_textedit.md#class_TextEdit_method_set_gutter_type) ( gutter: [int](class_int.md#class_int), type: [GutterType](class_textedit.md#enum_TextEdit_GutterType) ) |
| void | [set_gutter_width](class_textedit.md#class_TextEdit_method_set_gutter_width) ( gutter: [int](class_int.md#class_int), width: [int](class_int.md#class_int) ) |
| void | [set_line](class_textedit.md#class_TextEdit_method_set_line) ( line: [int](class_int.md#class_int), new_text: [String](class_string.md#class_String) ) |
| void | [set_line_as_center_visible](class_textedit.md#class_TextEdit_method_set_line_as_center_visible) ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = 0 ) |
| void | [set_line_as_first_visible](class_textedit.md#class_TextEdit_method_set_line_as_first_visible) ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = 0 ) |
| void | [set_line_as_last_visible](class_textedit.md#class_TextEdit_method_set_line_as_last_visible) ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = 0 ) |
| void | [set_line_background_color](class_textedit.md#class_TextEdit_method_set_line_background_color) ( line: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_line_gutter_clickable](class_textedit.md#class_TextEdit_method_set_line_gutter_clickable) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), clickable: [bool](class_bool.md#class_bool) ) |
| void | [set_line_gutter_icon](class_textedit.md#class_TextEdit_method_set_line_gutter_icon) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_line_gutter_item_color](class_textedit.md#class_TextEdit_method_set_line_gutter_item_color) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [set_line_gutter_metadata](class_textedit.md#class_TextEdit_method_set_line_gutter_metadata) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) |
| void | [set_line_gutter_text](class_textedit.md#class_TextEdit_method_set_line_gutter_text) ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) |
| void | [set_overtype_mode_enabled](class_textedit.md#class_TextEdit_method_set_overtype_mode_enabled) ( enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_search_flags](class_textedit.md#class_TextEdit_method_set_search_flags) ( flags: [int](class_int.md#class_int) ) |
| void | [set_search_text](class_textedit.md#class_TextEdit_method_set_search_text) ( search_text: [String](class_string.md#class_String) ) |
| void | [set_selection_mode](class_textedit.md#class_TextEdit_method_set_selection_mode) ( mode: [SelectionMode](class_textedit.md#enum_TextEdit_SelectionMode) ) |
| void | [set_selection_origin_column](class_textedit.md#class_TextEdit_method_set_selection_origin_column) ( column: [int](class_int.md#class_int), caret_index: [int](class_int.md#class_int) = 0 ) |
| void | [set_selection_origin_line](class_textedit.md#class_TextEdit_method_set_selection_origin_line) ( line: [int](class_int.md#class_int), can_be_hidden: [bool](class_bool.md#class_bool) = true, wrap_index: [int](class_int.md#class_int) = -1, caret_index: [int](class_int.md#class_int) = 0 ) |
| void | [set_tab_size](class_textedit.md#class_TextEdit_method_set_tab_size) ( size: [int](class_int.md#class_int) ) |
| void | [set_tooltip_request_func](class_textedit.md#class_TextEdit_method_set_tooltip_request_func) ( callback: [Callable](class_callable.md#class_Callable) ) |
| void | [skip_selection_for_next_occurrence](class_textedit.md#class_TextEdit_method_skip_selection_for_next_occurrence) ( ) |
| void | [start_action](class_textedit.md#class_TextEdit_method_start_action) ( action: [EditAction](class_textedit.md#enum_TextEdit_EditAction) ) |
| void | [swap_lines](class_textedit.md#class_TextEdit_method_swap_lines) ( from_line: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int) ) |
| void | [tag_saved_version](class_textedit.md#class_TextEdit_method_tag_saved_version) ( ) |
| void | [undo](class_textedit.md#class_TextEdit_method_undo) ( ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [background_color](class_textedit.md#class_TextEdit_theme_color_background_color) | `Color(0, 0, 0, 0)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [caret_background_color](class_textedit.md#class_TextEdit_theme_color_caret_background_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [caret_color](class_textedit.md#class_TextEdit_theme_color_caret_color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class_Color) | [current_line_color](class_textedit.md#class_TextEdit_theme_color_current_line_color) | `Color(0.25, 0.25, 0.26, 0.8)` |
| [Color](class_color.md#class_Color) | [font_color](class_textedit.md#class_TextEdit_theme_color_font_color) | `Color(0.875, 0.875, 0.875, 1)` |
| [Color](class_color.md#class_Color) | [font_outline_color](class_textedit.md#class_TextEdit_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_placeholder_color](class_textedit.md#class_TextEdit_theme_color_font_placeholder_color) | `Color(0.875, 0.875, 0.875, 0.6)` |
| [Color](class_color.md#class_Color) | [font_readonly_color](class_textedit.md#class_TextEdit_theme_color_font_readonly_color) | `Color(0.875, 0.875, 0.875, 0.5)` |
| [Color](class_color.md#class_Color) | [font_selected_color](class_textedit.md#class_TextEdit_theme_color_font_selected_color) | `Color(0, 0, 0, 0)` |
| [Color](class_color.md#class_Color) | [search_result_border_color](class_textedit.md#class_TextEdit_theme_color_search_result_border_color) | `Color(0.3, 0.3, 0.3, 0.4)` |
| [Color](class_color.md#class_Color) | [search_result_color](class_textedit.md#class_TextEdit_theme_color_search_result_color) | `Color(0.3, 0.3, 0.3, 1)` |
| [Color](class_color.md#class_Color) | [selection_color](class_textedit.md#class_TextEdit_theme_color_selection_color) | `Color(0.5, 0.5, 0.5, 1)` |
| [Color](class_color.md#class_Color) | [word_highlighted_color](class_textedit.md#class_TextEdit_theme_color_word_highlighted_color) | `Color(0.5, 0.5, 0.5, 0.25)` |
| [int](class_int.md#class_int) | [caret_width](class_textedit.md#class_TextEdit_theme_constant_caret_width) | `1` |
| [int](class_int.md#class_int) | [line_spacing](class_textedit.md#class_TextEdit_theme_constant_line_spacing) | `4` |
| [int](class_int.md#class_int) | [outline_size](class_textedit.md#class_TextEdit_theme_constant_outline_size) | `0` |
| [int](class_int.md#class_int) | [wrap_offset](class_textedit.md#class_TextEdit_theme_constant_wrap_offset) | `10` |
| [Font](class_font.md#class_Font) | [font](class_textedit.md#class_TextEdit_theme_font_font) |
| [int](class_int.md#class_int) | [font_size](class_textedit.md#class_TextEdit_theme_font_size_font_size) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [space](class_textedit.md#class_TextEdit_theme_icon_space) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [tab](class_textedit.md#class_TextEdit_theme_icon_tab) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [focus](class_textedit.md#class_TextEdit_theme_style_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [normal](class_textedit.md#class_TextEdit_theme_style_normal) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [read_only](class_textedit.md#class_TextEdit_theme_style_read_only) |

---

### Signals

<span id="class_TextEdit_signal_caret_changed"></span>

**caret_changed** ( ) [🔗](class_textedit.md#class_TextEdit_signal_caret_changed)

Emitted when any caret changes position.

---

<span id="class_TextEdit_signal_gutter_added"></span>

**gutter_added** ( ) [🔗](class_textedit.md#class_TextEdit_signal_gutter_added)

Emitted when a gutter is added.

---

<span id="class_TextEdit_signal_gutter_clicked"></span>

**gutter_clicked** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_signal_gutter_clicked)

Emitted when a gutter is clicked.

---

<span id="class_TextEdit_signal_gutter_removed"></span>

**gutter_removed** ( ) [🔗](class_textedit.md#class_TextEdit_signal_gutter_removed)

Emitted when a gutter is removed.

---

<span id="class_TextEdit_signal_lines_edited_from"></span>

**lines_edited_from** ( from_line: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_signal_lines_edited_from)

Emitted immediately when the text changes.

When text is added `from_line` will be less than `to_line`. On a remove `to_line` will be less than `from_line`.

---

<span id="class_TextEdit_signal_text_changed"></span>

**text_changed** ( ) [🔗](class_textedit.md#class_TextEdit_signal_text_changed)

Emitted when the text changes.

---

<span id="class_TextEdit_signal_text_set"></span>

**text_set** ( ) [🔗](class_textedit.md#class_TextEdit_signal_text_set)

Emitted when [clear()](class_textedit.md#class_TextEdit_method_clear) is called or [text](class_textedit.md#class_TextEdit_property_text) is set.

---

### Enumerations

<span id="enum_TextEdit_MenuItems"></span>

enum **MenuItems**: [🔗](class_textedit.md#enum_TextEdit_MenuItems)

<span id="class_TextEdit_constant_MENU_CUT"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_CUT** = `0`

Cuts (copies and clears) the selected text.

<span id="class_TextEdit_constant_MENU_COPY"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_COPY** = `1`

Copies the selected text.

<span id="class_TextEdit_constant_MENU_PASTE"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_PASTE** = `2`

Pastes the clipboard text over the selected text (or at the cursor's position).

<span id="class_TextEdit_constant_MENU_CLEAR"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_CLEAR** = `3`

Erases the whole **TextEdit** text.

<span id="class_TextEdit_constant_MENU_SELECT_ALL"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_SELECT_ALL** = `4`

Selects the whole **TextEdit** text.

<span id="class_TextEdit_constant_MENU_UNDO"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_UNDO** = `5`

Undoes the previous action.

<span id="class_TextEdit_constant_MENU_REDO"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_REDO** = `6`

Redoes the previous action.

<span id="class_TextEdit_constant_MENU_SUBMENU_TEXT_DIR"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_SUBMENU_TEXT_DIR** = `7`

ID of "Text Writing Direction" submenu.

<span id="class_TextEdit_constant_MENU_DIR_INHERITED"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_DIR_INHERITED** = `8`

Sets text direction to inherited.

<span id="class_TextEdit_constant_MENU_DIR_AUTO"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_DIR_AUTO** = `9`

Sets text direction to automatic.

<span id="class_TextEdit_constant_MENU_DIR_LTR"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_DIR_LTR** = `10`

Sets text direction to left-to-right.

<span id="class_TextEdit_constant_MENU_DIR_RTL"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_DIR_RTL** = `11`

Sets text direction to right-to-left.

<span id="class_TextEdit_constant_MENU_DISPLAY_UCC"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_DISPLAY_UCC** = `12`

Toggles control character display.

<span id="class_TextEdit_constant_MENU_SUBMENU_INSERT_UCC"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_SUBMENU_INSERT_UCC** = `13`

ID of "Insert Control Character" submenu.

<span id="class_TextEdit_constant_MENU_INSERT_LRM"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_LRM** = `14`

Inserts left-to-right mark (LRM) character.

<span id="class_TextEdit_constant_MENU_INSERT_RLM"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_RLM** = `15`

Inserts right-to-left mark (RLM) character.

<span id="class_TextEdit_constant_MENU_INSERT_LRE"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_LRE** = `16`

Inserts start of left-to-right embedding (LRE) character.

<span id="class_TextEdit_constant_MENU_INSERT_RLE"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_RLE** = `17`

Inserts start of right-to-left embedding (RLE) character.

<span id="class_TextEdit_constant_MENU_INSERT_LRO"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_LRO** = `18`

Inserts start of left-to-right override (LRO) character.

<span id="class_TextEdit_constant_MENU_INSERT_RLO"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_RLO** = `19`

Inserts start of right-to-left override (RLO) character.

<span id="class_TextEdit_constant_MENU_INSERT_PDF"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_PDF** = `20`

Inserts pop direction formatting (PDF) character.

<span id="class_TextEdit_constant_MENU_INSERT_ALM"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_ALM** = `21`

Inserts Arabic letter mark (ALM) character.

<span id="class_TextEdit_constant_MENU_INSERT_LRI"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_LRI** = `22`

Inserts left-to-right isolate (LRI) character.

<span id="class_TextEdit_constant_MENU_INSERT_RLI"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_RLI** = `23`

Inserts right-to-left isolate (RLI) character.

<span id="class_TextEdit_constant_MENU_INSERT_FSI"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_FSI** = `24`

Inserts first strong isolate (FSI) character.

<span id="class_TextEdit_constant_MENU_INSERT_PDI"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_PDI** = `25`

Inserts pop direction isolate (PDI) character.

<span id="class_TextEdit_constant_MENU_INSERT_ZWJ"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_ZWJ** = `26`

Inserts zero width joiner (ZWJ) character.

<span id="class_TextEdit_constant_MENU_INSERT_ZWNJ"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_ZWNJ** = `27`

Inserts zero width non-joiner (ZWNJ) character.

<span id="class_TextEdit_constant_MENU_INSERT_WJ"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_WJ** = `28`

Inserts word joiner (WJ) character.

<span id="class_TextEdit_constant_MENU_INSERT_SHY"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_INSERT_SHY** = `29`

Inserts soft hyphen (SHY) character.

<span id="class_TextEdit_constant_MENU_EMOJI_AND_SYMBOL"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_EMOJI_AND_SYMBOL** = `30`

Opens system emoji and symbol picker.

<span id="class_TextEdit_constant_MENU_MAX"></span>

[MenuItems](class_textedit.md#enum_TextEdit_MenuItems) **MENU_MAX** = `31`

Represents the size of the [MenuItems](class_textedit.md#enum_TextEdit_MenuItems) enum.

---

<span id="enum_TextEdit_EditAction"></span>

enum **EditAction**: [🔗](class_textedit.md#enum_TextEdit_EditAction)

<span id="class_TextEdit_constant_ACTION_NONE"></span>

[EditAction](class_textedit.md#enum_TextEdit_EditAction) **ACTION_NONE** = `0`

No current action.

<span id="class_TextEdit_constant_ACTION_TYPING"></span>

[EditAction](class_textedit.md#enum_TextEdit_EditAction) **ACTION_TYPING** = `1`

A typing action.

<span id="class_TextEdit_constant_ACTION_BACKSPACE"></span>

[EditAction](class_textedit.md#enum_TextEdit_EditAction) **ACTION_BACKSPACE** = `2`

A backwards delete action.

<span id="class_TextEdit_constant_ACTION_DELETE"></span>

[EditAction](class_textedit.md#enum_TextEdit_EditAction) **ACTION_DELETE** = `3`

A forward delete action.

---

<span id="enum_TextEdit_SearchFlags"></span>

enum **SearchFlags**: [🔗](class_textedit.md#enum_TextEdit_SearchFlags)

<span id="class_TextEdit_constant_SEARCH_MATCH_CASE"></span>

[SearchFlags](class_textedit.md#enum_TextEdit_SearchFlags) **SEARCH_MATCH_CASE** = `1`

Match case when searching.

<span id="class_TextEdit_constant_SEARCH_WHOLE_WORDS"></span>

[SearchFlags](class_textedit.md#enum_TextEdit_SearchFlags) **SEARCH_WHOLE_WORDS** = `2`

Match whole words when searching.

<span id="class_TextEdit_constant_SEARCH_BACKWARDS"></span>

[SearchFlags](class_textedit.md#enum_TextEdit_SearchFlags) **SEARCH_BACKWARDS** = `4`

Search from end to beginning.

---

<span id="enum_TextEdit_CaretType"></span>

enum **CaretType**: [🔗](class_textedit.md#enum_TextEdit_CaretType)

<span id="class_TextEdit_constant_CARET_TYPE_LINE"></span>

[CaretType](class_textedit.md#enum_TextEdit_CaretType) **CARET_TYPE_LINE** = `0`

Vertical line caret.

<span id="class_TextEdit_constant_CARET_TYPE_BLOCK"></span>

[CaretType](class_textedit.md#enum_TextEdit_CaretType) **CARET_TYPE_BLOCK** = `1`

Block caret.

---

<span id="enum_TextEdit_SelectionMode"></span>

enum **SelectionMode**: [🔗](class_textedit.md#enum_TextEdit_SelectionMode)

<span id="class_TextEdit_constant_SELECTION_MODE_NONE"></span>

[SelectionMode](class_textedit.md#enum_TextEdit_SelectionMode) **SELECTION_MODE_NONE** = `0`

Not selecting.

<span id="class_TextEdit_constant_SELECTION_MODE_SHIFT"></span>

[SelectionMode](class_textedit.md#enum_TextEdit_SelectionMode) **SELECTION_MODE_SHIFT** = `1`

Select as if `shift` is pressed.

<span id="class_TextEdit_constant_SELECTION_MODE_POINTER"></span>

[SelectionMode](class_textedit.md#enum_TextEdit_SelectionMode) **SELECTION_MODE_POINTER** = `2`

Select single characters as if the user single clicked.

<span id="class_TextEdit_constant_SELECTION_MODE_WORD"></span>

[SelectionMode](class_textedit.md#enum_TextEdit_SelectionMode) **SELECTION_MODE_WORD** = `3`

Select whole words as if the user double clicked.

<span id="class_TextEdit_constant_SELECTION_MODE_LINE"></span>

[SelectionMode](class_textedit.md#enum_TextEdit_SelectionMode) **SELECTION_MODE_LINE** = `4`

Select whole lines as if the user triple clicked.

---

<span id="enum_TextEdit_LineWrappingMode"></span>

enum **LineWrappingMode**: [🔗](class_textedit.md#enum_TextEdit_LineWrappingMode)

<span id="class_TextEdit_constant_LINE_WRAPPING_NONE"></span>

[LineWrappingMode](class_textedit.md#enum_TextEdit_LineWrappingMode) **LINE_WRAPPING_NONE** = `0`

Line wrapping is disabled.

<span id="class_TextEdit_constant_LINE_WRAPPING_BOUNDARY"></span>

[LineWrappingMode](class_textedit.md#enum_TextEdit_LineWrappingMode) **LINE_WRAPPING_BOUNDARY** = `1`

Line wrapping occurs at the control boundary, beyond what would normally be visible.

---

<span id="enum_TextEdit_GutterType"></span>

enum **GutterType**: [🔗](class_textedit.md#enum_TextEdit_GutterType)

<span id="class_TextEdit_constant_GUTTER_TYPE_STRING"></span>

[GutterType](class_textedit.md#enum_TextEdit_GutterType) **GUTTER_TYPE_STRING** = `0`

When a gutter is set to string using [set_gutter_type()](class_textedit.md#class_TextEdit_method_set_gutter_type), it is used to contain text set via the [set_line_gutter_text()](class_textedit.md#class_TextEdit_method_set_line_gutter_text) method.

<span id="class_TextEdit_constant_GUTTER_TYPE_ICON"></span>

[GutterType](class_textedit.md#enum_TextEdit_GutterType) **GUTTER_TYPE_ICON** = `1`

When a gutter is set to icon using [set_gutter_type()](class_textedit.md#class_TextEdit_method_set_gutter_type), it is used to contain an icon set via the [set_line_gutter_icon()](class_textedit.md#class_TextEdit_method_set_line_gutter_icon) method.

<span id="class_TextEdit_constant_GUTTER_TYPE_CUSTOM"></span>

[GutterType](class_textedit.md#enum_TextEdit_GutterType) **GUTTER_TYPE_CUSTOM** = `2`

When a gutter is set to custom using [set_gutter_type()](class_textedit.md#class_TextEdit_method_set_gutter_type), it is used to contain custom visuals controlled by a callback method set via the [set_gutter_custom_draw()](class_textedit.md#class_TextEdit_method_set_gutter_custom_draw) method.

---

### Property Descriptions

<span id="class_TextEdit_property_autowrap_mode"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **autowrap_mode** = `3` [🔗](class_textedit.md#class_TextEdit_property_autowrap_mode)

- void **set_autowrap_mode** ( value: [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) )
- [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **get_autowrap_mode** ( )

If [wrap_mode](class_textedit.md#class_TextEdit_property_wrap_mode) is set to [LINE_WRAPPING_BOUNDARY](class_textedit.md#class_TextEdit_constant_LINE_WRAPPING_BOUNDARY), sets text wrapping mode.

---

<span id="class_TextEdit_property_backspace_deletes_composite_character_enabled"></span>

[bool](class_bool.md#class_bool) **backspace_deletes_composite_character_enabled** = `false` [🔗](class_textedit.md#class_TextEdit_property_backspace_deletes_composite_character_enabled)

- void **set_backspace_deletes_composite_character_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_backspace_deletes_composite_character_enabled** ( )

If `true` and [caret_mid_grapheme](class_textedit.md#class_TextEdit_property_caret_mid_grapheme) is `false`, backspace deletes an entire composite character such as ❤️‍🩹, instead of deleting part of the composite character.

---

<span id="class_TextEdit_property_caret_blink"></span>

[bool](class_bool.md#class_bool) **caret_blink** = `false` [🔗](class_textedit.md#class_TextEdit_property_caret_blink)

- void **set_caret_blink_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_caret_blink_enabled** ( )

If `true`, makes the caret blink.

---

<span id="class_TextEdit_property_caret_blink_interval"></span>

[float](class_float.md#class_float) **caret_blink_interval** = `0.65` [🔗](class_textedit.md#class_TextEdit_property_caret_blink_interval)

- void **set_caret_blink_interval** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_caret_blink_interval** ( )

The interval at which the caret blinks (in seconds).

---

<span id="class_TextEdit_property_caret_draw_when_editable_disabled"></span>

[bool](class_bool.md#class_bool) **caret_draw_when_editable_disabled** = `false` [🔗](class_textedit.md#class_TextEdit_property_caret_draw_when_editable_disabled)

- void **set_draw_caret_when_editable_disabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drawing_caret_when_editable_disabled** ( )

If `true`, caret will be visible when [editable](class_textedit.md#class_TextEdit_property_editable) is disabled.

---

<span id="class_TextEdit_property_caret_mid_grapheme"></span>

[bool](class_bool.md#class_bool) **caret_mid_grapheme** = `false` [🔗](class_textedit.md#class_TextEdit_property_caret_mid_grapheme)

- void **set_caret_mid_grapheme_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_caret_mid_grapheme_enabled** ( )

Allow moving caret, selecting and removing the individual composite character components.

 **Note:** :kbd:`Backspace` is always removing individual composite character components.

---

<span id="class_TextEdit_property_caret_move_on_right_click"></span>

[bool](class_bool.md#class_bool) **caret_move_on_right_click** = `true` [🔗](class_textedit.md#class_TextEdit_property_caret_move_on_right_click)

- void **set_move_caret_on_right_click_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_move_caret_on_right_click_enabled** ( )

If `true`, a right-click moves the caret at the mouse position before displaying the context menu.

If `false`, the context menu ignores mouse location.

---

<span id="class_TextEdit_property_caret_multiple"></span>

[bool](class_bool.md#class_bool) **caret_multiple** = `true` [🔗](class_textedit.md#class_TextEdit_property_caret_multiple)

- void **set_multiple_carets_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_multiple_carets_enabled** ( )

If `true`, multiple carets are allowed. Left-clicking with :kbd:`Alt` adds a new caret. See [add_caret()](class_textedit.md#class_TextEdit_method_add_caret) and [get_caret_count()](class_textedit.md#class_TextEdit_method_get_caret_count).

---

<span id="class_TextEdit_property_caret_type"></span>

[CaretType](class_textedit.md#enum_TextEdit_CaretType) **caret_type** = `0` [🔗](class_textedit.md#class_TextEdit_property_caret_type)

- void **set_caret_type** ( value: [CaretType](class_textedit.md#enum_TextEdit_CaretType) )
- [CaretType](class_textedit.md#enum_TextEdit_CaretType) **get_caret_type** ( )

Set the type of caret to draw.

---

<span id="class_TextEdit_property_context_menu_enabled"></span>

[bool](class_bool.md#class_bool) **context_menu_enabled** = `true` [🔗](class_textedit.md#class_TextEdit_property_context_menu_enabled)

- void **set_context_menu_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_context_menu_enabled** ( )

If `true`, a right-click displays the context menu.

---

<span id="class_TextEdit_property_custom_word_separators"></span>

[String](class_string.md#class_String) **custom_word_separators** = `""` [🔗](class_textedit.md#class_TextEdit_property_custom_word_separators)

- void **set_custom_word_separators** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_custom_word_separators** ( )

The characters to consider as word delimiters if [use_custom_word_separators](class_textedit.md#class_TextEdit_property_use_custom_word_separators) is `true`. The characters should be defined without separation, for example `#_!`.

---

<span id="class_TextEdit_property_deselect_on_focus_loss_enabled"></span>

[bool](class_bool.md#class_bool) **deselect_on_focus_loss_enabled** = `true` [🔗](class_textedit.md#class_TextEdit_property_deselect_on_focus_loss_enabled)

- void **set_deselect_on_focus_loss_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_deselect_on_focus_loss_enabled** ( )

If `true`, the selected text will be deselected when focus is lost.

---

<span id="class_TextEdit_property_drag_and_drop_selection_enabled"></span>

[bool](class_bool.md#class_bool) **drag_and_drop_selection_enabled** = `true` [🔗](class_textedit.md#class_TextEdit_property_drag_and_drop_selection_enabled)

- void **set_drag_and_drop_selection_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drag_and_drop_selection_enabled** ( )

If `true`, allow drag and drop of selected text. Text can still be dropped from other sources.

---

<span id="class_TextEdit_property_draw_control_chars"></span>

[bool](class_bool.md#class_bool) **draw_control_chars** = `false` [🔗](class_textedit.md#class_TextEdit_property_draw_control_chars)

- void **set_draw_control_chars** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_draw_control_chars** ( )

If `true`, control characters are displayed.

---

<span id="class_TextEdit_property_draw_spaces"></span>

[bool](class_bool.md#class_bool) **draw_spaces** = `false` [🔗](class_textedit.md#class_TextEdit_property_draw_spaces)

- void **set_draw_spaces** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drawing_spaces** ( )

If `true`, the "space" character will have a visible representation.

---

<span id="class_TextEdit_property_draw_tabs"></span>

[bool](class_bool.md#class_bool) **draw_tabs** = `false` [🔗](class_textedit.md#class_TextEdit_property_draw_tabs)

- void **set_draw_tabs** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drawing_tabs** ( )

If `true`, the "tab" character will have a visible representation.

---

<span id="class_TextEdit_property_editable"></span>

[bool](class_bool.md#class_bool) **editable** = `true` [🔗](class_textedit.md#class_TextEdit_property_editable)

- void **set_editable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editable** ( )

If `false`, existing text cannot be modified and new text cannot be added.

---

<span id="class_TextEdit_property_emoji_menu_enabled"></span>

[bool](class_bool.md#class_bool) **emoji_menu_enabled** = `true` [🔗](class_textedit.md#class_TextEdit_property_emoji_menu_enabled)

- void **set_emoji_menu_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_emoji_menu_enabled** ( )

If `true`, "Emoji and Symbols" menu is enabled.

---

<span id="class_TextEdit_property_empty_selection_clipboard_enabled"></span>

[bool](class_bool.md#class_bool) **empty_selection_clipboard_enabled** = `true` [🔗](class_textedit.md#class_TextEdit_property_empty_selection_clipboard_enabled)

- void **set_empty_selection_clipboard_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_empty_selection_clipboard_enabled** ( )

If `true`, copying or cutting without a selection is performed on all lines with a caret. Otherwise, copy and cut require a selection.

---

<span id="class_TextEdit_property_highlight_all_occurrences"></span>

[bool](class_bool.md#class_bool) **highlight_all_occurrences** = `false` [🔗](class_textedit.md#class_TextEdit_property_highlight_all_occurrences)

- void **set_highlight_all_occurrences** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_highlight_all_occurrences_enabled** ( )

If `true`, all occurrences of the selected text will be highlighted.

---

<span id="class_TextEdit_property_highlight_current_line"></span>

[bool](class_bool.md#class_bool) **highlight_current_line** = `false` [🔗](class_textedit.md#class_TextEdit_property_highlight_current_line)

- void **set_highlight_current_line** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_highlight_current_line_enabled** ( )

If `true`, the line containing the cursor is highlighted.

---

<span id="class_TextEdit_property_indent_wrapped_lines"></span>

[bool](class_bool.md#class_bool) **indent_wrapped_lines** = `false` [🔗](class_textedit.md#class_TextEdit_property_indent_wrapped_lines)

- void **set_indent_wrapped_lines** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_indent_wrapped_lines** ( )

If `true`, all wrapped lines are indented to the same amount as the unwrapped line.

---

<span id="class_TextEdit_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_textedit.md#class_TextEdit_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_TextEdit_property_middle_mouse_paste_enabled"></span>

[bool](class_bool.md#class_bool) **middle_mouse_paste_enabled** = `true` [🔗](class_textedit.md#class_TextEdit_property_middle_mouse_paste_enabled)

- void **set_middle_mouse_paste_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_middle_mouse_paste_enabled** ( )

If `false`, using middle mouse button to paste clipboard will be disabled.

 **Note:** This method is only implemented on Linux.

---

<span id="class_TextEdit_property_minimap_draw"></span>

[bool](class_bool.md#class_bool) **minimap_draw** = `false` [🔗](class_textedit.md#class_TextEdit_property_minimap_draw)

- void **set_draw_minimap** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drawing_minimap** ( )

If `true`, a minimap is shown, providing an outline of your source code. The minimap uses a fixed-width text size.

---

<span id="class_TextEdit_property_minimap_width"></span>

[int](class_int.md#class_int) **minimap_width** = `80` [🔗](class_textedit.md#class_TextEdit_property_minimap_width)

- void **set_minimap_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_minimap_width** ( )

The width, in pixels, of the minimap.

---

<span id="class_TextEdit_property_placeholder_text"></span>

[String](class_string.md#class_String) **placeholder_text** = `""` [🔗](class_textedit.md#class_TextEdit_property_placeholder_text)

- void **set_placeholder** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_placeholder** ( )

Text shown when the **TextEdit** is empty. It is **not** the **TextEdit**'s default value (see [text](class_textedit.md#class_TextEdit_property_text)).

---

<span id="class_TextEdit_property_scroll_fit_content_height"></span>

[bool](class_bool.md#class_bool) **scroll_fit_content_height** = `false` [🔗](class_textedit.md#class_TextEdit_property_scroll_fit_content_height)

- void **set_fit_content_height_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_fit_content_height_enabled** ( )

If `true`, **TextEdit** will disable vertical scroll and fit minimum height to the number of visible lines. When both this property and [scroll_fit_content_width](class_textedit.md#class_TextEdit_property_scroll_fit_content_width) are `true`, no scrollbars will be displayed.

---

<span id="class_TextEdit_property_scroll_fit_content_width"></span>

[bool](class_bool.md#class_bool) **scroll_fit_content_width** = `false` [🔗](class_textedit.md#class_TextEdit_property_scroll_fit_content_width)

- void **set_fit_content_width_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_fit_content_width_enabled** ( )

If `true`, **TextEdit** will disable horizontal scroll and fit minimum width to the widest line in the text. When both this property and [scroll_fit_content_height](class_textedit.md#class_TextEdit_property_scroll_fit_content_height) are `true`, no scrollbars will be displayed.

---

<span id="class_TextEdit_property_scroll_horizontal"></span>

[int](class_int.md#class_int) **scroll_horizontal** = `0` [🔗](class_textedit.md#class_TextEdit_property_scroll_horizontal)

- void **set_h_scroll** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_h_scroll** ( )

If there is a horizontal scrollbar, this determines the current horizontal scroll value in pixels.

---

<span id="class_TextEdit_property_scroll_past_end_of_file"></span>

[bool](class_bool.md#class_bool) **scroll_past_end_of_file** = `false` [🔗](class_textedit.md#class_TextEdit_property_scroll_past_end_of_file)

- void **set_scroll_past_end_of_file_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_scroll_past_end_of_file_enabled** ( )

Allow scrolling past the last line into "virtual" space.

---

<span id="class_TextEdit_property_scroll_smooth"></span>

[bool](class_bool.md#class_bool) **scroll_smooth** = `false` [🔗](class_textedit.md#class_TextEdit_property_scroll_smooth)

- void **set_smooth_scroll_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_smooth_scroll_enabled** ( )

Scroll smoothly over the text rather than jumping to the next location.

---

<span id="class_TextEdit_property_scroll_v_scroll_speed"></span>

[float](class_float.md#class_float) **scroll_v_scroll_speed** = `80.0` [🔗](class_textedit.md#class_TextEdit_property_scroll_v_scroll_speed)

- void **set_v_scroll_speed** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_v_scroll_speed** ( )

Sets the scroll speed with the minimap or when [scroll_smooth](class_textedit.md#class_TextEdit_property_scroll_smooth) is enabled.

---

<span id="class_TextEdit_property_scroll_vertical"></span>

[float](class_float.md#class_float) **scroll_vertical** = `0.0` [🔗](class_textedit.md#class_TextEdit_property_scroll_vertical)

- void **set_v_scroll** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_v_scroll** ( )

If there is a vertical scrollbar, this determines the current vertical scroll value in line numbers, starting at 0 for the top line.

---

<span id="class_TextEdit_property_selecting_enabled"></span>

[bool](class_bool.md#class_bool) **selecting_enabled** = `true` [🔗](class_textedit.md#class_TextEdit_property_selecting_enabled)

- void **set_selecting_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_selecting_enabled** ( )

If `true`, text can be selected.

If `false`, text can not be selected by the user or by the [select()](class_textedit.md#class_TextEdit_method_select) or [select_all()](class_textedit.md#class_TextEdit_method_select_all) methods.

---

<span id="class_TextEdit_property_shortcut_keys_enabled"></span>

[bool](class_bool.md#class_bool) **shortcut_keys_enabled** = `true` [🔗](class_textedit.md#class_TextEdit_property_shortcut_keys_enabled)

- void **set_shortcut_keys_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_shortcut_keys_enabled** ( )

If `true`, shortcut keys for context menu items are enabled, even if the context menu is disabled.

---

<span id="class_TextEdit_property_structured_text_bidi_override"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **structured_text_bidi_override** = `0` [🔗](class_textedit.md#class_TextEdit_property_structured_text_bidi_override)

- void **set_structured_text_bidi_override** ( value: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) )
- [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **get_structured_text_bidi_override** ( )

Set BiDi algorithm override for the structured text.

---

<span id="class_TextEdit_property_structured_text_bidi_override_options"></span>

[Array](class_array.md#class_Array) **structured_text_bidi_override_options** = `[]` [🔗](class_textedit.md#class_TextEdit_property_structured_text_bidi_override_options)

- void **set_structured_text_bidi_override_options** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_structured_text_bidi_override_options** ( )

Set additional options for BiDi override.

---

<span id="class_TextEdit_property_syntax_highlighter"></span>

[SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) **syntax_highlighter** [🔗](class_textedit.md#class_TextEdit_property_syntax_highlighter)

- void **set_syntax_highlighter** ( value: [SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) )
- [SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) **get_syntax_highlighter** ( )

The syntax highlighter to use.

 **Note:** A [SyntaxHighlighter](class_syntaxhighlighter.md#class_SyntaxHighlighter) instance should not be used across multiple **TextEdit** nodes.

---

<span id="class_TextEdit_property_tab_input_mode"></span>

[bool](class_bool.md#class_bool) **tab_input_mode** = `true` [🔗](class_textedit.md#class_TextEdit_property_tab_input_mode)

- void **set_tab_input_mode** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_tab_input_mode** ( )

If `true`, ProjectSettings.input/ui_text_indent input `Tab` character, otherwise it moves keyboard focus to the next [Control](class_control.md#class_Control) in the scene.

---

<span id="class_TextEdit_property_text"></span>

[String](class_string.md#class_String) **text** = `""` [🔗](class_textedit.md#class_TextEdit_property_text)

- void **set_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_text** ( )

String value of the **TextEdit**.

---

<span id="class_TextEdit_property_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **text_direction** = `0` [🔗](class_textedit.md#class_TextEdit_property_text_direction)

- void **set_text_direction** ( value: [TextDirection](class_control.md#enum_Control_TextDirection) )
- [TextDirection](class_control.md#enum_Control_TextDirection) **get_text_direction** ( )

Base text writing direction.

---

<span id="class_TextEdit_property_use_custom_word_separators"></span>

[bool](class_bool.md#class_bool) **use_custom_word_separators** = `false` [🔗](class_textedit.md#class_TextEdit_property_use_custom_word_separators)

- void **set_use_custom_word_separators** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_custom_word_separators_enabled** ( )

If `false`, using :kbd:`Ctrl + Left` or :kbd:`Ctrl + Right` (:kbd:`Cmd + Left` or :kbd:`Cmd + Right` on macOS) bindings will use the behavior of [use_default_word_separators](class_textedit.md#class_TextEdit_property_use_default_word_separators). If `true`, it will also stop the caret if a character within [custom_word_separators](class_textedit.md#class_TextEdit_property_custom_word_separators) is detected. Useful for subword moving. This behavior also will be applied to the behavior of text selection.

---

<span id="class_TextEdit_property_use_default_word_separators"></span>

[bool](class_bool.md#class_bool) **use_default_word_separators** = `true` [🔗](class_textedit.md#class_TextEdit_property_use_default_word_separators)

- void **set_use_default_word_separators** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_default_word_separators_enabled** ( )

If `false`, using :kbd:`Ctrl + Left` or :kbd:`Ctrl + Right` (:kbd:`Cmd + Left` or :kbd:`Cmd + Right` on macOS) bindings will stop moving caret only if a space or punctuation is detected. If `true`, it will also stop the caret if a character is part of ``!"#$%&'()*+,-./:;<=>?@[\]^`{|}~``, the Unicode General Punctuation table, or the Unicode CJK Punctuation table. Useful for subword moving. This behavior also will be applied to the behavior of text selection.

---

<span id="class_TextEdit_property_virtual_keyboard_enabled"></span>

[bool](class_bool.md#class_bool) **virtual_keyboard_enabled** = `true` [🔗](class_textedit.md#class_TextEdit_property_virtual_keyboard_enabled)

- void **set_virtual_keyboard_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_virtual_keyboard_enabled** ( )

If `true`, the native virtual keyboard is enabled on platforms that support it.

---

<span id="class_TextEdit_property_virtual_keyboard_show_on_focus"></span>

[bool](class_bool.md#class_bool) **virtual_keyboard_show_on_focus** = `true` [🔗](class_textedit.md#class_TextEdit_property_virtual_keyboard_show_on_focus)

- void **set_virtual_keyboard_show_on_focus** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_virtual_keyboard_show_on_focus** ( )

If `true`, the native virtual keyboard is shown on focus events on platforms that support it.

---

<span id="class_TextEdit_property_wrap_mode"></span>

[LineWrappingMode](class_textedit.md#enum_TextEdit_LineWrappingMode) **wrap_mode** = `0` [🔗](class_textedit.md#class_TextEdit_property_wrap_mode)

- void **set_line_wrapping_mode** ( value: [LineWrappingMode](class_textedit.md#enum_TextEdit_LineWrappingMode) )
- [LineWrappingMode](class_textedit.md#enum_TextEdit_LineWrappingMode) **get_line_wrapping_mode** ( )

Sets the line wrapping mode to use.

---

### Method Descriptions

<span id="class_TextEdit_private_method__backspace"></span>

void **_backspace** ( caret_index: [int](class_int.md#class_int) ) *virtual* [🔗](class_textedit.md#class_TextEdit_private_method__backspace)

Override this method to define what happens when the user presses the backspace key.

---

<span id="class_TextEdit_private_method__copy"></span>

void **_copy** ( caret_index: [int](class_int.md#class_int) ) *virtual* [🔗](class_textedit.md#class_TextEdit_private_method__copy)

Override this method to define what happens when the user performs a copy operation.

---

<span id="class_TextEdit_private_method__cut"></span>

void **_cut** ( caret_index: [int](class_int.md#class_int) ) *virtual* [🔗](class_textedit.md#class_TextEdit_private_method__cut)

Override this method to define what happens when the user performs a cut operation.

---

<span id="class_TextEdit_private_method__handle_unicode_input"></span>

void **_handle_unicode_input** ( unicode_char: [int](class_int.md#class_int), caret_index: [int](class_int.md#class_int) ) *virtual* [🔗](class_textedit.md#class_TextEdit_private_method__handle_unicode_input)

Override this method to define what happens when the user types in the provided key `unicode_char`.

---

<span id="class_TextEdit_private_method__paste"></span>

void **_paste** ( caret_index: [int](class_int.md#class_int) ) *virtual* [🔗](class_textedit.md#class_TextEdit_private_method__paste)

Override this method to define what happens when the user performs a paste operation.

---

<span id="class_TextEdit_private_method__paste_primary_clipboard"></span>

void **_paste_primary_clipboard** ( caret_index: [int](class_int.md#class_int) ) *virtual* [🔗](class_textedit.md#class_TextEdit_private_method__paste_primary_clipboard)

Override this method to define what happens when the user performs a paste operation with middle mouse button.

 **Note:** This method is only implemented on Linux.

---

<span id="class_TextEdit_method_add_caret"></span>

[int](class_int.md#class_int) **add_caret** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_add_caret)

Adds a new caret at the given location. Returns the index of the new caret, or `-1` if the location is invalid.

---

<span id="class_TextEdit_method_add_caret_at_carets"></span>

void **add_caret_at_carets** ( below: [bool](class_bool.md#class_bool) ) [🔗](class_textedit.md#class_TextEdit_method_add_caret_at_carets)

Adds an additional caret above or below every caret. If `below` is `true` the new caret will be added below and above otherwise.

---

<span id="class_TextEdit_method_add_gutter"></span>

void **add_gutter** ( at: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_add_gutter)

Register a new gutter to this **TextEdit**. Use `at` to have a specific gutter order. A value of `-1` appends the gutter to the right.

---

<span id="class_TextEdit_method_add_selection_for_next_occurrence"></span>

void **add_selection_for_next_occurrence** ( ) [🔗](class_textedit.md#class_TextEdit_method_add_selection_for_next_occurrence)

Adds a selection and a caret for the next occurrence of the current selection. If there is no active selection, selects word under caret.

---

<span id="class_TextEdit_method_adjust_carets_after_edit"></span>

void **adjust_carets_after_edit** ( caret: [int](class_int.md#class_int), from_line: [int](class_int.md#class_int), from_col: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int), to_col: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_adjust_carets_after_edit)

**Deprecated:** No longer necessary since methods now adjust carets themselves.

This method does nothing.

---

<span id="class_TextEdit_method_adjust_viewport_to_caret"></span>

void **adjust_viewport_to_caret** ( caret_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_adjust_viewport_to_caret)

Adjust the viewport so the caret is visible.

---

<span id="class_TextEdit_method_apply_ime"></span>

void **apply_ime** ( ) [🔗](class_textedit.md#class_TextEdit_method_apply_ime)

Applies text from the Input Method Editor (IME) to each caret and closes the IME if it is open.

---

<span id="class_TextEdit_method_backspace"></span>

void **backspace** ( caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_backspace)

Called when the user presses the backspace key. Can be overridden with [_backspace()](class_textedit.md#class_TextEdit_private_method__backspace).

---

<span id="class_TextEdit_method_begin_complex_operation"></span>

void **begin_complex_operation** ( ) [🔗](class_textedit.md#class_TextEdit_method_begin_complex_operation)

Starts a multipart edit. All edits will be treated as one action until [end_complex_operation()](class_textedit.md#class_TextEdit_method_end_complex_operation) is called.

---

<span id="class_TextEdit_method_begin_multicaret_edit"></span>

void **begin_multicaret_edit** ( ) [🔗](class_textedit.md#class_TextEdit_method_begin_multicaret_edit)

Starts an edit for multiple carets. The edit must be ended with [end_multicaret_edit()](class_textedit.md#class_TextEdit_method_end_multicaret_edit). Multicaret edits can be used to edit text at multiple carets and delay merging the carets until the end, so the caret indexes aren't affected immediately. [begin_multicaret_edit()](class_textedit.md#class_TextEdit_method_begin_multicaret_edit) and [end_multicaret_edit()](class_textedit.md#class_TextEdit_method_end_multicaret_edit) can be nested, and the merge will happen at the last [end_multicaret_edit()](class_textedit.md#class_TextEdit_method_end_multicaret_edit).

::

    begin_complex_operation()
    begin_multicaret_edit()
    for i in range(get_caret_count()):
        if multicaret_edit_ignore_caret(i):
            continue
        # Logic here.
    end_multicaret_edit()
    end_complex_operation()

---

<span id="class_TextEdit_method_cancel_ime"></span>

void **cancel_ime** ( ) [🔗](class_textedit.md#class_TextEdit_method_cancel_ime)

Closes the Input Method Editor (IME) if it is open. Any text in the IME will be lost.

---

<span id="class_TextEdit_method_center_viewport_to_caret"></span>

void **center_viewport_to_caret** ( caret_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_center_viewport_to_caret)

Centers the viewport on the line the editing caret is at. This also resets the [scroll_horizontal](class_textedit.md#class_TextEdit_property_scroll_horizontal) value to `0`.

---

<span id="class_TextEdit_method_clear"></span>

void **clear** ( ) [🔗](class_textedit.md#class_TextEdit_method_clear)

Performs a full reset of **TextEdit**, including undo history.

---

<span id="class_TextEdit_method_clear_undo_history"></span>

void **clear_undo_history** ( ) [🔗](class_textedit.md#class_TextEdit_method_clear_undo_history)

Clears the undo history.

---

<span id="class_TextEdit_method_collapse_carets"></span>

void **collapse_carets** ( from_line: [int](class_int.md#class_int), from_column: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int), to_column: [int](class_int.md#class_int), inclusive: [bool](class_bool.md#class_bool) = false ) [🔗](class_textedit.md#class_TextEdit_method_collapse_carets)

Collapse all carets in the given range to the `from_line` and `from_column` position.

 `inclusive` applies to both ends.

If [is_in_mulitcaret_edit()](class_textedit.md#class_TextEdit_method_is_in_mulitcaret_edit) is `true`, carets that are collapsed will be `true` for [multicaret_edit_ignore_caret()](class_textedit.md#class_TextEdit_method_multicaret_edit_ignore_caret).

 [merge_overlapping_carets()](class_textedit.md#class_TextEdit_method_merge_overlapping_carets) will be called if any carets were collapsed.

---

<span id="class_TextEdit_method_copy"></span>

void **copy** ( caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_copy)

Copies the current text selection. Can be overridden with [_copy()](class_textedit.md#class_TextEdit_private_method__copy).

---

<span id="class_TextEdit_method_cut"></span>

void **cut** ( caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_cut)

Cut's the current selection. Can be overridden with [_cut()](class_textedit.md#class_TextEdit_private_method__cut).

---

<span id="class_TextEdit_method_delete_selection"></span>

void **delete_selection** ( caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_delete_selection)

Deletes the selected text.

---

<span id="class_TextEdit_method_deselect"></span>

void **deselect** ( caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_deselect)

Deselects the current selection.

---

<span id="class_TextEdit_method_end_action"></span>

void **end_action** ( ) [🔗](class_textedit.md#class_TextEdit_method_end_action)

Marks the end of steps in the current action started with [start_action()](class_textedit.md#class_TextEdit_method_start_action).

---

<span id="class_TextEdit_method_end_complex_operation"></span>

void **end_complex_operation** ( ) [🔗](class_textedit.md#class_TextEdit_method_end_complex_operation)

Ends a multipart edit, started with [begin_complex_operation()](class_textedit.md#class_TextEdit_method_begin_complex_operation). If called outside a complex operation, the current operation is pushed onto the undo/redo stack.

---

<span id="class_TextEdit_method_end_multicaret_edit"></span>

void **end_multicaret_edit** ( ) [🔗](class_textedit.md#class_TextEdit_method_end_multicaret_edit)

Ends an edit for multiple carets, that was started with [begin_multicaret_edit()](class_textedit.md#class_TextEdit_method_begin_multicaret_edit). If this was the last [end_multicaret_edit()](class_textedit.md#class_TextEdit_method_end_multicaret_edit) and [merge_overlapping_carets()](class_textedit.md#class_TextEdit_method_merge_overlapping_carets) was called, carets will be merged.

---

<span id="class_TextEdit_method_get_caret_column"></span>

[int](class_int.md#class_int) **get_caret_column** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_caret_column)

Returns the column the editing caret is at.

---

<span id="class_TextEdit_method_get_caret_count"></span>

[int](class_int.md#class_int) **get_caret_count** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_caret_count)

Returns the number of carets in this **TextEdit**.

---

<span id="class_TextEdit_method_get_caret_draw_pos"></span>

[Vector2](class_vector2.md#class_Vector2) **get_caret_draw_pos** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_caret_draw_pos)

Returns the caret pixel draw position.

---

<span id="class_TextEdit_method_get_caret_index_edit_order"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_caret_index_edit_order** ( ) [🔗](class_textedit.md#class_TextEdit_method_get_caret_index_edit_order)

**Deprecated:** Carets no longer need to be edited in any specific order. If the carets need to be sorted, use [get_sorted_carets()](class_textedit.md#class_TextEdit_method_get_sorted_carets) instead.

Returns a list of caret indexes in their edit order, this done from bottom to top. Edit order refers to the way actions such as [insert_text_at_caret()](class_textedit.md#class_TextEdit_method_insert_text_at_caret) are applied.

---

<span id="class_TextEdit_method_get_caret_line"></span>

[int](class_int.md#class_int) **get_caret_line** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_caret_line)

Returns the line the editing caret is on.

---

<span id="class_TextEdit_method_get_caret_wrap_index"></span>

[int](class_int.md#class_int) **get_caret_wrap_index** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_caret_wrap_index)

Returns the wrap index the editing caret is on.

---

<span id="class_TextEdit_method_get_first_non_whitespace_column"></span>

[int](class_int.md#class_int) **get_first_non_whitespace_column** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_first_non_whitespace_column)

Returns the first column containing a non-whitespace character on the given line. If there is only whitespace, returns the number of characters.

---

<span id="class_TextEdit_method_get_first_visible_line"></span>

[int](class_int.md#class_int) **get_first_visible_line** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_first_visible_line)

Returns the first visible line.

---

<span id="class_TextEdit_method_get_gutter_count"></span>

[int](class_int.md#class_int) **get_gutter_count** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_gutter_count)

Returns the number of gutters registered.

---

<span id="class_TextEdit_method_get_gutter_name"></span>

[String](class_string.md#class_String) **get_gutter_name** ( gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_gutter_name)

Returns the name of the gutter at the given index.

---

<span id="class_TextEdit_method_get_gutter_type"></span>

[GutterType](class_textedit.md#enum_TextEdit_GutterType) **get_gutter_type** ( gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_gutter_type)

Returns the type of the gutter at the given index. Gutters can contain icons, text, or custom visuals.

---

<span id="class_TextEdit_method_get_gutter_width"></span>

[int](class_int.md#class_int) **get_gutter_width** ( gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_gutter_width)

Returns the width of the gutter at the given index.

---

<span id="class_TextEdit_method_get_h_scroll_bar"></span>

[HScrollBar](class_hscrollbar.md#class_HScrollBar) **get_h_scroll_bar** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_h_scroll_bar)

Returns the [HScrollBar](class_hscrollbar.md#class_HScrollBar) used by **TextEdit**.

---

<span id="class_TextEdit_method_get_indent_level"></span>

[int](class_int.md#class_int) **get_indent_level** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_indent_level)

Returns the indent level of the given line. This is the number of spaces and tabs at the beginning of the line, with the tabs taking the tab size into account (see [get_tab_size()](class_textedit.md#class_TextEdit_method_get_tab_size)).

---

<span id="class_TextEdit_method_get_last_full_visible_line"></span>

[int](class_int.md#class_int) **get_last_full_visible_line** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_last_full_visible_line)

Returns the last visible line. Use [get_last_full_visible_line_wrap_index()](class_textedit.md#class_TextEdit_method_get_last_full_visible_line_wrap_index) for the wrap index.

---

<span id="class_TextEdit_method_get_last_full_visible_line_wrap_index"></span>

[int](class_int.md#class_int) **get_last_full_visible_line_wrap_index** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_last_full_visible_line_wrap_index)

Returns the last visible wrap index of the last visible line.

---

<span id="class_TextEdit_method_get_last_unhidden_line"></span>

[int](class_int.md#class_int) **get_last_unhidden_line** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_last_unhidden_line)

Returns the last unhidden line in the entire **TextEdit**.

---

<span id="class_TextEdit_method_get_line"></span>

[String](class_string.md#class_String) **get_line** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line)

Returns the text of a specific line.

---

<span id="class_TextEdit_method_get_line_background_color"></span>

[Color](class_color.md#class_Color) **get_line_background_color** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_background_color)

Returns the custom background color of the given line. If no color is set, returns `Color(0, 0, 0, 0)`.

---

<span id="class_TextEdit_method_get_line_column_at_pos"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_line_column_at_pos** ( position: [Vector2i](class_vector2i.md#class_Vector2i), clamp_line: [bool](class_bool.md#class_bool) = true, clamp_column: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_column_at_pos)

Returns the line and column at the given position. In the returned vector, `x` is the column and `y` is the line.

If `clamp_line` is `false` and `position` is below the last line, `Vector2i(-1, -1)` is returned.

If `clamp_column` is `false` and `position` is outside the column range of the line, `Vector2i(-1, -1)` is returned.

---

<span id="class_TextEdit_method_get_line_count"></span>

[int](class_int.md#class_int) **get_line_count** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_count)

Returns the number of lines in the text.

---

<span id="class_TextEdit_method_get_line_gutter_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_line_gutter_icon** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_gutter_icon)

Returns the icon currently in `gutter` at `line`. This only works when the gutter type is [GUTTER_TYPE_ICON](class_textedit.md#class_TextEdit_constant_GUTTER_TYPE_ICON) (see [set_gutter_type()](class_textedit.md#class_TextEdit_method_set_gutter_type)).

---

<span id="class_TextEdit_method_get_line_gutter_item_color"></span>

[Color](class_color.md#class_Color) **get_line_gutter_item_color** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_gutter_item_color)

Returns the color currently in `gutter` at `line`.

---

<span id="class_TextEdit_method_get_line_gutter_metadata"></span>

[Variant](class_variant.md#class_Variant) **get_line_gutter_metadata** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_gutter_metadata)

Returns the metadata currently in `gutter` at `line`.

---

<span id="class_TextEdit_method_get_line_gutter_text"></span>

[String](class_string.md#class_String) **get_line_gutter_text** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_gutter_text)

Returns the text currently in `gutter` at `line`. This only works when the gutter type is [GUTTER_TYPE_STRING](class_textedit.md#class_TextEdit_constant_GUTTER_TYPE_STRING) (see [set_gutter_type()](class_textedit.md#class_TextEdit_method_set_gutter_type)).

---

<span id="class_TextEdit_method_get_line_height"></span>

[int](class_int.md#class_int) **get_line_height** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_height)

Returns the maximum value of the line height among all lines.

 **Note:** The return value is influenced by [line_spacing](class_textedit.md#class_TextEdit_theme_constant_line_spacing) and [font_size](class_textedit.md#class_TextEdit_theme_font_size_font_size). And it will not be less than `1`.

---

<span id="class_TextEdit_method_get_line_ranges_from_carets"></span>

[Array](class_array.md#class_Array)\[[Vector2i](class_vector2i.md#class_Vector2i)\] **get_line_ranges_from_carets** ( only_selections: [bool](class_bool.md#class_bool) = false, merge_adjacent: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_ranges_from_carets)

Returns an [Array](class_array.md#class_Array) of line ranges where `x` is the first line and `y` is the last line. All lines within these ranges will have a caret on them or be part of a selection. Each line will only be part of one line range, even if it has multiple carets on it.

If a selection's end column ([get_selection_to_column()](class_textedit.md#class_TextEdit_method_get_selection_to_column)) is at column `0`, that line will not be included. If a selection begins on the line after another selection ends and `merge_adjacent` is `true`, or they begin and end on the same line, one line range will include both selections.

---

<span id="class_TextEdit_method_get_line_width"></span>

[int](class_int.md#class_int) **get_line_width** ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_width)

Returns the width in pixels of the `wrap_index` on `line`.

---

<span id="class_TextEdit_method_get_line_with_ime"></span>

[String](class_string.md#class_String) **get_line_with_ime** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_with_ime)

Returns line text as it is currently displayed, including IME composition string.

---

<span id="class_TextEdit_method_get_line_wrap_count"></span>

[int](class_int.md#class_int) **get_line_wrap_count** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_wrap_count)

Returns the number of times the given line is wrapped.

---

<span id="class_TextEdit_method_get_line_wrap_index_at_column"></span>

[int](class_int.md#class_int) **get_line_wrap_index_at_column** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_wrap_index_at_column)

Returns the wrap index of the given column on the given line. This ranges from `0` to [get_line_wrap_count()](class_textedit.md#class_TextEdit_method_get_line_wrap_count).

---

<span id="class_TextEdit_method_get_line_wrapped_text"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_line_wrapped_text** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_line_wrapped_text)

Returns an array of [String](class_string.md#class_String) s representing each wrapped index.

---

<span id="class_TextEdit_method_get_local_mouse_pos"></span>

[Vector2](class_vector2.md#class_Vector2) **get_local_mouse_pos** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_local_mouse_pos)

Returns the local mouse position adjusted for the text direction.

---

<span id="class_TextEdit_method_get_menu"></span>

[PopupMenu](class_popupmenu.md#class_PopupMenu) **get_menu** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_menu)

Returns the [PopupMenu](class_popupmenu.md#class_PopupMenu) of this **TextEdit**. By default, this menu is displayed when right-clicking on the **TextEdit**.

You can add custom menu items or remove standard ones. Make sure your IDs don't conflict with the standard ones (see [MenuItems](class_textedit.md#enum_TextEdit_MenuItems)). For example:

.. tabs::

```
```

    func _ready():
        var menu = get_menu()
        # Remove all items after "Redo".
        menu.item_count = menu.get_item_index(MENU_REDO) + 1
        # Add custom items.
        menu.add_separator()
        menu.add_item("Insert Date", MENU_MAX + 1)
        # Connect callback.
        menu.id_pressed.connect(_on_item_pressed)

    func _on_item_pressed(id):
        if id == MENU_MAX + 1:
            insert_text_at_caret(Time.get_date_string_from_system())

```
```

    public override void _Ready()
    {
        var menu = GetMenu();
        // Remove all items after "Redo".
        menu.ItemCount = menu.GetItemIndex(TextEdit.MenuItems.Redo) + 1;
        // Add custom items.
        menu.AddSeparator();
        menu.AddItem("Insert Date", TextEdit.MenuItems.Max + 1);
        // Add event handler.
        menu.IdPressed += OnItemPressed;
    }

    public void OnItemPressed(int id)
    {
        if (id == TextEdit.MenuItems.Max + 1)
        {
            InsertTextAtCaret(Time.GetDateStringFromSystem());
        }
    }

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class_Window_property_visible) property.

---

<span id="class_TextEdit_method_get_minimap_line_at_pos"></span>

[int](class_int.md#class_int) **get_minimap_line_at_pos** ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_minimap_line_at_pos)

Returns the equivalent minimap line at `position`.

---

<span id="class_TextEdit_method_get_minimap_visible_lines"></span>

[int](class_int.md#class_int) **get_minimap_visible_lines** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_minimap_visible_lines)

Returns the number of lines that may be drawn on the minimap.

---

<span id="class_TextEdit_method_get_next_composite_character_column"></span>

[int](class_int.md#class_int) **get_next_composite_character_column** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_next_composite_character_column)

Returns the correct column at the end of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the start of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

 **Note:** To check at caret location use `get_next_composite_character_column(get_caret_line(), get_caret_column())`

---

<span id="class_TextEdit_method_get_next_visible_line_index_offset_from"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_next_visible_line_index_offset_from** ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int), visible_amount: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_next_visible_line_index_offset_from)

Similar to [get_next_visible_line_offset_from()](class_textedit.md#class_TextEdit_method_get_next_visible_line_offset_from), but takes into account the line wrap indexes. In the returned vector, `x` is the line, `y` is the wrap index.

---

<span id="class_TextEdit_method_get_next_visible_line_offset_from"></span>

[int](class_int.md#class_int) **get_next_visible_line_offset_from** ( line: [int](class_int.md#class_int), visible_amount: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_next_visible_line_offset_from)

Returns the count to the next visible line from `line` to `line + visible_amount`. Can also count backwards. For example if a **TextEdit** has 5 lines with lines 2 and 3 hidden, calling this with `line = 1, visible_amount = 1` would return 3.

---

<span id="class_TextEdit_method_get_pos_at_line_column"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_pos_at_line_column** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_pos_at_line_column)

Returns the local position for the given `line` and `column`. If `x` or `y` of the returned vector equal `-1`, the position is outside of the viewable area of the control.

 **Note:** The Y position corresponds to the bottom side of the line. Use [get_rect_at_line_column()](class_textedit.md#class_TextEdit_method_get_rect_at_line_column) to get the top side position.

---

<span id="class_TextEdit_method_get_previous_composite_character_column"></span>

[int](class_int.md#class_int) **get_previous_composite_character_column** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_previous_composite_character_column)

Returns the correct column at the start of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the end of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

 **Note:** To check at caret location use `get_previous_composite_character_column(get_caret_line(), get_caret_column())`

---

<span id="class_TextEdit_method_get_rect_at_line_column"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **get_rect_at_line_column** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_rect_at_line_column)

Returns the local position and size for the grapheme at the given `line` and `column`. If `x` or `y` position of the returned rect equal `-1`, the position is outside of the viewable area of the control.

 **Note:** The Y position of the returned rect corresponds to the top side of the line, unlike [get_pos_at_line_column()](class_textedit.md#class_TextEdit_method_get_pos_at_line_column) which returns the bottom side.

---

<span id="class_TextEdit_method_get_saved_version"></span>

[int](class_int.md#class_int) **get_saved_version** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_saved_version)

Returns the last tagged saved version from [tag_saved_version()](class_textedit.md#class_TextEdit_method_tag_saved_version).

---

<span id="class_TextEdit_method_get_scroll_pos_for_line"></span>

[float](class_float.md#class_float) **get_scroll_pos_for_line** ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_scroll_pos_for_line)

Returns the scroll position for `wrap_index` of `line`.

---

<span id="class_TextEdit_method_get_selected_text"></span>

[String](class_string.md#class_String) **get_selected_text** ( caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_get_selected_text)

Returns the text inside the selection of a caret, or all the carets if `caret_index` is its default value `-1`.

---

<span id="class_TextEdit_method_get_selection_at_line_column"></span>

[int](class_int.md#class_int) **get_selection_at_line_column** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int), include_edges: [bool](class_bool.md#class_bool) = true, only_selections: [bool](class_bool.md#class_bool) = true ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_at_line_column)

Returns the caret index of the selection at the given `line` and `column`, or `-1` if there is none.

If `include_edges` is `false`, the position must be inside the selection and not at either end. If `only_selections` is `false`, carets without a selection will also be considered.

---

<span id="class_TextEdit_method_get_selection_column"></span>

[int](class_int.md#class_int) **get_selection_column** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_column)

**Deprecated:** Use [get_selection_origin_column()](class_textedit.md#class_TextEdit_method_get_selection_origin_column) instead.

Returns the original start column of the selection.

---

<span id="class_TextEdit_method_get_selection_from_column"></span>

[int](class_int.md#class_int) **get_selection_from_column** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_from_column)

Returns the selection begin column. Returns the caret column if there is no selection.

---

<span id="class_TextEdit_method_get_selection_from_line"></span>

[int](class_int.md#class_int) **get_selection_from_line** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_from_line)

Returns the selection begin line. Returns the caret line if there is no selection.

---

<span id="class_TextEdit_method_get_selection_line"></span>

[int](class_int.md#class_int) **get_selection_line** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_line)

**Deprecated:** Use [get_selection_origin_line()](class_textedit.md#class_TextEdit_method_get_selection_origin_line) instead.

Returns the original start line of the selection.

---

<span id="class_TextEdit_method_get_selection_mode"></span>

[SelectionMode](class_textedit.md#enum_TextEdit_SelectionMode) **get_selection_mode** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_mode)

Returns the current selection mode.

---

<span id="class_TextEdit_method_get_selection_origin_column"></span>

[int](class_int.md#class_int) **get_selection_origin_column** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_origin_column)

Returns the origin column of the selection. This is the opposite end from the caret.

---

<span id="class_TextEdit_method_get_selection_origin_line"></span>

[int](class_int.md#class_int) **get_selection_origin_line** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_origin_line)

Returns the origin line of the selection. This is the opposite end from the caret.

---

<span id="class_TextEdit_method_get_selection_to_column"></span>

[int](class_int.md#class_int) **get_selection_to_column** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_to_column)

Returns the selection end column. Returns the caret column if there is no selection.

---

<span id="class_TextEdit_method_get_selection_to_line"></span>

[int](class_int.md#class_int) **get_selection_to_line** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_selection_to_line)

Returns the selection end line. Returns the caret line if there is no selection.

---

<span id="class_TextEdit_method_get_sorted_carets"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_sorted_carets** ( include_ignored_carets: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_sorted_carets)

Returns the carets sorted by selection beginning from lowest line and column to highest (from top to bottom of text).

If `include_ignored_carets` is `false`, carets from [multicaret_edit_ignore_caret()](class_textedit.md#class_TextEdit_method_multicaret_edit_ignore_caret) will be ignored.

---

<span id="class_TextEdit_method_get_tab_size"></span>

[int](class_int.md#class_int) **get_tab_size** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_tab_size)

Returns the **TextEdit**'s' tab size.

---

<span id="class_TextEdit_method_get_total_gutter_width"></span>

[int](class_int.md#class_int) **get_total_gutter_width** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_total_gutter_width)

Returns the total width of all gutters and internal padding.

---

<span id="class_TextEdit_method_get_total_visible_line_count"></span>

[int](class_int.md#class_int) **get_total_visible_line_count** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_total_visible_line_count)

Returns the total number of lines in the text. This includes wrapped lines and excludes folded lines. If [wrap_mode](class_textedit.md#class_TextEdit_property_wrap_mode) is set to [LINE_WRAPPING_NONE](class_textedit.md#class_TextEdit_constant_LINE_WRAPPING_NONE) and no lines are folded (see [CodeEdit.is_line_folded()](class_codeedit.md#class_CodeEdit_method_is_line_folded)) then this is equivalent to [get_line_count()](class_textedit.md#class_TextEdit_method_get_line_count). See [get_visible_line_count_in_range()](class_textedit.md#class_TextEdit_method_get_visible_line_count_in_range) for a limited range of lines.

---

<span id="class_TextEdit_method_get_v_scroll_bar"></span>

[VScrollBar](class_vscrollbar.md#class_VScrollBar) **get_v_scroll_bar** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_v_scroll_bar)

Returns the [VScrollBar](class_vscrollbar.md#class_VScrollBar) of the **TextEdit**.

---

<span id="class_TextEdit_method_get_version"></span>

[int](class_int.md#class_int) **get_version** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_version)

Returns the current version of the **TextEdit**. The version is a count of recorded operations by the undo/redo history.

---

<span id="class_TextEdit_method_get_visible_line_count"></span>

[int](class_int.md#class_int) **get_visible_line_count** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_visible_line_count)

Returns the number of lines that can visually fit, rounded down, based on this control's height.

---

<span id="class_TextEdit_method_get_visible_line_count_in_range"></span>

[int](class_int.md#class_int) **get_visible_line_count_in_range** ( from_line: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_visible_line_count_in_range)

Returns the total number of lines between `from_line` and `to_line` (inclusive) in the text. This includes wrapped lines and excludes folded lines. If the range covers all lines it is equivalent to [get_total_visible_line_count()](class_textedit.md#class_TextEdit_method_get_total_visible_line_count).

---

<span id="class_TextEdit_method_get_word_at_pos"></span>

[String](class_string.md#class_String) **get_word_at_pos** ( position: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_word_at_pos)

Returns the word at `position`.

---

<span id="class_TextEdit_method_get_word_under_caret"></span>

[String](class_string.md#class_String) **get_word_under_caret** ( caret_index: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_textedit.md#class_TextEdit_method_get_word_under_caret)

Returns a [String](class_string.md#class_String) text with the word under the caret's location.

---

<span id="class_TextEdit_method_has_ime_text"></span>

[bool](class_bool.md#class_bool) **has_ime_text** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_has_ime_text)

Returns `true` if the user has text in the Input Method Editor (IME).

---

<span id="class_TextEdit_method_has_redo"></span>

[bool](class_bool.md#class_bool) **has_redo** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_has_redo)

Returns `true` if a "redo" action is available.

---

<span id="class_TextEdit_method_has_selection"></span>

[bool](class_bool.md#class_bool) **has_selection** ( caret_index: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_textedit.md#class_TextEdit_method_has_selection)

Returns `true` if the user has selected text.

---

<span id="class_TextEdit_method_has_undo"></span>

[bool](class_bool.md#class_bool) **has_undo** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_has_undo)

Returns `true` if an "undo" action is available.

---

<span id="class_TextEdit_method_insert_line_at"></span>

void **insert_line_at** ( line: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) [🔗](class_textedit.md#class_TextEdit_method_insert_line_at)

Inserts a new line with `text` at `line`.

---

<span id="class_TextEdit_method_insert_text"></span>

void **insert_text** ( text: [String](class_string.md#class_String), line: [int](class_int.md#class_int), column: [int](class_int.md#class_int), before_selection_begin: [bool](class_bool.md#class_bool) = true, before_selection_end: [bool](class_bool.md#class_bool) = false ) [🔗](class_textedit.md#class_TextEdit_method_insert_text)

Inserts the `text` at `line` and `column`.

If `before_selection_begin` is `true`, carets and selections that begin at `line` and `column` will moved to the end of the inserted text, along with all carets after it.

If `before_selection_end` is `true`, selections that end at `line` and `column` will be extended to the end of the inserted text. These parameters can be used to insert text inside of or outside of selections.

---

<span id="class_TextEdit_method_insert_text_at_caret"></span>

void **insert_text_at_caret** ( text: [String](class_string.md#class_String), caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_insert_text_at_caret)

Insert the specified text at the caret position.

---

<span id="class_TextEdit_method_is_caret_after_selection_origin"></span>

[bool](class_bool.md#class_bool) **is_caret_after_selection_origin** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_caret_after_selection_origin)

Returns `true` if the caret of the selection is after the selection origin. This can be used to determine the direction of the selection.

---

<span id="class_TextEdit_method_is_caret_visible"></span>

[bool](class_bool.md#class_bool) **is_caret_visible** ( caret_index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_caret_visible)

Returns `true` if the caret is visible, `false` otherwise. A caret will be considered hidden if it is outside the scrollable area when scrolling is enabled.

 **Note:** [is_caret_visible()](class_textedit.md#class_TextEdit_method_is_caret_visible) does not account for a caret being off-screen if it is still within the scrollable area. It will return `true` even if the caret is off-screen as long as it meets **TextEdit**'s own conditions for being visible. This includes uses of [scroll_fit_content_width](class_textedit.md#class_TextEdit_property_scroll_fit_content_width) and [scroll_fit_content_height](class_textedit.md#class_TextEdit_property_scroll_fit_content_height) that cause the **TextEdit** to expand beyond the viewport's bounds.

---

<span id="class_TextEdit_method_is_dragging_cursor"></span>

[bool](class_bool.md#class_bool) **is_dragging_cursor** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_dragging_cursor)

Returns `true` if the user is dragging their mouse for scrolling, selecting, or text dragging.

---

<span id="class_TextEdit_method_is_gutter_clickable"></span>

[bool](class_bool.md#class_bool) **is_gutter_clickable** ( gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_gutter_clickable)

Returns `true` if the gutter at the given index is clickable. See [set_gutter_clickable()](class_textedit.md#class_TextEdit_method_set_gutter_clickable).

---

<span id="class_TextEdit_method_is_gutter_drawn"></span>

[bool](class_bool.md#class_bool) **is_gutter_drawn** ( gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_gutter_drawn)

Returns `true` if the gutter at the given index is currently drawn. See [set_gutter_draw()](class_textedit.md#class_TextEdit_method_set_gutter_draw).

---

<span id="class_TextEdit_method_is_gutter_overwritable"></span>

[bool](class_bool.md#class_bool) **is_gutter_overwritable** ( gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_gutter_overwritable)

Returns `true` if the gutter at the given index is overwritable. See [set_gutter_overwritable()](class_textedit.md#class_TextEdit_method_set_gutter_overwritable).

---

<span id="class_TextEdit_method_is_in_mulitcaret_edit"></span>

[bool](class_bool.md#class_bool) **is_in_mulitcaret_edit** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_in_mulitcaret_edit)

Returns `true` if a [begin_multicaret_edit()](class_textedit.md#class_TextEdit_method_begin_multicaret_edit) has been called and [end_multicaret_edit()](class_textedit.md#class_TextEdit_method_end_multicaret_edit) has not yet been called.

---

<span id="class_TextEdit_method_is_line_gutter_clickable"></span>

[bool](class_bool.md#class_bool) **is_line_gutter_clickable** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_line_gutter_clickable)

Returns `true` if the gutter at the given index on the given line is clickable. See [set_line_gutter_clickable()](class_textedit.md#class_TextEdit_method_set_line_gutter_clickable).

---

<span id="class_TextEdit_method_is_line_wrapped"></span>

[bool](class_bool.md#class_bool) **is_line_wrapped** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_line_wrapped)

Returns if the given line is wrapped.

---

<span id="class_TextEdit_method_is_menu_visible"></span>

[bool](class_bool.md#class_bool) **is_menu_visible** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_menu_visible)

Returns `true` if the menu is visible. Use this instead of `get_menu().visible` to improve performance (so the creation of the menu is avoided). See [get_menu()](class_textedit.md#class_TextEdit_method_get_menu).

---

<span id="class_TextEdit_method_is_mouse_over_selection"></span>

[bool](class_bool.md#class_bool) **is_mouse_over_selection** ( edges: [bool](class_bool.md#class_bool), caret_index: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_mouse_over_selection)

Returns `true` if the mouse is over a selection. If `edges` is `true`, the edges are considered part of the selection.

---

<span id="class_TextEdit_method_is_overtype_mode_enabled"></span>

[bool](class_bool.md#class_bool) **is_overtype_mode_enabled** ( ) *const* [🔗](class_textedit.md#class_TextEdit_method_is_overtype_mode_enabled)

Returns `true` if overtype mode is enabled. See [set_overtype_mode_enabled()](class_textedit.md#class_TextEdit_method_set_overtype_mode_enabled).

---

<span id="class_TextEdit_method_menu_option"></span>

void **menu_option** ( option: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_menu_option)

Executes a given action as defined in the [MenuItems](class_textedit.md#enum_TextEdit_MenuItems) enum.

---

<span id="class_TextEdit_method_merge_gutters"></span>

void **merge_gutters** ( from_line: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_merge_gutters)

Merge the gutters from `from_line` into `to_line`. Only overwritable gutters will be copied. See [set_gutter_overwritable()](class_textedit.md#class_TextEdit_method_set_gutter_overwritable).

---

<span id="class_TextEdit_method_merge_overlapping_carets"></span>

void **merge_overlapping_carets** ( ) [🔗](class_textedit.md#class_TextEdit_method_merge_overlapping_carets)

Merges any overlapping carets. Will favor the newest caret, or the caret with a selection.

If [is_in_mulitcaret_edit()](class_textedit.md#class_TextEdit_method_is_in_mulitcaret_edit) is `true`, the merge will be queued to happen at the end of the multicaret edit. See [begin_multicaret_edit()](class_textedit.md#class_TextEdit_method_begin_multicaret_edit) and [end_multicaret_edit()](class_textedit.md#class_TextEdit_method_end_multicaret_edit).

 **Note:** This is not called when a caret changes position but after certain actions, so it is possible to get into a state where carets overlap.

---

<span id="class_TextEdit_method_multicaret_edit_ignore_caret"></span>

[bool](class_bool.md#class_bool) **multicaret_edit_ignore_caret** ( caret_index: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_multicaret_edit_ignore_caret)

Returns `true` if the given `caret_index` should be ignored as part of a multicaret edit. See [begin_multicaret_edit()](class_textedit.md#class_TextEdit_method_begin_multicaret_edit) and [end_multicaret_edit()](class_textedit.md#class_TextEdit_method_end_multicaret_edit). Carets that should be ignored are ones that were part of removed text and will likely be merged at the end of the edit, or carets that were added during the edit.

It is recommended to `continue` within a loop iterating on multiple carets if a caret should be ignored.

---

<span id="class_TextEdit_method_paste"></span>

void **paste** ( caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_paste)

Paste at the current location. Can be overridden with [_paste()](class_textedit.md#class_TextEdit_private_method__paste).

---

<span id="class_TextEdit_method_paste_primary_clipboard"></span>

void **paste_primary_clipboard** ( caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_paste_primary_clipboard)

Pastes the primary clipboard.

---

<span id="class_TextEdit_method_redo"></span>

void **redo** ( ) [🔗](class_textedit.md#class_TextEdit_method_redo)

Perform redo operation.

---

<span id="class_TextEdit_method_remove_caret"></span>

void **remove_caret** ( caret: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_remove_caret)

Removes the given caret index.

 **Note:** This can result in adjustment of all other caret indices.

---

<span id="class_TextEdit_method_remove_gutter"></span>

void **remove_gutter** ( gutter: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_remove_gutter)

Removes the gutter at the given index.

---

<span id="class_TextEdit_method_remove_line_at"></span>

void **remove_line_at** ( line: [int](class_int.md#class_int), move_carets_down: [bool](class_bool.md#class_bool) = true ) [🔗](class_textedit.md#class_TextEdit_method_remove_line_at)

Removes the line of text at `line`. Carets on this line will attempt to match their previous visual x position.

If `move_carets_down` is `true` carets will move to the next line down, otherwise carets will move up.

---

<span id="class_TextEdit_method_remove_secondary_carets"></span>

void **remove_secondary_carets** ( ) [🔗](class_textedit.md#class_TextEdit_method_remove_secondary_carets)

Removes all additional carets.

---

<span id="class_TextEdit_method_remove_text"></span>

void **remove_text** ( from_line: [int](class_int.md#class_int), from_column: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int), to_column: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_remove_text)

Removes text between the given positions.

---

<span id="class_TextEdit_method_search"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **search** ( text: [String](class_string.md#class_String), flags: [int](class_int.md#class_int), from_line: [int](class_int.md#class_int), from_column: [int](class_int.md#class_int) ) *const* [🔗](class_textedit.md#class_TextEdit_method_search)

Perform a search inside the text. Search flags can be specified in the [SearchFlags](class_textedit.md#enum_TextEdit_SearchFlags) enum.

In the returned vector, `x` is the column, `y` is the line. If no results are found, both are equal to `-1`.

.. tabs::

```
```

    var result = search("print", SEARCH_WHOLE_WORDS, 0, 0)
    if result.x != -1:
        # Result found.
        var line_number = result.y
        var column_number = result.x

```
```

    Vector2I result = Search("print", (uint)TextEdit.SearchFlags.WholeWords, 0, 0);
    if (result.X != -1)
    {
        // Result found.
        int lineNumber = result.Y;
        int columnNumber = result.X;
    }

---

<span id="class_TextEdit_method_select"></span>

void **select** ( origin_line: [int](class_int.md#class_int), origin_column: [int](class_int.md#class_int), caret_line: [int](class_int.md#class_int), caret_column: [int](class_int.md#class_int), caret_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_select)

Selects text from `origin_line` and `origin_column` to `caret_line` and `caret_column` for the given `caret_index`. This moves the selection origin and the caret. If the positions are the same, the selection will be deselected.

If [selecting_enabled](class_textedit.md#class_TextEdit_property_selecting_enabled) is `false`, no selection will occur.

 **Note:** If supporting multiple carets this will not check for any overlap. See [merge_overlapping_carets()](class_textedit.md#class_TextEdit_method_merge_overlapping_carets).

---

<span id="class_TextEdit_method_select_all"></span>

void **select_all** ( ) [🔗](class_textedit.md#class_TextEdit_method_select_all)

Select all the text.

If [selecting_enabled](class_textedit.md#class_TextEdit_property_selecting_enabled) is `false`, no selection will occur.

---

<span id="class_TextEdit_method_select_word_under_caret"></span>

void **select_word_under_caret** ( caret_index: [int](class_int.md#class_int) = -1 ) [🔗](class_textedit.md#class_TextEdit_method_select_word_under_caret)

Selects the word under the caret.

---

<span id="class_TextEdit_method_set_caret_column"></span>

void **set_caret_column** ( column: [int](class_int.md#class_int), adjust_viewport: [bool](class_bool.md#class_bool) = true, caret_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_set_caret_column)

Moves the caret to the specified `column` index.

If `adjust_viewport` is `true`, the viewport will center at the caret position after the move occurs.

 **Note:** If supporting multiple carets this will not check for any overlap. See [merge_overlapping_carets()](class_textedit.md#class_TextEdit_method_merge_overlapping_carets).

---

<span id="class_TextEdit_method_set_caret_line"></span>

void **set_caret_line** ( line: [int](class_int.md#class_int), adjust_viewport: [bool](class_bool.md#class_bool) = true, can_be_hidden: [bool](class_bool.md#class_bool) = true, wrap_index: [int](class_int.md#class_int) = 0, caret_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_set_caret_line)

Moves the caret to the specified `line` index. The caret column will be moved to the same visual position it was at the last time [set_caret_column()](class_textedit.md#class_TextEdit_method_set_caret_column) was called, or clamped to the end of the line.

If `adjust_viewport` is `true`, the viewport will center at the caret position after the move occurs.

If `can_be_hidden` is `true`, the specified `line` can be hidden.

If `wrap_index` is `-1`, the caret column will be clamped to the `line`'s length. If `wrap_index` is greater than `-1`, the column will be moved to attempt to match the visual x position on the line's `wrap_index` to the position from the last time [set_caret_column()](class_textedit.md#class_TextEdit_method_set_caret_column) was called.

 **Note:** If supporting multiple carets this will not check for any overlap. See [merge_overlapping_carets()](class_textedit.md#class_TextEdit_method_merge_overlapping_carets).

---

<span id="class_TextEdit_method_set_gutter_clickable"></span>

void **set_gutter_clickable** ( gutter: [int](class_int.md#class_int), clickable: [bool](class_bool.md#class_bool) ) [🔗](class_textedit.md#class_TextEdit_method_set_gutter_clickable)

If `true`, the mouse cursor will change to a pointing hand ([Control.CURSOR_POINTING_HAND](class_control.md#class_Control_constant_CURSOR_POINTING_HAND)) when hovering over the gutter at the given index. See [is_gutter_clickable()](class_textedit.md#class_TextEdit_method_is_gutter_clickable) and [set_line_gutter_clickable()](class_textedit.md#class_TextEdit_method_set_line_gutter_clickable).

---

<span id="class_TextEdit_method_set_gutter_custom_draw"></span>

void **set_gutter_custom_draw** ( column: [int](class_int.md#class_int), draw_callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_textedit.md#class_TextEdit_method_set_gutter_custom_draw)

Set a custom draw callback for the gutter at the given index. `draw_callback` must take the following arguments: A line index [int](class_int.md#class_int), a gutter index [int](class_int.md#class_int), and an area [Rect2](class_rect2.md#class_Rect2). This callback only works when the gutter type is [GUTTER_TYPE_CUSTOM](class_textedit.md#class_TextEdit_constant_GUTTER_TYPE_CUSTOM) (see [set_gutter_type()](class_textedit.md#class_TextEdit_method_set_gutter_type)).

---

<span id="class_TextEdit_method_set_gutter_draw"></span>

void **set_gutter_draw** ( gutter: [int](class_int.md#class_int), draw: [bool](class_bool.md#class_bool) ) [🔗](class_textedit.md#class_TextEdit_method_set_gutter_draw)

If `true`, the gutter at the given index is drawn. The gutter type ([set_gutter_type()](class_textedit.md#class_TextEdit_method_set_gutter_type)) determines how it is drawn. See [is_gutter_drawn()](class_textedit.md#class_TextEdit_method_is_gutter_drawn).

---

<span id="class_TextEdit_method_set_gutter_name"></span>

void **set_gutter_name** ( gutter: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_textedit.md#class_TextEdit_method_set_gutter_name)

Sets the name of the gutter at the given index.

---

<span id="class_TextEdit_method_set_gutter_overwritable"></span>

void **set_gutter_overwritable** ( gutter: [int](class_int.md#class_int), overwritable: [bool](class_bool.md#class_bool) ) [🔗](class_textedit.md#class_TextEdit_method_set_gutter_overwritable)

If `true`, the line data of the gutter at the given index can be overridden when using [merge_gutters()](class_textedit.md#class_TextEdit_method_merge_gutters). See [is_gutter_overwritable()](class_textedit.md#class_TextEdit_method_is_gutter_overwritable).

---

<span id="class_TextEdit_method_set_gutter_type"></span>

void **set_gutter_type** ( gutter: [int](class_int.md#class_int), type: [GutterType](class_textedit.md#enum_TextEdit_GutterType) ) [🔗](class_textedit.md#class_TextEdit_method_set_gutter_type)

Sets the type of gutter at the given index. Gutters can contain icons, text, or custom visuals.

---

<span id="class_TextEdit_method_set_gutter_width"></span>

void **set_gutter_width** ( gutter: [int](class_int.md#class_int), width: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_set_gutter_width)

Set the width of the gutter at the given index.

---

<span id="class_TextEdit_method_set_line"></span>

void **set_line** ( line: [int](class_int.md#class_int), new_text: [String](class_string.md#class_String) ) [🔗](class_textedit.md#class_TextEdit_method_set_line)

Sets the text for a specific `line`.

Carets on the line will attempt to keep their visual x position.

---

<span id="class_TextEdit_method_set_line_as_center_visible"></span>

void **set_line_as_center_visible** ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_set_line_as_center_visible)

Positions the `wrap_index` of `line` at the center of the viewport.

---

<span id="class_TextEdit_method_set_line_as_first_visible"></span>

void **set_line_as_first_visible** ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_set_line_as_first_visible)

Positions the `wrap_index` of `line` at the top of the viewport.

---

<span id="class_TextEdit_method_set_line_as_last_visible"></span>

void **set_line_as_last_visible** ( line: [int](class_int.md#class_int), wrap_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_set_line_as_last_visible)

Positions the `wrap_index` of `line` at the bottom of the viewport.

---

<span id="class_TextEdit_method_set_line_background_color"></span>

void **set_line_background_color** ( line: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_textedit.md#class_TextEdit_method_set_line_background_color)

Sets the custom background color of the given line. If transparent, this color is applied on top of the default background color (See [background_color](class_textedit.md#class_TextEdit_theme_color_background_color)). If set to `Color(0, 0, 0, 0)`, no additional color is applied.

---

<span id="class_TextEdit_method_set_line_gutter_clickable"></span>

void **set_line_gutter_clickable** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), clickable: [bool](class_bool.md#class_bool) ) [🔗](class_textedit.md#class_TextEdit_method_set_line_gutter_clickable)

If `clickable` is `true`, makes the `gutter` on the given `line` clickable. This is like [set_gutter_clickable()](class_textedit.md#class_TextEdit_method_set_gutter_clickable), but for a single line. If [is_gutter_clickable()](class_textedit.md#class_TextEdit_method_is_gutter_clickable) is `true`, this will not have any effect. See [is_line_gutter_clickable()](class_textedit.md#class_TextEdit_method_is_line_gutter_clickable) and [gutter_clicked](class_textedit.md#class_TextEdit_signal_gutter_clicked).

---

<span id="class_TextEdit_method_set_line_gutter_icon"></span>

void **set_line_gutter_icon** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_textedit.md#class_TextEdit_method_set_line_gutter_icon)

Sets the icon for `gutter` on `line` to `icon`. This only works when the gutter type is [GUTTER_TYPE_ICON](class_textedit.md#class_TextEdit_constant_GUTTER_TYPE_ICON) (see [set_gutter_type()](class_textedit.md#class_TextEdit_method_set_gutter_type)).

---

<span id="class_TextEdit_method_set_line_gutter_item_color"></span>

void **set_line_gutter_item_color** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_textedit.md#class_TextEdit_method_set_line_gutter_item_color)

Sets the color for `gutter` on `line` to `color`.

---

<span id="class_TextEdit_method_set_line_gutter_metadata"></span>

void **set_line_gutter_metadata** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), metadata: [Variant](class_variant.md#class_Variant) ) [🔗](class_textedit.md#class_TextEdit_method_set_line_gutter_metadata)

Sets the metadata for `gutter` on `line` to `metadata`.

---

<span id="class_TextEdit_method_set_line_gutter_text"></span>

void **set_line_gutter_text** ( line: [int](class_int.md#class_int), gutter: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) [🔗](class_textedit.md#class_TextEdit_method_set_line_gutter_text)

Sets the text for `gutter` on `line` to `text`. This only works when the gutter type is [GUTTER_TYPE_STRING](class_textedit.md#class_TextEdit_constant_GUTTER_TYPE_STRING) (see [set_gutter_type()](class_textedit.md#class_TextEdit_method_set_gutter_type)).

---

<span id="class_TextEdit_method_set_overtype_mode_enabled"></span>

void **set_overtype_mode_enabled** ( enabled: [bool](class_bool.md#class_bool) ) [🔗](class_textedit.md#class_TextEdit_method_set_overtype_mode_enabled)

If `true`, enables overtype mode. In this mode, typing overrides existing text instead of inserting text. The ProjectSettings.input/ui_text_toggle_insert_mode action toggles overtype mode. See [is_overtype_mode_enabled()](class_textedit.md#class_TextEdit_method_is_overtype_mode_enabled).

---

<span id="class_TextEdit_method_set_search_flags"></span>

void **set_search_flags** ( flags: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_set_search_flags)

Sets the search `flags`. This is used with [set_search_text()](class_textedit.md#class_TextEdit_method_set_search_text) to highlight occurrences of the searched text. Search flags can be specified from the [SearchFlags](class_textedit.md#enum_TextEdit_SearchFlags) enum.

---

<span id="class_TextEdit_method_set_search_text"></span>

void **set_search_text** ( search_text: [String](class_string.md#class_String) ) [🔗](class_textedit.md#class_TextEdit_method_set_search_text)

Sets the search text. See [set_search_flags()](class_textedit.md#class_TextEdit_method_set_search_flags).

---

<span id="class_TextEdit_method_set_selection_mode"></span>

void **set_selection_mode** ( mode: [SelectionMode](class_textedit.md#enum_TextEdit_SelectionMode) ) [🔗](class_textedit.md#class_TextEdit_method_set_selection_mode)

Sets the current selection mode.

---

<span id="class_TextEdit_method_set_selection_origin_column"></span>

void **set_selection_origin_column** ( column: [int](class_int.md#class_int), caret_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_set_selection_origin_column)

Sets the selection origin column to the `column` for the given `caret_index`. If the selection origin is moved to the caret position, the selection will deselect.

---

<span id="class_TextEdit_method_set_selection_origin_line"></span>

void **set_selection_origin_line** ( line: [int](class_int.md#class_int), can_be_hidden: [bool](class_bool.md#class_bool) = true, wrap_index: [int](class_int.md#class_int) = -1, caret_index: [int](class_int.md#class_int) = 0 ) [🔗](class_textedit.md#class_TextEdit_method_set_selection_origin_line)

Sets the selection origin line to the `line` for the given `caret_index`. If the selection origin is moved to the caret position, the selection will deselect.

If `can_be_hidden` is `false`, The line will be set to the nearest unhidden line below or above.

If `wrap_index` is `-1`, the selection origin column will be clamped to the `line`'s length. If `wrap_index` is greater than `-1`, the column will be moved to attempt to match the visual x position on the line's `wrap_index` to the position from the last time [set_selection_origin_column()](class_textedit.md#class_TextEdit_method_set_selection_origin_column) or [select()](class_textedit.md#class_TextEdit_method_select) was called.

---

<span id="class_TextEdit_method_set_tab_size"></span>

void **set_tab_size** ( size: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_set_tab_size)

Sets the tab size for the **TextEdit** to use.

---

<span id="class_TextEdit_method_set_tooltip_request_func"></span>

void **set_tooltip_request_func** ( callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_textedit.md#class_TextEdit_method_set_tooltip_request_func)

Provide custom tooltip text. The callback method must take the following args: `hovered_word: String`.

---

<span id="class_TextEdit_method_skip_selection_for_next_occurrence"></span>

void **skip_selection_for_next_occurrence** ( ) [🔗](class_textedit.md#class_TextEdit_method_skip_selection_for_next_occurrence)

Moves a selection and a caret for the next occurrence of the current selection. If there is no active selection, moves to the next occurrence of the word under caret.

---

<span id="class_TextEdit_method_start_action"></span>

void **start_action** ( action: [EditAction](class_textedit.md#enum_TextEdit_EditAction) ) [🔗](class_textedit.md#class_TextEdit_method_start_action)

Starts an action, will end the current action if `action` is different.

An action will also end after a call to [end_action()](class_textedit.md#class_TextEdit_method_end_action), after ProjectSettings.gui/timers/text_edit_idle_detect_sec is triggered or a new undoable step outside the [start_action()](class_textedit.md#class_TextEdit_method_start_action) and [end_action()](class_textedit.md#class_TextEdit_method_end_action) calls.

---

<span id="class_TextEdit_method_swap_lines"></span>

void **swap_lines** ( from_line: [int](class_int.md#class_int), to_line: [int](class_int.md#class_int) ) [🔗](class_textedit.md#class_TextEdit_method_swap_lines)

Swaps the two lines. Carets will be swapped with the lines.

---

<span id="class_TextEdit_method_tag_saved_version"></span>

void **tag_saved_version** ( ) [🔗](class_textedit.md#class_TextEdit_method_tag_saved_version)

Tag the current version as saved.

---

<span id="class_TextEdit_method_undo"></span>

void **undo** ( ) [🔗](class_textedit.md#class_TextEdit_method_undo)

Perform undo operation.

---

### Theme Property Descriptions

<span id="class_TextEdit_theme_color_background_color"></span>

[Color](class_color.md#class_Color) **background_color** = `Color(0, 0, 0, 0)` [🔗](class_textedit.md#class_TextEdit_theme_color_background_color)

Sets the background [Color](class_color.md#class_Color) of this **TextEdit**.

---

<span id="class_TextEdit_theme_color_caret_background_color"></span>

[Color](class_color.md#class_Color) **caret_background_color** = `Color(0, 0, 0, 1)` [🔗](class_textedit.md#class_TextEdit_theme_color_caret_background_color)

[Color](class_color.md#class_Color) of the text behind the caret when using a block caret.

---

<span id="class_TextEdit_theme_color_caret_color"></span>

[Color](class_color.md#class_Color) **caret_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_textedit.md#class_TextEdit_theme_color_caret_color)

[Color](class_color.md#class_Color) of the caret. This can be set to a fully transparent color to hide the caret entirely.

---

<span id="class_TextEdit_theme_color_current_line_color"></span>

[Color](class_color.md#class_Color) **current_line_color** = `Color(0.25, 0.25, 0.26, 0.8)` [🔗](class_textedit.md#class_TextEdit_theme_color_current_line_color)

Background [Color](class_color.md#class_Color) of the line containing the caret.

---

<span id="class_TextEdit_theme_color_font_color"></span>

[Color](class_color.md#class_Color) **font_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_textedit.md#class_TextEdit_theme_color_font_color)

Sets the font [Color](class_color.md#class_Color).

---

<span id="class_TextEdit_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_textedit.md#class_TextEdit_theme_color_font_outline_color)

The tint of text outline of the **TextEdit**.

---

<span id="class_TextEdit_theme_color_font_placeholder_color"></span>

[Color](class_color.md#class_Color) **font_placeholder_color** = `Color(0.875, 0.875, 0.875, 0.6)` [🔗](class_textedit.md#class_TextEdit_theme_color_font_placeholder_color)

Font color for [placeholder_text](class_textedit.md#class_TextEdit_property_placeholder_text).

---

<span id="class_TextEdit_theme_color_font_readonly_color"></span>

[Color](class_color.md#class_Color) **font_readonly_color** = `Color(0.875, 0.875, 0.875, 0.5)` [🔗](class_textedit.md#class_TextEdit_theme_color_font_readonly_color)

Sets the font [Color](class_color.md#class_Color) when [editable](class_textedit.md#class_TextEdit_property_editable) is disabled.

---

<span id="class_TextEdit_theme_color_font_selected_color"></span>

[Color](class_color.md#class_Color) **font_selected_color** = `Color(0, 0, 0, 0)` [🔗](class_textedit.md#class_TextEdit_theme_color_font_selected_color)

Sets the [Color](class_color.md#class_Color) of the selected text. If equal to `Color(0, 0, 0, 0)`, it will be ignored.

---

<span id="class_TextEdit_theme_color_search_result_border_color"></span>

[Color](class_color.md#class_Color) **search_result_border_color** = `Color(0.3, 0.3, 0.3, 0.4)` [🔗](class_textedit.md#class_TextEdit_theme_color_search_result_border_color)

[Color](class_color.md#class_Color) of the border around text that matches the search query.

---

<span id="class_TextEdit_theme_color_search_result_color"></span>

[Color](class_color.md#class_Color) **search_result_color** = `Color(0.3, 0.3, 0.3, 1)` [🔗](class_textedit.md#class_TextEdit_theme_color_search_result_color)

[Color](class_color.md#class_Color) behind the text that matches the search query.

---

<span id="class_TextEdit_theme_color_selection_color"></span>

[Color](class_color.md#class_Color) **selection_color** = `Color(0.5, 0.5, 0.5, 1)` [🔗](class_textedit.md#class_TextEdit_theme_color_selection_color)

Sets the highlight [Color](class_color.md#class_Color) of text selections.

---

<span id="class_TextEdit_theme_color_word_highlighted_color"></span>

[Color](class_color.md#class_Color) **word_highlighted_color** = `Color(0.5, 0.5, 0.5, 0.25)` [🔗](class_textedit.md#class_TextEdit_theme_color_word_highlighted_color)

Sets the highlight [Color](class_color.md#class_Color) of multiple occurrences. [highlight_all_occurrences](class_textedit.md#class_TextEdit_property_highlight_all_occurrences) has to be enabled.

---

<span id="class_TextEdit_theme_constant_caret_width"></span>

[int](class_int.md#class_int) **caret_width** = `1` [🔗](class_textedit.md#class_TextEdit_theme_constant_caret_width)

The caret's width in pixels. Greater values can be used to improve accessibility by ensuring the caret is easily visible, or to ensure consistency with a large font size. If set to `0` or lower, the caret width is automatically set to 1 pixel and multiplied by the display scaling factor.

---

<span id="class_TextEdit_theme_constant_line_spacing"></span>

[int](class_int.md#class_int) **line_spacing** = `4` [🔗](class_textedit.md#class_TextEdit_theme_constant_line_spacing)

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

<span id="class_TextEdit_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_textedit.md#class_TextEdit_theme_constant_outline_size)

The size of the text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_textedit.md#class_TextEdit_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_TextEdit_theme_constant_wrap_offset"></span>

[int](class_int.md#class_int) **wrap_offset** = `10` [🔗](class_textedit.md#class_TextEdit_theme_constant_wrap_offset)

Sets an additional margin for line wrapping width.

---

<span id="class_TextEdit_theme_font_font"></span>

[Font](class_font.md#class_Font) **font** [🔗](class_textedit.md#class_TextEdit_theme_font_font)

Sets the default [Font](class_font.md#class_Font).

---

<span id="class_TextEdit_theme_font_size_font_size"></span>

[int](class_int.md#class_int) **font_size** [🔗](class_textedit.md#class_TextEdit_theme_font_size_font_size)

Sets default font size.

---

<span id="class_TextEdit_theme_icon_space"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **space** [🔗](class_textedit.md#class_TextEdit_theme_icon_space)

Sets a custom [Texture2D](class_texture2d.md#class_Texture2D) for space text characters.

---

<span id="class_TextEdit_theme_icon_tab"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **tab** [🔗](class_textedit.md#class_TextEdit_theme_icon_tab)

Sets a custom [Texture2D](class_texture2d.md#class_Texture2D) for tab text characters.

---

<span id="class_TextEdit_theme_style_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **focus** [🔗](class_textedit.md#class_TextEdit_theme_style_focus)

Sets the [StyleBox](class_stylebox.md#class_StyleBox) when in focus. The [focus](class_textedit.md#class_TextEdit_theme_style_focus) [StyleBox](class_stylebox.md#class_StyleBox) is displayed *over* the base [StyleBox](class_stylebox.md#class_StyleBox), so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the base [StyleBox](class_stylebox.md#class_StyleBox) remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_TextEdit_theme_style_normal"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **normal** [🔗](class_textedit.md#class_TextEdit_theme_style_normal)

Sets the [StyleBox](class_stylebox.md#class_StyleBox) of this **TextEdit**.

---

<span id="class_TextEdit_theme_style_read_only"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **read_only** [🔗](class_textedit.md#class_TextEdit_theme_style_read_only)

Sets the [StyleBox](class_stylebox.md#class_StyleBox) of this **TextEdit** when [editable](class_textedit.md#class_TextEdit_property_editable) is disabled.
