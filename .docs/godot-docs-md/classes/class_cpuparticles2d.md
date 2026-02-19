<span id="class_CPUParticles2D"></span>

## CPUParticles2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A CPU-based 2D particle emitter.

### Description

CPU-based 2D particle node used to create a variety of particle systems and effects.

See also [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D), which provides the same functionality with hardware acceleration, but may not run on older devices.

### Tutorials

- [Particle systems (2D)](../tutorials/2d/particle_systems_2d.md)

### Properties


| [int](class_int.md#class_int) | [amount](class_cpuparticles2d.md#class_CPUParticles2D_property_amount) | `8` |
| --- | --- | --- |
| [Curve](class_curve.md#class_Curve) | [angle_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_angle_curve) |
| [float](class_float.md#class_float) | [angle_max](class_cpuparticles2d.md#class_CPUParticles2D_property_angle_max) | `0.0` |
| [float](class_float.md#class_float) | [angle_min](class_cpuparticles2d.md#class_CPUParticles2D_property_angle_min) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [angular_velocity_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_angular_velocity_curve) |
| [float](class_float.md#class_float) | [angular_velocity_max](class_cpuparticles2d.md#class_CPUParticles2D_property_angular_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [angular_velocity_min](class_cpuparticles2d.md#class_CPUParticles2D_property_angular_velocity_min) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [anim_offset_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_offset_curve) |
| [float](class_float.md#class_float) | [anim_offset_max](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_offset_max) | `0.0` |
| [float](class_float.md#class_float) | [anim_offset_min](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_offset_min) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [anim_speed_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_speed_curve) |
| [float](class_float.md#class_float) | [anim_speed_max](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_speed_max) | `0.0` |
| [float](class_float.md#class_float) | [anim_speed_min](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_speed_min) | `0.0` |
| [Color](class_color.md#class_Color) | [color](class_cpuparticles2d.md#class_CPUParticles2D_property_color) | `Color(1, 1, 1, 1)` |
| [Gradient](class_gradient.md#class_Gradient) | [color_initial_ramp](class_cpuparticles2d.md#class_CPUParticles2D_property_color_initial_ramp) |
| [Gradient](class_gradient.md#class_Gradient) | [color_ramp](class_cpuparticles2d.md#class_CPUParticles2D_property_color_ramp) |
| [Curve](class_curve.md#class_Curve) | [damping_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_damping_curve) |
| [float](class_float.md#class_float) | [damping_max](class_cpuparticles2d.md#class_CPUParticles2D_property_damping_max) | `0.0` |
| [float](class_float.md#class_float) | [damping_min](class_cpuparticles2d.md#class_CPUParticles2D_property_damping_min) | `0.0` |
| [Vector2](class_vector2.md#class_Vector2) | [direction](class_cpuparticles2d.md#class_CPUParticles2D_property_direction) | `Vector2(1, 0)` |
| [DrawOrder](class_cpuparticles2d.md#enum_CPUParticles2D_DrawOrder) | [draw_order](class_cpuparticles2d.md#class_CPUParticles2D_property_draw_order) | `0` |
| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [emission_colors](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_colors) |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [emission_normals](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_normals) |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [emission_points](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_points) |
| [Vector2](class_vector2.md#class_Vector2) | [emission_rect_extents](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_rect_extents) |
| [float](class_float.md#class_float) | [emission_ring_inner_radius](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_ring_inner_radius) |
| [float](class_float.md#class_float) | [emission_ring_radius](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_ring_radius) |
| [EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) | [emission_shape](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_shape) | `0` |
| [float](class_float.md#class_float) | [emission_sphere_radius](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_sphere_radius) |
| [bool](class_bool.md#class_bool) | [emitting](class_cpuparticles2d.md#class_CPUParticles2D_property_emitting) | `true` |
| [float](class_float.md#class_float) | [explosiveness](class_cpuparticles2d.md#class_CPUParticles2D_property_explosiveness) | `0.0` |
| [int](class_int.md#class_int) | [fixed_fps](class_cpuparticles2d.md#class_CPUParticles2D_property_fixed_fps) | `0` |
| [bool](class_bool.md#class_bool) | [fract_delta](class_cpuparticles2d.md#class_CPUParticles2D_property_fract_delta) | `true` |
| [Vector2](class_vector2.md#class_Vector2) | [gravity](class_cpuparticles2d.md#class_CPUParticles2D_property_gravity) | `Vector2(0, 980)` |
| [Curve](class_curve.md#class_Curve) | [hue_variation_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_hue_variation_curve) |
| [float](class_float.md#class_float) | [hue_variation_max](class_cpuparticles2d.md#class_CPUParticles2D_property_hue_variation_max) | `0.0` |
| [float](class_float.md#class_float) | [hue_variation_min](class_cpuparticles2d.md#class_CPUParticles2D_property_hue_variation_min) | `0.0` |
| [float](class_float.md#class_float) | [initial_velocity_max](class_cpuparticles2d.md#class_CPUParticles2D_property_initial_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [initial_velocity_min](class_cpuparticles2d.md#class_CPUParticles2D_property_initial_velocity_min) | `0.0` |
| [float](class_float.md#class_float) | [lifetime](class_cpuparticles2d.md#class_CPUParticles2D_property_lifetime) | `1.0` |
| [float](class_float.md#class_float) | [lifetime_randomness](class_cpuparticles2d.md#class_CPUParticles2D_property_lifetime_randomness) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [linear_accel_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_linear_accel_curve) |
| [float](class_float.md#class_float) | [linear_accel_max](class_cpuparticles2d.md#class_CPUParticles2D_property_linear_accel_max) | `0.0` |
| [float](class_float.md#class_float) | [linear_accel_min](class_cpuparticles2d.md#class_CPUParticles2D_property_linear_accel_min) | `0.0` |
| [bool](class_bool.md#class_bool) | [local_coords](class_cpuparticles2d.md#class_CPUParticles2D_property_local_coords) | `false` |
| [bool](class_bool.md#class_bool) | [one_shot](class_cpuparticles2d.md#class_CPUParticles2D_property_one_shot) | `false` |
| [Curve](class_curve.md#class_Curve) | [orbit_velocity_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_orbit_velocity_curve) |
| [float](class_float.md#class_float) | [orbit_velocity_max](class_cpuparticles2d.md#class_CPUParticles2D_property_orbit_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [orbit_velocity_min](class_cpuparticles2d.md#class_CPUParticles2D_property_orbit_velocity_min) | `0.0` |
| [bool](class_bool.md#class_bool) | [particle_flag_align_y](class_cpuparticles2d.md#class_CPUParticles2D_property_particle_flag_align_y) | `false` |
| [PhysicsInterpolationMode](class_node.md#enum_Node_PhysicsInterpolationMode) | physics_interpolation_mode | `2` (overrides [Node](class_node.md#class_Node_property_physics_interpolation_mode)) |
| [float](class_float.md#class_float) | [preprocess](class_cpuparticles2d.md#class_CPUParticles2D_property_preprocess) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [radial_accel_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_radial_accel_curve) |
| [float](class_float.md#class_float) | [radial_accel_max](class_cpuparticles2d.md#class_CPUParticles2D_property_radial_accel_max) | `0.0` |
| [float](class_float.md#class_float) | [radial_accel_min](class_cpuparticles2d.md#class_CPUParticles2D_property_radial_accel_min) | `0.0` |
| [float](class_float.md#class_float) | [randomness](class_cpuparticles2d.md#class_CPUParticles2D_property_randomness) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [scale_amount_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_amount_curve) |
| [float](class_float.md#class_float) | [scale_amount_max](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_amount_max) | `1.0` |
| [float](class_float.md#class_float) | [scale_amount_min](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_amount_min) | `1.0` |
| [Curve](class_curve.md#class_Curve) | [scale_curve_x](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_curve_x) |
| [Curve](class_curve.md#class_Curve) | [scale_curve_y](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_curve_y) |
| [int](class_int.md#class_int) | [seed](class_cpuparticles2d.md#class_CPUParticles2D_property_seed) | `0` |
| [float](class_float.md#class_float) | [speed_scale](class_cpuparticles2d.md#class_CPUParticles2D_property_speed_scale) | `1.0` |
| [bool](class_bool.md#class_bool) | [split_scale](class_cpuparticles2d.md#class_CPUParticles2D_property_split_scale) | `false` |
| [float](class_float.md#class_float) | [spread](class_cpuparticles2d.md#class_CPUParticles2D_property_spread) | `45.0` |
| [Curve](class_curve.md#class_Curve) | [tangential_accel_curve](class_cpuparticles2d.md#class_CPUParticles2D_property_tangential_accel_curve) |
| [float](class_float.md#class_float) | [tangential_accel_max](class_cpuparticles2d.md#class_CPUParticles2D_property_tangential_accel_max) | `0.0` |
| [float](class_float.md#class_float) | [tangential_accel_min](class_cpuparticles2d.md#class_CPUParticles2D_property_tangential_accel_min) | `0.0` |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_cpuparticles2d.md#class_CPUParticles2D_property_texture) |
| [bool](class_bool.md#class_bool) | [use_fixed_seed](class_cpuparticles2d.md#class_CPUParticles2D_property_use_fixed_seed) | `false` |

### Methods


| void | [convert_from_particles](class_cpuparticles2d.md#class_CPUParticles2D_method_convert_from_particles) ( particles: [Node](class_node.md#class_Node) ) |
| --- | --- |
| [Curve](class_curve.md#class_Curve) | [get_param_curve](class_cpuparticles2d.md#class_CPUParticles2D_method_get_param_curve) ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) const |
| [float](class_float.md#class_float) | [get_param_max](class_cpuparticles2d.md#class_CPUParticles2D_method_get_param_max) ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) const |
| [float](class_float.md#class_float) | [get_param_min](class_cpuparticles2d.md#class_CPUParticles2D_method_get_param_min) ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) const |
| [bool](class_bool.md#class_bool) | [get_particle_flag](class_cpuparticles2d.md#class_CPUParticles2D_method_get_particle_flag) ( particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags) ) const |
| void | [request_particles_process](class_cpuparticles2d.md#class_CPUParticles2D_method_request_particles_process) ( process_time: [float](class_float.md#class_float) ) |
| void | [restart](class_cpuparticles2d.md#class_CPUParticles2D_method_restart) ( keep_seed: [bool](class_bool.md#class_bool) = false ) |
| void | [set_param_curve](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) ) |
| void | [set_param_max](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max) ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) ) |
| void | [set_param_min](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min) ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) ) |
| void | [set_particle_flag](class_cpuparticles2d.md#class_CPUParticles2D_method_set_particle_flag) ( particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags), enable: [bool](class_bool.md#class_bool) ) |

---

### Signals

<span id="class_CPUParticles2D_signal_finished"></span>

**finished** ( ) [🔗](class_cpuparticles2d.md#class_CPUParticles2D_signal_finished)

Emitted when all active particles have finished processing. When [one_shot](class_cpuparticles2d.md#class_CPUParticles2D_property_one_shot) is disabled, particles will process continuously, so this is never emitted.

---

### Enumerations

<span id="enum_CPUParticles2D_DrawOrder"></span>

enum **DrawOrder**: [🔗](class_cpuparticles2d.md#enum_CPUParticles2D_DrawOrder)

<span id="class_CPUParticles2D_constant_DRAW_ORDER_INDEX"></span>

[DrawOrder](class_cpuparticles2d.md#enum_CPUParticles2D_DrawOrder) **DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

<span id="class_CPUParticles2D_constant_DRAW_ORDER_LIFETIME"></span>

[DrawOrder](class_cpuparticles2d.md#enum_CPUParticles2D_DrawOrder) **DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the particle with the highest lifetime is drawn at the front.

---

<span id="enum_CPUParticles2D_Parameter"></span>

enum **Parameter**: [🔗](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter)

<span id="class_CPUParticles2D_constant_PARAM_INITIAL_LINEAR_VELOCITY"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set initial velocity properties.

<span id="class_CPUParticles2D_constant_PARAM_ANGULAR_VELOCITY"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_ANGULAR_VELOCITY** = `1`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set angular velocity properties.

<span id="class_CPUParticles2D_constant_PARAM_ORBIT_VELOCITY"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_ORBIT_VELOCITY** = `2`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set orbital velocity properties.

<span id="class_CPUParticles2D_constant_PARAM_LINEAR_ACCEL"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_LINEAR_ACCEL** = `3`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set linear acceleration properties.

<span id="class_CPUParticles2D_constant_PARAM_RADIAL_ACCEL"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_RADIAL_ACCEL** = `4`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set radial acceleration properties.

<span id="class_CPUParticles2D_constant_PARAM_TANGENTIAL_ACCEL"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_TANGENTIAL_ACCEL** = `5`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set tangential acceleration properties.

<span id="class_CPUParticles2D_constant_PARAM_DAMPING"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_DAMPING** = `6`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set damping properties.

<span id="class_CPUParticles2D_constant_PARAM_ANGLE"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_ANGLE** = `7`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set angle properties.

<span id="class_CPUParticles2D_constant_PARAM_SCALE"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_SCALE** = `8`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set scale properties.

<span id="class_CPUParticles2D_constant_PARAM_HUE_VARIATION"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_HUE_VARIATION** = `9`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set hue variation properties.

<span id="class_CPUParticles2D_constant_PARAM_ANIM_SPEED"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_ANIM_SPEED** = `10`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set animation speed properties.

<span id="class_CPUParticles2D_constant_PARAM_ANIM_OFFSET"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_ANIM_OFFSET** = `11`

Use with [set_param_min()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min), [set_param_max()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max), and [set_param_curve()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve) to set animation offset properties.

<span id="class_CPUParticles2D_constant_PARAM_MAX"></span>

[Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) **PARAM_MAX** = `12`

Represents the size of the [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) enum.

---

<span id="enum_CPUParticles2D_ParticleFlags"></span>

enum **ParticleFlags**: [🔗](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags)

<span id="class_CPUParticles2D_constant_PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY"></span>

[ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags) **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with [set_particle_flag()](class_cpuparticles2d.md#class_CPUParticles2D_method_set_particle_flag) to set [particle_flag_align_y](class_cpuparticles2d.md#class_CPUParticles2D_property_particle_flag_align_y).

<span id="class_CPUParticles2D_constant_PARTICLE_FLAG_ROTATE_Y"></span>

[ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags) **PARTICLE_FLAG_ROTATE_Y** = `1`

Present for consistency with 3D particle nodes, not used in 2D.

<span id="class_CPUParticles2D_constant_PARTICLE_FLAG_DISABLE_Z"></span>

[ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags) **PARTICLE_FLAG_DISABLE_Z** = `2`

Present for consistency with 3D particle nodes, not used in 2D.

<span id="class_CPUParticles2D_constant_PARTICLE_FLAG_MAX"></span>

[ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags) **PARTICLE_FLAG_MAX** = `3`

Represents the size of the [ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags) enum.

---

<span id="enum_CPUParticles2D_EmissionShape"></span>

enum **EmissionShape**: [🔗](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape)

<span id="class_CPUParticles2D_constant_EMISSION_SHAPE_POINT"></span>

[EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

<span id="class_CPUParticles2D_constant_EMISSION_SHAPE_SPHERE"></span>

[EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere flattened to two dimensions.

<span id="class_CPUParticles2D_constant_EMISSION_SHAPE_SPHERE_SURFACE"></span>

[EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere flattened to two dimensions.

<span id="class_CPUParticles2D_constant_EMISSION_SHAPE_RECTANGLE"></span>

[EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **EMISSION_SHAPE_RECTANGLE** = `3`

Particles will be emitted in the area of a rectangle.

<span id="class_CPUParticles2D_constant_EMISSION_SHAPE_POINTS"></span>

[EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position chosen randomly among [emission_points](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_points). Particle color will be modulated by [emission_colors](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_colors).

<span id="class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS"></span>

[EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position chosen randomly among [emission_points](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_points). Particle velocity and rotation will be set based on [emission_normals](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_normals). Particle color will be modulated by [emission_colors](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_colors).

<span id="class_CPUParticles2D_constant_EMISSION_SHAPE_RING"></span>

[EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in the area of a ring parameterized by its outer and inner radius.

<span id="class_CPUParticles2D_constant_EMISSION_SHAPE_MAX"></span>

[EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **EMISSION_SHAPE_MAX** = `7`

Represents the size of the [EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) enum.

---

### Property Descriptions

<span id="class_CPUParticles2D_property_amount"></span>

[int](class_int.md#class_int) **amount** = `8` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_amount)

- void **set_amount** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_amount** ( )

Number of particles emitted in one emission cycle.

---

<span id="class_CPUParticles2D_property_angle_curve"></span>

[Curve](class_curve.md#class_Curve) **angle_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_angle_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's rotation will be animated along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_angle_max"></span>

[float](class_float.md#class_float) **angle_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_angle_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum initial rotation applied to each particle, in degrees.

---

<span id="class_CPUParticles2D_property_angle_min"></span>

[float](class_float.md#class_float) **angle_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_angle_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [angle_max](class_cpuparticles2d.md#class_CPUParticles2D_property_angle_max).

---

<span id="class_CPUParticles2D_property_angular_velocity_curve"></span>

[Curve](class_curve.md#class_Curve) **angular_velocity_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_angular_velocity_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's angular velocity will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_angular_velocity_max"></span>

[float](class_float.md#class_float) **angular_velocity_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_angular_velocity_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

---

<span id="class_CPUParticles2D_property_angular_velocity_min"></span>

[float](class_float.md#class_float) **angular_velocity_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_angular_velocity_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [angular_velocity_max](class_cpuparticles2d.md#class_CPUParticles2D_property_angular_velocity_max).

---

<span id="class_CPUParticles2D_property_anim_offset_curve"></span>

[Curve](class_curve.md#class_Curve) **anim_offset_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_offset_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's animation offset will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_anim_offset_max"></span>

[float](class_float.md#class_float) **anim_offset_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_offset_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum animation offset that corresponds to frame index in the texture. `0` is the first frame, `1` is the last one. See [CanvasItemMaterial.particles_animation](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_animation).

---

<span id="class_CPUParticles2D_property_anim_offset_min"></span>

[float](class_float.md#class_float) **anim_offset_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_offset_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [anim_offset_max](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_offset_max).

---

<span id="class_CPUParticles2D_property_anim_speed_curve"></span>

[Curve](class_curve.md#class_Curve) **anim_speed_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_speed_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's animation speed will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_anim_speed_max"></span>

[float](class_float.md#class_float) **anim_speed_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_speed_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum particle animation speed. Animation speed of `1` means that the particles will make full `0` to `1` offset cycle during lifetime, `2` means `2` cycles etc.

With animation speed greater than `1`, remember to enable [CanvasItemMaterial.particles_anim_loop](class_canvasitemmaterial.md#class_CanvasItemMaterial_property_particles_anim_loop) property if you want the animation to repeat.

---

<span id="class_CPUParticles2D_property_anim_speed_min"></span>

[float](class_float.md#class_float) **anim_speed_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_speed_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [anim_speed_max](class_cpuparticles2d.md#class_CPUParticles2D_property_anim_speed_max).

---

<span id="class_CPUParticles2D_property_color"></span>

[Color](class_color.md#class_Color) **color** = `Color(1, 1, 1, 1)` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_color)

- void **set_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_color** ( )

Each particle's initial color. If [texture](class_cpuparticles2d.md#class_CPUParticles2D_property_texture) is defined, it will be multiplied by this color.

---

<span id="class_CPUParticles2D_property_color_initial_ramp"></span>

[Gradient](class_gradient.md#class_Gradient) **color_initial_ramp** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_color_initial_ramp)

- void **set_color_initial_ramp** ( value: [Gradient](class_gradient.md#class_Gradient) )
- [Gradient](class_gradient.md#class_Gradient) **get_color_initial_ramp** ( )

Each particle's initial color will vary along this [Gradient](class_gradient.md#class_Gradient) (multiplied with [color](class_cpuparticles2d.md#class_CPUParticles2D_property_color)).

---

<span id="class_CPUParticles2D_property_color_ramp"></span>

[Gradient](class_gradient.md#class_Gradient) **color_ramp** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_color_ramp)

- void **set_color_ramp** ( value: [Gradient](class_gradient.md#class_Gradient) )
- [Gradient](class_gradient.md#class_Gradient) **get_color_ramp** ( )

Each particle's color will vary along this [Gradient](class_gradient.md#class_Gradient) over its lifetime (multiplied with [color](class_cpuparticles2d.md#class_CPUParticles2D_property_color)).

---

<span id="class_CPUParticles2D_property_damping_curve"></span>

[Curve](class_curve.md#class_Curve) **damping_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_damping_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Damping will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_damping_max"></span>

[float](class_float.md#class_float) **damping_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_damping_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

The maximum rate at which particles lose velocity. For example value of `100` means that the particle will go from `100` velocity to `0` in `1` second.

---

<span id="class_CPUParticles2D_property_damping_min"></span>

[float](class_float.md#class_float) **damping_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_damping_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [damping_max](class_cpuparticles2d.md#class_CPUParticles2D_property_damping_max).

---

<span id="class_CPUParticles2D_property_direction"></span>

[Vector2](class_vector2.md#class_Vector2) **direction** = `Vector2(1, 0)` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_direction)

- void **set_direction** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_direction** ( )

Unit vector specifying the particles' emission direction.

---

<span id="class_CPUParticles2D_property_draw_order"></span>

[DrawOrder](class_cpuparticles2d.md#enum_CPUParticles2D_DrawOrder) **draw_order** = `0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_draw_order)

- void **set_draw_order** ( value: [DrawOrder](class_cpuparticles2d.md#enum_CPUParticles2D_DrawOrder) )
- [DrawOrder](class_cpuparticles2d.md#enum_CPUParticles2D_DrawOrder) **get_draw_order** ( )

Particle draw order.

---

<span id="class_CPUParticles2D_property_emission_colors"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **emission_colors** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_colors)

- void **set_emission_colors** ( value: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) )
- [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **get_emission_colors** ( )

Sets the [Color](class_color.md#class_Color) s to modulate particles by when using [EMISSION_SHAPE_POINTS](class_cpuparticles2d.md#class_CPUParticles2D_constant_EMISSION_SHAPE_POINTS) or [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles2d.md#class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) for more details.

---

<span id="class_CPUParticles2D_property_emission_normals"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **emission_normals** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_normals)

- void **set_emission_normals** ( value: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )
- [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_emission_normals** ( )

Sets the direction the particles will be emitted in when using [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles2d.md#class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.

---

<span id="class_CPUParticles2D_property_emission_points"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **emission_points** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_points)

- void **set_emission_points** ( value: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )
- [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_emission_points** ( )

Sets the initial positions to spawn particles when using [EMISSION_SHAPE_POINTS](class_cpuparticles2d.md#class_CPUParticles2D_constant_EMISSION_SHAPE_POINTS) or [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles2d.md#class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.

---

<span id="class_CPUParticles2D_property_emission_rect_extents"></span>

[Vector2](class_vector2.md#class_Vector2) **emission_rect_extents** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_rect_extents)

- void **set_emission_rect_extents** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_emission_rect_extents** ( )

The rectangle's extents if [emission_shape](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_shape) is set to [EMISSION_SHAPE_RECTANGLE](class_cpuparticles2d.md#class_CPUParticles2D_constant_EMISSION_SHAPE_RECTANGLE).

---

<span id="class_CPUParticles2D_property_emission_ring_inner_radius"></span>

[float](class_float.md#class_float) **emission_ring_inner_radius** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_ring_inner_radius)

- void **set_emission_ring_inner_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_inner_radius** ( )

The ring's inner radius if [emission_shape](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_shape) is set to [EMISSION_SHAPE_RING](class_cpuparticles2d.md#class_CPUParticles2D_constant_EMISSION_SHAPE_RING).

---

<span id="class_CPUParticles2D_property_emission_ring_radius"></span>

[float](class_float.md#class_float) **emission_ring_radius** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_ring_radius)

- void **set_emission_ring_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_radius** ( )

The ring's outer radius if [emission_shape](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_shape) is set to [EMISSION_SHAPE_RING](class_cpuparticles2d.md#class_CPUParticles2D_constant_EMISSION_SHAPE_RING).

---

<span id="class_CPUParticles2D_property_emission_shape"></span>

[EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **emission_shape** = `0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_shape)

- void **set_emission_shape** ( value: [EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) )
- [EmissionShape](class_cpuparticles2d.md#enum_CPUParticles2D_EmissionShape) **get_emission_shape** ( )

Particles will be emitted inside this region.

---

<span id="class_CPUParticles2D_property_emission_sphere_radius"></span>

[float](class_float.md#class_float) **emission_sphere_radius** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_sphere_radius)

- void **set_emission_sphere_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_sphere_radius** ( )

The sphere's radius if [emission_shape](class_cpuparticles2d.md#class_CPUParticles2D_property_emission_shape) is set to [EMISSION_SHAPE_SPHERE](class_cpuparticles2d.md#class_CPUParticles2D_constant_EMISSION_SHAPE_SPHERE).

---

<span id="class_CPUParticles2D_property_emitting"></span>

[bool](class_bool.md#class_bool) **emitting** = `true` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_emitting)

- void **set_emitting** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_emitting** ( )

If `true`, particles are being emitted. [emitting](class_cpuparticles2d.md#class_CPUParticles2D_property_emitting) can be used to start and stop particles from emitting. However, if [one_shot](class_cpuparticles2d.md#class_CPUParticles2D_property_one_shot) is `true` setting [emitting](class_cpuparticles2d.md#class_CPUParticles2D_property_emitting) to `true` will not restart the emission cycle until after all active particles finish processing. You can use the [finished](class_cpuparticles2d.md#class_CPUParticles2D_signal_finished) signal to be notified once all active particles finish processing.

---

<span id="class_CPUParticles2D_property_explosiveness"></span>

[float](class_float.md#class_float) **explosiveness** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_explosiveness)

- void **set_explosiveness_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_explosiveness_ratio** ( )

How rapidly particles in an emission cycle are emitted. If greater than `0`, there will be a gap in emissions before the next cycle begins.

---

<span id="class_CPUParticles2D_property_fixed_fps"></span>

[int](class_int.md#class_int) **fixed_fps** = `0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_fixed_fps)

- void **set_fixed_fps** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_fixed_fps** ( )

The particle system's frame rate is fixed to a value. For example, changing the value to 2 will make the particles render at 2 frames per second. Note this does not slow down the simulation of the particle system itself.

---

<span id="class_CPUParticles2D_property_fract_delta"></span>

[bool](class_bool.md#class_bool) **fract_delta** = `true` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_fract_delta)

- void **set_fractional_delta** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_fractional_delta** ( )

If `true`, results in fractional delta calculation which has a smoother particles display effect.

---

<span id="class_CPUParticles2D_property_gravity"></span>

[Vector2](class_vector2.md#class_Vector2) **gravity** = `Vector2(0, 980)` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_gravity)

- void **set_gravity** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_gravity** ( )

Gravity applied to every particle.

---

<span id="class_CPUParticles2D_property_hue_variation_curve"></span>

[Curve](class_curve.md#class_Curve) **hue_variation_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_hue_variation_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's hue will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_hue_variation_max"></span>

[float](class_float.md#class_float) **hue_variation_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_hue_variation_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum initial hue variation applied to each particle. It will shift the particle color's hue.

---

<span id="class_CPUParticles2D_property_hue_variation_min"></span>

[float](class_float.md#class_float) **hue_variation_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_hue_variation_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [hue_variation_max](class_cpuparticles2d.md#class_CPUParticles2D_property_hue_variation_max).

---

<span id="class_CPUParticles2D_property_initial_velocity_max"></span>

[float](class_float.md#class_float) **initial_velocity_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_initial_velocity_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum initial velocity magnitude for each particle. Direction comes from [direction](class_cpuparticles2d.md#class_CPUParticles2D_property_direction) and [spread](class_cpuparticles2d.md#class_CPUParticles2D_property_spread).

---

<span id="class_CPUParticles2D_property_initial_velocity_min"></span>

[float](class_float.md#class_float) **initial_velocity_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_initial_velocity_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [initial_velocity_max](class_cpuparticles2d.md#class_CPUParticles2D_property_initial_velocity_max).

---

<span id="class_CPUParticles2D_property_lifetime"></span>

[float](class_float.md#class_float) **lifetime** = `1.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_lifetime)

- void **set_lifetime** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_lifetime** ( )

Amount of time each particle will exist.

---

<span id="class_CPUParticles2D_property_lifetime_randomness"></span>

[float](class_float.md#class_float) **lifetime_randomness** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_lifetime_randomness)

- void **set_lifetime_randomness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_lifetime_randomness** ( )

Particle lifetime randomness ratio.

---

<span id="class_CPUParticles2D_property_linear_accel_curve"></span>

[Curve](class_curve.md#class_Curve) **linear_accel_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_linear_accel_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's linear acceleration will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_linear_accel_max"></span>

[float](class_float.md#class_float) **linear_accel_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_linear_accel_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum linear acceleration applied to each particle in the direction of motion.

---

<span id="class_CPUParticles2D_property_linear_accel_min"></span>

[float](class_float.md#class_float) **linear_accel_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_linear_accel_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [linear_accel_max](class_cpuparticles2d.md#class_CPUParticles2D_property_linear_accel_max).

---

<span id="class_CPUParticles2D_property_local_coords"></span>

[bool](class_bool.md#class_bool) **local_coords** = `false` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_local_coords)

- void **set_use_local_coordinates** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_local_coordinates** ( )

If `true`, particles use the parent node's coordinate space (known as local coordinates). This will cause particles to move and rotate along the **CPUParticles2D** node (and its parents) when it is moved or rotated. If `false`, particles use global coordinates; they will not move or rotate along the **CPUParticles2D** node (and its parents) when it is moved or rotated.

---

<span id="class_CPUParticles2D_property_one_shot"></span>

[bool](class_bool.md#class_bool) **one_shot** = `false` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_one_shot)

- void **set_one_shot** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_one_shot** ( )

If `true`, only one emission cycle occurs. If set `true` during a cycle, emission will stop at the cycle's end.

---

<span id="class_CPUParticles2D_property_orbit_velocity_curve"></span>

[Curve](class_curve.md#class_Curve) **orbit_velocity_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_orbit_velocity_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's orbital velocity will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_orbit_velocity_max"></span>

[float](class_float.md#class_float) **orbit_velocity_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_orbit_velocity_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum orbital velocity applied to each particle. Makes the particles circle around origin. Specified in number of full rotations around origin per second.

---

<span id="class_CPUParticles2D_property_orbit_velocity_min"></span>

[float](class_float.md#class_float) **orbit_velocity_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_orbit_velocity_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [orbit_velocity_max](class_cpuparticles2d.md#class_CPUParticles2D_property_orbit_velocity_max).

---

<span id="class_CPUParticles2D_property_particle_flag_align_y"></span>

[bool](class_bool.md#class_bool) **particle_flag_align_y** = `false` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_particle_flag_align_y)

- void **set_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags) ) *const*

Align Y axis of particle with the direction of its velocity.

---

<span id="class_CPUParticles2D_property_preprocess"></span>

[float](class_float.md#class_float) **preprocess** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_preprocess)

- void **set_pre_process_time** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pre_process_time** ( )

Particle system starts as if it had already run for this many seconds.

---

<span id="class_CPUParticles2D_property_radial_accel_curve"></span>

[Curve](class_curve.md#class_Curve) **radial_accel_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_radial_accel_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's radial acceleration will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_radial_accel_max"></span>

[float](class_float.md#class_float) **radial_accel_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_radial_accel_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum radial acceleration applied to each particle. Makes particle accelerate away from the origin or towards it if negative.

---

<span id="class_CPUParticles2D_property_radial_accel_min"></span>

[float](class_float.md#class_float) **radial_accel_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_radial_accel_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [radial_accel_max](class_cpuparticles2d.md#class_CPUParticles2D_property_radial_accel_max).

---

<span id="class_CPUParticles2D_property_randomness"></span>

[float](class_float.md#class_float) **randomness** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_randomness)

- void **set_randomness_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_randomness_ratio** ( )

Emission lifetime randomness ratio.

---

<span id="class_CPUParticles2D_property_scale_amount_curve"></span>

[Curve](class_curve.md#class_Curve) **scale_amount_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_amount_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's scale will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_scale_amount_max"></span>

[float](class_float.md#class_float) **scale_amount_max** = `1.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_amount_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum initial scale applied to each particle.

---

<span id="class_CPUParticles2D_property_scale_amount_min"></span>

[float](class_float.md#class_float) **scale_amount_min** = `1.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_amount_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [scale_amount_max](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_amount_max).

---

<span id="class_CPUParticles2D_property_scale_curve_x"></span>

[Curve](class_curve.md#class_Curve) **scale_curve_x** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_curve_x)

- void **set_scale_curve_x** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_scale_curve_x** ( )

Each particle's horizontal scale will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

 [split_scale](class_cpuparticles2d.md#class_CPUParticles2D_property_split_scale) must be enabled.

---

<span id="class_CPUParticles2D_property_scale_curve_y"></span>

[Curve](class_curve.md#class_Curve) **scale_curve_y** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_curve_y)

- void **set_scale_curve_y** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_scale_curve_y** ( )

Each particle's vertical scale will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

 [split_scale](class_cpuparticles2d.md#class_CPUParticles2D_property_split_scale) must be enabled.

---

<span id="class_CPUParticles2D_property_seed"></span>

[int](class_int.md#class_int) **seed** = `0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_seed)

- void **set_seed** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_seed** ( )

Sets the random seed used by the particle system. Only effective if [use_fixed_seed](class_cpuparticles2d.md#class_CPUParticles2D_property_use_fixed_seed) is `true`.

---

<span id="class_CPUParticles2D_property_speed_scale"></span>

[float](class_float.md#class_float) **speed_scale** = `1.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_speed_scale)

- void **set_speed_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_speed_scale** ( )

Particle system's running speed scaling ratio. A value of `0` can be used to pause the particles.

---

<span id="class_CPUParticles2D_property_split_scale"></span>

[bool](class_bool.md#class_bool) **split_scale** = `false` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_split_scale)

- void **set_split_scale** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_split_scale** ( )

If `true`, the scale curve will be split into x and y components. See [scale_curve_x](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_curve_x) and [scale_curve_y](class_cpuparticles2d.md#class_CPUParticles2D_property_scale_curve_y).

---

<span id="class_CPUParticles2D_property_spread"></span>

[float](class_float.md#class_float) **spread** = `45.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_spread)

- void **set_spread** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_spread** ( )

Each particle's initial direction range from `+spread` to `-spread` degrees.

---

<span id="class_CPUParticles2D_property_tangential_accel_curve"></span>

[Curve](class_curve.md#class_Curve) **tangential_accel_curve** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_tangential_accel_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Each particle's tangential acceleration will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_property_tangential_accel_max"></span>

[float](class_float.md#class_float) **tangential_accel_max** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_tangential_accel_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Maximum tangential acceleration applied to each particle. Tangential acceleration is perpendicular to the particle's velocity giving the particles a swirling motion.

---

<span id="class_CPUParticles2D_property_tangential_accel_min"></span>

[float](class_float.md#class_float) **tangential_accel_min** = `0.0` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_tangential_accel_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const*

Minimum equivalent of [tangential_accel_max](class_cpuparticles2d.md#class_CPUParticles2D_property_tangential_accel_max).

---

<span id="class_CPUParticles2D_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

Particle texture. If `null`, particles will be squares.

---

<span id="class_CPUParticles2D_property_use_fixed_seed"></span>

[bool](class_bool.md#class_bool) **use_fixed_seed** = `false` [🔗](class_cpuparticles2d.md#class_CPUParticles2D_property_use_fixed_seed)

- void **set_use_fixed_seed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_fixed_seed** ( )

If `true`, particles will use the same seed for every simulation using the seed defined in [seed](class_cpuparticles2d.md#class_CPUParticles2D_property_seed). This is useful for situations where the visual outcome should be consistent across replays, for example when using Movie Maker mode.

---

### Method Descriptions

<span id="class_CPUParticles2D_method_convert_from_particles"></span>

void **convert_from_particles** ( particles: [Node](class_node.md#class_Node) ) [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_convert_from_particles)

Sets this node's properties to match a given [GPUParticles2D](class_gpuparticles2d.md#class_GPUParticles2D) node with an assigned [ParticleProcessMaterial](class_particleprocessmaterial.md#class_ParticleProcessMaterial).

---

<span id="class_CPUParticles2D_method_get_param_curve"></span>

[Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const* [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_get_param_curve)

Returns the [Curve](class_curve.md#class_Curve) of the parameter specified by [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter).

---

<span id="class_CPUParticles2D_method_get_param_max"></span>

[float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const* [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_get_param_max)

Returns the maximum value range for the given parameter.

---

<span id="class_CPUParticles2D_method_get_param_min"></span>

[float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter) ) *const* [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_get_param_min)

Returns the minimum value range for the given parameter.

---

<span id="class_CPUParticles2D_method_get_particle_flag"></span>

[bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags) ) *const* [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_get_particle_flag)

Returns the enabled state of the given particle flag.

---

<span id="class_CPUParticles2D_method_request_particles_process"></span>

void **request_particles_process** ( process_time: [float](class_float.md#class_float) ) [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_request_particles_process)

Requests the particles to process for extra process time during a single frame.

Useful for particle playback, if used in combination with [use_fixed_seed](class_cpuparticles2d.md#class_CPUParticles2D_property_use_fixed_seed) or by calling [restart()](class_cpuparticles2d.md#class_CPUParticles2D_method_restart) with parameter `keep_seed` set to `true`.

---

<span id="class_CPUParticles2D_method_restart"></span>

void **restart** ( keep_seed: [bool](class_bool.md#class_bool) = false ) [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_restart)

Restarts the particle emitter.

If `keep_seed` is `true`, the current random seed will be preserved. Useful for seeking and playback.

---

<span id="class_CPUParticles2D_method_set_param_curve"></span>

void **set_param_curve** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), curve: [Curve](class_curve.md#class_Curve) ) [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_curve)

Sets the [Curve](class_curve.md#class_Curve) of the parameter specified by [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles2D_method_set_param_max"></span>

void **set_param_max** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) ) [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_max)

Sets the maximum value for the given parameter.

---

<span id="class_CPUParticles2D_method_set_param_min"></span>

void **set_param_min** ( param: [Parameter](class_cpuparticles2d.md#enum_CPUParticles2D_Parameter), value: [float](class_float.md#class_float) ) [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_set_param_min)

Sets the minimum value for the given parameter.

---

<span id="class_CPUParticles2D_method_set_particle_flag"></span>

void **set_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles2d.md#enum_CPUParticles2D_ParticleFlags), enable: [bool](class_bool.md#class_bool) ) [🔗](class_cpuparticles2d.md#class_CPUParticles2D_method_set_particle_flag)

Enables or disables the given particle flag.
