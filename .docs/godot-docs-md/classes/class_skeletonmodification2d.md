<span id="class_SkeletonModification2D"></span>

## SkeletonModification2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

**Inherited By:** [SkeletonModification2DCCDIK](class_skeletonmodification2dccdik.md#class_SkeletonModification2DCCDIK), [SkeletonModification2DFABRIK](class_skeletonmodification2dfabrik.md#class_SkeletonModification2DFABRIK), [SkeletonModification2DJiggle](class_skeletonmodification2djiggle.md#class_SkeletonModification2DJiggle), [SkeletonModification2DLookAt](class_skeletonmodification2dlookat.md#class_SkeletonModification2DLookAt), [SkeletonModification2DPhysicalBones](class_skeletonmodification2dphysicalbones.md#class_SkeletonModification2DPhysicalBones), [SkeletonModification2DStackHolder](class_skeletonmodification2dstackholder.md#class_SkeletonModification2DStackHolder), [SkeletonModification2DTwoBoneIK](class_skeletonmodification2dtwoboneik.md#class_SkeletonModification2DTwoBoneIK)

Base class for resources that operate on [Bone2D](class_bone2d.md#class_Bone2D) s in a [Skeleton2D](class_skeleton2d.md#class_Skeleton2D).

### Description

This resource provides an interface that can be expanded so code that operates on [Bone2D](class_bone2d.md#class_Bone2D) nodes in a [Skeleton2D](class_skeleton2d.md#class_Skeleton2D) can be mixed and matched together to create complex interactions.

This is used to provide Godot with a flexible and powerful Inverse Kinematics solution that can be adapted for many different uses.

### Properties


| [bool](class_bool.md#class_bool) | [enabled](class_skeletonmodification2d.md#class_SkeletonModification2D_property_enabled) | `true` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [execution_mode](class_skeletonmodification2d.md#class_SkeletonModification2D_property_execution_mode) | `0` |

### Methods


| void | [_draw_editor_gizmo](class_skeletonmodification2d.md#class_SkeletonModification2D_private_method__draw_editor_gizmo) ( ) virtual |
| --- | --- |
| void | [_execute](class_skeletonmodification2d.md#class_SkeletonModification2D_private_method__execute) ( delta: [float](class_float.md#class_float) ) virtual |
| void | [_setup_modification](class_skeletonmodification2d.md#class_SkeletonModification2D_private_method__setup_modification) ( modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) ) virtual |
| [float](class_float.md#class_float) | [clamp_angle](class_skeletonmodification2d.md#class_SkeletonModification2D_method_clamp_angle) ( angle: [float](class_float.md#class_float), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float), invert: [bool](class_bool.md#class_bool) ) |
| [bool](class_bool.md#class_bool) | [get_editor_draw_gizmo](class_skeletonmodification2d.md#class_SkeletonModification2D_method_get_editor_draw_gizmo) ( ) const |
| [bool](class_bool.md#class_bool) | [get_is_setup](class_skeletonmodification2d.md#class_SkeletonModification2D_method_get_is_setup) ( ) const |
| [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) | [get_modification_stack](class_skeletonmodification2d.md#class_SkeletonModification2D_method_get_modification_stack) ( ) |
| void | [set_editor_draw_gizmo](class_skeletonmodification2d.md#class_SkeletonModification2D_method_set_editor_draw_gizmo) ( draw_gizmo: [bool](class_bool.md#class_bool) ) |
| void | [set_is_setup](class_skeletonmodification2d.md#class_SkeletonModification2D_method_set_is_setup) ( is_setup: [bool](class_bool.md#class_bool) ) |

---

### Property Descriptions

<span id="class_SkeletonModification2D_property_enabled"></span>

[bool](class_bool.md#class_bool) **enabled** = `true` [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_property_enabled)

- void **set_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_enabled** ( )

If `true`, the modification's [_execute()](class_skeletonmodification2d.md#class_SkeletonModification2D_private_method__execute) function will be called by the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D).

---

<span id="class_SkeletonModification2D_property_execution_mode"></span>

[int](class_int.md#class_int) **execution_mode** = `0` [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_property_execution_mode)

- void **set_execution_mode** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_execution_mode** ( )

The execution mode for the modification. This tells the modification stack when to execute the modification. Some modifications have settings that are only available in certain execution modes.

---

### Method Descriptions

<span id="class_SkeletonModification2D_private_method__draw_editor_gizmo"></span>

void **_draw_editor_gizmo** ( ) *virtual* [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_private_method__draw_editor_gizmo)

Used for drawing **editor-only** modification gizmos. This function will only be called in the Godot editor and can be overridden to draw custom gizmos.

 **Note:** You will need to use the Skeleton2D from [SkeletonModificationStack2D.get_skeleton()](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D_method_get_skeleton) and it's draw functions, as the **SkeletonModification2D** resource cannot draw on its own.

---

<span id="class_SkeletonModification2D_private_method__execute"></span>

void **_execute** ( delta: [float](class_float.md#class_float) ) *virtual* [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_private_method__execute)

Executes the given modification. This is where the modification performs whatever function it is designed to do.

---

<span id="class_SkeletonModification2D_private_method__setup_modification"></span>

void **_setup_modification** ( modification_stack: [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) ) *virtual* [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_private_method__setup_modification)

Called when the modification is setup. This is where the modification performs initialization.

---

<span id="class_SkeletonModification2D_method_clamp_angle"></span>

[float](class_float.md#class_float) **clamp_angle** ( angle: [float](class_float.md#class_float), min: [float](class_float.md#class_float), max: [float](class_float.md#class_float), invert: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_method_clamp_angle)

Takes an angle and clamps it so it is within the passed-in `min` and `max` range. `invert` will inversely clamp the angle, clamping it to the range outside of the given bounds.

---

<span id="class_SkeletonModification2D_method_get_editor_draw_gizmo"></span>

[bool](class_bool.md#class_bool) **get_editor_draw_gizmo** ( ) *const* [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_method_get_editor_draw_gizmo)

Returns whether this modification will call [_draw_editor_gizmo()](class_skeletonmodification2d.md#class_SkeletonModification2D_private_method__draw_editor_gizmo) in the Godot editor to draw modification-specific gizmos.

---

<span id="class_SkeletonModification2D_method_get_is_setup"></span>

[bool](class_bool.md#class_bool) **get_is_setup** ( ) *const* [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_method_get_is_setup)

Returns whether this modification has been successfully setup or not.

---

<span id="class_SkeletonModification2D_method_get_modification_stack"></span>

[SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) **get_modification_stack** ( ) [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_method_get_modification_stack)

Returns the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) that this modification is bound to. Through the modification stack, you can access the Skeleton2D the modification is operating on.

---

<span id="class_SkeletonModification2D_method_set_editor_draw_gizmo"></span>

void **set_editor_draw_gizmo** ( draw_gizmo: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_method_set_editor_draw_gizmo)

Sets whether this modification will call [_draw_editor_gizmo()](class_skeletonmodification2d.md#class_SkeletonModification2D_private_method__draw_editor_gizmo) in the Godot editor to draw modification-specific gizmos.

---

<span id="class_SkeletonModification2D_method_set_is_setup"></span>

void **set_is_setup** ( is_setup: [bool](class_bool.md#class_bool) ) [🔗](class_skeletonmodification2d.md#class_SkeletonModification2D_method_set_is_setup)

Manually allows you to set the setup state of the modification. This function should only rarely be used, as the [SkeletonModificationStack2D](class_skeletonmodificationstack2d.md#class_SkeletonModificationStack2D) the modification is bound to should handle setting the modification up.
