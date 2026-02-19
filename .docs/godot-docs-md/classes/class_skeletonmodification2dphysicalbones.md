<span id="class_SkeletonModification2DPhysicalBones"></span>

## SkeletonModification2DPhysicalBones

**Experimental:** Physical bones may be changed in the future to perform the position update of [Bone2D](class_bone2d.md#class_Bone2D) on their own, without needing this resource.

**Inherits:** [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A modification that applies the transforms of [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes to [Bone2D](class_bone2d.md#class_Bone2D) nodes.

### Description

This modification takes the transforms of [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes and applies them to [Bone2D](class_bone2d.md#class_Bone2D) nodes. This allows the [Bone2D](class_bone2d.md#class_Bone2D) nodes to react to physics thanks to the linked [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes.

### Properties


| [int](class_int.md#class_int) | [physical_bone_chain_length](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_property_physical_bone_chain_length) | `0` |
| --- | --- | --- |

### Methods


| void | [fetch_physical_bones](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_fetch_physical_bones) ( ) |
| --- | --- |
| [NodePath](class_nodepath.md#class_NodePath) | [get_physical_bone_node](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_get_physical_bone_node) ( joint_idx: [int](class_int.md#class_int) ) const |
| void | [set_physical_bone_node](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_set_physical_bone_node) ( joint_idx: [int](class_int.md#class_int), physicalbone2d_node: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [start_simulation](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_start_simulation) ( bones: [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] = [] ) |
| void | [stop_simulation](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_stop_simulation) ( bones: [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] = [] ) |

---

### Property Descriptions

<span id="class_SkeletonModification2DPhysicalBones_property_physical_bone_chain_length"></span>

[int](class_int.md#class_int) **physical_bone_chain_length** = `0` [🔗](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_property_physical_bone_chain_length)

- void **set_physical_bone_chain_length** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_physical_bone_chain_length** ( )

The number of [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes linked in this modification.

---

### Method Descriptions

<span id="class_SkeletonModification2DPhysicalBones_method_fetch_physical_bones"></span>

void **fetch_physical_bones** ( ) [🔗](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_fetch_physical_bones)

Empties the list of [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes and populates it with all [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes that are children of the [Skeleton2D](class_skeleton2d.md#class_Skeleton2D).

---

<span id="class_SkeletonModification2DPhysicalBones_method_get_physical_bone_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_physical_bone_node** ( joint_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_get_physical_bone_node)

Returns the [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) node at `joint_idx`.

---

<span id="class_SkeletonModification2DPhysicalBones_method_set_physical_bone_node"></span>

void **set_physical_bone_node** ( joint_idx: [int](class_int.md#class_int), physicalbone2d_node: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_set_physical_bone_node)

Sets the [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) node at `joint_idx`.

 **Note:** This is just the index used for this modification, not the bone index used in the [Skeleton2D](class_skeleton2d.md#class_Skeleton2D).

---

<span id="class_SkeletonModification2DPhysicalBones_method_start_simulation"></span>

void **start_simulation** ( bones: [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] = [] ) [🔗](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_start_simulation)

Tell the [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes to start simulating and interacting with the physics world.

Optionally, an array of bone names can be passed to this function, and that will cause only [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes with those names to start simulating.

---

<span id="class_SkeletonModification2DPhysicalBones_method_stop_simulation"></span>

void **stop_simulation** ( bones: [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] = [] ) [🔗](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones_method_stop_simulation)

Tell the [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes to stop simulating and interacting with the physics world.

Optionally, an array of bone names can be passed to this function, and that will cause only [PhysicalBone2D](class_physicalbone2d.md#class_PhysicalBone2D) nodes with those names to stop simulating.
