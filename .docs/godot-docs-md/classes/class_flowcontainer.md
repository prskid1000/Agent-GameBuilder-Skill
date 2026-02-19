<span id="class_FlowContainer"></span>

## FlowContainer

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [HFlowContainer](class_hflowcontainer.md#class_HFlowContainer), [VFlowContainer](class_vflowcontainer.md#class_VFlowContainer)

A container that arranges its child controls horizontally or vertically and wraps them around at the borders.

### Description

A container that arranges its child controls horizontally or vertically and wraps them around at the borders. This is similar to how text in a book wraps around when no more words can fit on a line.

### Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

### Properties


| [AlignmentMode](class_flowcontainer.md#enum_FlowContainer_AlignmentMode) | [alignment](class_flowcontainer.md#class_FlowContainer_property_alignment) | `0` |
| --- | --- | --- |
| [LastWrapAlignmentMode](class_flowcontainer.md#enum_FlowContainer_LastWrapAlignmentMode) | [last_wrap_alignment](class_flowcontainer.md#class_FlowContainer_property_last_wrap_alignment) | `0` |
| [bool](class_bool.md#class_bool) | [reverse_fill](class_flowcontainer.md#class_FlowContainer_property_reverse_fill) | `false` |
| [bool](class_bool.md#class_bool) | [vertical](class_flowcontainer.md#class_FlowContainer_property_vertical) | `false` |

### Methods


| [int](class_int.md#class_int) | [get_line_count](class_flowcontainer.md#class_FlowContainer_method_get_line_count) ( ) const |
| --- | --- |

### Theme Properties


| [int](class_int.md#class_int) | [h_separation](class_flowcontainer.md#class_FlowContainer_theme_constant_h_separation) | `4` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [v_separation](class_flowcontainer.md#class_FlowContainer_theme_constant_v_separation) | `4` |

---

### Enumerations

<span id="enum_FlowContainer_AlignmentMode"></span>

enum **AlignmentMode**: [🔗](class_flowcontainer.md#enum_FlowContainer_AlignmentMode)

<span id="class_FlowContainer_constant_ALIGNMENT_BEGIN"></span>

[AlignmentMode](class_flowcontainer.md#enum_FlowContainer_AlignmentMode) **ALIGNMENT_BEGIN** = `0`

The child controls will be arranged at the beginning of the container, i.e. top if orientation is vertical, left if orientation is horizontal (right for RTL layout).

<span id="class_FlowContainer_constant_ALIGNMENT_CENTER"></span>

[AlignmentMode](class_flowcontainer.md#enum_FlowContainer_AlignmentMode) **ALIGNMENT_CENTER** = `1`

The child controls will be centered in the container.

<span id="class_FlowContainer_constant_ALIGNMENT_END"></span>

[AlignmentMode](class_flowcontainer.md#enum_FlowContainer_AlignmentMode) **ALIGNMENT_END** = `2`

The child controls will be arranged at the end of the container, i.e. bottom if orientation is vertical, right if orientation is horizontal (left for RTL layout).

---

<span id="enum_FlowContainer_LastWrapAlignmentMode"></span>

enum **LastWrapAlignmentMode**: [🔗](class_flowcontainer.md#enum_FlowContainer_LastWrapAlignmentMode)

<span id="class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_INHERIT"></span>

[LastWrapAlignmentMode](class_flowcontainer.md#enum_FlowContainer_LastWrapAlignmentMode) **LAST_WRAP_ALIGNMENT_INHERIT** = `0`

The last partially filled row or column will wrap aligned to the previous row or column in accordance with [alignment](class_flowcontainer.md#class_FlowContainer_property_alignment).

<span id="class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_BEGIN"></span>

[LastWrapAlignmentMode](class_flowcontainer.md#enum_FlowContainer_LastWrapAlignmentMode) **LAST_WRAP_ALIGNMENT_BEGIN** = `1`

The last partially filled row or column will wrap aligned to the beginning of the previous row or column.

<span id="class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_CENTER"></span>

[LastWrapAlignmentMode](class_flowcontainer.md#enum_FlowContainer_LastWrapAlignmentMode) **LAST_WRAP_ALIGNMENT_CENTER** = `2`

The last partially filled row or column will wrap aligned to the center of the previous row or column.

<span id="class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_END"></span>

[LastWrapAlignmentMode](class_flowcontainer.md#enum_FlowContainer_LastWrapAlignmentMode) **LAST_WRAP_ALIGNMENT_END** = `3`

The last partially filled row or column will wrap aligned to the end of the previous row or column.

---

### Property Descriptions

<span id="class_FlowContainer_property_alignment"></span>

[AlignmentMode](class_flowcontainer.md#enum_FlowContainer_AlignmentMode) **alignment** = `0` [🔗](class_flowcontainer.md#class_FlowContainer_property_alignment)

- void **set_alignment** ( value: [AlignmentMode](class_flowcontainer.md#enum_FlowContainer_AlignmentMode) )
- [AlignmentMode](class_flowcontainer.md#enum_FlowContainer_AlignmentMode) **get_alignment** ( )

The alignment of the container's children (must be one of [ALIGNMENT_BEGIN](class_flowcontainer.md#class_FlowContainer_constant_ALIGNMENT_BEGIN), [ALIGNMENT_CENTER](class_flowcontainer.md#class_FlowContainer_constant_ALIGNMENT_CENTER), or [ALIGNMENT_END](class_flowcontainer.md#class_FlowContainer_constant_ALIGNMENT_END)).

---

<span id="class_FlowContainer_property_last_wrap_alignment"></span>

[LastWrapAlignmentMode](class_flowcontainer.md#enum_FlowContainer_LastWrapAlignmentMode) **last_wrap_alignment** = `0` [🔗](class_flowcontainer.md#class_FlowContainer_property_last_wrap_alignment)

- void **set_last_wrap_alignment** ( value: [LastWrapAlignmentMode](class_flowcontainer.md#enum_FlowContainer_LastWrapAlignmentMode) )
- [LastWrapAlignmentMode](class_flowcontainer.md#enum_FlowContainer_LastWrapAlignmentMode) **get_last_wrap_alignment** ( )

The wrap behavior of the last, partially filled row or column (must be one of [LAST_WRAP_ALIGNMENT_INHERIT](class_flowcontainer.md#class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_INHERIT), [LAST_WRAP_ALIGNMENT_BEGIN](class_flowcontainer.md#class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_BEGIN), [LAST_WRAP_ALIGNMENT_CENTER](class_flowcontainer.md#class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_CENTER), or [LAST_WRAP_ALIGNMENT_END](class_flowcontainer.md#class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_END)).

---

<span id="class_FlowContainer_property_reverse_fill"></span>

[bool](class_bool.md#class_bool) **reverse_fill** = `false` [🔗](class_flowcontainer.md#class_FlowContainer_property_reverse_fill)

- void **set_reverse_fill** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_reverse_fill** ( )

If `true`, reverses fill direction. Horizontal **FlowContainer** s will fill rows bottom to top, vertical **FlowContainer** s will fill columns right to left.

When using a vertical **FlowContainer** with a right to left [Control.layout_direction](class_control.md#class_Control_property_layout_direction), columns will fill left to right instead.

---

<span id="class_FlowContainer_property_vertical"></span>

[bool](class_bool.md#class_bool) **vertical** = `false` [🔗](class_flowcontainer.md#class_FlowContainer_property_vertical)

- void **set_vertical** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_vertical** ( )

If `true`, the **FlowContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HFlowContainer](class_hflowcontainer.md#class_HFlowContainer) and [VFlowContainer](class_vflowcontainer.md#class_VFlowContainer).

---

### Method Descriptions

<span id="class_FlowContainer_method_get_line_count"></span>

[int](class_int.md#class_int) **get_line_count** ( ) *const* [🔗](class_flowcontainer.md#class_FlowContainer_method_get_line_count)

Returns the current line count.

---

### Theme Property Descriptions

<span id="class_FlowContainer_theme_constant_h_separation"></span>

[int](class_int.md#class_int) **h_separation** = `4` [🔗](class_flowcontainer.md#class_FlowContainer_theme_constant_h_separation)

The horizontal separation of child nodes.

---

<span id="class_FlowContainer_theme_constant_v_separation"></span>

[int](class_int.md#class_int) **v_separation** = `4` [🔗](class_flowcontainer.md#class_FlowContainer_theme_constant_v_separation)

The vertical separation of child nodes.
