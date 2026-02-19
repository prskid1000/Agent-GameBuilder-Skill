<span id="class_PlaneMesh"></span>

## PlaneMesh

**Inherits:** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [QuadMesh](class_quadmesh.md#class_QuadMesh)

Class representing a planar [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh).

### Description

Class representing a planar [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh). This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Z axes; this default rotation isn't suited for use with billboarded materials. For billboarded materials, change [orientation](class_planemesh.md#class_PlaneMesh_property_orientation) to [FACE_Z](class_planemesh.md#class_PlaneMesh_constant_FACE_Z).

 **Note:** When using a large textured **PlaneMesh** (e.g. as a floor), you may stumble upon UV jittering issues depending on the camera angle. To solve this, increase [subdivide_depth](class_planemesh.md#class_PlaneMesh_property_subdivide_depth) and [subdivide_width](class_planemesh.md#class_PlaneMesh_property_subdivide_width) until you no longer notice UV jittering.

### Properties


| [Vector3](class_vector3.md#class_Vector3) | [center_offset](class_planemesh.md#class_PlaneMesh_property_center_offset) | `Vector3(0, 0, 0)` |
| --- | --- | --- |
| [Orientation](class_planemesh.md#enum_PlaneMesh_Orientation) | [orientation](class_planemesh.md#class_PlaneMesh_property_orientation) | `1` |
| [Vector2](class_vector2.md#class_Vector2) | [size](class_planemesh.md#class_PlaneMesh_property_size) | `Vector2(2, 2)` |
| [int](class_int.md#class_int) | [subdivide_depth](class_planemesh.md#class_PlaneMesh_property_subdivide_depth) | `0` |
| [int](class_int.md#class_int) | [subdivide_width](class_planemesh.md#class_PlaneMesh_property_subdivide_width) | `0` |

---

### Enumerations

<span id="enum_PlaneMesh_Orientation"></span>

enum **Orientation**: [🔗](class_planemesh.md#enum_PlaneMesh_Orientation)

<span id="class_PlaneMesh_constant_FACE_X"></span>

[Orientation](class_planemesh.md#enum_PlaneMesh_Orientation) **FACE_X** = `0`

**PlaneMesh** will face the positive X-axis.

<span id="class_PlaneMesh_constant_FACE_Y"></span>

[Orientation](class_planemesh.md#enum_PlaneMesh_Orientation) **FACE_Y** = `1`

**PlaneMesh** will face the positive Y-axis. This matches the behavior of the **PlaneMesh** in Godot 3.x.

<span id="class_PlaneMesh_constant_FACE_Z"></span>

[Orientation](class_planemesh.md#enum_PlaneMesh_Orientation) **FACE_Z** = `2`

**PlaneMesh** will face the positive Z-axis. This matches the behavior of the QuadMesh in Godot 3.x.

---

### Property Descriptions

<span id="class_PlaneMesh_property_center_offset"></span>

[Vector3](class_vector3.md#class_Vector3) **center_offset** = `Vector3(0, 0, 0)` [🔗](class_planemesh.md#class_PlaneMesh_property_center_offset)

- void **set_center_offset** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_center_offset** ( )

Offset of the generated plane. Useful for particles.

---

<span id="class_PlaneMesh_property_orientation"></span>

[Orientation](class_planemesh.md#enum_PlaneMesh_Orientation) **orientation** = `1` [🔗](class_planemesh.md#class_PlaneMesh_property_orientation)

- void **set_orientation** ( value: [Orientation](class_planemesh.md#enum_PlaneMesh_Orientation) )
- [Orientation](class_planemesh.md#enum_PlaneMesh_Orientation) **get_orientation** ( )

Direction that the **PlaneMesh** is facing.

---

<span id="class_PlaneMesh_property_size"></span>

[Vector2](class_vector2.md#class_Vector2) **size** = `Vector2(2, 2)` [🔗](class_planemesh.md#class_PlaneMesh_property_size)

- void **set_size** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_size** ( )

Size of the generated plane.

---

<span id="class_PlaneMesh_property_subdivide_depth"></span>

[int](class_int.md#class_int) **subdivide_depth** = `0` [🔗](class_planemesh.md#class_PlaneMesh_property_subdivide_depth)

- void **set_subdivide_depth** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_subdivide_depth** ( )

Number of subdivision along the Z axis.

---

<span id="class_PlaneMesh_property_subdivide_width"></span>

[int](class_int.md#class_int) **subdivide_width** = `0` [🔗](class_planemesh.md#class_PlaneMesh_property_subdivide_width)

- void **set_subdivide_width** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_subdivide_width** ( )

Number of subdivision along the X axis.
