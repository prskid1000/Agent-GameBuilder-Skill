<span id="class_PhysicsServer3DExtension"></span>

## PhysicsServer3DExtension

**Inherits:** [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) **<** [Object](class_object.md#class_Object)

Provides virtual methods that can be overridden to create custom [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) implementations.

### Description

This class extends [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D).

### Methods


| void | [_area_add_shape](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_add_shape) ( area: [RID](class_rid.md#class_RID), shape: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), disabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| --- | --- | --- | --- |
| void | [_area_attach_object_instance_id](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_attach_object_instance_id) ( area: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) | virtual | required |
| void | [_area_clear_shapes](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_clear_shapes) ( area: [RID](class_rid.md#class_RID) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_area_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_create) ( ) | virtual | required |
| [int](class_int.md#class_int) | [_area_get_collision_layer](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_collision_layer) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_area_get_collision_mask](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_collision_mask) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_area_get_object_instance_id](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_object_instance_id) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_area_get_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_param) ( area: [RID](class_rid.md#class_RID), param: [AreaParameter](class_physicsserver3d.md#enum_PhysicsServer3D_AreaParameter) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_area_get_shape](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_shape) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_area_get_shape_count](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_shape_count) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [_area_get_shape_transform](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_shape_transform) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_area_get_space](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_space) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [_area_get_transform](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_transform) ( area: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_area_remove_shape](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_remove_shape) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required |
| void | [_area_set_area_monitor_callback](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_area_monitor_callback) ( area: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) | virtual | required |
| void | [_area_set_collision_layer](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_collision_layer) ( area: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) | virtual | required |
| void | [_area_set_collision_mask](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_collision_mask) ( area: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) | virtual | required |
| void | [_area_set_monitor_callback](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_monitor_callback) ( area: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) | virtual | required |
| void | [_area_set_monitorable](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_monitorable) ( area: [RID](class_rid.md#class_RID), monitorable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_area_set_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_param) ( area: [RID](class_rid.md#class_RID), param: [AreaParameter](class_physicsserver3d.md#enum_PhysicsServer3D_AreaParameter), value: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_area_set_ray_pickable](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_ray_pickable) ( area: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_area_set_shape](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_shape) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_area_set_shape_disabled](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_shape_disabled) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_area_set_shape_transform](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_shape_transform) ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) | virtual | required |
| void | [_area_set_space](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_space) ( area: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_area_set_transform](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_transform) ( area: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) | virtual | required |
| void | [_body_add_collision_exception](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_collision_exception) ( body: [RID](class_rid.md#class_RID), excepted_body: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_add_constant_central_force](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_constant_central_force) ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_add_constant_force](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_constant_force) ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_add_constant_torque](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_constant_torque) ( body: [RID](class_rid.md#class_RID), torque: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_add_shape](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_shape) ( body: [RID](class_rid.md#class_RID), shape: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), disabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_apply_central_force](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_central_force) ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_apply_central_impulse](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_central_impulse) ( body: [RID](class_rid.md#class_RID), impulse: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_apply_force](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_force) ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_apply_impulse](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_impulse) ( body: [RID](class_rid.md#class_RID), impulse: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_apply_torque](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_torque) ( body: [RID](class_rid.md#class_RID), torque: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_apply_torque_impulse](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_torque_impulse) ( body: [RID](class_rid.md#class_RID), impulse: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_attach_object_instance_id](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_attach_object_instance_id) ( body: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_clear_shapes](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_clear_shapes) ( body: [RID](class_rid.md#class_RID) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_body_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_create) ( ) | virtual | required |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [_body_get_collision_exceptions](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_collision_exceptions) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_body_get_collision_layer](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_collision_layer) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_body_get_collision_mask](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_collision_mask) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_body_get_collision_priority](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_collision_priority) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_body_get_constant_force](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_constant_force) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_body_get_constant_torque](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_constant_torque) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_body_get_contacts_reported_depth_threshold](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_contacts_reported_depth_threshold) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class_PhysicsDirectBodyState3D) | [_body_get_direct_state](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_direct_state) ( body: [RID](class_rid.md#class_RID) ) | virtual | required |
| [int](class_int.md#class_int) | [_body_get_max_contacts_reported](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_max_contacts_reported) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [BodyMode](class_physicsserver3d.md#enum_PhysicsServer3D_BodyMode) | [_body_get_mode](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_mode) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_body_get_object_instance_id](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_object_instance_id) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_body_get_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_param) ( body: [RID](class_rid.md#class_RID), param: [BodyParameter](class_physicsserver3d.md#enum_PhysicsServer3D_BodyParameter) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_body_get_shape](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_shape) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_body_get_shape_count](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_shape_count) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [_body_get_shape_transform](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_shape_transform) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_body_get_space](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_space) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_body_get_state](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_state) ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver3d.md#enum_PhysicsServer3D_BodyState) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_body_get_user_flags](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_user_flags) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_body_is_axis_locked](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_is_axis_locked) ( body: [RID](class_rid.md#class_RID), axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_body_is_continuous_collision_detection_enabled](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_is_continuous_collision_detection_enabled) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_body_is_omitting_force_integration](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_is_omitting_force_integration) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_body_remove_collision_exception](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_remove_collision_exception) ( body: [RID](class_rid.md#class_RID), excepted_body: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_remove_shape](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_remove_shape) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_reset_mass_properties](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_reset_mass_properties) ( body: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_set_axis_lock](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_axis_lock) ( body: [RID](class_rid.md#class_RID), axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_set_axis_velocity](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_axis_velocity) ( body: [RID](class_rid.md#class_RID), axis_velocity: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_set_collision_layer](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_collision_layer) ( body: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_set_collision_mask](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_collision_mask) ( body: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_set_collision_priority](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_collision_priority) ( body: [RID](class_rid.md#class_RID), priority: [float](class_float.md#class_float) ) | virtual | required |
| void | [_body_set_constant_force](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_constant_force) ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_set_constant_torque](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_constant_torque) ( body: [RID](class_rid.md#class_RID), torque: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_body_set_contacts_reported_depth_threshold](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_contacts_reported_depth_threshold) ( body: [RID](class_rid.md#class_RID), threshold: [float](class_float.md#class_float) ) | virtual | required |
| void | [_body_set_enable_continuous_collision_detection](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_enable_continuous_collision_detection) ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_set_force_integration_callback](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_force_integration_callback) ( body: [RID](class_rid.md#class_RID), callable: [Callable](class_callable.md#class_Callable), userdata: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_body_set_max_contacts_reported](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_max_contacts_reported) ( body: [RID](class_rid.md#class_RID), amount: [int](class_int.md#class_int) ) | virtual | required |
| void | [_body_set_mode](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_mode) ( body: [RID](class_rid.md#class_RID), mode: [BodyMode](class_physicsserver3d.md#enum_PhysicsServer3D_BodyMode) ) | virtual | required |
| void | [_body_set_omit_force_integration](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_omit_force_integration) ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_set_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_param) ( body: [RID](class_rid.md#class_RID), param: [BodyParameter](class_physicsserver3d.md#enum_PhysicsServer3D_BodyParameter), value: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_body_set_ray_pickable](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_ray_pickable) ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_set_shape](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_shape) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_set_shape_disabled](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_shape_disabled) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_body_set_shape_transform](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_shape_transform) ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) | virtual | required |
| void | [_body_set_space](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_space) ( body: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_body_set_state](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_state) ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver3d.md#enum_PhysicsServer3D_BodyState), value: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_body_set_state_sync_callback](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_state_sync_callback) ( body: [RID](class_rid.md#class_RID), callable: [Callable](class_callable.md#class_Callable) ) | virtual | required |
| void | [_body_set_user_flags](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_user_flags) ( body: [RID](class_rid.md#class_RID), flags: [int](class_int.md#class_int) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_body_test_motion](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_test_motion) ( body: [RID](class_rid.md#class_RID), from: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), max_collisions: [int](class_int.md#class_int), collide_separation_ray: [bool](class_bool.md#class_bool), recovery_as_collision: [bool](class_bool.md#class_bool), result: `PhysicsServer3DExtensionMotionResult*` ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_box_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__box_shape_create) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_capsule_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__capsule_shape_create) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_concave_polygon_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__concave_polygon_shape_create) ( ) | virtual | required |
| [float](class_float.md#class_float) | [_cone_twist_joint_get_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__cone_twist_joint_get_param) ( joint: [RID](class_rid.md#class_RID), param: [ConeTwistJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_ConeTwistJointParam) ) | virtual | required | const |
| void | [_cone_twist_joint_set_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__cone_twist_joint_set_param) ( joint: [RID](class_rid.md#class_RID), param: [ConeTwistJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_ConeTwistJointParam), value: [float](class_float.md#class_float) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_convex_polygon_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__convex_polygon_shape_create) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_custom_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__custom_shape_create) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_cylinder_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__cylinder_shape_create) ( ) | virtual | required |
| void | [_end_sync](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__end_sync) ( ) | virtual | required |
| void | [_finish](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__finish) ( ) | virtual | required |
| void | [_flush_queries](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__flush_queries) ( ) | virtual | required |
| void | [_free_rid](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__free_rid) ( rid: [RID](class_rid.md#class_RID) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_generic_6dof_joint_get_flag](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_flag) ( joint: [RID](class_rid.md#class_RID), axis: [Axis](class_vector3.md#enum_Vector3_Axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum_PhysicsServer3D_G6DOFJointAxisFlag) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_generic_6dof_joint_get_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_param) ( joint: [RID](class_rid.md#class_RID), axis: [Axis](class_vector3.md#enum_Vector3_Axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum_PhysicsServer3D_G6DOFJointAxisParam) ) | virtual | required | const |
| void | [_generic_6dof_joint_set_flag](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_flag) ( joint: [RID](class_rid.md#class_RID), axis: [Axis](class_vector3.md#enum_Vector3_Axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum_PhysicsServer3D_G6DOFJointAxisFlag), enable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_generic_6dof_joint_set_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_param) ( joint: [RID](class_rid.md#class_RID), axis: [Axis](class_vector3.md#enum_Vector3_Axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum_PhysicsServer3D_G6DOFJointAxisParam), value: [float](class_float.md#class_float) ) | virtual | required |
| [int](class_int.md#class_int) | [_get_process_info](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__get_process_info) ( process_info: [ProcessInfo](class_physicsserver3d.md#enum_PhysicsServer3D_ProcessInfo) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_heightmap_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__heightmap_shape_create) ( ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_hinge_joint_get_flag](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__hinge_joint_get_flag) ( joint: [RID](class_rid.md#class_RID), flag: [HingeJointFlag](class_physicsserver3d.md#enum_PhysicsServer3D_HingeJointFlag) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_hinge_joint_get_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__hinge_joint_get_param) ( joint: [RID](class_rid.md#class_RID), param: [HingeJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_HingeJointParam) ) | virtual | required | const |
| void | [_hinge_joint_set_flag](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__hinge_joint_set_flag) ( joint: [RID](class_rid.md#class_RID), flag: [HingeJointFlag](class_physicsserver3d.md#enum_PhysicsServer3D_HingeJointFlag), enabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_hinge_joint_set_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__hinge_joint_set_param) ( joint: [RID](class_rid.md#class_RID), param: [HingeJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_HingeJointParam), value: [float](class_float.md#class_float) ) | virtual | required |
| void | [_init](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__init) ( ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_is_flushing_queries](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__is_flushing_queries) ( ) | virtual | required | const |
| void | [_joint_clear](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_clear) ( joint: [RID](class_rid.md#class_RID) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_joint_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_create) ( ) | virtual | required |
| void | [_joint_disable_collisions_between_bodies](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_disable_collisions_between_bodies) ( joint: [RID](class_rid.md#class_RID), disable: [bool](class_bool.md#class_bool) ) | virtual | required |
| [int](class_int.md#class_int) | [_joint_get_solver_priority](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_get_solver_priority) ( joint: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [JointType](class_physicsserver3d.md#enum_PhysicsServer3D_JointType) | [_joint_get_type](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_get_type) ( joint: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_joint_is_disabled_collisions_between_bodies](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_is_disabled_collisions_between_bodies) ( joint: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_joint_make_cone_twist](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_cone_twist) ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), local_ref_A: [Transform3D](class_transform3d.md#class_Transform3D), body_B: [RID](class_rid.md#class_RID), local_ref_B: [Transform3D](class_transform3d.md#class_Transform3D) ) | virtual | required |
| void | [_joint_make_generic_6dof](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_generic_6dof) ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), local_ref_A: [Transform3D](class_transform3d.md#class_Transform3D), body_B: [RID](class_rid.md#class_RID), local_ref_B: [Transform3D](class_transform3d.md#class_Transform3D) ) | virtual | required |
| void | [_joint_make_hinge](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_hinge) ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), hinge_A: [Transform3D](class_transform3d.md#class_Transform3D), body_B: [RID](class_rid.md#class_RID), hinge_B: [Transform3D](class_transform3d.md#class_Transform3D) ) | virtual | required |
| void | [_joint_make_hinge_simple](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_hinge_simple) ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), pivot_A: [Vector3](class_vector3.md#class_Vector3), axis_A: [Vector3](class_vector3.md#class_Vector3), body_B: [RID](class_rid.md#class_RID), pivot_B: [Vector3](class_vector3.md#class_Vector3), axis_B: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_joint_make_pin](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_pin) ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), local_A: [Vector3](class_vector3.md#class_Vector3), body_B: [RID](class_rid.md#class_RID), local_B: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_joint_make_slider](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_slider) ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), local_ref_A: [Transform3D](class_transform3d.md#class_Transform3D), body_B: [RID](class_rid.md#class_RID), local_ref_B: [Transform3D](class_transform3d.md#class_Transform3D) ) | virtual | required |
| void | [_joint_set_solver_priority](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_set_solver_priority) ( joint: [RID](class_rid.md#class_RID), priority: [int](class_int.md#class_int) ) | virtual | required |
| [Vector3](class_vector3.md#class_Vector3) | [_pin_joint_get_local_a](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_get_local_a) ( joint: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_pin_joint_get_local_b](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_get_local_b) ( joint: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_pin_joint_get_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_get_param) ( joint: [RID](class_rid.md#class_RID), param: [PinJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_PinJointParam) ) | virtual | required | const |
| void | [_pin_joint_set_local_a](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_set_local_a) ( joint: [RID](class_rid.md#class_RID), local_A: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_pin_joint_set_local_b](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_set_local_b) ( joint: [RID](class_rid.md#class_RID), local_B: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_pin_joint_set_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_set_param) ( joint: [RID](class_rid.md#class_RID), param: [PinJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_PinJointParam), value: [float](class_float.md#class_float) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_separation_ray_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__separation_ray_shape_create) ( ) | virtual | required |
| void | [_set_active](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__set_active) ( active: [bool](class_bool.md#class_bool) ) | virtual | required |
| [float](class_float.md#class_float) | [_shape_get_custom_solver_bias](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_get_custom_solver_bias) ( shape: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_shape_get_data](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_get_data) ( shape: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_shape_get_margin](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_get_margin) ( shape: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [ShapeType](class_physicsserver3d.md#enum_PhysicsServer3D_ShapeType) | [_shape_get_type](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_get_type) ( shape: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_shape_set_custom_solver_bias](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_set_custom_solver_bias) ( shape: [RID](class_rid.md#class_RID), bias: [float](class_float.md#class_float) ) | virtual | required |
| void | [_shape_set_data](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_set_data) ( shape: [RID](class_rid.md#class_RID), data: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_shape_set_margin](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_set_margin) ( shape: [RID](class_rid.md#class_RID), margin: [float](class_float.md#class_float) ) | virtual | required |
| [float](class_float.md#class_float) | [_slider_joint_get_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__slider_joint_get_param) ( joint: [RID](class_rid.md#class_RID), param: [SliderJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_SliderJointParam) ) | virtual | required | const |
| void | [_slider_joint_set_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__slider_joint_set_param) ( joint: [RID](class_rid.md#class_RID), param: [SliderJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_SliderJointParam), value: [float](class_float.md#class_float) ) | virtual | required |
| void | [_soft_body_add_collision_exception](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_add_collision_exception) ( body: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_soft_body_apply_central_force](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_apply_central_force) ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_soft_body_apply_central_impulse](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_apply_central_impulse) ( body: [RID](class_rid.md#class_RID), impulse: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_soft_body_apply_point_force](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_apply_point_force) ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int), force: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_soft_body_apply_point_impulse](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_apply_point_impulse) ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int), impulse: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_soft_body_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_create) ( ) | virtual | required |
| [AABB](class_aabb.md#class_AABB) | [_soft_body_get_bounds](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_bounds) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] | [_soft_body_get_collision_exceptions](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_collision_exceptions) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_soft_body_get_collision_layer](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_collision_layer) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_soft_body_get_collision_mask](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_collision_mask) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_soft_body_get_damping_coefficient](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_damping_coefficient) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_soft_body_get_drag_coefficient](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_drag_coefficient) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_soft_body_get_linear_stiffness](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_linear_stiffness) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_soft_body_get_point_global_position](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_point_global_position) ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_soft_body_get_pressure_coefficient](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_pressure_coefficient) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_soft_body_get_shrinking_factor](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_shrinking_factor) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_soft_body_get_simulation_precision](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_simulation_precision) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_soft_body_get_space](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_space) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [Variant](class_variant.md#class_Variant) | [_soft_body_get_state](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_state) ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver3d.md#enum_PhysicsServer3D_BodyState) ) | virtual | required | const |
| [float](class_float.md#class_float) | [_soft_body_get_total_mass](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_total_mass) ( body: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_soft_body_is_point_pinned](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_is_point_pinned) ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int) ) | virtual | required | const |
| void | [_soft_body_move_point](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_move_point) ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int), global_position: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_soft_body_pin_point](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_pin_point) ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int), pin: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_soft_body_remove_all_pinned_points](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_remove_all_pinned_points) ( body: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_soft_body_remove_collision_exception](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_remove_collision_exception) ( body: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_soft_body_set_collision_layer](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_collision_layer) ( body: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) | virtual | required |
| void | [_soft_body_set_collision_mask](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_collision_mask) ( body: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) | virtual | required |
| void | [_soft_body_set_damping_coefficient](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_damping_coefficient) ( body: [RID](class_rid.md#class_RID), damping_coefficient: [float](class_float.md#class_float) ) | virtual | required |
| void | [_soft_body_set_drag_coefficient](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_drag_coefficient) ( body: [RID](class_rid.md#class_RID), drag_coefficient: [float](class_float.md#class_float) ) | virtual | required |
| void | [_soft_body_set_linear_stiffness](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_linear_stiffness) ( body: [RID](class_rid.md#class_RID), linear_stiffness: [float](class_float.md#class_float) ) | virtual | required |
| void | [_soft_body_set_mesh](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_mesh) ( body: [RID](class_rid.md#class_RID), mesh: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_soft_body_set_pressure_coefficient](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_pressure_coefficient) ( body: [RID](class_rid.md#class_RID), pressure_coefficient: [float](class_float.md#class_float) ) | virtual | required |
| void | [_soft_body_set_ray_pickable](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_ray_pickable) ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_soft_body_set_shrinking_factor](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_shrinking_factor) ( body: [RID](class_rid.md#class_RID), shrinking_factor: [float](class_float.md#class_float) ) | virtual | required |
| void | [_soft_body_set_simulation_precision](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_simulation_precision) ( body: [RID](class_rid.md#class_RID), simulation_precision: [int](class_int.md#class_int) ) | virtual | required |
| void | [_soft_body_set_space](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_space) ( body: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) | virtual | required |
| void | [_soft_body_set_state](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_state) ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver3d.md#enum_PhysicsServer3D_BodyState), variant: [Variant](class_variant.md#class_Variant) ) | virtual | required |
| void | [_soft_body_set_total_mass](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_total_mass) ( body: [RID](class_rid.md#class_RID), total_mass: [float](class_float.md#class_float) ) | virtual | required |
| void | [_soft_body_set_transform](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_transform) ( body: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) | virtual | required |
| void | [_soft_body_update_rendering_server](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_update_rendering_server) ( body: [RID](class_rid.md#class_RID), rendering_server_handler: [PhysicsServer3DRenderingServerHandler](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_space_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_create) ( ) | virtual | required |
| [int](class_int.md#class_int) | [_space_get_contact_count](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_get_contact_count) ( space: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [_space_get_contacts](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_get_contacts) ( space: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) | [_space_get_direct_state](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_get_direct_state) ( space: [RID](class_rid.md#class_RID) ) | virtual | required |
| [float](class_float.md#class_float) | [_space_get_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_get_param) ( space: [RID](class_rid.md#class_RID), param: [SpaceParameter](class_physicsserver3d.md#enum_PhysicsServer3D_SpaceParameter) ) | virtual | required | const |
| [bool](class_bool.md#class_bool) | [_space_is_active](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_is_active) ( space: [RID](class_rid.md#class_RID) ) | virtual | required | const |
| void | [_space_set_active](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_set_active) ( space: [RID](class_rid.md#class_RID), active: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_space_set_debug_contacts](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_set_debug_contacts) ( space: [RID](class_rid.md#class_RID), max_contacts: [int](class_int.md#class_int) ) | virtual | required |
| void | [_space_set_param](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_set_param) ( space: [RID](class_rid.md#class_RID), param: [SpaceParameter](class_physicsserver3d.md#enum_PhysicsServer3D_SpaceParameter), value: [float](class_float.md#class_float) ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_sphere_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__sphere_shape_create) ( ) | virtual | required |
| void | [_step](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__step) ( step: [float](class_float.md#class_float) ) | virtual | required |
| void | [_sync](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__sync) ( ) | virtual | required |
| [RID](class_rid.md#class_RID) | [_world_boundary_shape_create](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__world_boundary_shape_create) ( ) | virtual | required |
| [bool](class_bool.md#class_bool) | [body_test_motion_is_excluding_body](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_body) ( body: [RID](class_rid.md#class_RID) ) const |
| [bool](class_bool.md#class_bool) | [body_test_motion_is_excluding_object](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_object) ( object: [int](class_int.md#class_int) ) const |

---

### Method Descriptions

<span id="class_PhysicsServer3DExtension_private_method__area_add_shape"></span>

void **_area_add_shape** ( area: [RID](class_rid.md#class_RID), shape: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), disabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_add_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_attach_object_instance_id"></span>

void **_area_attach_object_instance_id** ( area: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_attach_object_instance_id)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_clear_shapes"></span>

void **_area_clear_shapes** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_clear_shapes)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_create"></span>

[RID](class_rid.md#class_RID) **_area_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_get_collision_layer"></span>

[int](class_int.md#class_int) **_area_get_collision_layer** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_collision_layer)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_get_collision_mask"></span>

[int](class_int.md#class_int) **_area_get_collision_mask** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_collision_mask)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_get_object_instance_id"></span>

[int](class_int.md#class_int) **_area_get_object_instance_id** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_object_instance_id)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_get_param"></span>

[Variant](class_variant.md#class_Variant) **_area_get_param** ( area: [RID](class_rid.md#class_RID), param: [AreaParameter](class_physicsserver3d.md#enum_PhysicsServer3D_AreaParameter) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_get_shape"></span>

[RID](class_rid.md#class_RID) **_area_get_shape** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_get_shape_count"></span>

[int](class_int.md#class_int) **_area_get_shape_count** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_shape_count)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_get_shape_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **_area_get_shape_transform** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_shape_transform)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_get_space"></span>

[RID](class_rid.md#class_RID) **_area_get_space** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_space)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_get_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **_area_get_transform** ( area: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_get_transform)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_remove_shape"></span>

void **_area_remove_shape** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_remove_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_area_monitor_callback"></span>

void **_area_set_area_monitor_callback** ( area: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_area_monitor_callback)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_collision_layer"></span>

void **_area_set_collision_layer** ( area: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_collision_layer)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_collision_mask"></span>

void **_area_set_collision_mask** ( area: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_collision_mask)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_monitor_callback"></span>

void **_area_set_monitor_callback** ( area: [RID](class_rid.md#class_RID), callback: [Callable](class_callable.md#class_Callable) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_monitor_callback)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_monitorable"></span>

void **_area_set_monitorable** ( area: [RID](class_rid.md#class_RID), monitorable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_monitorable)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_param"></span>

void **_area_set_param** ( area: [RID](class_rid.md#class_RID), param: [AreaParameter](class_physicsserver3d.md#enum_PhysicsServer3D_AreaParameter), value: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_ray_pickable"></span>

void **_area_set_ray_pickable** ( area: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_ray_pickable)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_shape"></span>

void **_area_set_shape** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_shape_disabled"></span>

void **_area_set_shape_disabled** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_shape_disabled)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_shape_transform"></span>

void **_area_set_shape_transform** ( area: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_shape_transform)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_space"></span>

void **_area_set_space** ( area: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_space)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__area_set_transform"></span>

void **_area_set_transform** ( area: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__area_set_transform)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_add_collision_exception"></span>

void **_body_add_collision_exception** ( body: [RID](class_rid.md#class_RID), excepted_body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_collision_exception)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_add_constant_central_force"></span>

void **_body_add_constant_central_force** ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_constant_central_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_add_constant_force"></span>

void **_body_add_constant_force** ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_constant_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_add_constant_torque"></span>

void **_body_add_constant_torque** ( body: [RID](class_rid.md#class_RID), torque: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_constant_torque)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_add_shape"></span>

void **_body_add_shape** ( body: [RID](class_rid.md#class_RID), shape: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), disabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_add_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_apply_central_force"></span>

void **_body_apply_central_force** ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_central_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_apply_central_impulse"></span>

void **_body_apply_central_impulse** ( body: [RID](class_rid.md#class_RID), impulse: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_central_impulse)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_apply_force"></span>

void **_body_apply_force** ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_apply_impulse"></span>

void **_body_apply_impulse** ( body: [RID](class_rid.md#class_RID), impulse: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_impulse)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_apply_torque"></span>

void **_body_apply_torque** ( body: [RID](class_rid.md#class_RID), torque: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_torque)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_apply_torque_impulse"></span>

void **_body_apply_torque_impulse** ( body: [RID](class_rid.md#class_RID), impulse: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_apply_torque_impulse)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_attach_object_instance_id"></span>

void **_body_attach_object_instance_id** ( body: [RID](class_rid.md#class_RID), id: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_attach_object_instance_id)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_clear_shapes"></span>

void **_body_clear_shapes** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_clear_shapes)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_create"></span>

[RID](class_rid.md#class_RID) **_body_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_collision_exceptions"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **_body_get_collision_exceptions** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_collision_exceptions)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_collision_layer"></span>

[int](class_int.md#class_int) **_body_get_collision_layer** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_collision_layer)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_collision_mask"></span>

[int](class_int.md#class_int) **_body_get_collision_mask** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_collision_mask)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_collision_priority"></span>

[float](class_float.md#class_float) **_body_get_collision_priority** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_collision_priority)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_constant_force"></span>

[Vector3](class_vector3.md#class_Vector3) **_body_get_constant_force** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_constant_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_constant_torque"></span>

[Vector3](class_vector3.md#class_Vector3) **_body_get_constant_torque** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_constant_torque)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_contacts_reported_depth_threshold"></span>

[float](class_float.md#class_float) **_body_get_contacts_reported_depth_threshold** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_contacts_reported_depth_threshold)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_direct_state"></span>

[PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class_PhysicsDirectBodyState3D) **_body_get_direct_state** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_direct_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_max_contacts_reported"></span>

[int](class_int.md#class_int) **_body_get_max_contacts_reported** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_max_contacts_reported)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_mode"></span>

[BodyMode](class_physicsserver3d.md#enum_PhysicsServer3D_BodyMode) **_body_get_mode** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_mode)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_object_instance_id"></span>

[int](class_int.md#class_int) **_body_get_object_instance_id** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_object_instance_id)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_param"></span>

[Variant](class_variant.md#class_Variant) **_body_get_param** ( body: [RID](class_rid.md#class_RID), param: [BodyParameter](class_physicsserver3d.md#enum_PhysicsServer3D_BodyParameter) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_shape"></span>

[RID](class_rid.md#class_RID) **_body_get_shape** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_shape_count"></span>

[int](class_int.md#class_int) **_body_get_shape_count** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_shape_count)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_shape_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **_body_get_shape_transform** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_shape_transform)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_space"></span>

[RID](class_rid.md#class_RID) **_body_get_space** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_space)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_state"></span>

[Variant](class_variant.md#class_Variant) **_body_get_state** ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver3d.md#enum_PhysicsServer3D_BodyState) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_get_user_flags"></span>

[int](class_int.md#class_int) **_body_get_user_flags** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_get_user_flags)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_is_axis_locked"></span>

[bool](class_bool.md#class_bool) **_body_is_axis_locked** ( body: [RID](class_rid.md#class_RID), axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_is_axis_locked)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_is_continuous_collision_detection_enabled"></span>

[bool](class_bool.md#class_bool) **_body_is_continuous_collision_detection_enabled** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_is_continuous_collision_detection_enabled)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_is_omitting_force_integration"></span>

[bool](class_bool.md#class_bool) **_body_is_omitting_force_integration** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_is_omitting_force_integration)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_remove_collision_exception"></span>

void **_body_remove_collision_exception** ( body: [RID](class_rid.md#class_RID), excepted_body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_remove_collision_exception)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_remove_shape"></span>

void **_body_remove_shape** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_remove_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_reset_mass_properties"></span>

void **_body_reset_mass_properties** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_reset_mass_properties)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_axis_lock"></span>

void **_body_set_axis_lock** ( body: [RID](class_rid.md#class_RID), axis: [BodyAxis](class_physicsserver3d.md#enum_PhysicsServer3D_BodyAxis), lock: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_axis_lock)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_axis_velocity"></span>

void **_body_set_axis_velocity** ( body: [RID](class_rid.md#class_RID), axis_velocity: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_axis_velocity)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_collision_layer"></span>

void **_body_set_collision_layer** ( body: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_collision_layer)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_collision_mask"></span>

void **_body_set_collision_mask** ( body: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_collision_mask)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_collision_priority"></span>

void **_body_set_collision_priority** ( body: [RID](class_rid.md#class_RID), priority: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_collision_priority)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_constant_force"></span>

void **_body_set_constant_force** ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_constant_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_constant_torque"></span>

void **_body_set_constant_torque** ( body: [RID](class_rid.md#class_RID), torque: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_constant_torque)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_contacts_reported_depth_threshold"></span>

void **_body_set_contacts_reported_depth_threshold** ( body: [RID](class_rid.md#class_RID), threshold: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_contacts_reported_depth_threshold)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_enable_continuous_collision_detection"></span>

void **_body_set_enable_continuous_collision_detection** ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_enable_continuous_collision_detection)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_force_integration_callback"></span>

void **_body_set_force_integration_callback** ( body: [RID](class_rid.md#class_RID), callable: [Callable](class_callable.md#class_Callable), userdata: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_force_integration_callback)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_max_contacts_reported"></span>

void **_body_set_max_contacts_reported** ( body: [RID](class_rid.md#class_RID), amount: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_max_contacts_reported)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_mode"></span>

void **_body_set_mode** ( body: [RID](class_rid.md#class_RID), mode: [BodyMode](class_physicsserver3d.md#enum_PhysicsServer3D_BodyMode) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_mode)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_omit_force_integration"></span>

void **_body_set_omit_force_integration** ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_omit_force_integration)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_param"></span>

void **_body_set_param** ( body: [RID](class_rid.md#class_RID), param: [BodyParameter](class_physicsserver3d.md#enum_PhysicsServer3D_BodyParameter), value: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_ray_pickable"></span>

void **_body_set_ray_pickable** ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_ray_pickable)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_shape"></span>

void **_body_set_shape** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), shape: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_shape_disabled"></span>

void **_body_set_shape_disabled** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), disabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_shape_disabled)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_shape_transform"></span>

void **_body_set_shape_transform** ( body: [RID](class_rid.md#class_RID), shape_idx: [int](class_int.md#class_int), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_shape_transform)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_space"></span>

void **_body_set_space** ( body: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_space)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_state"></span>

void **_body_set_state** ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver3d.md#enum_PhysicsServer3D_BodyState), value: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_state_sync_callback"></span>

void **_body_set_state_sync_callback** ( body: [RID](class_rid.md#class_RID), callable: [Callable](class_callable.md#class_Callable) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_state_sync_callback)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_set_user_flags"></span>

void **_body_set_user_flags** ( body: [RID](class_rid.md#class_RID), flags: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_set_user_flags)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__body_test_motion"></span>

[bool](class_bool.md#class_bool) **_body_test_motion** ( body: [RID](class_rid.md#class_RID), from: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), max_collisions: [int](class_int.md#class_int), collide_separation_ray: [bool](class_bool.md#class_bool), recovery_as_collision: [bool](class_bool.md#class_bool), result: `PhysicsServer3DExtensionMotionResult*` ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__body_test_motion)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__box_shape_create"></span>

[RID](class_rid.md#class_RID) **_box_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__box_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__capsule_shape_create"></span>

[RID](class_rid.md#class_RID) **_capsule_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__capsule_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__concave_polygon_shape_create"></span>

[RID](class_rid.md#class_RID) **_concave_polygon_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__concave_polygon_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__cone_twist_joint_get_param"></span>

[float](class_float.md#class_float) **_cone_twist_joint_get_param** ( joint: [RID](class_rid.md#class_RID), param: [ConeTwistJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_ConeTwistJointParam) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__cone_twist_joint_get_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__cone_twist_joint_set_param"></span>

void **_cone_twist_joint_set_param** ( joint: [RID](class_rid.md#class_RID), param: [ConeTwistJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_ConeTwistJointParam), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__cone_twist_joint_set_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__convex_polygon_shape_create"></span>

[RID](class_rid.md#class_RID) **_convex_polygon_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__convex_polygon_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__custom_shape_create"></span>

[RID](class_rid.md#class_RID) **_custom_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__custom_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__cylinder_shape_create"></span>

[RID](class_rid.md#class_RID) **_cylinder_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__cylinder_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__end_sync"></span>

void **_end_sync** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__end_sync)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__finish"></span>

void **_finish** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__finish)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__flush_queries"></span>

void **_flush_queries** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__flush_queries)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__free_rid"></span>

void **_free_rid** ( rid: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__free_rid)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_flag"></span>

[bool](class_bool.md#class_bool) **_generic_6dof_joint_get_flag** ( joint: [RID](class_rid.md#class_RID), axis: [Axis](class_vector3.md#enum_Vector3_Axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum_PhysicsServer3D_G6DOFJointAxisFlag) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_flag)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_param"></span>

[float](class_float.md#class_float) **_generic_6dof_joint_get_param** ( joint: [RID](class_rid.md#class_RID), axis: [Axis](class_vector3.md#enum_Vector3_Axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum_PhysicsServer3D_G6DOFJointAxisParam) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_flag"></span>

void **_generic_6dof_joint_set_flag** ( joint: [RID](class_rid.md#class_RID), axis: [Axis](class_vector3.md#enum_Vector3_Axis), flag: [G6DOFJointAxisFlag](class_physicsserver3d.md#enum_PhysicsServer3D_G6DOFJointAxisFlag), enable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_flag)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_param"></span>

void **_generic_6dof_joint_set_param** ( joint: [RID](class_rid.md#class_RID), axis: [Axis](class_vector3.md#enum_Vector3_Axis), param: [G6DOFJointAxisParam](class_physicsserver3d.md#enum_PhysicsServer3D_G6DOFJointAxisParam), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__get_process_info"></span>

[int](class_int.md#class_int) **_get_process_info** ( process_info: [ProcessInfo](class_physicsserver3d.md#enum_PhysicsServer3D_ProcessInfo) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__get_process_info)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__heightmap_shape_create"></span>

[RID](class_rid.md#class_RID) **_heightmap_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__heightmap_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__hinge_joint_get_flag"></span>

[bool](class_bool.md#class_bool) **_hinge_joint_get_flag** ( joint: [RID](class_rid.md#class_RID), flag: [HingeJointFlag](class_physicsserver3d.md#enum_PhysicsServer3D_HingeJointFlag) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__hinge_joint_get_flag)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__hinge_joint_get_param"></span>

[float](class_float.md#class_float) **_hinge_joint_get_param** ( joint: [RID](class_rid.md#class_RID), param: [HingeJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_HingeJointParam) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__hinge_joint_get_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__hinge_joint_set_flag"></span>

void **_hinge_joint_set_flag** ( joint: [RID](class_rid.md#class_RID), flag: [HingeJointFlag](class_physicsserver3d.md#enum_PhysicsServer3D_HingeJointFlag), enabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__hinge_joint_set_flag)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__hinge_joint_set_param"></span>

void **_hinge_joint_set_param** ( joint: [RID](class_rid.md#class_RID), param: [HingeJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_HingeJointParam), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__hinge_joint_set_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__init"></span>

void **_init** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__init)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__is_flushing_queries"></span>

[bool](class_bool.md#class_bool) **_is_flushing_queries** ( ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__is_flushing_queries)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_clear"></span>

void **_joint_clear** ( joint: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_clear)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_create"></span>

[RID](class_rid.md#class_RID) **_joint_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_disable_collisions_between_bodies"></span>

void **_joint_disable_collisions_between_bodies** ( joint: [RID](class_rid.md#class_RID), disable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_disable_collisions_between_bodies)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_get_solver_priority"></span>

[int](class_int.md#class_int) **_joint_get_solver_priority** ( joint: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_get_solver_priority)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_get_type"></span>

[JointType](class_physicsserver3d.md#enum_PhysicsServer3D_JointType) **_joint_get_type** ( joint: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_get_type)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_is_disabled_collisions_between_bodies"></span>

[bool](class_bool.md#class_bool) **_joint_is_disabled_collisions_between_bodies** ( joint: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_is_disabled_collisions_between_bodies)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_make_cone_twist"></span>

void **_joint_make_cone_twist** ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), local_ref_A: [Transform3D](class_transform3d.md#class_Transform3D), body_B: [RID](class_rid.md#class_RID), local_ref_B: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_cone_twist)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_make_generic_6dof"></span>

void **_joint_make_generic_6dof** ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), local_ref_A: [Transform3D](class_transform3d.md#class_Transform3D), body_B: [RID](class_rid.md#class_RID), local_ref_B: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_generic_6dof)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_make_hinge"></span>

void **_joint_make_hinge** ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), hinge_A: [Transform3D](class_transform3d.md#class_Transform3D), body_B: [RID](class_rid.md#class_RID), hinge_B: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_hinge)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_make_hinge_simple"></span>

void **_joint_make_hinge_simple** ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), pivot_A: [Vector3](class_vector3.md#class_Vector3), axis_A: [Vector3](class_vector3.md#class_Vector3), body_B: [RID](class_rid.md#class_RID), pivot_B: [Vector3](class_vector3.md#class_Vector3), axis_B: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_hinge_simple)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_make_pin"></span>

void **_joint_make_pin** ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), local_A: [Vector3](class_vector3.md#class_Vector3), body_B: [RID](class_rid.md#class_RID), local_B: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_pin)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_make_slider"></span>

void **_joint_make_slider** ( joint: [RID](class_rid.md#class_RID), body_A: [RID](class_rid.md#class_RID), local_ref_A: [Transform3D](class_transform3d.md#class_Transform3D), body_B: [RID](class_rid.md#class_RID), local_ref_B: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_make_slider)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__joint_set_solver_priority"></span>

void **_joint_set_solver_priority** ( joint: [RID](class_rid.md#class_RID), priority: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__joint_set_solver_priority)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__pin_joint_get_local_a"></span>

[Vector3](class_vector3.md#class_Vector3) **_pin_joint_get_local_a** ( joint: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_get_local_a)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__pin_joint_get_local_b"></span>

[Vector3](class_vector3.md#class_Vector3) **_pin_joint_get_local_b** ( joint: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_get_local_b)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__pin_joint_get_param"></span>

[float](class_float.md#class_float) **_pin_joint_get_param** ( joint: [RID](class_rid.md#class_RID), param: [PinJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_PinJointParam) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_get_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__pin_joint_set_local_a"></span>

void **_pin_joint_set_local_a** ( joint: [RID](class_rid.md#class_RID), local_A: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_set_local_a)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__pin_joint_set_local_b"></span>

void **_pin_joint_set_local_b** ( joint: [RID](class_rid.md#class_RID), local_B: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_set_local_b)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__pin_joint_set_param"></span>

void **_pin_joint_set_param** ( joint: [RID](class_rid.md#class_RID), param: [PinJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_PinJointParam), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__pin_joint_set_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__separation_ray_shape_create"></span>

[RID](class_rid.md#class_RID) **_separation_ray_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__separation_ray_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__set_active"></span>

void **_set_active** ( active: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__set_active)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__shape_get_custom_solver_bias"></span>

[float](class_float.md#class_float) **_shape_get_custom_solver_bias** ( shape: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_get_custom_solver_bias)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__shape_get_data"></span>

[Variant](class_variant.md#class_Variant) **_shape_get_data** ( shape: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_get_data)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__shape_get_margin"></span>

[float](class_float.md#class_float) **_shape_get_margin** ( shape: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_get_margin)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__shape_get_type"></span>

[ShapeType](class_physicsserver3d.md#enum_PhysicsServer3D_ShapeType) **_shape_get_type** ( shape: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_get_type)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__shape_set_custom_solver_bias"></span>

void **_shape_set_custom_solver_bias** ( shape: [RID](class_rid.md#class_RID), bias: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_set_custom_solver_bias)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__shape_set_data"></span>

void **_shape_set_data** ( shape: [RID](class_rid.md#class_RID), data: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_set_data)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__shape_set_margin"></span>

void **_shape_set_margin** ( shape: [RID](class_rid.md#class_RID), margin: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__shape_set_margin)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__slider_joint_get_param"></span>

[float](class_float.md#class_float) **_slider_joint_get_param** ( joint: [RID](class_rid.md#class_RID), param: [SliderJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_SliderJointParam) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__slider_joint_get_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__slider_joint_set_param"></span>

void **_slider_joint_set_param** ( joint: [RID](class_rid.md#class_RID), param: [SliderJointParam](class_physicsserver3d.md#enum_PhysicsServer3D_SliderJointParam), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__slider_joint_set_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_add_collision_exception"></span>

void **_soft_body_add_collision_exception** ( body: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_add_collision_exception)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_apply_central_force"></span>

void **_soft_body_apply_central_force** ( body: [RID](class_rid.md#class_RID), force: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_apply_central_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_apply_central_impulse"></span>

void **_soft_body_apply_central_impulse** ( body: [RID](class_rid.md#class_RID), impulse: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_apply_central_impulse)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_apply_point_force"></span>

void **_soft_body_apply_point_force** ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int), force: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_apply_point_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_apply_point_impulse"></span>

void **_soft_body_apply_point_impulse** ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int), impulse: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_apply_point_impulse)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_create"></span>

[RID](class_rid.md#class_RID) **_soft_body_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_bounds"></span>

[AABB](class_aabb.md#class_AABB) **_soft_body_get_bounds** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_bounds)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_collision_exceptions"></span>

[Array](class_array.md#class_Array)\[[RID](class_rid.md#class_RID)\] **_soft_body_get_collision_exceptions** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_collision_exceptions)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_collision_layer"></span>

[int](class_int.md#class_int) **_soft_body_get_collision_layer** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_collision_layer)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_collision_mask"></span>

[int](class_int.md#class_int) **_soft_body_get_collision_mask** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_collision_mask)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_damping_coefficient"></span>

[float](class_float.md#class_float) **_soft_body_get_damping_coefficient** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_damping_coefficient)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_drag_coefficient"></span>

[float](class_float.md#class_float) **_soft_body_get_drag_coefficient** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_drag_coefficient)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_linear_stiffness"></span>

[float](class_float.md#class_float) **_soft_body_get_linear_stiffness** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_linear_stiffness)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_point_global_position"></span>

[Vector3](class_vector3.md#class_Vector3) **_soft_body_get_point_global_position** ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_point_global_position)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_pressure_coefficient"></span>

[float](class_float.md#class_float) **_soft_body_get_pressure_coefficient** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_pressure_coefficient)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_shrinking_factor"></span>

[float](class_float.md#class_float) **_soft_body_get_shrinking_factor** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_shrinking_factor)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_simulation_precision"></span>

[int](class_int.md#class_int) **_soft_body_get_simulation_precision** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_simulation_precision)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_space"></span>

[RID](class_rid.md#class_RID) **_soft_body_get_space** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_space)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_state"></span>

[Variant](class_variant.md#class_Variant) **_soft_body_get_state** ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver3d.md#enum_PhysicsServer3D_BodyState) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_get_total_mass"></span>

[float](class_float.md#class_float) **_soft_body_get_total_mass** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_get_total_mass)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_is_point_pinned"></span>

[bool](class_bool.md#class_bool) **_soft_body_is_point_pinned** ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_is_point_pinned)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_move_point"></span>

void **_soft_body_move_point** ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int), global_position: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_move_point)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_pin_point"></span>

void **_soft_body_pin_point** ( body: [RID](class_rid.md#class_RID), point_index: [int](class_int.md#class_int), pin: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_pin_point)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_remove_all_pinned_points"></span>

void **_soft_body_remove_all_pinned_points** ( body: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_remove_all_pinned_points)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_remove_collision_exception"></span>

void **_soft_body_remove_collision_exception** ( body: [RID](class_rid.md#class_RID), body_b: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_remove_collision_exception)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_collision_layer"></span>

void **_soft_body_set_collision_layer** ( body: [RID](class_rid.md#class_RID), layer: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_collision_layer)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_collision_mask"></span>

void **_soft_body_set_collision_mask** ( body: [RID](class_rid.md#class_RID), mask: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_collision_mask)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_damping_coefficient"></span>

void **_soft_body_set_damping_coefficient** ( body: [RID](class_rid.md#class_RID), damping_coefficient: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_damping_coefficient)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_drag_coefficient"></span>

void **_soft_body_set_drag_coefficient** ( body: [RID](class_rid.md#class_RID), drag_coefficient: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_drag_coefficient)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_linear_stiffness"></span>

void **_soft_body_set_linear_stiffness** ( body: [RID](class_rid.md#class_RID), linear_stiffness: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_linear_stiffness)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_mesh"></span>

void **_soft_body_set_mesh** ( body: [RID](class_rid.md#class_RID), mesh: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_mesh)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_pressure_coefficient"></span>

void **_soft_body_set_pressure_coefficient** ( body: [RID](class_rid.md#class_RID), pressure_coefficient: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_pressure_coefficient)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_ray_pickable"></span>

void **_soft_body_set_ray_pickable** ( body: [RID](class_rid.md#class_RID), enable: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_ray_pickable)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_shrinking_factor"></span>

void **_soft_body_set_shrinking_factor** ( body: [RID](class_rid.md#class_RID), shrinking_factor: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_shrinking_factor)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_simulation_precision"></span>

void **_soft_body_set_simulation_precision** ( body: [RID](class_rid.md#class_RID), simulation_precision: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_simulation_precision)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_space"></span>

void **_soft_body_set_space** ( body: [RID](class_rid.md#class_RID), space: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_space)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_state"></span>

void **_soft_body_set_state** ( body: [RID](class_rid.md#class_RID), state: [BodyState](class_physicsserver3d.md#enum_PhysicsServer3D_BodyState), variant: [Variant](class_variant.md#class_Variant) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_total_mass"></span>

void **_soft_body_set_total_mass** ( body: [RID](class_rid.md#class_RID), total_mass: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_total_mass)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_set_transform"></span>

void **_soft_body_set_transform** ( body: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_set_transform)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__soft_body_update_rendering_server"></span>

void **_soft_body_update_rendering_server** ( body: [RID](class_rid.md#class_RID), rendering_server_handler: [PhysicsServer3DRenderingServerHandler](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_update_rendering_server)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__space_create"></span>

[RID](class_rid.md#class_RID) **_space_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__space_get_contact_count"></span>

[int](class_int.md#class_int) **_space_get_contact_count** ( space: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_get_contact_count)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__space_get_contacts"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **_space_get_contacts** ( space: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_get_contacts)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__space_get_direct_state"></span>

[PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) **_space_get_direct_state** ( space: [RID](class_rid.md#class_RID) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_get_direct_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__space_get_param"></span>

[float](class_float.md#class_float) **_space_get_param** ( space: [RID](class_rid.md#class_RID), param: [SpaceParameter](class_physicsserver3d.md#enum_PhysicsServer3D_SpaceParameter) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_get_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__space_is_active"></span>

[bool](class_bool.md#class_bool) **_space_is_active** ( space: [RID](class_rid.md#class_RID) ) *virtual* |required| *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_is_active)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__space_set_active"></span>

void **_space_set_active** ( space: [RID](class_rid.md#class_RID), active: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_set_active)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__space_set_debug_contacts"></span>

void **_space_set_debug_contacts** ( space: [RID](class_rid.md#class_RID), max_contacts: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_set_debug_contacts)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__space_set_param"></span>

void **_space_set_param** ( space: [RID](class_rid.md#class_RID), param: [SpaceParameter](class_physicsserver3d.md#enum_PhysicsServer3D_SpaceParameter), value: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__space_set_param)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__sphere_shape_create"></span>

[RID](class_rid.md#class_RID) **_sphere_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__sphere_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__step"></span>

void **_step** ( step: [float](class_float.md#class_float) ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__step)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__sync"></span>

void **_sync** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__sync)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_private_method__world_boundary_shape_create"></span>

[RID](class_rid.md#class_RID) **_world_boundary_shape_create** ( ) *virtual* |required| [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__world_boundary_shape_create)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_body"></span>

[bool](class_bool.md#class_bool) **body_test_motion_is_excluding_body** ( body: [RID](class_rid.md#class_RID) ) *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_body)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_object"></span>

[bool](class_bool.md#class_bool) **body_test_motion_is_excluding_object** ( object: [int](class_int.md#class_int) ) *const* [🔗](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_object)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
