<span id="class_RichTextLabel"></span>

## RichTextLabel

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A control for displaying text that can contain different font styles, images, and basic formatting.

### Description

A control for displaying text that can contain custom fonts, images, and basic formatting. **RichTextLabel** manages these as an internal tag stack. It also adapts itself to given width/heights.

 **Note:** [newline()](class_richtextlabel.md#class_RichTextLabel_method_newline), [push_paragraph()](class_richtextlabel.md#class_RichTextLabel_method_push_paragraph), `"\n"`, `"\r\n"`, `p` tag, and alignment tags start a new paragraph. Each paragraph is processed independently, in its own BiDi context. If you want to force line wrapping within paragraph, any other line breaking character can be used, for example, Form Feed (U+000C), Next Line (U+0085), Line Separator (U+2028).

 **Note:** Assignments to [text](class_richtextlabel.md#class_RichTextLabel_property_text) clear the tag stack and reconstruct it from the property's contents. Any edits made to [text](class_richtextlabel.md#class_RichTextLabel_property_text) will erase previous edits made from other manual sources such as [append_text()](class_richtextlabel.md#class_RichTextLabel_method_append_text) and the `push_*` / [pop()](class_richtextlabel.md#class_RichTextLabel_method_pop) methods.

 **Note:** RichTextLabel doesn't support entangled BBCode tags. For example, instead of using `[b]bold[i]bold italic[/b]italic[/i]`, use `[b]bold[i]bold italic[/i][/b][i]italic[/i]`.

 **Note:** `push_*/pop_*` functions won't affect BBCode.

 **Note:** While [bbcode_enabled](class_richtextlabel.md#class_RichTextLabel_property_bbcode_enabled) is enabled, alignment tags such as `[center]` will take priority over the [horizontal_alignment](class_richtextlabel.md#class_RichTextLabel_property_horizontal_alignment) setting which determines the default text alignment.

### Tutorials

- [BBCode in RichTextLabel](../tutorials/ui/bbcode_in_richtextlabel.md)

- Rich Text Label with BBCode Demo

- Operating System Testing Demo

### Properties


| [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) | [autowrap_mode](class_richtextlabel.md#class_RichTextLabel_property_autowrap_mode) | `3` |
| --- | --- | --- |
| bitfield | \[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] | [autowrap_trim_flags](class_richtextlabel.md#class_RichTextLabel_property_autowrap_trim_flags) | `192` |
| [bool](class_bool.md#class_bool) | [bbcode_enabled](class_richtextlabel.md#class_RichTextLabel_property_bbcode_enabled) | `false` |
| [bool](class_bool.md#class_bool) | clip_contents | `true` (overrides [Control](class_control.md#class_Control_property_clip_contents)) |
| [bool](class_bool.md#class_bool) | [context_menu_enabled](class_richtextlabel.md#class_RichTextLabel_property_context_menu_enabled) | `false` |
| [Array](class_array.md#class_Array) | [custom_effects](class_richtextlabel.md#class_RichTextLabel_property_custom_effects) | `[]` |
| [bool](class_bool.md#class_bool) | [deselect_on_focus_loss_enabled](class_richtextlabel.md#class_RichTextLabel_property_deselect_on_focus_loss_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [drag_and_drop_selection_enabled](class_richtextlabel.md#class_RichTextLabel_property_drag_and_drop_selection_enabled) | `true` |
| [bool](class_bool.md#class_bool) | [fit_content](class_richtextlabel.md#class_RichTextLabel_property_fit_content) | `false` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `3` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [bool](class_bool.md#class_bool) | [hint_underlined](class_richtextlabel.md#class_RichTextLabel_property_hint_underlined) | `true` |
| HorizontalAlignment | [horizontal_alignment](class_richtextlabel.md#class_RichTextLabel_property_horizontal_alignment) | `0` |
| bitfield | \[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] | [justification_flags](class_richtextlabel.md#class_RichTextLabel_property_justification_flags) | `163` |
| [String](class_string.md#class_String) | [language](class_richtextlabel.md#class_RichTextLabel_property_language) | `""` |
| [bool](class_bool.md#class_bool) | [meta_underlined](class_richtextlabel.md#class_RichTextLabel_property_meta_underlined) | `true` |
| [int](class_int.md#class_int) | [progress_bar_delay](class_richtextlabel.md#class_RichTextLabel_property_progress_bar_delay) | `1000` |
| [bool](class_bool.md#class_bool) | [scroll_active](class_richtextlabel.md#class_RichTextLabel_property_scroll_active) | `true` |
| [bool](class_bool.md#class_bool) | [scroll_following](class_richtextlabel.md#class_RichTextLabel_property_scroll_following) | `false` |
| [bool](class_bool.md#class_bool) | [scroll_following_visible_characters](class_richtextlabel.md#class_RichTextLabel_property_scroll_following_visible_characters) | `false` |
| [bool](class_bool.md#class_bool) | [selection_enabled](class_richtextlabel.md#class_RichTextLabel_property_selection_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [shortcut_keys_enabled](class_richtextlabel.md#class_RichTextLabel_property_shortcut_keys_enabled) | `true` |
| [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) | [structured_text_bidi_override](class_richtextlabel.md#class_RichTextLabel_property_structured_text_bidi_override) | `0` |
| [Array](class_array.md#class_Array) | [structured_text_bidi_override_options](class_richtextlabel.md#class_RichTextLabel_property_structured_text_bidi_override_options) | `[]` |
| [int](class_int.md#class_int) | [tab_size](class_richtextlabel.md#class_RichTextLabel_property_tab_size) | `4` |
| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [tab_stops](class_richtextlabel.md#class_RichTextLabel_property_tab_stops) | `PackedFloat32Array()` |
| [String](class_string.md#class_String) | [text](class_richtextlabel.md#class_RichTextLabel_property_text) | `""` |
| [TextDirection](class_control.md#enum_Control_TextDirection) | [text_direction](class_richtextlabel.md#class_RichTextLabel_property_text_direction) | `0` |
| [bool](class_bool.md#class_bool) | [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) | `false` |
| VerticalAlignment | [vertical_alignment](class_richtextlabel.md#class_RichTextLabel_property_vertical_alignment) | `0` |
| [int](class_int.md#class_int) | [visible_characters](class_richtextlabel.md#class_RichTextLabel_property_visible_characters) | `-1` |
| [VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) | [visible_characters_behavior](class_richtextlabel.md#class_RichTextLabel_property_visible_characters_behavior) | `0` |
| [float](class_float.md#class_float) | [visible_ratio](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio) | `1.0` |

### Methods


| void | [add_hr](class_richtextlabel.md#class_RichTextLabel_method_add_hr) ( width: [int](class_int.md#class_int) = 90, height: [int](class_int.md#class_int) = 2, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), alignment: HorizontalAlignment = 1, width_in_percent: [bool](class_bool.md#class_bool) = true, height_in_percent: [bool](class_bool.md#class_bool) = false ) |
| --- | --- |
| void | [add_image](class_richtextlabel.md#class_RichTextLabel_method_add_image) ( image: [Texture2D](class_texture2d.md#class_Texture2D), width: [int](class_int.md#class_int) = 0, height: [int](class_int.md#class_int) = 0, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), inline_align: InlineAlignment = 5, region: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), key: [Variant](class_variant.md#class_Variant) = null, pad: [bool](class_bool.md#class_bool) = false, tooltip: [String](class_string.md#class_String) = "", width_in_percent: [bool](class_bool.md#class_bool) = false, height_in_percent: [bool](class_bool.md#class_bool) = false, alt_text: [String](class_string.md#class_String) = "" ) |
| void | [add_text](class_richtextlabel.md#class_RichTextLabel_method_add_text) ( text: [String](class_string.md#class_String) ) |
| void | [append_text](class_richtextlabel.md#class_RichTextLabel_method_append_text) ( bbcode: [String](class_string.md#class_String) ) |
| void | [clear](class_richtextlabel.md#class_RichTextLabel_method_clear) ( ) |
| void | [deselect](class_richtextlabel.md#class_RichTextLabel_method_deselect) ( ) |
| [int](class_int.md#class_int) | [get_character_line](class_richtextlabel.md#class_RichTextLabel_method_get_character_line) ( character: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_character_paragraph](class_richtextlabel.md#class_RichTextLabel_method_get_character_paragraph) ( character: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_content_height](class_richtextlabel.md#class_RichTextLabel_method_get_content_height) ( ) const |
| [int](class_int.md#class_int) | [get_content_width](class_richtextlabel.md#class_RichTextLabel_method_get_content_width) ( ) const |
| [int](class_int.md#class_int) | [get_line_count](class_richtextlabel.md#class_RichTextLabel_method_get_line_count) ( ) const |
| [int](class_int.md#class_int) | [get_line_height](class_richtextlabel.md#class_RichTextLabel_method_get_line_height) ( line: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_line_offset](class_richtextlabel.md#class_RichTextLabel_method_get_line_offset) ( line: [int](class_int.md#class_int) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_line_range](class_richtextlabel.md#class_RichTextLabel_method_get_line_range) ( line: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_line_width](class_richtextlabel.md#class_RichTextLabel_method_get_line_width) ( line: [int](class_int.md#class_int) ) const |
| [PopupMenu](class_popupmenu.md#class_PopupMenu) | [get_menu](class_richtextlabel.md#class_RichTextLabel_method_get_menu) ( ) const |
| [int](class_int.md#class_int) | [get_paragraph_count](class_richtextlabel.md#class_RichTextLabel_method_get_paragraph_count) ( ) const |
| [float](class_float.md#class_float) | [get_paragraph_offset](class_richtextlabel.md#class_RichTextLabel_method_get_paragraph_offset) ( paragraph: [int](class_int.md#class_int) ) |
| [String](class_string.md#class_String) | [get_parsed_text](class_richtextlabel.md#class_RichTextLabel_method_get_parsed_text) ( ) const |
| [String](class_string.md#class_String) | [get_selected_text](class_richtextlabel.md#class_RichTextLabel_method_get_selected_text) ( ) const |
| [int](class_int.md#class_int) | [get_selection_from](class_richtextlabel.md#class_RichTextLabel_method_get_selection_from) ( ) const |
| [float](class_float.md#class_float) | [get_selection_line_offset](class_richtextlabel.md#class_RichTextLabel_method_get_selection_line_offset) ( ) const |
| [int](class_int.md#class_int) | [get_selection_to](class_richtextlabel.md#class_RichTextLabel_method_get_selection_to) ( ) const |
| [int](class_int.md#class_int) | [get_total_character_count](class_richtextlabel.md#class_RichTextLabel_method_get_total_character_count) ( ) const |
| [VScrollBar](class_vscrollbar.md#class_VScrollBar) | [get_v_scroll_bar](class_richtextlabel.md#class_RichTextLabel_method_get_v_scroll_bar) ( ) |
| [Rect2i](class_rect2i.md#class_Rect2i) | [get_visible_content_rect](class_richtextlabel.md#class_RichTextLabel_method_get_visible_content_rect) ( ) const |
| [int](class_int.md#class_int) | [get_visible_line_count](class_richtextlabel.md#class_RichTextLabel_method_get_visible_line_count) ( ) const |
| [int](class_int.md#class_int) | [get_visible_paragraph_count](class_richtextlabel.md#class_RichTextLabel_method_get_visible_paragraph_count) ( ) const |
| void | [install_effect](class_richtextlabel.md#class_RichTextLabel_method_install_effect) ( effect: [Variant](class_variant.md#class_Variant) ) |
| [bool](class_bool.md#class_bool) | [invalidate_paragraph](class_richtextlabel.md#class_RichTextLabel_method_invalidate_paragraph) ( paragraph: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [is_finished](class_richtextlabel.md#class_RichTextLabel_method_is_finished) ( ) const |
| [bool](class_bool.md#class_bool) | [is_menu_visible](class_richtextlabel.md#class_RichTextLabel_method_is_menu_visible) ( ) const |
| [bool](class_bool.md#class_bool) | [is_ready](class_richtextlabel.md#class_RichTextLabel_method_is_ready) ( ) const |
| void | [menu_option](class_richtextlabel.md#class_RichTextLabel_method_menu_option) ( option: [int](class_int.md#class_int) ) |
| void | [newline](class_richtextlabel.md#class_RichTextLabel_method_newline) ( ) |
| void | [parse_bbcode](class_richtextlabel.md#class_RichTextLabel_method_parse_bbcode) ( bbcode: [String](class_string.md#class_String) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [parse_expressions_for_values](class_richtextlabel.md#class_RichTextLabel_method_parse_expressions_for_values) ( expressions: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) |
| void | [pop](class_richtextlabel.md#class_RichTextLabel_method_pop) ( ) |
| void | [pop_all](class_richtextlabel.md#class_RichTextLabel_method_pop_all) ( ) |
| void | [pop_context](class_richtextlabel.md#class_RichTextLabel_method_pop_context) ( ) |
| void | [push_bgcolor](class_richtextlabel.md#class_RichTextLabel_method_push_bgcolor) ( bgcolor: [Color](class_color.md#class_Color) ) |
| void | [push_bold](class_richtextlabel.md#class_RichTextLabel_method_push_bold) ( ) |
| void | [push_bold_italics](class_richtextlabel.md#class_RichTextLabel_method_push_bold_italics) ( ) |
| void | [push_cell](class_richtextlabel.md#class_RichTextLabel_method_push_cell) ( ) |
| void | [push_color](class_richtextlabel.md#class_RichTextLabel_method_push_color) ( color: [Color](class_color.md#class_Color) ) |
| void | [push_context](class_richtextlabel.md#class_RichTextLabel_method_push_context) ( ) |
| void | [push_customfx](class_richtextlabel.md#class_RichTextLabel_method_push_customfx) ( effect: [RichTextEffect](class_richtexteffect.md#class_RichTextEffect), env: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| void | [push_dropcap](class_richtextlabel.md#class_RichTextLabel_method_push_dropcap) ( string: [String](class_string.md#class_String), font: [Font](class_font.md#class_Font), size: [int](class_int.md#class_int), dropcap_margins: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), outline_size: [int](class_int.md#class_int) = 0, outline_color: [Color](class_color.md#class_Color) = Color(0, 0, 0, 0) ) |
| void | [push_fgcolor](class_richtextlabel.md#class_RichTextLabel_method_push_fgcolor) ( fgcolor: [Color](class_color.md#class_Color) ) |
| void | [push_font](class_richtextlabel.md#class_RichTextLabel_method_push_font) ( font: [Font](class_font.md#class_Font), font_size: [int](class_int.md#class_int) = 0 ) |
| void | [push_font_size](class_richtextlabel.md#class_RichTextLabel_method_push_font_size) ( font_size: [int](class_int.md#class_int) ) |
| void | [push_hint](class_richtextlabel.md#class_RichTextLabel_method_push_hint) ( description: [String](class_string.md#class_String) ) |
| void | [push_indent](class_richtextlabel.md#class_RichTextLabel_method_push_indent) ( level: [int](class_int.md#class_int) ) |
| void | [push_italics](class_richtextlabel.md#class_RichTextLabel_method_push_italics) ( ) |
| void | [push_language](class_richtextlabel.md#class_RichTextLabel_method_push_language) ( language: [String](class_string.md#class_String) ) |
| void | [push_list](class_richtextlabel.md#class_RichTextLabel_method_push_list) ( level: [int](class_int.md#class_int), type: [ListType](class_richtextlabel.md#enum_RichTextLabel_ListType), capitalize: [bool](class_bool.md#class_bool), bullet: [String](class_string.md#class_String) = "•" ) |
| void | [push_meta](class_richtextlabel.md#class_RichTextLabel_method_push_meta) ( data: [Variant](class_variant.md#class_Variant), underline_mode: [MetaUnderline](class_richtextlabel.md#enum_RichTextLabel_MetaUnderline) = 1, tooltip: [String](class_string.md#class_String) = "" ) |
| void | [push_mono](class_richtextlabel.md#class_RichTextLabel_method_push_mono) ( ) |
| void | [push_normal](class_richtextlabel.md#class_RichTextLabel_method_push_normal) ( ) |
| void | [push_outline_color](class_richtextlabel.md#class_RichTextLabel_method_push_outline_color) ( color: [Color](class_color.md#class_Color) ) |
| void | [push_outline_size](class_richtextlabel.md#class_RichTextLabel_method_push_outline_size) ( outline_size: [int](class_int.md#class_int) ) |
| void | [push_paragraph](class_richtextlabel.md#class_RichTextLabel_method_push_paragraph) ( alignment: HorizontalAlignment, base_direction: [TextDirection](class_control.md#enum_Control_TextDirection) = 0, language: [String](class_string.md#class_String) = "", st_parser: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) = 0, justification_flags: | bitfield | \[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] = 163, tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) = PackedFloat32Array() ) |
| void | [push_strikethrough](class_richtextlabel.md#class_RichTextLabel_method_push_strikethrough) ( color: [Color](class_color.md#class_Color) = Color(0, 0, 0, 0) ) |
| void | [push_table](class_richtextlabel.md#class_RichTextLabel_method_push_table) ( columns: [int](class_int.md#class_int), inline_align: InlineAlignment = 0, align_to_row: [int](class_int.md#class_int) = -1, name: [String](class_string.md#class_String) = "" ) |
| void | [push_underline](class_richtextlabel.md#class_RichTextLabel_method_push_underline) ( color: [Color](class_color.md#class_Color) = Color(0, 0, 0, 0) ) |
| void | [reload_effects](class_richtextlabel.md#class_RichTextLabel_method_reload_effects) ( ) |
| [bool](class_bool.md#class_bool) | [remove_paragraph](class_richtextlabel.md#class_RichTextLabel_method_remove_paragraph) ( paragraph: [int](class_int.md#class_int), no_invalidate: [bool](class_bool.md#class_bool) = false ) |
| void | [scroll_to_line](class_richtextlabel.md#class_RichTextLabel_method_scroll_to_line) ( line: [int](class_int.md#class_int) ) |
| void | [scroll_to_paragraph](class_richtextlabel.md#class_RichTextLabel_method_scroll_to_paragraph) ( paragraph: [int](class_int.md#class_int) ) |
| void | [scroll_to_selection](class_richtextlabel.md#class_RichTextLabel_method_scroll_to_selection) ( ) |
| void | [select_all](class_richtextlabel.md#class_RichTextLabel_method_select_all) ( ) |
| void | [set_cell_border_color](class_richtextlabel.md#class_RichTextLabel_method_set_cell_border_color) ( color: [Color](class_color.md#class_Color) ) |
| void | [set_cell_padding](class_richtextlabel.md#class_RichTextLabel_method_set_cell_padding) ( padding: [Rect2](class_rect2.md#class_Rect2) ) |
| void | [set_cell_row_background_color](class_richtextlabel.md#class_RichTextLabel_method_set_cell_row_background_color) ( odd_row_bg: [Color](class_color.md#class_Color), even_row_bg: [Color](class_color.md#class_Color) ) |
| void | [set_cell_size_override](class_richtextlabel.md#class_RichTextLabel_method_set_cell_size_override) ( min_size: [Vector2](class_vector2.md#class_Vector2), max_size: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_table_column_expand](class_richtextlabel.md#class_RichTextLabel_method_set_table_column_expand) ( column: [int](class_int.md#class_int), expand: [bool](class_bool.md#class_bool), ratio: [int](class_int.md#class_int) = 1, shrink: [bool](class_bool.md#class_bool) = true ) |
| void | [set_table_column_name](class_richtextlabel.md#class_RichTextLabel_method_set_table_column_name) ( column: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [update_image](class_richtextlabel.md#class_RichTextLabel_method_update_image) ( key: [Variant](class_variant.md#class_Variant), mask: | bitfield | \[[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask)\], image: [Texture2D](class_texture2d.md#class_Texture2D), width: [int](class_int.md#class_int) = 0, height: [int](class_int.md#class_int) = 0, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), inline_align: InlineAlignment = 5, region: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), pad: [bool](class_bool.md#class_bool) = false, tooltip: [String](class_string.md#class_String) = "", width_in_percent: [bool](class_bool.md#class_bool) = false, height_in_percent: [bool](class_bool.md#class_bool) = false ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [default_color](class_richtextlabel.md#class_RichTextLabel_theme_color_default_color) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [font_outline_color](class_richtextlabel.md#class_RichTextLabel_theme_color_font_outline_color) | `Color(0, 0, 0, 1)` |
| [Color](class_color.md#class_Color) | [font_selected_color](class_richtextlabel.md#class_RichTextLabel_theme_color_font_selected_color) | `Color(0, 0, 0, 0)` |
| [Color](class_color.md#class_Color) | [font_shadow_color](class_richtextlabel.md#class_RichTextLabel_theme_color_font_shadow_color) | `Color(0, 0, 0, 0)` |
| [Color](class_color.md#class_Color) | [selection_color](class_richtextlabel.md#class_RichTextLabel_theme_color_selection_color) | `Color(0.1, 0.1, 1, 0.8)` |
| [Color](class_color.md#class_Color) | [table_border](class_richtextlabel.md#class_RichTextLabel_theme_color_table_border) | `Color(0, 0, 0, 0)` |
| [Color](class_color.md#class_Color) | [table_even_row_bg](class_richtextlabel.md#class_RichTextLabel_theme_color_table_even_row_bg) | `Color(0, 0, 0, 0)` |
| [Color](class_color.md#class_Color) | [table_odd_row_bg](class_richtextlabel.md#class_RichTextLabel_theme_color_table_odd_row_bg) | `Color(0, 0, 0, 0)` |
| [int](class_int.md#class_int) | [line_separation](class_richtextlabel.md#class_RichTextLabel_theme_constant_line_separation) | `0` |
| [int](class_int.md#class_int) | [outline_size](class_richtextlabel.md#class_RichTextLabel_theme_constant_outline_size) | `0` |
| [int](class_int.md#class_int) | [paragraph_separation](class_richtextlabel.md#class_RichTextLabel_theme_constant_paragraph_separation) | `0` |
| [int](class_int.md#class_int) | [shadow_offset_x](class_richtextlabel.md#class_RichTextLabel_theme_constant_shadow_offset_x) | `1` |
| [int](class_int.md#class_int) | [shadow_offset_y](class_richtextlabel.md#class_RichTextLabel_theme_constant_shadow_offset_y) | `1` |
| [int](class_int.md#class_int) | [shadow_outline_size](class_richtextlabel.md#class_RichTextLabel_theme_constant_shadow_outline_size) | `1` |
| [int](class_int.md#class_int) | [strikethrough_alpha](class_richtextlabel.md#class_RichTextLabel_theme_constant_strikethrough_alpha) | `50` |
| [int](class_int.md#class_int) | [table_h_separation](class_richtextlabel.md#class_RichTextLabel_theme_constant_table_h_separation) | `3` |
| [int](class_int.md#class_int) | [table_v_separation](class_richtextlabel.md#class_RichTextLabel_theme_constant_table_v_separation) | `3` |
| [int](class_int.md#class_int) | [text_highlight_h_padding](class_richtextlabel.md#class_RichTextLabel_theme_constant_text_highlight_h_padding) | `3` |
| [int](class_int.md#class_int) | [text_highlight_v_padding](class_richtextlabel.md#class_RichTextLabel_theme_constant_text_highlight_v_padding) | `3` |
| [int](class_int.md#class_int) | [underline_alpha](class_richtextlabel.md#class_RichTextLabel_theme_constant_underline_alpha) | `50` |
| [Font](class_font.md#class_Font) | [bold_font](class_richtextlabel.md#class_RichTextLabel_theme_font_bold_font) |
| [Font](class_font.md#class_Font) | [bold_italics_font](class_richtextlabel.md#class_RichTextLabel_theme_font_bold_italics_font) |
| [Font](class_font.md#class_Font) | [italics_font](class_richtextlabel.md#class_RichTextLabel_theme_font_italics_font) |
| [Font](class_font.md#class_Font) | [mono_font](class_richtextlabel.md#class_RichTextLabel_theme_font_mono_font) |
| [Font](class_font.md#class_Font) | [normal_font](class_richtextlabel.md#class_RichTextLabel_theme_font_normal_font) |
| [int](class_int.md#class_int) | [bold_font_size](class_richtextlabel.md#class_RichTextLabel_theme_font_size_bold_font_size) |
| [int](class_int.md#class_int) | [bold_italics_font_size](class_richtextlabel.md#class_RichTextLabel_theme_font_size_bold_italics_font_size) |
| [int](class_int.md#class_int) | [italics_font_size](class_richtextlabel.md#class_RichTextLabel_theme_font_size_italics_font_size) |
| [int](class_int.md#class_int) | [mono_font_size](class_richtextlabel.md#class_RichTextLabel_theme_font_size_mono_font_size) |
| [int](class_int.md#class_int) | [normal_font_size](class_richtextlabel.md#class_RichTextLabel_theme_font_size_normal_font_size) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [horizontal_rule](class_richtextlabel.md#class_RichTextLabel_theme_icon_horizontal_rule) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [focus](class_richtextlabel.md#class_RichTextLabel_theme_style_focus) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [normal](class_richtextlabel.md#class_RichTextLabel_theme_style_normal) |

---

### Signals

<span id="class_RichTextLabel_signal_finished"></span>

**finished** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_signal_finished)

Triggered when the document is fully loaded.

 **Note:** This can happen before the text is processed for drawing. Scrolling values may not be valid until the document is drawn for the first time after this signal.

---

<span id="class_RichTextLabel_signal_meta_clicked"></span>

**meta_clicked** ( meta: [Variant](class_variant.md#class_Variant) ) [🔗](class_richtextlabel.md#class_RichTextLabel_signal_meta_clicked)

Triggered when the user clicks on content between meta (URL) tags. If the meta is defined in BBCode, e.g. `[url={"key": "value"}]Text[/url]`, then the parameter for this signal will always be a [String](class_string.md#class_String) type. If a particular type or an object is desired, the [push_meta()](class_richtextlabel.md#class_RichTextLabel_method_push_meta) method must be used to manually insert the data into the tag stack. Alternatively, you can convert the [String](class_string.md#class_String) input to the desired type based on its contents (such as calling [JSON.parse()](class_json.md#class_JSON_method_parse) on it).

For example, the following method can be connected to [meta_clicked](class_richtextlabel.md#class_RichTextLabel_signal_meta_clicked) to open clicked URLs using the user's default web browser:

.. tabs::

```
```

    # This assumes RichTextLabel's `meta_clicked` signal was connected to
    # the function below using the signal connection dialog.
    func _richtextlabel_on_meta_clicked(meta):
        # `meta` is of Variant type, so convert it to a String to avoid script errors at run-time.
        OS.shell_open(str(meta))

---

<span id="class_RichTextLabel_signal_meta_hover_ended"></span>

**meta_hover_ended** ( meta: [Variant](class_variant.md#class_Variant) ) [🔗](class_richtextlabel.md#class_RichTextLabel_signal_meta_hover_ended)

Triggers when the mouse exits a meta tag.

---

<span id="class_RichTextLabel_signal_meta_hover_started"></span>

**meta_hover_started** ( meta: [Variant](class_variant.md#class_Variant) ) [🔗](class_richtextlabel.md#class_RichTextLabel_signal_meta_hover_started)

Triggers when the mouse enters a meta tag.

---

### Enumerations

<span id="enum_RichTextLabel_ListType"></span>

enum **ListType**: [🔗](class_richtextlabel.md#enum_RichTextLabel_ListType)

<span id="class_RichTextLabel_constant_LIST_NUMBERS"></span>

[ListType](class_richtextlabel.md#enum_RichTextLabel_ListType) **LIST_NUMBERS** = `0`

Each list item has a number marker.

<span id="class_RichTextLabel_constant_LIST_LETTERS"></span>

[ListType](class_richtextlabel.md#enum_RichTextLabel_ListType) **LIST_LETTERS** = `1`

Each list item has a letter marker.

<span id="class_RichTextLabel_constant_LIST_ROMAN"></span>

[ListType](class_richtextlabel.md#enum_RichTextLabel_ListType) **LIST_ROMAN** = `2`

Each list item has a roman number marker.

<span id="class_RichTextLabel_constant_LIST_DOTS"></span>

[ListType](class_richtextlabel.md#enum_RichTextLabel_ListType) **LIST_DOTS** = `3`

Each list item has a filled circle marker.

---

<span id="enum_RichTextLabel_MenuItems"></span>

enum **MenuItems**: [🔗](class_richtextlabel.md#enum_RichTextLabel_MenuItems)

<span id="class_RichTextLabel_constant_MENU_COPY"></span>

[MenuItems](class_richtextlabel.md#enum_RichTextLabel_MenuItems) **MENU_COPY** = `0`

Copies the selected text.

<span id="class_RichTextLabel_constant_MENU_SELECT_ALL"></span>

[MenuItems](class_richtextlabel.md#enum_RichTextLabel_MenuItems) **MENU_SELECT_ALL** = `1`

Selects the whole **RichTextLabel** text.

<span id="class_RichTextLabel_constant_MENU_MAX"></span>

[MenuItems](class_richtextlabel.md#enum_RichTextLabel_MenuItems) **MENU_MAX** = `2`

Represents the size of the [MenuItems](class_richtextlabel.md#enum_RichTextLabel_MenuItems) enum.

---

<span id="enum_RichTextLabel_MetaUnderline"></span>

enum **MetaUnderline**: [🔗](class_richtextlabel.md#enum_RichTextLabel_MetaUnderline)

<span id="class_RichTextLabel_constant_META_UNDERLINE_NEVER"></span>

[MetaUnderline](class_richtextlabel.md#enum_RichTextLabel_MetaUnderline) **META_UNDERLINE_NEVER** = `0`

Meta tag does not display an underline, even if [meta_underlined](class_richtextlabel.md#class_RichTextLabel_property_meta_underlined) is `true`.

<span id="class_RichTextLabel_constant_META_UNDERLINE_ALWAYS"></span>

[MetaUnderline](class_richtextlabel.md#enum_RichTextLabel_MetaUnderline) **META_UNDERLINE_ALWAYS** = `1`

If [meta_underlined](class_richtextlabel.md#class_RichTextLabel_property_meta_underlined) is `true`, meta tag always display an underline.

<span id="class_RichTextLabel_constant_META_UNDERLINE_ON_HOVER"></span>

[MetaUnderline](class_richtextlabel.md#enum_RichTextLabel_MetaUnderline) **META_UNDERLINE_ON_HOVER** = `2`

If [meta_underlined](class_richtextlabel.md#class_RichTextLabel_property_meta_underlined) is `true`, meta tag display an underline when the mouse cursor is over it.

---

<span id="enum_RichTextLabel_ImageUpdateMask"></span>

flags **ImageUpdateMask**: [🔗](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask)

<span id="class_RichTextLabel_constant_UPDATE_TEXTURE"></span>

[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask) **UPDATE_TEXTURE** = `1`

If this bit is set, [update_image()](class_richtextlabel.md#class_RichTextLabel_method_update_image) changes image texture.

<span id="class_RichTextLabel_constant_UPDATE_SIZE"></span>

[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask) **UPDATE_SIZE** = `2`

If this bit is set, [update_image()](class_richtextlabel.md#class_RichTextLabel_method_update_image) changes image size.

<span id="class_RichTextLabel_constant_UPDATE_COLOR"></span>

[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask) **UPDATE_COLOR** = `4`

If this bit is set, [update_image()](class_richtextlabel.md#class_RichTextLabel_method_update_image) changes image color.

<span id="class_RichTextLabel_constant_UPDATE_ALIGNMENT"></span>

[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask) **UPDATE_ALIGNMENT** = `8`

If this bit is set, [update_image()](class_richtextlabel.md#class_RichTextLabel_method_update_image) changes image inline alignment.

<span id="class_RichTextLabel_constant_UPDATE_REGION"></span>

[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask) **UPDATE_REGION** = `16`

If this bit is set, [update_image()](class_richtextlabel.md#class_RichTextLabel_method_update_image) changes image texture region.

<span id="class_RichTextLabel_constant_UPDATE_PAD"></span>

[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask) **UPDATE_PAD** = `32`

If this bit is set, [update_image()](class_richtextlabel.md#class_RichTextLabel_method_update_image) changes image padding.

<span id="class_RichTextLabel_constant_UPDATE_TOOLTIP"></span>

[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask) **UPDATE_TOOLTIP** = `64`

If this bit is set, [update_image()](class_richtextlabel.md#class_RichTextLabel_method_update_image) changes image tooltip.

<span id="class_RichTextLabel_constant_UPDATE_WIDTH_IN_PERCENT"></span>

[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask) **UPDATE_WIDTH_IN_PERCENT** = `128`

If this bit is set, [update_image()](class_richtextlabel.md#class_RichTextLabel_method_update_image) changes image width from/to percents.

---

### Property Descriptions

<span id="class_RichTextLabel_property_autowrap_mode"></span>

[AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **autowrap_mode** = `3` [🔗](class_richtextlabel.md#class_RichTextLabel_property_autowrap_mode)

- void **set_autowrap_mode** ( value: [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) )
- [AutowrapMode](class_textserver.md#enum_TextServer_AutowrapMode) **get_autowrap_mode** ( )

If set to something other than [TextServer.AUTOWRAP_OFF](class_textserver.md#class_TextServer_constant_AUTOWRAP_OFF), the text gets wrapped inside the node's bounding rectangle.

---

<span id="class_RichTextLabel_property_autowrap_trim_flags"></span>

*BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **autowrap_trim_flags** = `192` [🔗](class_richtextlabel.md#class_RichTextLabel_property_autowrap_trim_flags)

- void **set_autowrap_trim_flags** ( value: *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] )
- *BitField*\[[LineBreakFlag](class_textserver.md#enum_TextServer_LineBreakFlag)\] **get_autowrap_trim_flags** ( )

Autowrap space trimming flags. See [TextServer.BREAK_TRIM_START_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES) and [TextServer.BREAK_TRIM_END_EDGE_SPACES](class_textserver.md#class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES) for more info.

---

<span id="class_RichTextLabel_property_bbcode_enabled"></span>

[bool](class_bool.md#class_bool) **bbcode_enabled** = `false` [🔗](class_richtextlabel.md#class_RichTextLabel_property_bbcode_enabled)

- void **set_use_bbcode** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_bbcode** ( )

If `true`, the label uses BBCode formatting.

 **Note:** This only affects the contents of [text](class_richtextlabel.md#class_RichTextLabel_property_text), not the tag stack.

---

<span id="class_RichTextLabel_property_context_menu_enabled"></span>

[bool](class_bool.md#class_bool) **context_menu_enabled** = `false` [🔗](class_richtextlabel.md#class_RichTextLabel_property_context_menu_enabled)

- void **set_context_menu_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_context_menu_enabled** ( )

If `true`, a right-click displays the context menu.

---

<span id="class_RichTextLabel_property_custom_effects"></span>

[Array](class_array.md#class_Array) **custom_effects** = `[]` [🔗](class_richtextlabel.md#class_RichTextLabel_property_custom_effects)

- void **set_effects** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_effects** ( )

The currently installed custom effects. This is an array of [RichTextEffect](class_richtexteffect.md#class_RichTextEffect) s.

To add a custom effect, it's more convenient to use [install_effect()](class_richtextlabel.md#class_RichTextLabel_method_install_effect).

---

<span id="class_RichTextLabel_property_deselect_on_focus_loss_enabled"></span>

[bool](class_bool.md#class_bool) **deselect_on_focus_loss_enabled** = `true` [🔗](class_richtextlabel.md#class_RichTextLabel_property_deselect_on_focus_loss_enabled)

- void **set_deselect_on_focus_loss_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_deselect_on_focus_loss_enabled** ( )

If `true`, the selected text will be deselected when focus is lost.

---

<span id="class_RichTextLabel_property_drag_and_drop_selection_enabled"></span>

[bool](class_bool.md#class_bool) **drag_and_drop_selection_enabled** = `true` [🔗](class_richtextlabel.md#class_RichTextLabel_property_drag_and_drop_selection_enabled)

- void **set_drag_and_drop_selection_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_drag_and_drop_selection_enabled** ( )

If `true`, allow drag and drop of selected text.

---

<span id="class_RichTextLabel_property_fit_content"></span>

[bool](class_bool.md#class_bool) **fit_content** = `false` [🔗](class_richtextlabel.md#class_RichTextLabel_property_fit_content)

- void **set_fit_content** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_fit_content_enabled** ( )

If `true`, the label's minimum size will be automatically updated to fit its content, matching the behavior of [Label](class_label.md#class_Label).

---

<span id="class_RichTextLabel_property_hint_underlined"></span>

[bool](class_bool.md#class_bool) **hint_underlined** = `true` [🔗](class_richtextlabel.md#class_RichTextLabel_property_hint_underlined)

- void **set_hint_underline** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_hint_underlined** ( )

If `true`, the label underlines hint tags such as `[hint=description]{text}[/hint]`.

---

<span id="class_RichTextLabel_property_horizontal_alignment"></span>

HorizontalAlignment **horizontal_alignment** = `0` [🔗](class_richtextlabel.md#class_RichTextLabel_property_horizontal_alignment)

- void **set_horizontal_alignment** ( value: HorizontalAlignment )
- HorizontalAlignment **get_horizontal_alignment** ( )

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

---

<span id="class_RichTextLabel_property_justification_flags"></span>

*BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **justification_flags** = `163` [🔗](class_richtextlabel.md#class_RichTextLabel_property_justification_flags)

- void **set_justification_flags** ( value: *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] )
- *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] **get_justification_flags** ( )

Line fill alignment rules.

---

<span id="class_RichTextLabel_property_language"></span>

[String](class_string.md#class_String) **language** = `""` [🔗](class_richtextlabel.md#class_RichTextLabel_property_language)

- void **set_language** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_language** ( )

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

---

<span id="class_RichTextLabel_property_meta_underlined"></span>

[bool](class_bool.md#class_bool) **meta_underlined** = `true` [🔗](class_richtextlabel.md#class_RichTextLabel_property_meta_underlined)

- void **set_meta_underline** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_meta_underlined** ( )

If `true`, the label underlines meta tags such as `[url]{text}[/url]`. These tags can call a function when clicked if [meta_clicked](class_richtextlabel.md#class_RichTextLabel_signal_meta_clicked) is connected to a function.

---

<span id="class_RichTextLabel_property_progress_bar_delay"></span>

[int](class_int.md#class_int) **progress_bar_delay** = `1000` [🔗](class_richtextlabel.md#class_RichTextLabel_property_progress_bar_delay)

- void **set_progress_bar_delay** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_progress_bar_delay** ( )

The delay after which the loading progress bar is displayed, in milliseconds. Set to `-1` to disable progress bar entirely.

 **Note:** Progress bar is displayed only if [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled.

---

<span id="class_RichTextLabel_property_scroll_active"></span>

[bool](class_bool.md#class_bool) **scroll_active** = `true` [🔗](class_richtextlabel.md#class_RichTextLabel_property_scroll_active)

- void **set_scroll_active** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_scroll_active** ( )

If `true`, the scrollbar is visible. Setting this to `false` does not block scrolling completely. See [scroll_to_line()](class_richtextlabel.md#class_RichTextLabel_method_scroll_to_line).

---

<span id="class_RichTextLabel_property_scroll_following"></span>

[bool](class_bool.md#class_bool) **scroll_following** = `false` [🔗](class_richtextlabel.md#class_RichTextLabel_property_scroll_following)

- void **set_scroll_follow** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_scroll_following** ( )

If `true`, the window scrolls down to display new content automatically.

---

<span id="class_RichTextLabel_property_scroll_following_visible_characters"></span>

[bool](class_bool.md#class_bool) **scroll_following_visible_characters** = `false` [🔗](class_richtextlabel.md#class_RichTextLabel_property_scroll_following_visible_characters)

- void **set_scroll_follow_visible_characters** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_scroll_following_visible_characters** ( )

If `true`, the window scrolls to display the last visible line when [visible_characters](class_richtextlabel.md#class_RichTextLabel_property_visible_characters) or [visible_ratio](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio) is changed.

---

<span id="class_RichTextLabel_property_selection_enabled"></span>

[bool](class_bool.md#class_bool) **selection_enabled** = `false` [🔗](class_richtextlabel.md#class_RichTextLabel_property_selection_enabled)

- void **set_selection_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_selection_enabled** ( )

If `true`, the label allows text selection.

---

<span id="class_RichTextLabel_property_shortcut_keys_enabled"></span>

[bool](class_bool.md#class_bool) **shortcut_keys_enabled** = `true` [🔗](class_richtextlabel.md#class_RichTextLabel_property_shortcut_keys_enabled)

- void **set_shortcut_keys_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_shortcut_keys_enabled** ( )

If `true`, shortcut keys for context menu items are enabled, even if the context menu is disabled.

---

<span id="class_RichTextLabel_property_structured_text_bidi_override"></span>

[StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **structured_text_bidi_override** = `0` [🔗](class_richtextlabel.md#class_RichTextLabel_property_structured_text_bidi_override)

- void **set_structured_text_bidi_override** ( value: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) )
- [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) **get_structured_text_bidi_override** ( )

Set BiDi algorithm override for the structured text.

---

<span id="class_RichTextLabel_property_structured_text_bidi_override_options"></span>

[Array](class_array.md#class_Array) **structured_text_bidi_override_options** = `[]` [🔗](class_richtextlabel.md#class_RichTextLabel_property_structured_text_bidi_override_options)

- void **set_structured_text_bidi_override_options** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_structured_text_bidi_override_options** ( )

Set additional options for BiDi override.

---

<span id="class_RichTextLabel_property_tab_size"></span>

[int](class_int.md#class_int) **tab_size** = `4` [🔗](class_richtextlabel.md#class_RichTextLabel_property_tab_size)

- void **set_tab_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_tab_size** ( )

The number of spaces associated with a single tab length. Does not affect `\t` in text tags, only indent tags.

---

<span id="class_RichTextLabel_property_tab_stops"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **tab_stops** = `PackedFloat32Array()` [🔗](class_richtextlabel.md#class_RichTextLabel_property_tab_stops)

- void **set_tab_stops** ( value: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) )
- [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **get_tab_stops** ( )

Aligns text to the given tab-stops.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) for more details.

---

<span id="class_RichTextLabel_property_text"></span>

[String](class_string.md#class_String) **text** = `""` [🔗](class_richtextlabel.md#class_RichTextLabel_property_text)

- void **set_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_text** ( )

The label's text in BBCode format. Is not representative of manual modifications to the internal tag stack. Erases changes made by other methods when edited.

 **Note:** If [bbcode_enabled](class_richtextlabel.md#class_RichTextLabel_property_bbcode_enabled) is `true`, it is unadvised to use the `+=` operator with [text](class_richtextlabel.md#class_RichTextLabel_property_text) (e.g. `text += "some string"`) as it replaces the whole text and can cause slowdowns. It will also erase all BBCode that was added to stack using `push_*` methods. Use [append_text()](class_richtextlabel.md#class_RichTextLabel_method_append_text) for adding text instead, unless you absolutely need to close a tag that was opened in an earlier method call.

---

<span id="class_RichTextLabel_property_text_direction"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **text_direction** = `0` [🔗](class_richtextlabel.md#class_RichTextLabel_property_text_direction)

- void **set_text_direction** ( value: [TextDirection](class_control.md#enum_Control_TextDirection) )
- [TextDirection](class_control.md#enum_Control_TextDirection) **get_text_direction** ( )

Base text writing direction.

---

<span id="class_RichTextLabel_property_threaded"></span>

[bool](class_bool.md#class_bool) **threaded** = `false` [🔗](class_richtextlabel.md#class_RichTextLabel_property_threaded)

- void **set_threaded** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_threaded** ( )

If `true`, text processing is done in a background thread.

---

<span id="class_RichTextLabel_property_vertical_alignment"></span>

VerticalAlignment **vertical_alignment** = `0` [🔗](class_richtextlabel.md#class_RichTextLabel_property_vertical_alignment)

- void **set_vertical_alignment** ( value: VerticalAlignment )
- VerticalAlignment **get_vertical_alignment** ( )

Controls the text's vertical alignment. Supports top, center, bottom, and fill.

---

<span id="class_RichTextLabel_property_visible_characters"></span>

[int](class_int.md#class_int) **visible_characters** = `-1` [🔗](class_richtextlabel.md#class_RichTextLabel_property_visible_characters)

- void **set_visible_characters** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_visible_characters** ( )

The number of characters to display. If set to `-1`, all characters are displayed. This can be useful when animating the text appearing in a dialog box.

 **Note:** Setting this property updates [visible_ratio](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio) accordingly.

 **Note:** Characters are counted as Unicode codepoints. A single visible grapheme may contain multiple codepoints (e.g. certain emoji use three codepoints). A single codepoint may contain two UTF-16 characters, which are used in C# strings.

---

<span id="class_RichTextLabel_property_visible_characters_behavior"></span>

[VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) **visible_characters_behavior** = `0` [🔗](class_richtextlabel.md#class_RichTextLabel_property_visible_characters_behavior)

- void **set_visible_characters_behavior** ( value: [VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) )
- [VisibleCharactersBehavior](class_textserver.md#enum_TextServer_VisibleCharactersBehavior) **get_visible_characters_behavior** ( )

The clipping behavior when [visible_characters](class_richtextlabel.md#class_RichTextLabel_property_visible_characters) or [visible_ratio](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio) is set.

---

<span id="class_RichTextLabel_property_visible_ratio"></span>

[float](class_float.md#class_float) **visible_ratio** = `1.0` [🔗](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio)

- void **set_visible_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_visible_ratio** ( )

The fraction of characters to display, relative to the total number of characters (see [get_total_character_count()](class_richtextlabel.md#class_RichTextLabel_method_get_total_character_count)). If set to `1.0`, all characters are displayed. If set to `0.5`, only half of the characters will be displayed. This can be useful when animating the text appearing in a dialog box.

 **Note:** Setting this property updates [visible_characters](class_richtextlabel.md#class_RichTextLabel_property_visible_characters) accordingly.

---

### Method Descriptions

<span id="class_RichTextLabel_method_add_hr"></span>

void **add_hr** ( width: [int](class_int.md#class_int) = 90, height: [int](class_int.md#class_int) = 2, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), alignment: HorizontalAlignment = 1, width_in_percent: [bool](class_bool.md#class_bool) = true, height_in_percent: [bool](class_bool.md#class_bool) = false ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_add_hr)

Adds a horizontal rule that can be used to separate content.

If `width_in_percent` is set, `width` values are percentages of the control width instead of pixels.

If `height_in_percent` is set, `height` values are percentages of the control width instead of pixels.

---

<span id="class_RichTextLabel_method_add_image"></span>

void **add_image** ( image: [Texture2D](class_texture2d.md#class_Texture2D), width: [int](class_int.md#class_int) = 0, height: [int](class_int.md#class_int) = 0, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), inline_align: InlineAlignment = 5, region: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), key: [Variant](class_variant.md#class_Variant) = null, pad: [bool](class_bool.md#class_bool) = false, tooltip: [String](class_string.md#class_String) = "", width_in_percent: [bool](class_bool.md#class_bool) = false, height_in_percent: [bool](class_bool.md#class_bool) = false, alt_text: [String](class_string.md#class_String) = "" ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_add_image)

Adds an image's opening and closing tags to the tag stack, optionally providing a `width` and `height` to resize the image, a `color` to tint the image and a `region` to only use parts of the image.

If `width` or `height` is set to 0, the image size will be adjusted in order to keep the original aspect ratio.

If `width` and `height` are not set, but `region` is, the region's rect will be used.

 `key` is an optional identifier, that can be used to modify the image via [update_image()](class_richtextlabel.md#class_RichTextLabel_method_update_image).

If `pad` is set, and the image is smaller than the size specified by `width` and `height`, the image padding is added to match the size instead of upscaling.

If `width_in_percent` is set, `width` values are percentages of the control width instead of pixels.

If `height_in_percent` is set, `height` values are percentages of the control width instead of pixels.

 `alt_text` is used as the image description for assistive apps.

---

<span id="class_RichTextLabel_method_add_text"></span>

void **add_text** ( text: [String](class_string.md#class_String) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_add_text)

Adds raw non-BBCode-parsed text to the tag stack.

---

<span id="class_RichTextLabel_method_append_text"></span>

void **append_text** ( bbcode: [String](class_string.md#class_String) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_append_text)

Parses `bbcode` and adds tags to the tag stack as needed.

 **Note:** Using this method, you can't close a tag that was opened in a previous [append_text()](class_richtextlabel.md#class_RichTextLabel_method_append_text) call. This is done to improve performance, especially when updating large RichTextLabels since rebuilding the whole BBCode every time would be slower. If you absolutely need to close a tag in a future method call, append the [text](class_richtextlabel.md#class_RichTextLabel_property_text) instead of using [append_text()](class_richtextlabel.md#class_RichTextLabel_method_append_text).

---

<span id="class_RichTextLabel_method_clear"></span>

void **clear** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_clear)

Clears the tag stack, causing the label to display nothing.

 **Note:** This method does not affect [text](class_richtextlabel.md#class_RichTextLabel_property_text), and its contents will show again if the label is redrawn. However, setting [text](class_richtextlabel.md#class_RichTextLabel_property_text) to an empty [String](class_string.md#class_String) also clears the stack.

---

<span id="class_RichTextLabel_method_deselect"></span>

void **deselect** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_deselect)

Clears the current selection.

---

<span id="class_RichTextLabel_method_get_character_line"></span>

[int](class_int.md#class_int) **get_character_line** ( character: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_character_line)

Returns the line number of the character position provided. Line and character numbers are both zero-indexed.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_get_character_paragraph"></span>

[int](class_int.md#class_int) **get_character_paragraph** ( character: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_character_paragraph)

Returns the paragraph number of the character position provided. Paragraph and character numbers are both zero-indexed.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_get_content_height"></span>

[int](class_int.md#class_int) **get_content_height** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_content_height)

Returns the height of the content.

 **Note:** This method always returns the full content size, and is not affected by [visible_ratio](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio) and [visible_characters](class_richtextlabel.md#class_RichTextLabel_property_visible_characters). To get the visible content size, use [get_visible_content_rect()](class_richtextlabel.md#class_RichTextLabel_method_get_visible_content_rect).

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_get_content_width"></span>

[int](class_int.md#class_int) **get_content_width** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_content_width)

Returns the width of the content.

 **Note:** This method always returns the full content size, and is not affected by [visible_ratio](class_richtextlabel.md#class_RichTextLabel_property_visible_ratio) and [visible_characters](class_richtextlabel.md#class_RichTextLabel_property_visible_characters). To get the visible content size, use [get_visible_content_rect()](class_richtextlabel.md#class_RichTextLabel_method_get_visible_content_rect).

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_get_line_count"></span>

[int](class_int.md#class_int) **get_line_count** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_line_count)

Returns the total number of lines in the text. Wrapped text is counted as multiple lines.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_get_line_height"></span>

[int](class_int.md#class_int) **get_line_height** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_line_height)

Returns the height of the line found at the provided index.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether the document is fully loaded.

---

<span id="class_RichTextLabel_method_get_line_offset"></span>

[float](class_float.md#class_float) **get_line_offset** ( line: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_line_offset)

Returns the vertical offset of the line found at the provided index.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_get_line_range"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_line_range** ( line: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_line_range)

Returns the indexes of the first and last visible characters for the given `line`, as a [Vector2i](class_vector2i.md#class_Vector2i).

 **Note:** If [visible_characters_behavior](class_richtextlabel.md#class_RichTextLabel_property_visible_characters_behavior) is set to [TextServer.VC_CHARS_BEFORE_SHAPING](class_textserver.md#class_TextServer_constant_VC_CHARS_BEFORE_SHAPING) only visible wrapped lines are counted.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_get_line_width"></span>

[int](class_int.md#class_int) **get_line_width** ( line: [int](class_int.md#class_int) ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_line_width)

Returns the width of the line found at the provided index.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether the document is fully loaded.

---

<span id="class_RichTextLabel_method_get_menu"></span>

[PopupMenu](class_popupmenu.md#class_PopupMenu) **get_menu** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_menu)

Returns the [PopupMenu](class_popupmenu.md#class_PopupMenu) of this **RichTextLabel**. By default, this menu is displayed when right-clicking on the **RichTextLabel**.

You can add custom menu items or remove standard ones. Make sure your IDs don't conflict with the standard ones (see [MenuItems](class_richtextlabel.md#enum_RichTextLabel_MenuItems)). For example:

.. tabs::

```
```

    func _ready():
        var menu = get_menu()
        # Remove "Select All" item.
        menu.remove_item(MENU_SELECT_ALL)
        # Add custom items.
        menu.add_separator()
        menu.add_item("Duplicate Text", MENU_MAX + 1)
        # Connect callback.
        menu.id_pressed.connect(_on_item_pressed)

    func _on_item_pressed(id):
        if id == MENU_MAX + 1:
            add_text("\n" + get_parsed_text())

```
```

    public override void _Ready()
    {
        var menu = GetMenu();
        // Remove "Select All" item.
        menu.RemoveItem(RichTextLabel.MenuItems.SelectAll);
        // Add custom items.
        menu.AddSeparator();
        menu.AddItem("Duplicate Text", RichTextLabel.MenuItems.Max + 1);
        // Add event handler.
        menu.IdPressed += OnItemPressed;
    }

    public void OnItemPressed(int id)
    {
        if (id == TextEdit.MenuItems.Max + 1)
        {
            AddText("\n" + GetParsedText());
        }
    }

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible](class_window.md#class_Window_property_visible) property.

---

<span id="class_RichTextLabel_method_get_paragraph_count"></span>

[int](class_int.md#class_int) **get_paragraph_count** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_paragraph_count)

Returns the total number of paragraphs (newlines or `p` tags in the tag stack's text tags). Considers wrapped text as one paragraph.

---

<span id="class_RichTextLabel_method_get_paragraph_offset"></span>

[float](class_float.md#class_float) **get_paragraph_offset** ( paragraph: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_paragraph_offset)

Returns the vertical offset of the paragraph found at the provided index.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_get_parsed_text"></span>

[String](class_string.md#class_String) **get_parsed_text** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_parsed_text)

Returns the text without BBCode mark-up.

---

<span id="class_RichTextLabel_method_get_selected_text"></span>

[String](class_string.md#class_String) **get_selected_text** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_selected_text)

Returns the current selection text. Does not include BBCodes.

---

<span id="class_RichTextLabel_method_get_selection_from"></span>

[int](class_int.md#class_int) **get_selection_from** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_selection_from)

Returns the current selection first character index if a selection is active, `-1` otherwise. Does not include BBCodes.

---

<span id="class_RichTextLabel_method_get_selection_line_offset"></span>

[float](class_float.md#class_float) **get_selection_line_offset** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_selection_line_offset)

Returns the current selection vertical line offset if a selection is active, `-1.0` otherwise.

---

<span id="class_RichTextLabel_method_get_selection_to"></span>

[int](class_int.md#class_int) **get_selection_to** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_selection_to)

Returns the current selection last character index if a selection is active, `-1` otherwise. Does not include BBCodes.

---

<span id="class_RichTextLabel_method_get_total_character_count"></span>

[int](class_int.md#class_int) **get_total_character_count** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_total_character_count)

Returns the total number of characters from text tags. Does not include BBCodes.

---

<span id="class_RichTextLabel_method_get_v_scroll_bar"></span>

[VScrollBar](class_vscrollbar.md#class_VScrollBar) **get_v_scroll_bar** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_v_scroll_bar)

Returns the vertical scrollbar.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.

---

<span id="class_RichTextLabel_method_get_visible_content_rect"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **get_visible_content_rect** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_visible_content_rect)

Returns the bounding rectangle of the visible content.

 **Note:** This method returns a correct value only after the label has been drawn.

.. tabs::

```
```

    extends RichTextLabel

    @export var background_panel: Panel

    func _ready():
        await draw
        background_panel.position = get_visible_content_rect().position
        background_panel.size = get_visible_content_rect().size

```
```

    public partial class TestLabel : RichTextLabel
    {
        [Export]
        public Panel BackgroundPanel { get; set; }

        public override async void _Ready()
        {
            await ToSignal(this, Control.SignalName.Draw);
            BackgroundGPanel.Position = GetVisibleContentRect().Position;
            BackgroundPanel.Size = GetVisibleContentRect().Size;
        }
    }

---

<span id="class_RichTextLabel_method_get_visible_line_count"></span>

[int](class_int.md#class_int) **get_visible_line_count** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_visible_line_count)

Returns the number of visible lines.

 **Note:** This method returns a correct value only after the label has been drawn.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_get_visible_paragraph_count"></span>

[int](class_int.md#class_int) **get_visible_paragraph_count** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_get_visible_paragraph_count)

Returns the number of visible paragraphs. A paragraph is considered visible if at least one of its lines is visible.

 **Note:** This method returns a correct value only after the label has been drawn.

 **Note:** If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, this method returns a value for the loaded part of the document. Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) or [finished](class_richtextlabel.md#class_RichTextLabel_signal_finished) to determine whether document is fully loaded.

---

<span id="class_RichTextLabel_method_install_effect"></span>

void **install_effect** ( effect: [Variant](class_variant.md#class_Variant) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_install_effect)

Installs a custom effect. This can also be done in the Inspector through the [custom_effects](class_richtextlabel.md#class_RichTextLabel_property_custom_effects) property. `effect` should be a valid [RichTextEffect](class_richtexteffect.md#class_RichTextEffect).

 **Example:** With the following script extending from [RichTextEffect](class_richtexteffect.md#class_RichTextEffect):

::

    # effect.gd
    class_name MyCustomEffect
    extends RichTextEffect

    var bbcode = "my_custom_effect"

    # ...

The above effect can be installed in **RichTextLabel** from a script:

::

    # rich_text_label.gd
    extends RichTextLabel

    func _ready():
        install_effect(MyCustomEffect.new())

        # Alternatively, if not using `class_name` in the script that extends RichTextEffect:
        install_effect(preload("res://effect.gd").new())

---

<span id="class_RichTextLabel_method_invalidate_paragraph"></span>

[bool](class_bool.md#class_bool) **invalidate_paragraph** ( paragraph: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_invalidate_paragraph)

Invalidates `paragraph` and all subsequent paragraphs cache.

---

<span id="class_RichTextLabel_method_is_finished"></span>

[bool](class_bool.md#class_bool) **is_finished** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_is_finished)

If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, returns `true` if the background thread has finished text processing, otherwise always return `true`.

---

<span id="class_RichTextLabel_method_is_menu_visible"></span>

[bool](class_bool.md#class_bool) **is_menu_visible** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_is_menu_visible)

Returns whether the menu is visible. Use this instead of `get_menu().visible` to improve performance (so the creation of the menu is avoided).

---

<span id="class_RichTextLabel_method_is_ready"></span>

[bool](class_bool.md#class_bool) **is_ready** ( ) *const* [🔗](class_richtextlabel.md#class_RichTextLabel_method_is_ready)

**Deprecated:** Use [is_finished()](class_richtextlabel.md#class_RichTextLabel_method_is_finished) instead.

If [threaded](class_richtextlabel.md#class_RichTextLabel_property_threaded) is enabled, returns `true` if the background thread has finished text processing, otherwise always return `true`.

---

<span id="class_RichTextLabel_method_menu_option"></span>

void **menu_option** ( option: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_menu_option)

Executes a given action as defined in the [MenuItems](class_richtextlabel.md#enum_RichTextLabel_MenuItems) enum.

---

<span id="class_RichTextLabel_method_newline"></span>

void **newline** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_newline)

Adds a newline tag to the tag stack.

---

<span id="class_RichTextLabel_method_parse_bbcode"></span>

void **parse_bbcode** ( bbcode: [String](class_string.md#class_String) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_parse_bbcode)

The assignment version of [append_text()](class_richtextlabel.md#class_RichTextLabel_method_append_text). Clears the tag stack and inserts the new content.

---

<span id="class_RichTextLabel_method_parse_expressions_for_values"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **parse_expressions_for_values** ( expressions: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_parse_expressions_for_values)

Parses BBCode parameter `expressions` into a dictionary.

---

<span id="class_RichTextLabel_method_pop"></span>

void **pop** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_pop)

Terminates the current tag. Use after `push_*` methods to close BBCodes manually. Does not need to follow `add_*` methods.

---

<span id="class_RichTextLabel_method_pop_all"></span>

void **pop_all** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_pop_all)

Terminates all tags opened by `push_*` methods.

---

<span id="class_RichTextLabel_method_pop_context"></span>

void **pop_context** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_pop_context)

Terminates tags opened after the last [push_context()](class_richtextlabel.md#class_RichTextLabel_method_push_context) call (including context marker), or all tags if there's no context marker on the stack.

---

<span id="class_RichTextLabel_method_push_bgcolor"></span>

void **push_bgcolor** ( bgcolor: [Color](class_color.md#class_Color) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_bgcolor)

Adds a `[bgcolor]` tag to the tag stack.

 **Note:** The background color has padding applied by default, which is controlled using [text_highlight_h_padding](class_richtextlabel.md#class_RichTextLabel_theme_constant_text_highlight_h_padding) and [text_highlight_v_padding](class_richtextlabel.md#class_RichTextLabel_theme_constant_text_highlight_v_padding). This can lead to overlapping highlights if background colors are placed on neighboring lines/columns, so consider setting those theme items to `0` if you want to avoid this.

---

<span id="class_RichTextLabel_method_push_bold"></span>

void **push_bold** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_bold)

Adds a `[font]` tag with a bold font to the tag stack. This is the same as adding a `[b]` tag if not currently in a `[i]` tag.

---

<span id="class_RichTextLabel_method_push_bold_italics"></span>

void **push_bold_italics** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_bold_italics)

Adds a `[font]` tag with a bold italics font to the tag stack.

---

<span id="class_RichTextLabel_method_push_cell"></span>

void **push_cell** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_cell)

Adds a `[cell]` tag to the tag stack. Must be inside a `[table]` tag. See [push_table()](class_richtextlabel.md#class_RichTextLabel_method_push_table) for details. Use [set_table_column_expand()](class_richtextlabel.md#class_RichTextLabel_method_set_table_column_expand) to set column expansion ratio, [set_cell_border_color()](class_richtextlabel.md#class_RichTextLabel_method_set_cell_border_color) to set cell border, [set_cell_row_background_color()](class_richtextlabel.md#class_RichTextLabel_method_set_cell_row_background_color) to set cell background, [set_cell_size_override()](class_richtextlabel.md#class_RichTextLabel_method_set_cell_size_override) to override cell size, and [set_cell_padding()](class_richtextlabel.md#class_RichTextLabel_method_set_cell_padding) to set padding.

---

<span id="class_RichTextLabel_method_push_color"></span>

void **push_color** ( color: [Color](class_color.md#class_Color) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_color)

Adds a `[color]` tag to the tag stack.

---

<span id="class_RichTextLabel_method_push_context"></span>

void **push_context** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_context)

Adds a context marker to the tag stack. See [pop_context()](class_richtextlabel.md#class_RichTextLabel_method_pop_context).

---

<span id="class_RichTextLabel_method_push_customfx"></span>

void **push_customfx** ( effect: [RichTextEffect](class_richtexteffect.md#class_RichTextEffect), env: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_customfx)

Adds a custom effect tag to the tag stack. The effect does not need to be in [custom_effects](class_richtextlabel.md#class_RichTextLabel_property_custom_effects). The environment is directly passed to the effect.

---

<span id="class_RichTextLabel_method_push_dropcap"></span>

void **push_dropcap** ( string: [String](class_string.md#class_String), font: [Font](class_font.md#class_Font), size: [int](class_int.md#class_int), dropcap_margins: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), outline_size: [int](class_int.md#class_int) = 0, outline_color: [Color](class_color.md#class_Color) = Color(0, 0, 0, 0) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_dropcap)

Adds a `[dropcap]` tag to the tag stack. Drop cap (dropped capital) is a decorative element at the beginning of a paragraph that is larger than the rest of the text.

---

<span id="class_RichTextLabel_method_push_fgcolor"></span>

void **push_fgcolor** ( fgcolor: [Color](class_color.md#class_Color) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_fgcolor)

Adds a `[fgcolor]` tag to the tag stack.

 **Note:** The foreground color has padding applied by default, which is controlled using [text_highlight_h_padding](class_richtextlabel.md#class_RichTextLabel_theme_constant_text_highlight_h_padding) and [text_highlight_v_padding](class_richtextlabel.md#class_RichTextLabel_theme_constant_text_highlight_v_padding). This can lead to overlapping highlights if foreground colors are placed on neighboring lines/columns, so consider setting those theme items to `0` if you want to avoid this.

---

<span id="class_RichTextLabel_method_push_font"></span>

void **push_font** ( font: [Font](class_font.md#class_Font), font_size: [int](class_int.md#class_int) = 0 ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_font)

Adds a `[font]` tag to the tag stack. Overrides default fonts for its duration.

Passing `0` to `font_size` will use the existing default font size.

---

<span id="class_RichTextLabel_method_push_font_size"></span>

void **push_font_size** ( font_size: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_font_size)

Adds a `[font_size]` tag to the tag stack. Overrides default font size for its duration.

---

<span id="class_RichTextLabel_method_push_hint"></span>

void **push_hint** ( description: [String](class_string.md#class_String) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_hint)

Adds a `[hint]` tag to the tag stack. Same as BBCode `[hint=something]{text}[/hint]`.

---

<span id="class_RichTextLabel_method_push_indent"></span>

void **push_indent** ( level: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_indent)

Adds an `[indent]` tag to the tag stack. Multiplies `level` by current [tab_size](class_richtextlabel.md#class_RichTextLabel_property_tab_size) to determine new margin length.

---

<span id="class_RichTextLabel_method_push_italics"></span>

void **push_italics** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_italics)

Adds a `[font]` tag with an italics font to the tag stack. This is the same as adding an `[i]` tag if not currently in a `[b]` tag.

---

<span id="class_RichTextLabel_method_push_language"></span>

void **push_language** ( language: [String](class_string.md#class_String) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_language)

Adds language code used for text shaping algorithm and Open-Type font features.

---

<span id="class_RichTextLabel_method_push_list"></span>

void **push_list** ( level: [int](class_int.md#class_int), type: [ListType](class_richtextlabel.md#enum_RichTextLabel_ListType), capitalize: [bool](class_bool.md#class_bool), bullet: [String](class_string.md#class_String) = "•" ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_list)

Adds `[ol]` or `[ul]` tag to the tag stack. Multiplies `level` by current [tab_size](class_richtextlabel.md#class_RichTextLabel_property_tab_size) to determine new margin length.

---

<span id="class_RichTextLabel_method_push_meta"></span>

void **push_meta** ( data: [Variant](class_variant.md#class_Variant), underline_mode: [MetaUnderline](class_richtextlabel.md#enum_RichTextLabel_MetaUnderline) = 1, tooltip: [String](class_string.md#class_String) = "" ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_meta)

Adds a meta tag to the tag stack. Similar to the BBCode `[url=something]{text}[/url]`, but supports non-[String](class_string.md#class_String) metadata types.

If [meta_underlined](class_richtextlabel.md#class_RichTextLabel_property_meta_underlined) is `true`, meta tags display an underline. This behavior can be customized with `underline_mode`.

 **Note:** Meta tags do nothing by default when clicked. To assign behavior when clicked, connect [meta_clicked](class_richtextlabel.md#class_RichTextLabel_signal_meta_clicked) to a function that is called when the meta tag is clicked.

---

<span id="class_RichTextLabel_method_push_mono"></span>

void **push_mono** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_mono)

Adds a `[font]` tag with a monospace font to the tag stack.

---

<span id="class_RichTextLabel_method_push_normal"></span>

void **push_normal** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_normal)

Adds a `[font]` tag with a normal font to the tag stack.

---

<span id="class_RichTextLabel_method_push_outline_color"></span>

void **push_outline_color** ( color: [Color](class_color.md#class_Color) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_outline_color)

Adds a `[outline_color]` tag to the tag stack. Adds text outline for its duration.

---

<span id="class_RichTextLabel_method_push_outline_size"></span>

void **push_outline_size** ( outline_size: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_outline_size)

Adds a `[outline_size]` tag to the tag stack. Overrides default text outline size for its duration.

---

<span id="class_RichTextLabel_method_push_paragraph"></span>

void **push_paragraph** ( alignment: HorizontalAlignment, base_direction: [TextDirection](class_control.md#enum_Control_TextDirection) = 0, language: [String](class_string.md#class_String) = "", st_parser: [StructuredTextParser](class_textserver.md#enum_TextServer_StructuredTextParser) = 0, justification_flags: *BitField*\[[JustificationFlag](class_textserver.md#enum_TextServer_JustificationFlag)\] = 163, tab_stops: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) = PackedFloat32Array() ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_paragraph)

Adds a `[p]` tag to the tag stack.

---

<span id="class_RichTextLabel_method_push_strikethrough"></span>

void **push_strikethrough** ( color: [Color](class_color.md#class_Color) = Color(0, 0, 0, 0) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_strikethrough)

Adds a `[s]` tag to the tag stack. If `color`'s alpha value is `0.0`, the current font's color with its alpha multiplied by [strikethrough_alpha](class_richtextlabel.md#class_RichTextLabel_theme_constant_strikethrough_alpha) is used.

---

<span id="class_RichTextLabel_method_push_table"></span>

void **push_table** ( columns: [int](class_int.md#class_int), inline_align: InlineAlignment = 0, align_to_row: [int](class_int.md#class_int) = -1, name: [String](class_string.md#class_String) = "" ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_table)

Adds a `[table=columns,inline_align]` tag to the tag stack. Use [set_table_column_expand()](class_richtextlabel.md#class_RichTextLabel_method_set_table_column_expand) to set column expansion ratio. Use [push_cell()](class_richtextlabel.md#class_RichTextLabel_method_push_cell) to add cells. `name` is used as the table name for assistive apps.

---

<span id="class_RichTextLabel_method_push_underline"></span>

void **push_underline** ( color: [Color](class_color.md#class_Color) = Color(0, 0, 0, 0) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_push_underline)

Adds a `[u]` tag to the tag stack. If `color`'s alpha value is `0.0`, the current font's color with its alpha multiplied by [underline_alpha](class_richtextlabel.md#class_RichTextLabel_theme_constant_underline_alpha) is used.

---

<span id="class_RichTextLabel_method_reload_effects"></span>

void **reload_effects** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_reload_effects)

Reloads custom effects. Useful when [custom_effects](class_richtextlabel.md#class_RichTextLabel_property_custom_effects) is modified manually.

---

<span id="class_RichTextLabel_method_remove_paragraph"></span>

[bool](class_bool.md#class_bool) **remove_paragraph** ( paragraph: [int](class_int.md#class_int), no_invalidate: [bool](class_bool.md#class_bool) = false ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_remove_paragraph)

Removes a paragraph of content from the label. Returns `true` if the paragraph exists.

The `paragraph` argument is the index of the paragraph to remove, it can take values in the interval `[0, get_paragraph_count() - 1]`.

If `no_invalidate` is set to `true`, cache for the subsequent paragraphs is not invalidated. Use it for faster updates if deleted paragraph is fully self-contained (have no unclosed tags), or this call is part of the complex edit operation and [invalidate_paragraph()](class_richtextlabel.md#class_RichTextLabel_method_invalidate_paragraph) will be called at the end of operation.

---

<span id="class_RichTextLabel_method_scroll_to_line"></span>

void **scroll_to_line** ( line: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_scroll_to_line)

Scrolls the window's top line to match `line`.

---

<span id="class_RichTextLabel_method_scroll_to_paragraph"></span>

void **scroll_to_paragraph** ( paragraph: [int](class_int.md#class_int) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_scroll_to_paragraph)

Scrolls the window's top line to match first line of the `paragraph`.

---

<span id="class_RichTextLabel_method_scroll_to_selection"></span>

void **scroll_to_selection** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_scroll_to_selection)

Scrolls to the beginning of the current selection.

---

<span id="class_RichTextLabel_method_select_all"></span>

void **select_all** ( ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_select_all)

Select all the text.

If [selection_enabled](class_richtextlabel.md#class_RichTextLabel_property_selection_enabled) is `false`, no selection will occur.

---

<span id="class_RichTextLabel_method_set_cell_border_color"></span>

void **set_cell_border_color** ( color: [Color](class_color.md#class_Color) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_set_cell_border_color)

Sets color of a table cell border.

---

<span id="class_RichTextLabel_method_set_cell_padding"></span>

void **set_cell_padding** ( padding: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_set_cell_padding)

Sets inner padding of a table cell.

---

<span id="class_RichTextLabel_method_set_cell_row_background_color"></span>

void **set_cell_row_background_color** ( odd_row_bg: [Color](class_color.md#class_Color), even_row_bg: [Color](class_color.md#class_Color) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_set_cell_row_background_color)

Sets color of a table cell. Separate colors for alternating rows can be specified.

---

<span id="class_RichTextLabel_method_set_cell_size_override"></span>

void **set_cell_size_override** ( min_size: [Vector2](class_vector2.md#class_Vector2), max_size: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_set_cell_size_override)

Sets minimum and maximum size overrides for a table cell.

---

<span id="class_RichTextLabel_method_set_table_column_expand"></span>

void **set_table_column_expand** ( column: [int](class_int.md#class_int), expand: [bool](class_bool.md#class_bool), ratio: [int](class_int.md#class_int) = 1, shrink: [bool](class_bool.md#class_bool) = true ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_set_table_column_expand)

Edits the selected column's expansion options. If `expand` is `true`, the column expands in proportion to its expansion ratio versus the other columns' ratios.

For example, 2 columns with ratios 3 and 4 plus 70 pixels in available width would expand 30 and 40 pixels, respectively.

If `expand` is `false`, the column will not contribute to the total ratio.

---

<span id="class_RichTextLabel_method_set_table_column_name"></span>

void **set_table_column_name** ( column: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_set_table_column_name)

Sets table column name for assistive apps.

---

<span id="class_RichTextLabel_method_update_image"></span>

void **update_image** ( key: [Variant](class_variant.md#class_Variant), mask: *BitField*\[[ImageUpdateMask](class_richtextlabel.md#enum_RichTextLabel_ImageUpdateMask)\], image: [Texture2D](class_texture2d.md#class_Texture2D), width: [int](class_int.md#class_int) = 0, height: [int](class_int.md#class_int) = 0, color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), inline_align: InlineAlignment = 5, region: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), pad: [bool](class_bool.md#class_bool) = false, tooltip: [String](class_string.md#class_String) = "", width_in_percent: [bool](class_bool.md#class_bool) = false, height_in_percent: [bool](class_bool.md#class_bool) = false ) [🔗](class_richtextlabel.md#class_RichTextLabel_method_update_image)

Updates the existing images with the key `key`. Only properties specified by `mask` bits are updated. See [add_image()](class_richtextlabel.md#class_RichTextLabel_method_add_image).

---

### Theme Property Descriptions

<span id="class_RichTextLabel_theme_color_default_color"></span>

[Color](class_color.md#class_Color) **default_color** = `Color(1, 1, 1, 1)` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_color_default_color)

The default text color.

---

<span id="class_RichTextLabel_theme_color_font_outline_color"></span>

[Color](class_color.md#class_Color) **font_outline_color** = `Color(0, 0, 0, 1)` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_color_font_outline_color)

The default tint of text outline.

---

<span id="class_RichTextLabel_theme_color_font_selected_color"></span>

[Color](class_color.md#class_Color) **font_selected_color** = `Color(0, 0, 0, 0)` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_color_font_selected_color)

The color of selected text, used when [selection_enabled](class_richtextlabel.md#class_RichTextLabel_property_selection_enabled) is `true`. If equal to `Color(0, 0, 0, 0)`, it will be ignored.

---

<span id="class_RichTextLabel_theme_color_font_shadow_color"></span>

[Color](class_color.md#class_Color) **font_shadow_color** = `Color(0, 0, 0, 0)` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_color_font_shadow_color)

The color of the font's shadow.

---

<span id="class_RichTextLabel_theme_color_selection_color"></span>

[Color](class_color.md#class_Color) **selection_color** = `Color(0.1, 0.1, 1, 0.8)` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_color_selection_color)

The color of the selection box.

---

<span id="class_RichTextLabel_theme_color_table_border"></span>

[Color](class_color.md#class_Color) **table_border** = `Color(0, 0, 0, 0)` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_color_table_border)

The default cell border color.

---

<span id="class_RichTextLabel_theme_color_table_even_row_bg"></span>

[Color](class_color.md#class_Color) **table_even_row_bg** = `Color(0, 0, 0, 0)` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_color_table_even_row_bg)

The default background color for even rows.

---

<span id="class_RichTextLabel_theme_color_table_odd_row_bg"></span>

[Color](class_color.md#class_Color) **table_odd_row_bg** = `Color(0, 0, 0, 0)` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_color_table_odd_row_bg)

The default background color for odd rows.

---

<span id="class_RichTextLabel_theme_constant_line_separation"></span>

[int](class_int.md#class_int) **line_separation** = `0` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_line_separation)

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

---

<span id="class_RichTextLabel_theme_constant_outline_size"></span>

[int](class_int.md#class_int) **outline_size** = `0` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_outline_size)

The size of the text outline.

 **Note:** If using a font with [FontFile.multichannel_signed_distance_field](class_fontfile.md#class_FontFile_property_multichannel_signed_distance_field) enabled, its [FontFile.msdf_pixel_range](class_fontfile.md#class_FontFile_property_msdf_pixel_range) must be set to at least *twice* the value of [outline_size](class_richtextlabel.md#class_RichTextLabel_theme_constant_outline_size) for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

---

<span id="class_RichTextLabel_theme_constant_paragraph_separation"></span>

[int](class_int.md#class_int) **paragraph_separation** = `0` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_paragraph_separation)

Additional vertical spacing between paragraphs (in pixels). Spacing is added after the last line. This value can be negative.

---

<span id="class_RichTextLabel_theme_constant_shadow_offset_x"></span>

[int](class_int.md#class_int) **shadow_offset_x** = `1` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_shadow_offset_x)

The horizontal offset of the font's shadow.

---

<span id="class_RichTextLabel_theme_constant_shadow_offset_y"></span>

[int](class_int.md#class_int) **shadow_offset_y** = `1` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_shadow_offset_y)

The vertical offset of the font's shadow.

---

<span id="class_RichTextLabel_theme_constant_shadow_outline_size"></span>

[int](class_int.md#class_int) **shadow_outline_size** = `1` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_shadow_outline_size)

The size of the shadow outline.

---

<span id="class_RichTextLabel_theme_constant_strikethrough_alpha"></span>

[int](class_int.md#class_int) **strikethrough_alpha** = `50` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_strikethrough_alpha)

The default strikethrough color transparency (percent). For strikethroughs with a custom color, this theme item is only used if the custom color's alpha is `0.0` (fully transparent).

---

<span id="class_RichTextLabel_theme_constant_table_h_separation"></span>

[int](class_int.md#class_int) **table_h_separation** = `3` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_table_h_separation)

The horizontal separation of elements in a table.

---

<span id="class_RichTextLabel_theme_constant_table_v_separation"></span>

[int](class_int.md#class_int) **table_v_separation** = `3` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_table_v_separation)

The vertical separation of elements in a table.

---

<span id="class_RichTextLabel_theme_constant_text_highlight_h_padding"></span>

[int](class_int.md#class_int) **text_highlight_h_padding** = `3` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_text_highlight_h_padding)

The horizontal padding around boxes drawn by the `[fgcolor]` and `[bgcolor]` tags. This does not affect the appearance of text selection. To avoid any risk of neighboring highlights overlapping each other, set this to `0` to disable padding.

---

<span id="class_RichTextLabel_theme_constant_text_highlight_v_padding"></span>

[int](class_int.md#class_int) **text_highlight_v_padding** = `3` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_text_highlight_v_padding)

The vertical padding around boxes drawn by the `[fgcolor]` and `[bgcolor]` tags. This does not affect the appearance of text selection. To avoid any risk of neighboring highlights overlapping each other, set this to `0` to disable padding.

---

<span id="class_RichTextLabel_theme_constant_underline_alpha"></span>

[int](class_int.md#class_int) **underline_alpha** = `50` [🔗](class_richtextlabel.md#class_RichTextLabel_theme_constant_underline_alpha)

The default underline color transparency (percent). For underlines with a custom color, this theme item is only used if the custom color's alpha is `0.0` (fully transparent).

---

<span id="class_RichTextLabel_theme_font_bold_font"></span>

[Font](class_font.md#class_Font) **bold_font** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_bold_font)

The font used for bold text.

---

<span id="class_RichTextLabel_theme_font_bold_italics_font"></span>

[Font](class_font.md#class_Font) **bold_italics_font** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_bold_italics_font)

The font used for bold italics text.

---

<span id="class_RichTextLabel_theme_font_italics_font"></span>

[Font](class_font.md#class_Font) **italics_font** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_italics_font)

The font used for italics text.

---

<span id="class_RichTextLabel_theme_font_mono_font"></span>

[Font](class_font.md#class_Font) **mono_font** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_mono_font)

The font used for monospace text.

---

<span id="class_RichTextLabel_theme_font_normal_font"></span>

[Font](class_font.md#class_Font) **normal_font** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_normal_font)

The default text font.

---

<span id="class_RichTextLabel_theme_font_size_bold_font_size"></span>

[int](class_int.md#class_int) **bold_font_size** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_size_bold_font_size)

The font size used for bold text.

---

<span id="class_RichTextLabel_theme_font_size_bold_italics_font_size"></span>

[int](class_int.md#class_int) **bold_italics_font_size** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_size_bold_italics_font_size)

The font size used for bold italics text.

---

<span id="class_RichTextLabel_theme_font_size_italics_font_size"></span>

[int](class_int.md#class_int) **italics_font_size** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_size_italics_font_size)

The font size used for italics text.

---

<span id="class_RichTextLabel_theme_font_size_mono_font_size"></span>

[int](class_int.md#class_int) **mono_font_size** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_size_mono_font_size)

The font size used for monospace text.

---

<span id="class_RichTextLabel_theme_font_size_normal_font_size"></span>

[int](class_int.md#class_int) **normal_font_size** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_font_size_normal_font_size)

The default text font size.

---

<span id="class_RichTextLabel_theme_icon_horizontal_rule"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **horizontal_rule** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_icon_horizontal_rule)

The horizontal rule texture.

---

<span id="class_RichTextLabel_theme_style_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **focus** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_style_focus)

The background used when the **RichTextLabel** is focused. The [focus](class_richtextlabel.md#class_RichTextLabel_theme_style_focus) [StyleBox](class_stylebox.md#class_StyleBox) is displayed *over* the base [StyleBox](class_stylebox.md#class_StyleBox), so a partially transparent [StyleBox](class_stylebox.md#class_StyleBox) should be used to ensure the base [StyleBox](class_stylebox.md#class_StyleBox) remains visible. A [StyleBox](class_stylebox.md#class_StyleBox) that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a [StyleBoxEmpty](class_styleboxempty.md#class_StyleBoxEmpty) resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

---

<span id="class_RichTextLabel_theme_style_normal"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **normal** [🔗](class_richtextlabel.md#class_RichTextLabel_theme_style_normal)

The normal background for the **RichTextLabel**.
