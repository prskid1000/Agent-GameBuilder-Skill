<span id="class_CollisionPolygon3D"></span>

## CollisionPolygon3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node that provides a thickened polygon shape (a prism) to a [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D) parent.

### Description

A node that provides a thickened polygon shape (a prism) to a [CollisionObject3D](class_collisionobject3d.md#class_CollisionObject3D) parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an [Area3D](class_area3d.md#class_Area3D) or turn a [PhysicsBody3D](class_physicsbody3d.md#class_PhysicsBody3D) into a solid object.

 **Warning:** A non-uniformly scaled [CollisionShape3D](class_collisionshape3d.md#class_CollisionShape3D) will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its shape resource instead.

### Properties


| [Color](class_color.md#class_Color) | [debug_color](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_debug_color) | `Color(0, 0, 0, 0)` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [debug_fill](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_debug_fill) | `true` |
| [float](class_float.md#class_float) | [depth](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_depth) | `1.0` |
| [bool](class_bool.md#class_bool) | [disabled](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_disabled) | `false` |
| [float](class_float.md#class_float) | [margin](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_margin) | `0.04` |
| [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) | [polygon](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_polygon) | `PackedVector2Array()` |

---

### Property Descriptions

<span id="class_CollisionPolygon3D_property_debug_color"></span>

[Color](class_color.md#class_Color) **debug_color** = `Color(0, 0, 0, 0)` [🔗](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_debug_color)

- void **set_debug_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_debug_color** ( )

The collision shape color that is displayed in the editor, or in the running project if **Debug > Visible Collision Shapes** is checked at the top of the editor.

 **Note:** The default value is ProjectSettings.debug/shapes/collision/shape_color. The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.

---

<span id="class_CollisionPolygon3D_property_debug_fill"></span>

[bool](class_bool.md#class_bool) **debug_fill** = `true` [🔗](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_debug_fill)

- void **set_enable_debug_fill** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enable_debug_fill** ( )

If `true`, when the shape is displayed, it will show a solid fill color in addition to its wireframe.

---

<span id="class_CollisionPolygon3D_property_depth"></span>

[float](class_float.md#class_float) **depth** = `1.0` [🔗](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_depth)

- void **set_depth** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_depth** ( )

Length that the resulting collision extends in either direction perpendicular to its 2D polygon.

---

<span id="class_CollisionPolygon3D_property_disabled"></span>

[bool](class_bool.md#class_bool) **disabled** = `false` [🔗](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_disabled)

- void **set_disabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_disabled** ( )

If `true`, no collision will be produced. This property should be changed with [Object.set_deferred()](class_object.md#class_Object_method_set_deferred).

---

<span id="class_CollisionPolygon3D_property_margin"></span>

[float](class_float.md#class_float) **margin** = `0.04` [🔗](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_margin)

- void **set_margin** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_margin** ( )

The collision margin for the generated [Shape3D](class_shape3d.md#class_Shape3D). See [Shape3D.margin](class_shape3d.md#class_Shape3D_property_margin) for more details.

---

<span id="class_CollisionPolygon3D_property_polygon"></span>

[PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **polygon** = `PackedVector2Array()` [🔗](class_collisionpolygon3d.md#class_CollisionPolygon3D_property_polygon)

- void **set_polygon** ( value: [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) )
- [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) **get_polygon** ( )

Array of vertices which define the 2D polygon in the local XY plane.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array](class_packedvector2array.md#class_PackedVector2Array) for more details.
