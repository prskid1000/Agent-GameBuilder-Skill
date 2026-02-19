<span id="class_SceneTree"></span>

## SceneTree

**Inherits:** [MainLoop](class_mainloop.md#class_MainLoop) **<** [Object](class_object.md#class_Object)

Manages the game loop via a hierarchy of nodes.

### Description

As one of the most important classes, the **SceneTree** manages the hierarchy of nodes in a scene, as well as scenes themselves. Nodes can be added, fetched and removed. The whole scene tree (and thus the current scene) can be paused. Scenes can be loaded, switched and reloaded.

You can also use the **SceneTree** to organize your nodes into **groups**: every node can be added to as many groups as you want to create, e.g. an "enemy" group. You can then iterate these groups or even call methods and set properties on all the nodes belonging to any given group.

 **SceneTree** is the default [MainLoop](class_mainloop.md#class_MainLoop) implementation used by the engine, and is thus in charge of the game loop.

### Tutorials

- [SceneTree](../tutorials/scripting/scene_tree.md)

- [Multiple resolutions](../tutorials/rendering/multiple_resolutions.md)

### Properties


| [bool](class_bool.md#class_bool) | [auto_accept_quit](class_scenetree.md#class_SceneTree_property_auto_accept_quit) | `true` |
| --- | --- | --- |
| [Node](class_node.md#class_Node) | [current_scene](class_scenetree.md#class_SceneTree_property_current_scene) |
| [bool](class_bool.md#class_bool) | [debug_collisions_hint](class_scenetree.md#class_SceneTree_property_debug_collisions_hint) | `false` |
| [bool](class_bool.md#class_bool) | [debug_navigation_hint](class_scenetree.md#class_SceneTree_property_debug_navigation_hint) | `false` |
| [bool](class_bool.md#class_bool) | [debug_paths_hint](class_scenetree.md#class_SceneTree_property_debug_paths_hint) | `false` |
| [Node](class_node.md#class_Node) | [edited_scene_root](class_scenetree.md#class_SceneTree_property_edited_scene_root) |
| [bool](class_bool.md#class_bool) | [multiplayer_poll](class_scenetree.md#class_SceneTree_property_multiplayer_poll) | `true` |
| [bool](class_bool.md#class_bool) | [paused](class_scenetree.md#class_SceneTree_property_paused) | `false` |
| [bool](class_bool.md#class_bool) | [physics_interpolation](class_scenetree.md#class_SceneTree_property_physics_interpolation) | `false` |
| [bool](class_bool.md#class_bool) | [quit_on_go_back](class_scenetree.md#class_SceneTree_property_quit_on_go_back) | `true` |
| [Window](class_window.md#class_Window) | [root](class_scenetree.md#class_SceneTree_property_root) |

### Methods


| void | [call_group](class_scenetree.md#class_SceneTree_method_call_group) ( group: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), ... ) vararg |
| --- | --- |
| void | [call_group_flags](class_scenetree.md#class_SceneTree_method_call_group_flags) ( flags: [int](class_int.md#class_int), group: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), ... ) vararg |
| Error | [change_scene_to_file](class_scenetree.md#class_SceneTree_method_change_scene_to_file) ( path: [String](class_string.md#class_String) ) |
| Error | [change_scene_to_node](class_scenetree.md#class_SceneTree_method_change_scene_to_node) ( node: [Node](class_node.md#class_Node) ) |
| Error | [change_scene_to_packed](class_scenetree.md#class_SceneTree_method_change_scene_to_packed) ( packed_scene: [PackedScene](class_packedscene.md#class_PackedScene) ) |
| [SceneTreeTimer](class_scenetreetimer.md#class_SceneTreeTimer) | [create_timer](class_scenetree.md#class_SceneTree_method_create_timer) ( time_sec: [float](class_float.md#class_float), process_always: [bool](class_bool.md#class_bool) = true, process_in_physics: [bool](class_bool.md#class_bool) = false, ignore_time_scale: [bool](class_bool.md#class_bool) = false ) |
| [Tween](class_tween.md#class_Tween) | [create_tween](class_scenetree.md#class_SceneTree_method_create_tween) ( ) |
| [Node](class_node.md#class_Node) | [get_first_node_in_group](class_scenetree.md#class_SceneTree_method_get_first_node_in_group) ( group: [StringName](class_stringname.md#class_StringName) ) |
| [int](class_int.md#class_int) | [get_frame](class_scenetree.md#class_SceneTree_method_get_frame) ( ) const |
| [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) | [get_multiplayer](class_scenetree.md#class_SceneTree_method_get_multiplayer) ( for_path: [NodePath](class_nodepath.md#class_NodePath) = NodePath("") ) const |
| [int](class_int.md#class_int) | [get_node_count](class_scenetree.md#class_SceneTree_method_get_node_count) ( ) const |
| [int](class_int.md#class_int) | [get_node_count_in_group](class_scenetree.md#class_SceneTree_method_get_node_count_in_group) ( group: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[Node](class_node.md#class_Node)\] | [get_nodes_in_group](class_scenetree.md#class_SceneTree_method_get_nodes_in_group) ( group: [StringName](class_stringname.md#class_StringName) ) |
| [Array](class_array.md#class_Array)\[[Tween](class_tween.md#class_Tween)\] | [get_processed_tweens](class_scenetree.md#class_SceneTree_method_get_processed_tweens) ( ) |
| [bool](class_bool.md#class_bool) | [has_group](class_scenetree.md#class_SceneTree_method_has_group) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [bool](class_bool.md#class_bool) | [is_accessibility_enabled](class_scenetree.md#class_SceneTree_method_is_accessibility_enabled) ( ) const |
| [bool](class_bool.md#class_bool) | [is_accessibility_supported](class_scenetree.md#class_SceneTree_method_is_accessibility_supported) ( ) const |
| void | [notify_group](class_scenetree.md#class_SceneTree_method_notify_group) ( group: [StringName](class_stringname.md#class_StringName), notification: [int](class_int.md#class_int) ) |
| void | [notify_group_flags](class_scenetree.md#class_SceneTree_method_notify_group_flags) ( call_flags: [int](class_int.md#class_int), group: [StringName](class_stringname.md#class_StringName), notification: [int](class_int.md#class_int) ) |
| void | [queue_delete](class_scenetree.md#class_SceneTree_method_queue_delete) ( obj: [Object](class_object.md#class_Object) ) |
| void | [quit](class_scenetree.md#class_SceneTree_method_quit) ( exit_code: [int](class_int.md#class_int) = 0 ) |
| Error | [reload_current_scene](class_scenetree.md#class_SceneTree_method_reload_current_scene) ( ) |
| void | [set_group](class_scenetree.md#class_SceneTree_method_set_group) ( group: [StringName](class_stringname.md#class_StringName), property: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) |
| void | [set_group_flags](class_scenetree.md#class_SceneTree_method_set_group_flags) ( call_flags: [int](class_int.md#class_int), group: [StringName](class_stringname.md#class_StringName), property: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) |
| void | [set_multiplayer](class_scenetree.md#class_SceneTree_method_set_multiplayer) ( multiplayer: [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI), root_path: [NodePath](class_nodepath.md#class_NodePath) = NodePath("") ) |
| void | [unload_current_scene](class_scenetree.md#class_SceneTree_method_unload_current_scene) ( ) |

---

### Signals

<span id="class_SceneTree_signal_node_added"></span>

**node_added** ( node: [Node](class_node.md#class_Node) ) [🔗](class_scenetree.md#class_SceneTree_signal_node_added)

Emitted when the `node` enters this tree.

---

<span id="class_SceneTree_signal_node_configuration_warning_changed"></span>

**node_configuration_warning_changed** ( node: [Node](class_node.md#class_Node) ) [🔗](class_scenetree.md#class_SceneTree_signal_node_configuration_warning_changed)

Emitted when the `node`'s [Node.update_configuration_warnings()](class_node.md#class_Node_method_update_configuration_warnings) is called. Only emitted in the editor.

---

<span id="class_SceneTree_signal_node_removed"></span>

**node_removed** ( node: [Node](class_node.md#class_Node) ) [🔗](class_scenetree.md#class_SceneTree_signal_node_removed)

Emitted when the `node` exits this tree.

---

<span id="class_SceneTree_signal_node_renamed"></span>

**node_renamed** ( node: [Node](class_node.md#class_Node) ) [🔗](class_scenetree.md#class_SceneTree_signal_node_renamed)

Emitted when the `node`'s [Node.name](class_node.md#class_Node_property_name) is changed.

---

<span id="class_SceneTree_signal_physics_frame"></span>

**physics_frame** ( ) [🔗](class_scenetree.md#class_SceneTree_signal_physics_frame)

Emitted immediately before [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) is called on every node in this tree.

---

<span id="class_SceneTree_signal_process_frame"></span>

**process_frame** ( ) [🔗](class_scenetree.md#class_SceneTree_signal_process_frame)

Emitted immediately before [Node._process()](class_node.md#class_Node_private_method__process) is called on every node in this tree.

---

<span id="class_SceneTree_signal_scene_changed"></span>

**scene_changed** ( ) [🔗](class_scenetree.md#class_SceneTree_signal_scene_changed)

Emitted after the new scene is added to scene tree and initialized. Can be used to reliably access [current_scene](class_scenetree.md#class_SceneTree_property_current_scene) when changing scenes.

::

    # This code should be inside an autoload.
    get_tree().change_scene_to_file(other_scene_path)
    await get_tree().scene_changed
    print(get_tree().current_scene) # Prints the new scene.

---

<span id="class_SceneTree_signal_tree_changed"></span>

**tree_changed** ( ) [🔗](class_scenetree.md#class_SceneTree_signal_tree_changed)

Emitted any time the tree's hierarchy changes (nodes being moved, renamed, etc.).

---

<span id="class_SceneTree_signal_tree_process_mode_changed"></span>

**tree_process_mode_changed** ( ) [🔗](class_scenetree.md#class_SceneTree_signal_tree_process_mode_changed)

Emitted when the [Node.process_mode](class_node.md#class_Node_property_process_mode) of any node inside the tree is changed. Only emitted in the editor, to update the visibility of disabled nodes.

---

### Enumerations

<span id="enum_SceneTree_GroupCallFlags"></span>

enum **GroupCallFlags**: [🔗](class_scenetree.md#enum_SceneTree_GroupCallFlags)

<span id="class_SceneTree_constant_GROUP_CALL_DEFAULT"></span>

[GroupCallFlags](class_scenetree.md#enum_SceneTree_GroupCallFlags) **GROUP_CALL_DEFAULT** = `0`

Call nodes within a group with no special behavior (default).

<span id="class_SceneTree_constant_GROUP_CALL_REVERSE"></span>

[GroupCallFlags](class_scenetree.md#enum_SceneTree_GroupCallFlags) **GROUP_CALL_REVERSE** = `1`

Call nodes within a group in reverse tree hierarchy order (all nested children are called before their respective parent nodes).

<span id="class_SceneTree_constant_GROUP_CALL_DEFERRED"></span>

[GroupCallFlags](class_scenetree.md#enum_SceneTree_GroupCallFlags) **GROUP_CALL_DEFERRED** = `2`

Call nodes within a group at the end of the current frame (can be either process or physics frame), similar to [Object.call_deferred()](class_object.md#class_Object_method_call_deferred).

<span id="class_SceneTree_constant_GROUP_CALL_UNIQUE"></span>

[GroupCallFlags](class_scenetree.md#enum_SceneTree_GroupCallFlags) **GROUP_CALL_UNIQUE** = `4`

Call nodes within a group only once, even if the call is executed many times in the same frame. Must be combined with [GROUP_CALL_DEFERRED](class_scenetree.md#class_SceneTree_constant_GROUP_CALL_DEFERRED) to work.

 **Note:** Different arguments are not taken into account. Therefore, when the same call is executed with different arguments, only the first call will be performed.

---

### Property Descriptions

<span id="class_SceneTree_property_auto_accept_quit"></span>

[bool](class_bool.md#class_bool) **auto_accept_quit** = `true` [🔗](class_scenetree.md#class_SceneTree_property_auto_accept_quit)

- void **set_auto_accept_quit** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_auto_accept_quit** ( )

If `true`, the application automatically accepts quitting requests.

For mobile platforms, see [quit_on_go_back](class_scenetree.md#class_SceneTree_property_quit_on_go_back).

---

<span id="class_SceneTree_property_current_scene"></span>

[Node](class_node.md#class_Node) **current_scene** [🔗](class_scenetree.md#class_SceneTree_property_current_scene)

- void **set_current_scene** ( value: [Node](class_node.md#class_Node) )
- [Node](class_node.md#class_Node) **get_current_scene** ( )

The root node of the currently loaded main scene, usually as a direct child of [root](class_scenetree.md#class_SceneTree_property_root). See also [change_scene_to_file()](class_scenetree.md#class_SceneTree_method_change_scene_to_file), [change_scene_to_packed()](class_scenetree.md#class_SceneTree_method_change_scene_to_packed), and [reload_current_scene()](class_scenetree.md#class_SceneTree_method_reload_current_scene).

 **Warning:** Setting this property directly may not work as expected, as it does *not* add or remove any nodes from this tree.

---

<span id="class_SceneTree_property_debug_collisions_hint"></span>

[bool](class_bool.md#class_bool) **debug_collisions_hint** = `false` [🔗](class_scenetree.md#class_SceneTree_property_debug_collisions_hint)

- void **set_debug_collisions_hint** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_debugging_collisions_hint** ( )

If `true`, collision shapes will be visible when running the game from the editor for debugging purposes.

 **Note:** This property is not designed to be changed at run-time. Changing the value of [debug_collisions_hint](class_scenetree.md#class_SceneTree_property_debug_collisions_hint) while the project is running will not have the desired effect.

---

<span id="class_SceneTree_property_debug_navigation_hint"></span>

[bool](class_bool.md#class_bool) **debug_navigation_hint** = `false` [🔗](class_scenetree.md#class_SceneTree_property_debug_navigation_hint)

- void **set_debug_navigation_hint** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_debugging_navigation_hint** ( )

If `true`, navigation polygons will be visible when running the game from the editor for debugging purposes.

 **Note:** This property is not designed to be changed at run-time. Changing the value of [debug_navigation_hint](class_scenetree.md#class_SceneTree_property_debug_navigation_hint) while the project is running will not have the desired effect.

---

<span id="class_SceneTree_property_debug_paths_hint"></span>

[bool](class_bool.md#class_bool) **debug_paths_hint** = `false` [🔗](class_scenetree.md#class_SceneTree_property_debug_paths_hint)

- void **set_debug_paths_hint** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_debugging_paths_hint** ( )

If `true`, curves from [Path2D](class_path2d.md#class_Path2D) and [Path3D](class_path3d.md#class_Path3D) nodes will be visible when running the game from the editor for debugging purposes.

 **Note:** This property is not designed to be changed at run-time. Changing the value of [debug_paths_hint](class_scenetree.md#class_SceneTree_property_debug_paths_hint) while the project is running will not have the desired effect.

---

<span id="class_SceneTree_property_edited_scene_root"></span>

[Node](class_node.md#class_Node) **edited_scene_root** [🔗](class_scenetree.md#class_SceneTree_property_edited_scene_root)

- void **set_edited_scene_root** ( value: [Node](class_node.md#class_Node) )
- [Node](class_node.md#class_Node) **get_edited_scene_root** ( )

The root of the scene currently being edited in the editor. This is usually a direct child of [root](class_scenetree.md#class_SceneTree_property_root).

 **Note:** This property does nothing in release builds.

---

<span id="class_SceneTree_property_multiplayer_poll"></span>

[bool](class_bool.md#class_bool) **multiplayer_poll** = `true` [🔗](class_scenetree.md#class_SceneTree_property_multiplayer_poll)

- void **set_multiplayer_poll_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_multiplayer_poll_enabled** ( )

If `true` (default value), enables automatic polling of the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) for this SceneTree during [process_frame](class_scenetree.md#class_SceneTree_signal_process_frame).

If `false`, you need to manually call [MultiplayerAPI.poll()](class_multiplayerapi.md#class_MultiplayerAPI_method_poll) to process network packets and deliver RPCs. This allows running RPCs in a different loop (e.g. physics, thread, specific time step) and for manual [Mutex](class_mutex.md#class_Mutex) protection when accessing the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) from threads.

---

<span id="class_SceneTree_property_paused"></span>

[bool](class_bool.md#class_bool) **paused** = `false` [🔗](class_scenetree.md#class_SceneTree_property_paused)

- void **set_pause** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_paused** ( )

If `true`, the scene tree is considered paused. This causes the following behavior:

- 2D and 3D physics will be stopped, as well as collision detection and related signals.

- Depending on each node's [Node.process_mode](class_node.md#class_Node_property_process_mode), their [Node._process()](class_node.md#class_Node_private_method__process), [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) and [Node._input()](class_node.md#class_Node_private_method__input) callback methods may not called anymore.

---

<span id="class_SceneTree_property_physics_interpolation"></span>

[bool](class_bool.md#class_bool) **physics_interpolation** = `false` [🔗](class_scenetree.md#class_SceneTree_property_physics_interpolation)

- void **set_physics_interpolation_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_physics_interpolation_enabled** ( )

If `true`, the renderer will interpolate the transforms of objects (both physics and non-physics) between the last two transforms, so that smooth motion is seen even when physics ticks do not coincide with rendered frames.

The default value of this property is controlled by ProjectSettings.physics/common/physics_interpolation.

 **Note:** Although this is a global setting, finer control of individual branches of the **SceneTree** is possible using [Node.physics_interpolation_mode](class_node.md#class_Node_property_physics_interpolation_mode).

---

<span id="class_SceneTree_property_quit_on_go_back"></span>

[bool](class_bool.md#class_bool) **quit_on_go_back** = `true` [🔗](class_scenetree.md#class_SceneTree_property_quit_on_go_back)

- void **set_quit_on_go_back** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_quit_on_go_back** ( )

If `true`, the application quits automatically when navigating back (e.g. using the system "Back" button on Android).

To handle 'Go Back' button when this option is disabled, use [DisplayServer.WINDOW_EVENT_GO_BACK_REQUEST](class_displayserver.md#class_DisplayServer_constant_WINDOW_EVENT_GO_BACK_REQUEST).

---

<span id="class_SceneTree_property_root"></span>

[Window](class_window.md#class_Window) **root** [🔗](class_scenetree.md#class_SceneTree_property_root)

- [Window](class_window.md#class_Window) **get_root** ( )

The tree's root [Window](class_window.md#class_Window). This is top-most [Node](class_node.md#class_Node) of the scene tree, and is always present. An absolute [NodePath](class_nodepath.md#class_NodePath) always starts from this node. Children of the root node may include the loaded [current_scene](class_scenetree.md#class_SceneTree_property_current_scene), as well as any [AutoLoad](../tutorials/scripting/singletons_autoload.md) configured in the Project Settings.

 **Warning:** Do not delete this node. This will result in unstable behavior, followed by a crash.

---

### Method Descriptions

<span id="class_SceneTree_method_call_group"></span>

void **call_group** ( group: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), ... ) *vararg* [🔗](class_scenetree.md#class_SceneTree_method_call_group)

Calls `method` on each node inside this tree added to the given `group`. You can pass arguments to `method` by specifying them at the end of this method call. Nodes that cannot call `method` (either because the method doesn't exist or the arguments do not match) are ignored. See also [set_group()](class_scenetree.md#class_SceneTree_method_set_group) and [notify_group()](class_scenetree.md#class_SceneTree_method_notify_group).

 **Note:** This method acts immediately on all selected nodes at once, which may cause stuttering in some performance-intensive situations.

 **Note:** In C#, `method` must be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in the `MethodName` class to avoid allocating a new [StringName](class_stringname.md#class_StringName) on each call.

---

<span id="class_SceneTree_method_call_group_flags"></span>

void **call_group_flags** ( flags: [int](class_int.md#class_int), group: [StringName](class_stringname.md#class_StringName), method: [StringName](class_stringname.md#class_StringName), ... ) *vararg* [🔗](class_scenetree.md#class_SceneTree_method_call_group_flags)

Calls the given `method` on each node inside this tree added to the given `group`. Use `flags` to customize this method's behavior (see [GroupCallFlags](class_scenetree.md#enum_SceneTree_GroupCallFlags)). Additional arguments for `method` can be passed at the end of this method. Nodes that cannot call `method` (either because the method doesn't exist or the arguments do not match) are ignored.

::

    # Calls "hide" to all nodes of the "enemies" group, at the end of the frame and in reverse tree order.
    get_tree().call_group_flags(
            SceneTree.GROUP_CALL_DEFERRED | SceneTree.GROUP_CALL_REVERSE,
            "enemies", "hide")

 **Note:** In C#, `method` must be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in the `MethodName` class to avoid allocating a new [StringName](class_stringname.md#class_StringName) on each call.

---

<span id="class_SceneTree_method_change_scene_to_file"></span>

Error **change_scene_to_file** ( path: [String](class_string.md#class_String) ) [🔗](class_scenetree.md#class_SceneTree_method_change_scene_to_file)

Changes the running scene to the one at the given `path`, after loading it into a [PackedScene](class_packedscene.md#class_PackedScene) and creating a new instance.

Returns @GlobalScope.OK on success, @GlobalScope.ERR_CANT_OPEN if the `path` cannot be loaded into a [PackedScene](class_packedscene.md#class_PackedScene), or @GlobalScope.ERR_CANT_CREATE if that scene cannot be instantiated.

 **Note:** See [change_scene_to_node()](class_scenetree.md#class_SceneTree_method_change_scene_to_node) for details on the order of operations.

---

<span id="class_SceneTree_method_change_scene_to_node"></span>

Error **change_scene_to_node** ( node: [Node](class_node.md#class_Node) ) [🔗](class_scenetree.md#class_SceneTree_method_change_scene_to_node)

Changes the running scene to the provided [Node](class_node.md#class_Node). Useful when you want to set up the new scene before changing.

Returns @GlobalScope.OK on success, @GlobalScope.ERR_INVALID_PARAMETER if the `node` is `null`, or @GlobalScope.ERR_UNCONFIGURED if the `node` is already inside the scene tree.

 **Note:** Operations happen in the following order when [change_scene_to_node()](class_scenetree.md#class_SceneTree_method_change_scene_to_node) is called:

1. The current scene node is immediately removed from the tree. From that point, [Node.get_tree()](class_node.md#class_Node_method_get_tree) called on the current (outgoing) scene will return `null`. [current_scene](class_scenetree.md#class_SceneTree_property_current_scene) will be `null` too, because the new scene is not available yet.

2. At the end of the frame, the formerly current scene, already removed from the tree, will be deleted (freed from memory) and then the new scene node will be added to the tree. [Node.get_tree()](class_node.md#class_Node_method_get_tree) and [current_scene](class_scenetree.md#class_SceneTree_property_current_scene) will be back to working as usual.

This ensures that both scenes aren't running at the same time, while still freeing the previous scene in a safe way similar to [Node.queue_free()](class_node.md#class_Node_method_queue_free).

If you want to reliably access the new scene, await the [scene_changed](class_scenetree.md#class_SceneTree_signal_scene_changed) signal.

 **Warning:** After using this method, the **SceneTree** will take ownership of the node and will free it automatically when changing scene again. Any references you had to that node will become invalid.

---

<span id="class_SceneTree_method_change_scene_to_packed"></span>

Error **change_scene_to_packed** ( packed_scene: [PackedScene](class_packedscene.md#class_PackedScene) ) [🔗](class_scenetree.md#class_SceneTree_method_change_scene_to_packed)

Changes the running scene to a new instance of the given [PackedScene](class_packedscene.md#class_PackedScene) (which must be valid).

Returns @GlobalScope.OK on success, @GlobalScope.ERR_CANT_CREATE if the scene cannot be instantiated, or @GlobalScope.ERR_INVALID_PARAMETER if the scene is invalid.

 **Note:** See [change_scene_to_node()](class_scenetree.md#class_SceneTree_method_change_scene_to_node) for details on the order of operations.

---

<span id="class_SceneTree_method_create_timer"></span>

[SceneTreeTimer](class_scenetreetimer.md#class_SceneTreeTimer) **create_timer** ( time_sec: [float](class_float.md#class_float), process_always: [bool](class_bool.md#class_bool) = true, process_in_physics: [bool](class_bool.md#class_bool) = false, ignore_time_scale: [bool](class_bool.md#class_bool) = false ) [🔗](class_scenetree.md#class_SceneTree_method_create_timer)

Returns a new [SceneTreeTimer](class_scenetreetimer.md#class_SceneTreeTimer). After `time_sec` in seconds have passed, the timer will emit [SceneTreeTimer.timeout](class_scenetreetimer.md#class_SceneTreeTimer_signal_timeout) and will be automatically freed.

If `process_always` is `false`, the timer will be paused when setting [paused](class_scenetree.md#class_SceneTree_property_paused) to `true`.

If `process_in_physics` is `true`, the timer will update at the end of the physics frame, instead of the process frame.

If `ignore_time_scale` is `true`, the timer will ignore [Engine.time_scale](class_engine.md#class_Engine_property_time_scale) and update with the real, elapsed time.

This method is commonly used to create a one-shot delay timer, as in the following example:

.. tabs::

```
```

    func some_function():
        print("start")
        await get_tree().create_timer(1.0).timeout
        print("end")

```
```

    public async Task SomeFunction()
    {
        GD.Print("start");
        await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
        GD.Print("end");
    }

 **Note:** The timer is always updated *after* all of the nodes in the tree. A node's [Node._process()](class_node.md#class_Node_private_method__process) method would be called before the timer updates (or [Node._physics_process()](class_node.md#class_Node_private_method__physics_process) if `process_in_physics` is set to `true`).

---

<span id="class_SceneTree_method_create_tween"></span>

[Tween](class_tween.md#class_Tween) **create_tween** ( ) [🔗](class_scenetree.md#class_SceneTree_method_create_tween)

Creates and returns a new [Tween](class_tween.md#class_Tween) processed in this tree. The Tween will start automatically on the next process frame or physics frame (depending on its [TweenProcessMode](class_tween.md#enum_Tween_TweenProcessMode)).

 **Note:** A [Tween](class_tween.md#class_Tween) created using this method is not bound to any [Node](class_node.md#class_Node). It may keep working until there is nothing left to animate. If you want the [Tween](class_tween.md#class_Tween) to be automatically killed when the [Node](class_node.md#class_Node) is freed, use [Node.create_tween()](class_node.md#class_Node_method_create_tween) or [Tween.bind_node()](class_tween.md#class_Tween_method_bind_node).

---

<span id="class_SceneTree_method_get_first_node_in_group"></span>

[Node](class_node.md#class_Node) **get_first_node_in_group** ( group: [StringName](class_stringname.md#class_StringName) ) [🔗](class_scenetree.md#class_SceneTree_method_get_first_node_in_group)

Returns the first [Node](class_node.md#class_Node) found inside the tree, that has been added to the given `group`, in scene hierarchy order. Returns `null` if no match is found. See also [get_nodes_in_group()](class_scenetree.md#class_SceneTree_method_get_nodes_in_group).

---

<span id="class_SceneTree_method_get_frame"></span>

[int](class_int.md#class_int) **get_frame** ( ) *const* [🔗](class_scenetree.md#class_SceneTree_method_get_frame)

Returns how many physics process steps have been processed, since the application started. This is *not* a measurement of elapsed time. See also [physics_frame](class_scenetree.md#class_SceneTree_signal_physics_frame). For the number of frames rendered, see [Engine.get_process_frames()](class_engine.md#class_Engine_method_get_process_frames).

---

<span id="class_SceneTree_method_get_multiplayer"></span>

[MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) **get_multiplayer** ( for_path: [NodePath](class_nodepath.md#class_NodePath) = NodePath("") ) *const* [🔗](class_scenetree.md#class_SceneTree_method_get_multiplayer)

Searches for the [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) configured for the given path, if one does not exist it searches the parent paths until one is found. If the path is empty, or none is found, the default one is returned. See [set_multiplayer()](class_scenetree.md#class_SceneTree_method_set_multiplayer).

---

<span id="class_SceneTree_method_get_node_count"></span>

[int](class_int.md#class_int) **get_node_count** ( ) *const* [🔗](class_scenetree.md#class_SceneTree_method_get_node_count)

Returns the number of nodes inside this tree.

---

<span id="class_SceneTree_method_get_node_count_in_group"></span>

[int](class_int.md#class_int) **get_node_count_in_group** ( group: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_scenetree.md#class_SceneTree_method_get_node_count_in_group)

Returns the number of nodes assigned to the given group.

---

<span id="class_SceneTree_method_get_nodes_in_group"></span>

[Array](class_array.md#class_Array)\[[Node](class_node.md#class_Node)\] **get_nodes_in_group** ( group: [StringName](class_stringname.md#class_StringName) ) [🔗](class_scenetree.md#class_SceneTree_method_get_nodes_in_group)

Returns an [Array](class_array.md#class_Array) containing all nodes inside this tree, that have been added to the given `group`, in scene hierarchy order.

---

<span id="class_SceneTree_method_get_processed_tweens"></span>

[Array](class_array.md#class_Array)\[[Tween](class_tween.md#class_Tween)\] **get_processed_tweens** ( ) [🔗](class_scenetree.md#class_SceneTree_method_get_processed_tweens)

Returns an [Array](class_array.md#class_Array) of currently existing [Tween](class_tween.md#class_Tween) s in the tree, including paused tweens.

---

<span id="class_SceneTree_method_has_group"></span>

[bool](class_bool.md#class_bool) **has_group** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_scenetree.md#class_SceneTree_method_has_group)

Returns `true` if a node added to the given group `name` exists in the tree.

---

<span id="class_SceneTree_method_is_accessibility_enabled"></span>

[bool](class_bool.md#class_bool) **is_accessibility_enabled** ( ) *const* [🔗](class_scenetree.md#class_SceneTree_method_is_accessibility_enabled)

Returns `true` if accessibility features are enabled, and accessibility information updates are actively processed.

---

<span id="class_SceneTree_method_is_accessibility_supported"></span>

[bool](class_bool.md#class_bool) **is_accessibility_supported** ( ) *const* [🔗](class_scenetree.md#class_SceneTree_method_is_accessibility_supported)

Returns `true` if accessibility features are supported by the OS and enabled in project settings.

---

<span id="class_SceneTree_method_notify_group"></span>

void **notify_group** ( group: [StringName](class_stringname.md#class_StringName), notification: [int](class_int.md#class_int) ) [🔗](class_scenetree.md#class_SceneTree_method_notify_group)

Calls [Object.notification()](class_object.md#class_Object_method_notification) with the given `notification` to all nodes inside this tree added to the `group`. See also [Godot notifications](../tutorials/best_practices/godot_notifications.md) and [call_group()](class_scenetree.md#class_SceneTree_method_call_group) and [set_group()](class_scenetree.md#class_SceneTree_method_set_group).

 **Note:** This method acts immediately on all selected nodes at once, which may cause stuttering in some performance-intensive situations.

---

<span id="class_SceneTree_method_notify_group_flags"></span>

void **notify_group_flags** ( call_flags: [int](class_int.md#class_int), group: [StringName](class_stringname.md#class_StringName), notification: [int](class_int.md#class_int) ) [🔗](class_scenetree.md#class_SceneTree_method_notify_group_flags)

Calls [Object.notification()](class_object.md#class_Object_method_notification) with the given `notification` to all nodes inside this tree added to the `group`. Use `call_flags` to customize this method's behavior (see [GroupCallFlags](class_scenetree.md#enum_SceneTree_GroupCallFlags)).

---

<span id="class_SceneTree_method_queue_delete"></span>

void **queue_delete** ( obj: [Object](class_object.md#class_Object) ) [🔗](class_scenetree.md#class_SceneTree_method_queue_delete)

Queues the given `obj` to be deleted, calling its [Object.free()](class_object.md#class_Object_method_free) at the end of the current frame. This method is similar to [Node.queue_free()](class_node.md#class_Node_method_queue_free).

---

<span id="class_SceneTree_method_quit"></span>

void **quit** ( exit_code: [int](class_int.md#class_int) = 0 ) [🔗](class_scenetree.md#class_SceneTree_method_quit)

Quits the application at the end of the current iteration, with the given `exit_code`.

By convention, an exit code of `0` indicates success, whereas any other exit code indicates an error. For portability reasons, it should be between `0` and `125` (inclusive).

 **Note:** On iOS this method doesn't work. Instead, as recommended by the iOS Human Interface Guidelines, the user is expected to close apps via the Home button.

---

<span id="class_SceneTree_method_reload_current_scene"></span>

Error **reload_current_scene** ( ) [🔗](class_scenetree.md#class_SceneTree_method_reload_current_scene)

Reloads the currently active scene, replacing [current_scene](class_scenetree.md#class_SceneTree_property_current_scene) with a new instance of its original [PackedScene](class_packedscene.md#class_PackedScene).

Returns @GlobalScope.OK on success, @GlobalScope.ERR_UNCONFIGURED if no [current_scene](class_scenetree.md#class_SceneTree_property_current_scene) is defined, @GlobalScope.ERR_CANT_OPEN if [current_scene](class_scenetree.md#class_SceneTree_property_current_scene) cannot be loaded into a [PackedScene](class_packedscene.md#class_PackedScene), or @GlobalScope.ERR_CANT_CREATE if the scene cannot be instantiated.

---

<span id="class_SceneTree_method_set_group"></span>

void **set_group** ( group: [StringName](class_stringname.md#class_StringName), property: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_scenetree.md#class_SceneTree_method_set_group)

Sets the given `property` to `value` on all nodes inside this tree added to the given `group`. Nodes that do not have the `property` are ignored. See also [call_group()](class_scenetree.md#class_SceneTree_method_call_group) and [notify_group()](class_scenetree.md#class_SceneTree_method_notify_group).

 **Note:** This method acts immediately on all selected nodes at once, which may cause stuttering in some performance-intensive situations.

 **Note:** In C#, `property` must be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in the `PropertyName` class to avoid allocating a new [StringName](class_stringname.md#class_StringName) on each call.

---

<span id="class_SceneTree_method_set_group_flags"></span>

void **set_group_flags** ( call_flags: [int](class_int.md#class_int), group: [StringName](class_stringname.md#class_StringName), property: [String](class_string.md#class_String), value: [Variant](class_variant.md#class_Variant) ) [🔗](class_scenetree.md#class_SceneTree_method_set_group_flags)

Sets the given `property` to `value` on all nodes inside this tree added to the given `group`. Nodes that do not have the `property` are ignored. Use `call_flags` to customize this method's behavior (see [GroupCallFlags](class_scenetree.md#enum_SceneTree_GroupCallFlags)).

 **Note:** In C#, `property` must be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in the `PropertyName` class to avoid allocating a new [StringName](class_stringname.md#class_StringName) on each call.

---

<span id="class_SceneTree_method_set_multiplayer"></span>

void **set_multiplayer** ( multiplayer: [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI), root_path: [NodePath](class_nodepath.md#class_NodePath) = NodePath("") ) [🔗](class_scenetree.md#class_SceneTree_method_set_multiplayer)

Sets a custom [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) with the given `root_path` (controlling also the relative subpaths), or override the default one if `root_path` is empty.

 **Note:** No [MultiplayerAPI](class_multiplayerapi.md#class_MultiplayerAPI) must be configured for the subpath containing `root_path`, nested custom multiplayers are not allowed. I.e. if one is configured for `"/root/Foo"` setting one for `"/root/Foo/Bar"` will cause an error.

 **Note:** [set_multiplayer()](class_scenetree.md#class_SceneTree_method_set_multiplayer) should be called *before* the child nodes are ready at the given `root_path`. If multiplayer nodes like [MultiplayerSpawner](class_multiplayerspawner.md#class_MultiplayerSpawner) or [MultiplayerSynchronizer](class_multiplayersynchronizer.md#class_MultiplayerSynchronizer) are added to the tree before the custom multiplayer API is set, they will not work.

---

<span id="class_SceneTree_method_unload_current_scene"></span>

void **unload_current_scene** ( ) [🔗](class_scenetree.md#class_SceneTree_method_unload_current_scene)

If a current scene is loaded, calling this method will unload it.
