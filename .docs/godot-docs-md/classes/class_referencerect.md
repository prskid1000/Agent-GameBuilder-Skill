<span id="class_ReferenceRect"></span>

## ReferenceRect

**Inherits:** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A rectangular box for designing UIs.

### Description

A rectangular box that displays only a colored border around its rectangle (see [Control.get_rect()](class_control.md#class_Control_method_get_rect)). It can be used to visualize the extents of a [Control](class_control.md#class_Control) node, for testing purposes.

### Properties


| [Color](class_color.md#class_Color) | [border_color](class_referencerect.md#class_ReferenceRect_property_border_color) | `Color(1, 0, 0, 1)` |
| --- | --- | --- |
| [float](class_float.md#class_float) | [border_width](class_referencerect.md#class_ReferenceRect_property_border_width) | `1.0` |
| [bool](class_bool.md#class_bool) | [editor_only](class_referencerect.md#class_ReferenceRect_property_editor_only) | `true` |

---

### Property Descriptions

<span id="class_ReferenceRect_property_border_color"></span>

[Color](class_color.md#class_Color) **border_color** = `Color(1, 0, 0, 1)` [🔗](class_referencerect.md#class_ReferenceRect_property_border_color)

- void **set_border_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_border_color** ( )

Sets the border color of the **ReferenceRect**.

---

<span id="class_ReferenceRect_property_border_width"></span>

[float](class_float.md#class_float) **border_width** = `1.0` [🔗](class_referencerect.md#class_ReferenceRect_property_border_width)

- void **set_border_width** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_border_width** ( )

Sets the border width of the **ReferenceRect**. The border grows both inwards and outwards with respect to the rectangle box.

---

<span id="class_ReferenceRect_property_editor_only"></span>

[bool](class_bool.md#class_bool) **editor_only** = `true` [🔗](class_referencerect.md#class_ReferenceRect_property_editor_only)

- void **set_editor_only** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **get_editor_only** ( )

If `true`, the **ReferenceRect** will only be visible while in editor. Otherwise, **ReferenceRect** will be visible in the running project.
