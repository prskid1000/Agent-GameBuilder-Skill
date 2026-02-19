<span id="class_RenderingDevice"></span>

## RenderingDevice

**Inherits:** [Object](class_object.md#class_Object)

Abstraction for working with modern low-level graphics APIs.

### Description

**RenderingDevice** is an abstraction for working with modern low-level graphics APIs such as Vulkan. Compared to [RenderingServer](class_renderingserver.md#class_RenderingServer) (which works with Godot's own rendering subsystems), **RenderingDevice** is much lower-level and allows working more directly with the underlying graphics APIs. **RenderingDevice** is used in Godot to provide support for several modern low-level graphics APIs while reducing the amount of code duplication required. **RenderingDevice** can also be used in your own projects to perform things that are not exposed by [RenderingServer](class_renderingserver.md#class_RenderingServer) or high-level nodes, such as using compute shaders.

On startup, Godot creates a global **RenderingDevice** which can be retrieved using [RenderingServer.get_rendering_device()](class_renderingserver.md#class_RenderingServer_method_get_rendering_device). This global **RenderingDevice** performs drawing to the screen.

 **Local RenderingDevices:** Using [RenderingServer.create_local_rendering_device()](class_renderingserver.md#class_RenderingServer_method_create_local_rendering_device), you can create "secondary" rendering devices to perform drawing and GPU compute operations on separate threads.

 **Note:** **RenderingDevice** assumes intermediate knowledge of modern graphics APIs such as Vulkan, Direct3D 12, Metal or WebGPU. These graphics APIs are lower-level than OpenGL or Direct3D 11, requiring you to perform what was previously done by the graphics driver itself. If you have difficulty understanding the concepts used in this class, follow the Vulkan Tutorial or Vulkan Guide. It's recommended to have existing modern OpenGL or Direct3D 11 knowledge before attempting to learn a low-level graphics API.

 **Note:** **RenderingDevice** is not available when running in headless mode or when using the Compatibility rendering method.

### Tutorials

- [Using compute shaders](../tutorials/shaders/compute_shaders.md)

### Methods


| Error | [acceleration_structure_build](class_renderingdevice.md#class_RenderingDevice_method_acceleration_structure_build) ( acceleration_structure: [RID](class_rid.md#class_RID) ) |
| --- | --- |
| void | [barrier](class_renderingdevice.md#class_RenderingDevice_method_barrier) ( from: | bitfield | \[[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask)\] = 32767, to: | bitfield | \[[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask)\] = 32767 ) |
| [RID](class_rid.md#class_RID) | [blas_create](class_renderingdevice.md#class_RenderingDevice_method_blas_create) ( vertex_array: [RID](class_rid.md#class_RID), index_array: [RID](class_rid.md#class_RID), geometry_bits: | bitfield | \[[AccelerationStructureGeometryBits](class_renderingdevice.md#enum_RenderingDevice_AccelerationStructureGeometryBits)\] = 0, position_attribute_location: [int](class_int.md#class_int) = 0 ) |
| Error | [buffer_clear](class_renderingdevice.md#class_RenderingDevice_method_buffer_clear) ( buffer: [RID](class_rid.md#class_RID), offset: [int](class_int.md#class_int), size_bytes: [int](class_int.md#class_int) ) |
| Error | [buffer_copy](class_renderingdevice.md#class_RenderingDevice_method_buffer_copy) ( src_buffer: [RID](class_rid.md#class_RID), dst_buffer: [RID](class_rid.md#class_RID), src_offset: [int](class_int.md#class_int), dst_offset: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [buffer_get_data](class_renderingdevice.md#class_RenderingDevice_method_buffer_get_data) ( buffer: [RID](class_rid.md#class_RID), offset_bytes: [int](class_int.md#class_int) = 0, size_bytes: [int](class_int.md#class_int) = 0 ) |
| Error | [buffer_get_data_async](class_renderingdevice.md#class_RenderingDevice_method_buffer_get_data_async) ( buffer: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable), offset_bytes: [int](class_int.md#class_int) = 0, size_bytes: [int](class_int.md#class_int) = 0 ) |
| [int](class_int.md#class_int) | [buffer_get_device_address](class_renderingdevice.md#class_RenderingDevice_method_buffer_get_device_address) ( buffer: [RID](class_rid.md#class_RID) ) |
| Error | [buffer_update](class_renderingdevice.md#class_RenderingDevice_method_buffer_update) ( buffer: [RID](class_rid.md#class_RID), offset: [int](class_int.md#class_int), size_bytes: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| void | [capture_timestamp](class_renderingdevice.md#class_RenderingDevice_method_capture_timestamp) ( name: [String](class_string.md#class_String) ) |
| void | [compute_list_add_barrier](class_renderingdevice.md#class_RenderingDevice_method_compute_list_add_barrier) ( compute_list: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [compute_list_begin](class_renderingdevice.md#class_RenderingDevice_method_compute_list_begin) ( ) |
| void | [compute_list_bind_compute_pipeline](class_renderingdevice.md#class_RenderingDevice_method_compute_list_bind_compute_pipeline) ( compute_list: [int](class_int.md#class_int), compute_pipeline: [RID](class_rid.md#class_RID) ) |
| void | [compute_list_bind_uniform_set](class_renderingdevice.md#class_RenderingDevice_method_compute_list_bind_uniform_set) ( compute_list: [int](class_int.md#class_int), uniform_set: [RID](class_rid.md#class_RID), set_index: [int](class_int.md#class_int) ) |
| void | [compute_list_dispatch](class_renderingdevice.md#class_RenderingDevice_method_compute_list_dispatch) ( compute_list: [int](class_int.md#class_int), x_groups: [int](class_int.md#class_int), y_groups: [int](class_int.md#class_int), z_groups: [int](class_int.md#class_int) ) |
| void | [compute_list_dispatch_indirect](class_renderingdevice.md#class_RenderingDevice_method_compute_list_dispatch_indirect) ( compute_list: [int](class_int.md#class_int), buffer: [RID](class_rid.md#class_RID), offset: [int](class_int.md#class_int) ) |
| void | [compute_list_end](class_renderingdevice.md#class_RenderingDevice_method_compute_list_end) ( ) |
| void | [compute_list_set_push_constant](class_renderingdevice.md#class_RenderingDevice_method_compute_list_set_push_constant) ( compute_list: [int](class_int.md#class_int), buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), size_bytes: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [compute_pipeline_create](class_renderingdevice.md#class_RenderingDevice_method_compute_pipeline_create) ( shader: [RID](class_rid.md#class_RID), specialization_constants: [Array](class_array.md#class_Array)\[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant)\] = [] ) |
| [bool](class_bool.md#class_bool) | [compute_pipeline_is_valid](class_renderingdevice.md#class_RenderingDevice_method_compute_pipeline_is_valid) ( compute_pipeline: [RID](class_rid.md#class_RID) ) |
| [RenderingDevice](class_renderingdevice.md#class_RenderingDevice) | [create_local_device](class_renderingdevice.md#class_RenderingDevice_method_create_local_device) ( ) |
| void | [draw_command_begin_label](class_renderingdevice.md#class_RenderingDevice_method_draw_command_begin_label) ( name: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color) ) |
| void | [draw_command_end_label](class_renderingdevice.md#class_RenderingDevice_method_draw_command_end_label) ( ) |
| void | [draw_command_insert_label](class_renderingdevice.md#class_RenderingDevice_method_draw_command_insert_label) ( name: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color) ) |
| [int](class_int.md#class_int) | [draw_list_begin](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin) ( framebuffer: [RID](class_rid.md#class_RID), draw_flags: | bitfield | \[[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags)\] = 0, clear_color_values: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) = PackedColorArray(), clear_depth_value: [float](class_float.md#class_float) = 1.0, clear_stencil_value: [int](class_int.md#class_int) = 0, region: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), breadcrumb: [int](class_int.md#class_int) = 0 ) |
| [int](class_int.md#class_int) | [draw_list_begin_for_screen](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin_for_screen) ( screen: [int](class_int.md#class_int) = 0, clear_color: [Color](class_color.md#class_Color) = Color(0, 0, 0, 1) ) |
| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [draw_list_begin_split](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin_split) ( framebuffer: [RID](class_rid.md#class_RID), splits: [int](class_int.md#class_int), initial_color_action: [InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction), final_color_action: [FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction), initial_depth_action: [InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction), final_depth_action: [FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction), clear_color_values: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) = PackedColorArray(), clear_depth: [float](class_float.md#class_float) = 1.0, clear_stencil: [int](class_int.md#class_int) = 0, region: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), storage_textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] = [] ) |
| void | [draw_list_bind_index_array](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_index_array) ( draw_list: [int](class_int.md#class_int), index_array: [RID](class_rid.md#class_RID) ) |
| void | [draw_list_bind_render_pipeline](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_render_pipeline) ( draw_list: [int](class_int.md#class_int), render_pipeline: [RID](class_rid.md#class_RID) ) |
| void | [draw_list_bind_uniform_set](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_uniform_set) ( draw_list: [int](class_int.md#class_int), uniform_set: [RID](class_rid.md#class_RID), set_index: [int](class_int.md#class_int) ) |
| void | [draw_list_bind_vertex_array](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_vertex_array) ( draw_list: [int](class_int.md#class_int), vertex_array: [RID](class_rid.md#class_RID) ) |
| void | [draw_list_bind_vertex_buffers_format](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_vertex_buffers_format) ( draw_list: [int](class_int.md#class_int), vertex_format: [int](class_int.md#class_int), vertex_count: [int](class_int.md#class_int), vertex_buffers: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], offsets: [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) = PackedInt64Array() ) |
| void | [draw_list_disable_scissor](class_renderingdevice.md#class_RenderingDevice_method_draw_list_disable_scissor) ( draw_list: [int](class_int.md#class_int) ) |
| void | [draw_list_draw](class_renderingdevice.md#class_RenderingDevice_method_draw_list_draw) ( draw_list: [int](class_int.md#class_int), use_indices: [bool](class_bool.md#class_bool), instances: [int](class_int.md#class_int), procedural_vertex_count: [int](class_int.md#class_int) = 0 ) |
| void | [draw_list_draw_indirect](class_renderingdevice.md#class_RenderingDevice_method_draw_list_draw_indirect) ( draw_list: [int](class_int.md#class_int), use_indices: [bool](class_bool.md#class_bool), buffer: [RID](class_rid.md#class_RID), offset: [int](class_int.md#class_int) = 0, draw_count: [int](class_int.md#class_int) = 1, stride: [int](class_int.md#class_int) = 0 ) |
| void | [draw_list_enable_scissor](class_renderingdevice.md#class_RenderingDevice_method_draw_list_enable_scissor) ( draw_list: [int](class_int.md#class_int), rect: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0) ) |
| void | [draw_list_end](class_renderingdevice.md#class_RenderingDevice_method_draw_list_end) ( ) |
| void | [draw_list_set_blend_constants](class_renderingdevice.md#class_RenderingDevice_method_draw_list_set_blend_constants) ( draw_list: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) |
| void | [draw_list_set_push_constant](class_renderingdevice.md#class_RenderingDevice_method_draw_list_set_push_constant) ( draw_list: [int](class_int.md#class_int), buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), size_bytes: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [draw_list_switch_to_next_pass](class_renderingdevice.md#class_RenderingDevice_method_draw_list_switch_to_next_pass) ( ) |
| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [draw_list_switch_to_next_pass_split](class_renderingdevice.md#class_RenderingDevice_method_draw_list_switch_to_next_pass_split) ( splits: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [framebuffer_create](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_create) ( textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], validate_with_format: [int](class_int.md#class_int) = -1, view_count: [int](class_int.md#class_int) = 1 ) |
| [RID](class_rid.md#class_RID) | [framebuffer_create_empty](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_create_empty) ( size: [Vector2i](class_vector2i.md#class_Vector2i), samples: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) = 0, validate_with_format: [int](class_int.md#class_int) = -1 ) |
| [RID](class_rid.md#class_RID) | [framebuffer_create_multipass](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_create_multipass) ( textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], passes: [Array](class_array.md#class_Array)\[[RDFramebufferPass](class_rdframebufferpass.md#class_RDFramebufferPass)\], validate_with_format: [int](class_int.md#class_int) = -1, view_count: [int](class_int.md#class_int) = 1 ) |
| [int](class_int.md#class_int) | [framebuffer_format_create](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_format_create) ( attachments: [Array](class_array.md#class_Array)\[[RDAttachmentFormat](class_rdattachmentformat.md#class_RDAttachmentFormat)\], view_count: [int](class_int.md#class_int) = 1 ) |
| [int](class_int.md#class_int) | [framebuffer_format_create_empty](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_format_create_empty) ( samples: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) = 0 ) |
| [int](class_int.md#class_int) | [framebuffer_format_create_multipass](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_format_create_multipass) ( attachments: [Array](class_array.md#class_Array)\[[RDAttachmentFormat](class_rdattachmentformat.md#class_RDAttachmentFormat)\], passes: [Array](class_array.md#class_Array)\[[RDFramebufferPass](class_rdframebufferpass.md#class_RDFramebufferPass)\], view_count: [int](class_int.md#class_int) = 1 ) |
| [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) | [framebuffer_format_get_texture_samples](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_format_get_texture_samples) ( format: [int](class_int.md#class_int), render_pass: [int](class_int.md#class_int) = 0 ) |
| [int](class_int.md#class_int) | [framebuffer_get_format](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_get_format) ( framebuffer: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [framebuffer_is_valid](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_is_valid) ( framebuffer: [RID](class_rid.md#class_RID) ) const |
| void | [free_rid](class_renderingdevice.md#class_RenderingDevice_method_free_rid) ( rid: [RID](class_rid.md#class_RID) ) |
| void | [full_barrier](class_renderingdevice.md#class_RenderingDevice_method_full_barrier) ( ) |
| [int](class_int.md#class_int) | [get_captured_timestamp_cpu_time](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_cpu_time) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_captured_timestamp_gpu_time](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_gpu_time) ( index: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_captured_timestamp_name](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_name) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_captured_timestamps_count](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamps_count) ( ) const |
| [int](class_int.md#class_int) | [get_captured_timestamps_frame](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamps_frame) ( ) const |
| [int](class_int.md#class_int) | [get_device_allocation_count](class_renderingdevice.md#class_RenderingDevice_method_get_device_allocation_count) ( ) const |
| [int](class_int.md#class_int) | [get_device_allocs_by_object_type](class_renderingdevice.md#class_RenderingDevice_method_get_device_allocs_by_object_type) ( type: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_device_memory_by_object_type](class_renderingdevice.md#class_RenderingDevice_method_get_device_memory_by_object_type) ( type: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_device_name](class_renderingdevice.md#class_RenderingDevice_method_get_device_name) ( ) const |
| [String](class_string.md#class_String) | [get_device_pipeline_cache_uuid](class_renderingdevice.md#class_RenderingDevice_method_get_device_pipeline_cache_uuid) ( ) const |
| [int](class_int.md#class_int) | [get_device_total_memory](class_renderingdevice.md#class_RenderingDevice_method_get_device_total_memory) ( ) const |
| [String](class_string.md#class_String) | [get_device_vendor_name](class_renderingdevice.md#class_RenderingDevice_method_get_device_vendor_name) ( ) const |
| [int](class_int.md#class_int) | [get_driver_allocation_count](class_renderingdevice.md#class_RenderingDevice_method_get_driver_allocation_count) ( ) const |
| [int](class_int.md#class_int) | [get_driver_allocs_by_object_type](class_renderingdevice.md#class_RenderingDevice_method_get_driver_allocs_by_object_type) ( type: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_driver_and_device_memory_report](class_renderingdevice.md#class_RenderingDevice_method_get_driver_and_device_memory_report) ( ) const |
| [int](class_int.md#class_int) | [get_driver_memory_by_object_type](class_renderingdevice.md#class_RenderingDevice_method_get_driver_memory_by_object_type) ( type: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_driver_resource](class_renderingdevice.md#class_RenderingDevice_method_get_driver_resource) ( resource: [DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource), rid: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_driver_total_memory](class_renderingdevice.md#class_RenderingDevice_method_get_driver_total_memory) ( ) const |
| [int](class_int.md#class_int) | [get_frame_delay](class_renderingdevice.md#class_RenderingDevice_method_get_frame_delay) ( ) const |
| [int](class_int.md#class_int) | [get_memory_usage](class_renderingdevice.md#class_RenderingDevice_method_get_memory_usage) ( type: [MemoryType](class_renderingdevice.md#enum_RenderingDevice_MemoryType) ) const |
| [String](class_string.md#class_String) | [get_perf_report](class_renderingdevice.md#class_RenderingDevice_method_get_perf_report) ( ) const |
| [String](class_string.md#class_String) | [get_tracked_object_name](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_name) ( type_index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_tracked_object_type_count](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_type_count) ( ) const |
| [bool](class_bool.md#class_bool) | [has_feature](class_renderingdevice.md#class_RenderingDevice_method_has_feature) ( feature: [Features](class_renderingdevice.md#enum_RenderingDevice_Features) ) const |
| [RID](class_rid.md#class_RID) | [index_array_create](class_renderingdevice.md#class_RenderingDevice_method_index_array_create) ( index_buffer: [RID](class_rid.md#class_RID), index_offset: [int](class_int.md#class_int), index_count: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [index_buffer_create](class_renderingdevice.md#class_RenderingDevice_method_index_buffer_create) ( size_indices: [int](class_int.md#class_int), format: [IndexBufferFormat](class_renderingdevice.md#enum_RenderingDevice_IndexBufferFormat), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray(), use_restart_indices: [bool](class_bool.md#class_bool) = false, creation_bits: | bitfield | \[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) |
| [int](class_int.md#class_int) | [limit_get](class_renderingdevice.md#class_RenderingDevice_method_limit_get) ( limit: [Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) ) const |
| [int](class_int.md#class_int) | [raytracing_list_begin](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_begin) ( ) |
| void | [raytracing_list_bind_raytracing_pipeline](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_bind_raytracing_pipeline) ( raytracing_list: [int](class_int.md#class_int), raytracing_pipeline: [RID](class_rid.md#class_RID) ) |
| void | [raytracing_list_bind_uniform_set](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_bind_uniform_set) ( raytracing_list: [int](class_int.md#class_int), uniform_set: [RID](class_rid.md#class_RID), set_index: [int](class_int.md#class_int) ) |
| void | [raytracing_list_end](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_end) ( ) |
| void | [raytracing_list_set_push_constant](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_set_push_constant) ( raytracing_list: [int](class_int.md#class_int), buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), size_bytes: [int](class_int.md#class_int) ) |
| void | [raytracing_list_trace_rays](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_trace_rays) ( raytracing_list: [int](class_int.md#class_int), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [raytracing_pipeline_create](class_renderingdevice.md#class_RenderingDevice_method_raytracing_pipeline_create) ( shader: [RID](class_rid.md#class_RID), specialization_constants: [Array](class_array.md#class_Array)\[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant)\] = [] ) |
| [bool](class_bool.md#class_bool) | [raytracing_pipeline_is_valid](class_renderingdevice.md#class_RenderingDevice_method_raytracing_pipeline_is_valid) ( raytracing_pipeline: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [render_pipeline_create](class_renderingdevice.md#class_RenderingDevice_method_render_pipeline_create) ( shader: [RID](class_rid.md#class_RID), framebuffer_format: [int](class_int.md#class_int), vertex_format: [int](class_int.md#class_int), primitive: [RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive), rasterization_state: [RDPipelineRasterizationState](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState), multisample_state: [RDPipelineMultisampleState](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState), stencil_state: [RDPipelineDepthStencilState](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState), color_blend_state: [RDPipelineColorBlendState](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState), dynamic_state_flags: | bitfield | \[[PipelineDynamicStateFlags](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags)\] = 0, for_render_pass: [int](class_int.md#class_int) = 0, specialization_constants: [Array](class_array.md#class_Array)\[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant)\] = [] ) |
| [bool](class_bool.md#class_bool) | [render_pipeline_is_valid](class_renderingdevice.md#class_RenderingDevice_method_render_pipeline_is_valid) ( render_pipeline: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [sampler_create](class_renderingdevice.md#class_RenderingDevice_method_sampler_create) ( state: [RDSamplerState](class_rdsamplerstate.md#class_RDSamplerState) ) |
| [bool](class_bool.md#class_bool) | [sampler_is_format_supported_for_filter](class_renderingdevice.md#class_RenderingDevice_method_sampler_is_format_supported_for_filter) ( format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), sampler_filter: [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) ) const |
| [int](class_int.md#class_int) | [screen_get_framebuffer_format](class_renderingdevice.md#class_RenderingDevice_method_screen_get_framebuffer_format) ( screen: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [screen_get_height](class_renderingdevice.md#class_RenderingDevice_method_screen_get_height) ( screen: [int](class_int.md#class_int) = 0 ) const |
| [int](class_int.md#class_int) | [screen_get_width](class_renderingdevice.md#class_RenderingDevice_method_screen_get_width) ( screen: [int](class_int.md#class_int) = 0 ) const |
| void | [set_resource_name](class_renderingdevice.md#class_RenderingDevice_method_set_resource_name) ( id: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [shader_compile_binary_from_spirv](class_renderingdevice.md#class_RenderingDevice_method_shader_compile_binary_from_spirv) ( spirv_data: [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV), name: [String](class_string.md#class_String) = "" ) |
| [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV) | [shader_compile_spirv_from_source](class_renderingdevice.md#class_RenderingDevice_method_shader_compile_spirv_from_source) ( shader_source: [RDShaderSource](class_rdshadersource.md#class_RDShaderSource), allow_cache: [bool](class_bool.md#class_bool) = true ) |
| [RID](class_rid.md#class_RID) | [shader_create_from_bytecode](class_renderingdevice.md#class_RenderingDevice_method_shader_create_from_bytecode) ( binary_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), placeholder_rid: [RID](class_rid.md#class_RID) = RID() ) |
| [RID](class_rid.md#class_RID) | [shader_create_from_spirv](class_renderingdevice.md#class_RenderingDevice_method_shader_create_from_spirv) ( spirv_data: [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV), name: [String](class_string.md#class_String) = "" ) |
| [RID](class_rid.md#class_RID) | [shader_create_placeholder](class_renderingdevice.md#class_RenderingDevice_method_shader_create_placeholder) ( ) |
| [int](class_int.md#class_int) | [shader_get_vertex_input_attribute_mask](class_renderingdevice.md#class_RenderingDevice_method_shader_get_vertex_input_attribute_mask) ( shader: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [storage_buffer_create](class_renderingdevice.md#class_RenderingDevice_method_storage_buffer_create) ( size_bytes: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray(), usage: | bitfield | \[[StorageBufferUsage](class_renderingdevice.md#enum_RenderingDevice_StorageBufferUsage)\] = 0, creation_bits: | bitfield | \[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) |
| void | [submit](class_renderingdevice.md#class_RenderingDevice_method_submit) ( ) |
| void | [sync](class_renderingdevice.md#class_RenderingDevice_method_sync) ( ) |
| [RID](class_rid.md#class_RID) | [texture_buffer_create](class_renderingdevice.md#class_RenderingDevice_method_texture_buffer_create) ( size_bytes: [int](class_int.md#class_int), format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray() ) |
| Error | [texture_clear](class_renderingdevice.md#class_RenderingDevice_method_texture_clear) ( texture: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color), base_mipmap: [int](class_int.md#class_int), mipmap_count: [int](class_int.md#class_int), base_layer: [int](class_int.md#class_int), layer_count: [int](class_int.md#class_int) ) |
| Error | [texture_copy](class_renderingdevice.md#class_RenderingDevice_method_texture_copy) ( from_texture: [RID](class_rid.md#class_RID), to_texture: [RID](class_rid.md#class_RID), from_pos: [Vector3](class_vector3.md#class_Vector3), to_pos: [Vector3](class_vector3.md#class_Vector3), size: [Vector3](class_vector3.md#class_Vector3), src_mipmap: [int](class_int.md#class_int), dst_mipmap: [int](class_int.md#class_int), src_layer: [int](class_int.md#class_int), dst_layer: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [texture_create](class_renderingdevice.md#class_RenderingDevice_method_texture_create) ( format: [RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat), view: [RDTextureView](class_rdtextureview.md#class_RDTextureView), data: [Array](class_array.md#class_Array)\[[PackedByteArray](class_packedbytearray.md#class_PackedByteArray)\] = [] ) |
| [RID](class_rid.md#class_RID) | [texture_create_from_extension](class_renderingdevice.md#class_RenderingDevice_method_texture_create_from_extension) ( type: [TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType), format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), samples: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples), usage_flags: | bitfield | \[[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits)\], image: [int](class_int.md#class_int), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), layers: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int) = 1 ) |
| [RID](class_rid.md#class_RID) | [texture_create_shared](class_renderingdevice.md#class_RenderingDevice_method_texture_create_shared) ( view: [RDTextureView](class_rdtextureview.md#class_RDTextureView), with_texture: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [texture_create_shared_from_slice](class_renderingdevice.md#class_RenderingDevice_method_texture_create_shared_from_slice) ( view: [RDTextureView](class_rdtextureview.md#class_RDTextureView), with_texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int), mipmap: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int) = 1, slice_type: [TextureSliceType](class_renderingdevice.md#enum_RenderingDevice_TextureSliceType) = 0 ) |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [texture_get_data](class_renderingdevice.md#class_RenderingDevice_method_texture_get_data) ( texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) |
| Error | [texture_get_data_async](class_renderingdevice.md#class_RenderingDevice_method_texture_get_data_async) ( texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) |
| [RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat) | [texture_get_format](class_renderingdevice.md#class_RenderingDevice_method_texture_get_format) ( texture: [RID](class_rid.md#class_RID) ) |
| [int](class_int.md#class_int) | [texture_get_native_handle](class_renderingdevice.md#class_RenderingDevice_method_texture_get_native_handle) ( texture: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [texture_is_discardable](class_renderingdevice.md#class_RenderingDevice_method_texture_is_discardable) ( texture: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [texture_is_format_supported_for_usage](class_renderingdevice.md#class_RenderingDevice_method_texture_is_format_supported_for_usage) ( format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), usage_flags: | bitfield | \[[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits)\] ) | const |
| [bool](class_bool.md#class_bool) | [texture_is_shared](class_renderingdevice.md#class_RenderingDevice_method_texture_is_shared) ( texture: [RID](class_rid.md#class_RID) ) |
| [bool](class_bool.md#class_bool) | [texture_is_valid](class_renderingdevice.md#class_RenderingDevice_method_texture_is_valid) ( texture: [RID](class_rid.md#class_RID) ) |
| Error | [texture_resolve_multisample](class_renderingdevice.md#class_RenderingDevice_method_texture_resolve_multisample) ( from_texture: [RID](class_rid.md#class_RID), to_texture: [RID](class_rid.md#class_RID) ) |
| void | [texture_set_discardable](class_renderingdevice.md#class_RenderingDevice_method_texture_set_discardable) ( texture: [RID](class_rid.md#class_RID), discardable: [bool](class_bool.md#class_bool) ) |
| Error | [texture_update](class_renderingdevice.md#class_RenderingDevice_method_texture_update) ( texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) |
| [RID](class_rid.md#class_RID) | [tlas_create](class_renderingdevice.md#class_RenderingDevice_method_tlas_create) ( instances_buffer: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [tlas_instances_buffer_create](class_renderingdevice.md#class_RenderingDevice_method_tlas_instances_buffer_create) ( instance_count: [int](class_int.md#class_int), creation_bits: | bitfield | \[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) |
| void | [tlas_instances_buffer_fill](class_renderingdevice.md#class_RenderingDevice_method_tlas_instances_buffer_fill) ( instances_buffer: [RID](class_rid.md#class_RID), blases: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], transforms: [Array](class_array.md#class_Array)\[[Transform3D](class_transform3d.md#class_Transform3D)\] ) |
| [RID](class_rid.md#class_RID) | [uniform_buffer_create](class_renderingdevice.md#class_RenderingDevice_method_uniform_buffer_create) ( size_bytes: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray(), creation_bits: | bitfield | \[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) |
| [RID](class_rid.md#class_RID) | [uniform_set_create](class_renderingdevice.md#class_RenderingDevice_method_uniform_set_create) ( uniforms: [Array](class_array.md#class_Array)\[[RDUniform](class_rduniform.md#class_RDUniform)\], shader: [RID](class_rid.md#class_RID), shader_set: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [uniform_set_is_valid](class_renderingdevice.md#class_RenderingDevice_method_uniform_set_is_valid) ( uniform_set: [RID](class_rid.md#class_RID) ) |
| [RID](class_rid.md#class_RID) | [vertex_array_create](class_renderingdevice.md#class_RenderingDevice_method_vertex_array_create) ( vertex_count: [int](class_int.md#class_int), vertex_format: [int](class_int.md#class_int), src_buffers: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], offsets: [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) = PackedInt64Array() ) |
| [RID](class_rid.md#class_RID) | [vertex_buffer_create](class_renderingdevice.md#class_RenderingDevice_method_vertex_buffer_create) ( size_bytes: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray(), creation_bits: | bitfield | \[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) |
| [int](class_int.md#class_int) | [vertex_format_create](class_renderingdevice.md#class_RenderingDevice_method_vertex_format_create) ( vertex_descriptions: [Array](class_array.md#class_Array)\[[RDVertexAttribute](class_rdvertexattribute.md#class_RDVertexAttribute)\] ) |

---

### Enumerations

<span id="enum_RenderingDevice_DeviceType"></span>

enum **DeviceType**: [🔗](class_renderingdevice.md#enum_RenderingDevice_DeviceType)

<span id="class_RenderingDevice_constant_DEVICE_TYPE_OTHER"></span>

[DeviceType](class_renderingdevice.md#enum_RenderingDevice_DeviceType) **DEVICE_TYPE_OTHER** = `0`

Rendering device type does not match any of the other enum values or is unknown.

<span id="class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU"></span>

[DeviceType](class_renderingdevice.md#enum_RenderingDevice_DeviceType) **DEVICE_TYPE_INTEGRATED_GPU** = `1`

Rendering device is an integrated GPU, which is typically *(but not always)* slower than dedicated GPUs ([DEVICE_TYPE_DISCRETE_GPU](class_renderingdevice.md#class_RenderingDevice_constant_DEVICE_TYPE_DISCRETE_GPU)). On Android and iOS, the rendering device type is always considered to be [DEVICE_TYPE_INTEGRATED_GPU](class_renderingdevice.md#class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU).

<span id="class_RenderingDevice_constant_DEVICE_TYPE_DISCRETE_GPU"></span>

[DeviceType](class_renderingdevice.md#enum_RenderingDevice_DeviceType) **DEVICE_TYPE_DISCRETE_GPU** = `2`

Rendering device is a dedicated GPU, which is typically *(but not always)* faster than integrated GPUs ([DEVICE_TYPE_INTEGRATED_GPU](class_renderingdevice.md#class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU)).

<span id="class_RenderingDevice_constant_DEVICE_TYPE_VIRTUAL_GPU"></span>

[DeviceType](class_renderingdevice.md#enum_RenderingDevice_DeviceType) **DEVICE_TYPE_VIRTUAL_GPU** = `3`

Rendering device is an emulated GPU in a virtual environment. This is typically much slower than the host GPU, which means the expected performance level on a dedicated GPU will be roughly equivalent to [DEVICE_TYPE_INTEGRATED_GPU](class_renderingdevice.md#class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU). Virtual machine GPU passthrough (such as VFIO) will not report the device type as [DEVICE_TYPE_VIRTUAL_GPU](class_renderingdevice.md#class_RenderingDevice_constant_DEVICE_TYPE_VIRTUAL_GPU). Instead, the host GPU's device type will be reported as if the GPU was not emulated.

<span id="class_RenderingDevice_constant_DEVICE_TYPE_CPU"></span>

[DeviceType](class_renderingdevice.md#enum_RenderingDevice_DeviceType) **DEVICE_TYPE_CPU** = `4`

Rendering device is provided by software emulation (such as Lavapipe or SwiftShader). This is the slowest kind of rendering device available; it's typically much slower than [DEVICE_TYPE_INTEGRATED_GPU](class_renderingdevice.md#class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU).

<span id="class_RenderingDevice_constant_DEVICE_TYPE_MAX"></span>

[DeviceType](class_renderingdevice.md#enum_RenderingDevice_DeviceType) **DEVICE_TYPE_MAX** = `5`

Represents the size of the [DeviceType](class_renderingdevice.md#enum_RenderingDevice_DeviceType) enum.

---

<span id="enum_RenderingDevice_DriverResource"></span>

enum **DriverResource**: [🔗](class_renderingdevice.md#enum_RenderingDevice_DriverResource)

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_LOGICAL_DEVICE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_LOGICAL_DEVICE** = `0`

Specific device object based on a physical device (`rid` parameter is ignored).

- Vulkan: Vulkan device driver resource (`VkDevice`).

- D3D12: D3D12 device driver resource (`ID3D12Device`).

- Metal: Metal device driver resource (`MTLDevice`).

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_PHYSICAL_DEVICE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_PHYSICAL_DEVICE** = `1`

Physical device the specific logical device is based on (`rid` parameter is ignored).

- Vulkan: `VkPhysicalDevice`.

- D3D12: `IDXGIAdapter`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_TOPMOST_OBJECT"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_TOPMOST_OBJECT** = `2`

Top-most graphics API entry object (`rid` parameter is ignored).

- Vulkan: `VkInstance`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_COMMAND_QUEUE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_COMMAND_QUEUE** = `3`

The main graphics-compute command queue (`rid` parameter is ignored).

- Vulkan: `VkQueue`.

- D3D12: `ID3D12CommandQueue`.

- Metal: `MTLCommandQueue`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_QUEUE_FAMILY"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_QUEUE_FAMILY** = `4`

The specific family the main queue belongs to (`rid` parameter is ignored).

- Vulkan: The queue family index, a `uint32_t`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_TEXTURE** = `5`

- Vulkan: `VkImage`.

- D3D12: `ID3D12Resource`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE_VIEW"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_TEXTURE_VIEW** = `6`

The view of an owned or shared texture.

- Vulkan: `VkImageView`.

- D3D12: `ID3D12Resource`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE_DATA_FORMAT"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_TEXTURE_DATA_FORMAT** = `7`

The native id of the data format of the texture.

- Vulkan: `VkFormat`.

- D3D12: `DXGI_FORMAT`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_SAMPLER"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_SAMPLER** = `8`

- Vulkan: `VkSampler`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_UNIFORM_SET"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_UNIFORM_SET** = `9`

- Vulkan: `VkDescriptorSet`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_BUFFER"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_BUFFER** = `10`

Buffer of any kind of (storage, vertex, etc.).

- Vulkan: `VkBuffer`.

- D3D12: `ID3D12Resource`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_COMPUTE_PIPELINE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_COMPUTE_PIPELINE** = `11`

- Vulkan: `VkPipeline`.

- Metal: `MTLComputePipelineState`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_RENDER_PIPELINE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_RENDER_PIPELINE** = `12`

- Vulkan: `VkPipeline`.

- Metal: `MTLRenderPipelineState`.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_DEVICE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_DEVICE** = `0`

**Deprecated:** Use [DRIVER_RESOURCE_LOGICAL_DEVICE](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_LOGICAL_DEVICE) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_PHYSICAL_DEVICE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_PHYSICAL_DEVICE** = `1`

**Deprecated:** Use [DRIVER_RESOURCE_PHYSICAL_DEVICE](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_PHYSICAL_DEVICE) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_INSTANCE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_INSTANCE** = `2`

**Deprecated:** Use [DRIVER_RESOURCE_TOPMOST_OBJECT](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_TOPMOST_OBJECT) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_QUEUE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_QUEUE** = `3`

**Deprecated:** Use [DRIVER_RESOURCE_COMMAND_QUEUE](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_COMMAND_QUEUE) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_QUEUE_FAMILY_INDEX"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_QUEUE_FAMILY_INDEX** = `4`

**Deprecated:** Use [DRIVER_RESOURCE_QUEUE_FAMILY](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_QUEUE_FAMILY) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_IMAGE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_IMAGE** = `5`

**Deprecated:** Use [DRIVER_RESOURCE_TEXTURE](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_IMAGE_VIEW"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_IMAGE_VIEW** = `6`

**Deprecated:** Use [DRIVER_RESOURCE_TEXTURE_VIEW](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE_VIEW) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_IMAGE_NATIVE_TEXTURE_FORMAT"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_IMAGE_NATIVE_TEXTURE_FORMAT** = `7`

**Deprecated:** Use [DRIVER_RESOURCE_TEXTURE_DATA_FORMAT](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE_DATA_FORMAT) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_SAMPLER"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_SAMPLER** = `8`

**Deprecated:** Use [DRIVER_RESOURCE_SAMPLER](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_SAMPLER) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_DESCRIPTOR_SET"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_DESCRIPTOR_SET** = `9`

**Deprecated:** Use [DRIVER_RESOURCE_UNIFORM_SET](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_UNIFORM_SET) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_BUFFER"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_BUFFER** = `10`

**Deprecated:** Use [DRIVER_RESOURCE_BUFFER](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_BUFFER) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_COMPUTE_PIPELINE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_COMPUTE_PIPELINE** = `11`

**Deprecated:** Use [DRIVER_RESOURCE_COMPUTE_PIPELINE](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_COMPUTE_PIPELINE) instead.

<span id="class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_RENDER_PIPELINE"></span>

[DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource) **DRIVER_RESOURCE_VULKAN_RENDER_PIPELINE** = `12`

**Deprecated:** Use [DRIVER_RESOURCE_RENDER_PIPELINE](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_RENDER_PIPELINE) instead.

---

<span id="enum_RenderingDevice_DataFormat"></span>

enum **DataFormat**: [🔗](class_renderingdevice.md#enum_RenderingDevice_DataFormat)

<span id="class_RenderingDevice_constant_DATA_FORMAT_R4G4_UNORM_PACK8"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R4G4_UNORM_PACK8** = `0`

4-bit-per-channel red/green channel data format, packed into 8 bits. Values are in the `[0.0, 1.0]` range.

 **Note:** More information on all data formats can be found on the Identification of formats section of the Vulkan specification, as well as the VkFormat enum.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R4G4B4A4_UNORM_PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R4G4B4A4_UNORM_PACK16** = `1`

4-bit-per-channel red/green/blue/alpha channel data format, packed into 16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B4G4R4A4_UNORM_PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B4G4R4A4_UNORM_PACK16** = `2`

4-bit-per-channel blue/green/red/alpha channel data format, packed into 16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R5G6B5_UNORM_PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R5G6B5_UNORM_PACK16** = `3`

Red/green/blue channel data format with 5 bits of red, 6 bits of green and 5 bits of blue, packed into 16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B5G6R5_UNORM_PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B5G6R5_UNORM_PACK16** = `4`

Blue/green/red channel data format with 5 bits of blue, 6 bits of green and 5 bits of red, packed into 16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R5G5B5A1_UNORM_PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R5G5B5A1_UNORM_PACK16** = `5`

Red/green/blue/alpha channel data format with 5 bits of red, 6 bits of green, 5 bits of blue and 1 bit of alpha, packed into 16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B5G5R5A1_UNORM_PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B5G5R5A1_UNORM_PACK16** = `6`

Blue/green/red/alpha channel data format with 5 bits of blue, 6 bits of green, 5 bits of red and 1 bit of alpha, packed into 16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A1R5G5B5_UNORM_PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A1R5G5B5_UNORM_PACK16** = `7`

Alpha/red/green/blue channel data format with 1 bit of alpha, 5 bits of red, 6 bits of green and 5 bits of blue, packed into 16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8_UNORM** = `8`

8-bit-per-channel unsigned floating-point red channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8_SNORM** = `9`

8-bit-per-channel signed floating-point red channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8_USCALED** = `10`

8-bit-per-channel unsigned floating-point red channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 255.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8_SSCALED** = `11`

8-bit-per-channel signed floating-point red channel data format with scaled value (value is converted from integer to float). Values are in the `[-127.0, 127.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8_UINT** = `12`

8-bit-per-channel unsigned integer red channel data format. Values are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8_SINT** = `13`

8-bit-per-channel signed integer red channel data format. Values are in the `[-127, 127]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8_SRGB"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8_SRGB** = `14`

8-bit-per-channel unsigned floating-point red channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8_UNORM** = `15`

8-bit-per-channel unsigned floating-point red/green channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8_SNORM** = `16`

8-bit-per-channel signed floating-point red/green channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8_USCALED** = `17`

8-bit-per-channel unsigned floating-point red/green channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 255.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8_SSCALED** = `18`

8-bit-per-channel signed floating-point red/green channel data format with scaled value (value is converted from integer to float). Values are in the `[-127.0, 127.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8_UINT** = `19`

8-bit-per-channel unsigned integer red/green channel data format. Values are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8_SINT** = `20`

8-bit-per-channel signed integer red/green channel data format. Values are in the `[-127, 127]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8_SRGB"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8_SRGB** = `21`

8-bit-per-channel unsigned floating-point red/green channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8_UNORM** = `22`

8-bit-per-channel unsigned floating-point red/green/blue channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8_SNORM** = `23`

8-bit-per-channel signed floating-point red/green/blue channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8_USCALED** = `24`

8-bit-per-channel unsigned floating-point red/green/blue channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 255.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8_SSCALED** = `25`

8-bit-per-channel signed floating-point red/green/blue channel data format with scaled value (value is converted from integer to float). Values are in the `[-127.0, 127.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8_UINT** = `26`

8-bit-per-channel unsigned integer red/green/blue channel data format. Values are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8_SINT** = `27`

8-bit-per-channel signed integer red/green/blue channel data format. Values are in the `[-127, 127]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_SRGB"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8_SRGB** = `28`

8-bit-per-channel unsigned floating-point red/green/blue channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8_UNORM** = `29`

8-bit-per-channel unsigned floating-point blue/green/red channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8_SNORM** = `30`

8-bit-per-channel signed floating-point blue/green/red channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8_USCALED** = `31`

8-bit-per-channel unsigned floating-point blue/green/red channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 255.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8_SSCALED** = `32`

8-bit-per-channel signed floating-point blue/green/red channel data format with scaled value (value is converted from integer to float). Values are in the `[-127.0, 127.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8_UINT** = `33`

8-bit-per-channel unsigned integer blue/green/red channel data format. Values are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8_SINT** = `34`

8-bit-per-channel signed integer blue/green/red channel data format. Values are in the `[-127, 127]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_SRGB"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8_SRGB** = `35`

8-bit-per-channel unsigned floating-point blue/green/red data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8A8_UNORM** = `36`

8-bit-per-channel unsigned floating-point red/green/blue/alpha channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8A8_SNORM** = `37`

8-bit-per-channel signed floating-point red/green/blue/alpha channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8A8_USCALED** = `38`

8-bit-per-channel unsigned floating-point red/green/blue/alpha channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 255.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8A8_SSCALED** = `39`

8-bit-per-channel signed floating-point red/green/blue/alpha channel data format with scaled value (value is converted from integer to float). Values are in the `[-127.0, 127.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8A8_UINT** = `40`

8-bit-per-channel unsigned integer red/green/blue/alpha channel data format. Values are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8A8_SINT** = `41`

8-bit-per-channel signed integer red/green/blue/alpha channel data format. Values are in the `[-127, 127]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_SRGB"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R8G8B8A8_SRGB** = `42`

8-bit-per-channel unsigned floating-point red/green/blue/alpha channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8A8_UNORM** = `43`

8-bit-per-channel unsigned floating-point blue/green/red/alpha channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8A8_SNORM** = `44`

8-bit-per-channel signed floating-point blue/green/red/alpha channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8A8_USCALED** = `45`

8-bit-per-channel unsigned floating-point blue/green/red/alpha channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 255.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8A8_SSCALED** = `46`

8-bit-per-channel signed floating-point blue/green/red/alpha channel data format with scaled value (value is converted from integer to float). Values are in the `[-127.0, 127.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8A8_UINT** = `47`

8-bit-per-channel unsigned integer blue/green/red/alpha channel data format. Values are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8A8_SINT** = `48`

8-bit-per-channel signed integer blue/green/red/alpha channel data format. Values are in the `[-127, 127]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_SRGB"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8A8_SRGB** = `49`

8-bit-per-channel unsigned floating-point blue/green/red/alpha channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_UNORM_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A8B8G8R8_UNORM_PACK32** = `50`

8-bit-per-channel unsigned floating-point alpha/red/green/blue channel data format with normalized value, packed in 32 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_SNORM_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A8B8G8R8_SNORM_PACK32** = `51`

8-bit-per-channel signed floating-point alpha/red/green/blue channel data format with normalized value, packed in 32 bits. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_USCALED_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A8B8G8R8_USCALED_PACK32** = `52`

8-bit-per-channel unsigned floating-point alpha/red/green/blue channel data format with scaled value (value is converted from integer to float), packed in 32 bits. Values are in the `[0.0, 255.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_SSCALED_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A8B8G8R8_SSCALED_PACK32** = `53`

8-bit-per-channel signed floating-point alpha/red/green/blue channel data format with scaled value (value is converted from integer to float), packed in 32 bits. Values are in the `[-127.0, 127.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_UINT_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A8B8G8R8_UINT_PACK32** = `54`

8-bit-per-channel unsigned integer alpha/red/green/blue channel data format, packed in 32 bits. Values are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_SINT_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A8B8G8R8_SINT_PACK32** = `55`

8-bit-per-channel signed integer alpha/red/green/blue channel data format, packed in 32 bits. Values are in the `[-127, 127]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_SRGB_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A8B8G8R8_SRGB_PACK32** = `56`

8-bit-per-channel unsigned floating-point alpha/red/green/blue channel data format with normalized value and nonlinear sRGB encoding, packed in 32 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_UNORM_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2R10G10B10_UNORM_PACK32** = `57`

Unsigned floating-point alpha/red/green/blue channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of red, 10 bits of green and 10 bits of blue. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_SNORM_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2R10G10B10_SNORM_PACK32** = `58`

Signed floating-point alpha/red/green/blue channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of red, 10 bits of green and 10 bits of blue. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_USCALED_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2R10G10B10_USCALED_PACK32** = `59`

Unsigned floating-point alpha/red/green/blue channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of red, 10 bits of green and 10 bits of blue. Values are in the `[0.0, 1023.0]` range for red/green/blue and `[0.0, 3.0]` for alpha.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_SSCALED_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2R10G10B10_SSCALED_PACK32** = `60`

Signed floating-point alpha/red/green/blue channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of red, 10 bits of green and 10 bits of blue. Values are in the `[-511.0, 511.0]` range for red/green/blue and `[-1.0, 1.0]` for alpha.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_UINT_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2R10G10B10_UINT_PACK32** = `61`

Unsigned integer alpha/red/green/blue channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of red, 10 bits of green and 10 bits of blue. Values are in the `[0, 1023]` range for red/green/blue and `[0, 3]` for alpha.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_SINT_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2R10G10B10_SINT_PACK32** = `62`

Signed integer alpha/red/green/blue channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of red, 10 bits of green and 10 bits of blue. Values are in the `[-511, 511]` range for red/green/blue and `[-1, 1]` for alpha.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_UNORM_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2B10G10R10_UNORM_PACK32** = `63`

Unsigned floating-point alpha/blue/green/red channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of blue, 10 bits of green and 10 bits of red. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_SNORM_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2B10G10R10_SNORM_PACK32** = `64`

Signed floating-point alpha/blue/green/red channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of blue, 10 bits of green and 10 bits of red. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_USCALED_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2B10G10R10_USCALED_PACK32** = `65`

Unsigned floating-point alpha/blue/green/red channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of blue, 10 bits of green and 10 bits of red. Values are in the `[0.0, 1023.0]` range for blue/green/red and `[0.0, 3.0]` for alpha.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_SSCALED_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2B10G10R10_SSCALED_PACK32** = `66`

Signed floating-point alpha/blue/green/red channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of blue, 10 bits of green and 10 bits of red. Values are in the `[-511.0, 511.0]` range for blue/green/red and `[-1.0, 1.0]` for alpha.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_UINT_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2B10G10R10_UINT_PACK32** = `67`

Unsigned integer alpha/blue/green/red channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of blue, 10 bits of green and 10 bits of red. Values are in the `[0, 1023]` range for blue/green/red and `[0, 3]` for alpha.

<span id="class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_SINT_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_A2B10G10R10_SINT_PACK32** = `68`

Signed integer alpha/blue/green/red channel data format with normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of blue, 10 bits of green and 10 bits of red. Values are in the `[-511, 511]` range for blue/green/red and `[-1, 1]` for alpha.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16_UNORM** = `69`

16-bit-per-channel unsigned floating-point red channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16_SNORM** = `70`

16-bit-per-channel signed floating-point red channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16_USCALED** = `71`

16-bit-per-channel unsigned floating-point red channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 65535.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16_SSCALED** = `72`

16-bit-per-channel signed floating-point red channel data format with scaled value (value is converted from integer to float). Values are in the `[-32767.0, 32767.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16_UINT** = `73`

16-bit-per-channel unsigned integer red channel data format. Values are in the `[0.0, 65535]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16_SINT** = `74`

16-bit-per-channel signed integer red channel data format. Values are in the `[-32767, 32767]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16_SFLOAT** = `75`

16-bit-per-channel signed floating-point red channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16_UNORM** = `76`

16-bit-per-channel unsigned floating-point red/green channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16_SNORM** = `77`

16-bit-per-channel signed floating-point red/green channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16_USCALED** = `78`

16-bit-per-channel unsigned floating-point red/green channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 65535.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16_SSCALED** = `79`

16-bit-per-channel signed floating-point red/green channel data format with scaled value (value is converted from integer to float). Values are in the `[-32767.0, 32767.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16_UINT** = `80`

16-bit-per-channel unsigned integer red/green channel data format. Values are in the `[0.0, 65535]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16_SINT** = `81`

16-bit-per-channel signed integer red/green channel data format. Values are in the `[-32767, 32767]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16_SFLOAT** = `82`

16-bit-per-channel signed floating-point red/green channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16_UNORM** = `83`

16-bit-per-channel unsigned floating-point red/green/blue channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16_SNORM** = `84`

16-bit-per-channel signed floating-point red/green/blue channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16_USCALED** = `85`

16-bit-per-channel unsigned floating-point red/green/blue channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 65535.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16_SSCALED** = `86`

16-bit-per-channel signed floating-point red/green/blue channel data format with scaled value (value is converted from integer to float). Values are in the `[-32767.0, 32767.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16_UINT** = `87`

16-bit-per-channel unsigned integer red/green/blue channel data format. Values are in the `[0.0, 65535]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16_SINT** = `88`

16-bit-per-channel signed integer red/green/blue channel data format. Values are in the `[-32767, 32767]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16_SFLOAT** = `89`

16-bit-per-channel signed floating-point red/green/blue channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16A16_UNORM** = `90`

16-bit-per-channel unsigned floating-point red/green/blue/alpha channel data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_SNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16A16_SNORM** = `91`

16-bit-per-channel signed floating-point red/green/blue/alpha channel data format with normalized value. Values are in the `[-1.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_USCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16A16_USCALED** = `92`

16-bit-per-channel unsigned floating-point red/green/blue/alpha channel data format with scaled value (value is converted from integer to float). Values are in the `[0.0, 65535.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_SSCALED"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16A16_SSCALED** = `93`

16-bit-per-channel signed floating-point red/green/blue/alpha channel data format with scaled value (value is converted from integer to float). Values are in the `[-32767.0, 32767.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16A16_UINT** = `94`

16-bit-per-channel unsigned integer red/green/blue/alpha channel data format. Values are in the `[0.0, 65535]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16A16_SINT** = `95`

16-bit-per-channel signed integer red/green/blue/alpha channel data format. Values are in the `[-32767, 32767]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R16G16B16A16_SFLOAT** = `96`

16-bit-per-channel signed floating-point red/green/blue/alpha channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32_UINT** = `97`

32-bit-per-channel unsigned integer red channel data format. Values are in the `[0, 2^32 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32_SINT** = `98`

32-bit-per-channel signed integer red channel data format. Values are in the `[2^31 + 1, 2^31 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32_SFLOAT** = `99`

32-bit-per-channel signed floating-point red channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32G32_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32G32_UINT** = `100`

32-bit-per-channel unsigned integer red/green channel data format. Values are in the `[0, 2^32 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32G32_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32G32_SINT** = `101`

32-bit-per-channel signed integer red/green channel data format. Values are in the `[2^31 + 1, 2^31 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32G32_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32G32_SFLOAT** = `102`

32-bit-per-channel signed floating-point red/green channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32G32B32_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32G32B32_UINT** = `103`

32-bit-per-channel unsigned integer red/green/blue channel data format. Values are in the `[0, 2^32 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32G32B32_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32G32B32_SINT** = `104`

32-bit-per-channel signed integer red/green/blue channel data format. Values are in the `[2^31 + 1, 2^31 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32G32B32_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32G32B32_SFLOAT** = `105`

32-bit-per-channel signed floating-point red/green/blue channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32G32B32A32_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32G32B32A32_UINT** = `106`

32-bit-per-channel unsigned integer red/green/blue/alpha channel data format. Values are in the `[0, 2^32 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32G32B32A32_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32G32B32A32_SINT** = `107`

32-bit-per-channel signed integer red/green/blue/alpha channel data format. Values are in the `[2^31 + 1, 2^31 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R32G32B32A32_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R32G32B32A32_SFLOAT** = `108`

32-bit-per-channel signed floating-point red/green/blue/alpha channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64_UINT** = `109`

64-bit-per-channel unsigned integer red channel data format. Values are in the `[0, 2^64 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64_SINT** = `110`

64-bit-per-channel signed integer red channel data format. Values are in the `[2^63 + 1, 2^63 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64_SFLOAT** = `111`

64-bit-per-channel signed floating-point red channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64G64_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64G64_UINT** = `112`

64-bit-per-channel unsigned integer red/green channel data format. Values are in the `[0, 2^64 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64G64_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64G64_SINT** = `113`

64-bit-per-channel signed integer red/green channel data format. Values are in the `[2^63 + 1, 2^63 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64G64_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64G64_SFLOAT** = `114`

64-bit-per-channel signed floating-point red/green channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64G64B64_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64G64B64_UINT** = `115`

64-bit-per-channel unsigned integer red/green/blue channel data format. Values are in the `[0, 2^64 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64G64B64_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64G64B64_SINT** = `116`

64-bit-per-channel signed integer red/green/blue channel data format. Values are in the `[2^63 + 1, 2^63 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64G64B64_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64G64B64_SFLOAT** = `117`

64-bit-per-channel signed floating-point red/green/blue channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64G64B64A64_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64G64B64A64_UINT** = `118`

64-bit-per-channel unsigned integer red/green/blue/alpha channel data format. Values are in the `[0, 2^64 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64G64B64A64_SINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64G64B64A64_SINT** = `119`

64-bit-per-channel signed integer red/green/blue/alpha channel data format. Values are in the `[2^63 + 1, 2^63 - 1]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R64G64B64A64_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R64G64B64A64_SFLOAT** = `120`

64-bit-per-channel signed floating-point red/green/blue/alpha channel data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B10G11R11_UFLOAT_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B10G11R11_UFLOAT_PACK32** = `121`

Unsigned floating-point blue/green/red data format with the value stored as-is, packed in 32 bits. The format's precision is 10 bits of blue channel, 11 bits of green channel and 11 bits of red channel.

<span id="class_RenderingDevice_constant_DATA_FORMAT_E5B9G9R9_UFLOAT_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_E5B9G9R9_UFLOAT_PACK32** = `122`

Unsigned floating-point exposure/blue/green/red data format with the value stored as-is, packed in 32 bits. The format's precision is 5 bits of exposure, 9 bits of blue channel, 9 bits of green channel and 9 bits of red channel.

<span id="class_RenderingDevice_constant_DATA_FORMAT_D16_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_D16_UNORM** = `123`

16-bit unsigned floating-point depth data format with normalized value. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_X8_D24_UNORM_PACK32"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_X8_D24_UNORM_PACK32** = `124`

24-bit unsigned floating-point depth data format with normalized value, plus 8 unused bits, packed in 32 bits. Values for depth are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_D32_SFLOAT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_D32_SFLOAT** = `125`

32-bit signed floating-point depth data format with the value stored as-is.

<span id="class_RenderingDevice_constant_DATA_FORMAT_S8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_S8_UINT** = `126`

8-bit unsigned integer stencil data format.

<span id="class_RenderingDevice_constant_DATA_FORMAT_D16_UNORM_S8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_D16_UNORM_S8_UINT** = `127`

16-bit unsigned floating-point depth data format with normalized value, plus 8 bits of stencil in unsigned integer format. Values for depth are in the `[0.0, 1.0]` range. Values for stencil are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_D24_UNORM_S8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_D24_UNORM_S8_UINT** = `128`

24-bit unsigned floating-point depth data format with normalized value, plus 8 bits of stencil in unsigned integer format. Values for depth are in the `[0.0, 1.0]` range. Values for stencil are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_D32_SFLOAT_S8_UINT"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_D32_SFLOAT_S8_UINT** = `129`

32-bit signed floating-point depth data format with the value stored as-is, plus 8 bits of stencil in unsigned integer format. Values for stencil are in the `[0, 255]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC1_RGB_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC1_RGB_UNORM_BLOCK** = `130`

VRAM-compressed unsigned red/green/blue channel data format with normalized value. Values are in the `[0.0, 1.0]` range. The format's precision is 5 bits of red channel, 6 bits of green channel and 5 bits of blue channel. Using BC1 texture compression (also known as S3TC DXT1).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC1_RGB_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC1_RGB_SRGB_BLOCK** = `131`

VRAM-compressed unsigned red/green/blue channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range. The format's precision is 5 bits of red channel, 6 bits of green channel, and 5 bits of blue channel. Using BC1 texture compression (also known as S3TC DXT1).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC1_RGBA_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC1_RGBA_UNORM_BLOCK** = `132`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value. Values are in the `[0.0, 1.0]` range. The format's precision is 5 bits of red channel, 6 bits of green channel, 5 bits of blue channel and 1 bit of alpha channel. Using BC1 texture compression (also known as S3TC DXT1).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC1_RGBA_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC1_RGBA_SRGB_BLOCK** = `133`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range. The format's precision is 5 bits of red channel, 6 bits of green channel, 5 bits of blue channel, and 1 bit of alpha channel. Using BC1 texture compression (also known as S3TC DXT1).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC2_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC2_UNORM_BLOCK** = `134`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value. Values are in the `[0.0, 1.0]` range. The format's precision is 5 bits of red channel, 6 bits of green channel, 5 bits of blue channel and 4 bits of alpha channel. Using BC2 texture compression (also known as S3TC DXT3).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC2_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC2_SRGB_BLOCK** = `135`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range. The format's precision is 5 bits of red channel, 6 bits of green channel, 5 bits of blue channel, and 4 bits of alpha channel. Using BC2 texture compression (also known as S3TC DXT3).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC3_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC3_UNORM_BLOCK** = `136`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value. Values are in the `[0.0, 1.0]` range. The format's precision is 5 bits of red channel, 6 bits of green channel, 5 bits of blue channel and 8 bits of alpha channel. Using BC3 texture compression (also known as S3TC DXT5).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC3_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC3_SRGB_BLOCK** = `137`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range. The format's precision is 5 bits of red channel, 6 bits of green channel, 5 bits of blue channel, and 8 bits of alpha channel. Using BC3 texture compression (also known as S3TC DXT5).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC4_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC4_UNORM_BLOCK** = `138`

VRAM-compressed unsigned red channel data format with normalized value. Values are in the `[0.0, 1.0]` range. The format's precision is 8 bits of red channel. Using BC4 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC4_SNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC4_SNORM_BLOCK** = `139`

VRAM-compressed signed red channel data format with normalized value. Values are in the `[-1.0, 1.0]` range. The format's precision is 8 bits of red channel. Using BC4 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC5_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC5_UNORM_BLOCK** = `140`

VRAM-compressed unsigned red/green channel data format with normalized value. Values are in the `[0.0, 1.0]` range. The format's precision is 8 bits of red channel and 8 bits of green channel. Using BC5 texture compression (also known as S3TC RGTC).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC5_SNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC5_SNORM_BLOCK** = `141`

VRAM-compressed signed red/green channel data format with normalized value. Values are in the `[-1.0, 1.0]` range. The format's precision is 8 bits of red channel and 8 bits of green channel. Using BC5 texture compression (also known as S3TC RGTC).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC6H_UFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC6H_UFLOAT_BLOCK** = `142`

VRAM-compressed unsigned red/green/blue channel data format with the floating-point value stored as-is. The format's precision is between 10 and 13 bits for the red/green/blue channels. Using BC6H texture compression (also known as BPTC HDR).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC6H_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC6H_SFLOAT_BLOCK** = `143`

VRAM-compressed signed red/green/blue channel data format with the floating-point value stored as-is. The format's precision is between 10 and 13 bits for the red/green/blue channels. Using BC6H texture compression (also known as BPTC HDR).

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC7_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC7_UNORM_BLOCK** = `144`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value. Values are in the `[0.0, 1.0]` range. The format's precision is between 4 and 7 bits for the red/green/blue channels and between 0 and 8 bits for the alpha channel. Also known as BPTC LDR.

<span id="class_RenderingDevice_constant_DATA_FORMAT_BC7_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_BC7_SRGB_BLOCK** = `145`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range. The format's precision is between 4 and 7 bits for the red/green/blue channels and between 0 and 8 bits for the alpha channel. Also known as BPTC LDR.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ETC2_R8G8B8_UNORM_BLOCK** = `146`

VRAM-compressed unsigned red/green/blue channel data format with normalized value. Values are in the `[0.0, 1.0]` range. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ETC2_R8G8B8_SRGB_BLOCK** = `147`

VRAM-compressed unsigned red/green/blue channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8A1_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ETC2_R8G8B8A1_UNORM_BLOCK** = `148`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value. Values are in the `[0.0, 1.0]` range. Red/green/blue use 8 bit of precision each, with alpha using 1 bit of precision. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8A1_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ETC2_R8G8B8A1_SRGB_BLOCK** = `149`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range. Red/green/blue use 8 bit of precision each, with alpha using 1 bit of precision. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8A8_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ETC2_R8G8B8A8_UNORM_BLOCK** = `150`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value. Values are in the `[0.0, 1.0]` range. Red/green/blue use 8 bits of precision each, with alpha using 8 bits of precision. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8A8_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ETC2_R8G8B8A8_SRGB_BLOCK** = `151`

VRAM-compressed unsigned red/green/blue/alpha channel data format with normalized value and nonlinear sRGB encoding. Values are in the `[0.0, 1.0]` range. Red/green/blue use 8 bits of precision each, with alpha using 8 bits of precision. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_EAC_R11_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_EAC_R11_UNORM_BLOCK** = `152`

11-bit VRAM-compressed unsigned red channel data format with normalized value. Values are in the `[0.0, 1.0]` range. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_EAC_R11_SNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_EAC_R11_SNORM_BLOCK** = `153`

11-bit VRAM-compressed signed red channel data format with normalized value. Values are in the `[-1.0, 1.0]` range. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_EAC_R11G11_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_EAC_R11G11_UNORM_BLOCK** = `154`

11-bit VRAM-compressed unsigned red/green channel data format with normalized value. Values are in the `[0.0, 1.0]` range. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_EAC_R11G11_SNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_EAC_R11G11_SNORM_BLOCK** = `155`

11-bit VRAM-compressed signed red/green channel data format with normalized value. Values are in the `[-1.0, 1.0]` range. Using ETC2 texture compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_4x4_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_4x4_UNORM_BLOCK** = `156`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 4×4 blocks (highest quality). Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_4x4_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_4x4_SRGB_BLOCK** = `157`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 4×4 blocks (highest quality). Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x4_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_5x4_UNORM_BLOCK** = `158`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 5×4 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x4_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_5x4_SRGB_BLOCK** = `159`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 5×4 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x5_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_5x5_UNORM_BLOCK** = `160`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 5×5 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x5_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_5x5_SRGB_BLOCK** = `161`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 5×5 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x5_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_6x5_UNORM_BLOCK** = `162`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 6×5 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x5_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_6x5_SRGB_BLOCK** = `163`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 6×5 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x6_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_6x6_UNORM_BLOCK** = `164`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 6×6 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x6_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_6x6_SRGB_BLOCK** = `165`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 6×6 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x5_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_8x5_UNORM_BLOCK** = `166`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 8×5 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x5_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_8x5_SRGB_BLOCK** = `167`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 8×5 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x6_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_8x6_UNORM_BLOCK** = `168`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 8×6 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x6_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_8x6_SRGB_BLOCK** = `169`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 8×6 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x8_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_8x8_UNORM_BLOCK** = `170`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 8×8 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x8_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_8x8_SRGB_BLOCK** = `171`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 8×8 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x5_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x5_UNORM_BLOCK** = `172`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 10×5 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x5_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x5_SRGB_BLOCK** = `173`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 10×5 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x6_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x6_UNORM_BLOCK** = `174`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 10×6 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x6_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x6_SRGB_BLOCK** = `175`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 10×6 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x8_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x8_UNORM_BLOCK** = `176`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 10×8 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x8_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x8_SRGB_BLOCK** = `177`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 10×8 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x10_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x10_UNORM_BLOCK** = `178`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 10×10 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x10_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x10_SRGB_BLOCK** = `179`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 10×10 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x10_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_12x10_UNORM_BLOCK** = `180`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 12×10 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x10_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_12x10_SRGB_BLOCK** = `181`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 12×10 blocks. Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x12_UNORM_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_12x12_UNORM_BLOCK** = `182`

VRAM-compressed unsigned floating-point data format with normalized value, packed in 12 blocks (lowest quality). Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x12_SRGB_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_12x12_SRGB_BLOCK** = `183`

VRAM-compressed unsigned floating-point data format with normalized value and nonlinear sRGB encoding, packed in 12 blocks (lowest quality). Values are in the `[0.0, 1.0]` range. Using ASTC compression.

<span id="class_RenderingDevice_constant_DATA_FORMAT_G8B8G8R8_422_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G8B8G8R8_422_UNORM** = `184`

8-bit-per-channel unsigned floating-point green/blue/red channel data format with normalized value. Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_B8G8R8G8_422_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B8G8R8G8_422_UNORM** = `185`

8-bit-per-channel unsigned floating-point blue/green/red channel data format with normalized value. Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G8_B8_R8_3PLANE_420_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G8_B8_R8_3PLANE_420_UNORM** = `186`

8-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, stored across 3 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G8_B8R8_2PLANE_420_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G8_B8R8_2PLANE_420_UNORM** = `187`

8-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, stored across 2 separate planes (green + blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G8_B8_R8_3PLANE_422_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G8_B8_R8_3PLANE_422_UNORM** = `188`

8-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, stored across 2 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G8_B8R8_2PLANE_422_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G8_B8R8_2PLANE_422_UNORM** = `189`

8-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, stored across 2 separate planes (green + blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G8_B8_R8_3PLANE_444_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G8_B8_R8_3PLANE_444_UNORM** = `190`

8-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, stored across 3 separate planes. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R10X6_UNORM_PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R10X6_UNORM_PACK16** = `191`

10-bit-per-channel unsigned floating-point red channel data with normalized value, plus 6 unused bits, packed in 16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R10X6G10X6_UNORM_2PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R10X6G10X6_UNORM_2PACK16** = `192`

10-bit-per-channel unsigned floating-point red/green channel data with normalized value, plus 6 unused bits after each channel, packed in 2×16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R10X6G10X6B10X6A10X6_UNORM_4PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R10X6G10X6B10X6A10X6_UNORM_4PACK16** = `193`

10-bit-per-channel unsigned floating-point red/green/blue/alpha channel data with normalized value, plus 6 unused bits after each channel, packed in 4×16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_G10X6B10X6G10X6R10X6_422_UNORM_4PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G10X6B10X6G10X6R10X6_422_UNORM_4PACK16** = `194`

10-bit-per-channel unsigned floating-point green/blue/green/red channel data with normalized value, plus 6 unused bits after each channel, packed in 4×16 bits. Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel). The green channel is listed twice, but contains different values to allow it to be represented at full resolution.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B10X6G10X6R10X6G10X6_422_UNORM_4PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B10X6G10X6R10X6G10X6_422_UNORM_4PACK16** = `195`

10-bit-per-channel unsigned floating-point blue/green/red/green channel data with normalized value, plus 6 unused bits after each channel, packed in 4×16 bits. Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel). The green channel is listed twice, but contains different values to allow it to be represented at full resolution.

<span id="class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_420_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_420_UNORM_3PACK16** = `196`

10-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 2 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16** = `197`

10-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 2 separate planes (green + blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_422_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_422_UNORM_3PACK16** = `198`

10-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 3 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_422_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_422_UNORM_3PACK16** = `199`

10-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 3 separate planes (green + blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_444_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_444_UNORM_3PACK16** = `200`

10-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 3 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R12X4_UNORM_PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R12X4_UNORM_PACK16** = `201`

12-bit-per-channel unsigned floating-point red channel data with normalized value, plus 6 unused bits, packed in 16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R12X4G12X4_UNORM_2PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R12X4G12X4_UNORM_2PACK16** = `202`

12-bit-per-channel unsigned floating-point red/green channel data with normalized value, plus 6 unused bits after each channel, packed in 2×16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_R12X4G12X4B12X4A12X4_UNORM_4PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_R12X4G12X4B12X4A12X4_UNORM_4PACK16** = `203`

12-bit-per-channel unsigned floating-point red/green/blue/alpha channel data with normalized value, plus 6 unused bits after each channel, packed in 4×16 bits. Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_G12X4B12X4G12X4R12X4_422_UNORM_4PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G12X4B12X4G12X4R12X4_422_UNORM_4PACK16** = `204`

12-bit-per-channel unsigned floating-point green/blue/green/red channel data with normalized value, plus 6 unused bits after each channel, packed in 4×16 bits. Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel). The green channel is listed twice, but contains different values to allow it to be represented at full resolution.

<span id="class_RenderingDevice_constant_DATA_FORMAT_B12X4G12X4R12X4G12X4_422_UNORM_4PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B12X4G12X4R12X4G12X4_422_UNORM_4PACK16** = `205`

12-bit-per-channel unsigned floating-point blue/green/red/green channel data with normalized value, plus 6 unused bits after each channel, packed in 4×16 bits. Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel). The green channel is listed twice, but contains different values to allow it to be represented at full resolution.

<span id="class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_420_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_420_UNORM_3PACK16** = `206`

12-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 2 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_420_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_420_UNORM_3PACK16** = `207`

12-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 2 separate planes (green + blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_422_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_422_UNORM_3PACK16** = `208`

12-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 3 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_422_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_422_UNORM_3PACK16** = `209`

12-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 3 separate planes (green + blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_444_UNORM_3PACK16"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_444_UNORM_3PACK16** = `210`

12-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Packed in 3×16 bits and stored across 3 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_G16B16G16R16_422_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G16B16G16R16_422_UNORM** = `211`

16-bit-per-channel unsigned floating-point green/blue/red channel data format with normalized value. Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_B16G16R16G16_422_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_B16G16R16G16_422_UNORM** = `212`

16-bit-per-channel unsigned floating-point blue/green/red channel data format with normalized value. Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G16_B16_R16_3PLANE_420_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G16_B16_R16_3PLANE_420_UNORM** = `213`

16-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Stored across 2 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G16_B16R16_2PLANE_420_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G16_B16R16_2PLANE_420_UNORM** = `214`

16-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Stored across 2 separate planes (green + blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G16_B16_R16_3PLANE_422_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G16_B16_R16_3PLANE_422_UNORM** = `215`

16-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Stored across 3 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G16_B16R16_2PLANE_422_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G16_B16R16_2PLANE_422_UNORM** = `216`

16-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Stored across 3 separate planes (green + blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is stored at halved horizontal resolution (i.e. 2 horizontally adjacent pixels will share the same value for the blue/red channel).

<span id="class_RenderingDevice_constant_DATA_FORMAT_G16_B16_R16_3PLANE_444_UNORM"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_G16_B16_R16_3PLANE_444_UNORM** = `217`

16-bit-per-channel unsigned floating-point green/blue/red channel data with normalized value, plus 6 unused bits after each channel. Stored across 3 separate planes (green + blue + red). Values are in the `[0.0, 1.0]` range.

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_4x4_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_4x4_SFLOAT_BLOCK** = `218`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x4_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_5x4_SFLOAT_BLOCK** = `219`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x5_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_5x5_SFLOAT_BLOCK** = `220`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x5_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_6x5_SFLOAT_BLOCK** = `221`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x6_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_6x6_SFLOAT_BLOCK** = `222`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x5_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_8x5_SFLOAT_BLOCK** = `223`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x6_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_8x6_SFLOAT_BLOCK** = `224`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x8_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_8x8_SFLOAT_BLOCK** = `225`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x5_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x5_SFLOAT_BLOCK** = `226`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x6_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x6_SFLOAT_BLOCK** = `227`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x8_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x8_SFLOAT_BLOCK** = `228`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x10_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_10x10_SFLOAT_BLOCK** = `229`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x10_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_12x10_SFLOAT_BLOCK** = `230`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x12_SFLOAT_BLOCK"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_ASTC_12x12_SFLOAT_BLOCK** = `231`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DATA_FORMAT_MAX"></span>

[DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) **DATA_FORMAT_MAX** = `232`

Represents the size of the [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat) enum.

---

<span id="enum_RenderingDevice_BarrierMask"></span>

flags **BarrierMask**: [🔗](class_renderingdevice.md#enum_RenderingDevice_BarrierMask)

<span id="class_RenderingDevice_constant_BARRIER_MASK_VERTEX"></span>

[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask) **BARRIER_MASK_VERTEX** = `1`

Vertex shader barrier mask.

<span id="class_RenderingDevice_constant_BARRIER_MASK_FRAGMENT"></span>

[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask) **BARRIER_MASK_FRAGMENT** = `8`

Fragment shader barrier mask.

<span id="class_RenderingDevice_constant_BARRIER_MASK_COMPUTE"></span>

[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask) **BARRIER_MASK_COMPUTE** = `2`

Compute barrier mask.

<span id="class_RenderingDevice_constant_BARRIER_MASK_TRANSFER"></span>

[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask) **BARRIER_MASK_TRANSFER** = `4`

Transfer barrier mask.

<span id="class_RenderingDevice_constant_BARRIER_MASK_RASTER"></span>

[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask) **BARRIER_MASK_RASTER** = `9`

Raster barrier mask (vertex and fragment). Equivalent to `BARRIER_MASK_VERTEX | BARRIER_MASK_FRAGMENT`.

<span id="class_RenderingDevice_constant_BARRIER_MASK_ALL_BARRIERS"></span>

[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask) **BARRIER_MASK_ALL_BARRIERS** = `32767`

Barrier mask for all types (vertex, fragment, compute, transfer).

<span id="class_RenderingDevice_constant_BARRIER_MASK_NO_BARRIER"></span>

[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask) **BARRIER_MASK_NO_BARRIER** = `32768`

No barrier for any type.

---

<span id="enum_RenderingDevice_TextureType"></span>

enum **TextureType**: [🔗](class_renderingdevice.md#enum_RenderingDevice_TextureType)

<span id="class_RenderingDevice_constant_TEXTURE_TYPE_1D"></span>

[TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **TEXTURE_TYPE_1D** = `0`

1-dimensional texture.

<span id="class_RenderingDevice_constant_TEXTURE_TYPE_2D"></span>

[TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **TEXTURE_TYPE_2D** = `1`

2-dimensional texture.

<span id="class_RenderingDevice_constant_TEXTURE_TYPE_3D"></span>

[TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **TEXTURE_TYPE_3D** = `2`

3-dimensional texture.

<span id="class_RenderingDevice_constant_TEXTURE_TYPE_CUBE"></span>

[TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **TEXTURE_TYPE_CUBE** = `3`

[Cubemap](class_cubemap.md#class_Cubemap) texture.

<span id="class_RenderingDevice_constant_TEXTURE_TYPE_1D_ARRAY"></span>

[TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **TEXTURE_TYPE_1D_ARRAY** = `4`

Array of 1-dimensional textures.

<span id="class_RenderingDevice_constant_TEXTURE_TYPE_2D_ARRAY"></span>

[TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **TEXTURE_TYPE_2D_ARRAY** = `5`

Array of 2-dimensional textures.

<span id="class_RenderingDevice_constant_TEXTURE_TYPE_CUBE_ARRAY"></span>

[TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **TEXTURE_TYPE_CUBE_ARRAY** = `6`

Array of [Cubemap](class_cubemap.md#class_Cubemap) textures.

<span id="class_RenderingDevice_constant_TEXTURE_TYPE_MAX"></span>

[TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) **TEXTURE_TYPE_MAX** = `7`

Represents the size of the [TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType) enum.

---

<span id="enum_RenderingDevice_TextureSamples"></span>

enum **TextureSamples**: [🔗](class_renderingdevice.md#enum_RenderingDevice_TextureSamples)

<span id="class_RenderingDevice_constant_TEXTURE_SAMPLES_1"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **TEXTURE_SAMPLES_1** = `0`

Perform 1 texture sample (this is the fastest but lowest-quality for antialiasing).

<span id="class_RenderingDevice_constant_TEXTURE_SAMPLES_2"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **TEXTURE_SAMPLES_2** = `1`

Perform 2 texture samples.

<span id="class_RenderingDevice_constant_TEXTURE_SAMPLES_4"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **TEXTURE_SAMPLES_4** = `2`

Perform 4 texture samples.

<span id="class_RenderingDevice_constant_TEXTURE_SAMPLES_8"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **TEXTURE_SAMPLES_8** = `3`

Perform 8 texture samples. Not supported on mobile GPUs (including Apple Silicon).

<span id="class_RenderingDevice_constant_TEXTURE_SAMPLES_16"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **TEXTURE_SAMPLES_16** = `4`

Perform 16 texture samples. Not supported on mobile GPUs and many desktop GPUs.

<span id="class_RenderingDevice_constant_TEXTURE_SAMPLES_32"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **TEXTURE_SAMPLES_32** = `5`

Perform 32 texture samples. Not supported on most GPUs.

<span id="class_RenderingDevice_constant_TEXTURE_SAMPLES_64"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **TEXTURE_SAMPLES_64** = `6`

Perform 64 texture samples (this is the slowest but highest-quality for antialiasing). Not supported on most GPUs.

<span id="class_RenderingDevice_constant_TEXTURE_SAMPLES_MAX"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **TEXTURE_SAMPLES_MAX** = `7`

Represents the size of the [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) enum.

---

<span id="enum_RenderingDevice_TextureUsageBits"></span>

flags **TextureUsageBits**: [🔗](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits)

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_SAMPLING_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_SAMPLING_BIT** = `1`

Texture can be sampled.

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_COLOR_ATTACHMENT_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_COLOR_ATTACHMENT_BIT** = `2`

Texture can be used as a color attachment in a framebuffer.

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT** = `4`

Texture can be used as a depth/stencil attachment in a framebuffer.

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_DEPTH_RESOLVE_ATTACHMENT_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_DEPTH_RESOLVE_ATTACHMENT_BIT** = `4096`

Texture can be used as a depth/stencil resolve attachment in a framebuffer.

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_STORAGE_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_STORAGE_BIT** = `8`

Texture can be used as a storage image.

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_STORAGE_ATOMIC_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_STORAGE_ATOMIC_BIT** = `16`

Texture can be used as a storage image with support for atomic operations.

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_CPU_READ_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_CPU_READ_BIT** = `32`

Texture can be read back on the CPU using [texture_get_data()](class_renderingdevice.md#class_RenderingDevice_method_texture_get_data) faster than without this bit, since it is always kept in the system memory.

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_CAN_UPDATE_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_CAN_UPDATE_BIT** = `64`

Texture can be updated using [texture_update()](class_renderingdevice.md#class_RenderingDevice_method_texture_update).

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_FROM_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_CAN_COPY_FROM_BIT** = `128`

Texture can be a source for [texture_copy()](class_renderingdevice.md#class_RenderingDevice_method_texture_copy).

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_TO_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_CAN_COPY_TO_BIT** = `256`

Texture can be a destination for [texture_copy()](class_renderingdevice.md#class_RenderingDevice_method_texture_copy).

<span id="class_RenderingDevice_constant_TEXTURE_USAGE_INPUT_ATTACHMENT_BIT"></span>

[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits) **TEXTURE_USAGE_INPUT_ATTACHMENT_BIT** = `512`

Texture can be used as a input attachment in a framebuffer.

---

<span id="enum_RenderingDevice_TextureSwizzle"></span>

enum **TextureSwizzle**: [🔗](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle)

<span id="class_RenderingDevice_constant_TEXTURE_SWIZZLE_IDENTITY"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **TEXTURE_SWIZZLE_IDENTITY** = `0`

Return the sampled value as-is.

<span id="class_RenderingDevice_constant_TEXTURE_SWIZZLE_ZERO"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **TEXTURE_SWIZZLE_ZERO** = `1`

Always return `0.0` when sampling.

<span id="class_RenderingDevice_constant_TEXTURE_SWIZZLE_ONE"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **TEXTURE_SWIZZLE_ONE** = `2`

Always return `1.0` when sampling.

<span id="class_RenderingDevice_constant_TEXTURE_SWIZZLE_R"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **TEXTURE_SWIZZLE_R** = `3`

Sample the red color channel.

<span id="class_RenderingDevice_constant_TEXTURE_SWIZZLE_G"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **TEXTURE_SWIZZLE_G** = `4`

Sample the green color channel.

<span id="class_RenderingDevice_constant_TEXTURE_SWIZZLE_B"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **TEXTURE_SWIZZLE_B** = `5`

Sample the blue color channel.

<span id="class_RenderingDevice_constant_TEXTURE_SWIZZLE_A"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **TEXTURE_SWIZZLE_A** = `6`

Sample the alpha channel.

<span id="class_RenderingDevice_constant_TEXTURE_SWIZZLE_MAX"></span>

[TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) **TEXTURE_SWIZZLE_MAX** = `7`

Represents the size of the [TextureSwizzle](class_renderingdevice.md#enum_RenderingDevice_TextureSwizzle) enum.

---

<span id="enum_RenderingDevice_TextureSliceType"></span>

enum **TextureSliceType**: [🔗](class_renderingdevice.md#enum_RenderingDevice_TextureSliceType)

<span id="class_RenderingDevice_constant_TEXTURE_SLICE_2D"></span>

[TextureSliceType](class_renderingdevice.md#enum_RenderingDevice_TextureSliceType) **TEXTURE_SLICE_2D** = `0`

2-dimensional texture slice.

<span id="class_RenderingDevice_constant_TEXTURE_SLICE_CUBEMAP"></span>

[TextureSliceType](class_renderingdevice.md#enum_RenderingDevice_TextureSliceType) **TEXTURE_SLICE_CUBEMAP** = `1`

Cubemap texture slice.

<span id="class_RenderingDevice_constant_TEXTURE_SLICE_3D"></span>

[TextureSliceType](class_renderingdevice.md#enum_RenderingDevice_TextureSliceType) **TEXTURE_SLICE_3D** = `2`

3-dimensional texture slice.

---

<span id="enum_RenderingDevice_SamplerFilter"></span>

enum **SamplerFilter**: [🔗](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter)

<span id="class_RenderingDevice_constant_SAMPLER_FILTER_NEAREST"></span>

[SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) **SAMPLER_FILTER_NEAREST** = `0`

Nearest-neighbor sampler filtering. Sampling at higher resolutions than the source will result in a pixelated look.

<span id="class_RenderingDevice_constant_SAMPLER_FILTER_LINEAR"></span>

[SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) **SAMPLER_FILTER_LINEAR** = `1`

Bilinear sampler filtering. Sampling at higher resolutions than the source will result in a blurry look.

---

<span id="enum_RenderingDevice_SamplerRepeatMode"></span>

enum **SamplerRepeatMode**: [🔗](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode)

<span id="class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_REPEAT"></span>

[SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **SAMPLER_REPEAT_MODE_REPEAT** = `0`

Sample with repeating enabled.

<span id="class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_MIRRORED_REPEAT"></span>

[SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **SAMPLER_REPEAT_MODE_MIRRORED_REPEAT** = `1`

Sample with mirrored repeating enabled. When sampling outside the `[0.0, 1.0]` range, return a mirrored version of the sampler. This mirrored version is mirrored again if sampling further away, with the pattern repeating indefinitely.

<span id="class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_EDGE"></span>

[SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **SAMPLER_REPEAT_MODE_CLAMP_TO_EDGE** = `2`

Sample with repeating disabled. When sampling outside the `[0.0, 1.0]` range, return the color of the last pixel on the edge.

<span id="class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER"></span>

[SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER** = `3`

Sample with repeating disabled. When sampling outside the `[0.0, 1.0]` range, return the specified [RDSamplerState.border_color](class_rdsamplerstate.md#class_RDSamplerState_property_border_color).

<span id="class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_MIRROR_CLAMP_TO_EDGE"></span>

[SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **SAMPLER_REPEAT_MODE_MIRROR_CLAMP_TO_EDGE** = `4`

Sample with mirrored repeating enabled, but only once. When sampling in the `[-1.0, 0.0]` range, return a mirrored version of the sampler. When sampling outside the `[-1.0, 1.0]` range, return the color of the last pixel on the edge.

<span id="class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_MAX"></span>

[SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) **SAMPLER_REPEAT_MODE_MAX** = `5`

Represents the size of the [SamplerRepeatMode](class_renderingdevice.md#enum_RenderingDevice_SamplerRepeatMode) enum.

---

<span id="enum_RenderingDevice_SamplerBorderColor"></span>

enum **SamplerBorderColor**: [🔗](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor)

<span id="class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_FLOAT_TRANSPARENT_BLACK"></span>

[SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) **SAMPLER_BORDER_COLOR_FLOAT_TRANSPARENT_BLACK** = `0`

Return a floating-point transparent black color when sampling outside the `[0.0, 1.0]` range. Only effective if the sampler repeat mode is [SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER](class_renderingdevice.md#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER).

<span id="class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_INT_TRANSPARENT_BLACK"></span>

[SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) **SAMPLER_BORDER_COLOR_INT_TRANSPARENT_BLACK** = `1`

Return an integer transparent black color when sampling outside the `[0.0, 1.0]` range. Only effective if the sampler repeat mode is [SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER](class_renderingdevice.md#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER).

<span id="class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_BLACK"></span>

[SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) **SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_BLACK** = `2`

Return a floating-point opaque black color when sampling outside the `[0.0, 1.0]` range. Only effective if the sampler repeat mode is [SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER](class_renderingdevice.md#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER).

<span id="class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_INT_OPAQUE_BLACK"></span>

[SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) **SAMPLER_BORDER_COLOR_INT_OPAQUE_BLACK** = `3`

Return an integer opaque black color when sampling outside the `[0.0, 1.0]` range. Only effective if the sampler repeat mode is [SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER](class_renderingdevice.md#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER).

<span id="class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_WHITE"></span>

[SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) **SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_WHITE** = `4`

Return a floating-point opaque white color when sampling outside the `[0.0, 1.0]` range. Only effective if the sampler repeat mode is [SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER](class_renderingdevice.md#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER).

<span id="class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_INT_OPAQUE_WHITE"></span>

[SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) **SAMPLER_BORDER_COLOR_INT_OPAQUE_WHITE** = `5`

Return an integer opaque white color when sampling outside the `[0.0, 1.0]` range. Only effective if the sampler repeat mode is [SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER](class_renderingdevice.md#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER).

<span id="class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_MAX"></span>

[SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) **SAMPLER_BORDER_COLOR_MAX** = `6`

Represents the size of the [SamplerBorderColor](class_renderingdevice.md#enum_RenderingDevice_SamplerBorderColor) enum.

---

<span id="enum_RenderingDevice_VertexFrequency"></span>

enum **VertexFrequency**: [🔗](class_renderingdevice.md#enum_RenderingDevice_VertexFrequency)

<span id="class_RenderingDevice_constant_VERTEX_FREQUENCY_VERTEX"></span>

[VertexFrequency](class_renderingdevice.md#enum_RenderingDevice_VertexFrequency) **VERTEX_FREQUENCY_VERTEX** = `0`

Vertex attribute addressing is a function of the vertex. This is used to specify the rate at which vertex attributes are pulled from buffers.

<span id="class_RenderingDevice_constant_VERTEX_FREQUENCY_INSTANCE"></span>

[VertexFrequency](class_renderingdevice.md#enum_RenderingDevice_VertexFrequency) **VERTEX_FREQUENCY_INSTANCE** = `1`

Vertex attribute addressing is a function of the instance index. This is used to specify the rate at which vertex attributes are pulled from buffers.

---

<span id="enum_RenderingDevice_IndexBufferFormat"></span>

enum **IndexBufferFormat**: [🔗](class_renderingdevice.md#enum_RenderingDevice_IndexBufferFormat)

<span id="class_RenderingDevice_constant_INDEX_BUFFER_FORMAT_UINT16"></span>

[IndexBufferFormat](class_renderingdevice.md#enum_RenderingDevice_IndexBufferFormat) **INDEX_BUFFER_FORMAT_UINT16** = `0`

Index buffer in 16-bit unsigned integer format. This limits the maximum index that can be specified to `65535`.

<span id="class_RenderingDevice_constant_INDEX_BUFFER_FORMAT_UINT32"></span>

[IndexBufferFormat](class_renderingdevice.md#enum_RenderingDevice_IndexBufferFormat) **INDEX_BUFFER_FORMAT_UINT32** = `1`

Index buffer in 32-bit unsigned integer format. This limits the maximum index that can be specified to `4294967295`.

---

<span id="enum_RenderingDevice_StorageBufferUsage"></span>

flags **StorageBufferUsage**: [🔗](class_renderingdevice.md#enum_RenderingDevice_StorageBufferUsage)

<span id="class_RenderingDevice_constant_STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT"></span>

[StorageBufferUsage](class_renderingdevice.md#enum_RenderingDevice_StorageBufferUsage) **STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT** = `1`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

<span id="enum_RenderingDevice_BufferCreationBits"></span>

flags **BufferCreationBits**: [🔗](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)

<span id="class_RenderingDevice_constant_BUFFER_CREATION_DEVICE_ADDRESS_BIT"></span>

[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits) **BUFFER_CREATION_DEVICE_ADDRESS_BIT** = `1`

Optionally, set this flag if you wish to use [buffer_get_device_address()](class_renderingdevice.md#class_RenderingDevice_method_buffer_get_device_address) functionality. You must first check the GPU supports it:

.. tabs::

```
```

    rd = RenderingServer.get_rendering_device()

    if rd.has_feature(RenderingDevice.SUPPORTS_BUFFER_DEVICE_ADDRESS):
        storage_buffer = rd.storage_buffer_create(bytes.size(), bytes, RenderingDevice.STORAGE_BUFFER_USAGE_SHADER_DEVICE_ADDRESS)
        storage_buffer_address = rd.buffer_get_device_address(storage_buffer)

<span id="class_RenderingDevice_constant_BUFFER_CREATION_AS_STORAGE_BIT"></span>

[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits) **BUFFER_CREATION_AS_STORAGE_BIT** = `2`

Set this flag so that it is created as storage. This is useful if Compute Shaders need access (for reading or writing) to the buffer, e.g. skeletal animations are processed in Compute Shaders which need access to vertex buffers, to be later consumed by vertex shaders as part of the regular rasterization pipeline.

<span id="class_RenderingDevice_constant_BUFFER_CREATION_ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_BIT"></span>

[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits) **BUFFER_CREATION_ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_BIT** = `8`

Allows usage of this buffer as input data for an acceleration structure build operation. You must first check that the GPU supports it:

.. tabs::

```
```

    rd = RenderingServer.get_rendering_device()

    if rd.has_feature(RenderingDevice.SUPPORTS_RAYTRACING_PIPELINE):
        storage_buffer = rd.storage_buffer_create(bytes.size(), bytes, RenderingDevice.BUFFER_CREATION_ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_BIT)

---

<span id="enum_RenderingDevice_AccelerationStructureGeometryBits"></span>

flags **AccelerationStructureGeometryBits**: [🔗](class_renderingdevice.md#enum_RenderingDevice_AccelerationStructureGeometryBits)

<span id="class_RenderingDevice_constant_ACCELERATION_STRUCTURE_GEOMETRY_OPAQUE"></span>

[AccelerationStructureGeometryBits](class_renderingdevice.md#enum_RenderingDevice_AccelerationStructureGeometryBits) **ACCELERATION_STRUCTURE_GEOMETRY_OPAQUE** = `1`

An opaque geometry does not invoke the any hit shaders.

<span id="class_RenderingDevice_constant_ACCELERATION_STRUCTURE_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION"></span>

[AccelerationStructureGeometryBits](class_renderingdevice.md#enum_RenderingDevice_AccelerationStructureGeometryBits) **ACCELERATION_STRUCTURE_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION** = `2`

This geometry only calls the any hit shader a single time for each primitive.

---

<span id="enum_RenderingDevice_UniformType"></span>

enum **UniformType**: [🔗](class_renderingdevice.md#enum_RenderingDevice_UniformType)

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_SAMPLER"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_SAMPLER** = `0`

Sampler uniform.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_SAMPLER_WITH_TEXTURE"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_SAMPLER_WITH_TEXTURE** = `1`

Sampler uniform with a texture.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_TEXTURE"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_TEXTURE** = `2`

Texture uniform.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_IMAGE"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_IMAGE** = `3`

Image uniform.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_TEXTURE_BUFFER"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_TEXTURE_BUFFER** = `4`

Texture buffer uniform.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_SAMPLER_WITH_TEXTURE_BUFFER"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_SAMPLER_WITH_TEXTURE_BUFFER** = `5`

Sampler uniform with a texture buffer.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_IMAGE_BUFFER"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_IMAGE_BUFFER** = `6`

Image buffer uniform.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_UNIFORM_BUFFER"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_UNIFORM_BUFFER** = `7`

Uniform buffer uniform.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_STORAGE_BUFFER"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_STORAGE_BUFFER** = `8`

Storage buffer uniform.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_INPUT_ATTACHMENT"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_INPUT_ATTACHMENT** = `9`

Input attachment uniform.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_UNIFORM_BUFFER_DYNAMIC"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_UNIFORM_BUFFER_DYNAMIC** = `10`

Same as UNIFORM_TYPE_UNIFORM_BUFFER but for buffers created with BUFFER_CREATION_DYNAMIC_PERSISTENT_BIT.

 **Note:** This flag is not available to GD users due to being too dangerous (i.e. wrong usage can result in visual glitches).

It's exposed in case GD users receive a buffer created with such flag from Godot.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_STORAGE_BUFFER_DYNAMIC"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_STORAGE_BUFFER_DYNAMIC** = `11`

Same as UNIFORM_TYPE_STORAGE_BUFFER but for buffers created with BUFFER_CREATION_DYNAMIC_PERSISTENT_BIT.

 **Note:** This flag is not available to GD users due to being too dangerous (i.e. wrong usage can result in visual glitches).

It's exposed in case GD users receive a buffer created with such flag from Godot.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_ACCELERATION_STRUCTURE"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_ACCELERATION_STRUCTURE** = `12`

Acceleration structure uniform.

<span id="class_RenderingDevice_constant_UNIFORM_TYPE_MAX"></span>

[UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) **UNIFORM_TYPE_MAX** = `13`

Represents the size of the [UniformType](class_renderingdevice.md#enum_RenderingDevice_UniformType) enum.

---

<span id="enum_RenderingDevice_RenderPrimitive"></span>

enum **RenderPrimitive**: [🔗](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive)

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_POINTS"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_POINTS** = `0`

Point rendering primitive (with constant size, regardless of distance from camera).

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_LINES"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_LINES** = `1`

Line list rendering primitive. Lines are drawn separated from each other.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_LINES_WITH_ADJACENCY"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_LINES_WITH_ADJACENCY** = `2`

Line list rendering primitive with adjacency.

 **Note:** Adjacency is only useful with geometry shaders, which Godot does not expose.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_LINESTRIPS"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_LINESTRIPS** = `3`

Line strip rendering primitive. Lines drawn are connected to the previous vertex.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_LINESTRIPS_WITH_ADJACENCY"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_LINESTRIPS_WITH_ADJACENCY** = `4`

Line strip rendering primitive with adjacency.

 **Note:** Adjacency is only useful with geometry shaders, which Godot does not expose.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLES"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_TRIANGLES** = `5`

Triangle list rendering primitive. Triangles are drawn separated from each other.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLES_WITH_ADJACENCY"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_TRIANGLES_WITH_ADJACENCY** = `6`

Triangle list rendering primitive with adjacency.

 **Note:** Adjacency is only useful with geometry shaders, which Godot does not expose.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLE_STRIPS"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_TRIANGLE_STRIPS** = `7`

Triangle strip rendering primitive. Triangles drawn are connected to the previous triangle.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_AJACENCY"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_AJACENCY** = `8`

Triangle strip rendering primitive with adjacency.

 **Note:** Adjacency is only useful with geometry shaders, which Godot does not expose.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_RESTART_INDEX"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_RESTART_INDEX** = `9`

Triangle strip rendering primitive with *primitive restart* enabled. Triangles drawn are connected to the previous triangle, but a primitive restart index can be specified before drawing to create a second triangle strip after the specified index.

 **Note:** Only compatible with indexed draws.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_TESSELATION_PATCH"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_TESSELATION_PATCH** = `10`

Tessellation patch rendering primitive. Only useful with tessellation shaders, which can be used to deform these patches.

<span id="class_RenderingDevice_constant_RENDER_PRIMITIVE_MAX"></span>

[RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) **RENDER_PRIMITIVE_MAX** = `11`

Represents the size of the [RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive) enum.

---

<span id="enum_RenderingDevice_PolygonCullMode"></span>

enum **PolygonCullMode**: [🔗](class_renderingdevice.md#enum_RenderingDevice_PolygonCullMode)

<span id="class_RenderingDevice_constant_POLYGON_CULL_DISABLED"></span>

[PolygonCullMode](class_renderingdevice.md#enum_RenderingDevice_PolygonCullMode) **POLYGON_CULL_DISABLED** = `0`

Do not use polygon front face or backface culling.

<span id="class_RenderingDevice_constant_POLYGON_CULL_FRONT"></span>

[PolygonCullMode](class_renderingdevice.md#enum_RenderingDevice_PolygonCullMode) **POLYGON_CULL_FRONT** = `1`

Use polygon frontface culling (faces pointing towards the camera are hidden).

<span id="class_RenderingDevice_constant_POLYGON_CULL_BACK"></span>

[PolygonCullMode](class_renderingdevice.md#enum_RenderingDevice_PolygonCullMode) **POLYGON_CULL_BACK** = `2`

Use polygon backface culling (faces pointing away from the camera are hidden).

---

<span id="enum_RenderingDevice_PolygonFrontFace"></span>

enum **PolygonFrontFace**: [🔗](class_renderingdevice.md#enum_RenderingDevice_PolygonFrontFace)

<span id="class_RenderingDevice_constant_POLYGON_FRONT_FACE_CLOCKWISE"></span>

[PolygonFrontFace](class_renderingdevice.md#enum_RenderingDevice_PolygonFrontFace) **POLYGON_FRONT_FACE_CLOCKWISE** = `0`

Clockwise winding order to determine which face of a polygon is its front face.

<span id="class_RenderingDevice_constant_POLYGON_FRONT_FACE_COUNTER_CLOCKWISE"></span>

[PolygonFrontFace](class_renderingdevice.md#enum_RenderingDevice_PolygonFrontFace) **POLYGON_FRONT_FACE_COUNTER_CLOCKWISE** = `1`

Counter-clockwise winding order to determine which face of a polygon is its front face.

---

<span id="enum_RenderingDevice_StencilOperation"></span>

enum **StencilOperation**: [🔗](class_renderingdevice.md#enum_RenderingDevice_StencilOperation)

<span id="class_RenderingDevice_constant_STENCIL_OP_KEEP"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **STENCIL_OP_KEEP** = `0`

Keep the current stencil value.

<span id="class_RenderingDevice_constant_STENCIL_OP_ZERO"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **STENCIL_OP_ZERO** = `1`

Set the stencil value to `0`.

<span id="class_RenderingDevice_constant_STENCIL_OP_REPLACE"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **STENCIL_OP_REPLACE** = `2`

Replace the existing stencil value with the new one.

<span id="class_RenderingDevice_constant_STENCIL_OP_INCREMENT_AND_CLAMP"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **STENCIL_OP_INCREMENT_AND_CLAMP** = `3`

Increment the existing stencil value and clamp to the maximum representable unsigned value if reached. Stencil bits are considered as an unsigned integer.

<span id="class_RenderingDevice_constant_STENCIL_OP_DECREMENT_AND_CLAMP"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **STENCIL_OP_DECREMENT_AND_CLAMP** = `4`

Decrement the existing stencil value and clamp to the minimum value if reached. Stencil bits are considered as an unsigned integer.

<span id="class_RenderingDevice_constant_STENCIL_OP_INVERT"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **STENCIL_OP_INVERT** = `5`

Bitwise-invert the existing stencil value.

<span id="class_RenderingDevice_constant_STENCIL_OP_INCREMENT_AND_WRAP"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **STENCIL_OP_INCREMENT_AND_WRAP** = `6`

Increment the stencil value and wrap around to `0` if reaching the maximum representable unsigned. Stencil bits are considered as an unsigned integer.

<span id="class_RenderingDevice_constant_STENCIL_OP_DECREMENT_AND_WRAP"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **STENCIL_OP_DECREMENT_AND_WRAP** = `7`

Decrement the stencil value and wrap around to the maximum representable unsigned if reaching the minimum. Stencil bits are considered as an unsigned integer.

<span id="class_RenderingDevice_constant_STENCIL_OP_MAX"></span>

[StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) **STENCIL_OP_MAX** = `8`

Represents the size of the [StencilOperation](class_renderingdevice.md#enum_RenderingDevice_StencilOperation) enum.

---

<span id="enum_RenderingDevice_CompareOperator"></span>

enum **CompareOperator**: [🔗](class_renderingdevice.md#enum_RenderingDevice_CompareOperator)

<span id="class_RenderingDevice_constant_COMPARE_OP_NEVER"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **COMPARE_OP_NEVER** = `0`

"Never" comparison (opposite of [COMPARE_OP_ALWAYS](class_renderingdevice.md#class_RenderingDevice_constant_COMPARE_OP_ALWAYS)).

<span id="class_RenderingDevice_constant_COMPARE_OP_LESS"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **COMPARE_OP_LESS** = `1`

"Less than" comparison.

<span id="class_RenderingDevice_constant_COMPARE_OP_EQUAL"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **COMPARE_OP_EQUAL** = `2`

"Equal" comparison.

<span id="class_RenderingDevice_constant_COMPARE_OP_LESS_OR_EQUAL"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **COMPARE_OP_LESS_OR_EQUAL** = `3`

"Less than or equal" comparison.

<span id="class_RenderingDevice_constant_COMPARE_OP_GREATER"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **COMPARE_OP_GREATER** = `4`

"Greater than" comparison.

<span id="class_RenderingDevice_constant_COMPARE_OP_NOT_EQUAL"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **COMPARE_OP_NOT_EQUAL** = `5`

"Not equal" comparison.

<span id="class_RenderingDevice_constant_COMPARE_OP_GREATER_OR_EQUAL"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **COMPARE_OP_GREATER_OR_EQUAL** = `6`

"Greater than or equal" comparison.

<span id="class_RenderingDevice_constant_COMPARE_OP_ALWAYS"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **COMPARE_OP_ALWAYS** = `7`

"Always" comparison (opposite of [COMPARE_OP_NEVER](class_renderingdevice.md#class_RenderingDevice_constant_COMPARE_OP_NEVER)).

<span id="class_RenderingDevice_constant_COMPARE_OP_MAX"></span>

[CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) **COMPARE_OP_MAX** = `8`

Represents the size of the [CompareOperator](class_renderingdevice.md#enum_RenderingDevice_CompareOperator) enum.

---

<span id="enum_RenderingDevice_LogicOperation"></span>

enum **LogicOperation**: [🔗](class_renderingdevice.md#enum_RenderingDevice_LogicOperation)

<span id="class_RenderingDevice_constant_LOGIC_OP_CLEAR"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_CLEAR** = `0`

Clear logic operation (result is always `0`). See also [LOGIC_OP_SET](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_SET).

<span id="class_RenderingDevice_constant_LOGIC_OP_AND"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_AND** = `1`

AND logic operation.

<span id="class_RenderingDevice_constant_LOGIC_OP_AND_REVERSE"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_AND_REVERSE** = `2`

AND logic operation with the *destination* operand being inverted. See also [LOGIC_OP_AND_INVERTED](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_AND_INVERTED).

<span id="class_RenderingDevice_constant_LOGIC_OP_COPY"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_COPY** = `3`

Copy logic operation (keeps the *source* value as-is). See also [LOGIC_OP_COPY_INVERTED](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_COPY_INVERTED) and [LOGIC_OP_NO_OP](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_NO_OP).

<span id="class_RenderingDevice_constant_LOGIC_OP_AND_INVERTED"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_AND_INVERTED** = `4`

AND logic operation with the *source* operand being inverted. See also [LOGIC_OP_AND_REVERSE](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_AND_REVERSE).

<span id="class_RenderingDevice_constant_LOGIC_OP_NO_OP"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_NO_OP** = `5`

No-op logic operation (keeps the *destination* value as-is). See also [LOGIC_OP_COPY](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_COPY).

<span id="class_RenderingDevice_constant_LOGIC_OP_XOR"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_XOR** = `6`

Exclusive or (XOR) logic operation.

<span id="class_RenderingDevice_constant_LOGIC_OP_OR"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_OR** = `7`

OR logic operation.

<span id="class_RenderingDevice_constant_LOGIC_OP_NOR"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_NOR** = `8`

Not-OR (NOR) logic operation.

<span id="class_RenderingDevice_constant_LOGIC_OP_EQUIVALENT"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_EQUIVALENT** = `9`

Not-XOR (XNOR) logic operation.

<span id="class_RenderingDevice_constant_LOGIC_OP_INVERT"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_INVERT** = `10`

Invert logic operation.

<span id="class_RenderingDevice_constant_LOGIC_OP_OR_REVERSE"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_OR_REVERSE** = `11`

OR logic operation with the *destination* operand being inverted. See also [LOGIC_OP_OR_REVERSE](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_OR_REVERSE).

<span id="class_RenderingDevice_constant_LOGIC_OP_COPY_INVERTED"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_COPY_INVERTED** = `12`

NOT logic operation (inverts the value). See also [LOGIC_OP_COPY](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_COPY).

<span id="class_RenderingDevice_constant_LOGIC_OP_OR_INVERTED"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_OR_INVERTED** = `13`

OR logic operation with the *source* operand being inverted. See also [LOGIC_OP_OR_REVERSE](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_OR_REVERSE).

<span id="class_RenderingDevice_constant_LOGIC_OP_NAND"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_NAND** = `14`

Not-AND (NAND) logic operation.

<span id="class_RenderingDevice_constant_LOGIC_OP_SET"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_SET** = `15`

SET logic operation (result is always `1`). See also [LOGIC_OP_CLEAR](class_renderingdevice.md#class_RenderingDevice_constant_LOGIC_OP_CLEAR).

<span id="class_RenderingDevice_constant_LOGIC_OP_MAX"></span>

[LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) **LOGIC_OP_MAX** = `16`

Represents the size of the [LogicOperation](class_renderingdevice.md#enum_RenderingDevice_LogicOperation) enum.

---

<span id="enum_RenderingDevice_BlendFactor"></span>

enum **BlendFactor**: [🔗](class_renderingdevice.md#enum_RenderingDevice_BlendFactor)

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ZERO"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ZERO** = `0`

Constant `0.0` blend factor.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ONE"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ONE** = `1`

Constant `1.0` blend factor.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_SRC_COLOR"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_SRC_COLOR** = `2`

Color blend factor is `source color`. Alpha blend factor is `source alpha`.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_COLOR"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ONE_MINUS_SRC_COLOR** = `3`

Color blend factor is `1.0 - source color`. Alpha blend factor is `1.0 - source alpha`.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_DST_COLOR"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_DST_COLOR** = `4`

Color blend factor is `destination color`. Alpha blend factor is `destination alpha`.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_DST_COLOR"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ONE_MINUS_DST_COLOR** = `5`

Color blend factor is `1.0 - destination color`. Alpha blend factor is `1.0 - destination alpha`.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_SRC_ALPHA** = `6`

Color and alpha blend factor is `source alpha`.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ONE_MINUS_SRC_ALPHA** = `7`

Color and alpha blend factor is `1.0 - source alpha`.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_DST_ALPHA"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_DST_ALPHA** = `8`

Color and alpha blend factor is `destination alpha`.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_DST_ALPHA"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ONE_MINUS_DST_ALPHA** = `9`

Color and alpha blend factor is `1.0 - destination alpha`.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_CONSTANT_COLOR"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_CONSTANT_COLOR** = `10`

Color blend factor is `blend constant color`. Alpha blend factor is `blend constant alpha` (see [draw_list_set_blend_constants()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_set_blend_constants)).

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR** = `11`

Color blend factor is `1.0 - blend constant color`. Alpha blend factor is `1.0 - blend constant alpha` (see [draw_list_set_blend_constants()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_set_blend_constants)).

<span id="class_RenderingDevice_constant_BLEND_FACTOR_CONSTANT_ALPHA"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_CONSTANT_ALPHA** = `12`

Color and alpha blend factor is `blend constant alpha` (see [draw_list_set_blend_constants()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_set_blend_constants)).

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA** = `13`

Color and alpha blend factor is `1.0 - blend constant alpha` (see [draw_list_set_blend_constants()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_set_blend_constants)).

<span id="class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA_SATURATE"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_SRC_ALPHA_SATURATE** = `14`

Color blend factor is `min(source alpha, 1.0 - destination alpha)`. Alpha blend factor is `1.0`.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_SRC1_COLOR"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_SRC1_COLOR** = `15`

Color blend factor is `second source color`. Alpha blend factor is `second source alpha`. Only relevant for dual-source blending.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC1_COLOR"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ONE_MINUS_SRC1_COLOR** = `16`

Color blend factor is `1.0 - second source color`. Alpha blend factor is `1.0 - second source alpha`. Only relevant for dual-source blending.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_SRC1_ALPHA"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_SRC1_ALPHA** = `17`

Color and alpha blend factor is `second source alpha`. Only relevant for dual-source blending.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC1_ALPHA"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_ONE_MINUS_SRC1_ALPHA** = `18`

Color and alpha blend factor is `1.0 - second source alpha`. Only relevant for dual-source blending.

<span id="class_RenderingDevice_constant_BLEND_FACTOR_MAX"></span>

[BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) **BLEND_FACTOR_MAX** = `19`

Represents the size of the [BlendFactor](class_renderingdevice.md#enum_RenderingDevice_BlendFactor) enum.

---

<span id="enum_RenderingDevice_BlendOperation"></span>

enum **BlendOperation**: [🔗](class_renderingdevice.md#enum_RenderingDevice_BlendOperation)

<span id="class_RenderingDevice_constant_BLEND_OP_ADD"></span>

[BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **BLEND_OP_ADD** = `0`

Additive blending operation (`source + destination`).

<span id="class_RenderingDevice_constant_BLEND_OP_SUBTRACT"></span>

[BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **BLEND_OP_SUBTRACT** = `1`

Subtractive blending operation (`source - destination`).

<span id="class_RenderingDevice_constant_BLEND_OP_REVERSE_SUBTRACT"></span>

[BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **BLEND_OP_REVERSE_SUBTRACT** = `2`

Reverse subtractive blending operation (`destination - source`).

<span id="class_RenderingDevice_constant_BLEND_OP_MINIMUM"></span>

[BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **BLEND_OP_MINIMUM** = `3`

Minimum blending operation (keep the lowest value of the two).

<span id="class_RenderingDevice_constant_BLEND_OP_MAXIMUM"></span>

[BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **BLEND_OP_MAXIMUM** = `4`

Maximum blending operation (keep the highest value of the two).

<span id="class_RenderingDevice_constant_BLEND_OP_MAX"></span>

[BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) **BLEND_OP_MAX** = `5`

Represents the size of the [BlendOperation](class_renderingdevice.md#enum_RenderingDevice_BlendOperation) enum.

---

<span id="enum_RenderingDevice_PipelineDynamicStateFlags"></span>

flags **PipelineDynamicStateFlags**: [🔗](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags)

<span id="class_RenderingDevice_constant_DYNAMIC_STATE_LINE_WIDTH"></span>

[PipelineDynamicStateFlags](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags) **DYNAMIC_STATE_LINE_WIDTH** = `1`

Allows dynamically changing the width of rendering lines.

<span id="class_RenderingDevice_constant_DYNAMIC_STATE_DEPTH_BIAS"></span>

[PipelineDynamicStateFlags](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags) **DYNAMIC_STATE_DEPTH_BIAS** = `2`

Allows dynamically changing the depth bias.

<span id="class_RenderingDevice_constant_DYNAMIC_STATE_BLEND_CONSTANTS"></span>

[PipelineDynamicStateFlags](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags) **DYNAMIC_STATE_BLEND_CONSTANTS** = `4`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DYNAMIC_STATE_DEPTH_BOUNDS"></span>

[PipelineDynamicStateFlags](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags) **DYNAMIC_STATE_DEPTH_BOUNDS** = `8`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DYNAMIC_STATE_STENCIL_COMPARE_MASK"></span>

[PipelineDynamicStateFlags](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags) **DYNAMIC_STATE_STENCIL_COMPARE_MASK** = `16`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DYNAMIC_STATE_STENCIL_WRITE_MASK"></span>

[PipelineDynamicStateFlags](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags) **DYNAMIC_STATE_STENCIL_WRITE_MASK** = `32`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_RenderingDevice_constant_DYNAMIC_STATE_STENCIL_REFERENCE"></span>

[PipelineDynamicStateFlags](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags) **DYNAMIC_STATE_STENCIL_REFERENCE** = `64`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

<span id="enum_RenderingDevice_InitialAction"></span>

enum **InitialAction**: [🔗](class_renderingdevice.md#enum_RenderingDevice_InitialAction)

<span id="class_RenderingDevice_constant_INITIAL_ACTION_LOAD"></span>

[InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) **INITIAL_ACTION_LOAD** = `0`

**Deprecated:** Initial actions are solved automatically by RenderingDevice.

Load the previous contents of the framebuffer.

<span id="class_RenderingDevice_constant_INITIAL_ACTION_CLEAR"></span>

[InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) **INITIAL_ACTION_CLEAR** = `1`

**Deprecated:** Initial actions are solved automatically by RenderingDevice.

Clear the whole framebuffer or its specified region.

<span id="class_RenderingDevice_constant_INITIAL_ACTION_DISCARD"></span>

[InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) **INITIAL_ACTION_DISCARD** = `2`

**Deprecated:** Initial actions are solved automatically by RenderingDevice.

Ignore the previous contents of the framebuffer. This is the fastest option if you'll overwrite all of the pixels and don't need to read any of them.

<span id="class_RenderingDevice_constant_INITIAL_ACTION_MAX"></span>

[InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) **INITIAL_ACTION_MAX** = `3`

**Deprecated:** Initial actions are solved automatically by RenderingDevice.

Represents the size of the [InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) enum.

<span id="class_RenderingDevice_constant_INITIAL_ACTION_CLEAR_REGION"></span>

[InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) **INITIAL_ACTION_CLEAR_REGION** = `1`

**Deprecated:** Initial actions are solved automatically by RenderingDevice.

<span id="class_RenderingDevice_constant_INITIAL_ACTION_CLEAR_REGION_CONTINUE"></span>

[InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) **INITIAL_ACTION_CLEAR_REGION_CONTINUE** = `1`

**Deprecated:** Initial actions are solved automatically by RenderingDevice.

<span id="class_RenderingDevice_constant_INITIAL_ACTION_KEEP"></span>

[InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) **INITIAL_ACTION_KEEP** = `0`

**Deprecated:** Initial actions are solved automatically by RenderingDevice.

<span id="class_RenderingDevice_constant_INITIAL_ACTION_DROP"></span>

[InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) **INITIAL_ACTION_DROP** = `2`

**Deprecated:** Initial actions are solved automatically by RenderingDevice.

<span id="class_RenderingDevice_constant_INITIAL_ACTION_CONTINUE"></span>

[InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction) **INITIAL_ACTION_CONTINUE** = `0`

**Deprecated:** Initial actions are solved automatically by RenderingDevice.

---

<span id="enum_RenderingDevice_FinalAction"></span>

enum **FinalAction**: [🔗](class_renderingdevice.md#enum_RenderingDevice_FinalAction)

<span id="class_RenderingDevice_constant_FINAL_ACTION_STORE"></span>

[FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction) **FINAL_ACTION_STORE** = `0`

**Deprecated:** Final actions are solved automatically by RenderingDevice.

Store the result of the draw list in the framebuffer. This is generally what you want to do.

<span id="class_RenderingDevice_constant_FINAL_ACTION_DISCARD"></span>

[FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction) **FINAL_ACTION_DISCARD** = `1`

**Deprecated:** Final actions are solved automatically by RenderingDevice.

Discard the contents of the framebuffer. This is the fastest option if you don't need to use the results of the draw list.

<span id="class_RenderingDevice_constant_FINAL_ACTION_MAX"></span>

[FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction) **FINAL_ACTION_MAX** = `2`

**Deprecated:** Final actions are solved automatically by RenderingDevice.

Represents the size of the [FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction) enum.

<span id="class_RenderingDevice_constant_FINAL_ACTION_READ"></span>

[FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction) **FINAL_ACTION_READ** = `0`

**Deprecated:** Final actions are solved automatically by RenderingDevice.

<span id="class_RenderingDevice_constant_FINAL_ACTION_CONTINUE"></span>

[FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction) **FINAL_ACTION_CONTINUE** = `0`

**Deprecated:** Final actions are solved automatically by RenderingDevice.

---

<span id="enum_RenderingDevice_ShaderStage"></span>

enum **ShaderStage**: [🔗](class_renderingdevice.md#enum_RenderingDevice_ShaderStage)

<span id="class_RenderingDevice_constant_SHADER_STAGE_VERTEX"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_VERTEX** = `0`

Vertex shader stage. This can be used to manipulate vertices from a shader (but not create new vertices).

<span id="class_RenderingDevice_constant_SHADER_STAGE_FRAGMENT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_FRAGMENT** = `1`

Fragment shader stage (called "pixel shader" in Direct3D). This can be used to manipulate pixels from a shader.

<span id="class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_CONTROL"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_TESSELATION_CONTROL** = `2`

Tessellation control shader stage. This can be used to create additional geometry from a shader.

<span id="class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_EVALUATION"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_TESSELATION_EVALUATION** = `3`

Tessellation evaluation shader stage. This can be used to create additional geometry from a shader.

<span id="class_RenderingDevice_constant_SHADER_STAGE_COMPUTE"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_COMPUTE** = `4`

Compute shader stage. This can be used to run arbitrary computing tasks in a shader, performing them on the GPU instead of the CPU.

<span id="class_RenderingDevice_constant_SHADER_STAGE_RAYGEN"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_RAYGEN** = `5`

Ray generation shader stage. This can be used to generate primary rays.

<span id="class_RenderingDevice_constant_SHADER_STAGE_ANY_HIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_ANY_HIT** = `6`

Any hit shader stage. Invoked when ray intersections are not opaque. This can be used to specify what happens when a ray hits any of the geometry in the scene.

<span id="class_RenderingDevice_constant_SHADER_STAGE_CLOSEST_HIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_CLOSEST_HIT** = `7`

Closest hit shader stage. This can be used to specify what happens when a ray hits the closest geometry in the scene.

<span id="class_RenderingDevice_constant_SHADER_STAGE_MISS"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_MISS** = `8`

Miss shader stage. This can be used to specify what happens if a ray does not hit anything in the scene.

<span id="class_RenderingDevice_constant_SHADER_STAGE_INTERSECTION"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_INTERSECTION** = `9`

Intersection shader stage. The intersection shader for triangles is built-in. This can be used to compute ray intersections with primitives that are not triangles.

<span id="class_RenderingDevice_constant_SHADER_STAGE_MAX"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_MAX** = `10`

Represents the size of the [ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) enum.

<span id="class_RenderingDevice_constant_SHADER_STAGE_VERTEX_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_VERTEX_BIT** = `1`

Vertex shader stage bit (see also [SHADER_STAGE_VERTEX](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_VERTEX)).

<span id="class_RenderingDevice_constant_SHADER_STAGE_FRAGMENT_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_FRAGMENT_BIT** = `2`

Fragment shader stage bit (see also [SHADER_STAGE_FRAGMENT](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_FRAGMENT)).

<span id="class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_CONTROL_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_TESSELATION_CONTROL_BIT** = `4`

Tessellation control shader stage bit (see also [SHADER_STAGE_TESSELATION_CONTROL](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_CONTROL)).

<span id="class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_EVALUATION_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_TESSELATION_EVALUATION_BIT** = `8`

Tessellation evaluation shader stage bit (see also [SHADER_STAGE_TESSELATION_EVALUATION](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_EVALUATION)).

<span id="class_RenderingDevice_constant_SHADER_STAGE_COMPUTE_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_COMPUTE_BIT** = `16`

Compute shader stage bit (see also [SHADER_STAGE_COMPUTE](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_COMPUTE)).

<span id="class_RenderingDevice_constant_SHADER_STAGE_RAYGEN_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_RAYGEN_BIT** = `32`

Ray generation shader stage bit (see also [SHADER_STAGE_RAYGEN](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_RAYGEN)).

<span id="class_RenderingDevice_constant_SHADER_STAGE_ANY_HIT_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_ANY_HIT_BIT** = `64`

Any hit shader stage bit (see also [SHADER_STAGE_ANY_HIT](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_ANY_HIT)).

<span id="class_RenderingDevice_constant_SHADER_STAGE_CLOSEST_HIT_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_CLOSEST_HIT_BIT** = `128`

Closest hit shader stage bit (see also [SHADER_STAGE_CLOSEST_HIT](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_CLOSEST_HIT)).

<span id="class_RenderingDevice_constant_SHADER_STAGE_MISS_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_MISS_BIT** = `256`

Miss shader stage bit (see also [SHADER_STAGE_MISS](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_MISS)).

<span id="class_RenderingDevice_constant_SHADER_STAGE_INTERSECTION_BIT"></span>

[ShaderStage](class_renderingdevice.md#enum_RenderingDevice_ShaderStage) **SHADER_STAGE_INTERSECTION_BIT** = `512`

Intersection shader stage bit (see also [SHADER_STAGE_INTERSECTION](class_renderingdevice.md#class_RenderingDevice_constant_SHADER_STAGE_INTERSECTION)).

---

<span id="enum_RenderingDevice_ShaderLanguage"></span>

enum **ShaderLanguage**: [🔗](class_renderingdevice.md#enum_RenderingDevice_ShaderLanguage)

<span id="class_RenderingDevice_constant_SHADER_LANGUAGE_GLSL"></span>

[ShaderLanguage](class_renderingdevice.md#enum_RenderingDevice_ShaderLanguage) **SHADER_LANGUAGE_GLSL** = `0`

Khronos' GLSL shading language (used natively by OpenGL and Vulkan). This is the language used for core Godot shaders.

<span id="class_RenderingDevice_constant_SHADER_LANGUAGE_HLSL"></span>

[ShaderLanguage](class_renderingdevice.md#enum_RenderingDevice_ShaderLanguage) **SHADER_LANGUAGE_HLSL** = `1`

Microsoft's High-Level Shading Language (used natively by Direct3D, but can also be used in Vulkan).

---

<span id="enum_RenderingDevice_PipelineSpecializationConstantType"></span>

enum **PipelineSpecializationConstantType**: [🔗](class_renderingdevice.md#enum_RenderingDevice_PipelineSpecializationConstantType)

<span id="class_RenderingDevice_constant_PIPELINE_SPECIALIZATION_CONSTANT_TYPE_BOOL"></span>

[PipelineSpecializationConstantType](class_renderingdevice.md#enum_RenderingDevice_PipelineSpecializationConstantType) **PIPELINE_SPECIALIZATION_CONSTANT_TYPE_BOOL** = `0`

Boolean specialization constant.

<span id="class_RenderingDevice_constant_PIPELINE_SPECIALIZATION_CONSTANT_TYPE_INT"></span>

[PipelineSpecializationConstantType](class_renderingdevice.md#enum_RenderingDevice_PipelineSpecializationConstantType) **PIPELINE_SPECIALIZATION_CONSTANT_TYPE_INT** = `1`

Integer specialization constant.

<span id="class_RenderingDevice_constant_PIPELINE_SPECIALIZATION_CONSTANT_TYPE_FLOAT"></span>

[PipelineSpecializationConstantType](class_renderingdevice.md#enum_RenderingDevice_PipelineSpecializationConstantType) **PIPELINE_SPECIALIZATION_CONSTANT_TYPE_FLOAT** = `2`

Floating-point specialization constant.

---

<span id="enum_RenderingDevice_Features"></span>

enum **Features**: [🔗](class_renderingdevice.md#enum_RenderingDevice_Features)

<span id="class_RenderingDevice_constant_SUPPORTS_METALFX_SPATIAL"></span>

[Features](class_renderingdevice.md#enum_RenderingDevice_Features) **SUPPORTS_METALFX_SPATIAL** = `3`

Support for MetalFX spatial upscaling.

<span id="class_RenderingDevice_constant_SUPPORTS_METALFX_TEMPORAL"></span>

[Features](class_renderingdevice.md#enum_RenderingDevice_Features) **SUPPORTS_METALFX_TEMPORAL** = `4`

Support for MetalFX temporal upscaling.

<span id="class_RenderingDevice_constant_SUPPORTS_BUFFER_DEVICE_ADDRESS"></span>

[Features](class_renderingdevice.md#enum_RenderingDevice_Features) **SUPPORTS_BUFFER_DEVICE_ADDRESS** = `6`

Features support for buffer device address extension.

<span id="class_RenderingDevice_constant_SUPPORTS_IMAGE_ATOMIC_32_BIT"></span>

[Features](class_renderingdevice.md#enum_RenderingDevice_Features) **SUPPORTS_IMAGE_ATOMIC_32_BIT** = `7`

Support for 32-bit image atomic operations.

<span id="class_RenderingDevice_constant_SUPPORTS_RAY_QUERY"></span>

[Features](class_renderingdevice.md#enum_RenderingDevice_Features) **SUPPORTS_RAY_QUERY** = `11`

Support for ray query extension.

 **Note:** This is currently only supported when using Vulkan. This is not supported on macOS and iOS (even on hardware supporting raytracing) due to MoltenVK limitations.

<span id="class_RenderingDevice_constant_SUPPORTS_RAYTRACING_PIPELINE"></span>

[Features](class_renderingdevice.md#enum_RenderingDevice_Features) **SUPPORTS_RAYTRACING_PIPELINE** = `12`

Support for raytracing pipeline extension.

 **Note:** This is currently only supported when using Vulkan. This is not supported on macOS and iOS (even on hardware supporting raytracing) due to MoltenVK limitations.

<span id="class_RenderingDevice_constant_SUPPORTS_HDR_OUTPUT"></span>

[Features](class_renderingdevice.md#enum_RenderingDevice_Features) **SUPPORTS_HDR_OUTPUT** = `13`

Support for high dynamic range (HDR) output.

---

<span id="enum_RenderingDevice_Limit"></span>

enum **Limit**: [🔗](class_renderingdevice.md#enum_RenderingDevice_Limit)

<span id="class_RenderingDevice_constant_LIMIT_MAX_BOUND_UNIFORM_SETS"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_BOUND_UNIFORM_SETS** = `0`

Maximum number of uniform sets that can be bound at a given time.

<span id="class_RenderingDevice_constant_LIMIT_MAX_FRAMEBUFFER_COLOR_ATTACHMENTS"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_FRAMEBUFFER_COLOR_ATTACHMENTS** = `1`

Maximum number of color framebuffer attachments that can be used at a given time.

<span id="class_RenderingDevice_constant_LIMIT_MAX_TEXTURES_PER_UNIFORM_SET"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_TEXTURES_PER_UNIFORM_SET** = `2`

Maximum number of textures that can be used per uniform set.

<span id="class_RenderingDevice_constant_LIMIT_MAX_SAMPLERS_PER_UNIFORM_SET"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_SAMPLERS_PER_UNIFORM_SET** = `3`

Maximum number of samplers that can be used per uniform set.

<span id="class_RenderingDevice_constant_LIMIT_MAX_STORAGE_BUFFERS_PER_UNIFORM_SET"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_STORAGE_BUFFERS_PER_UNIFORM_SET** = `4`

Maximum number of storage buffers per uniform set.

<span id="class_RenderingDevice_constant_LIMIT_MAX_STORAGE_IMAGES_PER_UNIFORM_SET"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_STORAGE_IMAGES_PER_UNIFORM_SET** = `5`

Maximum number of storage images per uniform set.

<span id="class_RenderingDevice_constant_LIMIT_MAX_UNIFORM_BUFFERS_PER_UNIFORM_SET"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_UNIFORM_BUFFERS_PER_UNIFORM_SET** = `6`

Maximum number of uniform buffers per uniform set.

<span id="class_RenderingDevice_constant_LIMIT_MAX_DRAW_INDEXED_INDEX"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_DRAW_INDEXED_INDEX** = `7`

Maximum index for an indexed draw command.

<span id="class_RenderingDevice_constant_LIMIT_MAX_FRAMEBUFFER_HEIGHT"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_FRAMEBUFFER_HEIGHT** = `8`

Maximum height of a framebuffer (in pixels).

<span id="class_RenderingDevice_constant_LIMIT_MAX_FRAMEBUFFER_WIDTH"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_FRAMEBUFFER_WIDTH** = `9`

Maximum width of a framebuffer (in pixels).

<span id="class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_ARRAY_LAYERS"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_TEXTURE_ARRAY_LAYERS** = `10`

Maximum number of texture array layers.

<span id="class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_SIZE_1D"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_TEXTURE_SIZE_1D** = `11`

Maximum supported 1-dimensional texture size (in pixels on a single axis).

<span id="class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_SIZE_2D"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_TEXTURE_SIZE_2D** = `12`

Maximum supported 2-dimensional texture size (in pixels on a single axis).

<span id="class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_SIZE_3D"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_TEXTURE_SIZE_3D** = `13`

Maximum supported 3-dimensional texture size (in pixels on a single axis).

<span id="class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_SIZE_CUBE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_TEXTURE_SIZE_CUBE** = `14`

Maximum supported cubemap texture size (in pixels on a single axis of a single face).

<span id="class_RenderingDevice_constant_LIMIT_MAX_TEXTURES_PER_SHADER_STAGE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_TEXTURES_PER_SHADER_STAGE** = `15`

Maximum number of textures per shader stage.

<span id="class_RenderingDevice_constant_LIMIT_MAX_SAMPLERS_PER_SHADER_STAGE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_SAMPLERS_PER_SHADER_STAGE** = `16`

Maximum number of samplers per shader stage.

<span id="class_RenderingDevice_constant_LIMIT_MAX_STORAGE_BUFFERS_PER_SHADER_STAGE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_STORAGE_BUFFERS_PER_SHADER_STAGE** = `17`

Maximum number of storage buffers per shader stage.

<span id="class_RenderingDevice_constant_LIMIT_MAX_STORAGE_IMAGES_PER_SHADER_STAGE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_STORAGE_IMAGES_PER_SHADER_STAGE** = `18`

Maximum number of storage images per shader stage.

<span id="class_RenderingDevice_constant_LIMIT_MAX_UNIFORM_BUFFERS_PER_SHADER_STAGE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_UNIFORM_BUFFERS_PER_SHADER_STAGE** = `19`

Maximum number of uniform buffers per uniform set.

<span id="class_RenderingDevice_constant_LIMIT_MAX_PUSH_CONSTANT_SIZE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_PUSH_CONSTANT_SIZE** = `20`

Maximum size of a push constant. A lot of devices are limited to 128 bytes, so try to avoid exceeding 128 bytes in push constants to ensure compatibility even if your GPU is reporting a higher value.

<span id="class_RenderingDevice_constant_LIMIT_MAX_UNIFORM_BUFFER_SIZE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_UNIFORM_BUFFER_SIZE** = `21`

Maximum size of a uniform buffer.

<span id="class_RenderingDevice_constant_LIMIT_MAX_VERTEX_INPUT_ATTRIBUTE_OFFSET"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_VERTEX_INPUT_ATTRIBUTE_OFFSET** = `22`

Maximum vertex input attribute offset.

<span id="class_RenderingDevice_constant_LIMIT_MAX_VERTEX_INPUT_ATTRIBUTES"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_VERTEX_INPUT_ATTRIBUTES** = `23`

Maximum number of vertex input attributes.

<span id="class_RenderingDevice_constant_LIMIT_MAX_VERTEX_INPUT_BINDINGS"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_VERTEX_INPUT_BINDINGS** = `24`

Maximum number of vertex input bindings.

<span id="class_RenderingDevice_constant_LIMIT_MAX_VERTEX_INPUT_BINDING_STRIDE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_VERTEX_INPUT_BINDING_STRIDE** = `25`

Maximum vertex input binding stride.

<span id="class_RenderingDevice_constant_LIMIT_MIN_UNIFORM_BUFFER_OFFSET_ALIGNMENT"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MIN_UNIFORM_BUFFER_OFFSET_ALIGNMENT** = `26`

Minimum uniform buffer offset alignment.

<span id="class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_SHARED_MEMORY_SIZE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_COMPUTE_SHARED_MEMORY_SIZE** = `27`

Maximum shared memory size for compute shaders.

<span id="class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_X"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_X** = `28`

Maximum number of workgroups for compute shaders on the X axis.

<span id="class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Y"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Y** = `29`

Maximum number of workgroups for compute shaders on the Y axis.

<span id="class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Z"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Z** = `30`

Maximum number of workgroups for compute shaders on the Z axis.

<span id="class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_INVOCATIONS"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_COMPUTE_WORKGROUP_INVOCATIONS** = `31`

Maximum number of workgroup invocations for compute shaders.

<span id="class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_X"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_X** = `32`

Maximum workgroup size for compute shaders on the X axis.

<span id="class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Y"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Y** = `33`

Maximum workgroup size for compute shaders on the Y axis.

<span id="class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Z"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Z** = `34`

Maximum workgroup size for compute shaders on the Z axis.

<span id="class_RenderingDevice_constant_LIMIT_MAX_VIEWPORT_DIMENSIONS_X"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_VIEWPORT_DIMENSIONS_X** = `35`

Maximum viewport width (in pixels).

<span id="class_RenderingDevice_constant_LIMIT_MAX_VIEWPORT_DIMENSIONS_Y"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_MAX_VIEWPORT_DIMENSIONS_Y** = `36`

Maximum viewport height (in pixels).

<span id="class_RenderingDevice_constant_LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE** = `46`

Returns the smallest value for ProjectSettings.rendering/scaling_3d/scale when using the MetalFX temporal upscaler.

 **Note:** The returned value is multiplied by a factor of `1000000` to preserve 6 digits of precision. It must be divided by `1000000.0` to convert the value to a floating point number.

<span id="class_RenderingDevice_constant_LIMIT_METALFX_TEMPORAL_SCALER_MAX_SCALE"></span>

[Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) **LIMIT_METALFX_TEMPORAL_SCALER_MAX_SCALE** = `47`

Returns the largest value for ProjectSettings.rendering/scaling_3d/scale when using the MetalFX temporal upscaler.

 **Note:** The returned value is multiplied by a factor of `1000000` to preserve 6 digits of precision. It must be divided by `1000000.0` to convert the value to a floating point number.

---

<span id="enum_RenderingDevice_MemoryType"></span>

enum **MemoryType**: [🔗](class_renderingdevice.md#enum_RenderingDevice_MemoryType)

<span id="class_RenderingDevice_constant_MEMORY_TEXTURES"></span>

[MemoryType](class_renderingdevice.md#enum_RenderingDevice_MemoryType) **MEMORY_TEXTURES** = `0`

Memory taken by textures.

<span id="class_RenderingDevice_constant_MEMORY_BUFFERS"></span>

[MemoryType](class_renderingdevice.md#enum_RenderingDevice_MemoryType) **MEMORY_BUFFERS** = `1`

Memory taken by buffers.

<span id="class_RenderingDevice_constant_MEMORY_TOTAL"></span>

[MemoryType](class_renderingdevice.md#enum_RenderingDevice_MemoryType) **MEMORY_TOTAL** = `2`

Total memory taken. This is greater than the sum of [MEMORY_TEXTURES](class_renderingdevice.md#class_RenderingDevice_constant_MEMORY_TEXTURES) and [MEMORY_BUFFERS](class_renderingdevice.md#class_RenderingDevice_constant_MEMORY_BUFFERS), as it also includes miscellaneous memory usage.

---

<span id="enum_RenderingDevice_BreadcrumbMarker"></span>

enum **BreadcrumbMarker**: [🔗](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker)

<span id="class_RenderingDevice_constant_NONE"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **NONE** = `0`

No breadcrumb marker will be added.

<span id="class_RenderingDevice_constant_REFLECTION_PROBES"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **REFLECTION_PROBES** = `65536`

During a GPU crash in dev or debug mode, Godot's error message will include `"REFLECTION_PROBES"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_SKY_PASS"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **SKY_PASS** = `131072`

During a GPU crash in dev or debug mode, Godot's error message will include `"SKY_PASS"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_LIGHTMAPPER_PASS"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **LIGHTMAPPER_PASS** = `196608`

During a GPU crash in dev or debug mode, Godot's error message will include `"LIGHTMAPPER_PASS"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_SHADOW_PASS_DIRECTIONAL"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **SHADOW_PASS_DIRECTIONAL** = `262144`

During a GPU crash in dev or debug mode, Godot's error message will include `"SHADOW_PASS_DIRECTIONAL"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_SHADOW_PASS_CUBE"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **SHADOW_PASS_CUBE** = `327680`

During a GPU crash in dev or debug mode, Godot's error message will include `"SHADOW_PASS_CUBE"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_OPAQUE_PASS"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **OPAQUE_PASS** = `393216`

During a GPU crash in dev or debug mode, Godot's error message will include `"OPAQUE_PASS"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_ALPHA_PASS"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **ALPHA_PASS** = `458752`

During a GPU crash in dev or debug mode, Godot's error message will include `"ALPHA_PASS"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_TRANSPARENT_PASS"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **TRANSPARENT_PASS** = `524288`

During a GPU crash in dev or debug mode, Godot's error message will include `"TRANSPARENT_PASS"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_POST_PROCESSING_PASS"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **POST_PROCESSING_PASS** = `589824`

During a GPU crash in dev or debug mode, Godot's error message will include `"POST_PROCESSING_PASS"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_BLIT_PASS"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **BLIT_PASS** = `655360`

During a GPU crash in dev or debug mode, Godot's error message will include `"BLIT_PASS"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_UI_PASS"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **UI_PASS** = `720896`

During a GPU crash in dev or debug mode, Godot's error message will include `"UI_PASS"` for added context as to when the crash occurred.

<span id="class_RenderingDevice_constant_DEBUG_PASS"></span>

[BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) **DEBUG_PASS** = `786432`

During a GPU crash in dev or debug mode, Godot's error message will include `"DEBUG_PASS"` for added context as to when the crash occurred.

---

<span id="enum_RenderingDevice_DrawFlags"></span>

flags **DrawFlags**: [🔗](class_renderingdevice.md#enum_RenderingDevice_DrawFlags)

<span id="class_RenderingDevice_constant_DRAW_DEFAULT_ALL"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_DEFAULT_ALL** = `0`

Do not clear or ignore any attachments.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_0"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_0** = `1`

Clear the first color attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_1"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_1** = `2`

Clear the second color attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_2"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_2** = `4`

Clear the third color attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_3"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_3** = `8`

Clear the fourth color attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_4"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_4** = `16`

Clear the fifth color attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_5"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_5** = `32`

Clear the sixth color attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_6"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_6** = `64`

Clear the seventh color attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_7"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_7** = `128`

Clear the eighth color attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_MASK"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_MASK** = `255`

Mask for clearing all color attachments.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_COLOR_ALL"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_COLOR_ALL** = `255`

Clear all color attachments.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_0"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_0** = `256`

Ignore the previous contents of the first color attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_1"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_1** = `512`

Ignore the previous contents of the second color attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_2"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_2** = `1024`

Ignore the previous contents of the third color attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_3"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_3** = `2048`

Ignore the previous contents of the fourth color attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_4"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_4** = `4096`

Ignore the previous contents of the fifth color attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_5"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_5** = `8192`

Ignore the previous contents of the sixth color attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_6"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_6** = `16384`

Ignore the previous contents of the seventh color attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_7"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_7** = `32768`

Ignore the previous contents of the eighth color attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_MASK"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_MASK** = `65280`

Mask for ignoring all the previous contents of the color attachments.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_COLOR_ALL"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_COLOR_ALL** = `65280`

Ignore the previous contents of all color attachments.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_DEPTH"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_DEPTH** = `65536`

Clear the depth attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_DEPTH"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_DEPTH** = `131072`

Ignore the previous contents of the depth attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_STENCIL"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_STENCIL** = `262144`

Clear the stencil attachment.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_STENCIL"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_STENCIL** = `524288`

Ignore the previous contents of the stencil attachment.

<span id="class_RenderingDevice_constant_DRAW_CLEAR_ALL"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_CLEAR_ALL** = `327935`

Clear all attachments.

<span id="class_RenderingDevice_constant_DRAW_IGNORE_ALL"></span>

[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags) **DRAW_IGNORE_ALL** = `720640`

Ignore the previous contents of all attachments.

---

### Constants

<span id="class_RenderingDevice_constant_INVALID_ID"></span>

**INVALID_ID** = `-1` [🔗](class_renderingdevice.md#class_RenderingDevice_constant_INVALID_ID)

Returned by functions that return an ID if a value is invalid.

<span id="class_RenderingDevice_constant_INVALID_FORMAT_ID"></span>

**INVALID_FORMAT_ID** = `-1` [🔗](class_renderingdevice.md#class_RenderingDevice_constant_INVALID_FORMAT_ID)

Returned by functions that return a format ID if a value is invalid.

---

### Method Descriptions

<span id="class_RenderingDevice_method_acceleration_structure_build"></span>

Error **acceleration_structure_build** ( acceleration_structure: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_acceleration_structure_build)

Builds the `acceleration_structure`.

---

<span id="class_RenderingDevice_method_barrier"></span>

void **barrier** ( from: *BitField*\[[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask)\] = 32767, to: *BitField*\[[BarrierMask](class_renderingdevice.md#enum_RenderingDevice_BarrierMask)\] = 32767 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_barrier)

**Deprecated:** Barriers are automatically inserted by RenderingDevice.

This method does nothing.

---

<span id="class_RenderingDevice_method_blas_create"></span>

[RID](class_rid.md#class_RID) **blas_create** ( vertex_array: [RID](class_rid.md#class_RID), index_array: [RID](class_rid.md#class_RID), geometry_bits: *BitField*\[[AccelerationStructureGeometryBits](class_renderingdevice.md#enum_RenderingDevice_AccelerationStructureGeometryBits)\] = 0, position_attribute_location: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_blas_create)

Creates a new Bottom Level Acceleration Structure. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

 `position_attribute_location` selects which vertex attribute location supplies the position data (default is 0).

---

<span id="class_RenderingDevice_method_buffer_clear"></span>

Error **buffer_clear** ( buffer: [RID](class_rid.md#class_RID), offset: [int](class_int.md#class_int), size_bytes: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_buffer_clear)

Clears the contents of the `buffer`, clearing `size_bytes` bytes, starting at `offset`.

Prints an error if:

- the size isn't a multiple of four

- the region specified by `offset` + `size_bytes` exceeds the buffer

- a draw list is currently active (created by [draw_list_begin()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin))

- a compute list is currently active (created by [compute_list_begin()](class_renderingdevice.md#class_RenderingDevice_method_compute_list_begin))

---

<span id="class_RenderingDevice_method_buffer_copy"></span>

Error **buffer_copy** ( src_buffer: [RID](class_rid.md#class_RID), dst_buffer: [RID](class_rid.md#class_RID), src_offset: [int](class_int.md#class_int), dst_offset: [int](class_int.md#class_int), size: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_buffer_copy)

Copies `size` bytes from the `src_buffer` at `src_offset` into `dst_buffer` at `dst_offset`.

Prints an error if:

- `size` exceeds the size of either `src_buffer` or `dst_buffer` at their corresponding offsets

- a draw list is currently active (created by [draw_list_begin()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin))

- a compute list is currently active (created by [compute_list_begin()](class_renderingdevice.md#class_RenderingDevice_method_compute_list_begin))

---

<span id="class_RenderingDevice_method_buffer_get_data"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **buffer_get_data** ( buffer: [RID](class_rid.md#class_RID), offset_bytes: [int](class_int.md#class_int) = 0, size_bytes: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_buffer_get_data)

Returns a copy of the data of the specified `buffer`, optionally `offset_bytes` and `size_bytes` can be set to copy only a portion of the buffer.

 **Note:** This method will block the GPU from working until the data is retrieved. Refer to [buffer_get_data_async()](class_renderingdevice.md#class_RenderingDevice_method_buffer_get_data_async) for an alternative that returns the data in more performant way.

---

<span id="class_RenderingDevice_method_buffer_get_data_async"></span>

Error **buffer_get_data_async** ( buffer: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable), offset_bytes: [int](class_int.md#class_int) = 0, size_bytes: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_buffer_get_data_async)

Asynchronous version of [buffer_get_data()](class_renderingdevice.md#class_RenderingDevice_method_buffer_get_data). RenderingDevice will call `callback` in a certain amount of frames with the data the buffer had at the time of the request.

 **Note:** At the moment, the delay corresponds to the amount of frames specified by ProjectSettings.rendering/rendering_device/vsync/frame_queue_size.

 **Note:** Downloading large buffers can have a prohibitive cost for real-time even when using the asynchronous method due to hardware bandwidth limitations. When dealing with large resources, you can adjust settings such as ProjectSettings.rendering/rendering_device/staging_buffer/block_size_kb to improve the transfer speed at the cost of extra memory.

::

    func _buffer_get_data_callback(array):
        value = array.decode_u32(0)

    ...

    rd.buffer_get_data_async(buffer, _buffer_get_data_callback)

---

<span id="class_RenderingDevice_method_buffer_get_device_address"></span>

[int](class_int.md#class_int) **buffer_get_device_address** ( buffer: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_buffer_get_device_address)

Returns the address of the given `buffer` which can be passed to shaders in any way to access underlying data. Buffer must have been created with this feature enabled.

 **Note:** You must check that the GPU supports this functionality by calling [has_feature()](class_renderingdevice.md#class_RenderingDevice_method_has_feature) with [SUPPORTS_BUFFER_DEVICE_ADDRESS](class_renderingdevice.md#class_RenderingDevice_constant_SUPPORTS_BUFFER_DEVICE_ADDRESS) as a parameter.

---

<span id="class_RenderingDevice_method_buffer_update"></span>

Error **buffer_update** ( buffer: [RID](class_rid.md#class_RID), offset: [int](class_int.md#class_int), size_bytes: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_buffer_update)

Updates a region of `size_bytes` bytes, starting at `offset`, in the buffer, with the specified `data`.

Prints an error if:

- the region specified by `offset` + `size_bytes` exceeds the buffer

- a draw list is currently active (created by [draw_list_begin()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin))

- a compute list is currently active (created by [compute_list_begin()](class_renderingdevice.md#class_RenderingDevice_method_compute_list_begin))

---

<span id="class_RenderingDevice_method_capture_timestamp"></span>

void **capture_timestamp** ( name: [String](class_string.md#class_String) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_capture_timestamp)

Creates a timestamp marker with the specified `name`. This is used for performance reporting with the [get_captured_timestamp_cpu_time()](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_cpu_time), [get_captured_timestamp_gpu_time()](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_gpu_time) and [get_captured_timestamp_name()](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_name) methods.

---

<span id="class_RenderingDevice_method_compute_list_add_barrier"></span>

void **compute_list_add_barrier** ( compute_list: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_list_add_barrier)

Raises a Vulkan compute barrier in the specified `compute_list`.

---

<span id="class_RenderingDevice_method_compute_list_begin"></span>

[int](class_int.md#class_int) **compute_list_begin** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_list_begin)

Starts a list of compute commands created with the `compute_*` methods. The returned value should be passed to other `compute_list_*` functions.

Multiple compute lists cannot be created at the same time; you must finish the previous compute list first using [compute_list_end()](class_renderingdevice.md#class_RenderingDevice_method_compute_list_end).

A simple compute operation might look like this (code is not a complete example):

::

    var rd = RenderingDevice.new()
    var compute_list = rd.compute_list_begin()

    rd.compute_list_bind_compute_pipeline(compute_list, compute_shader_dilate_pipeline)
    rd.compute_list_bind_uniform_set(compute_list, compute_base_uniform_set, 0)
    rd.compute_list_bind_uniform_set(compute_list, dilate_uniform_set, 1)

    for i in atlas_slices:
        rd.compute_list_set_push_constant(compute_list, push_constant, push_constant.size())
        rd.compute_list_dispatch(compute_list, group_size.x, group_size.y, group_size.z)
        # No barrier, let them run all together.

    rd.compute_list_end()

---

<span id="class_RenderingDevice_method_compute_list_bind_compute_pipeline"></span>

void **compute_list_bind_compute_pipeline** ( compute_list: [int](class_int.md#class_int), compute_pipeline: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_list_bind_compute_pipeline)

Tells the GPU what compute pipeline to use when processing the compute list. If the shader has changed since the last time this function was called, Godot will unbind all descriptor sets and will re-bind them inside [compute_list_dispatch()](class_renderingdevice.md#class_RenderingDevice_method_compute_list_dispatch).

---

<span id="class_RenderingDevice_method_compute_list_bind_uniform_set"></span>

void **compute_list_bind_uniform_set** ( compute_list: [int](class_int.md#class_int), uniform_set: [RID](class_rid.md#class_RID), set_index: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_list_bind_uniform_set)

Binds the `uniform_set` to this `compute_list`. Godot ensures that all textures in the uniform set have the correct Vulkan access masks. If Godot had to change access masks of textures, it will raise a Vulkan image memory barrier.

---

<span id="class_RenderingDevice_method_compute_list_dispatch"></span>

void **compute_list_dispatch** ( compute_list: [int](class_int.md#class_int), x_groups: [int](class_int.md#class_int), y_groups: [int](class_int.md#class_int), z_groups: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_list_dispatch)

Submits the compute list for processing on the GPU. This is the compute equivalent to [draw_list_draw()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_draw).

---

<span id="class_RenderingDevice_method_compute_list_dispatch_indirect"></span>

void **compute_list_dispatch_indirect** ( compute_list: [int](class_int.md#class_int), buffer: [RID](class_rid.md#class_RID), offset: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_list_dispatch_indirect)

Submits the compute list for processing on the GPU with the given group counts stored in the `buffer` at `offset`. Buffer must have been created with [STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT](class_renderingdevice.md#class_RenderingDevice_constant_STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT) flag.

---

<span id="class_RenderingDevice_method_compute_list_end"></span>

void **compute_list_end** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_list_end)

Finishes a list of compute commands created with the `compute_*` methods.

---

<span id="class_RenderingDevice_method_compute_list_set_push_constant"></span>

void **compute_list_set_push_constant** ( compute_list: [int](class_int.md#class_int), buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), size_bytes: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_list_set_push_constant)

Sets the push constant data to `buffer` for the specified `compute_list`. The shader determines how this binary data is used. The buffer's size in bytes must also be specified in `size_bytes` (this can be obtained by calling the [PackedByteArray.size()](class_packedbytearray.md#class_PackedByteArray_method_size) method on the passed `buffer`).

---

<span id="class_RenderingDevice_method_compute_pipeline_create"></span>

[RID](class_rid.md#class_RID) **compute_pipeline_create** ( shader: [RID](class_rid.md#class_RID), specialization_constants: [Array](class_array.md#class_Array)\[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant)\] = [] ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_pipeline_create)

Creates a new compute pipeline. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

This will be freed automatically when the `shader` is freed.

---

<span id="class_RenderingDevice_method_compute_pipeline_is_valid"></span>

[bool](class_bool.md#class_bool) **compute_pipeline_is_valid** ( compute_pipeline: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_compute_pipeline_is_valid)

Returns `true` if the compute pipeline specified by the `compute_pipeline` RID is valid, `false` otherwise.

---

<span id="class_RenderingDevice_method_create_local_device"></span>

[RenderingDevice](class_renderingdevice.md#class_RenderingDevice) **create_local_device** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_create_local_device)

Create a new local **RenderingDevice**. This is most useful for performing compute operations on the GPU independently from the rest of the engine.

---

<span id="class_RenderingDevice_method_draw_command_begin_label"></span>

void **draw_command_begin_label** ( name: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_command_begin_label)

Create a command buffer debug label region that can be displayed in third-party tools such as RenderDoc. All regions must be ended with a [draw_command_end_label()](class_renderingdevice.md#class_RenderingDevice_method_draw_command_end_label) call. When viewed from the linear series of submissions to a single queue, calls to [draw_command_begin_label()](class_renderingdevice.md#class_RenderingDevice_method_draw_command_begin_label) and [draw_command_end_label()](class_renderingdevice.md#class_RenderingDevice_method_draw_command_end_label) must be matched and balanced.

The `VK_EXT_DEBUG_UTILS_EXTENSION_NAME` Vulkan extension must be available and enabled for command buffer debug label region to work. See also [draw_command_end_label()](class_renderingdevice.md#class_RenderingDevice_method_draw_command_end_label).

---

<span id="class_RenderingDevice_method_draw_command_end_label"></span>

void **draw_command_end_label** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_command_end_label)

Ends the command buffer debug label region started by a [draw_command_begin_label()](class_renderingdevice.md#class_RenderingDevice_method_draw_command_begin_label) call.

---

<span id="class_RenderingDevice_method_draw_command_insert_label"></span>

void **draw_command_insert_label** ( name: [String](class_string.md#class_String), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_command_insert_label)

**Deprecated:** Inserting labels no longer applies due to command reordering.

This method does nothing.

---

<span id="class_RenderingDevice_method_draw_list_begin"></span>

[int](class_int.md#class_int) **draw_list_begin** ( framebuffer: [RID](class_rid.md#class_RID), draw_flags: *BitField*\[[DrawFlags](class_renderingdevice.md#enum_RenderingDevice_DrawFlags)\] = 0, clear_color_values: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) = PackedColorArray(), clear_depth_value: [float](class_float.md#class_float) = 1.0, clear_stencil_value: [int](class_int.md#class_int) = 0, region: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), breadcrumb: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin)

Starts a list of raster drawing commands created with the `draw_*` methods. The returned value should be passed to other `draw_list_*` functions.

Multiple draw lists cannot be created at the same time; you must finish the previous draw list first using [draw_list_end()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_end).

A simple drawing operation might look like this (code is not a complete example):

::

    var rd = RenderingDevice.new()
    var clear_colors = PackedColorArray([Color(0, 0, 0, 0), Color(0, 0, 0, 0), Color(0, 0, 0, 0)])
    var draw_list = rd.draw_list_begin(framebuffers[i], RenderingDevice.CLEAR_COLOR_ALL, clear_colors, true, 1.0f, true, 0, Rect2(), RenderingDevice.OPAQUE_PASS)

    # Draw opaque.
    rd.draw_list_bind_render_pipeline(draw_list, raster_pipeline)
    rd.draw_list_bind_uniform_set(draw_list, raster_base_uniform, 0)
    rd.draw_list_set_push_constant(draw_list, raster_push_constant, raster_push_constant.size())
    rd.draw_list_draw(draw_list, false, 1, slice_triangle_count[i] * 3)
    # Draw wire.
    rd.draw_list_bind_render_pipeline(draw_list, raster_pipeline_wire)
    rd.draw_list_bind_uniform_set(draw_list, raster_base_uniform, 0)
    rd.draw_list_set_push_constant(draw_list, raster_push_constant, raster_push_constant.size())
    rd.draw_list_draw(draw_list, false, 1, slice_triangle_count[i] * 3)

    rd.draw_list_end()

The `draw_flags` indicates if the texture attachments of the framebuffer should be cleared or ignored. Only one of the two flags can be used for each individual attachment. Ignoring an attachment means that any contents that existed before the draw list will be completely discarded, reducing the memory bandwidth used by the render pass but producing garbage results if the pixels aren't replaced. The default behavior allows the engine to figure out the right operation to use if the texture is discardable, which can result in increased performance. See [RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat) or [texture_set_discardable()](class_renderingdevice.md#class_RenderingDevice_method_texture_set_discardable).

The `breadcrumb` parameter can be an arbitrary 32-bit integer that is useful to diagnose GPU crashes. If Godot is built in dev or debug mode; when the GPU crashes Godot will dump all shaders that were being executed at the time of the crash and the breadcrumb is useful to diagnose what passes did those shaders belong to.

It does not affect rendering behavior and can be set to 0. It is recommended to use [BreadcrumbMarker](class_renderingdevice.md#enum_RenderingDevice_BreadcrumbMarker) enumerations for consistency but it's not required. It is also possible to use bitwise operations to add extra data. e.g.

::

    rd.draw_list_begin(fb[i], RenderingDevice.CLEAR_COLOR_ALL, clear_colors, true, 1.0f, true, 0, Rect2(), RenderingDevice.OPAQUE_PASS | 5)

---

<span id="class_RenderingDevice_method_draw_list_begin_for_screen"></span>

[int](class_int.md#class_int) **draw_list_begin_for_screen** ( screen: [int](class_int.md#class_int) = 0, clear_color: [Color](class_color.md#class_Color) = Color(0, 0, 0, 1) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin_for_screen)

High-level variant of [draw_list_begin()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin), with the parameters automatically being adjusted for drawing onto the window specified by the `screen` ID.

 **Note:** Cannot be used with local RenderingDevices, as these don't have a screen. If called on a local RenderingDevice, [draw_list_begin_for_screen()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin_for_screen) returns [INVALID_ID](class_renderingdevice.md#class_RenderingDevice_constant_INVALID_ID).

---

<span id="class_RenderingDevice_method_draw_list_begin_split"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **draw_list_begin_split** ( framebuffer: [RID](class_rid.md#class_RID), splits: [int](class_int.md#class_int), initial_color_action: [InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction), final_color_action: [FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction), initial_depth_action: [InitialAction](class_renderingdevice.md#enum_RenderingDevice_InitialAction), final_depth_action: [FinalAction](class_renderingdevice.md#enum_RenderingDevice_FinalAction), clear_color_values: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) = PackedColorArray(), clear_depth: [float](class_float.md#class_float) = 1.0, clear_stencil: [int](class_int.md#class_int) = 0, region: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0), storage_textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] = [] ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_begin_split)

**Deprecated:** Split draw lists are used automatically by RenderingDevice.

This method does nothing and always returns an empty [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array).

---

<span id="class_RenderingDevice_method_draw_list_bind_index_array"></span>

void **draw_list_bind_index_array** ( draw_list: [int](class_int.md#class_int), index_array: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_index_array)

Binds `index_array` to the specified `draw_list`.

---

<span id="class_RenderingDevice_method_draw_list_bind_render_pipeline"></span>

void **draw_list_bind_render_pipeline** ( draw_list: [int](class_int.md#class_int), render_pipeline: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_render_pipeline)

Binds `render_pipeline` to the specified `draw_list`.

---

<span id="class_RenderingDevice_method_draw_list_bind_uniform_set"></span>

void **draw_list_bind_uniform_set** ( draw_list: [int](class_int.md#class_int), uniform_set: [RID](class_rid.md#class_RID), set_index: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_uniform_set)

Binds `uniform_set` to the specified `draw_list`. A `set_index` must also be specified, which is an identifier starting from `0` that must match the one expected by the draw list.

---

<span id="class_RenderingDevice_method_draw_list_bind_vertex_array"></span>

void **draw_list_bind_vertex_array** ( draw_list: [int](class_int.md#class_int), vertex_array: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_vertex_array)

Binds `vertex_array` to the specified `draw_list`.

---

<span id="class_RenderingDevice_method_draw_list_bind_vertex_buffers_format"></span>

void **draw_list_bind_vertex_buffers_format** ( draw_list: [int](class_int.md#class_int), vertex_format: [int](class_int.md#class_int), vertex_count: [int](class_int.md#class_int), vertex_buffers: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], offsets: [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) = PackedInt64Array() ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_bind_vertex_buffers_format)

Binds a set of `vertex_buffers` directly to the specified `draw_list` using `vertex_format` without creating a vertex array RID. Provide the number of vertices in `vertex_count`; optional per-buffer byte `offsets` may also be supplied.

---

<span id="class_RenderingDevice_method_draw_list_disable_scissor"></span>

void **draw_list_disable_scissor** ( draw_list: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_disable_scissor)

Removes and disables the scissor rectangle for the specified `draw_list`. See also [draw_list_enable_scissor()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_enable_scissor).

---

<span id="class_RenderingDevice_method_draw_list_draw"></span>

void **draw_list_draw** ( draw_list: [int](class_int.md#class_int), use_indices: [bool](class_bool.md#class_bool), instances: [int](class_int.md#class_int), procedural_vertex_count: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_draw)

Submits `draw_list` for rendering on the GPU. This is the raster equivalent to [compute_list_dispatch()](class_renderingdevice.md#class_RenderingDevice_method_compute_list_dispatch).

---

<span id="class_RenderingDevice_method_draw_list_draw_indirect"></span>

void **draw_list_draw_indirect** ( draw_list: [int](class_int.md#class_int), use_indices: [bool](class_bool.md#class_bool), buffer: [RID](class_rid.md#class_RID), offset: [int](class_int.md#class_int) = 0, draw_count: [int](class_int.md#class_int) = 1, stride: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_draw_indirect)

Submits `draw_list` for rendering on the GPU with the given parameters stored in the `buffer` at `offset`. Parameters being integers: vertex count, instance count, first vertex, first instance. And when using indices: index count, instance count, first index, vertex offset, first instance. Buffer must have been created with [STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT](class_renderingdevice.md#class_RenderingDevice_constant_STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT) flag.

---

<span id="class_RenderingDevice_method_draw_list_enable_scissor"></span>

void **draw_list_enable_scissor** ( draw_list: [int](class_int.md#class_int), rect: [Rect2](class_rect2.md#class_Rect2) = Rect2(0, 0, 0, 0) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_enable_scissor)

Creates a scissor rectangle and enables it for the specified `draw_list`. Scissor rectangles are used for clipping by discarding fragments that fall outside a specified rectangular portion of the screen. See also [draw_list_disable_scissor()](class_renderingdevice.md#class_RenderingDevice_method_draw_list_disable_scissor).

 **Note:** The specified `rect` is automatically intersected with the screen's dimensions, which means it cannot exceed the screen's dimensions.

---

<span id="class_RenderingDevice_method_draw_list_end"></span>

void **draw_list_end** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_end)

Finishes a list of raster drawing commands created with the `draw_*` methods.

---

<span id="class_RenderingDevice_method_draw_list_set_blend_constants"></span>

void **draw_list_set_blend_constants** ( draw_list: [int](class_int.md#class_int), color: [Color](class_color.md#class_Color) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_set_blend_constants)

Sets blend constants for the specified `draw_list` to `color`. Blend constants are used only if the graphics pipeline is created with [DYNAMIC_STATE_BLEND_CONSTANTS](class_renderingdevice.md#class_RenderingDevice_constant_DYNAMIC_STATE_BLEND_CONSTANTS) flag set.

---

<span id="class_RenderingDevice_method_draw_list_set_push_constant"></span>

void **draw_list_set_push_constant** ( draw_list: [int](class_int.md#class_int), buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), size_bytes: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_set_push_constant)

Sets the push constant data to `buffer` for the specified `draw_list`. The shader determines how this binary data is used. The buffer's size in bytes must also be specified in `size_bytes` (this can be obtained by calling the [PackedByteArray.size()](class_packedbytearray.md#class_PackedByteArray_method_size) method on the passed `buffer`).

---

<span id="class_RenderingDevice_method_draw_list_switch_to_next_pass"></span>

[int](class_int.md#class_int) **draw_list_switch_to_next_pass** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_switch_to_next_pass)

Switches to the next draw pass.

---

<span id="class_RenderingDevice_method_draw_list_switch_to_next_pass_split"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **draw_list_switch_to_next_pass_split** ( splits: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_draw_list_switch_to_next_pass_split)

**Deprecated:** Split draw lists are used automatically by RenderingDevice.

This method does nothing and always returns an empty [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array).

---

<span id="class_RenderingDevice_method_framebuffer_create"></span>

[RID](class_rid.md#class_RID) **framebuffer_create** ( textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], validate_with_format: [int](class_int.md#class_int) = -1, view_count: [int](class_int.md#class_int) = 1 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_create)

Creates a new framebuffer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

This will be freed automatically when any of the `textures` is freed.

---

<span id="class_RenderingDevice_method_framebuffer_create_empty"></span>

[RID](class_rid.md#class_RID) **framebuffer_create_empty** ( size: [Vector2i](class_vector2i.md#class_Vector2i), samples: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) = 0, validate_with_format: [int](class_int.md#class_int) = -1 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_create_empty)

Creates a new empty framebuffer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

---

<span id="class_RenderingDevice_method_framebuffer_create_multipass"></span>

[RID](class_rid.md#class_RID) **framebuffer_create_multipass** ( textures: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], passes: [Array](class_array.md#class_Array)\[[RDFramebufferPass](class_rdframebufferpass.md#class_RDFramebufferPass)\], validate_with_format: [int](class_int.md#class_int) = -1, view_count: [int](class_int.md#class_int) = 1 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_create_multipass)

Creates a new multipass framebuffer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

This will be freed automatically when any of the `textures` is freed.

---

<span id="class_RenderingDevice_method_framebuffer_format_create"></span>

[int](class_int.md#class_int) **framebuffer_format_create** ( attachments: [Array](class_array.md#class_Array)\[[RDAttachmentFormat](class_rdattachmentformat.md#class_RDAttachmentFormat)\], view_count: [int](class_int.md#class_int) = 1 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_format_create)

Creates a new framebuffer format with the specified `attachments` and `view_count`. Returns the new framebuffer's unique framebuffer format ID.

If `view_count` is greater than or equal to `2`, enables multiview which is used for VR rendering. This requires support for the Vulkan multiview extension.

---

<span id="class_RenderingDevice_method_framebuffer_format_create_empty"></span>

[int](class_int.md#class_int) **framebuffer_format_create_empty** ( samples: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_format_create_empty)

Creates a new empty framebuffer format with the specified number of `samples` and returns its ID.

---

<span id="class_RenderingDevice_method_framebuffer_format_create_multipass"></span>

[int](class_int.md#class_int) **framebuffer_format_create_multipass** ( attachments: [Array](class_array.md#class_Array)\[[RDAttachmentFormat](class_rdattachmentformat.md#class_RDAttachmentFormat)\], passes: [Array](class_array.md#class_Array)\[[RDFramebufferPass](class_rdframebufferpass.md#class_RDFramebufferPass)\], view_count: [int](class_int.md#class_int) = 1 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_format_create_multipass)

Creates a multipass framebuffer format with the specified `attachments`, `passes` and `view_count` and returns its ID. If `view_count` is greater than or equal to `2`, enables multiview which is used for VR rendering. This requires support for the Vulkan multiview extension.

---

<span id="class_RenderingDevice_method_framebuffer_format_get_texture_samples"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **framebuffer_format_get_texture_samples** ( format: [int](class_int.md#class_int), render_pass: [int](class_int.md#class_int) = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_format_get_texture_samples)

Returns the number of texture samples used for the given framebuffer `format` ID (returned by [framebuffer_get_format()](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_get_format)).

---

<span id="class_RenderingDevice_method_framebuffer_get_format"></span>

[int](class_int.md#class_int) **framebuffer_get_format** ( framebuffer: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_get_format)

Returns the format ID of the framebuffer specified by the `framebuffer` RID. This ID is guaranteed to be unique for the same formats and does not need to be freed.

---

<span id="class_RenderingDevice_method_framebuffer_is_valid"></span>

[bool](class_bool.md#class_bool) **framebuffer_is_valid** ( framebuffer: [RID](class_rid.md#class_RID) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_framebuffer_is_valid)

Returns `true` if the framebuffer specified by the `framebuffer` RID is valid, `false` otherwise.

---

<span id="class_RenderingDevice_method_free_rid"></span>

void **free_rid** ( rid: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_free_rid)

Tries to free an object in the RenderingDevice. To avoid memory leaks, this should be called after using an object as memory management does not occur automatically when using RenderingDevice directly.

---

<span id="class_RenderingDevice_method_full_barrier"></span>

void **full_barrier** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_full_barrier)

**Deprecated:** Barriers are automatically inserted by RenderingDevice.

This method does nothing.

---

<span id="class_RenderingDevice_method_get_captured_timestamp_cpu_time"></span>

[int](class_int.md#class_int) **get_captured_timestamp_cpu_time** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_cpu_time)

Returns the timestamp in CPU time for the rendering step specified by `index` (in microseconds since the engine started). See also [get_captured_timestamp_gpu_time()](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_gpu_time) and [capture_timestamp()](class_renderingdevice.md#class_RenderingDevice_method_capture_timestamp).

---

<span id="class_RenderingDevice_method_get_captured_timestamp_gpu_time"></span>

[int](class_int.md#class_int) **get_captured_timestamp_gpu_time** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_gpu_time)

Returns the timestamp in GPU time for the rendering step specified by `index` (in microseconds since the engine started). See also [get_captured_timestamp_cpu_time()](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_cpu_time) and [capture_timestamp()](class_renderingdevice.md#class_RenderingDevice_method_capture_timestamp).

---

<span id="class_RenderingDevice_method_get_captured_timestamp_name"></span>

[String](class_string.md#class_String) **get_captured_timestamp_name** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamp_name)

Returns the timestamp's name for the rendering step specified by `index`. See also [capture_timestamp()](class_renderingdevice.md#class_RenderingDevice_method_capture_timestamp).

---

<span id="class_RenderingDevice_method_get_captured_timestamps_count"></span>

[int](class_int.md#class_int) **get_captured_timestamps_count** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamps_count)

Returns the total number of timestamps (rendering steps) available for profiling.

---

<span id="class_RenderingDevice_method_get_captured_timestamps_frame"></span>

[int](class_int.md#class_int) **get_captured_timestamps_frame** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_captured_timestamps_frame)

Returns the index of the last frame rendered that has rendering timestamps available for querying.

---

<span id="class_RenderingDevice_method_get_device_allocation_count"></span>

[int](class_int.md#class_int) **get_device_allocation_count** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_device_allocation_count)

Returns how many allocations the GPU has performed for internal driver structures.

This is only used by Vulkan in debug builds and can return 0 when this information is not tracked or unknown.

---

<span id="class_RenderingDevice_method_get_device_allocs_by_object_type"></span>

[int](class_int.md#class_int) **get_device_allocs_by_object_type** ( type: [int](class_int.md#class_int) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_device_allocs_by_object_type)

Same as [get_device_allocation_count()](class_renderingdevice.md#class_RenderingDevice_method_get_device_allocation_count) but filtered for a given object type.

The type argument must be in range `[0; get_tracked_object_type_count - 1]`. If [get_tracked_object_type_count()](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_type_count) is 0, then type argument is ignored and always returns 0.

This is only used by Vulkan in debug builds and can return 0 when this information is not tracked or unknown.

---

<span id="class_RenderingDevice_method_get_device_memory_by_object_type"></span>

[int](class_int.md#class_int) **get_device_memory_by_object_type** ( type: [int](class_int.md#class_int) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_device_memory_by_object_type)

Same as [get_device_total_memory()](class_renderingdevice.md#class_RenderingDevice_method_get_device_total_memory) but filtered for a given object type.

The type argument must be in range `[0; get_tracked_object_type_count - 1]`. If [get_tracked_object_type_count()](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_type_count) is 0, then type argument is ignored and always returns 0.

This is only used by Vulkan in debug builds and can return 0 when this information is not tracked or unknown.

---

<span id="class_RenderingDevice_method_get_device_name"></span>

[String](class_string.md#class_String) **get_device_name** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_device_name)

Returns the name of the video adapter (e.g. "GeForce GTX 1080/PCIe/SSE2"). Equivalent to [RenderingServer.get_video_adapter_name()](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_name). See also [get_device_vendor_name()](class_renderingdevice.md#class_RenderingDevice_method_get_device_vendor_name).

---

<span id="class_RenderingDevice_method_get_device_pipeline_cache_uuid"></span>

[String](class_string.md#class_String) **get_device_pipeline_cache_uuid** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_device_pipeline_cache_uuid)

Returns the universally unique identifier for the pipeline cache. This is used to cache shader files on disk, which avoids shader recompilations on subsequent engine runs. This UUID varies depending on the graphics card model, but also the driver version. Therefore, updating graphics drivers will invalidate the shader cache.

---

<span id="class_RenderingDevice_method_get_device_total_memory"></span>

[int](class_int.md#class_int) **get_device_total_memory** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_device_total_memory)

Returns how much bytes the GPU is using.

This is only used by Vulkan in debug builds and can return 0 when this information is not tracked or unknown.

---

<span id="class_RenderingDevice_method_get_device_vendor_name"></span>

[String](class_string.md#class_String) **get_device_vendor_name** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_device_vendor_name)

Returns the vendor of the video adapter (e.g. "NVIDIA Corporation"). Equivalent to [RenderingServer.get_video_adapter_vendor()](class_renderingserver.md#class_RenderingServer_method_get_video_adapter_vendor). See also [get_device_name()](class_renderingdevice.md#class_RenderingDevice_method_get_device_name).

---

<span id="class_RenderingDevice_method_get_driver_allocation_count"></span>

[int](class_int.md#class_int) **get_driver_allocation_count** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_driver_allocation_count)

Returns how many allocations the GPU driver has performed for internal driver structures.

This is only used by Vulkan in debug builds and can return 0 when this information is not tracked or unknown.

---

<span id="class_RenderingDevice_method_get_driver_allocs_by_object_type"></span>

[int](class_int.md#class_int) **get_driver_allocs_by_object_type** ( type: [int](class_int.md#class_int) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_driver_allocs_by_object_type)

Same as [get_driver_allocation_count()](class_renderingdevice.md#class_RenderingDevice_method_get_driver_allocation_count) but filtered for a given object type.

The type argument must be in range `[0; get_tracked_object_type_count - 1]`. If [get_tracked_object_type_count()](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_type_count) is 0, then type argument is ignored and always returns 0.

This is only used by Vulkan in debug builds and can return 0 when this information is not tracked or unknown.

---

<span id="class_RenderingDevice_method_get_driver_and_device_memory_report"></span>

[String](class_string.md#class_String) **get_driver_and_device_memory_report** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_driver_and_device_memory_report)

Returns string report in CSV format using the following methods:

- [get_tracked_object_name()](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_name)

- [get_tracked_object_type_count()](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_type_count)

- [get_driver_total_memory()](class_renderingdevice.md#class_RenderingDevice_method_get_driver_total_memory)

- [get_driver_allocation_count()](class_renderingdevice.md#class_RenderingDevice_method_get_driver_allocation_count)

- [get_driver_memory_by_object_type()](class_renderingdevice.md#class_RenderingDevice_method_get_driver_memory_by_object_type)

- [get_driver_allocs_by_object_type()](class_renderingdevice.md#class_RenderingDevice_method_get_driver_allocs_by_object_type)

- [get_device_total_memory()](class_renderingdevice.md#class_RenderingDevice_method_get_device_total_memory)

- [get_device_allocation_count()](class_renderingdevice.md#class_RenderingDevice_method_get_device_allocation_count)

- [get_device_memory_by_object_type()](class_renderingdevice.md#class_RenderingDevice_method_get_device_memory_by_object_type)

- [get_device_allocs_by_object_type()](class_renderingdevice.md#class_RenderingDevice_method_get_device_allocs_by_object_type)

This is only used by Vulkan in debug builds. Godot must also be started with the `--extra-gpu-memory-tracking` [command line argument](../tutorials/editor/command_line_tutorial.md).

---

<span id="class_RenderingDevice_method_get_driver_memory_by_object_type"></span>

[int](class_int.md#class_int) **get_driver_memory_by_object_type** ( type: [int](class_int.md#class_int) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_driver_memory_by_object_type)

Same as [get_driver_total_memory()](class_renderingdevice.md#class_RenderingDevice_method_get_driver_total_memory) but filtered for a given object type.

The type argument must be in range `[0; get_tracked_object_type_count - 1]`. If [get_tracked_object_type_count()](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_type_count) is 0, then type argument is ignored and always returns 0.

This is only used by Vulkan in debug builds and can return 0 when this information is not tracked or unknown.

---

<span id="class_RenderingDevice_method_get_driver_resource"></span>

[int](class_int.md#class_int) **get_driver_resource** ( resource: [DriverResource](class_renderingdevice.md#enum_RenderingDevice_DriverResource), rid: [RID](class_rid.md#class_RID), index: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_driver_resource)

Returns the unique identifier of the driver `resource` for the specified `rid`. Some driver resource types ignore the specified `rid`. `index` is always ignored but must be specified anyway.

---

<span id="class_RenderingDevice_method_get_driver_total_memory"></span>

[int](class_int.md#class_int) **get_driver_total_memory** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_driver_total_memory)

Returns how much bytes the GPU driver is using for internal driver structures.

This is only used by Vulkan in debug builds and can return 0 when this information is not tracked or unknown.

---

<span id="class_RenderingDevice_method_get_frame_delay"></span>

[int](class_int.md#class_int) **get_frame_delay** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_frame_delay)

Returns the frame count kept by the graphics API. Higher values result in higher input lag, but with more consistent throughput. For the main **RenderingDevice**, frames are cycled (usually 3 with triple-buffered V-Sync enabled). However, local **RenderingDevice** s only have 1 frame.

---

<span id="class_RenderingDevice_method_get_memory_usage"></span>

[int](class_int.md#class_int) **get_memory_usage** ( type: [MemoryType](class_renderingdevice.md#enum_RenderingDevice_MemoryType) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_memory_usage)

Returns the memory usage in bytes corresponding to the given `type`. When using Vulkan, these statistics are calculated by Vulkan Memory Allocator.

---

<span id="class_RenderingDevice_method_get_perf_report"></span>

[String](class_string.md#class_String) **get_perf_report** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_perf_report)

Returns a string with a performance report from the past frame. Updates every frame.

---

<span id="class_RenderingDevice_method_get_tracked_object_name"></span>

[String](class_string.md#class_String) **get_tracked_object_name** ( type_index: [int](class_int.md#class_int) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_name)

Returns the name of the type of object for the given `type_index`. This value must be in range `[0; get_tracked_object_type_count - 1]`. If [get_tracked_object_type_count()](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_type_count) is 0, then type argument is ignored and always returns the same string.

The return value is important because it gives meaning to the types passed to [get_driver_memory_by_object_type()](class_renderingdevice.md#class_RenderingDevice_method_get_driver_memory_by_object_type), [get_driver_allocs_by_object_type()](class_renderingdevice.md#class_RenderingDevice_method_get_driver_allocs_by_object_type), [get_device_memory_by_object_type()](class_renderingdevice.md#class_RenderingDevice_method_get_device_memory_by_object_type), and [get_device_allocs_by_object_type()](class_renderingdevice.md#class_RenderingDevice_method_get_device_allocs_by_object_type). Examples of strings it can return (not exhaustive):

- DEVICE_MEMORY

- PIPELINE_CACHE

- SWAPCHAIN_KHR

- COMMAND_POOL

Thus if e.g. `get_tracked_object_name(5)` returns "COMMAND_POOL", then `get_device_memory_by_object_type(5)` returns the bytes used by the GPU for command pools.

This is only used by Vulkan in debug builds. Godot must also be started with the `--extra-gpu-memory-tracking` [command line argument](../tutorials/editor/command_line_tutorial.md).

---

<span id="class_RenderingDevice_method_get_tracked_object_type_count"></span>

[int](class_int.md#class_int) **get_tracked_object_type_count** ( ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_get_tracked_object_type_count)

Returns how many types of trackable objects there are.

This is only used by Vulkan in debug builds. Godot must also be started with the `--extra-gpu-memory-tracking` [command line argument](../tutorials/editor/command_line_tutorial.md).

---

<span id="class_RenderingDevice_method_has_feature"></span>

[bool](class_bool.md#class_bool) **has_feature** ( feature: [Features](class_renderingdevice.md#enum_RenderingDevice_Features) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_has_feature)

Returns `true` if the `feature` is supported by the GPU.

---

<span id="class_RenderingDevice_method_index_array_create"></span>

[RID](class_rid.md#class_RID) **index_array_create** ( index_buffer: [RID](class_rid.md#class_RID), index_offset: [int](class_int.md#class_int), index_count: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_index_array_create)

Creates a new index array. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

This will be freed automatically when the `index_buffer` is freed.

---

<span id="class_RenderingDevice_method_index_buffer_create"></span>

[RID](class_rid.md#class_RID) **index_buffer_create** ( size_indices: [int](class_int.md#class_int), format: [IndexBufferFormat](class_renderingdevice.md#enum_RenderingDevice_IndexBufferFormat), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray(), use_restart_indices: [bool](class_bool.md#class_bool) = false, creation_bits: *BitField*\[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_index_buffer_create)

Creates a new index buffer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

---

<span id="class_RenderingDevice_method_limit_get"></span>

[int](class_int.md#class_int) **limit_get** ( limit: [Limit](class_renderingdevice.md#enum_RenderingDevice_Limit) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_limit_get)

Returns the value of the specified `limit`. This limit varies depending on the current graphics hardware (and sometimes the driver version). If the given limit is exceeded, rendering errors will occur.

Limits for various graphics hardware can be found in the Vulkan Hardware Database.

---

<span id="class_RenderingDevice_method_raytracing_list_begin"></span>

[int](class_int.md#class_int) **raytracing_list_begin** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_begin)

Starts a list of raytracing commands. The returned value should be passed to other `raytracing_list_*` functions.

Multiple raytracing lists cannot be created at the same time; you must finish the previous raytracing list first using [raytracing_list_end()](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_end).

A simple raytracing operation might look like this (code is not a complete example):

.. tabs::

```
```

    var rd = RenderingDevice.new()
    assert(rd.has_feature(RenderingDevice.SUPPORTS_RAYTRACING_PIPELINE))

    # Create a BLAS for a mesh.
    blas = rd.blas_create(vertex_array, index_array, RenderingDevice.ACCELERATION_STRUCTURE_GEOMETRY_OPAQUE)
    # Create TLAS with BLASs.
    instances_buffer = rd.tlas_instances_buffer_create(1)
    rd.tlas_instances_buffer_fill(instances_buffer, [blas], [Transform3D()])
    tlas = rd.tlas_create(instances_buffer)

    # Build acceleration structures.
    rd.acceleration_structure_build(blas)
    rd.acceleration_structure_build(tlas)

    var raylist = rd.raytracing_list_begin()

    # Bind pipeline and uniforms.
    rd.raytracing_list_bind_raytracing_pipeline(raylist, raytracing_pipeline)
    rd.raytracing_list_bind_uniform_set(raylist, uniform_set, 0)

    # Trace rays.
    var width = get_viewport().size.x
    var height = get_viewport().size.y
    rd.raytracing_list_trace_rays(raylist, width, height)

    rd.raytracing_list_end()

---

<span id="class_RenderingDevice_method_raytracing_list_bind_raytracing_pipeline"></span>

void **raytracing_list_bind_raytracing_pipeline** ( raytracing_list: [int](class_int.md#class_int), raytracing_pipeline: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_bind_raytracing_pipeline)

Binds `raytracing_pipeline` to the specified `raytracing_list`.

---

<span id="class_RenderingDevice_method_raytracing_list_bind_uniform_set"></span>

void **raytracing_list_bind_uniform_set** ( raytracing_list: [int](class_int.md#class_int), uniform_set: [RID](class_rid.md#class_RID), set_index: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_bind_uniform_set)

Binds the `uniform_set` to this `raytracing_list`.

---

<span id="class_RenderingDevice_method_raytracing_list_end"></span>

void **raytracing_list_end** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_end)

Finishes a list of raytracing commands created with the `raytracing_*` methods.

---

<span id="class_RenderingDevice_method_raytracing_list_set_push_constant"></span>

void **raytracing_list_set_push_constant** ( raytracing_list: [int](class_int.md#class_int), buffer: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), size_bytes: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_set_push_constant)

Sets the push constant data to `buffer` for the specified `raytracing_list`. The shader determines how this binary data is used. The buffer's size in bytes must also be specified in `size_bytes` (this can be obtained by calling the [PackedByteArray.size()](class_packedbytearray.md#class_PackedByteArray_method_size) method on the passed `buffer`).

---

<span id="class_RenderingDevice_method_raytracing_list_trace_rays"></span>

void **raytracing_list_trace_rays** ( raytracing_list: [int](class_int.md#class_int), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_raytracing_list_trace_rays)

Initializes a ray tracing dispatch for the specified `raytracing_list` assembling a group of `width` x `height` rays.

---

<span id="class_RenderingDevice_method_raytracing_pipeline_create"></span>

[RID](class_rid.md#class_RID) **raytracing_pipeline_create** ( shader: [RID](class_rid.md#class_RID), specialization_constants: [Array](class_array.md#class_Array)\[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant)\] = [] ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_raytracing_pipeline_create)

Creates a new raytracing pipeline. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

 **Note:**: Recursive raytracing is not permitted.

---

<span id="class_RenderingDevice_method_raytracing_pipeline_is_valid"></span>

[bool](class_bool.md#class_bool) **raytracing_pipeline_is_valid** ( raytracing_pipeline: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_raytracing_pipeline_is_valid)

Returns `true` if the raytracing pipeline specified by the `raytracing_pipeline` RID is valid, `false` otherwise.

---

<span id="class_RenderingDevice_method_render_pipeline_create"></span>

[RID](class_rid.md#class_RID) **render_pipeline_create** ( shader: [RID](class_rid.md#class_RID), framebuffer_format: [int](class_int.md#class_int), vertex_format: [int](class_int.md#class_int), primitive: [RenderPrimitive](class_renderingdevice.md#enum_RenderingDevice_RenderPrimitive), rasterization_state: [RDPipelineRasterizationState](class_rdpipelinerasterizationstate.md#class_RDPipelineRasterizationState), multisample_state: [RDPipelineMultisampleState](class_rdpipelinemultisamplestate.md#class_RDPipelineMultisampleState), stencil_state: [RDPipelineDepthStencilState](class_rdpipelinedepthstencilstate.md#class_RDPipelineDepthStencilState), color_blend_state: [RDPipelineColorBlendState](class_rdpipelinecolorblendstate.md#class_RDPipelineColorBlendState), dynamic_state_flags: *BitField*\[[PipelineDynamicStateFlags](class_renderingdevice.md#enum_RenderingDevice_PipelineDynamicStateFlags)\] = 0, for_render_pass: [int](class_int.md#class_int) = 0, specialization_constants: [Array](class_array.md#class_Array)\[[RDPipelineSpecializationConstant](class_rdpipelinespecializationconstant.md#class_RDPipelineSpecializationConstant)\] = [] ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_render_pipeline_create)

Creates a new render pipeline. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

This will be freed automatically when the `shader` is freed.

---

<span id="class_RenderingDevice_method_render_pipeline_is_valid"></span>

[bool](class_bool.md#class_bool) **render_pipeline_is_valid** ( render_pipeline: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_render_pipeline_is_valid)

Returns `true` if the render pipeline specified by the `render_pipeline` RID is valid, `false` otherwise.

---

<span id="class_RenderingDevice_method_sampler_create"></span>

[RID](class_rid.md#class_RID) **sampler_create** ( state: [RDSamplerState](class_rdsamplerstate.md#class_RDSamplerState) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_sampler_create)

Creates a new sampler. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

---

<span id="class_RenderingDevice_method_sampler_is_format_supported_for_filter"></span>

[bool](class_bool.md#class_bool) **sampler_is_format_supported_for_filter** ( format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), sampler_filter: [SamplerFilter](class_renderingdevice.md#enum_RenderingDevice_SamplerFilter) ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_sampler_is_format_supported_for_filter)

Returns `true` if implementation supports using a texture of `format` with the given `sampler_filter`.

---

<span id="class_RenderingDevice_method_screen_get_framebuffer_format"></span>

[int](class_int.md#class_int) **screen_get_framebuffer_format** ( screen: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_screen_get_framebuffer_format)

Returns the framebuffer format of the given screen.

 **Note:** Only the main **RenderingDevice** returned by [RenderingServer.get_rendering_device()](class_renderingserver.md#class_RenderingServer_method_get_rendering_device) has a format. If called on a local **RenderingDevice**, this method prints an error and returns [INVALID_ID](class_renderingdevice.md#class_RenderingDevice_constant_INVALID_ID).

---

<span id="class_RenderingDevice_method_screen_get_height"></span>

[int](class_int.md#class_int) **screen_get_height** ( screen: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_screen_get_height)

Returns the window height matching the graphics API context for the given window ID (in pixels). Despite the parameter being named `screen`, this returns the *window* size. See also [screen_get_width()](class_renderingdevice.md#class_RenderingDevice_method_screen_get_width).

 **Note:** Only the main **RenderingDevice** returned by [RenderingServer.get_rendering_device()](class_renderingserver.md#class_RenderingServer_method_get_rendering_device) has a height. If called on a local **RenderingDevice**, this method prints an error and returns [INVALID_ID](class_renderingdevice.md#class_RenderingDevice_constant_INVALID_ID).

---

<span id="class_RenderingDevice_method_screen_get_width"></span>

[int](class_int.md#class_int) **screen_get_width** ( screen: [int](class_int.md#class_int) = 0 ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_screen_get_width)

Returns the window width matching the graphics API context for the given window ID (in pixels). Despite the parameter being named `screen`, this returns the *window* size. See also [screen_get_height()](class_renderingdevice.md#class_RenderingDevice_method_screen_get_height).

 **Note:** Only the main **RenderingDevice** returned by [RenderingServer.get_rendering_device()](class_renderingserver.md#class_RenderingServer_method_get_rendering_device) has a width. If called on a local **RenderingDevice**, this method prints an error and returns [INVALID_ID](class_renderingdevice.md#class_RenderingDevice_constant_INVALID_ID).

---

<span id="class_RenderingDevice_method_set_resource_name"></span>

void **set_resource_name** ( id: [RID](class_rid.md#class_RID), name: [String](class_string.md#class_String) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_set_resource_name)

Sets the resource name for `id` to `name`. This is used for debugging with third-party tools such as RenderDoc.

The following types of resources can be named: texture, sampler, vertex buffer, index buffer, uniform buffer, texture buffer, storage buffer, uniform set buffer, shader, render pipeline and compute pipeline. Framebuffers cannot be named. Attempting to name an incompatible resource type will print an error.

 **Note:** Resource names are only set when the engine runs in verbose mode ([OS.is_stdout_verbose()](class_os.md#class_OS_method_is_stdout_verbose) = `true`), or when using an engine build compiled with the `dev_mode=yes` SCons option. The graphics driver must also support the `VK_EXT_DEBUG_UTILS_EXTENSION_NAME` Vulkan extension for named resources to work.

---

<span id="class_RenderingDevice_method_shader_compile_binary_from_spirv"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **shader_compile_binary_from_spirv** ( spirv_data: [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV), name: [String](class_string.md#class_String) = "" ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_shader_compile_binary_from_spirv)

Compiles a binary shader from `spirv_data` and returns the compiled binary data as a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray). This compiled shader is specific to the GPU model and driver version used; it will not work on different GPU models or even different driver versions. See also [shader_compile_spirv_from_source()](class_renderingdevice.md#class_RenderingDevice_method_shader_compile_spirv_from_source).

 `name` is an optional human-readable name that can be given to the compiled shader for organizational purposes.

---

<span id="class_RenderingDevice_method_shader_compile_spirv_from_source"></span>

[RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV) **shader_compile_spirv_from_source** ( shader_source: [RDShaderSource](class_rdshadersource.md#class_RDShaderSource), allow_cache: [bool](class_bool.md#class_bool) = true ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_shader_compile_spirv_from_source)

Compiles a SPIR-V from the shader source code in `shader_source` and returns the SPIR-V as an [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV). This intermediate language shader is portable across different GPU models and driver versions, but cannot be run directly by GPUs until compiled into a binary shader using [shader_compile_binary_from_spirv()](class_renderingdevice.md#class_RenderingDevice_method_shader_compile_binary_from_spirv).

If `allow_cache` is `true`, make use of the shader cache generated by Godot. This avoids a potentially lengthy shader compilation step if the shader is already in cache. If `allow_cache` is `false`, Godot's shader cache is ignored and the shader will always be recompiled.

---

<span id="class_RenderingDevice_method_shader_create_from_bytecode"></span>

[RID](class_rid.md#class_RID) **shader_create_from_bytecode** ( binary_data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), placeholder_rid: [RID](class_rid.md#class_RID) = RID() ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_shader_create_from_bytecode)

Creates a new shader instance from a binary compiled shader. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method. See also [shader_compile_binary_from_spirv()](class_renderingdevice.md#class_RenderingDevice_method_shader_compile_binary_from_spirv) and [shader_create_from_spirv()](class_renderingdevice.md#class_RenderingDevice_method_shader_create_from_spirv).

---

<span id="class_RenderingDevice_method_shader_create_from_spirv"></span>

[RID](class_rid.md#class_RID) **shader_create_from_spirv** ( spirv_data: [RDShaderSPIRV](class_rdshaderspirv.md#class_RDShaderSPIRV), name: [String](class_string.md#class_String) = "" ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_shader_create_from_spirv)

Creates a new shader instance from SPIR-V intermediate code. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method. See also [shader_compile_spirv_from_source()](class_renderingdevice.md#class_RenderingDevice_method_shader_compile_spirv_from_source) and [shader_create_from_bytecode()](class_renderingdevice.md#class_RenderingDevice_method_shader_create_from_bytecode).

---

<span id="class_RenderingDevice_method_shader_create_placeholder"></span>

[RID](class_rid.md#class_RID) **shader_create_placeholder** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_shader_create_placeholder)

Create a placeholder RID by allocating an RID without initializing it for use in [shader_create_from_bytecode()](class_renderingdevice.md#class_RenderingDevice_method_shader_create_from_bytecode). This allows you to create an RID for a shader and pass it around, but defer compiling the shader to a later time.

---

<span id="class_RenderingDevice_method_shader_get_vertex_input_attribute_mask"></span>

[int](class_int.md#class_int) **shader_get_vertex_input_attribute_mask** ( shader: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_shader_get_vertex_input_attribute_mask)

Returns the internal vertex input mask. Internally, the vertex input mask is an unsigned integer consisting of the locations (specified in GLSL via. `layout(location = ...)`) of the input variables (specified in GLSL by the `in` keyword).

---

<span id="class_RenderingDevice_method_storage_buffer_create"></span>

[RID](class_rid.md#class_RID) **storage_buffer_create** ( size_bytes: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray(), usage: *BitField*\[[StorageBufferUsage](class_renderingdevice.md#enum_RenderingDevice_StorageBufferUsage)\] = 0, creation_bits: *BitField*\[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_storage_buffer_create)

Creates a storage buffer with the specified `data` and `usage`. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

---

<span id="class_RenderingDevice_method_submit"></span>

void **submit** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_submit)

Pushes the frame setup and draw command buffers then marks the local device as currently processing (which allows calling [sync()](class_renderingdevice.md#class_RenderingDevice_method_sync)).

 **Note:** Only available in local RenderingDevices.

---

<span id="class_RenderingDevice_method_sync"></span>

void **sync** ( ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_sync)

Forces a synchronization between the CPU and GPU, which may be required in certain cases. Only call this when needed, as CPU-GPU synchronization has a performance cost.

 **Note:** Only available in local RenderingDevices.

 **Note:** [sync()](class_renderingdevice.md#class_RenderingDevice_method_sync) can only be called after a [submit()](class_renderingdevice.md#class_RenderingDevice_method_submit).

---

<span id="class_RenderingDevice_method_texture_buffer_create"></span>

[RID](class_rid.md#class_RID) **texture_buffer_create** ( size_bytes: [int](class_int.md#class_int), format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray() ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_buffer_create)

Creates a new texture buffer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

---

<span id="class_RenderingDevice_method_texture_clear"></span>

Error **texture_clear** ( texture: [RID](class_rid.md#class_RID), color: [Color](class_color.md#class_Color), base_mipmap: [int](class_int.md#class_int), mipmap_count: [int](class_int.md#class_int), base_layer: [int](class_int.md#class_int), layer_count: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_clear)

Clears the specified `texture` by replacing all of its pixels with the specified `color`. `base_mipmap` and `mipmap_count` determine which mipmaps of the texture are affected by this clear operation, while `base_layer` and `layer_count` determine which layers of a 3D texture (or texture array) are affected by this clear operation. For 2D textures (which only have one layer by design), `base_layer` must be `0` and `layer_count` must be `1`.

 **Note:** `texture` can't be cleared while a draw list that uses it as part of a framebuffer is being created. Ensure the draw list is finalized (and that the color/depth texture using it is not set to [FINAL_ACTION_CONTINUE](class_renderingdevice.md#class_RenderingDevice_constant_FINAL_ACTION_CONTINUE)) to clear this texture.

---

<span id="class_RenderingDevice_method_texture_copy"></span>

Error **texture_copy** ( from_texture: [RID](class_rid.md#class_RID), to_texture: [RID](class_rid.md#class_RID), from_pos: [Vector3](class_vector3.md#class_Vector3), to_pos: [Vector3](class_vector3.md#class_Vector3), size: [Vector3](class_vector3.md#class_Vector3), src_mipmap: [int](class_int.md#class_int), dst_mipmap: [int](class_int.md#class_int), src_layer: [int](class_int.md#class_int), dst_layer: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_copy)

Copies the `from_texture` to `to_texture` with the specified `from_pos`, `to_pos` and `size` coordinates. The Z axis of the `from_pos`, `to_pos` and `size` must be `0` for 2-dimensional textures. Source and destination mipmaps/layers must also be specified, with these parameters being `0` for textures without mipmaps or single-layer textures. Returns @GlobalScope.OK if the texture copy was successful or @GlobalScope.ERR_INVALID_PARAMETER otherwise.

 **Note:** `from_texture` texture can't be copied while a draw list that uses it as part of a framebuffer is being created. Ensure the draw list is finalized (and that the color/depth texture using it is not set to [FINAL_ACTION_CONTINUE](class_renderingdevice.md#class_RenderingDevice_constant_FINAL_ACTION_CONTINUE)) to copy this texture.

 **Note:** `from_texture` texture requires the [TEXTURE_USAGE_CAN_COPY_FROM_BIT](class_renderingdevice.md#class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_FROM_BIT) to be retrieved.

 **Note:** `to_texture` can't be copied while a draw list that uses it as part of a framebuffer is being created. Ensure the draw list is finalized (and that the color/depth texture using it is not set to [FINAL_ACTION_CONTINUE](class_renderingdevice.md#class_RenderingDevice_constant_FINAL_ACTION_CONTINUE)) to copy this texture.

 **Note:** `to_texture` requires the [TEXTURE_USAGE_CAN_COPY_TO_BIT](class_renderingdevice.md#class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_TO_BIT) to be retrieved.

 **Note:** `from_texture` and `to_texture` must be of the same type (color or depth).

---

<span id="class_RenderingDevice_method_texture_create"></span>

[RID](class_rid.md#class_RID) **texture_create** ( format: [RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat), view: [RDTextureView](class_rdtextureview.md#class_RDTextureView), data: [Array](class_array.md#class_Array)\[[PackedByteArray](class_packedbytearray.md#class_PackedByteArray)\] = [] ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_create)

Creates a new texture. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

 **Note:** `data` takes an [Array](class_array.md#class_Array) of [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) s. For [TEXTURE_TYPE_1D](class_renderingdevice.md#class_RenderingDevice_constant_TEXTURE_TYPE_1D), [TEXTURE_TYPE_2D](class_renderingdevice.md#class_RenderingDevice_constant_TEXTURE_TYPE_2D), and [TEXTURE_TYPE_3D](class_renderingdevice.md#class_RenderingDevice_constant_TEXTURE_TYPE_3D) types, this array should only have one element, a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) containing all the data for the texture. For `_ARRAY` and `_CUBE` types, the length should be the same as the number of [RDTextureFormat.array_layers](class_rdtextureformat.md#class_RDTextureFormat_property_array_layers) in `format`.

 **Note:** Not to be confused with [RenderingServer.texture_2d_create()](class_renderingserver.md#class_RenderingServer_method_texture_2d_create), which creates the Godot-specific [Texture2D](class_texture2d.md#class_Texture2D) resource as opposed to the graphics API's own texture type.

---

<span id="class_RenderingDevice_method_texture_create_from_extension"></span>

[RID](class_rid.md#class_RID) **texture_create_from_extension** ( type: [TextureType](class_renderingdevice.md#enum_RenderingDevice_TextureType), format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), samples: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples), usage_flags: *BitField*\[[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits)\], image: [int](class_int.md#class_int), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), depth: [int](class_int.md#class_int), layers: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int) = 1 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_create_from_extension)

Returns an RID for an existing `image` (`VkImage`) with the given `type`, `format`, `samples`, `usage_flags`, `width`, `height`, `depth`, `layers`, and `mipmaps`. This can be used to allow Godot to render onto foreign images.

---

<span id="class_RenderingDevice_method_texture_create_shared"></span>

[RID](class_rid.md#class_RID) **texture_create_shared** ( view: [RDTextureView](class_rdtextureview.md#class_RDTextureView), with_texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_create_shared)

Creates a shared texture using the specified `view` and the texture information from `with_texture`.

This will be freed automatically when the `with_texture` is freed.

---

<span id="class_RenderingDevice_method_texture_create_shared_from_slice"></span>

[RID](class_rid.md#class_RID) **texture_create_shared_from_slice** ( view: [RDTextureView](class_rdtextureview.md#class_RDTextureView), with_texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int), mipmap: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int) = 1, slice_type: [TextureSliceType](class_renderingdevice.md#enum_RenderingDevice_TextureSliceType) = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_create_shared_from_slice)

Creates a shared texture using the specified `view` and the texture information from `with_texture`'s `layer` and `mipmap`. The number of included mipmaps from the original texture can be controlled using the `mipmaps` parameter. Only relevant for textures with multiple layers, such as 3D textures, texture arrays and cubemaps. For single-layer textures, use [texture_create_shared()](class_renderingdevice.md#class_RenderingDevice_method_texture_create_shared).

For 2D textures (which only have one layer), `layer` must be `0`.

 **Note:** Layer slicing is only supported for 2D texture arrays, not 3D textures or cubemaps.

This will be freed automatically when the `with_texture` is freed.

---

<span id="class_RenderingDevice_method_texture_get_data"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **texture_get_data** ( texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_get_data)

Returns the `texture` data for the specified `layer` as raw binary data. For 2D textures (which only have one layer), `layer` must be `0`.

 **Note:** `texture` can't be retrieved while a draw list that uses it as part of a framebuffer is being created. Ensure the draw list is finalized (and that the color/depth texture using it is not set to [FINAL_ACTION_CONTINUE](class_renderingdevice.md#class_RenderingDevice_constant_FINAL_ACTION_CONTINUE)) to retrieve this texture. Otherwise, an error is printed and an empty [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) is returned.

 **Note:** `texture` requires the [TEXTURE_USAGE_CAN_COPY_FROM_BIT](class_renderingdevice.md#class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_FROM_BIT) to be retrieved. Otherwise, an error is printed and an empty [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) is returned.

 **Note:** This method will block the GPU from working until the data is retrieved. Refer to [texture_get_data_async()](class_renderingdevice.md#class_RenderingDevice_method_texture_get_data_async) for an alternative that returns the data in more performant way.

---

<span id="class_RenderingDevice_method_texture_get_data_async"></span>

Error **texture_get_data_async** ( texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int), callback: [Callable](class_callable.md#class_Callable) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_get_data_async)

Asynchronous version of [texture_get_data()](class_renderingdevice.md#class_RenderingDevice_method_texture_get_data). RenderingDevice will call `callback` in a certain amount of frames with the data the texture had at the time of the request.

 **Note:** At the moment, the delay corresponds to the amount of frames specified by ProjectSettings.rendering/rendering_device/vsync/frame_queue_size.

 **Note:** Downloading large textures can have a prohibitive cost for real-time even when using the asynchronous method due to hardware bandwidth limitations. When dealing with large resources, you can adjust settings such as ProjectSettings.rendering/rendering_device/staging_buffer/texture_download_region_size_px and ProjectSettings.rendering/rendering_device/staging_buffer/block_size_kb to improve the transfer speed at the cost of extra memory.

::

    func _texture_get_data_callback(array):
        value = array.decode_u32(0)

    ...

    rd.texture_get_data_async(texture, 0, _texture_get_data_callback)

---

<span id="class_RenderingDevice_method_texture_get_format"></span>

[RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat) **texture_get_format** ( texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_get_format)

Returns the data format used to create this texture.

---

<span id="class_RenderingDevice_method_texture_get_native_handle"></span>

[int](class_int.md#class_int) **texture_get_native_handle** ( texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_get_native_handle)

**Deprecated:** Use [get_driver_resource()](class_renderingdevice.md#class_RenderingDevice_method_get_driver_resource) with [DRIVER_RESOURCE_TEXTURE](class_renderingdevice.md#class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE) instead.

Returns the internal graphics handle for this texture object. For use when communicating with third-party APIs mostly with GDExtension.

 **Note:** This function returns a `uint64_t` which internally maps to a `GLuint` (OpenGL) or `VkImage` (Vulkan).

---

<span id="class_RenderingDevice_method_texture_is_discardable"></span>

[bool](class_bool.md#class_bool) **texture_is_discardable** ( texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_is_discardable)

Returns `true` if the `texture` is discardable, `false` otherwise. See [RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat) or [texture_set_discardable()](class_renderingdevice.md#class_RenderingDevice_method_texture_set_discardable).

---

<span id="class_RenderingDevice_method_texture_is_format_supported_for_usage"></span>

[bool](class_bool.md#class_bool) **texture_is_format_supported_for_usage** ( format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), usage_flags: *BitField*\[[TextureUsageBits](class_renderingdevice.md#enum_RenderingDevice_TextureUsageBits)\] ) *const* [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_is_format_supported_for_usage)

Returns `true` if the specified `format` is supported for the given `usage_flags`, `false` otherwise.

---

<span id="class_RenderingDevice_method_texture_is_shared"></span>

[bool](class_bool.md#class_bool) **texture_is_shared** ( texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_is_shared)

Returns `true` if the `texture` is shared, `false` otherwise. See [RDTextureView](class_rdtextureview.md#class_RDTextureView).

---

<span id="class_RenderingDevice_method_texture_is_valid"></span>

[bool](class_bool.md#class_bool) **texture_is_valid** ( texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_is_valid)

Returns `true` if the `texture` is valid, `false` otherwise.

---

<span id="class_RenderingDevice_method_texture_resolve_multisample"></span>

Error **texture_resolve_multisample** ( from_texture: [RID](class_rid.md#class_RID), to_texture: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_resolve_multisample)

Resolves the `from_texture` texture onto `to_texture` with multisample antialiasing enabled. This must be used when rendering a framebuffer for MSAA to work. Returns @GlobalScope.OK if successful, @GlobalScope.ERR_INVALID_PARAMETER otherwise.

 **Note:** `from_texture` and `to_texture` textures must have the same dimension, format and type (color or depth).

 **Note:** `from_texture` can't be copied while a draw list that uses it as part of a framebuffer is being created. Ensure the draw list is finalized (and that the color/depth texture using it is not set to [FINAL_ACTION_CONTINUE](class_renderingdevice.md#class_RenderingDevice_constant_FINAL_ACTION_CONTINUE)) to resolve this texture.

 **Note:** `from_texture` requires the [TEXTURE_USAGE_CAN_COPY_FROM_BIT](class_renderingdevice.md#class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_FROM_BIT) to be retrieved.

 **Note:** `from_texture` must be multisampled and must also be 2D (or a slice of a 3D/cubemap texture).

 **Note:** `to_texture` can't be copied while a draw list that uses it as part of a framebuffer is being created. Ensure the draw list is finalized (and that the color/depth texture using it is not set to [FINAL_ACTION_CONTINUE](class_renderingdevice.md#class_RenderingDevice_constant_FINAL_ACTION_CONTINUE)) to resolve this texture.

 **Note:** `to_texture` texture requires the [TEXTURE_USAGE_CAN_COPY_TO_BIT](class_renderingdevice.md#class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_TO_BIT) to be retrieved.

 **Note:** `to_texture` texture must **not** be multisampled and must also be 2D (or a slice of a 3D/cubemap texture).

---

<span id="class_RenderingDevice_method_texture_set_discardable"></span>

void **texture_set_discardable** ( texture: [RID](class_rid.md#class_RID), discardable: [bool](class_bool.md#class_bool) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_set_discardable)

Updates the discardable property of `texture`.

If a texture is discardable, its contents do not need to be preserved between frames. This flag is only relevant when the texture is used as target in a draw list.

This information is used by **RenderingDevice** to figure out if a texture's contents can be discarded, eliminating unnecessary writes to memory and boosting performance.

---

<span id="class_RenderingDevice_method_texture_update"></span>

Error **texture_update** ( texture: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_texture_update)

Updates texture data with new data, replacing the previous data in place. The updated texture data must have the same dimensions and format. For 2D textures (which only have one layer), `layer` must be `0`. Returns @GlobalScope.OK if the update was successful, @GlobalScope.ERR_INVALID_PARAMETER otherwise.

 **Note:** Updating textures is forbidden during creation of a draw or compute list.

 **Note:** The existing `texture` can't be updated while a draw list that uses it as part of a framebuffer is being created. Ensure the draw list is finalized (and that the color/depth texture using it is not set to [FINAL_ACTION_CONTINUE](class_renderingdevice.md#class_RenderingDevice_constant_FINAL_ACTION_CONTINUE)) to update this texture.

 **Note:** The existing `texture` requires the [TEXTURE_USAGE_CAN_UPDATE_BIT](class_renderingdevice.md#class_RenderingDevice_constant_TEXTURE_USAGE_CAN_UPDATE_BIT) to be updatable.

---

<span id="class_RenderingDevice_method_tlas_create"></span>

[RID](class_rid.md#class_RID) **tlas_create** ( instances_buffer: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_tlas_create)

Creates a new Top Level Acceleration Structure. It can be accessed with the RID that is returned.

The instances buffer passed as input is expected to be filled before building the TLAS.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

---

<span id="class_RenderingDevice_method_tlas_instances_buffer_create"></span>

[RID](class_rid.md#class_RID) **tlas_instances_buffer_create** ( instance_count: [int](class_int.md#class_int), creation_bits: *BitField*\[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_tlas_instances_buffer_create)

Creates a new instances buffer which can be used to create a TLAS. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

---

<span id="class_RenderingDevice_method_tlas_instances_buffer_fill"></span>

void **tlas_instances_buffer_fill** ( instances_buffer: [RID](class_rid.md#class_RID), blases: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], transforms: [Array](class_array.md#class_Array)\[[Transform3D](class_transform3d.md#class_Transform3D)\] ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_tlas_instances_buffer_fill)

Fills the content of an instances buffer. The number of BLASes and transforms passed as input should be the same and should equal the instance count used at instance buffer creation time.

---

<span id="class_RenderingDevice_method_uniform_buffer_create"></span>

[RID](class_rid.md#class_RID) **uniform_buffer_create** ( size_bytes: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray(), creation_bits: *BitField*\[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_uniform_buffer_create)

Creates a new uniform buffer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

---

<span id="class_RenderingDevice_method_uniform_set_create"></span>

[RID](class_rid.md#class_RID) **uniform_set_create** ( uniforms: [Array](class_array.md#class_Array)\[[RDUniform](class_rduniform.md#class_RDUniform)\], shader: [RID](class_rid.md#class_RID), shader_set: [int](class_int.md#class_int) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_uniform_set_create)

Creates a new uniform set. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

This will be freed automatically when the `shader` or any of the RIDs in the `uniforms` is freed.

---

<span id="class_RenderingDevice_method_uniform_set_is_valid"></span>

[bool](class_bool.md#class_bool) **uniform_set_is_valid** ( uniform_set: [RID](class_rid.md#class_RID) ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_uniform_set_is_valid)

Checks if the `uniform_set` is valid, i.e. is owned.

---

<span id="class_RenderingDevice_method_vertex_array_create"></span>

[RID](class_rid.md#class_RID) **vertex_array_create** ( vertex_count: [int](class_int.md#class_int), vertex_format: [int](class_int.md#class_int), src_buffers: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\], offsets: [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) = PackedInt64Array() ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_vertex_array_create)

Creates a vertex array based on the specified buffers. Optionally, `offsets` (in bytes) may be defined for each buffer.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

This will be freed automatically when any of the `src_buffers` is freed.

---

<span id="class_RenderingDevice_method_vertex_buffer_create"></span>

[RID](class_rid.md#class_RID) **vertex_buffer_create** ( size_bytes: [int](class_int.md#class_int), data: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) = PackedByteArray(), creation_bits: *BitField*\[[BufferCreationBits](class_renderingdevice.md#enum_RenderingDevice_BufferCreationBits)\] = 0 ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_vertex_buffer_create)

Creates a new vertex buffer. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the RenderingDevice's [free_rid()](class_renderingdevice.md#class_RenderingDevice_method_free_rid) method.

---

<span id="class_RenderingDevice_method_vertex_format_create"></span>

[int](class_int.md#class_int) **vertex_format_create** ( vertex_descriptions: [Array](class_array.md#class_Array)\[[RDVertexAttribute](class_rdvertexattribute.md#class_RDVertexAttribute)\] ) [🔗](class_renderingdevice.md#class_RenderingDevice_method_vertex_format_create)

Creates a new vertex format with the specified `vertex_descriptions`. Returns a unique vertex format ID corresponding to the newly created vertex format.
