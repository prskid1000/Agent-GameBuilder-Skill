<span id="class_AnimationNodeBlend2"></span>

## AnimationNodeBlend2

**Inherits:** [AnimationNodeSync](class_animationnodesync.md#class_AnimationNodeSync) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Blends two animations linearly inside of an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

### Description

A resource to add to an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree). Blends two animations linearly based on the amount value.

In general, the blend value should be in the `[0.0, 1.0]` range. Values outside of this range can blend amplified or inverted animations, however, [AnimationNodeAdd2](class_animationnodeadd2.md#class_AnimationNodeAdd2) works better for this purpose.

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

- 3D Platformer Demo

- Third Person Shooter (TPS) Demo
