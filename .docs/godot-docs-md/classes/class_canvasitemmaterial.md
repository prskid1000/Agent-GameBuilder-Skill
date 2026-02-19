<span id="class_CanvasItemMaterial"></span>

## CanvasItemMaterial

**Inherits:** [Material](class_material.md#class_Material) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A material for [CanvasItem](class_canvasitem.md#class_CanvasItem) s.

### Description

**CanvasItemMaterial** s provide a means of modifying the textures associated with a CanvasItem. They specialize in describing blend and lighting behaviors for textures. Use a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) to more fully customize a material's interactions with a [CanvasItem](class_canvasitem.md#class_CanvasItem).

### Properties


| [BlendMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode) | [blend_mode](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_blend_mode) | `0` |
| --- | --- | --- |
| [LightMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_LightMode) | [light_mode](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_light_mode) | `0` |
| [int](class_int.md#class_int) | [particles_anim_h_frames](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_anim_h_frames) |
| [bool](class_bool.md#class_bool) | [particles_anim_loop](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_anim_loop) |
| [int](class_int.md#class_int) | [particles_anim_v_frames](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_anim_v_frames) |
| [bool](class_bool.md#class_bool) | [particles_animation](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_animation) | `false` |

---

### Enumerations

<span id="enum_CanvasItemMaterial_BlendMode"></span>

enum **BlendMode**: [🔗](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode)

<span id="class_CanvasItemMaterial_constant_BLEND_MODE_MIX"></span>

[BlendMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode) **BLEND_MODE_MIX** = `0`

Mix blending mode. Colors are assumed to be independent of the alpha (opacity) value.

<span id="class_CanvasItemMaterial_constant_BLEND_MODE_ADD"></span>

[BlendMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode) **BLEND_MODE_ADD** = `1`

Additive blending mode.

<span id="class_CanvasItemMaterial_constant_BLEND_MODE_SUB"></span>

[BlendMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode) **BLEND_MODE_SUB** = `2`

Subtractive blending mode.

<span id="class_CanvasItemMaterial_constant_BLEND_MODE_MUL"></span>

[BlendMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode) **BLEND_MODE_MUL** = `3`

Multiplicative blending mode.

<span id="class_CanvasItemMaterial_constant_BLEND_MODE_PREMULT_ALPHA"></span>

[BlendMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode) **BLEND_MODE_PREMULT_ALPHA** = `4`

Mix blending mode. Colors are assumed to be premultiplied by the alpha (opacity) value.

---

<span id="enum_CanvasItemMaterial_LightMode"></span>

enum **LightMode**: [🔗](class_canvasitemmaterial.md#enum_CanvasItemMaterial_LightMode)

<span id="class_CanvasItemMaterial_constant_LIGHT_MODE_NORMAL"></span>

[LightMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_LightMode) **LIGHT_MODE_NORMAL** = `0`

Render the material using both light and non-light sensitive material properties.

<span id="class_CanvasItemMaterial_constant_LIGHT_MODE_UNSHADED"></span>

[LightMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_LightMode) **LIGHT_MODE_UNSHADED** = `1`

Render the material as if there were no light.

<span id="class_CanvasItemMaterial_constant_LIGHT_MODE_LIGHT_ONLY"></span>

[LightMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_LightMode) **LIGHT_MODE_LIGHT_ONLY** = `2`

Render the material as if there were only light.

---

### Property Descriptions

<span id="class_CanvasItemMaterial_property_blend_mode"></span>

[BlendMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode) **blend_mode** = `0` [🔗](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_blend_mode)

- void **set_blend_mode** ( value: [BlendMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode) )
- [BlendMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_BlendMode) **get_blend_mode** ( )

The manner in which a material's rendering is applied to underlying textures.

---

<span id="class_CanvasItemMaterial_property_light_mode"></span>

[LightMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_LightMode) **light_mode** = `0` [🔗](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_light_mode)

- void **set_light_mode** ( value: [LightMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_LightMode) )
- [LightMode](class_canvasitemmaterial.md#enum_CanvasItemMaterial_LightMode) **get_light_mode** ( )

The manner in which material reacts to lighting.

---

<span id="class_CanvasItemMaterial_property_particles_anim_h_frames"></span>

[int](class_int.md#class_int) **particles_anim_h_frames** [🔗](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_anim_h_frames)

- void **set_particles_anim_h_frames** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_particles_anim_h_frames** ( )

The number of columns in the spritesheet assigned as [Texture2D](class_texture2d.md#class_Texture2D) for a [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) or [CPUParticles2D](class_cpuparticles2d.md#class_CPUParticles2D).

 **Note:** This property is only used and visible in the editor if [particles_animation](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_animation) is `true`.

---

<span id="class_CanvasItemMaterial_property_particles_anim_loop"></span>

[bool](class_bool.md#class_bool) **particles_anim_loop** [🔗](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_anim_loop)

- void **set_particles_anim_loop** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particles_anim_loop** ( )

If `true`, the particles animation will loop.

 **Note:** This property is only used and visible in the editor if [particles_animation](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_animation) is `true`.

---

<span id="class_CanvasItemMaterial_property_particles_anim_v_frames"></span>

[int](class_int.md#class_int) **particles_anim_v_frames** [🔗](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_anim_v_frames)

- void **set_particles_anim_v_frames** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_particles_anim_v_frames** ( )

The number of rows in the spritesheet assigned as [Texture2D](class_texture2d.md#class_Texture2D) for a [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) or [CPUParticles2D](class_cpuparticles2d.md#class_CPUParticles2D).

 **Note:** This property is only used and visible in the editor if [particles_animation](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_animation) is `true`.

---

<span id="class_CanvasItemMaterial_property_particles_animation"></span>

[bool](class_bool.md#class_bool) **particles_animation** = `false` [🔗](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_animation)

- void **set_particles_animation** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particles_animation** ( )

If `true`, enable spritesheet-based animation features when assigned to [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) and [CPUParticles2D](class_cpuparticles2d.md#class_CPUParticles2D) nodes. The [ParticleProcessMaterial.anim_speed_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_speed_max) or [CPUParticles2D.anim_speed_max](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_speed_max) should also be set to a positive value for the animation to play.

This property (and other `particles_anim_*` properties that depend on it) has no effect on other types of nodes.
