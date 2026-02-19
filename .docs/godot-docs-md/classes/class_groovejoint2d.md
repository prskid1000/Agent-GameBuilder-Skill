<span id="class_GrooveJoint2D"></span>

## GrooveJoint2D

**Inherits:** [Joint2D](class_joint2d.md#class_Joint2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A physics joint that restricts the movement of two 2D physics bodies to a fixed axis.

### Description

A physics joint that restricts the movement of two 2D physics bodies to a fixed axis. For example, a [StaticBody2D](class_staticbody2d.md#class_StaticBody2D) representing a piston base can be attached to a [RigidBody2D](class_rigidbody2d.md#class_RigidBody2D) representing the piston head, moving up and down.

### Properties


| [float](class_float.md#class_float) | [initial_offset](class_groovejoint2d.md#class_GrooveJoint2D_property_initial_offset) | `25.0` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [length](class_groovejoint2d.md#class_GrooveJoint2D_property_length) | `50.0` |

---

### Property Descriptions

<span id="class_GrooveJoint2D_property_initial_offset"></span>

[float](class_float.md#class_float) **initial_offset** = `25.0` [🔗](class_groovejoint2d.md#class_GrooveJoint2D_property_initial_offset)

- void **set_initial_offset** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_initial_offset** ( )

The body B's initial anchor position defined by the joint's origin and a local offset [initial_offset](class_groovejoint2d.md#class_GrooveJoint2D_property_initial_offset) along the joint's Y axis (along the groove).

---

<span id="class_GrooveJoint2D_property_length"></span>

[float](class_float.md#class_float) **length** = `50.0` [🔗](class_groovejoint2d.md#class_GrooveJoint2D_property_length)

- void **set_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_length** ( )

The groove's length. The groove is from the joint's origin towards [length](class_groovejoint2d.md#class_GrooveJoint2D_property_length) along the joint's local Y axis.
