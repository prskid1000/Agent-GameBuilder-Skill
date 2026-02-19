<span id="class_GPUParticlesAttractorSphere3D"></span>

## GPUParticlesAttractorSphere3D

**Inherits:** [GPUParticlesAttractor3D](class_gpuparticlesattractor3d.md#class_GPUParticlesAttractor3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A spheroid-shaped attractor that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes.

### Description

A spheroid-shaped attractor that influences particles from [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D) nodes. Can be used to attract particles towards its origin, or to push them away from its origin.

Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.

 **Note:** Particle attractors only affect [GPUParticles3D](class_gpuparticles3d.md#class_GPUParticles3D), not [CPUParticles3D](class_cpuparticles3d.md#class_CPUParticles3D).

### Properties


| [float](class_float.md#class_float) | [radius](class_gpuparticlesattractorsphere3d.md#class_GPUParticlesAttractorSphere3D_property_radius) | `1.0` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_GPUParticlesAttractorSphere3D_property_radius"></span>

[float](class_float.md#class_float) **radius** = `1.0` [🔗](class_gpuparticlesattractorsphere3d.md#class_GPUParticlesAttractorSphere3D_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The attractor sphere's radius in 3D units.

 **Note:** Stretched ellipses can be obtained by using non-uniform scaling on the **GPUParticlesAttractorSphere3D** node.
