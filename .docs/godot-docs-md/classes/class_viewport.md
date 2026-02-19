<span id="class_Viewport"></span>

## Viewport

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [SubViewport](class_subviewport.md#class_SubViewport), [Window](class_window.md#class_Window)

Abstract base class for viewports. Encapsulates drawing and interaction with a game world.

### Description

A **Viewport** creates a different view into the screen, or a sub-view inside another viewport. Child 2D nodes will display on it, and child Camera3D 3D nodes will render on it too.

Optionally, a viewport can have its own 2D or 3D world, so it doesn't share what it draws with other viewports.

Viewports can also choose to be audio listeners, so they generate positional audio depending on a 2D or 3D camera child of it.

Also, viewports can be assigned to different screens in case the devices have multiple screens.

Finally, viewports can also behave as render targets, in which case they will not be visible unless the associated texture is used to draw.

### Tutorials

- [Using Viewports](../tutorials/rendering/viewports.md)

- [Viewport and canvas transforms](../tutorials/2d/2d_transforms.md)

- GUI in 3D Viewport Demo

- 3D in 2D Viewport Demo

- 2D in 3D Viewport Demo

- Screen Capture Demo

- Dynamic Split Screen Demo

- 3D Resolution Scaling Demo

### Properties


| [AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) | [anisotropic_filtering_level](class_viewport.md#class_Viewport_property_anisotropic_filtering_level) | `2` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [audio_listener_enable_2d](class_viewport.md#class_Viewport_property_audio_listener_enable_2d) | `false` |
| [bool](class_bool.md#class_bool) | [audio_listener_enable_3d](class_viewport.md#class_Viewport_property_audio_listener_enable_3d) | `false` |
| [int](class_int.md#class_int) | [canvas_cull_mask](class_viewport.md#class_Viewport_property_canvas_cull_mask) | `4294967295` |
| [DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) | [canvas_item_default_texture_filter](class_viewport.md#class_Viewport_property_canvas_item_default_texture_filter) | `1` |
| [DefaultCanvasItemTextureRepeat](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat) | [canvas_item_default_texture_repeat](class_viewport.md#class_Viewport_property_canvas_item_default_texture_repeat) | `0` |
| [Transform2D](class_transform2d.md#class_Transform2D) | [canvas_transform](class_viewport.md#class_Viewport_property_canvas_transform) |
| [DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) | [debug_draw](class_viewport.md#class_Viewport_property_debug_draw) | `0` |
| [bool](class_bool.md#class_bool) | [disable_3d](class_viewport.md#class_Viewport_property_disable_3d) | `false` |
| [float](class_float.md#class_float) | [fsr_sharpness](class_viewport.md#class_Viewport_property_fsr_sharpness) | `0.2` |
| [Transform2D](class_transform2d.md#class_Transform2D) | [global_canvas_transform](class_viewport.md#class_Viewport_property_global_canvas_transform) |
| [bool](class_bool.md#class_bool) | [gui_disable_input](class_viewport.md#class_Viewport_property_gui_disable_input) | `false` |
| [int](class_int.md#class_int) | [gui_drag_threshold](class_viewport.md#class_Viewport_property_gui_drag_threshold) | `10` |
| [bool](class_bool.md#class_bool) | [gui_embed_subwindows](class_viewport.md#class_Viewport_property_gui_embed_subwindows) | `false` |
| [bool](class_bool.md#class_bool) | [gui_snap_controls_to_pixels](class_viewport.md#class_Viewport_property_gui_snap_controls_to_pixels) | `true` |
| [bool](class_bool.md#class_bool) | [handle_input_locally](class_viewport.md#class_Viewport_property_handle_input_locally) | `true` |
| [float](class_float.md#class_float) | [mesh_lod_threshold](class_viewport.md#class_Viewport_property_mesh_lod_threshold) | `1.0` |
| [MSAA](class_viewport.md#enum_Viewport_MSAA) | [msaa_2d](class_viewport.md#class_Viewport_property_msaa_2d) | `0` |
| [MSAA](class_viewport.md#enum_Viewport_MSAA) | [msaa_3d](class_viewport.md#class_Viewport_property_msaa_3d) | `0` |
| [bool](class_bool.md#class_bool) | [oversampling](class_viewport.md#class_Viewport_property_oversampling) | `true` |
| [float](class_float.md#class_float) | [oversampling_override](class_viewport.md#class_Viewport_property_oversampling_override) | `0.0` |
| [bool](class_bool.md#class_bool) | [own_world_3d](class_viewport.md#class_Viewport_property_own_world_3d) | `false` |
| [PhysicsInterpolationMode](class_node.md#enum_Node_PhysicsInterpolationMode) | physics_interpolation_mode | `1` (overrides [Node](class_node.md#class_Node_property_physics_interpolation_mode)) |
| [bool](class_bool.md#class_bool) | [physics_object_picking](class_viewport.md#class_Viewport_property_physics_object_picking) | `false` |
| [bool](class_bool.md#class_bool) | [physics_object_picking_first_only](class_viewport.md#class_Viewport_property_physics_object_picking_first_only) | `false` |
| [bool](class_bool.md#class_bool) | [physics_object_picking_sort](class_viewport.md#class_Viewport_property_physics_object_picking_sort) | `false` |
| [bool](class_bool.md#class_bool) | [positional_shadow_atlas_16_bits](class_viewport.md#class_Viewport_property_positional_shadow_atlas_16_bits) | `true` |
| [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) | [positional_shadow_atlas_quad_0](class_viewport.md#class_Viewport_property_positional_shadow_atlas_quad_0) | `2` |
| [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) | [positional_shadow_atlas_quad_1](class_viewport.md#class_Viewport_property_positional_shadow_atlas_quad_1) | `2` |
| [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) | [positional_shadow_atlas_quad_2](class_viewport.md#class_Viewport_property_positional_shadow_atlas_quad_2) | `3` |
| [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) | [positional_shadow_atlas_quad_3](class_viewport.md#class_Viewport_property_positional_shadow_atlas_quad_3) | `4` |
| [int](class_int.md#class_int) | [positional_shadow_atlas_size](class_viewport.md#class_Viewport_property_positional_shadow_atlas_size) | `2048` |
| [Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) | [scaling_3d_mode](class_viewport.md#class_Viewport_property_scaling_3d_mode) | `0` |
| [float](class_float.md#class_float) | [scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale) | `1.0` |
| [ScreenSpaceAA](class_viewport.md#enum_Viewport_ScreenSpaceAA) | [screen_space_aa](class_viewport.md#class_Viewport_property_screen_space_aa) | `0` |
| [SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) | [sdf_oversize](class_viewport.md#class_Viewport_property_sdf_oversize) | `1` |
| [SDFScale](class_viewport.md#enum_Viewport_SDFScale) | [sdf_scale](class_viewport.md#class_Viewport_property_sdf_scale) | `1` |
| [bool](class_bool.md#class_bool) | [snap_2d_transforms_to_pixel](class_viewport.md#class_Viewport_property_snap_2d_transforms_to_pixel) | `false` |
| [bool](class_bool.md#class_bool) | [snap_2d_vertices_to_pixel](class_viewport.md#class_Viewport_property_snap_2d_vertices_to_pixel) | `false` |
| [float](class_float.md#class_float) | [texture_mipmap_bias](class_viewport.md#class_Viewport_property_texture_mipmap_bias) | `0.0` |
| [bool](class_bool.md#class_bool) | [transparent_bg](class_viewport.md#class_Viewport_property_transparent_bg) | `false` |
| [bool](class_bool.md#class_bool) | [use_debanding](class_viewport.md#class_Viewport_property_use_debanding) | `false` |
| [bool](class_bool.md#class_bool) | [use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d) | `false` |
| [bool](class_bool.md#class_bool) | [use_occlusion_culling](class_viewport.md#class_Viewport_property_use_occlusion_culling) | `false` |
| [bool](class_bool.md#class_bool) | [use_taa](class_viewport.md#class_Viewport_property_use_taa) | `false` |
| [bool](class_bool.md#class_bool) | [use_xr](class_viewport.md#class_Viewport_property_use_xr) | `false` |
| [VRSMode](class_viewport.md#enum_Viewport_VRSMode) | [vrs_mode](class_viewport.md#class_Viewport_property_vrs_mode) | `0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [vrs_texture](class_viewport.md#class_Viewport_property_vrs_texture) |
| [VRSUpdateMode](class_viewport.md#enum_Viewport_VRSUpdateMode) | [vrs_update_mode](class_viewport.md#class_Viewport_property_vrs_update_mode) | `1` |
| [World2D](class_world2d.md#class_World2D) | [world_2d](class_viewport.md#class_Viewport_property_world_2d) |
| [World3D](class_world3d.md#class_World3D) | [world_3d](class_viewport.md#class_Viewport_property_world_3d) |

### Methods


| [World2D](class_world2d.md#class_World2D) | [find_world_2d](class_viewport.md#class_Viewport_method_find_world_2d) ( ) const |
| --- | --- |
| [World3D](class_world3d.md#class_World3D) | [find_world_3d](class_viewport.md#class_Viewport_method_find_world_3d) ( ) const |
| [AudioListener2D](class_audiolistener2d.md#class_AudioListener2D) | [get_audio_listener_2d](class_viewport.md#class_Viewport_method_get_audio_listener_2d) ( ) const |
| [AudioListener3D](class_audiolistener3d.md#class_AudioListener3D) | [get_audio_listener_3d](class_viewport.md#class_Viewport_method_get_audio_listener_3d) ( ) const |
| [Camera2D](class_camera2d.md#class_Camera2D) | [get_camera_2d](class_viewport.md#class_Viewport_method_get_camera_2d) ( ) const |
| [Camera3D](class_camera3d.md#class_Camera3D) | [get_camera_3d](class_viewport.md#class_Viewport_method_get_camera_3d) ( ) const |
| [bool](class_bool.md#class_bool) | [get_canvas_cull_mask_bit](class_viewport.md#class_Viewport_method_get_canvas_cull_mask_bit) ( layer: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array)\[[Window](class_window.md#class_Window)\] | [get_embedded_subwindows](class_viewport.md#class_Viewport_method_get_embedded_subwindows) ( ) const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [get_final_transform](class_viewport.md#class_Viewport_method_get_final_transform) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_mouse_position](class_viewport.md#class_Viewport_method_get_mouse_position) ( ) const |
| [float](class_float.md#class_float) | [get_oversampling](class_viewport.md#class_Viewport_method_get_oversampling) ( ) const |
| [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) | [get_positional_shadow_atlas_quadrant_subdiv](class_viewport.md#class_Viewport_method_get_positional_shadow_atlas_quadrant_subdiv) ( quadrant: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_render_info](class_viewport.md#class_Viewport_method_get_render_info) ( type: [RenderInfoType](class_viewport.md#enum_Viewport_RenderInfoType), info: [RenderInfo](class_viewport.md#enum_Viewport_RenderInfo) ) |
| [Transform2D](class_transform2d.md#class_Transform2D) | [get_screen_transform](class_viewport.md#class_Viewport_method_get_screen_transform) ( ) const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [get_stretch_transform](class_viewport.md#class_Viewport_method_get_stretch_transform) ( ) const |
| [ViewportTexture](class_viewporttexture.md#class_ViewportTexture) | [get_texture](class_viewport.md#class_Viewport_method_get_texture) ( ) const |
| [RID](class_rid.md#class_RID) | [get_viewport_rid](class_viewport.md#class_Viewport_method_get_viewport_rid) ( ) const |
| [Rect2](class_rect2.md#class_Rect2) | [get_visible_rect](class_viewport.md#class_Viewport_method_get_visible_rect) ( ) const |
| void | [gui_cancel_drag](class_viewport.md#class_Viewport_method_gui_cancel_drag) ( ) |
| [Variant](class_variant.md#class_Variant) | [gui_get_drag_data](class_viewport.md#class_Viewport_method_gui_get_drag_data) ( ) const |
| [String](class_string.md#class_String) | [gui_get_drag_description](class_viewport.md#class_Viewport_method_gui_get_drag_description) ( ) const |
| [Control](class_control.md#class_Control) | [gui_get_focus_owner](class_viewport.md#class_Viewport_method_gui_get_focus_owner) ( ) const |
| [Control](class_control.md#class_Control) | [gui_get_hovered_control](class_viewport.md#class_Viewport_method_gui_get_hovered_control) ( ) const |
| [bool](class_bool.md#class_bool) | [gui_is_drag_successful](class_viewport.md#class_Viewport_method_gui_is_drag_successful) ( ) const |
| [bool](class_bool.md#class_bool) | [gui_is_dragging](class_viewport.md#class_Viewport_method_gui_is_dragging) ( ) const |
| void | [gui_release_focus](class_viewport.md#class_Viewport_method_gui_release_focus) ( ) |
| void | [gui_set_drag_description](class_viewport.md#class_Viewport_method_gui_set_drag_description) ( description: [String](class_string.md#class_String) ) |
| [bool](class_bool.md#class_bool) | [is_input_handled](class_viewport.md#class_Viewport_method_is_input_handled) ( ) const |
| void | [notify_mouse_entered](class_viewport.md#class_Viewport_method_notify_mouse_entered) ( ) |
| void | [notify_mouse_exited](class_viewport.md#class_Viewport_method_notify_mouse_exited) ( ) |
| void | [push_input](class_viewport.md#class_Viewport_method_push_input) ( event: [InputEvent](class_inputevent.md#class_InputEvent), in_local_coords: [bool](class_bool.md#class_bool) = false ) |
| void | [push_text_input](class_viewport.md#class_Viewport_method_push_text_input) ( text: [String](class_string.md#class_String) ) |
| void | [push_unhandled_input](class_viewport.md#class_Viewport_method_push_unhandled_input) ( event: [InputEvent](class_inputevent.md#class_InputEvent), in_local_coords: [bool](class_bool.md#class_bool) = false ) |
| void | [set_canvas_cull_mask_bit](class_viewport.md#class_Viewport_method_set_canvas_cull_mask_bit) ( layer: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_input_as_handled](class_viewport.md#class_Viewport_method_set_input_as_handled) ( ) |
| void | [set_positional_shadow_atlas_quadrant_subdiv](class_viewport.md#class_Viewport_method_set_positional_shadow_atlas_quadrant_subdiv) ( quadrant: [int](class_int.md#class_int), subdiv: [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) ) |
| void | [update_mouse_cursor_state](class_viewport.md#class_Viewport_method_update_mouse_cursor_state) ( ) |
| void | [warp_mouse](class_viewport.md#class_Viewport_method_warp_mouse) ( position: [Vector2](class_vector2.md#class_Vector2) ) |

---

### Signals

<span id="class_Viewport_signal_gui_focus_changed"></span>

**gui_focus_changed** ( node: [Control](class_control.md#class_Control) ) [🔗](class_viewport.md#class_Viewport_signal_gui_focus_changed)

Emitted when a Control node grabs keyboard focus.

 **Note:** A Control node losing focus doesn't cause this signal to be emitted.

---

<span id="class_Viewport_signal_size_changed"></span>

**size_changed** ( ) [🔗](class_viewport.md#class_Viewport_signal_size_changed)

Emitted when the size of the viewport is changed, whether by resizing of window, or some other means.

---

### Enumerations

<span id="enum_Viewport_PositionalShadowAtlasQuadrantSubdiv"></span>

enum **PositionalShadowAtlasQuadrantSubdiv**: [🔗](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv)

<span id="class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_DISABLED"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **SHADOW_ATLAS_QUADRANT_SUBDIV_DISABLED** = `0`

This quadrant will not be used.

<span id="class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_1"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **SHADOW_ATLAS_QUADRANT_SUBDIV_1** = `1`

This quadrant will only be used by one shadow map.

<span id="class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_4"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **SHADOW_ATLAS_QUADRANT_SUBDIV_4** = `2`

This quadrant will be split in 4 and used by up to 4 shadow maps.

<span id="class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_16"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **SHADOW_ATLAS_QUADRANT_SUBDIV_16** = `3`

This quadrant will be split 16 ways and used by up to 16 shadow maps.

<span id="class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_64"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **SHADOW_ATLAS_QUADRANT_SUBDIV_64** = `4`

This quadrant will be split 64 ways and used by up to 64 shadow maps.

<span id="class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_256"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **SHADOW_ATLAS_QUADRANT_SUBDIV_256** = `5`

This quadrant will be split 256 ways and used by up to 256 shadow maps. Unless the [positional_shadow_atlas_size](class_viewport.md#class_Viewport_property_positional_shadow_atlas_size) is very high, the shadows in this quadrant will be very low resolution.

<span id="class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_1024"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **SHADOW_ATLAS_QUADRANT_SUBDIV_1024** = `6`

This quadrant will be split 1024 ways and used by up to 1024 shadow maps. Unless the [positional_shadow_atlas_size](class_viewport.md#class_Viewport_property_positional_shadow_atlas_size) is very high, the shadows in this quadrant will be very low resolution.

<span id="class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_MAX"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **SHADOW_ATLAS_QUADRANT_SUBDIV_MAX** = `7`

Represents the size of the [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) enum.

---

<span id="enum_Viewport_Scaling3DMode"></span>

enum **Scaling3DMode**: [🔗](class_viewport.md#enum_Viewport_Scaling3DMode)

<span id="class_Viewport_constant_SCALING_3D_MODE_BILINEAR"></span>

[Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) **SCALING_3D_MODE_BILINEAR** = `0`

Use bilinear scaling for the viewport's 3D buffer. The amount of scaling can be set using [scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale). Values less than `1.0` will result in undersampling while values greater than `1.0` will result in supersampling. A value of `1.0` disables scaling.

<span id="class_Viewport_constant_SCALING_3D_MODE_FSR"></span>

[Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) **SCALING_3D_MODE_FSR** = `1`

Use AMD FidelityFX Super Resolution 1.0 upscaling for the viewport's 3D buffer. The amount of scaling can be set using [scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale). Values less than `1.0` will result in the viewport being upscaled using FSR. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` disables scaling.

<span id="class_Viewport_constant_SCALING_3D_MODE_FSR2"></span>

[Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) **SCALING_3D_MODE_FSR2** = `2`

Use AMD FidelityFX Super Resolution 2.2 upscaling for the viewport's 3D buffer. The amount of scaling can be set using [scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale). Values less than `1.0` will result in the viewport being upscaled using FSR2. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` will use FSR2 at native resolution as a TAA solution.

<span id="class_Viewport_constant_SCALING_3D_MODE_METALFX_SPATIAL"></span>

[Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) **SCALING_3D_MODE_METALFX_SPATIAL** = `3`

Use the MetalFX spatial upscaler for the viewport's 3D buffer.

The amount of scaling can be set using [scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale).

Values less than `1.0` will result in the viewport being upscaled using MetalFX. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` disables scaling.

More information: MetalFX.

 **Note:** Only supported when the Metal rendering driver is in use, which limits this scaling mode to macOS and iOS.

<span id="class_Viewport_constant_SCALING_3D_MODE_METALFX_TEMPORAL"></span>

[Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) **SCALING_3D_MODE_METALFX_TEMPORAL** = `4`

Use the MetalFX temporal upscaler for the viewport's 3D buffer.

The amount of scaling can be set using [scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale). To determine the minimum input scale, use the [RenderingDevice.limit_get()](class_renderingdevice.md#class_RenderingDevice_method_limit_get) method with [RenderingDevice.LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE](class_renderingdevice.md#class_RenderingDevice_constant_LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE).

Values less than `1.0` will result in the viewport being upscaled using MetalFX. Values greater than `1.0` are not supported and bilinear downsampling will be used instead. A value of `1.0` will use MetalFX at native resolution as a TAA solution.

More information: MetalFX.

 **Note:** Only supported when the Metal rendering driver is in use, which limits this scaling mode to macOS and iOS.

<span id="class_Viewport_constant_SCALING_3D_MODE_MAX"></span>

[Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) **SCALING_3D_MODE_MAX** = `5`

Represents the size of the [Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) enum.

---

<span id="enum_Viewport_MSAA"></span>

enum **MSAA**: [🔗](class_viewport.md#enum_Viewport_MSAA)

<span id="class_Viewport_constant_MSAA_DISABLED"></span>

[MSAA](class_viewport.md#enum_Viewport_MSAA) **MSAA_DISABLED** = `0`

Multisample antialiasing mode disabled. This is the default value, and is also the fastest setting.

<span id="class_Viewport_constant_MSAA_2X"></span>

[MSAA](class_viewport.md#enum_Viewport_MSAA) **MSAA_2X** = `1`

Use 2× Multisample Antialiasing. This has a moderate performance cost. It helps reduce aliasing noticeably, but 4× MSAA still looks substantially better.

<span id="class_Viewport_constant_MSAA_4X"></span>

[MSAA](class_viewport.md#enum_Viewport_MSAA) **MSAA_4X** = `2`

Use 4× Multisample Antialiasing. This has a significant performance cost, and is generally a good compromise between performance and quality.

<span id="class_Viewport_constant_MSAA_8X"></span>

[MSAA](class_viewport.md#enum_Viewport_MSAA) **MSAA_8X** = `3`

Use 8× Multisample Antialiasing. This has a very high performance cost. The difference between 4× and 8× MSAA may not always be visible in real gameplay conditions. Likely unsupported on low-end and older hardware.

<span id="class_Viewport_constant_MSAA_MAX"></span>

[MSAA](class_viewport.md#enum_Viewport_MSAA) **MSAA_MAX** = `4`

Represents the size of the [MSAA](class_viewport.md#enum_Viewport_MSAA) enum.

---

<span id="enum_Viewport_AnisotropicFiltering"></span>

enum **AnisotropicFiltering**: [🔗](class_viewport.md#enum_Viewport_AnisotropicFiltering)

<span id="class_Viewport_constant_ANISOTROPY_DISABLED"></span>

[AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) **ANISOTROPY_DISABLED** = `0`

Anisotropic filtering is disabled.

<span id="class_Viewport_constant_ANISOTROPY_2X"></span>

[AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) **ANISOTROPY_2X** = `1`

Use 2× anisotropic filtering.

<span id="class_Viewport_constant_ANISOTROPY_4X"></span>

[AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) **ANISOTROPY_4X** = `2`

Use 4× anisotropic filtering. This is the default value.

<span id="class_Viewport_constant_ANISOTROPY_8X"></span>

[AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) **ANISOTROPY_8X** = `3`

Use 8× anisotropic filtering.

<span id="class_Viewport_constant_ANISOTROPY_16X"></span>

[AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) **ANISOTROPY_16X** = `4`

Use 16× anisotropic filtering.

<span id="class_Viewport_constant_ANISOTROPY_MAX"></span>

[AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) **ANISOTROPY_MAX** = `5`

Represents the size of the [AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) enum.

---

<span id="enum_Viewport_ScreenSpaceAA"></span>

enum **ScreenSpaceAA**: [🔗](class_viewport.md#enum_Viewport_ScreenSpaceAA)

<span id="class_Viewport_constant_SCREEN_SPACE_AA_DISABLED"></span>

[ScreenSpaceAA](class_viewport.md#enum_Viewport_ScreenSpaceAA) **SCREEN_SPACE_AA_DISABLED** = `0`

Do not perform any antialiasing in the full screen post-process.

<span id="class_Viewport_constant_SCREEN_SPACE_AA_FXAA"></span>

[ScreenSpaceAA](class_viewport.md#enum_Viewport_ScreenSpaceAA) **SCREEN_SPACE_AA_FXAA** = `1`

Use fast approximate antialiasing. FXAA is a popular screen-space antialiasing method, which is fast but will make the image look blurry, especially at lower resolutions. It can still work relatively well at large resolutions such as 1440p and 4K.

<span id="class_Viewport_constant_SCREEN_SPACE_AA_SMAA"></span>

[ScreenSpaceAA](class_viewport.md#enum_Viewport_ScreenSpaceAA) **SCREEN_SPACE_AA_SMAA** = `2`

Use subpixel morphological antialiasing. SMAA may produce clearer results than FXAA, but at a slightly higher performance cost.

<span id="class_Viewport_constant_SCREEN_SPACE_AA_MAX"></span>

[ScreenSpaceAA](class_viewport.md#enum_Viewport_ScreenSpaceAA) **SCREEN_SPACE_AA_MAX** = `3`

Represents the size of the [ScreenSpaceAA](class_viewport.md#enum_Viewport_ScreenSpaceAA) enum.

---

<span id="enum_Viewport_RenderInfo"></span>

enum **RenderInfo**: [🔗](class_viewport.md#enum_Viewport_RenderInfo)

<span id="class_Viewport_constant_RENDER_INFO_OBJECTS_IN_FRAME"></span>

[RenderInfo](class_viewport.md#enum_Viewport_RenderInfo) **RENDER_INFO_OBJECTS_IN_FRAME** = `0`

Amount of objects in frame.

<span id="class_Viewport_constant_RENDER_INFO_PRIMITIVES_IN_FRAME"></span>

[RenderInfo](class_viewport.md#enum_Viewport_RenderInfo) **RENDER_INFO_PRIMITIVES_IN_FRAME** = `1`

Amount of vertices in frame.

<span id="class_Viewport_constant_RENDER_INFO_DRAW_CALLS_IN_FRAME"></span>

[RenderInfo](class_viewport.md#enum_Viewport_RenderInfo) **RENDER_INFO_DRAW_CALLS_IN_FRAME** = `2`

Amount of draw calls in frame.

<span id="class_Viewport_constant_RENDER_INFO_MAX"></span>

[RenderInfo](class_viewport.md#enum_Viewport_RenderInfo) **RENDER_INFO_MAX** = `3`

Represents the size of the [RenderInfo](class_viewport.md#enum_Viewport_RenderInfo) enum.

---

<span id="enum_Viewport_RenderInfoType"></span>

enum **RenderInfoType**: [🔗](class_viewport.md#enum_Viewport_RenderInfoType)

<span id="class_Viewport_constant_RENDER_INFO_TYPE_VISIBLE"></span>

[RenderInfoType](class_viewport.md#enum_Viewport_RenderInfoType) **RENDER_INFO_TYPE_VISIBLE** = `0`

Visible render pass (excluding shadows).

<span id="class_Viewport_constant_RENDER_INFO_TYPE_SHADOW"></span>

[RenderInfoType](class_viewport.md#enum_Viewport_RenderInfoType) **RENDER_INFO_TYPE_SHADOW** = `1`

Shadow render pass. Objects will be rendered several times depending on the number of amounts of lights with shadows and the number of directional shadow splits.

<span id="class_Viewport_constant_RENDER_INFO_TYPE_CANVAS"></span>

[RenderInfoType](class_viewport.md#enum_Viewport_RenderInfoType) **RENDER_INFO_TYPE_CANVAS** = `2`

Canvas item rendering. This includes all 2D rendering.

<span id="class_Viewport_constant_RENDER_INFO_TYPE_MAX"></span>

[RenderInfoType](class_viewport.md#enum_Viewport_RenderInfoType) **RENDER_INFO_TYPE_MAX** = `3`

Represents the size of the [RenderInfoType](class_viewport.md#enum_Viewport_RenderInfoType) enum.

---

<span id="enum_Viewport_DebugDraw"></span>

enum **DebugDraw**: [🔗](class_viewport.md#enum_Viewport_DebugDraw)

<span id="class_Viewport_constant_DEBUG_DRAW_DISABLED"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_DISABLED** = `0`

Objects are displayed normally.

<span id="class_Viewport_constant_DEBUG_DRAW_UNSHADED"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_UNSHADED** = `1`

Objects are displayed without light information.

<span id="class_Viewport_constant_DEBUG_DRAW_LIGHTING"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_LIGHTING** = `2`

Objects are displayed without textures and only with lighting information.

 **Note:** When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.

<span id="class_Viewport_constant_DEBUG_DRAW_OVERDRAW"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_OVERDRAW** = `3`

Objects are displayed semi-transparent with additive blending so you can see where they are drawing over top of one another. A higher overdraw means you are wasting performance on drawing pixels that are being hidden behind others.

 **Note:** When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.

<span id="class_Viewport_constant_DEBUG_DRAW_WIREFRAME"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_WIREFRAME** = `4`

Objects are displayed as wireframe models.

 **Note:** [RenderingServer.set_debug_generate_wireframes()](class_renderingserver.md#class_RenderingServer_method_set_debug_generate_wireframes) must be called before loading any meshes for wireframes to be visible when using the Compatibility renderer.

<span id="class_Viewport_constant_DEBUG_DRAW_NORMAL_BUFFER"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_NORMAL_BUFFER** = `5`

Objects are displayed without lighting information and their textures replaced by normal mapping.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_VOXEL_GI_ALBEDO"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_VOXEL_GI_ALBEDO** = `6`

Objects are displayed with only the albedo value from [VoxelGI](class_voxelgi.md#class_VoxelGI) s. Requires at least one visible [VoxelGI](class_voxelgi.md#class_VoxelGI) node that has been baked to have a visible effect.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_VOXEL_GI_LIGHTING"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_VOXEL_GI_LIGHTING** = `7`

Objects are displayed with only the lighting value from [VoxelGI](class_voxelgi.md#class_VoxelGI) s. Requires at least one visible [VoxelGI](class_voxelgi.md#class_VoxelGI) node that has been baked to have a visible effect.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_VOXEL_GI_EMISSION"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_VOXEL_GI_EMISSION** = `8`

Objects are displayed with only the emission color from [VoxelGI](class_voxelgi.md#class_VoxelGI) s. Requires at least one visible [VoxelGI](class_voxelgi.md#class_VoxelGI) node that has been baked to have a visible effect.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_SHADOW_ATLAS"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_SHADOW_ATLAS** = `9`

Draws the shadow atlas that stores shadows from [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) s and [SpotLight3D](class_spotlight3d.md#class_SpotLight3D) s in the upper left quadrant of the **Viewport**.

<span id="class_Viewport_constant_DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS** = `10`

Draws the shadow atlas that stores shadows from [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D) s in the upper left quadrant of the **Viewport**.

<span id="class_Viewport_constant_DEBUG_DRAW_SCENE_LUMINANCE"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_SCENE_LUMINANCE** = `11`

Draws the scene luminance buffer (if available) in the upper left quadrant of the **Viewport**.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

<span id="class_Viewport_constant_DEBUG_DRAW_SSAO"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_SSAO** = `12`

Draws the screen-space ambient occlusion texture instead of the scene so that you can clearly see how it is affecting objects. In order for this display mode to work, you must have [Environment.ssao_enabled](class_environment.md#class_Environment_property_ssao_enabled) set in your [WorldEnvironment](class_worldenvironment.md#class_WorldEnvironment).

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_SSIL"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_SSIL** = `13`

Draws the screen-space indirect lighting texture instead of the scene so that you can clearly see how it is affecting objects. In order for this display mode to work, you must have [Environment.ssil_enabled](class_environment.md#class_Environment_property_ssil_enabled) set in your [WorldEnvironment](class_worldenvironment.md#class_WorldEnvironment).

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_PSSM_SPLITS"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_PSSM_SPLITS** = `14`

Colors each PSSM split for the [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D) s in the scene a different color so you can see where the splits are. In order (from closest to furthest from the camera), they are colored red, green, blue, and yellow.

 **Note:** When using this debug draw mode, custom shaders are ignored since all materials in the scene temporarily use a debug material. This means the result from custom shader functions (such as vertex displacement) won't be visible anymore when using this debug draw mode.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

<span id="class_Viewport_constant_DEBUG_DRAW_DECAL_ATLAS"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_DECAL_ATLAS** = `15`

Draws the decal atlas used by [Decal](class_decal.md#class_Decal) s and light projector textures in the upper left quadrant of the **Viewport**.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

<span id="class_Viewport_constant_DEBUG_DRAW_SDFGI"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_SDFGI** = `16`

Draws the cascades used to render signed distance field global illumination (SDFGI).

Does nothing if the current environment's [Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled) is `false`.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_SDFGI_PROBES"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_SDFGI_PROBES** = `17`

Draws the probes used for signed distance field global illumination (SDFGI).

When in the editor, left-clicking a probe will display additional bright dots that show its occlusion information. A white dot means the light is not occluded at all at the dot's position, while a red dot means the light is fully occluded. Intermediate values are possible.

Does nothing if the current environment's [Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled) is `false`.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_GI_BUFFER"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_GI_BUFFER** = `18`

Draws the buffer used for global illumination from [VoxelGI](class_voxelgi.md#class_VoxelGI) or SDFGI. Requires [VoxelGI](class_voxelgi.md#class_VoxelGI) (at least one visible baked VoxelGI node) or SDFGI ([Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled)) to be enabled to have a visible effect.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_DISABLE_LOD"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_DISABLE_LOD** = `19`

Draws all of the objects at their highest polycount regardless of their distance from the camera. No low level of detail (LOD) is applied.

<span id="class_Viewport_constant_DEBUG_DRAW_CLUSTER_OMNI_LIGHTS"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_CLUSTER_OMNI_LIGHTS** = `20`

Draws the cluster used by [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) nodes to optimize light rendering.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_CLUSTER_SPOT_LIGHTS"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_CLUSTER_SPOT_LIGHTS** = `21`

Draws the cluster used by [SpotLight3D](class_spotlight3d.md#class_SpotLight3D) nodes to optimize light rendering.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_CLUSTER_DECALS"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_CLUSTER_DECALS** = `22`

Draws the cluster used by [Decal](class_decal.md#class_Decal) nodes to optimize decal rendering.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_CLUSTER_REFLECTION_PROBES"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_CLUSTER_REFLECTION_PROBES** = `23`

Draws the cluster used by [ReflectionProbe](class_reflectionprobe.md#class_ReflectionProbe) nodes to optimize reflection probes.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_OCCLUDERS"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_OCCLUDERS** = `24`

Draws the buffer used for occlusion culling.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

<span id="class_Viewport_constant_DEBUG_DRAW_MOTION_VECTORS"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_MOTION_VECTORS** = `25`

Draws vector lines over the viewport to indicate the movement of pixels between frames.

 **Note:** Only supported when using the Forward+ rendering method.

<span id="class_Viewport_constant_DEBUG_DRAW_INTERNAL_BUFFER"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **DEBUG_DRAW_INTERNAL_BUFFER** = `26`

Draws the internal resolution buffer of the scene in linear colorspace before tonemapping or post-processing is applied.

 **Note:** Only supported when using the Forward+ or Mobile rendering methods.

---

<span id="enum_Viewport_DefaultCanvasItemTextureFilter"></span>

enum **DefaultCanvasItemTextureFilter**: [🔗](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter)

<span id="class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST"></span>

[DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST** = `0`

The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).

<span id="class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR"></span>

[DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR** = `1`

The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).

<span id="class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS"></span>

[DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS** = `2`

The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`). This makes the texture look smooth from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class_Camera2D) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<span id="class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS"></span>

[DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS** = `3`

The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`). This makes the texture look pixelated from up close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale (e.g. due to [Camera2D](class_camera2d.md#class_Camera2D) zoom or sprite scaling), as mipmaps are important to smooth out pixels that are smaller than on-screen pixels.

<span id="class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_MAX"></span>

[DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_MAX** = `4`

Represents the size of the [DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) enum.

---

<span id="enum_Viewport_DefaultCanvasItemTextureRepeat"></span>

enum **DefaultCanvasItemTextureRepeat**: [🔗](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat)

<span id="class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_DISABLED"></span>

[DefaultCanvasItemTextureRepeat](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat) **DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_DISABLED** = `0`

Disables textures repeating. Instead, when reading UVs outside the 0-1 range, the value will be clamped to the edge of the texture, resulting in a stretched out look at the borders of the texture.

<span id="class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_ENABLED"></span>

[DefaultCanvasItemTextureRepeat](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat) **DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_ENABLED** = `1`

Enables the texture to repeat when UV coordinates are outside the 0-1 range. If using one of the linear filtering modes, this can result in artifacts at the edges of a texture when the sampler filters across the edges of the texture.

<span id="class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MIRROR"></span>

[DefaultCanvasItemTextureRepeat](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat) **DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MIRROR** = `2`

Flip the texture when repeating so that the edge lines up instead of abruptly changing.

<span id="class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MAX"></span>

[DefaultCanvasItemTextureRepeat](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat) **DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MAX** = `3`

Represents the size of the [DefaultCanvasItemTextureRepeat](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat) enum.

---

<span id="enum_Viewport_SDFOversize"></span>

enum **SDFOversize**: [🔗](class_viewport.md#enum_Viewport_SDFOversize)

<span id="class_Viewport_constant_SDF_OVERSIZE_100_PERCENT"></span>

[SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) **SDF_OVERSIZE_100_PERCENT** = `0`

The signed distance field only covers the viewport's own rectangle.

<span id="class_Viewport_constant_SDF_OVERSIZE_120_PERCENT"></span>

[SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) **SDF_OVERSIZE_120_PERCENT** = `1`

The signed distance field is expanded to cover 20% of the viewport's size around the borders.

<span id="class_Viewport_constant_SDF_OVERSIZE_150_PERCENT"></span>

[SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) **SDF_OVERSIZE_150_PERCENT** = `2`

The signed distance field is expanded to cover 50% of the viewport's size around the borders.

<span id="class_Viewport_constant_SDF_OVERSIZE_200_PERCENT"></span>

[SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) **SDF_OVERSIZE_200_PERCENT** = `3`

The signed distance field is expanded to cover 100% (double) of the viewport's size around the borders.

<span id="class_Viewport_constant_SDF_OVERSIZE_MAX"></span>

[SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) **SDF_OVERSIZE_MAX** = `4`

Represents the size of the [SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) enum.

---

<span id="enum_Viewport_SDFScale"></span>

enum **SDFScale**: [🔗](class_viewport.md#enum_Viewport_SDFScale)

<span id="class_Viewport_constant_SDF_SCALE_100_PERCENT"></span>

[SDFScale](class_viewport.md#enum_Viewport_SDFScale) **SDF_SCALE_100_PERCENT** = `0`

The signed distance field is rendered at full resolution.

<span id="class_Viewport_constant_SDF_SCALE_50_PERCENT"></span>

[SDFScale](class_viewport.md#enum_Viewport_SDFScale) **SDF_SCALE_50_PERCENT** = `1`

The signed distance field is rendered at half the resolution of this viewport.

<span id="class_Viewport_constant_SDF_SCALE_25_PERCENT"></span>

[SDFScale](class_viewport.md#enum_Viewport_SDFScale) **SDF_SCALE_25_PERCENT** = `2`

The signed distance field is rendered at a quarter the resolution of this viewport.

<span id="class_Viewport_constant_SDF_SCALE_MAX"></span>

[SDFScale](class_viewport.md#enum_Viewport_SDFScale) **SDF_SCALE_MAX** = `3`

Represents the size of the [SDFScale](class_viewport.md#enum_Viewport_SDFScale) enum.

---

<span id="enum_Viewport_VRSMode"></span>

enum **VRSMode**: [🔗](class_viewport.md#enum_Viewport_VRSMode)

<span id="class_Viewport_constant_VRS_DISABLED"></span>

[VRSMode](class_viewport.md#enum_Viewport_VRSMode) **VRS_DISABLED** = `0`

Variable Rate Shading is disabled.

<span id="class_Viewport_constant_VRS_TEXTURE"></span>

[VRSMode](class_viewport.md#enum_Viewport_VRSMode) **VRS_TEXTURE** = `1`

Variable Rate Shading uses a texture. Note, for stereoscopic use a texture atlas with a texture for each view.

<span id="class_Viewport_constant_VRS_XR"></span>

[VRSMode](class_viewport.md#enum_Viewport_VRSMode) **VRS_XR** = `2`

Variable Rate Shading's texture is supplied by the primary [XRInterface](class_xrinterface.md#class_XRInterface).

<span id="class_Viewport_constant_VRS_MAX"></span>

[VRSMode](class_viewport.md#enum_Viewport_VRSMode) **VRS_MAX** = `3`

Represents the size of the [VRSMode](class_viewport.md#enum_Viewport_VRSMode) enum.

---

<span id="enum_Viewport_VRSUpdateMode"></span>

enum **VRSUpdateMode**: [🔗](class_viewport.md#enum_Viewport_VRSUpdateMode)

<span id="class_Viewport_constant_VRS_UPDATE_DISABLED"></span>

[VRSUpdateMode](class_viewport.md#enum_Viewport_VRSUpdateMode) **VRS_UPDATE_DISABLED** = `0`

The input texture for variable rate shading will not be processed.

<span id="class_Viewport_constant_VRS_UPDATE_ONCE"></span>

[VRSUpdateMode](class_viewport.md#enum_Viewport_VRSUpdateMode) **VRS_UPDATE_ONCE** = `1`

The input texture for variable rate shading will be processed once.

<span id="class_Viewport_constant_VRS_UPDATE_ALWAYS"></span>

[VRSUpdateMode](class_viewport.md#enum_Viewport_VRSUpdateMode) **VRS_UPDATE_ALWAYS** = `2`

The input texture for variable rate shading will be processed each frame.

<span id="class_Viewport_constant_VRS_UPDATE_MAX"></span>

[VRSUpdateMode](class_viewport.md#enum_Viewport_VRSUpdateMode) **VRS_UPDATE_MAX** = `3`

Represents the size of the [VRSUpdateMode](class_viewport.md#enum_Viewport_VRSUpdateMode) enum.

---

### Property Descriptions

<span id="class_Viewport_property_anisotropic_filtering_level"></span>

[AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) **anisotropic_filtering_level** = `2` [🔗](class_viewport.md#class_Viewport_property_anisotropic_filtering_level)

- void **set_anisotropic_filtering_level** ( value: [AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) )
- [AnisotropicFiltering](class_viewport.md#enum_Viewport_AnisotropicFiltering) **get_anisotropic_filtering_level** ( )

Sets the maximum number of samples to take when using anisotropic filtering on textures (as a power of two). A higher sample count will result in sharper textures at oblique angles, but is more expensive to compute. A value of `0` forcibly disables anisotropic filtering, even on materials where it is enabled.

The anisotropic filtering level also affects decals and light projectors if they are configured to use anisotropic filtering. See ProjectSettings.rendering/textures/decals/filter and ProjectSettings.rendering/textures/light_projectors/filter.

 **Note:** In 3D, for this setting to have an effect, set [BaseMaterial3D.texture_filter](class_basematerial3d.md#class_BaseMaterial3D_property_texture_filter) to [BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC](class_basematerial3d.md#class_BaseMaterial3D_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC) or [BaseMaterial3D.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC](class_basematerial3d.md#class_BaseMaterial3D_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC) on materials.

 **Note:** In 2D, for this setting to have an effect, set [CanvasItem.texture_filter](class_canvasitem.md#class_CanvasItem_property_texture_filter) to [CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC](class_canvasitem.md#class_CanvasItem_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC) or [CanvasItem.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC](class_canvasitem.md#class_CanvasItem_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC) on the [CanvasItem](class_canvasitem.md#class_CanvasItem) node displaying the texture (or in [CanvasTexture](class_canvastexture.md#class_CanvasTexture)). However, anisotropic filtering is rarely useful in 2D, so only enable it for textures in 2D if it makes a meaningful visual difference.

---

<span id="class_Viewport_property_audio_listener_enable_2d"></span>

[bool](class_bool.md#class_bool) **audio_listener_enable_2d** = `false` [🔗](class_viewport.md#class_Viewport_property_audio_listener_enable_2d)

- void **set_as_audio_listener_2d** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_audio_listener_2d** ( )

If `true`, the viewport will process 2D audio streams.

---

<span id="class_Viewport_property_audio_listener_enable_3d"></span>

[bool](class_bool.md#class_bool) **audio_listener_enable_3d** = `false` [🔗](class_viewport.md#class_Viewport_property_audio_listener_enable_3d)

- void **set_as_audio_listener_3d** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_audio_listener_3d** ( )

If `true`, the viewport will process 3D audio streams.

---

<span id="class_Viewport_property_canvas_cull_mask"></span>

[int](class_int.md#class_int) **canvas_cull_mask** = `4294967295` [🔗](class_viewport.md#class_Viewport_property_canvas_cull_mask)

- void **set_canvas_cull_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_canvas_cull_mask** ( )

The rendering layers in which this **Viewport** renders [CanvasItem](class_canvasitem.md#class_CanvasItem) nodes.

 **Note:** A [CanvasItem](class_canvasitem.md#class_CanvasItem) does not inherit its parents' visibility layers. See [CanvasItem.visibility_layer](class_canvasitem.md#class_CanvasItem_property_visibility_layer)'s description for details.

---

<span id="class_Viewport_property_canvas_item_default_texture_filter"></span>

[DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) **canvas_item_default_texture_filter** = `1` [🔗](class_viewport.md#class_Viewport_property_canvas_item_default_texture_filter)

- void **set_default_canvas_item_texture_filter** ( value: [DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) )
- [DefaultCanvasItemTextureFilter](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureFilter) **get_default_canvas_item_texture_filter** ( )

The default filter mode used by [CanvasItem](class_canvasitem.md#class_CanvasItem) nodes in this viewport.

---

<span id="class_Viewport_property_canvas_item_default_texture_repeat"></span>

[DefaultCanvasItemTextureRepeat](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat) **canvas_item_default_texture_repeat** = `0` [🔗](class_viewport.md#class_Viewport_property_canvas_item_default_texture_repeat)

- void **set_default_canvas_item_texture_repeat** ( value: [DefaultCanvasItemTextureRepeat](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat) )
- [DefaultCanvasItemTextureRepeat](class_viewport.md#enum_Viewport_DefaultCanvasItemTextureRepeat) **get_default_canvas_item_texture_repeat** ( )

The default repeat mode used by [CanvasItem](class_canvasitem.md#class_CanvasItem) nodes in this viewport.

---

<span id="class_Viewport_property_canvas_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **canvas_transform** [🔗](class_viewport.md#class_Viewport_property_canvas_transform)

- void **set_canvas_transform** ( value: [Transform2D](class_transform2d.md#class_Transform2D) )
- [Transform2D](class_transform2d.md#class_Transform2D) **get_canvas_transform** ( )

The canvas transform of the viewport, useful for changing the on-screen positions of all child [CanvasItem](class_canvasitem.md#class_CanvasItem) s. This is relative to the global canvas transform of the viewport.

---

<span id="class_Viewport_property_debug_draw"></span>

[DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **debug_draw** = `0` [🔗](class_viewport.md#class_Viewport_property_debug_draw)

- void **set_debug_draw** ( value: [DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) )
- [DebugDraw](class_viewport.md#enum_Viewport_DebugDraw) **get_debug_draw** ( )

The overlay mode for test rendered geometry in debug purposes.

---

<span id="class_Viewport_property_disable_3d"></span>

[bool](class_bool.md#class_bool) **disable_3d** = `false` [🔗](class_viewport.md#class_Viewport_property_disable_3d)

- void **set_disable_3d** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_3d_disabled** ( )

Disable 3D rendering (but keep 2D rendering).

---

<span id="class_Viewport_property_fsr_sharpness"></span>

[float](class_float.md#class_float) **fsr_sharpness** = `0.2` [🔗](class_viewport.md#class_Viewport_property_fsr_sharpness)

- void **set_fsr_sharpness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fsr_sharpness** ( )

Determines how sharp the upscaled image will be when using the FSR upscaling mode. Sharpness halves with every whole number. Values go from 0.0 (sharpest) to 2.0. Values above 2.0 won't make a visible difference.

To control this property on the root viewport, set the ProjectSettings.rendering/scaling_3d/fsr_sharpness project setting.

---

<span id="class_Viewport_property_global_canvas_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **global_canvas_transform** [🔗](class_viewport.md#class_Viewport_property_global_canvas_transform)

- void **set_global_canvas_transform** ( value: [Transform2D](class_transform2d.md#class_Transform2D) )
- [Transform2D](class_transform2d.md#class_Transform2D) **get_global_canvas_transform** ( )

The global canvas transform of the viewport. The canvas transform is relative to this.

---

<span id="class_Viewport_property_gui_disable_input"></span>

[bool](class_bool.md#class_bool) **gui_disable_input** = `false` [🔗](class_viewport.md#class_Viewport_property_gui_disable_input)

- void **set_disable_input** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_input_disabled** ( )

If `true`, the viewport will not receive input events.

---

<span id="class_Viewport_property_gui_drag_threshold"></span>

[int](class_int.md#class_int) **gui_drag_threshold** = `10` [🔗](class_viewport.md#class_Viewport_property_gui_drag_threshold)

- void **set_drag_threshold** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_drag_threshold** ( )

The minimum distance the mouse cursor must move while pressed before a drag operation begins.

---

<span id="class_Viewport_property_gui_embed_subwindows"></span>

[bool](class_bool.md#class_bool) **gui_embed_subwindows** = `false` [🔗](class_viewport.md#class_Viewport_property_gui_embed_subwindows)

- void **set_embedding_subwindows** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_embedding_subwindows** ( )

If `true`, sub-windows (popups and dialogs) will be embedded inside application window as control-like nodes. If `false`, they will appear as separate windows handled by the operating system.

---

<span id="class_Viewport_property_gui_snap_controls_to_pixels"></span>

[bool](class_bool.md#class_bool) **gui_snap_controls_to_pixels** = `true` [🔗](class_viewport.md#class_Viewport_property_gui_snap_controls_to_pixels)

- void **set_snap_controls_to_pixels** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_snap_controls_to_pixels_enabled** ( )

If `true`, the GUI controls on the viewport will lay pixel perfectly.

---

<span id="class_Viewport_property_handle_input_locally"></span>

[bool](class_bool.md#class_bool) **handle_input_locally** = `true` [🔗](class_viewport.md#class_Viewport_property_handle_input_locally)

- void **set_handle_input_locally** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_handling_input_locally** ( )

If `true`, this viewport will mark incoming input events as handled by itself. If `false`, this is instead done by the first parent viewport that is set to handle input locally.

A [SubViewportContainer](class_subviewportcontainer.md#class_SubViewportContainer) will automatically set this property to `false` for the **Viewport** contained inside of it.

See also [set_input_as_handled()](class_viewport.md#class_Viewport_method_set_input_as_handled) and [is_input_handled()](class_viewport.md#class_Viewport_method_is_input_handled).

---

<span id="class_Viewport_property_mesh_lod_threshold"></span>

[float](class_float.md#class_float) **mesh_lod_threshold** = `1.0` [🔗](class_viewport.md#class_Viewport_property_mesh_lod_threshold)

- void **set_mesh_lod_threshold** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_mesh_lod_threshold** ( )

The automatic LOD bias to use for meshes rendered within the **Viewport** (this is analogous to [ReflectionProbe.mesh_lod_threshold](class_reflectionprobe.md#class_ReflectionProbe_property_mesh_lod_threshold)). Higher values will use less detailed versions of meshes that have LOD variations generated. If set to `0.0`, automatic LOD is disabled. Increase [mesh_lod_threshold](class_viewport.md#class_Viewport_property_mesh_lod_threshold) to improve performance at the cost of geometry detail.

To control this property on the root viewport, set the ProjectSettings.rendering/mesh_lod/lod_change/threshold_pixels project setting.

 **Note:** [mesh_lod_threshold](class_viewport.md#class_Viewport_property_mesh_lod_threshold) does not affect [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) visibility ranges (also known as "manual" LOD or hierarchical LOD).

---

<span id="class_Viewport_property_msaa_2d"></span>

[MSAA](class_viewport.md#enum_Viewport_MSAA) **msaa_2d** = `0` [🔗](class_viewport.md#class_Viewport_property_msaa_2d)

- void **set_msaa_2d** ( value: [MSAA](class_viewport.md#enum_Viewport_MSAA) )
- [MSAA](class_viewport.md#enum_Viewport_MSAA) **get_msaa_2d** ( )

The multisample antialiasing mode for 2D/Canvas rendering. A higher number results in smoother edges at the cost of significantly worse performance. A value of [MSAA_2X](class_viewport.md#class_Viewport_constant_MSAA_2X) or [MSAA_4X](class_viewport.md#class_Viewport_constant_MSAA_4X) is best unless targeting very high-end systems. This has no effect on shader-induced aliasing or texture aliasing.

See also ProjectSettings.rendering/anti_aliasing/quality/msaa_2d and [RenderingServer.viewport_set_msaa_2d()](class_renderingserver.md#class_RenderingServer_method_viewport_set_msaa_2d).

---

<span id="class_Viewport_property_msaa_3d"></span>

[MSAA](class_viewport.md#enum_Viewport_MSAA) **msaa_3d** = `0` [🔗](class_viewport.md#class_Viewport_property_msaa_3d)

- void **set_msaa_3d** ( value: [MSAA](class_viewport.md#enum_Viewport_MSAA) )
- [MSAA](class_viewport.md#enum_Viewport_MSAA) **get_msaa_3d** ( )

The multisample antialiasing mode for 3D rendering. A higher number results in smoother edges at the cost of significantly worse performance. A value of [MSAA_2X](class_viewport.md#class_Viewport_constant_MSAA_2X) or [MSAA_4X](class_viewport.md#class_Viewport_constant_MSAA_4X) is best unless targeting very high-end systems. See also bilinear scaling 3D [scaling_3d_mode](class_viewport.md#class_Viewport_property_scaling_3d_mode) for supersampling, which provides higher quality but is much more expensive. This has no effect on shader-induced aliasing or texture aliasing.

See also ProjectSettings.rendering/anti_aliasing/quality/msaa_3d and [RenderingServer.viewport_set_msaa_3d()](class_renderingserver.md#class_RenderingServer_method_viewport_set_msaa_3d).

---

<span id="class_Viewport_property_oversampling"></span>

[bool](class_bool.md#class_bool) **oversampling** = `true` [🔗](class_viewport.md#class_Viewport_property_oversampling)

- void **set_use_oversampling** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_oversampling** ( )

If `true` and one of the following conditions are true: [SubViewport.size_2d_override_stretch](class_subviewport.md#class_SubViewport_property_size_2d_override_stretch) and [SubViewport.size_2d_override](class_subviewport.md#class_SubViewport_property_size_2d_override) are set, [Window.content_scale_factor](class_window.md#class_Window_property_content_scale_factor) is set and scaling is enabled, [oversampling_override](class_viewport.md#class_Viewport_property_oversampling_override) is set, font and [DPITexture](class_dpitexture.md#class_DPITexture) oversampling are enabled.

---

<span id="class_Viewport_property_oversampling_override"></span>

[float](class_float.md#class_float) **oversampling_override** = `0.0` [🔗](class_viewport.md#class_Viewport_property_oversampling_override)

- void **set_oversampling_override** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_oversampling_override** ( )

If greater than zero, this value is used as the font oversampling factor, otherwise oversampling is equal to viewport scale.

---

<span id="class_Viewport_property_own_world_3d"></span>

[bool](class_bool.md#class_bool) **own_world_3d** = `false` [🔗](class_viewport.md#class_Viewport_property_own_world_3d)

- void **set_use_own_world_3d** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_own_world_3d** ( )

If `true`, the viewport will use a unique copy of the [World3D](class_world3d.md#class_World3D) defined in [world_3d](class_viewport.md#class_Viewport_property_world_3d).

---

<span id="class_Viewport_property_physics_object_picking"></span>

[bool](class_bool.md#class_bool) **physics_object_picking** = `false` [🔗](class_viewport.md#class_Viewport_property_physics_object_picking)

- void **set_physics_object_picking** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_physics_object_picking** ( )

If `true`, the objects rendered by viewport become subjects of mouse picking process.

 **Note:** The number of simultaneously pickable objects is limited to 64 and they are selected in a non-deterministic order, which can be different in each picking process.

---

<span id="class_Viewport_property_physics_object_picking_first_only"></span>

[bool](class_bool.md#class_bool) **physics_object_picking_first_only** = `false` [🔗](class_viewport.md#class_Viewport_property_physics_object_picking_first_only)

- void **set_physics_object_picking_first_only** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_physics_object_picking_first_only** ( )

If `true`, the input_event signal will only be sent to one physics object in the mouse picking process. If you want to get the top object only, you must also enable [physics_object_picking_sort](class_viewport.md#class_Viewport_property_physics_object_picking_sort).

If `false`, an input_event signal will be sent to all physics objects in the mouse picking process.

This applies to 2D CanvasItem object picking only.

---

<span id="class_Viewport_property_physics_object_picking_sort"></span>

[bool](class_bool.md#class_bool) **physics_object_picking_sort** = `false` [🔗](class_viewport.md#class_Viewport_property_physics_object_picking_sort)

- void **set_physics_object_picking_sort** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_physics_object_picking_sort** ( )

If `true`, objects receive mouse picking events sorted primarily by their [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) and secondarily by their position in the scene tree. If `false`, the order is undetermined.

 **Note:** This setting is disabled by default because of its potential expensive computational cost.

 **Note:** Sorting happens after selecting the pickable objects. Because of the limitation of 64 simultaneously pickable objects, it is not guaranteed that the object with the highest [CanvasItem.z_index](class_canvasitem.md#class_CanvasItem_property_z_index) receives the picking event.

---

<span id="class_Viewport_property_positional_shadow_atlas_16_bits"></span>

[bool](class_bool.md#class_bool) **positional_shadow_atlas_16_bits** = `true` [🔗](class_viewport.md#class_Viewport_property_positional_shadow_atlas_16_bits)

- void **set_positional_shadow_atlas_16_bits** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_positional_shadow_atlas_16_bits** ( )

Use 16 bits for the omni/spot shadow depth map. Enabling this results in shadows having less precision and may result in shadow acne, but can lead to performance improvements on some devices.

---

<span id="class_Viewport_property_positional_shadow_atlas_quad_0"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **positional_shadow_atlas_quad_0** = `2` [🔗](class_viewport.md#class_Viewport_property_positional_shadow_atlas_quad_0)

- void **set_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int), subdiv: [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) )
- [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **get_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int) ) *const*

The subdivision amount of the first quadrant on the shadow atlas.

---

<span id="class_Viewport_property_positional_shadow_atlas_quad_1"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **positional_shadow_atlas_quad_1** = `2` [🔗](class_viewport.md#class_Viewport_property_positional_shadow_atlas_quad_1)

- void **set_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int), subdiv: [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) )
- [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **get_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int) ) *const*

The subdivision amount of the second quadrant on the shadow atlas.

---

<span id="class_Viewport_property_positional_shadow_atlas_quad_2"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **positional_shadow_atlas_quad_2** = `3` [🔗](class_viewport.md#class_Viewport_property_positional_shadow_atlas_quad_2)

- void **set_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int), subdiv: [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) )
- [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **get_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int) ) *const*

The subdivision amount of the third quadrant on the shadow atlas.

---

<span id="class_Viewport_property_positional_shadow_atlas_quad_3"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **positional_shadow_atlas_quad_3** = `4` [🔗](class_viewport.md#class_Viewport_property_positional_shadow_atlas_quad_3)

- void **set_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int), subdiv: [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) )
- [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **get_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int) ) *const*

The subdivision amount of the fourth quadrant on the shadow atlas.

---

<span id="class_Viewport_property_positional_shadow_atlas_size"></span>

[int](class_int.md#class_int) **positional_shadow_atlas_size** = `2048` [🔗](class_viewport.md#class_Viewport_property_positional_shadow_atlas_size)

- void **set_positional_shadow_atlas_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_positional_shadow_atlas_size** ( )

The shadow atlas' resolution (used for omni and spot lights). The value is rounded up to the nearest power of 2.

 **Note:** If this is set to `0`, no positional shadows will be visible at all. This can improve performance significantly on low-end systems by reducing both the CPU and GPU load (as fewer draw calls are needed to draw the scene without shadows).

---

<span id="class_Viewport_property_scaling_3d_mode"></span>

[Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) **scaling_3d_mode** = `0` [🔗](class_viewport.md#class_Viewport_property_scaling_3d_mode)

- void **set_scaling_3d_mode** ( value: [Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) )
- [Scaling3DMode](class_viewport.md#enum_Viewport_Scaling3DMode) **get_scaling_3d_mode** ( )

Sets scaling 3D mode. Bilinear scaling renders at different resolution to either undersample or supersample the viewport. FidelityFX Super Resolution 1.0, abbreviated to FSR, is an upscaling technology that produces high quality images at fast framerates by using a spatially aware upscaling algorithm. FSR is slightly more expensive than bilinear, but it produces significantly higher image quality. FSR should be used where possible.

To control this property on the root viewport, set the ProjectSettings.rendering/scaling_3d/mode project setting.

---

<span id="class_Viewport_property_scaling_3d_scale"></span>

[float](class_float.md#class_float) **scaling_3d_scale** = `1.0` [🔗](class_viewport.md#class_Viewport_property_scaling_3d_scale)

- void **set_scaling_3d_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_scaling_3d_scale** ( )

Scales the 3D render buffer based on the viewport size uses an image filter specified in ProjectSettings.rendering/scaling_3d/mode to scale the output image to the full viewport size. Values lower than `1.0` can be used to speed up 3D rendering at the cost of quality (undersampling). Values greater than `1.0` are only valid for bilinear mode and can be used to improve 3D rendering quality at a high performance cost (supersampling). See also ProjectSettings.rendering/anti_aliasing/quality/msaa_3d for multi-sample antialiasing, which is significantly cheaper but only smooths the edges of polygons.

When using FSR upscaling, AMD recommends exposing the following values as preset options to users "Ultra Quality: 0.77", "Quality: 0.67", "Balanced: 0.59", "Performance: 0.5" instead of exposing the entire scale.

To control this property on the root viewport, set the ProjectSettings.rendering/scaling_3d/scale project setting.

---

<span id="class_Viewport_property_screen_space_aa"></span>

[ScreenSpaceAA](class_viewport.md#enum_Viewport_ScreenSpaceAA) **screen_space_aa** = `0` [🔗](class_viewport.md#class_Viewport_property_screen_space_aa)

- void **set_screen_space_aa** ( value: [ScreenSpaceAA](class_viewport.md#enum_Viewport_ScreenSpaceAA) )
- [ScreenSpaceAA](class_viewport.md#enum_Viewport_ScreenSpaceAA) **get_screen_space_aa** ( )

Sets the screen-space antialiasing method used. Screen-space antialiasing works by selectively blurring edges in a post-process shader. It differs from MSAA which takes multiple coverage samples while rendering objects. Screen-space AA methods are typically faster than MSAA and will smooth out specular aliasing, but tend to make scenes appear blurry.

See also ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa and [RenderingServer.viewport_set_screen_space_aa()](class_renderingserver.md#class_RenderingServer_method_viewport_set_screen_space_aa).

---

<span id="class_Viewport_property_sdf_oversize"></span>

[SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) **sdf_oversize** = `1` [🔗](class_viewport.md#class_Viewport_property_sdf_oversize)

- void **set_sdf_oversize** ( value: [SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) )
- [SDFOversize](class_viewport.md#enum_Viewport_SDFOversize) **get_sdf_oversize** ( )

Controls how much of the original viewport's size should be covered by the 2D signed distance field. This SDF can be sampled in [CanvasItem](class_canvasitem.md#class_CanvasItem) shaders and is also used for [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) collision. Higher values allow portions of occluders located outside the viewport to still be taken into account in the generated signed distance field, at the cost of performance. If you notice particles falling through [LightOccluder2D](class_lightoccluder2d.md#class_LightOccluder2D) s as the occluders leave the viewport, increase this setting.

The percentage is added on each axis and on both sides. For example, with the default [SDF_OVERSIZE_120_PERCENT](class_viewport.md#class_Viewport_constant_SDF_OVERSIZE_120_PERCENT), the signed distance field will cover 20% of the viewport's size outside the viewport on each side (top, right, bottom, left).

---

<span id="class_Viewport_property_sdf_scale"></span>

[SDFScale](class_viewport.md#enum_Viewport_SDFScale) **sdf_scale** = `1` [🔗](class_viewport.md#class_Viewport_property_sdf_scale)

- void **set_sdf_scale** ( value: [SDFScale](class_viewport.md#enum_Viewport_SDFScale) )
- [SDFScale](class_viewport.md#enum_Viewport_SDFScale) **get_sdf_scale** ( )

The resolution scale to use for the 2D signed distance field. Higher values lead to a more precise and more stable signed distance field as the camera moves, at the cost of performance.

---

<span id="class_Viewport_property_snap_2d_transforms_to_pixel"></span>

[bool](class_bool.md#class_bool) **snap_2d_transforms_to_pixel** = `false` [🔗](class_viewport.md#class_Viewport_property_snap_2d_transforms_to_pixel)

- void **set_snap_2d_transforms_to_pixel** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_snap_2d_transforms_to_pixel_enabled** ( )

If `true`, [CanvasItem](class_canvasitem.md#class_CanvasItem) nodes will internally snap to full pixels. Their position can still be sub-pixel, but the decimals will not have effect. This can lead to a crisper appearance at the cost of less smooth movement, especially when [Camera2D](class_camera2d.md#class_Camera2D) smoothing is enabled.

---

<span id="class_Viewport_property_snap_2d_vertices_to_pixel"></span>

[bool](class_bool.md#class_bool) **snap_2d_vertices_to_pixel** = `false` [🔗](class_viewport.md#class_Viewport_property_snap_2d_vertices_to_pixel)

- void **set_snap_2d_vertices_to_pixel** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_snap_2d_vertices_to_pixel_enabled** ( )

If `true`, vertices of [CanvasItem](class_canvasitem.md#class_CanvasItem) nodes will snap to full pixels. Only affects the final vertex positions, not the transforms. This can lead to a crisper appearance at the cost of less smooth movement, especially when [Camera2D](class_camera2d.md#class_Camera2D) smoothing is enabled.

---

<span id="class_Viewport_property_texture_mipmap_bias"></span>

[float](class_float.md#class_float) **texture_mipmap_bias** = `0.0` [🔗](class_viewport.md#class_Viewport_property_texture_mipmap_bias)

- void **set_texture_mipmap_bias** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_texture_mipmap_bias** ( )

Affects the final texture sharpness by reading from a lower or higher mipmap (also called "texture LOD bias"). Negative values make mipmapped textures sharper but grainier when viewed at a distance, while positive values make mipmapped textures blurrier (even when up close).

Enabling temporal antialiasing ([use_taa](class_viewport.md#class_Viewport_property_use_taa)) will automatically apply a `-0.5` offset to this value, while enabling FXAA ([screen_space_aa](class_viewport.md#class_Viewport_property_screen_space_aa)) will automatically apply a `-0.25` offset to this value. If both TAA and FXAA are enabled at the same time, an offset of `-0.75` is applied to this value.

 **Note:** If [scaling_3d_scale](class_viewport.md#class_Viewport_property_scaling_3d_scale) is lower than `1.0` (exclusive), [texture_mipmap_bias](class_viewport.md#class_Viewport_property_texture_mipmap_bias) is used to adjust the automatic mipmap bias which is calculated internally based on the scale factor. The formula for this is `log2(scaling_3d_scale) + mipmap_bias`.

To control this property on the root viewport, set the ProjectSettings.rendering/textures/default_filters/texture_mipmap_bias project setting.

---

<span id="class_Viewport_property_transparent_bg"></span>

[bool](class_bool.md#class_bool) **transparent_bg** = `false` [🔗](class_viewport.md#class_Viewport_property_transparent_bg)

- void **set_transparent_background** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_transparent_background** ( )

If `true`, the viewport should render its background as transparent.

 **Note:** Due to technical limitations, certain rendering features are disabled when a viewport has a transparent background. This currently applies to screen-space reflections, subsurface scattering, and depth of field.

---

<span id="class_Viewport_property_use_debanding"></span>

[bool](class_bool.md#class_bool) **use_debanding** = `false` [🔗](class_viewport.md#class_Viewport_property_use_debanding)

- void **set_use_debanding** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_debanding** ( )

When using the Mobile or Forward+ renderers, set [use_debanding](class_viewport.md#class_Viewport_property_use_debanding) to enable or disable the debanding feature of this **Viewport**. If [use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d) is `false`, 2D rendering is *not* affected by debanding unless the [Environment.background_mode](class_environment.md#class_Environment_property_background_mode) is [Environment.BG_CANVAS](class_environment.md#class_Environment_constant_BG_CANVAS). If [use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d) is `true`, debanding will only be applied if this is the root **Viewport** and will affect all 2D and 3D rendering, including canvas items.

 [use_debanding](class_viewport.md#class_Viewport_property_use_debanding) has no effect when using the Compatibility rendering method. The Mobile renderer can also use material debanding, which can be set with [RenderingServer.material_set_use_debanding()](class_renderingserver.md#class_RenderingServer_method_material_set_use_debanding) or configured with ProjectSettings.rendering/anti_aliasing/quality/use_debanding.

See also ProjectSettings.rendering/anti_aliasing/quality/use_debanding, [RenderingServer.material_set_use_debanding()](class_renderingserver.md#class_RenderingServer_method_material_set_use_debanding), and [RenderingServer.viewport_set_use_debanding()](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_debanding).

---

<span id="class_Viewport_property_use_hdr_2d"></span>

[bool](class_bool.md#class_bool) **use_hdr_2d** = `false` [🔗](class_viewport.md#class_Viewport_property_use_hdr_2d)

- void **set_use_hdr_2d** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_hdr_2d** ( )

If `true`, 2D rendering will use a high dynamic range (HDR) `RGBA16` format framebuffer. Additionally, 2D rendering will be performed on linear values and will be converted using the appropriate transfer function immediately before blitting to the screen (if the Viewport is attached to the screen).

Practically speaking, this means that the end result of the Viewport will not be clamped to the `0-1` range and can be used in 3D rendering without color encoding adjustments. This allows 2D rendering to take advantage of effects requiring high dynamic range (e.g. 2D glow) as well as substantially improves the appearance of effects requiring highly detailed gradients.

---

<span id="class_Viewport_property_use_occlusion_culling"></span>

[bool](class_bool.md#class_bool) **use_occlusion_culling** = `false` [🔗](class_viewport.md#class_Viewport_property_use_occlusion_culling)

- void **set_use_occlusion_culling** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_occlusion_culling** ( )

If `true`, [OccluderInstance3D](class_occluderinstance3d.md#class_OccluderInstance3D) nodes will be usable for occlusion culling in 3D for this viewport. For the root viewport, ProjectSettings.rendering/occlusion_culling/use_occlusion_culling must be set to `true` instead.

 **Note:** Enabling occlusion culling has a cost on the CPU. Only enable occlusion culling if you actually plan to use it, and think whether your scene can actually benefit from occlusion culling. Large, open scenes with few or no objects blocking the view will generally not benefit much from occlusion culling. Large open scenes generally benefit more from mesh LOD and visibility ranges ([GeometryInstance3D.visibility_range_begin](class_geometryinstance3d.md#class_GeometryInstance3D_property_visibility_range_begin) and [GeometryInstance3D.visibility_range_end](class_geometryinstance3d.md#class_GeometryInstance3D_property_visibility_range_end)) compared to occlusion culling.

 **Note:** Due to memory constraints, occlusion culling is not supported by default in Web export templates. It can be enabled by compiling custom Web export templates with `module_raycast_enabled=yes`.

---

<span id="class_Viewport_property_use_taa"></span>

[bool](class_bool.md#class_bool) **use_taa** = `false` [🔗](class_viewport.md#class_Viewport_property_use_taa)

- void **set_use_taa** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_taa** ( )

Enables temporal antialiasing for this viewport. TAA works by jittering the camera and accumulating the images of the last rendered frames, motion vector rendering is used to account for camera and object motion.

 **Note:** The implementation is not complete yet, some visual instances such as particles and skinned meshes may show artifacts.

See also ProjectSettings.rendering/anti_aliasing/quality/use_taa and [RenderingServer.viewport_set_use_taa()](class_renderingserver.md#class_RenderingServer_method_viewport_set_use_taa).

---

<span id="class_Viewport_property_use_xr"></span>

[bool](class_bool.md#class_bool) **use_xr** = `false` [🔗](class_viewport.md#class_Viewport_property_use_xr)

- void **set_use_xr** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_xr** ( )

If `true`, the viewport will use the primary XR interface to render XR output. When applicable this can result in a stereoscopic image and the resulting render being output to a headset.

---

<span id="class_Viewport_property_vrs_mode"></span>

[VRSMode](class_viewport.md#enum_Viewport_VRSMode) **vrs_mode** = `0` [🔗](class_viewport.md#class_Viewport_property_vrs_mode)

- void **set_vrs_mode** ( value: [VRSMode](class_viewport.md#enum_Viewport_VRSMode) )
- [VRSMode](class_viewport.md#enum_Viewport_VRSMode) **get_vrs_mode** ( )

The Variable Rate Shading (VRS) mode that is used for this viewport. Note, if hardware does not support VRS this property is ignored.

---

<span id="class_Viewport_property_vrs_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **vrs_texture** [🔗](class_viewport.md#class_Viewport_property_vrs_texture)

- void **set_vrs_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_vrs_texture** ( )

Texture to use when [vrs_mode](class_viewport.md#class_Viewport_property_vrs_mode) is set to [VRS_TEXTURE](class_viewport.md#class_Viewport_constant_VRS_TEXTURE).

The texture *must* use a lossless compression format so that colors can be matched precisely. The following VRS densities are mapped to various colors, with brighter colors representing a lower level of shading precision:

.. code:: text

    - 1×1 = rgb(0, 0, 0)     - #000000
    - 1×2 = rgb(0, 85, 0)    - #005500
    - 2×1 = rgb(85, 0, 0)    - #550000
    - 2×2 = rgb(85, 85, 0)   - #555500
    - 2×4 = rgb(85, 170, 0)  - #55aa00
    - 4×2 = rgb(170, 85, 0)  - #aa5500
    - 4×4 = rgb(170, 170, 0) - #aaaa00
    - 4×8 = rgb(170, 255, 0) - #aaff00 - Not supported on most hardware
    - 8×4 = rgb(255, 170, 0) - #ffaa00 - Not supported on most hardware
    - 8×8 = rgb(255, 255, 0) - #ffff00 - Not supported on most hardware

---

<span id="class_Viewport_property_vrs_update_mode"></span>

[VRSUpdateMode](class_viewport.md#enum_Viewport_VRSUpdateMode) **vrs_update_mode** = `1` [🔗](class_viewport.md#class_Viewport_property_vrs_update_mode)

- void **set_vrs_update_mode** ( value: [VRSUpdateMode](class_viewport.md#enum_Viewport_VRSUpdateMode) )
- [VRSUpdateMode](class_viewport.md#enum_Viewport_VRSUpdateMode) **get_vrs_update_mode** ( )

Sets the update mode for Variable Rate Shading (VRS) for the viewport. VRS requires the input texture to be converted to the format usable by the VRS method supported by the hardware. The update mode defines how often this happens. If the GPU does not support VRS, or VRS is not enabled, this property is ignored.

---

<span id="class_Viewport_property_world_2d"></span>

[World2D](class_world2d.md#class_World2D) **world_2d** [🔗](class_viewport.md#class_Viewport_property_world_2d)

- void **set_world_2d** ( value: [World2D](class_world2d.md#class_World2D) )
- [World2D](class_world2d.md#class_World2D) **get_world_2d** ( )

The custom [World2D](class_world2d.md#class_World2D) which can be used as 2D environment source.

---

<span id="class_Viewport_property_world_3d"></span>

[World3D](class_world3d.md#class_World3D) **world_3d** [🔗](class_viewport.md#class_Viewport_property_world_3d)

- void **set_world_3d** ( value: [World3D](class_world3d.md#class_World3D) )
- [World3D](class_world3d.md#class_World3D) **get_world_3d** ( )

The custom [World3D](class_world3d.md#class_World3D) which can be used as 3D environment source.

---

### Method Descriptions

<span id="class_Viewport_method_find_world_2d"></span>

[World2D](class_world2d.md#class_World2D) **find_world_2d** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_find_world_2d)

Returns the first valid [World2D](class_world2d.md#class_World2D) for this viewport, searching the [world_2d](class_viewport.md#class_Viewport_property_world_2d) property of itself and any Viewport ancestor.

---

<span id="class_Viewport_method_find_world_3d"></span>

[World3D](class_world3d.md#class_World3D) **find_world_3d** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_find_world_3d)

Returns the first valid [World3D](class_world3d.md#class_World3D) for this viewport, searching the [world_3d](class_viewport.md#class_Viewport_property_world_3d) property of itself and any Viewport ancestor.

---

<span id="class_Viewport_method_get_audio_listener_2d"></span>

[AudioListener2D](class_audiolistener2d.md#class_AudioListener2D) **get_audio_listener_2d** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_audio_listener_2d)

Returns the currently active 2D audio listener. Returns `null` if there are no active 2D audio listeners, in which case the active 2D camera will be treated as listener.

---

<span id="class_Viewport_method_get_audio_listener_3d"></span>

[AudioListener3D](class_audiolistener3d.md#class_AudioListener3D) **get_audio_listener_3d** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_audio_listener_3d)

Returns the currently active 3D audio listener. Returns `null` if there are no active 3D audio listeners, in which case the active 3D camera will be treated as listener.

---

<span id="class_Viewport_method_get_camera_2d"></span>

[Camera2D](class_camera2d.md#class_Camera2D) **get_camera_2d** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_camera_2d)

Returns the currently active 2D camera. Returns `null` if there are no active cameras.

 **Note:** If called while the *Camera Override* system is active in editor, this will return the internally managed override camera. It is therefore advised to avoid caching the return value, or to check that the cached value is still a valid instance and is the current camera before use. See @GlobalScope.is_instance_valid() and [Camera2D.is_current()](class_camera2d.md#class_Camera2D_method_is_current).

---

<span id="class_Viewport_method_get_camera_3d"></span>

[Camera3D](class_camera3d.md#class_Camera3D) **get_camera_3d** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_camera_3d)

Returns the currently active 3D camera. Returns `null` if there are no active cameras.

 **Note:** If called while the *Camera Override* system is active in editor, this will return the internally managed override camera. It is therefore advised to avoid caching the return value, or to check that the cached value is a valid instance and is the current camera before use. See @GlobalScope.is_instance_valid() and [Camera3D.current](class_camera3d.md#class_Camera3D_property_current).

---

<span id="class_Viewport_method_get_canvas_cull_mask_bit"></span>

[bool](class_bool.md#class_bool) **get_canvas_cull_mask_bit** ( layer: [int](class_int.md#class_int) ) *const* [🔗](class_viewport.md#class_Viewport_method_get_canvas_cull_mask_bit)

Returns an individual bit on the rendering layer mask.

---

<span id="class_Viewport_method_get_embedded_subwindows"></span>

[Array](class_array.md#class_Array)\[[Window](class_window.md#class_Window)\] **get_embedded_subwindows** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_embedded_subwindows)

Returns a list of the visible embedded [Window](class_window.md#class_Window) s inside the viewport.

 **Note:** [Window](class_window.md#class_Window) s inside other viewports will not be listed.

---

<span id="class_Viewport_method_get_final_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **get_final_transform** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_final_transform)

Returns the transform from the viewport's coordinate system to the embedder's coordinate system.

---

<span id="class_Viewport_method_get_mouse_position"></span>

[Vector2](class_vector2.md#class_Vector2) **get_mouse_position** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_mouse_position)

Returns the mouse's position in this **Viewport** using the coordinate system of this **Viewport**.

---

<span id="class_Viewport_method_get_oversampling"></span>

[float](class_float.md#class_float) **get_oversampling** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_oversampling)

Returns viewport oversampling factor.

---

<span id="class_Viewport_method_get_positional_shadow_atlas_quadrant_subdiv"></span>

[PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) **get_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int) ) *const* [🔗](class_viewport.md#class_Viewport_method_get_positional_shadow_atlas_quadrant_subdiv)

Returns the positional shadow atlas quadrant subdivision of the specified quadrant.

---

<span id="class_Viewport_method_get_render_info"></span>

[int](class_int.md#class_int) **get_render_info** ( type: [RenderInfoType](class_viewport.md#enum_Viewport_RenderInfoType), info: [RenderInfo](class_viewport.md#enum_Viewport_RenderInfo) ) [🔗](class_viewport.md#class_Viewport_method_get_render_info)

Returns rendering statistics of the given type.

---

<span id="class_Viewport_method_get_screen_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **get_screen_transform** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_screen_transform)

Returns the transform from the Viewport's coordinates to the screen coordinates of the containing window manager window.

---

<span id="class_Viewport_method_get_stretch_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **get_stretch_transform** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_stretch_transform)

Returns the automatically computed 2D stretch transform, taking the **Viewport**'s stretch settings into account. The final value is multiplied by [Window.content_scale_factor](class_window.md#class_Window_property_content_scale_factor), but only for the root viewport. If this method is called on a [SubViewport](class_subviewport.md#class_SubViewport) (e.g., in a scene tree with [SubViewportContainer](class_subviewportcontainer.md#class_SubViewportContainer) and [SubViewport](class_subviewport.md#class_SubViewport)), the scale factor of the root window will not be applied. Using [Transform2D.get_scale()](class_transform2d.md#class_Transform2D_method_get_scale) on the returned value, this can be used to compensate for scaling when zooming a [Camera2D](class_camera2d.md#class_Camera2D) node, or to scale down a [TextureRect](class_texturerect.md#class_TextureRect) to be pixel-perfect regardless of the automatically computed scale factor.

 **Note:** Due to how pixel scaling works, the returned transform's X and Y scale may differ slightly, even when [Window.content_scale_aspect](class_window.md#class_Window_property_content_scale_aspect) is set to a mode that preserves the pixels' aspect ratio. If [Window.content_scale_aspect](class_window.md#class_Window_property_content_scale_aspect) is [Window.CONTENT_SCALE_ASPECT_IGNORE](class_window.md#class_Window_constant_CONTENT_SCALE_ASPECT_IGNORE), the X and Y scale may differ *significantly*.

---

<span id="class_Viewport_method_get_texture"></span>

[ViewportTexture](class_viewporttexture.md#class_ViewportTexture) **get_texture** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_texture)

Returns the viewport's texture.

 **Note:** When trying to store the current texture (e.g. in a file), it might be completely black or outdated if used too early, especially when used in e.g. [Node._ready()](class_node.md#class_Node_private_method__ready). To make sure the texture you get is correct, you can await [RenderingServer.frame_post_draw](class_renderingserver.md#class_RenderingServer_signal_frame_post_draw) signal.

.. tabs::

```
```

    func _ready():
        await RenderingServer.frame_post_draw
        $Viewport.get_texture().get_image().save_png("user://Screenshot.png")

```
```

    public async override void _Ready()
    {
        await ToSignal(RenderingServer.Singleton, RenderingServer.SignalName.FramePostDraw);
        var viewport = GetNode<Viewport>("Viewport");
        viewport.GetTexture().GetImage().SavePng("user://Screenshot.png");
    }

 **Note:** When [use_hdr_2d](class_viewport.md#class_Viewport_property_use_hdr_2d) is `true` the returned texture will be an HDR image using linear encoding.

---

<span id="class_Viewport_method_get_viewport_rid"></span>

[RID](class_rid.md#class_RID) **get_viewport_rid** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_viewport_rid)

Returns the viewport's RID from the [RenderingServer](class_renderingserver.md#class_RenderingServer).

---

<span id="class_Viewport_method_get_visible_rect"></span>

[Rect2](class_rect2.md#class_Rect2) **get_visible_rect** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_get_visible_rect)

Returns the visible rectangle in global screen coordinates.

---

<span id="class_Viewport_method_gui_cancel_drag"></span>

void **gui_cancel_drag** ( ) [🔗](class_viewport.md#class_Viewport_method_gui_cancel_drag)

Cancels the drag operation that was previously started through [Control._get_drag_data()](class_control.md#class_Control_private_method__get_drag_data) or forced with [Control.force_drag()](class_control.md#class_Control_method_force_drag).

---

<span id="class_Viewport_method_gui_get_drag_data"></span>

[Variant](class_variant.md#class_Variant) **gui_get_drag_data** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_gui_get_drag_data)

Returns the drag data from the GUI, that was previously returned by [Control._get_drag_data()](class_control.md#class_Control_private_method__get_drag_data).

---

<span id="class_Viewport_method_gui_get_drag_description"></span>

[String](class_string.md#class_String) **gui_get_drag_description** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_gui_get_drag_description)

Returns the human-readable description of the drag data, used for assistive apps.

---

<span id="class_Viewport_method_gui_get_focus_owner"></span>

[Control](class_control.md#class_Control) **gui_get_focus_owner** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_gui_get_focus_owner)

Returns the currently focused [Control](class_control.md#class_Control) within this viewport. If no [Control](class_control.md#class_Control) is focused, returns `null`.

---

<span id="class_Viewport_method_gui_get_hovered_control"></span>

[Control](class_control.md#class_Control) **gui_get_hovered_control** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_gui_get_hovered_control)

Returns the [Control](class_control.md#class_Control) that the mouse is currently hovering over in this viewport. If no [Control](class_control.md#class_Control) has the cursor, returns `null`.

Typically the leaf [Control](class_control.md#class_Control) node or deepest level of the subtree which claims hover. This is very useful when used together with [Node.is_ancestor_of()](class_node.md#class_Node_method_is_ancestor_of) to find if the mouse is within a control tree.

---

<span id="class_Viewport_method_gui_is_drag_successful"></span>

[bool](class_bool.md#class_bool) **gui_is_drag_successful** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_gui_is_drag_successful)

Returns `true` if the drag operation is successful.

---

<span id="class_Viewport_method_gui_is_dragging"></span>

[bool](class_bool.md#class_bool) **gui_is_dragging** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_gui_is_dragging)

Returns `true` if a drag operation is currently ongoing and where the drop action could happen in this viewport.

Alternative to [Node.NOTIFICATION_DRAG_BEGIN](class_node.md#class_Node_constant_NOTIFICATION_DRAG_BEGIN) and [Node.NOTIFICATION_DRAG_END](class_node.md#class_Node_constant_NOTIFICATION_DRAG_END) when you prefer polling the value.

---

<span id="class_Viewport_method_gui_release_focus"></span>

void **gui_release_focus** ( ) [🔗](class_viewport.md#class_Viewport_method_gui_release_focus)

Removes the focus from the currently focused [Control](class_control.md#class_Control) within this viewport. If no [Control](class_control.md#class_Control) has the focus, does nothing.

---

<span id="class_Viewport_method_gui_set_drag_description"></span>

void **gui_set_drag_description** ( description: [String](class_string.md#class_String) ) [🔗](class_viewport.md#class_Viewport_method_gui_set_drag_description)

Sets the human-readable description of the drag data to `description`, used for assistive apps.

---

<span id="class_Viewport_method_is_input_handled"></span>

[bool](class_bool.md#class_bool) **is_input_handled** ( ) *const* [🔗](class_viewport.md#class_Viewport_method_is_input_handled)

Returns whether the current [InputEvent](class_inputevent.md#class_InputEvent) has been handled. Input events are not handled until [set_input_as_handled()](class_viewport.md#class_Viewport_method_set_input_as_handled) has been called during the lifetime of an [InputEvent](class_inputevent.md#class_InputEvent).

This is usually done as part of input handling methods like [Node._input()](class_node.md#class_Node_private_method__input), [Control._gui_input()](class_control.md#class_Control_private_method__gui_input) or others, as well as in corresponding signal handlers.

If [handle_input_locally](class_viewport.md#class_Viewport_property_handle_input_locally) is set to `false`, this method will try finding the first parent viewport that is set to handle input locally, and return its value for [is_input_handled()](class_viewport.md#class_Viewport_method_is_input_handled) instead.

---

<span id="class_Viewport_method_notify_mouse_entered"></span>

void **notify_mouse_entered** ( ) [🔗](class_viewport.md#class_Viewport_method_notify_mouse_entered)

Inform the Viewport that the mouse has entered its area. Use this function before sending an [InputEventMouseButton](class_inputeventmousebutton.md#class_InputEventMouseButton) or [InputEventMouseMotion](class_inputeventmousemotion.md#class_InputEventMouseMotion) to the **Viewport** with [push_input()](class_viewport.md#class_Viewport_method_push_input). See also [notify_mouse_exited()](class_viewport.md#class_Viewport_method_notify_mouse_exited).

 **Note:** In most cases, it is not necessary to call this function because [SubViewport](class_subviewport.md#class_SubViewport) nodes that are children of [SubViewportContainer](class_subviewportcontainer.md#class_SubViewportContainer) are notified automatically. This is only necessary when interacting with viewports in non-default ways, for example as textures in [TextureRect](class_texturerect.md#class_TextureRect) or with an [Area3D](class_area3d.md#class_Area3D) that forwards input events.

---

<span id="class_Viewport_method_notify_mouse_exited"></span>

void **notify_mouse_exited** ( ) [🔗](class_viewport.md#class_Viewport_method_notify_mouse_exited)

Inform the Viewport that the mouse has left its area. Use this function when the node that displays the viewport notices the mouse has left the area of the displayed viewport. See also [notify_mouse_entered()](class_viewport.md#class_Viewport_method_notify_mouse_entered).

 **Note:** In most cases, it is not necessary to call this function because [SubViewport](class_subviewport.md#class_SubViewport) nodes that are children of [SubViewportContainer](class_subviewportcontainer.md#class_SubViewportContainer) are notified automatically. This is only necessary when interacting with viewports in non-default ways, for example as textures in [TextureRect](class_texturerect.md#class_TextureRect) or with an [Area3D](class_area3d.md#class_Area3D) that forwards input events.

---

<span id="class_Viewport_method_push_input"></span>

void **push_input** ( event: [InputEvent](class_inputevent.md#class_InputEvent), in_local_coords: [bool](class_bool.md#class_bool) = false ) [🔗](class_viewport.md#class_Viewport_method_push_input)

Triggers the given `event` in this **Viewport**. This can be used to pass an [InputEvent](class_inputevent.md#class_InputEvent) between viewports, or to locally apply inputs that were sent over the network or saved to a file.

If `in_local_coords` is `false`, the event's position is in the embedder's coordinates and will be converted to viewport coordinates. If `in_local_coords` is `true`, the event's position is in viewport coordinates.

While this method serves a similar purpose as [Input.parse_input_event()](class_input.md#class_Input_method_parse_input_event), it does not remap the specified `event` based on project settings like ProjectSettings.input_devices/pointing/emulate_touch_from_mouse.

Calling this method will propagate calls to child nodes for following methods in the given order:

- [Node._input()](class_node.md#class_Node_private_method__input)

- [Control._gui_input()](class_control.md#class_Control_private_method__gui_input) for [Control](class_control.md#class_Control) nodes

- [Node._shortcut_input()](class_node.md#class_Node_private_method__shortcut_input)

- [Node._unhandled_key_input()](class_node.md#class_Node_private_method__unhandled_key_input)

- [Node._unhandled_input()](class_node.md#class_Node_private_method__unhandled_input)

If an earlier method marks the input as handled via [set_input_as_handled()](class_viewport.md#class_Viewport_method_set_input_as_handled), any later method in this list will not be called.

If none of the methods handle the event and [physics_object_picking](class_viewport.md#class_Viewport_property_physics_object_picking) is `true`, the event is used for physics object picking.

---

<span id="class_Viewport_method_push_text_input"></span>

void **push_text_input** ( text: [String](class_string.md#class_String) ) [🔗](class_viewport.md#class_Viewport_method_push_text_input)

Helper method which calls the `set_text()` method on the currently focused [Control](class_control.md#class_Control), provided that it is defined (e.g. if the focused Control is [Button](class_button.md#class_Button) or [LineEdit](class_lineedit.md#class_LineEdit)).

---

<span id="class_Viewport_method_push_unhandled_input"></span>

void **push_unhandled_input** ( event: [InputEvent](class_inputevent.md#class_InputEvent), in_local_coords: [bool](class_bool.md#class_bool) = false ) [🔗](class_viewport.md#class_Viewport_method_push_unhandled_input)

**Deprecated:** Use [push_input()](class_viewport.md#class_Viewport_method_push_input) instead.

Triggers the given `event` in this **Viewport**. This can be used to pass an [InputEvent](class_inputevent.md#class_InputEvent) between viewports, or to locally apply inputs that were sent over the network or saved to a file.

If `in_local_coords` is `false`, the event's position is in the embedder's coordinates and will be converted to viewport coordinates. If `in_local_coords` is `true`, the event's position is in viewport coordinates.

Calling this method will propagate calls to child nodes for following methods in the given order:

- [Node._shortcut_input()](class_node.md#class_Node_private_method__shortcut_input)

- [Node._unhandled_key_input()](class_node.md#class_Node_private_method__unhandled_key_input)

- [Node._unhandled_input()](class_node.md#class_Node_private_method__unhandled_input)

If an earlier method marks the input as handled via [set_input_as_handled()](class_viewport.md#class_Viewport_method_set_input_as_handled), any later method in this list will not be called.

If none of the methods handle the event and [physics_object_picking](class_viewport.md#class_Viewport_property_physics_object_picking) is `true`, the event is used for physics object picking.

 **Note:** This method doesn't propagate input events to embedded [Window](class_window.md#class_Window) s or [SubViewport](class_subviewport.md#class_SubViewport) s.

---

<span id="class_Viewport_method_set_canvas_cull_mask_bit"></span>

void **set_canvas_cull_mask_bit** ( layer: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool) ) [🔗](class_viewport.md#class_Viewport_method_set_canvas_cull_mask_bit)

Set/clear individual bits on the rendering layer mask. This simplifies editing this **Viewport**'s layers.

---

<span id="class_Viewport_method_set_input_as_handled"></span>

void **set_input_as_handled** ( ) [🔗](class_viewport.md#class_Viewport_method_set_input_as_handled)

Stops the input from propagating further up the [SceneTree](class_scenetree.md#class_SceneTree).

 **Note:** This does not affect the methods in [Input](class_input.md#class_Input), only the way events are propagated.

---

<span id="class_Viewport_method_set_positional_shadow_atlas_quadrant_subdiv"></span>

void **set_positional_shadow_atlas_quadrant_subdiv** ( quadrant: [int](class_int.md#class_int), subdiv: [PositionalShadowAtlasQuadrantSubdiv](class_viewport.md#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv) ) [🔗](class_viewport.md#class_Viewport_method_set_positional_shadow_atlas_quadrant_subdiv)

Sets the number of subdivisions to use in the specified quadrant. A higher number of subdivisions allows you to have more shadows in the scene at once, but reduces the quality of the shadows. A good practice is to have quadrants with a varying number of subdivisions and to have as few subdivisions as possible.

---

<span id="class_Viewport_method_update_mouse_cursor_state"></span>

void **update_mouse_cursor_state** ( ) [🔗](class_viewport.md#class_Viewport_method_update_mouse_cursor_state)

Force instantly updating the display based on the current mouse cursor position. This includes updating the mouse cursor shape and sending necessary [Control.mouse_entered](class_control.md#class_Control_signal_mouse_entered), [CollisionObject2D.mouse_entered](class_collisionobject2d.md#class_CollisionObject2D_signal_mouse_entered), [CollisionObject3D.mouse_entered](class_collisionobject3d.md#class_CollisionObject3D_signal_mouse_entered) and [Window.mouse_entered](class_window.md#class_Window_signal_mouse_entered) signals and their respective `mouse_exited` counterparts.

---

<span id="class_Viewport_method_warp_mouse"></span>

void **warp_mouse** ( position: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_viewport.md#class_Viewport_method_warp_mouse)

Moves the mouse pointer to the specified position in this **Viewport** using the coordinate system of this **Viewport**.

 **Note:** [warp_mouse()](class_viewport.md#class_Viewport_method_warp_mouse) is only supported on Windows, macOS and Linux. It has no effect on Android, iOS and Web.
