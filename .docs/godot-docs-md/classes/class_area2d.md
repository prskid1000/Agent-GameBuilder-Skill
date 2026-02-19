.. meta::
	:keywords: trigger

<span id="class_Area2D"></span>

## Area2D

**Inherits:** [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A region of 2D space that detects other [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) s entering or exiting it.

### Description

**Area2D** is a region of 2D space defined by one or multiple [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) or [CollisionPolygon2D](class_collisionpolygon2d.md#class_CollisionPolygon2D) child nodes. It detects when other [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) s enter or exit it, and it also keeps track of which collision objects haven't exited it yet (i.e. which one are overlapping it).

This node can also locally alter or override physics parameters (gravity, damping) and route audio to custom audio buses.

 **Note:** Areas and bodies created with [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D) might not interact as expected with **Area2D** s, and might not emit signals or track objects correctly.

### Tutorials

- [Using Area2D](../tutorials/physics/using_area_2d.md)

- 2D Dodge The Creeps Demo

- 2D Pong Demo

- 2D Platformer Demo

### Properties


| [float](class_float.md#class_float) | [angular_damp](class_area2d.md#class_Area2D_property_angular_damp) | `1.0` |
| --- | --- | --- |
| [SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) | [angular_damp_space_override](class_area2d.md#class_Area2D_property_angular_damp_space_override) | `0` |
| [StringName](class_stringname.md#class_StringName) | [audio_bus_name](class_area2d.md#class_Area2D_property_audio_bus_name) | `&"Master"` |
| [bool](class_bool.md#class_bool) | [audio_bus_override](class_area2d.md#class_Area2D_property_audio_bus_override) | `false` |
| [float](class_float.md#class_float) | [gravity](class_area2d.md#class_Area2D_property_gravity) | `980.0` |
| [Vector2](class_vector2.md#class_Vector2) | [gravity_direction](class_area2d.md#class_Area2D_property_gravity_direction) | `Vector2(0, 1)` |
| [bool](class_bool.md#class_bool) | [gravity_point](class_area2d.md#class_Area2D_property_gravity_point) | `false` |
| [Vector2](class_vector2.md#class_Vector2) | [gravity_point_center](class_area2d.md#class_Area2D_property_gravity_point_center) | `Vector2(0, 1)` |
| [float](class_float.md#class_float) | [gravity_point_unit_distance](class_area2d.md#class_Area2D_property_gravity_point_unit_distance) | `0.0` |
| [SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) | [gravity_space_override](class_area2d.md#class_Area2D_property_gravity_space_override) | `0` |
| [float](class_float.md#class_float) | [linear_damp](class_area2d.md#class_Area2D_property_linear_damp) | `0.1` |
| [SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) | [linear_damp_space_override](class_area2d.md#class_Area2D_property_linear_damp_space_override) | `0` |
| [bool](class_bool.md#class_bool) | [monitorable](class_area2d.md#class_Area2D_property_monitorable) | `true` |
| [bool](class_bool.md#class_bool) | [monitoring](class_area2d.md#class_Area2D_property_monitoring) | `true` |
| [int](class_int.md#class_int) | [priority](class_area2d.md#class_Area2D_property_priority) | `0` |

### Methods


| [Array](class_array.md#class_Array)\[[Area2D](class_area2d.md#class_Area2D)\] | [get_overlapping_areas](class_area2d.md#class_Area2D_method_get_overlapping_areas) ( ) const |
| --- | --- |
| [Array](class_array.md#class_Array)\[[Node2D](class_node2d.md#class_Node2D)\] | [get_overlapping_bodies](class_area2d.md#class_Area2D_method_get_overlapping_bodies) ( ) const |
| [bool](class_bool.md#class_bool) | [has_overlapping_areas](class_area2d.md#class_Area2D_method_has_overlapping_areas) ( ) const |
| [bool](class_bool.md#class_bool) | [has_overlapping_bodies](class_area2d.md#class_Area2D_method_has_overlapping_bodies) ( ) const |
| [bool](class_bool.md#class_bool) | [overlaps_area](class_area2d.md#class_Area2D_method_overlaps_area) ( area: [Node](class_node.md#class_Node) ) const |
| [bool](class_bool.md#class_bool) | [overlaps_body](class_area2d.md#class_Area2D_method_overlaps_body) ( body: [Node](class_node.md#class_Node) ) const |

---

### Signals

<span id="class_Area2D_signal_area_entered"></span>

**area_entered** ( area: [Area2D](class_area2d.md#class_Area2D) ) [🔗](class_area2d.md#class_Area2D_signal_area_entered)

Emitted when the received `area` enters this area. Requires [monitoring](class_area2d.md#class_Area2D_property_monitoring) to be set to `true`.

---

<span id="class_Area2D_signal_area_exited"></span>

**area_exited** ( area: [Area2D](class_area2d.md#class_Area2D) ) [🔗](class_area2d.md#class_Area2D_signal_area_exited)

Emitted when the received `area` exits this area. Requires [monitoring](class_area2d.md#class_Area2D_property_monitoring) to be set to `true`.

---

<span id="class_Area2D_signal_area_shape_entered"></span>

**area_shape_entered** ( area_rid: [RID](class_rid.md#class_RID), area: [Area2D](class_area2d.md#class_Area2D), area_shape_index: [int](class_int.md#class_int), local_shape_index: [int](class_int.md#class_int) ) [🔗](class_area2d.md#class_Area2D_signal_area_shape_entered)

Emitted when a [Shape2D](class_shape2d.md#class_Shape2D) of the received `area` enters a shape of this area. Requires [monitoring](class_area2d.md#class_Area2D_property_monitoring) to be set to `true`.

 `local_shape_index` and `area_shape_index` contain indices of the interacting shapes from this area and the other area, respectively. `area_rid` contains the [RID](class_rid.md#class_RID) of the other area. These values can be used with the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D).

 **Example:** Get the [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) node from the shape index:

.. tabs::

```
```

    var other_shape_owner = area.shape_find_owner(area_shape_index)
    var other_shape_node = area.shape_owner_get_owner(other_shape_owner)

    var local_shape_owner = shape_find_owner(local_shape_index)
    var local_shape_node = shape_owner_get_owner(local_shape_owner)

---

<span id="class_Area2D_signal_area_shape_exited"></span>

**area_shape_exited** ( area_rid: [RID](class_rid.md#class_RID), area: [Area2D](class_area2d.md#class_Area2D), area_shape_index: [int](class_int.md#class_int), local_shape_index: [int](class_int.md#class_int) ) [🔗](class_area2d.md#class_Area2D_signal_area_shape_exited)

Emitted when a [Shape2D](class_shape2d.md#class_Shape2D) of the received `area` exits a shape of this area. Requires [monitoring](class_area2d.md#class_Area2D_property_monitoring) to be set to `true`.

See also [area_shape_entered](class_area2d.md#class_Area2D_signal_area_shape_entered).

---

<span id="class_Area2D_signal_body_entered"></span>

**body_entered** ( body: [Node2D](class_node2d.md#class_Node2D) ) [🔗](class_area2d.md#class_Area2D_signal_body_entered)

Emitted when the received `body` enters this area. `body` can be a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or a [TileMap](class_tilemap.md#class_TileMap). [TileMap](class_tilemap.md#class_TileMap) s are detected if their [TileSet](class_tileset.md#class_TileSet) has collision shapes configured. Requires [monitoring](class_area2d.md#class_Area2D_property_monitoring) to be set to `true`.

---

<span id="class_Area2D_signal_body_exited"></span>

**body_exited** ( body: [Node2D](class_node2d.md#class_Node2D) ) [🔗](class_area2d.md#class_Area2D_signal_body_exited)

Emitted when the received `body` exits this area. `body` can be a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or a [TileMap](class_tilemap.md#class_TileMap). [TileMap](class_tilemap.md#class_TileMap) s are detected if their [TileSet](class_tileset.md#class_TileSet) has collision shapes configured. Requires [monitoring](class_area2d.md#class_Area2D_property_monitoring) to be set to `true`.

---

<span id="class_Area2D_signal_body_shape_entered"></span>

**body_shape_entered** ( body_rid: [RID](class_rid.md#class_RID), body: [Node2D](class_node2d.md#class_Node2D), body_shape_index: [int](class_int.md#class_int), local_shape_index: [int](class_int.md#class_int) ) [🔗](class_area2d.md#class_Area2D_signal_body_shape_entered)

Emitted when a [Shape2D](class_shape2d.md#class_Shape2D) of the received `body` enters a shape of this area. `body` can be a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or a [TileMap](class_tilemap.md#class_TileMap). [TileMap](class_tilemap.md#class_TileMap) s are detected if their [TileSet](class_tileset.md#class_TileSet) has collision shapes configured. Requires [monitoring](class_area2d.md#class_Area2D_property_monitoring) to be set to `true`.

 `local_shape_index` and `body_shape_index` contain indices of the interacting shapes from this area and the interacting body, respectively. `body_rid` contains the [RID](class_rid.md#class_RID) of the body. These values can be used with the [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D).

 **Example:** Get the [CollisionShape2D](class_collisionshape2d.md#class_CollisionShape2D) node from the shape index:

.. tabs::

```
```

    var body_shape_owner = body.shape_find_owner(body_shape_index)
    var body_shape_node = body.shape_owner_get_owner(body_shape_owner)

    var local_shape_owner = shape_find_owner(local_shape_index)
    var local_shape_node = shape_owner_get_owner(local_shape_owner)

---

<span id="class_Area2D_signal_body_shape_exited"></span>

**body_shape_exited** ( body_rid: [RID](class_rid.md#class_RID), body: [Node2D](class_node2d.md#class_Node2D), body_shape_index: [int](class_int.md#class_int), local_shape_index: [int](class_int.md#class_int) ) [🔗](class_area2d.md#class_Area2D_signal_body_shape_exited)

Emitted when a [Shape2D](class_shape2d.md#class_Shape2D) of the received `body` exits a shape of this area. `body` can be a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or a [TileMap](class_tilemap.md#class_TileMap). [TileMap](class_tilemap.md#class_TileMap) s are detected if their [TileSet](class_tileset.md#class_TileSet) has collision shapes configured. Requires [monitoring](class_area2d.md#class_Area2D_property_monitoring) to be set to `true`.

See also [body_shape_entered](class_area2d.md#class_Area2D_signal_body_shape_entered).

---

### Enumerations

<span id="enum_Area2D_SpaceOverride"></span>

enum **SpaceOverride**: [🔗](class_area2d.md#enum_Area2D_SpaceOverride)

<span id="class_Area2D_constant_SPACE_OVERRIDE_DISABLED"></span>

[SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **SPACE_OVERRIDE_DISABLED** = `0`

This area does not affect gravity/damping.

<span id="class_Area2D_constant_SPACE_OVERRIDE_COMBINE"></span>

[SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **SPACE_OVERRIDE_COMBINE** = `1`

This area adds its gravity/damping values to whatever has been calculated so far (in [priority](class_area2d.md#class_Area2D_property_priority) order).

<span id="class_Area2D_constant_SPACE_OVERRIDE_COMBINE_REPLACE"></span>

[SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **SPACE_OVERRIDE_COMBINE_REPLACE** = `2`

This area adds its gravity/damping values to whatever has been calculated so far (in [priority](class_area2d.md#class_Area2D_property_priority) order), ignoring any lower priority areas.

<span id="class_Area2D_constant_SPACE_OVERRIDE_REPLACE"></span>

[SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **SPACE_OVERRIDE_REPLACE** = `3`

This area replaces any gravity/damping, even the defaults, ignoring any lower priority areas.

<span id="class_Area2D_constant_SPACE_OVERRIDE_REPLACE_COMBINE"></span>

[SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **SPACE_OVERRIDE_REPLACE_COMBINE** = `4`

This area replaces any gravity/damping calculated so far (in [priority](class_area2d.md#class_Area2D_property_priority) order), but keeps calculating the rest of the areas.

---

### Property Descriptions

<span id="class_Area2D_property_angular_damp"></span>

[float](class_float.md#class_float) **angular_damp** = `1.0` [🔗](class_area2d.md#class_Area2D_property_angular_damp)

- void **set_angular_damp** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_angular_damp** ( )

The rate at which objects stop spinning in this area. Represents the angular velocity lost per second.

See ProjectSettings.physics/2d/default_angular_damp for more details about damping.

---

<span id="class_Area2D_property_angular_damp_space_override"></span>

[SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **angular_damp_space_override** = `0` [🔗](class_area2d.md#class_Area2D_property_angular_damp_space_override)

- void **set_angular_damp_space_override_mode** ( value: [SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) )
- [SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **get_angular_damp_space_override_mode** ( )

Override mode for angular damping calculations within this area.

---

<span id="class_Area2D_property_audio_bus_name"></span>

[StringName](class_stringname.md#class_StringName) **audio_bus_name** = `&"Master"` [🔗](class_area2d.md#class_Area2D_property_audio_bus_name)

- void **set_audio_bus_name** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_audio_bus_name** ( )

The name of the area's audio bus.

---

<span id="class_Area2D_property_audio_bus_override"></span>

[bool](class_bool.md#class_bool) **audio_bus_override** = `false` [🔗](class_area2d.md#class_Area2D_property_audio_bus_override)

- void **set_audio_bus_override** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_overriding_audio_bus** ( )

If `true`, the area's audio bus overrides the default audio bus.

---

<span id="class_Area2D_property_gravity"></span>

[float](class_float.md#class_float) **gravity** = `980.0` [🔗](class_area2d.md#class_Area2D_property_gravity)

- void **set_gravity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_gravity** ( )

The area's gravity intensity (in pixels per second squared). This value multiplies the gravity direction. This is useful to alter the force of gravity without altering its direction.

---

<span id="class_Area2D_property_gravity_direction"></span>

[Vector2](class_vector2.md#class_Vector2) **gravity_direction** = `Vector2(0, 1)` [🔗](class_area2d.md#class_Area2D_property_gravity_direction)

- void **set_gravity_direction** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_gravity_direction** ( )

The area's gravity vector (not normalized).

---

<span id="class_Area2D_property_gravity_point"></span>

[bool](class_bool.md#class_bool) **gravity_point** = `false` [🔗](class_area2d.md#class_Area2D_property_gravity_point)

- void **set_gravity_is_point** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_gravity_a_point** ( )

If `true`, gravity is calculated from a point (set via [gravity_point_center](class_area2d.md#class_Area2D_property_gravity_point_center)). See also [gravity_space_override](class_area2d.md#class_Area2D_property_gravity_space_override).

---

<span id="class_Area2D_property_gravity_point_center"></span>

[Vector2](class_vector2.md#class_Vector2) **gravity_point_center** = `Vector2(0, 1)` [🔗](class_area2d.md#class_Area2D_property_gravity_point_center)

- void **set_gravity_point_center** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_gravity_point_center** ( )

If gravity is a point (see [gravity_point](class_area2d.md#class_Area2D_property_gravity_point)), this will be the point of attraction.

---

<span id="class_Area2D_property_gravity_point_unit_distance"></span>

[float](class_float.md#class_float) **gravity_point_unit_distance** = `0.0` [🔗](class_area2d.md#class_Area2D_property_gravity_point_unit_distance)

- void **set_gravity_point_unit_distance** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_gravity_point_unit_distance** ( )

The distance at which the gravity strength is equal to [gravity](class_area2d.md#class_Area2D_property_gravity). For example, on a planet 100 pixels in radius with a surface gravity of 4.0 px/s², set the [gravity](class_area2d.md#class_Area2D_property_gravity) to 4.0 and the unit distance to 100.0. The gravity will have falloff according to the inverse square law, so in the example, at 200 pixels from the center the gravity will be 1.0 px/s² (twice the distance, 1/4th the gravity), at 50 pixels it will be 16.0 px/s² (half the distance, 4x the gravity), and so on.

The above is true only when the unit distance is a positive number. When this is set to 0.0, the gravity will be constant regardless of distance.

---

<span id="class_Area2D_property_gravity_space_override"></span>

[SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **gravity_space_override** = `0` [🔗](class_area2d.md#class_Area2D_property_gravity_space_override)

- void **set_gravity_space_override_mode** ( value: [SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) )
- [SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **get_gravity_space_override_mode** ( )

Override mode for gravity calculations within this area.

---

<span id="class_Area2D_property_linear_damp"></span>

[float](class_float.md#class_float) **linear_damp** = `0.1` [🔗](class_area2d.md#class_Area2D_property_linear_damp)

- void **set_linear_damp** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_linear_damp** ( )

The rate at which objects stop moving in this area. Represents the linear velocity lost per second.

See ProjectSettings.physics/2d/default_linear_damp for more details about damping.

---

<span id="class_Area2D_property_linear_damp_space_override"></span>

[SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **linear_damp_space_override** = `0` [🔗](class_area2d.md#class_Area2D_property_linear_damp_space_override)

- void **set_linear_damp_space_override_mode** ( value: [SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) )
- [SpaceOverride](class_area2d.md#enum_Area2D_SpaceOverride) **get_linear_damp_space_override_mode** ( )

Override mode for linear damping calculations within this area.

---

<span id="class_Area2D_property_monitorable"></span>

[bool](class_bool.md#class_bool) **monitorable** = `true` [🔗](class_area2d.md#class_Area2D_property_monitorable)

- void **set_monitorable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_monitorable** ( )

If `true`, other monitoring areas can detect this area.

---

<span id="class_Area2D_property_monitoring"></span>

[bool](class_bool.md#class_bool) **monitoring** = `true` [🔗](class_area2d.md#class_Area2D_property_monitoring)

- void **set_monitoring** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_monitoring** ( )

If `true`, the area detects bodies or areas entering and exiting it.

---

<span id="class_Area2D_property_priority"></span>

[int](class_int.md#class_int) **priority** = `0` [🔗](class_area2d.md#class_Area2D_property_priority)

- void **set_priority** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_priority** ( )

The area's priority. Higher priority areas are processed first. The [World2D](class_world2d.md#class_World2D)'s physics is always processed last, after all areas.

---

### Method Descriptions

<span id="class_Area2D_method_get_overlapping_areas"></span>

[Array](class_array.md#class_Array)\[[Area2D](class_area2d.md#class_Area2D)\] **get_overlapping_areas** ( ) *const* [🔗](class_area2d.md#class_Area2D_method_get_overlapping_areas)

Returns a list of intersecting **Area2D** s. The overlapping area's [CollisionObject2D.collision_layer](class_collisionobject2d.md#class_CollisionObject2D_property_collision_layer) must be part of this area's [CollisionObject2D.collision_mask](class_collisionobject2d.md#class_CollisionObject2D_property_collision_mask) in order to be detected.

For performance reasons (collisions are all processed at the same time) this list is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.

---

<span id="class_Area2D_method_get_overlapping_bodies"></span>

[Array](class_array.md#class_Array)\[[Node2D](class_node2d.md#class_Node2D)\] **get_overlapping_bodies** ( ) *const* [🔗](class_area2d.md#class_Area2D_method_get_overlapping_bodies)

Returns a list of intersecting [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) s and [TileMap](class_tilemap.md#class_TileMap) s. The overlapping body's [CollisionObject2D.collision_layer](class_collisionobject2d.md#class_CollisionObject2D_property_collision_layer) must be part of this area's [CollisionObject2D.collision_mask](class_collisionobject2d.md#class_CollisionObject2D_property_collision_mask) in order to be detected.

For performance reasons (collisions are all processed at the same time) this list is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.

---

<span id="class_Area2D_method_has_overlapping_areas"></span>

[bool](class_bool.md#class_bool) **has_overlapping_areas** ( ) *const* [🔗](class_area2d.md#class_Area2D_method_has_overlapping_areas)

Returns `true` if intersecting any **Area2D** s, otherwise returns `false`. The overlapping area's [CollisionObject2D.collision_layer](class_collisionobject2d.md#class_CollisionObject2D_property_collision_layer) must be part of this area's [CollisionObject2D.collision_mask](class_collisionobject2d.md#class_CollisionObject2D_property_collision_mask) in order to be detected.

For performance reasons (collisions are all processed at the same time) the list of overlapping areas is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.

---

<span id="class_Area2D_method_has_overlapping_bodies"></span>

[bool](class_bool.md#class_bool) **has_overlapping_bodies** ( ) *const* [🔗](class_area2d.md#class_Area2D_method_has_overlapping_bodies)

Returns `true` if intersecting any [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) s or [TileMap](class_tilemap.md#class_TileMap) s, otherwise returns `false`. The overlapping body's [CollisionObject2D.collision_layer](class_collisionobject2d.md#class_CollisionObject2D_property_collision_layer) must be part of this area's [CollisionObject2D.collision_mask](class_collisionobject2d.md#class_CollisionObject2D_property_collision_mask) in order to be detected.

For performance reasons (collisions are all processed at the same time) the list of overlapping bodies is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.

---

<span id="class_Area2D_method_overlaps_area"></span>

[bool](class_bool.md#class_bool) **overlaps_area** ( area: [Node](class_node.md#class_Node) ) *const* [🔗](class_area2d.md#class_Area2D_method_overlaps_area)

Returns `true` if the given **Area2D** intersects or overlaps this **Area2D**, `false` otherwise.

 **Note:** The result of this test is not immediate after moving objects. For performance, the list of overlaps is updated once per frame and before the physics step. Consider using signals instead.

---

<span id="class_Area2D_method_overlaps_body"></span>

[bool](class_bool.md#class_bool) **overlaps_body** ( body: [Node](class_node.md#class_Node) ) *const* [🔗](class_area2d.md#class_Area2D_method_overlaps_body)

Returns `true` if the given physics body intersects or overlaps this **Area2D**, `false` otherwise.

 **Note:** The result of this test is not immediate after moving objects. For performance, list of overlaps is updated once per frame and before the physics step. Consider using signals instead.

The `body` argument can either be a [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) or a [TileMap](class_tilemap.md#class_TileMap) instance. While TileMaps are not physics bodies themselves, they register their tiles with collision shapes as a virtual physics body.
