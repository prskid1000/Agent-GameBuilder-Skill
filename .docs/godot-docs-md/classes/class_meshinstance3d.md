<span id="class_MeshInstance3D"></span>

## MeshInstance3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [SoftBody3D](class_softbody3d.md#class_SoftBody3D)

Node that instances meshes into a scenario.

### Description

MeshInstance3D is a node that takes a [Mesh](class_mesh.md#class_Mesh) resource and adds it to the current scenario by creating an instance of it. This is the class most often used to render 3D geometry and can be used to instance a single [Mesh](class_mesh.md#class_Mesh) in many places. This allows reusing geometry, which can save on resources. When a [Mesh](class_mesh.md#class_Mesh) has to be instantiated more than thousands of times at close proximity, consider using a [MultiMesh](class_multimesh.md#class_MultiMesh) in a [MultiMeshInstance3D](class_multimeshinstance3d.md#class_MultiMeshInstance3D) instead.

### Tutorials

- 3D Material Testers Demo

- 3D Kinematic Character Demo

- 3D Platformer Demo

- Third Person Shooter (TPS) Demo

### Properties


| [Mesh](class_mesh.md#class_Mesh) | [mesh](class_meshinstance3d.md#class_MeshInstance3D_property_mesh) |
| --- | --- |
| [NodePath](class_nodepath.md#class_NodePath) | [skeleton](class_meshinstance3d.md#class_MeshInstance3D_property_skeleton) | `NodePath("")` |
| [Skin](class_skin.md#class_Skin) | [skin](class_meshinstance3d.md#class_MeshInstance3D_property_skin) |

### Methods


| [ArrayMesh](class_arraymesh.md#class_ArrayMesh) | [bake_mesh_from_current_blend_shape_mix](class_meshinstance3d.md#class_MeshInstance3D_method_bake_mesh_from_current_blend_shape_mix) ( existing: [ArrayMesh](class_arraymesh.md#class_ArrayMesh) = null ) |
| --- | --- |
| [ArrayMesh](class_arraymesh.md#class_ArrayMesh) | [bake_mesh_from_current_skeleton_pose](class_meshinstance3d.md#class_MeshInstance3D_method_bake_mesh_from_current_skeleton_pose) ( existing: [ArrayMesh](class_arraymesh.md#class_ArrayMesh) = null ) |
| void | [create_convex_collision](class_meshinstance3d.md#class_MeshInstance3D_method_create_convex_collision) ( clean: [bool](class_bool.md#class_bool) = true, simplify: [bool](class_bool.md#class_bool) = false ) |
| void | [create_debug_tangents](class_meshinstance3d.md#class_MeshInstance3D_method_create_debug_tangents) ( ) |
| void | [create_multiple_convex_collisions](class_meshinstance3d.md#class_MeshInstance3D_method_create_multiple_convex_collisions) ( settings: [MeshConvexDecompositionSettings](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings) = null ) |
| void | [create_trimesh_collision](class_meshinstance3d.md#class_MeshInstance3D_method_create_trimesh_collision) ( ) |
| [int](class_int.md#class_int) | [find_blend_shape_by_name](class_meshinstance3d.md#class_MeshInstance3D_method_find_blend_shape_by_name) ( name: [StringName](class_stringname.md#class_StringName) ) |
| [Material](class_material.md#class_Material) | [get_active_material](class_meshinstance3d.md#class_MeshInstance3D_method_get_active_material) ( surface: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_blend_shape_count](class_meshinstance3d.md#class_MeshInstance3D_method_get_blend_shape_count) ( ) const |
| [float](class_float.md#class_float) | [get_blend_shape_value](class_meshinstance3d.md#class_MeshInstance3D_method_get_blend_shape_value) ( blend_shape_idx: [int](class_int.md#class_int) ) const |
| [SkinReference](class_skinreference.md#class_SkinReference) | [get_skin_reference](class_meshinstance3d.md#class_MeshInstance3D_method_get_skin_reference) ( ) const |
| [Material](class_material.md#class_Material) | [get_surface_override_material](class_meshinstance3d.md#class_MeshInstance3D_method_get_surface_override_material) ( surface: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_surface_override_material_count](class_meshinstance3d.md#class_MeshInstance3D_method_get_surface_override_material_count) ( ) const |
| void | [set_blend_shape_value](class_meshinstance3d.md#class_MeshInstance3D_method_set_blend_shape_value) ( blend_shape_idx: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) |
| void | [set_surface_override_material](class_meshinstance3d.md#class_MeshInstance3D_method_set_surface_override_material) ( surface: [int](class_int.md#class_int), material: [Material](class_material.md#class_Material) ) |

---

### Property Descriptions

<span id="class_MeshInstance3D_property_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **mesh** [🔗](class_meshinstance3d.md#class_MeshInstance3D_property_mesh)

- void **set_mesh** ( value: [Mesh](class_mesh.md#class_Mesh) )
- [Mesh](class_mesh.md#class_Mesh) **get_mesh** ( )

The [Mesh](class_mesh.md#class_Mesh) resource for the instance.

---

<span id="class_MeshInstance3D_property_skeleton"></span>

[NodePath](class_nodepath.md#class_NodePath) **skeleton** = `NodePath("")` [🔗](class_meshinstance3d.md#class_MeshInstance3D_property_skeleton)

- void **set_skeleton_path** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_skeleton_path** ( )

[NodePath](class_nodepath.md#class_NodePath) to the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) associated with the instance.

 **Note:** The default value of this property has changed in Godot 4.6. Enable ProjectSettings.animation/compatibility/default_parent_skeleton_in_mesh_instance_3d if the old behavior is needed for compatibility.

---

<span id="class_MeshInstance3D_property_skin"></span>

[Skin](class_skin.md#class_Skin) **skin** [🔗](class_meshinstance3d.md#class_MeshInstance3D_property_skin)

- void **set_skin** ( value: [Skin](class_skin.md#class_Skin) )
- [Skin](class_skin.md#class_Skin) **get_skin** ( )

The [Skin](class_skin.md#class_Skin) to be used by this instance.

---

### Method Descriptions

<span id="class_MeshInstance3D_method_bake_mesh_from_current_blend_shape_mix"></span>

[ArrayMesh](class_arraymesh.md#class_ArrayMesh) **bake_mesh_from_current_blend_shape_mix** ( existing: [ArrayMesh](class_arraymesh.md#class_ArrayMesh) = null ) [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_bake_mesh_from_current_blend_shape_mix)

Takes a snapshot from the current [ArrayMesh](class_arraymesh.md#class_ArrayMesh) with all blend shapes applied according to their current weights and bakes it to the provided `existing` mesh. If no `existing` mesh is provided a new [ArrayMesh](class_arraymesh.md#class_ArrayMesh) is created, baked and returned. Mesh surface materials are not copied.

 **Performance:** [Mesh](class_mesh.md#class_Mesh) data needs to be received from the GPU, stalling the [RenderingServer](class_renderingserver.md#class_RenderingServer) in the process.

---

<span id="class_MeshInstance3D_method_bake_mesh_from_current_skeleton_pose"></span>

[ArrayMesh](class_arraymesh.md#class_ArrayMesh) **bake_mesh_from_current_skeleton_pose** ( existing: [ArrayMesh](class_arraymesh.md#class_ArrayMesh) = null ) [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_bake_mesh_from_current_skeleton_pose)

Takes a snapshot of the current animated skeleton pose of the skinned mesh and bakes it to the provided `existing` mesh. If no `existing` mesh is provided a new [ArrayMesh](class_arraymesh.md#class_ArrayMesh) is created, baked, and returned. Requires a skeleton with a registered skin to work. Blendshapes are ignored. Mesh surface materials are not copied.

 **Performance:** [Mesh](class_mesh.md#class_Mesh) data needs to be retrieved from the GPU, stalling the [RenderingServer](class_renderingserver.md#class_RenderingServer) in the process.

---

<span id="class_MeshInstance3D_method_create_convex_collision"></span>

void **create_convex_collision** ( clean: [bool](class_bool.md#class_bool) = true, simplify: [bool](class_bool.md#class_bool) = false ) [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_create_convex_collision)

This helper creates a [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) child node with a [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class_ConvexPolygonShape3D) collision shape calculated from the mesh geometry. It's mainly used for testing.

If `clean` is `true` (default), duplicate and interior vertices are removed automatically. You can set it to `false` to make the process faster if not needed.

If `simplify` is `true`, the geometry can be further simplified to reduce the number of vertices. Disabled by default.

---

<span id="class_MeshInstance3D_method_create_debug_tangents"></span>

void **create_debug_tangents** ( ) [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_create_debug_tangents)

This helper creates a **MeshInstance3D** child node with gizmos at every vertex calculated from the mesh geometry. It's mainly used for testing.

---

<span id="class_MeshInstance3D_method_create_multiple_convex_collisions"></span>

void **create_multiple_convex_collisions** ( settings: [MeshConvexDecompositionSettings](class_meshconvexdecompositionsettings.md#class_MeshConvexDecompositionSettings) = null ) [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_create_multiple_convex_collisions)

This helper creates a [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) child node with multiple [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class_ConvexPolygonShape3D) collision shapes calculated from the mesh geometry via convex decomposition. The convex decomposition operation can be controlled with parameters from the optional `settings`.

---

<span id="class_MeshInstance3D_method_create_trimesh_collision"></span>

void **create_trimesh_collision** ( ) [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_create_trimesh_collision)

This helper creates a [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) child node with a [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D) collision shape calculated from the mesh geometry. It's mainly used for testing.

---

<span id="class_MeshInstance3D_method_find_blend_shape_by_name"></span>

[int](class_int.md#class_int) **find_blend_shape_by_name** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_find_blend_shape_by_name)

Returns the index of the blend shape with the given `name`. Returns `-1` if no blend shape with this name exists, including when [mesh](class_meshinstance3d.md#class_MeshInstance3D_property_mesh) is `null`.

---

<span id="class_MeshInstance3D_method_get_active_material"></span>

[Material](class_material.md#class_Material) **get_active_material** ( surface: [int](class_int.md#class_int) ) *const* [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_get_active_material)

Returns the [Material](class_material.md#class_Material) that will be used by the [Mesh](class_mesh.md#class_Mesh) when drawing. This can return the [GeometryInstance3D.material_override](class_geometryinstance3d.md#class_GeometryInstance3D_property_material_override), the surface override [Material](class_material.md#class_Material) defined in this **MeshInstance3D**, or the surface [Material](class_material.md#class_Material) defined in the [mesh](class_meshinstance3d.md#class_MeshInstance3D_property_mesh). For example, if [GeometryInstance3D.material_override](class_geometryinstance3d.md#class_GeometryInstance3D_property_material_override) is used, all surfaces will return the override material.

Returns `null` if no material is active, including when [mesh](class_meshinstance3d.md#class_MeshInstance3D_property_mesh) is `null`.

---

<span id="class_MeshInstance3D_method_get_blend_shape_count"></span>

[int](class_int.md#class_int) **get_blend_shape_count** ( ) *const* [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_get_blend_shape_count)

Returns the number of blend shapes available. Produces an error if [mesh](class_meshinstance3d.md#class_MeshInstance3D_property_mesh) is `null`.

---

<span id="class_MeshInstance3D_method_get_blend_shape_value"></span>

[float](class_float.md#class_float) **get_blend_shape_value** ( blend_shape_idx: [int](class_int.md#class_int) ) *const* [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_get_blend_shape_value)

Returns the value of the blend shape at the given `blend_shape_idx`. Returns `0.0` and produces an error if [mesh](class_meshinstance3d.md#class_MeshInstance3D_property_mesh) is `null` or doesn't have a blend shape at that index.

---

<span id="class_MeshInstance3D_method_get_skin_reference"></span>

[SkinReference](class_skinreference.md#class_SkinReference) **get_skin_reference** ( ) *const* [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_get_skin_reference)

Returns the internal [SkinReference](class_skinreference.md#class_SkinReference) containing the skeleton's [RID](class_rid.md#class_RID) attached to this RID. See also [Resource.get_rid()](class_resource.md#class_Resource_method_get_rid), [SkinReference.get_skeleton()](class_skinreference.md#class_SkinReference_method_get_skeleton), and [RenderingServer.instance_attach_skeleton()](class_renderingserver.md#class_RenderingServer_method_instance_attach_skeleton).

---

<span id="class_MeshInstance3D_method_get_surface_override_material"></span>

[Material](class_material.md#class_Material) **get_surface_override_material** ( surface: [int](class_int.md#class_int) ) *const* [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_get_surface_override_material)

Returns the override [Material](class_material.md#class_Material) for the specified `surface` of the [Mesh](class_mesh.md#class_Mesh) resource. See also [get_surface_override_material_count()](class_meshinstance3d.md#class_MeshInstance3D_method_get_surface_override_material_count).

 **Note:** This returns the [Material](class_material.md#class_Material) associated to the **MeshInstance3D**'s Surface Material Override properties, not the material within the [Mesh](class_mesh.md#class_Mesh) resource. To get the material within the [Mesh](class_mesh.md#class_Mesh) resource, use [Mesh.surface_get_material()](class_mesh.md#class_Mesh_method_surface_get_material) instead.

---

<span id="class_MeshInstance3D_method_get_surface_override_material_count"></span>

[int](class_int.md#class_int) **get_surface_override_material_count** ( ) *const* [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_get_surface_override_material_count)

Returns the number of surface override materials. This is equivalent to [Mesh.get_surface_count()](class_mesh.md#class_Mesh_method_get_surface_count). See also [get_surface_override_material()](class_meshinstance3d.md#class_MeshInstance3D_method_get_surface_override_material).

---

<span id="class_MeshInstance3D_method_set_blend_shape_value"></span>

void **set_blend_shape_value** ( blend_shape_idx: [int](class_int.md#class_int), value: [float](class_float.md#class_float) ) [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_set_blend_shape_value)

Sets the value of the blend shape at `blend_shape_idx` to `value`. Produces an error if [mesh](class_meshinstance3d.md#class_MeshInstance3D_property_mesh) is `null` or doesn't have a blend shape at that index.

---

<span id="class_MeshInstance3D_method_set_surface_override_material"></span>

void **set_surface_override_material** ( surface: [int](class_int.md#class_int), material: [Material](class_material.md#class_Material) ) [🔗](class_meshinstance3d.md#class_MeshInstance3D_method_set_surface_override_material)

Sets the override `material` for the specified `surface` of the [Mesh](class_mesh.md#class_Mesh) resource. This material is associated with this **MeshInstance3D** rather than with [mesh](class_meshinstance3d.md#class_MeshInstance3D_property_mesh).

 **Note:** This assigns the [Material](class_material.md#class_Material) associated to the **MeshInstance3D**'s Surface Material Override properties, not the material within the [Mesh](class_mesh.md#class_Mesh) resource. To set the material within the [Mesh](class_mesh.md#class_Mesh) resource, use [Mesh.surface_set_material()](class_mesh.md#class_Mesh_method_surface_set_material) instead.
