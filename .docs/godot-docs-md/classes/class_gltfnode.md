<span id="class_GLTFNode"></span>

## GLTFNode

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

glTF node class.

### Description

Represents a glTF node. glTF nodes may have names, transforms, children (other glTF nodes), and more specialized properties (represented by their own classes).

glTF nodes generally exist inside of [GLTFState](class_gltfstate.md#class_GLTFState) which represents all data of a glTF file. Most of GLTFNode's properties are indices of other data in the glTF file. You can extend a glTF node with additional properties by using [get_additional_data()](class_gltfnode.md#class_GLTFNode_method_get_additional_data) and [set_additional_data()](class_gltfnode.md#class_GLTFNode_method_set_additional_data).

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

- glTF scene and node spec

### Properties


| [int](class_int.md#class_int) | [camera](class_gltfnode.md#class_GLTFNode_property_camera) | `-1` |
| --- | --- | --- |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [children](class_gltfnode.md#class_GLTFNode_property_children) | `PackedInt32Array()` |
| [int](class_int.md#class_int) | [height](class_gltfnode.md#class_GLTFNode_property_height) | `-1` |
| [int](class_int.md#class_int) | [light](class_gltfnode.md#class_GLTFNode_property_light) | `-1` |
| [int](class_int.md#class_int) | [mesh](class_gltfnode.md#class_GLTFNode_property_mesh) | `-1` |
| [String](class_string.md#class_String) | [original_name](class_gltfnode.md#class_GLTFNode_property_original_name) | `""` |
| [int](class_int.md#class_int) | [parent](class_gltfnode.md#class_GLTFNode_property_parent) | `-1` |
| [Vector3](class_vector3.md#class_Vector3) | [position](class_gltfnode.md#class_GLTFNode_property_position) | `Vector3(0, 0, 0)` |
| [Quaternion](class_quaternion.md#class_Quaternion) | [rotation](class_gltfnode.md#class_GLTFNode_property_rotation) | `Quaternion(0, 0, 0, 1)` |
| [Vector3](class_vector3.md#class_Vector3) | [scale](class_gltfnode.md#class_GLTFNode_property_scale) | `Vector3(1, 1, 1)` |
| [int](class_int.md#class_int) | [skeleton](class_gltfnode.md#class_GLTFNode_property_skeleton) | `-1` |
| [int](class_int.md#class_int) | [skin](class_gltfnode.md#class_GLTFNode_property_skin) | `-1` |
| [bool](class_bool.md#class_bool) | [visible](class_gltfnode.md#class_GLTFNode_property_visible) | `true` |
| [Transform3D](class_transform3d.md#class_Transform3D) | [xform](class_gltfnode.md#class_GLTFNode_property_xform) | `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` |

### Methods


| void | [append_child_index](class_gltfnode.md#class_GLTFNode_method_append_child_index) ( child_index: [int](class_int.md#class_int) ) |
| --- | --- |
| [Variant](class_variant.md#class_Variant) | [get_additional_data](class_gltfnode.md#class_GLTFNode_method_get_additional_data) ( extension_name: [StringName](class_stringname.md#class_StringName) ) |
| [NodePath](class_nodepath.md#class_NodePath) | [get_scene_node_path](class_gltfnode.md#class_GLTFNode_method_get_scene_node_path) ( gltf_state: [GLTFState](class_gltfstate.md#class_GLTFState), handle_skeletons: [bool](class_bool.md#class_bool) = true ) |
| void | [set_additional_data](class_gltfnode.md#class_GLTFNode_method_set_additional_data) ( extension_name: [StringName](class_stringname.md#class_StringName), additional_data: [Variant](class_variant.md#class_Variant) ) |

---

### Property Descriptions

<span id="class_GLTFNode_property_camera"></span>

[int](class_int.md#class_int) **camera** = `-1` [🔗](class_gltfnode.md#class_GLTFNode_property_camera)

- void **set_camera** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_camera** ( )

If this glTF node is a camera, the index of the [GLTFCamera](class_gltfcamera.md#class_GLTFCamera) in the [GLTFState](class_gltfstate.md#class_GLTFState) that describes the camera's properties. If `-1`, this node is not a camera.

---

<span id="class_GLTFNode_property_children"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **children** = `PackedInt32Array()` [🔗](class_gltfnode.md#class_GLTFNode_property_children)

- void **set_children** ( value: [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) )
- [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_children** ( )

The indices of the child nodes in the [GLTFState](class_gltfstate.md#class_GLTFState). If this glTF node has no children, this will be an empty array.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) for more details.

---

<span id="class_GLTFNode_property_height"></span>

[int](class_int.md#class_int) **height** = `-1` [🔗](class_gltfnode.md#class_GLTFNode_property_height)

- void **set_height** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_height** ( )

How deep into the node hierarchy this node is. A root node will have a height of 0, its children will have a height of 1, and so on. If -1, the height has not been calculated.

---

<span id="class_GLTFNode_property_light"></span>

[int](class_int.md#class_int) **light** = `-1` [🔗](class_gltfnode.md#class_GLTFNode_property_light)

- void **set_light** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_light** ( )

If this glTF node is a light, the index of the [GLTFLight](class_gltflight.md#class_GLTFLight) in the [GLTFState](class_gltfstate.md#class_GLTFState) that describes the light's properties. If -1, this node is not a light.

---

<span id="class_GLTFNode_property_mesh"></span>

[int](class_int.md#class_int) **mesh** = `-1` [🔗](class_gltfnode.md#class_GLTFNode_property_mesh)

- void **set_mesh** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_mesh** ( )

If this glTF node is a mesh, the index of the [GLTFMesh](class_gltfmesh.md#class_GLTFMesh) in the [GLTFState](class_gltfstate.md#class_GLTFState) that describes the mesh's properties. If -1, this node is not a mesh.

---

<span id="class_GLTFNode_property_original_name"></span>

[String](class_string.md#class_String) **original_name** = `""` [🔗](class_gltfnode.md#class_GLTFNode_property_original_name)

- void **set_original_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_original_name** ( )

The original name of the node.

---

<span id="class_GLTFNode_property_parent"></span>

[int](class_int.md#class_int) **parent** = `-1` [🔗](class_gltfnode.md#class_GLTFNode_property_parent)

- void **set_parent** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_parent** ( )

The index of the parent node in the [GLTFState](class_gltfstate.md#class_GLTFState). If -1, this node is a root node.

---

<span id="class_GLTFNode_property_position"></span>

[Vector3](class_vector3.md#class_Vector3) **position** = `Vector3(0, 0, 0)` [🔗](class_gltfnode.md#class_GLTFNode_property_position)

- void **set_position** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_position** ( )

The position of the glTF node relative to its parent.

---

<span id="class_GLTFNode_property_rotation"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **rotation** = `Quaternion(0, 0, 0, 1)` [🔗](class_gltfnode.md#class_GLTFNode_property_rotation)

- void **set_rotation** ( value: [Quaternion](class_quaternion.md#class_Quaternion) )
- [Quaternion](class_quaternion.md#class_Quaternion) **get_rotation** ( )

The rotation of the glTF node relative to its parent.

---

<span id="class_GLTFNode_property_scale"></span>

[Vector3](class_vector3.md#class_Vector3) **scale** = `Vector3(1, 1, 1)` [🔗](class_gltfnode.md#class_GLTFNode_property_scale)

- void **set_scale** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_scale** ( )

The scale of the glTF node relative to its parent.

---

<span id="class_GLTFNode_property_skeleton"></span>

[int](class_int.md#class_int) **skeleton** = `-1` [🔗](class_gltfnode.md#class_GLTFNode_property_skeleton)

- void **set_skeleton** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_skeleton** ( )

If this glTF node has a skeleton, the index of the [GLTFSkeleton](class_gltfskeleton.md#class_GLTFSkeleton) in the [GLTFState](class_gltfstate.md#class_GLTFState) that describes the skeleton's properties. If -1, this node does not have a skeleton.

---

<span id="class_GLTFNode_property_skin"></span>

[int](class_int.md#class_int) **skin** = `-1` [🔗](class_gltfnode.md#class_GLTFNode_property_skin)

- void **set_skin** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_skin** ( )

If this glTF node has a skin, the index of the [GLTFSkin](class_gltfskin.md#class_GLTFSkin) in the [GLTFState](class_gltfstate.md#class_GLTFState) that describes the skin's properties. If -1, this node does not have a skin.

---

<span id="class_GLTFNode_property_visible"></span>

[bool](class_bool.md#class_bool) **visible** = `true` [🔗](class_gltfnode.md#class_GLTFNode_property_visible)

- void **set_visible** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_visible** ( )

If `true`, the GLTF node is visible. If `false`, the GLTF node is not visible. This is converted to the [Node3D.visible](class_node3d.md#class_Node3D_property_visible) property in the Godot scene, and is exported to `KHR_node_visibility` when `false`.

---

<span id="class_GLTFNode_property_xform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **xform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗](class_gltfnode.md#class_GLTFNode_property_xform)

- void **set_xform** ( value: [Transform3D](class_transform3d.md#class_Transform3D) )
- [Transform3D](class_transform3d.md#class_Transform3D) **get_xform** ( )

The transform of the glTF node relative to its parent. This property is usually unused since the position, rotation, and scale properties are preferred.

---

### Method Descriptions

<span id="class_GLTFNode_method_append_child_index"></span>

void **append_child_index** ( child_index: [int](class_int.md#class_int) ) [🔗](class_gltfnode.md#class_GLTFNode_method_append_child_index)

Appends the given child node index to the [children](class_gltfnode.md#class_GLTFNode_property_children) array.

---

<span id="class_GLTFNode_method_get_additional_data"></span>

[Variant](class_variant.md#class_Variant) **get_additional_data** ( extension_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_gltfnode.md#class_GLTFNode_method_get_additional_data)

Gets additional arbitrary data in this **GLTFNode** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.

---

<span id="class_GLTFNode_method_get_scene_node_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_scene_node_path** ( gltf_state: [GLTFState](class_gltfstate.md#class_GLTFState), handle_skeletons: [bool](class_bool.md#class_bool) = true ) [🔗](class_gltfnode.md#class_GLTFNode_method_get_scene_node_path)

Returns the [NodePath](class_nodepath.md#class_NodePath) that this GLTF node will have in the Godot scene tree after being imported. This is useful when importing glTF object model pointers with [GLTFObjectModelProperty](class_gltfobjectmodelproperty.md#class_GLTFObjectModelProperty), for handling extensions such as `KHR_animation_pointer` or `KHR_interactivity`.

If `handle_skeletons` is `true`, paths to skeleton bone glTF nodes will be resolved properly. For example, a path that would be `^"A/B/C/Bone1/Bone2/Bone3"` if `false` will become `^"A/B/C/Skeleton3D:Bone3"`.

---

<span id="class_GLTFNode_method_set_additional_data"></span>

void **set_additional_data** ( extension_name: [StringName](class_stringname.md#class_StringName), additional_data: [Variant](class_variant.md#class_Variant) ) [🔗](class_gltfnode.md#class_GLTFNode_method_set_additional_data)

Sets additional arbitrary data in this **GLTFNode** instance. This can be used to keep per-node state data in [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension](class_gltfdocumentextension.md#class_GLTFDocumentExtension) name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.
