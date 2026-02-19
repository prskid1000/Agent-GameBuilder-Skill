<span id="class_AnimationNodeSync"></span>

## AnimationNodeSync

**Inherits:** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AnimationNodeAdd2](class_animationnodeadd2.md#class_AnimationNodeAdd2), [AnimationNodeAdd3](class_animationnodeadd3.md#class_AnimationNodeAdd3), [AnimationNodeBlend2](class_animationnodeblend2.md#class_AnimationNodeBlend2), [AnimationNodeBlend3](class_animationnodeblend3.md#class_AnimationNodeBlend3), [AnimationNodeOneShot](class_animationnodeoneshot.md#class_AnimationNodeOneShot), [AnimationNodeSub2](class_animationnodesub2.md#class_AnimationNodeSub2), [AnimationNodeTransition](class_animationnodetransition.md#class_AnimationNodeTransition)

Base class for [AnimationNode](class_animationnode.md#class_AnimationNode) s with multiple input ports that must be synchronized.

### Description

An animation node used to combine, mix, or blend two or more animations together while keeping them synchronized within an [AnimationTree](class_animationtree.md#class_AnimationTree).

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

### Properties


| [bool](class_bool.md#class_bool) | [sync](class_animationnodesync.md#class_AnimationNodeSync_property_sync) | `false` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_AnimationNodeSync_property_sync"></span>

[bool](class_bool.md#class_bool) **sync** = `false` [🔗](class_animationnodesync.md#class_AnimationNodeSync_property_sync)

- void **set_use_sync** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_using_sync** ( )

If `false`, the blended animations' frame are stopped when the blend value is `0`.

If `true`, forcing the blended animations to advance frame.
