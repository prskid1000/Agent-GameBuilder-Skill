<span id="class_ConcavePolygonShape3D"></span>

## ConcavePolygonShape3D

**Inherits:** [Shape3D](class_shape3d.md#class_Shape3D) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A 3D trimesh shape used for physics collision.

### Description

A 3D trimesh shape, intended for use in physics. Usually used to provide a shape for a [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D).

Being just a collection of interconnected triangles, **ConcavePolygonShape3D** is the most freely configurable single 3D shape. It can be used to form polyhedra of any nature, or even shapes that don't enclose a volume. However, **ConcavePolygonShape3D** is *hollow* even if the interconnected triangles do enclose a volume, which often makes it unsuitable for physics or detection.

 **Note:** When used for collision, **ConcavePolygonShape3D** is intended to work with static [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D) nodes like [StaticBody3D](class_staticbody3d.md#class_StaticBody3D) and will likely not behave well for [CharacterBody3D](class_characterbody3d.md#class_CharacterBody3D) s or [RigidBody3D](class_rigidbody3d.md#class_RigidBody3D) s in a mode other than Static.

 **Warning:** Physics bodies that are small have a chance to clip through this shape when moving fast. This happens because on one frame, the physics body may be on the "outside" of the shape, and on the next frame it may be "inside" it. **ConcavePolygonShape3D** is hollow, so it won't detect a collision.

 **Performance:** Due to its complexity, **ConcavePolygonShape3D** is the slowest 3D collision shape to check collisions against. Its use should generally be limited to level geometry. For convex geometry, [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class_ConvexPolygonShape3D) should be used. For dynamic physics bodies that need concave collision, several [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class_ConvexPolygonShape3D) s can be used to represent its collision by using convex decomposition; see [ConvexPolygonShape3D](class_convexpolygonshape3d.md#class_ConvexPolygonShape3D)'s documentation for instructions.

### Tutorials

- 3D Physics Tests Demo

### Properties


| [bool](class_bool.md#class_bool) | [backface_collision](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D_property_backface_collision) | `false` |
| --- | --- | --- |

### Methods


| [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) | [get_faces](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D_method_get_faces) ( ) const |
| --- | --- |
| void | [set_faces](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D_method_set_faces) ( faces: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) |

---

### Property Descriptions

<span id="class_ConcavePolygonShape3D_property_backface_collision"></span>

[bool](class_bool.md#class_bool) **backface_collision** = `false` [🔗](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D_property_backface_collision)

- void **set_backface_collision_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_backface_collision_enabled** ( )

If set to `true`, collisions occur on both sides of the concave shape faces. Otherwise they occur only along the face normals.

---

### Method Descriptions

<span id="class_ConcavePolygonShape3D_method_get_faces"></span>

[PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) **get_faces** ( ) *const* [🔗](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D_method_get_faces)

Returns the faces of the trimesh shape as an array of vertices. The array (of length divisible by three) is naturally divided into triples; each triple of vertices defines a triangle.

---

<span id="class_ConcavePolygonShape3D_method_set_faces"></span>

void **set_faces** ( faces: [PackedVector3Array](class_packedvector3array.md#class_PackedVector3Array) ) [🔗](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D_method_set_faces)

Sets the faces of the trimesh shape from an array of vertices. The `faces` array should be composed of triples such that each triple of vertices defines a triangle.
