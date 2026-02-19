<span id="class_CSGCylinder3D"></span>

## CSGCylinder3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class_CSGPrimitive3D) **<** [CSGShape3D](class_csgshape3d.md#class_CSGShape3D) **<** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A CSG Cylinder shape.

### Description

This node allows you to create a cylinder (or cone) for use with the CSG system.

 **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) with a [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

### Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

### Properties


| [bool](class_bool.md#class_bool) | [cone](class_csgcylinder3d.md#class_CSGCylinder3D_property_cone) | `false` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [height](class_csgcylinder3d.md#class_CSGCylinder3D_property_height) | `2.0` |
| [Material](class_material.md#class_Material) | [material](class_csgcylinder3d.md#class_CSGCylinder3D_property_material) |
| [float](class_float.md#class_float) | [radius](class_csgcylinder3d.md#class_CSGCylinder3D_property_radius) | `0.5` |
| [int](class_int.md#class_int) | [sides](class_csgcylinder3d.md#class_CSGCylinder3D_property_sides) | `8` |
| [bool](class_bool.md#class_bool) | [smooth_faces](class_csgcylinder3d.md#class_CSGCylinder3D_property_smooth_faces) | `true` |

---

### Property Descriptions

<span id="class_CSGCylinder3D_property_cone"></span>

[bool](class_bool.md#class_bool) **cone** = `false` [🔗](class_csgcylinder3d.md#class_CSGCylinder3D_property_cone)

- void **set_cone** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_cone** ( )

If `true` a cone is created, the [radius](class_csgcylinder3d.md#class_CSGCylinder3D_property_radius) will only apply to one side.

---

<span id="class_CSGCylinder3D_property_height"></span>

[float](class_float.md#class_float) **height** = `2.0` [🔗](class_csgcylinder3d.md#class_CSGCylinder3D_property_height)

- void **set_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height** ( )

The height of the cylinder.

---

<span id="class_CSGCylinder3D_property_material"></span>

[Material](class_material.md#class_Material) **material** [🔗](class_csgcylinder3d.md#class_CSGCylinder3D_property_material)

- void **set_material** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_material** ( )

The material used to render the cylinder.

---

<span id="class_CSGCylinder3D_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.5` [🔗](class_csgcylinder3d.md#class_CSGCylinder3D_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The radius of the cylinder.

---

<span id="class_CSGCylinder3D_property_sides"></span>

[int](class_int.md#class_int) **sides** = `8` [🔗](class_csgcylinder3d.md#class_CSGCylinder3D_property_sides)

- void **set_sides** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sides** ( )

The number of sides of the cylinder, the higher this number the more detail there will be in the cylinder.

---

<span id="class_CSGCylinder3D_property_smooth_faces"></span>

[bool](class_bool.md#class_bool) **smooth_faces** = `true` [🔗](class_csgcylinder3d.md#class_CSGCylinder3D_property_smooth_faces)

- void **set_smooth_faces** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_smooth_faces** ( )

If `true` the normals of the cylinder are set to give a smooth effect making the cylinder seem rounded. If `false` the cylinder will have a flat shaded look.
