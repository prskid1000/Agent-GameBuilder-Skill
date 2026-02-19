<span id="class_AnimationRootNode"></span>

## AnimationRootNode

**Inherits:** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AnimationNodeAnimation](class_animationnodeanimation.md#class_AnimationNodeAnimation), [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D), [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class_AnimationNodeStateMachine)

Base class for [AnimationNode](class_animationnode.md#class_AnimationNode) s that hold one or multiple composite animations. Usually used for [AnimationTree.tree_root](class_animationtree.md#class_AnimationTree_property_tree_root).

### Description

**AnimationRootNode** is a base class for [AnimationNode](class_animationnode.md#class_AnimationNode) s that hold a complete animation. A complete animation refers to the output of an [AnimationNodeOutput](class_animationnodeoutput.md#class_AnimationNodeOutput) in an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree) or the output of another **AnimationRootNode**. Used for [AnimationTree.tree_root](class_animationtree.md#class_AnimationTree_property_tree_root) or in other **AnimationRootNode** s.

Examples of built-in root nodes include [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree) (allows blending nodes between each other using various modes), [AnimationNodeStateMachine](class_animationnodestatemachine.md#class_AnimationNodeStateMachine) (allows to configure blending and transitions between nodes using a state machine pattern), [AnimationNodeBlendSpace2D](class_animationnodeblendspace2d.md#class_AnimationNodeBlendSpace2D) (allows linear blending between **three** [AnimationNode](class_animationnode.md#class_AnimationNode) s), [AnimationNodeBlendSpace1D](class_animationnodeblendspace1d.md#class_AnimationNodeBlendSpace1D) (allows linear blending only between **two** [AnimationNode](class_animationnode.md#class_AnimationNode) s).

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
