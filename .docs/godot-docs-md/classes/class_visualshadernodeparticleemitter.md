<span id="class_VisualShaderNodeParticleEmitter"></span>

## VisualShaderNodeParticleEmitter

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [VisualShaderNodeParticleBoxEmitter](class_visualshadernodeparticleboxemitter.md#class_VisualShaderNodeParticleBoxEmitter), [VisualShaderNodeParticleMeshEmitter](class_visualshadernodeparticlemeshemitter.md#class_VisualShaderNodeParticleMeshEmitter), [VisualShaderNodeParticleRingEmitter](class_visualshadernodeparticleringemitter.md#class_VisualShaderNodeParticleRingEmitter), [VisualShaderNodeParticleSphereEmitter](class_visualshadernodeparticlesphereemitter.md#class_VisualShaderNodeParticleSphereEmitter)

A base class for particle emitters.

### Description

Particle emitter nodes can be used in "start" step of particle shaders and they define the starting position of the particles. Connect them to the Position output port.

### Properties


| [bool](class_bool.md#class_bool) | [mode_2d](class_visualshadernodeparticleemitter.md#class_VisualShaderNodeParticleEmitter_property_mode_2d) | `false` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_VisualShaderNodeParticleEmitter_property_mode_2d"></span>

[bool](class_bool.md#class_bool) **mode_2d** = `false` [🔗](class_visualshadernodeparticleemitter.md#class_VisualShaderNodeParticleEmitter_property_mode_2d)

- void **set_mode_2d** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_mode_2d** ( )

If `true`, the result of this emitter is projected to 2D space. By default it is `false` and meant for use in 3D space.
