<span id="class_CSGPrimitive3D"></span>

## CSGPrimitive3D

**Inherits:** [CSGShape3D](class_csgshape3d.md#class_CSGShape3D) **<** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CSGBox3D](class_csgbox3d.md#class_CSGBox3D), [CSGCylinder3D](class_csgcylinder3d.md#class_CSGCylinder3D), [CSGMesh3D](class_csgmesh3d.md#class_CSGMesh3D), [CSGPolygon3D](class_csgpolygon3d.md#class_CSGPolygon3D), [CSGSphere3D](class_csgsphere3d.md#class_CSGSphere3D), [CSGTorus3D](class_csgtorus3d.md#class_CSGTorus3D)

Base class for CSG primitives.

### Description

Parent class for various CSG primitives. It contains code and functionality that is common between them. It cannot be used directly. Instead use one of the various classes that inherit from it.

 **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) with a [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

### Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

### Properties


| [bool](class_bool.md#class_bool) | [flip_faces](class_csgprimitive3d.md#class_CSGPrimitive3D_property_flip_faces) | `false` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_CSGPrimitive3D_property_flip_faces"></span>

[bool](class_bool.md#class_bool) **flip_faces** = `false` [🔗](class_csgprimitive3d.md#class_CSGPrimitive3D_property_flip_faces)

- void **set_flip_faces** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flip_faces** ( )

If set, the order of the vertices in each triangle are reversed resulting in the backside of the mesh being drawn.
