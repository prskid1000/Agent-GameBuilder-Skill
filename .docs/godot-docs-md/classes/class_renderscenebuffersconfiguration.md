<span id="class_RenderSceneBuffersConfiguration"></span>

## RenderSceneBuffersConfiguration

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Configuration object used to setup a [RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) object.

### Description

This configuration object is created and populated by the render engine on a viewport change and used to (re)configure a [RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) object.

### Properties


| [ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) | [anisotropic_filtering_level](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_anisotropic_filtering_level) | `2` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [fsr_sharpness](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_fsr_sharpness) | `0.0` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [internal_size](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_internal_size) | `Vector2i(0, 0)` |
| [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) | [msaa_3d](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_msaa_3d) | `0` |
| [RID](class_rid.md#class_RID) | [render_target](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_render_target) | `RID()` |
| [ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) | [scaling_3d_mode](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_scaling_3d_mode) | `255` |
| [ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) | [screen_space_aa](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_screen_space_aa) | `0` |
| [Vector2i](class_vector2i.md#class_Vector2i) | [target_size](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_target_size) | `Vector2i(0, 0)` |
| [float](class_float.md#class_float) | [texture_mipmap_bias](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_texture_mipmap_bias) | `0.0` |
| [int](class_int.md#class_int) | [view_count](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_view_count) | `1` |

---

### Property Descriptions

<span id="class_RenderSceneBuffersConfiguration_property_anisotropic_filtering_level"></span>

[ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) **anisotropic_filtering_level** = `2` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_anisotropic_filtering_level)

- void **set_anisotropic_filtering_level** ( value: [ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) )
- [ViewportAnisotropicFiltering](class_renderingserver.md#enum_RenderingServer_ViewportAnisotropicFiltering) **get_anisotropic_filtering_level** ( )

Level of the anisotropic filter.

---

<span id="class_RenderSceneBuffersConfiguration_property_fsr_sharpness"></span>

[float](class_float.md#class_float) **fsr_sharpness** = `0.0` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_fsr_sharpness)

- void **set_fsr_sharpness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fsr_sharpness** ( )

FSR Sharpness applicable if FSR upscaling is used.

---

<span id="class_RenderSceneBuffersConfiguration_property_internal_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **internal_size** = `Vector2i(0, 0)` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_internal_size)

- void **set_internal_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_internal_size** ( )

The size of the 3D render buffer used for rendering.

---

<span id="class_RenderSceneBuffersConfiguration_property_msaa_3d"></span>

[ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) **msaa_3d** = `0` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_msaa_3d)

- void **set_msaa_3d** ( value: [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) )
- [ViewportMSAA](class_renderingserver.md#enum_RenderingServer_ViewportMSAA) **get_msaa_3d** ( )

The MSAA mode we're using for 3D rendering.

---

<span id="class_RenderSceneBuffersConfiguration_property_render_target"></span>

[RID](class_rid.md#class_RID) **render_target** = `RID()` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_render_target)

- void **set_render_target** ( value: [RID](class_rid.md#class_RID) )
- [RID](class_rid.md#class_RID) **get_render_target** ( )

The render target associated with these buffer.

---

<span id="class_RenderSceneBuffersConfiguration_property_scaling_3d_mode"></span>

[ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) **scaling_3d_mode** = `255` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_scaling_3d_mode)

- void **set_scaling_3d_mode** ( value: [ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) )
- [ViewportScaling3DMode](class_renderingserver.md#enum_RenderingServer_ViewportScaling3DMode) **get_scaling_3d_mode** ( )

The requested scaling mode with which we upscale/downscale if [internal_size](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_internal_size) and [target_size](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_target_size) are not equal.

---

<span id="class_RenderSceneBuffersConfiguration_property_screen_space_aa"></span>

[ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) **screen_space_aa** = `0` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_screen_space_aa)

- void **set_screen_space_aa** ( value: [ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) )
- [ViewportScreenSpaceAA](class_renderingserver.md#enum_RenderingServer_ViewportScreenSpaceAA) **get_screen_space_aa** ( )

The requested screen space AA applied in post processing.

---

<span id="class_RenderSceneBuffersConfiguration_property_target_size"></span>

[Vector2i](class_vector2i.md#class_Vector2i) **target_size** = `Vector2i(0, 0)` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_target_size)

- void **set_target_size** ( value: [Vector2i](class_vector2i.md#class_Vector2i) )
- [Vector2i](class_vector2i.md#class_Vector2i) **get_target_size** ( )

The target (upscale) size if scaling is used.

---

<span id="class_RenderSceneBuffersConfiguration_property_texture_mipmap_bias"></span>

[float](class_float.md#class_float) **texture_mipmap_bias** = `0.0` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_texture_mipmap_bias)

- void **set_texture_mipmap_bias** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_texture_mipmap_bias** ( )

Bias applied to mipmaps.

---

<span id="class_RenderSceneBuffersConfiguration_property_view_count"></span>

[int](class_int.md#class_int) **view_count** = `1` [🔗](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration_property_view_count)

- void **set_view_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_view_count** ( )

The number of views we're rendering.
