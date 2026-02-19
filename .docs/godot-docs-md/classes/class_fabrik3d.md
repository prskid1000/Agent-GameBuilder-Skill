<span id="class_FABRIK3D"></span>

## FABRIK3D

**Inherits:** [IterateIK3D](class_iterateik3d.md#class_IterateIK3D) **<** [ChainIK3D](class_chainik3d.md#class_ChainIK3D) **<** [IKModifier3D](class_ikmodifier3d.md#class_IKModifier3D) **<** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Position based forward and backward reaching inverse kinematics solver.

### Description

**FABRIK3D** is position based IK, allowing precise and accurate tracking of targets. It's ideal for simple chains without limitations.

The resulting twist around the forward vector will always be kept from the previous pose.

 **Note:** When the target is close to the root, it tends to produce zig-zag patterns, resulting in unnatural visual movement.

### Tutorials

- Inverse Kinematics Returns to Godot 4.6 - IKModifier3D
