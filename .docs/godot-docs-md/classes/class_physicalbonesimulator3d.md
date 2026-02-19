<span id="class_PhysicalBoneSimulator3D"></span>

## PhysicalBoneSimulator3D

**Inherits:** [SkeletonModifier3D](class_skeletonmodifier3d.md#class_SkeletonModifier3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Node that can be the parent of [PhysicalBone3D](class_physicalbone3d.md#class_PhysicalBone3D) and can apply the simulation results to [Skeleton3D](class_skeleton3d.md#class_Skeleton3D).

### Description

Node that can be the parent of [PhysicalBone3D](class_physicalbone3d.md#class_PhysicalBone3D) and can apply the simulation results to [Skeleton3D](class_skeleton3d.md#class_Skeleton3D).

### Methods


| [bool](class_bool.md#class_bool) | [is_simulating_physics](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_is_simulating_physics) ( ) const |
| --- | --- |
| void | [physical_bones_add_collision_exception](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_physical_bones_add_collision_exception) ( exception: [RID](class_rid.md#class_RID) ) |
| void | [physical_bones_remove_collision_exception](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_physical_bones_remove_collision_exception) ( exception: [RID](class_rid.md#class_RID) ) |
| void | [physical_bones_start_simulation](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_physical_bones_start_simulation) ( bones: [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] = [] ) |
| void | [physical_bones_stop_simulation](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_physical_bones_stop_simulation) ( ) |

---

### Method Descriptions

<span id="class_PhysicalBoneSimulator3D_method_is_simulating_physics"></span>

[bool](class_bool.md#class_bool) **is_simulating_physics** ( ) *const* [🔗](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_is_simulating_physics)

Returns a boolean that indicates whether the **PhysicalBoneSimulator3D** is running and simulating.

---

<span id="class_PhysicalBoneSimulator3D_method_physical_bones_add_collision_exception"></span>

void **physical_bones_add_collision_exception** ( exception: [RID](class_rid.md#class_RID) ) [🔗](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_physical_bones_add_collision_exception)

Adds a collision exception to the physical bone.

Works just like the [RigidBody3D](class_rigidbody3d.md#class_RigidBody3D) node.

---

<span id="class_PhysicalBoneSimulator3D_method_physical_bones_remove_collision_exception"></span>

void **physical_bones_remove_collision_exception** ( exception: [RID](class_rid.md#class_RID) ) [🔗](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_physical_bones_remove_collision_exception)

Removes a collision exception to the physical bone.

Works just like the [RigidBody3D](class_rigidbody3d.md#class_RigidBody3D) node.

---

<span id="class_PhysicalBoneSimulator3D_method_physical_bones_start_simulation"></span>

void **physical_bones_start_simulation** ( bones: [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] = [] ) [🔗](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_physical_bones_start_simulation)

Tells the [PhysicalBone3D](class_physicalbone3d.md#class_PhysicalBone3D) nodes in the Skeleton to start simulating and reacting to the physics world.

Optionally, a list of bone names can be passed-in, allowing only the passed-in bones to be simulated.

---

<span id="class_PhysicalBoneSimulator3D_method_physical_bones_stop_simulation"></span>

void **physical_bones_stop_simulation** ( ) [🔗](class_physicalbonesimulator3d.md#class_PhysicalBoneSimulator3D_method_physical_bones_stop_simulation)

Tells the [PhysicalBone3D](class_physicalbone3d.md#class_PhysicalBone3D) nodes in the Skeleton to stop simulating.
