<span id="class_QuadMesh"></span>

## QuadMesh

**Inherits:** [PlaneMesh](class_planemesh.md#class_PlaneMesh) **<** [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh) **<** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Class representing a square mesh facing the camera.

### Description

Class representing a square [PrimitiveMesh](class_primitivemesh.md#class_PrimitiveMesh). This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Y axes; this rotation is more suited for use with billboarded materials. A **QuadMesh** is equivalent to a [PlaneMesh](class_planemesh.md#class_PlaneMesh) except its default [PlaneMesh.orientation](class_planemesh.md#class_PlaneMesh_property_orientation) is [PlaneMesh.FACE_Z](class_planemesh.md#class_PlaneMesh_constant_FACE_Z).

### Tutorials

- GUI in 3D Viewport Demo

- 2D in 3D Viewport Demo

### Properties


| [Orientation](class_planemesh.md#enum_PlaneMesh_Orientation) | orientation | `2` (overrides [PlaneMesh](class_planemesh.md#class_PlaneMesh_property_orientation)) |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | size | `Vector2(1, 1)` (overrides [PlaneMesh](class_planemesh.md#class_PlaneMesh_property_size)) |
