<span id="class_Light3D"></span>

## Light3D

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D), [OmniLight3D](class_omnilight3d.md#class_OmniLight3D), [SpotLight3D](class_spotlight3d.md#class_SpotLight3D)

Provides a base class for different kinds of light nodes.

### Description

Light3D is the *abstract* base class for light nodes. As it can't be instantiated, it shouldn't be used directly. Other types of light nodes inherit from it. Light3D contains the common variables and parameters used for lighting.

### Tutorials

- [3D lights and shadows](../tutorials/3d/lights_and_shadows.md)

- [Faking global illumination](../tutorials/3d/global_illumination/faking_global_illumination.md)

- Third Person Shooter (TPS) Demo

### Properties


| [float](class_float.md#class_float) | [distance_fade_begin](class_light3d.md#class_Light3D_property_distance_fade_begin) | `40.0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [distance_fade_enabled](class_light3d.md#class_Light3D_property_distance_fade_enabled) | `false` |
| [float](class_float.md#class_float) | [distance_fade_length](class_light3d.md#class_Light3D_property_distance_fade_length) | `10.0` |
| [float](class_float.md#class_float) | [distance_fade_shadow](class_light3d.md#class_Light3D_property_distance_fade_shadow) | `50.0` |
| [bool](class_bool.md#class_bool) | [editor_only](class_light3d.md#class_Light3D_property_editor_only) | `false` |
| [float](class_float.md#class_float) | [light_angular_distance](class_light3d.md#class_Light3D_property_light_angular_distance) | `0.0` |
| [BakeMode](class_light3d.md#enum_Light3D_BakeMode) | [light_bake_mode](class_light3d.md#class_Light3D_property_light_bake_mode) | `2` |
| [Color](class_color.md#class_Color) | [light_color](class_light3d.md#class_Light3D_property_light_color) | `Color(1, 1, 1, 1)` |
| [int](class_int.md#class_int) | [light_cull_mask](class_light3d.md#class_Light3D_property_light_cull_mask) | `4294967295` |
| [float](class_float.md#class_float) | [light_energy](class_light3d.md#class_Light3D_property_light_energy) | `1.0` |
| [float](class_float.md#class_float) | [light_indirect_energy](class_light3d.md#class_Light3D_property_light_indirect_energy) | `1.0` |
| [float](class_float.md#class_float) | [light_intensity_lumens](class_light3d.md#class_Light3D_property_light_intensity_lumens) |
| [float](class_float.md#class_float) | [light_intensity_lux](class_light3d.md#class_Light3D_property_light_intensity_lux) |
| [bool](class_bool.md#class_bool) | [light_negative](class_light3d.md#class_Light3D_property_light_negative) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [light_projector](class_light3d.md#class_Light3D_property_light_projector) |
| [float](class_float.md#class_float) | [light_size](class_light3d.md#class_Light3D_property_light_size) | `0.0` |
| [float](class_float.md#class_float) | [light_specular](class_light3d.md#class_Light3D_property_light_specular) | `1.0` |
| [float](class_float.md#class_float) | [light_temperature](class_light3d.md#class_Light3D_property_light_temperature) |
| [float](class_float.md#class_float) | [light_volumetric_fog_energy](class_light3d.md#class_Light3D_property_light_volumetric_fog_energy) | `1.0` |
| [float](class_float.md#class_float) | [shadow_bias](class_light3d.md#class_Light3D_property_shadow_bias) | `0.1` |
| [float](class_float.md#class_float) | [shadow_blur](class_light3d.md#class_Light3D_property_shadow_blur) | `1.0` |
| [int](class_int.md#class_int) | [shadow_caster_mask](class_light3d.md#class_Light3D_property_shadow_caster_mask) | `4294967295` |
| [bool](class_bool.md#class_bool) | [shadow_enabled](class_light3d.md#class_Light3D_property_shadow_enabled) | `false` |
| [float](class_float.md#class_float) | [shadow_normal_bias](class_light3d.md#class_Light3D_property_shadow_normal_bias) | `2.0` |
| [float](class_float.md#class_float) | [shadow_opacity](class_light3d.md#class_Light3D_property_shadow_opacity) | `1.0` |
| [bool](class_bool.md#class_bool) | [shadow_reverse_cull_face](class_light3d.md#class_Light3D_property_shadow_reverse_cull_face) | `false` |
| [float](class_float.md#class_float) | [shadow_transmittance_bias](class_light3d.md#class_Light3D_property_shadow_transmittance_bias) | `0.05` |

### Methods


| [Color](class_color.md#class_Color) | [get_correlated_color](class_light3d.md#class_Light3D_method_get_correlated_color) ( ) const |
| --- | --- |
| [float](class_float.md#class_float) | [get_param](class_light3d.md#class_Light3D_method_get_param) ( param: [Param](class_light3d.md#enum_Light3D_Param) ) const |
| void | [set_param](class_light3d.md#class_Light3D_method_set_param) ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_Light3D_Param"></span>

enum **Param**: [🔗](class_light3d.md#enum_Light3D_Param)

<span id="class_Light3D_constant_PARAM_ENERGY"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_ENERGY** = `0`

Constant for accessing [light_energy](class_light3d.md#class_Light3D_property_light_energy).

<span id="class_Light3D_constant_PARAM_INDIRECT_ENERGY"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_INDIRECT_ENERGY** = `1`

Constant for accessing [light_indirect_energy](class_light3d.md#class_Light3D_property_light_indirect_energy).

<span id="class_Light3D_constant_PARAM_VOLUMETRIC_FOG_ENERGY"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_VOLUMETRIC_FOG_ENERGY** = `2`

Constant for accessing [light_volumetric_fog_energy](class_light3d.md#class_Light3D_property_light_volumetric_fog_energy).

<span id="class_Light3D_constant_PARAM_SPECULAR"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SPECULAR** = `3`

Constant for accessing [light_specular](class_light3d.md#class_Light3D_property_light_specular).

<span id="class_Light3D_constant_PARAM_RANGE"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_RANGE** = `4`

Constant for accessing [OmniLight3D.omni_range](class_omnilight3d.md#class_OmniLight3D_property_omni_range) or [SpotLight3D.spot_range](class_spotlight3d.md#class_SpotLight3D_property_spot_range).

<span id="class_Light3D_constant_PARAM_SIZE"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SIZE** = `5`

Constant for accessing [light_size](class_light3d.md#class_Light3D_property_light_size).

<span id="class_Light3D_constant_PARAM_ATTENUATION"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_ATTENUATION** = `6`

Constant for accessing [OmniLight3D.omni_attenuation](class_omnilight3d.md#class_OmniLight3D_property_omni_attenuation) or [SpotLight3D.spot_attenuation](class_spotlight3d.md#class_SpotLight3D_property_spot_attenuation).

<span id="class_Light3D_constant_PARAM_SPOT_ANGLE"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SPOT_ANGLE** = `7`

Constant for accessing [SpotLight3D.spot_angle](class_spotlight3d.md#class_SpotLight3D_property_spot_angle).

<span id="class_Light3D_constant_PARAM_SPOT_ATTENUATION"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SPOT_ATTENUATION** = `8`

Constant for accessing [SpotLight3D.spot_angle_attenuation](class_spotlight3d.md#class_SpotLight3D_property_spot_angle_attenuation).

<span id="class_Light3D_constant_PARAM_SHADOW_MAX_DISTANCE"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_MAX_DISTANCE** = `9`

Constant for accessing [DirectionalLight3D.directional_shadow_max_distance](class_directionallight3d.md#class_DirectionalLight3D_property_directional_shadow_max_distance).

<span id="class_Light3D_constant_PARAM_SHADOW_SPLIT_1_OFFSET"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_SPLIT_1_OFFSET** = `10`

Constant for accessing [DirectionalLight3D.directional_shadow_split_1](class_directionallight3d.md#class_DirectionalLight3D_property_directional_shadow_split_1).

<span id="class_Light3D_constant_PARAM_SHADOW_SPLIT_2_OFFSET"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_SPLIT_2_OFFSET** = `11`

Constant for accessing [DirectionalLight3D.directional_shadow_split_2](class_directionallight3d.md#class_DirectionalLight3D_property_directional_shadow_split_2).

<span id="class_Light3D_constant_PARAM_SHADOW_SPLIT_3_OFFSET"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_SPLIT_3_OFFSET** = `12`

Constant for accessing [DirectionalLight3D.directional_shadow_split_3](class_directionallight3d.md#class_DirectionalLight3D_property_directional_shadow_split_3).

<span id="class_Light3D_constant_PARAM_SHADOW_FADE_START"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_FADE_START** = `13`

Constant for accessing [DirectionalLight3D.directional_shadow_fade_start](class_directionallight3d.md#class_DirectionalLight3D_property_directional_shadow_fade_start).

<span id="class_Light3D_constant_PARAM_SHADOW_NORMAL_BIAS"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_NORMAL_BIAS** = `14`

Constant for accessing [shadow_normal_bias](class_light3d.md#class_Light3D_property_shadow_normal_bias).

<span id="class_Light3D_constant_PARAM_SHADOW_BIAS"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_BIAS** = `15`

Constant for accessing [shadow_bias](class_light3d.md#class_Light3D_property_shadow_bias).

<span id="class_Light3D_constant_PARAM_SHADOW_PANCAKE_SIZE"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_PANCAKE_SIZE** = `16`

Constant for accessing [DirectionalLight3D.directional_shadow_pancake_size](class_directionallight3d.md#class_DirectionalLight3D_property_directional_shadow_pancake_size).

<span id="class_Light3D_constant_PARAM_SHADOW_OPACITY"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_OPACITY** = `17`

Constant for accessing [shadow_opacity](class_light3d.md#class_Light3D_property_shadow_opacity).

<span id="class_Light3D_constant_PARAM_SHADOW_BLUR"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_SHADOW_BLUR** = `18`

Constant for accessing [shadow_blur](class_light3d.md#class_Light3D_property_shadow_blur).

<span id="class_Light3D_constant_PARAM_TRANSMITTANCE_BIAS"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_TRANSMITTANCE_BIAS** = `19`

Constant for accessing [shadow_transmittance_bias](class_light3d.md#class_Light3D_property_shadow_transmittance_bias).

<span id="class_Light3D_constant_PARAM_INTENSITY"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_INTENSITY** = `20`

Constant for accessing [light_intensity_lumens](class_light3d.md#class_Light3D_property_light_intensity_lumens) and [light_intensity_lux](class_light3d.md#class_Light3D_property_light_intensity_lux). Only used when ProjectSettings.rendering/lights_and_shadows/use_physical_light_units is `true`.

<span id="class_Light3D_constant_PARAM_MAX"></span>

[Param](class_light3d.md#enum_Light3D_Param) **PARAM_MAX** = `21`

Represents the size of the [Param](class_light3d.md#enum_Light3D_Param) enum.

---

<span id="enum_Light3D_BakeMode"></span>

enum **BakeMode**: [🔗](class_light3d.md#enum_Light3D_BakeMode)

<span id="class_Light3D_constant_BAKE_DISABLED"></span>

[BakeMode](class_light3d.md#enum_Light3D_BakeMode) **BAKE_DISABLED** = `0`

Light is ignored when baking. This is the fastest mode, but the light will not be taken into account when baking global illumination. This mode should generally be used for dynamic lights that change quickly, as the effect of global illumination is less noticeable on those lights.

 **Note:** Hiding a light does *not* affect baking [LightmapGI](class_lightmapgi.md#class_LightmapGI). Hiding a light will still affect baking [VoxelGI](class_voxelgi.md#class_VoxelGI) and SDFGI (see [Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled)).

<span id="class_Light3D_constant_BAKE_STATIC"></span>

[BakeMode](class_light3d.md#enum_Light3D_BakeMode) **BAKE_STATIC** = `1`

Light is taken into account in static baking ([VoxelGI](class_voxelgi.md#class_VoxelGI), [LightmapGI](class_lightmapgi.md#class_LightmapGI), SDFGI ([Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled))). The light can be moved around or modified, but its global illumination will not update in real-time. This is suitable for subtle changes (such as flickering torches), but generally not large changes such as toggling a light on and off.

 **Note:** The light is not baked in [LightmapGI](class_lightmapgi.md#class_LightmapGI) if [editor_only](class_light3d.md#class_Light3D_property_editor_only) is `true`.

<span id="class_Light3D_constant_BAKE_DYNAMIC"></span>

[BakeMode](class_light3d.md#enum_Light3D_BakeMode) **BAKE_DYNAMIC** = `2`

Light is taken into account in dynamic baking ([VoxelGI](class_voxelgi.md#class_VoxelGI) and SDFGI ([Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled)) only). The light can be moved around or modified with global illumination updating in real-time. The light's global illumination appearance will be slightly different compared to [BAKE_STATIC](class_light3d.md#class_Light3D_constant_BAKE_STATIC). This has a greater performance cost compared to [BAKE_STATIC](class_light3d.md#class_Light3D_constant_BAKE_STATIC). When using SDFGI, the update speed of dynamic lights is affected by ProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights.

---

### Property Descriptions

<span id="class_Light3D_property_distance_fade_begin"></span>

[float](class_float.md#class_float) **distance_fade_begin** = `40.0` [🔗](class_light3d.md#class_Light3D_property_distance_fade_begin)

- void **set_distance_fade_begin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_distance_fade_begin** ( )

The distance from the camera at which the light begins to fade away (in 3D units).

 **Note:** Only effective for [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) and [SpotLight3D](class_spotlight3d.md#class_SpotLight3D).

---

<span id="class_Light3D_property_distance_fade_enabled"></span>

[bool](class_bool.md#class_bool) **distance_fade_enabled** = `false` [🔗](class_light3d.md#class_Light3D_property_distance_fade_enabled)

- void **set_enable_distance_fade** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_distance_fade_enabled** ( )

If `true`, the light will smoothly fade away when far from the active [Camera3D](class_camera3d.md#class_Camera3D) starting at [distance_fade_begin](class_light3d.md#class_Light3D_property_distance_fade_begin). This acts as a form of level of detail (LOD). The light will fade out over [distance_fade_begin](class_light3d.md#class_Light3D_property_distance_fade_begin) + [distance_fade_length](class_light3d.md#class_Light3D_property_distance_fade_length), after which it will be culled and not sent to the shader at all. Use this to reduce the number of active lights in a scene and thus improve performance.

 **Note:** Only effective for [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) and [SpotLight3D](class_spotlight3d.md#class_SpotLight3D).

---

<span id="class_Light3D_property_distance_fade_length"></span>

[float](class_float.md#class_float) **distance_fade_length** = `10.0` [🔗](class_light3d.md#class_Light3D_property_distance_fade_length)

- void **set_distance_fade_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_distance_fade_length** ( )

Distance over which the light and its shadow fades. The light's energy and shadow's opacity is progressively reduced over this distance and is completely invisible at the end.

 **Note:** Only effective for [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) and [SpotLight3D](class_spotlight3d.md#class_SpotLight3D).

---

<span id="class_Light3D_property_distance_fade_shadow"></span>

[float](class_float.md#class_float) **distance_fade_shadow** = `50.0` [🔗](class_light3d.md#class_Light3D_property_distance_fade_shadow)

- void **set_distance_fade_shadow** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_distance_fade_shadow** ( )

The distance from the camera at which the light's shadow cuts off (in 3D units). Set this to a value lower than [distance_fade_begin](class_light3d.md#class_Light3D_property_distance_fade_begin) + [distance_fade_length](class_light3d.md#class_Light3D_property_distance_fade_length) to further improve performance, as shadow rendering is often more expensive than light rendering itself.

 **Note:** Only effective for [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) and [SpotLight3D](class_spotlight3d.md#class_SpotLight3D), and only when [shadow_enabled](class_light3d.md#class_Light3D_property_shadow_enabled) is `true`.

---

<span id="class_Light3D_property_editor_only"></span>

[bool](class_bool.md#class_bool) **editor_only** = `false` [🔗](class_light3d.md#class_Light3D_property_editor_only)

- void **set_editor_only** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_editor_only** ( )

If `true`, the light only appears in the editor and will not be visible at runtime. If `true`, the light will never be baked in [LightmapGI](class_lightmapgi.md#class_LightmapGI) regardless of its [light_bake_mode](class_light3d.md#class_Light3D_property_light_bake_mode).

---

<span id="class_Light3D_property_light_angular_distance"></span>

[float](class_float.md#class_float) **light_angular_distance** = `0.0` [🔗](class_light3d.md#class_Light3D_property_light_angular_distance)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

The light's angular size in degrees. Increasing this will make shadows softer at greater distances (also called percentage-closer soft shadows, or PCSS). Only available for [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D) s. For reference, the Sun from the Earth is approximately `0.5`. Increasing this value above `0.0` for lights with shadows enabled will have a noticeable performance cost due to PCSS.

 **Note:** [light_angular_distance](class_light3d.md#class_Light3D_property_light_angular_distance) is not affected by [Node3D.scale](class_node3d.md#class_Node3D_property_scale) (the light's scale or its parent's scale).

 **Note:** PCSS for directional lights is only supported in the Forward+ rendering method, not Mobile or Compatibility.

---

<span id="class_Light3D_property_light_bake_mode"></span>

[BakeMode](class_light3d.md#enum_Light3D_BakeMode) **light_bake_mode** = `2` [🔗](class_light3d.md#class_Light3D_property_light_bake_mode)

- void **set_bake_mode** ( value: [BakeMode](class_light3d.md#enum_Light3D_BakeMode) )
- [BakeMode](class_light3d.md#enum_Light3D_BakeMode) **get_bake_mode** ( )

The light's bake mode. This will affect the global illumination techniques that have an effect on the light's rendering.

 **Note:** Meshes' global illumination mode will also affect the global illumination rendering. See [GeometryInstance3D.gi_mode](class_geometryinstance3d.md#class_GeometryInstance3D_property_gi_mode).

---

<span id="class_Light3D_property_light_color"></span>

[Color](class_color.md#class_Color) **light_color** = `Color(1, 1, 1, 1)` [🔗](class_light3d.md#class_Light3D_property_light_color)

- void **set_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_color** ( )

The light's color in nonlinear sRGB encoding. An *overbright* color can be used to achieve a result equivalent to increasing the light's [light_energy](class_light3d.md#class_Light3D_property_light_energy).

---

<span id="class_Light3D_property_light_cull_mask"></span>

[int](class_int.md#class_int) **light_cull_mask** = `4294967295` [🔗](class_light3d.md#class_Light3D_property_light_cull_mask)

- void **set_cull_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_cull_mask** ( )

The light will affect objects in the selected layers.

 **Note:** The light cull mask is ignored by [VoxelGI](class_voxelgi.md#class_VoxelGI), SDFGI, [LightmapGI](class_lightmapgi.md#class_LightmapGI), and volumetric fog. These will always render lights in a way that ignores the cull mask. See also [VisualInstance3D.layers](class_visualinstance3d.md#class_VisualInstance3D_property_layers).

---

<span id="class_Light3D_property_light_energy"></span>

[float](class_float.md#class_float) **light_energy** = `1.0` [🔗](class_light3d.md#class_Light3D_property_light_energy)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

The light's strength multiplier (this is not a physical unit). For [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) and [SpotLight3D](class_spotlight3d.md#class_SpotLight3D), changing this value will only change the light color's intensity, not the light's radius.

---

<span id="class_Light3D_property_light_indirect_energy"></span>

[float](class_float.md#class_float) **light_indirect_energy** = `1.0` [🔗](class_light3d.md#class_Light3D_property_light_indirect_energy)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

Secondary multiplier used with indirect light (light bounces). Used with [VoxelGI](class_voxelgi.md#class_VoxelGI) and SDFGI (see [Environment.sdfgi_enabled](class_environment.md#class_Environment_property_sdfgi_enabled)).

 **Note:** This property is ignored if [light_energy](class_light3d.md#class_Light3D_property_light_energy) is equal to `0.0`, as the light won't be present at all in the GI shader.

---

<span id="class_Light3D_property_light_intensity_lumens"></span>

[float](class_float.md#class_float) **light_intensity_lumens** [🔗](class_light3d.md#class_Light3D_property_light_intensity_lumens)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

Used by positional lights ([OmniLight3D](class_omnilight3d.md#class_OmniLight3D) and [SpotLight3D](class_spotlight3d.md#class_SpotLight3D)) when ProjectSettings.rendering/lights_and_shadows/use_physical_light_units is `true`. Sets the intensity of the light source measured in Lumens. Lumens are a measure of luminous flux, which is the total amount of visible light emitted by a light source per unit of time.

For [SpotLight3D](class_spotlight3d.md#class_SpotLight3D) s, we assume that the area outside the visible cone is surrounded by a perfect light absorbing material. Accordingly, the apparent brightness of the cone area does not change as the cone increases and decreases in size.

A typical household lightbulb can range from around 600 lumens to 1,200 lumens, a candle is about 13 lumens, while a streetlight can be approximately 60,000 lumens.

---

<span id="class_Light3D_property_light_intensity_lux"></span>

[float](class_float.md#class_float) **light_intensity_lux** [🔗](class_light3d.md#class_Light3D_property_light_intensity_lux)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

Used by [DirectionalLight3D](class_directionallight3d.md#class_DirectionalLight3D) s when ProjectSettings.rendering/lights_and_shadows/use_physical_light_units is `true`. Sets the intensity of the light source measured in Lux. Lux is a measure of luminous flux per unit area, it is equal to one lumen per square meter. Lux is the measure of how much light hits a surface at a given time.

On a clear sunny day a surface in direct sunlight may be approximately 100,000 lux, a typical room in a home may be approximately 50 lux, while the moonlit ground may be approximately 0.1 lux.

---

<span id="class_Light3D_property_light_negative"></span>

[bool](class_bool.md#class_bool) **light_negative** = `false` [🔗](class_light3d.md#class_Light3D_property_light_negative)

- void **set_negative** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_negative** ( )

If `true`, the light's effect is reversed, darkening areas and casting bright shadows.

---

<span id="class_Light3D_property_light_projector"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **light_projector** [🔗](class_light3d.md#class_Light3D_property_light_projector)

- void **set_projector** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_projector** ( )

[Texture2D](class_texture2d.md#class_Texture2D) projected by light. [shadow_enabled](class_light3d.md#class_Light3D_property_shadow_enabled) must be on for the projector to work. Light projectors make the light appear as if it is shining through a colored but transparent object, almost like light shining through stained-glass.

 **Note:** Unlike [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D) whose filter mode can be adjusted on a per-material basis, the filter mode for light projector textures is set globally with ProjectSettings.rendering/textures/light_projectors/filter.

 **Note:** Light projector textures are only supported in the Forward+ and Mobile rendering methods, not Compatibility.

---

<span id="class_Light3D_property_light_size"></span>

[float](class_float.md#class_float) **light_size** = `0.0` [🔗](class_light3d.md#class_Light3D_property_light_size)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

The size of the light in Godot units. Only available for [OmniLight3D](class_omnilight3d.md#class_OmniLight3D) s and [SpotLight3D](class_spotlight3d.md#class_SpotLight3D) s. Increasing this value will make the light fade out slower and shadows appear blurrier (also called percentage-closer soft shadows, or PCSS). This can be used to simulate area lights to an extent. Increasing this value above `0.0` for lights with shadows enabled will have a noticeable performance cost due to PCSS.

 **Note:** [light_size](class_light3d.md#class_Light3D_property_light_size) is not affected by [Node3D.scale](class_node3d.md#class_Node3D_property_scale) (the light's scale or its parent's scale).

 **Note:** PCSS for positional lights is only supported in the Forward+ and Mobile rendering methods, not Compatibility.

---

<span id="class_Light3D_property_light_specular"></span>

[float](class_float.md#class_float) **light_specular** = `1.0` [🔗](class_light3d.md#class_Light3D_property_light_specular)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

The intensity of the specular blob in objects affected by the light. At `0`, the light becomes a pure diffuse light. When not baking emission, this can be used to avoid unrealistic reflections when placing lights above an emissive surface.

---

<span id="class_Light3D_property_light_temperature"></span>

[float](class_float.md#class_float) **light_temperature** [🔗](class_light3d.md#class_Light3D_property_light_temperature)

- void **set_temperature** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_temperature** ( )

Sets the color temperature of the light source, measured in Kelvin. This is used to calculate a correlated color temperature which tints the [light_color](class_light3d.md#class_Light3D_property_light_color).

The sun on a cloudy day is approximately 6500 Kelvin, on a clear day it is between 5500 to 6000 Kelvin, and on a clear day at sunrise or sunset it ranges to around 1850 Kelvin.

---

<span id="class_Light3D_property_light_volumetric_fog_energy"></span>

[float](class_float.md#class_float) **light_volumetric_fog_energy** = `1.0` [🔗](class_light3d.md#class_Light3D_property_light_volumetric_fog_energy)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

Secondary multiplier multiplied with [light_energy](class_light3d.md#class_Light3D_property_light_energy) then used with the [Environment](class_environment.md#class_Environment)'s volumetric fog (if enabled). If set to `0.0`, computing volumetric fog will be skipped for this light, which can improve performance for large amounts of lights when volumetric fog is enabled.

 **Note:** To prevent short-lived dynamic light effects from poorly interacting with volumetric fog, lights used in those effects should have [light_volumetric_fog_energy](class_light3d.md#class_Light3D_property_light_volumetric_fog_energy) set to `0.0` unless [Environment.volumetric_fog_temporal_reprojection_enabled](class_environment.md#class_Environment_property_volumetric_fog_temporal_reprojection_enabled) is disabled (or unless the reprojection amount is significantly lowered).

---

<span id="class_Light3D_property_shadow_bias"></span>

[float](class_float.md#class_float) **shadow_bias** = `0.1` [🔗](class_light3d.md#class_Light3D_property_shadow_bias)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

Used to adjust shadow appearance. Too small a value results in self-shadowing ("shadow acne"), while too large a value causes shadows to separate from casters ("peter-panning"). Adjust as needed.

---

<span id="class_Light3D_property_shadow_blur"></span>

[float](class_float.md#class_float) **shadow_blur** = `1.0` [🔗](class_light3d.md#class_Light3D_property_shadow_blur)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

Blurs the edges of the shadow. Can be used to hide pixel artifacts in low-resolution shadow maps. A high value can impact performance, make shadows appear grainy and can cause other unwanted artifacts. Try to keep as near default as possible.

---

<span id="class_Light3D_property_shadow_caster_mask"></span>

[int](class_int.md#class_int) **shadow_caster_mask** = `4294967295` [🔗](class_light3d.md#class_Light3D_property_shadow_caster_mask)

- void **set_shadow_caster_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_shadow_caster_mask** ( )

The light will only cast shadows using objects in the selected layers.

---

<span id="class_Light3D_property_shadow_enabled"></span>

[bool](class_bool.md#class_bool) **shadow_enabled** = `false` [🔗](class_light3d.md#class_Light3D_property_shadow_enabled)

- void **set_shadow** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_shadow** ( )

If `true`, the light will cast real-time shadows. This has a significant performance cost. Only enable shadow rendering when it makes a noticeable difference in the scene's appearance, and consider using [distance_fade_enabled](class_light3d.md#class_Light3D_property_distance_fade_enabled) to hide the light when far away from the [Camera3D](class_camera3d.md#class_Camera3D).

---

<span id="class_Light3D_property_shadow_normal_bias"></span>

[float](class_float.md#class_float) **shadow_normal_bias** = `2.0` [🔗](class_light3d.md#class_Light3D_property_shadow_normal_bias)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

Offsets the lookup into the shadow map by the object's normal. This can be used to reduce self-shadowing artifacts without using [shadow_bias](class_light3d.md#class_Light3D_property_shadow_bias). In practice, this value should be tweaked along with [shadow_bias](class_light3d.md#class_Light3D_property_shadow_bias) to reduce artifacts as much as possible.

---

<span id="class_Light3D_property_shadow_opacity"></span>

[float](class_float.md#class_float) **shadow_opacity** = `1.0` [🔗](class_light3d.md#class_Light3D_property_shadow_opacity)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

The opacity to use when rendering the light's shadow map. Values lower than `1.0` make the light appear through shadows. This can be used to fake global illumination at a low performance cost.

---

<span id="class_Light3D_property_shadow_reverse_cull_face"></span>

[bool](class_bool.md#class_bool) **shadow_reverse_cull_face** = `false` [🔗](class_light3d.md#class_Light3D_property_shadow_reverse_cull_face)

- void **set_shadow_reverse_cull_face** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_shadow_reverse_cull_face** ( )

If `true`, reverses the backface culling of the mesh. This can be useful when you have a flat mesh that has a light behind it. If you need to cast a shadow on both sides of the mesh, set the mesh to use double-sided shadows with [GeometryInstance3D.SHADOW_CASTING_SETTING_DOUBLE_SIDED](class_geometryinstance3d.md#class_GeometryInstance3D_constant_SHADOW_CASTING_SETTING_DOUBLE_SIDED).

---

<span id="class_Light3D_property_shadow_transmittance_bias"></span>

[float](class_float.md#class_float) **shadow_transmittance_bias** = `0.05` [🔗](class_light3d.md#class_Light3D_property_shadow_transmittance_bias)

- void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

### Method Descriptions

<span id="class_Light3D_method_get_correlated_color"></span>

[Color](class_color.md#class_Color) **get_correlated_color** ( ) *const* [🔗](class_light3d.md#class_Light3D_method_get_correlated_color)

Returns the [Color](class_color.md#class_Color) of an idealized blackbody at the given [light_temperature](class_light3d.md#class_Light3D_property_light_temperature). This value is calculated internally based on the [light_temperature](class_light3d.md#class_Light3D_property_light_temperature). This [Color](class_color.md#class_Color) is multiplied by [light_color](class_light3d.md#class_Light3D_property_light_color) before being sent to the [RenderingServer](class_renderingserver.md#class_RenderingServer).

---

<span id="class_Light3D_method_get_param"></span>

[float](class_float.md#class_float) **get_param** ( param: [Param](class_light3d.md#enum_Light3D_Param) ) *const* [🔗](class_light3d.md#class_Light3D_method_get_param)

Returns the value of the specified [Param](class_light3d.md#enum_Light3D_Param) parameter.

---

<span id="class_Light3D_method_set_param"></span>

void **set_param** ( param: [Param](class_light3d.md#enum_Light3D_Param), value: [float](class_float.md#class_float) ) [🔗](class_light3d.md#class_Light3D_method_set_param)

Sets the value of the specified [Param](class_light3d.md#enum_Light3D_Param) parameter.
