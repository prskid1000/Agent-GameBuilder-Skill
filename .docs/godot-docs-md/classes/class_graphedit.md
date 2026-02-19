<span id="class_GraphEdit"></span>

## GraphEdit

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

An editor for graph-like structures, using [GraphNode](class_graphnode.md#class_GraphNode) s.

### Description

**GraphEdit** provides tools for creation, manipulation, and display of various graphs. Its main purpose in the engine is to power the visual programming systems, such as visual shaders, but it is also available for use in user projects.

 **GraphEdit** by itself is only an empty container, representing an infinite grid where [GraphNode](class_graphnode.md#class_GraphNode) s can be placed. Each [GraphNode](class_graphnode.md#class_GraphNode) represents a node in the graph, a single unit of data in the connected scheme. **GraphEdit**, in turn, helps to control various interactions with nodes and between nodes. When the user attempts to connect, disconnect, or delete a [GraphNode](class_graphnode.md#class_GraphNode), a signal is emitted in the **GraphEdit**, but no action is taken by default. It is the responsibility of the programmer utilizing this control to implement the necessary logic to determine how each request should be handled.

 **Performance:** It is greatly advised to enable low-processor usage mode (see [OS.low_processor_usage_mode](class_os.md#class_OS_property_low_processor_usage_mode)) when using GraphEdits.

 **Note:** Keep in mind that [Node.get_children()](class_node.md#class_Node_method_get_children) will also return the connection layer node named `_connection_layer` due to technical limitations. This behavior may change in future releases.

### Properties


| [bool](class_bool.md#class_bool) | clip_contents | `true` (overrides [Control](class_control.md#class_Control_property_clip_contents)) |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [connection_lines_antialiased](class_graphedit.md#class_GraphEdit_property_connection_lines_antialiased) | `true` |
| [float](class_float.md#class_float) | [connection_lines_curvature](class_graphedit.md#class_GraphEdit_property_connection_lines_curvature) | `0.5` |
| [float](class_float.md#class_float) | [connection_lines_thickness](class_graphedit.md#class_GraphEdit_property_connection_lines_thickness) | `4.0` |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [connections](class_graphedit.md#class_GraphEdit_property_connections) | `[]` |
| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `2` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| [GridPattern](class_graphedit.md#enum_GraphEdit_GridPattern) | [grid_pattern](class_graphedit.md#class_GraphEdit_property_grid_pattern) | `0` |
| [bool](class_bool.md#class_bool) | [minimap_enabled](class_graphedit.md#class_GraphEdit_property_minimap_enabled) | `true` |
| [float](class_float.md#class_float) | [minimap_opacity](class_graphedit.md#class_GraphEdit_property_minimap_opacity) | `0.65` |
| [Vector2](class_vector2.md#class_Vector2) | [minimap_size](class_graphedit.md#class_GraphEdit_property_minimap_size) | `Vector2(240, 160)` |
| [PanningScheme](class_graphedit.md#enum_GraphEdit_PanningScheme) | [panning_scheme](class_graphedit.md#class_GraphEdit_property_panning_scheme) | `0` |
| [bool](class_bool.md#class_bool) | [right_disconnects](class_graphedit.md#class_GraphEdit_property_right_disconnects) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [scroll_offset](class_graphedit.md#class_GraphEdit_property_scroll_offset) | `Vector2(0, 0)` |
| [bool](class_bool.md#class_bool) | [show_arrange_button](class_graphedit.md#class_GraphEdit_property_show_arrange_button) | `true` |
| [bool](class_bool.md#class_bool) | [show_grid](class_graphedit.md#class_GraphEdit_property_show_grid) | `true` |
| [bool](class_bool.md#class_bool) | [show_grid_buttons](class_graphedit.md#class_GraphEdit_property_show_grid_buttons) | `true` |
| [bool](class_bool.md#class_bool) | [show_menu](class_graphedit.md#class_GraphEdit_property_show_menu) | `true` |
| [bool](class_bool.md#class_bool) | [show_minimap_button](class_graphedit.md#class_GraphEdit_property_show_minimap_button) | `true` |
| [bool](class_bool.md#class_bool) | [show_zoom_buttons](class_graphedit.md#class_GraphEdit_property_show_zoom_buttons) | `true` |
| [bool](class_bool.md#class_bool) | [show_zoom_label](class_graphedit.md#class_GraphEdit_property_show_zoom_label) | `false` |
| [int](class_int.md#class_int) | [snapping_distance](class_graphedit.md#class_GraphEdit_property_snapping_distance) | `20` |
| [bool](class_bool.md#class_bool) | [snapping_enabled](class_graphedit.md#class_GraphEdit_property_snapping_enabled) | `true` |
| [Dictionary](class_dictionary.md#class_Dictionary) | [type_names](class_graphedit.md#class_GraphEdit_property_type_names) | `{}` |
| [float](class_float.md#class_float) | [zoom](class_graphedit.md#class_GraphEdit_property_zoom) | `1.0` |
| [float](class_float.md#class_float) | [zoom_max](class_graphedit.md#class_GraphEdit_property_zoom_max) | `2.0736003` |
| [float](class_float.md#class_float) | [zoom_min](class_graphedit.md#class_GraphEdit_property_zoom_min) | `0.23256795` |
| [float](class_float.md#class_float) | [zoom_step](class_graphedit.md#class_GraphEdit_property_zoom_step) | `1.2` |

### Methods


| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [_get_connection_line](class_graphedit.md#class_GraphEdit_private_method__get_connection_line) ( from_position: [Vector2](class_vector2.md#class_Vector2), to_position: [Vector2](class_vector2.md#class_Vector2) ) | virtual | const |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_is_in_input_hotzone](class_graphedit.md#class_GraphEdit_private_method__is_in_input_hotzone) ( in_node: [Object](class_object.md#class_Object), in_port: [int](class_int.md#class_int), mouse_position: [Vector2](class_vector2.md#class_Vector2) ) virtual |
| [bool](class_bool.md#class_bool) | [_is_in_output_hotzone](class_graphedit.md#class_GraphEdit_private_method__is_in_output_hotzone) ( in_node: [Object](class_object.md#class_Object), in_port: [int](class_int.md#class_int), mouse_position: [Vector2](class_vector2.md#class_Vector2) ) virtual |
| [bool](class_bool.md#class_bool) | [_is_node_hover_valid](class_graphedit.md#class_GraphEdit_private_method__is_node_hover_valid) ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int) ) virtual |
| void | [add_valid_connection_type](class_graphedit.md#class_GraphEdit_method_add_valid_connection_type) ( from_type: [int](class_int.md#class_int), to_type: [int](class_int.md#class_int) ) |
| void | [add_valid_left_disconnect_type](class_graphedit.md#class_GraphEdit_method_add_valid_left_disconnect_type) ( type: [int](class_int.md#class_int) ) |
| void | [add_valid_right_disconnect_type](class_graphedit.md#class_GraphEdit_method_add_valid_right_disconnect_type) ( type: [int](class_int.md#class_int) ) |
| void | [arrange_nodes](class_graphedit.md#class_GraphEdit_method_arrange_nodes) ( ) |
| void | [attach_graph_element_to_frame](class_graphedit.md#class_GraphEdit_method_attach_graph_element_to_frame) ( element: [StringName](class_stringname.md#class_StringName), frame: [StringName](class_stringname.md#class_StringName) ) |
| void | [clear_connections](class_graphedit.md#class_GraphEdit_method_clear_connections) ( ) |
| Error | [connect_node](class_graphedit.md#class_GraphEdit_method_connect_node) ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int), keep_alive: [bool](class_bool.md#class_bool) = false ) |
| void | [detach_graph_element_from_frame](class_graphedit.md#class_GraphEdit_method_detach_graph_element_from_frame) ( element: [StringName](class_stringname.md#class_StringName) ) |
| void | [disconnect_node](class_graphedit.md#class_GraphEdit_method_disconnect_node) ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int) ) |
| void | [force_connection_drag_end](class_graphedit.md#class_GraphEdit_method_force_connection_drag_end) ( ) |
| [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] | [get_attached_nodes_of_frame](class_graphedit.md#class_GraphEdit_method_get_attached_nodes_of_frame) ( frame: [StringName](class_stringname.md#class_StringName) ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_closest_connection_at_point](class_graphedit.md#class_GraphEdit_method_get_closest_connection_at_point) ( point: [Vector2](class_vector2.md#class_Vector2), max_distance: [float](class_float.md#class_float) = 4.0 ) const |
| [int](class_int.md#class_int) | [get_connection_count](class_graphedit.md#class_GraphEdit_method_get_connection_count) ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int) ) |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [get_connection_line](class_graphedit.md#class_GraphEdit_method_get_connection_line) ( from_node: [Vector2](class_vector2.md#class_Vector2), to_node: [Vector2](class_vector2.md#class_Vector2) ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_connection_list_from_node](class_graphedit.md#class_GraphEdit_method_get_connection_list_from_node) ( node: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_connections_intersecting_with_rect](class_graphedit.md#class_GraphEdit_method_get_connections_intersecting_with_rect) ( rect: [Rect2](class_rect2.md#class_Rect2) ) const |
| [GraphFrame](class_graphframe.md#class_GraphFrame) | [get_element_frame](class_graphedit.md#class_GraphEdit_method_get_element_frame) ( element: [StringName](class_stringname.md#class_StringName) ) |
| [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) | [get_menu_hbox](class_graphedit.md#class_GraphEdit_method_get_menu_hbox) ( ) |
| [bool](class_bool.md#class_bool) | [is_node_connected](class_graphedit.md#class_GraphEdit_method_is_node_connected) ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [is_valid_connection_type](class_graphedit.md#class_GraphEdit_method_is_valid_connection_type) ( from_type: [int](class_int.md#class_int), to_type: [int](class_int.md#class_int) ) const |
| void | [remove_valid_connection_type](class_graphedit.md#class_GraphEdit_method_remove_valid_connection_type) ( from_type: [int](class_int.md#class_int), to_type: [int](class_int.md#class_int) ) |
| void | [remove_valid_left_disconnect_type](class_graphedit.md#class_GraphEdit_method_remove_valid_left_disconnect_type) ( type: [int](class_int.md#class_int) ) |
| void | [remove_valid_right_disconnect_type](class_graphedit.md#class_GraphEdit_method_remove_valid_right_disconnect_type) ( type: [int](class_int.md#class_int) ) |
| void | [set_connection_activity](class_graphedit.md#class_GraphEdit_method_set_connection_activity) ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int), amount: [float](class_float.md#class_float) ) |
| void | [set_selected](class_graphedit.md#class_GraphEdit_method_set_selected) ( node: [Node](class_node.md#class_Node) ) |

### Theme Properties


| [Color](class_color.md#class_Color) | [activity](class_graphedit.md#class_GraphEdit_theme_color_activity) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Color](class_color.md#class_Color) | [connection_hover_tint_color](class_graphedit.md#class_GraphEdit_theme_color_connection_hover_tint_color) | `Color(0, 0, 0, 0.3)` |
| [Color](class_color.md#class_Color) | [connection_rim_color](class_graphedit.md#class_GraphEdit_theme_color_connection_rim_color) | `Color(0.1, 0.1, 0.1, 0.6)` |
| [Color](class_color.md#class_Color) | [connection_valid_target_tint_color](class_graphedit.md#class_GraphEdit_theme_color_connection_valid_target_tint_color) | `Color(1, 1, 1, 0.4)` |
| [Color](class_color.md#class_Color) | [grid_major](class_graphedit.md#class_GraphEdit_theme_color_grid_major) | `Color(1, 1, 1, 0.2)` |
| [Color](class_color.md#class_Color) | [grid_minor](class_graphedit.md#class_GraphEdit_theme_color_grid_minor) | `Color(1, 1, 1, 0.05)` |
| [Color](class_color.md#class_Color) | [selection_fill](class_graphedit.md#class_GraphEdit_theme_color_selection_fill) | `Color(1, 1, 1, 0.3)` |
| [Color](class_color.md#class_Color) | [selection_stroke](class_graphedit.md#class_GraphEdit_theme_color_selection_stroke) | `Color(1, 1, 1, 0.8)` |
| [int](class_int.md#class_int) | [connection_hover_thickness](class_graphedit.md#class_GraphEdit_theme_constant_connection_hover_thickness) | `0` |
| [int](class_int.md#class_int) | [port_hotzone_inner_extent](class_graphedit.md#class_GraphEdit_theme_constant_port_hotzone_inner_extent) | `22` |
| [int](class_int.md#class_int) | [port_hotzone_outer_extent](class_graphedit.md#class_GraphEdit_theme_constant_port_hotzone_outer_extent) | `26` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [grid_toggle](class_graphedit.md#class_GraphEdit_theme_icon_grid_toggle) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [layout](class_graphedit.md#class_GraphEdit_theme_icon_layout) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [minimap_toggle](class_graphedit.md#class_GraphEdit_theme_icon_minimap_toggle) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [snapping_toggle](class_graphedit.md#class_GraphEdit_theme_icon_snapping_toggle) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [zoom_in](class_graphedit.md#class_GraphEdit_theme_icon_zoom_in) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [zoom_out](class_graphedit.md#class_GraphEdit_theme_icon_zoom_out) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [zoom_reset](class_graphedit.md#class_GraphEdit_theme_icon_zoom_reset) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [menu_panel](class_graphedit.md#class_GraphEdit_theme_style_menu_panel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [panel](class_graphedit.md#class_GraphEdit_theme_style_panel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [panel_focus](class_graphedit.md#class_GraphEdit_theme_style_panel_focus) |

---

### Signals

<span id="class_GraphEdit_signal_begin_node_move"></span>

**begin_node_move** ( ) [🔗](class_graphedit.md#class_GraphEdit_signal_begin_node_move)

Emitted at the beginning of a [GraphElement](class_graphelement.md#class_GraphElement)'s movement.

---

<span id="class_GraphEdit_signal_connection_drag_ended"></span>

**connection_drag_ended** ( ) [🔗](class_graphedit.md#class_GraphEdit_signal_connection_drag_ended)

Emitted at the end of a connection drag.

---

<span id="class_GraphEdit_signal_connection_drag_started"></span>

**connection_drag_started** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), is_output: [bool](class_bool.md#class_bool) ) [🔗](class_graphedit.md#class_GraphEdit_signal_connection_drag_started)

Emitted at the beginning of a connection drag.

---

<span id="class_GraphEdit_signal_connection_from_empty"></span>

**connection_from_empty** ( to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int), release_position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_graphedit.md#class_GraphEdit_signal_connection_from_empty)

Emitted when user drags a connection from an input port into the empty space of the graph.

---

<span id="class_GraphEdit_signal_connection_request"></span>

**connection_request** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_signal_connection_request)

Emitted to the GraphEdit when the connection between the `from_port` of the `from_node` [GraphNode](class_graphnode.md#class_GraphNode) and the `to_port` of the `to_node` [GraphNode](class_graphnode.md#class_GraphNode) is attempted to be created.

---

<span id="class_GraphEdit_signal_connection_to_empty"></span>

**connection_to_empty** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), release_position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_graphedit.md#class_GraphEdit_signal_connection_to_empty)

Emitted when user drags a connection from an output port into the empty space of the graph.

---

<span id="class_GraphEdit_signal_copy_nodes_request"></span>

**copy_nodes_request** ( ) [🔗](class_graphedit.md#class_GraphEdit_signal_copy_nodes_request)

Emitted when this **GraphEdit** captures a `ui_copy` action (:kbd:`Ctrl + C` by default). In general, this signal indicates that the selected [GraphElement](class_graphelement.md#class_GraphElement) s should be copied.

---

<span id="class_GraphEdit_signal_cut_nodes_request"></span>

**cut_nodes_request** ( ) [🔗](class_graphedit.md#class_GraphEdit_signal_cut_nodes_request)

Emitted when this **GraphEdit** captures a `ui_cut` action (:kbd:`Ctrl + X` by default). In general, this signal indicates that the selected [GraphElement](class_graphelement.md#class_GraphElement) s should be cut.

---

<span id="class_GraphEdit_signal_delete_nodes_request"></span>

**delete_nodes_request** ( nodes: [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] ) [🔗](class_graphedit.md#class_GraphEdit_signal_delete_nodes_request)

Emitted when this **GraphEdit** captures a `ui_graph_delete` action (:kbd:`Delete` by default).

 `nodes` is an array of node names that should be removed. These usually include all selected nodes.

---

<span id="class_GraphEdit_signal_disconnection_request"></span>

**disconnection_request** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_signal_disconnection_request)

Emitted to the GraphEdit when the connection between `from_port` of `from_node` [GraphNode](class_graphnode.md#class_GraphNode) and `to_port` of `to_node` [GraphNode](class_graphnode.md#class_GraphNode) is attempted to be removed.

---

<span id="class_GraphEdit_signal_duplicate_nodes_request"></span>

**duplicate_nodes_request** ( ) [🔗](class_graphedit.md#class_GraphEdit_signal_duplicate_nodes_request)

Emitted when this **GraphEdit** captures a `ui_graph_duplicate` action (:kbd:`Ctrl + D` by default). In general, this signal indicates that the selected [GraphElement](class_graphelement.md#class_GraphElement) s should be duplicated.

---

<span id="class_GraphEdit_signal_end_node_move"></span>

**end_node_move** ( ) [🔗](class_graphedit.md#class_GraphEdit_signal_end_node_move)

Emitted at the end of a [GraphElement](class_graphelement.md#class_GraphElement)'s movement.

---

<span id="class_GraphEdit_signal_frame_rect_changed"></span>

**frame_rect_changed** ( frame: [GraphFrame](class_graphframe.md#class_GraphFrame), new_rect: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_graphedit.md#class_GraphEdit_signal_frame_rect_changed)

Emitted when the [GraphFrame](class_graphframe.md#class_GraphFrame) `frame` is resized to `new_rect`.

---

<span id="class_GraphEdit_signal_graph_elements_linked_to_frame_request"></span>

**graph_elements_linked_to_frame_request** ( elements: [Array](class_array.md#class_Array), frame: [StringName](class_stringname.md#class_StringName) ) [🔗](class_graphedit.md#class_GraphEdit_signal_graph_elements_linked_to_frame_request)

Emitted when one or more [GraphElement](class_graphelement.md#class_GraphElement) s are dropped onto the [GraphFrame](class_graphframe.md#class_GraphFrame) named `frame`, when they were not previously attached to any other one.

 `elements` is an array of [GraphElement](class_graphelement.md#class_GraphElement) s to be attached.

---

<span id="class_GraphEdit_signal_node_deselected"></span>

**node_deselected** ( node: [Node](class_node.md#class_Node) ) [🔗](class_graphedit.md#class_GraphEdit_signal_node_deselected)

Emitted when the given [GraphElement](class_graphelement.md#class_GraphElement) node is deselected.

---

<span id="class_GraphEdit_signal_node_selected"></span>

**node_selected** ( node: [Node](class_node.md#class_Node) ) [🔗](class_graphedit.md#class_GraphEdit_signal_node_selected)

Emitted when the given [GraphElement](class_graphelement.md#class_GraphElement) node is selected.

---

<span id="class_GraphEdit_signal_paste_nodes_request"></span>

**paste_nodes_request** ( ) [🔗](class_graphedit.md#class_GraphEdit_signal_paste_nodes_request)

Emitted when this **GraphEdit** captures a `ui_paste` action (:kbd:`Ctrl + V` by default). In general, this signal indicates that previously copied [GraphElement](class_graphelement.md#class_GraphElement) s should be pasted.

---

<span id="class_GraphEdit_signal_popup_request"></span>

**popup_request** ( at_position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_graphedit.md#class_GraphEdit_signal_popup_request)

Emitted when a popup is requested. Happens on right-clicking in the GraphEdit. `at_position` is the position of the mouse pointer when the signal is sent.

---

<span id="class_GraphEdit_signal_scroll_offset_changed"></span>

**scroll_offset_changed** ( offset: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_graphedit.md#class_GraphEdit_signal_scroll_offset_changed)

Emitted when the scroll offset is changed by the user. It will not be emitted when changed in code.

---

### Enumerations

<span id="enum_GraphEdit_PanningScheme"></span>

enum **PanningScheme**: [🔗](class_graphedit.md#enum_GraphEdit_PanningScheme)

<span id="class_GraphEdit_constant_SCROLL_ZOOMS"></span>

[PanningScheme](class_graphedit.md#enum_GraphEdit_PanningScheme) **SCROLL_ZOOMS** = `0`

:kbd:`Mouse Wheel` will zoom, :kbd:`Ctrl + Mouse Wheel` will move the view.

<span id="class_GraphEdit_constant_SCROLL_PANS"></span>

[PanningScheme](class_graphedit.md#enum_GraphEdit_PanningScheme) **SCROLL_PANS** = `1`

:kbd:`Mouse Wheel` will move the view, :kbd:`Ctrl + Mouse Wheel` will zoom.

---

<span id="enum_GraphEdit_GridPattern"></span>

enum **GridPattern**: [🔗](class_graphedit.md#enum_GraphEdit_GridPattern)

<span id="class_GraphEdit_constant_GRID_PATTERN_LINES"></span>

[GridPattern](class_graphedit.md#enum_GraphEdit_GridPattern) **GRID_PATTERN_LINES** = `0`

Draw the grid using solid lines.

<span id="class_GraphEdit_constant_GRID_PATTERN_DOTS"></span>

[GridPattern](class_graphedit.md#enum_GraphEdit_GridPattern) **GRID_PATTERN_DOTS** = `1`

Draw the grid using dots.

---

### Property Descriptions

<span id="class_GraphEdit_property_connection_lines_antialiased"></span>

[bool](class_bool.md#class_bool) **connection_lines_antialiased** = `true` [🔗](class_graphedit.md#class_GraphEdit_property_connection_lines_antialiased)

- void **set_connection_lines_antialiased** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_connection_lines_antialiased** ( )

If `true`, the lines between nodes will use antialiasing.

---

<span id="class_GraphEdit_property_connection_lines_curvature"></span>

[float](class_float.md#class_float) **connection_lines_curvature** = `0.5` [🔗](class_graphedit.md#class_GraphEdit_property_connection_lines_curvature)

- void **set_connection_lines_curvature** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_connection_lines_curvature** ( )

The curvature of the lines between the nodes. 0 results in straight lines.

---

<span id="class_GraphEdit_property_connection_lines_thickness"></span>

[float](class_float.md#class_float) **connection_lines_thickness** = `4.0` [🔗](class_graphedit.md#class_GraphEdit_property_connection_lines_thickness)

- void **set_connection_lines_thickness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_connection_lines_thickness** ( )

The thickness of the lines between the nodes.

---

<span id="class_GraphEdit_property_connections"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **connections** = `[]` [🔗](class_graphedit.md#class_GraphEdit_property_connections)

- void **set_connections** ( value: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] )
- [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_connection_list** ( )

The connections between [GraphNode](class_graphnode.md#class_GraphNode) s.

A connection is represented as a [Dictionary](class_dictionary.md#class_Dictionary) in the form of:

::

    {
        from_node: StringName,
        from_port: int,
        to_node: StringName,
        to_port: int,
        keep_alive: bool
    }

Connections with `keep_alive` set to `false` may be deleted automatically if invalid during a redraw.

---

<span id="class_GraphEdit_property_grid_pattern"></span>

[GridPattern](class_graphedit.md#enum_GraphEdit_GridPattern) **grid_pattern** = `0` [🔗](class_graphedit.md#class_GraphEdit_property_grid_pattern)

- void **set_grid_pattern** ( value: [GridPattern](class_graphedit.md#enum_GraphEdit_GridPattern) )
- [GridPattern](class_graphedit.md#enum_GraphEdit_GridPattern) **get_grid_pattern** ( )

The pattern used for drawing the grid.

---

<span id="class_GraphEdit_property_minimap_enabled"></span>

[bool](class_bool.md#class_bool) **minimap_enabled** = `true` [🔗](class_graphedit.md#class_GraphEdit_property_minimap_enabled)

- void **set_minimap_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_minimap_enabled** ( )

If `true`, the minimap is visible.

---

<span id="class_GraphEdit_property_minimap_opacity"></span>

[float](class_float.md#class_float) **minimap_opacity** = `0.65` [🔗](class_graphedit.md#class_GraphEdit_property_minimap_opacity)

- void **set_minimap_opacity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_minimap_opacity** ( )

The opacity of the minimap rectangle.

---

<span id="class_GraphEdit_property_minimap_size"></span>

[Vector2](class_vector2.md#class_Vector2) **minimap_size** = `Vector2(240, 160)` [🔗](class_graphedit.md#class_GraphEdit_property_minimap_size)

- void **set_minimap_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_minimap_size** ( )

The size of the minimap rectangle. The map itself is based on the size of the grid area and is scaled to fit this rectangle.

---

<span id="class_GraphEdit_property_panning_scheme"></span>

[PanningScheme](class_graphedit.md#enum_GraphEdit_PanningScheme) **panning_scheme** = `0` [🔗](class_graphedit.md#class_GraphEdit_property_panning_scheme)

- void **set_panning_scheme** ( value: [PanningScheme](class_graphedit.md#enum_GraphEdit_PanningScheme) )
- [PanningScheme](class_graphedit.md#enum_GraphEdit_PanningScheme) **get_panning_scheme** ( )

Defines the control scheme for panning with mouse wheel.

---

<span id="class_GraphEdit_property_right_disconnects"></span>

[bool](class_bool.md#class_bool) **right_disconnects** = `false` [🔗](class_graphedit.md#class_GraphEdit_property_right_disconnects)

- void **set_right_disconnects** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_right_disconnects_enabled** ( )

If `true`, enables disconnection of existing connections in the GraphEdit by dragging the right end.

---

<span id="class_GraphEdit_property_scroll_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **scroll_offset** = `Vector2(0, 0)` [🔗](class_graphedit.md#class_GraphEdit_property_scroll_offset)

- void **set_scroll_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_scroll_offset** ( )

The scroll offset.

---

<span id="class_GraphEdit_property_show_arrange_button"></span>

[bool](class_bool.md#class_bool) **show_arrange_button** = `true` [🔗](class_graphedit.md#class_GraphEdit_property_show_arrange_button)

- void **set_show_arrange_button** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_showing_arrange_button** ( )

If `true`, the button to automatically arrange graph nodes is visible.

---

<span id="class_GraphEdit_property_show_grid"></span>

[bool](class_bool.md#class_bool) **show_grid** = `true` [🔗](class_graphedit.md#class_GraphEdit_property_show_grid)

- void **set_show_grid** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_showing_grid** ( )

If `true`, the grid is visible.

---

<span id="class_GraphEdit_property_show_grid_buttons"></span>

[bool](class_bool.md#class_bool) **show_grid_buttons** = `true` [🔗](class_graphedit.md#class_GraphEdit_property_show_grid_buttons)

- void **set_show_grid_buttons** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_showing_grid_buttons** ( )

If `true`, buttons that allow to configure grid and snapping options are visible.

---

<span id="class_GraphEdit_property_show_menu"></span>

[bool](class_bool.md#class_bool) **show_menu** = `true` [🔗](class_graphedit.md#class_GraphEdit_property_show_menu)

- void **set_show_menu** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_showing_menu** ( )

If `true`, the menu toolbar is visible.

---

<span id="class_GraphEdit_property_show_minimap_button"></span>

[bool](class_bool.md#class_bool) **show_minimap_button** = `true` [🔗](class_graphedit.md#class_GraphEdit_property_show_minimap_button)

- void **set_show_minimap_button** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_showing_minimap_button** ( )

If `true`, the button to toggle the minimap is visible.

---

<span id="class_GraphEdit_property_show_zoom_buttons"></span>

[bool](class_bool.md#class_bool) **show_zoom_buttons** = `true` [🔗](class_graphedit.md#class_GraphEdit_property_show_zoom_buttons)

- void **set_show_zoom_buttons** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_showing_zoom_buttons** ( )

If `true`, buttons that allow to change and reset the zoom level are visible.

---

<span id="class_GraphEdit_property_show_zoom_label"></span>

[bool](class_bool.md#class_bool) **show_zoom_label** = `false` [🔗](class_graphedit.md#class_GraphEdit_property_show_zoom_label)

- void **set_show_zoom_label** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_showing_zoom_label** ( )

If `true`, the label with the current zoom level is visible. The zoom level is displayed in percents.

---

<span id="class_GraphEdit_property_snapping_distance"></span>

[int](class_int.md#class_int) **snapping_distance** = `20` [🔗](class_graphedit.md#class_GraphEdit_property_snapping_distance)

- void **set_snapping_distance** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_snapping_distance** ( )

The snapping distance in pixels, also determines the grid line distance.

---

<span id="class_GraphEdit_property_snapping_enabled"></span>

[bool](class_bool.md#class_bool) **snapping_enabled** = `true` [🔗](class_graphedit.md#class_GraphEdit_property_snapping_enabled)

- void **set_snapping_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_snapping_enabled** ( )

If `true`, enables snapping.

---

<span id="class_GraphEdit_property_type_names"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **type_names** = `{}` [🔗](class_graphedit.md#class_GraphEdit_property_type_names)

- void **set_type_names** ( value: [Dictionary](class_dictionary.md#class_Dictionary) )
- [Dictionary](class_dictionary.md#class_Dictionary) **get_type_names** ( )

[Dictionary](class_dictionary.md#class_Dictionary) of human-readable port type names.

---

<span id="class_GraphEdit_property_zoom"></span>

[float](class_float.md#class_float) **zoom** = `1.0` [🔗](class_graphedit.md#class_GraphEdit_property_zoom)

- void **set_zoom** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_zoom** ( )

The current zoom value.

---

<span id="class_GraphEdit_property_zoom_max"></span>

[float](class_float.md#class_float) **zoom_max** = `2.0736003` [🔗](class_graphedit.md#class_GraphEdit_property_zoom_max)

- void **set_zoom_max** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_zoom_max** ( )

The upper zoom limit.

---

<span id="class_GraphEdit_property_zoom_min"></span>

[float](class_float.md#class_float) **zoom_min** = `0.23256795` [🔗](class_graphedit.md#class_GraphEdit_property_zoom_min)

- void **set_zoom_min** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_zoom_min** ( )

The lower zoom limit.

---

<span id="class_GraphEdit_property_zoom_step"></span>

[float](class_float.md#class_float) **zoom_step** = `1.2` [🔗](class_graphedit.md#class_GraphEdit_property_zoom_step)

- void **set_zoom_step** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_zoom_step** ( )

The step of each zoom level.

---

### Method Descriptions

<span id="class_GraphEdit_private_method__get_connection_line"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **_get_connection_line** ( from_position: [Vector2](class_vector2.md#class_Vector2), to_position: [Vector2](class_vector2.md#class_Vector2) ) *virtual* *const* [🔗](class_graphedit.md#class_GraphEdit_private_method__get_connection_line)

Virtual method which can be overridden to customize how connections are drawn.

---

<span id="class_GraphEdit_private_method__is_in_input_hotzone"></span>

[bool](class_bool.md#class_bool) **_is_in_input_hotzone** ( in_node: [Object](class_object.md#class_Object), in_port: [int](class_int.md#class_int), mouse_position: [Vector2](class_vector2.md#class_Vector2) ) *virtual* [🔗](class_graphedit.md#class_GraphEdit_private_method__is_in_input_hotzone)

Returns whether the `mouse_position` is in the input hot zone.

By default, a hot zone is a [Rect2](class_rect2.md#class_Rect2) positioned such that its center is at `in_node`. [GraphNode.get_input_port_position()](class_graphnode.md#class_GraphNode_method_get_input_port_position) (`in_port`) (For output's case, call [GraphNode.get_output_port_position()](class_graphnode.md#class_GraphNode_method_get_output_port_position) instead). The hot zone's width is twice the Theme Property `port_grab_distance_horizontal`, and its height is twice the `port_grab_distance_vertical`.

Below is a sample code to help get started:

::

    func _is_in_input_hotzone(in_node, in_port, mouse_position):
        var port_size = Vector2(get_theme_constant("port_grab_distance_horizontal"), get_theme_constant("port_grab_distance_vertical"))
        var port_pos = in_node.get_position() + in_node.get_input_port_position(in_port) - port_size / 2
        var rect = Rect2(port_pos, port_size)

        return rect.has_point(mouse_position)

---

<span id="class_GraphEdit_private_method__is_in_output_hotzone"></span>

[bool](class_bool.md#class_bool) **_is_in_output_hotzone** ( in_node: [Object](class_object.md#class_Object), in_port: [int](class_int.md#class_int), mouse_position: [Vector2](class_vector2.md#class_Vector2) ) *virtual* [🔗](class_graphedit.md#class_GraphEdit_private_method__is_in_output_hotzone)

Returns whether the `mouse_position` is in the output hot zone. For more information on hot zones, see [_is_in_input_hotzone()](class_graphedit.md#class_GraphEdit_private_method__is_in_input_hotzone).

Below is a sample code to help get started:

::

    func _is_in_output_hotzone(in_node, in_port, mouse_position):
        var port_size = Vector2(get_theme_constant("port_grab_distance_horizontal"), get_theme_constant("port_grab_distance_vertical"))
        var port_pos = in_node.get_position() + in_node.get_output_port_position(in_port) - port_size / 2
        var rect = Rect2(port_pos, port_size)

        return rect.has_point(mouse_position)

---

<span id="class_GraphEdit_private_method__is_node_hover_valid"></span>

[bool](class_bool.md#class_bool) **_is_node_hover_valid** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int) ) *virtual* [🔗](class_graphedit.md#class_GraphEdit_private_method__is_node_hover_valid)

This virtual method can be used to insert additional error detection while the user is dragging a connection over a valid port.

Return `true` if the connection is indeed valid or return `false` if the connection is impossible. If the connection is impossible, no snapping to the port and thus no connection request to that port will happen.

In this example a connection to same node is suppressed:

.. tabs::

```
```

    func _is_node_hover_valid(from, from_port, to, to_port):
        return from != to

```
```

    public override bool _IsNodeHoverValid(StringName fromNode, int fromPort, StringName toNode, int toPort)
    {
        return fromNode != toNode;
    }

---

<span id="class_GraphEdit_method_add_valid_connection_type"></span>

void **add_valid_connection_type** ( from_type: [int](class_int.md#class_int), to_type: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_method_add_valid_connection_type)

Allows the connection between two different port types. The port type is defined individually for the left and the right port of each slot with the [GraphNode.set_slot()](class_graphnode.md#class_GraphNode_method_set_slot) method.

See also [is_valid_connection_type()](class_graphedit.md#class_GraphEdit_method_is_valid_connection_type) and [remove_valid_connection_type()](class_graphedit.md#class_GraphEdit_method_remove_valid_connection_type).

---

<span id="class_GraphEdit_method_add_valid_left_disconnect_type"></span>

void **add_valid_left_disconnect_type** ( type: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_method_add_valid_left_disconnect_type)

Allows to disconnect nodes when dragging from the left port of the [GraphNode](class_graphnode.md#class_GraphNode)'s slot if it has the specified type. See also [remove_valid_left_disconnect_type()](class_graphedit.md#class_GraphEdit_method_remove_valid_left_disconnect_type).

---

<span id="class_GraphEdit_method_add_valid_right_disconnect_type"></span>

void **add_valid_right_disconnect_type** ( type: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_method_add_valid_right_disconnect_type)

Allows to disconnect nodes when dragging from the right port of the [GraphNode](class_graphnode.md#class_GraphNode)'s slot if it has the specified type. See also [remove_valid_right_disconnect_type()](class_graphedit.md#class_GraphEdit_method_remove_valid_right_disconnect_type).

---

<span id="class_GraphEdit_method_arrange_nodes"></span>

void **arrange_nodes** ( ) [🔗](class_graphedit.md#class_GraphEdit_method_arrange_nodes)

Rearranges selected nodes in a layout with minimum crossings between connections and uniform horizontal and vertical gap between nodes.

---

<span id="class_GraphEdit_method_attach_graph_element_to_frame"></span>

void **attach_graph_element_to_frame** ( element: [StringName](class_stringname.md#class_StringName), frame: [StringName](class_stringname.md#class_StringName) ) [🔗](class_graphedit.md#class_GraphEdit_method_attach_graph_element_to_frame)

Attaches the `element` [GraphElement](class_graphelement.md#class_GraphElement) to the `frame` [GraphFrame](class_graphframe.md#class_GraphFrame).

---

<span id="class_GraphEdit_method_clear_connections"></span>

void **clear_connections** ( ) [🔗](class_graphedit.md#class_GraphEdit_method_clear_connections)

Removes all connections between nodes.

---

<span id="class_GraphEdit_method_connect_node"></span>

Error **connect_node** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int), keep_alive: [bool](class_bool.md#class_bool) = false ) [🔗](class_graphedit.md#class_GraphEdit_method_connect_node)

Create a connection between the `from_port` of the `from_node` [GraphNode](class_graphnode.md#class_GraphNode) and the `to_port` of the `to_node` [GraphNode](class_graphnode.md#class_GraphNode). If the connection already exists, no connection is created.

Connections with `keep_alive` set to `false` may be deleted automatically if invalid during a redraw.

---

<span id="class_GraphEdit_method_detach_graph_element_from_frame"></span>

void **detach_graph_element_from_frame** ( element: [StringName](class_stringname.md#class_StringName) ) [🔗](class_graphedit.md#class_GraphEdit_method_detach_graph_element_from_frame)

Detaches the `element` [GraphElement](class_graphelement.md#class_GraphElement) from the [GraphFrame](class_graphframe.md#class_GraphFrame) it is currently attached to.

---

<span id="class_GraphEdit_method_disconnect_node"></span>

void **disconnect_node** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_method_disconnect_node)

Removes the connection between the `from_port` of the `from_node` [GraphNode](class_graphnode.md#class_GraphNode) and the `to_port` of the `to_node` [GraphNode](class_graphnode.md#class_GraphNode). If the connection does not exist, no connection is removed.

---

<span id="class_GraphEdit_method_force_connection_drag_end"></span>

void **force_connection_drag_end** ( ) [🔗](class_graphedit.md#class_GraphEdit_method_force_connection_drag_end)

Ends the creation of the current connection. In other words, if you are dragging a connection you can use this method to abort the process and remove the line that followed your cursor.

This is best used together with [connection_drag_started](class_graphedit.md#class_GraphEdit_signal_connection_drag_started) and [connection_drag_ended](class_graphedit.md#class_GraphEdit_signal_connection_drag_ended) to add custom behavior like node addition through shortcuts.

 **Note:** This method suppresses any other connection request signals apart from [connection_drag_ended](class_graphedit.md#class_GraphEdit_signal_connection_drag_ended).

---

<span id="class_GraphEdit_method_get_attached_nodes_of_frame"></span>

[Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] **get_attached_nodes_of_frame** ( frame: [StringName](class_stringname.md#class_StringName) ) [🔗](class_graphedit.md#class_GraphEdit_method_get_attached_nodes_of_frame)

Returns an array of node names that are attached to the [GraphFrame](class_graphframe.md#class_GraphFrame) with the given name.

---

<span id="class_GraphEdit_method_get_closest_connection_at_point"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_closest_connection_at_point** ( point: [Vector2](class_vector2.md#class_Vector2), max_distance: [float](class_float.md#class_float) = 4.0 ) *const* [🔗](class_graphedit.md#class_GraphEdit_method_get_closest_connection_at_point)

Returns the closest connection to the given point in screen space. If no connection is found within `max_distance` pixels, an empty [Dictionary](class_dictionary.md#class_Dictionary) is returned.

A connection is represented as a [Dictionary](class_dictionary.md#class_Dictionary) in the form of:

::

    {
        from_node: StringName,
        from_port: int,
        to_node: StringName,
        to_port: int,
        keep_alive: bool
    }

For example, getting a connection at a given mouse position can be achieved like this:

.. tabs::

```
```

    var connection = get_closest_connection_at_point(mouse_event.get_position())

---

<span id="class_GraphEdit_method_get_connection_count"></span>

[int](class_int.md#class_int) **get_connection_count** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_method_get_connection_count)

Returns the number of connections from `from_port` of `from_node`.

---

<span id="class_GraphEdit_method_get_connection_line"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_connection_line** ( from_node: [Vector2](class_vector2.md#class_Vector2), to_node: [Vector2](class_vector2.md#class_Vector2) ) *const* [🔗](class_graphedit.md#class_GraphEdit_method_get_connection_line)

Returns the points which would make up a connection between `from_node` and `to_node`.

---

<span id="class_GraphEdit_method_get_connection_list_from_node"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_connection_list_from_node** ( node: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_graphedit.md#class_GraphEdit_method_get_connection_list_from_node)

Returns an [Array](class_array.md#class_Array) containing a list of all connections for `node`.

A connection is represented as a [Dictionary](class_dictionary.md#class_Dictionary) in the form of:

::

    {
        from_node: StringName,
        from_port: int,
        to_node: StringName,
        to_port: int,
        keep_alive: bool
    }

 **Example:** Get all connections on a specific port:

::

    func get_connection_list_from_port(node, port):
        var connections = get_connection_list_from_node(node)
        var result = []
        for connection in connections:
            var dict = {}
            if connection["from_node"] == node and connection["from_port"] == port:
                dict["node"] = connection["to_node"]
                dict["port"] = connection["to_port"]
                dict["type"] = "left"
                result.push_back(dict)
            elif connection["to_node"] == node and connection["to_port"] == port:
                dict["node"] = connection["from_node"]
                dict["port"] = connection["from_port"]
                dict["type"] = "right"
                result.push_back(dict)
        return result

---

<span id="class_GraphEdit_method_get_connections_intersecting_with_rect"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_connections_intersecting_with_rect** ( rect: [Rect2](class_rect2.md#class_Rect2) ) *const* [🔗](class_graphedit.md#class_GraphEdit_method_get_connections_intersecting_with_rect)

Returns an [Array](class_array.md#class_Array) containing the list of connections that intersect with the given [Rect2](class_rect2.md#class_Rect2).

A connection is represented as a [Dictionary](class_dictionary.md#class_Dictionary) in the form of:

::

    {
        from_node: StringName,
        from_port: int,
        to_node: StringName,
        to_port: int,
        keep_alive: bool
    }

---

<span id="class_GraphEdit_method_get_element_frame"></span>

[GraphFrame](class_graphframe.md#class_GraphFrame) **get_element_frame** ( element: [StringName](class_stringname.md#class_StringName) ) [🔗](class_graphedit.md#class_GraphEdit_method_get_element_frame)

Returns the [GraphFrame](class_graphframe.md#class_GraphFrame) that contains the [GraphElement](class_graphelement.md#class_GraphElement) with the given name.

---

<span id="class_GraphEdit_method_get_menu_hbox"></span>

[HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) **get_menu_hbox** ( ) [🔗](class_graphedit.md#class_GraphEdit_method_get_menu_hbox)

Gets the [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) that contains the zooming and grid snap controls in the top left of the graph. You can use this method to reposition the toolbar or to add your own custom controls to it.

 **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible](class_canvasitem.md#class_CanvasItem_property_visible) property.

---

<span id="class_GraphEdit_method_is_node_connected"></span>

[bool](class_bool.md#class_bool) **is_node_connected** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_method_is_node_connected)

Returns `true` if the `from_port` of the `from_node` [GraphNode](class_graphnode.md#class_GraphNode) is connected to the `to_port` of the `to_node` [GraphNode](class_graphnode.md#class_GraphNode).

---

<span id="class_GraphEdit_method_is_valid_connection_type"></span>

[bool](class_bool.md#class_bool) **is_valid_connection_type** ( from_type: [int](class_int.md#class_int), to_type: [int](class_int.md#class_int) ) *const* [🔗](class_graphedit.md#class_GraphEdit_method_is_valid_connection_type)

Returns whether it's possible to make a connection between two different port types. The port type is defined individually for the left and the right port of each slot with the [GraphNode.set_slot()](class_graphnode.md#class_GraphNode_method_set_slot) method.

See also [add_valid_connection_type()](class_graphedit.md#class_GraphEdit_method_add_valid_connection_type) and [remove_valid_connection_type()](class_graphedit.md#class_GraphEdit_method_remove_valid_connection_type).

---

<span id="class_GraphEdit_method_remove_valid_connection_type"></span>

void **remove_valid_connection_type** ( from_type: [int](class_int.md#class_int), to_type: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_method_remove_valid_connection_type)

Disallows the connection between two different port types previously allowed by [add_valid_connection_type()](class_graphedit.md#class_GraphEdit_method_add_valid_connection_type). The port type is defined individually for the left and the right port of each slot with the [GraphNode.set_slot()](class_graphnode.md#class_GraphNode_method_set_slot) method.

See also [is_valid_connection_type()](class_graphedit.md#class_GraphEdit_method_is_valid_connection_type).

---

<span id="class_GraphEdit_method_remove_valid_left_disconnect_type"></span>

void **remove_valid_left_disconnect_type** ( type: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_method_remove_valid_left_disconnect_type)

Disallows to disconnect nodes when dragging from the left port of the [GraphNode](class_graphnode.md#class_GraphNode)'s slot if it has the specified type. Use this to disable a disconnection previously allowed with [add_valid_left_disconnect_type()](class_graphedit.md#class_GraphEdit_method_add_valid_left_disconnect_type).

---

<span id="class_GraphEdit_method_remove_valid_right_disconnect_type"></span>

void **remove_valid_right_disconnect_type** ( type: [int](class_int.md#class_int) ) [🔗](class_graphedit.md#class_GraphEdit_method_remove_valid_right_disconnect_type)

Disallows to disconnect nodes when dragging from the right port of the [GraphNode](class_graphnode.md#class_GraphNode)'s slot if it has the specified type. Use this to disable a disconnection previously allowed with [add_valid_right_disconnect_type()](class_graphedit.md#class_GraphEdit_method_add_valid_right_disconnect_type).

---

<span id="class_GraphEdit_method_set_connection_activity"></span>

void **set_connection_activity** ( from_node: [StringName](class_stringname.md#class_StringName), from_port: [int](class_int.md#class_int), to_node: [StringName](class_stringname.md#class_StringName), to_port: [int](class_int.md#class_int), amount: [float](class_float.md#class_float) ) [🔗](class_graphedit.md#class_GraphEdit_method_set_connection_activity)

Sets the coloration of the connection between `from_node`'s `from_port` and `to_node`'s `to_port` with the color provided in the [activity](class_graphedit.md#class_GraphEdit_theme_color_activity) theme property. The color is linearly interpolated between the connection color and the activity color using `amount` as weight.

---

<span id="class_GraphEdit_method_set_selected"></span>

void **set_selected** ( node: [Node](class_node.md#class_Node) ) [🔗](class_graphedit.md#class_GraphEdit_method_set_selected)

Sets the specified `node` as the one selected.

---

### Theme Property Descriptions

<span id="class_GraphEdit_theme_color_activity"></span>

[Color](class_color.md#class_Color) **activity** = `Color(1, 1, 1, 1)` [🔗](class_graphedit.md#class_GraphEdit_theme_color_activity)

Color the connection line is interpolated to based on the activity value of a connection (see [set_connection_activity()](class_graphedit.md#class_GraphEdit_method_set_connection_activity)).

---

<span id="class_GraphEdit_theme_color_connection_hover_tint_color"></span>

[Color](class_color.md#class_Color) **connection_hover_tint_color** = `Color(0, 0, 0, 0.3)` [🔗](class_graphedit.md#class_GraphEdit_theme_color_connection_hover_tint_color)

Color which is blended with the connection line when the mouse is hovering over it.

---

<span id="class_GraphEdit_theme_color_connection_rim_color"></span>

[Color](class_color.md#class_Color) **connection_rim_color** = `Color(0.1, 0.1, 0.1, 0.6)` [🔗](class_graphedit.md#class_GraphEdit_theme_color_connection_rim_color)

Color of the rim around each connection line used for making intersecting lines more distinguishable.

---

<span id="class_GraphEdit_theme_color_connection_valid_target_tint_color"></span>

[Color](class_color.md#class_Color) **connection_valid_target_tint_color** = `Color(1, 1, 1, 0.4)` [🔗](class_graphedit.md#class_GraphEdit_theme_color_connection_valid_target_tint_color)

Color which is blended with the connection line when the currently dragged connection is hovering over a valid target port.

---

<span id="class_GraphEdit_theme_color_grid_major"></span>

[Color](class_color.md#class_Color) **grid_major** = `Color(1, 1, 1, 0.2)` [🔗](class_graphedit.md#class_GraphEdit_theme_color_grid_major)

Color of major grid lines/dots.

---

<span id="class_GraphEdit_theme_color_grid_minor"></span>

[Color](class_color.md#class_Color) **grid_minor** = `Color(1, 1, 1, 0.05)` [🔗](class_graphedit.md#class_GraphEdit_theme_color_grid_minor)

Color of minor grid lines/dots.

---

<span id="class_GraphEdit_theme_color_selection_fill"></span>

[Color](class_color.md#class_Color) **selection_fill** = `Color(1, 1, 1, 0.3)` [🔗](class_graphedit.md#class_GraphEdit_theme_color_selection_fill)

The fill color of the selection rectangle.

---

<span id="class_GraphEdit_theme_color_selection_stroke"></span>

[Color](class_color.md#class_Color) **selection_stroke** = `Color(1, 1, 1, 0.8)` [🔗](class_graphedit.md#class_GraphEdit_theme_color_selection_stroke)

The outline color of the selection rectangle.

---

<span id="class_GraphEdit_theme_constant_connection_hover_thickness"></span>

[int](class_int.md#class_int) **connection_hover_thickness** = `0` [🔗](class_graphedit.md#class_GraphEdit_theme_constant_connection_hover_thickness)

Widens the line of a connection when the mouse is hovering over it by a percentage factor. A value of `0` disables the highlight. A value of `100` doubles the line width.

---

<span id="class_GraphEdit_theme_constant_port_hotzone_inner_extent"></span>

[int](class_int.md#class_int) **port_hotzone_inner_extent** = `22` [🔗](class_graphedit.md#class_GraphEdit_theme_constant_port_hotzone_inner_extent)

The horizontal range within which a port can be grabbed (inner side).

---

<span id="class_GraphEdit_theme_constant_port_hotzone_outer_extent"></span>

[int](class_int.md#class_int) **port_hotzone_outer_extent** = `26` [🔗](class_graphedit.md#class_GraphEdit_theme_constant_port_hotzone_outer_extent)

The horizontal range within which a port can be grabbed (outer side).

---

<span id="class_GraphEdit_theme_icon_grid_toggle"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **grid_toggle** [🔗](class_graphedit.md#class_GraphEdit_theme_icon_grid_toggle)

The icon for the grid toggle button.

---

<span id="class_GraphEdit_theme_icon_layout"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **layout** [🔗](class_graphedit.md#class_GraphEdit_theme_icon_layout)

The icon for the layout button for auto-arranging the graph.

---

<span id="class_GraphEdit_theme_icon_minimap_toggle"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **minimap_toggle** [🔗](class_graphedit.md#class_GraphEdit_theme_icon_minimap_toggle)

The icon for the minimap toggle button.

---

<span id="class_GraphEdit_theme_icon_snapping_toggle"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **snapping_toggle** [🔗](class_graphedit.md#class_GraphEdit_theme_icon_snapping_toggle)

The icon for the snapping toggle button.

---

<span id="class_GraphEdit_theme_icon_zoom_in"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **zoom_in** [🔗](class_graphedit.md#class_GraphEdit_theme_icon_zoom_in)

The icon for the zoom in button.

---

<span id="class_GraphEdit_theme_icon_zoom_out"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **zoom_out** [🔗](class_graphedit.md#class_GraphEdit_theme_icon_zoom_out)

The icon for the zoom out button.

---

<span id="class_GraphEdit_theme_icon_zoom_reset"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **zoom_reset** [🔗](class_graphedit.md#class_GraphEdit_theme_icon_zoom_reset)

The icon for the zoom reset button.

---

<span id="class_GraphEdit_theme_style_menu_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **menu_panel** [🔗](class_graphedit.md#class_GraphEdit_theme_style_menu_panel)

.. container:: contribute

	There is currently no description for this theme property. Please help us by contributing one!

---

<span id="class_GraphEdit_theme_style_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **panel** [🔗](class_graphedit.md#class_GraphEdit_theme_style_panel)

The background drawn under the grid.

---

<span id="class_GraphEdit_theme_style_panel_focus"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **panel_focus** [🔗](class_graphedit.md#class_GraphEdit_theme_style_panel_focus)

[StyleBox](class_stylebox.md#class_StyleBox) used when the **GraphEdit** is focused (when used with assistive apps).
