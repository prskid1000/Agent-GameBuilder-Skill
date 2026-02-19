<span id="class_SphereMesh"></span>

## SphereMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Class representing a spherical [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Description

Class representing a spherical [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Properties


| [float](class_float.md#class_float) | [height](class_spheremesh.md#class_SphereMesh_property_height) | `1.0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [is_hemisphere](class_spheremesh.md#class_SphereMesh_property_is_hemisphere) | `false` |
| [int](class_int.md#class_int) | [radial_segments](class_spheremesh.md#class_SphereMesh_property_radial_segments) | `64` |
| [float](class_float.md#class_float) | [radius](class_spheremesh.md#class_SphereMesh_property_radius) | `0.5` |
| [int](class_int.md#class_int) | [rings](class_spheremesh.md#class_SphereMesh_property_rings) | `32` |

---

### Property Descriptions

<span id="class_SphereMesh_property_height"></span>

[float](class_float.md#class_float) **height** = `1.0` [🔗](class_spheremesh.md#class_SphereMesh_property_height)

- void **set_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height** ( )

Full height of the sphere.

---

<span id="class_SphereMesh_property_is_hemisphere"></span>

[bool](class_bool.md#class_bool) **is_hemisphere** = `false` [🔗](class_spheremesh.md#class_SphereMesh_property_is_hemisphere)

- void **set_is_hemisphere** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_is_hemisphere** ( )

If `true`, a hemisphere is created rather than a full sphere.

 **Note:** To get a regular hemisphere, the height and radius of the sphere must be equal.

---

<span id="class_SphereMesh_property_radial_segments"></span>

[int](class_int.md#class_int) **radial_segments** = `64` [🔗](class_spheremesh.md#class_SphereMesh_property_radial_segments)

- void **set_radial_segments** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_radial_segments** ( )

Number of radial segments on the sphere.

---

<span id="class_SphereMesh_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.5` [🔗](class_spheremesh.md#class_SphereMesh_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

Radius of sphere.

---

<span id="class_SphereMesh_property_rings"></span>

[int](class_int.md#class_int) **rings** = `32` [🔗](class_spheremesh.md#class_SphereMesh_property_rings)

- void **set_rings** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_rings** ( )

Number of segments along the height of the sphere.
