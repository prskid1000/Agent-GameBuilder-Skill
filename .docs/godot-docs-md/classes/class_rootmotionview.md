<span id="class_RootMotionView"></span>

## RootMotionView

**Inherits:** [VisualInstance3D](class_visualinstance3d.md#class_VisualInstance3D) **<** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Editor-only helper for setting up root motion in [AnimationMixer](class_animationmixer.md#class_AnimationMixer).

### Description

*Root motion* refers to an animation technique where a mesh's skeleton is used to give impulse to a character. When working with 3D animations, a popular technique is for animators to use the root skeleton bone to give motion to the rest of the skeleton. This allows animating characters in a way where steps actually match the floor below. It also allows precise interaction with objects during cinematics. See also [AnimationMixer](class_animationmixer.md#class_AnimationMixer).

 **Note:** **RootMotionView** is only visible in the editor. It will be hidden automatically in the running project.

### Tutorials

- `Using AnimationTree - Root motion <../tutorials/animation/animation_tree.html#root-motion>`__

### Properties


| [NodePath](class_nodepath.md#class_NodePath) | [animation_path](class_rootmotionview.md#class_RootMotionView_property_animation_path) | `NodePath("")` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [cell_size](class_rootmotionview.md#class_RootMotionView_property_cell_size) | `1.0` |
| [Color](class_color.md#class_Color) | [color](class_rootmotionview.md#class_RootMotionView_property_color) | `Color(0.5, 0.5, 1, 1)` |
| [float](class_float.md#class_float) | [radius](class_rootmotionview.md#class_RootMotionView_property_radius) | `10.0` |
| [bool](class_bool.md#class_bool) | [zero_y](class_rootmotionview.md#class_RootMotionView_property_zero_y) | `true` |

---

### Property Descriptions

<span id="class_RootMotionView_property_animation_path"></span>

[NodePath](class_nodepath.md#class_NodePath) **animation_path** = `NodePath("")` [🔗](class_rootmotionview.md#class_RootMotionView_property_animation_path)

- void **set_animation_path** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_animation_path** ( )

Path to an [AnimationMixer](class_animationmixer.md#class_AnimationMixer) node to use as a basis for root motion.

---

<span id="class_RootMotionView_property_cell_size"></span>

[float](class_float.md#class_float) **cell_size** = `1.0` [🔗](class_rootmotionview.md#class_RootMotionView_property_cell_size)

- void **set_cell_size** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_cell_size** ( )

The grid's cell size in 3D units.

---

<span id="class_RootMotionView_property_color"></span>

[Color](class_color.md#class_Color) **color** = `Color(0.5, 0.5, 1, 1)` [🔗](class_rootmotionview.md#class_RootMotionView_property_color)

- void **set_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_color** ( )

The grid's color.

---

<span id="class_RootMotionView_property_radius"></span>

[float](class_float.md#class_float) **radius** = `10.0` [🔗](class_rootmotionview.md#class_RootMotionView_property_radius)

- void **set_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_radius** ( )

The grid's radius in 3D units. The grid's opacity will fade gradually as the distance from the origin increases until this [radius](class_rootmotionview.md#class_RootMotionView_property_radius) is reached.

---

<span id="class_RootMotionView_property_zero_y"></span>

[bool](class_bool.md#class_bool) **zero_y** = `true` [🔗](class_rootmotionview.md#class_RootMotionView_property_zero_y)

- void **set_zero_y** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_zero_y** ( )

If `true`, the grid's points will all be on the same Y coordinate (*local* Y = 0). If `false`, the points' original Y coordinate is preserved.
