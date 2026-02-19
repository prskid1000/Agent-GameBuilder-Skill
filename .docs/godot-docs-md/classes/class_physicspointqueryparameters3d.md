<span id="class_PhysicsPointQueryParameters3D"></span>

## PhysicsPointQueryParameters3D

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides parameters for [PhysicsDirectSpaceState3D.intersect_point()](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D_method_intersect_point).

### Description

By changing various properties of this object, such as the point position, you can configure the parameters for [PhysicsDirectSpaceState3D.intersect_point()](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D_method_intersect_point).

### Properties


| [bool](class_bool.md#class_bool) | [collide_with_areas](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_collide_with_areas) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [collide_with_bodies](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_collide_with_bodies) | `true` |
| [int](class_int.md#class_int) | [collision_mask](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_collision_mask) | `4294967295` |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [exclude](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_exclude) | `[]` |
| [Vector3](class_vector3.md#class_Vector3) | [position](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_position) | `Vector3(0, 0, 0)` |

---

### Property Descriptions

<span id="class_PhysicsPointQueryParameters3D_property_collide_with_areas"></span>

[bool](class_bool.md#class_bool) **collide_with_areas** = `false` [🔗](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_collide_with_areas)

- void **set_collide_with_areas** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_areas_enabled** ( )

If `true`, the query will take [Area3D](class_area3d.md#class_Area3D) s into account.

---

<span id="class_PhysicsPointQueryParameters3D_property_collide_with_bodies"></span>

[bool](class_bool.md#class_bool) **collide_with_bodies** = `true` [🔗](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_collide_with_bodies)

- void **set_collide_with_bodies** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_bodies_enabled** ( )

If `true`, the query will take [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) s into account.

---

<span id="class_PhysicsPointQueryParameters3D_property_collision_mask"></span>

[int](class_int.md#class_int) **collision_mask** = `4294967295` [🔗](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_PhysicsPointQueryParameters3D_property_exclude"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **exclude** = `[]` [🔗](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_exclude)

- void **set_exclude** ( value: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] )
- [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **get_exclude** ( )

The list of object [RID](class_rid.md#class_RID) s that will be excluded from collisions. Use [CollisionObject3D.get_rid()](class_collisionobject3d.md#class_CollisionObject3D_method_get_rid) to get the [RID](class_rid.md#class_RID) associated with a [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D)-derived node.

 **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.

---

<span id="class_PhysicsPointQueryParameters3D_property_position"></span>

[Vector3](class_vector3.md#class_Vector3) **position** = `Vector3(0, 0, 0)` [🔗](class_physicspointqueryparameters3d.md#class_PhysicsPointQueryParameters3D_property_position)

- void **set_position** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_position** ( )

The position being queried for, in global coordinates.
