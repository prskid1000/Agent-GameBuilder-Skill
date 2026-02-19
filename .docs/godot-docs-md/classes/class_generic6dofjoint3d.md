<span id="class_Generic6DOFJoint3D"></span>

## Generic6DOFJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class_Joint3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A physics joint that allows for complex movement and rotation between two 3D physics bodies.

### Description

The **Generic6DOFJoint3D** (6 Degrees Of Freedom) joint allows for implementing custom types of joints by locking the rotation and translation of certain axes.

The first 3 DOF represent the linear motion of the physics bodies and the last 3 DOF represent the angular motion of the physics bodies. Each axis can be either locked, or limited.

### Properties


| [float](class_float.md#class_float) | angular_limit_x/damping | `1.0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | angular_limit_x/enabled | `true` |
| [float](class_float.md#class_float) | angular_limit_x/erp | `0.5` |
| [float](class_float.md#class_float) | angular_limit_x/force_limit | `0.0` |
| [float](class_float.md#class_float) | angular_limit_x/lower_angle | `0.0` |
| [float](class_float.md#class_float) | angular_limit_x/restitution | `0.0` |
| [float](class_float.md#class_float) | angular_limit_x/softness | `0.5` |
| [float](class_float.md#class_float) | angular_limit_x/upper_angle | `0.0` |
| [float](class_float.md#class_float) | angular_limit_y/damping | `1.0` |
| [bool](class_bool.md#class_bool) | angular_limit_y/enabled | `true` |
| [float](class_float.md#class_float) | angular_limit_y/erp | `0.5` |
| [float](class_float.md#class_float) | angular_limit_y/force_limit | `0.0` |
| [float](class_float.md#class_float) | angular_limit_y/lower_angle | `0.0` |
| [float](class_float.md#class_float) | angular_limit_y/restitution | `0.0` |
| [float](class_float.md#class_float) | angular_limit_y/softness | `0.5` |
| [float](class_float.md#class_float) | angular_limit_y/upper_angle | `0.0` |
| [float](class_float.md#class_float) | angular_limit_z/damping | `1.0` |
| [bool](class_bool.md#class_bool) | angular_limit_z/enabled | `true` |
| [float](class_float.md#class_float) | angular_limit_z/erp | `0.5` |
| [float](class_float.md#class_float) | angular_limit_z/force_limit | `0.0` |
| [float](class_float.md#class_float) | angular_limit_z/lower_angle | `0.0` |
| [float](class_float.md#class_float) | angular_limit_z/restitution | `0.0` |
| [float](class_float.md#class_float) | angular_limit_z/softness | `0.5` |
| [float](class_float.md#class_float) | angular_limit_z/upper_angle | `0.0` |
| [bool](class_bool.md#class_bool) | angular_motor_x/enabled | `false` |
| [float](class_float.md#class_float) | angular_motor_x/force_limit | `300.0` |
| [float](class_float.md#class_float) | angular_motor_x/target_velocity | `0.0` |
| [bool](class_bool.md#class_bool) | angular_motor_y/enabled | `false` |
| [float](class_float.md#class_float) | angular_motor_y/force_limit | `300.0` |
| [float](class_float.md#class_float) | angular_motor_y/target_velocity | `0.0` |
| [bool](class_bool.md#class_bool) | angular_motor_z/enabled | `false` |
| [float](class_float.md#class_float) | angular_motor_z/force_limit | `300.0` |
| [float](class_float.md#class_float) | angular_motor_z/target_velocity | `0.0` |
| [float](class_float.md#class_float) | angular_spring_x/damping | `0.0` |
| [bool](class_bool.md#class_bool) | angular_spring_x/enabled | `false` |
| [float](class_float.md#class_float) | angular_spring_x/equilibrium_point | `0.0` |
| [float](class_float.md#class_float) | angular_spring_x/stiffness | `0.0` |
| [float](class_float.md#class_float) | angular_spring_y/damping | `0.0` |
| [bool](class_bool.md#class_bool) | angular_spring_y/enabled | `false` |
| [float](class_float.md#class_float) | angular_spring_y/equilibrium_point | `0.0` |
| [float](class_float.md#class_float) | angular_spring_y/stiffness | `0.0` |
| [float](class_float.md#class_float) | angular_spring_z/damping | `0.0` |
| [bool](class_bool.md#class_bool) | angular_spring_z/enabled | `false` |
| [float](class_float.md#class_float) | angular_spring_z/equilibrium_point | `0.0` |
| [float](class_float.md#class_float) | angular_spring_z/stiffness | `0.0` |
| [float](class_float.md#class_float) | linear_limit_x/damping | `1.0` |
| [bool](class_bool.md#class_bool) | linear_limit_x/enabled | `true` |
| [float](class_float.md#class_float) | linear_limit_x/lower_distance | `0.0` |
| [float](class_float.md#class_float) | linear_limit_x/restitution | `0.5` |
| [float](class_float.md#class_float) | linear_limit_x/softness | `0.7` |
| [float](class_float.md#class_float) | linear_limit_x/upper_distance | `0.0` |
| [float](class_float.md#class_float) | linear_limit_y/damping | `1.0` |
| [bool](class_bool.md#class_bool) | linear_limit_y/enabled | `true` |
| [float](class_float.md#class_float) | linear_limit_y/lower_distance | `0.0` |
| [float](class_float.md#class_float) | linear_limit_y/restitution | `0.5` |
| [float](class_float.md#class_float) | linear_limit_y/softness | `0.7` |
| [float](class_float.md#class_float) | linear_limit_y/upper_distance | `0.0` |
| [float](class_float.md#class_float) | linear_limit_z/damping | `1.0` |
| [bool](class_bool.md#class_bool) | linear_limit_z/enabled | `true` |
| [float](class_float.md#class_float) | linear_limit_z/lower_distance | `0.0` |
| [float](class_float.md#class_float) | linear_limit_z/restitution | `0.5` |
| [float](class_float.md#class_float) | linear_limit_z/softness | `0.7` |
| [float](class_float.md#class_float) | linear_limit_z/upper_distance | `0.0` |
| [bool](class_bool.md#class_bool) | linear_motor_x/enabled | `false` |
| [float](class_float.md#class_float) | linear_motor_x/force_limit | `0.0` |
| [float](class_float.md#class_float) | linear_motor_x/target_velocity | `0.0` |
| [bool](class_bool.md#class_bool) | linear_motor_y/enabled | `false` |
| [float](class_float.md#class_float) | linear_motor_y/force_limit | `0.0` |
| [float](class_float.md#class_float) | linear_motor_y/target_velocity | `0.0` |
| [bool](class_bool.md#class_bool) | linear_motor_z/enabled | `false` |
| [float](class_float.md#class_float) | linear_motor_z/force_limit | `0.0` |
| [float](class_float.md#class_float) | linear_motor_z/target_velocity | `0.0` |
| [float](class_float.md#class_float) | linear_spring_x/damping | `0.01` |
| [bool](class_bool.md#class_bool) | linear_spring_x/enabled | `false` |
| [float](class_float.md#class_float) | linear_spring_x/equilibrium_point | `0.0` |
| [float](class_float.md#class_float) | linear_spring_x/stiffness | `0.01` |
| [float](class_float.md#class_float) | linear_spring_y/damping | `0.01` |
| [bool](class_bool.md#class_bool) | linear_spring_y/enabled | `false` |
| [float](class_float.md#class_float) | linear_spring_y/equilibrium_point | `0.0` |
| [float](class_float.md#class_float) | linear_spring_y/stiffness | `0.01` |
| [float](class_float.md#class_float) | linear_spring_z/damping | `0.01` |
| [bool](class_bool.md#class_bool) | linear_spring_z/enabled | `false` |
| [float](class_float.md#class_float) | linear_spring_z/equilibrium_point | `0.0` |
| [float](class_float.md#class_float) | linear_spring_z/stiffness | `0.01` |

### Methods


| [bool](class_bool.md#class_bool) | [get_flag_x](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_flag_x) ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [get_flag_y](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_flag_y) ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) const |
| [bool](class_bool.md#class_bool) | [get_flag_z](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_flag_z) ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) const |
| [float](class_float.md#class_float) | [get_param_x](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_param_x) ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) const |
| [float](class_float.md#class_float) | [get_param_y](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_param_y) ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) const |
| [float](class_float.md#class_float) | [get_param_z](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_param_z) ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) const |
| void | [set_flag_x](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_flag_x) ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) ) |
| void | [set_flag_y](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_flag_y) ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) ) |
| void | [set_flag_z](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_flag_z) ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) ) |
| void | [set_param_x](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_param_x) ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) ) |
| void | [set_param_y](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_param_y) ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) ) |
| void | [set_param_z](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_param_z) ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_Generic6DOFJoint3D_Param"></span>

enum **Param**: [🔗](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param)

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_LOWER_LIMIT"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_LOWER_LIMIT** = `0`

The minimum difference between the pivot points' axes.

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_UPPER_LIMIT"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_UPPER_LIMIT** = `1`

The maximum difference between the pivot points' axes.

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_LIMIT_SOFTNESS"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_LIMIT_SOFTNESS** = `2`

A factor applied to the movement across the axes. The lower, the slower the movement.

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_RESTITUTION"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_RESTITUTION** = `3`

The amount of restitution on the axes' movement. The lower, the more momentum gets lost.

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_DAMPING"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_DAMPING** = `4`

The amount of damping that happens at the linear motion across the axes.

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_MOTOR_TARGET_VELOCITY"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_MOTOR_TARGET_VELOCITY** = `5`

The velocity the linear motor will try to reach.

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_MOTOR_FORCE_LIMIT"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_MOTOR_FORCE_LIMIT** = `6`

The maximum force the linear motor will apply while trying to reach the velocity target.

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_SPRING_STIFFNESS"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_SPRING_STIFFNESS** = `7`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_SPRING_DAMPING"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_SPRING_DAMPING** = `8`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_Generic6DOFJoint3D_constant_PARAM_LINEAR_SPRING_EQUILIBRIUM_POINT"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_LINEAR_SPRING_EQUILIBRIUM_POINT** = `9`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_LOWER_LIMIT"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_LOWER_LIMIT** = `10`

The minimum rotation in negative direction to break loose and rotate around the axes.

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_UPPER_LIMIT"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_UPPER_LIMIT** = `11`

The minimum rotation in positive direction to break loose and rotate around the axes.

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_LIMIT_SOFTNESS"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_LIMIT_SOFTNESS** = `12`

The speed of all rotations across the axes.

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_DAMPING"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_DAMPING** = `13`

The amount of rotational damping across the axes. The lower, the more damping occurs.

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_RESTITUTION"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_RESTITUTION** = `14`

The amount of rotational restitution across the axes. The lower, the more restitution occurs.

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_FORCE_LIMIT"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_FORCE_LIMIT** = `15`

The maximum amount of force that can occur, when rotating around the axes.

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_ERP"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_ERP** = `16`

When rotating across the axes, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_MOTOR_TARGET_VELOCITY"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_MOTOR_TARGET_VELOCITY** = `17`

Target speed for the motor at the axes.

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_MOTOR_FORCE_LIMIT"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_MOTOR_FORCE_LIMIT** = `18`

Maximum acceleration for the motor at the axes.

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_SPRING_STIFFNESS"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_SPRING_STIFFNESS** = `19`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_SPRING_DAMPING"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_SPRING_DAMPING** = `20`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT** = `21`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_Generic6DOFJoint3D_constant_PARAM_MAX"></span>

[Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) **PARAM_MAX** = `22`

Represents the size of the [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) enum.

---

<span id="enum_Generic6DOFJoint3D_Flag"></span>

enum **Flag**: [🔗](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag)

<span id="class_Generic6DOFJoint3D_constant_FLAG_ENABLE_LINEAR_LIMIT"></span>

[Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) **FLAG_ENABLE_LINEAR_LIMIT** = `0`

If enabled, linear motion is possible within the given limits.

<span id="class_Generic6DOFJoint3D_constant_FLAG_ENABLE_ANGULAR_LIMIT"></span>

[Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) **FLAG_ENABLE_ANGULAR_LIMIT** = `1`

If enabled, rotational motion is possible within the given limits.

<span id="class_Generic6DOFJoint3D_constant_FLAG_ENABLE_LINEAR_SPRING"></span>

[Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) **FLAG_ENABLE_LINEAR_SPRING** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_Generic6DOFJoint3D_constant_FLAG_ENABLE_ANGULAR_SPRING"></span>

[Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) **FLAG_ENABLE_ANGULAR_SPRING** = `2`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

<span id="class_Generic6DOFJoint3D_constant_FLAG_ENABLE_MOTOR"></span>

[Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) **FLAG_ENABLE_MOTOR** = `4`

If enabled, there is a rotational motor across these axes.

<span id="class_Generic6DOFJoint3D_constant_FLAG_ENABLE_LINEAR_MOTOR"></span>

[Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) **FLAG_ENABLE_LINEAR_MOTOR** = `5`

If enabled, there is a linear motor across these axes.

<span id="class_Generic6DOFJoint3D_constant_FLAG_MAX"></span>

[Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) **FLAG_MAX** = `6`

Represents the size of the [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) enum.

---

### Property Descriptions

.. _class_Generic6DOFJoint3D_property_angular_limit_x/damping:

[float](class_float.md#class_float) **angular_limit_x/damping** = `1.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of rotational damping across the X axis.

The lower, the longer an impulse from one side takes to travel to the other side.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_x/enabled:

[bool](class_bool.md#class_bool) **angular_limit_x/enabled** = `true` 🔗

- void **set_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, rotation across the X axis is limited.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_x/erp:

[float](class_float.md#class_float) **angular_limit_x/erp** = `0.5` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

When rotating across the X axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_x/force_limit:

[float](class_float.md#class_float) **angular_limit_x/force_limit** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The maximum amount of force that can occur, when rotating around the X axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_x/lower_angle:

[float](class_float.md#class_float) **angular_limit_x/lower_angle** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The minimum rotation in negative direction to break loose and rotate around the X axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_x/restitution:

[float](class_float.md#class_float) **angular_limit_x/restitution** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of rotational restitution across the X axis. The lower, the more restitution occurs.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_x/softness:

[float](class_float.md#class_float) **angular_limit_x/softness** = `0.5` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The speed of all rotations across the X axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_x/upper_angle:

[float](class_float.md#class_float) **angular_limit_x/upper_angle** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The minimum rotation in positive direction to break loose and rotate around the X axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_y/damping:

[float](class_float.md#class_float) **angular_limit_y/damping** = `1.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of rotational damping across the Y axis. The lower, the more damping occurs.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_y/enabled:

[bool](class_bool.md#class_bool) **angular_limit_y/enabled** = `true` 🔗

- void **set_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, rotation across the Y axis is limited.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_y/erp:

[float](class_float.md#class_float) **angular_limit_y/erp** = `0.5` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

When rotating across the Y axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_y/force_limit:

[float](class_float.md#class_float) **angular_limit_y/force_limit** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The maximum amount of force that can occur, when rotating around the Y axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_y/lower_angle:

[float](class_float.md#class_float) **angular_limit_y/lower_angle** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The minimum rotation in negative direction to break loose and rotate around the Y axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_y/restitution:

[float](class_float.md#class_float) **angular_limit_y/restitution** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of rotational restitution across the Y axis. The lower, the more restitution occurs.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_y/softness:

[float](class_float.md#class_float) **angular_limit_y/softness** = `0.5` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The speed of all rotations across the Y axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_y/upper_angle:

[float](class_float.md#class_float) **angular_limit_y/upper_angle** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The minimum rotation in positive direction to break loose and rotate around the Y axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_z/damping:

[float](class_float.md#class_float) **angular_limit_z/damping** = `1.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of rotational damping across the Z axis. The lower, the more damping occurs.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_z/enabled:

[bool](class_bool.md#class_bool) **angular_limit_z/enabled** = `true` 🔗

- void **set_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, rotation across the Z axis is limited.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_z/erp:

[float](class_float.md#class_float) **angular_limit_z/erp** = `0.5` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

When rotating across the Z axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_z/force_limit:

[float](class_float.md#class_float) **angular_limit_z/force_limit** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The maximum amount of force that can occur, when rotating around the Z axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_z/lower_angle:

[float](class_float.md#class_float) **angular_limit_z/lower_angle** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The minimum rotation in negative direction to break loose and rotate around the Z axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_z/restitution:

[float](class_float.md#class_float) **angular_limit_z/restitution** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of rotational restitution across the Z axis. The lower, the more restitution occurs.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_z/softness:

[float](class_float.md#class_float) **angular_limit_z/softness** = `0.5` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The speed of all rotations across the Z axis.

---

.. _class_Generic6DOFJoint3D_property_angular_limit_z/upper_angle:

[float](class_float.md#class_float) **angular_limit_z/upper_angle** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The minimum rotation in positive direction to break loose and rotate around the Z axis.

---

.. _class_Generic6DOFJoint3D_property_angular_motor_x/enabled:

[bool](class_bool.md#class_bool) **angular_motor_x/enabled** = `false` 🔗

- void **set_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, a rotating motor at the X axis is enabled.

---

.. _class_Generic6DOFJoint3D_property_angular_motor_x/force_limit:

[float](class_float.md#class_float) **angular_motor_x/force_limit** = `300.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

Maximum acceleration for the motor at the X axis.

---

.. _class_Generic6DOFJoint3D_property_angular_motor_x/target_velocity:

[float](class_float.md#class_float) **angular_motor_x/target_velocity** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

Target speed for the motor at the X axis.

---

.. _class_Generic6DOFJoint3D_property_angular_motor_y/enabled:

[bool](class_bool.md#class_bool) **angular_motor_y/enabled** = `false` 🔗

- void **set_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, a rotating motor at the Y axis is enabled.

---

.. _class_Generic6DOFJoint3D_property_angular_motor_y/force_limit:

[float](class_float.md#class_float) **angular_motor_y/force_limit** = `300.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

Maximum acceleration for the motor at the Y axis.

---

.. _class_Generic6DOFJoint3D_property_angular_motor_y/target_velocity:

[float](class_float.md#class_float) **angular_motor_y/target_velocity** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

Target speed for the motor at the Y axis.

---

.. _class_Generic6DOFJoint3D_property_angular_motor_z/enabled:

[bool](class_bool.md#class_bool) **angular_motor_z/enabled** = `false` 🔗

- void **set_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, a rotating motor at the Z axis is enabled.

---

.. _class_Generic6DOFJoint3D_property_angular_motor_z/force_limit:

[float](class_float.md#class_float) **angular_motor_z/force_limit** = `300.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

Maximum acceleration for the motor at the Z axis.

---

.. _class_Generic6DOFJoint3D_property_angular_motor_z/target_velocity:

[float](class_float.md#class_float) **angular_motor_z/target_velocity** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

Target speed for the motor at the Z axis.

---

.. _class_Generic6DOFJoint3D_property_angular_spring_x/damping:

[float](class_float.md#class_float) **angular_spring_x/damping** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_x/enabled:

[bool](class_bool.md#class_bool) **angular_spring_x/enabled** = `false` 🔗

- void **set_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_x/equilibrium_point:

[float](class_float.md#class_float) **angular_spring_x/equilibrium_point** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_x/stiffness:

[float](class_float.md#class_float) **angular_spring_x/stiffness** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_y/damping:

[float](class_float.md#class_float) **angular_spring_y/damping** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_y/enabled:

[bool](class_bool.md#class_bool) **angular_spring_y/enabled** = `false` 🔗

- void **set_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_y/equilibrium_point:

[float](class_float.md#class_float) **angular_spring_y/equilibrium_point** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_y/stiffness:

[float](class_float.md#class_float) **angular_spring_y/stiffness** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_z/damping:

[float](class_float.md#class_float) **angular_spring_z/damping** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_z/enabled:

[bool](class_bool.md#class_bool) **angular_spring_z/enabled** = `false` 🔗

- void **set_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_z/equilibrium_point:

[float](class_float.md#class_float) **angular_spring_z/equilibrium_point** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_angular_spring_z/stiffness:

[float](class_float.md#class_float) **angular_spring_z/stiffness** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_limit_x/damping:

[float](class_float.md#class_float) **linear_limit_x/damping** = `1.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of damping that happens at the X motion.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_x/enabled:

[bool](class_bool.md#class_bool) **linear_limit_x/enabled** = `true` 🔗

- void **set_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, the linear motion across the X axis is limited.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_x/lower_distance:

[float](class_float.md#class_float) **linear_limit_x/lower_distance** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The minimum difference between the pivot points' X axis.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_x/restitution:

[float](class_float.md#class_float) **linear_limit_x/restitution** = `0.5` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of restitution on the X axis movement. The lower, the more momentum gets lost.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_x/softness:

[float](class_float.md#class_float) **linear_limit_x/softness** = `0.7` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

A factor applied to the movement across the X axis. The lower, the slower the movement.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_x/upper_distance:

[float](class_float.md#class_float) **linear_limit_x/upper_distance** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The maximum difference between the pivot points' X axis.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_y/damping:

[float](class_float.md#class_float) **linear_limit_y/damping** = `1.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of damping that happens at the Y motion.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_y/enabled:

[bool](class_bool.md#class_bool) **linear_limit_y/enabled** = `true` 🔗

- void **set_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, the linear motion across the Y axis is limited.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_y/lower_distance:

[float](class_float.md#class_float) **linear_limit_y/lower_distance** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The minimum difference between the pivot points' Y axis.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_y/restitution:

[float](class_float.md#class_float) **linear_limit_y/restitution** = `0.5` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of restitution on the Y axis movement. The lower, the more momentum gets lost.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_y/softness:

[float](class_float.md#class_float) **linear_limit_y/softness** = `0.7` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

A factor applied to the movement across the Y axis. The lower, the slower the movement.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_y/upper_distance:

[float](class_float.md#class_float) **linear_limit_y/upper_distance** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The maximum difference between the pivot points' Y axis.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_z/damping:

[float](class_float.md#class_float) **linear_limit_z/damping** = `1.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of damping that happens at the Z motion.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_z/enabled:

[bool](class_bool.md#class_bool) **linear_limit_z/enabled** = `true` 🔗

- void **set_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, the linear motion across the Z axis is limited.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_z/lower_distance:

[float](class_float.md#class_float) **linear_limit_z/lower_distance** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The minimum difference between the pivot points' Z axis.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_z/restitution:

[float](class_float.md#class_float) **linear_limit_z/restitution** = `0.5` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The amount of restitution on the Z axis movement. The lower, the more momentum gets lost.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_z/softness:

[float](class_float.md#class_float) **linear_limit_z/softness** = `0.7` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

A factor applied to the movement across the Z axis. The lower, the slower the movement.

---

.. _class_Generic6DOFJoint3D_property_linear_limit_z/upper_distance:

[float](class_float.md#class_float) **linear_limit_z/upper_distance** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The maximum difference between the pivot points' Z axis.

---

.. _class_Generic6DOFJoint3D_property_linear_motor_x/enabled:

[bool](class_bool.md#class_bool) **linear_motor_x/enabled** = `false` 🔗

- void **set_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, then there is a linear motor on the X axis. It will attempt to reach the target velocity while staying within the force limits.

---

.. _class_Generic6DOFJoint3D_property_linear_motor_x/force_limit:

[float](class_float.md#class_float) **linear_motor_x/force_limit** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The maximum force the linear motor can apply on the X axis while trying to reach the target velocity.

---

.. _class_Generic6DOFJoint3D_property_linear_motor_x/target_velocity:

[float](class_float.md#class_float) **linear_motor_x/target_velocity** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The speed that the linear motor will attempt to reach on the X axis.

---

.. _class_Generic6DOFJoint3D_property_linear_motor_y/enabled:

[bool](class_bool.md#class_bool) **linear_motor_y/enabled** = `false` 🔗

- void **set_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, then there is a linear motor on the Y axis. It will attempt to reach the target velocity while staying within the force limits.

---

.. _class_Generic6DOFJoint3D_property_linear_motor_y/force_limit:

[float](class_float.md#class_float) **linear_motor_y/force_limit** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The maximum force the linear motor can apply on the Y axis while trying to reach the target velocity.

---

.. _class_Generic6DOFJoint3D_property_linear_motor_y/target_velocity:

[float](class_float.md#class_float) **linear_motor_y/target_velocity** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The speed that the linear motor will attempt to reach on the Y axis.

---

.. _class_Generic6DOFJoint3D_property_linear_motor_z/enabled:

[bool](class_bool.md#class_bool) **linear_motor_z/enabled** = `false` 🔗

- void **set_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

If `true`, then there is a linear motor on the Z axis. It will attempt to reach the target velocity while staying within the force limits.

---

.. _class_Generic6DOFJoint3D_property_linear_motor_z/force_limit:

[float](class_float.md#class_float) **linear_motor_z/force_limit** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The maximum force the linear motor can apply on the Z axis while trying to reach the target velocity.

---

.. _class_Generic6DOFJoint3D_property_linear_motor_z/target_velocity:

[float](class_float.md#class_float) **linear_motor_z/target_velocity** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

The speed that the linear motor will attempt to reach on the Z axis.

---

.. _class_Generic6DOFJoint3D_property_linear_spring_x/damping:

[float](class_float.md#class_float) **linear_spring_x/damping** = `0.01` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_x/enabled:

[bool](class_bool.md#class_bool) **linear_spring_x/enabled** = `false` 🔗

- void **set_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_x/equilibrium_point:

[float](class_float.md#class_float) **linear_spring_x/equilibrium_point** = `0.0` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_x/stiffness:

[float](class_float.md#class_float) **linear_spring_x/stiffness** = `0.01` 🔗

- void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_y/damping:

[float](class_float.md#class_float) **linear_spring_y/damping** = `0.01` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_y/enabled:

[bool](class_bool.md#class_bool) **linear_spring_y/enabled** = `false` 🔗

- void **set_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_y/equilibrium_point:

[float](class_float.md#class_float) **linear_spring_y/equilibrium_point** = `0.0` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_y/stiffness:

[float](class_float.md#class_float) **linear_spring_y/stiffness** = `0.01` 🔗

- void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_z/damping:

[float](class_float.md#class_float) **linear_spring_z/damping** = `0.01` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_z/enabled:

[bool](class_bool.md#class_bool) **linear_spring_z/enabled** = `false` 🔗

- void **set_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_z/equilibrium_point:

[float](class_float.md#class_float) **linear_spring_z/equilibrium_point** = `0.0` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

.. _class_Generic6DOFJoint3D_property_linear_spring_z/stiffness:

[float](class_float.md#class_float) **linear_spring_z/stiffness** = `0.01` 🔗

- void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const*

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

### Method Descriptions

<span id="class_Generic6DOFJoint3D_method_get_flag_x"></span>

[bool](class_bool.md#class_bool) **get_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const* [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_flag_x)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_get_flag_y"></span>

[bool](class_bool.md#class_bool) **get_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const* [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_flag_y)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_get_flag_z"></span>

[bool](class_bool.md#class_bool) **get_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag) ) *const* [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_flag_z)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_get_param_x"></span>

[float](class_float.md#class_float) **get_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const* [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_param_x)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_get_param_y"></span>

[float](class_float.md#class_float) **get_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const* [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_param_y)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_get_param_z"></span>

[float](class_float.md#class_float) **get_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param) ) *const* [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_get_param_z)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_set_flag_x"></span>

void **set_flag_x** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) ) [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_flag_x)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_set_flag_y"></span>

void **set_flag_y** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) ) [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_flag_y)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_set_flag_z"></span>

void **set_flag_z** ( flag: [Flag](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Flag), value: [bool](class_bool.md#class_bool) ) [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_flag_z)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_set_param_x"></span>

void **set_param_x** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) ) [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_param_x)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_set_param_y"></span>

void **set_param_y** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) ) [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_param_y)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_Generic6DOFJoint3D_method_set_param_z"></span>

void **set_param_z** ( param: [Param](class_generic6dofjoint3d.md#enum_Generic6DOFJoint3D_Param), value: [float](class_float.md#class_float) ) [🔗](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D_method_set_param_z)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
