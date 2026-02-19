<span id="class_OpenXRActionSet"></span>

## OpenXRActionSet

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Collection of [OpenXRAction](class_openxraction.md#class_OpenXRAction) resources that make up an action set.

### Description

Action sets in OpenXR define a collection of actions that can be activated in unison. This allows games to easily change between different states that require different inputs or need to reinterpret inputs. For instance we could have an action set that is active when a menu is open, an action set that is active when the player is freely walking around and an action set that is active when the player is controlling a vehicle.

Action sets can contain the same action with the same name, if such action sets are active at the same time the action set with the highest priority defines which binding is active.

### Properties


| [Array](class_array.md#class_Array) | [actions](class_openxractionset.md#class_OpenXRActionSet_property_actions) | `[]` |
| --- | --- | --- |
| [String](class_string.md#class_String) | [localized_name](class_openxractionset.md#class_OpenXRActionSet_property_localized_name) | `""` |
| [int](class_int.md#class_int) | [priority](class_openxractionset.md#class_OpenXRActionSet_property_priority) | `0` |

### Methods


| void | [add_action](class_openxractionset.md#class_OpenXRActionSet_method_add_action) ( action: [OpenXRAction](class_openxraction.md#class_OpenXRAction) ) |
| --- | --- |
| [int](class_int.md#class_int) | [get_action_count](class_openxractionset.md#class_OpenXRActionSet_method_get_action_count) ( ) const |
| void | [remove_action](class_openxractionset.md#class_OpenXRActionSet_method_remove_action) ( action: [OpenXRAction](class_openxraction.md#class_OpenXRAction) ) |

---

### Property Descriptions

<span id="class_OpenXRActionSet_property_actions"></span>

[Array](class_array.md#class_Array) **actions** = `[]` [🔗](class_openxractionset.md#class_OpenXRActionSet_property_actions)

- void **set_actions** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_actions** ( )

Collection of actions for this action set.

---

<span id="class_OpenXRActionSet_property_localized_name"></span>

[String](class_string.md#class_String) **localized_name** = `""` [🔗](class_openxractionset.md#class_OpenXRActionSet_property_localized_name)

- void **set_localized_name** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_localized_name** ( )

The localized name of this action set.

---

<span id="class_OpenXRActionSet_property_priority"></span>

[int](class_int.md#class_int) **priority** = `0` [🔗](class_openxractionset.md#class_OpenXRActionSet_property_priority)

- void **set_priority** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_priority** ( )

The priority for this action set.

---

### Method Descriptions

<span id="class_OpenXRActionSet_method_add_action"></span>

void **add_action** ( action: [OpenXRAction](class_openxraction.md#class_OpenXRAction) ) [🔗](class_openxractionset.md#class_OpenXRActionSet_method_add_action)

Add an action to this action set.

---

<span id="class_OpenXRActionSet_method_get_action_count"></span>

[int](class_int.md#class_int) **get_action_count** ( ) *const* [🔗](class_openxractionset.md#class_OpenXRActionSet_method_get_action_count)

Retrieve the number of actions in our action set.

---

<span id="class_OpenXRActionSet_method_remove_action"></span>

void **remove_action** ( action: [OpenXRAction](class_openxraction.md#class_OpenXRAction) ) [🔗](class_openxractionset.md#class_OpenXRActionSet_method_remove_action)

Remove an action from this action set.
