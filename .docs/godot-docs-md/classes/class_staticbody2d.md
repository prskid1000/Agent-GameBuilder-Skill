<span id="class_StaticBody2D"></span>

## StaticBody2D

**Inherits:** [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) **<** [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AnimatableBody2D](class_animatablebody2d.md#class_AnimatableBody2D)

A 2D physics body that can't be moved by external forces. When moved manually, it doesn't affect other bodies in its path.

### Description

A static 2D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, [AnimationMixer](class_animationmixer.md#class_AnimationMixer) s (with [AnimationMixer.callback_mode_process](class_animationmixer.md#class_AnimationMixer_property_callback_mode_process) set to [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS](class_animationmixer.md#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS)), and [RemoteTransform2D](class_remotetransform2d.md#class_RemoteTransform2D).

When **StaticBody2D** is moved, it is teleported to its new position without affecting other physics bodies in its path. If this is not desired, use [AnimatableBody2D](class_animatablebody2d.md#class_AnimatableBody2D) instead.

 **StaticBody2D** is useful for completely static objects like floors and walls, as well as moving surfaces like conveyor belts and circular revolving platforms (by using [constant_linear_velocity](class_staticbody2d.md#class_StaticBody2D_property_constant_linear_velocity) and [constant_angular_velocity](class_staticbody2d.md#class_StaticBody2D_property_constant_angular_velocity)).

### Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)

### Properties


| [float](class_float.md#class_float) | [constant_angular_velocity](class_staticbody2d.md#class_StaticBody2D_property_constant_angular_velocity) | `0.0` |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [constant_linear_velocity](class_staticbody2d.md#class_StaticBody2D_property_constant_linear_velocity) | `Vector2(0, 0)` |
| [PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) | [physics_material_override](class_staticbody2d.md#class_StaticBody2D_property_physics_material_override) |

---

### Property Descriptions

<span id="class_StaticBody2D_property_constant_angular_velocity"></span>

[float](class_float.md#class_float) **constant_angular_velocity** = `0.0` [🔗](class_staticbody2d.md#class_StaticBody2D_property_constant_angular_velocity)

- void **set_constant_angular_velocity** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_constant_angular_velocity** ( )

The body's constant angular velocity. This does not rotate the body, but affects touching bodies, as if it were rotating.

---

<span id="class_StaticBody2D_property_constant_linear_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **constant_linear_velocity** = `Vector2(0, 0)` [🔗](class_staticbody2d.md#class_StaticBody2D_property_constant_linear_velocity)

- void **set_constant_linear_velocity** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_constant_linear_velocity** ( )

The body's constant linear velocity. This does not move the body, but affects touching bodies, as if it were moving.

---

<span id="class_StaticBody2D_property_physics_material_override"></span>

[PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) **physics_material_override** [🔗](class_staticbody2d.md#class_StaticBody2D_property_physics_material_override)

- void **set_physics_material_override** ( value: [PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) )
- [PhysicsMaterial](class_physicsmaterial.md#class_PhysicsMaterial) **get_physics_material_override** ( )

The physics material override for the body.

If a material is assigned to this property, it will be used instead of any other physics material, such as an inherited one.
