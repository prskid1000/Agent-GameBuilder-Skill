<span id="class_OpenXRAction"></span>

## OpenXRAction

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

An OpenXR action.

### Description

This resource defines an OpenXR action. Actions can be used both for inputs (buttons, joysticks, triggers, etc.) and outputs (haptics).

OpenXR performs automatic conversion between action type and input type whenever possible. An analog trigger bound to a boolean action will thus return `false` if the trigger is depressed and `true` if pressed fully.

Actions are not directly bound to specific devices, instead OpenXR recognizes a limited number of top level paths that identify devices by usage. We can restrict which devices an action can be bound to by these top level paths. For instance an action that should only be used for hand held controllers can have the top level paths "/user/hand/left" and "/user/hand/right" associated with them. See the reserved path section in the OpenXR specification for more info on the top level paths.

Note that the name of the resource is used to register the action with.

### Properties


| [ActionType](class_openxraction.md#enum_OpenXRAction_ActionType) | [action_type](class_openxraction.md#class_OpenXRAction_property_action_type) | `1` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [localized_name](class_openxraction.md#class_OpenXRAction_property_localized_name) | `""` |
| [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) | [toplevel_paths](class_openxraction.md#class_OpenXRAction_property_toplevel_paths) | `PackedStringArray()` |

---

### Enumerations

<span id="enum_OpenXRAction_ActionType"></span>

enum **ActionType**: [🔗](class_openxraction.md#enum_OpenXRAction_ActionType)

<span id="class_OpenXRAction_constant_OPENXR_ACTION_BOOL"></span>

[ActionType](class_openxraction.md#enum_OpenXRAction_ActionType) **OPENXR_ACTION_BOOL** = `0`

This action provides a boolean value.

<span id="class_OpenXRAction_constant_OPENXR_ACTION_FLOAT"></span>

[ActionType](class_openxraction.md#enum_OpenXRAction_ActionType) **OPENXR_ACTION_FLOAT** = `1`

This action provides a float value between `0.0` and `1.0` for any analog input such as triggers.

<span id="class_OpenXRAction_constant_OPENXR_ACTION_VECTOR2"></span>

[ActionType](class_openxraction.md#enum_OpenXRAction_ActionType) **OPENXR_ACTION_VECTOR2** = `2`

This action provides a [Vector2](class_vector2.md#class_Vector2) value and can be bound to embedded trackpads and joysticks.

<span id="class_OpenXRAction_constant_OPENXR_ACTION_POSE"></span>

[ActionType](class_openxraction.md#enum_OpenXRAction_ActionType) **OPENXR_ACTION_POSE** = `3`

.. container:: contribute

	There is currently no description for this enum. Please help us by contributing one!

---

### Property Descriptions

<span id="class_OpenXRAction_property_action_type"></span>

[ActionType](class_openxraction.md#enum_OpenXRAction_ActionType) **action_type** = `1` [🔗](class_openxraction.md#class_OpenXRAction_property_action_type)

- void **set_action_type** ( value: [ActionType](class_openxraction.md#enum_OpenXRAction_ActionType) )
- [ActionType](class_openxraction.md#enum_OpenXRAction_ActionType) **get_action_type** ( )

The type of action.

---

<span id="class_OpenXRAction_property_localized_name"></span>

[String](class_string.md#class_String) **localized_name** = `""` [🔗](class_openxraction.md#class_OpenXRAction_property_localized_name)

- void **set_localized_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_localized_name** ( )

The localized description of this action.

---

<span id="class_OpenXRAction_property_toplevel_paths"></span>

[PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **toplevel_paths** = `PackedStringArray()` [🔗](class_openxraction.md#class_OpenXRAction_property_toplevel_paths)

- void **set_toplevel_paths** ( value: [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) )
- [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) **get_toplevel_paths** ( )

A collections of toplevel paths to which this action can be bound.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedStringArray](class_packedstringarray.md#class_PackedStringArray) for more details.
