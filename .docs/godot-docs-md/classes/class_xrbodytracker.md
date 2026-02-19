<span id="class_XRBodyTracker"></span>

## XRBodyTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [XRPositionalTracker](class_xrpositionaltracker.md#class_XRPositionalTracker) **<** [XRTracker](class_xrtracker.md#class_XRTracker) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A tracked body in XR.

### Description

A body tracking system will create an instance of this object and add it to the [XRServer](class_xrserver.md#class_XRServer). This tracking system will then obtain skeleton data, convert it to the Godot Humanoid skeleton and store this data on the **XRBodyTracker** object.

Use [XRBodyModifier3D](class_xrbodymodifier3d.md#class_XRBodyModifier3D) to animate a body mesh using body tracking data.

### Tutorials

- [XR documentation index](../tutorials/xr/index.md)

### Properties


| bitfield | \[[BodyFlags](class_xrbodytracker.md#enum_XRBodyTracker_BodyFlags)\] | [body_flags](class_xrbodytracker.md#class_XRBodyTracker_property_body_flags) | `0` |
| --- | --- | --- | --- |
| [bool](class_bool.md#class_bool) | [has_tracking_data](class_xrbodytracker.md#class_XRBodyTracker_property_has_tracking_data) | `false` |
| [TrackerType](class_xrserver.md#enum_XRServer_TrackerType) | type | `32` (overrides [XRTracker](class_xrtracker.md#class_XRTracker_property_type)) |

### Methods


| bitfield | \[[JointFlags](class_xrbodytracker.md#enum_XRBodyTracker_JointFlags)\] | [get_joint_flags](class_xrbodytracker.md#class_XRBodyTracker_method_get_joint_flags) ( joint: [Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) ) | const |
| --- | --- | --- | --- |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_joint_transform](class_xrbodytracker.md#class_XRBodyTracker_method_get_joint_transform) ( joint: [Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) ) const |
| void | [set_joint_flags](class_xrbodytracker.md#class_XRBodyTracker_method_set_joint_flags) ( joint: [Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint), flags: | bitfield | \[[JointFlags](class_xrbodytracker.md#enum_XRBodyTracker_JointFlags)\] ) |
| void | [set_joint_transform](class_xrbodytracker.md#class_XRBodyTracker_method_set_joint_transform) ( joint: [Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) |

---

### Enumerations

<span id="enum_XRBodyTracker_BodyFlags"></span>

flags **BodyFlags**: [🔗](class_xrbodytracker.md#enum_XRBodyTracker_BodyFlags)

<span id="class_XRBodyTracker_constant_BODY_FLAG_UPPER_BODY_SUPPORTED"></span>

[BodyFlags](class_xrbodytracker.md#enum_XRBodyTracker_BodyFlags) **BODY_FLAG_UPPER_BODY_SUPPORTED** = `1`

Upper body tracking supported.

<span id="class_XRBodyTracker_constant_BODY_FLAG_LOWER_BODY_SUPPORTED"></span>

[BodyFlags](class_xrbodytracker.md#enum_XRBodyTracker_BodyFlags) **BODY_FLAG_LOWER_BODY_SUPPORTED** = `2`

Lower body tracking supported.

<span id="class_XRBodyTracker_constant_BODY_FLAG_HANDS_SUPPORTED"></span>

[BodyFlags](class_xrbodytracker.md#enum_XRBodyTracker_BodyFlags) **BODY_FLAG_HANDS_SUPPORTED** = `4`

Hand tracking supported.

---

<span id="enum_XRBodyTracker_Joint"></span>

enum **Joint**: [🔗](class_xrbodytracker.md#enum_XRBodyTracker_Joint)

<span id="class_XRBodyTracker_constant_JOINT_ROOT"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_ROOT** = `0`

Root joint.

<span id="class_XRBodyTracker_constant_JOINT_HIPS"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_HIPS** = `1`

Hips joint.

<span id="class_XRBodyTracker_constant_JOINT_SPINE"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_SPINE** = `2`

Spine joint.

<span id="class_XRBodyTracker_constant_JOINT_CHEST"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_CHEST** = `3`

Chest joint.

<span id="class_XRBodyTracker_constant_JOINT_UPPER_CHEST"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_UPPER_CHEST** = `4`

Upper chest joint.

<span id="class_XRBodyTracker_constant_JOINT_NECK"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_NECK** = `5`

Neck joint.

<span id="class_XRBodyTracker_constant_JOINT_HEAD"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_HEAD** = `6`

Head joint.

<span id="class_XRBodyTracker_constant_JOINT_HEAD_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_HEAD_TIP** = `7`

Head tip joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_SHOULDER"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_SHOULDER** = `8`

Left shoulder joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_UPPER_ARM"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_UPPER_ARM** = `9`

Left upper arm joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_LOWER_ARM"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_LOWER_ARM** = `10`

Left lower arm joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_SHOULDER"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_SHOULDER** = `11`

Right shoulder joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_UPPER_ARM"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_UPPER_ARM** = `12`

Right upper arm joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_LOWER_ARM"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_LOWER_ARM** = `13`

Right lower arm joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_UPPER_LEG"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_UPPER_LEG** = `14`

Left upper leg joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_LOWER_LEG"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_LOWER_LEG** = `15`

Left lower leg joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_FOOT"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_FOOT** = `16`

Left foot joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_TOES"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_TOES** = `17`

Left toes joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_UPPER_LEG"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_UPPER_LEG** = `18`

Right upper leg joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_LOWER_LEG"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_LOWER_LEG** = `19`

Right lower leg joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_FOOT"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_FOOT** = `20`

Right foot joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_TOES"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_TOES** = `21`

Right toes joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_HAND"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_HAND** = `22`

Left hand joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_PALM"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_PALM** = `23`

Left palm joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_WRIST"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_WRIST** = `24`

Left wrist joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_THUMB_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_THUMB_METACARPAL** = `25`

Left thumb metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_THUMB_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_THUMB_PHALANX_PROXIMAL** = `26`

Left thumb phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_THUMB_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_THUMB_PHALANX_DISTAL** = `27`

Left thumb phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_THUMB_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_THUMB_TIP** = `28`

Left thumb tip joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_INDEX_FINGER_METACARPAL** = `29`

Left index finger metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_INDEX_FINGER_PHALANX_PROXIMAL** = `30`

Left index finger phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_PHALANX_INTERMEDIATE"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_INDEX_FINGER_PHALANX_INTERMEDIATE** = `31`

Left index finger phalanx intermediate joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_INDEX_FINGER_PHALANX_DISTAL** = `32`

Left index finger phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_INDEX_FINGER_TIP** = `33`

Left index finger tip joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_MIDDLE_FINGER_METACARPAL** = `34`

Left middle finger metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_MIDDLE_FINGER_PHALANX_PROXIMAL** = `35`

Left middle finger phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_PHALANX_INTERMEDIATE"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_MIDDLE_FINGER_PHALANX_INTERMEDIATE** = `36`

Left middle finger phalanx intermediate joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_MIDDLE_FINGER_PHALANX_DISTAL** = `37`

Left middle finger phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_MIDDLE_FINGER_TIP** = `38`

Left middle finger tip joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_RING_FINGER_METACARPAL** = `39`

Left ring finger metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_RING_FINGER_PHALANX_PROXIMAL** = `40`

Left ring finger phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_PHALANX_INTERMEDIATE"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_RING_FINGER_PHALANX_INTERMEDIATE** = `41`

Left ring finger phalanx intermediate joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_RING_FINGER_PHALANX_DISTAL** = `42`

Left ring finger phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_RING_FINGER_TIP** = `43`

Left ring finger tip joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_PINKY_FINGER_METACARPAL** = `44`

Left pinky finger metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_PINKY_FINGER_PHALANX_PROXIMAL** = `45`

Left pinky finger phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_PHALANX_INTERMEDIATE"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_PINKY_FINGER_PHALANX_INTERMEDIATE** = `46`

Left pinky finger phalanx intermediate joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_PINKY_FINGER_PHALANX_DISTAL** = `47`

Left pinky finger phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_PINKY_FINGER_TIP** = `48`

Left pinky finger tip joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_HAND"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_HAND** = `49`

Right hand joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_PALM"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_PALM** = `50`

Right palm joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_WRIST"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_WRIST** = `51`

Right wrist joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_THUMB_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_THUMB_METACARPAL** = `52`

Right thumb metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_THUMB_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_THUMB_PHALANX_PROXIMAL** = `53`

Right thumb phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_THUMB_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_THUMB_PHALANX_DISTAL** = `54`

Right thumb phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_THUMB_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_THUMB_TIP** = `55`

Right thumb tip joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_INDEX_FINGER_METACARPAL** = `56`

Right index finger metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_INDEX_FINGER_PHALANX_PROXIMAL** = `57`

Right index finger phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_PHALANX_INTERMEDIATE"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_INDEX_FINGER_PHALANX_INTERMEDIATE** = `58`

Right index finger phalanx intermediate joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_INDEX_FINGER_PHALANX_DISTAL** = `59`

Right index finger phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_INDEX_FINGER_TIP** = `60`

Right index finger tip joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_MIDDLE_FINGER_METACARPAL** = `61`

Right middle finger metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_MIDDLE_FINGER_PHALANX_PROXIMAL** = `62`

Right middle finger phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_PHALANX_INTERMEDIATE"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_MIDDLE_FINGER_PHALANX_INTERMEDIATE** = `63`

Right middle finger phalanx intermediate joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_MIDDLE_FINGER_PHALANX_DISTAL** = `64`

Right middle finger phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_MIDDLE_FINGER_TIP** = `65`

Right middle finger tip joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_RING_FINGER_METACARPAL** = `66`

Right ring finger metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_RING_FINGER_PHALANX_PROXIMAL** = `67`

Right ring finger phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_PHALANX_INTERMEDIATE"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_RING_FINGER_PHALANX_INTERMEDIATE** = `68`

Right ring finger phalanx intermediate joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_RING_FINGER_PHALANX_DISTAL** = `69`

Right ring finger phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_RING_FINGER_TIP** = `70`

Right ring finger tip joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_METACARPAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_PINKY_FINGER_METACARPAL** = `71`

Right pinky finger metacarpal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_PHALANX_PROXIMAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_PINKY_FINGER_PHALANX_PROXIMAL** = `72`

Right pinky finger phalanx proximal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_PHALANX_INTERMEDIATE"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_PINKY_FINGER_PHALANX_INTERMEDIATE** = `73`

Right pinky finger phalanx intermediate joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_PHALANX_DISTAL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_PINKY_FINGER_PHALANX_DISTAL** = `74`

Right pinky finger phalanx distal joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_TIP"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_PINKY_FINGER_TIP** = `75`

Right pinky finger tip joint.

<span id="class_XRBodyTracker_constant_JOINT_LOWER_CHEST"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LOWER_CHEST** = `76`

Lower chest joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_SCAPULA"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_SCAPULA** = `77`

Left scapula joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_WRIST_TWIST"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_WRIST_TWIST** = `78`

Left wrist twist joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_SCAPULA"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_SCAPULA** = `79`

Right scapula joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_WRIST_TWIST"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_WRIST_TWIST** = `80`

Right wrist twist joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_FOOT_TWIST"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_FOOT_TWIST** = `81`

Left foot twist joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_HEEL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_HEEL** = `82`

Left heel joint.

<span id="class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FOOT"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_LEFT_MIDDLE_FOOT** = `83`

Left middle foot joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_FOOT_TWIST"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_FOOT_TWIST** = `84`

Right foot twist joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_HEEL"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_HEEL** = `85`

Right heel joint.

<span id="class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FOOT"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_RIGHT_MIDDLE_FOOT** = `86`

Right middle foot joint.

<span id="class_XRBodyTracker_constant_JOINT_MAX"></span>

[Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) **JOINT_MAX** = `87`

Represents the size of the [Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) enum.

---

<span id="enum_XRBodyTracker_JointFlags"></span>

flags **JointFlags**: [🔗](class_xrbodytracker.md#enum_XRBodyTracker_JointFlags)

<span id="class_XRBodyTracker_constant_JOINT_FLAG_ORIENTATION_VALID"></span>

[JointFlags](class_xrbodytracker.md#enum_XRBodyTracker_JointFlags) **JOINT_FLAG_ORIENTATION_VALID** = `1`

The joint's orientation data is valid.

<span id="class_XRBodyTracker_constant_JOINT_FLAG_ORIENTATION_TRACKED"></span>

[JointFlags](class_xrbodytracker.md#enum_XRBodyTracker_JointFlags) **JOINT_FLAG_ORIENTATION_TRACKED** = `2`

The joint's orientation is actively tracked. May not be set if tracking has been temporarily lost.

<span id="class_XRBodyTracker_constant_JOINT_FLAG_POSITION_VALID"></span>

[JointFlags](class_xrbodytracker.md#enum_XRBodyTracker_JointFlags) **JOINT_FLAG_POSITION_VALID** = `4`

The joint's position data is valid.

<span id="class_XRBodyTracker_constant_JOINT_FLAG_POSITION_TRACKED"></span>

[JointFlags](class_xrbodytracker.md#enum_XRBodyTracker_JointFlags) **JOINT_FLAG_POSITION_TRACKED** = `8`

The joint's position is actively tracked. May not be set if tracking has been temporarily lost.

---

### Property Descriptions

<span id="class_XRBodyTracker_property_body_flags"></span>

*BitField*\[[BodyFlags](class_xrbodytracker.md#enum_XRBodyTracker_BodyFlags)\] **body_flags** = `0` [🔗](class_xrbodytracker.md#class_XRBodyTracker_property_body_flags)

- void **set_body_flags** ( value: *BitField*\[[BodyFlags](class_xrbodytracker.md#enum_XRBodyTracker_BodyFlags)\] )
- *BitField*\[[BodyFlags](class_xrbodytracker.md#enum_XRBodyTracker_BodyFlags)\] **get_body_flags** ( )

The type of body tracking data captured.

---

<span id="class_XRBodyTracker_property_has_tracking_data"></span>

[bool](class_bool.md#class_bool) **has_tracking_data** = `false` [🔗](class_xrbodytracker.md#class_XRBodyTracker_property_has_tracking_data)

- void **set_has_tracking_data** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_has_tracking_data** ( )

If `true`, the body tracking data is valid.

---

### Method Descriptions

<span id="class_XRBodyTracker_method_get_joint_flags"></span>

*BitField*\[[JointFlags](class_xrbodytracker.md#enum_XRBodyTracker_JointFlags)\] **get_joint_flags** ( joint: [Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) ) *const* [🔗](class_xrbodytracker.md#class_XRBodyTracker_method_get_joint_flags)

Returns flags about the validity of the tracking data for the given body joint.

---

<span id="class_XRBodyTracker_method_get_joint_transform"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_joint_transform** ( joint: [Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint) ) *const* [🔗](class_xrbodytracker.md#class_XRBodyTracker_method_get_joint_transform)

Returns the transform for the given body joint.

---

<span id="class_XRBodyTracker_method_set_joint_flags"></span>

void **set_joint_flags** ( joint: [Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint), flags: *BitField*\[[JointFlags](class_xrbodytracker.md#enum_XRBodyTracker_JointFlags)\] ) [🔗](class_xrbodytracker.md#class_XRBodyTracker_method_set_joint_flags)

Sets flags about the validity of the tracking data for the given body joint.

---

<span id="class_XRBodyTracker_method_set_joint_transform"></span>

void **set_joint_transform** ( joint: [Joint](class_xrbodytracker.md#enum_XRBodyTracker_Joint), transform: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_xrbodytracker.md#class_XRBodyTracker_method_set_joint_transform)

Sets the transform for the given body joint.
