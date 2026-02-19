<span id="class_PhysicsDirectBodyState3DExtension"></span>

## PhysicsDirectBodyState3DExtension

**Inherits:** [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class_PhysicsDirectBodyState3D) **<** [Object](class_object.md#class_Object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class_PhysicsDirectBodyState3D) implementations.

### Description

This class extends [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class_PhysicsDirectBodyState3D) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectBodyState3D](class_physicsdirectbodystate3d.md#class_PhysicsDirectBodyState3D).

### Methods


| void | [_add_constant_central_force](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__add_constant_central_force) ( force: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| --- | --- | --- | --- |
| void | [_add_constant_force](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__add_constant_force) ( force: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_add_constant_torque](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__add_constant_torque) ( torque: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_apply_central_force](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_central_force) ( force: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_apply_central_impulse](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_central_impulse) ( impulse: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_apply_force](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_force) ( force: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_apply_impulse](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_impulse) ( impulse: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_apply_torque](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_torque) ( torque: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_apply_torque_impulse](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_torque_impulse) ( impulse: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| [Vector3](class_vector3.md#class_Vector3) | [_get_angular_velocity](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_angular_velocity) ( ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_center_of_mass](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass) ( ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_center_of_mass_local](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass_local) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_collision_layer](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_collision_layer) ( ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_collision_mask](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_collision_mask) ( ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_constant_force](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_constant_force) ( ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_constant_torque](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_constant_torque) ( ) | virtual | required | const |
| [RID](class_rid.md#class_RID) | [_get_contact_collider](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_contact_collider_id](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_id) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [Object](class_object.md#class_Object) | [_get_contact_collider_object](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_object) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_contact_collider_position](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_position) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_contact_collider_shape](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_shape) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_contact_collider_velocity_at_position](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_velocity_at_position) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_contact_count](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_count) ( ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_contact_impulse](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_impulse) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_contact_local_normal](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_normal) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_contact_local_position](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_position) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_get_contact_local_shape](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_shape) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_contact_local_velocity_at_position](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_velocity_at_position) ( contact_idx: [int](class_int.md#class_int) ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_inverse_inertia](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia) ( ) | virtual | required | const |
| [Basis](class_basis.md#class_Basis) | [_get_inverse_inertia_tensor](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia_tensor) ( ) | virtual | required | const |
| [float](class_float.md#class_float) | [_get_inverse_mass](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_mass) ( ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_linear_velocity](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_linear_velocity) ( ) | virtual | required | const |
| [Basis](class_basis.md#class_Basis) | [_get_principal_inertia_axes](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_principal_inertia_axes) ( ) | virtual | required | const |
| [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) | [_get_space_state](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_space_state) ( ) | virtual | required |
| [float](class_float.md#class_float) | [_get_step](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_step) ( ) | virtual | required | const |
| [float](class_float.md#class_float) | [_get_total_angular_damp](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_total_angular_damp) ( ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_total_gravity](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_total_gravity) ( ) | virtual | required | const |
| [float](class_float.md#class_float) | [_get_total_linear_damp](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_total_linear_damp) ( ) | virtual | required | const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [_get_transform](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_transform) ( ) | virtual | required | const |
| [Vector3](class_vector3.md#class_Vector3) | [_get_velocity_at_local_position](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_velocity_at_local_position) ( local_position: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required | const |
| void | [_integrate_forces](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__integrate_forces) ( ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_is_sleeping](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__is_sleeping) ( ) | virtual | required | const |
| void | [_set_angular_velocity](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_angular_velocity) ( velocity: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_set_collision_layer](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_collision_layer) ( layer: [int](class_int.md#class_int) ) | virtual | required |
| void | [_set_collision_mask](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_collision_mask) ( mask: [int](class_int.md#class_int) ) | virtual | required |
| void | [_set_constant_force](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_constant_force) ( force: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_set_constant_torque](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_constant_torque) ( torque: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_set_linear_velocity](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_linear_velocity) ( velocity: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_set_sleep_state](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_sleep_state) ( enabled: [bool](class_bool.md#class_bool) ) | virtual | required |
| void | [_set_transform](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_transform) ( transform: [Transform3D](class_transform3d.md#class_Transform3D) ) | virtual | required |

---

### Method Descriptions

<span id="class_PhysicsDirectBodyState3DExtension_private_method__add_constant_central_force"></span>

void **_add_constant_central_force** ( force: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__add_constant_central_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__add_constant_force"></span>

void **_add_constant_force** ( force: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__add_constant_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__add_constant_torque"></span>

void **_add_constant_torque** ( torque: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__add_constant_torque)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__apply_central_force"></span>

void **_apply_central_force** ( force: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_central_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__apply_central_impulse"></span>

void **_apply_central_impulse** ( impulse: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_central_impulse)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__apply_force"></span>

void **_apply_force** ( force: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__apply_impulse"></span>

void **_apply_impulse** ( impulse: [Vector3](class_vector3.md#class_Vector3), position: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_impulse)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__apply_torque"></span>

void **_apply_torque** ( torque: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_torque)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__apply_torque_impulse"></span>

void **_apply_torque_impulse** ( impulse: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__apply_torque_impulse)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_angular_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_angular_velocity** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_angular_velocity)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_center_of_mass** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass_local"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_center_of_mass_local** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass_local)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_collision_layer"></span>

[int](class_int.md#class_int) **_get_collision_layer** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_collision_layer)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_collision_mask"></span>

[int](class_int.md#class_int) **_get_collision_mask** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_collision_mask)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_constant_force"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_constant_force** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_constant_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_constant_torque"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_constant_torque** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_constant_torque)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider"></span>

[RID](class_rid.md#class_RID) **_get_contact_collider** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_id"></span>

[int](class_int.md#class_int) **_get_contact_collider_id** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_id)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_object"></span>

[Object](class_object.md#class_Object) **_get_contact_collider_object** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_object)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_position"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_contact_collider_position** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_position)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_shape"></span>

[int](class_int.md#class_int) **_get_contact_collider_shape** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_velocity_at_position"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_contact_collider_velocity_at_position** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_velocity_at_position)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_count"></span>

[int](class_int.md#class_int) **_get_contact_count** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_count)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_impulse"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_contact_impulse** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_impulse)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_normal"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_contact_local_normal** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_normal)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_position"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_contact_local_position** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_position)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_shape"></span>

[int](class_int.md#class_int) **_get_contact_local_shape** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_velocity_at_position"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_contact_local_velocity_at_position** ( contact_idx: [int](class_int.md#class_int) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_velocity_at_position)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_inverse_inertia** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia_tensor"></span>

[Basis](class_basis.md#class_Basis) **_get_inverse_inertia_tensor** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia_tensor)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_mass"></span>

[float](class_float.md#class_float) **_get_inverse_mass** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_mass)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_linear_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_linear_velocity** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_linear_velocity)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_principal_inertia_axes"></span>

[Basis](class_basis.md#class_Basis) **_get_principal_inertia_axes** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_principal_inertia_axes)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_space_state"></span>

[PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) **_get_space_state** ( ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_space_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_step"></span>

[float](class_float.md#class_float) **_get_step** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_step)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_total_angular_damp"></span>

[float](class_float.md#class_float) **_get_total_angular_damp** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_total_angular_damp)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_total_gravity"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_total_gravity** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_total_gravity)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_total_linear_damp"></span>

[float](class_float.md#class_float) **_get_total_linear_damp** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_total_linear_damp)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **_get_transform** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_transform)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__get_velocity_at_local_position"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_velocity_at_local_position** ( local_position: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__get_velocity_at_local_position)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__integrate_forces"></span>

void **_integrate_forces** ( ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__integrate_forces)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__is_sleeping"></span>

[bool](class_bool.md#class_bool) **_is_sleeping** ( ) *virtual* |required| *const* [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__is_sleeping)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__set_angular_velocity"></span>

void **_set_angular_velocity** ( velocity: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_angular_velocity)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__set_collision_layer"></span>

void **_set_collision_layer** ( layer: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_collision_layer)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__set_collision_mask"></span>

void **_set_collision_mask** ( mask: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_collision_mask)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__set_constant_force"></span>

void **_set_constant_force** ( force: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_constant_force)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__set_constant_torque"></span>

void **_set_constant_torque** ( torque: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_constant_torque)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__set_linear_velocity"></span>

void **_set_linear_velocity** ( velocity: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_linear_velocity)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__set_sleep_state"></span>

void **_set_sleep_state** ( enabled: [bool](class_bool.md#class_bool) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_sleep_state)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectBodyState3DExtension_private_method__set_transform"></span>

void **_set_transform** ( transform: [Transform3D](class_transform3d.md#class_Transform3D) ) *virtual* |required| [🔗](class_physicsdirectbodystate3dextension.md#class_PhysicsDirectBodyState3DExtension_private_method__set_transform)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
