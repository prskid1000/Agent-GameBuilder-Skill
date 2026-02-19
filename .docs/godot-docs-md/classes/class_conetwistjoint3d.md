<span id="class_ConeTwistJoint3D"></span>

## ConeTwistJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class_Joint3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint.

### Description

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint. The twist axis is initiated as the X axis of the **ConeTwistJoint3D**. Once the physics bodies swing, the twist axis is calculated as the middle of the X axes of the joint in the local space of the two physics bodies. Useful for limbs like shoulders and hips, lamps hanging off a ceiling, etc.

### Properties


| [float](class_float.md#class_float) | [bias](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_bias) | `0.3` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [relaxation](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_relaxation) | `1.0` |
| [float](class_float.md#class_float) | [softness](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_softness) | `0.8` |
| [float](class_float.md#class_float) | [swing_span](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_swing_span) | `0.7853982` |
| [float](class_float.md#class_float) | [twist_span](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_twist_span) | `3.1415927` |

### Methods


| [float](class_float.md#class_float) | [get_param](class_conetwistjoint3d.md#class_ConeTwistJoint3D_method_get_param) ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) ) const |
| --- | --- |
| void | [set_param](class_conetwistjoint3d.md#class_ConeTwistJoint3D_method_set_param) ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param), value: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_ConeTwistJoint3D_Param"></span>

enum **Param**: [🔗](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param)

<span id="class_ConeTwistJoint3D_constant_PARAM_SWING_SPAN"></span>

[Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) **PARAM_SWING_SPAN** = `0`

Swing is rotation from side to side, around the axis perpendicular to the twist axis.

The swing span defines, how much rotation will not get corrected along the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.

<span id="class_ConeTwistJoint3D_constant_PARAM_TWIST_SPAN"></span>

[Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) **PARAM_TWIST_SPAN** = `1`

Twist is the rotation around the twist axis, this value defined how far the joint can twist.

Twist is locked if below 0.05.

<span id="class_ConeTwistJoint3D_constant_PARAM_BIAS"></span>

[Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) **PARAM_BIAS** = `2`

The speed with which the swing or twist will take place.

The higher, the faster.

<span id="class_ConeTwistJoint3D_constant_PARAM_SOFTNESS"></span>

[Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) **PARAM_SOFTNESS** = `3`

The ease with which the joint starts to twist. If it's too low, it takes more force to start twisting the joint.

<span id="class_ConeTwistJoint3D_constant_PARAM_RELAXATION"></span>

[Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) **PARAM_RELAXATION** = `4`

Defines, how fast the swing- and twist-speed-difference on both sides gets synced.

<span id="class_ConeTwistJoint3D_constant_PARAM_MAX"></span>

[Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) **PARAM_MAX** = `5`

Represents the size of the [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) enum.

---

### Property Descriptions

<span id="class_ConeTwistJoint3D_property_bias"></span>

[float](class_float.md#class_float) **bias** = `0.3` [🔗](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_bias)

- void **set_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) ) *const*

The speed with which the swing or twist will take place.

The higher, the faster.

---

<span id="class_ConeTwistJoint3D_property_relaxation"></span>

[float](class_float.md#class_float) **relaxation** = `1.0` [🔗](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_relaxation)

- void **set_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) ) *const*

Defines, how fast the swing- and twist-speed-difference on both sides gets synced.

---

<span id="class_ConeTwistJoint3D_property_softness"></span>

[float](class_float.md#class_float) **softness** = `0.8` [🔗](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_softness)

- void **set_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) ) *const*

The ease with which the joint starts to twist. If it's too low, it takes more force to start twisting the joint.

---

<span id="class_ConeTwistJoint3D_property_swing_span"></span>

[float](class_float.md#class_float) **swing_span** = `0.7853982` [🔗](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_swing_span)

- void **set_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) ) *const*

Swing is rotation from side to side, around the axis perpendicular to the twist axis.

The swing span defines, how much rotation will not get corrected along the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.

---

<span id="class_ConeTwistJoint3D_property_twist_span"></span>

[float](class_float.md#class_float) **twist_span** = `3.1415927` [🔗](class_conetwistjoint3d.md#class_ConeTwistJoint3D_property_twist_span)

- void **set_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) ) *const*

Twist is the rotation around the twist axis, this value defined how far the joint can twist.

Twist is locked if below 0.05.

---

### Method Descriptions

<span id="class_ConeTwistJoint3D_method_get_param"></span>

[float](class_float.md#class_float) **get_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param) ) *const* [🔗](class_conetwistjoint3d.md#class_ConeTwistJoint3D_method_get_param)

Returns the value of the specified parameter.

---

<span id="class_ConeTwistJoint3D_method_set_param"></span>

void **set_param** ( param: [Param](class_conetwistjoint3d.md#enum_ConeTwistJoint3D_Param), value: [float](class_float.md#class_float) ) [🔗](class_conetwistjoint3d.md#class_ConeTwistJoint3D_method_set_param)

Sets the value of the specified parameter.
