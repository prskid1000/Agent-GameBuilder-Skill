<span id="class_PhysicsServer3DRenderingServerHandler"></span>

## PhysicsServer3DRenderingServerHandler

**Inherits:** [Object](class_object.md#class_Object)

A class used to provide [PhysicsServer3DExtension._soft_body_update_rendering_server()](class_physicsserver3dextension.md#class_PhysicsServer3DExtension_private_method__soft_body_update_rendering_server) with a rendering handler for soft bodies.

### Methods


| void | [_set_aabb](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_private_method__set_aabb) ( aabb: [AABB](class_aabb.md#class_AABB) ) | virtual | required |
| --- | --- | --- | --- |
| void | [_set_normal](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_private_method__set_normal) ( vertex_id: [int](class_int.md#class_int), normal: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [_set_vertex](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_private_method__set_vertex) ( vertex_id: [int](class_int.md#class_int), vertex: [Vector3](class_vector3.md#class_Vector3) ) | virtual | required |
| void | [set_aabb](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_method_set_aabb) ( aabb: [AABB](class_aabb.md#class_AABB) ) |
| void | [set_normal](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_method_set_normal) ( vertex_id: [int](class_int.md#class_int), normal: [Vector3](class_vector3.md#class_Vector3) ) |
| void | [set_vertex](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_method_set_vertex) ( vertex_id: [int](class_int.md#class_int), vertex: [Vector3](class_vector3.md#class_Vector3) ) |

---

### Method Descriptions

<span id="class_PhysicsServer3DRenderingServerHandler_private_method__set_aabb"></span>

void **_set_aabb** ( aabb: [AABB](class_aabb.md#class_AABB) ) *virtual* |required| [🔗](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_private_method__set_aabb)

Called by the [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) to set the bounding box for the [SoftBody3D](class_softbody3d.md#class_SoftBody3D).

---

<span id="class_PhysicsServer3DRenderingServerHandler_private_method__set_normal"></span>

void **_set_normal** ( vertex_id: [int](class_int.md#class_int), normal: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_private_method__set_normal)

Called by the [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) to set the normal for the [SoftBody3D](class_softbody3d.md#class_SoftBody3D) vertex at the index specified by `vertex_id`.

 **Note:** The `normal` parameter used to be of type `const void*` prior to Godot 4.2.

---

<span id="class_PhysicsServer3DRenderingServerHandler_private_method__set_vertex"></span>

void **_set_vertex** ( vertex_id: [int](class_int.md#class_int), vertex: [Vector3](class_vector3.md#class_Vector3) ) *virtual* |required| [🔗](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_private_method__set_vertex)

Called by the [PhysicsServer3D](class_physicsserver3d.md#class_PhysicsServer3D) to set the position for the [SoftBody3D](class_softbody3d.md#class_SoftBody3D) vertex at the index specified by `vertex_id`.

 **Note:** The `vertex` parameter used to be of type `const void*` prior to Godot 4.2.

---

<span id="class_PhysicsServer3DRenderingServerHandler_method_set_aabb"></span>

void **set_aabb** ( aabb: [AABB](class_aabb.md#class_AABB) ) [🔗](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_method_set_aabb)

Sets the bounding box for the [SoftBody3D](class_softbody3d.md#class_SoftBody3D).

---

<span id="class_PhysicsServer3DRenderingServerHandler_method_set_normal"></span>

void **set_normal** ( vertex_id: [int](class_int.md#class_int), normal: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_method_set_normal)

Sets the normal for the [SoftBody3D](class_softbody3d.md#class_SoftBody3D) vertex at the index specified by `vertex_id`.

---

<span id="class_PhysicsServer3DRenderingServerHandler_method_set_vertex"></span>

void **set_vertex** ( vertex_id: [int](class_int.md#class_int), vertex: [Vector3](class_vector3.md#class_Vector3) ) [🔗](class_physicsserver3drenderingserverhandler.md#class_PhysicsServer3DRenderingServerHandler_method_set_vertex)

Sets the position for the [SoftBody3D](class_softbody3d.md#class_SoftBody3D) vertex at the index specified by `vertex_id`.
