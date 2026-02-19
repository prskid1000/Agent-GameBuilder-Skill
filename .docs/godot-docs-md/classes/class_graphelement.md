<span id="class_GraphElement"></span>

## GraphElement

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [GraphFrame](class_graphframe.md#class_GraphFrame), [GraphNode](class_graphnode.md#class_GraphNode)

A container that represents a basic element that can be placed inside a [GraphEdit](class_graphedit.md#class_GraphEdit) control.

### Description

**GraphElement** allows to create custom elements for a [GraphEdit](class_graphedit.md#class_GraphEdit) graph. By default such elements can be selected, resized, and repositioned, but they cannot be connected. For a graph element that allows for connections see [GraphNode](class_graphnode.md#class_GraphNode).

### Properties


| [bool](class_bool.md#class_bool) | [draggable](class_graphelement.md#class_GraphElement_property_draggable) | `true` |
| --- | --- | --- |
| [Vector2](class_vector2.md#class_Vector2) | [position_offset](class_graphelement.md#class_GraphElement_property_position_offset) | `Vector2(0, 0)` |
| [bool](class_bool.md#class_bool) | [resizable](class_graphelement.md#class_GraphElement_property_resizable) | `false` |
| [bool](class_bool.md#class_bool) | [scaling_menus](class_graphelement.md#class_GraphElement_property_scaling_menus) | `false` |
| [bool](class_bool.md#class_bool) | [selectable](class_graphelement.md#class_GraphElement_property_selectable) | `true` |
| [bool](class_bool.md#class_bool) | [selected](class_graphelement.md#class_GraphElement_property_selected) | `false` |

### Theme Properties


| [Texture2D](class_texture2d.md#class_Texture2D) | [resizer](class_graphelement.md#class_GraphElement_theme_icon_resizer) |
| --- | --- |

---

### Signals

<span id="class_GraphElement_signal_delete_request"></span>

**delete_request** ( ) [🔗](class_graphelement.md#class_GraphElement_signal_delete_request)

Emitted when removing the GraphElement is requested.

---

<span id="class_GraphElement_signal_dragged"></span>

**dragged** ( from: [Vector2](class_vector2.md#class_Vector2), to: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_graphelement.md#class_GraphElement_signal_dragged)

Emitted when the GraphElement is dragged.

---

<span id="class_GraphElement_signal_node_deselected"></span>

**node_deselected** ( ) [🔗](class_graphelement.md#class_GraphElement_signal_node_deselected)

Emitted when the GraphElement is deselected.

---

<span id="class_GraphElement_signal_node_selected"></span>

**node_selected** ( ) [🔗](class_graphelement.md#class_GraphElement_signal_node_selected)

Emitted when the GraphElement is selected.

---

<span id="class_GraphElement_signal_position_offset_changed"></span>

**position_offset_changed** ( ) [🔗](class_graphelement.md#class_GraphElement_signal_position_offset_changed)

Emitted when the GraphElement is moved.

---

<span id="class_GraphElement_signal_raise_request"></span>

**raise_request** ( ) [🔗](class_graphelement.md#class_GraphElement_signal_raise_request)

Emitted when displaying the GraphElement over other ones is requested. Happens on focusing (clicking into) the GraphElement.

---

<span id="class_GraphElement_signal_resize_end"></span>

**resize_end** ( new_size: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_graphelement.md#class_GraphElement_signal_resize_end)

Emitted when releasing the mouse button after dragging the resizer handle (see [resizable](class_graphelement.md#class_GraphElement_property_resizable)).

---

<span id="class_GraphElement_signal_resize_request"></span>

**resize_request** ( new_size: [Vector2](class_vector2.md#class_Vector2) ) [🔗](class_graphelement.md#class_GraphElement_signal_resize_request)

Emitted when resizing the GraphElement is requested. Happens on dragging the resizer handle (see [resizable](class_graphelement.md#class_GraphElement_property_resizable)).

---

### Property Descriptions

<span id="class_GraphElement_property_draggable"></span>

[bool](class_bool.md#class_bool) **draggable** = `true` [🔗](class_graphelement.md#class_GraphElement_property_draggable)

- void **set_draggable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_draggable** ( )

If `true`, the user can drag the GraphElement.

---

<span id="class_GraphElement_property_position_offset"></span>

[Vector2](class_vector2.md#class_Vector2) **position_offset** = `Vector2(0, 0)` [🔗](class_graphelement.md#class_GraphElement_property_position_offset)

- void **set_position_offset** ( value: [Vector2](class_vector2.md#class_Vector2) )
- [Vector2](class_vector2.md#class_Vector2) **get_position_offset** ( )

The offset of the GraphElement, relative to the scroll offset of the [GraphEdit](class_graphedit.md#class_GraphEdit).

---

<span id="class_GraphElement_property_resizable"></span>

[bool](class_bool.md#class_bool) **resizable** = `false` [🔗](class_graphelement.md#class_GraphElement_property_resizable)

- void **set_resizable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_resizable** ( )

If `true`, the user can resize the GraphElement.

 **Note:** Dragging the handle will only emit the [resize_request](class_graphelement.md#class_GraphElement_signal_resize_request) and [resize_end](class_graphelement.md#class_GraphElement_signal_resize_end) signals, the GraphElement needs to be resized manually.

---

<span id="class_GraphElement_property_scaling_menus"></span>

[bool](class_bool.md#class_bool) **scaling_menus** = `false` [🔗](class_graphelement.md#class_GraphElement_property_scaling_menus)

- void **set_scaling_menus** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_scaling_menus** ( )

If `true`, [PopupMenu](class_popupmenu.md#class_PopupMenu) s that are descendants of the GraphElement are scaled with the [GraphEdit](class_graphedit.md#class_GraphEdit) zoom.

---

<span id="class_GraphElement_property_selectable"></span>

[bool](class_bool.md#class_bool) **selectable** = `true` [🔗](class_graphelement.md#class_GraphElement_property_selectable)

- void **set_selectable** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_selectable** ( )

If `true`, the user can select the GraphElement.

---

<span id="class_GraphElement_property_selected"></span>

[bool](class_bool.md#class_bool) **selected** = `false` [🔗](class_graphelement.md#class_GraphElement_property_selected)

- void **set_selected** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_selected** ( )

If `true`, the GraphElement is selected.

---

### Theme Property Descriptions

<span id="class_GraphElement_theme_icon_resizer"></span>

[Texture2D](class_texture2d.md#class_Texture2D) **resizer** [🔗](class_graphelement.md#class_GraphElement_theme_icon_resizer)

The icon used for the resizer, visible when [resizable](class_graphelement.md#class_GraphElement_property_resizable) is enabled.
