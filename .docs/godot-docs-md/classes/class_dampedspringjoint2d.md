<span id="class_DampedSpringJoint2D"></span>

## DampedSpringJoint2D

**Inherits:** [Joint2D](class_joint2d.md#class_Joint2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A physics joint that connects two 2D physics bodies with a spring-like force.

### Description

A physics joint that connects two 2D physics bodies with a spring-like force. This behaves like a spring that always wants to stretch to a given length.

### Properties


| [float](class_float.md#class_float) | [damping](class_dampedspringjoint2d.md#class_DampedSpringJoint2D_property_damping) | `1.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [length](class_dampedspringjoint2d.md#class_DampedSpringJoint2D_property_length) | `50.0` |
| [float](class_float.md#class_float) | [rest_length](class_dampedspringjoint2d.md#class_DampedSpringJoint2D_property_rest_length) | `0.0` |
| [float](class_float.md#class_float) | [stiffness](class_dampedspringjoint2d.md#class_DampedSpringJoint2D_property_stiffness) | `20.0` |

---

### Property Descriptions

<span id="class_DampedSpringJoint2D_property_damping"></span>

[float](class_float.md#class_float) **damping** = `1.0` [🔗](class_dampedspringjoint2d.md#class_DampedSpringJoint2D_property_damping)

- void **set_damping** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_damping** ( )

The spring joint's damping ratio. A value between `0` and `1`. When the two bodies move into different directions the system tries to align them to the spring axis again. A high [damping](class_dampedspringjoint2d.md#class_DampedSpringJoint2D_property_damping) value forces the attached bodies to align faster.

---

<span id="class_DampedSpringJoint2D_property_length"></span>

[float](class_float.md#class_float) **length** = `50.0` [🔗](class_dampedspringjoint2d.md#class_DampedSpringJoint2D_property_length)

- void **set_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_length** ( )

The spring joint's maximum length. The two attached bodies cannot stretch it past this value.

---

<span id="class_DampedSpringJoint2D_property_rest_length"></span>

[float](class_float.md#class_float) **rest_length** = `0.0` [🔗](class_dampedspringjoint2d.md#class_DampedSpringJoint2D_property_rest_length)

- void **set_rest_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_rest_length** ( )

When the bodies attached to the spring joint move they stretch or squash it. The joint always tries to resize towards this length.

---

<span id="class_DampedSpringJoint2D_property_stiffness"></span>

[float](class_float.md#class_float) **stiffness** = `20.0` [🔗](class_dampedspringjoint2d.md#class_DampedSpringJoint2D_property_stiffness)

- void **set_stiffness** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_stiffness** ( )

The higher the value, the less the bodies attached to the joint will deform it. The joint applies an opposing force to the bodies, the product of the stiffness multiplied by the size difference from its resting length.
