<span id="class_SpringBoneCollision3D"></span>

## SpringBoneCollision3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [SpringBoneCollisionCapsule3D](class_springbonecollisioncapsule3d.md#class_SpringBoneCollisionCapsule3D), [SpringBoneCollisionPlane3D](class_springbonecollisionplane3d.md#class_SpringBoneCollisionPlane3D), [SpringBoneCollisionSphere3D](class_springbonecollisionsphere3d.md#class_SpringBoneCollisionSphere3D)

A base class of the collision that interacts with [SpringBoneSimulator3D](class_springbonesimulator3d.md#class_SpringBoneSimulator3D).

### Description

A collision can be a child of [SpringBoneSimulator3D](class_springbonesimulator3d.md#class_SpringBoneSimulator3D). If it is not a child of [SpringBoneSimulator3D](class_springbonesimulator3d.md#class_SpringBoneSimulator3D), it has no effect.

The colliding and sliding are done in the [SpringBoneSimulator3D](class_springbonesimulator3d.md#class_SpringBoneSimulator3D)'s modification process in order of its collision list which is set by [SpringBoneSimulator3D.set_collision_path()](class_springbonesimulator3d.md#class_SpringBoneSimulator3D_method_set_collision_path). If [SpringBoneSimulator3D.are_all_child_collisions_enabled()](class_springbonesimulator3d.md#class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled) is `true`, the order matches [SceneTree](class_scenetree.md#class_SceneTree).

If [bone](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_bone) is set, it synchronizes with the bone pose of the ancestor [Skeleton3D](class_skeleton3d.md#class_Skeleton3D), which is done in before the [SpringBoneSimulator3D](class_springbonesimulator3d.md#class_SpringBoneSimulator3D)'s modification process as the pre-process.

 **Warning:** A scaled **SpringBoneCollision3D** will likely not behave as expected. Make sure that the parent [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) and its bones are not scaled.

### Properties


| [int](class_int.md#class_int) | [bone](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_bone) | `-1` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [bone_name](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_bone_name) | `""` |
| [Vector3](class_vector3.md#class_Vector3) | [position_offset](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_position_offset) |
| [Quaternion](class_quaternion.md#class_Quaternion) | [rotation_offset](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_rotation_offset) |

### Methods


| [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) | [get_skeleton](class_springbonecollision3d.md#class_SpringBoneCollision3D_method_get_skeleton) ( ) const |
| --- | --- |

---

### Property Descriptions

<span id="class_SpringBoneCollision3D_property_bone"></span>

[int](class_int.md#class_int) **bone** = `-1` [🔗](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_bone)

- void **set_bone** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bone** ( )

The index of the attached bone.

---

<span id="class_SpringBoneCollision3D_property_bone_name"></span>

[String](class_string.md#class_String) **bone_name** = `""` [🔗](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_bone_name)

- void **set_bone_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_bone_name** ( )

The name of the attached bone.

---

<span id="class_SpringBoneCollision3D_property_position_offset"></span>

[Vector3](class_vector3.md#class_Vector3) **position_offset** [🔗](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_position_offset)

- void **set_position_offset** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_position_offset** ( )

The offset of the position from [Skeleton3D](class_skeleton3d.md#class_Skeleton3D)'s [bone](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_bone) pose position.

---

<span id="class_SpringBoneCollision3D_property_rotation_offset"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **rotation_offset** [🔗](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_rotation_offset)

- void **set_rotation_offset** ( value: [Quaternion](class_quaternion.md#class_Quaternion) )
- [Quaternion](class_quaternion.md#class_Quaternion) **get_rotation_offset** ( )

The offset of the rotation from [Skeleton3D](class_skeleton3d.md#class_Skeleton3D)'s [bone](class_springbonecollision3d.md#class_SpringBoneCollision3D_property_bone) pose rotation.

---

### Method Descriptions

<span id="class_SpringBoneCollision3D_method_get_skeleton"></span>

[Skeleton3D](class_skeleton3d.md#class_Skeleton3D) **get_skeleton** ( ) *const* [🔗](class_springbonecollision3d.md#class_SpringBoneCollision3D_method_get_skeleton)

Get parent [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) node of the parent [SpringBoneSimulator3D](class_springbonesimulator3d.md#class_SpringBoneSimulator3D) if found.
