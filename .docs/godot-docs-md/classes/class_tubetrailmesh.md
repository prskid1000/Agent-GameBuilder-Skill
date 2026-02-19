<span id="class_TubeTrailMesh"></span>

## TubeTrailMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a straight tube-shaped [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) with variable width.

### Description

**TubeTrailMesh** represents a straight tube-shaped mesh with variable width. The tube is composed of a number of cylindrical sections, each with the same [section_length](class_tubetrailmesh.md#class_TubeTrailMesh_property_section_length) and number of [section_rings](class_tubetrailmesh.md#class_TubeTrailMesh_property_section_rings). A [curve](class_tubetrailmesh.md#class_TubeTrailMesh_property_curve) is sampled along the total length of the tube, meaning that the curve determines the radius of the tube along its length.

This primitive mesh is usually used for particle trails.

### Tutorials

- [3D Particle trails](../tutorials/3d/particles/trails.md)

- [Particle systems (3D)](../tutorials/3d/particles/index.md)

### Properties


| [bool](class_bool.md#class_bool) | [cap_bottom](class_tubetrailmesh.md#class_TubeTrailMesh_property_cap_bottom) | `true` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [cap_top](class_tubetrailmesh.md#class_TubeTrailMesh_property_cap_top) | `true` |
| [Curve](class_curve.md#class_Curve) | [curve](class_tubetrailmesh.md#class_TubeTrailMesh_property_curve) |
| [int](class_int.md#class_int) | [radial_steps](class_tubetrailmesh.md#class_TubeTrailMesh_property_radial_steps) | `8` |
| [float](class_float.md#class_float) | [radius](class_tubetrailmesh.md#class_TubeTrailMesh_property_radius) | `0.5` |
| [float](class_float.md#class_float) | [section_length](class_tubetrailmesh.md#class_TubeTrailMesh_property_section_length) | `0.2` |
| [int](class_int.md#class_int) | [section_rings](class_tubetrailmesh.md#class_TubeTrailMesh_property_section_rings) | `3` |
| [int](class_int.md#class_int) | [sections](class_tubetrailmesh.md#class_TubeTrailMesh_property_sections) | `5` |

---

### Property Descriptions

<span id="class_TubeTrailMesh_property_cap_bottom"></span>

[bool](class_bool.md#class_bool) **cap_bottom** = `true` [🔗](class_tubetrailmesh.md#class_TubeTrailMesh_property_cap_bottom)

- void **set_cap_bottom** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_cap_bottom** ( )

If `true`, generates a cap at the bottom of the tube. This can be set to `false` to speed up generation and rendering when the cap is never seen by the camera.

---

<span id="class_TubeTrailMesh_property_cap_top"></span>

[bool](class_bool.md#class_bool) **cap_top** = `true` [🔗](class_tubetrailmesh.md#class_TubeTrailMesh_property_cap_top)

- void **set_cap_top** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_cap_top** ( )

If `true`, generates a cap at the top of the tube. This can be set to `false` to speed up generation and rendering when the cap is never seen by the camera.

---

<span id="class_TubeTrailMesh_property_curve"></span>

[Curve](class_curve.md#class_Curve) **curve** [🔗](class_tubetrailmesh.md#class_TubeTrailMesh_property_curve)

- void **set_curve** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_curve** ( )

Determines the radius of the tube along its length. The radius of a particular section ring is obtained by multiplying the baseline [radius](class_tubetrailmesh.md#class_TubeTrailMesh_property_radius) by the value of this curve at the given distance. For values smaller than `0`, the faces will be inverted. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_TubeTrailMesh_property_radial_steps"></span>

[int](class_int.md#class_int) **radial_steps** = `8` [🔗](class_tubetrailmesh.md#class_TubeTrailMesh_property_radial_steps)

- void **set_radial_steps** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_radial_steps** ( )

The number of sides on the tube. For example, a value of `5` means the tube will be pentagonal. Higher values result in a more detailed tube at the cost of performance.

---

<span id="class_TubeTrailMesh_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.5` [🔗](class_tubetrailmesh.md#class_TubeTrailMesh_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The baseline radius of the tube. The radius of a particular section ring is obtained by multiplying this radius by the value of the [curve](class_tubetrailmesh.md#class_TubeTrailMesh_property_curve) at the given distance.

---

<span id="class_TubeTrailMesh_property_section_length"></span>

[float](class_float.md#class_float) **section_length** = `0.2` [🔗](class_tubetrailmesh.md#class_TubeTrailMesh_property_section_length)

- void **set_section_length** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_section_length** ( )

The length of a section of the tube.

---

<span id="class_TubeTrailMesh_property_section_rings"></span>

[int](class_int.md#class_int) **section_rings** = `3` [🔗](class_tubetrailmesh.md#class_TubeTrailMesh_property_section_rings)

- void **set_section_rings** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_section_rings** ( )

The number of rings in a section. The [curve](class_tubetrailmesh.md#class_TubeTrailMesh_property_curve) is sampled on each ring to determine its radius. Higher values result in a more detailed tube at the cost of performance.

---

<span id="class_TubeTrailMesh_property_sections"></span>

[int](class_int.md#class_int) **sections** = `5` [🔗](class_tubetrailmesh.md#class_TubeTrailMesh_property_sections)

- void **set_sections** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_sections** ( )

The total number of sections on the tube.
