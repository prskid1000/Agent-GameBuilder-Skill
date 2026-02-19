<span id="class_AnimationNodeTimeSeek"></span>

## AnimationNodeTimeSeek

**Inherits:** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A time-seeking animation node used in [AnimationTree](class_animationtree.md#class_AnimationTree).

### Description

This animation node can be used to cause a seek command to happen to any sub-children of the animation graph. Use to play an [Animation](class_animation.md#class_Animation) from the start or a certain playback position inside the [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

After setting the time and changing the animation playback, the time seek node automatically goes into sleep mode on the next process frame by setting its `seek_request` value to `-1.0`.

.. tabs::

```
```

    # Play child animation from the start.
    animation_tree.set("parameters/TimeSeek/seek_request", 0.0)
    # Alternative syntax (same result as above).
    animation_tree["parameters/TimeSeek/seek_request"] = 0.0

    # Play child animation from 12 second timestamp.
    animation_tree.set("parameters/TimeSeek/seek_request", 12.0)
    # Alternative syntax (same result as above).
    animation_tree["parameters/TimeSeek/seek_request"] = 12.0

```
```

    // Play child animation from the start.
    animationTree.Set("parameters/TimeSeek/seek_request", 0.0);

    // Play child animation from 12 second timestamp.
    animationTree.Set("parameters/TimeSeek/seek_request", 12.0);

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

### Properties


| [bool](class_bool.md#class_bool) | [explicit_elapse](class_animationnodetimeseek.md#class_AnimationNodeTimeSeek_property_explicit_elapse) | `true` |
| --- | --- | --- |

---

### Property Descriptions

<span id="class_AnimationNodeTimeSeek_property_explicit_elapse"></span>

[bool](class_bool.md#class_bool) **explicit_elapse** = `true` [🔗](class_animationnodetimeseek.md#class_AnimationNodeTimeSeek_property_explicit_elapse)

- void **set_explicit_elapse** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_explicit_elapse** ( )

If `true`, some processes are executed to handle keys between seeks, such as calculating root motion and finding the nearest discrete key.
