<span id="class_JacobianIK3D"></span>

## JacobianIK3D

**Inherits:** [IterateIK3D](class_iterateik3d.md#class_IterateIK3D) **<** [ChainIK3D](class_chainik3d.md#class_ChainIK3D) **<** [IKModifier3D](class_ikmodifier3d.md#class_IKModifier3D) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Jacobian transpose based inverse kinematics solver.

### Description

**JacobianIK3D** calculates rotations for all joints simultaneously, producing natural and smooth movement. It is particularly suited for biological animations.

The resulting twist around the forward vector will always be kept from the previous pose.

 **Note:** It converges more slowly than other IK solvers, leading to gentler and less immediate tracking of targets.
