<span id="class_MeshLibrary"></span>

## MeshLibrary

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Library of meshes.

### Description

A library of meshes. Contains a list of [Mesh](class_mesh.md#class_Mesh) resources, each with a name and ID. Each item can also include collision and navigation shapes. This resource is used in [GridMap](class_gridmap.md#class_GridMap).

### Tutorials

- 3D Kinematic Character Demo

- 3D Platformer Demo

### Methods


| void | [clear](class_meshlibrary.md#class_MeshLibrary_method_clear) ( ) |
| --- | --- |
| void | [create_item](class_meshlibrary.md#class_MeshLibrary_method_create_item) ( id: [int](class_int.md#class_int) ) |
| [int](class_int.md#class_int) | [find_item_by_name](class_meshlibrary.md#class_MeshLibrary_method_find_item_by_name) ( name: [String](class_string.md#class_String) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_item_list](class_meshlibrary.md#class_MeshLibrary_method_get_item_list) ( ) const |
| [Mesh](class_mesh.md#class_Mesh) | [get_item_mesh](class_meshlibrary.md#class_MeshLibrary_method_get_item_mesh) ( id: [int](class_int.md#class_int) ) const |
| [ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) | [get_item_mesh_cast_shadow](class_meshlibrary.md#class_MeshLibrary_method_get_item_mesh_cast_shadow) ( id: [int](class_int.md#class_int) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_item_mesh_transform](class_meshlibrary.md#class_MeshLibrary_method_get_item_mesh_transform) ( id: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_item_name](class_meshlibrary.md#class_MeshLibrary_method_get_item_name) ( id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_item_navigation_layers](class_meshlibrary.md#class_MeshLibrary_method_get_item_navigation_layers) ( id: [int](class_int.md#class_int) ) const |
| [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) | [get_item_navigation_mesh](class_meshlibrary.md#class_MeshLibrary_method_get_item_navigation_mesh) ( id: [int](class_int.md#class_int) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_item_navigation_mesh_transform](class_meshlibrary.md#class_MeshLibrary_method_get_item_navigation_mesh_transform) ( id: [int](class_int.md#class_int) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_item_preview](class_meshlibrary.md#class_MeshLibrary_method_get_item_preview) ( id: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array) | [get_item_shapes](class_meshlibrary.md#class_MeshLibrary_method_get_item_shapes) ( id: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_last_unused_item_id](class_meshlibrary.md#class_MeshLibrary_method_get_last_unused_item_id) ( ) const |
| void | [remove_item](class_meshlibrary.md#class_MeshLibrary_method_remove_item) ( id: [int](class_int.md#class_int) ) |
| void | [set_item_mesh](class_meshlibrary.md#class_MeshLibrary_method_set_item_mesh) ( id: [int](class_int.md#class_int), mesh: [Mesh](class_mesh.md#class_Mesh) ) |
| void | [set_item_mesh_cast_shadow](class_meshlibrary.md#class_MeshLibrary_method_set_item_mesh_cast_shadow) ( id: [int](class_int.md#class_int), shadow_casting_setting: [ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) ) |
| void | [set_item_mesh_transform](class_meshlibrary.md#class_MeshLibrary_method_set_item_mesh_transform) ( id: [int](class_int.md#class_int), mesh_transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [set_item_name](class_meshlibrary.md#class_MeshLibrary_method_set_item_name) ( id: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) |
| void | [set_item_navigation_layers](class_meshlibrary.md#class_MeshLibrary_method_set_item_navigation_layers) ( id: [int](class_int.md#class_int), navigation_layers: [int](class_int.md#class_int) ) |
| void | [set_item_navigation_mesh](class_meshlibrary.md#class_MeshLibrary_method_set_item_navigation_mesh) ( id: [int](class_int.md#class_int), navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) ) |
| void | [set_item_navigation_mesh_transform](class_meshlibrary.md#class_MeshLibrary_method_set_item_navigation_mesh_transform) ( id: [int](class_int.md#class_int), navigation_mesh: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [set_item_preview](class_meshlibrary.md#class_MeshLibrary_method_set_item_preview) ( id: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |
| void | [set_item_shapes](class_meshlibrary.md#class_MeshLibrary_method_set_item_shapes) ( id: [int](class_int.md#class_int), shapes: [Array](class_array.md#class_Array) ) |

---

### Method Descriptions

<span id="class_MeshLibrary_method_clear"></span>

void **clear** ( ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_clear)

Clears the library.

---

<span id="class_MeshLibrary_method_create_item"></span>

void **create_item** ( id: [int](class_int.md#class_int) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_create_item)

Creates a new item in the library with the given ID.

You can get an unused ID from [get_last_unused_item_id()](class_meshlibrary.md#class_MeshLibrary_method_get_last_unused_item_id).

---

<span id="class_MeshLibrary_method_find_item_by_name"></span>

[int](class_int.md#class_int) **find_item_by_name** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_find_item_by_name)

Returns the first item with the given name, or `-1` if no item is found.

---

<span id="class_MeshLibrary_method_get_item_list"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_item_list** ( ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_list)

Returns the list of item IDs in use.

---

<span id="class_MeshLibrary_method_get_item_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **get_item_mesh** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_mesh)

Returns the item's mesh.

---

<span id="class_MeshLibrary_method_get_item_mesh_cast_shadow"></span>

[ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) **get_item_mesh_cast_shadow** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_mesh_cast_shadow)

Returns the item's shadow casting mode.

---

<span id="class_MeshLibrary_method_get_item_mesh_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_item_mesh_transform** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_mesh_transform)

Returns the transform applied to the item's mesh.

---

<span id="class_MeshLibrary_method_get_item_name"></span>

[String](class_string.md#class_String) **get_item_name** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_name)

Returns the item's name.

---

<span id="class_MeshLibrary_method_get_item_navigation_layers"></span>

[int](class_int.md#class_int) **get_item_navigation_layers** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_navigation_layers)

Returns the item's navigation layers bitmask.

---

<span id="class_MeshLibrary_method_get_item_navigation_mesh"></span>

[NavigationMesh](class_navigationmesh.md#class_NavigationMesh) **get_item_navigation_mesh** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_navigation_mesh)

Returns the item's navigation mesh.

---

<span id="class_MeshLibrary_method_get_item_navigation_mesh_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_item_navigation_mesh_transform** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_navigation_mesh_transform)

Returns the transform applied to the item's navigation mesh.

---

<span id="class_MeshLibrary_method_get_item_preview"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_item_preview** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_preview)

When running in the editor, returns a generated item preview (a 3D rendering in isometric perspective). When used in a running project, returns the manually-defined item preview which can be set using [set_item_preview()](class_meshlibrary.md#class_MeshLibrary_method_set_item_preview). Returns an empty [Texture2D](class_texture2d.md#class_Texture2D) if no preview was manually set in a running project.

---

<span id="class_MeshLibrary_method_get_item_shapes"></span>

[Array](class_array.md#class_Array) **get_item_shapes** ( id: [int](class_int.md#class_int) ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_item_shapes)

Returns an item's collision shapes.

The array consists of each [Shape3D](class_shape3d.md#class_Shape3D) followed by its [Transform3D](class_transform3d.md#class_Transform3D).

---

<span id="class_MeshLibrary_method_get_last_unused_item_id"></span>

[int](class_int.md#class_int) **get_last_unused_item_id** ( ) *const* [🔗](class_meshlibrary.md#class_MeshLibrary_method_get_last_unused_item_id)

Gets an unused ID for a new item.

---

<span id="class_MeshLibrary_method_remove_item"></span>

void **remove_item** ( id: [int](class_int.md#class_int) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_remove_item)

Removes the item.

---

<span id="class_MeshLibrary_method_set_item_mesh"></span>

void **set_item_mesh** ( id: [int](class_int.md#class_int), mesh: [Mesh](class_mesh.md#class_Mesh) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_set_item_mesh)

Sets the item's mesh.

---

<span id="class_MeshLibrary_method_set_item_mesh_cast_shadow"></span>

void **set_item_mesh_cast_shadow** ( id: [int](class_int.md#class_int), shadow_casting_setting: [ShadowCastingSetting](class_renderingserver.md#enum_RenderingServer_ShadowCastingSetting) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_set_item_mesh_cast_shadow)

Sets the item's shadow casting mode to `shadow_casting_setting`.

---

<span id="class_MeshLibrary_method_set_item_mesh_transform"></span>

void **set_item_mesh_transform** ( id: [int](class_int.md#class_int), mesh_transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_set_item_mesh_transform)

Sets the transform to apply to the item's mesh.

---

<span id="class_MeshLibrary_method_set_item_name"></span>

void **set_item_name** ( id: [int](class_int.md#class_int), name: [String](class_string.md#class_String) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_set_item_name)

Sets the item's name.

This name is shown in the editor. It can also be used to look up the item later using [find_item_by_name()](class_meshlibrary.md#class_MeshLibrary_method_find_item_by_name).

---

<span id="class_MeshLibrary_method_set_item_navigation_layers"></span>

void **set_item_navigation_layers** ( id: [int](class_int.md#class_int), navigation_layers: [int](class_int.md#class_int) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_set_item_navigation_layers)

Sets the item's navigation layers bitmask.

---

<span id="class_MeshLibrary_method_set_item_navigation_mesh"></span>

void **set_item_navigation_mesh** ( id: [int](class_int.md#class_int), navigation_mesh: [NavigationMesh](class_navigationmesh.md#class_NavigationMesh) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_set_item_navigation_mesh)

Sets the item's navigation mesh.

---

<span id="class_MeshLibrary_method_set_item_navigation_mesh_transform"></span>

void **set_item_navigation_mesh_transform** ( id: [int](class_int.md#class_int), navigation_mesh: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_set_item_navigation_mesh_transform)

Sets the transform to apply to the item's navigation mesh.

---

<span id="class_MeshLibrary_method_set_item_preview"></span>

void **set_item_preview** ( id: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_set_item_preview)

Sets a texture to use as the item's preview icon in the editor.

---

<span id="class_MeshLibrary_method_set_item_shapes"></span>

void **set_item_shapes** ( id: [int](class_int.md#class_int), shapes: [Array](class_array.md#class_Array) ) [🔗](class_meshlibrary.md#class_MeshLibrary_method_set_item_shapes)

Sets an item's collision shapes.

The array should consist of [Shape3D](class_shape3d.md#class_Shape3D) objects, each followed by a [Transform3D](class_transform3d.md#class_Transform3D) that will be applied to it. For shapes that should not have a transform, use [Transform3D.IDENTITY](class_transform3d.md#class_Transform3D_constant_IDENTITY).
