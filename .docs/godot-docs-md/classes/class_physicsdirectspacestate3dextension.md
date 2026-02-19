<span id="class_PhysicsDirectSpaceState3DExtension"></span>

## PhysicsDirectSpaceState3DExtension

**Inherits:** [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) **<** [Object](class_object.md#class_Object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) implementations.

### Description

This class extends [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectSpaceState3D](class_physicsdirectspacestate3d.md#class_PhysicsDirectSpaceState3D).

### Methods


| [bool](class_bool.md#class_bool) | [_cast_motion](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__cast_motion) ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), closest_safe: `float*`, closest_unsafe: `float*`, info: `PhysicsServer3DExtensionShapeRestInfo*` ) | virtual | required |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_collide_shape](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__collide_shape) ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), results: `void*`, max_results: [int](class_int.md#class_int), result_count: `int32_t*` ) | virtual | required |
| [Vector3](class_vector3.md#class_Vector3) | [_get_closest_point_to_object_volume](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__get_closest_point_to_object_volume) ( object: [RID](class_rid.md#class_RID), point: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required | const |
| [int](class_int.md#class_int) | [_intersect_point](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__intersect_point) ( position: [Vector3](class_vector3.md#class_Vector3), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), results: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class_int) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_intersect_ray](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__intersect_ray) ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), hit_from_inside: [bool](class_bool.md#class_bool), hit_back_faces: [bool](class_bool.md#class_bool), pick_ray: [bool](class_bool.md#class_bool), result: `PhysicsServer3DExtensionRayResult*` ) | virtual | required |
| [int](class_int.md#class_int) | [_intersect_shape](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__intersect_shape) ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), result_count: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class_int) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_rest_info](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__rest_info) ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), rest_info: `PhysicsServer3DExtensionShapeRestInfo*` ) | virtual | required |
| [bool](class_bool.md#class_bool) | [is_body_excluded_from_query](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_method_is_body_excluded_from_query) ( body: [RID](class_rid.md#class_RID) ) const |

---

### Method Descriptions

<span id="class_PhysicsDirectSpaceState3DExtension_private_method__cast_motion"></span>

[bool](class_bool.md#class_bool) **_cast_motion** ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), closest_safe: `float*`, closest_unsafe: `float*`, info: `PhysicsServer3DExtensionShapeRestInfo*` ) *virtual* |required| [🔗](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__cast_motion)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState3DExtension_private_method__collide_shape"></span>

[bool](class_bool.md#class_bool) **_collide_shape** ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), results: `void*`, max_results: [int](class_int.md#class_int), result_count: `int32_t*` ) *virtual* |required| [🔗](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__collide_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState3DExtension_private_method__get_closest_point_to_object_volume"></span>

[Vector3](class_vector3.md#class_Vector3) **_get_closest_point_to_object_volume** ( object: [RID](class_rid.md#class_RID), point: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| *const* [🔗](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__get_closest_point_to_object_volume)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState3DExtension_private_method__intersect_point"></span>

[int](class_int.md#class_int) **_intersect_point** ( position: [Vector3](class_vector3.md#class_Vector3), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), results: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__intersect_point)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState3DExtension_private_method__intersect_ray"></span>

[bool](class_bool.md#class_bool) **_intersect_ray** ( from: [Vector3](class_vector3.md#class_Vector3), to: [Vector3](class_vector3.md#class_Vector3), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), hit_from_inside: [bool](class_bool.md#class_bool), hit_back_faces: [bool](class_bool.md#class_bool), pick_ray: [bool](class_bool.md#class_bool), result: `PhysicsServer3DExtensionRayResult*` ) *virtual* |required| [🔗](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__intersect_ray)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState3DExtension_private_method__intersect_shape"></span>

[int](class_int.md#class_int) **_intersect_shape** ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), result_count: `PhysicsServer3DExtensionShapeResult*`, max_results: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__intersect_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState3DExtension_private_method__rest_info"></span>

[bool](class_bool.md#class_bool) **_rest_info** ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform3D](class_transform3d.md#class_Transform3D), motion: [Vector3](class_vector3.md#class_Vector3), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), rest_info: `PhysicsServer3DExtensionShapeRestInfo*` ) *virtual* |required| [🔗](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_private_method__rest_info)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState3DExtension_method_is_body_excluded_from_query"></span>

[bool](class_bool.md#class_bool) **is_body_excluded_from_query** ( body: [RID](class_rid.md#class_RID) ) *const* [🔗](class_physicsdirectspacestate3dextension.md#class_PhysicsDirectSpaceState3DExtension_method_is_body_excluded_from_query)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
