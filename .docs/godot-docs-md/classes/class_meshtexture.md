<span id="class_MeshTexture"></span>

## MeshTexture

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Simple texture that uses a mesh to draw itself.

### Description

Simple texture that uses a mesh to draw itself. It's limited because flags can't be changed and region drawing is not supported.

### Properties


| [Texture2D](class_texture2d.md#class_Texture2D) | [base_texture](class_meshtexture.md#class_MeshTexture_property_base_texture) |
| --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [image_size](class_meshtexture.md#class_MeshTexture_property_image_size) | `Vector2(0, 0)` |
| [Mesh](class_mesh.md#class_Mesh) | [mesh](class_meshtexture.md#class_MeshTexture_property_mesh) |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |

---

### Property Descriptions

<span id="class_MeshTexture_property_base_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **base_texture** [🔗](class_meshtexture.md#class_MeshTexture_property_base_texture)

- void **set_base_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_base_texture** ( )

Sets the base texture that the Mesh will use to draw.

---

<span id="class_MeshTexture_property_image_size"></span>

[Vector2](class_vector2.md#class_Vector2) **image_size** = `Vector2(0, 0)` [🔗](class_meshtexture.md#class_MeshTexture_property_image_size)

- void **set_image_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_image_size** ( )

Sets the size of the image, needed for reference.

---

<span id="class_MeshTexture_property_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **mesh** [🔗](class_meshtexture.md#class_MeshTexture_property_mesh)

- void **set_mesh** ( value: [Mesh](class_mesh.md#class_Mesh) )
- [Mesh](class_mesh.md#class_Mesh) **get_mesh** ( )

Sets the mesh used to draw. It must be a mesh using 2D vertices.
