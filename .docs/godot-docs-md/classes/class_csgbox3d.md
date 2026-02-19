<span id="class_CSGBox3D"></span>

## CSGBox3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class_CSGPrimitive3D) **<** [CSGShape3D](class_csgshape3d.md#class_CSGShape3D) **<** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A CSG Box shape.

### Description

This node allows you to create a box for use with the CSG system.

 **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) with a [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

### Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

### Properties


| [Material](class_material.md#class_Material) | [material](class_csgbox3d.md#class_CSGBox3D_property_material) |
| --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [size](class_csgbox3d.md#class_CSGBox3D_property_size) | `Vector3(1, 1, 1)` |

---

### Property Descriptions

<span id="class_CSGBox3D_property_material"></span>

[Material](class_material.md#class_Material) **material** [🔗](class_csgbox3d.md#class_CSGBox3D_property_material)

- void **set_material** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_material** ( )

The material used to render the box.

---

<span id="class_CSGBox3D_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_csgbox3d.md#class_CSGBox3D_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The box's width, height and depth.
