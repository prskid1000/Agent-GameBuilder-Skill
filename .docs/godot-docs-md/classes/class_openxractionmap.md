<span id="class_OpenXRActionMap"></span>

## OpenXRActionMap

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

Collection of [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) and [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) resources for the OpenXR module.

### Description

OpenXR uses an action system similar to Godots Input map system to bind inputs and outputs on various types of XR controllers to named actions. OpenXR specifies more detail on these inputs and outputs than Godot supports.

Another important distinction is that OpenXR offers no control over these bindings. The bindings we register are suggestions, it is up to the XR runtime to offer users the ability to change these bindings. This allows the XR runtime to fill in the gaps if new hardware becomes available.

The action map therefore needs to be loaded at startup and can't be changed afterwards. This resource is a container for the entire action map.

### Properties


| [Array](class_array.md#class_Array) | [action_sets](class_openxractionmap.md#class_OpenXRActionMap_property_action_sets) | `[]` |
| --- | --- | --- |
| [Array](class_array.md#class_Array) | [interaction_profiles](class_openxractionmap.md#class_OpenXRActionMap_property_interaction_profiles) | `[]` |

### Methods


| void | [add_action_set](class_openxractionmap.md#class_OpenXRActionMap_method_add_action_set) ( action_set: [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) ) |
| --- | --- |
| void | [add_interaction_profile](class_openxractionmap.md#class_OpenXRActionMap_method_add_interaction_profile) ( interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) ) |
| void | [create_default_action_sets](class_openxractionmap.md#class_OpenXRActionMap_method_create_default_action_sets) ( ) |
| [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) | [find_action_set](class_openxractionmap.md#class_OpenXRActionMap_method_find_action_set) ( name: [String](class_string.md#class_String) ) const |
| [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) | [find_interaction_profile](class_openxractionmap.md#class_OpenXRActionMap_method_find_interaction_profile) ( name: [String](class_string.md#class_String) ) const |
| [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) | [get_action_set](class_openxractionmap.md#class_OpenXRActionMap_method_get_action_set) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_action_set_count](class_openxractionmap.md#class_OpenXRActionMap_method_get_action_set_count) ( ) const |
| [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) | [get_interaction_profile](class_openxractionmap.md#class_OpenXRActionMap_method_get_interaction_profile) ( idx: [int](class_int.md#class_int) ) const |
| [int](class_int.md#class_int) | [get_interaction_profile_count](class_openxractionmap.md#class_OpenXRActionMap_method_get_interaction_profile_count) ( ) const |
| void | [remove_action_set](class_openxractionmap.md#class_OpenXRActionMap_method_remove_action_set) ( action_set: [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) ) |
| void | [remove_interaction_profile](class_openxractionmap.md#class_OpenXRActionMap_method_remove_interaction_profile) ( interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) ) |

---

### Property Descriptions

<span id="class_OpenXRActionMap_property_action_sets"></span>

[Array](class_array.md#class_Array) **action_sets** = `[]` [🔗](class_openxractionmap.md#class_OpenXRActionMap_property_action_sets)

- void **set_action_sets** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_action_sets** ( )

Collection of [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) s that are part of this action map.

---

<span id="class_OpenXRActionMap_property_interaction_profiles"></span>

[Array](class_array.md#class_Array) **interaction_profiles** = `[]` [🔗](class_openxractionmap.md#class_OpenXRActionMap_property_interaction_profiles)

- void **set_interaction_profiles** ( value: [Array](class_array.md#class_Array) )
- [Array](class_array.md#class_Array) **get_interaction_profiles** ( )

Collection of [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) s that are part of this action map.

---

### Method Descriptions

<span id="class_OpenXRActionMap_method_add_action_set"></span>

void **add_action_set** ( action_set: [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) ) [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_add_action_set)

Add an action set.

---

<span id="class_OpenXRActionMap_method_add_interaction_profile"></span>

void **add_interaction_profile** ( interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) ) [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_add_interaction_profile)

Add an interaction profile.

---

<span id="class_OpenXRActionMap_method_create_default_action_sets"></span>

void **create_default_action_sets** ( ) [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_create_default_action_sets)

Setup this action set with our default actions.

---

<span id="class_OpenXRActionMap_method_find_action_set"></span>

[OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) **find_action_set** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_find_action_set)

Retrieve an action set by name.

---

<span id="class_OpenXRActionMap_method_find_interaction_profile"></span>

[OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) **find_interaction_profile** ( name: [String](class_string.md#class_String) ) *const* [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_find_interaction_profile)

Find an interaction profile by its name (path).

---

<span id="class_OpenXRActionMap_method_get_action_set"></span>

[OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) **get_action_set** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_get_action_set)

Retrieve the action set at this index.

---

<span id="class_OpenXRActionMap_method_get_action_set_count"></span>

[int](class_int.md#class_int) **get_action_set_count** ( ) *const* [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_get_action_set_count)

Retrieve the number of actions sets in our action map.

---

<span id="class_OpenXRActionMap_method_get_interaction_profile"></span>

[OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) **get_interaction_profile** ( idx: [int](class_int.md#class_int) ) *const* [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_get_interaction_profile)

Get the interaction profile at this index.

---

<span id="class_OpenXRActionMap_method_get_interaction_profile_count"></span>

[int](class_int.md#class_int) **get_interaction_profile_count** ( ) *const* [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_get_interaction_profile_count)

Retrieve the number of interaction profiles in our action map.

---

<span id="class_OpenXRActionMap_method_remove_action_set"></span>

void **remove_action_set** ( action_set: [OpenXRActionSet](class_openxractionset.md#class_OpenXRActionSet) ) [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_remove_action_set)

Remove an action set.

---

<span id="class_OpenXRActionMap_method_remove_interaction_profile"></span>

void **remove_interaction_profile** ( interaction_profile: [OpenXRInteractionProfile](class_openxrinteractionprofile.md#class_OpenXRInteractionProfile) ) [🔗](class_openxractionmap.md#class_OpenXRActionMap_method_remove_interaction_profile)

Remove an interaction profile.
