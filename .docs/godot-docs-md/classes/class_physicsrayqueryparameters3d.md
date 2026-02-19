<span id="class_PhysicsRayQueryParameters3D"></span>

## PhysicsRayQueryParameters3D

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides parameters for [PhysicsDirectSpaceState3D.intersect_ray()](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D_method_intersect_ray).

### Description

By changing various properties of this object, such as the ray position, you can configure the parameters for [PhysicsDirectSpaceState3D.intersect_ray()](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D_method_intersect_ray).

### Properties


| [bool](class_bool.md#class_bool) | [collide_with_areas](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_collide_with_areas) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [collide_with_bodies](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_collide_with_bodies) | `true` |
| [int](class_int.md#class_int) | [collision_mask](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_collision_mask) | `4294967295` |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [exclude](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_exclude) | `[]` |
| [Vector3](class_vector3.md#class_Vector3) | [from](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_from) | `Vector3(0, 0, 0)` |
| [bool](class_bool.md#class_bool) | [hit_back_faces](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_hit_back_faces) | `true` |
| [bool](class_bool.md#class_bool) | [hit_from_inside](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_hit_from_inside) | `false` |
| [Vector3](class_vector3.md#class_Vector3) | [to](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_to) | `Vector3(0, 0, 0)` |

### Methods


| [PhysicsRayQueryParameters3D](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D) | [create](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_method_create) ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), collision_mask: [int](class_int.md#class_int) = 4294967295, exclude: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] = [] ) static |
| --- | --- |

---

### Property Descriptions

<span id="class_PhysicsRayQueryParameters3D_property_collide_with_areas"></span>

[bool](class_bool.md#class_bool) **collide_with_areas** = `false` [🔗](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_collide_with_areas)

- void **set_collide_with_areas** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_areas_enabled** ( )

If `true`, the query will take [Area3D](class_area3d.md#class_Area3D) s into account.

---

<span id="class_PhysicsRayQueryParameters3D_property_collide_with_bodies"></span>

[bool](class_bool.md#class_bool) **collide_with_bodies** = `true` [🔗](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_collide_with_bodies)

- void **set_collide_with_bodies** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_collide_with_bodies_enabled** ( )

If `true`, the query will take [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) s into account.

---

<span id="class_PhysicsRayQueryParameters3D_property_collision_mask"></span>

[int](class_int.md#class_int) **collision_mask** = `4294967295` [🔗](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_PhysicsRayQueryParameters3D_property_exclude"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **exclude** = `[]` [🔗](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_exclude)

- void **set_exclude** ( value: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] )
- [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **get_exclude** ( )

The list of object [RID](class_rid.md#class_RID) s that will be excluded from collisions. Use [CollisionObject3D.get_rid()](class_collisionobject3d.md#class_CollisionObject3D_method_get_rid) to get the [RID](class_rid.md#class_RID) associated with a [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D)-derived node.

 **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.

---

<span id="class_PhysicsRayQueryParameters3D_property_from"></span>

[Vector3](class_vector3.md#class_Vector3) **from** = `Vector3(0, 0, 0)` [🔗](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_from)

- void **set_from** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_from** ( )

The starting point of the ray being queried for, in global coordinates.

---

<span id="class_PhysicsRayQueryParameters3D_property_hit_back_faces"></span>

[bool](class_bool.md#class_bool) **hit_back_faces** = `true` [🔗](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_hit_back_faces)

- void **set_hit_back_faces** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_hit_back_faces_enabled** ( )

If `true`, the query will hit back faces with concave polygon shapes with back face enabled or heightmap shapes.

---

<span id="class_PhysicsRayQueryParameters3D_property_hit_from_inside"></span>

[bool](class_bool.md#class_bool) **hit_from_inside** = `false` [🔗](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_hit_from_inside)

- void **set_hit_from_inside** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_hit_from_inside_enabled** ( )

If `true`, the query will detect a hit when starting inside shapes. In this case the collision normal will be `Vector3(0, 0, 0)`. Does not affect concave polygon shapes or heightmap shapes.

---

<span id="class_PhysicsRayQueryParameters3D_property_to"></span>

[Vector3](class_vector3.md#class_Vector3) **to** = `Vector3(0, 0, 0)` [🔗](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_property_to)

- void **set_to** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_to** ( )

The ending point of the ray being queried for, in global coordinates.

---

### Method Descriptions

<span id="class_PhysicsRayQueryParameters3D_method_create"></span>

[PhysicsRayQueryParameters3D](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D) **create** ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), collision_mask: [int](class_int.md#class_int) = 4294967295, exclude: [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] = [] ) *static* [🔗](class_physicsrayqueryparameters3d.md#class_PhysicsRayQueryParameters3D_method_create)

Returns a new, pre-configured **PhysicsRayQueryParameters3D** object. Use it to quickly create query parameters using the most common options.

::

    var query = PhysicsRayQueryParameters3D.create(position, position + Vector3(0, -10, 0))
    var collision = get_world_3d().direct_space_state.intersect_ray(query)
