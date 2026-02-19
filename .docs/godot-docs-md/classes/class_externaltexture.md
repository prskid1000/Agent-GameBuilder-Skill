<span id="class_ExternalTexture"></span>

## ExternalTexture

**Inherits:** [Texture2D](class_texture2d.md#class_Texture2D) **<** [Texture](class_texture.md#class_Texture) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Texture which displays the content of an external buffer.

### Description

Displays the content of an external buffer provided by the platform.

Requires the OES_EGL_image_external extension (OpenGL) or VK_ANDROID_external_memory_android_hardware_buffer extension (Vulkan).

 **Note:** This is currently only supported in Android builds.

### Properties


| [bool](class_bool.md#class_bool) | resource_local_to_scene | `false` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [size](class_externaltexture.md#class_ExternalTexture_property_size) | `Vector2(256, 256)` |

### Methods


| [int](class_int.md#class_int) | [get_external_texture_id](class_externaltexture.md#class_ExternalTexture_method_get_external_texture_id) ( ) const |
| --- | --- |
| void | [set_external_buffer_id](class_externaltexture.md#class_ExternalTexture_method_set_external_buffer_id) ( external_buffer_id: [int](class_int.md#class_int) ) |

---

### Property Descriptions

<span id="class_ExternalTexture_property_size"></span>

[Vector2](class_vector2.md#class_Vector2) **size** = `Vector2(256, 256)` [🔗](class_externaltexture.md#class_ExternalTexture_property_size)

- void **set_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_size** ( )

External texture size.

---

### Method Descriptions

<span id="class_ExternalTexture_method_get_external_texture_id"></span>

[int](class_int.md#class_int) **get_external_texture_id** ( ) *const* [🔗](class_externaltexture.md#class_ExternalTexture_method_get_external_texture_id)

Returns the external texture ID.

Depending on your use case, you may need to pass this to platform APIs, for example, when creating an `android.graphics.SurfaceTexture` on Android.

---

<span id="class_ExternalTexture_method_set_external_buffer_id"></span>

void **set_external_buffer_id** ( external_buffer_id: [int](class_int.md#class_int) ) [🔗](class_externaltexture.md#class_ExternalTexture_method_set_external_buffer_id)

Sets the external buffer ID.

Depending on your use case, you may need to call this with data received from a platform API, for example, `SurfaceTexture.getHardwareBuffer()` on Android.
