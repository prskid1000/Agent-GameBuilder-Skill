<span id="class_SkeletonModificationStack2D"></span>

## SkeletonModificationStack2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A resource that holds a stack of [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) s.

### Description

This resource is used by the Skeleton and holds a stack of [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) s.

This controls the order of the modifications and how they are applied. Modification order is especially important for full-body IK setups, as you need to execute the modifications in the correct order to get the desired results. For example, you want to execute a modification on the spine *before* the arms on a humanoid skeleton.

This resource also controls how strongly all of the modifications are applied to the [Skeleton2D](class_skeleton2d.md#class_Skeleton2D).

### Properties


| [bool](class_bool.md#class_bool) | [enabled](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_property_enabled) | `false` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [modification_count](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_property_modification_count) | `0` |
| [float](class_float.md#class_float) | [strength](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_property_strength) | `1.0` |

### Methods


| void | [add_modification](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_add_modification) ( modification: [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) ) |
| --- | --- |
| void | [delete_modification](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_delete_modification) ( mod_idx: [int](class_int.md#class_int) ) |
| void | [enable_all_modifications](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_enable_all_modifications) ( enabled: [bool](class_bool.md#class_bool) ) |
| void | [execute](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_execute) ( delta: [float](class_float.md#class_float), execution_mode: [int](class_int.md#class_int) ) |
| [bool](class_bool.md#class_bool) | [get_is_setup](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_get_is_setup) ( ) const |
| [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) | [get_modification](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_get_modification) ( mod_idx: [int](class_int.md#class_int) ) const |
| [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) | [get_skeleton](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_get_skeleton) ( ) const |
| void | [set_modification](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_set_modification) ( mod_idx: [int](class_int.md#class_int), modification: [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) ) |
| void | [setup](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_setup) ( ) |

---

### Property Descriptions

<span id="class_SkeletonModificationStack2D_property_enabled"></span>

[bool](class_bool.md#class_bool) **enabled** = `false` [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_property_enabled)

- void **set_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enabled** ( )

If `true`, the modification's in the stack will be called. This is handled automatically through the [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) node.

---

<span id="class_SkeletonModificationStack2D_property_modification_count"></span>

[int](class_int.md#class_int) **modification_count** = `0` [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_property_modification_count)

- void **set_modification_count** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_modification_count** ( )

The number of modifications in the stack.

---

<span id="class_SkeletonModificationStack2D_property_strength"></span>

[float](class_float.md#class_float) **strength** = `1.0` [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_property_strength)

- void **set_strength** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_strength** ( )

The interpolation strength of the modifications in stack. A value of `0` will make it where the modifications are not applied, a strength of `0.5` will be half applied, and a strength of `1` will allow the modifications to be fully applied and override the [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) [Bone2D](class_bone2d.md#class_Bone2D) poses.

---

### Method Descriptions

<span id="class_SkeletonModificationStack2D_method_add_modification"></span>

void **add_modification** ( modification: [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) ) [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_add_modification)

Adds the passed-in [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) to the stack.

---

<span id="class_SkeletonModificationStack2D_method_delete_modification"></span>

void **delete_modification** ( mod_idx: [int](class_int.md#class_int) ) [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_delete_modification)

Deletes the [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) at the index position `mod_idx`, if it exists.

---

<span id="class_SkeletonModificationStack2D_method_enable_all_modifications"></span>

void **enable_all_modifications** ( enabled: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_enable_all_modifications)

Enables all [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) s in the stack.

---

<span id="class_SkeletonModificationStack2D_method_execute"></span>

void **execute** ( delta: [float](class_float.md#class_float), execution_mode: [int](class_int.md#class_int) ) [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_execute)

Executes all of the [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) s in the stack that use the same execution mode as the passed-in `execution_mode`, starting from index `0` to [modification_count](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_property_modification_count).

 **Note:** The order of the modifications can matter depending on the modifications. For example, modifications on a spine should operate before modifications on the arms in order to get proper results.

---

<span id="class_SkeletonModificationStack2D_method_get_is_setup"></span>

[bool](class_bool.md#class_bool) **get_is_setup** ( ) *const* [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_get_is_setup)

Returns a boolean that indicates whether the modification stack is setup and can execute.

---

<span id="class_SkeletonModificationStack2D_method_get_modification"></span>

[SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) **get_modification** ( mod_idx: [int](class_int.md#class_int) ) *const* [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_get_modification)

Returns the [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) at the passed-in index, `mod_idx`.

---

<span id="class_SkeletonModificationStack2D_method_get_skeleton"></span>

[Skeleton2D](class_skeleton2d.md#class_Skeleton2D) **get_skeleton** ( ) *const* [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_get_skeleton)

Returns the [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) node that the SkeletonModificationStack2D is bound to.

---

<span id="class_SkeletonModificationStack2D_method_set_modification"></span>

void **set_modification** ( mod_idx: [int](class_int.md#class_int), modification: [SkeletonModification2D](class_skeletonmodification2d.md#class_SkeletonModification2D) ) [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_set_modification)

Sets the modification at `mod_idx` to the passed-in modification, `modification`.

---

<span id="class_SkeletonModificationStack2D_method_setup"></span>

void **setup** ( ) [🔗](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_setup)

Sets up the modification stack so it can execute. This function should be called by [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) and shouldn't be manually called unless you know what you are doing.
