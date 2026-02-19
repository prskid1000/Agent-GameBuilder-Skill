<span id="class_CodeEdit"></span>

## CodeEdit

**Inherits:** [TextEdit](class_textedit.md#class_TextEdit) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A multiline text editor designed for editing code.

### Description

CodeEdit is a specialized [TextEdit](class_textedit.md#class_TextEdit) designed for editing plain text code files. It has many features commonly found in code editors such as line numbers, line folding, code completion, indent management, and string/comment management.

 **Note:** Regardless of locale, **CodeEdit** will by default always use left-to-right text direction to correctly display source code.

### Properties


| [bool](class_bool.md#class_bool) | [auto_brace_completion_enabled](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_enabled) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [auto_brace_completion_highlight_matching](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_highlight_matching) | `false` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [auto_brace_completion_pairs](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_pairs) | `{ "\"": "\"", "'": "'", "(": ")", "[": "]", "{": "}" }` |
| [bool](class_bool.md#class_bool) | [code_completion_enabled](class_codeedit.md#class_CodeEdit_property_code_completion_enabled) | `false` |
| [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] | [code_completion_prefixes](class_codeedit.md#class_CodeEdit_property_code_completion_prefixes) | `[]` |
| [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] | [delimiter_comments](class_codeedit.md#class_CodeEdit_property_delimiter_comments) | `[]` |
| [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] | [delimiter_strings](class_codeedit.md#class_CodeEdit_property_delimiter_strings) | `["' '", "\" \""]` |
| [bool](class_bool.md#class_bool) | [gutters_draw_bookmarks](class_codeedit.md#class_CodeEdit_property_gutters_draw_bookmarks) | `false` |
| [bool](class_bool.md#class_bool) | [gutters_draw_breakpoints_gutter](class_codeedit.md#class_CodeEdit_property_gutters_draw_breakpoints_gutter) | `false` |
| [bool](class_bool.md#class_bool) | [gutters_draw_executing_lines](class_codeedit.md#class_CodeEdit_property_gutters_draw_executing_lines) | `false` |
| [bool](class_bool.md#class_bool) | [gutters_draw_fold_gutter](class_codeedit.md#class_CodeEdit_property_gutters_draw_fold_gutter) | `false` |
| [bool](class_bool.md#class_bool) | [gutters_draw_line_numbers](class_codeedit.md#class_CodeEdit_property_gutters_draw_line_numbers) | `false` |
| [int](class_int.md#class_int) | [gutters_line_numbers_min_digits](class_codeedit.md#class_CodeEdit_property_gutters_line_numbers_min_digits) | `3` |
| [bool](class_bool.md#class_bool) | [gutters_zero_pad_line_numbers](class_codeedit.md#class_CodeEdit_property_gutters_zero_pad_line_numbers) | `false` |
| [bool](class_bool.md#class_bool) | [indent_automatic](class_codeedit.md#class_CodeEdit_property_indent_automatic) | `false` |
| [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] | [indent_automatic_prefixes](class_codeedit.md#class_CodeEdit_property_indent_automatic_prefixes) | `[":", "{", "[", "("]` |
| [int](class_int.md#class_int) | [indent_size](class_codeedit.md#class_CodeEdit_property_indent_size) | `4` |
| [bool](class_bool.md#class_bool) | [indent_use_spaces](class_codeedit.md#class_CodeEdit_property_indent_use_spaces) | `false` |
| [LayoutDirection](class_control.md#enum_Control_LayoutDirection) | layout_direction | `2` (overrides [Control](class_control.md#class_Control_property_layout_direction)) |
| [bool](class_bool.md#class_bool) | [line_folding](class_codeedit.md#class_CodeEdit_property_line_folding) | `false` |
| [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] | [line_length_guidelines](class_codeedit.md#class_CodeEdit_property_line_length_guidelines) | `[]` |
| [bool](class_bool.md#class_bool) | [symbol_lookup_on_click](class_codeedit.md#class_CodeEdit_property_symbol_lookup_on_click) | `false` |
| [bool](class_bool.md#class_bool) | [symbol_tooltip_on_hover](class_codeedit.md#class_CodeEdit_property_symbol_tooltip_on_hover) | `false` |
| [TextDirection](class_control.md#enum_Control_TextDirection) | text_direction | `1` (overrides [TextEdit](class_textedit.md#class_TextEdit_property_text_direction)) |

### Methods


| void | [_confirm_code_completion](class_codeedit.md#class_CodeEdit_private_method__confirm_code_completion) ( replace: [bool](class_bool.md#class_bool) ) virtual |
| --- | --- |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [_filter_code_completion_candidates](class_codeedit.md#class_CodeEdit_private_method__filter_code_completion_candidates) ( candidates: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] ) | virtual | const |
| void | [_request_code_completion](class_codeedit.md#class_CodeEdit_private_method__request_code_completion) ( force: [bool](class_bool.md#class_bool) ) virtual |
| void | [add_auto_brace_completion_pair](class_codeedit.md#class_CodeEdit_method_add_auto_brace_completion_pair) ( start_key: [String](class_string.md#class_String), end_key: [String](class_string.md#class_String) ) |
| void | [add_code_completion_option](class_codeedit.md#class_CodeEdit_method_add_code_completion_option) ( type: [CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind), display_text: [String](class_string.md#class_String), insert_text: [String](class_string.md#class_String), text_color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), icon: [Resource](class_resource.md#class_Resource) = null, value: [Variant](class_variant.md#class_Variant) = null, location: [int](class_int.md#class_int) = 1024 ) |
| void | [add_comment_delimiter](class_codeedit.md#class_CodeEdit_method_add_comment_delimiter) ( start_key: [String](class_string.md#class_String), end_key: [String](class_string.md#class_String), line_only: [bool](class_bool.md#class_bool) = false ) |
| void | [add_string_delimiter](class_codeedit.md#class_CodeEdit_method_add_string_delimiter) ( start_key: [String](class_string.md#class_String), end_key: [String](class_string.md#class_String), line_only: [bool](class_bool.md#class_bool) = false ) |
| [bool](class_bool.md#class_bool) | [can_fold_line](class_codeedit.md#class_CodeEdit_method_can_fold_line) ( line: [int](class_int.md#class_int) ) const |
| void | [cancel_code_completion](class_codeedit.md#class_CodeEdit_method_cancel_code_completion) ( ) |
| void | [clear_bookmarked_lines](class_codeedit.md#class_CodeEdit_method_clear_bookmarked_lines) ( ) |
| void | [clear_breakpointed_lines](class_codeedit.md#class_CodeEdit_method_clear_breakpointed_lines) ( ) |
| void | [clear_comment_delimiters](class_codeedit.md#class_CodeEdit_method_clear_comment_delimiters) ( ) |
| void | [clear_executing_lines](class_codeedit.md#class_CodeEdit_method_clear_executing_lines) ( ) |
| void | [clear_string_delimiters](class_codeedit.md#class_CodeEdit_method_clear_string_delimiters) ( ) |
| void | [confirm_code_completion](class_codeedit.md#class_CodeEdit_method_confirm_code_completion) ( replace: [bool](class_bool.md#class_bool) = false ) |
| void | [convert_indent](class_codeedit.md#class_CodeEdit_method_convert_indent) ( from_line: [int](class_int.md#class_int) = -1, to_line: [int](class_int.md#class_int) = -1 ) |
| void | [create_code_region](class_codeedit.md#class_CodeEdit_method_create_code_region) ( ) |
| void | [delete_lines](class_codeedit.md#class_CodeEdit_method_delete_lines) ( ) |
| void | [do_indent](class_codeedit.md#class_CodeEdit_method_do_indent) ( ) |
| void | [duplicate_lines](class_codeedit.md#class_CodeEdit_method_duplicate_lines) ( ) |
| void | [duplicate_selection](class_codeedit.md#class_CodeEdit_method_duplicate_selection) ( ) |
| void | [fold_all_lines](class_codeedit.md#class_CodeEdit_method_fold_all_lines) ( ) |
| void | [fold_line](class_codeedit.md#class_CodeEdit_method_fold_line) ( line: [int](class_int.md#class_int) ) |
| [String](class_string.md#class_String) | [get_auto_brace_completion_close_key](class_codeedit.md#class_CodeEdit_method_get_auto_brace_completion_close_key) ( open_key: [String](class_string.md#class_String) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_bookmarked_lines](class_codeedit.md#class_CodeEdit_method_get_bookmarked_lines) ( ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_breakpointed_lines](class_codeedit.md#class_CodeEdit_method_get_breakpointed_lines) ( ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_code_completion_option](class_codeedit.md#class_CodeEdit_method_get_code_completion_option) ( index: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_code_completion_options](class_codeedit.md#class_CodeEdit_method_get_code_completion_options) ( ) const |
| [int](class_int.md#class_int) | [get_code_completion_selected_index](class_codeedit.md#class_CodeEdit_method_get_code_completion_selected_index) ( ) const |
| [String](class_string.md#class_String) | [get_code_region_end_tag](class_codeedit.md#class_CodeEdit_method_get_code_region_end_tag) ( ) const |
| [String](class_string.md#class_String) | [get_code_region_start_tag](class_codeedit.md#class_CodeEdit_method_get_code_region_start_tag) ( ) const |
| [String](class_string.md#class_String) | [get_delimiter_end_key](class_codeedit.md#class_CodeEdit_method_get_delimiter_end_key) ( delimiter_index: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_delimiter_end_position](class_codeedit.md#class_CodeEdit_method_get_delimiter_end_position) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_delimiter_start_key](class_codeedit.md#class_CodeEdit_method_get_delimiter_start_key) ( delimiter_index: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_delimiter_start_position](class_codeedit.md#class_CodeEdit_method_get_delimiter_start_position) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_executing_lines](class_codeedit.md#class_CodeEdit_method_get_executing_lines) ( ) const |
| [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] | [get_folded_lines](class_codeedit.md#class_CodeEdit_method_get_folded_lines) ( ) const |
| [String](class_string.md#class_String) | [get_text_for_code_completion](class_codeedit.md#class_CodeEdit_method_get_text_for_code_completion) ( ) const |
| [String](class_string.md#class_String) | [get_text_for_symbol_lookup](class_codeedit.md#class_CodeEdit_method_get_text_for_symbol_lookup) ( ) const |
| [String](class_string.md#class_String) | [get_text_with_cursor_char](class_codeedit.md#class_CodeEdit_method_get_text_with_cursor_char) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has_auto_brace_completion_close_key](class_codeedit.md#class_CodeEdit_method_has_auto_brace_completion_close_key) ( close_key: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [has_auto_brace_completion_open_key](class_codeedit.md#class_CodeEdit_method_has_auto_brace_completion_open_key) ( open_key: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [has_comment_delimiter](class_codeedit.md#class_CodeEdit_method_has_comment_delimiter) ( start_key: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [has_string_delimiter](class_codeedit.md#class_CodeEdit_method_has_string_delimiter) ( start_key: [String](class_string.md#class_String) ) const |
| void | [indent_lines](class_codeedit.md#class_CodeEdit_method_indent_lines) ( ) |
| [int](class_int.md#class_int) | [is_in_comment](class_codeedit.md#class_CodeEdit_method_is_in_comment) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) = -1 ) const |
| [int](class_int.md#class_int) | [is_in_string](class_codeedit.md#class_CodeEdit_method_is_in_string) ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) = -1 ) const |
| [bool](class_bool.md#class_bool) | [is_line_bookmarked](class_codeedit.md#class_CodeEdit_method_is_line_bookmarked) ( line: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_line_breakpointed](class_codeedit.md#class_CodeEdit_method_is_line_breakpointed) ( line: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_line_code_region_end](class_codeedit.md#class_CodeEdit_method_is_line_code_region_end) ( line: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_line_code_region_start](class_codeedit.md#class_CodeEdit_method_is_line_code_region_start) ( line: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_line_executing](class_codeedit.md#class_CodeEdit_method_is_line_executing) ( line: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_line_folded](class_codeedit.md#class_CodeEdit_method_is_line_folded) ( line: [int](class_int.md#class_int) ) const |
| void | [move_lines_down](class_codeedit.md#class_CodeEdit_method_move_lines_down) ( ) |
| void | [move_lines_up](class_codeedit.md#class_CodeEdit_method_move_lines_up) ( ) |
| void | [remove_comment_delimiter](class_codeedit.md#class_CodeEdit_method_remove_comment_delimiter) ( start_key: [String](class_string.md#class_String) ) |
| void | [remove_string_delimiter](class_codeedit.md#class_CodeEdit_method_remove_string_delimiter) ( start_key: [String](class_string.md#class_String) ) |
| void | [request_code_completion](class_codeedit.md#class_CodeEdit_method_request_code_completion) ( force: [bool](class_bool.md#class_bool) = false ) |
| void | [set_code_completion_selected_index](class_codeedit.md#class_CodeEdit_method_set_code_completion_selected_index) ( index: [int](class_int.md#class_int) ) |
| void | [set_code_hint](class_codeedit.md#class_CodeEdit_method_set_code_hint) ( code_hint: [String](class_string.md#class_String) ) |
| void | [set_code_hint_draw_below](class_codeedit.md#class_CodeEdit_method_set_code_hint_draw_below) ( draw_below: [bool](class_bool.md#class_bool) ) |
| void | [set_code_region_tags](class_codeedit.md#class_CodeEdit_method_set_code_region_tags) ( start: [String](class_string.md#class_String) = "region", end: [String](class_string.md#class_String) = "endregion" ) |
| void | [set_line_as_bookmarked](class_codeedit.md#class_CodeEdit_method_set_line_as_bookmarked) ( line: [int](class_int.md#class_int), bookmarked: [bool](class_bool.md#class_bool) ) |
| void | [set_line_as_breakpoint](class_codeedit.md#class_CodeEdit_method_set_line_as_breakpoint) ( line: [int](class_int.md#class_int), breakpointed: [bool](class_bool.md#class_bool) ) |
| void | [set_line_as_executing](class_codeedit.md#class_CodeEdit_method_set_line_as_executing) ( line: [int](class_int.md#class_int), executing: [bool](class_bool.md#class_bool) ) |
| void | [set_symbol_lookup_word_as_valid](class_codeedit.md#class_CodeEdit_method_set_symbol_lookup_word_as_valid) ( valid: [bool](class_bool.md#class_bool) ) |
| void | [toggle_foldable_line](class_codeedit.md#class_CodeEdit_method_toggle_foldable_line) ( line: [int](class_int.md#class_int) ) |
| void | [toggle_foldable_lines_at_carets](class_codeedit.md#class_CodeEdit_method_toggle_foldable_lines_at_carets) ( ) |
| void | [unfold_all_lines](class_codeedit.md#class_CodeEdit_method_unfold_all_lines) ( ) |
| void | [unfold_line](class_codeedit.md#class_CodeEdit_method_unfold_line) ( line: [int](class_int.md#class_int) ) |
| void | [unindent_lines](class_codeedit.md#class_CodeEdit_method_unindent_lines) ( ) |
| void | [update_code_completion_options](class_codeedit.md#class_CodeEdit_method_update_code_completion_options) ( force: [bool](class_bool.md#class_bool) ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [bookmark_color](class_codeedit.md#class_CodeEdit_theme_color_bookmark_color) | `Color(0.5, 0.64, 1, 0.8)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [brace_mismatch_color](class_codeedit.md#class_CodeEdit_theme_color_brace_mismatch_color) | `Color(1, 0.2, 0.2, 1)` |
| [Color](class_color.md#class_Color) | [breakpoint_color](class_codeedit.md#class_CodeEdit_theme_color_breakpoint_color) | `Color(0.9, 0.29, 0.3, 1)` |
| [Color](class_color.md#class_Color) | [code_folding_color](class_codeedit.md#class_CodeEdit_theme_color_code_folding_color) | `Color(0.8, 0.8, 0.8, 0.8)` |
| [Color](class_color.md#class_Color) | [completion_background_color](class_codeedit.md#class_CodeEdit_theme_color_completion_background_color) | `Color(0.17, 0.16, 0.2, 1)` |
| [Color](class_color.md#class_Color) | [completion_existing_color](class_codeedit.md#class_CodeEdit_theme_color_completion_existing_color) | `Color(0.87, 0.87, 0.87, 0.13)` |
| [Color](class_color.md#class_Color) | [completion_scroll_color](class_codeedit.md#class_CodeEdit_theme_color_completion_scroll_color) | `Color(1, 1, 1, 0.29)` |
| [Color](class_color.md#class_Color) | [completion_scroll_hovered_color](class_codeedit.md#class_CodeEdit_theme_color_completion_scroll_hovered_color) | `Color(1, 1, 1, 0.4)` |
| [Color](class_color.md#class_Color) | [completion_selected_color](class_codeedit.md#class_CodeEdit_theme_color_completion_selected_color) | `Color(0.26, 0.26, 0.27, 1)` |
| [Color](class_color.md#class_Color) | [executing_line_color](class_codeedit.md#class_CodeEdit_theme_color_executing_line_color) | `Color(0.98, 0.89, 0.27, 1)` |
| [Color](class_color.md#class_Color) | [folded_code_region_color](class_codeedit.md#class_CodeEdit_theme_color_folded_code_region_color) | `Color(0.68, 0.46, 0.77, 0.2)` |
| [Color](class_color.md#class_Color) | [line_length_guideline_color](class_codeedit.md#class_CodeEdit_theme_color_line_length_guideline_color) | `Color(0.3, 0.5, 0.8, 0.1)` |
| [Color](class_color.md#class_Color) | [line_number_color](class_codeedit.md#class_CodeEdit_theme_color_line_number_color) | `Color(0.67, 0.67, 0.67, 0.4)` |
| [int](class_int.md#class_int) | [completion_lines](class_codeedit.md#class_CodeEdit_theme_constant_completion_lines) | `7` |
| [int](class_int.md#class_int) | [completion_max_width](class_codeedit.md#class_CodeEdit_theme_constant_completion_max_width) | `50` |
| [int](class_int.md#class_int) | [completion_scroll_width](class_codeedit.md#class_CodeEdit_theme_constant_completion_scroll_width) | `6` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [bookmark](class_codeedit.md#class_CodeEdit_theme_icon_bookmark) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [breakpoint](class_codeedit.md#class_CodeEdit_theme_icon_breakpoint) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [can_fold](class_codeedit.md#class_CodeEdit_theme_icon_can_fold) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [can_fold_code_region](class_codeedit.md#class_CodeEdit_theme_icon_can_fold_code_region) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [completion_color_bg](class_codeedit.md#class_CodeEdit_theme_icon_completion_color_bg) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [executing_line](class_codeedit.md#class_CodeEdit_theme_icon_executing_line) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [folded](class_codeedit.md#class_CodeEdit_theme_icon_folded) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [folded_code_region](class_codeedit.md#class_CodeEdit_theme_icon_folded_code_region) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [folded_eol_icon](class_codeedit.md#class_CodeEdit_theme_icon_folded_eol_icon) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [completion](class_codeedit.md#class_CodeEdit_theme_style_completion) |

---

### Signals

<span id="class_CodeEdit_signal_breakpoint_toggled"></span>

**breakpoint_toggled** ( line: [int](class_int.md#class_int) ) [🔗](class_codeedit.md#class_CodeEdit_signal_breakpoint_toggled)

Emitted when a breakpoint is added or removed from a line. If the line is removed via backspace, a signal is emitted at the old line.

---

<span id="class_CodeEdit_signal_code_completion_requested"></span>

**code_completion_requested** ( ) [🔗](class_codeedit.md#class_CodeEdit_signal_code_completion_requested)

Emitted when the user requests code completion. This signal will not be sent if [_request_code_completion()](class_codeedit.md#class_CodeEdit_private_method__request_code_completion) is overridden or [code_completion_enabled](class_codeedit.md#class_CodeEdit_property_code_completion_enabled) is `false`.

---

<span id="class_CodeEdit_signal_symbol_hovered"></span>

**symbol_hovered** ( symbol: [String](class_string.md#class_String), line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) [🔗](class_codeedit.md#class_CodeEdit_signal_symbol_hovered)

Emitted when the user hovers over a symbol. Unlike [Control.mouse_entered](class_control.md#class_Control_signal_mouse_entered), this signal is not emitted immediately, but when the cursor is over the symbol for ProjectSettings.gui/timers/tooltip_delay_sec seconds.

 **Note:** [symbol_tooltip_on_hover](class_codeedit.md#class_CodeEdit_property_symbol_tooltip_on_hover) must be `true` for this signal to be emitted.

---

<span id="class_CodeEdit_signal_symbol_lookup"></span>

**symbol_lookup** ( symbol: [String](class_string.md#class_String), line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) [🔗](class_codeedit.md#class_CodeEdit_signal_symbol_lookup)

Emitted when the user has clicked on a valid symbol.

---

<span id="class_CodeEdit_signal_symbol_validate"></span>

**symbol_validate** ( symbol: [String](class_string.md#class_String) ) [🔗](class_codeedit.md#class_CodeEdit_signal_symbol_validate)

Emitted when the user hovers over a symbol. The symbol should be validated and responded to, by calling [set_symbol_lookup_word_as_valid()](class_codeedit.md#class_CodeEdit_method_set_symbol_lookup_word_as_valid).

 **Note:** [symbol_lookup_on_click](class_codeedit.md#class_CodeEdit_property_symbol_lookup_on_click) must be `true` for this signal to be emitted.

---

### Enumerations

<span id="enum_CodeEdit_CodeCompletionKind"></span>

enum **CodeCompletionKind**: [🔗](class_codeedit.md#enum_CodeEdit_CodeCompletionKind)

<span id="class_CodeEdit_constant_KIND_CLASS"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_CLASS** = `0`

Marks the option as a class.

<span id="class_CodeEdit_constant_KIND_FUNCTION"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_FUNCTION** = `1`

Marks the option as a function.

<span id="class_CodeEdit_constant_KIND_SIGNAL"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_SIGNAL** = `2`

Marks the option as a Godot signal.

<span id="class_CodeEdit_constant_KIND_VARIABLE"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_VARIABLE** = `3`

Marks the option as a variable.

<span id="class_CodeEdit_constant_KIND_MEMBER"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_MEMBER** = `4`

Marks the option as a member.

<span id="class_CodeEdit_constant_KIND_ENUM"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_ENUM** = `5`

Marks the option as an enum entry.

<span id="class_CodeEdit_constant_KIND_CONSTANT"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_CONSTANT** = `6`

Marks the option as a constant.

<span id="class_CodeEdit_constant_KIND_NODE_PATH"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_NODE_PATH** = `7`

Marks the option as a Godot node path.

<span id="class_CodeEdit_constant_KIND_FILE_PATH"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_FILE_PATH** = `8`

Marks the option as a file path.

<span id="class_CodeEdit_constant_KIND_PLAIN_TEXT"></span>

[CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind) **KIND_PLAIN_TEXT** = `9`

Marks the option as unclassified or plain text.

---

<span id="enum_CodeEdit_CodeCompletionLocation"></span>

enum **CodeCompletionLocation**: [🔗](class_codeedit.md#enum_CodeEdit_CodeCompletionLocation)

<span id="class_CodeEdit_constant_LOCATION_LOCAL"></span>

[CodeCompletionLocation](class_codeedit.md#enum_CodeEdit_CodeCompletionLocation) **LOCATION_LOCAL** = `0`

The option is local to the location of the code completion query - e.g. a local variable. Subsequent value of location represent options from the outer class, the exact value represent how far they are (in terms of inner classes).

<span id="class_CodeEdit_constant_LOCATION_PARENT_MASK"></span>

[CodeCompletionLocation](class_codeedit.md#enum_CodeEdit_CodeCompletionLocation) **LOCATION_PARENT_MASK** = `256`

The option is from the containing class or a parent class, relative to the location of the code completion query. Perform a bitwise OR with the class depth (e.g. `0` for the local class, `1` for the parent, `2` for the grandparent, etc.) to store the depth of an option in the class or a parent class.

<span id="class_CodeEdit_constant_LOCATION_OTHER_USER_CODE"></span>

[CodeCompletionLocation](class_codeedit.md#enum_CodeEdit_CodeCompletionLocation) **LOCATION_OTHER_USER_CODE** = `512`

The option is from user code which is not local and not in a derived class (e.g. Autoload Singletons).

<span id="class_CodeEdit_constant_LOCATION_OTHER"></span>

[CodeCompletionLocation](class_codeedit.md#enum_CodeEdit_CodeCompletionLocation) **LOCATION_OTHER** = `1024`

The option is from other engine code, not covered by the other enum constants - e.g. built-in classes.

---

### Property Descriptions

<span id="class_CodeEdit_property_auto_brace_completion_enabled"></span>

[bool](class_bool.md#class_bool) **auto_brace_completion_enabled** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_enabled)

- void **set_auto_brace_completion_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_auto_brace_completion_enabled** ( )

If `true`, uses [auto_brace_completion_pairs](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_pairs) to automatically insert the closing brace when the opening brace is inserted by typing or autocompletion. Also automatically removes the closing brace when using backspace on the opening brace.

---

<span id="class_CodeEdit_property_auto_brace_completion_highlight_matching"></span>

[bool](class_bool.md#class_bool) **auto_brace_completion_highlight_matching** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_highlight_matching)

- void **set_highlight_matching_braces_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_highlight_matching_braces_enabled** ( )

If `true`, highlights brace pairs when the caret is on either one, using [auto_brace_completion_pairs](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_pairs). If matching, the pairs will be underlined. If a brace is unmatched, it is colored with [brace_mismatch_color](class_codeedit.md#class_CodeEdit_theme_color_brace_mismatch_color).

---

<span id="class_CodeEdit_property_auto_brace_completion_pairs"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **auto_brace_completion_pairs** = `{ "\"": "\"", "'": "'", "(": ")", "[": "]", "{": "}" }` [🔗](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_pairs)

- void **set_auto_brace_completion_pairs** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_auto_brace_completion_pairs** ( )

Sets the brace pairs to be autocompleted. For each entry in the dictionary, the key is the opening brace and the value is the closing brace that matches it. A brace is a [String](class_string.md#class_String) made of symbols. See [auto_brace_completion_enabled](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_enabled) and [auto_brace_completion_highlight_matching](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_highlight_matching).

---

<span id="class_CodeEdit_property_code_completion_enabled"></span>

[bool](class_bool.md#class_bool) **code_completion_enabled** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_code_completion_enabled)

- void **set_code_completion_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_code_completion_enabled** ( )

If `true`, the ProjectSettings.input/ui_text_completion_query action requests code completion. To handle it, see [_request_code_completion()](class_codeedit.md#class_CodeEdit_private_method__request_code_completion) or [code_completion_requested](class_codeedit.md#class_CodeEdit_signal_code_completion_requested).

---

<span id="class_CodeEdit_property_code_completion_prefixes"></span>

[Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **code_completion_prefixes** = `[]` [🔗](class_codeedit.md#class_CodeEdit_property_code_completion_prefixes)

- void **set_code_completion_prefixes** ( value: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] )
- [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **get_code_completion_prefixes** ( )

Sets prefixes that will trigger code completion.

---

<span id="class_CodeEdit_property_delimiter_comments"></span>

[Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **delimiter_comments** = `[]` [🔗](class_codeedit.md#class_CodeEdit_property_delimiter_comments)

- void **set_comment_delimiters** ( value: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] )
- [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **get_comment_delimiters** ( )

Sets the comment delimiters. All existing comment delimiters will be removed.

---

<span id="class_CodeEdit_property_delimiter_strings"></span>

[Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **delimiter_strings** = `["' '", "\" \""]` [🔗](class_codeedit.md#class_CodeEdit_property_delimiter_strings)

- void **set_string_delimiters** ( value: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] )
- [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **get_string_delimiters** ( )

Sets the string delimiters. All existing string delimiters will be removed.

---

<span id="class_CodeEdit_property_gutters_draw_bookmarks"></span>

[bool](class_bool.md#class_bool) **gutters_draw_bookmarks** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_gutters_draw_bookmarks)

- void **set_draw_bookmarks_gutter** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drawing_bookmarks_gutter** ( )

If `true`, bookmarks are drawn in the gutter. This gutter is shared with breakpoints and executing lines. See [set_line_as_bookmarked()](class_codeedit.md#class_CodeEdit_method_set_line_as_bookmarked).

---

<span id="class_CodeEdit_property_gutters_draw_breakpoints_gutter"></span>

[bool](class_bool.md#class_bool) **gutters_draw_breakpoints_gutter** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_gutters_draw_breakpoints_gutter)

- void **set_draw_breakpoints_gutter** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drawing_breakpoints_gutter** ( )

If `true`, breakpoints are drawn in the gutter. This gutter is shared with bookmarks and executing lines. Clicking the gutter will toggle the breakpoint for the line, see [set_line_as_breakpoint()](class_codeedit.md#class_CodeEdit_method_set_line_as_breakpoint).

---

<span id="class_CodeEdit_property_gutters_draw_executing_lines"></span>

[bool](class_bool.md#class_bool) **gutters_draw_executing_lines** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_gutters_draw_executing_lines)

- void **set_draw_executing_lines_gutter** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drawing_executing_lines_gutter** ( )

If `true`, executing lines are marked in the gutter. This gutter is shared with breakpoints and bookmarks. See [set_line_as_executing()](class_codeedit.md#class_CodeEdit_method_set_line_as_executing).

---

<span id="class_CodeEdit_property_gutters_draw_fold_gutter"></span>

[bool](class_bool.md#class_bool) **gutters_draw_fold_gutter** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_gutters_draw_fold_gutter)

- void **set_draw_fold_gutter** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drawing_fold_gutter** ( )

If `true`, the fold gutter is drawn. In this gutter, the [can_fold_code_region](class_codeedit.md#class_CodeEdit_theme_icon_can_fold_code_region) icon is drawn for each foldable line (see [can_fold_line()](class_codeedit.md#class_CodeEdit_method_can_fold_line)) and the [folded_code_region](class_codeedit.md#class_CodeEdit_theme_icon_folded_code_region) icon is drawn for each folded line (see [is_line_folded()](class_codeedit.md#class_CodeEdit_method_is_line_folded)). These icons can be clicked to toggle the fold state, see [toggle_foldable_line()](class_codeedit.md#class_CodeEdit_method_toggle_foldable_line). [line_folding](class_codeedit.md#class_CodeEdit_property_line_folding) must be `true` to show icons.

---

<span id="class_CodeEdit_property_gutters_draw_line_numbers"></span>

[bool](class_bool.md#class_bool) **gutters_draw_line_numbers** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_gutters_draw_line_numbers)

- void **set_draw_line_numbers** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_draw_line_numbers_enabled** ( )

If `true`, the line number gutter is drawn. Line numbers start at `1` and are incremented for each line of text. Clicking and dragging in the line number gutter will select entire lines of text.

---

<span id="class_CodeEdit_property_gutters_line_numbers_min_digits"></span>

[int](class_int.md#class_int) **gutters_line_numbers_min_digits** = `3` [🔗](class_codeedit.md#class_CodeEdit_property_gutters_line_numbers_min_digits)

- void **set_line_numbers_min_digits** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_line_numbers_min_digits** ( )

The minimum width in digits reserved for the line number gutter.

---

<span id="class_CodeEdit_property_gutters_zero_pad_line_numbers"></span>

[bool](class_bool.md#class_bool) **gutters_zero_pad_line_numbers** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_gutters_zero_pad_line_numbers)

- void **set_line_numbers_zero_padded** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_line_numbers_zero_padded** ( )

If `true`, line numbers drawn in the gutter are zero padded based on the total line count. Requires [gutters_draw_line_numbers](class_codeedit.md#class_CodeEdit_property_gutters_draw_line_numbers) to be set to `true`.

---

<span id="class_CodeEdit_property_indent_automatic"></span>

[bool](class_bool.md#class_bool) **indent_automatic** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_indent_automatic)

- void **set_auto_indent_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_auto_indent_enabled** ( )

If `true`, an extra indent is automatically inserted when a new line is added and a prefix in [indent_automatic_prefixes](class_codeedit.md#class_CodeEdit_property_indent_automatic_prefixes) is found. If a brace pair opening key is found, the matching closing brace will be moved to another new line (see [auto_brace_completion_pairs](class_codeedit.md#class_CodeEdit_property_auto_brace_completion_pairs)).

---

<span id="class_CodeEdit_property_indent_automatic_prefixes"></span>

[Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **indent_automatic_prefixes** = `[":", "{", "[", "("]` [🔗](class_codeedit.md#class_CodeEdit_property_indent_automatic_prefixes)

- void **set_auto_indent_prefixes** ( value: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] )
- [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **get_auto_indent_prefixes** ( )

Prefixes to trigger an automatic indent. Used when [indent_automatic](class_codeedit.md#class_CodeEdit_property_indent_automatic) is set to `true`.

---

<span id="class_CodeEdit_property_indent_size"></span>

[int](class_int.md#class_int) **indent_size** = `4` [🔗](class_codeedit.md#class_CodeEdit_property_indent_size)

- void **set_indent_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_indent_size** ( )

Size of the tabulation indent (one :kbd:`Tab` press) in characters. If [indent_use_spaces](class_codeedit.md#class_CodeEdit_property_indent_use_spaces) is enabled the number of spaces to use.

---

<span id="class_CodeEdit_property_indent_use_spaces"></span>

[bool](class_bool.md#class_bool) **indent_use_spaces** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_indent_use_spaces)

- void **set_indent_using_spaces** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_indent_using_spaces** ( )

Use spaces instead of tabs for indentation.

---

<span id="class_CodeEdit_property_line_folding"></span>

[bool](class_bool.md#class_bool) **line_folding** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_line_folding)

- void **set_line_folding_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_line_folding_enabled** ( )

If `true`, lines can be folded. Otherwise, line folding methods like [fold_line()](class_codeedit.md#class_CodeEdit_method_fold_line) will not work and [can_fold_line()](class_codeedit.md#class_CodeEdit_method_can_fold_line) will always return `false`. See [gutters_draw_fold_gutter](class_codeedit.md#class_CodeEdit_property_gutters_draw_fold_gutter).

---

<span id="class_CodeEdit_property_line_length_guidelines"></span>

[Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] **line_length_guidelines** = `[]` [🔗](class_codeedit.md#class_CodeEdit_property_line_length_guidelines)

- void **set_line_length_guidelines** ( value: [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] )
- [Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] **get_line_length_guidelines** ( )

Draws vertical lines at the provided columns. The first entry is considered a main hard guideline and is drawn more prominently.

---

<span id="class_CodeEdit_property_symbol_lookup_on_click"></span>

[bool](class_bool.md#class_bool) **symbol_lookup_on_click** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_symbol_lookup_on_click)

- void **set_symbol_lookup_on_click_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_symbol_lookup_on_click_enabled** ( )

Set when a validated word from [symbol_validate](class_codeedit.md#class_CodeEdit_signal_symbol_validate) is clicked, the [symbol_lookup](class_codeedit.md#class_CodeEdit_signal_symbol_lookup) should be emitted.

---

<span id="class_CodeEdit_property_symbol_tooltip_on_hover"></span>

[bool](class_bool.md#class_bool) **symbol_tooltip_on_hover** = `false` [🔗](class_codeedit.md#class_CodeEdit_property_symbol_tooltip_on_hover)

- void **set_symbol_tooltip_on_hover_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_symbol_tooltip_on_hover_enabled** ( )

If `true`, the [symbol_hovered](class_codeedit.md#class_CodeEdit_signal_symbol_hovered) signal is emitted when hovering over a word.

---

### Method Descriptions

<span id="class_CodeEdit_private_method__confirm_code_completion"></span>

void **_confirm_code_completion** ( replace: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_codeedit.md#class_CodeEdit_private_method__confirm_code_completion)

Override this method to define how the selected entry should be inserted. If `replace` is `true`, any existing text should be replaced.

---

<span id="class_CodeEdit_private_method__filter_code_completion_candidates"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **_filter_code_completion_candidates** ( candidates: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] ) *virtual* *const* [🔗](class_codeedit.md#class_CodeEdit_private_method__filter_code_completion_candidates)

Override this method to define what items in `candidates` should be displayed.

Both `candidates` and the return is an [Array](class_array.md#class_Array) of [Dictionary](class_dictionary.md#class_Dictionary), see [get_code_completion_option()](class_codeedit.md#class_CodeEdit_method_get_code_completion_option) for [Dictionary](class_dictionary.md#class_Dictionary) content.

---

<span id="class_CodeEdit_private_method__request_code_completion"></span>

void **_request_code_completion** ( force: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_codeedit.md#class_CodeEdit_private_method__request_code_completion)

Override this method to define what happens when the user requests code completion. If `force` is `true`, any checks should be bypassed.

---

<span id="class_CodeEdit_method_add_auto_brace_completion_pair"></span>

void **add_auto_brace_completion_pair** ( start_key: [String](class_string.md#class_String), end_key: [String](class_string.md#class_String) ) [🔗](class_codeedit.md#class_CodeEdit_method_add_auto_brace_completion_pair)

Adds a brace pair.

Both the start and end keys must be symbols. Only the start key has to be unique.

---

<span id="class_CodeEdit_method_add_code_completion_option"></span>

void **add_code_completion_option** ( type: [CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind), display_text: [String](class_string.md#class_String), insert_text: [String](class_string.md#class_String), text_color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), icon: [Resource](class_resource.md#class_Resource) = null, value: [Variant](class_variant.md#class_Variant) = null, location: [int](class_int.md#class_int) = 1024 ) [🔗](class_codeedit.md#class_CodeEdit_method_add_code_completion_option)

Submits an item to the queue of potential candidates for the autocomplete menu. Call [update_code_completion_options()](class_codeedit.md#class_CodeEdit_method_update_code_completion_options) to update the list.

 `location` indicates location of the option relative to the location of the code completion query. See [CodeCompletionLocation](class_codeedit.md#enum_CodeEdit_CodeCompletionLocation) for how to set this value.

 **Note:** This list will replace all current candidates.

---

<span id="class_CodeEdit_method_add_comment_delimiter"></span>

void **add_comment_delimiter** ( start_key: [String](class_string.md#class_String), end_key: [String](class_string.md#class_String), line_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_codeedit.md#class_CodeEdit_method_add_comment_delimiter)

Adds a comment delimiter from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty [String](class_string.md#class_String), the region does not carry over to the next line.

---

<span id="class_CodeEdit_method_add_string_delimiter"></span>

void **add_string_delimiter** ( start_key: [String](class_string.md#class_String), end_key: [String](class_string.md#class_String), line_only: [bool](class_bool.md#class_bool) = false ) [🔗](class_codeedit.md#class_CodeEdit_method_add_string_delimiter)

Defines a string delimiter from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty [String](class_string.md#class_String), the region does not carry over to the next line.

---

<span id="class_CodeEdit_method_can_fold_line"></span>

[bool](class_bool.md#class_bool) **can_fold_line** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_can_fold_line)

Returns `true` if the given line is foldable. A line is foldable if it is the start of a valid code region (see [get_code_region_start_tag()](class_codeedit.md#class_CodeEdit_method_get_code_region_start_tag)), if it is the start of a comment or string block, or if the next non-empty line is more indented (see [TextEdit.get_indent_level()](class_textedit.md#class_TextEdit_method_get_indent_level)).

---

<span id="class_CodeEdit_method_cancel_code_completion"></span>

void **cancel_code_completion** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_cancel_code_completion)

Cancels the autocomplete menu.

---

<span id="class_CodeEdit_method_clear_bookmarked_lines"></span>

void **clear_bookmarked_lines** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_clear_bookmarked_lines)

Clears all bookmarked lines.

---

<span id="class_CodeEdit_method_clear_breakpointed_lines"></span>

void **clear_breakpointed_lines** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_clear_breakpointed_lines)

Clears all breakpointed lines.

---

<span id="class_CodeEdit_method_clear_comment_delimiters"></span>

void **clear_comment_delimiters** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_clear_comment_delimiters)

Removes all comment delimiters.

---

<span id="class_CodeEdit_method_clear_executing_lines"></span>

void **clear_executing_lines** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_clear_executing_lines)

Clears all executed lines.

---

<span id="class_CodeEdit_method_clear_string_delimiters"></span>

void **clear_string_delimiters** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_clear_string_delimiters)

Removes all string delimiters.

---

<span id="class_CodeEdit_method_confirm_code_completion"></span>

void **confirm_code_completion** ( replace: [bool](class_bool.md#class_bool) = false ) [🔗](class_codeedit.md#class_CodeEdit_method_confirm_code_completion)

Inserts the selected entry into the text. If `replace` is `true`, any existing text is replaced rather than merged.

---

<span id="class_CodeEdit_method_convert_indent"></span>

void **convert_indent** ( from_line: [int](class_int.md#class_int) = -1, to_line: [int](class_int.md#class_int) = -1 ) [🔗](class_codeedit.md#class_CodeEdit_method_convert_indent)

Converts the indents of lines between `from_line` and `to_line` to tabs or spaces as set by [indent_use_spaces](class_codeedit.md#class_CodeEdit_property_indent_use_spaces).

Values of `-1` convert the entire text.

---

<span id="class_CodeEdit_method_create_code_region"></span>

void **create_code_region** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_create_code_region)

Creates a new code region with the selection. At least one single line comment delimiter have to be defined (see [add_comment_delimiter()](class_codeedit.md#class_CodeEdit_method_add_comment_delimiter)).

A code region is a part of code that is highlighted when folded and can help organize your script.

Code region start and end tags can be customized (see [set_code_region_tags()](class_codeedit.md#class_CodeEdit_method_set_code_region_tags)).

Code regions are delimited using start and end tags (respectively `region` and `endregion` by default) preceded by one line comment delimiter. (eg. `#region` and `#endregion`)

---

<span id="class_CodeEdit_method_delete_lines"></span>

void **delete_lines** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_delete_lines)

Deletes all lines that are selected or have a caret on them.

---

<span id="class_CodeEdit_method_do_indent"></span>

void **do_indent** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_do_indent)

If there is no selection, indentation is inserted at the caret. Otherwise, the selected lines are indented like [indent_lines()](class_codeedit.md#class_CodeEdit_method_indent_lines). Equivalent to the ProjectSettings.input/ui_text_indent action. The indentation characters used depend on [indent_use_spaces](class_codeedit.md#class_CodeEdit_property_indent_use_spaces) and [indent_size](class_codeedit.md#class_CodeEdit_property_indent_size).

---

<span id="class_CodeEdit_method_duplicate_lines"></span>

void **duplicate_lines** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_duplicate_lines)

Duplicates all lines currently selected with any caret. Duplicates the entire line beneath the current one no matter where the caret is within the line.

---

<span id="class_CodeEdit_method_duplicate_selection"></span>

void **duplicate_selection** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_duplicate_selection)

Duplicates all selected text and duplicates all lines with a caret on them.

---

<span id="class_CodeEdit_method_fold_all_lines"></span>

void **fold_all_lines** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_fold_all_lines)

Folds all lines that are possible to be folded (see [can_fold_line()](class_codeedit.md#class_CodeEdit_method_can_fold_line)).

---

<span id="class_CodeEdit_method_fold_line"></span>

void **fold_line** ( line: [int](class_int.md#class_int) ) [🔗](class_codeedit.md#class_CodeEdit_method_fold_line)

Folds the given line, if possible (see [can_fold_line()](class_codeedit.md#class_CodeEdit_method_can_fold_line)).

---

<span id="class_CodeEdit_method_get_auto_brace_completion_close_key"></span>

[String](class_string.md#class_String) **get_auto_brace_completion_close_key** ( open_key: [String](class_string.md#class_String) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_auto_brace_completion_close_key)

Gets the matching auto brace close key for `open_key`.

---

<span id="class_CodeEdit_method_get_bookmarked_lines"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_bookmarked_lines** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_bookmarked_lines)

Gets all bookmarked lines.

---

<span id="class_CodeEdit_method_get_breakpointed_lines"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_breakpointed_lines** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_breakpointed_lines)

Gets all breakpointed lines.

---

<span id="class_CodeEdit_method_get_code_completion_option"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_code_completion_option** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_code_completion_option)

Gets the completion option at `index`. The return [Dictionary](class_dictionary.md#class_Dictionary) has the following key-values:

 `kind`: [CodeCompletionKind](class_codeedit.md#enum_CodeEdit_CodeCompletionKind)

 `display_text`: Text that is shown on the autocomplete menu.

 `insert_text`: Text that is to be inserted when this item is selected.

 `font_color`: Color of the text on the autocomplete menu.

 `icon`: Icon to draw on the autocomplete menu.

 `default_value`: Value of the symbol.

---

<span id="class_CodeEdit_method_get_code_completion_options"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_code_completion_options** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_code_completion_options)

Gets all completion options, see [get_code_completion_option()](class_codeedit.md#class_CodeEdit_method_get_code_completion_option) for return content.

---

<span id="class_CodeEdit_method_get_code_completion_selected_index"></span>

[int](class_int.md#class_int) **get_code_completion_selected_index** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_code_completion_selected_index)

Gets the index of the current selected completion option.

---

<span id="class_CodeEdit_method_get_code_region_end_tag"></span>

[String](class_string.md#class_String) **get_code_region_end_tag** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_code_region_end_tag)

Returns the code region end tag (without comment delimiter).

---

<span id="class_CodeEdit_method_get_code_region_start_tag"></span>

[String](class_string.md#class_String) **get_code_region_start_tag** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_code_region_start_tag)

Returns the code region start tag (without comment delimiter).

---

<span id="class_CodeEdit_method_get_delimiter_end_key"></span>

[String](class_string.md#class_String) **get_delimiter_end_key** ( delimiter_index: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_delimiter_end_key)

Gets the end key for a string or comment region index.

---

<span id="class_CodeEdit_method_get_delimiter_end_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_delimiter_end_position** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_delimiter_end_position)

If `line` `column` is in a string or comment, returns the end position of the region. If not or no end could be found, both [Vector2](class_vector2.md#class_Vector2) values will be `-1`.

---

<span id="class_CodeEdit_method_get_delimiter_start_key"></span>

[String](class_string.md#class_String) **get_delimiter_start_key** ( delimiter_index: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_delimiter_start_key)

Gets the start key for a string or comment region index.

---

<span id="class_CodeEdit_method_get_delimiter_start_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_delimiter_start_position** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_delimiter_start_position)

If `line` `column` is in a string or comment, returns the start position of the region. If not or no start could be found, both [Vector2](class_vector2.md#class_Vector2) values will be `-1`.

---

<span id="class_CodeEdit_method_get_executing_lines"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_executing_lines** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_executing_lines)

Gets all executing lines.

---

<span id="class_CodeEdit_method_get_folded_lines"></span>

[Array](class_array.md#class_Array)\[[int](class_int.md#class_int)\] **get_folded_lines** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_folded_lines)

Returns all lines that are currently folded.

---

<span id="class_CodeEdit_method_get_text_for_code_completion"></span>

[String](class_string.md#class_String) **get_text_for_code_completion** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_text_for_code_completion)

Returns the full text with char `0xFFFF` at the caret location.

---

<span id="class_CodeEdit_method_get_text_for_symbol_lookup"></span>

[String](class_string.md#class_String) **get_text_for_symbol_lookup** ( ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_text_for_symbol_lookup)

Returns the full text with char `0xFFFF` at the cursor location.

---

<span id="class_CodeEdit_method_get_text_with_cursor_char"></span>

[String](class_string.md#class_String) **get_text_with_cursor_char** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_get_text_with_cursor_char)

Returns the full text with char `0xFFFF` at the specified location.

---

<span id="class_CodeEdit_method_has_auto_brace_completion_close_key"></span>

[bool](class_bool.md#class_bool) **has_auto_brace_completion_close_key** ( close_key: [String](class_string.md#class_String) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_has_auto_brace_completion_close_key)

Returns `true` if close key `close_key` exists.

---

<span id="class_CodeEdit_method_has_auto_brace_completion_open_key"></span>

[bool](class_bool.md#class_bool) **has_auto_brace_completion_open_key** ( open_key: [String](class_string.md#class_String) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_has_auto_brace_completion_open_key)

Returns `true` if open key `open_key` exists.

---

<span id="class_CodeEdit_method_has_comment_delimiter"></span>

[bool](class_bool.md#class_bool) **has_comment_delimiter** ( start_key: [String](class_string.md#class_String) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_has_comment_delimiter)

Returns `true` if comment `start_key` exists.

---

<span id="class_CodeEdit_method_has_string_delimiter"></span>

[bool](class_bool.md#class_bool) **has_string_delimiter** ( start_key: [String](class_string.md#class_String) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_has_string_delimiter)

Returns `true` if string `start_key` exists.

---

<span id="class_CodeEdit_method_indent_lines"></span>

void **indent_lines** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_indent_lines)

Indents all lines that are selected or have a caret on them. Uses spaces or a tab depending on [indent_use_spaces](class_codeedit.md#class_CodeEdit_property_indent_use_spaces). See [unindent_lines()](class_codeedit.md#class_CodeEdit_method_unindent_lines).

---

<span id="class_CodeEdit_method_is_in_comment"></span>

[int](class_int.md#class_int) **is_in_comment** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_is_in_comment)

Returns delimiter index if `line` `column` is in a comment. If `column` is not provided, will return delimiter index if the entire `line` is a comment. Otherwise `-1`.

---

<span id="class_CodeEdit_method_is_in_string"></span>

[int](class_int.md#class_int) **is_in_string** ( line: [int](class_int.md#class_int), column: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_is_in_string)

Returns the delimiter index if `line` `column` is in a string. If `column` is not provided, will return the delimiter index if the entire `line` is a string. Otherwise `-1`.

---

<span id="class_CodeEdit_method_is_line_bookmarked"></span>

[bool](class_bool.md#class_bool) **is_line_bookmarked** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_is_line_bookmarked)

Returns `true` if the given line is bookmarked. See [set_line_as_bookmarked()](class_codeedit.md#class_CodeEdit_method_set_line_as_bookmarked).

---

<span id="class_CodeEdit_method_is_line_breakpointed"></span>

[bool](class_bool.md#class_bool) **is_line_breakpointed** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_is_line_breakpointed)

Returns `true` if the given line is breakpointed. See [set_line_as_breakpoint()](class_codeedit.md#class_CodeEdit_method_set_line_as_breakpoint).

---

<span id="class_CodeEdit_method_is_line_code_region_end"></span>

[bool](class_bool.md#class_bool) **is_line_code_region_end** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_is_line_code_region_end)

Returns `true` if the given line is a code region end. See [set_code_region_tags()](class_codeedit.md#class_CodeEdit_method_set_code_region_tags).

---

<span id="class_CodeEdit_method_is_line_code_region_start"></span>

[bool](class_bool.md#class_bool) **is_line_code_region_start** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_is_line_code_region_start)

Returns `true` if the given line is a code region start. See [set_code_region_tags()](class_codeedit.md#class_CodeEdit_method_set_code_region_tags).

---

<span id="class_CodeEdit_method_is_line_executing"></span>

[bool](class_bool.md#class_bool) **is_line_executing** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_is_line_executing)

Returns `true` if the given line is marked as executing. See [set_line_as_executing()](class_codeedit.md#class_CodeEdit_method_set_line_as_executing).

---

<span id="class_CodeEdit_method_is_line_folded"></span>

[bool](class_bool.md#class_bool) **is_line_folded** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_codeedit.md#class_CodeEdit_method_is_line_folded)

Returns `true` if the given line is folded. See [fold_line()](class_codeedit.md#class_CodeEdit_method_fold_line).

---

<span id="class_CodeEdit_method_move_lines_down"></span>

void **move_lines_down** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_move_lines_down)

Moves all lines down that are selected or have a caret on them.

---

<span id="class_CodeEdit_method_move_lines_up"></span>

void **move_lines_up** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_move_lines_up)

Moves all lines up that are selected or have a caret on them.

---

<span id="class_CodeEdit_method_remove_comment_delimiter"></span>

void **remove_comment_delimiter** ( start_key: [String](class_string.md#class_String) ) [🔗](class_codeedit.md#class_CodeEdit_method_remove_comment_delimiter)

Removes the comment delimiter with `start_key`.

---

<span id="class_CodeEdit_method_remove_string_delimiter"></span>

void **remove_string_delimiter** ( start_key: [String](class_string.md#class_String) ) [🔗](class_codeedit.md#class_CodeEdit_method_remove_string_delimiter)

Removes the string delimiter with `start_key`.

---

<span id="class_CodeEdit_method_request_code_completion"></span>

void **request_code_completion** ( force: [bool](class_bool.md#class_bool) = false ) [🔗](class_codeedit.md#class_CodeEdit_method_request_code_completion)

Emits [code_completion_requested](class_codeedit.md#class_CodeEdit_signal_code_completion_requested), if `force` is `true` will bypass all checks. Otherwise will check that the caret is in a word or in front of a prefix. Will ignore the request if all current options are of type file path, node path, or signal.

---

<span id="class_CodeEdit_method_set_code_completion_selected_index"></span>

void **set_code_completion_selected_index** ( index: [int](class_int.md#class_int) ) [🔗](class_codeedit.md#class_CodeEdit_method_set_code_completion_selected_index)

Sets the current selected completion option.

---

<span id="class_CodeEdit_method_set_code_hint"></span>

void **set_code_hint** ( code_hint: [String](class_string.md#class_String) ) [🔗](class_codeedit.md#class_CodeEdit_method_set_code_hint)

Sets the code hint text. Pass an empty string to clear.

---

<span id="class_CodeEdit_method_set_code_hint_draw_below"></span>

void **set_code_hint_draw_below** ( draw_below: [bool](class_bool.md#class_bool) ) [🔗](class_codeedit.md#class_CodeEdit_method_set_code_hint_draw_below)

If `true`, the code hint will draw below the main caret. If `false`, the code hint will draw above the main caret. See [set_code_hint()](class_codeedit.md#class_CodeEdit_method_set_code_hint).

---

<span id="class_CodeEdit_method_set_code_region_tags"></span>

void **set_code_region_tags** ( start: [String](class_string.md#class_String) = "region", end: [String](class_string.md#class_String) = "endregion" ) [🔗](class_codeedit.md#class_CodeEdit_method_set_code_region_tags)

Sets the code region start and end tags (without comment delimiter).

---

<span id="class_CodeEdit_method_set_line_as_bookmarked"></span>

void **set_line_as_bookmarked** ( line: [int](class_int.md#class_int), bookmarked: [bool](class_bool.md#class_bool) ) [🔗](class_codeedit.md#class_CodeEdit_method_set_line_as_bookmarked)

Sets the given line as bookmarked. If `true` and [gutters_draw_bookmarks](class_codeedit.md#class_CodeEdit_property_gutters_draw_bookmarks) is `true`, draws the [bookmark](class_codeedit.md#class_CodeEdit_theme_icon_bookmark) icon in the gutter for this line. See [get_bookmarked_lines()](class_codeedit.md#class_CodeEdit_method_get_bookmarked_lines) and [is_line_bookmarked()](class_codeedit.md#class_CodeEdit_method_is_line_bookmarked).

---

<span id="class_CodeEdit_method_set_line_as_breakpoint"></span>

void **set_line_as_breakpoint** ( line: [int](class_int.md#class_int), breakpointed: [bool](class_bool.md#class_bool) ) [🔗](class_codeedit.md#class_CodeEdit_method_set_line_as_breakpoint)

Sets the given line as a breakpoint. If `true` and [gutters_draw_breakpoints_gutter](class_codeedit.md#class_CodeEdit_property_gutters_draw_breakpoints_gutter) is `true`, draws the [breakpoint](class_codeedit.md#class_CodeEdit_theme_icon_breakpoint) icon in the gutter for this line. See [get_breakpointed_lines()](class_codeedit.md#class_CodeEdit_method_get_breakpointed_lines) and [is_line_breakpointed()](class_codeedit.md#class_CodeEdit_method_is_line_breakpointed).

---

<span id="class_CodeEdit_method_set_line_as_executing"></span>

void **set_line_as_executing** ( line: [int](class_int.md#class_int), executing: [bool](class_bool.md#class_bool) ) [🔗](class_codeedit.md#class_CodeEdit_method_set_line_as_executing)

Sets the given line as executing. If `true` and [gutters_draw_executing_lines](class_codeedit.md#class_CodeEdit_property_gutters_draw_executing_lines) is `true`, draws the [executing_line](class_codeedit.md#class_CodeEdit_theme_icon_executing_line) icon in the gutter for this line. See [get_executing_lines()](class_codeedit.md#class_CodeEdit_method_get_executing_lines) and [is_line_executing()](class_codeedit.md#class_CodeEdit_method_is_line_executing).

---

<span id="class_CodeEdit_method_set_symbol_lookup_word_as_valid"></span>

void **set_symbol_lookup_word_as_valid** ( valid: [bool](class_bool.md#class_bool) ) [🔗](class_codeedit.md#class_CodeEdit_method_set_symbol_lookup_word_as_valid)

Sets the symbol emitted by [symbol_validate](class_codeedit.md#class_CodeEdit_signal_symbol_validate) as a valid lookup.

---

<span id="class_CodeEdit_method_toggle_foldable_line"></span>

void **toggle_foldable_line** ( line: [int](class_int.md#class_int) ) [🔗](class_codeedit.md#class_CodeEdit_method_toggle_foldable_line)

Toggle the folding of the code block at the given line.

---

<span id="class_CodeEdit_method_toggle_foldable_lines_at_carets"></span>

void **toggle_foldable_lines_at_carets** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_toggle_foldable_lines_at_carets)

Toggle the folding of the code block on all lines with a caret on them.

---

<span id="class_CodeEdit_method_unfold_all_lines"></span>

void **unfold_all_lines** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_unfold_all_lines)

Unfolds all lines that are folded.

---

<span id="class_CodeEdit_method_unfold_line"></span>

void **unfold_line** ( line: [int](class_int.md#class_int) ) [🔗](class_codeedit.md#class_CodeEdit_method_unfold_line)

Unfolds the given line if it is folded or if it is hidden under a folded line.

---

<span id="class_CodeEdit_method_unindent_lines"></span>

void **unindent_lines** ( ) [🔗](class_codeedit.md#class_CodeEdit_method_unindent_lines)

Unindents all lines that are selected or have a caret on them. Uses spaces or a tab depending on [indent_use_spaces](class_codeedit.md#class_CodeEdit_property_indent_use_spaces). Equivalent to the ProjectSettings.input/ui_text_dedent action. See [indent_lines()](class_codeedit.md#class_CodeEdit_method_indent_lines).

---

<span id="class_CodeEdit_method_update_code_completion_options"></span>

void **update_code_completion_options** ( force: [bool](class_bool.md#class_bool) ) [🔗](class_codeedit.md#class_CodeEdit_method_update_code_completion_options)

Submits all completion options added with [add_code_completion_option()](class_codeedit.md#class_CodeEdit_method_add_code_completion_option). Will try to force the autocomplete menu to popup, if `force` is `true`.

 **Note:** This will replace all current candidates.

---

### Theme Property Descriptions

<span id="class_CodeEdit_theme_color_bookmark_color"></span>

[Color](class_color.md#class_Color) **bookmark_color** = `Color(0.5, 0.64, 1, 0.8)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_bookmark_color)

[Color](class_color.md#class_Color) of the bookmark icon for bookmarked lines.

---

<span id="class_CodeEdit_theme_color_brace_mismatch_color"></span>

[Color](class_color.md#class_Color) **brace_mismatch_color** = `Color(1, 0.2, 0.2, 1)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_brace_mismatch_color)

[Color](class_color.md#class_Color) of the text to highlight mismatched braces.

---

<span id="class_CodeEdit_theme_color_breakpoint_color"></span>

[Color](class_color.md#class_Color) **breakpoint_color** = `Color(0.9, 0.29, 0.3, 1)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_breakpoint_color)

[Color](class_color.md#class_Color) of the breakpoint icon for bookmarked lines.

---

<span id="class_CodeEdit_theme_color_code_folding_color"></span>

[Color](class_color.md#class_Color) **code_folding_color** = `Color(0.8, 0.8, 0.8, 0.8)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_code_folding_color)

[Color](class_color.md#class_Color) for all icons related to line folding.

---

<span id="class_CodeEdit_theme_color_completion_background_color"></span>

[Color](class_color.md#class_Color) **completion_background_color** = `Color(0.17, 0.16, 0.2, 1)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_completion_background_color)

Sets the background [Color](class_color.md#class_Color) for the code completion popup.

---

<span id="class_CodeEdit_theme_color_completion_existing_color"></span>

[Color](class_color.md#class_Color) **completion_existing_color** = `Color(0.87, 0.87, 0.87, 0.13)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_completion_existing_color)

Background highlight [Color](class_color.md#class_Color) for matching text in code completion options.

---

<span id="class_CodeEdit_theme_color_completion_scroll_color"></span>

[Color](class_color.md#class_Color) **completion_scroll_color** = `Color(1, 1, 1, 0.29)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_completion_scroll_color)

[Color](class_color.md#class_Color) of the scrollbar in the code completion popup.

---

<span id="class_CodeEdit_theme_color_completion_scroll_hovered_color"></span>

[Color](class_color.md#class_Color) **completion_scroll_hovered_color** = `Color(1, 1, 1, 0.4)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_completion_scroll_hovered_color)

[Color](class_color.md#class_Color) of the scrollbar in the code completion popup when hovered.

---

<span id="class_CodeEdit_theme_color_completion_selected_color"></span>

[Color](class_color.md#class_Color) **completion_selected_color** = `Color(0.26, 0.26, 0.27, 1)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_completion_selected_color)

Background highlight [Color](class_color.md#class_Color) for the current selected option item in the code completion popup.

---

<span id="class_CodeEdit_theme_color_executing_line_color"></span>

[Color](class_color.md#class_Color) **executing_line_color** = `Color(0.98, 0.89, 0.27, 1)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_executing_line_color)

[Color](class_color.md#class_Color) of the executing icon for executing lines.

---

<span id="class_CodeEdit_theme_color_folded_code_region_color"></span>

[Color](class_color.md#class_Color) **folded_code_region_color** = `Color(0.68, 0.46, 0.77, 0.2)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_folded_code_region_color)

[Color](class_color.md#class_Color) of background line highlight for folded code region.

---

<span id="class_CodeEdit_theme_color_line_length_guideline_color"></span>

[Color](class_color.md#class_Color) **line_length_guideline_color** = `Color(0.3, 0.5, 0.8, 0.1)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_line_length_guideline_color)

[Color](class_color.md#class_Color) of the main line length guideline, secondary guidelines will have 50% alpha applied.

---

<span id="class_CodeEdit_theme_color_line_number_color"></span>

[Color](class_color.md#class_Color) **line_number_color** = `Color(0.67, 0.67, 0.67, 0.4)` [🔗](class_codeedit.md#class_CodeEdit_theme_color_line_number_color)

Sets the [Color](class_color.md#class_Color) of line numbers.

---

<span id="class_CodeEdit_theme_constant_completion_lines"></span>

[int](class_int.md#class_int) **completion_lines** = `7` [🔗](class_codeedit.md#class_CodeEdit_theme_constant_completion_lines)

Max number of options to display in the code completion popup at any one time.

---

<span id="class_CodeEdit_theme_constant_completion_max_width"></span>

[int](class_int.md#class_int) **completion_max_width** = `50` [🔗](class_codeedit.md#class_CodeEdit_theme_constant_completion_max_width)

Max width of options in the code completion popup. Options longer than this will be cut off.

---

<span id="class_CodeEdit_theme_constant_completion_scroll_width"></span>

[int](class_int.md#class_int) **completion_scroll_width** = `6` [🔗](class_codeedit.md#class_CodeEdit_theme_constant_completion_scroll_width)

Width of the scrollbar in the code completion popup.

---

<span id="class_CodeEdit_theme_icon_bookmark"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **bookmark** [🔗](class_codeedit.md#class_CodeEdit_theme_icon_bookmark)

Sets a custom [Texture2D](class_texture2d.md#class_Texture2D) to draw in the bookmark gutter for bookmarked lines.

---

<span id="class_CodeEdit_theme_icon_breakpoint"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **breakpoint** [🔗](class_codeedit.md#class_CodeEdit_theme_icon_breakpoint)

Sets a custom [Texture2D](class_texture2d.md#class_Texture2D) to draw in the breakpoint gutter for breakpointed lines.

---

<span id="class_CodeEdit_theme_icon_can_fold"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **can_fold** [🔗](class_codeedit.md#class_CodeEdit_theme_icon_can_fold)

Sets a custom [Texture2D](class_texture2d.md#class_Texture2D) to draw in the line folding gutter when a line can be folded.

---

<span id="class_CodeEdit_theme_icon_can_fold_code_region"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **can_fold_code_region** [🔗](class_codeedit.md#class_CodeEdit_theme_icon_can_fold_code_region)

Sets a custom [Texture2D](class_texture2d.md#class_Texture2D) to draw in the line folding gutter when a code region can be folded.

---

<span id="class_CodeEdit_theme_icon_completion_color_bg"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **completion_color_bg** [🔗](class_codeedit.md#class_CodeEdit_theme_icon_completion_color_bg)

Background panel for the color preview box in autocompletion (visible when the color is translucent).

---

<span id="class_CodeEdit_theme_icon_executing_line"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **executing_line** [🔗](class_codeedit.md#class_CodeEdit_theme_icon_executing_line)

Icon to draw in the executing gutter for executing lines.

---

<span id="class_CodeEdit_theme_icon_folded"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **folded** [🔗](class_codeedit.md#class_CodeEdit_theme_icon_folded)

Sets a custom [Texture2D](class_texture2d.md#class_Texture2D) to draw in the line folding gutter when a line is folded and can be unfolded.

---

<span id="class_CodeEdit_theme_icon_folded_code_region"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **folded_code_region** [🔗](class_codeedit.md#class_CodeEdit_theme_icon_folded_code_region)

Sets a custom [Texture2D](class_texture2d.md#class_Texture2D) to draw in the line folding gutter when a code region is folded and can be unfolded.

---

<span id="class_CodeEdit_theme_icon_folded_eol_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **folded_eol_icon** [🔗](class_codeedit.md#class_CodeEdit_theme_icon_folded_eol_icon)

Sets a custom [Texture2D](class_texture2d.md#class_Texture2D) to draw at the end of a folded line.

---

<span id="class_CodeEdit_theme_style_completion"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **completion** [🔗](class_codeedit.md#class_CodeEdit_theme_style_completion)

[StyleBox](class_stylebox.md#class_StyleBox) for the code completion popup.
