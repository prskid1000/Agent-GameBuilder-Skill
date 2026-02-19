<span id="class_AudioStreamInteractive"></span>

## AudioStreamInteractive

**Inherits:** [AudioStream](class_audiostream.md#class_AudioStream) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Audio stream that can playback music interactively, combining clips and a transition table.

### Description

This is an audio stream that can playback music interactively, combining clips and a transition table. Clips must be added first, and then the transition rules via the [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition). Additionally, this stream exports a property parameter to control the playback via [AudioStreamPlayer](class_audiostreamplayer.md#class_AudioStreamPlayer), [AudioStreamPlayer2D](class_audiostreamplayer2d.md#class_AudioStreamPlayer2D), or [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D).

The way this is used is by filling a number of clips, then configuring the transition table. From there, clips are selected for playback and the music will smoothly go from the current to the new one while using the corresponding transition rule defined in the transition table.

### Properties


| [int](class_int.md#class_int) | [clip_count](class_audiostreaminteractive.md#class_AudioStreamInteractive_property_clip_count) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [initial_clip](class_audiostreaminteractive.md#class_AudioStreamInteractive_property_initial_clip) | `0` |

### Methods


| void | [add_transition](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int), from_time: [TransitionFromTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionFromTime), to_time: [TransitionToTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionToTime), fade_mode: [FadeMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode), fade_beats: [float](class_float.md#class_float), use_filler_clip: [bool](class_bool.md#class_bool) = false, filler_clip: [int](class_int.md#class_int) = -1, hold_previous: [bool](class_bool.md#class_bool) = false ) |
| --- | --- |
| void | [erase_transition](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_erase_transition) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) |
| [AutoAdvanceMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_AutoAdvanceMode) | [get_clip_auto_advance](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_clip_auto_advance) ( clip_index: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_clip_auto_advance_next_clip](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_clip_auto_advance_next_clip) ( clip_index: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_clip_name](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_clip_name) ( clip_index: [int](class_int.md#class_int) ) const |
| [AudioStream](class_audiostream.md#class_AudioStream) | [get_clip_stream](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_clip_stream) ( clip_index: [int](class_int.md#class_int) ) const |
| [float](class_float.md#class_float) | [get_transition_fade_beats](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_fade_beats) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) const |
| [FadeMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode) | [get_transition_fade_mode](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_fade_mode) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_transition_filler_clip](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_filler_clip) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) const |
| [TransitionFromTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionFromTime) | [get_transition_from_time](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_from_time) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) const |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [get_transition_list](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_list) ( ) const |
| [TransitionToTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionToTime) | [get_transition_to_time](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_to_time) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [has_transition](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_has_transition) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_transition_holding_previous](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_is_transition_holding_previous) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_transition_using_filler_clip](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_is_transition_using_filler_clip) ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) const |
| void | [set_clip_auto_advance](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_set_clip_auto_advance) ( clip_index: [int](class_int.md#class_int), mode: [AutoAdvanceMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_AutoAdvanceMode) ) |
| void | [set_clip_auto_advance_next_clip](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_set_clip_auto_advance_next_clip) ( clip_index: [int](class_int.md#class_int), auto_advance_next_clip: [int](class_int.md#class_int) ) |
| void | [set_clip_name](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_set_clip_name) ( clip_index: [int](class_int.md#class_int), name: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_clip_stream](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_set_clip_stream) ( clip_index: [int](class_int.md#class_int), stream: [AudioStream](class_audiostream.md#class_AudioStream) ) |

---

### Enumerations

<span id="enum_AudioStreamInteractive_TransitionFromTime"></span>

enum **TransitionFromTime**: [🔗](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionFromTime)

<span id="class_AudioStreamInteractive_constant_TRANSITION_FROM_TIME_IMMEDIATE"></span>

[TransitionFromTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionFromTime) **TRANSITION_FROM_TIME_IMMEDIATE** = `0`

Start transition as soon as possible, don't wait for any specific time position.

<span id="class_AudioStreamInteractive_constant_TRANSITION_FROM_TIME_NEXT_BEAT"></span>

[TransitionFromTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionFromTime) **TRANSITION_FROM_TIME_NEXT_BEAT** = `1`

Transition when the clip playback position reaches the next beat.

<span id="class_AudioStreamInteractive_constant_TRANSITION_FROM_TIME_NEXT_BAR"></span>

[TransitionFromTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionFromTime) **TRANSITION_FROM_TIME_NEXT_BAR** = `2`

Transition when the clip playback position reaches the next bar.

<span id="class_AudioStreamInteractive_constant_TRANSITION_FROM_TIME_END"></span>

[TransitionFromTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionFromTime) **TRANSITION_FROM_TIME_END** = `3`

Transition when the current clip finished playing.

---

<span id="enum_AudioStreamInteractive_TransitionToTime"></span>

enum **TransitionToTime**: [🔗](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionToTime)

<span id="class_AudioStreamInteractive_constant_TRANSITION_TO_TIME_SAME_POSITION"></span>

[TransitionToTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionToTime) **TRANSITION_TO_TIME_SAME_POSITION** = `0`

Transition to the same position in the destination clip. This is useful when both clips have exactly the same length and the music should fade between them.

<span id="class_AudioStreamInteractive_constant_TRANSITION_TO_TIME_START"></span>

[TransitionToTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionToTime) **TRANSITION_TO_TIME_START** = `1`

Transition to the start of the destination clip.

---

<span id="enum_AudioStreamInteractive_FadeMode"></span>

enum **FadeMode**: [🔗](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode)

<span id="class_AudioStreamInteractive_constant_FADE_DISABLED"></span>

[FadeMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode) **FADE_DISABLED** = `0`

Do not use fade for the transition. This is useful when transitioning from a clip-end to clip-beginning, and each clip has their begin/end.

<span id="class_AudioStreamInteractive_constant_FADE_IN"></span>

[FadeMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode) **FADE_IN** = `1`

Use a fade-in in the next clip, let the current clip finish.

<span id="class_AudioStreamInteractive_constant_FADE_OUT"></span>

[FadeMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode) **FADE_OUT** = `2`

Use a fade-out in the current clip, the next clip will start by itself.

<span id="class_AudioStreamInteractive_constant_FADE_CROSS"></span>

[FadeMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode) **FADE_CROSS** = `3`

Use a cross-fade between clips.

<span id="class_AudioStreamInteractive_constant_FADE_AUTOMATIC"></span>

[FadeMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode) **FADE_AUTOMATIC** = `4`

Use automatic fade logic depending on the transition from/to. It is recommended to use this by default.

---

<span id="enum_AudioStreamInteractive_AutoAdvanceMode"></span>

enum **AutoAdvanceMode**: [🔗](class_audiostreaminteractive.md#enum_AudioStreamInteractive_AutoAdvanceMode)

<span id="class_AudioStreamInteractive_constant_AUTO_ADVANCE_DISABLED"></span>

[AutoAdvanceMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_AutoAdvanceMode) **AUTO_ADVANCE_DISABLED** = `0`

Disable auto-advance (default).

<span id="class_AudioStreamInteractive_constant_AUTO_ADVANCE_ENABLED"></span>

[AutoAdvanceMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_AutoAdvanceMode) **AUTO_ADVANCE_ENABLED** = `1`

Enable auto-advance, a clip must be specified.

<span id="class_AudioStreamInteractive_constant_AUTO_ADVANCE_RETURN_TO_HOLD"></span>

[AutoAdvanceMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_AutoAdvanceMode) **AUTO_ADVANCE_RETURN_TO_HOLD** = `2`

Enable auto-advance, but instead of specifying a clip, the playback will return to hold (see [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)).

---

### Constants

<span id="class_AudioStreamInteractive_constant_CLIP_ANY"></span>

**CLIP_ANY** = `-1` [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_constant_CLIP_ANY)

This constant describes that any clip is valid for a specific transition as either source or destination.

---

### Property Descriptions

<span id="class_AudioStreamInteractive_property_clip_count"></span>

[int](class_int.md#class_int) **clip_count** = `0` [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_property_clip_count)

- void **set_clip_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_clip_count** ( )

Amount of clips contained in this interactive player.

---

<span id="class_AudioStreamInteractive_property_initial_clip"></span>

[int](class_int.md#class_int) **initial_clip** = `0` [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_property_initial_clip)

- void **set_initial_clip** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_initial_clip** ( )

Index of the initial clip, which will be played first when this stream is played.

---

### Method Descriptions

<span id="class_AudioStreamInteractive_method_add_transition"></span>

void **add_transition** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int), from_time: [TransitionFromTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionFromTime), to_time: [TransitionToTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionToTime), fade_mode: [FadeMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode), fade_beats: [float](class_float.md#class_float), use_filler_clip: [bool](class_bool.md#class_bool) = false, filler_clip: [int](class_int.md#class_int) = -1, hold_previous: [bool](class_bool.md#class_bool) = false ) [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)

Add a transition between two clips. Provide the indices of the source and destination clips, or use the [CLIP_ANY](class_audiostreaminteractive.md#class_AudioStreamInteractive_constant_CLIP_ANY) constant to indicate that transition happens to/from any clip to this one.

\* `from_time` indicates the moment in the current clip the transition will begin after triggered.

\* `to_time` indicates the time in the next clip that the playback will start from.

\* `fade_mode` indicates how the fade will happen between clips. If unsure, just use [FADE_AUTOMATIC](class_audiostreaminteractive.md#class_AudioStreamInteractive_constant_FADE_AUTOMATIC) which uses the most common type of fade for each situation.

\* `fade_beats` indicates how many beats the fade will take. Using decimals is allowed.

\* `use_filler_clip` indicates that there will be a filler clip used between the source and destination clips.

\* `filler_clip` the index of the filler clip.

\* If `hold_previous` is used, then this clip will be remembered. This can be used together with [AUTO_ADVANCE_RETURN_TO_HOLD](class_audiostreaminteractive.md#class_AudioStreamInteractive_constant_AUTO_ADVANCE_RETURN_TO_HOLD) to return to this clip after another is done playing.

---

<span id="class_AudioStreamInteractive_method_erase_transition"></span>

void **erase_transition** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_erase_transition)

Erase a transition by providing `from_clip` and `to_clip` clip indices. [CLIP_ANY](class_audiostreaminteractive.md#class_AudioStreamInteractive_constant_CLIP_ANY) can be used for either argument or both.

---

<span id="class_AudioStreamInteractive_method_get_clip_auto_advance"></span>

[AutoAdvanceMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_AutoAdvanceMode) **get_clip_auto_advance** ( clip_index: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_clip_auto_advance)

Return whether a clip has auto-advance enabled. See [set_clip_auto_advance()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_set_clip_auto_advance).

---

<span id="class_AudioStreamInteractive_method_get_clip_auto_advance_next_clip"></span>

[int](class_int.md#class_int) **get_clip_auto_advance_next_clip** ( clip_index: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_clip_auto_advance_next_clip)

Return the clip towards which the clip referenced by `clip_index` will auto-advance to.

---

<span id="class_AudioStreamInteractive_method_get_clip_name"></span>

[StringName](class_stringname.md#class_StringName) **get_clip_name** ( clip_index: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_clip_name)

Return the name of a clip.

---

<span id="class_AudioStreamInteractive_method_get_clip_stream"></span>

[AudioStream](class_audiostream.md#class_AudioStream) **get_clip_stream** ( clip_index: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_clip_stream)

Return the [AudioStream](class_audiostream.md#class_AudioStream) associated with a clip.

---

<span id="class_AudioStreamInteractive_method_get_transition_fade_beats"></span>

[float](class_float.md#class_float) **get_transition_fade_beats** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_fade_beats)

Return the time (in beats) for a transition (see [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)).

---

<span id="class_AudioStreamInteractive_method_get_transition_fade_mode"></span>

[FadeMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_FadeMode) **get_transition_fade_mode** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_fade_mode)

Return the mode for a transition (see [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)).

---

<span id="class_AudioStreamInteractive_method_get_transition_filler_clip"></span>

[int](class_int.md#class_int) **get_transition_filler_clip** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_filler_clip)

Return the filler clip for a transition (see [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)).

---

<span id="class_AudioStreamInteractive_method_get_transition_from_time"></span>

[TransitionFromTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionFromTime) **get_transition_from_time** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_from_time)

Return the source time position for a transition (see [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)).

---

<span id="class_AudioStreamInteractive_method_get_transition_list"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **get_transition_list** ( ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_list)

Return the list of transitions (from, to interleaved).

---

<span id="class_AudioStreamInteractive_method_get_transition_to_time"></span>

[TransitionToTime](class_audiostreaminteractive.md#enum_AudioStreamInteractive_TransitionToTime) **get_transition_to_time** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_get_transition_to_time)

Return the destination time position for a transition (see [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)).

---

<span id="class_AudioStreamInteractive_method_has_transition"></span>

[bool](class_bool.md#class_bool) **has_transition** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_has_transition)

Returns `true` if a given transition exists (was added via [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)).

---

<span id="class_AudioStreamInteractive_method_is_transition_holding_previous"></span>

[bool](class_bool.md#class_bool) **is_transition_holding_previous** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_is_transition_holding_previous)

Return whether a transition uses the *hold previous* functionality (see [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)).

---

<span id="class_AudioStreamInteractive_method_is_transition_using_filler_clip"></span>

[bool](class_bool.md#class_bool) **is_transition_using_filler_clip** ( from_clip: [int](class_int.md#class_int), to_clip: [int](class_int.md#class_int) ) *const* [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_is_transition_using_filler_clip)

Return whether a transition uses the *filler clip* functionality (see [add_transition()](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_add_transition)).

---

<span id="class_AudioStreamInteractive_method_set_clip_auto_advance"></span>

void **set_clip_auto_advance** ( clip_index: [int](class_int.md#class_int), mode: [AutoAdvanceMode](class_audiostreaminteractive.md#enum_AudioStreamInteractive_AutoAdvanceMode) ) [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_set_clip_auto_advance)

Set whether a clip will auto-advance by changing the auto-advance mode.

---

<span id="class_AudioStreamInteractive_method_set_clip_auto_advance_next_clip"></span>

void **set_clip_auto_advance_next_clip** ( clip_index: [int](class_int.md#class_int), auto_advance_next_clip: [int](class_int.md#class_int) ) [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_set_clip_auto_advance_next_clip)

Set the index of the next clip towards which this clip will auto advance to when finished. If the clip being played loops, then auto-advance will be ignored.

---

<span id="class_AudioStreamInteractive_method_set_clip_name"></span>

void **set_clip_name** ( clip_index: [int](class_int.md#class_int), name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_set_clip_name)

Set the name of the current clip (for easier identification).

---

<span id="class_AudioStreamInteractive_method_set_clip_stream"></span>

void **set_clip_stream** ( clip_index: [int](class_int.md#class_int), stream: [AudioStream](class_audiostream.md#class_AudioStream) ) [🔗](class_audiostreaminteractive.md#class_AudioStreamInteractive_method_set_clip_stream)

Set the [AudioStream](class_audiostream.md#class_AudioStream) associated with the current clip.
