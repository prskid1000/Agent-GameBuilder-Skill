<span id="class_CSGMesh3D"></span>

## CSGMesh3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class_CSGPrimitive3D) **<** [CSGShape3D](class_csgshape3d.md#class_CSGShape3D) **<** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A CSG Mesh shape that uses a mesh resource.

### Description

This CSG node allows you to use any mesh resource as a CSG shape, provided it is *manifold*. A manifold shape is closed, does not self-intersect, does not contain internal faces and has no edges that connect to more than two faces. See also [CSGPolygon3D](class_csgpolygon3d.md#class_CSGPolygon3D) for drawing 2D extruded polygons to be used as CSG nodes.

 **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) with a [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

### Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

### Properties


| [Material](class_material.md#class_Material) | [material](class_csgmesh3d.md#class_CSGMesh3D_property_material) |
| --- | --- |
| [Mesh](class_mesh.md#class_Mesh) | [mesh](class_csgmesh3d.md#class_CSGMesh3D_property_mesh) |

---

### Property Descriptions

<span id="class_CSGMesh3D_property_material"></span>

[Material](class_material.md#class_Material) **material** [🔗](class_csgmesh3d.md#class_CSGMesh3D_property_material)

- void **set_material** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_material** ( )

The [Material](class_material.md#class_Material) used in drawing the CSG shape.

---

<span id="class_CSGMesh3D_property_mesh"></span>

[Mesh](class_mesh.md#class_Mesh) **mesh** [🔗](class_csgmesh3d.md#class_CSGMesh3D_property_mesh)

- void **set_mesh** ( value: [Mesh](class_mesh.md#class_Mesh) )
- [Mesh](class_mesh.md#class_Mesh) **get_mesh** ( )

The [Mesh](class_mesh.md#class_Mesh) resource to use as a CSG shape.

 **Note:** Some [Mesh](class_mesh.md#class_Mesh) types such as [PlaneMesh](class_planemesh.md#class_PlaneMesh), [PointMesh](class_pointmesh.md#class_PointMesh), [QuadMesh](class_quadmesh.md#class_QuadMesh), and [RibbonTrailMesh](class_ribbontrailmesh.md#class_RibbonTrailMesh) are excluded from the type hint for this property, as these primitives are non-*manifold* and thus not compatible with the CSG algorithm.

 **Note:** When using an [ArrayMesh](class_arraymesh.md#class_ArrayMesh), all vertex attributes except [Mesh.ARRAY_VERTEX](class_mesh.md#class_Mesh_constant_ARRAY_VERTEX), [Mesh.ARRAY_NORMAL](class_mesh.md#class_Mesh_constant_ARRAY_NORMAL) and [Mesh.ARRAY_TEX_UV](class_mesh.md#class_Mesh_constant_ARRAY_TEX_UV) are left unused. Only [Mesh.ARRAY_VERTEX](class_mesh.md#class_Mesh_constant_ARRAY_VERTEX) and [Mesh.ARRAY_TEX_UV](class_mesh.md#class_Mesh_constant_ARRAY_TEX_UV) will be passed to the GPU.

 [Mesh.ARRAY_NORMAL](class_mesh.md#class_Mesh_constant_ARRAY_NORMAL) is only used to determine which faces require the use of flat shading. By default, CSGMesh will ignore the mesh's vertex normals, recalculate them for each vertex and use a smooth shader. If a flat shader is required for a face, ensure that all vertex normals of the face are approximately equal.
