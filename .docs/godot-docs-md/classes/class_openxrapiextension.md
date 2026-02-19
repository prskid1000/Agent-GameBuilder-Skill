<span id="class_OpenXRAPIExtension"></span>

## OpenXRAPIExtension

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Makes the OpenXR API available for GDExtension.

### Description

**OpenXRAPIExtension** makes OpenXR available for GDExtension. It provides the OpenXR API to GDExtension through the [get_instance_proc_addr()](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_instance_proc_addr) method, and the OpenXR instance through [get_instance()](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_instance).

It also provides methods for querying the status of OpenXR initialization, and helper methods for ease of use of the API with GDExtension.

### Tutorials

- XrResult documentation

- XrInstance documentation

- XrSpace documentation

- XrSession documentation

- XrSystemId documentation

- xrBeginSession documentation

- XrPosef documentation

### Methods


| [int](class_int.md#class_int) | [action_get_handle](class_openxrapiextension.md#class_OpenXRAPIExtension_method_action_get_handle) ( action: [RID](class_rid.md#class_RID) ) |
| --- | --- |
| void | [begin_debug_label_region](class_openxrapiextension.md#class_OpenXRAPIExtension_method_begin_debug_label_region) ( label_name: [String](class_string.md#class_String) ) |
| [bool](class_bool.md#class_bool) | [can_render](class_openxrapiextension.md#class_OpenXRAPIExtension_method_can_render) ( ) |
| void | [end_debug_label_region](class_openxrapiextension.md#class_OpenXRAPIExtension_method_end_debug_label_region) ( ) |
| [RID](class_rid.md#class_RID) | [find_action](class_openxrapiextension.md#class_OpenXRAPIExtension_method_find_action) ( name: [String](class_string.md#class_String), action_set: [RID](class_rid.md#class_RID) ) |
| [String](class_string.md#class_String) | [get_error_string](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_error_string) ( result: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_hand_tracker](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_hand_tracker) ( hand_index: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_instance](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_instance) ( ) |
| [int](class_int.md#class_int) | [get_instance_proc_addr](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_instance_proc_addr) ( name: [String](class_string.md#class_String) ) |
| [int](class_int.md#class_int) | [get_next_frame_time](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_next_frame_time) ( ) |
| [int](class_int.md#class_int) | [get_openxr_version](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_openxr_version) ( ) |
| [int](class_int.md#class_int) | [get_play_space](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_play_space) ( ) |
| [int](class_int.md#class_int) | [get_predicted_display_time](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_predicted_display_time) ( ) |
| [int](class_int.md#class_int) | [get_projection_layer](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_projection_layer) ( ) |
| [float](class_float.md#class_float) | [get_render_state_z_far](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_render_state_z_far) ( ) |
| [float](class_float.md#class_float) | [get_render_state_z_near](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_render_state_z_near) ( ) |
| [int](class_int.md#class_int) | [get_session](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_session) ( ) |
| [PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) | [get_supported_swapchain_formats](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_supported_swapchain_formats) ( ) |
| [String](class_string.md#class_String) | [get_swapchain_format_name](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_swapchain_format_name) ( swapchain_format: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_system_id](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_system_id) ( ) |
| void | [insert_debug_label](class_openxrapiextension.md#class_OpenXRAPIExtension_method_insert_debug_label) ( label_name: [String](class_string.md#class_String) ) |
| [OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport) | [is_environment_blend_mode_alpha_supported](class_openxrapiextension.md#class_OpenXRAPIExtension_method_is_environment_blend_mode_alpha_supported) ( ) |
| [bool](class_bool.md#class_bool) | [is_initialized](class_openxrapiextension.md#class_OpenXRAPIExtension_method_is_initialized) ( ) |
| [bool](class_bool.md#class_bool) | [is_running](class_openxrapiextension.md#class_OpenXRAPIExtension_method_is_running) ( ) |
| [bool](class_bool.md#class_bool) | [openxr_is_enabled](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_is_enabled) ( check_run_in_editor: [bool](class_bool.md#class_bool) ) static |
| void | [openxr_swapchain_acquire](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_acquire) ( swapchain: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [openxr_swapchain_create](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_create) ( create_flags: [int](class_int.md#class_int), usage_flags: [int](class_int.md#class_int), swapchain_format: [int](class_int.md#class_int), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), sample_count: [int](class_int.md#class_int), array_size: [int](class_int.md#class_int) ) |
| void | [openxr_swapchain_free](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_free) ( swapchain: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [openxr_swapchain_get_image](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_get_image) ( swapchain: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [openxr_swapchain_get_swapchain](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_get_swapchain) ( swapchain: [int](class_int.md#class_int) ) |
| void | [openxr_swapchain_release](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_release) ( swapchain: [int](class_int.md#class_int) ) |
| void | [register_composition_layer_provider](class_openxrapiextension.md#class_OpenXRAPIExtension_method_register_composition_layer_provider) ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) |
| void | [register_frame_info_extension](class_openxrapiextension.md#class_OpenXRAPIExtension_method_register_frame_info_extension) ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) |
| void | [register_projection_views_extension](class_openxrapiextension.md#class_OpenXRAPIExtension_method_register_projection_views_extension) ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) |
| void | [set_custom_play_space](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_custom_play_space) ( space: `const void*` ) |
| void | [set_emulate_environment_blend_mode_alpha_blend](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_emulate_environment_blend_mode_alpha_blend) ( enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_object_name](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_object_name) ( object_type: [int](class_int.md#class_int), object_handle: [int](class_int.md#class_int), object_name: [String](class_string.md#class_String) ) |
| void | [set_render_region](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_render_region) ( render_region: [Rect2i](class_rect2i.md#class_Rect2i) ) |
| void | [set_velocity_depth_texture](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_velocity_depth_texture) ( render_target: [RID](class_rid.md#class_RID) ) |
| void | [set_velocity_target_size](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_velocity_target_size) ( target_size: [Vector2i](class_vector2i.md#class_Vector2i) ) |
| void | [set_velocity_texture](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_velocity_texture) ( render_target: [RID](class_rid.md#class_RID) ) |
| [Transform3D](class_transform3d.md#class_Transform3D) | [transform_from_pose](class_openxrapiextension.md#class_OpenXRAPIExtension_method_transform_from_pose) ( pose: `const void*` ) |
| void | [unregister_composition_layer_provider](class_openxrapiextension.md#class_OpenXRAPIExtension_method_unregister_composition_layer_provider) ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) |
| void | [unregister_frame_info_extension](class_openxrapiextension.md#class_OpenXRAPIExtension_method_unregister_frame_info_extension) ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) |
| void | [unregister_projection_views_extension](class_openxrapiextension.md#class_OpenXRAPIExtension_method_unregister_projection_views_extension) ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) |
| void | [update_main_swapchain_size](class_openxrapiextension.md#class_OpenXRAPIExtension_method_update_main_swapchain_size) ( ) |
| [bool](class_bool.md#class_bool) | [xr_result](class_openxrapiextension.md#class_OpenXRAPIExtension_method_xr_result) ( result: [int](class_int.md#class_int), format: [String](class_string.md#class_String), args: [Array](class_array.md#class_Array) ) |

---

### Enumerations

<span id="enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport"></span>

enum **OpenXRAlphaBlendModeSupport**: [🔗](class_openxrapiextension.md#enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport)

<span id="class_OpenXRAPIExtension_constant_OPENXR_ALPHA_BLEND_MODE_SUPPORT_NONE"></span>

[OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport) **OPENXR_ALPHA_BLEND_MODE_SUPPORT_NONE** = `0`

Means that [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND) isn't supported at all.

<span id="class_OpenXRAPIExtension_constant_OPENXR_ALPHA_BLEND_MODE_SUPPORT_REAL"></span>

[OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport) **OPENXR_ALPHA_BLEND_MODE_SUPPORT_REAL** = `1`

Means that [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND) is really supported.

<span id="class_OpenXRAPIExtension_constant_OPENXR_ALPHA_BLEND_MODE_SUPPORT_EMULATING"></span>

[OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport) **OPENXR_ALPHA_BLEND_MODE_SUPPORT_EMULATING** = `2`

Means that [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND) is emulated.

---

### Method Descriptions

<span id="class_OpenXRAPIExtension_method_action_get_handle"></span>

[int](class_int.md#class_int) **action_get_handle** ( action: [RID](class_rid.md#class_RID) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_action_get_handle)

Returns the corresponding `XrAction` OpenXR handle for the given action RID.

---

<span id="class_OpenXRAPIExtension_method_begin_debug_label_region"></span>

void **begin_debug_label_region** ( label_name: [String](class_string.md#class_String) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_begin_debug_label_region)

Begins a new debug label region, this label will be reported in debug messages for any calls following this until [end_debug_label_region()](class_openxrapiextension.md#class_OpenXRAPIExtension_method_end_debug_label_region) is called. Debug labels can be stacked.

---

<span id="class_OpenXRAPIExtension_method_can_render"></span>

[bool](class_bool.md#class_bool) **can_render** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_can_render)

Returns `true` if OpenXR is initialized for rendering with an XR viewport.

---

<span id="class_OpenXRAPIExtension_method_end_debug_label_region"></span>

void **end_debug_label_region** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_end_debug_label_region)

Marks the end of a debug label region. Removes the latest debug label region added by calling [begin_debug_label_region()](class_openxrapiextension.md#class_OpenXRAPIExtension_method_begin_debug_label_region).

---

<span id="class_OpenXRAPIExtension_method_find_action"></span>

[RID](class_rid.md#class_RID) **find_action** ( name: [String](class_string.md#class_String), action_set: [RID](class_rid.md#class_RID) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_find_action)

Returns the [RID](class_rid.md#class_RID) corresponding to an `Action` of a matching name, optionally limited to a specified action set.

---

<span id="class_OpenXRAPIExtension_method_get_error_string"></span>

[String](class_string.md#class_String) **get_error_string** ( result: [int](class_int.md#class_int) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_error_string)

Returns an error string for the given XrResult.

---

<span id="class_OpenXRAPIExtension_method_get_hand_tracker"></span>

[int](class_int.md#class_int) **get_hand_tracker** ( hand_index: [int](class_int.md#class_int) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_hand_tracker)

Returns the corresponding `XRHandTrackerEXT` handle for the given hand index value.

---

<span id="class_OpenXRAPIExtension_method_get_instance"></span>

[int](class_int.md#class_int) **get_instance** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_instance)

Returns the XrInstance created during the initialization of the OpenXR API.

---

<span id="class_OpenXRAPIExtension_method_get_instance_proc_addr"></span>

[int](class_int.md#class_int) **get_instance_proc_addr** ( name: [String](class_string.md#class_String) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_instance_proc_addr)

Returns the function pointer of the OpenXR function with the specified name, cast to an integer. If the function with the given name does not exist, the method returns `0`.

 **Note:** `openxr/util.h` contains utility macros for acquiring OpenXR functions, e.g. `GDEXTENSION_INIT_XR_FUNC_V(xrCreateAction)`.

---

<span id="class_OpenXRAPIExtension_method_get_next_frame_time"></span>

[int](class_int.md#class_int) **get_next_frame_time** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_next_frame_time)

Returns the predicted display timing for the next frame.

---

<span id="class_OpenXRAPIExtension_method_get_openxr_version"></span>

[int](class_int.md#class_int) **get_openxr_version** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_openxr_version)

Returns the version of OpenXR that was initialized. Only valid after the OpenXR instance has been created. See XR_MAKE_VERSION for how the version is calculated.

---

<span id="class_OpenXRAPIExtension_method_get_play_space"></span>

[int](class_int.md#class_int) **get_play_space** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_play_space)

Returns the play space, which is an XrSpace cast to an integer.

---

<span id="class_OpenXRAPIExtension_method_get_predicted_display_time"></span>

[int](class_int.md#class_int) **get_predicted_display_time** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_predicted_display_time)

Returns the predicted display timing for the current frame.

---

<span id="class_OpenXRAPIExtension_method_get_projection_layer"></span>

[int](class_int.md#class_int) **get_projection_layer** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_projection_layer)

Returns a pointer to the render state's `XrCompositionLayerProjection` struct.

 **Note:** This method should only be called from the rendering thread.

---

<span id="class_OpenXRAPIExtension_method_get_render_state_z_far"></span>

[float](class_float.md#class_float) **get_render_state_z_far** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_render_state_z_far)

Returns the far boundary value of the camera frustum.

 **Note:** This is only accessible in the render thread.

---

<span id="class_OpenXRAPIExtension_method_get_render_state_z_near"></span>

[float](class_float.md#class_float) **get_render_state_z_near** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_render_state_z_near)

Returns the near boundary value of the camera frustum.

 **Note:** This is only accessible in the render thread.

---

<span id="class_OpenXRAPIExtension_method_get_session"></span>

[int](class_int.md#class_int) **get_session** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_session)

Returns the OpenXR session, which is an XrSession cast to an integer.

---

<span id="class_OpenXRAPIExtension_method_get_supported_swapchain_formats"></span>

[PackedInt64Array](class_packedint64array.md#class_PackedInt64Array) **get_supported_swapchain_formats** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_supported_swapchain_formats)

Returns an array of supported swapchain formats.

---

<span id="class_OpenXRAPIExtension_method_get_swapchain_format_name"></span>

[String](class_string.md#class_String) **get_swapchain_format_name** ( swapchain_format: [int](class_int.md#class_int) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_swapchain_format_name)

Returns the name of the specified swapchain format.

---

<span id="class_OpenXRAPIExtension_method_get_system_id"></span>

[int](class_int.md#class_int) **get_system_id** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_get_system_id)

Returns the ID of the system, which is an XrSystemId cast to an integer.

---

<span id="class_OpenXRAPIExtension_method_insert_debug_label"></span>

void **insert_debug_label** ( label_name: [String](class_string.md#class_String) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_insert_debug_label)

Inserts a debug label, this label is reported in any debug message resulting from the OpenXR calls that follows, until any of [begin_debug_label_region()](class_openxrapiextension.md#class_OpenXRAPIExtension_method_begin_debug_label_region), [end_debug_label_region()](class_openxrapiextension.md#class_OpenXRAPIExtension_method_end_debug_label_region), or [insert_debug_label()](class_openxrapiextension.md#class_OpenXRAPIExtension_method_insert_debug_label) is called.

---

<span id="class_OpenXRAPIExtension_method_is_environment_blend_mode_alpha_supported"></span>

[OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport) **is_environment_blend_mode_alpha_supported** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_is_environment_blend_mode_alpha_supported)

Returns [OpenXRAlphaBlendModeSupport](class_openxrapiextension.md#enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport) denoting if [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND) is really supported, emulated or not supported at all.

---

<span id="class_OpenXRAPIExtension_method_is_initialized"></span>

[bool](class_bool.md#class_bool) **is_initialized** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_is_initialized)

Returns `true` if OpenXR is initialized.

---

<span id="class_OpenXRAPIExtension_method_is_running"></span>

[bool](class_bool.md#class_bool) **is_running** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_is_running)

Returns `true` if OpenXR is running (xrBeginSession was successfully called and the swapchains were created).

---

<span id="class_OpenXRAPIExtension_method_openxr_is_enabled"></span>

[bool](class_bool.md#class_bool) **openxr_is_enabled** ( check_run_in_editor: [bool](class_bool.md#class_bool) ) *static* [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_is_enabled)

Returns `true` if OpenXR is enabled.

---

<span id="class_OpenXRAPIExtension_method_openxr_swapchain_acquire"></span>

void **openxr_swapchain_acquire** ( swapchain: [int](class_int.md#class_int) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_acquire)

Acquires the image of the provided swapchain.

---

<span id="class_OpenXRAPIExtension_method_openxr_swapchain_create"></span>

[int](class_int.md#class_int) **openxr_swapchain_create** ( create_flags: [int](class_int.md#class_int), usage_flags: [int](class_int.md#class_int), swapchain_format: [int](class_int.md#class_int), width: [int](class_int.md#class_int), height: [int](class_int.md#class_int), sample_count: [int](class_int.md#class_int), array_size: [int](class_int.md#class_int) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_create)

Returns a pointer to a new swapchain created using the provided parameters.

---

<span id="class_OpenXRAPIExtension_method_openxr_swapchain_free"></span>

void **openxr_swapchain_free** ( swapchain: [int](class_int.md#class_int) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_free)

Destroys the provided swapchain and frees it from memory.

---

<span id="class_OpenXRAPIExtension_method_openxr_swapchain_get_image"></span>

[RID](class_rid.md#class_RID) **openxr_swapchain_get_image** ( swapchain: [int](class_int.md#class_int) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_get_image)

Returns the RID of the provided swapchain's image.

---

<span id="class_OpenXRAPIExtension_method_openxr_swapchain_get_swapchain"></span>

[int](class_int.md#class_int) **openxr_swapchain_get_swapchain** ( swapchain: [int](class_int.md#class_int) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_get_swapchain)

Returns the `XrSwapchain` handle of the provided swapchain.

---

<span id="class_OpenXRAPIExtension_method_openxr_swapchain_release"></span>

void **openxr_swapchain_release** ( swapchain: [int](class_int.md#class_int) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_openxr_swapchain_release)

Releases the image of the provided swapchain.

---

<span id="class_OpenXRAPIExtension_method_register_composition_layer_provider"></span>

void **register_composition_layer_provider** ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_register_composition_layer_provider)

Registers the given extension as a composition layer provider.

 **Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper_private_method__on_session_created).

---

<span id="class_OpenXRAPIExtension_method_register_frame_info_extension"></span>

void **register_frame_info_extension** ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_register_frame_info_extension)

Registers the given extension as modifying frame info via the [OpenXRExtensionWrapper._set_frame_wait_info_and_get_next_pointer()](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper_private_method__set_frame_wait_info_and_get_next_pointer), [OpenXRExtensionWrapper._set_view_locate_info_and_get_next_pointer()](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper_private_method__set_view_locate_info_and_get_next_pointer), or [OpenXRExtensionWrapper._set_frame_end_info_and_get_next_pointer()](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper_private_method__set_frame_end_info_and_get_next_pointer) virtual methods.

 **Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper_private_method__on_session_created).

---

<span id="class_OpenXRAPIExtension_method_register_projection_views_extension"></span>

void **register_projection_views_extension** ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_register_projection_views_extension)

Registers the given extension as a provider of additional data structures to projections views.

 **Note:** This cannot be called after the OpenXR session has started. However, it can be called in [OpenXRExtensionWrapper._on_session_created()](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper_private_method__on_session_created).

---

<span id="class_OpenXRAPIExtension_method_set_custom_play_space"></span>

void **set_custom_play_space** ( space: `const void*` ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_custom_play_space)

Sets the reference space used by OpenXR to the given XrSpace (cast to a `void *`).

---

<span id="class_OpenXRAPIExtension_method_set_emulate_environment_blend_mode_alpha_blend"></span>

void **set_emulate_environment_blend_mode_alpha_blend** ( enabled: [bool](class_bool.md#class_bool) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_emulate_environment_blend_mode_alpha_blend)

If set to `true`, an OpenXR extension is loaded which is capable of emulating the [XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND](class_xrinterface.md#class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND) blend mode.

---

<span id="class_OpenXRAPIExtension_method_set_object_name"></span>

void **set_object_name** ( object_type: [int](class_int.md#class_int), object_handle: [int](class_int.md#class_int), object_name: [String](class_string.md#class_String) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_object_name)

Set the object name of an OpenXR object, used for debug output. `object_type` must be a valid OpenXR `XrObjectType` enum and `object_handle` must be a valid OpenXR object handle.

---

<span id="class_OpenXRAPIExtension_method_set_render_region"></span>

void **set_render_region** ( render_region: [Rect2i](class_rect2i.md#class_Rect2i) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_render_region)

Sets the render region to `render_region`, overriding the normal render target's rect.

---

<span id="class_OpenXRAPIExtension_method_set_velocity_depth_texture"></span>

void **set_velocity_depth_texture** ( render_target: [RID](class_rid.md#class_RID) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_velocity_depth_texture)

Sets the render target of the velocity depth texture.

---

<span id="class_OpenXRAPIExtension_method_set_velocity_target_size"></span>

void **set_velocity_target_size** ( target_size: [Vector2i](class_vector2i.md#class_Vector2i) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_velocity_target_size)

Sets the target size of the velocity and velocity depth textures.

---

<span id="class_OpenXRAPIExtension_method_set_velocity_texture"></span>

void **set_velocity_texture** ( render_target: [RID](class_rid.md#class_RID) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_set_velocity_texture)

Sets the render target of the velocity texture.

---

<span id="class_OpenXRAPIExtension_method_transform_from_pose"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **transform_from_pose** ( pose: `const void*` ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_transform_from_pose)

Creates a [Transform3D](class_transform3d.md#class_Transform3D) from an XrPosef.

---

<span id="class_OpenXRAPIExtension_method_unregister_composition_layer_provider"></span>

void **unregister_composition_layer_provider** ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_unregister_composition_layer_provider)

Unregisters the given extension as a composition layer provider.

 **Note:** This cannot be called while the OpenXR session is still running.

---

<span id="class_OpenXRAPIExtension_method_unregister_frame_info_extension"></span>

void **unregister_frame_info_extension** ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_unregister_frame_info_extension)

Unregisters the given extension as modifying frame info.

 **Note:** This cannot be called while the OpenXR session is still running.

---

<span id="class_OpenXRAPIExtension_method_unregister_projection_views_extension"></span>

void **unregister_projection_views_extension** ( extension: [OpenXRExtensionWrapper](class_openxrextensionwrapper.md#class_OpenXRExtensionWrapper) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_unregister_projection_views_extension)

Unregisters the given extension as a provider of additional data structures to projections views.

 **Note:** This cannot be called while the OpenXR session is still running.

---

<span id="class_OpenXRAPIExtension_method_update_main_swapchain_size"></span>

void **update_main_swapchain_size** ( ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_update_main_swapchain_size)

Request the recommended resolution from the OpenXR runtime and update the main swapchain size if it has changed.

---

<span id="class_OpenXRAPIExtension_method_xr_result"></span>

[bool](class_bool.md#class_bool) **xr_result** ( result: [int](class_int.md#class_int), format: [String](class_string.md#class_String), args: [Array](class_array.md#class_Array) ) [🔗](class_openxrapiextension.md#class_OpenXRAPIExtension_method_xr_result)

Returns `true` if the provided XrResult (cast to an integer) is successful. Otherwise returns `false` and prints the XrResult converted to a string, with the specified additional information.
