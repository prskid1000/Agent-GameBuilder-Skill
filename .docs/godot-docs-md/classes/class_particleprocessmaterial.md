<span id="class_ParticleProcessMaterial"></span>

## ParticleProcessMaterial

**Inherits:** [Material](class_material.md#class_Material) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Holds a particle configuration for [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) or [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes.

### Description

**ParticleProcessMaterial** defines particle properties and behavior. It is used in the `process_material` of the [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) and [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes. Some of this material's properties are applied to each particle when emitted, while others can have a [CurveTexture](class_curvetexture.md#class_CurveTexture) or a [GradientTexture1D](class_gradienttexture1d.md#class_GradientTexture1D) applied to vary numerical or color values over the lifetime of the particle.

### Properties


| [Texture2D](class_texture2d.md#class_Texture2D) | [alpha_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_alpha_curve) |
| --- | --- |
| [Texture2D](class_texture2d.md#class_Texture2D) | [angle_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angle_curve) |
| [float](class_float.md#class_float) | [angle_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angle_max) | `0.0` |
| [float](class_float.md#class_float) | [angle_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angle_min) | `0.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [angular_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angular_velocity_curve) |
| [float](class_float.md#class_float) | [angular_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angular_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [angular_velocity_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angular_velocity_min) | `0.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [anim_offset_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_offset_curve) |
| [float](class_float.md#class_float) | [anim_offset_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_offset_max) | `0.0` |
| [float](class_float.md#class_float) | [anim_offset_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_offset_min) | `0.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [anim_speed_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_speed_curve) |
| [float](class_float.md#class_float) | [anim_speed_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_speed_max) | `0.0` |
| [float](class_float.md#class_float) | [anim_speed_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_speed_min) | `0.0` |
| [bool](class_bool.md#class_bool) | [attractor_interaction_enabled](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_attractor_interaction_enabled) | `true` |
| [float](class_float.md#class_float) | [collision_bounce](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_bounce) |
| [float](class_float.md#class_float) | [collision_friction](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_friction) |
| [CollisionMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode) | [collision_mode](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_mode) | `0` |
| [bool](class_bool.md#class_bool) | [collision_use_scale](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_use_scale) | `false` |
| [Color](class_color.md#class_Color) | [color](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color) | `Color(1, 1, 1, 1)` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [color_initial_ramp](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color_initial_ramp) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [color_ramp](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color_ramp) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [damping_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_damping_curve) |
| [float](class_float.md#class_float) | [damping_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_damping_max) | `0.0` |
| [float](class_float.md#class_float) | [damping_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_damping_min) | `0.0` |
| [Vector3](class_vector3.md#class_Vector3) | [direction](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_direction) | `Vector3(1, 0, 0)` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [directional_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_directional_velocity_curve) |
| [float](class_float.md#class_float) | [directional_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_directional_velocity_max) |
| [float](class_float.md#class_float) | [directional_velocity_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_directional_velocity_min) |
| [Vector3](class_vector3.md#class_Vector3) | [emission_box_extents](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_box_extents) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [emission_color_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_color_texture) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [emission_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_curve) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [emission_normal_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_normal_texture) |
| [int](class_int.md#class_int) | [emission_point_count](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_point_count) |
| [Texture2D](class_texture2d.md#class_Texture2D) | [emission_point_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_point_texture) |
| [Vector3](class_vector3.md#class_Vector3) | [emission_ring_axis](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_axis) |
| [float](class_float.md#class_float) | [emission_ring_cone_angle](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_cone_angle) |
| [float](class_float.md#class_float) | [emission_ring_height](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_height) |
| [float](class_float.md#class_float) | [emission_ring_inner_radius](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_inner_radius) |
| [float](class_float.md#class_float) | [emission_ring_radius](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_radius) |
| [EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) | [emission_shape](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape) | `0` |
| [Vector3](class_vector3.md#class_Vector3) | [emission_shape_offset](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape_offset) | `Vector3(0, 0, 0)` |
| [Vector3](class_vector3.md#class_Vector3) | [emission_shape_scale](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape_scale) | `Vector3(1, 1, 1)` |
| [float](class_float.md#class_float) | [emission_sphere_radius](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_sphere_radius) |
| [float](class_float.md#class_float) | [flatness](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_flatness) | `0.0` |
| [Vector3](class_vector3.md#class_Vector3) | [gravity](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_gravity) | `Vector3(0, -9.8, 0)` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [hue_variation_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_hue_variation_curve) |
| [float](class_float.md#class_float) | [hue_variation_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_hue_variation_max) | `0.0` |
| [float](class_float.md#class_float) | [hue_variation_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_hue_variation_min) | `0.0` |
| [float](class_float.md#class_float) | [inherit_velocity_ratio](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_inherit_velocity_ratio) | `0.0` |
| [float](class_float.md#class_float) | [initial_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_initial_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [initial_velocity_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_initial_velocity_min) | `0.0` |
| [float](class_float.md#class_float) | [lifetime_randomness](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_lifetime_randomness) | `0.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [linear_accel_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_linear_accel_curve) |
| [float](class_float.md#class_float) | [linear_accel_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_linear_accel_max) | `0.0` |
| [float](class_float.md#class_float) | [linear_accel_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_linear_accel_min) | `0.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [orbit_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_orbit_velocity_curve) |
| [float](class_float.md#class_float) | [orbit_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_orbit_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [orbit_velocity_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_orbit_velocity_min) | `0.0` |
| [bool](class_bool.md#class_bool) | [particle_flag_align_y](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_align_y) | `false` |
| [bool](class_bool.md#class_bool) | [particle_flag_damping_as_friction](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_damping_as_friction) | `false` |
| [bool](class_bool.md#class_bool) | [particle_flag_disable_z](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_disable_z) | `false` |
| [bool](class_bool.md#class_bool) | [particle_flag_rotate_y](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_rotate_y) | `false` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [radial_accel_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_accel_curve) |
| [float](class_float.md#class_float) | [radial_accel_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_accel_max) | `0.0` |
| [float](class_float.md#class_float) | [radial_accel_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_accel_min) | `0.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [radial_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_velocity_curve) |
| [float](class_float.md#class_float) | [radial_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [radial_velocity_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_velocity_min) | `0.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [scale_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_curve) |
| [float](class_float.md#class_float) | [scale_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_max) | `1.0` |
| [float](class_float.md#class_float) | [scale_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_min) | `1.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [scale_over_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_curve) |
| [float](class_float.md#class_float) | [scale_over_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [scale_over_velocity_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_min) | `0.0` |
| [float](class_float.md#class_float) | [spread](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_spread) | `45.0` |
| [int](class_int.md#class_int) | [sub_emitter_amount_at_collision](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_amount_at_collision) |
| [int](class_int.md#class_int) | [sub_emitter_amount_at_end](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_amount_at_end) |
| [int](class_int.md#class_int) | [sub_emitter_amount_at_start](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_amount_at_start) |
| [float](class_float.md#class_float) | [sub_emitter_frequency](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_frequency) |
| [bool](class_bool.md#class_bool) | [sub_emitter_keep_velocity](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_keep_velocity) | `false` |
| [SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) | [sub_emitter_mode](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_mode) | `0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [tangential_accel_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_tangential_accel_curve) |
| [float](class_float.md#class_float) | [tangential_accel_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_tangential_accel_max) | `0.0` |
| [float](class_float.md#class_float) | [tangential_accel_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_tangential_accel_min) | `0.0` |
| [bool](class_bool.md#class_bool) | [turbulence_enabled](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_enabled) | `false` |
| [float](class_float.md#class_float) | [turbulence_influence_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_max) | `0.1` |
| [float](class_float.md#class_float) | [turbulence_influence_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_min) | `0.1` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [turbulence_influence_over_life](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_over_life) |
| [float](class_float.md#class_float) | [turbulence_initial_displacement_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_initial_displacement_max) | `0.0` |
| [float](class_float.md#class_float) | [turbulence_initial_displacement_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_initial_displacement_min) | `0.0` |
| [float](class_float.md#class_float) | [turbulence_noise_scale](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_noise_scale) | `9.0` |
| [Vector3](class_vector3.md#class_Vector3) | [turbulence_noise_speed](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_noise_speed) | `Vector3(0, 0, 0)` |
| [float](class_float.md#class_float) | [turbulence_noise_speed_random](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_noise_speed_random) | `0.2` |
| [float](class_float.md#class_float) | [turbulence_noise_strength](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_noise_strength) | `1.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) |
| [Vector3](class_vector3.md#class_Vector3) | [velocity_pivot](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_pivot) | `Vector3(0, 0, 0)` |

### Methods


| [Vector2](class_vector2.md#class_Vector2) | [get_param](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_param) ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) const |
| --- | --- |
| [float](class_float.md#class_float) | [get_param_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_param_max) ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) const |
| [float](class_float.md#class_float) | [get_param_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_param_min) ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_param_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_param_texture) ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) const |
| [bool](class_bool.md#class_bool) | [get_particle_flag](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_particle_flag) ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) ) const |
| void | [set_param](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param) ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_param_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max) ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) ) |
| void | [set_param_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min) ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) ) |
| void | [set_param_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_particle_flag](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_particle_flag) ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags), enable: [bool](class_bool.md#class_bool) ) |

---

### Signals

<span id="class_ParticleProcessMaterial_signal_emission_shape_changed"></span>

**emission_shape_changed** ( ) [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_signal_emission_shape_changed)

Emitted when this material's emission shape is changed in any way. This includes changes to [emission_shape](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape), [emission_shape_scale](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape_scale), or [emission_sphere_radius](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_sphere_radius), and any other property that affects the emission shape's offset, size, scale, or orientation.

 **Note:** This signal is only emitted inside the editor for performance reasons.

---

### Enumerations

<span id="enum_ParticleProcessMaterial_Parameter"></span>

enum **Parameter**: [🔗](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter)

<span id="class_ParticleProcessMaterial_constant_PARAM_INITIAL_LINEAR_VELOCITY"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set initial velocity properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_ANGULAR_VELOCITY"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_ANGULAR_VELOCITY** = `1`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set angular velocity properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_ORBIT_VELOCITY"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_ORBIT_VELOCITY** = `2`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set orbital velocity properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_LINEAR_ACCEL"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_LINEAR_ACCEL** = `3`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set linear acceleration properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_RADIAL_ACCEL"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_RADIAL_ACCEL** = `4`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set radial acceleration properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_TANGENTIAL_ACCEL"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_TANGENTIAL_ACCEL** = `5`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set tangential acceleration properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_DAMPING"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_DAMPING** = `6`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set damping properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_ANGLE"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_ANGLE** = `7`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set angle properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_SCALE"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_SCALE** = `8`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set scale properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_HUE_VARIATION"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_HUE_VARIATION** = `9`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set hue variation properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_ANIM_SPEED"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_ANIM_SPEED** = `10`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set animation speed properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_ANIM_OFFSET"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_ANIM_OFFSET** = `11`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set animation offset properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_RADIAL_VELOCITY"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_RADIAL_VELOCITY** = `15`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set radial velocity properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_DIRECTIONAL_VELOCITY"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_DIRECTIONAL_VELOCITY** = `16`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set directional velocity properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_SCALE_OVER_VELOCITY"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_SCALE_OVER_VELOCITY** = `17`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min), [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max), and [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set scale over velocity properties.

<span id="class_ParticleProcessMaterial_constant_PARAM_MAX"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_MAX** = `18`

Represents the size of the [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) enum.

<span id="class_ParticleProcessMaterial_constant_PARAM_TURB_VEL_INFLUENCE"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_TURB_VEL_INFLUENCE** = `13`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min) and [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max) to set the turbulence minimum und maximum influence on each particles velocity.

<span id="class_ParticleProcessMaterial_constant_PARAM_TURB_INIT_DISPLACEMENT"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_TURB_INIT_DISPLACEMENT** = `14`

Use with [set_param_min()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min) and [set_param_max()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max) to set the turbulence minimum and maximum displacement of the particles spawn position.

<span id="class_ParticleProcessMaterial_constant_PARAM_TURB_INFLUENCE_OVER_LIFE"></span>

[Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) **PARAM_TURB_INFLUENCE_OVER_LIFE** = `12`

Use with [set_param_texture()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture) to set the turbulence influence over the particles life time.

---

<span id="enum_ParticleProcessMaterial_ParticleFlags"></span>

enum **ParticleFlags**: [🔗](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags)

<span id="class_ParticleProcessMaterial_constant_PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY"></span>

[ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with [set_particle_flag()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_particle_flag) to set [particle_flag_align_y](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_align_y).

<span id="class_ParticleProcessMaterial_constant_PARTICLE_FLAG_ROTATE_Y"></span>

[ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) **PARTICLE_FLAG_ROTATE_Y** = `1`

Use with [set_particle_flag()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_particle_flag) to set [particle_flag_rotate_y](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_rotate_y).

<span id="class_ParticleProcessMaterial_constant_PARTICLE_FLAG_DISABLE_Z"></span>

[ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) **PARTICLE_FLAG_DISABLE_Z** = `2`

Use with [set_particle_flag()](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_particle_flag) to set [particle_flag_disable_z](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_disable_z).

<span id="class_ParticleProcessMaterial_constant_PARTICLE_FLAG_DAMPING_AS_FRICTION"></span>

[ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) **PARTICLE_FLAG_DAMPING_AS_FRICTION** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_ParticleProcessMaterial_constant_PARTICLE_FLAG_MAX"></span>

[ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) **PARTICLE_FLAG_MAX** = `4`

Represents the size of the [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) enum.

---

<span id="enum_ParticleProcessMaterial_EmissionShape"></span>

enum **EmissionShape**: [🔗](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape)

<span id="class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINT"></span>

[EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

<span id="class_ParticleProcessMaterial_constant_EMISSION_SHAPE_SPHERE"></span>

[EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere.

<span id="class_ParticleProcessMaterial_constant_EMISSION_SHAPE_SPHERE_SURFACE"></span>

[EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere.

<span id="class_ParticleProcessMaterial_constant_EMISSION_SHAPE_BOX"></span>

[EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **EMISSION_SHAPE_BOX** = `3`

Particles will be emitted in the volume of a box.

<span id="class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINTS"></span>

[EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position determined by sampling a random point on the [emission_point_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_point_texture). Particle color will be modulated by [emission_color_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_color_texture).

<span id="class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS"></span>

[EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position determined by sampling a random point on the [emission_point_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_point_texture). Particle velocity and rotation will be set based on [emission_normal_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_normal_texture). Particle color will be modulated by [emission_color_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_color_texture).

<span id="class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING"></span>

[EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in a ring or cylinder.

<span id="class_ParticleProcessMaterial_constant_EMISSION_SHAPE_MAX"></span>

[EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **EMISSION_SHAPE_MAX** = `7`

Represents the size of the [EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) enum.

---

<span id="enum_ParticleProcessMaterial_SubEmitterMode"></span>

enum **SubEmitterMode**: [🔗](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode)

<span id="class_ParticleProcessMaterial_constant_SUB_EMITTER_DISABLED"></span>

[SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) **SUB_EMITTER_DISABLED** = `0`

The subemitter is disabled.

<span id="class_ParticleProcessMaterial_constant_SUB_EMITTER_CONSTANT"></span>

[SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) **SUB_EMITTER_CONSTANT** = `1`

The submitter is emitted on the constant interval defined by [sub_emitter_frequency](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_frequency).

<span id="class_ParticleProcessMaterial_constant_SUB_EMITTER_AT_END"></span>

[SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) **SUB_EMITTER_AT_END** = `2`

The subemitter is emitted at the end of the particle's lifetime.

<span id="class_ParticleProcessMaterial_constant_SUB_EMITTER_AT_COLLISION"></span>

[SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) **SUB_EMITTER_AT_COLLISION** = `3`

The subemitter is emitted when the particle collides.

<span id="class_ParticleProcessMaterial_constant_SUB_EMITTER_AT_START"></span>

[SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) **SUB_EMITTER_AT_START** = `4`

The subemitter is emitted when the particle spawns.

<span id="class_ParticleProcessMaterial_constant_SUB_EMITTER_MAX"></span>

[SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) **SUB_EMITTER_MAX** = `5`

Represents the size of the [SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) enum.

---

<span id="enum_ParticleProcessMaterial_CollisionMode"></span>

enum **CollisionMode**: [🔗](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode)

<span id="class_ParticleProcessMaterial_constant_COLLISION_DISABLED"></span>

[CollisionMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode) **COLLISION_DISABLED** = `0`

No collision for particles. Particles will go through [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D) nodes.

<span id="class_ParticleProcessMaterial_constant_COLLISION_RIGID"></span>

[CollisionMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode) **COLLISION_RIGID** = `1`

[RigidBody3D](class_rigidbody3d.md#class_RigidBody3D)-style collision for particles using [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D) nodes.

<span id="class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT"></span>

[CollisionMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode) **COLLISION_HIDE_ON_CONTACT** = `2`

Hide particles instantly when colliding with a [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D) node. This can be combined with a subemitter that uses the [COLLISION_RIGID](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_COLLISION_RIGID) collision mode to "replace" the parent particle with the subemitter on impact.

<span id="class_ParticleProcessMaterial_constant_COLLISION_MAX"></span>

[CollisionMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode) **COLLISION_MAX** = `3`

Represents the size of the [CollisionMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode) enum.

---

### Property Descriptions

<span id="class_ParticleProcessMaterial_property_alpha_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **alpha_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_alpha_curve)

- void **set_alpha_curve** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_alpha_curve** ( )

The alpha value of each particle's color will be multiplied by this [CurveTexture](class_curvetexture.md#class_CurveTexture) over its lifetime.

 **Note:** [alpha_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_alpha_curve) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALPHA *= COLOR.a;` must be inserted in the shader's `fragment()` function. Otherwise, [alpha_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_alpha_curve) will have no visible effect.

---

<span id="class_ParticleProcessMaterial_property_angle_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **angle_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angle_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's rotation will be animated along this [CurveTexture](class_curvetexture.md#class_CurveTexture).

---

<span id="class_ParticleProcessMaterial_property_angle_max"></span>

[float](class_float.md#class_float) **angle_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angle_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum initial rotation applied to each particle, in degrees.

Only applied when [particle_flag_disable_z](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_disable_z) or [particle_flag_rotate_y](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_rotate_y) are `true` or the [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D) being used to draw the particle is using [BaseMaterial3D.BILLBOARD_PARTICLES](class_basematerial3d.md#class_BaseMaterial3D_constant_BILLBOARD_PARTICLES).

---

<span id="class_ParticleProcessMaterial_property_angle_min"></span>

[float](class_float.md#class_float) **angle_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angle_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [angle_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angle_max).

---

<span id="class_ParticleProcessMaterial_property_angular_velocity_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **angular_velocity_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angular_velocity_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's angular velocity (rotation speed) will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture) over its lifetime.

---

<span id="class_ParticleProcessMaterial_property_angular_velocity_max"></span>

[float](class_float.md#class_float) **angular_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angular_velocity_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

Only applied when [particle_flag_disable_z](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_disable_z) or [particle_flag_rotate_y](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_rotate_y) are `true` or the [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D) being used to draw the particle is using [BaseMaterial3D.BILLBOARD_PARTICLES](class_basematerial3d.md#class_BaseMaterial3D_constant_BILLBOARD_PARTICLES).

---

<span id="class_ParticleProcessMaterial_property_angular_velocity_min"></span>

[float](class_float.md#class_float) **angular_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angular_velocity_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [angular_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angular_velocity_max).

---

<span id="class_ParticleProcessMaterial_property_anim_offset_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **anim_offset_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_offset_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's animation offset will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture).

---

<span id="class_ParticleProcessMaterial_property_anim_offset_max"></span>

[float](class_float.md#class_float) **anim_offset_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_offset_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum animation offset that corresponds to frame index in the texture. `0` is the first frame, `1` is the last one. See [CanvasItemMaterial.particles_animation](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_animation).

---

<span id="class_ParticleProcessMaterial_property_anim_offset_min"></span>

[float](class_float.md#class_float) **anim_offset_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_offset_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [anim_offset_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_offset_max).

---

<span id="class_ParticleProcessMaterial_property_anim_speed_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **anim_speed_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_speed_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's animation speed will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture).

---

<span id="class_ParticleProcessMaterial_property_anim_speed_max"></span>

[float](class_float.md#class_float) **anim_speed_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_speed_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum particle animation speed. Animation speed of `1` means that the particles will make full `0` to `1` offset cycle during lifetime, `2` means `2` cycles etc.

With animation speed greater than `1`, remember to enable [CanvasItemMaterial.particles_anim_loop](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_anim_loop) property if you want the animation to repeat.

---

<span id="class_ParticleProcessMaterial_property_anim_speed_min"></span>

[float](class_float.md#class_float) **anim_speed_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_speed_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [anim_speed_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_anim_speed_max).

---

<span id="class_ParticleProcessMaterial_property_attractor_interaction_enabled"></span>

[bool](class_bool.md#class_bool) **attractor_interaction_enabled** = `true` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_attractor_interaction_enabled)

- void **set_attractor_interaction_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_attractor_interaction_enabled** ( )

If `true`, interaction with particle attractors is enabled. In 3D, attraction only occurs within the area defined by the [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) node's [GPUParticles3D.visibility_aabb](class_gpuparticles3d.md#class_GPUParticles3D_property_visibility_aabb).

---

<span id="class_ParticleProcessMaterial_property_collision_bounce"></span>

[float](class_float.md#class_float) **collision_bounce** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_bounce)

- void **set_collision_bounce** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_collision_bounce** ( )

The particles' bounciness. Values range from `0` (no bounce) to `1` (full bounciness). Only effective if [collision_mode](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_mode) is [COLLISION_RIGID](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_COLLISION_RIGID).

---

<span id="class_ParticleProcessMaterial_property_collision_friction"></span>

[float](class_float.md#class_float) **collision_friction** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_friction)

- void **set_collision_friction** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_collision_friction** ( )

The particles' friction. Values range from `0` (frictionless) to `1` (maximum friction). Only effective if [collision_mode](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_mode) is [COLLISION_RIGID](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_COLLISION_RIGID).

---

<span id="class_ParticleProcessMaterial_property_collision_mode"></span>

[CollisionMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode) **collision_mode** = `0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_mode)

- void **set_collision_mode** ( value: [CollisionMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode) )
- [CollisionMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_CollisionMode) **get_collision_mode** ( )

The particles' collision mode.

 **Note:** 3D Particles can only collide with [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D) nodes, not [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) nodes. To make particles collide with various objects, you can add [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D) nodes as children of [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) nodes. In 3D, collisions only occur within the area defined by the [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) node's [GPUParticles3D.visibility_aabb](class_gpuparticles3d.md#class_GPUParticles3D_property_visibility_aabb).

 **Note:** 2D Particles can only collide with [LightOccluder2D](class_lightoccluder2d.md#class_LightOccluder2D) nodes, not [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) nodes.

---

<span id="class_ParticleProcessMaterial_property_collision_use_scale"></span>

[bool](class_bool.md#class_bool) **collision_use_scale** = `false` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_use_scale)

- void **set_collision_use_scale** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collision_using_scale** ( )

If `true`, [GPUParticles3D.collision_base_size](class_gpuparticles3d.md#class_GPUParticles3D_property_collision_base_size) is multiplied by the particle's effective scale (see [scale_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_min), [scale_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_max), [scale_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_curve), and [scale_over_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_curve)).

---

<span id="class_ParticleProcessMaterial_property_color"></span>

[Color](class_color.md#class_Color) **color** = `Color(1, 1, 1, 1)` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color)

- void **set_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_color** ( )

Each particle's initial color. If the [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D)'s `texture` is defined, it will be multiplied by this color.

 **Note:** [color](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color) will have no visible effect.

---

<span id="class_ParticleProcessMaterial_property_color_initial_ramp"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **color_initial_ramp** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color_initial_ramp)

- void **set_color_initial_ramp** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_color_initial_ramp** ( )

Each particle's initial color will vary along this [GradientTexture1D](class_gradienttexture1d.md#class_GradientTexture1D) (multiplied with [color](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color)).

 **Note:** [color_initial_ramp](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color_initial_ramp) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color_initial_ramp](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color_initial_ramp) will have no visible effect.

---

<span id="class_ParticleProcessMaterial_property_color_ramp"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **color_ramp** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color_ramp)

- void **set_color_ramp** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_color_ramp** ( )

Each particle's color will vary along this [GradientTexture1D](class_gradienttexture1d.md#class_GradientTexture1D) over its lifetime (multiplied with [color](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color)).

 **Note:** [color_ramp](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color_ramp) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color_ramp](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_color_ramp) will have no visible effect.

---

<span id="class_ParticleProcessMaterial_property_damping_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **damping_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_damping_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Damping will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture).

---

<span id="class_ParticleProcessMaterial_property_damping_max"></span>

[float](class_float.md#class_float) **damping_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_damping_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

The maximum rate at which particles lose velocity. For example value of `100` means that the particle will go from `100` velocity to `0` in `1` second.

---

<span id="class_ParticleProcessMaterial_property_damping_min"></span>

[float](class_float.md#class_float) **damping_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_damping_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [damping_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_damping_max).

---

<span id="class_ParticleProcessMaterial_property_direction"></span>

[Vector3](class_vector3.md#class_Vector3) **direction** = `Vector3(1, 0, 0)` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_direction)

- void **set_direction** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_direction** ( )

Unit vector specifying the particles' emission direction.

---

<span id="class_ParticleProcessMaterial_property_directional_velocity_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **directional_velocity_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_directional_velocity_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

A curve that specifies the velocity along each of the axes of the particle system along its lifetime.

 **Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) instead.

---

<span id="class_ParticleProcessMaterial_property_directional_velocity_max"></span>

[float](class_float.md#class_float) **directional_velocity_max** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_directional_velocity_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum directional velocity value, which is multiplied by [directional_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_directional_velocity_curve).

 **Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) instead.

---

<span id="class_ParticleProcessMaterial_property_directional_velocity_min"></span>

[float](class_float.md#class_float) **directional_velocity_min** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_directional_velocity_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum directional velocity value, which is multiplied by [directional_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_directional_velocity_curve).

 **Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) instead.

---

<span id="class_ParticleProcessMaterial_property_emission_box_extents"></span>

[Vector3](class_vector3.md#class_Vector3) **emission_box_extents** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_box_extents)

- void **set_emission_box_extents** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_emission_box_extents** ( )

The box's extents if [emission_shape](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape) is set to [EMISSION_SHAPE_BOX](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_BOX).

 **Note:** [emission_box_extents](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_box_extents) starts from the center point and applies the X, Y, and Z values in both directions. The size is twice the area of the extents.

---

<span id="class_ParticleProcessMaterial_property_emission_color_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **emission_color_texture** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_color_texture)

- void **set_emission_color_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_emission_color_texture** ( )

Particle color will be modulated by color determined by sampling this texture at the same point as the [emission_point_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_point_texture).

 **Note:** [emission_color_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_color_texture) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [emission_color_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_color_texture) will have no visible effect.

---

<span id="class_ParticleProcessMaterial_property_emission_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **emission_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_curve)

- void **set_emission_curve** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_emission_curve** ( )

Each particle's color will be multiplied by this [CurveTexture](class_curvetexture.md#class_CurveTexture) over its lifetime.

 **Note:** [emission_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_curve) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [emission_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_curve) will have no visible effect.

---

<span id="class_ParticleProcessMaterial_property_emission_normal_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **emission_normal_texture** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_normal_texture)

- void **set_emission_normal_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_emission_normal_texture** ( )

Particle velocity and rotation will be set by sampling this texture at the same point as the [emission_point_texture](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_point_texture). Used only in [EMISSION_SHAPE_DIRECTED_POINTS](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS). Can be created automatically from mesh or node by selecting "Create Emission Points from Mesh/Node" under the "Particles" tool in the toolbar.

---

<span id="class_ParticleProcessMaterial_property_emission_point_count"></span>

[int](class_int.md#class_int) **emission_point_count** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_point_count)

- void **set_emission_point_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_emission_point_count** ( )

The number of emission points if [emission_shape](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape) is set to [EMISSION_SHAPE_POINTS](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINTS) or [EMISSION_SHAPE_DIRECTED_POINTS](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS).

---

<span id="class_ParticleProcessMaterial_property_emission_point_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **emission_point_texture** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_point_texture)

- void **set_emission_point_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_emission_point_texture** ( )

Particles will be emitted at positions determined by sampling this texture at a random position. Used with [EMISSION_SHAPE_POINTS](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINTS) and [EMISSION_SHAPE_DIRECTED_POINTS](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS). Can be created automatically from mesh or node by selecting "Create Emission Points from Mesh/Node" under the "Particles" tool in the toolbar.

---

<span id="class_ParticleProcessMaterial_property_emission_ring_axis"></span>

[Vector3](class_vector3.md#class_Vector3) **emission_ring_axis** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_axis)

- void **set_emission_ring_axis** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_emission_ring_axis** ( )

The axis of the ring when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING).

---

<span id="class_ParticleProcessMaterial_property_emission_ring_cone_angle"></span>

[float](class_float.md#class_float) **emission_ring_cone_angle** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_cone_angle)

- void **set_emission_ring_cone_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_cone_angle** ( )

The angle of the cone when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING). The default angle of 90 degrees results in a ring, while an angle of 0 degrees results in a cone. Intermediate values will result in a ring where one end is larger than the other.

 **Note:** Depending on [emission_ring_height](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_height), the angle may be clamped if the ring's end is reached to form a perfect cone.

---

<span id="class_ParticleProcessMaterial_property_emission_ring_height"></span>

[float](class_float.md#class_float) **emission_ring_height** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_height)

- void **set_emission_ring_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_height** ( )

The height of the ring when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING).

---

<span id="class_ParticleProcessMaterial_property_emission_ring_inner_radius"></span>

[float](class_float.md#class_float) **emission_ring_inner_radius** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_inner_radius)

- void **set_emission_ring_inner_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_inner_radius** ( )

The inner radius of the ring when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING).

---

<span id="class_ParticleProcessMaterial_property_emission_ring_radius"></span>

[float](class_float.md#class_float) **emission_ring_radius** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_ring_radius)

- void **set_emission_ring_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_radius** ( )

The radius of the ring when using the emitter [EMISSION_SHAPE_RING](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING).

---

<span id="class_ParticleProcessMaterial_property_emission_shape"></span>

[EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **emission_shape** = `0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape)

- void **set_emission_shape** ( value: [EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) )
- [EmissionShape](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_EmissionShape) **get_emission_shape** ( )

Particles will be emitted inside this region.

---

<span id="class_ParticleProcessMaterial_property_emission_shape_offset"></span>

[Vector3](class_vector3.md#class_Vector3) **emission_shape_offset** = `Vector3(0, 0, 0)` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape_offset)

- void **set_emission_shape_offset** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_emission_shape_offset** ( )

The offset for the [emission_shape](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape), in local space.

---

<span id="class_ParticleProcessMaterial_property_emission_shape_scale"></span>

[Vector3](class_vector3.md#class_Vector3) **emission_shape_scale** = `Vector3(1, 1, 1)` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape_scale)

- void **set_emission_shape_scale** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_emission_shape_scale** ( )

The scale of the [emission_shape](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape), in local space.

---

<span id="class_ParticleProcessMaterial_property_emission_sphere_radius"></span>

[float](class_float.md#class_float) **emission_sphere_radius** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_sphere_radius)

- void **set_emission_sphere_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_sphere_radius** ( )

The sphere's radius if [emission_shape](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_emission_shape) is set to [EMISSION_SHAPE_SPHERE](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_SPHERE).

---

<span id="class_ParticleProcessMaterial_property_flatness"></span>

[float](class_float.md#class_float) **flatness** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_flatness)

- void **set_flatness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_flatness** ( )

Amount of [spread](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_spread) along the Y axis.

---

<span id="class_ParticleProcessMaterial_property_gravity"></span>

[Vector3](class_vector3.md#class_Vector3) **gravity** = `Vector3(0, -9.8, 0)` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_gravity)

- void **set_gravity** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_gravity** ( )

Gravity applied to every particle.

---

<span id="class_ParticleProcessMaterial_property_hue_variation_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **hue_variation_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_hue_variation_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's hue will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture).

---

<span id="class_ParticleProcessMaterial_property_hue_variation_max"></span>

[float](class_float.md#class_float) **hue_variation_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_hue_variation_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum initial hue variation applied to each particle. It will shift the particle color's hue.

---

<span id="class_ParticleProcessMaterial_property_hue_variation_min"></span>

[float](class_float.md#class_float) **hue_variation_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_hue_variation_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [hue_variation_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_hue_variation_max).

---

<span id="class_ParticleProcessMaterial_property_inherit_velocity_ratio"></span>

[float](class_float.md#class_float) **inherit_velocity_ratio** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_inherit_velocity_ratio)

- void **set_inherit_velocity_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_inherit_velocity_ratio** ( )

Percentage of the velocity of the respective [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) or [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) inherited by each particle when spawning.

---

<span id="class_ParticleProcessMaterial_property_initial_velocity_max"></span>

[float](class_float.md#class_float) **initial_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_initial_velocity_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum initial velocity magnitude for each particle. Direction comes from [direction](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_direction) and [spread](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_spread).

---

<span id="class_ParticleProcessMaterial_property_initial_velocity_min"></span>

[float](class_float.md#class_float) **initial_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_initial_velocity_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [initial_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_initial_velocity_max).

---

<span id="class_ParticleProcessMaterial_property_lifetime_randomness"></span>

[float](class_float.md#class_float) **lifetime_randomness** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_lifetime_randomness)

- void **set_lifetime_randomness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_lifetime_randomness** ( )

Particle lifetime randomness ratio. The equation for the lifetime of a particle is `lifetime * (1.0 - randf() * lifetime_randomness)`. For example, a [lifetime_randomness](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_lifetime_randomness) of `0.4` scales the lifetime between `0.6` to `1.0` of its original value.

---

<span id="class_ParticleProcessMaterial_property_linear_accel_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **linear_accel_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_linear_accel_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's linear acceleration will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture).

---

<span id="class_ParticleProcessMaterial_property_linear_accel_max"></span>

[float](class_float.md#class_float) **linear_accel_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_linear_accel_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum linear acceleration applied to each particle in the direction of motion.

---

<span id="class_ParticleProcessMaterial_property_linear_accel_min"></span>

[float](class_float.md#class_float) **linear_accel_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_linear_accel_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [linear_accel_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_linear_accel_max).

---

<span id="class_ParticleProcessMaterial_property_orbit_velocity_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **orbit_velocity_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_orbit_velocity_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's orbital velocity will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture).

 **Note:** For 3D orbital velocity, use a [CurveXYZTexture](class_curvexyztexture.md#class_CurveXYZTexture).

 **Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) instead.

---

<span id="class_ParticleProcessMaterial_property_orbit_velocity_max"></span>

[float](class_float.md#class_float) **orbit_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_orbit_velocity_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum orbital velocity applied to each particle. Makes the particles circle around origin. Specified in number of full rotations around origin per second.

 **Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) instead.

---

<span id="class_ParticleProcessMaterial_property_orbit_velocity_min"></span>

[float](class_float.md#class_float) **orbit_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_orbit_velocity_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [orbit_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_orbit_velocity_max).

 **Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) instead.

---

<span id="class_ParticleProcessMaterial_property_particle_flag_align_y"></span>

[bool](class_bool.md#class_bool) **particle_flag_align_y** = `false` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_align_y)

- void **set_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) ) *const*

Align Y axis of particle with the direction of its velocity.

---

<span id="class_ParticleProcessMaterial_property_particle_flag_damping_as_friction"></span>

[bool](class_bool.md#class_bool) **particle_flag_damping_as_friction** = `false` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_damping_as_friction)

- void **set_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) ) *const*

Changes the behavior of the damping properties from a linear deceleration to a deceleration based on speed percentage.

---

<span id="class_ParticleProcessMaterial_property_particle_flag_disable_z"></span>

[bool](class_bool.md#class_bool) **particle_flag_disable_z** = `false` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_disable_z)

- void **set_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) ) *const*

If `true`, particles will not move on the z axis.

---

<span id="class_ParticleProcessMaterial_property_particle_flag_rotate_y"></span>

[bool](class_bool.md#class_bool) **particle_flag_rotate_y** = `false` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_particle_flag_rotate_y)

- void **set_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) ) *const*

If `true`, particles rotate around Y axis by [angle_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_angle_min).

---

<span id="class_ParticleProcessMaterial_property_radial_accel_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **radial_accel_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_accel_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's radial acceleration will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture).

---

<span id="class_ParticleProcessMaterial_property_radial_accel_max"></span>

[float](class_float.md#class_float) **radial_accel_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_accel_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum radial acceleration applied to each particle. Makes particle accelerate away from the origin or towards it if negative.

---

<span id="class_ParticleProcessMaterial_property_radial_accel_min"></span>

[float](class_float.md#class_float) **radial_accel_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_accel_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [radial_accel_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_accel_max).

---

<span id="class_ParticleProcessMaterial_property_radial_velocity_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **radial_velocity_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_velocity_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

A [CurveTexture](class_curvetexture.md#class_CurveTexture) that defines the velocity over the particle's lifetime away (or toward) the [velocity_pivot](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_pivot).

 **Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) instead.

---

<span id="class_ParticleProcessMaterial_property_radial_velocity_max"></span>

[float](class_float.md#class_float) **radial_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_velocity_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum radial velocity applied to each particle. Makes particles move away from the [velocity_pivot](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_pivot), or toward it if negative.

 **Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) instead.

---

<span id="class_ParticleProcessMaterial_property_radial_velocity_min"></span>

[float](class_float.md#class_float) **radial_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_radial_velocity_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum radial velocity applied to each particle. Makes particles move away from the [velocity_pivot](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_pivot), or toward it if negative.

 **Note:** Animated velocities will not be affected by damping, use [velocity_limit_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve) instead.

---

<span id="class_ParticleProcessMaterial_property_scale_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **scale_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's scale will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture) over its lifetime. If a [CurveXYZTexture](class_curvexyztexture.md#class_CurveXYZTexture) is supplied instead, the scale will be separated per-axis.

---

<span id="class_ParticleProcessMaterial_property_scale_max"></span>

[float](class_float.md#class_float) **scale_max** = `1.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum initial scale applied to each particle.

---

<span id="class_ParticleProcessMaterial_property_scale_min"></span>

[float](class_float.md#class_float) **scale_min** = `1.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [scale_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_max).

---

<span id="class_ParticleProcessMaterial_property_scale_over_velocity_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **scale_over_velocity_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Either a [CurveTexture](class_curvetexture.md#class_CurveTexture) or a [CurveXYZTexture](class_curvexyztexture.md#class_CurveXYZTexture) that scales each particle based on its velocity.

---

<span id="class_ParticleProcessMaterial_property_scale_over_velocity_max"></span>

[float](class_float.md#class_float) **scale_over_velocity_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum velocity value reference for [scale_over_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_curve).

 [scale_over_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_curve) will be interpolated between [scale_over_velocity_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_min) and [scale_over_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_max).

---

<span id="class_ParticleProcessMaterial_property_scale_over_velocity_min"></span>

[float](class_float.md#class_float) **scale_over_velocity_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum velocity value reference for [scale_over_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_curve).

 [scale_over_velocity_curve](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_curve) will be interpolated between [scale_over_velocity_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_min) and [scale_over_velocity_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_scale_over_velocity_max).

---

<span id="class_ParticleProcessMaterial_property_spread"></span>

[float](class_float.md#class_float) **spread** = `45.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_spread)

- void **set_spread** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_spread** ( )

Each particle's initial direction range from `+spread` to `-spread` degrees.

---

<span id="class_ParticleProcessMaterial_property_sub_emitter_amount_at_collision"></span>

[int](class_int.md#class_int) **sub_emitter_amount_at_collision** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_amount_at_collision)

- void **set_sub_emitter_amount_at_collision** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sub_emitter_amount_at_collision** ( )

The amount of particles to spawn from the subemitter node when a collision occurs. When combined with [COLLISION_HIDE_ON_CONTACT](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT) on the main particles material, this can be used to achieve effects such as raindrops hitting the ground.

 **Note:** This value shouldn't exceed [GPUParticles2D.amount](class_gpuparticles2d.md#class_GPUParticles2D_property_amount) or [GPUParticles3D.amount](class_gpuparticles3d.md#class_GPUParticles3D_property_amount) defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

---

<span id="class_ParticleProcessMaterial_property_sub_emitter_amount_at_end"></span>

[int](class_int.md#class_int) **sub_emitter_amount_at_end** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_amount_at_end)

- void **set_sub_emitter_amount_at_end** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sub_emitter_amount_at_end** ( )

The amount of particles to spawn from the subemitter node when the particle expires.

 **Note:** This value shouldn't exceed [GPUParticles2D.amount](class_gpuparticles2d.md#class_GPUParticles2D_property_amount) or [GPUParticles3D.amount](class_gpuparticles3d.md#class_GPUParticles3D_property_amount) defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

---

<span id="class_ParticleProcessMaterial_property_sub_emitter_amount_at_start"></span>

[int](class_int.md#class_int) **sub_emitter_amount_at_start** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_amount_at_start)

- void **set_sub_emitter_amount_at_start** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sub_emitter_amount_at_start** ( )

The amount of particles to spawn from the subemitter node when the particle spawns.

 **Note:** This value shouldn't exceed [GPUParticles2D.amount](class_gpuparticles2d.md#class_GPUParticles2D_property_amount) or [GPUParticles3D.amount](class_gpuparticles3d.md#class_GPUParticles3D_property_amount) defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

---

<span id="class_ParticleProcessMaterial_property_sub_emitter_frequency"></span>

[float](class_float.md#class_float) **sub_emitter_frequency** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_frequency)

- void **set_sub_emitter_frequency** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_sub_emitter_frequency** ( )

The frequency at which particles should be emitted from the subemitter node. One particle will be spawned every [sub_emitter_frequency](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_frequency) seconds.

 **Note:** This value shouldn't exceed [GPUParticles2D.amount](class_gpuparticles2d.md#class_GPUParticles2D_property_amount) or [GPUParticles3D.amount](class_gpuparticles3d.md#class_GPUParticles3D_property_amount) defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

---

<span id="class_ParticleProcessMaterial_property_sub_emitter_keep_velocity"></span>

[bool](class_bool.md#class_bool) **sub_emitter_keep_velocity** = `false` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_keep_velocity)

- void **set_sub_emitter_keep_velocity** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_sub_emitter_keep_velocity** ( )

If `true`, the subemitter inherits the parent particle's velocity when it spawns.

---

<span id="class_ParticleProcessMaterial_property_sub_emitter_mode"></span>

[SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) **sub_emitter_mode** = `0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_sub_emitter_mode)

- void **set_sub_emitter_mode** ( value: [SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) )
- [SubEmitterMode](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_SubEmitterMode) **get_sub_emitter_mode** ( )

The particle subemitter mode (see [GPUParticles2D.sub_emitter](class_gpuparticles2d.md#class_GPUParticles2D_property_sub_emitter) and [GPUParticles3D.sub_emitter](class_gpuparticles3d.md#class_GPUParticles3D_property_sub_emitter)).

---

<span id="class_ParticleProcessMaterial_property_tangential_accel_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **tangential_accel_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_tangential_accel_curve)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's tangential acceleration will vary along this [CurveTexture](class_curvetexture.md#class_CurveTexture).

---

<span id="class_ParticleProcessMaterial_property_tangential_accel_max"></span>

[float](class_float.md#class_float) **tangential_accel_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_tangential_accel_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum tangential acceleration applied to each particle. Tangential acceleration is perpendicular to the particle's velocity giving the particles a swirling motion.

---

<span id="class_ParticleProcessMaterial_property_tangential_accel_min"></span>

[float](class_float.md#class_float) **tangential_accel_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_tangential_accel_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum equivalent of [tangential_accel_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_tangential_accel_max).

---

<span id="class_ParticleProcessMaterial_property_turbulence_enabled"></span>

[bool](class_bool.md#class_bool) **turbulence_enabled** = `false` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_enabled)

- void **set_turbulence_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_turbulence_enabled** ( )

If `true`, enables turbulence for the particle system. Turbulence can be used to vary particle movement according to its position (based on a 3D noise pattern). In 3D, [GPUParticlesAttractorVectorField3D](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D) with [NoiseTexture3D](class_noisetexture3d.md#class_NoiseTexture3D) can be used as an alternative to turbulence that works in world space and with multiple particle systems reacting in the same way.

 **Note:** Enabling turbulence has a high performance cost on the GPU. Only enable turbulence on a few particle systems at once at most, and consider disabling it when targeting mobile/web platforms.

---

<span id="class_ParticleProcessMaterial_property_turbulence_influence_max"></span>

[float](class_float.md#class_float) **turbulence_influence_max** = `0.1` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum turbulence influence on each particle.

The actual amount of turbulence influence on each particle is calculated as a random value between [turbulence_influence_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_min) and [turbulence_influence_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_max) and multiplied by the amount of turbulence influence from [turbulence_influence_over_life](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_over_life).

---

<span id="class_ParticleProcessMaterial_property_turbulence_influence_min"></span>

[float](class_float.md#class_float) **turbulence_influence_min** = `0.1` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum turbulence influence on each particle.

The actual amount of turbulence influence on each particle is calculated as a random value between [turbulence_influence_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_min) and [turbulence_influence_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_max) and multiplied by the amount of turbulence influence from [turbulence_influence_over_life](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_over_life).

---

<span id="class_ParticleProcessMaterial_property_turbulence_influence_over_life"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **turbulence_influence_over_life** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_influence_over_life)

- void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Each particle's amount of turbulence will be influenced along this [CurveTexture](class_curvetexture.md#class_CurveTexture) over its life time.

---

<span id="class_ParticleProcessMaterial_property_turbulence_initial_displacement_max"></span>

[float](class_float.md#class_float) **turbulence_initial_displacement_max** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_initial_displacement_max)

- void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Maximum displacement of each particle's spawn position by the turbulence.

The actual amount of displacement will be a factor of the underlying turbulence multiplied by a random value between [turbulence_initial_displacement_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_initial_displacement_min) and [turbulence_initial_displacement_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_initial_displacement_max).

---

<span id="class_ParticleProcessMaterial_property_turbulence_initial_displacement_min"></span>

[float](class_float.md#class_float) **turbulence_initial_displacement_min** = `0.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_initial_displacement_min)

- void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const*

Minimum displacement of each particle's spawn position by the turbulence.

The actual amount of displacement will be a factor of the underlying turbulence multiplied by a random value between [turbulence_initial_displacement_min](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_initial_displacement_min) and [turbulence_initial_displacement_max](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_initial_displacement_max).

---

<span id="class_ParticleProcessMaterial_property_turbulence_noise_scale"></span>

[float](class_float.md#class_float) **turbulence_noise_scale** = `9.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_noise_scale)

- void **set_turbulence_noise_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_turbulence_noise_scale** ( )

This value controls the overall scale/frequency of the turbulence noise pattern.

A small scale will result in smaller features with more detail while a high scale will result in smoother noise with larger features.

---

<span id="class_ParticleProcessMaterial_property_turbulence_noise_speed"></span>

[Vector3](class_vector3.md#class_Vector3) **turbulence_noise_speed** = `Vector3(0, 0, 0)` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_noise_speed)

- void **set_turbulence_noise_speed** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_turbulence_noise_speed** ( )

A scrolling velocity for the turbulence field. This sets a directional trend for the pattern to move in over time.

The default value of `Vector3(0, 0, 0)` turns off the scrolling.

---

<span id="class_ParticleProcessMaterial_property_turbulence_noise_speed_random"></span>

[float](class_float.md#class_float) **turbulence_noise_speed_random** = `0.2` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_noise_speed_random)

- void **set_turbulence_noise_speed_random** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_turbulence_noise_speed_random** ( )

The in-place rate of change of the turbulence field. This defines how quickly the noise pattern varies over time.

A value of 0.0 will result in a fixed pattern.

---

<span id="class_ParticleProcessMaterial_property_turbulence_noise_strength"></span>

[float](class_float.md#class_float) **turbulence_noise_strength** = `1.0` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_turbulence_noise_strength)

- void **set_turbulence_noise_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_turbulence_noise_strength** ( )

The turbulence noise strength. Increasing this will result in a stronger, more contrasting, flow pattern.

---

<span id="class_ParticleProcessMaterial_property_velocity_limit_curve"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **velocity_limit_curve** [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_limit_curve)

- void **set_velocity_limit_curve** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_velocity_limit_curve** ( )

A [CurveTexture](class_curvetexture.md#class_CurveTexture) that defines the maximum velocity of a particle during its lifetime.

---

<span id="class_ParticleProcessMaterial_property_velocity_pivot"></span>

[Vector3](class_vector3.md#class_Vector3) **velocity_pivot** = `Vector3(0, 0, 0)` [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_velocity_pivot)

- void **set_velocity_pivot** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_velocity_pivot** ( )

A pivot point used to calculate radial and orbital velocity of particles.

---

### Method Descriptions

<span id="class_ParticleProcessMaterial_method_get_param"></span>

[Vector2](class_vector2.md#class_Vector2) **get_param** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const* [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_param)

Returns the minimum and maximum values of the given `param` as a vector.

The `x` component of the returned vector corresponds to minimum and the `y` component corresponds to maximum.

---

<span id="class_ParticleProcessMaterial_method_get_param_max"></span>

[float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const* [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_param_max)

Returns the maximum value range for the given parameter.

---

<span id="class_ParticleProcessMaterial_method_get_param_min"></span>

[float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const* [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_param_min)

Returns the minimum value range for the given parameter.

---

<span id="class_ParticleProcessMaterial_method_get_param_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter) ) *const* [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_param_texture)

Returns the [Texture2D](class_texture2d.md#class_Texture2D) used by the specified parameter.

---

<span id="class_ParticleProcessMaterial_method_get_particle_flag"></span>

[bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags) ) *const* [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_get_particle_flag)

Returns `true` if the specified particle flag is enabled.

---

<span id="class_ParticleProcessMaterial_method_set_param"></span>

void **set_param** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param)

Sets the minimum and maximum values of the given `param`.

The `x` component of the argument vector corresponds to minimum and the `y` component corresponds to maximum.

---

<span id="class_ParticleProcessMaterial_method_set_param_max"></span>

void **set_param_max** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) ) [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_max)

Sets the maximum value range for the given parameter.

---

<span id="class_ParticleProcessMaterial_method_set_param_min"></span>

void **set_param_min** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), value: [float](class_float.md#class_float) ) [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_min)

Sets the minimum value range for the given parameter.

---

<span id="class_ParticleProcessMaterial_method_set_param_texture"></span>

void **set_param_texture** ( param: [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_param_texture)

Sets the [Texture2D](class_texture2d.md#class_Texture2D) for the specified [Parameter](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_Parameter).

---

<span id="class_ParticleProcessMaterial_method_set_particle_flag"></span>

void **set_particle_flag** ( particle_flag: [ParticleFlags](class_particleprocessmaterial.md#enum_ParticleProcessMaterial_ParticleFlags), enable: [bool](class_bool.md#class_bool) ) [🔗](class_particleprocessmaterial.md#class_ParticleProcessMaterial_method_set_particle_flag)

Sets the `particle_flag` to `enable`.
