<span id="class_CapsuleMesh"></span>

## CapsuleMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Class representing a capsule-shaped [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Description

Class representing a capsule-shaped [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Properties


| [float](class_float.md#class_float) | [height](class_capsulemesh.md#class_CapsuleMesh_property_height) | `2.0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [radial_segments](class_capsulemesh.md#class_CapsuleMesh_property_radial_segments) | `64` |
| [float](class_float.md#class_float) | [radius](class_capsulemesh.md#class_CapsuleMesh_property_radius) | `0.5` |
| [int](class_int.md#class_int) | [rings](class_capsulemesh.md#class_CapsuleMesh_property_rings) | `8` |

---

### Property Descriptions

<span id="class_CapsuleMesh_property_height"></span>

[float](class_float.md#class_float) **height** = `2.0` [🔗](class_capsulemesh.md#class_CapsuleMesh_property_height)

- void **set_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height** ( )

Total height of the capsule mesh (including the hemispherical ends).

 **Note:** The [height](class_capsulemesh.md#class_CapsuleMesh_property_height) of a capsule must be at least twice its [radius](class_capsulemesh.md#class_CapsuleMesh_property_radius). Otherwise, the capsule becomes a circle. If the [height](class_capsulemesh.md#class_CapsuleMesh_property_height) is less than twice the [radius](class_capsulemesh.md#class_CapsuleMesh_property_radius), the properties adjust to a valid value.

---

<span id="class_CapsuleMesh_property_radial_segments"></span>

[int](class_int.md#class_int) **radial_segments** = `64` [🔗](class_capsulemesh.md#class_CapsuleMesh_property_radial_segments)

- void **set_radial_segments** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_radial_segments** ( )

Number of radial segments on the capsule mesh.

---

<span id="class_CapsuleMesh_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.5` [🔗](class_capsulemesh.md#class_CapsuleMesh_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

Radius of the capsule mesh.

 **Note:** The [radius](class_capsulemesh.md#class_CapsuleMesh_property_radius) of a capsule cannot be greater than half of its [height](class_capsulemesh.md#class_CapsuleMesh_property_height). Otherwise, the capsule becomes a circle. If the [radius](class_capsulemesh.md#class_CapsuleMesh_property_radius) is greater than half of the [height](class_capsulemesh.md#class_CapsuleMesh_property_height), the properties adjust to a valid value.

---

<span id="class_CapsuleMesh_property_rings"></span>

[int](class_int.md#class_int) **rings** = `8` [🔗](class_capsulemesh.md#class_CapsuleMesh_property_rings)

- void **set_rings** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_rings** ( )

Number of rings along the height of the capsule.
