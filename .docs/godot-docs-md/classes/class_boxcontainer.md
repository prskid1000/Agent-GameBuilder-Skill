<span id="class_BoxContainer"></span>

## BoxContainer

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer), [VBoxContainer](class_vboxcontainer.md#class_VBoxContainer)

A container that arranges its child controls horizontally or vertically.

### Description

A container that arranges its child controls horizontally or vertically, rearranging them automatically when their minimum size changes.

### Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

### Properties


| [AlignmentMode](class_boxcontainer.md#enum_BoxContainer_AlignmentMode) | [alignment](class_boxcontainer.md#class_BoxContainer_property_alignment) | `0` |
| --- | --- | --- |
| [bool](class_bool.md#class_bool) | [vertical](class_boxcontainer.md#class_BoxContainer_property_vertical) | `false` |

### Methods


| [Control](class_control.md#class_Control) | [add_spacer](class_boxcontainer.md#class_BoxContainer_method_add_spacer) ( begin: [bool](class_bool.md#class_bool) ) |
| --- | --- |

### Theme Properties


| [int](class_int.md#class_int) | [separation](class_boxcontainer.md#class_BoxContainer_theme_constant_separation) | `4` |
| --- | --- | --- |

---

### Enumerations

<span id="enum_BoxContainer_AlignmentMode"></span>

enum **AlignmentMode**: [🔗](class_boxcontainer.md#enum_BoxContainer_AlignmentMode)

<span id="class_BoxContainer_constant_ALIGNMENT_BEGIN"></span>

[AlignmentMode](class_boxcontainer.md#enum_BoxContainer_AlignmentMode) **ALIGNMENT_BEGIN** = `0`

The child controls will be arranged at the beginning of the container, i.e. top if orientation is vertical, left if orientation is horizontal (right for RTL layout).

<span id="class_BoxContainer_constant_ALIGNMENT_CENTER"></span>

[AlignmentMode](class_boxcontainer.md#enum_BoxContainer_AlignmentMode) **ALIGNMENT_CENTER** = `1`

The child controls will be centered in the container.

<span id="class_BoxContainer_constant_ALIGNMENT_END"></span>

[AlignmentMode](class_boxcontainer.md#enum_BoxContainer_AlignmentMode) **ALIGNMENT_END** = `2`

The child controls will be arranged at the end of the container, i.e. bottom if orientation is vertical, right if orientation is horizontal (left for RTL layout).

---

### Property Descriptions

<span id="class_BoxContainer_property_alignment"></span>

[AlignmentMode](class_boxcontainer.md#enum_BoxContainer_AlignmentMode) **alignment** = `0` [🔗](class_boxcontainer.md#class_BoxContainer_property_alignment)

- void **set_alignment** ( value: [AlignmentMode](class_boxcontainer.md#enum_BoxContainer_AlignmentMode) )
- [AlignmentMode](class_boxcontainer.md#enum_BoxContainer_AlignmentMode) **get_alignment** ( )

The alignment of the container's children (must be one of [ALIGNMENT_BEGIN](class_boxcontainer.md#class_BoxContainer_constant_ALIGNMENT_BEGIN), [ALIGNMENT_CENTER](class_boxcontainer.md#class_BoxContainer_constant_ALIGNMENT_CENTER), or [ALIGNMENT_END](class_boxcontainer.md#class_BoxContainer_constant_ALIGNMENT_END)).

---

<span id="class_BoxContainer_property_vertical"></span>

[bool](class_bool.md#class_bool) **vertical** = `false` [🔗](class_boxcontainer.md#class_BoxContainer_property_vertical)

- void **set_vertical** ( value: [bool](class_bool.md#class_bool) )
- [bool](class_bool.md#class_bool) **is_vertical** ( )

If `true`, the **BoxContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HBoxContainer](class_hboxcontainer.md#class_HBoxContainer) and [VBoxContainer](class_vboxcontainer.md#class_VBoxContainer).

---

### Method Descriptions

<span id="class_BoxContainer_method_add_spacer"></span>

[Control](class_control.md#class_Control) **add_spacer** ( begin: [bool](class_bool.md#class_bool) ) [🔗](class_boxcontainer.md#class_BoxContainer_method_add_spacer)

Adds a [Control](class_control.md#class_Control) node to the box as a spacer. If `begin` is `true`, it will insert the [Control](class_control.md#class_Control) node in front of all other children.

---

### Theme Property Descriptions

<span id="class_BoxContainer_theme_constant_separation"></span>

[int](class_int.md#class_int) **separation** = `4` [🔗](class_boxcontainer.md#class_BoxContainer_theme_constant_separation)

The space between the **BoxContainer**'s elements, in pixels.
