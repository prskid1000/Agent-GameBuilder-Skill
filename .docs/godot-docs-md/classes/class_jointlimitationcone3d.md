<span id="class_JointLimitationCone3D"></span>

## JointLimitationCone3D

**Inherits:** [JointLimitation3D](class_jointlimitation3d.md#class_JointLimitation3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A cone shape limitation that interacts with [ChainIK3D](class_chainik3d.md#class_ChainIK3D).

### Description

A cone shape limitation that interacts with [ChainIK3D](class_chainik3d.md#class_ChainIK3D).

### Properties


| [float](class_float.md#class_float) | [angle](class_jointlimitationcone3d.md#class_JointLimitationCone3D_property_angle) | `1.5707964` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_JointLimitationCone3D_property_angle"></span>

[float](class_float.md#class_float) **angle** = `1.5707964` [🔗](class_jointlimitationcone3d.md#class_JointLimitationCone3D_property_angle)

- void **set_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_angle** ( )

The radius range of the hole made by the cone.

 `0` degrees makes a sphere without hole, `180` degrees makes a hemisphere, and `360` degrees become empty (no limitation).
