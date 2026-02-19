<span id="class_SkeletonProfileHumanoid"></span>

## SkeletonProfileHumanoid

**Inherits:** [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) **<** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A humanoid [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) preset.

### Description

A [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) as a preset that is optimized for the human form. This exists for standardization, so all parameters are read-only.

A humanoid skeleton profile contains 56 bones divided into 4 groups: `"Body"`, `"Face"`, `"LeftHand"`, and `"RightHand"`. It is structured as follows:

.. code:: text

    Root
    └─ Hips
        ├─ LeftUpperLeg
        │  └─ LeftLowerLeg
        │     └─ LeftFoot
        │        └─ LeftToes
        ├─ RightUpperLeg
        │  └─ RightLowerLeg
        │     └─ RightFoot
        │        └─ RightToes
        └─ Spine
            └─ Chest
                └─ UpperChest
                    ├─ Neck
                    │   └─ Head
                    │       ├─ Jaw
                    │       ├─ LeftEye
                    │       └─ RightEye
                    ├─ LeftShoulder
                    │  └─ LeftUpperArm
                    │     └─ LeftLowerArm
                    │        └─ LeftHand
                    │           ├─ LeftThumbMetacarpal
                    │           │  └─ LeftThumbProximal
                    │           │    └─ LeftThumbDistal
                    │           ├─ LeftIndexProximal
                    │           │  └─ LeftIndexIntermediate
                    │           │    └─ LeftIndexDistal
                    │           ├─ LeftMiddleProximal
                    │           │  └─ LeftMiddleIntermediate
                    │           │    └─ LeftMiddleDistal
                    │           ├─ LeftRingProximal
                    │           │  └─ LeftRingIntermediate
                    │           │    └─ LeftRingDistal
                    │           └─ LeftLittleProximal
                    │              └─ LeftLittleIntermediate
                    │                └─ LeftLittleDistal
                    └─ RightShoulder
                       └─ RightUpperArm
                          └─ RightLowerArm
                             └─ RightHand
                                ├─ RightThumbMetacarpal
                                │  └─ RightThumbProximal
                                │     └─ RightThumbDistal
                                ├─ RightIndexProximal
                                │  └─ RightIndexIntermediate
                                │     └─ RightIndexDistal
                                ├─ RightMiddleProximal
                                │  └─ RightMiddleIntermediate
                                │     └─ RightMiddleDistal
                                ├─ RightRingProximal
                                │  └─ RightRingIntermediate
                                │     └─ RightRingDistal
                                └─ RightLittleProximal
                                   └─ RightLittleIntermediate
                                     └─ RightLittleDistal

### Tutorials

- [Retargeting 3D Skeletons](../tutorials/assets_pipeline/retargeting_3d_skeletons.md)

### Properties


| [int](class_int.md#class_int) | bone_size | `56` (overrides [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile_property_bone_size)) |
| --- | --- | --- |
| [int](class_int.md#class_int) | group_size | `4` (overrides [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile_property_group_size)) |
| [StringName](class_stringname.md#class_StringName) | root_bone | `&"Root"` (overrides [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile_property_root_bone)) |
| [StringName](class_stringname.md#class_StringName) | scale_base_bone | `&"Hips"` (overrides [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile_property_scale_base_bone)) |
