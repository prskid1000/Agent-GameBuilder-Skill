<span id="class_AnimationNodeAdd2"></span>

## AnimationNodeAdd2

**Inherits:** [AnimationNodeSync](class_animationnodesync.md#class_AnimationNodeSync) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Blends two animations additively inside of an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

### Description

A resource to add to an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree). Blends two animations additively based on the amount value.

If the amount is greater than `1.0`, the animation connected to "in" port is blended with the amplified animation connected to "add" port.

If the amount is less than `0.0`, the animation connected to "in" port is blended with the inverted animation connected to "add" port.

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)
