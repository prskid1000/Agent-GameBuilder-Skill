<span id="class_SceneState"></span>

## SceneState

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Provides access to a scene file's information.

### Description

Maintains a list of resources, nodes, exported and overridden properties, and built-in scripts associated with a scene. They cannot be modified from a **SceneState**, only accessed. Useful for peeking into what a [PackedScene](class_packedscene.md#class_PackedScene) contains without instantiating it.

This class cannot be instantiated directly, it is retrieved for a given scene as the result of [PackedScene.get_state()](class_packedscene.md#class_PackedScene_method_get_state).

### Methods


| [SceneState](class_scenestate.md#class_SceneState) | [get_base_scene_state](class_scenestate.md#class_SceneState_method_get_base_scene_state) ( ) const |
| --- | --- |
| [Array](class_array.md#class_Array) | [get_connection_binds](class_scenestate.md#class_SceneState_method_get_connection_binds) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_connection_count](class_scenestate.md#class_SceneState_method_get_connection_count) ( ) const |
| [int](class_int.md#class_int) | [get_connection_flags](class_scenestate.md#class_SceneState_method_get_connection_flags) ( idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_connection_method](class_scenestate.md#class_SceneState_method_get_connection_method) ( idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_connection_signal](class_scenestate.md#class_SceneState_method_get_connection_signal) ( idx: [int](class_int.md#class_int) ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_connection_source](class_scenestate.md#class_SceneState_method_get_connection_source) ( idx: [int](class_int.md#class_int) ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_connection_target](class_scenestate.md#class_SceneState_method_get_connection_target) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_connection_unbinds](class_scenestate.md#class_SceneState_method_get_connection_unbinds) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_node_count](class_scenestate.md#class_SceneState_method_get_node_count) ( ) const |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [get_node_groups](class_scenestate.md#class_SceneState_method_get_node_groups) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_node_index](class_scenestate.md#class_SceneState_method_get_node_index) ( idx: [int](class_int.md#class_int) ) const |
| [PackedScene](class_packedscene.md#class_PackedScene) | [get_node_instance](class_scenestate.md#class_SceneState_method_get_node_instance) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_node_instance_placeholder](class_scenestate.md#class_SceneState_method_get_node_instance_placeholder) ( idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_node_name](class_scenestate.md#class_SceneState_method_get_node_name) ( idx: [int](class_int.md#class_int) ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_node_owner_path](class_scenestate.md#class_SceneState_method_get_node_owner_path) ( idx: [int](class_int.md#class_int) ) const |
| [NodePath](class_nodepath.md#class_NodePath) | [get_node_path](class_scenestate.md#class_SceneState_method_get_node_path) ( idx: [int](class_int.md#class_int), for_parent: [bool](class_bool.md#class_bool) = false ) const |
| [int](class_int.md#class_int) | [get_node_property_count](class_scenestate.md#class_SceneState_method_get_node_property_count) ( idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_node_property_name](class_scenestate.md#class_SceneState_method_get_node_property_name) ( idx: [int](class_int.md#class_int), prop_idx: [int](class_int.md#class_int) ) const |
| [Variant](class_variant.md#class_Variant) | [get_node_property_value](class_scenestate.md#class_SceneState_method_get_node_property_value) ( idx: [int](class_int.md#class_int), prop_idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_node_type](class_scenestate.md#class_SceneState_method_get_node_type) ( idx: [int](class_int.md#class_int) ) const |
| [String](class_string.md#class_String) | [get_path](class_scenestate.md#class_SceneState_method_get_path) ( ) const |
| [bool](class_bool.md#class_bool) | [is_node_instance_placeholder](class_scenestate.md#class_SceneState_method_is_node_instance_placeholder) ( idx: [int](class_int.md#class_int) ) const |

---

### Enumerations

<span id="enum_SceneState_GenEditState"></span>

enum **GenEditState**: [🔗](class_scenestate.md#enum_SceneState_GenEditState)

<span id="class_SceneState_constant_GEN_EDIT_STATE_DISABLED"></span>

[GenEditState](class_scenestate.md#enum_SceneState_GenEditState) **GEN_EDIT_STATE_DISABLED** = `0`

If passed to [PackedScene.instantiate()](class_packedscene.md#class_PackedScene_method_instantiate), blocks edits to the scene state.

<span id="class_SceneState_constant_GEN_EDIT_STATE_INSTANCE"></span>

[GenEditState](class_scenestate.md#enum_SceneState_GenEditState) **GEN_EDIT_STATE_INSTANCE** = `1`

If passed to [PackedScene.instantiate()](class_packedscene.md#class_PackedScene_method_instantiate), provides inherited scene resources to the local scene.

 **Note:** Only available in editor builds.

<span id="class_SceneState_constant_GEN_EDIT_STATE_MAIN"></span>

[GenEditState](class_scenestate.md#enum_SceneState_GenEditState) **GEN_EDIT_STATE_MAIN** = `2`

If passed to [PackedScene.instantiate()](class_packedscene.md#class_PackedScene_method_instantiate), provides local scene resources to the local scene. Only the main scene should receive the main edit state.

 **Note:** Only available in editor builds.

<span id="class_SceneState_constant_GEN_EDIT_STATE_MAIN_INHERITED"></span>

[GenEditState](class_scenestate.md#enum_SceneState_GenEditState) **GEN_EDIT_STATE_MAIN_INHERITED** = `3`

If passed to [PackedScene.instantiate()](class_packedscene.md#class_PackedScene_method_instantiate), it's similar to [GEN_EDIT_STATE_MAIN](class_scenestate.md#class_SceneState_constant_GEN_EDIT_STATE_MAIN), but for the case where the scene is being instantiated to be the base of another one.

 **Note:** Only available in editor builds.

---

### Method Descriptions

<span id="class_SceneState_method_get_base_scene_state"></span>

[SceneState](class_scenestate.md#class_SceneState) **get_base_scene_state** ( ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_base_scene_state)

Returns the **SceneState** of the scene that this scene inherits from, or `null` if it doesn't inherit from any scene.

---

<span id="class_SceneState_method_get_connection_binds"></span>

[Array](class_array.md#class_Array) **get_connection_binds** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_connection_binds)

Returns the list of bound parameters for the signal at `idx`.

---

<span id="class_SceneState_method_get_connection_count"></span>

[int](class_int.md#class_int) **get_connection_count** ( ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_connection_count)

Returns the number of signal connections in the scene.

The `idx` argument used to query connection metadata in other `get_connection_*` methods in the interval `[0, get_connection_count() - 1]`.

---

<span id="class_SceneState_method_get_connection_flags"></span>

[int](class_int.md#class_int) **get_connection_flags** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_connection_flags)

Returns the connection flags for the signal at `idx`. See [ConnectFlags](class_object.md#enum_Object_ConnectFlags) constants.

---

<span id="class_SceneState_method_get_connection_method"></span>

[StringName](class_stringname.md#class_StringName) **get_connection_method** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_connection_method)

Returns the method connected to the signal at `idx`.

---

<span id="class_SceneState_method_get_connection_signal"></span>

[StringName](class_stringname.md#class_StringName) **get_connection_signal** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_connection_signal)

Returns the name of the signal at `idx`.

---

<span id="class_SceneState_method_get_connection_source"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_connection_source** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_connection_source)

Returns the path to the node that owns the signal at `idx`, relative to the root node.

---

<span id="class_SceneState_method_get_connection_target"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_connection_target** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_connection_target)

Returns the path to the node that owns the method connected to the signal at `idx`, relative to the root node.

---

<span id="class_SceneState_method_get_connection_unbinds"></span>

[int](class_int.md#class_int) **get_connection_unbinds** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_connection_unbinds)

Returns the number of unbound parameters for the signal at `idx`.

---

<span id="class_SceneState_method_get_node_count"></span>

[int](class_int.md#class_int) **get_node_count** ( ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_count)

Returns the number of nodes in the scene.

The `idx` argument used to query node data in other `get_node_*` methods in the interval `[0, get_node_count() - 1]`.

---

<span id="class_SceneState_method_get_node_groups"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_node_groups** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_groups)

Returns the list of group names associated with the node at `idx`.

---

<span id="class_SceneState_method_get_node_index"></span>

[int](class_int.md#class_int) **get_node_index** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_index)

Returns the node's index, which is its position relative to its siblings. This is only relevant and saved in scenes for cases where new nodes are added to an instantiated or inherited scene among siblings from the base scene. Despite the name, this index is not related to the `idx` argument used here and in other methods.

---

<span id="class_SceneState_method_get_node_instance"></span>

[PackedScene](class_packedscene.md#class_PackedScene) **get_node_instance** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_instance)

Returns a [PackedScene](class_packedscene.md#class_PackedScene) for the node at `idx` (i.e. the whole branch starting at this node, with its child nodes and resources), or `null` if the node is not an instance.

---

<span id="class_SceneState_method_get_node_instance_placeholder"></span>

[String](class_string.md#class_String) **get_node_instance_placeholder** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_instance_placeholder)

Returns the path to the represented scene file if the node at `idx` is an [InstancePlaceholder](class_instanceplaceholder.md#class_InstancePlaceholder).

---

<span id="class_SceneState_method_get_node_name"></span>

[StringName](class_stringname.md#class_StringName) **get_node_name** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_name)

Returns the name of the node at `idx`.

---

<span id="class_SceneState_method_get_node_owner_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_node_owner_path** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_owner_path)

Returns the path to the owner of the node at `idx`, relative to the root node.

---

<span id="class_SceneState_method_get_node_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **get_node_path** ( idx: [int](class_int.md#class_int), for_parent: [bool](class_bool.md#class_bool) = false ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_path)

Returns the path to the node at `idx`.

If `for_parent` is `true`, returns the path of the `idx` node's parent instead.

---

<span id="class_SceneState_method_get_node_property_count"></span>

[int](class_int.md#class_int) **get_node_property_count** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_property_count)

Returns the number of exported or overridden properties for the node at `idx`.

The `prop_idx` argument used to query node property data in other `get_node_property_*` methods in the interval `[0, get_node_property_count() - 1]`.

---

<span id="class_SceneState_method_get_node_property_name"></span>

[StringName](class_stringname.md#class_StringName) **get_node_property_name** ( idx: [int](class_int.md#class_int), prop_idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_property_name)

Returns the name of the property at `prop_idx` for the node at `idx`.

---

<span id="class_SceneState_method_get_node_property_value"></span>

[Variant](class_variant.md#class_Variant) **get_node_property_value** ( idx: [int](class_int.md#class_int), prop_idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_property_value)

Returns the value of the property at `prop_idx` for the node at `idx`.

---

<span id="class_SceneState_method_get_node_type"></span>

[StringName](class_stringname.md#class_StringName) **get_node_type** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_node_type)

Returns the type of the node at `idx`.

---

<span id="class_SceneState_method_get_path"></span>

[String](class_string.md#class_String) **get_path** ( ) *const* [🔗](class_scenestate.md#class_SceneState_method_get_path)

Returns the resource path to the represented [PackedScene](class_packedscene.md#class_PackedScene).

---

<span id="class_SceneState_method_is_node_instance_placeholder"></span>

[bool](class_bool.md#class_bool) **is_node_instance_placeholder** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_scenestate.md#class_SceneState_method_is_node_instance_placeholder)

Returns `true` if the node at `idx` is an [InstancePlaceholder](class_instanceplaceholder.md#class_InstancePlaceholder).
