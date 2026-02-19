.. meta::
	:keywords: ragdoll

<span id="class_PhysicalBone2D"></span>

## PhysicalBone2D

**Inherits:** [RigidBody2D](class_rigidbody2d.md#class_RigidBody2D) **<** [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) **<** [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A [RigidBody2D](class_rigidbody2d.md#class_RigidBody2D)-derived node used to make [Bone2D](class_bone2d.md#class_Bone2D) s in a [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) react to physics.

### Description

The **PhysicalBone2D** node is a [RigidBody2D](class_rigidbody2d.md#class_RigidBody2D)-based node that can be used to make [Bone2D](class_bone2d.md#class_Bone2D) s in a [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) react to physics.

 **Note:** To make the [Bone2D](class_bone2d.md#class_Bone2D) s visually follow the **PhysicalBone2D** node, use a [SkeletonModification2DPhysicalBones](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones) modification on the [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) parent.

 **Note:** The **PhysicalBone2D** node does not automatically create a [Joint2D](class_joint2d.md#class_Joint2D) node to keep **PhysicalBone2D** nodes together. They must be created manually. For most cases, you want to use a [PinJoint2D](class_pinjoint2d.md#class_PinJoint2D) node. The **PhysicalBone2D** node will automatically configure the [Joint2D](class_joint2d.md#class_Joint2D) node once it's been added as a child node.

### Properties


| [bool](class_bool.md#class_bool) | [auto_configure_joint](class_physicalbone2d.md#class_PhysicalBone2D_property_auto_configure_joint) | `true` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [bone2d_index](class_physicalbone2d.md#class_PhysicalBone2D_property_bone2d_index) | `-1` |
| [NodePath](class_nodepath.md#class_NodePath) | [bone2d_nodepath](class_physicalbone2d.md#class_PhysicalBone2D_property_bone2d_nodepath) | `NodePath("")` |
| [bool](class_bool.md#class_bool) | [follow_bone_when_simulating](class_physicalbone2d.md#class_PhysicalBone2D_property_follow_bone_when_simulating) | `false` |
| [bool](class_bool.md#class_bool) | [simulate_physics](class_physicalbone2d.md#class_PhysicalBone2D_property_simulate_physics) | `false` |

### Methods


| [Joint2D](class_joint2d.md#class_Joint2D) | [get_joint](class_physicalbone2d.md#class_PhysicalBone2D_method_get_joint) ( ) const |
| --- | --- |
| [bool](class_bool.md#class_bool) | [is_simulating_physics](class_physicalbone2d.md#class_PhysicalBone2D_method_is_simulating_physics) ( ) const |

---

### Property Descriptions

<span id="class_PhysicalBone2D_property_auto_configure_joint"></span>

[bool](class_bool.md#class_bool) **auto_configure_joint** = `true` [🔗](class_physicalbone2d.md#class_PhysicalBone2D_property_auto_configure_joint)

- void **set_auto_configure_joint** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_auto_configure_joint** ( )

If `true`, the **PhysicalBone2D** will automatically configure the first [Joint2D](class_joint2d.md#class_Joint2D) child node. The automatic configuration is limited to setting up the node properties and positioning the [Joint2D](class_joint2d.md#class_Joint2D).

---

<span id="class_PhysicalBone2D_property_bone2d_index"></span>

[int](class_int.md#class_int) **bone2d_index** = `-1` [🔗](class_physicalbone2d.md#class_PhysicalBone2D_property_bone2d_index)

- void **set_bone2d_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bone2d_index** ( )

The index of the [Bone2D](class_bone2d.md#class_Bone2D) that this **PhysicalBone2D** should simulate.

---

<span id="class_PhysicalBone2D_property_bone2d_nodepath"></span>

[NodePath](class_nodepath.md#class_NodePath) **bone2d_nodepath** = `NodePath("")` [🔗](class_physicalbone2d.md#class_PhysicalBone2D_property_bone2d_nodepath)

- void **set_bone2d_nodepath** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_bone2d_nodepath** ( )

The [NodePath](class_nodepath.md#class_NodePath) to the [Bone2D](class_bone2d.md#class_Bone2D) that this **PhysicalBone2D** should simulate.

---

<span id="class_PhysicalBone2D_property_follow_bone_when_simulating"></span>

[bool](class_bool.md#class_bool) **follow_bone_when_simulating** = `false` [🔗](class_physicalbone2d.md#class_PhysicalBone2D_property_follow_bone_when_simulating)

- void **set_follow_bone_when_simulating** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_follow_bone_when_simulating** ( )

If `true`, the **PhysicalBone2D** will keep the transform of the bone it is bound to when simulating physics.

---

<span id="class_PhysicalBone2D_property_simulate_physics"></span>

[bool](class_bool.md#class_bool) **simulate_physics** = `false` [🔗](class_physicalbone2d.md#class_PhysicalBone2D_property_simulate_physics)

- void **set_simulate_physics** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_simulate_physics** ( )

If `true`, the **PhysicalBone2D** will start simulating using physics. If `false`, the **PhysicalBone2D** will follow the transform of the [Bone2D](class_bone2d.md#class_Bone2D) node.

 **Note:** To have the [Bone2D](class_bone2d.md#class_Bone2D) s visually follow the **PhysicalBone2D**, use a [SkeletonModification2DPhysicalBones](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones) modification on the [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) node with the [Bone2D](class_bone2d.md#class_Bone2D) nodes.

---

### Method Descriptions

<span id="class_PhysicalBone2D_method_get_joint"></span>

[Joint2D](class_joint2d.md#class_Joint2D) **get_joint** ( ) *const* [🔗](class_physicalbone2d.md#class_PhysicalBone2D_method_get_joint)

Returns the first [Joint2D](class_joint2d.md#class_Joint2D) child node, if one exists. This is mainly a helper function to make it easier to get the [Joint2D](class_joint2d.md#class_Joint2D) that the **PhysicalBone2D** is autoconfiguring.

---

<span id="class_PhysicalBone2D_method_is_simulating_physics"></span>

[bool](class_bool.md#class_bool) **is_simulating_physics** ( ) *const* [🔗](class_physicalbone2d.md#class_PhysicalBone2D_method_is_simulating_physics)

Returns a boolean that indicates whether the **PhysicalBone2D** is running and simulating using the Godot 2D physics engine. When `true`, the PhysicalBone2D node is using physics.
