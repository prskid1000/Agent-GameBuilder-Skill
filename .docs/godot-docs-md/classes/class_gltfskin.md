<span id="class_GLTFSkin"></span>

## GLTFSkin

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

.. container:: contribute

	There is currently no description for this class. Please help us by contributing one!

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

### Properties


| [Skin](class_skin.md#class_Skin) | [godot_skin](class_gltfskin.md#class_GLTFSkin_property_godot_skin) |
| --- | --- |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [joints](class_gltfskin.md#class_GLTFSkin_property_joints) | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [joints_original](class_gltfskin.md#class_GLTFSkin_property_joints_original) | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [non_joints](class_gltfskin.md#class_GLTFSkin_property_non_joints) | `PackedInt32Array()` |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [roots](class_gltfskin.md#class_GLTFSkin_property_roots) | `PackedInt32Array()` |
| [int](class_int.md#class_int) | [skeleton](class_gltfskin.md#class_GLTFSkin_property_skeleton) | `-1` |
| [int](class_int.md#class_int) | [skin_root](class_gltfskin.md#class_GLTFSkin_property_skin_root) | `-1` |

### Methods


| [Array](class_array.md#class_Array)\[[Transform3D](class_transform3d.md#class_Transform3D)\] | [get_inverse_binds](class_gltfskin.md#class_GLTFSkin_method_get_inverse_binds) ( ) |
| --- | --- |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_joint_i_to_bone_i](class_gltfskin.md#class_GLTFSkin_method_get_joint_i_to_bone_i) ( ) |
| [Dictionary](class_dictionary.md#class_Dictionary) | [get_joint_i_to_name](class_gltfskin.md#class_GLTFSkin_method_get_joint_i_to_name) ( ) |
| void | [set_inverse_binds](class_gltfskin.md#class_GLTFSkin_method_set_inverse_binds) ( inverse_binds: [Array](class_array.md#class_Array)\[[Transform3D](class_transform3d.md#class_Transform3D)\] ) |
| void | [set_joint_i_to_bone_i](class_gltfskin.md#class_GLTFSkin_method_set_joint_i_to_bone_i) ( joint_i_to_bone_i: [Dictionary](class_dictionary.md#class_Dictionary) ) |
| void | [set_joint_i_to_name](class_gltfskin.md#class_GLTFSkin_method_set_joint_i_to_name) ( joint_i_to_name: [Dictionary](class_dictionary.md#class_Dictionary) ) |

---

### Property Descriptions

<span id="class_GLTFSkin_property_godot_skin"></span>

[Skin](class_skin.md#class_Skin) **godot_skin** [🔗](class_gltfskin.md#class_GLTFSkin_property_godot_skin)

- void **set_godot_skin** ( value: [Skin](class_skin.md#class_Skin) )
- [Skin](class_skin.md#class_Skin) **get_godot_skin** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_GLTFSkin_property_joints"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **joints** = `PackedInt32Array()` [🔗](class_gltfskin.md#class_GLTFSkin_property_joints)

- void **set_joints** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_joints** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_GLTFSkin_property_joints_original"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **joints_original** = `PackedInt32Array()` [🔗](class_gltfskin.md#class_GLTFSkin_property_joints_original)

- void **set_joints_original** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_joints_original** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_GLTFSkin_property_non_joints"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **non_joints** = `PackedInt32Array()` [🔗](class_gltfskin.md#class_GLTFSkin_property_non_joints)

- void **set_non_joints** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_non_joints** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_GLTFSkin_property_roots"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **roots** = `PackedInt32Array()` [🔗](class_gltfskin.md#class_GLTFSkin_property_roots)

- void **set_roots** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_roots** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_GLTFSkin_property_skeleton"></span>

[int](class_int.md#class_int) **skeleton** = `-1` [🔗](class_gltfskin.md#class_GLTFSkin_property_skeleton)

- void **set_skeleton** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_skeleton** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

<span id="class_GLTFSkin_property_skin_root"></span>

[int](class_int.md#class_int) **skin_root** = `-1` [🔗](class_gltfskin.md#class_GLTFSkin_property_skin_root)

- void **set_skin_root** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_skin_root** ( )

.. container:: contribute

	There is currently no description for this property. Please help us by contributing one!

---

### Method Descriptions

<span id="class_GLTFSkin_method_get_inverse_binds"></span>

[Array](class_array.md#class_Array)\[[Transform3D](class_transform3d.md#class_Transform3D)\] **get_inverse_binds** ( ) [🔗](class_gltfskin.md#class_GLTFSkin_method_get_inverse_binds)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_GLTFSkin_method_get_joint_i_to_bone_i"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_joint_i_to_bone_i** ( ) [🔗](class_gltfskin.md#class_GLTFSkin_method_get_joint_i_to_bone_i)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_GLTFSkin_method_get_joint_i_to_name"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **get_joint_i_to_name** ( ) [🔗](class_gltfskin.md#class_GLTFSkin_method_get_joint_i_to_name)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_GLTFSkin_method_set_inverse_binds"></span>

void **set_inverse_binds** ( inverse_binds: [Array](class_array.md#class_Array)\[[Transform3D](class_transform3d.md#class_Transform3D)\] ) [🔗](class_gltfskin.md#class_GLTFSkin_method_set_inverse_binds)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_GLTFSkin_method_set_joint_i_to_bone_i"></span>

void **set_joint_i_to_bone_i** ( joint_i_to_bone_i: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_gltfskin.md#class_GLTFSkin_method_set_joint_i_to_bone_i)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!

---

<span id="class_GLTFSkin_method_set_joint_i_to_name"></span>

void **set_joint_i_to_name** ( joint_i_to_name: [Dictionary](class_dictionary.md#class_Dictionary) ) [🔗](class_gltfskin.md#class_GLTFSkin_method_set_joint_i_to_name)

.. container:: contribute

	There is currently no description for this method. Please help us by contributing one!
