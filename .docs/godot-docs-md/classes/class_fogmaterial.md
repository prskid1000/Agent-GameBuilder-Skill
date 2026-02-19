<span id="class_FogMaterial"></span>

## FogMaterial

**Inherits:** [Material](class_material.md#class_Material) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A material that controls how volumetric fog is rendered, to be assigned to a [FogVolume](class_fogvolume.md#class_FogVolume).

### Description

A [Material](class_material.md#class_Material) resource that can be used by [FogVolume](class_fogvolume.md#class_FogVolume) s to draw volumetric effects.

If you need more advanced effects, use a custom [fog shader](../tutorials/shaders/shader_reference/fog_shader.md).

### Properties


| [Color](class_color.md#class_Color) | [albedo](class_fogmaterial.md#class_FogMaterial_property_albedo) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [density](class_fogmaterial.md#class_FogMaterial_property_density) | `1.0` |
| [Texture3D](class_texture3d.md#class_Texture3D) | [density_texture](class_fogmaterial.md#class_FogMaterial_property_density_texture) |
| [float](class_float.md#class_float) | [edge_fade](class_fogmaterial.md#class_FogMaterial_property_edge_fade) | `0.1` |
| [Color](class_color.md#class_Color) | [emission](class_fogmaterial.md#class_FogMaterial_property_emission) | `Color(0, 0, 0, 1)` |
| [float](class_float.md#class_float) | [height_falloff](class_fogmaterial.md#class_FogMaterial_property_height_falloff) | `0.0` |

---

### Property Descriptions

<span id="class_FogMaterial_property_albedo"></span>

[Color](class_color.md#class_Color) **albedo** = `Color(1, 1, 1, 1)` [🔗](class_fogmaterial.md#class_FogMaterial_property_albedo)

- void **set_albedo** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_albedo** ( )

The single-scattering [Color](class_color.md#class_Color) of the [FogVolume](class_fogvolume.md#class_FogVolume). Internally, [albedo](class_fogmaterial.md#class_FogMaterial_property_albedo) is converted into single-scattering, which is additively blended with other [FogVolume](class_fogvolume.md#class_FogVolume) s and the [Environment.volumetric_fog_albedo](class_environment.md#class_Environment_property_volumetric_fog_albedo).

---

<span id="class_FogMaterial_property_density"></span>

[float](class_float.md#class_float) **density** = `1.0` [🔗](class_fogmaterial.md#class_FogMaterial_property_density)

- void **set_density** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_density** ( )

The density of the [FogVolume](class_fogvolume.md#class_FogVolume). Denser objects are more opaque, but may suffer from under-sampling artifacts that look like stripes. Negative values can be used to subtract fog from other [FogVolume](class_fogvolume.md#class_FogVolume) s or global volumetric fog.

 **Note:** Due to limited precision, [density](class_fogmaterial.md#class_FogMaterial_property_density) values between `-0.001` and `0.001` (exclusive) act like `0.0`. This does not apply to [Environment.volumetric_fog_density](class_environment.md#class_Environment_property_volumetric_fog_density).

---

<span id="class_FogMaterial_property_density_texture"></span>

[Texture3D](class_texture3d.md#class_Texture3D) **density_texture** [🔗](class_fogmaterial.md#class_FogMaterial_property_density_texture)

- void **set_density_texture** ( value: [Texture3D](class_texture3d.md#class_Texture3D) )
- [Texture3D](class_texture3d.md#class_Texture3D) **get_density_texture** ( )

The 3D texture that is used to scale the [density](class_fogmaterial.md#class_FogMaterial_property_density) of the [FogVolume](class_fogvolume.md#class_FogVolume). This can be used to vary fog density within the [FogVolume](class_fogvolume.md#class_FogVolume) with any kind of static pattern. For animated effects, consider using a custom [fog shader](../tutorials/shaders/shader_reference/fog_shader.md).

---

<span id="class_FogMaterial_property_edge_fade"></span>

[float](class_float.md#class_float) **edge_fade** = `0.1` [🔗](class_fogmaterial.md#class_FogMaterial_property_edge_fade)

- void **set_edge_fade** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_edge_fade** ( )

The hardness of the edges of the [FogVolume](class_fogvolume.md#class_FogVolume). A higher value will result in softer edges, while a lower value will result in harder edges.

---

<span id="class_FogMaterial_property_emission"></span>

[Color](class_color.md#class_Color) **emission** = `Color(0, 0, 0, 1)` [🔗](class_fogmaterial.md#class_FogMaterial_property_emission)

- void **set_emission** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_emission** ( )

The [Color](class_color.md#class_Color) of the light emitted by the [FogVolume](class_fogvolume.md#class_FogVolume). Emitted light will not cast light or shadows on other objects, but can be useful for modulating the [Color](class_color.md#class_Color) of the [FogVolume](class_fogvolume.md#class_FogVolume) independently from light sources.

---

<span id="class_FogMaterial_property_height_falloff"></span>

[float](class_float.md#class_float) **height_falloff** = `0.0` [🔗](class_fogmaterial.md#class_FogMaterial_property_height_falloff)

- void **set_height_falloff** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height_falloff** ( )

The rate by which the height-based fog decreases in density as height increases in world space. A high falloff will result in a sharp transition, while a low falloff will result in a smoother transition. A value of `0.0` results in uniform-density fog. The height threshold is determined by the height of the associated [FogVolume](class_fogvolume.md#class_FogVolume).
