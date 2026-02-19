<span id="class_AnimationNodeBlend3"></span>

## AnimationNodeBlend3

**Inherits:** [AnimationNodeSync](class_animationnodesync.md#class_AnimationNodeSync) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Blends two of three animations linearly inside of an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

### Description

A resource to add to an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree). Blends two animations out of three linearly out of three based on the amount value.

This animation node has three inputs:

- The base animation to blend with

- A "-blend" animation to blend with when the blend amount is negative value

- A "+blend" animation to blend with when the blend amount is positive value

In general, the blend value should be in the `[-1.0, 1.0]` range. Values outside of this range can blend amplified animations, however, [AnimationNodeAdd3](class_animationnodeadd3.md#class_AnimationNodeAdd3) works better for this purpose.

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
