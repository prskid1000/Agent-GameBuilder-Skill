.. meta::
	:keywords: network

<span id="class_MultiplayerAPI"></span>

## MultiplayerAPI

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [MultiplayerAPIExtension](class_multiplayerapiextension.md#class_MultiplayerAPIExtension), [SceneMultiplayer](class_scenemultiplayer.md#class_SceneMultiplayer)

High-level multiplayer API interface.

### Description

Base class for high-level multiplayer API implementations. See also [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer).

By default, [SceneTree](class_scenetree.md#class_SceneTree) has a reference to an implementation of this class and uses it to provide multiplayer capabilities (i.e. RPCs) across the whole scene.

It is possible to override the MultiplayerAPI instance used by specific tree branches by calling the [SceneTree.set_multiplayer()](class_scenetree.md#class_SceneTree_method_set_multiplayer) method, effectively allowing to run both client and server in the same scene.

It is also possible to extend or replace the default implementation via scripting or native extensions. See [MultiplayerAPIExtension](class_multiplayerapiextension.md#class_MultiplayerAPIExtension) for details about extensions, [SceneMultiplayer](class_scenemultiplayer.md#class_SceneMultiplayer) for the details about the default implementation.

### Properties


| [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) | [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer) |
| --- | --- |

### Methods


| [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) | [create_default_interface](class_multiplayerapi.md#class_MultiplayerAPI_method_create_default_interface) ( ) static |
| --- | --- |
| [StringName](class_stringname.md#class_StringName) | [get_default_interface](class_multiplayerapi.md#class_MultiplayerAPI_method_get_default_interface) ( ) static |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_peers](class_multiplayerapi.md#class_MultiplayerAPI_method_get_peers) ( ) |
| [int](class_int.md#class_int) | [get_remote_sender_id](class_multiplayerapi.md#class_MultiplayerAPI_method_get_remote_sender_id) ( ) |
| [int](class_int.md#class_int) | [get_unique_id](class_multiplayerapi.md#class_MultiplayerAPI_method_get_unique_id) ( ) |
| [bool](class_bool.md#class_bool) | [has_multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_method_has_multiplayer_peer) ( ) |
| [bool](class_bool.md#class_bool) | [is_server](class_multiplayerapi.md#class_MultiplayerAPI_method_is_server) ( ) |
| Error | [object_configuration_add](class_multiplayerapi.md#class_MultiplayerAPI_method_object_configuration_add) ( object: [Object](class_object.md#class_Object), configuration: [Variant](class_variant.md#class_Variant) ) |
| Error | [object_configuration_remove](class_multiplayerapi.md#class_MultiplayerAPI_method_object_configuration_remove) ( object: [Object](class_object.md#class_Object), configuration: [Variant](class_variant.md#class_Variant) ) |
| Error | [poll](class_multiplayerapi.md#class_MultiplayerAPI_method_poll) ( ) |
| Error | [rpc](class_multiplayerapi.md#class_MultiplayerAPI_method_rpc) ( peer: [int](class_int.md#class_int), object: [Object](class_object.md#class_Object), method: [StringName](class_stringname.md#class_StringName), arguments: [Array](class_array.md#class_Array) = [] ) |
| void | [set_default_interface](class_multiplayerapi.md#class_MultiplayerAPI_method_set_default_interface) ( interface_name: [StringName](class_stringname.md#class_StringName) ) static |

---

### Signals

<span id="class_MultiplayerAPI_signal_connected_to_server"></span>

**connected_to_server** ( ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_signal_connected_to_server)

Emitted when this MultiplayerAPI's [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer) successfully connected to a server. Only emitted on clients.

---

<span id="class_MultiplayerAPI_signal_connection_failed"></span>

**connection_failed** ( ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_signal_connection_failed)

Emitted when this MultiplayerAPI's [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer) fails to establish a connection to a server. Only emitted on clients.

---

<span id="class_MultiplayerAPI_signal_peer_connected"></span>

**peer_connected** ( id: [int](class_int.md#class_int) ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_signal_peer_connected)

Emitted when this MultiplayerAPI's [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer) connects with a new peer. ID is the peer ID of the new peer. Clients get notified when other clients connect to the same server. Upon connecting to a server, a client also receives this signal for the server (with ID being 1).

---

<span id="class_MultiplayerAPI_signal_peer_disconnected"></span>

**peer_disconnected** ( id: [int](class_int.md#class_int) ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_signal_peer_disconnected)

Emitted when this MultiplayerAPI's [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer) disconnects from a peer. Clients get notified when other clients disconnect from the same server.

---

<span id="class_MultiplayerAPI_signal_server_disconnected"></span>

**server_disconnected** ( ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_signal_server_disconnected)

Emitted when this MultiplayerAPI's [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer) disconnects from server. Only emitted on clients.

---

### Enumerations

<span id="enum_MultiplayerAPI_RPCMode"></span>

enum **RPCMode**: [🔗](class_multiplayerapi.md#enum_MultiplayerAPI_RPCMode)

<span id="class_MultiplayerAPI_constant_RPC_MODE_DISABLED"></span>

[RPCMode](class_multiplayerapi.md#enum_MultiplayerAPI_RPCMode) **RPC_MODE_DISABLED** = `0`

Used with [Node.rpc_config()](class_node.md#class_Node_method_rpc_config) to disable a method or property for all RPC calls, making it unavailable. Default for all methods.

<span id="class_MultiplayerAPI_constant_RPC_MODE_ANY_PEER"></span>

[RPCMode](class_multiplayerapi.md#enum_MultiplayerAPI_RPCMode) **RPC_MODE_ANY_PEER** = `1`

Used with [Node.rpc_config()](class_node.md#class_Node_method_rpc_config) to set a method to be callable remotely by any peer. Analogous to the `@rpc("any_peer")` annotation. Calls are accepted from all remote peers, no matter if they are node's authority or not.

<span id="class_MultiplayerAPI_constant_RPC_MODE_AUTHORITY"></span>

[RPCMode](class_multiplayerapi.md#enum_MultiplayerAPI_RPCMode) **RPC_MODE_AUTHORITY** = `2`

Used with [Node.rpc_config()](class_node.md#class_Node_method_rpc_config) to set a method to be callable remotely only by the current multiplayer authority (which is the server by default). Analogous to the `@rpc("authority")` annotation. See [Node.set_multiplayer_authority()](class_node.md#class_Node_method_set_multiplayer_authority).

---

### Property Descriptions

<span id="class_MultiplayerAPI_property_multiplayer_peer"></span>

[MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) **multiplayer_peer** [🔗](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer)

- void **set_multiplayer_peer** ( value: [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) )
- [MultiplayerPeer](class_multiplayerpeer.md#class_MultiplayerPeer) **get_multiplayer_peer** ( )

The peer object to handle the RPC system (effectively enabling networking when set). Depending on the peer itself, the MultiplayerAPI will become a network server (check with [is_server()](class_multiplayerapi.md#class_MultiplayerAPI_method_is_server)) and will set root node's network mode to authority, or it will become a regular client peer. All child nodes are set to inherit the network mode by default. Handling of networking-related events (connection, disconnection, new clients) is done by connecting to MultiplayerAPI's signals.

---

### Method Descriptions

<span id="class_MultiplayerAPI_method_create_default_interface"></span>

[MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) **create_default_interface** ( ) *static* [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_create_default_interface)

Returns a new instance of the default MultiplayerAPI.

---

<span id="class_MultiplayerAPI_method_get_default_interface"></span>

[StringName](class_stringname.md#class_StringName) **get_default_interface** ( ) *static* [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_get_default_interface)

Returns the default MultiplayerAPI implementation class name. This is usually `"SceneMultiplayer"` when [SceneMultiplayer](class_scenemultiplayer.md#class_SceneMultiplayer) is available. See [set_default_interface()](class_multiplayerapi.md#class_MultiplayerAPI_method_set_default_interface).

---

<span id="class_MultiplayerAPI_method_get_peers"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_peers** ( ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_get_peers)

Returns the peer IDs of all connected peers of this MultiplayerAPI's [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer).

---

<span id="class_MultiplayerAPI_method_get_remote_sender_id"></span>

[int](class_int.md#class_int) **get_remote_sender_id** ( ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_get_remote_sender_id)

Returns the sender's peer ID for the RPC currently being executed.

 **Note:** This method returns `0` when called outside of an RPC. As such, the original peer ID may be lost when code execution is delayed (such as with GDScript's `await` keyword).

---

<span id="class_MultiplayerAPI_method_get_unique_id"></span>

[int](class_int.md#class_int) **get_unique_id** ( ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_get_unique_id)

Returns the unique peer ID of this MultiplayerAPI's [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer).

---

<span id="class_MultiplayerAPI_method_has_multiplayer_peer"></span>

[bool](class_bool.md#class_bool) **has_multiplayer_peer** ( ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_has_multiplayer_peer)

Returns `true` if there is a [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer) set.

---

<span id="class_MultiplayerAPI_method_is_server"></span>

[bool](class_bool.md#class_bool) **is_server** ( ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_is_server)

Returns `true` if this MultiplayerAPI's [multiplayer_peer](class_multiplayerapi.md#class_MultiplayerAPI_property_multiplayer_peer) is valid and in server mode (listening for connections).

---

<span id="class_MultiplayerAPI_method_object_configuration_add"></span>

Error **object_configuration_add** ( object: [Object](class_object.md#class_Object), configuration: [Variant](class_variant.md#class_Variant) ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_object_configuration_add)

Notifies the MultiplayerAPI of a new `configuration` for the given `object`. This method is used internally by [SceneTree](class_scenetree.md#class_SceneTree) to configure the root path for this MultiplayerAPI (passing `null` and a valid [NodePath](class_nodepath.md#class_NodePath) as `configuration`). This method can be further used by MultiplayerAPI implementations to provide additional features, refer to specific implementation (e.g. [SceneMultiplayer](class_scenemultiplayer.md#class_SceneMultiplayer)) for details on how they use it.

 **Note:** This method is mostly relevant when extending or overriding the MultiplayerAPI behavior via [MultiplayerAPIExtension](class_multiplayerapiextension.md#class_MultiplayerAPIExtension).

---

<span id="class_MultiplayerAPI_method_object_configuration_remove"></span>

Error **object_configuration_remove** ( object: [Object](class_object.md#class_Object), configuration: [Variant](class_variant.md#class_Variant) ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_object_configuration_remove)

Notifies the MultiplayerAPI to remove a `configuration` for the given `object`. This method is used internally by [SceneTree](class_scenetree.md#class_SceneTree) to configure the root path for this MultiplayerAPI (passing `null` and an empty [NodePath](class_nodepath.md#class_NodePath) as `configuration`). This method can be further used by MultiplayerAPI implementations to provide additional features, refer to specific implementation (e.g. [SceneMultiplayer](class_scenemultiplayer.md#class_SceneMultiplayer)) for details on how they use it.

 **Note:** This method is mostly relevant when extending or overriding the MultiplayerAPI behavior via [MultiplayerAPIExtension](class_multiplayerapiextension.md#class_MultiplayerAPIExtension).

---

<span id="class_MultiplayerAPI_method_poll"></span>

Error **poll** ( ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_poll)

Method used for polling the MultiplayerAPI. You only need to worry about this if you set [SceneTree.multiplayer_poll](class_scenetree.md#class_SceneTree_property_multiplayer_poll) to `false`. By default, [SceneTree](class_scenetree.md#class_SceneTree) will poll its MultiplayerAPI(s) for you.

 **Note:** This method results in RPCs being called, so they will be executed in the same context of this function (e.g. `_process`, `physics`, [Thread](class_thread.md#class_Thread)).

---

<span id="class_MultiplayerAPI_method_rpc"></span>

Error **rpc** ( peer: [int](class_int.md#class_int), object: [Object](class_object.md#class_Object), method: [StringName](class_stringname.md#class_StringName), arguments: [Array](class_array.md#class_Array) = [] ) [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_rpc)

Sends an RPC to the target `peer`. The given `method` will be called on the remote `object` with the provided `arguments`. The RPC may also be called locally depending on the implementation and RPC configuration. See [Node.rpc()](class_node.md#class_Node_method_rpc) and [Node.rpc_config()](class_node.md#class_Node_method_rpc_config).

 **Note:** Prefer using [Node.rpc()](class_node.md#class_Node_method_rpc), [Node.rpc_id()](class_node.md#class_Node_method_rpc_id), or `my_method.rpc(peer, arg1, arg2, ...)` (in GDScript), since they are faster. This method is mostly useful in conjunction with [MultiplayerAPIExtension](class_multiplayerapiextension.md#class_MultiplayerAPIExtension) when extending or replacing the multiplayer capabilities.

---

<span id="class_MultiplayerAPI_method_set_default_interface"></span>

void **set_default_interface** ( interface_name: [StringName](class_stringname.md#class_StringName) ) *static* [🔗](class_multiplayerapi.md#class_MultiplayerAPI_method_set_default_interface)

Sets the default MultiplayerAPI implementation class. This method can be used by modules and extensions to configure which implementation will be used by [SceneTree](class_scenetree.md#class_SceneTree) when the engine starts.
