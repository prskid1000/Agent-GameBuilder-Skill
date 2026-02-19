<span id="class_DisplayServer"></span>

## DisplayServer

**Inherits:** [Object](class_object.md#class_Object)

A server interface for low-level window management.

### Description

**DisplayServer** handles everything related to window management. It is separated from [OS](class_os.md#class_OS) as a single operating system may support multiple display servers.

 **Headless mode:** Starting the engine with the `--headless` [command line argument](../tutorials/editor/command_line_tutorial.md) disables all rendering and window management functions. Most functions from **DisplayServer** will return dummy values in this case.

### Methods


| [RID](class_rid.md#class_RID) | [accessibility_create_element](class_displayserver.md#class_DisplayServer_method_accessibility_create_element) ( window_id: [int](class_int.md#class_int), role: [AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) ) |
| --- | --- |
| [RID](class_rid.md#class_RID) | [accessibility_create_sub_element](class_displayserver.md#class_DisplayServer_method_accessibility_create_sub_element) ( parent_rid: [RID](class_rid.md#class_RID), role: [AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole), insert_pos: [int](class_int.md#class_int) = -1 ) |
| [RID](class_rid.md#class_RID) | [accessibility_create_sub_text_edit_elements](class_displayserver.md#class_DisplayServer_method_accessibility_create_sub_text_edit_elements) ( parent_rid: [RID](class_rid.md#class_RID), shaped_text: [RID](class_rid.md#class_RID), min_height: [float](class_float.md#class_float), insert_pos: [int](class_int.md#class_int) = -1, is_last_line: [bool](class_bool.md#class_bool) = false ) |
| [Variant](class_variant.md#class_Variant) | [accessibility_element_get_meta](class_displayserver.md#class_DisplayServer_method_accessibility_element_get_meta) ( id: [RID](class_rid.md#class_RID) ) const |
| void | [accessibility_element_set_meta](class_displayserver.md#class_DisplayServer_method_accessibility_element_set_meta) ( id: [RID](class_rid.md#class_RID), meta: [Variant](class_variant.md#class_Variant) ) |
| void | [accessibility_free_element](class_displayserver.md#class_DisplayServer_method_accessibility_free_element) ( id: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [accessibility_get_window_root](class_displayserver.md#class_DisplayServer_method_accessibility_get_window_root) ( window_id: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [accessibility_has_element](class_displayserver.md#class_DisplayServer_method_accessibility_has_element) ( id: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [accessibility_screen_reader_active](class_displayserver.md#class_DisplayServer_method_accessibility_screen_reader_active) ( ) const |
| void | [accessibility_set_window_focused](class_displayserver.md#class_DisplayServer_method_accessibility_set_window_focused) ( window_id: [int](class_int.md#class_int), focused: [bool](class_bool.md#class_bool) ) |
| void | [accessibility_set_window_rect](class_displayserver.md#class_DisplayServer_method_accessibility_set_window_rect) ( window_id: [int](class_int.md#class_int), rect_out: [Rect2](class_rect2.md#class_Rect2), rect_in: [Rect2](class_rect2.md#class_Rect2) ) |
| [int](class_int.md#class_int) | [accessibility_should_increase_contrast](class_displayserver.md#class_DisplayServer_method_accessibility_should_increase_contrast) ( ) const |
| [int](class_int.md#class_int) | [accessibility_should_reduce_animation](class_displayserver.md#class_DisplayServer_method_accessibility_should_reduce_animation) ( ) const |
| [int](class_int.md#class_int) | [accessibility_should_reduce_transparency](class_displayserver.md#class_DisplayServer_method_accessibility_should_reduce_transparency) ( ) const |
| void | [accessibility_update_add_action](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_action) ( id: [RID](class_rid.md#class_RID), action: [AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction), callable: [Callable](class_callable.md#class_Callable) ) |
| void | [accessibility_update_add_child](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_child) ( id: [RID](class_rid.md#class_RID), child_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_add_custom_action](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_custom_action) ( id: [RID](class_rid.md#class_RID), action_id: [int](class_int.md#class_int), action_description: [String](class_string.md#class_String) ) |
| void | [accessibility_update_add_related_controls](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_controls) ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_add_related_described_by](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_described_by) ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_add_related_details](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_details) ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_add_related_flow_to](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_flow_to) ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_add_related_labeled_by](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_labeled_by) ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_add_related_radio_group](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_radio_group) ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_set_active_descendant](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_active_descendant) ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_set_background_color](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_background_color) ( id: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [accessibility_update_set_bounds](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_bounds) ( id: [RID](class_rid.md#class_RID), p_rect: [Rect2](class_rect2.md#class_Rect2) ) |
| void | [accessibility_update_set_checked](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_checked) ( id: [RID](class_rid.md#class_RID), checekd: [bool](class_bool.md#class_bool) ) |
| void | [accessibility_update_set_classname](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_classname) ( id: [RID](class_rid.md#class_RID), classname: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_color_value](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_color_value) ( id: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [accessibility_update_set_description](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_description) ( id: [RID](class_rid.md#class_RID), description: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_error_message](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_error_message) ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_set_extra_info](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_extra_info) ( id: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_flag](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_flag) ( id: [RID](class_rid.md#class_RID), flag: [AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags), value: [bool](class_bool.md#class_bool) ) |
| void | [accessibility_update_set_focus](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_focus) ( id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_set_foreground_color](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_foreground_color) ( id: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [accessibility_update_set_in_page_link_target](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_in_page_link_target) ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_set_language](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_language) ( id: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_list_item_count](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_count) ( id: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_list_item_expanded](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_expanded) ( id: [RID](class_rid.md#class_RID), expanded: [bool](class_bool.md#class_bool) ) |
| void | [accessibility_update_set_list_item_index](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_index) ( id: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_list_item_level](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_level) ( id: [RID](class_rid.md#class_RID), level: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_list_item_selected](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_selected) ( id: [RID](class_rid.md#class_RID), selected: [bool](class_bool.md#class_bool) ) |
| void | [accessibility_update_set_list_orientation](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_orientation) ( id: [RID](class_rid.md#class_RID), vertical: [bool](class_bool.md#class_bool) ) |
| void | [accessibility_update_set_live](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_live) ( id: [RID](class_rid.md#class_RID), live: [AccessibilityLiveMode](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode) ) |
| void | [accessibility_update_set_member_of](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_member_of) ( id: [RID](class_rid.md#class_RID), group_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_set_name](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_name) ( id: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_next_on_line](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_next_on_line) ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_set_num_jump](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_num_jump) ( id: [RID](class_rid.md#class_RID), jump: [float](class_float.md#class_float) ) |
| void | [accessibility_update_set_num_range](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_num_range) ( id: [RID](class_rid.md#class_RID), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) |
| void | [accessibility_update_set_num_step](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_num_step) ( id: [RID](class_rid.md#class_RID), step: [float](class_float.md#class_float) ) |
| void | [accessibility_update_set_num_value](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_num_value) ( id: [RID](class_rid.md#class_RID), position: [float](class_float.md#class_float) ) |
| void | [accessibility_update_set_placeholder](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_placeholder) ( id: [RID](class_rid.md#class_RID), placeholder: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_popup_type](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_popup_type) ( id: [RID](class_rid.md#class_RID), popup: [AccessibilityPopupType](class_displayserver.md#enum_DisplayServer_AccessibilityPopupType) ) |
| void | [accessibility_update_set_previous_on_line](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_previous_on_line) ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) |
| void | [accessibility_update_set_role](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_role) ( id: [RID](class_rid.md#class_RID), role: [AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) ) |
| void | [accessibility_update_set_role_description](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_role_description) ( id: [RID](class_rid.md#class_RID), description: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_scroll_x](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_scroll_x) ( id: [RID](class_rid.md#class_RID), position: [float](class_float.md#class_float) ) |
| void | [accessibility_update_set_scroll_x_range](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_scroll_x_range) ( id: [RID](class_rid.md#class_RID), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) |
| void | [accessibility_update_set_scroll_y](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_scroll_y) ( id: [RID](class_rid.md#class_RID), position: [float](class_float.md#class_float) ) |
| void | [accessibility_update_set_scroll_y_range](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_scroll_y_range) ( id: [RID](class_rid.md#class_RID), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) |
| void | [accessibility_update_set_shortcut](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_shortcut) ( id: [RID](class_rid.md#class_RID), shortcut: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_state_description](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_state_description) ( id: [RID](class_rid.md#class_RID), description: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_table_cell_position](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_cell_position) ( id: [RID](class_rid.md#class_RID), row_index: [int](class_int.md#class_int), column_index: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_table_cell_span](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_cell_span) ( id: [RID](class_rid.md#class_RID), row_span: [int](class_int.md#class_int), column_span: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_table_column_count](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_column_count) ( id: [RID](class_rid.md#class_RID), count: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_table_column_index](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_column_index) ( id: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_table_row_count](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_row_count) ( id: [RID](class_rid.md#class_RID), count: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_table_row_index](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_row_index) ( id: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_text_align](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_text_align) ( id: [RID](class_rid.md#class_RID), align: HorizontalAlignment ) |
| void | [accessibility_update_set_text_decorations](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_text_decorations) ( id: [RID](class_rid.md#class_RID), underline: [bool](class_bool.md#class_bool), strikethrough: [bool](class_bool.md#class_bool), overline: [bool](class_bool.md#class_bool) ) |
| void | [accessibility_update_set_text_orientation](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_text_orientation) ( id: [RID](class_rid.md#class_RID), vertical: [bool](class_bool.md#class_bool) ) |
| void | [accessibility_update_set_text_selection](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_text_selection) ( id: [RID](class_rid.md#class_RID), text_start_id: [RID](class_rid.md#class_RID), start_char: [int](class_int.md#class_int), text_end_id: [RID](class_rid.md#class_RID), end_char: [int](class_int.md#class_int) ) |
| void | [accessibility_update_set_tooltip](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_tooltip) ( id: [RID](class_rid.md#class_RID), tooltip: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_transform](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_transform) ( id: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [accessibility_update_set_url](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_url) ( id: [RID](class_rid.md#class_RID), url: [String](class_string.md#class_String) ) |
| void | [accessibility_update_set_value](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_value) ( id: [RID](class_rid.md#class_RID), value: [String](class_string.md#class_String) ) |
| void | [beep](class_displayserver.md#class_DisplayServer_method_beep) ( ) const |
| [String](class_string.md#class_String) | [clipboard_get](class_displayserver.md#class_DisplayServer_method_clipboard_get) ( ) const |
| [Image](class_image.md#class_Image) | [clipboard_get_image](class_displayserver.md#class_DisplayServer_method_clipboard_get_image) ( ) const |
| [String](class_string.md#class_String) | [clipboard_get_primary](class_displayserver.md#class_DisplayServer_method_clipboard_get_primary) ( ) const |
| [bool](class_bool.md#class_bool) | [clipboard_has](class_displayserver.md#class_DisplayServer_method_clipboard_has) ( ) const |
| [bool](class_bool.md#class_bool) | [clipboard_has_image](class_displayserver.md#class_DisplayServer_method_clipboard_has_image) ( ) const |
| void | [clipboard_set](class_displayserver.md#class_DisplayServer_method_clipboard_set) ( clipboard: [String](class_string.md#class_String) ) |
| void | [clipboard_set_primary](class_displayserver.md#class_DisplayServer_method_clipboard_set_primary) ( clipboard_primary: [String](class_string.md#class_String) ) |
| [bool](class_bool.md#class_bool) | [color_picker](class_displayserver.md#class_DisplayServer_method_color_picker) ( callback: [Callable](class_callable.md#class_Callable) ) |
| [int](class_int.md#class_int) | [create_status_indicator](class_displayserver.md#class_DisplayServer_method_create_status_indicator) ( icon: [Texture2D](class_texture2d.md#class_Texture2D), tooltip: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) ) |
| [CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) | [cursor_get_shape](class_displayserver.md#class_DisplayServer_method_cursor_get_shape) ( ) const |
| void | [cursor_set_custom_image](class_displayserver.md#class_DisplayServer_method_cursor_set_custom_image) ( cursor: [Resource](class_resource.md#class_Resource), shape: [CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) = 0, hotspot: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) |
| void | [cursor_set_shape](class_displayserver.md#class_DisplayServer_method_cursor_set_shape) ( shape: [CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) ) |
| void | [delete_status_indicator](class_displayserver.md#class_DisplayServer_method_delete_status_indicator) ( id: [int](class_int.md#class_int) ) |
| Error | [dialog_input_text](class_displayserver.md#class_DisplayServer_method_dialog_input_text) ( title: [String](class_string.md#class_String), description: [String](class_string.md#class_String), existing_text: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) ) |
| Error | [dialog_show](class_displayserver.md#class_DisplayServer_method_dialog_show) ( title: [String](class_string.md#class_String), description: [String](class_string.md#class_String), buttons: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), callback: [Callable](class_callable.md#class_Callable) ) |
| void | [enable_for_stealing_focus](class_displayserver.md#class_DisplayServer_method_enable_for_stealing_focus) ( process_id: [int](class_int.md#class_int) ) |
| Error | [file_dialog_show](class_displayserver.md#class_DisplayServer_method_file_dialog_show) ( title: [String](class_string.md#class_String), current_directory: [String](class_string.md#class_String), filename: [String](class_string.md#class_String), show_hidden: [bool](class_bool.md#class_bool), mode: [FileDialogMode](class_displayserver.md#enum_DisplayServer_FileDialogMode), filters: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), callback: [Callable](class_callable.md#class_Callable), parent_window_id: [int](class_int.md#class_int) = 0 ) |
| Error | [file_dialog_with_options_show](class_displayserver.md#class_DisplayServer_method_file_dialog_with_options_show) ( title: [String](class_string.md#class_String), current_directory: [String](class_string.md#class_String), root: [String](class_string.md#class_String), filename: [String](class_string.md#class_String), show_hidden: [bool](class_bool.md#class_bool), mode: [FileDialogMode](class_displayserver.md#enum_DisplayServer_FileDialogMode), filters: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), options: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\], callback: [Callable](class_callable.md#class_Callable), parent_window_id: [int](class_int.md#class_int) = 0 ) |
| void | [force_process_and_drop_events](class_displayserver.md#class_DisplayServer_method_force_process_and_drop_events) ( ) |
| [Color](class_color.md#class_Color) | [get_accent_color](class_displayserver.md#class_DisplayServer_method_get_accent_color) ( ) const |
| [Color](class_color.md#class_Color) | [get_base_color](class_displayserver.md#class_DisplayServer_method_get_base_color) ( ) const |
| [Array](class_array.md#class_Array)\[[Rect2](class_rect2.md#class_Rect2)\] | [get_display_cutouts](class_displayserver.md#class_DisplayServer_method_get_display_cutouts) ( ) const |
| [Rect2i](class_rect2i.md#class_Rect2i) | [get_display_safe_area](class_displayserver.md#class_DisplayServer_method_get_display_safe_area) ( ) const |
| [int](class_int.md#class_int) | [get_keyboard_focus_screen](class_displayserver.md#class_DisplayServer_method_get_keyboard_focus_screen) ( ) const |
| [String](class_string.md#class_String) | [get_name](class_displayserver.md#class_DisplayServer_method_get_name) ( ) const |
| [int](class_int.md#class_int) | [get_primary_screen](class_displayserver.md#class_DisplayServer_method_get_primary_screen) ( ) const |
| [int](class_int.md#class_int) | [get_screen_count](class_displayserver.md#class_DisplayServer_method_get_screen_count) ( ) const |
| [int](class_int.md#class_int) | [get_screen_from_rect](class_displayserver.md#class_DisplayServer_method_get_screen_from_rect) ( rect: [Rect2](class_rect2.md#class_Rect2) ) const |
| [bool](class_bool.md#class_bool) | [get_swap_cancel_ok](class_displayserver.md#class_DisplayServer_method_get_swap_cancel_ok) ( ) |
| [int](class_int.md#class_int) | [get_window_at_screen_position](class_displayserver.md#class_DisplayServer_method_get_window_at_screen_position) ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_window_list](class_displayserver.md#class_DisplayServer_method_get_window_list) ( ) const |
| [int](class_int.md#class_int) | [global_menu_add_check_item](class_displayserver.md#class_DisplayServer_method_global_menu_add_check_item) ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [global_menu_add_icon_check_item](class_displayserver.md#class_DisplayServer_method_global_menu_add_icon_check_item) ( menu_root: [String](class_string.md#class_String), icon: [Texture2D](class_texture2d.md#class_Texture2D), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [global_menu_add_icon_item](class_displayserver.md#class_DisplayServer_method_global_menu_add_icon_item) ( menu_root: [String](class_string.md#class_String), icon: [Texture2D](class_texture2d.md#class_Texture2D), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [global_menu_add_icon_radio_check_item](class_displayserver.md#class_DisplayServer_method_global_menu_add_icon_radio_check_item) ( menu_root: [String](class_string.md#class_String), icon: [Texture2D](class_texture2d.md#class_Texture2D), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [global_menu_add_item](class_displayserver.md#class_DisplayServer_method_global_menu_add_item) ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [global_menu_add_multistate_item](class_displayserver.md#class_DisplayServer_method_global_menu_add_multistate_item) ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), max_states: [int](class_int.md#class_int), default_state: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [global_menu_add_radio_check_item](class_displayserver.md#class_DisplayServer_method_global_menu_add_radio_check_item) ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [global_menu_add_separator](class_displayserver.md#class_DisplayServer_method_global_menu_add_separator) ( menu_root: [String](class_string.md#class_String), index: [int](class_int.md#class_int) = -1 ) |
| [int](class_int.md#class_int) | [global_menu_add_submenu_item](class_displayserver.md#class_DisplayServer_method_global_menu_add_submenu_item) ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), submenu: [String](class_string.md#class_String), index: [int](class_int.md#class_int) = -1 ) |
| void | [global_menu_clear](class_displayserver.md#class_DisplayServer_method_global_menu_clear) ( menu_root: [String](class_string.md#class_String) ) |
| Key | [global_menu_get_item_accelerator](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_accelerator) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [Callable](class_callable.md#class_Callable) | [global_menu_get_item_callback](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_callback) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [global_menu_get_item_count](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_count) ( menu_root: [String](class_string.md#class_String) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [global_menu_get_item_icon](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_icon) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [global_menu_get_item_indentation_level](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_indentation_level) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [global_menu_get_item_index_from_tag](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_index_from_tag) ( menu_root: [String](class_string.md#class_String), tag: [Variant](class_variant.md#class_Variant) ) const |
| [int](class_int.md#class_int) | [global_menu_get_item_index_from_text](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_index_from_text) ( menu_root: [String](class_string.md#class_String), text: [String](class_string.md#class_String) ) const |
| [Callable](class_callable.md#class_Callable) | [global_menu_get_item_key_callback](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_key_callback) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [global_menu_get_item_max_states](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_max_states) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [global_menu_get_item_state](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_state) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [global_menu_get_item_submenu](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_submenu) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [global_menu_get_item_tag](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_tag) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [global_menu_get_item_text](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_text) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [global_menu_get_item_tooltip](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_tooltip) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [global_menu_get_system_menu_roots](class_displayserver.md#class_DisplayServer_method_global_menu_get_system_menu_roots) ( ) const |
| [bool](class_bool.md#class_bool) | [global_menu_is_item_checkable](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_checkable) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [global_menu_is_item_checked](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_checked) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [global_menu_is_item_disabled](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_disabled) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [global_menu_is_item_hidden](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_hidden) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [global_menu_is_item_radio_checkable](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_radio_checkable) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) const |
| void | [global_menu_remove_item](class_displayserver.md#class_DisplayServer_method_global_menu_remove_item) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) |
| void | [global_menu_set_item_accelerator](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_accelerator) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), keycode: Key ) |
| void | [global_menu_set_item_callback](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_callback) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) |
| void | [global_menu_set_item_checkable](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_checkable) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), checkable: [bool](class_bool.md#class_bool) ) |
| void | [global_menu_set_item_checked](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_checked) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), checked: [bool](class_bool.md#class_bool) ) |
| void | [global_menu_set_item_disabled](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_disabled) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) |
| void | [global_menu_set_item_hidden](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_hidden) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), hidden: [bool](class_bool.md#class_bool) ) |
| void | [global_menu_set_item_hover_callbacks](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_hover_callbacks) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) |
| void | [global_menu_set_item_icon](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_icon) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [global_menu_set_item_indentation_level](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_indentation_level) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), level: [int](class_int.md#class_int) ) |
| void | [global_menu_set_item_key_callback](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_key_callback) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), key_callback: [Callable](class_callable.md#class_Callable) ) |
| void | [global_menu_set_item_max_states](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_max_states) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), max_states: [int](class_int.md#class_int) ) |
| void | [global_menu_set_item_radio_checkable](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_radio_checkable) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), checkable: [bool](class_bool.md#class_bool) ) |
| void | [global_menu_set_item_state](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_state) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), state: [int](class_int.md#class_int) ) |
| void | [global_menu_set_item_submenu](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_submenu) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), submenu: [String](class_string.md#class_String) ) |
| void | [global_menu_set_item_tag](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_tag) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), tag: [Variant](class_variant.md#class_Variant) ) |
| void | [global_menu_set_item_text](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_text) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) |
| void | [global_menu_set_item_tooltip](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_tooltip) ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) |
| void | [global_menu_set_popup_callbacks](class_displayserver.md#class_DisplayServer_method_global_menu_set_popup_callbacks) ( menu_root: [String](class_string.md#class_String), open_callback: [Callable](class_callable.md#class_Callable), close_callback: [Callable](class_callable.md#class_Callable) ) |
| [bool](class_bool.md#class_bool) | [has_additional_outputs](class_displayserver.md#class_DisplayServer_method_has_additional_outputs) ( ) const |
| [bool](class_bool.md#class_bool) | [has_feature](class_displayserver.md#class_DisplayServer_method_has_feature) ( feature: [Feature](class_displayserver.md#enum_DisplayServer_Feature) ) const |
| [bool](class_bool.md#class_bool) | [has_hardware_keyboard](class_displayserver.md#class_DisplayServer_method_has_hardware_keyboard) ( ) const |
| void | [help_set_search_callbacks](class_displayserver.md#class_DisplayServer_method_help_set_search_callbacks) ( search_callback: [Callable](class_callable.md#class_Callable), action_callback: [Callable](class_callable.md#class_Callable) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [ime_get_selection](class_displayserver.md#class_DisplayServer_method_ime_get_selection) ( ) const |
| [String](class_string.md#class_String) | [ime_get_text](class_displayserver.md#class_DisplayServer_method_ime_get_text) ( ) const |
| [bool](class_bool.md#class_bool) | [is_dark_mode](class_displayserver.md#class_DisplayServer_method_is_dark_mode) ( ) const |
| [bool](class_bool.md#class_bool) | [is_dark_mode_supported](class_displayserver.md#class_DisplayServer_method_is_dark_mode_supported) ( ) const |
| [bool](class_bool.md#class_bool) | [is_touchscreen_available](class_displayserver.md#class_DisplayServer_method_is_touchscreen_available) ( ) const |
| [bool](class_bool.md#class_bool) | [is_window_transparency_available](class_displayserver.md#class_DisplayServer_method_is_window_transparency_available) ( ) const |
| [int](class_int.md#class_int) | [keyboard_get_current_layout](class_displayserver.md#class_DisplayServer_method_keyboard_get_current_layout) ( ) const |
| Key | [keyboard_get_keycode_from_physical](class_displayserver.md#class_DisplayServer_method_keyboard_get_keycode_from_physical) ( keycode: Key ) const |
| Key | [keyboard_get_label_from_physical](class_displayserver.md#class_DisplayServer_method_keyboard_get_label_from_physical) ( keycode: Key ) const |
| [int](class_int.md#class_int) | [keyboard_get_layout_count](class_displayserver.md#class_DisplayServer_method_keyboard_get_layout_count) ( ) const |
| [String](class_string.md#class_String) | [keyboard_get_layout_language](class_displayserver.md#class_DisplayServer_method_keyboard_get_layout_language) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [keyboard_get_layout_name](class_displayserver.md#class_DisplayServer_method_keyboard_get_layout_name) ( index: [int](class_int.md#class_int) ) const |
| void | [keyboard_set_current_layout](class_displayserver.md#class_DisplayServer_method_keyboard_set_current_layout) ( index: [int](class_int.md#class_int) ) |
| bitfield | \[MouseButtonMask\] | [mouse_get_button_state](class_displayserver.md#class_DisplayServer_method_mouse_get_button_state) ( ) | const |
| [MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) | [mouse_get_mode](class_displayserver.md#class_DisplayServer_method_mouse_get_mode) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [mouse_get_position](class_displayserver.md#class_DisplayServer_method_mouse_get_position) ( ) const |
| void | [mouse_set_mode](class_displayserver.md#class_DisplayServer_method_mouse_set_mode) ( mouse_mode: [MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) ) |
| void | [process_events](class_displayserver.md#class_DisplayServer_method_process_events) ( ) |
| void | [register_additional_output](class_displayserver.md#class_DisplayServer_method_register_additional_output) ( object: [Object](class_object.md#class_Object) ) |
| [int](class_int.md#class_int) | [screen_get_dpi](class_displayserver.md#class_DisplayServer_method_screen_get_dpi) ( screen: [int](class_int.md#class_int) = -1 ) const |
| [Image](class_image.md#class_Image) | [screen_get_image](class_displayserver.md#class_DisplayServer_method_screen_get_image) ( screen: [int](class_int.md#class_int) = -1 ) const |
| [Image](class_image.md#class_Image) | [screen_get_image_rect](class_displayserver.md#class_DisplayServer_method_screen_get_image_rect) ( rect: [Rect2i](class_rect2i.md#class_Rect2i) ) const |
| [float](class_float.md#class_float) | [screen_get_max_scale](class_displayserver.md#class_DisplayServer_method_screen_get_max_scale) ( ) const |
| [ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation) | [screen_get_orientation](class_displayserver.md#class_DisplayServer_method_screen_get_orientation) ( screen: [int](class_int.md#class_int) = -1 ) const |
| [Color](class_color.md#class_Color) | [screen_get_pixel](class_displayserver.md#class_DisplayServer_method_screen_get_pixel) ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [screen_get_position](class_displayserver.md#class_DisplayServer_method_screen_get_position) ( screen: [int](class_int.md#class_int) = -1 ) const |
| [float](class_float.md#class_float) | [screen_get_refresh_rate](class_displayserver.md#class_DisplayServer_method_screen_get_refresh_rate) ( screen: [int](class_int.md#class_int) = -1 ) const |
| [float](class_float.md#class_float) | [screen_get_scale](class_displayserver.md#class_DisplayServer_method_screen_get_scale) ( screen: [int](class_int.md#class_int) = -1 ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [screen_get_size](class_displayserver.md#class_DisplayServer_method_screen_get_size) ( screen: [int](class_int.md#class_int) = -1 ) const |
| [Rect2i](class_rect2i.md#class_Rect2i) | [screen_get_usable_rect](class_displayserver.md#class_DisplayServer_method_screen_get_usable_rect) ( screen: [int](class_int.md#class_int) = -1 ) const |
| [bool](class_bool.md#class_bool) | [screen_is_kept_on](class_displayserver.md#class_DisplayServer_method_screen_is_kept_on) ( ) const |
| void | [screen_set_keep_on](class_displayserver.md#class_DisplayServer_method_screen_set_keep_on) ( enable: [bool](class_bool.md#class_bool) ) |
| void | [screen_set_orientation](class_displayserver.md#class_DisplayServer_method_screen_set_orientation) ( orientation: [ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation), screen: [int](class_int.md#class_int) = -1 ) |
| void | [set_hardware_keyboard_connection_change_callback](class_displayserver.md#class_DisplayServer_method_set_hardware_keyboard_connection_change_callback) ( callable: [Callable](class_callable.md#class_Callable) ) |
| void | [set_icon](class_displayserver.md#class_DisplayServer_method_set_icon) ( image: [Image](class_image.md#class_Image) ) |
| void | [set_native_icon](class_displayserver.md#class_DisplayServer_method_set_native_icon) ( filename: [String](class_string.md#class_String) ) |
| void | [set_system_theme_change_callback](class_displayserver.md#class_DisplayServer_method_set_system_theme_change_callback) ( callable: [Callable](class_callable.md#class_Callable) ) |
| void | [show_emoji_and_symbol_picker](class_displayserver.md#class_DisplayServer_method_show_emoji_and_symbol_picker) ( ) const |
| [Rect2](class_rect2.md#class_Rect2) | [status_indicator_get_rect](class_displayserver.md#class_DisplayServer_method_status_indicator_get_rect) ( id: [int](class_int.md#class_int) ) const |
| void | [status_indicator_set_callback](class_displayserver.md#class_DisplayServer_method_status_indicator_set_callback) ( id: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) |
| void | [status_indicator_set_icon](class_displayserver.md#class_DisplayServer_method_status_indicator_set_icon) ( id: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [status_indicator_set_menu](class_displayserver.md#class_DisplayServer_method_status_indicator_set_menu) ( id: [int](class_int.md#class_int), menu_rid: [RID](class_rid.md#class_RID) ) |
| void | [status_indicator_set_tooltip](class_displayserver.md#class_DisplayServer_method_status_indicator_set_tooltip) ( id: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) |
| [String](class_string.md#class_String) | [tablet_get_current_driver](class_displayserver.md#class_DisplayServer_method_tablet_get_current_driver) ( ) const |
| [int](class_int.md#class_int) | [tablet_get_driver_count](class_displayserver.md#class_DisplayServer_method_tablet_get_driver_count) ( ) const |
| [String](class_string.md#class_String) | [tablet_get_driver_name](class_displayserver.md#class_DisplayServer_method_tablet_get_driver_name) ( idx: [int](class_int.md#class_int) ) const |
| void | [tablet_set_current_driver](class_displayserver.md#class_DisplayServer_method_tablet_set_current_driver) ( name: [String](class_string.md#class_String) ) |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [tts_get_voices](class_displayserver.md#class_DisplayServer_method_tts_get_voices) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [tts_get_voices_for_language](class_displayserver.md#class_DisplayServer_method_tts_get_voices_for_language) ( language: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [tts_is_paused](class_displayserver.md#class_DisplayServer_method_tts_is_paused) ( ) const |
| [bool](class_bool.md#class_bool) | [tts_is_speaking](class_displayserver.md#class_DisplayServer_method_tts_is_speaking) ( ) const |
| void | [tts_pause](class_displayserver.md#class_DisplayServer_method_tts_pause) ( ) |
| void | [tts_resume](class_displayserver.md#class_DisplayServer_method_tts_resume) ( ) |
| void | [tts_set_utterance_callback](class_displayserver.md#class_DisplayServer_method_tts_set_utterance_callback) ( event: [TTSUtteranceEvent](class_displayserver.md#enum_DisplayServer_TTSUtteranceEvent), callable: [Callable](class_callable.md#class_Callable) ) |
| void | [tts_speak](class_displayserver.md#class_DisplayServer_method_tts_speak) ( text: [String](class_string.md#class_String), voice: [String](class_string.md#class_String), volume: [int](class_int.md#class_int) = 50, pitch: [float](class_float.md#class_float) = 1.0, rate: [float](class_float.md#class_float) = 1.0, utterance_id: [int](class_int.md#class_int) = 0, interrupt: [bool](class_bool.md#class_bool) = false ) |
| void | [tts_stop](class_displayserver.md#class_DisplayServer_method_tts_stop) ( ) |
| void | [unregister_additional_output](class_displayserver.md#class_DisplayServer_method_unregister_additional_output) ( object: [Object](class_object.md#class_Object) ) |
| [int](class_int.md#class_int) | [virtual_keyboard_get_height](class_displayserver.md#class_DisplayServer_method_virtual_keyboard_get_height) ( ) const |
| void | [virtual_keyboard_hide](class_displayserver.md#class_DisplayServer_method_virtual_keyboard_hide) ( ) |
| void | [virtual_keyboard_show](class_displayserver.md#class_DisplayServer_method_virtual_keyboard_show) ( existing_text: [String](class_string.md#class_String), position: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), type: [VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) = 0, max_length: [int](class_int.md#class_int) = -1, cursor_start: [int](class_int.md#class_int) = -1, cursor_end: [int](class_int.md#class_int) = -1 ) |
| void | [warp_mouse](class_displayserver.md#class_DisplayServer_method_warp_mouse) ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [bool](class_bool.md#class_bool) | [window_can_draw](class_displayserver.md#class_DisplayServer_method_window_can_draw) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [window_get_active_popup](class_displayserver.md#class_DisplayServer_method_window_get_active_popup) ( ) const |
| [int](class_int.md#class_int) | [window_get_attached_instance_id](class_displayserver.md#class_DisplayServer_method_window_get_attached_instance_id) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [window_get_current_screen](class_displayserver.md#class_DisplayServer_method_window_get_current_screen) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [bool](class_bool.md#class_bool) | [window_get_flag](class_displayserver.md#class_DisplayServer_method_window_get_flag) ( flag: [WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags), window_id: [int](class_int.md#class_int) = 0 ) const |
| [float](class_float.md#class_float) | [window_get_hdr_output_current_max_luminance](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_max_luminance) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [float](class_float.md#class_float) | [window_get_hdr_output_current_reference_luminance](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_reference_luminance) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [float](class_float.md#class_float) | [window_get_hdr_output_max_luminance](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_max_luminance) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [float](class_float.md#class_float) | [window_get_hdr_output_reference_luminance](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_reference_luminance) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [window_get_max_size](class_displayserver.md#class_DisplayServer_method_window_get_max_size) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [window_get_min_size](class_displayserver.md#class_DisplayServer_method_window_get_min_size) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [WindowMode](class_displayserver.md#enum_DisplayServer_WindowMode) | [window_get_mode](class_displayserver.md#class_DisplayServer_method_window_get_mode) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [window_get_native_handle](class_displayserver.md#class_DisplayServer_method_window_get_native_handle) ( handle_type: [HandleType](class_displayserver.md#enum_DisplayServer_HandleType), window_id: [int](class_int.md#class_int) = 0 ) const |
| [float](class_float.md#class_float) | [window_get_output_max_linear_value](class_displayserver.md#class_DisplayServer_method_window_get_output_max_linear_value) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [Rect2i](class_rect2i.md#class_Rect2i) | [window_get_popup_safe_rect](class_displayserver.md#class_DisplayServer_method_window_get_popup_safe_rect) ( window: [int](class_int.md#class_int) ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [window_get_position](class_displayserver.md#class_DisplayServer_method_window_get_position) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [window_get_position_with_decorations](class_displayserver.md#class_DisplayServer_method_window_get_position_with_decorations) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [Vector3i](class_vector3i.md#class_Vector3i) | [window_get_safe_title_margins](class_displayserver.md#class_DisplayServer_method_window_get_safe_title_margins) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [window_get_size](class_displayserver.md#class_DisplayServer_method_window_get_size) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [window_get_size_with_decorations](class_displayserver.md#class_DisplayServer_method_window_get_size_with_decorations) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [window_get_title_size](class_displayserver.md#class_DisplayServer_method_window_get_title_size) ( title: [String](class_string.md#class_String), window_id: [int](class_int.md#class_int) = 0 ) const |
| [VSyncMode](class_displayserver.md#enum_DisplayServer_VSyncMode) | [window_get_vsync_mode](class_displayserver.md#class_DisplayServer_method_window_get_vsync_mode) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [bool](class_bool.md#class_bool) | [window_is_focused](class_displayserver.md#class_DisplayServer_method_window_is_focused) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [bool](class_bool.md#class_bool) | [window_is_hdr_output_enabled](class_displayserver.md#class_DisplayServer_method_window_is_hdr_output_enabled) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [bool](class_bool.md#class_bool) | [window_is_hdr_output_requested](class_displayserver.md#class_DisplayServer_method_window_is_hdr_output_requested) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [bool](class_bool.md#class_bool) | [window_is_hdr_output_supported](class_displayserver.md#class_DisplayServer_method_window_is_hdr_output_supported) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [bool](class_bool.md#class_bool) | [window_is_maximize_allowed](class_displayserver.md#class_DisplayServer_method_window_is_maximize_allowed) ( window_id: [int](class_int.md#class_int) = 0 ) const |
| [bool](class_bool.md#class_bool) | [window_maximize_on_title_dbl_click](class_displayserver.md#class_DisplayServer_method_window_maximize_on_title_dbl_click) ( ) const |
| [bool](class_bool.md#class_bool) | [window_minimize_on_title_dbl_click](class_displayserver.md#class_DisplayServer_method_window_minimize_on_title_dbl_click) ( ) const |
| void | [window_move_to_foreground](class_displayserver.md#class_DisplayServer_method_window_move_to_foreground) ( window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_request_attention](class_displayserver.md#class_DisplayServer_method_window_request_attention) ( window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_request_hdr_output](class_displayserver.md#class_DisplayServer_method_window_request_hdr_output) ( enable: [bool](class_bool.md#class_bool), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_color](class_displayserver.md#class_DisplayServer_method_window_set_color) ( color: [Color](class_color.md#class_Color) ) |
| void | [window_set_current_screen](class_displayserver.md#class_DisplayServer_method_window_set_current_screen) ( screen: [int](class_int.md#class_int), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_drop_files_callback](class_displayserver.md#class_DisplayServer_method_window_set_drop_files_callback) ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_exclusive](class_displayserver.md#class_DisplayServer_method_window_set_exclusive) ( window_id: [int](class_int.md#class_int), exclusive: [bool](class_bool.md#class_bool) ) |
| void | [window_set_flag](class_displayserver.md#class_DisplayServer_method_window_set_flag) ( flag: [WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags), enabled: [bool](class_bool.md#class_bool), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_hdr_output_max_luminance](class_displayserver.md#class_DisplayServer_method_window_set_hdr_output_max_luminance) ( max_luminance: [float](class_float.md#class_float), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_hdr_output_reference_luminance](class_displayserver.md#class_DisplayServer_method_window_set_hdr_output_reference_luminance) ( reference_luminance: [float](class_float.md#class_float), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_ime_active](class_displayserver.md#class_DisplayServer_method_window_set_ime_active) ( active: [bool](class_bool.md#class_bool), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_ime_position](class_displayserver.md#class_DisplayServer_method_window_set_ime_position) ( position: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_input_event_callback](class_displayserver.md#class_DisplayServer_method_window_set_input_event_callback) ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_input_text_callback](class_displayserver.md#class_DisplayServer_method_window_set_input_text_callback) ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_max_size](class_displayserver.md#class_DisplayServer_method_window_set_max_size) ( max_size: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_min_size](class_displayserver.md#class_DisplayServer_method_window_set_min_size) ( min_size: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_mode](class_displayserver.md#class_DisplayServer_method_window_set_mode) ( mode: [WindowMode](class_displayserver.md#enum_DisplayServer_WindowMode), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_mouse_passthrough](class_displayserver.md#class_DisplayServer_method_window_set_mouse_passthrough) ( region: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_popup_safe_rect](class_displayserver.md#class_DisplayServer_method_window_set_popup_safe_rect) ( window: [int](class_int.md#class_int), rect: [Rect2i](class_rect2i.md#class_Rect2i) ) |
| void | [window_set_position](class_displayserver.md#class_DisplayServer_method_window_set_position) ( position: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_rect_changed_callback](class_displayserver.md#class_DisplayServer_method_window_set_rect_changed_callback) ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_size](class_displayserver.md#class_DisplayServer_method_window_set_size) ( size: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_title](class_displayserver.md#class_DisplayServer_method_window_set_title) ( title: [String](class_string.md#class_String), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_transient](class_displayserver.md#class_DisplayServer_method_window_set_transient) ( window_id: [int](class_int.md#class_int), parent_window_id: [int](class_int.md#class_int) ) |
| void | [window_set_vsync_mode](class_displayserver.md#class_DisplayServer_method_window_set_vsync_mode) ( vsync_mode: [VSyncMode](class_displayserver.md#enum_DisplayServer_VSyncMode), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_window_buttons_offset](class_displayserver.md#class_DisplayServer_method_window_set_window_buttons_offset) ( offset: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_set_window_event_callback](class_displayserver.md#class_DisplayServer_method_window_set_window_event_callback) ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_start_drag](class_displayserver.md#class_DisplayServer_method_window_start_drag) ( window_id: [int](class_int.md#class_int) = 0 ) |
| void | [window_start_resize](class_displayserver.md#class_DisplayServer_method_window_start_resize) ( edge: [WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge), window_id: [int](class_int.md#class_int) = 0 ) |

---

### Signals

<span id="class_DisplayServer_signal_orientation_changed"></span>

**orientation_changed** ( orientation: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_signal_orientation_changed)

Emitted when the device orientation changes. `orientation` is the new orientation.

Returns `1` for portrait, `2` for landscape, and `0` if the orientation is undefined.

 **Note:** This method is implemented on Android and iOS.

---

### Enumerations

<span id="enum_DisplayServer_Feature"></span>

enum **Feature**: [🔗](class_displayserver.md#enum_DisplayServer_Feature)

<span id="class_DisplayServer_constant_FEATURE_GLOBAL_MENU"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_GLOBAL_MENU** = `0`

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Display server supports global menu. This allows the application to display its menu items in the operating system's top bar. **macOS**

<span id="class_DisplayServer_constant_FEATURE_SUBWINDOWS"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_SUBWINDOWS** = `1`

Display server supports multiple windows that can be moved outside of the main window. **Windows, macOS, Linux (X11)**

<span id="class_DisplayServer_constant_FEATURE_TOUCHSCREEN"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_TOUCHSCREEN** = `2`

Display server supports touchscreen input. **Windows, Linux (X11), Android, iOS, Web**

<span id="class_DisplayServer_constant_FEATURE_MOUSE"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_MOUSE** = `3`

Display server supports mouse input. **Windows, macOS, Linux (X11/Wayland), Android, Web**

<span id="class_DisplayServer_constant_FEATURE_MOUSE_WARP"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_MOUSE_WARP** = `4`

Display server supports warping mouse coordinates to keep the mouse cursor constrained within an area, but looping when one of the edges is reached. **Windows, macOS, Linux (X11/Wayland)**

<span id="class_DisplayServer_constant_FEATURE_CLIPBOARD"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_CLIPBOARD** = `5`

Display server supports setting and getting clipboard data. See also [FEATURE_CLIPBOARD_PRIMARY](class_displayserver.md#class_DisplayServer_constant_FEATURE_CLIPBOARD_PRIMARY). **Windows, macOS, Linux (X11/Wayland), Android, iOS, Web**

<span id="class_DisplayServer_constant_FEATURE_VIRTUAL_KEYBOARD"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_VIRTUAL_KEYBOARD** = `6`

Display server supports popping up a virtual keyboard when requested to input text without a physical keyboard. **Android, iOS, Web**

<span id="class_DisplayServer_constant_FEATURE_CURSOR_SHAPE"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_CURSOR_SHAPE** = `7`

Display server supports setting the mouse cursor shape to be different from the default. **Windows, macOS, Linux (X11/Wayland), Android, Web**

<span id="class_DisplayServer_constant_FEATURE_CUSTOM_CURSOR_SHAPE"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_CUSTOM_CURSOR_SHAPE** = `8`

Display server supports setting the mouse cursor shape to a custom image. **Windows, macOS, Linux (X11/Wayland), Web**

<span id="class_DisplayServer_constant_FEATURE_NATIVE_DIALOG"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_NATIVE_DIALOG** = `9`

Display server supports spawning text dialogs using the operating system's native look-and-feel. See [dialog_show()](class_displayserver.md#class_DisplayServer_method_dialog_show). **Windows, macOS**

<span id="class_DisplayServer_constant_FEATURE_IME"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_IME** = `10`

Display server supports Input Method Editor, which is commonly used for inputting Chinese/Japanese/Korean text. This is handled by the operating system, rather than by Godot. **Windows, macOS, Linux (X11)**

<span id="class_DisplayServer_constant_FEATURE_WINDOW_TRANSPARENCY"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_WINDOW_TRANSPARENCY** = `11`

Display server supports windows can use per-pixel transparency to make windows behind them partially or fully visible. **Windows, macOS, Linux (X11/Wayland), Android**

<span id="class_DisplayServer_constant_FEATURE_HIDPI"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_HIDPI** = `12`

Display server supports querying the operating system's display scale factor. This allows automatically detecting the hiDPI display *reliably*, instead of guessing based on the screen resolution and the display's reported DPI (which might be unreliable due to broken monitor EDID). **Windows, Linux (Wayland), macOS**

<span id="class_DisplayServer_constant_FEATURE_ICON"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_ICON** = `13`

Display server supports changing the window icon (usually displayed in the top-left corner). **Windows, macOS, Linux (X11/Wayland)**

 **Note:** Use on Wayland requires the compositor to implement the xdg_toplevel_icon_v1 protocol, which not all compositors do. See xdg_toplevel_icon_v1#compositor-support for more information on individual compositor support.

<span id="class_DisplayServer_constant_FEATURE_NATIVE_ICON"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_NATIVE_ICON** = `14`

Display server supports changing the window icon (usually displayed in the top-left corner). **Windows, macOS**

<span id="class_DisplayServer_constant_FEATURE_ORIENTATION"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_ORIENTATION** = `15`

Display server supports changing the screen orientation. **Android, iOS**

<span id="class_DisplayServer_constant_FEATURE_SWAP_BUFFERS"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_SWAP_BUFFERS** = `16`

Display server supports V-Sync status can be changed from the default (which is forced to be enabled platforms not supporting this feature). **Windows, macOS, Linux (X11/Wayland)**

<span id="class_DisplayServer_constant_FEATURE_CLIPBOARD_PRIMARY"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_CLIPBOARD_PRIMARY** = `18`

Display server supports Primary clipboard can be used. This is a different clipboard from [FEATURE_CLIPBOARD](class_displayserver.md#class_DisplayServer_constant_FEATURE_CLIPBOARD). **Linux (X11/Wayland)**

<span id="class_DisplayServer_constant_FEATURE_TEXT_TO_SPEECH"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_TEXT_TO_SPEECH** = `19`

Display server supports text-to-speech. See `tts_*` methods. **Windows, macOS, Linux (X11/Wayland), Android, iOS, Web**

<span id="class_DisplayServer_constant_FEATURE_EXTEND_TO_TITLE"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_EXTEND_TO_TITLE** = `20`

Display server supports expanding window content to the title. See [WINDOW_FLAG_EXTEND_TO_TITLE](class_displayserver.md#class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE). **macOS**

<span id="class_DisplayServer_constant_FEATURE_SCREEN_CAPTURE"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_SCREEN_CAPTURE** = `21`

Display server supports reading screen pixels. See [screen_get_pixel()](class_displayserver.md#class_DisplayServer_method_screen_get_pixel).

<span id="class_DisplayServer_constant_FEATURE_STATUS_INDICATOR"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_STATUS_INDICATOR** = `22`

Display server supports application status indicators.

<span id="class_DisplayServer_constant_FEATURE_NATIVE_HELP"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_NATIVE_HELP** = `23`

Display server supports native help system search callbacks. See [help_set_search_callbacks()](class_displayserver.md#class_DisplayServer_method_help_set_search_callbacks).

<span id="class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_INPUT"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_NATIVE_DIALOG_INPUT** = `24`

Display server supports spawning text input dialogs using the operating system's native look-and-feel. See [dialog_input_text()](class_displayserver.md#class_DisplayServer_method_dialog_input_text). **Windows, macOS**

<span id="class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_FILE"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_NATIVE_DIALOG_FILE** = `25`

Display server supports spawning dialogs for selecting files or directories using the operating system's native look-and-feel. See [file_dialog_show()](class_displayserver.md#class_DisplayServer_method_file_dialog_show). **Windows, macOS, Linux (X11/Wayland), Android**

<span id="class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_FILE_EXTRA"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_NATIVE_DIALOG_FILE_EXTRA** = `26`

The display server supports all features of [FEATURE_NATIVE_DIALOG_FILE](class_displayserver.md#class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_FILE), with the added functionality of Options and native dialog file access to `res://` and `user://` paths. See [file_dialog_show()](class_displayserver.md#class_DisplayServer_method_file_dialog_show) and [file_dialog_with_options_show()](class_displayserver.md#class_DisplayServer_method_file_dialog_with_options_show). **Windows, macOS, Linux (X11/Wayland)**

<span id="class_DisplayServer_constant_FEATURE_WINDOW_DRAG"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_WINDOW_DRAG** = `27`

The display server supports initiating window drag and resize operations on demand. See [window_start_drag()](class_displayserver.md#class_DisplayServer_method_window_start_drag) and [window_start_resize()](class_displayserver.md#class_DisplayServer_method_window_start_resize).

<span id="class_DisplayServer_constant_FEATURE_SCREEN_EXCLUDE_FROM_CAPTURE"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_SCREEN_EXCLUDE_FROM_CAPTURE** = `28`

Display server supports [WINDOW_FLAG_EXCLUDE_FROM_CAPTURE](class_displayserver.md#class_DisplayServer_constant_WINDOW_FLAG_EXCLUDE_FROM_CAPTURE) window flag. **Windows, macOS**

<span id="class_DisplayServer_constant_FEATURE_WINDOW_EMBEDDING"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_WINDOW_EMBEDDING** = `29`

Display server supports embedding a window from another process. **Windows, Linux (X11), macOS**

<span id="class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_FILE_MIME"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_NATIVE_DIALOG_FILE_MIME** = `30`

Native file selection dialog supports MIME types as filters.

<span id="class_DisplayServer_constant_FEATURE_EMOJI_AND_SYMBOL_PICKER"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_EMOJI_AND_SYMBOL_PICKER** = `31`

Display server supports system emoji and symbol picker. **Windows, macOS**

<span id="class_DisplayServer_constant_FEATURE_NATIVE_COLOR_PICKER"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_NATIVE_COLOR_PICKER** = `32`

Display server supports native color picker. **Linux (X11/Wayland)**

<span id="class_DisplayServer_constant_FEATURE_SELF_FITTING_WINDOWS"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_SELF_FITTING_WINDOWS** = `33`

Display server automatically fits popups according to the screen boundaries. Window nodes should not attempt to do that themselves.

<span id="class_DisplayServer_constant_FEATURE_ACCESSIBILITY_SCREEN_READER"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_ACCESSIBILITY_SCREEN_READER** = `34`

Display server supports interaction with screen reader or Braille display. **Linux (X11/Wayland), macOS, Windows**

<span id="class_DisplayServer_constant_FEATURE_HDR_OUTPUT"></span>

[Feature](class_displayserver.md#enum_DisplayServer_Feature) **FEATURE_HDR_OUTPUT** = `35`

Display server supports HDR output. **Windows**

---

<span id="enum_DisplayServer_AccessibilityRole"></span>

enum **AccessibilityRole**: [🔗](class_displayserver.md#enum_DisplayServer_AccessibilityRole)

<span id="class_DisplayServer_constant_ROLE_UNKNOWN"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_UNKNOWN** = `0`

Unknown or custom role.

<span id="class_DisplayServer_constant_ROLE_DEFAULT_BUTTON"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_DEFAULT_BUTTON** = `1`

Default dialog button element.

<span id="class_DisplayServer_constant_ROLE_AUDIO"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_AUDIO** = `2`

Audio player element.

<span id="class_DisplayServer_constant_ROLE_VIDEO"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_VIDEO** = `3`

Video player element.

<span id="class_DisplayServer_constant_ROLE_STATIC_TEXT"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_STATIC_TEXT** = `4`

Non-editable text label.

<span id="class_DisplayServer_constant_ROLE_CONTAINER"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_CONTAINER** = `5`

Container element. Elements with this role are used for internal structure and ignored by screen readers.

<span id="class_DisplayServer_constant_ROLE_PANEL"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_PANEL** = `6`

Panel container element.

<span id="class_DisplayServer_constant_ROLE_BUTTON"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_BUTTON** = `7`

Button element.

<span id="class_DisplayServer_constant_ROLE_LINK"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_LINK** = `8`

Link element.

<span id="class_DisplayServer_constant_ROLE_CHECK_BOX"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_CHECK_BOX** = `9`

Check box element.

<span id="class_DisplayServer_constant_ROLE_RADIO_BUTTON"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_RADIO_BUTTON** = `10`

Radio button element.

<span id="class_DisplayServer_constant_ROLE_CHECK_BUTTON"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_CHECK_BUTTON** = `11`

Check button element.

<span id="class_DisplayServer_constant_ROLE_SCROLL_BAR"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_SCROLL_BAR** = `12`

Scroll bar element.

<span id="class_DisplayServer_constant_ROLE_SCROLL_VIEW"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_SCROLL_VIEW** = `13`

Scroll container element.

<span id="class_DisplayServer_constant_ROLE_SPLITTER"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_SPLITTER** = `14`

Container splitter handle element.

<span id="class_DisplayServer_constant_ROLE_SLIDER"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_SLIDER** = `15`

Slider element.

<span id="class_DisplayServer_constant_ROLE_SPIN_BUTTON"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_SPIN_BUTTON** = `16`

Spin box element.

<span id="class_DisplayServer_constant_ROLE_PROGRESS_INDICATOR"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_PROGRESS_INDICATOR** = `17`

Progress indicator element.

<span id="class_DisplayServer_constant_ROLE_TEXT_FIELD"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_TEXT_FIELD** = `18`

Editable text field element.

<span id="class_DisplayServer_constant_ROLE_MULTILINE_TEXT_FIELD"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_MULTILINE_TEXT_FIELD** = `19`

Multiline editable text field element.

<span id="class_DisplayServer_constant_ROLE_COLOR_PICKER"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_COLOR_PICKER** = `20`

Color picker element.

<span id="class_DisplayServer_constant_ROLE_TABLE"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_TABLE** = `21`

Table element.

<span id="class_DisplayServer_constant_ROLE_CELL"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_CELL** = `22`

Table/tree cell element.

<span id="class_DisplayServer_constant_ROLE_ROW"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_ROW** = `23`

Table/tree row element.

<span id="class_DisplayServer_constant_ROLE_ROW_GROUP"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_ROW_GROUP** = `24`

Table/tree row group element.

<span id="class_DisplayServer_constant_ROLE_ROW_HEADER"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_ROW_HEADER** = `25`

Table/tree row header element.

<span id="class_DisplayServer_constant_ROLE_COLUMN_HEADER"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_COLUMN_HEADER** = `26`

Table/tree column header element.

<span id="class_DisplayServer_constant_ROLE_TREE"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_TREE** = `27`

Tree view element.

<span id="class_DisplayServer_constant_ROLE_TREE_ITEM"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_TREE_ITEM** = `28`

Tree view item element.

<span id="class_DisplayServer_constant_ROLE_LIST"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_LIST** = `29`

List element.

<span id="class_DisplayServer_constant_ROLE_LIST_ITEM"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_LIST_ITEM** = `30`

List item element.

<span id="class_DisplayServer_constant_ROLE_LIST_BOX"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_LIST_BOX** = `31`

List view element.

<span id="class_DisplayServer_constant_ROLE_LIST_BOX_OPTION"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_LIST_BOX_OPTION** = `32`

List view item element.

<span id="class_DisplayServer_constant_ROLE_TAB_BAR"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_TAB_BAR** = `33`

Tab bar element.

<span id="class_DisplayServer_constant_ROLE_TAB"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_TAB** = `34`

Tab bar item element.

<span id="class_DisplayServer_constant_ROLE_TAB_PANEL"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_TAB_PANEL** = `35`

Tab panel element.

<span id="class_DisplayServer_constant_ROLE_MENU_BAR"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_MENU_BAR** = `36`

Menu bar element.

<span id="class_DisplayServer_constant_ROLE_MENU"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_MENU** = `37`

Popup menu element.

<span id="class_DisplayServer_constant_ROLE_MENU_ITEM"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_MENU_ITEM** = `38`

Popup menu item element.

<span id="class_DisplayServer_constant_ROLE_MENU_ITEM_CHECK_BOX"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_MENU_ITEM_CHECK_BOX** = `39`

Popup menu check button item element.

<span id="class_DisplayServer_constant_ROLE_MENU_ITEM_RADIO"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_MENU_ITEM_RADIO** = `40`

Popup menu radio button item element.

<span id="class_DisplayServer_constant_ROLE_IMAGE"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_IMAGE** = `41`

Image element.

<span id="class_DisplayServer_constant_ROLE_WINDOW"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_WINDOW** = `42`

Window element.

<span id="class_DisplayServer_constant_ROLE_TITLE_BAR"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_TITLE_BAR** = `43`

Embedded window title bar element.

<span id="class_DisplayServer_constant_ROLE_DIALOG"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_DIALOG** = `44`

Dialog window element.

<span id="class_DisplayServer_constant_ROLE_TOOLTIP"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_TOOLTIP** = `45`

Tooltip element.

<span id="class_DisplayServer_constant_ROLE_REGION"></span>

[AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) **ROLE_REGION** = `46`

Region/landmark element. Screen readers can navigate between regions using landmark navigation.

---

<span id="enum_DisplayServer_AccessibilityPopupType"></span>

enum **AccessibilityPopupType**: [🔗](class_displayserver.md#enum_DisplayServer_AccessibilityPopupType)

<span id="class_DisplayServer_constant_POPUP_MENU"></span>

[AccessibilityPopupType](class_displayserver.md#enum_DisplayServer_AccessibilityPopupType) **POPUP_MENU** = `0`

Popup menu.

<span id="class_DisplayServer_constant_POPUP_LIST"></span>

[AccessibilityPopupType](class_displayserver.md#enum_DisplayServer_AccessibilityPopupType) **POPUP_LIST** = `1`

Popup list.

<span id="class_DisplayServer_constant_POPUP_TREE"></span>

[AccessibilityPopupType](class_displayserver.md#enum_DisplayServer_AccessibilityPopupType) **POPUP_TREE** = `2`

Popup tree view.

<span id="class_DisplayServer_constant_POPUP_DIALOG"></span>

[AccessibilityPopupType](class_displayserver.md#enum_DisplayServer_AccessibilityPopupType) **POPUP_DIALOG** = `3`

Popup dialog.

---

<span id="enum_DisplayServer_AccessibilityFlags"></span>

enum **AccessibilityFlags**: [🔗](class_displayserver.md#enum_DisplayServer_AccessibilityFlags)

<span id="class_DisplayServer_constant_FLAG_HIDDEN"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_HIDDEN** = `0`

Element is hidden for accessibility tools.

<span id="class_DisplayServer_constant_FLAG_MULTISELECTABLE"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_MULTISELECTABLE** = `1`

Element supports multiple item selection.

<span id="class_DisplayServer_constant_FLAG_REQUIRED"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_REQUIRED** = `2`

Element require user input.

<span id="class_DisplayServer_constant_FLAG_VISITED"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_VISITED** = `3`

Element is a visited link.

<span id="class_DisplayServer_constant_FLAG_BUSY"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_BUSY** = `4`

Element content is not ready (e.g. loading).

<span id="class_DisplayServer_constant_FLAG_MODAL"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_MODAL** = `5`

Element is modal window.

<span id="class_DisplayServer_constant_FLAG_TOUCH_PASSTHROUGH"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_TOUCH_PASSTHROUGH** = `6`

Element allows touches to be passed through when a screen reader is in touch exploration mode.

<span id="class_DisplayServer_constant_FLAG_READONLY"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_READONLY** = `7`

Element is text field with selectable but read-only text.

<span id="class_DisplayServer_constant_FLAG_DISABLED"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_DISABLED** = `8`

Element is disabled.

<span id="class_DisplayServer_constant_FLAG_CLIPS_CHILDREN"></span>

[AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags) **FLAG_CLIPS_CHILDREN** = `9`

Element clips children.

---

<span id="enum_DisplayServer_AccessibilityAction"></span>

enum **AccessibilityAction**: [🔗](class_displayserver.md#enum_DisplayServer_AccessibilityAction)

<span id="class_DisplayServer_constant_ACTION_CLICK"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_CLICK** = `0`

Single click action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_FOCUS"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_FOCUS** = `1`

Focus action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_BLUR"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_BLUR** = `2`

Blur action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_COLLAPSE"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_COLLAPSE** = `3`

Collapse action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_EXPAND"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_EXPAND** = `4`

Expand action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_DECREMENT"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_DECREMENT** = `5`

Decrement action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_INCREMENT"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_INCREMENT** = `6`

Increment action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_HIDE_TOOLTIP"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_HIDE_TOOLTIP** = `7`

Hide tooltip action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_SHOW_TOOLTIP"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SHOW_TOOLTIP** = `8`

Show tooltip action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_SET_TEXT_SELECTION"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SET_TEXT_SELECTION** = `9`

Set text selection action, callback argument is set to [Dictionary](class_dictionary.md#class_Dictionary) with the following keys:

- `"start_element"` accessibility element of the selection start.

- `"start_char"` character offset relative to the accessibility element of the selection start.

- `"end_element"` accessibility element of the selection end.

- `"end_char"` character offset relative to the accessibility element of the selection end.

<span id="class_DisplayServer_constant_ACTION_REPLACE_SELECTED_TEXT"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_REPLACE_SELECTED_TEXT** = `10`

Replace text action, callback argument is set to [String](class_string.md#class_String) with the replacement text.

<span id="class_DisplayServer_constant_ACTION_SCROLL_BACKWARD"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SCROLL_BACKWARD** = `11`

Scroll backward action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_SCROLL_DOWN"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SCROLL_DOWN** = `12`

Scroll down action, callback argument is set to [AccessibilityScrollUnit](class_displayserver.md#enum_DisplayServer_AccessibilityScrollUnit).

<span id="class_DisplayServer_constant_ACTION_SCROLL_FORWARD"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SCROLL_FORWARD** = `13`

Scroll forward action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_SCROLL_LEFT"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SCROLL_LEFT** = `14`

Scroll left action, callback argument is set to [AccessibilityScrollUnit](class_displayserver.md#enum_DisplayServer_AccessibilityScrollUnit).

<span id="class_DisplayServer_constant_ACTION_SCROLL_RIGHT"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SCROLL_RIGHT** = `15`

Scroll right action, callback argument is set to [AccessibilityScrollUnit](class_displayserver.md#enum_DisplayServer_AccessibilityScrollUnit).

<span id="class_DisplayServer_constant_ACTION_SCROLL_UP"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SCROLL_UP** = `16`

Scroll up action, callback argument is set to [AccessibilityScrollUnit](class_displayserver.md#enum_DisplayServer_AccessibilityScrollUnit).

<span id="class_DisplayServer_constant_ACTION_SCROLL_INTO_VIEW"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SCROLL_INTO_VIEW** = `17`

Scroll into view action, callback argument is set to [AccessibilityScrollHint](class_displayserver.md#enum_DisplayServer_AccessibilityScrollHint).

<span id="class_DisplayServer_constant_ACTION_SCROLL_TO_POINT"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SCROLL_TO_POINT** = `18`

Scroll to point action, callback argument is set to [Vector2](class_vector2.md#class_Vector2) with the relative point coordinates.

<span id="class_DisplayServer_constant_ACTION_SET_SCROLL_OFFSET"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SET_SCROLL_OFFSET** = `19`

Set scroll offset action, callback argument is set to [Vector2](class_vector2.md#class_Vector2) with the scroll offset.

<span id="class_DisplayServer_constant_ACTION_SET_VALUE"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SET_VALUE** = `20`

Set value action, callback argument is set to [String](class_string.md#class_String) or number with the new value.

<span id="class_DisplayServer_constant_ACTION_SHOW_CONTEXT_MENU"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_SHOW_CONTEXT_MENU** = `21`

Show context menu action, callback argument is not set.

<span id="class_DisplayServer_constant_ACTION_CUSTOM"></span>

[AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction) **ACTION_CUSTOM** = `22`

Custom action, callback argument is set to the integer action ID.

---

<span id="enum_DisplayServer_AccessibilityLiveMode"></span>

enum **AccessibilityLiveMode**: [🔗](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode)

<span id="class_DisplayServer_constant_LIVE_OFF"></span>

[AccessibilityLiveMode](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode) **LIVE_OFF** = `0`

Indicates that updates to the live region should not be presented.

<span id="class_DisplayServer_constant_LIVE_POLITE"></span>

[AccessibilityLiveMode](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode) **LIVE_POLITE** = `1`

Indicates that updates to the live region should be presented at the next opportunity (for example at the end of speaking the current sentence).

<span id="class_DisplayServer_constant_LIVE_ASSERTIVE"></span>

[AccessibilityLiveMode](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode) **LIVE_ASSERTIVE** = `2`

Indicates that updates to the live region have the highest priority and should be presented immediately.

---

<span id="enum_DisplayServer_AccessibilityScrollUnit"></span>

enum **AccessibilityScrollUnit**: [🔗](class_displayserver.md#enum_DisplayServer_AccessibilityScrollUnit)

<span id="class_DisplayServer_constant_SCROLL_UNIT_ITEM"></span>

[AccessibilityScrollUnit](class_displayserver.md#enum_DisplayServer_AccessibilityScrollUnit) **SCROLL_UNIT_ITEM** = `0`

The amount by which to scroll. A single item of a list, line of text.

<span id="class_DisplayServer_constant_SCROLL_UNIT_PAGE"></span>

[AccessibilityScrollUnit](class_displayserver.md#enum_DisplayServer_AccessibilityScrollUnit) **SCROLL_UNIT_PAGE** = `1`

The amount by which to scroll. A single page.

---

<span id="enum_DisplayServer_AccessibilityScrollHint"></span>

enum **AccessibilityScrollHint**: [🔗](class_displayserver.md#enum_DisplayServer_AccessibilityScrollHint)

<span id="class_DisplayServer_constant_SCROLL_HINT_TOP_LEFT"></span>

[AccessibilityScrollHint](class_displayserver.md#enum_DisplayServer_AccessibilityScrollHint) **SCROLL_HINT_TOP_LEFT** = `0`

A preferred position for the node scrolled into view. Top-left edge of the scroll container.

<span id="class_DisplayServer_constant_SCROLL_HINT_BOTTOM_RIGHT"></span>

[AccessibilityScrollHint](class_displayserver.md#enum_DisplayServer_AccessibilityScrollHint) **SCROLL_HINT_BOTTOM_RIGHT** = `1`

A preferred position for the node scrolled into view. Bottom-right edge of the scroll container.

<span id="class_DisplayServer_constant_SCROLL_HINT_TOP_EDGE"></span>

[AccessibilityScrollHint](class_displayserver.md#enum_DisplayServer_AccessibilityScrollHint) **SCROLL_HINT_TOP_EDGE** = `2`

A preferred position for the node scrolled into view. Top edge of the scroll container.

<span id="class_DisplayServer_constant_SCROLL_HINT_BOTTOM_EDGE"></span>

[AccessibilityScrollHint](class_displayserver.md#enum_DisplayServer_AccessibilityScrollHint) **SCROLL_HINT_BOTTOM_EDGE** = `3`

A preferred position for the node scrolled into view. Bottom edge of the scroll container.

<span id="class_DisplayServer_constant_SCROLL_HINT_LEFT_EDGE"></span>

[AccessibilityScrollHint](class_displayserver.md#enum_DisplayServer_AccessibilityScrollHint) **SCROLL_HINT_LEFT_EDGE** = `4`

A preferred position for the node scrolled into view. Left edge of the scroll container.

<span id="class_DisplayServer_constant_SCROLL_HINT_RIGHT_EDGE"></span>

[AccessibilityScrollHint](class_displayserver.md#enum_DisplayServer_AccessibilityScrollHint) **SCROLL_HINT_RIGHT_EDGE** = `5`

A preferred position for the node scrolled into view. Right edge of the scroll container.

---

<span id="enum_DisplayServer_MouseMode"></span>

enum **MouseMode**: [🔗](class_displayserver.md#enum_DisplayServer_MouseMode)

<span id="class_DisplayServer_constant_MOUSE_MODE_VISIBLE"></span>

[MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) **MOUSE_MODE_VISIBLE** = `0`

Makes the mouse cursor visible if it is hidden.

<span id="class_DisplayServer_constant_MOUSE_MODE_HIDDEN"></span>

[MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) **MOUSE_MODE_HIDDEN** = `1`

Makes the mouse cursor hidden if it is visible.

<span id="class_DisplayServer_constant_MOUSE_MODE_CAPTURED"></span>

[MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) **MOUSE_MODE_CAPTURED** = `2`

Captures the mouse. The mouse will be hidden and its position locked at the center of the window manager's window.

 **Note:** If you want to process the mouse's movement in this mode, you need to use [InputEventMouseMotion.relative](class_inputeventmousemotion.md#class_InputEventMouseMotion_property_relative).

<span id="class_DisplayServer_constant_MOUSE_MODE_CONFINED"></span>

[MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) **MOUSE_MODE_CONFINED** = `3`

Confines the mouse cursor to the game window, and make it visible.

<span id="class_DisplayServer_constant_MOUSE_MODE_CONFINED_HIDDEN"></span>

[MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) **MOUSE_MODE_CONFINED_HIDDEN** = `4`

Confines the mouse cursor to the game window, and make it hidden.

<span id="class_DisplayServer_constant_MOUSE_MODE_MAX"></span>

[MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) **MOUSE_MODE_MAX** = `5`

Max value of the [MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode).

---

<span id="enum_DisplayServer_ScreenOrientation"></span>

enum **ScreenOrientation**: [🔗](class_displayserver.md#enum_DisplayServer_ScreenOrientation)

<span id="class_DisplayServer_constant_SCREEN_LANDSCAPE"></span>

[ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation) **SCREEN_LANDSCAPE** = `0`

Default landscape orientation.

<span id="class_DisplayServer_constant_SCREEN_PORTRAIT"></span>

[ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation) **SCREEN_PORTRAIT** = `1`

Default portrait orientation.

<span id="class_DisplayServer_constant_SCREEN_REVERSE_LANDSCAPE"></span>

[ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation) **SCREEN_REVERSE_LANDSCAPE** = `2`

Reverse landscape orientation (upside down).

<span id="class_DisplayServer_constant_SCREEN_REVERSE_PORTRAIT"></span>

[ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation) **SCREEN_REVERSE_PORTRAIT** = `3`

Reverse portrait orientation (upside down).

<span id="class_DisplayServer_constant_SCREEN_SENSOR_LANDSCAPE"></span>

[ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation) **SCREEN_SENSOR_LANDSCAPE** = `4`

Automatic landscape orientation (default or reverse depending on sensor).

<span id="class_DisplayServer_constant_SCREEN_SENSOR_PORTRAIT"></span>

[ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation) **SCREEN_SENSOR_PORTRAIT** = `5`

Automatic portrait orientation (default or reverse depending on sensor).

<span id="class_DisplayServer_constant_SCREEN_SENSOR"></span>

[ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation) **SCREEN_SENSOR** = `6`

Automatic landscape or portrait orientation (default or reverse depending on sensor).

---

<span id="enum_DisplayServer_VirtualKeyboardType"></span>

enum **VirtualKeyboardType**: [🔗](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType)

<span id="class_DisplayServer_constant_KEYBOARD_TYPE_DEFAULT"></span>

[VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) **KEYBOARD_TYPE_DEFAULT** = `0`

Default text virtual keyboard.

<span id="class_DisplayServer_constant_KEYBOARD_TYPE_MULTILINE"></span>

[VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) **KEYBOARD_TYPE_MULTILINE** = `1`

Multiline virtual keyboard.

<span id="class_DisplayServer_constant_KEYBOARD_TYPE_NUMBER"></span>

[VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) **KEYBOARD_TYPE_NUMBER** = `2`

Virtual number keypad, useful for PIN entry.

<span id="class_DisplayServer_constant_KEYBOARD_TYPE_NUMBER_DECIMAL"></span>

[VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) **KEYBOARD_TYPE_NUMBER_DECIMAL** = `3`

Virtual number keypad, useful for entering fractional numbers.

<span id="class_DisplayServer_constant_KEYBOARD_TYPE_PHONE"></span>

[VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) **KEYBOARD_TYPE_PHONE** = `4`

Virtual phone number keypad.

<span id="class_DisplayServer_constant_KEYBOARD_TYPE_EMAIL_ADDRESS"></span>

[VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) **KEYBOARD_TYPE_EMAIL_ADDRESS** = `5`

Virtual keyboard with additional keys to assist with typing email addresses.

<span id="class_DisplayServer_constant_KEYBOARD_TYPE_PASSWORD"></span>

[VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) **KEYBOARD_TYPE_PASSWORD** = `6`

Virtual keyboard for entering a password. On most platforms, this should disable autocomplete and autocapitalization.

 **Note:** This is not supported on Web. Instead, this behaves identically to [KEYBOARD_TYPE_DEFAULT](class_displayserver.md#class_DisplayServer_constant_KEYBOARD_TYPE_DEFAULT).

<span id="class_DisplayServer_constant_KEYBOARD_TYPE_URL"></span>

[VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) **KEYBOARD_TYPE_URL** = `7`

Virtual keyboard with additional keys to assist with typing URLs.

---

<span id="enum_DisplayServer_CursorShape"></span>

enum **CursorShape**: [🔗](class_displayserver.md#enum_DisplayServer_CursorShape)

<span id="class_DisplayServer_constant_CURSOR_ARROW"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_ARROW** = `0`

Arrow cursor shape. This is the default when not pointing anything that overrides the mouse cursor, such as a [LineEdit](class_lineedit.md#class_LineEdit) or [TextEdit](class_textedit.md#class_TextEdit).

<span id="class_DisplayServer_constant_CURSOR_IBEAM"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_IBEAM** = `1`

I-beam cursor shape. This is used by default when hovering a control that accepts text input, such as [LineEdit](class_lineedit.md#class_LineEdit) or [TextEdit](class_textedit.md#class_TextEdit).

<span id="class_DisplayServer_constant_CURSOR_POINTING_HAND"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_POINTING_HAND** = `2`

Pointing hand cursor shape. This is used by default when hovering a [LinkButton](class_linkbutton.md#class_LinkButton) or a URL tag in a [RichTextLabel](class_richtextlabel.md#class_RichTextLabel).

<span id="class_DisplayServer_constant_CURSOR_CROSS"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_CROSS** = `3`

Crosshair cursor. This is intended to be displayed when the user needs precise aim over an element, such as a rectangle selection tool or a color picker.

<span id="class_DisplayServer_constant_CURSOR_WAIT"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_WAIT** = `4`

Wait cursor. On most cursor themes, this displays a spinning icon *besides* the arrow. Intended to be used for non-blocking operations (when the user can do something else at the moment). See also [CURSOR_BUSY](class_displayserver.md#class_DisplayServer_constant_CURSOR_BUSY).

<span id="class_DisplayServer_constant_CURSOR_BUSY"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_BUSY** = `5`

Wait cursor. On most cursor themes, this *replaces* the arrow with a spinning icon. Intended to be used for blocking operations (when the user can't do anything else at the moment). See also [CURSOR_WAIT](class_displayserver.md#class_DisplayServer_constant_CURSOR_WAIT).

<span id="class_DisplayServer_constant_CURSOR_DRAG"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_DRAG** = `6`

Dragging hand cursor. This is displayed during drag-and-drop operations. See also [CURSOR_CAN_DROP](class_displayserver.md#class_DisplayServer_constant_CURSOR_CAN_DROP).

<span id="class_DisplayServer_constant_CURSOR_CAN_DROP"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_CAN_DROP** = `7`

"Can drop" cursor. This is displayed during drag-and-drop operations if hovering over a [Control](class_control.md#class_Control) that can accept the drag-and-drop event. On most cursor themes, this displays a dragging hand with an arrow symbol besides it. See also [CURSOR_DRAG](class_displayserver.md#class_DisplayServer_constant_CURSOR_DRAG).

<span id="class_DisplayServer_constant_CURSOR_FORBIDDEN"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_FORBIDDEN** = `8`

Forbidden cursor. This is displayed during drag-and-drop operations if the hovered [Control](class_control.md#class_Control) can't accept the drag-and-drop event.

<span id="class_DisplayServer_constant_CURSOR_VSIZE"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_VSIZE** = `9`

Vertical resize cursor. Intended to be displayed when the hovered [Control](class_control.md#class_Control) can be vertically resized using the mouse. See also [CURSOR_VSPLIT](class_displayserver.md#class_DisplayServer_constant_CURSOR_VSPLIT).

<span id="class_DisplayServer_constant_CURSOR_HSIZE"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_HSIZE** = `10`

Horizontal resize cursor. Intended to be displayed when the hovered [Control](class_control.md#class_Control) can be horizontally resized using the mouse. See also [CURSOR_HSPLIT](class_displayserver.md#class_DisplayServer_constant_CURSOR_HSPLIT).

<span id="class_DisplayServer_constant_CURSOR_BDIAGSIZE"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_BDIAGSIZE** = `11`

Secondary diagonal resize cursor (top-right/bottom-left). Intended to be displayed when the hovered [Control](class_control.md#class_Control) can be resized on both axes at once using the mouse.

<span id="class_DisplayServer_constant_CURSOR_FDIAGSIZE"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_FDIAGSIZE** = `12`

Main diagonal resize cursor (top-left/bottom-right). Intended to be displayed when the hovered [Control](class_control.md#class_Control) can be resized on both axes at once using the mouse.

<span id="class_DisplayServer_constant_CURSOR_MOVE"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_MOVE** = `13`

Move cursor. Intended to be displayed when the hovered [Control](class_control.md#class_Control) can be moved using the mouse.

<span id="class_DisplayServer_constant_CURSOR_VSPLIT"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_VSPLIT** = `14`

Vertical split cursor. This is displayed when hovering a [Control](class_control.md#class_Control) with splits that can be vertically resized using the mouse, such as [VSplitContainer](class_vsplitcontainer.md#class_VSplitContainer). On some cursor themes, this cursor may have the same appearance as [CURSOR_VSIZE](class_displayserver.md#class_DisplayServer_constant_CURSOR_VSIZE).

<span id="class_DisplayServer_constant_CURSOR_HSPLIT"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_HSPLIT** = `15`

Horizontal split cursor. This is displayed when hovering a [Control](class_control.md#class_Control) with splits that can be horizontally resized using the mouse, such as [HSplitContainer](class_hsplitcontainer.md#class_HSplitContainer). On some cursor themes, this cursor may have the same appearance as [CURSOR_HSIZE](class_displayserver.md#class_DisplayServer_constant_CURSOR_HSIZE).

<span id="class_DisplayServer_constant_CURSOR_HELP"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_HELP** = `16`

Help cursor. On most cursor themes, this displays a question mark icon instead of the mouse cursor. Intended to be used when the user has requested help on the next element that will be clicked.

<span id="class_DisplayServer_constant_CURSOR_MAX"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **CURSOR_MAX** = `17`

Represents the size of the [CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) enum.

---

<span id="enum_DisplayServer_FileDialogMode"></span>

enum **FileDialogMode**: [🔗](class_displayserver.md#enum_DisplayServer_FileDialogMode)

<span id="class_DisplayServer_constant_FILE_DIALOG_MODE_OPEN_FILE"></span>

[FileDialogMode](class_displayserver.md#enum_DisplayServer_FileDialogMode) **FILE_DIALOG_MODE_OPEN_FILE** = `0`

The native file dialog allows selecting one, and only one file.

<span id="class_DisplayServer_constant_FILE_DIALOG_MODE_OPEN_FILES"></span>

[FileDialogMode](class_displayserver.md#enum_DisplayServer_FileDialogMode) **FILE_DIALOG_MODE_OPEN_FILES** = `1`

The native file dialog allows selecting multiple files.

<span id="class_DisplayServer_constant_FILE_DIALOG_MODE_OPEN_DIR"></span>

[FileDialogMode](class_displayserver.md#enum_DisplayServer_FileDialogMode) **FILE_DIALOG_MODE_OPEN_DIR** = `2`

The native file dialog only allows selecting a directory, disallowing the selection of any file.

<span id="class_DisplayServer_constant_FILE_DIALOG_MODE_OPEN_ANY"></span>

[FileDialogMode](class_displayserver.md#enum_DisplayServer_FileDialogMode) **FILE_DIALOG_MODE_OPEN_ANY** = `3`

The native file dialog allows selecting one file or directory.

<span id="class_DisplayServer_constant_FILE_DIALOG_MODE_SAVE_FILE"></span>

[FileDialogMode](class_displayserver.md#enum_DisplayServer_FileDialogMode) **FILE_DIALOG_MODE_SAVE_FILE** = `4`

The native file dialog will warn when a file exists.

---

<span id="enum_DisplayServer_WindowMode"></span>

enum **WindowMode**: [🔗](class_displayserver.md#enum_DisplayServer_WindowMode)

<span id="class_DisplayServer_constant_WINDOW_MODE_WINDOWED"></span>

[WindowMode](class_displayserver.md#enum_DisplayServer_WindowMode) **WINDOW_MODE_WINDOWED** = `0`

Windowed mode, i.e. [Window](class_window.md#class_Window) doesn't occupy the whole screen (unless set to the size of the screen).

<span id="class_DisplayServer_constant_WINDOW_MODE_MINIMIZED"></span>

[WindowMode](class_displayserver.md#enum_DisplayServer_WindowMode) **WINDOW_MODE_MINIMIZED** = `1`

Minimized window mode, i.e. [Window](class_window.md#class_Window) is not visible and available on window manager's window list. Normally happens when the minimize button is pressed.

<span id="class_DisplayServer_constant_WINDOW_MODE_MAXIMIZED"></span>

[WindowMode](class_displayserver.md#enum_DisplayServer_WindowMode) **WINDOW_MODE_MAXIMIZED** = `2`

Maximized window mode, i.e. [Window](class_window.md#class_Window) will occupy whole screen area except task bar and still display its borders. Normally happens when the maximize button is pressed.

<span id="class_DisplayServer_constant_WINDOW_MODE_FULLSCREEN"></span>

[WindowMode](class_displayserver.md#enum_DisplayServer_WindowMode) **WINDOW_MODE_FULLSCREEN** = `3`

Full screen mode with full multi-window support.

Full screen window covers the entire display area of a screen and has no decorations. The display's video mode is not changed.

 **On Android:** This enables immersive mode.

 **On macOS:** A new desktop is used to display the running project.

 **Note:** Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supports [multiple resolutions](../tutorials/rendering/multiple_resolutions.md) when enabling full screen mode.

<span id="class_DisplayServer_constant_WINDOW_MODE_EXCLUSIVE_FULLSCREEN"></span>

[WindowMode](class_displayserver.md#enum_DisplayServer_WindowMode) **WINDOW_MODE_EXCLUSIVE_FULLSCREEN** = `4`

A single window full screen mode. This mode has less overhead, but only one window can be open on a given screen at a time (opening a child window or application switching will trigger a full screen transition).

Full screen window covers the entire display area of a screen and has no border or decorations. The display's video mode is not changed.

 **Note:** This mode might not work with screen recording software.

 **On Android:** This enables immersive mode.

 **On Windows:** Depending on video driver, full screen transition might cause screens to go black for a moment.

 **On macOS:** A new desktop is used to display the running project. Exclusive full screen mode prevents Dock and Menu from showing up when the mouse pointer is hovering the edge of the screen.

 **On Linux (X11):** Exclusive full screen mode bypasses compositor.

 **On Linux (Wayland):** Equivalent to [WINDOW_MODE_FULLSCREEN](class_displayserver.md#class_DisplayServer_constant_WINDOW_MODE_FULLSCREEN).

 **Note:** Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supports [multiple resolutions](../tutorials/rendering/multiple_resolutions.md) when enabling full screen mode.

---

<span id="enum_DisplayServer_WindowFlags"></span>

enum **WindowFlags**: [🔗](class_displayserver.md#enum_DisplayServer_WindowFlags)

<span id="class_DisplayServer_constant_WINDOW_FLAG_RESIZE_DISABLED"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_RESIZE_DISABLED** = `0`

The window can't be resized by dragging its resize grip. It's still possible to resize the window using [window_set_size()](class_displayserver.md#class_DisplayServer_method_window_set_size). This flag is ignored for full screen windows.

<span id="class_DisplayServer_constant_WINDOW_FLAG_BORDERLESS"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_BORDERLESS** = `1`

The window do not have native title bar and other decorations. This flag is ignored for full-screen windows.

<span id="class_DisplayServer_constant_WINDOW_FLAG_ALWAYS_ON_TOP"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_ALWAYS_ON_TOP** = `2`

The window is floating on top of all other windows. This flag is ignored for full-screen windows.

<span id="class_DisplayServer_constant_WINDOW_FLAG_TRANSPARENT"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_TRANSPARENT** = `3`

The window background can be transparent.

 **Note:** This flag has no effect if [is_window_transparency_available()](class_displayserver.md#class_DisplayServer_method_is_window_transparency_available) returns `false`.

 **Note:** Transparency support is implemented on Linux (X11/Wayland), macOS, and Windows, but availability might vary depending on GPU driver, display manager, and compositor capabilities.

 **Note:** Transparency support is implemented on Android, but can only be enabled via ProjectSettings.display/window/per_pixel_transparency/allowed. This flag has no effect on Android.

<span id="class_DisplayServer_constant_WINDOW_FLAG_NO_FOCUS"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_NO_FOCUS** = `4`

The window can't be focused. No-focus window will ignore all input, except mouse clicks.

<span id="class_DisplayServer_constant_WINDOW_FLAG_POPUP"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_POPUP** = `5`

Window is part of menu or [OptionButton](class_optionbutton.md#class_OptionButton) dropdown. This flag can't be changed when the window is visible. An active popup window will exclusively receive all input, without stealing focus from its parent. Popup windows are automatically closed when uses click outside it, or when an application is switched. Popup window must have transient parent set (see [window_set_transient()](class_displayserver.md#class_DisplayServer_method_window_set_transient)).

<span id="class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_EXTEND_TO_TITLE** = `6`

Window content is expanded to the full size of the window. Unlike borderless window, the frame is left intact and can be used to resize the window, title bar is transparent, but have minimize/maximize/close buttons.

Use [window_set_window_buttons_offset()](class_displayserver.md#class_DisplayServer_method_window_set_window_buttons_offset) to adjust minimize/maximize/close buttons offset.

Use [window_get_safe_title_margins()](class_displayserver.md#class_DisplayServer_method_window_get_safe_title_margins) to determine area under the title bar that is not covered by decorations.

 **Note:** This flag is implemented only on macOS.

<span id="class_DisplayServer_constant_WINDOW_FLAG_MOUSE_PASSTHROUGH"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_MOUSE_PASSTHROUGH** = `7`

All mouse events are passed to the underlying window of the same application.

<span id="class_DisplayServer_constant_WINDOW_FLAG_SHARP_CORNERS"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_SHARP_CORNERS** = `8`

Window style is overridden, forcing sharp corners.

 **Note:** This flag is implemented only on Windows (11).

<span id="class_DisplayServer_constant_WINDOW_FLAG_EXCLUDE_FROM_CAPTURE"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_EXCLUDE_FROM_CAPTURE** = `9`

Window is excluded from screenshots taken by [screen_get_image()](class_displayserver.md#class_DisplayServer_method_screen_get_image), [screen_get_image_rect()](class_displayserver.md#class_DisplayServer_method_screen_get_image_rect), and [screen_get_pixel()](class_displayserver.md#class_DisplayServer_method_screen_get_pixel).

 **Note:** This flag is implemented on macOS and Windows (10, 20H1).

 **Note:** Setting this flag will prevent standard screenshot methods from capturing a window image, but does **NOT** guarantee that other apps won't be able to capture an image. It should not be used as a DRM or security measure.

<span id="class_DisplayServer_constant_WINDOW_FLAG_POPUP_WM_HINT"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_POPUP_WM_HINT** = `10`

Signals the window manager that this window is supposed to be an implementation-defined "popup" (usually a floating, borderless, untileable and immovable child window).

<span id="class_DisplayServer_constant_WINDOW_FLAG_MINIMIZE_DISABLED"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_MINIMIZE_DISABLED** = `11`

Window minimize button is disabled.

 **Note:** This flag is implemented on macOS and Windows.

<span id="class_DisplayServer_constant_WINDOW_FLAG_MAXIMIZE_DISABLED"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_MAXIMIZE_DISABLED** = `12`

Window maximize button is disabled.

 **Note:** This flag is implemented on macOS and Windows.

<span id="class_DisplayServer_constant_WINDOW_FLAG_MAX"></span>

[WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) **WINDOW_FLAG_MAX** = `13`

Represents the size of the [WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags) enum.

---

<span id="enum_DisplayServer_WindowEvent"></span>

enum **WindowEvent**: [🔗](class_displayserver.md#enum_DisplayServer_WindowEvent)

<span id="class_DisplayServer_constant_WINDOW_EVENT_MOUSE_ENTER"></span>

[WindowEvent](class_displayserver.md#enum_DisplayServer_WindowEvent) **WINDOW_EVENT_MOUSE_ENTER** = `0`

Sent when the mouse pointer enters the window.

<span id="class_DisplayServer_constant_WINDOW_EVENT_MOUSE_EXIT"></span>

[WindowEvent](class_displayserver.md#enum_DisplayServer_WindowEvent) **WINDOW_EVENT_MOUSE_EXIT** = `1`

Sent when the mouse pointer exits the window.

<span id="class_DisplayServer_constant_WINDOW_EVENT_FOCUS_IN"></span>

[WindowEvent](class_displayserver.md#enum_DisplayServer_WindowEvent) **WINDOW_EVENT_FOCUS_IN** = `2`

Sent when the window grabs focus.

<span id="class_DisplayServer_constant_WINDOW_EVENT_FOCUS_OUT"></span>

[WindowEvent](class_displayserver.md#enum_DisplayServer_WindowEvent) **WINDOW_EVENT_FOCUS_OUT** = `3`

Sent when the window loses focus.

<span id="class_DisplayServer_constant_WINDOW_EVENT_CLOSE_REQUEST"></span>

[WindowEvent](class_displayserver.md#enum_DisplayServer_WindowEvent) **WINDOW_EVENT_CLOSE_REQUEST** = `4`

Sent when the user has attempted to close the window (e.g. close button is pressed).

<span id="class_DisplayServer_constant_WINDOW_EVENT_GO_BACK_REQUEST"></span>

[WindowEvent](class_displayserver.md#enum_DisplayServer_WindowEvent) **WINDOW_EVENT_GO_BACK_REQUEST** = `5`

Sent when the device "Back" button is pressed.

 **Note:** This event is implemented only on Android.

<span id="class_DisplayServer_constant_WINDOW_EVENT_DPI_CHANGE"></span>

[WindowEvent](class_displayserver.md#enum_DisplayServer_WindowEvent) **WINDOW_EVENT_DPI_CHANGE** = `6`

Sent when the window is moved to the display with different DPI, or display DPI is changed.

 **Note:** This flag is implemented only on macOS and Linux (Wayland).

<span id="class_DisplayServer_constant_WINDOW_EVENT_TITLEBAR_CHANGE"></span>

[WindowEvent](class_displayserver.md#enum_DisplayServer_WindowEvent) **WINDOW_EVENT_TITLEBAR_CHANGE** = `7`

Sent when the window title bar decoration is changed (e.g. [WINDOW_FLAG_EXTEND_TO_TITLE](class_displayserver.md#class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE) is set or window entered/exited full screen mode).

 **Note:** This flag is implemented only on macOS.

<span id="class_DisplayServer_constant_WINDOW_EVENT_FORCE_CLOSE"></span>

[WindowEvent](class_displayserver.md#enum_DisplayServer_WindowEvent) **WINDOW_EVENT_FORCE_CLOSE** = `8`

Sent when the window has been forcibly closed by the display server. The window will immediately hide and clean any internal rendering references.

 **Note:** This flag is implemented only on Linux (Wayland).

---

<span id="enum_DisplayServer_WindowResizeEdge"></span>

enum **WindowResizeEdge**: [🔗](class_displayserver.md#enum_DisplayServer_WindowResizeEdge)

<span id="class_DisplayServer_constant_WINDOW_EDGE_TOP_LEFT"></span>

[WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) **WINDOW_EDGE_TOP_LEFT** = `0`

Top-left edge of a window.

<span id="class_DisplayServer_constant_WINDOW_EDGE_TOP"></span>

[WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) **WINDOW_EDGE_TOP** = `1`

Top edge of a window.

<span id="class_DisplayServer_constant_WINDOW_EDGE_TOP_RIGHT"></span>

[WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) **WINDOW_EDGE_TOP_RIGHT** = `2`

Top-right edge of a window.

<span id="class_DisplayServer_constant_WINDOW_EDGE_LEFT"></span>

[WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) **WINDOW_EDGE_LEFT** = `3`

Left edge of a window.

<span id="class_DisplayServer_constant_WINDOW_EDGE_RIGHT"></span>

[WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) **WINDOW_EDGE_RIGHT** = `4`

Right edge of a window.

<span id="class_DisplayServer_constant_WINDOW_EDGE_BOTTOM_LEFT"></span>

[WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) **WINDOW_EDGE_BOTTOM_LEFT** = `5`

Bottom-left edge of a window.

<span id="class_DisplayServer_constant_WINDOW_EDGE_BOTTOM"></span>

[WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) **WINDOW_EDGE_BOTTOM** = `6`

Bottom edge of a window.

<span id="class_DisplayServer_constant_WINDOW_EDGE_BOTTOM_RIGHT"></span>

[WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) **WINDOW_EDGE_BOTTOM_RIGHT** = `7`

Bottom-right edge of a window.

<span id="class_DisplayServer_constant_WINDOW_EDGE_MAX"></span>

[WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) **WINDOW_EDGE_MAX** = `8`

Represents the size of the [WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) enum.

---

<span id="enum_DisplayServer_VSyncMode"></span>

enum **VSyncMode**: [🔗](class_displayserver.md#enum_DisplayServer_VSyncMode)

<span id="class_DisplayServer_constant_VSYNC_DISABLED"></span>

[VSyncMode](class_displayserver.md#enum_DisplayServer_VSyncMode) **VSYNC_DISABLED** = `0`

No vertical synchronization, which means the engine will display frames as fast as possible (tearing may be visible). Framerate is unlimited (regardless of [Engine.max_fps](class_engine.md#class_Engine_property_max_fps)).

<span id="class_DisplayServer_constant_VSYNC_ENABLED"></span>

[VSyncMode](class_displayserver.md#enum_DisplayServer_VSyncMode) **VSYNC_ENABLED** = `1`

Default vertical synchronization mode, the image is displayed only on vertical blanking intervals (no tearing is visible). Framerate is limited by the monitor refresh rate (regardless of [Engine.max_fps](class_engine.md#class_Engine_property_max_fps)).

<span id="class_DisplayServer_constant_VSYNC_ADAPTIVE"></span>

[VSyncMode](class_displayserver.md#enum_DisplayServer_VSyncMode) **VSYNC_ADAPTIVE** = `2`

Behaves like [VSYNC_DISABLED](class_displayserver.md#class_DisplayServer_constant_VSYNC_DISABLED) when the framerate drops below the screen's refresh rate to reduce stuttering (tearing may be visible). Otherwise, vertical synchronization is enabled to avoid tearing. Framerate is limited by the monitor refresh rate (regardless of [Engine.max_fps](class_engine.md#class_Engine_property_max_fps)). Behaves like [VSYNC_ENABLED](class_displayserver.md#class_DisplayServer_constant_VSYNC_ENABLED) when using the Compatibility rendering method.

<span id="class_DisplayServer_constant_VSYNC_MAILBOX"></span>

[VSyncMode](class_displayserver.md#enum_DisplayServer_VSyncMode) **VSYNC_MAILBOX** = `3`

Displays the most recent image in the queue on vertical blanking intervals, while rendering to the other images (no tearing is visible). Framerate is unlimited (regardless of [Engine.max_fps](class_engine.md#class_Engine_property_max_fps)).

Although not guaranteed, the images can be rendered as fast as possible, which may reduce input lag (also called "Fast" V-Sync mode). [VSYNC_MAILBOX](class_displayserver.md#class_DisplayServer_constant_VSYNC_MAILBOX) works best when at least twice as many frames as the display refresh rate are rendered. Behaves like [VSYNC_ENABLED](class_displayserver.md#class_DisplayServer_constant_VSYNC_ENABLED) when using the Compatibility rendering method.

---

<span id="enum_DisplayServer_HandleType"></span>

enum **HandleType**: [🔗](class_displayserver.md#enum_DisplayServer_HandleType)

<span id="class_DisplayServer_constant_DISPLAY_HANDLE"></span>

[HandleType](class_displayserver.md#enum_DisplayServer_HandleType) **DISPLAY_HANDLE** = `0`

Display handle:

- Linux (X11): `X11::Display*` for the display.

- Linux (Wayland): `wl_display` for the display.

- Android: `EGLDisplay` for the display.

<span id="class_DisplayServer_constant_WINDOW_HANDLE"></span>

[HandleType](class_displayserver.md#enum_DisplayServer_HandleType) **WINDOW_HANDLE** = `1`

Window handle:

- Windows: `HWND` for the window.

- Linux (X11): `X11::Window*` for the window.

- Linux (Wayland): `wl_surface` for the window.

- macOS: `NSWindow*` for the window.

- iOS: `UIViewController*` for the view controller.

- Android: `jObject` for the activity.

<span id="class_DisplayServer_constant_WINDOW_VIEW"></span>

[HandleType](class_displayserver.md#enum_DisplayServer_HandleType) **WINDOW_VIEW** = `2`

Window view:

- Windows: `HDC` for the window (only with the Compatibility renderer).

- macOS: `NSView*` for the window main view.

- iOS: `UIView*` for the window main view.

<span id="class_DisplayServer_constant_OPENGL_CONTEXT"></span>

[HandleType](class_displayserver.md#enum_DisplayServer_HandleType) **OPENGL_CONTEXT** = `3`

OpenGL context (only with the Compatibility renderer):

- Windows: `HGLRC` for the window (native GL), or `EGLContext` for the window (ANGLE).

- Linux (X11): `GLXContext*` for the window.

- Linux (Wayland): `EGLContext` for the window.

- macOS: `NSOpenGLContext*` for the window (native GL), or `EGLContext` for the window (ANGLE).

- Android: `EGLContext` for the window.

<span id="class_DisplayServer_constant_EGL_DISPLAY"></span>

[HandleType](class_displayserver.md#enum_DisplayServer_HandleType) **EGL_DISPLAY** = `4`

- Windows: `EGLDisplay` for the window (ANGLE).

- macOS: `EGLDisplay` for the window (ANGLE).

- Linux (Wayland): `EGLDisplay` for the window.

<span id="class_DisplayServer_constant_EGL_CONFIG"></span>

[HandleType](class_displayserver.md#enum_DisplayServer_HandleType) **EGL_CONFIG** = `5`

- Windows: `EGLConfig` for the window (ANGLE).

- macOS: `EGLConfig` for the window (ANGLE).

- Linux (Wayland): `EGLConfig` for the window.

---

<span id="enum_DisplayServer_TTSUtteranceEvent"></span>

enum **TTSUtteranceEvent**: [🔗](class_displayserver.md#enum_DisplayServer_TTSUtteranceEvent)

<span id="class_DisplayServer_constant_TTS_UTTERANCE_STARTED"></span>

[TTSUtteranceEvent](class_displayserver.md#enum_DisplayServer_TTSUtteranceEvent) **TTS_UTTERANCE_STARTED** = `0`

Utterance has begun to be spoken.

<span id="class_DisplayServer_constant_TTS_UTTERANCE_ENDED"></span>

[TTSUtteranceEvent](class_displayserver.md#enum_DisplayServer_TTSUtteranceEvent) **TTS_UTTERANCE_ENDED** = `1`

Utterance was successfully finished.

<span id="class_DisplayServer_constant_TTS_UTTERANCE_CANCELED"></span>

[TTSUtteranceEvent](class_displayserver.md#enum_DisplayServer_TTSUtteranceEvent) **TTS_UTTERANCE_CANCELED** = `2`

Utterance was canceled, or TTS service was unable to process it.

<span id="class_DisplayServer_constant_TTS_UTTERANCE_BOUNDARY"></span>

[TTSUtteranceEvent](class_displayserver.md#enum_DisplayServer_TTSUtteranceEvent) **TTS_UTTERANCE_BOUNDARY** = `3`

Utterance reached a word or sentence boundary.

---

### Constants

<span id="class_DisplayServer_constant_INVALID_SCREEN"></span>

**INVALID_SCREEN** = `-1` [🔗](class_displayserver.md#class_DisplayServer_constant_INVALID_SCREEN)

The ID that refers to a screen that does not exist. This is returned by some **DisplayServer** methods if no screen matches the requested result.

<span id="class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS"></span>

**SCREEN_WITH_MOUSE_FOCUS** = `-4` [🔗](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS)

Represents the screen containing the mouse pointer.

 **Note:** On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index `0`.

<span id="class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS"></span>

**SCREEN_WITH_KEYBOARD_FOCUS** = `-3` [🔗](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS)

Represents the screen containing the window with the keyboard focus.

 **Note:** On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index `0`.

<span id="class_DisplayServer_constant_SCREEN_PRIMARY"></span>

**SCREEN_PRIMARY** = `-2` [🔗](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY)

Represents the primary screen.

 **Note:** On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index `0`.

<span id="class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW"></span>

**SCREEN_OF_MAIN_WINDOW** = `-1` [🔗](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW)

Represents the screen where the main window is located. This is usually the default value in functions that allow specifying one of several screens.

 **Note:** On Android, iOS, Web, and Linux (Wayland), this constant always represents the screen at index `0`.

<span id="class_DisplayServer_constant_MAIN_WINDOW_ID"></span>

**MAIN_WINDOW_ID** = `0` [🔗](class_displayserver.md#class_DisplayServer_constant_MAIN_WINDOW_ID)

The ID of the main window spawned by the engine, which can be passed to methods expecting a `window_id`.

<span id="class_DisplayServer_constant_INVALID_WINDOW_ID"></span>

**INVALID_WINDOW_ID** = `-1` [🔗](class_displayserver.md#class_DisplayServer_constant_INVALID_WINDOW_ID)

The ID that refers to a nonexistent window. This is returned by some **DisplayServer** methods if no window matches the requested result.

<span id="class_DisplayServer_constant_INVALID_INDICATOR_ID"></span>

**INVALID_INDICATOR_ID** = `-1` [🔗](class_displayserver.md#class_DisplayServer_constant_INVALID_INDICATOR_ID)

The ID that refers to a nonexistent application status indicator.

---

### Method Descriptions

<span id="class_DisplayServer_method_accessibility_create_element"></span>

[RID](class_rid.md#class_RID) **accessibility_create_element** ( window_id: [int](class_int.md#class_int), role: [AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_create_element)

Creates a new, empty accessibility element resource.

 **Note:** An accessibility element is created and freed automatically for each [Node](class_node.md#class_Node). In general, this function should not be called manually.

---

<span id="class_DisplayServer_method_accessibility_create_sub_element"></span>

[RID](class_rid.md#class_RID) **accessibility_create_sub_element** ( parent_rid: [RID](class_rid.md#class_RID), role: [AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole), insert_pos: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_create_sub_element)

Creates a new, empty accessibility sub-element resource. Sub-elements can be used to provide accessibility information for objects which are not [Node](class_node.md#class_Node) s, such as list items, table cells, or menu items. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the [accessibility_free_element()](class_displayserver.md#class_DisplayServer_method_accessibility_free_element) method.

---

<span id="class_DisplayServer_method_accessibility_create_sub_text_edit_elements"></span>

[RID](class_rid.md#class_RID) **accessibility_create_sub_text_edit_elements** ( parent_rid: [RID](class_rid.md#class_RID), shaped_text: [RID](class_rid.md#class_RID), min_height: [float](class_float.md#class_float), insert_pos: [int](class_int.md#class_int) = -1, is_last_line: [bool](class_bool.md#class_bool) = false ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_create_sub_text_edit_elements)

Creates a new, empty accessibility sub-element from the shaped text buffer. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the [accessibility_free_element()](class_displayserver.md#class_DisplayServer_method_accessibility_free_element) method.

If `is_last_line` is `true`, no trailing newline is appended to the text content. Set to `true` for the last line in multi-line text fields and for single-line text fields.

---

<span id="class_DisplayServer_method_accessibility_element_get_meta"></span>

[Variant](class_variant.md#class_Variant) **accessibility_element_get_meta** ( id: [RID](class_rid.md#class_RID) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_element_get_meta)

Returns the metadata of the accessibility element `id`.

---

<span id="class_DisplayServer_method_accessibility_element_set_meta"></span>

void **accessibility_element_set_meta** ( id: [RID](class_rid.md#class_RID), meta: [Variant](class_variant.md#class_Variant) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_element_set_meta)

Sets the metadata of the accessibility element `id` to `meta`.

---

<span id="class_DisplayServer_method_accessibility_free_element"></span>

void **accessibility_free_element** ( id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_free_element)

Frees the accessibility element `id` created by [accessibility_create_element()](class_displayserver.md#class_DisplayServer_method_accessibility_create_element), [accessibility_create_sub_element()](class_displayserver.md#class_DisplayServer_method_accessibility_create_sub_element), or [accessibility_create_sub_text_edit_elements()](class_displayserver.md#class_DisplayServer_method_accessibility_create_sub_text_edit_elements).

---

<span id="class_DisplayServer_method_accessibility_get_window_root"></span>

[RID](class_rid.md#class_RID) **accessibility_get_window_root** ( window_id: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_get_window_root)

Returns the main accessibility element of the OS native window.

---

<span id="class_DisplayServer_method_accessibility_has_element"></span>

[bool](class_bool.md#class_bool) **accessibility_has_element** ( id: [RID](class_rid.md#class_RID) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_has_element)

Returns `true` if `id` is a valid accessibility element.

---

<span id="class_DisplayServer_method_accessibility_screen_reader_active"></span>

[int](class_int.md#class_int) **accessibility_screen_reader_active** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_screen_reader_active)

Returns `1` if a screen reader, Braille display or other assistive app is active, `0` otherwise. Returns `-1` if status is unknown.

 **Note:** This method is implemented on Linux, macOS, and Windows.

 **Note:** Accessibility debugging tools, such as Accessibility Insights for Windows, Accessibility Inspector (macOS), or AT-SPI Browser (Linux/BSD), do not count as assistive apps and will not affect this value. To test your project with these tools, set ProjectSettings.accessibility/general/accessibility_support to `1`.

---

<span id="class_DisplayServer_method_accessibility_set_window_focused"></span>

void **accessibility_set_window_focused** ( window_id: [int](class_int.md#class_int), focused: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_set_window_focused)

Sets the window focused state for assistive apps.

 **Note:** This method is implemented on Linux, macOS, and Windows.

 **Note:** Advanced users only! [Window](class_window.md#class_Window) objects call this method automatically.

---

<span id="class_DisplayServer_method_accessibility_set_window_rect"></span>

void **accessibility_set_window_rect** ( window_id: [int](class_int.md#class_int), rect_out: [Rect2](class_rect2.md#class_Rect2), rect_in: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_set_window_rect)

Sets window outer (with decorations) and inner (without decorations) bounds for assistive apps.

 **Note:** This method is implemented on Linux, macOS, and Windows.

 **Note:** Advanced users only! [Window](class_window.md#class_Window) objects call this method automatically.

---

<span id="class_DisplayServer_method_accessibility_should_increase_contrast"></span>

[int](class_int.md#class_int) **accessibility_should_increase_contrast** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_should_increase_contrast)

Returns `1` if a high-contrast user interface theme should be used, `0` otherwise. Returns `-1` if status is unknown.

 **Note:** This method is implemented on Linux (X11/Wayland, GNOME), macOS, and Windows.

---

<span id="class_DisplayServer_method_accessibility_should_reduce_animation"></span>

[int](class_int.md#class_int) **accessibility_should_reduce_animation** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_should_reduce_animation)

Returns `1` if flashing, blinking, and other moving content that can cause seizures in users with photosensitive epilepsy should be disabled, `0` otherwise. Returns `-1` if status is unknown.

 **Note:** This method is implemented on macOS and Windows.

---

<span id="class_DisplayServer_method_accessibility_should_reduce_transparency"></span>

[int](class_int.md#class_int) **accessibility_should_reduce_transparency** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_should_reduce_transparency)

Returns `1` if background images, transparency, and other features that can reduce the contrast between the foreground and background should be disabled, `0` otherwise. Returns `-1` if status is unknown.

 **Note:** This method is implemented on macOS and Windows.

---

<span id="class_DisplayServer_method_accessibility_update_add_action"></span>

void **accessibility_update_add_action** ( id: [RID](class_rid.md#class_RID), action: [AccessibilityAction](class_displayserver.md#enum_DisplayServer_AccessibilityAction), callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_action)

Adds a callback for the accessibility action (action which can be performed by using a special screen reader command or buttons on the Braille display), and marks this action as supported. The action callback receives one [Variant](class_variant.md#class_Variant) argument, which value depends on action type.

---

<span id="class_DisplayServer_method_accessibility_update_add_child"></span>

void **accessibility_update_add_child** ( id: [RID](class_rid.md#class_RID), child_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_child)

Adds a child accessibility element.

 **Note:** [Node](class_node.md#class_Node) children and sub-elements are added to the child list automatically.

---

<span id="class_DisplayServer_method_accessibility_update_add_custom_action"></span>

void **accessibility_update_add_custom_action** ( id: [RID](class_rid.md#class_RID), action_id: [int](class_int.md#class_int), action_description: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_custom_action)

Adds support for a custom accessibility action. `action_id` is passed as an argument to the callback of [ACTION_CUSTOM](class_displayserver.md#class_DisplayServer_constant_ACTION_CUSTOM) action.

---

<span id="class_DisplayServer_method_accessibility_update_add_related_controls"></span>

void **accessibility_update_add_related_controls** ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_controls)

Adds an element that is controlled by this element.

---

<span id="class_DisplayServer_method_accessibility_update_add_related_described_by"></span>

void **accessibility_update_add_related_described_by** ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_described_by)

Adds an element that describes this element.

---

<span id="class_DisplayServer_method_accessibility_update_add_related_details"></span>

void **accessibility_update_add_related_details** ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_details)

Adds an element that details this element.

---

<span id="class_DisplayServer_method_accessibility_update_add_related_flow_to"></span>

void **accessibility_update_add_related_flow_to** ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_flow_to)

Adds an element that this element flow into.

---

<span id="class_DisplayServer_method_accessibility_update_add_related_labeled_by"></span>

void **accessibility_update_add_related_labeled_by** ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_labeled_by)

Adds an element that labels this element.

---

<span id="class_DisplayServer_method_accessibility_update_add_related_radio_group"></span>

void **accessibility_update_add_related_radio_group** ( id: [RID](class_rid.md#class_RID), related_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_add_related_radio_group)

Adds an element that is part of the same radio group.

 **Note:** This method should be called on each element of the group, using all other elements as `related_id`.

---

<span id="class_DisplayServer_method_accessibility_update_set_active_descendant"></span>

void **accessibility_update_set_active_descendant** ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_active_descendant)

Adds an element that is an active descendant of this element.

---

<span id="class_DisplayServer_method_accessibility_update_set_background_color"></span>

void **accessibility_update_set_background_color** ( id: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_background_color)

Sets element background color.

---

<span id="class_DisplayServer_method_accessibility_update_set_bounds"></span>

void **accessibility_update_set_bounds** ( id: [RID](class_rid.md#class_RID), p_rect: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_bounds)

Sets element bounding box, relative to the node position.

---

<span id="class_DisplayServer_method_accessibility_update_set_checked"></span>

void **accessibility_update_set_checked** ( id: [RID](class_rid.md#class_RID), checekd: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_checked)

Sets element checked state.

---

<span id="class_DisplayServer_method_accessibility_update_set_classname"></span>

void **accessibility_update_set_classname** ( id: [RID](class_rid.md#class_RID), classname: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_classname)

Sets element class name.

---

<span id="class_DisplayServer_method_accessibility_update_set_color_value"></span>

void **accessibility_update_set_color_value** ( id: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_color_value)

Sets element color value.

---

<span id="class_DisplayServer_method_accessibility_update_set_description"></span>

void **accessibility_update_set_description** ( id: [RID](class_rid.md#class_RID), description: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_description)

Sets element accessibility description.

---

<span id="class_DisplayServer_method_accessibility_update_set_error_message"></span>

void **accessibility_update_set_error_message** ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_error_message)

Sets an element which contains an error message for this element.

---

<span id="class_DisplayServer_method_accessibility_update_set_extra_info"></span>

void **accessibility_update_set_extra_info** ( id: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_extra_info)

Sets element accessibility extra information added to the element name.

---

<span id="class_DisplayServer_method_accessibility_update_set_flag"></span>

void **accessibility_update_set_flag** ( id: [RID](class_rid.md#class_RID), flag: [AccessibilityFlags](class_displayserver.md#enum_DisplayServer_AccessibilityFlags), value: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_flag)

Sets element flag.

---

<span id="class_DisplayServer_method_accessibility_update_set_focus"></span>

void **accessibility_update_set_focus** ( id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_focus)

Sets currently focused element.

---

<span id="class_DisplayServer_method_accessibility_update_set_foreground_color"></span>

void **accessibility_update_set_foreground_color** ( id: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_foreground_color)

Sets element foreground color.

---

<span id="class_DisplayServer_method_accessibility_update_set_in_page_link_target"></span>

void **accessibility_update_set_in_page_link_target** ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_in_page_link_target)

Sets target element for the link.

---

<span id="class_DisplayServer_method_accessibility_update_set_language"></span>

void **accessibility_update_set_language** ( id: [RID](class_rid.md#class_RID), language: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_language)

Sets element text language.

---

<span id="class_DisplayServer_method_accessibility_update_set_list_item_count"></span>

void **accessibility_update_set_list_item_count** ( id: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_count)

Sets number of items in the list.

---

<span id="class_DisplayServer_method_accessibility_update_set_list_item_expanded"></span>

void **accessibility_update_set_list_item_expanded** ( id: [RID](class_rid.md#class_RID), expanded: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_expanded)

Sets list/tree item expanded status.

---

<span id="class_DisplayServer_method_accessibility_update_set_list_item_index"></span>

void **accessibility_update_set_list_item_index** ( id: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_index)

Sets the position of the element in the list.

---

<span id="class_DisplayServer_method_accessibility_update_set_list_item_level"></span>

void **accessibility_update_set_list_item_level** ( id: [RID](class_rid.md#class_RID), level: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_level)

Sets the hierarchical level of the element in the list.

---

<span id="class_DisplayServer_method_accessibility_update_set_list_item_selected"></span>

void **accessibility_update_set_list_item_selected** ( id: [RID](class_rid.md#class_RID), selected: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_item_selected)

Sets list/tree item selected status.

---

<span id="class_DisplayServer_method_accessibility_update_set_list_orientation"></span>

void **accessibility_update_set_list_orientation** ( id: [RID](class_rid.md#class_RID), vertical: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_list_orientation)

Sets the orientation of the list elements.

---

<span id="class_DisplayServer_method_accessibility_update_set_live"></span>

void **accessibility_update_set_live** ( id: [RID](class_rid.md#class_RID), live: [AccessibilityLiveMode](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_live)

Sets the priority of the live region updates.

---

<span id="class_DisplayServer_method_accessibility_update_set_member_of"></span>

void **accessibility_update_set_member_of** ( id: [RID](class_rid.md#class_RID), group_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_member_of)

Sets the element to be a member of the group.

---

<span id="class_DisplayServer_method_accessibility_update_set_name"></span>

void **accessibility_update_set_name** ( id: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_name)

Sets element accessibility name.

---

<span id="class_DisplayServer_method_accessibility_update_set_next_on_line"></span>

void **accessibility_update_set_next_on_line** ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_next_on_line)

Sets next element on the line.

---

<span id="class_DisplayServer_method_accessibility_update_set_num_jump"></span>

void **accessibility_update_set_num_jump** ( id: [RID](class_rid.md#class_RID), jump: [float](class_float.md#class_float) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_num_jump)

Sets numeric value jump.

---

<span id="class_DisplayServer_method_accessibility_update_set_num_range"></span>

void **accessibility_update_set_num_range** ( id: [RID](class_rid.md#class_RID), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_num_range)

Sets numeric value range.

---

<span id="class_DisplayServer_method_accessibility_update_set_num_step"></span>

void **accessibility_update_set_num_step** ( id: [RID](class_rid.md#class_RID), step: [float](class_float.md#class_float) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_num_step)

Sets numeric value step.

---

<span id="class_DisplayServer_method_accessibility_update_set_num_value"></span>

void **accessibility_update_set_num_value** ( id: [RID](class_rid.md#class_RID), position: [float](class_float.md#class_float) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_num_value)

Sets numeric value.

---

<span id="class_DisplayServer_method_accessibility_update_set_placeholder"></span>

void **accessibility_update_set_placeholder** ( id: [RID](class_rid.md#class_RID), placeholder: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_placeholder)

Sets placeholder text.

---

<span id="class_DisplayServer_method_accessibility_update_set_popup_type"></span>

void **accessibility_update_set_popup_type** ( id: [RID](class_rid.md#class_RID), popup: [AccessibilityPopupType](class_displayserver.md#enum_DisplayServer_AccessibilityPopupType) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_popup_type)

Sets popup type for popup buttons.

---

<span id="class_DisplayServer_method_accessibility_update_set_previous_on_line"></span>

void **accessibility_update_set_previous_on_line** ( id: [RID](class_rid.md#class_RID), other_id: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_previous_on_line)

Sets previous element on the line.

---

<span id="class_DisplayServer_method_accessibility_update_set_role"></span>

void **accessibility_update_set_role** ( id: [RID](class_rid.md#class_RID), role: [AccessibilityRole](class_displayserver.md#enum_DisplayServer_AccessibilityRole) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_role)

Sets element accessibility role.

---

<span id="class_DisplayServer_method_accessibility_update_set_role_description"></span>

void **accessibility_update_set_role_description** ( id: [RID](class_rid.md#class_RID), description: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_role_description)

Sets element accessibility role description text.

---

<span id="class_DisplayServer_method_accessibility_update_set_scroll_x"></span>

void **accessibility_update_set_scroll_x** ( id: [RID](class_rid.md#class_RID), position: [float](class_float.md#class_float) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_scroll_x)

Sets scroll bar x position.

---

<span id="class_DisplayServer_method_accessibility_update_set_scroll_x_range"></span>

void **accessibility_update_set_scroll_x_range** ( id: [RID](class_rid.md#class_RID), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_scroll_x_range)

Sets scroll bar x range.

---

<span id="class_DisplayServer_method_accessibility_update_set_scroll_y"></span>

void **accessibility_update_set_scroll_y** ( id: [RID](class_rid.md#class_RID), position: [float](class_float.md#class_float) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_scroll_y)

Sets scroll bar y position.

---

<span id="class_DisplayServer_method_accessibility_update_set_scroll_y_range"></span>

void **accessibility_update_set_scroll_y_range** ( id: [RID](class_rid.md#class_RID), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_scroll_y_range)

Sets scroll bar y range.

---

<span id="class_DisplayServer_method_accessibility_update_set_shortcut"></span>

void **accessibility_update_set_shortcut** ( id: [RID](class_rid.md#class_RID), shortcut: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_shortcut)

Sets the list of keyboard shortcuts used by element.

---

<span id="class_DisplayServer_method_accessibility_update_set_state_description"></span>

void **accessibility_update_set_state_description** ( id: [RID](class_rid.md#class_RID), description: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_state_description)

Sets human-readable description of the current checked state.

---

<span id="class_DisplayServer_method_accessibility_update_set_table_cell_position"></span>

void **accessibility_update_set_table_cell_position** ( id: [RID](class_rid.md#class_RID), row_index: [int](class_int.md#class_int), column_index: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_cell_position)

Sets cell position in the table.

---

<span id="class_DisplayServer_method_accessibility_update_set_table_cell_span"></span>

void **accessibility_update_set_table_cell_span** ( id: [RID](class_rid.md#class_RID), row_span: [int](class_int.md#class_int), column_span: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_cell_span)

Sets cell row/column span.

---

<span id="class_DisplayServer_method_accessibility_update_set_table_column_count"></span>

void **accessibility_update_set_table_column_count** ( id: [RID](class_rid.md#class_RID), count: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_column_count)

Sets number of columns in the table.

---

<span id="class_DisplayServer_method_accessibility_update_set_table_column_index"></span>

void **accessibility_update_set_table_column_index** ( id: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_column_index)

Sets position of the column.

---

<span id="class_DisplayServer_method_accessibility_update_set_table_row_count"></span>

void **accessibility_update_set_table_row_count** ( id: [RID](class_rid.md#class_RID), count: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_row_count)

Sets number of rows in the table.

---

<span id="class_DisplayServer_method_accessibility_update_set_table_row_index"></span>

void **accessibility_update_set_table_row_index** ( id: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_table_row_index)

Sets position of the row in the table.

---

<span id="class_DisplayServer_method_accessibility_update_set_text_align"></span>

void **accessibility_update_set_text_align** ( id: [RID](class_rid.md#class_RID), align: HorizontalAlignment ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_text_align)

Sets element text alignment.

---

<span id="class_DisplayServer_method_accessibility_update_set_text_decorations"></span>

void **accessibility_update_set_text_decorations** ( id: [RID](class_rid.md#class_RID), underline: [bool](class_bool.md#class_bool), strikethrough: [bool](class_bool.md#class_bool), overline: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_text_decorations)

Sets text underline/overline/strikethrough.

---

<span id="class_DisplayServer_method_accessibility_update_set_text_orientation"></span>

void **accessibility_update_set_text_orientation** ( id: [RID](class_rid.md#class_RID), vertical: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_text_orientation)

Sets text orientation.

---

<span id="class_DisplayServer_method_accessibility_update_set_text_selection"></span>

void **accessibility_update_set_text_selection** ( id: [RID](class_rid.md#class_RID), text_start_id: [RID](class_rid.md#class_RID), start_char: [int](class_int.md#class_int), text_end_id: [RID](class_rid.md#class_RID), end_char: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_text_selection)

Sets text selection to the text field. `text_start_id` and `text_end_id` should be elements created by [accessibility_create_sub_text_edit_elements()](class_displayserver.md#class_DisplayServer_method_accessibility_create_sub_text_edit_elements). Character offsets are relative to the corresponding element.

---

<span id="class_DisplayServer_method_accessibility_update_set_tooltip"></span>

void **accessibility_update_set_tooltip** ( id: [RID](class_rid.md#class_RID), tooltip: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_tooltip)

Sets tooltip text.

---

<span id="class_DisplayServer_method_accessibility_update_set_transform"></span>

void **accessibility_update_set_transform** ( id: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_transform)

Sets element 2D transform.

---

<span id="class_DisplayServer_method_accessibility_update_set_url"></span>

void **accessibility_update_set_url** ( id: [RID](class_rid.md#class_RID), url: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_url)

Sets link URL.

---

<span id="class_DisplayServer_method_accessibility_update_set_value"></span>

void **accessibility_update_set_value** ( id: [RID](class_rid.md#class_RID), value: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_accessibility_update_set_value)

Sets element text value.

---

<span id="class_DisplayServer_method_beep"></span>

void **beep** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_beep)

Plays the beep sound from the operative system, if possible. Because it comes from the OS, the beep sound will be audible even if the application is muted. It may also be disabled for the entire OS by the user.

 **Note:** This method is implemented on macOS, Linux (X11/Wayland), and Windows.

---

<span id="class_DisplayServer_method_clipboard_get"></span>

[String](class_string.md#class_String) **clipboard_get** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_clipboard_get)

Returns the user's clipboard as a string if possible.

---

<span id="class_DisplayServer_method_clipboard_get_image"></span>

[Image](class_image.md#class_Image) **clipboard_get_image** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_clipboard_get_image)

Returns the user's clipboard as an image if possible.

 **Note:** This method uses the copied pixel data, e.g. from an image editing software or a web browser, not an image file copied from file explorer.

---

<span id="class_DisplayServer_method_clipboard_get_primary"></span>

[String](class_string.md#class_String) **clipboard_get_primary** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_clipboard_get_primary)

Returns the user's primary clipboard as a string if possible. This is the clipboard that is set when the user selects text in any application, rather than when pressing :kbd:`Ctrl + C`. The clipboard data can then be pasted by clicking the middle mouse button in any application that supports the primary clipboard mechanism.

 **Note:** This method is only implemented on Linux (X11/Wayland).

---

<span id="class_DisplayServer_method_clipboard_has"></span>

[bool](class_bool.md#class_bool) **clipboard_has** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_clipboard_has)

Returns `true` if there is a text content on the user's clipboard.

---

<span id="class_DisplayServer_method_clipboard_has_image"></span>

[bool](class_bool.md#class_bool) **clipboard_has_image** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_clipboard_has_image)

Returns `true` if there is an image content on the user's clipboard.

---

<span id="class_DisplayServer_method_clipboard_set"></span>

void **clipboard_set** ( clipboard: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_clipboard_set)

Sets the user's clipboard content to the given string.

---

<span id="class_DisplayServer_method_clipboard_set_primary"></span>

void **clipboard_set_primary** ( clipboard_primary: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_clipboard_set_primary)

Sets the user's primary clipboard content to the given string. This is the clipboard that is set when the user selects text in any application, rather than when pressing :kbd:`Ctrl + C`. The clipboard data can then be pasted by clicking the middle mouse button in any application that supports the primary clipboard mechanism.

 **Note:** This method is only implemented on Linux (X11/Wayland).

---

<span id="class_DisplayServer_method_color_picker"></span>

[bool](class_bool.md#class_bool) **color_picker** ( callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_color_picker)

Displays OS native color picker.

Callbacks have the following arguments: `status: bool, color: Color`.

 **Note:** This method is implemented if the display server has the [FEATURE_NATIVE_COLOR_PICKER](class_displayserver.md#class_DisplayServer_constant_FEATURE_NATIVE_COLOR_PICKER) feature.

 **Note:** This method is only implemented on Linux (X11/Wayland).

---

<span id="class_DisplayServer_method_create_status_indicator"></span>

[int](class_int.md#class_int) **create_status_indicator** ( icon: [Texture2D](class_texture2d.md#class_Texture2D), tooltip: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_create_status_indicator)

Creates a new application status indicator with the specified icon, tooltip, and activation callback.

 `callback` should take two arguments: the pressed mouse button (one of the MouseButton constants) and the click position in screen coordinates (a [Vector2i](class_vector2i.md#class_Vector2i)).

---

<span id="class_DisplayServer_method_cursor_get_shape"></span>

[CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) **cursor_get_shape** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_cursor_get_shape)

Returns the default mouse cursor shape set by [cursor_set_shape()](class_displayserver.md#class_DisplayServer_method_cursor_set_shape).

---

<span id="class_DisplayServer_method_cursor_set_custom_image"></span>

void **cursor_set_custom_image** ( cursor: [Resource](class_resource.md#class_Resource), shape: [CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) = 0, hotspot: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) [🔗](class_displayserver.md#class_DisplayServer_method_cursor_set_custom_image)

Sets a custom mouse cursor image for the given `shape`. This means the user's operating system and mouse cursor theme will no longer influence the mouse cursor's appearance.

 `cursor` can be either a [Texture2D](class_texture2d.md#class_Texture2D) or an [Image](class_image.md#class_Image), and it should not be larger than 256×256 to display correctly. Optionally, `hotspot` can be set to offset the image's position relative to the click point. By default, `hotspot` is set to the top-left corner of the image. See also [cursor_set_shape()](class_displayserver.md#class_DisplayServer_method_cursor_set_shape).

 **Note:** On Web, calling this method every frame can cause the cursor to flicker.

---

<span id="class_DisplayServer_method_cursor_set_shape"></span>

void **cursor_set_shape** ( shape: [CursorShape](class_displayserver.md#enum_DisplayServer_CursorShape) ) [🔗](class_displayserver.md#class_DisplayServer_method_cursor_set_shape)

Sets the default mouse cursor shape. The cursor's appearance will vary depending on the user's operating system and mouse cursor theme. See also [cursor_get_shape()](class_displayserver.md#class_DisplayServer_method_cursor_get_shape) and [cursor_set_custom_image()](class_displayserver.md#class_DisplayServer_method_cursor_set_custom_image).

---

<span id="class_DisplayServer_method_delete_status_indicator"></span>

void **delete_status_indicator** ( id: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_delete_status_indicator)

Removes the application status indicator.

---

<span id="class_DisplayServer_method_dialog_input_text"></span>

Error **dialog_input_text** ( title: [String](class_string.md#class_String), description: [String](class_string.md#class_String), existing_text: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_dialog_input_text)

Shows a text input dialog which uses the operating system's native look-and-feel. `callback` should accept a single [String](class_string.md#class_String) parameter which contains the text field's contents.

 **Note:** This method is implemented if the display server has the [FEATURE_NATIVE_DIALOG_INPUT](class_displayserver.md#class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_INPUT) feature. Supported platforms include macOS, Windows, and Android.

---

<span id="class_DisplayServer_method_dialog_show"></span>

Error **dialog_show** ( title: [String](class_string.md#class_String), description: [String](class_string.md#class_String), buttons: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_dialog_show)

Shows a text dialog which uses the operating system's native look-and-feel. `callback` should accept a single [int](class_int.md#class_int) parameter which corresponds to the index of the pressed button.

 **Note:** This method is implemented if the display server has the [FEATURE_NATIVE_DIALOG](class_displayserver.md#class_DisplayServer_constant_FEATURE_NATIVE_DIALOG) feature. Supported platforms include macOS, Windows, and Android.

---

<span id="class_DisplayServer_method_enable_for_stealing_focus"></span>

void **enable_for_stealing_focus** ( process_id: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_enable_for_stealing_focus)

Allows the `process_id` PID to steal focus from this window. In other words, this disables the operating system's focus stealing protection for the specified PID.

 **Note:** This method is implemented only on Windows.

---

<span id="class_DisplayServer_method_file_dialog_show"></span>

Error **file_dialog_show** ( title: [String](class_string.md#class_String), current_directory: [String](class_string.md#class_String), filename: [String](class_string.md#class_String), show_hidden: [bool](class_bool.md#class_bool), mode: [FileDialogMode](class_displayserver.md#enum_DisplayServer_FileDialogMode), filters: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), callback: [Callable](class_callable.md#class_Callable), parent_window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_file_dialog_show)

Displays OS native dialog for selecting files or directories in the file system.

Each filter string in the `filters` array should be formatted like this: `*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description text of the filter is optional and can be omitted. It is recommended to set both file extension and MIME type. See also [FileDialog.filters](class_filedialog.md#class_FileDialog_property_filters).

Callbacks have the following arguments: `status: bool, selected_paths: PackedStringArray, selected_filter_index: int`. **On Android,** the third callback argument (`selected_filter_index`) is always `0`.

 **Note:** This method is implemented if the display server has the [FEATURE_NATIVE_DIALOG_FILE](class_displayserver.md#class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_FILE) feature. Supported platforms include Linux (X11/Wayland), Windows, macOS, and Android.

 **Note:** `current_directory` might be ignored.

 **Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.

 **Note:** On Android and Linux, `show_hidden` is ignored.

 **Note:** On Android and macOS, native file dialogs have no title.

 **Note:** On macOS, sandboxed apps will save security-scoped bookmarks to retain access to the opened folders across multiple sessions. Use [OS.get_granted_permissions()](class_os.md#class_OS_method_get_granted_permissions) to get a list of saved bookmarks.

 **Note:** On Android, this method uses the Android Storage Access Framework (SAF).

The file picker returns a URI instead of a filesystem path. This URI can be passed directly to [FileAccess](class_fileaccess.md#class_FileAccess) to perform read/write operations.

When using [FILE_DIALOG_MODE_OPEN_DIR](class_displayserver.md#class_DisplayServer_constant_FILE_DIALOG_MODE_OPEN_DIR), it returns a tree URI that grants full access to the selected directory. File operations inside this directory can be performed by passing a path on the form `treeUri#relative/path/to/file` to [FileAccess](class_fileaccess.md#class_FileAccess).

To avoid opening the file picker again after each app restart, you can take persistable URI permission as follows:

.. tabs::

```
```

    val uri = "content://com.android..." # URI of the selected file or folder.
    val persist = true # Set to false to release the persistable permission.
    var android_runtime = Engine.get_singleton("AndroidRuntime")
    android_runtime.updatePersistableUriPermission(uri, persist)

The persistable URI permission remains valid across app restarts as long as the directory is not moved, renamed, or deleted.

---

<span id="class_DisplayServer_method_file_dialog_with_options_show"></span>

Error **file_dialog_with_options_show** ( title: [String](class_string.md#class_String), current_directory: [String](class_string.md#class_String), root: [String](class_string.md#class_String), filename: [String](class_string.md#class_String), show_hidden: [bool](class_bool.md#class_bool), mode: [FileDialogMode](class_displayserver.md#enum_DisplayServer_FileDialogMode), filters: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray), options: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\], callback: [Callable](class_callable.md#class_Callable), parent_window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_file_dialog_with_options_show)

Displays OS native dialog for selecting files or directories in the file system with additional user selectable options.

Each filter string in the `filters` array should be formatted like this: `*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description text of the filter is optional and can be omitted. It is recommended to set both file extension and MIME type. See also [FileDialog.filters](class_filedialog.md#class_FileDialog_property_filters).

 `options` is array of [Dictionary](class_dictionary.md#class_Dictionary) s with the following keys:

- `"name"` - option's name [String](class_string.md#class_String).

- `"values"` - [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) of values. If empty, boolean option (check box) is used.

- `"default"` - default selected option index ([int](class_int.md#class_int)) or default boolean value ([bool](class_bool.md#class_bool)).

Callbacks have the following arguments: `status: bool, selected_paths: PackedStringArray, selected_filter_index: int, selected_option: Dictionary`.

 **Note:** This method is implemented if the display server has the [FEATURE_NATIVE_DIALOG_FILE_EXTRA](class_displayserver.md#class_DisplayServer_constant_FEATURE_NATIVE_DIALOG_FILE_EXTRA) feature. Supported platforms include Linux (X11/Wayland), Windows, and macOS.

 **Note:** `current_directory` might be ignored.

 **Note:** Embedded file dialogs and Windows file dialogs support only file extensions, while Android, Linux, and macOS file dialogs also support MIME types.

 **Note:** On Linux (X11), `show_hidden` is ignored.

 **Note:** On macOS, native file dialogs have no title.

 **Note:** On macOS, sandboxed apps will save security-scoped bookmarks to retain access to the opened folders across multiple sessions. Use [OS.get_granted_permissions()](class_os.md#class_OS_method_get_granted_permissions) to get a list of saved bookmarks.

---

<span id="class_DisplayServer_method_force_process_and_drop_events"></span>

void **force_process_and_drop_events** ( ) [🔗](class_displayserver.md#class_DisplayServer_method_force_process_and_drop_events)

Forces window manager processing while ignoring all [InputEvent](class_inputevent.md#class_InputEvent) s. See also [process_events()](class_displayserver.md#class_DisplayServer_method_process_events).

 **Note:** This method is implemented on Windows and macOS.

---

<span id="class_DisplayServer_method_get_accent_color"></span>

[Color](class_color.md#class_Color) **get_accent_color** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_accent_color)

Returns OS theme accent color. Returns `Color(0, 0, 0, 0)`, if accent color is unknown.

 **Note:** This method is implemented on macOS, Windows, Android, and Linux (X11/Wayland).

---

<span id="class_DisplayServer_method_get_base_color"></span>

[Color](class_color.md#class_Color) **get_base_color** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_base_color)

Returns the OS theme base color (default control background). Returns `Color(0, 0, 0, 0)` if the base color is unknown.

 **Note:** This method is implemented on macOS, Windows, and Android.

---

<span id="class_DisplayServer_method_get_display_cutouts"></span>

[Array](class_array.md#class_Array)\[[Rect2](class_rect2.md#class_Rect2)\] **get_display_cutouts** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_display_cutouts)

Returns an [Array](class_array.md#class_Array) of [Rect2](class_rect2.md#class_Rect2), each of which is the bounding rectangle for a display cutout or notch. These are non-functional areas on edge-to-edge screens used by cameras and sensors. Returns an empty array if the device does not have cutouts. See also [get_display_safe_area()](class_displayserver.md#class_DisplayServer_method_get_display_safe_area).

 **Note:** Currently only implemented on Android. Other platforms will return an empty array even if they do have display cutouts or notches.

---

<span id="class_DisplayServer_method_get_display_safe_area"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **get_display_safe_area** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_display_safe_area)

Returns the unobscured area of the display where interactive controls should be rendered. See also [get_display_cutouts()](class_displayserver.md#class_DisplayServer_method_get_display_cutouts).

 **Note:** Currently only implemented on Android and iOS. On other platforms, `screen_get_usable_rect(SCREEN_OF_MAIN_WINDOW)` will be returned as a fallback. See also [screen_get_usable_rect()](class_displayserver.md#class_DisplayServer_method_screen_get_usable_rect).

---

<span id="class_DisplayServer_method_get_keyboard_focus_screen"></span>

[int](class_int.md#class_int) **get_keyboard_focus_screen** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_keyboard_focus_screen)

Returns the index of the screen containing the window with the keyboard focus, or the primary screen if there's no focused window.

 **Note:** This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns the primary screen.

---

<span id="class_DisplayServer_method_get_name"></span>

[String](class_string.md#class_String) **get_name** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_name)

Returns the name of the **DisplayServer** currently in use. Most operating systems only have a single **DisplayServer**, but Linux has access to more than one **DisplayServer** (currently X11 and Wayland).

The names of built-in display servers are `Windows`, `macOS`, `X11` (Linux), `Wayland` (Linux), `Android`, `iOS`, `web` (HTML5), and `headless` (when started with the `--headless` [command line argument](../tutorials/editor/command_line_tutorial.md)).

---

<span id="class_DisplayServer_method_get_primary_screen"></span>

[int](class_int.md#class_int) **get_primary_screen** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_primary_screen)

Returns the index of the primary screen.

 **Note:** This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns `0`.

---

<span id="class_DisplayServer_method_get_screen_count"></span>

[int](class_int.md#class_int) **get_screen_count** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_screen_count)

Returns the number of displays available.

 **Note:** This method is implemented on Linux (X11 and Wayland), macOS, and Windows. On other platforms, this method always returns `1`.

---

<span id="class_DisplayServer_method_get_screen_from_rect"></span>

[int](class_int.md#class_int) **get_screen_from_rect** ( rect: [Rect2](class_rect2.md#class_Rect2) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_screen_from_rect)

Returns the index of the screen that overlaps the most with the given rectangle. Returns [INVALID_SCREEN](class_displayserver.md#class_DisplayServer_constant_INVALID_SCREEN) if the rectangle doesn't overlap with any screen or has no area.

---

<span id="class_DisplayServer_method_get_swap_cancel_ok"></span>

[bool](class_bool.md#class_bool) **get_swap_cancel_ok** ( ) [🔗](class_displayserver.md#class_DisplayServer_method_get_swap_cancel_ok)

Returns `true` if positions of **OK** and **Cancel** buttons are swapped in dialogs. This is enabled by default on Windows to follow interface conventions, and be toggled by changing ProjectSettings.gui/common/swap_cancel_ok.

 **Note:** This doesn't affect native dialogs such as the ones spawned by [dialog_show()](class_displayserver.md#class_DisplayServer_method_dialog_show).

---

<span id="class_DisplayServer_method_get_window_at_screen_position"></span>

[int](class_int.md#class_int) **get_window_at_screen_position** ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_window_at_screen_position)

Returns the ID of the window at the specified screen `position` (in pixels). On multi-monitor setups, the screen position is relative to the virtual desktop area. On multi-monitor setups with different screen resolutions or orientations, the origin may be located outside any display like this:

.. code:: text

    * (0, 0)        +-------+
                    |       |
    +-------------+ |       |
    |             | |       |
    |             | |       |
    +-------------+ +-------+

---

<span id="class_DisplayServer_method_get_window_list"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_window_list** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_get_window_list)

Returns the list of Godot window IDs belonging to this process.

 **Note:** Native dialogs are not included in this list.

---

<span id="class_DisplayServer_method_global_menu_add_check_item"></span>

[int](class_int.md#class_int) **global_menu_add_check_item** ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_add_check_item)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Adds a new checkable item with text `label` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMask s and Key s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (:kbd:`Ctrl + A`).

 **Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_add_icon_check_item"></span>

[int](class_int.md#class_int) **global_menu_add_icon_check_item** ( menu_root: [String](class_string.md#class_String), icon: [Texture2D](class_texture2d.md#class_Texture2D), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_add_icon_check_item)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Adds a new checkable item with text `label` and icon `icon` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMask s and Key s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (:kbd:`Ctrl + A`).

 **Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_add_icon_item"></span>

[int](class_int.md#class_int) **global_menu_add_icon_item** ( menu_root: [String](class_string.md#class_String), icon: [Texture2D](class_texture2d.md#class_Texture2D), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_add_icon_item)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Adds a new item with text `label` and icon `icon` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMask s and Key s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (:kbd:`Ctrl + A`).

 **Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_add_icon_radio_check_item"></span>

[int](class_int.md#class_int) **global_menu_add_icon_radio_check_item** ( menu_root: [String](class_string.md#class_String), icon: [Texture2D](class_texture2d.md#class_Texture2D), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_add_icon_radio_check_item)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Adds a new radio-checkable item with text `label` and icon `icon` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMask s and Key s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (:kbd:`Ctrl + A`).

 **Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [global_menu_set_item_checked()](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_checked) for more info on how to control it.

 **Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_add_item"></span>

[int](class_int.md#class_int) **global_menu_add_item** ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_add_item)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Adds a new item with text `label` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMask s and Key s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (:kbd:`Ctrl + A`).

 **Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_add_multistate_item"></span>

[int](class_int.md#class_int) **global_menu_add_multistate_item** ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), max_states: [int](class_int.md#class_int), default_state: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_add_multistate_item)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Adds a new item with text `label` to the global menu with ID `menu_root`.

Contrarily to normal binary items, multistate items can have more than two states, as defined by `max_states`. Each press or activate of the item will increase the state by one. The default value is defined by `default_state`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMask s and Key s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (:kbd:`Ctrl + A`).

 **Note:** By default, there's no indication of the current item state, it should be changed manually.

 **Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_add_radio_check_item"></span>

[int](class_int.md#class_int) **global_menu_add_radio_check_item** ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), callback: [Callable](class_callable.md#class_Callable) = Callable(), key_callback: [Callable](class_callable.md#class_Callable) = Callable(), tag: [Variant](class_variant.md#class_Variant) = null, accelerator: Key = 0, index: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_add_radio_check_item)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Adds a new radio-checkable item with text `label` to the global menu with ID `menu_root`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of KeyModifierMask s and Key s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (:kbd:`Ctrl + A`).

 **Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See [global_menu_set_item_checked()](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_checked) for more info on how to control it.

 **Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_add_separator"></span>

[int](class_int.md#class_int) **global_menu_add_separator** ( menu_root: [String](class_string.md#class_String), index: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_add_separator)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Adds a separator between items to the global menu with ID `menu_root`. Separators also occupy an index.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_add_submenu_item"></span>

[int](class_int.md#class_int) **global_menu_add_submenu_item** ( menu_root: [String](class_string.md#class_String), label: [String](class_string.md#class_String), submenu: [String](class_string.md#class_String), index: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_add_submenu_item)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Adds an item that will act as a submenu of the global menu `menu_root`. The `submenu` argument is the ID of the global menu root that will be shown when the item is clicked.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_clear"></span>

void **global_menu_clear** ( menu_root: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_clear)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Removes all items from the global menu with ID `menu_root`.

 **Note:** This method is implemented only on macOS.

 **Supported system menu IDs:**

.. code:: text

    "_main" - Main menu (macOS).
    "_dock" - Dock popup menu (macOS).
    "_apple" - Apple menu (macOS, custom items added before "Services").
    "_window" - Window menu (macOS, custom items added after "Bring All to Front").
    "_help" - Help menu (macOS).

---

<span id="class_DisplayServer_method_global_menu_get_item_accelerator"></span>

Key **global_menu_get_item_accelerator** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_accelerator)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the accelerator of the item at index `idx`. Accelerators are special combinations of keys that activate the item, no matter which control is focused.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_callback"></span>

[Callable](class_callable.md#class_Callable) **global_menu_get_item_callback** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_callback)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the callback of the item at index `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_count"></span>

[int](class_int.md#class_int) **global_menu_get_item_count** ( menu_root: [String](class_string.md#class_String) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_count)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns number of items in the global menu with ID `menu_root`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **global_menu_get_item_icon** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_icon)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the icon of the item at index `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_indentation_level"></span>

[int](class_int.md#class_int) **global_menu_get_item_indentation_level** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_indentation_level)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the horizontal offset of the item at the given `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_index_from_tag"></span>

[int](class_int.md#class_int) **global_menu_get_item_index_from_tag** ( menu_root: [String](class_string.md#class_String), tag: [Variant](class_variant.md#class_Variant) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_index_from_tag)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the index of the item with the specified `tag`. Indices are automatically assigned to each item by the engine, and cannot be set manually.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_index_from_text"></span>

[int](class_int.md#class_int) **global_menu_get_item_index_from_text** ( menu_root: [String](class_string.md#class_String), text: [String](class_string.md#class_String) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_index_from_text)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the index of the item with the specified `text`. Indices are automatically assigned to each item by the engine, and cannot be set manually.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_key_callback"></span>

[Callable](class_callable.md#class_Callable) **global_menu_get_item_key_callback** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_key_callback)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the callback of the item accelerator at index `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_max_states"></span>

[int](class_int.md#class_int) **global_menu_get_item_max_states** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_max_states)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns number of states of a multistate item. See [global_menu_add_multistate_item()](class_displayserver.md#class_DisplayServer_method_global_menu_add_multistate_item) for details.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_state"></span>

[int](class_int.md#class_int) **global_menu_get_item_state** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_state)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the state of a multistate item. See [global_menu_add_multistate_item()](class_displayserver.md#class_DisplayServer_method_global_menu_add_multistate_item) for details.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_submenu"></span>

[String](class_string.md#class_String) **global_menu_get_item_submenu** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_submenu)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the submenu ID of the item at index `idx`. See [global_menu_add_submenu_item()](class_displayserver.md#class_DisplayServer_method_global_menu_add_submenu_item) for more info on how to add a submenu.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_tag"></span>

[Variant](class_variant.md#class_Variant) **global_menu_get_item_tag** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_tag)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the metadata of the specified item, which might be of any type. You can set it with [global_menu_set_item_tag()](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_tag), which provides a simple way of assigning context data to items.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_text"></span>

[String](class_string.md#class_String) **global_menu_get_item_text** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_text)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the text of the item at index `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_item_tooltip"></span>

[String](class_string.md#class_String) **global_menu_get_item_tooltip** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_tooltip)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns the tooltip associated with the specified index `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_get_system_menu_roots"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **global_menu_get_system_menu_roots** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_get_system_menu_roots)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns Dictionary of supported system menu IDs and names.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_is_item_checkable"></span>

[bool](class_bool.md#class_bool) **global_menu_is_item_checkable** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_checkable)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns `true` if the item at index `idx` is checkable in some way, i.e. if it has a checkbox or radio button.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_is_item_checked"></span>

[bool](class_bool.md#class_bool) **global_menu_is_item_checked** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_checked)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns `true` if the item at index `idx` is checked.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_is_item_disabled"></span>

[bool](class_bool.md#class_bool) **global_menu_is_item_disabled** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_disabled)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns `true` if the item at index `idx` is disabled. When it is disabled it can't be selected, or its action invoked.

See [global_menu_set_item_disabled()](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_disabled) for more info on how to disable an item.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_is_item_hidden"></span>

[bool](class_bool.md#class_bool) **global_menu_is_item_hidden** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_hidden)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns `true` if the item at index `idx` is hidden.

See [global_menu_set_item_hidden()](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_hidden) for more info on how to hide an item.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_is_item_radio_checkable"></span>

[bool](class_bool.md#class_bool) **global_menu_is_item_radio_checkable** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_is_item_radio_checkable)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Returns `true` if the item at index `idx` has radio button-style checkability.

 **Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_remove_item"></span>

void **global_menu_remove_item** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_remove_item)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Removes the item at index `idx` from the global menu `menu_root`.

 **Note:** The indices of items after the removed item will be shifted by one.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_accelerator"></span>

void **global_menu_set_item_accelerator** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), keycode: Key ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_accelerator)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the accelerator of the item at index `idx`. `keycode` can be a single Key, or a combination of KeyModifierMask s and Key s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (:kbd:`Ctrl + A`).

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_callback"></span>

void **global_menu_set_item_callback** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_callback)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the callback of the item at index `idx`. Callback is emitted when an item is pressed.

 **Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_checkable"></span>

void **global_menu_set_item_checkable** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), checkable: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_checkable)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets whether the item at index `idx` has a checkbox. If `false`, sets the type of the item to plain text.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_checked"></span>

void **global_menu_set_item_checked** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), checked: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_checked)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the checkstate status of the item at index `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_disabled"></span>

void **global_menu_set_item_disabled** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_disabled)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Enables/disables the item at index `idx`. When it is disabled, it can't be selected and its action can't be invoked.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_hidden"></span>

void **global_menu_set_item_hidden** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), hidden: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_hidden)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Hides/shows the item at index `idx`. When it is hidden, an item does not appear in a menu and its action cannot be invoked.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_hover_callbacks"></span>

void **global_menu_set_item_hover_callbacks** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_hover_callbacks)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the callback of the item at index `idx`. The callback is emitted when an item is hovered.

 **Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_icon"></span>

void **global_menu_set_item_icon** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_icon)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Replaces the [Texture2D](class_texture2d.md#class_Texture2D) icon of the specified `idx`.

 **Note:** This method is implemented only on macOS.

 **Note:** This method is not supported by macOS "_dock" menu items.

---

<span id="class_DisplayServer_method_global_menu_set_item_indentation_level"></span>

void **global_menu_set_item_indentation_level** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), level: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_indentation_level)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the horizontal offset of the item at the given `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_key_callback"></span>

void **global_menu_set_item_key_callback** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), key_callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_key_callback)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the callback of the item at index `idx`. Callback is emitted when its accelerator is activated.

 **Note:** The `key_callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_max_states"></span>

void **global_menu_set_item_max_states** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), max_states: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_max_states)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets number of state of a multistate item. See [global_menu_add_multistate_item()](class_displayserver.md#class_DisplayServer_method_global_menu_add_multistate_item) for details.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_radio_checkable"></span>

void **global_menu_set_item_radio_checkable** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), checkable: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_radio_checkable)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the type of the item at the specified index `idx` to radio button. If `false`, sets the type of the item to plain text.

 **Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_state"></span>

void **global_menu_set_item_state** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), state: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_state)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the state of a multistate item. See [global_menu_add_multistate_item()](class_displayserver.md#class_DisplayServer_method_global_menu_add_multistate_item) for details.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_submenu"></span>

void **global_menu_set_item_submenu** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), submenu: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_submenu)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the submenu of the item at index `idx`. The submenu is the ID of a global menu root that would be shown when the item is clicked.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_tag"></span>

void **global_menu_set_item_tag** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), tag: [Variant](class_variant.md#class_Variant) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_tag)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the metadata of an item, which may be of any type. You can later get it with [global_menu_get_item_tag()](class_displayserver.md#class_DisplayServer_method_global_menu_get_item_tag), which provides a simple way of assigning context data to items.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_text"></span>

void **global_menu_set_item_text** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), text: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_text)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the text of the item at index `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_item_tooltip"></span>

void **global_menu_set_item_tooltip** ( menu_root: [String](class_string.md#class_String), idx: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_item_tooltip)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Sets the [String](class_string.md#class_String) tooltip of the item at the specified index `idx`.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_global_menu_set_popup_callbacks"></span>

void **global_menu_set_popup_callbacks** ( menu_root: [String](class_string.md#class_String), open_callback: [Callable](class_callable.md#class_Callable), close_callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_global_menu_set_popup_callbacks)

**Deprecated:** Use [NativeMenu](class_nativemenu.md#class_NativeMenu) or [PopupMenu](class_popupmenu.md#class_PopupMenu) instead.

Registers callables to emit when the menu is respectively about to show or closed. Callback methods should have zero arguments.

---

<span id="class_DisplayServer_method_has_additional_outputs"></span>

[bool](class_bool.md#class_bool) **has_additional_outputs** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_has_additional_outputs)

Returns `true` if any additional outputs have been registered via [register_additional_output()](class_displayserver.md#class_DisplayServer_method_register_additional_output).

---

<span id="class_DisplayServer_method_has_feature"></span>

[bool](class_bool.md#class_bool) **has_feature** ( feature: [Feature](class_displayserver.md#enum_DisplayServer_Feature) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_has_feature)

Returns `true` if the specified `feature` is supported by the current **DisplayServer**, `false` otherwise.

---

<span id="class_DisplayServer_method_has_hardware_keyboard"></span>

[bool](class_bool.md#class_bool) **has_hardware_keyboard** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_has_hardware_keyboard)

Returns `true` if a hardware keyboard is connected.

 **Note:** This method is implemented on Android and iOS. On other platforms, this method always returns `true`.

---

<span id="class_DisplayServer_method_help_set_search_callbacks"></span>

void **help_set_search_callbacks** ( search_callback: [Callable](class_callable.md#class_Callable), action_callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_help_set_search_callbacks)

Sets native help system search callbacks.

 `search_callback` has the following arguments: `String search_string, int result_limit` and return a [Dictionary](class_dictionary.md#class_Dictionary) with "key, display name" pairs for the search results. Called when the user enters search terms in the `Help` menu.

 `action_callback` has the following arguments: `String key`. Called when the user selects a search result in the `Help` menu.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_ime_get_selection"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **ime_get_selection** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_ime_get_selection)

Returns the text selection in the Input Method Editor composition string, with the [Vector2i](class_vector2i.md#class_Vector2i)'s `x` component being the caret position and `y` being the length of the selection.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_ime_get_text"></span>

[String](class_string.md#class_String) **ime_get_text** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_ime_get_text)

Returns the composition string contained within the Input Method Editor window.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_is_dark_mode"></span>

[bool](class_bool.md#class_bool) **is_dark_mode** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_is_dark_mode)

Returns `true` if OS is using dark mode.

 **Note:** This method is implemented on Android, iOS, macOS, Windows, and Linux (X11/Wayland).

---

<span id="class_DisplayServer_method_is_dark_mode_supported"></span>

[bool](class_bool.md#class_bool) **is_dark_mode_supported** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_is_dark_mode_supported)

Returns `true` if OS supports dark mode.

 **Note:** This method is implemented on Android, iOS, macOS, Windows, and Linux (X11/Wayland).

---

<span id="class_DisplayServer_method_is_touchscreen_available"></span>

[bool](class_bool.md#class_bool) **is_touchscreen_available** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_is_touchscreen_available)

Returns `true` if touch events are available (Android or iOS), the capability is detected on the Web platform or if ProjectSettings.input_devices/pointing/emulate_touch_from_mouse is `true`.

---

<span id="class_DisplayServer_method_is_window_transparency_available"></span>

[bool](class_bool.md#class_bool) **is_window_transparency_available** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_is_window_transparency_available)

Returns `true` if the window background can be made transparent. This method returns `false` if ProjectSettings.display/window/per_pixel_transparency/allowed is set to `false`, or if transparency is not supported by the renderer or OS compositor.

---

<span id="class_DisplayServer_method_keyboard_get_current_layout"></span>

[int](class_int.md#class_int) **keyboard_get_current_layout** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_keyboard_get_current_layout)

Returns active keyboard layout index.

 **Note:** This method is implemented on Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_keyboard_get_keycode_from_physical"></span>

Key **keyboard_get_keycode_from_physical** ( keycode: Key ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_keyboard_get_keycode_from_physical)

Converts a physical (US QWERTY) `keycode` to one in the active keyboard layout.

 **Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

<span id="class_DisplayServer_method_keyboard_get_label_from_physical"></span>

Key **keyboard_get_label_from_physical** ( keycode: Key ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_keyboard_get_label_from_physical)

Converts a physical (US QWERTY) `keycode` to localized label printed on the key in the active keyboard layout.

 **Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

<span id="class_DisplayServer_method_keyboard_get_layout_count"></span>

[int](class_int.md#class_int) **keyboard_get_layout_count** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_keyboard_get_layout_count)

Returns the number of keyboard layouts.

 **Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

<span id="class_DisplayServer_method_keyboard_get_layout_language"></span>

[String](class_string.md#class_String) **keyboard_get_layout_language** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_keyboard_get_layout_language)

Returns the ISO-639/BCP-47 language code of the keyboard layout at position `index`.

 **Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

<span id="class_DisplayServer_method_keyboard_get_layout_name"></span>

[String](class_string.md#class_String) **keyboard_get_layout_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_keyboard_get_layout_name)

Returns the localized name of the keyboard layout at position `index`.

 **Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

<span id="class_DisplayServer_method_keyboard_set_current_layout"></span>

void **keyboard_set_current_layout** ( index: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_keyboard_set_current_layout)

Sets the active keyboard layout.

 **Note:** This method is implemented on Linux (X11/Wayland), macOS and Windows.

---

<span id="class_DisplayServer_method_mouse_get_button_state"></span>

*BitField*\[MouseButtonMask\] **mouse_get_button_state** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_mouse_get_button_state)

Returns the current state of mouse buttons (whether each button is pressed) as a bitmask. If multiple mouse buttons are pressed at the same time, the bits are added together. Equivalent to [Input.get_mouse_button_mask()](class_input.md#class_Input_method_get_mouse_button_mask).

---

<span id="class_DisplayServer_method_mouse_get_mode"></span>

[MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) **mouse_get_mode** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_mouse_get_mode)

Returns the current mouse mode. See also [mouse_set_mode()](class_displayserver.md#class_DisplayServer_method_mouse_set_mode).

---

<span id="class_DisplayServer_method_mouse_get_position"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **mouse_get_position** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_mouse_get_position)

Returns the mouse cursor's current position in screen coordinates.

---

<span id="class_DisplayServer_method_mouse_set_mode"></span>

void **mouse_set_mode** ( mouse_mode: [MouseMode](class_displayserver.md#enum_DisplayServer_MouseMode) ) [🔗](class_displayserver.md#class_DisplayServer_method_mouse_set_mode)

Sets the current mouse mode. See also [mouse_get_mode()](class_displayserver.md#class_DisplayServer_method_mouse_get_mode).

---

<span id="class_DisplayServer_method_process_events"></span>

void **process_events** ( ) [🔗](class_displayserver.md#class_DisplayServer_method_process_events)

Perform window manager processing, including input flushing. See also [force_process_and_drop_events()](class_displayserver.md#class_DisplayServer_method_force_process_and_drop_events), [Input.flush_buffered_events()](class_input.md#class_Input_method_flush_buffered_events) and [Input.use_accumulated_input](class_input.md#class_Input_property_use_accumulated_input).

---

<span id="class_DisplayServer_method_register_additional_output"></span>

void **register_additional_output** ( object: [Object](class_object.md#class_Object) ) [🔗](class_displayserver.md#class_DisplayServer_method_register_additional_output)

Registers an [Object](class_object.md#class_Object) which represents an additional output that will be rendered too, beyond normal windows. The [Object](class_object.md#class_Object) is only used as an identifier, which can be later passed to [unregister_additional_output()](class_displayserver.md#class_DisplayServer_method_unregister_additional_output).

This can be used to prevent Godot from skipping rendering when no normal windows are visible.

---

<span id="class_DisplayServer_method_screen_get_dpi"></span>

[int](class_int.md#class_int) **screen_get_dpi** ( screen: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_dpi)

Returns the dots per inch density of the specified screen. Returns platform specific default value if `screen` is invalid.

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

 **Note:** On macOS, returned value is inaccurate if fractional display scaling mode is used.

 **Note:** On Android devices, the actual screen densities are grouped into six generalized densities:

.. code:: text

       ldpi - 120 dpi
       mdpi - 160 dpi
       hdpi - 240 dpi
      xhdpi - 320 dpi
     xxhdpi - 480 dpi
    xxxhdpi - 640 dpi

 **Note:** This method is implemented on Android, iOS, Linux (X11/Wayland), macOS, Web, and Windows. On other platforms, this method always returns `72`.

---

<span id="class_DisplayServer_method_screen_get_image"></span>

[Image](class_image.md#class_Image) **screen_get_image** ( screen: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_image)

Returns a screenshot of the `screen`. Returns `null` if `screen` is invalid or the **DisplayServer** fails to capture screenshot.

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

 **Note:** This method is implemented on Linux (X11, excluding XWayland), macOS, and Windows. On other platforms, this method always returns `null`.

 **Note:** On macOS, this method requires the "Screen Recording" permission. If permission is not granted, this method returns a screenshot that will not include other application windows or OS elements not related to the application.

---

<span id="class_DisplayServer_method_screen_get_image_rect"></span>

[Image](class_image.md#class_Image) **screen_get_image_rect** ( rect: [Rect2i](class_rect2i.md#class_Rect2i) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_image_rect)

Returns a screenshot of the screen region defined by `rect`. Returns `null` if `rect` is outside screen bounds or the **DisplayServer** fails to capture screenshot.

 **Note:** This method is implemented on macOS and Windows. On other platforms, this method always returns `null`.

 **Note:** On macOS, this method requires the "Screen Recording" permission. If permission is not granted, this method returns a screenshot that will not include other application windows or OS elements not related to the application.

---

<span id="class_DisplayServer_method_screen_get_max_scale"></span>

[float](class_float.md#class_float) **screen_get_max_scale** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_max_scale)

Returns the greatest scale factor of all screens.

 **Note:** On macOS returned value is `2.0` if there is at least one hiDPI (Retina) screen in the system, and `1.0` in all other cases.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_screen_get_orientation"></span>

[ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation) **screen_get_orientation** ( screen: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_orientation)

Returns the `screen`'s current orientation. See also [screen_set_orientation()](class_displayserver.md#class_DisplayServer_method_screen_set_orientation). Returns [SCREEN_LANDSCAPE](class_displayserver.md#class_DisplayServer_constant_SCREEN_LANDSCAPE) if `screen` is invalid.

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

 **Note:** This method is implemented on Android and iOS. On other platforms, this method always returns [SCREEN_LANDSCAPE](class_displayserver.md#class_DisplayServer_constant_SCREEN_LANDSCAPE).

---

<span id="class_DisplayServer_method_screen_get_pixel"></span>

[Color](class_color.md#class_Color) **screen_get_pixel** ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_pixel)

Returns the color of the pixel at the given screen `position`. On multi-monitor setups, the screen position is relative to the virtual desktop area.

 **Note:** This method is implemented on Linux (X11, excluding XWayland), macOS, and Windows. On other platforms, this method always returns `Color(0, 0, 0, 1)`.

 **Note:** On macOS, this method requires the "Screen Recording" permission. If permission is not granted, this method returns a color from a screenshot that will not include other application windows or OS elements not related to the application.

---

<span id="class_DisplayServer_method_screen_get_position"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **screen_get_position** ( screen: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_position)

Returns the screen's top-left corner position in pixels. Returns [Vector2i.ZERO](class_vector2i.md#class_Vector2i_constant_ZERO) if `screen` is invalid. On multi-monitor setups, the screen position is relative to the virtual desktop area. On multi-monitor setups with different screen resolutions or orientations, the origin might be located outside any display like this:

.. code:: text

    * (0, 0)        +-------+
                    |       |
    +-------------+ |       |
    |             | |       |
    |             | |       |
    +-------------+ +-------+

See also [screen_get_size()](class_displayserver.md#class_DisplayServer_method_screen_get_size).

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

---

<span id="class_DisplayServer_method_screen_get_refresh_rate"></span>

[float](class_float.md#class_float) **screen_get_refresh_rate** ( screen: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_refresh_rate)

Returns the current refresh rate of the specified screen. When V-Sync is enabled, this returns the maximum framerate the project can effectively reach. Returns `-1.0` if `screen` is invalid or the **DisplayServer** fails to find the refresh rate for the specified screen.

To fallback to a default refresh rate if the method fails, try:

::

    var refresh_rate = DisplayServer.screen_get_refresh_rate()
    if refresh_rate < 0:
        refresh_rate = 60.0

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

 **Note:** This method is implemented on Android, iOS, macOS, Linux (X11 and Wayland), and Windows. On other platforms, this method always returns `-1.0`.

---

<span id="class_DisplayServer_method_screen_get_scale"></span>

[float](class_float.md#class_float) **screen_get_scale** ( screen: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_scale)

Returns the scale factor of the specified screen by index. Returns `1.0` if `screen` is invalid.

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

 **Note:** On macOS, the returned value is `2.0` for hiDPI (Retina) screens, and `1.0` for all other cases.

 **Note:** On Linux (Wayland), the returned value is accurate only when `screen` is [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW). Due to API limitations, passing a direct index will return a rounded-up integer, if the screen has a fractional scale (e.g. `1.25` would get rounded up to `2.0`).

 **Note:** This method is implemented on Android, iOS, Web, macOS, and Linux (Wayland). On other platforms, this method always returns `1.0`.

---

<span id="class_DisplayServer_method_screen_get_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **screen_get_size** ( screen: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_size)

Returns the screen's size in pixels. See also [screen_get_position()](class_displayserver.md#class_DisplayServer_method_screen_get_position) and [screen_get_usable_rect()](class_displayserver.md#class_DisplayServer_method_screen_get_usable_rect). Returns [Vector2i.ZERO](class_vector2i.md#class_Vector2i_constant_ZERO) if `screen` is invalid.

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

---

<span id="class_DisplayServer_method_screen_get_usable_rect"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **screen_get_usable_rect** ( screen: [int](class_int.md#class_int) = -1 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_get_usable_rect)

Returns the portion of the screen that is not obstructed by a status bar in pixels. See also [screen_get_size()](class_displayserver.md#class_DisplayServer_method_screen_get_size).

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

 **Note:** This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns `Rect2i(screen_get_position(screen), screen_get_size(screen))`.

---

<span id="class_DisplayServer_method_screen_is_kept_on"></span>

[bool](class_bool.md#class_bool) **screen_is_kept_on** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_screen_is_kept_on)

Returns `true` if the screen should never be turned off by the operating system's power-saving measures. See also [screen_set_keep_on()](class_displayserver.md#class_DisplayServer_method_screen_set_keep_on).

---

<span id="class_DisplayServer_method_screen_set_keep_on"></span>

void **screen_set_keep_on** ( enable: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_screen_set_keep_on)

Sets whether the screen should never be turned off by the operating system's power-saving measures. See also [screen_is_kept_on()](class_displayserver.md#class_DisplayServer_method_screen_is_kept_on).

---

<span id="class_DisplayServer_method_screen_set_orientation"></span>

void **screen_set_orientation** ( orientation: [ScreenOrientation](class_displayserver.md#enum_DisplayServer_ScreenOrientation), screen: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_screen_set_orientation)

Sets the `screen`'s `orientation`. See also [screen_get_orientation()](class_displayserver.md#class_DisplayServer_method_screen_get_orientation).

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

 **Note:** This method is implemented on Android and iOS.

 **Note:** On iOS, this method has no effect if ProjectSettings.display/window/handheld/orientation is not set to [SCREEN_SENSOR](class_displayserver.md#class_DisplayServer_constant_SCREEN_SENSOR).

---

<span id="class_DisplayServer_method_set_hardware_keyboard_connection_change_callback"></span>

void **set_hardware_keyboard_connection_change_callback** ( callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_set_hardware_keyboard_connection_change_callback)

Sets the callback that should be called when a hardware keyboard is connected or disconnected. `callable` should accept a single [bool](class_bool.md#class_bool) argument indicating whether the keyboard has been connected (`true`) or disconnected (`false`).

 **Note:** This method is only implemented on Android.

---

<span id="class_DisplayServer_method_set_icon"></span>

void **set_icon** ( image: [Image](class_image.md#class_Image) ) [🔗](class_displayserver.md#class_DisplayServer_method_set_icon)

Sets the window icon (usually displayed in the top-left corner) with an [Image](class_image.md#class_Image). To use icons in the operating system's native format, use [set_native_icon()](class_displayserver.md#class_DisplayServer_method_set_native_icon) instead.

 **Note:** Requires support for [FEATURE_ICON](class_displayserver.md#class_DisplayServer_constant_FEATURE_ICON).

---

<span id="class_DisplayServer_method_set_native_icon"></span>

void **set_native_icon** ( filename: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_set_native_icon)

Sets the window icon (usually displayed in the top-left corner) in the operating system's *native* format. The file at `filename` must be in `.ico` format on Windows or `.icns` on macOS. By using specially crafted `.ico` or `.icns` icons, [set_native_icon()](class_displayserver.md#class_DisplayServer_method_set_native_icon) allows specifying different icons depending on the size the icon is displayed at. This size is determined by the operating system and user preferences (including the display scale factor). To use icons in other formats, use [set_icon()](class_displayserver.md#class_DisplayServer_method_set_icon) instead.

 **Note:** Requires support for [FEATURE_NATIVE_ICON](class_displayserver.md#class_DisplayServer_constant_FEATURE_NATIVE_ICON).

---

<span id="class_DisplayServer_method_set_system_theme_change_callback"></span>

void **set_system_theme_change_callback** ( callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_set_system_theme_change_callback)

Sets the callback that should be called when the system's theme settings are changed. `callable` should accept zero arguments.

 **Note:** This method is implemented on Android, iOS, macOS, Windows, and Linux (X11/Wayland).

---

<span id="class_DisplayServer_method_show_emoji_and_symbol_picker"></span>

void **show_emoji_and_symbol_picker** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_show_emoji_and_symbol_picker)

Opens system emoji and symbol picker.

 **Note:** This method is implemented on macOS and Windows.

---

<span id="class_DisplayServer_method_status_indicator_get_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **status_indicator_get_rect** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_status_indicator_get_rect)

Returns the rectangle for the given status indicator `id` in screen coordinates. If the status indicator is not visible, returns an empty [Rect2](class_rect2.md#class_Rect2).

 **Note:** This method is implemented on macOS and Windows.

---

<span id="class_DisplayServer_method_status_indicator_set_callback"></span>

void **status_indicator_set_callback** ( id: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_status_indicator_set_callback)

Sets the application status indicator activation callback. `callback` should take two arguments: [int](class_int.md#class_int) mouse button index (one of MouseButton values) and [Vector2i](class_vector2i.md#class_Vector2i) click position in screen coordinates.

 **Note:** This method is implemented on macOS and Windows.

---

<span id="class_DisplayServer_method_status_indicator_set_icon"></span>

void **status_indicator_set_icon** ( id: [int](class_int.md#class_int), icon: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_displayserver.md#class_DisplayServer_method_status_indicator_set_icon)

Sets the application status indicator icon.

 **Note:** This method is implemented on macOS and Windows.

---

<span id="class_DisplayServer_method_status_indicator_set_menu"></span>

void **status_indicator_set_menu** ( id: [int](class_int.md#class_int), menu_rid: [RID](class_rid.md#class_RID) ) [🔗](class_displayserver.md#class_DisplayServer_method_status_indicator_set_menu)

Sets the application status indicator native popup menu.

 **Note:** On macOS, the menu is activated by any mouse button. Its activation callback is *not* triggered.

 **Note:** On Windows, the menu is activated by the right mouse button, selecting the status icon and pressing :kbd:`Shift + F10`, or the applications key. The menu's activation callback for the other mouse buttons is still triggered.

 **Note:** Native popup is only supported if [NativeMenu](class_nativemenu.md#class_NativeMenu) supports the [NativeMenu.FEATURE_POPUP_MENU](class_nativemenu.md#class_NativeMenu_constant_FEATURE_POPUP_MENU) feature.

---

<span id="class_DisplayServer_method_status_indicator_set_tooltip"></span>

void **status_indicator_set_tooltip** ( id: [int](class_int.md#class_int), tooltip: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_status_indicator_set_tooltip)

Sets the application status indicator tooltip.

 **Note:** This method is implemented on macOS and Windows.

---

<span id="class_DisplayServer_method_tablet_get_current_driver"></span>

[String](class_string.md#class_String) **tablet_get_current_driver** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_tablet_get_current_driver)

Returns current active tablet driver name.

 **Note:** This method is implemented only on Windows.

---

<span id="class_DisplayServer_method_tablet_get_driver_count"></span>

[int](class_int.md#class_int) **tablet_get_driver_count** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_tablet_get_driver_count)

Returns the total number of available tablet drivers.

 **Note:** This method is implemented only on Windows.

---

<span id="class_DisplayServer_method_tablet_get_driver_name"></span>

[String](class_string.md#class_String) **tablet_get_driver_name** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_tablet_get_driver_name)

Returns the tablet driver name for the given index.

 **Note:** This method is implemented only on Windows.

---

<span id="class_DisplayServer_method_tablet_set_current_driver"></span>

void **tablet_set_current_driver** ( name: [String](class_string.md#class_String) ) [🔗](class_displayserver.md#class_DisplayServer_method_tablet_set_current_driver)

Set active tablet driver name.

Supported drivers:

- `winink`: Windows Ink API, default.

- `wintab`: Wacom Wintab API (compatible device driver required).

- `dummy`: Dummy driver, tablet input is disabled.

 **Note:** This method is implemented only on Windows.

---

<span id="class_DisplayServer_method_tts_get_voices"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **tts_get_voices** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_tts_get_voices)

Returns an [Array](class_array.md#class_Array) of voice information dictionaries.

Each [Dictionary](class_dictionary.md#class_Dictionary) contains two [String](class_string.md#class_String) entries:

- `name` is voice name.

- `id` is voice identifier.

- `language` is language code in `lang_Variant` format. The `lang` part is a 2 or 3-letter code based on the ISO-639 standard, in lowercase. The `Variant` part is an engine-dependent string describing country, region or/and dialect.

Note that Godot depends on system libraries for text-to-speech functionality. These libraries are installed by default on Windows and macOS, but not on all Linux distributions. If they are not present, this method will return an empty list. This applies to both Godot users on Linux, as well as end-users on Linux running Godot games that use text-to-speech.

 **Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_tts_get_voices_for_language"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **tts_get_voices_for_language** ( language: [String](class_string.md#class_String) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_tts_get_voices_for_language)

Returns a [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) of voice identifiers for the `language`.

 **Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_tts_is_paused"></span>

[bool](class_bool.md#class_bool) **tts_is_paused** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_tts_is_paused)

Returns `true` if the synthesizer is in a paused state.

 **Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_tts_is_speaking"></span>

[bool](class_bool.md#class_bool) **tts_is_speaking** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_tts_is_speaking)

Returns `true` if the synthesizer is generating speech, or have utterance waiting in the queue.

 **Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_tts_pause"></span>

void **tts_pause** ( ) [🔗](class_displayserver.md#class_DisplayServer_method_tts_pause)

Puts the synthesizer into a paused state.

 **Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_tts_resume"></span>

void **tts_resume** ( ) [🔗](class_displayserver.md#class_DisplayServer_method_tts_resume)

Resumes the synthesizer if it was paused.

 **Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_tts_set_utterance_callback"></span>

void **tts_set_utterance_callback** ( event: [TTSUtteranceEvent](class_displayserver.md#enum_DisplayServer_TTSUtteranceEvent), callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_displayserver.md#class_DisplayServer_method_tts_set_utterance_callback)

Adds a callback, which is called when the utterance has started, finished, canceled or reached a text boundary.

- [TTS_UTTERANCE_STARTED](class_displayserver.md#class_DisplayServer_constant_TTS_UTTERANCE_STARTED), [TTS_UTTERANCE_ENDED](class_displayserver.md#class_DisplayServer_constant_TTS_UTTERANCE_ENDED), and [TTS_UTTERANCE_CANCELED](class_displayserver.md#class_DisplayServer_constant_TTS_UTTERANCE_CANCELED) callable's method should take one [int](class_int.md#class_int) parameter, the utterance ID.

- [TTS_UTTERANCE_BOUNDARY](class_displayserver.md#class_DisplayServer_constant_TTS_UTTERANCE_BOUNDARY) callable's method should take two [int](class_int.md#class_int) parameters, the index of the character and the utterance ID.

 **Note:** The granularity of the boundary callbacks is engine dependent.

 **Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_tts_speak"></span>

void **tts_speak** ( text: [String](class_string.md#class_String), voice: [String](class_string.md#class_String), volume: [int](class_int.md#class_int) = 50, pitch: [float](class_float.md#class_float) = 1.0, rate: [float](class_float.md#class_float) = 1.0, utterance_id: [int](class_int.md#class_int) = 0, interrupt: [bool](class_bool.md#class_bool) = false ) [🔗](class_displayserver.md#class_DisplayServer_method_tts_speak)

Adds an utterance to the queue. If `interrupt` is `true`, the queue is cleared first.

- `voice` identifier is one of the `"id"` values returned by [tts_get_voices()](class_displayserver.md#class_DisplayServer_method_tts_get_voices) or one of the values returned by [tts_get_voices_for_language()](class_displayserver.md#class_DisplayServer_method_tts_get_voices_for_language).

- `volume` ranges from `0` (lowest) to `100` (highest).

- `pitch` ranges from `0.0` (lowest) to `2.0` (highest), `1.0` is default pitch for the current voice.

- `rate` ranges from `0.1` (lowest) to `10.0` (highest), `1.0` is a normal speaking rate. Other values act as a percentage relative.

- `utterance_id` is passed as a parameter to the callback functions.

 **Note:** On Windows and Linux (X11/Wayland), utterance `text` can use SSML markup. SSML support is engine and voice dependent. If the engine does not support SSML, you should strip out all XML markup before calling [tts_speak()](class_displayserver.md#class_DisplayServer_method_tts_speak).

 **Note:** The granularity of pitch, rate, and volume is engine and voice dependent. Values may be truncated.

 **Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_tts_stop"></span>

void **tts_stop** ( ) [🔗](class_displayserver.md#class_DisplayServer_method_tts_stop)

Stops synthesis in progress and removes all utterances from the queue.

 **Note:** This method is implemented on Android, iOS, Web, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_unregister_additional_output"></span>

void **unregister_additional_output** ( object: [Object](class_object.md#class_Object) ) [🔗](class_displayserver.md#class_DisplayServer_method_unregister_additional_output)

Unregisters an [Object](class_object.md#class_Object) representing an additional output, that was registered via [register_additional_output()](class_displayserver.md#class_DisplayServer_method_register_additional_output).

---

<span id="class_DisplayServer_method_virtual_keyboard_get_height"></span>

[int](class_int.md#class_int) **virtual_keyboard_get_height** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_virtual_keyboard_get_height)

Returns the on-screen keyboard's height in pixels. Returns `0` if there is no keyboard or if it is currently hidden.

 **Note:** On Android 7 and 8, the keyboard height may return `0` the first time the keyboard is opened in non-immersive mode. This behavior does not occur in immersive mode.

---

<span id="class_DisplayServer_method_virtual_keyboard_hide"></span>

void **virtual_keyboard_hide** ( ) [🔗](class_displayserver.md#class_DisplayServer_method_virtual_keyboard_hide)

Hides the virtual keyboard if it is shown, does nothing otherwise.

---

<span id="class_DisplayServer_method_virtual_keyboard_show"></span>

void **virtual_keyboard_show** ( existing_text: [String](class_string.md#class_String), position: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), type: [VirtualKeyboardType](class_displayserver.md#enum_DisplayServer_VirtualKeyboardType) = 0, max_length: [int](class_int.md#class_int) = -1, cursor_start: [int](class_int.md#class_int) = -1, cursor_end: [int](class_int.md#class_int) = -1 ) [🔗](class_displayserver.md#class_DisplayServer_method_virtual_keyboard_show)

Shows the virtual keyboard if the platform has one.

 `existing_text` parameter is useful for implementing your own [LineEdit](class_lineedit.md#class_LineEdit) or [TextEdit](class_textedit.md#class_TextEdit), as it tells the virtual keyboard what text has already been typed (the virtual keyboard uses it for auto-correct and predictions).

 `position` parameter is the screen space [Rect2](class_rect2.md#class_Rect2) of the edited text.

 `type` parameter allows configuring which type of virtual keyboard to show.

 `max_length` limits the number of characters that can be entered if different from `-1`.

 `cursor_start` can optionally define the current text cursor position if `cursor_end` is not set.

 `cursor_start` and `cursor_end` can optionally define the current text selection.

 **Note:** This method is implemented on Android, iOS and Web.

---

<span id="class_DisplayServer_method_warp_mouse"></span>

void **warp_mouse** ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_displayserver.md#class_DisplayServer_method_warp_mouse)

Sets the mouse cursor position to the given `position` relative to an origin at the upper left corner of the currently focused game Window Manager window.

 **Note:** [warp_mouse()](class_displayserver.md#class_DisplayServer_method_warp_mouse) is only supported on Windows, macOS, and Linux (X11/Wayland). It has no effect on Android, iOS, and Web.

---

<span id="class_DisplayServer_method_window_can_draw"></span>

[bool](class_bool.md#class_bool) **window_can_draw** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_can_draw)

Returns `true` if anything can be drawn in the window specified by `window_id`, `false` otherwise. Using the `--disable-render-loop` command line argument or a headless build will return `false`.

---

<span id="class_DisplayServer_method_window_get_active_popup"></span>

[int](class_int.md#class_int) **window_get_active_popup** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_active_popup)

Returns ID of the active popup window, or [INVALID_WINDOW_ID](class_displayserver.md#class_DisplayServer_constant_INVALID_WINDOW_ID) if there is none.

---

<span id="class_DisplayServer_method_window_get_attached_instance_id"></span>

[int](class_int.md#class_int) **window_get_attached_instance_id** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_attached_instance_id)

Returns the [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id) of the [Window](class_window.md#class_Window) the `window_id` is attached to.

---

<span id="class_DisplayServer_method_window_get_current_screen"></span>

[int](class_int.md#class_int) **window_get_current_screen** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_current_screen)

Returns the screen the window specified by `window_id` is currently positioned on. If the screen overlaps multiple displays, the screen where the window's center is located is returned. See also [window_set_current_screen()](class_displayserver.md#class_DisplayServer_method_window_set_current_screen). Returns [INVALID_SCREEN](class_displayserver.md#class_DisplayServer_constant_INVALID_SCREEN) if `window_id` is invalid.

 **Note:** This method is implemented on Linux/X11, macOS, and Windows. On other platforms, this method always returns `0`.

---

<span id="class_DisplayServer_method_window_get_flag"></span>

[bool](class_bool.md#class_bool) **window_get_flag** ( flag: [WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags), window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_flag)

Returns the current value of the given window's `flag`.

---

<span id="class_DisplayServer_method_window_get_hdr_output_current_max_luminance"></span>

[float](class_float.md#class_float) **window_get_hdr_output_current_max_luminance** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_max_luminance)

**Experimental:** This method may be changed or removed in future versions.

When [window_is_hdr_output_enabled()](class_displayserver.md#class_DisplayServer_method_window_is_hdr_output_enabled) returns `true`, this returns the current maximum luminance in nits (cd/m²) for HDR output by the window specified by `window_id`. If the maximum luminance is being automatically adjusted based on the screen's capabilities, this method will return that value. Otherwise, it will return the value set by [window_set_hdr_output_max_luminance()](class_displayserver.md#class_DisplayServer_method_window_set_hdr_output_max_luminance). This maximum luminance value is used when calculating [window_get_output_max_linear_value()](class_displayserver.md#class_DisplayServer_method_window_get_output_max_linear_value).

 **Note:** This maximum luminance may not match the physical behavior of the screen, but will always be proportionally correct relative to [window_get_hdr_output_current_reference_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_reference_luminance).

---

<span id="class_DisplayServer_method_window_get_hdr_output_current_reference_luminance"></span>

[float](class_float.md#class_float) **window_get_hdr_output_current_reference_luminance** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_reference_luminance)

When [window_is_hdr_output_enabled()](class_displayserver.md#class_DisplayServer_method_window_is_hdr_output_enabled) returns `true`, this returns the current reference white luminance in nits (cd/m²) for HDR output by the window specified by `window_id`. If the reference luminance is being automatically adjusted to match the operating system brightness, this will return that value. Otherwise, it will return the value set by [window_set_hdr_output_reference_luminance()](class_displayserver.md#class_DisplayServer_method_window_set_hdr_output_reference_luminance). This reference luminance value is used when calculating [window_get_output_max_linear_value()](class_displayserver.md#class_DisplayServer_method_window_get_output_max_linear_value).

 **Note:** This reference white luminance may not match the physical behavior of the screen, but will always be proportionally correct relative to [window_get_hdr_output_current_max_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_max_luminance).

---

<span id="class_DisplayServer_method_window_get_hdr_output_max_luminance"></span>

[float](class_float.md#class_float) **window_get_hdr_output_max_luminance** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_max_luminance)

**Experimental:** This method may be changed or removed in future versions.

Returns the maximum luminance in nits (cd/m²) set for HDR output by the window specified by `window_id`. Negative values indicate that the value is being automatically adjusted based on the screen's capabilities. See also [window_get_hdr_output_current_max_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_max_luminance).

---

<span id="class_DisplayServer_method_window_get_hdr_output_reference_luminance"></span>

[float](class_float.md#class_float) **window_get_hdr_output_reference_luminance** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_reference_luminance)

Returns the reference white luminance in nits (cd/m²) set for HDR output by the window specified by `window_id`. Negative values indicate that the value is being automatically adjusted to match the operating system brightness. See also [window_get_hdr_output_current_reference_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_reference_luminance).

---

<span id="class_DisplayServer_method_window_get_max_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **window_get_max_size** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_max_size)

Returns the window's maximum size (in pixels). See also [window_set_max_size()](class_displayserver.md#class_DisplayServer_method_window_set_max_size).

---

<span id="class_DisplayServer_method_window_get_min_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **window_get_min_size** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_min_size)

Returns the window's minimum size (in pixels). See also [window_set_min_size()](class_displayserver.md#class_DisplayServer_method_window_set_min_size).

---

<span id="class_DisplayServer_method_window_get_mode"></span>

[WindowMode](class_displayserver.md#enum_DisplayServer_WindowMode) **window_get_mode** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_mode)

Returns the mode of the given window.

---

<span id="class_DisplayServer_method_window_get_native_handle"></span>

[int](class_int.md#class_int) **window_get_native_handle** ( handle_type: [HandleType](class_displayserver.md#enum_DisplayServer_HandleType), window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_native_handle)

Returns internal structure pointers for use in plugins.

 **Note:** This method is implemented on Android, Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_window_get_output_max_linear_value"></span>

[float](class_float.md#class_float) **window_get_output_max_linear_value** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_output_max_linear_value)

Returns the maximum value for linear color components that can be displayed for the window specified by `window_id`, regardless of SDR or HDR output. Returns `1.0` if HDR is not enabled or not supported. When HDR output is enabled, this is calculated based on [window_get_hdr_output_current_reference_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_reference_luminance) and [window_get_hdr_output_current_max_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_max_luminance). This value is used by tonemapping and other [Environment](class_environment.md#class_Environment) effects to ensure that bright colors are presented in the range that can be displayed by this window. Corresponds to [Window.get_output_max_linear_value()](class_window.md#class_Window_method_get_output_max_linear_value).

---

<span id="class_DisplayServer_method_window_get_popup_safe_rect"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **window_get_popup_safe_rect** ( window: [int](class_int.md#class_int) ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_popup_safe_rect)

Returns the bounding box of control, or menu item that was used to open the popup window, in the screen coordinate system.

---

<span id="class_DisplayServer_method_window_get_position"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **window_get_position** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_position)

Returns the position of the client area of the given window on the screen.

---

<span id="class_DisplayServer_method_window_get_position_with_decorations"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **window_get_position_with_decorations** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_position_with_decorations)

Returns the position of the given window on the screen including the borders drawn by the operating system. See also [window_get_position()](class_displayserver.md#class_DisplayServer_method_window_get_position).

---

<span id="class_DisplayServer_method_window_get_safe_title_margins"></span>

[Vector3i](class_vector3i.md#class_Vector3i) **window_get_safe_title_margins** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_safe_title_margins)

Returns left margins (`x`), right margins (`y`) and height (`z`) of the title that are safe to use (contains no buttons or other elements) when [WINDOW_FLAG_EXTEND_TO_TITLE](class_displayserver.md#class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE) flag is set.

---

<span id="class_DisplayServer_method_window_get_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **window_get_size** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_size)

Returns the size of the window specified by `window_id` (in pixels), excluding the borders drawn by the operating system. This is also called the "client area". See also [window_get_size_with_decorations()](class_displayserver.md#class_DisplayServer_method_window_get_size_with_decorations), [window_set_size()](class_displayserver.md#class_DisplayServer_method_window_set_size) and [window_get_position()](class_displayserver.md#class_DisplayServer_method_window_get_position).

---

<span id="class_DisplayServer_method_window_get_size_with_decorations"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **window_get_size_with_decorations** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_size_with_decorations)

Returns the size of the window specified by `window_id` (in pixels), including the borders drawn by the operating system. See also [window_get_size()](class_displayserver.md#class_DisplayServer_method_window_get_size).

---

<span id="class_DisplayServer_method_window_get_title_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **window_get_title_size** ( title: [String](class_string.md#class_String), window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_title_size)

Returns the estimated window title bar size (including text and window buttons) for the window specified by `window_id` (in pixels). This method does not change the window title.

 **Note:** This method is implemented on macOS and Windows.

---

<span id="class_DisplayServer_method_window_get_vsync_mode"></span>

[VSyncMode](class_displayserver.md#enum_DisplayServer_VSyncMode) **window_get_vsync_mode** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_get_vsync_mode)

Returns the V-Sync mode of the given window.

---

<span id="class_DisplayServer_method_window_is_focused"></span>

[bool](class_bool.md#class_bool) **window_is_focused** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_is_focused)

Returns `true` if the window specified by `window_id` is focused.

---

<span id="class_DisplayServer_method_window_is_hdr_output_enabled"></span>

[bool](class_bool.md#class_bool) **window_is_hdr_output_enabled** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_is_hdr_output_enabled)

Returns `true` if HDR output is currently enabled for the window specified by `window_id`. The returned value may change dynamically based on system settings, screen capabilities, and which screen the window is currently on.

---

<span id="class_DisplayServer_method_window_is_hdr_output_requested"></span>

[bool](class_bool.md#class_bool) **window_is_hdr_output_requested** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_is_hdr_output_requested)

Returns `true` if HDR output is requested for the window specified by `window_id`. Corresponds to [Window.hdr_output_requested](class_window.md#class_Window_property_hdr_output_requested).

---

<span id="class_DisplayServer_method_window_is_hdr_output_supported"></span>

[bool](class_bool.md#class_bool) **window_is_hdr_output_supported** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_is_hdr_output_supported)

Returns `true` if the window specified by `window_id` supports HDR output. This depends on the platform, screen capabilities, system settings, and the screen the window is currently on.

---

<span id="class_DisplayServer_method_window_is_maximize_allowed"></span>

[bool](class_bool.md#class_bool) **window_is_maximize_allowed** ( window_id: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_is_maximize_allowed)

Returns `true` if the given window can be maximized (the maximize button is enabled).

---

<span id="class_DisplayServer_method_window_maximize_on_title_dbl_click"></span>

[bool](class_bool.md#class_bool) **window_maximize_on_title_dbl_click** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_maximize_on_title_dbl_click)

Returns `true` if double-clicking on a window's title should maximize it.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_window_minimize_on_title_dbl_click"></span>

[bool](class_bool.md#class_bool) **window_minimize_on_title_dbl_click** ( ) *const* [🔗](class_displayserver.md#class_DisplayServer_method_window_minimize_on_title_dbl_click)

Returns `true` if double-clicking on a window's title should minimize it.

 **Note:** This method is implemented only on macOS.

---

<span id="class_DisplayServer_method_window_move_to_foreground"></span>

void **window_move_to_foreground** ( window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_move_to_foreground)

Moves the window specified by `window_id` to the foreground, so that it is visible over other windows.

---

<span id="class_DisplayServer_method_window_request_attention"></span>

void **window_request_attention** ( window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_request_attention)

Makes the window specified by `window_id` request attention, which is materialized by the window title and taskbar entry blinking until the window is focused. This usually has no visible effect if the window is currently focused. The exact behavior varies depending on the operating system.

---

<span id="class_DisplayServer_method_window_request_hdr_output"></span>

void **window_request_hdr_output** ( enable: [bool](class_bool.md#class_bool), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_request_hdr_output)

If `enable` is `true`, HDR output is requested for the window specified by `window_id`. The window will automatically switch between HDR and SDR if it is moved between screens, screen capabilities change, or system settings are modified. This will internally force [Viewport.use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d) to be enabled on the main [Viewport](class_viewport.md#class_Viewport). All other [SubViewport](class_subviewport.md#class_SubViewport) of the [Window](class_window.md#class_Window) must have their [Viewport.use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d) property enabled to produce HDR output. Corresponds to [Window.hdr_output_requested](class_window.md#class_Window_property_hdr_output_requested).

---

<span id="class_DisplayServer_method_window_set_color"></span>

void **window_set_color** ( color: [Color](class_color.md#class_Color) ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_color)

Sets the background color of the root window.

 **Note:** This method is implemented only on Android.

---

<span id="class_DisplayServer_method_window_set_current_screen"></span>

void **window_set_current_screen** ( screen: [int](class_int.md#class_int), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_current_screen)

Moves the window specified by `window_id` to the specified `screen`. See also [window_get_current_screen()](class_displayserver.md#class_DisplayServer_method_window_get_current_screen).

 **Note:** One of the following constants can be used as `screen`: [SCREEN_OF_MAIN_WINDOW](class_displayserver.md#class_DisplayServer_constant_SCREEN_OF_MAIN_WINDOW), [SCREEN_PRIMARY](class_displayserver.md#class_DisplayServer_constant_SCREEN_PRIMARY), [SCREEN_WITH_MOUSE_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_MOUSE_FOCUS), or [SCREEN_WITH_KEYBOARD_FOCUS](class_displayserver.md#class_DisplayServer_constant_SCREEN_WITH_KEYBOARD_FOCUS).

 **Note:** This method is implemented on Linux/X11, macOS, and Windows.

---

<span id="class_DisplayServer_method_window_set_drop_files_callback"></span>

void **window_set_drop_files_callback** ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_drop_files_callback)

Sets the `callback` that should be called when files are dropped from the operating system's file manager to the window specified by `window_id`. `callback` should take one [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) argument, which is the list of dropped files.

 **Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class_Window) node will override its default implementation, which can introduce bugs.

 **Note:** This method is implemented on Windows, macOS, Linux (X11/Wayland), and Web.

---

<span id="class_DisplayServer_method_window_set_exclusive"></span>

void **window_set_exclusive** ( window_id: [int](class_int.md#class_int), exclusive: [bool](class_bool.md#class_bool) ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_exclusive)

If set to `true`, this window will always stay on top of its parent window, parent window will ignore input while this window is opened.

 **Note:** On macOS, exclusive windows are confined to the same space (virtual desktop or screen) as the parent window.

 **Note:** This method is implemented on macOS and Windows.

---

<span id="class_DisplayServer_method_window_set_flag"></span>

void **window_set_flag** ( flag: [WindowFlags](class_displayserver.md#enum_DisplayServer_WindowFlags), enabled: [bool](class_bool.md#class_bool), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_flag)

Enables or disables the given window's given `flag`.

---

<span id="class_DisplayServer_method_window_set_hdr_output_max_luminance"></span>

void **window_set_hdr_output_max_luminance** ( max_luminance: [float](class_float.md#class_float), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_hdr_output_max_luminance)

**Experimental:** This method may be changed or removed in future versions.

Sets the maximum luminance in nits (cd/m²) for HDR output by the window specified by `window_id`. If `max_luminance` is negative, the window uses the screen's maximum luminance that is reported by the operating system. By default, this luminance is set to `-1.0` for every window. Typically this property should be left at this default value, but may optionally be exposed through in-game settings to allow the player to correct an inaccurate maximum luminance reported by the operating system. See also [window_get_hdr_output_current_max_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_max_luminance) and [window_get_hdr_output_max_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_max_luminance).

---

<span id="class_DisplayServer_method_window_set_hdr_output_reference_luminance"></span>

void **window_set_hdr_output_reference_luminance** ( reference_luminance: [float](class_float.md#class_float), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_hdr_output_reference_luminance)

Sets the reference white luminance in nits (cd/m²) for HDR output by the window specified by `window_id`. If `reference_luminance` is negative, the window automatically adjusts to the brightness set by the operating system. By default, this luminance is set to `-1.0` for every window. Typically this property should be left at this default value, but may optionally be exposed as an "HDR Brightness" in-game setting to allow the player to adjust the brightness of their game, independently of their device settings. See also [window_get_hdr_output_current_reference_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_current_reference_luminance) and [window_get_hdr_output_reference_luminance()](class_displayserver.md#class_DisplayServer_method_window_get_hdr_output_reference_luminance).

---

<span id="class_DisplayServer_method_window_set_ime_active"></span>

void **window_set_ime_active** ( active: [bool](class_bool.md#class_bool), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_ime_active)

Sets whether Input Method Editor should be enabled for the window specified by `window_id`. See also [window_set_ime_position()](class_displayserver.md#class_DisplayServer_method_window_set_ime_position).

---

<span id="class_DisplayServer_method_window_set_ime_position"></span>

void **window_set_ime_position** ( position: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_ime_position)

Sets the position of the Input Method Editor popup for the specified `window_id`. Only effective if [window_set_ime_active()](class_displayserver.md#class_DisplayServer_method_window_set_ime_active) was set to `true` for the specified `window_id`.

---

<span id="class_DisplayServer_method_window_set_input_event_callback"></span>

void **window_set_input_event_callback** ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_input_event_callback)

Sets the `callback` that should be called when any [InputEvent](class_inputevent.md#class_InputEvent) is sent to the window specified by `window_id`.

 **Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class_Window) node will override its default implementation, which can introduce bugs.

---

<span id="class_DisplayServer_method_window_set_input_text_callback"></span>

void **window_set_input_text_callback** ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_input_text_callback)

Sets the `callback` that should be called when text is entered using the virtual keyboard to the window specified by `window_id`.

 **Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class_Window) node will override its default implementation, which can introduce bugs.

---

<span id="class_DisplayServer_method_window_set_max_size"></span>

void **window_set_max_size** ( max_size: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_max_size)

Sets the maximum size of the window specified by `window_id` in pixels. Normally, the user will not be able to drag the window to make it larger than the specified size. See also [window_get_max_size()](class_displayserver.md#class_DisplayServer_method_window_get_max_size).

 **Note:** It's recommended to change this value using [Window.max_size](class_window.md#class_Window_property_max_size) instead.

 **Note:** Using third-party tools, it is possible for users to disable window geometry restrictions and therefore bypass this limit.

---

<span id="class_DisplayServer_method_window_set_min_size"></span>

void **window_set_min_size** ( min_size: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_min_size)

Sets the minimum size for the given window to `min_size` in pixels. Normally, the user will not be able to drag the window to make it smaller than the specified size. See also [window_get_min_size()](class_displayserver.md#class_DisplayServer_method_window_get_min_size).

 **Note:** It's recommended to change this value using [Window.min_size](class_window.md#class_Window_property_min_size) instead.

 **Note:** By default, the main window has a minimum size of `Vector2i(64, 64)`. This prevents issues that can arise when the window is resized to a near-zero size.

 **Note:** Using third-party tools, it is possible for users to disable window geometry restrictions and therefore bypass this limit.

---

<span id="class_DisplayServer_method_window_set_mode"></span>

void **window_set_mode** ( mode: [WindowMode](class_displayserver.md#enum_DisplayServer_WindowMode), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_mode)

Sets window mode for the given window to `mode`.

 **Note:** On Android, setting it to [WINDOW_MODE_FULLSCREEN](class_displayserver.md#class_DisplayServer_constant_WINDOW_MODE_FULLSCREEN) or [WINDOW_MODE_EXCLUSIVE_FULLSCREEN](class_displayserver.md#class_DisplayServer_constant_WINDOW_MODE_EXCLUSIVE_FULLSCREEN) will enable immersive mode.

 **Note:** Setting the window to full screen forcibly sets the borderless flag to `true`, so make sure to set it back to `false` when not wanted.

---

<span id="class_DisplayServer_method_window_set_mouse_passthrough"></span>

void **window_set_mouse_passthrough** ( region: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_mouse_passthrough)

Sets a polygonal region of the window which accepts mouse events. Mouse events outside the region will be passed through.

Passing an empty array will disable passthrough support (all mouse events will be intercepted by the window, which is the default behavior).

.. tabs::

```
```

    # Set region, using Path2D node.
    DisplayServer.window_set_mouse_passthrough($Path2D.curve.get_baked_points())

    # Set region, using Polygon2D node.
    DisplayServer.window_set_mouse_passthrough($Polygon2D.polygon)

    # Reset region to default.
    DisplayServer.window_set_mouse_passthrough([])

```
```

    // Set region, using Path2D node.
    DisplayServer.WindowSetMousePassthrough(GetNode<Path2D>("Path2D").Curve.GetBakedPoints());

    // Set region, using Polygon2D node.
    DisplayServer.WindowSetMousePassthrough(GetNode<Polygon2D>("Polygon2D").Polygon);

    // Reset region to default.
    DisplayServer.WindowSetMousePassthrough([]);

 **Note:** On Windows, the portion of a window that lies outside the region is not drawn, while on Linux (X11) and macOS it is.

 **Note:** This method is implemented on Linux (X11), macOS and Windows.

---

<span id="class_DisplayServer_method_window_set_popup_safe_rect"></span>

void **window_set_popup_safe_rect** ( window: [int](class_int.md#class_int), rect: [Rect2i](class_rect2i.md#class_Rect2i) ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_popup_safe_rect)

Sets the bounding box of control, or menu item that was used to open the popup window, in the screen coordinate system. Clicking this area will not auto-close this popup.

---

<span id="class_DisplayServer_method_window_set_position"></span>

void **window_set_position** ( position: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_position)

Sets the position of the given window to `position`. On multi-monitor setups, the screen position is relative to the virtual desktop area. On multi-monitor setups with different screen resolutions or orientations, the origin may be located outside any display like this:

.. code:: text

    * (0, 0)        +-------+
                    |       |
    +-------------+ |       |
    |             | |       |
    |             | |       |
    +-------------+ +-------+

See also [window_get_position()](class_displayserver.md#class_DisplayServer_method_window_get_position) and [window_set_size()](class_displayserver.md#class_DisplayServer_method_window_set_size).

 **Note:** It's recommended to change this value using [Window.position](class_window.md#class_Window_property_position) instead.

 **Note:** On Linux (Wayland): this method is a no-op.

---

<span id="class_DisplayServer_method_window_set_rect_changed_callback"></span>

void **window_set_rect_changed_callback** ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_rect_changed_callback)

Sets the `callback` that will be called when the window specified by `window_id` is moved or resized.

 **Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class_Window) node will override its default implementation, which can introduce bugs.

---

<span id="class_DisplayServer_method_window_set_size"></span>

void **window_set_size** ( size: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_size)

Sets the size of the given window to `size` (in pixels). See also [window_get_size()](class_displayserver.md#class_DisplayServer_method_window_get_size) and [window_get_position()](class_displayserver.md#class_DisplayServer_method_window_get_position).

 **Note:** It's recommended to change this value using [Window.size](class_window.md#class_Window_property_size) instead.

---

<span id="class_DisplayServer_method_window_set_title"></span>

void **window_set_title** ( title: [String](class_string.md#class_String), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_title)

Sets the title of the given window to `title`.

 **Note:** It's recommended to change this value using [Window.title](class_window.md#class_Window_property_title) instead.

 **Note:** Avoid changing the window title every frame, as this can cause performance issues on certain window managers. Try to change the window title only a few times per second at most.

---

<span id="class_DisplayServer_method_window_set_transient"></span>

void **window_set_transient** ( window_id: [int](class_int.md#class_int), parent_window_id: [int](class_int.md#class_int) ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_transient)

Sets window transient parent. Transient window will be destroyed with its transient parent and will return focus to their parent when closed. The transient window is displayed on top of a non-exclusive full-screen parent window. Transient windows can't enter full-screen mode.

 **Note:** It's recommended to change this value using [Window.transient](class_window.md#class_Window_property_transient) instead.

 **Note:** The behavior might be different depending on the platform.

---

<span id="class_DisplayServer_method_window_set_vsync_mode"></span>

void **window_set_vsync_mode** ( vsync_mode: [VSyncMode](class_displayserver.md#enum_DisplayServer_VSyncMode), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_vsync_mode)

Sets the V-Sync mode of the given window. See also ProjectSettings.display/window/vsync/vsync_mode.

Depending on the platform and used renderer, the engine will fall back to [VSYNC_ENABLED](class_displayserver.md#class_DisplayServer_constant_VSYNC_ENABLED) if the desired mode is not supported.

 **Note:** V-Sync modes other than [VSYNC_ENABLED](class_displayserver.md#class_DisplayServer_constant_VSYNC_ENABLED) are only supported in the Forward+ and Mobile rendering methods, not Compatibility.

---

<span id="class_DisplayServer_method_window_set_window_buttons_offset"></span>

void **window_set_window_buttons_offset** ( offset: [Vector2i](class_vector2i.md#class_Vector2i), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_window_buttons_offset)

When [WINDOW_FLAG_EXTEND_TO_TITLE](class_displayserver.md#class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE) flag is set, set offset to the center of the first titlebar button.

 **Note:** This flag is implemented only on macOS.

---

<span id="class_DisplayServer_method_window_set_window_event_callback"></span>

void **window_set_window_event_callback** ( callback: [Callable](class_callable.md#class_Callable), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_set_window_event_callback)

Sets the `callback` that will be called when an event occurs in the window specified by `window_id`.

 **Warning:** Advanced users only! Adding such a callback to a [Window](class_window.md#class_Window) node will override its default implementation, which can introduce bugs.

---

<span id="class_DisplayServer_method_window_start_drag"></span>

void **window_start_drag** ( window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_start_drag)

Starts an interactive drag operation on the window with the given `window_id`, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's title bar. Using this method allows the window to participate in space switching, tiling, and other system features.

 **Note:** This method is implemented on Linux (X11/Wayland), macOS, and Windows.

---

<span id="class_DisplayServer_method_window_start_resize"></span>

void **window_start_resize** ( edge: [WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge), window_id: [int](class_int.md#class_int) = 0 ) [🔗](class_displayserver.md#class_DisplayServer_method_window_start_resize)

Starts an interactive resize operation on the window with the given `window_id`, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's edge.

 **Note:** This method is implemented on Linux (X11/Wayland), macOS, and Windows.
