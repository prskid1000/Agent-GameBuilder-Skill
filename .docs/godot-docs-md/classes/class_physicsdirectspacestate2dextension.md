<span id="class_PhysicsDirectSpaceState2DExtension"></span>

## PhysicsDirectSpaceState2DExtension

**Inherits:** [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) **<** [Object](class_object.md#class_Object)

Provides virtual methods that can be overridden to create custom [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) implementations.

### Description

This class extends [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D) by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectSpaceState2D](class_physicsdirectspacestate2d.md#class_PhysicsDirectSpaceState2D).

### Methods


| [bool](class_bool.md#class_bool) | [_cast_motion](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__cast_motion) ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), closest_safe: `float*`, closest_unsafe: `float*` ) | virtual | required |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [_collide_shape](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__collide_shape) ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), results: `void*`, max_results: [int](class_int.md#class_int), result_count: `int32_t*` ) | virtual | required |
| [int](class_int.md#class_int) | [_intersect_point](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__intersect_point) ( position: [Vector2](class_vector2.md#class_Vector2), canvas_instance_id: [int](class_int.md#class_int), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), results: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class_int) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_intersect_ray](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__intersect_ray) ( from: [Vector2](class_vector2.md#class_Vector2), to: [Vector2](class_vector2.md#class_Vector2), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), hit_from_inside: [bool](class_bool.md#class_bool), result: `PhysicsServer2DExtensionRayResult*` ) | virtual | required |
| [int](class_int.md#class_int) | [_intersect_shape](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__intersect_shape) ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), result: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class_int) ) | virtual | required |
| [bool](class_bool.md#class_bool) | [_rest_info](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__rest_info) ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), rest_info: `PhysicsServer2DExtensionShapeRestInfo*` ) | virtual | required |
| [bool](class_bool.md#class_bool) | [is_body_excluded_from_query](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_method_is_body_excluded_from_query) ( body: [RID](class_rid.md#class_RID) ) const |

---

### Method Descriptions

<span id="class_PhysicsDirectSpaceState2DExtension_private_method__cast_motion"></span>

[bool](class_bool.md#class_bool) **_cast_motion** ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), closest_safe: `float*`, closest_unsafe: `float*` ) *virtual* |required| [🔗](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__cast_motion)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState2DExtension_private_method__collide_shape"></span>

[bool](class_bool.md#class_bool) **_collide_shape** ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), results: `void*`, max_results: [int](class_int.md#class_int), result_count: `int32_t*` ) *virtual* |required| [🔗](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__collide_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState2DExtension_private_method__intersect_point"></span>

[int](class_int.md#class_int) **_intersect_point** ( position: [Vector2](class_vector2.md#class_Vector2), canvas_instance_id: [int](class_int.md#class_int), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), results: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__intersect_point)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState2DExtension_private_method__intersect_ray"></span>

[bool](class_bool.md#class_bool) **_intersect_ray** ( from: [Vector2](class_vector2.md#class_Vector2), to: [Vector2](class_vector2.md#class_Vector2), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), hit_from_inside: [bool](class_bool.md#class_bool), result: `PhysicsServer2DExtensionRayResult*` ) *virtual* |required| [🔗](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__intersect_ray)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState2DExtension_private_method__intersect_shape"></span>

[int](class_int.md#class_int) **_intersect_shape** ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), result: `PhysicsServer2DExtensionShapeResult*`, max_results: [int](class_int.md#class_int) ) *virtual* |required| [🔗](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__intersect_shape)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState2DExtension_private_method__rest_info"></span>

[bool](class_bool.md#class_bool) **_rest_info** ( shape_rid: [RID](class_rid.md#class_RID), transform: [Transform2D](class_transform2d.md#class_Transform2D), motion: [Vector2](class_vector2.md#class_Vector2), margin: [float](class_float.md#class_float), collision_mask: [int](class_int.md#class_int), collide_with_bodies: [bool](class_bool.md#class_bool), collide_with_areas: [bool](class_bool.md#class_bool), rest_info: `PhysicsServer2DExtensionShapeRestInfo*` ) *virtual* |required| [🔗](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_private_method__rest_info)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_PhysicsDirectSpaceState2DExtension_method_is_body_excluded_from_query"></span>

[bool](class_bool.md#class_bool) **is_body_excluded_from_query** ( body: [RID](class_rid.md#class_RID) ) *const* [🔗](class_physicsdirectspacestate2dextension.md#class_PhysicsDirectSpaceState2DExtension_method_is_body_excluded_from_query)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
