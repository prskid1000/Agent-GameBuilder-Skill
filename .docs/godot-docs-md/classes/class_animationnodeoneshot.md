<span id="class_AnimationNodeOneShot"></span>

## AnimationNodeOneShot

**Inherits:** [AnimationNodeSync](class_animationnodesync.md#class_AnimationNodeSync) **<** [AnimationNode](class_animationnode.md#class_AnimationNode) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Plays an animation once in an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree).

### Description

A resource to add to an [AnimationNodeBlendTree](class_animationnodeblendtree.md#class_AnimationNodeBlendTree). This animation node will execute a sub-animation and return once it finishes. Blend times for fading in and out can be customized, as well as filters.

After setting the request and changing the animation playback, the one-shot node automatically clears the request on the next process frame by setting its `request` value to [ONE_SHOT_REQUEST_NONE](class_animationnodeoneshot.md#class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_NONE).

.. tabs::

```
```

    # Play child animation connected to "shot" port.
    animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE)
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE

    # Abort child animation connected to "shot" port.
    animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT)
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT

    # Abort child animation with fading out connected to "shot" port.
    animation_tree.set("parameters/OneShot/request", AnimationNodeOneShot.ONE_SHOT_REQUEST_FADE_OUT)
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/request"] = AnimationNodeOneShot.ONE_SHOT_REQUEST_FADE_OUT

    # Get current state (read-only).
    animation_tree.get("parameters/OneShot/active")
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/active"]

    # Get current internal state (read-only).
    animation_tree.get("parameters/OneShot/internal_active")
    # Alternative syntax (same result as above).
    animation_tree["parameters/OneShot/internal_active"]

```
```

    // Play child animation connected to "shot" port.
    animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.Fire);

    // Abort child animation connected to "shot" port.
    animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.Abort);

    // Abort child animation with fading out connected to "shot" port.
    animationTree.Set("parameters/OneShot/request", (int)AnimationNodeOneShot.OneShotRequest.FadeOut);

    // Get current state (read-only).
    animationTree.Get("parameters/OneShot/active");

    // Get current internal state (read-only).
    animationTree.Get("parameters/OneShot/internal_active");

### Tutorials

- [Using AnimationTree](../tutorials/animation/animation_tree.md)

- Third Person Shooter (TPS) Demo

### Properties


| [bool](class_bool.md#class_bool) | [abort_on_reset](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_abort_on_reset) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [autorestart](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_autorestart) | `false` |
| [float](class_float.md#class_float) | [autorestart_delay](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_autorestart_delay) | `1.0` |
| [float](class_float.md#class_float) | [autorestart_random_delay](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_autorestart_random_delay) | `0.0` |
| [bool](class_bool.md#class_bool) | [break_loop_at_end](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_break_loop_at_end) | `false` |
| [Curve](class_curve.md#class_Curve) | [fadein_curve](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_fadein_curve) |
| [float](class_float.md#class_float) | [fadein_time](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_fadein_time) | `0.0` |
| [Curve](class_curve.md#class_Curve) | [fadeout_curve](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_fadeout_curve) |
| [float](class_float.md#class_float) | [fadeout_time](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_fadeout_time) | `0.0` |
| [MixMode](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_MixMode) | [mix_mode](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_mix_mode) | `0` |

---

### Enumerations

<span id="enum_AnimationNodeOneShot_OneShotRequest"></span>

enum **OneShotRequest**: [🔗](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_OneShotRequest)

<span id="class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_NONE"></span>

[OneShotRequest](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_OneShotRequest) **ONE_SHOT_REQUEST_NONE** = `0`

The default state of the request. Nothing is done.

<span id="class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FIRE"></span>

[OneShotRequest](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_OneShotRequest) **ONE_SHOT_REQUEST_FIRE** = `1`

The request to play the animation connected to "shot" port.

<span id="class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_ABORT"></span>

[OneShotRequest](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_OneShotRequest) **ONE_SHOT_REQUEST_ABORT** = `2`

The request to stop the animation connected to "shot" port.

<span id="class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FADE_OUT"></span>

[OneShotRequest](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_OneShotRequest) **ONE_SHOT_REQUEST_FADE_OUT** = `3`

The request to fade out the animation connected to "shot" port.

---

<span id="enum_AnimationNodeOneShot_MixMode"></span>

enum **MixMode**: [🔗](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_MixMode)

<span id="class_AnimationNodeOneShot_constant_MIX_MODE_BLEND"></span>

[MixMode](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_MixMode) **MIX_MODE_BLEND** = `0`

Blends two animations. See also [AnimationNodeBlend2](class_animationnodeblend2.md#class_AnimationNodeBlend2).

<span id="class_AnimationNodeOneShot_constant_MIX_MODE_ADD"></span>

[MixMode](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_MixMode) **MIX_MODE_ADD** = `1`

Blends two animations additively. See also [AnimationNodeAdd2](class_animationnodeadd2.md#class_AnimationNodeAdd2).

---

### Property Descriptions

<span id="class_AnimationNodeOneShot_property_abort_on_reset"></span>

[bool](class_bool.md#class_bool) **abort_on_reset** = `false` [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_abort_on_reset)

- void **set_abort_on_reset** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_aborted_on_reset** ( )

If `true`, the sub-animation will abort if resumed with a reset after a prior interruption.

---

<span id="class_AnimationNodeOneShot_property_autorestart"></span>

[bool](class_bool.md#class_bool) **autorestart** = `false` [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_autorestart)

- void **set_autorestart** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **has_autorestart** ( )

If `true`, the sub-animation will restart automatically after finishing.

In other words, to start auto restarting, the animation must be played once with the [ONE_SHOT_REQUEST_FIRE](class_animationnodeoneshot.md#class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FIRE) request. The [ONE_SHOT_REQUEST_ABORT](class_animationnodeoneshot.md#class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_ABORT) request stops the auto restarting, but it does not disable the [autorestart](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_autorestart) itself. So, the [ONE_SHOT_REQUEST_FIRE](class_animationnodeoneshot.md#class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FIRE) request will start auto restarting again.

---

<span id="class_AnimationNodeOneShot_property_autorestart_delay"></span>

[float](class_float.md#class_float) **autorestart_delay** = `1.0` [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_autorestart_delay)

- void **set_autorestart_delay** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_autorestart_delay** ( )

The delay after which the automatic restart is triggered, in seconds.

---

<span id="class_AnimationNodeOneShot_property_autorestart_random_delay"></span>

[float](class_float.md#class_float) **autorestart_random_delay** = `0.0` [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_autorestart_random_delay)

- void **set_autorestart_random_delay** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_autorestart_random_delay** ( )

If [autorestart](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_autorestart) is `true`, a random additional delay (in seconds) between 0 and this value will be added to [autorestart_delay](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_autorestart_delay).

---

<span id="class_AnimationNodeOneShot_property_break_loop_at_end"></span>

[bool](class_bool.md#class_bool) **break_loop_at_end** = `false` [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_break_loop_at_end)

- void **set_break_loop_at_end** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_loop_broken_at_end** ( )

If `true`, breaks the loop at the end of the loop cycle for transition, even if the animation is looping.

---

<span id="class_AnimationNodeOneShot_property_fadein_curve"></span>

[Curve](class_curve.md#class_Curve) **fadein_curve** [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_fadein_curve)

- void **set_fadein_curve** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_fadein_curve** ( )

Determines how cross-fading between animations is eased. If empty, the transition will be linear. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_AnimationNodeOneShot_property_fadein_time"></span>

[float](class_float.md#class_float) **fadein_time** = `0.0` [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_fadein_time)

- void **set_fadein_time** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fadein_time** ( )

The fade-in duration. For example, setting this to `1.0` for a 5 second length animation will produce a cross-fade that starts at 0 second and ends at 1 second during the animation.

 **Note:** **AnimationNodeOneShot** transitions the current state after the fading has finished.

---

<span id="class_AnimationNodeOneShot_property_fadeout_curve"></span>

[Curve](class_curve.md#class_Curve) **fadeout_curve** [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_fadeout_curve)

- void **set_fadeout_curve** ( value: [Curve](class_curve.md#class_Curve) )
- [Curve](class_curve.md#class_Curve) **get_fadeout_curve** ( )

Determines how cross-fading between animations is eased. If empty, the transition will be linear. Should be a unit [Curve](class_curve.md#class_Curve).

---

<span id="class_AnimationNodeOneShot_property_fadeout_time"></span>

[float](class_float.md#class_float) **fadeout_time** = `0.0` [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_fadeout_time)

- void **set_fadeout_time** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_fadeout_time** ( )

The fade-out duration. For example, setting this to `1.0` for a 5 second length animation will produce a cross-fade that starts at 4 second and ends at 5 second during the animation.

 **Note:** **AnimationNodeOneShot** transitions the current state after the fading has finished.

---

<span id="class_AnimationNodeOneShot_property_mix_mode"></span>

[MixMode](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_MixMode) **mix_mode** = `0` [🔗](class_animationnodeoneshot.md#class_AnimationNodeOneShot_property_mix_mode)

- void **set_mix_mode** ( value: [MixMode](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_MixMode) )
- [MixMode](class_animationnodeoneshot.md#enum_AnimationNodeOneShot_MixMode) **get_mix_mode** ( )

The blend type.
