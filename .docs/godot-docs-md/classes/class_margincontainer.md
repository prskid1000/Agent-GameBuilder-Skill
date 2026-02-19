.. meta::
	:keywords: padding

<span id="class_MarginContainer"></span>

## MarginContainer

**Inherits:** [Container](class_container.md#class_Container) **<** [Control](class_control.md#class_Control) **<** [CanvasItem](class_canvasitem.md#class_CanvasItem) **<** [Node](class_node.md#class_Node) **<** [Object](class_object.md#class_Object)

**Inherited By:** [EditorDock](class_editordock.md#class_EditorDock)

A container that keeps a margin around its child controls.

### Description

**MarginContainer** adds an adjustable margin on each side of its child controls. The margins are added around all children, not around each individual one. To control the **MarginContainer**'s margins, use the `margin_*` theme properties listed below.

 **Note:** The margin sizes are theme overrides, not normal properties. This is an example of how to change them in code:

.. tabs::

```
```

    # This code sample assumes the current script is extending MarginContainer.
    var margin_value = 100
    add_theme_constant_override("margin_top", margin_value)
    add_theme_constant_override("margin_left", margin_value)
    add_theme_constant_override("margin_bottom", margin_value)
    add_theme_constant_override("margin_right", margin_value)

```
```

    // This code sample assumes the current script is extending MarginContainer.
    int marginValue = 100;
    AddThemeConstantOverride("margin_top", marginValue);
    AddThemeConstantOverride("margin_left", marginValue);
    AddThemeConstantOverride("margin_bottom", marginValue);
    AddThemeConstantOverride("margin_right", marginValue);

### Tutorials

- [Using Containers](../tutorials/ui/gui_containers.md)

### Theme Properties


| [int](class_int.md#class_int) | [margin_bottom](class_margincontainer.md#class_MarginContainer_theme_constant_margin_bottom) | `0` |
| --- | --- | --- |
| [int](class_int.md#class_int) | [margin_left](class_margincontainer.md#class_MarginContainer_theme_constant_margin_left) | `0` |
| [int](class_int.md#class_int) | [margin_right](class_margincontainer.md#class_MarginContainer_theme_constant_margin_right) | `0` |
| [int](class_int.md#class_int) | [margin_top](class_margincontainer.md#class_MarginContainer_theme_constant_margin_top) | `0` |

---

### Theme Property Descriptions

<span id="class_MarginContainer_theme_constant_margin_bottom"></span>

[int](class_int.md#class_int) **margin_bottom** = `0` [🔗](class_margincontainer.md#class_MarginContainer_theme_constant_margin_bottom)

Offsets towards the inside direct children of the container by this amount of pixels from the bottom.

---

<span id="class_MarginContainer_theme_constant_margin_left"></span>

[int](class_int.md#class_int) **margin_left** = `0` [🔗](class_margincontainer.md#class_MarginContainer_theme_constant_margin_left)

Offsets towards the inside direct children of the container by this amount of pixels from the left.

---

<span id="class_MarginContainer_theme_constant_margin_right"></span>

[int](class_int.md#class_int) **margin_right** = `0` [🔗](class_margincontainer.md#class_MarginContainer_theme_constant_margin_right)

Offsets towards the inside direct children of the container by this amount of pixels from the right.

---

<span id="class_MarginContainer_theme_constant_margin_top"></span>

[int](class_int.md#class_int) **margin_top** = `0` [🔗](class_margincontainer.md#class_MarginContainer_theme_constant_margin_top)

Offsets towards the inside direct children of the container by this amount of pixels from the top.
