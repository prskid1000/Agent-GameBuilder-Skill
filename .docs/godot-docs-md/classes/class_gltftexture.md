<span id="class_GLTFTexture"></span>

## GLTFTexture

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

GLTFTexture represents a texture in a glTF file.

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [int](class_int.md#class_int) | [sampler](class_gltftexture.md#class_GLTFTexture_property_sampler) | `-1` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [src_image](class_gltftexture.md#class_GLTFTexture_property_src_image) | `-1` |

---

### Property Descriptions

<span id="class_GLTFTexture_property_sampler"></span>

[int](class_int.md#class_int) **sampler** = `-1` [🔗](class_gltftexture.md#class_GLTFTexture_property_sampler)

- void **set_sampler** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sampler** ( )

ID of the texture sampler to use when sampling the image. If -1, then the default texture sampler is used (linear filtering, and repeat wrapping in both axes).

---

<span id="class_GLTFTexture_property_src_image"></span>

[int](class_int.md#class_int) **src_image** = `-1` [🔗](class_gltftexture.md#class_GLTFTexture_property_src_image)

- void **set_src_image** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_src_image** ( )

The index of the image associated with this texture, see [GLTFState.get_images()](class_gltfstate.md#class_GLTFState_method_get_images). If -1, then this texture does not have an image assigned.
