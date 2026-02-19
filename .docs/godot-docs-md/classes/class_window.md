<span id="class_Window"></span>

## Window

**Inherits:** [Viewport](class_viewport.md#class_Viewport) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AcceptDialog](class_acceptdialog.md#class_AcceptDialog), [Popup](class_popup.md#class_Popup)

Base class for all windows, dialogs, and popups.

### Description

A node that creates a window. The window can either be a native system window or embedded inside another **Window** (see [Viewport.gui_embed_subwindows](class_viewport.md#class_Viewport_property_gui_embed_subwindows)).

At runtime, **Window** s will not close automatically when requested. You need to handle it manually using the [close_requested](class_window.md#class_Window_signal_close_requested) signal (this applies both to pressing the close button and clicking outside of a popup).

### Properties


| [String](class_string.md#class_String) | [accessibility_description](class_window.md#class_Window_property_accessibility_description) | `""` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [accessibility_name](class_window.md#class_Window_property_accessibility_name) | `""` |
| [bool](class_bool.md#class_bool) | [always_on_top](class_window.md#class_Window_property_always_on_top) | `false` |
| [bool](class_bool.md#class_bool) | [auto_translate](class_window.md#class_Window_property_auto_translate) |
| [bool](class_bool.md#class_bool) | [borderless](class_window.md#class_Window_property_borderless) | `false` |
| [ContentScaleAspect](class_window.md#enum_Window_ContentScaleAspect) | [content_scale_aspect](class_window.md#class_Window_property_content_scale_aspect) | `0` |
| [float](class_float.md#class_float) | [content_scale_factor](class_window.md#class_Window_property_content_scale_factor) | `1.0` |
| [ContentScaleMode](class_window.md#enum_Window_ContentScaleMode) | [content_scale_mode](class_window.md#class_Window_property_content_scale_mode) | `0` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [content_scale_size](class_window.md#class_Window_property_content_scale_size) | `Vector2i(0, 0)` |
| [ContentScaleStretch](class_window.md#enum_Window_ContentScaleStretch) | [content_scale_stretch](class_window.md#class_Window_property_content_scale_stretch) | `0` |
| [int](class_int.md#class_int) | [current_screen](class_window.md#class_Window_property_current_screen) |
| [bool](class_bool.md#class_bool) | [exclude_from_capture](class_window.md#class_Window_property_exclude_from_capture) | `false` |
| [bool](class_bool.md#class_bool) | [exclusive](class_window.md#class_Window_property_exclusive) | `false` |
| [bool](class_bool.md#class_bool) | [extend_to_title](class_window.md#class_Window_property_extend_to_title) | `false` |
| [bool](class_bool.md#class_bool) | [force_native](class_window.md#class_Window_property_force_native) | `false` |
| [bool](class_bool.md#class_bool) | [hdr_output_requested](class_window.md#class_Window_property_hdr_output_requested) | `false` |
| [WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) | [initial_position](class_window.md#class_Window_property_initial_position) | `0` |
| [bool](class_bool.md#class_bool) | [keep_title_visible](class_window.md#class_Window_property_keep_title_visible) | `false` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [max_size](class_window.md#class_Window_property_max_size) | `Vector2i(0, 0)` |
| [bool](class_bool.md#class_bool) | [maximize_disabled](class_window.md#class_Window_property_maximize_disabled) | `false` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [min_size](class_window.md#class_Window_property_min_size) | `Vector2i(0, 0)` |
| [bool](class_bool.md#class_bool) | [minimize_disabled](class_window.md#class_Window_property_minimize_disabled) | `false` |
| [Mode](class_window.md#enum_Window_Mode) | [mode](class_window.md#class_Window_property_mode) | `0` |
| [bool](class_bool.md#class_bool) | [mouse_passthrough](class_window.md#class_Window_property_mouse_passthrough) | `false` |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [mouse_passthrough_polygon](class_window.md#class_Window_property_mouse_passthrough_polygon) | `PackedVector2Array()` |
| [Rect2i](class_rect2i.md#class_Rect2i) | [nonclient_area](class_window.md#class_Window_property_nonclient_area) | `Rect2i(0, 0, 0, 0)` |
| [bool](class_bool.md#class_bool) | [popup_window](class_window.md#class_Window_property_popup_window) | `false` |
| [bool](class_bool.md#class_bool) | [popup_wm_hint](class_window.md#class_Window_property_popup_wm_hint) | `false` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [position](class_window.md#class_Window_property_position) | `Vector2i(0, 0)` |
| [bool](class_bool.md#class_bool) | [sharp_corners](class_window.md#class_Window_property_sharp_corners) | `false` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [size](class_window.md#class_Window_property_size) | `Vector2i(100, 100)` |
| [Theme](class_theme.md#class_Theme) | [theme](class_window.md#class_Window_property_theme) |
| [StringName](class_stringname.md#class_StringName) | [theme_type_variation](class_window.md#class_Window_property_theme_type_variation) | `&""` |
| [String](class_string.md#class_String) | [title](class_window.md#class_Window_property_title) | `""` |
| [bool](class_bool.md#class_bool) | [transient](class_window.md#class_Window_property_transient) | `false` |
| [bool](class_bool.md#class_bool) | [transient_to_focused](class_window.md#class_Window_property_transient_to_focused) | `false` |
| [bool](class_bool.md#class_bool) | [transparent](class_window.md#class_Window_property_transparent) | `false` |
| [bool](class_bool.md#class_bool) | [unfocusable](class_window.md#class_Window_property_unfocusable) | `false` |
| [bool](class_bool.md#class_bool) | [unresizable](class_window.md#class_Window_property_unresizable) | `false` |
| [bool](class_bool.md#class_bool) | [visible](class_window.md#class_Window_property_visible) | `true` |
| [bool](class_bool.md#class_bool) | [wrap_controls](class_window.md#class_Window_property_wrap_controls) | `false` |

### Methods


| [Vector2](class_vector2.md#class_Vector2) | [_get_contents_minimum_size](class_window.md#class_Window_private_method__get_contents_minimum_size) ( ) | virtual | const |
| --- | --- | --- | --- |
| void | [add_theme_color_override](class_window.md#class_Window_method_add_theme_color_override) ( name: [StringName](class_stringname.md#class_StringName), color: [Color](class_color.md#class_Color) ) |
| void | [add_theme_constant_override](class_window.md#class_Window_method_add_theme_constant_override) ( name: [StringName](class_stringname.md#class_StringName), constant: [int](class_int.md#class_int) ) |
| void | [add_theme_font_override](class_window.md#class_Window_method_add_theme_font_override) ( name: [StringName](class_stringname.md#class_StringName), font: [Font](class_font.md#class_Font) ) |
| void | [add_theme_font_size_override](class_window.md#class_Window_method_add_theme_font_size_override) ( name: [StringName](class_stringname.md#class_StringName), font_size: [int](class_int.md#class_int) ) |
| void | [add_theme_icon_override](class_window.md#class_Window_method_add_theme_icon_override) ( name: [StringName](class_stringname.md#class_StringName), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [add_theme_stylebox_override](class_window.md#class_Window_method_add_theme_stylebox_override) ( name: [StringName](class_stringname.md#class_StringName), stylebox: [StyleBox](class_stylebox.md#class_StyleBox) ) |
| void | [begin_bulk_theme_override](class_window.md#class_Window_method_begin_bulk_theme_override) ( ) |
| [bool](class_bool.md#class_bool) | [can_draw](class_window.md#class_Window_method_can_draw) ( ) const |
| void | [child_controls_changed](class_window.md#class_Window_method_child_controls_changed) ( ) |
| void | [end_bulk_theme_override](class_window.md#class_Window_method_end_bulk_theme_override) ( ) |
| [Vector2](class_vector2.md#class_Vector2) | [get_contents_minimum_size](class_window.md#class_Window_method_get_contents_minimum_size) ( ) const |
| [bool](class_bool.md#class_bool) | [get_flag](class_window.md#class_Window_method_get_flag) ( flag: [Flags](class_window.md#enum_Window_Flags) ) const |
| [Window](class_window.md#class_Window) | [get_focused_window](class_window.md#class_Window_method_get_focused_window) ( ) static |
| [LayoutDirection](class_window.md#enum_Window_LayoutDirection) | [get_layout_direction](class_window.md#class_Window_method_get_layout_direction) ( ) const |
| [float](class_float.md#class_float) | [get_output_max_linear_value](class_window.md#class_Window_method_get_output_max_linear_value) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_position_with_decorations](class_window.md#class_Window_method_get_position_with_decorations) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_size_with_decorations](class_window.md#class_Window_method_get_size_with_decorations) ( ) const |
| [Color](class_color.md#class_Color) | [get_theme_color](class_window.md#class_Window_method_get_theme_color) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [int](class_int.md#class_int) | [get_theme_constant](class_window.md#class_Window_method_get_theme_constant) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [float](class_float.md#class_float) | [get_theme_default_base_scale](class_window.md#class_Window_method_get_theme_default_base_scale) ( ) const |
| [Font](class_font.md#class_Font) | [get_theme_default_font](class_window.md#class_Window_method_get_theme_default_font) ( ) const |
| [int](class_int.md#class_int) | [get_theme_default_font_size](class_window.md#class_Window_method_get_theme_default_font_size) ( ) const |
| [Font](class_font.md#class_Font) | [get_theme_font](class_window.md#class_Window_method_get_theme_font) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [int](class_int.md#class_int) | [get_theme_font_size](class_window.md#class_Window_method_get_theme_font_size) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_theme_icon](class_window.md#class_Window_method_get_theme_icon) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [StyleBox](class_stylebox.md#class_StyleBox) | [get_theme_stylebox](class_window.md#class_Window_method_get_theme_stylebox) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [int](class_int.md#class_int) | [get_window_id](class_window.md#class_Window_method_get_window_id) ( ) const |
| void | [grab_focus](class_window.md#class_Window_method_grab_focus) ( ) |
| [bool](class_bool.md#class_bool) | [has_focus](class_window.md#class_Window_method_has_focus) ( ) const |
| [bool](class_bool.md#class_bool) | [has_theme_color](class_window.md#class_Window_method_has_theme_color) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_color_override](class_window.md#class_Window_method_has_theme_color_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_constant](class_window.md#class_Window_method_has_theme_constant) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_constant_override](class_window.md#class_Window_method_has_theme_constant_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_font](class_window.md#class_Window_method_has_theme_font) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_font_override](class_window.md#class_Window_method_has_theme_font_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_font_size](class_window.md#class_Window_method_has_theme_font_size) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_font_size_override](class_window.md#class_Window_method_has_theme_font_size_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_icon](class_window.md#class_Window_method_has_theme_icon) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_icon_override](class_window.md#class_Window_method_has_theme_icon_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_stylebox](class_window.md#class_Window_method_has_theme_stylebox) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_stylebox_override](class_window.md#class_Window_method_has_theme_stylebox_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| void | [hide](class_window.md#class_Window_method_hide) ( ) |
| [bool](class_bool.md#class_bool) | [is_embedded](class_window.md#class_Window_method_is_embedded) ( ) const |
| [bool](class_bool.md#class_bool) | [is_layout_rtl](class_window.md#class_Window_method_is_layout_rtl) ( ) const |
| [bool](class_bool.md#class_bool) | [is_maximize_allowed](class_window.md#class_Window_method_is_maximize_allowed) ( ) const |
| [bool](class_bool.md#class_bool) | [is_using_font_oversampling](class_window.md#class_Window_method_is_using_font_oversampling) ( ) const |
| void | [move_to_center](class_window.md#class_Window_method_move_to_center) ( ) |
| void | [move_to_foreground](class_window.md#class_Window_method_move_to_foreground) ( ) |
| void | [popup](class_window.md#class_Window_method_popup) ( rect: [Rect2i](class_rect2i.md#class_Rect2i) = Rect2i(0, 0, 0, 0) ) |
| void | [popup_centered](class_window.md#class_Window_method_popup_centered) ( minsize: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(0, 0) ) |
| void | [popup_centered_clamped](class_window.md#class_Window_method_popup_centered_clamped) ( minsize: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(0, 0), fallback_ratio: [float](class_float.md#class_float) = 0.75 ) |
| void | [popup_centered_ratio](class_window.md#class_Window_method_popup_centered_ratio) ( ratio: [float](class_float.md#class_float) = 0.8 ) |
| void | [popup_exclusive](class_window.md#class_Window_method_popup_exclusive) ( from_node: [Node](class_node.md#class_Node), rect: [Rect2i](class_rect2i.md#class_Rect2i) = Rect2i(0, 0, 0, 0) ) |
| void | [popup_exclusive_centered](class_window.md#class_Window_method_popup_exclusive_centered) ( from_node: [Node](class_node.md#class_Node), minsize: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(0, 0) ) |
| void | [popup_exclusive_centered_clamped](class_window.md#class_Window_method_popup_exclusive_centered_clamped) ( from_node: [Node](class_node.md#class_Node), minsize: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(0, 0), fallback_ratio: [float](class_float.md#class_float) = 0.75 ) |
| void | [popup_exclusive_centered_ratio](class_window.md#class_Window_method_popup_exclusive_centered_ratio) ( from_node: [Node](class_node.md#class_Node), ratio: [float](class_float.md#class_float) = 0.8 ) |
| void | [popup_exclusive_on_parent](class_window.md#class_Window_method_popup_exclusive_on_parent) ( from_node: [Node](class_node.md#class_Node), parent_rect: [Rect2i](class_rect2i.md#class_Rect2i) ) |
| void | [popup_on_parent](class_window.md#class_Window_method_popup_on_parent) ( parent_rect: [Rect2i](class_rect2i.md#class_Rect2i) ) |
| void | [remove_theme_color_override](class_window.md#class_Window_method_remove_theme_color_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_constant_override](class_window.md#class_Window_method_remove_theme_constant_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_font_override](class_window.md#class_Window_method_remove_theme_font_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_font_size_override](class_window.md#class_Window_method_remove_theme_font_size_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_icon_override](class_window.md#class_Window_method_remove_theme_icon_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_stylebox_override](class_window.md#class_Window_method_remove_theme_stylebox_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [request_attention](class_window.md#class_Window_method_request_attention) ( ) |
| void | [reset_size](class_window.md#class_Window_method_reset_size) ( ) |
| void | [set_flag](class_window.md#class_Window_method_set_flag) ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_ime_active](class_window.md#class_Window_method_set_ime_active) ( active: [bool](class_bool.md#class_bool) ) |
| void | [set_ime_position](class_window.md#class_Window_method_set_ime_position) ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [set_layout_direction](class_window.md#class_Window_method_set_layout_direction) ( direction: [LayoutDirection](class_window.md#enum_Window_LayoutDirection) ) |
| void | [set_unparent_when_invisible](class_window.md#class_Window_method_set_unparent_when_invisible) ( unparent: [bool](class_bool.md#class_bool) ) |
| void | [set_use_font_oversampling](class_window.md#class_Window_method_set_use_font_oversampling) ( enable: [bool](class_bool.md#class_bool) ) |
| void | [show](class_window.md#class_Window_method_show) ( ) |
| void | [start_drag](class_window.md#class_Window_method_start_drag) ( ) |
| void | [start_resize](class_window.md#class_Window_method_start_resize) ( edge: [WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [title_color](class_window.md#class_Window_theme_color_title_color) | `Color(0.875, 0.875, 0.875, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [title_outline_modulate](class_window.md#class_Window_theme_color_title_outline_modulate) | `Color(0, 0, 0, 1)` |
| [int](class_int.md#class_int) | [close_h_offset](class_window.md#class_Window_theme_constant_close_h_offset) | `18` |
| [int](class_int.md#class_int) | [close_v_offset](class_window.md#class_Window_theme_constant_close_v_offset) | `24` |
| [int](class_int.md#class_int) | [resize_margin](class_window.md#class_Window_theme_constant_resize_margin) | `4` |
| [int](class_int.md#class_int) | [title_height](class_window.md#class_Window_theme_constant_title_height) | `36` |
| [int](class_int.md#class_int) | [title_outline_size](class_window.md#class_Window_theme_constant_title_outline_size) | `0` |
| [Font](class_font.md#class_Font) | [title_font](class_window.md#class_Window_theme_font_title_font) |
| [int](class_int.md#class_int) | [title_font_size](class_window.md#class_Window_theme_font_size_title_font_size) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [close](class_window.md#class_Window_theme_icon_close) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [close_pressed](class_window.md#class_Window_theme_icon_close_pressed) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [embedded_border](class_window.md#class_Window_theme_style_embedded_border) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [embedded_unfocused_border](class_window.md#class_Window_theme_style_embedded_unfocused_border) |

---

### Signals

<span id="class_Window_signal_about_to_popup"></span>

**about_to_popup** ( ) [🔗](class_window.md#class_Window_signal_about_to_popup)

Emitted right after [popup()](class_window.md#class_Window_method_popup) call, before the **Window** appears or does anything.

---

<span id="class_Window_signal_close_requested"></span>

**close_requested** ( ) [🔗](class_window.md#class_Window_signal_close_requested)

Emitted when the **Window**'s close button is pressed or when [popup_window](class_window.md#class_Window_property_popup_window) is enabled and user clicks outside the window.

This signal can be used to handle window closing, e.g. by connecting it to [hide()](class_window.md#class_Window_method_hide).

---

<span id="class_Window_signal_dpi_changed"></span>

**dpi_changed** ( ) [🔗](class_window.md#class_Window_signal_dpi_changed)

Emitted when the **Window**'s DPI changes as a result of OS-level changes (e.g. moving the window from a Retina display to a lower resolution one).

 **Note:** Only implemented on macOS and Linux (Wayland).

---

<span id="class_Window_signal_files_dropped"></span>

**files_dropped** ( files: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) ) [🔗](class_window.md#class_Window_signal_files_dropped)

Emitted when files are dragged from the OS file manager and dropped in the game window. The argument is a list of file paths.

::

    func _ready():
        get_window().files_dropped.connect(on_files_dropped)

    func on_files_dropped(files):
        print(files)

 **Note:** This signal only works with native windows, i.e. the main window and **Window**-derived nodes when [Viewport.gui_embed_subwindows](class_viewport.md#class_Viewport_property_gui_embed_subwindows) is disabled in the main viewport.

---

<span id="class_Window_signal_focus_entered"></span>

**focus_entered** ( ) [🔗](class_window.md#class_Window_signal_focus_entered)

Emitted when the **Window** gains focus.

---

<span id="class_Window_signal_focus_exited"></span>

**focus_exited** ( ) [🔗](class_window.md#class_Window_signal_focus_exited)

Emitted when the **Window** loses its focus.

---

<span id="class_Window_signal_go_back_requested"></span>

**go_back_requested** ( ) [🔗](class_window.md#class_Window_signal_go_back_requested)

Emitted when a go back request is sent (e.g. pressing the "Back" button on Android), right after [Node.NOTIFICATION_WM_GO_BACK_REQUEST](class_node.md#class_Node_constant_NOTIFICATION_WM_GO_BACK_REQUEST).

---

<span id="class_Window_signal_mouse_entered"></span>

**mouse_entered** ( ) [🔗](class_window.md#class_Window_signal_mouse_entered)

Emitted when the mouse cursor enters the **Window**'s visible area, that is not occluded behind other [Control](class_control.md#class_Control) s or windows, provided its [Viewport.gui_disable_input](class_viewport.md#class_Viewport_property_gui_disable_input) is `false` and regardless if it's currently focused or not.

---

<span id="class_Window_signal_mouse_exited"></span>

**mouse_exited** ( ) [🔗](class_window.md#class_Window_signal_mouse_exited)

Emitted when the mouse cursor leaves the **Window**'s visible area, that is not occluded behind other [Control](class_control.md#class_Control) s or windows, provided its [Viewport.gui_disable_input](class_viewport.md#class_Viewport_property_gui_disable_input) is `false` and regardless if it's currently focused or not.

---

<span id="class_Window_signal_nonclient_window_input"></span>

**nonclient_window_input** ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) [🔗](class_window.md#class_Window_signal_nonclient_window_input)

Emitted when the mouse event is received by the custom decoration area defined by [nonclient_area](class_window.md#class_Window_property_nonclient_area), and normal input to the window is blocked (such as when it has an exclusive child opened). `event`'s position is in the embedder's coordinate system.

---

<span id="class_Window_signal_theme_changed"></span>

**theme_changed** ( ) [🔗](class_window.md#class_Window_signal_theme_changed)

Emitted when the [NOTIFICATION_THEME_CHANGED](class_window.md#class_Window_constant_NOTIFICATION_THEME_CHANGED) notification is sent.

---

<span id="class_Window_signal_title_changed"></span>

**title_changed** ( ) [🔗](class_window.md#class_Window_signal_title_changed)

Emitted when window title bar text is changed.

---

<span id="class_Window_signal_titlebar_changed"></span>

**titlebar_changed** ( ) [🔗](class_window.md#class_Window_signal_titlebar_changed)

Emitted when window title bar decorations are changed, e.g. macOS window enter/exit full screen mode, or extend-to-title flag is changed.

---

<span id="class_Window_signal_visibility_changed"></span>

**visibility_changed** ( ) [🔗](class_window.md#class_Window_signal_visibility_changed)

Emitted when **Window** is made visible or disappears.

---

<span id="class_Window_signal_window_input"></span>

**window_input** ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) [🔗](class_window.md#class_Window_signal_window_input)

Emitted when the **Window** is currently focused and receives any input, passing the received event as an argument. The event's position, if present, is in the embedder's coordinate system.

---

### Enumerations

<span id="enum_Window_Mode"></span>

enum **Mode**: [🔗](class_window.md#enum_Window_Mode)

<span id="class_Window_constant_MODE_WINDOWED"></span>

[Mode](class_window.md#enum_Window_Mode) **MODE_WINDOWED** = `0`

Windowed mode, i.e. **Window** doesn't occupy the whole screen (unless set to the size of the screen).

<span id="class_Window_constant_MODE_MINIMIZED"></span>

[Mode](class_window.md#enum_Window_Mode) **MODE_MINIMIZED** = `1`

Minimized window mode, i.e. **Window** is not visible and available on window manager's window list. Normally happens when the minimize button is pressed.

<span id="class_Window_constant_MODE_MAXIMIZED"></span>

[Mode](class_window.md#enum_Window_Mode) **MODE_MAXIMIZED** = `2`

Maximized window mode, i.e. **Window** will occupy whole screen area except task bar and still display its borders. Normally happens when the maximize button is pressed.

<span id="class_Window_constant_MODE_FULLSCREEN"></span>

[Mode](class_window.md#enum_Window_Mode) **MODE_FULLSCREEN** = `3`

Full screen mode with full multi-window support.

Full screen window covers the entire display area of a screen and has no decorations. The display's video mode is not changed.

 **On Android:** This enables immersive mode.

 **On macOS:** A new desktop is used to display the running project.

 **Note:** Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supports [multiple resolutions](../tutorials/rendering/multiple_resolutions.md) when enabling full screen mode.

<span id="class_Window_constant_MODE_EXCLUSIVE_FULLSCREEN"></span>

[Mode](class_window.md#enum_Window_Mode) **MODE_EXCLUSIVE_FULLSCREEN** = `4`

A single window full screen mode. This mode has less overhead, but only one window can be open on a given screen at a time (opening a child window or application switching will trigger a full screen transition).

Full screen window covers the entire display area of a screen and has no border or decorations. The display's video mode is not changed.

 **Note:** This mode might not work with screen recording software.

 **On Android:** This enables immersive mode.

 **On Windows:** Depending on video driver, full screen transition might cause screens to go black for a moment.

 **On macOS:** A new desktop is used to display the running project. Exclusive full screen mode prevents Dock and Menu from showing up when the mouse pointer is hovering the edge of the screen.

 **On Linux (X11):** Exclusive full screen mode bypasses compositor.

 **On Linux (Wayland):** Equivalent to [MODE_FULLSCREEN](class_window.md#class_Window_constant_MODE_FULLSCREEN).

 **Note:** Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supports [multiple resolutions](../tutorials/rendering/multiple_resolutions.md) when enabling full screen mode.

---

<span id="enum_Window_Flags"></span>

enum **Flags**: [🔗](class_window.md#enum_Window_Flags)

<span id="class_Window_constant_FLAG_RESIZE_DISABLED"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_RESIZE_DISABLED** = `0`

The window can't be resized by dragging its resize grip. It's still possible to resize the window using [size](class_window.md#class_Window_property_size). This flag is ignored for full screen windows. Set with [unresizable](class_window.md#class_Window_property_unresizable).

<span id="class_Window_constant_FLAG_BORDERLESS"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_BORDERLESS** = `1`

The window do not have native title bar and other decorations. This flag is ignored for full-screen windows. Set with [borderless](class_window.md#class_Window_property_borderless).

<span id="class_Window_constant_FLAG_ALWAYS_ON_TOP"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_ALWAYS_ON_TOP** = `2`

The window is floating on top of all other windows. This flag is ignored for full-screen windows. Set with [always_on_top](class_window.md#class_Window_property_always_on_top).

<span id="class_Window_constant_FLAG_TRANSPARENT"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_TRANSPARENT** = `3`

The window background can be transparent. Set with [transparent](class_window.md#class_Window_property_transparent).

 **Note:** This flag has no effect if either ProjectSettings.display/window/per_pixel_transparency/allowed, or the window's [Viewport.transparent_bg](class_viewport.md#class_Viewport_property_transparent_bg) is set to `false`.

<span id="class_Window_constant_FLAG_NO_FOCUS"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_NO_FOCUS** = `4`

The window can't be focused. No-focus window will ignore all input, except mouse clicks. Set with [unfocusable](class_window.md#class_Window_property_unfocusable).

<span id="class_Window_constant_FLAG_POPUP"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_POPUP** = `5`

Window is part of menu or [OptionButton](class_optionbutton.md#class_OptionButton) dropdown. This flag can't be changed when the window is visible. An active popup window will exclusively receive all input, without stealing focus from its parent. Popup windows are automatically closed when uses click outside it, or when an application is switched. Popup window must have transient parent set (see [transient](class_window.md#class_Window_property_transient)).

 **Note:** This flag has no effect in embedded windows (unless said window is a [Popup](class_popup.md#class_Popup)).

<span id="class_Window_constant_FLAG_EXTEND_TO_TITLE"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_EXTEND_TO_TITLE** = `6`

Window content is expanded to the full size of the window. Unlike borderless window, the frame is left intact and can be used to resize the window, title bar is transparent, but have minimize/maximize/close buttons. Set with [extend_to_title](class_window.md#class_Window_property_extend_to_title).

 **Note:** This flag is implemented only on macOS.

 **Note:** This flag has no effect in embedded windows.

<span id="class_Window_constant_FLAG_MOUSE_PASSTHROUGH"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_MOUSE_PASSTHROUGH** = `7`

All mouse events are passed to the underlying window of the same application.

 **Note:** This flag has no effect in embedded windows.

<span id="class_Window_constant_FLAG_SHARP_CORNERS"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_SHARP_CORNERS** = `8`

Window style is overridden, forcing sharp corners.

 **Note:** This flag has no effect in embedded windows.

 **Note:** This flag is implemented only on Windows (11).

<span id="class_Window_constant_FLAG_EXCLUDE_FROM_CAPTURE"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_EXCLUDE_FROM_CAPTURE** = `9`

Windows is excluded from screenshots taken by [DisplayServer.screen_get_image()](class_displayserver.md#class_DisplayServer_method_screen_get_image), [DisplayServer.screen_get_image_rect()](class_displayserver.md#class_DisplayServer_method_screen_get_image_rect), and [DisplayServer.screen_get_pixel()](class_displayserver.md#class_DisplayServer_method_screen_get_pixel).

 **Note:** This flag has no effect in embedded windows.

 **Note:** This flag is implemented on macOS and Windows (10, 20H1).

 **Note:** Setting this flag will prevent standard screenshot methods from capturing a window image, but does **NOT** guarantee that other apps won't be able to capture an image. It should not be used as a DRM or security measure.

<span id="class_Window_constant_FLAG_POPUP_WM_HINT"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_POPUP_WM_HINT** = `10`

Signals the window manager that this window is supposed to be an implementation-defined "popup" (usually a floating, borderless, untileable and immovable child window).

<span id="class_Window_constant_FLAG_MINIMIZE_DISABLED"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_MINIMIZE_DISABLED** = `11`

Window minimize button is disabled.

 **Note:** This flag is implemented on macOS and Windows.

<span id="class_Window_constant_FLAG_MAXIMIZE_DISABLED"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_MAXIMIZE_DISABLED** = `12`

Window maximize button is disabled.

 **Note:** This flag is implemented on macOS and Windows.

<span id="class_Window_constant_FLAG_MAX"></span>

[Flags](class_window.md#enum_Window_Flags) **FLAG_MAX** = `13`

Max value of the [Flags](class_window.md#enum_Window_Flags).

---

<span id="enum_Window_ContentScaleMode"></span>

enum **ContentScaleMode**: [🔗](class_window.md#enum_Window_ContentScaleMode)

<span id="class_Window_constant_CONTENT_SCALE_MODE_DISABLED"></span>

[ContentScaleMode](class_window.md#enum_Window_ContentScaleMode) **CONTENT_SCALE_MODE_DISABLED** = `0`

The content will not be scaled to match the **Window**'s size ([content_scale_size](class_window.md#class_Window_property_content_scale_size) is ignored).

<span id="class_Window_constant_CONTENT_SCALE_MODE_CANVAS_ITEMS"></span>

[ContentScaleMode](class_window.md#enum_Window_ContentScaleMode) **CONTENT_SCALE_MODE_CANVAS_ITEMS** = `1`

The content will be rendered at the target size. This is more performance-expensive than [CONTENT_SCALE_MODE_VIEWPORT](class_window.md#class_Window_constant_CONTENT_SCALE_MODE_VIEWPORT), but provides better results.

<span id="class_Window_constant_CONTENT_SCALE_MODE_VIEWPORT"></span>

[ContentScaleMode](class_window.md#enum_Window_ContentScaleMode) **CONTENT_SCALE_MODE_VIEWPORT** = `2`

The content will be rendered at the base size and then scaled to the target size. More performant than [CONTENT_SCALE_MODE_CANVAS_ITEMS](class_window.md#class_Window_constant_CONTENT_SCALE_MODE_CANVAS_ITEMS), but results in pixelated image.

---

<span id="enum_Window_ContentScaleAspect"></span>

enum **ContentScaleAspect**: [🔗](class_window.md#enum_Window_ContentScaleAspect)

<span id="class_Window_constant_CONTENT_SCALE_ASPECT_IGNORE"></span>

[ContentScaleAspect](class_window.md#enum_Window_ContentScaleAspect) **CONTENT_SCALE_ASPECT_IGNORE** = `0`

The aspect will be ignored. Scaling will simply stretch the content to fit the target size.

<span id="class_Window_constant_CONTENT_SCALE_ASPECT_KEEP"></span>

[ContentScaleAspect](class_window.md#enum_Window_ContentScaleAspect) **CONTENT_SCALE_ASPECT_KEEP** = `1`

The content's aspect will be preserved. If the target size has different aspect from the base one, the image will be centered and black bars will appear on left and right sides.

<span id="class_Window_constant_CONTENT_SCALE_ASPECT_KEEP_WIDTH"></span>

[ContentScaleAspect](class_window.md#enum_Window_ContentScaleAspect) **CONTENT_SCALE_ASPECT_KEEP_WIDTH** = `2`

The content can be expanded vertically. Scaling horizontally will result in keeping the width ratio and then black bars on left and right sides.

<span id="class_Window_constant_CONTENT_SCALE_ASPECT_KEEP_HEIGHT"></span>

[ContentScaleAspect](class_window.md#enum_Window_ContentScaleAspect) **CONTENT_SCALE_ASPECT_KEEP_HEIGHT** = `3`

The content can be expanded horizontally. Scaling vertically will result in keeping the height ratio and then black bars on top and bottom sides.

<span id="class_Window_constant_CONTENT_SCALE_ASPECT_EXPAND"></span>

[ContentScaleAspect](class_window.md#enum_Window_ContentScaleAspect) **CONTENT_SCALE_ASPECT_EXPAND** = `4`

The content's aspect will be preserved. If the target size has different aspect from the base one, the content will stay in the top-left corner and add an extra visible area in the stretched space.

---

<span id="enum_Window_ContentScaleStretch"></span>

enum **ContentScaleStretch**: [🔗](class_window.md#enum_Window_ContentScaleStretch)

<span id="class_Window_constant_CONTENT_SCALE_STRETCH_FRACTIONAL"></span>

[ContentScaleStretch](class_window.md#enum_Window_ContentScaleStretch) **CONTENT_SCALE_STRETCH_FRACTIONAL** = `0`

The content will be stretched according to a fractional factor. This fills all the space available in the window, but allows "pixel wobble" to occur due to uneven pixel scaling.

<span id="class_Window_constant_CONTENT_SCALE_STRETCH_INTEGER"></span>

[ContentScaleStretch](class_window.md#enum_Window_ContentScaleStretch) **CONTENT_SCALE_STRETCH_INTEGER** = `1`

The content will be stretched only according to an integer factor, preserving sharp pixels. This may leave a black background visible on the window's edges depending on the window size.

---

<span id="enum_Window_LayoutDirection"></span>

enum **LayoutDirection**: [🔗](class_window.md#enum_Window_LayoutDirection)

<span id="class_Window_constant_LAYOUT_DIRECTION_INHERITED"></span>

[LayoutDirection](class_window.md#enum_Window_LayoutDirection) **LAYOUT_DIRECTION_INHERITED** = `0`

Automatic layout direction, determined from the parent window layout direction.

<span id="class_Window_constant_LAYOUT_DIRECTION_APPLICATION_LOCALE"></span>

[LayoutDirection](class_window.md#enum_Window_LayoutDirection) **LAYOUT_DIRECTION_APPLICATION_LOCALE** = `1`

Automatic layout direction, determined from the current locale.

<span id="class_Window_constant_LAYOUT_DIRECTION_LTR"></span>

[LayoutDirection](class_window.md#enum_Window_LayoutDirection) **LAYOUT_DIRECTION_LTR** = `2`

Left-to-right layout direction.

<span id="class_Window_constant_LAYOUT_DIRECTION_RTL"></span>

[LayoutDirection](class_window.md#enum_Window_LayoutDirection) **LAYOUT_DIRECTION_RTL** = `3`

Right-to-left layout direction.

<span id="class_Window_constant_LAYOUT_DIRECTION_SYSTEM_LOCALE"></span>

[LayoutDirection](class_window.md#enum_Window_LayoutDirection) **LAYOUT_DIRECTION_SYSTEM_LOCALE** = `4`

Automatic layout direction, determined from the system locale.

<span id="class_Window_constant_LAYOUT_DIRECTION_MAX"></span>

[LayoutDirection](class_window.md#enum_Window_LayoutDirection) **LAYOUT_DIRECTION_MAX** = `5`

Represents the size of the [LayoutDirection](class_window.md#enum_Window_LayoutDirection) enum.

<span id="class_Window_constant_LAYOUT_DIRECTION_LOCALE"></span>

[LayoutDirection](class_window.md#enum_Window_LayoutDirection) **LAYOUT_DIRECTION_LOCALE** = `1`

**Deprecated:** Use [LAYOUT_DIRECTION_APPLICATION_LOCALE](class_window.md#class_Window_constant_LAYOUT_DIRECTION_APPLICATION_LOCALE) instead.

---

<span id="enum_Window_WindowInitialPosition"></span>

enum **WindowInitialPosition**: [🔗](class_window.md#enum_Window_WindowInitialPosition)

<span id="class_Window_constant_WINDOW_INITIAL_POSITION_ABSOLUTE"></span>

[WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) **WINDOW_INITIAL_POSITION_ABSOLUTE** = `0`

Initial window position is determined by [position](class_window.md#class_Window_property_position).

<span id="class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_PRIMARY_SCREEN"></span>

[WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) **WINDOW_INITIAL_POSITION_CENTER_PRIMARY_SCREEN** = `1`

Initial window position is the center of the primary screen.

<span id="class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_MAIN_WINDOW_SCREEN"></span>

[WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) **WINDOW_INITIAL_POSITION_CENTER_MAIN_WINDOW_SCREEN** = `2`

Initial window position is the center of the main window screen.

<span id="class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_OTHER_SCREEN"></span>

[WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) **WINDOW_INITIAL_POSITION_CENTER_OTHER_SCREEN** = `3`

Initial window position is the center of [current_screen](class_window.md#class_Window_property_current_screen) screen.

<span id="class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_MOUSE_FOCUS"></span>

[WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) **WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_MOUSE_FOCUS** = `4`

Initial window position is the center of the screen containing the mouse pointer.

<span id="class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_KEYBOARD_FOCUS"></span>

[WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) **WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_KEYBOARD_FOCUS** = `5`

Initial window position is the center of the screen containing the window with the keyboard focus.

---

### Constants

<span id="class_Window_constant_NOTIFICATION_VISIBILITY_CHANGED"></span>

**NOTIFICATION_VISIBILITY_CHANGED** = `30` [🔗](class_window.md#class_Window_constant_NOTIFICATION_VISIBILITY_CHANGED)

Emitted when **Window**'s visibility changes, right before [visibility_changed](class_window.md#class_Window_signal_visibility_changed).

<span id="class_Window_constant_NOTIFICATION_THEME_CHANGED"></span>

**NOTIFICATION_THEME_CHANGED** = `32` [🔗](class_window.md#class_Window_constant_NOTIFICATION_THEME_CHANGED)

Sent when the node needs to refresh its theme items. This happens in one of the following cases:

- The [theme](class_window.md#class_Window_property_theme) property is changed on this node or any of its ancestors.

- The [theme_type_variation](class_window.md#class_Window_property_theme_type_variation) property is changed on this node.

- The node enters the scene tree.

 **Note:** As an optimization, this notification won't be sent from changes that occur while this node is outside of the scene tree. Instead, all of the theme item updates can be applied at once when the node enters the scene tree.

---

### Property Descriptions

<span id="class_Window_property_accessibility_description"></span>

[String](class_string.md#class_String) **accessibility_description** = `""` [🔗](class_window.md#class_Window_property_accessibility_description)

- void **set_accessibility_description** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_accessibility_description** ( )

The human-readable node description that is reported to assistive apps.

---

<span id="class_Window_property_accessibility_name"></span>

[String](class_string.md#class_String) **accessibility_name** = `""` [🔗](class_window.md#class_Window_property_accessibility_name)

- void **set_accessibility_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_accessibility_name** ( )

The human-readable node name that is reported to assistive apps.

---

<span id="class_Window_property_always_on_top"></span>

[bool](class_bool.md#class_bool) **always_on_top** = `false` [🔗](class_window.md#class_Window_property_always_on_top)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the window will be on top of all other windows. Does not work if [transient](class_window.md#class_Window_property_transient) is enabled.

---

<span id="class_Window_property_auto_translate"></span>

[bool](class_bool.md#class_bool) **auto_translate** [🔗](class_window.md#class_Window_property_auto_translate)

- void **set_auto_translate** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_auto_translating** ( )

**Deprecated:** Use [Node.auto_translate_mode](class_node.md#class_Node_property_auto_translate_mode) and [Node.can_auto_translate()](class_node.md#class_Node_method_can_auto_translate) instead.

Toggles if any text should automatically change to its translated version depending on the current locale.

---

<span id="class_Window_property_borderless"></span>

[bool](class_bool.md#class_bool) **borderless** = `false` [🔗](class_window.md#class_Window_property_borderless)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the window will have no borders.

---

<span id="class_Window_property_content_scale_aspect"></span>

[ContentScaleAspect](class_window.md#enum_Window_ContentScaleAspect) **content_scale_aspect** = `0` [🔗](class_window.md#class_Window_property_content_scale_aspect)

- void **set_content_scale_aspect** ( value: [ContentScaleAspect](class_window.md#enum_Window_ContentScaleAspect) )
- [ContentScaleAspect](class_window.md#enum_Window_ContentScaleAspect) **get_content_scale_aspect** ( )

Specifies how the content's aspect behaves when the **Window** is resized. The base aspect is determined by [content_scale_size](class_window.md#class_Window_property_content_scale_size).

---

<span id="class_Window_property_content_scale_factor"></span>

[float](class_float.md#class_float) **content_scale_factor** = `1.0` [🔗](class_window.md#class_Window_property_content_scale_factor)

- void **set_content_scale_factor** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_content_scale_factor** ( )

Specifies the base scale of **Window**'s content when its [size](class_window.md#class_Window_property_size) is equal to [content_scale_size](class_window.md#class_Window_property_content_scale_size). See also [Viewport.get_stretch_transform()](class_viewport.md#class_Viewport_method_get_stretch_transform).

---

<span id="class_Window_property_content_scale_mode"></span>

[ContentScaleMode](class_window.md#enum_Window_ContentScaleMode) **content_scale_mode** = `0` [🔗](class_window.md#class_Window_property_content_scale_mode)

- void **set_content_scale_mode** ( value: [ContentScaleMode](class_window.md#enum_Window_ContentScaleMode) )
- [ContentScaleMode](class_window.md#enum_Window_ContentScaleMode) **get_content_scale_mode** ( )

Specifies how the content is scaled when the **Window** is resized.

---

<span id="class_Window_property_content_scale_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **content_scale_size** = `Vector2i(0, 0)` [🔗](class_window.md#class_Window_property_content_scale_size)

- void **set_content_scale_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_content_scale_size** ( )

The content's base size in "virtual" pixels. Not to be confused with [size](class_window.md#class_Window_property_size), which sets the actual window's physical size in pixels. If set to a value greater than `0` and [content_scale_mode](class_window.md#class_Window_property_content_scale_mode) is set to a value other than [CONTENT_SCALE_MODE_DISABLED](class_window.md#class_Window_constant_CONTENT_SCALE_MODE_DISABLED), the **Window**'s content will be scaled when the window is resized to a different size. Higher values will make the content appear *smaller*, as it will be able to fit more of the project in view. On the root **Window**, this is set to match ProjectSettings.display/window/size/viewport_width and ProjectSettings.display/window/size/viewport_height by default.

For example, when using [CONTENT_SCALE_MODE_CANVAS_ITEMS](class_window.md#class_Window_constant_CONTENT_SCALE_MODE_CANVAS_ITEMS) and [content_scale_size](class_window.md#class_Window_property_content_scale_size) set to `Vector2i(1280, 720)`, using a window size of `2560×1440` will make 2D elements appear at double their original size, as the content is scaled by a factor of `2.0` (`2560.0 / 1280.0 = 2.0`, `1440.0 / 720.0 = 2.0`).

See `the Base size section of the Multiple resolutions documentation <../tutorials/rendering/multiple_resolutions.html#base-size>`__ for details.

---

<span id="class_Window_property_content_scale_stretch"></span>

[ContentScaleStretch](class_window.md#enum_Window_ContentScaleStretch) **content_scale_stretch** = `0` [🔗](class_window.md#class_Window_property_content_scale_stretch)

- void **set_content_scale_stretch** ( value: [ContentScaleStretch](class_window.md#enum_Window_ContentScaleStretch) )
- [ContentScaleStretch](class_window.md#enum_Window_ContentScaleStretch) **get_content_scale_stretch** ( )

The policy to use to determine the final scale factor for 2D elements. This affects how [content_scale_factor](class_window.md#class_Window_property_content_scale_factor) is applied, in addition to the automatic scale factor determined by [content_scale_size](class_window.md#class_Window_property_content_scale_size).

---

<span id="class_Window_property_current_screen"></span>

[int](class_int.md#class_int) **current_screen** [🔗](class_window.md#class_Window_property_current_screen)

- void **set_current_screen** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_current_screen** ( )

The screen the window is currently on.

---

<span id="class_Window_property_exclude_from_capture"></span>

[bool](class_bool.md#class_bool) **exclude_from_capture** = `false` [🔗](class_window.md#class_Window_property_exclude_from_capture)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the **Window** is excluded from screenshots taken by [DisplayServer.screen_get_image()](class_displayserver.md#class_DisplayServer_method_screen_get_image), [DisplayServer.screen_get_image_rect()](class_displayserver.md#class_DisplayServer_method_screen_get_image_rect), and [DisplayServer.screen_get_pixel()](class_displayserver.md#class_DisplayServer_method_screen_get_pixel).

 **Note:** This property is implemented on macOS and Windows.

 **Note:** Enabling this setting will prevent standard screenshot methods from capturing a window image, but does **NOT** guarantee that other apps won't be able to capture an image. It should not be used as a DRM or security measure.

---

<span id="class_Window_property_exclusive"></span>

[bool](class_bool.md#class_bool) **exclusive** = `false` [🔗](class_window.md#class_Window_property_exclusive)

- void **set_exclusive** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_exclusive** ( )

If `true`, the **Window** will be in exclusive mode. Exclusive windows are always on top of their parent and will block all input going to the parent **Window**.

Needs [transient](class_window.md#class_Window_property_transient) enabled to work.

---

<span id="class_Window_property_extend_to_title"></span>

[bool](class_bool.md#class_bool) **extend_to_title** = `false` [🔗](class_window.md#class_Window_property_extend_to_title)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the **Window** contents is expanded to the full size of the window, window title bar is transparent.

 **Note:** This property is implemented only on macOS.

 **Note:** This property only works with native windows.

---

<span id="class_Window_property_force_native"></span>

[bool](class_bool.md#class_bool) **force_native** = `false` [🔗](class_window.md#class_Window_property_force_native)

- void **set_force_native** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_force_native** ( )

If `true`, native window will be used regardless of parent viewport and project settings.

---

<span id="class_Window_property_hdr_output_requested"></span>

[bool](class_bool.md#class_bool) **hdr_output_requested** = `false` [🔗](class_window.md#class_Window_property_hdr_output_requested)

- void **set_hdr_output_requested** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_hdr_output_requested** ( )

If `true`, requests HDR output for the **Window**, falling back to SDR if not supported, and automatically switching between HDR and SDR as the window moves between screens, screen capabilities change, or system settings are modified. This will internally force [Viewport.use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d) to be enabled on the main [Viewport](class_viewport.md#class_Viewport). All other [SubViewport](class_subviewport.md#class_SubViewport) of this **Window** must have their [Viewport.use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d) property enabled to produce HDR output.

---

<span id="class_Window_property_initial_position"></span>

[WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) **initial_position** = `0` [🔗](class_window.md#class_Window_property_initial_position)

- void **set_initial_position** ( value: [WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) )
- [WindowInitialPosition](class_window.md#enum_Window_WindowInitialPosition) **get_initial_position** ( )

Specifies the initial type of position for the **Window**.

---

<span id="class_Window_property_keep_title_visible"></span>

[bool](class_bool.md#class_bool) **keep_title_visible** = `false` [🔗](class_window.md#class_Window_property_keep_title_visible)

- void **set_keep_title_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_keep_title_visible** ( )

If `true`, the **Window** width is expanded to keep the title bar text fully visible.

---

<span id="class_Window_property_max_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **max_size** = `Vector2i(0, 0)` [🔗](class_window.md#class_Window_property_max_size)

- void **set_max_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_max_size** ( )

If non-zero, the **Window** can't be resized to be bigger than this size.

 **Note:** This property will be ignored if the value is lower than [min_size](class_window.md#class_Window_property_min_size).

---

<span id="class_Window_property_maximize_disabled"></span>

[bool](class_bool.md#class_bool) **maximize_disabled** = `false` [🔗](class_window.md#class_Window_property_maximize_disabled)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the **Window**'s maximize button is disabled.

 **Note:** If both minimize and maximize buttons are disabled, buttons are fully hidden, and only close button is visible.

 **Note:** This property is implemented only on macOS and Windows.

---

<span id="class_Window_property_min_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **min_size** = `Vector2i(0, 0)` [🔗](class_window.md#class_Window_property_min_size)

- void **set_min_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_min_size** ( )

If non-zero, the **Window** can't be resized to be smaller than this size.

 **Note:** This property will be ignored in favor of [get_contents_minimum_size()](class_window.md#class_Window_method_get_contents_minimum_size) if [wrap_controls](class_window.md#class_Window_property_wrap_controls) is enabled and if its size is bigger.

---

<span id="class_Window_property_minimize_disabled"></span>

[bool](class_bool.md#class_bool) **minimize_disabled** = `false` [🔗](class_window.md#class_Window_property_minimize_disabled)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the **Window**'s minimize button is disabled.

 **Note:** If both minimize and maximize buttons are disabled, buttons are fully hidden, and only close button is visible.

 **Note:** This property is implemented only on macOS and Windows.

---

<span id="class_Window_property_mode"></span>

[Mode](class_window.md#enum_Window_Mode) **mode** = `0` [🔗](class_window.md#class_Window_property_mode)

- void **set_mode** ( value: [Mode](class_window.md#enum_Window_Mode) )
- [Mode](class_window.md#enum_Window_Mode) **get_mode** ( )

Set's the window's current mode.

 **Note:** Fullscreen mode is not exclusive full screen on Windows and Linux.

 **Note:** This method only works with native windows, i.e. the main window and **Window**-derived nodes when [Viewport.gui_embed_subwindows](class_viewport.md#class_Viewport_property_gui_embed_subwindows) is disabled in the main viewport.

---

<span id="class_Window_property_mouse_passthrough"></span>

[bool](class_bool.md#class_bool) **mouse_passthrough** = `false` [🔗](class_window.md#class_Window_property_mouse_passthrough)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, all mouse events will be passed to the underlying window of the same application. See also [mouse_passthrough_polygon](class_window.md#class_Window_property_mouse_passthrough_polygon).

 **Note:** This property is implemented on Linux (X11), macOS and Windows.

 **Note:** This property only works with native windows.

---

<span id="class_Window_property_mouse_passthrough_polygon"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **mouse_passthrough_polygon** = `PackedVector2Array()` [🔗](class_window.md#class_Window_property_mouse_passthrough_polygon)

- void **set_mouse_passthrough_polygon** ( value: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )
- [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_mouse_passthrough_polygon** ( )

Sets a polygonal region of the window which accepts mouse events. Mouse events outside the region will be passed through.

Passing an empty array will disable passthrough support (all mouse events will be intercepted by the window, which is the default behavior).

.. tabs::

```
```

    # Set region, using Path2D node.
    $Window.mouse_passthrough_polygon = $Path2D.curve.get_baked_points()

    # Set region, using Polygon2D node.
    $Window.mouse_passthrough_polygon = $Polygon2D.polygon

    # Reset region to default.
    $Window.mouse_passthrough_polygon = []

```
```

    // Set region, using Path2D node.
    GetNode<Window>("Window").MousePassthroughPolygon = GetNode<Path2D>("Path2D").Curve.GetBakedPoints();

    // Set region, using Polygon2D node.
    GetNode<Window>("Window").MousePassthroughPolygon = GetNode<Polygon2D>("Polygon2D").Polygon;

    // Reset region to default.
    GetNode<Window>("Window").MousePassthroughPolygon = [];

 **Note:** This property is ignored if [mouse_passthrough](class_window.md#class_Window_property_mouse_passthrough) is set to `true`.

 **Note:** On Windows, the portion of a window that lies outside the region is not drawn, while on Linux (X11) and macOS it is.

 **Note:** This property is implemented on Linux (X11), macOS and Windows.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.

---

<span id="class_Window_property_nonclient_area"></span>

[Rect2i](class_rect2i.md#class_Rect2i) **nonclient_area** = `Rect2i(0, 0, 0, 0)` [🔗](class_window.md#class_Window_property_nonclient_area)

- void **set_nonclient_area** ( value: [Rect2i](class_rect2i.md#class_Rect2i) )
- [Rect2i](class_rect2i.md#class_Rect2i) **get_nonclient_area** ( )

If set, defines the window's custom decoration area which will receive mouse input, even if normal input to the window is blocked (such as when it has an exclusive child opened). See also [nonclient_window_input](class_window.md#class_Window_signal_nonclient_window_input).

---

<span id="class_Window_property_popup_window"></span>

[bool](class_bool.md#class_bool) **popup_window** = `false` [🔗](class_window.md#class_Window_property_popup_window)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the **Window** will be considered a popup. Popups are sub-windows that don't show as separate windows in system's window manager's window list and will send close request when anything is clicked outside of them (unless [exclusive](class_window.md#class_Window_property_exclusive) is enabled).

---

<span id="class_Window_property_popup_wm_hint"></span>

[bool](class_bool.md#class_bool) **popup_wm_hint** = `false` [🔗](class_window.md#class_Window_property_popup_wm_hint)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the **Window** will signal to the window manager that it is supposed to be an implementation-defined "popup" (usually a floating, borderless, untileable and immovable child window).

---

<span id="class_Window_property_position"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **position** = `Vector2i(0, 0)` [🔗](class_window.md#class_Window_property_position)

- void **set_position** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_position** ( )

The window's position in pixels.

If ProjectSettings.display/window/subwindows/embed_subwindows is `false`, the position is in absolute screen coordinates. This typically applies to editor plugins. If the setting is `true`, the window's position is in the coordinates of its parent [Viewport](class_viewport.md#class_Viewport).

 **Note:** This property only works if [initial_position](class_window.md#class_Window_property_initial_position) is set to [WINDOW_INITIAL_POSITION_ABSOLUTE](class_window.md#class_Window_constant_WINDOW_INITIAL_POSITION_ABSOLUTE).

---

<span id="class_Window_property_sharp_corners"></span>

[bool](class_bool.md#class_bool) **sharp_corners** = `false` [🔗](class_window.md#class_Window_property_sharp_corners)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the **Window** will override the OS window style to display sharp corners.

 **Note:** This property is implemented only on Windows (11).

 **Note:** This property only works with native windows.

---

<span id="class_Window_property_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **size** = `Vector2i(100, 100)` [🔗](class_window.md#class_Window_property_size)

- void **set_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_size** ( )

The window's size in pixels. See also [content_scale_size](class_window.md#class_Window_property_content_scale_size), which doesn't set the window's physical size but affects how scaling works relative to the current [content_scale_mode](class_window.md#class_Window_property_content_scale_mode).

---

<span id="class_Window_property_theme"></span>

[Theme](class_theme.md#class_Theme) **theme** [🔗](class_window.md#class_Window_property_theme)

- void **set_theme** ( value: [Theme](class_theme.md#class_Theme) )
- [Theme](class_theme.md#class_Theme) **get_theme** ( )

The [Theme](class_theme.md#class_Theme) resource this node and all its [Control](class_control.md#class_Control) and **Window** children use. If a child node has its own [Theme](class_theme.md#class_Theme) resource set, theme items are merged with child's definitions having higher priority.

 **Note:** **Window** styles will have no effect unless the window is embedded.

---

<span id="class_Window_property_theme_type_variation"></span>

[StringName](class_stringname.md#class_StringName) **theme_type_variation** = `&""` [🔗](class_window.md#class_Window_property_theme_type_variation)

- void **set_theme_type_variation** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_theme_type_variation** ( )

The name of a theme type variation used by this **Window** to look up its own theme items. See [Control.theme_type_variation](class_control.md#class_Control_property_theme_type_variation) for more details.

---

<span id="class_Window_property_title"></span>

[String](class_string.md#class_String) **title** = `""` [🔗](class_window.md#class_Window_property_title)

- void **set_title** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_title** ( )

The window's title. If the **Window** is native, title styles set in [Theme](class_theme.md#class_Theme) will have no effect.

---

<span id="class_Window_property_transient"></span>

[bool](class_bool.md#class_bool) **transient** = `false` [🔗](class_window.md#class_Window_property_transient)

- void **set_transient** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_transient** ( )

If `true`, the **Window** is transient, i.e. it's considered a child of another **Window**. The transient window will be destroyed with its transient parent and will return focus to their parent when closed. The transient window is displayed on top of a non-exclusive full-screen parent window. Transient windows can't enter full-screen mode.

Note that behavior might be different depending on the platform.

---

<span id="class_Window_property_transient_to_focused"></span>

[bool](class_bool.md#class_bool) **transient_to_focused** = `false` [🔗](class_window.md#class_Window_property_transient_to_focused)

- void **set_transient_to_focused** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_transient_to_focused** ( )

If `true`, and the **Window** is [transient](class_window.md#class_Window_property_transient), this window will (at the time of becoming visible) become transient to the currently focused window instead of the immediate parent window in the hierarchy. Note that the transient parent is assigned at the time this window becomes visible, so changing it afterwards has no effect until re-shown.

---

<span id="class_Window_property_transparent"></span>

[bool](class_bool.md#class_bool) **transparent** = `false` [🔗](class_window.md#class_Window_property_transparent)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the **Window**'s background can be transparent. This is best used with embedded windows.

 **Note:** Transparency support is implemented on Linux, macOS and Windows, but availability might vary depending on GPU driver, display manager, and compositor capabilities.

 **Note:** This property has no effect if ProjectSettings.display/window/per_pixel_transparency/allowed is set to `false`.

---

<span id="class_Window_property_unfocusable"></span>

[bool](class_bool.md#class_bool) **unfocusable** = `false` [🔗](class_window.md#class_Window_property_unfocusable)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the **Window** can't be focused nor interacted with. It can still be visible.

---

<span id="class_Window_property_unresizable"></span>

[bool](class_bool.md#class_bool) **unresizable** = `false` [🔗](class_window.md#class_Window_property_unresizable)

- void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const*

If `true`, the window can't be resized.

---

<span id="class_Window_property_visible"></span>

[bool](class_bool.md#class_bool) **visible** = `true` [🔗](class_window.md#class_Window_property_visible)

- void **set_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_visible** ( )

If `true`, the window is visible.

---

<span id="class_Window_property_wrap_controls"></span>

[bool](class_bool.md#class_bool) **wrap_controls** = `false` [🔗](class_window.md#class_Window_property_wrap_controls)

- void **set_wrap_controls** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_wrapping_controls** ( )

If `true`, the window's size will automatically update when a child node is added or removed, ignoring [min_size](class_window.md#class_Window_property_min_size) if the new size is bigger.

If `false`, you need to call [child_controls_changed()](class_window.md#class_Window_method_child_controls_changed) manually.

---

### Method Descriptions

<span id="class_Window_private_method__get_contents_minimum_size"></span>

[Vector2](class_vector2.md#class_Vector2) **_get_contents_minimum_size** ( ) *virtual* *const* [🔗](class_window.md#class_Window_private_method__get_contents_minimum_size)

Virtual method to be implemented by the user. Overrides the value returned by [get_contents_minimum_size()](class_window.md#class_Window_method_get_contents_minimum_size).

---

<span id="class_Window_method_add_theme_color_override"></span>

void **add_theme_color_override** ( name: [StringName](class_stringname.md#class_StringName), color: [Color](class_color.md#class_Color) ) [🔗](class_window.md#class_Window_method_add_theme_color_override)

Creates a local override for a theme [Color](class_color.md#class_Color) with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_color_override()](class_window.md#class_Window_method_remove_theme_color_override).

See also [get_theme_color()](class_window.md#class_Window_method_get_theme_color) and [Control.add_theme_color_override()](class_control.md#class_Control_method_add_theme_color_override) for more details.

---

<span id="class_Window_method_add_theme_constant_override"></span>

void **add_theme_constant_override** ( name: [StringName](class_stringname.md#class_StringName), constant: [int](class_int.md#class_int) ) [🔗](class_window.md#class_Window_method_add_theme_constant_override)

Creates a local override for a theme constant with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_constant_override()](class_window.md#class_Window_method_remove_theme_constant_override).

See also [get_theme_constant()](class_window.md#class_Window_method_get_theme_constant).

---

<span id="class_Window_method_add_theme_font_override"></span>

void **add_theme_font_override** ( name: [StringName](class_stringname.md#class_StringName), font: [Font](class_font.md#class_Font) ) [🔗](class_window.md#class_Window_method_add_theme_font_override)

Creates a local override for a theme [Font](class_font.md#class_Font) with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_font_override()](class_window.md#class_Window_method_remove_theme_font_override).

See also [get_theme_font()](class_window.md#class_Window_method_get_theme_font).

---

<span id="class_Window_method_add_theme_font_size_override"></span>

void **add_theme_font_size_override** ( name: [StringName](class_stringname.md#class_StringName), font_size: [int](class_int.md#class_int) ) [🔗](class_window.md#class_Window_method_add_theme_font_size_override)

Creates a local override for a theme font size with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_font_size_override()](class_window.md#class_Window_method_remove_theme_font_size_override).

See also [get_theme_font_size()](class_window.md#class_Window_method_get_theme_font_size).

---

<span id="class_Window_method_add_theme_icon_override"></span>

void **add_theme_icon_override** ( name: [StringName](class_stringname.md#class_StringName), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_window.md#class_Window_method_add_theme_icon_override)

Creates a local override for a theme icon with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_icon_override()](class_window.md#class_Window_method_remove_theme_icon_override).

See also [get_theme_icon()](class_window.md#class_Window_method_get_theme_icon).

---

<span id="class_Window_method_add_theme_stylebox_override"></span>

void **add_theme_stylebox_override** ( name: [StringName](class_stringname.md#class_StringName), stylebox: [StyleBox](class_stylebox.md#class_StyleBox) ) [🔗](class_window.md#class_Window_method_add_theme_stylebox_override)

Creates a local override for a theme [StyleBox](class_stylebox.md#class_StyleBox) with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_stylebox_override()](class_window.md#class_Window_method_remove_theme_stylebox_override).

See also [get_theme_stylebox()](class_window.md#class_Window_method_get_theme_stylebox) and [Control.add_theme_stylebox_override()](class_control.md#class_Control_method_add_theme_stylebox_override) for more details.

---

<span id="class_Window_method_begin_bulk_theme_override"></span>

void **begin_bulk_theme_override** ( ) [🔗](class_window.md#class_Window_method_begin_bulk_theme_override)

Prevents `*_theme_*_override` methods from emitting [NOTIFICATION_THEME_CHANGED](class_window.md#class_Window_constant_NOTIFICATION_THEME_CHANGED) until [end_bulk_theme_override()](class_window.md#class_Window_method_end_bulk_theme_override) is called.

---

<span id="class_Window_method_can_draw"></span>

[bool](class_bool.md#class_bool) **can_draw** ( ) *const* [🔗](class_window.md#class_Window_method_can_draw)

Returns whether the window is being drawn to the screen.

---

<span id="class_Window_method_child_controls_changed"></span>

void **child_controls_changed** ( ) [🔗](class_window.md#class_Window_method_child_controls_changed)

Requests an update of the **Window** size to fit underlying [Control](class_control.md#class_Control) nodes.

---

<span id="class_Window_method_end_bulk_theme_override"></span>

void **end_bulk_theme_override** ( ) [🔗](class_window.md#class_Window_method_end_bulk_theme_override)

Ends a bulk theme override update. See [begin_bulk_theme_override()](class_window.md#class_Window_method_begin_bulk_theme_override).

---

<span id="class_Window_method_get_contents_minimum_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_contents_minimum_size** ( ) *const* [🔗](class_window.md#class_Window_method_get_contents_minimum_size)

Returns the combined minimum size from the child [Control](class_control.md#class_Control) nodes of the window. Use [child_controls_changed()](class_window.md#class_Window_method_child_controls_changed) to update it when child nodes have changed.

The value returned by this method can be overridden with [_get_contents_minimum_size()](class_window.md#class_Window_private_method__get_contents_minimum_size).

---

<span id="class_Window_method_get_flag"></span>

[bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_window.md#enum_Window_Flags) ) *const* [🔗](class_window.md#class_Window_method_get_flag)

Returns `true` if the `flag` is set.

---

<span id="class_Window_method_get_focused_window"></span>

[Window](class_window.md#class_Window) **get_focused_window** ( ) *static* [🔗](class_window.md#class_Window_method_get_focused_window)

Returns the focused window.

---

<span id="class_Window_method_get_layout_direction"></span>

[LayoutDirection](class_window.md#enum_Window_LayoutDirection) **get_layout_direction** ( ) *const* [🔗](class_window.md#class_Window_method_get_layout_direction)

Returns layout direction and text writing direction.

---

<span id="class_Window_method_get_output_max_linear_value"></span>

[float](class_float.md#class_float) **get_output_max_linear_value** ( ) *const* [🔗](class_window.md#class_Window_method_get_output_max_linear_value)

Returns the maximum value for linear color components that can be displayed in this window, regardless of SDR or HDR output. Returns `1.0` if HDR is not enabled or not supported. This value is used by tonemapping and other [Environment](class_environment.md#class_Environment) effects to ensure that bright colors are presented in the range that can be displayed by this window.

When using the Linear tonemapper without [Environment](class_environment.md#class_Environment) effects or no [WorldEnvironment](class_worldenvironment.md#class_WorldEnvironment), use the returned value to scale content to maximize the screen's brightness, such as for lasers or other bright effects. The following is an example that produces the brightest purple color that the screen can produce:

.. tabs::

```
```

    func _process(_delta):
        # output_max_linear_value may change often, so do this every frame.
        var max_linear_value = get_window().get_output_max_linear_value()
        # Replace this with your color:
        var original_color = Color.PURPLE
        # Normalize to max_linear_value to produce the brightest color possible,
        # regardless of SDR or HDR output:
        var bright_color = normalize_color(original_color, max_linear_value)

    func normalize_color(srgb_color, max_linear_value = 1.0):
        # Color must be linear-encoded to use math operations.
        var linear_color = srgb_color.srgb_to_linear()
        var max_rgb_value = maxf(linear_color.r, maxf(linear_color.g, linear_color.b))
        var brightness_scale = max_linear_value / max_rgb_value
        linear_color *= brightness_scale
        # Undo changes to the alpha channel, which should not be modified.
        linear_color.a = srgb_color.a
        # Convert back to nonlinear sRGB encoding, which is required for Color in
        # Godot unless stated otherwise.
        return linear_color.linear_to_srgb()

 **Note:** You will need to convert sRGB colors to linear before multiplying by this value to get correct results.

---

<span id="class_Window_method_get_position_with_decorations"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_position_with_decorations** ( ) *const* [🔗](class_window.md#class_Window_method_get_position_with_decorations)

Returns the window's position including its border.

 **Note:** If [visible](class_window.md#class_Window_property_visible) is `false`, this method returns the same value as [position](class_window.md#class_Window_property_position).

---

<span id="class_Window_method_get_size_with_decorations"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_size_with_decorations** ( ) *const* [🔗](class_window.md#class_Window_method_get_size_with_decorations)

Returns the window's size including its border.

 **Note:** If [visible](class_window.md#class_Window_property_visible) is `false`, this method returns the same value as [size](class_window.md#class_Window_property_size).

---

<span id="class_Window_method_get_theme_color"></span>

[Color](class_color.md#class_Color) **get_theme_color** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_get_theme_color)

Returns a [Color](class_color.md#class_Color) from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a color item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for more details.

---

<span id="class_Window_method_get_theme_constant"></span>

[int](class_int.md#class_int) **get_theme_constant** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_get_theme_constant)

Returns a constant from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a constant item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for more details.

---

<span id="class_Window_method_get_theme_default_base_scale"></span>

[float](class_float.md#class_float) **get_theme_default_base_scale** ( ) *const* [🔗](class_window.md#class_Window_method_get_theme_default_base_scale)

Returns the default base scale value from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a valid [Theme.default_base_scale](class_theme.md#class_Theme_property_default_base_scale) value.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_get_theme_default_font"></span>

[Font](class_font.md#class_Font) **get_theme_default_font** ( ) *const* [🔗](class_window.md#class_Window_method_get_theme_default_font)

Returns the default font from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a valid [Theme.default_font](class_theme.md#class_Theme_property_default_font) value.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_get_theme_default_font_size"></span>

[int](class_int.md#class_int) **get_theme_default_font_size** ( ) *const* [🔗](class_window.md#class_Window_method_get_theme_default_font_size)

Returns the default font size value from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a valid [Theme.default_font_size](class_theme.md#class_Theme_property_default_font_size) value.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_get_theme_font"></span>

[Font](class_font.md#class_Font) **get_theme_font** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_get_theme_font)

Returns a [Font](class_font.md#class_Font) from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a font item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_get_theme_font_size"></span>

[int](class_int.md#class_int) **get_theme_font_size** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_get_theme_font_size)

Returns a font size from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a font size item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_get_theme_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_theme_icon** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_get_theme_icon)

Returns an icon from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has an icon item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_get_theme_stylebox"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **get_theme_stylebox** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_get_theme_stylebox)

Returns a [StyleBox](class_stylebox.md#class_StyleBox) from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a stylebox item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_get_window_id"></span>

[int](class_int.md#class_int) **get_window_id** ( ) *const* [🔗](class_window.md#class_Window_method_get_window_id)

Returns the ID of the window.

---

<span id="class_Window_method_grab_focus"></span>

void **grab_focus** ( ) [🔗](class_window.md#class_Window_method_grab_focus)

Causes the window to grab focus, allowing it to receive user input.

---

<span id="class_Window_method_has_focus"></span>

[bool](class_bool.md#class_bool) **has_focus** ( ) *const* [🔗](class_window.md#class_Window_method_has_focus)

Returns `true` if the window is focused.

---

<span id="class_Window_method_has_theme_color"></span>

[bool](class_bool.md#class_bool) **has_theme_color** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_has_theme_color)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a color item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_has_theme_color_override"></span>

[bool](class_bool.md#class_bool) **has_theme_color_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_window.md#class_Window_method_has_theme_color_override)

Returns `true` if there is a local override for a theme [Color](class_color.md#class_Color) with the specified `name` in this [Control](class_control.md#class_Control) node.

See [add_theme_color_override()](class_window.md#class_Window_method_add_theme_color_override).

---

<span id="class_Window_method_has_theme_constant"></span>

[bool](class_bool.md#class_bool) **has_theme_constant** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_has_theme_constant)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a constant item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_has_theme_constant_override"></span>

[bool](class_bool.md#class_bool) **has_theme_constant_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_window.md#class_Window_method_has_theme_constant_override)

Returns `true` if there is a local override for a theme constant with the specified `name` in this [Control](class_control.md#class_Control) node.

See [add_theme_constant_override()](class_window.md#class_Window_method_add_theme_constant_override).

---

<span id="class_Window_method_has_theme_font"></span>

[bool](class_bool.md#class_bool) **has_theme_font** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_has_theme_font)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a font item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_has_theme_font_override"></span>

[bool](class_bool.md#class_bool) **has_theme_font_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_window.md#class_Window_method_has_theme_font_override)

Returns `true` if there is a local override for a theme [Font](class_font.md#class_Font) with the specified `name` in this [Control](class_control.md#class_Control) node.

See [add_theme_font_override()](class_window.md#class_Window_method_add_theme_font_override).

---

<span id="class_Window_method_has_theme_font_size"></span>

[bool](class_bool.md#class_bool) **has_theme_font_size** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_has_theme_font_size)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a font size item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_has_theme_font_size_override"></span>

[bool](class_bool.md#class_bool) **has_theme_font_size_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_window.md#class_Window_method_has_theme_font_size_override)

Returns `true` if there is a local override for a theme font size with the specified `name` in this [Control](class_control.md#class_Control) node.

See [add_theme_font_size_override()](class_window.md#class_Window_method_add_theme_font_size_override).

---

<span id="class_Window_method_has_theme_icon"></span>

[bool](class_bool.md#class_bool) **has_theme_icon** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_has_theme_icon)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has an icon item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_has_theme_icon_override"></span>

[bool](class_bool.md#class_bool) **has_theme_icon_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_window.md#class_Window_method_has_theme_icon_override)

Returns `true` if there is a local override for a theme icon with the specified `name` in this [Control](class_control.md#class_Control) node.

See [add_theme_icon_override()](class_window.md#class_Window_method_add_theme_icon_override).

---

<span id="class_Window_method_has_theme_stylebox"></span>

[bool](class_bool.md#class_bool) **has_theme_stylebox** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_window.md#class_Window_method_has_theme_stylebox)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a stylebox item with the specified `name` and `theme_type`.

See [Control.get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Window_method_has_theme_stylebox_override"></span>

[bool](class_bool.md#class_bool) **has_theme_stylebox_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_window.md#class_Window_method_has_theme_stylebox_override)

Returns `true` if there is a local override for a theme [StyleBox](class_stylebox.md#class_StyleBox) with the specified `name` in this [Control](class_control.md#class_Control) node.

See [add_theme_stylebox_override()](class_window.md#class_Window_method_add_theme_stylebox_override).

---

<span id="class_Window_method_hide"></span>

void **hide** ( ) [🔗](class_window.md#class_Window_method_hide)

Hides the window. This is not the same as minimized state. Hidden window can't be interacted with and needs to be made visible with [show()](class_window.md#class_Window_method_show).

---

<span id="class_Window_method_is_embedded"></span>

[bool](class_bool.md#class_bool) **is_embedded** ( ) *const* [🔗](class_window.md#class_Window_method_is_embedded)

Returns `true` if the window is currently embedded in another window.

---

<span id="class_Window_method_is_layout_rtl"></span>

[bool](class_bool.md#class_bool) **is_layout_rtl** ( ) *const* [🔗](class_window.md#class_Window_method_is_layout_rtl)

Returns `true` if the layout is right-to-left.

---

<span id="class_Window_method_is_maximize_allowed"></span>

[bool](class_bool.md#class_bool) **is_maximize_allowed** ( ) *const* [🔗](class_window.md#class_Window_method_is_maximize_allowed)

Returns `true` if the window can be maximized (the maximize button is enabled).

---

<span id="class_Window_method_is_using_font_oversampling"></span>

[bool](class_bool.md#class_bool) **is_using_font_oversampling** ( ) *const* [🔗](class_window.md#class_Window_method_is_using_font_oversampling)

Returns `true` if font oversampling is enabled. See [set_use_font_oversampling()](class_window.md#class_Window_method_set_use_font_oversampling).

---

<span id="class_Window_method_move_to_center"></span>

void **move_to_center** ( ) [🔗](class_window.md#class_Window_method_move_to_center)

Centers the window in the current screen. If the window is embedded, it is centered in the embedder [Viewport](class_viewport.md#class_Viewport) instead.

---

<span id="class_Window_method_move_to_foreground"></span>

void **move_to_foreground** ( ) [🔗](class_window.md#class_Window_method_move_to_foreground)

**Deprecated:** Use [grab_focus()](class_window.md#class_Window_method_grab_focus) instead.

Causes the window to grab focus, allowing it to receive user input.

---

<span id="class_Window_method_popup"></span>

void **popup** ( rect: [Rect2i](class_rect2i.md#class_Rect2i) = Rect2i(0, 0, 0, 0) ) [🔗](class_window.md#class_Window_method_popup)

Shows the **Window** and makes it transient (see [transient](class_window.md#class_Window_property_transient)). If `rect` is provided, it will be set as the **Window**'s size. Fails if called on the main window.

If ProjectSettings.display/window/subwindows/embed_subwindows is `true` (single-window mode), `rect`'s coordinates are global and relative to the main window's top-left corner (excluding window decorations). If `rect`'s position coordinates are negative, the window will be located outside the main window and may not be visible as a result.

If ProjectSettings.display/window/subwindows/embed_subwindows is `false` (multi-window mode), `rect`'s coordinates are global and relative to the top-left corner of the leftmost screen. If `rect`'s position coordinates are negative, the window will be placed at the top-left corner of the screen.

 **Note:** `rect` must be in global coordinates if specified.

---

<span id="class_Window_method_popup_centered"></span>

void **popup_centered** ( minsize: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(0, 0) ) [🔗](class_window.md#class_Window_method_popup_centered)

Popups the **Window** at the center of the current screen, with optionally given minimum size. If the **Window** is embedded, it will be centered in the parent [Viewport](class_viewport.md#class_Viewport) instead.

 **Note:** Calling it with the default value of `minsize` is equivalent to calling it with [size](class_window.md#class_Window_property_size).

---

<span id="class_Window_method_popup_centered_clamped"></span>

void **popup_centered_clamped** ( minsize: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(0, 0), fallback_ratio: [float](class_float.md#class_float) = 0.75 ) [🔗](class_window.md#class_Window_method_popup_centered_clamped)

Popups the **Window** centered inside its parent **Window**. `fallback_ratio` determines the maximum size of the **Window**, in relation to its parent.

 **Note:** Calling it with the default value of `minsize` is equivalent to calling it with [size](class_window.md#class_Window_property_size).

---

<span id="class_Window_method_popup_centered_ratio"></span>

void **popup_centered_ratio** ( ratio: [float](class_float.md#class_float) = 0.8 ) [🔗](class_window.md#class_Window_method_popup_centered_ratio)

If **Window** is embedded, popups the **Window** centered inside its embedder and sets its size as a `ratio` of embedder's size.

If **Window** is a native window, popups the **Window** centered inside the screen of its parent **Window** and sets its size as a `ratio` of the screen size.

---

<span id="class_Window_method_popup_exclusive"></span>

void **popup_exclusive** ( from_node: [Node](class_node.md#class_Node), rect: [Rect2i](class_rect2i.md#class_Rect2i) = Rect2i(0, 0, 0, 0) ) [🔗](class_window.md#class_Window_method_popup_exclusive)

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls [popup()](class_window.md#class_Window_method_popup) on it. The dialog must have no current parent, otherwise the method fails.

See also [set_unparent_when_invisible()](class_window.md#class_Window_method_set_unparent_when_invisible) and [Node.get_last_exclusive_window()](class_node.md#class_Node_method_get_last_exclusive_window).

---

<span id="class_Window_method_popup_exclusive_centered"></span>

void **popup_exclusive_centered** ( from_node: [Node](class_node.md#class_Node), minsize: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(0, 0) ) [🔗](class_window.md#class_Window_method_popup_exclusive_centered)

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls [popup_centered()](class_window.md#class_Window_method_popup_centered) on it. The dialog must have no current parent, otherwise the method fails.

See also [set_unparent_when_invisible()](class_window.md#class_Window_method_set_unparent_when_invisible) and [Node.get_last_exclusive_window()](class_node.md#class_Node_method_get_last_exclusive_window).

---

<span id="class_Window_method_popup_exclusive_centered_clamped"></span>

void **popup_exclusive_centered_clamped** ( from_node: [Node](class_node.md#class_Node), minsize: [Vector2i](class_vector2i.md#class_Vector2i) = Vector2i(0, 0), fallback_ratio: [float](class_float.md#class_float) = 0.75 ) [🔗](class_window.md#class_Window_method_popup_exclusive_centered_clamped)

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls [popup_centered_clamped()](class_window.md#class_Window_method_popup_centered_clamped) on it. The dialog must have no current parent, otherwise the method fails.

See also [set_unparent_when_invisible()](class_window.md#class_Window_method_set_unparent_when_invisible) and [Node.get_last_exclusive_window()](class_node.md#class_Node_method_get_last_exclusive_window).

---

<span id="class_Window_method_popup_exclusive_centered_ratio"></span>

void **popup_exclusive_centered_ratio** ( from_node: [Node](class_node.md#class_Node), ratio: [float](class_float.md#class_float) = 0.8 ) [🔗](class_window.md#class_Window_method_popup_exclusive_centered_ratio)

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls [popup_centered_ratio()](class_window.md#class_Window_method_popup_centered_ratio) on it. The dialog must have no current parent, otherwise the method fails.

See also [set_unparent_when_invisible()](class_window.md#class_Window_method_set_unparent_when_invisible) and [Node.get_last_exclusive_window()](class_node.md#class_Node_method_get_last_exclusive_window).

---

<span id="class_Window_method_popup_exclusive_on_parent"></span>

void **popup_exclusive_on_parent** ( from_node: [Node](class_node.md#class_Node), parent_rect: [Rect2i](class_rect2i.md#class_Rect2i) ) [🔗](class_window.md#class_Window_method_popup_exclusive_on_parent)

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls [popup_on_parent()](class_window.md#class_Window_method_popup_on_parent) on it. The dialog must have no current parent, otherwise the method fails.

See also [set_unparent_when_invisible()](class_window.md#class_Window_method_set_unparent_when_invisible) and [Node.get_last_exclusive_window()](class_node.md#class_Node_method_get_last_exclusive_window).

---

<span id="class_Window_method_popup_on_parent"></span>

void **popup_on_parent** ( parent_rect: [Rect2i](class_rect2i.md#class_Rect2i) ) [🔗](class_window.md#class_Window_method_popup_on_parent)

Popups the **Window** with a position shifted by parent **Window**'s position. If the **Window** is embedded, has the same effect as [popup()](class_window.md#class_Window_method_popup).

---

<span id="class_Window_method_remove_theme_color_override"></span>

void **remove_theme_color_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_window.md#class_Window_method_remove_theme_color_override)

Removes a local override for a theme [Color](class_color.md#class_Color) with the specified `name` previously added by [add_theme_color_override()](class_window.md#class_Window_method_add_theme_color_override) or via the Inspector dock.

---

<span id="class_Window_method_remove_theme_constant_override"></span>

void **remove_theme_constant_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_window.md#class_Window_method_remove_theme_constant_override)

Removes a local override for a theme constant with the specified `name` previously added by [add_theme_constant_override()](class_window.md#class_Window_method_add_theme_constant_override) or via the Inspector dock.

---

<span id="class_Window_method_remove_theme_font_override"></span>

void **remove_theme_font_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_window.md#class_Window_method_remove_theme_font_override)

Removes a local override for a theme [Font](class_font.md#class_Font) with the specified `name` previously added by [add_theme_font_override()](class_window.md#class_Window_method_add_theme_font_override) or via the Inspector dock.

---

<span id="class_Window_method_remove_theme_font_size_override"></span>

void **remove_theme_font_size_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_window.md#class_Window_method_remove_theme_font_size_override)

Removes a local override for a theme font size with the specified `name` previously added by [add_theme_font_size_override()](class_window.md#class_Window_method_add_theme_font_size_override) or via the Inspector dock.

---

<span id="class_Window_method_remove_theme_icon_override"></span>

void **remove_theme_icon_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_window.md#class_Window_method_remove_theme_icon_override)

Removes a local override for a theme icon with the specified `name` previously added by [add_theme_icon_override()](class_window.md#class_Window_method_add_theme_icon_override) or via the Inspector dock.

---

<span id="class_Window_method_remove_theme_stylebox_override"></span>

void **remove_theme_stylebox_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_window.md#class_Window_method_remove_theme_stylebox_override)

Removes a local override for a theme [StyleBox](class_stylebox.md#class_StyleBox) with the specified `name` previously added by [add_theme_stylebox_override()](class_window.md#class_Window_method_add_theme_stylebox_override) or via the Inspector dock.

---

<span id="class_Window_method_request_attention"></span>

void **request_attention** ( ) [🔗](class_window.md#class_Window_method_request_attention)

Tells the OS that the **Window** needs an attention. This makes the window stand out in some way depending on the system, e.g. it might blink on the task bar.

---

<span id="class_Window_method_reset_size"></span>

void **reset_size** ( ) [🔗](class_window.md#class_Window_method_reset_size)

Resets the size to the minimum size, which is the max of [min_size](class_window.md#class_Window_property_min_size) and (if [wrap_controls](class_window.md#class_Window_property_wrap_controls) is enabled) [get_contents_minimum_size()](class_window.md#class_Window_method_get_contents_minimum_size). This is equivalent to calling `set_size(Vector2i())` (or any size below the minimum).

---

<span id="class_Window_method_set_flag"></span>

void **set_flag** ( flag: [Flags](class_window.md#enum_Window_Flags), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_window.md#class_Window_method_set_flag)

Sets a specified window flag.

---

<span id="class_Window_method_set_ime_active"></span>

void **set_ime_active** ( active: [bool](class_bool.md#class_bool) ) [🔗](class_window.md#class_Window_method_set_ime_active)

If `active` is `true`, enables system's native IME (Input Method Editor).

---

<span id="class_Window_method_set_ime_position"></span>

void **set_ime_position** ( position: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_window.md#class_Window_method_set_ime_position)

Moves IME to the given position.

---

<span id="class_Window_method_set_layout_direction"></span>

void **set_layout_direction** ( direction: [LayoutDirection](class_window.md#enum_Window_LayoutDirection) ) [🔗](class_window.md#class_Window_method_set_layout_direction)

Sets layout direction and text writing direction. Right-to-left layouts are necessary for certain languages (e.g. Arabic and Hebrew).

---

<span id="class_Window_method_set_unparent_when_invisible"></span>

void **set_unparent_when_invisible** ( unparent: [bool](class_bool.md#class_bool) ) [🔗](class_window.md#class_Window_method_set_unparent_when_invisible)

If `unparent` is `true`, the window is automatically unparented when going invisible.

 **Note:** Make sure to keep a reference to the node, otherwise it will be orphaned. You also need to manually call [Node.queue_free()](class_node.md#class_Node_method_queue_free) to free the window if it's not parented.

---

<span id="class_Window_method_set_use_font_oversampling"></span>

void **set_use_font_oversampling** ( enable: [bool](class_bool.md#class_bool) ) [🔗](class_window.md#class_Window_method_set_use_font_oversampling)

Enables font oversampling. This makes fonts look better when they are scaled up.

---

<span id="class_Window_method_show"></span>

void **show** ( ) [🔗](class_window.md#class_Window_method_show)

Makes the **Window** appear. This enables interactions with the **Window** and doesn't change any of its property other than visibility (unlike e.g. [popup()](class_window.md#class_Window_method_popup)).

---

<span id="class_Window_method_start_drag"></span>

void **start_drag** ( ) [🔗](class_window.md#class_Window_method_start_drag)

Starts an interactive drag operation on the window, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's title bar. Using this method allows the window to participate in space switching, tiling, and other system features.

---

<span id="class_Window_method_start_resize"></span>

void **start_resize** ( edge: [WindowResizeEdge](class_displayserver.md#enum_DisplayServer_WindowResizeEdge) ) [🔗](class_window.md#class_Window_method_start_resize)

Starts an interactive resize operation on the window, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's edge.

---

### Theme Property Descriptions

<span id="class_Window_theme_color_title_color"></span>

[Color](class_color.md#class_Color) **title_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_window.md#class_Window_theme_color_title_color)

The color of the title's text.

---

<span id="class_Window_theme_color_title_outline_modulate"></span>

[Color](class_color.md#class_Color) **title_outline_modulate** = `Color(0, 0, 0, 1)` [🔗](class_window.md#class_Window_theme_color_title_outline_modulate)

The color of the title's text outline.

---

<span id="class_Window_theme_constant_close_h_offset"></span>

[int](class_int.md#class_int) **close_h_offset** = `18` [🔗](class_window.md#class_Window_theme_constant_close_h_offset)

Horizontal position offset of the close button, relative to the end of the title bar, towards the beginning of the title bar.

---

<span id="class_Window_theme_constant_close_v_offset"></span>

[int](class_int.md#class_int) **close_v_offset** = `24` [🔗](class_window.md#class_Window_theme_constant_close_v_offset)

Vertical position offset of the close button, relative to the bottom of the title bar, towards the top of the title bar.

---

<span id="class_Window_theme_constant_resize_margin"></span>

[int](class_int.md#class_int) **resize_margin** = `4` [🔗](class_window.md#class_Window_theme_constant_resize_margin)

Defines the outside margin at which the window border can be grabbed with mouse and resized.

---

<span id="class_Window_theme_constant_title_height"></span>

[int](class_int.md#class_int) **title_height** = `36` [🔗](class_window.md#class_Window_theme_constant_title_height)

Height of the title bar.

---

<span id="class_Window_theme_constant_title_outline_size"></span>

[int](class_int.md#class_int) **title_outline_size** = `0` [🔗](class_window.md#class_Window_theme_constant_title_outline_size)

The size of the title outline.

---

<span id="class_Window_theme_font_title_font"></span>

[Font](class_font.md#class_Font) **title_font** [🔗](class_window.md#class_Window_theme_font_title_font)

The font used to draw the title.

---

<span id="class_Window_theme_font_size_title_font_size"></span>

[int](class_int.md#class_int) **title_font_size** [🔗](class_window.md#class_Window_theme_font_size_title_font_size)

The size of the title font.

---

<span id="class_Window_theme_icon_close"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **close** [🔗](class_window.md#class_Window_theme_icon_close)

The icon for the close button.

---

<span id="class_Window_theme_icon_close_pressed"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **close_pressed** [🔗](class_window.md#class_Window_theme_icon_close_pressed)

The icon for the close button when it's being pressed.

---

<span id="class_Window_theme_style_embedded_border"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **embedded_border** [🔗](class_window.md#class_Window_theme_style_embedded_border)

The background style used when the **Window** is embedded. Note that this is drawn only under the window's content, excluding the title. For proper borders and title bar style, you can use `expand_margin_*` properties of [StyleBoxFlat](class_styleboxflat.md#class_StyleBoxFlat).

 **Note:** The content background will not be visible unless [transparent](class_window.md#class_Window_property_transparent) is enabled.

---

<span id="class_Window_theme_style_embedded_unfocused_border"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **embedded_unfocused_border** [🔗](class_window.md#class_Window_theme_style_embedded_unfocused_border)

The background style used when the **Window** is embedded and unfocused.
