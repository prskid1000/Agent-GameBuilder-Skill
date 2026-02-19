.. meta::
	:keywords: expandable, collapsible, collapse

<span id="class_FoldableGroup"></span>

## FoldableGroup

**Inherits:** [Resource](class_resource.md#class_Resource) **<** [RefCounted](class_refcounted.md#class_RefCounted) **<** [Object](class_object.md#class_Object)

A group of foldable containers that doesn't allow more than one container to be expanded at a time.

### Description

A group of [FoldableContainer](class_foldablecontainer.md#class_FoldableContainer)-derived nodes. Only one container can be expanded at a time.

### Properties


| [bool](class_bool.md#class_bool) | [allow_folding_all](class_foldablegroup.md#class_FoldableGroup_property_allow_folding_all) | `false` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | resource_local_to_scene | `true` (overrides [Resource](class_resource.md#class_Resource_property_resource_local_to_scene)) |

### Methods


| [Array](class_array.md#class_Array)\[[FoldableContainer](class_foldablecontainer.md#class_FoldableContainer)\] | [get_containers](class_foldablegroup.md#class_FoldableGroup_method_get_containers) ( ) const |
| --- | --- |
| [FoldableContainer](class_foldablecontainer.md#class_FoldableContainer) | [get_expanded_container](class_foldablegroup.md#class_FoldableGroup_method_get_expanded_container) ( ) const |

---

### Signals

<span id="class_FoldableGroup_signal_expanded"></span>

**expanded** ( container: [FoldableContainer](class_foldablecontainer.md#class_FoldableContainer) ) [🔗](class_foldablegroup.md#class_FoldableGroup_signal_expanded)

Emitted when one of the containers of the group is expanded.

---

### Property Descriptions

<span id="class_FoldableGroup_property_allow_folding_all"></span>

[bool](class_bool.md#class_bool) **allow_folding_all** = `false` [🔗](class_foldablegroup.md#class_FoldableGroup_property_allow_folding_all)

- void **set_allow_folding_all** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_allow_folding_all** ( )

If `true`, it is possible to fold all containers in this FoldableGroup.

---

### Method Descriptions

<span id="class_FoldableGroup_method_get_containers"></span>

[Array](class_array.md#class_Array)\[[FoldableContainer](class_foldablecontainer.md#class_FoldableContainer)\] **get_containers** ( ) *const* [🔗](class_foldablegroup.md#class_FoldableGroup_method_get_containers)

Returns an [Array](class_array.md#class_Array) of [FoldableContainer](class_foldablecontainer.md#class_FoldableContainer) s that have this as their FoldableGroup (see [FoldableContainer.foldable_group](class_foldablecontainer.md#class_FoldableContainer_property_foldable_group)). This is equivalent to [ButtonGroup](class_buttongroup.md#class_ButtonGroup) but for FoldableContainers.

---

<span id="class_FoldableGroup_method_get_expanded_container"></span>

[FoldableContainer](class_foldablecontainer.md#class_FoldableContainer) **get_expanded_container** ( ) *const* [🔗](class_foldablegroup.md#class_FoldableGroup_method_get_expanded_container)

Returns the current expanded container.
