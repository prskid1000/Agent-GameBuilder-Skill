<span id="class_GLTFAnimation"></span>

## GLTFAnimation

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

.. container:: contribute

	There is currently no description for this class. Please help us by contributing one!

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [bool](class_bool.md#class_bool) | [loop](class_gltfanimation.md#class_GLTFAnimation_property_loop) | `false` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [original_name](class_gltfanimation.md#class_GLTFAnimation_property_original_name) | `""` |

### Methods


| [Variant](class_variant.md#class_Variant) | [get_additional_data](class_gltfanimation.md#class_GLTFAnimation_method_get_additional_data) ( extension_name: [StringName](class_stringname.md#class_StringName) ) |
| --- | --- |
| void | [set_additional_data](class_gltfanimation.md#class_GLTFAnimation_method_set_additional_data) ( extension_name: [StringName](class_stringname.md#class_StringName), additional_data: [Variant](class_variant.md#class_Variant) ) |

---

### Property Descriptions

<span id="class_GLTFAnimation_property_loop"></span>

[bool](class_bool.md#class_bool) **loop** = `false` [🔗](class_gltfanimation.md#class_GLTFAnimation_property_loop)

- void **set_loop** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_loop** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_GLTFAnimation_property_original_name"></span>

[String](class_string.md#class_String) **original_name** = `""` [🔗](class_gltfanimation.md#class_GLTFAnimation_property_original_name)

- void **set_original_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_original_name** ( )

The original name of the animation.

---

### Method Descriptions

<span id="class_GLTFAnimation_method_get_additional_data"></span>

[Variant](class_variant.md#class_Variant) **get_additional_data** ( extension_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_gltfanimation.md#class_GLTFAnimation_method_get_additional_data)

Gets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.

---

<span id="class_GLTFAnimation_method_set_additional_data"></span>

void **set_additional_data** ( extension_name: [StringName](class_stringname.md#class_StringName), additional_data: [Variant](class_variant.md#class_Variant) ) [🔗](class_gltfanimation.md#class_GLTFAnimation_method_set_additional_data)

Sets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.
