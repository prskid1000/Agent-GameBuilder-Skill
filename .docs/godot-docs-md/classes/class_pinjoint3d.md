<span id="class_PinJoint3D"></span>

## PinJoint3D

**Inherits:** [Joint3D](class_joint3d.md#class_Joint3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate.

### Description

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate. For example, a [RigidBody3D](class_rigidbody3d.md#class_RigidBody3D) can be attached to a [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) to create a pendulum or a seesaw.

### Properties


| [float](class_float.md#class_float) | params/bias | `0.3` |
| --- | --- | --- |
| [float](class_float.md#class_float) | params/damping | `1.0` |
| [float](class_float.md#class_float) | params/impulse_clamp | `0.0` |

### Methods


| [float](class_float.md#class_float) | [get_param](class_pinjoint3d.md#class_PinJoint3D_method_get_param) ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param) ) const |
| --- | --- |
| void | [set_param](class_pinjoint3d.md#class_PinJoint3D_method_set_param) ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param), value: [float](class_float.md#class_float) ) |

---

### Enumerations

<span id="enum_PinJoint3D_Param"></span>

enum **Param**: [🔗](class_pinjoint3d.md#enum_PinJoint3D_Param)

<span id="class_PinJoint3D_constant_PARAM_BIAS"></span>

[Param](class_pinjoint3d.md#enum_PinJoint3D_Param) **PARAM_BIAS** = `0`

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.

<span id="class_PinJoint3D_constant_PARAM_DAMPING"></span>

[Param](class_pinjoint3d.md#enum_PinJoint3D_Param) **PARAM_DAMPING** = `1`

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.

<span id="class_PinJoint3D_constant_PARAM_IMPULSE_CLAMP"></span>

[Param](class_pinjoint3d.md#enum_PinJoint3D_Param) **PARAM_IMPULSE_CLAMP** = `2`

If above 0, this value is the maximum value for an impulse that this Joint3D produces.

---

### Property Descriptions

.. _class_PinJoint3D_property_params/bias:

[float](class_float.md#class_float) **params/bias** = `0.3` 🔗

- void **set_param** ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param) ) *const*

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.

---

.. _class_PinJoint3D_property_params/damping:

[float](class_float.md#class_float) **params/damping** = `1.0` 🔗

- void **set_param** ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param) ) *const*

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.

---

.. _class_PinJoint3D_property_params/impulse_clamp:

[float](class_float.md#class_float) **params/impulse_clamp** = `0.0` 🔗

- void **set_param** ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param), value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_param** ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param) ) *const*

If above 0, this value is the maximum value for an impulse that this Joint3D produces.

---

### Method Descriptions

<span id="class_PinJoint3D_method_get_param"></span>

[float](class_float.md#class_float) **get_param** ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param) ) *const* [🔗](class_pinjoint3d.md#class_PinJoint3D_method_get_param)

Returns the value of the specified parameter.

---

<span id="class_PinJoint3D_method_set_param"></span>

void **set_param** ( param: [Param](class_pinjoint3d.md#enum_PinJoint3D_Param), value: [float](class_float.md#class_float) ) [🔗](class_pinjoint3d.md#class_PinJoint3D_method_set_param)

Sets the value of the specified parameter.
