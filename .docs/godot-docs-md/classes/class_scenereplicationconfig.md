<span id="class_SceneReplicationConfig"></span>

## SceneReplicationConfig

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Configuration for properties to synchronize with a [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer).

### Methods


| void | [add_property](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_add_property) ( path: [NodePath](class_nodepath.md#class_NodePath), index: [int](class_int.md#class_int) = -1 ) |
| --- | --- |
| [Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] | [get_properties](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_get_properties) ( ) const |
| [bool](class_bool.md#class_bool) | [has_property](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_has_property) ( path: [NodePath](class_nodepath.md#class_NodePath) ) const |
| [int](class_int.md#class_int) | [property_get_index](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_index) ( path: [NodePath](class_nodepath.md#class_NodePath) ) const |
| [ReplicationMode](class_scenereplicationconfig.md#enum_SceneReplicationConfig_ReplicationMode) | [property_get_replication_mode](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_replication_mode) ( path: [NodePath](class_nodepath.md#class_NodePath) ) |
| [bool](class_bool.md#class_bool) | [property_get_spawn](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_spawn) ( path: [NodePath](class_nodepath.md#class_NodePath) ) |
| [bool](class_bool.md#class_bool) | [property_get_sync](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_sync) ( path: [NodePath](class_nodepath.md#class_NodePath) ) |
| [bool](class_bool.md#class_bool) | [property_get_watch](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_watch) ( path: [NodePath](class_nodepath.md#class_NodePath) ) |
| void | [property_set_replication_mode](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_replication_mode) ( path: [NodePath](class_nodepath.md#class_NodePath), mode: [ReplicationMode](class_scenereplicationconfig.md#enum_SceneReplicationConfig_ReplicationMode) ) |
| void | [property_set_spawn](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_spawn) ( path: [NodePath](class_nodepath.md#class_NodePath), enabled: [bool](class_bool.md#class_bool) ) |
| void | [property_set_sync](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_sync) ( path: [NodePath](class_nodepath.md#class_NodePath), enabled: [bool](class_bool.md#class_bool) ) |
| void | [property_set_watch](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_watch) ( path: [NodePath](class_nodepath.md#class_NodePath), enabled: [bool](class_bool.md#class_bool) ) |
| void | [remove_property](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_remove_property) ( path: [NodePath](class_nodepath.md#class_NodePath) ) |

---

### Enumerations

<span id="enum_SceneReplicationConfig_ReplicationMode"></span>

enum **ReplicationMode**: [🔗](class_scenereplicationconfig.md#enum_SceneReplicationConfig_ReplicationMode)

<span id="class_SceneReplicationConfig_constant_REPLICATION_MODE_NEVER"></span>

[ReplicationMode](class_scenereplicationconfig.md#enum_SceneReplicationConfig_ReplicationMode) **REPLICATION_MODE_NEVER** = `0`

Do not keep the given property synchronized.

<span id="class_SceneReplicationConfig_constant_REPLICATION_MODE_ALWAYS"></span>

[ReplicationMode](class_scenereplicationconfig.md#enum_SceneReplicationConfig_ReplicationMode) **REPLICATION_MODE_ALWAYS** = `1`

Replicate the given property on process by constantly sending updates using unreliable transfer mode.

<span id="class_SceneReplicationConfig_constant_REPLICATION_MODE_ON_CHANGE"></span>

[ReplicationMode](class_scenereplicationconfig.md#enum_SceneReplicationConfig_ReplicationMode) **REPLICATION_MODE_ON_CHANGE** = `2`

Replicate the given property on process by sending updates using reliable transfer mode when its value changes.

---

### Method Descriptions

<span id="class_SceneReplicationConfig_method_add_property"></span>

void **add_property** ( path: [NodePath](class_nodepath.md#class_NodePath), index: [int](class_int.md#class_int) = -1 ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_add_property)

Adds the property identified by the given `path` to the list of the properties being synchronized, optionally passing an `index`.

 **Note:** For details on restrictions and limitations on property synchronization, see [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer).

---

<span id="class_SceneReplicationConfig_method_get_properties"></span>

[Array](class_array.md#class_Array)\[[NodePath](class_nodepath.md#class_NodePath)\] **get_properties** ( ) *const* [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_get_properties)

Returns a list of synchronized property [NodePath](class_nodepath.md#class_NodePath) s.

---

<span id="class_SceneReplicationConfig_method_has_property"></span>

[bool](class_bool.md#class_bool) **has_property** ( path: [NodePath](class_nodepath.md#class_NodePath) ) *const* [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_has_property)

Returns `true` if the given `path` is configured for synchronization.

---

<span id="class_SceneReplicationConfig_method_property_get_index"></span>

[int](class_int.md#class_int) **property_get_index** ( path: [NodePath](class_nodepath.md#class_NodePath) ) *const* [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_index)

Finds the index of the given `path`.

---

<span id="class_SceneReplicationConfig_method_property_get_replication_mode"></span>

[ReplicationMode](class_scenereplicationconfig.md#enum_SceneReplicationConfig_ReplicationMode) **property_get_replication_mode** ( path: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_replication_mode)

Returns the replication mode for the property identified by the given `path`.

---

<span id="class_SceneReplicationConfig_method_property_get_spawn"></span>

[bool](class_bool.md#class_bool) **property_get_spawn** ( path: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_spawn)

Returns `true` if the property identified by the given `path` is configured to be synchronized on spawn.

---

<span id="class_SceneReplicationConfig_method_property_get_sync"></span>

[bool](class_bool.md#class_bool) **property_get_sync** ( path: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_sync)

**Deprecated:** Use [property_get_replication_mode()](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_replication_mode) instead.

Returns `true` if the property identified by the given `path` is configured to be synchronized on process.

---

<span id="class_SceneReplicationConfig_method_property_get_watch"></span>

[bool](class_bool.md#class_bool) **property_get_watch** ( path: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_watch)

**Deprecated:** Use [property_get_replication_mode()](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_get_replication_mode) instead.

Returns `true` if the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.

---

<span id="class_SceneReplicationConfig_method_property_set_replication_mode"></span>

void **property_set_replication_mode** ( path: [NodePath](class_nodepath.md#class_NodePath), mode: [ReplicationMode](class_scenereplicationconfig.md#enum_SceneReplicationConfig_ReplicationMode) ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_replication_mode)

Sets the synchronization mode for the property identified by the given `path`.

---

<span id="class_SceneReplicationConfig_method_property_set_spawn"></span>

void **property_set_spawn** ( path: [NodePath](class_nodepath.md#class_NodePath), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_spawn)

Sets whether the property identified by the given `path` is configured to be synchronized on spawn.

---

<span id="class_SceneReplicationConfig_method_property_set_sync"></span>

void **property_set_sync** ( path: [NodePath](class_nodepath.md#class_NodePath), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_sync)

**Deprecated:** Use [property_set_replication_mode()](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_replication_mode) with [REPLICATION_MODE_ALWAYS](class_scenereplicationconfig.md#class_SceneReplicationConfig_constant_REPLICATION_MODE_ALWAYS) instead.

Sets whether the property identified by the given `path` is configured to be synchronized on process.

---

<span id="class_SceneReplicationConfig_method_property_set_watch"></span>

void **property_set_watch** ( path: [NodePath](class_nodepath.md#class_NodePath), enabled: [bool](class_bool.md#class_bool) ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_watch)

**Deprecated:** Use [property_set_replication_mode()](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_property_set_replication_mode) with [REPLICATION_MODE_ON_CHANGE](class_scenereplicationconfig.md#class_SceneReplicationConfig_constant_REPLICATION_MODE_ON_CHANGE) instead.

Sets whether the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.

---

<span id="class_SceneReplicationConfig_method_remove_property"></span>

void **remove_property** ( path: [NodePath](class_nodepath.md#class_NodePath) ) [🔗](class_scenereplicationconfig.md#class_SceneReplicationConfig_method_remove_property)

Removes the property identified by the given `path` from the configuration.
