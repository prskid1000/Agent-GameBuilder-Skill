<span id="class_RenderSceneBuffersRD"></span>

## RenderSceneBuffersRD

**Inherits:** [RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Render scene buffer implementation for the RenderingDevice based renderers.

### Description

This object manages all 3D rendering buffers for the rendering device based renderers. An instance of this object is created for every viewport that has 3D rendering enabled. See also [RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers).

All buffers are organized in **contexts**. The default context is called **render_buffers** and can contain amongst others the color buffer, depth buffer, velocity buffers, VRS density map and MSAA variants of these buffers.

Buffers are only guaranteed to exist during rendering of the viewport.

 **Note:** This is an internal rendering server object. Do not instantiate this class from a script.

### Methods


| void | [clear_context](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_clear_context) ( context: [StringName](class_stringname.md#class_StringName) ) |
| --- | --- |
| [RID](class_rid.md#class_RID) | [create_texture](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_create_texture) ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), data_format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), usage_bits: [int](class_int.md#class_int), texture_samples: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples), size: [Vector2i](class_vector2i.md#class_Vector2i), layers: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int), unique: [bool](class_bool.md#class_bool), discardable: [bool](class_bool.md#class_bool) ) |
| [RID](class_rid.md#class_RID) | [create_texture_from_format](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_create_texture_from_format) ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), format: [RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat), view: [RDTextureView](class_rdtextureview.md#class_RDTextureView), unique: [bool](class_bool.md#class_bool) ) |
| [RID](class_rid.md#class_RID) | [create_texture_view](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_create_texture_view) ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), view_name: [StringName](class_stringname.md#class_StringName), view: [RDTextureView](class_rdtextureview.md#class_RDTextureView) ) |
| [RID](class_rid.md#class_RID) | [get_color_layer](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_color_layer) ( layer: [int](class_int.md#class_int), msaa: [bool](class_bool.md#class_bool) = false ) |
| [RID](class_rid.md#class_RID) | [get_color_texture](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_color_texture) ( msaa: [bool](class_bool.md#class_bool) = false ) |
| [RID](class_rid.md#class_RID) | [get_depth_layer](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_depth_layer) ( layer: [int](class_int.md#class_int), msaa: [bool](class_bool.md#class_bool) = false ) |
| [RID](class_rid.md#class_RID) | [get_depth_texture](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_depth_texture) ( msaa: [bool](class_bool.md#class_bool) = false ) |
| [float](class_float.md#class_float) | [get_fsr_sharpness](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_fsr_sharpness) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_internal_size](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_internal_size) ( ) const |
| [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) | [get_msaa_3d](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_msaa_3d) ( ) const |
| [RID](class_rid.md#class_RID) | [get_render_target](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_render_target) ( ) const |
| [ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) | [get_scaling_3d_mode](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_scaling_3d_mode) ( ) const |
| [ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) | [get_screen_space_aa](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_screen_space_aa) ( ) const |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_target_size](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_target_size) ( ) const |
| [RID](class_rid.md#class_RID) | [get_texture](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture) ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) const |
| [RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat) | [get_texture_format](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_format) ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) const |
| [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) | [get_texture_samples](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_samples) ( ) const |
| [RID](class_rid.md#class_RID) | [get_texture_slice](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_slice) ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), layer: [int](class_int.md#class_int), mipmap: [int](class_int.md#class_int), layers: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int) ) |
| [Vector2i](class_vector2i.md#class_Vector2i) | [get_texture_slice_size](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_slice_size) ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), mipmap: [int](class_int.md#class_int) ) |
| [RID](class_rid.md#class_RID) | [get_texture_slice_view](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_slice_view) ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), layer: [int](class_int.md#class_int), mipmap: [int](class_int.md#class_int), layers: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int), view: [RDTextureView](class_rdtextureview.md#class_RDTextureView) ) |
| [bool](class_bool.md#class_bool) | [get_use_debanding](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_use_debanding) ( ) const |
| [bool](class_bool.md#class_bool) | [get_use_taa](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_use_taa) ( ) const |
| [RID](class_rid.md#class_RID) | [get_velocity_layer](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_velocity_layer) ( layer: [int](class_int.md#class_int), msaa: [bool](class_bool.md#class_bool) = false ) |
| [RID](class_rid.md#class_RID) | [get_velocity_texture](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_velocity_texture) ( msaa: [bool](class_bool.md#class_bool) = false ) |
| [int](class_int.md#class_int) | [get_view_count](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_view_count) ( ) const |
| [bool](class_bool.md#class_bool) | [has_texture](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_has_texture) ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) const |

---

### Method Descriptions

<span id="class_RenderSceneBuffersRD_method_clear_context"></span>

void **clear_context** ( context: [StringName](class_stringname.md#class_StringName) ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_clear_context)

Frees all buffers related to this context.

---

<span id="class_RenderSceneBuffersRD_method_create_texture"></span>

[RID](class_rid.md#class_RID) **create_texture** ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), data_format: [DataFormat](class_renderingdevice.md#enum_RenderingDevice_DataFormat), usage_bits: [int](class_int.md#class_int), texture_samples: [TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples), size: [Vector2i](class_vector2i.md#class_Vector2i), layers: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int), unique: [bool](class_bool.md#class_bool), discardable: [bool](class_bool.md#class_bool) ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_create_texture)

Create a new texture with the given definition and cache this under the given name. Will return the existing texture if it already exists.

---

<span id="class_RenderSceneBuffersRD_method_create_texture_from_format"></span>

[RID](class_rid.md#class_RID) **create_texture_from_format** ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), format: [RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat), view: [RDTextureView](class_rdtextureview.md#class_RDTextureView), unique: [bool](class_bool.md#class_bool) ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_create_texture_from_format)

Create a new texture using the given format and view and cache this under the given name. Will return the existing texture if it already exists.

---

<span id="class_RenderSceneBuffersRD_method_create_texture_view"></span>

[RID](class_rid.md#class_RID) **create_texture_view** ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), view_name: [StringName](class_stringname.md#class_StringName), view: [RDTextureView](class_rdtextureview.md#class_RDTextureView) ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_create_texture_view)

Create a new texture view for an existing texture and cache this under the given `view_name`. Will return the existing texture view if it already exists. Will error if the source texture doesn't exist.

---

<span id="class_RenderSceneBuffersRD_method_get_color_layer"></span>

[RID](class_rid.md#class_RID) **get_color_layer** ( layer: [int](class_int.md#class_int), msaa: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_color_layer)

Returns the specified layer from the color texture we are rendering 3D content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

---

<span id="class_RenderSceneBuffersRD_method_get_color_texture"></span>

[RID](class_rid.md#class_RID) **get_color_texture** ( msaa: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_color_texture)

Returns the color texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

---

<span id="class_RenderSceneBuffersRD_method_get_depth_layer"></span>

[RID](class_rid.md#class_RID) **get_depth_layer** ( layer: [int](class_int.md#class_int), msaa: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_depth_layer)

Returns the specified layer from the depth texture we are rendering 3D content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

---

<span id="class_RenderSceneBuffersRD_method_get_depth_texture"></span>

[RID](class_rid.md#class_RID) **get_depth_texture** ( msaa: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_depth_texture)

Returns the depth texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

---

<span id="class_RenderSceneBuffersRD_method_get_fsr_sharpness"></span>

[float](class_float.md#class_float) **get_fsr_sharpness** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_fsr_sharpness)

Returns the FSR sharpness value used while rendering the 3D content (if [get_scaling_3d_mode()](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_scaling_3d_mode) is an FSR mode).

---

<span id="class_RenderSceneBuffersRD_method_get_internal_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_internal_size** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_internal_size)

Returns the internal size of the render buffer (size before upscaling) with which textures are created by default.

---

<span id="class_RenderSceneBuffersRD_method_get_msaa_3d"></span>

[ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) **get_msaa_3d** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_msaa_3d)

Returns the applied 3D MSAA mode for this viewport.

---

<span id="class_RenderSceneBuffersRD_method_get_render_target"></span>

[RID](class_rid.md#class_RID) **get_render_target** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_render_target)

Returns the render target associated with this buffers object.

---

<span id="class_RenderSceneBuffersRD_method_get_scaling_3d_mode"></span>

[ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) **get_scaling_3d_mode** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_scaling_3d_mode)

Returns the scaling mode used for upscaling.

---

<span id="class_RenderSceneBuffersRD_method_get_screen_space_aa"></span>

[ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) **get_screen_space_aa** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_screen_space_aa)

Returns the screen-space antialiasing method applied.

---

<span id="class_RenderSceneBuffersRD_method_get_target_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_target_size** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_target_size)

Returns the target size of the render buffer (size after upscaling).

---

<span id="class_RenderSceneBuffersRD_method_get_texture"></span>

[RID](class_rid.md#class_RID) **get_texture** ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture)

Returns a cached texture with this name.

---

<span id="class_RenderSceneBuffersRD_method_get_texture_format"></span>

[RDTextureFormat](class_rdtextureformat.md#class_RDTextureFormat) **get_texture_format** ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_format)

Returns the texture format information with which a cached texture was created.

---

<span id="class_RenderSceneBuffersRD_method_get_texture_samples"></span>

[TextureSamples](class_renderingdevice.md#enum_RenderingDevice_TextureSamples) **get_texture_samples** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_samples)

Returns the number of MSAA samples used.

---

<span id="class_RenderSceneBuffersRD_method_get_texture_slice"></span>

[RID](class_rid.md#class_RID) **get_texture_slice** ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), layer: [int](class_int.md#class_int), mipmap: [int](class_int.md#class_int), layers: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int) ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_slice)

Returns a specific slice (layer or mipmap) for a cached texture.

---

<span id="class_RenderSceneBuffersRD_method_get_texture_slice_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **get_texture_slice_size** ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), mipmap: [int](class_int.md#class_int) ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_slice_size)

Returns the texture size of a given slice of a cached texture.

---

<span id="class_RenderSceneBuffersRD_method_get_texture_slice_view"></span>

[RID](class_rid.md#class_RID) **get_texture_slice_view** ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName), layer: [int](class_int.md#class_int), mipmap: [int](class_int.md#class_int), layers: [int](class_int.md#class_int), mipmaps: [int](class_int.md#class_int), view: [RDTextureView](class_rdtextureview.md#class_RDTextureView) ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_texture_slice_view)

Returns a specific view of a slice (layer or mipmap) for a cached texture.

---

<span id="class_RenderSceneBuffersRD_method_get_use_debanding"></span>

[bool](class_bool.md#class_bool) **get_use_debanding** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_use_debanding)

Returns `true` if debanding is enabled.

---

<span id="class_RenderSceneBuffersRD_method_get_use_taa"></span>

[bool](class_bool.md#class_bool) **get_use_taa** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_use_taa)

Returns `true` if TAA is enabled.

---

<span id="class_RenderSceneBuffersRD_method_get_velocity_layer"></span>

[RID](class_rid.md#class_RID) **get_velocity_layer** ( layer: [int](class_int.md#class_int), msaa: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_velocity_layer)

Returns the specified layer from the velocity texture we are rendering 3D content to.

---

<span id="class_RenderSceneBuffersRD_method_get_velocity_texture"></span>

[RID](class_rid.md#class_RID) **get_velocity_texture** ( msaa: [bool](class_bool.md#class_bool) = false ) [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_velocity_texture)

Returns the velocity texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is **true** and MSAA is enabled, this returns the MSAA variant of the buffer.

---

<span id="class_RenderSceneBuffersRD_method_get_view_count"></span>

[int](class_int.md#class_int) **get_view_count** ( ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_get_view_count)

Returns the view count for the associated viewport.

---

<span id="class_RenderSceneBuffersRD_method_has_texture"></span>

[bool](class_bool.md#class_bool) **has_texture** ( context: [StringName](class_stringname.md#class_StringName), name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_renderscenebuffersrd.md#class_RenderSceneBuffersRD_method_has_texture)

Returns `true` if a cached texture exists for this name.
