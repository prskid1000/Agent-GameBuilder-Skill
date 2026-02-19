<span id="class_RemoteTransform2D"></span>

## RemoteTransform2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

RemoteTransform2D pushes its own [Transform2D](class_transform2d.md#class_Transform2D) to another [Node2D](class_node2d.md#class_Node2D) derived node in the scene.

### Description

RemoteTransform2D pushes its own [Transform2D](class_transform2d.md#class_Transform2D) to another [Node2D](class_node2d.md#class_Node2D) derived node (called the remote node) in the scene.

It can be set to update another node's position, rotation and/or scale. It can use either global or local coordinates.

### Properties


| [NodePath](class_nodepath.md#class_NodePath) | [remote_path](class_remotetransform2d.md#class_RemoteTransform2D_property_remote_path) | `NodePath("")` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [update_position](class_remotetransform2d.md#class_RemoteTransform2D_property_update_position) | `true` |
| [bool](class_bool.md#class_bool) | [update_rotation](class_remotetransform2d.md#class_RemoteTransform2D_property_update_rotation) | `true` |
| [bool](class_bool.md#class_bool) | [update_scale](class_remotetransform2d.md#class_RemoteTransform2D_property_update_scale) | `true` |
| [bool](class_bool.md#class_bool) | [use_global_coordinates](class_remotetransform2d.md#class_RemoteTransform2D_property_use_global_coordinates) | `true` |

### Methods


| void | [force_update_cache](class_remotetransform2d.md#class_RemoteTransform2D_method_force_update_cache) ( ) |
| --- | --- |

---

### Property Descriptions

<span id="class_RemoteTransform2D_property_remote_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **remote_path** = `NodePath("")` [🔗](class_remotetransform2d.md#class_RemoteTransform2D_property_remote_path)

- void **set_remote_node** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_remote_node** ( )

The [NodePath](class_nodepath.md#class_NodePath) to the remote node, relative to the RemoteTransform2D's position in the scene.

---

<span id="class_RemoteTransform2D_property_update_position"></span>

[bool](class_bool.md#class_bool) **update_position** = `true` [🔗](class_remotetransform2d.md#class_RemoteTransform2D_property_update_position)

- void **set_update_position** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_update_position** ( )

If `true`, the remote node's position is updated.

---

<span id="class_RemoteTransform2D_property_update_rotation"></span>

[bool](class_bool.md#class_bool) **update_rotation** = `true` [🔗](class_remotetransform2d.md#class_RemoteTransform2D_property_update_rotation)

- void **set_update_rotation** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_update_rotation** ( )

If `true`, the remote node's rotation is updated.

---

<span id="class_RemoteTransform2D_property_update_scale"></span>

[bool](class_bool.md#class_bool) **update_scale** = `true` [🔗](class_remotetransform2d.md#class_RemoteTransform2D_property_update_scale)

- void **set_update_scale** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_update_scale** ( )

If `true`, the remote node's scale is updated.

---

<span id="class_RemoteTransform2D_property_use_global_coordinates"></span>

[bool](class_bool.md#class_bool) **use_global_coordinates** = `true` [🔗](class_remotetransform2d.md#class_RemoteTransform2D_property_use_global_coordinates)

- void **set_use_global_coordinates** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_use_global_coordinates** ( )

If `true`, global coordinates are used. If `false`, local coordinates are used.

---

### Method Descriptions

<span id="class_RemoteTransform2D_method_force_update_cache"></span>

void **force_update_cache** ( ) [🔗](class_remotetransform2d.md#class_RemoteTransform2D_method_force_update_cache)

**RemoteTransform2D** caches the remote node. It may not notice if the remote node disappears; [force_update_cache()](class_remotetransform2d.md#class_RemoteTransform2D_method_force_update_cache) forces it to update the cache again.
