<span id="class_SkinReference"></span>

## SkinReference

**Inherits:** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A reference-counted holder object for a skeleton RID used in the [RenderingServer](class_renderingserver.md#class_RenderingServer).

### Description

An internal object containing a mapping from a [Skin](class_skin.md#class_Skin) used within the context of a particular [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) to refer to the skeleton's [RID](class_rid.md#class_RID) in the RenderingServer.

See also [MeshInstance3D.get_skin_reference()](class_meshinstance3d.md#class_MeshInstance3D_method_get_skin_reference) and [RenderingServer.instance_attach_skeleton()](class_renderingserver.md#class_RenderingServer_method_instance_attach_skeleton).

Note that despite the similar naming, the skeleton RID used in the [RenderingServer](class_renderingserver.md#class_RenderingServer) does not have a direct one-to-one correspondence to a [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) node.

In particular, a [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) node with no [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) children may be unknown to the [RenderingServer](class_renderingserver.md#class_RenderingServer).

On the other hand, a [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) with multiple [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) nodes which each have different [MeshInstance3D.skin](class_meshinstance3d.md#class_MeshInstance3D_property_skin) objects may have multiple SkinReference instances (and hence, multiple skeleton [RID](class_rid.md#class_RID) s).

### Methods


| [RID](class_rid.md#class_RID) | [get_skeleton](class_skinreference.md#class_SkinReference_method_get_skeleton) ( ) const |
| --- | --- |
| [Skin](class_skin.md#class_Skin) | [get_skin](class_skinreference.md#class_SkinReference_method_get_skin) ( ) const |

---

### Method Descriptions

<span id="class_SkinReference_method_get_skeleton"></span>

[RID](class_rid.md#class_RID) **get_skeleton** ( ) *const* [🔗](class_skinreference.md#class_SkinReference_method_get_skeleton)

Returns the [RID](class_rid.md#class_RID) owned by this SkinReference, as returned by [RenderingServer.skeleton_create()](class_renderingserver.md#class_RenderingServer_method_skeleton_create).

---

<span id="class_SkinReference_method_get_skin"></span>

[Skin](class_skin.md#class_Skin) **get_skin** ( ) *const* [🔗](class_skinreference.md#class_SkinReference_method_get_skin)

Returns the [Skin](class_skin.md#class_Skin) connected to this SkinReference. In the case of [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D) with no [MeshInstance3D.skin](class_meshinstance3d.md#class_MeshInstance3D_property_skin) assigned, this will reference an internal default [Skin](class_skin.md#class_Skin) owned by that [MeshInstance3D](class_meshinstance3d.md#class_MeshInstance3D).

Note that a single [Skin](class_skin.md#class_Skin) may have more than one **SkinReference** in the case that it is shared by meshes across multiple [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) nodes.
