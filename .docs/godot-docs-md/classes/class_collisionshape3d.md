<span id="class_CollisionShape3D"></span>

## CollisionShape3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node that provides a [Shape3D](class_shape3d.md#class_Shape3D) to a [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D) parent.

### Description

A node that provides a [Shape3D](class_shape3d.md#class_Shape3D) to a [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D) parent and allows it to be edited. This can give a detection shape to an [Area3D](class_area3d.md#class_Area3D) or turn a [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) into a solid object.

 **Warning:** A non-uniformly scaled **CollisionShape3D** will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its [shape](class_collisionshape3d.md#class_CollisionShape3D_property_shape) resource instead.

### Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

- 3D Kinematic Character Demo

- 3D Platformer Demo

- Third Person Shooter (TPS) Demo

### Properties


| [Color](class_color.md#class_Color) | [debug_color](class_collisionshape3d.md#class_CollisionShape3D_property_debug_color) | `Color(0, 0, 0, 0)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [debug_fill](class_collisionshape3d.md#class_CollisionShape3D_property_debug_fill) | `true` |
| [bool](class_bool.md#class_bool) | [disabled](class_collisionshape3d.md#class_CollisionShape3D_property_disabled) | `false` |
| [Shape3D](class_shape3d.md#class_Shape3D) | [shape](class_collisionshape3d.md#class_CollisionShape3D_property_shape) |

### Methods


| void | [make_convex_from_siblings](class_collisionshape3d.md#class_CollisionShape3D_method_make_convex_from_siblings) ( ) |
| --- | --- |
| void | [resource_changed](class_collisionshape3d.md#class_CollisionShape3D_method_resource_changed) ( resource: [Resource](class_resource.md#class_Resource) ) |

---

### Property Descriptions

<span id="class_CollisionShape3D_property_debug_color"></span>

[Color](class_color.md#class_Color) **debug_color** = `Color(0, 0, 0, 0)` [🔗](class_collisionshape3d.md#class_CollisionShape3D_property_debug_color)

- void **set_debug_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_debug_color** ( )

The collision shape color that is displayed in the editor, or in the running project if **Debug > Visible Collision Shapes** is checked at the top of the editor.

 **Note:** The default value is ProjectSettings.debug/shapes/collision/shape_color. The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.

---

<span id="class_CollisionShape3D_property_debug_fill"></span>

[bool](class_bool.md#class_bool) **debug_fill** = `true` [🔗](class_collisionshape3d.md#class_CollisionShape3D_property_debug_fill)

- void **set_enable_debug_fill** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_debug_fill** ( )

If `true`, when the shape is displayed, it will show a solid fill color in addition to its wireframe.

---

<span id="class_CollisionShape3D_property_disabled"></span>

[bool](class_bool.md#class_bool) **disabled** = `false` [🔗](class_collisionshape3d.md#class_CollisionShape3D_property_disabled)

- void **set_disabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_disabled** ( )

A disabled collision shape has no effect in the world. This property should be changed with [Object.set_deferred()](class_object.md#class_Object_method_set_deferred).

---

<span id="class_CollisionShape3D_property_shape"></span>

[Shape3D](class_shape3d.md#class_Shape3D) **shape** [🔗](class_collisionshape3d.md#class_CollisionShape3D_property_shape)

- void **set_shape** ( value: [Shape3D](class_shape3d.md#class_Shape3D) )
- [Shape3D](class_shape3d.md#class_Shape3D) **get_shape** ( )

The actual shape owned by this collision shape.

---

### Method Descriptions

<span id="class_CollisionShape3D_method_make_convex_from_siblings"></span>

void **make_convex_from_siblings** ( ) [🔗](class_collisionshape3d.md#class_CollisionShape3D_method_make_convex_from_siblings)

Sets the collision shape's shape to the addition of all its convexed [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) siblings geometry.

---

<span id="class_CollisionShape3D_method_resource_changed"></span>

void **resource_changed** ( resource: [Resource](class_resource.md#class_Resource) ) [🔗](class_collisionshape3d.md#class_CollisionShape3D_method_resource_changed)

**Deprecated:** Use [Resource.changed](class_resource.md#class_Resource_signal_changed) instead.

This method does nothing.
