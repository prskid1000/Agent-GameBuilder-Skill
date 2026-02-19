.. meta::
	:keywords: batch

<span id="class_MultiMeshInstance2D"></span>

## MultiMeshInstance2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Node that instances a [MultiMesh](class_multimesh.md#class_MultiMesh) in 2D.

### Description

**MultiMeshInstance2D** is a specialized node to instance a [MultiMesh](class_multimesh.md#class_MultiMesh) resource in 2D. This can be faster to render compared to displaying many [Sprite2D](class_sprite2d.md#class_Sprite2D) nodes with large transparent areas, especially if the nodes take up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprites' opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

Usage is the same as [MultiMeshInstance3D](class_multimeshinstance3d.md#class_MultiMeshInstance3D).

### Properties


| [MultiMesh](class_multimesh.md#class_MultiMesh) | [multimesh](class_multimeshinstance2d.md#class_MultiMeshInstance2D_property_multimesh) |
| --- | --- |
| [Texture2D](class_texture2d.md#class_Texture2D) | [texture](class_multimeshinstance2d.md#class_MultiMeshInstance2D_property_texture) |

---

### Signals

<span id="class_MultiMeshInstance2D_signal_texture_changed"></span>

**texture_changed** ( ) [🔗](class_multimeshinstance2d.md#class_MultiMeshInstance2D_signal_texture_changed)

Emitted when the [texture](class_multimeshinstance2d.md#class_MultiMeshInstance2D_property_texture) is changed.

---

### Property Descriptions

<span id="class_MultiMeshInstance2D_property_multimesh"></span>

[MultiMesh](class_multimesh.md#class_MultiMesh) **multimesh** [🔗](class_multimeshinstance2d.md#class_MultiMeshInstance2D_property_multimesh)

- void **set_multimesh** ( value: [MultiMesh](class_multimesh.md#class_MultiMesh) )
- [MultiMesh](class_multimesh.md#class_MultiMesh) **get_multimesh** ( )

The [MultiMesh](class_multimesh.md#class_MultiMesh) that will be drawn by the **MultiMeshInstance2D**.

---

<span id="class_MultiMeshInstance2D_property_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **texture** [🔗](class_multimeshinstance2d.md#class_MultiMeshInstance2D_property_texture)

- void **set_texture** ( value: [Texture2D](class_texture2d.md#class_Texture2D) )
- [Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( )

The [Texture2D](class_texture2d.md#class_Texture2D) that will be used if using the default [CanvasItemMaterial](class_canvasitemmaterial.md#class_CanvasItemMaterial). Can be accessed as `TEXTURE` in CanvasItem shader.
