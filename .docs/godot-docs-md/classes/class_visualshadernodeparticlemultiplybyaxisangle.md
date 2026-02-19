<span id="class_VisualShaderNodeParticleMultiplyByAxisAngle"></span>

## VisualShaderNodeParticleMultiplyByAxisAngle

**Inherits:** [VisualShaderNode](class_visualshadernode.md#class_VisualShaderNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A visual shader helper node for multiplying position and rotation of particles.

### Description

This node helps to multiply a position input vector by rotation using specific axis. Intended to work with emitters.

### Properties


| [bool](class_bool.md#class_bool) | [degrees_mode](class_visualshadernodeparticlemultiplybyaxisangle.md#class_VisualShaderNodeParticleMultiplyByAxisAngle_property_degrees_mode) | `true` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_VisualShaderNodeParticleMultiplyByAxisAngle_property_degrees_mode"></span>

[bool](class_bool.md#class_bool) **degrees_mode** = `true` [🔗](class_visualshadernodeparticlemultiplybyaxisangle.md#class_VisualShaderNodeParticleMultiplyByAxisAngle_property_degrees_mode)

- void **set_degrees_mode** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_degrees_mode** ( )

If `true`, the angle will be interpreted in degrees instead of radians.
