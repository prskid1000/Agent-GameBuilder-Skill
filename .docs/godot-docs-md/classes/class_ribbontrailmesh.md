<span id="class_RibbonTrailMesh"></span>

## RibbonTrailMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a straight ribbon-shaped [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) with variable width.

### Description

**RibbonTrailMesh** represents a straight ribbon-shaped mesh with variable width. The ribbon is composed of a number of flat or cross-shaped sections, each with the same [section_length](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_section_length) and number of [section_segments](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_section_segments). A [curve](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_curve) is sampled along the total length of the ribbon, meaning that the curve determines the size of the ribbon along its length.

This primitive mesh is usually used for particle trails.

### Tutorials

- [3D Particle trails](../tutorials/3d/particles/trails.md)

- [Particle systems (3D)](../tutorials/3d/particles/index.md)

### Properties


| [Curve](class_curve.md#class_Curve) | [curve](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_curve) |
| --- | --- |
| [float](class_float.md#class_float) | [section_length](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_section_length) | `0.2` |
| [int](class_int.md#class_int) | [section_segments](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_section_segments) | `3` |
| [int](class_int.md#class_int) | [sections](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_sections) | `5` |
| [Shape](class_ribbontrailmesh.md#enum_RibbonTrailMesh_Shape) | [shape](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_shape) | `1` |
| [float](class_float.md#class_float) | [size](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_size) | `1.0` |

---

### Enumerations

<span id="enum_RibbonTrailMesh_Shape"></span>

enum **Shape**: [🔗](class_ribbontrailmesh.md#enum_RibbonTrailMesh_Shape)

<span id="class_RibbonTrailMesh_constant_SHAPE_FLAT"></span>

[Shape](class_ribbontrailmesh.md#enum_RibbonTrailMesh_Shape) **SHAPE_FLAT** = `0`

Gives the mesh a single flat face.

<span id="class_RibbonTrailMesh_constant_SHAPE_CROSS"></span>

[Shape](class_ribbontrailmesh.md#enum_RibbonTrailMesh_Shape) **SHAPE_CROSS** = `1`

Gives the mesh two perpendicular flat faces, making a cross shape.

---

### Property Descriptions

<span id="class_RibbonTrailMesh_property_curve"></span>

[Curve](class_curve.md#class_Curve) **curve** [🔗](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_curve)

- void **set_curve** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_curve** ( )

Determines the size of the ribbon along its length. The size of a particular section segment is obtained by multiplying the baseline [size](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_size) by the value of this curve at the given distance. For values smaller than `0`, the faces will be inverted. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_RibbonTrailMesh_property_section_length"></span>

[float](class_float.md#class_float) **section_length** = `0.2` [🔗](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_section_length)

- void **set_section_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_section_length** ( )

The length of a section of the ribbon.

---

<span id="class_RibbonTrailMesh_property_section_segments"></span>

[int](class_int.md#class_int) **section_segments** = `3` [🔗](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_section_segments)

- void **set_section_segments** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_section_segments** ( )

The number of segments in a section. The [curve](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_curve) is sampled on each segment to determine its size. Higher values result in a more detailed ribbon at the cost of performance.

---

<span id="class_RibbonTrailMesh_property_sections"></span>

[int](class_int.md#class_int) **sections** = `5` [🔗](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_sections)

- void **set_sections** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sections** ( )

The total number of sections on the ribbon.

---

<span id="class_RibbonTrailMesh_property_shape"></span>

[Shape](class_ribbontrailmesh.md#enum_RibbonTrailMesh_Shape) **shape** = `1` [🔗](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_shape)

- void **set_shape** ( value: [Shape](class_ribbontrailmesh.md#enum_RibbonTrailMesh_Shape) )
- [Shape](class_ribbontrailmesh.md#enum_RibbonTrailMesh_Shape) **get_shape** ( )

Determines the shape of the ribbon.

---

<span id="class_RibbonTrailMesh_property_size"></span>

[float](class_float.md#class_float) **size** = `1.0` [🔗](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_size)

- void **set_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_size** ( )

The baseline size of the ribbon. The size of a particular section segment is obtained by multiplying this size by the value of the [curve](class_ribbontrailmesh.md#class_RibbonTrailMesh_property_curve) at the given distance.
