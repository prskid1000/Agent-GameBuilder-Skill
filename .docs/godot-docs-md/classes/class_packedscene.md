<span id="class_PackedScene"></span>

## PackedScene

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An abstraction of a serialized scene.

### Description

A simplified interface to a scene file. Provides access to operations and checks that can be performed on the scene resource itself.

Can be used to save a node to a file. When saving, the node as well as all the nodes it owns get saved (see [Node.owner](class_node.md#class_Node_property_owner) property).

 **Note:** The node doesn't need to own itself.

 **Example:** Load a saved scene:

.. tabs::

```
```

    # Use load() instead of preload() if the path isn't known at compile-time.
    var scene = preload("res://scene.tscn").instantiate()
    # Add the node as a child of the node the script is attached to.
    add_child(scene)

```
```

    // C# has no preload, so you have to always use ResourceLoader.Load<PackedScene>().
    var scene = ResourceLoader.Load<PackedScene>("res://scene.tscn").Instantiate();
    // Add the node as a child of the node the script is attached to.
    AddChild(scene);

 **Example:** Save a node with different owners. The following example creates 3 objects: [Node2D](class_node2d.md#class_Node2D) (`node`), [RigidBody2D](class_rigidbody2d.md#class_RigidBody2D) (`body`) and [CollisionObject2D](class_collisionobject2d.md#class_CollisionObject2D) (`collision`). `collision` is a child of `body` which is a child of `node`. Only `body` is owned by `node` and [pack()](class_packedscene.md#class_PackedScene_method_pack) will therefore only save those two nodes, but not `collision`.

.. tabs::

```
```

    # Create the objects.
    var node = Node2D.new()
    var body = RigidBody2D.new()
    var collision = CollisionShape2D.new()

    # Create the object hierarchy.
    body.add_child(collision)
    node.add_child(body)

    # Change owner of `body`, but not of `collision`.
    body.owner = node
    var scene = PackedScene.new()

    # Only `node` and `body` are now packed.
    var result = scene.pack(node)
    if result == OK:
        var error = ResourceSaver.save(scene, "res://path/name.tscn")  # Or "user://..."
        if error != OK:
            push_error("An error occurred while saving the scene to disk.")

```
```

    // Create the objects.
    var node = new Node2D();
    var body = new RigidBody2D();
    var collision = new CollisionShape2D();

    // Create the object hierarchy.
    body.AddChild(collision);
    node.AddChild(body);

    // Change owner of `body`, but not of `collision`.
    body.Owner = node;
    var scene = new PackedScene();

    // Only `node` and `body` are now packed.
    Error result = scene.Pack(node);
    if (result == Error.Ok)
    {
        Error error = ResourceSaver.Save(scene, "res://path/name.tscn"); // Or "user://..."
        if (error != Error.Ok)
        {
            GD.PushError("An error occurred while saving the scene to disk.");
        }
    }

### Tutorials

- 2D Role Playing Game (RPG) Demo

### Methods


| [bool](class_bool.md#class_bool) | [can_instantiate](class_packedscene.md#class_PackedScene_method_can_instantiate) ( ) const |
| --- | --- |
| [SceneState](class_scenestate.md#class_SceneState) | [get_state](class_packedscene.md#class_PackedScene_method_get_state) ( ) const |
| [Node](class_node.md#class_Node) | [instantiate](class_packedscene.md#class_PackedScene_method_instantiate) ( edit_state: [GenEditState](class_packedscene.md#enum_PackedScene_GenEditState) = 0 ) const |
| Error | [pack](class_packedscene.md#class_PackedScene_method_pack) ( path: [Node](class_node.md#class_Node) ) |

---

### Enumerations

<span id="enum_PackedScene_GenEditState"></span>

enum **GenEditState**: [🔗](class_packedscene.md#enum_PackedScene_GenEditState)

<span id="class_PackedScene_constant_GEN_EDIT_STATE_DISABLED"></span>

[GenEditState](class_packedscene.md#enum_PackedScene_GenEditState) **GEN_EDIT_STATE_DISABLED** = `0`

If passed to [instantiate()](class_packedscene.md#class_PackedScene_method_instantiate), blocks edits to the scene state.

<span id="class_PackedScene_constant_GEN_EDIT_STATE_INSTANCE"></span>

[GenEditState](class_packedscene.md#enum_PackedScene_GenEditState) **GEN_EDIT_STATE_INSTANCE** = `1`

If passed to [instantiate()](class_packedscene.md#class_PackedScene_method_instantiate), provides local scene resources to the local scene.

 **Note:** Only available in editor builds.

<span id="class_PackedScene_constant_GEN_EDIT_STATE_MAIN"></span>

[GenEditState](class_packedscene.md#enum_PackedScene_GenEditState) **GEN_EDIT_STATE_MAIN** = `2`

If passed to [instantiate()](class_packedscene.md#class_PackedScene_method_instantiate), provides local scene resources to the local scene. Only the main scene should receive the main edit state.

 **Note:** Only available in editor builds.

<span id="class_PackedScene_constant_GEN_EDIT_STATE_MAIN_INHERITED"></span>

[GenEditState](class_packedscene.md#enum_PackedScene_GenEditState) **GEN_EDIT_STATE_MAIN_INHERITED** = `3`

It's similar to [GEN_EDIT_STATE_MAIN](class_packedscene.md#class_PackedScene_constant_GEN_EDIT_STATE_MAIN), but for the case where the scene is being instantiated to be the base of another one.

 **Note:** Only available in editor builds.

---

### Method Descriptions

<span id="class_PackedScene_method_can_instantiate"></span>

[bool](class_bool.md#class_bool) **can_instantiate** ( ) *const* [🔗](class_packedscene.md#class_PackedScene_method_can_instantiate)

Returns `true` if the scene file has nodes.

---

<span id="class_PackedScene_method_get_state"></span>

[SceneState](class_scenestate.md#class_SceneState) **get_state** ( ) *const* [🔗](class_packedscene.md#class_PackedScene_method_get_state)

Returns the [SceneState](class_scenestate.md#class_SceneState) representing the scene file contents.

---

<span id="class_PackedScene_method_instantiate"></span>

[Node](class_node.md#class_Node) **instantiate** ( edit_state: [GenEditState](class_packedscene.md#enum_PackedScene_GenEditState) = 0 ) *const* [🔗](class_packedscene.md#class_PackedScene_method_instantiate)

Instantiates the scene's node hierarchy. Triggers child scene instantiation(s). Triggers a [Node.NOTIFICATION_SCENE_INSTANTIATED](class_node.md#class_Node_constant_NOTIFICATION_SCENE_INSTANTIATED) notification on the root node.

---

<span id="class_PackedScene_method_pack"></span>

Error **pack** ( path: [Node](class_node.md#class_Node) ) [🔗](class_packedscene.md#class_PackedScene_method_pack)

Packs the `path` node, and all owned sub-nodes, into this **PackedScene**. Any existing data will be cleared. See [Node.owner](class_node.md#class_Node_property_owner).
