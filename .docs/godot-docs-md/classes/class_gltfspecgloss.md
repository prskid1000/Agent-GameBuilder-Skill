<span id="class_GLTFSpecGloss"></span>

## GLTFSpecGloss

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Archived glTF extension for specular/glossy materials.

### Description

KHR_materials_pbrSpecularGlossiness is an archived glTF extension. This means that it is deprecated and not recommended for new files. However, it is still supported for loading old files.

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

- KHR_materials_pbrSpecularGlossiness glTF extension spec

### Properties


| [Color](class_color.md#class_Color) | [diffuse_factor](class_gltfspecgloss.md#class_GLTFSpecGloss_property_diffuse_factor) | `Color(1, 1, 1, 1)` |
| --- | --- | --- |
| [Image](class_image.md#class_Image) | [diffuse_img](class_gltfspecgloss.md#class_GLTFSpecGloss_property_diffuse_img) |
| [float](class_float.md#class_float) | [gloss_factor](class_gltfspecgloss.md#class_GLTFSpecGloss_property_gloss_factor) | `1.0` |
| [Image](class_image.md#class_Image) | [spec_gloss_img](class_gltfspecgloss.md#class_GLTFSpecGloss_property_spec_gloss_img) |
| [Color](class_color.md#class_Color) | [specular_factor](class_gltfspecgloss.md#class_GLTFSpecGloss_property_specular_factor) | `Color(1, 1, 1, 1)` |

---

### Property Descriptions

<span id="class_GLTFSpecGloss_property_diffuse_factor"></span>

[Color](class_color.md#class_Color) **diffuse_factor** = `Color(1, 1, 1, 1)` [🔗](class_gltfspecgloss.md#class_GLTFSpecGloss_property_diffuse_factor)

- void **set_diffuse_factor** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_diffuse_factor** ( )

The reflected diffuse factor of the material.

---

<span id="class_GLTFSpecGloss_property_diffuse_img"></span>

[Image](class_image.md#class_Image) **diffuse_img** [🔗](class_gltfspecgloss.md#class_GLTFSpecGloss_property_diffuse_img)

- void **set_diffuse_img** ( value: [Image](class_image.md#class_Image) )
- [Image](class_image.md#class_Image) **get_diffuse_img** ( )

The diffuse texture.

---

<span id="class_GLTFSpecGloss_property_gloss_factor"></span>

[float](class_float.md#class_float) **gloss_factor** = `1.0` [🔗](class_gltfspecgloss.md#class_GLTFSpecGloss_property_gloss_factor)

- void **set_gloss_factor** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_gloss_factor** ( )

The glossiness or smoothness of the material.

---

<span id="class_GLTFSpecGloss_property_spec_gloss_img"></span>

[Image](class_image.md#class_Image) **spec_gloss_img** [🔗](class_gltfspecgloss.md#class_GLTFSpecGloss_property_spec_gloss_img)

- void **set_spec_gloss_img** ( value: [Image](class_image.md#class_Image) )
- [Image](class_image.md#class_Image) **get_spec_gloss_img** ( )

The specular-glossiness texture.

---

<span id="class_GLTFSpecGloss_property_specular_factor"></span>

[Color](class_color.md#class_Color) **specular_factor** = `Color(1, 1, 1, 1)` [🔗](class_gltfspecgloss.md#class_GLTFSpecGloss_property_specular_factor)

- void **set_specular_factor** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_specular_factor** ( )

The specular RGB color of the material. The alpha channel is unused.
