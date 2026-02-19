<span id="class_SpringArm3D"></span>

## SpringArm3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A 3D raycast that dynamically moves its children near the collision point.

### Description

**SpringArm3D** casts a ray or a shape along its Z axis and moves all its direct children to the collision point, with an optional margin. This is useful for 3rd person cameras that move closer to the player when inside a tight space (you may need to exclude the player's collider from the **SpringArm3D**'s collision check).

### Tutorials

- [Third-person camera with spring arm](../tutorials/3d/spring_arm.md)

### Properties


| [int](class_int.md#class_int) | [collision_mask](class_springarm3d.md#class_SpringArm3D_property_collision_mask) | `1` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [margin](class_springarm3d.md#class_SpringArm3D_property_margin) | `0.01` |
| [Shape3D](class_shape3d.md#class_Shape3D) | [shape](class_springarm3d.md#class_SpringArm3D_property_shape) |
| [float](class_float.md#class_float) | [spring_length](class_springarm3d.md#class_SpringArm3D_property_spring_length) | `1.0` |

### Methods


| void | [add_excluded_object](class_springarm3d.md#class_SpringArm3D_method_add_excluded_object) ( RID: [RID](class_rid.md#class_RID) ) |
| --- | --- |
| void | [clear_excluded_objects](class_springarm3d.md#class_SpringArm3D_method_clear_excluded_objects) ( ) |
| [float](class_float.md#class_float) | [get_hit_length](class_springarm3d.md#class_SpringArm3D_method_get_hit_length) ( ) |
| [bool](class_bool.md#class_bool) | [remove_excluded_object](class_springarm3d.md#class_SpringArm3D_method_remove_excluded_object) ( RID: [RID](class_rid.md#class_RID) ) |

---

### Property Descriptions

<span id="class_SpringArm3D_property_collision_mask"></span>

[int](class_int.md#class_int) **collision_mask** = `1` [🔗](class_springarm3d.md#class_SpringArm3D_property_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The layers against which the collision check will be done. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_SpringArm3D_property_margin"></span>

[float](class_float.md#class_float) **margin** = `0.01` [🔗](class_springarm3d.md#class_SpringArm3D_property_margin)

- void **set_margin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_margin** ( )

When the collision check is made, a candidate length for the SpringArm3D is given.

The margin is then subtracted to this length and the translation is applied to the child objects of the SpringArm3D.

This margin is useful for when the SpringArm3D has a [Camera3D](class_camera3d.md#class_Camera3D) as a child node: without the margin, the [Camera3D](class_camera3d.md#class_Camera3D) would be placed on the exact point of collision, while with the margin the [Camera3D](class_camera3d.md#class_Camera3D) would be placed close to the point of collision.

---

<span id="class_SpringArm3D_property_shape"></span>

[Shape3D](class_shape3d.md#class_Shape3D) **shape** [🔗](class_springarm3d.md#class_SpringArm3D_property_shape)

- void **set_shape** ( value: [Shape3D](class_shape3d.md#class_Shape3D) )
- [Shape3D](class_shape3d.md#class_Shape3D) **get_shape** ( )

The [Shape3D](class_shape3d.md#class_Shape3D) to use for the SpringArm3D.

When the shape is set, the SpringArm3D will cast the [Shape3D](class_shape3d.md#class_Shape3D) on its z axis instead of performing a ray cast.

---

<span id="class_SpringArm3D_property_spring_length"></span>

[float](class_float.md#class_float) **spring_length** = `1.0` [🔗](class_springarm3d.md#class_SpringArm3D_property_spring_length)

- void **set_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_length** ( )

The maximum extent of the SpringArm3D. This is used as a length for both the ray and the shape cast used internally to calculate the desired position of the SpringArm3D's child nodes.

To know more about how to perform a shape cast or a ray cast, please consult the [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) documentation.

---

### Method Descriptions

<span id="class_SpringArm3D_method_add_excluded_object"></span>

void **add_excluded_object** ( RID: [RID](class_rid.md#class_RID) ) [🔗](class_springarm3d.md#class_SpringArm3D_method_add_excluded_object)

Adds the [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) object with the given [RID](class_rid.md#class_RID) to the list of [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) objects excluded from the collision check.

---

<span id="class_SpringArm3D_method_clear_excluded_objects"></span>

void **clear_excluded_objects** ( ) [🔗](class_springarm3d.md#class_SpringArm3D_method_clear_excluded_objects)

Clears the list of [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) objects excluded from the collision check.

---

<span id="class_SpringArm3D_method_get_hit_length"></span>

[float](class_float.md#class_float) **get_hit_length** ( ) [🔗](class_springarm3d.md#class_SpringArm3D_method_get_hit_length)

Returns the spring arm's current length.

---

<span id="class_SpringArm3D_method_remove_excluded_object"></span>

[bool](class_bool.md#class_bool) **remove_excluded_object** ( RID: [RID](class_rid.md#class_RID) ) [🔗](class_springarm3d.md#class_SpringArm3D_method_remove_excluded_object)

Removes the given [RID](class_rid.md#class_RID) from the list of [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) objects excluded from the collision check.
