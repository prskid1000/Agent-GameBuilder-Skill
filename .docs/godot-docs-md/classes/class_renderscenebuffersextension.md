<span id="class_RenderSceneBuffersExtension"></span>

## RenderSceneBuffersExtension

**Inherits:** [RenderSceneBuffers](class_renderscenebuffers.md#class_RenderSceneBuffers) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

### Description

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

### Methods


| void | [_configure](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__configure) ( config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration) ) virtual |
| --- | --- |
| void | [_set_anisotropic_filtering_level](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__set_anisotropic_filtering_level) ( anisotropic_filtering_level: [int](class_int.md#class_int) ) virtual |
| void | [_set_fsr_sharpness](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__set_fsr_sharpness) ( fsr_sharpness: [float](class_float.md#class_float) ) virtual |
| void | [_set_texture_mipmap_bias](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__set_texture_mipmap_bias) ( texture_mipmap_bias: [float](class_float.md#class_float) ) virtual |
| void | [_set_use_debanding](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__set_use_debanding) ( use_debanding: [bool](class_bool.md#class_bool) ) virtual |

---

### Method Descriptions

<span id="class_RenderSceneBuffersExtension_private_method__configure"></span>

void **_configure** ( config: [RenderSceneBuffersConfiguration](class_renderscenebuffersconfiguration.md#class_RenderSceneBuffersConfiguration) ) *virtual* [🔗](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__configure)

Implement this in GDExtension to handle the (re)sizing of a viewport.

---

<span id="class_RenderSceneBuffersExtension_private_method__set_anisotropic_filtering_level"></span>

void **_set_anisotropic_filtering_level** ( anisotropic_filtering_level: [int](class_int.md#class_int) ) *virtual* [🔗](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__set_anisotropic_filtering_level)

Implement this in GDExtension to change the anisotropic filtering level.

---

<span id="class_RenderSceneBuffersExtension_private_method__set_fsr_sharpness"></span>

void **_set_fsr_sharpness** ( fsr_sharpness: [float](class_float.md#class_float) ) *virtual* [🔗](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__set_fsr_sharpness)

Implement this in GDExtension to record a new FSR sharpness value.

---

<span id="class_RenderSceneBuffersExtension_private_method__set_texture_mipmap_bias"></span>

void **_set_texture_mipmap_bias** ( texture_mipmap_bias: [float](class_float.md#class_float) ) *virtual* [🔗](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__set_texture_mipmap_bias)

Implement this in GDExtension to change the texture mipmap bias.

---

<span id="class_RenderSceneBuffersExtension_private_method__set_use_debanding"></span>

void **_set_use_debanding** ( use_debanding: [bool](class_bool.md#class_bool) ) *virtual* [🔗](class_renderscenebuffersextension.md#class_RenderSceneBuffersExtension_private_method__set_use_debanding)

Implement this in GDExtension to react to the debanding flag changing.
