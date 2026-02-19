<span id="class_VisualShaderNodeParticleMeshEmitter"></span>

## VisualShaderNodeParticleMeshEmitter

**Inherits:** [VisualShaderNodeParticleEmitter](class_visualshadernodeparticleemitter.md#class_VisualShaderNodeParticleEmitter) **<** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A visual shader node that makes particles emitted in a shape defined by a [Mesh](class_mesh.md#class_Mesh).

### Description

[VisualShaderNodeParticleEmitter](class_visualshadernodeparticleemitter.md#class_VisualShaderNodeParticleEmitter) that makes the particles emitted in a shape of the assigned [mesh](class_visualshadernodeparticlemeshemitter.md#class_VisualShaderNodeParticleMeshEmitter_property_mesh). It will emit from the mesh's surfaces, either all or only the specified one.

### Properties


| [Mesh](class_mesh.md#class_Mesh) | [mesh](class_visualshadernodeparticlemeshemitter.md#class_VisualShaderNodeParticleMeshEmitter_property_mesh) |
| --- | --- |
| [int](class_int.md#class_int) | [surface_index](class_visualshadernodeparticlemeshemitter.md#class_VisualShaderNodeParticleMeshEmitter_property_surface_index) | `0` |
| [bool](class_bool.md#class_bool) | [use_all_surfaces](class_visualshadernodeparticlemeshemitter.md#class_VisualShaderNodeParticleMeshEmitter_property_use_all_surfaces) | `true` |

---

### Property Descriptions

<span id="class_VisualShaderNodeParticleMeshEmitter_property_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **mesh** [🔗](class_visualshadernodeparticlemeshemitter.md#class_VisualShaderNodeParticleMeshEmitter_property_mesh)

- void **set_mesh** ( value: [Mesh](class_mesh.md#class_Mesh) )
- [Mesh](class_mesh.md#class_Mesh) **get_mesh** ( )

The [Mesh](class_mesh.md#class_Mesh) that defines emission shape.

---

<span id="class_VisualShaderNodeParticleMeshEmitter_property_surface_index"></span>

[int](class_int.md#class_int) **surface_index** = `0` [🔗](class_visualshadernodeparticlemeshemitter.md#class_VisualShaderNodeParticleMeshEmitter_property_surface_index)

- void **set_surface_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_surface_index** ( )

Index of the surface that emits particles. [use_all_surfaces](class_visualshadernodeparticlemeshemitter.md#class_VisualShaderNodeParticleMeshEmitter_property_use_all_surfaces) must be `false` for this to take effect.

---

<span id="class_VisualShaderNodeParticleMeshEmitter_property_use_all_surfaces"></span>

[bool](class_bool.md#class_bool) **use_all_surfaces** = `true` [🔗](class_visualshadernodeparticlemeshemitter.md#class_VisualShaderNodeParticleMeshEmitter_property_use_all_surfaces)

- void **set_use_all_surfaces** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_use_all_surfaces** ( )

If `true`, the particles will emit from all surfaces of the mesh.
