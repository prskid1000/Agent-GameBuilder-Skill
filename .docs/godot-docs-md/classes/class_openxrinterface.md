<span id="class_OpenXRInterface"></span>

## OpenXRInterface

**Inherits:** [XRInterface](class_xrinterface.md#class_XRInterface) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Our OpenXR interface.

### Description

The OpenXR interface allows Godot to interact with OpenXR runtimes and make it possible to create XR experiences and games.

Due to the needs of OpenXR this interface works slightly different than other plugin based XR interfaces. It needs to be initialized when Godot starts. You need to enable OpenXR, settings for this can be found in your games project settings under the XR heading. You do need to mark a viewport for use with XR in order for Godot to know which render result should be output to the headset.

### Tutorials

- [Setting up XR](../tutorials/xr/setting_up_xr.md)

### Properties


| [float](class_float.md#class_float) | [display_refresh_rate](class_openxrinterface.md#class_OpenXRInterface_property_display_refresh_rate) | `0.0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [foveation_dynamic](class_openxrinterface.md#class_OpenXRInterface_property_foveation_dynamic) | `false` |
| [int](class_int.md#class_int) | [foveation_level](class_openxrinterface.md#class_OpenXRInterface_property_foveation_level) | `0` |
| [float](class_float.md#class_float) | [render_target_size_multiplier](class_openxrinterface.md#class_OpenXRInterface_property_render_target_size_multiplier) | `1.0` |
| [float](class_float.md#class_float) | [vrs_min_radius](class_openxrinterface.md#class_OpenXRInterface_property_vrs_min_radius) | `20.0` |
| [float](class_float.md#class_float) | [vrs_strength](class_openxrinterface.md#class_OpenXRInterface_property_vrs_strength) | `1.0` |

### Methods


| [Array](class_array.md#class_Array) | [get_action_sets](class_openxrinterface.md#class_OpenXRInterface_method_get_action_sets) ( ) const |
| --- | --- |
| [Array](class_array.md#class_Array) | [get_available_display_refresh_rates](class_openxrinterface.md#class_OpenXRInterface_method_get_available_display_refresh_rates) ( ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_hand_joint_angular_velocity](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_angular_velocity) ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) const |
| bitfield | \[[HandJointFlags](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags)\] | [get_hand_joint_flags](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_flags) ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) | const |
| [Vector3](class_vector3.md#class_Vector3) | [get_hand_joint_linear_velocity](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_linear_velocity) ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) const |
| [Vector3](class_vector3.md#class_Vector3) | [get_hand_joint_position](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_position) ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) const |
| [float](class_float.md#class_float) | [get_hand_joint_radius](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_radius) ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) const |
| [Quaternion](class_quaternion.md#class_Quaternion) | [get_hand_joint_rotation](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_rotation) ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) const |
| [HandTrackedSource](class_openxrinterface.md#enum_OpenXRInterface_HandTrackedSource) | [get_hand_tracking_source](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_tracking_source) ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand) ) const |
| [HandMotionRange](class_openxrinterface.md#enum_OpenXRInterface_HandMotionRange) | [get_motion_range](class_openxrinterface.md#class_OpenXRInterface_method_get_motion_range) ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand) ) const |
| [SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) | [get_session_state](class_openxrinterface.md#class_OpenXRInterface_method_get_session_state) ( ) |
| [bool](class_bool.md#class_bool) | [is_action_set_active](class_openxrinterface.md#class_OpenXRInterface_method_is_action_set_active) ( name: [String](class_string.md#class_String) ) const |
| [bool](class_bool.md#class_bool) | [is_eye_gaze_interaction_supported](class_openxrinterface.md#class_OpenXRInterface_method_is_eye_gaze_interaction_supported) ( ) |
| [bool](class_bool.md#class_bool) | [is_foveation_supported](class_openxrinterface.md#class_OpenXRInterface_method_is_foveation_supported) ( ) const |
| [bool](class_bool.md#class_bool) | [is_hand_interaction_supported](class_openxrinterface.md#class_OpenXRInterface_method_is_hand_interaction_supported) ( ) const |
| [bool](class_bool.md#class_bool) | [is_hand_tracking_supported](class_openxrinterface.md#class_OpenXRInterface_method_is_hand_tracking_supported) ( ) |
| [bool](class_bool.md#class_bool) | [is_user_presence_supported](class_openxrinterface.md#class_OpenXRInterface_method_is_user_presence_supported) ( ) const |
| [bool](class_bool.md#class_bool) | [is_user_present](class_openxrinterface.md#class_OpenXRInterface_method_is_user_present) ( ) const |
| void | [set_action_set_active](class_openxrinterface.md#class_OpenXRInterface_method_set_action_set_active) ( name: [String](class_string.md#class_String), active: [bool](class_bool.md#class_bool) ) |
| void | [set_cpu_level](class_openxrinterface.md#class_OpenXRInterface_method_set_cpu_level) ( level: [PerfSettingsLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsLevel) ) |
| void | [set_gpu_level](class_openxrinterface.md#class_OpenXRInterface_method_set_gpu_level) ( level: [PerfSettingsLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsLevel) ) |
| void | [set_motion_range](class_openxrinterface.md#class_OpenXRInterface_method_set_motion_range) ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), motion_range: [HandMotionRange](class_openxrinterface.md#enum_OpenXRInterface_HandMotionRange) ) |

---

### Signals

<span id="class_OpenXRInterface_signal_cpu_level_changed"></span>

**cpu_level_changed** ( sub_domain: [int](class_int.md#class_int), from_level: [int](class_int.md#class_int), to_level: [int](class_int.md#class_int) ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_cpu_level_changed)

Informs the device CPU performance level has changed in the specified subdomain.

---

<span id="class_OpenXRInterface_signal_gpu_level_changed"></span>

**gpu_level_changed** ( sub_domain: [int](class_int.md#class_int), from_level: [int](class_int.md#class_int), to_level: [int](class_int.md#class_int) ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_gpu_level_changed)

Informs the device GPU performance level has changed in the specified subdomain.

---

<span id="class_OpenXRInterface_signal_instance_exiting"></span>

**instance_exiting** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_instance_exiting)

Informs our OpenXR instance is exiting.

---

<span id="class_OpenXRInterface_signal_pose_recentered"></span>

**pose_recentered** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_pose_recentered)

Informs the user queued a recenter of the player position.

---

<span id="class_OpenXRInterface_signal_refresh_rate_changed"></span>

**refresh_rate_changed** ( refresh_rate: [float](class_float.md#class_float) ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_refresh_rate_changed)

Informs the user the HMD refresh rate has changed.

 **Note:** Only emitted if XR runtime supports the refresh rate extension.

---

<span id="class_OpenXRInterface_signal_session_begun"></span>

**session_begun** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_session_begun)

Informs our OpenXR session has been started.

---

<span id="class_OpenXRInterface_signal_session_focussed"></span>

**session_focussed** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_session_focussed)

Informs our OpenXR session now has focus, for example output is sent to the HMD and we're receiving XR input.

---

<span id="class_OpenXRInterface_signal_session_loss_pending"></span>

**session_loss_pending** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_session_loss_pending)

Informs our OpenXR session is in the process of being lost.

---

<span id="class_OpenXRInterface_signal_session_stopping"></span>

**session_stopping** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_session_stopping)

Informs our OpenXR session is stopping.

---

<span id="class_OpenXRInterface_signal_session_synchronized"></span>

**session_synchronized** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_session_synchronized)

Informs our OpenXR session has been synchronized.

---

<span id="class_OpenXRInterface_signal_session_visible"></span>

**session_visible** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_session_visible)

Informs our OpenXR session is now visible, for example output is sent to the HMD but we don't receive XR input.

---

<span id="class_OpenXRInterface_signal_user_presence_changed"></span>

**user_presence_changed** ( is_user_present: [bool](class_bool.md#class_bool) ) [🔗](class_openxrinterface.md#class_OpenXRInterface_signal_user_presence_changed)

Signal emitted when the user presence value changes.

 **Note:** This signal will not be emitted during application startup and application shutdown. Developers should assume user presence is gained on startup and lost on shutdown.

---

### Enumerations

<span id="enum_OpenXRInterface_SessionState"></span>

enum **SessionState**: [🔗](class_openxrinterface.md#enum_OpenXRInterface_SessionState)

<span id="class_OpenXRInterface_constant_SESSION_STATE_UNKNOWN"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **SESSION_STATE_UNKNOWN** = `0`

The state of the session is unknown, we haven't tried setting up OpenXR yet.

<span id="class_OpenXRInterface_constant_SESSION_STATE_IDLE"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **SESSION_STATE_IDLE** = `1`

The initial state after the OpenXR session is created or after the session is destroyed.

<span id="class_OpenXRInterface_constant_SESSION_STATE_READY"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **SESSION_STATE_READY** = `2`

OpenXR is ready to begin our session. [session_begun](class_openxrinterface.md#class_OpenXRInterface_signal_session_begun) is emitted when we change to this state.

<span id="class_OpenXRInterface_constant_SESSION_STATE_SYNCHRONIZED"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **SESSION_STATE_SYNCHRONIZED** = `3`

The application has synched its frame loop with the runtime but we're not rendering anything. [session_synchronized](class_openxrinterface.md#class_OpenXRInterface_signal_session_synchronized) is emitted when we change to this state.

<span id="class_OpenXRInterface_constant_SESSION_STATE_VISIBLE"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **SESSION_STATE_VISIBLE** = `4`

The application has synched its frame loop with the runtime and we're rendering output to the user, however we receive no user input. [session_visible](class_openxrinterface.md#class_OpenXRInterface_signal_session_visible) is emitted when we change to this state.

 **Note:** This is the current state just before we get the focused state, whenever the user opens a system menu, switches to another application, or takes off their headset.

<span id="class_OpenXRInterface_constant_SESSION_STATE_FOCUSED"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **SESSION_STATE_FOCUSED** = `5`

The application has synched its frame loop with the runtime, we're rendering output to the user and we're receiving XR input. [session_focussed](class_openxrinterface.md#class_OpenXRInterface_signal_session_focussed) is emitted when we change to this state.

 **Note:** This is the state OpenXR will be in when the user can fully interact with your game.

<span id="class_OpenXRInterface_constant_SESSION_STATE_STOPPING"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **SESSION_STATE_STOPPING** = `6`

Our session is being stopped. [session_stopping](class_openxrinterface.md#class_OpenXRInterface_signal_session_stopping) is emitted when we change to this state.

<span id="class_OpenXRInterface_constant_SESSION_STATE_LOSS_PENDING"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **SESSION_STATE_LOSS_PENDING** = `7`

The session is about to be lost. [session_loss_pending](class_openxrinterface.md#class_OpenXRInterface_signal_session_loss_pending) is emitted when we change to this state.

<span id="class_OpenXRInterface_constant_SESSION_STATE_EXITING"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **SESSION_STATE_EXITING** = `8`

The OpenXR instance is about to be destroyed and we're exiting. [instance_exiting](class_openxrinterface.md#class_OpenXRInterface_signal_instance_exiting) is emitted when we change to this state.

---

<span id="enum_OpenXRInterface_Hand"></span>

enum **Hand**: [🔗](class_openxrinterface.md#enum_OpenXRInterface_Hand)

<span id="class_OpenXRInterface_constant_HAND_LEFT"></span>

[Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand) **HAND_LEFT** = `0`

Left hand.

<span id="class_OpenXRInterface_constant_HAND_RIGHT"></span>

[Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand) **HAND_RIGHT** = `1`

Right hand.

<span id="class_OpenXRInterface_constant_HAND_MAX"></span>

[Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand) **HAND_MAX** = `2`

Maximum value for the hand enum.

---

<span id="enum_OpenXRInterface_HandMotionRange"></span>

enum **HandMotionRange**: [🔗](class_openxrinterface.md#enum_OpenXRInterface_HandMotionRange)

<span id="class_OpenXRInterface_constant_HAND_MOTION_RANGE_UNOBSTRUCTED"></span>

[HandMotionRange](class_openxrinterface.md#enum_OpenXRInterface_HandMotionRange) **HAND_MOTION_RANGE_UNOBSTRUCTED** = `0`

Full hand range, if user closes their hands, we make a full fist.

<span id="class_OpenXRInterface_constant_HAND_MOTION_RANGE_CONFORM_TO_CONTROLLER"></span>

[HandMotionRange](class_openxrinterface.md#enum_OpenXRInterface_HandMotionRange) **HAND_MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

Conform to controller, if user closes their hands, the tracked data conforms to the shape of the controller.

<span id="class_OpenXRInterface_constant_HAND_MOTION_RANGE_MAX"></span>

[HandMotionRange](class_openxrinterface.md#enum_OpenXRInterface_HandMotionRange) **HAND_MOTION_RANGE_MAX** = `2`

Maximum value for the motion range enum.

---

<span id="enum_OpenXRInterface_HandTrackedSource"></span>

enum **HandTrackedSource**: [🔗](class_openxrinterface.md#enum_OpenXRInterface_HandTrackedSource)

<span id="class_OpenXRInterface_constant_HAND_TRACKED_SOURCE_UNKNOWN"></span>

[HandTrackedSource](class_openxrinterface.md#enum_OpenXRInterface_HandTrackedSource) **HAND_TRACKED_SOURCE_UNKNOWN** = `0`

The source of hand tracking data is unknown (the extension is likely unsupported).

<span id="class_OpenXRInterface_constant_HAND_TRACKED_SOURCE_UNOBSTRUCTED"></span>

[HandTrackedSource](class_openxrinterface.md#enum_OpenXRInterface_HandTrackedSource) **HAND_TRACKED_SOURCE_UNOBSTRUCTED** = `1`

The source of hand tracking is unobstructed, this means that an accurate method of hand tracking is used, e.g. optical hand tracking, data gloves, etc.

<span id="class_OpenXRInterface_constant_HAND_TRACKED_SOURCE_CONTROLLER"></span>

[HandTrackedSource](class_openxrinterface.md#enum_OpenXRInterface_HandTrackedSource) **HAND_TRACKED_SOURCE_CONTROLLER** = `2`

The source of hand tracking is a controller, bone positions are inferred from controller inputs.

<span id="class_OpenXRInterface_constant_HAND_TRACKED_SOURCE_MAX"></span>

[HandTrackedSource](class_openxrinterface.md#enum_OpenXRInterface_HandTrackedSource) **HAND_TRACKED_SOURCE_MAX** = `3`

Represents the size of the [HandTrackedSource](class_openxrinterface.md#enum_OpenXRInterface_HandTrackedSource) enum.

---

<span id="enum_OpenXRInterface_HandJoints"></span>

enum **HandJoints**: [🔗](class_openxrinterface.md#enum_OpenXRInterface_HandJoints)

<span id="class_OpenXRInterface_constant_HAND_JOINT_PALM"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_PALM** = `0`

Palm joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_WRIST"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_WRIST** = `1`

Wrist joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_THUMB_METACARPAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_THUMB_METACARPAL** = `2`

Thumb metacarpal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_THUMB_PROXIMAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_THUMB_PROXIMAL** = `3`

Thumb proximal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_THUMB_DISTAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_THUMB_DISTAL** = `4`

Thumb distal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_THUMB_TIP"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_THUMB_TIP** = `5`

Thumb tip joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_INDEX_METACARPAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_INDEX_METACARPAL** = `6`

Index finger metacarpal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_INDEX_PROXIMAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_INDEX_PROXIMAL** = `7`

Index finger phalanx proximal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_INDEX_INTERMEDIATE"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_INDEX_INTERMEDIATE** = `8`

Index finger phalanx intermediate joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_INDEX_DISTAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_INDEX_DISTAL** = `9`

Index finger phalanx distal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_INDEX_TIP"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_INDEX_TIP** = `10`

Index finger tip joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_METACARPAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_MIDDLE_METACARPAL** = `11`

Middle finger metacarpal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_PROXIMAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_MIDDLE_PROXIMAL** = `12`

Middle finger phalanx proximal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_INTERMEDIATE"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_MIDDLE_INTERMEDIATE** = `13`

Middle finger phalanx intermediate joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_DISTAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_MIDDLE_DISTAL** = `14`

Middle finger phalanx distal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_MIDDLE_TIP"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_MIDDLE_TIP** = `15`

Middle finger tip joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_RING_METACARPAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_RING_METACARPAL** = `16`

Ring finger metacarpal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_RING_PROXIMAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_RING_PROXIMAL** = `17`

Ring finger phalanx proximal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_RING_INTERMEDIATE"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_RING_INTERMEDIATE** = `18`

Ring finger phalanx intermediate joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_RING_DISTAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_RING_DISTAL** = `19`

Ring finger phalanx distal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_RING_TIP"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_RING_TIP** = `20`

Ring finger tip joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_LITTLE_METACARPAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_LITTLE_METACARPAL** = `21`

Pinky finger metacarpal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_LITTLE_PROXIMAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_LITTLE_PROXIMAL** = `22`

Pinky finger phalanx proximal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_LITTLE_INTERMEDIATE"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_LITTLE_INTERMEDIATE** = `23`

Pinky finger phalanx intermediate joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_LITTLE_DISTAL"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_LITTLE_DISTAL** = `24`

Pinky finger phalanx distal joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_LITTLE_TIP"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_LITTLE_TIP** = `25`

Pinky finger tip joint.

<span id="class_OpenXRInterface_constant_HAND_JOINT_MAX"></span>

[HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) **HAND_JOINT_MAX** = `26`

Represents the size of the [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) enum.

---

<span id="enum_OpenXRInterface_PerfSettingsLevel"></span>

enum **PerfSettingsLevel**: [🔗](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsLevel)

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_LEVEL_POWER_SAVINGS"></span>

[PerfSettingsLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsLevel) **PERF_SETTINGS_LEVEL_POWER_SAVINGS** = `0`

The application has entered a non-XR section (head-locked / static screen), during which power savings are to be prioritized.

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_LEVEL_SUSTAINED_LOW"></span>

[PerfSettingsLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsLevel) **PERF_SETTINGS_LEVEL_SUSTAINED_LOW** = `1`

The application has entered a low and stable complexity section, during which reducing power is more important than occasional late rendering frames.

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_LEVEL_SUSTAINED_HIGH"></span>

[PerfSettingsLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsLevel) **PERF_SETTINGS_LEVEL_SUSTAINED_HIGH** = `2`

The application has entered a high or dynamic complexity section, during which the XR Runtime strives for consistent XR compositing and frame rendering within a thermally sustainable range.

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_LEVEL_BOOST"></span>

[PerfSettingsLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsLevel) **PERF_SETTINGS_LEVEL_BOOST** = `3`

The application has entered a section with very high complexity, during which the XR Runtime is allowed to step up beyond the thermally sustainable range.

---

<span id="enum_OpenXRInterface_PerfSettingsSubDomain"></span>

enum **PerfSettingsSubDomain**: [🔗](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsSubDomain)

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_SUB_DOMAIN_COMPOSITING"></span>

[PerfSettingsSubDomain](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsSubDomain) **PERF_SETTINGS_SUB_DOMAIN_COMPOSITING** = `0`

The compositing performance within the runtime has reached a new level.

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_SUB_DOMAIN_RENDERING"></span>

[PerfSettingsSubDomain](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsSubDomain) **PERF_SETTINGS_SUB_DOMAIN_RENDERING** = `1`

The application rendering performance has reached a new level.

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_SUB_DOMAIN_THERMAL"></span>

[PerfSettingsSubDomain](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsSubDomain) **PERF_SETTINGS_SUB_DOMAIN_THERMAL** = `2`

The temperature of the device has reached a new level.

---

<span id="enum_OpenXRInterface_PerfSettingsNotificationLevel"></span>

enum **PerfSettingsNotificationLevel**: [🔗](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsNotificationLevel)

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_NOTIF_LEVEL_NORMAL"></span>

[PerfSettingsNotificationLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsNotificationLevel) **PERF_SETTINGS_NOTIF_LEVEL_NORMAL** = `0`

The sub-domain has reached a level where no further actions other than currently applied are necessary.

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_NOTIF_LEVEL_WARNING"></span>

[PerfSettingsNotificationLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsNotificationLevel) **PERF_SETTINGS_NOTIF_LEVEL_WARNING** = `1`

The sub-domain has reached an early warning level where the application should start proactive mitigation actions.

<span id="class_OpenXRInterface_constant_PERF_SETTINGS_NOTIF_LEVEL_IMPAIRED"></span>

[PerfSettingsNotificationLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsNotificationLevel) **PERF_SETTINGS_NOTIF_LEVEL_IMPAIRED** = `2`

The sub-domain has reached a critical level where the application should start drastic mitigation actions.

---

<span id="enum_OpenXRInterface_HandJointFlags"></span>

flags **HandJointFlags**: [🔗](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags)

<span id="class_OpenXRInterface_constant_HAND_JOINT_NONE"></span>

[HandJointFlags](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags) **HAND_JOINT_NONE** = `0`

No flags are set.

<span id="class_OpenXRInterface_constant_HAND_JOINT_ORIENTATION_VALID"></span>

[HandJointFlags](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags) **HAND_JOINT_ORIENTATION_VALID** = `1`

If set, the orientation data is valid, otherwise, the orientation data is unreliable and should not be used.

<span id="class_OpenXRInterface_constant_HAND_JOINT_ORIENTATION_TRACKED"></span>

[HandJointFlags](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags) **HAND_JOINT_ORIENTATION_TRACKED** = `2`

If set, the orientation data comes from tracking data, otherwise, the orientation data contains predicted data.

<span id="class_OpenXRInterface_constant_HAND_JOINT_POSITION_VALID"></span>

[HandJointFlags](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags) **HAND_JOINT_POSITION_VALID** = `4`

If set, the positional data is valid, otherwise, the positional data is unreliable and should not be used.

<span id="class_OpenXRInterface_constant_HAND_JOINT_POSITION_TRACKED"></span>

[HandJointFlags](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags) **HAND_JOINT_POSITION_TRACKED** = `8`

If set, the positional data comes from tracking data, otherwise, the positional data contains predicted data.

<span id="class_OpenXRInterface_constant_HAND_JOINT_LINEAR_VELOCITY_VALID"></span>

[HandJointFlags](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags) **HAND_JOINT_LINEAR_VELOCITY_VALID** = `16`

If set, our linear velocity data is valid, otherwise, the linear velocity data is unreliable and should not be used.

<span id="class_OpenXRInterface_constant_HAND_JOINT_ANGULAR_VELOCITY_VALID"></span>

[HandJointFlags](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags) **HAND_JOINT_ANGULAR_VELOCITY_VALID** = `32`

If set, our angular velocity data is valid, otherwise, the angular velocity data is unreliable and should not be used.

---

### Property Descriptions

<span id="class_OpenXRInterface_property_display_refresh_rate"></span>

[float](class_float.md#class_float) **display_refresh_rate** = `0.0` [🔗](class_openxrinterface.md#class_OpenXRInterface_property_display_refresh_rate)

- void **set_display_refresh_rate** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_display_refresh_rate** ( )

The display refresh rate for the current HMD. Only functional if this feature is supported by the OpenXR runtime and after the interface has been initialized.

---

<span id="class_OpenXRInterface_property_foveation_dynamic"></span>

[bool](class_bool.md#class_bool) **foveation_dynamic** = `false` [🔗](class_openxrinterface.md#class_OpenXRInterface_property_foveation_dynamic)

- void **set_foveation_dynamic** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_foveation_dynamic** ( )

If `true`, enables dynamic foveation adjustment. The interface must be initialized before this is accessible. If enabled, foveation will automatically be adjusted between low and [foveation_level](class_openxrinterface.md#class_OpenXRInterface_property_foveation_level).

 **Note:** Only works on the Compatibility renderer.

---

<span id="class_OpenXRInterface_property_foveation_level"></span>

[int](class_int.md#class_int) **foveation_level** = `0` [🔗](class_openxrinterface.md#class_OpenXRInterface_property_foveation_level)

- void **set_foveation_level** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_foveation_level** ( )

The foveation level, from `0` (off) to `3` (high). The interface must be initialized before this is accessible.

 **Note:** Only works on the Compatibility renderer.

---

<span id="class_OpenXRInterface_property_render_target_size_multiplier"></span>

[float](class_float.md#class_float) **render_target_size_multiplier** = `1.0` [🔗](class_openxrinterface.md#class_OpenXRInterface_property_render_target_size_multiplier)

- void **set_render_target_size_multiplier** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_render_target_size_multiplier** ( )

The render size multiplier for the current HMD. Must be set before the interface has been initialized.

---

<span id="class_OpenXRInterface_property_vrs_min_radius"></span>

[float](class_float.md#class_float) **vrs_min_radius** = `20.0` [🔗](class_openxrinterface.md#class_OpenXRInterface_property_vrs_min_radius)

- void **set_vrs_min_radius** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_vrs_min_radius** ( )

The minimum radius around the focal point where full quality is guaranteed if VRS is used as a percentage of screen size.

 **Note:** Mobile and Forward+ renderers only. Requires [Viewport.vrs_mode](class_viewport.md#class_Viewport_property_vrs_mode) to be set to [Viewport.VRS_XR](class_viewport.md#class_Viewport_constant_VRS_XR).

---

<span id="class_OpenXRInterface_property_vrs_strength"></span>

[float](class_float.md#class_float) **vrs_strength** = `1.0` [🔗](class_openxrinterface.md#class_OpenXRInterface_property_vrs_strength)

- void **set_vrs_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_vrs_strength** ( )

The strength used to calculate the VRS density map. The greater this value, the more noticeable VRS is. This improves performance at the cost of quality.

 **Note:** Mobile and Forward+ renderers only. Requires [Viewport.vrs_mode](class_viewport.md#class_Viewport_property_vrs_mode) to be set to [Viewport.VRS_XR](class_viewport.md#class_Viewport_constant_VRS_XR).

---

### Method Descriptions

<span id="class_OpenXRInterface_method_get_action_sets"></span>

[Array](class_array.md#class_Array) **get_action_sets** ( ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_action_sets)

Returns a list of action sets registered with Godot (loaded from the action map at runtime).

---

<span id="class_OpenXRInterface_method_get_available_display_refresh_rates"></span>

[Array](class_array.md#class_Array) **get_available_display_refresh_rates** ( ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_available_display_refresh_rates)

Returns a list of display refresh rates supported by the current HMD. Only returned if this feature is supported by the OpenXR runtime and after the interface has been initialized.

---

<span id="class_OpenXRInterface_method_get_hand_joint_angular_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **get_hand_joint_angular_velocity** ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_angular_velocity)

**Deprecated:** Use [XRHandTracker.get_hand_joint_angular_velocity()](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_angular_velocity) obtained from [XRServer.get_tracker()](class_xrserver.md#class_XRServer_method_get_tracker) instead.

If handtracking is enabled, returns the angular velocity of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D)!

---

<span id="class_OpenXRInterface_method_get_hand_joint_flags"></span>

*BitField*\[[HandJointFlags](class_openxrinterface.md#enum_OpenXRInterface_HandJointFlags)\] **get_hand_joint_flags** ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_flags)

**Deprecated:** Use [XRHandTracker.get_hand_joint_flags()](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_flags) obtained from [XRServer.get_tracker()](class_xrserver.md#class_XRServer_method_get_tracker) instead.

If handtracking is enabled, returns flags that inform us of the validity of the tracking data.

---

<span id="class_OpenXRInterface_method_get_hand_joint_linear_velocity"></span>

[Vector3](class_vector3.md#class_Vector3) **get_hand_joint_linear_velocity** ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_linear_velocity)

**Deprecated:** Use [XRHandTracker.get_hand_joint_linear_velocity()](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_linear_velocity) obtained from [XRServer.get_tracker()](class_xrserver.md#class_XRServer_method_get_tracker) instead.

If handtracking is enabled, returns the linear velocity of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D) without worldscale applied!

---

<span id="class_OpenXRInterface_method_get_hand_joint_position"></span>

[Vector3](class_vector3.md#class_Vector3) **get_hand_joint_position** ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_position)

**Deprecated:** Use [XRHandTracker.get_hand_joint_transform()](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_transform) obtained from [XRServer.get_tracker()](class_xrserver.md#class_XRServer_method_get_tracker) instead.

If handtracking is enabled, returns the position of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to [XROrigin3D](class_xrorigin3d.md#class_XROrigin3D) without worldscale applied!

---

<span id="class_OpenXRInterface_method_get_hand_joint_radius"></span>

[float](class_float.md#class_float) **get_hand_joint_radius** ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_radius)

**Deprecated:** Use [XRHandTracker.get_hand_joint_radius()](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_radius) obtained from [XRServer.get_tracker()](class_xrserver.md#class_XRServer_method_get_tracker) instead.

If handtracking is enabled, returns the radius of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is without worldscale applied!

---

<span id="class_OpenXRInterface_method_get_hand_joint_rotation"></span>

[Quaternion](class_quaternion.md#class_Quaternion) **get_hand_joint_rotation** ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), joint: [HandJoints](class_openxrinterface.md#enum_OpenXRInterface_HandJoints) ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_joint_rotation)

**Deprecated:** Use [XRHandTracker.get_hand_joint_transform()](class_xrhandtracker.md#class_XRHandTracker_method_get_hand_joint_transform) obtained from [XRServer.get_tracker()](class_xrserver.md#class_XRServer_method_get_tracker) instead.

If handtracking is enabled, returns the rotation of a joint (`joint`) of a hand (`hand`) as provided by OpenXR.

---

<span id="class_OpenXRInterface_method_get_hand_tracking_source"></span>

[HandTrackedSource](class_openxrinterface.md#enum_OpenXRInterface_HandTrackedSource) **get_hand_tracking_source** ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand) ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_hand_tracking_source)

**Deprecated:** Use [XRHandTracker.hand_tracking_source](class_xrhandtracker.md#class_XRHandTracker_property_hand_tracking_source) obtained from [XRServer.get_tracker()](class_xrserver.md#class_XRServer_method_get_tracker) instead.

If handtracking is enabled and hand tracking source is supported, gets the source of the hand tracking data for `hand`.

---

<span id="class_OpenXRInterface_method_get_motion_range"></span>

[HandMotionRange](class_openxrinterface.md#enum_OpenXRInterface_HandMotionRange) **get_motion_range** ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand) ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_motion_range)

If handtracking is enabled and motion range is supported, gets the currently configured motion range for `hand`.

---

<span id="class_OpenXRInterface_method_get_session_state"></span>

[SessionState](class_openxrinterface.md#enum_OpenXRInterface_SessionState) **get_session_state** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_method_get_session_state)

Returns the current state of our OpenXR session.

---

<span id="class_OpenXRInterface_method_is_action_set_active"></span>

[bool](class_bool.md#class_bool) **is_action_set_active** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_is_action_set_active)

Returns `true` if the given action set is active.

---

<span id="class_OpenXRInterface_method_is_eye_gaze_interaction_supported"></span>

[bool](class_bool.md#class_bool) **is_eye_gaze_interaction_supported** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_method_is_eye_gaze_interaction_supported)

Returns the capabilities of the eye gaze interaction extension.

 **Note:** This only returns a valid value after OpenXR has been initialized.

---

<span id="class_OpenXRInterface_method_is_foveation_supported"></span>

[bool](class_bool.md#class_bool) **is_foveation_supported** ( ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_is_foveation_supported)

Returns `true` if OpenXR's foveation extension is supported. The interface must be initialized before this returns a valid value.

 **Note:** When using the Vulkan rendering driver, [Viewport.vrs_mode](class_viewport.md#class_Viewport_property_vrs_mode) must be set to [Viewport.VRS_XR](class_viewport.md#class_Viewport_constant_VRS_XR) to support foveation.

---

<span id="class_OpenXRInterface_method_is_hand_interaction_supported"></span>

[bool](class_bool.md#class_bool) **is_hand_interaction_supported** ( ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_is_hand_interaction_supported)

Returns `true` if OpenXR's hand interaction profile is supported and enabled.

 **Note:** This only returns a valid value after OpenXR has been initialized.

---

<span id="class_OpenXRInterface_method_is_hand_tracking_supported"></span>

[bool](class_bool.md#class_bool) **is_hand_tracking_supported** ( ) [🔗](class_openxrinterface.md#class_OpenXRInterface_method_is_hand_tracking_supported)

Returns `true` if OpenXR's hand tracking is supported and enabled.

 **Note:** This only returns a valid value after OpenXR has been initialized.

---

<span id="class_OpenXRInterface_method_is_user_presence_supported"></span>

[bool](class_bool.md#class_bool) **is_user_presence_supported** ( ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_is_user_presence_supported)

Returns `true` if OpenXR's user presence extension is supported and enabled.

 **Note:** This only returns a valid value after OpenXR has been initialized.

---

<span id="class_OpenXRInterface_method_is_user_present"></span>

[bool](class_bool.md#class_bool) **is_user_present** ( ) *const* [🔗](class_openxrinterface.md#class_OpenXRInterface_method_is_user_present)

Returns `true` if system has detected the presence of a user in the XR experience.

---

<span id="class_OpenXRInterface_method_set_action_set_active"></span>

void **set_action_set_active** ( name: [String](class_string.md#class_String), active: [bool](class_bool.md#class_bool) ) [🔗](class_openxrinterface.md#class_OpenXRInterface_method_set_action_set_active)

Sets the given action set as active or inactive.

---

<span id="class_OpenXRInterface_method_set_cpu_level"></span>

void **set_cpu_level** ( level: [PerfSettingsLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsLevel) ) [🔗](class_openxrinterface.md#class_OpenXRInterface_method_set_cpu_level)

Sets the CPU performance level of the OpenXR device.

---

<span id="class_OpenXRInterface_method_set_gpu_level"></span>

void **set_gpu_level** ( level: [PerfSettingsLevel](class_openxrinterface.md#enum_OpenXRInterface_PerfSettingsLevel) ) [🔗](class_openxrinterface.md#class_OpenXRInterface_method_set_gpu_level)

Sets the GPU performance level of the OpenXR device.

---

<span id="class_OpenXRInterface_method_set_motion_range"></span>

void **set_motion_range** ( hand: [Hand](class_openxrinterface.md#enum_OpenXRInterface_Hand), motion_range: [HandMotionRange](class_openxrinterface.md#enum_OpenXRInterface_HandMotionRange) ) [🔗](class_openxrinterface.md#class_OpenXRInterface_method_set_motion_range)

If handtracking is enabled and motion range is supported, sets the currently configured motion range for `hand` to `motion_range`.
