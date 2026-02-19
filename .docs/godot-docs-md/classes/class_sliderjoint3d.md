<span id="class_SliderJoint3D"></span>

## SliderJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class_Joint3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A physics joint that restricts the movement of a 3D physics body along an axis relative to another physics body.

### Description

A physics joint that restricts the movement of a 3D physics body along an axis relative to another physics body. For example, Body A could be a [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) representing a piston base, while Body B could be a [RigidBody3D](class_rigidbody3d.md#class_RigidBody3D) representing the piston head, moving up and down.

### Properties


| [float](class_float.md#class_float) | angular_limit/damping | `0.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | angular_limit/lower_angle | `0.0` |
| [float](class_float.md#class_float) | angular_limit/restitution | `0.7` |
| [float](class_float.md#class_float) | angular_limit/softness | `1.0` |
| [float](class_float.md#class_float) | angular_limit/upper_angle | `0.0` |
| [float](class_float.md#class_float) | angular_motion/damping | `1.0` |
| [float](class_float.md#class_float) | angular_motion/restitution | `0.7` |
| [float](class_float.md#class_float) | angular_motion/softness | `1.0` |
| [float](class_float.md#class_float) | angular_ortho/damping | `1.0` |
| [float](class_float.md#class_float) | angular_ortho/restitution | `0.7` |
| [float](class_float.md#class_float) | angular_ortho/softness | `1.0` |
| [float](class_float.md#class_float) | linear_limit/damping | `1.0` |
| [float](class_float.md#class_float) | linear_limit/lower_distance | `-1.0` |
| [float](class_float.md#class_float) | linear_limit/restitution | `0.7` |
| [float](class_float.md#class_float) | linear_limit/softness | `1.0` |
| [float](class_float.md#class_float) | linear_limit/upper_distance | `1.0` |
| [float](class_float.md#class_float) | linear_motion/damping | `0.0` |
| [float](class_float.md#class_float) | linear_motion/restitution | `0.7` |
| [float](class_float.md#class_float) | linear_motion/softness | `1.0` |
| [float](class_float.md#class_float) | linear_ortho/damping | `1.0` |
| [float](class_float.md#class_float) | linear_ortho/restitution | `0.7` |
| [float](class_float.md#class_float) | linear_ortho/softness | `1.0` |

### Methods


| [float](class_float.md#class_float) | [get_param](class_sliderjoint3d.md#class_SliderJoint3D_method_get_param) ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) const |
| --- | --- |
| void | [set_param](class_sliderjoint3d.md#class_SliderJoint3D_method_set_param) ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_SliderJoint3D_Param"></span>

enum **Param**: [🔗](class_sliderjoint3d.md#enum_SliderJoint3D_Param)

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_UPPER"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_LIMIT_UPPER** = `0`

Constant for accessing linear_limit/upper_distance. The maximum difference between the pivot points on their X axis before damping happens.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_LOWER"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_LIMIT_LOWER** = `1`

Constant for accessing linear_limit/lower_distance. The minimum difference between the pivot points on their X axis before damping happens.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_SOFTNESS"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_LIMIT_SOFTNESS** = `2`

Constant for accessing linear_limit/softness. A factor applied to the movement across the slider axis once the limits get surpassed. The lower, the slower the movement.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_RESTITUTION"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_LIMIT_RESTITUTION** = `3`

Constant for accessing linear_limit/restitution. The amount of restitution once the limits are surpassed. The lower, the more velocity-energy gets lost.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_DAMPING"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_LIMIT_DAMPING** = `4`

Constant for accessing linear_limit/damping. The amount of damping once the slider limits are surpassed.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_MOTION_SOFTNESS"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_MOTION_SOFTNESS** = `5`

Constant for accessing linear_motion/softness. A factor applied to the movement across the slider axis as long as the slider is in the limits. The lower, the slower the movement.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_MOTION_RESTITUTION"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_MOTION_RESTITUTION** = `6`

Constant for accessing linear_motion/restitution. The amount of restitution inside the slider limits.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_MOTION_DAMPING"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_MOTION_DAMPING** = `7`

Constant for accessing linear_motion/damping. The amount of damping inside the slider limits.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_ORTHOGONAL_SOFTNESS"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_ORTHOGONAL_SOFTNESS** = `8`

Constant for accessing linear_ortho/softness. A factor applied to the movement across axes orthogonal to the slider.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_ORTHOGONAL_RESTITUTION"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_ORTHOGONAL_RESTITUTION** = `9`

Constant for accessing linear_motion/restitution. The amount of restitution when movement is across axes orthogonal to the slider.

<span id="class_SliderJoint3D_constant_PARAM_LINEAR_ORTHOGONAL_DAMPING"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_LINEAR_ORTHOGONAL_DAMPING** = `10`

Constant for accessing linear_motion/damping. The amount of damping when movement is across axes orthogonal to the slider.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_UPPER"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_LIMIT_UPPER** = `11`

Constant for accessing angular_limit/upper_angle. The upper limit of rotation in the slider.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_LOWER"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_LIMIT_LOWER** = `12`

Constant for accessing angular_limit/lower_angle. The lower limit of rotation in the slider.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_SOFTNESS"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_LIMIT_SOFTNESS** = `13`

Constant for accessing angular_limit/softness. A factor applied to the all rotation once the limit is surpassed.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_RESTITUTION"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_LIMIT_RESTITUTION** = `14`

Constant for accessing angular_limit/restitution. The amount of restitution of the rotation when the limit is surpassed.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_DAMPING"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_LIMIT_DAMPING** = `15`

Constant for accessing angular_limit/damping. The amount of damping of the rotation when the limit is surpassed.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_MOTION_SOFTNESS"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_MOTION_SOFTNESS** = `16`

Constant for accessing angular_motion/softness. A factor applied to the all rotation in the limits.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_MOTION_RESTITUTION"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_MOTION_RESTITUTION** = `17`

Constant for accessing angular_motion/restitution. The amount of restitution of the rotation in the limits.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_MOTION_DAMPING"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_MOTION_DAMPING** = `18`

Constant for accessing angular_motion/damping. The amount of damping of the rotation in the limits.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_ORTHOGONAL_SOFTNESS"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_ORTHOGONAL_SOFTNESS** = `19`

Constant for accessing angular_ortho/softness. A factor applied to the all rotation across axes orthogonal to the slider.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_ORTHOGONAL_RESTITUTION"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_ORTHOGONAL_RESTITUTION** = `20`

Constant for accessing angular_ortho/restitution. The amount of restitution of the rotation across axes orthogonal to the slider.

<span id="class_SliderJoint3D_constant_PARAM_ANGULAR_ORTHOGONAL_DAMPING"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_ANGULAR_ORTHOGONAL_DAMPING** = `21`

Constant for accessing angular_ortho/damping. The amount of damping of the rotation across axes orthogonal to the slider.

<span id="class_SliderJoint3D_constant_PARAM_MAX"></span>

[Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) **PARAM_MAX** = `22`

Represents the size of the [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) enum.

---

### Property Descriptions

.. _class_SliderJoint3D_property_angular_limit/damping:

[float](class_float.md#class_float) **angular_limit/damping** = `0.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of damping of the rotation when the limit is surpassed.

A lower damping value allows a rotation initiated by body A to travel to body B slower.

---

.. _class_SliderJoint3D_property_angular_limit/lower_angle:

[float](class_float.md#class_float) **angular_limit/lower_angle** = `0.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The lower limit of rotation in the slider.

---

.. _class_SliderJoint3D_property_angular_limit/restitution:

[float](class_float.md#class_float) **angular_limit/restitution** = `0.7` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of restitution of the rotation when the limit is surpassed.

Does not affect damping.

---

.. _class_SliderJoint3D_property_angular_limit/softness:

[float](class_float.md#class_float) **angular_limit/softness** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

A factor applied to the all rotation once the limit is surpassed.

Makes all rotation slower when between 0 and 1.

---

.. _class_SliderJoint3D_property_angular_limit/upper_angle:

[float](class_float.md#class_float) **angular_limit/upper_angle** = `0.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The upper limit of rotation in the slider.

---

.. _class_SliderJoint3D_property_angular_motion/damping:

[float](class_float.md#class_float) **angular_motion/damping** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of damping of the rotation in the limits.

---

.. _class_SliderJoint3D_property_angular_motion/restitution:

[float](class_float.md#class_float) **angular_motion/restitution** = `0.7` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of restitution of the rotation in the limits.

---

.. _class_SliderJoint3D_property_angular_motion/softness:

[float](class_float.md#class_float) **angular_motion/softness** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

A factor applied to the all rotation in the limits.

---

.. _class_SliderJoint3D_property_angular_ortho/damping:

[float](class_float.md#class_float) **angular_ortho/damping** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of damping of the rotation across axes orthogonal to the slider.

---

.. _class_SliderJoint3D_property_angular_ortho/restitution:

[float](class_float.md#class_float) **angular_ortho/restitution** = `0.7` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of restitution of the rotation across axes orthogonal to the slider.

---

.. _class_SliderJoint3D_property_angular_ortho/softness:

[float](class_float.md#class_float) **angular_ortho/softness** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

A factor applied to the all rotation across axes orthogonal to the slider.

---

.. _class_SliderJoint3D_property_linear_limit/damping:

[float](class_float.md#class_float) **linear_limit/damping** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of damping that happens once the limit defined by linear_limit/lower_distance and linear_limit/upper_distance is surpassed.

---

.. _class_SliderJoint3D_property_linear_limit/lower_distance:

[float](class_float.md#class_float) **linear_limit/lower_distance** = `-1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The minimum difference between the pivot points on their X axis before damping happens.

---

.. _class_SliderJoint3D_property_linear_limit/restitution:

[float](class_float.md#class_float) **linear_limit/restitution** = `0.7` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of restitution once the limits are surpassed. The lower, the more velocity-energy gets lost.

---

.. _class_SliderJoint3D_property_linear_limit/softness:

[float](class_float.md#class_float) **linear_limit/softness** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

A factor applied to the movement across the slider axis once the limits get surpassed. The lower, the slower the movement.

---

.. _class_SliderJoint3D_property_linear_limit/upper_distance:

[float](class_float.md#class_float) **linear_limit/upper_distance** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The maximum difference between the pivot points on their X axis before damping happens.

---

.. _class_SliderJoint3D_property_linear_motion/damping:

[float](class_float.md#class_float) **linear_motion/damping** = `0.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of damping inside the slider limits.

---

.. _class_SliderJoint3D_property_linear_motion/restitution:

[float](class_float.md#class_float) **linear_motion/restitution** = `0.7` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of restitution inside the slider limits.

---

.. _class_SliderJoint3D_property_linear_motion/softness:

[float](class_float.md#class_float) **linear_motion/softness** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

A factor applied to the movement across the slider axis as long as the slider is in the limits. The lower, the slower the movement.

---

.. _class_SliderJoint3D_property_linear_ortho/damping:

[float](class_float.md#class_float) **linear_ortho/damping** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of damping when movement is across axes orthogonal to the slider.

---

.. _class_SliderJoint3D_property_linear_ortho/restitution:

[float](class_float.md#class_float) **linear_ortho/restitution** = `0.7` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

The amount of restitution when movement is across axes orthogonal to the slider.

---

.. _class_SliderJoint3D_property_linear_ortho/softness:

[float](class_float.md#class_float) **linear_ortho/softness** = `1.0` 🔗

- void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const*

A factor applied to the movement across axes orthogonal to the slider.

---

### Method Descriptions

<span id="class_SliderJoint3D_method_get_param"></span>

[float](class_float.md#class_float) **get_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param) ) *const* [🔗](class_sliderjoint3d.md#class_SliderJoint3D_method_get_param)

Returns the value of the given parameter.

---

<span id="class_SliderJoint3D_method_set_param"></span>

void **set_param** ( param: [Param](class_sliderjoint3d.md#enum_SliderJoint3D_Param), value: [float](class_float.md#class_float) ) [🔗](class_sliderjoint3d.md#class_SliderJoint3D_method_set_param)

Assigns `value` to the given parameter.
