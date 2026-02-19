<span id="class_Joint2D"></span>

## Joint2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [DampedSpringJoint2D](class_dampedspringjoint2d.md#class_DampedSpringJoint2D), [GrooveJoint2D](class_groovejoint2d.md#class_GrooveJoint2D), [PinJoint2D](class_pinjoint2d.md#class_PinJoint2D)

Abstract base class for all 2D physics joints.

### Description

Abstract base class for all joints in 2D physics. 2D joints bind together two physics bodies ([node_a](class_joint2d.md#class_Joint2D_property_node_a) and [node_b](class_joint2d.md#class_Joint2D_property_node_b)) and apply a constraint.

### Properties


| [float](class_float.md#class_float) | [bias](class_joint2d.md#class_Joint2D_property_bias) | `0.0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [disable_collision](class_joint2d.md#class_Joint2D_property_disable_collision) | `true` |
| [NodePath](class_nodepath.md#class_NodePath) | [node_a](class_joint2d.md#class_Joint2D_property_node_a) | `NodePath("")` |
| [NodePath](class_nodepath.md#class_NodePath) | [node_b](class_joint2d.md#class_Joint2D_property_node_b) | `NodePath("")` |

### Methods


| [RID](class_rid.md#class_RID) | [get_rid](class_joint2d.md#class_Joint2D_method_get_rid) ( ) const |
| --- | --- |

---

### Property Descriptions

<span id="class_Joint2D_property_bias"></span>

[float](class_float.md#class_float) **bias** = `0.0` [🔗](class_joint2d.md#class_Joint2D_property_bias)

- void **set_bias** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_bias** ( )

When [node_a](class_joint2d.md#class_Joint2D_property_node_a) and [node_b](class_joint2d.md#class_Joint2D_property_node_b) move in different directions the [bias](class_joint2d.md#class_Joint2D_property_bias) controls how fast the joint pulls them back to their original position. The lower the [bias](class_joint2d.md#class_Joint2D_property_bias) the more the two bodies can pull on the joint.

When set to `0`, the default value from ProjectSettings.physics/2d/solver/default_constraint_bias is used.

---

<span id="class_Joint2D_property_disable_collision"></span>

[bool](class_bool.md#class_bool) **disable_collision** = `true` [🔗](class_joint2d.md#class_Joint2D_property_disable_collision)

- void **set_exclude_nodes_from_collision** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_exclude_nodes_from_collision** ( )

If `true`, the two bodies bound together do not collide with each other.

---

<span id="class_Joint2D_property_node_a"></span>

[NodePath](class_nodepath.md#class_NodePath) **node_a** = `NodePath("")` [🔗](class_joint2d.md#class_Joint2D_property_node_a)

- void **set_node_a** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_node_a** ( )

Path to the first body (A) attached to the joint. The node must inherit [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D).

---

<span id="class_Joint2D_property_node_b"></span>

[NodePath](class_nodepath.md#class_NodePath) **node_b** = `NodePath("")` [🔗](class_joint2d.md#class_Joint2D_property_node_b)

- void **set_node_b** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_node_b** ( )

Path to the second body (B) attached to the joint. The node must inherit [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D).

---

### Method Descriptions

<span id="class_Joint2D_method_get_rid"></span>

[RID](class_rid.md#class_RID) **get_rid** ( ) *const* [🔗](class_joint2d.md#class_Joint2D_method_get_rid)

Returns the joint's internal [RID](class_rid.md#class_RID) from the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D).
