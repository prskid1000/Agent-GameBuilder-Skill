<span id="class_PhysicsServer2DExtension"></span>

## PhysicsServer2DExtension

**Inherits:** [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D) **<** [Object](class_object.md#class_Object)

Provides virtual methods that can be overridden to create custom [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D) implementations.

### Description

This class extends [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D).

### Methods


| void | [_area_add_shape](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_add_shape) ( area: [RID](class_rid.md#class_RID), shape: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), disabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| --- | --- | --- | --- |
| void | [_area_attach_canvas_instance_id](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_attach_canvas_instance_id) ( area: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) | virtual | required |
| void | [_area_attach_object_instance_id](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_attach_object_instance_id) ( area: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) | virtual | required |
| void | [_area_clear_shapes](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_clear_shapes) ( area: [RID](class_rid.md#class_RID) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_area_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_create) ( ) | virtual | required |
| [int](class_int.md#class_int) | [_area_get_canvas_instance_id](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_canvas_instance_id) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_area_get_collision_layer](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_collision_layer) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_area_get_collision_mask](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_collision_mask) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_area_get_object_instance_id](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_object_instance_id) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_area_get_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_param) ( area: [RID](class_rid.md#class_RID), param: [AreaParameter](class_physicsserver2d.md#enum_PhysicsServer2D_AreaParameter) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_area_get_shape](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_shape) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_area_get_shape_count](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_shape_count) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [_area_get_shape_transform](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_shape_transform) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_area_get_space](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_space) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [_area_get_transform](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_transform) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_area_remove_shape](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_remove_shape) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required |
| void | [_area_set_area_monitor_callback](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_area_monitor_callback) ( area: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) | virtual | required |
| void | [_area_set_collision_layer](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_collision_layer) ( area: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) | virtual | required |
| void | [_area_set_collision_mask](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_collision_mask) ( area: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) | virtual | required |
| void | [_area_set_monitor_callback](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_monitor_callback) ( area: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) | virtual | required |
| void | [_area_set_monitorable](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_monitorable) ( area: [RID](class_rid.md#class_RID), monitorable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_area_set_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_param) ( area: [RID](class_rid.md#class_RID), param: [AreaParameter](class_physicsserver2d.md#enum_PhysicsServer2D_AreaParameter), value: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_area_set_pickable](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_pickable) ( area: [RID](class_rid.md#class_RID), pickable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_area_set_shape](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_shape) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_area_set_shape_disabled](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_shape_disabled) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_area_set_shape_transform](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_shape_transform) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) | virtual | required |
| void | [_area_set_space](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_space) ( area: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_area_set_transform](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_transform) ( area: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) | virtual | required |
| void | [_body_add_collision_exception](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_collision_exception) ( body: [RID](class_rid.md#class_RID), excepted_body: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_add_constant_central_force](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_constant_central_force) ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_body_add_constant_force](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_constant_force) ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_body_add_constant_torque](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_constant_torque) ( body: [RID](class_rid.md#class_RID), torque: [float](class_float.md#class_float) ) | virtual | required |
| void | [_body_add_shape](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_shape) ( body: [RID](class_rid.md#class_RID), shape: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), disabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_apply_central_force](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_central_force) ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_body_apply_central_impulse](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_central_impulse) ( body: [RID](class_rid.md#class_RID), impulse: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_body_apply_force](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_force) ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_body_apply_impulse](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_impulse) ( body: [RID](class_rid.md#class_RID), impulse: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_body_apply_torque](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_torque) ( body: [RID](class_rid.md#class_RID), torque: [float](class_float.md#class_float) ) | virtual | required |
| void | [_body_apply_torque_impulse](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_torque_impulse) ( body: [RID](class_rid.md#class_RID), impulse: [float](class_float.md#class_float) ) | virtual | required |
| void | [_body_attach_canvas_instance_id](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_attach_canvas_instance_id) ( body: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_attach_object_instance_id](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_attach_object_instance_id) ( body: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_clear_shapes](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_clear_shapes) ( body: [RID](class_rid.md#class_RID) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_body_collide_shape](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_collide_shape) ( body: [RID](class_rid.md#class_RID), body_shape: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID), shape_xform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), results: `void*`, result_max: [int](class_int.md#class_int), result_count: `int32_t*` ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_body_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_create) ( ) | virtual | required |
| [int](class_int.md#class_int) | [_body_get_canvas_instance_id](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_canvas_instance_id) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [_body_get_collision_exceptions](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_collision_exceptions) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_body_get_collision_layer](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_collision_layer) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_body_get_collision_mask](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_collision_mask) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_body_get_collision_priority](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_collision_priority) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Vector2](class_vector2.md#class_Vector2) | [_body_get_constant_force](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_constant_force) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_body_get_constant_torque](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_constant_torque) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_body_get_contacts_reported_depth_threshold](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_contacts_reported_depth_threshold) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [CCDMode](class_physicsserver2d.md#enum_PhysicsServer2D_CCDMode) | [_body_get_continuous_collision_detection_mode](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_continuous_collision_detection_mode) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D) | [_body_get_direct_state](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_direct_state) ( body: [RID](class_rid.md#class_RID) ) | virtual | required |
| [int](class_int.md#class_int) | [_body_get_max_contacts_reported](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_max_contacts_reported) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [BodyMode](class_physicsserver2d.md#enum_PhysicsServer2D_BodyMode) | [_body_get_mode](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_mode) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_body_get_object_instance_id](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_object_instance_id) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_body_get_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_param) ( body: [RID](class_rid.md#class_RID), param: [BodyParameter](class_physicsserver2d.md#enum_PhysicsServer2D_BodyParameter) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_body_get_shape](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_shape) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_body_get_shape_count](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_shape_count) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [_body_get_shape_transform](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_shape_transform) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_body_get_space](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_space) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_body_get_state](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_state) ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver2d.md#enum_PhysicsServer2D_BodyState) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_body_is_omitting_force_integration](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_is_omitting_force_integration) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_body_remove_collision_exception](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_remove_collision_exception) ( body: [RID](class_rid.md#class_RID), excepted_body: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_remove_shape](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_remove_shape) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_reset_mass_properties](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_reset_mass_properties) ( body: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_set_axis_velocity](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_axis_velocity) ( body: [RID](class_rid.md#class_RID), axis_velocity: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_body_set_collision_layer](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_collision_layer) ( body: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_set_collision_mask](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_collision_mask) ( body: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_set_collision_priority](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_collision_priority) ( body: [RID](class_rid.md#class_RID), priority: [float](class_float.md#class_float) ) | virtual | required |
| void | [_body_set_constant_force](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_constant_force) ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_body_set_constant_torque](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_constant_torque) ( body: [RID](class_rid.md#class_RID), torque: [float](class_float.md#class_float) ) | virtual | required |
| void | [_body_set_contacts_reported_depth_threshold](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_contacts_reported_depth_threshold) ( body: [RID](class_rid.md#class_RID), threshold: [float](class_float.md#class_float) ) | virtual | required |
| void | [_body_set_continuous_collision_detection_mode](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_continuous_collision_detection_mode) ( body: [RID](class_rid.md#class_RID), mode: [CCDMode](class_physicsserver2d.md#enum_PhysicsServer2D_CCDMode) ) | virtual | required |
| void | [_body_set_force_integration_callback](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_force_integration_callback) ( body: [RID](class_rid.md#class_RID), callable: [Callable](class_callable.md#class_Callable), userdata: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_body_set_max_contacts_reported](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_max_contacts_reported) ( body: [RID](class_rid.md#class_RID), amount: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_set_mode](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_mode) ( body: [RID](class_rid.md#class_RID), mode: [BodyMode](class_physicsserver2d.md#enum_PhysicsServer2D_BodyMode) ) | virtual | required |
| void | [_body_set_omit_force_integration](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_omit_force_integration) ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_set_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_param) ( body: [RID](class_rid.md#class_RID), param: [BodyParameter](class_physicsserver2d.md#enum_PhysicsServer2D_BodyParameter), value: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_body_set_pickable](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_pickable) ( body: [RID](class_rid.md#class_RID), pickable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_set_shape](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_shape) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_set_shape_as_one_way_collision](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_shape_as_one_way_collision) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool), margin: [float](class_float.md#class_float), direction: [Vector2](class_vector2.md#class_Vector2) ) | virtual | required |
| void | [_body_set_shape_disabled](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_shape_disabled) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_set_shape_transform](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_shape_transform) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) | virtual | required |
| void | [_body_set_space](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_space) ( body: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_set_state](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_state) ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver2d.md#enum_PhysicsServer2D_BodyState), value: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_body_set_state_sync_callback](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_state_sync_callback) ( body: [RID](class_rid.md#class_RID), callable: [Callable](class_callable.md#class_Callable) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_body_test_motion](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_test_motion) ( body: [RID](class_rid.md#class_RID), from: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collide_separation_ray: [bool](class_bool.md#class_bool), recovery_as_collision: [bool](class_bool.md#class_bool), result: `PhysicsServer2DExtensionMotionResult*` ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_capsule_shape_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__capsule_shape_create) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_circle_shape_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__circle_shape_create) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_concave_polygon_shape_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__concave_polygon_shape_create) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_convex_polygon_shape_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__convex_polygon_shape_create) ( ) | virtual | required |
| [float](class_float.md#class_float) | [_damped_spring_joint_get_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__damped_spring_joint_get_param) ( joint: [RID](class_rid.md#class_RID), param: [DampedSpringParam](class_physicsserver2d.md#enum_PhysicsServer2D_DampedSpringParam) ) | virtual | required | const |
| void | [_damped_spring_joint_set_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__damped_spring_joint_set_param) ( joint: [RID](class_rid.md#class_RID), param: [DampedSpringParam](class_physicsserver2d.md#enum_PhysicsServer2D_DampedSpringParam), value: [float](class_float.md#class_float) ) | virtual | required |
| void | [_end_sync](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__end_sync) ( ) | virtual | required |
| void | [_finish](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__finish) ( ) | virtual | required |
| void | [_flush_queries](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__flush_queries) ( ) | virtual | required |
| void | [_free_rid](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__free_rid) ( rid: [RID](class_rid.md#class_RID) ) | virtual | required |
| [int](class_int.md#class_int) | [_get_process_info](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__get_process_info) ( process_info: [ProcessInfo](class_physicsserver2d.md#enum_PhysicsServer2D_ProcessInfo) ) | virtual | required |
| void | [_init](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__init) ( ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_is_flushing_queries](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__is_flushing_queries) ( ) | virtual | required | const |
| void | [_joint_clear](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_clear) ( joint: [RID](class_rid.md#class_RID) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_joint_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_create) ( ) | virtual | required |
| void | [_joint_disable_collisions_between_bodies](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_disable_collisions_between_bodies) ( joint: [RID](class_rid.md#class_RID), disable: [bool](class_bool.md#class_bool) ) | virtual | required |
| [float](class_float.md#class_float) | [_joint_get_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_get_param) ( joint: [RID](class_rid.md#class_RID), param: [JointParam](class_physicsserver2d.md#enum_PhysicsServer2D_JointParam) ) | virtual | required | const |
| [JointType](class_physicsserver2d.md#enum_PhysicsServer2D_JointType) | [_joint_get_type](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_get_type) ( joint: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_joint_is_disabled_collisions_between_bodies](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_is_disabled_collisions_between_bodies) ( joint: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_joint_make_damped_spring](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_make_damped_spring) ( joint: [RID](class_rid.md#class_RID), anchor_a: [Vector2](class_vector2.md#class_Vector2), anchor_b: [Vector2](class_vector2.md#class_Vector2), body_a: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_joint_make_groove](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_make_groove) ( joint: [RID](class_rid.md#class_RID), a_groove1: [Vector2](class_vector2.md#class_Vector2), a_groove2: [Vector2](class_vector2.md#class_Vector2), b_anchor: [Vector2](class_vector2.md#class_Vector2), body_a: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_joint_make_pin](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_make_pin) ( joint: [RID](class_rid.md#class_RID), anchor: [Vector2](class_vector2.md#class_Vector2), body_a: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_joint_set_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_set_param) ( joint: [RID](class_rid.md#class_RID), param: [JointParam](class_physicsserver2d.md#enum_PhysicsServer2D_JointParam), value: [float](class_float.md#class_float) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_pin_joint_get_flag](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__pin_joint_get_flag) ( joint: [RID](class_rid.md#class_RID), flag: [PinJointFlag](class_physicsserver2d.md#enum_PhysicsServer2D_PinJointFlag) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_pin_joint_get_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__pin_joint_get_param) ( joint: [RID](class_rid.md#class_RID), param: [PinJointParam](class_physicsserver2d.md#enum_PhysicsServer2D_PinJointParam) ) | virtual | required | const |
| void | [_pin_joint_set_flag](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__pin_joint_set_flag) ( joint: [RID](class_rid.md#class_RID), flag: [PinJointFlag](class_physicsserver2d.md#enum_PhysicsServer2D_PinJointFlag), enabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_pin_joint_set_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__pin_joint_set_param) ( joint: [RID](class_rid.md#class_RID), param: [PinJointParam](class_physicsserver2d.md#enum_PhysicsServer2D_PinJointParam), value: [float](class_float.md#class_float) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_rectangle_shape_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__rectangle_shape_create) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_segment_shape_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__segment_shape_create) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_separation_ray_shape_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__separation_ray_shape_create) ( ) | virtual | required |
| void | [_set_active](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__set_active) ( active: [bool](class_bool.md#class_bool) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_shape_collide](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_collide) ( shape_A: [RID](class_rid.md#class_RID), xform_A: [Transform2D](class_transform2d.md#class_Transform2D), motion_A: [Vector2](class_vector2.md#class_Vector2), shape_B: [RID](class_rid.md#class_RID), xform_B: [Transform2D](class_transform2d.md#class_Transform2D), motion_B: [Vector2](class_vector2.md#class_Vector2), results: `void*`, result_max: [int](class_int.md#class_int), result_count: `int32_t*` ) | virtual | required |
| [float](class_float.md#class_float) | [_shape_get_custom_solver_bias](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_get_custom_solver_bias) ( shape: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_shape_get_data](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_get_data) ( shape: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [ShapeType](class_physicsserver2d.md#enum_PhysicsServer2D_ShapeType) | [_shape_get_type](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_get_type) ( shape: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_shape_set_custom_solver_bias](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_set_custom_solver_bias) ( shape: [RID](class_rid.md#class_RID), bias: [float](class_float.md#class_float) ) | virtual | required |
| void | [_shape_set_data](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_set_data) ( shape: [RID](class_rid.md#class_RID), data: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_space_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_create) ( ) | virtual | required |
| [int](class_int.md#class_int) | [_space_get_contact_count](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_contact_count) ( space: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [_space_get_contacts](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_contacts) ( space: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) | [_space_get_direct_state](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_direct_state) ( space: [RID](class_rid.md#class_RID) ) | virtual | required |
| [float](class_float.md#class_float) | [_space_get_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_param) ( space: [RID](class_rid.md#class_RID), param: [SpaceParameter](class_physicsserver2d.md#enum_PhysicsServer2D_SpaceParameter) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_space_is_active](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_is_active) ( space: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_space_set_active](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_set_active) ( space: [RID](class_rid.md#class_RID), active: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_space_set_debug_contacts](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_set_debug_contacts) ( space: [RID](class_rid.md#class_RID), max_contacts: [int](class_int.md#class_int) ) | virtual | required |
| void | [_space_set_param](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_set_param) ( space: [RID](class_rid.md#class_RID), param: [SpaceParameter](class_physicsserver2d.md#enum_PhysicsServer2D_SpaceParameter), value: [float](class_float.md#class_float) ) | virtual | required |
| void | [_step](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__step) ( step: [float](class_float.md#class_float) ) | virtual | required |
| void | [_sync](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__sync) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_world_boundary_shape_create](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__world_boundary_shape_create) ( ) | virtual | required |
| [bool](class_bool.md#class_bool) | [body_test_motion_is_excluding_body](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_body) ( body: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [body_test_motion_is_excluding_object](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_object) ( object: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_PhysicsServer2DExtension_private_method__area_add_shape"></span>

void **_area_add_shape** ( area: [RID](class_rid.md#class_RID), shape: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), disabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_add_shape)

Overridable version of [PhysicsServer2D.area_add_shape()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_add_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__area_attach_canvas_instance_id"></span>

void **_area_attach_canvas_instance_id** ( area: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_attach_canvas_instance_id)

Overridable version of [PhysicsServer2D.area_attach_canvas_instance_id()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_attach_canvas_instance_id).

---

<span id="class_PhysicsServer2DExtension_private_method__area_attach_object_instance_id"></span>

void **_area_attach_object_instance_id** ( area: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_attach_object_instance_id)

Overridable version of [PhysicsServer2D.area_attach_object_instance_id()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_attach_object_instance_id).

---

<span id="class_PhysicsServer2DExtension_private_method__area_clear_shapes"></span>

void **_area_clear_shapes** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_clear_shapes)

Overridable version of [PhysicsServer2D.area_clear_shapes()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_clear_shapes).

---

<span id="class_PhysicsServer2DExtension_private_method__area_create"></span>

[RID](class_rid.md#class_RID) **_area_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_create)

Overridable version of [PhysicsServer2D.area_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_create).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_canvas_instance_id"></span>

[int](class_int.md#class_int) **_area_get_canvas_instance_id** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_canvas_instance_id)

Overridable version of [PhysicsServer2D.area_get_canvas_instance_id()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_canvas_instance_id).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_collision_layer"></span>

[int](class_int.md#class_int) **_area_get_collision_layer** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_collision_layer)

Overridable version of [PhysicsServer2D.area_get_collision_layer()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_collision_layer).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_collision_mask"></span>

[int](class_int.md#class_int) **_area_get_collision_mask** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_collision_mask)

Overridable version of [PhysicsServer2D.area_get_collision_mask()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_collision_mask).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_object_instance_id"></span>

[int](class_int.md#class_int) **_area_get_object_instance_id** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_object_instance_id)

Overridable version of [PhysicsServer2D.area_get_object_instance_id()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_object_instance_id).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_param"></span>

[Variant](class_variant.md#class_Variant) **_area_get_param** ( area: [RID](class_rid.md#class_RID), param: [AreaParameter](class_physicsserver2d.md#enum_PhysicsServer2D_AreaParameter) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_param)

Overridable version of [PhysicsServer2D.area_get_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_param).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_shape"></span>

[RID](class_rid.md#class_RID) **_area_get_shape** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_shape)

Overridable version of [PhysicsServer2D.area_get_shape()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_shape_count"></span>

[int](class_int.md#class_int) **_area_get_shape_count** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_shape_count)

Overridable version of [PhysicsServer2D.area_get_shape_count()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_shape_count).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_shape_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **_area_get_shape_transform** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_shape_transform)

Overridable version of [PhysicsServer2D.area_get_shape_transform()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_shape_transform).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_space"></span>

[RID](class_rid.md#class_RID) **_area_get_space** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_space)

Overridable version of [PhysicsServer2D.area_get_space()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_space).

---

<span id="class_PhysicsServer2DExtension_private_method__area_get_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **_area_get_transform** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_get_transform)

Overridable version of [PhysicsServer2D.area_get_transform()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_get_transform).

---

<span id="class_PhysicsServer2DExtension_private_method__area_remove_shape"></span>

void **_area_remove_shape** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_remove_shape)

Overridable version of [PhysicsServer2D.area_remove_shape()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_remove_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_area_monitor_callback"></span>

void **_area_set_area_monitor_callback** ( area: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_area_monitor_callback)

Overridable version of [PhysicsServer2D.area_set_area_monitor_callback()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_area_monitor_callback).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_collision_layer"></span>

void **_area_set_collision_layer** ( area: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_collision_layer)

Overridable version of [PhysicsServer2D.area_set_collision_layer()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_collision_layer).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_collision_mask"></span>

void **_area_set_collision_mask** ( area: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_collision_mask)

Overridable version of [PhysicsServer2D.area_set_collision_mask()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_collision_mask).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_monitor_callback"></span>

void **_area_set_monitor_callback** ( area: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_monitor_callback)

Overridable version of [PhysicsServer2D.area_set_monitor_callback()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_monitor_callback).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_monitorable"></span>

void **_area_set_monitorable** ( area: [RID](class_rid.md#class_RID), monitorable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_monitorable)

Overridable version of [PhysicsServer2D.area_set_monitorable()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_monitorable).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_param"></span>

void **_area_set_param** ( area: [RID](class_rid.md#class_RID), param: [AreaParameter](class_physicsserver2d.md#enum_PhysicsServer2D_AreaParameter), value: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_param)

Overridable version of [PhysicsServer2D.area_set_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_param).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_pickable"></span>

void **_area_set_pickable** ( area: [RID](class_rid.md#class_RID), pickable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_pickable)

If set to `true`, allows the area with the given [RID](class_rid.md#class_RID) to detect mouse inputs when the mouse cursor is hovering on it.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `area_set_pickable` method. Corresponds to [CollisionObject2D.input_pickable](class_collisionobject2d.md#class_CollisionObject2D_property_input_pickable).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_shape"></span>

void **_area_set_shape** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_shape)

Overridable version of [PhysicsServer2D.area_set_shape()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_shape_disabled"></span>

void **_area_set_shape_disabled** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_shape_disabled)

Overridable version of [PhysicsServer2D.area_set_shape_disabled()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_shape_disabled).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_shape_transform"></span>

void **_area_set_shape_transform** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_shape_transform)

Overridable version of [PhysicsServer2D.area_set_shape_transform()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_shape_transform).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_space"></span>

void **_area_set_space** ( area: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_space)

Overridable version of [PhysicsServer2D.area_set_space()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_space).

---

<span id="class_PhysicsServer2DExtension_private_method__area_set_transform"></span>

void **_area_set_transform** ( area: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__area_set_transform)

Overridable version of [PhysicsServer2D.area_set_transform()](class_physicsserver2d.md#class_PhysicsServer2D_method_area_set_transform).

---

<span id="class_PhysicsServer2DExtension_private_method__body_add_collision_exception"></span>

void **_body_add_collision_exception** ( body: [RID](class_rid.md#class_RID), excepted_body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_collision_exception)

Overridable version of [PhysicsServer2D.body_add_collision_exception()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_add_collision_exception).

---

<span id="class_PhysicsServer2DExtension_private_method__body_add_constant_central_force"></span>

void **_body_add_constant_central_force** ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_constant_central_force)

Overridable version of [PhysicsServer2D.body_add_constant_central_force()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_add_constant_central_force).

---

<span id="class_PhysicsServer2DExtension_private_method__body_add_constant_force"></span>

void **_body_add_constant_force** ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_constant_force)

Overridable version of [PhysicsServer2D.body_add_constant_force()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_add_constant_force).

---

<span id="class_PhysicsServer2DExtension_private_method__body_add_constant_torque"></span>

void **_body_add_constant_torque** ( body: [RID](class_rid.md#class_RID), torque: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_constant_torque)

Overridable version of [PhysicsServer2D.body_add_constant_torque()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_add_constant_torque).

---

<span id="class_PhysicsServer2DExtension_private_method__body_add_shape"></span>

void **_body_add_shape** ( body: [RID](class_rid.md#class_RID), shape: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), disabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_shape)

Overridable version of [PhysicsServer2D.body_add_shape()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_add_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__body_apply_central_force"></span>

void **_body_apply_central_force** ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_central_force)

Overridable version of [PhysicsServer2D.body_apply_central_force()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_apply_central_force).

---

<span id="class_PhysicsServer2DExtension_private_method__body_apply_central_impulse"></span>

void **_body_apply_central_impulse** ( body: [RID](class_rid.md#class_RID), impulse: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_central_impulse)

Overridable version of [PhysicsServer2D.body_apply_central_impulse()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_apply_central_impulse).

---

<span id="class_PhysicsServer2DExtension_private_method__body_apply_force"></span>

void **_body_apply_force** ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_force)

Overridable version of [PhysicsServer2D.body_apply_force()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_apply_force).

---

<span id="class_PhysicsServer2DExtension_private_method__body_apply_impulse"></span>

void **_body_apply_impulse** ( body: [RID](class_rid.md#class_RID), impulse: [Vector2](class_vector2.md#class_Vector2), position: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_impulse)

Overridable version of [PhysicsServer2D.body_apply_impulse()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_apply_impulse).

---

<span id="class_PhysicsServer2DExtension_private_method__body_apply_torque"></span>

void **_body_apply_torque** ( body: [RID](class_rid.md#class_RID), torque: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_torque)

Overridable version of [PhysicsServer2D.body_apply_torque()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_apply_torque).

---

<span id="class_PhysicsServer2DExtension_private_method__body_apply_torque_impulse"></span>

void **_body_apply_torque_impulse** ( body: [RID](class_rid.md#class_RID), impulse: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_apply_torque_impulse)

Overridable version of [PhysicsServer2D.body_apply_torque_impulse()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_apply_torque_impulse).

---

<span id="class_PhysicsServer2DExtension_private_method__body_attach_canvas_instance_id"></span>

void **_body_attach_canvas_instance_id** ( body: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_attach_canvas_instance_id)

Overridable version of [PhysicsServer2D.body_attach_canvas_instance_id()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_attach_canvas_instance_id).

---

<span id="class_PhysicsServer2DExtension_private_method__body_attach_object_instance_id"></span>

void **_body_attach_object_instance_id** ( body: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_attach_object_instance_id)

Overridable version of [PhysicsServer2D.body_attach_object_instance_id()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_attach_object_instance_id).

---

<span id="class_PhysicsServer2DExtension_private_method__body_clear_shapes"></span>

void **_body_clear_shapes** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_clear_shapes)

Overridable version of [PhysicsServer2D.body_clear_shapes()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_clear_shapes).

---

<span id="class_PhysicsServer2DExtension_private_method__body_collide_shape"></span>

[bool](class_bool.md#class_bool) **_body_collide_shape** ( body: [RID](class_rid.md#class_RID), body_shape: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID), shape_xform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), results: `void*`, result_max: [int](class_int.md#class_int), result_count: `int32_t*` ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_collide_shape)

Given a `body`, a `shape`, and their respective parameters, this method should return `true` if a collision between the two would occur, with additional details passed in `results`.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `shape_collide` method. Corresponds to [PhysicsDirectSpaceState2D.collide_shape()](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D_method_collide_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__body_create"></span>

[RID](class_rid.md#class_RID) **_body_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_create)

Overridable version of [PhysicsServer2D.body_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_create).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_canvas_instance_id"></span>

[int](class_int.md#class_int) **_body_get_canvas_instance_id** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_canvas_instance_id)

Overridable version of [PhysicsServer2D.body_get_canvas_instance_id()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_canvas_instance_id).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_collision_exceptions"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **_body_get_collision_exceptions** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_collision_exceptions)

Returns the [RID](class_rid.md#class_RID) s of all bodies added as collision exceptions for the given `body`. See also [_body_add_collision_exception()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_add_collision_exception) and [_body_remove_collision_exception()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_remove_collision_exception).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `body_get_collision_exceptions` method. Corresponds to [PhysicsBody2D.get_collision_exceptions()](class_physicsbody2d.md#class_PhysicsBody2D_method_get_collision_exceptions).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_collision_layer"></span>

[int](class_int.md#class_int) **_body_get_collision_layer** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_collision_layer)

Overridable version of [PhysicsServer2D.body_get_collision_layer()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_collision_layer).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_collision_mask"></span>

[int](class_int.md#class_int) **_body_get_collision_mask** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_collision_mask)

Overridable version of [PhysicsServer2D.body_get_collision_mask()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_collision_mask).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_collision_priority"></span>

[float](class_float.md#class_float) **_body_get_collision_priority** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_collision_priority)

Overridable version of [PhysicsServer2D.body_get_collision_priority()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_collision_priority).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_constant_force"></span>

[Vector2](class_vector2.md#class_Vector2) **_body_get_constant_force** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_constant_force)

Overridable version of [PhysicsServer2D.body_get_constant_force()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_constant_force).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_constant_torque"></span>

[float](class_float.md#class_float) **_body_get_constant_torque** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_constant_torque)

Overridable version of [PhysicsServer2D.body_get_constant_torque()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_constant_torque).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_contacts_reported_depth_threshold"></span>

[float](class_float.md#class_float) **_body_get_contacts_reported_depth_threshold** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_contacts_reported_depth_threshold)

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `body_get_contacts_reported_depth_threshold` method.

 **Note:** This method is currently unused by Godot's default physics implementation.

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_continuous_collision_detection_mode"></span>

[CCDMode](class_physicsserver2d.md#enum_PhysicsServer2D_CCDMode) **_body_get_continuous_collision_detection_mode** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_continuous_collision_detection_mode)

Overridable version of [PhysicsServer2D.body_get_continuous_collision_detection_mode()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_continuous_collision_detection_mode).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_direct_state"></span>

[PhysicsDirectBodyState2D](class_physicsdirectbodystate2d.md#class_PhysicsDirectBodyState2D) **_body_get_direct_state** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_direct_state)

Overridable version of [PhysicsServer2D.body_get_direct_state()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_direct_state).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_max_contacts_reported"></span>

[int](class_int.md#class_int) **_body_get_max_contacts_reported** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_max_contacts_reported)

Overridable version of [PhysicsServer2D.body_get_max_contacts_reported()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_max_contacts_reported).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_mode"></span>

[BodyMode](class_physicsserver2d.md#enum_PhysicsServer2D_BodyMode) **_body_get_mode** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_mode)

Overridable version of [PhysicsServer2D.body_get_mode()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_mode).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_object_instance_id"></span>

[int](class_int.md#class_int) **_body_get_object_instance_id** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_object_instance_id)

Overridable version of [PhysicsServer2D.body_get_object_instance_id()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_object_instance_id).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_param"></span>

[Variant](class_variant.md#class_Variant) **_body_get_param** ( body: [RID](class_rid.md#class_RID), param: [BodyParameter](class_physicsserver2d.md#enum_PhysicsServer2D_BodyParameter) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_param)

Overridable version of [PhysicsServer2D.body_get_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_param).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_shape"></span>

[RID](class_rid.md#class_RID) **_body_get_shape** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_shape)

Overridable version of [PhysicsServer2D.body_get_shape()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_shape_count"></span>

[int](class_int.md#class_int) **_body_get_shape_count** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_shape_count)

Overridable version of [PhysicsServer2D.body_get_shape_count()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_shape_count).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_shape_transform"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **_body_get_shape_transform** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_shape_transform)

Overridable version of [PhysicsServer2D.body_get_shape_transform()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_shape_transform).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_space"></span>

[RID](class_rid.md#class_RID) **_body_get_space** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_space)

Overridable version of [PhysicsServer2D.body_get_space()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_space).

---

<span id="class_PhysicsServer2DExtension_private_method__body_get_state"></span>

[Variant](class_variant.md#class_Variant) **_body_get_state** ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver2d.md#enum_PhysicsServer2D_BodyState) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_get_state)

Overridable version of [PhysicsServer2D.body_get_state()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_get_state).

---

<span id="class_PhysicsServer2DExtension_private_method__body_is_omitting_force_integration"></span>

[bool](class_bool.md#class_bool) **_body_is_omitting_force_integration** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_is_omitting_force_integration)

Overridable version of [PhysicsServer2D.body_is_omitting_force_integration()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_is_omitting_force_integration).

---

<span id="class_PhysicsServer2DExtension_private_method__body_remove_collision_exception"></span>

void **_body_remove_collision_exception** ( body: [RID](class_rid.md#class_RID), excepted_body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_remove_collision_exception)

Overridable version of [PhysicsServer2D.body_remove_collision_exception()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_remove_collision_exception).

---

<span id="class_PhysicsServer2DExtension_private_method__body_remove_shape"></span>

void **_body_remove_shape** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_remove_shape)

Overridable version of [PhysicsServer2D.body_remove_shape()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_remove_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__body_reset_mass_properties"></span>

void **_body_reset_mass_properties** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_reset_mass_properties)

Overridable version of [PhysicsServer2D.body_reset_mass_properties()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_reset_mass_properties).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_axis_velocity"></span>

void **_body_set_axis_velocity** ( body: [RID](class_rid.md#class_RID), axis_velocity: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_axis_velocity)

Overridable version of [PhysicsServer2D.body_set_axis_velocity()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_axis_velocity).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_collision_layer"></span>

void **_body_set_collision_layer** ( body: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_collision_layer)

Overridable version of [PhysicsServer2D.body_set_collision_layer()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_collision_layer).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_collision_mask"></span>

void **_body_set_collision_mask** ( body: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_collision_mask)

Overridable version of [PhysicsServer2D.body_set_collision_mask()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_collision_mask).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_collision_priority"></span>

void **_body_set_collision_priority** ( body: [RID](class_rid.md#class_RID), priority: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_collision_priority)

Overridable version of [PhysicsServer2D.body_set_collision_priority()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_collision_priority).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_constant_force"></span>

void **_body_set_constant_force** ( body: [RID](class_rid.md#class_RID), force: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_constant_force)

Overridable version of [PhysicsServer2D.body_set_constant_force()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_constant_force).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_constant_torque"></span>

void **_body_set_constant_torque** ( body: [RID](class_rid.md#class_RID), torque: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_constant_torque)

Overridable version of [PhysicsServer2D.body_set_constant_torque()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_constant_torque).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_contacts_reported_depth_threshold"></span>

void **_body_set_contacts_reported_depth_threshold** ( body: [RID](class_rid.md#class_RID), threshold: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_contacts_reported_depth_threshold)

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `body_set_contacts_reported_depth_threshold` method.

 **Note:** This method is currently unused by Godot's default physics implementation.

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_continuous_collision_detection_mode"></span>

void **_body_set_continuous_collision_detection_mode** ( body: [RID](class_rid.md#class_RID), mode: [CCDMode](class_physicsserver2d.md#enum_PhysicsServer2D_CCDMode) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_continuous_collision_detection_mode)

Overridable version of [PhysicsServer2D.body_set_continuous_collision_detection_mode()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_continuous_collision_detection_mode).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_force_integration_callback"></span>

void **_body_set_force_integration_callback** ( body: [RID](class_rid.md#class_RID), callable: [Callable](class_callable.md#class_Callable), userdata: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_force_integration_callback)

Overridable version of [PhysicsServer2D.body_set_force_integration_callback()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_force_integration_callback).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_max_contacts_reported"></span>

void **_body_set_max_contacts_reported** ( body: [RID](class_rid.md#class_RID), amount: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_max_contacts_reported)

Overridable version of [PhysicsServer2D.body_set_max_contacts_reported()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_max_contacts_reported).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_mode"></span>

void **_body_set_mode** ( body: [RID](class_rid.md#class_RID), mode: [BodyMode](class_physicsserver2d.md#enum_PhysicsServer2D_BodyMode) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_mode)

Overridable version of [PhysicsServer2D.body_set_mode()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_mode).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_omit_force_integration"></span>

void **_body_set_omit_force_integration** ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_omit_force_integration)

Overridable version of [PhysicsServer2D.body_set_omit_force_integration()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_omit_force_integration).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_param"></span>

void **_body_set_param** ( body: [RID](class_rid.md#class_RID), param: [BodyParameter](class_physicsserver2d.md#enum_PhysicsServer2D_BodyParameter), value: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_param)

Overridable version of [PhysicsServer2D.body_set_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_param).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_pickable"></span>

void **_body_set_pickable** ( body: [RID](class_rid.md#class_RID), pickable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_pickable)

If set to `true`, allows the body with the given [RID](class_rid.md#class_RID) to detect mouse inputs when the mouse cursor is hovering on it.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `body_set_pickable` method. Corresponds to [CollisionObject2D.input_pickable](class_collisionobject2d.md#class_CollisionObject2D_property_input_pickable).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_shape"></span>

void **_body_set_shape** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_shape)

Overridable version of [PhysicsServer2D.body_set_shape()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_shape_as_one_way_collision"></span>

void **_body_set_shape_as_one_way_collision** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), enable: [bool](class_bool.md#class_bool), margin: [float](class_float.md#class_float), direction: [Vector2](class_vector2.md#class_Vector2) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_shape_as_one_way_collision)

Overridable version of [PhysicsServer2D.body_set_shape_as_one_way_collision()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_shape_as_one_way_collision).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_shape_disabled"></span>

void **_body_set_shape_disabled** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_shape_disabled)

Overridable version of [PhysicsServer2D.body_set_shape_disabled()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_shape_disabled).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_shape_transform"></span>

void **_body_set_shape_transform** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), transform: [Transform2D](class_transform2d.md#class_Transform2D) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_shape_transform)

Overridable version of [PhysicsServer2D.body_set_shape_transform()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_shape_transform).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_space"></span>

void **_body_set_space** ( body: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_space)

Overridable version of [PhysicsServer2D.body_set_space()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_space).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_state"></span>

void **_body_set_state** ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver2d.md#enum_PhysicsServer2D_BodyState), value: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_state)

Overridable version of [PhysicsServer2D.body_set_state()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_state).

---

<span id="class_PhysicsServer2DExtension_private_method__body_set_state_sync_callback"></span>

void **_body_set_state_sync_callback** ( body: [RID](class_rid.md#class_RID), callable: [Callable](class_callable.md#class_Callable) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_set_state_sync_callback)

Assigns the `body` to call the given `callable` during the synchronization phase of the loop, before [_step()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__step) is called. See also [_sync()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__sync).

Overridable version of [PhysicsServer2D.body_set_state_sync_callback()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_set_state_sync_callback).

---

<span id="class_PhysicsServer2DExtension_private_method__body_test_motion"></span>

[bool](class_bool.md#class_bool) **_body_test_motion** ( body: [RID](class_rid.md#class_RID), from: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collide_separation_ray: [bool](class_bool.md#class_bool), recovery_as_collision: [bool](class_bool.md#class_bool), result: `PhysicsServer2DExtensionMotionResult*` ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_test_motion)

Overridable version of [PhysicsServer2D.body_test_motion()](class_physicsserver2d.md#class_PhysicsServer2D_method_body_test_motion). Unlike the exposed implementation, this method does not receive all of the arguments inside a [PhysicsTestMotionParameters2D](class_physicstestmotionparameters2d.md#class_PhysicsTestMotionParameters2D).

---

<span id="class_PhysicsServer2DExtension_private_method__capsule_shape_create"></span>

[RID](class_rid.md#class_RID) **_capsule_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__capsule_shape_create)

Overridable version of [PhysicsServer2D.capsule_shape_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_capsule_shape_create).

---

<span id="class_PhysicsServer2DExtension_private_method__circle_shape_create"></span>

[RID](class_rid.md#class_RID) **_circle_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__circle_shape_create)

Overridable version of [PhysicsServer2D.circle_shape_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_circle_shape_create).

---

<span id="class_PhysicsServer2DExtension_private_method__concave_polygon_shape_create"></span>

[RID](class_rid.md#class_RID) **_concave_polygon_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__concave_polygon_shape_create)

Overridable version of [PhysicsServer2D.concave_polygon_shape_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_concave_polygon_shape_create).

---

<span id="class_PhysicsServer2DExtension_private_method__convex_polygon_shape_create"></span>

[RID](class_rid.md#class_RID) **_convex_polygon_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__convex_polygon_shape_create)

Overridable version of [PhysicsServer2D.convex_polygon_shape_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_convex_polygon_shape_create).

---

<span id="class_PhysicsServer2DExtension_private_method__damped_spring_joint_get_param"></span>

[float](class_float.md#class_float) **_damped_spring_joint_get_param** ( joint: [RID](class_rid.md#class_RID), param: [DampedSpringParam](class_physicsserver2d.md#enum_PhysicsServer2D_DampedSpringParam) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__damped_spring_joint_get_param)

Overridable version of [PhysicsServer2D.damped_spring_joint_get_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_damped_spring_joint_get_param).

---

<span id="class_PhysicsServer2DExtension_private_method__damped_spring_joint_set_param"></span>

void **_damped_spring_joint_set_param** ( joint: [RID](class_rid.md#class_RID), param: [DampedSpringParam](class_physicsserver2d.md#enum_PhysicsServer2D_DampedSpringParam), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__damped_spring_joint_set_param)

Overridable version of [PhysicsServer2D.damped_spring_joint_set_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_damped_spring_joint_set_param).

---

<span id="class_PhysicsServer2DExtension_private_method__end_sync"></span>

void **_end_sync** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__end_sync)

Called to indicate that the physics server has stopped synchronizing. It is in the loop's iteration/physics phase, and can access physics objects even if running on a separate thread. See also [_sync()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__sync).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `end_sync` method.

---

<span id="class_PhysicsServer2DExtension_private_method__finish"></span>

void **_finish** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__finish)

Called when the main loop finalizes to shut down the physics server. See also [MainLoop._finalize()](class_mainloop.md#class_MainLoop_private_method__finalize) and [_init()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__init).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `finish` method.

---

<span id="class_PhysicsServer2DExtension_private_method__flush_queries"></span>

void **_flush_queries** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__flush_queries)

Called every physics step before [_step()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__step) to process all remaining queries.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `flush_queries` method.

---

<span id="class_PhysicsServer2DExtension_private_method__free_rid"></span>

void **_free_rid** ( rid: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__free_rid)

Overridable version of [PhysicsServer2D.free_rid()](class_physicsserver2d.md#class_PhysicsServer2D_method_free_rid).

---

<span id="class_PhysicsServer2DExtension_private_method__get_process_info"></span>

[int](class_int.md#class_int) **_get_process_info** ( process_info: [ProcessInfo](class_physicsserver2d.md#enum_PhysicsServer2D_ProcessInfo) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__get_process_info)

Overridable version of [PhysicsServer2D.get_process_info()](class_physicsserver2d.md#class_PhysicsServer2D_method_get_process_info).

---

<span id="class_PhysicsServer2DExtension_private_method__init"></span>

void **_init** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__init)

Called when the main loop is initialized and creates a new instance of this physics server. See also [MainLoop._initialize()](class_mainloop.md#class_MainLoop_private_method__initialize) and [_finish()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__finish).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `init` method.

---

<span id="class_PhysicsServer2DExtension_private_method__is_flushing_queries"></span>

[bool](class_bool.md#class_bool) **_is_flushing_queries** ( ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__is_flushing_queries)

Overridable method that should return `true` when the physics server is processing queries. See also [_flush_queries()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__flush_queries).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `is_flushing_queries` method.

---

<span id="class_PhysicsServer2DExtension_private_method__joint_clear"></span>

void **_joint_clear** ( joint: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_clear)

Overridable version of [PhysicsServer2D.joint_clear()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_clear).

---

<span id="class_PhysicsServer2DExtension_private_method__joint_create"></span>

[RID](class_rid.md#class_RID) **_joint_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_create)

Overridable version of [PhysicsServer2D.joint_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_create).

---

<span id="class_PhysicsServer2DExtension_private_method__joint_disable_collisions_between_bodies"></span>

void **_joint_disable_collisions_between_bodies** ( joint: [RID](class_rid.md#class_RID), disable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_disable_collisions_between_bodies)

Overridable version of [PhysicsServer2D.joint_disable_collisions_between_bodies()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_disable_collisions_between_bodies).

---

<span id="class_PhysicsServer2DExtension_private_method__joint_get_param"></span>

[float](class_float.md#class_float) **_joint_get_param** ( joint: [RID](class_rid.md#class_RID), param: [JointParam](class_physicsserver2d.md#enum_PhysicsServer2D_JointParam) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_get_param)

Overridable version of [PhysicsServer2D.joint_get_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_get_param).

---

<span id="class_PhysicsServer2DExtension_private_method__joint_get_type"></span>

[JointType](class_physicsserver2d.md#enum_PhysicsServer2D_JointType) **_joint_get_type** ( joint: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_get_type)

Overridable version of [PhysicsServer2D.joint_get_type()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_get_type).

---

<span id="class_PhysicsServer2DExtension_private_method__joint_is_disabled_collisions_between_bodies"></span>

[bool](class_bool.md#class_bool) **_joint_is_disabled_collisions_between_bodies** ( joint: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_is_disabled_collisions_between_bodies)

Overridable version of [PhysicsServer2D.joint_is_disabled_collisions_between_bodies()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_is_disabled_collisions_between_bodies).

---

<span id="class_PhysicsServer2DExtension_private_method__joint_make_damped_spring"></span>

void **_joint_make_damped_spring** ( joint: [RID](class_rid.md#class_RID), anchor_a: [Vector2](class_vector2.md#class_Vector2), anchor_b: [Vector2](class_vector2.md#class_Vector2), body_a: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_make_damped_spring)

Overridable version of [PhysicsServer2D.joint_make_damped_spring()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_make_damped_spring).

---

<span id="class_PhysicsServer2DExtension_private_method__joint_make_groove"></span>

void **_joint_make_groove** ( joint: [RID](class_rid.md#class_RID), a_groove1: [Vector2](class_vector2.md#class_Vector2), a_groove2: [Vector2](class_vector2.md#class_Vector2), b_anchor: [Vector2](class_vector2.md#class_Vector2), body_a: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_make_groove)

Overridable version of [PhysicsServer2D.joint_make_groove()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_make_groove).

---

<span id="class_PhysicsServer2DExtension_private_method__joint_make_pin"></span>

void **_joint_make_pin** ( joint: [RID](class_rid.md#class_RID), anchor: [Vector2](class_vector2.md#class_Vector2), body_a: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_make_pin)

Overridable version of [PhysicsServer2D.joint_make_pin()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_make_pin).

---

<span id="class_PhysicsServer2DExtension_private_method__joint_set_param"></span>

void **_joint_set_param** ( joint: [RID](class_rid.md#class_RID), param: [JointParam](class_physicsserver2d.md#enum_PhysicsServer2D_JointParam), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__joint_set_param)

Overridable version of [PhysicsServer2D.joint_set_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_joint_set_param).

---

<span id="class_PhysicsServer2DExtension_private_method__pin_joint_get_flag"></span>

[bool](class_bool.md#class_bool) **_pin_joint_get_flag** ( joint: [RID](class_rid.md#class_RID), flag: [PinJointFlag](class_physicsserver2d.md#enum_PhysicsServer2D_PinJointFlag) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__pin_joint_get_flag)

Overridable version of [PhysicsServer2D.pin_joint_get_flag()](class_physicsserver2d.md#class_PhysicsServer2D_method_pin_joint_get_flag).

---

<span id="class_PhysicsServer2DExtension_private_method__pin_joint_get_param"></span>

[float](class_float.md#class_float) **_pin_joint_get_param** ( joint: [RID](class_rid.md#class_RID), param: [PinJointParam](class_physicsserver2d.md#enum_PhysicsServer2D_PinJointParam) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__pin_joint_get_param)

Overridable version of [PhysicsServer2D.pin_joint_get_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_pin_joint_get_param).

---

<span id="class_PhysicsServer2DExtension_private_method__pin_joint_set_flag"></span>

void **_pin_joint_set_flag** ( joint: [RID](class_rid.md#class_RID), flag: [PinJointFlag](class_physicsserver2d.md#enum_PhysicsServer2D_PinJointFlag), enabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__pin_joint_set_flag)

Overridable version of [PhysicsServer2D.pin_joint_set_flag()](class_physicsserver2d.md#class_PhysicsServer2D_method_pin_joint_set_flag).

---

<span id="class_PhysicsServer2DExtension_private_method__pin_joint_set_param"></span>

void **_pin_joint_set_param** ( joint: [RID](class_rid.md#class_RID), param: [PinJointParam](class_physicsserver2d.md#enum_PhysicsServer2D_PinJointParam), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__pin_joint_set_param)

Overridable version of [PhysicsServer2D.pin_joint_set_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_pin_joint_set_param).

---

<span id="class_PhysicsServer2DExtension_private_method__rectangle_shape_create"></span>

[RID](class_rid.md#class_RID) **_rectangle_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__rectangle_shape_create)

Overridable version of [PhysicsServer2D.rectangle_shape_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_rectangle_shape_create).

---

<span id="class_PhysicsServer2DExtension_private_method__segment_shape_create"></span>

[RID](class_rid.md#class_RID) **_segment_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__segment_shape_create)

Overridable version of [PhysicsServer2D.segment_shape_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_segment_shape_create).

---

<span id="class_PhysicsServer2DExtension_private_method__separation_ray_shape_create"></span>

[RID](class_rid.md#class_RID) **_separation_ray_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__separation_ray_shape_create)

Overridable version of [PhysicsServer2D.separation_ray_shape_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_separation_ray_shape_create).

---

<span id="class_PhysicsServer2DExtension_private_method__set_active"></span>

void **_set_active** ( active: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__set_active)

Overridable version of [PhysicsServer2D.set_active()](class_physicsserver2d.md#class_PhysicsServer2D_method_set_active).

---

<span id="class_PhysicsServer2DExtension_private_method__shape_collide"></span>

[bool](class_bool.md#class_bool) **_shape_collide** ( shape_A: [RID](class_rid.md#class_RID), xform_A: [Transform2D](class_transform2d.md#class_Transform2D), motion_A: [Vector2](class_vector2.md#class_Vector2), shape_B: [RID](class_rid.md#class_RID), xform_B: [Transform2D](class_transform2d.md#class_Transform2D), motion_B: [Vector2](class_vector2.md#class_Vector2), results: `void*`, result_max: [int](class_int.md#class_int), result_count: `int32_t*` ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_collide)

Given two shapes and their parameters, should return `true` if a collision between the two would occur, with additional details passed in `results`.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `shape_collide` method. Corresponds to [PhysicsDirectSpaceState2D.collide_shape()](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D_method_collide_shape).

---

<span id="class_PhysicsServer2DExtension_private_method__shape_get_custom_solver_bias"></span>

[float](class_float.md#class_float) **_shape_get_custom_solver_bias** ( shape: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_get_custom_solver_bias)

Should return the custom solver bias of the given `shape`, which defines how much bodies are forced to separate on contact when this shape is involved.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `shape_get_custom_solver_bias` method. Corresponds to [Shape2D.custom_solver_bias](class_shape2d.md#class_Shape2D_property_custom_solver_bias).

---

<span id="class_PhysicsServer2DExtension_private_method__shape_get_data"></span>

[Variant](class_variant.md#class_Variant) **_shape_get_data** ( shape: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_get_data)

Overridable version of [PhysicsServer2D.shape_get_data()](class_physicsserver2d.md#class_PhysicsServer2D_method_shape_get_data).

---

<span id="class_PhysicsServer2DExtension_private_method__shape_get_type"></span>

[ShapeType](class_physicsserver2d.md#enum_PhysicsServer2D_ShapeType) **_shape_get_type** ( shape: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_get_type)

Overridable version of [PhysicsServer2D.shape_get_type()](class_physicsserver2d.md#class_PhysicsServer2D_method_shape_get_type).

---

<span id="class_PhysicsServer2DExtension_private_method__shape_set_custom_solver_bias"></span>

void **_shape_set_custom_solver_bias** ( shape: [RID](class_rid.md#class_RID), bias: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_set_custom_solver_bias)

Should set the custom solver bias for the given `shape`. It defines how much bodies are forced to separate on contact.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `shape_get_custom_solver_bias` method. Corresponds to [Shape2D.custom_solver_bias](class_shape2d.md#class_Shape2D_property_custom_solver_bias).

---

<span id="class_PhysicsServer2DExtension_private_method__shape_set_data"></span>

void **_shape_set_data** ( shape: [RID](class_rid.md#class_RID), data: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__shape_set_data)

Overridable version of [PhysicsServer2D.shape_set_data()](class_physicsserver2d.md#class_PhysicsServer2D_method_shape_set_data).

---

<span id="class_PhysicsServer2DExtension_private_method__space_create"></span>

[RID](class_rid.md#class_RID) **_space_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_create)

Overridable version of [PhysicsServer2D.space_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_space_create).

---

<span id="class_PhysicsServer2DExtension_private_method__space_get_contact_count"></span>

[int](class_int.md#class_int) **_space_get_contact_count** ( space: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_contact_count)

Should return how many contacts have occurred during the last physics step in the given `space`. See also [_space_get_contacts()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_contacts) and [_space_set_debug_contacts()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_set_debug_contacts).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `space_get_contact_count` method.

---

<span id="class_PhysicsServer2DExtension_private_method__space_get_contacts"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **_space_get_contacts** ( space: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_contacts)

Should return the positions of all contacts that have occurred during the last physics step in the given `space`. See also [_space_get_contact_count()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_contact_count) and [_space_set_debug_contacts()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_set_debug_contacts).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `space_get_contacts` method.

---

<span id="class_PhysicsServer2DExtension_private_method__space_get_direct_state"></span>

[PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) **_space_get_direct_state** ( space: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_direct_state)

Overridable version of [PhysicsServer2D.space_get_direct_state()](class_physicsserver2d.md#class_PhysicsServer2D_method_space_get_direct_state).

---

<span id="class_PhysicsServer2DExtension_private_method__space_get_param"></span>

[float](class_float.md#class_float) **_space_get_param** ( space: [RID](class_rid.md#class_RID), param: [SpaceParameter](class_physicsserver2d.md#enum_PhysicsServer2D_SpaceParameter) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_get_param)

Overridable version of [PhysicsServer2D.space_get_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_space_get_param).

---

<span id="class_PhysicsServer2DExtension_private_method__space_is_active"></span>

[bool](class_bool.md#class_bool) **_space_is_active** ( space: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_is_active)

Overridable version of [PhysicsServer2D.space_is_active()](class_physicsserver2d.md#class_PhysicsServer2D_method_space_is_active).

---

<span id="class_PhysicsServer2DExtension_private_method__space_set_active"></span>

void **_space_set_active** ( space: [RID](class_rid.md#class_RID), active: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_set_active)

Overridable version of [PhysicsServer2D.space_set_active()](class_physicsserver2d.md#class_PhysicsServer2D_method_space_set_active).

---

<span id="class_PhysicsServer2DExtension_private_method__space_set_debug_contacts"></span>

void **_space_set_debug_contacts** ( space: [RID](class_rid.md#class_RID), max_contacts: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_set_debug_contacts)

Used internally to allow the given `space` to store contact points, up to `max_contacts`. This is automatically set for the main [World2D](class_world2d.md#class_World2D)'s space when [SceneTree.debug_collisions_hint](class_scenetree.md#class_SceneTree_property_debug_collisions_hint) is `true`, or by checking "Visible Collision Shapes" in the editor. Only works in debug builds.

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `space_set_debug_contacts` method.

---

<span id="class_PhysicsServer2DExtension_private_method__space_set_param"></span>

void **_space_set_param** ( space: [RID](class_rid.md#class_RID), param: [SpaceParameter](class_physicsserver2d.md#enum_PhysicsServer2D_SpaceParameter), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__space_set_param)

Overridable version of [PhysicsServer2D.space_set_param()](class_physicsserver2d.md#class_PhysicsServer2D_method_space_set_param).

---

<span id="class_PhysicsServer2DExtension_private_method__step"></span>

void **_step** ( step: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__step)

Called every physics step to process the physics simulation. `step` is the time elapsed since the last physics step, in seconds. It is usually the same as the value returned by [Node.get_physics_process_delta_time()](class_node.md#class_Node_method_get_physics_process_delta_time).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `step` method.

---

<span id="class_PhysicsServer2DExtension_private_method__sync"></span>

void **_sync** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__sync)

Called to indicate that the physics server is synchronizing and cannot access physics states if running on a separate thread. See also [_end_sync()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__end_sync).

Overridable version of [PhysicsServer2D](class_physicsserver2d.md#class_PhysicsServer2D)'s internal `sync` method.

---

<span id="class_PhysicsServer2DExtension_private_method__world_boundary_shape_create"></span>

[RID](class_rid.md#class_RID) **_world_boundary_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__world_boundary_shape_create)

Overridable version of [PhysicsServer2D.world_boundary_shape_create()](class_physicsserver2d.md#class_PhysicsServer2D_method_world_boundary_shape_create).

---

<span id="class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_body"></span>

[bool](class_bool.md#class_bool) **body_test_motion_is_excluding_body** ( body: [RID](class_rid.md#class_RID) ) *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_body)

Returns `true` if the body with the given [RID](class_rid.md#class_RID) is being excluded from [_body_test_motion()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_test_motion). See also [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id).

---

<span id="class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_object"></span>

[bool](class_bool.md#class_bool) **body_test_motion_is_excluding_object** ( object: [int](class_int.md#class_int) ) *const* [🔗](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_object)

Returns `true` if the object with the given instance ID is being excluded from [_body_test_motion()](class_physicsserver2dextension.md#class_PhysicsServer2DExtension_private_method__body_test_motion). See also [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id).
