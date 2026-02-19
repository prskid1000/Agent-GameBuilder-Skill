<span id="class_GPUParticlesAttractorBox3D"></span>

## GPUParticlesAttractorBox3D

**Inherits:** [GPUParticlesAttractor3D](class_gpuparticlesattractor3d.md#class_GPUParticlesAttractor3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A box-shaped attractor that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes.

### Description

A box-shaped attractor that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes. Can be used to attract particles towards its origin, or to push them away from its origin.

Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.

 **Note:** Particle attractors only affect [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D), not [CPUParticles3D](class_cpuparticles3d.md#class_CPUParticles3D).

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [size](class_gpuparticlesattractorbox3d.md#class_GPUParticlesAttractorBox3D_property_size) | `Vector3(2, 2, 2)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_GPUParticlesAttractorBox3D_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(2, 2, 2)` [🔗](class_gpuparticlesattractorbox3d.md#class_GPUParticlesAttractorBox3D_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The attractor box's size in 3D units.
