<span id="class_VisualShaderNodeParticleAccelerator"></span>

## VisualShaderNodeParticleAccelerator

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A visual shader node that accelerates particles.

### Description

Particle accelerator can be used in "process" step of particle shader. It will accelerate the particles. Connect it to the Velocity output port.

### Properties


| [Mode](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode) | [mode](class_visualshadernodeparticleaccelerator.md#class_VisualShaderNodeParticleAccelerator_property_mode) | `0` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_VisualShaderNodeParticleAccelerator_Mode"></span>

enum **Mode**: [🔗](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode)

<span id="class_VisualShaderNodeParticleAccelerator_constant_MODE_LINEAR"></span>

[Mode](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode) **MODE_LINEAR** = `0`

The particles will be accelerated based on their velocity.

<span id="class_VisualShaderNodeParticleAccelerator_constant_MODE_RADIAL"></span>

[Mode](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode) **MODE_RADIAL** = `1`

The particles will be accelerated towards or away from the center.

<span id="class_VisualShaderNodeParticleAccelerator_constant_MODE_TANGENTIAL"></span>

[Mode](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode) **MODE_TANGENTIAL** = `2`

The particles will be accelerated tangentially to the radius vector from center to their position.

<span id="class_VisualShaderNodeParticleAccelerator_constant_MODE_MAX"></span>

[Mode](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode) **MODE_MAX** = `3`

Represents the size of the [Mode](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode) enum.

---

### Property Descriptions

<span id="class_VisualShaderNodeParticleAccelerator_property_mode"></span>

[Mode](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode) **mode** = `0` [🔗](class_visualshadernodeparticleaccelerator.md#class_VisualShaderNodeParticleAccelerator_property_mode)

- void **set_mode** ( value: [Mode](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode) )
- [Mode](class_visualshadernodeparticleaccelerator.md#enum_VisualShaderNodeParticleAccelerator_Mode) **get_mode** ( )

Defines in what manner the particles will be accelerated.
