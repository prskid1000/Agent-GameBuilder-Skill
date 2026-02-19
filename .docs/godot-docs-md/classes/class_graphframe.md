<span id="class_GraphFrame"></span>

## GraphFrame

**Inherits:** [GraphElement](class_graphelement.md#class_GraphElement) **<** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

GraphFrame is a special [GraphElement](class_graphelement.md#class_GraphElement) that can be used to organize other [GraphElement](class_graphelement.md#class_GraphElement) s inside a [GraphEdit](class_graphedit.md#class_GraphEdit).

### Description

GraphFrame is a special [GraphElement](class_graphelement.md#class_GraphElement) to which other [GraphElement](class_graphelement.md#class_GraphElement) s can be attached. It can be configured to automatically resize to enclose all attached [GraphElement](class_graphelement.md#class_GraphElement) s. If the frame is moved, all the attached [GraphElement](class_graphelement.md#class_GraphElement) s inside it will be moved as well.

A GraphFrame is always kept behind the connection layer and other [GraphElement](class_graphelement.md#class_GraphElement) s inside a [GraphEdit](class_graphedit.md#class_GraphEdit).

### Properties


| [bool](class_bool.md#class_bool) | [autoshrink_enabled](class_graphframe.md#class_GraphFrame_property_autoshrink_enabled) | `true` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [autoshrink_margin](class_graphframe.md#class_GraphFrame_property_autoshrink_margin) | `40` |
| [int](class_int.md#class_int) | [drag_margin](class_graphframe.md#class_GraphFrame_property_drag_margin) | `16` |
| [MouseFilter](class_control.md#enum_Control_MouseFilter) | mouse_filter | `0` (overrides [Control](class_control.md#class_Control_property_mouse_filter)) |
| [Color](class_color.md#class_Color) | [tint_color](class_graphframe.md#class_GraphFrame_property_tint_color) | `Color(0.3, 0.3, 0.3, 0.75)` |
| [bool](class_bool.md#class_bool) | [tint_color_enabled](class_graphframe.md#class_GraphFrame_property_tint_color_enabled) | `false` |
| [String](class_string.md#class_String) | [title](class_graphframe.md#class_GraphFrame_property_title) | `""` |

### Methods


| [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) | [get_titlebar_hbox](class_graphframe.md#class_GraphFrame_method_get_titlebar_hbox) ( ) |
| --- | --- |

### Theme Properties


| [Color](class_color.md#class_Color) | [resizer_color](class_graphframe.md#class_GraphFrame_theme_color_resizer_color) | `Color(0.875, 0.875, 0.875, 1)` |
| --- | --- | --- |
| [StyleBox](class_stylebox.md#class_StyleBox) | [panel](class_graphframe.md#class_GraphFrame_theme_style_panel) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [panel_selected](class_graphframe.md#class_GraphFrame_theme_style_panel_selected) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [titlebar](class_graphframe.md#class_GraphFrame_theme_style_titlebar) |
| [StyleBox](class_stylebox.md#class_StyleBox) | [titlebar_selected](class_graphframe.md#class_GraphFrame_theme_style_titlebar_selected) |

---

### Signals

<span id="class_GraphFrame_signal_autoshrink_changed"></span>

**autoshrink_changed** ( ) [🔗](class_graphframe.md#class_GraphFrame_signal_autoshrink_changed)

Emitted when [autoshrink_enabled](class_graphframe.md#class_GraphFrame_property_autoshrink_enabled) or [autoshrink_margin](class_graphframe.md#class_GraphFrame_property_autoshrink_margin) changes.

---

### Property Descriptions

<span id="class_GraphFrame_property_autoshrink_enabled"></span>

[bool](class_bool.md#class_bool) **autoshrink_enabled** = `true` [🔗](class_graphframe.md#class_GraphFrame_property_autoshrink_enabled)

- void **set_autoshrink_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_autoshrink_enabled** ( )

If `true`, the frame's rect will be adjusted automatically to enclose all attached [GraphElement](class_graphelement.md#class_GraphElement) s.

---

<span id="class_GraphFrame_property_autoshrink_margin"></span>

[int](class_int.md#class_int) **autoshrink_margin** = `40` [🔗](class_graphframe.md#class_GraphFrame_property_autoshrink_margin)

- void **set_autoshrink_margin** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_autoshrink_margin** ( )

The margin around the attached nodes that is used to calculate the size of the frame when [autoshrink_enabled](class_graphframe.md#class_GraphFrame_property_autoshrink_enabled) is `true`.

---

<span id="class_GraphFrame_property_drag_margin"></span>

[int](class_int.md#class_int) **drag_margin** = `16` [🔗](class_graphframe.md#class_GraphFrame_property_drag_margin)

- void **set_drag_margin** ( value: [int](class_int.md#class_int) )
- [int](class_int.md#class_int) **get_drag_margin** ( )

The margin inside the frame that can be used to drag the frame.

---

<span id="class_GraphFrame_property_tint_color"></span>

[Color](class_color.md#class_Color) **tint_color** = `Color(0.3, 0.3, 0.3, 0.75)` [🔗](class_graphframe.md#class_GraphFrame_property_tint_color)

- void **set_tint_color** ( value: [Color](class_color.md#class_Color) )
- [Color](class_color.md#class_Color) **get_tint_color** ( )

The color of the frame when [tint_color_enabled](class_graphframe.md#class_GraphFrame_property_tint_color_enabled) is `true`.

---

<span id="class_GraphFrame_property_tint_color_enabled"></span>

[bool](class_bool.md#class_bool) **tint_color_enabled** = `false` [🔗](class_graphframe.md#class_GraphFrame_property_tint_color_enabled)

- void **set_tint_color_enabled** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_tint_color_enabled** ( )

If `true`, the tint color will be used to tint the frame.

---

<span id="class_GraphFrame_property_title"></span>

[String](class_string.md#class_String) **title** = `""` [🔗](class_graphframe.md#class_GraphFrame_property_title)

- void **set_title** ( value: [String](class_string.md#class_String) )
- [String](class_string.md#class_String) **get_title** ( )

Title of the frame.

---

### Method Descriptions

<span id="class_GraphFrame_method_get_titlebar_hbox"></span>

[HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) **get_titlebar_hbox** ( ) [🔗](class_graphframe.md#class_GraphFrame_method_get_titlebar_hbox)

Returns the [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) used for the title bar, only containing a [Label](class_label.md#class_Label) for displaying the title by default.

This can be used to add custom controls to the title bar such as option or close buttons.

---

### Theme Property Descriptions

<span id="class_GraphFrame_theme_color_resizer_color"></span>

[Color](class_color.md#class_Color) **resizer_color** = `Color(0.875, 0.875, 0.875, 1)` [🔗](class_graphframe.md#class_GraphFrame_theme_color_resizer_color)

The color modulation applied to the resizer icon.

---

<span id="class_GraphFrame_theme_style_panel"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **panel** [🔗](class_graphframe.md#class_GraphFrame_theme_style_panel)

The default [StyleBox](class_stylebox.md#class_StyleBox) used for the background of the **GraphFrame**.

---

<span id="class_GraphFrame_theme_style_panel_selected"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **panel_selected** [🔗](class_graphframe.md#class_GraphFrame_theme_style_panel_selected)

The [StyleBox](class_stylebox.md#class_StyleBox) used for the background of the **GraphFrame** when it is selected.

---

<span id="class_GraphFrame_theme_style_titlebar"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **titlebar** [🔗](class_graphframe.md#class_GraphFrame_theme_style_titlebar)

The [StyleBox](class_stylebox.md#class_StyleBox) used for the title bar of the **GraphFrame**.

---

<span id="class_GraphFrame_theme_style_titlebar_selected"></span>

[StyleBox](class_stylebox.md#class_StyleBox) **titlebar_selected** [🔗](class_graphframe.md#class_GraphFrame_theme_style_titlebar_selected)

The [StyleBox](class_stylebox.md#class_StyleBox) used for the title bar of the **GraphFrame** when it is selected.
