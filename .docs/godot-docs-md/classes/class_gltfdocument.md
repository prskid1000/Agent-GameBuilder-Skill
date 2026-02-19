<span id="class_GLTFDocument"></span>

## GLTFDocument

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [FBXDocument](class_fbxdocument.md#class_FBXDocument)

Class for importing and exporting glTF files in and out of Godot.

### Description

GLTFDocument supports reading data from a glTF file, buffer, or Godot scene. This data can then be written to the filesystem, buffer, or used to create a Godot scene.

All of the data in a glTF scene is stored in the [GLTFState](class_gltfstate.md#class_GLTFState) class. GLTFDocument processes state objects, but does not contain any scene data itself. GLTFDocument has member variables to store export configuration settings such as the image format, but is otherwise stateless. Multiple scenes can be processed with the same settings using the same GLTFDocument object and different [GLTFState](class_gltfstate.md#class_GLTFState) objects.

GLTFDocument can be extended with arbitrary functionality by extending the [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) class and registering it with GLTFDocument via [register_gltf_document_extension()](class_gltfdocument.md#class_GLTFDocument_method_register_gltf_document_extension). This allows for custom data to be imported and exported.

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

- glTF 'What the duck?' guide

- Khronos glTF specification

### Properties


| [String](class_string.md#class_String) | [fallback_image_format](class_gltfdocument.md#class_GLTFDocument_property_fallback_image_format) | `"None"` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [fallback_image_quality](class_gltfdocument.md#class_GLTFDocument_property_fallback_image_quality) | `0.25` |
| [String](class_string.md#class_String) | [image_format](class_gltfdocument.md#class_GLTFDocument_property_image_format) | `"PNG"` |
| [float](class_float.md#class_float) | [lossy_quality](class_gltfdocument.md#class_GLTFDocument_property_lossy_quality) | `0.75` |
| [RootNodeMode](class_gltfdocument.md#enum_GLTFDocument_RootNodeMode) | [root_node_mode](class_gltfdocument.md#class_GLTFDocument_property_root_node_mode) | `0` |
| [VisibilityMode](class_gltfdocument.md#enum_GLTFDocument_VisibilityMode) | [visibility_mode](class_gltfdocument.md#class_GLTFDocument_property_visibility_mode) | `0` |

### Methods


| Error | [append_from_buffer](class_gltfdocument.md#class_GLTFDocument_method_append_from_buffer) ( bytes: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), base_path: [String](class_string.md#class_String), state: [GLTFState](class_gltfstate.md#class_GLTFState), flags: [int](class_int.md#class_int) = 0 ) |
| --- | --- |
| Error | [append_from_file](class_gltfdocument.md#class_GLTFDocument_method_append_from_file) ( path: [String](class_string.md#class_String), state: [GLTFState](class_gltfstate.md#class_GLTFState), flags: [int](class_int.md#class_int) = 0, base_path: [String](class_string.md#class_String) = "" ) |
| Error | [append_from_scene](class_gltfdocument.md#class_GLTFDocument_method_append_from_scene) ( node: [Node](class_node.md#class_Node), state: [GLTFState](class_gltfstate.md#class_GLTFState), flags: [int](class_int.md#class_int) = 0 ) |
| [GLTFObjectModelProperty](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty) | [export_object_model_property](class_gltfdocument.md#class_GLTFDocument_method_export_object_model_property) ( state: [GLTFState](class_gltfstate.md#class_GLTFState), node_path: [NodePath](class_nodepath.md#class_NodePath), godot_node: [Node](class_node.md#class_Node), gltf_node_index: [int](class_int.md#class_int) ) static |
| [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) | [generate_buffer](class_gltfdocument.md#class_GLTFDocument_method_generate_buffer) ( state: [GLTFState](class_gltfstate.md#class_GLTFState) ) |
| [Node](class_node.md#class_Node) | [generate_scene](class_gltfdocument.md#class_GLTFDocument_method_generate_scene) ( state: [GLTFState](class_gltfstate.md#class_GLTFState), bake_fps: [float](class_float.md#class_float) = 30, trimming: [bool](class_bool.md#class_bool) = false, remove_immutable_tracks: [bool](class_bool.md#class_bool) = true ) |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_supported_gltf_extensions](class_gltfdocument.md#class_GLTFDocument_method_get_supported_gltf_extensions) ( ) static |
| [GLTFObjectModelProperty](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty) | [import_object_model_property](class_gltfdocument.md#class_GLTFDocument_method_import_object_model_property) ( state: [GLTFState](class_gltfstate.md#class_GLTFState), json_pointer: [String](class_string.md#class_String) ) static |
| void | [register_gltf_document_extension](class_gltfdocument.md#class_GLTFDocument_method_register_gltf_document_extension) ( extension: [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension), first_priority: [bool](class_bool.md#class_bool) = false ) static |
| void | [unregister_gltf_document_extension](class_gltfdocument.md#class_GLTFDocument_method_unregister_gltf_document_extension) ( extension: [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) ) static |
| Error | [write_to_filesystem](class_gltfdocument.md#class_GLTFDocument_method_write_to_filesystem) ( state: [GLTFState](class_gltfstate.md#class_GLTFState), path: [String](class_string.md#class_String) ) |

---

### Enumerations

<span id="enum_GLTFDocument_RootNodeMode"></span>

enum **RootNodeMode**: [🔗](class_gltfdocument.md#enum_GLTFDocument_RootNodeMode)

<span id="class_GLTFDocument_constant_ROOT_NODE_MODE_SINGLE_ROOT"></span>

[RootNodeMode](class_gltfdocument.md#enum_GLTFDocument_RootNodeMode) **ROOT_NODE_MODE_SINGLE_ROOT** = `0`

Treat the Godot scene's root node as the root node of the glTF file, and mark it as the single root node via the `GODOT_single_root` glTF extension. This will be parsed the same as [ROOT_NODE_MODE_KEEP_ROOT](class_gltfdocument.md#class_GLTFDocument_constant_ROOT_NODE_MODE_KEEP_ROOT) if the implementation does not support `GODOT_single_root`.

<span id="class_GLTFDocument_constant_ROOT_NODE_MODE_KEEP_ROOT"></span>

[RootNodeMode](class_gltfdocument.md#enum_GLTFDocument_RootNodeMode) **ROOT_NODE_MODE_KEEP_ROOT** = `1`

Treat the Godot scene's root node as the root node of the glTF file, but do not mark it as anything special. An extra root node will be generated when importing into Godot. This uses only vanilla glTF features. This is equivalent to the behavior in Godot 4.1 and earlier.

<span id="class_GLTFDocument_constant_ROOT_NODE_MODE_MULTI_ROOT"></span>

[RootNodeMode](class_gltfdocument.md#enum_GLTFDocument_RootNodeMode) **ROOT_NODE_MODE_MULTI_ROOT** = `2`

Treat the Godot scene's root node as the name of the glTF scene, and add all of its children as root nodes of the glTF file. This uses only vanilla glTF features. This avoids an extra root node, but only the name of the Godot scene's root node will be preserved, as it will not be saved as a node.

---

<span id="enum_GLTFDocument_VisibilityMode"></span>

enum **VisibilityMode**: [🔗](class_gltfdocument.md#enum_GLTFDocument_VisibilityMode)

<span id="class_GLTFDocument_constant_VISIBILITY_MODE_INCLUDE_REQUIRED"></span>

[VisibilityMode](class_gltfdocument.md#enum_GLTFDocument_VisibilityMode) **VISIBILITY_MODE_INCLUDE_REQUIRED** = `0`

If the scene contains any non-visible nodes, include them, mark them as non-visible with `KHR_node_visibility`, and require that importers respect their non-visibility. Downside: If the importer does not support `KHR_node_visibility`, the file cannot be imported.

<span id="class_GLTFDocument_constant_VISIBILITY_MODE_INCLUDE_OPTIONAL"></span>

[VisibilityMode](class_gltfdocument.md#enum_GLTFDocument_VisibilityMode) **VISIBILITY_MODE_INCLUDE_OPTIONAL** = `1`

If the scene contains any non-visible nodes, include them, mark them as non-visible with `KHR_node_visibility`, and do not impose any requirements on importers. Downside: If the importer does not support `KHR_node_visibility`, invisible objects will be visible.

<span id="class_GLTFDocument_constant_VISIBILITY_MODE_EXCLUDE"></span>

[VisibilityMode](class_gltfdocument.md#enum_GLTFDocument_VisibilityMode) **VISIBILITY_MODE_EXCLUDE** = `2`

If the scene contains any non-visible nodes, do not include them in the export. This is the same as the behavior in Godot 4.4 and earlier. Downside: Invisible nodes will not exist in the exported file.

---

### Property Descriptions

<span id="class_GLTFDocument_property_fallback_image_format"></span>

[String](class_string.md#class_String) **fallback_image_format** = `"None"` [🔗](class_gltfdocument.md#class_GLTFDocument_property_fallback_image_format)

- void **set_fallback_image_format** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_fallback_image_format** ( )

The user-friendly name of the fallback image format. This is used when exporting the glTF file, including writing to a file and writing to a byte array.

This property may only be one of "None", "PNG", or "JPEG", and is only used when the [image_format](class_gltfdocument.md#class_GLTFDocument_property_image_format) is not one of "None", "PNG", or "JPEG". If having multiple extension image formats is desired, that can be done using a [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) class - this property only covers the use case of providing a base glTF fallback image when using a custom image format.

---

<span id="class_GLTFDocument_property_fallback_image_quality"></span>

[float](class_float.md#class_float) **fallback_image_quality** = `0.25` [🔗](class_gltfdocument.md#class_GLTFDocument_property_fallback_image_quality)

- void **set_fallback_image_quality** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fallback_image_quality** ( )

The quality of the fallback image, if any. For PNG files, this downscales the image on both dimensions by this factor. For JPEG files, this is the lossy quality of the image. A low value is recommended, since including multiple high quality images in a glTF file defeats the file size gains of using a more efficient image format.

---

<span id="class_GLTFDocument_property_image_format"></span>

[String](class_string.md#class_String) **image_format** = `"PNG"` [🔗](class_gltfdocument.md#class_GLTFDocument_property_image_format)

- void **set_image_format** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_image_format** ( )

The user-friendly name of the export image format. This is used when exporting the glTF file, including writing to a file and writing to a byte array.

By default, Godot allows the following options: "None", "PNG", "JPEG", "Lossless WebP", and "Lossy WebP". Support for more image formats can be added in [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) classes. A single extension class can provide multiple options for the specific format to use, or even an option that uses multiple formats at once.

---

<span id="class_GLTFDocument_property_lossy_quality"></span>

[float](class_float.md#class_float) **lossy_quality** = `0.75` [🔗](class_gltfdocument.md#class_GLTFDocument_property_lossy_quality)

- void **set_lossy_quality** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_lossy_quality** ( )

If [image_format](class_gltfdocument.md#class_GLTFDocument_property_image_format) is a lossy image format, this determines the lossy quality of the image. On a range of `0.0` to `1.0`, where `0.0` is the lowest quality and `1.0` is the highest quality. A lossy quality of `1.0` is not the same as lossless.

---

<span id="class_GLTFDocument_property_root_node_mode"></span>

[RootNodeMode](class_gltfdocument.md#enum_GLTFDocument_RootNodeMode) **root_node_mode** = `0` [🔗](class_gltfdocument.md#class_GLTFDocument_property_root_node_mode)

- void **set_root_node_mode** ( value: [RootNodeMode](class_gltfdocument.md#enum_GLTFDocument_RootNodeMode) )
- [RootNodeMode](class_gltfdocument.md#enum_GLTFDocument_RootNodeMode) **get_root_node_mode** ( )

How to process the root node during export. The default and recommended value is [ROOT_NODE_MODE_SINGLE_ROOT](class_gltfdocument.md#class_GLTFDocument_constant_ROOT_NODE_MODE_SINGLE_ROOT).

 **Note:** Regardless of how the glTF file is exported, when importing, the root node type and name can be overridden in the scene import settings tab.

---

<span id="class_GLTFDocument_property_visibility_mode"></span>

[VisibilityMode](class_gltfdocument.md#enum_GLTFDocument_VisibilityMode) **visibility_mode** = `0` [🔗](class_gltfdocument.md#class_GLTFDocument_property_visibility_mode)

- void **set_visibility_mode** ( value: [VisibilityMode](class_gltfdocument.md#enum_GLTFDocument_VisibilityMode) )
- [VisibilityMode](class_gltfdocument.md#enum_GLTFDocument_VisibilityMode) **get_visibility_mode** ( )

How to deal with node visibility during export. This setting does nothing if all nodes are visible. The default and recommended value is [VISIBILITY_MODE_INCLUDE_REQUIRED](class_gltfdocument.md#class_GLTFDocument_constant_VISIBILITY_MODE_INCLUDE_REQUIRED), which uses the `KHR_node_visibility` extension.

---

### Method Descriptions

<span id="class_GLTFDocument_method_append_from_buffer"></span>

Error **append_from_buffer** ( bytes: [PackedByteArray](class_packedbytearray.md#class_PackedByteArray), base_path: [String](class_string.md#class_String), state: [GLTFState](class_gltfstate.md#class_GLTFState), flags: [int](class_int.md#class_int) = 0 ) [🔗](class_gltfdocument.md#class_GLTFDocument_method_append_from_buffer)

Takes a [PackedByteArray](class_packedbytearray.md#class_PackedByteArray) defining a glTF and imports the data to the given [GLTFState](class_gltfstate.md#class_GLTFState) object through the `state` parameter.

 **Note:** The `base_path` tells [append_from_buffer()](class_gltfdocument.md#class_GLTFDocument_method_append_from_buffer) where to find dependencies and can be empty.

---

<span id="class_GLTFDocument_method_append_from_file"></span>

Error **append_from_file** ( path: [String](class_string.md#class_String), state: [GLTFState](class_gltfstate.md#class_GLTFState), flags: [int](class_int.md#class_int) = 0, base_path: [String](class_string.md#class_String) = "" ) [🔗](class_gltfdocument.md#class_GLTFDocument_method_append_from_file)

Takes a path to a glTF file and imports the data at that file path to the given [GLTFState](class_gltfstate.md#class_GLTFState) object through the `state` parameter.

 **Note:** The `base_path` tells [append_from_file()](class_gltfdocument.md#class_GLTFDocument_method_append_from_file) where to find dependencies and can be empty.

---

<span id="class_GLTFDocument_method_append_from_scene"></span>

Error **append_from_scene** ( node: [Node](class_node.md#class_Node), state: [GLTFState](class_gltfstate.md#class_GLTFState), flags: [int](class_int.md#class_int) = 0 ) [🔗](class_gltfdocument.md#class_GLTFDocument_method_append_from_scene)

Takes a Godot Engine scene node and exports it and its descendants to the given [GLTFState](class_gltfstate.md#class_GLTFState) object through the `state` parameter.

---

<span id="class_GLTFDocument_method_export_object_model_property"></span>

[GLTFObjectModelProperty](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty) **export_object_model_property** ( state: [GLTFState](class_gltfstate.md#class_GLTFState), node_path: [NodePath](class_nodepath.md#class_NodePath), godot_node: [Node](class_node.md#class_Node), gltf_node_index: [int](class_int.md#class_int) ) *static* [🔗](class_gltfdocument.md#class_GLTFDocument_method_export_object_model_property)

Determines a mapping between the given Godot `node_path` and the corresponding glTF Object Model JSON pointer(s) in the generated glTF file. The details of this mapping are returned in a [GLTFObjectModelProperty](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty) object. Additional mappings can be supplied via the [GLTFDocumentExtension._import_object_model_property()](class_gltfdocumentextension.md#class_GLTFDocumentExtension_private_method__import_object_model_property) callback method.

---

<span id="class_GLTFDocument_method_generate_buffer"></span>

[PackedByteArray](class_packedbytearray.md#class_PackedByteArray) **generate_buffer** ( state: [GLTFState](class_gltfstate.md#class_GLTFState) ) [🔗](class_gltfdocument.md#class_GLTFDocument_method_generate_buffer)

Takes a [GLTFState](class_gltfstate.md#class_GLTFState) object through the `state` parameter and returns a glTF [PackedByteArray](class_packedbytearray.md#class_PackedByteArray).

---

<span id="class_GLTFDocument_method_generate_scene"></span>

[Node](class_node.md#class_Node) **generate_scene** ( state: [GLTFState](class_gltfstate.md#class_GLTFState), bake_fps: [float](class_float.md#class_float) = 30, trimming: [bool](class_bool.md#class_bool) = false, remove_immutable_tracks: [bool](class_bool.md#class_bool) = true ) [🔗](class_gltfdocument.md#class_GLTFDocument_method_generate_scene)

Takes a [GLTFState](class_gltfstate.md#class_GLTFState) object through the `state` parameter and returns a Godot Engine scene node.

The `bake_fps` parameter overrides the bake_fps in `state`.

---

<span id="class_GLTFDocument_method_get_supported_gltf_extensions"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_supported_gltf_extensions** ( ) *static* [🔗](class_gltfdocument.md#class_GLTFDocument_method_get_supported_gltf_extensions)

Returns a list of all support glTF extensions, including extensions supported directly by the engine, and extensions supported by user plugins registering [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) classes.

 **Note:** If this method is run before a GLTFDocumentExtension is registered, its extensions won't be included in the list. Be sure to only run this method after all extensions are registered. If you run this when the engine starts, consider waiting a frame before calling this method to ensure all extensions are registered.

---

<span id="class_GLTFDocument_method_import_object_model_property"></span>

[GLTFObjectModelProperty](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty) **import_object_model_property** ( state: [GLTFState](class_gltfstate.md#class_GLTFState), json_pointer: [String](class_string.md#class_String) ) *static* [🔗](class_gltfdocument.md#class_GLTFDocument_method_import_object_model_property)

Determines a mapping between the given glTF Object Model `json_pointer` and the corresponding Godot node path(s) in the generated Godot scene. The details of this mapping are returned in a [GLTFObjectModelProperty](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty) object. Additional mappings can be supplied via the [GLTFDocumentExtension._export_object_model_property()](class_gltfdocumentextension.md#class_GLTFDocumentExtension_private_method__export_object_model_property) callback method.

---

<span id="class_GLTFDocument_method_register_gltf_document_extension"></span>

void **register_gltf_document_extension** ( extension: [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension), first_priority: [bool](class_bool.md#class_bool) = false ) *static* [🔗](class_gltfdocument.md#class_GLTFDocument_method_register_gltf_document_extension)

Registers the given [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) instance with GLTFDocument. If `first_priority` is `true`, this extension will be run first. Otherwise, it will be run last.

 **Note:** Like GLTFDocument itself, all GLTFDocumentExtension classes must be stateless in order to function properly. If you need to store data, use the `set_additional_data` and `get_additional_data` methods in [GLTFState](class_gltfstate.md#class_GLTFState) or [GLTFNode](class_gltfnode.md#class_GLTFNode).

---

<span id="class_GLTFDocument_method_unregister_gltf_document_extension"></span>

void **unregister_gltf_document_extension** ( extension: [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) ) *static* [🔗](class_gltfdocument.md#class_GLTFDocument_method_unregister_gltf_document_extension)

Unregisters the given [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) instance.

---

<span id="class_GLTFDocument_method_write_to_filesystem"></span>

Error **write_to_filesystem** ( state: [GLTFState](class_gltfstate.md#class_GLTFState), path: [String](class_string.md#class_String) ) [🔗](class_gltfdocument.md#class_GLTFDocument_method_write_to_filesystem)

Takes a [GLTFState](class_gltfstate.md#class_GLTFState) object through the `state` parameter and writes a glTF file to the filesystem.

 **Note:** The extension of the glTF file determines if it is a .glb binary file or a .gltf text file.
