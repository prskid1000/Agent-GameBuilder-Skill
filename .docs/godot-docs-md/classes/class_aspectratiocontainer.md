<span id="class_AspectRatioContainer"></span>

## AspectRatioContainer

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

A container that preserves the proportions of its child controls.

### Description

A container type that arranges its child controls in a way that preserves their proportions automatically when the container is resized. Useful when a container has a dynamic size and the child nodes must adjust their sizes accordingly without losing their aspect ratios.

### Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

### Properties


| [AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) | [alignment_horizontal](class_aspectratiocontainer.md#class_AspectRatioContainer_property_alignment_horizontal) | `1` |
| --- | --- | --- |
| [AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) | [alignment_vertical](class_aspectratiocontainer.md#class_AspectRatioContainer_property_alignment_vertical) | `1` |
| [float](class_float.md#class_float) | [ratio](class_aspectratiocontainer.md#class_AspectRatioContainer_property_ratio) | `1.0` |
| [StretchMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_StretchMode) | [stretch_mode](class_aspectratiocontainer.md#class_AspectRatioContainer_property_stretch_mode) | `2` |

---

### Enumerations

<span id="enum_AspectRatioContainer_StretchMode"></span>

enum **StretchMode**: [🔗](class_aspectratiocontainer.md#enum_AspectRatioContainer_StretchMode)

<span id="class_AspectRatioContainer_constant_STRETCH_WIDTH_CONTROLS_HEIGHT"></span>

[StretchMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_StretchMode) **STRETCH_WIDTH_CONTROLS_HEIGHT** = `0`

The height of child controls is automatically adjusted based on the width of the container.

<span id="class_AspectRatioContainer_constant_STRETCH_HEIGHT_CONTROLS_WIDTH"></span>

[StretchMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_StretchMode) **STRETCH_HEIGHT_CONTROLS_WIDTH** = `1`

The width of child controls is automatically adjusted based on the height of the container.

<span id="class_AspectRatioContainer_constant_STRETCH_FIT"></span>

[StretchMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_StretchMode) **STRETCH_FIT** = `2`

The bounding rectangle of child controls is automatically adjusted to fit inside the container while keeping the aspect ratio.

<span id="class_AspectRatioContainer_constant_STRETCH_COVER"></span>

[StretchMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_StretchMode) **STRETCH_COVER** = `3`

The width and height of child controls is automatically adjusted to make their bounding rectangle cover the entire area of the container while keeping the aspect ratio.

When the bounding rectangle of child controls exceed the container's size and [Control.clip_contents](class_control.md#class_Control_property_clip_contents) is enabled, this allows to show only the container's area restricted by its own bounding rectangle.

---

<span id="enum_AspectRatioContainer_AlignmentMode"></span>

enum **AlignmentMode**: [🔗](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode)

<span id="class_AspectRatioContainer_constant_ALIGNMENT_BEGIN"></span>

[AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) **ALIGNMENT_BEGIN** = `0`

Aligns child controls with the beginning (left or top) of the container.

<span id="class_AspectRatioContainer_constant_ALIGNMENT_CENTER"></span>

[AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) **ALIGNMENT_CENTER** = `1`

Aligns child controls with the center of the container.

<span id="class_AspectRatioContainer_constant_ALIGNMENT_END"></span>

[AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) **ALIGNMENT_END** = `2`

Aligns child controls with the end (right or bottom) of the container.

---

### Property Descriptions

<span id="class_AspectRatioContainer_property_alignment_horizontal"></span>

[AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) **alignment_horizontal** = `1` [🔗](class_aspectratiocontainer.md#class_AspectRatioContainer_property_alignment_horizontal)

- void **set_alignment_horizontal** ( value: [AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) )
- [AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) **get_alignment_horizontal** ( )

Specifies the horizontal relative position of child controls.

---

<span id="class_AspectRatioContainer_property_alignment_vertical"></span>

[AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) **alignment_vertical** = `1` [🔗](class_aspectratiocontainer.md#class_AspectRatioContainer_property_alignment_vertical)

- void **set_alignment_vertical** ( value: [AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) )
- [AlignmentMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_AlignmentMode) **get_alignment_vertical** ( )

Specifies the vertical relative position of child controls.

---

<span id="class_AspectRatioContainer_property_ratio"></span>

[float](class_float.md#class_float) **ratio** = `1.0` [🔗](class_aspectratiocontainer.md#class_AspectRatioContainer_property_ratio)

- void **set_ratio** ( value: [float](class_float.md#class_float) )
- [float](class_float.md#class_float) **get_ratio** ( )

The aspect ratio to enforce on child controls. This is the width divided by the height. The ratio depends on the [stretch_mode](class_aspectratiocontainer.md#class_AspectRatioContainer_property_stretch_mode).

---

<span id="class_AspectRatioContainer_property_stretch_mode"></span>

[StretchMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_StretchMode) **stretch_mode** = `2` [🔗](class_aspectratiocontainer.md#class_AspectRatioContainer_property_stretch_mode)

- void **set_stretch_mode** ( value: [StretchMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_StretchMode) )
- [StretchMode](class_aspectratiocontainer.md#enum_AspectRatioContainer_StretchMode) **get_stretch_mode** ( )

The stretch mode used to align child controls.
