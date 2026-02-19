<span id="class_Joint3D"></span>

## Joint3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [ConeTwistJoint3D](class_conetwistjoint3d.md#class_ConeTwistJoint3D), [Generic6DOFJoint3D](class_generic6dofjoint3d.md#class_Generic6DOFJoint3D), [HingeJoint3D](class_hingejoint3d.md#class_HingeJoint3D), [PinJoint3D](class_pinjoint3d.md#class_PinJoint3D), [SliderJoint3D](class_sliderjoint3d.md#class_SliderJoint3D)

Abstract base class for all 3D physics joints.

### Description

Abstract base class for all joints in 3D physics. 3D joints bind together two physics bodies ([node_a](class_joint3d.md#class_Joint3D_property_node_a) and [node_b](class_joint3d.md#class_Joint3D_property_node_b)) and apply a constraint. If only one body is defined, it is attached to a fixed [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) without collision shapes.

### Tutorials

- 3D Truck Town Demo

### Properties


| [bool](class_bool.md#class_bool) | [exclude_nodes_from_collision](class_joint3d.md#class_Joint3D_property_exclude_nodes_from_collision) | `true` |
| --- | --- | --- |
| [NodePath](class_nodepath.md#class_NodePath) | [node_a](class_joint3d.md#class_Joint3D_property_node_a) | `NodePath("")` |
| [NodePath](class_nodepath.md#class_NodePath) | [node_b](class_joint3d.md#class_Joint3D_property_node_b) | `NodePath("")` |
| [int](class_int.md#class_int) | [solver_priority](class_joint3d.md#class_Joint3D_property_solver_priority) | `1` |

### Methods


| [RID](class_rid.md#class_RID) | [get_rid](class_joint3d.md#class_Joint3D_method_get_rid) ( ) const |
| --- | --- |

---

### Property Descriptions

<span id="class_Joint3D_property_exclude_nodes_from_collision"></span>

[bool](class_bool.md#class_bool) **exclude_nodes_from_collision** = `true` [🔗](class_joint3d.md#class_Joint3D_property_exclude_nodes_from_collision)

- void **set_exclude_nodes_from_collision** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_exclude_nodes_from_collision** ( )

If `true`, the two bodies bound together do not collide with each other.

---

<span id="class_Joint3D_property_node_a"></span>

[NodePath](class_nodepath.md#class_NodePath) **node_a** = `NodePath("")` [🔗](class_joint3d.md#class_Joint3D_property_node_a)

- void **set_node_a** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_node_a** ( )

Path to the first node (A) attached to the joint. The node must inherit [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D).

If left empty and [node_b](class_joint3d.md#class_Joint3D_property_node_b) is set, the body is attached to a fixed [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) without collision shapes.

---

<span id="class_Joint3D_property_node_b"></span>

[NodePath](class_nodepath.md#class_NodePath) **node_b** = `NodePath("")` [🔗](class_joint3d.md#class_Joint3D_property_node_b)

- void **set_node_b** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_node_b** ( )

Path to the second node (B) attached to the joint. The node must inherit [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D).

If left empty and [node_a](class_joint3d.md#class_Joint3D_property_node_a) is set, the body is attached to a fixed [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) without collision shapes.

---

<span id="class_Joint3D_property_solver_priority"></span>

[int](class_int.md#class_int) **solver_priority** = `1` [🔗](class_joint3d.md#class_Joint3D_property_solver_priority)

- void **set_solver_priority** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_solver_priority** ( )

The priority used to define which solver is executed first for multiple joints. The lower the value, the higher the priority.

---

### Method Descriptions

<span id="class_Joint3D_method_get_rid"></span>

[RID](class_rid.md#class_RID) **get_rid** ( ) *const* [🔗](class_joint3d.md#class_Joint3D_method_get_rid)

Returns the joint's internal [RID](class_rid.md#class_RID) from the [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D).
