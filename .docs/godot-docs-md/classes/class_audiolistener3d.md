.. meta::
	:keywords: sound

<span id="class_AudioListener3D"></span>

## AudioListener3D

**Inherits:** [Node3D](class_node3d.md#class_Node3D) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

Overrides the location sounds are heard from.

### Description

Once added to the scene tree and enabled using [make_current()](class_audiolistener3d.md#class_AudioListener3D_method_make_current), this node will override the location sounds are heard from. This can be used to listen from a location different from the [Camera3D](class_camera3d.md#class_Camera3D).

### Properties


| [DopplerTracking](class_audiolistener3d.md#enum_AudioListener3D_DopplerTracking) | [doppler_tracking](class_audiolistener3d.md#class_AudioListener3D_property_doppler_tracking) | `0` |
| --- | --- | --- |

### Methods


| void | [clear_current](class_audiolistener3d.md#class_AudioListener3D_method_clear_current) ( ) |
| --- | --- |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_listener_transform](class_audiolistener3d.md#class_AudioListener3D_method_get_listener_transform) ( ) const |
| [bool](class_bool.md#class_bool) | [is_current](class_audiolistener3d.md#class_AudioListener3D_method_is_current) ( ) const |
| void | [make_current](class_audiolistener3d.md#class_AudioListener3D_method_make_current) ( ) |

---

### Enumerations

<span id="enum_AudioListener3D_DopplerTracking"></span>

enum **DopplerTracking**: [🔗](class_audiolistener3d.md#enum_AudioListener3D_DopplerTracking)

<span id="class_AudioListener3D_constant_DOPPLER_TRACKING_DISABLED"></span>

[DopplerTracking](class_audiolistener3d.md#enum_AudioListener3D_DopplerTracking) **DOPPLER_TRACKING_DISABLED** = `0`

Disables Doppler effect simulation (default).

<span id="class_AudioListener3D_constant_DOPPLER_TRACKING_IDLE_STEP"></span>

[DopplerTracking](class_audiolistener3d.md#enum_AudioListener3D_DopplerTracking) **DOPPLER_TRACKING_IDLE_STEP** = `1`

Simulate Doppler effect by tracking positions of objects that are changed in `_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_pitch_scale)).

<span id="class_AudioListener3D_constant_DOPPLER_TRACKING_PHYSICS_STEP"></span>

[DopplerTracking](class_audiolistener3d.md#enum_AudioListener3D_DopplerTracking) **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Simulate Doppler effect by tracking positions of objects that are changed in `_physics_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_pitch_scale)).

---

### Property Descriptions

<span id="class_AudioListener3D_property_doppler_tracking"></span>

[DopplerTracking](class_audiolistener3d.md#enum_AudioListener3D_DopplerTracking) **doppler_tracking** = `0` [🔗](class_audiolistener3d.md#class_AudioListener3D_property_doppler_tracking)

- void **set_doppler_tracking** ( value: [DopplerTracking](class_audiolistener3d.md#enum_AudioListener3D_DopplerTracking) )
- [DopplerTracking](class_audiolistener3d.md#enum_AudioListener3D_DopplerTracking) **get_doppler_tracking** ( )

If not [DOPPLER_TRACKING_DISABLED](class_audiolistener3d.md#class_AudioListener3D_constant_DOPPLER_TRACKING_DISABLED), this listener will simulate the Doppler effect for objects changed in particular `_process` methods.

 **Note:** The Doppler effect will only be heard on [AudioStreamPlayer3D](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D) s if [AudioStreamPlayer3D.doppler_tracking](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_property_doppler_tracking) is not set to [AudioStreamPlayer3D.DOPPLER_TRACKING_DISABLED](class_audiostreamplayer3d.md#class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_DISABLED).

---

### Method Descriptions

<span id="class_AudioListener3D_method_clear_current"></span>

void **clear_current** ( ) [🔗](class_audiolistener3d.md#class_AudioListener3D_method_clear_current)

Disables the listener to use the current camera's listener instead.

---

<span id="class_AudioListener3D_method_get_listener_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_listener_transform** ( ) *const* [🔗](class_audiolistener3d.md#class_AudioListener3D_method_get_listener_transform)

Returns the listener's global orthonormalized [Transform3D](class_transform3d.md#class_Transform3D).

---

<span id="class_AudioListener3D_method_is_current"></span>

[bool](class_bool.md#class_bool) **is_current** ( ) *const* [🔗](class_audiolistener3d.md#class_AudioListener3D_method_is_current)

Returns `true` if the listener was made current using [make_current()](class_audiolistener3d.md#class_AudioListener3D_method_make_current), `false` otherwise.

 **Note:** There may be more than one AudioListener3D marked as "current" in the scene tree, but only the one that was made current last will be used.

---

<span id="class_AudioListener3D_method_make_current"></span>

void **make_current** ( ) [🔗](class_audiolistener3d.md#class_AudioListener3D_method_make_current)

Enables the listener. This will override the current camera's listener.
