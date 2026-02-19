<span id="class_Skeleton2D"></span>

## Skeleton2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

The parent of a hierarchy of [Bone2D](class_bone2d.md#class_Bone2D) s, used to create a 2D skeletal animation.

### Description

**Skeleton2D** parents a hierarchy of [Bone2D](class_bone2d.md#class_Bone2D) nodes. It holds a reference to each [Bone2D](class_bone2d.md#class_Bone2D)'s rest pose and acts as a single point of access to its bones.

To set up different types of inverse kinematics for the given Skeleton2D, a [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) should be created. The inverse kinematics be applied by increasing [SkeletonModificationStack2D.modification_count](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_property_modification_count) and creating the desired number of modifications.

### Tutorials

- [2D skeletons](../tutorials/animation/2d_skeletons.md)

### Methods


| void | [execute_modifications](class_skeleton2d.md#class_Skeleton2D_method_execute_modifications) ( delta: [float](class_float.md#class_float), execution_mode: [int](class_int.md#class_int) ) |
| --- | --- |
| [Bone2D](class_bone2d.md#class_Bone2D) | [get_bone](class_skeleton2d.md#class_Skeleton2D_method_get_bone) ( idx: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_bone_count](class_skeleton2d.md#class_Skeleton2D_method_get_bone_count) ( ) const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [get_bone_local_pose_override](class_skeleton2d.md#class_Skeleton2D_method_get_bone_local_pose_override) ( bone_idx: [int](class_int.md#class_int) ) |
| [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) | [get_modification_stack](class_skeleton2d.md#class_Skeleton2D_method_get_modification_stack) ( ) const |
| [RID](class_rid.md#class_RID) | [get_skeleton](class_skeleton2d.md#class_Skeleton2D_method_get_skeleton) ( ) const |
| void | [set_bone_local_pose_override](class_skeleton2d.md#class_Skeleton2D_method_set_bone_local_pose_override) ( bone_idx: [int](class_int.md#class_int), override_pose: [Transform2D](class_transform2d.md#class_Transform2D), strength: [float](class_float.md#class_float), persistent: [bool](class_bool.md#class_bool) ) |
| void | [set_modification_stack](class_skeleton2d.md#class_Skeleton2D_method_set_modification_stack) ( modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) ) |

---

### Signals

<span id="class_Skeleton2D_signal_bone_setup_changed"></span>

**bone_setup_changed** ( ) [🔗](class_skeleton2d.md#class_Skeleton2D_signal_bone_setup_changed)

Emitted when the [Bone2D](class_bone2d.md#class_Bone2D) setup attached to this skeletons changes. This is primarily used internally within the skeleton.

---

### Method Descriptions

<span id="class_Skeleton2D_method_execute_modifications"></span>

void **execute_modifications** ( delta: [float](class_float.md#class_float), execution_mode: [int](class_int.md#class_int) ) [🔗](class_skeleton2d.md#class_Skeleton2D_method_execute_modifications)

Executes all the modifications on the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D), if the Skeleton2D has one assigned.

---

<span id="class_Skeleton2D_method_get_bone"></span>

[Bone2D](class_bone2d.md#class_Bone2D) **get_bone** ( idx: [int](class_int.md#class_int) ) [🔗](class_skeleton2d.md#class_Skeleton2D_method_get_bone)

Returns a [Bone2D](class_bone2d.md#class_Bone2D) from the node hierarchy parented by Skeleton2D. The object to return is identified by the parameter `idx`. Bones are indexed by descending the node hierarchy from top to bottom, adding the children of each branch before moving to the next sibling.

---

<span id="class_Skeleton2D_method_get_bone_count"></span>

[int](class_int.md#class_int) **get_bone_count** ( ) *const* [🔗](class_skeleton2d.md#class_Skeleton2D_method_get_bone_count)

Returns the number of [Bone2D](class_bone2d.md#class_Bone2D) nodes in the node hierarchy parented by Skeleton2D.

---

<span id="class_Skeleton2D_method_get_bone_local_pose_override"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **get_bone_local_pose_override** ( bone_idx: [int](class_int.md#class_int) ) [🔗](class_skeleton2d.md#class_Skeleton2D_method_get_bone_local_pose_override)

Returns the local pose override transform for `bone_idx`.

---

<span id="class_Skeleton2D_method_get_modification_stack"></span>

[SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) **get_modification_stack** ( ) *const* [🔗](class_skeleton2d.md#class_Skeleton2D_method_get_modification_stack)

Returns the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) attached to this skeleton, if one exists.

---

<span id="class_Skeleton2D_method_get_skeleton"></span>

[RID](class_rid.md#class_RID) **get_skeleton** ( ) *const* [🔗](class_skeleton2d.md#class_Skeleton2D_method_get_skeleton)

Returns the [RID](class_rid.md#class_RID) of a Skeleton2D instance.

---

<span id="class_Skeleton2D_method_set_bone_local_pose_override"></span>

void **set_bone_local_pose_override** ( bone_idx: [int](class_int.md#class_int), override_pose: [Transform2D](class_transform2d.md#class_Transform2D), strength: [float](class_float.md#class_float), persistent: [bool](class_bool.md#class_bool) ) [🔗](class_skeleton2d.md#class_Skeleton2D_method_set_bone_local_pose_override)

Sets the local pose transform, `override_pose`, for the bone at `bone_idx`.

 `strength` is the interpolation strength that will be used when applying the pose, and `persistent` determines if the applied pose will remain.

 **Note:** The pose transform needs to be a local transform relative to the [Bone2D](class_bone2d.md#class_Bone2D) node at `bone_idx`!

---

<span id="class_Skeleton2D_method_set_modification_stack"></span>

void **set_modification_stack** ( modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) ) [🔗](class_skeleton2d.md#class_Skeleton2D_method_set_modification_stack)

Sets the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) attached to this skeleton.
