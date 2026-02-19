<span id="class_GPUParticlesAttractorVectorField3D"></span>

## GPUParticlesAttractorVectorField3D

**Inherits:** [GPUParticlesAttractor3D](class_gpuparticlesattractor3d.md#class_GPUParticlesAttractor3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A box-shaped attractor with varying directions and strengths defined in it that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes.

### Description

A box-shaped attractor with varying directions and strengths defined in it that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes.

Unlike [GPUParticlesAttractorBox3D](class_gpuparticlesattractorbox3d.md#class_GPUParticlesAttractorBox3D), **GPUParticlesAttractorVectorField3D** uses a [texture](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D_property_texture) to affect attraction strength within the box. This can be used to create complex attraction scenarios where particles travel in different directions depending on their location. This can be useful for weather effects such as sandstorms.

Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.

 **Note:** Particle attractors only affect [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D), not [CPUParticles3D](class_cpuparticles3d.md#class_CPUParticles3D).

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [size](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D_property_size) | `Vector3(2, 2, 2)` |
| --- | --- | --- |
| [Texture3D](class_texture3d.md#class_Texture3D) | [texture](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D_property_texture) |

---

### Property Descriptions

<span id="class_GPUParticlesAttractorVectorField3D_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(2, 2, 2)` [🔗](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The size of the vector field box in 3D units.

---

<span id="class_GPUParticlesAttractorVectorField3D_property_texture"></span>

[Texture3D](class_texture3d.md#class_Texture3D) **texture** [🔗](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D_property_texture)

- void **set_texture** ( value: [Texture3D](class_texture3d.md#class_Texture3D) )
- [Texture3D](class_texture3d.md#class_Texture3D) **get_texture** ( )

The 3D texture to be used. Values are linearly interpolated between the texture's pixels.

 **Note:** To get better performance, the 3D texture's resolution should reflect the [size](class_gpuparticlesattractorvectorfield3d.md#class_GPUParticlesAttractorVectorField3D_property_size) of the attractor. Since particle attraction is usually low-frequency data, the texture can be kept at a low resolution such as 64×64×64.
