<span id="class_PrismMesh"></span>

## PrismMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Class representing a prism-shaped [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Description

Class representing a prism-shaped [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Properties


| [float](class_float.md#class_float) | [left_to_right](class_prismmesh.md#class_PrismMesh_property_left_to_right) | `0.5` |
| --- | --- | --- |
| [Vector3](class_vector3.md#class_Vector3) | [size](class_prismmesh.md#class_PrismMesh_property_size) | `Vector3(1, 1, 1)` |
| [int](class_int.md#class_int) | [subdivide_depth](class_prismmesh.md#class_PrismMesh_property_subdivide_depth) | `0` |
| [int](class_int.md#class_int) | [subdivide_height](class_prismmesh.md#class_PrismMesh_property_subdivide_height) | `0` |
| [int](class_int.md#class_int) | [subdivide_width](class_prismmesh.md#class_PrismMesh_property_subdivide_width) | `0` |

---

### Property Descriptions

<span id="class_PrismMesh_property_left_to_right"></span>

[float](class_float.md#class_float) **left_to_right** = `0.5` [🔗](class_prismmesh.md#class_PrismMesh_property_left_to_right)

- void **set_left_to_right** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_left_to_right** ( )

Displacement of the upper edge along the X axis. 0.0 positions edge straight above the bottom-left edge.

---

<span id="class_PrismMesh_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_prismmesh.md#class_PrismMesh_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

Size of the prism.

---

<span id="class_PrismMesh_property_subdivide_depth"></span>

[int](class_int.md#class_int) **subdivide_depth** = `0` [🔗](class_prismmesh.md#class_PrismMesh_property_subdivide_depth)

- void **set_subdivide_depth** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_subdivide_depth** ( )

Number of added edge loops along the Z axis.

---

<span id="class_PrismMesh_property_subdivide_height"></span>

[int](class_int.md#class_int) **subdivide_height** = `0` [🔗](class_prismmesh.md#class_PrismMesh_property_subdivide_height)

- void **set_subdivide_height** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_subdivide_height** ( )

Number of added edge loops along the Y axis.

---

<span id="class_PrismMesh_property_subdivide_width"></span>

[int](class_int.md#class_int) **subdivide_width** = `0` [🔗](class_prismmesh.md#class_PrismMesh_property_subdivide_width)

- void **set_subdivide_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_subdivide_width** ( )

Number of added edge loops along the X axis.
