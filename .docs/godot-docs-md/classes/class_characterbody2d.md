<span id="class_CharacterBody2D"></span>

## CharacterBody2D

**Inherits:** [PhysicsBody2D](class_physicsbody2d.md#class_PhysicsBody2D) **<** [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) **<** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A 2D physics body specialized for characters moved by script.

### Description

**CharacterBody2D** is a specialized class for physics bodies that are meant to be user-controlled. They are not affected by physics at all, but they affect other physics bodies in their path. They are mainly used to provide high-level API to move objects with wall and slope detection ([move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide) method) in addition to the general collision detection provided by [PhysicsBody2D.move_and_collide()](class_physicsbody2d.md#class_PhysicsBody2D_method_move_and_collide). This makes it useful for highly configurable physics bodies that must move in specific ways and collide with the world, as is often the case with user-controlled characters.

For game objects that don't require complex movement or collision detection, such as moving platforms, [AnimatableBody2D](class_animatablebody2d.md#class_AnimatableBody2D) is simpler to configure.

### Tutorials

- [Physics introduction](../tutorials/physics/physics_introduction.md)

- [Troubleshooting physics issues](../tutorials/physics/troubleshooting_physics_issues.md)

- [Kinematic character (2D)](../tutorials/physics/kinematic_character_2d.md)

- [Using CharacterBody2D](../tutorials/physics/using_character_body_2d.md)

- 2D Kinematic Character Demo

- 2D Platformer Demo

### Properties


| [bool](class_bool.md#class_bool) | [floor_block_on_wall](class_characterbody2d.md#class_CharacterBody2D_property_floor_block_on_wall) | `true` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [floor_constant_speed](class_characterbody2d.md#class_CharacterBody2D_property_floor_constant_speed) | `false` |
| [float](class_float.md#class_float) | [floor_max_angle](class_characterbody2d.md#class_CharacterBody2D_property_floor_max_angle) | `0.7853982` |
| [float](class_float.md#class_float) | [floor_snap_length](class_characterbody2d.md#class_CharacterBody2D_property_floor_snap_length) | `1.0` |
| [bool](class_bool.md#class_bool) | [floor_stop_on_slope](class_characterbody2d.md#class_CharacterBody2D_property_floor_stop_on_slope) | `true` |
| [int](class_int.md#class_int) | [max_slides](class_characterbody2d.md#class_CharacterBody2D_property_max_slides) | `4` |
| [MotionMode](class_characterbody2d.md#enum_CharacterBody2D_MotionMode) | [motion_mode](class_characterbody2d.md#class_CharacterBody2D_property_motion_mode) | `0` |
| [int](class_int.md#class_int) | [platform_floor_layers](class_characterbody2d.md#class_CharacterBody2D_property_platform_floor_layers) | `4294967295` |
| [PlatformOnLeave](class_characterbody2d.md#enum_CharacterBody2D_PlatformOnLeave) | [platform_on_leave](class_characterbody2d.md#class_CharacterBody2D_property_platform_on_leave) | `0` |
| [int](class_int.md#class_int) | [platform_wall_layers](class_characterbody2d.md#class_CharacterBody2D_property_platform_wall_layers) | `0` |
| [float](class_float.md#class_float) | [safe_margin](class_characterbody2d.md#class_CharacterBody2D_property_safe_margin) | `0.08` |
| [bool](class_bool.md#class_bool) | [slide_on_ceiling](class_characterbody2d.md#class_CharacterBody2D_property_slide_on_ceiling) | `true` |
| [Vector2](class_vector2.md#class_Vector2) | [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction) | `Vector2(0, -1)` |
| [Vector2](class_vector2.md#class_Vector2) | [velocity](class_characterbody2d.md#class_CharacterBody2D_property_velocity) | `Vector2(0, 0)` |
| [float](class_float.md#class_float) | [wall_min_slide_angle](class_characterbody2d.md#class_CharacterBody2D_property_wall_min_slide_angle) | `0.2617994` |

### Methods


| void | [apply_floor_snap](class_characterbody2d.md#class_CharacterBody2D_method_apply_floor_snap) ( ) |
| --- | --- |
| [float](class_float.md#class_float) | [get_floor_angle](class_characterbody2d.md#class_CharacterBody2D_method_get_floor_angle) ( up_direction: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, -1) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_floor_normal](class_characterbody2d.md#class_CharacterBody2D_method_get_floor_normal) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_last_motion](class_characterbody2d.md#class_CharacterBody2D_method_get_last_motion) ( ) const |
| [KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D) | [get_last_slide_collision](class_characterbody2d.md#class_CharacterBody2D_method_get_last_slide_collision) ( ) |
| [Vector2](class_vector2.md#class_Vector2) | [get_platform_velocity](class_characterbody2d.md#class_CharacterBody2D_method_get_platform_velocity) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_position_delta](class_characterbody2d.md#class_CharacterBody2D_method_get_position_delta) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_real_velocity](class_characterbody2d.md#class_CharacterBody2D_method_get_real_velocity) ( ) const |
| [KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D) | [get_slide_collision](class_characterbody2d.md#class_CharacterBody2D_method_get_slide_collision) ( slide_idx: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [get_slide_collision_count](class_characterbody2d.md#class_CharacterBody2D_method_get_slide_collision_count) ( ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_wall_normal](class_characterbody2d.md#class_CharacterBody2D_method_get_wall_normal) ( ) const |
| [bool](class_bool.md#class_bool) | [is_on_ceiling](class_characterbody2d.md#class_CharacterBody2D_method_is_on_ceiling) ( ) const |
| [bool](class_bool.md#class_bool) | [is_on_ceiling_only](class_characterbody2d.md#class_CharacterBody2D_method_is_on_ceiling_only) ( ) const |
| [bool](class_bool.md#class_bool) | [is_on_floor](class_characterbody2d.md#class_CharacterBody2D_method_is_on_floor) ( ) const |
| [bool](class_bool.md#class_bool) | [is_on_floor_only](class_characterbody2d.md#class_CharacterBody2D_method_is_on_floor_only) ( ) const |
| [bool](class_bool.md#class_bool) | [is_on_wall](class_characterbody2d.md#class_CharacterBody2D_method_is_on_wall) ( ) const |
| [bool](class_bool.md#class_bool) | [is_on_wall_only](class_characterbody2d.md#class_CharacterBody2D_method_is_on_wall_only) ( ) const |
| [bool](class_bool.md#class_bool) | [move_and_slide](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide) ( ) |

---

### Enumerations

<span id="enum_CharacterBody2D_MotionMode"></span>

enum **MotionMode**: [🔗](class_characterbody2d.md#enum_CharacterBody2D_MotionMode)

<span id="class_CharacterBody2D_constant_MOTION_MODE_GROUNDED"></span>

[MotionMode](class_characterbody2d.md#enum_CharacterBody2D_MotionMode) **MOTION_MODE_GROUNDED** = `0`

Apply when notions of walls, ceiling and floor are relevant. In this mode the body motion will react to slopes (acceleration/slowdown). This mode is suitable for sided games like platformers.

<span id="class_CharacterBody2D_constant_MOTION_MODE_FLOATING"></span>

[MotionMode](class_characterbody2d.md#enum_CharacterBody2D_MotionMode) **MOTION_MODE_FLOATING** = `1`

Apply when there is no notion of floor or ceiling. All collisions will be reported as `on_wall`. In this mode, when you slide, the speed will always be constant. This mode is suitable for top-down games.

---

<span id="enum_CharacterBody2D_PlatformOnLeave"></span>

enum **PlatformOnLeave**: [🔗](class_characterbody2d.md#enum_CharacterBody2D_PlatformOnLeave)

<span id="class_CharacterBody2D_constant_PLATFORM_ON_LEAVE_ADD_VELOCITY"></span>

[PlatformOnLeave](class_characterbody2d.md#enum_CharacterBody2D_PlatformOnLeave) **PLATFORM_ON_LEAVE_ADD_VELOCITY** = `0`

Add the last platform velocity to the [velocity](class_characterbody2d.md#class_CharacterBody2D_property_velocity) when you leave a moving platform.

<span id="class_CharacterBody2D_constant_PLATFORM_ON_LEAVE_ADD_UPWARD_VELOCITY"></span>

[PlatformOnLeave](class_characterbody2d.md#enum_CharacterBody2D_PlatformOnLeave) **PLATFORM_ON_LEAVE_ADD_UPWARD_VELOCITY** = `1`

Add the last platform velocity to the [velocity](class_characterbody2d.md#class_CharacterBody2D_property_velocity) when you leave a moving platform, but any downward motion is ignored. It's useful to keep full jump height even when the platform is moving down.

<span id="class_CharacterBody2D_constant_PLATFORM_ON_LEAVE_DO_NOTHING"></span>

[PlatformOnLeave](class_characterbody2d.md#enum_CharacterBody2D_PlatformOnLeave) **PLATFORM_ON_LEAVE_DO_NOTHING** = `2`

Do nothing when leaving a platform.

---

### Property Descriptions

<span id="class_CharacterBody2D_property_floor_block_on_wall"></span>

[bool](class_bool.md#class_bool) **floor_block_on_wall** = `true` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_floor_block_on_wall)

- void **set_floor_block_on_wall_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_floor_block_on_wall_enabled** ( )

If `true`, the body will be able to move on the floor only. This option avoids to be able to walk on walls, it will however allow to slide down along them.

---

<span id="class_CharacterBody2D_property_floor_constant_speed"></span>

[bool](class_bool.md#class_bool) **floor_constant_speed** = `false` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_floor_constant_speed)

- void **set_floor_constant_speed_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_floor_constant_speed_enabled** ( )

If `false` (by default), the body will move faster on downward slopes and slower on upward slopes.

If `true`, the body will always move at the same speed on the ground no matter the slope. Note that you need to use [floor_snap_length](class_characterbody2d.md#class_CharacterBody2D_property_floor_snap_length) to stick along a downward slope at constant speed.

---

<span id="class_CharacterBody2D_property_floor_max_angle"></span>

[float](class_float.md#class_float) **floor_max_angle** = `0.7853982` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_floor_max_angle)

- void **set_floor_max_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_floor_max_angle** ( )

Maximum angle (in radians) where a slope is still considered a floor (or a ceiling), rather than a wall, when calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). The default value equals 45 degrees.

---

<span id="class_CharacterBody2D_property_floor_snap_length"></span>

[float](class_float.md#class_float) **floor_snap_length** = `1.0` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_floor_snap_length)

- void **set_floor_snap_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_floor_snap_length** ( )

Sets a snapping distance. When set to a value different from `0.0`, the body is kept attached to slopes when calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). The snapping vector is determined by the given distance along the opposite direction of the [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction).

As long as the snapping vector is in contact with the ground and the body moves against [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction), the body will remain attached to the surface. Snapping is not applied if the body moves along [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction), meaning it contains vertical rising velocity, so it will be able to detach from the ground when jumping or when the body is pushed up by something. If you want to apply a snap without taking into account the velocity, use [apply_floor_snap()](class_characterbody2d.md#class_CharacterBody2D_method_apply_floor_snap).

---

<span id="class_CharacterBody2D_property_floor_stop_on_slope"></span>

[bool](class_bool.md#class_bool) **floor_stop_on_slope** = `true` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_floor_stop_on_slope)

- void **set_floor_stop_on_slope_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_floor_stop_on_slope_enabled** ( )

If `true`, the body will not slide on slopes when calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide) when the body is standing still.

If `false`, the body will slide on floor's slopes when [velocity](class_characterbody2d.md#class_CharacterBody2D_property_velocity) applies a downward force.

---

<span id="class_CharacterBody2D_property_max_slides"></span>

[int](class_int.md#class_int) **max_slides** = `4` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_max_slides)

- void **set_max_slides** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_max_slides** ( )

Maximum number of times the body can change direction before it stops when calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Must be greater than zero.

---

<span id="class_CharacterBody2D_property_motion_mode"></span>

[MotionMode](class_characterbody2d.md#enum_CharacterBody2D_MotionMode) **motion_mode** = `0` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_motion_mode)

- void **set_motion_mode** ( value: [MotionMode](class_characterbody2d.md#enum_CharacterBody2D_MotionMode) )
- [MotionMode](class_characterbody2d.md#enum_CharacterBody2D_MotionMode) **get_motion_mode** ( )

Sets the motion mode which defines the behavior of [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide).

---

<span id="class_CharacterBody2D_property_platform_floor_layers"></span>

[int](class_int.md#class_int) **platform_floor_layers** = `4294967295` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_platform_floor_layers)

- void **set_platform_floor_layers** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_platform_floor_layers** ( )

Collision layers that will be included for detecting floor bodies that will act as moving platforms to be followed by the **CharacterBody2D**. By default, all floor bodies are detected and propagate their velocity.

---

<span id="class_CharacterBody2D_property_platform_on_leave"></span>

[PlatformOnLeave](class_characterbody2d.md#enum_CharacterBody2D_PlatformOnLeave) **platform_on_leave** = `0` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_platform_on_leave)

- void **set_platform_on_leave** ( value: [PlatformOnLeave](class_characterbody2d.md#enum_CharacterBody2D_PlatformOnLeave) )
- [PlatformOnLeave](class_characterbody2d.md#enum_CharacterBody2D_PlatformOnLeave) **get_platform_on_leave** ( )

Sets the behavior to apply when you leave a moving platform. By default, to be physically accurate, when you leave the last platform velocity is applied.

---

<span id="class_CharacterBody2D_property_platform_wall_layers"></span>

[int](class_int.md#class_int) **platform_wall_layers** = `0` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_platform_wall_layers)

- void **set_platform_wall_layers** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_platform_wall_layers** ( )

Collision layers that will be included for detecting wall bodies that will act as moving platforms to be followed by the **CharacterBody2D**. By default, all wall bodies are ignored.

---

<span id="class_CharacterBody2D_property_safe_margin"></span>

[float](class_float.md#class_float) **safe_margin** = `0.08` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_safe_margin)

- void **set_safe_margin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_safe_margin** ( )

Extra margin used for collision recovery when calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide).

If the body is at least this close to another body, it will consider them to be colliding and will be pushed away before performing the actual motion.

A higher value means it's more flexible for detecting collision, which helps with consistently detecting walls and floors.

A lower value forces the collision algorithm to use more exact detection, so it can be used in cases that specifically require precision, e.g at very low scale to avoid visible jittering, or for stability with a stack of character bodies.

---

<span id="class_CharacterBody2D_property_slide_on_ceiling"></span>

[bool](class_bool.md#class_bool) **slide_on_ceiling** = `true` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_slide_on_ceiling)

- void **set_slide_on_ceiling_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_slide_on_ceiling_enabled** ( )

If `true`, during a jump against the ceiling, the body will slide, if `false` it will be stopped and will fall vertically.

---

<span id="class_CharacterBody2D_property_up_direction"></span>

[Vector2](class_vector2.md#class_Vector2) **up_direction** = `Vector2(0, -1)` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_up_direction)

- void **set_up_direction** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_up_direction** ( )

Vector pointing upwards, used to determine what is a wall and what is a floor (or a ceiling) when calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Defaults to [Vector2.UP](class_vector2.md#class_Vector2_constant_UP). As the vector will be normalized it can't be equal to [Vector2.ZERO](class_vector2.md#class_Vector2_constant_ZERO), if you want all collisions to be reported as walls, consider using [MOTION_MODE_FLOATING](class_characterbody2d.md#class_CharacterBody2D_constant_MOTION_MODE_FLOATING) as [motion_mode](class_characterbody2d.md#class_CharacterBody2D_property_motion_mode).

---

<span id="class_CharacterBody2D_property_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **velocity** = `Vector2(0, 0)` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_velocity)

- void **set_velocity** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_velocity** ( )

Current velocity vector in pixels per second, used and modified during calls to [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide).

 **Note:** A common mistake is setting this property to the desired velocity multiplied by `delta`, which produces a motion vector in pixels.

---

<span id="class_CharacterBody2D_property_wall_min_slide_angle"></span>

[float](class_float.md#class_float) **wall_min_slide_angle** = `0.2617994` [🔗](class_characterbody2d.md#class_CharacterBody2D_property_wall_min_slide_angle)

- void **set_wall_min_slide_angle** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_wall_min_slide_angle** ( )

Minimum angle (in radians) where the body is allowed to slide when it encounters a wall. The default value equals 15 degrees. This property only affects movement when [motion_mode](class_characterbody2d.md#class_CharacterBody2D_property_motion_mode) is [MOTION_MODE_FLOATING](class_characterbody2d.md#class_CharacterBody2D_constant_MOTION_MODE_FLOATING).

---

### Method Descriptions

<span id="class_CharacterBody2D_method_apply_floor_snap"></span>

void **apply_floor_snap** ( ) [🔗](class_characterbody2d.md#class_CharacterBody2D_method_apply_floor_snap)

Allows to manually apply a snap to the floor regardless of the body's velocity. This function does nothing when [is_on_floor()](class_characterbody2d.md#class_CharacterBody2D_method_is_on_floor) returns `true`.

---

<span id="class_CharacterBody2D_method_get_floor_angle"></span>

[float](class_float.md#class_float) **get_floor_angle** ( up_direction: [Vector2](class_vector2.md#class_Vector2) = Vector2(0, -1) ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_floor_angle)

Returns the floor's collision angle at the last collision point according to `up_direction`, which is [Vector2.UP](class_vector2.md#class_Vector2_constant_UP) by default. This value is always positive and only valid after calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide) and when [is_on_floor()](class_characterbody2d.md#class_CharacterBody2D_method_is_on_floor) returns `true`.

---

<span id="class_CharacterBody2D_method_get_floor_normal"></span>

[Vector2](class_vector2.md#class_Vector2) **get_floor_normal** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_floor_normal)

Returns the collision normal of the floor at the last collision point. Only valid after calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide) and when [is_on_floor()](class_characterbody2d.md#class_CharacterBody2D_method_is_on_floor) returns `true`.

 **Warning:** The collision normal is not always the same as the surface normal.

---

<span id="class_CharacterBody2D_method_get_last_motion"></span>

[Vector2](class_vector2.md#class_Vector2) **get_last_motion** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_last_motion)

Returns the last motion applied to the **CharacterBody2D** during the last call to [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). The movement can be split into multiple motions when sliding occurs, and this method return the last one, which is useful to retrieve the current direction of the movement.

---

<span id="class_CharacterBody2D_method_get_last_slide_collision"></span>

[KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D) **get_last_slide_collision** ( ) [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_last_slide_collision)

Returns a [KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D) if a collision occurred. The returned value contains information about the latest collision that occurred during the last call to [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Returns `null` if no collision occurred. See also [get_slide_collision()](class_characterbody2d.md#class_CharacterBody2D_method_get_slide_collision).

---

<span id="class_CharacterBody2D_method_get_platform_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **get_platform_velocity** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_platform_velocity)

Returns the linear velocity of the platform at the last collision point. Only valid after calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide).

---

<span id="class_CharacterBody2D_method_get_position_delta"></span>

[Vector2](class_vector2.md#class_Vector2) **get_position_delta** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_position_delta)

Returns the travel (position delta) that occurred during the last call to [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide).

---

<span id="class_CharacterBody2D_method_get_real_velocity"></span>

[Vector2](class_vector2.md#class_Vector2) **get_real_velocity** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_real_velocity)

Returns the current real velocity since the last call to [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). For example, when you climb a slope, you will move diagonally even though the velocity is horizontal. This method returns the diagonal movement, as opposed to [velocity](class_characterbody2d.md#class_CharacterBody2D_property_velocity) which returns the requested velocity.

---

<span id="class_CharacterBody2D_method_get_slide_collision"></span>

[KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D) **get_slide_collision** ( slide_idx: [int](class_int.md#class_int) ) [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_slide_collision)

Returns a [KinematicCollision2D](class_kinematiccollision2d.md#class_KinematicCollision2D), which contains information about a collision that occurred during the last call to [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Since the body can collide several times in a single call to [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide), you must specify the index of the collision in the range 0 to ([get_slide_collision_count()](class_characterbody2d.md#class_CharacterBody2D_method_get_slide_collision_count) - 1). See also [get_last_slide_collision()](class_characterbody2d.md#class_CharacterBody2D_method_get_last_slide_collision).

 **Example:** Iterate through the collisions with a `for` loop:

.. tabs::

```
```

    for i in get_slide_collision_count():
        var collision = get_slide_collision(i)
        print("Collided with: ", collision.get_collider().name)

```
```

    for (int i = 0; i < GetSlideCollisionCount(); i++)
    {
        KinematicCollision2D collision = GetSlideCollision(i);
        GD.Print("Collided with: ", (collision.GetCollider() as Node).Name);
    }

---

<span id="class_CharacterBody2D_method_get_slide_collision_count"></span>

[int](class_int.md#class_int) **get_slide_collision_count** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_slide_collision_count)

Returns the number of times the body collided and changed direction during the last call to [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide).

---

<span id="class_CharacterBody2D_method_get_wall_normal"></span>

[Vector2](class_vector2.md#class_Vector2) **get_wall_normal** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_get_wall_normal)

Returns the collision normal of the wall at the last collision point. Only valid after calling [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide) and when [is_on_wall()](class_characterbody2d.md#class_CharacterBody2D_method_is_on_wall) returns `true`.

 **Warning:** The collision normal is not always the same as the surface normal.

---

<span id="class_CharacterBody2D_method_is_on_ceiling"></span>

[bool](class_bool.md#class_bool) **is_on_ceiling** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_is_on_ceiling)

Returns `true` if the body collided with the ceiling on the last call of [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Otherwise, returns `false`. The [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction) and [floor_max_angle](class_characterbody2d.md#class_CharacterBody2D_property_floor_max_angle) are used to determine whether a surface is "ceiling" or not.

---

<span id="class_CharacterBody2D_method_is_on_ceiling_only"></span>

[bool](class_bool.md#class_bool) **is_on_ceiling_only** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_is_on_ceiling_only)

Returns `true` if the body collided only with the ceiling on the last call of [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Otherwise, returns `false`. The [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction) and [floor_max_angle](class_characterbody2d.md#class_CharacterBody2D_property_floor_max_angle) are used to determine whether a surface is "ceiling" or not.

---

<span id="class_CharacterBody2D_method_is_on_floor"></span>

[bool](class_bool.md#class_bool) **is_on_floor** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_is_on_floor)

Returns `true` if the body collided with the floor on the last call of [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Otherwise, returns `false`. The [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction) and [floor_max_angle](class_characterbody2d.md#class_CharacterBody2D_property_floor_max_angle) are used to determine whether a surface is "floor" or not.

---

<span id="class_CharacterBody2D_method_is_on_floor_only"></span>

[bool](class_bool.md#class_bool) **is_on_floor_only** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_is_on_floor_only)

Returns `true` if the body collided only with the floor on the last call of [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Otherwise, returns `false`. The [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction) and [floor_max_angle](class_characterbody2d.md#class_CharacterBody2D_property_floor_max_angle) are used to determine whether a surface is "floor" or not.

---

<span id="class_CharacterBody2D_method_is_on_wall"></span>

[bool](class_bool.md#class_bool) **is_on_wall** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_is_on_wall)

Returns `true` if the body collided with a wall on the last call of [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Otherwise, returns `false`. The [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction) and [floor_max_angle](class_characterbody2d.md#class_CharacterBody2D_property_floor_max_angle) are used to determine whether a surface is "wall" or not.

---

<span id="class_CharacterBody2D_method_is_on_wall_only"></span>

[bool](class_bool.md#class_bool) **is_on_wall_only** ( ) *const* [🔗](class_characterbody2d.md#class_CharacterBody2D_method_is_on_wall_only)

Returns `true` if the body collided only with a wall on the last call of [move_and_slide()](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide). Otherwise, returns `false`. The [up_direction](class_characterbody2d.md#class_CharacterBody2D_property_up_direction) and [floor_max_angle](class_characterbody2d.md#class_CharacterBody2D_property_floor_max_angle) are used to determine whether a surface is "wall" or not.

---

<span id="class_CharacterBody2D_method_move_and_slide"></span>

[bool](class_bool.md#class_bool) **move_and_slide** ( ) [🔗](class_characterbody2d.md#class_CharacterBody2D_method_move_and_slide)

Moves the body based on [velocity](class_characterbody2d.md#class_CharacterBody2D_property_velocity). If the body collides with another, it will slide along the other body (by default only on floor) rather than stop immediately. If the other body is a **CharacterBody2D** or [RigidBody2D](class_rigidbody2d.md#class_RigidBody2D), it will also be affected by the motion of the other body. You can use this to make moving and rotating platforms, or to make nodes push other nodes.

This method should be used in [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) (or in a method called by [Node._physics_process()](class_node.md#class_Node_private_method__physics_process)), as it uses the physics step's `delta` value automatically in calculations. Otherwise, the simulation will run at an incorrect speed.

Modifies [velocity](class_characterbody2d.md#class_CharacterBody2D_property_velocity) if a slide collision occurred. To get the latest collision call [get_last_slide_collision()](class_characterbody2d.md#class_CharacterBody2D_method_get_last_slide_collision), for detailed information about collisions that occurred, use [get_slide_collision()](class_characterbody2d.md#class_CharacterBody2D_method_get_slide_collision).

When the body touches a moving platform, the platform's velocity is automatically added to the body motion. If a collision occurs due to the platform's motion, it will always be first in the slide collisions.

The general behavior and available properties change according to the [motion_mode](class_characterbody2d.md#class_CharacterBody2D_property_motion_mode).

Returns `true` if the body collided, otherwise, returns `false`.
