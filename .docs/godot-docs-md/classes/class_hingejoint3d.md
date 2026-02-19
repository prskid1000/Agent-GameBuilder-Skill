<span id="class_HingeJoint3D"></span>

## HingeJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class_Joint3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body.

### Description

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body. For example, Body A can be a [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) representing a door hinge that a [RigidBody3D](class_rigidbody3d.md#class_RigidBody3D) rotates around.

### Properties


| [float](class_float.md#class_float) | angular_limit/bias | `0.3` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | angular_limit/enable | `false` |
| [float](class_float.md#class_float) | angular_limit/lower | `-1.5707964` |
| [float](class_float.md#class_float) | angular_limit/relaxation | `1.0` |
| [float](class_float.md#class_float) | angular_limit/softness | `0.9` |
| [float](class_float.md#class_float) | angular_limit/upper | `1.5707964` |
| [bool](class_bool.md#class_bool) | motor/enable | `false` |
| [float](class_float.md#class_float) | motor/max_impulse | `1.0` |
| [float](class_float.md#class_float) | motor/target_velocity | `1.0` |
| [float](class_float.md#class_float) | params/bias | `0.3` |

### Methods


| [bool](class_bool.md#class_bool) | [get_flag](class_hingejoint3d.md#class_HingeJoint3D_method_get_flag) ( flag: [Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag) ) const |
| --- | --- |
| [float](class_float.md#class_float) | [get_param](class_hingejoint3d.md#class_HingeJoint3D_method_get_param) ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) const |
| void | [set_flag](class_hingejoint3d.md#class_HingeJoint3D_method_set_flag) ( flag: [Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag), enabled: [bool](class_bool.md#class_bool) ) |
| void | [set_param](class_hingejoint3d.md#class_HingeJoint3D_method_set_param) ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_HingeJoint3D_Param"></span>

enum **Param**: [🔗](class_hingejoint3d.md#enum_HingeJoint3D_Param)

<span id="class_HingeJoint3D_constant_PARAM_BIAS"></span>

[Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) **PARAM_BIAS** = `0`

The speed with which the two bodies get pulled together when they move in different directions.

<span id="class_HingeJoint3D_constant_PARAM_LIMIT_UPPER"></span>

[Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) **PARAM_LIMIT_UPPER** = `1`

The maximum rotation. Only active if angular_limit/enable is `true`.

<span id="class_HingeJoint3D_constant_PARAM_LIMIT_LOWER"></span>

[Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) **PARAM_LIMIT_LOWER** = `2`

The minimum rotation. Only active if angular_limit/enable is `true`.

<span id="class_HingeJoint3D_constant_PARAM_LIMIT_BIAS"></span>

[Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) **PARAM_LIMIT_BIAS** = `3`

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.

<span id="class_HingeJoint3D_constant_PARAM_LIMIT_SOFTNESS"></span>

[Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) **PARAM_LIMIT_SOFTNESS** = `4`

**Deprecated:** This property is never used by the engine and is kept for compatibility purpose.

<span id="class_HingeJoint3D_constant_PARAM_LIMIT_RELAXATION"></span>

[Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) **PARAM_LIMIT_RELAXATION** = `5`

The lower this value, the more the rotation gets slowed down.

<span id="class_HingeJoint3D_constant_PARAM_MOTOR_TARGET_VELOCITY"></span>

[Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) **PARAM_MOTOR_TARGET_VELOCITY** = `6`

Target speed for the motor.

<span id="class_HingeJoint3D_constant_PARAM_MOTOR_MAX_IMPULSE"></span>

[Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) **PARAM_MOTOR_MAX_IMPULSE** = `7`

Maximum acceleration for the motor.

<span id="class_HingeJoint3D_constant_PARAM_MAX"></span>

[Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) **PARAM_MAX** = `8`

Represents the size of the [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) enum.

---

<span id="enum_HingeJoint3D_Flag"></span>

enum **Flag**: [🔗](class_hingejoint3d.md#enum_HingeJoint3D_Flag)

<span id="class_HingeJoint3D_constant_FLAG_USE_LIMIT"></span>

[Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag) **FLAG_USE_LIMIT** = `0`

If `true`, the hinges maximum and minimum rotation, defined by angular_limit/lower and angular_limit/upper has effects.

<span id="class_HingeJoint3D_constant_FLAG_ENABLE_MOTOR"></span>

[Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag) **FLAG_ENABLE_MOTOR** = `1`

When activated, a motor turns the hinge.

<span id="class_HingeJoint3D_constant_FLAG_MAX"></span>

[Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag) **FLAG_MAX** = `2`

Represents the size of the [Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag) enum.

---

### Property Descriptions

.. _class_HingeJoint3D_property_angular_limit/bias:

[float](class_float.md#class_float) **angular_limit/bias** = `0.3` 🔗

- void **set_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) *const*

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.

---

.. _class_HingeJoint3D_property_angular_limit/enable:

[bool](class_bool.md#class_bool) **angular_limit/enable** = `false` 🔗

- void **set_flag** ( flag: [Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag) ) *const*

If `true`, the hinges maximum and minimum rotation, defined by angular_limit/lower and angular_limit/upper has effects.

---

.. _class_HingeJoint3D_property_angular_limit/lower:

[float](class_float.md#class_float) **angular_limit/lower** = `-1.5707964` 🔗

- void **set_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) *const*

The minimum rotation. Only active if angular_limit/enable is `true`.

---

.. _class_HingeJoint3D_property_angular_limit/relaxation:

[float](class_float.md#class_float) **angular_limit/relaxation** = `1.0` 🔗

- void **set_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) *const*

The lower this value, the more the rotation gets slowed down.

---

.. _class_HingeJoint3D_property_angular_limit/softness:

[float](class_float.md#class_float) **angular_limit/softness** = `0.9` 🔗

- void **set_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) *const*

**Deprecated:** This property is never set by the engine and is kept for compatibility purposes.

---

.. _class_HingeJoint3D_property_angular_limit/upper:

[float](class_float.md#class_float) **angular_limit/upper** = `1.5707964` 🔗

- void **set_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) *const*

The maximum rotation. Only active if angular_limit/enable is `true`.

---

.. _class_HingeJoint3D_property_motor/enable:

[bool](class_bool.md#class_bool) **motor/enable** = `false` 🔗

- void **set_flag** ( flag: [Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag), enabled: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag** ( flag: [Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag) ) *const*

When activated, a motor turns the hinge.

---

.. _class_HingeJoint3D_property_motor/max_impulse:

[float](class_float.md#class_float) **motor/max_impulse** = `1.0` 🔗

- void **set_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) *const*

Maximum acceleration for the motor.

---

.. _class_HingeJoint3D_property_motor/target_velocity:

[float](class_float.md#class_float) **motor/target_velocity** = `1.0` 🔗

- void **set_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) *const*

Target speed for the motor.

---

.. _class_HingeJoint3D_property_params/bias:

[float](class_float.md#class_float) **params/bias** = `0.3` 🔗

- void **set_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) *const*

The speed with which the two bodies get pulled together when they move in different directions.

---

### Method Descriptions

<span id="class_HingeJoint3D_method_get_flag"></span>

[bool](class_bool.md#class_bool) **get_flag** ( flag: [Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag) ) *const* [🔗](class_hingejoint3d.md#class_HingeJoint3D_method_get_flag)

Returns the value of the specified flag.

---

<span id="class_HingeJoint3D_method_get_param"></span>

[float](class_float.md#class_float) **get_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param) ) *const* [🔗](class_hingejoint3d.md#class_HingeJoint3D_method_get_param)

Returns the value of the specified parameter.

---

<span id="class_HingeJoint3D_method_set_flag"></span>

void **set_flag** ( flag: [Flag](class_hingejoint3d.md#enum_HingeJoint3D_Flag), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_hingejoint3d.md#class_HingeJoint3D_method_set_flag)

If `true`, enables the specified flag.

---

<span id="class_HingeJoint3D_method_set_param"></span>

void **set_param** ( param: [Param](class_hingejoint3d.md#enum_HingeJoint3D_Param), value: [float](class_float.md#class_float) ) [🔗](class_hingejoint3d.md#class_HingeJoint3D_method_set_param)

Sets the value of the specified parameter.
