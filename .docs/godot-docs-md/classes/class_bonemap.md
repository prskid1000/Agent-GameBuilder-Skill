<span id="class_BoneMap"></span>

## BoneMap

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Describes a mapping of bone names for retargeting [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) into common names defined by a [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile).

### Description

This class contains a dictionary that uses a list of bone names in [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) as key names.

By assigning the actual [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) bone name as the key value, it maps the [Skeleton3D](class_skeleton3d.md#class_Skeleton3D) to the [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile).

### Tutorials

- [Retargeting 3D Skeletons](../tutorials/assets_pipeline/retargeting_3d_skeletons.md)

### Properties


| [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) | [profile](class_bonemap.md#class_BoneMap_property_profile) |
| --- | --- |

### Methods


| [StringName](class_stringname.md#class_StringName) | [find_profile_bone_name](class_bonemap.md#class_BoneMap_method_find_profile_bone_name) ( skeleton_bone_name: [StringName](class_stringname.md#class_StringName) ) const |
| --- | --- |
| [StringName](class_stringname.md#class_StringName) | [get_skeleton_bone_name](class_bonemap.md#class_BoneMap_method_get_skeleton_bone_name) ( profile_bone_name: [StringName](class_stringname.md#class_StringName) ) const |
| void | [set_skeleton_bone_name](class_bonemap.md#class_BoneMap_method_set_skeleton_bone_name) ( profile_bone_name: [StringName](class_stringname.md#class_StringName), skeleton_bone_name: [StringName](class_stringname.md#class_StringName) ) |

---

### Signals

<span id="class_BoneMap_signal_bone_map_updated"></span>

**bone_map_updated** ( ) [🔗](class_bonemap.md#class_BoneMap_signal_bone_map_updated)

This signal is emitted when change the key value in the **BoneMap**. This is used to validate mapping and to update **BoneMap** editor.

---

<span id="class_BoneMap_signal_profile_updated"></span>

**profile_updated** ( ) [🔗](class_bonemap.md#class_BoneMap_signal_profile_updated)

This signal is emitted when change the value in profile or change the reference of profile. This is used to update key names in the **BoneMap** and to redraw the **BoneMap** editor.

---

### Property Descriptions

<span id="class_BoneMap_property_profile"></span>

[SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) **profile** [🔗](class_bonemap.md#class_BoneMap_property_profile)

- void **set_profile** ( value: [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) )
- [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) **get_profile** ( )

A [SkeletonProfile](class_skeletonprofile.md#class_SkeletonProfile) of the mapping target. Key names in the **BoneMap** are synchronized with it.

---

### Method Descriptions

<span id="class_BoneMap_method_find_profile_bone_name"></span>

[StringName](class_stringname.md#class_StringName) **find_profile_bone_name** ( skeleton_bone_name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_bonemap.md#class_BoneMap_method_find_profile_bone_name)

Returns a profile bone name having `skeleton_bone_name`. If not found, an empty [StringName](class_stringname.md#class_StringName) will be returned.

In the retargeting process, the returned bone name is the bone name of the target skeleton.

---

<span id="class_BoneMap_method_get_skeleton_bone_name"></span>

[StringName](class_stringname.md#class_StringName) **get_skeleton_bone_name** ( profile_bone_name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_bonemap.md#class_BoneMap_method_get_skeleton_bone_name)

Returns a skeleton bone name is mapped to `profile_bone_name`.

In the retargeting process, the returned bone name is the bone name of the source skeleton.

---

<span id="class_BoneMap_method_set_skeleton_bone_name"></span>

void **set_skeleton_bone_name** ( profile_bone_name: [StringName](class_stringname.md#class_StringName), skeleton_bone_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_bonemap.md#class_BoneMap_method_set_skeleton_bone_name)

Maps a skeleton bone name to `profile_bone_name`.

In the retargeting process, the setting bone name is the bone name of the source skeleton.
