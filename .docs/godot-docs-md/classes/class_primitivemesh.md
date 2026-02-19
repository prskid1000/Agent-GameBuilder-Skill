<span id="class_PrimitiveMesh"></span>

## PrimitiveMesh

**Inherits:** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [BoxMesh](class_boxmesh.md#class_BoxMesh), [CapsuleMesh](class_capsulemesh.md#class_CapsuleMesh), [CylinderMesh](class_cylindermesh.md#class_CylinderMesh), [PlaneMesh](class_planemesh.md#class_PlaneMesh), [PointMesh](class_pointmesh.md#class_PointMesh), [PrismMesh](class_prismmesh.md#class_PrismMesh), [RibbonTrailMesh](class_ribbontrailmesh.md#class_RibbonTrailMesh), [SphereMesh](class_spheremesh.md#class_SphereMesh), [TextMesh](class_textmesh.md#class_TextMesh), [TorusMesh](class_torusmesh.md#class_TorusMesh), [TubeTrailMesh](class_tubetrailmesh.md#class_TubeTrailMesh)

Base class for all primitive meshes. Handles applying a [Material](class_material.md#class_Material) to a primitive mesh.

### Description

Base class for all primitive meshes. Handles applying a [Material](class_material.md#class_Material) to a primitive mesh. Examples include [BoxMesh](class_boxmesh.md#class_BoxMesh), [CapsuleMesh](class_capsulemesh.md#class_CapsuleMesh), [CylinderMesh](class_cylindermesh.md#class_CylinderMesh), [PlaneMesh](class_planemesh.md#class_PlaneMesh), [PrismMesh](class_prismmesh.md#class_PrismMesh), and [SphereMesh](class_spheremesh.md#class_SphereMesh).

### Properties


| [bool](class_bool.md#class_bool) | [add_uv2](class_primitivemesh.md#class_PrimitiveMesh_property_add_uv2) | `false` |
| --- | --- | --- |
| [AABB](class_aabb.md#class_AABB) | [custom_aabb](class_primitivemesh.md#class_PrimitiveMesh_property_custom_aabb) | `AABB(0, 0, 0, 0, 0, 0)` |
| [bool](class_bool.md#class_bool) | [flip_faces](class_primitivemesh.md#class_PrimitiveMesh_property_flip_faces) | `false` |
| [Material](class_material.md#class_Material) | [material](class_primitivemesh.md#class_PrimitiveMesh_property_material) |
| [float](class_float.md#class_float) | [uv2_padding](class_primitivemesh.md#class_PrimitiveMesh_property_uv2_padding) | `2.0` |

### Methods


| [Array](class_array.md#class_Array) | [_create_mesh_array](class_primitivemesh.md#class_PrimitiveMesh_private_method__create_mesh_array) ( ) | virtual | const |
| --- | --- | --- | --- |
| [Array](class_array.md#class_Array) | [get_mesh_arrays](class_primitivemesh.md#class_PrimitiveMesh_method_get_mesh_arrays) ( ) const |
| void | [request_update](class_primitivemesh.md#class_PrimitiveMesh_method_request_update) ( ) |

---

### Property Descriptions

<span id="class_PrimitiveMesh_property_add_uv2"></span>

[bool](class_bool.md#class_bool) **add_uv2** = `false` [🔗](class_primitivemesh.md#class_PrimitiveMesh_property_add_uv2)

- void **set_add_uv2** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_add_uv2** ( )

If set, generates UV2 UV coordinates applying a padding using the [uv2_padding](class_primitivemesh.md#class_PrimitiveMesh_property_uv2_padding) setting. UV2 is needed for lightmapping.

---

<span id="class_PrimitiveMesh_property_custom_aabb"></span>

[AABB](class_aabb.md#class_AABB) **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_primitivemesh.md#class_PrimitiveMesh_property_custom_aabb)

- void **set_custom_aabb** ( value: [AABB](class_aabb.md#class_AABB) )
- [AABB](class_aabb.md#class_AABB) **get_custom_aabb** ( )

Overrides the [AABB](class_aabb.md#class_AABB) with one defined by user for use with frustum culling. Especially useful to avoid unexpected culling when using a shader to offset vertices.

---

<span id="class_PrimitiveMesh_property_flip_faces"></span>

[bool](class_bool.md#class_bool) **flip_faces** = `false` [🔗](class_primitivemesh.md#class_PrimitiveMesh_property_flip_faces)

- void **set_flip_faces** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_flip_faces** ( )

If `true`, the order of the vertices in each triangle is reversed, resulting in the backside of the mesh being drawn.

This gives the same result as using [BaseMaterial3D.CULL_FRONT](class_basematerial3d.md#class_BaseMaterial3D_constant_CULL_FRONT) in [BaseMaterial3D.cull_mode](class_basematerial3d.md#class_BaseMaterial3D_property_cull_mode).

---

<span id="class_PrimitiveMesh_property_material"></span>

[Material](class_material.md#class_Material) **material** [🔗](class_primitivemesh.md#class_PrimitiveMesh_property_material)

- void **set_material** ( value: [Material](class_material.md#class_Material) )
- [Material](class_material.md#class_Material) **get_material** ( )

The current [Material](class_material.md#class_Material) of the primitive mesh.

---

<span id="class_PrimitiveMesh_property_uv2_padding"></span>

[float](class_float.md#class_float) **uv2_padding** = `2.0` [🔗](class_primitivemesh.md#class_PrimitiveMesh_property_uv2_padding)

- void **set_uv2_padding** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_uv2_padding** ( )

If [add_uv2](class_primitivemesh.md#class_PrimitiveMesh_property_add_uv2) is set, specifies the padding in pixels applied along seams of the mesh. Lower padding values allow making better use of the lightmap texture (resulting in higher texel density), but may introduce visible lightmap bleeding along edges.

If the size of the lightmap texture can't be determined when generating the mesh, UV2 is calculated assuming a texture size of 1024x1024.

---

### Method Descriptions

<span id="class_PrimitiveMesh_private_method__create_mesh_array"></span>

[Array](class_array.md#class_Array) **_create_mesh_array** ( ) *virtual* *const* [🔗](class_primitivemesh.md#class_PrimitiveMesh_private_method__create_mesh_array)

Override this method to customize how this primitive mesh should be generated. Should return an [Array](class_array.md#class_Array) where each element is another Array of values required for the mesh (see the [ArrayType](class_mesh.md#enum_Mesh_ArrayType) constants).

---

<span id="class_PrimitiveMesh_method_get_mesh_arrays"></span>

[Array](class_array.md#class_Array) **get_mesh_arrays** ( ) *const* [🔗](class_primitivemesh.md#class_PrimitiveMesh_method_get_mesh_arrays)

Returns the mesh arrays used to make up the surface of this primitive mesh.

 **Example:** Pass the result to [ArrayMesh.add_surface_from_arrays()](class_arraymesh.md#class_ArrayMesh_method_add_surface_from_arrays) to create a new surface:

.. tabs::

```
```

    var c = CylinderMesh.new()
    var arr_mesh = ArrayMesh.new()
    arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, c.get_mesh_arrays())

```
```

    var c = new CylinderMesh();
    var arrMesh = new ArrayMesh();
    arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, c.GetMeshArrays());

---

<span id="class_PrimitiveMesh_method_request_update"></span>

void **request_update** ( ) [🔗](class_primitivemesh.md#class_PrimitiveMesh_method_request_update)

Request an update of this primitive mesh based on its properties.
