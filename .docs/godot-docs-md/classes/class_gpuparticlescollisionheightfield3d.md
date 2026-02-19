<span id="class_GPUParticlesCollisionHeightField3D"></span>

## GPUParticlesCollisionHeightField3D

**Inherits:** [GPUParticlesCollision3D](class_gpuparticlescollision3d.md#class_GPUParticlesCollision3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A real-time heightmap-shaped 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes.

### Description

A real-time heightmap-shaped 3D particle collision shape affecting [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes.

Heightmap shapes allow for efficiently representing collisions for convex and concave objects with a single "floor" (such as terrain). This is less flexible than [GPUParticlesCollisionSDF3D](class_gpuparticlescollisionsdf3d.md#class_GPUParticlesCollisionSDF3D), but it doesn't require a baking step.

 **GPUParticlesCollisionHeightField3D** can also be regenerated in real-time when it is moved, when the camera moves, or even continuously. This makes **GPUParticlesCollisionHeightField3D** a good choice for weather effects such as rain and snow and games with highly dynamic geometry. However, this class is limited since heightmaps cannot represent overhangs (e.g. indoors or caves).

 **Note:** [ParticleProcessMaterial.collision_mode](class_particleprocessmaterial.md#class_ParticleProcessMaterial_property_collision_mode) must be `true` on the [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D)'s process material for collision to work.

 **Note:** Particle collision only affects [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D), not [CPUParticles3D](class_cpuparticles3d.md#class_CPUParticles3D).

### Properties


| [bool](class_bool.md#class_bool) | [follow_camera_enabled](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_follow_camera_enabled) | `false` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [heightfield_mask](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask) | `1048575` |
| [Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) | [resolution](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_resolution) | `2` |
| [Vector3](class_vector3.md#class_Vector3) | [size](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_size) | `Vector3(2, 2, 2)` |
| [UpdateMode](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_UpdateMode) | [update_mode](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_update_mode) | `0` |

### Methods


| [bool](class_bool.md#class_bool) | [get_heightfield_mask_value](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_method_get_heightfield_mask_value) ( layer_number: [int](class_int.md#class_int) ) const |
| --- | --- |
| void | [set_heightfield_mask_value](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_method_set_heightfield_mask_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |

---

### Enumerations

<span id="enum_GPUParticlesCollisionHeightField3D_Resolution"></span>

enum **Resolution**: [🔗](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution)

<span id="class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_256"></span>

[Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) **RESOLUTION_256** = `0`

Generate a 256×256 heightmap. Intended for small-scale scenes, or larger scenes with no distant particles.

<span id="class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_512"></span>

[Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) **RESOLUTION_512** = `1`

Generate a 512×512 heightmap. Intended for medium-scale scenes, or larger scenes with no distant particles.

<span id="class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_1024"></span>

[Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) **RESOLUTION_1024** = `2`

Generate a 1024×1024 heightmap. Intended for large scenes with distant particles.

<span id="class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_2048"></span>

[Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) **RESOLUTION_2048** = `3`

Generate a 2048×2048 heightmap. Intended for very large scenes with distant particles.

<span id="class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_4096"></span>

[Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) **RESOLUTION_4096** = `4`

Generate a 4096×4096 heightmap. Intended for huge scenes with distant particles.

<span id="class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_8192"></span>

[Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) **RESOLUTION_8192** = `5`

Generate a 8192×8192 heightmap. Intended for gigantic scenes with distant particles.

<span id="class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_MAX"></span>

[Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) **RESOLUTION_MAX** = `6`

Represents the size of the [Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) enum.

---

<span id="enum_GPUParticlesCollisionHeightField3D_UpdateMode"></span>

enum **UpdateMode**: [🔗](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_UpdateMode)

<span id="class_GPUParticlesCollisionHeightField3D_constant_UPDATE_MODE_WHEN_MOVED"></span>

[UpdateMode](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_UpdateMode) **UPDATE_MODE_WHEN_MOVED** = `0`

Only update the heightmap when the **GPUParticlesCollisionHeightField3D** node is moved, or when the camera moves if [follow_camera_enabled](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_follow_camera_enabled) is `true`. An update can be forced by slightly moving the **GPUParticlesCollisionHeightField3D** in any direction, or by calling [RenderingServer.particles_collision_height_field_update()](class_renderingserver.md#class_RenderingServer_method_particles_collision_height_field_update).

<span id="class_GPUParticlesCollisionHeightField3D_constant_UPDATE_MODE_ALWAYS"></span>

[UpdateMode](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_UpdateMode) **UPDATE_MODE_ALWAYS** = `1`

Update the heightmap every frame. This has a significant performance cost. This update should only be used when geometry that particles can collide with changes significantly during gameplay.

---

### Property Descriptions

<span id="class_GPUParticlesCollisionHeightField3D_property_follow_camera_enabled"></span>

[bool](class_bool.md#class_bool) **follow_camera_enabled** = `false` [🔗](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_follow_camera_enabled)

- void **set_follow_camera_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_follow_camera_enabled** ( )

If `true`, the **GPUParticlesCollisionHeightField3D** will follow the current camera in global space. The **GPUParticlesCollisionHeightField3D** does not need to be a child of the [Camera3D](class_camera3d.md#class_Camera3D) node for this to work.

Following the camera has a performance cost, as it will force the heightmap to update whenever the camera moves. Consider lowering [resolution](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_resolution) to improve performance if [follow_camera_enabled](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_follow_camera_enabled) is `true`.

---

<span id="class_GPUParticlesCollisionHeightField3D_property_heightfield_mask"></span>

[int](class_int.md#class_int) **heightfield_mask** = `1048575` [🔗](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask)

- void **set_heightfield_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_heightfield_mask** ( )

The visual layers to account for when updating the heightmap. Only [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) s whose [VisualInstance3D.layers](class_visualinstance3d.md#class_VisualInstance3D_property_layers) match with this [heightfield_mask](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask) will be included in the heightmap collision update. By default, all 20 user-visible layers are taken into account for updating the heightmap collision.

 **Note:** Since the [heightfield_mask](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask) allows for 32 layers to be stored in total, there are an additional 12 layers that are only used internally by the engine and aren't exposed in the editor. Setting [heightfield_mask](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask) using a script allows you to toggle those reserved layers, which can be useful for editor plugins.

To adjust [heightfield_mask](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask) more easily using a script, use [get_heightfield_mask_value()](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_method_get_heightfield_mask_value) and [set_heightfield_mask_value()](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_method_set_heightfield_mask_value).

---

<span id="class_GPUParticlesCollisionHeightField3D_property_resolution"></span>

[Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) **resolution** = `2` [🔗](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_resolution)

- void **set_resolution** ( value: [Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) )
- [Resolution](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_Resolution) **get_resolution** ( )

Higher resolutions can represent small details more accurately in large scenes, at the cost of lower performance. If [update_mode](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_update_mode) is [UPDATE_MODE_ALWAYS](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_constant_UPDATE_MODE_ALWAYS), consider using the lowest resolution possible.

---

<span id="class_GPUParticlesCollisionHeightField3D_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(2, 2, 2)` [🔗](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The collision heightmap's size in 3D units. To improve heightmap quality, [size](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_size) should be set as small as possible while covering the parts of the scene you need.

---

<span id="class_GPUParticlesCollisionHeightField3D_property_update_mode"></span>

[UpdateMode](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_UpdateMode) **update_mode** = `0` [🔗](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_update_mode)

- void **set_update_mode** ( value: [UpdateMode](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_UpdateMode) )
- [UpdateMode](class_gpuparticlescollisionheightfield3d.md#enum_GPUParticlesCollisionHeightField3D_UpdateMode) **get_update_mode** ( )

The update policy to use for the generated heightmap.

---

### Method Descriptions

<span id="class_GPUParticlesCollisionHeightField3D_method_get_heightfield_mask_value"></span>

[bool](class_bool.md#class_bool) **get_heightfield_mask_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_method_get_heightfield_mask_value)

Returns `true` if the specified layer of the [heightfield_mask](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask) is enabled, given a `layer_number` between `1` and `20`, inclusive.

---

<span id="class_GPUParticlesCollisionHeightField3D_method_set_heightfield_mask_value"></span>

void **set_heightfield_mask_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_method_set_heightfield_mask_value)

Based on `value`, enables or disables the specified layer in the [heightfield_mask](class_gpuparticlescollisionheightfield3d.md#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask), given a `layer_number` between `1` and `20`, inclusive.
