<span id="class_GLTFSkeleton"></span>

## GLTFSkeleton

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

.. container:: contribute

	There is currently no description for this class. Please help us by contributing one!

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [joints](class_gltfskeleton.md#class_GLTFSkeleton_property_joints) | `PackedInt32Array()` |
| --- | --- | --- |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [roots](class_gltfskeleton.md#class_GLTFSkeleton_property_roots) | `PackedInt32Array()` |

### Methods


| [BoneAttachment3D](class_boneattachment3d.md#class_BoneAttachment3D) | [get_bone_attachment](class_gltfskeleton.md#class_GLTFSkeleton_method_get_bone_attachment) ( idx: [int](class_int.md#class_int) ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_bone_attachment_count](class_gltfskeleton.md#class_GLTFSkeleton_method_get_bone_attachment_count) ( ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_godot_bone_node](class_gltfskeleton.md#class_GLTFSkeleton_method_get_godot_bone_node) ( ) |
| [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) | [get_godot_skeleton](class_gltfskeleton.md#class_GLTFSkeleton_method_get_godot_skeleton) ( ) |
| [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] | [get_unique_names](class_gltfskeleton.md#class_GLTFSkeleton_method_get_unique_names) ( ) |
| void | [set_godot_bone_node](class_gltfskeleton.md#class_GLTFSkeleton_method_set_godot_bone_node) ( godot_bone_node: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| void | [set_unique_names](class_gltfskeleton.md#class_GLTFSkeleton_method_set_unique_names) ( unique_names: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] ) |

---

### Property Descriptions

<span id="class_GLTFSkeleton_property_joints"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **joints** = `PackedInt32Array()` [🔗](class_gltfskeleton.md#class_GLTFSkeleton_property_joints)

- void **set_joints** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_joints** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_GLTFSkeleton_property_roots"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **roots** = `PackedInt32Array()` [🔗](class_gltfskeleton.md#class_GLTFSkeleton_property_roots)

- void **set_roots** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_roots** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

### Method Descriptions

<span id="class_GLTFSkeleton_method_get_bone_attachment"></span>

[BoneAttachment3D](class_boneattachment3d.md#class_BoneAttachment3D) **get_bone_attachment** ( idx: [int](class_int.md#class_int) ) [🔗](class_gltfskeleton.md#class_GLTFSkeleton_method_get_bone_attachment)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_GLTFSkeleton_method_get_bone_attachment_count"></span>

[int](class_int.md#class_int) **get_bone_attachment_count** ( ) [🔗](class_gltfskeleton.md#class_GLTFSkeleton_method_get_bone_attachment_count)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_GLTFSkeleton_method_get_godot_bone_node"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_godot_bone_node** ( ) [🔗](class_gltfskeleton.md#class_GLTFSkeleton_method_get_godot_bone_node)

Returns a [Dictionary](class_dictionary.md#class_Dictionary) that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.

---

<span id="class_GLTFSkeleton_method_get_godot_skeleton"></span>

[Skeleton3D](class_skeleton3d.md#class_Skeleton3D) **get_godot_skeleton** ( ) [🔗](class_gltfskeleton.md#class_GLTFSkeleton_method_get_godot_skeleton)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_GLTFSkeleton_method_get_unique_names"></span>

[Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] **get_unique_names** ( ) [🔗](class_gltfskeleton.md#class_GLTFSkeleton_method_get_unique_names)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_GLTFSkeleton_method_set_godot_bone_node"></span>

void **set_godot_bone_node** ( godot_bone_node: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_gltfskeleton.md#class_GLTFSkeleton_method_set_godot_bone_node)

Sets a [Dictionary](class_dictionary.md#class_Dictionary) that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.

---

<span id="class_GLTFSkeleton_method_set_unique_names"></span>

void **set_unique_names** ( unique_names: [Array](class_array.md#class_Array)\[[String](class_string.md#class_String)\] ) [🔗](class_gltfskeleton.md#class_GLTFSkeleton_method_set_unique_names)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
