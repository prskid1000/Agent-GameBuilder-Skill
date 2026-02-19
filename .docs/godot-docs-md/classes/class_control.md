<span id="class_Control"></span>

## Control

**Inherits:** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [BaseButton](class_basebutton.md#class_BaseButton), [ColorRect](class_colorrect.md#class_ColorRect), [Container](class_container.md#class_Container), [GraphEdit](class_graphedit.md#class_GraphEdit), [ItemList](class_itemlist.md#class_ItemList), [Label](class_label.md#class_Label), [LineEdit](class_lineedit.md#class_LineEdit), [MenuBar](class_menubar.md#class_MenuBar), [NinePatchRect](class_ninepatchrect.md#class_NinePatchRect), [Panel](class_panel.md#class_Panel), [Range](class_range.md#class_Range), [ReferenceRect](class_referencerect.md#class_ReferenceRect), [RichTextLabel](class_richtextlabel.md#class_RichTextLabel), [ScriptEditorBase](class_scripteditorbase.md#class_ScriptEditorBase), [Separator](class_separator.md#class_Separator), [TabBar](class_tabbar.md#class_TabBar), [TextEdit](class_textedit.md#class_TextEdit), [TextureRect](class_texturerect.md#class_TextureRect), [Tree](class_tree.md#class_Tree), [VideoStreamPlayer](class_videostreamplayer.md#class_VideoStreamPlayer), [VirtualJoystick](class_virtualjoystick.md#class_VirtualJoystick)

Base class for all GUI controls. Adapts its position and size based on its parent control.

### Description

Base class for all UI-related nodes. **Control** features a bounding rectangle that defines its extents, an anchor position relative to its parent control or the current viewport, and offsets relative to the anchor. The offsets update automatically when the node, any of its parents, or the screen size change.

For more information on Godot's UI system, anchors, offsets, and containers, see the related tutorials in the manual. To build flexible UIs, you'll need a mix of UI elements that inherit from **Control** and [Container](class_container.md#class_Container) nodes.

 **Note:** Since both [Node2D](class_node2d.md#class_Node2D) and **Control** inherit from [CanvasItem](class_canvasitem.md#class_CanvasItem), they share several concepts from the class such as the [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) and [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) properties.

 **User Interface nodes and input**

Godot propagates input events via viewports. Each [Viewport](class_viewport.md#class_Viewport) is responsible for propagating [InputEvent](class_inputevent.md#class_InputEvent) s to their child nodes. As the [SceneTree.root](class_scenetree.md#class_SceneTree_property_root) is a [Window](class_window.md#class_Window), this already happens automatically for all UI elements in your game.

Input events are propagated through the [SceneTree](class_scenetree.md#class_SceneTree) from the root node to all child nodes by calling [Node._input()](class_node.md#class_Node_private_method__input). For UI elements specifically, it makes more sense to override the virtual method [_gui_input()](class_control.md#class_Control_private_method__gui_input), which filters out unrelated input events, such as by checking z-order, [mouse_filter](class_control.md#class_Control_property_mouse_filter), focus, or if the event was inside of the control's bounding box.

Call [accept_event()](class_control.md#class_Control_method_accept_event) so no other node receives the event. Once you accept an input, it becomes handled so [Node._unhandled_input()](class_node.md#class_Node_private_method__unhandled_input) will not process it.

Only one **Control** node can be in focus. Only the node in focus will receive events. To get the focus, call [grab_focus()](class_control.md#class_Control_method_grab_focus). **Control** nodes lose focus when another node grabs it, or if you hide the node in focus. Focus will not be represented visually if gained via mouse/touch input, only appearing with keyboard/gamepad input (for accessibility), or via [grab_focus()](class_control.md#class_Control_method_grab_focus).

Set [mouse_filter](class_control.md#class_Control_property_mouse_filter) to [MOUSE_FILTER_IGNORE](class_control.md#class_Control_constant_MOUSE_FILTER_IGNORE) to tell a **Control** node to ignore mouse or touch events. You'll need it if you place an icon on top of a button.

 [Theme](class_theme.md#class_Theme) resources change the control's appearance. The [theme](class_control.md#class_Control_property_theme) of a **Control** node affects all of its direct and indirect children (as long as a chain of controls is uninterrupted). To override some of the theme items, call one of the `add_theme_*_override` methods, like [add_theme_font_override()](class_control.md#class_Control_method_add_theme_font_override). You can also override theme items in the Inspector.

 **Note:** Theme items are *not* [Object](class_object.md#class_Object) properties. This means you can't access their values using [Object.get()](class_object.md#class_Object_method_get) and [Object.set()](class_object.md#class_Object_method_set). Instead, use the `get_theme_*` and `add_theme_*_override` methods provided by this class.

### Tutorials

- [GUI documentation index](../tutorials/ui/index.md)

- [Custom drawing in 2D](../tutorials/2d/custom_drawing_in_2d.md)

- [Control node gallery](../tutorials/ui/control_node_gallery.md)

- [Multiple resolutions](../tutorials/rendering/multiple_resolutions.md)

- All GUI Demos

### Properties


| [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] | [accessibility_controls_nodes](class_control.md#class_Control_property_accessibility_controls_nodes) | `[]` |
| --- | --- | --- |
| [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] | [accessibility_described_by_nodes](class_control.md#class_Control_property_accessibility_described_by_nodes) | `[]` |
| [String](class_string.md#class_String) | [accessibility_description](class_control.md#class_Control_property_accessibility_description) | `""` |
| [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] | [accessibility_flow_to_nodes](class_control.md#class_Control_property_accessibility_flow_to_nodes) | `[]` |
| [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] | [accessibility_labeled_by_nodes](class_control.md#class_Control_property_accessibility_labeled_by_nodes) | `[]` |
| [AccessibilityLiveMode](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode) | [accessibility_live](class_control.md#class_Control_property_accessibility_live) | `0` |
| [String](class_string.md#class_String) | [accessibility_name](class_control.md#class_Control_property_accessibility_name) | `""` |
| [float](class_float.md#class_float) | [anchor_bottom](class_control.md#class_Control_property_anchor_bottom) | `0.0` |
| [float](class_float.md#class_float) | [anchor_left](class_control.md#class_Control_property_anchor_left) | `0.0` |
| [float](class_float.md#class_float) | [anchor_right](class_control.md#class_Control_property_anchor_right) | `0.0` |
| [float](class_float.md#class_float) | [anchor_top](class_control.md#class_Control_property_anchor_top) | `0.0` |
| [bool](class_bool.md#class_bool) | [auto_translate](class_control.md#class_Control_property_auto_translate) |
| [bool](class_bool.md#class_bool) | [clip_contents](class_control.md#class_Control_property_clip_contents) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [custom_minimum_size](class_control.md#class_Control_property_custom_minimum_size) | `Vector2(0, 0)` |
| [FocusBehaviorRecursive](class_control.md#enum_Control_FocusBehaviorRecursive) | [focus_behavior_recursive](class_control.md#class_Control_property_focus_behavior_recursive) | `0` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | [focus_mode](class_control.md#class_Control_property_focus_mode) | `0` |
| [NodePath](class_nodepath.md#class_NodePath) | [focus_neighbor_bottom](class_control.md#class_Control_property_focus_neighbor_bottom) | `NodePath("")` |
| [NodePath](class_nodepath.md#class_NodePath) | [focus_neighbor_left](class_control.md#class_Control_property_focus_neighbor_left) | `NodePath("")` |
| [NodePath](class_nodepath.md#class_NodePath) | [focus_neighbor_right](class_control.md#class_Control_property_focus_neighbor_right) | `NodePath("")` |
| [NodePath](class_nodepath.md#class_NodePath) | [focus_neighbor_top](class_control.md#class_Control_property_focus_neighbor_top) | `NodePath("")` |
| [NodePath](class_nodepath.md#class_NodePath) | [focus_next](class_control.md#class_Control_property_focus_next) | `NodePath("")` |
| [NodePath](class_nodepath.md#class_NodePath) | [focus_previous](class_control.md#class_Control_property_focus_previous) | `NodePath("")` |
| [Vector2](class_vector2.md#class_Vector2) | [global_position](class_control.md#class_Control_property_global_position) |
| [GrowDirection](class_control.md#enum_Control_GrowDirection) | [grow_horizontal](class_control.md#class_Control_property_grow_horizontal) | `1` |
| [GrowDirection](class_control.md#enum_Control_GrowDirection) | [grow_vertical](class_control.md#class_Control_property_grow_vertical) | `1` |
| [LayoutDirection](class_control.md#enum_Control_LayoutDirection) | [layout_direction](class_control.md#class_Control_property_layout_direction) | `0` |
| [bool](class_bool.md#class_bool) | [localize_numeral_system](class_control.md#class_Control_property_localize_numeral_system) | `true` |
| [MouseBehaviorRecursive](class_control.md#enum_Control_MouseBehaviorRecursive) | [mouse_behavior_recursive](class_control.md#class_Control_property_mouse_behavior_recursive) | `0` |
| [CursorShape](class_control.md#enum_Control_CursorShape) | [mouse_default_cursor_shape](class_control.md#class_Control_property_mouse_default_cursor_shape) | `0` |
| [MouseFilter](class_control.md#enum_Control_MouseFilter) | [mouse_filter](class_control.md#class_Control_property_mouse_filter) | `0` |
| [bool](class_bool.md#class_bool) | [mouse_force_pass_scroll_events](class_control.md#class_Control_property_mouse_force_pass_scroll_events) | `true` |
| [float](class_float.md#class_float) | [offset_bottom](class_control.md#class_Control_property_offset_bottom) | `0.0` |
| [float](class_float.md#class_float) | [offset_left](class_control.md#class_Control_property_offset_left) | `0.0` |
| [float](class_float.md#class_float) | [offset_right](class_control.md#class_Control_property_offset_right) | `0.0` |
| [float](class_float.md#class_float) | [offset_top](class_control.md#class_Control_property_offset_top) | `0.0` |
| [PhysicsInterpolationMode](class_node.md#enum_Node_PhysicsInterpolationMode) | physics_interpolation_mode | `2` (overrides [Node](class_node.md#class_Node_property_physics_interpolation_mode)) |
| [Vector2](class_vector2.md#class_Vector2) | [pivot_offset](class_control.md#class_Control_property_pivot_offset) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [pivot_offset_ratio](class_control.md#class_Control_property_pivot_offset_ratio) | `Vector2(0, 0)` |
| [Vector2](class_vector2.md#class_Vector2) | [position](class_control.md#class_Control_property_position) | `Vector2(0, 0)` |
| [float](class_float.md#class_float) | [rotation](class_control.md#class_Control_property_rotation) | `0.0` |
| [float](class_float.md#class_float) | [rotation_degrees](class_control.md#class_Control_property_rotation_degrees) |
| [Vector2](class_vector2.md#class_Vector2) | [scale](class_control.md#class_Control_property_scale) | `Vector2(1, 1)` |
| [Node](class_node.md#class_Node) | [shortcut_context](class_control.md#class_Control_property_shortcut_context) |
| [Vector2](class_vector2.md#class_Vector2) | [size](class_control.md#class_Control_property_size) | `Vector2(0, 0)` |
| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | [size_flags_horizontal](class_control.md#class_Control_property_size_flags_horizontal) | `1` |
| [float](class_float.md#class_float) | [size_flags_stretch_ratio](class_control.md#class_Control_property_size_flags_stretch_ratio) | `1.0` |
| bitfield | \[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] | [size_flags_vertical](class_control.md#class_Control_property_size_flags_vertical) | `1` |
| [Theme](class_theme.md#class_Theme) | [theme](class_control.md#class_Control_property_theme) |
| [StringName](class_stringname.md#class_StringName) | [theme_type_variation](class_control.md#class_Control_property_theme_type_variation) | `&""` |
| [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) | [tooltip_auto_translate_mode](class_control.md#class_Control_property_tooltip_auto_translate_mode) | `0` |
| [String](class_string.md#class_String) | [tooltip_text](class_control.md#class_Control_property_tooltip_text) | `""` |

### Methods


| [String](class_string.md#class_String) | [_accessibility_get_contextual_info](class_control.md#class_Control_private_method__accessibility_get_contextual_info) ( ) | virtual | const |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_can_drop_data](class_control.md#class_Control_private_method__can_drop_data) ( at_position: [Vector2](class_vector2.md#class_Vector2), data: [Variant](class_variant.md#class_Variant) ) | virtual | const |
| void | [_drop_data](class_control.md#class_Control_private_method__drop_data) ( at_position: [Vector2](class_vector2.md#class_Vector2), data: [Variant](class_variant.md#class_Variant) ) virtual |
| [String](class_string.md#class_String) | [_get_accessibility_container_name](class_control.md#class_Control_private_method__get_accessibility_container_name) ( node: [Node](class_node.md#class_Node) ) | virtual | const |
| [Variant](class_variant.md#class_Variant) | [_get_drag_data](class_control.md#class_Control_private_method__get_drag_data) ( at_position: [Vector2](class_vector2.md#class_Vector2) ) virtual |
| [Vector2](class_vector2.md#class_Vector2) | [_get_minimum_size](class_control.md#class_Control_private_method__get_minimum_size) ( ) | virtual | const |
| [String](class_string.md#class_String) | [_get_tooltip](class_control.md#class_Control_private_method__get_tooltip) ( at_position: [Vector2](class_vector2.md#class_Vector2) ) | virtual | const |
| void | [_gui_input](class_control.md#class_Control_private_method__gui_input) ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) virtual |
| [bool](class_bool.md#class_bool) | [_has_point](class_control.md#class_Control_private_method__has_point) ( point: [Vector2](class_vector2.md#class_Vector2) ) | virtual | const |
| [Object](class_object.md#class_Object) | [_make_custom_tooltip](class_control.md#class_Control_private_method__make_custom_tooltip) ( for_text: [String](class_string.md#class_String) ) | virtual | const |
| [Array](class_array.md#class_Array)\[[Vector3i](class_vector3i.md#class_Vector3i)\] | [_structured_text_parser](class_control.md#class_Control_private_method__structured_text_parser) ( args: [Array](class_array.md#class_Array), text: [String](class_string.md#class_String) ) | virtual | const |
| void | [accept_event](class_control.md#class_Control_method_accept_event) ( ) |
| void | [accessibility_drag](class_control.md#class_Control_method_accessibility_drag) ( ) |
| void | [accessibility_drop](class_control.md#class_Control_method_accessibility_drop) ( ) |
| void | [add_theme_color_override](class_control.md#class_Control_method_add_theme_color_override) ( name: [StringName](class_stringname.md#class_StringName), color: [Color](class_color.md#class_Color) ) |
| void | [add_theme_constant_override](class_control.md#class_Control_method_add_theme_constant_override) ( name: [StringName](class_stringname.md#class_StringName), constant: [int](class_int.md#class_int) ) |
| void | [add_theme_font_override](class_control.md#class_Control_method_add_theme_font_override) ( name: [StringName](class_stringname.md#class_StringName), font: [Font](class_font.md#class_Font) ) |
| void | [add_theme_font_size_override](class_control.md#class_Control_method_add_theme_font_size_override) ( name: [StringName](class_stringname.md#class_StringName), font_size: [int](class_int.md#class_int) ) |
| void | [add_theme_icon_override](class_control.md#class_Control_method_add_theme_icon_override) ( name: [StringName](class_stringname.md#class_StringName), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [add_theme_stylebox_override](class_control.md#class_Control_method_add_theme_stylebox_override) ( name: [StringName](class_stringname.md#class_StringName), stylebox: [StyleBox](class_stylebox.md#class_StyleBox) ) |
| void | [begin_bulk_theme_override](class_control.md#class_Control_method_begin_bulk_theme_override) ( ) |
| void | [end_bulk_theme_override](class_control.md#class_Control_method_end_bulk_theme_override) ( ) |
| [Control](class_control.md#class_Control) | [find_next_valid_focus](class_control.md#class_Control_method_find_next_valid_focus) ( ) const |
| [Control](class_control.md#class_Control) | [find_prev_valid_focus](class_control.md#class_Control_method_find_prev_valid_focus) ( ) const |
| [Control](class_control.md#class_Control) | [find_valid_focus_neighbor](class_control.md#class_Control_method_find_valid_focus_neighbor) ( side: Side ) const |
| void | [force_drag](class_control.md#class_Control_method_force_drag) ( data: [Variant](class_variant.md#class_Variant), preview: [Control](class_control.md#class_Control) ) |
| [float](class_float.md#class_float) | [get_anchor](class_control.md#class_Control_method_get_anchor) ( side: Side ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_begin](class_control.md#class_Control_method_get_begin) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_combined_minimum_size](class_control.md#class_Control_method_get_combined_minimum_size) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_combined_pivot_offset](class_control.md#class_Control_method_get_combined_pivot_offset) ( ) const |
| [CursorShape](class_control.md#enum_Control_CursorShape) | [get_cursor_shape](class_control.md#class_Control_method_get_cursor_shape) ( position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_end](class_control.md#class_Control_method_get_end) ( ) const |
| [FocusMode](class_control.md#enum_Control_FocusMode) | [get_focus_mode_with_override](class_control.md#class_Control_method_get_focus_mode_with_override) ( ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_focus_neighbor](class_control.md#class_Control_method_get_focus_neighbor) ( side: Side ) const |
| [Rect2](class_rect2.md#class_Rect2) | [get_global_rect](class_control.md#class_Control_method_get_global_rect) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_minimum_size](class_control.md#class_Control_method_get_minimum_size) ( ) const |
| [MouseFilter](class_control.md#enum_Control_MouseFilter) | [get_mouse_filter_with_override](class_control.md#class_Control_method_get_mouse_filter_with_override) ( ) const |
| [float](class_float.md#class_float) | [get_offset](class_control.md#class_Control_method_get_offset) ( offset: Side ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_parent_area_size](class_control.md#class_Control_method_get_parent_area_size) ( ) const |
| [Control](class_control.md#class_Control) | [get_parent_control](class_control.md#class_Control_method_get_parent_control) ( ) const |
| [Rect2](class_rect2.md#class_Rect2) | [get_rect](class_control.md#class_Control_method_get_rect) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_screen_position](class_control.md#class_Control_method_get_screen_position) ( ) const |
| [Color](class_color.md#class_Color) | [get_theme_color](class_control.md#class_Control_method_get_theme_color) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [int](class_int.md#class_int) | [get_theme_constant](class_control.md#class_Control_method_get_theme_constant) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [float](class_float.md#class_float) | [get_theme_default_base_scale](class_control.md#class_Control_method_get_theme_default_base_scale) ( ) const |
| [Font](class_font.md#class_Font) | [get_theme_default_font](class_control.md#class_Control_method_get_theme_default_font) ( ) const |
| [int](class_int.md#class_int) | [get_theme_default_font_size](class_control.md#class_Control_method_get_theme_default_font_size) ( ) const |
| [Font](class_font.md#class_Font) | [get_theme_font](class_control.md#class_Control_method_get_theme_font) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [int](class_int.md#class_int) | [get_theme_font_size](class_control.md#class_Control_method_get_theme_font_size) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_theme_icon](class_control.md#class_Control_method_get_theme_icon) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [StyleBox](class_stylebox.md#class_StyleBox) | [get_theme_stylebox](class_control.md#class_Control_method_get_theme_stylebox) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [String](class_string.md#class_String) | [get_tooltip](class_control.md#class_Control_method_get_tooltip) ( at_position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) const |
| void | [grab_click_focus](class_control.md#class_Control_method_grab_click_focus) ( ) |
| void | [grab_focus](class_control.md#class_Control_method_grab_focus) ( hide_focus: [bool](class_bool.md#class_bool) = false ) |
| [bool](class_bool.md#class_bool) | [has_focus](class_control.md#class_Control_method_has_focus) ( ignore_hidden_focus: [bool](class_bool.md#class_bool) = false ) const |
| [bool](class_bool.md#class_bool) | [has_theme_color](class_control.md#class_Control_method_has_theme_color) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_color_override](class_control.md#class_Control_method_has_theme_color_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_constant](class_control.md#class_Control_method_has_theme_constant) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_constant_override](class_control.md#class_Control_method_has_theme_constant_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_font](class_control.md#class_Control_method_has_theme_font) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_font_override](class_control.md#class_Control_method_has_theme_font_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_font_size](class_control.md#class_Control_method_has_theme_font_size) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_font_size_override](class_control.md#class_Control_method_has_theme_font_size_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_icon](class_control.md#class_Control_method_has_theme_icon) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_icon_override](class_control.md#class_Control_method_has_theme_icon_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [has_theme_stylebox](class_control.md#class_Control_method_has_theme_stylebox) ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) const |
| [bool](class_bool.md#class_bool) | [has_theme_stylebox_override](class_control.md#class_Control_method_has_theme_stylebox_override) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [is_drag_successful](class_control.md#class_Control_method_is_drag_successful) ( ) const |
| [bool](class_bool.md#class_bool) | [is_layout_rtl](class_control.md#class_Control_method_is_layout_rtl) ( ) const |
| void | [release_focus](class_control.md#class_Control_method_release_focus) ( ) |
| void | [remove_theme_color_override](class_control.md#class_Control_method_remove_theme_color_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_constant_override](class_control.md#class_Control_method_remove_theme_constant_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_font_override](class_control.md#class_Control_method_remove_theme_font_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_font_size_override](class_control.md#class_Control_method_remove_theme_font_size_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_icon_override](class_control.md#class_Control_method_remove_theme_icon_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [remove_theme_stylebox_override](class_control.md#class_Control_method_remove_theme_stylebox_override) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [reset_size](class_control.md#class_Control_method_reset_size) ( ) |
| void | [set_anchor](class_control.md#class_Control_method_set_anchor) ( side: Side, anchor: [float](class_float.md#class_float), keep_offset: [bool](class_bool.md#class_bool) = false, push_opposite_anchor: [bool](class_bool.md#class_bool) = true ) |
| void | [set_anchor_and_offset](class_control.md#class_Control_method_set_anchor_and_offset) ( side: Side, anchor: [float](class_float.md#class_float), offset: [float](class_float.md#class_float), push_opposite_anchor: [bool](class_bool.md#class_bool) = false ) |
| void | [set_anchors_and_offsets_preset](class_control.md#class_Control_method_set_anchors_and_offsets_preset) ( preset: [LayoutPreset](class_control.md#enum_Control_LayoutPreset), resize_mode: [LayoutPresetMode](class_control.md#enum_Control_LayoutPresetMode) = 0, margin: [int](class_int.md#class_int) = 0 ) |
| void | [set_anchors_preset](class_control.md#class_Control_method_set_anchors_preset) ( preset: [LayoutPreset](class_control.md#enum_Control_LayoutPreset), keep_offsets: [bool](class_bool.md#class_bool) = false ) |
| void | [set_begin](class_control.md#class_Control_method_set_begin) ( position: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_drag_forwarding](class_control.md#class_Control_method_set_drag_forwarding) ( drag_func: [Callable](class_callable.md#class_Callable), can_drop_func: [Callable](class_callable.md#class_Callable), drop_func: [Callable](class_callable.md#class_Callable) ) |
| void | [set_drag_preview](class_control.md#class_Control_method_set_drag_preview) ( control: [Control](class_control.md#class_Control) ) |
| void | [set_end](class_control.md#class_Control_method_set_end) ( position: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_focus_neighbor](class_control.md#class_Control_method_set_focus_neighbor) ( side: Side, neighbor: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [set_global_position](class_control.md#class_Control_method_set_global_position) ( position: [Vector2](class_vector2.md#class_Vector2), keep_offsets: [bool](class_bool.md#class_bool) = false ) |
| void | [set_offset](class_control.md#class_Control_method_set_offset) ( side: Side, offset: [float](class_float.md#class_float) ) |
| void | [set_offsets_preset](class_control.md#class_Control_method_set_offsets_preset) ( preset: [LayoutPreset](class_control.md#enum_Control_LayoutPreset), resize_mode: [LayoutPresetMode](class_control.md#enum_Control_LayoutPresetMode) = 0, margin: [int](class_int.md#class_int) = 0 ) |
| void | [set_position](class_control.md#class_Control_method_set_position) ( position: [Vector2](class_vector2.md#class_Vector2), keep_offsets: [bool](class_bool.md#class_bool) = false ) |
| void | [set_size](class_control.md#class_Control_method_set_size) ( size: [Vector2](class_vector2.md#class_Vector2), keep_offsets: [bool](class_bool.md#class_bool) = false ) |
| void | [update_minimum_size](class_control.md#class_Control_method_update_minimum_size) ( ) |
| void | [warp_mouse](class_control.md#class_Control_method_warp_mouse) ( position: [Vector2](class_vector2.md#class_Vector2) ) |

---

### Signals

<span id="class_Control_signal_focus_entered"></span>

**focus_entered** ( ) [🔗](class_control.md#class_Control_signal_focus_entered)

Emitted when the node gains focus.

---

<span id="class_Control_signal_focus_exited"></span>

**focus_exited** ( ) [🔗](class_control.md#class_Control_signal_focus_exited)

Emitted when the node loses focus.

---

<span id="class_Control_signal_gui_input"></span>

**gui_input** ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) [🔗](class_control.md#class_Control_signal_gui_input)

Emitted when the node receives an [InputEvent](class_inputevent.md#class_InputEvent).

---

<span id="class_Control_signal_minimum_size_changed"></span>

**minimum_size_changed** ( ) [🔗](class_control.md#class_Control_signal_minimum_size_changed)

Emitted when the node's minimum size changes.

---

<span id="class_Control_signal_mouse_entered"></span>

**mouse_entered** ( ) [🔗](class_control.md#class_Control_signal_mouse_entered)

Emitted when the mouse cursor enters the control's (or any child control's) visible area, that is not occluded behind other Controls or Windows, provided its [mouse_filter](class_control.md#class_Control_property_mouse_filter) lets the event reach it and regardless if it's currently focused or not.

 **Note:** [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) doesn't affect, which Control receives the signal.

---

<span id="class_Control_signal_mouse_exited"></span>

**mouse_exited** ( ) [🔗](class_control.md#class_Control_signal_mouse_exited)

Emitted when the mouse cursor leaves the control's (and all child control's) visible area, that is not occluded behind other Controls or Windows, provided its [mouse_filter](class_control.md#class_Control_property_mouse_filter) lets the event reach it and regardless if it's currently focused or not.

 **Note:** [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) doesn't affect, which Control receives the signal.

 **Note:** If you want to check whether the mouse truly left the area, ignoring any top nodes, you can use code like this:

::

    func _on_mouse_exited():
        if not Rect2(Vector2(), size).has_point(get_local_mouse_position()):
            # Not hovering over area.

---

<span id="class_Control_signal_resized"></span>

**resized** ( ) [🔗](class_control.md#class_Control_signal_resized)

Emitted when the control changes size.

---

<span id="class_Control_signal_size_flags_changed"></span>

**size_flags_changed** ( ) [🔗](class_control.md#class_Control_signal_size_flags_changed)

Emitted when one of the size flags changes. See [size_flags_horizontal](class_control.md#class_Control_property_size_flags_horizontal) and [size_flags_vertical](class_control.md#class_Control_property_size_flags_vertical).

---

<span id="class_Control_signal_theme_changed"></span>

**theme_changed** ( ) [🔗](class_control.md#class_Control_signal_theme_changed)

Emitted when the [NOTIFICATION_THEME_CHANGED](class_control.md#class_Control_constant_NOTIFICATION_THEME_CHANGED) notification is sent.

---

### Enumerations

<span id="enum_Control_FocusMode"></span>

enum **FocusMode**: [🔗](class_control.md#enum_Control_FocusMode)

<span id="class_Control_constant_FOCUS_NONE"></span>

[FocusMode](class_control.md#enum_Control_FocusMode) **FOCUS_NONE** = `0`

The node cannot grab focus. Use with [focus_mode](class_control.md#class_Control_property_focus_mode).

<span id="class_Control_constant_FOCUS_CLICK"></span>

[FocusMode](class_control.md#enum_Control_FocusMode) **FOCUS_CLICK** = `1`

The node can only grab focus on mouse clicks. Use with [focus_mode](class_control.md#class_Control_property_focus_mode).

<span id="class_Control_constant_FOCUS_ALL"></span>

[FocusMode](class_control.md#enum_Control_FocusMode) **FOCUS_ALL** = `2`

The node can grab focus on mouse click, using the arrows and the Tab keys on the keyboard, or using the D-pad buttons on a gamepad. Use with [focus_mode](class_control.md#class_Control_property_focus_mode).

<span id="class_Control_constant_FOCUS_ACCESSIBILITY"></span>

[FocusMode](class_control.md#enum_Control_FocusMode) **FOCUS_ACCESSIBILITY** = `3`

The node can grab focus only when screen reader is active. Use with [focus_mode](class_control.md#class_Control_property_focus_mode).

---

<span id="enum_Control_FocusBehaviorRecursive"></span>

enum **FocusBehaviorRecursive**: [🔗](class_control.md#enum_Control_FocusBehaviorRecursive)

<span id="class_Control_constant_FOCUS_BEHAVIOR_INHERITED"></span>

[FocusBehaviorRecursive](class_control.md#enum_Control_FocusBehaviorRecursive) **FOCUS_BEHAVIOR_INHERITED** = `0`

Inherits the [focus_behavior_recursive](class_control.md#class_Control_property_focus_behavior_recursive) from the parent control. If there is no parent control, this is the same as [FOCUS_BEHAVIOR_ENABLED](class_control.md#class_Control_constant_FOCUS_BEHAVIOR_ENABLED).

<span id="class_Control_constant_FOCUS_BEHAVIOR_DISABLED"></span>

[FocusBehaviorRecursive](class_control.md#enum_Control_FocusBehaviorRecursive) **FOCUS_BEHAVIOR_DISABLED** = `1`

Prevents the control from getting focused. [get_focus_mode_with_override()](class_control.md#class_Control_method_get_focus_mode_with_override) will return [FOCUS_NONE](class_control.md#class_Control_constant_FOCUS_NONE).

<span id="class_Control_constant_FOCUS_BEHAVIOR_ENABLED"></span>

[FocusBehaviorRecursive](class_control.md#enum_Control_FocusBehaviorRecursive) **FOCUS_BEHAVIOR_ENABLED** = `2`

Allows the control to be focused, depending on the [focus_mode](class_control.md#class_Control_property_focus_mode). This can be used to ignore the parent's [focus_behavior_recursive](class_control.md#class_Control_property_focus_behavior_recursive). [get_focus_mode_with_override()](class_control.md#class_Control_method_get_focus_mode_with_override) will return the [focus_mode](class_control.md#class_Control_property_focus_mode).

---

<span id="enum_Control_MouseBehaviorRecursive"></span>

enum **MouseBehaviorRecursive**: [🔗](class_control.md#enum_Control_MouseBehaviorRecursive)

<span id="class_Control_constant_MOUSE_BEHAVIOR_INHERITED"></span>

[MouseBehaviorRecursive](class_control.md#enum_Control_MouseBehaviorRecursive) **MOUSE_BEHAVIOR_INHERITED** = `0`

Inherits the [mouse_behavior_recursive](class_control.md#class_Control_property_mouse_behavior_recursive) from the parent control. If there is no parent control, this is the same as [MOUSE_BEHAVIOR_ENABLED](class_control.md#class_Control_constant_MOUSE_BEHAVIOR_ENABLED).

<span id="class_Control_constant_MOUSE_BEHAVIOR_DISABLED"></span>

[MouseBehaviorRecursive](class_control.md#enum_Control_MouseBehaviorRecursive) **MOUSE_BEHAVIOR_DISABLED** = `1`

Prevents the control from receiving mouse input. [get_mouse_filter_with_override()](class_control.md#class_Control_method_get_mouse_filter_with_override) will return [MOUSE_FILTER_IGNORE](class_control.md#class_Control_constant_MOUSE_FILTER_IGNORE).

<span id="class_Control_constant_MOUSE_BEHAVIOR_ENABLED"></span>

[MouseBehaviorRecursive](class_control.md#enum_Control_MouseBehaviorRecursive) **MOUSE_BEHAVIOR_ENABLED** = `2`

Allows the control to receive mouse input, depending on the [mouse_filter](class_control.md#class_Control_property_mouse_filter). This can be used to ignore the parent's [mouse_behavior_recursive](class_control.md#class_Control_property_mouse_behavior_recursive). [get_mouse_filter_with_override()](class_control.md#class_Control_method_get_mouse_filter_with_override) will return the [mouse_filter](class_control.md#class_Control_property_mouse_filter).

---

<span id="enum_Control_CursorShape"></span>

enum **CursorShape**: [🔗](class_control.md#enum_Control_CursorShape)

<span id="class_Control_constant_CURSOR_ARROW"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_ARROW** = `0`

Show the system's arrow mouse cursor when the user hovers the node. Use with [mouse_default_cursor_shape](class_control.md#class_Control_property_mouse_default_cursor_shape).

<span id="class_Control_constant_CURSOR_IBEAM"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_IBEAM** = `1`

Show the system's I-beam mouse cursor when the user hovers the node. The I-beam pointer has a shape similar to "I". It tells the user they can highlight or insert text.

<span id="class_Control_constant_CURSOR_POINTING_HAND"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_POINTING_HAND** = `2`

Show the system's pointing hand mouse cursor when the user hovers the node.

<span id="class_Control_constant_CURSOR_CROSS"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_CROSS** = `3`

Show the system's cross mouse cursor when the user hovers the node.

<span id="class_Control_constant_CURSOR_WAIT"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_WAIT** = `4`

Show the system's wait mouse cursor when the user hovers the node. Often an hourglass.

<span id="class_Control_constant_CURSOR_BUSY"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_BUSY** = `5`

Show the system's busy mouse cursor when the user hovers the node. Often an arrow with a small hourglass.

<span id="class_Control_constant_CURSOR_DRAG"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_DRAG** = `6`

Show the system's drag mouse cursor, often a closed fist or a cross symbol, when the user hovers the node. It tells the user they're currently dragging an item, like a node in the Scene dock.

<span id="class_Control_constant_CURSOR_CAN_DROP"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_CAN_DROP** = `7`

Show the system's drop mouse cursor when the user hovers the node. It can be an open hand. It tells the user they can drop an item they're currently grabbing, like a node in the Scene dock.

<span id="class_Control_constant_CURSOR_FORBIDDEN"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_FORBIDDEN** = `8`

Show the system's forbidden mouse cursor when the user hovers the node. Often a crossed circle.

<span id="class_Control_constant_CURSOR_VSIZE"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_VSIZE** = `9`

Show the system's vertical resize mouse cursor when the user hovers the node. A double-headed vertical arrow. It tells the user they can resize the window or the panel vertically.

<span id="class_Control_constant_CURSOR_HSIZE"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_HSIZE** = `10`

Show the system's horizontal resize mouse cursor when the user hovers the node. A double-headed horizontal arrow. It tells the user they can resize the window or the panel horizontally.

<span id="class_Control_constant_CURSOR_BDIAGSIZE"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_BDIAGSIZE** = `11`

Show the system's window resize mouse cursor when the user hovers the node. The cursor is a double-headed arrow that goes from the bottom left to the top right. It tells the user they can resize the window or the panel both horizontally and vertically.

<span id="class_Control_constant_CURSOR_FDIAGSIZE"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_FDIAGSIZE** = `12`

Show the system's window resize mouse cursor when the user hovers the node. The cursor is a double-headed arrow that goes from the top left to the bottom right, the opposite of [CURSOR_BDIAGSIZE](class_control.md#class_Control_constant_CURSOR_BDIAGSIZE). It tells the user they can resize the window or the panel both horizontally and vertically.

<span id="class_Control_constant_CURSOR_MOVE"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_MOVE** = `13`

Show the system's move mouse cursor when the user hovers the node. It shows 2 double-headed arrows at a 90 degree angle. It tells the user they can move a UI element freely.

<span id="class_Control_constant_CURSOR_VSPLIT"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_VSPLIT** = `14`

Show the system's vertical split mouse cursor when the user hovers the node. On Windows, it's the same as [CURSOR_VSIZE](class_control.md#class_Control_constant_CURSOR_VSIZE).

<span id="class_Control_constant_CURSOR_HSPLIT"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_HSPLIT** = `15`

Show the system's horizontal split mouse cursor when the user hovers the node. On Windows, it's the same as [CURSOR_HSIZE](class_control.md#class_Control_constant_CURSOR_HSIZE).

<span id="class_Control_constant_CURSOR_HELP"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **CURSOR_HELP** = `16`

Show the system's help mouse cursor when the user hovers the node, a question mark.

---

<span id="enum_Control_LayoutPreset"></span>

enum **LayoutPreset**: [🔗](class_control.md#enum_Control_LayoutPreset)

<span id="class_Control_constant_PRESET_TOP_LEFT"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_TOP_LEFT** = `0`

Snap all 4 anchors to the top-left of the parent control's bounds. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_TOP_RIGHT"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_TOP_RIGHT** = `1`

Snap all 4 anchors to the top-right of the parent control's bounds. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_BOTTOM_LEFT"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_BOTTOM_LEFT** = `2`

Snap all 4 anchors to the bottom-left of the parent control's bounds. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_BOTTOM_RIGHT"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_BOTTOM_RIGHT** = `3`

Snap all 4 anchors to the bottom-right of the parent control's bounds. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_CENTER_LEFT"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_CENTER_LEFT** = `4`

Snap all 4 anchors to the center of the left edge of the parent control's bounds. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_CENTER_TOP"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_CENTER_TOP** = `5`

Snap all 4 anchors to the center of the top edge of the parent control's bounds. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_CENTER_RIGHT"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_CENTER_RIGHT** = `6`

Snap all 4 anchors to the center of the right edge of the parent control's bounds. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_CENTER_BOTTOM"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_CENTER_BOTTOM** = `7`

Snap all 4 anchors to the center of the bottom edge of the parent control's bounds. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_CENTER"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_CENTER** = `8`

Snap all 4 anchors to the center of the parent control's bounds. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_LEFT_WIDE"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_LEFT_WIDE** = `9`

Snap all 4 anchors to the left edge of the parent control. The left offset becomes relative to the left edge and the top offset relative to the top left corner of the node's parent. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_TOP_WIDE"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_TOP_WIDE** = `10`

Snap all 4 anchors to the top edge of the parent control. The left offset becomes relative to the top left corner, the top offset relative to the top edge, and the right offset relative to the top right corner of the node's parent. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_RIGHT_WIDE"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_RIGHT_WIDE** = `11`

Snap all 4 anchors to the right edge of the parent control. The right offset becomes relative to the right edge and the top offset relative to the top right corner of the node's parent. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_BOTTOM_WIDE"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_BOTTOM_WIDE** = `12`

Snap all 4 anchors to the bottom edge of the parent control. The left offset becomes relative to the bottom left corner, the bottom offset relative to the bottom edge, and the right offset relative to the bottom right corner of the node's parent. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_VCENTER_WIDE"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_VCENTER_WIDE** = `13`

Snap all 4 anchors to a vertical line that cuts the parent control in half. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_HCENTER_WIDE"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_HCENTER_WIDE** = `14`

Snap all 4 anchors to a horizontal line that cuts the parent control in half. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_PRESET_FULL_RECT"></span>

[LayoutPreset](class_control.md#enum_Control_LayoutPreset) **PRESET_FULL_RECT** = `15`

Snap all 4 anchors to the respective corners of the parent control. Set all 4 offsets to 0 after you applied this preset and the **Control** will fit its parent control. Use with [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

---

<span id="enum_Control_LayoutPresetMode"></span>

enum **LayoutPresetMode**: [🔗](class_control.md#enum_Control_LayoutPresetMode)

<span id="class_Control_constant_PRESET_MODE_MINSIZE"></span>

[LayoutPresetMode](class_control.md#enum_Control_LayoutPresetMode) **PRESET_MODE_MINSIZE** = `0`

The control will be resized to its minimum size.

<span id="class_Control_constant_PRESET_MODE_KEEP_WIDTH"></span>

[LayoutPresetMode](class_control.md#enum_Control_LayoutPresetMode) **PRESET_MODE_KEEP_WIDTH** = `1`

The control's width will not change.

<span id="class_Control_constant_PRESET_MODE_KEEP_HEIGHT"></span>

[LayoutPresetMode](class_control.md#enum_Control_LayoutPresetMode) **PRESET_MODE_KEEP_HEIGHT** = `2`

The control's height will not change.

<span id="class_Control_constant_PRESET_MODE_KEEP_SIZE"></span>

[LayoutPresetMode](class_control.md#enum_Control_LayoutPresetMode) **PRESET_MODE_KEEP_SIZE** = `3`

The control's size will not change.

---

<span id="enum_Control_SizeFlags"></span>

flags **SizeFlags**: [🔗](class_control.md#enum_Control_SizeFlags)

<span id="class_Control_constant_SIZE_SHRINK_BEGIN"></span>

[SizeFlags](class_control.md#enum_Control_SizeFlags) **SIZE_SHRINK_BEGIN** = `0`

Tells the parent [Container](class_container.md#class_Container) to align the node with its start, either the top or the left edge. It is mutually exclusive with [SIZE_FILL](class_control.md#class_Control_constant_SIZE_FILL) and other shrink size flags, but can be used with [SIZE_EXPAND](class_control.md#class_Control_constant_SIZE_EXPAND) in some containers. Use with [size_flags_horizontal](class_control.md#class_Control_property_size_flags_horizontal) and [size_flags_vertical](class_control.md#class_Control_property_size_flags_vertical).

 **Note:** Setting this flag is equal to not having any size flags.

<span id="class_Control_constant_SIZE_FILL"></span>

[SizeFlags](class_control.md#enum_Control_SizeFlags) **SIZE_FILL** = `1`

Tells the parent [Container](class_container.md#class_Container) to expand the bounds of this node to fill all the available space without pushing any other node. It is mutually exclusive with shrink size flags. Use with [size_flags_horizontal](class_control.md#class_Control_property_size_flags_horizontal) and [size_flags_vertical](class_control.md#class_Control_property_size_flags_vertical).

<span id="class_Control_constant_SIZE_EXPAND"></span>

[SizeFlags](class_control.md#enum_Control_SizeFlags) **SIZE_EXPAND** = `2`

Tells the parent [Container](class_container.md#class_Container) to let this node take all the available space on the axis you flag. If multiple neighboring nodes are set to expand, they'll share the space based on their stretch ratio. See [size_flags_stretch_ratio](class_control.md#class_Control_property_size_flags_stretch_ratio). Use with [size_flags_horizontal](class_control.md#class_Control_property_size_flags_horizontal) and [size_flags_vertical](class_control.md#class_Control_property_size_flags_vertical).

<span id="class_Control_constant_SIZE_EXPAND_FILL"></span>

[SizeFlags](class_control.md#enum_Control_SizeFlags) **SIZE_EXPAND_FILL** = `3`

Sets the node's size flags to both fill and expand. See [SIZE_FILL](class_control.md#class_Control_constant_SIZE_FILL) and [SIZE_EXPAND](class_control.md#class_Control_constant_SIZE_EXPAND) for more information.

<span id="class_Control_constant_SIZE_SHRINK_CENTER"></span>

[SizeFlags](class_control.md#enum_Control_SizeFlags) **SIZE_SHRINK_CENTER** = `4`

Tells the parent [Container](class_container.md#class_Container) to center the node in the available space. It is mutually exclusive with [SIZE_FILL](class_control.md#class_Control_constant_SIZE_FILL) and other shrink size flags, but can be used with [SIZE_EXPAND](class_control.md#class_Control_constant_SIZE_EXPAND) in some containers. Use with [size_flags_horizontal](class_control.md#class_Control_property_size_flags_horizontal) and [size_flags_vertical](class_control.md#class_Control_property_size_flags_vertical).

<span id="class_Control_constant_SIZE_SHRINK_END"></span>

[SizeFlags](class_control.md#enum_Control_SizeFlags) **SIZE_SHRINK_END** = `8`

Tells the parent [Container](class_container.md#class_Container) to align the node with its end, either the bottom or the right edge. It is mutually exclusive with [SIZE_FILL](class_control.md#class_Control_constant_SIZE_FILL) and other shrink size flags, but can be used with [SIZE_EXPAND](class_control.md#class_Control_constant_SIZE_EXPAND) in some containers. Use with [size_flags_horizontal](class_control.md#class_Control_property_size_flags_horizontal) and [size_flags_vertical](class_control.md#class_Control_property_size_flags_vertical).

---

<span id="enum_Control_MouseFilter"></span>

enum **MouseFilter**: [🔗](class_control.md#enum_Control_MouseFilter)

<span id="class_Control_constant_MOUSE_FILTER_STOP"></span>

[MouseFilter](class_control.md#enum_Control_MouseFilter) **MOUSE_FILTER_STOP** = `0`

The control will receive mouse movement input events and mouse button input events if clicked on through [_gui_input()](class_control.md#class_Control_private_method__gui_input). The control will also receive the [mouse_entered](class_control.md#class_Control_signal_mouse_entered) and [mouse_exited](class_control.md#class_Control_signal_mouse_exited) signals. These events are automatically marked as handled, and they will not propagate further to other controls. This also results in blocking signals in other controls.

<span id="class_Control_constant_MOUSE_FILTER_PASS"></span>

[MouseFilter](class_control.md#enum_Control_MouseFilter) **MOUSE_FILTER_PASS** = `1`

The control will receive mouse movement input events and mouse button input events if clicked on through [_gui_input()](class_control.md#class_Control_private_method__gui_input). The control will also receive the [mouse_entered](class_control.md#class_Control_signal_mouse_entered) and [mouse_exited](class_control.md#class_Control_signal_mouse_exited) signals.

If this control does not handle the event, the event will propagate up to its parent control if it has one. The event is bubbled up the node hierarchy until it reaches a non-[CanvasItem](class_canvasitem.md#class_CanvasItem), a control with [MOUSE_FILTER_STOP](class_control.md#class_Control_constant_MOUSE_FILTER_STOP), or a [CanvasItem](class_canvasitem.md#class_CanvasItem) with [CanvasItem.top_level](class_canvasitem.md#class_CanvasItem_property_top_level) enabled. This will allow signals to fire in all controls it reaches. If no control handled it, the event will be passed to [Node._shortcut_input()](class_node.md#class_Node_private_method__shortcut_input) for further processing.

<span id="class_Control_constant_MOUSE_FILTER_IGNORE"></span>

[MouseFilter](class_control.md#enum_Control_MouseFilter) **MOUSE_FILTER_IGNORE** = `2`

The control will not receive any mouse movement input events nor mouse button input events through [_gui_input()](class_control.md#class_Control_private_method__gui_input). The control will also not receive the [mouse_entered](class_control.md#class_Control_signal_mouse_entered) nor [mouse_exited](class_control.md#class_Control_signal_mouse_exited) signals. This will not block other controls from receiving these events or firing the signals. Ignored events will not be handled automatically. If a child has [MOUSE_FILTER_PASS](class_control.md#class_Control_constant_MOUSE_FILTER_PASS) and an event was passed to this control, the event will further propagate up to the control's parent.

 **Note:** If the control has received [mouse_entered](class_control.md#class_Control_signal_mouse_entered) but not [mouse_exited](class_control.md#class_Control_signal_mouse_exited), changing the [mouse_filter](class_control.md#class_Control_property_mouse_filter) to [MOUSE_FILTER_IGNORE](class_control.md#class_Control_constant_MOUSE_FILTER_IGNORE) will cause [mouse_exited](class_control.md#class_Control_signal_mouse_exited) to be emitted.

---

<span id="enum_Control_GrowDirection"></span>

enum **GrowDirection**: [🔗](class_control.md#enum_Control_GrowDirection)

<span id="class_Control_constant_GROW_DIRECTION_BEGIN"></span>

[GrowDirection](class_control.md#enum_Control_GrowDirection) **GROW_DIRECTION_BEGIN** = `0`

The control will grow to the left or top to make up if its minimum size is changed to be greater than its current size on the respective axis.

<span id="class_Control_constant_GROW_DIRECTION_END"></span>

[GrowDirection](class_control.md#enum_Control_GrowDirection) **GROW_DIRECTION_END** = `1`

The control will grow to the right or bottom to make up if its minimum size is changed to be greater than its current size on the respective axis.

<span id="class_Control_constant_GROW_DIRECTION_BOTH"></span>

[GrowDirection](class_control.md#enum_Control_GrowDirection) **GROW_DIRECTION_BOTH** = `2`

The control will grow in both directions equally to make up if its minimum size is changed to be greater than its current size.

---

<span id="enum_Control_Anchor"></span>

enum **Anchor**: [🔗](class_control.md#enum_Control_Anchor)

<span id="class_Control_constant_ANCHOR_BEGIN"></span>

[Anchor](class_control.md#enum_Control_Anchor) **ANCHOR_BEGIN** = `0`

Snaps one of the 4 anchor's sides to the origin of the node's `Rect`, in the top left. Use it with one of the `anchor_*` member variables, like [anchor_left](class_control.md#class_Control_property_anchor_left). To change all 4 anchors at once, use [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

<span id="class_Control_constant_ANCHOR_END"></span>

[Anchor](class_control.md#enum_Control_Anchor) **ANCHOR_END** = `1`

Snaps one of the 4 anchor's sides to the end of the node's `Rect`, in the bottom right. Use it with one of the `anchor_*` member variables, like [anchor_left](class_control.md#class_Control_property_anchor_left). To change all 4 anchors at once, use [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset).

---

<span id="enum_Control_LayoutDirection"></span>

enum **LayoutDirection**: [🔗](class_control.md#enum_Control_LayoutDirection)

<span id="class_Control_constant_LAYOUT_DIRECTION_INHERITED"></span>

[LayoutDirection](class_control.md#enum_Control_LayoutDirection) **LAYOUT_DIRECTION_INHERITED** = `0`

Automatic layout direction, determined from the parent control layout direction.

<span id="class_Control_constant_LAYOUT_DIRECTION_APPLICATION_LOCALE"></span>

[LayoutDirection](class_control.md#enum_Control_LayoutDirection) **LAYOUT_DIRECTION_APPLICATION_LOCALE** = `1`

Automatic layout direction, determined from the current locale. Right-to-left layout direction is automatically used for languages that require it such as Arabic and Hebrew, but only if a valid translation file is loaded for the given language (unless said language is configured as a fallback in ProjectSettings.internationalization/locale/fallback). For all other languages (or if no valid translation file is found by Godot), left-to-right layout direction is used. If using [TextServerFallback](class_textserverfallback.md#class_TextServerFallback) (ProjectSettings.internationalization/rendering/text_driver), left-to-right layout direction is always used regardless of the language. Right-to-left layout direction can also be forced using ProjectSettings.internationalization/rendering/force_right_to_left_layout_direction.

<span id="class_Control_constant_LAYOUT_DIRECTION_LTR"></span>

[LayoutDirection](class_control.md#enum_Control_LayoutDirection) **LAYOUT_DIRECTION_LTR** = `2`

Left-to-right layout direction.

<span id="class_Control_constant_LAYOUT_DIRECTION_RTL"></span>

[LayoutDirection](class_control.md#enum_Control_LayoutDirection) **LAYOUT_DIRECTION_RTL** = `3`

Right-to-left layout direction.

<span id="class_Control_constant_LAYOUT_DIRECTION_SYSTEM_LOCALE"></span>

[LayoutDirection](class_control.md#enum_Control_LayoutDirection) **LAYOUT_DIRECTION_SYSTEM_LOCALE** = `4`

Automatic layout direction, determined from the system locale. Right-to-left layout direction is automatically used for languages that require it such as Arabic and Hebrew, but only if a valid translation file is loaded for the given language. For all other languages (or if no valid translation file is found by Godot), left-to-right layout direction is used. If using [TextServerFallback](class_textserverfallback.md#class_TextServerFallback) (ProjectSettings.internationalization/rendering/text_driver), left-to-right layout direction is always used regardless of the language.

<span id="class_Control_constant_LAYOUT_DIRECTION_MAX"></span>

[LayoutDirection](class_control.md#enum_Control_LayoutDirection) **LAYOUT_DIRECTION_MAX** = `5`

Represents the size of the [LayoutDirection](class_control.md#enum_Control_LayoutDirection) enum.

<span id="class_Control_constant_LAYOUT_DIRECTION_LOCALE"></span>

[LayoutDirection](class_control.md#enum_Control_LayoutDirection) **LAYOUT_DIRECTION_LOCALE** = `1`

**Deprecated:** Use [LAYOUT_DIRECTION_APPLICATION_LOCALE](class_control.md#class_Control_constant_LAYOUT_DIRECTION_APPLICATION_LOCALE) instead.

---

<span id="enum_Control_TextDirection"></span>

enum **TextDirection**: [🔗](class_control.md#enum_Control_TextDirection)

<span id="class_Control_constant_TEXT_DIRECTION_INHERITED"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **TEXT_DIRECTION_INHERITED** = `3`

Text writing direction is the same as layout direction.

<span id="class_Control_constant_TEXT_DIRECTION_AUTO"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **TEXT_DIRECTION_AUTO** = `0`

Automatic text writing direction, determined from the current locale and text content.

<span id="class_Control_constant_TEXT_DIRECTION_LTR"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **TEXT_DIRECTION_LTR** = `1`

Left-to-right text writing direction.

<span id="class_Control_constant_TEXT_DIRECTION_RTL"></span>

[TextDirection](class_control.md#enum_Control_TextDirection) **TEXT_DIRECTION_RTL** = `2`

Right-to-left text writing direction.

---

### Constants

<span id="class_Control_constant_NOTIFICATION_RESIZED"></span>

**NOTIFICATION_RESIZED** = `40` [🔗](class_control.md#class_Control_constant_NOTIFICATION_RESIZED)

Sent when the node changes size. Use [size](class_control.md#class_Control_property_size) to get the new size.

<span id="class_Control_constant_NOTIFICATION_MOUSE_ENTER"></span>

**NOTIFICATION_MOUSE_ENTER** = `41` [🔗](class_control.md#class_Control_constant_NOTIFICATION_MOUSE_ENTER)

Sent when the mouse cursor enters the control's (or any child control's) visible area, that is not occluded behind other Controls or Windows, provided its [mouse_filter](class_control.md#class_Control_property_mouse_filter) lets the event reach it and regardless if it's currently focused or not.

 **Note:** [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) doesn't affect which Control receives the notification.

See also [NOTIFICATION_MOUSE_ENTER_SELF](class_control.md#class_Control_constant_NOTIFICATION_MOUSE_ENTER_SELF).

<span id="class_Control_constant_NOTIFICATION_MOUSE_EXIT"></span>

**NOTIFICATION_MOUSE_EXIT** = `42` [🔗](class_control.md#class_Control_constant_NOTIFICATION_MOUSE_EXIT)

Sent when the mouse cursor leaves the control's (and all child control's) visible area, that is not occluded behind other Controls or Windows, provided its [mouse_filter](class_control.md#class_Control_property_mouse_filter) lets the event reach it and regardless if it's currently focused or not.

 **Note:** [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) doesn't affect which Control receives the notification.

See also [NOTIFICATION_MOUSE_EXIT_SELF](class_control.md#class_Control_constant_NOTIFICATION_MOUSE_EXIT_SELF).

<span id="class_Control_constant_NOTIFICATION_MOUSE_ENTER_SELF"></span>

**NOTIFICATION_MOUSE_ENTER_SELF** = `60` [🔗](class_control.md#class_Control_constant_NOTIFICATION_MOUSE_ENTER_SELF)

**Experimental:** The reason this notification is sent may change in the future.

Sent when the mouse cursor enters the control's visible area, that is not occluded behind other Controls or Windows, provided its [mouse_filter](class_control.md#class_Control_property_mouse_filter) lets the event reach it and regardless if it's currently focused or not.

 **Note:** [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) doesn't affect which Control receives the notification.

See also [NOTIFICATION_MOUSE_ENTER](class_control.md#class_Control_constant_NOTIFICATION_MOUSE_ENTER).

<span id="class_Control_constant_NOTIFICATION_MOUSE_EXIT_SELF"></span>

**NOTIFICATION_MOUSE_EXIT_SELF** = `61` [🔗](class_control.md#class_Control_constant_NOTIFICATION_MOUSE_EXIT_SELF)

**Experimental:** The reason this notification is sent may change in the future.

Sent when the mouse cursor leaves the control's visible area, that is not occluded behind other Controls or Windows, provided its [mouse_filter](class_control.md#class_Control_property_mouse_filter) lets the event reach it and regardless if it's currently focused or not.

 **Note:** [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) doesn't affect which Control receives the notification.

See also [NOTIFICATION_MOUSE_EXIT](class_control.md#class_Control_constant_NOTIFICATION_MOUSE_EXIT).

<span id="class_Control_constant_NOTIFICATION_FOCUS_ENTER"></span>

**NOTIFICATION_FOCUS_ENTER** = `43` [🔗](class_control.md#class_Control_constant_NOTIFICATION_FOCUS_ENTER)

Sent when the node grabs focus.

<span id="class_Control_constant_NOTIFICATION_FOCUS_EXIT"></span>

**NOTIFICATION_FOCUS_EXIT** = `44` [🔗](class_control.md#class_Control_constant_NOTIFICATION_FOCUS_EXIT)

Sent when the node loses focus.

This notification is sent in reversed order.

<span id="class_Control_constant_NOTIFICATION_THEME_CHANGED"></span>

**NOTIFICATION_THEME_CHANGED** = `45` [🔗](class_control.md#class_Control_constant_NOTIFICATION_THEME_CHANGED)

Sent when the node needs to refresh its theme items. This happens in one of the following cases:

- The [theme](class_control.md#class_Control_property_theme) property is changed on this node or any of its ancestors.

- The [theme_type_variation](class_control.md#class_Control_property_theme_type_variation) property is changed on this node.

- One of the node's theme property overrides is changed.

- The node enters the scene tree.

 **Note:** As an optimization, this notification won't be sent from changes that occur while this node is outside of the scene tree. Instead, all of the theme item updates can be applied at once when the node enters the scene tree.

 **Note:** This notification is received alongside [Node.NOTIFICATION_ENTER_TREE](class_node.md#class_Node_constant_NOTIFICATION_ENTER_TREE), so if you are instantiating a scene, the child nodes will not be initialized yet. You can use it to setup theming for this node, child nodes created from script, or if you want to access child nodes added in the editor, make sure the node is ready using [Node.is_node_ready()](class_node.md#class_Node_method_is_node_ready).

::

    func _notification(what):
        if what == NOTIFICATION_THEME_CHANGED:
            if not is_node_ready():
                await ready # Wait until ready signal.
            $Label.add_theme_color_override("font_color", Color.YELLOW)

<span id="class_Control_constant_NOTIFICATION_SCROLL_BEGIN"></span>

**NOTIFICATION_SCROLL_BEGIN** = `47` [🔗](class_control.md#class_Control_constant_NOTIFICATION_SCROLL_BEGIN)

Sent when this node is inside a [ScrollContainer](class_scrollcontainer.md#class_ScrollContainer) which has begun being scrolled when dragging the scrollable area *with a touch event*. This notification is *not* sent when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

 **Note:** This signal is only emitted on Android or iOS, or on desktop/web platforms when ProjectSettings.input_devices/pointing/emulate_touch_from_mouse is enabled.

<span id="class_Control_constant_NOTIFICATION_SCROLL_END"></span>

**NOTIFICATION_SCROLL_END** = `48` [🔗](class_control.md#class_Control_constant_NOTIFICATION_SCROLL_END)

Sent when this node is inside a [ScrollContainer](class_scrollcontainer.md#class_ScrollContainer) which has stopped being scrolled when dragging the scrollable area *with a touch event*. This notification is *not* sent when scrolling by dragging the scrollbar, scrolling with the mouse wheel or scrolling with keyboard/gamepad events.

 **Note:** This signal is only emitted on Android or iOS, or on desktop/web platforms when ProjectSettings.input_devices/pointing/emulate_touch_from_mouse is enabled.

<span id="class_Control_constant_NOTIFICATION_LAYOUT_DIRECTION_CHANGED"></span>

**NOTIFICATION_LAYOUT_DIRECTION_CHANGED** = `49` [🔗](class_control.md#class_Control_constant_NOTIFICATION_LAYOUT_DIRECTION_CHANGED)

Sent when the control layout direction is changed from LTR or RTL or vice versa. This notification is propagated to child Control nodes as result of a change to [layout_direction](class_control.md#class_Control_property_layout_direction).

---

### Property Descriptions

<span id="class_Control_property_accessibility_controls_nodes"></span>

[Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **accessibility_controls_nodes** = `[]` [🔗](class_control.md#class_Control_property_accessibility_controls_nodes)

- void **set_accessibility_controls_nodes** ( value: [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] )
- [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **get_accessibility_controls_nodes** ( )

The paths to the nodes which are controlled by this node.

---

<span id="class_Control_property_accessibility_described_by_nodes"></span>

[Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **accessibility_described_by_nodes** = `[]` [🔗](class_control.md#class_Control_property_accessibility_described_by_nodes)

- void **set_accessibility_described_by_nodes** ( value: [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] )
- [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **get_accessibility_described_by_nodes** ( )

The paths to the nodes which are describing this node.

---

<span id="class_Control_property_accessibility_description"></span>

[String](class_string.md#class_String) **accessibility_description** = `""` [🔗](class_control.md#class_Control_property_accessibility_description)

- void **set_accessibility_description** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_accessibility_description** ( )

The human-readable node description that is reported to assistive apps.

---

<span id="class_Control_property_accessibility_flow_to_nodes"></span>

[Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **accessibility_flow_to_nodes** = `[]` [🔗](class_control.md#class_Control_property_accessibility_flow_to_nodes)

- void **set_accessibility_flow_to_nodes** ( value: [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] )
- [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **get_accessibility_flow_to_nodes** ( )

The paths to the nodes which this node flows into.

---

<span id="class_Control_property_accessibility_labeled_by_nodes"></span>

[Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **accessibility_labeled_by_nodes** = `[]` [🔗](class_control.md#class_Control_property_accessibility_labeled_by_nodes)

- void **set_accessibility_labeled_by_nodes** ( value: [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] )
- [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **get_accessibility_labeled_by_nodes** ( )

The paths to the nodes which label this node.

---

<span id="class_Control_property_accessibility_live"></span>

[AccessibilityLiveMode](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode) **accessibility_live** = `0` [🔗](class_control.md#class_Control_property_accessibility_live)

- void **set_accessibility_live** ( value: [AccessibilityLiveMode](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode) )
- [AccessibilityLiveMode](class_displayserver.md#enum_DisplayServer_AccessibilityLiveMode) **get_accessibility_live** ( )

The mode with which a live region updates. A live region is a [Node](class_node.md#class_Node) that is updated as a result of an external event when the user's focus may be elsewhere.

---

<span id="class_Control_property_accessibility_name"></span>

[String](class_string.md#class_String) **accessibility_name** = `""` [🔗](class_control.md#class_Control_property_accessibility_name)

- void **set_accessibility_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_accessibility_name** ( )

The human-readable node name that is reported to assistive apps.

---

<span id="class_Control_property_anchor_bottom"></span>

[float](class_float.md#class_float) **anchor_bottom** = `0.0` [🔗](class_control.md#class_Control_property_anchor_bottom)

- [float](class_float.md#class_float) **get_anchor** ( side: Side ) *const*

Anchors the bottom edge of the node to the origin, the center, or the end of its parent control. It changes how the bottom offset updates when the node moves or changes size. You can use one of the [Anchor](class_control.md#enum_Control_Anchor) constants for convenience.

---

<span id="class_Control_property_anchor_left"></span>

[float](class_float.md#class_float) **anchor_left** = `0.0` [🔗](class_control.md#class_Control_property_anchor_left)

- [float](class_float.md#class_float) **get_anchor** ( side: Side ) *const*

Anchors the left edge of the node to the origin, the center or the end of its parent control. It changes how the left offset updates when the node moves or changes size. You can use one of the [Anchor](class_control.md#enum_Control_Anchor) constants for convenience.

---

<span id="class_Control_property_anchor_right"></span>

[float](class_float.md#class_float) **anchor_right** = `0.0` [🔗](class_control.md#class_Control_property_anchor_right)

- [float](class_float.md#class_float) **get_anchor** ( side: Side ) *const*

Anchors the right edge of the node to the origin, the center or the end of its parent control. It changes how the right offset updates when the node moves or changes size. You can use one of the [Anchor](class_control.md#enum_Control_Anchor) constants for convenience.

---

<span id="class_Control_property_anchor_top"></span>

[float](class_float.md#class_float) **anchor_top** = `0.0` [🔗](class_control.md#class_Control_property_anchor_top)

- [float](class_float.md#class_float) **get_anchor** ( side: Side ) *const*

Anchors the top edge of the node to the origin, the center or the end of its parent control. It changes how the top offset updates when the node moves or changes size. You can use one of the [Anchor](class_control.md#enum_Control_Anchor) constants for convenience.

---

<span id="class_Control_property_auto_translate"></span>

[bool](class_bool.md#class_bool) **auto_translate** [🔗](class_control.md#class_Control_property_auto_translate)

- void **set_auto_translate** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_auto_translating** ( )

**Deprecated:** Use [Node.auto_translate_mode](class_node.md#class_Node_property_auto_translate_mode) and [Node.can_auto_translate()](class_node.md#class_Node_method_can_auto_translate) instead.

Toggles if any text should automatically change to its translated version depending on the current locale.

---

<span id="class_Control_property_clip_contents"></span>

[bool](class_bool.md#class_bool) **clip_contents** = `false` [🔗](class_control.md#class_Control_property_clip_contents)

- void **set_clip_contents** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_clipping_contents** ( )

Enables whether rendering of [CanvasItem](class_canvasitem.md#class_CanvasItem) based children should be clipped to this control's rectangle. If `true`, parts of a child which would be visibly outside of this control's rectangle will not be rendered and won't receive input.

---

<span id="class_Control_property_custom_minimum_size"></span>

[Vector2](class_vector2.md#class_Vector2) **custom_minimum_size** = `Vector2(0, 0)` [🔗](class_control.md#class_Control_property_custom_minimum_size)

- void **set_custom_minimum_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_custom_minimum_size** ( )

The minimum size of the node's bounding rectangle. If you set it to a value greater than `(0, 0)`, the node's bounding rectangle will always have at least this size. Note that **Control** nodes have their internal minimum size returned by [get_minimum_size()](class_control.md#class_Control_method_get_minimum_size). It depends on the control's contents, like text, textures, or style boxes. The actual minimum size is the maximum value of this property and the internal minimum size (see [get_combined_minimum_size()](class_control.md#class_Control_method_get_combined_minimum_size)).

---

<span id="class_Control_property_focus_behavior_recursive"></span>

[FocusBehaviorRecursive](class_control.md#enum_Control_FocusBehaviorRecursive) **focus_behavior_recursive** = `0` [🔗](class_control.md#class_Control_property_focus_behavior_recursive)

- void **set_focus_behavior_recursive** ( value: [FocusBehaviorRecursive](class_control.md#enum_Control_FocusBehaviorRecursive) )
- [FocusBehaviorRecursive](class_control.md#enum_Control_FocusBehaviorRecursive) **get_focus_behavior_recursive** ( )

Determines which controls can be focused together with [focus_mode](class_control.md#class_Control_property_focus_mode). See [get_focus_mode_with_override()](class_control.md#class_Control_method_get_focus_mode_with_override). Since the default behavior is [FOCUS_BEHAVIOR_INHERITED](class_control.md#class_Control_constant_FOCUS_BEHAVIOR_INHERITED), this can be used to prevent all children controls from getting focused.

---

<span id="class_Control_property_focus_mode"></span>

[FocusMode](class_control.md#enum_Control_FocusMode) **focus_mode** = `0` [🔗](class_control.md#class_Control_property_focus_mode)

- void **set_focus_mode** ( value: [FocusMode](class_control.md#enum_Control_FocusMode) )
- [FocusMode](class_control.md#enum_Control_FocusMode) **get_focus_mode** ( )

Determines which controls can be focused. Only one control can be focused at a time, and the focused control will receive keyboard, gamepad, and mouse events in [_gui_input()](class_control.md#class_Control_private_method__gui_input). Use [get_focus_mode_with_override()](class_control.md#class_Control_method_get_focus_mode_with_override) to determine if a control can grab focus, since [focus_behavior_recursive](class_control.md#class_Control_property_focus_behavior_recursive) also affects it. See also [grab_focus()](class_control.md#class_Control_method_grab_focus).

---

<span id="class_Control_property_focus_neighbor_bottom"></span>

[NodePath](class_nodepath.md#class_NodePath) **focus_neighbor_bottom** = `NodePath("")` [🔗](class_control.md#class_Control_property_focus_neighbor_bottom)

- void **set_focus_neighbor** ( side: Side, neighbor: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_focus_neighbor** ( side: Side ) *const*

Tells Godot which node it should give focus to if the user presses the down arrow on the keyboard or down on a gamepad by default. You can change the key by editing the ProjectSettings.input/ui_down input action. The node must be a **Control**. If this property is not set, Godot will give focus to the closest **Control** to the bottom of this one.

---

<span id="class_Control_property_focus_neighbor_left"></span>

[NodePath](class_nodepath.md#class_NodePath) **focus_neighbor_left** = `NodePath("")` [🔗](class_control.md#class_Control_property_focus_neighbor_left)

- void **set_focus_neighbor** ( side: Side, neighbor: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_focus_neighbor** ( side: Side ) *const*

Tells Godot which node it should give focus to if the user presses the left arrow on the keyboard or left on a gamepad by default. You can change the key by editing the ProjectSettings.input/ui_left input action. The node must be a **Control**. If this property is not set, Godot will give focus to the closest **Control** to the left of this one.

---

<span id="class_Control_property_focus_neighbor_right"></span>

[NodePath](class_nodepath.md#class_NodePath) **focus_neighbor_right** = `NodePath("")` [🔗](class_control.md#class_Control_property_focus_neighbor_right)

- void **set_focus_neighbor** ( side: Side, neighbor: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_focus_neighbor** ( side: Side ) *const*

Tells Godot which node it should give focus to if the user presses the right arrow on the keyboard or right on a gamepad by default. You can change the key by editing the ProjectSettings.input/ui_right input action. The node must be a **Control**. If this property is not set, Godot will give focus to the closest **Control** to the right of this one.

---

<span id="class_Control_property_focus_neighbor_top"></span>

[NodePath](class_nodepath.md#class_NodePath) **focus_neighbor_top** = `NodePath("")` [🔗](class_control.md#class_Control_property_focus_neighbor_top)

- void **set_focus_neighbor** ( side: Side, neighbor: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_focus_neighbor** ( side: Side ) *const*

Tells Godot which node it should give focus to if the user presses the top arrow on the keyboard or top on a gamepad by default. You can change the key by editing the ProjectSettings.input/ui_up input action. The node must be a **Control**. If this property is not set, Godot will give focus to the closest **Control** to the top of this one.

---

<span id="class_Control_property_focus_next"></span>

[NodePath](class_nodepath.md#class_NodePath) **focus_next** = `NodePath("")` [🔗](class_control.md#class_Control_property_focus_next)

- void **set_focus_next** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_focus_next** ( )

Tells Godot which node it should give focus to if the user presses :kbd:`Tab` on a keyboard by default. You can change the key by editing the ProjectSettings.input/ui_focus_next input action.

If this property is not set, Godot will select a "best guess" based on surrounding nodes in the scene tree.

---

<span id="class_Control_property_focus_previous"></span>

[NodePath](class_nodepath.md#class_NodePath) **focus_previous** = `NodePath("")` [🔗](class_control.md#class_Control_property_focus_previous)

- void **set_focus_previous** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_focus_previous** ( )

Tells Godot which node it should give focus to if the user presses :kbd:`Shift + Tab` on a keyboard by default. You can change the key by editing the ProjectSettings.input/ui_focus_prev input action.

If this property is not set, Godot will select a "best guess" based on surrounding nodes in the scene tree.

---

<span id="class_Control_property_global_position"></span>

[Vector2](class_vector2.md#class_Vector2) **global_position** [🔗](class_control.md#class_Control_property_global_position)

- [Vector2](class_vector2.md#class_Vector2) **get_global_position** ( )

The node's global position, relative to the world (usually to the [CanvasLayer](class_canvaslayer.md#class_CanvasLayer)).

---

<span id="class_Control_property_grow_horizontal"></span>

[GrowDirection](class_control.md#enum_Control_GrowDirection) **grow_horizontal** = `1` [🔗](class_control.md#class_Control_property_grow_horizontal)

- void **set_h_grow_direction** ( value: [GrowDirection](class_control.md#enum_Control_GrowDirection) )
- [GrowDirection](class_control.md#enum_Control_GrowDirection) **get_h_grow_direction** ( )

Controls the direction on the horizontal axis in which the control should grow if its horizontal minimum size is changed to be greater than its current size, as the control always has to be at least the minimum size.

---

<span id="class_Control_property_grow_vertical"></span>

[GrowDirection](class_control.md#enum_Control_GrowDirection) **grow_vertical** = `1` [🔗](class_control.md#class_Control_property_grow_vertical)

- void **set_v_grow_direction** ( value: [GrowDirection](class_control.md#enum_Control_GrowDirection) )
- [GrowDirection](class_control.md#enum_Control_GrowDirection) **get_v_grow_direction** ( )

Controls the direction on the vertical axis in which the control should grow if its vertical minimum size is changed to be greater than its current size, as the control always has to be at least the minimum size.

---

<span id="class_Control_property_layout_direction"></span>

[LayoutDirection](class_control.md#enum_Control_LayoutDirection) **layout_direction** = `0` [🔗](class_control.md#class_Control_property_layout_direction)

- void **set_layout_direction** ( value: [LayoutDirection](class_control.md#enum_Control_LayoutDirection) )
- [LayoutDirection](class_control.md#enum_Control_LayoutDirection) **get_layout_direction** ( )

Controls layout direction and text writing direction. Right-to-left layouts are necessary for certain languages (e.g. Arabic and Hebrew). See also [is_layout_rtl()](class_control.md#class_Control_method_is_layout_rtl).

---

<span id="class_Control_property_localize_numeral_system"></span>

[bool](class_bool.md#class_bool) **localize_numeral_system** = `true` [🔗](class_control.md#class_Control_property_localize_numeral_system)

- void **set_localize_numeral_system** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_localizing_numeral_system** ( )

If `true`, automatically converts code line numbers, list indices, [SpinBox](class_spinbox.md#class_SpinBox) and [ProgressBar](class_progressbar.md#class_ProgressBar) values from the Western Arabic (0..9) to the numeral systems used in current locale.

 **Note:** Numbers within the text are not automatically converted, it can be done manually, using [TextServer.format_number()](class_textserver.md#class_TextServer_method_format_number).

---

<span id="class_Control_property_mouse_behavior_recursive"></span>

[MouseBehaviorRecursive](class_control.md#enum_Control_MouseBehaviorRecursive) **mouse_behavior_recursive** = `0` [🔗](class_control.md#class_Control_property_mouse_behavior_recursive)

- void **set_mouse_behavior_recursive** ( value: [MouseBehaviorRecursive](class_control.md#enum_Control_MouseBehaviorRecursive) )
- [MouseBehaviorRecursive](class_control.md#enum_Control_MouseBehaviorRecursive) **get_mouse_behavior_recursive** ( )

Determines which controls can receive mouse input together with [mouse_filter](class_control.md#class_Control_property_mouse_filter). See [get_mouse_filter_with_override()](class_control.md#class_Control_method_get_mouse_filter_with_override). Since the default behavior is [MOUSE_BEHAVIOR_INHERITED](class_control.md#class_Control_constant_MOUSE_BEHAVIOR_INHERITED), this can be used to prevent all children controls from receiving mouse input.

---

<span id="class_Control_property_mouse_default_cursor_shape"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **mouse_default_cursor_shape** = `0` [🔗](class_control.md#class_Control_property_mouse_default_cursor_shape)

- void **set_default_cursor_shape** ( value: [CursorShape](class_control.md#enum_Control_CursorShape) )
- [CursorShape](class_control.md#enum_Control_CursorShape) **get_default_cursor_shape** ( )

The default cursor shape for this control. Useful for Godot plugins and applications or games that use the system's mouse cursors.

 **Note:** On Linux, shapes may vary depending on the cursor theme of the system.

---

<span id="class_Control_property_mouse_filter"></span>

[MouseFilter](class_control.md#enum_Control_MouseFilter) **mouse_filter** = `0` [🔗](class_control.md#class_Control_property_mouse_filter)

- void **set_mouse_filter** ( value: [MouseFilter](class_control.md#enum_Control_MouseFilter) )
- [MouseFilter](class_control.md#enum_Control_MouseFilter) **get_mouse_filter** ( )

Determines which controls will be able to receive mouse button input events through [_gui_input()](class_control.md#class_Control_private_method__gui_input) and the [mouse_entered](class_control.md#class_Control_signal_mouse_entered), and [mouse_exited](class_control.md#class_Control_signal_mouse_exited) signals. Also determines how these events should be propagated. See the constants to learn what each does. Use [get_mouse_filter_with_override()](class_control.md#class_Control_method_get_mouse_filter_with_override) to determine if a control can receive mouse input, since [mouse_behavior_recursive](class_control.md#class_Control_property_mouse_behavior_recursive) also affects it.

---

<span id="class_Control_property_mouse_force_pass_scroll_events"></span>

[bool](class_bool.md#class_bool) **mouse_force_pass_scroll_events** = `true` [🔗](class_control.md#class_Control_property_mouse_force_pass_scroll_events)

- void **set_force_pass_scroll_events** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_force_pass_scroll_events** ( )

When enabled, scroll wheel events processed by [_gui_input()](class_control.md#class_Control_private_method__gui_input) will be passed to the parent control even if [mouse_filter](class_control.md#class_Control_property_mouse_filter) is set to [MOUSE_FILTER_STOP](class_control.md#class_Control_constant_MOUSE_FILTER_STOP).

You should disable it on the root of your UI if you do not want scroll events to go to the [Node._unhandled_input()](class_node.md#class_Node_private_method__unhandled_input) processing.

 **Note:** Because this property defaults to `true`, this allows nested scrollable containers to work out of the box.

---

<span id="class_Control_property_offset_bottom"></span>

[float](class_float.md#class_float) **offset_bottom** = `0.0` [🔗](class_control.md#class_Control_property_offset_bottom)

- void **set_offset** ( side: Side, offset: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_offset** ( offset: Side ) *const*

Distance between the node's bottom edge and its parent control, based on [anchor_bottom](class_control.md#class_Control_property_anchor_bottom).

Offsets are often controlled by one or multiple parent [Container](class_container.md#class_Container) nodes, so you should not modify them manually if your node is a direct child of a [Container](class_container.md#class_Container). Offsets update automatically when you move or resize the node.

---

<span id="class_Control_property_offset_left"></span>

[float](class_float.md#class_float) **offset_left** = `0.0` [🔗](class_control.md#class_Control_property_offset_left)

- void **set_offset** ( side: Side, offset: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_offset** ( offset: Side ) *const*

Distance between the node's left edge and its parent control, based on [anchor_left](class_control.md#class_Control_property_anchor_left).

Offsets are often controlled by one or multiple parent [Container](class_container.md#class_Container) nodes, so you should not modify them manually if your node is a direct child of a [Container](class_container.md#class_Container). Offsets update automatically when you move or resize the node.

---

<span id="class_Control_property_offset_right"></span>

[float](class_float.md#class_float) **offset_right** = `0.0` [🔗](class_control.md#class_Control_property_offset_right)

- void **set_offset** ( side: Side, offset: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_offset** ( offset: Side ) *const*

Distance between the node's right edge and its parent control, based on [anchor_right](class_control.md#class_Control_property_anchor_right).

Offsets are often controlled by one or multiple parent [Container](class_container.md#class_Container) nodes, so you should not modify them manually if your node is a direct child of a [Container](class_container.md#class_Container). Offsets update automatically when you move or resize the node.

---

<span id="class_Control_property_offset_top"></span>

[float](class_float.md#class_float) **offset_top** = `0.0` [🔗](class_control.md#class_Control_property_offset_top)

- void **set_offset** ( side: Side, offset: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_offset** ( offset: Side ) *const*

Distance between the node's top edge and its parent control, based on [anchor_top](class_control.md#class_Control_property_anchor_top).

Offsets are often controlled by one or multiple parent [Container](class_container.md#class_Container) nodes, so you should not modify them manually if your node is a direct child of a [Container](class_container.md#class_Container). Offsets update automatically when you move or resize the node.

---

<span id="class_Control_property_pivot_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **pivot_offset** = `Vector2(0, 0)` [🔗](class_control.md#class_Control_property_pivot_offset)

- void **set_pivot_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_pivot_offset** ( )

By default, the node's pivot is its top-left corner. When you change its [rotation](class_control.md#class_Control_property_rotation) or [scale](class_control.md#class_Control_property_scale), it will rotate or scale around this pivot.

The actual offset is the combined value of this property and [pivot_offset_ratio](class_control.md#class_Control_property_pivot_offset_ratio).

---

<span id="class_Control_property_pivot_offset_ratio"></span>

[Vector2](class_vector2.md#class_Vector2) **pivot_offset_ratio** = `Vector2(0, 0)` [🔗](class_control.md#class_Control_property_pivot_offset_ratio)

- void **set_pivot_offset_ratio** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_pivot_offset_ratio** ( )

Same as [pivot_offset](class_control.md#class_Control_property_pivot_offset), but expressed as uniform vector, where `Vector2(0, 0)` is the top-left corner of this control, and `Vector2(1, 1)` is its bottom-right corner. Set this property to `Vector2(0.5, 0.5)` to pivot around this control's center.

The actual offset is the combined value of this property and [pivot_offset](class_control.md#class_Control_property_pivot_offset).

---

<span id="class_Control_property_position"></span>

[Vector2](class_vector2.md#class_Vector2) **position** = `Vector2(0, 0)` [🔗](class_control.md#class_Control_property_position)

- [Vector2](class_vector2.md#class_Vector2) **get_position** ( )

The node's position, relative to its containing node. It corresponds to the rectangle's top-left corner. The property is not affected by [pivot_offset](class_control.md#class_Control_property_pivot_offset).

---

<span id="class_Control_property_rotation"></span>

[float](class_float.md#class_float) **rotation** = `0.0` [🔗](class_control.md#class_Control_property_rotation)

- void **set_rotation** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_rotation** ( )

The node's rotation around its pivot, in radians. See [pivot_offset](class_control.md#class_Control_property_pivot_offset) to change the pivot's position.

 **Note:** This property is edited in the inspector in degrees. If you want to use degrees in a script, use [rotation_degrees](class_control.md#class_Control_property_rotation_degrees).

---

<span id="class_Control_property_rotation_degrees"></span>

[float](class_float.md#class_float) **rotation_degrees** [🔗](class_control.md#class_Control_property_rotation_degrees)

- void **set_rotation_degrees** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_rotation_degrees** ( )

Helper property to access [rotation](class_control.md#class_Control_property_rotation) in degrees instead of radians.

---

<span id="class_Control_property_scale"></span>

[Vector2](class_vector2.md#class_Vector2) **scale** = `Vector2(1, 1)` [🔗](class_control.md#class_Control_property_scale)

- void **set_scale** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_scale** ( )

The node's scale, relative to its [size](class_control.md#class_Control_property_size). Change this property to scale the node around its [pivot_offset](class_control.md#class_Control_property_pivot_offset). The Control's tooltip will also scale according to this value.

 **Note:** This property is mainly intended to be used for animation purposes. To support multiple resolutions in your project, use an appropriate viewport stretch mode as described in the [documentation](../tutorials/rendering/multiple_resolutions.md) instead of scaling Controls individually.

 **Note:** [FontFile.oversampling](class_fontfile.md#class_FontFile_property_oversampling) does *not* take **Control** [scale](class_control.md#class_Control_property_scale) into account. This means that scaling up/down will cause bitmap fonts and rasterized (non-MSDF) dynamic fonts to appear blurry or pixelated. To ensure text remains crisp regardless of scale, you can enable MSDF font rendering by enabling ProjectSettings.gui/theme/default_font_multichannel_signed_distance_field (applies to the default project font only), or enabling **Multichannel Signed Distance Field** in the import options of a DynamicFont for custom fonts. On system fonts, [SystemFont.multichannel_signed_distance_field](class_systemfont.md#class_SystemFont_property_multichannel_signed_distance_field) can be enabled in the inspector.

 **Note:** If the Control node is a child of a [Container](class_container.md#class_Container) node, the scale will be reset to `Vector2(1, 1)` when the scene is instantiated. To set the Control's scale when it's instantiated, wait for one frame using `await get_tree().process_frame` then set its [scale](class_control.md#class_Control_property_scale) property.

---

<span id="class_Control_property_shortcut_context"></span>

[Node](class_node.md#class_Node) **shortcut_context** [🔗](class_control.md#class_Control_property_shortcut_context)

- void **set_shortcut_context** ( value: [Node](class_node.md#class_Node) )
- [Node](class_node.md#class_Node) **get_shortcut_context** ( )

The [Node](class_node.md#class_Node) which must be a parent of the focused **Control** for the shortcut to be activated. If `null`, the shortcut can be activated when any control is focused (a global shortcut). This allows shortcuts to be accepted only when the user has a certain area of the GUI focused.

---

<span id="class_Control_property_size"></span>

[Vector2](class_vector2.md#class_Vector2) **size** = `Vector2(0, 0)` [🔗](class_control.md#class_Control_property_size)

- [Vector2](class_vector2.md#class_Vector2) **get_size** ( )

The size of the node's bounding rectangle, in the node's coordinate system. [Container](class_container.md#class_Container) nodes update this property automatically.

---

<span id="class_Control_property_size_flags_horizontal"></span>

*BitField*\[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] **size_flags_horizontal** = `1` [🔗](class_control.md#class_Control_property_size_flags_horizontal)

- void **set_h_size_flags** ( value: *BitField*\[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] )
- *BitField*\[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] **get_h_size_flags** ( )

Tells the parent [Container](class_container.md#class_Container) nodes how they should resize and place the node on the X axis. Use a combination of the [SizeFlags](class_control.md#enum_Control_SizeFlags) constants to change the flags. See the constants to learn what each does.

---

<span id="class_Control_property_size_flags_stretch_ratio"></span>

[float](class_float.md#class_float) **size_flags_stretch_ratio** = `1.0` [🔗](class_control.md#class_Control_property_size_flags_stretch_ratio)

- void **set_stretch_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_stretch_ratio** ( )

If the node and at least one of its neighbors uses the [SIZE_EXPAND](class_control.md#class_Control_constant_SIZE_EXPAND) size flag, the parent [Container](class_container.md#class_Container) will let it take more or less space depending on this property. If this node has a stretch ratio of 2 and its neighbor a ratio of 1, this node will take two thirds of the available space.

---

<span id="class_Control_property_size_flags_vertical"></span>

*BitField*\[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] **size_flags_vertical** = `1` [🔗](class_control.md#class_Control_property_size_flags_vertical)

- void **set_v_size_flags** ( value: *BitField*\[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] )
- *BitField*\[[SizeFlags](class_control.md#enum_Control_SizeFlags)\] **get_v_size_flags** ( )

Tells the parent [Container](class_container.md#class_Container) nodes how they should resize and place the node on the Y axis. Use a combination of the [SizeFlags](class_control.md#enum_Control_SizeFlags) constants to change the flags. See the constants to learn what each does.

---

<span id="class_Control_property_theme"></span>

[Theme](class_theme.md#class_Theme) **theme** [🔗](class_control.md#class_Control_property_theme)

- void **set_theme** ( value: [Theme](class_theme.md#class_Theme) )
- [Theme](class_theme.md#class_Theme) **get_theme** ( )

The [Theme](class_theme.md#class_Theme) resource this node and all its **Control** and [Window](class_window.md#class_Window) children use. If a child node has its own [Theme](class_theme.md#class_Theme) resource set, theme items are merged with child's definitions having higher priority.

 **Note:** [Window](class_window.md#class_Window) styles will have no effect unless the window is embedded.

---

<span id="class_Control_property_theme_type_variation"></span>

[StringName](class_stringname.md#class_StringName) **theme_type_variation** = `&""` [🔗](class_control.md#class_Control_property_theme_type_variation)

- void **set_theme_type_variation** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_theme_type_variation** ( )

The name of a theme type variation used by this **Control** to look up its own theme items. When empty, the class name of the node is used (e.g. `Button` for the [Button](class_button.md#class_Button) control), as well as the class names of all parent classes (in order of inheritance).

When set, this property gives the highest priority to the type of the specified name. This type can in turn extend another type, forming a dependency chain. See [Theme.set_type_variation()](class_theme.md#class_Theme_method_set_type_variation). If the theme item cannot be found using this type or its base types, lookup falls back on the class names.

 **Note:** To look up **Control**'s own items use various `get_theme_*` methods without specifying `theme_type`.

 **Note:** Theme items are looked for in the tree order, from branch to root, where each **Control** node is checked for its [theme](class_control.md#class_Control_property_theme) property. The earliest match against any type/class name is returned. The project-level Theme and the default Theme are checked last.

---

<span id="class_Control_property_tooltip_auto_translate_mode"></span>

[AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) **tooltip_auto_translate_mode** = `0` [🔗](class_control.md#class_Control_property_tooltip_auto_translate_mode)

- void **set_tooltip_auto_translate_mode** ( value: [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) )
- [AutoTranslateMode](class_node.md#enum_Node_AutoTranslateMode) **get_tooltip_auto_translate_mode** ( )

Defines if tooltip text should automatically change to its translated version depending on the current locale. Uses the same auto translate mode as this control when set to [Node.AUTO_TRANSLATE_MODE_INHERIT](class_node.md#class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT).

 **Note:** Tooltips customized using [_make_custom_tooltip()](class_control.md#class_Control_private_method__make_custom_tooltip) do not use this auto translate mode automatically.

---

<span id="class_Control_property_tooltip_text"></span>

[String](class_string.md#class_String) **tooltip_text** = `""` [🔗](class_control.md#class_Control_property_tooltip_text)

- void **set_tooltip_text** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_tooltip_text** ( )

The default tooltip text. The tooltip appears when the user's mouse cursor stays idle over this control for a few moments, provided that the [mouse_filter](class_control.md#class_Control_property_mouse_filter) property is not [MOUSE_FILTER_IGNORE](class_control.md#class_Control_constant_MOUSE_FILTER_IGNORE). The time required for the tooltip to appear can be changed with the ProjectSettings.gui/timers/tooltip_delay_sec setting.

This string is the default return value of [get_tooltip()](class_control.md#class_Control_method_get_tooltip). Override [_get_tooltip()](class_control.md#class_Control_private_method__get_tooltip) to generate tooltip text dynamically. Override [_make_custom_tooltip()](class_control.md#class_Control_private_method__make_custom_tooltip) to customize the tooltip interface and behavior.

The tooltip popup will use either a default implementation, or a custom one that you can provide by overriding [_make_custom_tooltip()](class_control.md#class_Control_private_method__make_custom_tooltip). The default tooltip includes a [PopupPanel](class_popuppanel.md#class_PopupPanel) and [Label](class_label.md#class_Label) whose theme properties can be customized using [Theme](class_theme.md#class_Theme) methods with the `"TooltipPanel"` and `"TooltipLabel"` respectively. For example:

.. tabs::

```
```

    var style_box = StyleBoxFlat.new()
    style_box.set_bg_color(Color(1, 1, 0))
    style_box.set_border_width_all(2)
    # We assume here that the `theme` property has been assigned a custom Theme beforehand.
    theme.set_stylebox("panel", "TooltipPanel", style_box)
    theme.set_color("font_color", "TooltipLabel", Color(0, 1, 1))

```
```

    var styleBox = new StyleBoxFlat();
    styleBox.SetBgColor(new Color(1, 1, 0));
    styleBox.SetBorderWidthAll(2);
    // We assume here that the `Theme` property has been assigned a custom Theme beforehand.
    Theme.SetStyleBox("panel", "TooltipPanel", styleBox);
    Theme.SetColor("font_color", "TooltipLabel", new Color(0, 1, 1));

---

### Method Descriptions

<span id="class_Control_private_method__accessibility_get_contextual_info"></span>

[String](class_string.md#class_String) **_accessibility_get_contextual_info** ( ) *virtual* *const* [🔗](class_control.md#class_Control_private_method__accessibility_get_contextual_info)

Return the description of the keyboard shortcuts and other contextual help for this control.

---

<span id="class_Control_private_method__can_drop_data"></span>

[bool](class_bool.md#class_bool) **_can_drop_data** ( at_position: [Vector2](class_vector2.md#class_Vector2), data: [Variant](class_variant.md#class_Variant) ) *virtual* *const* [🔗](class_control.md#class_Control_private_method__can_drop_data)

Godot calls this method to test if `data` from a control's [_get_drag_data()](class_control.md#class_Control_private_method__get_drag_data) can be dropped at `at_position`. `at_position` is local to this control.

This method should only be used to test the data. Process the data in [_drop_data()](class_control.md#class_Control_private_method__drop_data).

 **Note:** If the drag was initiated by a keyboard shortcut or [accessibility_drag()](class_control.md#class_Control_method_accessibility_drag), `at_position` is set to [Vector2.INF](class_vector2.md#class_Vector2_constant_INF), and the currently selected item/text position should be used as the drop position.

.. tabs::

```
```

    func _can_drop_data(position, data):
        # Check position if it is relevant to you
        # Otherwise, just check data
        return typeof(data) == TYPE_DICTIONARY and data.has("expected")

```
```

    public override bool _CanDropData(Vector2 atPosition, Variant data)
    {
        // Check position if it is relevant to you
        // Otherwise, just check data
        return data.VariantType == Variant.Type.Dictionary && data.AsGodotDictionary().ContainsKey("expected");
    }

---

<span id="class_Control_private_method__drop_data"></span>

void **_drop_data** ( at_position: [Vector2](class_vector2.md#class_Vector2), data: [Variant](class_variant.md#class_Variant) ) *virtual* [🔗](class_control.md#class_Control_private_method__drop_data)

Godot calls this method to pass you the `data` from a control's [_get_drag_data()](class_control.md#class_Control_private_method__get_drag_data) result. Godot first calls [_can_drop_data()](class_control.md#class_Control_private_method__can_drop_data) to test if `data` is allowed to drop at `at_position` where `at_position` is local to this control.

 **Note:** If the drag was initiated by a keyboard shortcut or [accessibility_drag()](class_control.md#class_Control_method_accessibility_drag), `at_position` is set to [Vector2.INF](class_vector2.md#class_Vector2_constant_INF), and the currently selected item/text position should be used as the drop position.

.. tabs::

```
```

    func _can_drop_data(position, data):
        return typeof(data) == TYPE_DICTIONARY and data.has("color")

    func _drop_data(position, data):
        var color = data["color"]

```
```

    public override bool _CanDropData(Vector2 atPosition, Variant data)
    {
        return data.VariantType == Variant.Type.Dictionary && data.AsGodotDictionary().ContainsKey("color");
    }

    public override void _DropData(Vector2 atPosition, Variant data)
    {
        Color color = data.AsGodotDictionary()["color"].AsColor();
    }

---

<span id="class_Control_private_method__get_accessibility_container_name"></span>

[String](class_string.md#class_String) **_get_accessibility_container_name** ( node: [Node](class_node.md#class_Node) ) *virtual* *const* [🔗](class_control.md#class_Control_private_method__get_accessibility_container_name)

Override this method to return a human-readable description of the position of the child `node` in the custom container, added to the [accessibility_name](class_control.md#class_Control_property_accessibility_name).

---

<span id="class_Control_private_method__get_drag_data"></span>

[Variant](class_variant.md#class_Variant) **_get_drag_data** ( at_position: [Vector2](class_vector2.md#class_Vector2) ) *virtual* [🔗](class_control.md#class_Control_private_method__get_drag_data)

Godot calls this method to get data that can be dragged and dropped onto controls that expect drop data. Returns `null` if there is no data to drag. Controls that want to receive drop data should implement [_can_drop_data()](class_control.md#class_Control_private_method__can_drop_data) and [_drop_data()](class_control.md#class_Control_private_method__drop_data). `at_position` is local to this control. Drag may be forced with [force_drag()](class_control.md#class_Control_method_force_drag).

A preview that will follow the mouse that should represent the data can be set with [set_drag_preview()](class_control.md#class_Control_method_set_drag_preview). A good time to set the preview is in this method.

 **Note:** If the drag was initiated by a keyboard shortcut or [accessibility_drag()](class_control.md#class_Control_method_accessibility_drag), `at_position` is set to [Vector2.INF](class_vector2.md#class_Vector2_constant_INF), and the currently selected item/text position should be used as the drag position.

.. tabs::

```
```

    func _get_drag_data(position):
        var mydata = make_data() # This is your custom method generating the drag data.
        set_drag_preview(make_preview(mydata)) # This is your custom method generating the preview of the drag data.
        return mydata

```
```

    public override Variant _GetDragData(Vector2 atPosition)
    {
        var myData = MakeData(); // This is your custom method generating the drag data.
        SetDragPreview(MakePreview(myData)); // This is your custom method generating the preview of the drag data.
        return myData;
    }

---

<span id="class_Control_private_method__get_minimum_size"></span>

[Vector2](class_vector2.md#class_Vector2) **_get_minimum_size** ( ) *virtual* *const* [🔗](class_control.md#class_Control_private_method__get_minimum_size)

Virtual method to be implemented by the user. Returns the minimum size for this control. Alternative to [custom_minimum_size](class_control.md#class_Control_property_custom_minimum_size) for controlling minimum size via code. The actual minimum size will be the max value of these two (in each axis separately).

If not overridden, defaults to [Vector2.ZERO](class_vector2.md#class_Vector2_constant_ZERO).

 **Note:** This method will not be called when the script is attached to a **Control** node that already overrides its minimum size (e.g. [Label](class_label.md#class_Label), [Button](class_button.md#class_Button), [PanelContainer](class_panelcontainer.md#class_PanelContainer) etc.). It can only be used with most basic GUI nodes, like **Control**, [Container](class_container.md#class_Container), [Panel](class_panel.md#class_Panel) etc.

---

<span id="class_Control_private_method__get_tooltip"></span>

[String](class_string.md#class_String) **_get_tooltip** ( at_position: [Vector2](class_vector2.md#class_Vector2) ) *virtual* *const* [🔗](class_control.md#class_Control_private_method__get_tooltip)

Virtual method to be implemented by the user. Returns the tooltip text for the position `at_position` in control's local coordinates, which will typically appear when the cursor is resting over this control. See [get_tooltip()](class_control.md#class_Control_method_get_tooltip).

 **Note:** If this method returns an empty [String](class_string.md#class_String) and [_make_custom_tooltip()](class_control.md#class_Control_private_method__make_custom_tooltip) is not overridden, no tooltip is displayed.

---

<span id="class_Control_private_method__gui_input"></span>

void **_gui_input** ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) *virtual* [🔗](class_control.md#class_Control_private_method__gui_input)

Virtual method to be implemented by the user. Override this method to handle and accept inputs on UI elements. See also [accept_event()](class_control.md#class_Control_method_accept_event).

 **Example:** Click on the control to print a message:

.. tabs::

```
```

    func _gui_input(event):
        if event is InputEventMouseButton:
            if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
                print("I've been clicked D:")

```
```

    public override void _GuiInput(InputEvent @event)
    {
        if (@event is InputEventMouseButton mb)
        {
            if (mb.ButtonIndex == MouseButton.Left && mb.Pressed)
            {
                GD.Print("I've been clicked D:");
            }
        }
    }

If the `event` inherits [InputEventMouse](class_inputeventmouse.md#class_InputEventMouse), this method will **not** be called when:

- the control's [mouse_filter](class_control.md#class_Control_property_mouse_filter) is set to [MOUSE_FILTER_IGNORE](class_control.md#class_Control_constant_MOUSE_FILTER_IGNORE);

- the control is obstructed by another control on top, that doesn't have [mouse_filter](class_control.md#class_Control_property_mouse_filter) set to [MOUSE_FILTER_IGNORE](class_control.md#class_Control_constant_MOUSE_FILTER_IGNORE);

- the control's parent has [mouse_filter](class_control.md#class_Control_property_mouse_filter) set to [MOUSE_FILTER_STOP](class_control.md#class_Control_constant_MOUSE_FILTER_STOP) or has accepted the event;

- the control's parent has [clip_contents](class_control.md#class_Control_property_clip_contents) enabled and the `event`'s position is outside the parent's rectangle;

- the `event`'s position is outside the control (see [_has_point()](class_control.md#class_Control_private_method__has_point)).

 **Note:** The `event`'s position is relative to this control's origin.

---

<span id="class_Control_private_method__has_point"></span>

[bool](class_bool.md#class_bool) **_has_point** ( point: [Vector2](class_vector2.md#class_Vector2) ) *virtual* *const* [🔗](class_control.md#class_Control_private_method__has_point)

Virtual method to be implemented by the user. Returns whether the given `point` is inside this control.

If not overridden, default behavior is checking if the point is within control's Rect.

 **Note:** If you want to check if a point is inside the control, you can use `Rect2(Vector2.ZERO, size).has_point(point)`.

---

<span id="class_Control_private_method__make_custom_tooltip"></span>

[Object](class_object.md#class_Object) **_make_custom_tooltip** ( for_text: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_control.md#class_Control_private_method__make_custom_tooltip)

Virtual method to be implemented by the user. Returns a **Control** node that should be used as a tooltip instead of the default one. `for_text` is the return value of [get_tooltip()](class_control.md#class_Control_method_get_tooltip).

The returned node must be of type **Control** or Control-derived. It can have child nodes of any type. It is freed when the tooltip disappears, so make sure you always provide a new instance (if you want to use a pre-existing node from your scene tree, you can duplicate it and pass the duplicated instance). When `null` or a non-Control node is returned, the default tooltip will be used instead.

The returned node will be added as child to a [PopupPanel](class_popuppanel.md#class_PopupPanel), so you should only provide the contents of that panel. That [PopupPanel](class_popuppanel.md#class_PopupPanel) can be themed using [Theme.set_stylebox()](class_theme.md#class_Theme_method_set_stylebox) for the type `"TooltipPanel"` (see [tooltip_text](class_control.md#class_Control_property_tooltip_text) for an example).

 **Note:** The tooltip is shrunk to minimal size. If you want to ensure it's fully visible, you might want to set its [custom_minimum_size](class_control.md#class_Control_property_custom_minimum_size) to some non-zero value.

 **Note:** The node (and any relevant children) should have their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) set to `true` when returned, otherwise, the viewport that instantiates it will not be able to calculate its minimum size reliably.

 **Note:** If overridden, this method is called even if [get_tooltip()](class_control.md#class_Control_method_get_tooltip) returns an empty string. When this happens with the default tooltip, it is not displayed. To copy this behavior, return `null` in this method when `for_text` is empty.

 **Example:** Use a constructed node as a tooltip:

.. tabs::

```
```

    func _make_custom_tooltip(for_text):
        var label = Label.new()
        label.text = for_text
        return label

```
```

    public override Control _MakeCustomTooltip(string forText)
    {
        var label = new Label();
        label.Text = forText;
        return label;
    }

 **Example:** Use a scene instance as a tooltip:

.. tabs::

```
```

    func _make_custom_tooltip(for_text):
        var tooltip = preload("res://some_tooltip_scene.tscn").instantiate()
        tooltip.get_node("Label").text = for_text
        return tooltip

```
```

    public override Control _MakeCustomTooltip(string forText)
    {
        Node tooltip = ResourceLoader.Load<PackedScene>("res://some_tooltip_scene.tscn").Instantiate();
        tooltip.GetNode<Label>("Label").Text = forText;
        return tooltip;
    }

---

<span id="class_Control_private_method__structured_text_parser"></span>

[Array](class_array.md#class_Array)\[[Vector3i](class_vector3i.md#class_Vector3i)\] **_structured_text_parser** ( args: [Array](class_array.md#class_Array), text: [String](class_string.md#class_String) ) *virtual* *const* [🔗](class_control.md#class_Control_private_method__structured_text_parser)

User defined BiDi algorithm override function.

Returns an [Array](class_array.md#class_Array) of [Vector3i](class_vector3i.md#class_Vector3i) text ranges and text base directions, in the left-to-right order. Ranges should cover full source `text` without overlaps. BiDi algorithm will be used on each range separately.

---

<span id="class_Control_method_accept_event"></span>

void **accept_event** ( ) [🔗](class_control.md#class_Control_method_accept_event)

Marks an input event as handled. Once you accept an input event, it stops propagating, even to nodes listening to [Node._unhandled_input()](class_node.md#class_Node_private_method__unhandled_input) or [Node._unhandled_key_input()](class_node.md#class_Node_private_method__unhandled_key_input).

 **Note:** This does not affect the methods in [Input](class_input.md#class_Input), only the way events are propagated.

---

<span id="class_Control_method_accessibility_drag"></span>

void **accessibility_drag** ( ) [🔗](class_control.md#class_Control_method_accessibility_drag)

Starts drag-and-drop operation without using a mouse.

---

<span id="class_Control_method_accessibility_drop"></span>

void **accessibility_drop** ( ) [🔗](class_control.md#class_Control_method_accessibility_drop)

Ends drag-and-drop operation without using a mouse.

---

<span id="class_Control_method_add_theme_color_override"></span>

void **add_theme_color_override** ( name: [StringName](class_stringname.md#class_StringName), color: [Color](class_color.md#class_Color) ) [🔗](class_control.md#class_Control_method_add_theme_color_override)

Creates a local override for a theme [Color](class_color.md#class_Color) with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_color_override()](class_control.md#class_Control_method_remove_theme_color_override).

See also [get_theme_color()](class_control.md#class_Control_method_get_theme_color).

 **Example:** Override a [Label](class_label.md#class_Label)'s color and reset it later:

.. tabs::

```
```

    # Given the child Label node "MyLabel", override its font color with a custom value.
    $MyLabel.add_theme_color_override("font_color", Color(1, 0.5, 0))
    # Reset the font color of the child label.
    $MyLabel.remove_theme_color_override("font_color")
    # Alternatively it can be overridden with the default value from the Label type.
    $MyLabel.add_theme_color_override("font_color", get_theme_color("font_color", "Label"))

```
```

    // Given the child Label node "MyLabel", override its font color with a custom value.
    GetNode<Label>("MyLabel").AddThemeColorOverride("font_color", new Color(1, 0.5f, 0));
    // Reset the font color of the child label.
    GetNode<Label>("MyLabel").RemoveThemeColorOverride("font_color");
    // Alternatively it can be overridden with the default value from the Label type.
    GetNode<Label>("MyLabel").AddThemeColorOverride("font_color", GetThemeColor("font_color", "Label"));

---

<span id="class_Control_method_add_theme_constant_override"></span>

void **add_theme_constant_override** ( name: [StringName](class_stringname.md#class_StringName), constant: [int](class_int.md#class_int) ) [🔗](class_control.md#class_Control_method_add_theme_constant_override)

Creates a local override for a theme constant with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_constant_override()](class_control.md#class_Control_method_remove_theme_constant_override).

See also [get_theme_constant()](class_control.md#class_Control_method_get_theme_constant).

---

<span id="class_Control_method_add_theme_font_override"></span>

void **add_theme_font_override** ( name: [StringName](class_stringname.md#class_StringName), font: [Font](class_font.md#class_Font) ) [🔗](class_control.md#class_Control_method_add_theme_font_override)

Creates a local override for a theme [Font](class_font.md#class_Font) with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_font_override()](class_control.md#class_Control_method_remove_theme_font_override).

See also [get_theme_font()](class_control.md#class_Control_method_get_theme_font).

---

<span id="class_Control_method_add_theme_font_size_override"></span>

void **add_theme_font_size_override** ( name: [StringName](class_stringname.md#class_StringName), font_size: [int](class_int.md#class_int) ) [🔗](class_control.md#class_Control_method_add_theme_font_size_override)

Creates a local override for a theme font size with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_font_size_override()](class_control.md#class_Control_method_remove_theme_font_size_override).

See also [get_theme_font_size()](class_control.md#class_Control_method_get_theme_font_size).

---

<span id="class_Control_method_add_theme_icon_override"></span>

void **add_theme_icon_override** ( name: [StringName](class_stringname.md#class_StringName), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_control.md#class_Control_method_add_theme_icon_override)

Creates a local override for a theme icon with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_icon_override()](class_control.md#class_Control_method_remove_theme_icon_override).

See also [get_theme_icon()](class_control.md#class_Control_method_get_theme_icon).

---

<span id="class_Control_method_add_theme_stylebox_override"></span>

void **add_theme_stylebox_override** ( name: [StringName](class_stringname.md#class_StringName), stylebox: [StyleBox](class_stylebox.md#class_StyleBox) ) [🔗](class_control.md#class_Control_method_add_theme_stylebox_override)

Creates a local override for a theme [StyleBox](class_stylebox.md#class_StyleBox) with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with [remove_theme_stylebox_override()](class_control.md#class_Control_method_remove_theme_stylebox_override).

See also [get_theme_stylebox()](class_control.md#class_Control_method_get_theme_stylebox).

 **Example:** Modify a property in a [StyleBox](class_stylebox.md#class_StyleBox) by duplicating it:

.. tabs::

```
```

    # The snippet below assumes the child node "MyButton" has a StyleBoxFlat assigned.
    # Resources are shared across instances, so we need to duplicate it
    # to avoid modifying the appearance of all other buttons.
    var new_stylebox_normal = $MyButton.get_theme_stylebox("normal").duplicate()
    new_stylebox_normal.border_width_top = 3
    new_stylebox_normal.border_color = Color(0, 1, 0.5)
    $MyButton.add_theme_stylebox_override("normal", new_stylebox_normal)
    # Remove the stylebox override.
    $MyButton.remove_theme_stylebox_override("normal")

```
```

    // The snippet below assumes the child node "MyButton" has a StyleBoxFlat assigned.
    // Resources are shared across instances, so we need to duplicate it
    // to avoid modifying the appearance of all other buttons.
    StyleBoxFlat newStyleboxNormal = GetNode<Button>("MyButton").GetThemeStylebox("normal").Duplicate() as StyleBoxFlat;
    newStyleboxNormal.BorderWidthTop = 3;
    newStyleboxNormal.BorderColor = new Color(0, 1, 0.5f);
    GetNode<Button>("MyButton").AddThemeStyleboxOverride("normal", newStyleboxNormal);
    // Remove the stylebox override.
    GetNode<Button>("MyButton").RemoveThemeStyleboxOverride("normal");

---

<span id="class_Control_method_begin_bulk_theme_override"></span>

void **begin_bulk_theme_override** ( ) [🔗](class_control.md#class_Control_method_begin_bulk_theme_override)

Prevents `*_theme_*_override` methods from emitting [NOTIFICATION_THEME_CHANGED](class_control.md#class_Control_constant_NOTIFICATION_THEME_CHANGED) until [end_bulk_theme_override()](class_control.md#class_Control_method_end_bulk_theme_override) is called.

---

<span id="class_Control_method_end_bulk_theme_override"></span>

void **end_bulk_theme_override** ( ) [🔗](class_control.md#class_Control_method_end_bulk_theme_override)

Ends a bulk theme override update. See [begin_bulk_theme_override()](class_control.md#class_Control_method_begin_bulk_theme_override).

---

<span id="class_Control_method_find_next_valid_focus"></span>

[Control](class_control.md#class_Control) **find_next_valid_focus** ( ) *const* [🔗](class_control.md#class_Control_method_find_next_valid_focus)

Finds the next (below in the tree) **Control** that can receive the focus.

---

<span id="class_Control_method_find_prev_valid_focus"></span>

[Control](class_control.md#class_Control) **find_prev_valid_focus** ( ) *const* [🔗](class_control.md#class_Control_method_find_prev_valid_focus)

Finds the previous (above in the tree) **Control** that can receive the focus.

---

<span id="class_Control_method_find_valid_focus_neighbor"></span>

[Control](class_control.md#class_Control) **find_valid_focus_neighbor** ( side: Side ) *const* [🔗](class_control.md#class_Control_method_find_valid_focus_neighbor)

Finds the next **Control** that can receive the focus on the specified Side.

 **Note:** This is different from [get_focus_neighbor()](class_control.md#class_Control_method_get_focus_neighbor), which returns the path of a specified focus neighbor.

---

<span id="class_Control_method_force_drag"></span>

void **force_drag** ( data: [Variant](class_variant.md#class_Variant), preview: [Control](class_control.md#class_Control) ) [🔗](class_control.md#class_Control_method_force_drag)

Forces drag and bypasses [_get_drag_data()](class_control.md#class_Control_private_method__get_drag_data) and [set_drag_preview()](class_control.md#class_Control_method_set_drag_preview) by passing `data` and `preview`. Drag will start even if the mouse is neither over nor pressed on this control.

The methods [_can_drop_data()](class_control.md#class_Control_private_method__can_drop_data) and [_drop_data()](class_control.md#class_Control_private_method__drop_data) must be implemented on controls that want to receive drop data.

---

<span id="class_Control_method_get_anchor"></span>

[float](class_float.md#class_float) **get_anchor** ( side: Side ) *const* [🔗](class_control.md#class_Control_method_get_anchor)

Returns the anchor for the specified Side. A getter method for [anchor_bottom](class_control.md#class_Control_property_anchor_bottom), [anchor_left](class_control.md#class_Control_property_anchor_left), [anchor_right](class_control.md#class_Control_property_anchor_right) and [anchor_top](class_control.md#class_Control_property_anchor_top).

---

<span id="class_Control_method_get_begin"></span>

[Vector2](class_vector2.md#class_Vector2) **get_begin** ( ) *const* [🔗](class_control.md#class_Control_method_get_begin)

Returns [offset_left](class_control.md#class_Control_property_offset_left) and [offset_top](class_control.md#class_Control_property_offset_top). See also [position](class_control.md#class_Control_property_position).

---

<span id="class_Control_method_get_combined_minimum_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_combined_minimum_size** ( ) *const* [🔗](class_control.md#class_Control_method_get_combined_minimum_size)

Returns combined minimum size from [custom_minimum_size](class_control.md#class_Control_property_custom_minimum_size) and [get_minimum_size()](class_control.md#class_Control_method_get_minimum_size).

---

<span id="class_Control_method_get_combined_pivot_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **get_combined_pivot_offset** ( ) *const* [🔗](class_control.md#class_Control_method_get_combined_pivot_offset)

Returns the combined value of [pivot_offset](class_control.md#class_Control_property_pivot_offset) and [pivot_offset_ratio](class_control.md#class_Control_property_pivot_offset_ratio), in pixels. The ratio is multiplied by the control's size.

---

<span id="class_Control_method_get_cursor_shape"></span>

[CursorShape](class_control.md#enum_Control_CursorShape) **get_cursor_shape** ( position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) *const* [🔗](class_control.md#class_Control_method_get_cursor_shape)

Returns the mouse cursor shape for this control when hovered over `position` in local coordinates. For most controls, this is the same as [mouse_default_cursor_shape](class_control.md#class_Control_property_mouse_default_cursor_shape), but some built-in controls implement more complex logic.

---

<span id="class_Control_method_get_end"></span>

[Vector2](class_vector2.md#class_Vector2) **get_end** ( ) *const* [🔗](class_control.md#class_Control_method_get_end)

Returns [offset_right](class_control.md#class_Control_property_offset_right) and [offset_bottom](class_control.md#class_Control_property_offset_bottom).

---

<span id="class_Control_method_get_focus_mode_with_override"></span>

[FocusMode](class_control.md#enum_Control_FocusMode) **get_focus_mode_with_override** ( ) *const* [🔗](class_control.md#class_Control_method_get_focus_mode_with_override)

Returns the [focus_mode](class_control.md#class_Control_property_focus_mode), but takes the [focus_behavior_recursive](class_control.md#class_Control_property_focus_behavior_recursive) into account. If [focus_behavior_recursive](class_control.md#class_Control_property_focus_behavior_recursive) is set to [FOCUS_BEHAVIOR_DISABLED](class_control.md#class_Control_constant_FOCUS_BEHAVIOR_DISABLED), or it is set to [FOCUS_BEHAVIOR_INHERITED](class_control.md#class_Control_constant_FOCUS_BEHAVIOR_INHERITED) and its ancestor is set to [FOCUS_BEHAVIOR_DISABLED](class_control.md#class_Control_constant_FOCUS_BEHAVIOR_DISABLED), then this returns [FOCUS_NONE](class_control.md#class_Control_constant_FOCUS_NONE).

---

<span id="class_Control_method_get_focus_neighbor"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_focus_neighbor** ( side: Side ) *const* [🔗](class_control.md#class_Control_method_get_focus_neighbor)

Returns the focus neighbor for the specified Side. A getter method for [focus_neighbor_bottom](class_control.md#class_Control_property_focus_neighbor_bottom), [focus_neighbor_left](class_control.md#class_Control_property_focus_neighbor_left), [focus_neighbor_right](class_control.md#class_Control_property_focus_neighbor_right) and [focus_neighbor_top](class_control.md#class_Control_property_focus_neighbor_top).

 **Note:** To find the next **Control** on the specific Side, even if a neighbor is not assigned, use [find_valid_focus_neighbor()](class_control.md#class_Control_method_find_valid_focus_neighbor).

---

<span id="class_Control_method_get_global_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **get_global_rect** ( ) *const* [🔗](class_control.md#class_Control_method_get_global_rect)

Returns the position and size of the control relative to the containing canvas. See [global_position](class_control.md#class_Control_property_global_position) and [size](class_control.md#class_Control_property_size).

 **Note:** If the node itself or any parent [CanvasItem](class_canvasitem.md#class_CanvasItem) between the node and the canvas have a non default rotation or skew, the resulting size is likely not meaningful.

 **Note:** Setting [Viewport.gui_snap_controls_to_pixels](class_viewport.md#class_Viewport_property_gui_snap_controls_to_pixels) to `true` can lead to rounding inaccuracies between the displayed control and the returned [Rect2](class_rect2.md#class_Rect2).

---

<span id="class_Control_method_get_minimum_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_minimum_size** ( ) *const* [🔗](class_control.md#class_Control_method_get_minimum_size)

Returns the minimum size for this control. See [custom_minimum_size](class_control.md#class_Control_property_custom_minimum_size).

---

<span id="class_Control_method_get_mouse_filter_with_override"></span>

[MouseFilter](class_control.md#enum_Control_MouseFilter) **get_mouse_filter_with_override** ( ) *const* [🔗](class_control.md#class_Control_method_get_mouse_filter_with_override)

Returns the [mouse_filter](class_control.md#class_Control_property_mouse_filter), but takes the [mouse_behavior_recursive](class_control.md#class_Control_property_mouse_behavior_recursive) into account. If [mouse_behavior_recursive](class_control.md#class_Control_property_mouse_behavior_recursive) is set to [MOUSE_BEHAVIOR_DISABLED](class_control.md#class_Control_constant_MOUSE_BEHAVIOR_DISABLED), or it is set to [MOUSE_BEHAVIOR_INHERITED](class_control.md#class_Control_constant_MOUSE_BEHAVIOR_INHERITED) and its ancestor is set to [MOUSE_BEHAVIOR_DISABLED](class_control.md#class_Control_constant_MOUSE_BEHAVIOR_DISABLED), then this returns [MOUSE_FILTER_IGNORE](class_control.md#class_Control_constant_MOUSE_FILTER_IGNORE).

---

<span id="class_Control_method_get_offset"></span>

[float](class_float.md#class_float) **get_offset** ( offset: Side ) *const* [🔗](class_control.md#class_Control_method_get_offset)

Returns the offset for the specified Side. A getter method for [offset_bottom](class_control.md#class_Control_property_offset_bottom), [offset_left](class_control.md#class_Control_property_offset_left), [offset_right](class_control.md#class_Control_property_offset_right) and [offset_top](class_control.md#class_Control_property_offset_top).

---

<span id="class_Control_method_get_parent_area_size"></span>

[Vector2](class_vector2.md#class_Vector2) **get_parent_area_size** ( ) *const* [🔗](class_control.md#class_Control_method_get_parent_area_size)

Returns the width/height occupied in the parent control.

---

<span id="class_Control_method_get_parent_control"></span>

[Control](class_control.md#class_Control) **get_parent_control** ( ) *const* [🔗](class_control.md#class_Control_method_get_parent_control)

Returns the parent control node.

---

<span id="class_Control_method_get_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **get_rect** ( ) *const* [🔗](class_control.md#class_Control_method_get_rect)

Returns the position and size of the control in the coordinate system of the containing node. See [position](class_control.md#class_Control_property_position), [scale](class_control.md#class_Control_property_scale) and [size](class_control.md#class_Control_property_size).

 **Note:** If [rotation](class_control.md#class_Control_property_rotation) is not the default rotation, the resulting size is not meaningful.

 **Note:** Setting [Viewport.gui_snap_controls_to_pixels](class_viewport.md#class_Viewport_property_gui_snap_controls_to_pixels) to `true` can lead to rounding inaccuracies between the displayed control and the returned [Rect2](class_rect2.md#class_Rect2).

---

<span id="class_Control_method_get_screen_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_screen_position** ( ) *const* [🔗](class_control.md#class_Control_method_get_screen_position)

Returns the position of this **Control** in global screen coordinates (i.e. taking window position into account). Mostly useful for editor plugins.

Equivalent to `get_screen_transform().origin` (see [CanvasItem.get_screen_transform()](class_canvasitem.md#class_CanvasItem_method_get_screen_transform)).

 **Example:** Show a popup at the mouse position:

::

    popup_menu.position = get_screen_position() + get_screen_transform().basis_xform(get_local_mouse_position())

    # The above code is equivalent to:
    popup_menu.position = get_screen_transform() * get_local_mouse_position()

    popup_menu.reset_size()
    popup_menu.popup()

---

<span id="class_Control_method_get_theme_color"></span>

[Color](class_color.md#class_Color) **get_theme_color** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_get_theme_color)

Returns a [Color](class_color.md#class_Color) from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a color item with the specified `name` and `theme_type`. If `theme_type` is omitted the class name of the current control is used as the type, or [theme_type_variation](class_control.md#class_Control_property_theme_type_variation) if it is defined. If the type is a class name its parent classes are also checked, in order of inheritance. If the type is a variation its base types are checked, in order of dependency, then the control's class name and its parent classes are checked.

For the current control its local overrides are considered first (see [add_theme_color_override()](class_control.md#class_Control_method_add_theme_color_override)), then its assigned [theme](class_control.md#class_Control_property_theme). After the current control, each parent control and its assigned [theme](class_control.md#class_Control_property_theme) are considered; controls without a [theme](class_control.md#class_Control_property_theme) assigned are skipped. If no matching [Theme](class_theme.md#class_Theme) is found in the tree, the custom project [Theme](class_theme.md#class_Theme) (see ProjectSettings.gui/theme/custom) and the default [Theme](class_theme.md#class_Theme) are used (see [ThemeDB](class_themedb.md#class_ThemeDB)).

.. tabs::

```
```

    func _ready():
        # Get the font color defined for the current Control's class, if it exists.
        modulate = get_theme_color("font_color")
        # Get the font color defined for the Button class.
        modulate = get_theme_color("font_color", "Button")

```
```

    public override void _Ready()
    {
        // Get the font color defined for the current Control's class, if it exists.
        Modulate = GetThemeColor("font_color");
        // Get the font color defined for the Button class.
        Modulate = GetThemeColor("font_color", "Button");
    }

---

<span id="class_Control_method_get_theme_constant"></span>

[int](class_int.md#class_int) **get_theme_constant** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_get_theme_constant)

Returns a constant from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a constant item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_get_theme_default_base_scale"></span>

[float](class_float.md#class_float) **get_theme_default_base_scale** ( ) *const* [🔗](class_control.md#class_Control_method_get_theme_default_base_scale)

Returns the default base scale value from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a valid [Theme.default_base_scale](class_theme.md#class_Theme_property_default_base_scale) value.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_get_theme_default_font"></span>

[Font](class_font.md#class_Font) **get_theme_default_font** ( ) *const* [🔗](class_control.md#class_Control_method_get_theme_default_font)

Returns the default font from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a valid [Theme.default_font](class_theme.md#class_Theme_property_default_font) value.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_get_theme_default_font_size"></span>

[int](class_int.md#class_int) **get_theme_default_font_size** ( ) *const* [🔗](class_control.md#class_Control_method_get_theme_default_font_size)

Returns the default font size value from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a valid [Theme.default_font_size](class_theme.md#class_Theme_property_default_font_size) value.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_get_theme_font"></span>

[Font](class_font.md#class_Font) **get_theme_font** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_get_theme_font)

Returns a [Font](class_font.md#class_Font) from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a font item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_get_theme_font_size"></span>

[int](class_int.md#class_int) **get_theme_font_size** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_get_theme_font_size)

Returns a font size from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a font size item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_get_theme_icon"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_theme_icon** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_get_theme_icon)

Returns an icon from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has an icon item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_get_theme_stylebox"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **get_theme_stylebox** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_get_theme_stylebox)

Returns a [StyleBox](class_stylebox.md#class_StyleBox) from the first matching [Theme](class_theme.md#class_Theme) in the tree if that [Theme](class_theme.md#class_Theme) has a stylebox item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_get_tooltip"></span>

[String](class_string.md#class_String) **get_tooltip** ( at_position: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, 0) ) *const* [🔗](class_control.md#class_Control_method_get_tooltip)

Returns the tooltip text for the position `at_position` in control's local coordinates, which will typically appear when the cursor is resting over this control. By default, it returns [tooltip_text](class_control.md#class_Control_property_tooltip_text).

This method can be overridden to customize its behavior. See [_get_tooltip()](class_control.md#class_Control_private_method__get_tooltip).

 **Note:** If this method returns an empty [String](class_string.md#class_String) and [_make_custom_tooltip()](class_control.md#class_Control_private_method__make_custom_tooltip) is not overridden, no tooltip is displayed.

---

<span id="class_Control_method_grab_click_focus"></span>

void **grab_click_focus** ( ) [🔗](class_control.md#class_Control_method_grab_click_focus)

Creates an [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton) that attempts to click the control. If the event is received, the control gains focus.

.. tabs::

```
```

    func _process(delta):
        grab_click_focus() # When clicking another Control node, this node will be clicked instead.

```
```

    public override void _Process(double delta)
    {
        GrabClickFocus(); // When clicking another Control node, this node will be clicked instead.
    }

---

<span id="class_Control_method_grab_focus"></span>

void **grab_focus** ( hide_focus: [bool](class_bool.md#class_bool) = false ) [🔗](class_control.md#class_Control_method_grab_focus)

Steal the focus from another control and become the focused control (see [focus_mode](class_control.md#class_Control_property_focus_mode)).

If `hide_focus` is `true`, the control will not visually show its focused state. Has no effect for [LineEdit](class_lineedit.md#class_LineEdit) and [TextEdit](class_textedit.md#class_TextEdit) when ProjectSettings.gui/common/show_focus_state_on_pointer_event is set to `Control Supports Keyboard Input`, or for any control when it is set to `Always`.

 **Note:** Using this method together with [Callable.call_deferred()](class_callable.md#class_Callable_method_call_deferred) makes it more reliable, especially when called inside [Node._ready()](class_node.md#class_Node_private_method__ready).

---

<span id="class_Control_method_has_focus"></span>

[bool](class_bool.md#class_bool) **has_focus** ( ignore_hidden_focus: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_control.md#class_Control_method_has_focus)

Returns `true` if this is the current focused control. See [focus_mode](class_control.md#class_Control_property_focus_mode).

If `ignore_hidden_focus` is `true`, controls that have their focus hidden will always return `false`. Hidden focus happens automatically when controls gain focus via mouse input, or manually using [grab_focus()](class_control.md#class_Control_method_grab_focus) with `hide_focus` set to `true`.

---

<span id="class_Control_method_has_theme_color"></span>

[bool](class_bool.md#class_bool) **has_theme_color** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_has_theme_color)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a color item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_has_theme_color_override"></span>

[bool](class_bool.md#class_bool) **has_theme_color_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_control.md#class_Control_method_has_theme_color_override)

Returns `true` if there is a local override for a theme [Color](class_color.md#class_Color) with the specified `name` in this **Control** node.

See [add_theme_color_override()](class_control.md#class_Control_method_add_theme_color_override).

---

<span id="class_Control_method_has_theme_constant"></span>

[bool](class_bool.md#class_bool) **has_theme_constant** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_has_theme_constant)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a constant item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_has_theme_constant_override"></span>

[bool](class_bool.md#class_bool) **has_theme_constant_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_control.md#class_Control_method_has_theme_constant_override)

Returns `true` if there is a local override for a theme constant with the specified `name` in this **Control** node.

See [add_theme_constant_override()](class_control.md#class_Control_method_add_theme_constant_override).

---

<span id="class_Control_method_has_theme_font"></span>

[bool](class_bool.md#class_bool) **has_theme_font** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_has_theme_font)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a font item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_has_theme_font_override"></span>

[bool](class_bool.md#class_bool) **has_theme_font_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_control.md#class_Control_method_has_theme_font_override)

Returns `true` if there is a local override for a theme [Font](class_font.md#class_Font) with the specified `name` in this **Control** node.

See [add_theme_font_override()](class_control.md#class_Control_method_add_theme_font_override).

---

<span id="class_Control_method_has_theme_font_size"></span>

[bool](class_bool.md#class_bool) **has_theme_font_size** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_has_theme_font_size)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a font size item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_has_theme_font_size_override"></span>

[bool](class_bool.md#class_bool) **has_theme_font_size_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_control.md#class_Control_method_has_theme_font_size_override)

Returns `true` if there is a local override for a theme font size with the specified `name` in this **Control** node.

See [add_theme_font_size_override()](class_control.md#class_Control_method_add_theme_font_size_override).

---

<span id="class_Control_method_has_theme_icon"></span>

[bool](class_bool.md#class_bool) **has_theme_icon** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_has_theme_icon)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has an icon item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_has_theme_icon_override"></span>

[bool](class_bool.md#class_bool) **has_theme_icon_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_control.md#class_Control_method_has_theme_icon_override)

Returns `true` if there is a local override for a theme icon with the specified `name` in this **Control** node.

See [add_theme_icon_override()](class_control.md#class_Control_method_add_theme_icon_override).

---

<span id="class_Control_method_has_theme_stylebox"></span>

[bool](class_bool.md#class_bool) **has_theme_stylebox** ( name: [StringName](class_stringname.md#class_StringName), theme_type: [StringName](class_stringname.md#class_StringName) = &"" ) *const* [🔗](class_control.md#class_Control_method_has_theme_stylebox)

Returns `true` if there is a matching [Theme](class_theme.md#class_Theme) in the tree that has a stylebox item with the specified `name` and `theme_type`.

See [get_theme_color()](class_control.md#class_Control_method_get_theme_color) for details.

---

<span id="class_Control_method_has_theme_stylebox_override"></span>

[bool](class_bool.md#class_bool) **has_theme_stylebox_override** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_control.md#class_Control_method_has_theme_stylebox_override)

Returns `true` if there is a local override for a theme [StyleBox](class_stylebox.md#class_StyleBox) with the specified `name` in this **Control** node.

See [add_theme_stylebox_override()](class_control.md#class_Control_method_add_theme_stylebox_override).

---

<span id="class_Control_method_is_drag_successful"></span>

[bool](class_bool.md#class_bool) **is_drag_successful** ( ) *const* [🔗](class_control.md#class_Control_method_is_drag_successful)

Returns `true` if a drag operation is successful. Alternative to [Viewport.gui_is_drag_successful()](class_viewport.md#class_Viewport_method_gui_is_drag_successful).

Best used with [Node.NOTIFICATION_DRAG_END](class_node.md#class_Node_constant_NOTIFICATION_DRAG_END).

---

<span id="class_Control_method_is_layout_rtl"></span>

[bool](class_bool.md#class_bool) **is_layout_rtl** ( ) *const* [🔗](class_control.md#class_Control_method_is_layout_rtl)

Returns `true` if the layout is right-to-left. See also [layout_direction](class_control.md#class_Control_property_layout_direction).

---

<span id="class_Control_method_release_focus"></span>

void **release_focus** ( ) [🔗](class_control.md#class_Control_method_release_focus)

Give up the focus. No other control will be able to receive input.

---

<span id="class_Control_method_remove_theme_color_override"></span>

void **remove_theme_color_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_control.md#class_Control_method_remove_theme_color_override)

Removes a local override for a theme [Color](class_color.md#class_Color) with the specified `name` previously added by [add_theme_color_override()](class_control.md#class_Control_method_add_theme_color_override) or via the Inspector dock.

---

<span id="class_Control_method_remove_theme_constant_override"></span>

void **remove_theme_constant_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_control.md#class_Control_method_remove_theme_constant_override)

Removes a local override for a theme constant with the specified `name` previously added by [add_theme_constant_override()](class_control.md#class_Control_method_add_theme_constant_override) or via the Inspector dock.

---

<span id="class_Control_method_remove_theme_font_override"></span>

void **remove_theme_font_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_control.md#class_Control_method_remove_theme_font_override)

Removes a local override for a theme [Font](class_font.md#class_Font) with the specified `name` previously added by [add_theme_font_override()](class_control.md#class_Control_method_add_theme_font_override) or via the Inspector dock.

---

<span id="class_Control_method_remove_theme_font_size_override"></span>

void **remove_theme_font_size_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_control.md#class_Control_method_remove_theme_font_size_override)

Removes a local override for a theme font size with the specified `name` previously added by [add_theme_font_size_override()](class_control.md#class_Control_method_add_theme_font_size_override) or via the Inspector dock.

---

<span id="class_Control_method_remove_theme_icon_override"></span>

void **remove_theme_icon_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_control.md#class_Control_method_remove_theme_icon_override)

Removes a local override for a theme icon with the specified `name` previously added by [add_theme_icon_override()](class_control.md#class_Control_method_add_theme_icon_override) or via the Inspector dock.

---

<span id="class_Control_method_remove_theme_stylebox_override"></span>

void **remove_theme_stylebox_override** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_control.md#class_Control_method_remove_theme_stylebox_override)

Removes a local override for a theme [StyleBox](class_stylebox.md#class_StyleBox) with the specified `name` previously added by [add_theme_stylebox_override()](class_control.md#class_Control_method_add_theme_stylebox_override) or via the Inspector dock.

---

<span id="class_Control_method_reset_size"></span>

void **reset_size** ( ) [🔗](class_control.md#class_Control_method_reset_size)

Resets the size to [get_combined_minimum_size()](class_control.md#class_Control_method_get_combined_minimum_size). This is equivalent to calling `set_size(Vector2())` (or any size below the minimum).

---

<span id="class_Control_method_set_anchor"></span>

void **set_anchor** ( side: Side, anchor: [float](class_float.md#class_float), keep_offset: [bool](class_bool.md#class_bool) = false, push_opposite_anchor: [bool](class_bool.md#class_bool) = true ) [🔗](class_control.md#class_Control_method_set_anchor)

Sets the anchor for the specified Side to `anchor`. A setter method for [anchor_bottom](class_control.md#class_Control_property_anchor_bottom), [anchor_left](class_control.md#class_Control_property_anchor_left), [anchor_right](class_control.md#class_Control_property_anchor_right) and [anchor_top](class_control.md#class_Control_property_anchor_top).

If `keep_offset` is `true`, offsets aren't updated after this operation.

If `push_opposite_anchor` is `true` and the opposite anchor overlaps this anchor, the opposite one will have its value overridden. For example, when setting left anchor to 1 and the right anchor has value of 0.5, the right anchor will also get value of 1. If `push_opposite_anchor` was `false`, the left anchor would get value 0.5.

---

<span id="class_Control_method_set_anchor_and_offset"></span>

void **set_anchor_and_offset** ( side: Side, anchor: [float](class_float.md#class_float), offset: [float](class_float.md#class_float), push_opposite_anchor: [bool](class_bool.md#class_bool) = false ) [🔗](class_control.md#class_Control_method_set_anchor_and_offset)

Works the same as [set_anchor()](class_control.md#class_Control_method_set_anchor), but instead of `keep_offset` argument and automatic update of offset, it allows to set the offset yourself (see [set_offset()](class_control.md#class_Control_method_set_offset)).

---

<span id="class_Control_method_set_anchors_and_offsets_preset"></span>

void **set_anchors_and_offsets_preset** ( preset: [LayoutPreset](class_control.md#enum_Control_LayoutPreset), resize_mode: [LayoutPresetMode](class_control.md#enum_Control_LayoutPresetMode) = 0, margin: [int](class_int.md#class_int) = 0 ) [🔗](class_control.md#class_Control_method_set_anchors_and_offsets_preset)

Sets both anchor preset and offset preset. See [set_anchors_preset()](class_control.md#class_Control_method_set_anchors_preset) and [set_offsets_preset()](class_control.md#class_Control_method_set_offsets_preset).

---

<span id="class_Control_method_set_anchors_preset"></span>

void **set_anchors_preset** ( preset: [LayoutPreset](class_control.md#enum_Control_LayoutPreset), keep_offsets: [bool](class_bool.md#class_bool) = false ) [🔗](class_control.md#class_Control_method_set_anchors_preset)

Sets the anchors to a `preset` from [LayoutPreset](class_control.md#enum_Control_LayoutPreset) enum. This is the code equivalent to using the Layout menu in the 2D editor.

If `keep_offsets` is `true`, control's position will also be updated.

---

<span id="class_Control_method_set_begin"></span>

void **set_begin** ( position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_control.md#class_Control_method_set_begin)

Sets [offset_left](class_control.md#class_Control_property_offset_left) and [offset_top](class_control.md#class_Control_property_offset_top) at the same time. Equivalent of changing [position](class_control.md#class_Control_property_position).

---

<span id="class_Control_method_set_drag_forwarding"></span>

void **set_drag_forwarding** ( drag_func: [Callable](class_callable.md#class_Callable), can_drop_func: [Callable](class_callable.md#class_Callable), drop_func: [Callable](class_callable.md#class_Callable) ) [🔗](class_control.md#class_Control_method_set_drag_forwarding)

Sets the given callables to be used instead of the control's own drag-and-drop virtual methods. If a callable is empty, its respective virtual method is used as normal.

The arguments for each callable should be exactly the same as their respective virtual methods, which would be:

- `drag_func` corresponds to [_get_drag_data()](class_control.md#class_Control_private_method__get_drag_data) and requires a [Vector2](class_vector2.md#class_Vector2);

- `can_drop_func` corresponds to [_can_drop_data()](class_control.md#class_Control_private_method__can_drop_data) and requires both a [Vector2](class_vector2.md#class_Vector2) and a [Variant](class_variant.md#class_Variant);

- `drop_func` corresponds to [_drop_data()](class_control.md#class_Control_private_method__drop_data) and requires both a [Vector2](class_vector2.md#class_Vector2) and a [Variant](class_variant.md#class_Variant).

---

<span id="class_Control_method_set_drag_preview"></span>

void **set_drag_preview** ( control: [Control](class_control.md#class_Control) ) [🔗](class_control.md#class_Control_method_set_drag_preview)

Shows the given control at the mouse pointer. A good time to call this method is in [_get_drag_data()](class_control.md#class_Control_private_method__get_drag_data). The control must not be in the scene tree. You should not free the control, and you should not keep a reference to the control beyond the duration of the drag. It will be deleted automatically after the drag has ended.

.. tabs::

```
```

    @export var color = Color(1, 0, 0, 1)

    func _get_drag_data(position):
        # Use a control that is not in the tree
        var cpb = ColorPickerButton.new()
        cpb.color = color
        cpb.size = Vector2(50, 50)
        set_drag_preview(cpb)
        return color

```
```

    [Export]
    private Color _color = new Color(1, 0, 0, 1);

    public override Variant _GetDragData(Vector2 atPosition)
    {
        // Use a control that is not in the tree
        var cpb = new ColorPickerButton();
        cpb.Color = _color;
        cpb.Size = new Vector2(50, 50);
        SetDragPreview(cpb);
        return _color;
    }

---

<span id="class_Control_method_set_end"></span>

void **set_end** ( position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_control.md#class_Control_method_set_end)

Sets [offset_right](class_control.md#class_Control_property_offset_right) and [offset_bottom](class_control.md#class_Control_property_offset_bottom) at the same time.

---

<span id="class_Control_method_set_focus_neighbor"></span>

void **set_focus_neighbor** ( side: Side, neighbor: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_control.md#class_Control_method_set_focus_neighbor)

Sets the focus neighbor for the specified Side to the **Control** at `neighbor` node path. A setter method for [focus_neighbor_bottom](class_control.md#class_Control_property_focus_neighbor_bottom), [focus_neighbor_left](class_control.md#class_Control_property_focus_neighbor_left), [focus_neighbor_right](class_control.md#class_Control_property_focus_neighbor_right) and [focus_neighbor_top](class_control.md#class_Control_property_focus_neighbor_top).

---

<span id="class_Control_method_set_global_position"></span>

void **set_global_position** ( position: [Vector2](class_vector2.md#class_Vector2), keep_offsets: [bool](class_bool.md#class_bool) = false ) [🔗](class_control.md#class_Control_method_set_global_position)

Sets the [global_position](class_control.md#class_Control_property_global_position) to given `position`.

If `keep_offsets` is `true`, control's anchors will be updated instead of offsets.

---

<span id="class_Control_method_set_offset"></span>

void **set_offset** ( side: Side, offset: [float](class_float.md#class_float) ) [🔗](class_control.md#class_Control_method_set_offset)

Sets the offset for the specified Side to `offset`. A setter method for [offset_bottom](class_control.md#class_Control_property_offset_bottom), [offset_left](class_control.md#class_Control_property_offset_left), [offset_right](class_control.md#class_Control_property_offset_right) and [offset_top](class_control.md#class_Control_property_offset_top).

---

<span id="class_Control_method_set_offsets_preset"></span>

void **set_offsets_preset** ( preset: [LayoutPreset](class_control.md#enum_Control_LayoutPreset), resize_mode: [LayoutPresetMode](class_control.md#enum_Control_LayoutPresetMode) = 0, margin: [int](class_int.md#class_int) = 0 ) [🔗](class_control.md#class_Control_method_set_offsets_preset)

Sets the offsets to a `preset` from [LayoutPreset](class_control.md#enum_Control_LayoutPreset) enum. This is the code equivalent to using the Layout menu in the 2D editor.

Use parameter `resize_mode` with constants from [LayoutPresetMode](class_control.md#enum_Control_LayoutPresetMode) to better determine the resulting size of the **Control**. Constant size will be ignored if used with presets that change size, e.g. [PRESET_LEFT_WIDE](class_control.md#class_Control_constant_PRESET_LEFT_WIDE).

Use parameter `margin` to determine the gap between the **Control** and the edges.

---

<span id="class_Control_method_set_position"></span>

void **set_position** ( position: [Vector2](class_vector2.md#class_Vector2), keep_offsets: [bool](class_bool.md#class_bool) = false ) [🔗](class_control.md#class_Control_method_set_position)

Sets the [position](class_control.md#class_Control_property_position) to given `position`.

If `keep_offsets` is `true`, control's anchors will be updated instead of offsets.

---

<span id="class_Control_method_set_size"></span>

void **set_size** ( size: [Vector2](class_vector2.md#class_Vector2), keep_offsets: [bool](class_bool.md#class_bool) = false ) [🔗](class_control.md#class_Control_method_set_size)

Sets the size (see [size](class_control.md#class_Control_property_size)).

If `keep_offsets` is `true`, control's anchors will be updated instead of offsets.

---

<span id="class_Control_method_update_minimum_size"></span>

void **update_minimum_size** ( ) [🔗](class_control.md#class_Control_method_update_minimum_size)

Invalidates the size cache in this node and in parent nodes up to top level. Intended to be used with [get_minimum_size()](class_control.md#class_Control_method_get_minimum_size) when the return value is changed. Setting [custom_minimum_size](class_control.md#class_Control_property_custom_minimum_size) directly calls this method automatically.

---

<span id="class_Control_method_warp_mouse"></span>

void **warp_mouse** ( position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_control.md#class_Control_method_warp_mouse)

Moves the mouse cursor to `position`, relative to [position](class_control.md#class_Control_property_position) of this **Control**.

 **Note:** [warp_mouse()](class_control.md#class_Control_method_warp_mouse) is only supported on Windows, macOS and Linux. It has no effect on Android, iOS and Web.
