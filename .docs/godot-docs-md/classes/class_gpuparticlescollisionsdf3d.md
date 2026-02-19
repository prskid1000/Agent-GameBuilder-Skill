<span id="class_GPUParticlesCollisionSDF3D"></span>

## GPUParticlesCollisionSDF3D

**Inherits:** [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A baked signed distance field 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes.

### Description

A baked signed distance field 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes.

Signed distance fields (SDF) allow for efficiently representing approximate collision shapes for convex and concave objects of any shape. This is more flexible than [GPUParticlesCollisionHeightField3D](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D), but it requires a baking step.

 **Baking:** The signed distance field texture can be baked by selecting the **GPUParticlesCollisionSDF3D** node in the editor, then clicking **Bake SDF** at the top of the 3D viewport. Any *visible* [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) s within the [size](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_size) will be taken into account for baking, regardless of their [GeometryInstance3D.gi_mode](class_geometryinstance3d.md#class_GeometryInstance3D_property_gi_mode).

 **Note:** Baking a **GPUParticlesCollisionSDF3D**'s [texture](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_texture) is only possible within the editor, as there is no bake method exposed for use in exported projects. However, it's still possible to load pre-baked [Texture3D](class_texture3d.md#class_Texture3D) s into its [texture](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_texture) property in an exported project.

 **Note:** [ParticleProcessMaterial.collision_mode](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_mode) must be [ParticleProcessMaterial.COLLISION_RIGID](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_COLLISION_RIGID) or [ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT](class_particleprocessmaterial.md#class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT) on the [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D)'s process material for collision to work.

 **Note:** Particle collision only affects [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D), not [CPUParticles3D](class_cpuparticles3d.md#class_CPUParticles3D).

### Properties


| [int](class_int.md#class_int) | [bake_mask](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_bake_mask) | `4294967295` |
| --- | --- | --- |
| [Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) | [resolution](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_resolution) | `2` |
| [Vector3](class_vector3.md#class_Vector3) | [size](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_size) | `Vector3(2, 2, 2)` |
| [Texture3D](class_texture3d.md#class_Texture3D) | [texture](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_texture) |
| [float](class_float.md#class_float) | [thickness](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_thickness) | `1.0` |

### Methods


| [bool](class_bool.md#class_bool) | [get_bake_mask_value](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_method_get_bake_mask_value) ( layer_number: [int](class_int.md#class_int) ) const |
| --- | --- |
| void | [set_bake_mask_value](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_method_set_bake_mask_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |

---

### Enumerations

<span id="enum_GPUParticlesCollisionSDF3D_Resolution"></span>

enum **Resolution**: [🔗](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution)

<span id="class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_16"></span>

[Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) **RESOLUTION_16** = `0`

Bake a 16×16×16 signed distance field. This is the fastest option, but also the least precise.

<span id="class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_32"></span>

[Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) **RESOLUTION_32** = `1`

Bake a 32×32×32 signed distance field.

<span id="class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_64"></span>

[Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) **RESOLUTION_64** = `2`

Bake a 64×64×64 signed distance field.

<span id="class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_128"></span>

[Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) **RESOLUTION_128** = `3`

Bake a 128×128×128 signed distance field.

<span id="class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_256"></span>

[Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) **RESOLUTION_256** = `4`

Bake a 256×256×256 signed distance field.

<span id="class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_512"></span>

[Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) **RESOLUTION_512** = `5`

Bake a 512×512×512 signed distance field. This is the slowest option, but also the most precise.

<span id="class_GPUParticlesCollisionSDF3D_constant_RESOLUTION_MAX"></span>

[Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) **RESOLUTION_MAX** = `6`

Represents the size of the [Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) enum.

---

### Property Descriptions

<span id="class_GPUParticlesCollisionSDF3D_property_bake_mask"></span>

[int](class_int.md#class_int) **bake_mask** = `4294967295` [🔗](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_bake_mask)

- void **set_bake_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bake_mask** ( )

The visual layers to account for when baking the particle collision SDF. Only [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) s whose [VisualInstance3D.layers](class_visualinstance3d.md#class_VisualInstance3D_property_layers) match with this [bake_mask](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_bake_mask) will be included in the generated particle collision SDF. By default, all objects are taken into account for the particle collision SDF baking.

---

<span id="class_GPUParticlesCollisionSDF3D_property_resolution"></span>

[Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) **resolution** = `2` [🔗](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_resolution)

- void **set_resolution** ( value: [Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) )
- [Resolution](class_gpuparticlescollisionsdf3d.md#enum_GPUParticlesCollisionSDF3D_Resolution) **get_resolution** ( )

The bake resolution to use for the signed distance field [texture](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_texture). The texture must be baked again for changes to the [resolution](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_resolution) property to be effective. Higher resolutions have a greater performance cost and take more time to bake. Higher resolutions also result in larger baked textures, leading to increased VRAM and storage space requirements. To improve performance and reduce bake times, use the lowest resolution possible for the object you're representing the collision of.

---

<span id="class_GPUParticlesCollisionSDF3D_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(2, 2, 2)` [🔗](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The collision SDF's size in 3D units. To improve SDF quality, the [size](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_size) should be set as small as possible while covering the parts of the scene you need.

---

<span id="class_GPUParticlesCollisionSDF3D_property_texture"></span>

[Texture3D](class_texture3d.md#class_Texture3D) **texture** [🔗](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_texture)

- void **set_texture** ( value: [Texture3D](class_texture3d.md#class_Texture3D) )
- [Texture3D](class_texture3d.md#class_Texture3D) **get_texture** ( )

The 3D texture representing the signed distance field.

---

<span id="class_GPUParticlesCollisionSDF3D_property_thickness"></span>

[float](class_float.md#class_float) **thickness** = `1.0` [🔗](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_thickness)

- void **set_thickness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_thickness** ( )

The collision shape's thickness. Unlike other particle colliders, **GPUParticlesCollisionSDF3D** is actually hollow on the inside. [thickness](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_thickness) can be increased to prevent particles from tunneling through the collision shape at high speeds, or when the **GPUParticlesCollisionSDF3D** is moved.

---

### Method Descriptions

<span id="class_GPUParticlesCollisionSDF3D_method_get_bake_mask_value"></span>

[bool](class_bool.md#class_bool) **get_bake_mask_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_method_get_bake_mask_value)

Returns whether or not the specified layer of the [bake_mask](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_bake_mask) is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_GPUParticlesCollisionSDF3D_method_set_bake_mask_value"></span>

void **set_bake_mask_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_method_set_bake_mask_value)

Based on `value`, enables or disables the specified layer in the [bake_mask](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D_property_bake_mask), given a `layer_number` between 1 and 32.
