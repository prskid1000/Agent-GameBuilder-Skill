<span id="class_CSGSphere3D"></span>

## CSGSphere3D

**Inherits:** [CSGPrimitive3D](class_csgprimitive3d.md#class_CSGPrimitive3D) **<** [CSGShape3D](class_csgshape3d.md#class_CSGShape3D) **<** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A CSG Sphere shape.

### Description

This node allows you to create a sphere for use with the CSG system.

 **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) with a [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh). Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

### Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

### Properties


| [Material](class_material.md#class_Material) | [material](class_csgsphere3d.md#class_CSGSphere3D_property_material) |
| --- | --- |
| [int](class_int.md#class_int) | [radial_segments](class_csgsphere3d.md#class_CSGSphere3D_property_radial_segments) | `12` |
| [float](class_float.md#class_float) | [radius](class_csgsphere3d.md#class_CSGSphere3D_property_radius) | `0.5` |
| [int](class_int.md#class_int) | [rings](class_csgsphere3d.md#class_CSGSphere3D_property_rings) | `6` |
| [bool](class_bool.md#class_bool) | [smooth_faces](class_csgsphere3d.md#class_CSGSphere3D_property_smooth_faces) | `true` |

---

### Property Descriptions

<span id="class_CSGSphere3D_property_material"></span>

[Material](class_material.md#class_Material) **material** [🔗](class_csgsphere3d.md#class_CSGSphere3D_property_material)

- void **set_material** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_material** ( )

The material used to render the sphere.

---

<span id="class_CSGSphere3D_property_radial_segments"></span>

[int](class_int.md#class_int) **radial_segments** = `12` [🔗](class_csgsphere3d.md#class_CSGSphere3D_property_radial_segments)

- void **set_radial_segments** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_radial_segments** ( )

Number of vertical slices for the sphere.

---

<span id="class_CSGSphere3D_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.5` [🔗](class_csgsphere3d.md#class_CSGSphere3D_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

Radius of the sphere.

---

<span id="class_CSGSphere3D_property_rings"></span>

[int](class_int.md#class_int) **rings** = `6` [🔗](class_csgsphere3d.md#class_CSGSphere3D_property_rings)

- void **set_rings** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_rings** ( )

Number of horizontal slices for the sphere.

---

<span id="class_CSGSphere3D_property_smooth_faces"></span>

[bool](class_bool.md#class_bool) **smooth_faces** = `true` [🔗](class_csgsphere3d.md#class_CSGSphere3D_property_smooth_faces)

- void **set_smooth_faces** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_smooth_faces** ( )

If `true` the normals of the sphere are set to give a smooth effect making the sphere seem rounded. If `false` the sphere will have a flat shaded look.
