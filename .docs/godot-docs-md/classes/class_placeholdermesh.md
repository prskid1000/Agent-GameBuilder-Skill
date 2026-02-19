<span id="class_PlaceholderMesh"></span>

## PlaceholderMesh

**Inherits:** [Mesh](class_mesh.md#class_Mesh) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Placeholder class for a mesh.

### Description

This class is used when loading a project that uses a [Mesh](class_mesh.md#class_Mesh) subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.

- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

### Properties


| [AABB](class_aabb.md#class_AABB) | [aabb](class_placeholdermesh.md#class_PlaceholderMesh_property_aabb) | `AABB(0, 0, 0, 0, 0, 0)` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_PlaceholderMesh_property_aabb"></span>

[AABB](class_aabb.md#class_AABB) **aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗](class_placeholdermesh.md#class_PlaceholderMesh_property_aabb)

- void **set_aabb** ( value: [AABB](class_aabb.md#class_AABB) )
- [AABB](class_aabb.md#class_AABB) **get_aabb** ( )

The smallest [AABB](class_aabb.md#class_AABB) enclosing this mesh in local space.
