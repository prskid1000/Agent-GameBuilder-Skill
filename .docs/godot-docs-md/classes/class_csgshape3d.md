<span id="class_CSGShape3D"></span>

## CSGShape3D

**Inherits:** [GeometryInstance3D](class_geometryinstance3d.md#class_GeometryInstance3D) **<** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [CSGCombiner3D](class_csgcombiner3d.md#class_CSGCombiner3D), [CSGPrimitive3D](class_csgprimitive3d.md#class_CSGPrimitive3D)

The CSG base class.

### Description

This is the CSG base class that provides CSG operation support to the various CSG nodes in Godot.

 **Performance:** CSG nodes are only intended for prototyping as they have a significant CPU performance cost. Consider baking final CSG operation results into static geometry that replaces the CSG nodes.

Individual CSG root node results can be baked to nodes with static resources with the editor menu that appears when a CSG root node is selected.

Individual CSG root nodes can also be baked to static resources with scripts by calling [bake_static_mesh()](class_csgshape3d.md#class_CSGShape3D_method_bake_static_mesh) for the visual mesh or [bake_collision_shape()](class_csgshape3d.md#class_CSGShape3D_method_bake_collision_shape) for the physics collision.

Entire scenes of CSG nodes can be baked to static geometry and exported with the editor glTF scene exporter: **Scene > Export As... > glTF 2.0 Scene...**

### Tutorials

- [Prototyping levels with CSG](../tutorials/3d/csg_tools.md)

### Properties


| [bool](class_bool.md#class_bool) | [calculate_tangents](class_csgshape3d.md#class_CSGShape3D_property_calculate_tangents) | `true` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [collision_layer](class_csgshape3d.md#class_CSGShape3D_property_collision_layer) | `1` |
| [int](class_int.md#class_int) | [collision_mask](class_csgshape3d.md#class_CSGShape3D_property_collision_mask) | `1` |
| [float](class_float.md#class_float) | [collision_priority](class_csgshape3d.md#class_CSGShape3D_property_collision_priority) | `1.0` |
| [Operation](class_csgshape3d.md#enum_CSGShape3D_Operation) | [operation](class_csgshape3d.md#class_CSGShape3D_property_operation) | `0` |
| [float](class_float.md#class_float) | [snap](class_csgshape3d.md#class_CSGShape3D_property_snap) |
| [bool](class_bool.md#class_bool) | [use_collision](class_csgshape3d.md#class_CSGShape3D_property_use_collision) | `false` |

### Methods


| [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D) | [bake_collision_shape](class_csgshape3d.md#class_CSGShape3D_method_bake_collision_shape) ( ) |
| --- | --- |
| [ArrayMesh](class_arraymesh.md#class_ArrayMesh) | [bake_static_mesh](class_csgshape3d.md#class_CSGShape3D_method_bake_static_mesh) ( ) |
| [bool](class_bool.md#class_bool) | [get_collision_layer_value](class_csgshape3d.md#class_CSGShape3D_method_get_collision_layer_value) ( layer_number: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [get_collision_mask_value](class_csgshape3d.md#class_CSGShape3D_method_get_collision_mask_value) ( layer_number: [int](class_int.md#class_int) ) const |
| [Array](class_array.md#class_Array) | [get_meshes](class_csgshape3d.md#class_CSGShape3D_method_get_meshes) ( ) const |
| [bool](class_bool.md#class_bool) | [is_root_shape](class_csgshape3d.md#class_CSGShape3D_method_is_root_shape) ( ) const |
| void | [set_collision_layer_value](class_csgshape3d.md#class_CSGShape3D_method_set_collision_layer_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |
| void | [set_collision_mask_value](class_csgshape3d.md#class_CSGShape3D_method_set_collision_mask_value) ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) |

---

### Enumerations

<span id="enum_CSGShape3D_Operation"></span>

enum **Operation**: [🔗](class_csgshape3d.md#enum_CSGShape3D_Operation)

<span id="class_CSGShape3D_constant_OPERATION_UNION"></span>

[Operation](class_csgshape3d.md#enum_CSGShape3D_Operation) **OPERATION_UNION** = `0`

Geometry of both primitives is merged, intersecting geometry is removed.

<span id="class_CSGShape3D_constant_OPERATION_INTERSECTION"></span>

[Operation](class_csgshape3d.md#enum_CSGShape3D_Operation) **OPERATION_INTERSECTION** = `1`

Only intersecting geometry remains, the rest is removed.

<span id="class_CSGShape3D_constant_OPERATION_SUBTRACTION"></span>

[Operation](class_csgshape3d.md#enum_CSGShape3D_Operation) **OPERATION_SUBTRACTION** = `2`

The second shape is subtracted from the first, leaving a dent with its shape.

---

### Property Descriptions

<span id="class_CSGShape3D_property_calculate_tangents"></span>

[bool](class_bool.md#class_bool) **calculate_tangents** = `true` [🔗](class_csgshape3d.md#class_CSGShape3D_property_calculate_tangents)

- void **set_calculate_tangents** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_calculating_tangents** ( )

Calculate tangents for the CSG shape which allows the use of normal and height maps. This is only applied on the root shape, this setting is ignored on any child. Setting this to `false` can speed up shape generation slightly.

---

<span id="class_CSGShape3D_property_collision_layer"></span>

[int](class_int.md#class_int) **collision_layer** = `1` [🔗](class_csgshape3d.md#class_CSGShape3D_property_collision_layer)

- void **set_collision_layer** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_layer** ( )

The physics layers this area is in.

Collidable objects can exist in any of 32 different layers. These layers work like a tagging system, and are not visual. A collidable can use these layers to select with which objects it can collide, using the collision_mask property.

A contact is detected if object A is in any of the layers that object B scans, or object B is in any layer scanned by object A. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_CSGShape3D_property_collision_mask"></span>

[int](class_int.md#class_int) **collision_mask** = `1` [🔗](class_csgshape3d.md#class_CSGShape3D_property_collision_mask)

- void **set_collision_mask** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_collision_mask** ( )

The physics layers this CSG shape scans for collisions. Only effective if [use_collision](class_csgshape3d.md#class_CSGShape3D_property_use_collision) is `true`. See `Collision layers and masks <../tutorials/physics/physics_introduction.html#collision-layers-and-masks>`__ in the documentation for more information.

---

<span id="class_CSGShape3D_property_collision_priority"></span>

[float](class_float.md#class_float) **collision_priority** = `1.0` [🔗](class_csgshape3d.md#class_CSGShape3D_property_collision_priority)

- void **set_collision_priority** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_collision_priority** ( )

The priority used to solve colliding when occurring penetration. Only effective if [use_collision](class_csgshape3d.md#class_CSGShape3D_property_use_collision) is `true`. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.

---

<span id="class_CSGShape3D_property_operation"></span>

[Operation](class_csgshape3d.md#enum_CSGShape3D_Operation) **operation** = `0` [🔗](class_csgshape3d.md#class_CSGShape3D_property_operation)

- void **set_operation** ( value: [Operation](class_csgshape3d.md#enum_CSGShape3D_Operation) )
- [Operation](class_csgshape3d.md#enum_CSGShape3D_Operation) **get_operation** ( )

The operation that is performed on this shape. This is ignored for the first CSG child node as the operation is between this node and the previous child of this nodes parent.

---

<span id="class_CSGShape3D_property_snap"></span>

[float](class_float.md#class_float) **snap** [🔗](class_csgshape3d.md#class_CSGShape3D_property_snap)

- void **set_snap** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_snap** ( )

**Deprecated:** The CSG library no longer uses snapping.

This property does nothing.

---

<span id="class_CSGShape3D_property_use_collision"></span>

[bool](class_bool.md#class_bool) **use_collision** = `false` [🔗](class_csgshape3d.md#class_CSGShape3D_property_use_collision)

- void **set_use_collision** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_collision** ( )

Adds a collision shape to the physics engine for our CSG shape. This will always act like a static body. Note that the collision shape is still active even if the CSG shape itself is hidden. See also [collision_mask](class_csgshape3d.md#class_CSGShape3D_property_collision_mask) and [collision_priority](class_csgshape3d.md#class_CSGShape3D_property_collision_priority).

---

### Method Descriptions

<span id="class_CSGShape3D_method_bake_collision_shape"></span>

[ConcavePolygonShape3D](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D) **bake_collision_shape** ( ) [🔗](class_csgshape3d.md#class_CSGShape3D_method_bake_collision_shape)

Returns a baked physics [ConcavePolygonShape3D](class_concavepolygonshape3d.md#class_ConcavePolygonShape3D) of this node's CSG operation result. Returns an empty shape if the node is not a CSG root node or has no valid geometry.

 **Performance:** If the CSG operation results in a very detailed geometry with many faces physics performance will be very slow. Concave shapes should in general only be used for static level geometry and not with dynamic objects that are moving.

 **Note:** CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty shape or outdated mesh data, make sure to call `await get_tree().process_frame` before using [bake_collision_shape()](class_csgshape3d.md#class_CSGShape3D_method_bake_collision_shape) in [Node._ready()](class_node.md#class_Node_private_method__ready) or after changing properties on the **CSGShape3D**.

---

<span id="class_CSGShape3D_method_bake_static_mesh"></span>

[ArrayMesh](class_arraymesh.md#class_ArrayMesh) **bake_static_mesh** ( ) [🔗](class_csgshape3d.md#class_CSGShape3D_method_bake_static_mesh)

Returns a baked static [ArrayMesh](class_arraymesh.md#class_ArrayMesh) of this node's CSG operation result. Materials from involved CSG nodes are added as extra mesh surfaces. Returns an empty mesh if the node is not a CSG root node or has no valid geometry.

 **Note:** CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty mesh or outdated mesh data, make sure to call `await get_tree().process_frame` before using [bake_static_mesh()](class_csgshape3d.md#class_CSGShape3D_method_bake_static_mesh) in [Node._ready()](class_node.md#class_Node_private_method__ready) or after changing properties on the **CSGShape3D**.

---

<span id="class_CSGShape3D_method_get_collision_layer_value"></span>

[bool](class_bool.md#class_bool) **get_collision_layer_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_csgshape3d.md#class_CSGShape3D_method_get_collision_layer_value)

Returns whether or not the specified layer of the [collision_layer](class_csgshape3d.md#class_CSGShape3D_property_collision_layer) is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_CSGShape3D_method_get_collision_mask_value"></span>

[bool](class_bool.md#class_bool) **get_collision_mask_value** ( layer_number: [int](class_int.md#class_int) ) *const* [🔗](class_csgshape3d.md#class_CSGShape3D_method_get_collision_mask_value)

Returns whether or not the specified layer of the [collision_mask](class_csgshape3d.md#class_CSGShape3D_property_collision_mask) is enabled, given a `layer_number` between 1 and 32.

---

<span id="class_CSGShape3D_method_get_meshes"></span>

[Array](class_array.md#class_Array) **get_meshes** ( ) *const* [🔗](class_csgshape3d.md#class_CSGShape3D_method_get_meshes)

Returns an [Array](class_array.md#class_Array) with two elements, the first is the [Transform3D](class_transform3d.md#class_Transform3D) of this node and the second is the root [Mesh](class_mesh.md#class_Mesh) of this node. Only works when this node is the root shape.

 **Note:** CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty shape or outdated mesh data, make sure to call `await get_tree().process_frame` before using [get_meshes()](class_csgshape3d.md#class_CSGShape3D_method_get_meshes) in [Node._ready()](class_node.md#class_Node_private_method__ready) or after changing properties on the **CSGShape3D**.

---

<span id="class_CSGShape3D_method_is_root_shape"></span>

[bool](class_bool.md#class_bool) **is_root_shape** ( ) *const* [🔗](class_csgshape3d.md#class_CSGShape3D_method_is_root_shape)

Returns `true` if this is a root shape and is thus the object that is rendered.

---

<span id="class_CSGShape3D_method_set_collision_layer_value"></span>

void **set_collision_layer_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_csgshape3d.md#class_CSGShape3D_method_set_collision_layer_value)

Based on `value`, enables or disables the specified layer in the [collision_layer](class_csgshape3d.md#class_CSGShape3D_property_collision_layer), given a `layer_number` between 1 and 32.

---

<span id="class_CSGShape3D_method_set_collision_mask_value"></span>

void **set_collision_mask_value** ( layer_number: [int](class_int.md#class_int), value: [bool](class_bool.md#class_bool) ) [🔗](class_csgshape3d.md#class_CSGShape3D_method_set_collision_mask_value)

Based on `value`, enables or disables the specified layer in the [collision_mask](class_csgshape3d.md#class_CSGShape3D_property_collision_mask), given a `layer_number` between 1 and 32.
