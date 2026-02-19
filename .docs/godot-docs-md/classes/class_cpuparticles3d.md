<span id="class_CPUParticles3D"></span>

## CPUParticles3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A CPU-based 3D particle emitter.

### Description

CPU-based 3D particle node used to create a variety of particle systems and effects.

See also [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D), which provides the same functionality with hardware acceleration, but may not run on older devices.

### Tutorials

- [Particle systems (3D)](../tutorials/3d/particles/index.md)

### Properties


| [int](class_int.md#class_int) | [amount](class_cpuparticles3d.md#class_CPUParticles3D_property_amount) | `8` |
| --- | --- | --- |
| [Curve](class_curve.md#class_Curve) | [angle_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_angle_curve) |
| [float](class_float.md#class_float) | [angle_max](class_cpuparticles3d.md#class_CPUParticles3D_property_angle_max) | `0.0` |
| [float](class_float.md#class_float) | [angle_min](class_cpuparticles3d.md#class_CPUParticles3D_property_angle_min) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [angular_velocity_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_angular_velocity_curve) |
| [float](class_float.md#class_float) | [angular_velocity_max](class_cpuparticles3d.md#class_CPUParticles3D_property_angular_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [angular_velocity_min](class_cpuparticles3d.md#class_CPUParticles3D_property_angular_velocity_min) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [anim_offset_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_offset_curve) |
| [float](class_float.md#class_float) | [anim_offset_max](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_offset_max) | `0.0` |
| [float](class_float.md#class_float) | [anim_offset_min](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_offset_min) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [anim_speed_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_speed_curve) |
| [float](class_float.md#class_float) | [anim_speed_max](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_speed_max) | `0.0` |
| [float](class_float.md#class_float) | [anim_speed_min](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_speed_min) | `0.0` |
| [Color](class_color.md#class_Color) | [color](class_cpuparticles3d.md#class_CPUParticles3D_property_color) | `Color(1, 1, 1, 1)` |
| [Gradient](class_gradient.md#class_Gradient) | [color_initial_ramp](class_cpuparticles3d.md#class_CPUParticles3D_property_color_initial_ramp) |
| [Gradient](class_gradient.md#class_Gradient) | [color_ramp](class_cpuparticles3d.md#class_CPUParticles3D_property_color_ramp) |
| [Curve](class_curve.md#class_Curve) | [damping_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_damping_curve) |
| [float](class_float.md#class_float) | [damping_max](class_cpuparticles3d.md#class_CPUParticles3D_property_damping_max) | `0.0` |
| [float](class_float.md#class_float) | [damping_min](class_cpuparticles3d.md#class_CPUParticles3D_property_damping_min) | `0.0` |
| [Vector3](class_vector3.md#class_Vector3) | [direction](class_cpuparticles3d.md#class_CPUParticles3D_property_direction) | `Vector3(1, 0, 0)` |
| [DrawOrder](class_cpuparticles3d.md#enum_CPUParticles3D_DrawOrder) | [draw_order](class_cpuparticles3d.md#class_CPUParticles3D_property_draw_order) | `0` |
| [Vector3](class_vector3.md#class_Vector3) | [emission_box_extents](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_box_extents) |
| [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) | [emission_colors](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_colors) | `PackedColorArray()` |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [emission_normals](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_normals) |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [emission_points](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_points) |
| [Vector3](class_vector3.md#class_Vector3) | [emission_ring_axis](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_axis) |
| [float](class_float.md#class_float) | [emission_ring_cone_angle](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_cone_angle) |
| [float](class_float.md#class_float) | [emission_ring_height](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_height) |
| [float](class_float.md#class_float) | [emission_ring_inner_radius](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_inner_radius) |
| [float](class_float.md#class_float) | [emission_ring_radius](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_radius) |
| [EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) | [emission_shape](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_shape) | `0` |
| [float](class_float.md#class_float) | [emission_sphere_radius](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_sphere_radius) |
| [bool](class_bool.md#class_bool) | [emitting](class_cpuparticles3d.md#class_CPUParticles3D_property_emitting) | `true` |
| [float](class_float.md#class_float) | [explosiveness](class_cpuparticles3d.md#class_CPUParticles3D_property_explosiveness) | `0.0` |
| [int](class_int.md#class_int) | [fixed_fps](class_cpuparticles3d.md#class_CPUParticles3D_property_fixed_fps) | `0` |
| [float](class_float.md#class_float) | [flatness](class_cpuparticles3d.md#class_CPUParticles3D_property_flatness) | `0.0` |
| [bool](class_bool.md#class_bool) | [fract_delta](class_cpuparticles3d.md#class_CPUParticles3D_property_fract_delta) | `true` |
| [Vector3](class_vector3.md#class_Vector3) | [gravity](class_cpuparticles3d.md#class_CPUParticles3D_property_gravity) | `Vector3(0, -9.8, 0)` |
| [Curve](class_curve.md#class_Curve) | [hue_variation_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_hue_variation_curve) |
| [float](class_float.md#class_float) | [hue_variation_max](class_cpuparticles3d.md#class_CPUParticles3D_property_hue_variation_max) | `0.0` |
| [float](class_float.md#class_float) | [hue_variation_min](class_cpuparticles3d.md#class_CPUParticles3D_property_hue_variation_min) | `0.0` |
| [float](class_float.md#class_float) | [initial_velocity_max](class_cpuparticles3d.md#class_CPUParticles3D_property_initial_velocity_max) | `0.0` |
| [float](class_float.md#class_float) | [initial_velocity_min](class_cpuparticles3d.md#class_CPUParticles3D_property_initial_velocity_min) | `0.0` |
| [float](class_float.md#class_float) | [lifetime](class_cpuparticles3d.md#class_CPUParticles3D_property_lifetime) | `1.0` |
| [float](class_float.md#class_float) | [lifetime_randomness](class_cpuparticles3d.md#class_CPUParticles3D_property_lifetime_randomness) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [linear_accel_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_linear_accel_curve) |
| [float](class_float.md#class_float) | [linear_accel_max](class_cpuparticles3d.md#class_CPUParticles3D_property_linear_accel_max) | `0.0` |
| [float](class_float.md#class_float) | [linear_accel_min](class_cpuparticles3d.md#class_CPUParticles3D_property_linear_accel_min) | `0.0` |
| [bool](class_bool.md#class_bool) | [local_coords](class_cpuparticles3d.md#class_CPUParticles3D_property_local_coords) | `false` |
| [Mesh](class_mesh.md#class_Mesh) | [mesh](class_cpuparticles3d.md#class_CPUParticles3D_property_mesh) |
| [bool](class_bool.md#class_bool) | [one_shot](class_cpuparticles3d.md#class_CPUParticles3D_property_one_shot) | `false` |
| [Curve](class_curve.md#class_Curve) | [orbit_velocity_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_orbit_velocity_curve) |
| [float](class_float.md#class_float) | [orbit_velocity_max](class_cpuparticles3d.md#class_CPUParticles3D_property_orbit_velocity_max) |
| [float](class_float.md#class_float) | [orbit_velocity_min](class_cpuparticles3d.md#class_CPUParticles3D_property_orbit_velocity_min) |
| [bool](class_bool.md#class_bool) | [particle_flag_align_y](class_cpuparticles3d.md#class_CPUParticles3D_property_particle_flag_align_y) | `false` |
| [bool](class_bool.md#class_bool) | [particle_flag_disable_z](class_cpuparticles3d.md#class_CPUParticles3D_property_particle_flag_disable_z) | `false` |
| [bool](class_bool.md#class_bool) | [particle_flag_rotate_y](class_cpuparticles3d.md#class_CPUParticles3D_property_particle_flag_rotate_y) | `false` |
| [float](class_float.md#class_float) | [preprocess](class_cpuparticles3d.md#class_CPUParticles3D_property_preprocess) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [radial_accel_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_radial_accel_curve) |
| [float](class_float.md#class_float) | [radial_accel_max](class_cpuparticles3d.md#class_CPUParticles3D_property_radial_accel_max) | `0.0` |
| [float](class_float.md#class_float) | [radial_accel_min](class_cpuparticles3d.md#class_CPUParticles3D_property_radial_accel_min) | `0.0` |
| [float](class_float.md#class_float) | [randomness](class_cpuparticles3d.md#class_CPUParticles3D_property_randomness) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [scale_amount_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_amount_curve) |
| [float](class_float.md#class_float) | [scale_amount_max](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_amount_max) | `1.0` |
| [float](class_float.md#class_float) | [scale_amount_min](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_amount_min) | `1.0` |
| [Curve](class_curve.md#class_Curve) | [scale_curve_x](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_curve_x) |
| [Curve](class_curve.md#class_Curve) | [scale_curve_y](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_curve_y) |
| [Curve](class_curve.md#class_Curve) | [scale_curve_z](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_curve_z) |
| [int](class_int.md#class_int) | [seed](class_cpuparticles3d.md#class_CPUParticles3D_property_seed) | `0` |
| [float](class_float.md#class_float) | [speed_scale](class_cpuparticles3d.md#class_CPUParticles3D_property_speed_scale) | `1.0` |
| [bool](class_bool.md#class_bool) | [split_scale](class_cpuparticles3d.md#class_CPUParticles3D_property_split_scale) | `false` |
| [float](class_float.md#class_float) | [spread](class_cpuparticles3d.md#class_CPUParticles3D_property_spread) | `45.0` |
| [Curve](class_curve.md#class_Curve) | [tangential_accel_curve](class_cpuparticles3d.md#class_CPUParticles3D_property_tangential_accel_curve) |
| [float](class_float.md#class_float) | [tangential_accel_max](class_cpuparticles3d.md#class_CPUParticles3D_property_tangential_accel_max) | `0.0` |
| [float](class_float.md#class_float) | [tangential_accel_min](class_cpuparticles3d.md#class_CPUParticles3D_property_tangential_accel_min) | `0.0` |
| [bool](class_bool.md#class_bool) | [use_fixed_seed](class_cpuparticles3d.md#class_CPUParticles3D_property_use_fixed_seed) | `false` |
| [AABB](class_aabb.md#class_AABB) | [visibility_aabb](class_cpuparticles3d.md#class_CPUParticles3D_property_visibility_aabb) | `AABB(0, 0, 0, 0, 0, 0)` |

### Methods


| [AABB](class_aabb.md#class_AABB) | [capture_aabb](class_cpuparticles3d.md#class_CPUParticles3D_method_capture_aabb) ( ) const |
| --- | --- |
| void | [convert_from_particles](class_cpuparticles3d.md#class_CPUParticles3D_method_convert_from_particles) ( particles: [Node](class_node.md#class_Node) ) |
| [Curve](class_curve.md#class_Curve) | [get_param_curve](class_cpuparticles3d.md#class_CPUParticles3D_method_get_param_curve) ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) const |
| [float](class_float.md#class_float) | [get_param_max](class_cpuparticles3d.md#class_CPUParticles3D_method_get_param_max) ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) const |
| [float](class_float.md#class_float) | [get_param_min](class_cpuparticles3d.md#class_CPUParticles3D_method_get_param_min) ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) const |
| [bool](class_bool.md#class_bool) | [get_particle_flag](class_cpuparticles3d.md#class_CPUParticles3D_method_get_particle_flag) ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) ) const |
| void | [request_particles_process](class_cpuparticles3d.md#class_CPUParticles3D_method_request_particles_process) ( process_time: [float](class_float.md#class_float) ) |
| void | [restart](class_cpuparticles3d.md#class_CPUParticles3D_method_restart) ( keep_seed: [bool](class_bool.md#class_bool) = false ) |
| void | [set_param_curve](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) ) |
| void | [set_param_max](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max) ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) ) |
| void | [set_param_min](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min) ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) ) |
| void | [set_particle_flag](class_cpuparticles3d.md#class_CPUParticles3D_method_set_particle_flag) ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags), enable: [bool](class_bool.md#class_bool) ) |

---

### Signals

<span id="class_CPUParticles3D_signal_finished"></span>

**finished** ( ) [🔗](class_cpuparticles3d.md#class_CPUParticles3D_signal_finished)

Emitted when all active particles have finished processing. When [one_shot](class_cpuparticles3d.md#class_CPUParticles3D_property_one_shot) is disabled, particles will process continuously, so this is never emitted.

---

### Enumerations

<span id="enum_CPUParticles3D_DrawOrder"></span>

enum **DrawOrder**: [🔗](class_cpuparticles3d.md#enum_CPUParticles3D_DrawOrder)

<span id="class_CPUParticles3D_constant_DRAW_ORDER_INDEX"></span>

[DrawOrder](class_cpuparticles3d.md#enum_CPUParticles3D_DrawOrder) **DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

<span id="class_CPUParticles3D_constant_DRAW_ORDER_LIFETIME"></span>

[DrawOrder](class_cpuparticles3d.md#enum_CPUParticles3D_DrawOrder) **DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the particle with the highest lifetime is drawn at the front.

<span id="class_CPUParticles3D_constant_DRAW_ORDER_VIEW_DEPTH"></span>

[DrawOrder](class_cpuparticles3d.md#enum_CPUParticles3D_DrawOrder) **DRAW_ORDER_VIEW_DEPTH** = `2`

Particles are drawn in order of depth.

---

<span id="enum_CPUParticles3D_Parameter"></span>

enum **Parameter**: [🔗](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter)

<span id="class_CPUParticles3D_constant_PARAM_INITIAL_LINEAR_VELOCITY"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set initial velocity properties.

<span id="class_CPUParticles3D_constant_PARAM_ANGULAR_VELOCITY"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_ANGULAR_VELOCITY** = `1`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set angular velocity properties.

<span id="class_CPUParticles3D_constant_PARAM_ORBIT_VELOCITY"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_ORBIT_VELOCITY** = `2`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set orbital velocity properties.

<span id="class_CPUParticles3D_constant_PARAM_LINEAR_ACCEL"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_LINEAR_ACCEL** = `3`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set linear acceleration properties.

<span id="class_CPUParticles3D_constant_PARAM_RADIAL_ACCEL"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_RADIAL_ACCEL** = `4`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set radial acceleration properties.

<span id="class_CPUParticles3D_constant_PARAM_TANGENTIAL_ACCEL"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_TANGENTIAL_ACCEL** = `5`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set tangential acceleration properties.

<span id="class_CPUParticles3D_constant_PARAM_DAMPING"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_DAMPING** = `6`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set damping properties.

<span id="class_CPUParticles3D_constant_PARAM_ANGLE"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_ANGLE** = `7`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set angle properties.

<span id="class_CPUParticles3D_constant_PARAM_SCALE"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_SCALE** = `8`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set scale properties.

<span id="class_CPUParticles3D_constant_PARAM_HUE_VARIATION"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_HUE_VARIATION** = `9`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set hue variation properties.

<span id="class_CPUParticles3D_constant_PARAM_ANIM_SPEED"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_ANIM_SPEED** = `10`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set animation speed properties.

<span id="class_CPUParticles3D_constant_PARAM_ANIM_OFFSET"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_ANIM_OFFSET** = `11`

Use with [set_param_min()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min), [set_param_max()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max), and [set_param_curve()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve) to set animation offset properties.

<span id="class_CPUParticles3D_constant_PARAM_MAX"></span>

[Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) **PARAM_MAX** = `12`

Represents the size of the [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) enum.

---

<span id="enum_CPUParticles3D_ParticleFlags"></span>

enum **ParticleFlags**: [🔗](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags)

<span id="class_CPUParticles3D_constant_PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY"></span>

[ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with [set_particle_flag()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_particle_flag) to set [particle_flag_align_y](class_cpuparticles3d.md#class_CPUParticles3D_property_particle_flag_align_y).

<span id="class_CPUParticles3D_constant_PARTICLE_FLAG_ROTATE_Y"></span>

[ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) **PARTICLE_FLAG_ROTATE_Y** = `1`

Use with [set_particle_flag()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_particle_flag) to set [particle_flag_rotate_y](class_cpuparticles3d.md#class_CPUParticles3D_property_particle_flag_rotate_y).

<span id="class_CPUParticles3D_constant_PARTICLE_FLAG_DISABLE_Z"></span>

[ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) **PARTICLE_FLAG_DISABLE_Z** = `2`

Use with [set_particle_flag()](class_cpuparticles3d.md#class_CPUParticles3D_method_set_particle_flag) to set [particle_flag_disable_z](class_cpuparticles3d.md#class_CPUParticles3D_property_particle_flag_disable_z).

<span id="class_CPUParticles3D_constant_PARTICLE_FLAG_MAX"></span>

[ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) **PARTICLE_FLAG_MAX** = `3`

Represents the size of the [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) enum.

---

<span id="enum_CPUParticles3D_EmissionShape"></span>

enum **EmissionShape**: [🔗](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape)

<span id="class_CPUParticles3D_constant_EMISSION_SHAPE_POINT"></span>

[EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

<span id="class_CPUParticles3D_constant_EMISSION_SHAPE_SPHERE"></span>

[EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere.

<span id="class_CPUParticles3D_constant_EMISSION_SHAPE_SPHERE_SURFACE"></span>

[EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere.

<span id="class_CPUParticles3D_constant_EMISSION_SHAPE_BOX"></span>

[EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **EMISSION_SHAPE_BOX** = `3`

Particles will be emitted in the volume of a box.

<span id="class_CPUParticles3D_constant_EMISSION_SHAPE_POINTS"></span>

[EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position chosen randomly among [emission_points](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_points). Particle color will be modulated by [emission_colors](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_colors).

<span id="class_CPUParticles3D_constant_EMISSION_SHAPE_DIRECTED_POINTS"></span>

[EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position chosen randomly among [emission_points](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_points). Particle velocity and rotation will be set based on [emission_normals](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_normals). Particle color will be modulated by [emission_colors](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_colors).

<span id="class_CPUParticles3D_constant_EMISSION_SHAPE_RING"></span>

[EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in a ring or cylinder.

<span id="class_CPUParticles3D_constant_EMISSION_SHAPE_MAX"></span>

[EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **EMISSION_SHAPE_MAX** = `7`

Represents the size of the [EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) enum.

---

### Property Descriptions

<span id="class_CPUParticles3D_property_amount"></span>

[int](class_int.md#class_int) **amount** = `8` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_amount)

- void **set_amount** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_amount** ( )

Number of particles emitted in one emission cycle.

---

<span id="class_CPUParticles3D_property_angle_curve"></span>

[Curve](class_curve.md#class_Curve) **angle_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_angle_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's rotation will be animated along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_angle_max"></span>

[float](class_float.md#class_float) **angle_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_angle_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum angle.

---

<span id="class_CPUParticles3D_property_angle_min"></span>

[float](class_float.md#class_float) **angle_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_angle_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum angle.

---

<span id="class_CPUParticles3D_property_angular_velocity_curve"></span>

[Curve](class_curve.md#class_Curve) **angular_velocity_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_angular_velocity_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's angular velocity (rotation speed) will vary along this [Curve](class_curve.md#class_Curve) over its lifetime. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_angular_velocity_max"></span>

[float](class_float.md#class_float) **angular_velocity_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_angular_velocity_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

---

<span id="class_CPUParticles3D_property_angular_velocity_min"></span>

[float](class_float.md#class_float) **angular_velocity_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_angular_velocity_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

---

<span id="class_CPUParticles3D_property_anim_offset_curve"></span>

[Curve](class_curve.md#class_Curve) **anim_offset_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_offset_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's animation offset will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_anim_offset_max"></span>

[float](class_float.md#class_float) **anim_offset_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_offset_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum animation offset.

---

<span id="class_CPUParticles3D_property_anim_offset_min"></span>

[float](class_float.md#class_float) **anim_offset_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_offset_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum animation offset.

---

<span id="class_CPUParticles3D_property_anim_speed_curve"></span>

[Curve](class_curve.md#class_Curve) **anim_speed_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_speed_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's animation speed will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_anim_speed_max"></span>

[float](class_float.md#class_float) **anim_speed_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_speed_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum particle animation speed.

---

<span id="class_CPUParticles3D_property_anim_speed_min"></span>

[float](class_float.md#class_float) **anim_speed_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_anim_speed_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum particle animation speed.

---

<span id="class_CPUParticles3D_property_color"></span>

[Color](class_color.md#class_Color) **color** = `Color(1, 1, 1, 1)` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_color)

- void **set_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_color** ( )

Each particle's initial color.

 **Note:** [color](class_cpuparticles3d.md#class_CPUParticles3D_property_color) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color](class_cpuparticles3d.md#class_CPUParticles3D_property_color) will have no visible effect.

---

<span id="class_CPUParticles3D_property_color_initial_ramp"></span>

[Gradient](class_gradient.md#class_Gradient) **color_initial_ramp** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_color_initial_ramp)

- void **set_color_initial_ramp** ( value: [Gradient](class_gradient.md#class_Gradient) )
- [Gradient](class_gradient.md#class_Gradient) **get_color_initial_ramp** ( )

Each particle's initial color will vary along this [Gradient](class_gradient.md#class_Gradient) (multiplied with [color](class_cpuparticles3d.md#class_CPUParticles3D_property_color)).

 **Note:** [color_initial_ramp](class_cpuparticles3d.md#class_CPUParticles3D_property_color_initial_ramp) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color_initial_ramp](class_cpuparticles3d.md#class_CPUParticles3D_property_color_initial_ramp) will have no visible effect.

---

<span id="class_CPUParticles3D_property_color_ramp"></span>

[Gradient](class_gradient.md#class_Gradient) **color_ramp** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_color_ramp)

- void **set_color_ramp** ( value: [Gradient](class_gradient.md#class_Gradient) )
- [Gradient](class_gradient.md#class_Gradient) **get_color_ramp** ( )

Each particle's color will vary along this [Gradient](class_gradient.md#class_Gradient) over its lifetime (multiplied with [color](class_cpuparticles3d.md#class_CPUParticles3D_property_color)).

 **Note:** [color_ramp](class_cpuparticles3d.md#class_CPUParticles3D_property_color_ramp) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [color_ramp](class_cpuparticles3d.md#class_CPUParticles3D_property_color_ramp) will have no visible effect.

---

<span id="class_CPUParticles3D_property_damping_curve"></span>

[Curve](class_curve.md#class_Curve) **damping_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_damping_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Damping will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_damping_max"></span>

[float](class_float.md#class_float) **damping_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_damping_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum damping.

---

<span id="class_CPUParticles3D_property_damping_min"></span>

[float](class_float.md#class_float) **damping_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_damping_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum damping.

---

<span id="class_CPUParticles3D_property_direction"></span>

[Vector3](class_vector3.md#class_Vector3) **direction** = `Vector3(1, 0, 0)` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_direction)

- void **set_direction** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_direction** ( )

Unit vector specifying the particles' emission direction.

---

<span id="class_CPUParticles3D_property_draw_order"></span>

[DrawOrder](class_cpuparticles3d.md#enum_CPUParticles3D_DrawOrder) **draw_order** = `0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_draw_order)

- void **set_draw_order** ( value: [DrawOrder](class_cpuparticles3d.md#enum_CPUParticles3D_DrawOrder) )
- [DrawOrder](class_cpuparticles3d.md#enum_CPUParticles3D_DrawOrder) **get_draw_order** ( )

Particle draw order.

---

<span id="class_CPUParticles3D_property_emission_box_extents"></span>

[Vector3](class_vector3.md#class_Vector3) **emission_box_extents** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_box_extents)

- void **set_emission_box_extents** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_emission_box_extents** ( )

The rectangle's extents if [emission_shape](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_shape) is set to [EMISSION_SHAPE_BOX](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_BOX).

---

<span id="class_CPUParticles3D_property_emission_colors"></span>

[PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **emission_colors** = `PackedColorArray()` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_colors)

- void **set_emission_colors** ( value: [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) )
- [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) **get_emission_colors** ( )

Sets the [Color](class_color.md#class_Color) s to modulate particles by when using [EMISSION_SHAPE_POINTS](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_POINTS) or [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_DIRECTED_POINTS).

 **Note:** [emission_colors](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_colors) multiplies the particle mesh's vertex colors. To have a visible effect on a [BaseMaterial3D](class_basematerial3d.md#class_BaseMaterial3D), [BaseMaterial3D.vertex_color_use_as_albedo](class_basematerial3d.md#class_BaseMaterial3D_property_vertex_color_use_as_albedo) *must* be `true`. For a [ShaderMaterial](class_shadermaterial.md#class_ShaderMaterial), `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, [emission_colors](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_colors) will have no visible effect.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray](class_packedcolorarray.md#class_PackedColorArray) for more details.

---

<span id="class_CPUParticles3D_property_emission_normals"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **emission_normals** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_normals)

- void **set_emission_normals** ( value: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) )
- [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_emission_normals** ( )

Sets the direction the particles will be emitted in when using [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_DIRECTED_POINTS).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) for more details.

---

<span id="class_CPUParticles3D_property_emission_points"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **emission_points** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_points)

- void **set_emission_points** ( value: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) )
- [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_emission_points** ( )

Sets the initial positions to spawn particles when using [EMISSION_SHAPE_POINTS](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_POINTS) or [EMISSION_SHAPE_DIRECTED_POINTS](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_DIRECTED_POINTS).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) for more details.

---

<span id="class_CPUParticles3D_property_emission_ring_axis"></span>

[Vector3](class_vector3.md#class_Vector3) **emission_ring_axis** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_axis)

- void **set_emission_ring_axis** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_emission_ring_axis** ( )

The axis of the ring when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_RING).

---

<span id="class_CPUParticles3D_property_emission_ring_cone_angle"></span>

[float](class_float.md#class_float) **emission_ring_cone_angle** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_cone_angle)

- void **set_emission_ring_cone_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_cone_angle** ( )

The angle of the cone when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_RING). The default angle of 90 degrees results in a ring, while an angle of 0 degrees results in a cone. Intermediate values will result in a ring where one end is larger than the other.

 **Note:** Depending on [emission_ring_height](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_height), the angle may be clamped if the ring's end is reached to form a perfect cone.

---

<span id="class_CPUParticles3D_property_emission_ring_height"></span>

[float](class_float.md#class_float) **emission_ring_height** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_height)

- void **set_emission_ring_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_height** ( )

The height of the ring when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_RING).

---

<span id="class_CPUParticles3D_property_emission_ring_inner_radius"></span>

[float](class_float.md#class_float) **emission_ring_inner_radius** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_inner_radius)

- void **set_emission_ring_inner_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_inner_radius** ( )

The inner radius of the ring when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_RING).

---

<span id="class_CPUParticles3D_property_emission_ring_radius"></span>

[float](class_float.md#class_float) **emission_ring_radius** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_ring_radius)

- void **set_emission_ring_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_ring_radius** ( )

The radius of the ring when using the emitter [EMISSION_SHAPE_RING](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_RING).

---

<span id="class_CPUParticles3D_property_emission_shape"></span>

[EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **emission_shape** = `0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_shape)

- void **set_emission_shape** ( value: [EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) )
- [EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) **get_emission_shape** ( )

Particles will be emitted inside this region.

---

<span id="class_CPUParticles3D_property_emission_sphere_radius"></span>

[float](class_float.md#class_float) **emission_sphere_radius** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emission_sphere_radius)

- void **set_emission_sphere_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_emission_sphere_radius** ( )

The sphere's radius if [EmissionShape](class_cpuparticles3d.md#enum_CPUParticles3D_EmissionShape) is set to [EMISSION_SHAPE_SPHERE](class_cpuparticles3d.md#class_CPUParticles3D_constant_EMISSION_SHAPE_SPHERE).

---

<span id="class_CPUParticles3D_property_emitting"></span>

[bool](class_bool.md#class_bool) **emitting** = `true` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_emitting)

- void **set_emitting** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_emitting** ( )

If `true`, particles are being emitted. [emitting](class_cpuparticles3d.md#class_CPUParticles3D_property_emitting) can be used to start and stop particles from emitting. However, if [one_shot](class_cpuparticles3d.md#class_CPUParticles3D_property_one_shot) is `true` setting [emitting](class_cpuparticles3d.md#class_CPUParticles3D_property_emitting) to `true` will not restart the emission cycle until after all active particles finish processing. You can use the [finished](class_cpuparticles3d.md#class_CPUParticles3D_signal_finished) signal to be notified once all active particles finish processing.

---

<span id="class_CPUParticles3D_property_explosiveness"></span>

[float](class_float.md#class_float) **explosiveness** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_explosiveness)

- void **set_explosiveness_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_explosiveness_ratio** ( )

How rapidly particles in an emission cycle are emitted. If greater than `0`, there will be a gap in emissions before the next cycle begins.

---

<span id="class_CPUParticles3D_property_fixed_fps"></span>

[int](class_int.md#class_int) **fixed_fps** = `0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_fixed_fps)

- void **set_fixed_fps** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_fixed_fps** ( )

The particle system's frame rate is fixed to a value. For example, changing the value to 2 will make the particles render at 2 frames per second. Note this does not slow down the particle system itself.

---

<span id="class_CPUParticles3D_property_flatness"></span>

[float](class_float.md#class_float) **flatness** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_flatness)

- void **set_flatness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_flatness** ( )

Amount of [spread](class_cpuparticles3d.md#class_CPUParticles3D_property_spread) in Y/Z plane. A value of `1` restricts particles to X/Z plane.

---

<span id="class_CPUParticles3D_property_fract_delta"></span>

[bool](class_bool.md#class_bool) **fract_delta** = `true` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_fract_delta)

- void **set_fractional_delta** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_fractional_delta** ( )

If `true`, results in fractional delta calculation which has a smoother particles display effect.

---

<span id="class_CPUParticles3D_property_gravity"></span>

[Vector3](class_vector3.md#class_Vector3) **gravity** = `Vector3(0, -9.8, 0)` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_gravity)

- void **set_gravity** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_gravity** ( )

Gravity applied to every particle.

---

<span id="class_CPUParticles3D_property_hue_variation_curve"></span>

[Curve](class_curve.md#class_Curve) **hue_variation_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_hue_variation_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's hue will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_hue_variation_max"></span>

[float](class_float.md#class_float) **hue_variation_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_hue_variation_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum hue variation.

---

<span id="class_CPUParticles3D_property_hue_variation_min"></span>

[float](class_float.md#class_float) **hue_variation_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_hue_variation_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum hue variation.

---

<span id="class_CPUParticles3D_property_initial_velocity_max"></span>

[float](class_float.md#class_float) **initial_velocity_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_initial_velocity_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum value of the initial velocity.

---

<span id="class_CPUParticles3D_property_initial_velocity_min"></span>

[float](class_float.md#class_float) **initial_velocity_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_initial_velocity_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum value of the initial velocity.

---

<span id="class_CPUParticles3D_property_lifetime"></span>

[float](class_float.md#class_float) **lifetime** = `1.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_lifetime)

- void **set_lifetime** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_lifetime** ( )

Amount of time each particle will exist.

---

<span id="class_CPUParticles3D_property_lifetime_randomness"></span>

[float](class_float.md#class_float) **lifetime_randomness** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_lifetime_randomness)

- void **set_lifetime_randomness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_lifetime_randomness** ( )

Particle lifetime randomness ratio.

---

<span id="class_CPUParticles3D_property_linear_accel_curve"></span>

[Curve](class_curve.md#class_Curve) **linear_accel_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_linear_accel_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's linear acceleration will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_linear_accel_max"></span>

[float](class_float.md#class_float) **linear_accel_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_linear_accel_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum linear acceleration.

---

<span id="class_CPUParticles3D_property_linear_accel_min"></span>

[float](class_float.md#class_float) **linear_accel_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_linear_accel_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum linear acceleration.

---

<span id="class_CPUParticles3D_property_local_coords"></span>

[bool](class_bool.md#class_bool) **local_coords** = `false` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_local_coords)

- void **set_use_local_coordinates** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_local_coordinates** ( )

If `true`, particles use the parent node's coordinate space (known as local coordinates). This will cause particles to move and rotate along the **CPUParticles3D** node (and its parents) when it is moved or rotated. If `false`, particles use global coordinates; they will not move or rotate along the **CPUParticles3D** node (and its parents) when it is moved or rotated.

---

<span id="class_CPUParticles3D_property_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **mesh** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_mesh)

- void **set_mesh** ( value: [Mesh](class_mesh.md#class_Mesh) )
- [Mesh](class_mesh.md#class_Mesh) **get_mesh** ( )

The [Mesh](class_mesh.md#class_Mesh) used for each particle. If `null`, particles will be spheres.

---

<span id="class_CPUParticles3D_property_one_shot"></span>

[bool](class_bool.md#class_bool) **one_shot** = `false` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_one_shot)

- void **set_one_shot** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_one_shot** ( )

If `true`, only one emission cycle occurs. If set `true` during a cycle, emission will stop at the cycle's end.

---

<span id="class_CPUParticles3D_property_orbit_velocity_curve"></span>

[Curve](class_curve.md#class_Curve) **orbit_velocity_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_orbit_velocity_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's orbital velocity will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_orbit_velocity_max"></span>

[float](class_float.md#class_float) **orbit_velocity_max** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_orbit_velocity_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum orbit velocity.

---

<span id="class_CPUParticles3D_property_orbit_velocity_min"></span>

[float](class_float.md#class_float) **orbit_velocity_min** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_orbit_velocity_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum orbit velocity.

---

<span id="class_CPUParticles3D_property_particle_flag_align_y"></span>

[bool](class_bool.md#class_bool) **particle_flag_align_y** = `false` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_particle_flag_align_y)

- void **set_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) ) *const*

Align Y axis of particle with the direction of its velocity.

---

<span id="class_CPUParticles3D_property_particle_flag_disable_z"></span>

[bool](class_bool.md#class_bool) **particle_flag_disable_z** = `false` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_particle_flag_disable_z)

- void **set_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) ) *const*

If `true`, particles will not move on the Z axis.

---

<span id="class_CPUParticles3D_property_particle_flag_rotate_y"></span>

[bool](class_bool.md#class_bool) **particle_flag_rotate_y** = `false` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_particle_flag_rotate_y)

- void **set_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags), enable: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) ) *const*

If `true`, particles rotate around Y axis by [angle_min](class_cpuparticles3d.md#class_CPUParticles3D_property_angle_min).

---

<span id="class_CPUParticles3D_property_preprocess"></span>

[float](class_float.md#class_float) **preprocess** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_preprocess)

- void **set_pre_process_time** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_pre_process_time** ( )

Particle system starts as if it had already run for this many seconds.

---

<span id="class_CPUParticles3D_property_radial_accel_curve"></span>

[Curve](class_curve.md#class_Curve) **radial_accel_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_radial_accel_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's radial acceleration will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_radial_accel_max"></span>

[float](class_float.md#class_float) **radial_accel_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_radial_accel_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum radial acceleration.

---

<span id="class_CPUParticles3D_property_radial_accel_min"></span>

[float](class_float.md#class_float) **radial_accel_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_radial_accel_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum radial acceleration.

---

<span id="class_CPUParticles3D_property_randomness"></span>

[float](class_float.md#class_float) **randomness** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_randomness)

- void **set_randomness_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_randomness_ratio** ( )

Emission lifetime randomness ratio.

---

<span id="class_CPUParticles3D_property_scale_amount_curve"></span>

[Curve](class_curve.md#class_Curve) **scale_amount_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_amount_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's scale will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_scale_amount_max"></span>

[float](class_float.md#class_float) **scale_amount_max** = `1.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_amount_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum scale.

---

<span id="class_CPUParticles3D_property_scale_amount_min"></span>

[float](class_float.md#class_float) **scale_amount_min** = `1.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_amount_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum scale.

---

<span id="class_CPUParticles3D_property_scale_curve_x"></span>

[Curve](class_curve.md#class_Curve) **scale_curve_x** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_curve_x)

- void **set_scale_curve_x** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_scale_curve_x** ( )

Curve for the scale over life, along the x axis.

---

<span id="class_CPUParticles3D_property_scale_curve_y"></span>

[Curve](class_curve.md#class_Curve) **scale_curve_y** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_curve_y)

- void **set_scale_curve_y** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_scale_curve_y** ( )

Curve for the scale over life, along the y axis.

---

<span id="class_CPUParticles3D_property_scale_curve_z"></span>

[Curve](class_curve.md#class_Curve) **scale_curve_z** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_scale_curve_z)

- void **set_scale_curve_z** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_scale_curve_z** ( )

Curve for the scale over life, along the z axis.

---

<span id="class_CPUParticles3D_property_seed"></span>

[int](class_int.md#class_int) **seed** = `0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_seed)

- void **set_seed** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_seed** ( )

Sets the random seed used by the particle system. Only effective if [use_fixed_seed](class_cpuparticles3d.md#class_CPUParticles3D_property_use_fixed_seed) is `true`.

---

<span id="class_CPUParticles3D_property_speed_scale"></span>

[float](class_float.md#class_float) **speed_scale** = `1.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_speed_scale)

- void **set_speed_scale** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_speed_scale** ( )

Particle system's running speed scaling ratio. A value of `0` can be used to pause the particles.

---

<span id="class_CPUParticles3D_property_split_scale"></span>

[bool](class_bool.md#class_bool) **split_scale** = `false` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_split_scale)

- void **set_split_scale** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_split_scale** ( )

If set to `true`, three different scale curves can be specified, one per scale axis.

---

<span id="class_CPUParticles3D_property_spread"></span>

[float](class_float.md#class_float) **spread** = `45.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_spread)

- void **set_spread** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_spread** ( )

Each particle's initial direction range from `+spread` to `-spread` degrees. Applied to X/Z plane and Y/Z planes.

---

<span id="class_CPUParticles3D_property_tangential_accel_curve"></span>

[Curve](class_curve.md#class_Curve) **tangential_accel_curve** [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_tangential_accel_curve)

- void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Each particle's tangential acceleration will vary along this [Curve](class_curve.md#class_Curve). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_property_tangential_accel_max"></span>

[float](class_float.md#class_float) **tangential_accel_max** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_tangential_accel_max)

- void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Maximum tangent acceleration.

---

<span id="class_CPUParticles3D_property_tangential_accel_min"></span>

[float](class_float.md#class_float) **tangential_accel_min** = `0.0` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_tangential_accel_min)

- void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const*

Minimum tangent acceleration.

---

<span id="class_CPUParticles3D_property_use_fixed_seed"></span>

[bool](class_bool.md#class_bool) **use_fixed_seed** = `false` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_use_fixed_seed)

- void **set_use_fixed_seed** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_fixed_seed** ( )

If `true`, particles will use the same seed for every simulation using the seed defined in [seed](class_cpuparticles3d.md#class_CPUParticles3D_property_seed). This is useful for situations where the visual outcome should be consistent across replays, for example when using Movie Maker mode.

---

<span id="class_CPUParticles3D_property_visibility_aabb"></span>

[AABB](class_aabb.md#class_AABB) **visibility_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_cpuparticles3d.md#class_CPUParticles3D_property_visibility_aabb)

- void **set_visibility_aabb** ( value: [AABB](class_aabb.md#class_AABB) )
- [AABB](class_aabb.md#class_AABB) **get_visibility_aabb** ( )

The [AABB](class_aabb.md#class_AABB) that determines the node's region which needs to be visible on screen for the particle system to be active.

Grow the box if particles suddenly appear/disappear when the node enters/exits the screen. The [AABB](class_aabb.md#class_AABB) can be grown via code or with the **Particles → Generate AABB** editor tool.

---

### Method Descriptions

<span id="class_CPUParticles3D_method_capture_aabb"></span>

[AABB](class_aabb.md#class_AABB) **capture_aabb** ( ) *const* [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_capture_aabb)

Returns the axis-aligned bounding box that contains all the particles that are active in the current frame.

---

<span id="class_CPUParticles3D_method_convert_from_particles"></span>

void **convert_from_particles** ( particles: [Node](class_node.md#class_Node) ) [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_convert_from_particles)

Sets this node's properties to match a given [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) node with an assigned [ParticleProcessMaterial](class_particleprocessmaterial.md#class_ParticleProcessMaterial).

---

<span id="class_CPUParticles3D_method_get_param_curve"></span>

[Curve](class_curve.md#class_Curve) **get_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const* [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_get_param_curve)

Returns the [Curve](class_curve.md#class_Curve) of the parameter specified by [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter).

---

<span id="class_CPUParticles3D_method_get_param_max"></span>

[float](class_float.md#class_float) **get_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const* [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_get_param_max)

Returns the maximum value range for the given parameter.

---

<span id="class_CPUParticles3D_method_get_param_min"></span>

[float](class_float.md#class_float) **get_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter) ) *const* [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_get_param_min)

Returns the minimum value range for the given parameter.

---

<span id="class_CPUParticles3D_method_get_particle_flag"></span>

[bool](class_bool.md#class_bool) **get_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags) ) *const* [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_get_particle_flag)

Returns the enabled state of the given particle flag.

---

<span id="class_CPUParticles3D_method_request_particles_process"></span>

void **request_particles_process** ( process_time: [float](class_float.md#class_float) ) [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_request_particles_process)

Requests the particles to process for extra process time during a single frame.

Useful for particle playback, if used in combination with [use_fixed_seed](class_cpuparticles3d.md#class_CPUParticles3D_property_use_fixed_seed) or by calling [restart()](class_cpuparticles3d.md#class_CPUParticles3D_method_restart) with parameter `keep_seed` set to `true`.

---

<span id="class_CPUParticles3D_method_restart"></span>

void **restart** ( keep_seed: [bool](class_bool.md#class_bool) = false ) [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_restart)

Restarts the particle emitter.

If `keep_seed` is `true`, the current random seed will be preserved. Useful for seeking and playback.

---

<span id="class_CPUParticles3D_method_set_param_curve"></span>

void **set_param_curve** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), curve: [Curve](class_curve.md#class_Curve) ) [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_curve)

Sets the [Curve](class_curve.md#class_Curve) of the parameter specified by [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter). Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_CPUParticles3D_method_set_param_max"></span>

void **set_param_max** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) ) [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_max)

Sets the maximum value for the given parameter.

---

<span id="class_CPUParticles3D_method_set_param_min"></span>

void **set_param_min** ( param: [Parameter](class_cpuparticles3d.md#enum_CPUParticles3D_Parameter), value: [float](class_float.md#class_float) ) [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_set_param_min)

Sets the minimum value for the given parameter.

---

<span id="class_CPUParticles3D_method_set_particle_flag"></span>

void **set_particle_flag** ( particle_flag: [ParticleFlags](class_cpuparticles3d.md#enum_CPUParticles3D_ParticleFlags), enable: [bool](class_bool.md#class_bool) ) [🔗](class_cpuparticles3d.md#class_CPUParticles3D_method_set_particle_flag)

Enables or disables the given particle flag.
