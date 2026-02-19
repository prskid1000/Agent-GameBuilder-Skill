<span id="class_SkeletonProfile"></span>

## SkeletonProfile

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class_SkeletonProfileHumanoid)

Base class for a profile of a virtual skeleton used as a target for retargeting.

### Description

This resource is used in [EditorScenePostImport](class_editorscenepostimport.md#class_EditorScenePostImport). Some parameters are referring to bones in [Skeleton3D](class_skeleton3d.md#class_Skeleton3D), [Skin](class_skin.md#class_Skin), [Animation](class_animation.md#class_Animation), and some other nodes are rewritten based on the parameters of **SkeletonProfile**.

 **Note:** These parameters need to be set only when creating a custom profile. In [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class_SkeletonProfileHumanoid), they are defined internally as read-only values.

### Tutorials

- [Retargeting 3D Skeletons](../tutorials/assets_pipeline/retargeting_3d_skeletons.md)

### Properties


| [int](class_int.md#class_int) | [bone_size](class_skeletonprofile.md#class_SkeletonProfile_property_bone_size) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [group_size](class_skeletonprofile.md#class_SkeletonProfile_property_group_size) | `0` |
| [StringName](class_stringname.md#class_StringName) | [root_bone](class_skeletonprofile.md#class_SkeletonProfile_property_root_bone) | `&""` |
| [StringName](class_stringname.md#class_StringName) | [scale_base_bone](class_skeletonprofile.md#class_SkeletonProfile_property_scale_base_bone) | `&""` |

### Methods


| [int](class_int.md#class_int) | [find_bone](class_skeletonprofile.md#class_SkeletonProfile_method_find_bone) ( bone_name: [StringName](class_stringname.md#class_StringName) ) const |
| --- | --- |
| [StringName](class_stringname.md#class_StringName) | [get_bone_name](class_skeletonprofile.md#class_SkeletonProfile_method_get_bone_name) ( bone_idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_bone_parent](class_skeletonprofile.md#class_SkeletonProfile_method_get_bone_parent) ( bone_idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_bone_tail](class_skeletonprofile.md#class_SkeletonProfile_method_get_bone_tail) ( bone_idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_group](class_skeletonprofile.md#class_SkeletonProfile_method_get_group) ( bone_idx: [int](class_int.md#class_int) ) const |
| [StringName](class_stringname.md#class_StringName) | [get_group_name](class_skeletonprofile.md#class_SkeletonProfile_method_get_group_name) ( group_idx: [int](class_int.md#class_int) ) const |
| [Vector2](class_vector2.md#class_Vector2) | [get_handle_offset](class_skeletonprofile.md#class_SkeletonProfile_method_get_handle_offset) ( bone_idx: [int](class_int.md#class_int) ) const |
| [Transform3D](class_transform3d.md#class_Transform3D) | [get_reference_pose](class_skeletonprofile.md#class_SkeletonProfile_method_get_reference_pose) ( bone_idx: [int](class_int.md#class_int) ) const |
| [TailDirection](class_skeletonprofile.md#enum_SkeletonProfile_TailDirection) | [get_tail_direction](class_skeletonprofile.md#class_SkeletonProfile_method_get_tail_direction) ( bone_idx: [int](class_int.md#class_int) ) const |
| [Texture2D](class_texture2d.md#class_Texture2D) | [get_texture](class_skeletonprofile.md#class_SkeletonProfile_method_get_texture) ( group_idx: [int](class_int.md#class_int) ) const |
| [bool](class_bool.md#class_bool) | [is_required](class_skeletonprofile.md#class_SkeletonProfile_method_is_required) ( bone_idx: [int](class_int.md#class_int) ) const |
| void | [set_bone_name](class_skeletonprofile.md#class_SkeletonProfile_method_set_bone_name) ( bone_idx: [int](class_int.md#class_int), bone_name: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_bone_parent](class_skeletonprofile.md#class_SkeletonProfile_method_set_bone_parent) ( bone_idx: [int](class_int.md#class_int), bone_parent: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_bone_tail](class_skeletonprofile.md#class_SkeletonProfile_method_set_bone_tail) ( bone_idx: [int](class_int.md#class_int), bone_tail: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_group](class_skeletonprofile.md#class_SkeletonProfile_method_set_group) ( bone_idx: [int](class_int.md#class_int), group: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_group_name](class_skeletonprofile.md#class_SkeletonProfile_method_set_group_name) ( group_idx: [int](class_int.md#class_int), group_name: [StringName](class_stringname.md#class_StringName) ) |
| void | [set_handle_offset](class_skeletonprofile.md#class_SkeletonProfile_method_set_handle_offset) ( bone_idx: [int](class_int.md#class_int), handle_offset: [Vector2](class_vector2.md#class_Vector2) ) |
| void | [set_reference_pose](class_skeletonprofile.md#class_SkeletonProfile_method_set_reference_pose) ( bone_idx: [int](class_int.md#class_int), bone_name: [Transform3D](class_transform3d.md#class_Transform3D) ) |
| void | [set_required](class_skeletonprofile.md#class_SkeletonProfile_method_set_required) ( bone_idx: [int](class_int.md#class_int), required: [bool](class_bool.md#class_bool) ) |
| void | [set_tail_direction](class_skeletonprofile.md#class_SkeletonProfile_method_set_tail_direction) ( bone_idx: [int](class_int.md#class_int), tail_direction: [TailDirection](class_skeletonprofile.md#enum_SkeletonProfile_TailDirection) ) |
| void | [set_texture](class_skeletonprofile.md#class_SkeletonProfile_method_set_texture) ( group_idx: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) |

---

### Signals

<span id="class_SkeletonProfile_signal_profile_updated"></span>

**profile_updated** ( ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_signal_profile_updated)

This signal is emitted when change the value in profile. This is used to update key name in the [BoneMap](class_bonemap.md#class_BoneMap) and to redraw the [BoneMap](class_bonemap.md#class_BoneMap) editor.

 **Note:** This signal is not connected directly to editor to simplify the reference, instead it is passed on to editor through the [BoneMap](class_bonemap.md#class_BoneMap).

---

### Enumerations

<span id="enum_SkeletonProfile_TailDirection"></span>

enum **TailDirection**: [🔗](class_skeletonprofile.md#enum_SkeletonProfile_TailDirection)

<span id="class_SkeletonProfile_constant_TAIL_DIRECTION_AVERAGE_CHILDREN"></span>

[TailDirection](class_skeletonprofile.md#enum_SkeletonProfile_TailDirection) **TAIL_DIRECTION_AVERAGE_CHILDREN** = `0`

Direction to the average coordinates of bone children.

<span id="class_SkeletonProfile_constant_TAIL_DIRECTION_SPECIFIC_CHILD"></span>

[TailDirection](class_skeletonprofile.md#enum_SkeletonProfile_TailDirection) **TAIL_DIRECTION_SPECIFIC_CHILD** = `1`

Direction to the coordinates of specified bone child.

<span id="class_SkeletonProfile_constant_TAIL_DIRECTION_END"></span>

[TailDirection](class_skeletonprofile.md#enum_SkeletonProfile_TailDirection) **TAIL_DIRECTION_END** = `2`

Direction is not calculated.

---

### Property Descriptions

<span id="class_SkeletonProfile_property_bone_size"></span>

[int](class_int.md#class_int) **bone_size** = `0` [🔗](class_skeletonprofile.md#class_SkeletonProfile_property_bone_size)

- void **set_bone_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_bone_size** ( )

The amount of bones in retargeting section's [BoneMap](class_bonemap.md#class_BoneMap) editor. For example, [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class_SkeletonProfileHumanoid) has 56 bones.

The size of elements in [BoneMap](class_bonemap.md#class_BoneMap) updates when changing this property in it's assigned **SkeletonProfile**.

---

<span id="class_SkeletonProfile_property_group_size"></span>

[int](class_int.md#class_int) **group_size** = `0` [🔗](class_skeletonprofile.md#class_SkeletonProfile_property_group_size)

- void **set_group_size** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_group_size** ( )

The amount of groups of bones in retargeting section's [BoneMap](class_bonemap.md#class_BoneMap) editor. For example, [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class_SkeletonProfileHumanoid) has 4 groups.

This property exists to separate the bone list into several sections in the editor.

---

<span id="class_SkeletonProfile_property_root_bone"></span>

[StringName](class_stringname.md#class_StringName) **root_bone** = `&""` [🔗](class_skeletonprofile.md#class_SkeletonProfile_property_root_bone)

- void **set_root_bone** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_root_bone** ( )

A bone name that will be used as the root bone in [AnimationTree](class_animationtree.md#class_AnimationTree). This should be the bone of the parent of hips that exists at the world origin.

---

<span id="class_SkeletonProfile_property_scale_base_bone"></span>

[StringName](class_stringname.md#class_StringName) **scale_base_bone** = `&""` [🔗](class_skeletonprofile.md#class_SkeletonProfile_property_scale_base_bone)

- void **set_scale_base_bone** ( value: [StringName](class_stringname.md#class_StringName) )
- [StringName](class_stringname.md#class_StringName) **get_scale_base_bone** ( )

A bone name which will use model's height as the coefficient for normalization. For example, [SkeletonProfileHumanoid](class_skeletonprofilehumanoid.md#class_SkeletonProfileHumanoid) defines it as `Hips`.

---

### Method Descriptions

<span id="class_SkeletonProfile_method_find_bone"></span>

[int](class_int.md#class_int) **find_bone** ( bone_name: [StringName](class_stringname.md#class_StringName) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_find_bone)

Returns the bone index that matches `bone_name` as its name.

---

<span id="class_SkeletonProfile_method_get_bone_name"></span>

[StringName](class_stringname.md#class_StringName) **get_bone_name** ( bone_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_get_bone_name)

Returns the name of the bone at `bone_idx` that will be the key name in the [BoneMap](class_bonemap.md#class_BoneMap).

In the retargeting process, the returned bone name is the bone name of the target skeleton.

---

<span id="class_SkeletonProfile_method_get_bone_parent"></span>

[StringName](class_stringname.md#class_StringName) **get_bone_parent** ( bone_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_get_bone_parent)

Returns the name of the bone which is the parent to the bone at `bone_idx`. The result is empty if the bone has no parent.

---

<span id="class_SkeletonProfile_method_get_bone_tail"></span>

[StringName](class_stringname.md#class_StringName) **get_bone_tail** ( bone_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_get_bone_tail)

Returns the name of the bone which is the tail of the bone at `bone_idx`.

---

<span id="class_SkeletonProfile_method_get_group"></span>

[StringName](class_stringname.md#class_StringName) **get_group** ( bone_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_get_group)

Returns the group of the bone at `bone_idx`.

---

<span id="class_SkeletonProfile_method_get_group_name"></span>

[StringName](class_stringname.md#class_StringName) **get_group_name** ( group_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_get_group_name)

Returns the name of the group at `group_idx` that will be the drawing group in the [BoneMap](class_bonemap.md#class_BoneMap) editor.

---

<span id="class_SkeletonProfile_method_get_handle_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **get_handle_offset** ( bone_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_get_handle_offset)

Returns the offset of the bone at `bone_idx` that will be the button position in the [BoneMap](class_bonemap.md#class_BoneMap) editor.

This is the offset with origin at the top left corner of the square.

---

<span id="class_SkeletonProfile_method_get_reference_pose"></span>

[Transform3D](class_transform3d.md#class_Transform3D) **get_reference_pose** ( bone_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_get_reference_pose)

Returns the reference pose transform for bone `bone_idx`.

---

<span id="class_SkeletonProfile_method_get_tail_direction"></span>

[TailDirection](class_skeletonprofile.md#enum_SkeletonProfile_TailDirection) **get_tail_direction** ( bone_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_get_tail_direction)

Returns the tail direction of the bone at `bone_idx`.

---

<span id="class_SkeletonProfile_method_get_texture"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **get_texture** ( group_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_get_texture)

Returns the texture of the group at `group_idx` that will be the drawing group background image in the [BoneMap](class_bonemap.md#class_BoneMap) editor.

---

<span id="class_SkeletonProfile_method_is_required"></span>

[bool](class_bool.md#class_bool) **is_required** ( bone_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_is_required)

Returns whether the bone at `bone_idx` is required for retargeting.

This value is used by the bone map editor. If this method returns `true`, and no bone is assigned, the handle color will be red on the bone map editor.

---

<span id="class_SkeletonProfile_method_set_bone_name"></span>

void **set_bone_name** ( bone_idx: [int](class_int.md#class_int), bone_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_bone_name)

Sets the name of the bone at `bone_idx` that will be the key name in the [BoneMap](class_bonemap.md#class_BoneMap).

In the retargeting process, the setting bone name is the bone name of the target skeleton.

---

<span id="class_SkeletonProfile_method_set_bone_parent"></span>

void **set_bone_parent** ( bone_idx: [int](class_int.md#class_int), bone_parent: [StringName](class_stringname.md#class_StringName) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_bone_parent)

Sets the bone with name `bone_parent` as the parent of the bone at `bone_idx`. If an empty string is passed, then the bone has no parent.

---

<span id="class_SkeletonProfile_method_set_bone_tail"></span>

void **set_bone_tail** ( bone_idx: [int](class_int.md#class_int), bone_tail: [StringName](class_stringname.md#class_StringName) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_bone_tail)

Sets the bone with name `bone_tail` as the tail of the bone at `bone_idx`.

---

<span id="class_SkeletonProfile_method_set_group"></span>

void **set_group** ( bone_idx: [int](class_int.md#class_int), group: [StringName](class_stringname.md#class_StringName) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_group)

Sets the group of the bone at `bone_idx`.

---

<span id="class_SkeletonProfile_method_set_group_name"></span>

void **set_group_name** ( group_idx: [int](class_int.md#class_int), group_name: [StringName](class_stringname.md#class_StringName) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_group_name)

Sets the name of the group at `group_idx` that will be the drawing group in the [BoneMap](class_bonemap.md#class_BoneMap) editor.

---

<span id="class_SkeletonProfile_method_set_handle_offset"></span>

void **set_handle_offset** ( bone_idx: [int](class_int.md#class_int), handle_offset: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_handle_offset)

Sets the offset of the bone at `bone_idx` that will be the button position in the [BoneMap](class_bonemap.md#class_BoneMap) editor.

This is the offset with origin at the top left corner of the square.

---

<span id="class_SkeletonProfile_method_set_reference_pose"></span>

void **set_reference_pose** ( bone_idx: [int](class_int.md#class_int), bone_name: [Transform3D](class_transform3d.md#class_Transform3D) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_reference_pose)

Sets the reference pose transform for bone `bone_idx`.

---

<span id="class_SkeletonProfile_method_set_required"></span>

void **set_required** ( bone_idx: [int](class_int.md#class_int), required: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_required)

Sets the required status for bone `bone_idx` to `required`.

---

<span id="class_SkeletonProfile_method_set_tail_direction"></span>

void **set_tail_direction** ( bone_idx: [int](class_int.md#class_int), tail_direction: [TailDirection](class_skeletonprofile.md#enum_SkeletonProfile_TailDirection) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_tail_direction)

Sets the tail direction of the bone at `bone_idx`.

 **Note:** This only specifies the method of calculation. The actual coordinates required should be stored in an external skeleton, so the calculation itself needs to be done externally.

---

<span id="class_SkeletonProfile_method_set_texture"></span>

void **set_texture** ( group_idx: [int](class_int.md#class_int), texture: [Texture2D](class_texture2d.md#class_Texture2D) ) [🔗](class_skeletonprofile.md#class_SkeletonProfile_method_set_texture)

Sets the texture of the group at `group_idx` that will be the drawing group background image in the [BoneMap](class_bonemap.md#class_BoneMap) editor.
