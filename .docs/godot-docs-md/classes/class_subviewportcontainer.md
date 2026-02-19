<span id="class_SubViewportContainer"></span>

## SubViewportContainer

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A container used for displaying the contents of a [SubViewport](class_subviewport.md#class_SubViewport).

### Description

A container that displays the contents of underlying [SubViewport](class_subviewport.md#class_SubViewport) child nodes. It uses the combined size of the [SubViewport](class_subviewport.md#class_SubViewport) s as minimum size, unless [stretch](class_subviewportcontainer.md#class_SubViewportContainer_property_stretch) is enabled.

 **Note:** Changing a **SubViewportContainer**'s [Control.scale](class_control.md#class_Control_property_scale) will cause its contents to appear distorted. To change its visual size without causing distortion, adjust the node's margins instead (if it's not already in a container).

 **Note:** The **SubViewportContainer** forwards mouse-enter and mouse-exit notifications to its sub-viewports.

### Properties


| [FocusMode](class_control.md#enum_Control_FocusMode) | focus_mode | `1` (overrides [Control](class_control.md#class_Control_property_focus_mode)) |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [mouse_target](class_subviewportcontainer.md#class_SubViewportContainer_property_mouse_target) | `false` |
| [bool](class_bool.md#class_bool) | [stretch](class_subviewportcontainer.md#class_SubViewportContainer_property_stretch) | `false` |
| [int](class_int.md#class_int) | [stretch_shrink](class_subviewportcontainer.md#class_SubViewportContainer_property_stretch_shrink) | `1` |

### Methods


| [bool](class_bool.md#class_bool) | [_propagate_input_event](class_subviewportcontainer.md#class_SubViewportContainer_private_method__propagate_input_event) ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) | virtual | const |
| --- | --- | --- | --- |

---

### Property Descriptions

<span id="class_SubViewportContainer_property_mouse_target"></span>

[bool](class_bool.md#class_bool) **mouse_target** = `false` [🔗](class_subviewportcontainer.md#class_SubViewportContainer_property_mouse_target)

- void **set_mouse_target** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_mouse_target_enabled** ( )

Configure, if either the **SubViewportContainer** or alternatively the [Control](class_control.md#class_Control) nodes of its [SubViewport](class_subviewport.md#class_SubViewport) children should be available as targets of mouse-related functionalities, like identifying the drop target in drag-and-drop operations or cursor shape of hovered [Control](class_control.md#class_Control) node.

If `false`, the [Control](class_control.md#class_Control) nodes inside its [SubViewport](class_subviewport.md#class_SubViewport) children are considered as targets.

If `true`, the **SubViewportContainer** itself will be considered as a target.

---

<span id="class_SubViewportContainer_property_stretch"></span>

[bool](class_bool.md#class_bool) **stretch** = `false` [🔗](class_subviewportcontainer.md#class_SubViewportContainer_property_stretch)

- void **set_stretch** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_stretch_enabled** ( )

If `true`, the sub-viewport will be automatically resized to the control's size.

 **Note:** If `true`, this will prohibit changing [SubViewport.size](class_subviewport.md#class_SubViewport_property_size) of its children manually.

---

<span id="class_SubViewportContainer_property_stretch_shrink"></span>

[int](class_int.md#class_int) **stretch_shrink** = `1` [🔗](class_subviewportcontainer.md#class_SubViewportContainer_property_stretch_shrink)

- void **set_stretch_shrink** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_stretch_shrink** ( )

Divides the sub-viewport's effective resolution by this value while preserving its scale. This can be used to speed up rendering.

For example, a 1280×720 sub-viewport with [stretch_shrink](class_subviewportcontainer.md#class_SubViewportContainer_property_stretch_shrink) set to `2` will be rendered at 640×360 while occupying the same size in the container.

 **Note:** [stretch](class_subviewportcontainer.md#class_SubViewportContainer_property_stretch) must be `true` for this property to work.

---

### Method Descriptions

<span id="class_SubViewportContainer_private_method__propagate_input_event"></span>

[bool](class_bool.md#class_bool) **_propagate_input_event** ( event: [InputEvent](class_inputevent.md#class_InputEvent) ) *virtual* *const* [🔗](class_subviewportcontainer.md#class_SubViewportContainer_private_method__propagate_input_event)

**Experimental:** This method may be changed or removed in future versions.

Virtual method to be implemented by the user. If it returns `true`, the `event` is propagated to [SubViewport](class_subviewport.md#class_SubViewport) children. Propagation doesn't happen if it returns `false`. If the function is not implemented, all events are propagated to SubViewports.
