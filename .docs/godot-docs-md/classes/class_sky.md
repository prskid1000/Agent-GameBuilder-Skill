<span id="class_Sky"></span>

## Sky

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Defines a 3D environment's background by using a [Material](class_material.md#class_Material).

### Description

The **Sky** class uses a [Material](class_material.md#class_Material) to render a 3D environment's background and the light it emits by updating the reflection/radiance cubemaps.

### Properties


| [ProcessMode](class_sky.md#enum_Sky_ProcessMode) | [process_mode](class_sky.md#class_Sky_property_process_mode) | `0` |
| --- | --- | --- |
| [RadianceSize](class_sky.md#enum_Sky_RadianceSize) | [radiance_size](class_sky.md#class_Sky_property_radiance_size) | `3` |
| [Material](class_material.md#class_Material) | [sky_material](class_sky.md#class_Sky_property_sky_material) |

---

### Enumerations

<span id="enum_Sky_RadianceSize"></span>

enum **RadianceSize**: [🔗](class_sky.md#enum_Sky_RadianceSize)

<span id="class_Sky_constant_RADIANCE_SIZE_32"></span>

[RadianceSize](class_sky.md#enum_Sky_RadianceSize) **RADIANCE_SIZE_32** = `0`

Radiance texture size is 32×32 pixels.

<span id="class_Sky_constant_RADIANCE_SIZE_64"></span>

[RadianceSize](class_sky.md#enum_Sky_RadianceSize) **RADIANCE_SIZE_64** = `1`

Radiance texture size is 64×64 pixels.

<span id="class_Sky_constant_RADIANCE_SIZE_128"></span>

[RadianceSize](class_sky.md#enum_Sky_RadianceSize) **RADIANCE_SIZE_128** = `2`

Radiance texture size is 128×128 pixels.

<span id="class_Sky_constant_RADIANCE_SIZE_256"></span>

[RadianceSize](class_sky.md#enum_Sky_RadianceSize) **RADIANCE_SIZE_256** = `3`

Radiance texture size is 256×256 pixels.

<span id="class_Sky_constant_RADIANCE_SIZE_512"></span>

[RadianceSize](class_sky.md#enum_Sky_RadianceSize) **RADIANCE_SIZE_512** = `4`

Radiance texture size is 512×512 pixels.

<span id="class_Sky_constant_RADIANCE_SIZE_1024"></span>

[RadianceSize](class_sky.md#enum_Sky_RadianceSize) **RADIANCE_SIZE_1024** = `5`

Radiance texture size is 1024×1024 pixels.

<span id="class_Sky_constant_RADIANCE_SIZE_2048"></span>

[RadianceSize](class_sky.md#enum_Sky_RadianceSize) **RADIANCE_SIZE_2048** = `6`

Radiance texture size is 2048×2048 pixels.

<span id="class_Sky_constant_RADIANCE_SIZE_MAX"></span>

[RadianceSize](class_sky.md#enum_Sky_RadianceSize) **RADIANCE_SIZE_MAX** = `7`

Represents the size of the [RadianceSize](class_sky.md#enum_Sky_RadianceSize) enum.

---

<span id="enum_Sky_ProcessMode"></span>

enum **ProcessMode**: [🔗](class_sky.md#enum_Sky_ProcessMode)

<span id="class_Sky_constant_PROCESS_MODE_AUTOMATIC"></span>

[ProcessMode](class_sky.md#enum_Sky_ProcessMode) **PROCESS_MODE_AUTOMATIC** = `0`

Automatically selects the appropriate process mode based on your sky shader. If your shader uses `TIME` or `POSITION`, this will use [PROCESS_MODE_REALTIME](class_sky.md#class_Sky_constant_PROCESS_MODE_REALTIME). If your shader uses any of the `LIGHT_*` variables or any custom uniforms, this uses [PROCESS_MODE_INCREMENTAL](class_sky.md#class_Sky_constant_PROCESS_MODE_INCREMENTAL). Otherwise, this defaults to [PROCESS_MODE_QUALITY](class_sky.md#class_Sky_constant_PROCESS_MODE_QUALITY).

<span id="class_Sky_constant_PROCESS_MODE_QUALITY"></span>

[ProcessMode](class_sky.md#enum_Sky_ProcessMode) **PROCESS_MODE_QUALITY** = `1`

Uses high quality importance sampling to process the radiance map. In general, this results in much higher quality than [PROCESS_MODE_REALTIME](class_sky.md#class_Sky_constant_PROCESS_MODE_REALTIME) but takes much longer to generate. This should not be used if you plan on changing the sky at runtime. If you are finding that the reflection is not blurry enough and is showing sparkles or fireflies, try increasing ProjectSettings.rendering/reflections/sky_reflections/ggx_samples.

<span id="class_Sky_constant_PROCESS_MODE_INCREMENTAL"></span>

[ProcessMode](class_sky.md#enum_Sky_ProcessMode) **PROCESS_MODE_INCREMENTAL** = `2`

Uses the same high quality importance sampling to process the radiance map as [PROCESS_MODE_QUALITY](class_sky.md#class_Sky_constant_PROCESS_MODE_QUALITY), but updates over several frames. The number of frames is determined by ProjectSettings.rendering/reflections/sky_reflections/roughness_layers. Use this when you need highest quality radiance maps, but have a sky that updates slowly.

<span id="class_Sky_constant_PROCESS_MODE_REALTIME"></span>

[ProcessMode](class_sky.md#enum_Sky_ProcessMode) **PROCESS_MODE_REALTIME** = `3`

Uses the fast filtering algorithm to process the radiance map. In general this results in lower quality, but substantially faster run times. If you need better quality, but still need to update the sky every frame, consider turning on ProjectSettings.rendering/reflections/sky_reflections/fast_filter_high_quality.

 **Note:** The fast filtering algorithm is limited to 256×256 cubemaps, so [radiance_size](class_sky.md#class_Sky_property_radiance_size) must be set to [RADIANCE_SIZE_256](class_sky.md#class_Sky_constant_RADIANCE_SIZE_256). Otherwise, a warning is printed and the overridden radiance size is ignored.

---

### Property Descriptions

<span id="class_Sky_property_process_mode"></span>

[ProcessMode](class_sky.md#enum_Sky_ProcessMode) **process_mode** = `0` [🔗](class_sky.md#class_Sky_property_process_mode)

- void **set_process_mode** ( value: [ProcessMode](class_sky.md#enum_Sky_ProcessMode) )
- [ProcessMode](class_sky.md#enum_Sky_ProcessMode) **get_process_mode** ( )

The method for generating the radiance map from the sky. The radiance map is a cubemap with increasingly blurry versions of the sky corresponding to different levels of roughness. Radiance maps can be expensive to calculate.

---

<span id="class_Sky_property_radiance_size"></span>

[RadianceSize](class_sky.md#enum_Sky_RadianceSize) **radiance_size** = `3` [🔗](class_sky.md#class_Sky_property_radiance_size)

- void **set_radiance_size** ( value: [RadianceSize](class_sky.md#enum_Sky_RadianceSize) )
- [RadianceSize](class_sky.md#enum_Sky_RadianceSize) **get_radiance_size** ( )

The **Sky**'s radiance map size. The higher the radiance map size, the more detailed the lighting from the **Sky** will be.

 **Note:** Some hardware will have trouble with higher radiance sizes, especially [RADIANCE_SIZE_512](class_sky.md#class_Sky_constant_RADIANCE_SIZE_512) and above. Only use such high values on high-end hardware.

---

<span id="class_Sky_property_sky_material"></span>

[Material](class_material.md#class_Material) **sky_material** [🔗](class_sky.md#class_Sky_property_sky_material)

- void **set_material** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_material** ( )

[Material](class_material.md#class_Material) used to draw the background. Can be [PanoramaSkyMaterial](class_panoramaskymaterial.md#class_PanoramaSkyMaterial), [ProceduralSkyMaterial](class_proceduralskymaterial.md#class_ProceduralSkyMaterial), [PhysicalSkyMaterial](class_physicalskymaterial.md#class_PhysicalSkyMaterial), or even a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial) if you want to use your own custom shader.
