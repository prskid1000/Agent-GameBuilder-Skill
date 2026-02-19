.. meta::
	:keywords: network

<span id="class_MultiplayerSpawner"></span>

## MultiplayerSpawner

**Inherits:** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Automatically replicates spawnable nodes from the authority to other multiplayer peers.

### Description

Spawnable scenes can be configured in the editor or through code (see [add_spawnable_scene()](class_multiplayerspawner.md#class_MultiplayerSpawner_method_add_spawnable_scene)).

Also supports custom node spawns through [spawn()](class_multiplayerspawner.md#class_MultiplayerSpawner_method_spawn), calling [spawn_function](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_function) on all peers.

Internally, **MultiplayerSpawner** uses [MultiplayerAPI.object_configuration_add()](class_multiplayerapi.md#class_MultiplayerAPI_method_object_configuration_add) to notify spawns passing the spawned node as the `object` and itself as the `configuration`, and [MultiplayerAPI.object_configuration_remove()](class_multiplayerapi.md#class_MultiplayerAPI_method_object_configuration_remove) to notify despawns in a similar way.

### Properties


| [Callable](class_callable.md#class_Callable) | [spawn_function](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_function) |
| --- | --- |
| [int](class_int.md#class_int) | [spawn_limit](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_limit) | `0` |
| [NodePath](class_nodepath.md#class_NodePath) | [spawn_path](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_path) | `NodePath("")` |

### Methods


| void | [add_spawnable_scene](class_multiplayerspawner.md#class_MultiplayerSpawner_method_add_spawnable_scene) ( path: [String](class_string.md#class_String) ) |
| --- | --- |
| void | [clear_spawnable_scenes](class_multiplayerspawner.md#class_MultiplayerSpawner_method_clear_spawnable_scenes) ( ) |
| [String](class_string.md#class_String) | [get_spawnable_scene](class_multiplayerspawner.md#class_MultiplayerSpawner_method_get_spawnable_scene) ( index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_spawnable_scene_count](class_multiplayerspawner.md#class_MultiplayerSpawner_method_get_spawnable_scene_count) ( ) const |
| [Node](class_node.md#class_Node) | [spawn](class_multiplayerspawner.md#class_MultiplayerSpawner_method_spawn) ( data: [Variant](class_variant.md#class_Variant) = null ) |

---

### Signals

<span id="class_MultiplayerSpawner_signal_despawned"></span>

**despawned** ( node: [Node](class_node.md#class_Node) ) [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_signal_despawned)

Emitted when a spawnable scene or custom spawn was despawned by the multiplayer authority. Only called on remote peers.

---

<span id="class_MultiplayerSpawner_signal_spawned"></span>

**spawned** ( node: [Node](class_node.md#class_Node) ) [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_signal_spawned)

Emitted when a spawnable scene or custom spawn was spawned by the multiplayer authority. Only called on remote peers.

---

### Property Descriptions

<span id="class_MultiplayerSpawner_property_spawn_function"></span>

[Callable](class_callable.md#class_Callable) **spawn_function** [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_function)

- void **set_spawn_function** ( value: [Callable](class_callable.md#class_Callable) )
- [Callable](class_callable.md#class_Callable) **get_spawn_function** ( )

Method called on all peers when a custom [spawn()](class_multiplayerspawner.md#class_MultiplayerSpawner_method_spawn) is requested by the authority. Will receive the `data` parameter, and should return a [Node](class_node.md#class_Node) that is not in the scene tree.

 **Note:** The returned node should **not** be added to the scene with [Node.add_child()](class_node.md#class_Node_method_add_child). This is done automatically.

---

<span id="class_MultiplayerSpawner_property_spawn_limit"></span>

[int](class_int.md#class_int) **spawn_limit** = `0` [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_limit)

- void **set_spawn_limit** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_spawn_limit** ( )

Maximum number of nodes allowed to be spawned by this spawner. Includes both spawnable scenes and custom spawns.

When set to `0` (the default), there is no limit.

---

<span id="class_MultiplayerSpawner_property_spawn_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **spawn_path** = `NodePath("")` [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_path)

- void **set_spawn_path** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_spawn_path** ( )

Path to the spawn root. Spawnable scenes that are added as direct children are replicated to other peers.

---

### Method Descriptions

<span id="class_MultiplayerSpawner_method_add_spawnable_scene"></span>

void **add_spawnable_scene** ( path: [String](class_string.md#class_String) ) [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_method_add_spawnable_scene)

Adds a scene path to spawnable scenes, making it automatically replicated from the multiplayer authority to other peers when added as children of the node pointed by [spawn_path](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_path).

---

<span id="class_MultiplayerSpawner_method_clear_spawnable_scenes"></span>

void **clear_spawnable_scenes** ( ) [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_method_clear_spawnable_scenes)

Clears all spawnable scenes. Does not despawn existing instances on remote peers.

---

<span id="class_MultiplayerSpawner_method_get_spawnable_scene"></span>

[String](class_string.md#class_String) **get_spawnable_scene** ( index: [int](class_int.md#class_int) ) *const* [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_method_get_spawnable_scene)

Returns the spawnable scene path by index.

---

<span id="class_MultiplayerSpawner_method_get_spawnable_scene_count"></span>

[int](class_int.md#class_int) **get_spawnable_scene_count** ( ) *const* [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_method_get_spawnable_scene_count)

Returns the count of spawnable scene paths.

---

<span id="class_MultiplayerSpawner_method_spawn"></span>

[Node](class_node.md#class_Node) **spawn** ( data: [Variant](class_variant.md#class_Variant) = null ) [🔗](class_multiplayerspawner.md#class_MultiplayerSpawner_method_spawn)

Requests a custom spawn, with `data` passed to [spawn_function](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_function) on all peers. Returns the locally spawned node instance already inside the scene tree, and added as a child of the node pointed by [spawn_path](class_multiplayerspawner.md#class_MultiplayerSpawner_property_spawn_path).

 **Note:** Spawnable scenes are spawned automatically. [spawn()](class_multiplayerspawner.md#class_MultiplayerSpawner_method_spawn) is only needed for custom spawns.
