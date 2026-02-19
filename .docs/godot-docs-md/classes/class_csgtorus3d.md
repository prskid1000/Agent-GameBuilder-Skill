<span id="class_CSGTorus3D"></span>

## CSGTorus3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class_CSGPrimitive3D) **<** [CSGShape3D](class_csgshape3d.md#class_CSGShape3D) **<** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A CSG Torus shape.

### Description

This node allows you to create a torus for use with the CSG system.

 **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) with a [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

### Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

### Properties


| [float](class_float.md#class_float) | [inner_radius](class_csgtorus3d.md#class_CSGTorus3D_property_inner_radius) | `0.5` |
| --- | --- | --- |
| [Material](class_material.md#class_Material) | [material](class_csgtorus3d.md#class_CSGTorus3D_property_material) |
| [float](class_float.md#class_float) | [outer_radius](class_csgtorus3d.md#class_CSGTorus3D_property_outer_radius) | `1.0` |
| [int](class_int.md#class_int) | [ring_sides](class_csgtorus3d.md#class_CSGTorus3D_property_ring_sides) | `6` |
| [int](class_int.md#class_int) | [sides](class_csgtorus3d.md#class_CSGTorus3D_property_sides) | `8` |
| [bool](class_bool.md#class_bool) | [smooth_faces](class_csgtorus3d.md#class_CSGTorus3D_property_smooth_faces) | `true` |

---

### Property Descriptions

<span id="class_CSGTorus3D_property_inner_radius"></span>

[float](class_float.md#class_float) **inner_radius** = `0.5` [🔗](class_csgtorus3d.md#class_CSGTorus3D_property_inner_radius)

- void **set_inner_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_inner_radius** ( )

The inner radius of the torus.

---

<span id="class_CSGTorus3D_property_material"></span>

[Material](class_material.md#class_Material) **material** [🔗](class_csgtorus3d.md#class_CSGTorus3D_property_material)

- void **set_material** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_material** ( )

The material used to render the torus.

---

<span id="class_CSGTorus3D_property_outer_radius"></span>

[float](class_float.md#class_float) **outer_radius** = `1.0` [🔗](class_csgtorus3d.md#class_CSGTorus3D_property_outer_radius)

- void **set_outer_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_outer_radius** ( )

The outer radius of the torus.

---

<span id="class_CSGTorus3D_property_ring_sides"></span>

[int](class_int.md#class_int) **ring_sides** = `6` [🔗](class_csgtorus3d.md#class_CSGTorus3D_property_ring_sides)

- void **set_ring_sides** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_ring_sides** ( )

The number of edges each ring of the torus is constructed of.

---

<span id="class_CSGTorus3D_property_sides"></span>

[int](class_int.md#class_int) **sides** = `8` [🔗](class_csgtorus3d.md#class_CSGTorus3D_property_sides)

- void **set_sides** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sides** ( )

The number of slices the torus is constructed of.

---

<span id="class_CSGTorus3D_property_smooth_faces"></span>

[bool](class_bool.md#class_bool) **smooth_faces** = `true` [🔗](class_csgtorus3d.md#class_CSGTorus3D_property_smooth_faces)

- void **set_smooth_faces** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_smooth_faces** ( )

If `true` the normals of the torus are set to give a smooth effect making the torus seem rounded. If `false` the torus will have a flat shaded look.
