<span id="class_AnimationLibrary"></span>

## AnimationLibrary

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Container for [Animation](class_animation.md#class_Animation) resources.

### Description

An animation library stores a set of animations accessible through [StringName](class_stringname.md#class_StringName) keys, for use with [AnimationPlayer](class_animationplayer.md#class_AnimationPlayer) nodes.

### Tutorials

- [Animation tutorial index](../tutorials/animation/index.md)

### Methods


| Error | [add_animation](class_animationlibrary.md#class_AnimationLibrary_method_add_animation) ( name: [StringName](class_stringname.md#class_StringName), animation: [Animation](class_animation.md#class_Animation) ) |
| --- | --- |
| [Animation](class_animation.md#class_Animation) | [get_animation](class_animationlibrary.md#class_AnimationLibrary_method_get_animation) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| [Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] | [get_animation_list](class_animationlibrary.md#class_AnimationLibrary_method_get_animation_list) ( ) const |
| [int](class_int.md#class_int) | [get_animation_list_size](class_animationlibrary.md#class_AnimationLibrary_method_get_animation_list_size) ( ) const |
| [bool](class_bool.md#class_bool) | [has_animation](class_animationlibrary.md#class_AnimationLibrary_method_has_animation) ( name: [StringName](class_stringname.md#class_StringName) ) const |
| void | [remove_animation](class_animationlibrary.md#class_AnimationLibrary_method_remove_animation) ( name: [StringName](class_stringname.md#class_StringName) ) |
| void | [rename_animation](class_animationlibrary.md#class_AnimationLibrary_method_rename_animation) ( name: [StringName](class_stringname.md#class_StringName), newname: [StringName](class_stringname.md#class_StringName) ) |

---

### Signals

<span id="class_AnimationLibrary_signal_animation_added"></span>

**animation_added** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationlibrary.md#class_AnimationLibrary_signal_animation_added)

Emitted when an [Animation](class_animation.md#class_Animation) is added, under the key `name`.

---

<span id="class_AnimationLibrary_signal_animation_changed"></span>

**animation_changed** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationlibrary.md#class_AnimationLibrary_signal_animation_changed)

Emitted when there's a change in one of the animations, e.g. tracks are added, moved or have changed paths. `name` is the key of the animation that was changed.

See also [Resource.changed](class_resource.md#class_Resource_signal_changed), which this acts as a relay for.

---

<span id="class_AnimationLibrary_signal_animation_removed"></span>

**animation_removed** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationlibrary.md#class_AnimationLibrary_signal_animation_removed)

Emitted when an [Animation](class_animation.md#class_Animation) stored with the key `name` is removed.

---

<span id="class_AnimationLibrary_signal_animation_renamed"></span>

**animation_renamed** ( name: [StringName](class_stringname.md#class_StringName), to_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationlibrary.md#class_AnimationLibrary_signal_animation_renamed)

Emitted when the key for an [Animation](class_animation.md#class_Animation) is changed, from `name` to `to_name`.

---

### Method Descriptions

<span id="class_AnimationLibrary_method_add_animation"></span>

Error **add_animation** ( name: [StringName](class_stringname.md#class_StringName), animation: [Animation](class_animation.md#class_Animation) ) [🔗](class_animationlibrary.md#class_AnimationLibrary_method_add_animation)

Adds the `animation` to the library, accessible by the key `name`.

---

<span id="class_AnimationLibrary_method_get_animation"></span>

[Animation](class_animation.md#class_Animation) **get_animation** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationlibrary.md#class_AnimationLibrary_method_get_animation)

Returns the [Animation](class_animation.md#class_Animation) with the key `name`. If the animation does not exist, `null` is returned and an error is logged.

---

<span id="class_AnimationLibrary_method_get_animation_list"></span>

[Array](class_array.md#class_Array)\[[StringName](class_stringname.md#class_StringName)\] **get_animation_list** ( ) *const* [🔗](class_animationlibrary.md#class_AnimationLibrary_method_get_animation_list)

Returns the keys for the [Animation](class_animation.md#class_Animation) s stored in the library.

---

<span id="class_AnimationLibrary_method_get_animation_list_size"></span>

[int](class_int.md#class_int) **get_animation_list_size** ( ) *const* [🔗](class_animationlibrary.md#class_AnimationLibrary_method_get_animation_list_size)

Returns the key count for the [Animation](class_animation.md#class_Animation) s stored in the library.

---

<span id="class_AnimationLibrary_method_has_animation"></span>

[bool](class_bool.md#class_bool) **has_animation** ( name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_animationlibrary.md#class_AnimationLibrary_method_has_animation)

Returns `true` if the library stores an [Animation](class_animation.md#class_Animation) with `name` as the key.

---

<span id="class_AnimationLibrary_method_remove_animation"></span>

void **remove_animation** ( name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationlibrary.md#class_AnimationLibrary_method_remove_animation)

Removes the [Animation](class_animation.md#class_Animation) with the key `name`.

---

<span id="class_AnimationLibrary_method_rename_animation"></span>

void **rename_animation** ( name: [StringName](class_stringname.md#class_StringName), newname: [StringName](class_stringname.md#class_StringName) ) [🔗](class_animationlibrary.md#class_AnimationLibrary_method_rename_animation)

Changes the key of the [Animation](class_animation.md#class_Animation) associated with the key `name` to `newname`.
