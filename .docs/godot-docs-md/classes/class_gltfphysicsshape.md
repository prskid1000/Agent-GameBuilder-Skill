<span id="class_GLTFPhysicsShape"></span>

## GLTFPhysicsShape

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Represents a glTF physics shape.

### Description

Represents a physics shape as defined by the `OMI_physics_shape` or `OMI_collider` glTF extensions. This class is an intermediary between the glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.

### Tutorials

- [Runtime file loading and saving](../tutorials/io/runtime_file_loading_and_saving.md)

- OMI_physics_shape glTF extension

- OMI_collider glTF extension

### Properties


| [float](class_float.md#class_float) | [height](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_height) | `2.0` |
| --- | --- | --- |
| [ImporterMesh](class_importermesh.md#class_ImporterMesh) | [importer_mesh](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_importer_mesh) |
| [bool](class_bool.md#class_bool) | [is_trigger](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_is_trigger) | `false` |
| [int](class_int.md#class_int) | [mesh_index](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_mesh_index) | `-1` |
| [float](class_float.md#class_float) | [radius](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_radius) | `0.5` |
| [String](class_string.md#class_String) | [shape_type](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_shape_type) | `""` |
| [Vector3](class_vector3.md#class_Vector3) | [size](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_size) | `Vector3(1, 1, 1)` |

### Methods


| [GLTFPhysicsShape](class_gltfphysicsshape.md#class_GLTFPhysicsShape) | [from_dictionary](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_from_dictionary) ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) static |
| --- | --- |
| [GLTFPhysicsShape](class_gltfphysicsshape.md#class_GLTFPhysicsShape) | [from_node](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_from_node) ( shape_node: [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D) ) static |
| [GLTFPhysicsShape](class_gltfphysicsshape.md#class_GLTFPhysicsShape) | [from_resource](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_from_resource) ( shape_resource: [Shape3D](class_shape3d.md#class_Shape3D) ) static |
| [Dictionary](class_dictionary.md#class_Dictionary) | [to_dictionary](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_to_dictionary) ( ) const |
| [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D) | [to_node](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_to_node) ( cache_shapes: [bool](class_bool.md#class_bool) = false ) |
| [Shape3D](class_shape3d.md#class_Shape3D) | [to_resource](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_to_resource) ( cache_shapes: [bool](class_bool.md#class_bool) = false ) |

---

### Property Descriptions

<span id="class_GLTFPhysicsShape_property_height"></span>

[float](class_float.md#class_float) **height** = `2.0` [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_height)

- void **set_height** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_height** ( )

The height of the shape, in meters. This is only used when the shape type is `"capsule"` or `"cylinder"`. This value should not be negative, and for `"capsule"` it should be at least twice the radius.

---

<span id="class_GLTFPhysicsShape_property_importer_mesh"></span>

[ImporterMesh](class_importermesh.md#class_ImporterMesh) **importer_mesh** [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_importer_mesh)

- void **set_importer_mesh** ( value: [ImporterMesh](class_importermesh.md#class_ImporterMesh) )
- [ImporterMesh](class_importermesh.md#class_ImporterMesh) **get_importer_mesh** ( )

The [ImporterMesh](class_importermesh.md#class_ImporterMesh) resource of the shape. This is only used when the shape type is `"hull"` (convex hull) or `"trimesh"` (concave trimesh).

---

<span id="class_GLTFPhysicsShape_property_is_trigger"></span>

[bool](class_bool.md#class_bool) **is_trigger** = `false` [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_is_trigger)

- void **set_is_trigger** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_is_trigger** ( )

If `true`, indicates that this shape is a trigger. For Godot, this means that the shape should be a child of an [Area3D](class_area3d.md#class_Area3D) node.

This is the only variable not used in the [to_node()](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_to_node) method, it's intended to be used alongside when deciding where to add the generated node as a child.

---

<span id="class_GLTFPhysicsShape_property_mesh_index"></span>

[int](class_int.md#class_int) **mesh_index** = `-1` [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_mesh_index)

- void **set_mesh_index** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_mesh_index** ( )

The index of the shape's mesh in the glTF file. This is only used when the shape type is `"hull"` (convex hull) or `"trimesh"` (concave trimesh).

---

<span id="class_GLTFPhysicsShape_property_radius"></span>

[float](class_float.md#class_float) **radius** = `0.5` [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The radius of the shape, in meters. This is only used when the shape type is `"capsule"`, `"cylinder"`, or `"sphere"`. This value should not be negative.

---

<span id="class_GLTFPhysicsShape_property_shape_type"></span>

[String](class_string.md#class_String) **shape_type** = `""` [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_shape_type)

- void **set_shape_type** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_shape_type** ( )

The type of shape this shape represents. Valid values are `"box"`, `"capsule"`, `"cylinder"`, `"sphere"`, `"hull"`, and `"trimesh"`.

---

<span id="class_GLTFPhysicsShape_property_size"></span>

[Vector3](class_vector3.md#class_Vector3) **size** = `Vector3(1, 1, 1)` [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_property_size)

- void **set_size** ( value: [Vector3](class_vector3.md#class_Vector3) )
- [Vector3](class_vector3.md#class_Vector3) **get_size** ( )

The size of the shape, in meters. This is only used when the shape type is `"box"`, and it represents the `"diameter"` of the box. This value should not be negative.

---

### Method Descriptions

<span id="class_GLTFPhysicsShape_method_from_dictionary"></span>

[GLTFPhysicsShape](class_gltfphysicsshape.md#class_GLTFPhysicsShape) **from_dictionary** ( dictionary: [Dictionary](class_dictionary.md#class_Dictionary) ) *static* [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_from_dictionary)

Creates a new GLTFPhysicsShape instance by parsing the given [Dictionary](class_dictionary.md#class_Dictionary).

---

<span id="class_GLTFPhysicsShape_method_from_node"></span>

[GLTFPhysicsShape](class_gltfphysicsshape.md#class_GLTFPhysicsShape) **from_node** ( shape_node: [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D) ) *static* [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_from_node)

Creates a new GLTFPhysicsShape instance from the given Godot [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D) node.

---

<span id="class_GLTFPhysicsShape_method_from_resource"></span>

[GLTFPhysicsShape](class_gltfphysicsshape.md#class_GLTFPhysicsShape) **from_resource** ( shape_resource: [Shape3D](class_shape3d.md#class_Shape3D) ) *static* [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_from_resource)

Creates a new GLTFPhysicsShape instance from the given Godot [Shape3D](class_shape3d.md#class_Shape3D) resource.

---

<span id="class_GLTFPhysicsShape_method_to_dictionary"></span>

[Dictionary](class_dictionary.md#class_Dictionary) **to_dictionary** ( ) *const* [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_to_dictionary)

Serializes this GLTFPhysicsShape instance into a [Dictionary](class_dictionary.md#class_Dictionary) in the format defined by `OMI_physics_shape`.

---

<span id="class_GLTFPhysicsShape_method_to_node"></span>

[CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D) **to_node** ( cache_shapes: [bool](class_bool.md#class_bool) = false ) [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_to_node)

Converts this GLTFPhysicsShape instance into a Godot [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D) node.

---

<span id="class_GLTFPhysicsShape_method_to_resource"></span>

[Shape3D](class_shape3d.md#class_Shape3D) **to_resource** ( cache_shapes: [bool](class_bool.md#class_bool) = false ) [🔗](class_gltfphysicsshape.md#class_GLTFPhysicsShape_method_to_resource)

Converts this GLTFPhysicsShape instance into a Godot [Shape3D](class_shape3d.md#class_Shape3D) resource.
