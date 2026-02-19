<span id="class_Container"></span>

## Container

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [AspectRatioContainer](class_aspectratiocontainer.md#class_AspectRatioContainer), [BoxContainer](class_boxcontainer.md#class_BoxContainer), [CenterContainer](class_centercontainer.md#class_CenterContainer), [EditorProperty](class_editorproperty.md#class_EditorProperty), [FlowContainer](class_flowcontainer.md#class_FlowContainer), [FoldableContainer](class_foldablecontainer.md#class_FoldableContainer), [GraphElement](class_graphelement.md#class_GraphElement), [GridContainer](class_gridcontainer.md#class_GridContainer), [MarginContainer](class_margincontainer.md#class_MarginContainer), [PanelContainer](class_panelcontainer.md#class_PanelContainer), [ScrollContainer](class_scrollcontainer.md#class_ScrollContainer), [SplitContainer](class_splitcontainer.md#class_SplitContainer), [SubViewportContainer](class_subviewportcontainer.md#class_SubViewportContainer), [TabContainer](class_tabcontainer.md#class_TabContainer)

Base class for all GUI containers.

### Description

Base class for all GUI containers. A **Container** automatically arranges its child controls in a certain way. This class can be inherited to make custom container types.

### Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

### Properties


| [bool](class_bool.md#class_bool) | [accessibility_region](class_container.md#class_Container_property_accessibility_region) | `false` |
| --- | --- | --- |
| [MouseFilter](class_control.md#enum_Control_MouseFilter) | mouse_filter | `1` (overrides [Control](class_control.md#class_Control_property_mouse_filter)) |

### Methods


| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_get_allowed_size_flags_horizontal](class_container.md#class_Container_private_method__get_allowed_size_flags_horizontal) ( ) | virtual | const |
| --- | --- | --- | --- |
| [PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) | [_get_allowed_size_flags_vertical](class_container.md#class_Container_private_method__get_allowed_size_flags_vertical) ( ) | virtual | const |
| void | [fit_child_in_rect](class_container.md#class_Container_method_fit_child_in_rect) ( child: [Control](class_control.md#class_Control), rect: [Rect2](class_rect2.md#class_Rect2) ) |
| void | [queue_sort](class_container.md#class_Container_method_queue_sort) ( ) |

---

### Signals

<span id="class_Container_signal_pre_sort_children"></span>

**pre_sort_children** ( ) [🔗](class_container.md#class_Container_signal_pre_sort_children)

Emitted when children are going to be sorted.

---

<span id="class_Container_signal_sort_children"></span>

**sort_children** ( ) [🔗](class_container.md#class_Container_signal_sort_children)

Emitted when sorting the children is needed.

---

### Constants

<span id="class_Container_constant_NOTIFICATION_PRE_SORT_CHILDREN"></span>

**NOTIFICATION_PRE_SORT_CHILDREN** = `50` [🔗](class_container.md#class_Container_constant_NOTIFICATION_PRE_SORT_CHILDREN)

Notification just before children are going to be sorted, in case there's something to process beforehand.

<span id="class_Container_constant_NOTIFICATION_SORT_CHILDREN"></span>

**NOTIFICATION_SORT_CHILDREN** = `51` [🔗](class_container.md#class_Container_constant_NOTIFICATION_SORT_CHILDREN)

Notification for when sorting the children, it must be obeyed immediately.

---

### Property Descriptions

<span id="class_Container_property_accessibility_region"></span>

[bool](class_bool.md#class_bool) **accessibility_region** = `false` [🔗](class_container.md#class_Container_property_accessibility_region)

- void **set_accessibility_region** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_accessibility_region** ( )

If `true`, this container is marked as a region for accessibility. Use [Control.accessibility_name](class_control.md#class_Control_property_accessibility_name) to give the region a descriptive name. Screen readers can navigate between regions using landmark navigation.

---

### Method Descriptions

<span id="class_Container_private_method__get_allowed_size_flags_horizontal"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_get_allowed_size_flags_horizontal** ( ) *virtual* *const* [🔗](class_container.md#class_Container_private_method__get_allowed_size_flags_horizontal)

Implement to return a list of allowed horizontal [SizeFlags](class_control.md#enum_Control_SizeFlags) for child nodes. This doesn't technically prevent the usages of any other size flags, if your implementation requires that. This only limits the options available to the user in the Inspector dock.

 **Note:** Having no size flags is equal to having [Control.SIZE_SHRINK_BEGIN](class_control.md#class_Control_constant_SIZE_SHRINK_BEGIN). As such, this value is always implicitly allowed.

---

<span id="class_Container_private_method__get_allowed_size_flags_vertical"></span>

[PackedInt32Array](class_packedint32array.md#class_PackedInt32Array) **_get_allowed_size_flags_vertical** ( ) *virtual* *const* [🔗](class_container.md#class_Container_private_method__get_allowed_size_flags_vertical)

Implement to return a list of allowed vertical [SizeFlags](class_control.md#enum_Control_SizeFlags) for child nodes. This doesn't technically prevent the usages of any other size flags, if your implementation requires that. This only limits the options available to the user in the Inspector dock.

 **Note:** Having no size flags is equal to having [Control.SIZE_SHRINK_BEGIN](class_control.md#class_Control_constant_SIZE_SHRINK_BEGIN). As such, this value is always implicitly allowed.

---

<span id="class_Container_method_fit_child_in_rect"></span>

void **fit_child_in_rect** ( child: [Control](class_control.md#class_Control), rect: [Rect2](class_rect2.md#class_Rect2) ) [🔗](class_container.md#class_Container_method_fit_child_in_rect)

Fit a child control in a given rect. This is mainly a helper for creating custom container classes.

---

<span id="class_Container_method_queue_sort"></span>

void **queue_sort** ( ) [🔗](class_container.md#class_Container_method_queue_sort)

Queue resort of the contained children. This is called automatically anyway, but can be called upon request.
