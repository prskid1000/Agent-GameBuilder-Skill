<span id="class_VisualShaderNodeParticleEmit"></span>

## VisualShaderNodeParticleEmit

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A visual shader node that forces to emit a particle from a sub-emitter.

### Description

This node internally calls `emit_subparticle` shader method. It will emit a particle from the configured sub-emitter and also allows to customize how its emitted. Requires a sub-emitter assigned to the particles node with this shader.

### Properties


| [EmitFlags](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags) | [flags](class_visualshadernodeparticleemit.md#class_VisualShaderNodeParticleEmit_property_flags) | `31` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeParticleEmit_EmitFlags"></span>

enum **EmitFlags**: [🔗](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags)

<span id="class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_POSITION"></span>

[EmitFlags](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags) **EMIT_FLAG_POSITION** = `1`

If enabled, the particle starts with the position defined by this node.

<span id="class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_ROT_SCALE"></span>

[EmitFlags](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags) **EMIT_FLAG_ROT_SCALE** = `2`

If enabled, the particle starts with the rotation and scale defined by this node.

<span id="class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_VELOCITY"></span>

[EmitFlags](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags) **EMIT_FLAG_VELOCITY** = `4`

If enabled,the particle starts with the velocity defined by this node.

<span id="class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_COLOR"></span>

[EmitFlags](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags) **EMIT_FLAG_COLOR** = `8`

If enabled, the particle starts with the color defined by this node.

<span id="class_VisualShaderNodeParticleEmit_constant_EMIT_FLAG_CUSTOM"></span>

[EmitFlags](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags) **EMIT_FLAG_CUSTOM** = `16`

If enabled, the particle starts with the `CUSTOM` data defined by this node.

---

### Property Descriptions

<span id="class_VisualShaderNodeParticleEmit_property_flags"></span>

[EmitFlags](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags) **flags** = `31` [🔗](class_visualshadernodeparticleemit.md#class_VisualShaderNodeParticleEmit_property_flags)

- void **set_flags** ( value: [EmitFlags](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags) )
- [EmitFlags](class_visualshadernodeparticleemit.md#enum_VisualShaderNodeParticleEmit_EmitFlags) **get_flags** ( )

Flags used to override the properties defined in the sub-emitter's process material.
