<span id="class_BoxMesh"></span>

## BoxMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Generate an axis-aligned box [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Description

Generate an axis-aligned box [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

The box's UV layout is arranged in a 3×2 layout that allows texturing each face individually. To apply the same texture on all faces, change the material's UV property to `Vector3(3, 2, 1)`. This is equivalent to adding `UV *= vec2(3.0, 2.0)` in a vertex shader.

 **Note:** When using a large textured **BoxMesh** (e.g. as a floor), you may stumble upon UV jittering issues depending on the camera angle. To solve this, increase [subdivide_depth](class_boxmesh.md#class_BoxMesh_property_subdivide_depth), [subdivide_height](class_boxmesh.md#class_BoxMesh_property_subdivide_height) and [subdivide_width](class_boxmesh.md#class_BoxMesh_property_subdivide_width) until you no longer notice UV jittering.

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [size](class_boxmesh.md#class_BoxMesh_property_size) | `Vector3(1, 1, 1)` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [subdivide_depth](class_boxmesh.md#class_BoxMesh_property_subdivide_depth) | `0` |
| [int](class_int.md#class_int) | [subdivide_height](class_boxmesh.md#class_BoxMesh_property_subdivide_height) | `0` |
| [int](class_int.md#class_int) | [subdivide_width](class_boxmesh.md#class_BoxMesh_property_subdivide_width) | `0` |

---

### Property Descriptions

<span id="class_BoxMesh_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_boxmesh.md#class_BoxMesh_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The box's width, height and depth.

---

<span id="class_BoxMesh_property_subdivide_depth"></span>

[int](class_int.md#class_int) **subdivide_depth** = `0` [🔗](class_boxmesh.md#class_BoxMesh_property_subdivide_depth)

- void **set_subdivide_depth** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_subdivide_depth** ( )

Number of extra edge loops inserted along the Z axis.

---

<span id="class_BoxMesh_property_subdivide_height"></span>

[int](class_int.md#class_int) **subdivide_height** = `0` [🔗](class_boxmesh.md#class_BoxMesh_property_subdivide_height)

- void **set_subdivide_height** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_subdivide_height** ( )

Number of extra edge loops inserted along the Y axis.

---

<span id="class_BoxMesh_property_subdivide_width"></span>

[int](class_int.md#class_int) **subdivide_width** = `0` [🔗](class_boxmesh.md#class_BoxMesh_property_subdivide_width)

- void **set_subdivide_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_subdivide_width** ( )

Number of extra edge loops inserted along the X axis.
