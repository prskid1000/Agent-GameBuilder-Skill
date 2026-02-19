<span id="class_CollisionObject3D"></span>

## CollisionObject3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [Area3D](class_area3d.md#class_Area3D), [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D)

Abstract base class for 3D physics objects.

### Description

Abstract base class for 3D physics objects. **CollisionObject3D** can hold any number of [Shape3D](class_shape3d.md#class_Shape3D) s for collision. Each shape must be assigned to a *shape owner*. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the `shape_owner_*` methods.

 **Warning:** With a non-uniform scale, this node will likely not behave as expected. It is advised to keep its scale the same on all axes and adjust its collision shape(s) instead.

### Properties


| [int](class_int.md#class_int) | [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer) | `1` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [collision_mask](class_collisionobject3d.md#class_CollisionObject3D_property_collision_mask) | `1` |
| [float](class_float.md#class_float) | [collision_priority](class_collisionobject3d.md#class_CollisionObject3D_property_collision_priority) | `1.0` |
| [DisableMode](class_collisionobject3d.md#enum_CollisionObject3D_DisableMode) | [disable_mode](class_collisionobject3d.md#class_CollisionObject3D_property_disable_mode) | `0` |
| [bool](class_bool.md#class_bool) | [input_capture_on_drag](class_collisionobject3d.md#class_CollisionObject3D_property_input_capture_on_drag) | `false` |
| [bool](class_bool.md#class_bool) | [input_ray_pickable](class_collisionobject3d.md#class_CollisionObject3D_property_input_ray_pickable) | `true` |

### Methods


| void | [_input_event](class_collisionobject3d.md#class_CollisionObject3D_private_method__input_event) ( camera: [Camera3D](class_camera3d.md#class_Camera3D), event: [InputEvent](class_inputevent.md#class_InputEvent), event_position: [Vector3](class_vector3.md#class_Vector3), normal: [Vector3](class_vector3.md#class_Vector3), shape_idx: [int](class_int.md#class_int) ) virtual |
| --- | --- |
| void | [_mouse_enter](class_collisionobject3d.md#class_CollisionObject3D_private_method__mouse_enter) ( ) virtual |
| void | [_mouse_exit](class_collisionobject3d.md#class_CollisionObject3D_private_method__mouse_exit) ( ) virtual |
| [int](class_int.md#class_int) | [create_shape_owner](class_collisionobject3d.md#class_CollisionObject3D_method_create_shape_owner) ( owner: [Object](class_object.md#class_Object) ) |
| [bool](class_bool.md#class_bool) | [get_collision_layer_value](class_collisionobject3d.md#class_CollisionObject3D_method_get_collision_layer_value) ( layer_number: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_collision_mask_value](class_collisionobject3d.md#class_CollisionObject3D_method_get_collision_mask_value) ( layer_number: [int](class_int.md#class_int) ) const |
| [RID](class_rid.md#class_RID) | [get_rid](class_collisionobject3d.md#class_CollisionObject3D_method_get_rid) ( ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_shape_owners](class_collisionobject3d.md#class_CollisionObject3D_method_get_shape_owners) ( ) |
| [bool](class_bool.md#class_bool) | [is_shape_owner_disabled](class_collisionobject3d.md#class_CollisionObject3D_method_is_shape_owner_disabled) ( owner_id: [int](class_int.md#class_int) ) const |
| void | [remove_shape_owner](class_collisionobject3d.md#class_CollisionObject3D_method_remove_shape_owner) ( owner_id: [int](class_int.md#class_int) ) |
| void | [set_collision_layer_value](class_collisionobject3d.md#class_CollisionObject3D_method_set_collision_layer_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |
| void | [set_collision_mask_value](class_collisionobject3d.md#class_CollisionObject3D_method_set_collision_mask_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |
| [int](class_int.md#class_int) | [shape_find_owner](class_collisionobject3d.md#class_CollisionObject3D_method_shape_find_owner) ( shape_index: [int](class_int.md#class_int) ) const |
| void | [shape_owner_add_shape](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_add_shape) ( owner_id: [int](class_int.md#class_int), shape: [Shape3D](class_shape3d.md#class_Shape3D) ) |
| void | [shape_owner_clear_shapes](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_clear_shapes) ( owner_id: [int](class_int.md#class_int) ) |
| [Object](class_object.md#class_Object) | [shape_owner_get_owner](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_owner) ( owner_id: [int](class_int.md#class_int) ) const |
| [Shape3D](class_shape3d.md#class_Shape3D) | [shape_owner_get_shape](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_shape) ( owner_id: [int](class_int.md#class_int), shape_id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [shape_owner_get_shape_count](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_shape_count) ( owner_id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [shape_owner_get_shape_index](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_shape_index) ( owner_id: [int](class_int.md#class_int), shape_id: [int](class_int.md#class_int) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [shape_owner_get_transform](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_transform) ( owner_id: [int](class_int.md#class_int) ) const |
| void | [shape_owner_remove_shape](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_remove_shape) ( owner_id: [int](class_int.md#class_int), shape_id: [int](class_int.md#class_int) ) |
| void | [shape_owner_set_disabled](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_set_disabled) ( owner_id: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) |
| void | [shape_owner_set_transform](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_set_transform) ( owner_id: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |

---

### Signals

<span id="class_CollisionObject3D_signal_input_event"></span>

**input_event** ( camera: [Node](class_node.md#class_Node), event: [InputEvent](class_inputevent.md#class_InputEvent), event_position: [Vector3](class_vector3.md#class_Vector3), normal: [Vector3](class_vector3.md#class_Vector3), shape_idx: [int](class_int.md#class_int) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_signal_input_event)

Emitted when the object receives an unhandled [InputEvent](class_inputevent.md#class_InputEvent). `event_position` is the location in world space of the mouse pointer on the surface of the shape with index `shape_idx` and `normal` is the normal vector of the surface at that point.

---

<span id="class_CollisionObject3D_signal_mouse_entered"></span>

**mouse_entered** ( ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_signal_mouse_entered)

Emitted when the mouse pointer enters any of this object's shapes. Requires [input_ray_pickable](class_collisionobject3d.md#class_CollisionObject3D_property_input_ray_pickable) to be `true` and at least one [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer) bit to be set.

 **Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject3D**'s area is small. This signal may also not be emitted if another **CollisionObject3D** is overlapping the **CollisionObject3D** in question.

---

<span id="class_CollisionObject3D_signal_mouse_exited"></span>

**mouse_exited** ( ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_signal_mouse_exited)

Emitted when the mouse pointer exits all this object's shapes. Requires [input_ray_pickable](class_collisionobject3d.md#class_CollisionObject3D_property_input_ray_pickable) to be `true` and at least one [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer) bit to be set.

 **Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject3D**'s area is small. This signal may also not be emitted if another **CollisionObject3D** is overlapping the **CollisionObject3D** in question.

---

### Enumerations

<span id="enum_CollisionObject3D_DisableMode"></span>

enum **DisableMode**: [🔗](class_collisionobject3d.md#enum_CollisionObject3D_DisableMode)

<span id="class_CollisionObject3D_constant_DISABLE_MODE_REMOVE"></span>

[DisableMode](class_collisionobject3d.md#enum_CollisionObject3D_DisableMode) **DISABLE_MODE_REMOVE** = `0`

When [Node.process_mode](class_node.md#class_Node_property_process_mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class_Node_constant_PROCESS_MODE_DISABLED), remove from the physics simulation to stop all physics interactions with this **CollisionObject3D**.

Automatically re-added to the physics simulation when the [Node](class_node.md#class_Node) is processed again.

<span id="class_CollisionObject3D_constant_DISABLE_MODE_MAKE_STATIC"></span>

[DisableMode](class_collisionobject3d.md#enum_CollisionObject3D_DisableMode) **DISABLE_MODE_MAKE_STATIC** = `1`

When [Node.process_mode](class_node.md#class_Node_property_process_mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class_Node_constant_PROCESS_MODE_DISABLED), make the body static. Doesn't affect [Area3D](class_area3d.md#class_Area3D). [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) can't be affected by forces or other bodies while static.

Automatically set [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) back to its original mode when the [Node](class_node.md#class_Node) is processed again.

<span id="class_CollisionObject3D_constant_DISABLE_MODE_KEEP_ACTIVE"></span>

[DisableMode](class_collisionobject3d.md#enum_CollisionObject3D_DisableMode) **DISABLE_MODE_KEEP_ACTIVE** = `2`

When [Node.process_mode](class_node.md#class_Node_property_process_mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class_Node_constant_PROCESS_MODE_DISABLED), do not affect the physics simulation.

---

### Property Descriptions

<span id="class_CollisionObject3D_property_collision_layer"></span>

[int](class_int.md#class_int) **collision_layer** = `1` [🔗](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer)

- void **set_collision_layer** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_layer** ( )

The physics layers this CollisionObject3D **is in**. Collision objects can exist in one or more of 32 different layers. See also [collision_mask](class_collisionobject3d.md#class_CollisionObject3D_property_collision_mask).

 **Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_CollisionObject3D_property_collision_mask"></span>

[int](class_int.md#class_int) **collision_mask** = `1` [🔗](class_collisionobject3d.md#class_CollisionObject3D_property_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The physics layers this CollisionObject3D **scans**. Collision objects can scan one or more of 32 different layers. See also [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer).

 **Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_CollisionObject3D_property_collision_priority"></span>

[float](class_float.md#class_float) **collision_priority** = `1.0` [🔗](class_collisionobject3d.md#class_CollisionObject3D_property_collision_priority)

- void **set_collision_priority** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_collision_priority** ( )

The priority used to solve colliding when occurring penetration. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.

---

<span id="class_CollisionObject3D_property_disable_mode"></span>

[DisableMode](class_collisionobject3d.md#enum_CollisionObject3D_DisableMode) **disable_mode** = `0` [🔗](class_collisionobject3d.md#class_CollisionObject3D_property_disable_mode)

- void **set_disable_mode** ( value: [DisableMode](class_collisionobject3d.md#enum_CollisionObject3D_DisableMode) )
- [DisableMode](class_collisionobject3d.md#enum_CollisionObject3D_DisableMode) **get_disable_mode** ( )

Defines the behavior in physics when [Node.process_mode](class_node.md#class_Node_property_process_mode) is set to [Node.PROCESS_MODE_DISABLED](class_node.md#class_Node_constant_PROCESS_MODE_DISABLED).

---

<span id="class_CollisionObject3D_property_input_capture_on_drag"></span>

[bool](class_bool.md#class_bool) **input_capture_on_drag** = `false` [🔗](class_collisionobject3d.md#class_CollisionObject3D_property_input_capture_on_drag)

- void **set_capture_input_on_drag** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_capture_input_on_drag** ( )

If `true`, the **CollisionObject3D** will continue to receive input events as the mouse is dragged across its shapes.

---

<span id="class_CollisionObject3D_property_input_ray_pickable"></span>

[bool](class_bool.md#class_bool) **input_ray_pickable** = `true` [🔗](class_collisionobject3d.md#class_CollisionObject3D_property_input_ray_pickable)

- void **set_ray_pickable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_ray_pickable** ( )

If `true`, this object is pickable. A pickable object can detect the mouse pointer entering/leaving, and if the mouse is inside it, report input events. Requires at least one [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer) bit to be set.

---

### Method Descriptions

<span id="class_CollisionObject3D_private_method__input_event"></span>

void **_input_event** ( camera: [Camera3D](class_camera3d.md#class_Camera3D), event: [InputEvent](class_inputevent.md#class_InputEvent), event_position: [Vector3](class_vector3.md#class_Vector3), normal: [Vector3](class_vector3.md#class_Vector3), shape_idx: [int](class_int.md#class_int) ) *virtual* [🔗](class_collisionobject3d.md#class_CollisionObject3D_private_method__input_event)

Receives unhandled [InputEvent](class_inputevent.md#class_InputEvent) s. `event_position` is the location in world space of the mouse pointer on the surface of the shape with index `shape_idx` and `normal` is the normal vector of the surface at that point. Connect to the [input_event](class_collisionobject3d.md#class_CollisionObject3D_signal_input_event) signal to easily pick up these events.

 **Note:** [_input_event()](class_collisionobject3d.md#class_CollisionObject3D_private_method__input_event) requires [input_ray_pickable](class_collisionobject3d.md#class_CollisionObject3D_property_input_ray_pickable) to be `true` and at least one [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer) bit to be set.

---

<span id="class_CollisionObject3D_private_method__mouse_enter"></span>

void **_mouse_enter** ( ) *virtual* [🔗](class_collisionobject3d.md#class_CollisionObject3D_private_method__mouse_enter)

Called when the mouse pointer enters any of this object's shapes. Requires [input_ray_pickable](class_collisionobject3d.md#class_CollisionObject3D_property_input_ray_pickable) to be `true` and at least one [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer) bit to be set. Note that moving between different shapes within a single **CollisionObject3D** won't cause this function to be called.

---

<span id="class_CollisionObject3D_private_method__mouse_exit"></span>

void **_mouse_exit** ( ) *virtual* [🔗](class_collisionobject3d.md#class_CollisionObject3D_private_method__mouse_exit)

Called when the mouse pointer exits all this object's shapes. Requires [input_ray_pickable](class_collisionobject3d.md#class_CollisionObject3D_property_input_ray_pickable) to be `true` and at least one [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer) bit to be set. Note that moving between different shapes within a single **CollisionObject3D** won't cause this function to be called.

---

<span id="class_CollisionObject3D_method_create_shape_owner"></span>

[int](class_int.md#class_int) **create_shape_owner** ( owner: [Object](class_object.md#class_Object) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_create_shape_owner)

Creates a new shape owner for the given object. Returns `owner_id` of the new owner for future reference.

---

<span id="class_CollisionObject3D_method_get_collision_layer_value"></span>

[bool](class_bool.md#class_bool) **get_collision_layer_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_get_collision_layer_value)

Returns whether or not the specified layer of the [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer) is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_CollisionObject3D_method_get_collision_mask_value"></span>

[bool](class_bool.md#class_bool) **get_collision_mask_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_get_collision_mask_value)

Returns whether or not the specified layer of the [collision_mask](class_collisionobject3d.md#class_CollisionObject3D_property_collision_mask) is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_CollisionObject3D_method_get_rid"></span>

[RID](class_rid.md#class_RID) **get_rid** ( ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_get_rid)

Returns the object's [RID](class_rid.md#class_RID).

---

<span id="class_CollisionObject3D_method_get_shape_owners"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_shape_owners** ( ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_get_shape_owners)

Returns an [Array](class_array.md#class_Array) of `owner_id` identifiers. You can use these ids in other methods that take `owner_id` as an argument.

---

<span id="class_CollisionObject3D_method_is_shape_owner_disabled"></span>

[bool](class_bool.md#class_bool) **is_shape_owner_disabled** ( owner_id: [int](class_int.md#class_int) ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_is_shape_owner_disabled)

If `true`, the shape owner and its shapes are disabled.

---

<span id="class_CollisionObject3D_method_remove_shape_owner"></span>

void **remove_shape_owner** ( owner_id: [int](class_int.md#class_int) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_remove_shape_owner)

Removes the given shape owner.

---

<span id="class_CollisionObject3D_method_set_collision_layer_value"></span>

void **set_collision_layer_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_set_collision_layer_value)

Based on `value`, enables or disables the specified layer in the [collision_layer](class_collisionobject3d.md#class_CollisionObject3D_property_collision_layer), given a `layer_number` between 1 and 32.

---

<span id="class_CollisionObject3D_method_set_collision_mask_value"></span>

void **set_collision_mask_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_set_collision_mask_value)

Based on `value`, enables or disables the specified layer in the [collision_mask](class_collisionobject3d.md#class_CollisionObject3D_property_collision_mask), given a `layer_number` between 1 and 32.

---

<span id="class_CollisionObject3D_method_shape_find_owner"></span>

[int](class_int.md#class_int) **shape_find_owner** ( shape_index: [int](class_int.md#class_int) ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_find_owner)

Returns the `owner_id` of the given shape.

---

<span id="class_CollisionObject3D_method_shape_owner_add_shape"></span>

void **shape_owner_add_shape** ( owner_id: [int](class_int.md#class_int), shape: [Shape3D](class_shape3d.md#class_Shape3D) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_add_shape)

Adds a [Shape3D](class_shape3d.md#class_Shape3D) to the shape owner.

---

<span id="class_CollisionObject3D_method_shape_owner_clear_shapes"></span>

void **shape_owner_clear_shapes** ( owner_id: [int](class_int.md#class_int) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_clear_shapes)

Removes all shapes from the shape owner.

---

<span id="class_CollisionObject3D_method_shape_owner_get_owner"></span>

[Object](class_object.md#class_Object) **shape_owner_get_owner** ( owner_id: [int](class_int.md#class_int) ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_owner)

Returns the parent object of the given shape owner.

---

<span id="class_CollisionObject3D_method_shape_owner_get_shape"></span>

[Shape3D](class_shape3d.md#class_Shape3D) **shape_owner_get_shape** ( owner_id: [int](class_int.md#class_int), shape_id: [int](class_int.md#class_int) ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_shape)

Returns the [Shape3D](class_shape3d.md#class_Shape3D) with the given ID from the given shape owner.

---

<span id="class_CollisionObject3D_method_shape_owner_get_shape_count"></span>

[int](class_int.md#class_int) **shape_owner_get_shape_count** ( owner_id: [int](class_int.md#class_int) ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_shape_count)

Returns the number of shapes the given shape owner contains.

---

<span id="class_CollisionObject3D_method_shape_owner_get_shape_index"></span>

[int](class_int.md#class_int) **shape_owner_get_shape_index** ( owner_id: [int](class_int.md#class_int), shape_id: [int](class_int.md#class_int) ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_shape_index)

Returns the child index of the [Shape3D](class_shape3d.md#class_Shape3D) with the given ID from the given shape owner.

---

<span id="class_CollisionObject3D_method_shape_owner_get_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **shape_owner_get_transform** ( owner_id: [int](class_int.md#class_int) ) *const* [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_get_transform)

Returns the shape owner's [Transform3D](class_transform3d.md#class_Transform3D).

---

<span id="class_CollisionObject3D_method_shape_owner_remove_shape"></span>

void **shape_owner_remove_shape** ( owner_id: [int](class_int.md#class_int), shape_id: [int](class_int.md#class_int) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_remove_shape)

Removes a shape from the given shape owner.

---

<span id="class_CollisionObject3D_method_shape_owner_set_disabled"></span>

void **shape_owner_set_disabled** ( owner_id: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_set_disabled)

If `true`, disables the given shape owner.

---

<span id="class_CollisionObject3D_method_shape_owner_set_transform"></span>

void **shape_owner_set_transform** ( owner_id: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_collisionobject3d.md#class_CollisionObject3D_method_shape_owner_set_transform)

Sets the [Transform3D](class_transform3d.md#class_Transform3D) of the given shape owner.
