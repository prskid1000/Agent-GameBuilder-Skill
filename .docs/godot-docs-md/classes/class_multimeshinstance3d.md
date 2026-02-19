.. meta::
	:keywords: batch

<span id="class_MultiMeshInstance3D"></span>

## MultiMeshInstance3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Node that instances a [MultiMesh](class_multimesh.md#class_MultiMesh).

### Description

**MultiMeshInstance3D** is a specialized node to instance [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) s based on a [MultiMesh](class_multimesh.md#class_MultiMesh) resource.

This is useful to optimize the rendering of a high number of instances of a given mesh (for example trees in a forest or grass strands).

### Tutorials

- [Using MultiMeshInstance](../tutorials/3d/using_multi_mesh_instance.md)

- [Optimization using MultiMeshes](../tutorials/performance/using_multimesh.md)

- [Animating thousands of fish with MultiMeshInstance](../tutorials/performance/vertex_animation/animating_thousands_of_fish.md)

### Properties


| [MultiMesh](class_multimesh.md#class_MultiMesh) | [multimesh](class_multimeshinstance3d.md#class_MultiMeshInstance3D_property_multimesh) |
| --- | --- |

---

### Property Descriptions

<span id="class_MultiMeshInstance3D_property_multimesh"></span>

[MultiMesh](class_multimesh.md#class_MultiMesh) **multimesh** [🔗](class_multimeshinstance3d.md#class_MultiMeshInstance3D_property_multimesh)

- void **set_multimesh** ( value: [MultiMesh](class_multimesh.md#class_MultiMesh) )
- [MultiMesh](class_multimesh.md#class_MultiMesh) **get_multimesh** ( )

The [MultiMesh](class_multimesh.md#class_MultiMesh) resource that will be used and shared among all instances of the **MultiMeshInstance3D**.
