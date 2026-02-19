.. meta::
	:keywords: network

<span id="class_MultiplayerSynchronizer"></span>

## MultiplayerSynchronizer

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Synchronizes properties from the multiplayer authority to the remote peers.

### Description

By default, **MultiplayerSynchronizer** synchronizes configured properties to all peers.

Visibility can be handled directly with [set_visibility_for()](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_set_visibility_for) or as-needed with [add_visibility_filter()](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_add_visibility_filter) and [update_visibility()](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_update_visibility).

 [MultiplayerSpawner](class_multiplayerspawner.md#class_MultiplayerSpawner) s will handle nodes according to visibility of synchronizers as long as the node at [root_path](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_root_path) was spawned by one.

Internally, **MultiplayerSynchronizer** uses [MultiplayerAPI.object_configuration_add()](class_multiplayerapi.md#class_MultiplayerAPI_method_object_configuration_add) to notify synchronization start passing the [Node](class_node.md#class_Node) at [root_path](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_root_path) as the `object` and itself as the `configuration`, and uses [MultiplayerAPI.object_configuration_remove()](class_multiplayerapi.md#class_MultiplayerAPI_method_object_configuration_remove) to notify synchronization end in a similar way.

 **Note:** Synchronization is not supported for [Object](class_object.md#class_Object) type properties, like [Resource](class_resource.md#class_Resource). Properties that are unique to each peer, like the instance IDs of [Object](class_object.md#class_Object) s (see [Object.get_instance_id()](class_object.md#class_Object_method_get_instance_id)) or [RID](class_rid.md#class_RID) s, will also not work in synchronization.

### Properties


| [float](class_float.md#class_float) | [delta_interval](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_delta_interval) | `0.0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [public_visibility](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_public_visibility) | `true` |
| [SceneReplicationConfig](class_scenereplicationconfig.md#class_SceneReplicationConfig) | [replication_config](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_replication_config) |
| [float](class_float.md#class_float) | [replication_interval](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_replication_interval) | `0.0` |
| [NodePath](class_nodepath.md#class_NodePath) | [root_path](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_root_path) | `NodePath("..")` |
| [VisibilityUpdateMode](class_multiplayersynchronizer.md#enum_MultiplayerSynchronizer_VisibilityUpdateMode) | [visibility_update_mode](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_visibility_update_mode) | `0` |

### Methods


| void | [add_visibility_filter](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_add_visibility_filter) ( filter: [Callable](class_callable.md#class_Callable) ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [get_visibility_for](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_get_visibility_for) ( peer: [int](class_int.md#class_int) ) const |
| void | [remove_visibility_filter](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_remove_visibility_filter) ( filter: [Callable](class_callable.md#class_Callable) ) |
| void | [set_visibility_for](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_set_visibility_for) ( peer: [int](class_int.md#class_int), visible: [bool](class_bool.md#class_bool) ) |
| void | [update_visibility](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_update_visibility) ( for_peer: [int](class_int.md#class_int) = 0 ) |

---

### Signals

<span id="class_MultiplayerSynchronizer_signal_delta_synchronized"></span>

**delta_synchronized** ( ) [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_signal_delta_synchronized)

Emitted when a new delta synchronization state is received by this synchronizer after the properties have been updated.

---

<span id="class_MultiplayerSynchronizer_signal_synchronized"></span>

**synchronized** ( ) [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_signal_synchronized)

Emitted when a new synchronization state is received by this synchronizer after the properties have been updated.

---

<span id="class_MultiplayerSynchronizer_signal_visibility_changed"></span>

**visibility_changed** ( for_peer: [int](class_int.md#class_int) ) [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_signal_visibility_changed)

Emitted when visibility of `for_peer` is updated. See [update_visibility()](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_update_visibility).

---

### Enumerations

<span id="enum_MultiplayerSynchronizer_VisibilityUpdateMode"></span>

enum **VisibilityUpdateMode**: [🔗](class_multiplayersynchronizer.md#enum_MultiplayerSynchronizer_VisibilityUpdateMode)

<span id="class_MultiplayerSynchronizer_constant_VISIBILITY_PROCESS_IDLE"></span>

[VisibilityUpdateMode](class_multiplayersynchronizer.md#enum_MultiplayerSynchronizer_VisibilityUpdateMode) **VISIBILITY_PROCESS_IDLE** = `0`

Visibility filters are updated during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS](class_node.md#class_Node_constant_NOTIFICATION_INTERNAL_PROCESS)).

<span id="class_MultiplayerSynchronizer_constant_VISIBILITY_PROCESS_PHYSICS"></span>

[VisibilityUpdateMode](class_multiplayersynchronizer.md#enum_MultiplayerSynchronizer_VisibilityUpdateMode) **VISIBILITY_PROCESS_PHYSICS** = `1`

Visibility filters are updated during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS](class_node.md#class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS)).

<span id="class_MultiplayerSynchronizer_constant_VISIBILITY_PROCESS_NONE"></span>

[VisibilityUpdateMode](class_multiplayersynchronizer.md#enum_MultiplayerSynchronizer_VisibilityUpdateMode) **VISIBILITY_PROCESS_NONE** = `2`

Visibility filters are not updated automatically, and must be updated manually by calling [update_visibility()](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_update_visibility).

---

### Property Descriptions

<span id="class_MultiplayerSynchronizer_property_delta_interval"></span>

[float](class_float.md#class_float) **delta_interval** = `0.0` [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_delta_interval)

- void **set_delta_interval** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_delta_interval** ( )

Time interval between delta synchronizations. Used when the replication is set to [SceneReplicationConfig.REPLICATION_MODE_ON_CHANGE](class_scenereplicationconfig.md#class_SceneReplicationConfig_constant_REPLICATION_MODE_ON_CHANGE). If set to `0.0` (the default), delta synchronizations happen every network process frame.

---

<span id="class_MultiplayerSynchronizer_property_public_visibility"></span>

[bool](class_bool.md#class_bool) **public_visibility** = `true` [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_public_visibility)

- void **set_visibility_public** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_visibility_public** ( )

Whether synchronization should be visible to all peers by default. See [set_visibility_for()](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_set_visibility_for) and [add_visibility_filter()](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_add_visibility_filter) for ways of configuring fine-grained visibility options.

---

<span id="class_MultiplayerSynchronizer_property_replication_config"></span>

[SceneReplicationConfig](class_scenereplicationconfig.md#class_SceneReplicationConfig) **replication_config** [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_replication_config)

- void **set_replication_config** ( value: [SceneReplicationConfig](class_scenereplicationconfig.md#class_SceneReplicationConfig) )
- [SceneReplicationConfig](class_scenereplicationconfig.md#class_SceneReplicationConfig) **get_replication_config** ( )

Resource containing which properties to synchronize.

---

<span id="class_MultiplayerSynchronizer_property_replication_interval"></span>

[float](class_float.md#class_float) **replication_interval** = `0.0` [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_replication_interval)

- void **set_replication_interval** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_replication_interval** ( )

Time interval between synchronizations. Used when the replication is set to [SceneReplicationConfig.REPLICATION_MODE_ALWAYS](class_scenereplicationconfig.md#class_SceneReplicationConfig_constant_REPLICATION_MODE_ALWAYS). If set to `0.0` (the default), synchronizations happen every network process frame.

---

<span id="class_MultiplayerSynchronizer_property_root_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **root_path** = `NodePath("..")` [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_root_path)

- void **set_root_path** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_root_path** ( )

Node path that replicated properties are relative to.

If [root_path](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_root_path) was spawned by a [MultiplayerSpawner](class_multiplayerspawner.md#class_MultiplayerSpawner), the node will be also be spawned and despawned based on this synchronizer visibility options.

---

<span id="class_MultiplayerSynchronizer_property_visibility_update_mode"></span>

[VisibilityUpdateMode](class_multiplayersynchronizer.md#enum_MultiplayerSynchronizer_VisibilityUpdateMode) **visibility_update_mode** = `0` [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_visibility_update_mode)

- void **set_visibility_update_mode** ( value: [VisibilityUpdateMode](class_multiplayersynchronizer.md#enum_MultiplayerSynchronizer_VisibilityUpdateMode) )
- [VisibilityUpdateMode](class_multiplayersynchronizer.md#enum_MultiplayerSynchronizer_VisibilityUpdateMode) **get_visibility_update_mode** ( )

Specifies when visibility filters are updated.

---

### Method Descriptions

<span id="class_MultiplayerSynchronizer_method_add_visibility_filter"></span>

void **add_visibility_filter** ( filter: [Callable](class_callable.md#class_Callable) ) [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_add_visibility_filter)

Adds a peer visibility filter for this synchronizer.

 `filter` should take a peer ID [int](class_int.md#class_int) and return a [bool](class_bool.md#class_bool).

---

<span id="class_MultiplayerSynchronizer_method_get_visibility_for"></span>

[bool](class_bool.md#class_bool) **get_visibility_for** ( peer: [int](class_int.md#class_int) ) *const* [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_get_visibility_for)

Queries the current visibility for peer `peer`.

---

<span id="class_MultiplayerSynchronizer_method_remove_visibility_filter"></span>

void **remove_visibility_filter** ( filter: [Callable](class_callable.md#class_Callable) ) [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_remove_visibility_filter)

Removes a peer visibility filter from this synchronizer.

---

<span id="class_MultiplayerSynchronizer_method_set_visibility_for"></span>

void **set_visibility_for** ( peer: [int](class_int.md#class_int), visible: [bool](class_bool.md#class_bool) ) [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_set_visibility_for)

Sets the visibility of `peer` to `visible`. If `peer` is `0`, the value of [public_visibility](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_property_public_visibility) will be updated instead.

---

<span id="class_MultiplayerSynchronizer_method_update_visibility"></span>

void **update_visibility** ( for_peer: [int](class_int.md#class_int) = 0 ) [🔗](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer_method_update_visibility)

Updates the visibility of `for_peer` according to visibility filters. If `for_peer` is `0` (the default), all peers' visibilties are updated.
