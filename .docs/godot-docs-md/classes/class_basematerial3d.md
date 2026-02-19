<span id="class_BaseMaterial3D"></span>

## BaseMaterial3D

**Inherits:** [Material](class_material.md#class_Material) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [ORMMaterial3D](class_ormmaterial3d.md#class_ORMMaterial3D), [StandardMaterial3D](class_standardmaterial3d.md#class_StandardMaterial3D)

Abstract base class for defining the 3D rendering properties of meshes.

### Description

This class serves as a default material with a wide variety of rendering features and properties without the need to write shader code. See the tutorial below for details.

### Tutorials

- [Standard Material 3D and ORM Material 3D](../tutorials/3d/standard_material_3d.md)

### Properties


| [Color](class_color.md#class_Color) | [albedo_color](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_color) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Texture2D](class_texture2d.md#class_Texture2D) | [albedo_texture](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture) |
| [bool](class_bool.md#class_bool) | [albedo_texture_force_srgb](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture_force_srgb) | `false` |
| [bool](class_bool.md#class_bool) | [albedo_texture_msdf](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture_msdf) | `false` |
| [float](class_float.md#class_float) | [alpha_antialiasing_edge](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_antialiasing_edge) |
| [AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) | [alpha_antialiasing_mode](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_antialiasing_mode) |
| [float](class_float.md#class_float) | [alpha_hash_scale](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_hash_scale) |
| [float](class_float.md#class_float) | [alpha_scissor_threshold](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_scissor_threshold) |
| [float](class_float.md#class_float) | [anisotropy](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy) | `0.0` |
| [bool](class_bool.md#class_bool) | [anisotropy_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy_enabled) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [anisotropy_flowmap](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy_flowmap) |
| [bool](class_bool.md#class_bool) | [ao_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_ao_enabled) | `false` |
| [float](class_float.md#class_float) | [ao_light_affect](class_basematerial3d.md#class_BaseMaterial3D_property_ao_light_affect) | `0.0` |
| [bool](class_bool.md#class_bool) | [ao_on_uv2](class_basematerial3d.md#class_BaseMaterial3D_property_ao_on_uv2) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [ao_texture](class_basematerial3d.md#class_BaseMaterial3D_property_ao_texture) |
| [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) | [ao_texture_channel](class_basematerial3d.md#class_BaseMaterial3D_property_ao_texture_channel) | `0` |
| [Color](class_color.md#class_Color) | [backlight](class_basematerial3d.md#class_BaseMaterial3D_property_backlight) | `Color(0, 0, 0, 1)` |
| [bool](class_bool.md#class_bool) | [backlight_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_backlight_enabled) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [backlight_texture](class_basematerial3d.md#class_BaseMaterial3D_property_backlight_texture) |
| [bool](class_bool.md#class_bool) | [bent_normal_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_bent_normal_enabled) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [bent_normal_texture](class_basematerial3d.md#class_BaseMaterial3D_property_bent_normal_texture) |
| [bool](class_bool.md#class_bool) | [billboard_keep_scale](class_basematerial3d.md#class_BaseMaterial3D_property_billboard_keep_scale) | `false` |
| [BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) | [billboard_mode](class_basematerial3d.md#class_BaseMaterial3D_property_billboard_mode) | `0` |
| [BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) | [blend_mode](class_basematerial3d.md#class_BaseMaterial3D_property_blend_mode) | `0` |
| [float](class_float.md#class_float) | [clearcoat](class_basematerial3d.md#class_BaseMaterial3D_property_clearcoat) | `1.0` |
| [bool](class_bool.md#class_bool) | [clearcoat_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_clearcoat_enabled) | `false` |
| [float](class_float.md#class_float) | [clearcoat_roughness](class_basematerial3d.md#class_BaseMaterial3D_property_clearcoat_roughness) | `0.5` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [clearcoat_texture](class_basematerial3d.md#class_BaseMaterial3D_property_clearcoat_texture) |
| [CullMode](class_basematerial3d.md#enum_BaseMaterial3D_CullMode) | [cull_mode](class_basematerial3d.md#class_BaseMaterial3D_property_cull_mode) | `0` |
| [DepthDrawMode](class_basematerial3d.md#enum_BaseMaterial3D_DepthDrawMode) | [depth_draw_mode](class_basematerial3d.md#class_BaseMaterial3D_property_depth_draw_mode) | `0` |
| [DepthTest](class_basematerial3d.md#enum_BaseMaterial3D_DepthTest) | [depth_test](class_basematerial3d.md#class_BaseMaterial3D_property_depth_test) | `0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo) |
| [BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) | [detail_blend_mode](class_basematerial3d.md#class_BaseMaterial3D_property_detail_blend_mode) | `0` |
| [bool](class_bool.md#class_bool) | [detail_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_detail_enabled) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [detail_mask](class_basematerial3d.md#class_BaseMaterial3D_property_detail_mask) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [detail_normal](class_basematerial3d.md#class_BaseMaterial3D_property_detail_normal) |
| [DetailUV](class_basematerial3d.md#enum_BaseMaterial3D_DetailUV) | [detail_uv_layer](class_basematerial3d.md#class_BaseMaterial3D_property_detail_uv_layer) | `0` |
| [DiffuseMode](class_basematerial3d.md#enum_BaseMaterial3D_DiffuseMode) | [diffuse_mode](class_basematerial3d.md#class_BaseMaterial3D_property_diffuse_mode) | `0` |
| [bool](class_bool.md#class_bool) | [disable_ambient_light](class_basematerial3d.md#class_BaseMaterial3D_property_disable_ambient_light) | `false` |
| [bool](class_bool.md#class_bool) | [disable_fog](class_basematerial3d.md#class_BaseMaterial3D_property_disable_fog) | `false` |
| [bool](class_bool.md#class_bool) | [disable_receive_shadows](class_basematerial3d.md#class_BaseMaterial3D_property_disable_receive_shadows) | `false` |
| [bool](class_bool.md#class_bool) | [disable_specular_occlusion](class_basematerial3d.md#class_BaseMaterial3D_property_disable_specular_occlusion) | `false` |
| [float](class_float.md#class_float) | [distance_fade_max_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_max_distance) | `10.0` |
| [float](class_float.md#class_float) | [distance_fade_min_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_min_distance) | `0.0` |
| [DistanceFadeMode](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode) | [distance_fade_mode](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_mode) | `0` |
| [Color](class_color.md#class_Color) | [emission](class_basematerial3d.md#class_BaseMaterial3D_property_emission) | `Color(0, 0, 0, 1)` |
| [bool](class_bool.md#class_bool) | [emission_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_emission_enabled) | `false` |
| [float](class_float.md#class_float) | [emission_energy_multiplier](class_basematerial3d.md#class_BaseMaterial3D_property_emission_energy_multiplier) | `1.0` |
| [float](class_float.md#class_float) | [emission_intensity](class_basematerial3d.md#class_BaseMaterial3D_property_emission_intensity) |
| [bool](class_bool.md#class_bool) | [emission_on_uv2](class_basematerial3d.md#class_BaseMaterial3D_property_emission_on_uv2) | `false` |
| [EmissionOperator](class_basematerial3d.md#enum_BaseMaterial3D_EmissionOperator) | [emission_operator](class_basematerial3d.md#class_BaseMaterial3D_property_emission_operator) | `0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [emission_texture](class_basematerial3d.md#class_BaseMaterial3D_property_emission_texture) |
| [bool](class_bool.md#class_bool) | [fixed_size](class_basematerial3d.md#class_BaseMaterial3D_property_fixed_size) | `false` |
| [float](class_float.md#class_float) | [fov_override](class_basematerial3d.md#class_BaseMaterial3D_property_fov_override) | `75.0` |
| [bool](class_bool.md#class_bool) | [grow](class_basematerial3d.md#class_BaseMaterial3D_property_grow) | `false` |
| [float](class_float.md#class_float) | [grow_amount](class_basematerial3d.md#class_BaseMaterial3D_property_grow_amount) | `0.0` |
| [bool](class_bool.md#class_bool) | [heightmap_deep_parallax](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_deep_parallax) | `false` |
| [bool](class_bool.md#class_bool) | [heightmap_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [heightmap_flip_binormal](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_binormal) | `false` |
| [bool](class_bool.md#class_bool) | [heightmap_flip_tangent](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_tangent) | `false` |
| [bool](class_bool.md#class_bool) | [heightmap_flip_texture](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_texture) | `false` |
| [int](class_int.md#class_int) | [heightmap_max_layers](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_max_layers) |
| [int](class_int.md#class_int) | [heightmap_min_layers](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_min_layers) |
| [float](class_float.md#class_float) | [heightmap_scale](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_scale) | `5.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [heightmap_texture](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_texture) |
| [float](class_float.md#class_float) | [metallic](class_basematerial3d.md#class_BaseMaterial3D_property_metallic) | `0.0` |
| [float](class_float.md#class_float) | [metallic_specular](class_basematerial3d.md#class_BaseMaterial3D_property_metallic_specular) | `0.5` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [metallic_texture](class_basematerial3d.md#class_BaseMaterial3D_property_metallic_texture) |
| [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) | [metallic_texture_channel](class_basematerial3d.md#class_BaseMaterial3D_property_metallic_texture_channel) | `0` |
| [float](class_float.md#class_float) | [msdf_outline_size](class_basematerial3d.md#class_BaseMaterial3D_property_msdf_outline_size) | `0.0` |
| [float](class_float.md#class_float) | [msdf_pixel_range](class_basematerial3d.md#class_BaseMaterial3D_property_msdf_pixel_range) | `4.0` |
| [bool](class_bool.md#class_bool) | [no_depth_test](class_basematerial3d.md#class_BaseMaterial3D_property_no_depth_test) | `false` |
| [bool](class_bool.md#class_bool) | [normal_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_normal_enabled) | `false` |
| [float](class_float.md#class_float) | [normal_scale](class_basematerial3d.md#class_BaseMaterial3D_property_normal_scale) | `1.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [normal_texture](class_basematerial3d.md#class_BaseMaterial3D_property_normal_texture) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [orm_texture](class_basematerial3d.md#class_BaseMaterial3D_property_orm_texture) |
| [int](class_int.md#class_int) | [particles_anim_h_frames](class_basematerial3d.md#class_BaseMaterial3D_property_particles_anim_h_frames) |
| [bool](class_bool.md#class_bool) | [particles_anim_loop](class_basematerial3d.md#class_BaseMaterial3D_property_particles_anim_loop) |
| [int](class_int.md#class_int) | [particles_anim_v_frames](class_basematerial3d.md#class_BaseMaterial3D_property_particles_anim_v_frames) |
| [float](class_float.md#class_float) | [point_size](class_basematerial3d.md#class_BaseMaterial3D_property_point_size) | `1.0` |
| [float](class_float.md#class_float) | [proximity_fade_distance](class_basematerial3d.md#class_BaseMaterial3D_property_proximity_fade_distance) | `1.0` |
| [bool](class_bool.md#class_bool) | [proximity_fade_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_proximity_fade_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [refraction_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_enabled) | `false` |
| [float](class_float.md#class_float) | [refraction_scale](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_scale) | `0.05` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [refraction_texture](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_texture) |
| [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) | [refraction_texture_channel](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_texture_channel) | `0` |
| [float](class_float.md#class_float) | [rim](class_basematerial3d.md#class_BaseMaterial3D_property_rim) | `1.0` |
| [bool](class_bool.md#class_bool) | [rim_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_rim_enabled) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [rim_texture](class_basematerial3d.md#class_BaseMaterial3D_property_rim_texture) |
| [float](class_float.md#class_float) | [rim_tint](class_basematerial3d.md#class_BaseMaterial3D_property_rim_tint) | `0.5` |
| [float](class_float.md#class_float) | [roughness](class_basematerial3d.md#class_BaseMaterial3D_property_roughness) | `1.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [roughness_texture](class_basematerial3d.md#class_BaseMaterial3D_property_roughness_texture) |
| [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) | [roughness_texture_channel](class_basematerial3d.md#class_BaseMaterial3D_property_roughness_texture_channel) | `0` |
| [ShadingMode](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode) | [shading_mode](class_basematerial3d.md#class_BaseMaterial3D_property_shading_mode) | `1` |
| [bool](class_bool.md#class_bool) | [shadow_to_opacity](class_basematerial3d.md#class_BaseMaterial3D_property_shadow_to_opacity) | `false` |
| [SpecularMode](class_basematerial3d.md#enum_BaseMaterial3D_SpecularMode) | [specular_mode](class_basematerial3d.md#class_BaseMaterial3D_property_specular_mode) | `0` |
| [Color](class_color.md#class_Color) | [stencil_color](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_color) | `Color(0, 0, 0, 1)` |
| [StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) | [stencil_compare](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_compare) | `0` |
| [int](class_int.md#class_int) | [stencil_flags](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_flags) | `0` |
| [StencilMode](class_basematerial3d.md#enum_BaseMaterial3D_StencilMode) | [stencil_mode](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_mode) | `0` |
| [float](class_float.md#class_float) | [stencil_outline_thickness](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_outline_thickness) | `0.01` |
| [int](class_int.md#class_int) | [stencil_reference](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_reference) | `1` |
| [bool](class_bool.md#class_bool) | [subsurf_scatter_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_enabled) | `false` |
| [bool](class_bool.md#class_bool) | [subsurf_scatter_skin_mode](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_skin_mode) | `false` |
| [float](class_float.md#class_float) | [subsurf_scatter_strength](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_strength) | `0.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [subsurf_scatter_texture](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_texture) |
| [float](class_float.md#class_float) | [subsurf_scatter_transmittance_boost](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_boost) | `0.0` |
| [Color](class_color.md#class_Color) | [subsurf_scatter_transmittance_color](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_color) | `Color(1, 1, 1, 1)` |
| [float](class_float.md#class_float) | [subsurf_scatter_transmittance_depth](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_depth) | `0.1` |
| [bool](class_bool.md#class_bool) | [subsurf_scatter_transmittance_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_enabled) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [subsurf_scatter_transmittance_texture](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_texture) |
| [TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) | [texture_filter](class_basematerial3d.md#class_BaseMaterial3D_property_texture_filter) | `3` |
| [bool](class_bool.md#class_bool) | [texture_repeat](class_basematerial3d.md#class_BaseMaterial3D_property_texture_repeat) | `true` |
| [Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) | [transparency](class_basematerial3d.md#class_BaseMaterial3D_property_transparency) | `0` |
| [bool](class_bool.md#class_bool) | [use_fov_override](class_basematerial3d.md#class_BaseMaterial3D_property_use_fov_override) | `false` |
| [bool](class_bool.md#class_bool) | [use_particle_trails](class_basematerial3d.md#class_BaseMaterial3D_property_use_particle_trails) | `false` |
| [bool](class_bool.md#class_bool) | [use_point_size](class_basematerial3d.md#class_BaseMaterial3D_property_use_point_size) | `false` |
| [bool](class_bool.md#class_bool) | [use_z_clip_scale](class_basematerial3d.md#class_BaseMaterial3D_property_use_z_clip_scale) | `false` |
| [Vector3](class_vector3.md#class_Vector3) | [uv1_offset](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_offset) | `Vector3(0, 0, 0)` |
| [Vector3](class_vector3.md#class_Vector3) | [uv1_scale](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_scale) | `Vector3(1, 1, 1)` |
| [bool](class_bool.md#class_bool) | [uv1_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_triplanar) | `false` |
| [float](class_float.md#class_float) | [uv1_triplanar_sharpness](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_triplanar_sharpness) | `1.0` |
| [bool](class_bool.md#class_bool) | [uv1_world_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_world_triplanar) | `false` |
| [Vector3](class_vector3.md#class_Vector3) | [uv2_offset](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_offset) | `Vector3(0, 0, 0)` |
| [Vector3](class_vector3.md#class_Vector3) | [uv2_scale](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_scale) | `Vector3(1, 1, 1)` |
| [bool](class_bool.md#class_bool) | [uv2_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_triplanar) | `false` |
| [float](class_float.md#class_float) | [uv2_triplanar_sharpness](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_triplanar_sharpness) | `1.0` |
| [bool](class_bool.md#class_bool) | [uv2_world_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_world_triplanar) | `false` |
| [bool](class_bool.md#class_bool) | [vertex_color_is_srgb](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_is_srgb) | `false` |
| [bool](class_bool.md#class_bool) | [vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) | `false` |
| [float](class_float.md#class_float) | [z_clip_scale](class_basematerial3d.md#class_BaseMaterial3D_property_z_clip_scale) | `1.0` |

### Methods


| [bool](class_bool.md#class_bool) | [get_feature](class_basematerial3d.md#class_BaseMaterial3D_method_get_feature) ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [get_flag](class_basematerial3d.md#class_BaseMaterial3D_method_get_flag) ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_texture](class_basematerial3d.md#class_BaseMaterial3D_method_get_texture) ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) const |
| void | [set_feature](class_basematerial3d.md#class_BaseMaterial3D_method_set_feature) ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_flag](class_basematerial3d.md#class_BaseMaterial3D_method_set_flag) ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) ) |
| void | [set_texture](class_basematerial3d.md#class_BaseMaterial3D_method_set_texture) ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |

---

### Enumerations

<span id="enum_BaseMaterial3D_TextureParam"></span>

enum **TextureParam**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam)

<span id="class_BaseMaterial3D_constant_TEXTURE_ALBEDO"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_ALBEDO** = `0`

Texture specifying per-pixel color.

<span id="class_BaseMaterial3D_constant_TEXTURE_METALLIC"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_METALLIC** = `1`

Texture specifying per-pixel metallic value.

<span id="class_BaseMaterial3D_constant_TEXTURE_ROUGHNESS"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_ROUGHNESS** = `2`

Texture specifying per-pixel roughness value.

<span id="class_BaseMaterial3D_constant_TEXTURE_EMISSION"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_EMISSION** = `3`

Texture specifying per-pixel emission color.

<span id="class_BaseMaterial3D_constant_TEXTURE_NORMAL"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_NORMAL** = `4`

Texture specifying per-pixel normal vector.

<span id="class_BaseMaterial3D_constant_TEXTURE_BENT_NORMAL"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_BENT_NORMAL** = `18`

Texture specifying per-pixel bent normal vector.

<span id="class_BaseMaterial3D_constant_TEXTURE_RIM"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_RIM** = `5`

Texture specifying per-pixel rim value.

<span id="class_BaseMaterial3D_constant_TEXTURE_CLEARCOAT"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_CLEARCOAT** = `6`

Texture specifying per-pixel clearcoat value.

<span id="class_BaseMaterial3D_constant_TEXTURE_FLOWMAP"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_FLOWMAP** = `7`

Texture specifying per-pixel flowmap direction for use with [anisotropy](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy).

<span id="class_BaseMaterial3D_constant_TEXTURE_AMBIENT_OCCLUSION"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_AMBIENT_OCCLUSION** = `8`

Texture specifying per-pixel ambient occlusion value.

<span id="class_BaseMaterial3D_constant_TEXTURE_HEIGHTMAP"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_HEIGHTMAP** = `9`

Texture specifying per-pixel height.

<span id="class_BaseMaterial3D_constant_TEXTURE_SUBSURFACE_SCATTERING"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_SUBSURFACE_SCATTERING** = `10`

Texture specifying per-pixel subsurface scattering.

<span id="class_BaseMaterial3D_constant_TEXTURE_SUBSURFACE_TRANSMITTANCE"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_SUBSURFACE_TRANSMITTANCE** = `11`

Texture specifying per-pixel transmittance for subsurface scattering.

<span id="class_BaseMaterial3D_constant_TEXTURE_BACKLIGHT"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_BACKLIGHT** = `12`

Texture specifying per-pixel backlight color.

<span id="class_BaseMaterial3D_constant_TEXTURE_REFRACTION"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_REFRACTION** = `13`

Texture specifying per-pixel refraction strength.

<span id="class_BaseMaterial3D_constant_TEXTURE_DETAIL_MASK"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_DETAIL_MASK** = `14`

Texture specifying per-pixel detail mask blending value.

<span id="class_BaseMaterial3D_constant_TEXTURE_DETAIL_ALBEDO"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_DETAIL_ALBEDO** = `15`

Texture specifying per-pixel detail color.

<span id="class_BaseMaterial3D_constant_TEXTURE_DETAIL_NORMAL"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_DETAIL_NORMAL** = `16`

Texture specifying per-pixel detail normal.

<span id="class_BaseMaterial3D_constant_TEXTURE_ORM"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_ORM** = `17`

Texture holding ambient occlusion, roughness, and metallic.

<span id="class_BaseMaterial3D_constant_TEXTURE_MAX"></span>

[TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) **TEXTURE_MAX** = `19`

Represents the size of the [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) enum.

---

<span id="enum_BaseMaterial3D_TextureFilter"></span>

enum **TextureFilter**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter)

<span id="class_BaseMaterial3D_constant_TEXTURE_FILTER_NEAREST"></span>

[TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **TEXTURE_FILTER_NEAREST** = `0`

The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).

<span id="class_BaseMaterial3D_constant_TEXTURE_FILTER_LINEAR"></span>

[TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **TEXTURE_FILTER_LINEAR** = `1`

The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).

<span id="class_BaseMaterial3D_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS"></span>

[TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **TEXTURE_FILTER_NEAREST_WITH_MIPMAPS** = `2`

The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`). This makes the texture look pixelated from up close, and smooth from a distance.

<span id="class_BaseMaterial3D_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS"></span>

[TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **TEXTURE_FILTER_LINEAR_WITH_MIPMAPS** = `3`

The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`). This makes the texture look smooth from up close, and smooth from a distance.

<span id="class_BaseMaterial3D_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC"></span>

[TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC** = `4`

The texture filter reads from the nearest pixel and blends between 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`) based on the angle between the surface and the camera view. This makes the texture look pixelated from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

<span id="class_BaseMaterial3D_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC"></span>

[TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC** = `5`

The texture filter blends between the nearest 4 pixels and blends between 2 mipmaps (or uses the nearest mipmap if ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter is `true`) based on the angle between the surface and the camera view. This makes the texture look smooth from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjusting ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.

<span id="class_BaseMaterial3D_constant_TEXTURE_FILTER_MAX"></span>

[TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **TEXTURE_FILTER_MAX** = `6`

Represents the size of the [TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) enum.

---

<span id="enum_BaseMaterial3D_DetailUV"></span>

enum **DetailUV**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_DetailUV)

<span id="class_BaseMaterial3D_constant_DETAIL_UV_1"></span>

[DetailUV](class_basematerial3d.md#enum_BaseMaterial3D_DetailUV) **DETAIL_UV_1** = `0`

Use `UV` with the detail texture.

<span id="class_BaseMaterial3D_constant_DETAIL_UV_2"></span>

[DetailUV](class_basematerial3d.md#enum_BaseMaterial3D_DetailUV) **DETAIL_UV_2** = `1`

Use `UV2` with the detail texture.

---

<span id="enum_BaseMaterial3D_Transparency"></span>

enum **Transparency**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_Transparency)

<span id="class_BaseMaterial3D_constant_TRANSPARENCY_DISABLED"></span>

[Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) **TRANSPARENCY_DISABLED** = `0`

The material will not use transparency. This is the fastest to render.

<span id="class_BaseMaterial3D_constant_TRANSPARENCY_ALPHA"></span>

[Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) **TRANSPARENCY_ALPHA** = `1`

The material will use the texture's alpha values for transparency. This is the slowest to render, and disables shadow casting.

<span id="class_BaseMaterial3D_constant_TRANSPARENCY_ALPHA_SCISSOR"></span>

[Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) **TRANSPARENCY_ALPHA_SCISSOR** = `2`

The material will cut off all values below a threshold, the rest will remain opaque. The opaque portions will be rendered in the depth prepass. This is faster to render than alpha blending, but slower than opaque rendering. This also supports casting shadows.

<span id="class_BaseMaterial3D_constant_TRANSPARENCY_ALPHA_HASH"></span>

[Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) **TRANSPARENCY_ALPHA_HASH** = `3`

The material will cut off all values below a spatially-deterministic threshold, the rest will remain opaque. This is faster to render than alpha blending, but slower than opaque rendering. This also supports casting shadows. Alpha hashing is suited for hair rendering.

<span id="class_BaseMaterial3D_constant_TRANSPARENCY_ALPHA_DEPTH_PRE_PASS"></span>

[Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) **TRANSPARENCY_ALPHA_DEPTH_PRE_PASS** = `4`

The material will use the texture's alpha value for transparency, but will discard fragments with an alpha of less than 0.99 during the depth prepass and fragments with an alpha less than 0.1 during the shadow pass. This also supports casting shadows.

<span id="class_BaseMaterial3D_constant_TRANSPARENCY_MAX"></span>

[Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) **TRANSPARENCY_MAX** = `5`

Represents the size of the [Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) enum.

---

<span id="enum_BaseMaterial3D_ShadingMode"></span>

enum **ShadingMode**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode)

<span id="class_BaseMaterial3D_constant_SHADING_MODE_UNSHADED"></span>

[ShadingMode](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode) **SHADING_MODE_UNSHADED** = `0`

The object will not receive shadows. This is the fastest to render, but it disables all interactions with lights.

<span id="class_BaseMaterial3D_constant_SHADING_MODE_PER_PIXEL"></span>

[ShadingMode](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode) **SHADING_MODE_PER_PIXEL** = `1`

The object will be shaded per pixel. Useful for realistic shading effects.

<span id="class_BaseMaterial3D_constant_SHADING_MODE_PER_VERTEX"></span>

[ShadingMode](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode) **SHADING_MODE_PER_VERTEX** = `2`

The object will be shaded per vertex. Useful when you want cheaper shaders and do not care about visual quality.

<span id="class_BaseMaterial3D_constant_SHADING_MODE_MAX"></span>

[ShadingMode](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode) **SHADING_MODE_MAX** = `3`

Represents the size of the [ShadingMode](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode) enum.

---

<span id="enum_BaseMaterial3D_Feature"></span>

enum **Feature**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_Feature)

<span id="class_BaseMaterial3D_constant_FEATURE_EMISSION"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_EMISSION** = `0`

Constant for setting [emission_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_emission_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_NORMAL_MAPPING"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_NORMAL_MAPPING** = `1`

Constant for setting [normal_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_normal_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_RIM"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_RIM** = `2`

Constant for setting [rim_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_rim_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_CLEARCOAT"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_CLEARCOAT** = `3`

Constant for setting [clearcoat_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_clearcoat_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_ANISOTROPY"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_ANISOTROPY** = `4`

Constant for setting [anisotropy_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_AMBIENT_OCCLUSION"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_AMBIENT_OCCLUSION** = `5`

Constant for setting [ao_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_ao_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_HEIGHT_MAPPING"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_HEIGHT_MAPPING** = `6`

Constant for setting [heightmap_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_SUBSURFACE_SCATTERING"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_SUBSURFACE_SCATTERING** = `7`

Constant for setting [subsurf_scatter_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_SUBSURFACE_TRANSMITTANCE"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_SUBSURFACE_TRANSMITTANCE** = `8`

Constant for setting [subsurf_scatter_transmittance_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_BACKLIGHT"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_BACKLIGHT** = `9`

Constant for setting [backlight_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_backlight_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_REFRACTION"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_REFRACTION** = `10`

Constant for setting [refraction_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_DETAIL"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_DETAIL** = `11`

Constant for setting [detail_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_detail_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_BENT_NORMAL_MAPPING"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_BENT_NORMAL_MAPPING** = `12`

Constant for setting [bent_normal_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_bent_normal_enabled).

<span id="class_BaseMaterial3D_constant_FEATURE_MAX"></span>

[Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) **FEATURE_MAX** = `13`

Represents the size of the [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) enum.

---

<span id="enum_BaseMaterial3D_BlendMode"></span>

enum **BlendMode**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode)

<span id="class_BaseMaterial3D_constant_BLEND_MODE_MIX"></span>

[BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) **BLEND_MODE_MIX** = `0`

Default blend mode. The color of the object is blended over the background based on the object's alpha value.

<span id="class_BaseMaterial3D_constant_BLEND_MODE_ADD"></span>

[BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) **BLEND_MODE_ADD** = `1`

The color of the object is added to the background.

<span id="class_BaseMaterial3D_constant_BLEND_MODE_SUB"></span>

[BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) **BLEND_MODE_SUB** = `2`

The color of the object is subtracted from the background.

<span id="class_BaseMaterial3D_constant_BLEND_MODE_MUL"></span>

[BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) **BLEND_MODE_MUL** = `3`

The color of the object is multiplied by the background.

<span id="class_BaseMaterial3D_constant_BLEND_MODE_PREMULT_ALPHA"></span>

[BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) **BLEND_MODE_PREMULT_ALPHA** = `4`

The color of the object is added to the background and the alpha channel is used to mask out the background. This is effectively a hybrid of the blend mix and add modes, useful for effects like fire where you want the flame to add but the smoke to mix. By default, this works with unshaded materials using premultiplied textures. For shaded materials, use the `PREMUL_ALPHA_FACTOR` built-in so that lighting can be modulated as well.

---

<span id="enum_BaseMaterial3D_AlphaAntiAliasing"></span>

enum **AlphaAntiAliasing**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing)

<span id="class_BaseMaterial3D_constant_ALPHA_ANTIALIASING_OFF"></span>

[AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) **ALPHA_ANTIALIASING_OFF** = `0`

Disables Alpha AntiAliasing for the material.

<span id="class_BaseMaterial3D_constant_ALPHA_ANTIALIASING_ALPHA_TO_COVERAGE"></span>

[AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) **ALPHA_ANTIALIASING_ALPHA_TO_COVERAGE** = `1`

Enables AlphaToCoverage. Alpha values in the material are passed to the AntiAliasing sample mask.

<span id="class_BaseMaterial3D_constant_ALPHA_ANTIALIASING_ALPHA_TO_COVERAGE_AND_TO_ONE"></span>

[AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) **ALPHA_ANTIALIASING_ALPHA_TO_COVERAGE_AND_TO_ONE** = `2`

Enables AlphaToCoverage and forces all non-zero alpha values to `1`. Alpha values in the material are passed to the AntiAliasing sample mask.

---

<span id="enum_BaseMaterial3D_DepthDrawMode"></span>

enum **DepthDrawMode**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_DepthDrawMode)

<span id="class_BaseMaterial3D_constant_DEPTH_DRAW_OPAQUE_ONLY"></span>

[DepthDrawMode](class_basematerial3d.md#enum_BaseMaterial3D_DepthDrawMode) **DEPTH_DRAW_OPAQUE_ONLY** = `0`

Default depth draw mode. Depth is drawn only for opaque objects during the opaque prepass (if any) and during the opaque pass.

<span id="class_BaseMaterial3D_constant_DEPTH_DRAW_ALWAYS"></span>

[DepthDrawMode](class_basematerial3d.md#enum_BaseMaterial3D_DepthDrawMode) **DEPTH_DRAW_ALWAYS** = `1`

Objects will write to depth during the opaque and the transparent passes. Transparent objects that are close to the camera may obscure other transparent objects behind them.

 **Note:** This does not influence whether transparent objects are included in the depth prepass or not. For that, see [Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency).

<span id="class_BaseMaterial3D_constant_DEPTH_DRAW_DISABLED"></span>

[DepthDrawMode](class_basematerial3d.md#enum_BaseMaterial3D_DepthDrawMode) **DEPTH_DRAW_DISABLED** = `2`

Objects will not write their depth to the depth buffer, even during the depth prepass (if enabled).

---

<span id="enum_BaseMaterial3D_DepthTest"></span>

enum **DepthTest**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_DepthTest)

<span id="class_BaseMaterial3D_constant_DEPTH_TEST_DEFAULT"></span>

[DepthTest](class_basematerial3d.md#enum_BaseMaterial3D_DepthTest) **DEPTH_TEST_DEFAULT** = `0`

Depth test will discard the pixel if it is behind other pixels.

<span id="class_BaseMaterial3D_constant_DEPTH_TEST_INVERTED"></span>

[DepthTest](class_basematerial3d.md#enum_BaseMaterial3D_DepthTest) **DEPTH_TEST_INVERTED** = `1`

Depth test will discard the pixel if it is in front of other pixels. Useful for stencil effects.

---

<span id="enum_BaseMaterial3D_CullMode"></span>

enum **CullMode**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_CullMode)

<span id="class_BaseMaterial3D_constant_CULL_BACK"></span>

[CullMode](class_basematerial3d.md#enum_BaseMaterial3D_CullMode) **CULL_BACK** = `0`

Default cull mode. The back of the object is culled when not visible. Back face triangles will be culled when facing the camera. This results in only the front side of triangles being drawn. For closed-surface meshes, this means that only the exterior of the mesh will be visible.

<span id="class_BaseMaterial3D_constant_CULL_FRONT"></span>

[CullMode](class_basematerial3d.md#enum_BaseMaterial3D_CullMode) **CULL_FRONT** = `1`

Front face triangles will be culled when facing the camera. This results in only the back side of triangles being drawn. For closed-surface meshes, this means that the interior of the mesh will be drawn instead of the exterior.

<span id="class_BaseMaterial3D_constant_CULL_DISABLED"></span>

[CullMode](class_basematerial3d.md#enum_BaseMaterial3D_CullMode) **CULL_DISABLED** = `2`

No face culling is performed; both the front face and back face will be visible.

---

<span id="enum_BaseMaterial3D_Flags"></span>

enum **Flags**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_Flags)

<span id="class_BaseMaterial3D_constant_FLAG_DISABLE_DEPTH_TEST"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_DISABLE_DEPTH_TEST** = `0`

Disables the depth test, so this object is drawn on top of all others drawn before it. This puts the object in the transparent draw pass where it is sorted based on distance to camera. Objects drawn after it in the draw order may cover it. This also disables writing to depth.

<span id="class_BaseMaterial3D_constant_FLAG_ALBEDO_FROM_VERTEX_COLOR"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_ALBEDO_FROM_VERTEX_COLOR** = `1`

Set `ALBEDO` to the per-vertex color specified in the mesh.

<span id="class_BaseMaterial3D_constant_FLAG_SRGB_VERTEX_COLOR"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_SRGB_VERTEX_COLOR** = `2`

Vertex colors are considered to be stored in nonlinear sRGB encoding and are converted to linear encoding during rendering. See also [vertex_color_is_srgb](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_is_srgb).

 **Note:** Only effective when using the Forward+ and Mobile rendering methods.

<span id="class_BaseMaterial3D_constant_FLAG_USE_POINT_SIZE"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_USE_POINT_SIZE** = `3`

Uses point size to alter the size of primitive points. Also changes the albedo texture lookup to use `POINT_COORD` instead of `UV`.

<span id="class_BaseMaterial3D_constant_FLAG_FIXED_SIZE"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_FIXED_SIZE** = `4`

Object is scaled by depth so that it always appears the same size on screen.

<span id="class_BaseMaterial3D_constant_FLAG_BILLBOARD_KEEP_SCALE"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_BILLBOARD_KEEP_SCALE** = `5`

Shader will keep the scale set for the mesh. Otherwise the scale is lost when billboarding. Only applies when [billboard_mode](class_basematerial3d.md#class_BaseMaterial3D_property_billboard_mode) is [BILLBOARD_ENABLED](class_basematerial3d.md#class_BaseMaterial3D_constant_BILLBOARD_ENABLED).

<span id="class_BaseMaterial3D_constant_FLAG_UV1_USE_TRIPLANAR"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_UV1_USE_TRIPLANAR** = `6`

Use triplanar texture lookup for all texture lookups that would normally use `UV`.

<span id="class_BaseMaterial3D_constant_FLAG_UV2_USE_TRIPLANAR"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_UV2_USE_TRIPLANAR** = `7`

Use triplanar texture lookup for all texture lookups that would normally use `UV2`.

<span id="class_BaseMaterial3D_constant_FLAG_UV1_USE_WORLD_TRIPLANAR"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_UV1_USE_WORLD_TRIPLANAR** = `8`

Use triplanar texture lookup for all texture lookups that would normally use `UV`.

<span id="class_BaseMaterial3D_constant_FLAG_UV2_USE_WORLD_TRIPLANAR"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_UV2_USE_WORLD_TRIPLANAR** = `9`

Use triplanar texture lookup for all texture lookups that would normally use `UV2`.

<span id="class_BaseMaterial3D_constant_FLAG_AO_ON_UV2"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_AO_ON_UV2** = `10`

Use `UV2` coordinates to look up from the [ao_texture](class_basematerial3d.md#class_BaseMaterial3D_property_ao_texture).

<span id="class_BaseMaterial3D_constant_FLAG_EMISSION_ON_UV2"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_EMISSION_ON_UV2** = `11`

Use `UV2` coordinates to look up from the [emission_texture](class_basematerial3d.md#class_BaseMaterial3D_property_emission_texture).

<span id="class_BaseMaterial3D_constant_FLAG_ALBEDO_TEXTURE_FORCE_SRGB"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_ALBEDO_TEXTURE_FORCE_SRGB** = `12`

Forces the shader to convert albedo from nonlinear sRGB encoding to linear encoding. See also [albedo_texture_force_srgb](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture_force_srgb).

<span id="class_BaseMaterial3D_constant_FLAG_DONT_RECEIVE_SHADOWS"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_DONT_RECEIVE_SHADOWS** = `13`

Disables receiving shadows from other objects.

<span id="class_BaseMaterial3D_constant_FLAG_DISABLE_AMBIENT_LIGHT"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_DISABLE_AMBIENT_LIGHT** = `14`

Disables receiving ambient light.

<span id="class_BaseMaterial3D_constant_FLAG_USE_SHADOW_TO_OPACITY"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_USE_SHADOW_TO_OPACITY** = `15`

Enables the shadow to opacity feature.

<span id="class_BaseMaterial3D_constant_FLAG_USE_TEXTURE_REPEAT"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_USE_TEXTURE_REPEAT** = `16`

Enables the texture to repeat when UV coordinates are outside the 0-1 range. If using one of the linear filtering modes, this can result in artifacts at the edges of a texture when the sampler filters across the edges of the texture.

<span id="class_BaseMaterial3D_constant_FLAG_INVERT_HEIGHTMAP"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_INVERT_HEIGHTMAP** = `17`

Invert values read from a depth texture to convert them to height values (heightmap).

<span id="class_BaseMaterial3D_constant_FLAG_SUBSURFACE_MODE_SKIN"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_SUBSURFACE_MODE_SKIN** = `18`

Enables the skin mode for subsurface scattering which is used to improve the look of subsurface scattering when used for human skin.

<span id="class_BaseMaterial3D_constant_FLAG_PARTICLE_TRAILS_MODE"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_PARTICLE_TRAILS_MODE** = `19`

Enables parts of the shader required for [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) trails to function. This also requires using a mesh with appropriate skinning, such as [RibbonTrailMesh](class_ribbontrailmesh.md#class_RibbonTrailMesh) or [TubeTrailMesh](class_tubetrailmesh.md#class_TubeTrailMesh). Enabling this feature outside of materials used in [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) meshes will break material rendering.

<span id="class_BaseMaterial3D_constant_FLAG_ALBEDO_TEXTURE_MSDF"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_ALBEDO_TEXTURE_MSDF** = `20`

Enables multichannel signed distance field rendering shader.

<span id="class_BaseMaterial3D_constant_FLAG_DISABLE_FOG"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_DISABLE_FOG** = `21`

Disables receiving depth-based or volumetric fog.

<span id="class_BaseMaterial3D_constant_FLAG_DISABLE_SPECULAR_OCCLUSION"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_DISABLE_SPECULAR_OCCLUSION** = `22`

Disables specular occlusion.

<span id="class_BaseMaterial3D_constant_FLAG_USE_Z_CLIP_SCALE"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_USE_Z_CLIP_SCALE** = `23`

Enables using [z_clip_scale](class_basematerial3d.md#class_BaseMaterial3D_property_z_clip_scale).

<span id="class_BaseMaterial3D_constant_FLAG_USE_FOV_OVERRIDE"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_USE_FOV_OVERRIDE** = `24`

Enables using [fov_override](class_basematerial3d.md#class_BaseMaterial3D_property_fov_override).

<span id="class_BaseMaterial3D_constant_FLAG_MAX"></span>

[Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) **FLAG_MAX** = `25`

Represents the size of the [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) enum.

---

<span id="enum_BaseMaterial3D_DiffuseMode"></span>

enum **DiffuseMode**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_DiffuseMode)

<span id="class_BaseMaterial3D_constant_DIFFUSE_BURLEY"></span>

[DiffuseMode](class_basematerial3d.md#enum_BaseMaterial3D_DiffuseMode) **DIFFUSE_BURLEY** = `0`

Default diffuse scattering algorithm.

<span id="class_BaseMaterial3D_constant_DIFFUSE_LAMBERT"></span>

[DiffuseMode](class_basematerial3d.md#enum_BaseMaterial3D_DiffuseMode) **DIFFUSE_LAMBERT** = `1`

Diffuse scattering ignores roughness.

<span id="class_BaseMaterial3D_constant_DIFFUSE_LAMBERT_WRAP"></span>

[DiffuseMode](class_basematerial3d.md#enum_BaseMaterial3D_DiffuseMode) **DIFFUSE_LAMBERT_WRAP** = `2`

Extends Lambert to cover more than 90 degrees when roughness increases.

<span id="class_BaseMaterial3D_constant_DIFFUSE_TOON"></span>

[DiffuseMode](class_basematerial3d.md#enum_BaseMaterial3D_DiffuseMode) **DIFFUSE_TOON** = `3`

Uses a hard cut for lighting, with smoothing affected by roughness.

---

<span id="enum_BaseMaterial3D_SpecularMode"></span>

enum **SpecularMode**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_SpecularMode)

<span id="class_BaseMaterial3D_constant_SPECULAR_SCHLICK_GGX"></span>

[SpecularMode](class_basematerial3d.md#enum_BaseMaterial3D_SpecularMode) **SPECULAR_SCHLICK_GGX** = `0`

Default specular blob.

 **Note:** Forward+ uses multiscattering for more accurate reflections, although the impact of multiscattering is more noticeable on rough metallic surfaces than on smooth, non-metallic surfaces.

 **Note:** Mobile and Compatibility don't perform multiscattering for performance reasons. Instead, they perform single scattering, which means rough metallic surfaces may look slightly darker than intended.

<span id="class_BaseMaterial3D_constant_SPECULAR_TOON"></span>

[SpecularMode](class_basematerial3d.md#enum_BaseMaterial3D_SpecularMode) **SPECULAR_TOON** = `1`

Toon blob which changes size based on roughness.

<span id="class_BaseMaterial3D_constant_SPECULAR_DISABLED"></span>

[SpecularMode](class_basematerial3d.md#enum_BaseMaterial3D_SpecularMode) **SPECULAR_DISABLED** = `2`

No specular blob. This is slightly faster to render than other specular modes.

---

<span id="enum_BaseMaterial3D_BillboardMode"></span>

enum **BillboardMode**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode)

<span id="class_BaseMaterial3D_constant_BILLBOARD_DISABLED"></span>

[BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) **BILLBOARD_DISABLED** = `0`

Billboard mode is disabled.

<span id="class_BaseMaterial3D_constant_BILLBOARD_ENABLED"></span>

[BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) **BILLBOARD_ENABLED** = `1`

The object's Z axis will always face the camera.

<span id="class_BaseMaterial3D_constant_BILLBOARD_FIXED_Y"></span>

[BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) **BILLBOARD_FIXED_Y** = `2`

The object's X axis will always face the camera.

<span id="class_BaseMaterial3D_constant_BILLBOARD_PARTICLES"></span>

[BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) **BILLBOARD_PARTICLES** = `3`

Used for particle systems when assigned to [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) and [CPUParticles3D](class_cpuparticles3d.md#class_CPUParticles3D) nodes (flipbook animation). Enables `particles_anim_*` properties.

The [ParticleProcessMaterial.anim_speed_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_speed_min) or [CPUParticles3D.anim_speed_min](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_speed_min) should also be set to a value bigger than zero for the animation to play.

---

<span id="enum_BaseMaterial3D_TextureChannel"></span>

enum **TextureChannel**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel)

<span id="class_BaseMaterial3D_constant_TEXTURE_CHANNEL_RED"></span>

[TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **TEXTURE_CHANNEL_RED** = `0`

Used to read from the red channel of a texture.

<span id="class_BaseMaterial3D_constant_TEXTURE_CHANNEL_GREEN"></span>

[TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **TEXTURE_CHANNEL_GREEN** = `1`

Used to read from the green channel of a texture.

<span id="class_BaseMaterial3D_constant_TEXTURE_CHANNEL_BLUE"></span>

[TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **TEXTURE_CHANNEL_BLUE** = `2`

Used to read from the blue channel of a texture.

<span id="class_BaseMaterial3D_constant_TEXTURE_CHANNEL_ALPHA"></span>

[TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **TEXTURE_CHANNEL_ALPHA** = `3`

Used to read from the alpha channel of a texture.

<span id="class_BaseMaterial3D_constant_TEXTURE_CHANNEL_GRAYSCALE"></span>

[TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **TEXTURE_CHANNEL_GRAYSCALE** = `4`

Used to read from the linear (non-perceptual) average of the red, green and blue channels of a texture.

---

<span id="enum_BaseMaterial3D_EmissionOperator"></span>

enum **EmissionOperator**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_EmissionOperator)

<span id="class_BaseMaterial3D_constant_EMISSION_OP_ADD"></span>

[EmissionOperator](class_basematerial3d.md#enum_BaseMaterial3D_EmissionOperator) **EMISSION_OP_ADD** = `0`

Adds the emission color to the color from the emission texture.

<span id="class_BaseMaterial3D_constant_EMISSION_OP_MULTIPLY"></span>

[EmissionOperator](class_basematerial3d.md#enum_BaseMaterial3D_EmissionOperator) **EMISSION_OP_MULTIPLY** = `1`

Multiplies the emission color by the color from the emission texture.

---

<span id="enum_BaseMaterial3D_DistanceFadeMode"></span>

enum **DistanceFadeMode**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode)

<span id="class_BaseMaterial3D_constant_DISTANCE_FADE_DISABLED"></span>

[DistanceFadeMode](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode) **DISTANCE_FADE_DISABLED** = `0`

Do not use distance fade.

<span id="class_BaseMaterial3D_constant_DISTANCE_FADE_PIXEL_ALPHA"></span>

[DistanceFadeMode](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode) **DISTANCE_FADE_PIXEL_ALPHA** = `1`

Smoothly fades the object out based on each pixel's distance from the camera using the alpha channel.

<span id="class_BaseMaterial3D_constant_DISTANCE_FADE_PIXEL_DITHER"></span>

[DistanceFadeMode](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode) **DISTANCE_FADE_PIXEL_DITHER** = `2`

Smoothly fades the object out based on each pixel's distance from the camera using a dithering approach. Dithering discards pixels based on a set pattern to smoothly fade without enabling transparency. On certain hardware, this can be faster than [DISTANCE_FADE_PIXEL_ALPHA](class_basematerial3d.md#class_BaseMaterial3D_constant_DISTANCE_FADE_PIXEL_ALPHA).

<span id="class_BaseMaterial3D_constant_DISTANCE_FADE_OBJECT_DITHER"></span>

[DistanceFadeMode](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode) **DISTANCE_FADE_OBJECT_DITHER** = `3`

Smoothly fades the object out based on the object's distance from the camera using a dithering approach. Dithering discards pixels based on a set pattern to smoothly fade without enabling transparency. On certain hardware, this can be faster than [DISTANCE_FADE_PIXEL_ALPHA](class_basematerial3d.md#class_BaseMaterial3D_constant_DISTANCE_FADE_PIXEL_ALPHA) and [DISTANCE_FADE_PIXEL_DITHER](class_basematerial3d.md#class_BaseMaterial3D_constant_DISTANCE_FADE_PIXEL_DITHER).

---

<span id="enum_BaseMaterial3D_StencilMode"></span>

enum **StencilMode**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_StencilMode)

<span id="class_BaseMaterial3D_constant_STENCIL_MODE_DISABLED"></span>

[StencilMode](class_basematerial3d.md#enum_BaseMaterial3D_StencilMode) **STENCIL_MODE_DISABLED** = `0`

Disables stencil operations.

<span id="class_BaseMaterial3D_constant_STENCIL_MODE_OUTLINE"></span>

[StencilMode](class_basematerial3d.md#enum_BaseMaterial3D_StencilMode) **STENCIL_MODE_OUTLINE** = `1`

Stencil preset which applies an outline to the object.

 **Note:** Requires a [Material.next_pass](class_material.md#class_Material_property_next_pass) material which will be automatically applied. Any manual changes made to [Material.next_pass](class_material.md#class_Material_property_next_pass) will be lost when the stencil properties are modified or the scene is reloaded. To safely apply a [Material.next_pass](class_material.md#class_Material_property_next_pass) material on a material that uses stencil presets, use [GeometryInstance3D.material_overlay](class_geometryinstance3d.md#class_GeometryInstance3D_property_material_overlay) instead.

<span id="class_BaseMaterial3D_constant_STENCIL_MODE_XRAY"></span>

[StencilMode](class_basematerial3d.md#enum_BaseMaterial3D_StencilMode) **STENCIL_MODE_XRAY** = `2`

Stencil preset which shows a silhouette of the object behind walls.

 **Note:** Requires a [Material.next_pass](class_material.md#class_Material_property_next_pass) material which will be automatically applied. Any manual changes made to [Material.next_pass](class_material.md#class_Material_property_next_pass) will be lost when the stencil properties are modified or the scene is reloaded. To safely apply a [Material.next_pass](class_material.md#class_Material_property_next_pass) material on a material that uses stencil presets, use [GeometryInstance3D.material_overlay](class_geometryinstance3d.md#class_GeometryInstance3D_property_material_overlay) instead.

<span id="class_BaseMaterial3D_constant_STENCIL_MODE_CUSTOM"></span>

[StencilMode](class_basematerial3d.md#enum_BaseMaterial3D_StencilMode) **STENCIL_MODE_CUSTOM** = `3`

Enables stencil operations without a preset.

---

<span id="enum_BaseMaterial3D_StencilFlags"></span>

enum **StencilFlags**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_StencilFlags)

<span id="class_BaseMaterial3D_constant_STENCIL_FLAG_READ"></span>

[StencilFlags](class_basematerial3d.md#enum_BaseMaterial3D_StencilFlags) **STENCIL_FLAG_READ** = `1`

The material will only be rendered where it passes a stencil comparison with existing stencil buffer values.

<span id="class_BaseMaterial3D_constant_STENCIL_FLAG_WRITE"></span>

[StencilFlags](class_basematerial3d.md#enum_BaseMaterial3D_StencilFlags) **STENCIL_FLAG_WRITE** = `2`

The material will write the reference value to the stencil buffer where it passes the depth test.

<span id="class_BaseMaterial3D_constant_STENCIL_FLAG_WRITE_DEPTH_FAIL"></span>

[StencilFlags](class_basematerial3d.md#enum_BaseMaterial3D_StencilFlags) **STENCIL_FLAG_WRITE_DEPTH_FAIL** = `4`

The material will write the reference value to the stencil buffer where it fails the depth test.

---

<span id="enum_BaseMaterial3D_StencilCompare"></span>

enum **StencilCompare**: [🔗](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare)

<span id="class_BaseMaterial3D_constant_STENCIL_COMPARE_ALWAYS"></span>

[StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) **STENCIL_COMPARE_ALWAYS** = `0`

Always passes the stencil test.

<span id="class_BaseMaterial3D_constant_STENCIL_COMPARE_LESS"></span>

[StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) **STENCIL_COMPARE_LESS** = `1`

Passes the stencil test when the reference value is less than the existing stencil value.

<span id="class_BaseMaterial3D_constant_STENCIL_COMPARE_EQUAL"></span>

[StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) **STENCIL_COMPARE_EQUAL** = `2`

Passes the stencil test when the reference value is equal to the existing stencil value.

<span id="class_BaseMaterial3D_constant_STENCIL_COMPARE_LESS_OR_EQUAL"></span>

[StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) **STENCIL_COMPARE_LESS_OR_EQUAL** = `3`

Passes the stencil test when the reference value is less than or equal to the existing stencil value.

<span id="class_BaseMaterial3D_constant_STENCIL_COMPARE_GREATER"></span>

[StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) **STENCIL_COMPARE_GREATER** = `4`

Passes the stencil test when the reference value is greater than the existing stencil value.

<span id="class_BaseMaterial3D_constant_STENCIL_COMPARE_NOT_EQUAL"></span>

[StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) **STENCIL_COMPARE_NOT_EQUAL** = `5`

Passes the stencil test when the reference value is not equal to the existing stencil value.

<span id="class_BaseMaterial3D_constant_STENCIL_COMPARE_GREATER_OR_EQUAL"></span>

[StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) **STENCIL_COMPARE_GREATER_OR_EQUAL** = `6`

Passes the stencil test when the reference value is greater than or equal to the existing stencil value.

---

### Property Descriptions

<span id="class_BaseMaterial3D_property_albedo_color"></span>

[Color](class_color.md#class_Color) **albedo_color** = `Color(1, 1, 1, 1)` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_color)

- void **set_albedo** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_albedo** ( )

The material's base color.

 **Note:** If [detail_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_detail_enabled) is `true` and a [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo) texture is specified, [albedo_color](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_color) will *not* modulate the detail texture. This can be used to color partial areas of a material by not specifying an albedo texture and using a transparent [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo) texture instead.

---

<span id="class_BaseMaterial3D_property_albedo_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **albedo_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture to multiply by [albedo_color](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_color). Used for basic texturing of objects.

If the texture appears unexpectedly too dark or too bright, check [albedo_texture_force_srgb](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture_force_srgb).

---

<span id="class_BaseMaterial3D_property_albedo_texture_force_srgb"></span>

[bool](class_bool.md#class_bool) **albedo_texture_force_srgb** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture_force_srgb)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, forces a conversion of the [albedo_texture](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture) from nonlinear sRGB encoding to linear encoding. See also [vertex_color_is_srgb](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_is_srgb).

This should only be enabled when needed (typically when using a [ViewportTexture](class_viewporttexture.md#class_ViewportTexture) as [albedo_texture](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture)). If [albedo_texture_force_srgb](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture_force_srgb) is `true` when it shouldn't be, the texture will appear to be too dark. If [albedo_texture_force_srgb](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture_force_srgb) is `false` when it shouldn't be, the texture will appear to be too bright.

---

<span id="class_BaseMaterial3D_property_albedo_texture_msdf"></span>

[bool](class_bool.md#class_bool) **albedo_texture_msdf** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture_msdf)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

Enables multichannel signed distance field rendering shader. Use [msdf_pixel_range](class_basematerial3d.md#class_BaseMaterial3D_property_msdf_pixel_range) and [msdf_outline_size](class_basematerial3d.md#class_BaseMaterial3D_property_msdf_outline_size) to configure MSDF parameters.

---

<span id="class_BaseMaterial3D_property_alpha_antialiasing_edge"></span>

[float](class_float.md#class_float) **alpha_antialiasing_edge** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_antialiasing_edge)

- void **set_alpha_antialiasing_edge** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_alpha_antialiasing_edge** ( )

Threshold at which antialiasing will be applied on the alpha channel.

---

<span id="class_BaseMaterial3D_property_alpha_antialiasing_mode"></span>

[AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) **alpha_antialiasing_mode** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_antialiasing_mode)

- void **set_alpha_antialiasing** ( value: [AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) )
- [AlphaAntiAliasing](class_basematerial3d.md#enum_BaseMaterial3D_AlphaAntiAliasing) **get_alpha_antialiasing** ( )

The type of alpha antialiasing to apply.

---

<span id="class_BaseMaterial3D_property_alpha_hash_scale"></span>

[float](class_float.md#class_float) **alpha_hash_scale** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_hash_scale)

- void **set_alpha_hash_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_alpha_hash_scale** ( )

The hashing scale for Alpha Hash. Recommended values between `0` and `2`.

---

<span id="class_BaseMaterial3D_property_alpha_scissor_threshold"></span>

[float](class_float.md#class_float) **alpha_scissor_threshold** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_scissor_threshold)

- void **set_alpha_scissor_threshold** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_alpha_scissor_threshold** ( )

Threshold at which the alpha scissor will discard values. Higher values will result in more pixels being discarded. If the material becomes too opaque at a distance, try increasing [alpha_scissor_threshold](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_scissor_threshold). If the material disappears at a distance, try decreasing [alpha_scissor_threshold](class_basematerial3d.md#class_BaseMaterial3D_property_alpha_scissor_threshold).

---

<span id="class_BaseMaterial3D_property_anisotropy"></span>

[float](class_float.md#class_float) **anisotropy** = `0.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy)

- void **set_anisotropy** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_anisotropy** ( )

The strength of the anisotropy effect. This is multiplied by [anisotropy_flowmap](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy_flowmap)'s alpha channel if a texture is defined there and the texture contains an alpha channel.

---

<span id="class_BaseMaterial3D_property_anisotropy_enabled"></span>

[bool](class_bool.md#class_bool) **anisotropy_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, anisotropy is enabled. Anisotropy changes the shape of the specular blob and aligns it to tangent space. This is useful for brushed aluminum and hair reflections.

 **Note:** Mesh tangents are needed for anisotropy to work. If the mesh does not contain tangents, the anisotropy effect will appear broken.

 **Note:** Material anisotropy should not to be confused with anisotropic texture filtering, which can be enabled by setting [texture_filter](class_basematerial3d.md#class_BaseMaterial3D_property_texture_filter) to [TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC](class_basematerial3d.md#class_BaseMaterial3D_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC).

---

<span id="class_BaseMaterial3D_property_anisotropy_flowmap"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **anisotropy_flowmap** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy_flowmap)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture that offsets the tangent map for anisotropy calculations and optionally controls the anisotropy effect (if an alpha channel is present). The flowmap texture is expected to be a derivative map, with the red channel representing distortion on the X axis and green channel representing distortion on the Y axis. Values below 0.5 will result in negative distortion, whereas values above 0.5 will result in positive distortion.

If present, the texture's alpha channel will be used to multiply the strength of the [anisotropy](class_basematerial3d.md#class_BaseMaterial3D_property_anisotropy) effect. Fully opaque pixels will keep the anisotropy effect's original strength while fully transparent pixels will disable the anisotropy effect entirely. The flowmap texture's blue channel is ignored.

---

<span id="class_BaseMaterial3D_property_ao_enabled"></span>

[bool](class_bool.md#class_bool) **ao_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_ao_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, ambient occlusion is enabled. Ambient occlusion darkens areas based on the [ao_texture](class_basematerial3d.md#class_BaseMaterial3D_property_ao_texture).

---

<span id="class_BaseMaterial3D_property_ao_light_affect"></span>

[float](class_float.md#class_float) **ao_light_affect** = `0.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_ao_light_affect)

- void **set_ao_light_affect** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_ao_light_affect** ( )

Amount that ambient occlusion affects lighting from lights. If `0`, ambient occlusion only affects ambient light. If `1`, ambient occlusion affects lights just as much as it affects ambient light. This can be used to impact the strength of the ambient occlusion effect, but typically looks unrealistic.

---

<span id="class_BaseMaterial3D_property_ao_on_uv2"></span>

[bool](class_bool.md#class_bool) **ao_on_uv2** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_ao_on_uv2)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, use `UV2` coordinates to look up from the [ao_texture](class_basematerial3d.md#class_BaseMaterial3D_property_ao_texture).

---

<span id="class_BaseMaterial3D_property_ao_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **ao_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_ao_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture that defines the amount of ambient occlusion for a given point on the object.

---

<span id="class_BaseMaterial3D_property_ao_texture_channel"></span>

[TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **ao_texture_channel** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_ao_texture_channel)

- void **set_ao_texture_channel** ( value: [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) )
- [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **get_ao_texture_channel** ( )

Specifies the channel of the [ao_texture](class_basematerial3d.md#class_BaseMaterial3D_property_ao_texture) in which the ambient occlusion information is stored. This is useful when you store the information for multiple effects in a single texture. For example if you stored metallic in the red channel, roughness in the blue, and ambient occlusion in the green you could reduce the number of textures you use.

---

<span id="class_BaseMaterial3D_property_backlight"></span>

[Color](class_color.md#class_Color) **backlight** = `Color(0, 0, 0, 1)` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_backlight)

- void **set_backlight** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_backlight** ( )

The color used by the backlight effect. Represents the light passing through an object.

---

<span id="class_BaseMaterial3D_property_backlight_enabled"></span>

[bool](class_bool.md#class_bool) **backlight_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_backlight_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, the backlight effect is enabled. See also [subsurf_scatter_transmittance_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_enabled).

---

<span id="class_BaseMaterial3D_property_backlight_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **backlight_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_backlight_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture used to control the backlight effect per-pixel. Added to [backlight](class_basematerial3d.md#class_BaseMaterial3D_property_backlight).

---

<span id="class_BaseMaterial3D_property_bent_normal_enabled"></span>

[bool](class_bool.md#class_bool) **bent_normal_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_bent_normal_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, the bent normal map is enabled. This allows for more accurate indirect lighting and specular occlusion.

---

<span id="class_BaseMaterial3D_property_bent_normal_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **bent_normal_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_bent_normal_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture that specifies the average direction of incoming ambient light at a given pixel. The [bent_normal_texture](class_basematerial3d.md#class_BaseMaterial3D_property_bent_normal_texture) only uses the red and green channels; the blue and alpha channels are ignored. The normal read from [bent_normal_texture](class_basematerial3d.md#class_BaseMaterial3D_property_bent_normal_texture) is oriented around the surface normal provided by the [Mesh](class_mesh.md#class_Mesh).

 **Note:** A bent normal map is different from a regular normal map. When baking a bent normal map make sure to use **a cosine distribution** for the bent normal map to work correctly.

 **Note:** The mesh must have both normals and tangents defined in its vertex data. Otherwise, the shading produced by the bent normal map will not look correct. If creating geometry with [SurfaceTool](class_surfacetool.md#class_SurfaceTool), you can use [SurfaceTool.generate_normals()](class_surfacetool.md#class_SurfaceTool_method_generate_normals) and [SurfaceTool.generate_tangents()](class_surfacetool.md#class_SurfaceTool_method_generate_tangents) to automatically generate normals and tangents respectively.

 **Note:** Godot expects the bent normal map to use X+, Y+, and Z+ coordinates. See this page for a comparison of normal map coordinates expected by popular engines.

---

<span id="class_BaseMaterial3D_property_billboard_keep_scale"></span>

[bool](class_bool.md#class_bool) **billboard_keep_scale** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_billboard_keep_scale)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, the shader will keep the scale set for the mesh. Otherwise, the scale is lost when billboarding. Only applies when [billboard_mode](class_basematerial3d.md#class_BaseMaterial3D_property_billboard_mode) is not [BILLBOARD_DISABLED](class_basematerial3d.md#class_BaseMaterial3D_constant_BILLBOARD_DISABLED).

---

<span id="class_BaseMaterial3D_property_billboard_mode"></span>

[BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) **billboard_mode** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_billboard_mode)

- void **set_billboard_mode** ( value: [BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) )
- [BillboardMode](class_basematerial3d.md#enum_BaseMaterial3D_BillboardMode) **get_billboard_mode** ( )

Controls how the object faces the camera.

 **Note:** Billboard mode is not suitable for VR because the left-right vector of the camera is not horizontal when the screen is attached to your head instead of on the table. See GitHub issue #41567 for details.

---

<span id="class_BaseMaterial3D_property_blend_mode"></span>

[BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) **blend_mode** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_blend_mode)

- void **set_blend_mode** ( value: [BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) )
- [BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) **get_blend_mode** ( )

The material's blend mode.

 **Note:** Values other than `Mix` force the object into the transparent pipeline.

---

<span id="class_BaseMaterial3D_property_clearcoat"></span>

[float](class_float.md#class_float) **clearcoat** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_clearcoat)

- void **set_clearcoat** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_clearcoat** ( )

Sets the strength of the clearcoat effect. Setting to `0` looks the same as disabling the clearcoat effect.

---

<span id="class_BaseMaterial3D_property_clearcoat_enabled"></span>

[bool](class_bool.md#class_bool) **clearcoat_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_clearcoat_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, clearcoat rendering is enabled. Adds a secondary transparent pass to the lighting calculation resulting in an added specular blob. This makes materials appear as if they have a clear layer on them that can be either glossy or rough.

 **Note:** Clearcoat rendering is not visible if the material's [shading_mode](class_basematerial3d.md#class_BaseMaterial3D_property_shading_mode) is [SHADING_MODE_UNSHADED](class_basematerial3d.md#class_BaseMaterial3D_constant_SHADING_MODE_UNSHADED).

---

<span id="class_BaseMaterial3D_property_clearcoat_roughness"></span>

[float](class_float.md#class_float) **clearcoat_roughness** = `0.5` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_clearcoat_roughness)

- void **set_clearcoat_roughness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_clearcoat_roughness** ( )

Sets the roughness of the clearcoat pass. A higher value results in a rougher clearcoat while a lower value results in a smoother clearcoat.

---

<span id="class_BaseMaterial3D_property_clearcoat_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **clearcoat_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_clearcoat_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture that defines the strength of the clearcoat effect and the glossiness of the clearcoat. Strength is specified in the red channel while glossiness is specified in the green channel.

---

<span id="class_BaseMaterial3D_property_cull_mode"></span>

[CullMode](class_basematerial3d.md#enum_BaseMaterial3D_CullMode) **cull_mode** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_cull_mode)

- void **set_cull_mode** ( value: [CullMode](class_basematerial3d.md#enum_BaseMaterial3D_CullMode) )
- [CullMode](class_basematerial3d.md#enum_BaseMaterial3D_CullMode) **get_cull_mode** ( )

Determines which side of the triangle to cull depending on whether the triangle faces towards or away from the camera.

---

<span id="class_BaseMaterial3D_property_depth_draw_mode"></span>

[DepthDrawMode](class_basematerial3d.md#enum_BaseMaterial3D_DepthDrawMode) **depth_draw_mode** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_depth_draw_mode)

- void **set_depth_draw_mode** ( value: [DepthDrawMode](class_basematerial3d.md#enum_BaseMaterial3D_DepthDrawMode) )
- [DepthDrawMode](class_basematerial3d.md#enum_BaseMaterial3D_DepthDrawMode) **get_depth_draw_mode** ( )

Determines when depth rendering takes place. See also [transparency](class_basematerial3d.md#class_BaseMaterial3D_property_transparency).

---

<span id="class_BaseMaterial3D_property_depth_test"></span>

[DepthTest](class_basematerial3d.md#enum_BaseMaterial3D_DepthTest) **depth_test** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_depth_test)

- void **set_depth_test** ( value: [DepthTest](class_basematerial3d.md#enum_BaseMaterial3D_DepthTest) )
- [DepthTest](class_basematerial3d.md#enum_BaseMaterial3D_DepthTest) **get_depth_test** ( )

**Experimental:** May be affected by future rendering pipeline changes.

Determines which comparison operator is used when testing depth.

 **Note:** Changing [depth_test](class_basematerial3d.md#class_BaseMaterial3D_property_depth_test) to a non-default value only has a visible effect when used on a transparent material, or a material that has [depth_draw_mode](class_basematerial3d.md#class_BaseMaterial3D_property_depth_draw_mode) set to [DEPTH_DRAW_DISABLED](class_basematerial3d.md#class_BaseMaterial3D_constant_DEPTH_DRAW_DISABLED).

---

<span id="class_BaseMaterial3D_property_detail_albedo"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **detail_albedo** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture that specifies the color of the detail overlay. [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo)'s alpha channel is used as a mask, even when the material is opaque. To use a dedicated texture as a mask, see [detail_mask](class_basematerial3d.md#class_BaseMaterial3D_property_detail_mask).

 **Note:** [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo) is *not* modulated by [albedo_color](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_color).

---

<span id="class_BaseMaterial3D_property_detail_blend_mode"></span>

[BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) **detail_blend_mode** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_detail_blend_mode)

- void **set_detail_blend_mode** ( value: [BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) )
- [BlendMode](class_basematerial3d.md#enum_BaseMaterial3D_BlendMode) **get_detail_blend_mode** ( )

Specifies how the [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo) should blend with the current `ALBEDO`.

---

<span id="class_BaseMaterial3D_property_detail_enabled"></span>

[bool](class_bool.md#class_bool) **detail_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_detail_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, enables the detail overlay. Detail is a second texture that gets mixed over the surface of the object based on [detail_mask](class_basematerial3d.md#class_BaseMaterial3D_property_detail_mask) and [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo)'s alpha channel. This can be used to add variation to objects, or to blend between two different albedo/normal textures.

---

<span id="class_BaseMaterial3D_property_detail_mask"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **detail_mask** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_detail_mask)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture used to specify how the detail textures get blended with the base textures. [detail_mask](class_basematerial3d.md#class_BaseMaterial3D_property_detail_mask) can be used together with [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo)'s alpha channel (if any).

---

<span id="class_BaseMaterial3D_property_detail_normal"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **detail_normal** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_detail_normal)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture that specifies the per-pixel normal of the detail overlay. The [detail_normal](class_basematerial3d.md#class_BaseMaterial3D_property_detail_normal) texture only uses the red and green channels; the blue and alpha channels are ignored. The normal read from [detail_normal](class_basematerial3d.md#class_BaseMaterial3D_property_detail_normal) is oriented around the surface normal provided by the [Mesh](class_mesh.md#class_Mesh).

 **Note:** Godot expects the normal map to use X+, Y+, and Z+ coordinates. See this page for a comparison of normal map coordinates expected by popular engines.

---

<span id="class_BaseMaterial3D_property_detail_uv_layer"></span>

[DetailUV](class_basematerial3d.md#enum_BaseMaterial3D_DetailUV) **detail_uv_layer** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_detail_uv_layer)

- void **set_detail_uv** ( value: [DetailUV](class_basematerial3d.md#enum_BaseMaterial3D_DetailUV) )
- [DetailUV](class_basematerial3d.md#enum_BaseMaterial3D_DetailUV) **get_detail_uv** ( )

Specifies whether to use `UV` or `UV2` for the detail layer.

---

<span id="class_BaseMaterial3D_property_diffuse_mode"></span>

[DiffuseMode](class_basematerial3d.md#enum_BaseMaterial3D_DiffuseMode) **diffuse_mode** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_diffuse_mode)

- void **set_diffuse_mode** ( value: [DiffuseMode](class_basematerial3d.md#enum_BaseMaterial3D_DiffuseMode) )
- [DiffuseMode](class_basematerial3d.md#enum_BaseMaterial3D_DiffuseMode) **get_diffuse_mode** ( )

The algorithm used for diffuse light scattering.

---

<span id="class_BaseMaterial3D_property_disable_ambient_light"></span>

[bool](class_bool.md#class_bool) **disable_ambient_light** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_disable_ambient_light)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, the object receives no ambient light.

---

<span id="class_BaseMaterial3D_property_disable_fog"></span>

[bool](class_bool.md#class_bool) **disable_fog** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_disable_fog)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, the object will not be affected by fog (neither volumetric nor depth fog). This is useful for unshaded or transparent materials (e.g. particles), which without this setting will be affected even if fully transparent.

---

<span id="class_BaseMaterial3D_property_disable_receive_shadows"></span>

[bool](class_bool.md#class_bool) **disable_receive_shadows** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_disable_receive_shadows)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, the object receives no shadow that would otherwise be cast onto it.

---

<span id="class_BaseMaterial3D_property_disable_specular_occlusion"></span>

[bool](class_bool.md#class_bool) **disable_specular_occlusion** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_disable_specular_occlusion)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, disables specular occlusion even if ProjectSettings.rendering/reflections/specular_occlusion/enabled is `false`.

---

<span id="class_BaseMaterial3D_property_distance_fade_max_distance"></span>

[float](class_float.md#class_float) **distance_fade_max_distance** = `10.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_max_distance)

- void **set_distance_fade_max_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_distance_fade_max_distance** ( )

Distance at which the object appears fully opaque.

 **Note:** If [distance_fade_max_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_max_distance) is less than [distance_fade_min_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_min_distance), the behavior will be reversed. The object will start to fade away at [distance_fade_max_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_max_distance) and will fully disappear once it reaches [distance_fade_min_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_min_distance).

---

<span id="class_BaseMaterial3D_property_distance_fade_min_distance"></span>

[float](class_float.md#class_float) **distance_fade_min_distance** = `0.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_min_distance)

- void **set_distance_fade_min_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_distance_fade_min_distance** ( )

Distance at which the object starts to become visible. If the object is less than this distance away, it will be invisible.

 **Note:** If [distance_fade_min_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_min_distance) is greater than [distance_fade_max_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_max_distance), the behavior will be reversed. The object will start to fade away at [distance_fade_max_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_max_distance) and will fully disappear once it reaches [distance_fade_min_distance](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_min_distance).

---

<span id="class_BaseMaterial3D_property_distance_fade_mode"></span>

[DistanceFadeMode](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode) **distance_fade_mode** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_distance_fade_mode)

- void **set_distance_fade** ( value: [DistanceFadeMode](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode) )
- [DistanceFadeMode](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode) **get_distance_fade** ( )

Specifies which type of fade to use. Can be any of the [DistanceFadeMode](class_basematerial3d.md#enum_BaseMaterial3D_DistanceFadeMode) s.

---

<span id="class_BaseMaterial3D_property_emission"></span>

[Color](class_color.md#class_Color) **emission** = `Color(0, 0, 0, 1)` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_emission)

- void **set_emission** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_emission** ( )

The emitted light's color. See [emission_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_emission_enabled).

---

<span id="class_BaseMaterial3D_property_emission_enabled"></span>

[bool](class_bool.md#class_bool) **emission_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_emission_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, the body emits light. Emitting light makes the object appear brighter. The object can also cast light on other objects if a [VoxelGI](class_voxelgi.md#class_VoxelGI), SDFGI, or [LightmapGI](class_lightmapgi.md#class_LightmapGI) is used and this object is used in baked lighting.

---

<span id="class_BaseMaterial3D_property_emission_energy_multiplier"></span>

[float](class_float.md#class_float) **emission_energy_multiplier** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_emission_energy_multiplier)

- void **set_emission_energy_multiplier** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_energy_multiplier** ( )

Multiplier for emitted light. See [emission_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_emission_enabled).

---

<span id="class_BaseMaterial3D_property_emission_intensity"></span>

[float](class_float.md#class_float) **emission_intensity** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_emission_intensity)

- void **set_emission_intensity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_intensity** ( )

Luminance of emitted light, measured in nits (candela per square meter). Only available when ProjectSettings.rendering/lights_and_shadows/use_physical_light_units is enabled. The default is roughly equivalent to an indoor lightbulb.

---

<span id="class_BaseMaterial3D_property_emission_on_uv2"></span>

[bool](class_bool.md#class_bool) **emission_on_uv2** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_emission_on_uv2)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

Use `UV2` to read from the [emission_texture](class_basematerial3d.md#class_BaseMaterial3D_property_emission_texture).

---

<span id="class_BaseMaterial3D_property_emission_operator"></span>

[EmissionOperator](class_basematerial3d.md#enum_BaseMaterial3D_EmissionOperator) **emission_operator** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_emission_operator)

- void **set_emission_operator** ( value: [EmissionOperator](class_basematerial3d.md#enum_BaseMaterial3D_EmissionOperator) )
- [EmissionOperator](class_basematerial3d.md#enum_BaseMaterial3D_EmissionOperator) **get_emission_operator** ( )

Sets how [emission](class_basematerial3d.md#class_BaseMaterial3D_property_emission) interacts with [emission_texture](class_basematerial3d.md#class_BaseMaterial3D_property_emission_texture). Can either add or multiply.

---

<span id="class_BaseMaterial3D_property_emission_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **emission_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_emission_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture that specifies how much surface emits light at a given point.

---

<span id="class_BaseMaterial3D_property_fixed_size"></span>

[bool](class_bool.md#class_bool) **fixed_size** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_fixed_size)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, the object is rendered at the same size regardless of distance. The object's size on screen is the same as if the camera was `1.0` units away from the object's origin, regardless of the actual distance from the camera. The [Camera3D](class_camera3d.md#class_Camera3D)'s field of view (or [Camera3D.size](class_camera3d.md#class_Camera3D_property_size) when in orthogonal/frustum mode) still affects the size the object is drawn at.

---

<span id="class_BaseMaterial3D_property_fov_override"></span>

[float](class_float.md#class_float) **fov_override** = `75.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_fov_override)

- void **set_fov_override** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fov_override** ( )

Overrides the [Camera3D](class_camera3d.md#class_Camera3D)'s field of view angle (in degrees).

 **Note:** This behaves as if the field of view is set on a [Camera3D](class_camera3d.md#class_Camera3D) with [Camera3D.keep_aspect](class_camera3d.md#class_Camera3D_property_keep_aspect) set to [Camera3D.KEEP_HEIGHT](class_camera3d.md#class_Camera3D_constant_KEEP_HEIGHT). Additionally, it may not look correct on a non-perspective camera where the field of view setting is ignored.

---

<span id="class_BaseMaterial3D_property_grow"></span>

[bool](class_bool.md#class_bool) **grow** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_grow)

- void **set_grow_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_grow_enabled** ( )

If `true`, enables the vertex grow setting. This can be used to create mesh-based outlines using a second material pass and its [cull_mode](class_basematerial3d.md#class_BaseMaterial3D_property_cull_mode) set to [CULL_FRONT](class_basematerial3d.md#class_BaseMaterial3D_constant_CULL_FRONT). See also [grow_amount](class_basematerial3d.md#class_BaseMaterial3D_property_grow_amount).

 **Note:** Vertex growth cannot create new vertices, which means that visible gaps may occur in sharp corners. This can be alleviated by designing the mesh to use smooth normals exclusively using face weighted normals in the 3D authoring software. In this case, grow will be able to join every outline together, just like in the original mesh.

---

<span id="class_BaseMaterial3D_property_grow_amount"></span>

[float](class_float.md#class_float) **grow_amount** = `0.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_grow_amount)

- void **set_grow** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_grow** ( )

Grows object vertices in the direction of their normals. Only effective if [grow](class_basematerial3d.md#class_BaseMaterial3D_property_grow) is `true`.

---

<span id="class_BaseMaterial3D_property_heightmap_deep_parallax"></span>

[bool](class_bool.md#class_bool) **heightmap_deep_parallax** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_deep_parallax)

- void **set_heightmap_deep_parallax** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_heightmap_deep_parallax_enabled** ( )

If `true`, uses parallax occlusion mapping to represent depth in the material instead of simple offset mapping (see [heightmap_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_enabled)). This results in a more convincing depth effect, but is much more expensive on the GPU. Only enable this on materials where it makes a significant visual difference.

---

<span id="class_BaseMaterial3D_property_heightmap_enabled"></span>

[bool](class_bool.md#class_bool) **heightmap_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, height mapping is enabled (also called "parallax mapping" or "depth mapping"). See also [normal_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_normal_enabled). Height mapping is a demanding feature on the GPU, so it should only be used on materials where it makes a significant visual difference.

 **Note:** Height mapping is not supported if triplanar mapping is used on the same material. The value of [heightmap_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_enabled) will be ignored if [uv1_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_triplanar) is enabled.

---

<span id="class_BaseMaterial3D_property_heightmap_flip_binormal"></span>

[bool](class_bool.md#class_bool) **heightmap_flip_binormal** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_binormal)

- void **set_heightmap_deep_parallax_flip_binormal** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_heightmap_deep_parallax_flip_binormal** ( )

If `true`, flips the mesh's binormal vectors when interpreting the height map. If the heightmap effect looks strange when the camera moves (even with a reasonable [heightmap_scale](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_scale)), try setting this to `true`.

---

<span id="class_BaseMaterial3D_property_heightmap_flip_tangent"></span>

[bool](class_bool.md#class_bool) **heightmap_flip_tangent** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_tangent)

- void **set_heightmap_deep_parallax_flip_tangent** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_heightmap_deep_parallax_flip_tangent** ( )

If `true`, flips the mesh's tangent vectors when interpreting the height map. If the heightmap effect looks strange when the camera moves (even with a reasonable [heightmap_scale](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_scale)), try setting this to `true`.

---

<span id="class_BaseMaterial3D_property_heightmap_flip_texture"></span>

[bool](class_bool.md#class_bool) **heightmap_flip_texture** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_texture)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, interprets the height map texture as a depth map, with brighter values appearing to be "lower" in altitude compared to darker values.

This can be enabled for compatibility with some materials authored for Godot 3.x. This is not necessary if the Invert import option was used to invert the depth map in Godot 3.x, in which case [heightmap_flip_texture](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_texture) should remain `false`.

---

<span id="class_BaseMaterial3D_property_heightmap_max_layers"></span>

[int](class_int.md#class_int) **heightmap_max_layers** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_max_layers)

- void **set_heightmap_deep_parallax_max_layers** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_heightmap_deep_parallax_max_layers** ( )

The number of layers to use for parallax occlusion mapping when the camera is up close to the material. Higher values result in a more convincing depth effect, especially in materials that have steep height changes. Higher values have a significant cost on the GPU, so it should only be increased on materials where it makes a significant visual difference.

 **Note:** Only effective if [heightmap_deep_parallax](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_deep_parallax) is `true`.

---

<span id="class_BaseMaterial3D_property_heightmap_min_layers"></span>

[int](class_int.md#class_int) **heightmap_min_layers** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_min_layers)

- void **set_heightmap_deep_parallax_min_layers** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_heightmap_deep_parallax_min_layers** ( )

The number of layers to use for parallax occlusion mapping when the camera is far away from the material. Higher values result in a more convincing depth effect, especially in materials that have steep height changes. Higher values have a significant cost on the GPU, so it should only be increased on materials where it makes a significant visual difference.

 **Note:** Only effective if [heightmap_deep_parallax](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_deep_parallax) is `true`.

---

<span id="class_BaseMaterial3D_property_heightmap_scale"></span>

[float](class_float.md#class_float) **heightmap_scale** = `5.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_scale)

- void **set_heightmap_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_heightmap_scale** ( )

The heightmap scale to use for the parallax effect (see [heightmap_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_enabled)). The default value is tuned so that the highest point (value = 255) appears to be 5 cm higher than the lowest point (value = 0). Higher values result in a deeper appearance, but may result in artifacts appearing when looking at the material from oblique angles, especially when the camera moves. Negative values can be used to invert the parallax effect, but this is different from inverting the texture using [heightmap_flip_texture](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_texture) as the material will also appear to be "closer" to the camera. In most cases, [heightmap_scale](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_scale) should be kept to a positive value.

 **Note:** If the height map effect looks strange regardless of this value, try adjusting [heightmap_flip_binormal](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_binormal) and [heightmap_flip_tangent](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_flip_tangent). See also [heightmap_texture](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_texture) for recommendations on authoring heightmap textures, as the way the heightmap texture is authored affects how [heightmap_scale](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_scale) behaves.

---

<span id="class_BaseMaterial3D_property_heightmap_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **heightmap_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

The texture to use as a height map. See also [heightmap_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_enabled).

For best results, the texture should be normalized (with [heightmap_scale](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_scale) reduced to compensate). In GIMP, this can be done using **Colors > Auto > Equalize**. If the texture only uses a small part of its available range, the parallax effect may look strange, especially when the camera moves.

 **Note:** To reduce memory usage and improve loading times, you may be able to use a lower-resolution heightmap texture as most heightmaps are only comprised of low-frequency data.

---

<span id="class_BaseMaterial3D_property_metallic"></span>

[float](class_float.md#class_float) **metallic** = `0.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_metallic)

- void **set_metallic** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_metallic** ( )

A high value makes the material appear more like a metal. Non-metals use their albedo as the diffuse color and add diffuse to the specular reflection. With non-metals, the reflection appears on top of the albedo color. Metals use their albedo as a multiplier to the specular reflection and set the diffuse color to black resulting in a tinted reflection. Materials work better when fully metal or fully non-metal, values between `0` and `1` should only be used for blending between metal and non-metal sections. To alter the amount of reflection use [roughness](class_basematerial3d.md#class_BaseMaterial3D_property_roughness).

---

<span id="class_BaseMaterial3D_property_metallic_specular"></span>

[float](class_float.md#class_float) **metallic_specular** = `0.5` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_metallic_specular)

- void **set_specular** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_specular** ( )

Adjusts the strength of specular reflections. Specular reflections are composed of scene reflections and the specular lobe which is the bright spot that is reflected from light sources. When set to `0.0`, no specular reflections will be visible. This differs from the [SPECULAR_DISABLED](class_basematerial3d.md#class_BaseMaterial3D_constant_SPECULAR_DISABLED) [SpecularMode](class_basematerial3d.md#enum_BaseMaterial3D_SpecularMode) as [SPECULAR_DISABLED](class_basematerial3d.md#class_BaseMaterial3D_constant_SPECULAR_DISABLED) only applies to the specular lobe from the light source.

 **Note:** Unlike [metallic](class_basematerial3d.md#class_BaseMaterial3D_property_metallic), this is not energy-conserving, so it should be left at `0.5` in most cases. See also [roughness](class_basematerial3d.md#class_BaseMaterial3D_property_roughness).

---

<span id="class_BaseMaterial3D_property_metallic_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **metallic_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_metallic_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture used to specify metallic for an object. This is multiplied by [metallic](class_basematerial3d.md#class_BaseMaterial3D_property_metallic).

---

<span id="class_BaseMaterial3D_property_metallic_texture_channel"></span>

[TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **metallic_texture_channel** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_metallic_texture_channel)

- void **set_metallic_texture_channel** ( value: [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) )
- [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **get_metallic_texture_channel** ( )

Specifies the channel of the [metallic_texture](class_basematerial3d.md#class_BaseMaterial3D_property_metallic_texture) in which the metallic information is stored. This is useful when you store the information for multiple effects in a single texture. For example if you stored metallic in the red channel, roughness in the blue, and ambient occlusion in the green you could reduce the number of textures you use.

---

<span id="class_BaseMaterial3D_property_msdf_outline_size"></span>

[float](class_float.md#class_float) **msdf_outline_size** = `0.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_msdf_outline_size)

- void **set_msdf_outline_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_msdf_outline_size** ( )

The width of the shape outline.

---

<span id="class_BaseMaterial3D_property_msdf_pixel_range"></span>

[float](class_float.md#class_float) **msdf_pixel_range** = `4.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_msdf_pixel_range)

- void **set_msdf_pixel_range** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_msdf_pixel_range** ( )

The width of the range around the shape between the minimum and maximum representable signed distance.

---

<span id="class_BaseMaterial3D_property_no_depth_test"></span>

[bool](class_bool.md#class_bool) **no_depth_test** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_no_depth_test)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, depth testing is disabled and the object will be drawn in render order.

---

<span id="class_BaseMaterial3D_property_normal_enabled"></span>

[bool](class_bool.md#class_bool) **normal_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_normal_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, normal mapping is enabled. This has a slight performance cost, especially on mobile GPUs.

---

<span id="class_BaseMaterial3D_property_normal_scale"></span>

[float](class_float.md#class_float) **normal_scale** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_normal_scale)

- void **set_normal_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_normal_scale** ( )

The strength of the normal map's effect.

---

<span id="class_BaseMaterial3D_property_normal_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **normal_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_normal_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture used to specify the normal at a given pixel. The [normal_texture](class_basematerial3d.md#class_BaseMaterial3D_property_normal_texture) only uses the red and green channels; the blue and alpha channels are ignored. The normal read from [normal_texture](class_basematerial3d.md#class_BaseMaterial3D_property_normal_texture) is oriented around the surface normal provided by the [Mesh](class_mesh.md#class_Mesh).

 **Note:** The mesh must have both normals and tangents defined in its vertex data. Otherwise, the normal map won't render correctly and will only appear to darken the whole surface. If creating geometry with [SurfaceTool](class_surfacetool.md#class_SurfaceTool), you can use [SurfaceTool.generate_normals()](class_surfacetool.md#class_SurfaceTool_method_generate_normals) and [SurfaceTool.generate_tangents()](class_surfacetool.md#class_SurfaceTool_method_generate_tangents) to automatically generate normals and tangents respectively.

 **Note:** Godot expects the normal map to use X+, Y+, and Z+ coordinates. See this page for a comparison of normal map coordinates expected by popular engines.

 **Note:** If [detail_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_detail_enabled) is `true`, the [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo) texture is drawn *below* the [normal_texture](class_basematerial3d.md#class_BaseMaterial3D_property_normal_texture). To display a normal map *above* the [detail_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_detail_albedo) texture, use [detail_normal](class_basematerial3d.md#class_BaseMaterial3D_property_detail_normal) instead.

---

<span id="class_BaseMaterial3D_property_orm_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **orm_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_orm_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

The Occlusion/Roughness/Metallic texture to use. This is a more efficient replacement of [ao_texture](class_basematerial3d.md#class_BaseMaterial3D_property_ao_texture), [roughness_texture](class_basematerial3d.md#class_BaseMaterial3D_property_roughness_texture) and [metallic_texture](class_basematerial3d.md#class_BaseMaterial3D_property_metallic_texture) in [ORMMaterial3D](class_ormmaterial3d.md#class_ORMMaterial3D). Ambient occlusion is stored in the red channel. Roughness map is stored in the green channel. Metallic map is stored in the blue channel. The alpha channel is ignored.

---

<span id="class_BaseMaterial3D_property_particles_anim_h_frames"></span>

[int](class_int.md#class_int) **particles_anim_h_frames** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_particles_anim_h_frames)

- void **set_particles_anim_h_frames** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_particles_anim_h_frames** ( )

The number of horizontal frames in the particle sprite sheet. Only enabled when using [BILLBOARD_PARTICLES](class_basematerial3d.md#class_BaseMaterial3D_constant_BILLBOARD_PARTICLES). See [billboard_mode](class_basematerial3d.md#class_BaseMaterial3D_property_billboard_mode).

---

<span id="class_BaseMaterial3D_property_particles_anim_loop"></span>

[bool](class_bool.md#class_bool) **particles_anim_loop** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_particles_anim_loop)

- void **set_particles_anim_loop** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particles_anim_loop** ( )

If `true`, particle animations are looped. Only enabled when using [BILLBOARD_PARTICLES](class_basematerial3d.md#class_BaseMaterial3D_constant_BILLBOARD_PARTICLES). See [billboard_mode](class_basematerial3d.md#class_BaseMaterial3D_property_billboard_mode).

---

<span id="class_BaseMaterial3D_property_particles_anim_v_frames"></span>

[int](class_int.md#class_int) **particles_anim_v_frames** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_particles_anim_v_frames)

- void **set_particles_anim_v_frames** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_particles_anim_v_frames** ( )

The number of vertical frames in the particle sprite sheet. Only enabled when using [BILLBOARD_PARTICLES](class_basematerial3d.md#class_BaseMaterial3D_constant_BILLBOARD_PARTICLES). See [billboard_mode](class_basematerial3d.md#class_BaseMaterial3D_property_billboard_mode).

---

<span id="class_BaseMaterial3D_property_point_size"></span>

[float](class_float.md#class_float) **point_size** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_point_size)

- void **set_point_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_point_size** ( )

The point size in pixels. See [use_point_size](class_basematerial3d.md#class_BaseMaterial3D_property_use_point_size).

---

<span id="class_BaseMaterial3D_property_proximity_fade_distance"></span>

[float](class_float.md#class_float) **proximity_fade_distance** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_proximity_fade_distance)

- void **set_proximity_fade_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_proximity_fade_distance** ( )

Distance over which the fade effect takes place. The larger the distance the longer it takes for an object to fade.

---

<span id="class_BaseMaterial3D_property_proximity_fade_enabled"></span>

[bool](class_bool.md#class_bool) **proximity_fade_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_proximity_fade_enabled)

- void **set_proximity_fade_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_proximity_fade_enabled** ( )

If `true`, the proximity fade effect is enabled. The proximity fade effect fades out each pixel based on its distance to another object.

---

<span id="class_BaseMaterial3D_property_refraction_enabled"></span>

[bool](class_bool.md#class_bool) **refraction_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, the refraction effect is enabled. Distorts transparency based on light from behind the object.

 **Note:** Refraction is implemented using the screen texture. Only opaque materials will appear in the refraction, since transparent materials do not appear in the screen texture.

---

<span id="class_BaseMaterial3D_property_refraction_scale"></span>

[float](class_float.md#class_float) **refraction_scale** = `0.05` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_scale)

- void **set_refraction** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_refraction** ( )

The strength of the refraction effect.

---

<span id="class_BaseMaterial3D_property_refraction_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **refraction_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture that controls the strength of the refraction per-pixel. Multiplied by [refraction_scale](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_scale).

---

<span id="class_BaseMaterial3D_property_refraction_texture_channel"></span>

[TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **refraction_texture_channel** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_texture_channel)

- void **set_refraction_texture_channel** ( value: [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) )
- [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **get_refraction_texture_channel** ( )

Specifies the channel of the [refraction_texture](class_basematerial3d.md#class_BaseMaterial3D_property_refraction_texture) in which the refraction information is stored. This is useful when you store the information for multiple effects in a single texture. For example if you stored refraction in the red channel, roughness in the blue, and ambient occlusion in the green you could reduce the number of textures you use.

---

<span id="class_BaseMaterial3D_property_rim"></span>

[float](class_float.md#class_float) **rim** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_rim)

- void **set_rim** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_rim** ( )

Sets the strength of the rim lighting effect.

---

<span id="class_BaseMaterial3D_property_rim_enabled"></span>

[bool](class_bool.md#class_bool) **rim_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_rim_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, rim effect is enabled. Rim lighting increases the brightness at glancing angles on an object.

 **Note:** Rim lighting is not visible if the material's [shading_mode](class_basematerial3d.md#class_BaseMaterial3D_property_shading_mode) is [SHADING_MODE_UNSHADED](class_basematerial3d.md#class_BaseMaterial3D_constant_SHADING_MODE_UNSHADED).

---

<span id="class_BaseMaterial3D_property_rim_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **rim_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_rim_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture used to set the strength of the rim lighting effect per-pixel. Multiplied by [rim](class_basematerial3d.md#class_BaseMaterial3D_property_rim).

---

<span id="class_BaseMaterial3D_property_rim_tint"></span>

[float](class_float.md#class_float) **rim_tint** = `0.5` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_rim_tint)

- void **set_rim_tint** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_rim_tint** ( )

The amount of to blend light and albedo color when rendering rim effect. If `0` the light color is used, while `1` means albedo color is used. An intermediate value generally works best.

---

<span id="class_BaseMaterial3D_property_roughness"></span>

[float](class_float.md#class_float) **roughness** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_roughness)

- void **set_roughness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_roughness** ( )

Surface reflection. A value of `0` represents a perfect mirror while a value of `1` completely blurs the reflection. See also [metallic](class_basematerial3d.md#class_BaseMaterial3D_property_metallic).

---

<span id="class_BaseMaterial3D_property_roughness_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **roughness_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_roughness_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture used to control the roughness per-pixel. Multiplied by [roughness](class_basematerial3d.md#class_BaseMaterial3D_property_roughness).

---

<span id="class_BaseMaterial3D_property_roughness_texture_channel"></span>

[TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **roughness_texture_channel** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_roughness_texture_channel)

- void **set_roughness_texture_channel** ( value: [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) )
- [TextureChannel](class_basematerial3d.md#enum_BaseMaterial3D_TextureChannel) **get_roughness_texture_channel** ( )

Specifies the channel of the [roughness_texture](class_basematerial3d.md#class_BaseMaterial3D_property_roughness_texture) in which the roughness information is stored. This is useful when you store the information for multiple effects in a single texture. For example if you stored metallic in the red channel, roughness in the blue, and ambient occlusion in the green you could reduce the number of textures you use.

---

<span id="class_BaseMaterial3D_property_shading_mode"></span>

[ShadingMode](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode) **shading_mode** = `1` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_shading_mode)

- void **set_shading_mode** ( value: [ShadingMode](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode) )
- [ShadingMode](class_basematerial3d.md#enum_BaseMaterial3D_ShadingMode) **get_shading_mode** ( )

Sets whether the shading takes place, per-pixel, per-vertex or unshaded. Per-vertex lighting is faster, making it the best choice for mobile applications, however it looks considerably worse than per-pixel. Unshaded rendering is the fastest, but disables all interactions with lights.

---

<span id="class_BaseMaterial3D_property_shadow_to_opacity"></span>

[bool](class_bool.md#class_bool) **shadow_to_opacity** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_shadow_to_opacity)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, enables the "shadow to opacity" render mode where lighting modifies the alpha so shadowed areas are opaque and non-shadowed areas are transparent. Useful for overlaying shadows onto a camera feed in AR.

---

<span id="class_BaseMaterial3D_property_specular_mode"></span>

[SpecularMode](class_basematerial3d.md#enum_BaseMaterial3D_SpecularMode) **specular_mode** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_specular_mode)

- void **set_specular_mode** ( value: [SpecularMode](class_basematerial3d.md#enum_BaseMaterial3D_SpecularMode) )
- [SpecularMode](class_basematerial3d.md#enum_BaseMaterial3D_SpecularMode) **get_specular_mode** ( )

The method for rendering the specular blob.

 **Note:** [specular_mode](class_basematerial3d.md#class_BaseMaterial3D_property_specular_mode) only applies to the specular blob. It does not affect specular reflections from the sky, screen-space reflections, [VoxelGI](class_voxelgi.md#class_VoxelGI), SDFGI or [ReflectionProbe](class_reflectionprobe.md#class_ReflectionProbe) s. To disable reflections from these sources as well, set [metallic_specular](class_basematerial3d.md#class_BaseMaterial3D_property_metallic_specular) to `0.0` instead.

---

<span id="class_BaseMaterial3D_property_stencil_color"></span>

[Color](class_color.md#class_Color) **stencil_color** = `Color(0, 0, 0, 1)` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_color)

- void **set_stencil_effect_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_stencil_effect_color** ( )

**Experimental:** May be affected by future rendering pipeline changes.

The primary color of the stencil effect.

---

<span id="class_BaseMaterial3D_property_stencil_compare"></span>

[StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) **stencil_compare** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_compare)

- void **set_stencil_compare** ( value: [StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) )
- [StencilCompare](class_basematerial3d.md#enum_BaseMaterial3D_StencilCompare) **get_stencil_compare** ( )

**Experimental:** May be affected by future rendering pipeline changes.

The comparison operator to use for stencil masking operations.

---

<span id="class_BaseMaterial3D_property_stencil_flags"></span>

[int](class_int.md#class_int) **stencil_flags** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_flags)

- void **set_stencil_flags** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_stencil_flags** ( )

**Experimental:** May be affected by future rendering pipeline changes.

The flags dictating how the stencil operation behaves.

---

<span id="class_BaseMaterial3D_property_stencil_mode"></span>

[StencilMode](class_basematerial3d.md#enum_BaseMaterial3D_StencilMode) **stencil_mode** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_mode)

- void **set_stencil_mode** ( value: [StencilMode](class_basematerial3d.md#enum_BaseMaterial3D_StencilMode) )
- [StencilMode](class_basematerial3d.md#enum_BaseMaterial3D_StencilMode) **get_stencil_mode** ( )

**Experimental:** May be affected by future rendering pipeline changes.

The stencil effect mode.

---

<span id="class_BaseMaterial3D_property_stencil_outline_thickness"></span>

[float](class_float.md#class_float) **stencil_outline_thickness** = `0.01` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_outline_thickness)

- void **set_stencil_effect_outline_thickness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_stencil_effect_outline_thickness** ( )

**Experimental:** May be affected by future rendering pipeline changes.

The outline thickness for [STENCIL_MODE_OUTLINE](class_basematerial3d.md#class_BaseMaterial3D_constant_STENCIL_MODE_OUTLINE).

---

<span id="class_BaseMaterial3D_property_stencil_reference"></span>

[int](class_int.md#class_int) **stencil_reference** = `1` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_stencil_reference)

- void **set_stencil_reference** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_stencil_reference** ( )

**Experimental:** May be affected by future rendering pipeline changes.

The stencil reference value (0-255). Typically a power of 2.

---

<span id="class_BaseMaterial3D_property_subsurf_scatter_enabled"></span>

[bool](class_bool.md#class_bool) **subsurf_scatter_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, subsurface scattering is enabled. Emulates light that penetrates an object's surface, is scattered, and then emerges. Subsurface scattering quality is controlled by ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_quality.

 **Note:** Subsurface scattering is not supported on viewports that have a transparent background (where [Viewport.transparent_bg](class_viewport.md#class_Viewport_property_transparent_bg) is `true`).

---

<span id="class_BaseMaterial3D_property_subsurf_scatter_skin_mode"></span>

[bool](class_bool.md#class_bool) **subsurf_scatter_skin_mode** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_skin_mode)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, subsurface scattering will use a special mode optimized for the color and density of human skin, such as boosting the intensity of the red channel in subsurface scattering.

---

<span id="class_BaseMaterial3D_property_subsurf_scatter_strength"></span>

[float](class_float.md#class_float) **subsurf_scatter_strength** = `0.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_strength)

- void **set_subsurface_scattering_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_subsurface_scattering_strength** ( )

The strength of the subsurface scattering effect. The depth of the effect is also controlled by ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_scale, which is set globally.

---

<span id="class_BaseMaterial3D_property_subsurf_scatter_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **subsurf_scatter_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

Texture used to control the subsurface scattering strength. Stored in the red texture channel. Multiplied by [subsurf_scatter_strength](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_strength).

---

<span id="class_BaseMaterial3D_property_subsurf_scatter_transmittance_boost"></span>

[float](class_float.md#class_float) **subsurf_scatter_transmittance_boost** = `0.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_boost)

- void **set_transmittance_boost** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_transmittance_boost** ( )

The intensity of the subsurface scattering transmittance effect.

---

<span id="class_BaseMaterial3D_property_subsurf_scatter_transmittance_color"></span>

[Color](class_color.md#class_Color) **subsurf_scatter_transmittance_color** = `Color(1, 1, 1, 1)` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_color)

- void **set_transmittance_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_transmittance_color** ( )

The color to multiply the subsurface scattering transmittance effect with. Ignored if [subsurf_scatter_skin_mode](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_skin_mode) is `true`.

---

<span id="class_BaseMaterial3D_property_subsurf_scatter_transmittance_depth"></span>

[float](class_float.md#class_float) **subsurf_scatter_transmittance_depth** = `0.1` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_depth)

- void **set_transmittance_depth** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_transmittance_depth** ( )

The depth of the subsurface scattering transmittance effect.

---

<span id="class_BaseMaterial3D_property_subsurf_scatter_transmittance_enabled"></span>

[bool](class_bool.md#class_bool) **subsurf_scatter_transmittance_enabled** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_enabled)

- void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const*

If `true`, enables subsurface scattering transmittance. Only effective if [subsurf_scatter_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_enabled) is `true`. See also [backlight_enabled](class_basematerial3d.md#class_BaseMaterial3D_property_backlight_enabled).

---

<span id="class_BaseMaterial3D_property_subsurf_scatter_transmittance_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **subsurf_scatter_transmittance_texture** [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_transmittance_texture)

- void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const*

The texture to use for multiplying the intensity of the subsurface scattering transmittance intensity. See also [subsurf_scatter_texture](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_texture). Ignored if [subsurf_scatter_skin_mode](class_basematerial3d.md#class_BaseMaterial3D_property_subsurf_scatter_skin_mode) is `true`.

---

<span id="class_BaseMaterial3D_property_texture_filter"></span>

[TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **texture_filter** = `3` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_texture_filter)

- void **set_texture_filter** ( value: [TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) )
- [TextureFilter](class_basematerial3d.md#enum_BaseMaterial3D_TextureFilter) **get_texture_filter** ( )

Filter flags for the texture.

 **Note:** [heightmap_texture](class_basematerial3d.md#class_BaseMaterial3D_property_heightmap_texture) is always sampled with linear filtering, even if nearest-neighbor filtering is selected here. This is to ensure the heightmap effect looks as intended. If you need sharper height transitions between pixels, resize the heightmap texture in an image editor with nearest-neighbor filtering.

---

<span id="class_BaseMaterial3D_property_texture_repeat"></span>

[bool](class_bool.md#class_bool) **texture_repeat** = `true` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_texture_repeat)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, the texture repeats when exceeding the texture's size. See [FLAG_USE_TEXTURE_REPEAT](class_basematerial3d.md#class_BaseMaterial3D_constant_FLAG_USE_TEXTURE_REPEAT).

---

<span id="class_BaseMaterial3D_property_transparency"></span>

[Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) **transparency** = `0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_transparency)

- void **set_transparency** ( value: [Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) )
- [Transparency](class_basematerial3d.md#enum_BaseMaterial3D_Transparency) **get_transparency** ( )

The material's transparency mode. Some transparency modes will disable shadow casting. Any transparency mode other than [TRANSPARENCY_DISABLED](class_basematerial3d.md#class_BaseMaterial3D_constant_TRANSPARENCY_DISABLED) has a greater performance impact compared to opaque rendering. See also [blend_mode](class_basematerial3d.md#class_BaseMaterial3D_property_blend_mode).

---

<span id="class_BaseMaterial3D_property_use_fov_override"></span>

[bool](class_bool.md#class_bool) **use_fov_override** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_use_fov_override)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true` use [fov_override](class_basematerial3d.md#class_BaseMaterial3D_property_fov_override) to override the [Camera3D](class_camera3d.md#class_Camera3D)'s field of view angle.

---

<span id="class_BaseMaterial3D_property_use_particle_trails"></span>

[bool](class_bool.md#class_bool) **use_particle_trails** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_use_particle_trails)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, enables parts of the shader required for [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) trails to function. This also requires using a mesh with appropriate skinning, such as [RibbonTrailMesh](class_ribbontrailmesh.md#class_RibbonTrailMesh) or [TubeTrailMesh](class_tubetrailmesh.md#class_TubeTrailMesh). Enabling this feature outside of materials used in [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) meshes will break material rendering.

---

<span id="class_BaseMaterial3D_property_use_point_size"></span>

[bool](class_bool.md#class_bool) **use_point_size** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_use_point_size)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, render point size can be changed.

 **Note:** This is only effective for objects whose geometry is point-based rather than triangle-based. See also [point_size](class_basematerial3d.md#class_BaseMaterial3D_property_point_size).

---

<span id="class_BaseMaterial3D_property_use_z_clip_scale"></span>

[bool](class_bool.md#class_bool) **use_z_clip_scale** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_use_z_clip_scale)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true` use [z_clip_scale](class_basematerial3d.md#class_BaseMaterial3D_property_z_clip_scale) to scale the object being rendered towards the camera to avoid clipping into things like walls.

---

<span id="class_BaseMaterial3D_property_uv1_offset"></span>

[Vector3](class_vector3.md#class_Vector3) **uv1_offset** = `Vector3(0, 0, 0)` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_offset)

- void **set_uv1_offset** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_uv1_offset** ( )

How much to offset the `UV` coordinates. This amount will be added to `UV` in the vertex function. This can be used to offset a texture. The Z component is used when [uv1_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_triplanar) is enabled, but it is not used anywhere else.

---

<span id="class_BaseMaterial3D_property_uv1_scale"></span>

[Vector3](class_vector3.md#class_Vector3) **uv1_scale** = `Vector3(1, 1, 1)` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_scale)

- void **set_uv1_scale** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_uv1_scale** ( )

How much to scale the `UV` coordinates. This is multiplied by `UV` in the vertex function. The Z component is used when [uv1_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_triplanar) is enabled, but it is not used anywhere else.

---

<span id="class_BaseMaterial3D_property_uv1_triplanar"></span>

[bool](class_bool.md#class_bool) **uv1_triplanar** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_triplanar)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, instead of using `UV` textures will use a triplanar texture lookup to determine how to apply textures. Triplanar uses the orientation of the object's surface to blend between texture coordinates. It reads from the source texture 3 times, once for each axis and then blends between the results based on how closely the pixel aligns with each axis. This is often used for natural features to get a realistic blend of materials. Because triplanar texturing requires many more texture reads per-pixel it is much slower than normal UV texturing. Additionally, because it is blending the texture between the three axes, it is unsuitable when you are trying to achieve crisp texturing.

---

<span id="class_BaseMaterial3D_property_uv1_triplanar_sharpness"></span>

[float](class_float.md#class_float) **uv1_triplanar_sharpness** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_triplanar_sharpness)

- void **set_uv1_triplanar_blend_sharpness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_uv1_triplanar_blend_sharpness** ( )

A lower number blends the texture more softly while a higher number blends the texture more sharply.

 **Note:** [uv1_triplanar_sharpness](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_triplanar_sharpness) is clamped between `0.0` and `150.0` (inclusive) as values outside that range can look broken depending on the mesh.

---

<span id="class_BaseMaterial3D_property_uv1_world_triplanar"></span>

[bool](class_bool.md#class_bool) **uv1_world_triplanar** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_world_triplanar)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, triplanar mapping for `UV` is calculated in world space rather than object local space. See also [uv1_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv1_triplanar).

---

<span id="class_BaseMaterial3D_property_uv2_offset"></span>

[Vector3](class_vector3.md#class_Vector3) **uv2_offset** = `Vector3(0, 0, 0)` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_offset)

- void **set_uv2_offset** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_uv2_offset** ( )

How much to offset the `UV2` coordinates. This amount will be added to `UV2` in the vertex function. This can be used to offset a texture. The Z component is used when [uv2_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_triplanar) is enabled, but it is not used anywhere else.

---

<span id="class_BaseMaterial3D_property_uv2_scale"></span>

[Vector3](class_vector3.md#class_Vector3) **uv2_scale** = `Vector3(1, 1, 1)` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_scale)

- void **set_uv2_scale** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_uv2_scale** ( )

How much to scale the `UV2` coordinates. This is multiplied by `UV2` in the vertex function. The Z component is used when [uv2_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_triplanar) is enabled, but it is not used anywhere else.

---

<span id="class_BaseMaterial3D_property_uv2_triplanar"></span>

[bool](class_bool.md#class_bool) **uv2_triplanar** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_triplanar)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, instead of using `UV2` textures will use a triplanar texture lookup to determine how to apply textures. Triplanar uses the orientation of the object's surface to blend between texture coordinates. It reads from the source texture 3 times, once for each axis and then blends between the results based on how closely the pixel aligns with each axis. This is often used for natural features to get a realistic blend of materials. Because triplanar texturing requires many more texture reads per-pixel it is much slower than normal UV texturing. Additionally, because it is blending the texture between the three axes, it is unsuitable when you are trying to achieve crisp texturing.

---

<span id="class_BaseMaterial3D_property_uv2_triplanar_sharpness"></span>

[float](class_float.md#class_float) **uv2_triplanar_sharpness** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_triplanar_sharpness)

- void **set_uv2_triplanar_blend_sharpness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_uv2_triplanar_blend_sharpness** ( )

A lower number blends the texture more softly while a higher number blends the texture more sharply.

 **Note:** [uv2_triplanar_sharpness](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_triplanar_sharpness) is clamped between `0.0` and `150.0` (inclusive) as values outside that range can look broken depending on the mesh.

---

<span id="class_BaseMaterial3D_property_uv2_world_triplanar"></span>

[bool](class_bool.md#class_bool) **uv2_world_triplanar** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_world_triplanar)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, triplanar mapping for `UV2` is calculated in world space rather than object local space. See also [uv2_triplanar](class_basematerial3d.md#class_BaseMaterial3D_property_uv2_triplanar).

---

<span id="class_BaseMaterial3D_property_vertex_color_is_srgb"></span>

[bool](class_bool.md#class_bool) **vertex_color_is_srgb** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_is_srgb)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, vertex colors are considered to be stored in nonlinear sRGB encoding and are converted to linear encoding during rendering. If `false`, vertex colors are considered to be stored in linear encoding and are rendered as-is. See also [albedo_texture_force_srgb](class_basematerial3d.md#class_BaseMaterial3D_property_albedo_texture_force_srgb).

 **Note:** Only effective when using the Forward+ and Mobile rendering methods, not Compatibility.

---

<span id="class_BaseMaterial3D_property_vertex_color_use_as_albedo"></span>

[bool](class_bool.md#class_bool) **vertex_color_use_as_albedo** = `false` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo)

- void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const*

If `true`, the vertex color is used as albedo color.

---

<span id="class_BaseMaterial3D_property_z_clip_scale"></span>

[float](class_float.md#class_float) **z_clip_scale** = `1.0` [🔗](class_basematerial3d.md#class_BaseMaterial3D_property_z_clip_scale)

- void **set_z_clip_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_z_clip_scale** ( )

Scales the object being rendered towards the camera to avoid clipping into things like walls. This is intended to be used for objects that are fixed with respect to the camera like player arms, tools, etc. Lighting and shadows will continue to work correctly when this setting is adjusted, but screen-space effects like SSAO and SSR may break with lower scales. Therefore, try to keep this setting as close to `1.0` as possible.

---

### Method Descriptions

<span id="class_BaseMaterial3D_method_get_feature"></span>

[bool](class_bool.md#class_bool) **get_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature) ) *const* [🔗](class_basematerial3d.md#class_BaseMaterial3D_method_get_feature)

Returns `true` if the specified `feature` is enabled.

---

<span id="class_BaseMaterial3D_method_get_flag"></span>

[bool](class_bool.md#class_bool) **get_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags) ) *const* [🔗](class_basematerial3d.md#class_BaseMaterial3D_method_get_flag)

Returns `true` if the specified `flag` is enabled.

---

<span id="class_BaseMaterial3D_method_get_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam) ) *const* [🔗](class_basematerial3d.md#class_BaseMaterial3D_method_get_texture)

Returns the [Texture2D](class_texture2d.md#class_Texture2D) associated with the specified texture `param`.

---

<span id="class_BaseMaterial3D_method_set_feature"></span>

void **set_feature** ( feature: [Feature](class_basematerial3d.md#enum_BaseMaterial3D_Feature), enable: [bool](class_bool.md#class_bool) ) [🔗](class_basematerial3d.md#class_BaseMaterial3D_method_set_feature)

If `enable` is `true`, enables the specified `feature`. Many features that are available in **BaseMaterial3D** need to be enabled before use. This way, the cost for using the feature is only incurred when specified. Features can also be enabled by setting their corresponding property to `true`.

---

<span id="class_BaseMaterial3D_method_set_flag"></span>

void **set_flag** ( flag: [Flags](class_basematerial3d.md#enum_BaseMaterial3D_Flags), enable: [bool](class_bool.md#class_bool) ) [🔗](class_basematerial3d.md#class_BaseMaterial3D_method_set_flag)

If `enable` is `true`, enables the specified `flag`. Flags are optional behavior that can be turned on and off. Only one flag can be enabled at a time with this function, the flag enumerators cannot be bit-masked together to enable or disable multiple flags at once. Flags can also be enabled by setting their corresponding property to `true`.

---

<span id="class_BaseMaterial3D_method_set_texture"></span>

void **set_texture** ( param: [TextureParam](class_basematerial3d.md#enum_BaseMaterial3D_TextureParam), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_basematerial3d.md#class_BaseMaterial3D_method_set_texture)

Sets the texture for the slot specified by `param`.
