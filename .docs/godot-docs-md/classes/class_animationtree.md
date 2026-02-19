<span id="class_AnimationTree"></span>

## AnimationTree

**Inherits:** [AnimationMixer](class_animationmixer.md#class_AnimationMixer) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A node used for advanced animation transitions in an [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer).

### Description

A node used for advanced animation transitions in an [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer).

 **Note:** When linked with an [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer), several properties and methods of the corresponding [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer) will not function as expected. Playback and transitions should be handled using only the **AnimationTree** and its constituent [AnimationNode](class_animationnode.md#class_AnimationNode) (s). The [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer) node should be used solely for adding, deleting, and editing animations.

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

- Third Person Shooter (TPS) Demo

### Properties


| [NodePath](class_nodepath.md#class_NodePath) | [advance_expression_base_node](class_animationtree.md#class_AnimationTree_property_advance_expression_base_node) | `NodePath(".")` |
| --- | --- | --- |
| [NodePath](class_nodepath.md#class_NodePath) | [anim_player](class_animationtree.md#class_AnimationTree_property_anim_player) | `NodePath("")` |
| [AnimationCallbackModeDiscrete](class_animationmixer.md#enum_AnimationMixer_AnimationCallbackModeDiscrete) | callback_mode_discrete | `2` (overrides [AnimationMixer](class_animationmixer.md#class_AnimationMixer_property_callback_mode_discrete)) |
| [bool](class_bool.md#class_bool) | deterministic | `true` (overrides [AnimationMixer](class_animationmixer.md#class_AnimationMixer_property_deterministic)) |
| [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) | [tree_root](class_animationtree.md#class_AnimationTree_property_tree_root) |

### Methods


| [AnimationProcessCallback](class_animationtree.md#enum_AnimationTree_AnimationProcessCallback) | [get_process_callback](class_animationtree.md#class_AnimationTree_method_get_process_callback) ( ) const |
| --- | --- |
| void | [set_process_callback](class_animationtree.md#class_AnimationTree_method_set_process_callback) ( mode: [AnimationProcessCallback](class_animationtree.md#enum_AnimationTree_AnimationProcessCallback) ) |

---

### Signals

<span id="class_AnimationTree_signal_animation_player_changed"></span>

**animation_player_changed** ( ) [🔗](class_animationtree.md#class_AnimationTree_signal_animation_player_changed)

Emitted when the [anim_player](class_animationtree.md#class_AnimationTree_property_anim_player) is changed.

---

### Enumerations

<span id="enum_AnimationTree_AnimationProcessCallback"></span>

enum **AnimationProcessCallback**: [🔗](class_animationtree.md#enum_AnimationTree_AnimationProcessCallback)

<span id="class_AnimationTree_constant_ANIMATION_PROCESS_PHYSICS"></span>

[AnimationProcessCallback](class_animationtree.md#enum_AnimationTree_AnimationProcessCallback) **ANIMATION_PROCESS_PHYSICS** = `0`

**Deprecated:** See [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS](class_animationmixer.md#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS).

<span id="class_AnimationTree_constant_ANIMATION_PROCESS_IDLE"></span>

[AnimationProcessCallback](class_animationtree.md#enum_AnimationTree_AnimationProcessCallback) **ANIMATION_PROCESS_IDLE** = `1`

**Deprecated:** See [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_IDLE](class_animationmixer.md#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_IDLE).

<span id="class_AnimationTree_constant_ANIMATION_PROCESS_MANUAL"></span>

[AnimationProcessCallback](class_animationtree.md#enum_AnimationTree_AnimationProcessCallback) **ANIMATION_PROCESS_MANUAL** = `2`

**Deprecated:** See [AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_MANUAL](class_animationmixer.md#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_MANUAL).

---

### Property Descriptions

<span id="class_AnimationTree_property_advance_expression_base_node"></span>

[NodePath](class_nodepath.md#class_NodePath) **advance_expression_base_node** = `NodePath(".")` [🔗](class_animationtree.md#class_AnimationTree_property_advance_expression_base_node)

- void **set_advance_expression_base_node** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_advance_expression_base_node** ( )

The path to the [Node](class_node.md#class_Node) used to evaluate the [AnimationNode](class_animationnode.md#class_AnimationNode) [Expression](class_expression.md#class_Expression) if one is not explicitly specified internally.

---

<span id="class_AnimationTree_property_anim_player"></span>

[NodePath](class_nodepath.md#class_NodePath) **anim_player** = `NodePath("")` [🔗](class_animationtree.md#class_AnimationTree_property_anim_player)

- void **set_animation_player** ( value: [NodePath](class_nodepath.md#class_NodePath) )
- [NodePath](class_nodepath.md#class_NodePath) **get_animation_player** ( )

The path to the [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer) used for animating.

---

<span id="class_AnimationTree_property_tree_root"></span>

[AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) **tree_root** [🔗](class_animationtree.md#class_AnimationTree_property_tree_root)

- void **set_tree_root** ( value: [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) )
- [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode) **get_tree_root** ( )

The root animation node of this **AnimationTree**. See [AnimationRootNode](class_animationrootnode.md#class_AnimationRootNode).

---

### Method Descriptions

<span id="class_AnimationTree_method_get_process_callback"></span>

[AnimationProcessCallback](class_animationtree.md#enum_AnimationTree_AnimationProcessCallback) **get_process_callback** ( ) *const* [🔗](class_animationtree.md#class_AnimationTree_method_get_process_callback)

**Deprecated:** Use [AnimationMixer.callback_mode_process](class_animationmixer.md#class_AnimationMixer_property_callback_mode_process) instead.

Returns the process notification in which to update animations.

---

<span id="class_AnimationTree_method_set_process_callback"></span>

void **set_process_callback** ( mode: [AnimationProcessCallback](class_animationtree.md#enum_AnimationTree_AnimationProcessCallback) ) [🔗](class_animationtree.md#class_AnimationTree_method_set_process_callback)

**Deprecated:** Use [AnimationMixer.callback_mode_process](class_animationmixer.md#class_AnimationMixer_property_callback_mode_process) instead.

Sets the process notification in which to update animations.
