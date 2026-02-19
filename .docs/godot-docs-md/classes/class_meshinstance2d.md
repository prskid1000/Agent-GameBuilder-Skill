<span id="class_MeshInstance2D"></span>

## MeshInstance2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Node used for displaying a [Mesh](class_mesh.md#class_Mesh) in 2D.

### Description

Node used for displaying a [Mesh](class_mesh.md#class_Mesh) in 2D. This can be faster to render compared to displaying a [Sprite2D](class_sprite2d.md#class_Sprite2D) node with large transparent areas, especially if the node takes up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprite's opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

When a [Mesh](class_mesh.md#class_Mesh) has to be instantiated more than thousands of times close to each other, consider using a [MultiMesh](class_multimesh.md#class_MultiMesh) in a [MultiMeshInstance2D](class_multimeshinstance2d.md#class_MultiMeshInstance2D) instead.

A **MeshInstance2D** can be created from an existing [Sprite2D](class_sprite2d.md#class_Sprite2D) via a tool in the editor toolbar. Select the [Sprite2D](class_sprite2d.md#class_Sprite2D) node, then choose **Sprite2D > Convert to MeshInstance2D** at the top of the 2D editor viewport.

### Tutorials

- [2D meshes](../tutorials/2d/2d_meshes.md)

### Properties


| [Mesh](class_mesh.md#class_Mesh) | [mesh](class_meshinstance2d.md#class_MeshInstance2D_property_mesh) |
| --- | --- |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_meshinstance2d.md#class_MeshInstance2D_property_texture) |

---

### Signals

<span id="class_MeshInstance2D_signal_texture_changed"></span>

**texture_changed** ( ) [🔗](class_meshinstance2d.md#class_MeshInstance2D_signal_texture_changed)

Emitted when the [texture](class_meshinstance2d.md#class_MeshInstance2D_property_texture) is changed.

---

### Property Descriptions

<span id="class_MeshInstance2D_property_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **mesh** [🔗](class_meshinstance2d.md#class_MeshInstance2D_property_mesh)

- void **set_mesh** ( value: [Mesh](class_mesh.md#class_Mesh) )
- [Mesh](class_mesh.md#class_Mesh) **get_mesh** ( )

The [Mesh](class_mesh.md#class_Mesh) that will be drawn by the **MeshInstance2D**.

---

<span id="class_MeshInstance2D_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_meshinstance2d.md#class_MeshInstance2D_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

The [Texture2D](class_texture2d.md#class_Texture2D) that will be used if using the default [CanvasItemMaterial](class_canvasitemmaterial.md#class_CanvasItemMaterial). Can be accessed as `TEXTURE` in CanvasItem shader.
