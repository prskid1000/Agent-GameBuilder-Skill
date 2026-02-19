<span id="class_Bone2D"></span>

## Bone2D

**Inherits:** [Node2D](class_node2d.md#class_Node2D) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A joint used with [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) to control and animate other nodes.

### Description

A hierarchy of **Bone2D** s can be bound to a [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) to control and animate other [Node2D](class_node2d.md#class_Node2D) nodes.

You can use **Bone2D** and [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) nodes to animate 2D meshes created with the [Polygon2D](class_polygon2d.md#class_Polygon2D) UV editor.

Each bone has a [rest](class_bone2d.md#class_Bone2D_property_rest) transform that you can reset to with [apply_rest()](class_bone2d.md#class_Bone2D_method_apply_rest). These rest poses are relative to the bone's parent.

If in the editor, you can set the rest pose of an entire skeleton using a menu option, from the code, you need to iterate over the bones to set their individual rest poses.

### Properties


| [Transform2D](class_transform2d.md#class_Transform2D) | [rest](class_bone2d.md#class_Bone2D_property_rest) | `Transform2D(0, 0, 0, 0, 0, 0)` |
| --- | --- | --- |

### Methods


| void | [apply_rest](class_bone2d.md#class_Bone2D_method_apply_rest) ( ) |
| --- | --- |
| [bool](class_bool.md#class_bool) | [get_autocalculate_length_and_angle](class_bone2d.md#class_Bone2D_method_get_autocalculate_length_and_angle) ( ) const |
| [float](class_float.md#class_float) | [get_bone_angle](class_bone2d.md#class_Bone2D_method_get_bone_angle) ( ) const |
| [int](class_int.md#class_int) | [get_index_in_skeleton](class_bone2d.md#class_Bone2D_method_get_index_in_skeleton) ( ) const |
| [float](class_float.md#class_float) | [get_length](class_bone2d.md#class_Bone2D_method_get_length) ( ) const |
| [Transform2D](class_transform2d.md#class_Transform2D) | [get_skeleton_rest](class_bone2d.md#class_Bone2D_method_get_skeleton_rest) ( ) const |
| void | [set_autocalculate_length_and_angle](class_bone2d.md#class_Bone2D_method_set_autocalculate_length_and_angle) ( auto_calculate: [bool](class_bool.md#class_bool) ) |
| void | [set_bone_angle](class_bone2d.md#class_Bone2D_method_set_bone_angle) ( angle: [float](class_float.md#class_float) ) |
| void | [set_length](class_bone2d.md#class_Bone2D_method_set_length) ( length: [float](class_float.md#class_float) ) |

---

### Property Descriptions

<span id="class_Bone2D_property_rest"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **rest** = `Transform2D(0, 0, 0, 0, 0, 0)` [🔗](class_bone2d.md#class_Bone2D_property_rest)

- void **set_rest** ( value: [Transform2D](class_transform2d.md#class_Transform2D) )
- [Transform2D](class_transform2d.md#class_Transform2D) **get_rest** ( )

Rest transform of the bone. You can reset the node's transforms to this value using [apply_rest()](class_bone2d.md#class_Bone2D_method_apply_rest).

---

### Method Descriptions

<span id="class_Bone2D_method_apply_rest"></span>

void **apply_rest** ( ) [🔗](class_bone2d.md#class_Bone2D_method_apply_rest)

Resets the bone to the rest pose. This is equivalent to setting [Node2D.transform](class_node2d.md#class_Node2D_property_transform) to [rest](class_bone2d.md#class_Bone2D_property_rest).

---

<span id="class_Bone2D_method_get_autocalculate_length_and_angle"></span>

[bool](class_bool.md#class_bool) **get_autocalculate_length_and_angle** ( ) *const* [🔗](class_bone2d.md#class_Bone2D_method_get_autocalculate_length_and_angle)

Returns whether this **Bone2D** is going to autocalculate its length and bone angle using its first **Bone2D** child node, if one exists. If there are no **Bone2D** children, then it cannot autocalculate these values and will print a warning.

---

<span id="class_Bone2D_method_get_bone_angle"></span>

[float](class_float.md#class_float) **get_bone_angle** ( ) *const* [🔗](class_bone2d.md#class_Bone2D_method_get_bone_angle)

Returns the angle of the bone in the **Bone2D**.

 **Note:** This is different from the **Bone2D**'s rotation. The bone's angle is the rotation of the bone shown by the gizmo, which is unaffected by the **Bone2D**'s [Node2D.transform](class_node2d.md#class_Node2D_property_transform).

---

<span id="class_Bone2D_method_get_index_in_skeleton"></span>

[int](class_int.md#class_int) **get_index_in_skeleton** ( ) *const* [🔗](class_bone2d.md#class_Bone2D_method_get_index_in_skeleton)

Returns the node's index as part of the entire skeleton. See [Skeleton2D](class_skeleton2d.md#class_Skeleton2D).

---

<span id="class_Bone2D_method_get_length"></span>

[float](class_float.md#class_float) **get_length** ( ) *const* [🔗](class_bone2d.md#class_Bone2D_method_get_length)

Returns the length of the bone in the **Bone2D** node.

---

<span id="class_Bone2D_method_get_skeleton_rest"></span>

[Transform2D](class_transform2d.md#class_Transform2D) **get_skeleton_rest** ( ) *const* [🔗](class_bone2d.md#class_Bone2D_method_get_skeleton_rest)

Returns the node's [rest](class_bone2d.md#class_Bone2D_property_rest) [Transform2D](class_transform2d.md#class_Transform2D) if it doesn't have a parent, or its rest pose relative to its parent.

---

<span id="class_Bone2D_method_set_autocalculate_length_and_angle"></span>

void **set_autocalculate_length_and_angle** ( auto_calculate: [bool](class_bool.md#class_bool) ) [🔗](class_bone2d.md#class_Bone2D_method_set_autocalculate_length_and_angle)

When set to `true`, the **Bone2D** node will attempt to automatically calculate the bone angle and length using the first child **Bone2D** node, if one exists. If none exist, the **Bone2D** cannot automatically calculate these values and will print a warning.

---

<span id="class_Bone2D_method_set_bone_angle"></span>

void **set_bone_angle** ( angle: [float](class_float.md#class_float) ) [🔗](class_bone2d.md#class_Bone2D_method_set_bone_angle)

Sets the bone angle for the **Bone2D**. This is typically set to the rotation from the **Bone2D** to a child **Bone2D** node.

 **Note:** This is different from the **Bone2D**'s rotation. The bone's angle is the rotation of the bone shown by the gizmo, which is unaffected by the **Bone2D**'s [Node2D.transform](class_node2d.md#class_Node2D_property_transform).

---

<span id="class_Bone2D_method_set_length"></span>

void **set_length** ( length: [float](class_float.md#class_float) ) [🔗](class_bone2d.md#class_Bone2D_method_set_length)

Sets the length of the bone in the **Bone2D**.
