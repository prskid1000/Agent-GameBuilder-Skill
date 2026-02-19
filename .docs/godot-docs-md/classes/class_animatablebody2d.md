<span id="class_AnimatableBody2D"></span>

## AnimatableBody2D

**Inherits:** [StaticBody2D](class_staticbody2d.md#class_StaticBody2D) **<** [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) **<** [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A 2D physics body that can't be moved by external forces. When moved manually, it affects other bodies in its path.

### Description

An animatable 2D physics body. It can't be moved by external forces or contacts, but can be moved manually by other means such as code, [AnimationMixer](class_animationmixer.md#class_AnimationMixer) s (with [AnimationMixer.callback_mode_process](class_animationmixer.md#class_AnimationMixer_property_callback_mode_process) set to [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS](class_animationmixer.md#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS)), and [RemoteTransform2D](class_remotetransform2d.md#class_RemoteTransform2D).

When **AnimatableBody2D** is moved, its linear and angular velocity are estimated and used to affect other physics bodies in its path. This makes it useful for moving platforms, doors, and other moving objects.

### Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)

### Properties


| [bool](class_bool.md#class_bool) | [sync_to_physics](class_animatablebody2d.md#class_AnimatableBody2D_property_sync_to_physics) | `true` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_AnimatableBody2D_property_sync_to_physics"></span>

[bool](class_bool.md#class_bool) **sync_to_physics** = `true` [🔗](class_animatablebody2d.md#class_AnimatableBody2D_property_sync_to_physics)

- void **set_sync_to_physics** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_sync_to_physics_enabled** ( )

If `true`, the body's movement will be synchronized to the physics frame. This is useful when animating movement via [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer), for example on moving platforms. Do **not** use together with [PhysicsBody2D.move_and_collide()](class_physicsbody2d.md#class_PhysicsBody2D_method_move_and_collide).
