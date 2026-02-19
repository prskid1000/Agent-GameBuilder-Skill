<span id="class_RenderingServer"></span>

## RenderingServer

**Inherits:** [Object](class_object.md#class_Object)

Server for anything visible.

### Description

The rendering server is the API backend for everything visible. The whole scene system mounts on it to display. The rendering server is completely opaque: the internals are entirely implementation-specific and cannot be accessed.

The rendering server can be used to bypass the scene/[Node](class_node.md#class_Node) system entirely. This can improve performance in cases where the scene system is the bottleneck, but won't improve performance otherwise (for instance, if the GPU is already fully utilized).

Resources are created using the `*_create` functions. These functions return [RID](class_rid.md#class_RID) s which are not references to the objects themselves, but opaque *pointers* towards these objects.

All objects are drawn to a viewport. You can use the [Viewport](class_viewport.md#class_Viewport) attached to the [SceneTree](class_scenetree.md#class_SceneTree) or you can create one yourself with [viewport_create()](class_renderingserver.md#class_RenderingServer_method_viewport_create). When using a custom scenario or canvas, the scenario or canvas needs to be attached to the viewport using [viewport_set_scenario()](class_renderingserver.md#class_RenderingServer_method_viewport_set_scenario) or [viewport_attach_canvas()](class_renderingserver.md#class_RenderingServer_method_viewport_attach_canvas).

 **Scenarios:** In 3D, all visual objects must be associated with a scenario. The scenario is a visual representation of the world. If accessing the rendering server from a running game, the scenario can be accessed from the scene tree from any [Node3D](class_node3d.md#class_Node3D) node with [Node3D.get_world_3d()](class_node3d.md#class_Node3D_method_get_world_3d). Otherwise, a scenario can be created with [scenario_create()](class_renderingserver.md#class_RenderingServer_method_scenario_create).

Similarly, in 2D, a canvas is needed to draw all canvas items.

 **3D:** In 3D, all visible objects are comprised of a resource and an instance. A resource can be a mesh, a particle system, a light, or any other 3D object. In order to be visible resources must be attached to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base). The instance must also be attached to the scenario using [instance_set_scenario()](class_renderingserver.md#class_RenderingServer_method_instance_set_scenario) in order to be visible. RenderingServer methods that don't have a prefix are usually 3D-specific (but not always).

 **2D:** In 2D, all visible objects are some form of canvas item. In order to be visible, a canvas item needs to be the child of a canvas attached to a viewport, or it needs to be the child of another canvas item that is eventually attached to the canvas. 2D-specific RenderingServer methods generally start with `canvas_*`.

 **Headless mode:** Starting the engine with the `--headless` [command line argument](../tutorials/editor/command_line_tutorial.md) disables all rendering and window management functions. Most functions from **RenderingServer** will return dummy values in this case.

### Tutorials

- [Optimization using Servers](../tutorials/performance/using_servers.md)

### Properties


| [bool](class_bool.md#class_bool) | [render_loop_enabled](class_renderingserver.md#class_RenderingServer_property_render_loop_enabled) |
| --- | --- |

### Methods


| [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] | [bake_render_uv2](class_renderingserver.md#class_RenderingServer_method_bake_render_uv2) ( base: [RID](class_rid.md#class_RID), material_overrides: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], image_size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| --- | --- |
| void | [call_on_render_thread](class_renderingserver.md#class_RenderingServer_method_call_on_render_thread) ( callable: [Callable](class_callable.md#class_Callable) ) |
| [RID](class_rid.md#class_RID) | [camera_attributes_create](class_renderingserver.md#class_RenderingServer_method_camera_attributes_create) ( ) |
| void | [camera_attributes_set_auto_exposure](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_auto_exposure) ( camera_attributes: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), min_sensitivity: [float](class_float.md#class_float), max_sensitivity: [float](class_float.md#class_float), speed: [float](class_float.md#class_float), scale: [float](class_float.md#class_float) ) |
| void | [camera_attributes_set_dof_blur](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_dof_blur) ( camera_attributes: [RID](class_rid.md#class_RID), far_enable: [bool](class_bool.md#class_bool), far_distance: [float](class_float.md#class_float), far_transition: [float](class_float.md#class_float), near_enable: [bool](class_bool.md#class_bool), near_distance: [float](class_float.md#class_float), near_transition: [float](class_float.md#class_float), amount: [float](class_float.md#class_float) ) |
| void | [camera_attributes_set_dof_blur_bokeh_shape](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_dof_blur_bokeh_shape) ( shape: [DOFBokehShape](class_renderingserver.md#enum_RenderingServer_DOFBokehShape) ) |
| void | [camera_attributes_set_dof_blur_quality](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_dof_blur_quality) ( quality: [DOFBlurQuality](class_renderingserver.md#enum_RenderingServer_DOFBlurQuality), use_jitter: [bool](class_bool.md#class_bool) ) |
| void | [camera_attributes_set_exposure](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_exposure) ( camera_attributes: [RID](class_rid.md#class_RID), multiplier: [float](class_float.md#class_float), normalization: [float](class_float.md#class_float) ) |
| [RID](class_rid.md#class_RID) | [camera_create](class_renderingserver.md#class_RenderingServer_method_camera_create) ( ) |
| void | [camera_set_camera_attributes](class_renderingserver.md#class_RenderingServer_method_camera_set_camera_attributes) ( camera: [RID](class_rid.md#class_RID), effects: [RID](class_rid.md#class_RID) ) |
| void | [camera_set_compositor](class_renderingserver.md#class_RenderingServer_method_camera_set_compositor) ( camera: [RID](class_rid.md#class_RID), compositor: [RID](class_rid.md#class_RID) ) |
| void | [camera_set_cull_mask](class_renderingserver.md#class_RenderingServer_method_camera_set_cull_mask) ( camera: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) |
| void | [camera_set_environment](class_renderingserver.md#class_RenderingServer_method_camera_set_environment) ( camera: [RID](class_rid.md#class_RID), env: [RID](class_rid.md#class_RID) ) |
| void | [camera_set_frustum](class_renderingserver.md#class_RenderingServer_method_camera_set_frustum) ( camera: [RID](class_rid.md#class_RID), size: [float](class_float.md#class_float), offset: [Vector2](class_vector2.md#class_Vector2), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) |
| void | [camera_set_orthogonal](class_renderingserver.md#class_RenderingServer_method_camera_set_orthogonal) ( camera: [RID](class_rid.md#class_RID), size: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) |
| void | [camera_set_perspective](class_renderingserver.md#class_RenderingServer_method_camera_set_perspective) ( camera: [RID](class_rid.md#class_RID), fovy_degrees: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) |
| void | [camera_set_transform](class_renderingserver.md#class_RenderingServer_method_camera_set_transform) ( camera: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [camera_set_use_vertical_aspect](class_renderingserver.md#class_RenderingServer_method_camera_set_use_vertical_aspect) ( camera: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| [RID](class_rid.md#class_RID) | [canvas_create](class_renderingserver.md#class_RenderingServer_method_canvas_create) ( ) |
| void | [canvas_item_add_animation_slice](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_animation_slice) ( item: [RID](class_rid.md#class_RID), animation_length: [float](class_float.md#class_float), slice_begin: [float](class_float.md#class_float), slice_end: [float](class_float.md#class_float), offset: [float](class_float.md#class_float) = 0.0 ) |
| void | [canvas_item_add_circle](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_circle) ( item: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), radius: [float](class_float.md#class_float), color: [Color](class_color.md#class_Color), antialiased: [bool](class_bool.md#class_bool) = false ) |
| void | [canvas_item_add_clip_ignore](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_clip_ignore) ( item: [RID](class_rid.md#class_RID), ignore: [bool](class_bool.md#class_bool) ) |
| void | [canvas_item_add_ellipse](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_ellipse) ( item: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), major: [float](class_float.md#class_float), minor: [float](class_float.md#class_float), color: [Color](class_color.md#class_Color), antialiased: [bool](class_bool.md#class_bool) = false ) |
| void | [canvas_item_add_lcd_texture_rect_region](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_lcd_texture_rect_region) ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color) ) |
| void | [canvas_item_add_line](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_line) ( item: [RID](class_rid.md#class_RID), from: [Vector2](class_vector2.md#class_Vector2), to: [Vector2](class_vector2.md#class_Vector2), color: [Color](class_color.md#class_Color), width: [float](class_float.md#class_float) = -1.0, antialiased: [bool](class_bool.md#class_bool) = false ) |
| void | [canvas_item_add_mesh](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_mesh) ( item: [RID](class_rid.md#class_RID), mesh: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) = Transform2D(1, 0, 0, 1, 0, 0), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), texture: [RID](class_rid.md#class_RID) = RID() ) |
| void | [canvas_item_add_msdf_texture_rect_region](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_msdf_texture_rect_region) ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), outline_size: [int](class_int.md#class_int) = 0, px_range: [float](class_float.md#class_float) = 1.0, scale: [float](class_float.md#class_float) = 1.0 ) |
| void | [canvas_item_add_multiline](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_multiline) ( item: [RID](class_rid.md#class_RID), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), width: [float](class_float.md#class_float) = -1.0, antialiased: [bool](class_bool.md#class_bool) = false ) |
| void | [canvas_item_add_multimesh](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_multimesh) ( item: [RID](class_rid.md#class_RID), mesh: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) = RID() ) |
| void | [canvas_item_add_nine_patch](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_nine_patch) ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), source: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), topleft: [Vector2](class_vector2.md#class_Vector2), bottomright: [Vector2](class_vector2.md#class_Vector2), x_axis_mode: [NinePatchAxisMode](class_renderingserver.md#enum_RenderingServer_NinePatchAxisMode) = 0, y_axis_mode: [NinePatchAxisMode](class_renderingserver.md#enum_RenderingServer_NinePatchAxisMode) = 0, draw_center: [bool](class_bool.md#class_bool) = true, modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1) ) |
| void | [canvas_item_add_particles](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_particles) ( item: [RID](class_rid.md#class_RID), particles: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) |
| void | [canvas_item_add_polygon](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_polygon) ( item: [RID](class_rid.md#class_RID), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), uvs: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) = PackedVector2Array(), texture: [RID](class_rid.md#class_RID) = RID() ) |
| void | [canvas_item_add_polyline](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_polyline) ( item: [RID](class_rid.md#class_RID), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), width: [float](class_float.md#class_float) = -1.0, antialiased: [bool](class_bool.md#class_bool) = false ) |
| void | [canvas_item_add_primitive](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_primitive) ( item: [RID](class_rid.md#class_RID), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), uvs: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), texture: [RID](class_rid.md#class_RID) ) |
| void | [canvas_item_add_rect](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_rect) ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), color: [Color](class_color.md#class_Color), antialiased: [bool](class_bool.md#class_bool) = false ) |
| void | [canvas_item_add_set_transform](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_set_transform) ( item: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [canvas_item_add_texture_rect](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_texture_rect) ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), tile: [bool](class_bool.md#class_bool) = false, modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false ) |
| void | [canvas_item_add_texture_rect_region](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_texture_rect_region) ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false, clip_uv: [bool](class_bool.md#class_bool) = true ) |
| void | [canvas_item_add_triangle_array](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_triangle_array) ( item: [RID](class_rid.md#class_RID), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), uvs: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) = PackedVector2Array(), bones: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) = PackedInt32Array(), weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) = PackedFloat32Array(), texture: [RID](class_rid.md#class_RID) = RID(), count: [int](class_int.md#class_int) = -1 ) |
| void | [canvas_item_attach_skeleton](class_renderingserver.md#class_RenderingServer_method_canvas_item_attach_skeleton) ( item: [RID](class_rid.md#class_RID), skeleton: [RID](class_rid.md#class_RID) ) |
| void | [canvas_item_clear](class_renderingserver.md#class_RenderingServer_method_canvas_item_clear) ( item: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [canvas_item_create](class_renderingserver.md#class_RenderingServer_method_canvas_item_create) ( ) |
| [Variant](class_variant.md#class_Variant) | [canvas_item_get_instance_shader_parameter](class_renderingserver.md#class_RenderingServer_method_canvas_item_get_instance_shader_parameter) ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) const |
| [Variant](class_variant.md#class_Variant) | [canvas_item_get_instance_shader_parameter_default_value](class_renderingserver.md#class_RenderingServer_method_canvas_item_get_instance_shader_parameter_default_value) ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [canvas_item_get_instance_shader_parameter_list](class_renderingserver.md#class_RenderingServer_method_canvas_item_get_instance_shader_parameter_list) ( instance: [RID](class_rid.md#class_RID) ) const |
| void | [canvas_item_reset_physics_interpolation](class_renderingserver.md#class_RenderingServer_method_canvas_item_reset_physics_interpolation) ( item: [RID](class_rid.md#class_RID) ) |
| void | [canvas_item_set_canvas_group_mode](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_canvas_group_mode) ( item: [RID](class_rid.md#class_RID), mode: [CanvasGroupMode](class_renderingserver.md#enum_RenderingServer_CanvasGroupMode), clear_margin: [float](class_float.md#class_float) = 5.0, fit_empty: [bool](class_bool.md#class_bool) = false, fit_margin: [float](class_float.md#class_float) = 0.0, blur_mipmaps: [bool](class_bool.md#class_bool) = false ) |
| void | [canvas_item_set_clip](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_clip) ( item: [RID](class_rid.md#class_RID), clip: [bool](class_bool.md#class_bool) ) |
| void | [canvas_item_set_copy_to_backbuffer](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_copy_to_backbuffer) ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool), rect: [Rect2](class_rect2.md#class_Rect2) ) |
| void | [canvas_item_set_custom_rect](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_custom_rect) ( item: [RID](class_rid.md#class_RID), use_custom_rect: [bool](class_bool.md#class_bool), rect: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0) ) |
| void | [canvas_item_set_default_texture_filter](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_default_texture_filter) ( item: [RID](class_rid.md#class_RID), filter: [CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) ) |
| void | [canvas_item_set_default_texture_repeat](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_default_texture_repeat) ( item: [RID](class_rid.md#class_RID), repeat: [CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) ) |
| void | [canvas_item_set_distance_field_mode](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_distance_field_mode) ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [canvas_item_set_draw_behind_parent](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_draw_behind_parent) ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [canvas_item_set_draw_index](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_draw_index) ( item: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) |
| void | [canvas_item_set_instance_shader_parameter](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_instance_shader_parameter) ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |
| void | [canvas_item_set_interpolated](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_interpolated) ( item: [RID](class_rid.md#class_RID), interpolated: [bool](class_bool.md#class_bool) ) |
| void | [canvas_item_set_light_mask](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_light_mask) ( item: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [canvas_item_set_material](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_material) ( item: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) |
| void | [canvas_item_set_modulate](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_modulate) ( item: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [canvas_item_set_parent](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_parent) ( item: [RID](class_rid.md#class_RID), parent: [RID](class_rid.md#class_RID) ) |
| void | [canvas_item_set_self_modulate](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_self_modulate) ( item: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [canvas_item_set_sort_children_by_y](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_sort_children_by_y) ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [canvas_item_set_transform](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_transform) ( item: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [canvas_item_set_use_parent_material](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_use_parent_material) ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [canvas_item_set_visibility_layer](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_visibility_layer) ( item: [RID](class_rid.md#class_RID), visibility_layer: [int](class_int.md#class_int) ) |
| void | [canvas_item_set_visibility_notifier](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_visibility_notifier) ( item: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), area: [Rect2](class_rect2.md#class_Rect2), enter_callable: [Callable](class_callable.md#class_Callable), exit_callable: [Callable](class_callable.md#class_Callable) ) |
| void | [canvas_item_set_visible](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_visible) ( item: [RID](class_rid.md#class_RID), visible: [bool](class_bool.md#class_bool) ) |
| void | [canvas_item_set_z_as_relative_to_parent](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_z_as_relative_to_parent) ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [canvas_item_set_z_index](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_z_index) ( item: [RID](class_rid.md#class_RID), z_index: [int](class_int.md#class_int) ) |
| void | [canvas_item_transform_physics_interpolation](class_renderingserver.md#class_RenderingServer_method_canvas_item_transform_physics_interpolation) ( item: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [canvas_light_attach_to_canvas](class_renderingserver.md#class_RenderingServer_method_canvas_light_attach_to_canvas) ( light: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [canvas_light_create](class_renderingserver.md#class_RenderingServer_method_canvas_light_create) ( ) |
| void | [canvas_light_occluder_attach_to_canvas](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_attach_to_canvas) ( occluder: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [canvas_light_occluder_create](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_create) ( ) |
| void | [canvas_light_occluder_reset_physics_interpolation](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_reset_physics_interpolation) ( occluder: [RID](class_rid.md#class_RID) ) |
| void | [canvas_light_occluder_set_as_sdf_collision](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_as_sdf_collision) ( occluder: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [canvas_light_occluder_set_enabled](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_enabled) ( occluder: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [canvas_light_occluder_set_interpolated](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_interpolated) ( occluder: [RID](class_rid.md#class_RID), interpolated: [bool](class_bool.md#class_bool) ) |
| void | [canvas_light_occluder_set_light_mask](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_light_mask) ( occluder: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [canvas_light_occluder_set_polygon](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_polygon) ( occluder: [RID](class_rid.md#class_RID), polygon: [RID](class_rid.md#class_RID) ) |
| void | [canvas_light_occluder_set_transform](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_transform) ( occluder: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [canvas_light_occluder_transform_physics_interpolation](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_transform_physics_interpolation) ( occluder: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [canvas_light_reset_physics_interpolation](class_renderingserver.md#class_RenderingServer_method_canvas_light_reset_physics_interpolation) ( light: [RID](class_rid.md#class_RID) ) |
| void | [canvas_light_set_blend_mode](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_blend_mode) ( light: [RID](class_rid.md#class_RID), mode: [CanvasLightBlendMode](class_renderingserver.md#enum_RenderingServer_CanvasLightBlendMode) ) |
| void | [canvas_light_set_color](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_color) ( light: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [canvas_light_set_enabled](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_enabled) ( light: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [canvas_light_set_energy](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_energy) ( light: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float) ) |
| void | [canvas_light_set_height](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_height) ( light: [RID](class_rid.md#class_RID), height: [float](class_float.md#class_float) ) |
| void | [canvas_light_set_interpolated](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_interpolated) ( light: [RID](class_rid.md#class_RID), interpolated: [bool](class_bool.md#class_bool) ) |
| void | [canvas_light_set_item_cull_mask](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_item_cull_mask) ( light: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [canvas_light_set_item_shadow_cull_mask](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_item_shadow_cull_mask) ( light: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [canvas_light_set_layer_range](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_layer_range) ( light: [RID](class_rid.md#class_RID), min_layer: [int](class_int.md#class_int), max_layer: [int](class_int.md#class_int) ) |
| void | [canvas_light_set_mode](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_mode) ( light: [RID](class_rid.md#class_RID), mode: [CanvasLightMode](class_renderingserver.md#enum_RenderingServer_CanvasLightMode) ) |
| void | [canvas_light_set_shadow_color](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_shadow_color) ( light: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [canvas_light_set_shadow_enabled](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_shadow_enabled) ( light: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [canvas_light_set_shadow_filter](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_shadow_filter) ( light: [RID](class_rid.md#class_RID), filter: [CanvasLightShadowFilter](class_renderingserver.md#enum_RenderingServer_CanvasLightShadowFilter) ) |
| void | [canvas_light_set_shadow_smooth](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_shadow_smooth) ( light: [RID](class_rid.md#class_RID), smooth: [float](class_float.md#class_float) ) |
| void | [canvas_light_set_texture](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_texture) ( light: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) |
| void | [canvas_light_set_texture_offset](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_texture_offset) ( light: [RID](class_rid.md#class_RID), offset: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [canvas_light_set_texture_scale](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_texture_scale) ( light: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) |
| void | [canvas_light_set_transform](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_transform) ( light: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [canvas_light_set_z_range](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_z_range) ( light: [RID](class_rid.md#class_RID), min_z: [int](class_int.md#class_int), max_z: [int](class_int.md#class_int) ) |
| void | [canvas_light_transform_physics_interpolation](class_renderingserver.md#class_RenderingServer_method_canvas_light_transform_physics_interpolation) ( light: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| [RID](class_rid.md#class_RID) | [canvas_occluder_polygon_create](class_renderingserver.md#class_RenderingServer_method_canvas_occluder_polygon_create) ( ) |
| void | [canvas_occluder_polygon_set_cull_mode](class_renderingserver.md#class_RenderingServer_method_canvas_occluder_polygon_set_cull_mode) ( occluder_polygon: [RID](class_rid.md#class_RID), mode: [CanvasOccluderPolygonCullMode](class_renderingserver.md#enum_RenderingServer_CanvasOccluderPolygonCullMode) ) |
| void | [canvas_occluder_polygon_set_shape](class_renderingserver.md#class_RenderingServer_method_canvas_occluder_polygon_set_shape) ( occluder_polygon: [RID](class_rid.md#class_RID), shape: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), closed: [bool](class_bool.md#class_bool) ) |
| void | [canvas_set_disable_scale](class_renderingserver.md#class_RenderingServer_method_canvas_set_disable_scale) ( disable: [bool](class_bool.md#class_bool) ) |
| void | [canvas_set_item_mirroring](class_renderingserver.md#class_RenderingServer_method_canvas_set_item_mirroring) ( canvas: [RID](class_rid.md#class_RID), item: [RID](class_rid.md#class_RID), mirroring: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [canvas_set_item_repeat](class_renderingserver.md#class_RenderingServer_method_canvas_set_item_repeat) ( item: [RID](class_rid.md#class_RID), repeat_size: [Vector2](class_vector2.md#class_Vector2), repeat_times: [int](class_int.md#class_int) ) |
| void | [canvas_set_modulate](class_renderingserver.md#class_RenderingServer_method_canvas_set_modulate) ( canvas: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [canvas_set_shadow_texture_size](class_renderingserver.md#class_RenderingServer_method_canvas_set_shadow_texture_size) ( size: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [canvas_texture_create](class_renderingserver.md#class_RenderingServer_method_canvas_texture_create) ( ) |
| void | [canvas_texture_set_channel](class_renderingserver.md#class_RenderingServer_method_canvas_texture_set_channel) ( canvas_texture: [RID](class_rid.md#class_RID), channel: [CanvasTextureChannel](class_renderingserver.md#enum_RenderingServer_CanvasTextureChannel), texture: [RID](class_rid.md#class_RID) ) |
| void | [canvas_texture_set_shading_parameters](class_renderingserver.md#class_RenderingServer_method_canvas_texture_set_shading_parameters) ( canvas_texture: [RID](class_rid.md#class_RID), base_color: [Color](class_color.md#class_Color), shininess: [float](class_float.md#class_float) ) |
| void | [canvas_texture_set_texture_filter](class_renderingserver.md#class_RenderingServer_method_canvas_texture_set_texture_filter) ( canvas_texture: [RID](class_rid.md#class_RID), filter: [CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) ) |
| void | [canvas_texture_set_texture_repeat](class_renderingserver.md#class_RenderingServer_method_canvas_texture_set_texture_repeat) ( canvas_texture: [RID](class_rid.md#class_RID), repeat: [CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) ) |
| [RID](class_rid.md#class_RID) | [compositor_create](class_renderingserver.md#class_RenderingServer_method_compositor_create) ( ) |
| [RID](class_rid.md#class_RID) | [compositor_effect_create](class_renderingserver.md#class_RenderingServer_method_compositor_effect_create) ( ) |
| void | [compositor_effect_set_callback](class_renderingserver.md#class_RenderingServer_method_compositor_effect_set_callback) ( effect: [RID](class_rid.md#class_RID), callback_type: [CompositorEffectCallbackType](class_renderingserver.md#enum_RenderingServer_CompositorEffectCallbackType), callback: [Callable](class_callable.md#class_Callable) ) |
| void | [compositor_effect_set_enabled](class_renderingserver.md#class_RenderingServer_method_compositor_effect_set_enabled) ( effect: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [compositor_effect_set_flag](class_renderingserver.md#class_RenderingServer_method_compositor_effect_set_flag) ( effect: [RID](class_rid.md#class_RID), flag: [CompositorEffectFlags](class_renderingserver.md#enum_RenderingServer_CompositorEffectFlags), set: [bool](class_bool.md#class_bool) ) |
| void | [compositor_set_compositor_effects](class_renderingserver.md#class_RenderingServer_method_compositor_set_compositor_effects) ( compositor: [RID](class_rid.md#class_RID), effects: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] ) |
| [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) | [create_local_rendering_device](class_renderingserver.md#class_RenderingServer_method_create_local_rendering_device) ( ) const |
| [Rect2](class_rect2.md#class_Rect2) | [debug_canvas_item_get_rect](class_renderingserver.md#class_RenderingServer_method_debug_canvas_item_get_rect) ( item: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [decal_create](class_renderingserver.md#class_RenderingServer_method_decal_create) ( ) |
| void | [decal_set_albedo_mix](class_renderingserver.md#class_RenderingServer_method_decal_set_albedo_mix) ( decal: [RID](class_rid.md#class_RID), albedo_mix: [float](class_float.md#class_float) ) |
| void | [decal_set_cull_mask](class_renderingserver.md#class_RenderingServer_method_decal_set_cull_mask) ( decal: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [decal_set_distance_fade](class_renderingserver.md#class_RenderingServer_method_decal_set_distance_fade) ( decal: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool), begin: [float](class_float.md#class_float), length: [float](class_float.md#class_float) ) |
| void | [decal_set_emission_energy](class_renderingserver.md#class_RenderingServer_method_decal_set_emission_energy) ( decal: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float) ) |
| void | [decal_set_fade](class_renderingserver.md#class_RenderingServer_method_decal_set_fade) ( decal: [RID](class_rid.md#class_RID), above: [float](class_float.md#class_float), below: [float](class_float.md#class_float) ) |
| void | [decal_set_modulate](class_renderingserver.md#class_RenderingServer_method_decal_set_modulate) ( decal: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [decal_set_normal_fade](class_renderingserver.md#class_RenderingServer_method_decal_set_normal_fade) ( decal: [RID](class_rid.md#class_RID), fade: [float](class_float.md#class_float) ) |
| void | [decal_set_size](class_renderingserver.md#class_RenderingServer_method_decal_set_size) ( decal: [RID](class_rid.md#class_RID), size: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [decal_set_texture](class_renderingserver.md#class_RenderingServer_method_decal_set_texture) ( decal: [RID](class_rid.md#class_RID), type: [DecalTexture](class_renderingserver.md#enum_RenderingServer_DecalTexture), texture: [RID](class_rid.md#class_RID) ) |
| void | [decals_set_filter](class_renderingserver.md#class_RenderingServer_method_decals_set_filter) ( filter: [DecalFilter](class_renderingserver.md#enum_RenderingServer_DecalFilter) ) |
| [RID](class_rid.md#class_RID) | [directional_light_create](class_renderingserver.md#class_RenderingServer_method_directional_light_create) ( ) |
| void | [directional_shadow_atlas_set_size](class_renderingserver.md#class_RenderingServer_method_directional_shadow_atlas_set_size) ( size: [int](class_int.md#class_int), is_16bits: [bool](class_bool.md#class_bool) ) |
| void | [directional_soft_shadow_filter_set_quality](class_renderingserver.md#class_RenderingServer_method_directional_soft_shadow_filter_set_quality) ( quality: [ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) ) |
| [Image](class_image.md#class_Image) | [environment_bake_panorama](class_renderingserver.md#class_RenderingServer_method_environment_bake_panorama) ( environment: [RID](class_rid.md#class_RID), bake_irradiance: [bool](class_bool.md#class_bool), size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [RID](class_rid.md#class_RID) | [environment_create](class_renderingserver.md#class_RenderingServer_method_environment_create) ( ) |
| void | [environment_glow_set_use_bicubic_upscale](class_renderingserver.md#class_RenderingServer_method_environment_glow_set_use_bicubic_upscale) ( enable: [bool](class_bool.md#class_bool) ) |
| void | [environment_set_adjustment](class_renderingserver.md#class_RenderingServer_method_environment_set_adjustment) ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), brightness: [float](class_float.md#class_float), contrast: [float](class_float.md#class_float), saturation: [float](class_float.md#class_float), use_1d_color_correction: [bool](class_bool.md#class_bool), color_correction: [RID](class_rid.md#class_RID) ) |
| void | [environment_set_ambient_light](class_renderingserver.md#class_RenderingServer_method_environment_set_ambient_light) ( env: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color), ambient: [EnvironmentAmbientSource](class_renderingserver.md#enum_RenderingServer_EnvironmentAmbientSource) = 0, energy: [float](class_float.md#class_float) = 1.0, sky_contribution: [float](class_float.md#class_float) = 0.0, reflection_source: [EnvironmentReflectionSource](class_renderingserver.md#enum_RenderingServer_EnvironmentReflectionSource) = 0 ) |
| void | [environment_set_background](class_renderingserver.md#class_RenderingServer_method_environment_set_background) ( env: [RID](class_rid.md#class_RID), bg: [EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) ) |
| void | [environment_set_bg_color](class_renderingserver.md#class_RenderingServer_method_environment_set_bg_color) ( env: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [environment_set_bg_energy](class_renderingserver.md#class_RenderingServer_method_environment_set_bg_energy) ( env: [RID](class_rid.md#class_RID), multiplier: [float](class_float.md#class_float), exposure_value: [float](class_float.md#class_float) ) |
| void | [environment_set_camera_id](class_renderingserver.md#class_RenderingServer_method_environment_set_camera_id) ( env: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) |
| void | [environment_set_canvas_max_layer](class_renderingserver.md#class_RenderingServer_method_environment_set_canvas_max_layer) ( env: [RID](class_rid.md#class_RID), max_layer: [int](class_int.md#class_int) ) |
| void | [environment_set_fog](class_renderingserver.md#class_RenderingServer_method_environment_set_fog) ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), light_color: [Color](class_color.md#class_Color), light_energy: [float](class_float.md#class_float), sun_scatter: [float](class_float.md#class_float), density: [float](class_float.md#class_float), height: [float](class_float.md#class_float), height_density: [float](class_float.md#class_float), aerial_perspective: [float](class_float.md#class_float), sky_affect: [float](class_float.md#class_float), fog_mode: [EnvironmentFogMode](class_renderingserver.md#enum_RenderingServer_EnvironmentFogMode) = 0 ) |
| void | [environment_set_fog_depth](class_renderingserver.md#class_RenderingServer_method_environment_set_fog_depth) ( env: [RID](class_rid.md#class_RID), curve: [float](class_float.md#class_float), begin: [float](class_float.md#class_float), end: [float](class_float.md#class_float) ) |
| void | [environment_set_glow](class_renderingserver.md#class_RenderingServer_method_environment_set_glow) ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), levels: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), intensity: [float](class_float.md#class_float), strength: [float](class_float.md#class_float), mix: [float](class_float.md#class_float), bloom_threshold: [float](class_float.md#class_float), blend_mode: [EnvironmentGlowBlendMode](class_renderingserver.md#enum_RenderingServer_EnvironmentGlowBlendMode), hdr_bleed_threshold: [float](class_float.md#class_float), hdr_bleed_scale: [float](class_float.md#class_float), hdr_luminance_cap: [float](class_float.md#class_float), glow_map_strength: [float](class_float.md#class_float), glow_map: [RID](class_rid.md#class_RID) ) |
| void | [environment_set_sdfgi](class_renderingserver.md#class_RenderingServer_method_environment_set_sdfgi) ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), cascades: [int](class_int.md#class_int), min_cell_size: [float](class_float.md#class_float), y_scale: [EnvironmentSDFGIYScale](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIYScale), use_occlusion: [bool](class_bool.md#class_bool), bounce_feedback: [float](class_float.md#class_float), read_sky: [bool](class_bool.md#class_bool), energy: [float](class_float.md#class_float), normal_bias: [float](class_float.md#class_float), probe_bias: [float](class_float.md#class_float) ) |
| void | [environment_set_sdfgi_frames_to_converge](class_renderingserver.md#class_RenderingServer_method_environment_set_sdfgi_frames_to_converge) ( frames: [EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) ) |
| void | [environment_set_sdfgi_frames_to_update_light](class_renderingserver.md#class_RenderingServer_method_environment_set_sdfgi_frames_to_update_light) ( frames: [EnvironmentSDFGIFramesToUpdateLight](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight) ) |
| void | [environment_set_sdfgi_ray_count](class_renderingserver.md#class_RenderingServer_method_environment_set_sdfgi_ray_count) ( ray_count: [EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) ) |
| void | [environment_set_sky](class_renderingserver.md#class_RenderingServer_method_environment_set_sky) ( env: [RID](class_rid.md#class_RID), sky: [RID](class_rid.md#class_RID) ) |
| void | [environment_set_sky_custom_fov](class_renderingserver.md#class_RenderingServer_method_environment_set_sky_custom_fov) ( env: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) |
| void | [environment_set_sky_orientation](class_renderingserver.md#class_RenderingServer_method_environment_set_sky_orientation) ( env: [RID](class_rid.md#class_RID), orientation: [Basis](class_basis.md#class_Basis) ) |
| void | [environment_set_ssao](class_renderingserver.md#class_RenderingServer_method_environment_set_ssao) ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), radius: [float](class_float.md#class_float), intensity: [float](class_float.md#class_float), power: [float](class_float.md#class_float), detail: [float](class_float.md#class_float), horizon: [float](class_float.md#class_float), sharpness: [float](class_float.md#class_float), light_affect: [float](class_float.md#class_float), ao_channel_affect: [float](class_float.md#class_float) ) |
| void | [environment_set_ssao_quality](class_renderingserver.md#class_RenderingServer_method_environment_set_ssao_quality) ( quality: [EnvironmentSSAOQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSAOQuality), half_size: [bool](class_bool.md#class_bool), adaptive_target: [float](class_float.md#class_float), blur_passes: [int](class_int.md#class_int), fadeout_from: [float](class_float.md#class_float), fadeout_to: [float](class_float.md#class_float) ) |
| void | [environment_set_ssil_quality](class_renderingserver.md#class_RenderingServer_method_environment_set_ssil_quality) ( quality: [EnvironmentSSILQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSILQuality), half_size: [bool](class_bool.md#class_bool), adaptive_target: [float](class_float.md#class_float), blur_passes: [int](class_int.md#class_int), fadeout_from: [float](class_float.md#class_float), fadeout_to: [float](class_float.md#class_float) ) |
| void | [environment_set_ssr](class_renderingserver.md#class_RenderingServer_method_environment_set_ssr) ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), max_steps: [int](class_int.md#class_int), fade_in: [float](class_float.md#class_float), fade_out: [float](class_float.md#class_float), depth_tolerance: [float](class_float.md#class_float) ) |
| void | [environment_set_ssr_half_size](class_renderingserver.md#class_RenderingServer_method_environment_set_ssr_half_size) ( half_size: [bool](class_bool.md#class_bool) ) |
| void | [environment_set_ssr_roughness_quality](class_renderingserver.md#class_RenderingServer_method_environment_set_ssr_roughness_quality) ( quality: [EnvironmentSSRRoughnessQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSRRoughnessQuality) ) |
| void | [environment_set_tonemap](class_renderingserver.md#class_RenderingServer_method_environment_set_tonemap) ( env: [RID](class_rid.md#class_RID), tone_mapper: [EnvironmentToneMapper](class_renderingserver.md#enum_RenderingServer_EnvironmentToneMapper), exposure: [float](class_float.md#class_float), white: [float](class_float.md#class_float) ) |
| void | [environment_set_tonemap_agx_contrast](class_renderingserver.md#class_RenderingServer_method_environment_set_tonemap_agx_contrast) ( env: [RID](class_rid.md#class_RID), agx_contrast: [float](class_float.md#class_float) ) |
| void | [environment_set_volumetric_fog](class_renderingserver.md#class_RenderingServer_method_environment_set_volumetric_fog) ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), density: [float](class_float.md#class_float), albedo: [Color](class_color.md#class_Color), emission: [Color](class_color.md#class_Color), emission_energy: [float](class_float.md#class_float), anisotropy: [float](class_float.md#class_float), length: [float](class_float.md#class_float), p_detail_spread: [float](class_float.md#class_float), gi_inject: [float](class_float.md#class_float), temporal_reprojection: [bool](class_bool.md#class_bool), temporal_reprojection_amount: [float](class_float.md#class_float), ambient_inject: [float](class_float.md#class_float), sky_affect: [float](class_float.md#class_float) ) |
| void | [environment_set_volumetric_fog_filter_active](class_renderingserver.md#class_RenderingServer_method_environment_set_volumetric_fog_filter_active) ( active: [bool](class_bool.md#class_bool) ) |
| void | [environment_set_volumetric_fog_volume_size](class_renderingserver.md#class_RenderingServer_method_environment_set_volumetric_fog_volume_size) ( size: [int](class_int.md#class_int), depth: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [fog_volume_create](class_renderingserver.md#class_RenderingServer_method_fog_volume_create) ( ) |
| void | [fog_volume_set_material](class_renderingserver.md#class_RenderingServer_method_fog_volume_set_material) ( fog_volume: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) |
| void | [fog_volume_set_shape](class_renderingserver.md#class_RenderingServer_method_fog_volume_set_shape) ( fog_volume: [RID](class_rid.md#class_RID), shape: [FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) ) |
| void | [fog_volume_set_size](class_renderingserver.md#class_RenderingServer_method_fog_volume_set_size) ( fog_volume: [RID](class_rid.md#class_RID), size: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [force_draw](class_renderingserver.md#class_RenderingServer_method_force_draw) ( swap_buffers: [bool](class_bool.md#class_bool) = true, frame_step: [float](class_float.md#class_float) = 0.0 ) |
| void | [force_sync](class_renderingserver.md#class_RenderingServer_method_force_sync) ( ) |
| void | [free_rid](class_renderingserver.md#class_RenderingServer_method_free_rid) ( rid: [RID](class_rid.md#class_RID) ) |
| [String](class_string.md#class_String) | [get_current_rendering_driver_name](class_renderingserver.md#class_RenderingServer_method_get_current_rendering_driver_name) ( ) const |
| [String](class_string.md#class_String) | [get_current_rendering_method](class_renderingserver.md#class_RenderingServer_method_get_current_rendering_method) ( ) const |
| [Color](class_color.md#class_Color) | [get_default_clear_color](class_renderingserver.md#class_RenderingServer_method_get_default_clear_color) ( ) |
| [float](class_float.md#class_float) | [get_frame_setup_time_cpu](class_renderingserver.md#class_RenderingServer_method_get_frame_setup_time_cpu) ( ) const |
| [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) | [get_rendering_device](class_renderingserver.md#class_RenderingServer_method_get_rendering_device) ( ) const |
| [int](class_int.md#class_int) | [get_rendering_info](class_renderingserver.md#class_RenderingServer_method_get_rendering_info) ( info: [RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) ) |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [get_shader_parameter_list](class_renderingserver.md#class_RenderingServer_method_get_shader_parameter_list) ( shader: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [get_test_cube](class_renderingserver.md#class_RenderingServer_method_get_test_cube) ( ) |
| [RID](class_rid.md#class_RID) | [get_test_texture](class_renderingserver.md#class_RenderingServer_method_get_test_texture) ( ) |
| [String](class_string.md#class_String) | [get_video_adapter_api_version](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_api_version) ( ) const |
| [String](class_string.md#class_String) | [get_video_adapter_name](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_name) ( ) const |
| [DeviceType](class_renderingdevice.md#enum_RenderingDevice_DeviceType) | [get_video_adapter_type](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_type) ( ) const |
| [String](class_string.md#class_String) | [get_video_adapter_vendor](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_vendor) ( ) const |
| [RID](class_rid.md#class_RID) | [get_white_texture](class_renderingserver.md#class_RenderingServer_method_get_white_texture) ( ) |
| void | [gi_set_use_half_resolution](class_renderingserver.md#class_RenderingServer_method_gi_set_use_half_resolution) ( half_resolution: [bool](class_bool.md#class_bool) ) |
| void | [global_shader_parameter_add](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_add) ( name: [StringName](class_stringname.md#class_StringName), type: [GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType), default_value: [Variant](class_variant.md#class_Variant) ) |
| [Variant](class_variant.md#class_Variant) | [global_shader_parameter_get](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_get) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] | [global_shader_parameter_get_list](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_get_list) ( ) const |
| [GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) | [global_shader_parameter_get_type](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_get_type) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| void | [global_shader_parameter_remove](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_remove) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [global_shader_parameter_set](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_set) ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |
| void | [global_shader_parameter_set_override](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_set_override) ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |
| [bool](class_bool.md#class_bool) | [has_changed](class_renderingserver.md#class_RenderingServer_method_has_changed) ( ) const |
| [bool](class_bool.md#class_bool) | [has_feature](class_renderingserver.md#class_RenderingServer_method_has_feature) ( feature: [Features](class_renderingserver.md#enum_RenderingServer_Features) ) const |
| [bool](class_bool.md#class_bool) | [has_os_feature](class_renderingserver.md#class_RenderingServer_method_has_os_feature) ( feature: [String](class_string.md#class_String) ) const |
| void | [instance_attach_object_instance_id](class_renderingserver.md#class_RenderingServer_method_instance_attach_object_instance_id) ( instance: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) |
| void | [instance_attach_skeleton](class_renderingserver.md#class_RenderingServer_method_instance_attach_skeleton) ( instance: [RID](class_rid.md#class_RID), skeleton: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [instance_create](class_renderingserver.md#class_RenderingServer_method_instance_create) ( ) |
| [RID](class_rid.md#class_RID) | [instance_create2](class_renderingserver.md#class_RenderingServer_method_instance_create2) ( base: [RID](class_rid.md#class_RID), scenario: [RID](class_rid.md#class_RID) ) |
| [Variant](class_variant.md#class_Variant) | [instance_geometry_get_shader_parameter](class_renderingserver.md#class_RenderingServer_method_instance_geometry_get_shader_parameter) ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) const |
| [Variant](class_variant.md#class_Variant) | [instance_geometry_get_shader_parameter_default_value](class_renderingserver.md#class_RenderingServer_method_instance_geometry_get_shader_parameter_default_value) ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] | [instance_geometry_get_shader_parameter_list](class_renderingserver.md#class_RenderingServer_method_instance_geometry_get_shader_parameter_list) ( instance: [RID](class_rid.md#class_RID) ) const |
| void | [instance_geometry_set_cast_shadows_setting](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_cast_shadows_setting) ( instance: [RID](class_rid.md#class_RID), shadow_casting_setting: [ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) ) |
| void | [instance_geometry_set_flag](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_flag) ( instance: [RID](class_rid.md#class_RID), flag: [InstanceFlags](class_renderingserver.md#enum_RenderingServer_InstanceFlags), enabled: [bool](class_bool.md#class_bool) ) |
| void | [instance_geometry_set_lightmap](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_lightmap) ( instance: [RID](class_rid.md#class_RID), lightmap: [RID](class_rid.md#class_RID), lightmap_uv_scale: [Rect2](class_rect2.md#class_Rect2), lightmap_slice: [int](class_int.md#class_int) ) |
| void | [instance_geometry_set_lod_bias](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_lod_bias) ( instance: [RID](class_rid.md#class_RID), lod_bias: [float](class_float.md#class_float) ) |
| void | [instance_geometry_set_material_overlay](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_material_overlay) ( instance: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) |
| void | [instance_geometry_set_material_override](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_material_override) ( instance: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) |
| void | [instance_geometry_set_shader_parameter](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_shader_parameter) ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |
| void | [instance_geometry_set_transparency](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_transparency) ( instance: [RID](class_rid.md#class_RID), transparency: [float](class_float.md#class_float) ) |
| void | [instance_geometry_set_visibility_range](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_visibility_range) ( instance: [RID](class_rid.md#class_RID), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float), min_margin: [float](class_float.md#class_float), max_margin: [float](class_float.md#class_float), fade_mode: [VisibilityRangeFadeMode](class_renderingserver.md#enum_RenderingServer_VisibilityRangeFadeMode) ) |
| void | [instance_set_base](class_renderingserver.md#class_RenderingServer_method_instance_set_base) ( instance: [RID](class_rid.md#class_RID), base: [RID](class_rid.md#class_RID) ) |
| void | [instance_set_blend_shape_weight](class_renderingserver.md#class_RenderingServer_method_instance_set_blend_shape_weight) ( instance: [RID](class_rid.md#class_RID), shape: [int](class_int.md#class_int), weight: [float](class_float.md#class_float) ) |
| void | [instance_set_custom_aabb](class_renderingserver.md#class_RenderingServer_method_instance_set_custom_aabb) ( instance: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) |
| void | [instance_set_extra_visibility_margin](class_renderingserver.md#class_RenderingServer_method_instance_set_extra_visibility_margin) ( instance: [RID](class_rid.md#class_RID), margin: [float](class_float.md#class_float) ) |
| void | [instance_set_ignore_culling](class_renderingserver.md#class_RenderingServer_method_instance_set_ignore_culling) ( instance: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [instance_set_layer_mask](class_renderingserver.md#class_RenderingServer_method_instance_set_layer_mask) ( instance: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [instance_set_pivot_data](class_renderingserver.md#class_RenderingServer_method_instance_set_pivot_data) ( instance: [RID](class_rid.md#class_RID), sorting_offset: [float](class_float.md#class_float), use_aabb_center: [bool](class_bool.md#class_bool) ) |
| void | [instance_set_scenario](class_renderingserver.md#class_RenderingServer_method_instance_set_scenario) ( instance: [RID](class_rid.md#class_RID), scenario: [RID](class_rid.md#class_RID) ) |
| void | [instance_set_surface_override_material](class_renderingserver.md#class_RenderingServer_method_instance_set_surface_override_material) ( instance: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), material: [RID](class_rid.md#class_RID) ) |
| void | [instance_set_transform](class_renderingserver.md#class_RenderingServer_method_instance_set_transform) ( instance: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [instance_set_visibility_parent](class_renderingserver.md#class_RenderingServer_method_instance_set_visibility_parent) ( instance: [RID](class_rid.md#class_RID), parent: [RID](class_rid.md#class_RID) ) |
| void | [instance_set_visible](class_renderingserver.md#class_RenderingServer_method_instance_set_visible) ( instance: [RID](class_rid.md#class_RID), visible: [bool](class_bool.md#class_bool) ) |
| void | [instance_teleport](class_renderingserver.md#class_RenderingServer_method_instance_teleport) ( instance: [RID](class_rid.md#class_RID) ) |
| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [instances_cull_aabb](class_renderingserver.md#class_RenderingServer_method_instances_cull_aabb) ( aabb: [AABB](class_aabb.md#class_AABB), scenario: [RID](class_rid.md#class_RID) = RID() ) const |
| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [instances_cull_convex](class_renderingserver.md#class_RenderingServer_method_instances_cull_convex) ( convex: [Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\], scenario: [RID](class_rid.md#class_RID) = RID() ) const |
| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [instances_cull_ray](class_renderingserver.md#class_RenderingServer_method_instances_cull_ray) ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), scenario: [RID](class_rid.md#class_RID) = RID() ) const |
| [bool](class_bool.md#class_bool) | [is_on_render_thread](class_renderingserver.md#class_RenderingServer_method_is_on_render_thread) ( ) |
| void | [light_directional_set_blend_splits](class_renderingserver.md#class_RenderingServer_method_light_directional_set_blend_splits) ( light: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [light_directional_set_shadow_mode](class_renderingserver.md#class_RenderingServer_method_light_directional_set_shadow_mode) ( light: [RID](class_rid.md#class_RID), mode: [LightDirectionalShadowMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalShadowMode) ) |
| void | [light_directional_set_sky_mode](class_renderingserver.md#class_RenderingServer_method_light_directional_set_sky_mode) ( light: [RID](class_rid.md#class_RID), mode: [LightDirectionalSkyMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalSkyMode) ) |
| void | [light_omni_set_shadow_mode](class_renderingserver.md#class_RenderingServer_method_light_omni_set_shadow_mode) ( light: [RID](class_rid.md#class_RID), mode: [LightOmniShadowMode](class_renderingserver.md#enum_RenderingServer_LightOmniShadowMode) ) |
| void | [light_projectors_set_filter](class_renderingserver.md#class_RenderingServer_method_light_projectors_set_filter) ( filter: [LightProjectorFilter](class_renderingserver.md#enum_RenderingServer_LightProjectorFilter) ) |
| void | [light_set_bake_mode](class_renderingserver.md#class_RenderingServer_method_light_set_bake_mode) ( light: [RID](class_rid.md#class_RID), bake_mode: [LightBakeMode](class_renderingserver.md#enum_RenderingServer_LightBakeMode) ) |
| void | [light_set_color](class_renderingserver.md#class_RenderingServer_method_light_set_color) ( light: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [light_set_cull_mask](class_renderingserver.md#class_RenderingServer_method_light_set_cull_mask) ( light: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [light_set_distance_fade](class_renderingserver.md#class_RenderingServer_method_light_set_distance_fade) ( decal: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool), begin: [float](class_float.md#class_float), shadow: [float](class_float.md#class_float), length: [float](class_float.md#class_float) ) |
| void | [light_set_max_sdfgi_cascade](class_renderingserver.md#class_RenderingServer_method_light_set_max_sdfgi_cascade) ( light: [RID](class_rid.md#class_RID), cascade: [int](class_int.md#class_int) ) |
| void | [light_set_negative](class_renderingserver.md#class_RenderingServer_method_light_set_negative) ( light: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [light_set_param](class_renderingserver.md#class_RenderingServer_method_light_set_param) ( light: [RID](class_rid.md#class_RID), param: [LightParam](class_renderingserver.md#enum_RenderingServer_LightParam), value: [float](class_float.md#class_float) ) |
| void | [light_set_projector](class_renderingserver.md#class_RenderingServer_method_light_set_projector) ( light: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) |
| void | [light_set_reverse_cull_face_mode](class_renderingserver.md#class_RenderingServer_method_light_set_reverse_cull_face_mode) ( light: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [light_set_shadow](class_renderingserver.md#class_RenderingServer_method_light_set_shadow) ( light: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [light_set_shadow_caster_mask](class_renderingserver.md#class_RenderingServer_method_light_set_shadow_caster_mask) ( light: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [lightmap_create](class_renderingserver.md#class_RenderingServer_method_lightmap_create) ( ) |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [lightmap_get_probe_capture_bsp_tree](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_bsp_tree) ( lightmap: [RID](class_rid.md#class_RID) ) const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [lightmap_get_probe_capture_points](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_points) ( lightmap: [RID](class_rid.md#class_RID) ) const |
| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [lightmap_get_probe_capture_sh](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_sh) ( lightmap: [RID](class_rid.md#class_RID) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [lightmap_get_probe_capture_tetrahedra](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_tetrahedra) ( lightmap: [RID](class_rid.md#class_RID) ) const |
| void | [lightmap_set_baked_exposure_normalization](class_renderingserver.md#class_RenderingServer_method_lightmap_set_baked_exposure_normalization) ( lightmap: [RID](class_rid.md#class_RID), baked_exposure: [float](class_float.md#class_float) ) |
| void | [lightmap_set_probe_bounds](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_bounds) ( lightmap: [RID](class_rid.md#class_RID), bounds: [AABB](class_aabb.md#class_AABB) ) |
| void | [lightmap_set_probe_capture_data](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_capture_data) ( lightmap: [RID](class_rid.md#class_RID), points: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), point_sh: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), tetrahedra: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), bsp_tree: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| void | [lightmap_set_probe_capture_update_speed](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_capture_update_speed) ( speed: [float](class_float.md#class_float) ) |
| void | [lightmap_set_probe_interior](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_interior) ( lightmap: [RID](class_rid.md#class_RID), interior: [bool](class_bool.md#class_bool) ) |
| void | [lightmap_set_textures](class_renderingserver.md#class_RenderingServer_method_lightmap_set_textures) ( lightmap: [RID](class_rid.md#class_RID), light: [RID](class_rid.md#class_RID), uses_sh: [bool](class_bool.md#class_bool) ) |
| void | [lightmaps_set_bicubic_filter](class_renderingserver.md#class_RenderingServer_method_lightmaps_set_bicubic_filter) ( enable: [bool](class_bool.md#class_bool) ) |
| [RID](class_rid.md#class_RID) | [make_sphere_mesh](class_renderingserver.md#class_RenderingServer_method_make_sphere_mesh) ( latitudes: [int](class_int.md#class_int), longitudes: [int](class_int.md#class_int), radius: [float](class_float.md#class_float) ) |
| [RID](class_rid.md#class_RID) | [material_create](class_renderingserver.md#class_RenderingServer_method_material_create) ( ) |
| [Variant](class_variant.md#class_Variant) | [material_get_param](class_renderingserver.md#class_RenderingServer_method_material_get_param) ( material: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) const |
| void | [material_set_next_pass](class_renderingserver.md#class_RenderingServer_method_material_set_next_pass) ( material: [RID](class_rid.md#class_RID), next_material: [RID](class_rid.md#class_RID) ) |
| void | [material_set_param](class_renderingserver.md#class_RenderingServer_method_material_set_param) ( material: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) |
| void | [material_set_render_priority](class_renderingserver.md#class_RenderingServer_method_material_set_render_priority) ( material: [RID](class_rid.md#class_RID), priority: [int](class_int.md#class_int) ) |
| void | [material_set_shader](class_renderingserver.md#class_RenderingServer_method_material_set_shader) ( shader_material: [RID](class_rid.md#class_RID), shader: [RID](class_rid.md#class_RID) ) |
| void | [material_set_use_debanding](class_renderingserver.md#class_RenderingServer_method_material_set_use_debanding) ( enable: [bool](class_bool.md#class_bool) ) |
| void | [mesh_add_surface](class_renderingserver.md#class_RenderingServer_method_mesh_add_surface) ( mesh: [RID](class_rid.md#class_RID), surface: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| void | [mesh_add_surface_from_arrays](class_renderingserver.md#class_RenderingServer_method_mesh_add_surface_from_arrays) ( mesh: [RID](class_rid.md#class_RID), primitive: [PrimitiveType](class_renderingserver.md#enum_RenderingServer_PrimitiveType), arrays: [Array](class_array.md#class_Array), blend_shapes: [Array](class_array.md#class_Array) = [], lods: [Dictionary](class_dictionary.md#class_Dictionary) = {}, compress_format: | bitfield | \[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\] = 0 ) |
| void | [mesh_clear](class_renderingserver.md#class_RenderingServer_method_mesh_clear) ( mesh: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [mesh_create](class_renderingserver.md#class_RenderingServer_method_mesh_create) ( ) |
| [RID](class_rid.md#class_RID) | [mesh_create_from_surfaces](class_renderingserver.md#class_RenderingServer_method_mesh_create_from_surfaces) ( surfaces: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\], blend_shape_count: [int](class_int.md#class_int) = 0 ) |
| [int](class_int.md#class_int) | [mesh_get_blend_shape_count](class_renderingserver.md#class_RenderingServer_method_mesh_get_blend_shape_count) ( mesh: [RID](class_rid.md#class_RID) ) const |
| [BlendShapeMode](class_renderingserver.md#enum_RenderingServer_BlendShapeMode) | [mesh_get_blend_shape_mode](class_renderingserver.md#class_RenderingServer_method_mesh_get_blend_shape_mode) ( mesh: [RID](class_rid.md#class_RID) ) const |
| [AABB](class_aabb.md#class_AABB) | [mesh_get_custom_aabb](class_renderingserver.md#class_RenderingServer_method_mesh_get_custom_aabb) ( mesh: [RID](class_rid.md#class_RID) ) const |
| [Dictionary](class_dictionary.md#class_Dictionary) | [mesh_get_surface](class_renderingserver.md#class_RenderingServer_method_mesh_get_surface) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [mesh_get_surface_count](class_renderingserver.md#class_RenderingServer_method_mesh_get_surface_count) ( mesh: [RID](class_rid.md#class_RID) ) const |
| void | [mesh_set_blend_shape_mode](class_renderingserver.md#class_RenderingServer_method_mesh_set_blend_shape_mode) ( mesh: [RID](class_rid.md#class_RID), mode: [BlendShapeMode](class_renderingserver.md#enum_RenderingServer_BlendShapeMode) ) |
| void | [mesh_set_custom_aabb](class_renderingserver.md#class_RenderingServer_method_mesh_set_custom_aabb) ( mesh: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) |
| void | [mesh_set_shadow_mesh](class_renderingserver.md#class_RenderingServer_method_mesh_set_shadow_mesh) ( mesh: [RID](class_rid.md#class_RID), shadow_mesh: [RID](class_rid.md#class_RID) ) |
| [Array](class_array.md#class_Array) | [mesh_surface_get_arrays](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_arrays) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array)\[[Array](class_array.md#class_Array)\] | [mesh_surface_get_blend_shape_arrays](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_blend_shape_arrays) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [mesh_surface_get_format_attribute_stride](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_attribute_stride) ( format: | bitfield | \[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) | const |
| [int](class_int.md#class_int) | [mesh_surface_get_format_index_stride](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_index_stride) ( format: | bitfield | \[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) | const |
| [int](class_int.md#class_int) | [mesh_surface_get_format_normal_tangent_stride](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_normal_tangent_stride) ( format: | bitfield | \[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) | const |
| [int](class_int.md#class_int) | [mesh_surface_get_format_offset](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_offset) ( format: | bitfield | \[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int), array_index: [int](class_int.md#class_int) ) | const |
| [int](class_int.md#class_int) | [mesh_surface_get_format_skin_stride](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_skin_stride) ( format: | bitfield | \[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) | const |
| [int](class_int.md#class_int) | [mesh_surface_get_format_vertex_stride](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_vertex_stride) ( format: | bitfield | \[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) | const |
| [RID](class_rid.md#class_RID) | [mesh_surface_get_material](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_material) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) const |
| void | [mesh_surface_remove](class_renderingserver.md#class_RenderingServer_method_mesh_surface_remove) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) |
| void | [mesh_surface_set_material](class_renderingserver.md#class_RenderingServer_method_mesh_surface_set_material) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), material: [RID](class_rid.md#class_RID) ) |
| void | [mesh_surface_update_attribute_region](class_renderingserver.md#class_RenderingServer_method_mesh_surface_update_attribute_region) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [mesh_surface_update_index_region](class_renderingserver.md#class_RenderingServer_method_mesh_surface_update_index_region) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [mesh_surface_update_skin_region](class_renderingserver.md#class_RenderingServer_method_mesh_surface_update_skin_region) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [mesh_surface_update_vertex_region](class_renderingserver.md#class_RenderingServer_method_mesh_surface_update_vertex_region) ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [multimesh_allocate_data](class_renderingserver.md#class_RenderingServer_method_multimesh_allocate_data) ( multimesh: [RID](class_rid.md#class_RID), instances: [int](class_int.md#class_int), transform_format: [MultimeshTransformFormat](class_renderingserver.md#enum_RenderingServer_MultimeshTransformFormat), color_format: [bool](class_bool.md#class_bool) = false, custom_data_format: [bool](class_bool.md#class_bool) = false, use_indirect: [bool](class_bool.md#class_bool) = false ) |
| [RID](class_rid.md#class_RID) | [multimesh_create](class_renderingserver.md#class_RenderingServer_method_multimesh_create) ( ) |
| [AABB](class_aabb.md#class_AABB) | [multimesh_get_aabb](class_renderingserver.md#class_RenderingServer_method_multimesh_get_aabb) ( multimesh: [RID](class_rid.md#class_RID) ) const |
| [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) | [multimesh_get_buffer](class_renderingserver.md#class_RenderingServer_method_multimesh_get_buffer) ( multimesh: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [multimesh_get_buffer_rd_rid](class_renderingserver.md#class_RenderingServer_method_multimesh_get_buffer_rd_rid) ( multimesh: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [multimesh_get_command_buffer_rd_rid](class_renderingserver.md#class_RenderingServer_method_multimesh_get_command_buffer_rd_rid) ( multimesh: [RID](class_rid.md#class_RID) ) const |
| [AABB](class_aabb.md#class_AABB) | [multimesh_get_custom_aabb](class_renderingserver.md#class_RenderingServer_method_multimesh_get_custom_aabb) ( multimesh: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [multimesh_get_instance_count](class_renderingserver.md#class_RenderingServer_method_multimesh_get_instance_count) ( multimesh: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [multimesh_get_mesh](class_renderingserver.md#class_RenderingServer_method_multimesh_get_mesh) ( multimesh: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [multimesh_get_visible_instances](class_renderingserver.md#class_RenderingServer_method_multimesh_get_visible_instances) ( multimesh: [RID](class_rid.md#class_RID) ) const |
| [Color](class_color.md#class_Color) | [multimesh_instance_get_color](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_get_color) ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [Color](class_color.md#class_Color) | [multimesh_instance_get_custom_data](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_get_custom_data) ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [multimesh_instance_get_transform](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_get_transform) ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [multimesh_instance_get_transform_2d](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_get_transform_2d) ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) const |
| void | [multimesh_instance_reset_physics_interpolation](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_reset_physics_interpolation) ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) |
| void | [multimesh_instance_set_color](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_set_color) ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [multimesh_instance_set_custom_data](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_set_custom_data) ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), custom_data: [Color](class_color.md#class_Color) ) |
| void | [multimesh_instance_set_transform](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_set_transform) ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [multimesh_instance_set_transform_2d](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_set_transform_2d) ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [multimesh_instances_reset_physics_interpolation](class_renderingserver.md#class_RenderingServer_method_multimesh_instances_reset_physics_interpolation) ( multimesh: [RID](class_rid.md#class_RID) ) |
| void | [multimesh_set_buffer](class_renderingserver.md#class_RenderingServer_method_multimesh_set_buffer) ( multimesh: [RID](class_rid.md#class_RID), buffer: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |
| void | [multimesh_set_buffer_interpolated](class_renderingserver.md#class_RenderingServer_method_multimesh_set_buffer_interpolated) ( multimesh: [RID](class_rid.md#class_RID), buffer: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), buffer_previous: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) |
| void | [multimesh_set_custom_aabb](class_renderingserver.md#class_RenderingServer_method_multimesh_set_custom_aabb) ( multimesh: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) |
| void | [multimesh_set_mesh](class_renderingserver.md#class_RenderingServer_method_multimesh_set_mesh) ( multimesh: [RID](class_rid.md#class_RID), mesh: [RID](class_rid.md#class_RID) ) |
| void | [multimesh_set_physics_interpolated](class_renderingserver.md#class_RenderingServer_method_multimesh_set_physics_interpolated) ( multimesh: [RID](class_rid.md#class_RID), interpolated: [bool](class_bool.md#class_bool) ) |
| void | [multimesh_set_physics_interpolation_quality](class_renderingserver.md#class_RenderingServer_method_multimesh_set_physics_interpolation_quality) ( multimesh: [RID](class_rid.md#class_RID), quality: [MultimeshPhysicsInterpolationQuality](class_renderingserver.md#enum_RenderingServer_MultimeshPhysicsInterpolationQuality) ) |
| void | [multimesh_set_visible_instances](class_renderingserver.md#class_RenderingServer_method_multimesh_set_visible_instances) ( multimesh: [RID](class_rid.md#class_RID), visible: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [occluder_create](class_renderingserver.md#class_RenderingServer_method_occluder_create) ( ) |
| void | [occluder_set_mesh](class_renderingserver.md#class_RenderingServer_method_occluder_set_mesh) ( occluder: [RID](class_rid.md#class_RID), vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| [RID](class_rid.md#class_RID) | [omni_light_create](class_renderingserver.md#class_RenderingServer_method_omni_light_create) ( ) |
| [RID](class_rid.md#class_RID) | [particles_collision_create](class_renderingserver.md#class_RenderingServer_method_particles_collision_create) ( ) |
| void | [particles_collision_height_field_update](class_renderingserver.md#class_RenderingServer_method_particles_collision_height_field_update) ( particles_collision: [RID](class_rid.md#class_RID) ) |
| void | [particles_collision_set_attractor_attenuation](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_attractor_attenuation) ( particles_collision: [RID](class_rid.md#class_RID), curve: [float](class_float.md#class_float) ) |
| void | [particles_collision_set_attractor_directionality](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_attractor_directionality) ( particles_collision: [RID](class_rid.md#class_RID), amount: [float](class_float.md#class_float) ) |
| void | [particles_collision_set_attractor_strength](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_attractor_strength) ( particles_collision: [RID](class_rid.md#class_RID), strength: [float](class_float.md#class_float) ) |
| void | [particles_collision_set_box_extents](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_box_extents) ( particles_collision: [RID](class_rid.md#class_RID), extents: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [particles_collision_set_collision_type](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_collision_type) ( particles_collision: [RID](class_rid.md#class_RID), type: [ParticlesCollisionType](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType) ) |
| void | [particles_collision_set_cull_mask](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_cull_mask) ( particles_collision: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [particles_collision_set_field_texture](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_field_texture) ( particles_collision: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) |
| void | [particles_collision_set_height_field_mask](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_height_field_mask) ( particles_collision: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) |
| void | [particles_collision_set_height_field_resolution](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_height_field_resolution) ( particles_collision: [RID](class_rid.md#class_RID), resolution: [ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) ) |
| void | [particles_collision_set_sphere_radius](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_sphere_radius) ( particles_collision: [RID](class_rid.md#class_RID), radius: [float](class_float.md#class_float) ) |
| [RID](class_rid.md#class_RID) | [particles_create](class_renderingserver.md#class_RenderingServer_method_particles_create) ( ) |
| void | [particles_emit](class_renderingserver.md#class_RenderingServer_method_particles_emit) ( particles: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), velocity: [Vector3](class_vector3.md#class_Vector3), color: [Color](class_color.md#class_Color), custom: [Color](class_color.md#class_Color), emit_flags: [int](class_int.md#class_int) ) |
| [AABB](class_aabb.md#class_AABB) | [particles_get_current_aabb](class_renderingserver.md#class_RenderingServer_method_particles_get_current_aabb) ( particles: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [particles_get_emitting](class_renderingserver.md#class_RenderingServer_method_particles_get_emitting) ( particles: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [particles_is_inactive](class_renderingserver.md#class_RenderingServer_method_particles_is_inactive) ( particles: [RID](class_rid.md#class_RID) ) |
| void | [particles_request_process](class_renderingserver.md#class_RenderingServer_method_particles_request_process) ( particles: [RID](class_rid.md#class_RID) ) |
| void | [particles_request_process_time](class_renderingserver.md#class_RenderingServer_method_particles_request_process_time) ( particles: [RID](class_rid.md#class_RID), time: [float](class_float.md#class_float) ) |
| void | [particles_restart](class_renderingserver.md#class_RenderingServer_method_particles_restart) ( particles: [RID](class_rid.md#class_RID) ) |
| void | [particles_set_amount](class_renderingserver.md#class_RenderingServer_method_particles_set_amount) ( particles: [RID](class_rid.md#class_RID), amount: [int](class_int.md#class_int) ) |
| void | [particles_set_amount_ratio](class_renderingserver.md#class_RenderingServer_method_particles_set_amount_ratio) ( particles: [RID](class_rid.md#class_RID), ratio: [float](class_float.md#class_float) ) |
| void | [particles_set_collision_base_size](class_renderingserver.md#class_RenderingServer_method_particles_set_collision_base_size) ( particles: [RID](class_rid.md#class_RID), size: [float](class_float.md#class_float) ) |
| void | [particles_set_custom_aabb](class_renderingserver.md#class_RenderingServer_method_particles_set_custom_aabb) ( particles: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) |
| void | [particles_set_draw_order](class_renderingserver.md#class_RenderingServer_method_particles_set_draw_order) ( particles: [RID](class_rid.md#class_RID), order: [ParticlesDrawOrder](class_renderingserver.md#enum_RenderingServer_ParticlesDrawOrder) ) |
| void | [particles_set_draw_pass_mesh](class_renderingserver.md#class_RenderingServer_method_particles_set_draw_pass_mesh) ( particles: [RID](class_rid.md#class_RID), pass: [int](class_int.md#class_int), mesh: [RID](class_rid.md#class_RID) ) |
| void | [particles_set_draw_passes](class_renderingserver.md#class_RenderingServer_method_particles_set_draw_passes) ( particles: [RID](class_rid.md#class_RID), count: [int](class_int.md#class_int) ) |
| void | [particles_set_emission_transform](class_renderingserver.md#class_RenderingServer_method_particles_set_emission_transform) ( particles: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [particles_set_emitter_velocity](class_renderingserver.md#class_RenderingServer_method_particles_set_emitter_velocity) ( particles: [RID](class_rid.md#class_RID), velocity: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [particles_set_emitting](class_renderingserver.md#class_RenderingServer_method_particles_set_emitting) ( particles: [RID](class_rid.md#class_RID), emitting: [bool](class_bool.md#class_bool) ) |
| void | [particles_set_explosiveness_ratio](class_renderingserver.md#class_RenderingServer_method_particles_set_explosiveness_ratio) ( particles: [RID](class_rid.md#class_RID), ratio: [float](class_float.md#class_float) ) |
| void | [particles_set_fixed_fps](class_renderingserver.md#class_RenderingServer_method_particles_set_fixed_fps) ( particles: [RID](class_rid.md#class_RID), fps: [int](class_int.md#class_int) ) |
| void | [particles_set_fractional_delta](class_renderingserver.md#class_RenderingServer_method_particles_set_fractional_delta) ( particles: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [particles_set_interp_to_end](class_renderingserver.md#class_RenderingServer_method_particles_set_interp_to_end) ( particles: [RID](class_rid.md#class_RID), factor: [float](class_float.md#class_float) ) |
| void | [particles_set_interpolate](class_renderingserver.md#class_RenderingServer_method_particles_set_interpolate) ( particles: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [particles_set_lifetime](class_renderingserver.md#class_RenderingServer_method_particles_set_lifetime) ( particles: [RID](class_rid.md#class_RID), lifetime: [float](class_float.md#class_float) ) |
| void | [particles_set_mode](class_renderingserver.md#class_RenderingServer_method_particles_set_mode) ( particles: [RID](class_rid.md#class_RID), mode: [ParticlesMode](class_renderingserver.md#enum_RenderingServer_ParticlesMode) ) |
| void | [particles_set_one_shot](class_renderingserver.md#class_RenderingServer_method_particles_set_one_shot) ( particles: [RID](class_rid.md#class_RID), one_shot: [bool](class_bool.md#class_bool) ) |
| void | [particles_set_pre_process_time](class_renderingserver.md#class_RenderingServer_method_particles_set_pre_process_time) ( particles: [RID](class_rid.md#class_RID), time: [float](class_float.md#class_float) ) |
| void | [particles_set_process_material](class_renderingserver.md#class_RenderingServer_method_particles_set_process_material) ( particles: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) |
| void | [particles_set_randomness_ratio](class_renderingserver.md#class_RenderingServer_method_particles_set_randomness_ratio) ( particles: [RID](class_rid.md#class_RID), ratio: [float](class_float.md#class_float) ) |
| void | [particles_set_speed_scale](class_renderingserver.md#class_RenderingServer_method_particles_set_speed_scale) ( particles: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) |
| void | [particles_set_subemitter](class_renderingserver.md#class_RenderingServer_method_particles_set_subemitter) ( particles: [RID](class_rid.md#class_RID), subemitter_particles: [RID](class_rid.md#class_RID) ) |
| void | [particles_set_trail_bind_poses](class_renderingserver.md#class_RenderingServer_method_particles_set_trail_bind_poses) ( particles: [RID](class_rid.md#class_RID), bind_poses: [Array](class_array.md#class_Array)\[[Transform3D](class_transform3d.md#class_Transform3D)\] ) |
| void | [particles_set_trails](class_renderingserver.md#class_RenderingServer_method_particles_set_trails) ( particles: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), length_sec: [float](class_float.md#class_float) ) |
| void | [particles_set_transform_align](class_renderingserver.md#class_RenderingServer_method_particles_set_transform_align) ( particles: [RID](class_rid.md#class_RID), align: [ParticlesTransformAlign](class_renderingserver.md#enum_RenderingServer_ParticlesTransformAlign) ) |
| void | [particles_set_use_local_coordinates](class_renderingserver.md#class_RenderingServer_method_particles_set_use_local_coordinates) ( particles: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [positional_soft_shadow_filter_set_quality](class_renderingserver.md#class_RenderingServer_method_positional_soft_shadow_filter_set_quality) ( quality: [ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) ) |
| [RID](class_rid.md#class_RID) | [reflection_probe_create](class_renderingserver.md#class_RenderingServer_method_reflection_probe_create) ( ) |
| void | [reflection_probe_set_ambient_color](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_ambient_color) ( probe: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) |
| void | [reflection_probe_set_ambient_energy](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_ambient_energy) ( probe: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float) ) |
| void | [reflection_probe_set_ambient_mode](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_ambient_mode) ( probe: [RID](class_rid.md#class_RID), mode: [ReflectionProbeAmbientMode](class_renderingserver.md#enum_RenderingServer_ReflectionProbeAmbientMode) ) |
| void | [reflection_probe_set_as_interior](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_as_interior) ( probe: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [reflection_probe_set_blend_distance](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_blend_distance) ( probe: [RID](class_rid.md#class_RID), blend_distance: [float](class_float.md#class_float) ) |
| void | [reflection_probe_set_cull_mask](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_cull_mask) ( probe: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) |
| void | [reflection_probe_set_enable_box_projection](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_enable_box_projection) ( probe: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [reflection_probe_set_enable_shadows](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_enable_shadows) ( probe: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [reflection_probe_set_intensity](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_intensity) ( probe: [RID](class_rid.md#class_RID), intensity: [float](class_float.md#class_float) ) |
| void | [reflection_probe_set_max_distance](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_max_distance) ( probe: [RID](class_rid.md#class_RID), distance: [float](class_float.md#class_float) ) |
| void | [reflection_probe_set_mesh_lod_threshold](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_mesh_lod_threshold) ( probe: [RID](class_rid.md#class_RID), pixels: [float](class_float.md#class_float) ) |
| void | [reflection_probe_set_origin_offset](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_origin_offset) ( probe: [RID](class_rid.md#class_RID), offset: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [reflection_probe_set_reflection_mask](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_reflection_mask) ( probe: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) |
| void | [reflection_probe_set_resolution](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_resolution) ( probe: [RID](class_rid.md#class_RID), resolution: [int](class_int.md#class_int) ) |
| void | [reflection_probe_set_size](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_size) ( probe: [RID](class_rid.md#class_RID), size: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [reflection_probe_set_update_mode](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_update_mode) ( probe: [RID](class_rid.md#class_RID), mode: [ReflectionProbeUpdateMode](class_renderingserver.md#enum_RenderingServer_ReflectionProbeUpdateMode) ) |
| void | [request_frame_drawn_callback](class_renderingserver.md#class_RenderingServer_method_request_frame_drawn_callback) ( callable: [Callable](class_callable.md#class_Callable) ) |
| [RID](class_rid.md#class_RID) | [scenario_create](class_renderingserver.md#class_RenderingServer_method_scenario_create) ( ) |
| void | [scenario_set_camera_attributes](class_renderingserver.md#class_RenderingServer_method_scenario_set_camera_attributes) ( scenario: [RID](class_rid.md#class_RID), effects: [RID](class_rid.md#class_RID) ) |
| void | [scenario_set_compositor](class_renderingserver.md#class_RenderingServer_method_scenario_set_compositor) ( scenario: [RID](class_rid.md#class_RID), compositor: [RID](class_rid.md#class_RID) ) |
| void | [scenario_set_environment](class_renderingserver.md#class_RenderingServer_method_scenario_set_environment) ( scenario: [RID](class_rid.md#class_RID), environment: [RID](class_rid.md#class_RID) ) |
| void | [scenario_set_fallback_environment](class_renderingserver.md#class_RenderingServer_method_scenario_set_fallback_environment) ( scenario: [RID](class_rid.md#class_RID), environment: [RID](class_rid.md#class_RID) ) |
| void | [screen_space_roughness_limiter_set_active](class_renderingserver.md#class_RenderingServer_method_screen_space_roughness_limiter_set_active) ( enable: [bool](class_bool.md#class_bool), amount: [float](class_float.md#class_float), limit: [float](class_float.md#class_float) ) |
| void | [set_boot_image](class_renderingserver.md#class_RenderingServer_method_set_boot_image) ( image: [Image](class_image.md#class_Image), color: [Color](class_color.md#class_Color), scale: [bool](class_bool.md#class_bool), use_filter: [bool](class_bool.md#class_bool) = true ) |
| void | [set_boot_image_with_stretch](class_renderingserver.md#class_RenderingServer_method_set_boot_image_with_stretch) ( image: [Image](class_image.md#class_Image), color: [Color](class_color.md#class_Color), stretch_mode: [SplashStretchMode](class_renderingserver.md#enum_RenderingServer_SplashStretchMode), use_filter: [bool](class_bool.md#class_bool) = true ) |
| void | [set_debug_generate_wireframes](class_renderingserver.md#class_RenderingServer_method_set_debug_generate_wireframes) ( generate: [bool](class_bool.md#class_bool) ) |
| void | [set_default_clear_color](class_renderingserver.md#class_RenderingServer_method_set_default_clear_color) ( color: [Color](class_color.md#class_Color) ) |
| [RID](class_rid.md#class_RID) | [shader_create](class_renderingserver.md#class_RenderingServer_method_shader_create) ( ) |
| [String](class_string.md#class_String) | [shader_get_code](class_renderingserver.md#class_RenderingServer_method_shader_get_code) ( shader: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [shader_get_default_texture_parameter](class_renderingserver.md#class_RenderingServer_method_shader_get_default_texture_parameter) ( shader: [RID](class_rid.md#class_RID), name: [StringName](class_stringname.md#class_StringName), index: [int](class_int.md#class_int) = 0 ) const |
| [Variant](class_variant.md#class_Variant) | [shader_get_parameter_default](class_renderingserver.md#class_RenderingServer_method_shader_get_parameter_default) ( shader: [RID](class_rid.md#class_RID), name: [StringName](class_stringname.md#class_StringName) ) const |
| void | [shader_set_code](class_renderingserver.md#class_RenderingServer_method_shader_set_code) ( shader: [RID](class_rid.md#class_RID), code: [String](class_string.md#class_String) ) |
| void | [shader_set_default_texture_parameter](class_renderingserver.md#class_RenderingServer_method_shader_set_default_texture_parameter) ( shader: [RID](class_rid.md#class_RID), name: [StringName](class_stringname.md#class_StringName), texture: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) = 0 ) |
| void | [shader_set_path_hint](class_renderingserver.md#class_RenderingServer_method_shader_set_path_hint) ( shader: [RID](class_rid.md#class_RID), path: [String](class_string.md#class_String) ) |
| void | [skeleton_allocate_data](class_renderingserver.md#class_RenderingServer_method_skeleton_allocate_data) ( skeleton: [RID](class_rid.md#class_RID), bones: [int](class_int.md#class_int), is_2d_skeleton: [bool](class_bool.md#class_bool) = false ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [skeleton_bone_get_transform](class_renderingserver.md#class_RenderingServer_method_skeleton_bone_get_transform) ( skeleton: [RID](class_rid.md#class_RID), bone: [int](class_int.md#class_int) ) const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [skeleton_bone_get_transform_2d](class_renderingserver.md#class_RenderingServer_method_skeleton_bone_get_transform_2d) ( skeleton: [RID](class_rid.md#class_RID), bone: [int](class_int.md#class_int) ) const |
| void | [skeleton_bone_set_transform](class_renderingserver.md#class_RenderingServer_method_skeleton_bone_set_transform) ( skeleton: [RID](class_rid.md#class_RID), bone: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [skeleton_bone_set_transform_2d](class_renderingserver.md#class_RenderingServer_method_skeleton_bone_set_transform_2d) ( skeleton: [RID](class_rid.md#class_RID), bone: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| [RID](class_rid.md#class_RID) | [skeleton_create](class_renderingserver.md#class_RenderingServer_method_skeleton_create) ( ) |
| [int](class_int.md#class_int) | [skeleton_get_bone_count](class_renderingserver.md#class_RenderingServer_method_skeleton_get_bone_count) ( skeleton: [RID](class_rid.md#class_RID) ) const |
| void | [skeleton_set_base_transform_2d](class_renderingserver.md#class_RenderingServer_method_skeleton_set_base_transform_2d) ( skeleton: [RID](class_rid.md#class_RID), base_transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| [Image](class_image.md#class_Image) | [sky_bake_panorama](class_renderingserver.md#class_RenderingServer_method_sky_bake_panorama) ( sky: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float), bake_irradiance: [bool](class_bool.md#class_bool), size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| [RID](class_rid.md#class_RID) | [sky_create](class_renderingserver.md#class_RenderingServer_method_sky_create) ( ) |
| void | [sky_set_material](class_renderingserver.md#class_RenderingServer_method_sky_set_material) ( sky: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) |
| void | [sky_set_mode](class_renderingserver.md#class_RenderingServer_method_sky_set_mode) ( sky: [RID](class_rid.md#class_RID), mode: [SkyMode](class_renderingserver.md#enum_RenderingServer_SkyMode) ) |
| void | [sky_set_radiance_size](class_renderingserver.md#class_RenderingServer_method_sky_set_radiance_size) ( sky: [RID](class_rid.md#class_RID), radiance_size: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [spot_light_create](class_renderingserver.md#class_RenderingServer_method_spot_light_create) ( ) |
| void | [sub_surface_scattering_set_quality](class_renderingserver.md#class_RenderingServer_method_sub_surface_scattering_set_quality) ( quality: [SubSurfaceScatteringQuality](class_renderingserver.md#enum_RenderingServer_SubSurfaceScatteringQuality) ) |
| void | [sub_surface_scattering_set_scale](class_renderingserver.md#class_RenderingServer_method_sub_surface_scattering_set_scale) ( scale: [float](class_float.md#class_float), depth_scale: [float](class_float.md#class_float) ) |
| [RID](class_rid.md#class_RID) | [texture_2d_create](class_renderingserver.md#class_RenderingServer_method_texture_2d_create) ( image: [Image](class_image.md#class_Image) ) |
| [Image](class_image.md#class_Image) | [texture_2d_get](class_renderingserver.md#class_RenderingServer_method_texture_2d_get) ( texture: [RID](class_rid.md#class_RID) ) const |
| [Image](class_image.md#class_Image) | [texture_2d_layer_get](class_renderingserver.md#class_RenderingServer_method_texture_2d_layer_get) ( texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) const |
| [RID](class_rid.md#class_RID) | [texture_2d_layered_create](class_renderingserver.md#class_RenderingServer_method_texture_2d_layered_create) ( layers: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\], layered_type: [TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) ) |
| [RID](class_rid.md#class_RID) | [texture_2d_layered_placeholder_create](class_renderingserver.md#class_RenderingServer_method_texture_2d_layered_placeholder_create) ( layered_type: [TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) ) |
| [RID](class_rid.md#class_RID) | [texture_2d_placeholder_create](class_renderingserver.md#class_RenderingServer_method_texture_2d_placeholder_create) ( ) |
| void | [texture_2d_update](class_renderingserver.md#class_RenderingServer_method_texture_2d_update) ( texture: [RID](class_rid.md#class_RID), image: [Image](class_image.md#class_Image), layer: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [texture_3d_create](class_renderingserver.md#class_RenderingServer_method_texture_3d_create) ( format: [Format](class_image.md#enum_Image_Format), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), mipmaps: [bool](class_bool.md#class_bool), data: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] ) |
| [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] | [texture_3d_get](class_renderingserver.md#class_RenderingServer_method_texture_3d_get) ( texture: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [texture_3d_placeholder_create](class_renderingserver.md#class_RenderingServer_method_texture_3d_placeholder_create) ( ) |
| void | [texture_3d_update](class_renderingserver.md#class_RenderingServer_method_texture_3d_update) ( texture: [RID](class_rid.md#class_RID), data: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] ) |
| [RID](class_rid.md#class_RID) | [texture_create_from_native_handle](class_renderingserver.md#class_RenderingServer_method_texture_create_from_native_handle) ( type: [TextureType](class_renderingserver.md#enum_RenderingServer_TextureType), format: [Format](class_image.md#enum_Image_Format), native_handle: [int](class_int.md#class_int), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), layers: [int](class_int.md#class_int) = 1, layered_type: [TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) = 0 ) |
| void | [texture_drawable_blit_rect](class_renderingserver.md#class_RenderingServer_method_texture_drawable_blit_rect) ( textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], rect: [Rect2i](class_rect2i.md#class_Rect2i), material: [RID](class_rid.md#class_RID), modulate: [Color](class_color.md#class_Color), source_textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], to_mipmap: [int](class_int.md#class_int) = 0 ) |
| [RID](class_rid.md#class_RID) | [texture_drawable_create](class_renderingserver.md#class_RenderingServer_method_texture_drawable_create) ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), format: [TextureDrawableFormat](class_renderingserver.md#enum_RenderingServer_TextureDrawableFormat), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), with_mipmaps: [bool](class_bool.md#class_bool) = false ) |
| void | [texture_drawable_generate_mipmaps](class_renderingserver.md#class_RenderingServer_method_texture_drawable_generate_mipmaps) ( texture: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [texture_drawable_get_default_material](class_renderingserver.md#class_RenderingServer_method_texture_drawable_get_default_material) ( ) const |
| [Format](class_image.md#enum_Image_Format) | [texture_get_format](class_renderingserver.md#class_RenderingServer_method_texture_get_format) ( texture: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [texture_get_native_handle](class_renderingserver.md#class_RenderingServer_method_texture_get_native_handle) ( texture: [RID](class_rid.md#class_RID), srgb: [bool](class_bool.md#class_bool) = false ) const |
| [String](class_string.md#class_String) | [texture_get_path](class_renderingserver.md#class_RenderingServer_method_texture_get_path) ( texture: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [texture_get_rd_texture](class_renderingserver.md#class_RenderingServer_method_texture_get_rd_texture) ( texture: [RID](class_rid.md#class_RID), srgb: [bool](class_bool.md#class_bool) = false ) const |
| [RID](class_rid.md#class_RID) | [texture_proxy_create](class_renderingserver.md#class_RenderingServer_method_texture_proxy_create) ( base: [RID](class_rid.md#class_RID) ) |
| void | [texture_proxy_update](class_renderingserver.md#class_RenderingServer_method_texture_proxy_update) ( texture: [RID](class_rid.md#class_RID), proxy_to: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [texture_rd_create](class_renderingserver.md#class_RenderingServer_method_texture_rd_create) ( rd_texture: [RID](class_rid.md#class_RID), layer_type: [TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) = 0 ) |
| void | [texture_replace](class_renderingserver.md#class_RenderingServer_method_texture_replace) ( texture: [RID](class_rid.md#class_RID), by_texture: [RID](class_rid.md#class_RID) ) |
| void | [texture_set_force_redraw_if_visible](class_renderingserver.md#class_RenderingServer_method_texture_set_force_redraw_if_visible) ( texture: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [texture_set_path](class_renderingserver.md#class_RenderingServer_method_texture_set_path) ( texture: [RID](class_rid.md#class_RID), path: [String](class_string.md#class_String) ) |
| void | [texture_set_size_override](class_renderingserver.md#class_RenderingServer_method_texture_set_size_override) ( texture: [RID](class_rid.md#class_RID), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) |
| void | [viewport_attach_camera](class_renderingserver.md#class_RenderingServer_method_viewport_attach_camera) ( viewport: [RID](class_rid.md#class_RID), camera: [RID](class_rid.md#class_RID) ) |
| void | [viewport_attach_canvas](class_renderingserver.md#class_RenderingServer_method_viewport_attach_canvas) ( viewport: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID) ) |
| void | [viewport_attach_to_screen](class_renderingserver.md#class_RenderingServer_method_viewport_attach_to_screen) ( viewport: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), screen: [int](class_int.md#class_int) = 0 ) |
| [RID](class_rid.md#class_RID) | [viewport_create](class_renderingserver.md#class_RenderingServer_method_viewport_create) ( ) |
| [float](class_float.md#class_float) | [viewport_get_measured_render_time_cpu](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_cpu) ( viewport: [RID](class_rid.md#class_RID) ) const |
| [float](class_float.md#class_float) | [viewport_get_measured_render_time_gpu](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_gpu) ( viewport: [RID](class_rid.md#class_RID) ) const |
| [int](class_int.md#class_int) | [viewport_get_render_info](class_renderingserver.md#class_RenderingServer_method_viewport_get_render_info) ( viewport: [RID](class_rid.md#class_RID), type: [ViewportRenderInfoType](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfoType), info: [ViewportRenderInfo](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfo) ) |
| [RID](class_rid.md#class_RID) | [viewport_get_render_target](class_renderingserver.md#class_RenderingServer_method_viewport_get_render_target) ( viewport: [RID](class_rid.md#class_RID) ) const |
| [RID](class_rid.md#class_RID) | [viewport_get_texture](class_renderingserver.md#class_RenderingServer_method_viewport_get_texture) ( viewport: [RID](class_rid.md#class_RID) ) const |
| [ViewportUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode) | [viewport_get_update_mode](class_renderingserver.md#class_RenderingServer_method_viewport_get_update_mode) ( viewport: [RID](class_rid.md#class_RID) ) const |
| void | [viewport_remove_canvas](class_renderingserver.md#class_RenderingServer_method_viewport_remove_canvas) ( viewport: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID) ) |
| void | [viewport_set_active](class_renderingserver.md#class_RenderingServer_method_viewport_set_active) ( viewport: [RID](class_rid.md#class_RID), active: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_anisotropic_filtering_level](class_renderingserver.md#class_RenderingServer_method_viewport_set_anisotropic_filtering_level) ( viewport: [RID](class_rid.md#class_RID), anisotropic_filtering_level: [ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) ) |
| void | [viewport_set_canvas_cull_mask](class_renderingserver.md#class_RenderingServer_method_viewport_set_canvas_cull_mask) ( viewport: [RID](class_rid.md#class_RID), canvas_cull_mask: [int](class_int.md#class_int) ) |
| void | [viewport_set_canvas_stacking](class_renderingserver.md#class_RenderingServer_method_viewport_set_canvas_stacking) ( viewport: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int), sublayer: [int](class_int.md#class_int) ) |
| void | [viewport_set_canvas_transform](class_renderingserver.md#class_RenderingServer_method_viewport_set_canvas_transform) ( viewport: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), offset: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [viewport_set_clear_mode](class_renderingserver.md#class_RenderingServer_method_viewport_set_clear_mode) ( viewport: [RID](class_rid.md#class_RID), clear_mode: [ViewportClearMode](class_renderingserver.md#enum_RenderingServer_ViewportClearMode) ) |
| void | [viewport_set_debug_draw](class_renderingserver.md#class_RenderingServer_method_viewport_set_debug_draw) ( viewport: [RID](class_rid.md#class_RID), draw: [ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) ) |
| void | [viewport_set_default_canvas_item_texture_filter](class_renderingserver.md#class_RenderingServer_method_viewport_set_default_canvas_item_texture_filter) ( viewport: [RID](class_rid.md#class_RID), filter: [CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) ) |
| void | [viewport_set_default_canvas_item_texture_repeat](class_renderingserver.md#class_RenderingServer_method_viewport_set_default_canvas_item_texture_repeat) ( viewport: [RID](class_rid.md#class_RID), repeat: [CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) ) |
| void | [viewport_set_disable_2d](class_renderingserver.md#class_RenderingServer_method_viewport_set_disable_2d) ( viewport: [RID](class_rid.md#class_RID), disable: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_disable_3d](class_renderingserver.md#class_RenderingServer_method_viewport_set_disable_3d) ( viewport: [RID](class_rid.md#class_RID), disable: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_environment_mode](class_renderingserver.md#class_RenderingServer_method_viewport_set_environment_mode) ( viewport: [RID](class_rid.md#class_RID), mode: [ViewportEnvironmentMode](class_renderingserver.md#enum_RenderingServer_ViewportEnvironmentMode) ) |
| void | [viewport_set_fsr_sharpness](class_renderingserver.md#class_RenderingServer_method_viewport_set_fsr_sharpness) ( viewport: [RID](class_rid.md#class_RID), sharpness: [float](class_float.md#class_float) ) |
| void | [viewport_set_global_canvas_transform](class_renderingserver.md#class_RenderingServer_method_viewport_set_global_canvas_transform) ( viewport: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) |
| void | [viewport_set_measure_render_time](class_renderingserver.md#class_RenderingServer_method_viewport_set_measure_render_time) ( viewport: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_msaa_2d](class_renderingserver.md#class_RenderingServer_method_viewport_set_msaa_2d) ( viewport: [RID](class_rid.md#class_RID), msaa: [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) ) |
| void | [viewport_set_msaa_3d](class_renderingserver.md#class_RenderingServer_method_viewport_set_msaa_3d) ( viewport: [RID](class_rid.md#class_RID), msaa: [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) ) |
| void | [viewport_set_occlusion_culling_build_quality](class_renderingserver.md#class_RenderingServer_method_viewport_set_occlusion_culling_build_quality) ( quality: [ViewportOcclusionCullingBuildQuality](class_renderingserver.md#enum_RenderingServer_ViewportOcclusionCullingBuildQuality) ) |
| void | [viewport_set_occlusion_rays_per_thread](class_renderingserver.md#class_RenderingServer_method_viewport_set_occlusion_rays_per_thread) ( rays_per_thread: [int](class_int.md#class_int) ) |
| void | [viewport_set_parent_viewport](class_renderingserver.md#class_RenderingServer_method_viewport_set_parent_viewport) ( viewport: [RID](class_rid.md#class_RID), parent_viewport: [RID](class_rid.md#class_RID) ) |
| void | [viewport_set_positional_shadow_atlas_quadrant_subdivision](class_renderingserver.md#class_RenderingServer_method_viewport_set_positional_shadow_atlas_quadrant_subdivision) ( viewport: [RID](class_rid.md#class_RID), quadrant: [int](class_int.md#class_int), subdivision: [int](class_int.md#class_int) ) |
| void | [viewport_set_positional_shadow_atlas_size](class_renderingserver.md#class_RenderingServer_method_viewport_set_positional_shadow_atlas_size) ( viewport: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), use_16_bits: [bool](class_bool.md#class_bool) = false ) |
| void | [viewport_set_render_direct_to_screen](class_renderingserver.md#class_RenderingServer_method_viewport_set_render_direct_to_screen) ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_scaling_3d_mode](class_renderingserver.md#class_RenderingServer_method_viewport_set_scaling_3d_mode) ( viewport: [RID](class_rid.md#class_RID), scaling_3d_mode: [ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) ) |
| void | [viewport_set_scaling_3d_scale](class_renderingserver.md#class_RenderingServer_method_viewport_set_scaling_3d_scale) ( viewport: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) |
| void | [viewport_set_scenario](class_renderingserver.md#class_RenderingServer_method_viewport_set_scenario) ( viewport: [RID](class_rid.md#class_RID), scenario: [RID](class_rid.md#class_RID) ) |
| void | [viewport_set_screen_space_aa](class_renderingserver.md#class_RenderingServer_method_viewport_set_screen_space_aa) ( viewport: [RID](class_rid.md#class_RID), mode: [ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) ) |
| void | [viewport_set_sdf_oversize_and_scale](class_renderingserver.md#class_RenderingServer_method_viewport_set_sdf_oversize_and_scale) ( viewport: [RID](class_rid.md#class_RID), oversize: [ViewportSDFOversize](class_renderingserver.md#enum_RenderingServer_ViewportSDFOversize), scale: [ViewportSDFScale](class_renderingserver.md#enum_RenderingServer_ViewportSDFScale) ) |
| void | [viewport_set_size](class_renderingserver.md#class_RenderingServer_method_viewport_set_size) ( viewport: [RID](class_rid.md#class_RID), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) |
| void | [viewport_set_snap_2d_transforms_to_pixel](class_renderingserver.md#class_RenderingServer_method_viewport_set_snap_2d_transforms_to_pixel) ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_snap_2d_vertices_to_pixel](class_renderingserver.md#class_RenderingServer_method_viewport_set_snap_2d_vertices_to_pixel) ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_texture_mipmap_bias](class_renderingserver.md#class_RenderingServer_method_viewport_set_texture_mipmap_bias) ( viewport: [RID](class_rid.md#class_RID), mipmap_bias: [float](class_float.md#class_float) ) |
| void | [viewport_set_transparent_background](class_renderingserver.md#class_RenderingServer_method_viewport_set_transparent_background) ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_update_mode](class_renderingserver.md#class_RenderingServer_method_viewport_set_update_mode) ( viewport: [RID](class_rid.md#class_RID), update_mode: [ViewportUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode) ) |
| void | [viewport_set_use_debanding](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_debanding) ( viewport: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_use_hdr_2d](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_hdr_2d) ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_use_occlusion_culling](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_occlusion_culling) ( viewport: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_use_taa](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_taa) ( viewport: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_use_xr](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_xr) ( viewport: [RID](class_rid.md#class_RID), use_xr: [bool](class_bool.md#class_bool) ) |
| void | [viewport_set_vrs_mode](class_renderingserver.md#class_RenderingServer_method_viewport_set_vrs_mode) ( viewport: [RID](class_rid.md#class_RID), mode: [ViewportVRSMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSMode) ) |
| void | [viewport_set_vrs_texture](class_renderingserver.md#class_RenderingServer_method_viewport_set_vrs_texture) ( viewport: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) |
| void | [viewport_set_vrs_update_mode](class_renderingserver.md#class_RenderingServer_method_viewport_set_vrs_update_mode) ( viewport: [RID](class_rid.md#class_RID), mode: [ViewportVRSUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSUpdateMode) ) |
| [RID](class_rid.md#class_RID) | [visibility_notifier_create](class_renderingserver.md#class_RenderingServer_method_visibility_notifier_create) ( ) |
| void | [visibility_notifier_set_aabb](class_renderingserver.md#class_RenderingServer_method_visibility_notifier_set_aabb) ( notifier: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) |
| void | [visibility_notifier_set_callbacks](class_renderingserver.md#class_RenderingServer_method_visibility_notifier_set_callbacks) ( notifier: [RID](class_rid.md#class_RID), enter_callable: [Callable](class_callable.md#class_Callable), exit_callable: [Callable](class_callable.md#class_Callable) ) |
| void | [voxel_gi_allocate_data](class_renderingserver.md#class_RenderingServer_method_voxel_gi_allocate_data) ( voxel_gi: [RID](class_rid.md#class_RID), to_cell_xform: [Transform3D](class_transform3d.md#class_Transform3D), aabb: [AABB](class_aabb.md#class_AABB), octree_size: [Vector3i](class_vector3i.md#class_Vector3i), octree_cells: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), data_cells: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), distance_field: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), level_counts: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) |
| [RID](class_rid.md#class_RID) | [voxel_gi_create](class_renderingserver.md#class_RenderingServer_method_voxel_gi_create) ( ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [voxel_gi_get_data_cells](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_data_cells) ( voxel_gi: [RID](class_rid.md#class_RID) ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [voxel_gi_get_distance_field](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_distance_field) ( voxel_gi: [RID](class_rid.md#class_RID) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [voxel_gi_get_level_counts](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_level_counts) ( voxel_gi: [RID](class_rid.md#class_RID) ) const |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [voxel_gi_get_octree_cells](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_octree_cells) ( voxel_gi: [RID](class_rid.md#class_RID) ) const |
| [Vector3i](class_vector3i.md#class_Vector3i) | [voxel_gi_get_octree_size](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_octree_size) ( voxel_gi: [RID](class_rid.md#class_RID) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [voxel_gi_get_to_cell_xform](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_to_cell_xform) ( voxel_gi: [RID](class_rid.md#class_RID) ) const |
| void | [voxel_gi_set_baked_exposure_normalization](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_baked_exposure_normalization) ( voxel_gi: [RID](class_rid.md#class_RID), baked_exposure: [float](class_float.md#class_float) ) |
| void | [voxel_gi_set_bias](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_bias) ( voxel_gi: [RID](class_rid.md#class_RID), bias: [float](class_float.md#class_float) ) |
| void | [voxel_gi_set_dynamic_range](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_dynamic_range) ( voxel_gi: [RID](class_rid.md#class_RID), range: [float](class_float.md#class_float) ) |
| void | [voxel_gi_set_energy](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_energy) ( voxel_gi: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float) ) |
| void | [voxel_gi_set_interior](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_interior) ( voxel_gi: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |
| void | [voxel_gi_set_normal_bias](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_normal_bias) ( voxel_gi: [RID](class_rid.md#class_RID), bias: [float](class_float.md#class_float) ) |
| void | [voxel_gi_set_propagation](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_propagation) ( voxel_gi: [RID](class_rid.md#class_RID), amount: [float](class_float.md#class_float) ) |
| void | [voxel_gi_set_quality](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_quality) ( quality: [VoxelGIQuality](class_renderingserver.md#enum_RenderingServer_VoxelGIQuality) ) |
| void | [voxel_gi_set_use_two_bounces](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_use_two_bounces) ( voxel_gi: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) |

---

### Signals

<span id="class_RenderingServer_signal_frame_post_draw"></span>

**frame_post_draw** ( ) [🔗](class_renderingserver.md#class_RenderingServer_signal_frame_post_draw)

Emitted at the end of the frame, after the RenderingServer has finished updating all the Viewports.

---

<span id="class_RenderingServer_signal_frame_pre_draw"></span>

**frame_pre_draw** ( ) [🔗](class_renderingserver.md#class_RenderingServer_signal_frame_pre_draw)

Emitted at the beginning of the frame, before the RenderingServer updates all the Viewports.

---

### Enumerations

<span id="enum_RenderingServer_TextureType"></span>

enum **TextureType**: [🔗](class_renderingserver.md#enum_RenderingServer_TextureType)

<span id="class_RenderingServer_constant_TEXTURE_TYPE_2D"></span>

[TextureType](class_renderingserver.md#enum_RenderingServer_TextureType) **TEXTURE_TYPE_2D** = `0`

2D texture.

<span id="class_RenderingServer_constant_TEXTURE_TYPE_LAYERED"></span>

[TextureType](class_renderingserver.md#enum_RenderingServer_TextureType) **TEXTURE_TYPE_LAYERED** = `1`

Layered texture.

<span id="class_RenderingServer_constant_TEXTURE_TYPE_3D"></span>

[TextureType](class_renderingserver.md#enum_RenderingServer_TextureType) **TEXTURE_TYPE_3D** = `2`

3D texture.

---

<span id="enum_RenderingServer_TextureLayeredType"></span>

enum **TextureLayeredType**: [🔗](class_renderingserver.md#enum_RenderingServer_TextureLayeredType)

<span id="class_RenderingServer_constant_TEXTURE_LAYERED_2D_ARRAY"></span>

[TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) **TEXTURE_LAYERED_2D_ARRAY** = `0`

Array of 2-dimensional textures (see [Texture2DArray](class_texture2darray.md#class_Texture2DArray)).

<span id="class_RenderingServer_constant_TEXTURE_LAYERED_CUBEMAP"></span>

[TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) **TEXTURE_LAYERED_CUBEMAP** = `1`

Cubemap texture (see [Cubemap](class_cubemap.md#class_Cubemap)).

<span id="class_RenderingServer_constant_TEXTURE_LAYERED_CUBEMAP_ARRAY"></span>

[TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) **TEXTURE_LAYERED_CUBEMAP_ARRAY** = `2`

Array of cubemap textures (see [CubemapArray](class_cubemaparray.md#class_CubemapArray)).

---

<span id="enum_RenderingServer_CubeMapLayer"></span>

enum **CubeMapLayer**: [🔗](class_renderingserver.md#enum_RenderingServer_CubeMapLayer)

<span id="class_RenderingServer_constant_CUBEMAP_LAYER_LEFT"></span>

[CubeMapLayer](class_renderingserver.md#enum_RenderingServer_CubeMapLayer) **CUBEMAP_LAYER_LEFT** = `0`

Left face of a [Cubemap](class_cubemap.md#class_Cubemap).

<span id="class_RenderingServer_constant_CUBEMAP_LAYER_RIGHT"></span>

[CubeMapLayer](class_renderingserver.md#enum_RenderingServer_CubeMapLayer) **CUBEMAP_LAYER_RIGHT** = `1`

Right face of a [Cubemap](class_cubemap.md#class_Cubemap).

<span id="class_RenderingServer_constant_CUBEMAP_LAYER_BOTTOM"></span>

[CubeMapLayer](class_renderingserver.md#enum_RenderingServer_CubeMapLayer) **CUBEMAP_LAYER_BOTTOM** = `2`

Bottom face of a [Cubemap](class_cubemap.md#class_Cubemap).

<span id="class_RenderingServer_constant_CUBEMAP_LAYER_TOP"></span>

[CubeMapLayer](class_renderingserver.md#enum_RenderingServer_CubeMapLayer) **CUBEMAP_LAYER_TOP** = `3`

Top face of a [Cubemap](class_cubemap.md#class_Cubemap).

<span id="class_RenderingServer_constant_CUBEMAP_LAYER_FRONT"></span>

[CubeMapLayer](class_renderingserver.md#enum_RenderingServer_CubeMapLayer) **CUBEMAP_LAYER_FRONT** = `4`

Front face of a [Cubemap](class_cubemap.md#class_Cubemap).

<span id="class_RenderingServer_constant_CUBEMAP_LAYER_BACK"></span>

[CubeMapLayer](class_renderingserver.md#enum_RenderingServer_CubeMapLayer) **CUBEMAP_LAYER_BACK** = `5`

Back face of a [Cubemap](class_cubemap.md#class_Cubemap).

---

<span id="enum_RenderingServer_TextureDrawableFormat"></span>

enum **TextureDrawableFormat**: [🔗](class_renderingserver.md#enum_RenderingServer_TextureDrawableFormat)

<span id="class_RenderingServer_constant_TEXTURE_DRAWABLE_FORMAT_RGBA8"></span>

[TextureDrawableFormat](class_renderingserver.md#enum_RenderingServer_TextureDrawableFormat) **TEXTURE_DRAWABLE_FORMAT_RGBA8** = `0`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

<span id="class_RenderingServer_constant_TEXTURE_DRAWABLE_FORMAT_RGBA8_SRGB"></span>

[TextureDrawableFormat](class_renderingserver.md#enum_RenderingServer_TextureDrawableFormat) **TEXTURE_DRAWABLE_FORMAT_RGBA8_SRGB** = `1`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

When drawn to, an sRGB to linear color space conversion is performed.

<span id="class_RenderingServer_constant_TEXTURE_DRAWABLE_FORMAT_RGBAH"></span>

[TextureDrawableFormat](class_renderingserver.md#enum_RenderingServer_TextureDrawableFormat) **TEXTURE_DRAWABLE_FORMAT_RGBAH** = `2`

OpenGL texture format GL_RGBA16F where there are four components, each a 16-bit "half-precision" floating-point value.

<span id="class_RenderingServer_constant_TEXTURE_DRAWABLE_FORMAT_RGBAF"></span>

[TextureDrawableFormat](class_renderingserver.md#enum_RenderingServer_TextureDrawableFormat) **TEXTURE_DRAWABLE_FORMAT_RGBAF** = `3`

OpenGL texture format GL_RGBA32F where there are four components, each a 32-bit floating-point value.

---

<span id="enum_RenderingServer_ShaderMode"></span>

enum **ShaderMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ShaderMode)

<span id="class_RenderingServer_constant_SHADER_SPATIAL"></span>

[ShaderMode](class_renderingserver.md#enum_RenderingServer_ShaderMode) **SHADER_SPATIAL** = `0`

Shader is a 3D shader.

<span id="class_RenderingServer_constant_SHADER_CANVAS_ITEM"></span>

[ShaderMode](class_renderingserver.md#enum_RenderingServer_ShaderMode) **SHADER_CANVAS_ITEM** = `1`

Shader is a 2D shader.

<span id="class_RenderingServer_constant_SHADER_PARTICLES"></span>

[ShaderMode](class_renderingserver.md#enum_RenderingServer_ShaderMode) **SHADER_PARTICLES** = `2`

Shader is a particle shader (can be used in both 2D and 3D).

<span id="class_RenderingServer_constant_SHADER_SKY"></span>

[ShaderMode](class_renderingserver.md#enum_RenderingServer_ShaderMode) **SHADER_SKY** = `3`

Shader is a 3D sky shader.

<span id="class_RenderingServer_constant_SHADER_FOG"></span>

[ShaderMode](class_renderingserver.md#enum_RenderingServer_ShaderMode) **SHADER_FOG** = `4`

Shader is a 3D fog shader.

<span id="class_RenderingServer_constant_SHADER_TEXTURE_BLIT"></span>

[ShaderMode](class_renderingserver.md#enum_RenderingServer_ShaderMode) **SHADER_TEXTURE_BLIT** = `5`

Shader is a texture_blit shader.

<span id="class_RenderingServer_constant_SHADER_MAX"></span>

[ShaderMode](class_renderingserver.md#enum_RenderingServer_ShaderMode) **SHADER_MAX** = `6`

Represents the size of the [ShaderMode](class_renderingserver.md#enum_RenderingServer_ShaderMode) enum.

---

<span id="enum_RenderingServer_ArrayType"></span>

enum **ArrayType**: [🔗](class_renderingserver.md#enum_RenderingServer_ArrayType)

<span id="class_RenderingServer_constant_ARRAY_VERTEX"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_VERTEX** = `0`

Array is a vertex position array.

<span id="class_RenderingServer_constant_ARRAY_NORMAL"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_NORMAL** = `1`

Array is a normal array.

<span id="class_RenderingServer_constant_ARRAY_TANGENT"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_TANGENT** = `2`

Array is a tangent array.

<span id="class_RenderingServer_constant_ARRAY_COLOR"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_COLOR** = `3`

Array is a vertex color array.

<span id="class_RenderingServer_constant_ARRAY_TEX_UV"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_TEX_UV** = `4`

Array is a UV coordinates array.

<span id="class_RenderingServer_constant_ARRAY_TEX_UV2"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_TEX_UV2** = `5`

Array is a UV coordinates array for the second set of UV coordinates.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM0"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_CUSTOM0** = `6`

Array is a custom data array for the first set of custom data.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM1"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_CUSTOM1** = `7`

Array is a custom data array for the second set of custom data.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM2"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_CUSTOM2** = `8`

Array is a custom data array for the third set of custom data.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM3"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_CUSTOM3** = `9`

Array is a custom data array for the fourth set of custom data.

<span id="class_RenderingServer_constant_ARRAY_BONES"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_BONES** = `10`

Array contains bone information.

<span id="class_RenderingServer_constant_ARRAY_WEIGHTS"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_WEIGHTS** = `11`

Array is weight information.

<span id="class_RenderingServer_constant_ARRAY_INDEX"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_INDEX** = `12`

Array is an index array.

<span id="class_RenderingServer_constant_ARRAY_MAX"></span>

[ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) **ARRAY_MAX** = `13`

Represents the size of the [ArrayType](class_renderingserver.md#enum_RenderingServer_ArrayType) enum.

---

<span id="enum_RenderingServer_ArrayCustomFormat"></span>

enum **ArrayCustomFormat**: [🔗](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat)

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_RGBA8_UNORM"></span>

[ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) **ARRAY_CUSTOM_RGBA8_UNORM** = `0`

Custom data array contains 8-bit-per-channel red/green/blue/alpha color data. Values are normalized, unsigned floating-point in the `[0.0, 1.0]` range.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_RGBA8_SNORM"></span>

[ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) **ARRAY_CUSTOM_RGBA8_SNORM** = `1`

Custom data array contains 8-bit-per-channel red/green/blue/alpha color data. Values are normalized, signed floating-point in the `[-1.0, 1.0]` range.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_RG_HALF"></span>

[ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) **ARRAY_CUSTOM_RG_HALF** = `2`

Custom data array contains 16-bit-per-channel red/green color data. Values are floating-point in half precision.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_RGBA_HALF"></span>

[ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) **ARRAY_CUSTOM_RGBA_HALF** = `3`

Custom data array contains 16-bit-per-channel red/green/blue/alpha color data. Values are floating-point in half precision.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_R_FLOAT"></span>

[ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) **ARRAY_CUSTOM_R_FLOAT** = `4`

Custom data array contains 32-bit-per-channel red color data. Values are floating-point in single precision.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_RG_FLOAT"></span>

[ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) **ARRAY_CUSTOM_RG_FLOAT** = `5`

Custom data array contains 32-bit-per-channel red/green color data. Values are floating-point in single precision.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_RGB_FLOAT"></span>

[ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) **ARRAY_CUSTOM_RGB_FLOAT** = `6`

Custom data array contains 32-bit-per-channel red/green/blue color data. Values are floating-point in single precision.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_RGBA_FLOAT"></span>

[ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) **ARRAY_CUSTOM_RGBA_FLOAT** = `7`

Custom data array contains 32-bit-per-channel red/green/blue/alpha color data. Values are floating-point in single precision.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_MAX"></span>

[ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) **ARRAY_CUSTOM_MAX** = `8`

Represents the size of the [ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) enum.

---

<span id="enum_RenderingServer_ArrayFormat"></span>

flags **ArrayFormat**: [🔗](class_renderingserver.md#enum_RenderingServer_ArrayFormat)

<span id="class_RenderingServer_constant_ARRAY_FORMAT_VERTEX"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_VERTEX** = `1`

Flag used to mark a vertex position array.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_NORMAL"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_NORMAL** = `2`

Flag used to mark a normal array.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_TANGENT"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_TANGENT** = `4`

Flag used to mark a tangent array.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_COLOR"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_COLOR** = `8`

Flag used to mark a vertex color array.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_TEX_UV"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_TEX_UV** = `16`

Flag used to mark a UV coordinates array.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_TEX_UV2"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_TEX_UV2** = `32`

Flag used to mark a UV coordinates array for the second UV coordinates.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM0"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM0** = `64`

Flag used to mark an array of custom per-vertex data for the first set of custom data.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM1"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM1** = `128`

Flag used to mark an array of custom per-vertex data for the second set of custom data.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM2"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM2** = `256`

Flag used to mark an array of custom per-vertex data for the third set of custom data.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM3"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM3** = `512`

Flag used to mark an array of custom per-vertex data for the fourth set of custom data.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_BONES"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_BONES** = `1024`

Flag used to mark a bone information array.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_WEIGHTS"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_WEIGHTS** = `2048`

Flag used to mark a weights array.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_INDEX"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_INDEX** = `4096`

Flag used to mark an index array.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_BLEND_SHAPE_MASK"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_BLEND_SHAPE_MASK** = `7`

Mask of mesh channels permitted in blend shapes.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM_BASE"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM_BASE** = `13`

Shift of first custom channel.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM_BITS"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM_BITS** = `3`

Number of format bits per custom channel. See [ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat).

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM0_SHIFT"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM0_SHIFT** = `13`

Amount to shift [ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) for custom channel index 0.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM1_SHIFT"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM1_SHIFT** = `16`

Amount to shift [ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) for custom channel index 1.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM2_SHIFT"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM2_SHIFT** = `19`

Amount to shift [ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) for custom channel index 2.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM3_SHIFT"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM3_SHIFT** = `22`

Amount to shift [ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat) for custom channel index 3.

<span id="class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM_MASK"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FORMAT_CUSTOM_MASK** = `7`

Mask of custom format bits per custom channel. Must be shifted by one of the SHIFT constants. See [ArrayCustomFormat](class_renderingserver.md#enum_RenderingServer_ArrayCustomFormat).

<span id="class_RenderingServer_constant_ARRAY_COMPRESS_FLAGS_BASE"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_COMPRESS_FLAGS_BASE** = `25`

Shift of first compress flag. Compress flags should be passed to [ArrayMesh.add_surface_from_arrays()](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays) and [SurfaceTool.commit()](class_surfacetool.md#class_SurfaceTool_method_commit).

<span id="class_RenderingServer_constant_ARRAY_FLAG_USE_2D_VERTICES"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_USE_2D_VERTICES** = `33554432`

Flag used to mark that the array contains 2D vertices.

<span id="class_RenderingServer_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_USE_DYNAMIC_UPDATE** = `67108864`

Flag used to mark that the mesh data will use `GL_DYNAMIC_DRAW` on GLES. Unused on Vulkan.

<span id="class_RenderingServer_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_USE_8_BONE_WEIGHTS** = `134217728`

Flag used to mark that the array uses 8 bone weights instead of 4.

<span id="class_RenderingServer_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY** = `268435456`

Flag used to mark that the mesh does not have a vertex array and instead will infer vertex positions in the shader using indices and other information.

<span id="class_RenderingServer_constant_ARRAY_FLAG_COMPRESS_ATTRIBUTES"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_COMPRESS_ATTRIBUTES** = `536870912`

Flag used to mark that a mesh is using compressed attributes (vertices, normals, tangents, UVs). When this form of compression is enabled, vertex positions will be packed into an RGBA16UNORM attribute and scaled in the vertex shader. The normal and tangent will be packed into an RG16UNORM representing an axis, and a 16-bit float stored in the A-channel of the vertex. UVs will use 16-bit normalized floats instead of full 32-bit signed floats. When using this compression mode you must use either vertices, normals, and tangents or only vertices. You cannot use normals without tangents. Importers will automatically enable this compression if they can.

<span id="class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_BASE"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_FORMAT_VERSION_BASE** = `35`

Flag used to mark the start of the bits used to store the mesh version.

<span id="class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_SHIFT"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_FORMAT_VERSION_SHIFT** = `35`

Flag used to shift a mesh format int to bring the version into the lowest digits.

<span id="class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_1"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_FORMAT_VERSION_1** = `0`

Flag used to record the format used by prior mesh versions before the introduction of a version.

<span id="class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_2"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_FORMAT_VERSION_2** = `34359738368`

Flag used to record the second iteration of the mesh version flag. The primary difference between this and [ARRAY_FLAG_FORMAT_VERSION_1](class_renderingserver.md#class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_1) is that this version supports [ARRAY_FLAG_COMPRESS_ATTRIBUTES](class_renderingserver.md#class_RenderingServer_constant_ARRAY_FLAG_COMPRESS_ATTRIBUTES) and in this version vertex positions are de-interleaved from normals and tangents.

<span id="class_RenderingServer_constant_ARRAY_FLAG_FORMAT_CURRENT_VERSION"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_FORMAT_CURRENT_VERSION** = `34359738368`

Flag used to record the current version that the engine expects. Currently this is the same as [ARRAY_FLAG_FORMAT_VERSION_2](class_renderingserver.md#class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_2).

<span id="class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_MASK"></span>

[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) **ARRAY_FLAG_FORMAT_VERSION_MASK** = `255`

Flag used to isolate the bits used for mesh version after using [ARRAY_FLAG_FORMAT_VERSION_SHIFT](class_renderingserver.md#class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_SHIFT) to shift them into place.

---

<span id="enum_RenderingServer_PrimitiveType"></span>

enum **PrimitiveType**: [🔗](class_renderingserver.md#enum_RenderingServer_PrimitiveType)

<span id="class_RenderingServer_constant_PRIMITIVE_POINTS"></span>

[PrimitiveType](class_renderingserver.md#enum_RenderingServer_PrimitiveType) **PRIMITIVE_POINTS** = `0`

Primitive to draw consists of points.

<span id="class_RenderingServer_constant_PRIMITIVE_LINES"></span>

[PrimitiveType](class_renderingserver.md#enum_RenderingServer_PrimitiveType) **PRIMITIVE_LINES** = `1`

Primitive to draw consists of lines.

<span id="class_RenderingServer_constant_PRIMITIVE_LINE_STRIP"></span>

[PrimitiveType](class_renderingserver.md#enum_RenderingServer_PrimitiveType) **PRIMITIVE_LINE_STRIP** = `2`

Primitive to draw consists of a line strip from start to end.

<span id="class_RenderingServer_constant_PRIMITIVE_TRIANGLES"></span>

[PrimitiveType](class_renderingserver.md#enum_RenderingServer_PrimitiveType) **PRIMITIVE_TRIANGLES** = `3`

Primitive to draw consists of triangles.

<span id="class_RenderingServer_constant_PRIMITIVE_TRIANGLE_STRIP"></span>

[PrimitiveType](class_renderingserver.md#enum_RenderingServer_PrimitiveType) **PRIMITIVE_TRIANGLE_STRIP** = `4`

Primitive to draw consists of a triangle strip (the last 3 vertices are always combined to make a triangle).

<span id="class_RenderingServer_constant_PRIMITIVE_MAX"></span>

[PrimitiveType](class_renderingserver.md#enum_RenderingServer_PrimitiveType) **PRIMITIVE_MAX** = `5`

Represents the size of the [PrimitiveType](class_renderingserver.md#enum_RenderingServer_PrimitiveType) enum.

---

<span id="enum_RenderingServer_BlendShapeMode"></span>

enum **BlendShapeMode**: [🔗](class_renderingserver.md#enum_RenderingServer_BlendShapeMode)

<span id="class_RenderingServer_constant_BLEND_SHAPE_MODE_NORMALIZED"></span>

[BlendShapeMode](class_renderingserver.md#enum_RenderingServer_BlendShapeMode) **BLEND_SHAPE_MODE_NORMALIZED** = `0`

Blend shapes are normalized.

<span id="class_RenderingServer_constant_BLEND_SHAPE_MODE_RELATIVE"></span>

[BlendShapeMode](class_renderingserver.md#enum_RenderingServer_BlendShapeMode) **BLEND_SHAPE_MODE_RELATIVE** = `1`

Blend shapes are relative to base weight.

---

<span id="enum_RenderingServer_MultimeshTransformFormat"></span>

enum **MultimeshTransformFormat**: [🔗](class_renderingserver.md#enum_RenderingServer_MultimeshTransformFormat)

<span id="class_RenderingServer_constant_MULTIMESH_TRANSFORM_2D"></span>

[MultimeshTransformFormat](class_renderingserver.md#enum_RenderingServer_MultimeshTransformFormat) **MULTIMESH_TRANSFORM_2D** = `0`

Use [Transform2D](class_transform2d.md#class_Transform2D) to store MultiMesh transform.

<span id="class_RenderingServer_constant_MULTIMESH_TRANSFORM_3D"></span>

[MultimeshTransformFormat](class_renderingserver.md#enum_RenderingServer_MultimeshTransformFormat) **MULTIMESH_TRANSFORM_3D** = `1`

Use [Transform3D](class_transform3d.md#class_Transform3D) to store MultiMesh transform.

---

<span id="enum_RenderingServer_MultimeshPhysicsInterpolationQuality"></span>

enum **MultimeshPhysicsInterpolationQuality**: [🔗](class_renderingserver.md#enum_RenderingServer_MultimeshPhysicsInterpolationQuality)

<span id="class_RenderingServer_constant_MULTIMESH_INTERP_QUALITY_FAST"></span>

[MultimeshPhysicsInterpolationQuality](class_renderingserver.md#enum_RenderingServer_MultimeshPhysicsInterpolationQuality) **MULTIMESH_INTERP_QUALITY_FAST** = `0`

MultiMesh physics interpolation favors speed over quality.

<span id="class_RenderingServer_constant_MULTIMESH_INTERP_QUALITY_HIGH"></span>

[MultimeshPhysicsInterpolationQuality](class_renderingserver.md#enum_RenderingServer_MultimeshPhysicsInterpolationQuality) **MULTIMESH_INTERP_QUALITY_HIGH** = `1`

MultiMesh physics interpolation favors quality over speed.

---

<span id="enum_RenderingServer_LightProjectorFilter"></span>

enum **LightProjectorFilter**: [🔗](class_renderingserver.md#enum_RenderingServer_LightProjectorFilter)

<span id="class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_NEAREST"></span>

[LightProjectorFilter](class_renderingserver.md#enum_RenderingServer_LightProjectorFilter) **LIGHT_PROJECTOR_FILTER_NEAREST** = `0`

Nearest-neighbor filter for light projectors (use for pixel art light projectors). No mipmaps are used for rendering, which means light projectors at a distance will look sharp but grainy. This has roughly the same performance cost as using mipmaps.

<span id="class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_LINEAR"></span>

[LightProjectorFilter](class_renderingserver.md#enum_RenderingServer_LightProjectorFilter) **LIGHT_PROJECTOR_FILTER_LINEAR** = `1`

Linear filter for light projectors (use for non-pixel art light projectors). No mipmaps are used for rendering, which means light projectors at a distance will look smooth but blurry. This has roughly the same performance cost as using mipmaps.

<span id="class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS"></span>

[LightProjectorFilter](class_renderingserver.md#enum_RenderingServer_LightProjectorFilter) **LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS** = `2`

Nearest-neighbor filter for light projectors (use for pixel art light projectors). Isotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.

<span id="class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS"></span>

[LightProjectorFilter](class_renderingserver.md#enum_RenderingServer_LightProjectorFilter) **LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS** = `3`

Linear filter for light projectors (use for non-pixel art light projectors). Isotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.

<span id="class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS_ANISOTROPIC"></span>

[LightProjectorFilter](class_renderingserver.md#enum_RenderingServer_LightProjectorFilter) **LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS_ANISOTROPIC** = `4`

Nearest-neighbor filter for light projectors (use for pixel art light projectors). Anisotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined by ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

<span id="class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS_ANISOTROPIC"></span>

[LightProjectorFilter](class_renderingserver.md#enum_RenderingServer_LightProjectorFilter) **LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS_ANISOTROPIC** = `5`

Linear filter for light projectors (use for non-pixel art light projectors). Anisotropic mipmaps are used for rendering, which means light projectors at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined by ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

---

<span id="enum_RenderingServer_LightType"></span>

enum **LightType**: [🔗](class_renderingserver.md#enum_RenderingServer_LightType)

<span id="class_RenderingServer_constant_LIGHT_DIRECTIONAL"></span>

[LightType](class_renderingserver.md#enum_RenderingServer_LightType) **LIGHT_DIRECTIONAL** = `0`

Directional (sun/moon) light (see [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D)).

<span id="class_RenderingServer_constant_LIGHT_OMNI"></span>

[LightType](class_renderingserver.md#enum_RenderingServer_LightType) **LIGHT_OMNI** = `1`

Omni light (see [OmniLight3D](class_omnilight3d.md#class_OmniLight3D)).

<span id="class_RenderingServer_constant_LIGHT_SPOT"></span>

[LightType](class_renderingserver.md#enum_RenderingServer_LightType) **LIGHT_SPOT** = `2`

Spot light (see [SpotLight3D](class_spotlight3d.md#class_SpotLight3D)).

---

<span id="enum_RenderingServer_LightParam"></span>

enum **LightParam**: [🔗](class_renderingserver.md#enum_RenderingServer_LightParam)

<span id="class_RenderingServer_constant_LIGHT_PARAM_ENERGY"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_ENERGY** = `0`

The light's energy multiplier.

<span id="class_RenderingServer_constant_LIGHT_PARAM_INDIRECT_ENERGY"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_INDIRECT_ENERGY** = `1`

The light's indirect energy multiplier (final indirect energy is [LIGHT_PARAM_ENERGY](class_renderingserver.md#class_RenderingServer_constant_LIGHT_PARAM_ENERGY) \* [LIGHT_PARAM_INDIRECT_ENERGY](class_renderingserver.md#class_RenderingServer_constant_LIGHT_PARAM_INDIRECT_ENERGY)).

<span id="class_RenderingServer_constant_LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY** = `2`

The light's volumetric fog energy multiplier (final volumetric fog energy is [LIGHT_PARAM_ENERGY](class_renderingserver.md#class_RenderingServer_constant_LIGHT_PARAM_ENERGY) \* [LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY](class_renderingserver.md#class_RenderingServer_constant_LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY)).

<span id="class_RenderingServer_constant_LIGHT_PARAM_SPECULAR"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SPECULAR** = `3`

The light's influence on specularity.

<span id="class_RenderingServer_constant_LIGHT_PARAM_RANGE"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_RANGE** = `4`

The light's range.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SIZE"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SIZE** = `5`

The size of the light when using spot light or omni light. The angular size of the light when using directional light.

<span id="class_RenderingServer_constant_LIGHT_PARAM_ATTENUATION"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_ATTENUATION** = `6`

The light's attenuation.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SPOT_ANGLE"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SPOT_ANGLE** = `7`

The spotlight's angle.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SPOT_ATTENUATION"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SPOT_ATTENUATION** = `8`

The spotlight's attenuation.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_MAX_DISTANCE"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_MAX_DISTANCE** = `9`

The maximum distance for shadow splits. Increasing this value will make directional shadows visible from further away, at the cost of lower overall shadow detail and performance (since more objects need to be included in the directional shadow rendering).

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_SPLIT_1_OFFSET"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_SPLIT_1_OFFSET** = `10`

Proportion of shadow atlas occupied by the first split.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_SPLIT_2_OFFSET"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_SPLIT_2_OFFSET** = `11`

Proportion of shadow atlas occupied by the second split.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_SPLIT_3_OFFSET"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_SPLIT_3_OFFSET** = `12`

Proportion of shadow atlas occupied by the third split. The fourth split occupies the rest.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_FADE_START"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_FADE_START** = `13`

Proportion of shadow max distance where the shadow will start to fade out.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_NORMAL_BIAS"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_NORMAL_BIAS** = `14`

Normal bias used to offset shadow lookup by object normal. Can be used to fix self-shadowing artifacts.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_BIAS"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_BIAS** = `15`

Bias for the shadow lookup to fix self-shadowing artifacts.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_PANCAKE_SIZE"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_PANCAKE_SIZE** = `16`

Sets the size of the directional shadow pancake. The pancake offsets the start of the shadow's camera frustum to provide a higher effective depth resolution for the shadow. However, a high pancake size can cause artifacts in the shadows of large objects that are close to the edge of the frustum. Reducing the pancake size can help. Setting the size to `0` turns off the pancaking effect.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_OPACITY"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_OPACITY** = `17`

The light's shadow opacity. Values lower than `1.0` make the light appear through shadows. This can be used to fake global illumination at a low performance cost.

<span id="class_RenderingServer_constant_LIGHT_PARAM_SHADOW_BLUR"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_SHADOW_BLUR** = `18`

Blurs the edges of the shadow. Can be used to hide pixel artifacts in low resolution shadow maps. A high value can make shadows appear grainy and can cause other unwanted artifacts. Try to keep as near default as possible.

<span id="class_RenderingServer_constant_LIGHT_PARAM_TRANSMITTANCE_BIAS"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_TRANSMITTANCE_BIAS** = `19`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingServer_constant_LIGHT_PARAM_INTENSITY"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_INTENSITY** = `20`

Constant representing the intensity of the light, measured in Lumens when dealing with a [SpotLight3D](class_spotlight3d.md#class_SpotLight3D) or [OmniLight3D](class_omnilight3d.md#class_OmniLight3D), or measured in Lux with a [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D). Only used when ProjectSettings.rendering/lights_and_shadows/use_physical_light_units is `true`.

<span id="class_RenderingServer_constant_LIGHT_PARAM_MAX"></span>

[LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) **LIGHT_PARAM_MAX** = `21`

Represents the size of the [LightParam](class_renderingserver.md#enum_RenderingServer_LightParam) enum.

---

<span id="enum_RenderingServer_LightBakeMode"></span>

enum **LightBakeMode**: [🔗](class_renderingserver.md#enum_RenderingServer_LightBakeMode)

<span id="class_RenderingServer_constant_LIGHT_BAKE_DISABLED"></span>

[LightBakeMode](class_renderingserver.md#enum_RenderingServer_LightBakeMode) **LIGHT_BAKE_DISABLED** = `0`

Light is ignored when baking. This is the fastest mode, but the light will be taken into account when baking global illumination. This mode should generally be used for dynamic lights that change quickly, as the effect of global illumination is less noticeable on those lights.

<span id="class_RenderingServer_constant_LIGHT_BAKE_STATIC"></span>

[LightBakeMode](class_renderingserver.md#enum_RenderingServer_LightBakeMode) **LIGHT_BAKE_STATIC** = `1`

Light is taken into account in static baking ([VoxelGI](class_voxelgi.md#class_VoxelGI), [LightmapGI](class_lightmapgi.md#class_LightmapGI), SDFGI ([Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled))). The light can be moved around or modified, but its global illumination will not update in real-time. This is suitable for subtle changes (such as flickering torches), but generally not large changes such as toggling a light on and off.

<span id="class_RenderingServer_constant_LIGHT_BAKE_DYNAMIC"></span>

[LightBakeMode](class_renderingserver.md#enum_RenderingServer_LightBakeMode) **LIGHT_BAKE_DYNAMIC** = `2`

Light is taken into account in dynamic baking ([VoxelGI](class_voxelgi.md#class_VoxelGI) and SDFGI ([Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled)) only). The light can be moved around or modified with global illumination updating in real-time. The light's global illumination appearance will be slightly different compared to [LIGHT_BAKE_STATIC](class_renderingserver.md#class_RenderingServer_constant_LIGHT_BAKE_STATIC). This has a greater performance cost compared to [LIGHT_BAKE_STATIC](class_renderingserver.md#class_RenderingServer_constant_LIGHT_BAKE_STATIC). When using SDFGI, the update speed of dynamic lights is affected by ProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights.

---

<span id="enum_RenderingServer_LightOmniShadowMode"></span>

enum **LightOmniShadowMode**: [🔗](class_renderingserver.md#enum_RenderingServer_LightOmniShadowMode)

<span id="class_RenderingServer_constant_LIGHT_OMNI_SHADOW_DUAL_PARABOLOID"></span>

[LightOmniShadowMode](class_renderingserver.md#enum_RenderingServer_LightOmniShadowMode) **LIGHT_OMNI_SHADOW_DUAL_PARABOLOID** = `0`

Use a dual paraboloid shadow map for omni lights.

<span id="class_RenderingServer_constant_LIGHT_OMNI_SHADOW_CUBE"></span>

[LightOmniShadowMode](class_renderingserver.md#enum_RenderingServer_LightOmniShadowMode) **LIGHT_OMNI_SHADOW_CUBE** = `1`

Use a cubemap shadow map for omni lights. Slower but better quality than dual paraboloid.

---

<span id="enum_RenderingServer_LightDirectionalShadowMode"></span>

enum **LightDirectionalShadowMode**: [🔗](class_renderingserver.md#enum_RenderingServer_LightDirectionalShadowMode)

<span id="class_RenderingServer_constant_LIGHT_DIRECTIONAL_SHADOW_ORTHOGONAL"></span>

[LightDirectionalShadowMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalShadowMode) **LIGHT_DIRECTIONAL_SHADOW_ORTHOGONAL** = `0`

Use orthogonal shadow projection for directional light.

<span id="class_RenderingServer_constant_LIGHT_DIRECTIONAL_SHADOW_PARALLEL_2_SPLITS"></span>

[LightDirectionalShadowMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalShadowMode) **LIGHT_DIRECTIONAL_SHADOW_PARALLEL_2_SPLITS** = `1`

Use 2 splits for shadow projection when using directional light.

<span id="class_RenderingServer_constant_LIGHT_DIRECTIONAL_SHADOW_PARALLEL_4_SPLITS"></span>

[LightDirectionalShadowMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalShadowMode) **LIGHT_DIRECTIONAL_SHADOW_PARALLEL_4_SPLITS** = `2`

Use 4 splits for shadow projection when using directional light.

---

<span id="enum_RenderingServer_LightDirectionalSkyMode"></span>

enum **LightDirectionalSkyMode**: [🔗](class_renderingserver.md#enum_RenderingServer_LightDirectionalSkyMode)

<span id="class_RenderingServer_constant_LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_AND_SKY"></span>

[LightDirectionalSkyMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalSkyMode) **LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_AND_SKY** = `0`

Use DirectionalLight3D in both sky rendering and scene lighting.

<span id="class_RenderingServer_constant_LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_ONLY"></span>

[LightDirectionalSkyMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalSkyMode) **LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_ONLY** = `1`

Only use DirectionalLight3D in scene lighting.

<span id="class_RenderingServer_constant_LIGHT_DIRECTIONAL_SKY_MODE_SKY_ONLY"></span>

[LightDirectionalSkyMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalSkyMode) **LIGHT_DIRECTIONAL_SKY_MODE_SKY_ONLY** = `2`

Only use DirectionalLight3D in sky rendering.

---

<span id="enum_RenderingServer_ShadowQuality"></span>

enum **ShadowQuality**: [🔗](class_renderingserver.md#enum_RenderingServer_ShadowQuality)

<span id="class_RenderingServer_constant_SHADOW_QUALITY_HARD"></span>

[ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) **SHADOW_QUALITY_HARD** = `0`

Lowest shadow filtering quality (fastest). Soft shadows are not available with this quality setting, which means the [Light3D.shadow_blur](class_light3d.md#class_Light3D_property_shadow_blur) property is ignored if [Light3D.light_size](class_light3d.md#class_Light3D_property_light_size) and [Light3D.light_angular_distance](class_light3d.md#class_Light3D_property_light_angular_distance) is `0.0`.

 **Note:** The variable shadow blur performed by [Light3D.light_size](class_light3d.md#class_Light3D_property_light_size) and [Light3D.light_angular_distance](class_light3d.md#class_Light3D_property_light_angular_distance) is still effective when using hard shadow filtering. In this case, [Light3D.shadow_blur](class_light3d.md#class_Light3D_property_shadow_blur) *is* taken into account. However, the results will not be blurred, instead the blur amount is treated as a maximum radius for the penumbra.

<span id="class_RenderingServer_constant_SHADOW_QUALITY_SOFT_VERY_LOW"></span>

[ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) **SHADOW_QUALITY_SOFT_VERY_LOW** = `1`

Very low shadow filtering quality (faster). When using this quality setting, [Light3D.shadow_blur](class_light3d.md#class_Light3D_property_shadow_blur) is automatically multiplied by 0.75× to avoid introducing too much noise. This division only applies to lights whose [Light3D.light_size](class_light3d.md#class_Light3D_property_light_size) or [Light3D.light_angular_distance](class_light3d.md#class_Light3D_property_light_angular_distance) is `0.0`).

<span id="class_RenderingServer_constant_SHADOW_QUALITY_SOFT_LOW"></span>

[ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) **SHADOW_QUALITY_SOFT_LOW** = `2`

Low shadow filtering quality (fast).

<span id="class_RenderingServer_constant_SHADOW_QUALITY_SOFT_MEDIUM"></span>

[ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) **SHADOW_QUALITY_SOFT_MEDIUM** = `3`

Medium low shadow filtering quality (average).

<span id="class_RenderingServer_constant_SHADOW_QUALITY_SOFT_HIGH"></span>

[ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) **SHADOW_QUALITY_SOFT_HIGH** = `4`

High low shadow filtering quality (slow). When using this quality setting, [Light3D.shadow_blur](class_light3d.md#class_Light3D_property_shadow_blur) is automatically multiplied by 1.5× to better make use of the high sample count. This increased blur also improves the stability of dynamic object shadows. This multiplier only applies to lights whose [Light3D.light_size](class_light3d.md#class_Light3D_property_light_size) or [Light3D.light_angular_distance](class_light3d.md#class_Light3D_property_light_angular_distance) is `0.0`).

<span id="class_RenderingServer_constant_SHADOW_QUALITY_SOFT_ULTRA"></span>

[ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) **SHADOW_QUALITY_SOFT_ULTRA** = `5`

Highest low shadow filtering quality (slowest). When using this quality setting, [Light3D.shadow_blur](class_light3d.md#class_Light3D_property_shadow_blur) is automatically multiplied by 2× to better make use of the high sample count. This increased blur also improves the stability of dynamic object shadows. This multiplier only applies to lights whose [Light3D.light_size](class_light3d.md#class_Light3D_property_light_size) or [Light3D.light_angular_distance](class_light3d.md#class_Light3D_property_light_angular_distance) is `0.0`).

<span id="class_RenderingServer_constant_SHADOW_QUALITY_MAX"></span>

[ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) **SHADOW_QUALITY_MAX** = `6`

Represents the size of the [ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) enum.

---

<span id="enum_RenderingServer_ReflectionProbeUpdateMode"></span>

enum **ReflectionProbeUpdateMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ReflectionProbeUpdateMode)

<span id="class_RenderingServer_constant_REFLECTION_PROBE_UPDATE_ONCE"></span>

[ReflectionProbeUpdateMode](class_renderingserver.md#enum_RenderingServer_ReflectionProbeUpdateMode) **REFLECTION_PROBE_UPDATE_ONCE** = `0`

Reflection probe will update reflections once and then stop.

<span id="class_RenderingServer_constant_REFLECTION_PROBE_UPDATE_ALWAYS"></span>

[ReflectionProbeUpdateMode](class_renderingserver.md#enum_RenderingServer_ReflectionProbeUpdateMode) **REFLECTION_PROBE_UPDATE_ALWAYS** = `1`

Reflection probe will update each frame. This mode is necessary to capture moving objects.

---

<span id="enum_RenderingServer_ReflectionProbeAmbientMode"></span>

enum **ReflectionProbeAmbientMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ReflectionProbeAmbientMode)

<span id="class_RenderingServer_constant_REFLECTION_PROBE_AMBIENT_DISABLED"></span>

[ReflectionProbeAmbientMode](class_renderingserver.md#enum_RenderingServer_ReflectionProbeAmbientMode) **REFLECTION_PROBE_AMBIENT_DISABLED** = `0`

Do not apply any ambient lighting inside the reflection probe's box defined by its size.

<span id="class_RenderingServer_constant_REFLECTION_PROBE_AMBIENT_ENVIRONMENT"></span>

[ReflectionProbeAmbientMode](class_renderingserver.md#enum_RenderingServer_ReflectionProbeAmbientMode) **REFLECTION_PROBE_AMBIENT_ENVIRONMENT** = `1`

Apply automatically-sourced environment lighting inside the reflection probe's box defined by its size.

<span id="class_RenderingServer_constant_REFLECTION_PROBE_AMBIENT_COLOR"></span>

[ReflectionProbeAmbientMode](class_renderingserver.md#enum_RenderingServer_ReflectionProbeAmbientMode) **REFLECTION_PROBE_AMBIENT_COLOR** = `2`

Apply custom ambient lighting inside the reflection probe's box defined by its size. See [reflection_probe_set_ambient_color()](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_ambient_color) and [reflection_probe_set_ambient_energy()](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_ambient_energy).

---

<span id="enum_RenderingServer_DecalTexture"></span>

enum **DecalTexture**: [🔗](class_renderingserver.md#enum_RenderingServer_DecalTexture)

<span id="class_RenderingServer_constant_DECAL_TEXTURE_ALBEDO"></span>

[DecalTexture](class_renderingserver.md#enum_RenderingServer_DecalTexture) **DECAL_TEXTURE_ALBEDO** = `0`

Albedo texture slot in a decal ([Decal.texture_albedo](class_decal.md#class_Decal_property_texture_albedo)).

<span id="class_RenderingServer_constant_DECAL_TEXTURE_NORMAL"></span>

[DecalTexture](class_renderingserver.md#enum_RenderingServer_DecalTexture) **DECAL_TEXTURE_NORMAL** = `1`

Normal map texture slot in a decal ([Decal.texture_normal](class_decal.md#class_Decal_property_texture_normal)).

<span id="class_RenderingServer_constant_DECAL_TEXTURE_ORM"></span>

[DecalTexture](class_renderingserver.md#enum_RenderingServer_DecalTexture) **DECAL_TEXTURE_ORM** = `2`

Occlusion/Roughness/Metallic texture slot in a decal ([Decal.texture_orm](class_decal.md#class_Decal_property_texture_orm)).

<span id="class_RenderingServer_constant_DECAL_TEXTURE_EMISSION"></span>

[DecalTexture](class_renderingserver.md#enum_RenderingServer_DecalTexture) **DECAL_TEXTURE_EMISSION** = `3`

Emission texture slot in a decal ([Decal.texture_emission](class_decal.md#class_Decal_property_texture_emission)).

<span id="class_RenderingServer_constant_DECAL_TEXTURE_MAX"></span>

[DecalTexture](class_renderingserver.md#enum_RenderingServer_DecalTexture) **DECAL_TEXTURE_MAX** = `4`

Represents the size of the [DecalTexture](class_renderingserver.md#enum_RenderingServer_DecalTexture) enum.

---

<span id="enum_RenderingServer_DecalFilter"></span>

enum **DecalFilter**: [🔗](class_renderingserver.md#enum_RenderingServer_DecalFilter)

<span id="class_RenderingServer_constant_DECAL_FILTER_NEAREST"></span>

[DecalFilter](class_renderingserver.md#enum_RenderingServer_DecalFilter) **DECAL_FILTER_NEAREST** = `0`

Nearest-neighbor filter for decals (use for pixel art decals). No mipmaps are used for rendering, which means decals at a distance will look sharp but grainy. This has roughly the same performance cost as using mipmaps.

<span id="class_RenderingServer_constant_DECAL_FILTER_LINEAR"></span>

[DecalFilter](class_renderingserver.md#enum_RenderingServer_DecalFilter) **DECAL_FILTER_LINEAR** = `1`

Linear filter for decals (use for non-pixel art decals). No mipmaps are used for rendering, which means decals at a distance will look smooth but blurry. This has roughly the same performance cost as using mipmaps.

<span id="class_RenderingServer_constant_DECAL_FILTER_NEAREST_MIPMAPS"></span>

[DecalFilter](class_renderingserver.md#enum_RenderingServer_DecalFilter) **DECAL_FILTER_NEAREST_MIPMAPS** = `2`

Nearest-neighbor filter for decals (use for pixel art decals). Isotropic mipmaps are used for rendering, which means decals at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.

<span id="class_RenderingServer_constant_DECAL_FILTER_LINEAR_MIPMAPS"></span>

[DecalFilter](class_renderingserver.md#enum_RenderingServer_DecalFilter) **DECAL_FILTER_LINEAR_MIPMAPS** = `3`

Linear filter for decals (use for non-pixel art decals). Isotropic mipmaps are used for rendering, which means decals at a distance will look smooth but blurry. This has roughly the same performance cost as not using mipmaps.

<span id="class_RenderingServer_constant_DECAL_FILTER_NEAREST_MIPMAPS_ANISOTROPIC"></span>

[DecalFilter](class_renderingserver.md#enum_RenderingServer_DecalFilter) **DECAL_FILTER_NEAREST_MIPMAPS_ANISOTROPIC** = `4`

Nearest-neighbor filter for decals (use for pixel art decals). Anisotropic mipmaps are used for rendering, which means decals at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined by ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

<span id="class_RenderingServer_constant_DECAL_FILTER_LINEAR_MIPMAPS_ANISOTROPIC"></span>

[DecalFilter](class_renderingserver.md#enum_RenderingServer_DecalFilter) **DECAL_FILTER_LINEAR_MIPMAPS_ANISOTROPIC** = `5`

Linear filter for decals (use for non-pixel art decals). Anisotropic mipmaps are used for rendering, which means decals at a distance will look smooth and sharp when viewed from oblique angles. This looks better compared to isotropic mipmaps, but is slower. The level of anisotropic filtering is defined by ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

---

<span id="enum_RenderingServer_VoxelGIQuality"></span>

enum **VoxelGIQuality**: [🔗](class_renderingserver.md#enum_RenderingServer_VoxelGIQuality)

<span id="class_RenderingServer_constant_VOXEL_GI_QUALITY_LOW"></span>

[VoxelGIQuality](class_renderingserver.md#enum_RenderingServer_VoxelGIQuality) **VOXEL_GI_QUALITY_LOW** = `0`

Low [VoxelGI](class_voxelgi.md#class_VoxelGI) rendering quality using 4 cones.

<span id="class_RenderingServer_constant_VOXEL_GI_QUALITY_HIGH"></span>

[VoxelGIQuality](class_renderingserver.md#enum_RenderingServer_VoxelGIQuality) **VOXEL_GI_QUALITY_HIGH** = `1`

High [VoxelGI](class_voxelgi.md#class_VoxelGI) rendering quality using 6 cones.

---

<span id="enum_RenderingServer_ParticlesMode"></span>

enum **ParticlesMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ParticlesMode)

<span id="class_RenderingServer_constant_PARTICLES_MODE_2D"></span>

[ParticlesMode](class_renderingserver.md#enum_RenderingServer_ParticlesMode) **PARTICLES_MODE_2D** = `0`

2D particles.

<span id="class_RenderingServer_constant_PARTICLES_MODE_3D"></span>

[ParticlesMode](class_renderingserver.md#enum_RenderingServer_ParticlesMode) **PARTICLES_MODE_3D** = `1`

3D particles.

---

<span id="enum_RenderingServer_ParticlesTransformAlign"></span>

enum **ParticlesTransformAlign**: [🔗](class_renderingserver.md#enum_RenderingServer_ParticlesTransformAlign)

<span id="class_RenderingServer_constant_PARTICLES_TRANSFORM_ALIGN_DISABLED"></span>

[ParticlesTransformAlign](class_renderingserver.md#enum_RenderingServer_ParticlesTransformAlign) **PARTICLES_TRANSFORM_ALIGN_DISABLED** = `0`

Do not align particle transforms relative to the camera or velocity.

<span id="class_RenderingServer_constant_PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD"></span>

[ParticlesTransformAlign](class_renderingserver.md#enum_RenderingServer_ParticlesTransformAlign) **PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD** = `1`

Align each particle's Z axis to face the camera.

<span id="class_RenderingServer_constant_PARTICLES_TRANSFORM_ALIGN_Y_TO_VELOCITY"></span>

[ParticlesTransformAlign](class_renderingserver.md#enum_RenderingServer_ParticlesTransformAlign) **PARTICLES_TRANSFORM_ALIGN_Y_TO_VELOCITY** = `2`

Align each particle's Y axis to the velocity vector.

<span id="class_RenderingServer_constant_PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD_Y_TO_VELOCITY"></span>

[ParticlesTransformAlign](class_renderingserver.md#enum_RenderingServer_ParticlesTransformAlign) **PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD_Y_TO_VELOCITY** = `3`

Align each particle's Z axis to face the camera and Y axis to the velocity vector.

---

<span id="enum_RenderingServer_ParticlesDrawOrder"></span>

enum **ParticlesDrawOrder**: [🔗](class_renderingserver.md#enum_RenderingServer_ParticlesDrawOrder)

<span id="class_RenderingServer_constant_PARTICLES_DRAW_ORDER_INDEX"></span>

[ParticlesDrawOrder](class_renderingserver.md#enum_RenderingServer_ParticlesDrawOrder) **PARTICLES_DRAW_ORDER_INDEX** = `0`

Draw particles in the order that they appear in the particles array.

<span id="class_RenderingServer_constant_PARTICLES_DRAW_ORDER_LIFETIME"></span>

[ParticlesDrawOrder](class_renderingserver.md#enum_RenderingServer_ParticlesDrawOrder) **PARTICLES_DRAW_ORDER_LIFETIME** = `1`

Sort particles based on their lifetime. In other words, the particle with the highest lifetime is drawn at the front.

<span id="class_RenderingServer_constant_PARTICLES_DRAW_ORDER_REVERSE_LIFETIME"></span>

[ParticlesDrawOrder](class_renderingserver.md#enum_RenderingServer_ParticlesDrawOrder) **PARTICLES_DRAW_ORDER_REVERSE_LIFETIME** = `2`

Sort particles based on the inverse of their lifetime. In other words, the particle with the lowest lifetime is drawn at the front.

<span id="class_RenderingServer_constant_PARTICLES_DRAW_ORDER_VIEW_DEPTH"></span>

[ParticlesDrawOrder](class_renderingserver.md#enum_RenderingServer_ParticlesDrawOrder) **PARTICLES_DRAW_ORDER_VIEW_DEPTH** = `3`

Sort particles based on their distance to the camera.

---

<span id="enum_RenderingServer_ParticlesCollisionType"></span>

enum **ParticlesCollisionType**: [🔗](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType)

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_SPHERE_ATTRACT"></span>

[ParticlesCollisionType](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType) **PARTICLES_COLLISION_TYPE_SPHERE_ATTRACT** = `0`

Sphere attractor type for [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) (see [GPUParticlesAttractorSphere3D](class_gpuparticlesattractorsphere3d.md#class_GPUParticlesAttractorSphere3D)).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_BOX_ATTRACT"></span>

[ParticlesCollisionType](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType) **PARTICLES_COLLISION_TYPE_BOX_ATTRACT** = `1`

Box attractor type for [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) (see [GPUParticlesAttractorBox3D](class_gpuparticlesattractorbox3d.md#class_GPUParticlesAttractorBox3D)).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_VECTOR_FIELD_ATTRACT"></span>

[ParticlesCollisionType](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType) **PARTICLES_COLLISION_TYPE_VECTOR_FIELD_ATTRACT** = `2`

Vector field attractor type for [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) (see [GPUParticlesAttractorVectorField3D](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D)).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_SPHERE_COLLIDE"></span>

[ParticlesCollisionType](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType) **PARTICLES_COLLISION_TYPE_SPHERE_COLLIDE** = `3`

Sphere collision type for [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) (see [GPUParticlesCollisionSphere3D](class_gpuparticlescollisionsphere3d.md#class_GPUParticlesCollisionSphere3D)).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_BOX_COLLIDE"></span>

[ParticlesCollisionType](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType) **PARTICLES_COLLISION_TYPE_BOX_COLLIDE** = `4`

Box collision type for [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) (see [GPUParticlesCollisionBox3D](class_gpuparticlescollisionbox3d.md#class_GPUParticlesCollisionBox3D)).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_SDF_COLLIDE"></span>

[ParticlesCollisionType](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType) **PARTICLES_COLLISION_TYPE_SDF_COLLIDE** = `5`

Signed distance field collision type for [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) (see [GPUParticlesCollisionSDF3D](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D)).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_HEIGHTFIELD_COLLIDE"></span>

[ParticlesCollisionType](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType) **PARTICLES_COLLISION_TYPE_HEIGHTFIELD_COLLIDE** = `6`

Heightfield collision type for [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) (see [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D)).

---

<span id="enum_RenderingServer_ParticlesCollisionHeightfieldResolution"></span>

enum **ParticlesCollisionHeightfieldResolution**: [🔗](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution)

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_256"></span>

[ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_256** = `0`

256×256 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_512"></span>

[ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_512** = `1`

512×512 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_1024"></span>

[ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_1024** = `2`

1024×1024 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_2048"></span>

[ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_2048** = `3`

2048×2048 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_4096"></span>

[ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_4096** = `4`

4096×4096 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_8192"></span>

[ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_8192** = `5`

8192×8192 heightfield resolution for [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D).

<span id="class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_MAX"></span>

[ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_MAX** = `6`

Represents the size of the [ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) enum.

---

<span id="enum_RenderingServer_FogVolumeShape"></span>

enum **FogVolumeShape**: [🔗](class_renderingserver.md#enum_RenderingServer_FogVolumeShape)

<span id="class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID"></span>

[FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) **FOG_VOLUME_SHAPE_ELLIPSOID** = `0`

[FogVolume](class_fogvolume.md#class_FogVolume) will be shaped like an ellipsoid (stretched sphere).

<span id="class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE"></span>

[FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) **FOG_VOLUME_SHAPE_CONE** = `1`

[FogVolume](class_fogvolume.md#class_FogVolume) will be shaped like a cone pointing upwards (in local coordinates). The cone's angle is set automatically to fill the size. The cone will be adjusted to fit within the size. Rotate the [FogVolume](class_fogvolume.md#class_FogVolume) node to reorient the cone. Non-uniform scaling via size is not supported (scale the [FogVolume](class_fogvolume.md#class_FogVolume) node instead).

<span id="class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER"></span>

[FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) **FOG_VOLUME_SHAPE_CYLINDER** = `2`

[FogVolume](class_fogvolume.md#class_FogVolume) will be shaped like an upright cylinder (in local coordinates). Rotate the [FogVolume](class_fogvolume.md#class_FogVolume) node to reorient the cylinder. The cylinder will be adjusted to fit within the size. Non-uniform scaling via size is not supported (scale the [FogVolume](class_fogvolume.md#class_FogVolume) node instead).

<span id="class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX"></span>

[FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) **FOG_VOLUME_SHAPE_BOX** = `3`

[FogVolume](class_fogvolume.md#class_FogVolume) will be shaped like a box.

<span id="class_RenderingServer_constant_FOG_VOLUME_SHAPE_WORLD"></span>

[FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) **FOG_VOLUME_SHAPE_WORLD** = `4`

[FogVolume](class_fogvolume.md#class_FogVolume) will have no shape, will cover the whole world and will not be culled.

<span id="class_RenderingServer_constant_FOG_VOLUME_SHAPE_MAX"></span>

[FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) **FOG_VOLUME_SHAPE_MAX** = `5`

Represents the size of the [FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) enum.

---

<span id="enum_RenderingServer_ViewportScaling3DMode"></span>

enum **ViewportScaling3DMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode)

<span id="class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_BILINEAR"></span>

[ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) **VIEWPORT_SCALING_3D_MODE_BILINEAR** = `0`

Use bilinear scaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale). Values less than `1.0` will result in undersampling while values greater than `1.0` will result in supersampling. A value of `1.0` disables scaling.

<span id="class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_FSR"></span>

[ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) **VIEWPORT_SCALING_3D_MODE_FSR** = `1`

Use AMD FidelityFX Super Resolution 1.0 upscaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale). Values less than `1.0` will result in the viewport being upscaled using FSR. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` disables scaling.

<span id="class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_FSR2"></span>

[ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) **VIEWPORT_SCALING_3D_MODE_FSR2** = `2`

Use AMD FidelityFX Super Resolution 2.2 upscaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale). Values less than `1.0` will result in the viewport being upscaled using FSR2. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` will use FSR2 at native resolution as a TAA solution.

<span id="class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_METALFX_SPATIAL"></span>

[ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) **VIEWPORT_SCALING_3D_MODE_METALFX_SPATIAL** = `3`

Use MetalFX spatial upscaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale). Values less than `1.0` will result in the viewport being upscaled using MetalFX. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` disables scaling.

 **Note:** Only supported when the Metal rendering driver is in use, which limits this scaling mode to macOS and iOS.

<span id="class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_METALFX_TEMPORAL"></span>

[ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) **VIEWPORT_SCALING_3D_MODE_METALFX_TEMPORAL** = `4`

Use MetalFX temporal upscaling for the viewport's 3D buffer. The amount of scaling can be set using [Viewport.scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale). Values less than `1.0` will result in the viewport being upscaled using MetalFX. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` will use MetalFX at native resolution as a TAA solution.

 **Note:** Only supported when the Metal rendering driver is in use, which limits this scaling mode to macOS and iOS.

<span id="class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_MAX"></span>

[ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) **VIEWPORT_SCALING_3D_MODE_MAX** = `5`

Represents the size of the [ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) enum.

---

<span id="enum_RenderingServer_ViewportUpdateMode"></span>

enum **ViewportUpdateMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode)

<span id="class_RenderingServer_constant_VIEWPORT_UPDATE_DISABLED"></span>

[ViewportUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode) **VIEWPORT_UPDATE_DISABLED** = `0`

Do not update the viewport's render target.

<span id="class_RenderingServer_constant_VIEWPORT_UPDATE_ONCE"></span>

[ViewportUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode) **VIEWPORT_UPDATE_ONCE** = `1`

Update the viewport's render target once, then switch to [VIEWPORT_UPDATE_DISABLED](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_UPDATE_DISABLED).

<span id="class_RenderingServer_constant_VIEWPORT_UPDATE_WHEN_VISIBLE"></span>

[ViewportUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode) **VIEWPORT_UPDATE_WHEN_VISIBLE** = `2`

Update the viewport's render target only when it is visible. This is the default value.

<span id="class_RenderingServer_constant_VIEWPORT_UPDATE_WHEN_PARENT_VISIBLE"></span>

[ViewportUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode) **VIEWPORT_UPDATE_WHEN_PARENT_VISIBLE** = `3`

Update the viewport's render target only when its parent is visible.

<span id="class_RenderingServer_constant_VIEWPORT_UPDATE_ALWAYS"></span>

[ViewportUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode) **VIEWPORT_UPDATE_ALWAYS** = `4`

Always update the viewport's render target.

---

<span id="enum_RenderingServer_ViewportClearMode"></span>

enum **ViewportClearMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportClearMode)

<span id="class_RenderingServer_constant_VIEWPORT_CLEAR_ALWAYS"></span>

[ViewportClearMode](class_renderingserver.md#enum_RenderingServer_ViewportClearMode) **VIEWPORT_CLEAR_ALWAYS** = `0`

Always clear the viewport's render target before drawing.

<span id="class_RenderingServer_constant_VIEWPORT_CLEAR_NEVER"></span>

[ViewportClearMode](class_renderingserver.md#enum_RenderingServer_ViewportClearMode) **VIEWPORT_CLEAR_NEVER** = `1`

Never clear the viewport's render target.

<span id="class_RenderingServer_constant_VIEWPORT_CLEAR_ONLY_NEXT_FRAME"></span>

[ViewportClearMode](class_renderingserver.md#enum_RenderingServer_ViewportClearMode) **VIEWPORT_CLEAR_ONLY_NEXT_FRAME** = `2`

Clear the viewport's render target on the next frame, then switch to [VIEWPORT_CLEAR_NEVER](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_CLEAR_NEVER).

---

<span id="enum_RenderingServer_ViewportEnvironmentMode"></span>

enum **ViewportEnvironmentMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportEnvironmentMode)

<span id="class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_DISABLED"></span>

[ViewportEnvironmentMode](class_renderingserver.md#enum_RenderingServer_ViewportEnvironmentMode) **VIEWPORT_ENVIRONMENT_DISABLED** = `0`

Disable rendering of 3D environment over 2D canvas.

<span id="class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_ENABLED"></span>

[ViewportEnvironmentMode](class_renderingserver.md#enum_RenderingServer_ViewportEnvironmentMode) **VIEWPORT_ENVIRONMENT_ENABLED** = `1`

Enable rendering of 3D environment over 2D canvas.

<span id="class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_INHERIT"></span>

[ViewportEnvironmentMode](class_renderingserver.md#enum_RenderingServer_ViewportEnvironmentMode) **VIEWPORT_ENVIRONMENT_INHERIT** = `2`

Inherit enable/disable value from parent. If the topmost parent is also set to [VIEWPORT_ENVIRONMENT_INHERIT](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_INHERIT), then this has the same behavior as [VIEWPORT_ENVIRONMENT_ENABLED](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_ENABLED).

<span id="class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_MAX"></span>

[ViewportEnvironmentMode](class_renderingserver.md#enum_RenderingServer_ViewportEnvironmentMode) **VIEWPORT_ENVIRONMENT_MAX** = `3`

Represents the size of the [ViewportEnvironmentMode](class_renderingserver.md#enum_RenderingServer_ViewportEnvironmentMode) enum.

---

<span id="enum_RenderingServer_ViewportSDFOversize"></span>

enum **ViewportSDFOversize**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportSDFOversize)

<span id="class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_100_PERCENT"></span>

[ViewportSDFOversize](class_renderingserver.md#enum_RenderingServer_ViewportSDFOversize) **VIEWPORT_SDF_OVERSIZE_100_PERCENT** = `0`

Do not oversize the 2D signed distance field. Occluders may disappear when touching the viewport's edges, and [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) collision may stop working earlier than intended. This has the lowest GPU requirements.

<span id="class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_120_PERCENT"></span>

[ViewportSDFOversize](class_renderingserver.md#enum_RenderingServer_ViewportSDFOversize) **VIEWPORT_SDF_OVERSIZE_120_PERCENT** = `1`

2D signed distance field covers 20% of the viewport's size outside the viewport on each side (top, right, bottom, left).

<span id="class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_150_PERCENT"></span>

[ViewportSDFOversize](class_renderingserver.md#enum_RenderingServer_ViewportSDFOversize) **VIEWPORT_SDF_OVERSIZE_150_PERCENT** = `2`

2D signed distance field covers 50% of the viewport's size outside the viewport on each side (top, right, bottom, left).

<span id="class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_200_PERCENT"></span>

[ViewportSDFOversize](class_renderingserver.md#enum_RenderingServer_ViewportSDFOversize) **VIEWPORT_SDF_OVERSIZE_200_PERCENT** = `3`

2D signed distance field covers 100% of the viewport's size outside the viewport on each side (top, right, bottom, left). This has the highest GPU requirements.

<span id="class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_MAX"></span>

[ViewportSDFOversize](class_renderingserver.md#enum_RenderingServer_ViewportSDFOversize) **VIEWPORT_SDF_OVERSIZE_MAX** = `4`

Represents the size of the [ViewportSDFOversize](class_renderingserver.md#enum_RenderingServer_ViewportSDFOversize) enum.

---

<span id="enum_RenderingServer_ViewportSDFScale"></span>

enum **ViewportSDFScale**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportSDFScale)

<span id="class_RenderingServer_constant_VIEWPORT_SDF_SCALE_100_PERCENT"></span>

[ViewportSDFScale](class_renderingserver.md#enum_RenderingServer_ViewportSDFScale) **VIEWPORT_SDF_SCALE_100_PERCENT** = `0`

Full resolution 2D signed distance field scale. This has the highest GPU requirements.

<span id="class_RenderingServer_constant_VIEWPORT_SDF_SCALE_50_PERCENT"></span>

[ViewportSDFScale](class_renderingserver.md#enum_RenderingServer_ViewportSDFScale) **VIEWPORT_SDF_SCALE_50_PERCENT** = `1`

Half resolution 2D signed distance field scale on each axis (25% of the viewport pixel count).

<span id="class_RenderingServer_constant_VIEWPORT_SDF_SCALE_25_PERCENT"></span>

[ViewportSDFScale](class_renderingserver.md#enum_RenderingServer_ViewportSDFScale) **VIEWPORT_SDF_SCALE_25_PERCENT** = `2`

Quarter resolution 2D signed distance field scale on each axis (6.25% of the viewport pixel count). This has the lowest GPU requirements.

<span id="class_RenderingServer_constant_VIEWPORT_SDF_SCALE_MAX"></span>

[ViewportSDFScale](class_renderingserver.md#enum_RenderingServer_ViewportSDFScale) **VIEWPORT_SDF_SCALE_MAX** = `3`

Represents the size of the [ViewportSDFScale](class_renderingserver.md#enum_RenderingServer_ViewportSDFScale) enum.

---

<span id="enum_RenderingServer_ViewportMSAA"></span>

enum **ViewportMSAA**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportMSAA)

<span id="class_RenderingServer_constant_VIEWPORT_MSAA_DISABLED"></span>

[ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) **VIEWPORT_MSAA_DISABLED** = `0`

Multisample antialiasing for 3D is disabled. This is the default value, and also the fastest setting.

<span id="class_RenderingServer_constant_VIEWPORT_MSAA_2X"></span>

[ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) **VIEWPORT_MSAA_2X** = `1`

Multisample antialiasing uses 2 samples per pixel for 3D. This has a moderate impact on performance.

<span id="class_RenderingServer_constant_VIEWPORT_MSAA_4X"></span>

[ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) **VIEWPORT_MSAA_4X** = `2`

Multisample antialiasing uses 4 samples per pixel for 3D. This has a high impact on performance.

<span id="class_RenderingServer_constant_VIEWPORT_MSAA_8X"></span>

[ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) **VIEWPORT_MSAA_8X** = `3`

Multisample antialiasing uses 8 samples per pixel for 3D. This has a very high impact on performance. Likely unsupported on low-end and older hardware.

<span id="class_RenderingServer_constant_VIEWPORT_MSAA_MAX"></span>

[ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) **VIEWPORT_MSAA_MAX** = `4`

Represents the size of the [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) enum.

---

<span id="enum_RenderingServer_ViewportAnisotropicFiltering"></span>

enum **ViewportAnisotropicFiltering**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering)

<span id="class_RenderingServer_constant_VIEWPORT_ANISOTROPY_DISABLED"></span>

[ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) **VIEWPORT_ANISOTROPY_DISABLED** = `0`

Anisotropic filtering is disabled.

<span id="class_RenderingServer_constant_VIEWPORT_ANISOTROPY_2X"></span>

[ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) **VIEWPORT_ANISOTROPY_2X** = `1`

Use 2× anisotropic filtering.

<span id="class_RenderingServer_constant_VIEWPORT_ANISOTROPY_4X"></span>

[ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) **VIEWPORT_ANISOTROPY_4X** = `2`

Use 4× anisotropic filtering. This is the default value.

<span id="class_RenderingServer_constant_VIEWPORT_ANISOTROPY_8X"></span>

[ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) **VIEWPORT_ANISOTROPY_8X** = `3`

Use 8× anisotropic filtering.

<span id="class_RenderingServer_constant_VIEWPORT_ANISOTROPY_16X"></span>

[ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) **VIEWPORT_ANISOTROPY_16X** = `4`

Use 16× anisotropic filtering.

<span id="class_RenderingServer_constant_VIEWPORT_ANISOTROPY_MAX"></span>

[ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) **VIEWPORT_ANISOTROPY_MAX** = `5`

Represents the size of the [ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) enum.

---

<span id="enum_RenderingServer_ViewportScreenSpaceAA"></span>

enum **ViewportScreenSpaceAA**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA)

<span id="class_RenderingServer_constant_VIEWPORT_SCREEN_SPACE_AA_DISABLED"></span>

[ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) **VIEWPORT_SCREEN_SPACE_AA_DISABLED** = `0`

Do not perform any antialiasing in the full screen post-process.

<span id="class_RenderingServer_constant_VIEWPORT_SCREEN_SPACE_AA_FXAA"></span>

[ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) **VIEWPORT_SCREEN_SPACE_AA_FXAA** = `1`

Use fast approximate antialiasing. FXAA is a popular screen-space antialiasing method, which is fast but will make the image look blurry, especially at lower resolutions. It can still work relatively well at large resolutions such as 1440p and 4K.

<span id="class_RenderingServer_constant_VIEWPORT_SCREEN_SPACE_AA_SMAA"></span>

[ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) **VIEWPORT_SCREEN_SPACE_AA_SMAA** = `2`

Use subpixel morphological antialiasing. SMAA may produce clearer results than FXAA, but at a slightly higher performance cost.

<span id="class_RenderingServer_constant_VIEWPORT_SCREEN_SPACE_AA_MAX"></span>

[ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) **VIEWPORT_SCREEN_SPACE_AA_MAX** = `3`

Represents the size of the [ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) enum.

---

<span id="enum_RenderingServer_ViewportOcclusionCullingBuildQuality"></span>

enum **ViewportOcclusionCullingBuildQuality**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportOcclusionCullingBuildQuality)

<span id="class_RenderingServer_constant_VIEWPORT_OCCLUSION_BUILD_QUALITY_LOW"></span>

[ViewportOcclusionCullingBuildQuality](class_renderingserver.md#enum_RenderingServer_ViewportOcclusionCullingBuildQuality) **VIEWPORT_OCCLUSION_BUILD_QUALITY_LOW** = `0`

Low occlusion culling BVH build quality (as defined by Embree). Results in the lowest CPU usage, but least effective culling.

<span id="class_RenderingServer_constant_VIEWPORT_OCCLUSION_BUILD_QUALITY_MEDIUM"></span>

[ViewportOcclusionCullingBuildQuality](class_renderingserver.md#enum_RenderingServer_ViewportOcclusionCullingBuildQuality) **VIEWPORT_OCCLUSION_BUILD_QUALITY_MEDIUM** = `1`

Medium occlusion culling BVH build quality (as defined by Embree).

<span id="class_RenderingServer_constant_VIEWPORT_OCCLUSION_BUILD_QUALITY_HIGH"></span>

[ViewportOcclusionCullingBuildQuality](class_renderingserver.md#enum_RenderingServer_ViewportOcclusionCullingBuildQuality) **VIEWPORT_OCCLUSION_BUILD_QUALITY_HIGH** = `2`

High occlusion culling BVH build quality (as defined by Embree). Results in the highest CPU usage, but most effective culling.

---

<span id="enum_RenderingServer_ViewportRenderInfo"></span>

enum **ViewportRenderInfo**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfo)

<span id="class_RenderingServer_constant_VIEWPORT_RENDER_INFO_OBJECTS_IN_FRAME"></span>

[ViewportRenderInfo](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfo) **VIEWPORT_RENDER_INFO_OBJECTS_IN_FRAME** = `0`

Number of objects drawn in a single frame.

<span id="class_RenderingServer_constant_VIEWPORT_RENDER_INFO_PRIMITIVES_IN_FRAME"></span>

[ViewportRenderInfo](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfo) **VIEWPORT_RENDER_INFO_PRIMITIVES_IN_FRAME** = `1`

Number of points, lines, or triangles drawn in a single frame.

<span id="class_RenderingServer_constant_VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME"></span>

[ViewportRenderInfo](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfo) **VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME** = `2`

Number of draw calls during this frame.

<span id="class_RenderingServer_constant_VIEWPORT_RENDER_INFO_MAX"></span>

[ViewportRenderInfo](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfo) **VIEWPORT_RENDER_INFO_MAX** = `3`

Represents the size of the [ViewportRenderInfo](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfo) enum.

---

<span id="enum_RenderingServer_ViewportRenderInfoType"></span>

enum **ViewportRenderInfoType**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfoType)

<span id="class_RenderingServer_constant_VIEWPORT_RENDER_INFO_TYPE_VISIBLE"></span>

[ViewportRenderInfoType](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfoType) **VIEWPORT_RENDER_INFO_TYPE_VISIBLE** = `0`

Visible render pass (excluding shadows).

<span id="class_RenderingServer_constant_VIEWPORT_RENDER_INFO_TYPE_SHADOW"></span>

[ViewportRenderInfoType](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfoType) **VIEWPORT_RENDER_INFO_TYPE_SHADOW** = `1`

Shadow render pass. Objects will be rendered several times depending on the number of amounts of lights with shadows and the number of directional shadow splits.

<span id="class_RenderingServer_constant_VIEWPORT_RENDER_INFO_TYPE_CANVAS"></span>

[ViewportRenderInfoType](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfoType) **VIEWPORT_RENDER_INFO_TYPE_CANVAS** = `2`

Canvas item rendering. This includes all 2D rendering.

<span id="class_RenderingServer_constant_VIEWPORT_RENDER_INFO_TYPE_MAX"></span>

[ViewportRenderInfoType](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfoType) **VIEWPORT_RENDER_INFO_TYPE_MAX** = `3`

Represents the size of the [ViewportRenderInfoType](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfoType) enum.

---

<span id="enum_RenderingServer_ViewportDebugDraw"></span>

enum **ViewportDebugDraw**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw)

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_DISABLED"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_DISABLED** = `0`

Debug draw is disabled. Default setting.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_UNSHADED"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_UNSHADED** = `1`

Objects are displayed without light information.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_LIGHTING"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_LIGHTING** = `2`

Objects are displayed with only light information.

 **Note:** When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_OVERDRAW"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_OVERDRAW** = `3`

Objects are displayed semi-transparent with additive blending so you can see where they are drawing over top of one another. A higher overdraw (represented by brighter colors) means you are wasting performance on drawing pixels that are being hidden behind others.

 **Note:** When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_WIREFRAME"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_WIREFRAME** = `4`

Debug draw draws objects in wireframe.

 **Note:** [set_debug_generate_wireframes()](class_renderingserver.md#class_RenderingServer_method_set_debug_generate_wireframes) must be called before loading any meshes for wireframes to be visible when using the Compatibility renderer.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_NORMAL_BUFFER"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_NORMAL_BUFFER** = `5`

Normal buffer is drawn instead of regular scene so you can see the per-pixel normals that will be used by post-processing effects.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_VOXEL_GI_ALBEDO"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_VOXEL_GI_ALBEDO** = `6`

Objects are displayed with only the albedo value from [VoxelGI](class_voxelgi.md#class_VoxelGI) s. Requires at least one visible [VoxelGI](class_voxelgi.md#class_VoxelGI) node that has been baked to have a visible effect.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_VOXEL_GI_LIGHTING"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_VOXEL_GI_LIGHTING** = `7`

Objects are displayed with only the lighting value from [VoxelGI](class_voxelgi.md#class_VoxelGI) s. Requires at least one visible [VoxelGI](class_voxelgi.md#class_VoxelGI) node that has been baked to have a visible effect.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_VOXEL_GI_EMISSION"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_VOXEL_GI_EMISSION** = `8`

Objects are displayed with only the emission color from [VoxelGI](class_voxelgi.md#class_VoxelGI) s. Requires at least one visible [VoxelGI](class_voxelgi.md#class_VoxelGI) node that has been baked to have a visible effect.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SHADOW_ATLAS"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_SHADOW_ATLAS** = `9`

Draws the shadow atlas that stores shadows from [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) s and [SpotLight3D](class_spotlight3d.md#class_SpotLight3D) s in the upper left quadrant of the [Viewport](class_viewport.md#class_Viewport).

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS** = `10`

Draws the shadow atlas that stores shadows from [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D) s in the upper left quadrant of the [Viewport](class_viewport.md#class_Viewport).

The slice of the camera frustum related to the shadow map cascade is superimposed to visualize coverage. The color of each slice matches the colors used for [VIEWPORT_DEBUG_DRAW_PSSM_SPLITS](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_PSSM_SPLITS). When shadow cascades are blended the overlap is taken into account when drawing the frustum slices.

The last cascade shows all frustum slices to illustrate the coverage of all slices.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SCENE_LUMINANCE"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_SCENE_LUMINANCE** = `11`

Draws the estimated scene luminance. This is a 1×1 texture that is generated when autoexposure is enabled to control the scene's exposure.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SSAO"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_SSAO** = `12`

Draws the screen space ambient occlusion texture instead of the scene so that you can clearly see how it is affecting objects. In order for this display mode to work, you must have [Environment.ssao_enabled](class_environment.md#class_Environment_property_ssao_enabled) set in your [WorldEnvironment](class_worldenvironment.md#class_WorldEnvironment).

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SSIL"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_SSIL** = `13`

Draws the screen space indirect lighting texture instead of the scene so that you can clearly see how it is affecting objects. In order for this display mode to work, you must have [Environment.ssil_enabled](class_environment.md#class_Environment_property_ssil_enabled) set in your [WorldEnvironment](class_worldenvironment.md#class_WorldEnvironment).

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_PSSM_SPLITS"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_PSSM_SPLITS** = `14`

Colors each PSSM split for the [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D) s in the scene a different color so you can see where the splits are. In order (from closest to furthest from the camera), they are colored red, green, blue, and yellow.

 **Note:** When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_DECAL_ATLAS"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_DECAL_ATLAS** = `15`

Draws the decal atlas that stores decal textures from [Decal](class_decal.md#class_Decal) s.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SDFGI"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_SDFGI** = `16`

Draws SDFGI cascade data. This is the data structure that is used to bounce lighting against and create reflections.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SDFGI_PROBES"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_SDFGI_PROBES** = `17`

Draws SDFGI probe data. This is the data structure that is used to give indirect lighting dynamic objects moving within the scene.

When in the editor, left-clicking a probe will display additional bright dots that show its occlusion information. A white dot means the light is not occluded at all at the dot's position, while a red dot means the light is fully occluded. Intermediate values are possible.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_GI_BUFFER"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_GI_BUFFER** = `18`

Draws the global illumination buffer from [VoxelGI](class_voxelgi.md#class_VoxelGI) or SDFGI. Requires [VoxelGI](class_voxelgi.md#class_VoxelGI) (at least one visible baked VoxelGI node) or SDFGI ([Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled)) to be enabled to have a visible effect.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_DISABLE_LOD"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_DISABLE_LOD** = `19`

Disable mesh LOD. All meshes are drawn with full detail, which can be used to compare performance.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_CLUSTER_OMNI_LIGHTS"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_CLUSTER_OMNI_LIGHTS** = `20`

Draws the [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) cluster. Clustering determines where lights are positioned in screen-space, which allows the engine to only process these portions of the screen for lighting.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_CLUSTER_SPOT_LIGHTS"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_CLUSTER_SPOT_LIGHTS** = `21`

Draws the [SpotLight3D](class_spotlight3d.md#class_SpotLight3D) cluster. Clustering determines where lights are positioned in screen-space, which allows the engine to only process these portions of the screen for lighting.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_CLUSTER_DECALS"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_CLUSTER_DECALS** = `22`

Draws the [Decal](class_decal.md#class_Decal) cluster. Clustering determines where decals are positioned in screen-space, which allows the engine to only process these portions of the screen for decals.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_CLUSTER_REFLECTION_PROBES"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_CLUSTER_REFLECTION_PROBES** = `23`

Draws the [ReflectionProbe](class_reflectionprobe.md#class_ReflectionProbe) cluster. Clustering determines where reflection probes are positioned in screen-space, which allows the engine to only process these portions of the screen for reflection probes.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_OCCLUDERS"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_OCCLUDERS** = `24`

Draws the occlusion culling buffer. This low-resolution occlusion culling buffer is rasterized on the CPU and is used to check whether instances are occluded by other objects.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_MOTION_VECTORS"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_MOTION_VECTORS** = `25`

Draws the motion vectors buffer. This is used by temporal antialiasing to correct for motion that occurs during gameplay.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_INTERNAL_BUFFER"></span>

[ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) **VIEWPORT_DEBUG_DRAW_INTERNAL_BUFFER** = `26`

Internal buffer is drawn instead of regular scene so you can see the per-pixel output that will be used by post-processing effects.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

---

<span id="enum_RenderingServer_ViewportVRSMode"></span>

enum **ViewportVRSMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportVRSMode)

<span id="class_RenderingServer_constant_VIEWPORT_VRS_DISABLED"></span>

[ViewportVRSMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSMode) **VIEWPORT_VRS_DISABLED** = `0`

Variable rate shading is disabled.

<span id="class_RenderingServer_constant_VIEWPORT_VRS_TEXTURE"></span>

[ViewportVRSMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSMode) **VIEWPORT_VRS_TEXTURE** = `1`

Variable rate shading uses a texture. Note, for stereoscopic use a texture atlas with a texture for each view.

<span id="class_RenderingServer_constant_VIEWPORT_VRS_XR"></span>

[ViewportVRSMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSMode) **VIEWPORT_VRS_XR** = `2`

Variable rate shading texture is supplied by the primary [XRInterface](class_xrinterface.md#class_XRInterface). Note that this may override the update mode.

<span id="class_RenderingServer_constant_VIEWPORT_VRS_MAX"></span>

[ViewportVRSMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSMode) **VIEWPORT_VRS_MAX** = `3`

Represents the size of the [ViewportVRSMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSMode) enum.

---

<span id="enum_RenderingServer_ViewportVRSUpdateMode"></span>

enum **ViewportVRSUpdateMode**: [🔗](class_renderingserver.md#enum_RenderingServer_ViewportVRSUpdateMode)

<span id="class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_DISABLED"></span>

[ViewportVRSUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSUpdateMode) **VIEWPORT_VRS_UPDATE_DISABLED** = `0`

The input texture for variable rate shading will not be processed.

<span id="class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_ONCE"></span>

[ViewportVRSUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSUpdateMode) **VIEWPORT_VRS_UPDATE_ONCE** = `1`

The input texture for variable rate shading will be processed once.

<span id="class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_ALWAYS"></span>

[ViewportVRSUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSUpdateMode) **VIEWPORT_VRS_UPDATE_ALWAYS** = `2`

The input texture for variable rate shading will be processed each frame.

<span id="class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_MAX"></span>

[ViewportVRSUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSUpdateMode) **VIEWPORT_VRS_UPDATE_MAX** = `3`

Represents the size of the [ViewportVRSUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSUpdateMode) enum.

---

<span id="enum_RenderingServer_SkyMode"></span>

enum **SkyMode**: [🔗](class_renderingserver.md#enum_RenderingServer_SkyMode)

<span id="class_RenderingServer_constant_SKY_MODE_AUTOMATIC"></span>

[SkyMode](class_renderingserver.md#enum_RenderingServer_SkyMode) **SKY_MODE_AUTOMATIC** = `0`

Automatically selects the appropriate process mode based on your sky shader. If your shader uses `TIME` or `POSITION`, this will use [SKY_MODE_REALTIME](class_renderingserver.md#class_RenderingServer_constant_SKY_MODE_REALTIME). If your shader uses any of the `LIGHT_*` variables or any custom uniforms, this uses [SKY_MODE_INCREMENTAL](class_renderingserver.md#class_RenderingServer_constant_SKY_MODE_INCREMENTAL). Otherwise, this defaults to [SKY_MODE_QUALITY](class_renderingserver.md#class_RenderingServer_constant_SKY_MODE_QUALITY).

<span id="class_RenderingServer_constant_SKY_MODE_QUALITY"></span>

[SkyMode](class_renderingserver.md#enum_RenderingServer_SkyMode) **SKY_MODE_QUALITY** = `1`

Uses high quality importance sampling to process the radiance map. In general, this results in much higher quality than [SKY_MODE_REALTIME](class_renderingserver.md#class_RenderingServer_constant_SKY_MODE_REALTIME) but takes much longer to generate. This should not be used if you plan on changing the sky at runtime. If you are finding that the reflection is not blurry enough and is showing sparkles or fireflies, try increasing ProjectSettings.rendering/reflections/sky_reflections/ggx_samples.

<span id="class_RenderingServer_constant_SKY_MODE_INCREMENTAL"></span>

[SkyMode](class_renderingserver.md#enum_RenderingServer_SkyMode) **SKY_MODE_INCREMENTAL** = `2`

Uses the same high quality importance sampling to process the radiance map as [SKY_MODE_QUALITY](class_renderingserver.md#class_RenderingServer_constant_SKY_MODE_QUALITY), but updates over several frames. The number of frames is determined by ProjectSettings.rendering/reflections/sky_reflections/roughness_layers. Use this when you need highest quality radiance maps, but have a sky that updates slowly.

<span id="class_RenderingServer_constant_SKY_MODE_REALTIME"></span>

[SkyMode](class_renderingserver.md#enum_RenderingServer_SkyMode) **SKY_MODE_REALTIME** = `3`

Uses the fast filtering algorithm to process the radiance map. In general this results in lower quality, but substantially faster run times. If you need better quality, but still need to update the sky every frame, consider turning on ProjectSettings.rendering/reflections/sky_reflections/fast_filter_high_quality.

 **Note:** The fast filtering algorithm is limited to 256×256 cubemaps, so [sky_set_radiance_size()](class_renderingserver.md#class_RenderingServer_method_sky_set_radiance_size) must be set to `256`. Otherwise, a warning is printed and the overridden radiance size is ignored.

---

<span id="enum_RenderingServer_CompositorEffectFlags"></span>

enum **CompositorEffectFlags**: [🔗](class_renderingserver.md#enum_RenderingServer_CompositorEffectFlags)

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_COLOR"></span>

[CompositorEffectFlags](class_renderingserver.md#enum_RenderingServer_CompositorEffectFlags) **COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_COLOR** = `1`

The rendering effect requires the color buffer to be resolved if MSAA is enabled.

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_DEPTH"></span>

[CompositorEffectFlags](class_renderingserver.md#enum_RenderingServer_CompositorEffectFlags) **COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_DEPTH** = `2`

The rendering effect requires the depth buffer to be resolved if MSAA is enabled.

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_NEEDS_MOTION_VECTORS"></span>

[CompositorEffectFlags](class_renderingserver.md#enum_RenderingServer_CompositorEffectFlags) **COMPOSITOR_EFFECT_FLAG_NEEDS_MOTION_VECTORS** = `4`

The rendering effect requires motion vectors to be produced.

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_NEEDS_ROUGHNESS"></span>

[CompositorEffectFlags](class_renderingserver.md#enum_RenderingServer_CompositorEffectFlags) **COMPOSITOR_EFFECT_FLAG_NEEDS_ROUGHNESS** = `8`

The rendering effect requires normals and roughness g-buffer to be produced (Forward+ only).

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_NEEDS_SEPARATE_SPECULAR"></span>

[CompositorEffectFlags](class_renderingserver.md#enum_RenderingServer_CompositorEffectFlags) **COMPOSITOR_EFFECT_FLAG_NEEDS_SEPARATE_SPECULAR** = `16`

The rendering effect requires specular data to be separated out (Forward+ only).

---

<span id="enum_RenderingServer_CompositorEffectCallbackType"></span>

enum **CompositorEffectCallbackType**: [🔗](class_renderingserver.md#enum_RenderingServer_CompositorEffectCallbackType)

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_OPAQUE"></span>

[CompositorEffectCallbackType](class_renderingserver.md#enum_RenderingServer_CompositorEffectCallbackType) **COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_OPAQUE** = `0`

The callback is called before our opaque rendering pass, but after depth prepass (if applicable).

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_OPAQUE"></span>

[CompositorEffectCallbackType](class_renderingserver.md#enum_RenderingServer_CompositorEffectCallbackType) **COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_OPAQUE** = `1`

The callback is called after our opaque rendering pass, but before our sky is rendered.

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_SKY"></span>

[CompositorEffectCallbackType](class_renderingserver.md#enum_RenderingServer_CompositorEffectCallbackType) **COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_SKY** = `2`

The callback is called after our sky is rendered, but before our back buffers are created (and if enabled, before subsurface scattering and/or screen space reflections).

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_TRANSPARENT"></span>

[CompositorEffectCallbackType](class_renderingserver.md#enum_RenderingServer_CompositorEffectCallbackType) **COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_TRANSPARENT** = `3`

The callback is called before our transparent rendering pass, but after our sky is rendered and we've created our back buffers.

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_TRANSPARENT"></span>

[CompositorEffectCallbackType](class_renderingserver.md#enum_RenderingServer_CompositorEffectCallbackType) **COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_TRANSPARENT** = `4`

The callback is called after our transparent rendering pass, but before any built-in post-processing effects and output to our render target.

<span id="class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_ANY"></span>

[CompositorEffectCallbackType](class_renderingserver.md#enum_RenderingServer_CompositorEffectCallbackType) **COMPOSITOR_EFFECT_CALLBACK_TYPE_ANY** = `-1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

<span id="enum_RenderingServer_EnvironmentBG"></span>

enum **EnvironmentBG**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentBG)

<span id="class_RenderingServer_constant_ENV_BG_CLEAR_COLOR"></span>

[EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) **ENV_BG_CLEAR_COLOR** = `0`

Use the clear color as background.

<span id="class_RenderingServer_constant_ENV_BG_COLOR"></span>

[EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) **ENV_BG_COLOR** = `1`

Use a specified color as the background.

<span id="class_RenderingServer_constant_ENV_BG_SKY"></span>

[EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) **ENV_BG_SKY** = `2`

Use a sky resource for the background.

<span id="class_RenderingServer_constant_ENV_BG_CANVAS"></span>

[EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) **ENV_BG_CANVAS** = `3`

Use a specified canvas layer as the background. This can be useful for instantiating a 2D scene in a 3D world.

<span id="class_RenderingServer_constant_ENV_BG_KEEP"></span>

[EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) **ENV_BG_KEEP** = `4`

Do not clear the background, use whatever was rendered last frame as the background.

<span id="class_RenderingServer_constant_ENV_BG_CAMERA_FEED"></span>

[EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) **ENV_BG_CAMERA_FEED** = `5`

Displays a camera feed in the background.

<span id="class_RenderingServer_constant_ENV_BG_MAX"></span>

[EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) **ENV_BG_MAX** = `6`

Represents the size of the [EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) enum.

---

<span id="enum_RenderingServer_EnvironmentAmbientSource"></span>

enum **EnvironmentAmbientSource**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentAmbientSource)

<span id="class_RenderingServer_constant_ENV_AMBIENT_SOURCE_BG"></span>

[EnvironmentAmbientSource](class_renderingserver.md#enum_RenderingServer_EnvironmentAmbientSource) **ENV_AMBIENT_SOURCE_BG** = `0`

Gather ambient light from whichever source is specified as the background.

<span id="class_RenderingServer_constant_ENV_AMBIENT_SOURCE_DISABLED"></span>

[EnvironmentAmbientSource](class_renderingserver.md#enum_RenderingServer_EnvironmentAmbientSource) **ENV_AMBIENT_SOURCE_DISABLED** = `1`

Disable ambient light.

<span id="class_RenderingServer_constant_ENV_AMBIENT_SOURCE_COLOR"></span>

[EnvironmentAmbientSource](class_renderingserver.md#enum_RenderingServer_EnvironmentAmbientSource) **ENV_AMBIENT_SOURCE_COLOR** = `2`

Specify a specific [Color](class_color.md#class_Color) for ambient light.

<span id="class_RenderingServer_constant_ENV_AMBIENT_SOURCE_SKY"></span>

[EnvironmentAmbientSource](class_renderingserver.md#enum_RenderingServer_EnvironmentAmbientSource) **ENV_AMBIENT_SOURCE_SKY** = `3`

Gather ambient light from the [Sky](class_sky.md#class_Sky) regardless of what the background is.

---

<span id="enum_RenderingServer_EnvironmentReflectionSource"></span>

enum **EnvironmentReflectionSource**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentReflectionSource)

<span id="class_RenderingServer_constant_ENV_REFLECTION_SOURCE_BG"></span>

[EnvironmentReflectionSource](class_renderingserver.md#enum_RenderingServer_EnvironmentReflectionSource) **ENV_REFLECTION_SOURCE_BG** = `0`

Use the background for reflections.

<span id="class_RenderingServer_constant_ENV_REFLECTION_SOURCE_DISABLED"></span>

[EnvironmentReflectionSource](class_renderingserver.md#enum_RenderingServer_EnvironmentReflectionSource) **ENV_REFLECTION_SOURCE_DISABLED** = `1`

Disable reflections.

<span id="class_RenderingServer_constant_ENV_REFLECTION_SOURCE_SKY"></span>

[EnvironmentReflectionSource](class_renderingserver.md#enum_RenderingServer_EnvironmentReflectionSource) **ENV_REFLECTION_SOURCE_SKY** = `2`

Use the [Sky](class_sky.md#class_Sky) for reflections regardless of what the background is.

---

<span id="enum_RenderingServer_EnvironmentGlowBlendMode"></span>

enum **EnvironmentGlowBlendMode**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentGlowBlendMode)

<span id="class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_ADDITIVE"></span>

[EnvironmentGlowBlendMode](class_renderingserver.md#enum_RenderingServer_EnvironmentGlowBlendMode) **ENV_GLOW_BLEND_MODE_ADDITIVE** = `0`

Adds the glow effect to the scene.

<span id="class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_SCREEN"></span>

[EnvironmentGlowBlendMode](class_renderingserver.md#enum_RenderingServer_EnvironmentGlowBlendMode) **ENV_GLOW_BLEND_MODE_SCREEN** = `1`

Adds the glow effect to the scene after modifying the glow influence based on the scene value; dark values will be highly influenced by glow and bright values will not be influenced by glow. This approach avoids bright values becoming overly bright from the glow effect. [Environment.tonemap_white](class_environment.md#class_Environment_property_tonemap_white) is used to determine the maximum scene value where the glow should have no influence. When [Environment.tonemap_mode](class_environment.md#class_Environment_property_tonemap_mode) is set to [Environment.TONE_MAPPER_LINEAR](class_environment.md#class_Environment_constant_TONE_MAPPER_LINEAR) and [Viewport.use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d) is `true`, the parent window's [Window.get_output_max_linear_value()](class_window.md#class_Window_method_get_output_max_linear_value) will be used as the maximum scene value.

<span id="class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_SOFTLIGHT"></span>

[EnvironmentGlowBlendMode](class_renderingserver.md#enum_RenderingServer_EnvironmentGlowBlendMode) **ENV_GLOW_BLEND_MODE_SOFTLIGHT** = `2`

Adds the glow effect to the tonemapped image after modifying the glow influence based on the image value; dark values and bright values will not be influenced by glow and mid-range values will be highly influenced by glow. This approach avoids bright values becoming overly bright from the glow effect. The glow will have the largest influence on image values of `0.25` and will have no influence when applied to image values greater than `1.0`.

 **Note:** This blend mode does not support HDR output because expects a maximum output value of `1.0`. It is recommended to use a different blend mode when rendering to an HDR screen.

<span id="class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_REPLACE"></span>

[EnvironmentGlowBlendMode](class_renderingserver.md#enum_RenderingServer_EnvironmentGlowBlendMode) **ENV_GLOW_BLEND_MODE_REPLACE** = `3`

Replaces all pixels' color by the glow effect. This can be used to simulate a full-screen blur effect by tweaking the glow parameters to match the original image's brightness or to preview glow configuration in the editor.

<span id="class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_MIX"></span>

[EnvironmentGlowBlendMode](class_renderingserver.md#enum_RenderingServer_EnvironmentGlowBlendMode) **ENV_GLOW_BLEND_MODE_MIX** = `4`

Mixes the glow image with the scene image. Best used with [Environment.glow_bloom](class_environment.md#class_Environment_property_glow_bloom) to avoid darkening the scene.

---

<span id="enum_RenderingServer_EnvironmentFogMode"></span>

enum **EnvironmentFogMode**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentFogMode)

<span id="class_RenderingServer_constant_ENV_FOG_MODE_EXPONENTIAL"></span>

[EnvironmentFogMode](class_renderingserver.md#enum_RenderingServer_EnvironmentFogMode) **ENV_FOG_MODE_EXPONENTIAL** = `0`

Use a physically-based fog model defined primarily by fog density.

<span id="class_RenderingServer_constant_ENV_FOG_MODE_DEPTH"></span>

[EnvironmentFogMode](class_renderingserver.md#enum_RenderingServer_EnvironmentFogMode) **ENV_FOG_MODE_DEPTH** = `1`

Use a simple fog model defined by start and end positions and a custom curve. While not physically accurate, this model can be useful when you need more artistic control.

---

<span id="enum_RenderingServer_EnvironmentToneMapper"></span>

enum **EnvironmentToneMapper**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentToneMapper)

<span id="class_RenderingServer_constant_ENV_TONE_MAPPER_LINEAR"></span>

[EnvironmentToneMapper](class_renderingserver.md#enum_RenderingServer_EnvironmentToneMapper) **ENV_TONE_MAPPER_LINEAR** = `0`

Does not modify color data, resulting in a linear tonemapping curve which unnaturally clips bright values, causing bright lighting to look blown out. The simplest and fastest tonemapper.

<span id="class_RenderingServer_constant_ENV_TONE_MAPPER_REINHARD"></span>

[EnvironmentToneMapper](class_renderingserver.md#enum_RenderingServer_EnvironmentToneMapper) **ENV_TONE_MAPPER_REINHARD** = `1`

A simple tonemapping curve that rolls off bright values to prevent clipping. This results in an image that can appear dull and low contrast. Slower than [ENV_TONE_MAPPER_LINEAR](class_renderingserver.md#class_RenderingServer_constant_ENV_TONE_MAPPER_LINEAR).

 **Note:** When [Environment.tonemap_white](class_environment.md#class_Environment_property_tonemap_white) is left at the default value of `1.0`, [ENV_TONE_MAPPER_REINHARD](class_renderingserver.md#class_RenderingServer_constant_ENV_TONE_MAPPER_REINHARD) produces an identical image to [ENV_TONE_MAPPER_LINEAR](class_renderingserver.md#class_RenderingServer_constant_ENV_TONE_MAPPER_LINEAR).

<span id="class_RenderingServer_constant_ENV_TONE_MAPPER_FILMIC"></span>

[EnvironmentToneMapper](class_renderingserver.md#enum_RenderingServer_EnvironmentToneMapper) **ENV_TONE_MAPPER_FILMIC** = `2`

Uses a film-like tonemapping curve to prevent clipping of bright values and provide better contrast than [ENV_TONE_MAPPER_REINHARD](class_renderingserver.md#class_RenderingServer_constant_ENV_TONE_MAPPER_REINHARD). Slightly slower than [ENV_TONE_MAPPER_REINHARD](class_renderingserver.md#class_RenderingServer_constant_ENV_TONE_MAPPER_REINHARD).

 **Note:** This tonemapper does not support HDR output because it produces output in the SDR range. It is recommended to use a different tonemapper when rendering to an HDR screen.

<span id="class_RenderingServer_constant_ENV_TONE_MAPPER_ACES"></span>

[EnvironmentToneMapper](class_renderingserver.md#enum_RenderingServer_EnvironmentToneMapper) **ENV_TONE_MAPPER_ACES** = `3`

Uses a high-contrast film-like tonemapping curve and desaturates bright values for a more realistic appearance. Slightly slower than [ENV_TONE_MAPPER_FILMIC](class_renderingserver.md#class_RenderingServer_constant_ENV_TONE_MAPPER_FILMIC).

 **Note:** This tonemapping operator is called "ACES Fitted" in Godot 3.x.

 **Note:** This tonemapper does not support HDR output because it produces output in the SDR range. It is recommended to use a different tonemapper when rendering to an HDR screen.

<span id="class_RenderingServer_constant_ENV_TONE_MAPPER_AGX"></span>

[EnvironmentToneMapper](class_renderingserver.md#enum_RenderingServer_EnvironmentToneMapper) **ENV_TONE_MAPPER_AGX** = `4`

Uses an adjustable film-like tonemapping curve and desaturates bright values for a more realistic appearance. Better than other tonemappers at maintaining the hue of colors as they become brighter. The slowest tonemapping option.

---

<span id="enum_RenderingServer_EnvironmentSSRRoughnessQuality"></span>

enum **EnvironmentSSRRoughnessQuality**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentSSRRoughnessQuality)

<span id="class_RenderingServer_constant_ENV_SSR_ROUGHNESS_QUALITY_DISABLED"></span>

[EnvironmentSSRRoughnessQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSRRoughnessQuality) **ENV_SSR_ROUGHNESS_QUALITY_DISABLED** = `0`

Lowest quality of roughness filter for screen-space reflections. Rough materials will not have blurrier screen-space reflections compared to smooth (non-rough) materials. This is the fastest option.

<span id="class_RenderingServer_constant_ENV_SSR_ROUGHNESS_QUALITY_LOW"></span>

[EnvironmentSSRRoughnessQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSRRoughnessQuality) **ENV_SSR_ROUGHNESS_QUALITY_LOW** = `1`

Low quality of roughness filter for screen-space reflections.

<span id="class_RenderingServer_constant_ENV_SSR_ROUGHNESS_QUALITY_MEDIUM"></span>

[EnvironmentSSRRoughnessQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSRRoughnessQuality) **ENV_SSR_ROUGHNESS_QUALITY_MEDIUM** = `2`

Medium quality of roughness filter for screen-space reflections.

<span id="class_RenderingServer_constant_ENV_SSR_ROUGHNESS_QUALITY_HIGH"></span>

[EnvironmentSSRRoughnessQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSRRoughnessQuality) **ENV_SSR_ROUGHNESS_QUALITY_HIGH** = `3`

High quality of roughness filter for screen-space reflections. This is the slowest option.

---

<span id="enum_RenderingServer_EnvironmentSSAOQuality"></span>

enum **EnvironmentSSAOQuality**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentSSAOQuality)

<span id="class_RenderingServer_constant_ENV_SSAO_QUALITY_VERY_LOW"></span>

[EnvironmentSSAOQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSAOQuality) **ENV_SSAO_QUALITY_VERY_LOW** = `0`

Lowest quality of screen-space ambient occlusion.

<span id="class_RenderingServer_constant_ENV_SSAO_QUALITY_LOW"></span>

[EnvironmentSSAOQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSAOQuality) **ENV_SSAO_QUALITY_LOW** = `1`

Low quality screen-space ambient occlusion.

<span id="class_RenderingServer_constant_ENV_SSAO_QUALITY_MEDIUM"></span>

[EnvironmentSSAOQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSAOQuality) **ENV_SSAO_QUALITY_MEDIUM** = `2`

Medium quality screen-space ambient occlusion.

<span id="class_RenderingServer_constant_ENV_SSAO_QUALITY_HIGH"></span>

[EnvironmentSSAOQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSAOQuality) **ENV_SSAO_QUALITY_HIGH** = `3`

High quality screen-space ambient occlusion.

<span id="class_RenderingServer_constant_ENV_SSAO_QUALITY_ULTRA"></span>

[EnvironmentSSAOQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSAOQuality) **ENV_SSAO_QUALITY_ULTRA** = `4`

Highest quality screen-space ambient occlusion. Uses the adaptive target setting which can be dynamically adjusted to smoothly balance performance and visual quality.

---

<span id="enum_RenderingServer_EnvironmentSSILQuality"></span>

enum **EnvironmentSSILQuality**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentSSILQuality)

<span id="class_RenderingServer_constant_ENV_SSIL_QUALITY_VERY_LOW"></span>

[EnvironmentSSILQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSILQuality) **ENV_SSIL_QUALITY_VERY_LOW** = `0`

Lowest quality of screen-space indirect lighting.

<span id="class_RenderingServer_constant_ENV_SSIL_QUALITY_LOW"></span>

[EnvironmentSSILQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSILQuality) **ENV_SSIL_QUALITY_LOW** = `1`

Low quality screen-space indirect lighting.

<span id="class_RenderingServer_constant_ENV_SSIL_QUALITY_MEDIUM"></span>

[EnvironmentSSILQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSILQuality) **ENV_SSIL_QUALITY_MEDIUM** = `2`

High quality screen-space indirect lighting.

<span id="class_RenderingServer_constant_ENV_SSIL_QUALITY_HIGH"></span>

[EnvironmentSSILQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSILQuality) **ENV_SSIL_QUALITY_HIGH** = `3`

High quality screen-space indirect lighting.

<span id="class_RenderingServer_constant_ENV_SSIL_QUALITY_ULTRA"></span>

[EnvironmentSSILQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSILQuality) **ENV_SSIL_QUALITY_ULTRA** = `4`

Highest quality screen-space indirect lighting. Uses the adaptive target setting which can be dynamically adjusted to smoothly balance performance and visual quality.

---

<span id="enum_RenderingServer_EnvironmentSDFGIYScale"></span>

enum **EnvironmentSDFGIYScale**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIYScale)

<span id="class_RenderingServer_constant_ENV_SDFGI_Y_SCALE_50_PERCENT"></span>

[EnvironmentSDFGIYScale](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIYScale) **ENV_SDFGI_Y_SCALE_50_PERCENT** = `0`

Use 50% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be twice as short as they are wide. This allows providing increased GI detail and reduced light leaking with thin floors and ceilings. This is usually the best choice for scenes that don't feature much verticality.

<span id="class_RenderingServer_constant_ENV_SDFGI_Y_SCALE_75_PERCENT"></span>

[EnvironmentSDFGIYScale](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIYScale) **ENV_SDFGI_Y_SCALE_75_PERCENT** = `1`

Use 75% scale for SDFGI on the Y (vertical) axis. This is a balance between the 50% and 100% SDFGI Y scales.

<span id="class_RenderingServer_constant_ENV_SDFGI_Y_SCALE_100_PERCENT"></span>

[EnvironmentSDFGIYScale](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIYScale) **ENV_SDFGI_Y_SCALE_100_PERCENT** = `2`

Use 100% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be as tall as they are wide. This is usually the best choice for highly vertical scenes. The downside is that light leaking may become more noticeable with thin floors and ceilings.

---

<span id="enum_RenderingServer_EnvironmentSDFGIRayCount"></span>

enum **EnvironmentSDFGIRayCount**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount)

<span id="class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_4"></span>

[EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) **ENV_SDFGI_RAY_COUNT_4** = `0`

Throw 4 rays per frame when converging SDFGI. This has the lowest GPU requirements, but creates the most noisy result.

<span id="class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_8"></span>

[EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) **ENV_SDFGI_RAY_COUNT_8** = `1`

Throw 8 rays per frame when converging SDFGI.

<span id="class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_16"></span>

[EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) **ENV_SDFGI_RAY_COUNT_16** = `2`

Throw 16 rays per frame when converging SDFGI.

<span id="class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_32"></span>

[EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) **ENV_SDFGI_RAY_COUNT_32** = `3`

Throw 32 rays per frame when converging SDFGI.

<span id="class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_64"></span>

[EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) **ENV_SDFGI_RAY_COUNT_64** = `4`

Throw 64 rays per frame when converging SDFGI.

<span id="class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_96"></span>

[EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) **ENV_SDFGI_RAY_COUNT_96** = `5`

Throw 96 rays per frame when converging SDFGI. This has high GPU requirements.

<span id="class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_128"></span>

[EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) **ENV_SDFGI_RAY_COUNT_128** = `6`

Throw 128 rays per frame when converging SDFGI. This has very high GPU requirements, but creates the least noisy result.

<span id="class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_MAX"></span>

[EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) **ENV_SDFGI_RAY_COUNT_MAX** = `7`

Represents the size of the [EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) enum.

---

<span id="enum_RenderingServer_EnvironmentSDFGIFramesToConverge"></span>

enum **EnvironmentSDFGIFramesToConverge**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge)

<span id="class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_5_FRAMES"></span>

[EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) **ENV_SDFGI_CONVERGE_IN_5_FRAMES** = `0`

Converge SDFGI over 5 frames. This is the most responsive, but creates the most noisy result with a given ray count.

<span id="class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_10_FRAMES"></span>

[EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) **ENV_SDFGI_CONVERGE_IN_10_FRAMES** = `1`

Configure SDFGI to fully converge over 10 frames.

<span id="class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_15_FRAMES"></span>

[EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) **ENV_SDFGI_CONVERGE_IN_15_FRAMES** = `2`

Configure SDFGI to fully converge over 15 frames.

<span id="class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_20_FRAMES"></span>

[EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) **ENV_SDFGI_CONVERGE_IN_20_FRAMES** = `3`

Configure SDFGI to fully converge over 20 frames.

<span id="class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_25_FRAMES"></span>

[EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) **ENV_SDFGI_CONVERGE_IN_25_FRAMES** = `4`

Configure SDFGI to fully converge over 25 frames.

<span id="class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_30_FRAMES"></span>

[EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) **ENV_SDFGI_CONVERGE_IN_30_FRAMES** = `5`

Configure SDFGI to fully converge over 30 frames. This is the least responsive, but creates the least noisy result with a given ray count.

<span id="class_RenderingServer_constant_ENV_SDFGI_CONVERGE_MAX"></span>

[EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) **ENV_SDFGI_CONVERGE_MAX** = `6`

Represents the size of the [EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) enum.

---

<span id="enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight"></span>

enum **EnvironmentSDFGIFramesToUpdateLight**: [🔗](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight)

<span id="class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_1_FRAME"></span>

[EnvironmentSDFGIFramesToUpdateLight](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight) **ENV_SDFGI_UPDATE_LIGHT_IN_1_FRAME** = `0`

Update indirect light from dynamic lights in SDFGI over 1 frame. This is the most responsive, but has the highest GPU requirements.

<span id="class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_2_FRAMES"></span>

[EnvironmentSDFGIFramesToUpdateLight](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight) **ENV_SDFGI_UPDATE_LIGHT_IN_2_FRAMES** = `1`

Update indirect light from dynamic lights in SDFGI over 2 frames.

<span id="class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_4_FRAMES"></span>

[EnvironmentSDFGIFramesToUpdateLight](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight) **ENV_SDFGI_UPDATE_LIGHT_IN_4_FRAMES** = `2`

Update indirect light from dynamic lights in SDFGI over 4 frames.

<span id="class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_8_FRAMES"></span>

[EnvironmentSDFGIFramesToUpdateLight](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight) **ENV_SDFGI_UPDATE_LIGHT_IN_8_FRAMES** = `3`

Update indirect light from dynamic lights in SDFGI over 8 frames.

<span id="class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_16_FRAMES"></span>

[EnvironmentSDFGIFramesToUpdateLight](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight) **ENV_SDFGI_UPDATE_LIGHT_IN_16_FRAMES** = `4`

Update indirect light from dynamic lights in SDFGI over 16 frames. This is the least responsive, but has the lowest GPU requirements.

<span id="class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_MAX"></span>

[EnvironmentSDFGIFramesToUpdateLight](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight) **ENV_SDFGI_UPDATE_LIGHT_MAX** = `5`

Represents the size of the [EnvironmentSDFGIFramesToUpdateLight](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight) enum.

---

<span id="enum_RenderingServer_SubSurfaceScatteringQuality"></span>

enum **SubSurfaceScatteringQuality**: [🔗](class_renderingserver.md#enum_RenderingServer_SubSurfaceScatteringQuality)

<span id="class_RenderingServer_constant_SUB_SURFACE_SCATTERING_QUALITY_DISABLED"></span>

[SubSurfaceScatteringQuality](class_renderingserver.md#enum_RenderingServer_SubSurfaceScatteringQuality) **SUB_SURFACE_SCATTERING_QUALITY_DISABLED** = `0`

Disables subsurface scattering entirely, even on materials that have [BaseMaterial3D.subsurf_scatter_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_enabled) set to `true`. This has the lowest GPU requirements.

<span id="class_RenderingServer_constant_SUB_SURFACE_SCATTERING_QUALITY_LOW"></span>

[SubSurfaceScatteringQuality](class_renderingserver.md#enum_RenderingServer_SubSurfaceScatteringQuality) **SUB_SURFACE_SCATTERING_QUALITY_LOW** = `1`

Low subsurface scattering quality.

<span id="class_RenderingServer_constant_SUB_SURFACE_SCATTERING_QUALITY_MEDIUM"></span>

[SubSurfaceScatteringQuality](class_renderingserver.md#enum_RenderingServer_SubSurfaceScatteringQuality) **SUB_SURFACE_SCATTERING_QUALITY_MEDIUM** = `2`

Medium subsurface scattering quality.

<span id="class_RenderingServer_constant_SUB_SURFACE_SCATTERING_QUALITY_HIGH"></span>

[SubSurfaceScatteringQuality](class_renderingserver.md#enum_RenderingServer_SubSurfaceScatteringQuality) **SUB_SURFACE_SCATTERING_QUALITY_HIGH** = `3`

High subsurface scattering quality. This has the highest GPU requirements.

---

<span id="enum_RenderingServer_DOFBokehShape"></span>

enum **DOFBokehShape**: [🔗](class_renderingserver.md#enum_RenderingServer_DOFBokehShape)

<span id="class_RenderingServer_constant_DOF_BOKEH_BOX"></span>

[DOFBokehShape](class_renderingserver.md#enum_RenderingServer_DOFBokehShape) **DOF_BOKEH_BOX** = `0`

Calculate the DOF blur using a box filter. The fastest option, but results in obvious lines in blur pattern.

<span id="class_RenderingServer_constant_DOF_BOKEH_HEXAGON"></span>

[DOFBokehShape](class_renderingserver.md#enum_RenderingServer_DOFBokehShape) **DOF_BOKEH_HEXAGON** = `1`

Calculates DOF blur using a hexagon shaped filter.

<span id="class_RenderingServer_constant_DOF_BOKEH_CIRCLE"></span>

[DOFBokehShape](class_renderingserver.md#enum_RenderingServer_DOFBokehShape) **DOF_BOKEH_CIRCLE** = `2`

Calculates DOF blur using a circle shaped filter. Best quality and most realistic, but slowest. Use only for areas where a lot of performance can be dedicated to post-processing (e.g. cutscenes).

---

<span id="enum_RenderingServer_DOFBlurQuality"></span>

enum **DOFBlurQuality**: [🔗](class_renderingserver.md#enum_RenderingServer_DOFBlurQuality)

<span id="class_RenderingServer_constant_DOF_BLUR_QUALITY_VERY_LOW"></span>

[DOFBlurQuality](class_renderingserver.md#enum_RenderingServer_DOFBlurQuality) **DOF_BLUR_QUALITY_VERY_LOW** = `0`

Lowest quality DOF blur. This is the fastest setting, but you may be able to see filtering artifacts.

<span id="class_RenderingServer_constant_DOF_BLUR_QUALITY_LOW"></span>

[DOFBlurQuality](class_renderingserver.md#enum_RenderingServer_DOFBlurQuality) **DOF_BLUR_QUALITY_LOW** = `1`

Low quality DOF blur.

<span id="class_RenderingServer_constant_DOF_BLUR_QUALITY_MEDIUM"></span>

[DOFBlurQuality](class_renderingserver.md#enum_RenderingServer_DOFBlurQuality) **DOF_BLUR_QUALITY_MEDIUM** = `2`

Medium quality DOF blur.

<span id="class_RenderingServer_constant_DOF_BLUR_QUALITY_HIGH"></span>

[DOFBlurQuality](class_renderingserver.md#enum_RenderingServer_DOFBlurQuality) **DOF_BLUR_QUALITY_HIGH** = `3`

Highest quality DOF blur. Results in the smoothest looking blur by taking the most samples, but is also significantly slower.

---

<span id="enum_RenderingServer_InstanceType"></span>

enum **InstanceType**: [🔗](class_renderingserver.md#enum_RenderingServer_InstanceType)

<span id="class_RenderingServer_constant_INSTANCE_NONE"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_NONE** = `0`

The instance does not have a type.

<span id="class_RenderingServer_constant_INSTANCE_MESH"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_MESH** = `1`

The instance is a mesh.

<span id="class_RenderingServer_constant_INSTANCE_MULTIMESH"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_MULTIMESH** = `2`

The instance is a multimesh.

<span id="class_RenderingServer_constant_INSTANCE_PARTICLES"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_PARTICLES** = `3`

The instance is a particle emitter.

<span id="class_RenderingServer_constant_INSTANCE_PARTICLES_COLLISION"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_PARTICLES_COLLISION** = `4`

The instance is a GPUParticles collision shape.

<span id="class_RenderingServer_constant_INSTANCE_LIGHT"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_LIGHT** = `5`

The instance is a light.

<span id="class_RenderingServer_constant_INSTANCE_REFLECTION_PROBE"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_REFLECTION_PROBE** = `6`

The instance is a reflection probe.

<span id="class_RenderingServer_constant_INSTANCE_DECAL"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_DECAL** = `7`

The instance is a decal.

<span id="class_RenderingServer_constant_INSTANCE_VOXEL_GI"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_VOXEL_GI** = `8`

The instance is a VoxelGI.

<span id="class_RenderingServer_constant_INSTANCE_LIGHTMAP"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_LIGHTMAP** = `9`

The instance is a lightmap.

<span id="class_RenderingServer_constant_INSTANCE_OCCLUDER"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_OCCLUDER** = `10`

The instance is an occlusion culling occluder.

<span id="class_RenderingServer_constant_INSTANCE_VISIBLITY_NOTIFIER"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_VISIBLITY_NOTIFIER** = `11`

The instance is a visible on-screen notifier.

<span id="class_RenderingServer_constant_INSTANCE_FOG_VOLUME"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_FOG_VOLUME** = `12`

The instance is a fog volume.

<span id="class_RenderingServer_constant_INSTANCE_MAX"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_MAX** = `13`

Represents the size of the [InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) enum.

<span id="class_RenderingServer_constant_INSTANCE_GEOMETRY_MASK"></span>

[InstanceType](class_renderingserver.md#enum_RenderingServer_InstanceType) **INSTANCE_GEOMETRY_MASK** = `14`

A combination of the flags of geometry instances (mesh, multimesh, immediate and particles).

---

<span id="enum_RenderingServer_InstanceFlags"></span>

enum **InstanceFlags**: [🔗](class_renderingserver.md#enum_RenderingServer_InstanceFlags)

<span id="class_RenderingServer_constant_INSTANCE_FLAG_USE_BAKED_LIGHT"></span>

[InstanceFlags](class_renderingserver.md#enum_RenderingServer_InstanceFlags) **INSTANCE_FLAG_USE_BAKED_LIGHT** = `0`

Allows the instance to be used in baked lighting.

<span id="class_RenderingServer_constant_INSTANCE_FLAG_USE_DYNAMIC_GI"></span>

[InstanceFlags](class_renderingserver.md#enum_RenderingServer_InstanceFlags) **INSTANCE_FLAG_USE_DYNAMIC_GI** = `1`

Allows the instance to be used with dynamic global illumination.

<span id="class_RenderingServer_constant_INSTANCE_FLAG_DRAW_NEXT_FRAME_IF_VISIBLE"></span>

[InstanceFlags](class_renderingserver.md#enum_RenderingServer_InstanceFlags) **INSTANCE_FLAG_DRAW_NEXT_FRAME_IF_VISIBLE** = `2`

When set, manually requests to draw geometry on next frame.

<span id="class_RenderingServer_constant_INSTANCE_FLAG_IGNORE_OCCLUSION_CULLING"></span>

[InstanceFlags](class_renderingserver.md#enum_RenderingServer_InstanceFlags) **INSTANCE_FLAG_IGNORE_OCCLUSION_CULLING** = `3`

Always draw, even if the instance would be culled by occlusion culling. Does not affect view frustum culling.

<span id="class_RenderingServer_constant_INSTANCE_FLAG_MAX"></span>

[InstanceFlags](class_renderingserver.md#enum_RenderingServer_InstanceFlags) **INSTANCE_FLAG_MAX** = `4`

Represents the size of the [InstanceFlags](class_renderingserver.md#enum_RenderingServer_InstanceFlags) enum.

---

<span id="enum_RenderingServer_ShadowCastingSetting"></span>

enum **ShadowCastingSetting**: [🔗](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting)

<span id="class_RenderingServer_constant_SHADOW_CASTING_SETTING_OFF"></span>

[ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) **SHADOW_CASTING_SETTING_OFF** = `0`

Disable shadows from this instance.

<span id="class_RenderingServer_constant_SHADOW_CASTING_SETTING_ON"></span>

[ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) **SHADOW_CASTING_SETTING_ON** = `1`

Cast shadows from this instance.

<span id="class_RenderingServer_constant_SHADOW_CASTING_SETTING_DOUBLE_SIDED"></span>

[ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) **SHADOW_CASTING_SETTING_DOUBLE_SIDED** = `2`

Disable backface culling when rendering the shadow of the object. This is slightly slower but may result in more correct shadows.

<span id="class_RenderingServer_constant_SHADOW_CASTING_SETTING_SHADOWS_ONLY"></span>

[ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) **SHADOW_CASTING_SETTING_SHADOWS_ONLY** = `3`

Only render the shadows from the object. The object itself will not be drawn.

---

<span id="enum_RenderingServer_VisibilityRangeFadeMode"></span>

enum **VisibilityRangeFadeMode**: [🔗](class_renderingserver.md#enum_RenderingServer_VisibilityRangeFadeMode)

<span id="class_RenderingServer_constant_VISIBILITY_RANGE_FADE_DISABLED"></span>

[VisibilityRangeFadeMode](class_renderingserver.md#enum_RenderingServer_VisibilityRangeFadeMode) **VISIBILITY_RANGE_FADE_DISABLED** = `0`

Disable visibility range fading for the given instance.

<span id="class_RenderingServer_constant_VISIBILITY_RANGE_FADE_SELF"></span>

[VisibilityRangeFadeMode](class_renderingserver.md#enum_RenderingServer_VisibilityRangeFadeMode) **VISIBILITY_RANGE_FADE_SELF** = `1`

Fade-out the given instance when it approaches its visibility range limits.

<span id="class_RenderingServer_constant_VISIBILITY_RANGE_FADE_DEPENDENCIES"></span>

[VisibilityRangeFadeMode](class_renderingserver.md#enum_RenderingServer_VisibilityRangeFadeMode) **VISIBILITY_RANGE_FADE_DEPENDENCIES** = `2`

Fade-in the given instance's dependencies when reaching its visibility range limits.

---

<span id="enum_RenderingServer_BakeChannels"></span>

enum **BakeChannels**: [🔗](class_renderingserver.md#enum_RenderingServer_BakeChannels)

<span id="class_RenderingServer_constant_BAKE_CHANNEL_ALBEDO_ALPHA"></span>

[BakeChannels](class_renderingserver.md#enum_RenderingServer_BakeChannels) **BAKE_CHANNEL_ALBEDO_ALPHA** = `0`

Index of [Image](class_image.md#class_Image) in array of [Image](class_image.md#class_Image) s returned by [bake_render_uv2()](class_renderingserver.md#class_RenderingServer_method_bake_render_uv2). Image uses [Image.FORMAT_RGBA8](class_image.md#class_Image_constant_FORMAT_RGBA8) and contains albedo color in the `.rgb` channels and alpha in the `.a` channel.

<span id="class_RenderingServer_constant_BAKE_CHANNEL_NORMAL"></span>

[BakeChannels](class_renderingserver.md#enum_RenderingServer_BakeChannels) **BAKE_CHANNEL_NORMAL** = `1`

Index of [Image](class_image.md#class_Image) in array of [Image](class_image.md#class_Image) s returned by [bake_render_uv2()](class_renderingserver.md#class_RenderingServer_method_bake_render_uv2). Image uses [Image.FORMAT_RGBA8](class_image.md#class_Image_constant_FORMAT_RGBA8) and contains the per-pixel normal of the object in the `.rgb` channels and nothing in the `.a` channel. The per-pixel normal is encoded as `normal * 0.5 + 0.5`.

<span id="class_RenderingServer_constant_BAKE_CHANNEL_ORM"></span>

[BakeChannels](class_renderingserver.md#enum_RenderingServer_BakeChannels) **BAKE_CHANNEL_ORM** = `2`

Index of [Image](class_image.md#class_Image) in array of [Image](class_image.md#class_Image) s returned by [bake_render_uv2()](class_renderingserver.md#class_RenderingServer_method_bake_render_uv2). Image uses [Image.FORMAT_RGBA8](class_image.md#class_Image_constant_FORMAT_RGBA8) and contains ambient occlusion (from material and decals only) in the `.r` channel, roughness in the `.g` channel, metallic in the `.b` channel and sub surface scattering amount in the `.a` channel.

<span id="class_RenderingServer_constant_BAKE_CHANNEL_EMISSION"></span>

[BakeChannels](class_renderingserver.md#enum_RenderingServer_BakeChannels) **BAKE_CHANNEL_EMISSION** = `3`

Index of [Image](class_image.md#class_Image) in array of [Image](class_image.md#class_Image) s returned by [bake_render_uv2()](class_renderingserver.md#class_RenderingServer_method_bake_render_uv2). Image uses [Image.FORMAT_RGBAH](class_image.md#class_Image_constant_FORMAT_RGBAH) and contains emission color in the `.rgb` channels and nothing in the `.a` channel.

---

<span id="enum_RenderingServer_CanvasTextureChannel"></span>

enum **CanvasTextureChannel**: [🔗](class_renderingserver.md#enum_RenderingServer_CanvasTextureChannel)

<span id="class_RenderingServer_constant_CANVAS_TEXTURE_CHANNEL_DIFFUSE"></span>

[CanvasTextureChannel](class_renderingserver.md#enum_RenderingServer_CanvasTextureChannel) **CANVAS_TEXTURE_CHANNEL_DIFFUSE** = `0`

Diffuse canvas texture ([CanvasTexture.diffuse_texture](class_canvastexture.md#class_CanvasTexture_property_diffuse_texture)).

<span id="class_RenderingServer_constant_CANVAS_TEXTURE_CHANNEL_NORMAL"></span>

[CanvasTextureChannel](class_renderingserver.md#enum_RenderingServer_CanvasTextureChannel) **CANVAS_TEXTURE_CHANNEL_NORMAL** = `1`

Normal map canvas texture ([CanvasTexture.normal_texture](class_canvastexture.md#class_CanvasTexture_property_normal_texture)).

<span id="class_RenderingServer_constant_CANVAS_TEXTURE_CHANNEL_SPECULAR"></span>

[CanvasTextureChannel](class_renderingserver.md#enum_RenderingServer_CanvasTextureChannel) **CANVAS_TEXTURE_CHANNEL_SPECULAR** = `2`

Specular map canvas texture ([CanvasTexture.specular_texture](class_canvastexture.md#class_CanvasTexture_property_specular_texture)).

---

<span id="enum_RenderingServer_NinePatchAxisMode"></span>

enum **NinePatchAxisMode**: [🔗](class_renderingserver.md#enum_RenderingServer_NinePatchAxisMode)

<span id="class_RenderingServer_constant_NINE_PATCH_STRETCH"></span>

[NinePatchAxisMode](class_renderingserver.md#enum_RenderingServer_NinePatchAxisMode) **NINE_PATCH_STRETCH** = `0`

The nine patch gets stretched where needed.

<span id="class_RenderingServer_constant_NINE_PATCH_TILE"></span>

[NinePatchAxisMode](class_renderingserver.md#enum_RenderingServer_NinePatchAxisMode) **NINE_PATCH_TILE** = `1`

The nine patch gets filled with tiles where needed.

<span id="class_RenderingServer_constant_NINE_PATCH_TILE_FIT"></span>

[NinePatchAxisMode](class_renderingserver.md#enum_RenderingServer_NinePatchAxisMode) **NINE_PATCH_TILE_FIT** = `2`

The nine patch gets filled with tiles where needed and stretches them a bit if needed.

---

<span id="enum_RenderingServer_CanvasItemTextureFilter"></span>

enum **CanvasItemTextureFilter**: [🔗](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter)

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_DEFAULT"></span>

[CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) **CANVAS_ITEM_TEXTURE_FILTER_DEFAULT** = `0`

Uses the default filter mode for this [Viewport](class_viewport.md#class_Viewport).

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_NEAREST"></span>

[CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) **CANVAS_ITEM_TEXTURE_FILTER_NEAREST** = `1`

The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_LINEAR"></span>

[CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) **CANVAS_ITEM_TEXTURE_FILTER_LINEAR** = `2`

The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS"></span>

[CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) **CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS** = `3`

The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`). This makes the texture look pixelated from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class_Camera2D) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS"></span>

[CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) **CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS** = `4`

The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`). This makes the texture look smooth from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class_Camera2D) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC"></span>

[CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) **CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC** = `5`

The texture filter reads from the nearest pixel and blends between 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`) based on the angle between the surface and the camera view. This makes the texture look pixelated from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

 **Note:** This texture filter is rarely useful in 2D projects. [CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS](class_renderingserver.md#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS) is usually more appropriate in this case.

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC"></span>

[CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) **CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC** = `6`

The texture filter blends between the nearest 4 pixels and blends between 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`) based on the angle between the surface and the camera view. This makes the texture look smooth from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

 **Note:** This texture filter is rarely useful in 2D projects. [CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS](class_renderingserver.md#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS) is usually more appropriate in this case.

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_MAX"></span>

[CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) **CANVAS_ITEM_TEXTURE_FILTER_MAX** = `7`

Max value for [CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) enum.

---

<span id="enum_RenderingServer_CanvasItemTextureRepeat"></span>

enum **CanvasItemTextureRepeat**: [🔗](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat)

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_DEFAULT"></span>

[CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) **CANVAS_ITEM_TEXTURE_REPEAT_DEFAULT** = `0`

Uses the default repeat mode for this [Viewport](class_viewport.md#class_Viewport).

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_DISABLED"></span>

[CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) **CANVAS_ITEM_TEXTURE_REPEAT_DISABLED** = `1`

Disables textures repeating. Instead, when reading UVs outside the 0-1 range, the value will be clamped to the edge of the texture, resulting in a stretched out look at the borders of the texture.

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_ENABLED"></span>

[CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) **CANVAS_ITEM_TEXTURE_REPEAT_ENABLED** = `2`

Enables the texture to repeat when UV coordinates are outside the 0-1 range. If using one of the linear filtering modes, this can result in artifacts at the edges of a texture when the sampler filters across the edges of the texture.

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_MIRROR"></span>

[CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) **CANVAS_ITEM_TEXTURE_REPEAT_MIRROR** = `3`

Flip the texture when repeating so that the edge lines up instead of abruptly changing.

<span id="class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_MAX"></span>

[CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) **CANVAS_ITEM_TEXTURE_REPEAT_MAX** = `4`

Max value for [CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) enum.

---

<span id="enum_RenderingServer_CanvasGroupMode"></span>

enum **CanvasGroupMode**: [🔗](class_renderingserver.md#enum_RenderingServer_CanvasGroupMode)

<span id="class_RenderingServer_constant_CANVAS_GROUP_MODE_DISABLED"></span>

[CanvasGroupMode](class_renderingserver.md#enum_RenderingServer_CanvasGroupMode) **CANVAS_GROUP_MODE_DISABLED** = `0`

Child draws over parent and is not clipped.

<span id="class_RenderingServer_constant_CANVAS_GROUP_MODE_CLIP_ONLY"></span>

[CanvasGroupMode](class_renderingserver.md#enum_RenderingServer_CanvasGroupMode) **CANVAS_GROUP_MODE_CLIP_ONLY** = `1`

Parent is used for the purposes of clipping only. Child is clipped to the parent's visible area, parent is not drawn.

<span id="class_RenderingServer_constant_CANVAS_GROUP_MODE_CLIP_AND_DRAW"></span>

[CanvasGroupMode](class_renderingserver.md#enum_RenderingServer_CanvasGroupMode) **CANVAS_GROUP_MODE_CLIP_AND_DRAW** = `2`

Parent is used for clipping child, but parent is also drawn underneath child as normal before clipping child to its visible area.

<span id="class_RenderingServer_constant_CANVAS_GROUP_MODE_TRANSPARENT"></span>

[CanvasGroupMode](class_renderingserver.md#enum_RenderingServer_CanvasGroupMode) **CANVAS_GROUP_MODE_TRANSPARENT** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

<span id="enum_RenderingServer_CanvasLightMode"></span>

enum **CanvasLightMode**: [🔗](class_renderingserver.md#enum_RenderingServer_CanvasLightMode)

<span id="class_RenderingServer_constant_CANVAS_LIGHT_MODE_POINT"></span>

[CanvasLightMode](class_renderingserver.md#enum_RenderingServer_CanvasLightMode) **CANVAS_LIGHT_MODE_POINT** = `0`

2D point light (see [PointLight2D](class_pointlight2d.md#class_PointLight2D)).

<span id="class_RenderingServer_constant_CANVAS_LIGHT_MODE_DIRECTIONAL"></span>

[CanvasLightMode](class_renderingserver.md#enum_RenderingServer_CanvasLightMode) **CANVAS_LIGHT_MODE_DIRECTIONAL** = `1`

2D directional (sun/moon) light (see [DirectionalLight2D](class_directionallight2d.md#class_DirectionalLight2D)).

---

<span id="enum_RenderingServer_CanvasLightBlendMode"></span>

enum **CanvasLightBlendMode**: [🔗](class_renderingserver.md#enum_RenderingServer_CanvasLightBlendMode)

<span id="class_RenderingServer_constant_CANVAS_LIGHT_BLEND_MODE_ADD"></span>

[CanvasLightBlendMode](class_renderingserver.md#enum_RenderingServer_CanvasLightBlendMode) **CANVAS_LIGHT_BLEND_MODE_ADD** = `0`

Adds light color additive to the canvas.

<span id="class_RenderingServer_constant_CANVAS_LIGHT_BLEND_MODE_SUB"></span>

[CanvasLightBlendMode](class_renderingserver.md#enum_RenderingServer_CanvasLightBlendMode) **CANVAS_LIGHT_BLEND_MODE_SUB** = `1`

Adds light color subtractive to the canvas.

<span id="class_RenderingServer_constant_CANVAS_LIGHT_BLEND_MODE_MIX"></span>

[CanvasLightBlendMode](class_renderingserver.md#enum_RenderingServer_CanvasLightBlendMode) **CANVAS_LIGHT_BLEND_MODE_MIX** = `2`

The light adds color depending on transparency.

---

<span id="enum_RenderingServer_CanvasLightShadowFilter"></span>

enum **CanvasLightShadowFilter**: [🔗](class_renderingserver.md#enum_RenderingServer_CanvasLightShadowFilter)

<span id="class_RenderingServer_constant_CANVAS_LIGHT_FILTER_NONE"></span>

[CanvasLightShadowFilter](class_renderingserver.md#enum_RenderingServer_CanvasLightShadowFilter) **CANVAS_LIGHT_FILTER_NONE** = `0`

Do not apply a filter to canvas light shadows.

<span id="class_RenderingServer_constant_CANVAS_LIGHT_FILTER_PCF5"></span>

[CanvasLightShadowFilter](class_renderingserver.md#enum_RenderingServer_CanvasLightShadowFilter) **CANVAS_LIGHT_FILTER_PCF5** = `1`

Use PCF5 filtering to filter canvas light shadows.

<span id="class_RenderingServer_constant_CANVAS_LIGHT_FILTER_PCF13"></span>

[CanvasLightShadowFilter](class_renderingserver.md#enum_RenderingServer_CanvasLightShadowFilter) **CANVAS_LIGHT_FILTER_PCF13** = `2`

Use PCF13 filtering to filter canvas light shadows.

<span id="class_RenderingServer_constant_CANVAS_LIGHT_FILTER_MAX"></span>

[CanvasLightShadowFilter](class_renderingserver.md#enum_RenderingServer_CanvasLightShadowFilter) **CANVAS_LIGHT_FILTER_MAX** = `3`

Max value of the [CanvasLightShadowFilter](class_renderingserver.md#enum_RenderingServer_CanvasLightShadowFilter) enum.

---

<span id="enum_RenderingServer_CanvasOccluderPolygonCullMode"></span>

enum **CanvasOccluderPolygonCullMode**: [🔗](class_renderingserver.md#enum_RenderingServer_CanvasOccluderPolygonCullMode)

<span id="class_RenderingServer_constant_CANVAS_OCCLUDER_POLYGON_CULL_DISABLED"></span>

[CanvasOccluderPolygonCullMode](class_renderingserver.md#enum_RenderingServer_CanvasOccluderPolygonCullMode) **CANVAS_OCCLUDER_POLYGON_CULL_DISABLED** = `0`

Culling of the canvas occluder is disabled.

<span id="class_RenderingServer_constant_CANVAS_OCCLUDER_POLYGON_CULL_CLOCKWISE"></span>

[CanvasOccluderPolygonCullMode](class_renderingserver.md#enum_RenderingServer_CanvasOccluderPolygonCullMode) **CANVAS_OCCLUDER_POLYGON_CULL_CLOCKWISE** = `1`

Culling of the canvas occluder is clockwise.

<span id="class_RenderingServer_constant_CANVAS_OCCLUDER_POLYGON_CULL_COUNTER_CLOCKWISE"></span>

[CanvasOccluderPolygonCullMode](class_renderingserver.md#enum_RenderingServer_CanvasOccluderPolygonCullMode) **CANVAS_OCCLUDER_POLYGON_CULL_COUNTER_CLOCKWISE** = `2`

Culling of the canvas occluder is counterclockwise.

---

<span id="enum_RenderingServer_GlobalShaderParameterType"></span>

enum **GlobalShaderParameterType**: [🔗](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType)

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_BOOL"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_BOOL** = `0`

Boolean global shader parameter (`global uniform bool ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_BVEC2"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_BVEC2** = `1`

2-dimensional boolean vector global shader parameter (`global uniform bvec2 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_BVEC3"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_BVEC3** = `2`

3-dimensional boolean vector global shader parameter (`global uniform bvec3 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_BVEC4"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_BVEC4** = `3`

4-dimensional boolean vector global shader parameter (`global uniform bvec4 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_INT"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_INT** = `4`

Integer global shader parameter (`global uniform int ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_IVEC2"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_IVEC2** = `5`

2-dimensional integer vector global shader parameter (`global uniform ivec2 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_IVEC3"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_IVEC3** = `6`

3-dimensional integer vector global shader parameter (`global uniform ivec3 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_IVEC4"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_IVEC4** = `7`

4-dimensional integer vector global shader parameter (`global uniform ivec4 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_RECT2I"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_RECT2I** = `8`

2-dimensional integer rectangle global shader parameter (`global uniform ivec4 ...`). Equivalent to [GLOBAL_VAR_TYPE_IVEC4](class_renderingserver.md#class_RenderingServer_constant_GLOBAL_VAR_TYPE_IVEC4) in shader code, but exposed as a [Rect2i](class_rect2i.md#class_Rect2i) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_UINT"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_UINT** = `9`

Unsigned integer global shader parameter (`global uniform uint ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_UVEC2"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_UVEC2** = `10`

2-dimensional unsigned integer vector global shader parameter (`global uniform uvec2 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_UVEC3"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_UVEC3** = `11`

3-dimensional unsigned integer vector global shader parameter (`global uniform uvec3 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_UVEC4"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_UVEC4** = `12`

4-dimensional unsigned integer vector global shader parameter (`global uniform uvec4 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_FLOAT"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_FLOAT** = `13`

Single-precision floating-point global shader parameter (`global uniform float ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC2"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_VEC2** = `14`

2-dimensional floating-point vector global shader parameter (`global uniform vec2 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC3"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_VEC3** = `15`

3-dimensional floating-point vector global shader parameter (`global uniform vec3 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC4"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_VEC4** = `16`

4-dimensional floating-point vector global shader parameter (`global uniform vec4 ...`).

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_COLOR"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_COLOR** = `17`

Color global shader parameter (`global uniform vec4 ...`). Equivalent to [GLOBAL_VAR_TYPE_VEC4](class_renderingserver.md#class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC4) in shader code, but exposed as a [Color](class_color.md#class_Color) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_RECT2"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_RECT2** = `18`

2-dimensional floating-point rectangle global shader parameter (`global uniform vec4 ...`). Equivalent to [GLOBAL_VAR_TYPE_VEC4](class_renderingserver.md#class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC4) in shader code, but exposed as a [Rect2](class_rect2.md#class_Rect2) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_MAT2"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_MAT2** = `19`

2×2 matrix global shader parameter (`global uniform mat2 ...`). Exposed as a [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_MAT3"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_MAT3** = `20`

3×3 matrix global shader parameter (`global uniform mat3 ...`). Exposed as a [Basis](class_basis.md#class_Basis) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_MAT4"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_MAT4** = `21`

4×4 matrix global shader parameter (`global uniform mat4 ...`). Exposed as a [Projection](class_projection.md#class_Projection) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_TRANSFORM_2D"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_TRANSFORM_2D** = `22`

2-dimensional transform global shader parameter (`global uniform mat2x3 ...`). Exposed as a [Transform2D](class_transform2d.md#class_Transform2D) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_TRANSFORM"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_TRANSFORM** = `23`

3-dimensional transform global shader parameter (`global uniform mat3x4 ...`). Exposed as a [Transform3D](class_transform3d.md#class_Transform3D) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLER2D"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_SAMPLER2D** = `24`

2D sampler global shader parameter (`global uniform sampler2D ...`). Exposed as a [Texture2D](class_texture2d.md#class_Texture2D) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLER2DARRAY"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_SAMPLER2DARRAY** = `25`

2D sampler array global shader parameter (`global uniform sampler2DArray ...`). Exposed as a [Texture2DArray](class_texture2darray.md#class_Texture2DArray) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLER3D"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_SAMPLER3D** = `26`

3D sampler global shader parameter (`global uniform sampler3D ...`). Exposed as a [Texture3D](class_texture3d.md#class_Texture3D) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLERCUBE"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_SAMPLERCUBE** = `27`

Cubemap sampler global shader parameter (`global uniform samplerCube ...`). Exposed as a [Cubemap](class_cubemap.md#class_Cubemap) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLEREXT"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_SAMPLEREXT** = `28`

External sampler global shader parameter (`global uniform samplerExternalOES ...`). Exposed as an [ExternalTexture](class_externaltexture.md#class_ExternalTexture) in the editor UI.

<span id="class_RenderingServer_constant_GLOBAL_VAR_TYPE_MAX"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **GLOBAL_VAR_TYPE_MAX** = `29`

Represents the size of the [GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) enum.

---

<span id="enum_RenderingServer_RenderingInfo"></span>

enum **RenderingInfo**: [🔗](class_renderingserver.md#enum_RenderingServer_RenderingInfo)

<span id="class_RenderingServer_constant_RENDERING_INFO_TOTAL_OBJECTS_IN_FRAME"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_TOTAL_OBJECTS_IN_FRAME** = `0`

Number of objects rendered in the current 3D scene. This varies depending on camera position and rotation.

<span id="class_RenderingServer_constant_RENDERING_INFO_TOTAL_PRIMITIVES_IN_FRAME"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_TOTAL_PRIMITIVES_IN_FRAME** = `1`

Number of points, lines, or triangles rendered in the current 3D scene. This varies depending on camera position and rotation.

<span id="class_RenderingServer_constant_RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME** = `2`

Number of draw calls performed to render in the current 3D scene. This varies depending on camera position and rotation.

<span id="class_RenderingServer_constant_RENDERING_INFO_TEXTURE_MEM_USED"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_TEXTURE_MEM_USED** = `3`

Texture memory used (in bytes).

<span id="class_RenderingServer_constant_RENDERING_INFO_BUFFER_MEM_USED"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_BUFFER_MEM_USED** = `4`

Buffer memory used (in bytes). This includes vertex data, uniform buffers, and many miscellaneous buffer types used internally.

<span id="class_RenderingServer_constant_RENDERING_INFO_VIDEO_MEM_USED"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_VIDEO_MEM_USED** = `5`

Video memory used (in bytes). When using the Forward+ or Mobile renderers, this is always greater than the sum of [RENDERING_INFO_TEXTURE_MEM_USED](class_renderingserver.md#class_RenderingServer_constant_RENDERING_INFO_TEXTURE_MEM_USED) and [RENDERING_INFO_BUFFER_MEM_USED](class_renderingserver.md#class_RenderingServer_constant_RENDERING_INFO_BUFFER_MEM_USED), since there is miscellaneous data not accounted for by those two metrics. When using the Compatibility renderer, this is equal to the sum of [RENDERING_INFO_TEXTURE_MEM_USED](class_renderingserver.md#class_RenderingServer_constant_RENDERING_INFO_TEXTURE_MEM_USED) and [RENDERING_INFO_BUFFER_MEM_USED](class_renderingserver.md#class_RenderingServer_constant_RENDERING_INFO_BUFFER_MEM_USED).

<span id="class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_CANVAS"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_PIPELINE_COMPILATIONS_CANVAS** = `6`

Number of pipeline compilations that were triggered by the 2D canvas renderer.

<span id="class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_MESH"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_PIPELINE_COMPILATIONS_MESH** = `7`

Number of pipeline compilations that were triggered by loading meshes. These compilations will show up as longer loading times the first time a user runs the game and the pipeline is required.

<span id="class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_SURFACE"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_PIPELINE_COMPILATIONS_SURFACE** = `8`

Number of pipeline compilations that were triggered by building the surface cache before rendering the scene. These compilations will show up as a stutter when loading a scene the first time a user runs the game and the pipeline is required.

<span id="class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_DRAW"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_PIPELINE_COMPILATIONS_DRAW** = `9`

Number of pipeline compilations that were triggered while drawing the scene. These compilations will show up as stutters during gameplay the first time a user runs the game and the pipeline is required.

<span id="class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_SPECIALIZATION"></span>

[RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) **RENDERING_INFO_PIPELINE_COMPILATIONS_SPECIALIZATION** = `10`

Number of pipeline compilations that were triggered to optimize the current scene. These compilations are done in the background and should not cause any stutters whatsoever.

---

<span id="enum_RenderingServer_PipelineSource"></span>

enum **PipelineSource**: [🔗](class_renderingserver.md#enum_RenderingServer_PipelineSource)

<span id="class_RenderingServer_constant_PIPELINE_SOURCE_CANVAS"></span>

[PipelineSource](class_renderingserver.md#enum_RenderingServer_PipelineSource) **PIPELINE_SOURCE_CANVAS** = `0`

Pipeline compilation that was triggered by the 2D canvas renderer.

<span id="class_RenderingServer_constant_PIPELINE_SOURCE_MESH"></span>

[PipelineSource](class_renderingserver.md#enum_RenderingServer_PipelineSource) **PIPELINE_SOURCE_MESH** = `1`

Pipeline compilation that was triggered by loading a mesh.

<span id="class_RenderingServer_constant_PIPELINE_SOURCE_SURFACE"></span>

[PipelineSource](class_renderingserver.md#enum_RenderingServer_PipelineSource) **PIPELINE_SOURCE_SURFACE** = `2`

Pipeline compilation that was triggered by building the surface cache before rendering the scene.

<span id="class_RenderingServer_constant_PIPELINE_SOURCE_DRAW"></span>

[PipelineSource](class_renderingserver.md#enum_RenderingServer_PipelineSource) **PIPELINE_SOURCE_DRAW** = `3`

Pipeline compilation that was triggered while drawing the scene.

<span id="class_RenderingServer_constant_PIPELINE_SOURCE_SPECIALIZATION"></span>

[PipelineSource](class_renderingserver.md#enum_RenderingServer_PipelineSource) **PIPELINE_SOURCE_SPECIALIZATION** = `4`

Pipeline compilation that was triggered to optimize the current scene.

<span id="class_RenderingServer_constant_PIPELINE_SOURCE_MAX"></span>

[PipelineSource](class_renderingserver.md#enum_RenderingServer_PipelineSource) **PIPELINE_SOURCE_MAX** = `5`

Represents the size of the [PipelineSource](class_renderingserver.md#enum_RenderingServer_PipelineSource) enum.

---

<span id="enum_RenderingServer_SplashStretchMode"></span>

enum **SplashStretchMode**: [🔗](class_renderingserver.md#enum_RenderingServer_SplashStretchMode)

<span id="class_RenderingServer_constant_SPLASH_STRETCH_MODE_DISABLED"></span>

[SplashStretchMode](class_renderingserver.md#enum_RenderingServer_SplashStretchMode) **SPLASH_STRETCH_MODE_DISABLED** = `0`

No stretching is applied.

<span id="class_RenderingServer_constant_SPLASH_STRETCH_MODE_KEEP"></span>

[SplashStretchMode](class_renderingserver.md#enum_RenderingServer_SplashStretchMode) **SPLASH_STRETCH_MODE_KEEP** = `1`

Stretches image to fullscreen while preserving aspect ratio.

<span id="class_RenderingServer_constant_SPLASH_STRETCH_MODE_KEEP_WIDTH"></span>

[SplashStretchMode](class_renderingserver.md#enum_RenderingServer_SplashStretchMode) **SPLASH_STRETCH_MODE_KEEP_WIDTH** = `2`

Stretches the height of the image based on the width of the screen.

<span id="class_RenderingServer_constant_SPLASH_STRETCH_MODE_KEEP_HEIGHT"></span>

[SplashStretchMode](class_renderingserver.md#enum_RenderingServer_SplashStretchMode) **SPLASH_STRETCH_MODE_KEEP_HEIGHT** = `3`

Stretches the width of the image based on the height of the screen.

<span id="class_RenderingServer_constant_SPLASH_STRETCH_MODE_COVER"></span>

[SplashStretchMode](class_renderingserver.md#enum_RenderingServer_SplashStretchMode) **SPLASH_STRETCH_MODE_COVER** = `4`

Stretches the image to cover the entire screen while preserving aspect ratio.

<span id="class_RenderingServer_constant_SPLASH_STRETCH_MODE_IGNORE"></span>

[SplashStretchMode](class_renderingserver.md#enum_RenderingServer_SplashStretchMode) **SPLASH_STRETCH_MODE_IGNORE** = `5`

Stretches the image to cover the entire screen but doesn't preserve aspect ratio.

---

<span id="enum_RenderingServer_Features"></span>

enum **Features**: [🔗](class_renderingserver.md#enum_RenderingServer_Features)

<span id="class_RenderingServer_constant_FEATURE_SHADERS"></span>

[Features](class_renderingserver.md#enum_RenderingServer_Features) **FEATURE_SHADERS** = `0`

**Deprecated:** This constant has not been used since Godot 3.0.

<span id="class_RenderingServer_constant_FEATURE_MULTITHREADED"></span>

[Features](class_renderingserver.md#enum_RenderingServer_Features) **FEATURE_MULTITHREADED** = `1`

**Deprecated:** This constant has not been used since Godot 3.0.

---

### Constants

<span id="class_RenderingServer_constant_NO_INDEX_ARRAY"></span>

**NO_INDEX_ARRAY** = `-1` [🔗](class_renderingserver.md#class_RenderingServer_constant_NO_INDEX_ARRAY)

Marks an error that shows that the index array is empty.

<span id="class_RenderingServer_constant_ARRAY_WEIGHTS_SIZE"></span>

**ARRAY_WEIGHTS_SIZE** = `4` [🔗](class_renderingserver.md#class_RenderingServer_constant_ARRAY_WEIGHTS_SIZE)

Number of weights/bones per vertex.

<span id="class_RenderingServer_constant_CANVAS_ITEM_Z_MIN"></span>

**CANVAS_ITEM_Z_MIN** = `-4096` [🔗](class_renderingserver.md#class_RenderingServer_constant_CANVAS_ITEM_Z_MIN)

The minimum Z-layer for canvas items.

<span id="class_RenderingServer_constant_CANVAS_ITEM_Z_MAX"></span>

**CANVAS_ITEM_Z_MAX** = `4096` [🔗](class_renderingserver.md#class_RenderingServer_constant_CANVAS_ITEM_Z_MAX)

The maximum Z-layer for canvas items.

<span id="class_RenderingServer_constant_CANVAS_LAYER_MIN"></span>

**CANVAS_LAYER_MIN** = `-2147483648` [🔗](class_renderingserver.md#class_RenderingServer_constant_CANVAS_LAYER_MIN)

The minimum canvas layer.

<span id="class_RenderingServer_constant_CANVAS_LAYER_MAX"></span>

**CANVAS_LAYER_MAX** = `2147483647` [🔗](class_renderingserver.md#class_RenderingServer_constant_CANVAS_LAYER_MAX)

The maximum canvas layer.

<span id="class_RenderingServer_constant_MAX_GLOW_LEVELS"></span>

**MAX_GLOW_LEVELS** = `7` [🔗](class_renderingserver.md#class_RenderingServer_constant_MAX_GLOW_LEVELS)

The maximum number of glow levels that can be used with the glow post-processing effect.

<span id="class_RenderingServer_constant_MAX_CURSORS"></span>

**MAX_CURSORS** = `8` [🔗](class_renderingserver.md#class_RenderingServer_constant_MAX_CURSORS)

**Deprecated:** This constant is not used by the engine.

<span id="class_RenderingServer_constant_MAX_2D_DIRECTIONAL_LIGHTS"></span>

**MAX_2D_DIRECTIONAL_LIGHTS** = `8` [🔗](class_renderingserver.md#class_RenderingServer_constant_MAX_2D_DIRECTIONAL_LIGHTS)

The maximum number of directional lights that can be rendered at a given time in 2D.

<span id="class_RenderingServer_constant_MAX_MESH_SURFACES"></span>

**MAX_MESH_SURFACES** = `256` [🔗](class_renderingserver.md#class_RenderingServer_constant_MAX_MESH_SURFACES)

The maximum number of surfaces a mesh can have.

<span id="class_RenderingServer_constant_MATERIAL_RENDER_PRIORITY_MIN"></span>

**MATERIAL_RENDER_PRIORITY_MIN** = `-128` [🔗](class_renderingserver.md#class_RenderingServer_constant_MATERIAL_RENDER_PRIORITY_MIN)

The minimum renderpriority of all materials.

<span id="class_RenderingServer_constant_MATERIAL_RENDER_PRIORITY_MAX"></span>

**MATERIAL_RENDER_PRIORITY_MAX** = `127` [🔗](class_renderingserver.md#class_RenderingServer_constant_MATERIAL_RENDER_PRIORITY_MAX)

The maximum renderpriority of all materials.

<span id="class_RenderingServer_constant_ARRAY_CUSTOM_COUNT"></span>

**ARRAY_CUSTOM_COUNT** = `4` [🔗](class_renderingserver.md#class_RenderingServer_constant_ARRAY_CUSTOM_COUNT)

The number of custom data arrays available ([ARRAY_CUSTOM0](class_renderingserver.md#class_RenderingServer_constant_ARRAY_CUSTOM0), [ARRAY_CUSTOM1](class_renderingserver.md#class_RenderingServer_constant_ARRAY_CUSTOM1), [ARRAY_CUSTOM2](class_renderingserver.md#class_RenderingServer_constant_ARRAY_CUSTOM2), [ARRAY_CUSTOM3](class_renderingserver.md#class_RenderingServer_constant_ARRAY_CUSTOM3)).

<span id="class_RenderingServer_constant_PARTICLES_EMIT_FLAG_POSITION"></span>

**PARTICLES_EMIT_FLAG_POSITION** = `1` [🔗](class_renderingserver.md#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_POSITION)

Particle starts at the specified position.

<span id="class_RenderingServer_constant_PARTICLES_EMIT_FLAG_ROTATION_SCALE"></span>

**PARTICLES_EMIT_FLAG_ROTATION_SCALE** = `2` [🔗](class_renderingserver.md#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_ROTATION_SCALE)

Particle starts with specified rotation and scale.

<span id="class_RenderingServer_constant_PARTICLES_EMIT_FLAG_VELOCITY"></span>

**PARTICLES_EMIT_FLAG_VELOCITY** = `4` [🔗](class_renderingserver.md#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_VELOCITY)

Particle starts with the specified velocity vector, which defines the emission direction and speed.

<span id="class_RenderingServer_constant_PARTICLES_EMIT_FLAG_COLOR"></span>

**PARTICLES_EMIT_FLAG_COLOR** = `8` [🔗](class_renderingserver.md#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_COLOR)

Particle starts with specified color.

<span id="class_RenderingServer_constant_PARTICLES_EMIT_FLAG_CUSTOM"></span>

**PARTICLES_EMIT_FLAG_CUSTOM** = `16` [🔗](class_renderingserver.md#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_CUSTOM)

Particle starts with specified `CUSTOM` data.

---

### Property Descriptions

<span id="class_RenderingServer_property_render_loop_enabled"></span>

[bool](class_bool.md#class_bool) **render_loop_enabled** [🔗](class_renderingserver.md#class_RenderingServer_property_render_loop_enabled)

- void **set_render_loop_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_render_loop_enabled** ( )

If `false`, disables rendering completely, but the engine logic is still being processed. You can call [force_draw()](class_renderingserver.md#class_RenderingServer_method_force_draw) to draw a frame even with rendering disabled.

---

### Method Descriptions

<span id="class_RenderingServer_method_bake_render_uv2"></span>

[Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] **bake_render_uv2** ( base: [RID](class_rid.md#class_RID), material_overrides: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], image_size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_renderingserver.md#class_RenderingServer_method_bake_render_uv2)

Bakes the material data of the Mesh passed in the `base` parameter with optional `material_overrides` to a set of [Image](class_image.md#class_Image) s of size `image_size`. Returns an array of [Image](class_image.md#class_Image) s containing material properties as specified in [BakeChannels](class_renderingserver.md#enum_RenderingServer_BakeChannels).

---

<span id="class_RenderingServer_method_call_on_render_thread"></span>

void **call_on_render_thread** ( callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_renderingserver.md#class_RenderingServer_method_call_on_render_thread)

As the RenderingServer actual logic may run on a separate thread, accessing its internals from the main (or any other) thread will result in errors. To make it easier to run code that can safely access the rendering internals (such as [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) and similar RD classes), push a callable via this function so it will be executed on the render thread.

---

<span id="class_RenderingServer_method_camera_attributes_create"></span>

[RID](class_rid.md#class_RID) **camera_attributes_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_attributes_create)

Creates a camera attributes object and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `camera_attributes_` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [CameraAttributes](class_cameraattributes.md#class_CameraAttributes).

---

<span id="class_RenderingServer_method_camera_attributes_set_auto_exposure"></span>

void **camera_attributes_set_auto_exposure** ( camera_attributes: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), min_sensitivity: [float](class_float.md#class_float), max_sensitivity: [float](class_float.md#class_float), speed: [float](class_float.md#class_float), scale: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_auto_exposure)

Sets the parameters to use with the auto-exposure effect. These parameters take on the same meaning as their counterparts in [CameraAttributes](class_cameraattributes.md#class_CameraAttributes) and [CameraAttributesPractical](class_cameraattributespractical.md#class_CameraAttributesPractical).

---

<span id="class_RenderingServer_method_camera_attributes_set_dof_blur"></span>

void **camera_attributes_set_dof_blur** ( camera_attributes: [RID](class_rid.md#class_RID), far_enable: [bool](class_bool.md#class_bool), far_distance: [float](class_float.md#class_float), far_transition: [float](class_float.md#class_float), near_enable: [bool](class_bool.md#class_bool), near_distance: [float](class_float.md#class_float), near_transition: [float](class_float.md#class_float), amount: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_dof_blur)

Sets the parameters to use with the DOF blur effect. These parameters take on the same meaning as their counterparts in [CameraAttributesPractical](class_cameraattributespractical.md#class_CameraAttributesPractical).

---

<span id="class_RenderingServer_method_camera_attributes_set_dof_blur_bokeh_shape"></span>

void **camera_attributes_set_dof_blur_bokeh_shape** ( shape: [DOFBokehShape](class_renderingserver.md#enum_RenderingServer_DOFBokehShape) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_dof_blur_bokeh_shape)

Sets the shape of the DOF bokeh pattern to `shape`. Different shapes may be used to achieve artistic effect, or to meet performance targets.

---

<span id="class_RenderingServer_method_camera_attributes_set_dof_blur_quality"></span>

void **camera_attributes_set_dof_blur_quality** ( quality: [DOFBlurQuality](class_renderingserver.md#enum_RenderingServer_DOFBlurQuality), use_jitter: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_dof_blur_quality)

Sets the quality level of the DOF blur effect to `quality`. `use_jitter` can be used to jitter samples taken during the blur pass to hide artifacts at the cost of looking more fuzzy.

---

<span id="class_RenderingServer_method_camera_attributes_set_exposure"></span>

void **camera_attributes_set_exposure** ( camera_attributes: [RID](class_rid.md#class_RID), multiplier: [float](class_float.md#class_float), normalization: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_exposure)

Sets the exposure values that will be used by the renderers. The normalization amount is used to bake a given Exposure Value (EV) into rendering calculations to reduce the dynamic range of the scene.

The normalization factor can be calculated from exposure value (EV100) as follows:

::

    func get_exposure_normalization(ev100: float):
        return 1.0 / (pow(2.0, ev100) * 1.2)

The exposure value can be calculated from aperture (in f-stops), shutter speed (in seconds), and sensitivity (in ISO) as follows:

::

    func get_exposure(aperture: float, shutter_speed: float, sensitivity: float):
        return log((aperture * aperture) / shutter_speed * (100.0 / sensitivity)) / log(2)

---

<span id="class_RenderingServer_method_camera_create"></span>

[RID](class_rid.md#class_RID) **camera_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_create)

Creates a 3D camera and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `camera_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent node is [Camera3D](class_camera3d.md#class_Camera3D).

---

<span id="class_RenderingServer_method_camera_set_camera_attributes"></span>

void **camera_set_camera_attributes** ( camera: [RID](class_rid.md#class_RID), effects: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_set_camera_attributes)

Sets the camera_attributes created with [camera_attributes_create()](class_renderingserver.md#class_RenderingServer_method_camera_attributes_create) to the given camera.

---

<span id="class_RenderingServer_method_camera_set_compositor"></span>

void **camera_set_compositor** ( camera: [RID](class_rid.md#class_RID), compositor: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_set_compositor)

Sets the compositor used by this camera. Equivalent to [Camera3D.compositor](class_camera3d.md#class_Camera3D_property_compositor).

---

<span id="class_RenderingServer_method_camera_set_cull_mask"></span>

void **camera_set_cull_mask** ( camera: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_set_cull_mask)

Sets the cull mask associated with this camera. The cull mask describes which 3D layers are rendered by this camera. Equivalent to [Camera3D.cull_mask](class_camera3d.md#class_Camera3D_property_cull_mask).

---

<span id="class_RenderingServer_method_camera_set_environment"></span>

void **camera_set_environment** ( camera: [RID](class_rid.md#class_RID), env: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_set_environment)

Sets the environment used by this camera. Equivalent to [Camera3D.environment](class_camera3d.md#class_Camera3D_property_environment).

---

<span id="class_RenderingServer_method_camera_set_frustum"></span>

void **camera_set_frustum** ( camera: [RID](class_rid.md#class_RID), size: [float](class_float.md#class_float), offset: [Vector2](class_vector2.md#class_Vector2), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_set_frustum)

Sets camera to use frustum projection. This mode allows adjusting the `offset` argument to create "tilted frustum" effects.

---

<span id="class_RenderingServer_method_camera_set_orthogonal"></span>

void **camera_set_orthogonal** ( camera: [RID](class_rid.md#class_RID), size: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_set_orthogonal)

Sets camera to use orthogonal projection, also known as orthographic projection. Objects remain the same size on the screen no matter how far away they are.

---

<span id="class_RenderingServer_method_camera_set_perspective"></span>

void **camera_set_perspective** ( camera: [RID](class_rid.md#class_RID), fovy_degrees: [float](class_float.md#class_float), z_near: [float](class_float.md#class_float), z_far: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_set_perspective)

Sets camera to use perspective projection. Objects on the screen becomes smaller when they are far away.

---

<span id="class_RenderingServer_method_camera_set_transform"></span>

void **camera_set_transform** ( camera: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_set_transform)

Sets [Transform3D](class_transform3d.md#class_Transform3D) of camera.

---

<span id="class_RenderingServer_method_camera_set_use_vertical_aspect"></span>

void **camera_set_use_vertical_aspect** ( camera: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_camera_set_use_vertical_aspect)

If `true`, preserves the horizontal aspect ratio which is equivalent to [Camera3D.KEEP_WIDTH](class_camera3d.md#class_Camera3D_constant_KEEP_WIDTH). If `false`, preserves the vertical aspect ratio which is equivalent to [Camera3D.KEEP_HEIGHT](class_camera3d.md#class_Camera3D_constant_KEEP_HEIGHT).

---

<span id="class_RenderingServer_method_canvas_create"></span>

[RID](class_rid.md#class_RID) **canvas_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_create)

Creates a canvas and returns the assigned [RID](class_rid.md#class_RID). It can be accessed with the RID that is returned. This RID will be used in all `canvas_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

Canvas has no [Resource](class_resource.md#class_Resource) or [Node](class_node.md#class_Node) equivalent.

---

<span id="class_RenderingServer_method_canvas_item_add_animation_slice"></span>

void **canvas_item_add_animation_slice** ( item: [RID](class_rid.md#class_RID), animation_length: [float](class_float.md#class_float), slice_begin: [float](class_float.md#class_float), slice_end: [float](class_float.md#class_float), offset: [float](class_float.md#class_float) = 0.0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_animation_slice)

Subsequent drawing commands will be ignored unless they fall within the specified animation slice. This is a faster way to implement animations that loop on background rather than redrawing constantly.

---

<span id="class_RenderingServer_method_canvas_item_add_circle"></span>

void **canvas_item_add_circle** ( item: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), radius: [float](class_float.md#class_float), color: [Color](class_color.md#class_Color), antialiased: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_circle)

Draws a circle on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_circle()](class_canvasitem.md#class_CanvasItem_method_draw_circle).

---

<span id="class_RenderingServer_method_canvas_item_add_clip_ignore"></span>

void **canvas_item_add_clip_ignore** ( item: [RID](class_rid.md#class_RID), ignore: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_clip_ignore)

If `ignore` is `true`, ignore clipping on items drawn with this canvas item until this is called again with `ignore` set to `false`.

---

<span id="class_RenderingServer_method_canvas_item_add_ellipse"></span>

void **canvas_item_add_ellipse** ( item: [RID](class_rid.md#class_RID), pos: [Vector2](class_vector2.md#class_Vector2), major: [float](class_float.md#class_float), minor: [float](class_float.md#class_float), color: [Color](class_color.md#class_Color), antialiased: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_ellipse)

Draws an ellipse with semi-major axis `major` and semi-minor axis `minor` on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_ellipse()](class_canvasitem.md#class_CanvasItem_method_draw_ellipse).

---

<span id="class_RenderingServer_method_canvas_item_add_lcd_texture_rect_region"></span>

void **canvas_item_add_lcd_texture_rect_region** ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_lcd_texture_rect_region)

See also [CanvasItem.draw_lcd_texture_rect_region()](class_canvasitem.md#class_CanvasItem_method_draw_lcd_texture_rect_region).

---

<span id="class_RenderingServer_method_canvas_item_add_line"></span>

void **canvas_item_add_line** ( item: [RID](class_rid.md#class_RID), from: [Vector2](class_vector2.md#class_Vector2), to: [Vector2](class_vector2.md#class_Vector2), color: [Color](class_color.md#class_Color), width: [float](class_float.md#class_float) = -1.0, antialiased: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_line)

Draws a line on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_line()](class_canvasitem.md#class_CanvasItem_method_draw_line).

---

<span id="class_RenderingServer_method_canvas_item_add_mesh"></span>

void **canvas_item_add_mesh** ( item: [RID](class_rid.md#class_RID), mesh: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) = Transform2D(1, 0, 0, 1, 0, 0), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), texture: [RID](class_rid.md#class_RID) = RID() ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_mesh)

Draws a mesh created with [mesh_create()](class_renderingserver.md#class_RenderingServer_method_mesh_create) with given `transform`, `modulate` color, and `texture`. This is used internally by [MeshInstance2D](class_meshinstance2d.md#class_MeshInstance2D).

---

<span id="class_RenderingServer_method_canvas_item_add_msdf_texture_rect_region"></span>

void **canvas_item_add_msdf_texture_rect_region** ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), outline_size: [int](class_int.md#class_int) = 0, px_range: [float](class_float.md#class_float) = 1.0, scale: [float](class_float.md#class_float) = 1.0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_msdf_texture_rect_region)

See also [CanvasItem.draw_msdf_texture_rect_region()](class_canvasitem.md#class_CanvasItem_method_draw_msdf_texture_rect_region).

---

<span id="class_RenderingServer_method_canvas_item_add_multiline"></span>

void **canvas_item_add_multiline** ( item: [RID](class_rid.md#class_RID), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), width: [float](class_float.md#class_float) = -1.0, antialiased: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_multiline)

Draws a 2D multiline on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_multiline()](class_canvasitem.md#class_CanvasItem_method_draw_multiline) and [CanvasItem.draw_multiline_colors()](class_canvasitem.md#class_CanvasItem_method_draw_multiline_colors).

---

<span id="class_RenderingServer_method_canvas_item_add_multimesh"></span>

void **canvas_item_add_multimesh** ( item: [RID](class_rid.md#class_RID), mesh: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) = RID() ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_multimesh)

Draws a 2D [MultiMesh](class_multimesh.md#class_MultiMesh) on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_multimesh()](class_canvasitem.md#class_CanvasItem_method_draw_multimesh).

---

<span id="class_RenderingServer_method_canvas_item_add_nine_patch"></span>

void **canvas_item_add_nine_patch** ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), source: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), topleft: [Vector2](class_vector2.md#class_Vector2), bottomright: [Vector2](class_vector2.md#class_Vector2), x_axis_mode: [NinePatchAxisMode](class_renderingserver.md#enum_RenderingServer_NinePatchAxisMode) = 0, y_axis_mode: [NinePatchAxisMode](class_renderingserver.md#enum_RenderingServer_NinePatchAxisMode) = 0, draw_center: [bool](class_bool.md#class_bool) = true, modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_nine_patch)

Draws a nine-patch rectangle on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_canvas_item_add_particles"></span>

void **canvas_item_add_particles** ( item: [RID](class_rid.md#class_RID), particles: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_particles)

Draws particles on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_canvas_item_add_polygon"></span>

void **canvas_item_add_polygon** ( item: [RID](class_rid.md#class_RID), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), uvs: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) = PackedVector2Array(), texture: [RID](class_rid.md#class_RID) = RID() ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_polygon)

Draws a 2D polygon on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). If you need more flexibility (such as being able to use bones), use [canvas_item_add_triangle_array()](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_triangle_array) instead. See also [CanvasItem.draw_polygon()](class_canvasitem.md#class_CanvasItem_method_draw_polygon).

 **Note:** If you frequently redraw the same polygon with a large number of vertices, consider pre-calculating the triangulation with [Geometry2D.triangulate_polygon()](class_geometry2d.md#class_Geometry2D_method_triangulate_polygon) and using [CanvasItem.draw_mesh()](class_canvasitem.md#class_CanvasItem_method_draw_mesh), [CanvasItem.draw_multimesh()](class_canvasitem.md#class_CanvasItem_method_draw_multimesh), or [canvas_item_add_triangle_array()](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_triangle_array).

---

<span id="class_RenderingServer_method_canvas_item_add_polyline"></span>

void **canvas_item_add_polyline** ( item: [RID](class_rid.md#class_RID), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), width: [float](class_float.md#class_float) = -1.0, antialiased: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_polyline)

Draws a 2D polyline on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_polyline()](class_canvasitem.md#class_CanvasItem_method_draw_polyline) and [CanvasItem.draw_polyline_colors()](class_canvasitem.md#class_CanvasItem_method_draw_polyline_colors).

---

<span id="class_RenderingServer_method_canvas_item_add_primitive"></span>

void **canvas_item_add_primitive** ( item: [RID](class_rid.md#class_RID), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), uvs: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_primitive)

Draws a 2D primitive on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_primitive()](class_canvasitem.md#class_CanvasItem_method_draw_primitive).

---

<span id="class_RenderingServer_method_canvas_item_add_rect"></span>

void **canvas_item_add_rect** ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), color: [Color](class_color.md#class_Color), antialiased: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_rect)

Draws a rectangle on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_rect()](class_canvasitem.md#class_CanvasItem_method_draw_rect).

---

<span id="class_RenderingServer_method_canvas_item_add_set_transform"></span>

void **canvas_item_add_set_transform** ( item: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_set_transform)

Sets a [Transform2D](class_transform2d.md#class_Transform2D) that will be used to transform subsequent canvas item commands.

---

<span id="class_RenderingServer_method_canvas_item_add_texture_rect"></span>

void **canvas_item_add_texture_rect** ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), tile: [bool](class_bool.md#class_bool) = false, modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_texture_rect)

Draws a 2D textured rectangle on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_texture_rect()](class_canvasitem.md#class_CanvasItem_method_draw_texture_rect) and [Texture2D.draw_rect()](class_texture2d.md#class_Texture2D_method_draw_rect).

---

<span id="class_RenderingServer_method_canvas_item_add_texture_rect_region"></span>

void **canvas_item_add_texture_rect_region** ( item: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2), texture: [RID](class_rid.md#class_RID), src_rect: [Rect2](class_rect2.md#class_Rect2), modulate: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), transpose: [bool](class_bool.md#class_bool) = false, clip_uv: [bool](class_bool.md#class_bool) = true ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_texture_rect_region)

Draws the specified region of a 2D textured rectangle on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). See also [CanvasItem.draw_texture_rect_region()](class_canvasitem.md#class_CanvasItem_method_draw_texture_rect_region) and [Texture2D.draw_rect_region()](class_texture2d.md#class_Texture2D_method_draw_rect_region).

---

<span id="class_RenderingServer_method_canvas_item_add_triangle_array"></span>

void **canvas_item_add_triangle_array** ( item: [RID](class_rid.md#class_RID), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), points: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), colors: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), uvs: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) = PackedVector2Array(), bones: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) = PackedInt32Array(), weights: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) = PackedFloat32Array(), texture: [RID](class_rid.md#class_RID) = RID(), count: [int](class_int.md#class_int) = -1 ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_triangle_array)

Draws a triangle array on the [CanvasItem](class_canvasitem.md#class_CanvasItem) pointed to by the `item` [RID](class_rid.md#class_RID). This is internally used by [Line2D](class_line2d.md#class_Line2D) and [StyleBoxFlat](class_styleboxflat.md#class_StyleBoxFlat) for rendering. [canvas_item_add_triangle_array()](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_triangle_array) is highly flexible, but more complex to use than [canvas_item_add_polygon()](class_renderingserver.md#class_RenderingServer_method_canvas_item_add_polygon).

 **Note:** If `count` is set to a non-negative value, only the first `count * 3` indices (corresponding to `count` triangles) will be drawn. Otherwise, all indices are drawn.

---

<span id="class_RenderingServer_method_canvas_item_attach_skeleton"></span>

void **canvas_item_attach_skeleton** ( item: [RID](class_rid.md#class_RID), skeleton: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_attach_skeleton)

Attaches a skeleton to the [CanvasItem](class_canvasitem.md#class_CanvasItem). Removes the previous skeleton.

---

<span id="class_RenderingServer_method_canvas_item_clear"></span>

void **canvas_item_clear** ( item: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_clear)

Clears the [CanvasItem](class_canvasitem.md#class_CanvasItem) and removes all commands in it.

---

<span id="class_RenderingServer_method_canvas_item_create"></span>

[RID](class_rid.md#class_RID) **canvas_item_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_create)

Creates a new CanvasItem instance and returns its [RID](class_rid.md#class_RID). It can be accessed with the RID that is returned. This RID will be used in all `canvas_item_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent node is [CanvasItem](class_canvasitem.md#class_CanvasItem).

---

<span id="class_RenderingServer_method_canvas_item_get_instance_shader_parameter"></span>

[Variant](class_variant.md#class_Variant) **canvas_item_get_instance_shader_parameter** ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_get_instance_shader_parameter)

Returns the value of the per-instance shader uniform from the specified canvas item instance. Equivalent to [CanvasItem.get_instance_shader_parameter()](class_canvasitem.md#class_CanvasItem_method_get_instance_shader_parameter).

---

<span id="class_RenderingServer_method_canvas_item_get_instance_shader_parameter_default_value"></span>

[Variant](class_variant.md#class_Variant) **canvas_item_get_instance_shader_parameter_default_value** ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_get_instance_shader_parameter_default_value)

Returns the default value of the per-instance shader uniform from the specified canvas item instance. Equivalent to [CanvasItem.get_instance_shader_parameter()](class_canvasitem.md#class_CanvasItem_method_get_instance_shader_parameter).

---

<span id="class_RenderingServer_method_canvas_item_get_instance_shader_parameter_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **canvas_item_get_instance_shader_parameter_list** ( instance: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_get_instance_shader_parameter_list)

Returns a dictionary of per-instance shader uniform names of the per-instance shader uniform from the specified canvas item instance.

The returned dictionary is in PropertyInfo format, with the keys `name`, `class_name`, `type`, `hint`, `hint_string`, and `usage`.

---

<span id="class_RenderingServer_method_canvas_item_reset_physics_interpolation"></span>

void **canvas_item_reset_physics_interpolation** ( item: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_reset_physics_interpolation)

Prevents physics interpolation for the current physics tick.

This is useful when moving a canvas item to a new location, to give an instantaneous change rather than interpolation from the previous location.

---

<span id="class_RenderingServer_method_canvas_item_set_canvas_group_mode"></span>

void **canvas_item_set_canvas_group_mode** ( item: [RID](class_rid.md#class_RID), mode: [CanvasGroupMode](class_renderingserver.md#enum_RenderingServer_CanvasGroupMode), clear_margin: [float](class_float.md#class_float) = 5.0, fit_empty: [bool](class_bool.md#class_bool) = false, fit_margin: [float](class_float.md#class_float) = 0.0, blur_mipmaps: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_canvas_group_mode)

Sets the canvas group mode used during 2D rendering for the canvas item specified by the `item` RID. For faster but more limited clipping, use [canvas_item_set_clip()](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_clip) instead.

 **Note:** The equivalent node functionality is found in [CanvasGroup](class_canvasgroup.md#class_CanvasGroup) and [CanvasItem.clip_children](class_canvasitem.md#class_CanvasItem_property_clip_children).

---

<span id="class_RenderingServer_method_canvas_item_set_clip"></span>

void **canvas_item_set_clip** ( item: [RID](class_rid.md#class_RID), clip: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_clip)

If `clip` is `true`, makes the canvas item specified by the `item` RID not draw anything outside of its rect's coordinates. This clipping is fast, but works only with axis-aligned rectangles. This means that rotation is ignored by the clipping rectangle. For more advanced clipping shapes, use [canvas_item_set_canvas_group_mode()](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_canvas_group_mode) instead.

 **Note:** The equivalent node functionality is found in [Label.clip_text](class_label.md#class_Label_property_clip_text), [RichTextLabel](class_richtextlabel.md#class_RichTextLabel) (always enabled) and more.

---

<span id="class_RenderingServer_method_canvas_item_set_copy_to_backbuffer"></span>

void **canvas_item_set_copy_to_backbuffer** ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool), rect: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_copy_to_backbuffer)

Sets the [CanvasItem](class_canvasitem.md#class_CanvasItem) to copy a rect to the backbuffer.

---

<span id="class_RenderingServer_method_canvas_item_set_custom_rect"></span>

void **canvas_item_set_custom_rect** ( item: [RID](class_rid.md#class_RID), use_custom_rect: [bool](class_bool.md#class_bool), rect: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_custom_rect)

If `use_custom_rect` is `true`, sets the custom visibility rectangle (used for culling) to `rect` for the canvas item specified by `item`. Setting a custom visibility rect can reduce CPU load when drawing lots of 2D instances. If `use_custom_rect` is `false`, automatically computes a visibility rectangle based on the canvas item's draw commands.

---

<span id="class_RenderingServer_method_canvas_item_set_default_texture_filter"></span>

void **canvas_item_set_default_texture_filter** ( item: [RID](class_rid.md#class_RID), filter: [CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_default_texture_filter)

Sets the default texture filter mode for the canvas item specified by the `item` RID. Equivalent to [CanvasItem.texture_filter](class_canvasitem.md#class_CanvasItem_property_texture_filter).

---

<span id="class_RenderingServer_method_canvas_item_set_default_texture_repeat"></span>

void **canvas_item_set_default_texture_repeat** ( item: [RID](class_rid.md#class_RID), repeat: [CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_default_texture_repeat)

Sets the default texture repeat mode for the canvas item specified by the `item` RID. Equivalent to [CanvasItem.texture_repeat](class_canvasitem.md#class_CanvasItem_property_texture_repeat).

---

<span id="class_RenderingServer_method_canvas_item_set_distance_field_mode"></span>

void **canvas_item_set_distance_field_mode** ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_distance_field_mode)

If `enabled` is `true`, enables multichannel signed distance field rendering mode for the canvas item specified by the `item` RID. This is meant to be used for font rendering, or with specially generated images using msdfgen.

---

<span id="class_RenderingServer_method_canvas_item_set_draw_behind_parent"></span>

void **canvas_item_set_draw_behind_parent** ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_draw_behind_parent)

If `enabled` is `true`, draws the canvas item specified by the `item` RID behind its parent. Equivalent to [CanvasItem.show_behind_parent](class_canvasitem.md#class_CanvasItem_property_show_behind_parent).

---

<span id="class_RenderingServer_method_canvas_item_set_draw_index"></span>

void **canvas_item_set_draw_index** ( item: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_draw_index)

Sets the index for the [CanvasItem](class_canvasitem.md#class_CanvasItem).

---

<span id="class_RenderingServer_method_canvas_item_set_instance_shader_parameter"></span>

void **canvas_item_set_instance_shader_parameter** ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_instance_shader_parameter)

Sets the per-instance shader uniform on the specified canvas item instance. Equivalent to [CanvasItem.set_instance_shader_parameter()](class_canvasitem.md#class_CanvasItem_method_set_instance_shader_parameter).

---

<span id="class_RenderingServer_method_canvas_item_set_interpolated"></span>

void **canvas_item_set_interpolated** ( item: [RID](class_rid.md#class_RID), interpolated: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_interpolated)

If `interpolated` is `true`, turns on physics interpolation for the canvas item.

---

<span id="class_RenderingServer_method_canvas_item_set_light_mask"></span>

void **canvas_item_set_light_mask** ( item: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_light_mask)

Sets the light `mask` for the canvas item specified by the `item` RID. Equivalent to [CanvasItem.light_mask](class_canvasitem.md#class_CanvasItem_property_light_mask).

---

<span id="class_RenderingServer_method_canvas_item_set_material"></span>

void **canvas_item_set_material** ( item: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_material)

Sets a new `material` to the canvas item specified by the `item` RID. Equivalent to [CanvasItem.material](class_canvasitem.md#class_CanvasItem_property_material).

---

<span id="class_RenderingServer_method_canvas_item_set_modulate"></span>

void **canvas_item_set_modulate** ( item: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_modulate)

Multiplies the color of the canvas item specified by the `item` RID, while affecting its children. See also [canvas_item_set_self_modulate()](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_self_modulate). Equivalent to [CanvasItem.modulate](class_canvasitem.md#class_CanvasItem_property_modulate).

---

<span id="class_RenderingServer_method_canvas_item_set_parent"></span>

void **canvas_item_set_parent** ( item: [RID](class_rid.md#class_RID), parent: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_parent)

Sets a parent [CanvasItem](class_canvasitem.md#class_CanvasItem) to the [CanvasItem](class_canvasitem.md#class_CanvasItem). The item will inherit transform, modulation and visibility from its parent, like [CanvasItem](class_canvasitem.md#class_CanvasItem) nodes in the scene tree.

---

<span id="class_RenderingServer_method_canvas_item_set_self_modulate"></span>

void **canvas_item_set_self_modulate** ( item: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_self_modulate)

Multiplies the color of the canvas item specified by the `item` RID, without affecting its children. See also [canvas_item_set_modulate()](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_modulate). Equivalent to [CanvasItem.self_modulate](class_canvasitem.md#class_CanvasItem_property_self_modulate).

---

<span id="class_RenderingServer_method_canvas_item_set_sort_children_by_y"></span>

void **canvas_item_set_sort_children_by_y** ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_sort_children_by_y)

If `enabled` is `true`, child nodes with the lowest Y position are drawn before those with a higher Y position. Y-sorting only affects children that inherit from the canvas item specified by the `item` RID, not the canvas item itself. Equivalent to [CanvasItem.y_sort_enabled](class_canvasitem.md#class_CanvasItem_property_y_sort_enabled).

---

<span id="class_RenderingServer_method_canvas_item_set_transform"></span>

void **canvas_item_set_transform** ( item: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_transform)

Sets the `transform` of the canvas item specified by the `item` RID. This affects where and how the item will be drawn. Child canvas items' transforms are multiplied by their parent's transform. Equivalent to [Node2D.transform](class_node2d.md#class_Node2D_property_transform).

---

<span id="class_RenderingServer_method_canvas_item_set_use_parent_material"></span>

void **canvas_item_set_use_parent_material** ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_use_parent_material)

Sets if the [CanvasItem](class_canvasitem.md#class_CanvasItem) uses its parent's material.

---

<span id="class_RenderingServer_method_canvas_item_set_visibility_layer"></span>

void **canvas_item_set_visibility_layer** ( item: [RID](class_rid.md#class_RID), visibility_layer: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_visibility_layer)

Sets the rendering visibility layer associated with this [CanvasItem](class_canvasitem.md#class_CanvasItem). Only [Viewport](class_viewport.md#class_Viewport) nodes with a matching rendering mask will render this [CanvasItem](class_canvasitem.md#class_CanvasItem).

---

<span id="class_RenderingServer_method_canvas_item_set_visibility_notifier"></span>

void **canvas_item_set_visibility_notifier** ( item: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), area: [Rect2](class_rect2.md#class_Rect2), enter_callable: [Callable](class_callable.md#class_Callable), exit_callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_visibility_notifier)

Sets the given [CanvasItem](class_canvasitem.md#class_CanvasItem) as visibility notifier. `area` defines the area of detecting visibility. `enter_callable` is called when the [CanvasItem](class_canvasitem.md#class_CanvasItem) enters the screen, `exit_callable` is called when the [CanvasItem](class_canvasitem.md#class_CanvasItem) exits the screen. If `enable` is `false`, the item will no longer function as notifier.

This method can be used to manually mimic [VisibleOnScreenNotifier2D](class_visibleonscreennotifier2d.md#class_VisibleOnScreenNotifier2D).

---

<span id="class_RenderingServer_method_canvas_item_set_visible"></span>

void **canvas_item_set_visible** ( item: [RID](class_rid.md#class_RID), visible: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_visible)

Sets the visibility of the [CanvasItem](class_canvasitem.md#class_CanvasItem).

---

<span id="class_RenderingServer_method_canvas_item_set_z_as_relative_to_parent"></span>

void **canvas_item_set_z_as_relative_to_parent** ( item: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_z_as_relative_to_parent)

If this is enabled, the Z index of the parent will be added to the children's Z index.

---

<span id="class_RenderingServer_method_canvas_item_set_z_index"></span>

void **canvas_item_set_z_index** ( item: [RID](class_rid.md#class_RID), z_index: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_set_z_index)

Sets the [CanvasItem](class_canvasitem.md#class_CanvasItem)'s Z index, i.e. its draw order (lower indexes are drawn first).

---

<span id="class_RenderingServer_method_canvas_item_transform_physics_interpolation"></span>

void **canvas_item_transform_physics_interpolation** ( item: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_item_transform_physics_interpolation)

Transforms both the current and previous stored transform for a canvas item.

This allows transforming a canvas item without creating a "glitch" in the interpolation, which is particularly useful for large worlds utilizing a shifting origin.

---

<span id="class_RenderingServer_method_canvas_light_attach_to_canvas"></span>

void **canvas_light_attach_to_canvas** ( light: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_attach_to_canvas)

Attaches the canvas light to the canvas. Removes it from its previous canvas.

---

<span id="class_RenderingServer_method_canvas_light_create"></span>

[RID](class_rid.md#class_RID) **canvas_light_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_create)

Creates a canvas light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `canvas_light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent node is [Light2D](class_light2d.md#class_Light2D).

---

<span id="class_RenderingServer_method_canvas_light_occluder_attach_to_canvas"></span>

void **canvas_light_occluder_attach_to_canvas** ( occluder: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_attach_to_canvas)

Attaches a light occluder to the canvas. Removes it from its previous canvas.

---

<span id="class_RenderingServer_method_canvas_light_occluder_create"></span>

[RID](class_rid.md#class_RID) **canvas_light_occluder_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_create)

Creates a light occluder and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `canvas_light_occluder_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent node is [LightOccluder2D](class_lightoccluder2d.md#class_LightOccluder2D).

---

<span id="class_RenderingServer_method_canvas_light_occluder_reset_physics_interpolation"></span>

void **canvas_light_occluder_reset_physics_interpolation** ( occluder: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_reset_physics_interpolation)

Prevents physics interpolation for the current physics tick.

This is useful when moving an occluder to a new location, to give an instantaneous change rather than interpolation from the previous location.

---

<span id="class_RenderingServer_method_canvas_light_occluder_set_as_sdf_collision"></span>

void **canvas_light_occluder_set_as_sdf_collision** ( occluder: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_as_sdf_collision)

Enables or disables using the light occluder as a signed distance field for 2D particle collision.

---

<span id="class_RenderingServer_method_canvas_light_occluder_set_enabled"></span>

void **canvas_light_occluder_set_enabled** ( occluder: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_enabled)

Enables or disables light occluder.

---

<span id="class_RenderingServer_method_canvas_light_occluder_set_interpolated"></span>

void **canvas_light_occluder_set_interpolated** ( occluder: [RID](class_rid.md#class_RID), interpolated: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_interpolated)

If `interpolated` is `true`, turns on physics interpolation for the light occluder.

---

<span id="class_RenderingServer_method_canvas_light_occluder_set_light_mask"></span>

void **canvas_light_occluder_set_light_mask** ( occluder: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_light_mask)

The light mask. See [LightOccluder2D](class_lightoccluder2d.md#class_LightOccluder2D) for more information on light masks.

---

<span id="class_RenderingServer_method_canvas_light_occluder_set_polygon"></span>

void **canvas_light_occluder_set_polygon** ( occluder: [RID](class_rid.md#class_RID), polygon: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_polygon)

Sets a light occluder's polygon.

---

<span id="class_RenderingServer_method_canvas_light_occluder_set_transform"></span>

void **canvas_light_occluder_set_transform** ( occluder: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_set_transform)

Sets a light occluder's [Transform2D](class_transform2d.md#class_Transform2D).

---

<span id="class_RenderingServer_method_canvas_light_occluder_transform_physics_interpolation"></span>

void **canvas_light_occluder_transform_physics_interpolation** ( occluder: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_occluder_transform_physics_interpolation)

Transforms both the current and previous stored transform for a light occluder.

This allows transforming an occluder without creating a "glitch" in the interpolation, which is particularly useful for large worlds utilizing a shifting origin.

---

<span id="class_RenderingServer_method_canvas_light_reset_physics_interpolation"></span>

void **canvas_light_reset_physics_interpolation** ( light: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_reset_physics_interpolation)

Prevents physics interpolation for the current physics tick.

This is useful when moving a canvas item to a new location, to give an instantaneous change rather than interpolation from the previous location.

---

<span id="class_RenderingServer_method_canvas_light_set_blend_mode"></span>

void **canvas_light_set_blend_mode** ( light: [RID](class_rid.md#class_RID), mode: [CanvasLightBlendMode](class_renderingserver.md#enum_RenderingServer_CanvasLightBlendMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_blend_mode)

Sets the blend mode for the given canvas light to `mode`. Equivalent to [Light2D.blend_mode](class_light2d.md#class_Light2D_property_blend_mode).

---

<span id="class_RenderingServer_method_canvas_light_set_color"></span>

void **canvas_light_set_color** ( light: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_color)

Sets the color for a light.

---

<span id="class_RenderingServer_method_canvas_light_set_enabled"></span>

void **canvas_light_set_enabled** ( light: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_enabled)

Enables or disables a canvas light.

---

<span id="class_RenderingServer_method_canvas_light_set_energy"></span>

void **canvas_light_set_energy** ( light: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_energy)

Sets a canvas light's energy.

---

<span id="class_RenderingServer_method_canvas_light_set_height"></span>

void **canvas_light_set_height** ( light: [RID](class_rid.md#class_RID), height: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_height)

Sets a canvas light's height.

---

<span id="class_RenderingServer_method_canvas_light_set_interpolated"></span>

void **canvas_light_set_interpolated** ( light: [RID](class_rid.md#class_RID), interpolated: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_interpolated)

If `interpolated` is `true`, turns on physics interpolation for the canvas light.

---

<span id="class_RenderingServer_method_canvas_light_set_item_cull_mask"></span>

void **canvas_light_set_item_cull_mask** ( light: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_item_cull_mask)

The light mask. See [LightOccluder2D](class_lightoccluder2d.md#class_LightOccluder2D) for more information on light masks.

---

<span id="class_RenderingServer_method_canvas_light_set_item_shadow_cull_mask"></span>

void **canvas_light_set_item_shadow_cull_mask** ( light: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_item_shadow_cull_mask)

The binary mask used to determine which layers this canvas light's shadows affects. See [LightOccluder2D](class_lightoccluder2d.md#class_LightOccluder2D) for more information on light masks.

---

<span id="class_RenderingServer_method_canvas_light_set_layer_range"></span>

void **canvas_light_set_layer_range** ( light: [RID](class_rid.md#class_RID), min_layer: [int](class_int.md#class_int), max_layer: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_layer_range)

The layer range that gets rendered with this light.

---

<span id="class_RenderingServer_method_canvas_light_set_mode"></span>

void **canvas_light_set_mode** ( light: [RID](class_rid.md#class_RID), mode: [CanvasLightMode](class_renderingserver.md#enum_RenderingServer_CanvasLightMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_mode)

Sets the mode of the canvas light.

---

<span id="class_RenderingServer_method_canvas_light_set_shadow_color"></span>

void **canvas_light_set_shadow_color** ( light: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_shadow_color)

Sets the color of the canvas light's shadow.

---

<span id="class_RenderingServer_method_canvas_light_set_shadow_enabled"></span>

void **canvas_light_set_shadow_enabled** ( light: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_shadow_enabled)

Enables or disables the canvas light's shadow.

---

<span id="class_RenderingServer_method_canvas_light_set_shadow_filter"></span>

void **canvas_light_set_shadow_filter** ( light: [RID](class_rid.md#class_RID), filter: [CanvasLightShadowFilter](class_renderingserver.md#enum_RenderingServer_CanvasLightShadowFilter) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_shadow_filter)

Sets the canvas light's shadow's filter.

---

<span id="class_RenderingServer_method_canvas_light_set_shadow_smooth"></span>

void **canvas_light_set_shadow_smooth** ( light: [RID](class_rid.md#class_RID), smooth: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_shadow_smooth)

Smoothens the shadow. The lower, the smoother.

---

<span id="class_RenderingServer_method_canvas_light_set_texture"></span>

void **canvas_light_set_texture** ( light: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_texture)

Sets the texture to be used by a [PointLight2D](class_pointlight2d.md#class_PointLight2D). Equivalent to [PointLight2D.texture](class_pointlight2d.md#class_PointLight2D_property_texture).

---

<span id="class_RenderingServer_method_canvas_light_set_texture_offset"></span>

void **canvas_light_set_texture_offset** ( light: [RID](class_rid.md#class_RID), offset: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_texture_offset)

Sets the offset of a [PointLight2D](class_pointlight2d.md#class_PointLight2D)'s texture. Equivalent to [PointLight2D.offset](class_pointlight2d.md#class_PointLight2D_property_offset).

---

<span id="class_RenderingServer_method_canvas_light_set_texture_scale"></span>

void **canvas_light_set_texture_scale** ( light: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_texture_scale)

Sets the scale factor of a [PointLight2D](class_pointlight2d.md#class_PointLight2D)'s texture. Equivalent to [PointLight2D.texture_scale](class_pointlight2d.md#class_PointLight2D_property_texture_scale).

---

<span id="class_RenderingServer_method_canvas_light_set_transform"></span>

void **canvas_light_set_transform** ( light: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_transform)

Sets the canvas light's [Transform2D](class_transform2d.md#class_Transform2D).

---

<span id="class_RenderingServer_method_canvas_light_set_z_range"></span>

void **canvas_light_set_z_range** ( light: [RID](class_rid.md#class_RID), min_z: [int](class_int.md#class_int), max_z: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_set_z_range)

Sets the Z range of objects that will be affected by this light. Equivalent to [Light2D.range_z_min](class_light2d.md#class_Light2D_property_range_z_min) and [Light2D.range_z_max](class_light2d.md#class_Light2D_property_range_z_max).

---

<span id="class_RenderingServer_method_canvas_light_transform_physics_interpolation"></span>

void **canvas_light_transform_physics_interpolation** ( light: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_light_transform_physics_interpolation)

Transforms both the current and previous stored transform for a canvas light.

This allows transforming a light without creating a "glitch" in the interpolation, which is particularly useful for large worlds utilizing a shifting origin.

---

<span id="class_RenderingServer_method_canvas_occluder_polygon_create"></span>

[RID](class_rid.md#class_RID) **canvas_occluder_polygon_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_occluder_polygon_create)

Creates a new light occluder polygon and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `canvas_occluder_polygon_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [OccluderPolygon2D](class_occluderpolygon2d.md#class_OccluderPolygon2D).

---

<span id="class_RenderingServer_method_canvas_occluder_polygon_set_cull_mode"></span>

void **canvas_occluder_polygon_set_cull_mode** ( occluder_polygon: [RID](class_rid.md#class_RID), mode: [CanvasOccluderPolygonCullMode](class_renderingserver.md#enum_RenderingServer_CanvasOccluderPolygonCullMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_occluder_polygon_set_cull_mode)

Sets an occluder polygon's cull mode.

---

<span id="class_RenderingServer_method_canvas_occluder_polygon_set_shape"></span>

void **canvas_occluder_polygon_set_shape** ( occluder_polygon: [RID](class_rid.md#class_RID), shape: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array), closed: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_occluder_polygon_set_shape)

Sets the shape of the occluder polygon.

---

<span id="class_RenderingServer_method_canvas_set_disable_scale"></span>

void **canvas_set_disable_scale** ( disable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_set_disable_scale)

If `disable` is `true`, makes 2D rendering ignore the canvas scale defined for each canvas layer. This affects [CanvasLayer](class_canvaslayer.md#class_CanvasLayer) s with the [CanvasLayer.follow_viewport_enabled](class_canvaslayer.md#class_CanvasLayer_property_follow_viewport_enabled) property set to `true`.

In the editor, this is set to `true` by default, and set to `false` when **View > Preview Canvas Scale** is enabled at the top of the 2D editor viewport.

 **Note:** Setting this to `true` does not impact the behavior of [CanvasLayer.scale](class_canvaslayer.md#class_CanvasLayer_property_scale), [Node2D.scale](class_node2d.md#class_Node2D_property_scale), or [Control.scale](class_control.md#class_Control_property_scale).

---

<span id="class_RenderingServer_method_canvas_set_item_mirroring"></span>

void **canvas_set_item_mirroring** ( canvas: [RID](class_rid.md#class_RID), item: [RID](class_rid.md#class_RID), mirroring: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_set_item_mirroring)

A copy of the canvas item will be drawn with a local offset of the `mirroring`.

 **Note:** This is equivalent to calling [canvas_set_item_repeat()](class_renderingserver.md#class_RenderingServer_method_canvas_set_item_repeat) like `canvas_set_item_repeat(item, mirroring, 1)`, with an additional check ensuring `canvas` is a parent of `item`.

---

<span id="class_RenderingServer_method_canvas_set_item_repeat"></span>

void **canvas_set_item_repeat** ( item: [RID](class_rid.md#class_RID), repeat_size: [Vector2](class_vector2.md#class_Vector2), repeat_times: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_set_item_repeat)

A copy of the canvas item will be drawn with a local offset of the `repeat_size` by the number of times of the `repeat_times`. As the `repeat_times` increases, the copies will spread away from the origin texture.

---

<span id="class_RenderingServer_method_canvas_set_modulate"></span>

void **canvas_set_modulate** ( canvas: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_set_modulate)

Modulates all colors in the given canvas.

---

<span id="class_RenderingServer_method_canvas_set_shadow_texture_size"></span>

void **canvas_set_shadow_texture_size** ( size: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_set_shadow_texture_size)

Sets the ProjectSettings.rendering/2d/shadow_atlas/size to use for [Light2D](class_light2d.md#class_Light2D) shadow rendering (in pixels). The value is rounded up to the nearest power of 2.

---

<span id="class_RenderingServer_method_canvas_texture_create"></span>

[RID](class_rid.md#class_RID) **canvas_texture_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_texture_create)

Creates a canvas texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `canvas_texture_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method. See also [texture_2d_create()](class_renderingserver.md#class_RenderingServer_method_texture_2d_create).

 **Note:** The equivalent resource is [CanvasTexture](class_canvastexture.md#class_CanvasTexture) and is only meant to be used in 2D rendering, not 3D.

---

<span id="class_RenderingServer_method_canvas_texture_set_channel"></span>

void **canvas_texture_set_channel** ( canvas_texture: [RID](class_rid.md#class_RID), channel: [CanvasTextureChannel](class_renderingserver.md#enum_RenderingServer_CanvasTextureChannel), texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_texture_set_channel)

Sets the `channel`'s `texture` for the canvas texture specified by the `canvas_texture` RID. Equivalent to [CanvasTexture.diffuse_texture](class_canvastexture.md#class_CanvasTexture_property_diffuse_texture), [CanvasTexture.normal_texture](class_canvastexture.md#class_CanvasTexture_property_normal_texture) and [CanvasTexture.specular_texture](class_canvastexture.md#class_CanvasTexture_property_specular_texture).

---

<span id="class_RenderingServer_method_canvas_texture_set_shading_parameters"></span>

void **canvas_texture_set_shading_parameters** ( canvas_texture: [RID](class_rid.md#class_RID), base_color: [Color](class_color.md#class_Color), shininess: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_texture_set_shading_parameters)

Sets the `base_color` and `shininess` to use for the canvas texture specified by the `canvas_texture` RID. Equivalent to [CanvasTexture.specular_color](class_canvastexture.md#class_CanvasTexture_property_specular_color) and [CanvasTexture.specular_shininess](class_canvastexture.md#class_CanvasTexture_property_specular_shininess).

---

<span id="class_RenderingServer_method_canvas_texture_set_texture_filter"></span>

void **canvas_texture_set_texture_filter** ( canvas_texture: [RID](class_rid.md#class_RID), filter: [CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_texture_set_texture_filter)

Sets the texture `filter` mode to use for the canvas texture specified by the `canvas_texture` RID.

---

<span id="class_RenderingServer_method_canvas_texture_set_texture_repeat"></span>

void **canvas_texture_set_texture_repeat** ( canvas_texture: [RID](class_rid.md#class_RID), repeat: [CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) ) [🔗](class_renderingserver.md#class_RenderingServer_method_canvas_texture_set_texture_repeat)

Sets the texture `repeat` mode to use for the canvas texture specified by the `canvas_texture` RID.

---

<span id="class_RenderingServer_method_compositor_create"></span>

[RID](class_rid.md#class_RID) **compositor_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_compositor_create)

Creates a new compositor and adds it to the RenderingServer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

---

<span id="class_RenderingServer_method_compositor_effect_create"></span>

[RID](class_rid.md#class_RID) **compositor_effect_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_compositor_effect_create)

Creates a new rendering effect and adds it to the RenderingServer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

---

<span id="class_RenderingServer_method_compositor_effect_set_callback"></span>

void **compositor_effect_set_callback** ( effect: [RID](class_rid.md#class_RID), callback_type: [CompositorEffectCallbackType](class_renderingserver.md#enum_RenderingServer_CompositorEffectCallbackType), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_renderingserver.md#class_RenderingServer_method_compositor_effect_set_callback)

Sets the callback type (`callback_type`) and callback method(`callback`) for this rendering effect.

---

<span id="class_RenderingServer_method_compositor_effect_set_enabled"></span>

void **compositor_effect_set_enabled** ( effect: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_compositor_effect_set_enabled)

Enables/disables this rendering effect.

---

<span id="class_RenderingServer_method_compositor_effect_set_flag"></span>

void **compositor_effect_set_flag** ( effect: [RID](class_rid.md#class_RID), flag: [CompositorEffectFlags](class_renderingserver.md#enum_RenderingServer_CompositorEffectFlags), set: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_compositor_effect_set_flag)

Sets the flag (`flag`) for this rendering effect to `true` or `false` (`set`).

---

<span id="class_RenderingServer_method_compositor_set_compositor_effects"></span>

void **compositor_set_compositor_effects** ( compositor: [RID](class_rid.md#class_RID), effects: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] ) [🔗](class_renderingserver.md#class_RenderingServer_method_compositor_set_compositor_effects)

Sets the compositor effects for the specified compositor RID. `effects` should be an array containing RIDs created with [compositor_effect_create()](class_renderingserver.md#class_RenderingServer_method_compositor_effect_create).

---

<span id="class_RenderingServer_method_create_local_rendering_device"></span>

[RenderingDevice](class_renderingdevice.md#class_RenderingDevice) **create_local_rendering_device** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_create_local_rendering_device)

Creates a RenderingDevice that can be used to do draw and compute operations on a separate thread. Cannot draw to the screen nor share data with the global RenderingDevice.

 **Note:** When using the OpenGL rendering driver or when running in headless mode, this function always returns `null`.

---

<span id="class_RenderingServer_method_debug_canvas_item_get_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **debug_canvas_item_get_rect** ( item: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_debug_canvas_item_get_rect)

Returns the bounding rectangle for a canvas item in local space, as calculated by the renderer. This bound is used internally for culling.

 **Warning:** This function is intended for debugging in the editor, and will pass through and return a zero [Rect2](class_rect2.md#class_Rect2) in exported projects.

---

<span id="class_RenderingServer_method_decal_create"></span>

[RID](class_rid.md#class_RID) **decal_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_create)

Creates a decal and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `decal_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach this decal to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

 **Note:** The equivalent node is [Decal](class_decal.md#class_Decal).

---

<span id="class_RenderingServer_method_decal_set_albedo_mix"></span>

void **decal_set_albedo_mix** ( decal: [RID](class_rid.md#class_RID), albedo_mix: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_set_albedo_mix)

Sets the `albedo_mix` in the decal specified by the `decal` RID. Equivalent to [Decal.albedo_mix](class_decal.md#class_Decal_property_albedo_mix).

---

<span id="class_RenderingServer_method_decal_set_cull_mask"></span>

void **decal_set_cull_mask** ( decal: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_set_cull_mask)

Sets the cull `mask` in the decal specified by the `decal` RID. Equivalent to [Decal.cull_mask](class_decal.md#class_Decal_property_cull_mask).

---

<span id="class_RenderingServer_method_decal_set_distance_fade"></span>

void **decal_set_distance_fade** ( decal: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool), begin: [float](class_float.md#class_float), length: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_set_distance_fade)

Sets the distance fade parameters in the decal specified by the `decal` RID. Equivalent to [Decal.distance_fade_enabled](class_decal.md#class_Decal_property_distance_fade_enabled), [Decal.distance_fade_begin](class_decal.md#class_Decal_property_distance_fade_begin) and [Decal.distance_fade_length](class_decal.md#class_Decal_property_distance_fade_length).

---

<span id="class_RenderingServer_method_decal_set_emission_energy"></span>

void **decal_set_emission_energy** ( decal: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_set_emission_energy)

Sets the emission `energy` in the decal specified by the `decal` RID. Equivalent to [Decal.emission_energy](class_decal.md#class_Decal_property_emission_energy).

---

<span id="class_RenderingServer_method_decal_set_fade"></span>

void **decal_set_fade** ( decal: [RID](class_rid.md#class_RID), above: [float](class_float.md#class_float), below: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_set_fade)

Sets the upper fade (`above`) and lower fade (`below`) in the decal specified by the `decal` RID. Equivalent to [Decal.upper_fade](class_decal.md#class_Decal_property_upper_fade) and [Decal.lower_fade](class_decal.md#class_Decal_property_lower_fade).

---

<span id="class_RenderingServer_method_decal_set_modulate"></span>

void **decal_set_modulate** ( decal: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_set_modulate)

Sets the color multiplier in the decal specified by the `decal` RID to `color`. Equivalent to [Decal.modulate](class_decal.md#class_Decal_property_modulate).

---

<span id="class_RenderingServer_method_decal_set_normal_fade"></span>

void **decal_set_normal_fade** ( decal: [RID](class_rid.md#class_RID), fade: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_set_normal_fade)

Sets the normal `fade` in the decal specified by the `decal` RID. Equivalent to [Decal.normal_fade](class_decal.md#class_Decal_property_normal_fade).

---

<span id="class_RenderingServer_method_decal_set_size"></span>

void **decal_set_size** ( decal: [RID](class_rid.md#class_RID), size: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_set_size)

Sets the `size` of the decal specified by the `decal` RID. Equivalent to [Decal.size](class_decal.md#class_Decal_property_size).

---

<span id="class_RenderingServer_method_decal_set_texture"></span>

void **decal_set_texture** ( decal: [RID](class_rid.md#class_RID), type: [DecalTexture](class_renderingserver.md#enum_RenderingServer_DecalTexture), texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decal_set_texture)

Sets the `texture` in the given texture `type` slot for the specified decal. Equivalent to [Decal.set_texture()](class_decal.md#class_Decal_method_set_texture).

---

<span id="class_RenderingServer_method_decals_set_filter"></span>

void **decals_set_filter** ( filter: [DecalFilter](class_renderingserver.md#enum_RenderingServer_DecalFilter) ) [🔗](class_renderingserver.md#class_RenderingServer_method_decals_set_filter)

Sets the texture `filter` mode to use when rendering decals. This parameter is global and cannot be set on a per-decal basis.

---

<span id="class_RenderingServer_method_directional_light_create"></span>

[RID](class_rid.md#class_RID) **directional_light_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_directional_light_create)

Creates a directional light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in most `light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach this directional light to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

 **Note:** The equivalent node is [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D).

---

<span id="class_RenderingServer_method_directional_shadow_atlas_set_size"></span>

void **directional_shadow_atlas_set_size** ( size: [int](class_int.md#class_int), is_16bits: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_directional_shadow_atlas_set_size)

Sets the `size` of the directional light shadows in 3D. See also ProjectSettings.rendering/lights_and_shadows/directional_shadow/size. This parameter is global and cannot be set on a per-viewport basis.

---

<span id="class_RenderingServer_method_directional_soft_shadow_filter_set_quality"></span>

void **directional_soft_shadow_filter_set_quality** ( quality: [ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) ) [🔗](class_renderingserver.md#class_RenderingServer_method_directional_soft_shadow_filter_set_quality)

Sets the filter `quality` for directional light shadows in 3D. See also ProjectSettings.rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality. This parameter is global and cannot be set on a per-viewport basis.

---

<span id="class_RenderingServer_method_environment_bake_panorama"></span>

[Image](class_image.md#class_Image) **environment_bake_panorama** ( environment: [RID](class_rid.md#class_RID), bake_irradiance: [bool](class_bool.md#class_bool), size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_bake_panorama)

Generates and returns an [Image](class_image.md#class_Image) containing the radiance map for the specified `environment` RID's sky. This supports built-in sky material and custom sky shaders. If `bake_irradiance` is `true`, the irradiance map is saved instead of the radiance map. The radiance map is used to render reflected light, while the irradiance map is used to render ambient light. See also [sky_bake_panorama()](class_renderingserver.md#class_RenderingServer_method_sky_bake_panorama).

 **Note:** The image is saved using linear encoding without any tonemapping performed, which means it will look too dark if viewed directly in an image editor.

 **Note:** `size` should be a 2:1 aspect ratio for the generated panorama to have square pixels. For radiance maps, there is no point in using a height greater than [Sky.radiance_size](class_sky.md#class_Sky_property_radiance_size), as it won't increase detail. Irradiance maps only contain low-frequency data, so there is usually no point in going past a size of 128×64 pixels when saving an irradiance map.

---

<span id="class_RenderingServer_method_environment_create"></span>

[RID](class_rid.md#class_RID) **environment_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_create)

Creates an environment and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `environment_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [Environment](class_environment.md#class_Environment).

---

<span id="class_RenderingServer_method_environment_glow_set_use_bicubic_upscale"></span>

void **environment_glow_set_use_bicubic_upscale** ( enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_glow_set_use_bicubic_upscale)

If `enable` is `true`, enables bicubic upscaling for glow which improves quality at the cost of performance. Equivalent to ProjectSettings.rendering/environment/glow/upscale_mode.

 **Note:** This setting is only effective when using the Forward+ or Mobile rendering methods, as Compatibility uses a different glow implementation.

---

<span id="class_RenderingServer_method_environment_set_adjustment"></span>

void **environment_set_adjustment** ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), brightness: [float](class_float.md#class_float), contrast: [float](class_float.md#class_float), saturation: [float](class_float.md#class_float), use_1d_color_correction: [bool](class_bool.md#class_bool), color_correction: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_adjustment)

Sets the values to be used with the "adjustments" post-process effect. See [Environment](class_environment.md#class_Environment) for more details.

---

<span id="class_RenderingServer_method_environment_set_ambient_light"></span>

void **environment_set_ambient_light** ( env: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color), ambient: [EnvironmentAmbientSource](class_renderingserver.md#enum_RenderingServer_EnvironmentAmbientSource) = 0, energy: [float](class_float.md#class_float) = 1.0, sky_contribution: [float](class_float.md#class_float) = 0.0, reflection_source: [EnvironmentReflectionSource](class_renderingserver.md#enum_RenderingServer_EnvironmentReflectionSource) = 0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_ambient_light)

Sets the values to be used for ambient light rendering. See [Environment](class_environment.md#class_Environment) for more details.

---

<span id="class_RenderingServer_method_environment_set_background"></span>

void **environment_set_background** ( env: [RID](class_rid.md#class_RID), bg: [EnvironmentBG](class_renderingserver.md#enum_RenderingServer_EnvironmentBG) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_background)

Sets the environment's background mode. Equivalent to [Environment.background_mode](class_environment.md#class_Environment_property_background_mode).

---

<span id="class_RenderingServer_method_environment_set_bg_color"></span>

void **environment_set_bg_color** ( env: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_bg_color)

Color displayed for clear areas of the scene. Only effective if using the [ENV_BG_COLOR](class_renderingserver.md#class_RenderingServer_constant_ENV_BG_COLOR) background mode.

---

<span id="class_RenderingServer_method_environment_set_bg_energy"></span>

void **environment_set_bg_energy** ( env: [RID](class_rid.md#class_RID), multiplier: [float](class_float.md#class_float), exposure_value: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_bg_energy)

Sets the intensity of the background color.

---

<span id="class_RenderingServer_method_environment_set_camera_id"></span>

void **environment_set_camera_id** ( env: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_camera_id)

Sets the camera ID to be used as environment background.

---

<span id="class_RenderingServer_method_environment_set_canvas_max_layer"></span>

void **environment_set_canvas_max_layer** ( env: [RID](class_rid.md#class_RID), max_layer: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_canvas_max_layer)

Sets the maximum layer to use if using Canvas background mode.

---

<span id="class_RenderingServer_method_environment_set_fog"></span>

void **environment_set_fog** ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), light_color: [Color](class_color.md#class_Color), light_energy: [float](class_float.md#class_float), sun_scatter: [float](class_float.md#class_float), density: [float](class_float.md#class_float), height: [float](class_float.md#class_float), height_density: [float](class_float.md#class_float), aerial_perspective: [float](class_float.md#class_float), sky_affect: [float](class_float.md#class_float), fog_mode: [EnvironmentFogMode](class_renderingserver.md#enum_RenderingServer_EnvironmentFogMode) = 0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_fog)

Configures fog for the specified environment RID. See `fog_*` properties in [Environment](class_environment.md#class_Environment) for more information.

---

<span id="class_RenderingServer_method_environment_set_fog_depth"></span>

void **environment_set_fog_depth** ( env: [RID](class_rid.md#class_RID), curve: [float](class_float.md#class_float), begin: [float](class_float.md#class_float), end: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_fog_depth)

Configures fog depth for the specified environment RID. Only has an effect when the fog mode of the environment is [ENV_FOG_MODE_DEPTH](class_renderingserver.md#class_RenderingServer_constant_ENV_FOG_MODE_DEPTH). See `fog_depth_*` properties in [Environment](class_environment.md#class_Environment) for more information.

---

<span id="class_RenderingServer_method_environment_set_glow"></span>

void **environment_set_glow** ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), levels: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), intensity: [float](class_float.md#class_float), strength: [float](class_float.md#class_float), mix: [float](class_float.md#class_float), bloom_threshold: [float](class_float.md#class_float), blend_mode: [EnvironmentGlowBlendMode](class_renderingserver.md#enum_RenderingServer_EnvironmentGlowBlendMode), hdr_bleed_threshold: [float](class_float.md#class_float), hdr_bleed_scale: [float](class_float.md#class_float), hdr_luminance_cap: [float](class_float.md#class_float), glow_map_strength: [float](class_float.md#class_float), glow_map: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_glow)

Configures glow for the specified environment RID. See `glow_*` properties in [Environment](class_environment.md#class_Environment) for more information.

---

<span id="class_RenderingServer_method_environment_set_sdfgi"></span>

void **environment_set_sdfgi** ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), cascades: [int](class_int.md#class_int), min_cell_size: [float](class_float.md#class_float), y_scale: [EnvironmentSDFGIYScale](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIYScale), use_occlusion: [bool](class_bool.md#class_bool), bounce_feedback: [float](class_float.md#class_float), read_sky: [bool](class_bool.md#class_bool), energy: [float](class_float.md#class_float), normal_bias: [float](class_float.md#class_float), probe_bias: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_sdfgi)

Configures signed distance field global illumination for the specified environment RID. See `sdfgi_*` properties in [Environment](class_environment.md#class_Environment) for more information.

---

<span id="class_RenderingServer_method_environment_set_sdfgi_frames_to_converge"></span>

void **environment_set_sdfgi_frames_to_converge** ( frames: [EnvironmentSDFGIFramesToConverge](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToConverge) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_sdfgi_frames_to_converge)

Sets the number of frames to use for converging signed distance field global illumination. Equivalent to ProjectSettings.rendering/global_illumination/sdfgi/frames_to_converge.

---

<span id="class_RenderingServer_method_environment_set_sdfgi_frames_to_update_light"></span>

void **environment_set_sdfgi_frames_to_update_light** ( frames: [EnvironmentSDFGIFramesToUpdateLight](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_sdfgi_frames_to_update_light)

Sets the update speed for dynamic lights' indirect lighting when computing signed distance field global illumination. Equivalent to ProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights.

---

<span id="class_RenderingServer_method_environment_set_sdfgi_ray_count"></span>

void **environment_set_sdfgi_ray_count** ( ray_count: [EnvironmentSDFGIRayCount](class_renderingserver.md#enum_RenderingServer_EnvironmentSDFGIRayCount) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_sdfgi_ray_count)

Sets the number of rays to throw per frame when computing signed distance field global illumination. Equivalent to ProjectSettings.rendering/global_illumination/sdfgi/probe_ray_count.

---

<span id="class_RenderingServer_method_environment_set_sky"></span>

void **environment_set_sky** ( env: [RID](class_rid.md#class_RID), sky: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_sky)

Sets the [Sky](class_sky.md#class_Sky) to be used as the environment's background when using *BGMode* sky. Equivalent to [Environment.sky](class_environment.md#class_Environment_property_sky).

---

<span id="class_RenderingServer_method_environment_set_sky_custom_fov"></span>

void **environment_set_sky_custom_fov** ( env: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_sky_custom_fov)

Sets a custom field of view for the background [Sky](class_sky.md#class_Sky). Equivalent to [Environment.sky_custom_fov](class_environment.md#class_Environment_property_sky_custom_fov).

---

<span id="class_RenderingServer_method_environment_set_sky_orientation"></span>

void **environment_set_sky_orientation** ( env: [RID](class_rid.md#class_RID), orientation: [Basis](class_basis.md#class_Basis) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_sky_orientation)

Sets the rotation of the background [Sky](class_sky.md#class_Sky) expressed as a [Basis](class_basis.md#class_Basis). Equivalent to [Environment.sky_rotation](class_environment.md#class_Environment_property_sky_rotation), where the rotation vector is used to construct the [Basis](class_basis.md#class_Basis).

---

<span id="class_RenderingServer_method_environment_set_ssao"></span>

void **environment_set_ssao** ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), radius: [float](class_float.md#class_float), intensity: [float](class_float.md#class_float), power: [float](class_float.md#class_float), detail: [float](class_float.md#class_float), horizon: [float](class_float.md#class_float), sharpness: [float](class_float.md#class_float), light_affect: [float](class_float.md#class_float), ao_channel_affect: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_ssao)

Sets the variables to be used with the screen-space ambient occlusion (SSAO) post-process effect. See [Environment](class_environment.md#class_Environment) for more details.

---

<span id="class_RenderingServer_method_environment_set_ssao_quality"></span>

void **environment_set_ssao_quality** ( quality: [EnvironmentSSAOQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSAOQuality), half_size: [bool](class_bool.md#class_bool), adaptive_target: [float](class_float.md#class_float), blur_passes: [int](class_int.md#class_int), fadeout_from: [float](class_float.md#class_float), fadeout_to: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_ssao_quality)

Sets the quality level of the screen-space ambient occlusion (SSAO) post-process effect. See [Environment](class_environment.md#class_Environment) for more details.

---

<span id="class_RenderingServer_method_environment_set_ssil_quality"></span>

void **environment_set_ssil_quality** ( quality: [EnvironmentSSILQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSILQuality), half_size: [bool](class_bool.md#class_bool), adaptive_target: [float](class_float.md#class_float), blur_passes: [int](class_int.md#class_int), fadeout_from: [float](class_float.md#class_float), fadeout_to: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_ssil_quality)

Sets the quality level of the screen-space indirect lighting (SSIL) post-process effect. See [Environment](class_environment.md#class_Environment) for more details.

---

<span id="class_RenderingServer_method_environment_set_ssr"></span>

void **environment_set_ssr** ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), max_steps: [int](class_int.md#class_int), fade_in: [float](class_float.md#class_float), fade_out: [float](class_float.md#class_float), depth_tolerance: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_ssr)

Sets the variables to be used with the screen-space reflections (SSR) post-process effect. See [Environment](class_environment.md#class_Environment) for more details.

---

<span id="class_RenderingServer_method_environment_set_ssr_half_size"></span>

void **environment_set_ssr_half_size** ( half_size: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_ssr_half_size)

Sets whether screen-space reflections will be rendered at full or half size. Half size is faster, but may look pixelated or cause flickering.

---

<span id="class_RenderingServer_method_environment_set_ssr_roughness_quality"></span>

void **environment_set_ssr_roughness_quality** ( quality: [EnvironmentSSRRoughnessQuality](class_renderingserver.md#enum_RenderingServer_EnvironmentSSRRoughnessQuality) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_ssr_roughness_quality)

**Deprecated:** This option no longer does anything.

---

<span id="class_RenderingServer_method_environment_set_tonemap"></span>

void **environment_set_tonemap** ( env: [RID](class_rid.md#class_RID), tone_mapper: [EnvironmentToneMapper](class_renderingserver.md#enum_RenderingServer_EnvironmentToneMapper), exposure: [float](class_float.md#class_float), white: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_tonemap)

Sets the variables to be used with the "tonemap" post-process effect. See [Environment](class_environment.md#class_Environment) for more details.

---

<span id="class_RenderingServer_method_environment_set_tonemap_agx_contrast"></span>

void **environment_set_tonemap_agx_contrast** ( env: [RID](class_rid.md#class_RID), agx_contrast: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_tonemap_agx_contrast)

See [Environment.tonemap_agx_contrast](class_environment.md#class_Environment_property_tonemap_agx_contrast) for more details.

---

<span id="class_RenderingServer_method_environment_set_volumetric_fog"></span>

void **environment_set_volumetric_fog** ( env: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), density: [float](class_float.md#class_float), albedo: [Color](class_color.md#class_Color), emission: [Color](class_color.md#class_Color), emission_energy: [float](class_float.md#class_float), anisotropy: [float](class_float.md#class_float), length: [float](class_float.md#class_float), p_detail_spread: [float](class_float.md#class_float), gi_inject: [float](class_float.md#class_float), temporal_reprojection: [bool](class_bool.md#class_bool), temporal_reprojection_amount: [float](class_float.md#class_float), ambient_inject: [float](class_float.md#class_float), sky_affect: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_volumetric_fog)

Sets the variables to be used with the volumetric fog post-process effect. See [Environment](class_environment.md#class_Environment) for more details.

---

<span id="class_RenderingServer_method_environment_set_volumetric_fog_filter_active"></span>

void **environment_set_volumetric_fog_filter_active** ( active: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_volumetric_fog_filter_active)

Enables filtering of the volumetric fog scattering buffer. This results in much smoother volumes with very few under-sampling artifacts.

---

<span id="class_RenderingServer_method_environment_set_volumetric_fog_volume_size"></span>

void **environment_set_volumetric_fog_volume_size** ( size: [int](class_int.md#class_int), depth: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_environment_set_volumetric_fog_volume_size)

Sets the resolution of the volumetric fog's froxel buffer. `size` is modified by the screen's aspect ratio and then used to set the width and height of the buffer. While `depth` is directly used to set the depth of the buffer.

---

<span id="class_RenderingServer_method_fog_volume_create"></span>

[RID](class_rid.md#class_RID) **fog_volume_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_fog_volume_create)

Creates a new fog volume and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `fog_volume_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent node is [FogVolume](class_fogvolume.md#class_FogVolume).

---

<span id="class_RenderingServer_method_fog_volume_set_material"></span>

void **fog_volume_set_material** ( fog_volume: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_fog_volume_set_material)

Sets the [Material](class_material.md#class_Material) of the fog volume. Can be either a [FogMaterial](class_fogmaterial.md#class_FogMaterial) or a custom [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial).

---

<span id="class_RenderingServer_method_fog_volume_set_shape"></span>

void **fog_volume_set_shape** ( fog_volume: [RID](class_rid.md#class_RID), shape: [FogVolumeShape](class_renderingserver.md#enum_RenderingServer_FogVolumeShape) ) [🔗](class_renderingserver.md#class_RenderingServer_method_fog_volume_set_shape)

Sets the shape of the fog volume to either [FOG_VOLUME_SHAPE_ELLIPSOID](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID), [FOG_VOLUME_SHAPE_CONE](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE), [FOG_VOLUME_SHAPE_CYLINDER](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER), [FOG_VOLUME_SHAPE_BOX](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX) or [FOG_VOLUME_SHAPE_WORLD](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_WORLD).

---

<span id="class_RenderingServer_method_fog_volume_set_size"></span>

void **fog_volume_set_size** ( fog_volume: [RID](class_rid.md#class_RID), size: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_renderingserver.md#class_RenderingServer_method_fog_volume_set_size)

Sets the size of the fog volume when shape is [FOG_VOLUME_SHAPE_ELLIPSOID](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID), [FOG_VOLUME_SHAPE_CONE](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE), [FOG_VOLUME_SHAPE_CYLINDER](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER) or [FOG_VOLUME_SHAPE_BOX](class_renderingserver.md#class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX).

---

<span id="class_RenderingServer_method_force_draw"></span>

void **force_draw** ( swap_buffers: [bool](class_bool.md#class_bool) = true, frame_step: [float](class_float.md#class_float) = 0.0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_force_draw)

Forces redrawing of all viewports at once. Must be called from the main thread.

---

<span id="class_RenderingServer_method_force_sync"></span>

void **force_sync** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_force_sync)

Forces a synchronization between the CPU and GPU, which may be required in certain cases. Only call this when needed, as CPU-GPU synchronization has a performance cost.

---

<span id="class_RenderingServer_method_free_rid"></span>

void **free_rid** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_free_rid)

Tries to free an object in the RenderingServer. To avoid memory leaks, this should be called after using an object as memory management does not occur automatically when using RenderingServer directly.

---

<span id="class_RenderingServer_method_get_current_rendering_driver_name"></span>

[String](class_string.md#class_String) **get_current_rendering_driver_name** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_get_current_rendering_driver_name)

Returns the name of the current rendering driver. This can be `vulkan`, `d3d12`, `metal`, `opengl3`, `opengl3_es`, or `opengl3_angle`. See also [get_current_rendering_method()](class_renderingserver.md#class_RenderingServer_method_get_current_rendering_method).

When ProjectSettings.rendering/renderer/rendering_method is `forward_plus` or `mobile`, the rendering driver is determined by ProjectSettings.rendering/rendering_device/driver.

When ProjectSettings.rendering/renderer/rendering_method is `gl_compatibility`, the rendering driver is determined by ProjectSettings.rendering/gl_compatibility/driver.

The rendering driver is also determined by the `--rendering-driver` command line argument that overrides this project setting, or an automatic fallback that is applied depending on the hardware.

---

<span id="class_RenderingServer_method_get_current_rendering_method"></span>

[String](class_string.md#class_String) **get_current_rendering_method** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_get_current_rendering_method)

Returns the name of the current rendering method. This can be `forward_plus`, `mobile`, or `gl_compatibility`. See also [get_current_rendering_driver_name()](class_renderingserver.md#class_RenderingServer_method_get_current_rendering_driver_name).

The rendering method is determined by ProjectSettings.rendering/renderer/rendering_method, the `--rendering-method` command line argument that overrides this project setting, or an automatic fallback that is applied depending on the hardware.

---

<span id="class_RenderingServer_method_get_default_clear_color"></span>

[Color](class_color.md#class_Color) **get_default_clear_color** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_get_default_clear_color)

Returns the default clear color which is used when a specific clear color has not been selected. See also [set_default_clear_color()](class_renderingserver.md#class_RenderingServer_method_set_default_clear_color).

---

<span id="class_RenderingServer_method_get_frame_setup_time_cpu"></span>

[float](class_float.md#class_float) **get_frame_setup_time_cpu** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_get_frame_setup_time_cpu)

Returns the time taken to setup rendering on the CPU in milliseconds. This value is shared across all viewports and does *not* require [viewport_set_measure_render_time()](class_renderingserver.md#class_RenderingServer_method_viewport_set_measure_render_time) to be enabled on a viewport to be queried. See also [viewport_get_measured_render_time_cpu()](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_cpu).

---

<span id="class_RenderingServer_method_get_rendering_device"></span>

[RenderingDevice](class_renderingdevice.md#class_RenderingDevice) **get_rendering_device** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_get_rendering_device)

Returns the global RenderingDevice.

 **Note:** When using the OpenGL rendering driver or when running in headless mode, this function always returns `null`.

---

<span id="class_RenderingServer_method_get_rendering_info"></span>

[int](class_int.md#class_int) **get_rendering_info** ( info: [RenderingInfo](class_renderingserver.md#enum_RenderingServer_RenderingInfo) ) [🔗](class_renderingserver.md#class_RenderingServer_method_get_rendering_info)

Returns a statistic about the rendering engine which can be used for performance profiling. See also [viewport_get_render_info()](class_renderingserver.md#class_RenderingServer_method_viewport_get_render_info), which returns information specific to a viewport.

 **Note:** Only 3D rendering is currently taken into account by some of these values, such as the number of draw calls.

 **Note:** Rendering information is not available until at least 2 frames have been rendered by the engine. If rendering information is not available, [get_rendering_info()](class_renderingserver.md#class_RenderingServer_method_get_rendering_info) returns `0`. To print rendering information in `_ready()` successfully, use the following:

::

    func _ready():
        for _i in 2:
            await get_tree().process_frame

        print(RenderingServer.get_rendering_info(RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME))

---

<span id="class_RenderingServer_method_get_shader_parameter_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **get_shader_parameter_list** ( shader: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_get_shader_parameter_list)

Returns the parameters of a shader.

---

<span id="class_RenderingServer_method_get_test_cube"></span>

[RID](class_rid.md#class_RID) **get_test_cube** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_get_test_cube)

Returns the RID of the test cube. This mesh will be created and returned on the first call to [get_test_cube()](class_renderingserver.md#class_RenderingServer_method_get_test_cube), then it will be cached for subsequent calls. See also [make_sphere_mesh()](class_renderingserver.md#class_RenderingServer_method_make_sphere_mesh).

---

<span id="class_RenderingServer_method_get_test_texture"></span>

[RID](class_rid.md#class_RID) **get_test_texture** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_get_test_texture)

Returns the RID of a 256×256 texture with a testing pattern on it (in [Image.FORMAT_RGB8](class_image.md#class_Image_constant_FORMAT_RGB8) format). This texture will be created and returned on the first call to [get_test_texture()](class_renderingserver.md#class_RenderingServer_method_get_test_texture), then it will be cached for subsequent calls. See also [get_white_texture()](class_renderingserver.md#class_RenderingServer_method_get_white_texture).

 **Example:** Get the test texture and apply it to a [Sprite2D](class_sprite2d.md#class_Sprite2D) node:

::

    var texture_rid = RenderingServer.get_test_texture()
    var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
    $Sprite2D.texture = texture

---

<span id="class_RenderingServer_method_get_video_adapter_api_version"></span>

[String](class_string.md#class_String) **get_video_adapter_api_version** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_api_version)

Returns the version of the graphics video adapter *currently in use* (e.g. "1.2.189" for Vulkan, "3.3.0 NVIDIA 510.60.02" for OpenGL). This version may be different from the actual latest version supported by the hardware, as Godot may not always request the latest version. See also [OS.get_video_adapter_driver_info()](class_os.md#class_OS_method_get_video_adapter_driver_info).

 **Note:** When running a headless or server binary, this function returns an empty string.

---

<span id="class_RenderingServer_method_get_video_adapter_name"></span>

[String](class_string.md#class_String) **get_video_adapter_name** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_name)

Returns the name of the video adapter (e.g. "GeForce GTX 1080/PCIe/SSE2").

 **Note:** When running a headless or server binary, this function returns an empty string.

 **Note:** On the web platform, some browsers such as Firefox may report a different, fixed GPU name such as "GeForce GTX 980" (regardless of the user's actual GPU model). This is done to make fingerprinting more difficult.

---

<span id="class_RenderingServer_method_get_video_adapter_type"></span>

[DeviceType](class_renderingdevice.md#enum_RenderingDevice_DeviceType) **get_video_adapter_type** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_type)

Returns the type of the video adapter. Since dedicated graphics cards from a given generation will *usually* be significantly faster than integrated graphics made in the same generation, the device type can be used as a basis for automatic graphics settings adjustment. However, this is not always true, so make sure to provide users with a way to manually override graphics settings.

 **Note:** When using the OpenGL rendering driver or when running in headless mode, this function always returns [RenderingDevice.DEVICE_TYPE_OTHER](class_renderingdevice.md#class_RenderingDevice_constant_DEVICE_TYPE_OTHER).

---

<span id="class_RenderingServer_method_get_video_adapter_vendor"></span>

[String](class_string.md#class_String) **get_video_adapter_vendor** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_vendor)

Returns the vendor of the video adapter (e.g. "NVIDIA Corporation").

 **Note:** When running a headless or server binary, this function returns an empty string.

---

<span id="class_RenderingServer_method_get_white_texture"></span>

[RID](class_rid.md#class_RID) **get_white_texture** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_get_white_texture)

Returns the ID of a 4×4 white texture (in [Image.FORMAT_RGB8](class_image.md#class_Image_constant_FORMAT_RGB8) format). This texture will be created and returned on the first call to [get_white_texture()](class_renderingserver.md#class_RenderingServer_method_get_white_texture), then it will be cached for subsequent calls. See also [get_test_texture()](class_renderingserver.md#class_RenderingServer_method_get_test_texture).

 **Example:** Get the white texture and apply it to a [Sprite2D](class_sprite2d.md#class_Sprite2D) node:

::

    var texture_rid = RenderingServer.get_white_texture()
    var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
    $Sprite2D.texture = texture

---

<span id="class_RenderingServer_method_gi_set_use_half_resolution"></span>

void **gi_set_use_half_resolution** ( half_resolution: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_gi_set_use_half_resolution)

If `half_resolution` is `true`, renders [VoxelGI](class_voxelgi.md#class_VoxelGI) and SDFGI ([Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled)) buffers at halved resolution on each axis (e.g. 960×540 when the viewport size is 1920×1080). This improves performance significantly when VoxelGI or SDFGI is enabled, at the cost of artifacts that may be visible on polygon edges. The loss in quality becomes less noticeable as the viewport resolution increases. [LightmapGI](class_lightmapgi.md#class_LightmapGI) rendering is not affected by this setting. Equivalent to ProjectSettings.rendering/global_illumination/gi/use_half_resolution.

---

<span id="class_RenderingServer_method_global_shader_parameter_add"></span>

void **global_shader_parameter_add** ( name: [StringName](class_stringname.md#class_StringName), type: [GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType), default_value: [Variant](class_variant.md#class_Variant) ) [🔗](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_add)

Creates a new global shader uniform.

 **Note:** Global shader parameter names are case-sensitive.

---

<span id="class_RenderingServer_method_global_shader_parameter_get"></span>

[Variant](class_variant.md#class_Variant) **global_shader_parameter_get** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_get)

Returns the value of the global shader uniform specified by `name`.

 **Note:** [global_shader_parameter_get()](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_get) has a large performance penalty as the rendering thread needs to synchronize with the calling thread, which is slow. Do not use this method during gameplay to avoid stuttering. If you need to read values in a script after setting them, consider creating an autoload where you store the values you need to query at the same time you're setting them as global parameters.

---

<span id="class_RenderingServer_method_global_shader_parameter_get_list"></span>

[Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] **global_shader_parameter_get_list** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_get_list)

Returns the list of global shader uniform names.

 **Note:** [global_shader_parameter_get()](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_get) has a large performance penalty as the rendering thread needs to synchronize with the calling thread, which is slow. Do not use this method during gameplay to avoid stuttering. If you need to read values in a script after setting them, consider creating an autoload where you store the values you need to query at the same time you're setting them as global parameters.

---

<span id="class_RenderingServer_method_global_shader_parameter_get_type"></span>

[GlobalShaderParameterType](class_renderingserver.md#enum_RenderingServer_GlobalShaderParameterType) **global_shader_parameter_get_type** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_get_type)

Returns the type associated to the global shader uniform specified by `name`.

 **Note:** [global_shader_parameter_get()](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_get) has a large performance penalty as the rendering thread needs to synchronize with the calling thread, which is slow. Do not use this method during gameplay to avoid stuttering. If you need to read values in a script after setting them, consider creating an autoload where you store the values you need to query at the same time you're setting them as global parameters.

---

<span id="class_RenderingServer_method_global_shader_parameter_remove"></span>

void **global_shader_parameter_remove** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_remove)

Removes the global shader uniform specified by `name`.

---

<span id="class_RenderingServer_method_global_shader_parameter_set"></span>

void **global_shader_parameter_set** ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_set)

Sets the global shader uniform `name` to `value`.

---

<span id="class_RenderingServer_method_global_shader_parameter_set_override"></span>

void **global_shader_parameter_set_override** ( name: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_renderingserver.md#class_RenderingServer_method_global_shader_parameter_set_override)

Overrides the global shader uniform `name` with `value`. Equivalent to the [ShaderGlobalsOverride](class_shaderglobalsoverride.md#class_ShaderGlobalsOverride) node.

---

<span id="class_RenderingServer_method_has_changed"></span>

[bool](class_bool.md#class_bool) **has_changed** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_has_changed)

Returns `true` if changes have been made to the RenderingServer's data. [force_draw()](class_renderingserver.md#class_RenderingServer_method_force_draw) is usually called if this happens.

---

<span id="class_RenderingServer_method_has_feature"></span>

[bool](class_bool.md#class_bool) **has_feature** ( feature: [Features](class_renderingserver.md#enum_RenderingServer_Features) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_has_feature)

**Deprecated:** This method has not been used since Godot 3.0.

This method does nothing and always returns `false`.

---

<span id="class_RenderingServer_method_has_os_feature"></span>

[bool](class_bool.md#class_bool) **has_os_feature** ( feature: [String](class_string.md#class_String) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_has_os_feature)

Returns `true` if the OS supports a certain `feature`. Features might be `s3tc`, `etc`, and `etc2`.

---

<span id="class_RenderingServer_method_instance_attach_object_instance_id"></span>

void **instance_attach_object_instance_id** ( instance: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_attach_object_instance_id)

Attaches a unique Object ID to instance. Object ID must be attached to instance for proper culling with [instances_cull_aabb()](class_renderingserver.md#class_RenderingServer_method_instances_cull_aabb), [instances_cull_convex()](class_renderingserver.md#class_RenderingServer_method_instances_cull_convex), and [instances_cull_ray()](class_renderingserver.md#class_RenderingServer_method_instances_cull_ray).

---

<span id="class_RenderingServer_method_instance_attach_skeleton"></span>

void **instance_attach_skeleton** ( instance: [RID](class_rid.md#class_RID), skeleton: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_attach_skeleton)

Attaches a skeleton to an instance. Removes the previous skeleton from the instance.

---

<span id="class_RenderingServer_method_instance_create"></span>

[RID](class_rid.md#class_RID) **instance_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_create)

Creates a visual instance and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `instance_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

An instance is a way of placing a 3D object in the scenario. Objects like particles, meshes, reflection probes and decals need to be associated with an instance to be visible in the scenario using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base).

 **Note:** The equivalent node is [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D).

---

<span id="class_RenderingServer_method_instance_create2"></span>

[RID](class_rid.md#class_RID) **instance_create2** ( base: [RID](class_rid.md#class_RID), scenario: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_create2)

Creates a visual instance, adds it to the RenderingServer, and sets both base and scenario. It can be accessed with the RID that is returned. This RID will be used in all `instance_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method. This is a shorthand for using [instance_create()](class_renderingserver.md#class_RenderingServer_method_instance_create) and setting the base and scenario manually.

---

<span id="class_RenderingServer_method_instance_geometry_get_shader_parameter"></span>

[Variant](class_variant.md#class_Variant) **instance_geometry_get_shader_parameter** ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_get_shader_parameter)

Returns the value of the per-instance shader uniform from the specified 3D geometry instance. Equivalent to [GeometryInstance3D.get_instance_shader_parameter()](class_geometryinstance3d.md#class_GeometryInstance3D_method_get_instance_shader_parameter).

 **Note:** Per-instance shader parameter names are case-sensitive.

---

<span id="class_RenderingServer_method_instance_geometry_get_shader_parameter_default_value"></span>

[Variant](class_variant.md#class_Variant) **instance_geometry_get_shader_parameter_default_value** ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_get_shader_parameter_default_value)

Returns the default value of the per-instance shader uniform from the specified 3D geometry instance. Equivalent to [GeometryInstance3D.get_instance_shader_parameter()](class_geometryinstance3d.md#class_GeometryInstance3D_method_get_instance_shader_parameter).

---

<span id="class_RenderingServer_method_instance_geometry_get_shader_parameter_list"></span>

[Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\] **instance_geometry_get_shader_parameter_list** ( instance: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_get_shader_parameter_list)

Returns a dictionary of per-instance shader uniform names of the per-instance shader uniform from the specified 3D geometry instance. The returned dictionary is in PropertyInfo format, with the keys `name`, `class_name`, `type`, `hint`, `hint_string` and `usage`. Equivalent to [GeometryInstance3D.get_instance_shader_parameter()](class_geometryinstance3d.md#class_GeometryInstance3D_method_get_instance_shader_parameter).

---

<span id="class_RenderingServer_method_instance_geometry_set_cast_shadows_setting"></span>

void **instance_geometry_set_cast_shadows_setting** ( instance: [RID](class_rid.md#class_RID), shadow_casting_setting: [ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_cast_shadows_setting)

Sets the shadow casting setting. Equivalent to [GeometryInstance3D.cast_shadow](class_geometryinstance3d.md#class_GeometryInstance3D_property_cast_shadow).

---

<span id="class_RenderingServer_method_instance_geometry_set_flag"></span>

void **instance_geometry_set_flag** ( instance: [RID](class_rid.md#class_RID), flag: [InstanceFlags](class_renderingserver.md#enum_RenderingServer_InstanceFlags), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_flag)

Sets the `flag` for a given `instance` to `enabled`.

---

<span id="class_RenderingServer_method_instance_geometry_set_lightmap"></span>

void **instance_geometry_set_lightmap** ( instance: [RID](class_rid.md#class_RID), lightmap: [RID](class_rid.md#class_RID), lightmap_uv_scale: [Rect2](class_rect2.md#class_Rect2), lightmap_slice: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_lightmap)

Sets the lightmap GI instance to use for the specified 3D geometry instance. The lightmap UV scale for the specified instance (equivalent to [GeometryInstance3D.gi_lightmap_scale](class_geometryinstance3d.md#class_GeometryInstance3D_property_gi_lightmap_scale)) and lightmap atlas slice must also be specified.

---

<span id="class_RenderingServer_method_instance_geometry_set_lod_bias"></span>

void **instance_geometry_set_lod_bias** ( instance: [RID](class_rid.md#class_RID), lod_bias: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_lod_bias)

Sets the level of detail bias to use when rendering the specified 3D geometry instance. Higher values result in higher detail from further away. Equivalent to [GeometryInstance3D.lod_bias](class_geometryinstance3d.md#class_GeometryInstance3D_property_lod_bias).

---

<span id="class_RenderingServer_method_instance_geometry_set_material_overlay"></span>

void **instance_geometry_set_material_overlay** ( instance: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_material_overlay)

Sets a material that will be rendered for all surfaces on top of active materials for the mesh associated with this instance. Equivalent to [GeometryInstance3D.material_overlay](class_geometryinstance3d.md#class_GeometryInstance3D_property_material_overlay).

---

<span id="class_RenderingServer_method_instance_geometry_set_material_override"></span>

void **instance_geometry_set_material_override** ( instance: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_material_override)

Sets a material that will override the material for all surfaces on the mesh associated with this instance. Equivalent to [GeometryInstance3D.material_override](class_geometryinstance3d.md#class_GeometryInstance3D_property_material_override).

---

<span id="class_RenderingServer_method_instance_geometry_set_shader_parameter"></span>

void **instance_geometry_set_shader_parameter** ( instance: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_shader_parameter)

Sets the per-instance shader uniform on the specified 3D geometry instance. Equivalent to [GeometryInstance3D.set_instance_shader_parameter()](class_geometryinstance3d.md#class_GeometryInstance3D_method_set_instance_shader_parameter).

---

<span id="class_RenderingServer_method_instance_geometry_set_transparency"></span>

void **instance_geometry_set_transparency** ( instance: [RID](class_rid.md#class_RID), transparency: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_transparency)

Sets the transparency for the given geometry instance. Equivalent to [GeometryInstance3D.transparency](class_geometryinstance3d.md#class_GeometryInstance3D_property_transparency).

A transparency of `0.0` is fully opaque, while `1.0` is fully transparent. Values greater than `0.0` (exclusive) will force the geometry's materials to go through the transparent pipeline, which is slower to render and can exhibit rendering issues due to incorrect transparency sorting. However, unlike using a transparent material, setting `transparency` to a value greater than `0.0` (exclusive) will *not* disable shadow rendering.

In spatial shaders, `1.0 - transparency` is set as the default value of the `ALPHA` built-in.

 **Note:** `transparency` is clamped between `0.0` and `1.0`, so this property cannot be used to make transparent materials more opaque than they originally are.

---

<span id="class_RenderingServer_method_instance_geometry_set_visibility_range"></span>

void **instance_geometry_set_visibility_range** ( instance: [RID](class_rid.md#class_RID), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float), min_margin: [float](class_float.md#class_float), max_margin: [float](class_float.md#class_float), fade_mode: [VisibilityRangeFadeMode](class_renderingserver.md#enum_RenderingServer_VisibilityRangeFadeMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_visibility_range)

Sets the visibility range values for the given geometry instance. Equivalent to [GeometryInstance3D.visibility_range_begin](class_geometryinstance3d.md#class_GeometryInstance3D_property_visibility_range_begin) and related properties.

---

<span id="class_RenderingServer_method_instance_set_base"></span>

void **instance_set_base** ( instance: [RID](class_rid.md#class_RID), base: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_base)

Sets the base of the instance. A base can be any of the 3D objects that are created in the RenderingServer that can be displayed. For example, any of the light types, mesh, multimesh, particle system, reflection probe, decal, lightmap, voxel GI and visibility notifiers are all types that can be set as the base of an instance in order to be displayed in the scenario.

---

<span id="class_RenderingServer_method_instance_set_blend_shape_weight"></span>

void **instance_set_blend_shape_weight** ( instance: [RID](class_rid.md#class_RID), shape: [int](class_int.md#class_int), weight: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_blend_shape_weight)

Sets the weight for a given blend shape associated with this instance.

---

<span id="class_RenderingServer_method_instance_set_custom_aabb"></span>

void **instance_set_custom_aabb** ( instance: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_custom_aabb)

Sets a custom AABB to use when culling objects from the view frustum. Equivalent to setting [GeometryInstance3D.custom_aabb](class_geometryinstance3d.md#class_GeometryInstance3D_property_custom_aabb).

---

<span id="class_RenderingServer_method_instance_set_extra_visibility_margin"></span>

void **instance_set_extra_visibility_margin** ( instance: [RID](class_rid.md#class_RID), margin: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_extra_visibility_margin)

Sets a margin to increase the size of the AABB when culling objects from the view frustum. This allows you to avoid culling objects that fall outside the view frustum. Equivalent to [GeometryInstance3D.extra_cull_margin](class_geometryinstance3d.md#class_GeometryInstance3D_property_extra_cull_margin).

---

<span id="class_RenderingServer_method_instance_set_ignore_culling"></span>

void **instance_set_ignore_culling** ( instance: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_ignore_culling)

If `true`, ignores both frustum and occlusion culling on the specified 3D geometry instance. This is not the same as [GeometryInstance3D.ignore_occlusion_culling](class_geometryinstance3d.md#class_GeometryInstance3D_property_ignore_occlusion_culling), which only ignores occlusion culling and leaves frustum culling intact.

---

<span id="class_RenderingServer_method_instance_set_layer_mask"></span>

void **instance_set_layer_mask** ( instance: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_layer_mask)

Sets the render layers that this instance will be drawn to. Equivalent to [VisualInstance3D.layers](class_visualinstance3d.md#class_VisualInstance3D_property_layers).

---

<span id="class_RenderingServer_method_instance_set_pivot_data"></span>

void **instance_set_pivot_data** ( instance: [RID](class_rid.md#class_RID), sorting_offset: [float](class_float.md#class_float), use_aabb_center: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_pivot_data)

Sets the sorting offset and switches between using the bounding box or instance origin for depth sorting.

---

<span id="class_RenderingServer_method_instance_set_scenario"></span>

void **instance_set_scenario** ( instance: [RID](class_rid.md#class_RID), scenario: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_scenario)

Sets the scenario that the instance is in. The scenario is the 3D world that the objects will be displayed in.

---

<span id="class_RenderingServer_method_instance_set_surface_override_material"></span>

void **instance_set_surface_override_material** ( instance: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), material: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_surface_override_material)

Sets the override material of a specific surface. Equivalent to [MeshInstance3D.set_surface_override_material()](class_meshinstance3d.md#class_MeshInstance3D_method_set_surface_override_material).

---

<span id="class_RenderingServer_method_instance_set_transform"></span>

void **instance_set_transform** ( instance: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_transform)

Sets the world space transform of the instance. Equivalent to [Node3D.global_transform](class_node3d.md#class_Node3D_property_global_transform).

---

<span id="class_RenderingServer_method_instance_set_visibility_parent"></span>

void **instance_set_visibility_parent** ( instance: [RID](class_rid.md#class_RID), parent: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_visibility_parent)

Sets the visibility parent for the given instance. Equivalent to [Node3D.visibility_parent](class_node3d.md#class_Node3D_property_visibility_parent).

---

<span id="class_RenderingServer_method_instance_set_visible"></span>

void **instance_set_visible** ( instance: [RID](class_rid.md#class_RID), visible: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_set_visible)

Sets whether an instance is drawn or not. Equivalent to [Node3D.visible](class_node3d.md#class_Node3D_property_visible).

---

<span id="class_RenderingServer_method_instance_teleport"></span>

void **instance_teleport** ( instance: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_instance_teleport)

Resets motion vectors and other interpolated values. Use this *after* teleporting a mesh from one position to another to avoid ghosting artifacts.

---

<span id="class_RenderingServer_method_instances_cull_aabb"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **instances_cull_aabb** ( aabb: [AABB](class_aabb.md#class_AABB), scenario: [RID](class_rid.md#class_RID) = RID() ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_instances_cull_aabb)

Returns an array of object IDs intersecting with the provided AABB. Only 3D nodes that inherit from [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) are considered, such as [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) or [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D). Use @GlobalScope.instance_from_id() to obtain the actual nodes. A scenario RID must be provided, which is available in the [World3D](class_world3d.md#class_World3D) you want to query. This forces an update for all resources queued to update.

 **Warning:** This function is primarily intended for editor usage. For in-game use cases, prefer physics collision.

---

<span id="class_RenderingServer_method_instances_cull_convex"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **instances_cull_convex** ( convex: [Array](class_array.md#class_Array)\[[Plane](class_plane.md#class_Plane)\], scenario: [RID](class_rid.md#class_RID) = RID() ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_instances_cull_convex)

Returns an array of object IDs intersecting with the provided convex shape. Only 3D nodes that inherit from [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) are considered, such as [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) or [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D). Use @GlobalScope.instance_from_id() to obtain the actual nodes. A scenario RID must be provided, which is available in the [World3D](class_world3d.md#class_World3D) you want to query. This forces an update for all resources queued to update.

 **Warning:** This function is primarily intended for editor usage. For in-game use cases, prefer physics collision.

---

<span id="class_RenderingServer_method_instances_cull_ray"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **instances_cull_ray** ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), scenario: [RID](class_rid.md#class_RID) = RID() ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_instances_cull_ray)

Returns an array of object IDs intersecting with the provided 3D ray. Only 3D nodes that inherit from [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) are considered, such as [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) or [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D). Use @GlobalScope.instance_from_id() to obtain the actual nodes. A scenario RID must be provided, which is available in the [World3D](class_world3d.md#class_World3D) you want to query. This forces an update for all resources queued to update.

 **Warning:** This function is primarily intended for editor usage. For in-game use cases, prefer physics collision.

---

<span id="class_RenderingServer_method_is_on_render_thread"></span>

[bool](class_bool.md#class_bool) **is_on_render_thread** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_is_on_render_thread)

Returns `true` if our code is currently executing on the rendering thread.

---

<span id="class_RenderingServer_method_light_directional_set_blend_splits"></span>

void **light_directional_set_blend_splits** ( light: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_directional_set_blend_splits)

If `true`, this directional light will blend between shadow map splits resulting in a smoother transition between them. Equivalent to [DirectionalLight3D.directional_shadow_blend_splits](class_directionallight3d.md#class_DirectionalLight3D_property_directional_shadow_blend_splits).

---

<span id="class_RenderingServer_method_light_directional_set_shadow_mode"></span>

void **light_directional_set_shadow_mode** ( light: [RID](class_rid.md#class_RID), mode: [LightDirectionalShadowMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalShadowMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_directional_set_shadow_mode)

Sets the shadow mode for this directional light. Equivalent to [DirectionalLight3D.directional_shadow_mode](class_directionallight3d.md#class_DirectionalLight3D_property_directional_shadow_mode).

---

<span id="class_RenderingServer_method_light_directional_set_sky_mode"></span>

void **light_directional_set_sky_mode** ( light: [RID](class_rid.md#class_RID), mode: [LightDirectionalSkyMode](class_renderingserver.md#enum_RenderingServer_LightDirectionalSkyMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_directional_set_sky_mode)

If `true`, this light will not be used for anything except sky shaders. Use this for lights that impact your sky shader that you may want to hide from affecting the rest of the scene. For example, you may want to enable this when the sun in your sky shader falls below the horizon.

---

<span id="class_RenderingServer_method_light_omni_set_shadow_mode"></span>

void **light_omni_set_shadow_mode** ( light: [RID](class_rid.md#class_RID), mode: [LightOmniShadowMode](class_renderingserver.md#enum_RenderingServer_LightOmniShadowMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_omni_set_shadow_mode)

Sets whether to use a dual paraboloid or a cubemap for the shadow map. Dual paraboloid is faster but may suffer from artifacts. Equivalent to [OmniLight3D.omni_shadow_mode](class_omnilight3d.md#class_OmniLight3D_property_omni_shadow_mode).

---

<span id="class_RenderingServer_method_light_projectors_set_filter"></span>

void **light_projectors_set_filter** ( filter: [LightProjectorFilter](class_renderingserver.md#enum_RenderingServer_LightProjectorFilter) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_projectors_set_filter)

Sets the texture filter mode to use when rendering light projectors. This parameter is global and cannot be set on a per-light basis.

---

<span id="class_RenderingServer_method_light_set_bake_mode"></span>

void **light_set_bake_mode** ( light: [RID](class_rid.md#class_RID), bake_mode: [LightBakeMode](class_renderingserver.md#enum_RenderingServer_LightBakeMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_bake_mode)

Sets the bake mode to use for the specified 3D light. Equivalent to [Light3D.light_bake_mode](class_light3d.md#class_Light3D_property_light_bake_mode).

---

<span id="class_RenderingServer_method_light_set_color"></span>

void **light_set_color** ( light: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_color)

Sets the color of the light. Equivalent to [Light3D.light_color](class_light3d.md#class_Light3D_property_light_color).

---

<span id="class_RenderingServer_method_light_set_cull_mask"></span>

void **light_set_cull_mask** ( light: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_cull_mask)

Sets the cull mask for this 3D light. Lights only affect objects in the selected layers. Equivalent to [Light3D.light_cull_mask](class_light3d.md#class_Light3D_property_light_cull_mask).

---

<span id="class_RenderingServer_method_light_set_distance_fade"></span>

void **light_set_distance_fade** ( decal: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool), begin: [float](class_float.md#class_float), shadow: [float](class_float.md#class_float), length: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_distance_fade)

Sets the distance fade for this 3D light. This acts as a form of level of detail (LOD) and can be used to improve performance. Equivalent to [Light3D.distance_fade_enabled](class_light3d.md#class_Light3D_property_distance_fade_enabled), [Light3D.distance_fade_begin](class_light3d.md#class_Light3D_property_distance_fade_begin), [Light3D.distance_fade_shadow](class_light3d.md#class_Light3D_property_distance_fade_shadow), and [Light3D.distance_fade_length](class_light3d.md#class_Light3D_property_distance_fade_length).

---

<span id="class_RenderingServer_method_light_set_max_sdfgi_cascade"></span>

void **light_set_max_sdfgi_cascade** ( light: [RID](class_rid.md#class_RID), cascade: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_max_sdfgi_cascade)

Sets the maximum SDFGI cascade in which the 3D light's indirect lighting is rendered. Higher values allow the light to be rendered in SDFGI further away from the camera.

---

<span id="class_RenderingServer_method_light_set_negative"></span>

void **light_set_negative** ( light: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_negative)

If `true`, the 3D light will subtract light instead of adding light. Equivalent to [Light3D.light_negative](class_light3d.md#class_Light3D_property_light_negative).

---

<span id="class_RenderingServer_method_light_set_param"></span>

void **light_set_param** ( light: [RID](class_rid.md#class_RID), param: [LightParam](class_renderingserver.md#enum_RenderingServer_LightParam), value: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_param)

Sets the specified 3D light parameter. Equivalent to [Light3D.set_param()](class_light3d.md#class_Light3D_method_set_param).

---

<span id="class_RenderingServer_method_light_set_projector"></span>

void **light_set_projector** ( light: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_projector)

Sets the projector texture to use for the specified 3D light. Equivalent to [Light3D.light_projector](class_light3d.md#class_Light3D_property_light_projector).

---

<span id="class_RenderingServer_method_light_set_reverse_cull_face_mode"></span>

void **light_set_reverse_cull_face_mode** ( light: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_reverse_cull_face_mode)

If `true`, reverses the backface culling of the mesh. This can be useful when you have a flat mesh that has a light behind it. If you need to cast a shadow on both sides of the mesh, set the mesh to use double-sided shadows with [instance_geometry_set_cast_shadows_setting()](class_renderingserver.md#class_RenderingServer_method_instance_geometry_set_cast_shadows_setting). Equivalent to [Light3D.shadow_reverse_cull_face](class_light3d.md#class_Light3D_property_shadow_reverse_cull_face).

---

<span id="class_RenderingServer_method_light_set_shadow"></span>

void **light_set_shadow** ( light: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_shadow)

If `true`, light will cast shadows. Equivalent to [Light3D.shadow_enabled](class_light3d.md#class_Light3D_property_shadow_enabled).

---

<span id="class_RenderingServer_method_light_set_shadow_caster_mask"></span>

void **light_set_shadow_caster_mask** ( light: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_light_set_shadow_caster_mask)

Sets the shadow caster mask for this 3D light. Shadows will only be cast using objects in the selected layers. Equivalent to [Light3D.shadow_caster_mask](class_light3d.md#class_Light3D_property_shadow_caster_mask).

---

<span id="class_RenderingServer_method_lightmap_create"></span>

[RID](class_rid.md#class_RID) **lightmap_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_create)

Creates a new lightmap global illumination instance and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `lightmap_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent node is [LightmapGI](class_lightmapgi.md#class_LightmapGI).

---

<span id="class_RenderingServer_method_lightmap_get_probe_capture_bsp_tree"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **lightmap_get_probe_capture_bsp_tree** ( lightmap: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_bsp_tree)

Returns the BSP tree data used for accelerating probe lookups. The BSP data is structured as a series of six signed 32-bit values per BSP node in this order: `float plane_x`, `float plane_y`, `float plane_z`, `float plane_distance`, `int32_t over`, `int32_t under`. An empty leaf is denoted by the value `-2147483648` (the minimum 32-bit signed integer). See also [lightmap_set_probe_capture_data()](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_capture_data).

---

<span id="class_RenderingServer_method_lightmap_get_probe_capture_points"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **lightmap_get_probe_capture_points** ( lightmap: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_points)

Returns the *local space* positions of each lightmap probe capture point. Keep in mind the lightmap instance may have a non-zero transform, which will affect the position of the probe capture points. See also [lightmap_set_probe_capture_data()](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_capture_data).

---

<span id="class_RenderingServer_method_lightmap_get_probe_capture_sh"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **lightmap_get_probe_capture_sh** ( lightmap: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_sh)

Returns the L0, L1, and L2 spherical harmonics data for each lightmap probe capture point. This is specified as 9 [Color](class_color.md#class_Color) values per probe, which means the size of the returned data is always 9 times the number of probe points. See also [lightmap_set_probe_capture_data()](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_capture_data).

---

<span id="class_RenderingServer_method_lightmap_get_probe_capture_tetrahedra"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **lightmap_get_probe_capture_tetrahedra** ( lightmap: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_tetrahedra)

Returns the tetrahedralization data used for interpolating between lightmap probe capture points. Each tetrahedron is specified as a series of 4 numbers, each being an index into the probe capture points array returned by [lightmap_get_probe_capture_points()](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_points). See also [lightmap_set_probe_capture_data()](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_capture_data).

---

<span id="class_RenderingServer_method_lightmap_set_baked_exposure_normalization"></span>

void **lightmap_set_baked_exposure_normalization** ( lightmap: [RID](class_rid.md#class_RID), baked_exposure: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_set_baked_exposure_normalization)

Used to inform the renderer what exposure normalization value was used while baking the lightmap. This value will be used and modulated at run time to ensure that the lightmap maintains a consistent level of exposure even if the scene-wide exposure normalization is changed at run time. For more information see [camera_attributes_set_exposure()](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_exposure).

---

<span id="class_RenderingServer_method_lightmap_set_probe_bounds"></span>

void **lightmap_set_probe_bounds** ( lightmap: [RID](class_rid.md#class_RID), bounds: [AABB](class_aabb.md#class_AABB) ) [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_bounds)

Sets the bounds that this lightmap instance should visually affect, both in terms of static lightmap baking and probe-based global illumination.

---

<span id="class_RenderingServer_method_lightmap_set_probe_capture_data"></span>

void **lightmap_set_probe_capture_data** ( lightmap: [RID](class_rid.md#class_RID), points: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), point_sh: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray), tetrahedra: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array), bsp_tree: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_capture_data)

Sets the probe capture data for the given lightmap instance. See [lightmap_get_probe_capture_points()](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_points), [lightmap_get_probe_capture_sh()](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_sh), [lightmap_get_probe_capture_tetrahedra()](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_tetrahedra), and [lightmap_get_probe_capture_bsp_tree()](class_renderingserver.md#class_RenderingServer_method_lightmap_get_probe_capture_bsp_tree) for the expected data formats.

---

<span id="class_RenderingServer_method_lightmap_set_probe_capture_update_speed"></span>

void **lightmap_set_probe_capture_update_speed** ( speed: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_capture_update_speed)

The framerate-independent update speed when representing dynamic object lighting from [LightmapProbe](class_lightmapprobe.md#class_LightmapProbe) s. Higher values make dynamic object lighting update faster. Higher values can prevent fast-moving objects from having "outdated" indirect lighting displayed on them, at the cost of possible flickering when an object moves from a bright area to a shaded area. See also ProjectSettings.rendering/lightmapping/probe_capture/update_speed.

---

<span id="class_RenderingServer_method_lightmap_set_probe_interior"></span>

void **lightmap_set_probe_interior** ( lightmap: [RID](class_rid.md#class_RID), interior: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_set_probe_interior)

Sets whether the lightmap instance should be considered as interior (when `interior` is `true`). If the lightmap is marked as interior, environment lighting is ignored when baking lightmaps.

---

<span id="class_RenderingServer_method_lightmap_set_textures"></span>

void **lightmap_set_textures** ( lightmap: [RID](class_rid.md#class_RID), light: [RID](class_rid.md#class_RID), uses_sh: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_lightmap_set_textures)

Set the textures on the given `lightmap` GI instance to the texture array pointed to by the `light` RID. If the lightmap texture was baked with [LightmapGI.directional](class_lightmapgi.md#class_LightmapGI_property_directional) set to `true`, then `uses_sh` must also be `true`.

---

<span id="class_RenderingServer_method_lightmaps_set_bicubic_filter"></span>

void **lightmaps_set_bicubic_filter** ( enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_lightmaps_set_bicubic_filter)

Toggles whether a bicubic filter should be used when lightmaps are sampled. This smoothens their appearance at a performance cost.

---

<span id="class_RenderingServer_method_make_sphere_mesh"></span>

[RID](class_rid.md#class_RID) **make_sphere_mesh** ( latitudes: [int](class_int.md#class_int), longitudes: [int](class_int.md#class_int), radius: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_make_sphere_mesh)

Returns a mesh of a sphere with the given number of horizontal subdivisions, vertical subdivisions and radius. See also [get_test_cube()](class_renderingserver.md#class_RenderingServer_method_get_test_cube).

---

<span id="class_RenderingServer_method_material_create"></span>

[RID](class_rid.md#class_RID) **material_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_material_create)

Creates an empty material and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `material_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [Material](class_material.md#class_Material).

---

<span id="class_RenderingServer_method_material_get_param"></span>

[Variant](class_variant.md#class_Variant) **material_get_param** ( material: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_material_get_param)

Returns the value of a certain material's parameter.

---

<span id="class_RenderingServer_method_material_set_next_pass"></span>

void **material_set_next_pass** ( material: [RID](class_rid.md#class_RID), next_material: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_material_set_next_pass)

Sets an object's next material.

---

<span id="class_RenderingServer_method_material_set_param"></span>

void **material_set_param** ( material: [RID](class_rid.md#class_RID), parameter: [StringName](class_stringname.md#class_StringName), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_renderingserver.md#class_RenderingServer_method_material_set_param)

Sets a material's parameter.

---

<span id="class_RenderingServer_method_material_set_render_priority"></span>

void **material_set_render_priority** ( material: [RID](class_rid.md#class_RID), priority: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_material_set_render_priority)

Sets a material's render priority.

---

<span id="class_RenderingServer_method_material_set_shader"></span>

void **material_set_shader** ( shader_material: [RID](class_rid.md#class_RID), shader: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_material_set_shader)

Sets a shader material's shader.

---

<span id="class_RenderingServer_method_material_set_use_debanding"></span>

void **material_set_use_debanding** ( enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_material_set_use_debanding)

When using the Mobile renderer, [material_set_use_debanding()](class_renderingserver.md#class_RenderingServer_method_material_set_use_debanding) can be used to enable or disable the debanding feature of 3D materials ([BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D) and [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial)).

 [material_set_use_debanding()](class_renderingserver.md#class_RenderingServer_method_material_set_use_debanding) has no effect when using the Compatibility or Forward+ renderer. In Forward+, [Viewport](class_viewport.md#class_Viewport) debanding can be used instead.

See also ProjectSettings.rendering/anti_aliasing/quality/use_debanding and [viewport_set_use_debanding()](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_debanding).

---

<span id="class_RenderingServer_method_mesh_add_surface"></span>

void **mesh_add_surface** ( mesh: [RID](class_rid.md#class_RID), surface: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_add_surface)

Creates a new surface on the given `mesh`. Equivalent to [mesh_add_surface_from_arrays()](class_renderingserver.md#class_RenderingServer_method_mesh_add_surface_from_arrays), but takes a single [Dictionary](class_dictionary.md#class_Dictionary) argument instead of separate arguments. The dictionary must follow this structure:

::

    {
        # Required:
        "primitive": RenderingServer.PrimitiveType,
        "format": RenderingServer.ArrayFormat,
        "vertex_data": PackedByteArray,
        "vertex_count": int,
        "aabb": AABB,

        # Optional:
        "attribute_data": PackedByteArray,
        "skin_data": PackedByteArray,
        "index_data": PackedByteArray,
        "index_count": int, # Required if `index_data` is specified.
        "uv_scale": Vector4,
        "lods": [
            # Both values are required for each LOD level.
            {
                "edge_length": float,
                "index_data": PackedByteArray,
            },
        ],
        "bone_aabbs": Array[AABB],
        "blend_shape_data": PackedByteArray,
        "material": Material,
    }

See also [mesh_get_surface()](class_renderingserver.md#class_RenderingServer_method_mesh_get_surface), which returns data in the same structure defined above.

---

<span id="class_RenderingServer_method_mesh_add_surface_from_arrays"></span>

void **mesh_add_surface_from_arrays** ( mesh: [RID](class_rid.md#class_RID), primitive: [PrimitiveType](class_renderingserver.md#enum_RenderingServer_PrimitiveType), arrays: [Array](class_array.md#class_Array), blend_shapes: [Array](class_array.md#class_Array) = [], lods: [Dictionary](class_dictionary.md#class_Dictionary) = {}, compress_format: *BitField*\[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\] = 0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_add_surface_from_arrays)

Creates a new surface on the given `mesh`. [mesh_get_surface_count()](class_renderingserver.md#class_RenderingServer_method_mesh_get_surface_count) will become the surface index for this new surface.

Surfaces are created to be rendered using a `primitive`, which may be any of the values defined in [PrimitiveType](class_mesh.md#enum_Mesh_PrimitiveType).

The `arrays` argument is an array of arrays. Each of the [Mesh.ARRAY_MAX](class_mesh.md#class_Mesh_constant_ARRAY_MAX) elements contains an array with some of the mesh data for this surface as described by the corresponding member of [ArrayType](class_mesh.md#enum_Mesh_ArrayType) or `null` if it is not used by the surface. For example, `arrays[0]` is the array of vertices. That first vertex sub-array is always required; the others are optional. Adding an index array puts this surface into "index mode" where the vertex and other arrays become the sources of data and the index array defines the vertex order. All sub-arrays must have the same length as the vertex array (or be an exact multiple of the vertex array's length, when multiple elements of a sub-array correspond to a single vertex) or be empty, except for [Mesh.ARRAY_INDEX](class_mesh.md#class_Mesh_constant_ARRAY_INDEX) if it is used.

The `blend_shapes` argument is an array of vertex data for each blend shape. Each element is an array of the same structure as `arrays`, but [Mesh.ARRAY_VERTEX](class_mesh.md#class_Mesh_constant_ARRAY_VERTEX), [Mesh.ARRAY_NORMAL](class_mesh.md#class_Mesh_constant_ARRAY_NORMAL), and [Mesh.ARRAY_TANGENT](class_mesh.md#class_Mesh_constant_ARRAY_TANGENT) are set if and only if they are set in `arrays` and all other entries are `null`.

The `lods` argument is a dictionary with [float](class_float.md#class_float) keys and [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) values. Each entry in the dictionary represents an LOD level of the surface, where the value is the [Mesh.ARRAY_INDEX](class_mesh.md#class_Mesh_constant_ARRAY_INDEX) array to use for the LOD level and the key is roughly proportional to the distance at which the LOD stats being used. I.e., increasing the key of an LOD also increases the distance that the objects has to be from the camera before the LOD is used.

The `compress_format` argument is the bitwise OR of, as required: One value of [ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat) left shifted by `ARRAY_FORMAT_CUSTOMn_SHIFT` for each custom channel in use, [ARRAY_FLAG_USE_DYNAMIC_UPDATE](class_renderingserver.md#class_RenderingServer_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE), [ARRAY_FLAG_USE_8_BONE_WEIGHTS](class_renderingserver.md#class_RenderingServer_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS), or [ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY](class_renderingserver.md#class_RenderingServer_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY).

See [ArrayMesh.add_surface_from_arrays()](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays) and [ImporterMesh.add_surface()](class_importermesh.md#class_ImporterMesh_method_add_surface) for higher-level equivalents of this method.

 **Note:** When using indices, it is recommended to only use points, lines, or triangles.

---

<span id="class_RenderingServer_method_mesh_clear"></span>

void **mesh_clear** ( mesh: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_clear)

Removes all surfaces from a mesh.

---

<span id="class_RenderingServer_method_mesh_create"></span>

[RID](class_rid.md#class_RID) **mesh_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_create)

Creates a new mesh and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `mesh_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach this mesh to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

 **Note:** The equivalent resource is [Mesh](class_mesh.md#class_Mesh).

---

<span id="class_RenderingServer_method_mesh_create_from_surfaces"></span>

[RID](class_rid.md#class_RID) **mesh_create_from_surfaces** ( surfaces: [Array](class_array.md#class_Array)\[[Dictionary](class_dictionary.md#class_Dictionary)\], blend_shape_count: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_create_from_surfaces)

Creates a new mesh with predefined surfaces for it and adds the mesh to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `mesh_*` RenderingServer functions. This method is more efficient for creating meshes with multiple surfaces compared to creating an empty mesh with [mesh_create()](class_renderingserver.md#class_RenderingServer_method_mesh_create) and adding surfaces one by one with [mesh_add_surface()](class_renderingserver.md#class_RenderingServer_method_mesh_add_surface).

Each element in the `surfaces` array must follow the same structure as described in [mesh_add_surface()](class_renderingserver.md#class_RenderingServer_method_mesh_add_surface). The `blend_shape_count` parameter must match the blend shape data defined in all surfaces.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach this mesh to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

 **Note:** The equivalent resource is [Mesh](class_mesh.md#class_Mesh).

---

<span id="class_RenderingServer_method_mesh_get_blend_shape_count"></span>

[int](class_int.md#class_int) **mesh_get_blend_shape_count** ( mesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_get_blend_shape_count)

Returns a mesh's blend shape count.

---

<span id="class_RenderingServer_method_mesh_get_blend_shape_mode"></span>

[BlendShapeMode](class_renderingserver.md#enum_RenderingServer_BlendShapeMode) **mesh_get_blend_shape_mode** ( mesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_get_blend_shape_mode)

Returns a mesh's blend shape mode.

---

<span id="class_RenderingServer_method_mesh_get_custom_aabb"></span>

[AABB](class_aabb.md#class_AABB) **mesh_get_custom_aabb** ( mesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_get_custom_aabb)

Returns a mesh's custom aabb.

---

<span id="class_RenderingServer_method_mesh_get_surface"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **mesh_get_surface** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_get_surface)

Returns a mesh's surface as a dictionary following the same structure as described in [mesh_add_surface()](class_renderingserver.md#class_RenderingServer_method_mesh_add_surface).

---

<span id="class_RenderingServer_method_mesh_get_surface_count"></span>

[int](class_int.md#class_int) **mesh_get_surface_count** ( mesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_get_surface_count)

Returns a mesh's number of surfaces.

---

<span id="class_RenderingServer_method_mesh_set_blend_shape_mode"></span>

void **mesh_set_blend_shape_mode** ( mesh: [RID](class_rid.md#class_RID), mode: [BlendShapeMode](class_renderingserver.md#enum_RenderingServer_BlendShapeMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_set_blend_shape_mode)

Sets a mesh's blend shape mode.

---

<span id="class_RenderingServer_method_mesh_set_custom_aabb"></span>

void **mesh_set_custom_aabb** ( mesh: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_set_custom_aabb)

Sets a mesh's custom aabb.

---

<span id="class_RenderingServer_method_mesh_set_shadow_mesh"></span>

void **mesh_set_shadow_mesh** ( mesh: [RID](class_rid.md#class_RID), shadow_mesh: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_set_shadow_mesh)

Sets an optional second mesh which can be used for rendering shadows and the depth prepass. Can be used to increase performance by supplying a mesh with fused vertices and only vertex position data (without normals, UVs, colors, etc.).

 **Note:** This mesh must have exactly the same vertex positions as the source mesh (including the source mesh's LODs, if present). If vertex positions differ, then the mesh will not draw correctly.

---

<span id="class_RenderingServer_method_mesh_surface_get_arrays"></span>

[Array](class_array.md#class_Array) **mesh_surface_get_arrays** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_arrays)

Returns a mesh's surface's buffer arrays.

---

<span id="class_RenderingServer_method_mesh_surface_get_blend_shape_arrays"></span>

[Array](class_array.md#class_Array)\[[Array](class_array.md#class_Array)\] **mesh_surface_get_blend_shape_arrays** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_blend_shape_arrays)

Returns a mesh's surface's arrays for blend shapes.

---

<span id="class_RenderingServer_method_mesh_surface_get_format_attribute_stride"></span>

[int](class_int.md#class_int) **mesh_surface_get_format_attribute_stride** ( format: *BitField*\[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_attribute_stride)

Returns the stride of the attribute buffer for a mesh with given `format`.

---

<span id="class_RenderingServer_method_mesh_surface_get_format_index_stride"></span>

[int](class_int.md#class_int) **mesh_surface_get_format_index_stride** ( format: *BitField*\[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_index_stride)

Returns the stride of the index buffer for a mesh with the given `format`.

---

<span id="class_RenderingServer_method_mesh_surface_get_format_normal_tangent_stride"></span>

[int](class_int.md#class_int) **mesh_surface_get_format_normal_tangent_stride** ( format: *BitField*\[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_normal_tangent_stride)

Returns the stride of the combined normals and tangents for a mesh with given `format`. Note importantly that, while normals and tangents are in the vertex buffer with vertices, they are only interleaved with each other and so have a different stride than vertex positions.

---

<span id="class_RenderingServer_method_mesh_surface_get_format_offset"></span>

[int](class_int.md#class_int) **mesh_surface_get_format_offset** ( format: *BitField*\[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int), array_index: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_offset)

Returns the offset of a given attribute by `array_index` in the start of its respective buffer.

---

<span id="class_RenderingServer_method_mesh_surface_get_format_skin_stride"></span>

[int](class_int.md#class_int) **mesh_surface_get_format_skin_stride** ( format: *BitField*\[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_skin_stride)

Returns the stride of the skin buffer for a mesh with given `format`.

---

<span id="class_RenderingServer_method_mesh_surface_get_format_vertex_stride"></span>

[int](class_int.md#class_int) **mesh_surface_get_format_vertex_stride** ( format: *BitField*\[[ArrayFormat](class_renderingserver.md#enum_RenderingServer_ArrayFormat)\], vertex_count: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_vertex_stride)

Returns the stride of the vertex positions for a mesh with given `format`. Note importantly that vertex positions are stored consecutively and are not interleaved with the other attributes in the vertex buffer (normals and tangents).

---

<span id="class_RenderingServer_method_mesh_surface_get_material"></span>

[RID](class_rid.md#class_RID) **mesh_surface_get_material** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_material)

Returns a mesh's surface's material.

---

<span id="class_RenderingServer_method_mesh_surface_remove"></span>

void **mesh_surface_remove** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_remove)

Removes the surface at the given index from the Mesh, shifting surfaces with higher index down by one.

---

<span id="class_RenderingServer_method_mesh_surface_set_material"></span>

void **mesh_surface_set_material** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), material: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_set_material)

Sets a mesh's surface's material.

---

<span id="class_RenderingServer_method_mesh_surface_update_attribute_region"></span>

void **mesh_surface_update_attribute_region** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_update_attribute_region)

Updates the attribute buffer of the mesh surface with the given `data`. The expected data per attribute is 8 or 12 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class_Vector2), and 3 floats per [Vector3](class_vector3.md#class_Vector3)) depending on if the mesh is using [Vector2](class_vector2.md#class_Vector2) or [Vector3](class_vector3.md#class_Vector3) vertices. This value can be determined with [mesh_surface_get_format_attribute_stride()](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_attribute_stride) instead.

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each attribute.

A [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) of attribute locations can be converted into a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class_PackedVector3Array_method_to_byte_array) for use in `data`.

---

<span id="class_RenderingServer_method_mesh_surface_update_index_region"></span>

void **mesh_surface_update_index_region** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_update_index_region)

Updates the index buffer of the mesh surface with the given `data`. The expected data are 16 or 32-bit unsigned integers, which can be determined with [mesh_surface_get_format_index_stride()](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_index_stride).

---

<span id="class_RenderingServer_method_mesh_surface_update_skin_region"></span>

void **mesh_surface_update_skin_region** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_update_skin_region)

Updates the skin buffer of the mesh surface with the given `data`. The expected data per skin is 8 or 12 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class_Vector2), and 3 floats per [Vector3](class_vector3.md#class_Vector3)) depending on if the mesh is using [Vector2](class_vector2.md#class_Vector2) or [Vector3](class_vector3.md#class_Vector3) vertices. This value can be determined with [mesh_surface_get_format_skin_stride()](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_skin_stride) instead.

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each skin.

A [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) of skin locations can be converted into a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class_PackedVector3Array_method_to_byte_array) for use in `data`.

---

<span id="class_RenderingServer_method_mesh_surface_update_vertex_region"></span>

void **mesh_surface_update_vertex_region** ( mesh: [RID](class_rid.md#class_RID), surface: [int](class_int.md#class_int), offset: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_renderingserver.md#class_RenderingServer_method_mesh_surface_update_vertex_region)

Updates the vertex buffer of the mesh surface with the given `data`. The expected data per vertex is 8 or 12 bytes (4 bytes per float, 2 floats per [Vector2](class_vector2.md#class_Vector2), and 3 floats per [Vector3](class_vector3.md#class_Vector3)) depending on if the mesh is using [Vector2](class_vector2.md#class_Vector2) or [Vector3](class_vector3.md#class_Vector3) vertices. This value can be determined with [mesh_surface_get_format_vertex_stride()](class_renderingserver.md#class_RenderingServer_method_mesh_surface_get_format_vertex_stride) instead.

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each vertex.

A [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) of vertex locations can be converted into a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) using [PackedVector3Array.to_byte_array()](class_packedvector3array.md#class_PackedVector3Array_method_to_byte_array) for use in `data`.

---

<span id="class_RenderingServer_method_multimesh_allocate_data"></span>

void **multimesh_allocate_data** ( multimesh: [RID](class_rid.md#class_RID), instances: [int](class_int.md#class_int), transform_format: [MultimeshTransformFormat](class_renderingserver.md#enum_RenderingServer_MultimeshTransformFormat), color_format: [bool](class_bool.md#class_bool) = false, custom_data_format: [bool](class_bool.md#class_bool) = false, use_indirect: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_allocate_data)

Sets up the multimesh using the specified data. The number of instances is set by `instances`. The format of the instance transforms is set by `transform_format`, which should be set according to whether the multimesh is meant to be rendered in 2D or 3D. If `color_format` is `true`, each instance will have a color associated with it. If `custom_data_format` is `true`, each instance will have a custom data vector associated with it. If `use_indirect` is `true`, an indirect command buffer will be created for this multimesh, allowing the instance count to be modified directly on the GPU. See also [multimesh_get_command_buffer_rd_rid()](class_renderingserver.md#class_RenderingServer_method_multimesh_get_command_buffer_rd_rid).

---

<span id="class_RenderingServer_method_multimesh_create"></span>

[RID](class_rid.md#class_RID) **multimesh_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_create)

Creates a new multimesh on the RenderingServer and returns an [RID](class_rid.md#class_RID) handle. This RID will be used in all `multimesh_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach this multimesh to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

 **Note:** The equivalent resource is [MultiMesh](class_multimesh.md#class_MultiMesh).

---

<span id="class_RenderingServer_method_multimesh_get_aabb"></span>

[AABB](class_aabb.md#class_AABB) **multimesh_get_aabb** ( multimesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_get_aabb)

Calculates and returns the axis-aligned bounding box that encloses all instances within the multimesh.

---

<span id="class_RenderingServer_method_multimesh_get_buffer"></span>

[PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) **multimesh_get_buffer** ( multimesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_get_buffer)

Returns the MultiMesh data (such as instance transforms, colors, etc.). See [multimesh_set_buffer()](class_renderingserver.md#class_RenderingServer_method_multimesh_set_buffer) for details on the returned data.

 **Note:** If the buffer is in the engine's internal cache, it will have to be fetched from GPU memory and possibly decompressed. This means [multimesh_get_buffer()](class_renderingserver.md#class_RenderingServer_method_multimesh_get_buffer) is potentially a slow operation and should be avoided whenever possible.

---

<span id="class_RenderingServer_method_multimesh_get_buffer_rd_rid"></span>

[RID](class_rid.md#class_RID) **multimesh_get_buffer_rd_rid** ( multimesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_get_buffer_rd_rid)

Returns the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) [RID](class_rid.md#class_RID) handle of the [MultiMesh](class_multimesh.md#class_MultiMesh), which can be used as any other buffer on the Rendering Device.

---

<span id="class_RenderingServer_method_multimesh_get_command_buffer_rd_rid"></span>

[RID](class_rid.md#class_RID) **multimesh_get_command_buffer_rd_rid** ( multimesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_get_command_buffer_rd_rid)

Returns the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) [RID](class_rid.md#class_RID) handle of the [MultiMesh](class_multimesh.md#class_MultiMesh) command buffer. This [RID](class_rid.md#class_RID) is only valid if `use_indirect` is set to `true` when allocating data through [multimesh_allocate_data()](class_renderingserver.md#class_RenderingServer_method_multimesh_allocate_data). It can be used to directly modify the instance count via buffer.

The data structure is dependent on both how many surfaces the mesh contains and whether it is indexed or not, the buffer has 5 integers in it, with the last unused if the mesh is not indexed.

Each of the values in the buffer correspond to these options:

.. code:: text

    Indexed:
      0 - indexCount;
      1 - instanceCount;
      2 - firstIndex;
      3 - vertexOffset;
      4 - firstInstance;
    Non-indexed:
      0 - vertexCount;
      1 - instanceCount;
      2 - firstVertex;
      3 - firstInstance;
      4 - unused;

---

<span id="class_RenderingServer_method_multimesh_get_custom_aabb"></span>

[AABB](class_aabb.md#class_AABB) **multimesh_get_custom_aabb** ( multimesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_get_custom_aabb)

Returns the custom AABB defined for this MultiMesh resource.

---

<span id="class_RenderingServer_method_multimesh_get_instance_count"></span>

[int](class_int.md#class_int) **multimesh_get_instance_count** ( multimesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_get_instance_count)

Returns the number of instances allocated for this multimesh.

---

<span id="class_RenderingServer_method_multimesh_get_mesh"></span>

[RID](class_rid.md#class_RID) **multimesh_get_mesh** ( multimesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_get_mesh)

Returns the RID of the mesh that will be used in drawing this multimesh.

---

<span id="class_RenderingServer_method_multimesh_get_visible_instances"></span>

[int](class_int.md#class_int) **multimesh_get_visible_instances** ( multimesh: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_get_visible_instances)

Returns the number of visible instances for this multimesh.

---

<span id="class_RenderingServer_method_multimesh_instance_get_color"></span>

[Color](class_color.md#class_Color) **multimesh_instance_get_color** ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_get_color)

Returns the color by which the specified instance will be modulated.

---

<span id="class_RenderingServer_method_multimesh_instance_get_custom_data"></span>

[Color](class_color.md#class_Color) **multimesh_instance_get_custom_data** ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_get_custom_data)

Returns the custom data associated with the specified instance.

---

<span id="class_RenderingServer_method_multimesh_instance_get_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **multimesh_instance_get_transform** ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_get_transform)

Returns the [Transform3D](class_transform3d.md#class_Transform3D) of the specified instance.

---

<span id="class_RenderingServer_method_multimesh_instance_get_transform_2d"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **multimesh_instance_get_transform_2d** ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_get_transform_2d)

Returns the [Transform2D](class_transform2d.md#class_Transform2D) of the specified instance. For use when the multimesh is set to use 2D transforms.

---

<span id="class_RenderingServer_method_multimesh_instance_reset_physics_interpolation"></span>

void **multimesh_instance_reset_physics_interpolation** ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_reset_physics_interpolation)

Prevents physics interpolation for the specified instance during the current physics tick.

This is useful when moving an instance to a new location, to give an instantaneous change rather than interpolation from the previous location.

---

<span id="class_RenderingServer_method_multimesh_instance_set_color"></span>

void **multimesh_instance_set_color** ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_set_color)

Sets the color by which this instance will be modulated. Equivalent to [MultiMesh.set_instance_color()](class_multimesh.md#class_MultiMesh_method_set_instance_color).

---

<span id="class_RenderingServer_method_multimesh_instance_set_custom_data"></span>

void **multimesh_instance_set_custom_data** ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), custom_data: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_set_custom_data)

Sets the custom data for this instance. Custom data is passed as a [Color](class_color.md#class_Color), but is interpreted as a `vec4` in the shader. Equivalent to [MultiMesh.set_instance_custom_data()](class_multimesh.md#class_MultiMesh_method_set_instance_custom_data).

---

<span id="class_RenderingServer_method_multimesh_instance_set_transform"></span>

void **multimesh_instance_set_transform** ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_set_transform)

Sets the [Transform3D](class_transform3d.md#class_Transform3D) for this instance. Equivalent to [MultiMesh.set_instance_transform()](class_multimesh.md#class_MultiMesh_method_set_instance_transform).

---

<span id="class_RenderingServer_method_multimesh_instance_set_transform_2d"></span>

void **multimesh_instance_set_transform_2d** ( multimesh: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instance_set_transform_2d)

Sets the [Transform2D](class_transform2d.md#class_Transform2D) for this instance. For use when multimesh is used in 2D. Equivalent to [MultiMesh.set_instance_transform_2d()](class_multimesh.md#class_MultiMesh_method_set_instance_transform_2d).

---

<span id="class_RenderingServer_method_multimesh_instances_reset_physics_interpolation"></span>

void **multimesh_instances_reset_physics_interpolation** ( multimesh: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_instances_reset_physics_interpolation)

Prevents physics interpolation for all instances during the current physics tick.

This is useful when moving all instances to new locations, to give instantaneous changes rather than interpolation from the previous locations.

---

<span id="class_RenderingServer_method_multimesh_set_buffer"></span>

void **multimesh_set_buffer** ( multimesh: [RID](class_rid.md#class_RID), buffer: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_set_buffer)

Set the entire data to use for drawing the `multimesh` at once to `buffer` (such as instance transforms and colors). `buffer`'s size must match the number of instances multiplied by the per-instance data size (which depends on the enabled MultiMesh fields). Otherwise, an error message is printed and nothing is rendered. See also [multimesh_get_buffer()](class_renderingserver.md#class_RenderingServer_method_multimesh_get_buffer).

The per-instance data size and expected data order is:

.. code:: text

    2D:
      - Position: 8 floats (8 floats for Transform2D)
      - Position + Vertex color: 12 floats (8 floats for Transform2D, 4 floats for Color)
      - Position + Custom data: 12 floats (8 floats for Transform2D, 4 floats of custom data)
      - Position + Vertex color + Custom data: 16 floats (8 floats for Transform2D, 4 floats for Color, 4 floats of custom data)
    3D:
      - Position: 12 floats (12 floats for Transform3D)
      - Position + Vertex color: 16 floats (12 floats for Transform3D, 4 floats for Color)
      - Position + Custom data: 16 floats (12 floats for Transform3D, 4 floats of custom data)
      - Position + Vertex color + Custom data: 20 floats (12 floats for Transform3D, 4 floats for Color, 4 floats of custom data)

Instance transforms are in row-major order. Specifically:

- For [Transform2D](class_transform2d.md#class_Transform2D) the float-order is: `(x.x, y.x, padding_float, origin.x, x.y, y.y, padding_float, origin.y)`.

- For [Transform3D](class_transform3d.md#class_Transform3D) the float-order is: `(basis.x.x, basis.y.x, basis.z.x, origin.x, basis.x.y, basis.y.y, basis.z.y, origin.y, basis.x.z, basis.y.z, basis.z.z, origin.z)`.

---

<span id="class_RenderingServer_method_multimesh_set_buffer_interpolated"></span>

void **multimesh_set_buffer_interpolated** ( multimesh: [RID](class_rid.md#class_RID), buffer: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array), buffer_previous: [PackedFloat32Array](class_packedfloat32array.md#class_PackedFloat32Array) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_set_buffer_interpolated)

Alternative version of [multimesh_set_buffer()](class_renderingserver.md#class_RenderingServer_method_multimesh_set_buffer) for use with physics interpolation.

Takes both an array of current data and an array of data for the previous physics tick.

---

<span id="class_RenderingServer_method_multimesh_set_custom_aabb"></span>

void **multimesh_set_custom_aabb** ( multimesh: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_set_custom_aabb)

Sets the custom AABB for this MultiMesh resource.

---

<span id="class_RenderingServer_method_multimesh_set_mesh"></span>

void **multimesh_set_mesh** ( multimesh: [RID](class_rid.md#class_RID), mesh: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_set_mesh)

Sets the mesh to be drawn by the multimesh. Equivalent to [MultiMesh.mesh](class_multimesh.md#class_MultiMesh_property_mesh).

---

<span id="class_RenderingServer_method_multimesh_set_physics_interpolated"></span>

void **multimesh_set_physics_interpolated** ( multimesh: [RID](class_rid.md#class_RID), interpolated: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_set_physics_interpolated)

Turns on and off physics interpolation for this MultiMesh resource.

---

<span id="class_RenderingServer_method_multimesh_set_physics_interpolation_quality"></span>

void **multimesh_set_physics_interpolation_quality** ( multimesh: [RID](class_rid.md#class_RID), quality: [MultimeshPhysicsInterpolationQuality](class_renderingserver.md#enum_RenderingServer_MultimeshPhysicsInterpolationQuality) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_set_physics_interpolation_quality)

Sets the physics interpolation quality for the [MultiMesh](class_multimesh.md#class_MultiMesh).

A value of [MULTIMESH_INTERP_QUALITY_FAST](class_renderingserver.md#class_RenderingServer_constant_MULTIMESH_INTERP_QUALITY_FAST) gives fast but low quality interpolation, a value of [MULTIMESH_INTERP_QUALITY_HIGH](class_renderingserver.md#class_RenderingServer_constant_MULTIMESH_INTERP_QUALITY_HIGH) gives slower but higher quality interpolation.

---

<span id="class_RenderingServer_method_multimesh_set_visible_instances"></span>

void **multimesh_set_visible_instances** ( multimesh: [RID](class_rid.md#class_RID), visible: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_multimesh_set_visible_instances)

Sets the number of instances visible at a given time. If -1, all instances that have been allocated are drawn. Equivalent to [MultiMesh.visible_instance_count](class_multimesh.md#class_MultiMesh_property_visible_instance_count).

---

<span id="class_RenderingServer_method_occluder_create"></span>

[RID](class_rid.md#class_RID) **occluder_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_occluder_create)

Creates an occluder instance and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `occluder_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [Occluder3D](class_occluder3d.md#class_Occluder3D) (not to be confused with the [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D) node).

---

<span id="class_RenderingServer_method_occluder_set_mesh"></span>

void **occluder_set_mesh** ( occluder: [RID](class_rid.md#class_RID), vertices: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array), indices: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_renderingserver.md#class_RenderingServer_method_occluder_set_mesh)

Sets the mesh data for the given occluder RID, which controls the shape of the occlusion culling that will be performed.

---

<span id="class_RenderingServer_method_omni_light_create"></span>

[RID](class_rid.md#class_RID) **omni_light_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_omni_light_create)

Creates a new omni light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in most `light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach this omni light to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

 **Note:** The equivalent node is [OmniLight3D](class_omnilight3d.md#class_OmniLight3D).

---

<span id="class_RenderingServer_method_particles_collision_create"></span>

[RID](class_rid.md#class_RID) **particles_collision_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_create)

Creates a new 3D GPU particle collision or attractor and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in most `particles_collision_*` RenderingServer functions.

 **Note:** The equivalent nodes are [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D) and [GPUParticlesAttractor3D](class_gpuparticlesattractor3d.md#class_GPUParticlesAttractor3D).

---

<span id="class_RenderingServer_method_particles_collision_height_field_update"></span>

void **particles_collision_height_field_update** ( particles_collision: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_height_field_update)

Requests an update for the 3D GPU particle collision heightfield. This may be automatically called by the 3D GPU particle collision heightfield depending on its [GPUParticlesCollisionHeightField3D.update_mode](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_update_mode).

---

<span id="class_RenderingServer_method_particles_collision_set_attractor_attenuation"></span>

void **particles_collision_set_attractor_attenuation** ( particles_collision: [RID](class_rid.md#class_RID), curve: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_attractor_attenuation)

Sets the attenuation `curve` for the 3D GPU particles attractor specified by the `particles_collision` RID. Only used for attractors, not colliders. Equivalent to [GPUParticlesAttractor3D.attenuation](class_gpuparticlesattractor3d.md#class_GPUParticlesAttractor3D_property_attenuation).

---

<span id="class_RenderingServer_method_particles_collision_set_attractor_directionality"></span>

void **particles_collision_set_attractor_directionality** ( particles_collision: [RID](class_rid.md#class_RID), amount: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_attractor_directionality)

Sets the directionality `amount` for the 3D GPU particles attractor specified by the `particles_collision` RID. Only used for attractors, not colliders. Equivalent to [GPUParticlesAttractor3D.directionality](class_gpuparticlesattractor3d.md#class_GPUParticlesAttractor3D_property_directionality).

---

<span id="class_RenderingServer_method_particles_collision_set_attractor_strength"></span>

void **particles_collision_set_attractor_strength** ( particles_collision: [RID](class_rid.md#class_RID), strength: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_attractor_strength)

Sets the `strength` for the 3D GPU particles attractor specified by the `particles_collision` RID. Only used for attractors, not colliders. Equivalent to [GPUParticlesAttractor3D.strength](class_gpuparticlesattractor3d.md#class_GPUParticlesAttractor3D_property_strength).

---

<span id="class_RenderingServer_method_particles_collision_set_box_extents"></span>

void **particles_collision_set_box_extents** ( particles_collision: [RID](class_rid.md#class_RID), extents: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_box_extents)

Sets the `extents` for the 3D GPU particles collision by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionBox3D.size](class_gpuparticlescollisionbox3d.md#class_GPUParticlesCollisionBox3D_property_size), [GPUParticlesCollisionSDF3D.size](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_size), [GPUParticlesCollisionHeightField3D.size](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_size), [GPUParticlesAttractorBox3D.size](class_gpuparticlesattractorbox3d.md#class_GPUParticlesAttractorBox3D_property_size) or [GPUParticlesAttractorVectorField3D.size](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D_property_size) depending on the `particles_collision` type.

---

<span id="class_RenderingServer_method_particles_collision_set_collision_type"></span>

void **particles_collision_set_collision_type** ( particles_collision: [RID](class_rid.md#class_RID), type: [ParticlesCollisionType](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionType) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_collision_type)

Sets the collision or attractor shape `type` for the 3D GPU particles collision or attractor specified by the `particles_collision` RID.

---

<span id="class_RenderingServer_method_particles_collision_set_cull_mask"></span>

void **particles_collision_set_cull_mask** ( particles_collision: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_cull_mask)

Sets the cull `mask` for the 3D GPU particles collision or attractor specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollision3D.cull_mask](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D_property_cull_mask) or [GPUParticlesAttractor3D.cull_mask](class_gpuparticlesattractor3d.md#class_GPUParticlesAttractor3D_property_cull_mask) depending on the `particles_collision` type.

---

<span id="class_RenderingServer_method_particles_collision_set_field_texture"></span>

void **particles_collision_set_field_texture** ( particles_collision: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_field_texture)

Sets the signed distance field `texture` for the 3D GPU particles collision specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionSDF3D.texture](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_texture) or [GPUParticlesAttractorVectorField3D.texture](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D_property_texture) depending on the `particles_collision` type.

---

<span id="class_RenderingServer_method_particles_collision_set_height_field_mask"></span>

void **particles_collision_set_height_field_mask** ( particles_collision: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_height_field_mask)

Sets the heightfield `mask` for the 3D GPU particles heightfield collision specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionHeightField3D.heightfield_mask](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask).

---

<span id="class_RenderingServer_method_particles_collision_set_height_field_resolution"></span>

void **particles_collision_set_height_field_resolution** ( particles_collision: [RID](class_rid.md#class_RID), resolution: [ParticlesCollisionHeightfieldResolution](class_renderingserver.md#enum_RenderingServer_ParticlesCollisionHeightfieldResolution) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_height_field_resolution)

Sets the heightmap `resolution` for the 3D GPU particles heightfield collision specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionHeightField3D.resolution](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_resolution).

---

<span id="class_RenderingServer_method_particles_collision_set_sphere_radius"></span>

void **particles_collision_set_sphere_radius** ( particles_collision: [RID](class_rid.md#class_RID), radius: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_collision_set_sphere_radius)

Sets the `radius` for the 3D GPU particles sphere collision or attractor specified by the `particles_collision` RID. Equivalent to [GPUParticlesCollisionSphere3D.radius](class_gpuparticlescollisionsphere3d.md#class_GPUParticlesCollisionSphere3D_property_radius) or [GPUParticlesAttractorSphere3D.radius](class_gpuparticlesattractorsphere3d.md#class_GPUParticlesAttractorSphere3D_property_radius) depending on the `particles_collision` type.

---

<span id="class_RenderingServer_method_particles_create"></span>

[RID](class_rid.md#class_RID) **particles_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_create)

Creates a GPU-based particle system and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `particles_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach these particles to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

 **Note:** The equivalent nodes are [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) and [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D).

 **Note:** All `particles_*` methods only apply to GPU-based particles, not CPU-based particles. [CPUParticles2D](class_cpuparticles2d.md#class_CPUParticles2D) and [CPUParticles3D](class_cpuparticles3d.md#class_CPUParticles3D) do not have equivalent RenderingServer functions available, as these use [MultiMeshInstance2D](class_multimeshinstance2d.md#class_MultiMeshInstance2D) and [MultiMeshInstance3D](class_multimeshinstance3d.md#class_MultiMeshInstance3D) under the hood (see `multimesh_*` methods).

---

<span id="class_RenderingServer_method_particles_emit"></span>

void **particles_emit** ( particles: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), velocity: [Vector3](class_vector3.md#class_Vector3), color: [Color](class_color.md#class_Color), custom: [Color](class_color.md#class_Color), emit_flags: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_emit)

Manually emits particles from the `particles` instance.

---

<span id="class_RenderingServer_method_particles_get_current_aabb"></span>

[AABB](class_aabb.md#class_AABB) **particles_get_current_aabb** ( particles: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_get_current_aabb)

Calculates and returns the axis-aligned bounding box that contains all the particles. Equivalent to [GPUParticles3D.capture_aabb()](class_gpuparticles3d.md#class_GPUParticles3D_method_capture_aabb).

---

<span id="class_RenderingServer_method_particles_get_emitting"></span>

[bool](class_bool.md#class_bool) **particles_get_emitting** ( particles: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_get_emitting)

Returns `true` if particles are currently set to emitting.

---

<span id="class_RenderingServer_method_particles_is_inactive"></span>

[bool](class_bool.md#class_bool) **particles_is_inactive** ( particles: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_is_inactive)

Returns `true` if particles are not emitting and particles are set to inactive.

---

<span id="class_RenderingServer_method_particles_request_process"></span>

void **particles_request_process** ( particles: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_request_process)

Add particle system to list of particle systems that need to be updated. Update will take place on the next frame, or on the next call to [instances_cull_aabb()](class_renderingserver.md#class_RenderingServer_method_instances_cull_aabb), [instances_cull_convex()](class_renderingserver.md#class_RenderingServer_method_instances_cull_convex), or [instances_cull_ray()](class_renderingserver.md#class_RenderingServer_method_instances_cull_ray).

---

<span id="class_RenderingServer_method_particles_request_process_time"></span>

void **particles_request_process_time** ( particles: [RID](class_rid.md#class_RID), time: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_request_process_time)

Requests particles to process for extra process time during a single frame.

---

<span id="class_RenderingServer_method_particles_restart"></span>

void **particles_restart** ( particles: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_restart)

Reset the particles on the next update. Equivalent to [GPUParticles3D.restart()](class_gpuparticles3d.md#class_GPUParticles3D_method_restart).

---

<span id="class_RenderingServer_method_particles_set_amount"></span>

void **particles_set_amount** ( particles: [RID](class_rid.md#class_RID), amount: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_amount)

Sets the number of particles to be drawn and allocates the memory for them. Equivalent to [GPUParticles3D.amount](class_gpuparticles3d.md#class_GPUParticles3D_property_amount).

---

<span id="class_RenderingServer_method_particles_set_amount_ratio"></span>

void **particles_set_amount_ratio** ( particles: [RID](class_rid.md#class_RID), ratio: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_amount_ratio)

Sets the amount ratio for particles to be emitted. Equivalent to [GPUParticles3D.amount_ratio](class_gpuparticles3d.md#class_GPUParticles3D_property_amount_ratio).

---

<span id="class_RenderingServer_method_particles_set_collision_base_size"></span>

void **particles_set_collision_base_size** ( particles: [RID](class_rid.md#class_RID), size: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_collision_base_size)

Sets the base size for particle collision. Equivalent to [GPUParticles3D.collision_base_size](class_gpuparticles3d.md#class_GPUParticles3D_property_collision_base_size).

---

<span id="class_RenderingServer_method_particles_set_custom_aabb"></span>

void **particles_set_custom_aabb** ( particles: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_custom_aabb)

Sets a custom axis-aligned bounding box for the particle system. Equivalent to [GPUParticles3D.visibility_aabb](class_gpuparticles3d.md#class_GPUParticles3D_property_visibility_aabb).

---

<span id="class_RenderingServer_method_particles_set_draw_order"></span>

void **particles_set_draw_order** ( particles: [RID](class_rid.md#class_RID), order: [ParticlesDrawOrder](class_renderingserver.md#enum_RenderingServer_ParticlesDrawOrder) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_draw_order)

Sets the draw order of the particles. Equivalent to [GPUParticles3D.draw_order](class_gpuparticles3d.md#class_GPUParticles3D_property_draw_order).

---

<span id="class_RenderingServer_method_particles_set_draw_pass_mesh"></span>

void **particles_set_draw_pass_mesh** ( particles: [RID](class_rid.md#class_RID), pass: [int](class_int.md#class_int), mesh: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_draw_pass_mesh)

Sets the mesh to be used for the specified draw pass. Equivalent to [GPUParticles3D.draw_pass_1](class_gpuparticles3d.md#class_GPUParticles3D_property_draw_pass_1), [GPUParticles3D.draw_pass_2](class_gpuparticles3d.md#class_GPUParticles3D_property_draw_pass_2), [GPUParticles3D.draw_pass_3](class_gpuparticles3d.md#class_GPUParticles3D_property_draw_pass_3), and [GPUParticles3D.draw_pass_4](class_gpuparticles3d.md#class_GPUParticles3D_property_draw_pass_4).

---

<span id="class_RenderingServer_method_particles_set_draw_passes"></span>

void **particles_set_draw_passes** ( particles: [RID](class_rid.md#class_RID), count: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_draw_passes)

Sets the number of draw passes to use. Equivalent to [GPUParticles3D.draw_passes](class_gpuparticles3d.md#class_GPUParticles3D_property_draw_passes).

---

<span id="class_RenderingServer_method_particles_set_emission_transform"></span>

void **particles_set_emission_transform** ( particles: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_emission_transform)

Sets the [Transform3D](class_transform3d.md#class_Transform3D) that will be used by the particles when they first emit.

---

<span id="class_RenderingServer_method_particles_set_emitter_velocity"></span>

void **particles_set_emitter_velocity** ( particles: [RID](class_rid.md#class_RID), velocity: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_emitter_velocity)

Sets the velocity of a particle node, that will be used by [ParticleProcessMaterial.inherit_velocity_ratio](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_inherit_velocity_ratio).

---

<span id="class_RenderingServer_method_particles_set_emitting"></span>

void **particles_set_emitting** ( particles: [RID](class_rid.md#class_RID), emitting: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_emitting)

If `true`, particles will emit over time. Setting to `false` does not reset the particles, but only stops their emission. Equivalent to [GPUParticles3D.emitting](class_gpuparticles3d.md#class_GPUParticles3D_property_emitting).

---

<span id="class_RenderingServer_method_particles_set_explosiveness_ratio"></span>

void **particles_set_explosiveness_ratio** ( particles: [RID](class_rid.md#class_RID), ratio: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_explosiveness_ratio)

Sets the explosiveness ratio. Equivalent to [GPUParticles3D.explosiveness](class_gpuparticles3d.md#class_GPUParticles3D_property_explosiveness).

---

<span id="class_RenderingServer_method_particles_set_fixed_fps"></span>

void **particles_set_fixed_fps** ( particles: [RID](class_rid.md#class_RID), fps: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_fixed_fps)

Sets the frame rate that the particle system rendering will be fixed to. Equivalent to [GPUParticles3D.fixed_fps](class_gpuparticles3d.md#class_GPUParticles3D_property_fixed_fps).

---

<span id="class_RenderingServer_method_particles_set_fractional_delta"></span>

void **particles_set_fractional_delta** ( particles: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_fractional_delta)

If `true`, uses fractional delta which smooths the movement of the particles. Equivalent to [GPUParticles3D.fract_delta](class_gpuparticles3d.md#class_GPUParticles3D_property_fract_delta).

---

<span id="class_RenderingServer_method_particles_set_interp_to_end"></span>

void **particles_set_interp_to_end** ( particles: [RID](class_rid.md#class_RID), factor: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_interp_to_end)

Sets the value that informs a [ParticleProcessMaterial](class_particleprocessmaterial.md#class_ParticleProcessMaterial) to rush all particles towards the end of their lifetime.

---

<span id="class_RenderingServer_method_particles_set_interpolate"></span>

void **particles_set_interpolate** ( particles: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_interpolate)

Sets whether particles should use interpolation between fixed steps. Equivalent to [GPUParticles3D.interpolate](class_gpuparticles3d.md#class_GPUParticles3D_property_interpolate).

---

<span id="class_RenderingServer_method_particles_set_lifetime"></span>

void **particles_set_lifetime** ( particles: [RID](class_rid.md#class_RID), lifetime: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_lifetime)

Sets the lifetime of each particle in the system. Equivalent to [GPUParticles3D.lifetime](class_gpuparticles3d.md#class_GPUParticles3D_property_lifetime).

---

<span id="class_RenderingServer_method_particles_set_mode"></span>

void **particles_set_mode** ( particles: [RID](class_rid.md#class_RID), mode: [ParticlesMode](class_renderingserver.md#enum_RenderingServer_ParticlesMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_mode)

Sets whether the GPU particles specified by the `particles` RID should be rendered in 2D or 3D according to `mode`.

---

<span id="class_RenderingServer_method_particles_set_one_shot"></span>

void **particles_set_one_shot** ( particles: [RID](class_rid.md#class_RID), one_shot: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_one_shot)

If `true`, particles will emit once and then stop. Equivalent to [GPUParticles3D.one_shot](class_gpuparticles3d.md#class_GPUParticles3D_property_one_shot).

---

<span id="class_RenderingServer_method_particles_set_pre_process_time"></span>

void **particles_set_pre_process_time** ( particles: [RID](class_rid.md#class_RID), time: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_pre_process_time)

Sets the preprocess time for the particles' animation. This lets you delay starting an animation until after the particles have begun emitting. Equivalent to [GPUParticles3D.preprocess](class_gpuparticles3d.md#class_GPUParticles3D_property_preprocess).

---

<span id="class_RenderingServer_method_particles_set_process_material"></span>

void **particles_set_process_material** ( particles: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_process_material)

Sets the material for processing the particles.

 **Note:** This is not the material used to draw the materials. Equivalent to [GPUParticles3D.process_material](class_gpuparticles3d.md#class_GPUParticles3D_property_process_material).

---

<span id="class_RenderingServer_method_particles_set_randomness_ratio"></span>

void **particles_set_randomness_ratio** ( particles: [RID](class_rid.md#class_RID), ratio: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_randomness_ratio)

Sets the emission randomness ratio. This randomizes the emission of particles within their phase. Equivalent to [GPUParticles3D.randomness](class_gpuparticles3d.md#class_GPUParticles3D_property_randomness).

---

<span id="class_RenderingServer_method_particles_set_speed_scale"></span>

void **particles_set_speed_scale** ( particles: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_speed_scale)

Sets the speed scale of the particle system. Equivalent to [GPUParticles3D.speed_scale](class_gpuparticles3d.md#class_GPUParticles3D_property_speed_scale).

---

<span id="class_RenderingServer_method_particles_set_subemitter"></span>

void **particles_set_subemitter** ( particles: [RID](class_rid.md#class_RID), subemitter_particles: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_subemitter)

Sets the subemitter particles for the particle system. Equivalent to [GPUParticles3D.sub_emitter](class_gpuparticles3d.md#class_GPUParticles3D_property_sub_emitter).

---

<span id="class_RenderingServer_method_particles_set_trail_bind_poses"></span>

void **particles_set_trail_bind_poses** ( particles: [RID](class_rid.md#class_RID), bind_poses: [Array](class_array.md#class_Array)\[[Transform3D](class_transform3d.md#class_Transform3D)\] ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_trail_bind_poses)

Sets the trail bind poses for the particle system. This specified as an array of [Transform3D](class_transform3d.md#class_Transform3D) s representing the bind pose for each draw pass. See [GPUParticles3D.draw_skin](class_gpuparticles3d.md#class_GPUParticles3D_property_draw_skin), [Skin.get_bind_count()](class_skin.md#class_Skin_method_get_bind_count), and [Skin.get_bind_pose()](class_skin.md#class_Skin_method_get_bind_pose). Set the value for each draw pass to [Transform3D.IDENTITY](class_transform3d.md#class_Transform3D_constant_IDENTITY) to use the default behavior, which is what built-in trails use ([RibbonTrailMesh](class_ribbontrailmesh.md#class_RibbonTrailMesh) and [TubeTrailMesh](class_tubetrailmesh.md#class_TubeTrailMesh)).

---

<span id="class_RenderingServer_method_particles_set_trails"></span>

void **particles_set_trails** ( particles: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool), length_sec: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_trails)

If `enable` is `true`, enables trails for the `particles` with the specified `length_sec` in seconds. Equivalent to [GPUParticles3D.trail_enabled](class_gpuparticles3d.md#class_GPUParticles3D_property_trail_enabled) and [GPUParticles3D.trail_lifetime](class_gpuparticles3d.md#class_GPUParticles3D_property_trail_lifetime).

---

<span id="class_RenderingServer_method_particles_set_transform_align"></span>

void **particles_set_transform_align** ( particles: [RID](class_rid.md#class_RID), align: [ParticlesTransformAlign](class_renderingserver.md#enum_RenderingServer_ParticlesTransformAlign) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_transform_align)

Sets the transform alignment for the particle system. Equivalent to [GPUParticles3D.transform_align](class_gpuparticles3d.md#class_GPUParticles3D_property_transform_align).

---

<span id="class_RenderingServer_method_particles_set_use_local_coordinates"></span>

void **particles_set_use_local_coordinates** ( particles: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_particles_set_use_local_coordinates)

If `true`, particles use local coordinates. If `false` they use global coordinates. Equivalent to [GPUParticles3D.local_coords](class_gpuparticles3d.md#class_GPUParticles3D_property_local_coords).

---

<span id="class_RenderingServer_method_positional_soft_shadow_filter_set_quality"></span>

void **positional_soft_shadow_filter_set_quality** ( quality: [ShadowQuality](class_renderingserver.md#enum_RenderingServer_ShadowQuality) ) [🔗](class_renderingserver.md#class_RenderingServer_method_positional_soft_shadow_filter_set_quality)

Sets the filter quality for omni and spot light shadows in 3D. See also ProjectSettings.rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality. This parameter is global and cannot be set on a per-viewport basis.

---

<span id="class_RenderingServer_method_reflection_probe_create"></span>

[RID](class_rid.md#class_RID) **reflection_probe_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_create)

Creates a reflection probe and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `reflection_probe_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach this reflection probe to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

 **Note:** The equivalent node is [ReflectionProbe](class_reflectionprobe.md#class_ReflectionProbe).

---

<span id="class_RenderingServer_method_reflection_probe_set_ambient_color"></span>

void **reflection_probe_set_ambient_color** ( probe: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_ambient_color)

Sets the reflection probe's custom ambient light color. Equivalent to [ReflectionProbe.ambient_color](class_reflectionprobe.md#class_ReflectionProbe_property_ambient_color).

---

<span id="class_RenderingServer_method_reflection_probe_set_ambient_energy"></span>

void **reflection_probe_set_ambient_energy** ( probe: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_ambient_energy)

Sets the reflection probe's custom ambient light energy. Equivalent to [ReflectionProbe.ambient_color_energy](class_reflectionprobe.md#class_ReflectionProbe_property_ambient_color_energy).

---

<span id="class_RenderingServer_method_reflection_probe_set_ambient_mode"></span>

void **reflection_probe_set_ambient_mode** ( probe: [RID](class_rid.md#class_RID), mode: [ReflectionProbeAmbientMode](class_renderingserver.md#enum_RenderingServer_ReflectionProbeAmbientMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_ambient_mode)

Sets the reflection probe's ambient light mode. Equivalent to [ReflectionProbe.ambient_mode](class_reflectionprobe.md#class_ReflectionProbe_property_ambient_mode).

---

<span id="class_RenderingServer_method_reflection_probe_set_as_interior"></span>

void **reflection_probe_set_as_interior** ( probe: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_as_interior)

If `true`, reflections will ignore sky contribution. Equivalent to [ReflectionProbe.interior](class_reflectionprobe.md#class_ReflectionProbe_property_interior).

---

<span id="class_RenderingServer_method_reflection_probe_set_blend_distance"></span>

void **reflection_probe_set_blend_distance** ( probe: [RID](class_rid.md#class_RID), blend_distance: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_blend_distance)

Sets the distance in meters over which a probe blends into the scene.

---

<span id="class_RenderingServer_method_reflection_probe_set_cull_mask"></span>

void **reflection_probe_set_cull_mask** ( probe: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_cull_mask)

Sets the render cull mask for this reflection probe. Only instances with a matching layer will be reflected by this probe. Equivalent to [ReflectionProbe.cull_mask](class_reflectionprobe.md#class_ReflectionProbe_property_cull_mask).

---

<span id="class_RenderingServer_method_reflection_probe_set_enable_box_projection"></span>

void **reflection_probe_set_enable_box_projection** ( probe: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_enable_box_projection)

If `true`, uses box projection. This can make reflections look more correct in certain situations. Equivalent to [ReflectionProbe.box_projection](class_reflectionprobe.md#class_ReflectionProbe_property_box_projection).

---

<span id="class_RenderingServer_method_reflection_probe_set_enable_shadows"></span>

void **reflection_probe_set_enable_shadows** ( probe: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_enable_shadows)

If `true`, computes shadows in the reflection probe. This makes the reflection much slower to compute. Equivalent to [ReflectionProbe.enable_shadows](class_reflectionprobe.md#class_ReflectionProbe_property_enable_shadows).

---

<span id="class_RenderingServer_method_reflection_probe_set_intensity"></span>

void **reflection_probe_set_intensity** ( probe: [RID](class_rid.md#class_RID), intensity: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_intensity)

Sets the intensity of the reflection probe. Intensity modulates the strength of the reflection. Equivalent to [ReflectionProbe.intensity](class_reflectionprobe.md#class_ReflectionProbe_property_intensity).

---

<span id="class_RenderingServer_method_reflection_probe_set_max_distance"></span>

void **reflection_probe_set_max_distance** ( probe: [RID](class_rid.md#class_RID), distance: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_max_distance)

Sets the max distance away from the probe an object can be before it is culled. Equivalent to [ReflectionProbe.max_distance](class_reflectionprobe.md#class_ReflectionProbe_property_max_distance).

---

<span id="class_RenderingServer_method_reflection_probe_set_mesh_lod_threshold"></span>

void **reflection_probe_set_mesh_lod_threshold** ( probe: [RID](class_rid.md#class_RID), pixels: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_mesh_lod_threshold)

Sets the mesh level of detail to use in the reflection probe rendering. Higher values will use less detailed versions of meshes that have LOD variations generated, which can improve performance. Equivalent to [ReflectionProbe.mesh_lod_threshold](class_reflectionprobe.md#class_ReflectionProbe_property_mesh_lod_threshold).

---

<span id="class_RenderingServer_method_reflection_probe_set_origin_offset"></span>

void **reflection_probe_set_origin_offset** ( probe: [RID](class_rid.md#class_RID), offset: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_origin_offset)

Sets the origin offset to be used when this reflection probe is in box project mode. Equivalent to [ReflectionProbe.origin_offset](class_reflectionprobe.md#class_ReflectionProbe_property_origin_offset).

---

<span id="class_RenderingServer_method_reflection_probe_set_reflection_mask"></span>

void **reflection_probe_set_reflection_mask** ( probe: [RID](class_rid.md#class_RID), layers: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_reflection_mask)

Sets the render reflection mask for this reflection probe. Only instances with a matching layer will have reflections applied from this probe. Equivalent to [ReflectionProbe.reflection_mask](class_reflectionprobe.md#class_ReflectionProbe_property_reflection_mask).

---

<span id="class_RenderingServer_method_reflection_probe_set_resolution"></span>

void **reflection_probe_set_resolution** ( probe: [RID](class_rid.md#class_RID), resolution: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_resolution)

**Deprecated:** This method has not done anything since Godot 3.

Deprecated. This method does nothing.

---

<span id="class_RenderingServer_method_reflection_probe_set_size"></span>

void **reflection_probe_set_size** ( probe: [RID](class_rid.md#class_RID), size: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_size)

Sets the size of the area that the reflection probe will capture. Equivalent to [ReflectionProbe.size](class_reflectionprobe.md#class_ReflectionProbe_property_size).

---

<span id="class_RenderingServer_method_reflection_probe_set_update_mode"></span>

void **reflection_probe_set_update_mode** ( probe: [RID](class_rid.md#class_RID), mode: [ReflectionProbeUpdateMode](class_renderingserver.md#enum_RenderingServer_ReflectionProbeUpdateMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_reflection_probe_set_update_mode)

Sets how often the reflection probe updates. Can either be once or every frame.

---

<span id="class_RenderingServer_method_request_frame_drawn_callback"></span>

void **request_frame_drawn_callback** ( callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_renderingserver.md#class_RenderingServer_method_request_frame_drawn_callback)

Schedules a callback to the given callable after a frame has been drawn.

---

<span id="class_RenderingServer_method_scenario_create"></span>

[RID](class_rid.md#class_RID) **scenario_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_scenario_create)

Creates a scenario and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `scenario_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

The scenario is the 3D world that all the visual instances exist in.

---

<span id="class_RenderingServer_method_scenario_set_camera_attributes"></span>

void **scenario_set_camera_attributes** ( scenario: [RID](class_rid.md#class_RID), effects: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_scenario_set_camera_attributes)

Sets the camera attributes (`effects`) that will be used with this scenario. See also [CameraAttributes](class_cameraattributes.md#class_CameraAttributes).

---

<span id="class_RenderingServer_method_scenario_set_compositor"></span>

void **scenario_set_compositor** ( scenario: [RID](class_rid.md#class_RID), compositor: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_scenario_set_compositor)

Sets the compositor (`compositor`) that will be used with this scenario. See also [Compositor](class_compositor.md#class_Compositor).

---

<span id="class_RenderingServer_method_scenario_set_environment"></span>

void **scenario_set_environment** ( scenario: [RID](class_rid.md#class_RID), environment: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_scenario_set_environment)

Sets the environment that will be used with this scenario. See also [Environment](class_environment.md#class_Environment).

---

<span id="class_RenderingServer_method_scenario_set_fallback_environment"></span>

void **scenario_set_fallback_environment** ( scenario: [RID](class_rid.md#class_RID), environment: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_scenario_set_fallback_environment)

Sets the fallback environment to be used by this scenario. The fallback environment is used if no environment is set. Internally, this is used by the editor to provide a default environment.

---

<span id="class_RenderingServer_method_screen_space_roughness_limiter_set_active"></span>

void **screen_space_roughness_limiter_set_active** ( enable: [bool](class_bool.md#class_bool), amount: [float](class_float.md#class_float), limit: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_screen_space_roughness_limiter_set_active)

Sets the screen-space roughness limiter parameters, such as whether it should be enabled and its thresholds. Equivalent to ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/enabled, ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/amount and ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/limit.

---

<span id="class_RenderingServer_method_set_boot_image"></span>

void **set_boot_image** ( image: [Image](class_image.md#class_Image), color: [Color](class_color.md#class_Color), scale: [bool](class_bool.md#class_bool), use_filter: [bool](class_bool.md#class_bool) = true ) [🔗](class_renderingserver.md#class_RenderingServer_method_set_boot_image)

**Deprecated:** Use [set_boot_image_with_stretch()](class_renderingserver.md#class_RenderingServer_method_set_boot_image_with_stretch) instead.

Sets a boot image. The `color` defines the background color. The value of `scale` indicates if the image will be scaled to fit the screen size. If `use_filter` is `true`, the image will be scaled with linear interpolation. If `use_filter` is `false`, the image will be scaled with nearest-neighbor interpolation.

---

<span id="class_RenderingServer_method_set_boot_image_with_stretch"></span>

void **set_boot_image_with_stretch** ( image: [Image](class_image.md#class_Image), color: [Color](class_color.md#class_Color), stretch_mode: [SplashStretchMode](class_renderingserver.md#enum_RenderingServer_SplashStretchMode), use_filter: [bool](class_bool.md#class_bool) = true ) [🔗](class_renderingserver.md#class_RenderingServer_method_set_boot_image_with_stretch)

Sets a boot image. The `color` defines the background color. The value of `stretch_mode` indicates how the image will be stretched (see [SplashStretchMode](class_renderingserver.md#enum_RenderingServer_SplashStretchMode) for possible values). If `use_filter` is `true`, the image will be scaled with linear interpolation. If `use_filter` is `false`, the image will be scaled with nearest-neighbor interpolation.

---

<span id="class_RenderingServer_method_set_debug_generate_wireframes"></span>

void **set_debug_generate_wireframes** ( generate: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_set_debug_generate_wireframes)

If `generate` is `true`, generates debug wireframes for all meshes that are loaded when using the Compatibility renderer. By default, the engine does not generate debug wireframes at runtime, since they slow down loading of assets and take up VRAM.

 **Note:** You must call this method before loading any meshes when using the Compatibility renderer, otherwise wireframes will not be used.

---

<span id="class_RenderingServer_method_set_default_clear_color"></span>

void **set_default_clear_color** ( color: [Color](class_color.md#class_Color) ) [🔗](class_renderingserver.md#class_RenderingServer_method_set_default_clear_color)

Sets the default clear color which is used when a specific clear color has not been selected. See also [get_default_clear_color()](class_renderingserver.md#class_RenderingServer_method_get_default_clear_color).

---

<span id="class_RenderingServer_method_shader_create"></span>

[RID](class_rid.md#class_RID) **shader_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_shader_create)

Creates an empty shader and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `shader_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [Shader](class_shader.md#class_Shader).

---

<span id="class_RenderingServer_method_shader_get_code"></span>

[String](class_string.md#class_String) **shader_get_code** ( shader: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_shader_get_code)

Returns a shader's source code as a string.

---

<span id="class_RenderingServer_method_shader_get_default_texture_parameter"></span>

[RID](class_rid.md#class_RID) **shader_get_default_texture_parameter** ( shader: [RID](class_rid.md#class_RID), name: [StringName](class_stringname.md#class_StringName), index: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_shader_get_default_texture_parameter)

Returns a default texture from a shader searched by name.

 **Note:** If the sampler array is used use `index` to access the specified texture.

---

<span id="class_RenderingServer_method_shader_get_parameter_default"></span>

[Variant](class_variant.md#class_Variant) **shader_get_parameter_default** ( shader: [RID](class_rid.md#class_RID), name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_shader_get_parameter_default)

Returns the default value for the specified shader uniform. This is usually the value written in the shader source code.

---

<span id="class_RenderingServer_method_shader_set_code"></span>

void **shader_set_code** ( shader: [RID](class_rid.md#class_RID), code: [String](class_string.md#class_String) ) [🔗](class_renderingserver.md#class_RenderingServer_method_shader_set_code)

Sets the shader's source code (which triggers recompilation after being changed).

---

<span id="class_RenderingServer_method_shader_set_default_texture_parameter"></span>

void **shader_set_default_texture_parameter** ( shader: [RID](class_rid.md#class_RID), name: [StringName](class_stringname.md#class_StringName), texture: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_shader_set_default_texture_parameter)

Sets a shader's default texture. Overwrites the texture given by name.

 **Note:** If the sampler array is used use `index` to access the specified texture.

---

<span id="class_RenderingServer_method_shader_set_path_hint"></span>

void **shader_set_path_hint** ( shader: [RID](class_rid.md#class_RID), path: [String](class_string.md#class_String) ) [🔗](class_renderingserver.md#class_RenderingServer_method_shader_set_path_hint)

Sets the path hint for the specified shader. This should generally match the [Shader](class_shader.md#class_Shader) resource's [Resource.resource_path](class_resource.md#class_Resource_property_resource_path).

---

<span id="class_RenderingServer_method_skeleton_allocate_data"></span>

void **skeleton_allocate_data** ( skeleton: [RID](class_rid.md#class_RID), bones: [int](class_int.md#class_int), is_2d_skeleton: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_skeleton_allocate_data)

Allocates data for this skeleton using the number of bones specified in `bones`. If `is_2d_skeleton` is `true`, the skeleton will be treated as a 2D skeleton instead of a 3D skeleton. See also [skeleton_get_bone_count()](class_renderingserver.md#class_RenderingServer_method_skeleton_get_bone_count).

---

<span id="class_RenderingServer_method_skeleton_bone_get_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **skeleton_bone_get_transform** ( skeleton: [RID](class_rid.md#class_RID), bone: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_skeleton_bone_get_transform)

Returns the [Transform3D](class_transform3d.md#class_Transform3D) set for a specific bone of this skeleton.

---

<span id="class_RenderingServer_method_skeleton_bone_get_transform_2d"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **skeleton_bone_get_transform_2d** ( skeleton: [RID](class_rid.md#class_RID), bone: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_skeleton_bone_get_transform_2d)

Returns the [Transform2D](class_transform2d.md#class_Transform2D) set for a specific bone of this skeleton.

---

<span id="class_RenderingServer_method_skeleton_bone_set_transform"></span>

void **skeleton_bone_set_transform** ( skeleton: [RID](class_rid.md#class_RID), bone: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_skeleton_bone_set_transform)

Sets the [Transform3D](class_transform3d.md#class_Transform3D) for a specific bone of this skeleton.

---

<span id="class_RenderingServer_method_skeleton_bone_set_transform_2d"></span>

void **skeleton_bone_set_transform_2d** ( skeleton: [RID](class_rid.md#class_RID), bone: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_skeleton_bone_set_transform_2d)

Sets the [Transform2D](class_transform2d.md#class_Transform2D) for a specific bone of this skeleton.

---

<span id="class_RenderingServer_method_skeleton_create"></span>

[RID](class_rid.md#class_RID) **skeleton_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_skeleton_create)

Creates a skeleton and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `skeleton_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

---

<span id="class_RenderingServer_method_skeleton_get_bone_count"></span>

[int](class_int.md#class_int) **skeleton_get_bone_count** ( skeleton: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_skeleton_get_bone_count)

Returns the number of bones allocated for this skeleton. See also [skeleton_allocate_data()](class_renderingserver.md#class_RenderingServer_method_skeleton_allocate_data).

---

<span id="class_RenderingServer_method_skeleton_set_base_transform_2d"></span>

void **skeleton_set_base_transform_2d** ( skeleton: [RID](class_rid.md#class_RID), base_transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_skeleton_set_base_transform_2d)

Sets the base [Transform2D](class_transform2d.md#class_Transform2D) to use for the specified skeleton.

---

<span id="class_RenderingServer_method_sky_bake_panorama"></span>

[Image](class_image.md#class_Image) **sky_bake_panorama** ( sky: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float), bake_irradiance: [bool](class_bool.md#class_bool), size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_renderingserver.md#class_RenderingServer_method_sky_bake_panorama)

Generates and returns an [Image](class_image.md#class_Image) containing the radiance map for the specified `sky` RID. This supports built-in sky material and custom sky shaders. If `bake_irradiance` is `true`, the irradiance map is saved instead of the radiance map. The radiance map is used to render reflected light, while the irradiance map is used to render ambient light. See also [environment_bake_panorama()](class_renderingserver.md#class_RenderingServer_method_environment_bake_panorama).

 **Note:** The image is saved using linear encoding without any tonemapping performed, which means it will look too dark if viewed directly in an image editor. `energy` values above `1.0` can be used to brighten the resulting image.

 **Note:** `size` should be a 2:1 aspect ratio for the generated panorama to have square pixels. For radiance maps, there is no point in using a height greater than [Sky.radiance_size](class_sky.md#class_Sky_property_radiance_size), as it won't increase detail. Irradiance maps only contain low-frequency data, so there is usually no point in going past a size of 128×64 pixels when saving an irradiance map.

---

<span id="class_RenderingServer_method_sky_create"></span>

[RID](class_rid.md#class_RID) **sky_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_sky_create)

Creates an empty sky and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `sky_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

---

<span id="class_RenderingServer_method_sky_set_material"></span>

void **sky_set_material** ( sky: [RID](class_rid.md#class_RID), material: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_sky_set_material)

Sets the material that the sky uses to render the background, ambient and reflection maps.

---

<span id="class_RenderingServer_method_sky_set_mode"></span>

void **sky_set_mode** ( sky: [RID](class_rid.md#class_RID), mode: [SkyMode](class_renderingserver.md#enum_RenderingServer_SkyMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_sky_set_mode)

Sets the process `mode` of the sky specified by the `sky` RID. Equivalent to [Sky.process_mode](class_sky.md#class_Sky_property_process_mode).

---

<span id="class_RenderingServer_method_sky_set_radiance_size"></span>

void **sky_set_radiance_size** ( sky: [RID](class_rid.md#class_RID), radiance_size: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_sky_set_radiance_size)

Sets the `radiance_size` of the sky specified by the `sky` RID (in pixels). Equivalent to [Sky.radiance_size](class_sky.md#class_Sky_property_radiance_size).

---

<span id="class_RenderingServer_method_spot_light_create"></span>

[RID](class_rid.md#class_RID) **spot_light_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_spot_light_create)

Creates a spot light and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID can be used in most `light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach this spot light to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

---

<span id="class_RenderingServer_method_sub_surface_scattering_set_quality"></span>

void **sub_surface_scattering_set_quality** ( quality: [SubSurfaceScatteringQuality](class_renderingserver.md#enum_RenderingServer_SubSurfaceScatteringQuality) ) [🔗](class_renderingserver.md#class_RenderingServer_method_sub_surface_scattering_set_quality)

Sets ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_quality to use when rendering materials that have subsurface scattering enabled.

---

<span id="class_RenderingServer_method_sub_surface_scattering_set_scale"></span>

void **sub_surface_scattering_set_scale** ( scale: [float](class_float.md#class_float), depth_scale: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_sub_surface_scattering_set_scale)

Sets the ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_scale and ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale to use when rendering materials that have subsurface scattering enabled.

---

<span id="class_RenderingServer_method_texture_2d_create"></span>

[RID](class_rid.md#class_RID) **texture_2d_create** ( image: [Image](class_image.md#class_Image) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_2d_create)

Creates a 2-dimensional texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_2d_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [Texture2D](class_texture2d.md#class_Texture2D).

 **Note:** Not to be confused with [RenderingDevice.texture_create()](class_renderingdevice.md#class_RenderingDevice_method_texture_create), which creates the graphics API's own texture type as opposed to the Godot-specific [Texture2D](class_texture2d.md#class_Texture2D) resource.

---

<span id="class_RenderingServer_method_texture_2d_get"></span>

[Image](class_image.md#class_Image) **texture_2d_get** ( texture: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_texture_2d_get)

Returns an [Image](class_image.md#class_Image) instance from the given `texture` [RID](class_rid.md#class_RID).

 **Example:** Get the test texture from [get_test_texture()](class_renderingserver.md#class_RenderingServer_method_get_test_texture) and apply it to a [Sprite2D](class_sprite2d.md#class_Sprite2D) node:

::

    var texture_rid = RenderingServer.get_test_texture()
    var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
    $Sprite2D.texture = texture

---

<span id="class_RenderingServer_method_texture_2d_layer_get"></span>

[Image](class_image.md#class_Image) **texture_2d_layer_get** ( texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_texture_2d_layer_get)

Returns an [Image](class_image.md#class_Image) instance from the given `texture` [RID](class_rid.md#class_RID) and `layer`.

---

<span id="class_RenderingServer_method_texture_2d_layered_create"></span>

[RID](class_rid.md#class_RID) **texture_2d_layered_create** ( layers: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\], layered_type: [TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_2d_layered_create)

Creates a 2-dimensional layered texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_2d_layered_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [TextureLayered](class_texturelayered.md#class_TextureLayered).

---

<span id="class_RenderingServer_method_texture_2d_layered_placeholder_create"></span>

[RID](class_rid.md#class_RID) **texture_2d_layered_placeholder_create** ( layered_type: [TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_2d_layered_placeholder_create)

Creates a placeholder for a 2-dimensional layered texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_2d_layered_*` RenderingServer functions, although it does nothing when used. See also [texture_2d_placeholder_create()](class_renderingserver.md#class_RenderingServer_method_texture_2d_placeholder_create).

 **Note:** The equivalent resource is [PlaceholderTextureLayered](class_placeholdertexturelayered.md#class_PlaceholderTextureLayered).

---

<span id="class_RenderingServer_method_texture_2d_placeholder_create"></span>

[RID](class_rid.md#class_RID) **texture_2d_placeholder_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_2d_placeholder_create)

Creates a placeholder for a 2-dimensional layered texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_2d_layered_*` RenderingServer functions, although it does nothing when used. See also [texture_2d_layered_placeholder_create()](class_renderingserver.md#class_RenderingServer_method_texture_2d_layered_placeholder_create).

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [PlaceholderTexture2D](class_placeholdertexture2d.md#class_PlaceholderTexture2D).

---

<span id="class_RenderingServer_method_texture_2d_update"></span>

void **texture_2d_update** ( texture: [RID](class_rid.md#class_RID), image: [Image](class_image.md#class_Image), layer: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_2d_update)

Updates the texture specified by the `texture` [RID](class_rid.md#class_RID) with the data in `image`. A `layer` must also be specified, which should be `0` when updating a single-layer texture ([Texture2D](class_texture2d.md#class_Texture2D)).

 **Note:** The `image` must have the same width, height and format as the current `texture` data. Otherwise, an error will be printed and the original texture won't be modified. If you need to use different width, height or format, use [texture_replace()](class_renderingserver.md#class_RenderingServer_method_texture_replace) instead.

---

<span id="class_RenderingServer_method_texture_3d_create"></span>

[RID](class_rid.md#class_RID) **texture_3d_create** ( format: [Format](class_image.md#enum_Image_Format), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), mipmaps: [bool](class_bool.md#class_bool), data: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_3d_create)

**Note:** The equivalent resource is [Texture3D](class_texture3d.md#class_Texture3D).

---

<span id="class_RenderingServer_method_texture_3d_get"></span>

[Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] **texture_3d_get** ( texture: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_texture_3d_get)

Returns 3D texture data as an array of [Image](class_image.md#class_Image) s for the specified texture [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_texture_3d_placeholder_create"></span>

[RID](class_rid.md#class_RID) **texture_3d_placeholder_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_3d_placeholder_create)

Creates a placeholder for a 3-dimensional texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_3d_*` RenderingServer functions, although it does nothing when used.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [PlaceholderTexture3D](class_placeholdertexture3d.md#class_PlaceholderTexture3D).

---

<span id="class_RenderingServer_method_texture_3d_update"></span>

void **texture_3d_update** ( texture: [RID](class_rid.md#class_RID), data: [Array](class_array.md#class_Array)\[[Image](class_image.md#class_Image)\] ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_3d_update)

Updates the texture specified by the `texture` [RID](class_rid.md#class_RID)'s data with the data in `data`. All the texture's layers must be replaced at once.

 **Note:** The `texture` must have the same width, height, depth and format as the current texture data. Otherwise, an error will be printed and the original texture won't be modified. If you need to use different width, height, depth or format, use [texture_replace()](class_renderingserver.md#class_RenderingServer_method_texture_replace) instead.

---

<span id="class_RenderingServer_method_texture_create_from_native_handle"></span>

[RID](class_rid.md#class_RID) **texture_create_from_native_handle** ( type: [TextureType](class_renderingserver.md#enum_RenderingServer_TextureType), format: [Format](class_image.md#enum_Image_Format), native_handle: [int](class_int.md#class_int), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), layers: [int](class_int.md#class_int) = 1, layered_type: [TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) = 0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_create_from_native_handle)

Creates a texture based on a native handle that was created outside of Godot's renderer.

 **Note:** If using only the rendering device renderer, it's recommend to use [RenderingDevice.texture_create_from_extension()](class_renderingdevice.md#class_RenderingDevice_method_texture_create_from_extension) together with [texture_rd_create()](class_renderingserver.md#class_RenderingServer_method_texture_rd_create), rather than this method. This way, the texture's format and usage can be controlled more effectively.

---

<span id="class_RenderingServer_method_texture_drawable_blit_rect"></span>

void **texture_drawable_blit_rect** ( textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], rect: [Rect2i](class_rect2i.md#class_Rect2i), material: [RID](class_rid.md#class_RID), modulate: [Color](class_color.md#class_Color), source_textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], to_mipmap: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_drawable_blit_rect)

Draws to `rect` on up to 4 given Drawable `textures`, using a TextureBlit Shader from `material`. `modulate` and up to 4 `source_textures` are uniforms for the Shader to process with. `to_mipmap` can specify to perform this draw to a lower mipmap level.

 **Note:** All `textures` must be the same size and format.

---

<span id="class_RenderingServer_method_texture_drawable_create"></span>

[RID](class_rid.md#class_RID) **texture_drawable_create** ( width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), format: [TextureDrawableFormat](class_renderingserver.md#enum_RenderingServer_TextureDrawableFormat), color: [Color](class_color.md#class_Color) = Color(1, 1, 1, 1), with_mipmaps: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_drawable_create)

Creates a 2-dimensional texture and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `texture_drawable*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent resource is [DrawableTexture2D](class_drawabletexture2d.md#class_DrawableTexture2D).

---

<span id="class_RenderingServer_method_texture_drawable_generate_mipmaps"></span>

void **texture_drawable_generate_mipmaps** ( texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_drawable_generate_mipmaps)

Calculates new MipMaps for the given Drawable `texture`.

---

<span id="class_RenderingServer_method_texture_drawable_get_default_material"></span>

[RID](class_rid.md#class_RID) **texture_drawable_get_default_material** ( ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_texture_drawable_get_default_material)

Returns a ShaderMaterial with the default texture_blit Shader.

---

<span id="class_RenderingServer_method_texture_get_format"></span>

[Format](class_image.md#enum_Image_Format) **texture_get_format** ( texture: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_texture_get_format)

Returns the format for the texture.

---

<span id="class_RenderingServer_method_texture_get_native_handle"></span>

[int](class_int.md#class_int) **texture_get_native_handle** ( texture: [RID](class_rid.md#class_RID), srgb: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_texture_get_native_handle)

Returns the internal graphics handle for this texture object. For use when communicating with third-party APIs mostly with GDExtension.

 `srgb` should be `true` when the texture uses nonlinear sRGB encoding and `false` when the texture uses linear encoding.

 **Note:** This function returns a `uint64_t` which internally maps to a `GLuint` (OpenGL) or `VkImage` (Vulkan).

---

<span id="class_RenderingServer_method_texture_get_path"></span>

[String](class_string.md#class_String) **texture_get_path** ( texture: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_texture_get_path)

Returns the resource path (starting with `res://` or `uid://`) for the specified texture RID. Returns an empty [String](class_string.md#class_String) if the resource is built-in. See also [texture_set_path()](class_renderingserver.md#class_RenderingServer_method_texture_set_path).

---

<span id="class_RenderingServer_method_texture_get_rd_texture"></span>

[RID](class_rid.md#class_RID) **texture_get_rd_texture** ( texture: [RID](class_rid.md#class_RID), srgb: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_texture_get_rd_texture)

Returns a texture [RID](class_rid.md#class_RID) that can be used with [RenderingDevice](class_renderingdevice.md#class_RenderingDevice).

 `srgb` should be `true` when the texture uses nonlinear sRGB encoding and `false` when the texture uses linear encoding.

---

<span id="class_RenderingServer_method_texture_proxy_create"></span>

[RID](class_rid.md#class_RID) **texture_proxy_create** ( base: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_proxy_create)

**Deprecated:** ProxyTexture was removed in Godot 4.

This method does nothing and always returns an invalid [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_texture_proxy_update"></span>

void **texture_proxy_update** ( texture: [RID](class_rid.md#class_RID), proxy_to: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_proxy_update)

**Deprecated:** ProxyTexture was removed in Godot 4.

This method does nothing.

---

<span id="class_RenderingServer_method_texture_rd_create"></span>

[RID](class_rid.md#class_RID) **texture_rd_create** ( rd_texture: [RID](class_rid.md#class_RID), layer_type: [TextureLayeredType](class_renderingserver.md#enum_RenderingServer_TextureLayeredType) = 0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_rd_create)

Creates a new texture object based on a texture created directly on the [RenderingDevice](class_renderingdevice.md#class_RenderingDevice). If the texture contains layers, `layer_type` is used to define the layer type.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) won't free the underlying `rd_texture`, you will want to free the `rd_texture` using [RenderingDevice.free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid).

---

<span id="class_RenderingServer_method_texture_replace"></span>

void **texture_replace** ( texture: [RID](class_rid.md#class_RID), by_texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_replace)

Replaces `texture`'s texture data by the texture specified by the `by_texture` RID, without changing `texture`'s RID.

---

<span id="class_RenderingServer_method_texture_set_force_redraw_if_visible"></span>

void **texture_set_force_redraw_if_visible** ( texture: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_set_force_redraw_if_visible)

Sets whether the texture RID should force redrawing when it's visible on screen when [OS.low_processor_usage_mode](class_os.md#class_OS_property_low_processor_usage_mode) is `true`. This is used by [AnimatedTexture](class_animatedtexture.md#class_AnimatedTexture) to force redrawing.

---

<span id="class_RenderingServer_method_texture_set_path"></span>

void **texture_set_path** ( texture: [RID](class_rid.md#class_RID), path: [String](class_string.md#class_String) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_set_path)

Sets the resource path for this texture RID. See also [texture_get_path()](class_renderingserver.md#class_RenderingServer_method_texture_get_path).

 **Note:** This is purely a hint and does not cause the texture to be automatically saved when set to a `res://` path.

---

<span id="class_RenderingServer_method_texture_set_size_override"></span>

void **texture_set_size_override** ( texture: [RID](class_rid.md#class_RID), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_texture_set_size_override)

Sets the size at which the texture should be *displayed* in 2D, ignoring its original size. This does not rescale the texture data itself, only how it is drawn in 2D. Set `width` and `height` to 0 to disable the size override.

---

<span id="class_RenderingServer_method_viewport_attach_camera"></span>

void **viewport_attach_camera** ( viewport: [RID](class_rid.md#class_RID), camera: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_attach_camera)

Sets a viewport's camera.

---

<span id="class_RenderingServer_method_viewport_attach_canvas"></span>

void **viewport_attach_canvas** ( viewport: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_attach_canvas)

Sets a viewport's canvas.

---

<span id="class_RenderingServer_method_viewport_attach_to_screen"></span>

void **viewport_attach_to_screen** ( viewport: [RID](class_rid.md#class_RID), rect: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), screen: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_attach_to_screen)

Copies the viewport to a region of the screen specified by `rect`. If [viewport_set_render_direct_to_screen()](class_renderingserver.md#class_RenderingServer_method_viewport_set_render_direct_to_screen) is `true`, then the viewport does not use a framebuffer and the contents of the viewport are rendered directly to screen. However, note that the root viewport is drawn last, therefore it will draw over the screen. Accordingly, you must set the root viewport to an area that does not cover the area that you have attached this viewport to.

For example, you can set the root viewport to not render at all with the following code:

.. tabs::

```
```

    func _ready():
        RenderingServer.viewport_attach_to_screen(get_viewport().get_viewport_rid(), Rect2())
        RenderingServer.viewport_attach_to_screen($Viewport.get_viewport_rid(), Rect2(0, 0, 600, 600))

Using this can result in significant optimization, especially on lower-end devices. However, it comes at the cost of having to manage your viewports manually. For further optimization, see [viewport_set_render_direct_to_screen()](class_renderingserver.md#class_RenderingServer_method_viewport_set_render_direct_to_screen).

---

<span id="class_RenderingServer_method_viewport_create"></span>

[RID](class_rid.md#class_RID) **viewport_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_create)

Creates an empty viewport and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `viewport_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent node is [Viewport](class_viewport.md#class_Viewport).

---

<span id="class_RenderingServer_method_viewport_get_measured_render_time_cpu"></span>

[float](class_float.md#class_float) **viewport_get_measured_render_time_cpu** ( viewport: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_cpu)

Returns the CPU time taken to render the last frame in milliseconds. This *only* includes time spent in rendering-related operations; scripts' `_process` functions and other engine subsystems are not included in this readout. To get a complete readout of CPU time spent to render the scene, sum the render times of all viewports that are drawn every frame plus [get_frame_setup_time_cpu()](class_renderingserver.md#class_RenderingServer_method_get_frame_setup_time_cpu). Unlike [Engine.get_frames_per_second()](class_engine.md#class_Engine_method_get_frames_per_second), this method will accurately reflect CPU utilization even if framerate is capped via V-Sync or [Engine.max_fps](class_engine.md#class_Engine_property_max_fps). See also [viewport_get_measured_render_time_gpu()](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_gpu).

 **Note:** Requires measurements to be enabled on the specified `viewport` using [viewport_set_measure_render_time()](class_renderingserver.md#class_RenderingServer_method_viewport_set_measure_render_time). Otherwise, this method returns `0.0`.

---

<span id="class_RenderingServer_method_viewport_get_measured_render_time_gpu"></span>

[float](class_float.md#class_float) **viewport_get_measured_render_time_gpu** ( viewport: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_gpu)

Returns the GPU time taken to render the last frame in milliseconds. To get a complete readout of GPU time spent to render the scene, sum the render times of all viewports that are drawn every frame. Unlike [Engine.get_frames_per_second()](class_engine.md#class_Engine_method_get_frames_per_second), this method accurately reflects GPU utilization even if framerate is capped via V-Sync or [Engine.max_fps](class_engine.md#class_Engine_property_max_fps). See also [viewport_get_measured_render_time_cpu()](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_cpu).

 **Note:** Requires measurements to be enabled on the specified `viewport` using [viewport_set_measure_render_time()](class_renderingserver.md#class_RenderingServer_method_viewport_set_measure_render_time). Otherwise, this method returns `0.0`.

 **Note:** When GPU utilization is low enough during a certain period of time, GPUs will decrease their power state (which in turn decreases core and memory clock speeds). This can cause the reported GPU time to increase if GPU utilization is kept low enough by a framerate cap (compared to what it would be at the GPU's highest power state). Keep this in mind when benchmarking using [viewport_get_measured_render_time_gpu()](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_gpu). This behavior can be overridden in the graphics driver settings at the cost of higher power usage.

---

<span id="class_RenderingServer_method_viewport_get_render_info"></span>

[int](class_int.md#class_int) **viewport_get_render_info** ( viewport: [RID](class_rid.md#class_RID), type: [ViewportRenderInfoType](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfoType), info: [ViewportRenderInfo](class_renderingserver.md#enum_RenderingServer_ViewportRenderInfo) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_get_render_info)

Returns a statistic about the rendering engine which can be used for performance profiling. This is separated into render pass `type` s, each of them having the same `info` s you can query (different passes will return different values).

See also [get_rendering_info()](class_renderingserver.md#class_RenderingServer_method_get_rendering_info), which returns global information across all viewports.

 **Note:** Viewport rendering information is not available until at least 2 frames have been rendered by the engine. If rendering information is not available, [viewport_get_render_info()](class_renderingserver.md#class_RenderingServer_method_viewport_get_render_info) returns `0`. To print rendering information in `_ready()` successfully, use the following:

::

    func _ready():
        for _i in 2:
            await get_tree().process_frame

        print(
                RenderingServer.viewport_get_render_info(get_viewport().get_viewport_rid(),
                RenderingServer.VIEWPORT_RENDER_INFO_TYPE_VISIBLE,
                RenderingServer.VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME)
        )

---

<span id="class_RenderingServer_method_viewport_get_render_target"></span>

[RID](class_rid.md#class_RID) **viewport_get_render_target** ( viewport: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_get_render_target)

Returns the render target for the viewport.

---

<span id="class_RenderingServer_method_viewport_get_texture"></span>

[RID](class_rid.md#class_RID) **viewport_get_texture** ( viewport: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_get_texture)

Returns the viewport's last rendered frame.

---

<span id="class_RenderingServer_method_viewport_get_update_mode"></span>

[ViewportUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode) **viewport_get_update_mode** ( viewport: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_get_update_mode)

Returns the viewport's update mode.

 **Warning:** Calling this from any thread other than the rendering thread will be detrimental to performance.

---

<span id="class_RenderingServer_method_viewport_remove_canvas"></span>

void **viewport_remove_canvas** ( viewport: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_remove_canvas)

Detaches a viewport from a canvas.

---

<span id="class_RenderingServer_method_viewport_set_active"></span>

void **viewport_set_active** ( viewport: [RID](class_rid.md#class_RID), active: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_active)

If `true`, sets the viewport active, else sets it inactive.

---

<span id="class_RenderingServer_method_viewport_set_anisotropic_filtering_level"></span>

void **viewport_set_anisotropic_filtering_level** ( viewport: [RID](class_rid.md#class_RID), anisotropic_filtering_level: [ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_anisotropic_filtering_level)

Sets the maximum number of samples to take when using anisotropic filtering on textures (as a power of two). A higher sample count will result in sharper textures at oblique angles, but is more expensive to compute. A value of `0` forcibly disables anisotropic filtering, even on materials where it is enabled.

The anisotropic filtering level also affects decals and light projectors if they are configured to use anisotropic filtering. See ProjectSettings.rendering/textures/decals/filter and ProjectSettings.rendering/textures/light_projectors/filter.

 **Note:** In 3D, for this setting to have an effect, set [BaseMaterial3D.texture_filter](class_basematerial3d.md#class_BaseMaterial3D_property_texture_filter) to [BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC](class_basematerial3d.md#class_BaseMaterial3D_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC) or [BaseMaterial3D.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC](class_basematerial3d.md#class_BaseMaterial3D_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC) on materials.

 **Note:** In 2D, for this setting to have an effect, set [CanvasItem.texture_filter](class_canvasitem.md#class_CanvasItem_property_texture_filter) to [CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC](class_canvasitem.md#class_CanvasItem_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC) or [CanvasItem.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC](class_canvasitem.md#class_CanvasItem_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC) on the [CanvasItem](class_canvasitem.md#class_CanvasItem) node displaying the texture (or in [CanvasTexture](class_canvastexture.md#class_CanvasTexture)). However, anisotropic filtering is rarely useful in 2D, so only enable it for textures in 2D if it makes a meaningful visual difference.

---

<span id="class_RenderingServer_method_viewport_set_canvas_cull_mask"></span>

void **viewport_set_canvas_cull_mask** ( viewport: [RID](class_rid.md#class_RID), canvas_cull_mask: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_canvas_cull_mask)

Sets the rendering mask associated with this [Viewport](class_viewport.md#class_Viewport). Only [CanvasItem](class_canvasitem.md#class_CanvasItem) nodes with a matching rendering visibility layer will be rendered by this [Viewport](class_viewport.md#class_Viewport).

---

<span id="class_RenderingServer_method_viewport_set_canvas_stacking"></span>

void **viewport_set_canvas_stacking** ( viewport: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int), sublayer: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_canvas_stacking)

Sets the stacking order for a viewport's canvas.

 `layer` is the actual canvas layer, while `sublayer` specifies the stacking order of the canvas among those in the same layer.

 **Note:** `layer` should be between [CANVAS_LAYER_MIN](class_renderingserver.md#class_RenderingServer_constant_CANVAS_LAYER_MIN) and [CANVAS_LAYER_MAX](class_renderingserver.md#class_RenderingServer_constant_CANVAS_LAYER_MAX) (inclusive). Any other value will wrap around.

---

<span id="class_RenderingServer_method_viewport_set_canvas_transform"></span>

void **viewport_set_canvas_transform** ( viewport: [RID](class_rid.md#class_RID), canvas: [RID](class_rid.md#class_RID), offset: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_canvas_transform)

Sets the transformation of a viewport's canvas.

---

<span id="class_RenderingServer_method_viewport_set_clear_mode"></span>

void **viewport_set_clear_mode** ( viewport: [RID](class_rid.md#class_RID), clear_mode: [ViewportClearMode](class_renderingserver.md#enum_RenderingServer_ViewportClearMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_clear_mode)

Sets the clear mode of a viewport.

---

<span id="class_RenderingServer_method_viewport_set_debug_draw"></span>

void **viewport_set_debug_draw** ( viewport: [RID](class_rid.md#class_RID), draw: [ViewportDebugDraw](class_renderingserver.md#enum_RenderingServer_ViewportDebugDraw) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_debug_draw)

Sets the debug draw mode of a viewport.

---

<span id="class_RenderingServer_method_viewport_set_default_canvas_item_texture_filter"></span>

void **viewport_set_default_canvas_item_texture_filter** ( viewport: [RID](class_rid.md#class_RID), filter: [CanvasItemTextureFilter](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureFilter) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_default_canvas_item_texture_filter)

Sets the default texture filtering mode for the specified `viewport` RID.

---

<span id="class_RenderingServer_method_viewport_set_default_canvas_item_texture_repeat"></span>

void **viewport_set_default_canvas_item_texture_repeat** ( viewport: [RID](class_rid.md#class_RID), repeat: [CanvasItemTextureRepeat](class_renderingserver.md#enum_RenderingServer_CanvasItemTextureRepeat) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_default_canvas_item_texture_repeat)

Sets the default texture repeat mode for the specified `viewport` RID.

---

<span id="class_RenderingServer_method_viewport_set_disable_2d"></span>

void **viewport_set_disable_2d** ( viewport: [RID](class_rid.md#class_RID), disable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_disable_2d)

If `true`, the viewport's canvas (i.e. 2D and GUI elements) is not rendered.

---

<span id="class_RenderingServer_method_viewport_set_disable_3d"></span>

void **viewport_set_disable_3d** ( viewport: [RID](class_rid.md#class_RID), disable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_disable_3d)

If `true`, the viewport's 3D elements are not rendered.

---

<span id="class_RenderingServer_method_viewport_set_environment_mode"></span>

void **viewport_set_environment_mode** ( viewport: [RID](class_rid.md#class_RID), mode: [ViewportEnvironmentMode](class_renderingserver.md#enum_RenderingServer_ViewportEnvironmentMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_environment_mode)

Sets the viewport's environment mode which allows enabling or disabling rendering of 3D environment over 2D canvas. When disabled, 2D will not be affected by the environment. When enabled, 2D will be affected by the environment if the environment background mode is [ENV_BG_CANVAS](class_renderingserver.md#class_RenderingServer_constant_ENV_BG_CANVAS). The default behavior is to inherit the setting from the viewport's parent. If the topmost parent is also set to [VIEWPORT_ENVIRONMENT_INHERIT](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_INHERIT), then the behavior will be the same as if it was set to [VIEWPORT_ENVIRONMENT_ENABLED](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_ENABLED).

---

<span id="class_RenderingServer_method_viewport_set_fsr_sharpness"></span>

void **viewport_set_fsr_sharpness** ( viewport: [RID](class_rid.md#class_RID), sharpness: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_fsr_sharpness)

Determines how sharp the upscaled image will be when using the FSR upscaling mode. Sharpness halves with every whole number. Values go from 0.0 (sharpest) to 2.0. Values above 2.0 won't make a visible difference.

---

<span id="class_RenderingServer_method_viewport_set_global_canvas_transform"></span>

void **viewport_set_global_canvas_transform** ( viewport: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_global_canvas_transform)

Sets the viewport's global transformation matrix.

---

<span id="class_RenderingServer_method_viewport_set_measure_render_time"></span>

void **viewport_set_measure_render_time** ( viewport: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_measure_render_time)

Sets the measurement for the given `viewport` RID (obtained using [Viewport.get_viewport_rid()](class_viewport.md#class_Viewport_method_get_viewport_rid)). Once enabled, [viewport_get_measured_render_time_cpu()](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_cpu) and [viewport_get_measured_render_time_gpu()](class_renderingserver.md#class_RenderingServer_method_viewport_get_measured_render_time_gpu) will return values greater than `0.0` when queried with the given `viewport`.

---

<span id="class_RenderingServer_method_viewport_set_msaa_2d"></span>

void **viewport_set_msaa_2d** ( viewport: [RID](class_rid.md#class_RID), msaa: [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_msaa_2d)

Sets the multisample antialiasing mode for 2D/Canvas on the specified `viewport` RID. Equivalent to ProjectSettings.rendering/anti_aliasing/quality/msaa_2d or [Viewport.msaa_2d](class_viewport.md#class_Viewport_property_msaa_2d).

---

<span id="class_RenderingServer_method_viewport_set_msaa_3d"></span>

void **viewport_set_msaa_3d** ( viewport: [RID](class_rid.md#class_RID), msaa: [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_msaa_3d)

Sets the multisample antialiasing mode for 3D on the specified `viewport` RID. Equivalent to ProjectSettings.rendering/anti_aliasing/quality/msaa_3d or [Viewport.msaa_3d](class_viewport.md#class_Viewport_property_msaa_3d).

---

<span id="class_RenderingServer_method_viewport_set_occlusion_culling_build_quality"></span>

void **viewport_set_occlusion_culling_build_quality** ( quality: [ViewportOcclusionCullingBuildQuality](class_renderingserver.md#enum_RenderingServer_ViewportOcclusionCullingBuildQuality) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_occlusion_culling_build_quality)

Sets the ProjectSettings.rendering/occlusion_culling/bvh_build_quality to use for occlusion culling. This parameter is global and cannot be set on a per-viewport basis.

---

<span id="class_RenderingServer_method_viewport_set_occlusion_rays_per_thread"></span>

void **viewport_set_occlusion_rays_per_thread** ( rays_per_thread: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_occlusion_rays_per_thread)

Sets the ProjectSettings.rendering/occlusion_culling/occlusion_rays_per_thread to use for occlusion culling. This parameter is global and cannot be set on a per-viewport basis.

---

<span id="class_RenderingServer_method_viewport_set_parent_viewport"></span>

void **viewport_set_parent_viewport** ( viewport: [RID](class_rid.md#class_RID), parent_viewport: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_parent_viewport)

Sets the viewport's parent to the viewport specified by the `parent_viewport` RID.

---

<span id="class_RenderingServer_method_viewport_set_positional_shadow_atlas_quadrant_subdivision"></span>

void **viewport_set_positional_shadow_atlas_quadrant_subdivision** ( viewport: [RID](class_rid.md#class_RID), quadrant: [int](class_int.md#class_int), subdivision: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_positional_shadow_atlas_quadrant_subdivision)

Sets the number of subdivisions to use in the specified shadow atlas `quadrant` for omni and spot shadows. See also [Viewport.set_positional_shadow_atlas_quadrant_subdiv()](class_viewport.md#class_Viewport_method_set_positional_shadow_atlas_quadrant_subdiv).

---

<span id="class_RenderingServer_method_viewport_set_positional_shadow_atlas_size"></span>

void **viewport_set_positional_shadow_atlas_size** ( viewport: [RID](class_rid.md#class_RID), size: [int](class_int.md#class_int), use_16_bits: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_positional_shadow_atlas_size)

Sets the `size` of the shadow atlas's images (used for omni and spot lights) on the viewport specified by the `viewport` RID. The value is rounded up to the nearest power of 2. If `use_16_bits` is `true`, use 16 bits for the omni/spot shadow depth map. Enabling this results in shadows having less precision and may result in shadow acne, but can lead to performance improvements on some devices.

 **Note:** If this is set to `0`, no positional shadows will be visible at all. This can improve performance significantly on low-end systems by reducing both the CPU and GPU load (as fewer draw calls are needed to draw the scene without shadows).

---

<span id="class_RenderingServer_method_viewport_set_render_direct_to_screen"></span>

void **viewport_set_render_direct_to_screen** ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_render_direct_to_screen)

If `true`, render the contents of the viewport directly to screen. This allows a low-level optimization where you can skip drawing a viewport to the root viewport. While this optimization can result in a significant increase in speed (especially on older devices), it comes at a cost of usability. When this is enabled, you cannot read from the viewport or from the screen_texture. You also lose the benefit of certain window settings, such as the various stretch modes. Another consequence to be aware of is that in 2D the rendering happens in window coordinates, so if you have a viewport that is double the size of the window, and you set this, then only the portion that fits within the window will be drawn, no automatic scaling is possible, even if your game scene is significantly larger than the window size.

---

<span id="class_RenderingServer_method_viewport_set_scaling_3d_mode"></span>

void **viewport_set_scaling_3d_mode** ( viewport: [RID](class_rid.md#class_RID), scaling_3d_mode: [ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_scaling_3d_mode)

Sets the 3D resolution scaling mode. Bilinear scaling renders at different resolution to either undersample or supersample the viewport. FidelityFX Super Resolution 1.0, abbreviated to FSR, is an upscaling technology that produces high quality images at fast framerates by using a spatially aware upscaling algorithm. FSR is slightly more expensive than bilinear, but it produces significantly higher image quality. FSR should be used where possible.

---

<span id="class_RenderingServer_method_viewport_set_scaling_3d_scale"></span>

void **viewport_set_scaling_3d_scale** ( viewport: [RID](class_rid.md#class_RID), scale: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_scaling_3d_scale)

Scales the 3D render buffer based on the viewport size uses an image filter specified in [ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) to scale the output image to the full viewport size. Values lower than `1.0` can be used to speed up 3D rendering at the cost of quality (undersampling). Values greater than `1.0` are only valid for bilinear mode and can be used to improve 3D rendering quality at a high performance cost (supersampling). See also [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) for multi-sample antialiasing, which is significantly cheaper but only smoothens the edges of polygons.

When using FSR upscaling, AMD recommends exposing the following values as preset options to users "Ultra Quality: 0.77", "Quality: 0.67", "Balanced: 0.59", "Performance: 0.5" instead of exposing the entire scale.

---

<span id="class_RenderingServer_method_viewport_set_scenario"></span>

void **viewport_set_scenario** ( viewport: [RID](class_rid.md#class_RID), scenario: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_scenario)

Sets a viewport's scenario. The scenario contains information about environment information, reflection atlas, etc.

---

<span id="class_RenderingServer_method_viewport_set_screen_space_aa"></span>

void **viewport_set_screen_space_aa** ( viewport: [RID](class_rid.md#class_RID), mode: [ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_screen_space_aa)

Sets the viewport's screen-space antialiasing mode. Equivalent to ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa or [Viewport.screen_space_aa](class_viewport.md#class_Viewport_property_screen_space_aa).

---

<span id="class_RenderingServer_method_viewport_set_sdf_oversize_and_scale"></span>

void **viewport_set_sdf_oversize_and_scale** ( viewport: [RID](class_rid.md#class_RID), oversize: [ViewportSDFOversize](class_renderingserver.md#enum_RenderingServer_ViewportSDFOversize), scale: [ViewportSDFScale](class_renderingserver.md#enum_RenderingServer_ViewportSDFScale) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_sdf_oversize_and_scale)

Sets the viewport's 2D signed distance field ProjectSettings.rendering/2d/sdf/oversize and ProjectSettings.rendering/2d/sdf/scale. This is used when sampling the signed distance field in [CanvasItem](class_canvasitem.md#class_CanvasItem) shaders as well as [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) collision. This is *not* used by SDFGI in 3D rendering.

---

<span id="class_RenderingServer_method_viewport_set_size"></span>

void **viewport_set_size** ( viewport: [RID](class_rid.md#class_RID), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_size)

Sets the viewport's width and height in pixels.

---

<span id="class_RenderingServer_method_viewport_set_snap_2d_transforms_to_pixel"></span>

void **viewport_set_snap_2d_transforms_to_pixel** ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_snap_2d_transforms_to_pixel)

If `true`, canvas item transforms (i.e. origin position) are snapped to the nearest pixel when rendering. This can lead to a crisper appearance at the cost of less smooth movement, especially when [Camera2D](class_camera2d.md#class_Camera2D) smoothing is enabled. Equivalent to ProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel.

---

<span id="class_RenderingServer_method_viewport_set_snap_2d_vertices_to_pixel"></span>

void **viewport_set_snap_2d_vertices_to_pixel** ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_snap_2d_vertices_to_pixel)

If `true`, canvas item vertices (i.e. polygon points) are snapped to the nearest pixel when rendering. This can lead to a crisper appearance at the cost of less smooth movement, especially when [Camera2D](class_camera2d.md#class_Camera2D) smoothing is enabled. Equivalent to ProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel.

---

<span id="class_RenderingServer_method_viewport_set_texture_mipmap_bias"></span>

void **viewport_set_texture_mipmap_bias** ( viewport: [RID](class_rid.md#class_RID), mipmap_bias: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_texture_mipmap_bias)

Affects the final texture sharpness by reading from a lower or higher mipmap (also called "texture LOD bias"). Negative values make mipmapped textures sharper but grainier when viewed at a distance, while positive values make mipmapped textures blurrier (even when up close). To get sharper textures at a distance without introducing too much graininess, set this between `-0.75` and `0.0`. Enabling temporal antialiasing (ProjectSettings.rendering/anti_aliasing/quality/use_taa) can help reduce the graininess visible when using negative mipmap bias.

 **Note:** When the 3D scaling mode is set to FSR 1.0, this value is used to adjust the automatic mipmap bias which is calculated internally based on the scale factor. The formula for this is `-log2(1.0 / scale) + mipmap_bias`.

---

<span id="class_RenderingServer_method_viewport_set_transparent_background"></span>

void **viewport_set_transparent_background** ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_transparent_background)

If `true`, the viewport renders its background as transparent.

---

<span id="class_RenderingServer_method_viewport_set_update_mode"></span>

void **viewport_set_update_mode** ( viewport: [RID](class_rid.md#class_RID), update_mode: [ViewportUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportUpdateMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_update_mode)

Sets when the viewport should be updated.

---

<span id="class_RenderingServer_method_viewport_set_use_debanding"></span>

void **viewport_set_use_debanding** ( viewport: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_debanding)

Equivalent to [Viewport.use_debanding](class_viewport.md#class_Viewport_property_use_debanding). See also ProjectSettings.rendering/anti_aliasing/quality/use_debanding.

---

<span id="class_RenderingServer_method_viewport_set_use_hdr_2d"></span>

void **viewport_set_use_hdr_2d** ( viewport: [RID](class_rid.md#class_RID), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_hdr_2d)

If `true`, 2D rendering will use a high dynamic range (HDR) `RGBA16` format framebuffer. Additionally, 2D rendering will be performed on linear values and will be converted using the appropriate transfer function immediately before blitting to the screen (if the Viewport is attached to the screen).

Practically speaking, this means that the end result of the Viewport will not be clamped to the `0-1` range and can be used in 3D rendering without color encoding adjustments. This allows 2D rendering to take advantage of effects requiring high dynamic range (e.g. 2D glow) as well as substantially improves the appearance of effects requiring highly detailed gradients. This setting has the same effect as [Viewport.use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d).

---

<span id="class_RenderingServer_method_viewport_set_use_occlusion_culling"></span>

void **viewport_set_use_occlusion_culling** ( viewport: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_occlusion_culling)

If `true`, enables occlusion culling on the specified viewport. Equivalent to ProjectSettings.rendering/occlusion_culling/use_occlusion_culling.

---

<span id="class_RenderingServer_method_viewport_set_use_taa"></span>

void **viewport_set_use_taa** ( viewport: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_taa)

If `true`, use temporal antialiasing. Equivalent to ProjectSettings.rendering/anti_aliasing/quality/use_taa or [Viewport.use_taa](class_viewport.md#class_Viewport_property_use_taa).

---

<span id="class_RenderingServer_method_viewport_set_use_xr"></span>

void **viewport_set_use_xr** ( viewport: [RID](class_rid.md#class_RID), use_xr: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_xr)

If `true`, the viewport uses augmented or virtual reality technologies. See [XRInterface](class_xrinterface.md#class_XRInterface).

---

<span id="class_RenderingServer_method_viewport_set_vrs_mode"></span>

void **viewport_set_vrs_mode** ( viewport: [RID](class_rid.md#class_RID), mode: [ViewportVRSMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_vrs_mode)

Sets the Variable Rate Shading (VRS) mode for the viewport. If the GPU does not support VRS, this property is ignored. Equivalent to ProjectSettings.rendering/vrs/mode.

---

<span id="class_RenderingServer_method_viewport_set_vrs_texture"></span>

void **viewport_set_vrs_texture** ( viewport: [RID](class_rid.md#class_RID), texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_vrs_texture)

The texture to use when the VRS mode is set to [VIEWPORT_VRS_TEXTURE](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_VRS_TEXTURE). Equivalent to ProjectSettings.rendering/vrs/texture.

---

<span id="class_RenderingServer_method_viewport_set_vrs_update_mode"></span>

void **viewport_set_vrs_update_mode** ( viewport: [RID](class_rid.md#class_RID), mode: [ViewportVRSUpdateMode](class_renderingserver.md#enum_RenderingServer_ViewportVRSUpdateMode) ) [🔗](class_renderingserver.md#class_RenderingServer_method_viewport_set_vrs_update_mode)

Sets the update mode for Variable Rate Shading (VRS) for the viewport. VRS requires the input texture to be converted to the format usable by the VRS method supported by the hardware. The update mode defines how often this happens. If the GPU does not support VRS, or VRS is not enabled, this property is ignored.

If set to [VIEWPORT_VRS_UPDATE_ONCE](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_ONCE), the input texture is copied once and the mode is changed to [VIEWPORT_VRS_UPDATE_DISABLED](class_renderingserver.md#class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_DISABLED).

---

<span id="class_RenderingServer_method_visibility_notifier_create"></span>

[RID](class_rid.md#class_RID) **visibility_notifier_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_visibility_notifier_create)

Creates a new 3D visibility notifier object and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `visibility_notifier_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

To place in a scene, attach this notifier to an instance using [instance_set_base()](class_renderingserver.md#class_RenderingServer_method_instance_set_base) using the returned RID.

 **Note:** The equivalent node is [VisibleOnScreenNotifier3D](class_visibleonscreennotifier3d.md#class_VisibleOnScreenNotifier3D).

---

<span id="class_RenderingServer_method_visibility_notifier_set_aabb"></span>

void **visibility_notifier_set_aabb** ( notifier: [RID](class_rid.md#class_RID), aabb: [AABB](class_aabb.md#class_AABB) ) [🔗](class_renderingserver.md#class_RenderingServer_method_visibility_notifier_set_aabb)

Sets the AABB of the specified visibility notifier.

---

<span id="class_RenderingServer_method_visibility_notifier_set_callbacks"></span>

void **visibility_notifier_set_callbacks** ( notifier: [RID](class_rid.md#class_RID), enter_callable: [Callable](class_callable.md#class_Callable), exit_callable: [Callable](class_callable.md#class_Callable) ) [🔗](class_renderingserver.md#class_RenderingServer_method_visibility_notifier_set_callbacks)

Sets the methods to be called when the notifier enters or exits the view.

---

<span id="class_RenderingServer_method_voxel_gi_allocate_data"></span>

void **voxel_gi_allocate_data** ( voxel_gi: [RID](class_rid.md#class_RID), to_cell_xform: [Transform3D](class_transform3d.md#class_Transform3D), aabb: [AABB](class_aabb.md#class_AABB), octree_size: [Vector3i](class_vector3i.md#class_Vector3i), octree_cells: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), data_cells: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), distance_field: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), level_counts: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_allocate_data)

Allocates and initializes the voxel GI data for the specified `voxel_gi` RID. `octree_cells` must be a multiple of 32. `octree_cells` must be double the size of `data_cells`. The allocated data can be retrieved later using the various `voxel_gi_get_*` methods.

---

<span id="class_RenderingServer_method_voxel_gi_create"></span>

[RID](class_rid.md#class_RID) **voxel_gi_create** ( ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_create)

Creates a new voxel-based global illumination object and adds it to the RenderingServer. It can be accessed with the RID that is returned. This RID will be used in all `voxel_gi_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the RenderingServer's [free_rid()](class_renderingserver.md#class_RenderingServer_method_free_rid) method.

 **Note:** The equivalent node is [VoxelGI](class_voxelgi.md#class_VoxelGI).

---

<span id="class_RenderingServer_method_voxel_gi_get_data_cells"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **voxel_gi_get_data_cells** ( voxel_gi: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_data_cells)

Returns the data cells for the specified voxel GI data instance. See also [voxel_gi_allocate_data()](class_renderingserver.md#class_RenderingServer_method_voxel_gi_allocate_data).

---

<span id="class_RenderingServer_method_voxel_gi_get_distance_field"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **voxel_gi_get_distance_field** ( voxel_gi: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_distance_field)

Returns the distance field data for the specified voxel GI data instance. See also [voxel_gi_allocate_data()](class_renderingserver.md#class_RenderingServer_method_voxel_gi_allocate_data).

---

<span id="class_RenderingServer_method_voxel_gi_get_level_counts"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **voxel_gi_get_level_counts** ( voxel_gi: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_level_counts)

Returns the level counts for the specified voxel GI data instance. See also [voxel_gi_allocate_data()](class_renderingserver.md#class_RenderingServer_method_voxel_gi_allocate_data).

---

<span id="class_RenderingServer_method_voxel_gi_get_octree_cells"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **voxel_gi_get_octree_cells** ( voxel_gi: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_octree_cells)

Returns the octree cell data for the specified voxel GI data instance. See also [voxel_gi_allocate_data()](class_renderingserver.md#class_RenderingServer_method_voxel_gi_allocate_data).

---

<span id="class_RenderingServer_method_voxel_gi_get_octree_size"></span>

[Vector3i](class_vector3i.md#class_Vector3i) **voxel_gi_get_octree_size** ( voxel_gi: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_octree_size)

Returns the octree size for the specified voxel GI data instance, which corresponds to the number of subdivisions per axis. This can be viewed in the editor by hovering the **Bake VoxelGI** button at the top of the 3D editor viewport when a [VoxelGI](class_voxelgi.md#class_VoxelGI) node is selected and looking at the **Subdivisions** field in the tooltip.

---

<span id="class_RenderingServer_method_voxel_gi_get_to_cell_xform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **voxel_gi_get_to_cell_xform** ( voxel_gi: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_get_to_cell_xform)

Returns the transform to cell space for the specified voxel GI data instance. See also [voxel_gi_allocate_data()](class_renderingserver.md#class_RenderingServer_method_voxel_gi_allocate_data).

---

<span id="class_RenderingServer_method_voxel_gi_set_baked_exposure_normalization"></span>

void **voxel_gi_set_baked_exposure_normalization** ( voxel_gi: [RID](class_rid.md#class_RID), baked_exposure: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_baked_exposure_normalization)

Used to inform the renderer what exposure normalization value was used while baking the voxel gi. This value will be used and modulated at run time to ensure that the voxel gi maintains a consistent level of exposure even if the scene-wide exposure normalization is changed at run time. For more information see [camera_attributes_set_exposure()](class_renderingserver.md#class_RenderingServer_method_camera_attributes_set_exposure).

---

<span id="class_RenderingServer_method_voxel_gi_set_bias"></span>

void **voxel_gi_set_bias** ( voxel_gi: [RID](class_rid.md#class_RID), bias: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_bias)

Sets the [VoxelGIData.bias](class_voxelgidata.md#class_VoxelGIData_property_bias) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_voxel_gi_set_dynamic_range"></span>

void **voxel_gi_set_dynamic_range** ( voxel_gi: [RID](class_rid.md#class_RID), range: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_dynamic_range)

Sets the [VoxelGIData.dynamic_range](class_voxelgidata.md#class_VoxelGIData_property_dynamic_range) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_voxel_gi_set_energy"></span>

void **voxel_gi_set_energy** ( voxel_gi: [RID](class_rid.md#class_RID), energy: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_energy)

Sets the [VoxelGIData.energy](class_voxelgidata.md#class_VoxelGIData_property_energy) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_voxel_gi_set_interior"></span>

void **voxel_gi_set_interior** ( voxel_gi: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_interior)

Sets the [VoxelGIData.interior](class_voxelgidata.md#class_VoxelGIData_property_interior) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_voxel_gi_set_normal_bias"></span>

void **voxel_gi_set_normal_bias** ( voxel_gi: [RID](class_rid.md#class_RID), bias: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_normal_bias)

Sets the [VoxelGIData.normal_bias](class_voxelgidata.md#class_VoxelGIData_property_normal_bias) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_voxel_gi_set_propagation"></span>

void **voxel_gi_set_propagation** ( voxel_gi: [RID](class_rid.md#class_RID), amount: [float](class_float.md#class_float) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_propagation)

Sets the [VoxelGIData.propagation](class_voxelgidata.md#class_VoxelGIData_property_propagation) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class_RID).

---

<span id="class_RenderingServer_method_voxel_gi_set_quality"></span>

void **voxel_gi_set_quality** ( quality: [VoxelGIQuality](class_renderingserver.md#enum_RenderingServer_VoxelGIQuality) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_quality)

Sets the ProjectSettings.rendering/global_illumination/voxel_gi/quality value to use when rendering. This parameter is global and cannot be set on a per-VoxelGI basis.

---

<span id="class_RenderingServer_method_voxel_gi_set_use_two_bounces"></span>

void **voxel_gi_set_use_two_bounces** ( voxel_gi: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingserver.md#class_RenderingServer_method_voxel_gi_set_use_two_bounces)

Sets the [VoxelGIData.use_two_bounces](class_voxelgidata.md#class_VoxelGIData_property_use_two_bounces) value to use on the specified `voxel_gi`'s [RID](class_rid.md#class_RID).
