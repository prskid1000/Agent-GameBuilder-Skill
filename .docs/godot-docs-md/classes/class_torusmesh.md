<span id="class_TorusMesh"></span>

## TorusMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Class representing a torus [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Description

Class representing a torus [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Properties


| [float](class_float.md#class_float) | [inner_radius](class_torusmesh.md#class_TorusMesh_property_inner_radius) | `0.5` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [outer_radius](class_torusmesh.md#class_TorusMesh_property_outer_radius) | `1.0` |
| [int](class_int.md#class_int) | [ring_segments](class_torusmesh.md#class_TorusMesh_property_ring_segments) | `32` |
| [int](class_int.md#class_int) | [rings](class_torusmesh.md#class_TorusMesh_property_rings) | `64` |

---

### Property Descriptions

<span id="class_TorusMesh_property_inner_radius"></span>

[float](class_float.md#class_float) **inner_radius** = `0.5` [🔗](class_torusmesh.md#class_TorusMesh_property_inner_radius)

- void **set_inner_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_inner_radius** ( )

The inner radius of the torus.

---

<span id="class_TorusMesh_property_outer_radius"></span>

[float](class_float.md#class_float) **outer_radius** = `1.0` [🔗](class_torusmesh.md#class_TorusMesh_property_outer_radius)

- void **set_outer_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_outer_radius** ( )

The outer radius of the torus.

---

<span id="class_TorusMesh_property_ring_segments"></span>

[int](class_int.md#class_int) **ring_segments** = `32` [🔗](class_torusmesh.md#class_TorusMesh_property_ring_segments)

- void **set_ring_segments** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_ring_segments** ( )

The number of edges each ring of the torus is constructed of.

---

<span id="class_TorusMesh_property_rings"></span>

[int](class_int.md#class_int) **rings** = `64` [🔗](class_torusmesh.md#class_TorusMesh_property_rings)

- void **set_rings** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_rings** ( )

The number of slices the torus is constructed of.
